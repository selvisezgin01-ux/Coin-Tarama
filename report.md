# Coin Tarama 5 — V2

Kapalı 15dk: hazırlık → hacimli kırılım → düşük hacimli geri test → sonraki mumda güçlenme. Hazırlıklar sessiz izlenir; yalnız tetik ve daha önce bildirilmiş adayın iptal/süre olayı bildirilir. Emir gönderilmez.

Son tamamlanmış tarama: 29.10.2026 19:10 TR.

Her borsanın mevcut likit spot+perpetual evrenindeki en çok60 coin her döngüde incelenir; daha önceki 12li rotasyon kaldırıldı. Teknik adaylar borsa başına en çok12lik sessiz havuzda oran geçmişi biriktirir. Aktif tetik üst sınırı küresel5 farklı sembol.

Hedef döngü5dk; gerçek başlangıç aralıkları (veri erişimi anlamına gelmez): {"all_starts": {"intervals": 55, "p95_minutes": 5.000016666666666, "longest_minutes": 5.476683333333333, "over_10_minutes": 0}, "within_session": {"intervals": 53, "p95_minutes": 5.000016666666666, "longest_minutes": 5.000016666666666, "over_10_minutes": 0}, "between_sessions": {"intervals": 2, "p95_minutes": 5.476683333333333, "longest_minutes": 5.476683333333333, "over_10_minutes": 0}, "note": "Loop starts are not evidence of complete provider data."}

| Coin | Borsa | Aşama | Son spot | Direnç | Geçersizlik | Hedef | Son gözlem TR |
|---|---|---|---:|---:|---:|---:|---|
| TIAUSDT | MEXC | KIRILIM İZLEME | 0.5485 | 0.5358 | 0.53115998 | — | 29.10.2026 19:10 |
| LINKUSDT | MEXC | KIRILIM İZLEME | 11.9955 | 11.642 | 11.564362 | — | 29.10.2026 19:10 |
| OKBUSDT | OKX | KIRILIM İZLEME | 113.79 | 111.33 | 110.75912 | — | 29.10.2026 19:10 |
| UNIUSDT | OKX | KIRILIM İZLEME | 7.5075 | 7.246 | 7.1236494 | — | 29.10.2026 19:10 |
| FILUSDT | OKX | KIRILIM İZLEME | 0.92065 | 0.908 | 0.90151372 | — | 29.10.2026 19:10 |
| ASTERUSDT | MEXC | KIRILIM İZLEME | 0.72465 | 0.7054 | 0.70234569 | — | 29.10.2026 19:10 |
| BICOUSDT | OKX | KIRILIM İZLEME | 0.017515 | 0.01663 | 0.016323866 | — | 29.10.2026 19:10 |
| ETHFIUSDT | MEXC | KIRILIM İZLEME | 0.68865 | 0.6691 | 0.65740908 | — | 29.10.2026 19:10 |
| PENDLEUSDT | MEXC | KIRILIM İZLEME | 2.0215 | 1.947 | 1.9202411 | — | 29.10.2026 19:10 |
| ADAUSDT | MEXC | KIRILIM İZLEME | 0.208 | 0.2023 | 0.20024663 | — | 29.10.2026 19:10 |
| KASUSDT | MEXC | KIRILIM İZLEME | 0.0372145 | 0.036134 | 0.03573992 | — | 29.10.2026 19:10 |
| BEATUSDT | MEXC | KIRILIM İZLEME | 0.10801 | 0.10184 | 0.096611069 | — | 29.10.2026 19:10 |
| HYPEUSDT | OKX | KIRILIM İZLEME | 95.6605 | 92.131 | 90.129285 | — | 29.10.2026 19:10 |
| APTUSDT | OKX | GERİ TEST | 0.7045 | 0.685 | 0.67550061 | — | 29.10.2026 19:10 |
| DOTUSDT | OKX | GERİ TEST | 1.0192 | 1.0013 | 0.98750976 | — | 29.10.2026 19:10 |
| OPUSDT | OKX | KIRILIM İZLEME | 0.11445 | 0.11177 | 0.11028211 | — | 29.10.2026 19:10 |
| AVAXUSDT | OKX | KIRILIM İZLEME | 9.053 | 8.86 | 8.7559065 | — | 29.10.2026 19:10 |

