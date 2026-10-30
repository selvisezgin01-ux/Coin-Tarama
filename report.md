# Coin Tarama5 — V4

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → geri test veya yukarıda yeni taban giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 30.10.2026 16:23 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 3, "p95_minutes": 9.628833333333333, "longest_minutes": 9.628833333333333, "over_10_minutes": 0}, "within_session": {"intervals": 2, "p95_minutes": 5.0, "longest_minutes": 5.0, "over_10_minutes": 0}, "between_sessions": {"intervals": 1, "p95_minutes": 9.628833333333333, "longest_minutes": 9.628833333333333, "over_10_minutes": 0}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| XPLUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 16:04 | 0.077295 | 0.07663 | 0.074844714 |
| EDGEUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 16:04 | 0.34125 | 0.3414 | 0.33507498 |
| EDGEUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 16:04 | 0.34125 | 0.3411 | 0.33397216 |
| REDUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 16:04 | 0.12205 | 0.1227 | 0.12031248 |
| EDGEUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 16:04 | 0.3409 | 0.341 | 0.33349741 |
| XPLUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 16:09 | 0.077285 | 0.07661 | 0.074720918 |
| JUPUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 16:09 | 0.2546 | 0.2572 | 0.25375987 |
| IBVMUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 16:09 | 0.1188 | 0.119 | 0.11290842 |

## Kapsam ve eleme

{"observed_ms": 1793366623750, "new_radars": [], "liquid_tickers": 1364, "candles_evaluated": 129, "errors": {"OKX:PERP": [], "OKX:SPOT": [], "MEXC:SPOT": [], "MEXC:PERP": []}, "failed_groups": []}

OKX:PERP: {"active_catalog": 288, "instrument_categories": {"1": 304, "3": 219, "4": 9}, "valid_liquid_tickers": 288, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793366611435, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 3, "funnel": {"candles_evaluated": 32, "close_not_strong": 26, "price_structure_not_ready": 29, "volume_not_accelerating": 24}, "calls": 36, "errors": []}

OKX:SPOT: {"active_catalog": 294, "instrument_categories": {"1": 1013, "4": 4, "3": 194}, "valid_liquid_tickers": 232, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793366611422, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 3, "funnel": {"candles_evaluated": 32, "close_not_strong": 27, "price_structure_not_ready": 25, "volume_not_accelerating": 24}, "calls": 36, "errors": []}

MEXC:PERP: {"active_catalog": 569, "instrument_categories": {}, "valid_liquid_tickers": 548, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793366611754, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 3, "funnel": {"candles_evaluated": 32, "volume_not_accelerating": 19, "close_not_strong": 23, "price_structure_not_ready": 24}, "calls": 37, "errors": []}

MEXC:SPOT: {"active_catalog": 1247, "instrument_categories": {}, "valid_liquid_tickers": 296, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793366611834, "selected_for_candles": 33, "candles_evaluated": 33, "fresh_candidate_quotes": 3, "funnel": {"candles_evaluated": 33, "volume_not_accelerating": 28, "close_not_strong": 24, "price_structure_not_ready": 26}, "calls": 36, "errors": []}

Ayrıntılı evren/ret nedenleri ve seçilen kimlikler state içinde saklanır. Rolling24s hacim farkı yalnız sıralama vekilidir,5dk alım hacmi değildir. Hacim sinyali yalnız kapalı15dk gerçek quote hacmiyle ölçülür.4s trend/OI erken radarı engellemez.3yeni sembol/döngü,6yeni sembol/saat,20aktif sembol/80pazar sınırı vardır. Aynı sembol her borsada kendi fiyatıyla izlenir; yalnız tekrar eden erken bildirimler bastırılır; kota dışı fırsatlar kaçabilir.

## İlk gerçek gözlem ölçümleri

Radar ve giriş ayrı referanslardır, bağımsız iki başarı gibi toplanmaz. Her pazar/evre/giriş türünün gerçek referansı korunur; aynı sembol ve tekrar girişler bağımsız örnek sayılmaz; borsalar/pazarlar arası fiyatlar birleştirilmez. Eski V3 kayıtları değişmeyen arşiv commitinde korunur; eski ölçümler ayrı legacy_v3 alanında sürer.

| Coin | Pazar | Evre / giriş türü | Gözlem TR | Referans | 1s | 4s | 12s | 24s |
|---|---|---|---|---:|---|---|---|---|
| XPLUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 16:04 | 0.077915 | — | — | — | — |
| EDGEUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 16:04 | 0.3428 | — | — | — | — |
| EDGEUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 16:04 | 0.34235 | — | — | — | — |
| REDUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 16:04 | 0.12365 | — | — | — | — |
| EDGEUSDT | OKX PERP | radar / radar #0 | 30.10.2026 16:04 | 0.3423 | — | — | — | — |
| XPLUSDT | OKX PERP | radar / radar #0 | 30.10.2026 16:09 | 0.077635 | — | — | — | — |
| JUPUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 16:09 | 0.2551 | — | — | — | — |
| 4USDT | MEXC PERP | radar / radar #0 | 30.10.2026 16:09 | 0.011075 | — | — | — | — |
| IBVMUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 16:09 | 0.1188 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 0, "attempted": 0, "observed_ms": 1793366634043, "unique_reads": 0}, "summary": {"radar": {"market_event_references": 9, "unique_symbol_labels": 6, "note": "Markets, routes and repeated entries of one symbol are correlated; never summed as independent wins. Early radar is not entry.", "groups": {"OKX:SPOT:radar": {"event_references": 2, "first_per_symbol": 2, "hours": {"1": {"known_first_symbols": 0, "median_reference_return_pct": null}, "4": {"known_first_symbols": 0, "median_reference_return_pct": null}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "MEXC:SPOT:radar": {"event_references": 3, "first_per_symbol": 3, "hours": {"1": {"known_first_symbols": 0, "median_reference_return_pct": null}, "4": {"known_first_symbols": 0, "median_reference_return_pct": null}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "MEXC:PERP:radar": {"event_references": 2, "first_per_symbol": 2, "hours": {"1": {"known_first_symbols": 0, "median_reference_return_pct": null}, "4": {"known_first_symbols": 0, "median_reference_return_pct": null}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "OKX:PERP:radar": {"event_references": 2, "first_per_symbol": 2, "hours": {"1": {"known_first_symbols": 0, "median_reference_return_pct": null}, "4": {"known_first_symbols": 0, "median_reference_return_pct": null}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}}}, "triggered": {"market_event_references": 0, "unique_symbol_labels": 0, "note": "Markets, routes and repeated entries of one symbol are correlated; never summed as independent wins. Early radar is not entry.", "groups": {}}}}
