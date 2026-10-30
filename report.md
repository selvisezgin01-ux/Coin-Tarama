# Coin Tarama Meme — V6

Son çalışma: 30.10.2026 06:30 Türkiye saati.

**Deneysel DEX izleme. Tüm yeni tokenleri kapsamaz ve yükseliş garantisi vermez.**

Kapsam: Solana, Ethereum, BNB Chain, Robinhood (Pons dahil), HyperEVM. Pons ayrı bir ağ değildir.

**Hedef: ilk yükseliş öncesi oluşum/birikim.** Yeni aday yalnız birikim evresinde alınır; ilk kırılım ancak daha önce bildirilen birikimin devamı olarak izlenir. Trend listesi aday kaynağı olarak kullanılmaz. **Cüzdan haritası manuel kontrol bekler.** Kritik kontrat/geliştirici verisi eksik tokenler bildirilmez.

Geçmişin tamamındaki fitiller ve açık mum dahil gözlenen dipten tepeye yükseliş %25 üzerindeyse, ilk fiyatın %10 üzerine uzamışsa veya tepeden %15 üzeri düşmüşse elenir. Bu eşikler deneysel tercihlerdir. Havuz başlangıcı, ara mumlar veya güncel mum yoksa ilk oluşum teyitsizdir. Eski pump sonrası yataylaşma yeni aday sayılmaz.

GMGN kullanılmaz. Solana: RugCheck + GoPlus Solana; desteklenen EVM ağları: GoPlus. GMGN’nin tüm sniper/bundler etiketleri ve eksiksiz geliştirici geçmişi sağlanmaz. Teknik risk ön elemesi tokenin resmî/orijinal proje kontratı olduğunu kanıtlamaz.

Yeni havuz yaşı tokenin yaratılma yaşı değildir. Market cap sağlayıcı bildirimi olarak, FDV ise açıkça ayrı değer türü olarak gösterilir. Geliştirici teyidi yalnız belirtilen 45 dakikalık işlem penceresindeki raporlanan adrese aittir; ömür boyu hiç satış yapmadığı veya başka cüzdan kullanmadığı anlamına gelmez.

| Ağ | Güncellenen token | Piyasa ön elemesi | Mum incelenen | Ön eleme / manuel harita bekliyor | İnceleme | Erişim/veri hatası |
|---|---:|---:|---:|---:|---:|---:|
| HyperEVM (HYPE) | 32 | 0 | 0 | 0 | 0 | 0 |
| Solana | 58 | 1 | 0 | 0 | 0 | 0 |
| Robinhood | 56 | 3 | 1 | 0 | 0 | 2 |
| Ethereum | 33 | 0 | 3 | 0 | 0 | 0 |
| BNB Chain | 56 | 0 | 2 | 0 | 0 | 1 |

Bu çalışmada aday olmayan mum incelemeleri (token listesi değildir):
- 1: Daha eski havuz geçmişi kapsam dışı
- 2: Önceden yükseliş / uzun fitil görülmüş; Başlangıç fiyatından fazla uzaklaşmış
- 1: Önceden yükseliş / uzun fitil görülmüş; Tepeden düşüş sonrası yapı elenmiş
- 1: Havuz başlangıç mumları eksik
- 1: need_three_base_bars_and_one_volume_bar

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

- Robinhood: SIC: gecko_request_reserved_for_buy_pressure; PMHFR30: gecko_request_reserved_for_buy_pressure
- BNB Chain: UNSAFU: gecko_request_reserved_for_buy_pressure


<!-- meme-v6-pipeline -->

## V6 keşif, aşamalar ve gerçek zamanlama

Gözlem kaydı alım adayı değildir. Tüm piyasa ön koşulları geçmeden sınırlı mum OKUMA yapılır; olumlu aday için eski piyasa/güvenlik/dev/ilk-pump şartları aynen zorunludur.

Yeni havuz keşfi en çok2sayfa/ağ;15dk altı havuzlar uygun yaşa yaklaşırken öncelikli yenilenir. Bütçe dışında kalan kapsam ve veri boşluğu gizlenmez.

