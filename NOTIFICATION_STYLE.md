# Bildirimlerde teyit görünümü

- 🟢🎯 **GİRİŞ TEYİDİ**: gerçekten bu evrede üretilen giriş teyidi. Coin5 V3
  geri test girişi mesajında başlık, üst banner ve ilgili satır vurgulanır.
- 🟦✅ **Teknik teyit**: Meme15dk fiyat teyidi +5dk alım akışı veya tutunma.
  Teknik teyit, emir/giriş gerçekleşmesi veya güvenli token garantisi değildir.
- Erken radar, normal ALIM/SATIŞ işlemi, iptal ve TEST mesajları giriş teyidine
  dönüştürülmez. Karma mesajda yalnız gerçek teyit satırı vurgulanır.

Ortak GitHub gönderim katmanı `notification_style.outgoing` kullanır. Yalnız
bu deponun Issue title/body sunumuna uygulanır; fiyat, stop, hedef, evre,
kurallar, state referansları ve gönderim markerları korunur. Telegram ve diğer
API isteği verileri değiştirilmez. İşlem stratejisi fingerprintleri değişmez.

`python -m unittest test_notification_style -q`

Uzun süren mevcut Python oturumları eski gönderim kodunu bellekte tutabilir.
Yeni oturumlar yeni biçimi otomatik alır. Değişen geçmiş teyit mesajları
yeniden yeni sinyal gönderilmiş sayılmaz.
