# Coin Tarama5 — V3

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → ayrı geri test giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 30.10.2026 09:01 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 126, "p95_minutes": 5.000016666666666, "longest_minutes": 5.812783333333333, "over_10_minutes": 0}, "within_session": {"intervals": 121, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 5, "p95_minutes": 5.812783333333333, "longest_minutes": 5.812783333333333, "over_10_minutes": 0}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| HAEDALUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 04:05 | 0.02242 | 0.02144 | 0.020507524 |
| FOGOUSDT | OKX PERP | GERİ TEST — GİRİŞ TEYİDİ | 30.10.2026 05:20 | 0.002815 | 0.002743 | 0.0027394611 |
| STABLEUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 06:20 | 0.025828 | 0.024837 | 0.024112822 |
| RAYUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 06:35 | 1.6434 | 1.5979 | 1.5328546 |
| SOPHUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 06:35 | 0.001615 | 0.001308 | 0.0011827829 |
| 1000RATSUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 07:10 | 0.016215 | 0.01648 | 0.016105144 |
| ZROUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 07:35 | 1.67285 | 1.5746 | 1.4708711 |
| FARTCOINUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 07:41 | 0.118195 | 0.11801 | 0.11376425 |
| MONUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 07:46 | 0.019735 | 0.01961 | 0.018827926 |
| CNPYUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 08:11 | 0.19025 | 0.182 | 0.17719054 |
| UAIUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 08:41 | 0.26905 | 0.2669 | 0.25733698 |
| GRASSUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 08:51 | 0.5892 | 0.5795 | 0.55896454 |
| UBUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 08:51 | 0.11144 | 0.11047 | 0.10507056 |

## Kapsam ve eleme

{"observed_ms": 1793340089311, "new_radars": [], "liquid_tickers": 1524, "candles_evaluated": 134, "errors": {"OKX:SPOT": [], "MEXC:SPOT": [], "MEXC:PERP": [], "OKX:PERP": []}, "failed_groups": []}

OKX:SPOT: {"active_catalog": 372, "valid_liquid_tickers": 241, "observed_ms": 1793340075199, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 2, "funnel": {"candles_evaluated": 32, "volume_not_accelerating": 25, "close_not_strong": 25, "price_structure_not_ready": 26}, "calls": 38, "errors": []}

OKX:PERP: {"active_catalog": 508, "valid_liquid_tickers": 456, "observed_ms": 1793340074918, "selected_for_candles": 34, "candles_evaluated": 34, "fresh_candidate_quotes": 5, "funnel": {"candles_evaluated": 34, "volume_not_accelerating": 28, "close_not_strong": 23, "price_structure_not_ready": 27}, "calls": 44, "errors": []}

MEXC:SPOT: {"active_catalog": 1247, "valid_liquid_tickers": 281, "observed_ms": 1793340074995, "selected_for_candles": 33, "candles_evaluated": 33, "fresh_candidate_quotes": 4, "funnel": {"candles_evaluated": 33, "volume_not_accelerating": 30, "close_not_strong": 23, "price_structure_not_ready": 24}, "calls": 41, "errors": []}

MEXC:PERP: {"active_catalog": 570, "valid_liquid_tickers": 546, "observed_ms": 1793340074694, "selected_for_candles": 35, "candles_evaluated": 35, "fresh_candidate_quotes": 5, "funnel": {"candles_evaluated": 35, "volume_not_accelerating": 29, "close_not_strong": 26, "price_structure_not_ready": 27, "already_extended": 2}, "calls": 44, "errors": []}

Ayrıntılı evren/ret nedenleri ve seçilen kimlikler state içinde saklanır. Rolling24s hacim farkı yalnız sıralama vekilidir,5dk alım hacmi değildir. Hacim sinyali yalnız kapalı15dk gerçek quote hacmiyle ölçülür.4s trend/OI erken radarı engellemez.3yeni radar/döngü,6radar/saat ve20aktif izleme sınırı vardır; kota dışı fırsatlar kaçabilir.

