# Coin Tarama Meme — V6

Son çalışma: 30.10.2026 08:04 Türkiye saati.

**Deneysel DEX izleme. Tüm yeni tokenleri kapsamaz ve yükseliş garantisi vermez.**

Kapsam: Solana, Ethereum, BNB Chain, Robinhood (Pons dahil), HyperEVM. Pons ayrı bir ağ değildir.

**Hedef: ilk yükseliş öncesi oluşum/birikim.** Yeni aday yalnız birikim evresinde alınır; ilk kırılım ancak daha önce bildirilen birikimin devamı olarak izlenir. Trend listesi aday kaynağı olarak kullanılmaz. **Cüzdan haritası manuel kontrol bekler.** Kritik kontrat/geliştirici verisi eksik tokenler bildirilmez.

Geçmişin tamamındaki fitiller ve açık mum dahil gözlenen dipten tepeye yükseliş %25 üzerindeyse, ilk fiyatın %10 üzerine uzamışsa veya tepeden %15 üzeri düşmüşse elenir. Bu eşikler deneysel tercihlerdir. Havuz başlangıcı, ara mumlar veya güncel mum yoksa ilk oluşum teyitsizdir. Eski pump sonrası yataylaşma yeni aday sayılmaz.

GMGN kullanılmaz. Solana: RugCheck + GoPlus Solana; desteklenen EVM ağları: GoPlus. GMGN’nin tüm sniper/bundler etiketleri ve eksiksiz geliştirici geçmişi sağlanmaz. Teknik risk ön elemesi tokenin resmî/orijinal proje kontratı olduğunu kanıtlamaz.

Yeni havuz yaşı tokenin yaratılma yaşı değildir. Market cap sağlayıcı bildirimi olarak, FDV ise açıkça ayrı değer türü olarak gösterilir. Geliştirici teyidi yalnız belirtilen 45 dakikalık işlem penceresindeki raporlanan adrese aittir; ömür boyu hiç satış yapmadığı veya başka cüzdan kullanmadığı anlamına gelmez.

| Ağ | Güncellenen token | Piyasa ön elemesi | Mum incelenen | Ön eleme / manuel harita bekliyor | İnceleme | Erişim/veri hatası |
|---|---:|---:|---:|---:|---:|---:|
| HyperEVM (HYPE) | 32 | 0 | 0 | 0 | 0 | 0 |
| Ethereum | 37 | 0 | 2 | 0 | 0 | 1 |
| BNB Chain | 53 | 1 | 1 | 0 | 0 | 2 |
| Robinhood | 53 | 1 | 1 | 0 | 0 | 2 |
| Solana | 62 | 0 | 2 | 0 | 0 | 1 |

Bu çalışmada aday olmayan mum incelemeleri (token listesi değildir):
- 1: Başlangıç fiyatından fazla uzaklaşmış
- 1: Daha eski havuz geçmişi kapsam dışı
- 3: Önceden yükseliş / uzun fitil görülmüş; Başlangıç fiyatından fazla uzaklaşmış
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

- Ethereum: SENT: gecko_request_reserved_for_buy_pressure
- BNB Chain: SWARM: gecko_request_reserved_for_buy_pressure; TMR: gecko_request_reserved_for_buy_pressure
- Robinhood: Fomiossa: gecko_request_reserved_for_buy_pressure; KENNETH: gecko_request_reserved_for_buy_pressure
- Solana: AODF: gecko_request_reserved_for_buy_pressure






<!-- meme-v6-pipeline -->

## V6 keşif, aşamalar ve gerçek zamanlama

Gözlem kaydı alım adayı değildir. Tüm piyasa ön koşulları geçmeden sınırlı mum OKUMA yapılır; olumlu aday için eski piyasa/güvenlik/dev/ilk-pump şartları aynen zorunludur.

Yeni havuz keşfi en çok2sayfa/ağ;15dk altı havuzlar uygun yaşa yaklaşırken öncelikli yenilenir. Bütçe dışında kalan kapsam ve veri boşluğu gizlenmez.

