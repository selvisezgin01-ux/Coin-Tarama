# Coin Tarama 3 — kısa öncelik listesi

Son kontrol: 28.10.2026 23:45 TR.

Geniş havuz: 120 borsa kaydı / 105 sembol. İşlem koşulu elemesini geçen: 18 farklı sembol. Bildirim ve üst liste: en fazla 5 farklı coin.

**Öncelik, kârlılık veya güvenli işlem garantisi değildir.** Hacim/makas, güncel fiyat, yapı ve uzama kontrollerinden geçenler sıralanır. Yalnız yatay hacim hazırlığı bildirilmez. Aday yoksa liste doldurulmaz.

| Coin | Fiyat borsası | Geçen borsalar | Grup | Gerçek gözlem TR | Fiyat | Makas % | Yapı mesafesi % |
|---|---|---|---|---|---:|---:|---:|
| CSPRUSDT | OKX | OKX | Erken dönüş | 28.10.2026 23:45 | 0.0023005 | 0.04 | 11.75 |
| EDGEUSDT | OKX | MEXC, OKX | Yeni kırılım | 28.10.2026 23:45 | 0.34995 | 0.14 | 7.07 |
| FLRUSDT | OKX | OKX | Erken dönüş | 28.10.2026 23:45 | 0.006184 | 0.10 | 2.26 |
| XLMUSDT | OKX | MEXC, OKX | Erken dönüş | 28.10.2026 23:45 | 0.17297 | 0.01 | 2.41 |
| PUMPUSDT | OKX | MEXC, OKX | Erken dönüş, Yeni kırılım | 28.10.2026 23:45 | 0.0044795 | 0.07 | 7.99 |

Sıralama: en çok 4x sayılan göreli hacim, kapanış konumu, dar makas ve aynı borsanın hacmi. Farklı borsaların hacimleri toplanmaz. Bu sıra başarı olasılığı değildir.

Başlangıç elemesi: en az 100.000 USDT kapalı 24s hacim, en çok %0,5 makas, izlenen seviyeyi koruyan güncel fiyat, kapanıştan en çok 1 ATR uzaklık, EMA20 üstüne en çok 2,5 ATR uzama ve yapı referansına en çok %12 mesafe. 20x üzeri hacim ayrıca incelemede kalır. Bunlar daha iyi sonuç verdiği kanıtlanmış yeni strateji eşikleri değildir.

