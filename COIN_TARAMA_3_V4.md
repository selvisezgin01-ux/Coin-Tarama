# Coin Tarama 3 — ayrı ileri dönem deneyi

Coin Tarama 2 önceki V3 seçim formülüyle sürer. Coin Tarama 3, V4 deneysel formülünü kullanır. İki sürüm de MEXC ve OKX spot/USDT piyasalarını Türkiye saatiyle 03:05, 07:05, 11:05, 15:05, 19:05 ve 23:05'te tarar. GitHub başlangıçları gecikebilir. Bilgisayarın açık kalması gerekmez.

## Telefonda takip

- [Coin Tarama 2 güncel raporu](https://github.com/selvisezgin01-ux/Coin-Tarama/blob/scanner-state/report.md)
- [Coin Tarama 3 güncel raporu](https://github.com/selvisezgin01-ux/Coin-Tarama/blob/scanner-state-v4/report.md)
- [İki sürümün bildirim kayıtları](https://github.com/selvisezgin01-ux/Coin-Tarama/issues)

Yeni aday Issue başlıkları **Coin Tarama 2** veya **Coin Tarama 3** ile başlar. İkisi de aynı kullanıcıyı etiketler. Yeni aday yoksa mesaj oluşmaz. Aynı sürümde sürekli listede kalan coin her dört saatte tekrar bildirilmez; yeniden girişlerde 48 saat bekleme uygulanır. Aynı coin iki sürüme birden girerse iki farklı sürüm başlığıyla bildirim alabilirsiniz.

## İki aday grubu

**Yeni kırılım:** Önceki 20 mumun tepesinin üstünde ilk kapanış ve önceki 20 mumun medyanına göre en az 1,5 kat hacim aranır. Kırılım yaşı 0–2 mumdur. Fiyat EMA20/50 üstünde, EMA20 yükseliyor ve 24 saat getirisi BTC'den güçlü olmalıdır. Son mum kapanışı aralığın üst %35'inde olmalı; kırılımdan sonraki tepeye göre geri çekilme hem %15'i hem 1,5 ATR'yi aşmamalıdır. 24 saat getirisi en az %2'dir.

**Tutunma:** Kırılım yaşı 3–18 mumdur. Eski kırılım seviyesi ve sonrasındaki tutunma korunmalı, son üç mumun medyan dibi önceki üç mumdan yüksek olmalıdır. Son kapanış aralığın üst yarısında olmalı; tepeden geri çekilme hem %20'yi hem 2,5 ATR'yi aşmamalıdır. 24 saat getirisi en az -%5, 72 saat getirisi pozitif ve 24 saat BTC göreli getirisi pozitif olmalıdır.

Her iki grupta kapanış kırılım seviyesinin üzerinde olmalı. Kırılım mumundan sonraki diplerin, kırılım seviyesinin 0,5 başlangıç ATR'sinden fazla altına sarkması bu referansı bozar. Kırılım mumunun kendi geniş alt fitili bu tutunma kontrolüne katılmaz. Yeniden geçerli referans için yeni hacimli kırılım gerekir. En az 180 kesintisiz kapalı mum, 24 saatte en az 10.000 USDT hacim ve altı mumda sıfır olmayan hacim gerekir.

V4 canlı ön elemesi 24 saatte en az -%10 değişim ve 10.000 USDT hacim kullanır; üst getiri sınırı yoktur. V3 kendi eski ön elemesini kullanır. Dolayısıyla iki sürümün ayrıntılı incelediği evren farklı olabilir.

## Uyarı olarak gösterilenler

Destekleyici alan olarak RSI(14) pozitif uyumsuzluğu da kaydedilir: ardışık iki teyitli fiyat dibinde fiyat daha düşük, RSI daha yüksek dip yaparsa PU işaretlenir. Her dip için iki sol ve iki sağ kapalı mum gerekir; sinyal ikinci sağ mum kapanınca oluşur, dip mumuna geriye yazılmaz. Dipler arası uzaklık 3–30 mum, teyitten sonraki etiket ömrü altı mumdur. Daha düşük yeni dip etiketi geçersiz kılar. PU aday seçimini veya puanı değiştirmez; giriş anındaki PU/RSI, sonuçları daha sonra karşılaştırmak için saklanır. [RSI ve uyumsuzluk tanımı — TradingView](https://www.tradingview.com/support/solutions/43000502338-relative-strength-index-rsi/)

24 saat getirisi %30'u, 72 saat getirisi %45'i, EMA20 uzaklığı 2,5 ATR'yi veya yapı bozulma mesafesi %12'yi aştığında aday otomatik silinmez; durum mesajda uyarı olarak gösterilir. Düşük hacim, %0,5 üstü makas, kapanıştan uzaklaşmış gözlem fiyatı ve henüz sonraki mum teyidi olmayan ilk kırılım ayrıca belirtilir. Bu riskleri kabul edilmiş bir işlem veya otomatik alım olarak yorumlamayın.

## 1–2 haftada nasıl karşılaştıracağız?

- Her sürüm kendi ilk **gerçek gözlem zamanı ve alış/satış orta fiyatından** kayıt başlatır. Geçmişe yeni giriş yazılmaz. Eski yerel MEXC/OKX pilot kayıtları korunur.
- 12/24/48 saat getirileri, tam hedef saatten sonraki ilk dakika kapanışından hesaplanır; zaman yuvarlama farkı 60 saniyeden küçüktür. Eksik veriler uydurulmaz, sonraki çalışmada yeniden denenir.
- Aynı anda gözlenen BTC ve mümkünse hacim/ATR bakımından benzer üç aday olmayan kontrol coinine göre farklar ölçülür. Üç geçerli kontrol yoksa kontrol sonucu boş kalır.
- Aynı coin bir sürümde grup değiştirdiğinde yeni bağımsız örnek sayılmaz. İki borsada görülen aynı sembol küresel coin sayısına bir kez girer; getiri tabloları borsa bazında ayrı tutulur.
- Listeden düşen coinlerin sonuçları ölçülmeye devam eder. İlk kez kaydedilen coin tekrar bildirilse bile bağımsız ikinci performans örneği oluşturulmaz.
- 26 Ekim 2026 başlangıcından yaklaşık bir hafta sonra **2 Kasım**, iki hafta sonra **9 Kasım** karşılaştırma için uygun tarihlerdir. Bunlar değerlendirme tarihleridir; otomatik durdurma veya garanti edilmiş hatırlatma değildir. Son 48 saatteki kayıtların 48 saat sonuçları henüz olgunlaşmamış olabilir.
- Medyan getiri, BTC ve kontrollere göre fark, ölçülen farklı coin sayısı, iki sürümün ortak/ayrı adayları ve yüksek risk uyarıları birlikte değerlendirilir. Bu süre tek başına istatistiksel üstünlük kanıtı değildir.

## İlk arşiv kontrolü

246 coinlik ortak arşivde bilinen tasarım örnekleri dışarıda bırakıldı. Gerçek geçmiş bildirim yerine kapalı mum fiyatlarıyla yeniden hesaplama yapıldı. Bu hesap, güncel borsa listeleri ve arşiv seçimi yanlılığı taşır.

| Sürüm | Ölçülebilen 48 saat olayı | Medyan 48 saat % | Kontrol coinleri üstü medyan puan |
|---|---:|---:|---:|
| Önceki V3 | 319 | -0,96 | -0,34 |
| Deneysel V4 | 717 | -0,88 | -0,59 |

V4'ün 48 saatte ölçülebilen yeni kırılım grubunda 547 olayın medyanı -%1,26; tutunma grubunda 170 olayın medyanı -%0,08'dir. Tutunma grubu kontrol medyanının yaklaşık 0,09 yüzde puan üstünde kaldı. Gruplar sonradan ayrı betimlenmiştir; bu sayılar bağımsız bir doğrulama değildir. T/DOS ve önceki bilinen örnekler bu toplamlarda yoktur. V4 daha fazla olay buldu, fakat toplu sonuçlarda kontrollere üstünlük göstermedi. Kurallar bu sonuçlara bakılarak tekrar optimize edilmedi.

T ve DOS'un 25 Ekim 23:00 kapanışları V4'te de otomatik aday değildir: T'de tepeden geri çekilme ve son mum kapanışı zayıf; DOS'ta son kırılım sonrası dipler eski referansı bozmuştur. Yalnız bu isimleri listeye sokmak için kural değişikliği yapılmadı.

## Kod ve kayıtların ayrılığı

V3: `github_scan.py`, `momentum_config.json`, `scanner-state`, `coin-scan.yml`.

Coin Tarama 3: `strength_v4.py`, `strength_v4_config.json`, `strength_v4_scan.py`, `strength_v4_watch.py`, `scanner-state-v4`, `coin-tarama-3.yml`.

Ortak ileri ölçüm: `paper_watch.py`. Yeni GitHub ölçümleri bu kurulumdan sonraki ilk gerçek taramada başlar; eski yerel 50 coin pilotları ayrı sürer. Hangi sürüm daha iyi diye karar verirken gerçek gözlemlerden aynı tarihlerde başlayan kayıtları esas alacağız.

Elle çevrimdışı inceleme: `python strength_v4_scan.py --archive`. Bu seçenek yalnız mevcut V3 arşivini kullanır ve genişletilmiş V4 canlı ön elemesini temsil etmez. Elle güncel okuma: `python strength_v4_scan.py --live`. Bu iki komut kendi başına bildirim göndermez. GitHub otomasyonu `strength_v4_watch.py` üzerinden kalıcı kayıt ve bildirimleri yönetir.
