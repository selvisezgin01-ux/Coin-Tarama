# Coin Tarama Meme — V5

Son çalışma: 29.10.2026 07:26 Türkiye saati.

**Deneysel DEX izleme. Tüm yeni tokenleri kapsamaz ve yükseliş garantisi vermez.**

Kapsam: Solana, Ethereum, BNB Chain, Robinhood (Pons dahil), HyperEVM. Pons ayrı bir ağ değildir.

**Hedef: ilk yükseliş öncesi oluşum/birikim.** Yeni aday yalnız birikim evresinde alınır; ilk kırılım ancak daha önce bildirilen birikimin devamı olarak izlenir. Trend listesi aday kaynağı olarak kullanılmaz. **Cüzdan haritası manuel kontrol bekler.** Kritik kontrat/geliştirici verisi eksik tokenler bildirilmez.

Geçmişin tamamındaki fitiller ve açık mum dahil gözlenen dipten tepeye yükseliş %25 üzerindeyse, ilk fiyatın %10 üzerine uzamışsa veya tepeden %15 üzeri düşmüşse elenir. Bu eşikler deneysel tercihlerdir. Havuz başlangıcı, ara mumlar veya güncel mum yoksa ilk oluşum teyitsizdir. Eski pump sonrası yataylaşma yeni aday sayılmaz.

GMGN kullanılmaz. Solana: RugCheck + GoPlus Solana; desteklenen EVM ağları: GoPlus. GMGN’nin tüm sniper/bundler etiketleri ve eksiksiz geliştirici geçmişi sağlanmaz. Teknik risk ön elemesi tokenin resmî/orijinal proje kontratı olduğunu kanıtlamaz.

Yeni havuz yaşı tokenin yaratılma yaşı değildir. Market cap sağlayıcı bildirimi olarak, FDV ise açıkça ayrı değer türü olarak gösterilir. Geliştirici teyidi yalnız belirtilen 45 dakikalık işlem penceresindeki raporlanan adrese aittir; ömür boyu hiç satış yapmadığı veya başka cüzdan kullanmadığı anlamına gelmez.

| Ağ | Güncellenen token | Piyasa ön elemesi | Mum incelenen | Ön eleme / manuel harita bekliyor | İnceleme | Erişim/veri hatası |
|---|---:|---:|---:|---:|---:|---:|
| HyperEVM (HYPE) | 19 | 0 | 0 | 0 | 0 | 0 |
| Solana | 70 | 2 | 0 | 0 | 0 | 0 |
| Ethereum | 39 | 1 | 3 | 0 | 0 | 0 |
| BNB Chain | 61 | 2 | 2 | 0 | 0 | 1 |
| Robinhood | 61 | 3 | 2 | 0 | 0 | 1 |

Bu çalışmada aday olmayan mum incelemeleri (token listesi değildir):
- 1: Başlangıç fiyatından fazla uzaklaşmış
- 2: Güncel mumun yüksek/düşük verisi eksik
- 4: Önceden yükseliş / uzun fitil görülmüş; Başlangıç fiyatından fazla uzaklaşmış

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

- BNB Chain: EVAA: gecko_request_budget_deferred
- Robinhood: CPU: gecko_request_budget_deferred


<!-- meme-v5-pipeline -->

## V5 keşif, aşamalar ve gerçek zamanlama

Gözlem kaydı alım adayı değildir. Tüm piyasa ön koşulları geçmeden sınırlı mum OKUMA yapılır; olumlu aday için eski piyasa/güvenlik/dev/ilk-pump şartları aynen zorunludur.

Yeni havuz keşfi en çok2sayfa/ağ;15dk altı havuzlar uygun yaşa yaklaşırken öncelikli yenilenir. Bütçe dışında kalan kapsam ve veri boşluğu gizlenmez.

