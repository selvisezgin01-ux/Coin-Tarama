# Coin Tarama Meme — V6

Son çalışma: 30.10.2026 05:21 Türkiye saati.

**Deneysel DEX izleme. Tüm yeni tokenleri kapsamaz ve yükseliş garantisi vermez.**

Kapsam: Solana, Ethereum, BNB Chain, Robinhood (Pons dahil), HyperEVM. Pons ayrı bir ağ değildir.

**Hedef: ilk yükseliş öncesi oluşum/birikim.** Yeni aday yalnız birikim evresinde alınır; ilk kırılım ancak daha önce bildirilen birikimin devamı olarak izlenir. Trend listesi aday kaynağı olarak kullanılmaz. **Cüzdan haritası manuel kontrol bekler.** Kritik kontrat/geliştirici verisi eksik tokenler bildirilmez.

Geçmişin tamamındaki fitiller ve açık mum dahil gözlenen dipten tepeye yükseliş %25 üzerindeyse, ilk fiyatın %10 üzerine uzamışsa veya tepeden %15 üzeri düşmüşse elenir. Bu eşikler deneysel tercihlerdir. Havuz başlangıcı, ara mumlar veya güncel mum yoksa ilk oluşum teyitsizdir. Eski pump sonrası yataylaşma yeni aday sayılmaz.

GMGN kullanılmaz. Solana: RugCheck + GoPlus Solana; desteklenen EVM ağları: GoPlus. GMGN’nin tüm sniper/bundler etiketleri ve eksiksiz geliştirici geçmişi sağlanmaz. Teknik risk ön elemesi tokenin resmî/orijinal proje kontratı olduğunu kanıtlamaz.

Yeni havuz yaşı tokenin yaratılma yaşı değildir. Market cap sağlayıcı bildirimi olarak, FDV ise açıkça ayrı değer türü olarak gösterilir. Geliştirici teyidi yalnız belirtilen 45 dakikalık işlem penceresindeki raporlanan adrese aittir; ömür boyu hiç satış yapmadığı veya başka cüzdan kullanmadığı anlamına gelmez.

| Ağ | Güncellenen token | Piyasa ön elemesi | Mum incelenen | Ön eleme / manuel harita bekliyor | İnceleme | Erişim/veri hatası |
|---|---:|---:|---:|---:|---:|---:|
| HyperEVM (HYPE) | 31 | 1 | 0 | 0 | 0 | 0 |
| Ethereum | 34 | 0 | 2 | 0 | 0 | 1 |
| BNB Chain | 49 | 1 | 1 | 0 | 0 | 2 |
| Robinhood | 52 | 3 | 1 | 0 | 0 | 2 |
| Solana | 57 | 1 | 2 | 0 | 0 | 1 |

Bu çalışmada aday olmayan mum incelemeleri (token listesi değildir):
- 3: Önceden yükseliş / uzun fitil görülmüş; Başlangıç fiyatından fazla uzaklaşmış
- 1: Önceden yükseliş / uzun fitil görülmüş; Başlangıç fiyatından fazla uzaklaşmış; Tepeden düşüş sonrası yapı elenmiş
- 1: Başlangıç geçmişinde veri boşluğu var
- 1: Havuz başlangıç mumları eksik

## Otomatik ön eleme geçti — manuel harita kontrolü bekliyor

| Token / adres | Ağ | Grup | Piyasa değeri / FDV USD | Geliştirici | Harita | Likidite kilidi | Büyük alıcı desteği | Eksik otomatik kontroller |
|---|---|---|---:|---|---|---|---|---|

**Henüz koşulları sağlayan aday yok.**


## İnceleme — eksik otomatik teyitler

| Token / adres | Ağ | Grup | Piyasa değeri / FDV USD | Geliştirici | Harita | Likidite kilidi | Büyük alıcı desteği | Eksik otomatik kontroller |
|---|---|---|---:|---|---|---|---|---|

