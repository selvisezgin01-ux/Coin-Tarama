# Coin Tarama Meme — V6

Son çalışma: 29.10.2026 21:34 Türkiye saati.

**Deneysel DEX izleme. Tüm yeni tokenleri kapsamaz ve yükseliş garantisi vermez.**

Kapsam: Solana, Ethereum, BNB Chain, Robinhood (Pons dahil), HyperEVM. Pons ayrı bir ağ değildir.

**Hedef: ilk yükseliş öncesi oluşum/birikim.** Yeni aday yalnız birikim evresinde alınır; ilk kırılım ancak daha önce bildirilen birikimin devamı olarak izlenir. Trend listesi aday kaynağı olarak kullanılmaz. **Cüzdan haritası manuel kontrol bekler.** Kritik kontrat/geliştirici verisi eksik tokenler bildirilmez.

Geçmişin tamamındaki fitiller ve açık mum dahil gözlenen dipten tepeye yükseliş %25 üzerindeyse, ilk fiyatın %10 üzerine uzamışsa veya tepeden %15 üzeri düşmüşse elenir. Bu eşikler deneysel tercihlerdir. Havuz başlangıcı, ara mumlar veya güncel mum yoksa ilk oluşum teyitsizdir. Eski pump sonrası yataylaşma yeni aday sayılmaz.

GMGN kullanılmaz. Solana: RugCheck + GoPlus Solana; desteklenen EVM ağları: GoPlus. GMGN’nin tüm sniper/bundler etiketleri ve eksiksiz geliştirici geçmişi sağlanmaz. Teknik risk ön elemesi tokenin resmî/orijinal proje kontratı olduğunu kanıtlamaz.

Yeni havuz yaşı tokenin yaratılma yaşı değildir. Market cap sağlayıcı bildirimi olarak, FDV ise açıkça ayrı değer türü olarak gösterilir. Geliştirici teyidi yalnız belirtilen 45 dakikalık işlem penceresindeki raporlanan adrese aittir; ömür boyu hiç satış yapmadığı veya başka cüzdan kullanmadığı anlamına gelmez.

| Ağ | Güncellenen token | Piyasa ön elemesi | Mum incelenen | Ön eleme / manuel harita bekliyor | İnceleme | Erişim/veri hatası |
|---|---:|---:|---:|---:|---:|---:|
| HyperEVM (HYPE) | 35 | 0 | 0 | 0 | 0 | 0 |
| Solana | 70 | 0 | 0 | 0 | 0 | 0 |
| Ethereum | 31 | 1 | 1 | 0 | 0 | 0 |
| Robinhood | 67 | 2 | 0 | 0 | 0 | 0 |
| BNB Chain | 60 | 0 | 2 | 0 | 0 | 0 |

Bu çalışmada aday olmayan mum incelemeleri (token listesi değildir):
- 2: Önceden yükseliş / uzun fitil görülmüş; Başlangıç fiyatından fazla uzaklaşmış; Tepeden düşüş sonrası yapı elenmiş
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



<!-- meme-v6-pipeline -->

## V6 keşif, aşamalar ve gerçek zamanlama

Gözlem kaydı alım adayı değildir. Tüm piyasa ön koşulları geçmeden sınırlı mum OKUMA yapılır; olumlu aday için eski piyasa/güvenlik/dev/ilk-pump şartları aynen zorunludur.

Yeni havuz keşfi en çok2sayfa/ağ;15dk altı havuzlar uygun yaşa yaklaşırken öncelikli yenilenir. Bütçe dışında kalan kapsam ve veri boşluğu gizlenmez.

