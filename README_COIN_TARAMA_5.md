# Coin Tarama 5

Bağımsız ve deneysel hazırlık / tetik / iptal taraması. MEXC ve OKX spot USDT pariteleri ve aynı borsanın aktif USDT perpetual kontratları. Emir, özel hesap, bakiye veya cüzdan erişimi yok. Coin Tarama2/3/Meme/Shortçu Kıstır'ın kodları ve durum dalları değiştirilmez; onların dört saatlik listeleri beklenmez.

## Veri ve kapsam

Yeni `.github/workflows/coin-tarama-5.yml` yaklaşık5dk planlanır; GitHub başlangıcı gecikebilir veya atlayabilir. Tam zamanlı/realtime servis değildir. En likit en çok60 uygun parite/borsa; her çalışmada12 dönüşümlü parite ve tüm aktif adaylar okunur. Tüm piyasa/her parite her5dk taranıyor değildir. Aktif aday sınırı küresel5coin; aynı sembol iki borsada iki aday sayılmaz. Evren top60 içindeki ilk tam dönüş normal şartta yaklaşık25dk; GitHub/API hataları uzatabilir. Bütün60 paritenin oranı her döngüde çekilmez. Fiyat hazırlığı veya aktif takip varsa oranlar istenir; geçmiş koşul geçişleri geriye doldurulmaz.

Spot24s hacim>=100bin USDT, spot ve vadeli makas<=%0.5, aynı borsa OI parasal boyutu>=yaklaşık1mUSD/USDT, spot/vadeli fark<=%2. MEXC OI değeri tahmini USDT, OKX sağlayıcıUSD; kontrat adedi artışı fiyat etkisinden ayrılır. Stable/leveraged/hisse metadata elemeleri mevcut sürümlerin listelerini yalnız okur. Kimlik tam exchange base kodu; cross-venue token kontrat kimliği doğrulanmış sayılmaz,1000token isim dönüşümü yok.

## Dondurulmuş ilk kurallar

- Son80 tam kapalı15dk/1s/4s mum. Eksik/ara/açık/güncel olmayan mum olumlu sinyal üretmez. MEXC saatlik API aralığı `60m`, OKX `1H`; quote hacmi kullanılır.
-4s kapanış EMA20'nin1ATR'den fazla altında olmayacak;1s kapanış EMA20'nin0.5ATR'den fazla altında olmayacak, EMA20 son3saatte0.2ATR'den fazla düşmeyecek. Son1saat BTC göreli getirisi negatif olmayacak. RSI14 ve SAR yalnız açıklayıcı bağlamdır, zorunlu kapı değildir.
- Hazırlık: son4kapalı15dk mum kutusu<=3ATR ve<=%8, net değişim<=1ATR, sonraki iki mum dipleri önceki iki mum dibini0.2ATR'den fazla aşındırmayacak. Düşüş mumlarının quote hacmi önceki8mum düşüş hacim medyanına göre artmayacak; son kutuda düşüş mumu yoksa satış baskısı koşulu sağlanır. Bu gerçek alıcı birikimi kanıtı değildir.
- Gerçek45–75dk önceki OI kontrat adedine göre en az%3 artış; vadeli fiyat değişimi-%0.5 ile+%6. Aynı kontrat/çarpan zorunlu. İlk gözlemde tarihsel OI uydurulmaz.
- Aynı45–75dk aralığında **en az bir kaynak grubunun short payında+2yüzde puan artış**. Sabit `%60 short` kapısı yok. İlk oran gözlemi başlangıçtır; aynı sağlayıcı zamanındaki revizyon eski bazı değiştirmez. Bir kaynak bilinmiyorsa diğerinin açık onayı kullanılabilir; iki kaynak tersse ayrışma mesajda görünür. Hiçbiri onaylanmıyorsa hazırlık oluşmaz.
- OKX açık pozisyon değeri en büyük%5grubu ve Binance teminat bakiyesi en büyük%20grubunun **pozisyon** dağılımları, ayrı kaynaklar. Piyasa geneli veya MEXC toplamı, hesap adedi veya mutlak short parasal boyutu değildir. Oran artışı hedge/üyelik değişimi/long azalmasından gelebilir. OI+oran short açılışı/likidasyon kanıtı değildir. Binance anonim kamu erişimi engellenirse durulur; anahtar/erişim veya bölgesel engel aşılmaz.
- Negatif fonlama zorunlu değildir; biliniyorsa sıralamada+1ek puan. Her onaylı pozisyon kaynağı+2puandır. Bu betimsel önceliktir, başarı olasılığı değildir.

