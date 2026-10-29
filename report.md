# Coin Tarama Meme — V6

Son çalışma: 30.10.2026 02:46 Türkiye saati.

**Deneysel DEX izleme. Tüm yeni tokenleri kapsamaz ve yükseliş garantisi vermez.**

Kapsam: Solana, Ethereum, BNB Chain, Robinhood (Pons dahil), HyperEVM. Pons ayrı bir ağ değildir.

**Hedef: ilk yükseliş öncesi oluşum/birikim.** Yeni aday yalnız birikim evresinde alınır; ilk kırılım ancak daha önce bildirilen birikimin devamı olarak izlenir. Trend listesi aday kaynağı olarak kullanılmaz. **Cüzdan haritası manuel kontrol bekler.** Kritik kontrat/geliştirici verisi eksik tokenler bildirilmez.

Geçmişin tamamındaki fitiller ve açık mum dahil gözlenen dipten tepeye yükseliş %25 üzerindeyse, ilk fiyatın %10 üzerine uzamışsa veya tepeden %15 üzeri düşmüşse elenir. Bu eşikler deneysel tercihlerdir. Havuz başlangıcı, ara mumlar veya güncel mum yoksa ilk oluşum teyitsizdir. Eski pump sonrası yataylaşma yeni aday sayılmaz.

GMGN kullanılmaz. Solana: RugCheck + GoPlus Solana; desteklenen EVM ağları: GoPlus. GMGN’nin tüm sniper/bundler etiketleri ve eksiksiz geliştirici geçmişi sağlanmaz. Teknik risk ön elemesi tokenin resmî/orijinal proje kontratı olduğunu kanıtlamaz.

Yeni havuz yaşı tokenin yaratılma yaşı değildir. Market cap sağlayıcı bildirimi olarak, FDV ise açıkça ayrı değer türü olarak gösterilir. Geliştirici teyidi yalnız belirtilen 45 dakikalık işlem penceresindeki raporlanan adrese aittir; ömür boyu hiç satış yapmadığı veya başka cüzdan kullanmadığı anlamına gelmez.

| Ağ | Güncellenen token | Piyasa ön elemesi | Mum incelenen | Ön eleme / manuel harita bekliyor | İnceleme | Erişim/veri hatası |
|---|---:|---:|---:|---:|---:|---:|
| HyperEVM (HYPE) | 42 | 0 | 0 | 0 | 0 | 0 |
| Solana | 70 | 0 | 1 | 0 | 0 | 0 |
| BNB Chain | 49 | 0 | 1 | 0 | 0 | 2 |
| Robinhood | 60 | 2 | 1 | 0 | 0 | 1 |
| Ethereum | 30 | 0 | 3 | 0 | 0 | 0 |

Bu çalışmada aday olmayan mum incelemeleri (token listesi değildir):
- 1: Başlangıç fiyatından fazla uzaklaşmış
- 3: Daha eski havuz geçmişi kapsam dışı
- 1: Önceden yükseliş / uzun fitil görülmüş; Başlangıç fiyatından fazla uzaklaşmış; Tepeden düşüş sonrası yapı elenmiş
- 1: Önceden yükseliş / uzun fitil görülmüş; Tepeden düşüş sonrası yapı elenmiş

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

- BNB Chain: beans: gecko_request_reserved_for_buy_pressure; 1029: gecko_request_reserved_for_buy_pressure
- Robinhood: R: gecko_request_reserved_for_buy_pressure






<!-- meme-v6-pipeline -->

## V6 keşif, aşamalar ve gerçek zamanlama

Gözlem kaydı alım adayı değildir. Tüm piyasa ön koşulları geçmeden sınırlı mum OKUMA yapılır; olumlu aday için eski piyasa/güvenlik/dev/ilk-pump şartları aynen zorunludur.

Yeni havuz keşfi en çok2sayfa/ağ;15dk altı havuzlar uygun yaşa yaklaşırken öncelikli yenilenir. Bütçe dışında kalan kapsam ve veri boşluğu gizlenmez.

