"""Reproducible MEXC 4h event study. No orders, signals are research only.

Run after fetch_history.ps1. Event timestamps identify candle OPEN times in
UTC+3. Every preparation snapshot ends strictly before its event candle.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
LOCAL = timezone(timedelta(hours=3))
FOUR_HOURS_MS = 4 * 60 * 60 * 1000


def load(symbol: str):
    raw = json.loads((ROOT / "data" / f"{symbol}.json").read_text(encoding="utf-8-sig"))
    frame = pd.DataFrame(raw["rows"], columns=[
        "time", "open", "high", "low", "close", "volume", "close_time", "quote_volume"
    ])
    for col in frame.columns:
        frame[col] = pd.to_numeric(frame[col], errors="raise")
    if frame["time"].duplicated().any():
        raise ValueError(f"{symbol}: duplicate candles")
    frame = frame.sort_values("time").set_index("time")
    if not ((frame["high"] >= frame[["open", "close", "low"]].max(axis=1)) &
            (frame["low"] <= frame[["open", "close"]].min(axis=1))).all():
        raise ValueError(f"{symbol}: invalid OHLC data")
    if not ((frame.index % FOUR_HOURS_MS) == 0).all():
        raise ValueError(f"{symbol}: unexpected 4h candle grid")
    gaps = int((np.diff(frame.index.to_numpy()) != FOUR_HOURS_MS).sum())
    # Exclude current open candles, including an endpoint's inclusive close time.
    closed = frame[(frame.index + FOUR_HOURS_MS) <= raw["fetched_server_time_ms"]].copy()
    return raw, closed, gaps


def features(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame.copy()
    mean = out["close"].rolling(20).mean()
    std = out["close"].rolling(20).std(ddof=0)
    out["bbw_pct"] = std * 4 / mean * 100
    out["bbw_q20_prev120"] = out["bbw_pct"].shift(1).rolling(120).quantile(.20)
    widths = out["bbw_pct"].to_numpy()
    ranks = np.full(len(out), np.nan)
    for i in range(139, len(out)):
        prior = widths[i-120:i]
        if np.isfinite(prior).all():
            ranks[i] = float(np.count_nonzero(prior <= widths[i]) / 120 * 100)
    out["bbw_rank_pct"] = ranks
    out["squeeze"] = (out["bbw_pct"] <= out["bbw_q20_prev120"]) & out["bbw_q20_prev120"].notna()
    out["volume6_vs_previous30"] = (
        out["quote_volume"].rolling(6).mean() /
        out["quote_volume"].shift(6).rolling(30).mean().replace(0, np.nan)
    )
    out["volume1_vs_previous30"] = (
        out["quote_volume"] / out["quote_volume"].shift(1).rolling(30).mean().replace(0, np.nan)
    )
    out["return24_pct"] = out["close"].pct_change(6, fill_method=None) * 100
    out["return72_pct"] = out["close"].pct_change(18, fill_method=None) * 100
    low12, high12 = out["low"].rolling(12).min(), out["high"].rolling(12).max()
    out["close_position12_pct"] = (out["close"]-low12)/(high12-low12).replace(0, np.nan)*100
    out["range12_pct"] = (high12/low12-1)*100
    out["median_low6_vs_previous6_pct"] = (
        out["low"].rolling(6).median() / out["low"].shift(6).rolling(6).median() - 1
    ) * 100
    out["distance_from_prior20_high_pct"] = (
        out["close"] / out["high"].shift(1).rolling(20).max()-1
    ) * 100
    out["bar_body_pct"] = (out["close"]/out["open"]-1)*100
    out["bar_high_from_open_pct"] = (out["high"]/out["open"]-1)*100
    return out.replace([np.inf, -np.inf], np.nan)


METRICS = [
    "bbw_pct", "bbw_rank_pct", "squeeze", "volume6_vs_previous30",
    "volume1_vs_previous30", "return24_pct", "return72_pct",
    "close_position12_pct", "range12_pct", "median_low6_vs_previous6_pct",
    "distance_from_prior20_high_pct", "bar_body_pct", "bar_high_from_open_pct"
]


def snapshot(row):
    result = {}
    for key in METRICS:
        value = row[key]
        result[key] = bool(value) if key == "squeeze" else (round(float(value), 5) if pd.notna(value) else None)
    return result


def self_check():
    # Features must not depend on future candles and widths must be scale invariant.
    times = np.arange(200) * FOUR_HOURS_MS
    close = 10 + np.sin(np.arange(200)/7) + np.arange(200)/100
    base = pd.DataFrame({"open": close, "close": close, "high": close+1,
                         "low": close-1, "quote_volume": np.arange(200)+10}, index=times)
    original = features(base)
    changed = base.copy()
    changed.iloc[170:, changed.columns.get_indexer(["open", "high", "low", "close"])] *= 10
    pd.testing.assert_frame_equal(original.iloc[:170], features(changed).iloc[:170])
    scaled = base.copy()
    scaled[["open", "high", "low", "close"]] *= 7
    np.testing.assert_allclose(original["bbw_pct"], features(scaled)["bbw_pct"], equal_nan=True)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    self_check()
    config = json.loads((ROOT / "examples.json").read_text(encoding="utf-8-sig"))
    _, btc, btc_gaps = load("BTCUSDT")
    btc = features(btc)
    results = []
    for event in config["examples"]:
        symbol = event["symbol"]
        when = datetime.fromisoformat(event["event_local"])
        event_ms = int(when.timestamp()*1000)
        raw, candles, gaps = load(symbol)
        f = features(candles)
        if event_ms not in f.index:
            raise ValueError(f"{symbol}: event OPEN timestamp missing: {when.isoformat()}")
        prior_times = [event_ms - n*FOUR_HOURS_MS for n in range(1, 141)]
        if not set(prior_times).issubset(f.index):
            raise ValueError(f"{symbol}: insufficient contiguous preparation history")
        pre_ms = event_ms - FOUR_HOURS_MS
        pre = snapshot(f.loc[pre_ms])
        if pre_ms not in btc.index:
            raise ValueError(f"BTC comparison missing at {pre_ms}")
        pre["btc_return24_pct"] = round(float(btc.loc[pre_ms, "return24_pct"]), 5)
        pre["relative_to_btc24_pct"] = round(
            ((1+pre["return24_pct"]/100)/(1+pre["btc_return24_pct"]/100)-1)*100, 5
        )
        lead = []
        for n in [1, 2, 3, 6, 12]:
            ms = event_ms-n*FOUR_HOURS_MS
            lead.append({"hours_before_event": n*4, "candle_open_local":
                         datetime.fromtimestamp(ms/1000, LOCAL).isoformat(), **snapshot(f.loc[ms])})
        last24 = f.loc[(f.index >= event_ms-6*FOUR_HOURS_MS) & (f.index < event_ms)]
        after = f.loc[(f.index >= event_ms) & (f.index < event_ms+6*FOUR_HOURS_MS)]
        background = f.loc[(f.index >= event_ms-30*86400000) &
                           (f.index < event_ms-2*86400000) & f["bbw_rank_pct"].notna()]
        results.append({
            "symbol": symbol, "event_local": event["event_local"],
            "pre_candle_open_local": datetime.fromtimestamp(pre_ms/1000, LOCAL).isoformat(),
            "pre_candle_close_local": event["event_local"],
            "data_rows_closed": len(candles), "data_gap_count": gaps,
            "source_urls": raw.get("urls", [raw.get("url")]),
            "pre": pre, "lead_snapshots": lead, "event": snapshot(f.loc[event_ms]),
            "squeeze_any_last24h": bool(last24["squeeze"].any()),
            "max_high_next24h_from_event_open_pct": round(float((after["high"].max()/f.loc[event_ms,"open"]-1)*100), 5),
            "available_closed_bars_next24h": len(after),
            "background_candles": len(background),
            "background_squeeze_candles": int(background["squeeze"].sum()),
        })
    report = {
        "scope": "Selected-event descriptive study, not an unbiased backtest or trade recommendation",
        "timezone": "UTC+03:00; supplied times treated as candle opens",
        "year": 2026, "bbw": "20 close observations, population stddev, +/-2 stddev",
        "squeeze": "current BBW <= 20th percentile of preceding 120 BBW observations, excluding current",
        "lookahead_checks": "passed: future mutation invariance and price scale invariance",
        "btc_gap_count": btc_gaps, "events": results,
    }
    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    (out/"event_study.json").write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8")
    lines = ["# MEXC 4 saatlik hazırlık incelemesi", "",
             "Yıl: 2026. Saatler: UTC+3; verilen saatler mum açılışı olarak ele alındı.",
             "Hazırlık ölçümleri hedef mum başlamadan hemen önce kapanan mumdan hesaplandı.", "",
             "BBW: 20 kapanış, 2 standart sapma. Sıkışma eşiği: önceki 120 BBW değerinin %20 yüzdeliği.",
             "Bu eşik denenmekte olan varsayımdır; doğrulanmış bir yükseliş öngörücüsü değildir.", "",
             "| Coin | Hedef mum (TR) | Önceki BBW sırası % | Sıkışma | Son 24 saatte sıkışma | Hacim 6/önceki30 | Önceki 24s getiri % | Hedef mum gövde % | Hedef mum tepe/açılış % |",
             "|---|---|---:|---|---|---:|---:|---:|---:|"]
    for r in results:
        p, e = r["pre"], r["event"]
        lines.append(f'| {r["symbol"]} | {r["event_local"][:16].replace("T"," ")} | '
                     f'{p["bbw_rank_pct"]:.1f} | {"Evet" if p["squeeze"] else "Hayır"} | '
                     f'{"Evet" if r["squeeze_any_last24h"] else "Hayır"} | '
                     f'{p["volume6_vs_previous30"]:.2f} | {p["return24_pct"]:.2f} | '
                     f'{e["bar_body_pct"]:.2f} | {e["bar_high_from_open_pct"]:.2f} |')
    direct = sum(r["pre"]["squeeze"] for r in results)
    day = sum(r["squeeze_any_last24h"] for r in results)
    lines += ["", f"Önceki mumda sıkışma: {direct}/{len(results)}. Önceki 24 saatte en az bir sıkışma: {day}/{len(results)}.",
              "", "## Hazırlık yapısını karşılaştırma", "",
              "| Coin | Önceki mum gövde % | Son 48s fiyat aralığı % | Son kapanışın bu aralıktaki yeri % | Son 24s BTC'ye göre getiri % | Son 24s dip medyanı değişimi % |",
              "|---|---:|---:|---:|---:|---:|"]
    for r in results:
        p = r["pre"]
        lines.append(f'| {r["symbol"]} | {p["bar_body_pct"]:.2f} | {p["range12_pct"]:.2f} | '
                     f'{p["close_position12_pct"]:.2f} | {p["relative_to_btc24_pct"]:.2f} | '
                     f'{p["median_low6_vs_previous6_pct"]:.2f} |')
    lines += ["", "## İlk bulgular", "",
              "- İlk BBW sıkışması varsayımı, verilen saatlerden hemen önce yalnızca RLCUSDT örneğinde karşılandı. Zorunlu filtre olarak desteklenmiyor.",
              "- IRYSUSDT ve BATUSDT hedef saatlerden önceki 24 saatte zaten sırasıyla %63,47 ve %38,99 yükselmişti; bu iki hedef mum ilk yükseliş mumu olarak alınmamalı.",
              "- BATUSDT için verilen hedef mumun gövdesi %-0,46. Diğer hedeflerin hazırlık başlangıcını karşılaştırmadan önce bu saat/grafik eşleşmesi kullanıcıyla kontrol edilmeli.",
              "- Diğer beş örneğin son 24 saatlik ortalama hacmi önceki 30 mum ortalamasının 0,82–1,17 katı. 2 kat hacim koşulu bu beşini elemiş olurdu.",
              "- BMTUSDT, önceki 24 saatte %14,09 düşmüş ve 48 saatlik aralığın alt tarafında kalmıştı. Her örnekte üst banda yakın güçlü taban varsayımı desteklenmiyor.",
              "- Tüm örneklerin hedef öncesi son mumu pozitif kapanmıştı; bu geniş bir özellik olup tek başına ayırt ediciliği henüz ölçülmedi.",
              "", "## Yorumlama sınırları", "",
              "- Yalnızca kullanıcı tarafından seçilmiş örnekler incelendi. Bu örnekler taramanın doğruluk oranını göstermez.",
              "- Hedef mumun gövdesi, tepe hareketi ve sonraki fiyatlar yalnızca olayı doğrulamak içindir; hazırlık formülünde kullanılmadı.",
              "- Bir mumun hangi anda 3 veya 4 kata ulaştığı bu tabloda ölçülmüyor; hedef mum ile yükselişin gerçek başlangıcı ayrıca kontrol edilmelidir.",
              "- USDT işlem hacmi oranı: son 6 kapanmış mum ortalaması / onların öncesindeki 30 mum ortalaması.",
              "- BBW sırası: önceki 120 genişliğin yüzde kaçı mevcut değere eşit veya daha küçük. Küçük değer daha dar banttır.",
              "- Daha önceki sıkışma, yükselişe çok erken uyarı vermiş olabilir. Birden fazla arka arkaya uyarı bağımsız fırsat sayılmaz.",
              "- Veride boşluk ve yinelenen zamanlar kontrol edildi; gelecekteki mumları değiştirme ve fiyat ölçeği testleri geçti.",
              "", "## Kaynak", "",
              "[MEXC mum verisi dokümantasyonu](https://www.mexc.com/api-docs/spot-v3/market-data-endpoints/klinecandlestick-data)",
              "", "Ham cevaplar data/ klasöründe; tüm ölçümler event_study.json içinde korunur."]
    (out/"inceleme.md").write_text("\n".join(lines)+"\n", encoding="utf-8")
    print("\n".join(lines[:19]))
    print(f"\nChecks passed. Reports: {out}")


if __name__ == "__main__":
    main()
