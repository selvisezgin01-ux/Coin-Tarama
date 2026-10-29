# Coin Tarama 3 — kısa öncelik listesi

Son kontrol: 29.10.2026 23:47 TR.

Geniş havuz: 12 borsa kaydı / 10 sembol. İşlem koşulu elemesini geçen: 0 farklı sembol. Bildirim ve üst liste: en fazla 5 farklı coin.

**Öncelik, kârlılık veya güvenli işlem garantisi değildir.** Hacim/makas, güncel fiyat, yapı ve uzama kontrollerinden geçenler sıralanır. Yalnız yatay hacim hazırlığı bildirilmez. Aday yoksa liste doldurulmaz.

| Coin | Fiyat borsası | Geçen borsalar | Grup | Gerçek gözlem TR | Fiyat | Makas % | Yapı mesafesi % |
|---|---|---|---|---|---:|---:|---:|

Şu an öncelik koşullarını sağlayan aday yok.

Sıralama: en çok 4x sayılan göreli hacim, kapanış konumu, dar makas ve aynı borsanın hacmi. Farklı borsaların hacimleri toplanmaz. Bu sıra başarı olasılığı değildir.

Başlangıç elemesi: en az 100.000 USDT kapalı 24s hacim, en çok %0,5 makas, izlenen seviyeyi koruyan güncel fiyat, kapanıştan en çok 1 ATR uzaklık, EMA20 üstüne en çok 2,5 ATR uzama ve yapı referansına en çok %12 mesafe. 20x üzeri hacim ayrıca incelemede kalır. Bunlar daha iyi sonuç verdiği kanıtlanmış yeni strateji eşikleri değildir.

