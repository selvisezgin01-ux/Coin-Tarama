# Coin Tarama5 — V3

Geniş spot/vadeli keşif → erken fiyat/hacim radarı → ayrı geri test giriş teyidi. Erken radar alım teyidi değildir. Emir gönderilmez.

Son gözlem: 29.10.2026 23:13 TR.

Bütün uygun aktif USDT paritelerinin toplu ticker ön elemesi; aynı borsada spot+perpetual kesişim zorunluluğu ve statik ilk60 sınırı yok. Ayrıntılı kapalı mumlar dinamik öncelik+rotasyonla bütçeli okunur; her coin her5dk ayrıntılı incelenmiş sayılmaz.

Hedef5dk, gerçek başlangıç aralıkları: {"all_starts": {"intervals": 9, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "within_session": {"intervals": 9, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 0, "p95_minutes": null, "longest_minutes": null, "over_10_minutes": 0}, "note": "Loop starts are not evidence of complete provider data."}

## Aktif izleme

| Coin | Borsa/pazar | Evre | İlk gerçek gözlem TR | Son fiyat | Seviye | Geçersizlik |
|---|---|---|---|---:|---:|---:|
| AVNTUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 22:28 | 0.10075 | 0.102 | 0.099751048 |
| DYDXUSDT | MEXC SPOT | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 22:48 | 0.113075 | 0.11639 | 0.11288124 |
| PARTIUSDT | MEXC PERP | ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL | 29.10.2026 22:48 | 0.057075 | 0.0641 | 0.048721984 |

## Kapsam ve eleme

{"observed_ms": 1793304819023, "new_radars": [], "liquid_tickers": 1438, "candles_evaluated": 122, "errors": {"OKX:SPOT": [], "MEXC:SPOT": [], "OKX:PERP": [], "MEXC:PERP": []}, "failed_groups": []}

OKX:SPOT: {"active_catalog": 372, "valid_liquid_tickers": 199, "observed_ms": 1793304806559, "selected_for_candles": 30, "candles_evaluated": 30, "fresh_candidate_quotes": 0, "funnel": {"candles_evaluated": 30, "price_structure_not_ready": 30, "volume_not_accelerating": 27, "close_not_strong": 25}, "calls": 22, "errors": []}

OKX:PERP: {"active_catalog": 508, "valid_liquid_tickers": 455, "observed_ms": 1793304806704, "selected_for_candles": 30, "candles_evaluated": 30, "fresh_candidate_quotes": 5, "funnel": {"candles_evaluated": 30, "volume_not_accelerating": 20, "close_not_strong": 16, "price_structure_not_ready": 18}, "calls": 30, "errors": []}

MEXC:SPOT: {"active_catalog": 1247, "valid_liquid_tickers": 237, "observed_ms": 1793304806866, "selected_for_candles": 31, "candles_evaluated": 31, "fresh_candidate_quotes": 1, "funnel": {"candles_evaluated": 31, "close_not_strong": 28, "price_structure_not_ready": 28, "volume_not_accelerating": 28}, "calls": 24, "errors": []}

MEXC:PERP: {"active_catalog": 570, "valid_liquid_tickers": 547, "observed_ms": 1793304807775, "selected_for_candles": 31, "candles_evaluated": 31, "fresh_candidate_quotes": 2, "funnel": {"candles_evaluated": 31, "close_not_strong": 29, "price_structure_not_ready": 29, "volume_not_accelerating": 27}, "calls": 29, "errors": []}

Ayrıntılı evren/ret nedenleri ve seçilen kimlikler state içinde saklanır. Rolling24s hacim farkı yalnız sıralama vekilidir,5dk alım hacmi değildir. Hacim sinyali yalnız kapalı15dk gerçek quote hacmiyle ölçülür.4s trend/OI erken radarı engellemez.3yeni radar/döngü,6radar/saat ve20aktif izleme sınırı vardır; kota dışı fırsatlar kaçabilir.

## İlk gerçek gözlem ölçümleri

Radar ve giriş ayrı referanslardır, bağımsız iki başarı gibi toplanmaz. Aynı sembolün ilk evre referansı korunur; borsalar/pazarlar arası fiyatlar birleştirilmez. Eski V2 kayıtları değişmeyen arşiv commitinde korunur.

| Coin | Pazar | Evre | Gözlem TR | Referans | 1s | 4s | 12s | 24s |
|---|---|---|---|---:|---|---|---|---|
| DODOUSDT | MEXC PERP | radar | 29.10.2026 22:28 | 0.025465 | — | — | — | — |
| AVNTUSDT | MEXC PERP | radar | 29.10.2026 22:28 | 0.10225 | — | — | — | — |
| CENTUSDT | MEXC SPOT | radar | 29.10.2026 22:28 | 0.0016625 | — | — | — | — |
| DYDXUSDT | MEXC SPOT | radar | 29.10.2026 22:48 | 0.11404 | — | — | — | — |
| POLYXUSDT | MEXC PERP | radar | 29.10.2026 22:48 | 0.03369 | — | — | — | — |
| PARTIUSDT | MEXC PERP | radar | 29.10.2026 22:48 | 0.06075 | — | — | — | — |

Giriş teyidinde risk<=%3, makas<=%0.3; geri testin üzerinde taze quote aranır. Bilinen direnç maliyet dahil2R hedefi kesiyorsa giriş yok. Direnç bulunmazsa hedef projeksiyondur, alan teyitli sayılmaz. BTC saatlik şok düşüşünde(-%2) giriş engellenir.

1/4/12/24s getiriler, BTC farkı, tam sonraki1dk mumlardan MAE/MFE; girişte ayrıca stop/hedef sırası, aynı mum/giriş parçası belirsizliği ve toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR. Gerçek fill/net kâr/fonlama değildir. OI ve short verisi bulunmazsa bilinmiyor; spot için vadeli şartı uydurulmaz.

Ölçüm: {"errors": [], "queue": {"due": 0, "attempted": 0, "observed_ms": 1793304823951, "unique_reads": 0}, "summary": {"radar": {"unique_symbol_labels": 6, "hours": {"1": {"known": 0, "median_pct": null}, "4": {"known": 0, "median_pct": null}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}, "triggered": {"unique_symbol_labels": 0, "hours": {"1": {"known": 0, "median_pct": null}, "4": {"known": 0, "median_pct": null}, "12": {"known": 0, "median_pct": null}, "24": {"known": 0, "median_pct": null}}}}}
