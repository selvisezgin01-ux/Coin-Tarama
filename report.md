# Coin Tarama Meme — V5

Son çalışma: 28.10.2026 21:55 Türkiye saati.

**Deneysel DEX izleme. Tüm yeni tokenleri kapsamaz ve yükseliş garantisi vermez.**

Kapsam: Solana, Ethereum, BNB Chain, Robinhood (Pons dahil), HyperEVM. Pons ayrı bir ağ değildir.

**Hedef: ilk yükseliş öncesi oluşum/birikim.** Yeni aday yalnız birikim evresinde alınır; ilk kırılım ancak daha önce bildirilen birikimin devamı olarak izlenir. Trend listesi aday kaynağı olarak kullanılmaz. **Cüzdan haritası manuel kontrol bekler.** Kritik kontrat/geliştirici verisi eksik tokenler bildirilmez.

Geçmişin tamamındaki fitiller ve açık mum dahil gözlenen dipten tepeye yükseliş %25 üzerindeyse, ilk fiyatın %10 üzerine uzamışsa veya tepeden %15 üzeri düşmüşse elenir. Bu eşikler deneysel tercihlerdir. Havuz başlangıcı, ara mumlar veya güncel mum yoksa ilk oluşum teyitsizdir. Eski pump sonrası yataylaşma yeni aday sayılmaz.

GMGN kullanılmaz. Solana: RugCheck + GoPlus Solana; desteklenen EVM ağları: GoPlus. GMGN’nin tüm sniper/bundler etiketleri ve eksiksiz geliştirici geçmişi sağlanmaz. Teknik risk ön elemesi tokenin resmî/orijinal proje kontratı olduğunu kanıtlamaz.

Yeni havuz yaşı tokenin yaratılma yaşı değildir. Market cap sağlayıcı bildirimi olarak, FDV ise açıkça ayrı değer türü olarak gösterilir. Geliştirici teyidi yalnız belirtilen 45 dakikalık işlem penceresindeki raporlanan adrese aittir; ömür boyu hiç satış yapmadığı veya başka cüzdan kullanmadığı anlamına gelmez.

| Ağ | Güncellenen token | Piyasa ön elemesi | Mum incelenen | Ön eleme / manuel harita bekliyor | İnceleme | Erişim/veri hatası |
|---|---:|---:|---:|---:|---:|---:|
| Solana | 66 | 0 | 0 | 0 | 0 | 0 |
| BNB Chain | 67 | 3 | 1 | 0 | 0 | 1 |
| Robinhood | 64 | 1 | 1 | 0 | 0 | 1 |
| HyperEVM (HYPE) | 18 | 0 | 2 | 0 | 0 | 0 |
| Ethereum | 39 | 1 | 2 | 0 | 0 | 1 |

Bu çalışmada aday olmayan mum incelemeleri (token listesi değildir):
- 2: Önceden yükseliş / uzun fitil görülmüş; Başlangıç fiyatından fazla uzaklaşmış; Tepeden düşüş sonrası yapı elenmiş
- 3: Başlangıç geçmişinde veri boşluğu var
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

5 dk erken aday: havuz açıldıktan sonraki üç tam kapalı 5 dk mum gerekir (yaklaşık 15–20 dk + veri/çalışma gecikmesi). 15 dk teknik teyit: üç tam kapalı 15 dk mum gerekir (yaklaşık 45–60 dk + gecikme); erken bildirim için beklenmez. İki aşama kendi gerçek gözlem fiyatıyla ayrı ölçülür, aynı token iki bağımsız başarı sayılmaz. 15 dk teyit daha yüksek başarı veya kontrat güvenliği kanıtı değildir. Başlangıç havuz verisi tokenin tüm geçmişini kapsamaz.

Bubblemaps haritasını kullanıcı manuel inceler; API anahtarı gerekmez. Hiçbir kayıt otomatik veya manuel harita onayı almış sayılmaz. Robinhood/HyperEVM harita desteği bu sürümde doğrulanmadığından genel uygulama bağlantısı verilir; uygun ağ/harita bulunamazsa bu kontrol eksik kalır. RPC veya güvenlik kaynağının ağ desteği yoksa o ağda fiyat/havuz takibi sürer; eksik otomatik teyitle aday bildirilmez.

Büyük alıcı desteği zorunlu filtre değildir: 15/30 dk işlem örneğinde adres başına net alım en az max(500 USD, havuz likiditesi × 0.005). Deneysel 0–10 puan olasılık/servet/akıllı para kanıtı değildir. Tek adres >%50 alım hacmi veya büyük alıcıda >=%50 geri satış puanı sıfırlar; eksik/kesilmiş veri bilinmiyor. Bilinen dev/havuz/vault/yakım adresleri çıkarılır; diğer adreslerin bağlantısı doğrulanmaz.

GitHub planı yaklaşık 5 dakikada birdir; zamanlayıcı gecikebilir. Birkaç saniyede oluşan ilk pump yakalanamayabilir. Mum/istek bütçesi nedeniyle aynı anda bütün havuzlara bakıldığı iddia edilmez.

- BNB Chain: Facebook: gecko_request_budget_deferred
- Robinhood: FYSTACK: gecko_request_budget_deferred
- Ethereum: GOB: gecko_request_budget_deferred






<!-- meme-v5-pipeline -->

## V5 keşif, aşamalar ve gerçek zamanlama

