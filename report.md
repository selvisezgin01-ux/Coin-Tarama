# Coin Tarama Meme — V5

Son çalışma: 28.10.2026 23:54 Türkiye saati.

**Deneysel DEX izleme. Tüm yeni tokenleri kapsamaz ve yükseliş garantisi vermez.**

Kapsam: Solana, Ethereum, BNB Chain, Robinhood (Pons dahil), HyperEVM. Pons ayrı bir ağ değildir.

**Hedef: ilk yükseliş öncesi oluşum/birikim.** Yeni aday yalnız birikim evresinde alınır; ilk kırılım ancak daha önce bildirilen birikimin devamı olarak izlenir. Trend listesi aday kaynağı olarak kullanılmaz. **Cüzdan haritası manuel kontrol bekler.** Kritik kontrat/geliştirici verisi eksik tokenler bildirilmez.

Geçmişin tamamındaki fitiller ve açık mum dahil gözlenen dipten tepeye yükseliş %25 üzerindeyse, ilk fiyatın %10 üzerine uzamışsa veya tepeden %15 üzeri düşmüşse elenir. Bu eşikler deneysel tercihlerdir. Havuz başlangıcı, ara mumlar veya güncel mum yoksa ilk oluşum teyitsizdir. Eski pump sonrası yataylaşma yeni aday sayılmaz.

GMGN kullanılmaz. Solana: RugCheck + GoPlus Solana; desteklenen EVM ağları: GoPlus. GMGN’nin tüm sniper/bundler etiketleri ve eksiksiz geliştirici geçmişi sağlanmaz. Teknik risk ön elemesi tokenin resmî/orijinal proje kontratı olduğunu kanıtlamaz.

Yeni havuz yaşı tokenin yaratılma yaşı değildir. Market cap sağlayıcı bildirimi olarak, FDV ise açıkça ayrı değer türü olarak gösterilir. Geliştirici teyidi yalnız belirtilen 45 dakikalık işlem penceresindeki raporlanan adrese aittir; ömür boyu hiç satış yapmadığı veya başka cüzdan kullanmadığı anlamına gelmez.

| Ağ | Güncellenen token | Piyasa ön elemesi | Mum incelenen | Ön eleme / manuel harita bekliyor | İnceleme | Erişim/veri hatası |
|---|---:|---:|---:|---:|---:|---:|
| BNB Chain | 33 | 1 | 0 | 0 | 0 | 4 |
| Robinhood | 30 | 1 | 0 | 0 | 0 | 2 |
| HyperEVM (HYPE) | 18 | 0 | 0 | 0 | 0 | 2 |
| Solana | 60 | 0 | 0 | 0 | 0 | 3 |
| Ethereum | 35 | 1 | 1 | 0 | 0 | 2 |

Bu çalışmada aday olmayan mum incelemeleri (token listesi değildir):
- 1: Güncel mumun yüksek/düşük verisi eksik

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

- BNB Chain: api.geckoterminal.com: HTTP 429; BOBB: api.geckoterminal.com: provider stopped after access/rate error; BAP: api.geckoterminal.com: provider stopped after access/rate error; TOKEN: api.geckoterminal.com: provider stopped after access/rate error
- Robinhood: api.geckoterminal.com: queued request stopped after access/rate error; MoonCoin: gecko_request_budget_deferred
- HyperEVM (HYPE): BULL: api.geckoterminal.com: queued request stopped after access/rate error; iBEAR: gecko_request_budget_deferred
- Solana: NODF: api.geckoterminal.com: queued request stopped after access/rate error; Toad: gecko_request_budget_deferred; uinhim: gecko_request_budget_deferred
- Ethereum: NBISon: api.geckoterminal.com: queued request stopped after access/rate error; USDte: gecko_request_budget_deferred


<!-- meme-v5-pipeline -->

## V5 keşif, aşamalar ve gerçek zamanlama

Gözlem kaydı alım adayı değildir. Tüm piyasa ön koşulları geçmeden sınırlı mum OKUMA yapılır; olumlu aday için eski piyasa/güvenlik/dev/ilk-pump şartları aynen zorunludur.

Yeni havuz keşfi en çok2sayfa/ağ;15dk altı havuzlar uygun yaşa yaklaşırken öncelikli yenilenir. Bütçe dışında kalan kapsam ve veri boşluğu gizlenmez.