- hyperevm: {"refreshed": 35, "eligible": 0, "evaluated": 0, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 35, "waiting_min_age": 0, "market_pass": 0, "market_failed": {"liquidity": 35, "valuation": 35, "volume15": 34, "transaction_flow15": 34, "liquidity_to_valuation": 3, "liquidity_withdrawal": 1}, "market_unknown": {}, "data_inspection_possible": 0, "ohlcv_read": 0, "ohlcv_attempted": 0, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 35}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 35}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793286840000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793298362641, "next_checkpoint_ms": 1793298662624, "oldest_returned_ms": 1793286840000, "valid_page": true}, "reasons": {}}
- solana: {"refreshed": 70, "eligible": 0, "evaluated": 0, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 70, "waiting_min_age": 40, "market_pass": 0, "market_failed": {"pool_age": 40, "liquidity": 65, "valuation": 70, "volume15": 48, "transaction_flow15": 63, "liquidity_to_valuation": 5, "liquidity_withdrawal": 17}, "market_unknown": {}, "data_inspection_possible": 0, "ohlcv_read": 0, "ohlcv_attempted": 0, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 70}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 70}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793298536000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793298573000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793298573000, "valid_page": true}, "reasons": {}}
- ethereum: {"refreshed": 31, "eligible": 1, "evaluated": 1, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 31, "waiting_min_age": 2, "market_pass": 1, "market_failed": {"pool_age": 2, "valuation": 30, "liquidity_to_valuation": 13, "volume15": 29, "transaction_flow15": 29, "liquidity": 27, "liquidity_withdrawal": 1}, "market_unknown": {"liquidity": 1}, "data_inspection_possible": 1, "ohlcv_read": 1, "ohlcv_attempted": 1, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 31}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 31}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793291639000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793298362641, "next_checkpoint_ms": 1793298662624, "oldest_returned_ms": 1793291639000, "valid_page": true}, "reasons": {"initial_pool_history_missing": 1}}
- robinhood: {"refreshed": 67, "eligible": 2, "evaluated": 0, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 67, "waiting_min_age": 37, "market_pass": 2, "market_failed": {"pool_age": 37, "liquidity": 52, "valuation": 56, "volume15": 43, "transaction_flow15": 58, "liquidity_to_valuation": 15, "liquidity_withdrawal": 6}, "market_unknown": {"liquidity": 3}, "data_inspection_possible": 0, "ohlcv_read": 0, "ohlcv_attempted": 0, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 67}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 67}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793298206000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793297935000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793297935000, "valid_page": true}, "reasons": {}}
- bnb: {"refreshed": 60, "eligible": 0, "evaluated": 2, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 60, "waiting_min_age": 30, "market_pass": 0, "market_failed": {"pool_age": 30, "liquidity": 53, "valuation": 56, "liquidity_to_valuation": 37, "volume15": 45, "transaction_flow15": 53, "liquidity_withdrawal": 10}, "market_unknown": {}, "data_inspection_possible": 0, "ohlcv_read": 2, "ohlcv_attempted": 2, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 60}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 60}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793298249000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793298091000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793298091000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price,post_peak_rebound_excluded": 2}}

Zamanlama: {"started_ms": 1793298662579, "finished_ms": 1793298850483, "duration_seconds": 187.904, "github_run_created_at": "2026-10-29T17:11:24Z", "worker_started_ms": "1793296561410", "github_job_started_at": "2026-10-29T17:55:48Z", "cadence": {"interval_count": 95, "p95_minutes": 5.626, "max_minutes": 5.83525, "meets_7m_target": true, "full_24h_observed": false}}

İstek durumu: {"api.geckoterminal.com:ok": 16, "api.dexscreener.com:ok": 12}; sağlayıcı429bekleme bitişi: 1793221779011

GitHub worker oturumları sınırlıdır. Çalışan oturum içinde hedef5dk; oturum başlangıcı/yenilenmesi gecikebilir. Gerçek aralıklar yukarıda;24saat tamamlanmadan kesintisiz5dk doğrulandı denmez. EskiV5 paralel taranmaz, referansları previous_v5 içinde korunur.

## Sabit miktarlı gösterge satış deneyi

100/500USD notional için ilk gözlem fiyatından hesaplanan token miktarı sabittir; alım gerçekleşmesi değildir. Aynı miktarın sonraki gösterge satış rotası sorgulanır. USDC1USD varsayılmaz. Alım maliyeti, tüm vergiler,gas veya gerçekleşme bilinmiyorsa netkâr bilinmiyor kalır. Stop-%10/hedef+%20/60dkzaman aşımı yalnız gözlenen satış kotasyonları üzerinde sabit deneydir; aradaki5dk yol ve stop-hedef sırası garanti edilmez.


Ölçüm hataları: []

## İlk taban ve alım yönlü erken hacim

MCAP:50.000–500.000USD; FDV MCAP yerine onay sayılmaz. 3tam5dk taban mumu ve sonraki kapalı5dkhacmi taban medyanının>=2katı aranır. Aynı kapalı5dk işlem örneğinde alım hacim/adet payı>=%60, alım-satım USD farkı>=250,>=8işlem,>=3netalıcı başlatıcı ve tek alıcı payı<=%60. Son300işlem pencereyi kapsamaz veya OHLCVhacmiyle uyuşmazsa bilinmiyor. Bu adresler bağımsız kişi/servet kanıtı değildir. En erken20–25dk+veri/çalışma gecikmesi. Güvenlik/dev/ilk-pump kapıları korunur.

