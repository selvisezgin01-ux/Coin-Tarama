# Coin Tarama5 — V4

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → geri test veya yukarıda yeni taban giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 31.10.2026 06:37 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 162, "p95_minutes": 5.61935, "longest_minutes": 55.56921666666667, "over_10_minutes": 1}, "within_session": {"intervals": 153, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 9, "p95_minutes": 55.56921666666667, "longest_minutes": 55.56921666666667, "over_10_minutes": 1}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| BIOUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 00:48 | 0.0217 | 0.0214 | 0.020860142 |
| BIOUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 00:48 | 0.021685 | 0.02139 | 0.020786291 |
| SPELLUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 00:53 | 8.225e-05 | 7.85e-05 | 7.5319201e-05 |
| IOUSDT | MEXC SPOT | 🟢🎯 GİRİŞ TEYİDİ | 31.10.2026 01:43 | 0.13705 | 0.13638 | 0.13654278 |
| RECALLUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 02:44 | 0.03475 | 0.03115 | 0.029249867 |
| SPKUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 03:14 | 0.019665 | 0.01883 | 0.018288567 |
| SPKUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 03:14 | 0.019665 | 0.01883 | 0.018277354 |
| STXUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 03:46 | 0.30065 | 0.289 | 0.28503667 |
| STXUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 03:46 | 0.30065 | 0.289 | 0.2851418 |
| PROSUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 05:01 | 0.56105 | 0.5732 | 0.55862023 |
| WOOUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 05:06 | 0.011065 | 0.01177 | 0.010929399 |
| CELOUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 05:31 | 0.075035 | 0.07497 | 0.073734795 |
| CELOUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 05:31 | 0.07465 | 0.07472 | 0.073439175 |
| NESUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 05:52 | 0.12425 | 0.1215 | 0.11905813 |
| RLSUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 06:02 | 0.0022485 | 0.002169 | 0.0021518854 |
| BULLAUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 06:07 | 0.07926 | 0.0778 | 0.075555005 |
| FLOKIUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 06:17 | 2.405e-05 | 2.42e-05 | 2.3799179e-05 |
| FLOKIUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 06:17 | 2.4015e-05 | 2.425e-05 | 2.3765078e-05 |
| AGLDUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 06:32 | 0.18855 | 0.1877 | 0.18383853 |
| AGLDUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 06:32 | 0.18845 | 0.188 | 0.18390433 |

## Kapsam ve eleme

{"observed_ms": 1793417859695, "new_radars": [], "liquid_tickers": 1272, "candles_evaluated": 135, "errors": {"OKX:PERP": [], "OKX:SPOT": [], "MEXC:PERP": [], "MEXC:SPOT": []}, "failed_groups": []}

OKX:PERP: {"active_catalog": 288, "instrument_categories": {"1": 304, "3": 219, "4": 9}, "valid_liquid_tickers": 288, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793417848060, "selected_for_candles": 35, "candles_evaluated": 35, "fresh_candidate_quotes": 10, "funnel": {"candles_evaluated": 35, "volume_not_accelerating": 21, "close_not_strong": 21, "price_structure_not_ready": 27, "already_extended": 1}, "calls": 23, "errors": []}

OKX:SPOT: {"active_catalog": 294, "instrument_categories": {"1": 1013, "4": 4, "3": 194}, "valid_liquid_tickers": 208, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793417848075, "selected_for_candles": 34, "candles_evaluated": 34, "fresh_candidate_quotes": 5, "funnel": {"candles_evaluated": 34, "volume_not_accelerating": 25, "close_not_strong": 25, "price_structure_not_ready": 30, "already_extended": 1}, "calls": 24, "errors": []}

MEXC:PERP: {"active_catalog": 569, "instrument_categories": {}, "valid_liquid_tickers": 546, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793417848709, "selected_for_candles": 34, "candles_evaluated": 34, "fresh_candidate_quotes": 4, "funnel": {"candles_evaluated": 34, "volume_not_accelerating": 29, "close_not_strong": 19, "price_structure_not_ready": 29, "already_extended": 4}, "calls": 30, "errors": []}

