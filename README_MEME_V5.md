# Coin Tarama Meme V5

Tek aktif Meme sürümü. EskiV4 state scanner-state-meme-v4 arşivlenir, geçmiş referanslar/değişmez pump dışlama kayıtları V5 migration içinde korunur. Yeni state scanner-state-meme-v5; eski CEX2/3/5 ve Shortçu Kıstır değişmez. V5 pipeline, gözlem ve ölçüm deneyidir; emir/hesap/cüzdan işlemi yapılmaz.

## Uygulanan değişiklikler

Her ağda yeni havuz keşfi en fazla2sayfa, önceki başarılı zaman aralığına5dkörtüşmeyle erişilene kadar. Bütçe yetmezse keşif boşluğu raporda kalır, sonraki turda başarı gibi unutulmaz. Yaşı15dkaltı kimliği belli havuzlar yalnız gözlem listesine alınır.15–120dkyaş aralığı ve uygun yaşa yaklaşanlar öncelikliyenilenir; her tur ençok30eski pool/ağ ve180saklanan kayıt/ağ. OI/para girişi bu DEX senaryosuna uydurulmaz.

Mum incelemesi artık tüm hacim/işlem sayısı kapılarını beklemez: bilinen likiditesi>=10binUSD ve uygun yaşı olan riskli olarak işaretlenmemiş havuzlarda veri okumaya izin verilir. Bu koşul olumlu aday kapısı değildir. Her ağda3OHLCVisteği,1güvenlik değerlendirmesi; bütçe dışında kalanlar sayılır. Mum okunması, ilkpump/eksikbaşlangıç/sıkışma analizi ve güvenlik değerlendirmesi ayrı raporlanır.

Olumlu adayda eski **piyasa, ilk-pump, güvenlik, geliştirici45dk ve manuel harita gereksinimleri aynen korunur**. Hacim15>=1000USD,>=12işlem,%60alımadedi vb eşikler bu revizyonda gevşetilmedi. Önce yenikeşif ve zamanlama etkisi ölçülecek. Eksik risk onay değildir; desteklenmeyen ağ olumlu aday üretmez. Yeni aday yalnız erkenbirikim; ilk kez pump/kırılım sonrası karşılaşılan token elenir. Kalıcı pump dışlaması havuz/kontrat ismiyenilenince kalkmaz.5dk3tam mum≈15–20dk,15dk3tam mum≈45–60dk+veri/çalışma gecikmesi;ilk15dkpumpınıöncedenyakalamaiddiasıyok.

Otomatik onay, devin ömür boyu satmadığı, tam bağlantılı cüzdan haritası, resmî kontrat veya risksiz token garantisi yok. Büyük alıcı desteği aynı bounded işlem örneğidir; servet/bağımsız kişi/smart money kanıtı değildir. İlk kırılım ancak önceden gerçek birikim bildirimi gönderildiyse devam bildirimi olabilir; pending veya eski kâğıt referans teslim edilmiş sayılmaz. Bot Issue marker'ı ile kabul edilmiş POST tekrarında uzlaştırma yapılır. Bayat veya yeni kritik riskli aday mesajı gönderilmez.

## Çalışma düzeni

Aynı coin-tarama-meme.yml iş akışı saatlik tetiklenir ve **en çok110dakikalık bir worker oturumu** çalıştırır. Varsayılan hedef her300saniyede yeni turdur; tur5dkdanuzunsa bunun üstüne ek bekleme konmaz ve gerçekaralık raporlanır. Oturumdan sonra yeni cron işi sıradan devam edebilir; concurrencyfalse ile aynıstate'e iki iş yazmaz. GitHub'ın başlangıç/yenileme/queue gecikmeleri bitmiş değildir; kesintisiz5dkgarantisi verilmez. İlk24saate ait gerçektur aralıklarınınp95<=7dk hedefi raporlanır;24saatdolmadan tamgünbaşarıiddiasıyok. Runoluşturulma,jobbaşlangıcı,workerbaşlangıcı,scanbaşlangıç/bitişi ayrı kaydedilir.

Yalnız public repository ve standart ubuntu-latest runner; bu mod GitHubstandartpublic kullanımücretsizliği doğrulanarak devreye alınır. Private depoya geçilirse dakika bütçesi ayrıca değerlendirilmeden bu sürelerle devam edilmemeli. Oturum süresi1–110dkvalidasyonludur,jobtimeout125dk. Yeni servis/ücretli sağlayıcı/kalıcı APIanahtarı alınmadı. Yerelkurulum aynı worker komutuyla mümkündür ancak makinenin açık/çevrimiçi olması ve güvenli GitHub izinleri ayrıca gerekir; yerelkalıcıservis bu revizyonda kurulmadı.