- bnb: {"refreshed": 33, "eligible": 1, "evaluated": 0, "qualified": 0, "review": 0, "errors": ["api.geckoterminal.com: HTTP 429", "BOBB: api.geckoterminal.com: provider stopped after access/rate error", "BAP: api.geckoterminal.com: provider stopped after access/rate error", "TOKEN: api.geckoterminal.com: provider stopped after access/rate error"], "funnel": {"records": 33, "waiting_min_age": 18, "market_pass": 1, "market_failed": {"pool_age": 18, "liquidity": 22, "valuation": 27, "volume15": 21, "transaction_flow15": 25, "liquidity_to_valuation": 8}, "market_unknown": {}, "data_inspection_possible": 5, "ohlcv_read": 0, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 2, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793219940000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793219537000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793219537000, "valid_page": true}, "reasons": {}}
- robinhood: {"refreshed": 30, "eligible": 1, "evaluated": 0, "qualified": 0, "review": 0, "errors": ["api.geckoterminal.com: queued request stopped after access/rate error", "MoonCoin: gecko_request_budget_deferred"], "funnel": {"records": 30, "waiting_min_age": 19, "market_pass": 1, "market_failed": {"pool_age": 19, "liquidity": 20, "valuation": 21, "volume15": 18, "transaction_flow15": 24, "liquidity_to_valuation": 8}, "market_unknown": {"liquidity": 2}, "data_inspection_possible": 1, "ohlcv_read": 0, "ohlcv_attempted": 1, "ohlcv_budget_waiting": 0, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793219994000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793219677000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793219677000, "valid_page": true}, "reasons": {}}
- hyperevm: {"refreshed": 18, "eligible": 0, "evaluated": 0, "qualified": 0, "review": 0, "errors": ["BULL: api.geckoterminal.com: queued request stopped after access/rate error", "iBEAR: gecko_request_budget_deferred"], "funnel": {"records": 18, "waiting_min_age": 0, "market_pass": 0, "market_failed": {"liquidity": 16, "valuation": 16, "volume15": 18, "transaction_flow15": 18, "liquidity_to_valuation": 1, "pool_age": 5}, "market_unknown": {}, "data_inspection_possible": 2, "ohlcv_read": 0, "ohlcv_attempted": 2, "ohlcv_budget_waiting": 0, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793098680000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793219475897, "next_checkpoint_ms": 1793220675068, "oldest_returned_ms": 1793098680000, "valid_page": true}, "reasons": {}}
- solana: {"refreshed": 60, "eligible": 0, "evaluated": 0, "qualified": 0, "review": 0, "errors": ["NODF: api.geckoterminal.com: queued request stopped after access/rate error", "Toad: gecko_request_budget_deferred", "uinhim: gecko_request_budget_deferred"], "funnel": {"records": 60, "waiting_min_age": 30, "market_pass": 0, "market_failed": {"pool_age": 30, "liquidity": 51, "transaction_flow15": 53, "valuation": 45, "volume15": 47, "liquidity_to_valuation": 5, "liquidity_withdrawal": 11}, "market_unknown": {"valuation": 10, "liquidity": 3}, "data_inspection_possible": 3, "ohlcv_read": 0, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 0, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793220600000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793220618000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793220618000, "valid_page": true}, "reasons": {}}
- ethereum: {"refreshed": 35, "eligible": 1, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["NBISon: api.geckoterminal.com: queued request stopped after access/rate error", "USDte: gecko_request_budget_deferred"], "funnel": {"records": 35, "waiting_min_age": 0, "market_pass": 1, "market_failed": {"liquidity": 28, "liquidity_to_valuation": 9, "volume15": 34, "transaction_flow15": 34, "liquidity_withdrawal": 3, "valuation": 30}, "market_unknown": {}, "data_inspection_possible": 6, "ohlcv_read": 1, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 3, "security_checked": 0}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793212259000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793219475897, "next_checkpoint_ms": 1793220675067, "oldest_returned_ms": 1793212259000, "valid_page": true}, "reasons": {"current_interval_history_missing": 1}}

Zamanlama: {"started_ms": 1793220675033, "finished_ms": 1793220875068, "duration_seconds": 200.035, "github_run_created_at": "2026-10-28T20:00:17Z", "worker_started_ms": "1793219473559", "github_job_started_at": "2026-10-28T20:30:56Z", "cadence": {"interval_count": 28, "p95_minutes": 5.059966666666667, "max_minutes": 8.3347, "meets_7m_target": true, "full_24h_observed": false}}

İstek durumu: {"api.geckoterminal.com:ok": 12, "api.dexscreener.com:ok": 8, "api.geckoterminal.com:error": 1, "gecko:budget_deferred": 5}; sağlayıcı429bekleme bitişi: 1793221775068

GitHub worker oturumları sınırlıdır. Çalışan oturum içinde hedef5dk; oturum başlangıcı/yenilenmesi gecikebilir. Gerçek aralıklar yukarıda;24saat tamamlanmadan kesintisiz5dk doğrulandı denmez. EskiV4 paralel taranmaz, referansları previous_v4 içinde korunur.

## Sabit miktarlı gösterge satış deneyi

100/500USD notional için ilk gözlem fiyatından hesaplanan token miktarı sabittir; alım gerçekleşmesi değildir. Aynı miktarın sonraki gösterge satış rotası sorgulanır. USDC1USD varsayılmaz. Alım maliyeti, tüm vergiler,gas veya gerçekleşme bilinmiyorsa netkâr bilinmiyor kalır. Stop-%10/hedef+%20/60dkzaman aşımı yalnız gözlenen satış kotasyonları üzerinde sabit deneydir; aradaki5dk yol ve stop-hedef sırası garanti edilmez.


Ölçüm hataları: []
