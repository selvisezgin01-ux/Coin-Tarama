# Coin Tarama5 — V4

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → geri test veya yukarıda yeni taban giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 30.10.2026 23:11 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 74, "p95_minutes": 5.7267, "longest_minutes": 55.56921666666667, "over_10_minutes": 1}, "within_session": {"intervals": 69, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 5, "p95_minutes": 55.56921666666667, "longest_minutes": 55.56921666666667, "over_10_minutes": 1}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| PLAYUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 19:24 | 0.014745 | 0.01384 | 0.013209099 |
| SENTUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 20:24 | 0.019455 | 0.01894 | 0.018355994 |
| VIRTUALUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 20:24 | 0.5896 | 0.5977 | 0.5846612 |
| VIRTUALUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 20:24 | 0.5893 | 0.5978 | 0.58415245 |
| SENTUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 20:49 | 0.019425 | 0.01914 | 0.018322205 |
| GWEIUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 21:34 | 0.022915 | 0.02172 | 0.020731221 |
| SIRENUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 22:00 | 0.022915 | 0.02239 | 0.02193586 |
| XPLUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 22:00 | 0.080705 | 0.0782 | 0.076839863 |
| ATOMUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 22:32 | 1.5115 | 1.515 | 1.4947312 |
| SPXUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 22:32 | 0.36045 | 0.3631 | 0.35248043 |
| UAIUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 22:36 | 0.27015 | 0.2709 | 0.2590681 |
| CVXUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 22:47 | 1.9945 | 1.987 | 1.9525225 |
| NIULAIUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 23:02 | 0.054035 | 0.05394 | 0.052244287 |
| EIGENUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 23:02 | 0.1878 | 0.1866 | 0.17928999 |
| EIGENUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 23:02 | 0.18795 | 0.1866 | 0.17947008 |
| EIGENUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 23:02 | 0.18775 | 0.1865 | 0.17906179 |

## Kapsam ve eleme

{"observed_ms": 1793391119590, "new_radars": [], "liquid_tickers": 1353, "candles_evaluated": 137, "errors": {"OKX:PERP": [], "OKX:SPOT": [], "MEXC:SPOT": [], "MEXC:PERP": []}, "failed_groups": []}

OKX:PERP: {"active_catalog": 288, "instrument_categories": {"1": 304, "3": 219, "4": 9}, "valid_liquid_tickers": 287, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793391108809, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 3, "funnel": {"candles_evaluated": 32, "volume_not_accelerating": 29, "close_not_strong": 11, "price_structure_not_ready": 12}, "calls": 26, "errors": []}

OKX:SPOT: {"active_catalog": 294, "instrument_categories": {"1": 1013, "4": 4, "3": 194}, "valid_liquid_tickers": 235, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793391108887, "selected_for_candles": 35, "candles_evaluated": 35, "fresh_candidate_quotes": 6, "funnel": {"candles_evaluated": 35, "volume_not_accelerating": 30, "close_not_strong": 15, "price_structure_not_ready": 10}, "calls": 26, "errors": []}

MEXC:PERP: {"active_catalog": 569, "instrument_categories": {}, "valid_liquid_tickers": 544, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793391109145, "selected_for_candles": 38, "candles_evaluated": 38, "fresh_candidate_quotes": 8, "funnel": {"candles_evaluated": 38, "close_not_strong": 19, "price_structure_not_ready": 19, "volume_not_accelerating": 30}, "calls": 32, "errors": []}