MEXC:SPOT: {"active_catalog": 1240, "instrument_categories": {}, "valid_liquid_tickers": 230, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793417849341, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 2, "funnel": {"candles_evaluated": 32, "volume_not_accelerating": 29, "close_not_strong": 18, "price_structure_not_ready": 25}, "calls": 30, "errors": []}

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
| BRUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 17:08 | 0.4864 | %-1.15 | %-3.06 | %-1.83 | — |
| HUMAUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:08 | 0.02887 | %+0.59 | %-2.67 | %-2.15 | — |
| ARKMUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:08 | 0.11046 | %+1.40 | %+0.31 | %+3.65 | — |
| PROVEUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:13 | 0.1955 | %+2.35 | %+2.92 | %+5.17 | — |
| BEAMXUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 17:13 | 0.0052475 | %-9.19 | %-9.98 | %-11.75 | — |
| LITUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:13 | 2.8186 | %+3.23 | %-2.88 | %-1.85 | — |
| WLDUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 18:19 | 0.4141 | %+0.07 | %-2.75 | %-2.97 | — |
| ZETAUSDT | OKX PERP | radar / radar #0 | 30.10.2026 18:19 | 0.03757 | %-1.57 | %-3.11 | %+0.45 | — |
| NEARUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 18:19 | 4.42085 | %-1.59 | %-3.39 | %-2.32 | — |
| TUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 18:24 | 0.0045505 | %-0.41 | %-2.54 | — | — |
| BREVUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 18:24 | 0.08922 | %-0.39 | %-0.81 | — | — |
| SAHARAUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 18:24 | 0.0075545 | %-0.67 | %-1.09 | — | — |
| BREVUSDT | OKX PERP | radar / radar #0 | 30.10.2026 18:24 | 0.08912 | %-0.18 | %-0.58 | %+0.26 | — |
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
| NEOUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 00:03 | 1.9965 | %+0.23 | %+1.38 | — | — |
| WIFUSDT | OKX PERP | radar / radar #0 | 31.10.2026 00:03 | 0.17605 | %+0.99 | %+0.48 | — | — |
| RENDERUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:13 | 1.5535 | %+1.38 | %+4.41 | — | — |
| WIFUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:18 | 0.17715 | %-0.08 | %-0.37 | — | — |
| WIFUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 00:18 | 0.17705 | %-0.20 | %-0.25 | — | — |
| WIFUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 00:18 | 0.17715 | %-0.08 | %-0.25 | — | — |
| RENDERUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 00:38 | 1.5715 | %+0.41 | %+2.51 | — | — |
| NFTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:43 | 2.345e-07 | %+0.17 | %-0.21 | — | — |
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
| IOUSDT | MEXC SPOT | triggered / retest #1 | 31.10.2026 02:04 | 0.137525 | %+0.37 | %-0.11 | — | — |
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
| IMXUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 03:56 | 0.12765 | %-0.82 | — | — | — |
| DGAIUSDT | OKX PERP | radar / radar #0 | 31.10.2026 03:56 | 0.78125 | %-0.03 | — | — | — |
| REUSDT | OKX PERP | radar / radar #0 | 31.10.2026 03:56 | 0.38363 | %-0.85 | — | — | — |
| IMXUSDT | OKX PERP | radar / radar #0 | 31.10.2026 04:01 | 0.127655 | %-1.37 | — | — | — |
| IMXUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 04:06 | 0.1276 | %-1.72 | — | — | — |
| ELSAUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 04:16 | 0.068965 | %-0.21 | — | — | — |
| RUNEUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 04:21 | 0.6621 | %+0.42 | — | — | — |
| WCTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 04:51 | 0.035885 | %-0.43 | — | — | — |
| RUNEUSDT | MEXC PERP | triggered / retest #1 | 31.10.2026 05:01 | 0.6651 | %-1.02 | — | — | — |
| METISUSDT | OKX PERP | radar / radar #0 | 31.10.2026 05:01 | 2.9175 | %-1.49 | — | — | — |
| PROSUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 05:01 | 0.56275 | %-0.03 | — | — | — |
| WOOUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 05:06 | 0.011615 | %-3.31 | — | — | — |
| TRXUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 05:16 | 0.34148 | %-2.33 | — | — | — |
| CELOUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 05:31 | 0.074955 | — | — | — | — |
| CELOUSDT | OKX PERP | radar / radar #0 | 31.10.2026 05:31 | 0.07457 | %+0.13 | — | — | — |
| NESUSDT | OKX PERP | radar / radar #0 | 31.10.2026 05:52 | 0.1227 | — | — | — | — |
| RLSUSDT | OKX PERP | radar / radar #0 | 31.10.2026 06:02 | 0.002202 | — | — | — | — |
| SPKUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 06:02 | 0.02006 | — | — | — | — |
| BULLAUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 06:07 | 0.079895 | — | — | — | — |
| FLOKIUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 06:17 | 2.408e-05 | — | — | — | — |
| FLOKIUSDT | OKX PERP | radar / radar #0 | 31.10.2026 06:17 | 2.404e-05 | — | — | — | — |
| AGLDUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 06:32 | 0.18825 | — | — | — | — |
| AGLDUSDT | OKX PERP | radar / radar #0 | 31.10.2026 06:32 | 0.18825 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 21, "attempted": 1, "observed_ms": 1793417579239, "unique_reads": 2}, "summary": {"radar": {"market_event_references": 115, "unique_symbol_labels": 79, "note": "Markets, routes and repeated entries of one symbol are correlated; never summed as independent wins. Early radar is not entry.", "groups": {"OKX:SPOT:radar": {"event_references": 40, "first_per_symbol": 40, "hours": {"1": {"known_first_symbols": 36, "median_reference_return_pct": -0.09253780575307347}, "4": {"known_first_symbols": 23, "median_reference_return_pct": -0.2132196162046851}, "12": {"known_first_symbols": 6, "median_reference_return_pct": 1.7220894018880661}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "MEXC:SPOT:radar": {"event_references": 23, "first_per_symbol": 23, "hours": {"1": {"known_first_symbols": 23, "median_reference_return_pct": -0.07302468234262616}, "4": {"known_first_symbols": 16, "median_reference_return_pct": -0.0856894437364919}, "12": {"known_first_symbols": 5, "median_reference_return_pct": 0.07302468234264836}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "MEXC:PERP:radar": {"event_references": 28, "first_per_symbol": 28, "hours": {"1": {"known_first_symbols": 27, "median_reference_return_pct": -0.04514672686229959}, "4": {"known_first_symbols": 20, "median_reference_return_pct": 0.05251400047151522}, "12": {"known_first_symbols": 4, "median_reference_return_pct": -0.9374582318522062}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "OKX:PERP:radar": {"event_references": 24, "first_per_symbol": 24, "hours": {"1": {"known_first_symbols": 20, "median_reference_return_pct": -0.5443331480782854}, "4": {"known_first_symbols": 10, "median_reference_return_pct": -0.43656406449675833}, "12": {"known_first_symbols": 4, "median_reference_return_pct": 0.35528384119839496}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}}}, "triggered": {"market_event_references": 2, "unique_symbol_labels": 2, "note": "Markets, routes and repeated entries of one symbol are correlated; never summed as independent wins. Early radar is not entry.", "groups": {"MEXC:SPOT:retest": {"event_references": 1, "first_per_symbol": 1, "hours": {"1": {"known_first_symbols": 1, "median_reference_return_pct": 0.3744773677513136}, "4": {"known_first_symbols": 1, "median_reference_return_pct": -0.10543537538629799}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "MEXC:PERP:retest": {"event_references": 1, "first_per_symbol": 1, "hours": {"1": {"known_first_symbols": 1, "median_reference_return_pct": -1.022402646218623}, "4": {"known_first_symbols": 0, "median_reference_return_pct": null}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}}}}}
