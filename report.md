# Coin Tarama Meme — V6

Son çalışma: 29.10.2026 17:47 Türkiye saati.

**Deneysel DEX izleme. Tüm yeni tokenleri kapsamaz ve yükseliş garantisi vermez.**

Kapsam: Solana, Ethereum, BNB Chain, Robinhood (Pons dahil), HyperEVM. Pons ayrı bir ağ değildir.

**Hedef: ilk yükseliş öncesi oluşum/birikim.** Yeni aday yalnız birikim evresinde alınır; ilk kırılım ancak daha önce bildirilen birikimin devamı olarak izlenir. Trend listesi aday kaynağı olarak kullanılmaz. **Cüzdan haritası manuel kontrol bekler.** Kritik kontrat/geliştirici verisi eksik tokenler bildirilmez.

Geçmişin tamamındaki fitiller ve açık mum dahil gözlenen dipten tepeye yükseliş %25 üzerindeyse, ilk fiyatın %10 üzerine uzamışsa veya tepeden %15 üzeri düşmüşse elenir. Bu eşikler deneysel tercihlerdir. Havuz başlangıcı, ara mumlar veya güncel mum yoksa ilk oluşum teyitsizdir. Eski pump sonrası yataylaşma yeni aday sayılmaz.

GMGN kullanılmaz. Solana: RugCheck + GoPlus Solana; desteklenen EVM ağları: GoPlus. GMGN’nin tüm sniper/bundler etiketleri ve eksiksiz geliştirici geçmişi sağlanmaz. Teknik risk ön elemesi tokenin resmî/orijinal proje kontratı olduğunu kanıtlamaz.

Yeni havuz yaşı tokenin yaratılma yaşı değildir. Market cap sağlayıcı bildirimi olarak, FDV ise açıkça ayrı değer türü olarak gösterilir. Geliştirici teyidi yalnız belirtilen 45 dakikalık işlem penceresindeki raporlanan adrese aittir; ömür boyu hiç satış yapmadığı veya başka cüzdan kullanmadığı anlamına gelmez.

| Ağ | Güncellenen token | Piyasa ön elemesi | Mum incelenen | Ön eleme / manuel harita bekliyor | İnceleme | Erişim/veri hatası |
|---|---:|---:|---:|---:|---:|---:|
| HyperEVM (HYPE) | 32 | 0 | 0 | 0 | 0 | 0 |
| Ethereum | 32 | 1 | 2 | 0 | 0 | 1 |
| BNB Chain | 57 | 0 | 1 | 0 | 0 | 2 |
| Robinhood | 64 | 1 | 1 | 0 | 0 | 2 |
| Solana | 55 | 1 | 2 | 0 | 0 | 0 |

Bu çalışmada aday olmayan mum incelemeleri (token listesi değildir):
- 2: Başlangıç fiyatından fazla uzaklaşmış
- 3: Güncel mumun yüksek/düşük verisi eksik
- 1: Önceden yükseliş / uzun fitil görülmüş; Başlangıç fiyatından fazla uzaklaşmış

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

- Ethereum: PEPE: gecko_request_reserved_for_buy_pressure
- BNB Chain: SKOOPS: gecko_request_reserved_for_buy_pressure; ELG: gecko_request_reserved_for_buy_pressure
- Robinhood: AIMCAP: gecko_request_reserved_for_buy_pressure; FLOAT: gecko_request_reserved_for_buy_pressure


<!-- meme-v6-pipeline -->

## V6 keşif, aşamalar ve gerçek zamanlama

Gözlem kaydı alım adayı değildir. Tüm piyasa ön koşulları geçmeden sınırlı mum OKUMA yapılır; olumlu aday için eski piyasa/güvenlik/dev/ilk-pump şartları aynen zorunludur.

Yeni havuz keşfi en çok2sayfa/ağ;15dk altı havuzlar uygun yaşa yaklaşırken öncelikli yenilenir. Bütçe dışında kalan kapsam ve veri boşluğu gizlenmez.