## Durumlar ve bildirim

Hazırlık anında kutu üstü direnç ve kutu altı-0.15ATR geçersizlik sabitlenir. Hazırlık mesajı kırılım teyidi değildir. Sonraki kapalı15dk mum sabit direncin üstünde, önceki20mum medyanına göre>=1.5x quote hacim ve mum üst%35kısımda kapanırsa tetik aranır. Kırılım kaydı sonrası ayrı bir kapalı mum seviyeye -0.2/+0.25ATR içinde geri dokunup üstünde pozitif kapanır ve kırılım hacmini aşmazsa geri test alternatifi vardır.

Tetikte teknik yapı/pozisyon onayı devam etmeli; güncel spot direnç üstünde ve en fazla1ATR uzakta, son kapalı mumdan en fazla1ATR uzakta olmalı. Geçersizliğe mesafe en çok%6. Son24kapalı4s mumdaki en yakın yukarı tepe bulunursa mesafe en az2R olmalı; daha yukarı tepe gözlenmemişse alan **bilinmiyor**, kesin2R getirisi değildir. Risk mesafesi bir stop emri veya stop gerçekleşme garantisi değildir.

Doğrulanmış güncel fiyat veya hazırlıktan sonraki kapalı mum sabit geçersizlik altına inerse **İPTAL**; hazırlık6saat veya tetikten24saat dolarsa **SÜRE DOLDU**. Veri yokluğu iptal sayılmaz; son gerçek gözlem saati raporda kalır. İptal/süre mesajı ancak daha önce bildirilen aday için gönderilir. Süre sonunda24saat yeniden giriş beklemesi. Pending işaretleriyle bot Issue uzlaştırılır; destek kaybından sonra eski hazırlık mesajı gönderilmez. GitHub bildirim kanalı mevcut `NOTIFICATION_CHANNEL=github_issue`; `COIN_NOTIFY_USER` kullanıcıyı etiketler. Test mesajı gerçek sinyal değildir. Yaklaşık5dk kontrol frekansı garanti değildir; ana Coin Tarama5 eski Shortçu oran takibinden bağımsızdır.

## Ölçüm

Kendi `scanner-state-coin-tarama-5` state/raporu. İlk hazırlık ve ilk tetik referansları ayrı gerçek spot fiyatı/saatinden başlar; tetiğe hazırlık fiyatı giriş olarak kopyalanmaz. Aynı sembol/evre tekrarı bağımsız örnek eklemez. İlk BTC referansı eksikse kayıt sonraki gerçek gözlemden başlar, geriye yazılmaz.

1/4/12/24saat getirisi, BTC farkı, tam giriş sonrası ilk1dk mumdan MAE/MFE, toplam%0.2/%0.5/%1 maliyet duyarlılığı. Eski ayrı deneyin salt ölçüm fonksiyonları kullanılır; hiçbir Shortçu state alanına yazılmaz. Eşlenmiş kontrol coinleri bu sürümde yok. Giriş dakikasının kalan parçası MAE/MFE dışıdır. Eksik ara mumda yol bilinmiyor, eksik fiyat sıfır getiri değildir. Döngüde en fazla2kayıt ölçülür; birikim/gecikme raporda görünür. Sonuçlar stop/limit emir simülasyonu veya net işlem kârı değildir. Olası hazırlık sonuçları ile tetik sonuçları toplanarak iki bağımsız başarı sayılmaz. En az20farklı coinlik tamamlanmış tetik ölçümünden önce üstünlük iddiası yapılmaz; bu sayı istatistiksel kanıt değildir. Sonuçlara göre sürekli eşik ayarı yapılmaz, yeni kural yeni sürüm gerektirir.

Kaynaklar: [MEXC Spot genel veri ve aralıklar](https://mexcdevelop.github.io/apidocs/spot_v3_en/), [OKX kamu piyasa API](https://www.okx.com/docs-v5/en/), [Binance pozisyon oranı](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio), [OKX grup oranı](https://www.okx.com/en-us/help/how-do-i-use-the-top-position-long-short-ratio-indicator), [GitHub zamanlama gecikmesi](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).