MEXC:SPOT: {"active_catalog": 1240, "instrument_categories": {}, "valid_liquid_tickers": 287, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793391109647, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 2, "funnel": {"candles_evaluated": 32, "volume_not_accelerating": 30, "price_structure_not_ready": 21, "close_not_strong": 11}, "calls": 26, "errors": []}

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
| BEAMXUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 17:13 | 0.0052475 | %-9.19 | %-9.98 | — | — |
| LITUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:13 | 2.8186 | %+3.23 | %-2.88 | — | — |
| WLDUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 18:19 | 0.4141 | %+0.07 | %-2.75 | — | — |
| ZETAUSDT | OKX PERP | radar / radar #0 | 30.10.2026 18:19 | 0.03757 | %-1.57 | %-3.11 | — | — |
| NEARUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 18:19 | 4.42085 | %-1.59 | %-3.39 | — | — |
| TUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 18:24 | 0.0045505 | %-0.41 | %-2.54 | — | — |
| BREVUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 18:24 | 0.08922 | %-0.39 | %-0.81 | — | — |
| SAHARAUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 18:24 | 0.0075545 | %-0.67 | %-1.09 | — | — |
| BREVUSDT | OKX PERP | radar / radar #0 | 30.10.2026 18:24 | 0.08912 | %-0.18 | %-0.58 | — | — |
| BREVUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 18:29 | 0.08906 | %-0.36 | %-1.39 | — | — |
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
| AINUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 21:04 | 0.183775 | %-0.48 | — | — | — |
| BULLAUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 21:29 | 0.073804 | %+0.78 | — | — | — |
| PARTIUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 21:29 | 0.053295 | %-6.54 | — | — | — |
| ILVUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 21:34 | 2.985 | %-2.51 | — | — | — |
| GWEIUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 21:34 | 0.02216 | %+6.14 | — | — | — |
| SIRENUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 22:00 | 0.02309 | %-1.21 | — | — | — |
| XPLUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 22:00 | 0.078245 | %+3.52 | — | — | — |
| ATOMUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 22:32 | 1.5085 | — | — | — | — |
| SPXUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 22:32 | 0.358 | — | — | — | — |
| UAIUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 22:36 | 0.2713 | — | — | — | — |
| CVXUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 22:47 | 1.992 | — | — | — | — |
| NIULAIUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 23:02 | 0.054305 | — | — | — | — |
| EIGENUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 23:02 | 0.1904 | — | — | — | — |
| EIGENUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 23:02 | 0.19055 | — | — | — | — |
| EIGENUSDT | OKX PERP | radar / radar #0 | 30.10.2026 23:02 | 0.19045 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 0, "attempted": 0, "observed_ms": 1793390836497, "unique_reads": 0}, "summary": {"radar": {"market_event_references": 55, "unique_symbol_labels": 41, "note": "Markets, routes and repeated entries of one symbol are correlated; never summed as independent wins. Early radar is not entry.", "groups": {"OKX:SPOT:radar": {"event_references": 19, "first_per_symbol": 19, "hours": {"1": {"known_first_symbols": 16, "median_reference_return_pct": -0.3994187277049699}, "4": {"known_first_symbols": 9, "median_reference_return_pct": -0.8069939475453869}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "MEXC:SPOT:radar": {"event_references": 12, "first_per_symbol": 12, "hours": {"1": {"known_first_symbols": 11, "median_reference_return_pct": -0.2525252525252597}, "4": {"known_first_symbols": 5, "median_reference_return_pct": -0.5488043904351314}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "MEXC:PERP:radar": {"event_references": 16, "first_per_symbol": 16, "hours": {"1": {"known_first_symbols": 13, "median_reference_return_pct": -0.3593083314619383}, "4": {"known_first_symbols": 5, "median_reference_return_pct": -1.3923197844150081}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "OKX:PERP:radar": {"event_references": 8, "first_per_symbol": 8, "hours": {"1": {"known_first_symbols": 7, "median_reference_return_pct": -1.3846847427062658}, "4": {"known_first_symbols": 4, "median_reference_return_pct": -0.6491833476151454}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}}}, "triggered": {"market_event_references": 0, "unique_symbol_labels": 0, "note": "Markets, routes and repeated entries of one symbol are correlated; never summed as independent wins. Early radar is not entry.", "groups": {}}}}