Bu çalışmada inceleme kaydı yok.


## Gerçek gözlem kayıtları

Fiyatlar sağlayıcının gözlenen fiyatıdır; emir, alış/satış kotasyonu veya gerçekleşebilir net getiri değildir. İnceleme ve daha sonraki teyitli bildirim fiyatları ayrı tutulur. Aynı token havuz/grup değiştirse de yeni bağımsız coin sayılmaz.

| Token | Ağ | Referans türü | Gerçek gözlem TR | Fiyat | 15dk % | 30dk % | 1s % | 3s % | 6s % | 24s % |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|

## Veri kapsamı ve eksikler

Getiri sütunları hedef sürelerdir. Parantezdeki +dakika gerçek fiyat gözleminin hedefe gecikmesidir; tam 15/30/60 dakikalık mum getirisi olduğu iddia edilmez. Geçerli gözlem penceresi kaçırılırsa sonuç boş kalır.

Her ağda yalnız yeni havuz akışı sınırlı sayfalarla okunur. Önceki izlenen havuzlar kalıcı kayıttan yenilenir. Ham keşif ve sosyal gözlem tokenleri aday listesinde gösterilmez. Ücretli profil/boost olumlu sinyal sayılmaz. Aynı simge farklı kontratlarda birleştirilmez.

5 dk erken aday: üç tam kapalı5dk taban mumu ve sonraki kapalı5dk hacim mumu gerekir (yaklaşık20–25dk + veri/çalışma gecikmesi). 15 dk fiyat teyidi ve ayrıca5dk alım akışı: üç tam kapalı15dk mum gerekir (yaklaşık 45–60 dk + gecikme); erken bildirim için beklenmez. İki aşama kendi gerçek gözlem fiyatıyla ayrı ölçülür, aynı token iki bağımsız başarı sayılmaz. 15 dk teyit daha yüksek başarı veya kontrat güvenliği kanıtı değildir. Başlangıç havuz verisi tokenin tüm geçmişini kapsamaz.

Bubblemaps haritasını kullanıcı manuel inceler; API anahtarı gerekmez. Hiçbir kayıt otomatik veya manuel harita onayı almış sayılmaz. Robinhood/HyperEVM harita desteği bu sürümde doğrulanmadığından genel uygulama bağlantısı verilir; uygun ağ/harita bulunamazsa bu kontrol eksik kalır. RPC veya güvenlik kaynağının ağ desteği yoksa o ağda fiyat/havuz takibi sürer; eksik otomatik teyitle aday bildirilmez.

Büyük alıcı desteği zorunlu filtre değildir: 15/30 dk işlem örneğinde adres başına net alım en az max(500 USD, havuz likiditesi × 0.005). Deneysel 0–10 puan olasılık/servet/akıllı para kanıtı değildir. Tek adres >%50 alım hacmi veya büyük alıcıda >=%50 geri satış puanı sıfırlar; eksik/kesilmiş veri bilinmiyor. Bilinen dev/havuz/vault/yakım adresleri çıkarılır; diğer adreslerin bağlantısı doğrulanmaz.

GitHub planı yaklaşık 5 dakikada birdir; zamanlayıcı gecikebilir. Birkaç saniyede oluşan ilk pump yakalanamayabilir. Mum/istek bütçesi nedeniyle aynı anda bütün havuzlara bakıldığı iddia edilmez.

- Ethereum: POL: gecko_request_reserved_for_buy_pressure
- BNB Chain: ROCK: gecko_request_reserved_for_buy_pressure; meme: gecko_request_reserved_for_buy_pressure
- Robinhood: ROBINHOOD: gecko_request_reserved_for_buy_pressure; FLEA: gecko_request_reserved_for_buy_pressure
- Solana: SPCX80K: gecko_request_reserved_for_buy_pressure


<!-- meme-v6-pipeline -->

## V6 keşif, aşamalar ve gerçek zamanlama

