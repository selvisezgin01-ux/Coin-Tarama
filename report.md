# Coin Tarama5 — V3

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → ayrı geri test giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 30.10.2026 01:43 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 39, "p95_minutes": 5.000016666666666, "longest_minutes": 5.353983333333334, "over_10_minutes": 0}, "within_session": {"intervals": 38, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 1, "p95_minutes": 5.353983333333334, "longest_minutes": 5.353983333333334, "over_10_minutes": 0}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| PARTIUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 22:48 | 0.05888 | 0.0641 | 0.048721984 |
| XUVXYUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 23:58 | 17.75 | 17.4 | 16.810019 |
| OLUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 00:34 | 0.007327 | 0.007439 | 0.0071022408 |
| SUNUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 00:43 | 0.0169205 | 0.016324 | 0.015938085 |
| RUNEUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 00:58 | 0.63675 | 0.6152 | 0.57562574 |
| XDPUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 01:03 | 0.0189475 | 0.018736 | 0.017731974 |

## Kapsam ve eleme

{"observed_ms": 1793313836562, "new_radars": [], "liquid_tickers": 1460, "candles_evaluated": 126, "errors": {"OKX:PERP": [], "OKX:SPOT": [], "MEXC:PERP": [], "MEXC:SPOT": []}, "failed_groups": []}

OKX:SPOT: {"active_catalog": 372, "valid_liquid_tickers": 217, "observed_ms": 1793313827850, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 2, "funnel": {"candles_evaluated": 32, "volume_not_accelerating": 16, "close_not_strong": 19, "price_structure_not_ready": 27, "already_extended": 1}, "calls": 26, "errors": []}

OKX:PERP: {"active_catalog": 508, "valid_liquid_tickers": 453, "observed_ms": 1793313827836, "selected_for_candles": 31, "candles_evaluated": 31, "fresh_candidate_quotes": 1, "funnel": {"candles_evaluated": 31, "close_not_strong": 13, "price_structure_not_ready": 26, "volume_not_accelerating": 25}, "calls": 26, "errors": []}

MEXC:SPOT: {"active_catalog": 1247, "valid_liquid_tickers": 245, "observed_ms": 1793313828034, "selected_for_candles": 30, "candles_evaluated": 30, "fresh_candidate_quotes": 0, "funnel": {"candles_evaluated": 30, "close_not_strong": 16, "price_structure_not_ready": 25, "volume_not_accelerating": 24}, "calls": 27, "errors": []}

MEXC:PERP: {"active_catalog": 570, "valid_liquid_tickers": 545, "observed_ms": 1793313828002, "selected_for_candles": 33, "candles_evaluated": 33, "fresh_candidate_quotes": 3, "funnel": {"candles_evaluated": 33, "volume_not_accelerating": 27, "close_not_strong": 14, "price_structure_not_ready": 30}, "calls": 26, "errors": []}

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
| JSTUSDT | MEXC PERP | radar | 30.10.2026 00:34 | 0.143265 | %-0.74 | — | — | — |
| OLUSDT | OKX PERP | radar | 30.10.2026 00:34 | 0.0074535 | %-1.90 | — | — | — |
| SUNUSDT | MEXC PERP | radar | 30.10.2026 00:43 | 0.0164935 | %+2.54 | — | — | — |
| JP225USDT | OKX PERP | radar | 30.10.2026 00:48 | 64388 | — | — | — | — |
| RUNEUSDT | MEXC PERP | radar | 30.10.2026 00:58 | 0.63125 | — | — | — | — |
| XDPUSDT | OKX SPOT | radar | 30.10.2026 01:03 | 0.018779 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 1, "attempted": 1, "observed_ms": 1793313842469, "unique_reads": 2}, "summary": {"radar": {"unique_symbol_labels": 18, "hours": {"1": {"known": 15, "median_pct": -2.200488997555017}, "4": {"known": 0, "median_pct": null}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}, "triggered": {"unique_symbol_labels": 0, "hours": {"1": {"known": 0, "median_pct": null}, "4": {"known": 0, "median_pct": null}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}}}
