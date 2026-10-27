# Coin Tarama 3 — kısa öncelik listesi

Son kontrol: 27.10.2026 19:53 TR.

Geniş havuz: 147 borsa kaydı / 126 sembol. İşlem koşulu elemesini geçen: 42 farklı sembol. Bildirim ve üst liste: en fazla 5 farklı coin.

**Öncelik, kârlılık veya güvenli işlem garantisi değildir.** Hacim/makas, güncel fiyat, yapı ve uzama kontrollerinden geçenler sıralanır. Yalnız yatay hacim hazırlığı bildirilmez. Aday yoksa liste doldurulmaz.

| Coin | Fiyat borsası | Geçen borsalar | Grup | Gerçek gözlem TR | Fiyat | Makas % | Yapı mesafesi % |
|---|---|---|---|---|---:|---:|---:|
| CFGUSDT | OKX | MEXC, OKX | Erken dönüş, Yeni kırılım | 27.10.2026 19:53 | 0.10832 | 0.09 | 8.19 |
| IOUSDT | MEXC | MEXC | Erken dönüş | 27.10.2026 19:53 | 0.15046 | 0.08 | 5.88 |
| PENGUUSDT | MEXC | MEXC, OKX | Erken dönüş | 27.10.2026 19:53 | 0.007689 | 0.13 | 3.92 |
| STETHUSDT | OKX | OKX | Erken dönüş | 27.10.2026 19:53 | 2344.565 | 0.07 | 1.69 |
| CELOUSDT | OKX | OKX | Erken dönüş, Yeni kırılım | 27.10.2026 19:53 | 0.08231 | 0.07 | 6.20 |

Sıralama: en çok 4x sayılan göreli hacim, kapanış konumu, dar makas ve aynı borsanın hacmi. Farklı borsaların hacimleri toplanmaz. Bu sıra başarı olasılığı değildir.

Başlangıç elemesi: en az 100.000 USDT kapalı 24s hacim, en çok %0,5 makas, izlenen seviyeyi koruyan güncel fiyat, kapanıştan en çok 1 ATR uzaklık, EMA20 üstüne en çok 2,5 ATR uzama ve yapı referansına en çok %12 mesafe. 20x üzeri hacim ayrıca incelemede kalır. Bunlar daha iyi sonuç verdiği kanıtlanmış yeni strateji eşikleri değildir.

