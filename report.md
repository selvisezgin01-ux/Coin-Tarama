# Coin Tarama5 — V4

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → geri test veya yukarıda yeni taban giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 31.10.2026 04:56 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 142, "p95_minutes": 5.61935, "longest_minutes": 55.56921666666667, "over_10_minutes": 1}, "within_session": {"intervals": 134, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 8, "p95_minutes": 55.56921666666667, "longest_minutes": 55.56921666666667, "over_10_minutes": 1}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| WOOUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 23:47 | 0.01166 | 0.01102 | 0.010733081 |
| WOOUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 23:47 | 0.011585 | 0.01104 | 0.010709904 |
| RENDERUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 23:52 | 1.613 | 1.558 | 1.5260206 |
| RENDERUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 00:13 | 1.609 | 1.554 | 1.5263324 |
| BIOUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 00:48 | 0.021855 | 0.0214 | 0.020860142 |
| BIOUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 00:48 | 0.021845 | 0.02139 | 0.020786291 |
| SPELLUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 00:53 | 8.195e-05 | 7.85e-05 | 7.5319201e-05 |
| IOUSDT | MEXC SPOT | 🟢🎯 GİRİŞ TEYİDİ | 31.10.2026 01:43 | 0.137395 | 0.13638 | 0.13654278 |
| RECALLUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 02:44 | 0.032025 | 0.03115 | 0.029249867 |
| SPKUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 03:14 | 0.019215 | 0.01883 | 0.018288567 |
| SPKUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 03:14 | 0.019175 | 0.01883 | 0.018277354 |
| STXUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 03:46 | 0.29605 | 0.289 | 0.28503667 |
| STXUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 03:46 | 0.29635 | 0.289 | 0.2851418 |
| DGAIUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 03:56 | 0.78065 | 0.78 | 0.77156022 |
| REUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 03:56 | 0.379965 | 0.37882 | 0.37213649 |
| RUNEUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 04:21 | 0.66555 | 0.66 | 0.64030082 |
| WCTUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 04:51 | 0.035825 | 0.03593 | 0.035153434 |

## Kapsam ve eleme

{"observed_ms": 1793411769862, "new_radars": [], "liquid_tickers": 1286, "candles_evaluated": 133, "errors": {"OKX:PERP": [], "MEXC:PERP": [], "MEXC:SPOT": [], "OKX:SPOT": []}, "failed_groups": []}

OKX:PERP: {"active_catalog": 288, "instrument_categories": {"1": 304, "3": 219, "4": 9}, "valid_liquid_tickers": 288, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793411760656, "selected_for_candles": 36, "candles_evaluated": 36, "fresh_candidate_quotes": 8, "funnel": {"candles_evaluated": 36, "volume_not_accelerating": 26, "close_not_strong": 23, "price_structure_not_ready": 27, "already_extended": 3}, "calls": 17, "errors": []}

OKX:SPOT: {"active_catalog": 294, "instrument_categories": {"1": 1013, "4": 4, "3": 194}, "valid_liquid_tickers": 212, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793411760665, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 7, "funnel": {"candles_evaluated": 32, "volume_not_accelerating": 18, "close_not_strong": 21, "price_structure_not_ready": 22, "already_extended": 1}, "calls": 29, "errors": []}

MEXC:PERP: {"active_catalog": 569, "instrument_categories": {}, "valid_liquid_tickers": 543, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793411760819, "selected_for_candles": 33, "candles_evaluated": 33, "fresh_candidate_quotes": 4, "funnel": {"candles_evaluated": 33, "volume_not_accelerating": 28, "close_not_strong": 19, "price_structure_not_ready": 20, "already_extended": 3}, "calls": 23, "errors": []}

MEXC:SPOT: {"active_catalog": 1240, "instrument_categories": {}, "valid_liquid_tickers": 243, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793411761184, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 2, "funnel": {"candles_evaluated": 32, "volume_not_accelerating": 27, "price_structure_not_ready": 28, "close_not_strong": 23}, "calls": 23, "errors": []}

