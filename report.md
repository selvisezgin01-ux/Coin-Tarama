# Shortçu Kıstır

Son çalışma: 27.10.2026 23:52 TR.

**Coin Tarama 3 teknik temelinden beslenen bağımsız deney. Short pozisyon açılmaz; yükseliş yönlü olası short sıkışması aranır. Başarı garantisi yoktur.**

Teknik işlem koşullarından geçen 15 borsa kaydı; squeeze koşullarını sağlayan en çok 5 farklı sembol; güncel liste 0.

Kaynak: Coin Tarama 3 tamamlandığında scanner-state-v5 dalından okunur. Kaynak adaylar, eski ölçümler ve beşli öncelik listesi değiştirilmez. Eski fiyatlar yeni sinyalin referansı değildir.

| Coin | Borsa | Gerçek spot gözlemi TR | Spot fiyat | Fonlama / dönem | OI değişimi | Gerçek aralık |
|---|---|---|---:|---|---:|---|

Şu an tüm koşulları doğrulanan aday yok. Veri birikimi/erişim eksikliği ile koşul sağlanmaması aşağıda ayrılır.

## Veri birikimi ve eleme nedenleri

- 13 borsa kaydı: yeterince negatif fonlama yok
- 1 borsa kaydı: fonlama verisi eksik/eski
- 1 borsa kaydı: aynı borsada eşleşen aktif USDT sürekli vadeli kontrat yok
- 5 borsa kaydı: açık pozisyon büyüklüğü yetersiz
- 14 borsa kaydı: uygun aralıkta önceki gerçek OI gözlemi birikiyor

Bir kayıtta birden çok neden olabilir. Şu anki fonlama ve OI, başarısız teknik filtreleri geçersiz kılmaz.

- OKX: 511 güncel vadeli OI kaydı; 5 fonlama incelemesi; 0 erişim/veri hatası.
- MEXC: 647 güncel vadeli OI kaydı; 8 fonlama incelemesi; 0 erişim/veri hatası.

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

Aynı ilk uygun gözlemde en çok 50 farklı sembol. Şu an 0 kayıt. Bildirim eklenmez; mevcut Shortçu Kıstır kuralları ve eski fiyatlar korunur.

Aynı anda tüm faktörler biliniyorsa kayda alınır. Eksik OI geçmişi, fonlama veya fiyat bilinmiyor kalır; olumsuz koşula veya 0 puana dönüştürülmez. Aynı sembol iki borsada iki bağımsız örnek sayılmaz.

| Grup | Koşul | Kayıt | Ölçülen 12s | Medyan % | BTC üstü puan | Kontrol üstü puan | Girişe göre dip % | Girişe göre tepe % |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| A | Teknik temel + ortak vadeli işlem koşulları | 0 | 0 | — | — | — | — | — |
| B | A + negatif fonlama | 0 | 0 | — | — | — | — | — |
| C | A + OI artışı ve fiyat tutunması | 0 | 0 | — | — | — | — | — |
| D | A + fonlama + OI/fiyat birlikte | 0 | 0 | — | — | — | — | — |

**Henüz üstünlük/başarı iddiası yok.** Ana karşılaştırma 12 saat; 6/24/48 saat ikincildir. Gruplar örtüşür, grup sayıları toplanarak bağımsız başarı hesaplanmaz. A da aynı borsada geçerli perpetual/likidite/makas/fiyat farkı şartlarına tabidir; bütün spot piyasanın kontrol grubu değildir.

Aynı başlangıç fiyatındaki koşullu karşılaştırmadır; bir coin saatler sonra yeni bir şartı sağladığında geriye dönük grup değiştirilmez. Bu nedenle D, mevcut üretim sinyallerinin tümünün birebir kopyası değildir; ilk ortak uygun gözlemde birlikte sağlanan koşulları ölçer. Üretimin kendi gerçek sinyal ölçümleri yukarıda ayrıca sürer.

Her grupta en az 20 tamamlanmış gözlem olmadan ilk değerlendirme yapılmaz. İlk 25 / sonraki 25 kayıt ayrı tutulur; dönem arasında sonuçlara bakıp eşik değiştirilmez. Bunlar istatistiksel kesinlik veya bağımsız piyasa rejimleri anlamına gelmez.

Maliyet duyarlılığı (gerçek gerçekleşme/net kâr değildir): gidiş-dönüş %0.2 / %0.5 / %1 toplam maliyet varsayımı getiriden ayrı düşülür. Sabit maliyet senaryosu gerçek hesap komisyonu, kayma, vergi veya vadeli fonlamanın ölçüldüğü anlamına gelmez.

| Grup | Ölçülen | %0.2 maliyet sonrası pozitif | %0.5 sonrası | %1 sonrası |
|---|---:|---:|---:|---:|
| A | 0 | — | — | — |
| B | 0 | — | — | — |
| C | 0 | — | — | — |
| D | 0 | — | — | — |

Ölçüm: girişten sonraki ilk TAM 1dk mumdan hedefin ilk dakika kapanışına kadar. Giriş mumunun kalan <1 dakikası dip/tepe hesabına dahil edilmez; tam işlem aralığının mutlak tepe/dibi olduğu iddia edilmez. Eksik ara mum varsa dip/tepe bilinmiyor; eksik sonuçlar sıfır getiri sayılmaz.

## Deneyin gerçek gözlem kayıtları

| No | Coin | Borsa | Grup üyelikleri | Gerçek gözlem TR | Spot referans | Kaynak kapanışından gecikme dk |
|---:|---|---|---|---|---:|---:|

Dış likidasyon haritası / büyük yatırımcı pozisyon oranı API bağlantısı yok; bu alanlar hesaplanmış veya doğrulanmış kabul edilmez. Ücretsiz deney mevcut kamu verisinin katkısını sınar. Dört saatlik teknik kaynak ve GitHub gecikmesi hızlı squeeze hareketlerini kaçırabilir; gecikme yukarıda kayıtlıdır.

Son kayıt elemesi: {"factor_unknown_or_common_failure": 15}
Fiyat kaynağı hataları: {}
Ölçüm erişim/veri hatası: 0.
