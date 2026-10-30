# Coin Tarama5 — V3

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → ayrı geri test giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 30.10.2026 15:00 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 197, "p95_minutes": 5.000016666666666, "longest_minutes": 6.080866666666667, "over_10_minutes": 0}, "within_session": {"intervals": 188, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 9, "p95_minutes": 6.080866666666667, "longest_minutes": 6.080866666666667, "over_10_minutes": 0}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| FOGOUSDT | OKX PERP | GERİ TEST — GİRİŞ TEYİDİ | 30.10.2026 05:20 | 0.0028225 | 0.002743 | 0.0027394611 |
| BILLUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 09:52 | 0.005523 | 0.00563 | 0.0053492184 |
| JASMYUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 10:17 | 0.003736 | 0.003811 | 0.0035827359 |
| ALPINEUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 11:43 | 0.35245 | 0.3791 | 0.28142156 |
| NOSUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 11:58 | 0.408265 | 0.4153 | 0.39940556 |
| KITEUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 12:33 | 0.111185 | 0.10656 | 0.10356642 |
| NIGHTUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 12:48 | 0.038865 | 0.03865 | 0.037668829 |
| WOOUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 12:53 | 0.010485 | 0.01024 | 0.010059366 |
| LDOUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 12:58 | 0.33495 | 0.33 | 0.32427691 |
| POLUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 13:49 | 0.091595 | 0.0911 | 0.088629238 |
| MEYUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 13:49 | 0.045085 | 0.04586 | 0.044776912 |
| LTCUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 13:59 | 55.105 | 55.77 | 55.051991 |
| SSVUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 14:19 | 2.3675 | 2.36 | 2.292648 |
| KOUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 14:39 | 94.935 | 95 | 94.456812 |
| NILUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 14:49 | 0.078155 | 0.07723 | 0.074744433 |
| TAGUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 14:54 | 0.00074515 | 0.0007319 | 0.00071367955 |
| TLMUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 14:54 | 0.0012805 | 0.0012658 | 0.0012191948 |

## Kapsam ve eleme

{"observed_ms": 1793361600820, "new_radars": [], "liquid_tickers": 1550, "candles_evaluated": 133, "errors": {"OKX:SPOT": [], "OKX:PERP": ["GIGADEVUSDT: Missing/stale closed history"], "MEXC:SPOT": [], "MEXC:PERP": ["SKRUSDT: MEXC PERP public connection/response error"]}, "failed_groups": []}

OKX:SPOT: {"active_catalog": 372, "valid_liquid_tickers": 243, "observed_ms": 1793361578926, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 3, "funnel": {"candles_evaluated": 32, "volume_not_accelerating": 28, "close_not_strong": 31, "price_structure_not_ready": 29}, "calls": 21, "errors": []}

OKX:PERP: {"active_catalog": 514, "valid_liquid_tickers": 465, "observed_ms": 1793361578937, "selected_for_candles": 35, "candles_evaluated": 34, "fresh_candidate_quotes": 5, "funnel": {"candles_evaluated": 34, "volume_not_accelerating": 30, "close_not_strong": 29, "price_structure_not_ready": 29}, "calls": 28, "errors": ["GIGADEVUSDT: Missing/stale closed history"]}

MEXC:SPOT: {"active_catalog": 1247, "valid_liquid_tickers": 298, "observed_ms": 1793361579261, "selected_for_candles": 34, "candles_evaluated": 34, "fresh_candidate_quotes": 5, "funnel": {"candles_evaluated": 34, "volume_not_accelerating": 31, "close_not_strong": 26, "price_structure_not_ready": 28}, "calls": 28, "errors": []}

MEXC:PERP: {"active_catalog": 569, "valid_liquid_tickers": 544, "observed_ms": 1793361579433, "selected_for_candles": 34, "candles_evaluated": 33, "fresh_candidate_quotes": 4, "funnel": {"candles_evaluated": 33, "volume_not_accelerating": 26, "close_not_strong": 24, "price_structure_not_ready": 22}, "calls": 30, "errors": ["SKRUSDT: MEXC PERP public connection/response error"]}