GeckoTerminal çağrıları süreç içinde host başına12.5snarayla ve tarama+ekölçümler için toplam20istek bütçesiyle sınırlı; yaklaşık4.8istek/dk, güncel30/dkresmîlimiti ve bazı eski10/dkbilgilerinin altında ihtiyatlıbütçe.401/403/418/429sonrası sağlayıcı o turdurur,proxy/anahtar/bölgeengeli aşılmaz. Her tur yeni client ile sonraki normalzaman diliminde tekrar denenebilir; sonsuzhızlıretryyok.

## Ölçüm ve gerçek sınırlamalar

İlkgerçek erkenaday ve15dkteyit referansı ayrı kaydedilir. Aynıchain/mint/evre tekrarları yeni bağımsızörnek değildir. GeçmişV4girişleri V5gibi sunulmaz; previous_v4ileayrıkorunur. Havuzkimliği değişirse sabitmiktarsatışölçümü yeni havuzfiyatını eskiyatırımın çıkışı saymaz.

100USD/500USD varsayımsalnotional için ilkgerçeksağlayıcıfiyatından tokenmiktarı hesaplanır ve sabit kalır; gerçekalımswapı yoktur. Aynı tokenmiktarıyla sonraki saltokunur Raydium/KyberSwap satışkotasyonları alınır. Tamvergi/alımgerçekleşmesi/gas/maliyetler doğrulanmadığından **net gerçekleşmişkâr bilinmiyor**. USDCotomatik1USDsayılmaz; SolanaquoteUSDCmiktarıUSDdeğeri olarak etiketlenmez. Rota bulunamaması risksiz/satılabilir sonuç değildir.

Sabitgösterge çıkışdeneyi: gözlenen satışkotasyonundagross-%10stop veya+%20hedef veya60dkzaman aşımı. Hazırlıkkutusualtı fiyatkaybı varsa ve güncel gösterge satışkotasyonu bulunuyorsa yapısalçıkışetiketi ayrıca verilir. Eşikler doğrulanmışavantaj değildir, gözlemler başlamadan dondurulmuştur. Aradaki5dk içinde hangi seviyeönceoldu bilinmez; sürekli izlenmiş/garantifillkârı yok. Alışmaliyetibasıödenmediğindenbaşarıkesinliği yok.10/30/60/240dkgerçekgözlem hedefleri7dkgecikmepenceresiyle ölçülür; kaçırılanpencerebilinmiyor.

Kapalı5dkbarlarla ek MAE/MFE **altpenceresi**: ilkgerçekgirişten sonraki ilk tam5dkmumdan sonkapalı5dkmuma kadar. Başlangıç/güncel parçalar ve eksikara mumvarsa sonuçsınırları açık; tamtradepathMAE/MFEiddiasıyok. Yalnızgözlenenfiyatmax/min ayrıca ayrıdır. Döngüde2ölçümkaydı; verieksikliği0kâryazılmaz. İlk20farklıtoken tamamlanmışsonuç inceleme eşiğidir, istatistikselkanıtdeğil. Güvenlikbilinmeyenve incelemekayıtları normalolumluaday mesajı olarak gönderilmez.

## Doğrulama

85önceki güvenlik/mum/sosyal/risk testleri ayrı süreçte, V5testleri ayrı süreçte çalışır. V5hedefleri: piyasaelenen tokenın mum verisi okunabilsin ama bildirimverilmesin; erkenyaş tekrarziyareti; kapsam boşluğu; V4referans/latchkoruma; sabitmiktar; eksikrota/maliyetUSDC; bayatbildirim vePOSTretryuzlaştırma. İlkcanlıdenemede raporkapsamı ve gerçekarayankifark doğrulanır, adayuydurulmaz.

Kaynaklar: [GitHub schedule gecikmesi](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule), [public standart runner ücretsizliği](https://docs.github.com/en/billing/concepts/product-billing/github-actions), [GeckoTerminal30istek/dklimiti](https://support.coingecko.com/articles/6867086195-does-geckoterminal-have-an-api). Hiçbir ücretli APIaboneliği başlatılmadı.

Canlı yereldenemede429görüldü; sağlayıcı o turdurdu. Sonraki üretim tasarımında12.5sn aralık,global20istek/turbütçesi,429sonrası15dkbekleme vegerçekmumokuma/istekdenemesiayrımı eklendi. Bekleme sırasında5dkhedefisağlanmışsayılmaz.

Meme aday bildirimlerinde ağ adı ve tam token kontratı ayrı text kod kutusundadır; kısaltma uygulanmaz. Havuz adresi DexScreener bağlantısında kalır. Adres biçimi/ağ kontrolü resmî token kimliği onayı değildir. Borsa taramalarının bildirimi bu değişiklikten etkilenmez.