Aynı sembol tek satırda gösterilir; yalnız elemeden geçen borsalar listelenir. Sembol eşleşmesi bağımsız kontrat kimliği teyidi değildir. Geniş havuz ve eski ölçümler korunur. [Tanınan OKX hisse tokenlerinin kaynağı](https://www.okx.com/help/okx-to-list-tokenized-stocks-for-trading). Liste 2026-10-26 tarihinde kontrol edildi; yeni hisse tokenlerinin eklenmesi gerekebilir.

## Eleme özeti

- 2 borsa kaydı: EMA20 uzaklığı fazla veya bilinmiyor
- 2 borsa kaydı: olağandışı hacim katsayısı; ayrıca inceleme
- 1 borsa kaydı: tanınan tokenleştirilmiş hisse
- 5 borsa kaydı: güncel fiyat kapanıştan uzak veya veri eksik
- 5 borsa kaydı: yapı bozulma mesafesi geniş veya bilinmiyor
- 7 borsa kaydı: makas geniş veya bilinmiyor
- 6 borsa kaydı: izlenen seviye kaybedilmiş veya bilinmiyor
- 7 borsa kaydı: hacim 100.000 USDT altında

Bir kayıtta birden fazla neden olabilir; sayılar bağımsız coinler gibi toplanmaz.
Sıralama sınırı dışında kalan uygun sembol: 0.


## Öncelik listesinin ayrı gerçek gözlem ölçümleri

Referans, bu kısa listeye ilk girişte gerçekten okunan fiyat ve saattir; eski geniş listedeki daha erken fiyat kullanılmaz. 12/24/48s ölçümleri state.json içinde ayrı tutulur. Aynı sembolün iki borsa kaydı bağımsız iki coin sayılmaz.

<details>
<summary>Öncelik listesinin 12/24/48 saat sonuçlarını aç</summary>

| Coin | Borsa | İlk gerçek gözlem TR | Referans | 12s % | 24s % | 48s % |
|---|---|---|---:|---:|---:|---:|
| LUNAUSDT | OKX | 26.10.2026 16:56 | 0.04159 | 1.37 | 1.08 | 2.14 |
| METUSDT | OKX | 26.10.2026 16:56 | 0.31085 | 1.59 | 1.43 | -0.50 |
| CRVUSDT | OKX | 26.10.2026 16:56 | 0.3495 | -3.52 | -4.89 | -4.09 |
| NIGHTUSDT | MEXC | 26.10.2026 16:56 | 0.03791 | 4.91 | 4.48 | 5.94 |
| ONDOUSDT | MEXC | 26.10.2026 16:56 | 0.41274 | -0.50 | -0.48 | 0.53 |
| ARBUSDT | MEXC | 26.10.2026 17:50 | 0.171355 | -2.17 | -1.96 | -3.67 |
| CELOUSDT | OKX | 26.10.2026 19:50 | 0.079105 | -0.89 | 3.91 | 0.39 |
| POLUSDT | OKX | 26.10.2026 19:50 | 0.091045 | -1.40 | 0.12 | 0.24 |
| ONDOUSDT | OKX | 26.10.2026 19:50 | 0.41515 | -1.96 | -0.08 | -0.37 |
| WLFIUSDT | OKX | 26.10.2026 19:50 | 0.053445 | -1.71 | -2.01 | -2.42 |
| MOVRUSDT | MEXC | 26.10.2026 19:50 | 1.0922 | 0.37 | 3.16 | 2.08 |
| COMPUSDT | MEXC | 26.10.2026 23:37 | 21.79 | -1.42 | -2.16 | -1.33 |
| ARXUSDT | MEXC | 26.10.2026 23:37 | 0.2252 | 0.84 | 8.75 | 8.08 |
| XKORUUSDT | OKX | 27.10.2026 03:44 | 11.475 | 0.83 | 7.36 | 17.21 |
| QNTUSDT | MEXC | 27.10.2026 03:44 | 203.095 | -0.44 | -1.62 | -1.69 |
| CLANKERUSDT | MEXC | 27.10.2026 03:44 | 13.645 | -0.77 | 1.65 | -5.31 |
| TELUSDT | MEXC | 27.10.2026 03:44 | 0.0015175 | 3.00 | 0.03 | -3.53 |
| IOSTUSDT | OKX | 27.10.2026 07:38 | 0.0008208 | -4.25 | -3.61 | -6.21 |
| ZBCNUSDT | OKX | 27.10.2026 07:38 | 0.00222315 | -2.38 | -5.71 | -7.64 |
| XSOXSUSDT | OKX | 27.10.2026 11:46 | 48.635 | -10.02 | -14.32 | -11.05 |
| ZORAUSDT | OKX | 27.10.2026 11:46 | 0.006395 | 2.31 | 1.13 | -0.81 |
| DASHUSDT | OKX | 27.10.2026 11:46 | 54.99 | 0.64 | -1.45 | -7.60 |
| TRUTHUSDT | MEXC | 27.10.2026 11:46 | 0.0210175 | 0.19 | -0.18 | 10.88 |
| AVAUSDT | MEXC | 27.10.2026 11:46 | 0.36365 | -1.86 | -6.31 | -12.11 |
| LSKUSDT | OKX | 27.10.2026 15:48 | 0.169625 | -1.21 | -1.77 | 1.19 |
| CASHCATUSDT | MEXC | 27.10.2026 15:48 | 0.09844 | 4.07 | 0.71 | 3.85 |
| XDCUSDT | MEXC | 27.10.2026 15:48 | 0.03539 | -4.61 | -5.23 | -6.10 |
| VVVUSDT | MEXC | 27.10.2026 15:48 | 25.6305 | 0.71 | -5.71 | -8.25 |
| CFGUSDT | OKX | 27.10.2026 19:53 | 0.10832 | 0.64 | -4.62 | -1.04 |
| STETHUSDT | OKX | 27.10.2026 19:53 | 2344.565 | 0.46 | -0.50 | 0.59 |
| IOUSDT | MEXC | 27.10.2026 19:53 | 0.15046 | -0.49 | -0.11 | 0.32 |
| PENGUUSDT | MEXC | 27.10.2026 19:53 | 0.007689 | 1.56 | 0.10 | 3.71 |
| HYPEUSDT | OKX | 27.10.2026 23:23 | 81.2315 | 0.10 | -0.23 | 15.06 |
| ROSEUSDT | MEXC | 27.10.2026 23:23 | 0.006775 | 0.58 | 0.83 | -2.89 |
| LYNUSDT | MEXC | 27.10.2026 23:23 | 0.01493 | 1.21 | 5.29 | -6.90 |
| ZENUSDT | MEXC | 27.10.2026 23:23 | 5.911 | 0.42 | -0.08 | -1.64 |
| NIGHTUSDT | OKX | 28.10.2026 03:54 | 0.0419635 | -4.32 | -3.62 | — |
| XSNXXUSDT | OKX | 28.10.2026 03:54 | 9.3325 | 3.72 | 7.42 | — |
| SAHARAUSDT | OKX | 28.10.2026 07:47 | 0.0080505 | -2.48 | -3.21 | — |
| ENSUSDT | OKX | 28.10.2026 07:47 | 5.283 | -0.74 | -2.21 | — |
| BCHUSDT | OKX | 28.10.2026 07:47 | 298.04 | -3.29 | -6.10 | — |
| ZAMAUSDT | OKX | 28.10.2026 11:56 | 0.078535 | -4.46 | -6.27 | — |
| MEGAUSDT | OKX | 28.10.2026 11:56 | 0.049225 | 4.07 | -2.73 | — |
| 4USDT | MEXC | 28.10.2026 11:56 | 0.012575 | -0.99 | -4.97 | — |
| PEAQUSDT | MEXC | 28.10.2026 11:56 | 0.03526 | -1.73 | -4.28 | — |
| RVNUSDT | OKX | 28.10.2026 15:55 | 0.0014715 | 1.46 | -2.62 | — |
| PROSUSDT | OKX | 28.10.2026 15:55 | 0.631 | -1.38 | -0.97 | — |
| HANAUSDT | MEXC | 28.10.2026 15:55 | 0.0146155 | 9.66 | 0.91 | — |
| GOMININGUSDT | MEXC | 28.10.2026 15:55 | 0.3936 | -1.50 | -4.01 | — |
| BICOUSDT | OKX | 28.10.2026 19:55 | 0.015915 | 3.74 | 9.83 | — |
| XPLUSDT | OKX | 28.10.2026 19:55 | 0.076615 | -1.05 | 1.61 | — |
| CSPRUSDT | OKX | 28.10.2026 23:45 | 0.0023005 | -0.89 | -4.76 | — |
| EDGEUSDT | OKX | 28.10.2026 23:45 | 0.34995 | -2.67 | -8.39 | — |
| FLRUSDT | OKX | 28.10.2026 23:45 | 0.006184 | -0.92 | -3.06 | — |
| XLMUSDT | OKX | 28.10.2026 23:45 | 0.17297 | -2.88 | -5.86 | — |
| PUMPUSDT | OKX | 28.10.2026 23:45 | 0.0044795 | -5.77 | -8.99 | — |
| ALEOUSDT | MEXC | 29.10.2026 03:55 | 0.03083 | -6.52 | — | — |
| KASUSDT | MEXC | 29.10.2026 03:55 | 0.0371455 | -3.71 | — | — |
| ETHFIUSDT | MEXC | 29.10.2026 03:55 | 0.6829 | -2.86 | — | — |
| XXIAOMIUSDT | OKX | 29.10.2026 07:51 | 3.277 | -0.21 | — | — |
| PIUSDT | MEXC | 29.10.2026 15:55 | 0.07874 | — | — | — |
| NEOUSDT | OKX | 29.10.2026 19:58 | 2.145 | — | — | — |
| SUIUSDT | OKX | 29.10.2026 19:58 | 0.94695 | — | — | — |
| AAVEUSDT | OKX | 29.10.2026 19:58 | 136.255 | — | — | — |
| GASUSDT | OKX | 29.10.2026 19:58 | 1.2229 | — | — | — |
| LITUSDT | MEXC | 29.10.2026 19:58 | 3.2467 | — | — | — |

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

MEXC: incelenen 1008, aday 9; kapanış 29.10.2026 23:00 TR; fiyat gözlemi 29.10.2026 23:45 TR.
V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |
|---|---|---:|---:|---|---|
| QRLUSDT | Erken dönüş | 2.28 | 4.70 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| ATRUSDT | Erken dönüş | 17.64 | 2.04 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| PAIDUSDT | Erken dönüş | 16.88 | 2.31 | Yok | yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| PARTIUSDT | Erken dönüş, Yeni kırılım | 54.50 | 18.79 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| RADUSDT | Erken dönüş, Yeni kırılım | 4.19 | 3.31 | RSI PU teyitli | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; gözlem fiyatı kapanıştan uzaklaştı |
| PAYAIUSDT | Erken dönüş | 20.19 | 2.16 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| OTKUSDT | Erken dönüş | 6.39 | 10.62 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| AVNTUSDT | Erken dönüş | -4.64 | 1.56 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| DUSKUSDT | Erken dönüş | -7.22 | 1.80 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |

OKX: incelenen 347, aday 3; kapanış 29.10.2026 23:00 TR; fiyat gözlemi 29.10.2026 23:42 TR.
V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |
|---|---|---:|---:|---|---|
| PARTIUSDT | Erken dönüş, Yeni kırılım | 53.65 | 180.86 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XDKNGUSDT | Erken dönüş | 2.02 | 23.33 | RSI PU teyitli | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| AVNTUSDT | Erken dönüş | -4.69 | 1.87 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |

İki borsada toplam 10 farklı sembol. Ortak semboller bağımsız iki başarı sayılmaz.

Eşikler başlangıç deneyidir; daha çok aday daha yüksek başarı demek değildir. Yazılım testleri kârlılık kanıtı değildir. Dört saatlik mum ve zamanlayıcı gecikmesi ilk hareketin kaçmasına yol açabilir. SAR yön desteğidir; getiri garantisi değildir.

## Bu döngüde yeni gelenler

PARTIUSDT · OKX
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 29.10.2026 23:42 TR; fiyat 0.060125
24s %53.65; ilgili hacim 180.86x; makas %0.35
24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XDKNGUSDT · OKX
Gruplar: Erken dönüş
Gözlem 29.10.2026 23:42 TR; fiyat 20.535
24s %2.02; ilgili hacim 23.327x; makas %0.24
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; teyitli RSI pozitif uyumsuzluk desteği

AVNTUSDT · OKX
Gruplar: Erken dönüş
Gözlem 29.10.2026 23:42 TR; fiyat 0.098045
24s %-4.69; ilgili hacim 1.8718x; makas %0.23
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı

QRLUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 29.10.2026 23:45 TR; fiyat 1.2331
24s %2.28; ilgili hacim 4.6973x; makas %0.51
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

ATRUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 29.10.2026 23:45 TR; fiyat 0.0003902
24s %17.64; ilgili hacim 2.0369x; makas %0.72
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

PAIDUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 29.10.2026 23:45 TR; fiyat 0.0033785
24s %16.88; ilgili hacim 2.3099x; makas %0.74
yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı

RADUSDT · MEXC
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 29.10.2026 23:45 TR; fiyat 0.2695
24s %4.19; ilgili hacim 3.308x; makas %0.59
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; gözlem fiyatı kapanıştan uzaklaştı; teyitli RSI pozitif uyumsuzluk desteği

PAYAIUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 29.10.2026 23:45 TR; fiyat 0.00754
24s %20.19; ilgili hacim 2.1599x; makas %2.65
ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

OTKUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 29.10.2026 23:45 TR; fiyat 0.0019857
24s %6.39; ilgili hacim 10.62x; makas %0.50
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

AVNTUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 29.10.2026 23:45 TR; fiyat 0.096585
24s %-4.64; ilgili hacim 1.5582x; makas %0.16
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı

DUSKUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 29.10.2026 23:45 TR; fiyat 0.09617
24s %-7.22; ilgili hacim 1.8028x; makas %0.19
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı

## V5 gerçek gözlemden sonraki sonuçlar

Her borsa/token için ilk gerçek fiyat bir ana kayıttır. Gruplar örtüşebilir; grup sayıları bağımsız başarı gibi toplanmaz. Bir gruba sonradan ilk giriş, o andaki gerçek fiyatla ayrıca ölçülür. Getiriler ücret/kayma dahil değildir; eksik ölçüm boş kalır.

| Coin | Borsa | İlk grup | Gerçek gözlem TR | Fiyat | 12s % | 24s % | 48s % |
|---|---|---|---|---:|---:|---:|---:|
| GALFTUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.8066 | -2.05 | -1.69 | -1.35 |
| XQCOMUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 177.525 | 1.92 | 1.97 | 3.90 |
| XGOOGLUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 322.39 | -0.93 | -1.00 | 0.78 |
| ARBUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.170775 | -0.80 | -0.84 | -3.24 |
| ASTRUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.0064895 | -0.35 | -4.66 | -0.01 |
| LUNAUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.041805 | 0.75 | -0.06 | 1.61 |
| METUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.31295 | 2.06 | 2.67 | -0.85 |
| XLITEUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 780.53 | 6.78 | 7.91 | 12.13 |
| SPKUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.01838 | 3.37 | 0.22 | -0.98 |
| XLRCXUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 234.725 | 2.10 | 3.08 | 4.74 |
| CRVUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.35035 | -2.64 | -4.24 | -3.84 |
| XASMLUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 1596.95 | 0.26 | 1.49 | 3.84 |
| IMXUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.1405 | -1.07 | -2.14 | -1.99 |
| CHIPUSDT | OKX | Yeni kırılım | 26.10.2026 15:39 | 0.049285 | 5.04 | 9.12 | 7.15 |
| PYTHUSDT | OKX | Yeni kırılım | 26.10.2026 15:39 | 0.075005 | -0.33 | -2.55 | -4.98 |
| DOODUSDT | OKX | Yeni kırılım | 26.10.2026 15:39 | 0.0023005 | -18.63 | -11.98 | -11.80 |
| DYDXUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 15:39 | 0.108095 | -0.95 | -1.39 | 0.81 |
| LDOUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 15:39 | 0.36995 | 0.50 | -0.26 | 0.47 |
| BICOUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 15:39 | 0.014945 | 0.30 | 1.10 | 4.52 |
| ILVUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 15:39 | 3.099 | -0.94 | -1.74 | -0.94 |
| SPCMUSDT | MEXC | Tutunma | 26.10.2026 15:43 | 0.0008465 | -3.79 | -5.32 | -2.07 |
| TAUSDT | MEXC | Tutunma | 26.10.2026 15:43 | 0.05873 | 5.93 | 6.76 | 6.40 |
| UMXUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.049465 | -13.70 | -3.00 | -30.27 |
| CAKEUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 2.1035 | 1.88 | -2.16 | -0.50 |
| ARBUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.170855 | -0.96 | -1.00 | -3.13 |
| BANKUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.02771 | -7.07 | 3.39 | 1.62 |
| NIGHTUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.038025 | 4.59 | 5.46 | 5.77 |
| NOMUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.001673 | -0.90 | 0.66 | -0.42 |
| SOONUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.3149 | -2.10 | -3.62 | -1.05 |
| UPCUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.12305 | 1.26 | -2.48 | -2.56 |
| GHXUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.009755 | -1.09 | -3.79 | 3.44 |
| TAGUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.0005201 | 32.38 | 58.47 | 30.86 |
| HYPEUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 77.435 | 1.67 | 1.72 | 4.29 |
| METUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.31225 | 2.32 | 2.80 | -0.46 |
| ONDOUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.413185 | 0.04 | -0.21 | 0.30 |
| SAGAUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.01787 | 0.78 | 2.07 | 2.74 |
| 4USDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.01169 | -0.51 | 1.03 | 5.90 |
| NATIXUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.000163895 | 21.65 | 7.91 | 7.03 |
| RUNEUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.6316 | -0.63 | -1.11 | -1.33 |
| MIUUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 9.35e-10 | -0.53 | -1.60 | -6.95 |
| BULLAUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 0.139074 | 10.56 | -52.90 | -53.26 |
| NEXUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 8.0765e-07 | -5.63 | -9.03 | -7.34 |
| PLAYUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 0.017415 | -5.54 | -8.41 | -9.16 |
| QNTUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 220.56 | -7.76 | -8.35 | -10.78 |
| CHIPUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 0.048875 | 5.90 | 10.06 | 7.81 |
| PYTHUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 0.075095 | -0.63 | -2.55 | -4.96 |
| DGMAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.01041 | -9.70 | -9.70 | -13.16 |
| PENGUUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.007525 | 0.20 | 0.31 | 2.72 |
| SHMUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 3.845e-05 | 0.13 | -0.13 | -0.13 |
| HMNDUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.0026355 | -4.72 | -4.57 | 1.76 |
| LYNUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.01345 | 3.87 | 4.76 | 13.38 |
| XLMUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.16945 | 0.09 | -0.44 | 0.27 |
| TRXUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.3313 | -0.54 | -0.85 | 0.12 |
| MONUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.021545 | 1.23 | 0.86 | -1.32 |
| DOGSUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 3.596e-05 | -0.89 | -2.34 | -1.56 |
| PARTIUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.037785 | 1.39 | -0.60 | 1.95 |
| CELOUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.079025 | -0.99 | 3.87 | 0.46 |
| DGBUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.00341 | -3.81 | -2.93 | -2.49 |
| DOGEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.077275 | 0.07 | 1.17 | 2.19 |
| ETCUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 7.564 | -0.49 | 0.42 | -0.38 |
| SUSHIUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.2016 | -0.94 | 2.38 | 1.84 |
| AXSUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.94855 | -0.73 | 0.66 | 0.09 |
| RESOLVUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.01674 | 0.00 | 0.00 | -3.94 |
| SNXUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.19645 | -0.74 | 1.40 | 0.69 |
| TRUMPUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 1.6845 | -0.68 | 0.56 | 1.16 |
| AAVEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 135.3 | -2.31 | -1.95 | -2.73 |
| ACEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.139285 | 2.16 | 2.65 | 3.86 |
| AVAXUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 8.911 | -1.98 | -0.68 | -0.83 |
| FETUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.17425 | -1.52 | 3.70 | 2.90 |
| JITOSOLUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 132.105 | -0.89 | -0.02 | 0.12 |
| JTOUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.43385 | -1.33 | 0.20 | -3.45 |
| LINKUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 11.442 | -0.94 | 0.39 | 0.48 |
| MANAUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.078525 | -1.38 | -0.52 | -0.04 |
| MORPHOUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 2.06625 | 3.67 | 4.85 | 6.25 |
| NEIROUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 6.6295e-05 | -0.44 | 2.18 | 1.21 |
| NIGHTUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.0396665 | -1.16 | -0.55 | 0.96 |
| ONDOUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.41435 | -1.82 | 0.37 | 0.01 |
| POLUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.090985 | -1.30 | 0.32 | 0.38 |
| PONSUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.244 | -2.50 | 5.49 | 16.68 |
| PUMPUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.0042435 | -2.32 | 1.10 | -1.83 |
| RENDERUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 1.7285 | -2.63 | -2.40 | -3.91 |
| WLFIUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.053395 | -1.62 | -1.92 | -2.18 |
| XAPLDUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 18.425 | -1.93 | 6.27 | 5.62 |
| XCRWVUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 56.425 | -1.28 | 4.69 | 6.62 |
| XIRENUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 26.1 | -1.95 | 3.75 | 4.18 |
| XSHAZUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 24.15 | -2.77 | 7.66 | 12.26 |
| ZILUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.0020015 | -1.72 | -0.12 | -0.87 |
| NOTUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.00036885 | -0.18 | 1.94 | 3.89 |
| BIOUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.022215 | -0.70 | 1.10 | 1.28 |
| HMSTRUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.0001404 | -0.07 | 0.93 | 0.85 |
| SCRUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.019465 | 2.13 | 6.96 | 7.32 |
| VELODROMEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.029835 | -1.42 | 3.87 | 3.17 |
| ADAUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.20475 | -0.42 | 0.46 | -1.73 |
| CFXUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.04769 | 0.02 | 0.65 | 0.34 |
| PENDLEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 1.96 | -1.48 | 1.33 | -0.61 |
| SEIUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.05231 | -1.72 | 0.48 | 0.04 |
| XPLUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.07329 | -2.36 | 0.78 | 3.72 |
| ZENUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 5.7115 | -0.34 | 2.21 | 1.76 |
| BANDUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.20115 | -0.62 | 3.06 | 5.24 |
| ONEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.001309 | -1.53 | -2.22 | -2.06 |
| SATSUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 1.0028e-08 | -0.74 | 1.21 | 0.70 |
| SENTUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.02053 | 2.00 | 9.84 | 5.94 |
| SPACEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.003631 | -0.11 | 1.96 | 1.82 |
| TRBUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 17.235 | -0.38 | 0.67 | 0.03 |
| XTSLAUSDT | OKX | Yeni kırılım | 26.10.2026 19:46 | 395.045 | -0.58 | 2.87 | 1.66 |
| XAVGOUSDT | OKX | Yeni kırılım | 26.10.2026 19:46 | 329.41 | 0.43 | 4.09 | 5.56 |
| XDELLUSDT | OKX | Yeni kırılım | 26.10.2026 19:46 | 470.555 | -0.41 | 6.97 | 4.87 |
| XINTCUSDT | OKX | Yeni kırılım | 26.10.2026 19:46 | 90.79 | -0.64 | 3.26 | 3.59 |
| XRKLBUSDT | OKX | Yeni kırılım | 26.10.2026 19:46 | 54.49 | -1.14 | 8.02 | 5.84 |
| ZECUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 1232.965 | -1.07 | 6.58 | 2.82 |
| ENAUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.206955 | 0.30 | 3.15 | -5.56 |
| CVCUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.024085 | 4.88 | 1.39 | -0.73 |
| VVVUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 24.8 | -0.28 | 3.79 | -3.51 |
| ACHUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.0050125 | -0.73 | 0.15 | -0.97 |
| XLMUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.16836 | -0.44 | 0.51 | 0.91 |
| MONUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.02178 | -2.53 | -1.19 | -3.54 |
| UNIUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 7.0455 | -0.05 | 1.43 | 0.05 |
| 1INCHUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.088065 | -1.07 | 0.02 | -0.40 |
| ARUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 3.3885 | 0.13 | 1.46 | 2.11 |
| BETHUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 2314.35 | -0.20 | 1.49 | 0.62 |
| ETHFIUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.63465 | 1.22 | 5.07 | 2.83 |
| SOLUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 101.085 | -1.04 | -0.12 | -0.22 |
| SUIUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.9113 | -0.31 | 1.46 | 1.06 |
| TAOUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 251.535 | -1.25 | 0.18 | -0.03 |
| XEWYUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 152.865 | 1.36 | 3.03 | 7.62 |
| QTUMUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.82625 | -0.80 | 0.44 | 0.38 |
| INJUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 7.815 | 0.58 | 4.29 | -1.31 |
| LITUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 3.08815 | -2.95 | -1.92 | -4.99 |
| STETHUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 2314.045 | -0.09 | 1.51 | 0.81 |
| UMAUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.3538 | -0.45 | -0.62 | -1.30 |
| XRPUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 1.29045 | 0.56 | 2.42 | 1.50 |
| XSKHYUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 141.265 | 3.20 | 3.48 | 16.09 |
| FILUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.9087 | -1.47 | -1.06 | -2.39 |
| JUPUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.27805 | -1.17 | 0.31 | 0.13 |
| OKSOLUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 101.025 | -0.83 | -0.02 | -0.25 |
| PEOPLEUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.007491 | -0.88 | 3.38 | 1.87 |
| TNSRUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.02956 | -0.54 | 1.35 | 1.96 |
| VIRTUALUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.6163 | -0.58 | 1.49 | 0.08 |
| WLDUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.43865 | -0.33 | -0.22 | -3.50 |
| AVNTUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.111175 | -2.77 | -1.68 | -3.96 |
| CETUSUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.021175 | 0.31 | 2.48 | 0.83 |
| PARTIUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.038145 | 0.41 | -1.22 | 0.80 |
| TRUMPUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 1.6815 | -0.39 | 0.51 | 1.22 |
| NOTUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0003695 | -0.19 | 1.65 | 3.60 |
| BLESSUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.008177 | 1.27 | 1.30 | 38.53 |
| FARTCOINUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.127285 | 0.37 | 1.91 | 1.95 |
| GIGGLEUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 30.095 | 0.05 | 2.54 | 3.31 |
| PIUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.07653 | -0.30 | -0.88 | -0.69 |
| WLFIUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.05339 | -1.55 | -2.00 | -2.32 |
| CFXUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.04764 | 0.27 | 0.48 | 0.31 |
| MINUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0031095 | -1.98 | -1.30 | -0.24 |
| MOVRUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 1.09225 | 0.22 | 3.19 | 2.07 |
| POWERUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.07827 | -1.21 | 0.60 | 7.91 |
| PUMPUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0042405 | -2.16 | 0.65 | -1.80 |
| RVNUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.001341 | 1.64 | 7.61 | 9.47 |
| ETCUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 7.565 | -0.33 | 0.20 | -0.46 |
| SHIBUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 4.8515e-06 | -0.26 | 0.18 | 1.33 |
| AEROUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.68045 | -1.71 | 3.33 | 2.84 |
| COOKIEUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0088385 | -0.98 | 1.40 | 0.71 |
| HUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.05535 | 0.40 | 2.08 | 1.81 |
| LINEAUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.002518 | -1.87 | -1.43 | -1.51 |
| ADAUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.20455 | -0.32 | 0.32 | -1.69 |
| APEXUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.2207 | -0.77 | 2.08 | 1.22 |
| BICOUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.01492 | -0.60 | 4.22 | 6.37 |
| DOGEUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.077185 | 0.23 | 1.15 | 2.18 |
| FLOCKUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.040705 | -1.09 | 1.98 | 0.53 |
| GALAUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0017415 | -1.69 | -1.00 | 0.09 |
| LINKUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 11.4335 | -0.88 | 0.15 | 0.48 |
| OWLUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0005305 | -7.94 | -8.28 | -12.89 |
| POLUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.09099 | -1.34 | 0.22 | 0.25 |
| PONSUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.244153 | -2.50 | 4.44 | 16.36 |
| XPLUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.07326 | -2.28 | 0.53 | 3.69 |
| STRKUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.045595 | 1.55 | 1.22 | 0.27 |
| SOILUSDT | MEXC | Yeni kırılım | 26.10.2026 19:49 | 0.12826 | -0.53 | -0.09 | -0.76 |
| BEATUSDT | MEXC | Yeni kırılım | 26.10.2026 19:49 | 0.08362 | -5.64 | 7.69 | -2.32 |
| CLANKERUSDT | MEXC | Yeni kırılım | 26.10.2026 19:49 | 13.64 | -0.81 | 0.44 | -1.39 |
| TRIAUSDT | MEXC | Yeni kırılım | 26.10.2026 19:49 | 0.002795 | 3.04 | 6.26 | 5.90 |
| YBUSDT | MEXC | Yeni kırılım | 26.10.2026 19:49 | 0.06585 | -4.36 | -1.46 | -1.79 |
| CVXUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 2.4655 | -7.44 | -7.04 | -4.64 |
| ENAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.20664 | 0.42 | 2.85 | -5.75 |
| ZECUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 1231.74 | -0.81 | 6.52 | 2.79 |
| LUNAMUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.00034772 | -0.66 | 0.07 | 0.68 |
| AGRSUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.24275 | 1.96 | 12.91 | 7.97 |
| M87USDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 1.668e-05 | -0.06 | -2.22 | -3.60 |
| UNIUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 7.0305 | 0.12 | 1.44 | 0.41 |
| PEPEUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 4.377e-06 | -1.21 | 1.64 | 10.26 |
| XCXUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.0022715 | -4.35 | -7.36 | -5.32 |
| INJUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 7.808 | 0.40 | 3.88 | -1.24 |
| LITUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 3.0799 | -2.66 | -1.81 | -4.81 |
| ARUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 3.384 | 0.35 | 1.27 | 2.30 |
| DINUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.0045765 | 0.19 | 0.12 | 0.43 |
| ETHFIUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.63415 | 1.24 | 4.75 | 2.89 |
| FEGUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 2.9635e-05 | 2.14 | 2.41 | 1.23 |
| FILUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.90795 | -1.37 | -1.31 | -2.55 |
| MAPOUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.00122355 | -10.02 | -10.87 | -8.72 |
| SOLUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 101.085 | -0.97 | -0.24 | -0.22 |
| VIRTUALUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.6157 | -0.41 | 1.40 | 0.16 |
| WELFUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.06665 | 15.99 | 12.51 | 5.06 |
| WXTUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.0179935 | -0.66 | 0.02 | 0.05 |
| BTCMTUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.6551 | -0.12 | -0.09 | -0.64 |
| CRYPGPTUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.0909 | -0.41 | 0.44 | 0.40 |
| IOTAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.042295 | -1.22 | -0.56 | -2.68 |
| SUIUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.91015 | -0.08 | 1.48 | 1.07 |
| WBTCUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 79828.225 | -0.33 | 0.69 | 0.64 |
| WLDUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.43745 | -0.22 | -0.17 | -3.69 |
| EVAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 43.915 | -0.33 | 0.63 | 0.63 |
| WUSDT | OKX | Erken dönüş | 26.10.2026 23:32 | 0.012345 | 0.62 | 3.53 | 3.22 |
| COMPUSDT | OKX | Erken dönüş | 26.10.2026 23:32 | 21.755 | -1.45 | -2.09 | -1.22 |
| FLUIDUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 23:32 | 2.188 | 1.59 | 0.71 | 0.36 |
| LQTYUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 23:32 | 0.1938 | -0.21 | 2.01 | 2.48 |
| APTMUSDT | MEXC | Erken dönüş | 26.10.2026 23:36 | 0.05199 | 0.08 | 0.33 | -2.27 |
| QUSDT | MEXC | Erken dönüş | 26.10.2026 23:36 | 0.1341405 | -22.83 | -59.84 | -47.22 |
| ARXUSDT | MEXC | Erken dönüş | 26.10.2026 23:36 | 0.22615 | 0.33 | 8.25 | 7.63 |
| COMPUSDT | MEXC | Erken dönüş | 26.10.2026 23:36 | 21.79 | -1.47 | -2.16 | -1.38 |
| SYMMUSDT | MEXC | Yeni kırılım | 26.10.2026 23:36 | 0.0307 | 17.26 | 9.12 | 20.85 |
| VERONAUSDT | MEXC | Yeni kırılım | 26.10.2026 23:36 | 0.13405 | -7.50 | -8.62 | -13.61 |
| JEANPHILUSDT | MEXC | Yeni kırılım | 26.10.2026 23:36 | 0.0045445 | 1.02 | -0.91 | -17.31 |
| FUELUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 23:36 | 0.00079595 | -0.36 | 0.45 | -0.17 |
| TIAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 23:36 | 0.54485 | -3.11 | -0.87 | 2.16 |
| ALEXUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 23:36 | 0.0038645 | 2.86 | 3.51 | 4.62 |
| GRVTUSDT | OKX | Erken dönüş | 27.10.2026 03:39 | 0.213205 | 0.58 | 8.59 | 4.59 |
| BATUSDT | OKX | Erken dönüş | 27.10.2026 03:39 | 0.14842 | 0.35 | -2.02 | -4.53 |
| XAAOIUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 73.69 | -0.12 | 3.88 | 10.42 |
| XAMDUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 537.745 | 0.59 | 4.31 | 5.47 |
| XCOHRUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 225.63 | 1.81 | 4.60 | 9.01 |
| XDRAMUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 49.47 | 0.81 | 3.01 | 8.53 |
| XGEVUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 861.89 | 1.42 | 4.55 | 1.35 |
| XINTWUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 17.675 | 0.54 | 4.89 | 3.65 |
| XMRVLUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 236.485 | 0.62 | 2.88 | -1.38 |
| XMUUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 917.215 | 1.11 | 2.17 | 5.39 |
| XNVDAUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 217.165 | 0.64 | 0.30 | -1.39 |
| XSMHUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 546.985 | 0.83 | 2.13 | 2.70 |
| XSOXLUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 93.21 | 2.25 | 6.93 | 9.12 |
| XTQQQUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 69.35 | 0.65 | 2.54 | 1.31 |
| XARMUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 226.955 | 0.11 | -0.29 | 1.58 |
| XKORUUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 11.52 | 0.87 | 6.16 | 16.32 |
| OPUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 03:39 | 0.112425 | -0.73 | -0.35 | 0.69 |
| ZKUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 03:39 | 0.012207 | 0.51 | -1.14 | -1.48 |
| PVTUSDT | MEXC | Tutunma | 27.10.2026 03:42 | 0.0001008 | 0.10 | 0.79 | 0.99 |
| MASKUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.40145 | -0.83 | 0.29 | -0.69 |
| TUTUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.0175235 | 2.43 | 10.95 | 9.56 |
| USUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.00528 | -6.63 | -3.22 | 2.08 |
| AIAUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.074555 | -3.29 | -5.37 | -3.55 |
| BASECATUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.010385 | 11.89 | 13.05 | 4.96 |
| TELUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.0015175 | 3.13 | 0.03 | -3.46 |
| AINUSDT | MEXC | Yeni kırılım | 27.10.2026 03:42 | 0.07002 | 96.02 | 124.51 | 117.94 |
| SYNUSDT | MEXC | Yeni kırılım | 27.10.2026 03:42 | 0.186635 | -4.69 | -4.17 | -5.28 |
| DVOUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 03:42 | 0.00485085 | -0.05 | 0.83 | -6.58 |
| IMXUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 03:42 | 0.13905 | -0.72 | -0.63 | 1.37 |
| TOWERUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 03:42 | 0.0001345 | -0.22 | -2.53 | -2.08 |
| XSPYUSDT | OKX | Tutunma | 27.10.2026 07:33 | 767.345 | 0.45 | 0.51 | 0.38 |
| ZBCNUSDT | OKX | Erken dönüş | 27.10.2026 07:33 | 0.0022456 | -3.48 | -7.35 | -8.39 |
| IOSTUSDT | OKX | Erken dönüş | 27.10.2026 07:33 | 0.000815 | -4.01 | -2.92 | -5.55 |
| LAYERUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 07:33 | 0.06465 | -1.18 | -0.02 | -2.65 |
| NEXAUSDT | MEXC | Erken dönüş | 27.10.2026 07:37 | 8.605e-07 | -13.33 | -8.30 | -16.99 |
| ANIMEUSDT | MEXC | Erken dönüş | 27.10.2026 07:37 | 0.002841 | 4.93 | 5.21 | -0.60 |
| POKTUSDT | MEXC | Yeni kırılım | 27.10.2026 07:37 | 0.01067 | -19.73 | -25.14 | -30.07 |
| TAKEUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 07:37 | 0.068745 | 8.26 | 4.53 | 1.91 |
| ZORAUSDT | OKX | Erken dönüş | 27.10.2026 11:40 | 0.006372 | 2.32 | 1.49 | -0.63 |
| XSOXSUSDT | OKX | Erken dönüş | 27.10.2026 11:40 | 48.42 | -9.98 | -14.27 | -10.84 |
| AGLDUSDT | OKX | Erken dönüş | 27.10.2026 11:40 | 0.17855 | -2.72 | -0.42 | -2.32 |
| NMRUSDT | OKX | Erken dönüş | 27.10.2026 11:40 | 9.767 | 2.11 | 4.13 | 1.60 |
| DASHUSDT | OKX | Yeni kırılım | 27.10.2026 11:40 | 55.11 | 0.42 | -1.38 | -7.69 |
| XCRWDUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 11:40 | 260.435 | 2.91 | 3.65 | -3.42 |
| ALGOUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 11:40 | 0.103425 | 0.03 | 0.27 | -3.97 |
| ARKMUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 11:40 | 0.11809 | 1.32 | 2.07 | -0.62 |
| AVAUSDT | MEXC | Erken dönüş | 27.10.2026 11:44 | 0.36415 | -2.05 | -6.63 | -12.34 |
| HINTUSDT | MEXC | Erken dönüş | 27.10.2026 11:44 | 0.0008701 | -0.16 | -0.06 | 0.57 |
| TRUTHUSDT | MEXC | Yeni kırılım | 27.10.2026 11:44 | 0.021048 | -0.08 | -0.35 | 10.31 |
| STAMPUSDT | MEXC | Yeni kırılım | 27.10.2026 11:44 | 0.0004802 | -3.37 | 40.21 | 180.80 |
| BCHUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 11:44 | 281.75 | 2.82 | 6.19 | -0.91 |
| TICSUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 11:44 | 0.000672 | 1.04 | 2.68 | 0.15 |
| GAGUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 11:44 | 0.004666 | 0.28 | 0.41 | 0.36 |
| XBOTUSDT | OKX | Tutunma | 27.10.2026 15:42 | 23.87 | 1.68 | 1.55 | -3.06 |
| ASPUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 0.0139275 | -12.91 | -9.97 | -18.43 |
| LSKUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 0.16987 | -1.55 | -1.57 | 0.83 |
| XAMZNUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 251.115 | 1.18 | 0.91 | -0.95 |
| XUSARUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 9.12 | 13.60 | 13.38 | 9.54 |
| XNBISUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 160.385 | 6.91 | 9.44 | 5.81 |
| XAMATUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 396.1 | 0.02 | 1.86 | 3.14 |
| XSMCIUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 33.525 | 4.79 | 5.80 | 4.73 |
| XORCLUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 128.285 | 2.28 | 2.51 | 10.54 |
| XHIMSUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 27.895 | 0.30 | 0.45 | 5.14 |
| SWFTCUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 0.0026045 | 0.13 | 0.67 | 2.09 |
| HUMAUSDT | OKX | Yeni kırılım | 27.10.2026 15:42 | 0.027195 | -5.35 | -1.60 | 9.98 |
| XVRTUSDT | OKX | Yeni kırılım | 27.10.2026 15:42 | 204.805 | 3.10 | 17.72 | 13.91 |
| BASEDUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 15:42 | 0.052675 | -0.52 | 0.14 | 5.36 |
| XSNDKUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 15:42 | 1281.35 | 2.35 | 5.95 | 6.61 |
| VVVUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 25.7316 | 0.32 | -5.55 | -8.67 |
| CASHCATUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 0.098615 | 3.65 | 1.32 | 3.64 |
| CPUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 0.00951 | -3.58 | -6.20 | -9.46 |
| BTWUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 1.467582 | 18.61 | 18.84 | 20.81 |
| XPUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 0.0084105 | 0.61 | -0.80 | -5.84 |
| WARDUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 0.002551 | 18.74 | 5.88 | 36.65 |
| HAEDALUSDT | MEXC | Yeni kırılım | 27.10.2026 15:46 | 0.02476 | 15.63 | 20.15 | 1.58 |
| LUCKYUSDT | MEXC | Yeni kırılım | 27.10.2026 15:46 | 0.001404 | 1.57 | 0.57 | -0.14 |
| HUMAUSDT | MEXC | Yeni kırılım | 27.10.2026 15:46 | 0.02654 | -3.39 | 0.94 | 12.66 |
| XDCUSDT | MEXC | Yeni kırılım | 27.10.2026 15:46 | 0.035375 | -4.42 | -5.07 | -6.06 |
| EDELUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.032405 | 1.62 | 0.35 | -4.03 |
| DEPUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.0010172 | 1.23 | 0.12 | -0.74 |
| HPUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.007858 | -2.35 | -1.71 | -4.58 |
| MYSTUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.077425 | 0.03 | 0.73 | 23.94 |
| ZIGUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.041114 | 2.80 | 3.14 | 2.20 |
| XNAUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 3.0035e-05 | 1.85 | 2.11 | 1.95 |
| ATHUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.0057595 | 2.06 | -0.13 | 2.07 |
| MEGAUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.048015 | 1.91 | 3.84 | -0.39 |
| ROBOUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.005801 | 1.93 | -3.81 | -1.72 |
| XAAPLUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 346.445 | 0.10 | -0.06 | 1.07 |
| XHOODUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 96.365 | -9.30 | -5.81 | -5.06 |
| GRASSUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.7 | 7.53 | -1.04 | -5.49 |
| OMIUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.00027155 | 0.61 | -2.08 | -3.41 |
| AEVOUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.021825 | 2.08 | -0.16 | 2.36 |
| PEPEUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 4.44505e-06 | 9.18 | 8.21 | 19.94 |
| API3USDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.25905 | 0.98 | -0.60 | 0.79 |
| CFGUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.108345 | 0.96 | -4.53 | -1.22 |
| ETHUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 2347.695 | 0.40 | -0.85 | 0.39 |
| FLOWUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.026355 | 0.51 | -1.08 | -1.42 |
| GRTUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.022495 | 1.00 | -0.78 | -0.42 |
| KAIAUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.035265 | 0.24 | -3.96 | -3.59 |
| KITEUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.11818 | -0.15 | -2.48 | -2.91 |
| PAXGUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 4066.2 | -0.49 | -0.52 | -1.05 |
| XCBRSUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 117.69 | 1.54 | -4.37 | 0.66 |
| BRL1USDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.1871 | -0.37 | -0.91 | -1.39 |
| RONUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.054205 | 0.89 | -0.65 | -0.14 |
| ENJUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.025465 | 0.77 | -1.20 | 0.69 |
| MMTUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.14255 | -0.67 | -4.03 | -3.54 |
| OLUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.0059965 | 0.83 | 19.80 | 23.24 |
| PENGUUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.007687 | 1.61 | 0.14 | 3.63 |
| PROVEUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.1902 | 2.58 | 1.68 | 5.21 |
| SSVUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 2.441 | 0.57 | 0.82 | 3.81 |
| BCHUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 290.69 | 2.56 | -0.85 | -0.21 |
| XSNXXUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 9.0805 | 6.99 | 10.75 | 6.36 |
| XTSMUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 437.38 | -0.58 | 0.40 | -0.96 |
| XWDCUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 383.095 | -0.36 | 2.77 | 4.14 |
| ZAMAUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 0.076345 | 0.87 | -1.95 | 0.27 |
| XALABUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 282.735 | 3.11 | 4.66 | 3.09 |
| XASTSUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 43.055 | -2.50 | -4.49 | 3.10 |
| XBEUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 220.655 | 0.46 | 1.90 | 2.72 |
| XMVLLUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 28.665 | 3.65 | 5.74 | -17.74 |
| ADXUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.05405 | 5.27 | 3.24 | 9.34 |
| DYDXUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.108505 | 1.29 | 0.91 | 5.72 |
| GRVTUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.22995 | 3.15 | -3.33 | -2.63 |
| MARSCOINUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.068555 | 2.20 | -3.80 | -2.62 |
| QUBICUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 4.269e-07 | -3.07 | -2.30 | -2.08 |
| STABLEUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.027418 | -1.07 | -0.61 | -1.26 |
| TLMUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.0012034 | 1.52 | 0.57 | 2.62 |
| GRASSUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.7087 | 6.10 | -1.90 | -7.08 |
| QRLUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 1.25273 | -1.31 | -2.89 | -3.33 |
| ROBOUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.005796 | 1.78 | -3.88 | -1.81 |
| SYLUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 5.655e-05 | 0.99 | 0.23 | 1.27 |
| CFGUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.1081 | 0.74 | -4.53 | -1.11 |
| FETUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.18 | 1.17 | -0.61 | 1.39 |
| IOUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.15039 | -0.14 | -0.19 | 0.31 |
| MEGAUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.04792 | 2.13 | 3.94 | -0.38 |
| COCOUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.15527 | -0.61 | -0.88 | -0.26 |
| ETHUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 2344.865 | 0.51 | -0.67 | 0.43 |
| LDOUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.37505 | 0.28 | -1.19 | -0.09 |
| LNQUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.0092495 | 0.44 | 0.17 | 1.11 |
| OGYUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.00126075 | 0.25 | 0.07 | -1.45 |
| ARKMUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.11935 | 1.29 | 0.14 | 1.45 |
| AZTECUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.01779 | -1.18 | -5.28 | -3.04 |
| DYMUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.01788 | 1.06 | -0.39 | -1.06 |
| GMXUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 8.4655 | 4.54 | 4.58 | 0.22 |
| MYXUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.06142 | 1.01 | 0.13 | 1.25 |
| RIFUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.070155 | 0.62 | 1.56 | 1.16 |
| OMIUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.0002718 | 0.07 | -2.17 | -4.01 |
| ZROUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 1.6772 | 2.65 | 0.14 | 4.54 |
| BXEUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.0016745 | 6.78 | 5.82 | 5.05 |
| HANAUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.014226 | 2.43 | 0.62 | 3.94 |
| ACUUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.131585 | 4.77 | -2.86 | -0.25 |
| INXUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.0048755 | 1.94 | -2.12 | -3.19 |
| LABUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.044255 | 8.19 | 3.83 | 9.37 |
| STOPUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.001795 | -0.06 | -0.17 | -3.40 |
| WUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.012784 | 0.68 | -0.71 | -2.32 |
| ELSAUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 19:50 | 0.082515 | -7.22 | -6.50 | -10.86 |
| MINIMAUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 19:50 | 0.003365 | -1.63 | 1.93 | -7.88 |
| BDXUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 19:50 | 0.07534 | -2.65 | -4.87 | -4.43 |
| AUCTIONUSDT | OKX | Erken dönüş | 27.10.2026 23:19 | 3.448 | -0.61 | -1.91 | -2.81 |
| XCRCLUSDT | OKX | Erken dönüş | 27.10.2026 23:19 | 81.33 | 0.23 | -0.48 | -2.39 |
| ALLOUSDT | OKX | Erken dönüş | 27.10.2026 23:19 | 0.189545 | -1.38 | -1.21 | -4.32 |
| HYPEUSDT | OKX | Yeni kırılım | 27.10.2026 23:19 | 81.2245 | 0.15 | -0.03 | 15.36 |
| MAGICUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 23:19 | 0.083805 | -1.66 | 0.85 | -2.94 |
| PNUTUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 23:19 | 0.04106 | 1.83 | 3.21 | 0.61 |
| XMSTRUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 23:19 | 141.745 | 0.74 | 2.62 | -0.84 |
| MEMEROBINHOODUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 0.007507 | 7.54 | 11.44 | -5.29 |
| RSCUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 0.051995 | -1.61 | -3.43 | -9.61 |
| ROSEUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 0.006775 | 0.58 | 0.83 | -2.89 |
| SIUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 0.01224 | 19.36 | 17.40 | 2.61 |
| AOUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 3.7015 | 8.55 | 7.36 | 2.80 |
| MOOUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 0.0018815 | 21.29 | 35.16 | 1.62 |
| AVAXUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 8.88 | 1.46 | 1.01 | -1.41 |
| EVAAUSDT | MEXC | Yeni kırılım | 27.10.2026 23:23 | 0.9027 | 44.10 | 59.78 | 23.76 |
| STONKUSDT | MEXC | Yeni kırılım | 27.10.2026 23:23 | 0.152495 | -3.54 | 0.08 | -5.40 |
| MHAUSDT | MEXC | Yeni kırılım | 27.10.2026 23:23 | 0.0054815 | -8.35 | -12.58 | -23.54 |
| ZENUSDT | MEXC | Yeni kırılım | 27.10.2026 23:23 | 5.9035 | 0.55 | 0.04 | -1.52 |
| XRPUSDT | MEXC | Yeni kırılım | 27.10.2026 23:23 | 1.32305 | 0.62 | 0.43 | -3.86 |
| SPXUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 23:23 | 0.3809 | 1.23 | 3.12 | 1.63 |
| BEAMXUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 23:23 | 0.0033585 | 0.88 | 1.68 | 1.35 |
| VTHOUSDT | MEXC | Erken dönüş | 28.10.2026 03:51 | 0.00058795 | -0.21 | -0.40 | — |
| BDCAUSDT | MEXC | Erken dönüş | 28.10.2026 03:51 | 0.29735 | -0.32 | 1.09 | — |
| NOCKUSDT | MEXC | Erken dönüş | 28.10.2026 03:51 | 0.01803 | -4.94 | -8.82 | — |
| CGPTUSDT | MEXC | Erken dönüş | 28.10.2026 03:51 | 0.01942 | 2.86 | 5.33 | — |
| POLYXUSDT | MEXC | Erken dönüş | 28.10.2026 03:51 | 0.03275 | 0.76 | 1.37 | — |
| COLLECTUSDT | MEXC | Yeni kırılım | 28.10.2026 03:51 | 0.027995 | -13.13 | -12.06 | — |
| TROLLSOLUSDT | MEXC | Yeni kırılım | 28.10.2026 03:51 | 0.031812 | -0.82 | 6.73 | — |
| MORPHOUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 03:51 | 2.1993 | -0.61 | 1.45 | — |
| JASMYUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 03:51 | 0.004308 | -2.18 | -5.20 | — |
| 2U2USDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 03:51 | 0.02145 | -1.21 | -2.00 | — |
| RENDERUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 03:51 | 1.688 | -1.48 | 0.41 | — |
| ICPUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 03:51 | 2.5925 | -0.87 | 1.91 | — |
| KATUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 0.004469 | -3.45 | 2.82 | — |
| ENSUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 5.2915 | -0.54 | -2.37 | — |
| SAHARAUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 0.0080715 | -2.42 | -3.46 | — |
| XBMNRUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 21.85 | -2.79 | -2.15 | — |
| COREUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 0.017685 | -1.05 | -3.87 | — |
| ICPUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 2.6095 | -0.86 | -2.17 | — |
| THETAUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 0.17985 | -1.58 | -4.03 | — |
| XOKTAUSDT | OKX | Yeni kırılım | 28.10.2026 07:43 | 227.7 | -2.24 | -7.57 | — |
| BOMEUSDT | OKX | Yeni kırılım | 28.10.2026 07:43 | 0.0006525 | -3.02 | -3.62 | — |
| FLOKIUSDT | OKX | Yeni kırılım | 28.10.2026 07:43 | 2.3745e-05 | -0.65 | -1.28 | — |
| ASTERUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 07:43 | 0.71505 | -1.70 | -2.29 | — |
| ONUSDT | MEXC | Tutunma | 28.10.2026 07:46 | 0.15155 | 9.48 | 24.22 | — |
| KATUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 0.004475 | -3.75 | 2.30 | — |
| CATIUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 0.043955 | -2.42 | -3.56 | — |
| SHROOMUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 0.003818 | -8.15 | -6.73 | — |
| TRACUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 0.3677 | -0.03 | -1.25 | — |
| AAVEUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 135.555 | -3.07 | -3.91 | — |
| WOLFTONUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 0.000469 | -2.45 | -2.54 | — |
| BONERUSDT | MEXC | Yeni kırılım | 28.10.2026 07:46 | 0.02076 | -9.06 | -14.60 | — |
| MEYUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 07:46 | 0.04875 | -1.25 | -2.63 | — |
| LOTUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 07:46 | 0.005585 | -0.02 | 0.61 | — |
| COREUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 07:46 | 0.01769 | -1.19 | -3.73 | — |
| DCTUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 07:46 | 0.0056285 | -0.44 | 1.04 | — |
| XMUUUSDT | OKX | Tutunma | 28.10.2026 11:50 | 28.97 | -1.31 | -4.45 | — |
| YBUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 11:50 | 0.0646 | 0.70 | -1.78 | — |
| PEAQUSDT | MEXC | Erken dönüş | 28.10.2026 11:54 | 0.03533 | -2.38 | -4.47 | — |
| SWARMUSDT | MEXC | Erken dönüş | 28.10.2026 11:54 | 0.10238 | -9.36 | -9.98 | — |
| CRETAUSDT | MEXC | Erken dönüş | 28.10.2026 11:54 | 0.0019645 | -3.13 | -3.33 | — |
| EMBERUSDT | MEXC | Erken dönüş | 28.10.2026 11:54 | 0.002146 | 3.12 | -5.64 | — |
| TRADOORUSDT | MEXC | Yeni kırılım | 28.10.2026 11:54 | 0.6564 | -2.07 | -7.72 | — |
| XANUSDT | MEXC | Yeni kırılım | 28.10.2026 11:54 | 0.011955 | -4.34 | -18.69 | — |
| SOLVUSDT | MEXC | Yeni kırılım | 28.10.2026 11:54 | 0.005166 | -6.81 | -10.69 | — |
| ZAMAUSDT | MEXC | Yeni kırılım | 28.10.2026 11:54 | 0.078595 | -4.71 | -6.97 | — |
| INDEXUSDT | MEXC | Yeni kırılım | 28.10.2026 11:54 | 0.007055 | 1.20 | -2.62 | — |
| HGPTUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 11:54 | 0.0014783 | -0.70 | -3.04 | — |
| BIOUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 11:54 | 0.02282 | 0.44 | -3.86 | — |
| KSKDUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 11:54 | 0.003413 | -1.03 | 0.64 | — |
| RVNUSDT | OKX | Tutunma | 28.10.2026 15:49 | 0.001468 | 1.70 | -2.32 | — |
| PROSUSDT | OKX | Erken dönüş | 28.10.2026 15:49 | 0.63125 | -1.31 | -1.09 | — |
| SANDUSDT | OKX | Erken dönüş | 28.10.2026 15:49 | 0.048015 | -1.14 | -0.66 | — |
| KSMUSDT | OKX | Erken dönüş | 28.10.2026 15:49 | 3.803 | -1.45 | -1.87 | — |
| LEOUSDT | OKX | Yeni kırılım | 28.10.2026 15:49 | 9.4315 | 0.36 | 0.30 | — |
| BNBUSDT | OKX | Yeni kırılım | 28.10.2026 15:49 | 754.075 | 0.37 | -1.72 | — |
| DOSUSDT | OKX | Yeni kırılım | 28.10.2026 15:49 | 0.3003 | -20.61 | -30.64 | — |
| SHIBUSDT | OKX | Yeni kırılım | 28.10.2026 15:49 | 4.948e-06 | 0.55 | -0.63 | — |
| MEMEUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 15:49 | 0.00047125 | 1.39 | -0.48 | — |
| APTUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 15:49 | 0.68015 | 2.79 | -0.30 | — |
| XTZUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 15:49 | 0.2768 | 2.02 | 0.33 | — |
| AEONUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 15:49 | 0.028605 | -0.82 | 1.98 | — |
| TURBOUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 15:49 | 0.0008186 | 1.33 | -0.22 | — |
| GOMININGUSDT | MEXC | Erken dönüş | 28.10.2026 15:52 | 0.39375 | -1.54 | -4.05 | — |
| KATAUSDT | MEXC | Erken dönüş | 28.10.2026 15:52 | 4.161e-05 | -5.89 | -6.10 | — |
| NAORISUSDT | MEXC | Erken dönüş | 28.10.2026 15:52 | 0.031585 | 14.36 | 3.97 | — |
| BNBUSDT | MEXC | Yeni kırılım | 28.10.2026 15:52 | 755.57 | 0.08 | -1.83 | — |
| DOSUSDT | MEXC | Yeni kırılım | 28.10.2026 15:52 | 0.30077 | -20.56 | -30.47 | — |
| INITUSDT | MEXC | Yeni kırılım | 28.10.2026 15:52 | 0.228635 | -2.63 | -1.99 | — |
| BATONUSDT | MEXC | Yeni kırılım | 28.10.2026 15:52 | 0.006925 | -4.84 | -12.92 | — |
| ATOMUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 15:52 | 1.6275 | 0.95 | 0.03 | — |
| XIBMUSDT | OKX | Erken dönüş | 28.10.2026 19:48 | 252.445 | -0.39 | 0.88 | — |
| XKOUSDT | OKX | Erken dönüş | 28.10.2026 19:48 | 91.895 | 1.21 | 0.55 | — |
| OFCUSDT | OKX | Yeni kırılım | 28.10.2026 19:48 | 0.006812 | -2.97 | -0.03 | — |
| WETUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 19:48 | 0.051765 | -1.13 | 1.15 | — |
| 2ZUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 19:48 | 0.02873 | -3.31 | 0.38 | — |
| CVXUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 19:48 | 2.3495 | -6.58 | -6.28 | — |
| XXIAOMIUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 19:48 | 3.2555 | 0.69 | 0.45 | — |
| CHIRPUSDT | MEXC | Erken dönüş | 28.10.2026 19:52 | 0.006419 | 4.02 | -3.07 | — |
| SIXUSDT | MEXC | Erken dönüş | 28.10.2026 19:52 | 0.00467 | 0.21 | -0.00 | — |
| FLUXUSDT | MEXC | Yeni kırılım | 28.10.2026 19:52 | 0.067745 | -0.14 | 0.60 | — |
| IDOLUSDT | MEXC | Yeni kırılım | 28.10.2026 19:52 | 0.0085295 | 59.36 | 59.24 | — |
| REALTOKENUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 19:52 | 0.0011955 | 2.63 | 6.32 | — |
| BABYUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 19:52 | 0.014568 | -4.23 | -6.92 | — |
| MOCAUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 19:52 | 0.008819 | -3.63 | -1.86 | — |
| GOHOMEUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 19:52 | 75.73 | 0.49 | 0.73 | — |
| ORCAUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 19:52 | 1.6559 | -0.36 | 2.27 | — |
| WETUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 19:52 | 0.051735 | -0.98 | 1.29 | — |
| WIFUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 19:52 | 0.17945 | -0.20 | 2.70 | — |
| GLMRUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 19:52 | 0.0083295 | 0.67 | 3.52 | — |
| APEUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.12455 | -3.95 | -4.87 | — |
| CSPRUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.0022985 | -1.46 | -5.07 | — |
| FLRUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.0061855 | -0.95 | -1.96 | — |
| LINEAUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.0025045 | -2.10 | -3.21 | — |
| ONTUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.04956 | -2.62 | -2.70 | — |
| XCOINUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 160.375 | -1.66 | -0.77 | — |
| GOATUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.014235 | -3.76 | -5.73 | — |
| SKYUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.065665 | -1.90 | -0.40 | — |
| STXUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.30275 | -6.16 | -5.73 | — |
| BABYDOGEUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 3.515e-10 | -2.13 | -5.83 | — |
| CHZUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.01299 | -3.31 | -3.39 | — |
| EIGENUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.1989 | -4.12 | -3.17 | — |
| EDGEUSDT | OKX | Yeni kırılım | 28.10.2026 23:40 | 0.35035 | -2.73 | -4.78 | — |
| TIAUSDT | OKX | Yeni kırılım | 28.10.2026 23:40 | 0.556 | -6.49 | -6.10 | — |
| YGGUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 23:40 | 0.025005 | -3.86 | -5.22 | — |
| SKLUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 23:40 | 0.0040445 | -2.61 | -3.72 | — |
| BOBOUSDT | MEXC | Tutunma | 28.10.2026 23:44 | 0.0052755 | -0.92 | 7.95 | — |
| EACCUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.00063945 | -18.05 | -15.54 | — |
| PLUMEUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.016313 | -6.33 | -10.29 | — |
| KASUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.036535 | -2.88 | -4.80 | — |
| ALGOUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.103775 | -4.34 | -8.93 | — |
| APEUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.12475 | -4.05 | -7.17 | — |
| XMNUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.00063 | -20.63 | -36.51 | — |
| AKEUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.0237875 | -13.01 | -11.89 | — |
| APTUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.70105 | -6.06 | -11.16 | — |
| EDENUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.055615 | -5.24 | -8.33 | — |
| CSPRUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.0023305 | -2.30 | -6.33 | — |
| EIGENUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.1994 | -4.31 | -6.67 | — |
| MOODENGUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.03873 | -4.80 | -7.57 | — |
| ZKUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.0119655 | -3.12 | -7.76 | — |
| FIGHTUSDT | MEXC | Yeni kırılım | 28.10.2026 23:44 | 0.004411 | -11.29 | -14.53 | — |
| AIINUUSDT | MEXC | Yeni kırılım | 28.10.2026 23:44 | 0.0814925 | -12.88 | -22.13 | — |
| XPINUSDT | MEXC | Yeni kırılım | 28.10.2026 23:44 | 0.0010006 | -26.34 | -29.70 | — |
| BBUSDT | MEXC | Yeni kırılım | 28.10.2026 23:44 | 0.007914 | -4.14 | -8.02 | — |
| EDGEUSDT | MEXC | Yeni kırılım | 28.10.2026 23:44 | 0.3503 | -2.94 | -7.42 | — |
| GSTOCKUSDT | MEXC | Yeni kırılım | 28.10.2026 23:44 | 0.0066945 | -3.11 | -12.29 | — |
| BASEDUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 23:44 | 0.053215 | -1.81 | -1.06 | — |
| SCRUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 23:44 | 0.02106 | -2.04 | -5.84 | — |
| VELOUSDT | OKX | Erken dönüş | 29.10.2026 03:49 | 0.0037295 | -1.76 | — | — |
| XLLYUSDT | OKX | Yeni kırılım | 29.10.2026 03:49 | 1309 | 3.09 | — | — |
| IXSUSDT | MEXC | Erken dönüş | 29.10.2026 03:52 | 0.0476 | -2.10 | — | — |
| ALEOUSDT | MEXC | Erken dönüş | 29.10.2026 03:52 | 0.03083 | -6.58 | — | — |
| APEPEUSDT | MEXC | Yeni kırılım | 29.10.2026 03:52 | 1.35115e-06 | 3.31 | — | — |
| SHELLUSDT | MEXC | Yeni kırılım | 29.10.2026 03:52 | 0.028015 | -13.08 | — | — |
| NESUSDT | OKX | Yatay fiyat / hacim artışı | 29.10.2026 07:46 | 0.11425 | 3.28 | — | — |
| NFTUSDT | OKX | Erken dönüş | 29.10.2026 11:52 | 2.366e-07 | — | — | — |
| TBCUSDT | MEXC | Erken dönüş | 29.10.2026 11:55 | 4.5955 | — | — | — |
| QORPOUSDT | MEXC | Erken dönüş | 29.10.2026 11:55 | 0.0022075 | — | — | — |
| NETXUSDT | MEXC | Yeni kırılım | 29.10.2026 11:55 | 0.14715 | — | — | — |
| XKLACUSDT | OKX | Tutunma | 29.10.2026 15:49 | 163.44 | — | — | — |
| XNFLXUSDT | OKX | Erken dönüş | 29.10.2026 15:49 | 62.755 | — | — | — |
| MERLUSDT | OKX | Erken dönüş | 29.10.2026 15:49 | 0.02775 | — | — | — |
| PIUSDT | OKX | Erken dönüş | 29.10.2026 15:49 | 0.078635 | — | — | — |
| SONICUSDT | OKX | Erken dönüş | 29.10.2026 15:49 | 0.022215 | — | — | — |
| MWXTUSDT | MEXC | Erken dönüş | 29.10.2026 15:53 | 0.04041 | — | — | — |
| MERLUSDT | MEXC | Erken dönüş | 29.10.2026 15:53 | 0.027805 | — | — | — |
| TWTUSDT | MEXC | Erken dönüş | 29.10.2026 15:53 | 0.44475 | — | — | — |
| EPICUSDT | MEXC | Erken dönüş | 29.10.2026 15:53 | 0.10485 | — | — | — |
| GRIFFAINUSDT | MEXC | Erken dönüş | 29.10.2026 15:53 | 0.014157 | — | — | — |
| KEKIUSUSDT | MEXC | Erken dönüş | 29.10.2026 15:53 | 0.0050325 | — | — | — |
| TPTUUSDT | MEXC | Yatay fiyat / hacim artışı | 29.10.2026 15:53 | 0.052575 | — | — | — |
| CATIUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 0.04373 | — | — | — |
| CCUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 0.102555 | — | — | — |
| GASUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 1.2238 | — | — | — |
| MEWUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 0.00045765 | — | — | — |
| NEOUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 2.144 | — | — | — |
| REUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 0.37816 | — | — | — |
| WCTUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 0.03652 | — | — | — |
| ZETAUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 0.04049 | — | — | — |
| ZROUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 1.75205 | — | — | — |
| XMETAUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 634.46 | — | — | — |
| AUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 0.091545 | — | — | — |
| MASKUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 0.40115 | — | — | — |
| XGLWUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 131.53 | — | — | — |
| ZRXUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 0.103135 | — | — | — |
| ORDIUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 3.71 | — | — | — |
| GALAUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 0.001797 | — | — | — |
| STRKUSDT | OKX | Erken dönüş | 29.10.2026 19:52 | 0.046825 | — | — | — |
| XONDSUSDT | OKX | Yeni kırılım | 29.10.2026 19:52 | 6.976 | — | — | — |
| EGLDUSDT | OKX | Yeni kırılım | 29.10.2026 19:52 | 3.546 | — | — | — |
| OKBUSDT | OKX | Yeni kırılım | 29.10.2026 19:52 | 113.51 | — | — | — |
| RPLUSDT | OKX | Yeni kırılım | 29.10.2026 19:52 | 1.5275 | — | — | — |
| BARDUSDT | OKX | Yeni kırılım | 29.10.2026 19:52 | 0.11505 | — | — | — |
| ASEUSDT | MEXC | Erken dönüş | 29.10.2026 19:55 | 0.0014 | — | — | — |
| ASTERUSDT | MEXC | Erken dönüş | 29.10.2026 19:55 | 0.71935 | — | — | — |
| NRGUSDT | MEXC | Erken dönüş | 29.10.2026 19:55 | 0.0043865 | — | — | — |
| CCUSDT | MEXC | Erken dönüş | 29.10.2026 19:55 | 0.102515 | — | — | — |
| FLOKIUSDT | MEXC | Erken dönüş | 29.10.2026 19:55 | 2.4365e-05 | — | — | — |
| MEWUSDT | MEXC | Erken dönüş | 29.10.2026 19:55 | 0.00045845 | — | — | — |
| SHXUSDT | MEXC | Erken dönüş | 29.10.2026 19:55 | 0.0051675 | — | — | — |
| ALLOUSDT | MEXC | Erken dönüş | 29.10.2026 19:55 | 0.18731 | — | — | — |
| PENDLEUSDT | MEXC | Erken dönüş | 29.10.2026 19:55 | 1.9975 | — | — | — |
| RESOLVUSDT | MEXC | Erken dönüş | 29.10.2026 19:55 | 0.016615 | — | — | — |
| PNUTUSDT | MEXC | Erken dönüş | 29.10.2026 19:55 | 0.042595 | — | — | — |
| REUSDT | MEXC | Erken dönüş | 29.10.2026 19:55 | 0.37883 | — | — | — |
| DGAIUSDT | MEXC | Erken dönüş | 29.10.2026 19:55 | 0.80395 | — | — | — |
| TAOUSDT | MEXC | Erken dönüş | 29.10.2026 19:55 | 256.545 | — | — | — |
| TIBBIRUSDT | MEXC | Erken dönüş | 29.10.2026 19:55 | 0.22525 | — | — | — |
| FATCOINUSDT | MEXC | Yeni kırılım | 29.10.2026 19:55 | 0.00054375 | — | — | — |
| SN51USDT | MEXC | Yeni kırılım | 29.10.2026 19:55 | 31.985 | — | — | — |
| OKBUSDT | MEXC | Yeni kırılım | 29.10.2026 19:55 | 113.57 | — | — | — |
| LWOLFUSDT | MEXC | Yeni kırılım | 29.10.2026 19:55 | 8.6555e-06 | — | — | — |
| ANVLUSDT | MEXC | Yeni kırılım | 29.10.2026 19:55 | 0.0018371 | — | — | — |
| BOMEUSDT | MEXC | Yeni kırılım | 29.10.2026 19:55 | 0.0006636 | — | — | — |
| CELRUSDT | MEXC | Yeni kırılım | 29.10.2026 19:55 | 0.002545 | — | — | — |
| DTECUSDT | MEXC | Yatay fiyat / hacim artışı | 29.10.2026 19:55 | 0.0033045 | — | — | — |
| MAGICUSDT | MEXC | Yatay fiyat / hacim artışı | 29.10.2026 19:55 | 0.08301 | — | — | — |
| XDKNGUSDT | OKX | Erken dönüş | 29.10.2026 23:42 | 20.535 | — | — | — |
| ATRUSDT | MEXC | Erken dönüş | 29.10.2026 23:45 | 0.0003902 | — | — | — |
| PAIDUSDT | MEXC | Erken dönüş | 29.10.2026 23:45 | 0.0033785 | — | — | — |
| RADUSDT | MEXC | Erken dönüş | 29.10.2026 23:45 | 0.2695 | — | — | — |
| PAYAIUSDT | MEXC | Erken dönüş | 29.10.2026 23:45 | 0.00754 | — | — | — |
| OTKUSDT | MEXC | Erken dönüş | 29.10.2026 23:45 | 0.00198565 | — | — | — |
| AVNTUSDT | MEXC | Erken dönüş | 29.10.2026 23:45 | 0.096585 | — | — | — |
| DUSKUSDT | MEXC | Erken dönüş | 29.10.2026 23:45 | 0.09617 | — | — | — |

### Grupların ayrı ölçümleri

| Grup | Borsa | Süre | Ölçülen / kayıt | Medyan % | BTC üstü puan | Kontrol üstü puan |
|---|---|---:|---:|---:|---:|---:|
| Geri testte tutunma / SAR | MEXC | 12s | 3/4 | -0.37 | -0.43 | 1.21 |
| Geri testte tutunma / SAR | MEXC | 24s | 3/4 | -1.65 | -2.19 | -0.79 |
| Geri testte tutunma / SAR | MEXC | 48s | 1/4 | -1.79 | -2.84 | -2.65 |
| Geri testte tutunma / SAR | OKX | 12s | 6/7 | 4.15 | 3.63 | 4.78 |
| Geri testte tutunma / SAR | OKX | 24s | 6/7 | 3.72 | 3.30 | 4.12 |
| Geri testte tutunma / SAR | OKX | 48s | 3/7 | 6.19 | 5.88 | 6.41 |
| Erken dönüş | MEXC | 12s | 151/189 | -0.33 | -0.46 | -0.59 |
| Erken dönüş | MEXC | 24s | 148/189 | -0.25 | -0.55 | -0.38 |
| Erken dönüş | MEXC | 48s | 109/189 | 0.30 | -0.41 | -0.37 |
| Erken dönüş | OKX | 12s | 164/201 | -0.77 | -0.47 | -0.50 |
| Erken dönüş | OKX | 24s | 162/201 | -0.51 | -0.45 | -0.04 |
| Erken dönüş | OKX | 48s | 125/201 | 0.47 | -0.30 | -0.09 |
| Yatay fiyat / hacim artışı | MEXC | 12s | 110/116 | -0.38 | -0.21 | 0.08 |
| Yatay fiyat / hacim artışı | MEXC | 24s | 109/116 | 0.31 | -0.18 | 0.37 |
| Yatay fiyat / hacim artışı | MEXC | 48s | 73/116 | 0.15 | -0.40 | 0.38 |
| Yatay fiyat / hacim artışı | OKX | 12s | 98/102 | -0.45 | -0.17 | -0.28 |
| Yatay fiyat / hacim artışı | OKX | 24s | 95/102 | 0.39 | -0.21 | -0.15 |
| Yatay fiyat / hacim artışı | OKX | 48s | 68/102 | 0.37 | -0.36 | -0.47 |
| Yeni kırılım | MEXC | 12s | 97/117 | -1.18 | -1.20 | -1.30 |
| Yeni kırılım | MEXC | 24s | 90/117 | -2.34 | -2.20 | -1.81 |
| Yeni kırılım | MEXC | 48s | 55/117 | -1.79 | -2.45 | -1.50 |
| Yeni kırılım | OKX | 12s | 94/111 | 0.44 | 0.03 | -0.11 |
| Yeni kırılım | OKX | 24s | 93/111 | -0.03 | -0.17 | 0.60 |
| Yeni kırılım | OKX | 48s | 62/111 | 2.40 | 1.47 | 1.48 |
| Tutunma | MEXC | 12s | 39/40 | -0.86 | -0.75 | -0.90 |
| Tutunma | MEXC | 24s | 37/40 | -1.65 | -1.61 | -0.84 |
| Tutunma | MEXC | 48s | 16/40 | -1.61 | -2.78 | -2.96 |
| Tutunma | OKX | 12s | 40/42 | -0.54 | -0.37 | -0.18 |
| Tutunma | OKX | 24s | 40/42 | -1.38 | -0.81 | -0.43 |
| Tutunma | OKX | 48s | 7/42 | 2.39 | 2.07 | -0.24 |

## Önceki V4 kayıtları — yeni kayıt alınmıyor

Eski gerçek giriş fiyatları korunur; bunlar yeni grupların geçmişte yakaladığı örnekler değildir. 12/24/48s ölçümleri ayrı sürdürülür.

## Gerçek gözlemden sonraki ölçümler

Her sürüm ve borsanın ilk gerçek alış/satış orta fiyatı ayrı kaydedilir. Aynı coin grup değiştirse de yeni bağımsız örnek sayılmaz. Hedef saatten sonraki ilk dakika kapanışı kullanılır; gecikme 60 saniyeden küçüktür. Ücret/kayma dahil net kâr değildir. Henüz oluşmamış veya eksik ölçümler boş kalır.

8 borsa kaydı, 8 farklı sembol. Ortak semboller iki bağımsız başarı gibi toplanmaz.

| Borsa | Süre | Ölçülen | Medyan % | BTC üstü puan | Kontrol üstü puan | Kontrol ölçülen |
|---|---:|---:|---:|---:|---:|---:|
| MEXC | 12s | 8/8 | -2.13 | -1.79 | -2.12 | 8 |
| MEXC | 24s | 8/8 | -2.41 | -1.82 | -2.00 | 8 |
| MEXC | 48s | 8/8 | -7.07 | -7.96 | -11.51 | 8 |

| Coin | Borsa | İlk grup | Gerçek gözlem TR | Referans fiyat | 12s % | 24s % | 48s % |
|---|---|---|---|---:|---:|---:|---:|
| BULLAUSDT | MEXC | Yeni kırılım | 26.10.2026 11:48 | 0.1130635 | 35.79 | 4.11 | -35.56 |
| CAPUSDT | MEXC | Tutunma | 26.10.2026 00:23 | 0.10956 | -21.28 | -9.24 | -9.21 |
| CPHUSDT | MEXC | Tutunma | 26.10.2026 11:48 | 0.0035595 | -3.05 | -3.55 | -15.58 |
| GBCKUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.0048565 | -0.59 | -1.27 | -0.96 |
| MIUUSDT | MEXC | Yeni kırılım | 26.10.2026 03:52 | 8.85e-10 | 5.08 | 3.95 | 1.69 |
| NEXUSDT | MEXC | Yeni kırılım | 26.10.2026 11:48 | 7.95e-07 | -10.87 | -9.67 | -4.93 |
| STONKSUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.0020883 | -19.28 | -24.35 | -53.64 |
| TAUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.06203 | -1.21 | -0.18 | 1.63 |

Karşılaştırma için en az 1–2 haftalık gerçek kayıt beklenir. Gruplar, borsalar ve ortak coinler dikkate alınmadan bir kazanma oranı iddia edilmez.


<!-- coin-priority-raw:end -->

</details>