Gözlem kaydı alım adayı değildir. Tüm piyasa ön koşulları geçmeden sınırlı mum OKUMA yapılır; olumlu aday için eski piyasa/güvenlik/dev/ilk-pump şartları aynen zorunludur.

Yeni havuz keşfi en çok2sayfa/ağ;15dk altı havuzlar uygun yaşa yaklaşırken öncelikli yenilenir. Bütçe dışında kalan kapsam ve veri boşluğu gizlenmez.

- hyperevm: {"refreshed": 31, "eligible": 1, "evaluated": 0, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 31, "waiting_min_age": 0, "market_pass": 1, "market_failed": {"liquidity": 30, "valuation": 30, "volume15": 30, "transaction_flow15": 30, "liquidity_to_valuation": 1}, "market_unknown": {}, "data_inspection_possible": 0, "ohlcv_read": 0, "ohlcv_attempted": 0, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 31}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 31}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793292540000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793326342595, "next_checkpoint_ms": 1793326642628, "oldest_returned_ms": 1793292540000, "valid_page": true}, "reasons": {}}
- ethereum: {"refreshed": 34, "eligible": 0, "evaluated": 2, "qualified": 0, "review": 0, "errors": ["POL: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 34, "waiting_min_age": 4, "market_pass": 0, "market_failed": {"pool_age": 4, "liquidity": 27, "valuation": 33, "liquidity_to_valuation": 25, "transaction_flow15": 33, "volume15": 27, "liquidity_withdrawal": 9}, "market_unknown": {"liquidity": 3}, "data_inspection_possible": 4, "ohlcv_read": 2, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 1, "security_checked": 0, "buy_pressure_status": {"not_checked": 34}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 34}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793325095000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793326342594, "next_checkpoint_ms": 1793326642628, "oldest_returned_ms": 1793325095000, "valid_page": true}, "reasons": {"initial_history_has_gaps": 1, "initial_pool_history_missing": 1}}
- bnb: {"refreshed": 49, "eligible": 1, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["ROCK: gecko_request_reserved_for_buy_pressure", "meme: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 49, "waiting_min_age": 8, "market_pass": 1, "market_failed": {"pool_age": 8, "valuation": 48, "volume15": 28, "transaction_flow15": 38, "liquidity": 33, "liquidity_withdrawal": 22, "liquidity_to_valuation": 10}, "market_unknown": {"liquidity": 5}, "data_inspection_possible": 6, "ohlcv_read": 1, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 4, "security_checked": 0, "buy_pressure_status": {"not_checked": 49}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 49}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793325474000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793324351000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793324351000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price": 1}}
- robinhood: {"refreshed": 52, "eligible": 3, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["ROBINHOOD: gecko_request_reserved_for_buy_pressure", "FLEA: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 52, "waiting_min_age": 18, "market_pass": 3, "market_failed": {"pool_age": 18, "valuation": 46, "volume15": 43, "transaction_flow15": 44, "liquidity": 40, "liquidity_to_valuation": 23, "liquidity_withdrawal": 4}, "market_unknown": {"liquidity": 6}, "data_inspection_possible": 3, "ohlcv_read": 1, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 1, "security_checked": 0, "buy_pressure_status": {"not_checked": 52}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 52}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793325893000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793325352000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793325352000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price": 1}}
- solana: {"refreshed": 57, "eligible": 1, "evaluated": 2, "qualified": 0, "review": 0, "errors": ["SPCX80K: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 57, "waiting_min_age": 27, "market_pass": 1, "market_failed": {"pool_age": 27, "valuation": 50, "volume15": 33, "transaction_flow15": 38, "liquidity": 27, "liquidity_to_valuation": 14, "liquidity_withdrawal": 17}, "market_unknown": {"liquidity": 27}, "data_inspection_possible": 1, "ohlcv_read": 2, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 57}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 57}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793326513000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793326558000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793326558000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price": 1, "first_rise_already_observed,already_extended_from_initial_price,post_peak_rebound_excluded": 1}}

Zamanlama: {"started_ms": 1793326642562, "finished_ms": 1793326868065, "duration_seconds": 225.503, "github_run_created_at": "2026-10-29T23:53:26Z", "worker_started_ms": "1793322741401", "github_job_started_at": "2026-10-30T01:12:06Z", "cadence": {"interval_count": 189, "p95_minutes": 5.622516666666667, "max_minutes": 6.028783333333333, "meets_7m_target": true, "full_24h_observed": false}}

İstek durumu: {"api.geckoterminal.com:ok": 19, "api.dexscreener.com:ok": 10, "gecko:reserved_for_buy_pressure": 6}; sağlayıcı429bekleme bitişi: 1793221779011

GitHub worker oturumları sınırlıdır. Çalışan oturum içinde hedef5dk; oturum başlangıcı/yenilenmesi gecikebilir. Gerçek aralıklar yukarıda;24saat tamamlanmadan kesintisiz5dk doğrulandı denmez. EskiV5 paralel taranmaz, referansları previous_v5 içinde korunur.

## Sabit miktarlı gösterge satış deneyi

100/500USD notional için ilk gözlem fiyatından hesaplanan token miktarı sabittir; alım gerçekleşmesi değildir. Aynı miktarın sonraki gösterge satış rotası sorgulanır. USDC1USD varsayılmaz. Alım maliyeti, tüm vergiler,gas veya gerçekleşme bilinmiyorsa netkâr bilinmiyor kalır. Stop-%10/hedef+%20/60dkzaman aşımı yalnız gözlenen satış kotasyonları üzerinde sabit deneydir; aradaki5dk yol ve stop-hedef sırası garanti edilmez.


Ölçüm hataları: []

## İlk taban ve alım yönlü erken hacim

MCAP:50.000–500.000USD; FDV MCAP yerine onay sayılmaz. 3tam5dk taban mumu ve sonraki kapalı5dkhacmi taban medyanının>=2katı aranır. Aynı kapalı5dk işlem örneğinde alım hacim/adet payı>=%60, alım-satım USD farkı>=250,>=8işlem,>=3netalıcı başlatıcı ve tek alıcı payı<=%60. Son300işlem pencereyi kapsamaz veya OHLCVhacmiyle uyuşmazsa bilinmiyor. Bu adresler bağımsız kişi/servet kanıtı değildir. En erken20–25dk+veri/çalışma gecikmesi. Güvenlik/dev/ilk-pump kapıları korunur.

- solana:dhf983GAxb7zTMkHhDeo2hSs1eWh1byFfm7N3Q8pump: {"tier": "watch", "first_base": {"pool": "5gFCikucbXF7xvYyUTFJtB6xcp8AsvafXCHmuGnWEzXe", "start_ms": 1793324700000, "end_ms": 1793325600000, "high": 0.07286788332908234, "low": 0.07184183998303346, "volume_median_usd": 475.9467380776317, "width_pct": 1.428197476973292, "net_change_pct": 0.8325869837604971}, "buy_pressure": {"status": "not_checked", "reasons": ["not_evaluated_this_cycle"]}, "quote_rejection": null}
- ethereum:0xc944e90c64b2c07662a292be6244bdf05cda44a7: {"tier": "watch", "first_base": {"pool": "0xdf074e89fcdfbd5ddfa3030394e9071dcc765fdf8c5e61495b799a34a6781e6c", "start_ms": 1793324100000, "end_ms": 1793325000000, "high": 0.0191176338254855, "low": 0.0184920261741979, "volume_median_usd": 3416.789307771583, "width_pct": 3.3831211647348702, "net_change_pct": 1.5251430570187186}, "buy_pressure": {"status": "not_checked", "reasons": ["not_evaluated_this_cycle"]}, "quote_rejection": null}
