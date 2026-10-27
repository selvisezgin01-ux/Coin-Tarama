# Shortçu Kıstır — dinamik short payı takibi

Kullanıcı, takipteki adayda anlamlı oran değiştiğinde ayrı bildirim istedi. Pozisyon büyüklüğüne dayalı oranlar kullanılır; fonlama/OI değişimi short yüzdesi olarak gösterilmez. Mevcut aday formülü, gerçek fiyat referansları ve ücretsiz karşılaştırma deneyi değiştirilmez.

## Ücretsiz veri kapsamı

- OKX: açık pozisyon değeri en büyük %5 yatırımcı grubunun **pozisyon** long/short oranı. En kısa belgelenmiş aralık 5m.
- Binance: teminat bakiyesi en büyük %20 yatırımcı grubunun **pozisyon** long/short oranı. En kısa belgelenmiş aralık 5m. Dokümantasyon API key gereksinimi gösterebilir; bu kurulumda anonim kamu okuması canlı testte çalışmıştır. Erişim 401/403/418/429/451 veya anahtar talebiyle reddedilirse durulur; kısıt aşılmaz, anahtar/cüzdan/hesap erişimi eklenmez.
- MEXC toplam short yüzdesi sağlandığı iddia edilmez. MEXC adayı için OKX/Binance verisi mevcutsa **kaynak adı ve grubuyla ayrı** gösterilir. İki kaynak farklı popülasyonlardır; toplanmaz veya ortalanmaz. Hesap sayısı veya tüm piyasanın yön bazlı toplamı değildir.
- Tam sembolle aktif linear USDT perpetual doğrulanır; 1000TOKEN dönüşümü yapılmaz. Sembol eşleşmesi farklı borsalarda bağımsız token kontrat kimliği doğrulaması değildir. Grup üyeleri zamanla değişebilir; oran değişimi yeni short açıldığını veya aynı yatırımcıların short büyüttüğünü tek başına kanıtlamaz.

## Bildirim ve örnek

Sadece Shortçu Kıstır üretiminde gerçekten bildirilmiş adaylar, bildirim kaydından sonra 24 saat izlenir. İnceleme/teknik havuz veya sessiz A/B deneyi tek başına izleme başlatmaz. En çok 10 yakın tarihli sembol izlenir; kapsam dışı sayısı raporlanır.

İlk canlı veri başlangıç noktasıdır, geçmişe değişim bildirimi yazılmaz. Son bildirilen/ilk gözlenen short payına göre **2 yüzde puan** değişim veya %50 seviyesinin geçilmesi anlamlı kabul edilir. Küçük değişimler birikerek eşiği aşabilir. Aynı sağlayıcı zaman damgalı düzeltme yeni dönem sayılmaz.

Örnek, gerçek aday değildir:

```
Short payı yükseliyor: %60.00 → %65.00
Değişim: +5.00 yüzde puan; göreli +%8.33
Son long payı: %35.00
Kaynak: OKX en büyük %5 grubu / pozisyon büyüklüğü
Veri: önceki saat → yeni saat (gerçek aralık)
Kontrol: bizim okuduğumuz saat
```

Short payı `100/(1+longShortRatio)` ile, long payı `100-short` ile türetilir. Önceki short payı sıfırsa göreli değişim tanımsızdır. Oran düşüşünde negatif yüzde puan ve göreli değişim gösterilir. “Short payı azalıyor” shortların mutlak parasal tutarının azaldığı anlamına gelmez.

## Çalışma ve kayıt

Ayrı `shortcu-position-monitor.yml`, yaklaşık her 5 dakikada bir ve ana Shortçu Kıstır tamamlandığında çalışır. GitHub gecikebilir veya bir çalışma atlanabilir; gerçek zamanlı/kesintisiz bildirim garantisi yoktur. Mesaj verinin iki sağlayıcı zamanını ve kontrol saatini ayrı gösterir. Yeni değişim, bizim tespit ettiğimiz anda bildirilir; tam oluşum anı biliniyor iddiası yoktur.

Ayrı durum/rapor: `scanner-state-shortcu-positions`. Üretim `scanner-state-shortcu-kistir` yalnız okunur; hiçbir eski üretim veya deney alanı değiştirilmez. Yalnız kendi GitHub Issue bildirimleri vardır; genel kanal report ise bildirim gönderilmez. Telegram bu ek modülde etkin değildir. Güncelleme mesajları yeni aday/alım/satım sinyali değildir.

Kaynak eksik/eski/desteksizse bilinmiyor; son geçerli veri güncelmiş gibi gösterilmez. Özel API/ücretli servis yoktur. İki kaynaktan biri erişilemiyorsa diğeri sürer ve kapsam eksikliği raporda görünür. Hiçbir aktif adayın verisi alınamıyorsa iş başarısız olarak işaretlenir; desteklenmeyen kontrat yoklukları gerçek sıfır short oranına dönüştürülmez.

Kaynaklar: [OKX pozisyon grubu](https://www.okx.com/en-us/help/how-do-i-use-the-top-position-long-short-ratio-indicator), [OKX kamu API](https://www.okx.com/docs-v5/en/), [Binance pozisyon API](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio), [GitHub schedule](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).
