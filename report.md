# Coin Tarama5 — V4

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → geri test veya yukarıda yeni taban giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 30.10.2026 18:19 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 16, "p95_minutes": 55.56921666666667, "longest_minutes": 55.56921666666667, "over_10_minutes": 1}, "within_session": {"intervals": 14, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 2, "p95_minutes": 55.56921666666667, "longest_minutes": 55.56921666666667, "over_10_minutes": 1}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| REDUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 16:04 | 0.12425 | 0.1227 | 0.12031248 |
| IBVMUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 16:09 | 0.1189 | 0.119 | 0.11290842 |
| HUMAUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 17:08 | 0.02897 | 0.02866 | 0.027941175 |
| ARKMUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 17:08 | 0.113305 | 0.11007 | 0.10764038 |
| PROVEUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 17:13 | 0.2004 | 0.1965 | 0.19352829 |
| LITUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 17:13 | 2.9364 | 2.828 | 2.7216376 |
| WLDUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 18:19 | 0.4141 | 0.409 | 0.39468829 |
| ZETAUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 18:19 | 0.03757 | 0.03701 | 0.036310405 |
| NEARUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 18:19 | 4.42085 | 4.3535 | 4.2114698 |

## Kapsam ve eleme

{"observed_ms": 1793373563225, "new_radars": ["MEXC:SPOT:WLDUSDT", "OKX:PERP:ZETAUSDT", "MEXC:SPOT:NEARUSDT"], "liquid_tickers": 1368, "candles_evaluated": 126, "errors": {"MEXC:PERP": [], "OKX:PERP": [], "MEXC:SPOT": [], "OKX:SPOT": []}, "failed_groups": []}

OKX:PERP: {"active_catalog": 288, "instrument_categories": {"1": 304, "3": 219, "4": 9}, "valid_liquid_tickers": 288, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793373545670, "selected_for_candles": 30, "candles_evaluated": 30, "fresh_candidate_quotes": 8, "funnel": {"candles_evaluated": 30, "volume_not_accelerating": 20, "close_not_strong": 3, "price_structure_not_ready": 3}, "calls": 49, "errors": []}

OKX:SPOT: {"active_catalog": 294, "instrument_categories": {"1": 1013, "4": 4, "3": 194}, "valid_liquid_tickers": 231, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793373545792, "selected_for_candles": 34, "candles_evaluated": 34, "fresh_candidate_quotes": 12, "funnel": {"candles_evaluated": 34, "close_not_strong": 8, "volume_not_accelerating": 22, "price_structure_not_ready": 4, "already_extended": 1}, "calls": 52, "errors": []}

MEXC:PERP: {"active_catalog": 569, "instrument_categories": {}, "valid_liquid_tickers": 549, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793373547666, "selected_for_candles": 31, "candles_evaluated": 31, "fresh_candidate_quotes": 5, "funnel": {"candles_evaluated": 31, "volume_not_accelerating": 21, "already_extended": 2, "close_not_strong": 7, "price_structure_not_ready": 6}, "calls": 41, "errors": []}

MEXC:SPOT: {"active_catalog": 1240, "instrument_categories": {}, "valid_liquid_tickers": 300, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793373545634, "selected_for_candles": 31, "candles_evaluated": 31, "fresh_candidate_quotes": 9, "funnel": {"candles_evaluated": 31, "volume_not_accelerating": 19, "close_not_strong": 7, "price_structure_not_ready": 6}, "calls": 50, "errors": []}

Ayrıntılı evren/ret nedenleri ve seçilen kimlikler state içinde saklanır. Rolling24s hacim farkı yalnız sıralama vekilidir,5dk alım hacmi değildir. Hacim sinyali yalnız kapalı15dk gerçek quote hacmiyle ölçülür.4s trend/OI erken radarı engellemez.3yeni sembol/döngü,6yeni sembol/saat,20aktif sembol/80pazar sınırı vardır. Aynı sembol her borsada kendi fiyatıyla izlenir; yalnız tekrar eden erken bildirimler bastırılır; kota dışı fırsatlar kaçabilir.

