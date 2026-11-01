# Coin Tarama5 — V4

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → geri test veya yukarıda yeni taban giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 01.11.2026 08:49 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 470, "p95_minutes": 5.000016666666666, "longest_minutes": 55.56921666666667, "over_10_minutes": 1}, "within_session": {"intervals": 447, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 23, "p95_minutes": 9.628833333333333, "longest_minutes": 55.56921666666667, "over_10_minutes": 1}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| TRXUSDT | OKX PERP | 🟢🎯 GİRİŞ TEYİDİ | 01.11.2026 03:37 | 0.31135 | 0.30485 | 0.30543012 |
| FLRUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 01.11.2026 04:54 | 0.006085 | 0.006074 | 0.0060039949 |
| AAVEUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 01.11.2026 06:06 | 139.385 | 136.54 | 133.46836 |
| BRETTUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 01.11.2026 06:26 | 0.004427 | 0.004362 | 0.0043200708 |
| AEVOUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 01.11.2026 06:46 | 0.020505 | 0.02046 | 0.020250677 |
| CHIPUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 01.11.2026 07:49 | 0.042535 | 0.04253 | 0.041577886 |
| RUNEUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 01.11.2026 07:49 | 0.64355 | 0.6272 | 0.61168565 |
| AKEUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 01.11.2026 08:04 | 0.0101884 | 0.0096937 | 0.0086357656 |
| YFIUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 01.11.2026 08:09 | 1997.5 | 1967 | 1929.5488 |
| YFIUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 01.11.2026 08:09 | 1999.5 | 1967 | 1931.7542 |
| ZBCNUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 01.11.2026 08:09 | 0.0020001 | 0.002005 | 0.0019669949 |
| GTCUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 01.11.2026 08:34 | 0.23084 | 0.22518 | 0.2193959 |

## Kapsam ve eleme

{"observed_ms": 1793512169735, "new_radars": [], "liquid_tickers": 1199, "candles_evaluated": 130, "errors": {"OKX:PERP": [], "OKX:SPOT": [], "MEXC:SPOT": [], "MEXC:PERP": []}, "failed_groups": []}

OKX:PERP: {"active_catalog": 288, "instrument_categories": {"1": 304, "3": 219, "4": 9}, "valid_liquid_tickers": 281, "active_quotes_retained_outside_discovery": 1, "observed_ms": 1793512156756, "selected_for_candles": 34, "candles_evaluated": 34, "fresh_candidate_quotes": 7, "funnel": {"candles_evaluated": 34, "close_not_strong": 25, "volume_not_accelerating": 25, "price_structure_not_ready": 25}, "calls": 39, "errors": []}

OKX:SPOT: {"active_catalog": 294, "instrument_categories": {"1": 1013, "4": 4, "3": 194}, "valid_liquid_tickers": 179, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793512156769, "selected_for_candles": 31, "candles_evaluated": 31, "fresh_candidate_quotes": 5, "funnel": {"candles_evaluated": 31, "volume_not_accelerating": 21, "close_not_strong": 20, "price_structure_not_ready": 21, "already_extended": 2, "flat_price_or_volume": 1}, "calls": 39, "errors": []}

MEXC:PERP: {"active_catalog": 569, "instrument_categories": {}, "valid_liquid_tickers": 544, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793512156996, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 5, "funnel": {"candles_evaluated": 32, "volume_not_accelerating": 25, "close_not_strong": 22, "price_structure_not_ready": 22}, "calls": 39, "errors": []}

MEXC:SPOT: {"active_catalog": 1237, "instrument_categories": {}, "valid_liquid_tickers": 194, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793512156743, "selected_for_candles": 33, "candles_evaluated": 33, "fresh_candidate_quotes": 5, "funnel": {"candles_evaluated": 33, "volume_not_accelerating": 25, "price_structure_not_ready": 23, "close_not_strong": 20, "already_extended": 1}, "calls": 40, "errors": []}

Ayrıntılı evren/ret nedenleri ve seçilen kimlikler state içinde saklanır. Rolling24s hacim farkı yalnız sıralama vekilidir,5dk alım hacmi değildir. Hacim sinyali yalnız kapalı15dk gerçek quote hacmiyle ölçülür.4s trend/OI erken radarı engellemez.3yeni sembol/döngü,6yeni sembol/saat,20aktif sembol/80pazar sınırı vardır. Aynı sembol her borsada kendi fiyatıyla izlenir; yalnız tekrar eden erken bildirimler bastırılır; kota dışı fırsatlar kaçabilir.

## İlk gerçek gözlem ölçümleri

Radar ve giriş ayrı referanslardır, bağımsız iki başarı gibi toplanmaz. Her pazar/evre/giriş türünün gerçek referansı korunur; aynı sembol ve tekrar girişler bağımsız örnek sayılmaz; borsalar/pazarlar arası fiyatlar birleştirilmez. Eski V3 kayıtları değişmeyen arşiv commitinde korunur; eski ölçümler ayrı legacy_v3 alanında sürer.