- hyperevm: {"refreshed": 32, "eligible": 0, "evaluated": 0, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 32, "waiting_min_age": 0, "market_pass": 0, "market_failed": {"liquidity": 32, "valuation": 32, "volume15": 32, "transaction_flow15": 32, "liquidity_to_valuation": 1}, "market_unknown": {}, "data_inspection_possible": 0, "ohlcv_read": 0, "ohlcv_attempted": 0, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 32}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 32}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793292540000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793336153016, "next_checkpoint_ms": 1793336452956, "oldest_returned_ms": 1793292540000, "valid_page": true}, "reasons": {}}
- ethereum: {"refreshed": 37, "eligible": 0, "evaluated": 2, "qualified": 0, "review": 0, "errors": ["SENT: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 37, "waiting_min_age": 6, "market_pass": 0, "market_failed": {"pool_age": 7, "liquidity": 27, "valuation": 37, "volume15": 34, "transaction_flow15": 35, "liquidity_to_valuation": 29, "liquidity_withdrawal": 6}, "market_unknown": {}, "data_inspection_possible": 6, "ohlcv_read": 2, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 3, "security_checked": 0, "buy_pressure_status": {"not_checked": 37}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 37}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793333843000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793336153016, "next_checkpoint_ms": 1793336452956, "oldest_returned_ms": 1793333843000, "valid_page": true}, "reasons": {"initial_pool_history_missing": 1, "earlier_pool_history_not_covered": 1}}
- bnb: {"refreshed": 53, "eligible": 1, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["SWARM: gecko_request_reserved_for_buy_pressure", "TMR: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 53, "waiting_min_age": 15, "market_pass": 1, "market_failed": {"pool_age": 16, "liquidity": 38, "valuation": 49, "volume15": 30, "transaction_flow15": 38, "liquidity_to_valuation": 13, "liquidity_withdrawal": 24}, "market_unknown": {"liquidity": 1}, "data_inspection_possible": 4, "ohlcv_read": 1, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 2, "security_checked": 0, "buy_pressure_status": {"not_checked": 53}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 53}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793335581000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793334687000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793334687000, "valid_page": true}, "reasons": {"already_extended_from_initial_price": 1}}
- robinhood: {"refreshed": 53, "eligible": 1, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["Fomiossa: gecko_request_reserved_for_buy_pressure", "KENNETH: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 53, "waiting_min_age": 14, "market_pass": 1, "market_failed": {"pool_age": 15, "liquidity": 38, "valuation": 45, "volume15": 36, "transaction_flow15": 49, "liquidity_to_valuation": 17, "liquidity_withdrawal": 8}, "market_unknown": {"liquidity": 1}, "data_inspection_possible": 5, "ohlcv_read": 1, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 3, "security_checked": 0, "buy_pressure_status": {"not_checked": 53}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 53}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793335476000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793334633000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793334633000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price": 1}}
- solana: {"refreshed": 62, "eligible": 0, "evaluated": 2, "qualified": 0, "review": 0, "errors": ["AODF: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 62, "waiting_min_age": 32, "market_pass": 0, "market_failed": {"pool_age": 32, "volume15": 46, "liquidity": 56, "valuation": 58, "transaction_flow15": 44, "liquidity_to_valuation": 7, "liquidity_withdrawal": 14}, "market_unknown": {}, "data_inspection_possible": 2, "ohlcv_read": 2, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 1, "security_checked": 0, "buy_pressure_status": {"not_checked": 62}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 62}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793336337000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793336377000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793336377000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price": 2}}

Zamanlama: {"started_ms": 1793336452920, "finished_ms": 1793336678453, "duration_seconds": 225.533, "github_run_created_at": "2026-10-30T04:06:10Z", "worker_started_ms": "1793335851507", "github_job_started_at": "2026-10-30T04:50:36Z", "cadence": {"interval_count": 222, "p95_minutes": 5.622516666666667, "max_minutes": 8.757266666666666, "meets_7m_target": true, "full_24h_observed": false}}

İstek durumu: {"api.geckoterminal.com:ok": 19, "api.dexscreener.com:ok": 17, "gecko:reserved_for_buy_pressure": 6}; sağlayıcı429bekleme bitişi: 1793335051606

GitHub worker oturumları sınırlıdır. Çalışan oturum içinde hedef5dk; oturum başlangıcı/yenilenmesi gecikebilir. Gerçek aralıklar yukarıda;24saat tamamlanmadan kesintisiz5dk doğrulandı denmez. EskiV5 paralel taranmaz, referansları previous_v5 içinde korunur.

## Sabit miktarlı gösterge satış deneyi

100/500USD notional için ilk gözlem fiyatından hesaplanan token miktarı sabittir; alım gerçekleşmesi değildir. Aynı miktarın sonraki gösterge satış rotası sorgulanır. USDC1USD varsayılmaz. Alım maliyeti, tüm vergiler,gas veya gerçekleşme bilinmiyorsa netkâr bilinmiyor kalır. Stop-%10/hedef+%20/60dkzaman aşımı yalnız gözlenen satış kotasyonları üzerinde sabit deneydir; aradaki5dk yol ve stop-hedef sırası garanti edilmez.


Ölçüm hataları: []

## İlk taban ve alım yönlü erken hacim

MCAP:50.000–500.000USD; FDV MCAP yerine onay sayılmaz. 3tam5dk taban mumu ve sonraki kapalı5dkhacmi taban medyanının>=2katı aranır. Aynı kapalı5dk işlem örneğinde alım hacim/adet payı>=%60, alım-satım USD farkı>=250,>=8işlem,>=3netalıcı başlatıcı ve tek alıcı payı<=%60. Son300işlem pencereyi kapsamaz veya OHLCVhacmiyle uyuşmazsa bilinmiyor. Bu adresler bağımsız kişi/servet kanıtı değildir. En erken20–25dk+veri/çalışma gecikmesi. Güvenlik/dev/ilk-pump kapıları korunur.

- ethereum:0xf629cbd94d3791c9250152bd8dfbdf380e2a3b9c: {"tier": "watch", "first_base": {"pool": "0xa963f4c9dc29ba718f50c03e10db85b87e309ec1", "start_ms": 1793334000000, "end_ms": 1793334900000, "high": 0.0224363757115038, "low": 0.0206959335748591, "volume_median_usd": 78262.35137763321, "width_pct": 8.409585053746715, "net_change_pct": 1.9999490605461245}, "buy_pressure": {"status": "not_checked", "reasons": ["not_evaluated_this_cycle"]}, "quote_rejection": null}
- ethereum:0xb62132e35a6c13ee1ee0f84dc5d40bad8d815206: {"tier": "watch", "first_base": {"pool": "0x393bde20c49a7db04b274c7fa71b9231156948e9feff46eb8f58966ee11b409f", "start_ms": 1793334000000, "end_ms": 1793334900000, "high": 0.748040723114512, "low": 0.676709086803438, "volume_median_usd": 2883.146821169459, "width_pct": 10.540960318417225, "net_change_pct": -1.4366909478423007}, "buy_pressure": {"status": "not_checked", "reasons": ["not_evaluated_this_cycle"]}, "quote_rejection": null}
- bnb:0xdd806e436dda5588bf54061c11590c77ddc87777: {"tier": "watch", "first_base": {"pool": "0xfe7ed321a4001b08f928eab725eb371025d47b37a1b180f49667a91f46c2f3cc", "start_ms": 1793332500000, "end_ms": 1793333400000, "high": 0.00258494092064184, "low": 0.00218233084645747, "volume_median_usd": 548.6979763638076, "width_pct": 18.448626835748485, "net_change_pct": 6.499838002188052}, "buy_pressure": {"status": "not_checked", "reasons": ["not_evaluated_this_cycle"]}, "quote_rejection": null}
- robinhood:0xccd0a093dcad25f8ae626d4b0f12ef0ccb2562e9: {"tier": "watch", "first_base": {"pool": "0x61ba0011831f78e53fb480b31d51018ec64393261aec8f5b085fc4ef70b75627", "start_ms": 1793334900000, "end_ms": 1793335800000, "high": 4.31460466095927e-05, "low": 3.88830207316257e-05, "volume_median_usd": 1054.4475809449973, "width_pct": 10.963720919191978, "net_change_pct": 6.441711792017024}, "buy_pressure": {"status": "not_checked", "reasons": ["not_evaluated_this_cycle"]}, "quote_rejection": null}