Aynı sembol tek satırda gösterilir; yalnız elemeden geçen borsalar listelenir. Sembol eşleşmesi bağımsız kontrat kimliği teyidi değildir. Geniş havuz ve eski ölçümler korunur. [Tanınan OKX hisse tokenlerinin kaynağı](https://www.okx.com/help/okx-to-list-tokenized-stocks-for-trading). Liste 2026-10-26 tarihinde kontrol edildi; yeni hisse tokenlerinin eklenmesi gerekebilir.

## Eleme özeti

- 12 borsa kaydı: EMA20 uzaklığı fazla veya bilinmiyor
- 4 borsa kaydı: olağandışı hacim katsayısı; ayrıca inceleme
- 19 borsa kaydı: tanınan tokenleştirilmiş hisse
- 8 borsa kaydı: yalnız hazırlık; ek teknik teyit yok
- 23 borsa kaydı: güncel fiyat kapanıştan uzak veya veri eksik
- 16 borsa kaydı: yapı bozulma mesafesi geniş veya bilinmiyor
- 7 borsa kaydı: makas geniş veya bilinmiyor
- 57 borsa kaydı: izlenen seviye kaybedilmiş veya bilinmiyor
- 38 borsa kaydı: hacim 100.000 USDT altında

Bir kayıtta birden fazla neden olabilir; sayılar bağımsız coinler gibi toplanmaz.
Sıralama sınırı dışında kalan uygun sembol: 13.


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
| XKORUUSDT | OKX | 27.10.2026 03:44 | 11.475 | 0.83 | 7.36 | — |
| QNTUSDT | MEXC | 27.10.2026 03:44 | 203.095 | -0.44 | -1.62 | — |
| CLANKERUSDT | MEXC | 27.10.2026 03:44 | 13.645 | -0.77 | 1.65 | — |
| TELUSDT | MEXC | 27.10.2026 03:44 | 0.0015175 | 3.00 | 0.03 | — |
| IOSTUSDT | OKX | 27.10.2026 07:38 | 0.0008208 | -4.25 | -3.61 | — |
| ZBCNUSDT | OKX | 27.10.2026 07:38 | 0.00222315 | -2.38 | -5.71 | — |
| XSOXSUSDT | OKX | 27.10.2026 11:46 | 48.635 | -10.02 | -14.32 | — |
| ZORAUSDT | OKX | 27.10.2026 11:46 | 0.006395 | 2.31 | 1.13 | — |
| DASHUSDT | OKX | 27.10.2026 11:46 | 54.99 | 0.64 | -1.45 | — |
| TRUTHUSDT | MEXC | 27.10.2026 11:46 | 0.0210175 | 0.19 | -0.18 | — |
| AVAUSDT | MEXC | 27.10.2026 11:46 | 0.36365 | -1.86 | -6.31 | — |
| LSKUSDT | OKX | 27.10.2026 15:48 | 0.169625 | -1.21 | -1.77 | — |
| CASHCATUSDT | MEXC | 27.10.2026 15:48 | 0.09844 | 4.07 | 0.71 | — |
| XDCUSDT | MEXC | 27.10.2026 15:48 | 0.03539 | -4.61 | -5.23 | — |
| VVVUSDT | MEXC | 27.10.2026 15:48 | 25.6305 | 0.71 | -5.71 | — |
| CFGUSDT | OKX | 27.10.2026 19:53 | 0.10832 | 0.64 | -4.62 | — |
| STETHUSDT | OKX | 27.10.2026 19:53 | 2344.565 | 0.46 | -0.50 | — |
| IOUSDT | MEXC | 27.10.2026 19:53 | 0.15046 | -0.49 | -0.11 | — |
| PENGUUSDT | MEXC | 27.10.2026 19:53 | 0.007689 | 1.56 | 0.10 | — |
| HYPEUSDT | OKX | 27.10.2026 23:23 | 81.2315 | 0.10 | -0.23 | — |
| ROSEUSDT | MEXC | 27.10.2026 23:23 | 0.006775 | 0.58 | 0.83 | — |
| LYNUSDT | MEXC | 27.10.2026 23:23 | 0.01493 | 1.21 | 5.29 | — |
| ZENUSDT | MEXC | 27.10.2026 23:23 | 5.911 | 0.42 | -0.08 | — |
| NIGHTUSDT | OKX | 28.10.2026 03:54 | 0.0419635 | -4.32 | — | — |
| XSNXXUSDT | OKX | 28.10.2026 03:54 | 9.3325 | 3.72 | — | — |
| SAHARAUSDT | OKX | 28.10.2026 07:47 | 0.0080505 | -2.48 | — | — |
| ENSUSDT | OKX | 28.10.2026 07:47 | 5.283 | -0.74 | — | — |
| BCHUSDT | OKX | 28.10.2026 07:47 | 298.04 | -3.29 | — | — |
| ZAMAUSDT | OKX | 28.10.2026 11:56 | 0.078535 | — | — | — |
| MEGAUSDT | OKX | 28.10.2026 11:56 | 0.049225 | — | — | — |
| 4USDT | MEXC | 28.10.2026 11:56 | 0.012575 | — | — | — |
| PEAQUSDT | MEXC | 28.10.2026 11:56 | 0.03526 | — | — | — |
| RVNUSDT | OKX | 28.10.2026 15:55 | 0.0014715 | — | — | — |
| PROSUSDT | OKX | 28.10.2026 15:55 | 0.631 | — | — | — |
| HANAUSDT | MEXC | 28.10.2026 15:55 | 0.0146155 | — | — | — |
| GOMININGUSDT | MEXC | 28.10.2026 15:55 | 0.3936 | — | — | — |
| BICOUSDT | OKX | 28.10.2026 19:55 | 0.015915 | — | — | — |
| XPLUSDT | OKX | 28.10.2026 19:55 | 0.076615 | — | — | — |
| CSPRUSDT | OKX | 28.10.2026 23:45 | 0.0023005 | — | — | — |
| EDGEUSDT | OKX | 28.10.2026 23:45 | 0.34995 | — | — | — |
| FLRUSDT | OKX | 28.10.2026 23:45 | 0.006184 | — | — | — |
| XLMUSDT | OKX | 28.10.2026 23:45 | 0.17297 | — | — | — |
| PUMPUSDT | OKX | 28.10.2026 23:45 | 0.0044795 | — | — | — |

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

MEXC: incelenen 1046, aday 40; kapanış 28.10.2026 23:00 TR; fiyat gözlemi 28.10.2026 23:44 TR.
V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |
|---|---|---:|---:|---|---|
| BOBOUSDT | Tutunma | 10.65 | 2.94 | Yok | yapı bozulma mesafesi geniş; düşük hacim; makas geniş |
| ONUSDT | Tutunma | 10.22 | 3.90 | RSI PU teyitli | yapı bozulma mesafesi geniş; makas geniş |
| BONERUSDT | Tutunma | 11.03 | 1.71 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim |
| PONSUSDT | Tutunma | 14.05 | 2.03 | Yok | yapı bozulma mesafesi geniş |
| INDEXUSDT | Tutunma | 35.67 | 2.02 | Yok | 24 saatlik yükseliş yüksek; yapı bozulma mesafesi geniş; makas geniş |
| EMBERUSDT | Tutunma | 20.73 | 2.67 | Yok | yapı bozulma mesafesi geniş; düşük hacim; makas geniş |
| SHROOMUSDT | Tutunma | 30.14 | 1.72 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; yapı bozulma mesafesi geniş; düşük hacim; makas geniş |
| EACCUSDT | Erken dönüş | 50.67 | 2.00 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| PLUMEUSDT | Erken dönüş, Yeni kırılım | 4.21 | 2.35 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| KASUSDT | Erken dönüş, Yeni kırılım | 3.50 | 1.80 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ALGOUSDT | Erken dönüş | 0.60 | 4.15 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| APEUSDT | Erken dönüş | 3.34 | 2.25 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| FILUSDT | Erken dönüş | 2.27 | 3.09 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| PUMPUSDT | Erken dönüş, Yeni kırılım | 5.41 | 2.34 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| RENDERUSDT | Erken dönüş | 1.35 | 2.89 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| XLMUSDT | Erken dönüş | 1.88 | 2.26 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XMNUSDT | Erken dönüş | 100.00 | 34.95 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| AKEUSDT | Erken dönüş | 3.30 | 4.31 | Yok | yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| APTUSDT | Erken dönüş | 3.41 | 2.39 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| EDENUSDT | Erken dönüş | 0.52 | 2.54 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ARBUSDT | Erken dönüş, Yeni kırılım | 3.92 | 1.89 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| CSPRUSDT | Erken dönüş | 12.18 | 1.85 | Yok | yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| EIGENUSDT | Erken dönüş | 2.12 | 1.56 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| ICPUSDT | Erken dönüş | 2.89 | 1.97 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| SUIUSDT | Erken dönüş | 2.62 | 1.54 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| MOODENGUSDT | Erken dönüş | 1.27 | 1.56 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| ZKUSDT | Erken dönüş | 0.65 | 1.63 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| FIGHTUSDT | Yeni kırılım | 15.33 | 2.53 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş |
| MEGAUSDT | Yeni kırılım | 6.49 | 1.53 | Yok | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| AIINUUSDT | Yeni kırılım | 25.06 | 2.55 | RSI PU teyitli | yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş |
| XPINUSDT | Yeni kırılım | 28.88 | 3.99 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı kapanıştan uzaklaştı |
| BBUSDT | Yeni kırılım | 5.17 | 1.59 | Yok | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| EDGEUSDT | Yeni kırılım | 4.98 | 1.97 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| FLUXUSDT | Yeni kırılım | 5.18 | 1.78 | Yok | düşük hacim |
| GSTOCKUSDT | Yeni kırılım | 39.48 | 1.58 | RSI PU teyitli | 24 saatlik yükseliş yüksek; yapı bozulma mesafesi geniş; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| TIAUSDT | Yeni kırılım | 2.83 | 2.83 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| TRUTHUSDT | Yatay fiyat / hacim artışı | 1.56 | 2.11 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| BASEDUSDT | Yatay fiyat / hacim artışı | 2.65 | 1.57 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| IOUSDT | Yatay fiyat / hacim artışı | 3.58 | 1.86 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| SCRUSDT | Yatay fiyat / hacim artışı | 1.44 | 1.86 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |

OKX: incelenen 348, aday 80; kapanış 28.10.2026 23:00 TR; fiyat gözlemi 28.10.2026 23:40 TR.
V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |
|---|---|---:|---:|---|---|
| MEGAUSDT | Tutunma | 6.60 | 2.43 | Yok | Ek eşik uyarısı yok |
| XALABUSDT | Tutunma | 4.15 | 7.24 | Yok | ortalamadan uzak; düşük hacim; gözlem fiyatı kapanıştan uzaklaştı |
| XBEUSDT | Tutunma | 4.25 | 3.80 | Yok | gözlem fiyatı kapanıştan uzaklaştı |
| XDRAMUSDT | Tutunma | 6.99 | 3.98 | Yok | ortalamadan uzak; düşük hacim; makas geniş; gözlem fiyatı kapanıştan uzaklaştı |
| LEOUSDT | Tutunma | 4.24 | 97.35 | Yok | ortalamadan uzak; düşük hacim |
| PONSUSDT | Tutunma | 13.83 | 2.24 | Yok | yapı bozulma mesafesi geniş |
| XPLUSDT | Tutunma | 5.59 | 2.52 | Yok | Ek eşik uyarısı yok |
| AAVEUSDT | Erken dönüş | 3.57 | 3.40 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| ALLOUSDT | Erken dönüş | 0.79 | 2.29 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| APEUSDT | Erken dönüş | 3.38 | 2.14 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| CRVUSDT | Erken dönüş | 0.91 | 2.67 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| CSPRUSDT | Erken dönüş | 12.15 | 6.01 | Yok | yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| FLRUSDT | Erken dönüş | 1.75 | 3.85 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| JUPUSDT | Erken dönüş | 3.03 | 2.44 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| LINEAUSDT | Erken dönüş | 1.65 | 2.71 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| MANAUSDT | Erken dönüş | 3.43 | 3.33 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| ONTUSDT | Erken dönüş | 2.15 | 2.35 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| PENDLEUSDT | Erken dönüş | 0.80 | 2.43 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| PUMPUSDT | Erken dönüş, Yeni kırılım | 5.34 | 3.36 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| RENDERUSDT | Erken dönüş | 1.41 | 2.10 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| SEIUSDT | Erken dönüş | 2.06 | 2.06 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| SUIUSDT | Erken dönüş | 2.64 | 2.90 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| TAOUSDT | Erken dönüş | 2.38 | 4.79 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| TURBOUSDT | Erken dönüş | 2.14 | 5.75 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| UMAUSDT | Erken dönüş | 1.45 | 5.60 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| XCOINUSDT | Erken dönüş | 0.61 | 2.89 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| XLMUSDT | Erken dönüş | 1.95 | 3.56 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| XTZUSDT | Erken dönüş | 1.14 | 3.83 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| GOATUSDT | Erken dönüş | 1.56 | 9.27 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| LQTYUSDT | Erken dönüş | 0.91 | 6.17 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| SKYUSDT | Erken dönüş | 2.72 | 2.02 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| STXUSDT | Erken dönüş | 1.25 | 2.11 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| TRBUSDT | Erken dönüş | 0.69 | 2.85 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| XMSTRUSDT | Erken dönüş | 2.56 | 2.50 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| ALGOUSDT | Erken dönüş | 0.67 | 1.80 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| ARBUSDT | Erken dönüş, Yeni kırılım | 3.84 | 1.87 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| BABYDOGEUSDT | Erken dönüş, Yeni kırılım | 2.30 | 2.53 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| BIOUSDT | Erken dönüş | 1.94 | 1.84 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| CHZUSDT | Erken dönüş | 1.08 | 1.88 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| GRTUSDT | Erken dönüş | 0.93 | 1.77 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| HMSTRUSDT | Erken dönüş | 1.97 | 1.93 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| IMXUSDT | Erken dönüş | 2.53 | 1.66 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| OPUSDT | Erken dönüş | 3.00 | 1.76 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| SNXUSDT | Erken dönüş | 1.80 | 1.84 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| APTUSDT | Erken dönüş | 3.41 | 1.76 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| EIGENUSDT | Erken dönüş | 2.07 | 1.55 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| JTOUSDT | Erken dönüş | 0.85 | 1.97 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| MONUSDT | Erken dönüş | 2.09 | 1.65 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| XAAOIUSDT | Yeni kırılım | 7.12 | 3.94 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| XAMDUSDT | Yeni kırılım | 3.27 | 2.21 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| XARMUSDT | Yeni kırılım | 3.84 | 2.52 | Yok | ortalamadan uzak; düşük hacim; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| XAVGOUSDT | Yeni kırılım | 2.74 | 3.91 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| XEWYUSDT | Yeni kırılım | 5.38 | 5.69 | Yok | ortalamadan uzak; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| XKORUUSDT | Yeni kırılım | 16.62 | 2.76 | Yok | ortalamadan uzak; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| XLITEUSDT | Yeni kırılım | 5.48 | 3.68 | Yok | ortalamadan uzak; gözlem fiyatı kapanıştan uzaklaştı |
| XMUUSDT | Yeni kırılım | 5.83 | 2.75 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| XMUUUSDT | Yeni kırılım | 10.52 | 10.97 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| XNBISUSDT | Yeni kırılım | 7.18 | 5.06 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| XSNXXUSDT | Yeni kırılım | 14.68 | 3.61 | Yok | ortalamadan uzak; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| XSOXLUSDT | Yeni kırılım | 6.23 | 3.92 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| XVRTUSDT | Yeni kırılım | 16.51 | 299.35 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş; gözlem fiyatı kapanıştan uzaklaştı |
| XSNDKUSDT | Yeni kırılım | 7.53 | 1.58 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| BICOUSDT | Yeni kırılım | 7.75 | 4.85 | Yok | ortalamadan uzak |
| EDGEUSDT | Yeni kırılım | 4.86 | 3.90 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XCRWVUSDT | Yeni kırılım | 7.44 | 2.18 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| XIRENUSDT | Yeni kırılım | 4.87 | 4.54 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| XORCLUSDT | Yeni kırılım | 10.60 | 40.59 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı kapanıştan uzaklaştı |
| SSVUSDT | Yeni kırılım | 3.14 | 1.71 | Yok | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| TRUMPUSDT | Yeni kırılım | 2.95 | 1.96 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| WETUSDT | Yeni kırılım | 4.13 | 1.89 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| PENGUUSDT | Yeni kırılım | 2.43 | 1.53 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| PNUTUSDT | Yeni kırılım | 3.31 | 1.79 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| TIAUSDT | Yeni kırılım | 2.85 | 1.69 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| BASEDUSDT | Yatay fiyat / hacim artışı | 2.58 | 2.09 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XMVLLUSDT | Yatay fiyat / hacim artışı, Yeni kırılım | 6.30 | 9.60 | Yok | ortalamadan uzak; düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| XMRVLUSDT | Yatay fiyat / hacim artışı, Yeni kırılım | 3.34 | 1.67 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| DYDXUSDT | Yatay fiyat / hacim artışı | 1.78 | 2.46 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| NOTUSDT | Yatay fiyat / hacim artışı, Yeni kırılım | 3.01 | 1.52 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| YGGUSDT | Yatay fiyat / hacim artışı | 3.49 | 2.80 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| SKLUSDT | Yatay fiyat / hacim artışı | 1.29 | 1.62 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |

İki borsada toplam 105 farklı sembol. Ortak semboller bağımsız iki başarı sayılmaz.

Eşikler başlangıç deneyidir; daha çok aday daha yüksek başarı demek değildir. Yazılım testleri kârlılık kanıtı değildir. Dört saatlik mum ve zamanlayıcı gecikmesi ilk hareketin kaçmasına yol açabilir. SAR yön desteğidir; getiri garantisi değildir.

## Bu döngüde yeni gelenler

AAVEUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 134.9
24s %3.57; ilgili hacim 3.4026x; makas %0.02
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

APEUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.12455
24s %3.38; ilgili hacim 2.1392x; makas %0.02
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

CRVUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.339
24s %0.91; ilgili hacim 2.6667x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; teyitli RSI pozitif uyumsuzluk desteği

CSPRUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.0022985
24s %12.15; ilgili hacim 6.01x; makas %0.04
yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

FLRUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.0061855
24s %1.75; ilgili hacim 3.845x; makas %0.08
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

JUPUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.28395
24s %3.03; ilgili hacim 2.4391x; makas %0.11
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

LINEAUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.0025045
24s %1.65; ilgili hacim 2.7134x; makas %0.12
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

MANAUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.079495
24s %3.43; ilgili hacim 3.3252x; makas %0.09
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

ONTUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.04956
24s %2.15; ilgili hacim 2.3526x; makas %0.16
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

PENDLEUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 1.983
24s %0.80; ilgili hacim 2.4298x; makas %0.10
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

PUMPUSDT · OKX
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 28.10.2026 23:40 TR; fiyat 0.004462
24s %5.34; ilgili hacim 3.3585x; makas %0.04
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

RENDERUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 1.696
24s %1.41; ilgili hacim 2.0964x; makas %0.12
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

SEIUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.053465
24s %2.06; ilgili hacim 2.0634x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

SUIUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.94025
24s %2.64; ilgili hacim 2.9021x; makas %0.01
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

TAOUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 257.25
24s %2.38; ilgili hacim 4.7938x; makas %0.02
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

UMAUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.35415
24s %1.45; ilgili hacim 5.6001x; makas %0.08
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

XCOINUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 160.38
24s %0.61; ilgili hacim 2.8885x; makas %0.03
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

XLMUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.17245
24s %1.95; ilgili hacim 3.5648x; makas %0.02
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

GOATUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.014235
24s %1.56; ilgili hacim 9.2735x; makas %0.21
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

LQTYUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.19785
24s %0.91; ilgili hacim 6.1698x; makas %0.25
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

SKYUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.065665
24s %2.72; ilgili hacim 2.0241x; makas %0.05
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; teyitli RSI pozitif uyumsuzluk desteği

STXUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.30275
24s %1.25; ilgili hacim 2.1071x; makas %0.10
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

TRBUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 17.33
24s %0.69; ilgili hacim 2.8457x; makas %0.12
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

ARBUSDT · OKX
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 28.10.2026 23:40 TR; fiyat 0.17392
24s %3.84; ilgili hacim 1.8683x; makas %0.02
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

BABYDOGEUSDT · OKX
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 28.10.2026 23:40 TR; fiyat 3.515e-10
24s %2.30; ilgili hacim 2.5304x; makas %0.28
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

BIOUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.022805
24s %1.94; ilgili hacim 1.8418x; makas %0.13
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

CHZUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.01299
24s %1.08; ilgili hacim 1.88x; makas %0.15
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

HMSTRUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.0001436
24s %1.97; ilgili hacim 1.9338x; makas %0.14
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

IMXUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.14
24s %2.53; ilgili hacim 1.6586x; makas %0.14
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

SNXUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.20135
24s %1.80; ilgili hacim 1.8428x; makas %0.15
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

EIGENUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.1989
24s %2.07; ilgili hacim 1.551x; makas %0.10
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

JTOUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.4289
24s %0.85; ilgili hacim 1.9688x; makas %0.05
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

MONUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:40 TR; fiyat 0.02147
24s %2.09; ilgili hacim 1.6471x; makas %0.09
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

XAVGOUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 28.10.2026 23:40 TR; fiyat 343.1
24s %2.74; ilgili hacim 3.9098x; makas %0.02
ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı

XLITEUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 28.10.2026 23:40 TR; fiyat 888.28
24s %5.48; ilgili hacim 3.6752x; makas %0.05
ortalamadan uzak; gözlem fiyatı kapanıştan uzaklaştı

EDGEUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 28.10.2026 23:40 TR; fiyat 0.35035
24s %4.86; ilgili hacim 3.8985x; makas %0.14
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

XCRWVUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 28.10.2026 23:40 TR; fiyat 61.35
24s %7.44; ilgili hacim 2.1774x; makas %0.13
ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı

XIRENUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 28.10.2026 23:40 TR; fiyat 27.815
24s %4.87; ilgili hacim 4.5376x; makas %0.11
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı

TRUMPUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 28.10.2026 23:40 TR; fiyat 1.7235
24s %2.95; ilgili hacim 1.9648x; makas %0.06
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında

TIAUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 28.10.2026 23:40 TR; fiyat 0.556
24s %2.85; ilgili hacim 1.6905x; makas %0.04
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

NOTUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı, Yeni kırılım
Gözlem 28.10.2026 23:40 TR; fiyat 0.0003873
24s %3.01; ilgili hacim 1.516x; makas %0.15
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

YGGUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 28.10.2026 23:40 TR; fiyat 0.025005
24s %3.49; ilgili hacim 2.8016x; makas %0.20
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

SKLUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 28.10.2026 23:40 TR; fiyat 0.0040445
24s %1.29; ilgili hacim 1.6175x; makas %0.22
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

BOBOUSDT · MEXC
Gruplar: Tutunma
Gözlem 28.10.2026 23:44 TR; fiyat 0.0052755
24s %10.65; ilgili hacim 2.9405x; makas %3.17
yapı bozulma mesafesi geniş; düşük hacim; makas geniş

EACCUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:44 TR; fiyat 0.00063945
24s %50.67; ilgili hacim 2.0027x; makas %1.74
24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

PLUMEUSDT · MEXC
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 28.10.2026 23:44 TR; fiyat 0.016313
24s %4.21; ilgili hacim 2.349x; makas %0.09
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

KASUSDT · MEXC
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 28.10.2026 23:44 TR; fiyat 0.036535
24s %3.50; ilgili hacim 1.8016x; makas %0.19
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ALGOUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:44 TR; fiyat 0.10378
24s %0.60; ilgili hacim 4.1527x; makas %0.07
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

APEUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:44 TR; fiyat 0.12475
24s %3.34; ilgili hacim 2.2456x; makas %0.08
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

FILUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:44 TR; fiyat 0.91405
24s %2.27; ilgili hacim 3.0899x; makas %0.01
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

PUMPUSDT · MEXC
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 28.10.2026 23:44 TR; fiyat 0.004463
24s %5.41; ilgili hacim 2.342x; makas %0.04
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XLMUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:44 TR; fiyat 0.17265
24s %1.88; ilgili hacim 2.2628x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XMNUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:44 TR; fiyat 0.00063
24s %100.00; ilgili hacim 34.95x; makas %3.17
24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

AKEUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:44 TR; fiyat 0.023787
24s %3.30; ilgili hacim 4.3097x; makas %0.24
yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

APTUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:44 TR; fiyat 0.70105
24s %3.41; ilgili hacim 2.3875x; makas %0.13
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

EDENUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:44 TR; fiyat 0.055615
24s %0.52; ilgili hacim 2.5449x; makas %0.09
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ARBUSDT · MEXC
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 28.10.2026 23:44 TR; fiyat 0.174
24s %3.92; ilgili hacim 1.8863x; makas %0.13
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

CSPRUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:44 TR; fiyat 0.0023305
24s %12.18; ilgili hacim 1.8489x; makas %0.13
yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

EIGENUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:44 TR; fiyat 0.1994
24s %2.12; ilgili hacim 1.5602x; makas %0.10
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

SUIUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:44 TR; fiyat 0.94195
24s %2.62; ilgili hacim 1.5425x; makas %0.01
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

MOODENGUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:44 TR; fiyat 0.03873
24s %1.27; ilgili hacim 1.5629x; makas %0.10
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

ZKUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 23:44 TR; fiyat 0.011966
24s %0.65; ilgili hacim 1.6262x; makas %0.09
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

FIGHTUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 28.10.2026 23:44 TR; fiyat 0.004411
24s %15.33; ilgili hacim 2.5313x; makas %0.27
ortalamadan uzak; yapı bozulma mesafesi geniş

AIINUUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 28.10.2026 23:44 TR; fiyat 0.081492
24s %25.06; ilgili hacim 2.552x; makas %1.23
yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş; teyitli RSI pozitif uyumsuzluk desteği

XPINUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 28.10.2026 23:44 TR; fiyat 0.0010006
24s %28.88; ilgili hacim 3.9874x; makas %0.32
ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı kapanıştan uzaklaştı

BBUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 28.10.2026 23:44 TR; fiyat 0.007914
24s %5.17; ilgili hacim 1.5913x; makas %0.15
düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

EDGEUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 28.10.2026 23:44 TR; fiyat 0.3503
24s %4.98; ilgili hacim 1.9748x; makas %0.17
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

GSTOCKUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 28.10.2026 23:44 TR; fiyat 0.0066945
24s %39.48; ilgili hacim 1.5817x; makas %0.31
24 saatlik yükseliş yüksek; yapı bozulma mesafesi geniş; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; teyitli RSI pozitif uyumsuzluk desteği

BASEDUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 28.10.2026 23:44 TR; fiyat 0.053215
24s %2.65; ilgili hacim 1.5699x; makas %0.17
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

SCRUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 28.10.2026 23:44 TR; fiyat 0.02106
24s %1.44; ilgili hacim 1.8594x; makas %0.09
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

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
| GRVTUSDT | OKX | Erken dönüş | 27.10.2026 03:39 | 0.213205 | 0.58 | 8.59 | — |
| BATUSDT | OKX | Erken dönüş | 27.10.2026 03:39 | 0.14842 | 0.35 | -2.02 | — |
| XAAOIUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 73.69 | -0.12 | 3.88 | — |
| XAMDUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 537.745 | 0.59 | 4.31 | — |
| XCOHRUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 225.63 | 1.81 | 4.60 | — |
| XDRAMUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 49.47 | 0.81 | 3.01 | — |
| XGEVUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 861.89 | 1.42 | 4.55 | — |
| XINTWUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 17.675 | 0.54 | 4.89 | — |
| XMRVLUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 236.485 | 0.62 | 2.88 | — |
| XMUUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 917.215 | 1.11 | 2.17 | — |
| XNVDAUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 217.165 | 0.64 | 0.30 | — |
| XSMHUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 546.985 | 0.83 | 2.13 | — |
| XSOXLUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 93.21 | 2.25 | 6.93 | — |
| XTQQQUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 69.35 | 0.65 | 2.54 | — |
| XARMUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 226.955 | 0.11 | -0.29 | — |
| XKORUUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 11.52 | 0.87 | 6.16 | — |
| OPUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 03:39 | 0.112425 | -0.73 | -0.35 | — |
| ZKUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 03:39 | 0.012207 | 0.51 | -1.14 | — |
| PVTUSDT | MEXC | Tutunma | 27.10.2026 03:42 | 0.0001008 | 0.10 | 0.79 | — |
| MASKUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.40145 | -0.83 | 0.29 | — |
| TUTUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.0175235 | 2.43 | 10.95 | — |
| USUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.00528 | -6.63 | -3.22 | — |
| AIAUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.074555 | -3.29 | -5.37 | — |
| BASECATUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.010385 | 11.89 | 13.05 | — |
| TELUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.0015175 | 3.13 | 0.03 | — |
| AINUSDT | MEXC | Yeni kırılım | 27.10.2026 03:42 | 0.07002 | 96.02 | 124.51 | — |
| SYNUSDT | MEXC | Yeni kırılım | 27.10.2026 03:42 | 0.186635 | -4.69 | -4.17 | — |
| DVOUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 03:42 | 0.00485085 | -0.05 | 0.83 | — |
| IMXUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 03:42 | 0.13905 | -0.72 | -0.63 | — |
| TOWERUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 03:42 | 0.0001345 | -0.22 | -2.53 | — |
| XSPYUSDT | OKX | Tutunma | 27.10.2026 07:33 | 767.345 | 0.45 | 0.51 | — |
| ZBCNUSDT | OKX | Erken dönüş | 27.10.2026 07:33 | 0.0022456 | -3.48 | -7.35 | — |
| IOSTUSDT | OKX | Erken dönüş | 27.10.2026 07:33 | 0.000815 | -4.01 | -2.92 | — |
| LAYERUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 07:33 | 0.06465 | -1.18 | -0.02 | — |
| NEXAUSDT | MEXC | Erken dönüş | 27.10.2026 07:37 | 8.605e-07 | -13.33 | -8.30 | — |
| ANIMEUSDT | MEXC | Erken dönüş | 27.10.2026 07:37 | 0.002841 | 4.93 | 5.21 | — |
| POKTUSDT | MEXC | Yeni kırılım | 27.10.2026 07:37 | 0.01067 | -19.73 | -25.14 | — |
| TAKEUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 07:37 | 0.068745 | 8.26 | 4.53 | — |
| ZORAUSDT | OKX | Erken dönüş | 27.10.2026 11:40 | 0.006372 | 2.32 | 1.49 | — |
| XSOXSUSDT | OKX | Erken dönüş | 27.10.2026 11:40 | 48.42 | -9.98 | -14.27 | — |
| AGLDUSDT | OKX | Erken dönüş | 27.10.2026 11:40 | 0.17855 | -2.72 | -0.42 | — |
| NMRUSDT | OKX | Erken dönüş | 27.10.2026 11:40 | 9.767 | 2.11 | 4.13 | — |
| DASHUSDT | OKX | Yeni kırılım | 27.10.2026 11:40 | 55.11 | 0.42 | -1.38 | — |
| XCRWDUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 11:40 | 260.435 | 2.91 | 3.65 | — |
| ALGOUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 11:40 | 0.103425 | 0.03 | 0.27 | — |
| ARKMUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 11:40 | 0.11809 | 1.32 | 2.07 | — |
| AVAUSDT | MEXC | Erken dönüş | 27.10.2026 11:44 | 0.36415 | -2.05 | -6.63 | — |
| HINTUSDT | MEXC | Erken dönüş | 27.10.2026 11:44 | 0.0008701 | -0.16 | -0.06 | — |
| TRUTHUSDT | MEXC | Yeni kırılım | 27.10.2026 11:44 | 0.021048 | -0.08 | -0.35 | — |
| STAMPUSDT | MEXC | Yeni kırılım | 27.10.2026 11:44 | 0.0004802 | -3.37 | 40.21 | — |
| BCHUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 11:44 | 281.75 | 2.82 | 6.19 | — |
| TICSUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 11:44 | 0.000672 | 1.04 | 2.68 | — |
| GAGUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 11:44 | 0.004666 | 0.28 | 0.41 | — |
| XBOTUSDT | OKX | Tutunma | 27.10.2026 15:42 | 23.87 | 1.68 | 1.55 | — |
| ASPUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 0.0139275 | -12.91 | -9.97 | — |
| LSKUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 0.16987 | -1.55 | -1.57 | — |
| XAMZNUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 251.115 | 1.18 | 0.91 | — |
| XUSARUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 9.12 | 13.60 | 13.38 | — |
| XNBISUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 160.385 | 6.91 | 9.44 | — |
| XAMATUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 396.1 | 0.02 | 1.86 | — |
| XSMCIUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 33.525 | 4.79 | 5.80 | — |
| XORCLUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 128.285 | 2.28 | 2.51 | — |
| XHIMSUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 27.895 | 0.30 | 0.45 | — |
| SWFTCUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 0.0026045 | 0.13 | 0.67 | — |
| HUMAUSDT | OKX | Yeni kırılım | 27.10.2026 15:42 | 0.027195 | -5.35 | -1.60 | — |
| XVRTUSDT | OKX | Yeni kırılım | 27.10.2026 15:42 | 204.805 | 3.10 | 17.72 | — |
| BASEDUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 15:42 | 0.052675 | -0.52 | 0.14 | — |
| XSNDKUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 15:42 | 1281.35 | 2.35 | 5.95 | — |
| VVVUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 25.7316 | 0.32 | -5.55 | — |
| CASHCATUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 0.098615 | 3.65 | 1.32 | — |
| CPUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 0.00951 | -3.58 | -6.20 | — |
| BTWUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 1.467582 | 18.61 | 18.84 | — |
| XPUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 0.0084105 | 0.61 | -0.80 | — |
| WARDUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 0.002551 | 18.74 | 5.88 | — |
| HAEDALUSDT | MEXC | Yeni kırılım | 27.10.2026 15:46 | 0.02476 | 15.63 | 20.15 | — |
| LUCKYUSDT | MEXC | Yeni kırılım | 27.10.2026 15:46 | 0.001404 | 1.57 | 0.57 | — |
| HUMAUSDT | MEXC | Yeni kırılım | 27.10.2026 15:46 | 0.02654 | -3.39 | 0.94 | — |
| XDCUSDT | MEXC | Yeni kırılım | 27.10.2026 15:46 | 0.035375 | -4.42 | -5.07 | — |
| EDELUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.032405 | 1.62 | 0.35 | — |
| DEPUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.0010172 | 1.23 | 0.12 | — |
| HPUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.007858 | -2.35 | -1.71 | — |
| MYSTUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.077425 | 0.03 | 0.73 | — |
| ZIGUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.041114 | 2.80 | 3.14 | — |
| XNAUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 3.0035e-05 | 1.85 | 2.11 | — |
| ATHUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.0057595 | 2.06 | -0.13 | — |
| MEGAUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.048015 | 1.91 | 3.84 | — |
| ROBOUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.005801 | 1.93 | -3.81 | — |
| XAAPLUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 346.445 | 0.10 | -0.06 | — |
| XHOODUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 96.365 | -9.30 | -5.81 | — |
| GRASSUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.7 | 7.53 | -1.04 | — |
| OMIUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.00027155 | 0.61 | -2.08 | — |
| AEVOUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.021825 | 2.08 | -0.16 | — |
| PEPEUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 4.44505e-06 | 9.18 | 8.21 | — |
| API3USDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.25905 | 0.98 | -0.60 | — |
| CFGUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.108345 | 0.96 | -4.53 | — |
| ETHUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 2347.695 | 0.40 | -0.85 | — |
| FLOWUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.026355 | 0.51 | -1.08 | — |
| GRTUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.022495 | 1.00 | -0.78 | — |
| KAIAUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.035265 | 0.24 | -3.96 | — |
| KITEUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.11818 | -0.15 | -2.48 | — |
| PAXGUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 4066.2 | -0.49 | -0.52 | — |
| XCBRSUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 117.69 | 1.54 | -4.37 | — |
| BRL1USDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.1871 | -0.37 | -0.91 | — |
| RONUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.054205 | 0.89 | -0.65 | — |
| ENJUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.025465 | 0.77 | -1.20 | — |
| MMTUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.14255 | -0.67 | -4.03 | — |
| OLUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.0059965 | 0.83 | 19.80 | — |
| PENGUUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.007687 | 1.61 | 0.14 | — |
| PROVEUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 0.1902 | 2.58 | 1.68 | — |
| SSVUSDT | OKX | Erken dönüş | 27.10.2026 19:47 | 2.441 | 0.57 | 0.82 | — |
| BCHUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 290.69 | 2.56 | -0.85 | — |
| XSNXXUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 9.0805 | 6.99 | 10.75 | — |
| XTSMUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 437.38 | -0.58 | 0.40 | — |
| XWDCUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 383.095 | -0.36 | 2.77 | — |
| ZAMAUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 0.076345 | 0.87 | -1.95 | — |
| XALABUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 282.735 | 3.11 | 4.66 | — |
| XASTSUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 43.055 | -2.50 | -4.49 | — |
| XBEUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 220.655 | 0.46 | 1.90 | — |
| XMVLLUSDT | OKX | Yeni kırılım | 27.10.2026 19:47 | 28.665 | 3.65 | 5.74 | — |
| ADXUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.05405 | 5.27 | 3.24 | — |
| DYDXUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.108505 | 1.29 | 0.91 | — |
| GRVTUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.22995 | 3.15 | -3.33 | — |
| MARSCOINUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.068555 | 2.20 | -3.80 | — |
| QUBICUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 4.269e-07 | -3.07 | -2.30 | — |
| STABLEUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.027418 | -1.07 | -0.61 | — |
| TLMUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.0012034 | 1.52 | 0.57 | — |
| GRASSUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.7087 | 6.10 | -1.90 | — |
| QRLUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 1.25273 | -1.31 | -2.89 | — |
| ROBOUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.005796 | 1.78 | -3.88 | — |
| SYLUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 5.655e-05 | 0.99 | 0.23 | — |
| CFGUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.1081 | 0.74 | -4.53 | — |
| FETUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.18 | 1.17 | -0.61 | — |
| IOUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.15039 | -0.14 | -0.19 | — |
| MEGAUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.04792 | 2.13 | 3.94 | — |
| COCOUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.15527 | -0.61 | -0.88 | — |
| ETHUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 2344.865 | 0.51 | -0.67 | — |
| LDOUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.37505 | 0.28 | -1.19 | — |
| LNQUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.0092495 | 0.44 | 0.17 | — |
| OGYUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.00126075 | 0.25 | 0.07 | — |
| ARKMUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.11935 | 1.29 | 0.14 | — |
| AZTECUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.01779 | -1.18 | -5.28 | — |
| DYMUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.01788 | 1.06 | -0.39 | — |
| GMXUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 8.4655 | 4.54 | 4.58 | — |
| MYXUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.06142 | 1.01 | 0.13 | — |
| RIFUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.070155 | 0.62 | 1.56 | — |
| OMIUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 0.0002718 | 0.07 | -2.17 | — |
| ZROUSDT | MEXC | Erken dönüş | 27.10.2026 19:50 | 1.6772 | 2.65 | 0.14 | — |
| BXEUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.0016745 | 6.78 | 5.82 | — |
| HANAUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.014226 | 2.43 | 0.62 | — |
| ACUUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.131585 | 4.77 | -2.86 | — |
| INXUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.0048755 | 1.94 | -2.12 | — |
| LABUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.044255 | 8.19 | 3.83 | — |
| STOPUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.001795 | -0.06 | -0.17 | — |
| WUSDT | MEXC | Yeni kırılım | 27.10.2026 19:50 | 0.012784 | 0.68 | -0.71 | — |
| ELSAUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 19:50 | 0.082515 | -7.22 | -6.50 | — |
| MINIMAUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 19:50 | 0.003365 | -1.63 | 1.93 | — |
| BDXUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 19:50 | 0.07534 | -2.65 | -4.87 | — |
| AUCTIONUSDT | OKX | Erken dönüş | 27.10.2026 23:19 | 3.448 | -0.61 | -1.91 | — |
| XCRCLUSDT | OKX | Erken dönüş | 27.10.2026 23:19 | 81.33 | 0.23 | -0.48 | — |
| ALLOUSDT | OKX | Erken dönüş | 27.10.2026 23:19 | 0.189545 | -1.38 | -1.21 | — |
| HYPEUSDT | OKX | Yeni kırılım | 27.10.2026 23:19 | 81.2245 | 0.15 | -0.03 | — |
| MAGICUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 23:19 | 0.083805 | -1.66 | 0.85 | — |
| PNUTUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 23:19 | 0.04106 | 1.83 | 3.21 | — |
| XMSTRUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 23:19 | 141.745 | 0.74 | 2.62 | — |
| MEMEROBINHOODUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 0.007507 | 7.54 | 11.44 | — |
| RSCUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 0.051995 | -1.61 | -3.43 | — |
| ROSEUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 0.006775 | 0.58 | 0.83 | — |
| SIUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 0.01224 | 19.36 | 17.40 | — |
| AOUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 3.7015 | 8.55 | 7.36 | — |
| MOOUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 0.0018815 | 21.29 | 35.16 | — |
| AVAXUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 8.88 | 1.46 | 1.01 | — |
| EVAAUSDT | MEXC | Yeni kırılım | 27.10.2026 23:23 | 0.9027 | 44.10 | 59.78 | — |
| STONKUSDT | MEXC | Yeni kırılım | 27.10.2026 23:23 | 0.152495 | -3.54 | 0.08 | — |
| MHAUSDT | MEXC | Yeni kırılım | 27.10.2026 23:23 | 0.0054815 | -8.35 | -12.58 | — |
| ZENUSDT | MEXC | Yeni kırılım | 27.10.2026 23:23 | 5.9035 | 0.55 | 0.04 | — |
| XRPUSDT | MEXC | Yeni kırılım | 27.10.2026 23:23 | 1.32305 | 0.62 | 0.43 | — |
| SPXUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 23:23 | 0.3809 | 1.23 | 3.12 | — |
| BEAMXUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 23:23 | 0.0033585 | 0.88 | 1.68 | — |
| VTHOUSDT | MEXC | Erken dönüş | 28.10.2026 03:51 | 0.00058795 | -0.21 | — | — |
| BDCAUSDT | MEXC | Erken dönüş | 28.10.2026 03:51 | 0.29735 | -0.32 | — | — |
| NOCKUSDT | MEXC | Erken dönüş | 28.10.2026 03:51 | 0.01803 | -4.94 | — | — |
| CGPTUSDT | MEXC | Erken dönüş | 28.10.2026 03:51 | 0.01942 | 2.86 | — | — |
| POLYXUSDT | MEXC | Erken dönüş | 28.10.2026 03:51 | 0.03275 | 0.76 | — | — |
| COLLECTUSDT | MEXC | Yeni kırılım | 28.10.2026 03:51 | 0.027995 | -13.13 | — | — |
| TROLLSOLUSDT | MEXC | Yeni kırılım | 28.10.2026 03:51 | 0.031812 | -0.82 | — | — |
| MORPHOUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 03:51 | 2.1993 | -0.61 | — | — |
| JASMYUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 03:51 | 0.004308 | -2.18 | — | — |
| 2U2USDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 03:51 | 0.02145 | -1.21 | — | — |
| RENDERUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 03:51 | 1.688 | -1.48 | — | — |
| ICPUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 03:51 | 2.5925 | -0.87 | — | — |
| KATUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 0.004469 | -3.45 | — | — |
| ENSUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 5.2915 | -0.54 | — | — |
| SAHARAUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 0.0080715 | -2.42 | — | — |
| XBMNRUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 21.85 | -2.79 | — | — |
| COREUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 0.017685 | -1.05 | — | — |
| ICPUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 2.6095 | -0.86 | — | — |
| THETAUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 0.17985 | -1.58 | — | — |
| XOKTAUSDT | OKX | Yeni kırılım | 28.10.2026 07:43 | 227.7 | -2.24 | — | — |
| BOMEUSDT | OKX | Yeni kırılım | 28.10.2026 07:43 | 0.0006525 | -3.02 | — | — |
| FLOKIUSDT | OKX | Yeni kırılım | 28.10.2026 07:43 | 2.3745e-05 | -0.65 | — | — |
| ASTERUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 07:43 | 0.71505 | -1.70 | — | — |
| ONUSDT | MEXC | Tutunma | 28.10.2026 07:46 | 0.15155 | 9.48 | — | — |
| KATUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 0.004475 | -3.75 | — | — |
| CATIUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 0.043955 | -2.42 | — | — |
| SHROOMUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 0.003818 | -8.15 | — | — |
| TRACUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 0.3677 | -0.03 | — | — |
| AAVEUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 135.555 | -3.07 | — | — |
| WOLFTONUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 0.000469 | -2.45 | — | — |
| BONERUSDT | MEXC | Yeni kırılım | 28.10.2026 07:46 | 0.02076 | -9.06 | — | — |
| MEYUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 07:46 | 0.04875 | -1.25 | — | — |
| LOTUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 07:46 | 0.005585 | -0.02 | — | — |
| COREUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 07:46 | 0.01769 | -1.19 | — | — |
| DCTUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 07:46 | 0.0056285 | -0.44 | — | — |
| XMUUUSDT | OKX | Tutunma | 28.10.2026 11:50 | 28.97 | — | — | — |
| YBUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 11:50 | 0.0646 | — | — | — |
| PEAQUSDT | MEXC | Erken dönüş | 28.10.2026 11:54 | 0.03533 | — | — | — |
| SWARMUSDT | MEXC | Erken dönüş | 28.10.2026 11:54 | 0.10238 | — | — | — |
| CRETAUSDT | MEXC | Erken dönüş | 28.10.2026 11:54 | 0.0019645 | — | — | — |
| EMBERUSDT | MEXC | Erken dönüş | 28.10.2026 11:54 | 0.002146 | — | — | — |
| TRADOORUSDT | MEXC | Yeni kırılım | 28.10.2026 11:54 | 0.6564 | — | — | — |
| XANUSDT | MEXC | Yeni kırılım | 28.10.2026 11:54 | 0.011955 | — | — | — |
| SOLVUSDT | MEXC | Yeni kırılım | 28.10.2026 11:54 | 0.005166 | — | — | — |
| ZAMAUSDT | MEXC | Yeni kırılım | 28.10.2026 11:54 | 0.078595 | — | — | — |
| INDEXUSDT | MEXC | Yeni kırılım | 28.10.2026 11:54 | 0.007055 | — | — | — |
| HGPTUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 11:54 | 0.0014783 | — | — | — |
| BIOUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 11:54 | 0.02282 | — | — | — |
| KSKDUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 11:54 | 0.003413 | — | — | — |
| RVNUSDT | OKX | Tutunma | 28.10.2026 15:49 | 0.001468 | — | — | — |
| PROSUSDT | OKX | Erken dönüş | 28.10.2026 15:49 | 0.63125 | — | — | — |
| SANDUSDT | OKX | Erken dönüş | 28.10.2026 15:49 | 0.048015 | — | — | — |
| KSMUSDT | OKX | Erken dönüş | 28.10.2026 15:49 | 3.803 | — | — | — |
| LEOUSDT | OKX | Yeni kırılım | 28.10.2026 15:49 | 9.4315 | — | — | — |
| BNBUSDT | OKX | Yeni kırılım | 28.10.2026 15:49 | 754.075 | — | — | — |
| DOSUSDT | OKX | Yeni kırılım | 28.10.2026 15:49 | 0.3003 | — | — | — |
| SHIBUSDT | OKX | Yeni kırılım | 28.10.2026 15:49 | 4.948e-06 | — | — | — |
| MEMEUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 15:49 | 0.00047125 | — | — | — |
| APTUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 15:49 | 0.68015 | — | — | — |
| XTZUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 15:49 | 0.2768 | — | — | — |
| AEONUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 15:49 | 0.028605 | — | — | — |
| TURBOUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 15:49 | 0.0008186 | — | — | — |
| GOMININGUSDT | MEXC | Erken dönüş | 28.10.2026 15:52 | 0.39375 | — | — | — |
| KATAUSDT | MEXC | Erken dönüş | 28.10.2026 15:52 | 4.161e-05 | — | — | — |
| NAORISUSDT | MEXC | Erken dönüş | 28.10.2026 15:52 | 0.031585 | — | — | — |
| BNBUSDT | MEXC | Yeni kırılım | 28.10.2026 15:52 | 755.57 | — | — | — |
| DOSUSDT | MEXC | Yeni kırılım | 28.10.2026 15:52 | 0.30077 | — | — | — |
| INITUSDT | MEXC | Yeni kırılım | 28.10.2026 15:52 | 0.228635 | — | — | — |
| BATONUSDT | MEXC | Yeni kırılım | 28.10.2026 15:52 | 0.006925 | — | — | — |
| ATOMUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 15:52 | 1.6275 | — | — | — |
| XIBMUSDT | OKX | Erken dönüş | 28.10.2026 19:48 | 252.445 | — | — | — |
| XKOUSDT | OKX | Erken dönüş | 28.10.2026 19:48 | 91.895 | — | — | — |
| OFCUSDT | OKX | Yeni kırılım | 28.10.2026 19:48 | 0.006812 | — | — | — |
| WETUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 19:48 | 0.051765 | — | — | — |
| 2ZUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 19:48 | 0.02873 | — | — | — |
| CVXUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 19:48 | 2.3495 | — | — | — |
| XXIAOMIUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 19:48 | 3.2555 | — | — | — |
| CHIRPUSDT | MEXC | Erken dönüş | 28.10.2026 19:52 | 0.006419 | — | — | — |
| SIXUSDT | MEXC | Erken dönüş | 28.10.2026 19:52 | 0.00467 | — | — | — |
| FLUXUSDT | MEXC | Yeni kırılım | 28.10.2026 19:52 | 0.067745 | — | — | — |
| IDOLUSDT | MEXC | Yeni kırılım | 28.10.2026 19:52 | 0.0085295 | — | — | — |
| REALTOKENUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 19:52 | 0.0011955 | — | — | — |
| BABYUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 19:52 | 0.014568 | — | — | — |
| MOCAUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 19:52 | 0.008819 | — | — | — |
| GOHOMEUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 19:52 | 75.73 | — | — | — |
| ORCAUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 19:52 | 1.6559 | — | — | — |
| WETUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 19:52 | 0.051735 | — | — | — |
| WIFUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 19:52 | 0.17945 | — | — | — |
| GLMRUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 19:52 | 0.0083295 | — | — | — |
| APEUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.12455 | — | — | — |
| CSPRUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.0022985 | — | — | — |
| FLRUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.0061855 | — | — | — |
| LINEAUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.0025045 | — | — | — |
| ONTUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.04956 | — | — | — |
| XCOINUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 160.375 | — | — | — |
| GOATUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.014235 | — | — | — |
| SKYUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.065665 | — | — | — |
| STXUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.30275 | — | — | — |
| BABYDOGEUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 3.515e-10 | — | — | — |
| CHZUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.01299 | — | — | — |
| EIGENUSDT | OKX | Erken dönüş | 28.10.2026 23:40 | 0.1989 | — | — | — |
| EDGEUSDT | OKX | Yeni kırılım | 28.10.2026 23:40 | 0.35035 | — | — | — |
| TIAUSDT | OKX | Yeni kırılım | 28.10.2026 23:40 | 0.556 | — | — | — |
| YGGUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 23:40 | 0.025005 | — | — | — |
| SKLUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 23:40 | 0.0040445 | — | — | — |
| BOBOUSDT | MEXC | Tutunma | 28.10.2026 23:44 | 0.0052755 | — | — | — |
| EACCUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.00063945 | — | — | — |
| PLUMEUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.016313 | — | — | — |
| KASUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.036535 | — | — | — |
| ALGOUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.103775 | — | — | — |
| APEUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.12475 | — | — | — |
| XMNUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.00063 | — | — | — |
| AKEUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.0237875 | — | — | — |
| APTUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.70105 | — | — | — |
| EDENUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.055615 | — | — | — |
| CSPRUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.0023305 | — | — | — |
| EIGENUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.1994 | — | — | — |
| MOODENGUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.03873 | — | — | — |
| ZKUSDT | MEXC | Erken dönüş | 28.10.2026 23:44 | 0.0119655 | — | — | — |
| FIGHTUSDT | MEXC | Yeni kırılım | 28.10.2026 23:44 | 0.004411 | — | — | — |
| AIINUUSDT | MEXC | Yeni kırılım | 28.10.2026 23:44 | 0.0814925 | — | — | — |
| XPINUSDT | MEXC | Yeni kırılım | 28.10.2026 23:44 | 0.0010006 | — | — | — |
| BBUSDT | MEXC | Yeni kırılım | 28.10.2026 23:44 | 0.007914 | — | — | — |
| EDGEUSDT | MEXC | Yeni kırılım | 28.10.2026 23:44 | 0.3503 | — | — | — |
| GSTOCKUSDT | MEXC | Yeni kırılım | 28.10.2026 23:44 | 0.0066945 | — | — | — |
| BASEDUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 23:44 | 0.053215 | — | — | — |
| SCRUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 23:44 | 0.02106 | — | — | — |

### Grupların ayrı ölçümleri

| Grup | Borsa | Süre | Ölçülen / kayıt | Medyan % | BTC üstü puan | Kontrol üstü puan |
|---|---|---:|---:|---:|---:|---:|
| Geri testte tutunma / SAR | MEXC | 12s | 2/3 | -2.32 | -2.01 | 1.24 |
| Geri testte tutunma / SAR | MEXC | 24s | 1/3 | -1.65 | -2.19 | -1.06 |
| Geri testte tutunma / SAR | MEXC | 48s | 0/3 | — | — | — |
| Geri testte tutunma / SAR | OKX | 12s | 5/6 | 6.74 | 6.22 | 6.68 |
| Geri testte tutunma / SAR | OKX | 24s | 3/6 | 9.24 | 6.90 | 7.05 |
| Geri testte tutunma / SAR | OKX | 48s | 0/6 | — | — | — |
| Erken dönüş | MEXC | 12s | 121/148 | 0.04 | -0.05 | -0.31 |
| Erken dönüş | MEXC | 24s | 109/148 | 0.20 | -0.21 | -0.18 |
| Erken dönüş | MEXC | 48s | 53/148 | 0.71 | 0.05 | 0.39 |
| Erken dönüş | OKX | 12s | 134/162 | -0.43 | -0.30 | -0.42 |
| Erken dönüş | OKX | 24s | 125/162 | 0.22 | -0.24 | -0.10 |
| Erken dönüş | OKX | 48s | 65/162 | 0.69 | 0.05 | 0.31 |
| Yatay fiyat / hacim artışı | MEXC | 12s | 85/109 | -0.33 | -0.10 | 0.13 |
| Yatay fiyat / hacim artışı | MEXC | 24s | 73/109 | 0.41 | -0.16 | 0.33 |
| Yatay fiyat / hacim artışı | MEXC | 48s | 48/109 | 0.33 | -0.32 | 0.09 |
| Yatay fiyat / hacim artışı | OKX | 12s | 71/95 | -0.42 | -0.05 | -0.01 |
| Yatay fiyat / hacim artışı | OKX | 24s | 68/95 | 0.89 | 0.09 | 0.27 |
| Yatay fiyat / hacim artışı | OKX | 48s | 53/95 | 0.38 | -0.25 | -0.43 |
| Yeni kırılım | MEXC | 12s | 64/90 | -0.52 | -0.62 | -0.26 |
| Yeni kırılım | MEXC | 24s | 55/90 | -0.78 | -1.60 | -1.63 |
| Yeni kırılım | MEXC | 48s | 19/90 | -2.32 | -2.98 | -4.88 |
| Yeni kırılım | OKX | 12s | 72/93 | 0.57 | 0.34 | -0.04 |
| Yeni kırılım | OKX | 24s | 62/93 | 1.00 | 0.90 | 0.76 |
| Yeni kırılım | OKX | 48s | 12/93 | 2.77 | 2.14 | 2.14 |
| Tutunma | MEXC | 12s | 25/37 | -0.37 | -0.75 | -0.30 |
| Tutunma | MEXC | 24s | 16/37 | -0.93 | -1.45 | -1.00 |
| Tutunma | MEXC | 48s | 5/37 | -2.07 | -3.02 | -6.77 |
| Tutunma | OKX | 12s | 24/40 | 0.66 | 0.39 | 0.04 |
| Tutunma | OKX | 24s | 7/40 | 5.57 | 4.74 | 0.67 |
| Tutunma | OKX | 48s | 0/40 | — | — | — |

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