Gözlem kaydı alım adayı değildir. Tüm piyasa ön koşulları geçmeden sınırlı mum OKUMA yapılır; olumlu aday için eski piyasa/güvenlik/dev/ilk-pump şartları aynen zorunludur.

Yeni havuz keşfi en çok2sayfa/ağ;15dk altı havuzlar uygun yaşa yaklaşırken öncelikli yenilenir. Bütçe dışında kalan kapsam ve veri boşluğu gizlenmez.

- solana: {"refreshed": 66, "eligible": 0, "evaluated": 0, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 66, "waiting_min_age": 36, "market_pass": 0, "market_failed": {"pool_age": 36, "valuation": 55, "liquidity": 60, "volume15": 26, "transaction_flow15": 46, "liquidity_to_valuation": 12, "liquidity_withdrawal": 11}, "market_unknown": {"liquidity": 1}, "data_inspection_possible": 0, "ohlcv_read": 0, "ohlcv_attempted": 0, "ohlcv_budget_waiting": 0, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793213413000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793213439000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793213439000, "valid_page": true}, "reasons": {}}
- bnb: {"refreshed": 67, "eligible": 3, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["Facebook: gecko_request_budget_deferred"], "funnel": {"records": 67, "waiting_min_age": 36, "market_pass": 3, "market_failed": {"pool_age": 36, "liquidity": 57, "valuation": 58, "volume15": 46, "transaction_flow15": 53, "liquidity_to_valuation": 13, "liquidity_withdrawal": 9}, "market_unknown": {}, "data_inspection_possible": 1, "ohlcv_read": 1, "ohlcv_attempted": 2, "ohlcv_budget_waiting": 0, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793213088000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793212737000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793212737000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price,post_peak_rebound_excluded": 1}}
- robinhood: {"refreshed": 64, "eligible": 1, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["FYSTACK: gecko_request_budget_deferred"], "funnel": {"records": 64, "waiting_min_age": 31, "market_pass": 1, "market_failed": {"pool_age": 32, "volume15": 46, "transaction_flow15": 52, "liquidity": 54, "valuation": 53, "liquidity_to_valuation": 7, "liquidity_withdrawal": 3}, "market_unknown": {}, "data_inspection_possible": 1, "ohlcv_read": 1, "ohlcv_attempted": 2, "ohlcv_budget_waiting": 0, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793213058000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793212684000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793212684000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price,post_peak_rebound_excluded": 1}}
- hyperevm: {"refreshed": 18, "eligible": 0, "evaluated": 2, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 18, "waiting_min_age": 0, "market_pass": 0, "market_failed": {"liquidity": 16, "valuation": 16, "volume15": 18, "transaction_flow15": 18, "liquidity_to_valuation": 1, "pool_age": 5}, "market_unknown": {}, "data_inspection_possible": 2, "ohlcv_read": 2, "ohlcv_attempted": 2, "ohlcv_budget_waiting": 0, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793098680000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793213219859, "next_checkpoint_ms": 1793213520201, "oldest_returned_ms": 1793098680000, "valid_page": true}, "reasons": {"initial_history_has_gaps": 1, "initial_pool_history_missing": 1}}
- ethereum: {"refreshed": 39, "eligible": 1, "evaluated": 2, "qualified": 0, "review": 0, "errors": ["GOB: gecko_request_budget_deferred"], "funnel": {"records": 39, "waiting_min_age": 0, "market_pass": 1, "market_failed": {"liquidity": 29, "valuation": 29, "volume15": 34, "transaction_flow15": 36, "liquidity_to_valuation": 14, "liquidity_withdrawal": 2}, "market_unknown": {}, "data_inspection_possible": 7, "ohlcv_read": 2, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 4, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793209859000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793206907000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793206907000, "valid_page": true}, "reasons": {"initial_history_has_gaps": 2}}

Zamanlama: {"started_ms": 1793213520177, "finished_ms": 1793213758177, "duration_seconds": 238.0, "github_run_created_at": "2026-10-28T18:37:34Z", "worker_started_ms": "1793212917794", "github_job_started_at": "2026-10-28T18:41:43Z", "cadence": {"interval_count": 4, "p95_minutes": 5.0086, "max_minutes": 5.0086, "meets_7m_target": true, "full_24h_observed": false}}

İstek durumu: {"api.geckoterminal.com:ok": 20, "api.dexscreener.com:ok": 18, "gecko:budget_deferred": 3}; sağlayıcı429bekleme bitişi: None

GitHub worker oturumları sınırlıdır. Çalışan oturum içinde hedef5dk; oturum başlangıcı/yenilenmesi gecikebilir. Gerçek aralıklar yukarıda;24saat tamamlanmadan kesintisiz5dk doğrulandı denmez. EskiV4 paralel taranmaz, referansları previous_v4 içinde korunur.

## Sabit miktarlı gösterge satış deneyi

100/500USD notional için ilk gözlem fiyatından hesaplanan token miktarı sabittir; alım gerçekleşmesi değildir. Aynı miktarın sonraki gösterge satış rotası sorgulanır. USDC1USD varsayılmaz. Alım maliyeti, tüm vergiler,gas veya gerçekleşme bilinmiyorsa netkâr bilinmiyor kalır. Stop-%10/hedef+%20/60dkzaman aşımı yalnız gözlenen satış kotasyonları üzerinde sabit deneydir; aradaki5dk yol ve stop-hedef sırası garanti edilmez.


Ölçüm hataları: []
