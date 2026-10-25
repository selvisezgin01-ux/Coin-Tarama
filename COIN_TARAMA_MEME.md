# Coin Tarama Meme

Coin Tarama 2 ve Coin Tarama 3'ten ayrı bir deneydir. Yalnız genel DEX, risk raporu ve zincir verilerini okur; cüzdana bağlanmaz, imza veya emir göndermez. Token kimliği simge adı değil **ağ + kontrat adresidir**.

## Kapsam ve takip

- Solana, Ethereum, BNB Chain, Robinhood, HyperEVM (HYPE).
- Pons, Robinhood içindeki bir platformdur; Robinhood verisindeki `pons-v2` havuzları ayrıca bir ağ icat edilmeden kapsama girer.
- GitHub iş akışı: **Coin Tarama Meme — 15 dakika birikim**. Yaklaşık beş dakikada bir, dakikanın 02/07/12/.../57 anlarında planlanır. GitHub gecikebilir; bu gerçek zamanlı bir işlem sistemi değildir.
- [Canlı meme raporu](https://github.com/selvisezgin01-ux/Coin-Tarama/blob/scanner-state-meme-v2/report.md)
- [Bildirimler](https://github.com/selvisezgin01-ux/Coin-Tarama/issues), başlık **Coin Tarama Meme**.
- Güncel veri ve tekrar bildirim kayıtları `scanner-state-meme-v2` dalında tutulur. İlk denemenin `scanner-state-meme` dalı korunur. Önceki iki CEX sürümünün kuralları/kayıtları değiştirilmez.
- Kullanıcı Bubblemaps kontrolünü manuel yapmayı seçmiştir. GMGN veya Bubblemaps API anahtarı gerekmez; bu sürüm ikisine otomatik sorgu göndermez. Bildirimler **otomatik risk ön elemesi geçti; manuel harita kontrolü bekliyor** anlamındadır.

## Başlangıç kuralları

Havuz yaşı **1–24 saat**; en az **10.000 USD likidite**; sağlayıcının piyasa değeri veya açıkça etiketlenen FDV değeri **25.000–5.000.000 USD** arasında olmalıdır. Likidite/değer oranı en az %3'tür. Son 15 dakikada en az 1.000 USD hacim ve 12 işlem; alışların toplam alış+satış işlem sayısına oranı en az %60 (alış/satış en az 1,5) aranır. Bunlar işlem sayılarıdır; benzersiz alıcı, gerçek para girişi veya wash-trading bulunmadığı iddiası değildir.

**Birikim:** Üç kapalı 15 dakikalık mumda toplam fiyat aralığı en çok %20, mutlak net değişim en çok %10 olmalı. Son mum hacmi ilkin en çok %80'i olmalı; son dip ilk dipten %2'den fazla aşağıda olmamalı. Son kapanış mum aralığının en az %55 seviyesinde olmalı.

**İlk kırılım:** Önceki üç mum yukarıdaki birikim yapısını sağlamalı. Yeni kapalı mum bu alanın tepesini aşmalı; hacim önceki üç mum ortalamasının en az 1,5 katı, kapanış konumu en az %65 olmalı. Kırılan seviyeden uzaklık en çok %12'dir. Eldeki havuz geçmişinde tek mumda %60 üstü yükseliş veya mevcut kapanışta tepeden %25 üstü geri çekilme varsa setup reddedilir. Veriler tüm geçmişi içermiyorsa tokenin hayatında hiç pump olmadığı iddia edilmez.

Açık mumlar kullanılmaz; işlem olmayan aralıklar uydurulmaz. Kesinti varsa özellikler son kesintisiz bölümde yeniden başlar. Güncel likidite önceki gözlemlere göre bir saatte %20'den fazla düşmüşse aday reddedilir.

## Piyasa değeri, cüzdan haritası ve geliştirici

**Market cap ve FDV ayrıdır.** Market cap sağlayıcı bildirimidir; dolaşımdaki arzın bağımsız denetimi değildir. FDV varsa ama market cap yoksa bu açıkça yazılır ve token üst teyitli gruba geçemez. Yeni havuz açılması eski bir tokenin yaşını sıfırlamaz: kayıtlı en eski havuz tarihi korunur. Bu tarih yine de tokenin mint/kontrat yaratılma tarihi değildir. Merkezi borsa listelenme durumu tüm ağlarda bağımsız kontrat eşlemesiyle doğrulanmış değildir; sırf simgesi MEXC/OKX'te var diye farklı bir kontrat elenmez.

**Dağılım:** Sağlayıcıda açıkça tanınan AMM/vault/yakım adresleri ayrılır; her kontrat körlemesine dışarı atılmaz. Solana'da aynı sahibin farklı token hesapları toplanır. Açıklanamayan tek sahip en çok toplam arzın %10'u, ilk on sahip toplamı en çok %35 olmalıdır. Eksik ilk on veri tam ölçüm gibi sunulmaz.

**Bağlantılar — manuel:** Bildirimde ağ, tam kontrat ve Bubblemaps bağlantısı verilir. Solana/Ethereum/BNB için adres içeren harita bağlantısı; Robinhood/HyperEVM için uygulama ana sayfası verilir, bu iki ağda harita desteği doğrulanmış sayılmaz. Harita/ağ bulunamaması temiz sonuç değildir. Kullanıcı haritada LP/CEX adreslerini ayırarak bağlantılı sahipleri, toplam küme payını ve harita zamanını inceler. %20 küme eşiği inceleme için başlangıç referansıdır; otomatik ölçülmüş veya onaylanmış sayılmaz. Transfer bağlantısı tek bir kişinin sahipliği veya kötü niyetinin kanıtı değildir. Kullanıcının manuel onayı sisteme kaydedilmediği için her kayıt harita kontrolü bekliyor olarak kalır.

**Otomatik kaynaklar:** Solana'da RugCheck ile GoPlus Solana çapraz kontrol edilir. Mint/freeze, transfer edilemezlik, hesap dondurma varsayılanı, bakiye değiştirme ve kapanış/yetki alanları incelenir; eksik alan olumlu sayılmaz. Bilinen salt metadata uzantısı tek başına tehlikeli transfer uzantısı sayılmaz; etkin veya çözümlenmemiş özel uzantılar incelemede kalır. Metadata değiştirilebilmesi uyarı olarak gösterilir, orijinallik kanıtı verilmez. Desteklenen EVM ağlarında GoPlus; honeypot, vergi, mint, proxy, gizli sahip, kara/beyaz liste, bakiye değiştirme, duraklatma ve satış kısıtlarını inceler. Sağlayıcı sahte token işareti döndürürse elenir; alanın bulunmaması orijinal olduğunu kanıtlamaz. GMGN'nin tüm sniper/bundler etiketleri ve tam geliştirici geçmişi sağlanmaz.

**Geliştirici:** Risk sağlayıcısının bildirdiği oluşturucu adresi esas alınır. Bu kişinin tüm bağlı cüzdanları kesin tespit edilmiş sayılmaz. Oluşturucu payı %8'den yüksekse elenir. Bakiyesinin sıfır olması satış yapmadığı, yaktığı veya kilitlediği şeklinde yorumlanmaz.

EVM'de doğru ağ kimliği doğrulanır; bildirilen oluşturucu bir kontratsa gerçek geliştirici gibi kabul edilmez. Son 45 dakikayı kapsadığı doğrulanan blok aralığında token çıkışları taranır. Solana'da oluşturucu ve mevcut token hesaplarının imzaları, işlem gövdeleri ve token bakiyeleri incelenir. Sayfa/işlem bütçesi, erişim veya zaman eksikliği varsa durum **bilinmiyor** kalır. Çıkış veya hesap azalması konservatif olarak eler; bunun satış, kendi cüzdanına transfer veya yakım olduğunu otomatik iddia etmez. Dolayısıyla kanıtlı bazı zararsız hareketler de inceleme gerektirebilir. Kilit/yakım konusunda ayrı işlem kanıtı olmadan olumlu teyit üretilmez.

Bu, **son 45 dakikalık gözlenen adres kapsamıdır**; token oluşturulduğundan beri hiç satış yapılmadığı veya satışın başka cüzdandan yapılmadığı kanıtı değildir.

**Likidite kilidi:** Geliştiricinin kendi token kilidiyle karıştırılmaz. RugCheck'te yalnız seçili havuzla eşleşen kilit yüzdesi gösterilir. GoPlus'ın birkaç havuzu birleştirebilen LP sahipliği yüzdesi tek bir havuza mal edilmez. V2 LP tokeni, V3/V4 pozisyon NFT'si ve bonding curve farklı yapılardır. Kilit bilgisi destekleyicidir; eksikliği her protokolde otomatik ret değildir, varlığı da mint/freeze/honeypot sorunlarını geçersiz kılmaz. Bir sağlayıcı kilit yüzdesi gelecekte likidite/çıkış garantisi değildir.

## Eksik veri ve bildirim davranışı

**Otomatik ön eleme / manuel harita bekliyor:** Piyasa yapısı, gerekli kontrat/dağılım alanları ve geliştiricinin son 45 dakikalık penceresi şartları sağlanmışsa bildirilir. Harita şartı kullanıcıya bırakılmıştır; bu açıkça bildirimde yazılır. Bu bir alım emri, harita onayı veya güvenli token onayı değildir.

**İnceleme:** Piyasa yapısı uygun, fakat kritik otomatik kontrat, dağılım veya geliştirici teyitleri eksikse rapora girer; telefona aday bildirimi gönderilmez. Manuel harita seçimi bu eksikleri geçersiz kılmaz. Belirgin kötü risk veya geliştirici çıkışı varsa token reddedilir.

Bu sürümde **GMGN_API_KEY** ve **BUBBLEMAPS_API_KEY** gerekmez. Cüzdan seed/private key gerekmez. GoPlus'ın belgelenen ücretsiz sınırı 30 istek/dakikadır; rapor önbelleği, alan eksikliği ve erişim kısıtları ayrıca gözetilir. RugCheck ücretsiz okuma sorgusu dönebilir; raporu zorla yeniden üretme seçeneği ücretli anahtar ister. Şimdi indirmek bütün alanların yeni hesaplandığı anlamına gelmez.

Genel RPC'ler sınırlı olabilir. İhtiyaç halinde aynı bölüme `MEME_RPC_SOLANA`, `MEME_RPC_ETHEREUM`, `MEME_RPC_BNB`, `MEME_RPC_ROBINHOOD`, `MEME_RPC_HYPEREVM` adlı özel okuma uçları eklenebilir. Boş secret değerleri genel okuma adresine döner. Desteklenmeyen GoPlus ağlarında (ilk kontrolde HyperEVM) güvenlik alanları bilinmiyor kalır; ağın fiyat/havuz takibi devam eder. Sağlayıcı API erişimi veya limitleri değişebilir.

## Ölçüm ve veri kapsamı

### X bağlantısı ve CTO uyarıları

Ek `meme_social_watch.py` modülü DexScreener'ın ağ + tam kontrat + seçili havuz eşleşen metadatasını okur. Ağ başına en çok 20 token sırayla yenilenir; yeni adaylar önceliklidir. İlk ve güncel X bağlantıları ile yalnız gözlem başladıktan sonraki değişiklik sayısı tutulur. Aynı hesabın kalıcı X kullanıcı kimliği veya sahibinin değişmesi doğrulanmaz; geçmiş kullanıcı adı değişikliği sayısı **bilinmiyor** kalır. Profil bağlantısı ile X topluluğu bağlantısı ayrılır. Eksik/malformed yanıt hesap silinmiş gibi yorumlanmaz; X/Twitter alanı dışındaki bağlantılar izlenmez ve tokenin verdiği adrese ağ isteği gönderilmez.

DexScreener'ın sınırlı son topluluk devri akışında eşleşme görülürse **CTO/topluluk devri kaydı** uyarısı eklenir. Kayıt geliştiricinin sattığını, on-chain sahipliğin değiştiğini veya dump geleceğini kanıtlamaz. Akışta görünmemesi CTO olmadığı anlamına gelmez. Geliştirici token çıkışı, likidite kaybı ve teknik güvenlik kontrolleri kendi ayrı kanıtlarıyla değerlendirilir.

İlk aday Issue'sunda sosyal verinin kapsamı/bilinmeyen geçmiş açıkça yer alır. Önceden bildirilen adayda sonradan X bağlantısı değişikliği veya yeni görülen CTO kaydı varsa ayrı, tekrar önleyici işaretli bir uyarı Issue'su açılır. Sadece ilk X gözlemi için uyarı gönderilmez. Bu ek modül seçim puanını, mum kurallarını veya geçmiş giriş fiyatlarını değiştirmez; kendi tasarım karmasıyla sosyal gözlem geçmişini korur. Sosyal veri eksikliği raporda gösterilir, teknik risk eksikliğini geçersiz kılmaz.

İlk inceleme fiyatı ile daha sonra bildirim yapılırsa o an yeniden okunan teyitli fiyat ayrı referanslardır. 15/30/60 dakika, 3/6/24 saat hedefleri sonraki gerçek gözlemle ölçülür. Tabloda hedefe gecikme ayrıca gösterilir; tam o dakikanın mum getirisiymiş gibi sunulmaz. Pencere kaçarsa veya fiyat kaybolursa getiri bilinmiyor kalır. Likiditesi kaybolan/ölçülemeyen tokenler veri kümesinden sessizce çıkarılmaz. Aynı ağ/kontrat, yeni havuz veya birikimden kırılıma geçişle yeni bağımsız coin sayılmaz.

V2 geçişi açıkça yeni dalda başlar. Eski kayıtların havuz yaşı, ilk görülme zamanı ve likidite/fiyat gözlemleri korunur; eski setup/risk sonuçları yeni sürümün sonucu gibi taşınmaz. Önceki sürümde ölçüm/bildirim kaydı varsa geçiş sessizce sıfırlamak yerine durur; ayrı ölçüm taşıma tasarımı gerekir. Kaynak dal/commit/tasarım karması yeni durum dosyasında yazılır.

Ücretsiz GeckoTerminal veri bütçesi dar olduğundan istekler global aralıkla sınırlıdır; her ağda bir döngüde en çok bir uygun havuzun mumları ayrıntılı incelenir. Daha önce az incelenen uygun havuzlara sıra verilir. Rapor güncellenen token sayısını, erişim hatalarını ve mum bütçesini gösterir. Bu sürüm tüm meme piyasasını veya her yeni çıkarılan tokeni taradığı iddiasında değildir. Sadece bu kaynaklarda indekslenen Pons havuzları görülebilir; indekslenmeden önceki tüm curve işlemleri kapsanmış sayılmaz.

Kaynaklar: [DexScreener API](https://docs.dexscreener.com/api/reference), [GeckoTerminal API](https://api.geckoterminal.com/docs/index.html), [RugCheck API şeması](https://api.rugcheck.xyz/swagger/doc.json), [GoPlus API](https://github.com/GoPlusLabs/OpenAPI/blob/main/SecurityAPI.md), [Bubblemaps API şeması](https://github.com/bubblemaps/api-docs/blob/main/openapi.json), [Solana RPC](https://solana.com/docs/rpc/http), [Robinhood ağ bilgisi](https://docs.robinhood.com/chain/connecting/), [HyperEVM](https://hyperliquid.gitbook.io/hyperliquid-docs/onboarding/how-to-use-the-hyperevm), [Pons resmi belgeleri](https://docs.ponsfamily.com).