Aynı sembol tek satırda gösterilir; yalnız elemeden geçen borsalar listelenir. Sembol eşleşmesi bağımsız kontrat kimliği teyidi değildir. Geniş havuz ve eski ölçümler korunur. [Tanınan OKX hisse tokenlerinin kaynağı](https://www.okx.com/help/okx-to-list-tokenized-stocks-for-trading). Liste 2026-10-26 tarihinde kontrol edildi; yeni hisse tokenlerinin eklenmesi gerekebilir.

## Eleme özeti

- 29 borsa kaydı: EMA20 uzaklığı fazla veya bilinmiyor
- 8 borsa kaydı: olağandışı hacim katsayısı; ayrıca inceleme
- 33 borsa kaydı: tanınan tokenleştirilmiş hisse
- 10 borsa kaydı: yalnız hazırlık; ek teknik teyit yok
- 4 borsa kaydı: güncel fiyat kapanıştan uzak veya veri eksik
- 5 borsa kaydı: yapı bozulma mesafesi geniş veya bilinmiyor
- 8 borsa kaydı: makas geniş veya bilinmiyor
- 11 borsa kaydı: izlenen seviye kaybedilmiş veya bilinmiyor
- 52 borsa kaydı: hacim 100.000 USDT altında

Bir kayıtta birden fazla neden olabilir; sayılar bağımsız coinler gibi toplanmaz.
Sıralama sınırı dışında kalan uygun sembol: 37.


## Öncelik listesinin ayrı gerçek gözlem ölçümleri

Referans, bu kısa listeye ilk girişte gerçekten okunan fiyat ve saattir; eski geniş listedeki daha erken fiyat kullanılmaz. 12/24/48s ölçümleri state.json içinde ayrı tutulur. Aynı sembolün iki borsa kaydı bağımsız iki coin sayılmaz.

<details>
<summary>Öncelik listesinin 12/24/48 saat sonuçlarını aç</summary>

| Coin | Borsa | İlk gerçek gözlem TR | Referans | 12s % | 24s % | 48s % |
|---|---|---|---:|---:|---:|---:|
| LUNAUSDT | OKX | 26.10.2026 16:56 | 0.04159 | 1.37 | 1.08 | — |
| METUSDT | OKX | 26.10.2026 16:56 | 0.31085 | 1.59 | 1.43 | — |
| CRVUSDT | OKX | 26.10.2026 16:56 | 0.3495 | -3.52 | -4.89 | — |
| NIGHTUSDT | MEXC | 26.10.2026 16:56 | 0.03791 | 4.91 | 4.48 | — |
| ONDOUSDT | MEXC | 26.10.2026 16:56 | 0.41274 | -0.50 | -0.48 | — |
| ARBUSDT | MEXC | 26.10.2026 17:50 | 0.171355 | -2.17 | -1.96 | — |
| CELOUSDT | OKX | 26.10.2026 19:50 | 0.079105 | -0.89 | 3.91 | — |
| POLUSDT | OKX | 26.10.2026 19:50 | 0.091045 | -1.40 | 0.12 | — |
| ONDOUSDT | OKX | 26.10.2026 19:50 | 0.41515 | -1.96 | -0.08 | — |
| WLFIUSDT | OKX | 26.10.2026 19:50 | 0.053445 | -1.71 | -2.01 | — |
| MOVRUSDT | MEXC | 26.10.2026 19:50 | 1.0922 | 0.37 | 3.16 | — |
| COMPUSDT | MEXC | 26.10.2026 23:37 | 21.79 | -1.42 | — | — |
| ARXUSDT | MEXC | 26.10.2026 23:37 | 0.2252 | 0.84 | — | — |
| XKORUUSDT | OKX | 27.10.2026 03:44 | 11.475 | 0.83 | — | — |
| QNTUSDT | MEXC | 27.10.2026 03:44 | 203.095 | -0.44 | — | — |
| CLANKERUSDT | MEXC | 27.10.2026 03:44 | 13.645 | -0.77 | — | — |
| TELUSDT | MEXC | 27.10.2026 03:44 | 0.0015175 | 3.00 | — | — |
| IOSTUSDT | OKX | 27.10.2026 07:38 | 0.0008208 | -4.25 | — | — |
| ZBCNUSDT | OKX | 27.10.2026 07:38 | 0.00222315 | -2.38 | — | — |
| XSOXSUSDT | OKX | 27.10.2026 11:46 | 48.635 | — | — | — |
| ZORAUSDT | OKX | 27.10.2026 11:46 | 0.006395 | — | — | — |
| DASHUSDT | OKX | 27.10.2026 11:46 | 54.99 | — | — | — |
| TRUTHUSDT | MEXC | 27.10.2026 11:46 | 0.0210175 | — | — | — |
| AVAUSDT | MEXC | 27.10.2026 11:46 | 0.36365 | — | — | — |
| LSKUSDT | OKX | 27.10.2026 15:48 | 0.169625 | — | — | — |
| CASHCATUSDT | MEXC | 27.10.2026 15:48 | 0.09844 | — | — | — |
| XDCUSDT | MEXC | 27.10.2026 15:48 | 0.03539 | — | — | — |
| VVVUSDT | MEXC | 27.10.2026 15:48 | 25.6305 | — | — | — |
| CFGUSDT | OKX | 27.10.2026 19:53 | 0.10832 | — | — | — |
| STETHUSDT | OKX | 27.10.2026 19:53 | 2344.565 | — | — | — |
| IOUSDT | MEXC | 27.10.2026 19:53 | 0.15046 | — | — | — |
| PENGUUSDT | MEXC | 27.10.2026 19:53 | 0.007689 | — | — | — |

</details>

<details>
<summary>Geniş tarama, hazırlık adayları ve önceki tüm ölçümler</summary>

<!-- coin-priority-raw:start -->
# Coin Tarama 3 — erken dönüş / hacim / geri test

**Deneysel canlı tarama; başarı üstünlüğü doğrulanmadı.**

V3 otomasyonu ve bildirimleri ayrı çalışır. Yeni adaylar Coin Tarama 3 başlığıyla bildirilir; yerel 50 coinlik pilot kayıtları ayrıdır. Puan başarı olasılığı değildir.

Üç ek grup birbirinin alternatifi: erken dönüş, yatay fiyat/hacim artışı, geri testte tutunma/SAR. Önceki yeni kırılım ve tutunma yolları da korunur. Bir token birden çok gruba uyabilir; bağımsız başarı gibi toplanmaz.

246 coinlik geçmiş kontrolünde bilinen tasarım örnekleri hariç yeni birleşim 1423, eski V4 724 olay üretti. Ölçülen 12s kapanış medyanı sırasıyla -%0,33 ve -%0,50; yeni birleşimin kontrol üstü medyan farkı -0,29 puan. Bu, kazanç veya üstünlük kanıtı değildir. Eski arşiv, canlı ön eleme ve işlem maliyetlerini tam temsil etmez.

Erken dönüşte önceki mum EMA20 altındayken üç mumluk yakın tepenin hacimle geri alınması aranır; yükselen EMA20 veya eski 20 mum tepesini aşması zorunlu değildir. Yatay hacim yükseliş onayı veya kesin toplama değildir. Geri testte sabit kırılım seviyesi, gerçek dönüş, dar taban, azalan hacim ve SAR alt konumu aranır.

MEXC: incelenen 1045, aday 60; kapanış 27.10.2026 19:00 TR; fiyat gözlemi 27.10.2026 19:50 TR.
V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |
|---|---|---:|---:|---|---|
| TRIAUSDT | Tutunma | 6.38 | 5.56 | Yok | düşük hacim |
| ADXUSDT | Erken dönüş | 0.75 | 59.51 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| DYDXUSDT | Erken dönüş | 0.06 | 2.56 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| GRVTUSDT | Erken dönüş, Yeni kırılım | 28.10 | 12.78 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı kapanıştan uzaklaştı |
| MARSCOINUSDT | Erken dönüş | 3.36 | 2.93 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| QUBICUSDT | Erken dönüş | 12.75 | 9.75 | RSI PU teyitli | yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| STABLEUSDT | Erken dönüş | 5.23 | 2.60 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| TLMUSDT | Erken dönüş | 2.73 | 5.34 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| GRASSUSDT | Erken dönüş | -0.71 | 2.15 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| QRLUSDT | Erken dönüş | 2.84 | 11.10 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| BTWUSDT | Erken dönüş | 28.98 | 1.65 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| DOGEUSDT | Erken dönüş | 0.51 | 1.57 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ENAUSDT | Erken dönüş | 1.10 | 1.80 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ROBOUSDT | Erken dönüş | 5.96 | 1.96 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| SYLUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 0.39 | 1.68 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; gözlem fiyatı grubun izlediği seviyenin altında |
| CFGUSDT | Erken dönüş | 7.79 | 2.41 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| FETUSDT | Erken dönüş | 2.38 | 3.77 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| INJUSDT | Erken dönüş, Yeni kırılım | 3.35 | 2.35 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| IOUSDT | Erken dönüş | 4.44 | 4.48 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| MOVRUSDT | Erken dönüş | 3.55 | 2.36 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| PENGUUSDT | Erken dönüş | 0.83 | 4.39 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XPLUSDT | Erken dönüş | -0.69 | 2.91 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| MEGAUSDT | Erken dönüş | 1.91 | 1.51 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| COCOUSDT | Erken dönüş | 0.35 | 3.07 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ETHUSDT | Erken dönüş | 0.80 | 3.72 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| LDOUSDT | Erken dönüş | 0.08 | 3.06 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| LNQUSDT | Erken dönüş | 1.22 | 3.89 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| OGYUSDT | Erken dönüş | 0.17 | 3.32 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| 4USDT | Erken dönüş | 2.85 | 1.97 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| AEROUSDT | Erken dönüş | 3.21 | 1.90 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| APEXUSDT | Erken dönüş | 1.84 | 1.67 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ARKMUSDT | Erken dönüş | 0.86 | 1.51 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| AZTECUSDT | Erken dönüş, Yeni kırılım | 8.31 | 1.51 | RSI PU teyitli | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| DYMUSDT | Erken dönüş | -0.22 | 1.53 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| GMXUSDT | Erken dönüş | 3.66 | 1.83 | RSI PU teyitli | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| MYXUSDT | Erken dönüş | 1.33 | 1.66 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| RIFUSDT | Erken dönüş | 2.03 | 1.60 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| OMIUSDT | Erken dönüş | 2.19 | 1.67 | RSI PU teyitli | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ZROUSDT | Erken dönüş | -1.10 | 1.58 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| AINUSDT | Yeni kırılım | 232.39 | 42.24 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| BANKUSDT | Yeni kırılım | 10.50 | 15.47 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| BCHUSDT | Yeni kırılım | 3.38 | 2.10 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| BXEUSDT | Yeni kırılım | 8.94 | 15.08 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| HANAUSDT | Yeni kırılım | 15.00 | 2.74 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş |
| ACUUSDT | Yeni kırılım | 17.14 | 1.82 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| INXUSDT | Yeni kırılım | 9.75 | 1.84 | Yok | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş; gözlem fiyatı grubun izlediği seviyenin altında |
| STAMPUSDT | Yeni kırılım | 81.85 | 4.13 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; makas geniş |
| ZECUSDT | Yeni kırılım | 3.62 | 1.51 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| LABUSDT | Yeni kırılım | 7.14 | 2.24 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı kapanıştan uzaklaştı |
| LUCKYUSDT | Yeni kırılım | 3.94 | 10.11 | Yok | ortalamadan uzak; düşük hacim |
| STOPUSDT | Yeni kırılım | 7.54 | 3.30 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş |
| TELUSDT | Yeni kırılım | 12.01 | 2.31 | RSI PU teyitli | Ek eşik uyarısı yok |
| WUSDT | Yeni kırılım | 7.84 | 3.79 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| ELSAUSDT | Yatay fiyat / hacim artışı | 14.67 | 2.27 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| CHIPUSDT | Yatay fiyat / hacim artışı | 4.72 | 2.06 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| MINIMAUSDT | Yatay fiyat / hacim artışı | 3.90 | 2.07 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| BDXUSDT | Yatay fiyat / hacim artışı | 0.40 | 2.07 | RSI PU teyitli | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| SHMUSDT | Yatay fiyat / hacim artışı | 0.26 | 1.73 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| VVVUSDT | Yatay fiyat / hacim artışı | 1.79 | 1.69 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| LYNUSDT | Yatay fiyat / hacim artışı | 3.68 | 1.62 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |

OKX: incelenen 338, aday 87; kapanış 27.10.2026 19:00 TR; fiyat gözlemi 27.10.2026 19:47 TR.
V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |
|---|---|---:|---:|---|---|
| ATHUSDT | Erken dönüş | 1.91 | 2.65 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| BICOUSDT | Erken dönüş | 2.25 | 2.30 | RSI PU teyitli | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| DYDXUSDT | Erken dönüş | 0.10 | 2.51 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ENAUSDT | Erken dönüş | 1.05 | 3.10 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| GRVTUSDT | Erken dönüş, Yeni kırılım | 28.05 | 15.89 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı kapanıştan uzaklaştı |
| MEGAUSDT | Erken dönüş | 1.89 | 2.00 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| PEOPLEUSDT | Erken dönüş | 1.48 | 2.05 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ROBOUSDT | Erken dönüş | 6.01 | 8.80 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XAAPLUSDT | Erken dönüş | 0.61 | 7.85 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XHOODUSDT | Erken dönüş | 3.17 | 6.56 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XUSARUSDT | Erken dönüş, Yeni kırılım | 9.01 | 222.12 | Yok | ortalamadan uzak; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ZENUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 0.87 | 2.25 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| GRASSUSDT | Erken dönüş | -0.44 | 2.81 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| OMIUSDT | Erken dönüş | 2.46 | 3.23 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| AEVOUSDT | Erken dönüş | 0.27 | 11.10 | RSI PU teyitli | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| BANDUSDT | Erken dönüş | 1.96 | 1.98 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| DOGEUSDT | Erken dönüş | 0.51 | 1.66 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| PEPEUSDT | Erken dönüş | 0.85 | 1.70 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| API3USDT | Erken dönüş | 3.13 | 2.51 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ARKMUSDT | Erken dönüş | 0.75 | 2.16 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| BETHUSDT | Erken dönüş | 0.81 | 2.51 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| CELOUSDT | Erken dönüş, Yeni kırılım | 2.92 | 5.19 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| CFGUSDT | Erken dönüş, Yeni kırılım | 8.04 | 4.79 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ETHUSDT | Erken dönüş | 0.79 | 2.47 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| FETUSDT | Erken dönüş | 2.26 | 3.41 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| FLOWUSDT | Erken dönüş | 0.04 | 3.75 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| GRTUSDT | Erken dönüş | 0.36 | 2.74 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| INJUSDT | Erken dönüş, Yeni kırılım | 3.29 | 2.28 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| KAIAUSDT | Erken dönüş | 1.98 | 2.54 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| KITEUSDT | Erken dönüş | 4.17 | 5.12 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| PAXGUSDT | Erken dönüş | 0.98 | 3.61 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| STETHUSDT | Erken dönüş | 0.46 | 4.06 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| VELODROMEUSDT | Erken dönüş | 2.16 | 2.46 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XCBRSUSDT | Erken dönüş | 1.94 | 5.07 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı kapanıştan uzaklaştı |
| XHIMSUSDT | Erken dönüş | 1.96 | 5.34 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XPLUSDT | Erken dönüş | -0.67 | 3.00 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| BRL1USDT | Erken dönüş | 1.79 | 2.86 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| LDOUSDT | Erken dönüş | 0.16 | 3.11 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| PENDLEUSDT | Erken dönüş | 0.20 | 3.27 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| RONUSDT | Erken dönüş | -0.33 | 4.34 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ENJUSDT | Erken dönüş | 1.19 | 1.99 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| MMTUSDT | Erken dönüş | 1.22 | 1.70 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| OLUSDT | Erken dönüş | 1.19 | 1.62 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| PENGUUSDT | Erken dönüş | 0.61 | 1.81 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| PROVEUSDT | Erken dönüş | 0.48 | 1.98 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| SSVUSDT | Erken dönüş | 0.46 | 1.76 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| JUPUSDT | Erken dönüş | -0.99 | 1.54 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| SUIUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 0.37 | 1.92 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| BCHUSDT | Yeni kırılım | 3.34 | 2.54 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XDRAMUSDT | Yeni kırılım | 4.41 | 2.78 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| ZECUSDT | Yeni kırılım | 3.59 | 3.07 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| WUSDT | Yeni kırılım | 7.69 | 5.58 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| XEWYUSDT | Yeni kırılım | 3.42 | 2.86 | RSI PU teyitli | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| XKORUUSDT | Yeni kırılım | 10.08 | 2.01 | RSI PU teyitli | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| XNBISUSDT | Yeni kırılım | 3.34 | 6.09 | RSI PU teyitli | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XORCLUSDT | Yeni kırılım | 2.91 | 9.34 | RSI PU teyitli | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XRKLBUSDT | Yeni kırılım | 6.55 | 24.16 | RSI PU teyitli | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XSHAZUSDT | Yeni kırılım | 6.43 | 12.21 | RSI PU teyitli | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XSNDKUSDT | Yeni kırılım | 3.56 | 5.16 | RSI PU teyitli | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XSNXXUSDT | Yeni kırılım | 6.76 | 2.18 | RSI PU teyitli | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XTSLAUSDT | Yeni kırılım | 3.35 | 10.94 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XTSMUSDT | Yeni kırılım | 2.61 | 5.23 | RSI PU teyitli | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XWDCUSDT | Yeni kırılım | 8.97 | 11.39 | RSI PU teyitli | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| ZAMAUSDT | Yeni kırılım | 4.37 | 26.49 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XAAOIUSDT | Yeni kırılım | 6.24 | 17.18 | RSI PU teyitli | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XALABUSDT | Yeni kırılım | 5.58 | 29.04 | RSI PU teyitli | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XAMDUSDT | Yeni kırılım | 5.99 | 2.14 | RSI PU teyitli | ortalamadan uzak |
| XAPLDUSDT | Yeni kırılım | 4.25 | 4.05 | RSI PU teyitli | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XASTSUSDT | Yeni kırılım | 4.88 | 22.14 | RSI PU teyitli | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XBEUSDT | Yeni kırılım | 6.36 | 3.80 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XCRWVUSDT | Yeni kırılım | 3.09 | 3.20 | Yok | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XDELLUSDT | Yeni kırılım | 6.94 | 9.89 | RSI PU teyitli | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XGEVUSDT | Yeni kırılım | 3.21 | 18.68 | Yok | ortalamadan uzak; düşük hacim |
| XINTCUSDT | Yeni kırılım | 3.22 | 5.41 | RSI PU teyitli | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XIRENUSDT | Yeni kırılım | 2.61 | 11.69 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XLITEUSDT | Yeni kırılım | 7.61 | 8.94 | RSI PU teyitli | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XMVLLUSDT | Yeni kırılım | 6.81 | 16.44 | RSI PU teyitli | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XSMCIUSDT | Yeni kırılım | 5.91 | 6.65 | RSI PU teyitli | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XSMHUSDT | Yeni kırılım | 2.21 | 25.87 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XSOXLUSDT | Yeni kırılım | 9.72 | 8.56 | RSI PU teyitli | ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XTQQQUSDT | Yeni kırılım | 3.74 | 7.27 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XVRTUSDT | Yeni kırılım | 4.60 | 7.48 | RSI PU teyitli | ortalamadan uzak; düşük hacim |
| XMRVLUSDT | Yeni kırılım | 3.75 | 1.91 | RSI PU teyitli | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XSKHYUSDT | Yatay fiyat / hacim artışı, Tutunma | 3.66 | 2.48 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| CHIPUSDT | Yatay fiyat / hacim artışı | 4.75 | 2.41 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| VVVUSDT | Yatay fiyat / hacim artışı | 2.02 | 1.52 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| PONSUSDT | Yatay fiyat / hacim artışı | 0.93 | 1.84 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |

İki borsada toplam 126 farklı sembol. Ortak semboller bağımsız iki başarı sayılmaz.

Eşikler başlangıç deneyidir; daha çok aday daha yüksek başarı demek değildir. Yazılım testleri kârlılık kanıtı değildir. Dört saatlik mum ve zamanlayıcı gecikmesi ilk hareketin kaçmasına yol açabilir. SAR yön desteğidir; getiri garantisi değildir.

## Bu döngüde yeni gelenler

ATHUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.0057595
24s %1.91; ilgili hacim 2.6499x; makas %0.16
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

MEGAUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.048015
24s %1.89; ilgili hacim 2.0004x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ROBOUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.005801
24s %6.01; ilgili hacim 8.8045x; makas %0.14
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XAAPLUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 346.45
24s %0.61; ilgili hacim 7.8545x; makas %0.02
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XHOODUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 96.365
24s %3.17; ilgili hacim 6.5634x; makas %0.03
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

GRASSUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.7
24s %-0.44; ilgili hacim 2.8103x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

OMIUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.00027155
24s %2.46; ilgili hacim 3.2297x; makas %0.11
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

AEVOUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.021825
24s %0.27; ilgili hacim 11.103x; makas %0.14
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; teyitli RSI pozitif uyumsuzluk desteği

PEPEUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 4.445e-06
24s %0.85; ilgili hacim 1.7025x; makas %0.01
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

API3USDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.25905
24s %3.13; ilgili hacim 2.5054x; makas %0.12
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

CFGUSDT · OKX
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 27.10.2026 19:47 TR; fiyat 0.10834
24s %8.04; ilgili hacim 4.789x; makas %0.10
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ETHUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 2347.7
24s %0.79; ilgili hacim 2.4735x; makas %0.00
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

FLOWUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.026355
24s %0.04; ilgili hacim 3.7535x; makas %0.19
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

GRTUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.022495
24s %0.36; ilgili hacim 2.7434x; makas %0.13
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

KAIAUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.035265
24s %1.98; ilgili hacim 2.5425x; makas %0.14
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

KITEUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.11818
24s %4.17; ilgili hacim 5.1243x; makas %0.12
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

PAXGUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 4066.2
24s %0.98; ilgili hacim 3.6147x; makas %0.00
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XCBRSUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 117.69
24s %1.94; ilgili hacim 5.0683x; makas %0.10
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı kapanıştan uzaklaştı

BRL1USDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.1871
24s %1.79; ilgili hacim 2.8589x; makas %0.21
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

RONUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.054205
24s %-0.33; ilgili hacim 4.3376x; makas %0.24
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ENJUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.025465
24s %1.19; ilgili hacim 1.9877x; makas %0.20
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

MMTUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.14255
24s %1.22; ilgili hacim 1.7034x; makas %0.21
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

OLUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.0059965
24s %1.19; ilgili hacim 1.6224x; makas %0.35
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

PENGUUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.007687
24s %0.61; ilgili hacim 1.8085x; makas %0.05
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

PROVEUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 0.1902
24s %0.48; ilgili hacim 1.9829x; makas %0.32
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

SSVUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:47 TR; fiyat 2.441
24s %0.46; ilgili hacim 1.7643x; makas %0.16
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

BCHUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 19:47 TR; fiyat 290.69
24s %3.34; ilgili hacim 2.5395x; makas %0.03
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

XSNXXUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 19:47 TR; fiyat 9.0805
24s %6.76; ilgili hacim 2.1814x; makas %0.21
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; teyitli RSI pozitif uyumsuzluk desteği

XTSMUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 19:47 TR; fiyat 437.38
24s %2.61; ilgili hacim 5.2268x; makas %0.03
ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; teyitli RSI pozitif uyumsuzluk desteği

XWDCUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 19:47 TR; fiyat 383.1
24s %8.97; ilgili hacim 11.393x; makas %0.08
ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; teyitli RSI pozitif uyumsuzluk desteği

ZAMAUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 19:47 TR; fiyat 0.076345
24s %4.37; ilgili hacim 26.493x; makas %0.09
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

XALABUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 19:47 TR; fiyat 282.74
24s %5.58; ilgili hacim 29.043x; makas %0.24
ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; teyitli RSI pozitif uyumsuzluk desteği

XASTSUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 19:47 TR; fiyat 43.055
24s %4.88; ilgili hacim 22.142x; makas %0.26
ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; teyitli RSI pozitif uyumsuzluk desteği

XBEUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 19:47 TR; fiyat 220.66
24s %6.36; ilgili hacim 3.7996x; makas %0.12
ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

XMVLLUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 19:47 TR; fiyat 28.665
24s %6.81; ilgili hacim 16.443x; makas %0.24
düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; teyitli RSI pozitif uyumsuzluk desteği

ADXUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.05405
24s %0.75; ilgili hacim 59.507x; makas %0.19
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

DYDXUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.1085
24s %0.06; ilgili hacim 2.5601x; makas %0.05
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

GRVTUSDT · MEXC
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 27.10.2026 19:50 TR; fiyat 0.22995
24s %28.10; ilgili hacim 12.779x; makas %0.22
ortalamadan uzak; yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı kapanıştan uzaklaştı

MARSCOINUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.068555
24s %3.36; ilgili hacim 2.9338x; makas %0.19
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

QUBICUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 4.269e-07
24s %12.75; ilgili hacim 9.7474x; makas %0.19
yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

STABLEUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.027418
24s %5.23; ilgili hacim 2.6016x; makas %0.11
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

TLMUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.0012034
24s %2.73; ilgili hacim 5.3376x; makas %0.13
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

GRASSUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.7087
24s %-0.71; ilgili hacim 2.1502x; makas %0.20
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

QRLUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 1.2527
24s %2.84; ilgili hacim 11.101x; makas %0.36
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ROBOUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.005796
24s %5.96; ilgili hacim 1.9611x; makas %0.24
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

SYLUSDT · MEXC
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 27.10.2026 19:50 TR; fiyat 5.655e-05
24s %0.39; ilgili hacim 1.6839x; makas %0.88
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; gözlem fiyatı grubun izlediği seviyenin altında

CFGUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.1081
24s %7.79; ilgili hacim 2.4092x; makas %0.19
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

FETUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.18
24s %2.38; ilgili hacim 3.7677x; makas %0.11
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

IOUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.15039
24s %4.44; ilgili hacim 4.4844x; makas %0.15
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

MEGAUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.04792
24s %1.91; ilgili hacim 1.506x; makas %0.04
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

COCOUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.15527
24s %0.35; ilgili hacim 3.0691x; makas %0.09
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ETHUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 2344.9
24s %0.80; ilgili hacim 3.7179x; makas %0.00
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

LDOUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.37505
24s %0.08; ilgili hacim 3.0641x; makas %0.03
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

LNQUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.0092495
24s %1.22; ilgili hacim 3.8885x; makas %0.88
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

OGYUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.0012607
24s %0.17; ilgili hacim 3.3197x; makas %0.71
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

ARKMUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.11935
24s %0.86; ilgili hacim 1.5142x; makas %0.12
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

AZTECUSDT · MEXC
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 27.10.2026 19:50 TR; fiyat 0.01779
24s %8.31; ilgili hacim 1.5139x; makas %0.34
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

DYMUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.01788
24s %-0.22; ilgili hacim 1.5323x; makas %0.11
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

GMXUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 8.4655
24s %3.66; ilgili hacim 1.8266x; makas %0.18
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

MYXUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.06142
24s %1.33; ilgili hacim 1.6598x; makas %0.23
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

RIFUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.070155
24s %2.03; ilgili hacim 1.5966x; makas %0.19
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

OMIUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 0.0002718
24s %2.19; ilgili hacim 1.6718x; makas %0.07
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

ZROUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 19:50 TR; fiyat 1.6772
24s %-1.10; ilgili hacim 1.5844x; makas %0.16
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

BXEUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 27.10.2026 19:50 TR; fiyat 0.0016745
24s %8.94; ilgili hacim 15.081x; makas %0.06
ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı

HANAUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 27.10.2026 19:50 TR; fiyat 0.014226
24s %15.00; ilgili hacim 2.7364x; makas %0.53
ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş

ACUUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 27.10.2026 19:50 TR; fiyat 0.13159
24s %17.14; ilgili hacim 1.8161x; makas %0.10
ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

INXUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 27.10.2026 19:50 TR; fiyat 0.0048755
24s %9.75; ilgili hacim 1.8435x; makas %1.05
düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş; gözlem fiyatı grubun izlediği seviyenin altında

LABUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 27.10.2026 19:50 TR; fiyat 0.044255
24s %7.14; ilgili hacim 2.2416x; makas %0.25
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı kapanıştan uzaklaştı

STOPUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 27.10.2026 19:50 TR; fiyat 0.001795
24s %7.54; ilgili hacim 3.2978x; makas %0.56
ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş

WUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 27.10.2026 19:50 TR; fiyat 0.012784
24s %7.84; ilgili hacim 3.7896x; makas %0.19
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında

ELSAUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 27.10.2026 19:50 TR; fiyat 0.082515
24s %14.67; ilgili hacim 2.2681x; makas %0.16
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

MINIMAUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 27.10.2026 19:50 TR; fiyat 0.003365
24s %3.90; ilgili hacim 2.0707x; makas %0.30
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

BDXUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 27.10.2026 19:50 TR; fiyat 0.07534
24s %0.40; ilgili hacim 2.0694x; makas %0.29
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

## V5 gerçek gözlemden sonraki sonuçlar

Her borsa/token için ilk gerçek fiyat bir ana kayıttır. Gruplar örtüşebilir; grup sayıları bağımsız başarı gibi toplanmaz. Bir gruba sonradan ilk giriş, o andaki gerçek fiyatla ayrıca ölçülür. Getiriler ücret/kayma dahil değildir; eksik ölçüm boş kalır.

| Coin | Borsa | İlk grup | Gerçek gözlem TR | Fiyat | 12s % | 24s % | 48s % |
|---|---|---|---|---:|---:|---:|---:|
| GALFTUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.8066 | -2.05 | -1.69 | — |
| XQCOMUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 177.525 | 1.92 | 1.97 | — |
| XGOOGLUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 322.39 | -0.93 | -1.00 | — |
| ARBUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.170775 | -0.80 | -0.84 | — |
| ASTRUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.0064895 | -0.35 | -4.66 | — |
| LUNAUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.041805 | 0.75 | -0.06 | — |
| METUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.31295 | 2.06 | 2.67 | — |
| XLITEUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 780.53 | 6.78 | 7.91 | — |
| SPKUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.01838 | 3.37 | 0.22 | — |
| XLRCXUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 234.725 | 2.10 | 3.08 | — |
| CRVUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.35035 | -2.64 | -4.24 | — |
| XASMLUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 1596.95 | 0.26 | 1.49 | — |
| IMXUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.1405 | -1.07 | -2.14 | — |
| CHIPUSDT | OKX | Yeni kırılım | 26.10.2026 15:39 | 0.049285 | 5.04 | 9.12 | — |
| PYTHUSDT | OKX | Yeni kırılım | 26.10.2026 15:39 | 0.075005 | -0.33 | -2.55 | — |
| DOODUSDT | OKX | Yeni kırılım | 26.10.2026 15:39 | 0.0023005 | -18.63 | -11.98 | — |
| DYDXUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 15:39 | 0.108095 | -0.95 | -1.39 | — |
| LDOUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 15:39 | 0.36995 | 0.50 | -0.26 | — |
| BICOUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 15:39 | 0.014945 | 0.30 | 1.10 | — |
| ILVUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 15:39 | 3.099 | -0.94 | -1.74 | — |
| SPCMUSDT | MEXC | Tutunma | 26.10.2026 15:43 | 0.0008465 | -3.79 | -5.32 | — |
| TAUSDT | MEXC | Tutunma | 26.10.2026 15:43 | 0.05873 | 5.93 | 6.76 | — |
| UMXUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.049465 | -13.70 | -3.00 | — |
| CAKEUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 2.1035 | 1.88 | -2.16 | — |
| ARBUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.170855 | -0.96 | -1.00 | — |
| BANKUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.02771 | -7.07 | 3.39 | — |
| NIGHTUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.038025 | 4.59 | 5.46 | — |
| NOMUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.001673 | -0.90 | 0.66 | — |
| SOONUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.3149 | -2.10 | -3.62 | — |
| UPCUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.12305 | 1.26 | -2.48 | — |
| GHXUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.009755 | -1.09 | -3.79 | — |
| TAGUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.0005201 | 32.38 | 58.47 | — |
| HYPEUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 77.435 | 1.67 | 1.72 | — |
| METUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.31225 | 2.32 | 2.80 | — |
| ONDOUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.413185 | 0.04 | -0.21 | — |
| SAGAUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.01787 | 0.78 | 2.07 | — |
| 4USDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.01169 | -0.51 | 1.03 | — |
| NATIXUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.000163895 | 21.65 | 7.91 | — |
| RUNEUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.6316 | -0.63 | -1.11 | — |
| MIUUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 9.35e-10 | -0.53 | -1.60 | — |
| BULLAUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 0.139074 | 10.56 | -52.90 | — |
| NEXUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 8.0765e-07 | -5.63 | -9.03 | — |
| PLAYUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 0.017415 | -5.54 | -8.41 | — |
| QNTUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 220.56 | -7.76 | -8.35 | — |
| CHIPUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 0.048875 | 5.90 | 10.06 | — |
| PYTHUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 0.075095 | -0.63 | -2.55 | — |
| DGMAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.01041 | -9.70 | -9.70 | — |
| PENGUUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.007525 | 0.20 | 0.31 | — |
| SHMUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 3.845e-05 | 0.13 | -0.13 | — |
| HMNDUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.0026355 | -4.72 | -4.57 | — |
| LYNUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.01345 | 3.87 | 4.76 | — |
| XLMUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.16945 | 0.09 | -0.44 | — |
| TRXUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.3313 | -0.54 | -0.85 | — |
| MONUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.021545 | 1.23 | 0.86 | — |
| DOGSUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 3.596e-05 | -0.89 | -2.34 | — |
| PARTIUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.037785 | 1.39 | -0.60 | — |
| CELOUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.079025 | -0.99 | 3.87 | — |
| DGBUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.00341 | -3.81 | -2.93 | — |
| DOGEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.077275 | 0.07 | 1.17 | — |
| ETCUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 7.564 | -0.49 | 0.42 | — |
| SUSHIUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.2016 | -0.94 | 2.38 | — |
| AXSUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.94855 | -0.73 | 0.66 | — |
| RESOLVUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.01674 | 0.00 | 0.00 | — |
| SNXUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.19645 | -0.74 | 1.40 | — |
| TRUMPUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 1.6845 | -0.68 | 0.56 | — |
| AAVEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 135.3 | -2.31 | -1.95 | — |
| ACEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.139285 | 2.16 | 2.65 | — |
| AVAXUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 8.911 | -1.98 | -0.68 | — |
| FETUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.17425 | -1.52 | 3.70 | — |
| JITOSOLUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 132.105 | -0.89 | -0.02 | — |
| JTOUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.43385 | -1.33 | 0.20 | — |
| LINKUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 11.442 | -0.94 | 0.39 | — |
| MANAUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.078525 | -1.38 | -0.52 | — |
| MORPHOUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 2.06625 | 3.67 | 4.85 | — |
| NEIROUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 6.6295e-05 | -0.44 | 2.18 | — |
| NIGHTUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.0396665 | -1.16 | -0.55 | — |
| ONDOUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.41435 | -1.82 | 0.37 | — |
| POLUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.090985 | -1.30 | 0.32 | — |
| PONSUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.244 | -2.50 | 5.49 | — |
| PUMPUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.0042435 | -2.32 | 1.10 | — |
| RENDERUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 1.7285 | -2.63 | -2.40 | — |
| WLFIUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.053395 | -1.62 | -1.92 | — |
| XAPLDUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 18.425 | -1.93 | 6.27 | — |
| XCRWVUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 56.425 | -1.28 | 4.69 | — |
| XIRENUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 26.1 | -1.95 | 3.75 | — |
| XSHAZUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 24.15 | -2.77 | 7.66 | — |
| ZILUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.0020015 | -1.72 | -0.12 | — |
| NOTUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.00036885 | -0.18 | 1.94 | — |
| BIOUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.022215 | -0.70 | 1.10 | — |
| HMSTRUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.0001404 | -0.07 | 0.93 | — |
| SCRUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.019465 | 2.13 | 6.96 | — |
| VELODROMEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.029835 | -1.42 | 3.87 | — |
| ADAUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.20475 | -0.42 | 0.46 | — |
| CFXUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.04769 | 0.02 | 0.65 | — |
| PENDLEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 1.96 | -1.48 | 1.33 | — |
| SEIUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.05231 | -1.72 | 0.48 | — |
| XPLUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.07329 | -2.36 | 0.78 | — |
| ZENUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 5.7115 | -0.34 | 2.21 | — |
| BANDUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.20115 | -0.62 | 3.06 | — |
| ONEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.001309 | -1.53 | -2.22 | — |
| SATSUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 1.0028e-08 | -0.74 | 1.21 | — |
| SENTUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.02053 | 2.00 | 9.84 | — |
| SPACEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.003631 | -0.11 | 1.96 | — |
| TRBUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 17.235 | -0.38 | 0.67 | — |
| XTSLAUSDT | OKX | Yeni kırılım | 26.10.2026 19:46 | 395.045 | -0.58 | 2.87 | — |
| XAVGOUSDT | OKX | Yeni kırılım | 26.10.2026 19:46 | 329.41 | 0.43 | 4.09 | — |
| XDELLUSDT | OKX | Yeni kırılım | 26.10.2026 19:46 | 470.555 | -0.41 | 6.97 | — |
| XINTCUSDT | OKX | Yeni kırılım | 26.10.2026 19:46 | 90.79 | -0.64 | 3.26 | — |
| XRKLBUSDT | OKX | Yeni kırılım | 26.10.2026 19:46 | 54.49 | -1.14 | 8.02 | — |
| ZECUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 1232.965 | -1.07 | 6.58 | — |
| ENAUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.206955 | 0.30 | 3.15 | — |
| CVCUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.024085 | 4.88 | 1.39 | — |
| VVVUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 24.8 | -0.28 | 3.79 | — |
| ACHUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.0050125 | -0.73 | 0.15 | — |
| XLMUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.16836 | -0.44 | 0.51 | — |
| MONUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.02178 | -2.53 | -1.19 | — |
| UNIUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 7.0455 | -0.05 | 1.43 | — |
| 1INCHUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.088065 | -1.07 | 0.02 | — |
| ARUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 3.3885 | 0.13 | 1.46 | — |
| BETHUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 2314.35 | -0.20 | 1.49 | — |
| ETHFIUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.63465 | 1.22 | 5.07 | — |
| SOLUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 101.085 | -1.04 | -0.12 | — |
| SUIUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.9113 | -0.31 | 1.46 | — |
| TAOUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 251.535 | -1.25 | 0.18 | — |
| XEWYUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 152.865 | 1.36 | 3.03 | — |
| QTUMUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.82625 | -0.80 | 0.44 | — |
| INJUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 7.815 | 0.58 | 4.29 | — |
| LITUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 3.08815 | -2.95 | -1.92 | — |
| STETHUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 2314.045 | -0.09 | 1.51 | — |
| UMAUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.3538 | -0.45 | -0.62 | — |
| XRPUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 1.29045 | 0.56 | 2.42 | — |
| XSKHYUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 141.265 | 3.20 | 3.48 | — |
| FILUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.9087 | -1.47 | -1.06 | — |
| JUPUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.27805 | -1.17 | 0.31 | — |
| OKSOLUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 101.025 | -0.83 | -0.02 | — |
| PEOPLEUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.007491 | -0.88 | 3.38 | — |
| TNSRUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.02956 | -0.54 | 1.35 | — |
| VIRTUALUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.6163 | -0.58 | 1.49 | — |
| WLDUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.43865 | -0.33 | -0.22 | — |
| AVNTUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.111175 | -2.77 | -1.68 | — |
| CETUSUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.021175 | 0.31 | 2.48 | — |
| PARTIUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.038145 | 0.41 | -1.22 | — |
| TRUMPUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 1.6815 | -0.39 | 0.51 | — |
| NOTUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0003695 | -0.19 | 1.65 | — |
| BLESSUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.008177 | 1.27 | 1.30 | — |
| FARTCOINUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.127285 | 0.37 | 1.91 | — |
| GIGGLEUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 30.095 | 0.05 | 2.54 | — |
| PIUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.07653 | -0.30 | -0.88 | — |
| WLFIUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.05339 | -1.55 | -2.00 | — |
| CFXUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.04764 | 0.27 | 0.48 | — |
| MINUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0031095 | -1.98 | -1.30 | — |
| MOVRUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 1.09225 | 0.22 | 3.19 | — |
| POWERUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.07827 | -1.21 | 0.60 | — |
| PUMPUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0042405 | -2.16 | 0.65 | — |
| RVNUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.001341 | 1.64 | 7.61 | — |
| ETCUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 7.565 | -0.33 | 0.20 | — |
| SHIBUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 4.8515e-06 | -0.26 | 0.18 | — |
| AEROUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.68045 | -1.71 | 3.33 | — |
| COOKIEUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0088385 | -0.98 | 1.40 | — |
| HUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.05535 | 0.40 | 2.08 | — |
| LINEAUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.002518 | -1.87 | -1.43 | — |
| ADAUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.20455 | -0.32 | 0.32 | — |
| APEXUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.2207 | -0.77 | 2.08 | — |
| BICOUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.01492 | -0.60 | 4.22 | — |
| DOGEUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.077185 | 0.23 | 1.15 | — |
| FLOCKUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.040705 | -1.09 | 1.98 | — |
| GALAUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0017415 | -1.69 | -1.00 | — |
| LINKUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 11.4335 | -0.88 | 0.15 | — |
| OWLUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0005305 | -7.94 | -8.28 | — |
| POLUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.09099 | -1.34 | 0.22 | — |
| PONSUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.244153 | -2.50 | 4.44 | — |
| XPLUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.07326 | -2.28 | 0.53 | — |
| STRKUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.045595 | 1.55 | 1.22 | — |
| SOILUSDT | MEXC | Yeni kırılım | 26.10.2026 19:49 | 0.12826 | -0.53 | -0.09 | — |
| BEATUSDT | MEXC | Yeni kırılım | 26.10.2026 19:49 | 0.08362 | -5.64 | 7.69 | — |
| CLANKERUSDT | MEXC | Yeni kırılım | 26.10.2026 19:49 | 13.64 | -0.81 | 0.44 | — |
| TRIAUSDT | MEXC | Yeni kırılım | 26.10.2026 19:49 | 0.002795 | 3.04 | 6.26 | — |
| YBUSDT | MEXC | Yeni kırılım | 26.10.2026 19:49 | 0.06585 | -4.36 | -1.46 | — |
| CVXUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 2.4655 | -7.44 | -7.04 | — |
| ENAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.20664 | 0.42 | 2.85 | — |
| ZECUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 1231.74 | -0.81 | 6.52 | — |
| LUNAMUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.00034772 | -0.66 | 0.07 | — |
| AGRSUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.24275 | 1.96 | 12.91 | — |
| M87USDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 1.668e-05 | -0.06 | -2.22 | — |
| UNIUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 7.0305 | 0.12 | 1.44 | — |
| PEPEUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 4.377e-06 | -1.21 | 1.64 | — |
| XCXUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.0022715 | -4.35 | -7.36 | — |
| INJUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 7.808 | 0.40 | 3.88 | — |
| LITUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 3.0799 | -2.66 | -1.81 | — |
| ARUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 3.384 | 0.35 | 1.27 | — |
| DINUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.0045765 | 0.19 | 0.12 | — |
| ETHFIUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.63415 | 1.24 | 4.75 | — |
| FEGUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 2.9635e-05 | 2.14 | 2.41 | — |
| FILUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.90795 | -1.37 | -1.31 | — |
| MAPOUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.00122355 | -10.02 | -10.87 | — |
| SOLUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 101.085 | -0.97 | -0.24 | — |
| VIRTUALUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.6157 | -0.41 | 1.40 | — |
| WELFUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.06665 | 15.99 | 12.51 | — |
| WXTUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.0179935 | -0.66 | 0.02 | — |
| BTCMTUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.6551 | -0.12 | -0.09 | — |
| CRYPGPTUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.0909 | -0.41 | 0.44 | — |
| IOTAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.042295 | -1.22 | -0.56 | — |
| SUIUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.91015 | -0.08 | 1.48 | — |
| WBTCUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 79828.225 | -0.33 | 0.69 | — |
| WLDUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.43745 | -0.22 | -0.17 | — |
| EVAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 43.915 | -0.33 | 0.63 | — |
| WUSDT | OKX | Erken dönüş | 26.10.2026 23:32 | 0.012345 | 0.62 | — | — |
| COMPUSDT | OKX | Erken dönüş | 26.10.2026 23:32 | 21.755 | -1.45 | — | — |
| FLUIDUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 23:32 | 2.188 | 1.59 | — | — |
| LQTYUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 23:32 | 0.1938 | -0.21 | — | — |
| APTMUSDT | MEXC | Erken dönüş | 26.10.2026 23:36 | 0.05199 | 0.08 | — | — |
| QUSDT | MEXC | Erken dönüş | 26.10.2026 23:36 | 0.1341405 | -22.83 | — | — |
| ARXUSDT | MEXC | Erken dönüş | 26.10.2026 23:36 | 0.22615 | 0.33 | — | — |
| COMPUSDT | MEXC | Erken dönüş | 26.10.2026 23:36 | 21.79 | -1.47 | — | — |
| SYMMUSDT | MEXC | Yeni kırılım | 26.10.2026 23:36 | 0.0307 | 17.26 | — | — |
| VERONAUSDT | MEXC | Yeni kırılım | 26.10.2026 23:36 | 0.13405 | -7.50 | — | — |
| JEANPHILUSDT | MEXC | Yeni kırılım | 26.10.2026 23:36 | 0.0045445 | 1.02 | — | — |
| FUELUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 23:36 | 0.00079595 | -0.36 | — | — |
| TIAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 23:36 | 0.54485 | -3.11 | — | — |
| ALEXUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 23:36 | 0.0038645 | 2.86 | — | — |
| GRVTUSDT | OKX | Erken dönüş | 27.10.2026 03:39 | 0.213205 | 0.58 | — | — |
| BATUSDT | OKX | Erken dönüş | 27.10.2026 03:39 | 0.14842 | 0.35 | — | — |
| XAAOIUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 73.69 | -0.12 | — | — |
| XAMDUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 537.745 | 0.59 | — | — |
| XCOHRUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 225.63 | 1.81 | — | — |
| XDRAMUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 49.47 | 0.81 | — | — |
| XGEVUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 861.89 | 1.42 | — | — |
| XINTWUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 17.675 | 0.54 | — | — |
| XMRVLUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 236.485 | 0.62 | — | — |
| XMUUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 917.215 | 1.11 | — | — |
| XNVDAUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 217.165 | 0.64 | — | — |
| XSMHUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 546.985 | 0.83 | — | — |
| XSOXLUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 93.21 | 2.25 | — | — |
| XTQQQUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 69.35 | 0.65 | — | — |
| XARMUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 226.955 | 0.11 | — | — |
| XKORUUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 11.52 | 0.87 | — | — |
| OPUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 03:39 | 0.112425 | -0.73 | — | — |
| ZKUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 03:39 | 0.012207 | 0.51 | — | — |
| PVTUSDT | MEXC | Tutunma | 27.10.2026 03:42 | 0.0001008 | 0.10 | — | — |
| MASKUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.40145 | -0.83 | — | — |
| TUTUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.0175235 | 2.43 | — | — |
| USUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.00528 | -6.63 | — | — |
| AIAUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.074555 | -3.29 | — | — |
| BASECATUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.010385 | 11.89 | — | — |
| TELUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.0015175 | 3.13 | — | — |
| AINUSDT | MEXC | Yeni kırılım | 27.10.2026 03:42 | 0.07002 | 96.02 | — | — |
| SYNUSDT | MEXC | Yeni kırılım | 27.10.2026 03:42 | 0.186635 | -4.69 | — | — |
| DVOUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 03:42 | 0.00485085 | -0.05 | — | — |
| IMXUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 03:42 | 0.13905 | -0.72 | — | — |
| TOWERUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 03:42 | 0.0001345 | -0.22 | — | — |
| XSPYUSDT | OKX | Tutunma | 27.10.2026 07:33 | 767.345 | 0.45 | — | — |
| ZBCNUSDT | OKX | Erken dönüş | 27.10.2026 07:33 | 0.0022456 | -3.48 | — | — |
| IOSTUSDT | OKX | Erken dönüş | 27.10.2026 07:33 | 0.000815 | -4.01 | — | — |
| LAYERUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 07:33 | 0.06465 | -1.18 | — | — |
| NEXAUSDT | MEXC | Erken dönüş | 27.10.2026 07:37 | 8.605e-07 | -13.33 | — | — |
| ANIMEUSDT | MEXC | Erken dönüş | 27.10.2026 07:37 | 0.002841 | 4.93 | — | — |
| POKTUSDT | MEXC | Yeni kırılım | 27.10.2026 07:37 | 0.01067 | -19.73 | — | — |
| TAKEUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 07:37 | 0.068745 | 8.26 | — | — |
| ZORAUSDT | OKX | Erken dönüş | 27.10.2026 11:40 | 0.006372 | — | — | — |
| XSOXSUSDT | OKX | Erken dönüş | 27.10.2026 11:40 | 48.42 | — | — | — |
| AGLDUSDT | OKX | Erken dönüş | 27.10.2026 11:40 | 0.17855 | — | — | — |
| NMRUSDT | OKX | Erken dönüş | 27.10.2026 11:40 | 9.767 | — | — | — |
| DASHUSDT | OKX | Yeni kırılım | 27.10.2026 11:40 | 55.11 | — | — | — |
| XCRWDUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 11:40 | 260.435 | — | — | — |
| ALGOUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 11:40 | 0.103425 | — | — | — |
| ARKMUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 11:40 | 0.11809 | — | — | — |
| AVAUSDT | MEXC | Erken dönüş | 27.10.2026 11:44 | 0.36415 | — | — | — |
| HINTUSDT | MEXC | Erken dönüş | 27.10.2026 11:44 | 0.0008701 | — | — | — |
| TRUTHUSDT | MEXC | Yeni kırılım | 27.10.2026 11:44 | 0.021048 | — | — | — |
| STAMPUSDT | MEXC | Yeni kırılım | 27.10.2026 11:44 | 0.0004802 | — | — | — |
| BCHUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 11:44 | 281.75 | — | — | — |
| TICSUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 11:44 | 0.000672 | — | — | — |
| GAGUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 11:44 | 0.004666 | — | — | — |
| XBOTUSDT | OKX | Tutunma | 27.10.2026 15:42 | 23.87 | — | — | — |
| ASPUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 0.0139275 | — | — | — |
| LSKUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 0.16987 | — | — | — |
| XAMZNUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 251.115 | — | — | — |
| XUSARUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 9.12 | — | — | — |
| XNBISUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 160.385 | — | — | — |
| XAMATUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 396.1 | — | — | — |
| XSMCIUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 33.525 | — | — | — |
| XORCLUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 128.285 | — | — | — |
| XHIMSUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 27.895 | — | — | — |
| SWFTCUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 0.0026045 | — | — | — |
| HUMAUSDT | OKX | Yeni kırılım | 27.10.2026 15:42 | 0.027195 | — | — | — |
| XVRTUSDT | OKX | Yeni kırılım | 27.10.2026 15:42 | 204.805 | — | — | — |
| BASEDUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 15:42 | 0.052675 | — | — | — |
| XSNDKUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 15:42 | 1281.35 | — | — | — |
| VVVUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 25.7316 | — | — | — |
| CASHCATUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 0.098615 | — | — | — |
| CPUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 0.00951 | — | — | — |
| BTWUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 1.467582 | — | — | — |
| XPUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 0.0084105 | — | — | — |
| WARDUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 0.002551 | — | — | — |
| HAEDALUSDT | MEXC | Yeni kırılım | 27.10.2026 15:46 | 0.02476 | — | — | — |
| LUCKYUSDT | MEXC | Yeni kırılım | 27.10.2026 15:46 | 0.001404 | — | — | — |
| HUMAUSDT | MEXC | Yeni kırılım | 27.10.2026 15:46 | 0.02654 | — | — | — |
| XDCUSDT | MEXC | Yeni kırılım | 27.10.2026 15:46 | 0.035375 | — | — | — |
| EDELUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.032405 | — | — | — |
| DEPUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.0010172 | — | — | — |
| HPUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.007858 | — | — | — |
| MYSTUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.077425 | — | — | — |
| ZIGUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.041114 | — | — | — |
| XNAUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 3.0035e-05 | — | — | — |
| ATHUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.0057595 | — | — | — |
| MEGAUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.048015 | — | — | — |
| ROBOUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.005801 | — | — | — |
| XAAPLUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 346.445 | — | — | — |
| XHOODUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 96.365 | — | — | — |
| GRASSUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.7 | — | — | — |
| OMIUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.00027155 | — | — | — |
| AEVOUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.021825 | — | — | — |
| PEPEUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 4.44505e-06 | — | — | — |
| API3USDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.25905 | — | — | — |
| CFGUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.108345 | — | — | — |
| ETHUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 2347.695 | — | — | — |
| FLOWUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.026355 | — | — | — |
| GRTUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.022495 | — | — | — |
| KAIAUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.035265 | — | — | — |
| KITEUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.11818 | — | — | — |
| PAXGUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 4066.2 | — | — | — |
| XCBRSUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 117.69 | — | — | — |
| BRL1USDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.1871 | — | — | — |
| RONUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.054205 | — | — | — |
| ENJUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.025465 | — | — | — |
| MMTUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.14255 | — | — | — |
| OLUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.0059965 | — | — | — |
| PENGUUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.007687 | — | — | — |
| PROVEUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.1902 | — | — | — |
| SSVUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 2.441 | — | — | — |
| BCHUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 290.69 | — | — | — |
| XSNXXUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 9.0805 | — | — | — |
| XTSMUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 437.38 | — | — | — |
| XWDCUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 383.095 | — | — | — |
| ZAMAUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 0.076345 | — | — | — |
| XALABUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 282.735 | — | — | — |
| XASTSUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 43.055 | — | — | — |
| XBEUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 220.655 | — | — | — |
| XMVLLUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 28.665 | — | — | — |
| ADXUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.05405 | — | — | — |
| DYDXUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.108505 | — | — | — |
| GRVTUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.22995 | — | — | — |
| MARSCOINUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.068555 | — | — | — |
| QUBICUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 4.269e-07 | — | — | — |
| STABLEUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.027418 | — | — | — |
| TLMUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.0012034 | — | — | — |
| GRASSUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.7087 | — | — | — |
| QRLUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 1.25273 | — | — | — |
| ROBOUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.005796 | — | — | — |
| SYLUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 5.655e-05 | — | — | — |
| CFGUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.1081 | — | — | — |
| FETUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.18 | — | — | — |
| IOUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.15039 | — | — | — |
| MEGAUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.04792 | — | — | — |
| COCOUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.15527 | — | — | — |
| ETHUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 2344.865 | — | — | — |
| LDOUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.37505 | — | — | — |
| LNQUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.0092495 | — | — | — |
| OGYUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.00126075 | — | — | — |
| ARKMUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.11935 | — | — | — |
| AZTECUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.01779 | — | — | — |
| DYMUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.01788 | — | — | — |
| GMXUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 8.4655 | — | — | — |
| MYXUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.06142 | — | — | — |
| RIFUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.070155 | — | — | — |
| OMIUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.0002718 | — | — | — |
| ZROUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 1.6772 | — | — | — |
| BXEUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.0016745 | — | — | — |
| HANAUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.014226 | — | — | — |
| ACUUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.131585 | — | — | — |
| INXUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.0048755 | — | — | — |
| LABUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.044255 | — | — | — |
| STOPUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.001795 | — | — | — |
| WUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.012784 | — | — | — |
| ELSAUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 19:50 | 0.082515 | — | — | — |
| MINIMAUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 19:50 | 0.003365 | — | — | — |
| BDXUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 19:50 | 0.07534 | — | — | — |

### Grupların ayrı ölçümleri

| Grup | Borsa | Süre | Ölçülen / kayıt | Medyan % | BTC üstü puan | Kontrol üstü puan |
|---|---|---:|---:|---:|---:|---:|
| Geri testte tutunma / SAR | MEXC | 12s | 1/1 | -0.37 | -0.43 | 1.26 |
| Geri testte tutunma / SAR | MEXC | 24s | 0/1 | — | — | — |
| Geri testte tutunma / SAR | MEXC | 48s | 0/1 | — | — | — |
| Geri testte tutunma / SAR | OKX | 12s | 1/3 | 7.69 | 6.60 | 6.68 |
| Geri testte tutunma / SAR | OKX | 24s | 0/3 | — | — | — |
| Geri testte tutunma / SAR | OKX | 48s | 0/3 | — | — | — |
| Erken dönüş | MEXC | 12s | 61/100 | -0.39 | -0.08 | -0.19 |
| Erken dönüş | MEXC | 24s | 49/100 | 0.65 | -0.06 | 0.30 |
| Erken dönüş | MEXC | 48s | 0/100 | — | — | — |
| Erken dönüş | OKX | 12s | 70/120 | -0.91 | -0.55 | -0.45 |
| Erken dönüş | OKX | 24s | 63/120 | 0.78 | 0.17 | 0.31 |
| Erken dönüş | OKX | 48s | 0/120 | — | — | — |
| Yatay fiyat / hacim artışı | MEXC | 12s | 52/69 | -0.33 | -0.10 | -0.11 |
| Yatay fiyat / hacim artışı | MEXC | 24s | 45/69 | 0.18 | -0.39 | 0.29 |
| Yatay fiyat / hacim artışı | MEXC | 48s | 0/69 | — | — | — |
| Yatay fiyat / hacim artışı | OKX | 12s | 57/65 | -0.45 | -0.06 | 0.07 |
| Yatay fiyat / hacim artışı | OKX | 24s | 51/65 | 0.93 | 0.17 | 0.25 |
| Yatay fiyat / hacim artışı | OKX | 48s | 0/65 | — | — | — |
| Yeni kırılım | MEXC | 12s | 25/45 | -0.81 | -0.73 | -0.15 |
| Yeni kırılım | MEXC | 24s | 15/45 | -1.22 | -1.60 | -1.63 |
| Yeni kırılım | MEXC | 48s | 0/45 | — | — | — |
| Yeni kırılım | OKX | 12s | 27/56 | 0.54 | 0.70 | 0.22 |
| Yeni kırılım | OKX | 24s | 12/56 | 3.06 | 2.31 | 3.19 |
| Yeni kırılım | OKX | 48s | 0/56 | — | — | — |
| Tutunma | MEXC | 12s | 10/15 | -1.54 | -1.63 | -2.11 |
| Tutunma | MEXC | 24s | 2/15 | 0.72 | 0.72 | -1.22 |
| Tutunma | MEXC | 48s | 0/15 | — | — | — |
| Tutunma | OKX | 12s | 2/7 | 3.55 | 2.46 | 1.04 |
| Tutunma | OKX | 24s | 0/7 | — | — | — |
| Tutunma | OKX | 48s | 0/7 | — | — | — |

## Önceki V4 kayıtları — yeni kayıt alınmıyor

Eski gerçek giriş fiyatları korunur; bunlar yeni grupların geçmişte yakaladığı örnekler değildir. 12/24/48s ölçümleri ayrı sürdürülür.

## Gerçek gözlemden sonraki ölçümler

Her sürüm ve borsanın ilk gerçek alış/satış orta fiyatı ayrı kaydedilir. Aynı coin grup değiştirse de yeni bağımsız örnek sayılmaz. Hedef saatten sonraki ilk dakika kapanışı kullanılır; gecikme 60 saniyeden küçüktür. Ücret/kayma dahil net kâr değildir. Henüz oluşmamış veya eksik ölçümler boş kalır.

8 borsa kaydı, 8 farklı sembol. Ortak semboller iki bağımsız başarı gibi toplanmaz.

| Borsa | Süre | Ölçülen | Medyan % | BTC üstü puan | Kontrol üstü puan | Kontrol ölçülen |
|---|---:|---:|---:|---:|---:|---:|
| MEXC | 12s | 8/8 | -2.13 | -1.79 | -2.12 | 8 |
| MEXC | 24s | 8/8 | -2.41 | -1.82 | -2.00 | 8 |
| MEXC | 48s | 0/8 | — | — | — | 0 |

| Coin | Borsa | İlk grup | Gerçek gözlem TR | Referans fiyat | 12s % | 24s % | 48s % |
|---|---|---|---|---:|---:|---:|---:|
| BULLAUSDT | MEXC | Yeni kırılım | 26.10.2026 11:48 | 0.1130635 | 35.79 | 4.11 | — |
| CAPUSDT | MEXC | Tutunma | 26.10.2026 00:23 | 0.10956 | -21.28 | -9.24 | — |
| CPHUSDT | MEXC | Tutunma | 26.10.2026 11:48 | 0.0035595 | -3.05 | -3.55 | — |
| GBCKUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.0048565 | -0.59 | -1.27 | — |
| MIUUSDT | MEXC | Yeni kırılım | 26.10.2026 03:52 | 8.85e-10 | 5.08 | 3.95 | — |
| NEXUSDT | MEXC | Yeni kırılım | 26.10.2026 11:48 | 7.95e-07 | -10.87 | -9.67 | — |
| STONKSUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.0020883 | -19.28 | -24.35 | — |
| TAUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.06203 | -1.21 | -0.18 | — |

Karşılaştırma için en az 1–2 haftalık gerçek kayıt beklenir. Gruplar, borsalar ve ortak coinler dikkate alınmadan bir kazanma oranı iddia edilmez.


<!-- coin-priority-raw:end -->

</details>
