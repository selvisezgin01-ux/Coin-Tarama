# Coin Tarama5 — V3 geniş erken radar

PARTI/LSK incelemesinden sonra kullanıcı erken yükseliş odağını koruyarak revizyonu açıkça onayladı. V2'nin aynı borsada spot+perpetual kesişimi ve statik60 hacim sırası erken fırsatları evren dışında bırakıyordu. V3 bu iki kapsam kısıtını kaldırır; yükselişin ilk hacimlenmesini izleme uyarısı ve geri test sonrası giriş değerlendirmesi ayrı evrelerdir. Henüz kanıtlanmış kâr avantajı değildir; emir göndermez, kaldıraç/pozisyon büyüklüğü belirlemez.

## Dört ayrı pazar ve gerçek kapsam

- MEXC SPOT, MEXC PERP, OKX SPOT, OKX PERP katalog/ticker/mum/fiyatları ayrıdır. Spotun uygun vadeli kontratı olması gerekmez; vadeli-only parite kendi mumlarıyla incelenir. Spot fiyatı vadeli ölçüme taşınmaz. Sembol benzerliği kontrat eşdeğerliğinin bağımsız doğrulaması değildir.
- Her döngüde bütün uygun aktif USDT paritelerinin toplu fiyat/hacim bilgisi okunur. Stable, metadata ile bilinen kaldıraçlı ürünler ve tam eşleşen bilinen hisse tokenleri elenir. MEXC perpetual type2 veya Stock/TradFi/ETF/forex/commodity konsept etiketli kontratlar dışlanır; bu metadata dışında yeni/bilinmeyen finansal ürünlerin tamamı için sınıflandırma garantisi değildir. Toplam24s hacim en az100bin USDT, radar makası en çok%0.5. MEXC amount24/spot quoteVolume ve OKX spot volCcy24h quote cirosudur; OKX swap base volCcy24h×güncel last yaklaşık USDT olarak açıkça etiketlenir.
- Ayrıntılı mum okuması pazar başına20dinamik öncelik+10dönüşümlü parite ve mevcut aktif izlemelerdir; en çok40parite ve100s yumuşak zaman bütçesi vardır. Devam eden HTTP isteği bütçeyi aşabilir. Her coin her5dk ayrıntılı incelenmiş sayılmaz; kısa pump yine kaçabilir. Her pazarın aktif katalog, ticker ön elemesi/ret nedeni, seçilen kimlikleri ve HER seçilmiş kimliğin mum/eleme/bütçe nedeni state'te saklanır.
- Öncelik aynı paritenin gerçek4–10dk önceki fiyatına göre yaklaşık5dk getiriyi, rolling24s ciro değişimini ve sınırlandırılmış24s değişimi kullanır. Rolling24s hacim farkı **gerçek5dk işlem veya alım hacmi değildir**; yalnız sıralama vekilidir. İlk gözlemde5dk geçmiş uydurulmaz; bootstrap24s veri+rotasyonla başlar. Aday olabilmek için gerçek kapalı15dk mum hacmi ayrıca doğrulanır.

## Erken radar

64tam kapalı15dk mum, ardışık zaman ızgarası ve taze kapanış gerekir. Açık/eksik/çelişkili mum olumlu sinyal üretmez. Son mum quote hacmi önceki20mum medyanının en az2katı, kapanış pozitif ve mum aralığının üst%40ında olmalıdır. Ayrıca önceki8mumun tepesini aşma VEYA önceki mum tepesinin/EMA20'nin üzerinde erken dönüş VEYA dar yatay kutuya yakın hacimlenme gerekir. Fiyat EMA20'den4ATR üzerindeyse veya son bir saatte%12'den fazla yükselmişse yeni erken aday elenir. Böylece sonradan görülmüş pump ilk oluşum diye yeniden adlandırılmaz.

**ERKEN RADAR — GİRİŞ TEYİDİ DEĞİL** mesajı gerçek gözlenen quote fiyatı/saatini taşır; geri test henüz yoktur. Başlangıçtabanı ve direnç sabitlenir. En çok3yeni radar/döngü,6radar/saat ve20aktif izleme vardır; kotanın dışında fırsat kaçabilir. Aynı sembolün farklı pazarları eşzamanlı yeni bağımsız aday gibi bildirilmez; en önce seçilen gerçek pazar fiyatı korunur. Bu, adres/sözleşme kimliği doğrulaması değildir.

Son fiyat kontrolünde kapanıştan1ATR'den fazla yukarı kaçış,0.5ATR'den fazla geri çekilme, taban desteği kaybı veya kırılan seviye altında0.2ATR fazla gerileme varsa yeni radar bildirilmez. Böylece mum güçlü kapanmış olsa da sonradan yapısı kaybolmuş fiyatla eski uyarı gönderilmez.

4s trend erken radar kapısı değildir, destek/uyarıdır. RSI/SAR için yeni zorunlu filtre eklenmez. OI/fonlama zorunlu değildir: MEXC perpetual holdVol verisi aynı kontrat/çarpanın gerçek45–75dk geçmişiyle karşılaştırılabilir; spot ve desteklenmeyen OI alanları bilinmiyor/uygulanamaz kalır. Ham fonlama varsa dönemi teyit edilmediğinden8saate ölçekli veya ödenmiş tutar sayılmaz. Bu sürümün toplu ticker akışında OKX OI ve seçili grup long/short oranları alınmaz; bilinmiyor kalır. Ayrı Shortçu Kıstır'ın mevcut oran takibi değişmez. OI artışı yeni short açılışı/likidasyon/balina kanıtı değildir.

## Ayrı giriş teyidi