## İlk gerçek gözlem ölçümleri

Radar ve giriş ayrı referanslardır, bağımsız iki başarı gibi toplanmaz. Aynı sembolün ilk evre referansı korunur; borsalar/pazarlar arası fiyatlar birleştirilmez. Eski V2 kayıtları değişmeyen arşiv commitinde korunur.

| Coin | Pazar | Evre | Gözlem TR | Referans | 1s | 4s | 12s | 24s |
|---|---|---|---|---:|---|---|---|---|
| DODOUSDT | MEXC PERP | radar | 29.10.2026 22:28 | 0.025465 | %-1.98 | %-2.69 | — | — |
| AVNTUSDT | MEXC PERP | radar | 29.10.2026 22:28 | 0.10225 | %-2.20 | %-7.58 | — | — |
| CENTUSDT | MEXC SPOT | radar | 29.10.2026 22:28 | 0.0016625 | %-6.23 | %-7.07 | — | — |
| DYDXUSDT | MEXC SPOT | radar | 29.10.2026 22:48 | 0.11404 | %-3.91 | %-7.55 | — | — |
| POLYXUSDT | MEXC PERP | radar | 29.10.2026 22:48 | 0.03369 | %-4.16 | %-5.16 | — | — |
| PARTIUSDT | MEXC PERP | radar | 29.10.2026 22:48 | 0.06075 | %-5.25 | %+1.86 | — | — |
| XSNXXUSDT | OKX SPOT | radar | 29.10.2026 23:33 | 9.8315 | %-10.07 | %-12.40 | — | — |
| SNDKUSDT | OKX PERP | radar | 29.10.2026 23:33 | 1369.35 | %-4.93 | %-6.30 | — | — |
| SNXXUSDT | OKX PERP | radar | 29.10.2026 23:33 | 9.8315 | %-9.84 | %-12.45 | — | — |
| BTWUSDT | OKX PERP | radar | 29.10.2026 23:48 | 1.5202 | %+1.24 | %+1.89 | — | — |
| XUVXYUSDT | OKX SPOT | radar | 29.10.2026 23:58 | 17.475 | %+0.54 | %+1.80 | — | — |
| SKDDUSDT | OKX PERP | radar | 29.10.2026 23:58 | 8.345 | %+1.83 | %+6.83 | — | — |
| JSTUSDT | MEXC PERP | radar | 30.10.2026 00:34 | 0.143265 | %-0.74 | %-1.96 | — | — |
| OLUSDT | OKX PERP | radar | 30.10.2026 00:34 | 0.0074535 | %-1.90 | %-2.23 | — | — |
| SUNUSDT | MEXC PERP | radar | 30.10.2026 00:43 | 0.0164935 | %+2.54 | %+1.98 | — | — |
| JP225USDT | OKX PERP | radar | 30.10.2026 00:48 | 64388 | %-0.87 | %-2.54 | — | — |
| RUNEUSDT | MEXC PERP | radar | 30.10.2026 00:58 | 0.63125 | %+1.50 | %+0.59 | — | — |
| XDPUSDT | OKX SPOT | radar | 30.10.2026 01:03 | 0.018779 | %+0.10 | %-5.59 | — | — |
| TMFUSDT | OKX PERP | radar | 30.10.2026 01:48 | 29.635 | %+0.22 | %+1.06 | — | — |
| SOPHUSDT | OKX SPOT | radar | 30.10.2026 01:48 | 0.0014635 | %-3.25 | %-12.54 | — | — |
| SOLVUSDT | MEXC PERP | radar | 30.10.2026 01:49 | 0.0048225 | %-0.03 | %-2.50 | — | — |
| FIGHTUSDT | MEXC SPOT | radar | 30.10.2026 01:53 | 0.0039185 | %-1.75 | %-1.57 | — | — |
| CAPUSDT | MEXC PERP | radar | 30.10.2026 02:04 | 0.078375 | %-2.01 | %+0.96 | — | — |
| MEGAUSDT | MEXC PERP | radar | 30.10.2026 02:04 | 0.0453 | %+1.02 | %-0.29 | — | — |
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
| DOODUSDT | OKX SPOT | radar | 30.10.2026 05:05 | 0.00191 | %+6.96 | — | — | — |
| FOGOUSDT | OKX PERP | radar | 30.10.2026 05:20 | 0.002766 | %+0.36 | — | — | — |
| RLCUSDT | MEXC PERP | radar | 30.10.2026 05:35 | 0.50475 | %+1.20 | — | — | — |
| PEPEUSDT | MEXC SPOT | radar | 30.10.2026 05:35 | 4.7355e-06 | %+1.43 | — | — | — |
| ORDERUSDT | MEXC PERP | radar | 30.10.2026 05:40 | 0.035165 | %+2.20 | — | — | — |
| STONKUSDT | MEXC SPOT | radar | 30.10.2026 05:50 | 0.134136 | %+2.48 | — | — | — |
| EDGEUSDT | OKX SPOT | radar | 30.10.2026 06:10 | 0.33135 | %-1.13 | — | — | — |
| STABLEUSDT | MEXC SPOT | radar | 30.10.2026 06:20 | 0.025304 | %+1.40 | — | — | — |
| FOGOUSDT | OKX PERP | triggered | 30.10.2026 06:30 | 0.0028075 | %-0.87 | — | — | — |
| RAYUSDT | MEXC SPOT | radar | 30.10.2026 06:35 | 1.62885 | %+1.05 | — | — | — |
| OPGUSDT | OKX PERP | radar | 30.10.2026 06:45 | 0.11632 | %-0.78 | — | — | — |
| EVAAUSDT | MEXC SPOT | radar | 30.10.2026 06:50 | 1.23905 | %-7.52 | — | — | — |
| 1000RATSUSDT | MEXC PERP | radar | 30.10.2026 07:10 | 0.016335 | %+0.46 | — | — | — |
| BOMEUSDT | OKX SPOT | radar | 30.10.2026 07:20 | 0.00061945 | %+1.12 | — | — | — |
| ZROUSDT | OKX PERP | radar | 30.10.2026 07:35 | 1.6388 | %+0.85 | — | — | — |
| FARTCOINUSDT | MEXC SPOT | radar | 30.10.2026 07:41 | 0.11923 | %+0.79 | — | — | — |
| MONUSDT | MEXC SPOT | radar | 30.10.2026 07:46 | 0.019865 | %+0.78 | — | — | — |
| PIPPINUSDT | MEXC SPOT | radar | 30.10.2026 07:51 | 0.01387 | %+0.40 | — | — | — |
| CNPYUSDT | OKX PERP | radar | 30.10.2026 08:11 | 0.19005 | — | — | — | — |
| CROUSDT | MEXC PERP | radar | 30.10.2026 08:21 | 0.05152 | — | — | — | — |
| UAIUSDT | MEXC PERP | radar | 30.10.2026 08:41 | 0.27215 | — | — | — | — |
| XLMUSDT | OKX SPOT | radar | 30.10.2026 08:41 | 0.167565 | — | — | — | — |
| GRASSUSDT | OKX SPOT | radar | 30.10.2026 08:51 | 0.59555 | — | — | — | — |
| UBUSDT | OKX PERP | radar | 30.10.2026 08:51 | 0.111685 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 1, "attempted": 1, "observed_ms": 1793339792652, "unique_reads": 2}, "summary": {"radar": {"unique_symbol_labels": 57, "hours": {"1": {"known": 51, "median_pct": -0.20121489132732817}, "4": {"known": 34, "median_pct": -1.7671841774978492}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}, "triggered": {"unique_symbol_labels": 1, "hours": {"1": {"known": 1, "median_pct": -0.8726625111309061}, "4": {"known": 0, "median_pct": null}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}}}
