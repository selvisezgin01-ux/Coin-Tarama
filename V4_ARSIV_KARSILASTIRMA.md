# V3 / deneysel V4 — arşiv karşılaştırması

Bu geriye dönük bir sağlamlık kontrolüdür; ileriye dönük doğrulama veya gerçekleşebilir net kâr testi değildir.
Ortak veri kümesi: 246 MEXC sembolü. Bilinen tasarım örnekleri aşağıdaki toplamlardan çıkarıldı.

| Sürüm | Bildirim olayı | Farklı coin | 48s ölçülen | Medyan 48s % | BTC üstü medyan puan | Kontrol üstü medyan puan | 48s ≤0 oranı |
|---|---:|---:|---:|---:|---:|---:|---:|
| v3 | 323 | 126 | 319 | -0.96 | -1.32 | -0.34 | 57.05% |
| v4 | 724 | 181 | 717 | -0.88 | -1.27 | -0.59 | 56.21% |

## Sınırlar

- Archive and current-listing selection bias; no market-wide success rate.
- Known examples excluded from headline aggregates; remaining data are still retrospective.
- Closed-price references, no bid/ask, fees or executable profit.
- 48h cooldown per symbol within each model; events can still share market exposure.
- Matched controls are descriptive and can be reused; no independent significance claim.

12/24/48 saatlik ayrıntılar summary.json, olaylar events.json dosyasındadır. Örneklerdeki artışlar eşik seçmek için tekrar optimize edilmez.