- hyperevm: {"refreshed": 19, "eligible": 0, "evaluated": 0, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 19, "waiting_min_age": 0, "market_pass": 0, "market_failed": {"liquidity": 18, "valuation": 18, "liquidity_to_valuation": 2, "volume15": 19, "transaction_flow15": 19, "pool_age": 2}, "market_unknown": {}, "data_inspection_possible": 0, "ohlcv_read": 0, "ohlcv_attempted": 0, "ohlcv_budget_waiting": 0, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793137020000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793247454125, "next_checkpoint_ms": 1793247754083, "oldest_returned_ms": 1793137020000, "valid_page": true}, "reasons": {}}
- solana: {"refreshed": 70, "eligible": 2, "evaluated": 0, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 70, "waiting_min_age": 40, "market_pass": 2, "market_failed": {"pool_age": 40, "liquidity": 61, "valuation": 62, "transaction_flow15": 56, "volume15": 50, "liquidity_to_valuation": 8, "liquidity_withdrawal": 6}, "market_unknown": {}, "data_inspection_possible": 0, "ohlcv_read": 0, "ohlcv_attempted": 0, "ohlcv_budget_waiting": 0, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793247564000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793247707000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793247707000, "valid_page": true}, "reasons": {}}
- ethereum: {"refreshed": 39, "eligible": 1, "evaluated": 3, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 39, "waiting_min_age": 2, "market_pass": 1, "market_failed": {"pool_age": 2, "liquidity": 32, "valuation": 34, "liquidity_to_valuation": 18, "volume15": 35, "transaction_flow15": 37, "liquidity_withdrawal": 2}, "market_unknown": {}, "data_inspection_possible": 2, "ohlcv_read": 3, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 0, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793235311000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793247454124, "next_checkpoint_ms": 1793247754083, "oldest_returned_ms": 1793235311000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price": 1, "current_interval_history_missing": 2}}
- bnb: {"refreshed": 61, "eligible": 2, "evaluated": 2, "qualified": 0, "review": 0, "errors": ["EVAA: gecko_request_budget_deferred"], "funnel": {"records": 61, "waiting_min_age": 17, "market_pass": 2, "market_failed": {"pool_age": 20, "liquidity": 51, "valuation": 51, "volume15": 48, "transaction_flow15": 55, "liquidity_withdrawal": 8, "liquidity_to_valuation": 7}, "market_unknown": {}, "data_inspection_possible": 1, "ohlcv_read": 2, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 0, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793247069000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793246737000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793246737000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price": 1, "already_extended_from_initial_price": 1}}
- robinhood: {"refreshed": 61, "eligible": 3, "evaluated": 2, "qualified": 0, "review": 0, "errors": ["CPU: gecko_request_budget_deferred"], "funnel": {"records": 61, "waiting_min_age": 21, "market_pass": 3, "market_failed": {"pool_age": 21, "valuation": 27, "volume15": 44, "transaction_flow15": 50, "liquidity": 48, "liquidity_to_valuation": 26, "liquidity_withdrawal": 4}, "market_unknown": {"liquidity": 1}, "data_inspection_possible": 1, "ohlcv_read": 2, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 0, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793247142000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793246489000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793246489000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price": 2}}

Zamanlama: {"started_ms": 1793247754040, "finished_ms": 1793247991943, "duration_seconds": 237.903, "github_run_created_at": "2026-10-29T03:03:47Z", "worker_started_ms": "1793245652723", "github_job_started_at": "2026-10-29T03:47:17Z", "cadence": {"interval_count": 118, "p95_minutes": 5.836983333333333, "max_minutes": 8.9655, "meets_7m_target": true, "full_24h_observed": false}}

İstek durumu: {"api.geckoterminal.com:ok": 20, "api.dexscreener.com:ok": 12, "gecko:budget_deferred": 2}; sağlayıcı429bekleme bitişi: 1793221779011

GitHub worker oturumları sınırlıdır. Çalışan oturum içinde hedef5dk; oturum başlangıcı/yenilenmesi gecikebilir. Gerçek aralıklar yukarıda;24saat tamamlanmadan kesintisiz5dk doğrulandı denmez. EskiV4 paralel taranmaz, referansları previous_v4 içinde korunur.

## Sabit miktarlı gösterge satış deneyi

100/500USD notional için ilk gözlem fiyatından hesaplanan token miktarı sabittir; alım gerçekleşmesi değildir. Aynı miktarın sonraki gösterge satış rotası sorgulanır. USDC1USD varsayılmaz. Alım maliyeti, tüm vergiler,gas veya gerçekleşme bilinmiyorsa netkâr bilinmiyor kalır. Stop-%10/hedef+%20/60dkzaman aşımı yalnız gözlenen satış kotasyonları üzerinde sabit deneydir; aradaki5dk yol ve stop-hedef sırası garanti edilmez.


Ölçüm hataları: []
