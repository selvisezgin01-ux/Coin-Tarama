# Coin Tarama Meme

Coin Tarama 2 ve Coin Tarama 3'ten ayrı bir deneydir. Yalnız genel DEX, risk raporu ve zincir verilerini okur; cüzdana bağlanmaz, imza veya emir göndermez. Token kimliği simge adı değil **ağ + kontrat adresidir**.

## Kapsam ve takip

- Solana, Ethereum, BNB Chain, Robinhood, HyperEVM (HYPE).
- Pons, Robinhood içindeki bir platformdur; Robinhood verisindeki `pons-v2` havuzları ayrıca bir ağ icat edilmeden kapsama girer.
- GitHub iş akışı: **Coin Tarama Meme — 15 dakika birikim**. Yaklaşık beş dakikada bir, dakikanın 02/07/12/.../57 anlarında planlanır. GitHub gecikebilir; bu gerçek zamanlı bir işlem sistemi değildir.
- [Canlı meme raporu](https://github.com/selvisezgin01-ux/Coin-Tarama/blob/scanner-state-meme/report.md)
- [Bildirimler](https://github.com/selvisezgin01-ux/Coin-Tarama/issues), başlık **Coin Tarama Meme**.
- Veri ve tekrar bildirim kayıtları yalnız `scanner-state-meme` dalında tutulur. Önceki iki sürümün kuralları/kayıtları değiştirilmez.

## Başlangıç kuralları

Havuz yaşı **1–24 saat**; en az **10.000 USD likidite**; sağlayıcının piyasa değeri veya açıkça etiketlenen FDV değeri **25.000–5.000.000 USD** arasında olmalıdır. Likidite/değer oranı en az %3'tür. Son 15 dakikada en az 1.000 USD hacim ve 12 işlem; alışların toplam alış+satış işlem sayısına oranı en az %60 (alış/satış en az 1,5) aranır. Bunlar işlem sayılarıdır; benzersiz alıcı, gerçek para girişi veya wash-trading bulunmadığı iddiası değildir.

**Birikim:** Üç kapalı 15 dakikalık mumda toplam fiyat aralığı en çok %20, mutlak net değişim en çok %10 olmalı. Son mum hacmi ilkin en çok %80'i olmalı; son dip ilk dipten %2'den fazla aşağıda olmamalı. Son kapanış mum aralığının en az %55 seviyesinde olmalı.

**İlk kırılım:** Önceki üç mum yukarıdaki birikim yapısını sağlamalı. Yeni kapalı mum bu alanın tepesini aşmalı; hacim önceki üç mum ortalamasının en az 1,5 katı, kapanış konumu en az %65 olmalı. Kırılan seviyeden uzaklık en çok %12'dir. Eldeki havuz geçmişinde tek mumda %60 üstü yükseliş veya mevcut kapanışta tepeden %25 üstü geri çekilme varsa setup reddedilir. Veriler tüm geçmişi içermiyorsa tokenin hayatında hiç pump olmadığı iddia edilmez.

Açık mumlar kullanılmaz; işlem olmayan aralıklar uydurulmaz. Kesinti varsa özellikler son kesintisiz bölümde yeniden başlar. Güncel likidite önceki gözlemlere göre bir saatte %20'den fazla düşmüşse aday reddedilir.

## Piyasa değeri, cüzdan haritası ve geliştirici

**Market cap ve FDV ayrıdır.** Market cap sağlayıcı bildirimidir; dolaşımdaki arzın bağımsız denetimi değildir. FDV varsa ama market cap yoksa bu açıkça yazılır ve token üst teyitli gruba geçemez. Yeni havuz açılması eski bir tokenin yaşını sıfırlamaz: kayıtlı en eski havuz tarihi korunur. Bu tarih yine de tokenin mint/kontrat yaratılma tarihi değildir. Merkezi borsa listelenme durumu tüm ağlarda bağımsız kontrat eşlemesiyle doğrulanmış değildir; sırf simgesi MEXC/OKX'te var diye farklı bir kontrat elenmez.

**Dağılım:** Sağlayıcıda açıkça tanınan AMM/vault/yakım adresleri ayrılır; her kontrat körlemesine dışarı atılmaz. Solana'da aynı sahibin farklı token hesapları toplanır. Açıklanamayan tek sahip en çok toplam arzın %10'u, ilk on sahip toplamı en çok %35 olmalıdır. Eksik ilk on veri tam ölçüm gibi sunulmaz.

**Bağlantılar:** Bubblemaps haritasındaki en büyük gözlenen bağlantılı küme en çok %20 olmalı. Pay birimi, token miktarı ve arzla çapraz kontrol edilmeden kullanılmaz. Harita 15 dakikadan eskiyse veya düğümler eksikse teyit verilmez. Transfer bağlantısı tek bir kişinin sahipliği veya kötü niyetinin kanıtı değildir; haritanın incelenen ilk 80 sahip kapsamı tüm zincir değildir.

**Geliştirici:** Risk sağlayıcısının bildirdiği oluşturucu adresi esas alınır. Bu kişinin tüm bağlı cüzdanları kesin tespit edilmiş sayılmaz. Oluşturucu payı %8'den yüksekse elenir. Bakiyesinin sıfır olması satış yapmadığı, yaktığı veya kilitlediği şeklinde yorumlanmaz.

EVM'de doğru ağ kimliği doğrulanır; bildirilen oluşturucu bir kontratsa gerçek geliştirici gibi kabul edilmez. Son 45 dakikayı kapsadığı doğrulanan blok aralığında token çıkışları taranır. Solana'da oluşturucu ve mevcut token hesaplarının imzaları, işlem gövdeleri ve token bakiyeleri incelenir. Sayfa/işlem bütçesi, erişim veya zaman eksikliği varsa durum **bilinmiyor** kalır. Çıkış veya hesap azalması konservatif olarak eler; bunun satış, kendi cüzdanına transfer veya yakım olduğunu otomatik iddia etmez. Dolayısıyla kanıtlı bazı zararsız hareketler de inceleme gerektirebilir. Kilit/yakım konusunda ayrı işlem kanıtı olmadan olumlu teyit üretilmez.

Bu, **son 45 dakikalık gözlenen adres kapsamıdır**; token oluşturulduğundan beri hiç satış yapılmadığı veya satışın başka cüzdandan yapılmadığı kanıtı değildir.

**Likidite kilidi:** Geliştiricinin kendi token kilidiyle karıştırılmaz. RugCheck'te yalnız seçili havuzla eşleşen kilit yüzdesi gösterilir. GoPlus'ın birkaç havuzu birleştirebilen LP sahipliği yüzdesi tek bir havuza mal edilmez. V2 LP tokeni, V3/V4 pozisyon NFT'si ve bonding curve farklı yapılardır. Kilit bilgisi destekleyicidir; eksikliği her protokolde otomatik ret değildir, varlığı da mint/freeze/honeypot sorunlarını geçersiz kılmaz. Bir sağlayıcı kilit yüzdesi gelecekte likidite/çıkış garantisi değildir.

## Eksik veri ve bildirim davranışı

**Filtreleri sağlayan izleme:** Piyasa yapısı, gerekli güvenlik alanları, geliştirici penceresi ve harita teyidi sağlanmışsa bildirilir. Bu bir alım emri veya güvenli token onayı değildir.

**İnceleme:** Piyasa yapısı uygun, fakat kritik teyitler eksikse rapora girer. Varsayılan olarak telefona aday bildirimi gönderilmez. Eksik harita/geliştirici verisi sıfır risk gibi yorumlanmaz. Belirgin kötü risk veya geliştirici çıkışı varsa token reddedilir.

Bağlantı haritasını otomatik okumak için kendi **BUBBLEMAPS_API_KEY** anahtarınızı GitHub **Settings → Secrets and variables → Actions → Secrets** bölümüne eklemek gerekir. Bu anahtar mevcut değildir; erişim açılmadan otomatik harita teyidi tamamlanamaz. Anahtarı sohbet mesajına yazmayın. Cüzdan seed/private key gerekmez.

Genel RPC'ler sınırlı olabilir. İhtiyaç halinde aynı bölüme `MEME_RPC_SOLANA`, `MEME_RPC_ETHEREUM`, `MEME_RPC_BNB`, `MEME_RPC_ROBINHOOD`, `MEME_RPC_HYPEREVM` adlı özel okuma uçları eklenebilir. Boş secret değerleri genel okuma adresine döner. Desteklenmeyen GoPlus ağlarında (ilk kontrolde HyperEVM) güvenlik alanları bilinmiyor kalır; ağın fiyat/havuz takibi devam eder. Sağlayıcı API erişimi veya limitleri değişebilir.

## Ölçüm ve veri kapsamı

İlk inceleme fiyatı ile daha sonra bildirim yapılırsa o an yeniden okunan teyitli fiyat ayrı referanslardır. 15/30/60 dakika, 3/6/24 saat hedefleri sonraki gerçek gözlemle ölçülür. Tabloda hedefe gecikme ayrıca gösterilir; tam o dakikanın mum getirisiymiş gibi sunulmaz. Pencere kaçarsa veya fiyat kaybolursa getiri bilinmiyor kalır. Likiditesi kaybolan/ölçülemeyen tokenler veri kümesinden sessizce çıkarılmaz. Aynı ağ/kontrat, yeni havuz veya birikimden kırılıma geçişle yeni bağımsız coin sayılmaz.

Ücretsiz GeckoTerminal veri bütçesi dar olduğundan istekler global aralıkla sınırlıdır; her ağda bir döngüde en çok bir uygun havuzun mumları ayrıntılı incelenir. Daha önce az incelenen uygun havuzlara sıra verilir. Rapor güncellenen token sayısını, erişim hatalarını ve mum bütçesini gösterir. Bu sürüm tüm meme piyasasını veya her yeni çıkarılan tokeni taradığı iddiasında değildir. Sadece bu kaynaklarda indekslenen Pons havuzları görülebilir; indekslenmeden önceki tüm curve işlemleri kapsanmış sayılmaz.

Kaynaklar: [DexScreener API](https://docs.dexscreener.com/api/reference), [GeckoTerminal API](https://api.geckoterminal.com/docs/index.html), [RugCheck API şeması](https://api.rugcheck.xyz/swagger/doc.json), [GoPlus API](https://github.com/GoPlusLabs/OpenAPI/blob/main/SecurityAPI.md), [Bubblemaps API şeması](https://github.com/bubblemaps/api-docs/blob/main/openapi.json), [Solana RPC](https://solana.com/docs/rpc/http), [Robinhood ağ bilgisi](https://docs.robinhood.com/chain/connecting/), [HyperEVM](https://hyperliquid.gitbook.io/hyperliquid-docs/onboarding/how-to-use-the-hyperevm), [Pons resmi belgeleri](https://docs.ponsfamily.com).
