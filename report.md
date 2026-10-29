# Coin Tarama Meme — V6

Son çalışma: 29.10.2026 18:41 Türkiye saati.

**Deneysel DEX izleme. Tüm yeni tokenleri kapsamaz ve yükseliş garantisi vermez.**

Kapsam: Solana, Ethereum, BNB Chain, Robinhood (Pons dahil), HyperEVM. Pons ayrı bir ağ değildir.

**Hedef: ilk yükseliş öncesi oluşum/birikim.** Yeni aday yalnız birikim evresinde alınır; ilk kırılım ancak daha önce bildirilen birikimin devamı olarak izlenir. Trend listesi aday kaynağı olarak kullanılmaz. **Cüzdan haritası manuel kontrol bekler.** Kritik kontrat/geliştirici verisi eksik tokenler bildirilmez.

Geçmişin tamamındaki fitiller ve açık mum dahil gözlenen dipten tepeye yükseliş %25 üzerindeyse, ilk fiyatın %10 üzerine uzamışsa veya tepeden %15 üzeri düşmüşse elenir. Bu eşikler deneysel tercihlerdir. Havuz başlangıcı, ara mumlar veya güncel mum yoksa ilk oluşum teyitsizdir. Eski pump sonrası yataylaşma yeni aday sayılmaz.

GMGN kullanılmaz. Solana: RugCheck + GoPlus Solana; desteklenen EVM ağları: GoPlus. GMGN’nin tüm sniper/bundler etiketleri ve eksiksiz geliştirici geçmişi sağlanmaz. Teknik risk ön elemesi tokenin resmî/orijinal proje kontratı olduğunu kanıtlamaz.

Yeni havuz yaşı tokenin yaratılma yaşı değildir. Market cap sağlayıcı bildirimi olarak, FDV ise açıkça ayrı değer türü olarak gösterilir. Geliştirici teyidi yalnız belirtilen 45 dakikalık işlem penceresindeki raporlanan adrese aittir; ömür boyu hiç satış yapmadığı veya başka cüzdan kullanmadığı anlamına gelmez.

| Ağ | Güncellenen token | Piyasa ön elemesi | Mum incelenen | Ön eleme / manuel harita bekliyor | İnceleme | Erişim/veri hatası |
|---|---:|---:|---:|---:|---:|---:|
| Ethereum | 33 | 0 | 0 | 0 | 0 | 0 |
| HyperEVM (HYPE) | 31 | 0 | 0 | 0 | 0 | 0 |
| Solana | 64 | 3 | 0 | 0 | 0 | 0 |
| BNB Chain | 59 | 0 | 1 | 0 | 0 | 0 |
| Robinhood | 62 | 4 | 1 | 0 | 0 | 0 |

Bu çalışmada aday olmayan mum incelemeleri (token listesi değildir):
- 1: Güncel mumun yüksek/düşük verisi eksik
- 1: Önceden yükseliş / uzun fitil görülmüş; Başlangıç fiyatından fazla uzaklaşmış; Tepeden düşüş sonrası yapı elenmiş

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

- ethereum: {"refreshed": 33, "eligible": 0, "evaluated": 0, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 33, "waiting_min_age": 4, "market_pass": 0, "market_failed": {"pool_age": 4, "liquidity": 32, "valuation": 30, "volume15": 31, "transaction_flow15": 31, "liquidity_to_valuation": 17, "liquidity_withdrawal": 7}, "market_unknown": {}, "data_inspection_possible": 0, "ohlcv_read": 0, "ohlcv_attempted": 0, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 33}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 33}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793283383000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793288026849, "next_checkpoint_ms": 1793288325856, "oldest_returned_ms": 1793283383000, "valid_page": true}, "reasons": {}}
- hyperevm: {"refreshed": 31, "eligible": 0, "evaluated": 0, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 31, "waiting_min_age": 1, "market_pass": 0, "market_failed": {"pool_age": 1, "liquidity": 30, "valuation": 31, "volume15": 28, "transaction_flow15": 30, "liquidity_withdrawal": 1, "liquidity_to_valuation": 1}, "market_unknown": {}, "data_inspection_possible": 0, "ohlcv_read": 0, "ohlcv_attempted": 0, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 31}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 31}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793278980000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793288026850, "next_checkpoint_ms": 1793288325857, "oldest_returned_ms": 1793278980000, "valid_page": true}, "reasons": {}}
- solana: {"refreshed": 64, "eligible": 3, "evaluated": 0, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 64, "waiting_min_age": 34, "market_pass": 3, "market_failed": {"pool_age": 34, "liquidity": 57, "valuation": 58, "volume15": 31, "transaction_flow15": 51, "liquidity_to_valuation": 4, "liquidity_withdrawal": 20}, "market_unknown": {"liquidity": 2}, "data_inspection_possible": 0, "ohlcv_read": 0, "ohlcv_attempted": 0, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 64}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 64}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793288256000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793288291000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793288291000, "valid_page": true}, "reasons": {}}
- bnb: {"refreshed": 59, "eligible": 0, "evaluated": 1, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 59, "waiting_min_age": 21, "market_pass": 0, "market_failed": {"pool_age": 22, "valuation": 54, "volume15": 43, "transaction_flow15": 49, "liquidity": 47, "liquidity_to_valuation": 19, "liquidity_withdrawal": 15}, "market_unknown": {"valuation": 1}, "data_inspection_possible": 2, "ohlcv_read": 1, "ohlcv_attempted": 1, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 59}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 59}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793287646000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793286672000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793286672000, "valid_page": true}, "reasons": {"current_interval_history_missing": 1}}
- robinhood: {"refreshed": 62, "eligible": 4, "evaluated": 1, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 62, "waiting_min_age": 32, "market_pass": 4, "market_failed": {"pool_age": 32, "liquidity": 45, "valuation": 50, "transaction_flow15": 49, "volume15": 26, "liquidity_to_valuation": 14, "liquidity_withdrawal": 10}, "market_unknown": {"liquidity": 3}, "data_inspection_possible": 0, "ohlcv_read": 1, "ohlcv_attempted": 1, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 62}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 62}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793288018000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793287884000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793287884000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price,post_peak_rebound_excluded": 1}}

