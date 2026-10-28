# Coin Tarama 3 — kısa öncelik listesi

Son kontrol: 28.10.2026 07:47 TR.

Geniş havuz: 98 borsa kaydı / 90 sembol. İşlem koşulu elemesini geçen: 13 farklı sembol. Bildirim ve üst liste: en fazla 5 farklı coin.

**Öncelik, kârlılık veya güvenli işlem garantisi değildir.** Hacim/makas, güncel fiyat, yapı ve uzama kontrollerinden geçenler sıralanır. Yalnız yatay hacim hazırlığı bildirilmez. Aday yoksa liste doldurulmaz.

| Coin | Fiyat borsası | Geçen borsalar | Grup | Gerçek gözlem TR | Fiyat | Makas % | Yapı mesafesi % |
|---|---|---|---|---|---:|---:|---:|
| SAHARAUSDT | OKX | OKX | Erken dönüş | 28.10.2026 07:47 | 0.0080505 | 0.16 | 5.27 |
| ENSUSDT | OKX | OKX | Erken dönüş | 28.10.2026 07:47 | 5.283 | 0.08 | 1.97 |
| CELOUSDT | OKX | OKX | Geri testte tutunma / SAR | 28.10.2026 07:47 | 0.080985 | 0.06 | 4.67 |
| ZENUSDT | MEXC | MEXC, OKX | Yeni kırılım | 28.10.2026 07:47 | 5.99 | 0.03 | 4.05 |
| BCHUSDT | OKX | MEXC, OKX | Yeni kırılım | 28.10.2026 07:47 | 298.04 | 0.03 | 4.15 |

Sıralama: en çok 4x sayılan göreli hacim, kapanış konumu, dar makas ve aynı borsanın hacmi. Farklı borsaların hacimleri toplanmaz. Bu sıra başarı olasılığı değildir.

Başlangıç elemesi: en az 100.000 USDT kapalı 24s hacim, en çok %0,5 makas, izlenen seviyeyi koruyan güncel fiyat, kapanıştan en çok 1 ATR uzaklık, EMA20 üstüne en çok 2,5 ATR uzama ve yapı referansına en çok %12 mesafe. 20x üzeri hacim ayrıca incelemede kalır. Bunlar daha iyi sonuç verdiği kanıtlanmış yeni strateji eşikleri değildir.

