# Shortçu Kıstır

Son çalışma: 28.10.2026 23:46 TR.

**Coin Tarama 3 teknik temelinden beslenen bağımsız deney. Short pozisyon açılmaz; yükseliş yönlü olası short sıkışması aranır. Başarı garantisi yoktur.**

Teknik işlem koşullarından geçen 23 borsa kaydı; squeeze koşullarını sağlayan en çok 5 farklı sembol; güncel liste 0.

Kaynak: Coin Tarama 3 tamamlandığında scanner-state-v5 dalından okunur. Kaynak adaylar, eski ölçümler ve beşli öncelik listesi değiştirilmez. Eski fiyatlar yeni sinyalin referansı değildir.

| Coin | Borsa | Gerçek spot gözlemi TR | Spot fiyat | Fonlama / dönem | OI değişimi | Gerçek aralık |
|---|---|---|---:|---|---:|---|

Şu an tüm koşulları doğrulanan aday yok. Veri birikimi/erişim eksikliği ile koşul sağlanmaması aşağıda ayrılır.

## Veri birikimi ve eleme nedenleri

- 20 borsa kaydı: yeterince negatif fonlama yok
- 3 borsa kaydı: aynı borsada eşleşen aktif USDT sürekli vadeli kontrat yok
- 18 borsa kaydı: toplam açık pozisyon artışı yetersiz
- 5 borsa kaydı: açık pozisyon büyüklüğü yetersiz

Bir kayıtta birden çok neden olabilir. Şu anki fonlama ve OI, başarısız teknik filtreleri geçersiz kılmaz.

- OKX: 511 güncel vadeli OI kaydı; 11 fonlama incelemesi; 0 erişim/veri hatası.
- MEXC: 1084 güncel vadeli OI kaydı; 9 fonlama incelemesi; 0 erişim/veri hatası.

## Dondurulmuş başlangıç kuralları

Coin Tarama 3 geniş aday havuzuna mevcut işlem koşulu elemesi uygulanır; eski beşli sınırı öncesindeki uygun adaylar değerlendirilir. Yalnız hazırlık grubu tek başına bildirilmez. Aynı borsada tam baz koduyla eşleşen aktif USDT perpetual kontrat gerekir; 1000x isimler veya başka borsanın verisi eşlenmez.

Güncel fonlama: 8 saate oransal ölçeklendiğinde en çok -%0.01. OI kontrat sayısı en az %5 artmış olmalı; önceki GERÇEK gözlem yaklaşık 4 saat önce (3–5 saat aralığı) olmalı. Fiyat aynı aralıkta %0–12 yükselmiş, vadeli makas en çok %0.5, OI büyüklüğü en az yaklaşık 1 milyon USD/USDT, spot-vadeli fiyat farkı en çok %2 olmalı. İlk çalışmada eski OI yoksa veri birikiyor; geriye sinyal yazılmaz.

OI değişimi fiyat etkisinden arındırılmış aynı kontrat sayılarıyla ölçülür; kontrat büyüklüğü değiştiyse eski baz kullanılmaz. MEXC OI parasal büyüklüğü güncel fiyatla tahmini USDT, OKX oiUsd sağlayıcı USD değeridir; eşdeğer nakit veya fiyat etkisinden arınmış büyüme değillerdir. Fonlama dönemleri ayrı gösterilir; 8 saat ölçeği gelecek ödeme tahmini değildir.

Negatif fonlama ve artan toplam OI, shortların çoğunlukta olduğunu veya fiyat yükseldiğinde kesin likidasyon olacağını kanıtlamaz. Likidasyon haritası, hesapların kaldıraçları ve bağımsız short-only OI verisi kullanılmaz. Bu bir araştırma filtresidir.

Aynı sembol küresel listede bir kez seçilir; farklı borsaların OI/hacimleri toplanmaz. Sembol eşleşmesi kontrat kimliğinin bağımsız doğrulaması değildir. Yeni girişler yalnız o andaki gerçek spot fiyatından 12/24/48 saat ölçülür; ücret, kayma ve vadeli fonlama dahil net getiri değildir.

## Bu deneyin ayrı gerçek gözlem ölçümleri

0 borsa kaydı / 0 farklı sembol. Aynı coin ayrı bağımsız başarı sayılmaz.

| Coin | Borsa | Teknik grup | Yeni deneyin ilk gerçek gözlemi TR | Spot referans | 12s % | 24s % | 48s % |
|---|---|---|---|---:|---:|---:|---:|

