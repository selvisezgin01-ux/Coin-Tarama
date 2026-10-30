# Coin Tarama5 — V4

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → geri test veya yukarıda yeni taban giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 30.10.2026 21:49 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 58, "p95_minutes": 5.61935, "longest_minutes": 55.56921666666667, "over_10_minutes": 1}, "within_session": {"intervals": 55, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 3, "p95_minutes": 55.56921666666667, "longest_minutes": 55.56921666666667, "over_10_minutes": 1}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| ARKMUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 17:08 | 0.11009 | 0.11007 | 0.10764038 |
| PLAYUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 19:24 | 0.01449 | 0.01384 | 0.013209099 |
| ZROUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 19:29 | 1.67545 | 1.7772 | 1.6726944 |
| CHIPUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 19:39 | 0.042625 | 0.04511 | 0.042514973 |
| SENTUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 20:24 | 0.019165 | 0.01894 | 0.018355994 |
| VIRTUALUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 20:24 | 0.5882 | 0.5977 | 0.5846612 |
| VIRTUALUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 20:24 | 0.58785 | 0.5978 | 0.58415245 |
| SENTUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 20:34 | 0.019205 | 0.01896 | 0.018345689 |
| AINUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 20:34 | 0.181725 | 0.17208 | 0.16529265 |
| SENTUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 20:49 | 0.0192 | 0.01916 | 0.018364497 |
| SENTUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 20:49 | 0.019155 | 0.01914 | 0.018322205 |
| AINUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 21:04 | 0.182345 | 0.17572 | 0.16751309 |
| BULLAUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 21:29 | 0.0785145 | 0.073224 | 0.071731662 |
| PARTIUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 21:29 | 0.051865 | 0.05104 | 0.047360718 |
| ILVUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 21:34 | 2.993 | 2.979 | 2.9252112 |
| GWEIUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 21:34 | 0.02255 | 0.02172 | 0.020731221 |

## Kapsam ve eleme

{"observed_ms": 1793386196086, "new_radars": [], "liquid_tickers": 1360, "candles_evaluated": 135, "errors": {"OKX:PERP": [], "OKX:SPOT": [], "MEXC:PERP": [], "MEXC:SPOT": ["MTOUSDT 4h optional context: Missing/stale closed history"]}, "failed_groups": []}

OKX:PERP: {"active_catalog": 288, "instrument_categories": {"1": 304, "3": 219, "4": 9}, "valid_liquid_tickers": 287, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793386182736, "selected_for_candles": 31, "candles_evaluated": 31, "fresh_candidate_quotes": 1, "funnel": {"candles_evaluated": 31, "volume_not_accelerating": 24, "close_not_strong": 27, "price_structure_not_ready": 29, "already_extended": 1}, "calls": 34, "errors": []}

OKX:SPOT: {"active_catalog": 294, "instrument_categories": {"1": 1013, "4": 4, "3": 194}, "valid_liquid_tickers": 233, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793386182805, "selected_for_candles": 34, "candles_evaluated": 34, "fresh_candidate_quotes": 5, "funnel": {"candles_evaluated": 34, "volume_not_accelerating": 28, "price_structure_not_ready": 32, "close_not_strong": 26, "already_extended": 1}, "calls": 37, "errors": []}

MEXC:PERP: {"active_catalog": 569, "instrument_categories": {}, "valid_liquid_tickers": 546, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793386183586, "selected_for_candles": 35, "candles_evaluated": 35, "fresh_candidate_quotes": 7, "funnel": {"candles_evaluated": 35, "close_not_strong": 29, "price_structure_not_ready": 31, "volume_not_accelerating": 22, "already_extended": 1}, "calls": 38, "errors": []}

MEXC:SPOT: {"active_catalog": 1240, "instrument_categories": {}, "valid_liquid_tickers": 292, "active_quotes_retained_outside_discovery": 2, "observed_ms": 1793386182951, "selected_for_candles": 35, "candles_evaluated": 35, "fresh_candidate_quotes": 7, "funnel": {"candles_evaluated": 35, "volume_not_accelerating": 24, "close_not_strong": 28, "price_structure_not_ready": 32}, "calls": 40, "errors": ["MTOUSDT 4h optional context: Missing/stale closed history"]}

Ayrıntılı evren/ret nedenleri ve seçilen kimlikler state içinde saklanır. Rolling24s hacim farkı yalnız sıralama vekilidir,5dk alım hacmi değildir. Hacim sinyali yalnız kapalı15dk gerçek quote hacmiyle ölçülür.4s trend/OI erken radarı engellemez.3yeni sembol/döngü,6yeni sembol/saat,20aktif sembol/80pazar sınırı vardır. Aynı sembol her borsada kendi fiyatıyla izlenir; yalnız tekrar eden erken bildirimler bastırılır; kota dışı fırsatlar kaçabilir.

## İlk gerçek gözlem ölçümleri

Radar ve giriş ayrı referanslardır, bağımsız iki başarı gibi toplanmaz. Her pazar/evre/giriş türünün gerçek referansı korunur; aynı sembol ve tekrar girişler bağımsız örnek sayılmaz; borsalar/pazarlar arası fiyatlar birleştirilmez. Eski V3 kayıtları değişmeyen arşiv commitinde korunur; eski ölçümler ayrı legacy_v3 alanında sürer.

