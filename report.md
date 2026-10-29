# Coin Tarama 5

Son gözlem: 29.10.2026 11:56 TR.

Bağımsız fiyat + pozisyon davranışı deneyi. 4s genel yapı, 1s hazırlık bağlamı, kapalı 15dk mumla kırılım/geri test; yaklaşık 5dk kamu veri kontrolü. GitHub gecikebilir/atlayabilir. Fiyat düşmezken OI ve kaynak grubun short payı artışı aranır; negatif fonlama yalnız ek destek.

Aktif 0 farklı coin; sınır 5. Hazırlık/tetik aynı coin için iki bağımsız başarı sayılmaz. Eski taramaların hiçbir state dalı okunmaz/yazılmaz.

| Coin | Borsa | Durum | İlk gerçek gözlem TR | Son spot | Sabit direnç | Geçersizlik | Son kontrol TR |
|---|---|---|---|---:|---:|---:|---|

Şu an doğrulanmış hazırlık/tetik yok. İlk OI ve oran bazları yaklaşık 45–75dk aralığında gerçek gözlemler biriktirir; kapsam rotasyonu/sağlayıcı/GitHub gecikmesi bunu uzatabilir.

OKX: {"cursor": 48, "coverage": {"active_spot": 372, "liquid_spot_perpetual": 122, "bounded_universe": 60, "requested": 12, "evaluated": 12, "rotated": 12, "active": 0}, "errors": ["GRVTUSDT BINANCE: BINANCE: public HTTP 451"], "calls": {"spot": 50, "futures": 4, "ratios": {"OKX": 2, "BINANCE": 1}}}

MEXC: {"cursor": 48, "coverage": {"active_spot": 1246, "liquid_spot_perpetual": 111, "bounded_universe": 60, "requested": 12, "evaluated": 12, "rotated": 12, "active": 0}, "errors": [], "calls": {"spot": 51, "futures": 2, "ratios": {"OKX": 0, "BINANCE": 0}}}

## Eleme ve veri durumu

{"4h_structure_weak": 15, "1h_structure_weak": 23, "btc_relative_weak": 20, "oi_growth_insufficient": 22, "short_increase_unconfirmed": 24, "price_not_holding_or_extended": 1, "price_preparation_not_ready": 23}

Bekleyen mesaj: 0. Deneysel eşikler başarı olasılığı değildir; yalnız sinyal sayısını artırmak için değiştirilmez.

Evren her borsada en likit en çok60 spot+USDT perpetual paritesi; her döngüde12 dönüşümlü parite ve aktif adaylar. Tüm piyasa veya her coin her5dk inceleniyor iddiası yok. Tokenleştirilmiş hisseler/stable/leveraged metadata ile elenir. Evren sıralamasında dönüş yapmış coinleri zorunlu kılan 24s pozitif getiri koşulu yok.

Oranlar OKX en büyük %5 pozisyon grubu ve Binance en büyük %20 teminat grubunun pozisyon ağırlıklarıdır. Kaynaklar ayrı kalır, birinde onay yeterlidir; diğeri ters yöndeyse ayrışma açıkça yazılır. Farklı borsa oranı MEXC oranı sayılmaz. Bir saatlik short payı artışı yeni short tutarını kanıtlamaz; grup değişimi/hedge/long azalması etkili olabilir.

Eksik oran/OI pozitif kabul edilmez. Kaynak veya mum hatası destek kaybı sayılmaz; aktif aday son gerçek gözlemiyle kalır. İptal yalnız yeni doğrulanmış fiyat/seviye kaybında; süre dolması ayrı etiketlenir. Açık mum olumlu sinyal üretmez. Destek ve direnç hazırlık anında dondurulur. Tetik hazırlıktan sonraki kapalı15dk mumda değerlendirilir; geçmiş kırılıma yeni tetik yazılmaz.

Öngörülen risk mesafesi en çok%6; tetiğe 1ATR fazla uzamış fiyat takip edilmez. Son24 kapalı4s mumdaki en yakın yukarı tepe biliniyorsa en az2R mesafe aranır; gözlenen yukarı tepe yoksa alan bilinmiyor olarak kalır ve2R kazanç vaat edilmez.

## Gerçek gözlem sonuçları

İlk gerçek hazırlık ve ilk gerçek tetik fiyatları ayrı saklanır; sembol/evre tekrarları yeni bağımsız başarı değildir. Sonuçlar1/4/12/24 saat; BTC farkı, tam sonraki1dk mum yolunda MAE/MFE ve %0.2/%0.5/%1 maliyet senaryoları. Gerçek net kâr veya stop emri gerçekleşmesi değildir; eşlenmiş kontrol coinleri bu sürümde yoktur. Eksik veri bilinmiyor.

| Coin | Evre | Borsa | Gerçek giriş TR | Referans | 1s % | 4s % | 12s % | 24s % |
|---|---|---|---|---:|---:|---:|---:|---:|

Ölçüm hataları: 0. Ölçüm için döngüde en çok2 kayıt; eksik/ara mumlar sıfır veya başarı sayılmaz. Girişten sonraki ilk tam dakika öncesi parça MAE/MFE dışındadır.

## Son olaylar

