# Coin Tarama 5 — V2

Kapalı 15dk: hazırlık → hacimli kırılım → düşük hacimli geri test → sonraki mumda güçlenme. Hazırlıklar sessiz izlenir; yalnız tetik ve daha önce bildirilmiş adayın iptal/süre olayı bildirilir. Emir gönderilmez.

Son tamamlanmış tarama: 29.10.2026 14:35 TR.

Her borsanın mevcut likit spot+perpetual evrenindeki en çok60 coin her döngüde incelenir; daha önceki 12li rotasyon kaldırıldı. Teknik adaylar borsa başına en çok12lik sessiz havuzda oran geçmişi biriktirir. Aktif tetik üst sınırı küresel5 farklı sembol.

Hedef döngü5dk; gerçek başlangıç aralıkları (veri erişimi anlamına gelmez): {"all_starts": {"intervals": 0, "p95_minutes": null, "longest_minutes": null, "over_10_minutes": 0}, "within_session": {"intervals": 0, "p95_minutes": null, "longest_minutes": null, "over_10_minutes": 0}, "between_sessions": {"intervals": 0, "p95_minutes": null, "longest_minutes": null, "over_10_minutes": 0}, "note": "Loop starts are not evidence of complete provider data."}

| Coin | Borsa | Aşama | Son spot | Direnç | Geçersizlik | Hedef | Son gözlem TR |
|---|---|---|---:|---:|---:|---:|---|
| XPLUSDT | MEXC | SESSİZ HAZIRLIK | 0.077085 | 0.07796 | 0.076529569 | — | 29.10.2026 14:35 |
| STRKUSDT | MEXC | SESSİZ HAZIRLIK | 0.046175 | 0.04682 | 0.045976612 | — | 29.10.2026 14:35 |
| TRXUSDT | MEXC | SESSİZ HAZIRLIK | 0.33165 | 0.3317 | 0.33125498 | — | 29.10.2026 14:35 |

## Eleme ve veri kapsamı

{"observed_ms": 1793273748164, "new_preparations": ["XPLUSDT", "STRKUSDT", "TRXUSDT"], "reasons": {"oi_growth_insufficient": 3, "1h_structure_weak": 49, "price_preparation_not_ready": 117, "4h_structure_weak": 56, "btc_relative_weak": 19, "stale_quotes_excluded": 0}, "evaluated": 120, "candidate_quotes": 3, "errors": {"OKX": [], "MEXC": ["TRXUSDT BINANCE: BINANCE: public HTTP 451", "STRKUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "XPLUSDT BINANCE: BINANCE: public requests stopped after access/rate error"]}, "failed_venues": []}

{"OKX": {"coverage": {"active_spot": 372, "liquid_spot_perpetual": 123, "bounded_universe": 60, "requested": 60, "attempted": 60, "chart_evaluated": 60, "evaluated": 0, "candidate_quotes": 0, "active": 0, "chart_budget_seconds": 150}, "errors": [], "calls": {"spot": 183, "futures": 6, "ratios": {"OKX": 0, "BINANCE": 0}}, "cursor": 0}, "MEXC": {"coverage": {"active_spot": 1246, "liquid_spot_perpetual": 110, "bounded_universe": 60, "requested": 60, "attempted": 60, "chart_evaluated": 60, "evaluated": 3, "candidate_quotes": 3, "active": 0, "chart_budget_seconds": 150}, "errors": ["TRXUSDT BINANCE: BINANCE: public HTTP 451", "STRKUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "XPLUSDT BINANCE: BINANCE: public requests stopped after access/rate error"], "calls": {"spot": 186, "futures": 7, "ratios": {"OKX": 4, "BINANCE": 1}}, "cursor": 0}}

OI kontrat adedinde gerçek45–75dk bazına göre en az%3 artış ve aynı aralıkta vadeli fiyat -%0.5/+%6 zorunlu. Baz yoksa bilinmiyor. Short payı+2yüzde puan şartı destek puanıdır; zorunlu değildir. OKX ve Binance grupları ayrı kalır; eksik oran verisi short açıldığı/azaldığı sayılmaz. Negatif fonlama ek destektir.

BTC son kapalı1s EMA20 altında ve EMA20 son3s düşüyorsa yeni long teyidi yok. Coinin1s/4s yapısı ve BTC göreli güç kontrolleri korunur. RSI/SAR açıklayıcıdır.

Giriş kırılan seviyeden en çok0.5ATR uzaklıkta; stop geri test dibi-0.15ATR ile ilk taban geçersizliğinin yüksek olanı. Risk en çok%6. En az iki sağ/sol kapalı4s mumla doğrulanmış yukarı tepe gerekir; bilinmeyen direnç2R alan sayılmaz. %0.5 toplam maliyet varsayımı dahil en az2R alan aranır.

## Gerçek gözlem ölçümleri

İlk farklı sembolün ilk gerçek tetik fiyatı değişmez. Önceki V1 kayıtları previous_v1 içinde aynen arşivlenir; yeni başarı sayılmaz. Saat getirileri1/4/12/24, BTC farkı, MAE/MFE yanında stop/hedef sırası ve maliyet sonrası R tutulur. Bunlar varsayımsal fiyat yolu ölçümüdür, gerçekleşmiş emir/net kâr değildir.

| Coin | Borsa | İlk tetik TR | Referans | Short teyidi | 1s | 4s | 12s | 24s |
|---|---|---|---:|---|---|---|---|---|

Short teyitli alt küme aynı girişlerin içindedir; iki bağımsız başarı gibi toplanmaz. Unknown kaynaklar ayrıca sayılır. Bu gözlemsel karşılaştırma tek başına short filtresinin nedensel katkısını kanıtlamaz.

Aynı1dk mumunda stop ve hedef varsa sıra belirsizdir. Giriş dakikasının zaman sırası bilinmiyorsa veya ilk dokunuştan önce eksik mum varsa sonuç bilinmiyor. Fiyat boşluğunda stop için daha kötü açılış kullanılır; bu fill garantisi değildir.

Maliyet senaryoları toplam%0.2/%0.5/%1; R ve saat getirileri farklı ölçümlerdir. Gerçek komisyon/kayma/fonlama ölçülmüş sayılmaz.

Ölçüm durumu: {"errors": [], "measurement": {"observed_ms": 1793273751460, "pending": 0, "attempted": 0, "unique_reads": 0}, "comparison": {"all_retest_entries": 0, "nested_short_confirmed": 0, "short_information_unknown": 0, "note": "Nested observational subsets at the same entries; not randomized independent trials.", "by_horizon": {"1": {"all_retests": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "short_confirmed": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "observed_without_short_confirmation": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "short_unknown": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}}, "4": {"all_retests": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "short_confirmed": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "observed_without_short_confirmation": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "short_unknown": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}}, "12": {"all_retests": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "short_confirmed": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "observed_without_short_confirmation": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "short_unknown": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}}, "24": {"all_retests": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "short_confirmed": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "observed_without_short_confirmation": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "short_unknown": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}}}}}