- hyperevm: {"refreshed": 32, "eligible": 0, "evaluated": 0, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 32, "waiting_min_age": 3, "market_pass": 0, "market_failed": {"pool_age": 3, "liquidity": 31, "valuation": 32, "volume15": 31, "transaction_flow15": 31, "liquidity_to_valuation": 1, "liquidity_withdrawal": 1}, "market_unknown": {}, "data_inspection_possible": 0, "ohlcv_read": 0, "ohlcv_attempted": 0, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 32}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 32}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793276640000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793284725846, "next_checkpoint_ms": 1793285025829, "oldest_returned_ms": 1793276640000, "valid_page": true}, "reasons": {}}
- ethereum: {"refreshed": 32, "eligible": 1, "evaluated": 2, "qualified": 0, "review": 0, "errors": ["PEPE: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 32, "waiting_min_age": 1, "market_pass": 1, "market_failed": {"pool_age": 2, "liquidity": 25, "valuation": 27, "volume15": 29, "transaction_flow15": 30, "liquidity_to_valuation": 13, "liquidity_withdrawal": 6}, "market_unknown": {}, "data_inspection_possible": 4, "ohlcv_read": 2, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 1, "security_checked": 0, "buy_pressure_status": {"not_checked": 32}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 32}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793280731000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793284725845, "next_checkpoint_ms": 1793285025828, "oldest_returned_ms": 1793280731000, "valid_page": true}, "reasons": {"current_interval_history_missing": 2}}
- bnb: {"refreshed": 57, "eligible": 0, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["SKOOPS: gecko_request_reserved_for_buy_pressure", "ELG: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 57, "waiting_min_age": 10, "market_pass": 0, "market_failed": {"pool_age": 12, "valuation": 48, "transaction_flow15": 50, "liquidity": 43, "liquidity_to_valuation": 21, "volume15": 42, "liquidity_withdrawal": 20}, "market_unknown": {"liquidity": 2, "valuation": 1}, "data_inspection_possible": 6, "ohlcv_read": 1, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 1, "security_checked": 0, "buy_pressure_status": {"not_checked": 57}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 57}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793283909000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793283421000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793283421000, "valid_page": true}, "reasons": {"current_interval_history_missing": 1}}
- robinhood: {"refreshed": 64, "eligible": 1, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["AIMCAP: gecko_request_reserved_for_buy_pressure", "FLOAT: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 64, "waiting_min_age": 26, "market_pass": 1, "market_failed": {"pool_age": 29, "liquidity": 52, "valuation": 55, "volume15": 28, "transaction_flow15": 51, "liquidity_to_valuation": 11, "liquidity_withdrawal": 17}, "market_unknown": {"liquidity": 4}, "data_inspection_possible": 2, "ohlcv_read": 1, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 64}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 64}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793284485000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793284261000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793284261000, "valid_page": true}, "reasons": {"already_extended_from_initial_price": 1}}
- solana: {"refreshed": 55, "eligible": 1, "evaluated": 2, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 55, "waiting_min_age": 25, "market_pass": 1, "market_failed": {"pool_age": 25, "liquidity": 50, "valuation": 50, "transaction_flow15": 47, "volume15": 30, "liquidity_to_valuation": 8, "liquidity_withdrawal": 17}, "market_unknown": {}, "data_inspection_possible": 0, "ohlcv_read": 2, "ohlcv_attempted": 2, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 55}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 55}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793284613000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793284613000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793284613000, "valid_page": true}, "reasons": {"already_extended_from_initial_price": 1, "first_rise_already_observed,already_extended_from_initial_price": 1}}

Zamanlama: {"started_ms": 1793285025777, "finished_ms": 1793285251170, "duration_seconds": 225.393, "github_run_created_at": "2026-10-29T13:21:10Z", "worker_started_ms": "1793283524519", "github_job_started_at": "2026-10-29T14:18:28Z", "cadence": {"interval_count": 49, "p95_minutes": 5.41685, "max_minutes": 5.626, "meets_7m_target": true, "full_24h_observed": false}}

İstek durumu: {"api.geckoterminal.com:ok": 19, "api.dexscreener.com:ok": 11, "gecko:reserved_for_buy_pressure": 5}; sağlayıcı429bekleme bitişi: 1793221779011

GitHub worker oturumları sınırlıdır. Çalışan oturum içinde hedef5dk; oturum başlangıcı/yenilenmesi gecikebilir. Gerçek aralıklar yukarıda;24saat tamamlanmadan kesintisiz5dk doğrulandı denmez. EskiV5 paralel taranmaz, referansları previous_v5 içinde korunur.

## Sabit miktarlı gösterge satış deneyi

100/500USD notional için ilk gözlem fiyatından hesaplanan token miktarı sabittir; alım gerçekleşmesi değildir. Aynı miktarın sonraki gösterge satış rotası sorgulanır. USDC1USD varsayılmaz. Alım maliyeti, tüm vergiler,gas veya gerçekleşme bilinmiyorsa netkâr bilinmiyor kalır. Stop-%10/hedef+%20/60dkzaman aşımı yalnız gözlenen satış kotasyonları üzerinde sabit deneydir; aradaki5dk yol ve stop-hedef sırası garanti edilmez.


Ölçüm hataları: []

## İlk taban ve alım yönlü erken hacim

MCAP:50.000–500.000USD; FDV MCAP yerine onay sayılmaz. 3tam5dk taban mumu ve sonraki kapalı5dkhacmi taban medyanının>=2katı aranır. Aynı kapalı5dk işlem örneğinde alım hacim/adet payı>=%60, alım-satım USD farkı>=250,>=8işlem,>=3netalıcı başlatıcı ve tek alıcı payı<=%60. Son300işlem pencereyi kapsamaz veya OHLCVhacmiyle uyuşmazsa bilinmiyor. Bu adresler bağımsız kişi/servet kanıtı değildir. En erken20–25dk+veri/çalışma gecikmesi. Güvenlik/dev/ilk-pump kapıları korunur.

- ethereum:0x66b67f39dda7137047931ea67c3ea25e2b42c375: {"tier": "watch", "first_base": {"pool": "0x3f5d4020395513406e455736a06791fcd47ddcee", "start_ms": 1793280300000, "end_ms": 1793281200000, "high": 4.83520629449707e-05, "low": 4.65873812941901e-05, "volume_median_usd": 96.5557933288, "width_pct": 3.7878962108579994, "net_change_pct": 3.7612832237952976}, "buy_pressure": {"status": "not_checked", "reasons": ["not_evaluated_this_cycle"]}, "quote_rejection": null}
