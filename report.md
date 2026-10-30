# Coin Tarama Meme — V6

Son çalışma: 30.10.2026 12:22 Türkiye saati.

**Deneysel DEX izleme. Tüm yeni tokenleri kapsamaz ve yükseliş garantisi vermez.**

Kapsam: Solana, Ethereum, BNB Chain, Robinhood (Pons dahil), HyperEVM. Pons ayrı bir ağ değildir.

**Hedef: ilk yükseliş öncesi oluşum/birikim.** Yeni aday yalnız birikim evresinde alınır; ilk kırılım ancak daha önce bildirilen birikimin devamı olarak izlenir. Trend listesi aday kaynağı olarak kullanılmaz. **Cüzdan haritası manuel kontrol bekler.** Kritik kontrat/geliştirici verisi eksik tokenler bildirilmez.

Geçmişin tamamındaki fitiller ve açık mum dahil gözlenen dipten tepeye yükseliş %25 üzerindeyse, ilk fiyatın %10 üzerine uzamışsa veya tepeden %15 üzeri düşmüşse elenir. Bu eşikler deneysel tercihlerdir. Havuz başlangıcı, ara mumlar veya güncel mum yoksa ilk oluşum teyitsizdir. Eski pump sonrası yataylaşma yeni aday sayılmaz.

GMGN kullanılmaz. Solana: RugCheck + GoPlus Solana; desteklenen EVM ağları: GoPlus. GMGN’nin tüm sniper/bundler etiketleri ve eksiksiz geliştirici geçmişi sağlanmaz. Teknik risk ön elemesi tokenin resmî/orijinal proje kontratı olduğunu kanıtlamaz.

Yeni havuz yaşı tokenin yaratılma yaşı değildir. Market cap sağlayıcı bildirimi olarak, FDV ise açıkça ayrı değer türü olarak gösterilir. Geliştirici teyidi yalnız belirtilen 45 dakikalık işlem penceresindeki raporlanan adrese aittir; ömür boyu hiç satış yapmadığı veya başka cüzdan kullanmadığı anlamına gelmez.

| Ağ | Güncellenen token | Piyasa ön elemesi | Mum incelenen | Ön eleme / manuel harita bekliyor | İnceleme | Erişim/veri hatası |
|---|---:|---:|---:|---:|---:|---:|
| HyperEVM (HYPE) | 34 | 0 | 0 | 0 | 0 | 0 |
| Solana | 66 | 0 | 1 | 0 | 0 | 0 |
| BNB Chain | 64 | 1 | 1 | 0 | 0 | 2 |
| Robinhood | 59 | 2 | 1 | 0 | 0 | 2 |
| Ethereum | 33 | 0 | 3 | 0 | 0 | 0 |

Bu çalışmada aday olmayan mum incelemeleri (token listesi değildir):
- 1: Daha eski havuz geçmişi kapsam dışı
- 3: Önceden yükseliş / uzun fitil görülmüş; Başlangıç fiyatından fazla uzaklaşmış
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

- BNB Chain: PREDICT: gecko_request_reserved_for_buy_pressure; PREDICT: gecko_request_reserved_for_buy_pressure
- Robinhood: SAFU: gecko_request_reserved_for_buy_pressure; PMBFT30: gecko_request_reserved_for_buy_pressure






<!-- meme-v6-pipeline -->

## V6 keşif, aşamalar ve gerçek zamanlama

Gözlem kaydı alım adayı değildir. Tüm piyasa ön koşulları geçmeden sınırlı mum OKUMA yapılır; olumlu aday için eski piyasa/güvenlik/dev/ilk-pump şartları aynen zorunludur.

Yeni havuz keşfi en çok2sayfa/ağ;15dk altı havuzlar uygun yaşa yaklaşırken öncelikli yenilenir. Bütçe dışında kalan kapsam ve veri boşluğu gizlenmez.

- hyperevm: {"refreshed": 34, "eligible": 0, "evaluated": 0, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 34, "waiting_min_age": 0, "market_pass": 0, "market_failed": {"valuation": 34, "transaction_flow15": 34, "liquidity": 33, "volume15": 33, "liquidity_to_valuation": 1}, "market_unknown": {}, "data_inspection_possible": 0, "ohlcv_read": 0, "ohlcv_attempted": 0, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 34}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 34}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793293440000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793351646826, "next_checkpoint_ms": 1793351946811, "oldest_returned_ms": 1793293440000, "valid_page": true}, "reasons": {}}
- solana: {"refreshed": 66, "eligible": 0, "evaluated": 1, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 66, "waiting_min_age": 36, "market_pass": 0, "market_failed": {"pool_age": 36, "liquidity": 61, "valuation": 66, "volume15": 52, "transaction_flow15": 55, "liquidity_to_valuation": 10, "liquidity_withdrawal": 19}, "market_unknown": {}, "data_inspection_possible": 0, "ohlcv_read": 1, "ohlcv_attempted": 1, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 66}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 66}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793351835000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793351869000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793351869000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price": 1}}
- bnb: {"refreshed": 64, "eligible": 1, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["PREDICT: gecko_request_reserved_for_buy_pressure", "PREDICT: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 64, "waiting_min_age": 24, "market_pass": 1, "market_failed": {"pool_age": 26, "liquidity": 52, "valuation": 60, "volume15": 41, "transaction_flow15": 55, "liquidity_withdrawal": 13, "liquidity_to_valuation": 13}, "market_unknown": {"valuation": 1}, "data_inspection_possible": 2, "ohlcv_read": 1, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 64}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 64}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793351509000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793351075000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793351075000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price": 1}}
- robinhood: {"refreshed": 59, "eligible": 2, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["SAFU: gecko_request_reserved_for_buy_pressure", "PMBFT30: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 59, "waiting_min_age": 19, "market_pass": 2, "market_failed": {"pool_age": 20, "valuation": 48, "transaction_flow15": 45, "volume15": 35, "liquidity": 48, "liquidity_to_valuation": 25, "liquidity_withdrawal": 10}, "market_unknown": {"liquidity": 1}, "data_inspection_possible": 2, "ohlcv_read": 1, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 59}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 59}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793351246000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793350604000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793350604000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price": 1}}
- ethereum: {"refreshed": 33, "eligible": 0, "evaluated": 3, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 33, "waiting_min_age": 3, "market_pass": 0, "market_failed": {"pool_age": 4, "liquidity": 30, "valuation": 33, "volume15": 33, "transaction_flow15": 32, "liquidity_to_valuation": 22, "liquidity_withdrawal": 4}, "market_unknown": {}, "data_inspection_possible": 3, "ohlcv_read": 3, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 33}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 33}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793349239000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793351646825, "next_checkpoint_ms": 1793351946810, "oldest_returned_ms": 1793349239000, "valid_page": true}, "reasons": {"initial_pool_history_missing": 1, "earlier_pool_history_not_covered": 1, "initial_history_has_gaps": 1}}