- hyperevm: {"refreshed": 32, "eligible": 0, "evaluated": 0, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 32, "waiting_min_age": 0, "market_pass": 0, "market_failed": {"liquidity": 31, "valuation": 31, "volume15": 32, "transaction_flow15": 32, "liquidity_to_valuation": 1}, "market_unknown": {}, "data_inspection_possible": 0, "ohlcv_read": 0, "ohlcv_attempted": 0, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 32}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 32}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793292540000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793330496779, "next_checkpoint_ms": 1793330796804, "oldest_returned_ms": 1793292540000, "valid_page": true}, "reasons": {}}
- solana: {"refreshed": 58, "eligible": 1, "evaluated": 0, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 58, "waiting_min_age": 28, "market_pass": 1, "market_failed": {"pool_age": 28, "valuation": 52, "liquidity": 54, "volume15": 22, "transaction_flow15": 32, "liquidity_to_valuation": 23, "liquidity_withdrawal": 13}, "market_unknown": {}, "data_inspection_possible": 0, "ohlcv_read": 0, "ohlcv_attempted": 0, "ohlcv_budget_waiting": 0, "security_checked": 0, "buy_pressure_status": {"not_checked": 58}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 58}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793330701000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793330673000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793330673000, "valid_page": true}, "reasons": {}}
- robinhood: {"refreshed": 56, "eligible": 3, "evaluated": 1, "qualified": 0, "review": 0, "errors": ["SIC: gecko_request_reserved_for_buy_pressure", "PMHFR30: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 56, "waiting_min_age": 21, "market_pass": 3, "market_failed": {"pool_age": 23, "liquidity": 44, "valuation": 51, "volume15": 41, "transaction_flow15": 47, "liquidity_withdrawal": 5, "liquidity_to_valuation": 12}, "market_unknown": {}, "data_inspection_possible": 4, "ohlcv_read": 1, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 2, "security_checked": 0, "buy_pressure_status": {"not_checked": 56}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 56}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793330132000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793329113000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793329113000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price": 1}}
- ethereum: {"refreshed": 33, "eligible": 0, "evaluated": 3, "qualified": 0, "review": 0, "errors": [], "funnel": {"records": 33, "waiting_min_age": 2, "market_pass": 0, "market_failed": {"valuation": 33, "liquidity_to_valuation": 33, "transaction_flow15": 28, "liquidity_withdrawal": 14, "pool_age": 3, "liquidity": 20, "volume15": 18}, "market_unknown": {}, "data_inspection_possible": 13, "ohlcv_read": 3, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 9, "security_checked": 0, "buy_pressure_status": {"not_checked": 33}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 33}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793328551000}], "covered_to_previous_checkpoint": true, "gap_or_initial_window_uncovered": false, "previous_checkpoint_ms": 1793330496778, "next_checkpoint_ms": 1793330796803, "oldest_returned_ms": 1793328551000, "valid_page": true}, "reasons": {"need_three_base_bars_and_one_volume_bar": 1, "initial_pool_history_missing": 1, "earlier_pool_history_not_covered": 1}}
- bnb: {"refreshed": 56, "eligible": 0, "evaluated": 2, "qualified": 0, "review": 0, "errors": ["UNSAFU: gecko_request_reserved_for_buy_pressure"], "funnel": {"records": 56, "waiting_min_age": 16, "market_pass": 0, "market_failed": {"pool_age": 17, "liquidity": 40, "valuation": 50, "volume15": 34, "transaction_flow15": 47, "liquidity_to_valuation": 13, "liquidity_withdrawal": 15}, "market_unknown": {"liquidity": 2, "valuation": 2}, "data_inspection_possible": 3, "ohlcv_read": 2, "ohlcv_attempted": 3, "ohlcv_budget_waiting": 1, "security_checked": 0, "buy_pressure_status": {"not_checked": 56}, "buy_pressure_reasons": {"not_evaluated_this_cycle": 56}}, "discovery": {"pages": [{"page": 1, "returned": 20, "oldest_created_ms": 1793330016000}, {"page": 2, "returned": 20, "oldest_created_ms": 1793329202000}], "covered_to_previous_checkpoint": false, "gap_or_initial_window_uncovered": true, "previous_checkpoint_ms": null, "next_checkpoint_ms": null, "oldest_returned_ms": 1793329202000, "valid_page": true}, "reasons": {"first_rise_already_observed,already_extended_from_initial_price": 1, "first_rise_already_observed,post_peak_rebound_excluded": 1}}