| Coin | Pazar | Evre / giriş türü | Gözlem TR | Referans | 1s | 4s | 12s | 24s |
|---|---|---|---|---:|---|---|---|---|
| XPLUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 16:04 | 0.077915 | %-1.17 | %-0.65 | — | — |
| EDGEUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 16:04 | 0.3428 | %+0.03 | %+2.95 | — | — |
| EDGEUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 16:04 | 0.34235 | %-0.07 | %+3.20 | — | — |
| REDUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 16:04 | 0.12365 | %-2.30 | %+1.33 | — | — |
| EDGEUSDT | OKX PERP | radar / radar #0 | 30.10.2026 16:04 | 0.3423 | %-0.23 | %+3.13 | — | — |
| XPLUSDT | OKX PERP | radar / radar #0 | 30.10.2026 16:09 | 0.077635 | %-1.38 | %-0.71 | — | — |
| JUPUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 16:09 | 0.2551 | %-1.14 | %-0.55 | — | — |
| 4USDT | MEXC PERP | radar / radar #0 | 30.10.2026 16:09 | 0.011075 | %-0.05 | %-0.14 | — | — |
| IBVMUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 16:09 | 0.1188 | %-0.25 | %+0.34 | — | — |
| BRUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 17:08 | 0.4864 | %-1.15 | %-3.06 | — | — |
| HUMAUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:08 | 0.02887 | %+0.59 | %-2.67 | — | — |
| ARKMUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:08 | 0.11046 | %+1.40 | %+0.31 | — | — |
| PROVEUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:13 | 0.1955 | %+2.35 | %+2.92 | — | — |
| BEAMXUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 17:13 | 0.0052475 | %-9.19 | — | — | — |
| LITUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:13 | 2.8186 | %+3.23 | %-2.88 | — | — |
| WLDUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 18:19 | 0.4141 | %+0.07 | — | — | — |
| ZETAUSDT | OKX PERP | radar / radar #0 | 30.10.2026 18:19 | 0.03757 | %-1.57 | — | — | — |
| NEARUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 18:19 | 4.42085 | %-1.59 | — | — | — |
| TUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 18:24 | 0.0045505 | %-0.41 | — | — | — |
| BREVUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 18:24 | 0.08922 | %-0.39 | — | — | — |
| SAHARAUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 18:24 | 0.0075545 | %-0.67 | — | — | — |
| BREVUSDT | OKX PERP | radar / radar #0 | 30.10.2026 18:24 | 0.08912 | %-0.18 | — | — | — |
| BREVUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 18:29 | 0.08906 | %-0.36 | — | — | — |
| GRTUSDT | OKX PERP | radar / radar #0 | 30.10.2026 19:24 | 0.021 | %-0.90 | — | — | — |
| PLAYUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 19:24 | 0.013925 | %+3.48 | — | — | — |
| GRASSUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 19:29 | 0.6026 | %+0.38 | — | — | — |
| GRASSUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 19:29 | 0.60245 | %+0.44 | — | — | — |
| ZROUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 19:29 | 1.76525 | %-0.68 | — | — | — |
| BIANRENSHENGUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 19:34 | 0.53025 | %+0.25 | — | — | — |
| CHIPUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 19:39 | 0.044335 | %-1.70 | — | — | — |
| SENTUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 20:24 | 0.019105 | %+1.44 | — | — | — |
| VIRTUALUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 20:24 | 0.5954 | %-0.82 | — | — | — |
| VIRTUALUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 20:24 | 0.595 | %-0.77 | — | — | — |
| EDENUSDT | OKX PERP | radar / radar #0 | 30.10.2026 20:29 | 0.05524 | %-2.44 | — | — | — |
| MMTUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 20:29 | 0.1294 | %-1.16 | — | — | — |
| SENTUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 20:34 | 0.01929 | %-0.31 | — | — | — |
| AINUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 20:34 | 0.173475 | %+9.25 | — | — | — |
| AIUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 20:39 | 0.016915 | %-0.98 | — | — | — |
| SENTUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 20:49 | 0.019585 | %-2.02 | — | — | — |
| SENTUSDT | OKX PERP | radar / radar #0 | 30.10.2026 20:49 | 0.01954 | %-2.00 | — | — | — |
| AINUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 21:04 | 0.183775 | — | — | — | — |
| BULLAUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 21:29 | 0.073804 | — | — | — | — |
| PARTIUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 21:29 | 0.053295 | — | — | — | — |
| ILVUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 21:34 | 2.985 | — | — | — | — |
| GWEIUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 21:34 | 0.02216 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 3, "attempted": 2, "observed_ms": 1793386208307, "unique_reads": 4}, "summary": {"radar": {"market_event_references": 45, "unique_symbol_labels": 34, "note": "Markets, routes and repeated entries of one symbol are correlated; never summed as independent wins. Early radar is not entry.", "groups": {"OKX:SPOT:radar": {"event_references": 16, "first_per_symbol": 16, "hours": {"1": {"known_first_symbols": 15, "median_reference_return_pct": -0.3922887245012219}, "4": {"known_first_symbols": 6, "median_reference_return_pct": -0.17016923819672125}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "MEXC:SPOT:radar": {"event_references": 11, "first_per_symbol": 11, "hours": {"1": {"known_first_symbols": 9, "median_reference_return_pct": -0.2525252525252597}, "4": {"known_first_symbols": 3, "median_reference_return_pct": 0.33670033670032407}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "MEXC:PERP:radar": {"event_references": 11, "first_per_symbol": 11, "hours": {"1": {"known_first_symbols": 9, "median_reference_return_pct": -0.3593083314619383}, "4": {"known_first_symbols": 3, "median_reference_return_pct": -0.13544018058689877}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "OKX:PERP:radar": {"event_references": 7, "first_per_symbol": 7, "hours": {"1": {"known_first_symbols": 7, "median_reference_return_pct": -1.3846847427062658}, "4": {"known_first_symbols": 2, "median_reference_return_pct": 1.2055145954891433}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}}}, "triggered": {"market_event_references": 0, "unique_symbol_labels": 0, "note": "Markets, routes and repeated entries of one symbol are correlated; never summed as independent wins. Early radar is not entry.", "groups": {}}}}