Zamanlama: {"started_ms": 1793288325806, "finished_ms": 1793288501219, "duration_seconds": 175.413, "github_run_created_at": "2026-10-29T13:21:10Z", "worker_started_ms": "1793283524519", "github_job_started_at": "2026-10-29T14:18:28Z", "cadence": {"interval_count": 60, "p95_minutes": 5.41685, "max_minutes": 5.627933333333333, "meets_7m_target": true, "full_24h_observed": false}}

İstek durumu: {"api.geckoterminal.com:ok": 15, "api.dexscreener.com:ok": 18}; sağlayıcı429bekleme bitişi: 1793221779011

GitHub worker oturumları sınırlıdır. Çalışan oturum içinde hedef5dk; oturum başlangıcı/yenilenmesi gecikebilir. Gerçek aralıklar yukarıda;24saat tamamlanmadan kesintisiz5dk doğrulandı denmez. EskiV5 paralel taranmaz, referansları previous_v5 içinde korunur.

## Sabit miktarlı gösterge satış deneyi

100/500USD notional için ilk gözlem fiyatından hesaplanan token miktarı sabittir; alım gerçekleşmesi değildir. Aynı miktarın sonraki gösterge satış rotası sorgulanır. USDC1USD varsayılmaz. Alım maliyeti, tüm vergiler,gas veya gerçekleşme bilinmiyorsa netkâr bilinmiyor kalır. Stop-%10/hedef+%20/60dkzaman aşımı yalnız gözlenen satış kotasyonları üzerinde sabit deneydir; aradaki5dk yol ve stop-hedef sırası garanti edilmez.


Ölçüm hataları: []

## İlk taban ve alım yönlü erken hacim

MCAP:50.000–500.000USD; FDV MCAP yerine onay sayılmaz. 3tam5dk taban mumu ve sonraki kapalı5dkhacmi taban medyanının>=2katı aranır. Aynı kapalı5dk işlem örneğinde alım hacim/adet payı>=%60, alım-satım USD farkı>=250,>=8işlem,>=3netalıcı başlatıcı ve tek alıcı payı<=%60. Son300işlem pencereyi kapsamaz veya OHLCVhacmiyle uyuşmazsa bilinmiyor. Bu adresler bağımsız kişi/servet kanıtı değildir. En erken20–25dk+veri/çalışma gecikmesi. Güvenlik/dev/ilk-pump kapıları korunur.

- solana:6DgbAN9fq9nTPkQgE2bFPJ9Yy9DzaFJR1sfGo8nTjdub: {"tier": "watch", "first_base": {"pool": "AWGkVaki2djd2QitX8P3ScKjnfMmVseEo9ARGuKfSKuA", "start_ms": 1793286300000, "end_ms": 1793287200000, "high": 9.541851547138032e-05, "low": 8.766486790092792e-05, "volume_median_usd": 271.30327030557294, "width_pct": 8.844646385841791, "net_change_pct": 8.803660258700718}, "buy_pressure": {"status": "not_checked", "reasons": ["not_evaluated_this_cycle"]}, "quote_rejection": null}
- bnb:0x7e88513f60bcd6c3011205f2c1133ef417007777: {"tier": "watch", "first_base": {"pool": "0xd555a47a6c08bb5ead543b713da972f730f00ee6", "start_ms": 1793286600000, "end_ms": 1793287500000, "high": 4.41879907873798e-05, "low": 3.80168166647304e-05, "volume_median_usd": 700.7819419574744, "width_pct": 16.232748199495163, "net_change_pct": 5.5501237412292515}, "buy_pressure": {"status": "not_checked", "reasons": ["not_evaluated_this_cycle"]}, "quote_rejection": null}