Zamanlama: {"started_ms": 1793351946768, "finished_ms": 1793352172284, "duration_seconds": 225.516, "github_run_created_at": "2026-10-30T07:21:59Z", "worker_started_ms": "1793348945405", "github_job_started_at": "2026-10-30T08:28:54Z", "cadence": {"interval_count": 274, "p95_minutes": 5.62405, "max_minutes": 8.757266666666666, "meets_7m_target": true, "full_24h_observed": false}}

İstek durumu: {"api.geckoterminal.com:ok": 19, "api.dexscreener.com:ok": 18, "gecko:reserved_for_buy_pressure": 4}; sağlayıcı429bekleme bitişi: 1793335051606

GitHub worker oturumları sınırlıdır. Çalışan oturum içinde hedef5dk; oturum başlangıcı/yenilenmesi gecikebilir. Gerçek aralıklar yukarıda;24saat tamamlanmadan kesintisiz5dk doğrulandı denmez. EskiV5 paralel taranmaz, referansları previous_v5 içinde korunur.

## Sabit miktarlı gösterge satış deneyi

100/500USD notional için ilk gözlem fiyatından hesaplanan token miktarı sabittir; alım gerçekleşmesi değildir. Aynı miktarın sonraki gösterge satış rotası sorgulanır. USDC1USD varsayılmaz. Alım maliyeti, tüm vergiler,gas veya gerçekleşme bilinmiyorsa netkâr bilinmiyor kalır. Stop-%10/hedef+%20/60dkzaman aşımı yalnız gözlenen satış kotasyonları üzerinde sabit deneydir; aradaki5dk yol ve stop-hedef sırası garanti edilmez.


Ölçüm hataları: []

## İlk taban ve alım yönlü erken hacim

MCAP:50.000–500.000USD; FDV MCAP yerine onay sayılmaz. 3tam5dk taban mumu ve sonraki kapalı5dkhacmi taban medyanının>=2katı aranır. Aynı kapalı5dk işlem örneğinde alım hacim/adet payı>=%60, alım-satım USD farkı>=250,>=8işlem,>=3netalıcı başlatıcı ve tek alıcı payı<=%60. Son300işlem pencereyi kapsamaz veya OHLCVhacmiyle uyuşmazsa bilinmiyor. Bu adresler bağımsız kişi/servet kanıtı değildir. En erken20–25dk+veri/çalışma gecikmesi. Güvenlik/dev/ilk-pump kapıları korunur.

- ethereum:0xb62132e35a6c13ee1ee0f84dc5d40bad8d815206: {"tier": "watch", "first_base": {"pool": "0x393bde20c49a7db04b274c7fa71b9231156948e9feff46eb8f58966ee11b409f", "start_ms": 1793334000000, "end_ms": 1793334900000, "high": 0.748040723114512, "low": 0.676709086803438, "volume_median_usd": 2883.146821169459, "width_pct": 10.540960318417225, "net_change_pct": -1.4366909478423007}, "buy_pressure": {"status": "not_checked", "reasons": ["not_evaluated_this_cycle"]}, "quote_rejection": null}
- ethereum:0x56a3ba04e95d34268a19b2a4474dc979babdaf76: {"tier": "watch", "first_base": {"pool": "0x626d1bb657dacaa9bd0fa9f81a2f8f1efcd2b6dc113598f06713959296294e78", "start_ms": 1793339100000, "end_ms": 1793340000000, "high": 0.0189295967555192, "low": 0.018401935210147, "volume_median_usd": 15592.76693137471, "width_pct": 2.8674242102604497, "net_change_pct": -0.9115077984417685}, "buy_pressure": {"status": "not_checked", "reasons": ["not_evaluated_this_cycle"]}, "quote_rejection": null}
- ethereum:0xff20817765cb7f73d4bde2e66e067e58d11095c2: {"tier": "watch", "first_base": {"pool": "0x1392338ec2482534d87c4c31d2d0cf2e4a5bf42fe2f9b0b348e18c658dae9279", "start_ms": 1793340300000, "end_ms": 1793341200000, "high": 0.000618131939699432, "low": 0.000569463125951467, "volume_median_usd": 27555.039207112877, "width_pct": 8.546438132697087, "net_change_pct": 3.6702482730982533}, "buy_pressure": {"status": "not_checked", "reasons": ["not_evaluated_this_cycle"]}, "quote_rejection": null}