| Coin | Pazar | Evre / giriş türü | Gözlem TR | Referans | 1s | 4s | 12s | 24s |
|---|---|---|---|---:|---|---|---|---|
| XPLUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 16:04 | 0.077915 | %-1.17 | %-0.65 | %+4.58 | %+4.02 |
| EDGEUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 16:04 | 0.3428 | %+0.03 | %+2.95 | %-0.20 | %-0.18 |
| EDGEUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 16:04 | 0.34235 | %-0.07 | %+3.20 | %+0.07 | %+0.04 |
| REDUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 16:04 | 0.12365 | %-2.30 | %+1.33 | %+5.46 | %+5.78 |
| EDGEUSDT | OKX PERP | radar / radar #0 | 30.10.2026 16:04 | 0.3423 | %-0.23 | %+3.13 | %+0.18 | %+0.00 |
| XPLUSDT | OKX PERP | radar / radar #0 | 30.10.2026 16:09 | 0.077635 | %-1.38 | %-0.71 | %+4.77 | %+4.06 |
| JUPUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 16:09 | 0.2551 | %-1.14 | %-0.55 | %+2.12 | %+1.14 |
| 4USDT | MEXC PERP | radar / radar #0 | 30.10.2026 16:09 | 0.011075 | %-0.05 | %-0.14 | %-0.05 | %+1.22 |
| IBVMUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 16:09 | 0.1188 | %-0.25 | %+0.34 | %+8.75 | %+14.65 |
| BRUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 17:08 | 0.4864 | %-1.15 | %-3.06 | %-1.83 | %+2.20 |
| HUMAUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:08 | 0.02887 | %+0.59 | %-2.67 | %-2.15 | %-2.49 |
| ARKMUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:08 | 0.11046 | %+1.40 | %+0.31 | %+3.65 | %+2.16 |
| PROVEUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:13 | 0.1955 | %+2.35 | %+2.92 | %+5.17 | %+8.75 |
| BEAMXUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 17:13 | 0.0052475 | %-9.19 | %-9.98 | %-11.75 | %-6.72 |
| LITUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:13 | 2.8186 | %+3.23 | %-2.88 | %-1.85 | %-3.17 |
| WLDUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 18:19 | 0.4141 | %+0.07 | %-2.75 | %-2.97 | %-2.95 |
| ZETAUSDT | OKX PERP | radar / radar #0 | 30.10.2026 18:19 | 0.03757 | %-1.57 | %-3.11 | %+0.45 | %-1.52 |
| NEARUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 18:19 | 4.42085 | %-1.59 | %-3.39 | %-2.32 | %+0.30 |
| TUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 18:24 | 0.0045505 | %-0.41 | %-2.54 | %-0.08 | %-0.05 |
| BREVUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 18:24 | 0.08922 | %-0.39 | %-0.81 | %+0.18 | %-2.48 |
| SAHARAUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 18:24 | 0.0075545 | %-0.67 | %-1.09 | %+0.38 | %-1.91 |
| BREVUSDT | OKX PERP | radar / radar #0 | 30.10.2026 18:24 | 0.08912 | %-0.18 | %-0.58 | %+0.26 | %-2.82 |
| BREVUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 18:29 | 0.08906 | %-0.36 | %-1.39 | %-0.98 | %-2.57 |
| GRTUSDT | OKX PERP | radar / radar #0 | 30.10.2026 19:24 | 0.021 | %-0.90 | %-3.95 | %-2.95 | %-0.24 |
| PLAYUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 19:24 | 0.013925 | %+3.48 | %+6.14 | %+11.67 | %+10.66 |
| GRASSUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 19:29 | 0.6026 | %+0.38 | %-2.42 | %-3.50 | %-2.56 |
| GRASSUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 19:29 | 0.60245 | %+0.44 | %-2.53 | %-3.36 | %-2.60 |
| ZROUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 19:29 | 1.76525 | %-0.68 | %-4.32 | %-3.71 | %+1.26 |
| BIANRENSHENGUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 19:34 | 0.53025 | %+0.25 | %-0.27 | %-1.90 | %-0.76 |
| CHIPUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 19:39 | 0.044335 | %-1.70 | %-0.89 | %-0.62 | %-1.86 |
| SENTUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 20:24 | 0.019105 | %+1.44 | %-0.03 | %-2.85 | %+1.33 |
| VIRTUALUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 20:24 | 0.5954 | %-0.82 | %+0.67 | %-1.01 | %-0.42 |
| VIRTUALUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 20:24 | 0.595 | %-0.77 | %+0.76 | %-1.06 | %-0.47 |
| EDENUSDT | OKX PERP | radar / radar #0 | 30.10.2026 20:29 | 0.05524 | %-2.44 | %-0.29 | %+1.38 | %+3.57 |
| MMTUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 20:29 | 0.1294 | %-1.16 | %+0.77 | %-0.62 | %-0.62 |
| SENTUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 20:34 | 0.01929 | %-0.31 | %-0.73 | %-3.63 | %+0.41 |
| AINUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 20:34 | 0.173475 | %+9.25 | %+1.70 | %+50.19 | %+32.81 |
| AIUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 20:39 | 0.016915 | %-0.98 | %+1.09 | %+1.33 | %+1.98 |
| SENTUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 20:49 | 0.019585 | %-2.02 | %-2.43 | %-4.88 | %-0.94 |
| SENTUSDT | OKX PERP | radar / radar #0 | 30.10.2026 20:49 | 0.01954 | %-2.00 | %-2.51 | %-5.07 | %-0.87 |
| AINUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 21:04 | 0.183775 | %-0.48 | %-1.12 | %+53.51 | %+24.78 |
| BULLAUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 21:29 | 0.073804 | %+0.78 | %+3.91 | %+15.64 | %-4.32 |
| PARTIUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 21:29 | 0.053295 | %-6.54 | %-6.28 | %-8.47 | — |
| ILVUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 21:34 | 2.985 | %-2.51 | %-0.23 | %+1.47 | %+3.05 |
| GWEIUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 21:34 | 0.02216 | %+6.14 | %+1.81 | %-1.22 | %-2.98 |
| SIRENUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 22:00 | 0.02309 | %-1.21 | %-1.56 | %+5.28 | %+3.38 |
| XPLUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 22:00 | 0.078245 | %+3.52 | %+3.10 | %+2.87 | %+2.82 |
| ATOMUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 22:32 | 1.5085 | %+1.03 | %+2.75 | %+0.36 | %+0.10 |
| SPXUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 22:32 | 0.358 | %+0.34 | %+1.12 | %-1.40 | %-0.84 |
| UAIUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 22:36 | 0.2713 | %-0.70 | %-0.15 | %+1.14 | %+13.97 |
| CVXUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 22:47 | 1.992 | %-0.10 | %+0.40 | %+0.15 | %+2.71 |
| NIULAIUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 23:02 | 0.054305 | %-0.67 | %+1.00 | %-2.42 | %+12.16 |
| EIGENUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 23:02 | 0.1904 | %-0.26 | %+0.11 | %-2.10 | %-1.63 |
| EIGENUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 23:02 | 0.19055 | %-0.24 | %+0.13 | %-2.23 | %-1.23 |
| EIGENUSDT | OKX PERP | radar / radar #0 | 30.10.2026 23:02 | 0.19045 | %-0.24 | %+0.03 | %-2.34 | %-1.39 |
| ATOMUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 23:32 | 1.5215 | %+1.68 | %+1.94 | %-0.89 | %-1.35 |
| CAPUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 23:41 | 0.08354 | %+0.19 | %-0.02 | %+5.69 | %-11.25 |
| WOOUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 23:47 | 0.01104 | %+2.17 | %+5.16 | %+3.71 | %+4.44 |
| WOOUSDT | OKX PERP | radar / radar #0 | 30.10.2026 23:47 | 0.011025 | %+1.86 | %+5.12 | %+3.58 | %+4.76 |
| RENDERUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 23:52 | 1.5445 | %+1.39 | %+4.95 | %+1.39 | %+1.13 |
| HOLOUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 23:51 | 0.058635 | %+0.35 | %+0.54 | %-1.65 | %-2.17 |
| NEOUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 00:03 | 1.9965 | %+0.23 | %+1.38 | %-0.53 | %-0.38 |
| WIFUSDT | OKX PERP | radar / radar #0 | 31.10.2026 00:03 | 0.17605 | %+0.99 | %+0.48 | %-0.03 | %-0.26 |
| RENDERUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:13 | 1.5535 | %+1.38 | %+4.41 | %+1.13 | %+0.80 |
| WIFUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:18 | 0.17715 | %-0.08 | %-0.37 | %-0.76 | %-0.71 |
| WIFUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 00:18 | 0.17705 | %-0.20 | %-0.25 | %-0.82 | %-0.71 |
| WIFUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 00:18 | 0.17715 | %-0.08 | %-0.25 | %-0.65 | %-0.65 |
| RENDERUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 00:38 | 1.5715 | %+0.41 | %+2.51 | %-0.22 | %-0.35 |
| NFTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:43 | 2.345e-07 | %+0.17 | %-0.21 | %-0.04 | %-0.38 |
| BIOUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:48 | 0.021605 | %+1.83 | %+1.37 | %-1.00 | %-0.21 |
| BIOUSDT | OKX PERP | radar / radar #0 | 31.10.2026 00:48 | 0.02158 | %+1.81 | %+1.20 | %-1.07 | %-0.28 |
| KMNOUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:53 | 0.033065 | %+0.35 | %-0.71 | %-4.52 | %-0.53 |
| SPELLUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 00:53 | 7.825e-05 | %+1.85 | %+4.66 | %-0.58 | %+0.45 |
| CETUSUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 01:08 | 0.021015 | %+1.64 | %-0.93 | %-0.26 | %-0.64 |
| POLUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 01:18 | 0.09547 | %-1.59 | %-1.61 | %-3.56 | %-3.48 |
| POLUSDT | OKX PERP | radar / radar #0 | 31.10.2026 01:28 | 0.095815 | %-1.72 | %-2.40 | %-4.23 | %-3.98 |
| IOUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 01:43 | 0.13712 | %+0.93 | %+0.34 | %-1.22 | %-2.52 |
| POLUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 01:43 | 0.095645 | %-0.36 | %-2.03 | %-4.03 | %-3.87 |
| SANDUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 01:54 | 0.046685 | %+0.67 | %+0.61 | %-0.35 | %-1.00 |
| COMPUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 01:54 | 20.43 | %+0.44 | %-0.20 | %-0.93 | %-0.05 |
| SANDUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 01:54 | 0.046725 | %+0.57 | %+0.33 | %-0.46 | %-1.00 |
| ARUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 01:54 | 3.2145 | %+0.76 | %-0.67 | %-1.54 | %-1.70 |
| IOUSDT | MEXC SPOT | triggered / retest #1 | 31.10.2026 02:04 | 0.137525 | %+0.37 | %-0.11 | %-1.45 | %-3.09 |
| QUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 02:09 | 0.048233 | %+3.27 | %-26.38 | %-31.40 | — |
| 1INCHUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 02:19 | 0.08015 | %+0.46 | %-0.22 | %-0.65 | — |
| RECALLUSDT | OKX PERP | radar / radar #0 | 31.10.2026 02:44 | 0.032955 | %-2.26 | %+4.51 | %-4.23 | — |
| ARUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 02:54 | 3.238 | %-0.31 | %-2.07 | %-2.13 | — |
| COREUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 02:54 | 0.015525 | %-0.16 | %-1.00 | %-7.44 | — |
| CHZUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 02:54 | 0.012545 | %-0.20 | %-0.92 | %-1.63 | — |
| SPKUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 03:14 | 0.018925 | %+2.30 | %+5.79 | %-4.20 | — |
| SPKUSDT | OKX PERP | radar / radar #0 | 31.10.2026 03:14 | 0.01893 | %+2.17 | %+5.76 | %-4.17 | — |
| ROBOUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 03:19 | 0.0053115 | %-1.16 | %-1.52 | %-7.22 | — |
| STXUSDT | OKX PERP | radar / radar #0 | 31.10.2026 03:46 | 0.2923 | %+1.51 | %+1.85 | %+12.66 | — |
| STXUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 03:46 | 0.29235 | %+1.49 | %+1.93 | %+12.81 | — |
| IMXUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 03:56 | 0.12765 | %-0.82 | %-4.11 | %-3.49 | — |
| DGAIUSDT | OKX PERP | radar / radar #0 | 31.10.2026 03:56 | 0.78125 | %-0.03 | %-0.61 | %-0.53 | — |
| REUSDT | OKX PERP | radar / radar #0 | 31.10.2026 03:56 | 0.38363 | %-0.85 | %-1.35 | %-8.93 | — |
| IMXUSDT | OKX PERP | radar / radar #0 | 31.10.2026 04:01 | 0.127655 | %-1.37 | %-4.09 | %-3.80 | — |
| IMXUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 04:06 | 0.1276 | %-1.72 | %-3.84 | %-3.61 | — |
| ELSAUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 04:16 | 0.068965 | %-0.21 | %+2.36 | %+0.65 | — |
| RUNEUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 04:21 | 0.6621 | %+0.42 | %+1.60 | %+7.66 | — |
| WCTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 04:51 | 0.035885 | %-0.43 | %-3.36 | %-3.00 | — |
| RUNEUSDT | MEXC PERP | triggered / retest #1 | 31.10.2026 05:01 | 0.6651 | %-1.02 | %-0.38 | %+5.58 | %-7.26 |
| METISUSDT | OKX PERP | radar / radar #0 | 31.10.2026 05:01 | 2.9175 | %-1.49 | %-1.97 | %-0.63 | — |
| PROSUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 05:01 | 0.56275 | %-0.03 | %-2.00 | %-2.35 | — |
| WOOUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 05:06 | 0.011615 | %-3.31 | %-3.92 | %+1.94 | — |
| TRXUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 05:16 | 0.34148 | %-2.33 | %-3.09 | %-6.71 | — |
| CELOUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 05:31 | 0.074955 | %+0.26 | %-0.82 | %+3.02 | — |
| CELOUSDT | OKX PERP | radar / radar #0 | 31.10.2026 05:31 | 0.07457 | %+0.13 | %-0.75 | %+3.06 | — |
| NESUSDT | OKX PERP | radar / radar #0 | 31.10.2026 05:52 | 0.1227 | %+1.79 | %+0.90 | %+2.04 | — |
| RLSUSDT | OKX PERP | radar / radar #0 | 31.10.2026 06:02 | 0.002202 | %+1.82 | %+3.22 | %+2.45 | — |
| SPKUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 06:02 | 0.02006 | %+0.25 | %-1.20 | %-10.37 | — |
| BULLAUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 06:07 | 0.079895 | %-0.98 | %+5.78 | %-12.70 | — |
| FLOKIUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 06:17 | 2.408e-05 | %-0.04 | %-1.66 | %-2.33 | — |
| FLOKIUSDT | OKX PERP | radar / radar #0 | 31.10.2026 06:17 | 2.404e-05 | %-0.04 | %-1.71 | %-2.16 | — |
| AGLDUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 06:32 | 0.18825 | %+0.72 | %+0.88 | %-1.35 | — |
| AGLDUSDT | OKX PERP | radar / radar #0 | 31.10.2026 06:32 | 0.18825 | %+0.66 | %+0.82 | %-1.67 | — |
| BLESSUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 06:52 | 0.010195 | %+3.82 | %-2.41 | %+3.33 | — |
| MASKUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 07:02 | 0.38735 | %-0.76 | %-0.76 | %+1.07 | — |
| ENJUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 07:02 | 0.02417 | %-0.62 | %-0.99 | %+0.58 | — |
| NMRUSDT | OKX PERP | radar / radar #0 | 31.10.2026 07:12 | 9.434 | %-0.07 | %+0.11 | %+7.94 | — |
| LAYERUSDT | OKX PERP | radar / radar #0 | 31.10.2026 07:17 | 0.06093 | %-0.64 | %-0.95 | %+0.67 | — |
| BULLAUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 07:34 | 0.0819365 | %+4.93 | %-8.82 | %-13.30 | — |
| NMRUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 07:39 | 9.4595 | %-0.87 | %+0.07 | %+5.89 | — |
| LYNUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 08:09 | 0.01439 | %-2.71 | %-3.47 | %+0.07 | %-0.83 |
| GTCUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 08:09 | 0.23017 | %-2.12 | %-1.83 | %-2.40 | %-2.36 |
| SOMIUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 08:14 | 0.19855 | %-1.18 | %-4.31 | %-2.64 | %-5.01 |
| AGLDUSDT | OKX SPOT | triggered / retest #1 | 31.10.2026 08:19 | 0.19015 | %-0.39 | %-0.87 | %+0.76 | %-0.87 |
| RESOLVUSDT | OKX PERP | radar / radar #0 | 31.10.2026 08:19 | 0.015505 | %+0.03 | %-1.00 | %-0.10 | %-1.77 |
| ZORAUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 08:19 | 0.006236 | %-0.32 | %-1.92 | %-2.00 | %-4.83 |
| RESOLVUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 08:29 | 0.015545 | %+0.16 | %-1.13 | — | — |
| JELLYJELLYUSDT | OKX PERP | radar / radar #0 | 31.10.2026 08:44 | 0.043235 | %+0.57 | %-0.84 | — | — |
| MAGMAUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 09:20 | 0.3914 | %+8.02 | %+4.94 | %+8.43 | — |
| MAGMAUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 09:20 | 0.390785 | %+7.83 | %+5.17 | — | — |
| MERLUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 09:20 | 0.02919 | %-0.51 | %+3.46 | — | — |
| TIAUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 09:25 | 0.47885 | %-0.24 | %-0.74 | %+0.18 | — |
| DOSUSDT | OKX PERP | radar / radar #0 | 31.10.2026 09:25 | 0.2137 | %-0.37 | %+3.46 | %-4.82 | — |
| ZROUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 09:25 | 1.71 | %-0.61 | %+2.61 | %+4.04 | — |
| RSRUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 09:45 | 0.001464 | %-1.09 | %+0.48 | %+6.76 | — |
| RSRUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 09:45 | 0.001464 | %-1.23 | %+0.27 | %+6.83 | — |
| RSRUSDT | OKX PERP | radar / radar #0 | 31.10.2026 09:45 | 0.0014635 | %-1.13 | %+0.31 | %+6.66 | — |
| RSRUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 09:45 | 0.0014685 | %-1.19 | %+0.31 | %+6.64 | — |
| BSBUSDT | OKX PERP | radar / radar #0 | 31.10.2026 10:25 | 0.09666 | %-1.40 | %-2.75 | %-0.97 | — |
| KITEUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 10:30 | 0.108585 | %-0.10 | %+1.06 | %+5.68 | — |
| ZAMAUSDT | OKX PERP | radar / radar #0 | 31.10.2026 10:30 | 0.06592 | %-0.68 | %-1.97 | %+4.29 | — |
| ZAMAUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 10:30 | 0.065895 | %-0.69 | %-1.81 | %+4.26 | — |
| ASTERUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 10:30 | 0.69135 | %-0.12 | %+0.05 | %+1.86 | — |
| ZAMAUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 10:30 | 0.065855 | %-0.31 | %-1.78 | %+4.38 | — |
| KITEUSDT | OKX PERP | radar / radar #0 | 31.10.2026 10:30 | 0.108495 | %-0.39 | %+0.83 | %+5.65 | — |
| EVAAUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 10:35 | 1.21095 | %-0.05 | %+4.01 | %+18.63 | — |
| UPUSDT | OKX PERP | radar / radar #0 | 31.10.2026 11:00 | 0.11995 | %+3.13 | %+10.13 | %+5.63 | — |
| RLCUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 11:27 | 0.47025 | %+1.14 | %+2.58 | %+2.29 | — |
| APRUSDT | OKX PERP | radar / radar #0 | 31.10.2026 11:32 | 0.055895 | %-1.87 | %-4.36 | %-3.19 | — |
| SKYUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 11:32 | 0.06792 | %+1.00 | %+0.35 | %-1.38 | — |
| ZROUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 11:37 | 1.70995 | %+2.97 | %+1.35 | %+4.74 | — |
| HBARUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 11:42 | 0.07216 | %+0.49 | %+0.68 | %+0.12 | — |
| TACUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 12:02 | 0.0011755 | %-1.40 | %-1.06 | %-4.21 | — |
| ZROUSDT | OKX PERP | radar / radar #0 | 31.10.2026 12:02 | 1.74065 | %+0.30 | %-0.48 | %+3.54 | — |
| QNTUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 12:32 | 197.125 | %+0.18 | %+1.79 | %+1.42 | — |
| BATUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 12:42 | 0.130415 | %+0.60 | %+2.32 | %+8.65 | — |
| BABYUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 12:42 | 0.0121925 | %+0.55 | %+1.77 | %+1.03 | — |
| GRVTUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 12:47 | 0.21775 | %+0.44 | %+0.85 | %-0.16 | — |
| APTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 12:47 | 0.6357 | %-0.36 | %+0.61 | %-0.31 | — |
| GRVTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 12:52 | 0.21821 | %+0.10 | %+0.53 | %-0.38 | — |
| GRVTUSDT | OKX PERP | radar / radar #0 | 31.10.2026 12:57 | 0.218685 | %-0.48 | %+0.05 | %-0.61 | — |
| UAIUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 13:05 | 0.29585 | %-0.63 | %+8.13 | %+4.99 | — |
| GRTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 13:35 | 0.02051 | %+0.29 | %+0.88 | %+0.54 | — |
| THETAUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 13:44 | 0.16065 | %+0.47 | %+0.53 | %-0.90 | — |
| GPSUSDT | OKX PERP | radar / radar #0 | 31.10.2026 13:44 | 0.0077145 | %-0.42 | %+0.46 | %+0.41 | — |
| OLUSDT | OKX PERP | radar / radar #0 | 31.10.2026 13:49 | 0.0064965 | %+0.48 | %+0.30 | %+2.32 | — |
| POWRUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 13:50 | 0.05751 | %-1.06 | %-1.20 | %-1.58 | — |
| OLUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 13:50 | 0.006506 | %+0.52 | %+0.12 | %+3.18 | — |
| OFCUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 14:05 | 0.006317 | %-0.17 | %-0.51 | %-1.52 | — |
| CSPRUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 14:35 | 0.002232 | %-0.63 | %-3.14 | %-5.69 | — |
| NEOUSDT | OKX PERP | radar / radar #0 | 31.10.2026 14:44 | 1.987 | %+0.20 | %+1.21 | %-0.20 | — |
| BLENDUSDT | OKX PERP | radar / radar #0 | 31.10.2026 14:44 | 0.053005 | %-0.50 | %-1.73 | %-1.18 | — |
| AVNTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 14:50 | 0.09456 | %-0.45 | %+1.67 | %-0.95 | — |
| METUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 14:50 | 0.28215 | %+0.51 | %+2.14 | %+0.55 | — |
| AWEUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 15:07 | 0.073605 | %+0.18 | %-0.56 | %-0.63 | — |
| NEARUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 15:37 | 4.407 | %-0.07 | %+2.29 | %+0.68 | — |
| NEARUSDT | OKX PERP | radar / radar #0 | 31.10.2026 15:37 | 4.4065 | %-0.03 | %+2.30 | %+0.69 | — |
| DATAUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 15:47 | 0.131 | %+0.23 | %+0.23 | %-0.69 | — |
| BATUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 15:47 | 0.135075 | %-1.23 | %+1.81 | %+3.65 | — |
| BATUSDT | OKX PERP | radar / radar #0 | 31.10.2026 15:47 | 0.13503 | %-1.14 | %+1.84 | %+3.67 | — |
| CROUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 15:52 | 0.051585 | %-0.11 | %+0.18 | %-0.09 | — |
| EGLDUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 15:52 | 3.4125 | %+0.31 | %+1.36 | %-0.01 | — |
| JCTUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 16:22 | 0.0059275 | %-10.30 | %-14.58 | %-20.84 | — |
| LSKUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 16:42 | 0.311485 | %-6.37 | — | — | — |
| LSKUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 16:42 | 0.311625 | %-6.61 | %-9.80 | %-23.31 | — |
| CPUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 16:49 | 0.0080635 | %-0.42 | — | — | — |
| 4USDT | MEXC SPOT | radar / radar #0 | 31.10.2026 16:49 | 0.01133 | %-0.88 | — | — | — |
| XDPUSDT | OKX PERP | radar / radar #0 | 31.10.2026 16:54 | 0.017665 | %-1.22 | — | — | — |
| XDPUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 16:54 | 0.0176725 | %-1.13 | — | — | — |
| GLMUSDT | OKX PERP | radar / radar #0 | 31.10.2026 16:54 | 0.11671 | %-1.87 | — | — | — |
| UPCUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 17:24 | 0.1217 | %-1.56 | — | — | — |
| CELOUSDT | OKX PERP | radar / radar #0 | 31.10.2026 17:44 | 0.07703 | %-0.83 | — | — | — |
| MORPHOUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 17:54 | 2.2351 | %+3.10 | — | — | — |
| SHIBUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 17:59 | 4.7155e-06 | %+0.07 | — | — | — |
| MORPHOUSDT | OKX PERP | radar / radar #0 | 31.10.2026 18:04 | 2.2543 | %+2.83 | — | — | — |
| ARBUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 18:04 | 0.163455 | %+0.72 | — | — | — |
| CTUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 18:04 | 0.140735 | %+2.16 | — | — | — |
| DYDXUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 18:24 | 0.10667 | %+0.81 | — | — | — |
| ARBUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 18:42 | 0.165425 | %-0.43 | — | — | — |
| ZAMAUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 18:47 | 0.065295 | %+3.39 | — | — | — |
| ZAMAUSDT | OKX PERP | radar / radar #0 | 31.10.2026 18:47 | 0.06528 | %+3.46 | — | — | — |
| ETHFIUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 18:57 | 0.63805 | %+0.79 | — | — | — |
| ETHFIUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 18:57 | 0.6382 | %+0.81 | — | — | — |
| ETHFIUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 18:57 | 0.63655 | %+0.93 | — | — | — |
| ETHFIUSDT | OKX PERP | radar / radar #0 | 31.10.2026 18:57 | 0.63705 | %+0.95 | — | — | — |
| AGLDUSDT | OKX PERP | radar / radar #0 | 31.10.2026 19:02 | 0.18845 | %+1.35 | — | — | — |
| REUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 19:07 | 0.364175 | %+1.79 | — | — | — |
| CTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 19:07 | 0.143975 | %-0.71 | — | — | — |
| ZAMAUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 19:17 | 0.06739 | %+1.04 | — | — | — |
| ORDERUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 19:27 | 0.036215 | %+1.04 | — | — | — |
| ORDERUSDT | OKX PERP | radar / radar #0 | 31.10.2026 19:27 | 0.036165 | %+1.12 | — | — | — |
| REUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 19:27 | 0.36965 | %+0.28 | — | — | — |
| RAREUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 19:52 | 0.013385 | %-1.38 | — | — | — |
| HANAUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 20:02 | 0.015828 | %-0.67 | — | — | — |
| ZAMAUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 20:17 | 0.068225 | %+0.24 | — | — | — |
| AGLDUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 20:22 | 0.1924 | %-0.42 | — | — | — |
| MERLUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 20:27 | 0.030905 | %-0.24 | — | — | — |
| MEYUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 20:44 | 0.044895 | %-1.55 | — | — | — |
| BTWUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 21:04 | 1.1196585 | %-1.24 | — | — | — |
| AEONUSDT | OKX PERP | radar / radar #0 | 31.10.2026 21:09 | 0.024105 | — | — | — | — |
| AEONUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 21:14 | 0.024185 | %-0.56 | — | — | — |
| ALLOUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 21:19 | 0.167915 | %-1.10 | — | — | — |
| IOTAUSDT | OKX PERP | radar / radar #0 | 31.10.2026 21:24 | 0.040445 | %-0.98 | — | — | — |
| LITUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 21:29 | 2.99465 | %-0.30 | — | — | — |
| LITUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 21:29 | 2.99535 | %-0.29 | — | — | — |
| LITUSDT | OKX PERP | radar / radar #0 | 31.10.2026 21:29 | 2.99155 | %-0.17 | — | — | — |
| ESPORTSUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 21:49 | 0.0097235 | %-2.47 | — | — | — |
| LITUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 21:49 | 3.01395 | %+2.04 | — | — | — |
| TAGUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 22:19 | 0.0007707 | %-2.14 | — | — | — |
| UNIUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 22:19 | 7.111 | %-0.38 | — | — | — |
| LINKUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 22:19 | 11.84 | %+0.72 | — | — | — |
| NESUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 22:27 | 0.13005 | %+0.35 | — | — | — |
| BULLAUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 22:32 | 0.0717965 | %-0.12 | — | — | — |
| NESUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 22:32 | 0.13025 | %+0.19 | — | — | — |
| RLSUSDT | OKX PERP | radar / radar #0 | 31.10.2026 22:51 | 0.0023005 | %+1.85 | — | — | — |
| STABLEUSDT | OKX PERP | radar / radar #0 | 31.10.2026 23:22 | 0.026605 | %-0.47 | — | — | — |
| DATAUSDT | OKX PERP | radar / radar #0 | 31.10.2026 23:22 | 0.13155 | %-0.49 | — | — | — |
| DATAUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 23:21 | 0.13175 | %-0.57 | — | — | — |
| GLMRUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 23:32 | 0.0082585 | %-1.76 | — | — | — |
| HANAUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 23:32 | 0.015795 | %-0.22 | — | — | — |
| LAUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 23:36 | 0.056395 | %+3.64 | — | — | — |
| LAUSDT | OKX PERP | radar / radar #0 | 31.10.2026 23:47 | 0.056665 | %+2.80 | — | — | — |
| ZORAUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 00:06 | 0.006086 | %-0.39 | — | — | — |
| ORDIUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 00:29 | 3.508 | %+0.31 | — | — | — |
| AIOTUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 00:29 | 0.0866395 | %+2.03 | — | — | — |
| FARTCOINUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 00:34 | 0.12092 | %-0.22 | — | — | — |
| KAITOUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 00:34 | 0.2404 | %-0.25 | — | — | — |
| HBARUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 00:39 | 0.072335 | %-0.28 | — | — | — |
| AIOTUSDT | MEXC SPOT | triggered / retest #1 | 01.11.2026 01:04 | 0.0873525 | %-0.06 | %+1.09 | — | — |
| ZBCNUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 01:09 | 0.00199585 | %-0.67 | — | — | — |
| BIOUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 01:29 | 0.021645 | %-0.35 | — | — | — |
| FLUIDUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 01:34 | 1.81195 | %-0.99 | — | — | — |
| IRYSUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 01:34 | 0.022995 | %+1.33 | — | — | — |
| SYRUPUSDT | MEXC PERP | radar / radar #0 | 01.11.2026 01:39 | 0.16135 | %-1.33 | — | — | — |
| SPCMUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 01:44 | 0.0008315 | %-0.01 | — | — | — |
| ALEOUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 02:12 | 0.032195 | %+0.79 | — | — | — |
| INITUSDT | OKX PERP | radar / radar #0 | 01.11.2026 02:32 | 0.181525 | %+1.91 | — | — | — |
| INITUSDT | MEXC PERP | radar / radar #0 | 01.11.2026 02:32 | 0.181635 | %+1.84 | — | — | — |
| WETUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 02:37 | 0.05923 | %+3.19 | — | — | — |
| WETUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 02:37 | 0.05923 | %+3.26 | — | — | — |
| JCTUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 02:42 | 0.004824 | %+0.02 | — | — | — |
| IRYSUSDT | MEXC PERP | radar / radar #0 | 01.11.2026 02:42 | 0.023185 | %-2.78 | — | — | — |
| IRYSUSDT | OKX PERP | radar / radar #0 | 01.11.2026 02:42 | 0.023205 | %-2.82 | — | — | — |
| 1000RATSUSDT | MEXC PERP | radar / radar #0 | 01.11.2026 02:47 | 0.015245 | %-0.16 | — | — | — |
| WETUSDT | OKX SPOT | triggered / retest #1 | 01.11.2026 03:02 | 0.059455 | %+0.55 | %-5.71 | — | — |
| MOVEUSDT | OKX PERP | radar / radar #0 | 01.11.2026 03:17 | 0.006339 | %+0.46 | — | — | — |
| WETUSDT | OKX PERP | radar / radar #0 | 01.11.2026 03:17 | 0.059405 | %-2.38 | — | — | — |
| MOVEUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 03:27 | 0.0063625 | %+0.20 | — | — | — |
| FILUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 03:32 | 0.877 | %+0.15 | — | — | — |
| TRXUSDT | OKX PERP | radar / radar #0 | 01.11.2026 03:37 | 0.30707 | %+0.67 | — | — | — |
| TRUMPUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 03:47 | 1.5795 | %+0.35 | — | — | — |
| ATHUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 03:47 | 0.0050585 | %-0.64 | — | — | — |
| SSVUSDT | OKX PERP | radar / radar #0 | 01.11.2026 03:52 | 2.269 | %-0.71 | — | — | — |
| INJUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 04:19 | 7.2945 | %-0.53 | — | — | — |
| NEARUSDT | OKX PERP | radar / radar #0 | 01.11.2026 04:34 | 4.4705 | %-1.04 | — | — | — |
| TRXUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 04:34 | 0.30805 | %+0.02 | — | — | — |
| BETHUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 04:39 | 2268.45 | %-0.19 | — | — | — |
| TRXUSDT | OKX PERP | triggered / retest #1 | 01.11.2026 04:49 | 0.309235 | %+0.09 | — | — | — |
| ETHUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 04:49 | 2268.405 | %+0.01 | — | — | — |
| ARXUSDT | OKX PERP | radar / radar #0 | 01.11.2026 04:49 | 0.21785 | %-1.31 | — | — | — |
| FLRUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 04:54 | 0.0060475 | %-0.01 | — | — | — |
| CVCUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 05:24 | 0.02435 | %-0.74 | — | — | — |
| CVCUSDT | MEXC PERP | radar / radar #0 | 01.11.2026 05:24 | 0.024305 | %-0.27 | — | — | — |
| AAVEUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 05:39 | 136.305 | %+1.57 | — | — | — |
| AAVEUSDT | OKX PERP | radar / radar #0 | 01.11.2026 05:39 | 136.235 | %+1.59 | — | — | — |
| BTWUSDT | OKX PERP | radar / radar #0 | 01.11.2026 05:39 | 1.1316 | %-1.44 | — | — | — |
| AAVEUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 06:01 | 136.87 | %+0.17 | — | — | — |
| PONSUSDT | OKX PERP | radar / radar #0 | 01.11.2026 06:01 | 0.2358 | %+1.99 | — | — | — |
| RLSUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 06:01 | 0.0023935 | %+0.90 | — | — | — |
| PENDLEUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 06:01 | 1.883 | %+0.48 | — | — | — |
| AAVEUSDT | MEXC PERP | radar / radar #0 | 01.11.2026 06:06 | 137.51 | %-0.52 | — | — | — |
| BRETTUSDT | OKX PERP | radar / radar #0 | 01.11.2026 06:26 | 0.004431 | %-0.54 | — | — | — |
| PONSUSDT | MEXC PERP | radar / radar #0 | 01.11.2026 06:31 | 0.24165 | %-1.14 | — | — | — |
| PONSUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 06:31 | 0.2411 | %-1.04 | — | — | — |
| PONSUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 06:31 | 0.24115 | %-1.00 | — | — | — |
| BANKUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 06:46 | 0.026225 | %+0.90 | — | — | — |
| AEVOUSDT | OKX PERP | radar / radar #0 | 01.11.2026 06:46 | 0.020455 | %+0.02 | — | — | — |
| JCTUSDT | MEXC PERP | radar / radar #0 | 01.11.2026 07:01 | 0.0047815 | %+12.79 | — | — | — |
| GUNUSDT | MEXC PERP | radar / radar #0 | 01.11.2026 07:01 | 0.002216 | %-2.98 | — | — | — |
| XPLUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 07:01 | 0.083475 | %-14.61 | — | — | — |
| RLSUSDT | MEXC SPOT | triggered / retest #1 | 01.11.2026 07:11 | 0.0024195 | %-1.51 | — | — | — |
| RAYUSDT | MEXC PERP | radar / radar #0 | 01.11.2026 07:31 | 1.63675 | %-0.15 | — | — | — |
| CHIPUSDT | OKX PERP | radar / radar #0 | 01.11.2026 07:49 | 0.042935 | — | — | — | — |
| RUNEUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 07:49 | 0.63295 | — | — | — | — |
| AKEUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 08:04 | 0.00984665 | — | — | — | — |
| YFIUSDT | OKX PERP | radar / radar #0 | 01.11.2026 08:09 | 1969.5 | — | — | — | — |
| YFIUSDT | OKX SPOT | radar / radar #0 | 01.11.2026 08:09 | 1970 | — | — | — | — |
| ZBCNUSDT | MEXC SPOT | radar / radar #0 | 01.11.2026 08:09 | 0.00199925 | — | — | — | — |
| GTCUSDT | MEXC PERP | radar / radar #0 | 01.11.2026 08:34 | 0.23107 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 138, "attempted": 2, "observed_ms": 1793511883943, "unique_reads": 6}, "summary": {"radar": {"market_event_references": 306, "unique_symbol_labels": 185, "note": "Markets, routes and repeated entries of one symbol are correlated; never summed as independent wins. Early radar is not entry.", "groups": {"OKX:SPOT:radar": {"event_references": 101, "first_per_symbol": 98, "hours": {"1": {"known_first_symbols": 97, "median_reference_return_pct": -0.09669843901092268}, "4": {"known_first_symbols": 68, "median_reference_return_pct": -0.20450506018261372}, "12": {"known_first_symbols": 66, "median_reference_return_pct": -0.3669000579589021}, "24": {"known_first_symbols": 29, "median_reference_return_pct": -0.47058823529412264}}}, "MEXC:SPOT:radar": {"event_references": 68, "first_per_symbol": 65, "hours": {"1": {"known_first_symbols": 62, "median_reference_return_pct": -0.02872267210332624}, "4": {"known_first_symbols": 34, "median_reference_return_pct": 0.10253350317166454}, "12": {"known_first_symbols": 33, "median_reference_return_pct": 0.07302468234264836}, "24": {"known_first_symbols": 21, "median_reference_return_pct": -0.649167372283388}}}, "MEXC:PERP:radar": {"event_references": 64, "first_per_symbol": 62, "hours": {"1": {"known_first_symbols": 62, "median_reference_return_pct": -0.21592034368240753}, "4": {"known_first_symbols": 39, "median_reference_return_pct": 0.3064351378958108}, "12": {"known_first_symbols": 39, "median_reference_return_pct": -0.9768695261621385}, "24": {"known_first_symbols": 23, "median_reference_return_pct": -0.3499840916321828}}}, "OKX:PERP:radar": {"event_references": 73, "first_per_symbol": 68, "hours": {"1": {"known_first_symbols": 65, "median_reference_return_pct": -0.23628248884222103}, "4": {"known_first_symbols": 43, "median_reference_return_pct": 0.026253609871362826}, "12": {"known_first_symbols": 42, "median_reference_return_pct": 0.0734419077123516}, "24": {"known_first_symbols": 13, "median_reference_return_pct": -0.2780352177942591}}}}}, "triggered": {"market_event_references": 7, "unique_symbol_labels": 7, "note": "Markets, routes and repeated entries of one symbol are correlated; never summed as independent wins. Early radar is not entry.", "groups": {"MEXC:SPOT:retest": {"event_references": 3, "first_per_symbol": 3, "hours": {"1": {"known_first_symbols": 3, "median_reference_return_pct": -0.06010131364299065}, "4": {"known_first_symbols": 2, "median_reference_return_pct": 0.4901975122152735}, "12": {"known_first_symbols": 1, "median_reference_return_pct": -1.4506453372114092}, "24": {"known_first_symbols": 1, "median_reference_return_pct": -3.09398291219779}}}, "MEXC:PERP:retest": {"event_references": 1, "first_per_symbol": 1, "hours": {"1": {"known_first_symbols": 1, "median_reference_return_pct": -1.022402646218623}, "4": {"known_first_symbols": 1, "median_reference_return_pct": -0.3758833258156735}, "12": {"known_first_symbols": 1, "median_reference_return_pct": 5.5781085551044995}, "24": {"known_first_symbols": 1, "median_reference_return_pct": -7.262065854758681}}}, "OKX:SPOT:retest": {"event_references": 2, "first_per_symbol": 2, "hours": {"1": {"known_first_symbols": 2, "median_reference_return_pct": 0.07610322644732159}, "4": {"known_first_symbols": 2, "median_reference_return_pct": -3.2889684951217744}, "12": {"known_first_symbols": 1, "median_reference_return_pct": 0.7625558769392526}, "24": {"known_first_symbols": 1, "median_reference_return_pct": -0.8677359978963906}}}, "OKX:PERP:retest": {"event_references": 1, "first_per_symbol": 1, "hours": {"1": {"known_first_symbols": 1, "median_reference_return_pct": 0.08892913156659521}, "4": {"known_first_symbols": 0, "median_reference_return_pct": null}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}}}}}