## Eleme ve veri kapsamı

{"observed_ms": 1793290251558, "new_preparations": [], "reasons": {"oi_growth_insufficient": 14, "price_not_holding_or_extended": 1, "btc_relative_weak": 26, "price_preparation_not_ready": 120, "4h_structure_weak": 5, "1h_structure_weak": 10, "stale_quotes_excluded": 0}, "evaluated": 120, "candidate_quotes": 17, "errors": {"MEXC": ["TIAUSDT BINANCE: BINANCE: public HTTP 451", "LINKUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "ASTERUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "ETHFIUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "PENDLEUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "ADAUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "KASUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "BEATUSDT BINANCE: BINANCE: public requests stopped after access/rate error"], "OKX": ["OKBUSDT BINANCE: BINANCE: public HTTP 451", "UNIUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "FILUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "BICOUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "HYPEUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "APTUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "DOTUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "OPUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "AVAXUSDT BINANCE: BINANCE: public requests stopped after access/rate error"]}, "failed_venues": []}

{"OKX": {"coverage": {"active_spot": 372, "liquid_spot_perpetual": 124, "bounded_universe": 60, "requested": 60, "attempted": 60, "chart_evaluated": 60, "evaluated": 9, "candidate_quotes": 9, "active": 9, "chart_budget_seconds": 150}, "errors": ["OKBUSDT BINANCE: BINANCE: public HTTP 451", "UNIUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "FILUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "BICOUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "HYPEUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "APTUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "DOTUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "OPUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "AVAXUSDT BINANCE: BINANCE: public requests stopped after access/rate error"], "calls": {"spot": 15, "futures": 15, "ratios": {"OKX": 10, "BINANCE": 1}}, "cursor": 0}, "MEXC": {"coverage": {"active_spot": 1247, "liquid_spot_perpetual": 111, "bounded_universe": 60, "requested": 60, "attempted": 60, "chart_evaluated": 60, "evaluated": 8, "candidate_quotes": 8, "active": 8, "chart_budget_seconds": 150}, "errors": ["TIAUSDT BINANCE: BINANCE: public HTTP 451", "LINKUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "ASTERUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "ETHFIUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "PENDLEUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "ADAUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "KASUSDT BINANCE: BINANCE: public requests stopped after access/rate error", "BEATUSDT BINANCE: BINANCE: public requests stopped after access/rate error"], "calls": {"spot": 11, "futures": 12, "ratios": {"OKX": 8, "BINANCE": 1}}, "cursor": 0}}

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

Ölçüm durumu: {"errors": [], "measurement": {"observed_ms": 1793289954315, "pending": 0, "attempted": 0, "unique_reads": 0}, "comparison": {"all_retest_entries": 0, "nested_short_confirmed": 0, "short_information_unknown": 0, "note": "Nested observational subsets at the same entries; not randomized independent trials.", "by_horizon": {"1": {"all_retests": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "short_confirmed": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "observed_without_short_confirmation": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "short_unknown": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}}, "4": {"all_retests": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "short_confirmed": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "observed_without_short_confirmation": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "short_unknown": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}}, "12": {"all_retests": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "short_confirmed": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "observed_without_short_confirmation": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "short_unknown": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}}, "24": {"all_retests": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "short_confirmed": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "observed_without_short_confirmation": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}, "short_unknown": {"unique_symbols": 0, "known_path_results": 0, "median_net_r": null, "target_first": 0, "stop_first": 0, "ambiguous_or_missing": 0}}}}}
