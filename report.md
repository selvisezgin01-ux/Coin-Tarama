# Coin Tarama5 — V3

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → ayrı geri test giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 29.10.2026 23:58 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 18, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "within_session": {"intervals": 18, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 0, "p95_minutes": null, "longest_minutes": null, "over_10_minutes": 0}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| PARTIUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 22:48 | 0.05742 | 0.0641 | 0.048721984 |
| XSNXXUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 23:33 | 8.995 | 9.414 | 8.4345115 |
| SNDKUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 23:33 | 1309.15 | 1341.2 | 1267.9833 |
| SNXXUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 23:33 | 8.9955 | 9.431 | 8.4187079 |
| BTWUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 23:48 | 1.5273 | 1.5183 | 1.4363281 |
| XUVXYUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 23:58 | 17.475 | 17.4 | 16.810019 |
| SKDDUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 23:58 | 8.345 | 8.28 | 7.7328067 |

## Kapsam ve eleme

{"observed_ms": 1793307515833, "new_radars": ["OKX:SPOT:XUVXYUSDT", "OKX:PERP:SKDDUSDT"], "liquid_tickers": 1450, "candles_evaluated": 125, "errors": {"MEXC:SPOT": [], "OKX:SPOT": [], "OKX:PERP": ["BTWUSDT 4h optional context: Missing/stale closed history"], "MEXC:PERP": ["PREDICTUSDT 4h optional context: Missing/stale closed history"]}, "failed_groups": []}

OKX:SPOT: {"active_catalog": 372, "valid_liquid_tickers": 212, "observed_ms": 1793307506590, "selected_for_candles": 31, "candles_evaluated": 31, "fresh_candidate_quotes": 2, "funnel": {"candles_evaluated": 31, "close_not_strong": 29, "price_structure_not_ready": 30}, "calls": 28, "errors": []}

OKX:PERP: {"active_catalog": 508, "valid_liquid_tickers": 454, "observed_ms": 1793307506885, "selected_for_candles": 33, "candles_evaluated": 33, "fresh_candidate_quotes": 4, "funnel": {"candles_evaluated": 33, "close_not_strong": 28, "price_structure_not_ready": 30, "volume_not_accelerating": 2}, "calls": 28, "errors": ["BTWUSDT 4h optional context: Missing/stale closed history"]}

MEXC:SPOT: {"active_catalog": 1247, "valid_liquid_tickers": 239, "observed_ms": 1793307506989, "selected_for_candles": 30, "candles_evaluated": 30, "fresh_candidate_quotes": 0, "funnel": {"candles_evaluated": 30, "close_not_strong": 30, "price_structure_not_ready": 29, "volume_not_accelerating": 8}, "calls": 19, "errors": []}

MEXC:PERP: {"active_catalog": 570, "valid_liquid_tickers": 545, "observed_ms": 1793307507147, "selected_for_candles": 31, "candles_evaluated": 31, "fresh_candidate_quotes": 3, "funnel": {"candles_evaluated": 31, "volume_not_accelerating": 11, "close_not_strong": 28, "price_structure_not_ready": 27}, "calls": 27, "errors": ["PREDICTUSDT 4h optional context: Missing/stale closed history"]}

Ayrıntılı evren/ret nedenleri ve seçilen kimlikler state içinde saklanır. Rolling24s hacim farkı yalnız sıralama vekilidir,5dk alım hacmi değildir. Hacim sinyali yalnız kapalı15dk gerçek quote hacmiyle ölçülür.4s trend/OI erken radarı engellemez.3yeni radar/döngü,6radar/saat ve20aktif izleme sınırı vardır; kota dışı fırsatlar kaçabilir.

## İlk gerçek gözlem ölçümleri

Radar ve giriş ayrı referanslardır, bağımsız iki başarı gibi toplanmaz. Aynı sembolün ilk evre referansı korunur; borsalar/pazarlar arası fiyatlar birleştirilmez. Eski V2 kayıtları değişmeyen arşiv commitinde korunur.

| Coin | Pazar | Evre | Gözlem TR | Referans | 1s | 4s | 12s | 24s |
|---|---|---|---|---:|---|---|---|---|
| DODOUSDT | MEXC PERP | radar | 29.10.2026 22:28 | 0.025465 | %-1.98 | — | — | — |
| AVNTUSDT | MEXC PERP | radar | 29.10.2026 22:28 | 0.10225 | %-2.20 | — | — | — |
| CENTUSDT | MEXC SPOT | radar | 29.10.2026 22:28 | 0.0016625 | %-6.23 | — | — | — |
| DYDXUSDT | MEXC SPOT | radar | 29.10.2026 22:48 | 0.11404 | %-3.91 | — | — | — |
| POLYXUSDT | MEXC PERP | radar | 29.10.2026 22:48 | 0.03369 | %-4.16 | — | — | — |
| PARTIUSDT | MEXC PERP | radar | 29.10.2026 22:48 | 0.06075 | — | — | — | — |
| XSNXXUSDT | OKX SPOT | radar | 29.10.2026 23:33 | 9.8315 | — | — | — | — |
| SNDKUSDT | OKX PERP | radar | 29.10.2026 23:33 | 1369.35 | — | — | — | — |
| SNXXUSDT | OKX PERP | radar | 29.10.2026 23:33 | 9.8315 | — | — | — | — |
| BTWUSDT | OKX PERP | radar | 29.10.2026 23:48 | 1.5202 | — | — | — | — |
| XUVXYUSDT | OKX SPOT | radar | 29.10.2026 23:58 | 17.475 | — | — | — | — |
| SKDDUSDT | OKX PERP | radar | 29.10.2026 23:58 | 8.345 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 3, "attempted": 2, "observed_ms": 1793307221957, "unique_reads": 4}, "summary": {"radar": {"unique_symbol_labels": 10, "hours": {"1": {"known": 5, "median_pct": -3.910908453174333}, "4": {"known": 0, "median_pct": null}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}, "triggered": {"unique_symbol_labels": 0, "hours": {"1": {"known": 0, "median_pct": null}, "4": {"known": 0, "median_pct": null}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}}}
