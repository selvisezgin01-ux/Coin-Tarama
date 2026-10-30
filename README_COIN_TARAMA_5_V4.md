# Coin Tarama 5 V4

Bu ileri dönem deneyinde her MEXC/OKX SPOT/PERP pazarı kendi gerçek fiyatıyla
izlenir. Aynı sembolde başka borsanın erken radarı ayrıntılı takibi veya giriş
teyidini engellemez. Ortak sembol farklı pazarlarda bağımsız başarı sayılmaz.

## Keşif ve güvenlik kontrolleri

- OKX'in resmi `instCategory=1` kripto sınıflandırması kullanılır; kategori
  bilinmiyorsa yeni kripto adayı olduğu varsayılmaz. Tokenleştirilmiş hisse/ETF,
  emtia, forex ve tahviller bu evrene girmez. X harfiyle başlama kuralı yoktur;
  XRP/XNO gibi kriptolar korunur. Katalog kategori sayıları kaydedilir.
  Kaynak: https://www.okx.com/docs-v5/en/#rest-api-public-data-get-instruments

- Kapalı 15 dakika mumları, EMA20 ve ATR14 kullanılır. Son mum pozitif, kapanış
  aralığın üst %40'ında ve hacim önceki 20 mum medyanının en az 2 katıdır.
- Son sekiz mumun tepesinde kırılım, erken dönüş veya dar bantta hacimlenme.
  Son saatte %12 üstü ve EMA20'den 4 ATR üstü uzama erken radar değildir.
- Günlük en az 100 bin USDT hacim, radarda en fazla %0,5 makas. Aktif takipte
  hacim/makas bozulan coinlerin geçerli güncel fiyatları da okunur; bu yeni
  girişte likidite kontrolünün kaldırılması değildir. Eksik fiyat bilinmiyor kalır.
- Bütçeler: döngüde 3, saatte 6 yeni sembol; en fazla 20 aktif sembol ve 80
  pazar. Aynı sembolün ek pazarları bu bütçeyi dört bağımsız coin gibi tüketmez.
  Grup başına dinamik 20 + dönen 10 ve en fazla 40 ayrıntılı mum serisi.
  Her coin her 5 dakikada ayrıntılı incelenmiş sayılmaz; gerçek kapsam kaydedilir.

## İptal sonrası yeni yapı

Kör altı saat bekleme kaldırılmıştır. Yeniden aday için en az 45 dakika,
iptalin gerçek gözleminden tamamen sonra başlayan üç tam kapalı 15 dakika
mumundan dar bir taban ve ardından yeni hacimli kırılım gerekir. Bu şartların
birlikte oluşması genellikle 60–75 dakika veya daha uzun sürer. Eski sinyal
mumu, arşivde görülmüş aynı mum veya sırf zaman geçmesi tekrar sinyal olamaz.

## İki giriş yolu

1. `retest`: Hacimli kırılan seviyeye geri test ve daha sonraki kapalı mumda
   geri test tepesinin aşılması.
2. `continuation`: İlk kırılımdan sonra eski seviyenin en az 0,5 ATR üstünde
   3–4 kapalı mumluk yeni taban. Bant en fazla 1,5 ATR, net sürüklenme en fazla
   0,75 ATR; taban medyan hacmi ilk itkiyi aşmaz. Ardından güçlü kapalı mumda
   taban tepesi ve hem taban hem önceki 20 mum medyanının en az 2 katı hacim
   aranır. Son itki en fazla 90 dakika öncedir; taban gözlem/giriş sonrasında
   oluşmalıdır. Güncel fiyat taban tepesinin en fazla 0,5 ATR üzerinde olabilir.

İki yolda da güncel giriş makası en fazla %0,3, stop mesafesi en fazla %3,
BTC'nin bilinen son kapalı saatinde düşüş %2'den küçük olmalı. BTC bağlamı
bilinmiyorsa giriş yoktur. Bilinen 1/4 saat direnci maliyet dahil 2R hedefini
engelliyorsa teyit yoktur. Direnç bilinmiyorsa hedef yalnız projeksiyondur.
Planlama maliyeti toplam %0,5'tir; emir, gerçek fill veya kâr vaadi değildir.