[MEXC kontrat verileri](https://www.mexc.com/api-docs/futures/market-endpoints/get-ticker-contract-market-data) · [MEXC fonlama](https://www.mexc.com/api-docs/futures/market-endpoints/get-funding-rate) · [OKX kamu verileri](https://www.okx.com/docs-v5/en/#public-data-rest-api-get-open-interest)

<!-- shortcu-kistir:v1 -->

<!-- shortcu-comparison:start -->

## Ücretsiz karşılaştırmalı deney — sessiz ölçüm

Aynı ilk uygun gözlemde en çok 50 farklı sembol. Şu an 18 kayıt. Bildirim eklenmez; mevcut Shortçu Kıstır kuralları ve eski fiyatlar korunur.

Aynı anda tüm faktörler biliniyorsa kayda alınır. Eksik OI geçmişi, fonlama veya fiyat bilinmiyor kalır; olumsuz koşula veya 0 puana dönüştürülmez. Aynı sembol iki borsada iki bağımsız örnek sayılmaz.

| Grup | Koşul | Kayıt | Ölçülen 12s | Medyan % | BTC üstü puan | Kontrol üstü puan | Girişe göre dip % | Girişe göre tepe % |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| A | Teknik temel + ortak vadeli işlem koşulları | 18 | 4 | -3.43 | -2.78 | -1.92 | -3.74 | +1.33 |
| B | A + negatif fonlama | 0 | 0 | — | — | — | — | — |
| C | A + OI artışı ve fiyat tutunması | 0 | 0 | — | — | — | — | — |
| D | A + fonlama + OI/fiyat birlikte | 0 | 0 | — | — | — | — | — |

**Henüz üstünlük/başarı iddiası yok.** Ana karşılaştırma 12 saat; 6/24/48 saat ikincildir. Gruplar örtüşür, grup sayıları toplanarak bağımsız başarı hesaplanmaz. A da aynı borsada geçerli perpetual/likidite/makas/fiyat farkı şartlarına tabidir; bütün spot piyasanın kontrol grubu değildir.

Aynı başlangıç fiyatındaki koşullu karşılaştırmadır; bir coin saatler sonra yeni bir şartı sağladığında geriye dönük grup değiştirilmez. Bu nedenle D, mevcut üretim sinyallerinin tümünün birebir kopyası değildir; ilk ortak uygun gözlemde birlikte sağlanan koşulları ölçer. Üretimin kendi gerçek sinyal ölçümleri yukarıda ayrıca sürer.

Her grupta en az 20 tamamlanmış gözlem olmadan ilk değerlendirme yapılmaz. İlk 25 / sonraki 25 kayıt ayrı tutulur; dönem arasında sonuçlara bakıp eşik değiştirilmez. Bunlar istatistiksel kesinlik veya bağımsız piyasa rejimleri anlamına gelmez.

Maliyet duyarlılığı (gerçek gerçekleşme/net kâr değildir): gidiş-dönüş %0.2 / %0.5 / %1 toplam maliyet varsayımı getiriden ayrı düşülür. Sabit maliyet senaryosu gerçek hesap komisyonu, kayma, vergi veya vadeli fonlamanın ölçüldüğü anlamına gelmez.

| Grup | Ölçülen | %0.2 maliyet sonrası pozitif | %0.5 sonrası | %1 sonrası |
|---|---:|---:|---:|---:|
| A | 4 | %0.0 | %0.0 | %0.0 |
| B | 0 | — | — | — |
| C | 0 | — | — | — |
| D | 0 | — | — | — |

Ölçüm: girişten sonraki ilk TAM 1dk mumdan hedefin ilk dakika kapanışına kadar. Giriş mumunun kalan <1 dakikası dip/tepe hesabına dahil edilmez; tam işlem aralığının mutlak tepe/dibi olduğu iddia edilmez. Eksik ara mum varsa dip/tepe bilinmiyor; eksik sonuçlar sıfır getiri sayılmaz.

## Deneyin gerçek gözlem kayıtları

| No | Coin | Borsa | Grup üyelikleri | Gerçek gözlem TR | Spot referans | Kaynak kapanışından gecikme dk |
|---:|---|---|---|---|---:|---:|
| 1 | SUIUSDT | MEXC | A | 28.10.2026 03:55 | 0.93185 | 55.2 |
| 2 | NIGHTUSDT | OKX | A | 28.10.2026 03:55 | 0.041944 | 55.2 |
| 3 | BCHUSDT | OKX | A | 28.10.2026 07:48 | 297.99 | 48.7 |
| 4 | AAVEUSDT | MEXC | A | 28.10.2026 07:48 | 135.305 | 48.7 |
| 5 | XRPUSDT | OKX | A | 28.10.2026 07:48 | 1.33025 | 48.7 |
| 6 | FILUSDT | OKX | A | 28.10.2026 07:48 | 0.91465 | 48.7 |
| 7 | ZECUSDT | OKX | A | 28.10.2026 07:48 | 1319.48 | 48.7 |
| 8 | ZAMAUSDT | MEXC | A | 28.10.2026 11:57 | 0.078535 | 57.6 |
| 9 | BNBUSDT | MEXC | A | 28.10.2026 15:56 | 755.41 | 56.2 |
| 10 | PONSUSDT | MEXC | A | 28.10.2026 15:56 | 0.2839625 | 56.2 |
| 11 | PROSUSDT | OKX | A | 28.10.2026 15:56 | 0.63045 | 56.2 |
| 12 | XPLUSDT | OKX | A | 28.10.2026 19:56 | 0.07642 | 56.5 |
| 13 | BICOUSDT | OKX | A | 28.10.2026 19:56 | 0.01588 | 56.5 |
| 14 | PENGUUSDT | OKX | A | 28.10.2026 23:46 | 0.0078725 | 46.8 |
| 15 | ARBUSDT | OKX | A | 28.10.2026 23:46 | 0.173985 | 46.8 |
| 16 | TIAUSDT | OKX | A | 28.10.2026 23:46 | 0.5568 | 46.8 |
| 17 | ICPUSDT | MEXC | A | 28.10.2026 23:46 | 2.6345 | 46.8 |
| 18 | PUMPUSDT | OKX | A | 28.10.2026 23:46 | 0.004466 | 46.8 |

Dış likidasyon haritası / büyük yatırımcı pozisyon oranı API bağlantısı yok; bu alanlar hesaplanmış veya doğrulanmış kabul edilmez. Ücretsiz deney mevcut kamu verisinin katkısını sınar. Dört saatlik teknik kaynak ve GitHub gecikmesi hızlı squeeze hareketlerini kaçırabilir; gecikme yukarıda kayıtlıdır.

Son kayıt elemesi: {"factor_unknown_or_common_failure": 8}
Fiyat kaynağı hataları: {}
Ölçüm erişim/veri hatası: 0.