## İlk gerçek gözlem ölçümleri

Radar ve giriş ayrı referanslardır, bağımsız iki başarı gibi toplanmaz. Her pazar/evre/giriş türünün gerçek referansı korunur; aynı sembol ve tekrar girişler bağımsız örnek sayılmaz; borsalar/pazarlar arası fiyatlar birleştirilmez. Eski V3 kayıtları değişmeyen arşiv commitinde korunur; eski ölçümler ayrı legacy_v3 alanında sürer.

| Coin | Pazar | Evre / giriş türü | Gözlem TR | Referans | 1s | 4s | 12s | 24s |
|---|---|---|---|---:|---|---|---|---|
| XPLUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 16:04 | 0.077915 | %-1.17 | — | — | — |
| EDGEUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 16:04 | 0.3428 | %+0.03 | — | — | — |
| EDGEUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 16:04 | 0.34235 | %-0.07 | — | — | — |
| REDUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 16:04 | 0.12365 | %-2.30 | — | — | — |
| EDGEUSDT | OKX PERP | radar / radar #0 | 30.10.2026 16:04 | 0.3423 | %-0.23 | — | — | — |
| XPLUSDT | OKX PERP | radar / radar #0 | 30.10.2026 16:09 | 0.077635 | %-1.38 | — | — | — |
| JUPUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 16:09 | 0.2551 | %-1.14 | — | — | — |
| 4USDT | MEXC PERP | radar / radar #0 | 30.10.2026 16:09 | 0.011075 | %-0.05 | — | — | — |
| IBVMUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 16:09 | 0.1188 | %-0.25 | — | — | — |
| BRUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 17:08 | 0.4864 | — | — | — | — |
| HUMAUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:08 | 0.02887 | — | — | — | — |
| ARKMUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:08 | 0.11046 | — | — | — | — |
| PROVEUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:13 | 0.1955 | — | — | — | — |
| BEAMXUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 17:13 | 0.0052475 | — | — | — | — |
| LITUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:13 | 2.8186 | — | — | — | — |
| WLDUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 18:19 | 0.4141 | — | — | — | — |
| ZETAUSDT | OKX PERP | radar / radar #0 | 30.10.2026 18:19 | 0.03757 | — | — | — | — |
| NEARUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 18:19 | 4.42085 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 8, "attempted": 2, "observed_ms": 1793373574102, "unique_reads": 3}, "summary": {"radar": {"market_event_references": 18, "unique_symbol_labels": 15, "note": "Markets, routes and repeated entries of one symbol are correlated; never summed as independent wins. Early radar is not entry.", "groups": {"OKX:SPOT:radar": {"event_references": 6, "first_per_symbol": 6, "hours": {"1": {"known_first_symbols": 2, "median_reference_return_pct": -0.5725925710714119}, "4": {"known_first_symbols": 0, "median_reference_return_pct": null}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "MEXC:SPOT:radar": {"event_references": 5, "first_per_symbol": 5, "hours": {"1": {"known_first_symbols": 3, "median_reference_return_pct": -0.2525252525252597}, "4": {"known_first_symbols": 0, "median_reference_return_pct": null}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "MEXC:PERP:radar": {"event_references": 4, "first_per_symbol": 4, "hours": {"1": {"known_first_symbols": 2, "median_reference_return_pct": -1.175019784781739}, "4": {"known_first_symbols": 0, "median_reference_return_pct": null}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "OKX:PERP:radar": {"event_references": 3, "first_per_symbol": 3, "hours": {"1": {"known_first_symbols": 2, "median_reference_return_pct": -0.8091989299274793}, "4": {"known_first_symbols": 0, "median_reference_return_pct": null}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}}}, "triggered": {"market_event_references": 0, "unique_symbol_labels": 0, "note": "Markets, routes and repeated entries of one symbol are correlated; never summed as independent wins. Early radar is not entry.", "groups": {}}}}
