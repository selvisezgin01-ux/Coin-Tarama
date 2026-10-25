# MEXC + OKX coin taraması — GitHub kurulumu

## Coin Tarama Meme — ayrı DEX deneyi

Solana, Ethereum, BNB Chain, Robinhood/Pons ve HyperEVM için 15 dakikalık birikim/ilk kırılım deneyi ayrı çalışır. [Meme raporu](https://github.com/selvisezgin01-ux/Coin-Tarama/blob/scanner-state-meme-v2/report.md) · [Kurallar ve veri erişimi](COIN_TARAMA_MEME.md).

GoPlus/RugCheck ile otomatik risk ön elemesi yapılır; **Bubblemaps haritasını kullanıcı manuel kontrol eder**. Bildirimler harita onayı bekleyen ön eleme adaylarıdır. Kritik kontrat/dağılım/geliştirici verisi eksikse aday bildirilmez. GMGN/Bubblemaps API anahtarı gerekmez; GMGN'nin tüm özel cüzdan etiketleri sağlanmaz. Likidite kilidi yardımcı bilgidir. İlk Meme deneyi `scanner-state-meme` dalında korunur; bu güncelleme Coin Tarama 2/3'ü değiştirmez.

Ek sosyal gözlem modülü, ilk gözlemden sonraki X bağlantı değişikliklerini ve DexScreener topluluk devri/CTO kayıtlarını raporlar. Geçmiş tüm kullanıcı adı değişiklikleri ve geliştiricinin sattığı bu verilerle kanıtlanmaz. Önceden bildirilen adayda yeni bir sosyal değişiklik görülürse ek uyarı Issue'su açılır; veri eksikliği temiz geçmiş sayılmaz.

## İki ayrı çalışan sürüm

**Coin Tarama 2** önceki V3 formülüyle, **Coin Tarama 3** yeni kırılım/tutunma gruplarıyla ayrı çalışır. İkisi de MEXC ve OKX'i dört saatte bir tarar. Bildirim başlıklarında sürüm adı görünür. Kalıcı kayıtlar ayrı dallardadır; ilk gerçek gözlemden sonraki 12/24/48 saat ölçümleri raporlara eklenir. Aynı coin grup değiştirdiğinde bağımsız ikinci performans örneği olmaz.

- [Coin Tarama 2 raporu](https://github.com/selvisezgin01-ux/Coin-Tarama/blob/scanner-state/report.md)
- [Coin Tarama 3 raporu](https://github.com/selvisezgin01-ux/Coin-Tarama/blob/scanner-state-v4/report.md)
- [Coin Tarama 3 kuralları, deney ve karşılaştırma planı](COIN_TARAMA_3.md)

Yeni sürüm deneysel olup arşiv kontrolünde toplu üstünlük göstermedi. 26 Ekim başlangıcından 1–2 hafta sonra, yaklaşık 2–9 Kasım 2026 arasında gerçek gözlem sonuçlarını karşılaştıracağız. Önceki yerel araştırma pilotlarının kayıtları korunur.

Bu paket, bilgisayarınız kapalıyken GitHub Actions üzerinde iki borsayı taramak içindir. ChatGPT/Codex uygulamasındaki takipten bağımsızdır; herhangi bir yapay zekâ servisi veya borsa hesabı anahtarı gerekmez.

Yükselişi yeni başlamış, BTC'ye göre güçlü ve kapalı 4 saatlik mum koşullarını sağlayan spot/USDT coinlerini arar. Araştırmadaki seçim formülü aynıdır. Yeni sürümün gelecekte kazandıracağı doğrulanmış değildir. Bu canlı izleyicide 50 coin sınırı yoktur; yerel araştırmanın 12/24/48 saatlik deney raporunu bu paket oluşturmaz.

## Issue nedir?

Issue, GitHub'da bir kayıt sayfasıdır. Hata, soru, yapılacak iş veya sonuç duyurusu için kullanılabilir. Bu projede **“Yeni coin adayları — tarih/saat”** başlıklı bir tarama kaydı olarak kullanılır. “Program hata verdi” anlamına gelmez.

GitHub'ın standart Actions bildirimleri taramanın çalışma durumunu bildirir. Yeni coinlerin listesini bildirmek için Issue seçeneği veya Telegram seçeneği vardır. Başlangıçta yalnız rapor seçeneği açıktır; hiçbir dış mesaj gönderilmez.

## İlk kurulum: hesabı açtıktan sonra

1. GitHub'da sağ üstteki **+ → New repository** seçeneğini açın.
2. Depo adına örneğin **coin-tarama** yazın. **Private** seçebilirsiniz. Depoyu oluşturun.
3. Size verilen ZIP'i bilgisayarda **çıkarın**. ZIP dosyasını GitHub'a olduğu gibi yüklemeyin; GitHub onu kendiliğinden kod olarak açmaz.
4. Depoda **Add file → Upload files** seçeneğiyle çıkarılan paketin içeriğini yükleyin. `.github` klasörü ve içindeki `workflows/coin-scan.yml` de yüklenmeli; dosyalar `main` gibi varsayılan dalda olmalı.
5. Alttaki **Commit changes** düğmesiyle kaydedin.
6. Depoda **Settings → Actions → General → Workflow permissions** bölümünde **Read and write permissions** seçip kaydedin. Otomasyon yalnız kendi `scanner-state` dalına durum/rapor yazar; Issue açma seçeneği için de iş akışında izin tanımlıdır.
7. **Actions → MEXC + OKX coin scanner → Run workflow → Run workflow** ile ilk taramayı elle başlatın. Actions devre dışı görünüyorsa bu depo için etkinleştirin.
8. Çalışma bitince sayfanın özetinde aday listesini görebilirsiniz. **Artifacts** bölümünden raporu da indirebilirsiniz. Son başarılı durum ve rapor, dal seçicisinden ulaşılabilen **scanner-state** dalındadır.

Repo bağlantısını paylaşırsanız sonraki adımları o ekrana göre birlikte yapabiliriz. GitHub parolanızı, kişisel erişim tokeninizi veya Telegram bot tokeninizi sohbete yazmayın.

## Issue bildirimi açma — Telegram gerekmez

1. **Settings → Secrets and variables → Actions → Variables → New repository variable** seçeneğini açın.
2. **Name:** `NOTIFICATION_CHANNEL`
3. **Value:** `github_issue`
4. Kaydedin.
5. Depo sayfasındaki **Watch → Custom → Issues** seçeneğini açın veya tüm etkinlikleri izleyin.
6. GitHub hesabınızın **Settings → Notifications** bölümünden e-posta bildirimlerini açın; hesap e-postanızı doğrulayın.

Yeni aday gelirse otomasyon başlığı ve coin listesini içeren bir Issue oluşturur. E-posta/GitHub bildiriminin ulaşması izleme ve hesap bildirim ayarlarına bağlıdır. Yeni aday yoksa Issue oluşturulmaz. İlk çalışmada o anda koşulları sağlayan adaylar ilk kez görülmüş kabul edilir.

Telefonda anlık bildirim için aynı Variables bölümüne `COIN_NOTIFY_USER` adlı değişkeni ekleyin; değerine GitHub kullanıcı adınızı `@` olmadan yazın. Yeni aday Issue'larının başında bu kullanıcı etiketlenir. Bu depoda alıcı `selvisezgin01-ux` olarak ayarlanmıştır. GitHub Mobile uygulamasında doğrudan etiketlenme bildirimlerini ve telefon ayarlarından GitHub için bildirim/ses izinlerini açın. Ses ve teslim zamanı telefonun sessiz/odak modu ve uygulama ayarlarına bağlıdır; kod telefonun ses ayarlarını değiştiremez. [GitHub Mobile bildirimleri](https://docs.github.com/en/subscriptions-and-notifications/get-started/configuring-notifications#managing-your-notification-settings-with-github-mobile)

Her dört saatte çalışma-durumu e-postası almak istemiyorsanız GitHub Actions bildirimlerini yalnız başarısız çalışmalara ayarlayabilirsiniz; coin sonuçları Issue üzerinden gelir. Hata durumunda Actions sayfasının kırmızı/başarısız durumu ayrıca kontrol edilir.

## Telegram seçeneği — isteğe bağlı

1. Telegram'da resmi **@BotFather** ile `/newbot` komutundan bir bot oluşturun.
2. Oluşturduğunuz bota gidip **Start / Başlat** düğmesine basın.
3. Botun API tokenini ve size ait sohbetin `chat_id` değerini alın. `chat_id`, resmi Bot API `getUpdates` yanıtındaki `message.chat.id` alanından öğrenilebilir. Tokeni üçüncü kişilere göndermeyin.
4. Depoda **Settings → Secrets and variables → Actions → Secrets → New repository secret** üzerinden `TELEGRAM_BOT_TOKEN` ve `TELEGRAM_CHAT_ID` adlı iki secret ekleyin.
5. **Variables** bölümündeki `NOTIFICATION_CHANNEL` değerini `telegram` yapın.

Telegram'a yalnız yeni aday paketleri gönderilir. Sunucuyu sürekli açık tutan bir bot programına ihtiyaç yoktur; GitHub çalışması mesajı Bot API üzerinden gönderir. Telegram seçeneği etkinken Issue oluşturulmaz. `NOTIFICATION_CHANNEL=report` bildirimi kapatır, rapor üretimini sürdürür.

## Saatler ve “yeni aday” tanımı

- Türkiye saatiyle **03:05, 07:05, 11:05, 15:05, 19:05, 23:05**.
- GitHub zamanlaması gecikebilir; kesin saniyede çalışma garantisi yoktur. Gözlem saati raporda gösterilir.
- Sürekli listede duran coin yeniden bildirilmez. Listeden çıkıp tekrar giren bir coin için önceki bildirimden itibaren **48 saat** bekleme vardır.
- Aynı coin iki borsada da görünürse borsa etiketleri korunur; iki bağımsız başarı gibi değerlendirilmez.
- MEXC ve OKX kendi fiyat/hacim/BTC verileriyle incelenir. Hacmi düşük veya güncel makası geniş adaylar mesajda işaretlenir.
- Yalnız 24 saat getirisi %0–35 ve hacmi en az 10.000 USDT olan ön eleme ayrıntılı incelenir; tüm aktif tokenler mutlaka aday değildir.

## Kalıcı kayıt ve arızalar

GitHub her çalışmada yeni bir makine açabilir. Tekrar bildirimlerini önleyen kayıt, geçici önbellek yerine deponun **scanner-state** dalında `state.json` olarak saklanır. Bu dalı silmek geçmiş görülenler kaydını sıfırlar. Ana kod dalına otomatik veri eklenmez. Bildirimden önce aday kaydı saklanır; teslimat hatasında bekleyen mesaj sonraki çalışmada yeniden denenir. Teslimattan hemen sonra kayıt yazılamazsa nadiren tekrar mesaj gelebilir; kusursuz tek teslim garantisi yoktur.

Bir borsa hata verirse diğerinin taraması sürer; hata veren borsanın eski aktif listesi korunur. İş akışı sonunda bu durum başarısız olarak işaretlenir. Yeni bir depoda GitHub sunucularından borsa API'lerine erişim ilk çalışmada doğrulanmalıdır.

Bu deponun ilk GitHub çalışması 25 Ekim 2026'da başarıyla tamamlandı: [çalıştırma kaydı](https://github.com/selvisezgin01-ux/Coin-Tarama/actions/runs/40229975805). Her iki borsa okundu; rapor ve kalıcı durum dalı kaydedildi. Bu depoda `NOTIFICATION_CHANNEL=github_issue` etkinleştirilmiştir. İlk deneme rapor modunda başlatıldığı için sonraki yeni adaylar Issue olarak bildirilecektir. Güncel rapor `scanner-state` dalındaki `report.md` dosyasıdır. E-posta teslimi hesabın bildirim tercihlerine bağlıdır.

Formül veya veri dönüştürme kodu değişirse eski kayıtla sessizce karıştırılmaz; tasarım karması kontrolü durdurur. Yeni bir sürüm için `SCANNER_STATE_BRANCH` değişkenini örneğin `scanner-state-v2` yaparak ayrı kayıt başlatabilirsiniz. Eski dalı karşılaştırma için koruyun.

GitHub hesabınızın Actions kullanım kotası ve kuralları geçerlidir. Zamanlanmış çalışmayı depodaki Actions sayfasından kapatabilirsiniz. GitHub sürümünü kapatmak Codex içindeki yerel otomasyonu etkilemez; onlar ayrı takiplerdir.

## Kaynaklar

- [GitHub: çalışma bildirimleri](https://docs.github.com/en/actions/concepts/workflows-and-actions/notifications-for-workflow-runs)
- [GitHub: zamanlanmış iş akışları](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)
- [Telegram: resmi bot oluşturma rehberi](https://core.telegram.org/bots/tutorial)
- [Telegram: resmi Bot API](https://core.telegram.org/bots/api#sendmessage)

## Dosyalar

`github_scan.py` bulut izleme/bildirim/kayıt işlerini; `.github/workflows/coin-scan.yml` zamanlamayı yönetir. `momentum_scan.py` ve `okx_scan.py` araştırmada kullanılan değiştirilmeyen tarama özelliklerini sağlar. Bağımlılıklar `requirements.txt` içindedir. Hesap veya emir işlemi yoktur.

Yerel davranış kontrolleri: `python -m unittest test_github_scan -v`.
