# Coin Tarama 3 — erken dönüş, hacim ve geri test

Coin Tarama 2 önceki formülüyle aynen çalışır. Coin Tarama 3'ün bu güncellemesi üç deneysel alternatif grup ekler; önceki yeni kırılım ve tutunma grupları da korunur. Ana zaman dilimi kapalı **4 saatlik mumdur**. MEXC ve OKX kendi verileriyle ayrı incelenir. Plan Türkiye saatiyle 03:05, 07:05, 11:05, 15:05, 19:05, 23:05; GitHub başlangıcı gecikebilir.

- [Güncel Coin Tarama 3 raporu](https://github.com/selvisezgin01-ux/Coin-Tarama/blob/scanner-state-v5/report.md)
- [Coin Tarama 2 raporu](https://github.com/selvisezgin01-ux/Coin-Tarama/blob/scanner-state/report.md)
- [Yeni aday bildirimleri](https://github.com/selvisezgin01-ux/Coin-Tarama/issues)
- [Önceki V4 kuralları ve ilk karşılaştırma](COIN_TARAMA_3_V4.md)


## Kisa oncelik listesi ve bildirim elemesi

Genis V5 stratejisi degismez; tum adaylar ve 12/24/48s olcumleri saklanir. Ek sunum katmani bildirimde ve raporun ustunde **en fazla 5 farkli sembol** gosterir. Ayni sembol iki borsada tek satirdir; fiyatlar veya hacimler toplanmaz. Yalniz uygun bulunan borsalar yazilir. Sembol birlestirmesi kontrat kimligi teyidi degildir.

- En az 100.000 USDT kapali 24s hacim, en cok %0,5 makas.
- Guncel fiyat izlenen seviyeyi korur; kapanistan uzaklik en cok 1 ATR, EMA20 uzerine uzama en cok 2,5 ATR.
- Gercek gozlem fiyatindan yapi bozulma referansina mesafe pozitif ve en cok %12. Bu gerceklesebilir zarar/stop garantisi degildir.
- Yalniz yatay hacim grubu hazirlik olarak raporda kalir, tek basina bildirilmez.
- 20x uzeri hacim katsayisi ayrica incelemeye ayrilir; bu, sahte islem veya dolandiricilik kaniti sayilmaz.
- [OKX resmi listesindeki](https://www.okx.com/help/okx-to-list-tokenized-stocks-for-trading) taninan hisse tokenleri exact isim + borsa eslesmesiyle ayiklanir. XRP/XLM gibi X ile baslayan butun tokenler elenmez. Liste 26 Ekim 2026'da kontrol edildi; gelecekte genisletilmesi gerekebilir.

Uygunlar once en cok 4x sayilan goreli hacimle, sonra kapanis konumu, dar makas ve ayni borsanin hacmiyle siralanir. Bu sira basari olasiligi veya beklenen getiri tahmini degildir. Bes aday yoksa liste doldurulmaz. Temel amac okunabilirlik ve piyasa kosulu elemesidir; daha karli oldugu henuz dogrulanmadi.

Fiyatlar ek katmanda kamuya acik alis/satis fiyatindan yeniden okunur. Yeni kisa-liste olcumlerinin BTC ve kontrol baslangic fiyatlari da ayni yeni fiyat okumasindandir; genis listedeki eski/ucuz fiyatlar kullanilmaz. Gozlemi 15dk'dan eski veya kapali karari guncel 4s araligina ait olmayan veriyle yeni oncelik bildirimi uretilmez. Erisim hatasi temiz eleme sonucu sayilmaz.

Genis listenin eski bildirim bekleme kaydi ile oncelik listesi teslim kaydi ayridir. Daha once genel havuzda gorunen bir coin sonradan oncelige girebilir. Oncelikte kalan ayni sembol tekrar bildirilmez; cikip yeniden gelirse 48 saat bekleme vardir. Bekleyen eski mesajlar, guncel fiyatla yeni mesajdan once teslim kimligiyle uzlastirilir. GitHub bildirimi `Oncelik listesi` basligiyla kullaniciyi etiketler. Genis aday listesi raporda acilir bolumde kalir.

Ek dosyalar: `strength_v5_priority.py`, `strength_v5_priority_config.json`, `test_strength_v5_priority.py`. Ek katmanin tasarim karmasi ve gercek fiyat olcumleri ana V5 kurallarindan ayri saklanir; ana kurallar veya onceki fiyatlar yeniden yazilmaz.

## Üç ek grup

Bu gruplar **VEYA** mantığıyla çalışır. Erken dönüş adayından önce eski 80 saatlik tepe kırılımı, sonra da geri test beklenmez. Bir token birden fazla gruba uyabilir; bildirimde hepsi yazılır.

**Erken dönüş:** Önceki kapanış EMA20 altındayken mevcut kapalı mum önceki üç mumun en yüksek fiyatını ve EMA5'i geri alır. Önceki kapanıştan yüksektir, hacmi önceki 20 mum medyanının en az 1,5 katıdır, kapanış konumu en az %50'dir. Dip önceki dibin 0,25 önceki ATR'sinden fazla altına sarkmaz. EMA20'nin yükselmesi, EMA50 üstünde olmak ve 20 mum tepesini aşmak zorunlu değildir. Bu, ilk dönüş işaretidir; uzun trend onayı değildir. SAR bu grupta destekleyici puandır.

**Yatay fiyat / hacim artışı:** Önceki üç kapalı mumun toplam aralığı en çok 2 önceki ATR, net fiyat değişimi en çok 0,75 ATR'dir. Yeni kapanış değişimi en çok 0,75 ATR ve eski alanın yakınındadır; dipler 0,25 ATR toleransla korunur. Hacim önceki 20 mum medyanının en az 1,5 katı, kapanış konumu en az %55'tir. Yüksek hacim tek başına alım baskısı veya toplama kanıtı değildir; yatay alandaki satış da yüksek hacim üretebilir.

**Geri testte tutunma / SAR:** Önceden mevcut V4 yeni kırılım koşullarını sağlayan kapalı bir kırılım bulunmalıdır. Kırılım seviyesi ve o andaki ATR sabittir. Kırılım mumunun kendi fitili geri test sayılmaz. Sonraki fiyat önce seviyeden en az 1 başlangıç ATR'si uzaklaşır; sonra son iki mum seviyeye 0,5 ATR yakınlığa döner ve üzerinde kapanır. Bu iki mumun alanı en çok 1,5 ATR, kapanışın seviyeden uzaklığı en çok 1 ATR ve ortalama hacmi kırılım hacminin en çok %80'idir. Kırılım sonrası dipler desteğin 0,5 ATR altını bozmamış olmalı; **SAR fiyat altında olmalıdır**. Eski kırılım bozulduysa sadece fiyatın tekrar üstüne çıkması aynı referansı temizlemez; yeni kırılım gerekir.

Her ek grupta en az 180 kesintisiz kapalı mum, son 24 saatte en az 10.000 USDT hacim ve altı mumda pozitif hacim gerekir. BTC'ye karşı 8 veya 24 saatlik göreli güç pozitiftir. Canlı ön eleme -%10 ve üzeri 24 saat getirisi / en az 10.000 USDT hacim kullanır; üst getiri sınırı yoktur. Dolayısıyla daha derin negatif 24 saatli dönüşler hâlâ kapsam dışındadır.

Başlangıç eşikleri, geniş arşiv sonucuna göre yeniden optimize edilmedi. Fiyat ölçeğine duyarlı sabit para tutarı yerine ATR ile yapı yakınlığı ölçülür. Bunlar kanıtlanmış kazanç eşikleri değildir.

## Korunan iki grup ve uyarılar

Yeni kırılım: önceki 20 mum tepesini en az 1,5 kat hacimle aşma, yükselen EMA20, fiyatın EMA20/50 üstünde olması, BTC göreli güç, güçlü kapanış ve sınırlı geri çekilme. Tutunma: aynı kırılımı 3–18 mum arasında koruma ve yükselen dipler. Eski kod/config değişmedi; V5 bu iki grubun çıktısını aynen alır.

SAR puan desteğidir; yalnız geri test ek grubunda zorunludur. RSI(14) pozitif uyumsuzluğu yardımcı etikettir, filtre veya puan değildir. İki sol/sağ kapalı mumla teyit edilir; dip tarihine geri yazılmaz.

Yüksek 24/72 saat getirisi, EMA uzaklığı, yapı bozulma mesafesi, düşük hacim, geniş makas ve gözlenen fiyatın izlenen seviyeyi kaybetmesi uyarı olarak yazılır. Bunlar otomatik alım veya güvenli fiyat garantisi değildir. Tam derinlik, kayma ve net işlem kârı hesaplanmaz.

## Geçmiş kontrolünün gerçek sonucu

246 coinlik arşiv kullanıldı; 21 dosyada yetersiz/eksik kesintisiz geçmiş vardı. DOOD/KAT/CTC ve önceki bilinen tasarım örnekleri ana sayılardan çıkarıldı. Her coin/model için 48 saat aralıklı olaylar sayıldı; farklı coinler ve gruplar yine aynı piyasa hareketini paylaşabilir. Canlı ticker ön elemesi geçmişe tam kurulamadı. Referans kapalı mum fiyatıdır; gerçekte gönderilmiş geçmiş sinyal değildir. İşlem maliyetleri dahil değildir. Bu dönemler daha önceki araştırmada erişilebilir olduğundan bağımsız test dönemi sayılmaz.

| Grup / birleşim | Ölçülen 12s olay | Medyan 12s % | Kontrol üstü medyan puan |
|---|---:|---:|---:|
| Önceki V4 | 722 | -0,50 | -0,56 |
| Güncel V5 birleşimi | 1419 | -0,33 | -0,29 |
| Erken dönüş | 509 | -0,36 | -0,32 |
| Yatay hacim | 469 | -0,21 | -0,18 |
| Geri test / SAR | 60 | -0,72 | -0,48 |

**Daha fazla aday tutarlı bir üstünlük sağlamadı.** Geri test grubunda 24s kontrol farkı pozitif olsa da diğer süreler bunu tutarlı biçimde desteklemedi. Yeni gruplar bu nedenle deneysel izleme olarak açıkça etiketlenir. Başarısız örnekler silinmedi. Tek bir kazanan grafikten genel başarı sonucu çıkarılmaz.

DOOD'un 26 Ekim 11:00 kapanışı yeniden hesaplamada iki borsada erken dönüşe uyar; KAT ve CTC o kapanışta uymaz. Bu örnekler tasarım örnekleridir, ana test sayılarında yer almaz. Bugünden önce yeni V5 sinyali gönderilmiş veya o fiyattan işlem yapılabilmiş sayılmaz.

## Kayıt ve bildirim

Aktif durum dalı `scanner-state-v5`; iş akışı hâlâ tek **Coin Tarama 3** iş akışıdır. Coin Tarama 2, Meme ve yerel ortak pilot değişmez. Önceki `scanner-state-v4` kaynak commit'i arşivlenir. Eski V4 gerçek referansları yeni state içindeki `previous_v4` bölümünde korunur ve 12/24/48s ölçümleri ayrı sürer. Bunlar yeni V5'in geçmiş başarısı gibi sunulmaz.

Önceki bildirimlerin 48 saatlik bekleme kayıtları korunur. Yeni sürümde aynı coin yeni bir bağımsız başarı gibi tekrar tekrar kaydedilmez. V5 ana kayıt her borsa/token için ilk gerçek gözlemden başlar. Bir gruba sonradan girerse o grubun ölçümü o andaki gerçek fiyatla ayrıca başlar; eski daha ucuz fiyat kullanılmaz. Gruplar örtüşür, sayıları bağımsız coin toplamı değildir.

Yeni adaylar aynı kullanıcıyı etiketleyen **Coin Tarama 3** Issue'larıyla bildirilir. Gruplar mesajda açıkça yazılır. Yeni aday yoksa bildirim yoktur. İlk gerçek fiyatlar ve hedefi izleyen ilk kapalı dakika kullanılır; 12/24/48s sonuçları borsaya göre ayrı, BTC ve mümkünse üç benzer hacim/ATR kontrolüyle karşılaştırılır. Eksik fiyatlar boş kalır, sonraki döngüde denenir.

Kod: `strength_v5.py`, `strength_v5_config.json`, `strength_v5_scan.py`, `strength_v5_watch.py`; temel V3/V4 modülleri değişmeyen bağımlılıklardır. Karşılaştırma kodu `compare_strength_v5.py`, testler `test_strength_v5.py`. Yazılım testleri gelecekteki başarı veya kârlılık kanıtı değildir.

SAR kaynağı: [TradingView](https://www.tradingview.com/support/solutions/43000502597-parabolic-sar-sar/). Hacim ve mum kuralları bu projenin deneysel tanımlarıdır.
