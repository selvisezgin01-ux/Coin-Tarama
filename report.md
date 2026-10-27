# Shortçu Kıstır — dinamik pozisyon oranı takibi

Son kontrol: 28.10.2026 01:20 TR.

**Yalnız gerçekten bildirilmiş Shortçu Kıstır adayları. Yeni aday seçimi veya alım/satım sinyali değildir.**

OKX: pozisyon değeri en büyük %5 grubunun pozisyon oranı. Binance: teminat bakiyesi en büyük %20 grubunun pozisyon oranı. Hesap sayısı veya tüm piyasanın toplam short yüzdesi değildir; iki kaynak ortalanmaz. Aday MEXC fiyatından seçilmiş olsa da OKX/Binance oranı MEXC oranı olarak adlandırılmaz.

0 aktif sembol; son aday bildiriminin ardından 24 saat, çalışmada en çok 10 sembol. İlk canlı gözlem yalnız başlangıç oluşturur; geçmişe bildirim yazılmaz.

| Coin | Aday borsası | Oran kaynağı | Son geçerli short % | Long % | Veri TR | Kontrol durumu |
|---|---|---|---:|---:|---|---|

Henüz son 24 saatte bildirilmiş, referansı doğrulanabilen aday yok; oran izleme listesi boş.

Anlamlı değişim: son bildirilen/ilk gözlenen short payına göre en az 2 yüzde puan veya %50 seviyesinin geçilmesi. Küçük değişimler birikerek eşiğe ulaşabilir. Aynı zaman damgalı revizyon yeni dönem gibi bildirilmez.

Örnek (gerçek aday değildir): short %60 → %65 = +5 yüzde puan, göreli +%8.33; long %35. Önceki short %0 ise göreli değişim tanımsızdır; uydurulmaz.

API verisinin en kısa istenen aralığı 5dk. GitHub yaklaşık 5dk kontrol için planlanır; gecikme/atlama olabilir. Mesaj iki gerçek sağlayıcı zaman damgasını ve kontrol saatini gösterir; her değişimin oluştuğu anı veya kesintisiz her 5dk gözlemi bildiği iddia edilmez.

Eksik, eski, desteklenmeyen veya erişimi engellenen veri bilinmiyor kalır. Binance anonim erişimi değişebilir; API anahtarı/erişim istendiğinde durulur, kısıt aşılmaz. Özel hesap/emir veya ücretli veri erişimi yoktur. Sembol eşleşmesi token kontrat kimliğinin bağımsız doğrulaması değildir.

Kapsam: {"delivered_candidates_in_window": 0, "unresolved_references": 0, "outside_request_budget": 0}
Bekleyen anlamlı değişim: 0; erişim/veri sorunu: 0.

[OKX kapsam](https://www.okx.com/en-us/help/how-do-i-use-the-top-position-long-short-ratio-indicator) · [Binance pozisyon oranı](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Top-Trader-Long-Short-Ratio)
