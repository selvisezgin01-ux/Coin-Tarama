# Coin Tarama5 — V3

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → ayrı geri test giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 30.10.2026 03:29 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 60, "p95_minutes": 5.000016666666666, "longest_minutes": 5.554583333333333, "over_10_minutes": 0}, "within_session": {"intervals": 58, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 2, "p95_minutes": 5.554583333333333, "longest_minutes": 5.554583333333333, "over_10_minutes": 0}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| PARTIUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 22:48 | 0.056975 | 0.0641 | 0.048721984 |
| XUVXYUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 23:58 | 17.73 | 17.4 | 16.810019 |
| RUNEUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 00:58 | 0.60355 | 0.6152 | 0.57562574 |
| FIGHTUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 01:53 | 0.0037415 | 0.003969 | 0.0036397004 |
| MEGAUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 02:04 | 0.04432 | 0.04508 | 0.042944758 |
| BEATUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 03:04 | 0.099165 | 0.10257 | 0.098034875 |
| SAMSUNGUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 03:14 | 166.175 | 166.13 | 162.54105 |
| BWETUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 03:19 | 948.125 | 945.93 | 911.52102 |
| NESUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 30.10.2026 03:29 | 0.11995 | 0.12 | 0.11632779 |

## Kapsam ve eleme

{"observed_ms": 1793320172712, "new_radars": ["OKX:SPOT:NESUSDT"], "liquid_tickers": 1489, "candles_evaluated": 127, "errors": {"MEXC:SPOT": ["AXISUSDT 4h optional context: Missing/stale closed history"], "MEXC:PERP": ["AXISUSDT 4h optional context: Missing/stale closed history"], "OKX:SPOT": [], "OKX:PERP": ["AXISUSDT 4h optional context: Missing/stale closed history"]}, "failed_groups": []}

OKX:SPOT: {"active_catalog": 372, "valid_liquid_tickers": 230, "observed_ms": 1793320161708, "selected_for_candles": 31, "candles_evaluated": 31, "fresh_candidate_quotes": 3, "funnel": {"candles_evaluated": 31, "volume_not_accelerating": 19, "price_structure_not_ready": 28, "close_not_strong": 25}, "calls": 32, "errors": []}

OKX:PERP: {"active_catalog": 508, "valid_liquid_tickers": 457, "observed_ms": 1793320161119, "selected_for_candles": 32, "candles_evaluated": 32, "fresh_candidate_quotes": 6, "funnel": {"candles_evaluated": 32, "close_not_strong": 19, "volume_not_accelerating": 19, "price_structure_not_ready": 19}, "calls": 36, "errors": ["AXISUSDT 4h optional context: Missing/stale closed history"]}

MEXC:SPOT: {"active_catalog": 1247, "valid_liquid_tickers": 259, "observed_ms": 1793320161361, "selected_for_candles": 31, "candles_evaluated": 31, "fresh_candidate_quotes": 3, "funnel": {"candles_evaluated": 31, "volume_not_accelerating": 20, "close_not_strong": 27, "price_structure_not_ready": 26}, "calls": 26, "errors": ["AXISUSDT 4h optional context: Missing/stale closed history"]}

MEXC:PERP: {"active_catalog": 570, "valid_liquid_tickers": 543, "observed_ms": 1793320161443, "selected_for_candles": 33, "candles_evaluated": 33, "fresh_candidate_quotes": 4, "funnel": {"candles_evaluated": 33, "volume_not_accelerating": 29, "price_structure_not_ready": 28, "close_not_strong": 28}, "calls": 27, "errors": ["AXISUSDT 4h optional context: Missing/stale closed history"]}

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
| XSNXXUSDT | OKX SPOT | radar | 29.10.2026 23:33 | 9.8315 | %-10.07 | — | — | — |
| SNDKUSDT | OKX PERP | radar | 29.10.2026 23:33 | 1369.35 | %-4.93 | — | — | — |
| SNXXUSDT | OKX PERP | radar | 29.10.2026 23:33 | 9.8315 | %-9.84 | — | — | — |
| BTWUSDT | OKX PERP | radar | 29.10.2026 23:48 | 1.5202 | %+1.24 | — | — | — |
| XUVXYUSDT | OKX SPOT | radar | 29.10.2026 23:58 | 17.475 | %+0.54 | — | — | — |
| SKDDUSDT | OKX PERP | radar | 29.10.2026 23:58 | 8.345 | %+1.83 | — | — | — |
| JSTUSDT | MEXC PERP | radar | 30.10.2026 00:34 | 0.143265 | %-0.74 | — | — | — |
| OLUSDT | OKX PERP | radar | 30.10.2026 00:34 | 0.0074535 | %-1.90 | — | — | — |
| SUNUSDT | MEXC PERP | radar | 30.10.2026 00:43 | 0.0164935 | %+2.54 | — | — | — |
| JP225USDT | OKX PERP | radar | 30.10.2026 00:48 | 64388 | %-0.87 | — | — | — |
| RUNEUSDT | MEXC PERP | radar | 30.10.2026 00:58 | 0.63125 | %+1.50 | — | — | — |
| XDPUSDT | OKX SPOT | radar | 30.10.2026 01:03 | 0.018779 | %+0.10 | — | — | — |
| TMFUSDT | OKX PERP | radar | 30.10.2026 01:48 | 29.635 | %+0.22 | — | — | — |
| SOPHUSDT | OKX SPOT | radar | 30.10.2026 01:48 | 0.0014635 | %-3.25 | — | — | — |
| SOLVUSDT | MEXC PERP | radar | 30.10.2026 01:49 | 0.0048225 | %-0.03 | — | — | — |
| FIGHTUSDT | MEXC SPOT | radar | 30.10.2026 01:53 | 0.0039185 | %-1.75 | — | — | — |
| CAPUSDT | MEXC PERP | radar | 30.10.2026 02:04 | 0.078375 | %-2.01 | — | — | — |
| MEGAUSDT | MEXC PERP | radar | 30.10.2026 02:04 | 0.0453 | %+1.02 | — | — | — |
| BEATUSDT | MEXC SPOT | radar | 30.10.2026 03:04 | 0.10283 | — | — | — | — |
| SAMSUNGUSDT | OKX PERP | radar | 30.10.2026 03:14 | 167.79 | — | — | — | — |
| BWETUSDT | OKX PERP | radar | 30.10.2026 03:19 | 950.98 | — | — | — | — |
| NESUSDT | OKX SPOT | radar | 30.10.2026 03:29 | 0.11995 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 0, "attempted": 0, "observed_ms": 1793319883928, "unique_reads": 0}, "summary": {"radar": {"unique_symbol_labels": 27, "hours": {"1": {"known": 24, "median_pct": -1.8232774390879392}, "4": {"known": 6, "median_pct": -6.116203241853518}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}, "triggered": {"unique_symbol_labels": 0, "hours": {"1": {"known": 0, "median_pct": null}, "4": {"known": 0, "median_pct": null}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}}}
