# Coin Tarama5 — V4

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → geri test veya yukarıda yeni taban giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 31.10.2026 16:54 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 283, "p95_minutes": 5.61935, "longest_minutes": 55.56921666666667, "over_10_minutes": 1}, "within_session": {"intervals": 268, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 15, "p95_minutes": 55.56921666666667, "longest_minutes": 55.56921666666667, "over_10_minutes": 1}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| UPUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 11:00 | 0.12975 | 0.1203 | 0.11852985 |
| BATUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 12:42 | 0.13337 | 0.12942 | 0.12840221 |
| APTUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 12:47 | 0.6375 | 0.6359 | 0.63005935 |
| THETAUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 13:44 | 0.1616 | 0.1602 | 0.15904012 |
| OFCUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 14:05 | 0.006294 | 0.006232 | 0.0061540355 |
| CSPRUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 14:35 | 0.00218 | 0.002176 | 0.0021368612 |
| METUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 14:50 | 0.28495 | 0.2817 | 0.27834797 |
| NEARUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 15:37 | 4.4105 | 4.347 | 4.3043207 |
| NEARUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 15:37 | 4.4105 | 4.348 | 4.3043087 |
| DATAUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 15:47 | 0.13065 | 0.1307 | 0.12890565 |
| EGLDUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 15:52 | 3.4305 | 3.415 | 3.3250374 |
| LSKUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 16:42 | 0.306385 | 0.29438 | 0.25749655 |
| LSKUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 16:42 | 0.305615 | 0.29498 | 0.26049226 |
| CPUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 16:49 | 0.008066 | 0.008091 | 0.0079971263 |
| 4USDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 16:49 | 0.01126 | 0.01127 | 0.011138443 |
| XDPUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 16:54 | 0.017665 | 0.01764 | 0.017334764 |
| XDPUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 16:54 | 0.0176725 | 0.01765 | 0.017364016 |
| GLMUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 31.10.2026 16:54 | 0.11671 | 0.11671 | 0.11354207 |

## Kapsam ve eleme

{"observed_ms": 1793454879424, "new_radars": ["OKX:PERP:XDPUSDT", "OKX:SPOT:XDPUSDT", "OKX:PERP:GLMUSDT"], "liquid_tickers": 1242, "candles_evaluated": 134, "errors": {"MEXC:SPOT": [], "OKX:SPOT": [], "OKX:PERP": [], "MEXC:PERP": []}, "failed_groups": []}

OKX:PERP: {"active_catalog": 288, "instrument_categories": {"1": 304, "3": 219, "4": 9}, "valid_liquid_tickers": 287, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793454867623, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 6, "funnel": {"candles_evaluated": 32, "volume_not_accelerating": 22, "close_not_strong": 15, "price_structure_not_ready": 19}, "calls": 35, "errors": []}

OKX:SPOT: {"active_catalog": 294, "instrument_categories": {"1": 1013, "4": 4, "3": 194}, "valid_liquid_tickers": 198, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793454867634, "selected_for_candles": 38, "candles_evaluated": 38, "fresh_candidate_quotes": 12, "funnel": {"candles_evaluated": 38, "volume_not_accelerating": 24, "close_not_strong": 18, "price_structure_not_ready": 23, "flat_price_or_volume": 1}, "calls": 29, "errors": []}

MEXC:PERP: {"active_catalog": 569, "instrument_categories": {}, "valid_liquid_tickers": 546, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793454867807, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 7, "funnel": {"candles_evaluated": 32, "volume_not_accelerating": 22, "close_not_strong": 9, "price_structure_not_ready": 18}, "calls": 36, "errors": []}