Ayrıntılı evren/ret nedenleri ve seçilen kimlikler state içinde saklanır. Rolling24s hacim farkı yalnız sıralama vekilidir,5dk alım hacmi değildir. Hacim sinyali yalnız kapalı15dk gerçek quote hacmiyle ölçülür.4s trend/OI erken radarı engellemez.3yeni radar/döngü,6radar/saat ve20aktif izleme sınırı vardır; kota dışı fırsatlar kaçabilir.

## İlk gerçek gözlem ölçümleri

Radar ve giriş ayrı referanslardır, bağımsız iki başarı gibi toplanmaz. Aynı sembolün ilk evre referansı korunur; borsalar/pazarlar arası fiyatlar birleştirilmez. Eski V2 kayıtları değişmeyen arşiv commitinde korunur.

| Coin | Pazar | Evre | Gözlem TR | Referans | 1s | 4s | 12s | 24s |
|---|---|---|---|---:|---|---|---|---|
| DODOUSDT | MEXC PERP | radar | 29.10.2026 22:28 | 0.025465 | %-1.98 | %-2.69 | %-7.56 | — |
| AVNTUSDT | MEXC PERP | radar | 29.10.2026 22:28 | 0.10225 | %-2.20 | %-7.58 | %-11.10 | — |
| CENTUSDT | MEXC SPOT | radar | 29.10.2026 22:28 | 0.0016625 | %-6.23 | %-7.07 | %-6.41 | — |
| DYDXUSDT | MEXC SPOT | radar | 29.10.2026 22:48 | 0.11404 | %-3.91 | %-7.55 | %-9.01 | — |
| POLYXUSDT | MEXC PERP | radar | 29.10.2026 22:48 | 0.03369 | %-4.16 | %-5.16 | %-5.82 | — |
| PARTIUSDT | MEXC PERP | radar | 29.10.2026 22:48 | 0.06075 | %-5.25 | %+1.86 | %-15.31 | — |
| XSNXXUSDT | OKX SPOT | radar | 29.10.2026 23:33 | 9.8315 | %-10.07 | %-12.40 | %-12.86 | — |
| SNDKUSDT | OKX PERP | radar | 29.10.2026 23:33 | 1369.35 | %-4.93 | %-6.30 | %-6.64 | — |
| SNXXUSDT | OKX PERP | radar | 29.10.2026 23:33 | 9.8315 | %-9.84 | %-12.45 | %-12.93 | — |
| BTWUSDT | OKX PERP | radar | 29.10.2026 23:48 | 1.5202 | %+1.24 | %+1.89 | %-5.76 | — |
| XUVXYUSDT | OKX SPOT | radar | 29.10.2026 23:58 | 17.475 | %+0.54 | %+1.80 | %+2.66 | — |
| SKDDUSDT | OKX PERP | radar | 29.10.2026 23:58 | 8.345 | %+1.83 | %+6.83 | %+5.26 | — |
| JSTUSDT | MEXC PERP | radar | 30.10.2026 00:34 | 0.143265 | %-0.74 | %-1.96 | %-3.71 | — |
| OLUSDT | OKX PERP | radar | 30.10.2026 00:34 | 0.0074535 | %-1.90 | %-2.23 | %-4.73 | — |
| SUNUSDT | MEXC PERP | radar | 30.10.2026 00:43 | 0.0164935 | %+2.54 | %+1.98 | %-1.31 | — |
| JP225USDT | OKX PERP | radar | 30.10.2026 00:48 | 64388 | %-0.87 | %-2.54 | %-2.01 | — |
| RUNEUSDT | MEXC PERP | radar | 30.10.2026 00:58 | 0.63125 | %+1.50 | %+0.59 | %+4.51 | — |
| XDPUSDT | OKX SPOT | radar | 30.10.2026 01:03 | 0.018779 | %+0.10 | %-5.59 | %+0.07 | — |
| TMFUSDT | OKX PERP | radar | 30.10.2026 01:48 | 29.635 | %+0.22 | %+1.06 | %+0.79 | — |
| SOPHUSDT | OKX SPOT | radar | 30.10.2026 01:48 | 0.0014635 | %-3.25 | %-12.54 | %+16.57 | — |
| SOLVUSDT | MEXC PERP | radar | 30.10.2026 01:49 | 0.0048225 | %-0.03 | %-2.50 | %+6.44 | — |
| FIGHTUSDT | MEXC SPOT | radar | 30.10.2026 01:53 | 0.0039185 | %-1.75 | %-1.57 | %+4.22 | — |
| CAPUSDT | MEXC PERP | radar | 30.10.2026 02:04 | 0.078375 | %-2.01 | %+0.96 | %+3.09 | — |
| MEGAUSDT | MEXC PERP | radar | 30.10.2026 02:04 | 0.0453 | %+1.02 | %-0.29 | %+2.83 | — |
| BEATUSDT | MEXC SPOT | radar | 30.10.2026 03:04 | 0.10283 | %-2.55 | %-0.30 | — | — |
| SAMSUNGUSDT | OKX PERP | radar | 30.10.2026 03:14 | 167.79 | %-1.83 | %-0.46 | — | — |
| BWETUSDT | OKX PERP | radar | 30.10.2026 03:19 | 950.98 | %-0.59 | %+1.60 | — | — |
| NESUSDT | OKX SPOT | radar | 30.10.2026 03:29 | 0.11995 | %-0.71 | %+1.54 | — | — |
| CTUSDT | MEXC SPOT | radar | 30.10.2026 04:05 | 0.13465 | %-4.57 | %-3.75 | — | — |
| HAEDALUSDT | MEXC PERP | radar | 30.10.2026 04:05 | 0.02219 | %-0.05 | %+2.48 | — | — |
| APRUSDT | OKX PERP | radar | 30.10.2026 04:10 | 0.05685 | %+3.22 | %+3.50 | — | — |
| BULLAUSDT | MEXC SPOT | radar | 30.10.2026 04:20 | 0.076583 | %-5.98 | %-2.61 | — | — |
| AKEUSDT | MEXC SPOT | radar | 30.10.2026 04:20 | 0.02104715 | %-0.20 | %-8.72 | — | — |
| USOUSDT | OKX PERP | radar | 30.10.2026 04:50 | 169.85 | %-0.68 | %-0.98 | — | — |
| DOODUSDT | OKX SPOT | radar | 30.10.2026 05:05 | 0.00191 | %+6.96 | %+2.57 | — | — |
| FOGOUSDT | OKX PERP | radar | 30.10.2026 05:20 | 0.002766 | %+0.36 | %+1.01 | — | — |
| RLCUSDT | MEXC PERP | radar | 30.10.2026 05:35 | 0.50475 | %+1.20 | %-0.90 | — | — |
| PEPEUSDT | MEXC SPOT | radar | 30.10.2026 05:35 | 4.7355e-06 | %+1.43 | %+5.80 | — | — |
| ORDERUSDT | MEXC PERP | radar | 30.10.2026 05:40 | 0.035165 | %+2.20 | %-0.44 | — | — |
| STONKUSDT | MEXC SPOT | radar | 30.10.2026 05:50 | 0.134136 | %+2.48 | %+2.06 | — | — |
| EDGEUSDT | OKX SPOT | radar | 30.10.2026 06:10 | 0.33135 | %-1.13 | %+0.20 | — | — |
| STABLEUSDT | MEXC SPOT | radar | 30.10.2026 06:20 | 0.025304 | %+1.40 | %+1.83 | — | — |
| FOGOUSDT | OKX PERP | triggered | 30.10.2026 06:30 | 0.0028075 | %-0.87 | %+1.34 | — | — |
| RAYUSDT | MEXC SPOT | radar | 30.10.2026 06:35 | 1.62885 | %+1.05 | %-0.29 | — | — |
| OPGUSDT | OKX PERP | radar | 30.10.2026 06:45 | 0.11632 | %-0.78 | %+3.52 | — | — |
| EVAAUSDT | MEXC SPOT | radar | 30.10.2026 06:50 | 1.23905 | %-7.52 | %+0.34 | — | — |
| 1000RATSUSDT | MEXC PERP | radar | 30.10.2026 07:10 | 0.016335 | %+0.46 | %-0.34 | — | — |
| BOMEUSDT | OKX SPOT | radar | 30.10.2026 07:20 | 0.00061945 | %+1.12 | %+1.91 | — | — |
| ZROUSDT | OKX PERP | radar | 30.10.2026 07:35 | 1.6388 | %+0.85 | %+2.48 | — | — |
| FARTCOINUSDT | MEXC SPOT | radar | 30.10.2026 07:41 | 0.11923 | %+0.79 | %-2.31 | — | — |
| MONUSDT | MEXC SPOT | radar | 30.10.2026 07:46 | 0.019865 | %+0.78 | %-1.13 | — | — |
| PIPPINUSDT | MEXC SPOT | radar | 30.10.2026 07:51 | 0.01387 | %+0.40 | %-1.46 | — | — |
| CNPYUSDT | OKX PERP | radar | 30.10.2026 08:11 | 0.19005 | %+1.71 | %+5.81 | — | — |
| CROUSDT | MEXC PERP | radar | 30.10.2026 08:21 | 0.05152 | %+0.04 | %-0.04 | — | — |
| UAIUSDT | MEXC PERP | radar | 30.10.2026 08:41 | 0.27215 | %+1.27 | %-0.83 | — | — |
| XLMUSDT | OKX SPOT | radar | 30.10.2026 08:41 | 0.167565 | %-0.24 | %-1.48 | — | — |
| GRASSUSDT | OKX SPOT | radar | 30.10.2026 08:51 | 0.59555 | %-1.00 | %-1.92 | — | — |
| UBUSDT | OKX PERP | radar | 30.10.2026 08:51 | 0.111685 | %+1.48 | %+1.71 | — | — |
| REZUSDT | MEXC SPOT | radar | 30.10.2026 09:16 | 0.0041165 | %+1.62 | %+2.25 | — | — |
| GLMRUSDT | MEXC SPOT | radar | 30.10.2026 09:21 | 0.007847 | %-0.87 | %-0.84 | — | — |
| FARTCOINUSDT | MEXC SPOT | triggered | 30.10.2026 09:32 | 0.118985 | %-0.47 | %-1.23 | — | — |
| ATHUSDT | OKX PERP | radar | 30.10.2026 09:42 | 0.005217 | %-0.94 | %-1.57 | — | — |
| LIGHTUSDT | MEXC SPOT | radar | 30.10.2026 09:42 | 0.25345 | %-1.60 | %-2.66 | — | — |
| YFIUSDT | MEXC PERP | radar | 30.10.2026 09:52 | 1812.5 | %-0.63 | %+0.86 | — | — |
| BILLUSDT | OKX PERP | radar | 30.10.2026 09:52 | 0.0055215 | %-0.44 | %+0.21 | — | — |
| JASMYUSDT | MEXC SPOT | radar | 30.10.2026 10:17 | 0.003788 | %+1.64 | %-1.00 | — | — |
| WETUSDT | OKX SPOT | radar | 30.10.2026 10:27 | 0.052595 | %+1.23 | %+0.39 | — | — |
| ATHUSDT | OKX PERP | triggered | 30.10.2026 10:32 | 0.005272 | %-2.33 | %-1.97 | — | — |
| DEFIUSDT | MEXC SPOT | radar | 30.10.2026 10:42 | 0.00010445 | %+0.24 | %+1.58 | — | — |
| SYRUPUSDT | MEXC PERP | radar | 30.10.2026 10:52 | 0.15255 | %-0.95 | %-0.62 | — | — |
| AZTECUSDT | MEXC SPOT | radar | 30.10.2026 10:57 | 0.014995 | %-0.70 | — | — | — |
| LSKUSDT | OKX SPOT | radar | 30.10.2026 11:17 | 0.191055 | %+1.02 | — | — | — |
| GRTUSDT | OKX SPOT | radar | 30.10.2026 11:28 | 0.01957 | %+0.56 | — | — | — |
| ALPINEUSDT | MEXC PERP | radar | 30.10.2026 11:43 | 0.34645 | %+6.48 | — | — | — |
| DUSKUSDT | MEXC SPOT | radar | 30.10.2026 11:43 | 0.09282 | %-2.61 | — | — | — |
| BLURUSDT | MEXC SPOT | radar | 30.10.2026 11:53 | 0.0081 | %+5.06 | — | — | — |
| NOSUSDT | MEXC SPOT | radar | 30.10.2026 11:58 | 0.417135 | %-1.18 | — | — | — |
| NOMUSDT | MEXC PERP | radar | 30.10.2026 12:18 | 0.0016195 | %-2.62 | — | — | — |
| KITEUSDT | OKX PERP | radar | 30.10.2026 12:33 | 0.10768 | %+3.08 | — | — | — |
| NIGHTUSDT | MEXC SPOT | radar | 30.10.2026 12:48 | 0.03912 | %-0.31 | — | — | — |
| WOOUSDT | OKX PERP | radar | 30.10.2026 12:53 | 0.01034 | %+0.58 | — | — | — |
| LDOUSDT | OKX SPOT | radar | 30.10.2026 12:58 | 0.3311 | %+0.91 | — | — | — |
| BTWUSDT | MEXC SPOT | triggered | 30.10.2026 13:49 | 1.52821 | %-16.24 | — | — | — |
| POLUSDT | OKX SPOT | radar | 30.10.2026 13:49 | 0.091555 | %+0.39 | — | — | — |
| MEYUSDT | MEXC SPOT | radar | 30.10.2026 13:49 | 0.045695 | %-1.26 | — | — | — |
| LPTUSDT | MEXC PERP | radar | 30.10.2026 13:54 | 1.4355 | %-1.22 | — | — | — |
| LTCUSDT | MEXC PERP | radar | 30.10.2026 13:59 | 55.73 | %-1.17 | — | — | — |
| SSVUSDT | OKX SPOT | radar | 30.10.2026 14:19 | 2.3575 | — | — | — | — |
| KOUSDT | OKX PERP | radar | 30.10.2026 14:39 | 94.935 | — | — | — | — |
| NILUSDT | MEXC PERP | radar | 30.10.2026 14:49 | 0.07829 | — | — | — | — |
| TAGUSDT | MEXC PERP | radar | 30.10.2026 14:54 | 0.00074635 | — | — | — | — |
| TLMUSDT | MEXC SPOT | radar | 30.10.2026 14:54 | 0.00128275 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 3, "attempted": 2, "observed_ms": 1793361609572, "unique_reads": 4}, "summary": {"radar": {"unique_symbol_labels": 88, "hours": {"1": {"known": 83, "median_pct": -0.20121489132732817}, "4": {"known": 67, "median_pct": -0.33670033670035737}, "12": {"known": 24, "median_pct": -2.8574701027968716}, "24": {"known": 0, "median_pct": null}}}, "triggered": {"unique_symbol_labels": 4, "hours": {"1": {"known": 4, "median_pct": -1.6028714680085543}, "4": {"known": 3, "median_pct": -1.2312476362566827}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}}}
