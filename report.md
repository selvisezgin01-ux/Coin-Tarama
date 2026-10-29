# Coin Tarama5 — V3

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → ayrı geri test giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 29.10.2026 23:33 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 13, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "within_session": {"intervals": 13, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 0, "p95_minutes": null, "longest_minutes": null, "over_10_minutes": 0}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| PARTIUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 22:48 | 0.058075 | 0.0641 | 0.048721984 |
| XSNXXUSDT | OKX SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 23:33 | 9.8315 | 9.414 | 8.4345115 |
| SNDKUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 23:33 | 1369.35 | 1341.2 | 1267.9833 |
| SNXXUSDT | OKX PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 23:33 | 9.8315 | 9.431 | 8.4187079 |

## Kapsam ve eleme

{"observed_ms": 1793306019144, "new_radars": ["OKX:SPOT:XSNXXUSDT", "OKX:PERP:SNDKUSDT", "OKX:PERP:SNXXUSDT"], "liquid_tickers": 1432, "candles_evaluated": 119, "errors": {"MEXC:SPOT": [], "OKX:SPOT": [], "OKX:PERP": [], "MEXC:PERP": ["JAGENTUSDT: Missing/stale closed history"]}, "failed_groups": []}

OKX:SPOT: {"active_catalog": 372, "valid_liquid_tickers": 198, "observed_ms": 1793306006563, "selected_for_candles": 30, "candles_evaluated": 30, "fresh_candidate_quotes": 1, "funnel": {"candles_evaluated": 30, "price_structure_not_ready": 29, "volume_not_accelerating": 20, "close_not_strong": 23}, "calls": 35, "errors": []}

OKX:PERP: {"active_catalog": 508, "valid_liquid_tickers": 454, "observed_ms": 1793306006549, "selected_for_candles": 30, "candles_evaluated": 30, "fresh_candidate_quotes": 3, "funnel": {"candles_evaluated": 30, "close_not_strong": 17, "price_structure_not_ready": 27, "volume_not_accelerating": 8}, "calls": 37, "errors": []}

MEXC:SPOT: {"active_catalog": 1247, "valid_liquid_tickers": 234, "observed_ms": 1793306006702, "selected_for_candles": 30, "candles_evaluated": 30, "fresh_candidate_quotes": 0, "funnel": {"candles_evaluated": 30, "volume_not_accelerating": 28, "close_not_strong": 20, "price_structure_not_ready": 26}, "calls": 33, "errors": []}

MEXC:PERP: {"active_catalog": 570, "valid_liquid_tickers": 546, "observed_ms": 1793306007567, "selected_for_candles": 30, "candles_evaluated": 29, "fresh_candidate_quotes": 2, "funnel": {"candles_evaluated": 29, "volume_not_accelerating": 21, "price_structure_not_ready": 26, "close_not_strong": 22}, "calls": 35, "errors": ["JAGENTUSDT: Missing/stale closed history"]}

Ayrıntılı evren/ret nedenleri ve seçilen kimlikler state içinde saklanır. Rolling24s hacim farkı yalnız sıralama vekilidir,5dk alım hacmi değildir. Hacim sinyali yalnız kapalı15dk gerçek quote hacmiyle ölçülür.4s trend/OI erken radarı engellemez.3yeni radar/döngü,6radar/saat ve20aktif izleme sınırı vardır; kota dışı fırsatlar kaçabilir.

## İlk gerçek gözlem ölçümleri

Radar ve giriş ayrı referanslardır, bağımsız iki başarı gibi toplanmaz. Aynı sembolün ilk evre referansı korunur; borsalar/pazarlar arası fiyatlar birleştirilmez. Eski V2 kayıtları değişmeyen arşiv commitinde korunur.

| Coin | Pazar | Evre | Gözlem TR | Referans | 1s | 4s | 12s | 24s |
|---|---|---|---|---:|---|---|---|---|
| DODOUSDT | MEXC PERP | radar | 29.10.2026 22:28 | 0.025465 | %-1.98 | — | — | — |
| AVNTUSDT | MEXC PERP | radar | 29.10.2026 22:28 | 0.10225 | — | — | — | — |
| CENTUSDT | MEXC SPOT | radar | 29.10.2026 22:28 | 0.0016625 | %-6.23 | — | — | — |
| DYDXUSDT | MEXC SPOT | radar | 29.10.2026 22:48 | 0.11404 | — | — | — | — |
| POLYXUSDT | MEXC PERP | radar | 29.10.2026 22:48 | 0.03369 | — | — | — | — |
| PARTIUSDT | MEXC PERP | radar | 29.10.2026 22:48 | 0.06075 | — | — | — | — |
| XSNXXUSDT | OKX SPOT | radar | 29.10.2026 23:33 | 9.8315 | — | — | — | — |
| SNDKUSDT | OKX PERP | radar | 29.10.2026 23:33 | 1369.35 | — | — | — | — |
| SNXXUSDT | OKX PERP | radar | 29.10.2026 23:33 | 9.8315 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 3, "attempted": 2, "observed_ms": 1793306027872, "unique_reads": 4}, "summary": {"radar": {"unique_symbol_labels": 9, "hours": {"1": {"known": 2, "median_pct": -4.104338993960455}, "4": {"known": 0, "median_pct": null}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}, "triggered": {"unique_symbol_labels": 0, "hours": {"1": {"known": 0, "median_pct": null}, "4": {"known": 0, "median_pct": null}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}}}
