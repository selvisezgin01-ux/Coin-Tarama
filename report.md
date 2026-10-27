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
