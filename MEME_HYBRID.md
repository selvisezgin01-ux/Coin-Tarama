# Coin Tarama Meme — 5 dk erken aday / 15 dk teknik teyit

26 Ekim 2026 kullanıcı kararıyla yalnız Meme taraması güncellenir. Coin Tarama 2/3 değişmez.
Tek aktif Meme workflow: `.github/workflows/coin-tarama-meme.yml`.
Güncel rapor: [scanner-state-meme-v4/report.md](https://github.com/selvisezgin01-ux/Coin-Tarama/blob/scanner-state-meme-v4/report.md).
Önceki `scanner-state-meme-v3` arşivdir, ayrıca çalıştırılmaz.

## Zaman ve veri

- Aynı havuzun gerçek 5 dk OHLCV verisi okunur; tüm gerekli alt mumlar kapalı ve mevcutsa 15 dk mumlar oluşturulur. Boş mum/veri uydurulmaz.
- Erken aday: havuz açıldıktan sonra üç TAM kapalı 5 dk mum. Açılışın hizasına göre yaklaşık 15–20 dk + keşif/API/GitHub çalışma gecikmesi.
- Ayrı teknik teyit: üç TAM kapalı 15 dk mum. Yaklaşık 45–60 dk + gecikme. Erken sinyal bunu beklemez. İlk gözlemde doğrudan 15 dk koşulları varsa önceki zamana erken sinyal yazılmaz.
- 5 dk zamanlaması daha erken gözlem sağlar; 15 dk teyidin daha kârlı olduğu ölçülmedi. Mum süresi kontrat güvenliği değildir.
- İki aşamanın ilk gerçek gözlem fiyatları/saatleri ayrıdır. Aynı zincir+kontrat tek token sayılır; sembol/havuz değişimi bağımsız başarı oluşturmaz.
- Önceki pump/dump, başlangıç verisi ve boşluk kontrolleri 5 dk tam erişilebilir geçmiş üzerinde korunur. Açık mum yalnız olumsuz geçmiş kontrollerinde kullanılır.
- Havuz yaşı 15 dk alt sınırına iner; diğer piyasa/güvenlik/dev/manuel harita koşulları korunur. 45 dk developer işlem penceresi geçmişe dönük kontroldür, yeni havuzun 45 dk beklemesi şartı değildir.
- Her ağda döngü başına en çok iki uygun havuzun mumları incelenir (önce bir). Diğer istek sınırları korunur; bütün piyasa veya kesin 5 dk bildirim garantisi yoktur. Zamanlayıcı gecikmesi ve sağlayıcı erişimi önemli sınırlamalardır.

## Büyük alıcı desteği

- 15/30 dk sınırlı havuz işlem örneğinde, aynı işlem başlatıcı adresin alımları birleştirilir, satışları düşülür; işlem ID tekrarları sayılmaz.
- Büyük net alım başlangıç eşiği `max(500 USD, havuz likiditesi * 0.005)`. Bu deneysel eşiktir, geçmiş performansa göre optimize edilmedi.
- Bilinen oluşturucu, havuz/vault ve yakım adresleri hariç tutulur. Diğer adreslerin farklı kişilere ait olduğu veya ilişkili olmadığı doğrulanmaz.
- 15 dk örneğinde adres sayısına göre en çok 8 puan; en az iki büyük adres ve toplam net pozitif akış varsa +2. En çok 10 destek puanı; zorunlu filtre veya başarı olasılığı değildir.
- Tek adres alım hacminin %50 üzerindeyse veya büyük alıcı alımlarının en az yarısı kadar satış da yaptıysa destek puanı 0 ve uyarı.
- En çok 300 işlem bütçesi pencereyi kesiyorsa, eksik/hatalı alan varsa veya veri okunamazsa bilinmiyor; 0 puan/temiz kabul edilmez.
- Büyük alım yapan adres, portföyü büyük veya başarılı yatırımcı olarak etiketlenmez. Örnek eksik satış/diğer havuzları kapsamayabilir; tam zincir kapsamı yoktur.
- Destek rapor/Issue içinde gösterilir, çekirdek güvenlik/ilk oluşum/pump elemesini aşamaz.

## Geçiş ve test

V3 başlangıç yaşı, olumsuz pump kayıtları, sosyal/followup geçmişi ve gerçek fiyat/sonuçları korunur. Eski bekleyen bildirimler denetim kaydı olarak saklanır, eski fiyatla tekrar gönderilmez. Yeni erken/teyit gözlemleri geriye yazılmaz.
83 yerel regresyon testi: kapalı/açık mum, eksik alt mum, kısmi açılış, erken/teyit fiyat ayrımı, tek bildirim, pump/güvenlik kapıları, büyük alıcı netleştirme ve eksik veri.

Kaynak alanları: [OHLCV](https://docs.coingecko.com/reference/pool-ohlcv-contract-address), [havuz işlemleri](https://docs.coingecko.com/reference/pool-trades-contract-address).
API kapsamı/ağ desteği fiyat takip edilse bile güvenlik teyidini sınırlayabilir. Hiçbir alım/satım, cüzdan bağlantısı, işlem oluşturma, imza veya yayın yapılmaz.
