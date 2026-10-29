# Coin Tarama5 — V3

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → ayrı geri test giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 30.10.2026 01:08 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 32, "p95_minutes": 5.000016666666666, "longest_minutes": 5.353983333333334, "over_10_minutes": 0}, "within_session": {"intervals": 31, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 1, "p95_minutes": 5.353983333333334, "longest_minutes": 5.353983333333334, "over_10_minutes": 0}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| PARTIUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 22:48 | 0.058365 | 0.0641 | 0.048721984 |
| XUVXYUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 23:58 | 17.575 | 17.4 | 16.810019 |
| SKDDUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 23:58 | 8.483 | 8.28 | 7.7328067 |
| JSTUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 00:34 | 0.142435 | 0.14209 | 0.14059039 |
| OLUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 00:34 | 0.007233 | 0.007439 | 0.0071022408 |
| SUNUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 00:43 | 0.0165755 | 0.016324 | 0.015938085 |
| JP225USDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 00:48 | 64115 | 64817 | 63948.371 |
| RUNEUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 00:58 | 0.62985 | 0.6152 | 0.57562574 |
| XDPUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 01:03 | 0.018649 | 0.018736 | 0.017731974 |

## Kapsam ve eleme

{"observed_ms": 1793311738643, "new_radars": [], "liquid_tickers": 1458, "candles_evaluated": 126, "errors": {"MEXC:SPOT": [], "OKX:SPOT": [], "OKX:PERP": [], "MEXC:PERP": ["JAGENTUSDT: Missing/stale closed history"]}, "failed_groups": []}

OKX:SPOT: {"active_catalog": 372, "valid_liquid_tickers": 217, "observed_ms": 1793311727830, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 2, "funnel": {"candles_evaluated": 32, "close_not_strong": 26, "price_structure_not_ready": 28, "volume_not_accelerating": 14, "already_extended": 1}, "calls": 28, "errors": []}

OKX:PERP: {"active_catalog": 508, "valid_liquid_tickers": 452, "observed_ms": 1793311727823, "selected_for_candles": 33, "candles_evaluated": 33, "fresh_candidate_quotes": 3, "funnel": {"candles_evaluated": 33, "volume_not_accelerating": 23, "close_not_strong": 30, "price_structure_not_ready": 31}, "calls": 31, "errors": []}

MEXC:SPOT: {"active_catalog": 1247, "valid_liquid_tickers": 245, "observed_ms": 1793311728075, "selected_for_candles": 30, "candles_evaluated": 30, "fresh_candidate_quotes": 1, "funnel": {"candles_evaluated": 30, "volume_not_accelerating": 19, "close_not_strong": 24, "price_structure_not_ready": 26, "already_extended": 2, "flat_price_or_volume": 1}, "calls": 21, "errors": []}

MEXC:PERP: {"active_catalog": 570, "valid_liquid_tickers": 544, "observed_ms": 1793311729213, "selected_for_candles": 32, "candles_evaluated": 31, "fresh_candidate_quotes": 4, "funnel": {"candles_evaluated": 31, "volume_not_accelerating": 24, "close_not_strong": 27, "price_structure_not_ready": 29, "already_extended": 1}, "calls": 26, "errors": ["JAGENTUSDT: Missing/stale closed history"]}

Ayrıntılı evren/ret nedenleri ve seçilen kimlikler state içinde saklanır. Rolling24s hacim farkı yalnız sıralama vekilidir,5dk alım hacmi değildir. Hacim sinyali yalnız kapalı15dk gerçek quote hacmiyle ölçülür.4s trend/OI erken radarı engellemez.3yeni radar/döngü,6radar/saat ve20aktif izleme sınırı vardır; kota dışı fırsatlar kaçabilir.

## İlk gerçek gözlem ölçümleri

Radar ve giriş ayrı referanslardır, bağımsız iki başarı gibi toplanmaz. Aynı sembolün ilk evre referansı korunur; borsalar/pazarlar arası fiyatlar birleştirilmez. Eski V2 kayıtları değişmeyen arşiv commitinde korunur.

| Coin | Pazar | Evre | Gözlem TR | Referans | 1s | 4s | 12s | 24s |
|---|---|---|---|---:|---|---|---|---|
| DODOUSDT | MEXC PERP | radar | 29.10.2026 22:28 | 0.025465 | %-1.98 | — | — | — |
| AVNTUSDT | MEXC PERP | radar | 29.10.2026 22:28 | 0.10225 | %-2.20 | — | — | — |
| CENTUSDT | MEXC SPOT | radar | 29.10.2026 22:28 | 0.0016625 | %-6.23 | — | — | — |
| DYDXUSDT | MEXC SPOT | radar | 29.10.2026 22:48 | 0.11404 | %-3.91 | — | — | — |
| POLYXUSDT | MEXC PERP | radar | 29.10.2026 22:48 | 0.03369 | %-4.16 | — | — | — |
| PARTIUSDT | MEXC PERP | radar | 29.10.2026 22:48 | 0.06075 | %-5.25 | — | — | — |
| XSNXXUSDT | OKX SPOT | radar | 29.10.2026 23:33 | 9.8315 | %-10.07 | — | — | — |
| SNDKUSDT | OKX PERP | radar | 29.10.2026 23:33 | 1369.35 | %-4.93 | — | — | — |
| SNXXUSDT | OKX PERP | radar | 29.10.2026 23:33 | 9.8315 | %-9.84 | — | — | — |
| BTWUSDT | OKX PERP | radar | 29.10.2026 23:48 | 1.5202 | %+1.24 | — | — | — |
| XUVXYUSDT | OKX SPOT | radar | 29.10.2026 23:58 | 17.475 | %+0.54 | — | — | — |
| SKDDUSDT | OKX PERP | radar | 29.10.2026 23:58 | 8.345 | %+1.83 | — | — | — |
| JSTUSDT | MEXC PERP | radar | 30.10.2026 00:34 | 0.143265 | — | — | — | — |
| OLUSDT | OKX PERP | radar | 30.10.2026 00:34 | 0.0074535 | — | — | — | — |
| SUNUSDT | MEXC PERP | radar | 30.10.2026 00:43 | 0.0164935 | — | — | — | — |
| JP225USDT | OKX PERP | radar | 30.10.2026 00:48 | 64388 | — | — | — | — |
| RUNEUSDT | MEXC PERP | radar | 30.10.2026 00:58 | 0.63125 | — | — | — | — |
| XDPUSDT | OKX SPOT | radar | 30.10.2026 01:03 | 0.018779 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 0, "attempted": 0, "observed_ms": 1793311451661, "unique_reads": 0}, "summary": {"radar": {"unique_symbol_labels": 18, "hours": {"1": {"known": 12, "median_pct": -4.033222110232165}, "4": {"known": 0, "median_pct": null}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}, "triggered": {"unique_symbol_labels": 0, "hours": {"1": {"known": 0, "median_pct": null}, "4": {"known": 0, "median_pct": null}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}}}