İlk görülen kapalı kırılım bir giriş fiyatı değildir; yalnız o anda gerçekten gözlendiği kaydedilir. Giriş için sonraki farklı kapalı15dk mumda direnç çevresine(-0.3/+0.5ATR) daha düşük/eşit hacimli geri test ve daha sonra geri test mumunun tepesinin üzerinde pozitif kapanış aranır. Teyit geri testten en çok1s sonra olabilir. Geçmiş mum kapanışına giriş yazılmaz; o sıradaki taze kotasyon kullanılır.

Giriş: makas<=%0.3, destek mesafesi en çok%3; güncel fiyat geri test tepesi ile+0.5ATR arasında ve ilk kırılım seviyesinden en çok2ATR uzakta olmalı. Stop, ilk taban geçersizliği ile geri test dibi-0.15ATR'nin yüksek olanıdır. Destek mesafesi hesap sermayesinin%3'ü anlamına gelmez. BTC son kapalı1s mumda en az%2 düşmüşse veya BTC bağlamı bilinmiyorsa yeni giriş engellenir; erken radar ayrı kalır.

Planlama toplam maliyet varsayımı%0.5; hedef `(stop mesafesi + maliyet)×2 + maliyet` gross getirisini sağlayacak şekilde projekte edilir. Geçmiş kapalı1s/4s iki sol/iki sağ mumla teyitli daha yakın direnç varsa giriş reddedilir. Yukarıda direnç gözlenmediyse hedef yalnız2R projeksiyonudur; direnç/alan bilinmiyor etiketi açıkça bildirilir. Bu, gerçekleşme veya kazanç garantisi değildir.

Gerçek yeni quote veya hazırlıktan sonraki kapalı mum taban desteğine dokunursa iptal; kırılım altında0.3ATR fazla kapanış veya geri test desteği kaybı iptal olur. Radar6s, tetik24s takip edilir. Veri yokluğu yapı kaybı değildir; süre dolması fiyat bilinmiyor notuyla ayrıca kaydedilebilir. Sonlandırılan pazar için6s yeniden giriş beklemesi uygulanır; aynı eski sinyal mumu tekrar kullanılmaz.

## Bildirim ve deney kayıtları

Mevcut GitHub bildirim kanalı sürer; bot marker'ı ile tekrarlar uzlaştırılır. Mesajlar ERKEN RADAR / GERİ TEST GİRİŞ TEYİDİ / İPTAL / SÜRE olarak ayrıdır.2dk'dan eski olaylar gönderilmez; daha önce bildirilmemiş adayın iptal/süre mesajı üretilmez. Gönderim checkpointi ve makbuz ayrı saklanır. Test mesajı kendiliğinden gönderilmez. Aynı evrede aynı sembolün ilk gerçek ölçüm referansı değişmez; yeni pazar/evreleri iki bağımsız başarı gibi toplanmaz.

1/4/12/24s sonuçları aynı pazarın gerçek1dk OHLCV serisinden ölçülür; spot/vadeli karıştırılmaz. Radar yalnız gözlem referansıdır; giriş tetiği kendi gerçek fiyatından ayrı ölçülür. BTC farkı, tam sonraki1dk mumlarla MAE/MFE ve%0.2/%0.5/%1 toplam maliyet duyarlılığı tutulur. Girişte stop/hedefin hangisine önce dokunulduğu da saklanır: giriş dakikası kısmi ve sınıra dokunmuşsa bilinmiyor; iki sınır aynı1dk mumda ise belirsiz; ilk dokunuştan önce eksik mum varsa bilinmiyor. Açılış stopun altındaysa daha kötü açılış kullanılır. Bunlar gerçekleşmiş emir/fill/net kâr veya fonlama ölçümü değildir.

Ölçüm en çok2kayıt/döngü; kuyruk gecikmesi raporlanır. Az sayıda kazanan, radar getirisi veya81/124testin geçmesi performans kanıtı değildir. En az20farklı olgun giriş sonucu olmadan ilk performans hükmü verilmez;20 de istatistiksel garanti değildir. V2/V3 ayrı takvim dönemleri karşılaştırması tek başına değişikliğin nedensel katkısını kanıtlamaz. PARTI/LSK geçmiş hareketlerinden geriye dönük gerçek sinyal/giriş oluşturulmaz.

## Sürüm ve çalışma

Yeni ayrı dal `scanner-state-coin-tarama-5-v3`. Eski V2 dalı/commit state'i bütünüyle değişmeden saklanır; eski işlem/aday kayıtlarının kopyası ve tam kaynak state hash/SHA'sı V3 archive alanında bulunur. Eski pending mesajlar replay edilmez. Coin2/3, Shortçu Kıstır ve Meme V6 dosyaları/ayarları korunur.

Tek etkin Coin Tarama5 workflow en çok110dk oturum çalıştırır,300s hedefli döngü; saatlik23.dakika tetik ve aynı concurrency kilidiyle devam eder. Her döngüde gözlem öncesi/sonrası değil, **bildirimden önce kayıt**, bildirimin ardından makbuz, ölçümün ardından sonuç checkpointi vardır. GitHub başlangıç/oturum geçişi/API gecikmesi5dk garantisi vermez. Gerçek başlangıç/bitiş, oturum içi/arası p95/en uzun/>10dk aralıkları ve kaynak hataları ayrı raporlanır. Bir işin başarıyla çalışması tam veri kapsaması değildir.

Kaynaklar: [MEXC kontrat kamu verileri](https://mexcdevelop.github.io/apidocs/contract_v1_en/), [MEXC spot](https://mexcdevelop.github.io/apidocs/spot_v3_en/), [OKX](https://www.okx.com/docs-v5/).

Doğrulama: `python -m unittest test_coin5 test_coin5_v2 test_coin5_v3 -q`.
