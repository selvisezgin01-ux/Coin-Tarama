# Coin Tarama Meme V7

V6 keşif boşluğu ve ilk pump koşullarından sonra kullanıcı onayıyla açılan ayrı deney. Beş ağ: Solana, Ethereum, BNB Chain, Robinhood ve HyperEVM. Emir veya özel anahtar işlemi yoktur.

- Sürekli toplayıcı: herkese açık sağlayıcının yeni havuz kimliklerini SQLite'a kaydeder. Hedef Solana 60sn, diğer ağlar180sn; sayfalama, önbellek, erişim, çağrı sınırı ve bilgisayar durumu gerçek aralığı uzatabilir. Sayfa sınırı ve uyku boşluğu kayda girer. Her kimlik korunur; son iki saatlik kimlik feed'i ayrı `scanner-feed-meme-v7` dalına yayımlanır. Ham keşfin normalize edilen kimlikleri ve geçersiz satır sayıları yerel audit'tedir.
- GitHub worker: `scanner-state-meme-v7`. Sürekli feed bayatsa sınırlı fallback açıkça gösterilir. Ayrıntılı quote/mum/akış okumaları bütçelidir; tam zincir veya tüm tokenlerin ayrıntılı incelenmesi iddia edilmez.
- Çok genç tokenler için ayrı quote kapasitesi, eski/aktif tokenler için ayrı bölüm vardır. 180kota yüzünden kimlik silinmez. Ledger ve karar geçişleri state'te saklanır; veri alınamayan ve bütçe bekleyenler görünür.
- 🟡 erken radar: gerçek MCAP50–500bin USD, likidite>=10binUSD, son5dk faaliyet ve alım AD EDİ payı. Alım hacmi, güvenli token veya giriş değildir. Kritik güvenlik bilinmeyebilir ve başlıkta açıkça belirtilir. Bildirim sınırı döngüde2/saatte6; söz konusu sınırlar veri toplama sınırı değildir.
- 🟢🎯 otomatik giriş: ilk GERÇEK V7 uygunluk gözleminden sonra iki tam kapalı5dk taban +bir ayrı kapalı5dk hacim mumu. Tabana yakın olumlu kapanış,>=2x hacim ve aynı pencerenin doğrulanabilen alım yönlü örneği. Güvenlik/dev tamlığı korunur; manuel harita ve orijinal kontrat kontrolü bekler. Likit ilk tabanın geçmiş MCAP'i uydurulmaz. Yeni fiyat/kotasyon kontrolü önceki gözlem fiyatını değiştirmez.
- İlk fiyattan %25 yükseliş yasağı yeni modelde kullanılmaz. Uygunluk sonrası erişilen geçmişte %35üzeri sert düşüş, ilk taban kaybı ve tabandan %8uzama elenir. Aynı tokenin sonraki havuzu yeni bağımsız giriş sayılmaz. Bu eşikler deneysel tercihlerdir.
- 🔵 güçlenme: gerçek giriş makbuzundan sonra başlayan bir tam15dk mumun korunmuş taban üzerinde güçlü kapanması. Aynı girişin devamıdır.
- Giriş için100USD gösterge alış/satış rotası ve<=%3roundtrip kotasyon kaybı istenir. USDC1USD kabul edilmez. Rota, vergi/gas/fill veya anlık satış garantisi değildir. Stop taban altı, risk mesafesi%0.5–8, hedef%1ilave maliyet varsayımıyla2Rprojeksiyondur; direnç alanı teyidi değildir.
- Sabit kotasyon token miktarı sonraki satış kotasyonlarıyla ölçülür.15/30dk,1/3/6/24saat sonuçları ve%0.2/%0.5/%1ilave maliyet senaryoları kaydedilir; gerçekleşmiş net kâr Nonekalır. Ara yol ve stop/hedef sırası bilinmeyebilir.50–100farklı kontrat ilk inceleme grubudur, kârlılık ispatı değildir.
- Yapı/likidite/risk/örnekte alım adedi zayıflaması, gösterge hedef veya zaman aşımı mesajları yalnız gerçekten giriş Issue makbuzu olan tokenlere gider.

## Arşiv

V6 eski dal ve SHA'sında korunur. V7 `archive` ve `legacy_v6` özgün referansları saklar; V6pump eleme latches'i yeni formül başarısı veya geriye dönük V7alarmı yapılmaz. Eski aday gönderilmez. Coin2/3/5,1coin ve Shortçu değişmez.

## Yerel servis ve sunucu

`python meme_v7_service.py --data-dir collector_data` yalnız yerel keşif yapar. `--publish` ayrı sabit feed dalını yayımlar; `GH_TOKEN` çalışma ortamından alınır, kod/rapor/state'e yazılmaz. Tek süreç kilidi, restart ve kalıcı SQLite kullanır. Yerel kurulum mevcut Git Credential Manager kimliğini bellekte kullanan özel başlatıcı üzerinden çalışır. Bilgisayar uyuduğunda/kapanınca durur; otomatik kullanıcı girişinde yeniden başlayabilir. Bu kurulum24saat sunucu değildir.

Gerçek sunucuda: `docker build -f Dockerfile.meme-v7 -t coin-tarama-meme-v7 .`, ardından mevcut sunucunun güvenli secret yöntemiyle GH_TOKEN ortamı ve kalıcı `/data` hacmi verilerek `--restart unless-stopped` kullanılır. Sunucu/hesap satın alınmaz veya tahsis edilmez. Hosting erişimi sağlandığında bu paket taşınabilir. Hiçbir özel cüzdan anahtarı gerekmez.

Bildirimler gerçek GitHub bot Issue'larıdır. Issue yaratılması telefon sesi veya okunma kanıtı değildir. Sahte testler gerçek aday sayılmaz.
