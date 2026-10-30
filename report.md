# Coin Tarama5 — V3

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → ayrı geri test giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 30.10.2026 07:30 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 108, "p95_minutes": 5.000016666666666, "longest_minutes": 5.585633333333333, "over_10_minutes": 0}, "within_session": {"intervals": 104, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 4, "p95_minutes": 5.585633333333333, "longest_minutes": 5.585633333333333, "over_10_minutes": 0}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| FIGHTUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 01:53 | 0.0040325 | 0.003969 | 0.0036397004 |
| HAEDALUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 04:05 | 0.022535 | 0.02144 | 0.020507524 |
| FOGOUSDT | OKX PERP | GERİ TEST — GİRİŞ TEYİDİ | 30.10.2026 05:20 | 0.0027845 | 0.002743 | 0.0027394611 |
| STABLEUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 06:20 | 0.025625 | 0.024837 | 0.024112822 |
| RAYUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 06:35 | 1.6608 | 1.5979 | 1.5328546 |
| SOPHUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 06:35 | 0.0014735 | 0.001308 | 0.0011827829 |
| OPGUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 06:45 | 0.115465 | 0.11368 | 0.11059393 |
| 1000RATSUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 07:10 | 0.016435 | 0.01648 | 0.016105144 |
| BOMEUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 07:20 | 0.00061535 | 0.0006164 | 0.00057625237 |

## Kapsam ve eleme

{"observed_ms": 1793334639317, "new_radars": [], "liquid_tickers": 1526, "candles_evaluated": 130, "errors": {"MEXC:SPOT": [], "OKX:SPOT": [], "MEXC:PERP": [], "OKX:PERP": []}, "failed_groups": []}

OKX:SPOT: {"active_catalog": 372, "valid_liquid_tickers": 238, "observed_ms": 1793334626055, "selected_for_candles": 31, "candles_evaluated": 31, "fresh_candidate_quotes": 5, "funnel": {"candles_evaluated": 31, "volume_not_accelerating": 22, "close_not_strong": 6, "price_structure_not_ready": 10}, "calls": 38, "errors": []}

OKX:PERP: {"active_catalog": 508, "valid_liquid_tickers": 459, "observed_ms": 1793334626047, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 5, "funnel": {"candles_evaluated": 32, "volume_not_accelerating": 24, "price_structure_not_ready": 12, "close_not_strong": 4}, "calls": 41, "errors": []}

MEXC:SPOT: {"active_catalog": 1247, "valid_liquid_tickers": 279, "observed_ms": 1793334626282, "selected_for_candles": 33, "candles_evaluated": 33, "fresh_candidate_quotes": 4, "funnel": {"candles_evaluated": 33, "close_not_strong": 11, "price_structure_not_ready": 16, "volume_not_accelerating": 28}, "calls": 36, "errors": []}

MEXC:PERP: {"active_catalog": 570, "valid_liquid_tickers": 550, "observed_ms": 1793334626348, "selected_for_candles": 34, "candles_evaluated": 34, "fresh_candidate_quotes": 6, "funnel": {"candles_evaluated": 34, "volume_not_accelerating": 29, "close_not_strong": 6, "price_structure_not_ready": 17}, "calls": 39, "errors": []}

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
| NESUSDT | OKX SPOT | radar | 30.10.2026 03:29 | 0.11995 | %-0.71 | — | — | — |
| CTUSDT | MEXC SPOT | radar | 30.10.2026 04:05 | 0.13465 | %-4.57 | — | — | — |
| HAEDALUSDT | MEXC PERP | radar | 30.10.2026 04:05 | 0.02219 | %-0.05 | — | — | — |
| APRUSDT | OKX PERP | radar | 30.10.2026 04:10 | 0.05685 | %+3.22 | — | — | — |
| BULLAUSDT | MEXC SPOT | radar | 30.10.2026 04:20 | 0.076583 | %-5.98 | — | — | — |
| AKEUSDT | MEXC SPOT | radar | 30.10.2026 04:20 | 0.02104715 | %-0.20 | — | — | — |
| USOUSDT | OKX PERP | radar | 30.10.2026 04:50 | 169.85 | %-0.68 | — | — | — |
| DOODUSDT | OKX SPOT | radar | 30.10.2026 05:05 | 0.00191 | %+6.96 | — | — | — |
| FOGOUSDT | OKX PERP | radar | 30.10.2026 05:20 | 0.002766 | %+0.36 | — | — | — |
| RLCUSDT | MEXC PERP | radar | 30.10.2026 05:35 | 0.50475 | %+1.20 | — | — | — |
| PEPEUSDT | MEXC SPOT | radar | 30.10.2026 05:35 | 4.7355e-06 | %+1.43 | — | — | — |
| ORDERUSDT | MEXC PERP | radar | 30.10.2026 05:40 | 0.035165 | %+2.20 | — | — | — |
| STONKUSDT | MEXC SPOT | radar | 30.10.2026 05:50 | 0.134136 | %+2.48 | — | — | — |
| EDGEUSDT | OKX SPOT | radar | 30.10.2026 06:10 | 0.33135 | %-1.13 | — | — | — |
| STABLEUSDT | MEXC SPOT | radar | 30.10.2026 06:20 | 0.025304 | %+1.40 | — | — | — |
| FOGOUSDT | OKX PERP | triggered | 30.10.2026 06:30 | 0.0028075 | — | — | — | — |
| RAYUSDT | MEXC SPOT | radar | 30.10.2026 06:35 | 1.62885 | — | — | — | — |
| OPGUSDT | OKX PERP | radar | 30.10.2026 06:45 | 0.11632 | — | — | — | — |
| EVAAUSDT | MEXC SPOT | radar | 30.10.2026 06:50 | 1.23905 | — | — | — | — |
| 1000RATSUSDT | MEXC PERP | radar | 30.10.2026 07:10 | 0.016335 | — | — | — | — |
| BOMEUSDT | OKX SPOT | radar | 30.10.2026 07:20 | 0.00061945 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 1, "attempted": 1, "observed_ms": 1793334342949, "unique_reads": 2}, "summary": {"radar": {"unique_symbol_labels": 47, "hours": {"1": {"known": 42, "median_pct": -0.692848298212767}, "4": {"known": 27, "median_pct": -1.9648902383694433}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}, "triggered": {"unique_symbol_labels": 1, "hours": {"1": {"known": 0, "median_pct": null}, "4": {"known": 0, "median_pct": null}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}}}