- hyperevm: {"refreshed": 42, "eligible": 0, "evaluated": 0, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 42, "waiting_min_age": 0, "market_pass": 0, "market_failed": {"liquidity": 41, "valuation": 41, "volume15": 41, "transaction_flow15": 42, "liquidity_withdrawal": 1, "liquidity_to_valuation": 3}, "market_unknown": {}, "data_inspection_possible": 0, "ohlcv_read": 0, "ohlcv_attempted": 0, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 42}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 42}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793292540000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793317089983, "next_checkpoint_ms": 1793317389958, "oldest_returned_ms": 1793292540000, "valid_page": true}, "reasons": {}}
- solana: {"refreshed": 70, "eligible": 0, "evaluated": 1, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 70, "waiting_min_age": 40, "market_pass": 0, "market_failed": {"pool_age": 40, "valuation": 64, "volume15": 30, "transaction_flow15": 51, "liquidity": 58, "liquidity_to_valuation": 15, "liquidity_withdrawal": 20}, "market_unknown": {"liquidity": 5, "valuation": 1}, "data_inspection_possible": 0, "ohlcv_read": 1, "ohlcv_attempted": 1, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 70}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 70}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793317259000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793317324000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793317324000, "valid_page": true}, "reasons": {"already_extended_from_initial_price": 1}}
- bnb: {"refreshed": 49, "eligible": 0, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["beans: gecko_request_reserved_for_buy_pressure", "1029: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 49, "waiting_min_age": 17, "market_pass": 0, "market_failed": {"pool_age": 18, "liquidity": 35, "valuation": 44, "transaction_flow15": 41, "liquidity_to_valuation": 16, "volume15": 32, "liquidity_withdrawal": 9}, "market_unknown": {"liquidity": 1, "valuation": 1}, "data_inspection_possible": 5, "ohlcv_read": 1, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 2, "security_checked": 0, "buy_pressure_status": {"not_checked": 49}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 49}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793316653000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793316321000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793316321000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price,post_peak_rebound_excluded": 1}}
- robinhood: {"refreshed": 60, "eligible": 2, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["R: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 60, "waiting_min_age": 22, "market_pass": 2, "market_failed": {"pool_age": 24, "valuation": 50, "liquidity": 47, "liquidity_to_valuation": 25, "volume15": 42, "transaction_flow15": 30, "liquidity_withdrawal": 6}, "market_unknown": {"liquidity": 3}, "data_inspection_possible": 1, "ohlcv_read": 1, "ohlcv_attempted": 2, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 60}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 60}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793316802000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793316468000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793316468000, "valid_page": true}, "reasons": {"first_rise_already_observed,post_peak_rebound_excluded": 1}}
- ethereum: {"refreshed": 30, "eligible": 0, "evaluated": 3, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 30, "waiting_min_age": 0, "market_pass": 0, "market_failed": {"valuation": 29, "liquidity_to_valuation": 20, "transaction_flow15": 29, "liquidity_withdrawal": 7, "liquidity": 26, "volume15": 28}, "market_unknown": {"liquidity": 1}, "data_inspection_possible": 3, "ohlcv_read": 3, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 30}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 30}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793315039000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793317089983, "next_checkpoint_ms": 1793317389957, "oldest_returned_ms": 1793315039000, "valid_page": true}, "reasons": {"earlier_pool_history_not_covered": 3}}

Zamanlama: {"started_ms": 1793317389903, "finished_ms": 1793317615242, "duration_seconds": 225.339, "github_run_created_at": "2026-10-29T22:57:19Z", "worker_started_ms": "1793316188742", "github_job_started_at": "2026-10-29T23:22:55Z", "cadence": {"interval_count": 158, "p95_minutes": 5.626, "max_minutes": 6.028783333333333, "meets_7m_target": true, "full_24h_observed": false}}

İstek durumu: {"api.geckoterminal.com:ok": 19, "api.dexscreener.com:ok": 16, "gecko:reserved_for_buy_pressure": 3}; sağlayıcı429bekleme bitişi: 1793221779011

GitHub worker oturumları sınırlıdır. Çalışan oturum içinde hedef5dk; oturum başlangıcı/yenilenmesi gecikebilir. Gerçek aralıklar yukarıda;24saat tamamlanmadan kesintisiz5dk doğrulandı denmez. EskiV5 paralel taranmaz, referansları previous_v5 içinde korunur.

## Sabit miktarlı gösterge satış deneyi

100/500USD notional için ilk gözlem fiyatından hesaplanan token miktarı sabittir; alım gerçekleşmesi değildir. Aynı miktarın sonraki gösterge satış rotası sorgulanır. USDC1USD varsayılmaz. Alım maliyeti, tüm vergiler,gas veya gerçekleşme bilinmiyorsa netkâr bilinmiyor kalır. Stop-%10/hedef+%20/60dkzaman aşımı yalnız gözlenen satış kotasyonları üzerinde sabit deneydir; aradaki5dk yol ve stop-hedef sırası garanti edilmez.


Ölçüm hataları: []

## İlk taban ve alım yönlü erken hacim

MCAP:50.000–500.000USD; FDV MCAP yerine onay sayılmaz. 3tam5dk taban mumu ve sonraki kapalı5dkhacmi taban medyanının>=2katı aranır. Aynı kapalı5dk işlem örneğinde alım hacim/adet payı>=%60, alım-satım USD farkı>=250,>=8işlem,>=3netalıcı başlatıcı ve tek alıcı payı<=%60. Son300işlem pencereyi kapsamaz veya OHLCVhacmiyle uyuşmazsa bilinmiyor. Bu adresler bağımsız kişi/servet kanıtı değildir. En erken20–25dk+veri/çalışma gecikmesi. Güvenlik/dev/ilk-pump kapıları korunur.

