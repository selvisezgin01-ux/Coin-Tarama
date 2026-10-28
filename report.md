# Coin Tarama Meme — V5

Son çalışma: 28.10.2026 22:10 Türkiye saati.

**Deneysel DEX izleme. Tüm yeni tokenleri kapsamaz ve yükseliş garantisi vermez.**

Kapsam: Solana, Ethereum, BNB Chain, Robinhood (Pons dahil), HyperEVM. Pons ayrı bir ağ değildir.

**Hedef: ilk yükseliş öncesi oluşum/birikim.** Yeni aday yalnız birikim evresinde alınır; ilk kırılım ancak daha önce bildirilen birikimin devamı olarak izlenir. Trend listesi aday kaynağı olarak kullanılmaz. **Cüzdan haritası manuel kontrol bekler.** Kritik kontrat/geliştirici verisi eksik tokenler bildirilmez.

Geçmişin tamamındaki fitiller ve açık mum dahil gözlenen dipten tepeye yükseliş %25 üzerindeyse, ilk fiyatın %10 üzerine uzamışsa veya tepeden %15 üzeri düşmüşse elenir. Bu eşikler deneysel tercihlerdir. Havuz başlangıcı, ara mumlar veya güncel mum yoksa ilk oluşum teyitsizdir. Eski pump sonrası yataylaşma yeni aday sayılmaz.

GMGN kullanılmaz. Solana: RugCheck + GoPlus Solana; desteklenen EVM ağları: GoPlus. GMGN’nin tüm sniper/bundler etiketleri ve eksiksiz geliştirici geçmişi sağlanmaz. Teknik risk ön elemesi tokenin resmî/orijinal proje kontratı olduğunu kanıtlamaz.

Yeni havuz yaşı tokenin yaratılma yaşı değildir. Market cap sağlayıcı bildirimi olarak, FDV ise açıkça ayrı değer türü olarak gösterilir. Geliştirici teyidi yalnız belirtilen 45 dakikalık işlem penceresindeki raporlanan adrese aittir; ömür boyu hiç satış yapmadığı veya başka cüzdan kullanmadığı anlamına gelmez.

| Ağ | Güncellenen token | Piyasa ön elemesi | Mum incelenen | Ön eleme / manuel harita bekliyor | İnceleme | Erişim/veri hatası |
|---|---:|---:|---:|---:|---:|---:|
| Solana | 59 | 0 | 1 | 0 | 0 | 1 |
| Ethereum | 39 | 0 | 1 | 0 | 0 | 2 |
| BNB Chain | 54 | 2 | 1 | 0 | 0 | 2 |
| Robinhood | 53 | 4 | 1 | 0 | 0 | 2 |
| HyperEVM (HYPE) | 18 | 0 | 2 | 0 | 0 | 0 |

Bu çalışmada aday olmayan mum incelemeleri (token listesi değildir):
- 1: Başlangıç fiyatından fazla uzaklaşmış
- 2: Önceden yükseliş / uzun fitil görülmüş; Başlangıç fiyatından fazla uzaklaşmış
- 1: Başlangıç geçmişinde veri boşluğu var
- 2: Havuz başlangıç mumları eksik

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

- Solana: ACTX: gecko_request_budget_deferred
- Ethereum: USD: gecko_request_budget_deferred; INVERSE: gecko_request_budget_deferred
- BNB Chain: DOG: gecko_request_budget_deferred; KLG: gecko_request_budget_deferred
- Robinhood: Meecot: gecko_request_budget_deferred; NIHILISM: gecko_request_budget_deferred






<!-- meme-v5-pipeline -->

## V5 keşif, aşamalar ve gerçek zamanlama

Gözlem kaydı alım adayı değildir. Tüm piyasa ön koşulları geçmeden sınırlı mum OKUMA yapılır; olumlu aday için eski piyasa/güvenlik/dev/ilk-pump şartları aynen zorunludur.

Yeni havuz keşfi en çok2sayfa/ağ;15dk altı havuzlar uygun yaşa yaklaşırken öncelikli yenilenir. Bütçe dışında kalan kapsam ve veri boşluğu gizlenmez.

