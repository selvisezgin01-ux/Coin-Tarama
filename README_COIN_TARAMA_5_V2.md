# Coin Tarama 5 — V2

V1 kayıtları korunarak başlatılan, gerçek gözlemli ve ayrı kurallı deney. Getiri üstünlüğü kanıtlanmış değildir; emir göndermez. Spot giriş referansları varsayımsaldır, vadeli işlem gerçekleşmesi veya kaldıraç önerisi değildir.

## Çalışma ve veri

Tek etkin `coin-tarama-5.yml` işi V2'yi çalıştırır. `scanner-state-coin-tarama-5-v2` ayrı state dalıdır; eski dal ve V1 kaynak dosyaları korunur. İlk çalışmada V1 state'i tam ve değiştirilmeden `previous_v1` içine alınır; eski giriş fiyatları/zamanları, bekleyen bildirimler ve sonuçlar yeni sinyal sayılmaz, replay edilmez. Gerçek OI/oran geçmişleri kimlik/zaman kontrollerine tabi olarak kopyalanır. Eski aktif coinler için24s bekleme uygulanır.

Saatlik23.dakika zamanlayıcısı aynı concurrency kilidiyle en çok110dk oturum başlatır. Oturum içinde300s hedefli döngü, her döngüde kalıcı checkpoint vardır. GitHub/API/gecikme nedeniyle5dk garanti edilmez. `runs` başlangıç/bitiş/oturum/kapsam/hata kayıtları; `timing` oturum içi ve oturumlar arası p95/en uzun/>10dk aralıklarını ayrı gösterir. Bir işin başarılı durumu tüm kaynakların sağlıklı olduğunu kanıtlamaz.

MEXC ve OKX döngüleri paraleldir. Her borsada mevcut en likit60 spot+aynı borsa perpetual USDT paritesinin tamamı hedeflenir;12li rotasyon kaldırılmıştır. Mum okuması borsa başına150s yumuşak bütçeyle sınırlanır; devam eden bir HTTP isteği bu bütçeyi aşabilir. Eksik kalan coinler gözlenmiş sayılmaz; attempted/chart_evaluated/candidate_quotes ayrı raporlanır. Önce mumlar, ardından taze toplu vadeli/OI verisi, izlenen adayların oranları ve en son gerçek spot fiyatları okunur. Böylece tüm evrenin mumlarını beklerken eski fiyatla giriş yazılmaz. Açık mum, eksik/geçersiz OHLCV, bayat quote ve veri hatası olumlu sinyal üretmez. API engeli aşılmaz. Her borsanın kaynakları ve gözlem fiyatı ayrı tutulur. Aynı sembol küresel tek aday/ilk bağımsız ölçüm sayılır; borsalar arası token kontratı eşdeğerliği ayrıca kanıtlanmış sayılmaz.

Spot24s hacim>=100bin, spot/vadeli spread<=%0.5, OI parasal boyut>=1m, spot-vadeli baz farkı<=%2 korunur. Her döngüde OI geçmişi birikir. Teknik hazırlıklar türev onayı beklenmeden borsa başına en çok12lik SESSİZ havuza alınır; bunların oran/fonlama verileri her döngüde okunur. İlk oran karşılaştırmasının45–75dk ısınması gerekebilir; kaynakta gerçek olmayan geçmiş üretilmez. Küresel aktif tetik sınırı5 farklı semboldür; alt sınır yoktur.

## Fiyat ve türev koşulları

- V1 kapalı80 adet15dk/1s/4s mum ve 1s/4s trend, BTC göreli güç, son4adet15dk sıkışma, dip savunma ve satış hacmi sönümlenmesi korunur. RSI14 ve SAR açıklayıcıdır, yeni zorunlu indikatör kapısı eklenmez.
- BTC1s kapanış EMA20 altında VE EMA20 son3s düşüyorsa yeni long tetiği engellenir. Hazırlık izlenebilir.
- OI kontrat adedi, aynı kontrat ve çarpanla gerçek45–75dk önceye göre>=%3; aynı aralıktaki vadeli fiyat -%0.5 ile+%6 arasında olmalıdır. Eksik baz, kimlik değişimi, yetersiz büyüme ayrı nedenlerdir. Dolar OI artışı fiyat etkisiyle yeni kontrat artışı sayılmaz.
- Short payında>=+2yüzde puan artış zorunlu kapıdan çıkarılmıştır. En az bir bilinen kaynak onaylıysa destek puanı ve `short_confirmed` alt kümesi; gözlenmiş ama teyitsiz ve kaynak bilinmiyor durumları ayrıdır. Oranlar ortalanmaz. OKX top%5 pozisyon grubu ve Binance top%20 teminat grubu aynı evren değildir; tüm piyasa kısa pozisyon toplamı veya tasfiye kanıtı değildir. Negatif fonlama yalnız destek puanıdır.