MEXC:SPOT: {"active_catalog": 1241, "instrument_categories": {}, "valid_liquid_tickers": 211, "active_quotes_retained_outside_discovery": 0, "observed_ms": 1793454867547, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 3, "funnel": {"candles_evaluated": 32, "volume_not_accelerating": 27, "close_not_strong": 12, "price_structure_not_ready": 20}, "calls": 26, "errors": []}

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
| BRUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 17:08 | 0.4864 | %-1.15 | %-3.06 | %-1.83 | — |
| HUMAUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:08 | 0.02887 | %+0.59 | %-2.67 | %-2.15 | — |
| ARKMUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:08 | 0.11046 | %+1.40 | %+0.31 | %+3.65 | — |
| PROVEUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:13 | 0.1955 | %+2.35 | %+2.92 | %+5.17 | — |
| BEAMXUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 17:13 | 0.0052475 | %-9.19 | %-9.98 | %-11.75 | — |
| LITUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 17:13 | 2.8186 | %+3.23 | %-2.88 | %-1.85 | — |
| WLDUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 18:19 | 0.4141 | %+0.07 | %-2.75 | %-2.97 | — |
| ZETAUSDT | OKX PERP | radar / radar #0 | 30.10.2026 18:19 | 0.03757 | %-1.57 | %-3.11 | %+0.45 | — |
| NEARUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 18:19 | 4.42085 | %-1.59 | %-3.39 | %-2.32 | — |
| TUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 18:24 | 0.0045505 | %-0.41 | %-2.54 | %-0.08 | — |
| BREVUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 18:24 | 0.08922 | %-0.39 | %-0.81 | %+0.18 | — |
| SAHARAUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 18:24 | 0.0075545 | %-0.67 | %-1.09 | %+0.38 | — |
| BREVUSDT | OKX PERP | radar / radar #0 | 30.10.2026 18:24 | 0.08912 | %-0.18 | %-0.58 | %+0.26 | — |
| BREVUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 18:29 | 0.08906 | %-0.36 | %-1.39 | %-0.98 | — |
| GRTUSDT | OKX PERP | radar / radar #0 | 30.10.2026 19:24 | 0.021 | %-0.90 | %-3.95 | %-2.95 | — |
| PLAYUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 19:24 | 0.013925 | %+3.48 | %+6.14 | %+11.67 | — |
| GRASSUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 19:29 | 0.6026 | %+0.38 | %-2.42 | %-3.50 | — |
| GRASSUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 19:29 | 0.60245 | %+0.44 | %-2.53 | %-3.36 | — |
| ZROUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 19:29 | 1.76525 | %-0.68 | %-4.32 | %-3.71 | — |
| BIANRENSHENGUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 19:34 | 0.53025 | %+0.25 | %-0.27 | %-1.90 | — |
| CHIPUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 19:39 | 0.044335 | %-1.70 | %-0.89 | %-0.62 | — |
| SENTUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 20:24 | 0.019105 | %+1.44 | %-0.03 | %-2.85 | — |
| VIRTUALUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 20:24 | 0.5954 | %-0.82 | %+0.67 | %-1.01 | — |
| VIRTUALUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 20:24 | 0.595 | %-0.77 | %+0.76 | %-1.06 | — |
| EDENUSDT | OKX PERP | radar / radar #0 | 30.10.2026 20:29 | 0.05524 | %-2.44 | %-0.29 | %+1.38 | — |
| MMTUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 20:29 | 0.1294 | %-1.16 | %+0.77 | %-0.62 | — |
| SENTUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 20:34 | 0.01929 | %-0.31 | %-0.73 | %-3.63 | — |
| AINUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 20:34 | 0.173475 | %+9.25 | %+1.70 | %+50.19 | — |
| AIUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 20:39 | 0.016915 | %-0.98 | %+1.09 | %+1.33 | — |
| SENTUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 20:49 | 0.019585 | %-2.02 | %-2.43 | %-4.88 | — |
| SENTUSDT | OKX PERP | radar / radar #0 | 30.10.2026 20:49 | 0.01954 | %-2.00 | %-2.51 | %-5.07 | — |
| AINUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 21:04 | 0.183775 | %-0.48 | %-1.12 | %+53.51 | — |
| BULLAUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 21:29 | 0.073804 | %+0.78 | %+3.91 | %+15.64 | — |
| PARTIUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 21:29 | 0.053295 | %-6.54 | %-6.28 | %-8.47 | — |
| ILVUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 21:34 | 2.985 | %-2.51 | %-0.23 | %+1.47 | — |
| GWEIUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 21:34 | 0.02216 | %+6.14 | %+1.81 | %-1.22 | — |
| SIRENUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 22:00 | 0.02309 | %-1.21 | %-1.56 | %+5.28 | — |
| XPLUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 22:00 | 0.078245 | %+3.52 | %+3.10 | %+2.87 | — |
| ATOMUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 22:32 | 1.5085 | %+1.03 | %+2.75 | %+0.36 | — |
| SPXUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 22:32 | 0.358 | %+0.34 | %+1.12 | %-1.40 | — |
| UAIUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 22:36 | 0.2713 | %-0.70 | %-0.15 | %+1.14 | — |
| CVXUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 22:47 | 1.992 | %-0.10 | %+0.40 | %+0.15 | — |
| NIULAIUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 23:02 | 0.054305 | %-0.67 | %+1.00 | %-2.42 | — |
| EIGENUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 23:02 | 0.1904 | %-0.26 | %+0.11 | %-2.10 | — |
| EIGENUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 23:02 | 0.19055 | %-0.24 | %+0.13 | %-2.23 | — |
| EIGENUSDT | OKX PERP | radar / radar #0 | 30.10.2026 23:02 | 0.19045 | %-0.24 | %+0.03 | %-2.34 | — |
| ATOMUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 23:32 | 1.5215 | %+1.68 | %+1.94 | %-0.89 | — |
| CAPUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 23:41 | 0.08354 | %+0.19 | %-0.02 | %+5.69 | — |
| WOOUSDT | OKX SPOT | radar / radar #0 | 30.10.2026 23:47 | 0.01104 | %+2.17 | %+5.16 | %+3.71 | — |
| WOOUSDT | OKX PERP | radar / radar #0 | 30.10.2026 23:47 | 0.011025 | %+1.86 | %+5.12 | %+3.58 | — |
| RENDERUSDT | MEXC SPOT | radar / radar #0 | 30.10.2026 23:52 | 1.5445 | %+1.39 | %+4.95 | %+1.39 | — |
| HOLOUSDT | MEXC PERP | radar / radar #0 | 30.10.2026 23:51 | 0.058635 | %+0.35 | %+0.54 | %-1.65 | — |
| NEOUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 00:03 | 1.9965 | %+0.23 | %+1.38 | %-0.53 | — |
| WIFUSDT | OKX PERP | radar / radar #0 | 31.10.2026 00:03 | 0.17605 | %+0.99 | %+0.48 | %-0.03 | — |
| RENDERUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:13 | 1.5535 | %+1.38 | %+4.41 | %+1.13 | — |
| WIFUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:18 | 0.17715 | %-0.08 | %-0.37 | %-0.76 | — |
| WIFUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 00:18 | 0.17705 | %-0.20 | %-0.25 | %-0.82 | — |
| WIFUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 00:18 | 0.17715 | %-0.08 | %-0.25 | %-0.65 | — |
| RENDERUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 00:38 | 1.5715 | %+0.41 | %+2.51 | %-0.22 | — |
| NFTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:43 | 2.345e-07 | %+0.17 | %-0.21 | %-0.04 | — |
| BIOUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:48 | 0.021605 | %+1.83 | %+1.37 | %-1.00 | — |
| BIOUSDT | OKX PERP | radar / radar #0 | 31.10.2026 00:48 | 0.02158 | %+1.81 | %+1.20 | %-1.07 | — |
| KMNOUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 00:53 | 0.033065 | %+0.35 | %-0.71 | %-4.52 | — |
| SPELLUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 00:53 | 7.825e-05 | %+1.85 | %+4.66 | %-0.58 | — |
| CETUSUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 01:08 | 0.021015 | %+1.64 | %-0.93 | %-0.26 | — |
| POLUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 01:18 | 0.09547 | %-1.59 | %-1.61 | %-3.56 | — |
| POLUSDT | OKX PERP | radar / radar #0 | 31.10.2026 01:28 | 0.095815 | %-1.72 | %-2.40 | %-4.23 | — |
| IOUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 01:43 | 0.13712 | %+0.93 | %+0.34 | %-1.22 | — |
| POLUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 01:43 | 0.095645 | %-0.36 | %-2.03 | %-4.03 | — |
| SANDUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 01:54 | 0.046685 | %+0.67 | %+0.61 | %-0.35 | — |
| COMPUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 01:54 | 20.43 | %+0.44 | %-0.20 | %-0.93 | — |
| SANDUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 01:54 | 0.046725 | %+0.57 | %+0.33 | %-0.46 | — |
| ARUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 01:54 | 3.2145 | %+0.76 | %-0.67 | %-1.54 | — |
| IOUSDT | MEXC SPOT | triggered / retest #1 | 31.10.2026 02:04 | 0.137525 | %+0.37 | %-0.11 | %-1.45 | — |
| QUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 02:09 | 0.048233 | %+3.27 | %-26.38 | — | — |
| 1INCHUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 02:19 | 0.08015 | %+0.46 | %-0.22 | — | — |
| RECALLUSDT | OKX PERP | radar / radar #0 | 31.10.2026 02:44 | 0.032955 | %-2.26 | %+4.51 | — | — |
| ARUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 02:54 | 3.238 | %-0.31 | %-2.07 | — | — |
| COREUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 02:54 | 0.015525 | %-0.16 | %-1.00 | — | — |
| CHZUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 02:54 | 0.012545 | %-0.20 | %-0.92 | — | — |
| SPKUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 03:14 | 0.018925 | %+2.30 | %+5.79 | — | — |
| SPKUSDT | OKX PERP | radar / radar #0 | 31.10.2026 03:14 | 0.01893 | %+2.17 | %+5.76 | — | — |
| ROBOUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 03:19 | 0.0053115 | %-1.16 | %-1.52 | — | — |
| STXUSDT | OKX PERP | radar / radar #0 | 31.10.2026 03:46 | 0.2923 | %+1.51 | %+1.85 | — | — |
| STXUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 03:46 | 0.29235 | %+1.49 | %+1.93 | — | — |
| IMXUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 03:56 | 0.12765 | %-0.82 | %-4.11 | — | — |
| DGAIUSDT | OKX PERP | radar / radar #0 | 31.10.2026 03:56 | 0.78125 | %-0.03 | %-0.61 | — | — |
| REUSDT | OKX PERP | radar / radar #0 | 31.10.2026 03:56 | 0.38363 | %-0.85 | %-1.35 | — | — |
| IMXUSDT | OKX PERP | radar / radar #0 | 31.10.2026 04:01 | 0.127655 | %-1.37 | %-4.09 | — | — |
| IMXUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 04:06 | 0.1276 | %-1.72 | %-3.84 | — | — |
| ELSAUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 04:16 | 0.068965 | %-0.21 | %+2.36 | — | — |
| RUNEUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 04:21 | 0.6621 | %+0.42 | %+1.60 | — | — |
| WCTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 04:51 | 0.035885 | %-0.43 | %-3.36 | — | — |
| RUNEUSDT | MEXC PERP | triggered / retest #1 | 31.10.2026 05:01 | 0.6651 | %-1.02 | %-0.38 | — | — |
| METISUSDT | OKX PERP | radar / radar #0 | 31.10.2026 05:01 | 2.9175 | %-1.49 | %-1.97 | — | — |
| PROSUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 05:01 | 0.56275 | %-0.03 | %-2.00 | — | — |
| WOOUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 05:06 | 0.011615 | %-3.31 | %-3.92 | — | — |
| TRXUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 05:16 | 0.34148 | %-2.33 | %-3.09 | — | — |
| CELOUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 05:31 | 0.074955 | %+0.26 | %-0.82 | — | — |
| CELOUSDT | OKX PERP | radar / radar #0 | 31.10.2026 05:31 | 0.07457 | %+0.13 | %-0.75 | — | — |
| NESUSDT | OKX PERP | radar / radar #0 | 31.10.2026 05:52 | 0.1227 | %+1.79 | %+0.90 | — | — |
| RLSUSDT | OKX PERP | radar / radar #0 | 31.10.2026 06:02 | 0.002202 | %+1.82 | %+3.22 | — | — |
| SPKUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 06:02 | 0.02006 | %+0.25 | %-1.20 | — | — |
| BULLAUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 06:07 | 0.079895 | %-0.98 | %+5.78 | — | — |
| FLOKIUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 06:17 | 2.408e-05 | %-0.04 | %-1.66 | — | — |
| FLOKIUSDT | OKX PERP | radar / radar #0 | 31.10.2026 06:17 | 2.404e-05 | %-0.04 | %-1.71 | — | — |
| AGLDUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 06:32 | 0.18825 | %+0.72 | %+0.88 | — | — |
| AGLDUSDT | OKX PERP | radar / radar #0 | 31.10.2026 06:32 | 0.18825 | %+0.66 | %+0.82 | — | — |
| BLESSUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 06:52 | 0.010195 | %+3.82 | %-2.41 | — | — |
| MASKUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 07:02 | 0.38735 | %-0.76 | %-0.76 | — | — |
| ENJUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 07:02 | 0.02417 | %-0.62 | %-0.99 | — | — |
| NMRUSDT | OKX PERP | radar / radar #0 | 31.10.2026 07:12 | 9.434 | %-0.07 | %+0.11 | — | — |
| LAYERUSDT | OKX PERP | radar / radar #0 | 31.10.2026 07:17 | 0.06093 | %-0.64 | %-0.95 | — | — |
| BULLAUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 07:34 | 0.0819365 | %+4.93 | %-8.82 | — | — |
| NMRUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 07:39 | 9.4595 | %-0.87 | %+0.07 | — | — |
| LYNUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 08:09 | 0.01439 | %-2.71 | — | — | — |
| GTCUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 08:09 | 0.23017 | %-2.12 | — | — | — |
| SOMIUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 08:14 | 0.19855 | %-1.18 | — | — | — |
| AGLDUSDT | OKX SPOT | triggered / retest #1 | 31.10.2026 08:19 | 0.19015 | %-0.39 | %-0.87 | — | — |
| RESOLVUSDT | OKX PERP | radar / radar #0 | 31.10.2026 08:19 | 0.015505 | %+0.03 | — | — | — |
| ZORAUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 08:19 | 0.006236 | %-0.32 | — | — | — |
| RESOLVUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 08:29 | 0.015545 | %+0.16 | — | — | — |
| JELLYJELLYUSDT | OKX PERP | radar / radar #0 | 31.10.2026 08:44 | 0.043235 | %+0.57 | — | — | — |
| MAGMAUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 09:20 | 0.3914 | %+8.02 | — | — | — |
| MAGMAUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 09:20 | 0.390785 | %+7.83 | — | — | — |
| MERLUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 09:20 | 0.02919 | %-0.51 | — | — | — |
| TIAUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 09:25 | 0.47885 | %-0.24 | — | — | — |
| DOSUSDT | OKX PERP | radar / radar #0 | 31.10.2026 09:25 | 0.2137 | %-0.37 | — | — | — |
| ZROUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 09:25 | 1.71 | %-0.61 | — | — | — |
| RSRUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 09:45 | 0.001464 | %-1.09 | — | — | — |
| RSRUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 09:45 | 0.001464 | %-1.23 | — | — | — |
| RSRUSDT | OKX PERP | radar / radar #0 | 31.10.2026 09:45 | 0.0014635 | %-1.13 | — | — | — |
| RSRUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 09:45 | 0.0014685 | %-1.19 | — | — | — |
| BSBUSDT | OKX PERP | radar / radar #0 | 31.10.2026 10:25 | 0.09666 | %-1.40 | — | — | — |
| KITEUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 10:30 | 0.108585 | %-0.10 | — | — | — |
| ZAMAUSDT | OKX PERP | radar / radar #0 | 31.10.2026 10:30 | 0.06592 | %-0.68 | — | — | — |
| ZAMAUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 10:30 | 0.065895 | %-0.69 | — | — | — |
| ASTERUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 10:30 | 0.69135 | %-0.12 | — | — | — |
| ZAMAUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 10:30 | 0.065855 | %-0.31 | — | — | — |
| KITEUSDT | OKX PERP | radar / radar #0 | 31.10.2026 10:30 | 0.108495 | %-0.39 | — | — | — |
| EVAAUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 10:35 | 1.21095 | %-0.05 | — | — | — |
| UPUSDT | OKX PERP | radar / radar #0 | 31.10.2026 11:00 | 0.11995 | %+3.13 | — | — | — |
| RLCUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 11:27 | 0.47025 | %+1.14 | — | — | — |
| APRUSDT | OKX PERP | radar / radar #0 | 31.10.2026 11:32 | 0.055895 | %-1.87 | — | — | — |
| SKYUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 11:32 | 0.06792 | %+1.00 | — | — | — |
| ZROUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 11:37 | 1.70995 | %+2.97 | — | — | — |
| HBARUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 11:42 | 0.07216 | %+0.49 | — | — | — |
| TACUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 12:02 | 0.0011755 | %-1.40 | — | — | — |
| ZROUSDT | OKX PERP | radar / radar #0 | 31.10.2026 12:02 | 1.74065 | %+0.30 | — | — | — |
| QNTUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 12:32 | 197.125 | %+0.18 | — | — | — |
| BATUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 12:42 | 0.130415 | %+0.60 | — | — | — |
| BABYUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 12:42 | 0.0121925 | %+0.55 | — | — | — |
| GRVTUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 12:47 | 0.21775 | %+0.44 | — | — | — |
| APTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 12:47 | 0.6357 | %-0.36 | — | — | — |
| GRVTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 12:52 | 0.21821 | %+0.10 | — | — | — |
| GRVTUSDT | OKX PERP | radar / radar #0 | 31.10.2026 12:57 | 0.218685 | %-0.48 | — | — | — |
| UAIUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 13:05 | 0.29585 | %-0.63 | — | — | — |
| GRTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 13:35 | 0.02051 | %+0.29 | — | — | — |
| THETAUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 13:44 | 0.16065 | %+0.47 | — | — | — |
| GPSUSDT | OKX PERP | radar / radar #0 | 31.10.2026 13:44 | 0.0077145 | %-0.42 | — | — | — |
| OLUSDT | OKX PERP | radar / radar #0 | 31.10.2026 13:49 | 0.0064965 | %+0.48 | — | — | — |
| POWRUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 13:50 | 0.05751 | %-1.06 | — | — | — |
| OLUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 13:50 | 0.006506 | %+0.52 | — | — | — |
| OFCUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 14:05 | 0.006317 | %-0.17 | — | — | — |
| CSPRUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 14:35 | 0.002232 | %-0.63 | — | — | — |
| NEOUSDT | OKX PERP | radar / radar #0 | 31.10.2026 14:44 | 1.987 | %+0.20 | — | — | — |
| BLENDUSDT | OKX PERP | radar / radar #0 | 31.10.2026 14:44 | 0.053005 | %-0.50 | — | — | — |
| AVNTUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 14:50 | 0.09456 | %-0.45 | — | — | — |
| METUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 14:50 | 0.28215 | %+0.51 | — | — | — |
| AWEUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 15:07 | 0.073605 | %+0.18 | — | — | — |
| NEARUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 15:37 | 4.407 | %-0.07 | — | — | — |
| NEARUSDT | OKX PERP | radar / radar #0 | 31.10.2026 15:37 | 4.4065 | %-0.03 | — | — | — |
| DATAUSDT | MEXC SPOT | radar / radar #0 | 31.10.2026 15:47 | 0.131 | %+0.23 | — | — | — |
| BATUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 15:47 | 0.135075 | %-1.23 | — | — | — |
| BATUSDT | OKX PERP | radar / radar #0 | 31.10.2026 15:47 | 0.13503 | %-1.14 | — | — | — |
| CROUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 15:52 | 0.051585 | — | — | — | — |
| EGLDUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 15:52 | 3.4125 | — | — | — | — |
| JCTUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 16:22 | 0.0059275 | — | — | — | — |
| LSKUSDT | MEXC PERP | radar / radar #0 | 31.10.2026 16:42 | 0.311485 | — | — | — | — |
| LSKUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 16:42 | 0.311625 | — | — | — | — |
| CPUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 16:49 | 0.0080635 | — | — | — | — |
| 4USDT | MEXC SPOT | radar / radar #0 | 31.10.2026 16:49 | 0.01133 | — | — | — | — |
| XDPUSDT | OKX PERP | radar / radar #0 | 31.10.2026 16:54 | 0.017665 | — | — | — | — |
| XDPUSDT | OKX SPOT | radar / radar #0 | 31.10.2026 16:54 | 0.0176725 | — | — | — | — |
| GLMUSDT | OKX PERP | radar / radar #0 | 31.10.2026 16:54 | 0.11671 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 62, "attempted": 2, "observed_ms": 1793454896643, "unique_reads": 4}, "summary": {"radar": {"market_event_references": 191, "unique_symbol_labels": 129, "note": "Markets, routes and repeated entries of one symbol are correlated; never summed as independent wins. Early radar is not entry.", "groups": {"OKX:SPOT:radar": {"event_references": 70, "first_per_symbol": 70, "hours": {"1": {"known_first_symbols": 66, "median_reference_return_pct": -0.07637376224070014}, "4": {"known_first_symbols": 43, "median_reference_return_pct": -0.7107213065174589}, "12": {"known_first_symbols": 29, "median_reference_return_pct": -0.618238021638351}, "24": {"known_first_symbols": 2, "median_reference_return_pct": 1.9242931534386831}}}, "MEXC:SPOT:radar": {"event_references": 36, "first_per_symbol": 35, "hours": {"1": {"known_first_symbols": 34, "median_reference_return_pct": 0.013513691509270398}, "4": {"known_first_symbols": 24, "median_reference_return_pct": -0.2442639389439505}, "12": {"known_first_symbols": 20, "median_reference_return_pct": -0.3609284662144163}, "24": {"known_first_symbols": 3, "median_reference_return_pct": 1.1368090944727571}}}, "MEXC:PERP:radar": {"event_references": 40, "first_per_symbol": 40, "hours": {"1": {"known_first_symbols": 37, "median_reference_return_pct": -0.21025157688681073}, "4": {"known_first_symbols": 28, "median_reference_return_pct": 0.7704063127147109}, "12": {"known_first_symbols": 21, "median_reference_return_pct": -0.9768695261621385}, "24": {"known_first_symbols": 2, "median_reference_return_pct": 3.500706045152202}}}, "OKX:PERP:radar": {"event_references": 45, "first_per_symbol": 45, "hours": {"1": {"known_first_symbols": 43, "median_reference_return_pct": -0.23628248884222103}, "4": {"known_first_symbols": 26, "median_reference_return_pct": -0.43656406449675833}, "12": {"known_first_symbols": 12, "median_reference_return_pct": 0.0734419077123516}, "24": {"known_first_symbols": 2, "median_reference_return_pct": 2.0319443549945193}}}}}, "triggered": {"market_event_references": 3, "unique_symbol_labels": 3, "note": "Markets, routes and repeated entries of one symbol are correlated; never summed as independent wins. Early radar is not entry.", "groups": {"MEXC:SPOT:retest": {"event_references": 1, "first_per_symbol": 1, "hours": {"1": {"known_first_symbols": 1, "median_reference_return_pct": 0.3744773677513136}, "4": {"known_first_symbols": 1, "median_reference_return_pct": -0.10543537538629799}, "12": {"known_first_symbols": 1, "median_reference_return_pct": -1.4506453372114092}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "MEXC:PERP:retest": {"event_references": 1, "first_per_symbol": 1, "hours": {"1": {"known_first_symbols": 1, "median_reference_return_pct": -1.022402646218623}, "4": {"known_first_symbols": 1, "median_reference_return_pct": -0.3758833258156735}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}, "OKX:SPOT:retest": {"event_references": 1, "first_per_symbol": 1, "hours": {"1": {"known_first_symbols": 1, "median_reference_return_pct": -0.3944254535892533}, "4": {"known_first_symbols": 1, "median_reference_return_pct": -0.8677359978963906}, "12": {"known_first_symbols": 0, "median_reference_return_pct": null}, "24": {"known_first_symbols": 0, "median_reference_return_pct": null}}}}}}}