- solana: {"refreshed": 59, "eligible": 0, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["ACTX: gecko_request_budget_deferred"], "funnel": {"records": 59, "waiting_min_age": 29, "market_pass": 0, "market_failed": {"pool_age": 29, "liquidity": 57, "valuation": 50, "transaction_flow15": 44, "volume15": 18, "liquidity_to_valuation": 12, "liquidity_withdrawal": 20}, "market_unknown": {}, "data_inspection_possible": 1, "ohlcv_read": 1, "ohlcv_attempted": 2, "ohlcv_budget_waiting": 0, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793214135000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793214149000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793214149000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price": 1}}
- ethereum: {"refreshed": 39, "eligible": 0, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["USD: gecko_request_budget_deferred", "INVERSE: gecko_request_budget_deferred"], "funnel": {"records": 39, "waiting_min_age": 3, "market_pass": 0, "market_failed": {"pool_age": 3, "liquidity": 28, "valuation": 29, "volume15": 36, "transaction_flow15": 38, "liquidity_to_valuation": 13, "liquidity_withdrawal": 3}, "market_unknown": {}, "data_inspection_possible": 7, "ohlcv_read": 1, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 4, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793210459000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793207327000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793207327000, "valid_page": true}, "reasons": {"initial_pool_history_missing": 1}}
- bnb: {"refreshed": 54, "eligible": 2, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["DOG: gecko_request_budget_deferred", "KLG: gecko_request_budget_deferred"], "funnel": {"records": 54, "waiting_min_age": 17, "market_pass": 2, "market_failed": {"pool_age": 19, "liquidity": 43, "valuation": 46, "volume15": 37, "transaction_flow15": 45, "liquidity_to_valuation": 7, "liquidity_withdrawal": 9}, "market_unknown": {"liquidity": 1}, "data_inspection_possible": 3, "ohlcv_read": 1, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 0, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793213730000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793213243000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793213243000, "valid_page": true}, "reasons": {"already_extended_from_initial_price": 1}}
- robinhood: {"refreshed": 53, "eligible": 4, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["Meecot: gecko_request_budget_deferred", "NIHILISM: gecko_request_budget_deferred"], "funnel": {"records": 53, "waiting_min_age": 17, "market_pass": 4, "market_failed": {"pool_age": 18, "liquidity": 40, "valuation": 41, "transaction_flow15": 38, "volume15": 33, "liquidity_to_valuation": 5, "liquidity_withdrawal": 5}, "market_unknown": {"liquidity": 1}, "data_inspection_possible": 5, "ohlcv_read": 1, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 3, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793213679000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793213529000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793213529000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price": 1}}
- hyperevm: {"refreshed": 18, "eligible": 0, "evaluated": 2, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 18, "waiting_min_age": 0, "market_pass": 0, "market_failed": {"liquidity": 16, "valuation": 16, "volume15": 18, "transaction_flow15": 18, "liquidity_to_valuation": 1, "pool_age": 5}, "market_unknown": {}, "data_inspection_possible": 2, "ohlcv_read": 2, "ohlcv_attempted": 2, "ohlcv_budget_waiting": 0, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793098680000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793214118953, "next_checkpoint_ms": 1793214418771, "oldest_returned_ms": 1793098680000, "valid_page": true}, "reasons": {"initial_history_has_gaps": 1, "initial_pool_history_missing": 1}}

Zamanlama: {"started_ms": 1793214418745, "finished_ms": 1793214656648, "duration_seconds": 237.903, "github_run_created_at": "2026-10-28T18:37:34Z", "worker_started_ms": "1793212917794", "github_job_started_at": "2026-10-28T18:41:43Z", "cadence": {"interval_count": 7, "p95_minutes": 5.0086, "max_minutes": 5.0086, "meets_7m_target": true, "full_24h_observed": false}}

İstek durumu: {"api.geckoterminal.com:ok": 20, "api.dexscreener.com:ok": 15, "gecko:budget_deferred": 7}; sağlayıcı429bekleme bitişi: None

GitHub worker oturumları sınırlıdır. Çalışan oturum içinde hedef5dk; oturum başlangıcı/yenilenmesi gecikebilir. Gerçek aralıklar yukarıda;24saat tamamlanmadan kesintisiz5dk doğrulandı denmez. EskiV4 paralel taranmaz, referansları previous_v4 içinde korunur.

## Sabit miktarlı gösterge satış deneyi

100/500USD notional için ilk gözlem fiyatından hesaplanan token miktarı sabittir; alım gerçekleşmesi değildir. Aynı miktarın sonraki gösterge satış rotası sorgulanır. USDC1USD varsayılmaz. Alım maliyeti, tüm vergiler,gas veya gerçekleşme bilinmiyorsa netkâr bilinmiyor kalır. Stop-%10/hedef+%20/60dkzaman aşımı yalnız gözlenen satış kotasyonları üzerinde sabit deneydir; aradaki5dk yol ve stop-hedef sırası garanti edilmez.


Ölçüm hataları: []