Ayrıntılı evren/ret nedenleri ve seçilen kimlikler state içinde saklanır. Rolling24s hacim farkı yalnız sıralama vekilidir,5dk alım hacmi değildir. Hacim sinyali yalnız kapalı15dk gerçek quote hacmiyle ölçülür.4s trend/OI erken radarı engellemez.3yeni sembol/döngü,6yeni sembol/saat,20aktif sembol/80pazar sınırı vardır. Aynı sembol her borsada kendi fiyatıyla izlenir; yalnız tekrar eden erken bildirimler bastırılır; kota dışı fırsatlar kaçabilir.

## İlk gerçek gözlem ölçümleri

Radar ve giriş ayrı referanslardır, bağımsız iki başarı gibi toplanmaz. Her pazar/evre/giriş türünün gerçek referansı korunur; aynı sembol ve tekrar girişler bağımsız örnek sayılmaz; borsalar/pazarlar arası fiyatlar birleştirilmez. Eski V3 kayıtları değişmeyen arşiv commitinde korunur; eski ölçümler ayrı legacy_v3 alanında sürer.

| Coin | Pazar | Evre / giriş türü | Gözlem TR | Referans | 1s | 4s | 12s | 24s |
|---|---|---|---|---:|---|---|---|---|
| XPLUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 16:04 | 0.077915 | %-1.17 | %-0.65 | %+4.58 | — |
| EDGEUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 16:04 | 0.3428 | %+0.03 | %+2.95 | %-0.20 | — |
| EDGEUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 16:04 | 0.34235 | %-0.07 | %+3.20 | %+0.07 | — |
| REDUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 16:04 | 0.12365 | %-2.30 | %+1.33 | %+5.46 | — |
| EDGEUSDT | OKX PERP | radar / radar #0 | 30.10.2026 16:04 | 0.3423 | %-0.23 | %+3.13 | %+0.18 | — |
| XPLUSDT | OKX PERP | radar / radar #0 | 30.10.2026 16:09 | 0.077635 | %-1.38 | %-0.71 | %+4.77 | — |
| JUPUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 16:09 | 0.2551 | %-1.14 | %-0.55 | %+2.12 | — |
| 4USDT | MEXC PERP | radar / radar #0 | 30.10.2026 16:09 | 0.011075 | %-0.05 | %-0.14 | %-0.05 | — |
| IBVMUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 16:09 | 0.1188 | %-0.25 | %+0.34 | %+8.75 | — |
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
| GRTUSDT | OKX PERP | radar / radar #0 | 30.10.2026 19:24 | 0.021 | %-0.90 | %-3.95 | — | — |
| PLAYUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 19:24 | 0.013925 | %+3.48 | %+6.14 | — | — |
| GRASSUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 19:29 | 0.6026 | %+0.38 | %-2.42 | — | — |
| GRASSUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 19:29 | 0.60245 | %+0.44 | %-2.53 | — | — |
| ZROUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 19:29 | 1.76525 | %-0.68 | %-4.32 | — | — |
| BIANRENSHENGUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 19:34 | 0.53025 | %+0.25 | %-0.27 | — | — |
| CHIPUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 19:39 | 0.044335 | %-1.70 | %-0.89 | — | — |
| SENTUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 20:24 | 0.019105 | %+1.44 | %-0.03 | — | — |
| VIRTUALUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 20:24 | 0.5954 | %-0.82 | %+0.67 | — | — |
| VIRTUALUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 20:24 | 0.595 | %-0.77 | %+0.76 | — | — |
| EDENUSDT | OKX PERP | radar / radar #0 | 30.10.2026 20:29 | 0.05524 | %-2.44 | %-0.29 | — | — |
| MMTUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 20:29 | 0.1294 | %-1.16 | %+0.77 | — | — |
| SENTUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 20:34 | 0.01929 | %-0.31 | %-0.73 | — | — |
| AINUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 20:34 | 0.173475 | %+9.25 | %+1.70 | — | — |
| AIUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 20:39 | 0.016915 | %-0.98 | %+1.09 | — | — |
| SENTUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 20:49 | 0.019585 | %-2.02 | %-2.43 | — | — |
| SENTUSDT | OKX PERP | radar / radar #0 | 30.10.2026 20:49 | 0.01954 | %-2.00 | %-2.51 | — | — |
| AINUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 21:04 | 0.183775 | %-0.48 | %-1.12 | — | — |
| BULLAUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 21:29 | 0.073804 | %+0.78 | %+3.91 | — | — |
| PARTIUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 21:29 | 0.053295 | %-6.54 | %-6.28 | — | — |
| ILVUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 21:34 | 2.985 | %-2.51 | %-0.23 | — | — |
| GWEIUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 21:34 | 0.02216 | %+6.14 | %+1.81 | — | — |
| SIRENUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 22:00 | 0.02309 | %-1.21 | %-1.56 | — | — |
| XPLUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 22:00 | 0.078245 | %+3.52 | %+3.10 | — | — |
| ATOMUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 22:32 | 1.5085 | %+1.03 | %+2.75 | — | — |
| SPXUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 22:32 | 0.358 | %+0.34 | %+1.12 | — | — |
| UAIUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 22:36 | 0.2713 | %-0.70 | %-0.15 | — | — |
| CVXUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 22:47 | 1.992 | %-0.10 | %+0.40 | — | — |
| NIULAIUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 23:02 | 0.054305 | %-0.67 | %+1.00 | — | — |
| EIGENUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 23:02 | 0.1904 | %-0.26 | %+0.11 | — | — |
| EIGENUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 23:02 | 0.19055 | %-0.24 | %+0.13 | — | — |
| EIGENUSDT | OKX PERP | radar / radar #0 | 30.10.2026 23:02 | 0.19045 | %-0.24 | %+0.03 | — | — |
| ATOMUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 23:32 | 1.5215 | %+1.68 | %+1.94 | — | — |
| CAPUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 23:41 | 0.08354 | %+0.19 | %-0.02 | — | — |
| WOOUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 23:47 | 0.01104 | %+2.17 | %+5.16 | — | — |
| WOOUSDT | OKX PERP | radar / radar #0 | 30.10.2026 23:47 | 0.011025 | %+1.86 | %+5.12 | — | — |
| RENDERUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 23:52 | 1.5445 | %+1.39 | %+4.95 | — | — |
| HOLOUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 23:51 | 0.058635 | %+0.35 | %+0.54 | — | — |
| NEOUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 00:03 | 1.9965 | %+0.23 | — | — | — |
| WIFUSDT | OKX PERP | radar / radar #0 | 31.10.2026 00:03 | 0.17605 | %+0.99 | — | — | — |
| RENDERUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:13 | 1.5535 | %+1.38 | — | — | — |
| WIFUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:18 | 0.17715 | %-0.08 | — | — | — |
| WIFUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 00:18 | 0.17705 | %-0.20 | — | — | — |
| WIFUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 00:18 | 0.17715 | %-0.08 | — | — | — |
| RENDERUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 00:38 | 1.5715 | %+0.41 | — | — | — |
| NFTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:43 | 2.345e-07 | %+0.17 | — | — | — |
| BIOUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:48 | 0.021605 | %+1.83 | — | — | — |
| BIOUSDT | OKX PERP | radar / radar #0 | 31.10.2026 00:48 | 0.02158 | %+1.81 | — | — | — |
| KMNOUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:53 | 0.033065 | %+0.35 | — | — | — |
| SPELLUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 00:53 | 7.825e-05 | %+1.85 | — | — | — |
| CETUSUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 01:08 | 0.021015 | %+1.64 | — | — | — |
| POLUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 01:18 | 0.09547 | %-1.59 | — | — | — |
| POLUSDT | OKX PERP | radar / radar #0 | 31.10.2026 01:28 | 0.095815 | %-1.72 | — | — | — |
| IOUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 01:43 | 0.13712 | %+0.93 | — | — | — |
| POLUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 01:43 | 0.095645 | %-0.36 | — | — | — |
| SANDUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 01:54 | 0.046685 | %+0.67 | — | — | — |
| COMPUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 01:54 | 20.43 | %+0.44 | — | — | — |
| SANDUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 01:54 | 0.046725 | %+0.57 | — | — | — |
| ARUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 01:54 | 3.2145 | %+0.76 | — | — | — |
| IOUSDT | MEXC SPOT | triggered / retest #1 | 31.10.2026 02:04 | 0.137525 | %+0.37 | — | — | — |
| QUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 02:09 | 0.048233 | %+3.27 | — | — | — |
| 1INCHUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 02:19 | 0.08015 | %+0.46 | — | — | — |
| RECALLUSDT | OKX PERP | radar / radar #0 | 31.10.2026 02:44 | 0.032955 | %-2.26 | — | — | — |
| ARUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 02:54 | 3.238 | %-0.31 | — | — | — |
| COREUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 02:54 | 0.015525 | %-0.16 | — | — | — |
| CHZUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 02:54 | 0.012545 | %-0.20 | — | — | — |
| SPKUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 03:14 | 0.018925 | %+2.30 | — | — | — |
| SPKUSDT | OKX PERP | radar / radar #0 | 31.10.2026 03:14 | 0.01893 | %+2.17 | — | — | — |
| ROBOUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 03:19 | 0.0053115 | %-1.16 | — | — | — |
| STXUSDT | OKX PERP | radar / radar #0 | 31.10.2026 03:46 | 0.2923 | %+1.51 | — | — | — |
| STXUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 03:46 | 0.29235 | %+1.49 | — | — | — |
| IMXUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 03:56 | 0.12765 | — | — | — | — |
| DGAIUSDT | OKX PERP | radar / radar #0 | 31.10.2026 03:56 | 0.78125 | — | — | — | — |
| REUSDT | OKX PERP | radar / radar #0 | 31.10.2026 03:56 | 0.38363 | — | — | — | — |
| IMXUSDT | OKX PERP | radar / radar #0 | 31.10.2026 04:01 | 0.127655 | — | — | — | — |
| IMXUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 04:06 | 0.1276 | — | — | — | — |
| ELSAUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 04:16 | 0.068965 | — | — | — | — |
| RUNEUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 04:21 | 0.6621 | — | — | — | — |
| WCTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 04:51 | 0.035885 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 12, "attempted": 2, "observed_ms": 1793411487951, "unique_reads": 4}, "summary": {"radar": {"market_event_references": 101, "unique_symbol_labels": 71, "note": "Markets, routes and repeated entries of one symbol are correlated; never summed as independent wins. Early radar is not entry.", "groups": {"OKX:SPOT:radar": {"event_references": 34, "first_per_symbol": 34, "hours": {"1": {"known_first_symbols": 32, "median_reference_return_pct": -0.027751238246170873}, "4": {"known_first_symbols": 20, "median_reference_return_pct": -0.2715500947218452}, "12": {"known_first_symbols": 2, "median_reference_return_pct": 2.185649120518568}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "MEXC:SPOT:radar": {"event_references": 22, "first_per_symbol": 22, "hours": {"1": {"known_first_symbols": 22, "median_reference_return_pct": -0.0002892066627402379}, "4": {"known_first_symbols": 15, "median_reference_return_pct": -0.023940627244445345}, "12": {"known_first_symbols": 3, "median_reference_return_pct": 2.1168169345354926}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "MEXC:PERP:radar": {"event_references": 27, "first_per_symbol": 27, "hours": {"1": {"known_first_symbols": 24, "median_reference_return_pct": 0.09012385670407741}, "4": {"known_first_symbols": 17, "median_reference_return_pct": -0.02617115938234882}, "12": {"known_first_symbols": 2, "median_reference_return_pct": 2.7069050029254917}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "OKX:PERP:radar": {"event_references": 18, "first_per_symbol": 18, "hours": {"1": {"known_first_symbols": 15, "median_reference_return_pct": -0.23628248884222103}, "4": {"known_first_symbols": 9, "median_reference_return_pct": -0.5834829443447154}, "12": {"known_first_symbols": 2, "median_reference_return_pct": 2.4738084522919923}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}}}, "triggered": {"market_event_references": 1, "unique_symbol_labels": 1, "note": "Markets, routes and repeated entries of one symbol are correlated; never summed as independent wins. Early radar is not entry.", "groups": {"MEXC:SPOT:retest": {"event_references": 1, "first_per_symbol": 1, "hours": {"1": {"known_first_symbols": 1, "median_reference_return_pct": 0.3744773677513136}, "4": {"known_first_symbols": 0, "median_reference_return_pct": null}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}}}}}
