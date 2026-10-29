# Coin Tarama5 — V3

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → ayrı geri test giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 30.10.2026 00:08 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 20, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "within_session": {"intervals": 20, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 0, "p95_minutes": null, "longest_minutes": null, "over_10_minutes": 0}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| PARTIUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 22:48 | 0.056715 | 0.0641 | 0.048721984 |
| BTWUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 23:48 | 1.52605 | 1.5183 | 1.4363281 |
| XUVXYUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 23:58 | 17.535 | 17.4 | 16.810019 |
| SKDDUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 23:58 | 8.393 | 8.28 | 7.7328067 |

## Kapsam ve eleme

{"observed_ms": 1793308118780, "new_radars": [], "liquid_tickers": 1452, "candles_evaluated": 124, "errors": {"MEXC:SPOT": [], "OKX:SPOT": [], "OKX:PERP": ["BTWUSDT 4h optional context: Missing/stale closed history"], "MEXC:PERP": []}, "failed_groups": []}

OKX:SPOT: {"active_catalog": 372, "valid_liquid_tickers": 214, "observed_ms": 1793308106594, "selected_for_candles": 31, "candles_evaluated": 31, "fresh_candidate_quotes": 1, "funnel": {"candles_evaluated": 31, "volume_not_accelerating": 1, "close_not_strong": 29, "price_structure_not_ready": 30}, "calls": 30, "errors": []}

OKX:PERP: {"active_catalog": 508, "valid_liquid_tickers": 454, "observed_ms": 1793308106549, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 2, "funnel": {"candles_evaluated": 32, "close_not_strong": 28, "price_structure_not_ready": 30, "volume_not_accelerating": 2}, "calls": 33, "errors": ["BTWUSDT 4h optional context: Missing/stale closed history"]}

MEXC:SPOT: {"active_catalog": 1247, "valid_liquid_tickers": 240, "observed_ms": 1793308106950, "selected_for_candles": 30, "candles_evaluated": 30, "fresh_candidate_quotes": 0, "funnel": {"candles_evaluated": 30, "close_not_strong": 21, "price_structure_not_ready": 27, "already_extended": 1, "volume_not_accelerating": 4, "flat_price_or_volume": 1}, "calls": 23, "errors": []}

MEXC:PERP: {"active_catalog": 570, "valid_liquid_tickers": 544, "observed_ms": 1793308108054, "selected_for_candles": 31, "candles_evaluated": 31, "fresh_candidate_quotes": 1, "funnel": {"candles_evaluated": 31, "volume_not_accelerating": 8, "close_not_strong": 24, "price_structure_not_ready": 28, "already_extended": 1}, "calls": 30, "errors": []}

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
| XSNXXUSDT | OKX SPOT | radar | 29.10.2026 23:33 | 9.8315 | — | — | — | — |
| SNDKUSDT | OKX PERP | radar | 29.10.2026 23:33 | 1369.35 | — | — | — | — |
| SNXXUSDT | OKX PERP | radar | 29.10.2026 23:33 | 9.8315 | — | — | — | — |
| BTWUSDT | OKX PERP | radar | 29.10.2026 23:48 | 1.5202 | — | — | — | — |
| XUVXYUSDT | OKX SPOT | radar | 29.10.2026 23:58 | 17.475 | — | — | — | — |
| SKDDUSDT | OKX PERP | radar | 29.10.2026 23:58 | 8.345 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 0, "attempted": 0, "observed_ms": 1793308126063, "unique_reads": 0}, "summary": {"radar": {"unique_symbol_labels": 12, "hours": {"1": {"known": 6, "median_pct": -4.033222110232165}, "4": {"known": 0, "median_pct": null}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}, "triggered": {"unique_symbol_labels": 0, "hours": {"1": {"known": 0, "median_pct": null}, "4": {"known": 0, "median_pct": null}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}}}
