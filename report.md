# Coin Tarama Meme

Son çalışma: 27.10.2026 17:09 Türkiye saati.

**Deneysel DEX izleme. Tüm yeni tokenleri kapsamaz ve yükseliş garantisi vermez.**

Kapsam: Solana, Ethereum, BNB Chain, Robinhood (Pons dahil), HyperEVM. Pons ayrı bir ağ değildir.

**Hedef: ilk yükseliş öncesi oluşum/birikim.** Yeni aday yalnız birikim evresinde alınır; ilk kırılım ancak daha önce bildirilen birikimin devamı olarak izlenir. Trend listesi aday kaynağı olarak kullanılmaz. **Cüzdan haritası manuel kontrol bekler.** Kritik kontrat/geliştirici verisi eksik tokenler bildirilmez.

Geçmişin tamamındaki fitiller ve açık mum dahil gözlenen dipten tepeye yükseliş %25 üzerindeyse, ilk fiyatın %10 üzerine uzamışsa veya tepeden %15 üzeri düşmüşse elenir. Bu eşikler deneysel tercihlerdir. Havuz başlangıcı, ara mumlar veya güncel mum yoksa ilk oluşum teyitsizdir. Eski pump sonrası yataylaşma yeni aday sayılmaz.

GMGN kullanılmaz. Solana: RugCheck + GoPlus Solana; desteklenen EVM ağları: GoPlus. GMGN’nin tüm sniper/bundler etiketleri ve eksiksiz geliştirici geçmişi sağlanmaz. Teknik risk ön elemesi tokenin resmî/orijinal proje kontratı olduğunu kanıtlamaz.

Yeni havuz yaşı tokenin yaratılma yaşı değildir. Market cap sağlayıcı bildirimi olarak, FDV ise açıkça ayrı değer türü olarak gösterilir. Geliştirici teyidi yalnız belirtilen 45 dakikalık işlem penceresindeki raporlanan adrese aittir; ömür boyu hiç satış yapmadığı veya başka cüzdan kullanmadığı anlamına gelmez.

| Ağ | Güncellenen token | Piyasa ön elemesi | Mum incelenen | Ön eleme / manuel harita bekliyor | İnceleme | Erişim/veri hatası |
|---|---:|---:|---:|---:|---:|---:|
| Solana | 20 | 0 | 0 | 0 | 0 | 1 |
| Ethereum | 34 | 0 | 0 | 0 | 0 | 0 |
| BNB Chain | 33 | 0 | 0 | 0 | 0 | 0 |
| HyperEVM (HYPE) | 19 | 0 | 0 | 0 | 0 | 0 |
| Robinhood | 19 | 0 | 0 | 0 | 0 | 1 |

## Otomatik ön eleme geçti — manuel harita kontrolü bekliyor

| Token / adres | Ağ | Grup | Piyasa değeri / FDV USD | Geliştirici | Harita | Likidite kilidi | Büyük alıcı desteği | Eksik otomatik kontroller |
|---|---|---|---:|---|---|---|---|---|

**Henüz koşulları sağlayan aday yok.**


## İnceleme — eksik otomatik teyitler

| Token / adres | Ağ | Grup | Piyasa değeri / FDV USD | Geliştirici | Harita | Likidite kilidi | Büyük alıcı desteği | Eksik otomatik kontroller |
|---|---|---|---:|---|---|---|---|---|

Bu çalışmada inceleme kaydı yok.


## Gerçek gözlem kayıtları

Fiyatlar sağlayıcının gözlenen fiyatıdır; emir, alış/satış kotasyonu veya gerçekleşebilir net getiri değildir. İnceleme ve daha sonraki teyitli bildirim fiyatları ayrı tutulur. Aynı token havuz/grup değiştirse de yeni bağımsız coin sayılmaz.

| Token | Ağ | Referans türü | Gerçek gözlem TR | Fiyat | 15dk % | 30dk % | 1s % | 3s % | 6s % | 24s % |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|

## Veri kapsamı ve eksikler

Getiri sütunları hedef sürelerdir. Parantezdeki +dakika gerçek fiyat gözleminin hedefe gecikmesidir; tam 15/30/60 dakikalık mum getirisi olduğu iddia edilmez. Geçerli gözlem penceresi kaçırılırsa sonuç boş kalır.

Her ağda yalnız yeni havuz akışı sınırlı sayfalarla okunur. Önceki izlenen havuzlar kalıcı kayıttan yenilenir. Ham keşif ve sosyal gözlem tokenleri aday listesinde gösterilmez. Ücretli profil/boost olumlu sinyal sayılmaz. Aynı simge farklı kontratlarda birleştirilmez.

