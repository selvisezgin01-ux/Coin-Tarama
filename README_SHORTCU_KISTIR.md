# Shortçu Kıstır

Kullanıcının 27 Ekim 2026 onayıyla bağımsız araştırma taraması. Coin Tarama 3'ün teknik temelini kullanır; Coin Tarama 2, 3, Meme veya yerel pilot dosyalarını/durumlarını değiştirmez. Hesap/emir, pozisyon açma, cüzdan veya özel API anahtarı kullanımı yoktur. Short pozisyon açmaz; olası short sıkışmasıyla yukarı hareket adayları araştırılır.

## Akış ve kapsam

`shortcu-kistir.yml`, Coin Tarama 3 tamamlandığında onun `scanner-state-v5/state.json` aday havuzunu salt okunur alır. Orijinal beşli listeye girmeyen ama aynı işlem koşulu elemesini geçen adaylar da değerlendirilir. Teknik tabanı geçmeyen vadeli coinler bu sürümün kapsamı dışındadır; bütün futures piyasası taraması değildir. Kaynak çalışma hatalı olsa bile iki borsanın mevcut/güncel sonuçları ayrı doğrulanır. Eski kaynak kapanışı güncel kabul edilmez.

Güncel spot fiyat/BTC/kontrol gözlemleri yenilenir; aynı borsadaki tam baz koduyla eşleşen aktif USDT perpetual kontratın genel verileri okunur. MEXC ve OKX fiyat/OI/hacimleri birleştirilmez; otomatik `1000TOKEN` dönüşümü yapılmaz. Tam baz kodu/spot-vadeli fiyat yakınlığı tek başına projenin kontrat kimliğini kanıtlamaz.

Deneysel başlangıç koşulları:

- Coin Tarama 3'ün mevcut işlem koşulu elemesi (100k USDT spot hacim, makas/uzama/yapı vb.); en fazla 5 farklı sembol.
- Güncel fonlama, 8 saate oransal ölçekle en çok -%0.01. Ham dönem ve oran birlikte gösterilir; gelecek 8 saatin gerçekleşmiş veya garanti ödemesi değildir.
- Aynı kontratın açık pozisyon sayısı, 3–5 saat önceki en yakın gerçek gözleme göre en az %5 artmış olmalı. Hedef aralık 4 saat; gerçek süre ayrıca gösterilir. Parasal OI artışı kullanılmaz, çünkü fiyat yükselmesi onu kendiliğinden artırabilir.
- Aynı aralıkta vadeli fiyat değişimi %0–12. Güncel vadeli makas <=%0.5; spot/vadeli fiyat farkı <=%2; OI büyüklüğü yaklaşık en az 1 milyon USD/USDT.
- Katalog/kontrat büyüklüğü veya veri zamanları uyuşmazsa bilinmiyor. İlk çalışmada 4 saatlik gözlem olmadığı için veri birikir. Geçmişe giriş/sinyal uydurulmaz.

Güncel OI gözlemleri uygun tüm vadeli kontratlar için saklanır; fonlama okumaları teknik olarak uygun ağ/borsa başına en çok 20 adayla sınırlıdır. Veri kaynağı 401/403/418/429 verirse o borsanın kamu istekleri durur, diğer borsa sürer. Ücretli/özel likidasyon haritası veya short-only OI sağlandığı iddia edilmez. Toplam OI artışı ve negatif fonlama short birikimi/likidasyon kanıtı değildir. Eşikler tarihsel performansa göre optimize edilmemiştir.

## Bağımsızlık, rapor ve bildirim

Kalıcı durum: `scanner-state-shortcu-kistir`. Güncel [rapor](https://github.com/selvisezgin01-ux/Coin-Tarama/blob/scanner-state-shortcu-kistir/report.md). Orijinal `scanner-state-v5` değiştirilmez. Yeni deneyin ilk gerçek spot fiyat/BTC/kontrol gözlemleri ayrı kaydedilir ve 12/24/48 saat ölçülür; eski Coin Tarama 3 fiyatları giriş olarak kullanılmaz. Aynı sembolün iki borsa kaydı iki bağımsız başarı değildir. İşlem maliyetleri ve vadeli fonlama dahil net kazanç hesaplanmaz.

Bildirim kanalı mevcut `NOTIFICATION_CHANNEL` ve `COIN_NOTIFY_USER` ayarlarını kullanır. GitHub Issue başlığı **Shortçu Kıstır** olur. Veri birikiyorsa veya doğrulanan aday yoksa sinyal Issue'su açılmaz. Kendi 48 saat tekrar beklemesi ve teslimat kaydı vardır. Repo/telefon bildirim tercihleri teslim ve sesi etkiler.

Bu tarama Coin Tarama 3'ün yaklaşık dört saatlik döngüsünden sonra çalışır; saniyelik squeeze radarına veya tam zamanında bildirime karşılık gelmez. Planlayıcı/API gecikmeleri vardır. Bağımsız workflow, ayrı rapor ve kayıtlar sağlar; teknik keşif kaynağı Coin Tarama 3'tür.

Kaynaklar: [MEXC kontrat alanları](https://www.mexc.com/api-docs/futures/market-endpoints/get-contract-info), [ticker/OI](https://www.mexc.com/api-docs/futures/market-endpoints/get-ticker-contract-market-data), [fonlama](https://www.mexc.com/api-docs/futures/market-endpoints/get-funding-rate), [OKX API](https://www.okx.com/docs-v5/en/#public-data-rest-api-get-open-interest).