Zamanlama: {"started_ms": 1793330796726, "finished_ms": 1793331022402, "duration_seconds": 225.676, "github_run_created_at": "2026-10-30T01:23:27Z", "worker_started_ms": "1793329295456", "github_job_started_at": "2026-10-30T03:01:20Z", "cadence": {"interval_count": 203, "p95_minutes": 5.6189, "max_minutes": 6.028783333333333, "meets_7m_target": true, "full_24h_observed": false}}

İstek durumu: {"api.geckoterminal.com:ok": 19, "api.dexscreener.com:ok": 10, "gecko:reserved_for_buy_pressure": 3}; sağlayıcı429bekleme bitişi: 1793221779011

GitHub worker oturumları sınırlıdır. Çalışan oturum içinde hedef5dk; oturum başlangıcı/yenilenmesi gecikebilir. Gerçek aralıklar yukarıda;24saat tamamlanmadan kesintisiz5dk doğrulandı denmez. EskiV5 paralel taranmaz, referansları previous_v5 içinde korunur.

## Sabit miktarlı gösterge satış deneyi

100/500USD notional için ilk gözlem fiyatından hesaplanan token miktarı sabittir; alım gerçekleşmesi değildir. Aynı miktarın sonraki gösterge satış rotası sorgulanır. USDC1USD varsayılmaz. Alım maliyeti, tüm vergiler,gas veya gerçekleşme bilinmiyorsa netkâr bilinmiyor kalır. Stop-%10/hedef+%20/60dkzaman aşımı yalnız gözlenen satış kotasyonları üzerinde sabit deneydir; aradaki5dk yol ve stop-hedef sırası garanti edilmez.


Ölçüm hataları: []

## İlk taban ve alım yönlü erken hacim

MCAP:50.000–500.000USD; FDV MCAP yerine onay sayılmaz. 3tam5dk taban mumu ve sonraki kapalı5dkhacmi taban medyanının>=2katı aranır. Aynı kapalı5dk işlem örneğinde alım hacim/adet payı>=%60, alım-satım USD farkı>=250,>=8işlem,>=3netalıcı başlatıcı ve tek alıcı payı<=%60. Son300işlem pencereyi kapsamaz veya OHLCVhacmiyle uyuşmazsa bilinmiyor. Bu adresler bağımsız kişi/servet kanıtı değildir. En erken20–25dk+veri/çalışma gecikmesi. Güvenlik/dev/ilk-pump kapıları korunur.

- solana:dhf983GAxb7zTMkHhDeo2hSs1eWh1byFfm7N3Q8pump: {"tier": "watch", "first_base": {"pool": "5gFCikucbXF7xvYyUTFJtB6xcp8AsvafXCHmuGnWEzXe", "start_ms": 1793324700000, "end_ms": 1793325600000, "high": 0.07286788332908234, "low": 0.07184183998303346, "volume_median_usd": 475.9467380776317, "width_pct": 1.428197476973292, "net_change_pct": 0.8325869837604971}, "buy_pressure": {"status": "not_checked", "reasons": ["not_evaluated_this_cycle"]}, "quote_rejection": null}
- ethereum:0xc944e90c64b2c07662a292be6244bdf05cda44a7: {"tier": "watch", "first_base": {"pool": "0xdf074e89fcdfbd5ddfa3030394e9071dcc765fdf8c5e61495b799a34a6781e6c", "start_ms": 1793324100000, "end_ms": 1793325000000, "high": 0.0191176338254855, "low": 0.0184920261741979, "volume_median_usd": 3416.789307771583, "width_pct": 3.3831211647348702, "net_change_pct": 1.5251430570187186}, "buy_pressure": {"status": "not_checked", "reasons": ["not_evaluated_this_cycle"]}, "quote_rejection": null}
- ethereum:0x8207c1ffc5b6804f6024322ccf34f29c3541ae26: {"tier": "watch", "first_base": {"pool": "0x9ed5944c585996c054a04f1c874d35c8ae816b123bf07db67b112feb1da15ecb", "start_ms": 1793327400000, "end_ms": 1793328300000, "high": 0.0213248241257274, "low": 0.0205891939732403, "volume_median_usd": 14213.00070094906, "width_pct": 3.572894370917079, "net_change_pct": -0.40220553406548065}, "buy_pressure": {"status": "not_checked", "reasons": ["not_evaluated_this_cycle"]}, "quote_rejection": null}