Aynı sembol tek satırda gösterilir; yalnız elemeden geçen borsalar listelenir. Sembol eşleşmesi bağımsız kontrat kimliği teyidi değildir. Geniş havuz ve eski ölçümler korunur. [Tanınan OKX hisse tokenlerinin kaynağı](https://www.okx.com/help/okx-to-list-tokenized-stocks-for-trading). Liste 2026-10-26 tarihinde kontrol edildi; yeni hisse tokenlerinin eklenmesi gerekebilir.

## Eleme özeti

- 35 borsa kaydı: EMA20 uzaklığı fazla veya bilinmiyor
- 3 borsa kaydı: olağandışı hacim katsayısı; ayrıca inceleme
- 41 borsa kaydı: tanınan tokenleştirilmiş hisse
- 6 borsa kaydı: yalnız hazırlık; ek teknik teyit yok
- 3 borsa kaydı: güncel fiyat kapanıştan uzak veya veri eksik
- 13 borsa kaydı: yapı bozulma mesafesi geniş veya bilinmiyor
- 13 borsa kaydı: makas geniş veya bilinmiyor
- 11 borsa kaydı: izlenen seviye kaybedilmiş veya bilinmiyor
- 43 borsa kaydı: hacim 100.000 USDT altında

Bir kayıtta birden fazla neden olabilir; sayılar bağımsız coinler gibi toplanmaz.
Sıralama sınırı dışında kalan uygun sembol: 8.


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
| COMPUSDT | MEXC | 26.10.2026 23:37 | 21.79 | -1.42 | -2.16 | — |
| ARXUSDT | MEXC | 26.10.2026 23:37 | 0.2252 | 0.84 | 8.75 | — |
| XKORUUSDT | OKX | 27.10.2026 03:44 | 11.475 | 0.83 | 7.36 | — |
| QNTUSDT | MEXC | 27.10.2026 03:44 | 203.095 | -0.44 | -1.62 | — |
| CLANKERUSDT | MEXC | 27.10.2026 03:44 | 13.645 | -0.77 | 1.65 | — |
| TELUSDT | MEXC | 27.10.2026 03:44 | 0.0015175 | 3.00 | 0.03 | — |
| IOSTUSDT | OKX | 27.10.2026 07:38 | 0.0008208 | -4.25 | -3.61 | — |
| ZBCNUSDT | OKX | 27.10.2026 07:38 | 0.00222315 | -2.38 | -5.71 | — |
| XSOXSUSDT | OKX | 27.10.2026 11:46 | 48.635 | -10.02 | — | — |
| ZORAUSDT | OKX | 27.10.2026 11:46 | 0.006395 | 2.31 | — | — |
| DASHUSDT | OKX | 27.10.2026 11:46 | 54.99 | 0.64 | — | — |
| TRUTHUSDT | MEXC | 27.10.2026 11:46 | 0.0210175 | 0.19 | — | — |
| AVAUSDT | MEXC | 27.10.2026 11:46 | 0.36365 | -1.86 | — | — |
| LSKUSDT | OKX | 27.10.2026 15:48 | 0.169625 | -1.21 | — | — |
| CASHCATUSDT | MEXC | 27.10.2026 15:48 | 0.09844 | 4.07 | — | — |
| XDCUSDT | MEXC | 27.10.2026 15:48 | 0.03539 | -4.61 | — | — |
| VVVUSDT | MEXC | 27.10.2026 15:48 | 25.6305 | 0.71 | — | — |
| CFGUSDT | OKX | 27.10.2026 19:53 | 0.10832 | — | — | — |
| STETHUSDT | OKX | 27.10.2026 19:53 | 2344.565 | — | — | — |
| IOUSDT | MEXC | 27.10.2026 19:53 | 0.15046 | — | — | — |
| PENGUUSDT | MEXC | 27.10.2026 19:53 | 0.007689 | — | — | — |
| HYPEUSDT | OKX | 27.10.2026 23:23 | 81.2315 | — | — | — |
| ROSEUSDT | MEXC | 27.10.2026 23:23 | 0.006775 | — | — | — |
| LYNUSDT | MEXC | 27.10.2026 23:23 | 0.01493 | — | — | — |
| ZENUSDT | MEXC | 27.10.2026 23:23 | 5.911 | — | — | — |
| NIGHTUSDT | OKX | 28.10.2026 03:54 | 0.0419635 | — | — | — |
| XSNXXUSDT | OKX | 28.10.2026 03:54 | 9.3325 | — | — | — |
| SAHARAUSDT | OKX | 28.10.2026 07:47 | 0.0080505 | — | — | — |
| ENSUSDT | OKX | 28.10.2026 07:47 | 5.283 | — | — | — |
| BCHUSDT | OKX | 28.10.2026 07:47 | 298.04 | — | — | — |

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

MEXC: incelenen 1043, aday 34; kapanış 28.10.2026 07:00 TR; fiyat gözlemi 28.10.2026 07:46 TR.
V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |
|---|---|---:|---:|---|---|
| EVAAUSDT | Tutunma | 104.47 | 15.87 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; gözlem fiyatı kapanıştan uzaklaştı |
| STAMPUSDT | Tutunma | 83.85 | 4.13 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; yapı bozulma mesafesi geniş; makas geniş |
| CHIPUSDT | Tutunma | 6.41 | 1.66 | Yok | yapı bozulma mesafesi geniş |
| ONUSDT | Tutunma | 16.96 | 3.90 | RSI PU teyitli | yapı bozulma mesafesi geniş; makas geniş |
| STOPUSDT | Tutunma | 4.54 | 3.30 | Yok | düşük hacim; makas geniş |
| WARDUSDT | Tutunma | 29.45 | 3.05 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş |
| ZECUSDT | Tutunma | 8.21 | 1.51 | Yok | Ek eşik uyarısı yok |
| LABUSDT | Tutunma | 16.05 | 2.24 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş |
| LUCKYUSDT | Tutunma | 3.93 | 10.11 | Yok | ortalamadan uzak; düşük hacim |
| PVTUSDT | Tutunma | 1.90 | 2.22 | Yok | düşük hacim; makas geniş |
| XRPUSDT | Tutunma | 2.82 | 1.53 | Yok | Ek eşik uyarısı yok |
| KATUSDT | Erken dönüş | -1.09 | 1.92 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| BDCAUSDT | Erken dönüş | 2.18 | 3.17 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; gözlem fiyatı grubun izlediği seviyenin altında |
| CATIUSDT | Erken dönüş | 2.33 | 1.76 | RSI PU teyitli | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| SHROOMUSDT | Erken dönüş, Yeni kırılım | 73.83 | 1.72 | Yok | 24 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| TRACUSDT | Erken dönüş | 3.10 | 1.53 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; gözlem fiyatı grubun izlediği seviyenin altında |
| AAVEUSDT | Erken dönüş | 1.85 | 1.78 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| MINUSDT | Erken dönüş | 3.88 | 1.55 | RSI PU teyitli | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| WOLFTONUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 0.02 | 1.68 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| LNQUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 1.68 | 1.60 | RSI PU teyitli | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| BLESSUSDT | Yeni kırılım | 9.68 | 2.12 | Yok | gözlem fiyatı kapanıştan uzaklaştı |
| BCHUSDT | Yeni kırılım | 5.50 | 1.96 | Yok | Ek eşik uyarısı yok |
| PONSUSDT | Yeni kırılım | 23.01 | 2.03 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş |
| SIUSDT | Yeni kırılım | 56.17 | 2.17 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş |
| ZENUSDT | Yeni kırılım | 4.42 | 3.66 | Yok | Ek eşik uyarısı yok |
| BONERUSDT | Yeni kırılım | 42.66 | 1.71 | Yok | 24 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; makas geniş; gözlem fiyatı kapanıştan uzaklaştı |
| NIGHTUSDT | Yeni kırılım | 7.33 | 1.99 | Yok | Ek eşik uyarısı yok |
| TROLLSOLUSDT | Yeni kırılım | 8.82 | 1.71 | Yok | düşük hacim; makas geniş |
| AZTECUSDT | Geri testte tutunma / SAR | 7.85 | 1.51 | Yok | düşük hacim; geri testte SAR desteği; devam garantisi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| MEYUSDT | Yatay fiyat / hacim artışı | 5.11 | 3.55 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| DEPUSDT | Yatay fiyat / hacim artışı | 3.18 | 1.65 | RSI PU teyitli | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| LOTUSDT | Yatay fiyat / hacim artışı | 0.97 | 1.59 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| COREUSDT | Yatay fiyat / hacim artışı | 2.69 | 1.63 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| DCTUSDT | Yatay fiyat / hacim artışı | -1.60 | 2.15 | RSI PU teyitli | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |

OKX: incelenen 339, aday 64; kapanış 28.10.2026 07:00 TR; fiyat gözlemi 28.10.2026 07:43 TR.
V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |
|---|---|---:|---:|---|---|
| XCRWDUSDT | Tutunma | 3.64 | 3.56 | Yok | ortalamadan uzak; düşük hacim |
| XLITEUSDT | Tutunma | 6.84 | 8.94 | Yok | ortalamadan uzak |
| XRKLBUSDT | Tutunma | 9.42 | 24.16 | Yok | ortalamadan uzak |
| XWDCUSDT | Tutunma | 7.37 | 11.39 | Yok | Ek eşik uyarısı yok |
| ZECUSDT | Tutunma | 8.18 | 3.07 | Yok | Ek eşik uyarısı yok |
| XTSLAUSDT | Tutunma | 3.84 | 10.94 | Yok | ortalamadan uzak |
| XBEUSDT | Tutunma | 7.93 | 3.80 | Yok | Ek eşik uyarısı yok |
| XCRWVUSDT | Tutunma | 7.51 | 3.20 | Yok | düşük hacim |
| XGEVUSDT | Tutunma | 5.27 | 18.68 | Yok | ortalamadan uzak; düşük hacim |
| XNBISUSDT | Tutunma | 12.37 | 6.09 | Yok | Ek eşik uyarısı yok |
| XORCLUSDT | Tutunma | 4.44 | 9.34 | Yok | ortalamadan uzak; düşük hacim |
| XRPUSDT | Tutunma | 2.85 | 2.21 | Yok | Ek eşik uyarısı yok |
| XSHAZUSDT | Tutunma | 11.15 | 12.21 | Yok | ortalamadan uzak; düşük hacim |
| XUSARUSDT | Tutunma | 16.74 | 222.12 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim |
| KATUSDT | Erken dönüş | -1.16 | 1.53 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ENSUSDT | Erken dönüş | 2.77 | 9.96 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| SAHARAUSDT | Erken dönüş | 3.87 | 10.42 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| LAYERUSDT | Erken dönüş | -0.18 | 10.04 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| FILUSDT | Erken dönüş | 1.93 | 1.75 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XBMNRUSDT | Erken dönüş | 4.13 | 1.63 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| COREUSDT | Erken dönüş | 3.40 | 1.50 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ICPUSDT | Erken dönüş | 1.48 | 1.63 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| IMXUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 1.31 | 1.83 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| THETAUSDT | Erken dönüş | 1.91 | 1.54 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| BCHUSDT | Yeni kırılım | 5.51 | 3.30 | Yok | Ek eşik uyarısı yok |
| XAVGOUSDT | Yeni kırılım | 4.32 | 3.65 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| XBOTUSDT | Yeni kırılım | 3.73 | 4.88 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| XDELLUSDT | Yeni kırılım | 8.34 | 2.20 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XDRAMUSDT | Yeni kırılım | 6.83 | 3.98 | Yok | ortalamadan uzak; düşük hacim |
| XEWYUSDT | Yeni kırılım | 4.86 | 3.68 | Yok | ortalamadan uzak; düşük hacim |
| XINTCUSDT | Yeni kırılım | 5.12 | 2.27 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XOKTAUSDT | Yeni kırılım | 3.48 | 18.73 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| XQCOMUSDT | Yeni kırılım | 3.55 | 6.64 | Yok | ortalamadan uzak; düşük hacim |
| XAMDUSDT | Yeni kırılım | 7.04 | 1.98 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XMRVLUSDT | Yeni kırılım | 5.89 | 1.54 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XMUUSDT | Yeni kırılım | 5.40 | 1.73 | Yok | ortalamadan uzak |
| XSMHUSDT | Yeni kırılım | 4.30 | 1.96 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| BOMEUSDT | Yeni kırılım | 5.17 | 3.08 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| FLOKIUSDT | Yeni kırılım | 4.17 | 3.71 | RSI PU teyitli | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| NIGHTUSDT | Yeni kırılım | 7.36 | 2.62 | Yok | Ek eşik uyarısı yok |
| PONSUSDT | Yeni kırılım | 23.01 | 2.24 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş |
| XAAOIUSDT | Yeni kırılım | 6.93 | 2.71 | Yok | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XALABUSDT | Yeni kırılım | 10.84 | 7.24 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XAMZNUSDT | Yeni kırılım | 2.16 | 2.83 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| XAPLDUSDT | Yeni kırılım | 9.50 | 2.98 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| XARMUSDT | Yeni kırılım | 3.33 | 4.19 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XASMLUSDT | Yeni kırılım | 4.61 | 6.93 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XCBRSUSDT | Yeni kırılım | 11.43 | 9.83 | Yok | ortalamadan uzak |
| XCOHRUSDT | Yeni kırılım | 7.62 | 3.37 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XIRENUSDT | Yeni kırılım | 8.34 | 8.44 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XKORUUSDT | Yeni kırılım | 14.16 | 10.17 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XLRCXUSDT | Yeni kırılım | 3.21 | 15.17 | Yok | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XMVLLUSDT | Yeni kırılım | 11.47 | 3.13 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XSNDKUSDT | Yeni kırılım | 7.32 | 2.04 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XSNXXUSDT | Yeni kırılım | 14.66 | 3.92 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XSOXLUSDT | Yeni kırılım | 13.62 | 3.01 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XTQQQUSDT | Yeni kırılım | 4.90 | 3.47 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| ZENUSDT | Yeni kırılım | 4.24 | 3.42 | Yok | Ek eşik uyarısı yok |
| XAMATUSDT | Yeni kırılım | 4.17 | 1.69 | Yok | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XSMCIUSDT | Yeni kırılım | 8.06 | 1.88 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XVRTUSDT | Yeni kırılım | 5.39 | 1.72 | Yok | ortalamadan uzak; düşük hacim |
| XASTSUSDT | Geri testte tutunma / SAR, Tutunma | 6.49 | 22.14 | Yok | düşük hacim; geri testte SAR desteği; devam garantisi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| CELOUSDT | Geri testte tutunma / SAR | 3.96 | 5.19 | Yok | geri testte SAR desteği; devam garantisi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ASTERUSDT | Yatay fiyat / hacim artışı | 1.53 | 1.63 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |

İki borsada toplam 90 farklı sembol. Ortak semboller bağımsız iki başarı sayılmaz.

Eşikler başlangıç deneyidir; daha çok aday daha yüksek başarı demek değildir. Yazılım testleri kârlılık kanıtı değildir. Dört saatlik mum ve zamanlayıcı gecikmesi ilk hareketin kaçmasına yol açabilir. SAR yön desteğidir; getiri garantisi değildir.

## Bu döngüde yeni gelenler

KATUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 07:43 TR; fiyat 0.004469
24s %-1.16; ilgili hacim 1.5267x; makas %0.13
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ENSUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 07:43 TR; fiyat 5.2915
24s %2.77; ilgili hacim 9.9572x; makas %0.09
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

SAHARAUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 07:43 TR; fiyat 0.0080715
24s %3.87; ilgili hacim 10.421x; makas %0.16
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XBMNRUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 07:43 TR; fiyat 21.85
24s %4.13; ilgili hacim 1.6287x; makas %0.09
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

COREUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 07:43 TR; fiyat 0.017685
24s %3.40; ilgili hacim 1.5013x; makas %0.17
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ICPUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 07:43 TR; fiyat 2.6095
24s %1.48; ilgili hacim 1.6293x; makas %0.04
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

THETAUSDT · OKX
Gruplar: Erken dönüş
Gözlem 28.10.2026 07:43 TR; fiyat 0.17985
24s %1.91; ilgili hacim 1.5444x; makas %0.17
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; teyitli RSI pozitif uyumsuzluk desteği

XOKTAUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 28.10.2026 07:43 TR; fiyat 227.7
24s %3.48; ilgili hacim 18.728x; makas %0.25
ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında

BOMEUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 28.10.2026 07:43 TR; fiyat 0.0006525
24s %5.17; ilgili hacim 3.0833x; makas %0.12
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

FLOKIUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 28.10.2026 07:43 TR; fiyat 2.3745e-05
24s %4.17; ilgili hacim 3.7062x; makas %0.04
düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; teyitli RSI pozitif uyumsuzluk desteği

ASTERUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 28.10.2026 07:43 TR; fiyat 0.71505
24s %1.53; ilgili hacim 1.6312x; makas %0.04
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ONUSDT · MEXC
Gruplar: Tutunma
Gözlem 28.10.2026 07:46 TR; fiyat 0.15155
24s %16.96; ilgili hacim 3.8984x; makas %0.73
yapı bozulma mesafesi geniş; makas geniş; teyitli RSI pozitif uyumsuzluk desteği

KATUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 07:46 TR; fiyat 0.004475
24s %-1.09; ilgili hacim 1.9222x; makas %0.22
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

CATIUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 07:46 TR; fiyat 0.043955
24s %2.33; ilgili hacim 1.7626x; makas %0.11
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; teyitli RSI pozitif uyumsuzluk desteği

SHROOMUSDT · MEXC
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 28.10.2026 07:46 TR; fiyat 0.003818
24s %73.83; ilgili hacim 1.7249x; makas %2.67
24 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

TRACUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 07:46 TR; fiyat 0.3677
24s %3.10; ilgili hacim 1.5324x; makas %0.54
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; gözlem fiyatı grubun izlediği seviyenin altında

AAVEUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 28.10.2026 07:46 TR; fiyat 135.56
24s %1.85; ilgili hacim 1.777x; makas %0.01
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

WOLFTONUSDT · MEXC
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 28.10.2026 07:46 TR; fiyat 0.000469
24s %0.02; ilgili hacim 1.675x; makas %0.21
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

BONERUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 28.10.2026 07:46 TR; fiyat 0.02076
24s %42.66; ilgili hacim 1.7064x; makas %1.93
24 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; makas geniş; gözlem fiyatı kapanıştan uzaklaştı

MEYUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 28.10.2026 07:46 TR; fiyat 0.04875
24s %5.11; ilgili hacim 3.5523x; makas %0.04
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

LOTUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 28.10.2026 07:46 TR; fiyat 0.005585
24s %0.97; ilgili hacim 1.588x; makas %1.07
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

COREUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 28.10.2026 07:46 TR; fiyat 0.01769
24s %2.69; ilgili hacim 1.6276x; makas %0.45
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

DCTUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 28.10.2026 07:46 TR; fiyat 0.0056285
24s %-1.60; ilgili hacim 2.1471x; makas %0.27
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

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
| WUSDT | OKX | Erken dönüş | 26.10.2026 23:32 | 0.012345 | 0.62 | 3.53 | — |
| COMPUSDT | OKX | Erken dönüş | 26.10.2026 23:32 | 21.755 | -1.45 | -2.09 | — |
| FLUIDUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 23:32 | 2.188 | 1.59 | 0.71 | — |
| LQTYUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 23:32 | 0.1938 | -0.21 | 2.01 | — |
| APTMUSDT | MEXC | Erken dönüş | 26.10.2026 23:36 | 0.05199 | 0.08 | 0.33 | — |
| QUSDT | MEXC | Erken dönüş | 26.10.2026 23:36 | 0.1341405 | -22.83 | -59.84 | — |
| ARXUSDT | MEXC | Erken dönüş | 26.10.2026 23:36 | 0.22615 | 0.33 | 8.25 | — |
| COMPUSDT | MEXC | Erken dönüş | 26.10.2026 23:36 | 21.79 | -1.47 | -2.16 | — |
| SYMMUSDT | MEXC | Yeni kırılım | 26.10.2026 23:36 | 0.0307 | 17.26 | 9.12 | — |
| VERONAUSDT | MEXC | Yeni kırılım | 26.10.2026 23:36 | 0.13405 | -7.50 | -8.62 | — |
| JEANPHILUSDT | MEXC | Yeni kırılım | 26.10.2026 23:36 | 0.0045445 | 1.02 | -0.91 | — |
| FUELUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 23:36 | 0.00079595 | -0.36 | 0.45 | — |
| TIAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 23:36 | 0.54485 | -3.11 | -0.87 | — |
| ALEXUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 23:36 | 0.0038645 | 2.86 | 3.51 | — |
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
| ZORAUSDT | OKX | Erken dönüş | 27.10.2026 11:40 | 0.006372 | 2.32 | — | — |
| XSOXSUSDT | OKX | Erken dönüş | 27.10.2026 11:40 | 48.42 | -9.98 | — | — |
| AGLDUSDT | OKX | Erken dönüş | 27.10.2026 11:40 | 0.17855 | -2.72 | — | — |
| NMRUSDT | OKX | Erken dönüş | 27.10.2026 11:40 | 9.767 | 2.11 | — | — |
| DASHUSDT | OKX | Yeni kırılım | 27.10.2026 11:40 | 55.11 | 0.42 | — | — |
| XCRWDUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 11:40 | 260.435 | 2.91 | — | — |
| ALGOUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 11:40 | 0.103425 | 0.03 | — | — |
| ARKMUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 11:40 | 0.11809 | 1.32 | — | — |
| AVAUSDT | MEXC | Erken dönüş | 27.10.2026 11:44 | 0.36415 | -2.05 | — | — |
| HINTUSDT | MEXC | Erken dönüş | 27.10.2026 11:44 | 0.0008701 | -0.16 | — | — |
| TRUTHUSDT | MEXC | Yeni kırılım | 27.10.2026 11:44 | 0.021048 | -0.08 | — | — |
| STAMPUSDT | MEXC | Yeni kırılım | 27.10.2026 11:44 | 0.0004802 | -3.37 | — | — |
| BCHUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 11:44 | 281.75 | 2.82 | — | — |
| TICSUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 11:44 | 0.000672 | 1.04 | — | — |
| GAGUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 11:44 | 0.004666 | 0.28 | — | — |
| XBOTUSDT | OKX | Tutunma | 27.10.2026 15:42 | 23.87 | 1.68 | — | — |
| ASPUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 0.0139275 | -12.91 | — | — |
| LSKUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 0.16987 | -1.55 | — | — |
| XAMZNUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 251.115 | 1.18 | — | — |
| XUSARUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 9.12 | 13.60 | — | — |
| XNBISUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 160.385 | 6.91 | — | — |
| XAMATUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 396.1 | 0.02 | — | — |
| XSMCIUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 33.525 | 4.79 | — | — |
| XORCLUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 128.285 | 2.28 | — | — |
| XHIMSUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 27.895 | 0.30 | — | — |
| SWFTCUSDT | OKX | Erken dönüş | 27.10.2026 15:42 | 0.0026045 | 0.13 | — | — |
| HUMAUSDT | OKX | Yeni kırılım | 27.10.2026 15:42 | 0.027195 | -5.35 | — | — |
| XVRTUSDT | OKX | Yeni kırılım | 27.10.2026 15:42 | 204.805 | 3.10 | — | — |
| BASEDUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 15:42 | 0.052675 | -0.52 | — | — |
| XSNDKUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 15:42 | 1281.35 | 2.35 | — | — |
| VVVUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 25.7316 | 0.32 | — | — |
| CASHCATUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 0.098615 | 3.65 | — | — |
| CPUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 0.00951 | -3.58 | — | — |
| BTWUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 1.467582 | 18.61 | — | — |
| XPUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 0.0084105 | 0.61 | — | — |
| WARDUSDT | MEXC | Erken dönüş | 27.10.2026 15:46 | 0.002551 | 18.74 | — | — |
| HAEDALUSDT | MEXC | Yeni kırılım | 27.10.2026 15:46 | 0.02476 | 15.63 | — | — |
| LUCKYUSDT | MEXC | Yeni kırılım | 27.10.2026 15:46 | 0.001404 | 1.57 | — | — |
| HUMAUSDT | MEXC | Yeni kırılım | 27.10.2026 15:46 | 0.02654 | -3.39 | — | — |
| XDCUSDT | MEXC | Yeni kırılım | 27.10.2026 15:46 | 0.035375 | -4.42 | — | — |
| EDELUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.032405 | 1.62 | — | — |
| DEPUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.0010172 | 1.23 | — | — |
| HPUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.007858 | -2.35 | — | — |
| MYSTUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.077425 | 0.03 | — | — |
| ZIGUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 0.041114 | 2.80 | — | — |
| XNAUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 15:46 | 3.0035e-05 | 1.85 | — | — |
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
| AUCTIONUSDT | OKX | Erken dönüş | 27.10.2026 23:19 | 3.448 | — | — | — |
| XCRCLUSDT | OKX | Erken dönüş | 27.10.2026 23:19 | 81.33 | — | — | — |
| ALLOUSDT | OKX | Erken dönüş | 27.10.2026 23:19 | 0.189545 | — | — | — |
| HYPEUSDT | OKX | Yeni kırılım | 27.10.2026 23:19 | 81.2245 | — | — | — |
| MAGICUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 23:19 | 0.083805 | — | — | — |
| PNUTUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 23:19 | 0.04106 | — | — | — |
| XMSTRUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 23:19 | 141.745 | — | — | — |
| MEMEROBINHOODUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 0.007507 | — | — | — |
| RSCUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 0.051995 | — | — | — |
| ROSEUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 0.006775 | — | — | — |
| SIUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 0.01224 | — | — | — |
| AOUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 3.7015 | — | — | — |
| MOOUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 0.0018815 | — | — | — |
| AVAXUSDT | MEXC | Erken dönüş | 27.10.2026 23:23 | 8.88 | — | — | — |
| EVAAUSDT | MEXC | Yeni kırılım | 27.10.2026 23:23 | 0.9027 | — | — | — |
| STONKUSDT | MEXC | Yeni kırılım | 27.10.2026 23:23 | 0.152495 | — | — | — |
| MHAUSDT | MEXC | Yeni kırılım | 27.10.2026 23:23 | 0.0054815 | — | — | — |
| ZENUSDT | MEXC | Yeni kırılım | 27.10.2026 23:23 | 5.9035 | — | — | — |
| XRPUSDT | MEXC | Yeni kırılım | 27.10.2026 23:23 | 1.32305 | — | — | — |
| SPXUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 23:23 | 0.3809 | — | — | — |
| BEAMXUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 23:23 | 0.0033585 | — | — | — |
| VTHOUSDT | MEXC | Erken dönüş | 28.10.2026 03:51 | 0.00058795 | — | — | — |
| BDCAUSDT | MEXC | Erken dönüş | 28.10.2026 03:51 | 0.29735 | — | — | — |
| NOCKUSDT | MEXC | Erken dönüş | 28.10.2026 03:51 | 0.01803 | — | — | — |
| CGPTUSDT | MEXC | Erken dönüş | 28.10.2026 03:51 | 0.01942 | — | — | — |
| POLYXUSDT | MEXC | Erken dönüş | 28.10.2026 03:51 | 0.03275 | — | — | — |
| COLLECTUSDT | MEXC | Yeni kırılım | 28.10.2026 03:51 | 0.027995 | — | — | — |
| TROLLSOLUSDT | MEXC | Yeni kırılım | 28.10.2026 03:51 | 0.031812 | — | — | — |
| MORPHOUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 03:51 | 2.1993 | — | — | — |
| JASMYUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 03:51 | 0.004308 | — | — | — |
| 2U2USDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 03:51 | 0.02145 | — | — | — |
| RENDERUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 03:51 | 1.688 | — | — | — |
| ICPUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 03:51 | 2.5925 | — | — | — |
| KATUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 0.004469 | — | — | — |
| ENSUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 5.2915 | — | — | — |
| SAHARAUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 0.0080715 | — | — | — |
| XBMNRUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 21.85 | — | — | — |
| COREUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 0.017685 | — | — | — |
| ICPUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 2.6095 | — | — | — |
| THETAUSDT | OKX | Erken dönüş | 28.10.2026 07:43 | 0.17985 | — | — | — |
| XOKTAUSDT | OKX | Yeni kırılım | 28.10.2026 07:43 | 227.7 | — | — | — |
| BOMEUSDT | OKX | Yeni kırılım | 28.10.2026 07:43 | 0.0006525 | — | — | — |
| FLOKIUSDT | OKX | Yeni kırılım | 28.10.2026 07:43 | 2.3745e-05 | — | — | — |
| ASTERUSDT | OKX | Yatay fiyat / hacim artışı | 28.10.2026 07:43 | 0.71505 | — | — | — |
| ONUSDT | MEXC | Tutunma | 28.10.2026 07:46 | 0.15155 | — | — | — |
| KATUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 0.004475 | — | — | — |
| CATIUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 0.043955 | — | — | — |
| SHROOMUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 0.003818 | — | — | — |
| TRACUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 0.3677 | — | — | — |
| AAVEUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 135.555 | — | — | — |
| WOLFTONUSDT | MEXC | Erken dönüş | 28.10.2026 07:46 | 0.000469 | — | — | — |
| BONERUSDT | MEXC | Yeni kırılım | 28.10.2026 07:46 | 0.02076 | — | — | — |
| MEYUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 07:46 | 0.04875 | — | — | — |
| LOTUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 07:46 | 0.005585 | — | — | — |
| COREUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 07:46 | 0.01769 | — | — | — |
| DCTUSDT | MEXC | Yatay fiyat / hacim artışı | 28.10.2026 07:46 | 0.0056285 | — | — | — |

### Grupların ayrı ölçümleri

| Grup | Borsa | Süre | Ölçülen / kayıt | Medyan % | BTC üstü puan | Kontrol üstü puan |
|---|---|---:|---:|---:|---:|---:|
| Geri testte tutunma / SAR | MEXC | 12s | 1/2 | -0.37 | -0.43 | 1.26 |
| Geri testte tutunma / SAR | MEXC | 24s | 1/2 | -1.65 | -2.19 | -1.06 |
| Geri testte tutunma / SAR | MEXC | 48s | 0/2 | — | — | — |
| Geri testte tutunma / SAR | OKX | 12s | 3/5 | 7.69 | 6.60 | 7.97 |
| Geri testte tutunma / SAR | OKX | 24s | 1/5 | 8.27 | 6.59 | 6.56 |
| Geri testte tutunma / SAR | OKX | 48s | 0/5 | — | — | — |
| Erken dönüş | MEXC | 12s | 69/121 | -0.32 | -0.08 | -0.22 |
| Erken dönüş | MEXC | 24s | 61/121 | 0.53 | -0.18 | 0.30 |
| Erken dönüş | MEXC | 48s | 0/121 | — | — | — |
| Erken dönüş | OKX | 12s | 84/134 | -0.74 | -0.44 | -0.40 |
| Erken dönüş | OKX | 24s | 70/134 | 0.66 | 0.03 | 0.30 |
| Erken dönüş | OKX | 48s | 0/134 | — | — | — |
| Yatay fiyat / hacim artışı | MEXC | 12s | 63/85 | -0.22 | -0.08 | 0.27 |
| Yatay fiyat / hacim artışı | MEXC | 24s | 52/85 | 0.24 | -0.42 | 0.10 |
| Yatay fiyat / hacim artışı | MEXC | 48s | 0/85 | — | — | — |
| Yatay fiyat / hacim artışı | OKX | 12s | 63/71 | -0.42 | -0.05 | 0.02 |
| Yatay fiyat / hacim artışı | OKX | 24s | 57/71 | 0.78 | 0.02 | 0.25 |
| Yatay fiyat / hacim artışı | OKX | 48s | 0/71 | — | — | — |
| Yeni kırılım | MEXC | 12s | 31/64 | -0.81 | -0.84 | -0.15 |
| Yeni kırılım | MEXC | 24s | 25/64 | -1.46 | -1.93 | -2.95 |
| Yeni kırılım | MEXC | 48s | 0/64 | — | — | — |
| Yeni kırılım | OKX | 12s | 31/72 | 0.54 | 0.65 | 0.18 |
| Yeni kırılım | OKX | 24s | 27/72 | 3.01 | 2.48 | 2.59 |
| Yeni kırılım | OKX | 48s | 0/72 | — | — | — |
| Tutunma | MEXC | 12s | 15/25 | -0.37 | -0.75 | 0.43 |
| Tutunma | MEXC | 24s | 10/25 | -1.63 | -2.37 | -2.88 |
| Tutunma | MEXC | 48s | 0/25 | — | — | — |
| Tutunma | OKX | 12s | 7/24 | 1.68 | 1.16 | -0.34 |
| Tutunma | OKX | 24s | 2/24 | 3.47 | 1.78 | -0.95 |
| Tutunma | OKX | 48s | 0/24 | — | — | — |

## Önceki V4 kayıtları — yeni kayıt alınmıyor

Eski gerçek giriş fiyatları korunur; bunlar yeni grupların geçmişte yakaladığı örnekler değildir. 12/24/48s ölçümleri ayrı sürdürülür.

## Gerçek gözlemden sonraki ölçümler

Her sürüm ve borsanın ilk gerçek alış/satış orta fiyatı ayrı kaydedilir. Aynı coin grup değiştirse de yeni bağımsız örnek sayılmaz. Hedef saatten sonraki ilk dakika kapanışı kullanılır; gecikme 60 saniyeden küçüktür. Ücret/kayma dahil net kâr değildir. Henüz oluşmamış veya eksik ölçümler boş kalır.

8 borsa kaydı, 8 farklı sembol. Ortak semboller iki bağımsız başarı gibi toplanmaz.

| Borsa | Süre | Ölçülen | Medyan % | BTC üstü puan | Kontrol üstü puan | Kontrol ölçülen |
|---|---:|---:|---:|---:|---:|---:|
| MEXC | 12s | 8/8 | -2.13 | -1.79 | -2.12 | 8 |
| MEXC | 24s | 8/8 | -2.41 | -1.82 | -2.00 | 8 |
| MEXC | 48s | 5/8 | -0.96 | -1.23 | -9.77 | 5 |

| Coin | Borsa | İlk grup | Gerçek gözlem TR | Referans fiyat | 12s % | 24s % | 48s % |
|---|---|---|---|---:|---:|---:|---:|
| BULLAUSDT | MEXC | Yeni kırılım | 26.10.2026 11:48 | 0.1130635 | 35.79 | 4.11 | — |
| CAPUSDT | MEXC | Tutunma | 26.10.2026 00:23 | 0.10956 | -21.28 | -9.24 | -9.21 |
| CPHUSDT | MEXC | Tutunma | 26.10.2026 11:48 | 0.0035595 | -3.05 | -3.55 | — |
| GBCKUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.0048565 | -0.59 | -1.27 | -0.96 |
| MIUUSDT | MEXC | Yeni kırılım | 26.10.2026 03:52 | 8.85e-10 | 5.08 | 3.95 | 1.69 |
| NEXUSDT | MEXC | Yeni kırılım | 26.10.2026 11:48 | 7.95e-07 | -10.87 | -9.67 | — |
| STONKSUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.0020883 | -19.28 | -24.35 | -53.64 |
| TAUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.06203 | -1.21 | -0.18 | 1.63 |

Karşılaştırma için en az 1–2 haftalık gerçek kayıt beklenir. Gruplar, borsalar ve ortak coinler dikkate alınmadan bir kazanma oranı iddia edilmez.


<!-- coin-priority-raw:end -->

</details>