## Üç farklı kapalı mum evresi

1. Sessiz hazırlığın direnç ve taban geçersizlik seviyesi sabitlenir. İlk hazırlıkta bildirim yoktur.
2. Sonraki kapalı15dk mum direnç üzerinde kapanır; önceki20 kapalı mum quote hacim medyanına göre>=1.5x hacim ve mumun üst%35inde kapanış gerekir. İlk kırılım bildirim değildir.
3. Daha sonraki kapalı mum direncin -0.2/+0.25ATR çevresine döner; üzerinde pozitif kapanır ve hacmi kırılımı aşmaz. Geri test tek başına bildirim değildir.
4. Geri testten sonraki en çok4 kapalı mum içinde fiyat geri test mumunun tepesini pozitif kapanışla aşmalıdır. Ancak o anda güncel quote, teknik/türev koşulları, BTC filtresi ve hedef alanı uygunsa TETİKLENDİ oluşturulur. Geçmiş mumlara giriş fiyatı/zamanı yazılmaz; gerçek yeni quote kullanılır.

Kırılım altında0.2ATR fazla kapanış veya geri test dibi-0.15ATR altında sonraki mum dip teması yapıyı iptal eder. Hazırlık6s, tetik takip süresi24s; kapanıştan sonra yeniden gözlem için24s beklenir. Veri yokluğu iptal değildir.

Güncel fiyat direnç üzerinde ve en çok0.5ATR uzağında olmalı; son kapanıştan uzaklık en çok1ATR. Stop, ilk taban geçersizliği ile geri test dibi-0.15ATR'nin yüksek olanıdır; güncel referansa göre risk<=%6. Bu seviyeler emir değildir. Hedef için geçmiş80kapalı4s mumda en az2sol/2sağ kapalı mumla doğrulanmış yukarı tepe gerekir; son iki mum pivot onayı sayılmaz. Direnç yoksa alan bilinmiyor ve tetik engellenir. %0.5 toplam maliyet varsayımı dahil `(dirence getiri - maliyet)/(stop mesafesi + maliyet)>=2` aranır. Varsayımsal hedef bu koşula göre dondurulur.

## Bildirim ve ölçüm

Yalnız gerçek tetik ile daha önce bildirilen adayın iptal/süre olayları GitHub Issue olur. Bot marker'ı ile tekrarlar uzlaştırılır. Gönderim anında2dk'dan eski olay düşürülür. Sinyalin gerçek gözlem fiyatı/zamanı yeniden yazılmaz; gönderim gecikmesi ayrıca kaydedilir. Kaydedilmiş her tetik mutlaka gönderildi demek değildir; `delivery` makbuzları ayrıdır. Gerçek aday uydurulmaz, test mesajı otomatik gönderilmez.

1/4/12/24saat getiri/BTC farkı ve tam sonraki1dk mumlardan MAE/MFE korunur. Ek stop/hedef sıra çalışması giriş dakikasını da kontrol eder: kısmi giriş dakikasında sınıra dokunma varsa sıra bilinmez; stop/hedef aynı1dk mumda ise belirsiz; ilk dokunuştan önce eksik mum varsa bilinmiyor. Sonraki boşluk daha önce kesin gözlenen dokunuş sırasını değiştirmez. Fiyat stopun altında açılmışsa daha kötü açılış varsayılır; limit/fill garantisi yoktur. Gidiş-dönüş toplam%0.2/%0.5/%1 maliyet sonrası varsayımsalR sonuçları ayrı tutulur; gerçek komisyon/kayma/fonlama değildir.

Tüm geri test girişleri ve onların short teyitli alt kümesi AYNI gerçek girişte karşılaştırılır; gözlenmiş-teyitsiz ve bilinmeyen kaynaklar ayrıca sayılır. Gruplar iç içedir ve bağımsız iki başarı gibi toplanamaz. Bu randomize deney veya nedensel katkı kanıtı değildir. En az20 farklı tamamlanmış coin olmadan ilk performans değerlendirmesi yapılmaz;20 de istatistiksel garanti değildir. V1 ile V2 takvim dönemleri farklı olduğundan fark yalnız formüle bağlanamaz. Balina girişi/büyük cüzdan işlemleri bu sürümde ölçülmez.

Doğrulama: `python -m unittest test_coin5 test_coin5_v2 -q`. Eski Coin Tarama2/3, Shortçu Kıstır, Meme ve onların bildirim ayarları değiştirilmez.