## Bildirimler ve trend

- Erken radar giriş değildir. Tekrar eden erken bildirimler bir saat içinde
  bastırılabilir; pazar takibi ve sonraki giriş teyitleri bastırılmaz.
- Her gerçek giriş `🟢🎯 GİRİŞ TEYİDİ` ile gösterilir; `retest/continuation`,
  gerçek fiyat/zaman, kaynak kapanışı, stop ve hedef türü ayrıca yazılır.
- Yeni girişten en az 60 dakika sonra, yeni bir yukarı taban ve hacimli kırılım
  aynı pazarda tekrar teyit verebilir. Bir adayda en fazla üç ilişkili giriş
  vardır; aynı kapalı mum tekrar giriş değildir. İlk fiyat/stop değişmez.
- Yalnız gerçek giriş bildirimi makbuzu bulunan adaylarda, girişten sonraki
  yeni kapalı 1 saat mumlarıyla `🔵📈 trend sürüyor/güçleniyor`,
  `🟠⚠️ zayıflıyor`, `🔴🧱 yapı bozuldu` durumları bildirilir.
  Yeni giriş olmayan trend mesajları yeşil giriş gibi gösterilmez.
- Güçlenme: EMA20 üstü ve yükselen EMA, üç yükselen dip ve önceki saat tepesini
  aşan kapanış. Son iki saatle teyit edilen daha yüksek dip yapı tabanıdır.
  Zayıflama: EMA20 altı veya önceki saat dibi altında kapanış. Yapı kaybı:
  takip edilen tabanın 0,15 saatlik ATR altı kapanış. Taze fiyat giriş
  geçersizliğini kaybederse ayrıca anlık yapı kaybı bildirimi oluşabilir.
- Aynı durum değişmeden tekrar bildirilmez. Güçlenmede yeni ve daha yüksek
  yapı tabanı ile en az 0,5 saatlik ATR fiyat ilerlemesi anlamlı güncellemedir.
- Bu trend durumları otomatik emir veya test edilmiş takip eden stop değildir.
  İlk girişin ölçüm stopu/karşılaştırması geriye dönük yükseltilmez.

## Deney ve arşiv

State: `scanner-state-coin-tarama-5-v4`; tek mevcut `coin-tarama-5.yml`
iş akışı V4 işçisini çalıştırır. Eski V3 dalı ve tüm kaynakları korunur.
V3 son tam state SHA'sı ve kanonik hash V4 arşivinde vardır. Eski fiyatlar,
BTC referansları, mesaj makbuzları ve sonuçlar `legacy_v3` alanında ayrı
kalır; eski sonuç ölçümleri üç döngüde bir bütçe paylaşarak sürer. Eski
adaylar veya mesajlar yeni V4 girişi diye tekrar oynatılmaz.

1/4/12/24 saat sonuçları kendi pazarının 1 dakika verisiyle gerçek ilk gözlem
fiyatından hesaplanır. Her giriş türü ve pazar ayrı gösterilir. Tek sembolün
ilk referansı grup içinde ayrıca ayrılır; tekrar girişler ve radar/giriş
birbirinden bağımsız örnek gibi birleştirilmez. Stop/hedef sırası,
MAE/MFE, BTC farkı ve %0,2/%0,5/%1 maliyet senaryoları korunur. Eksik veri,
giriş parçası ve aynı mum belirsizliği gerçekleşmiş net kâr sayılmaz.

SOPH bu revizyonun tasarım örneğidir; geçmiş SOPH yükselişi V4 başarısı değildir.
Formülün üstünlüğü ancak yeterli sayıda farklı coin ve olgunlaşmış ileri dönem
sonucu ile değerlendirilebilir. Hedef döngü 5 dakikadır; GitHub kuyruğu,
veri sağlayıcıları ve ölçüm süresi nedeniyle kesintisiz 5 dakika garantisi yoktur.
