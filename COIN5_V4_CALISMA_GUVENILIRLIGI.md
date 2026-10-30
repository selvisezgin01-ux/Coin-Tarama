# Coin Tarama 5 V4 — kayıt ve süreç kurtarma

Bu değişiklik sinyal/ölçüm kurallarını değiştirmez. V4 kural fingerprint'i
`a037f92f3df635673a8f8a00f16adf14d5f7957088fdc5e046a7043f7251d685`
ve mevcut state dalı korunur. Yeni finansal deney veya geriye dönük giriş yoktur.

## Güvenli kayıt tekrarı

- Her checkpoint önce aynı yerel gözlem snapshot'ını ve kimlik bilgisi
  içermeyen gönderim günlüğünü saklar. Bir kez hazırlanmış aynı commit denenir.
- Göndermeden önce uzak dalın beklenen önceki commit veya aynı hazırlanmış
  commit olduğu doğrulanır. Kayıt kabul edilip cevap kaybolduysa tekrar gönderilmez.
- Ağ/zaman aşımı/geçici HTTP hatalarında toplam dört deneme, aralarda5/15/30s
  bekleme; checkpoint için toplam120s bütçe vardır. Alt Git çağrıları en fazla30s.
- Yetki hatası, beklenmeyen başka yazar, non-fast-forward veya bilinmeyen hata
  zorla yazılmaz. Force-push, kör rebase veya eski fiyatları değiştiren birleştirme yok.
- Git hata ayrıntısı, çıkış kodu ve sınıfı token/Authorization/URL şifreleri
  maskelenerek GitHub çalışma günlüğüne ve publication_health.json dosyasına yazılır.

## Kontrollü yeniden başlatma

- Aynı GitHub işi içinde, geçici hatayla biten tarayıcı20s sonra en fazla bir
  kez yeniden başlatılır. Beklenmeyen normal süreç çökmesine de tek deneme tanınır.
- Yetki/kural/çakışma hataları ve elle iptal otomatik yeniden başlatılmaz.
- Yeni süreç yalnız başlangıçta ayrılmış oturum süresinin kalanını kullanır.
  Tekrar başlayınca110dakika daha eklemez; aynı concurrency grubunda tek yazar kalır.
- Aynı işin doğrulanmış yerel snapshot'ı, uzak dal hâlâ beklenen parent ise
  özgün fiyat/zaman/pending/makbuz kimlikleriyle korunur. Uzak kayıt zaten kabul
  edilmişse o kayıt kullanılır. Başka bir işin veya değişmiş uzak dalın verisi
  yeniden oynatılmaz. Geçersiz/kısmi run tamamlanmış gibi gösterilmez.
- Bildirimlerin mevcut bot-marker uzlaştırması aynen sürer. Gecikmiş eski bir
  aday yeni fiyat/saatle taze giriş diye sunulmaz; bildirim yaş sınırı korunur.
- İlk checkpoint'te runtime_policy, sonraki checkpoint'te önceki gerçek başarılı
  yayın bilgisi kaydedilir. operational_recoveries/process_restarts fiyat değiştirmez.

## Kapsam sınırı

Bu önlemler tüm GitHub sunucusunun/runner'ın kapanmasını veya zamanlayıcı
gecikmesini ortadan kaldırmaz. Süpervizör aynı işte yaşadığı sürece hızlı
yeniden başlatır. Kalıcı yetki ve başka-yazar sorunları güvenli biçimde durur;
sonsuz yeniden başlatma yoktur.5dakika hedefi kesintisiz kapsam garantisi değildir.
Eski başarısız işin17:18–18:14boşluğu geriye dönük düzeltilmiş sayılmaz.

Üretimde arıza bilerek çıkarılmaz. Geçici hata, kayıp cevap, çakışma ve tekrar
başlatma senaryoları izole testlerde denenir; ilk normal gerçek döngü ayrıca doğrulanır.
