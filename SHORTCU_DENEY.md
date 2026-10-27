# Ücretsiz Shortçu Kıstır karşılaştırma protokolü

Kullanıcı 27 Ekim 2026'da önce ücretsiz, ölçümlü denemeyi seçti. Amaç, yeni göstergelerin teknik temele katkısını ölçmek; ücretli veri satın alınmaz. Mevcut üretim Shortçu Kıstır v1 eşikleri, kaynak Coin Tarama 3, Coin Tarama 2 ve Meme değiştirilmez.

## Aynı gerçek gözlemde dört koşullu grup

Tüm faktörlerin bilindiği, ilk ortak uygun teknik aday gözlemi alınır. Ortak koşullar: aynı borsada doğrulanmış aktif USDT perpetual, geçerli vadeli makas/pozisyon büyüklüğü/spot-vadeli fiyat farkı, güncel fonlama, geçerli eski OI gözlemi ve güncel spot/BTC referansı. Bilinmeyen veya birikmekte olan OI geçmişi olumsuz koşul sayılmaz; kayıt o anda başlatılmaz.

- A: Teknik temel + ortak işlem/veri koşulları; fonlama/OI artışı yön şartı yok.
- B: A + negatif fonlama (üretimin sabit eşiği).
- C: A + OI artışı ve fiyatın tutunması (üretimin sabit eşikleri).
- D: A + B/C birlikte.

A bütün spot coinleri kapsamaz. C, yalnız OI etkisini değil OI/fiyat paketini ölçer. Gruplar örtüşür; grup toplamları bağımsız coin sayısı değildir. D, ilk ortak hazır gözlemde tüm koşulların birlikteliğidir; saatler sonra ayrı bir üretim sinyali oluşmasıyla geriye dönük etiket değiştirilmez. Üretim sinyallerinin kendi ölçümleri ayrıca korunur.

## Kayıt ve değerlendirme

- En çok 50 farklı sembol, her çalışmada en çok 5 yeni kayıt. Aynı sembolün iki borsa kaydı iki bağımsız örnek değildir; fiyat/makas/hacim seçim kuralı grupların sonucundan bağımsızdır. Tam kontrat kimliği borsalar arasında ayrıca doğrulanmış sayılmaz.
- Her kaydın **yeni gerçek spot fiyatı ve saati**, BTC ve kontrol referansları aynı borsadan alınır. Eski Coin Tarama 3 veya üretim fiyatı yeni giriş olarak kullanılmaz. Türev verileri bu ana en çok 5 dk uzaklıkta olmalıdır.
- Ana sonuç 12 saat; 6/24/48 saat ikincil. Girişe göre dip/tepe (MAE/MFE), BTC/kontrol üstü fark ve maliyet duyarlılığı raporlanır. Maliyet senaryoları gidiş-dönüş %0.2/%0.5/%1; gerçek komisyon/kayma/fonlama ölçümü veya gerçekleşebilir net kâr değildir.
- Fiyat yolu girişten sonraki ilk TAM 1 dk mumdan hedefin ilk dakika kapanışına uzanır. Giriş mumunun kalan <1 dakikası tepe/dip hesabına katılmaz; tüm gerçek işlem aralığının eksiksiz tepe/dibi olduğu iddia edilmez. Ara mum eksikse MAE/MFE bilinmiyor; uç fiyat eksikse getiri bilinmiyor. Eksik/başarısız kayıtlar silinmez veya 0 getiri sayılmaz.
- İlk 25 ve sonraki 25 kayıt ayrı saklanır. Eşikler sonuçlara bakılıp dönem arasında değiştirilmez; değişirse yeni kohort gerekir. Bir grup için en az 20 tamamlanmış ölçüm olmadan ilk yorum yapılmaz. Bu sayılar istatistiksel kesinlik veya farklı piyasa rejimi garantisi değildir; çok az sinyal varsa daha fazla veri gerekir.
- Her çalışmada en çok 4 vakanın vadesi gelen dakika ölçümleri güncellenir. Tamamlanmış gözlem tekrarlanmaz; veri hatası sonraki çalışmada tekrar denenir. Ölçüm gecikmesi ile fiyat hedefi karıştırılmaz; gerçekte hedefin dakika kapanışı kullanılır.
- Sessizdir: yeni Issue/Telegram bildirimi üretmez. Üretim bildirimlerinden SONRA çalışır; gölge ölçüm nedeniyle aday mesajı bekletilmez.

Kalıcı durumun yalnız `comparison_lab` bölümü değişir; kendi tasarım karması vardır. Üretimin tüm diğer alanlarının aynı kaldığı her çalışmada hash ile doğrulanır. Aynı bağımsız Shortçu Kıstır raporunun sonunda deney bölümü bulunur; başka ad altında yeni tarama veya eski 2/3/Meme güncellemesi değildir.

## Dış veri ve ücretli seçenekler

Bu sürümde CoinGlass/Hyblock/CoinAnk anahtarı yok; harita veya büyük yatırımcı pozisyon dağılımı eklenmiş sayılmaz. Erişim kısıtları aşılmaz, gizli web uç noktaları kazınmaz, veri uydurulmaz. Ücretsiz protokol önce mevcut kamu verisinin katkısını ölçer.

27 Ekim kontrolünde CoinGlass API fiyatları Hobbyist $29/ay, Startup $79/ay, Standard $299/ay, Professional $699/ay. **İncelenen Coin Liquidation Map API uç noktası yalnız Professional/Enterprise listeliyor**; $29 planın bu haritayı sunduğu varsayılmaz. Bu, bütün sağlayıcılardaki tüm haritaların asgari fiyatı değildir. Hyblock/CoinAnk için bu çalışmada doğrulanmış sayısal teklif yok; fiyat uydurulmaz. Abonelik gerekirse uç nokta/coin kapsamı ve güncel fiyat ayrıca doğrulanır; otomatik satın alma yapılmaz.

Kaynaklar: [CoinGlass planları](https://www.coinglass.com/pricing), [Coin Liquidation Map erişimi](https://docs.coinglass.com/reference/liquidation-aggregated-map), [Hyblock kimlik doğrulama](https://docs.hyblockcapital.com/).
