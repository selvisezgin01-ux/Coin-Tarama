# Coin Tarama Meme V6 — ilk taban ve alım yönlü erken hacim

Kullanıcının 29 Ekim2026 talebiyle yalnız Meme taraması güncellendi. Tek aktif Meme workflow/concurrency aynıdır; yeni state `scanner-state-meme-v6`, V5 tarihsel arşivdir. Diğer taramalar ve bildirim ayarları korunur. Para/cüzdan/emir işlemi veya ücretli API yoktur.

## Koşullar

- Sağlayıcı tarafından raporlanan **MCAP50.000–500.000USD**, iki uç dahil. FDV olumlu MCAP onayı değildir. Kimliği aynı ağ+token+havuzla eşleşen DexScreener gözleminde fiyat/MCAP/likidite bildirim öncesi tekrar okunur. Bu değerler geçmiş alımlar anındaki MCAP diye sunulmaz.
- İlk uygun taban: havuz doğumundan sonraki **3tam kapalı5dkmum**; aralıksız veri, pozitif hacim, en çok%20dip/tepe genişliği, mutlak net fiyat değişimi en çok%10, son dip ilk dipten en çok%2aşağıda. İlk bulunan taban sabittir; bir sonraki sessiz bölgeyle yenilenmez. Taban60dk geçerlidir.
- Takip eden kapalı5dkmum hacmi bu tabanın medyanının en az**2katı** ve en az**500USD** olmalı. Son fiyat tabanı tutmalı; ilk kez kırılım sonrası görülen token erken hazırlık diye bildirilmez. Kırılım devam bildirimi için daha önce gerçekten teslim edilmiş birikim bildirimi gerekir.
- Güvenlik/geliştirici koşullarını sağlayan teknik kurulumdan sonra aynı kapalı5dk aralığındaki işlem yönü kontrol edilir: alım USDpayı>=%60, alım adet payı>=%60, alım-satım USDfarkı>=250,>=8işlem,>=3netalıcı işlem başlatıcı adresi, en büyük başlatıcının alım hacim payı<=%60. Bilinen geliştiricinin satış işlemi veto nedenidir. Bu eşikler deneysel, başarıyla kalibre edilmiş değildir.
- İşlemler tokenin girdiği/çıktığı tarafa göre yönlendirilir; yeşil mum alım yönü kanıtı sayılmaz. Tekrarlanan işlem kimlikleri sayılmaz, çelişen kayıtlar bilinmiyor. Son300işlem tüm pencereyi kapsamıyorsa veya toplam işlem hacmi OHLCV ile%20toleransta uyuşmuyorsa alım teyidi yoktur. Anomalous/eksik veriden olumlu teyit üretilmez. Veri yokluğu sıfır satış sayılmaz.
- Adresler bağımsız yatırımcı/insan, balina veya akıllı para diye etiketlenmez; örneklemdeki yönlü swap hacmi toplam sermaye girişi değildir.
- Erken aşama üç taban mumu ve sonraki hacim mumu nedeniyle en erken yaklaşık**20–25dk**+veri/GitHub gecikmesidir.15dk etiketi üç tam15dkmumun fiyatı taban üzerinde tutması ve ayrıca güncel kapalı5dkalım teyididir;15dkhacim teyidi diye sunulmaz.

## Korunan kurallar ve kayıtlar

Güvenlik/dev/manual harita koşulları ve ilk-pump geçmişini dışlayan eşikler değiştirilmedi. Önceden kaydedilmiş pump dışlama etiketleri silinmez; Dubble'ın yakalanması garanti veya amaç fonksiyonu değildir. Açılış fitillerinin daha esnek yorumlanması bu değişikliğe dahil edilmedi. EskiV5 giriş fiyatları/zamanları, ölçümleri, teslimat ve pending kayıtları `previous_v5` arşivindedir; V6 geçmişe sinyal yazmadan yeni gerçek gözlemle başlar. Bekleyen eski mesajlar yeni sürüm diye tekrar gönderilmez. Kaynak429beklemesi taşınır, kısıt aşılmaz.

MCAP, hacim katı, kapalı5dk alım/satım/fark ve başlatıcı sayısı, ağ ve kopyalanabilir tam kontrat bildirimde gösterilir. Kimlik/güvenlik raporu tüm sahte tokenları dışladığı veya resmî kontratı kanıtladığı iddiası değildir. Satış kısıtı, yetki, sahip yoğunlaşması/dev ve mevcut kaynak kontrolleri aynen zorunludur; eksik kritik veri olumlu aday değildir.

## Çalışma ve doğrulama

110dk sınırlı GitHub oturumunda hedef300sn aralıktır. Global20Geckoistek/tur ve12.5sn aralık korunur;1istek alım akışı kontrolüne ayrılır. Dolayısıyla bütün ağlardaki bütün tokenlar her tur incelenemez; bütçe/kapsam ve kaynak hataları görünür kalır. Diğer CEX taramalarının zamanlaması bu güncellemeyle düzeltilmedi.

Eski85güvenlik/mum,35V5 ve yeniV6testleri ayrı süreçlerde çalışır. V6 testleri kapalı mum, sabit ilk taban, alım miktarı/adet ayrımı, tek adres, yinelenen/eksik/ters yönlü/anomalous işlem, kaynak kısılması, MCAP sınırları/FDV, güvenlik önceliği, eski fiyat/latch/bekleme koruması ve gerçek Issue gövdesini kapsar. Canlı denemede aday uydurulmaz; sıfır aday olabilir. Sabit miktarlı kağıt satış deneyi korunur, gerçek emir veya garanti net kâr yoktur.

Kaynak: [sağlayıcının işlem veri yapısı ve son300işlem sınırı](https://docs.coingecko.com/reference/pool-trades-contract-address). Aynı kamu GeckoTerminal uç noktası mevcut adaptörle kullanılır; Pro API satın alınmadı.