5 dk erken aday: havuz açıldıktan sonraki üç tam kapalı 5 dk mum gerekir (yaklaşık 15–20 dk + veri/çalışma gecikmesi). 15 dk teknik teyit: üç tam kapalı 15 dk mum gerekir (yaklaşık 45–60 dk + gecikme); erken bildirim için beklenmez. İki aşama kendi gerçek gözlem fiyatıyla ayrı ölçülür, aynı token iki bağımsız başarı sayılmaz. 15 dk teyit daha yüksek başarı veya kontrat güvenliği kanıtı değildir. Başlangıç havuz verisi tokenin tüm geçmişini kapsamaz.

Bubblemaps haritasını kullanıcı manuel inceler; API anahtarı gerekmez. Hiçbir kayıt otomatik veya manuel harita onayı almış sayılmaz. Robinhood/HyperEVM harita desteği bu sürümde doğrulanmadığından genel uygulama bağlantısı verilir; uygun ağ/harita bulunamazsa bu kontrol eksik kalır. RPC veya güvenlik kaynağının ağ desteği yoksa o ağda fiyat/havuz takibi sürer; eksik otomatik teyitle aday bildirilmez.

Büyük alıcı desteği zorunlu filtre değildir: 15/30 dk işlem örneğinde adres başına net alım en az max(500 USD, havuz likiditesi × 0.005). Deneysel 0–10 puan olasılık/servet/akıllı para kanıtı değildir. Tek adres >%50 alım hacmi veya büyük alıcıda >=%50 geri satış puanı sıfırlar; eksik/kesilmiş veri bilinmiyor. Bilinen dev/havuz/vault/yakım adresleri çıkarılır; diğer adreslerin bağlantısı doğrulanmaz.

GitHub planı yaklaşık 5 dakikada birdir; zamanlayıcı gecikebilir. Birkaç saniyede oluşan ilk pump yakalanamayabilir. Mum/istek bütçesi nedeniyle aynı anda bütün havuzlara bakıldığı iddia edilmez.

- Solana: api.geckoterminal.com: HTTP 504
- Robinhood: api.geckoterminal.com: data connection or response error

## Bildirim sonrası ek ölçümler

Yalnız ön elemeden geçen tokenler; ilk bildirimden sonra 24 saat, döngü başına en çok 2 token sırayla kontrol edilir. Her token her döngüde kontrol edilmiş sayılmaz. Ek ölçümler seçim eşiklerini veya geçmiş referans fiyatını değiştirmez.

Henüz ön eleme adayı yok; ek ölçüm listesi boş.

Alıcı sayısı, net alım ve yoğunlaşma son en çok 300 işlemin 15/30dk örneğinden hesaplanır; tam pencere veya bağımsız kişi sayısı değildir. Ayrıntı state.json içindedir. Holder değişimi yalnız aynı sağlayıcının iki gerçek gözlemi arasında ölçülür; önbellek yaşı bilinmez. Developer takibi yalnız bilinen oluşturucu ve sınırlı 45dk pencereyi kapsar; boşluklar kalabilir.

Satış rotaları yalnız GET fiyat sorgusudur; işlem oluşturulmaz, imzalanmaz ve gönderilmez. Rota bulunamaması tek başına satış engeli değildir. Kendi havuzumuz dışındaki rotalar da kullanılabilir. Raydium fiyat etkisinin birimi ayrıca doğrulanmadığından yüzdelik iddia yapılmaz; ham sağlayıcı alanı kaydedilir. Gaz ve verginin eksik olduğu yerde net kazanç hesaplanmaz.

## X bağlantıları ve topluluk devri — ek gözlem

Kaynak: DexScreener token metadata ve sınırlı son topluluk devri akışı. Geçmiş tüm X isim değişiklikleri, aynı hesabın kimliği ve hesabın sahibinin değişmesi doğrulanmaz. İlk gözlemden önceki geçmiş bilinmiyor; sayaç yalnız takip sırasında görülen bağlantı değişimlerini sayar. CTO kaydı satış veya dump kanıtı değildir.

| Token / ağ | İlk X gözlemi TR | İlk bağlantı | Güncel bağlantı | Gözlenen değişiklik | CTO kaydı |
|---|---|---|---|---:|---|

Henüz aday yok; ham sosyal gözlem tokenleri aday olarak gösterilmez.


Her döngüde ağ başına en çok 20 tokenin metadatası okunur; bütün tokenler aynı anda kapsanmaz. X bağlantıları yalnız metin olarak doğrulanır; hesap varlığı veya resmî proje hesabı olduğu onaylanmaz. Daha önce bildirilen adayda sonradan bağlantı değişimi/CTO kaydı gözlenirse ayrı uyarı Issue’su oluşur.
