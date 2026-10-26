# Coin Tarama 3 — kısa öncelik listesi

Son kontrol: 26.10.2026 19:50 TR.

Geniş havuz: 162 borsa kaydı / 134 sembol. İşlem koşulu elemesini geçen: 16 farklı sembol. Bildirim ve üst liste: en fazla 5 farklı coin.

**Öncelik, kârlılık veya güvenli işlem garantisi değildir.** Hacim/makas, güncel fiyat, yapı ve uzama kontrollerinden geçenler sıralanır. Yalnız yatay hacim hazırlığı bildirilmez. Aday yoksa liste doldurulmaz.

| Coin | Fiyat borsası | Geçen borsalar | Grup | Gerçek gözlem TR | Fiyat | Makas % | Yapı mesafesi % |
|---|---|---|---|---|---:|---:|---:|
| CELOUSDT | OKX | OKX | Erken dönüş | 26.10.2026 19:50 | 0.079105 | 0.11 | 2.97 |
| POLUSDT | OKX | MEXC, OKX | Erken dönüş | 26.10.2026 19:50 | 0.091045 | 0.03 | 2.65 |
| ONDOUSDT | OKX | OKX | Erken dönüş | 26.10.2026 19:50 | 0.41515 | 0.02 | 1.79 |
| WLFIUSDT | OKX | OKX | Erken dönüş | 26.10.2026 19:50 | 0.053445 | 0.06 | 1.34 |
| MOVRUSDT | MEXC | MEXC | Erken dönüş | 26.10.2026 19:50 | 1.0922 | 0.38 | 4.38 |

Sıralama: en çok 4x sayılan göreli hacim, kapanış konumu, dar makas ve aynı borsanın hacmi. Farklı borsaların hacimleri toplanmaz. Bu sıra başarı olasılığı değildir.

Başlangıç elemesi: en az 100.000 USDT kapalı 24s hacim, en çok %0,5 makas, izlenen seviyeyi koruyan güncel fiyat, kapanıştan en çok 1 ATR uzaklık, EMA20 üstüne en çok 2,5 ATR uzama ve yapı referansına en çok %12 mesafe. 20x üzeri hacim ayrıca incelemede kalır. Bunlar daha iyi sonuç verdiği kanıtlanmış yeni strateji eşikleri değildir.

Aynı sembol tek satırda gösterilir; yalnız elemeden geçen borsalar listelenir. Sembol eşleşmesi bağımsız kontrat kimliği teyidi değildir. Geniş havuz ve eski ölçümler korunur. [Tanınan OKX hisse tokenlerinin kaynağı](https://www.okx.com/help/okx-to-list-tokenized-stocks-for-trading). Liste 2026-10-26 tarihinde kontrol edildi; yeni hisse tokenlerinin eklenmesi gerekebilir.

## Eleme özeti

- 9 borsa kaydı: EMA20 uzaklığı fazla veya bilinmiyor
- 4 borsa kaydı: olağandışı hacim katsayısı; ayrıca inceleme
- 12 borsa kaydı: tanınan tokenleştirilmiş hisse
- 62 borsa kaydı: yalnız hazırlık; ek teknik teyit yok
- 4 borsa kaydı: güncel fiyat kapanıştan uzak veya veri eksik
- 7 borsa kaydı: yapı bozulma mesafesi geniş veya bilinmiyor
- 9 borsa kaydı: makas geniş veya bilinmiyor
- 52 borsa kaydı: izlenen seviye kaybedilmiş veya bilinmiyor
- 57 borsa kaydı: hacim 100.000 USDT altında

Bir kayıtta birden fazla neden olabilir; sayılar bağımsız coinler gibi toplanmaz.
Sıralama sınırı dışında kalan uygun sembol: 11.


## Öncelik listesinin ayrı gerçek gözlem ölçümleri

Referans, bu kısa listeye ilk girişte gerçekten okunan fiyat ve saattir; eski geniş listedeki daha erken fiyat kullanılmaz. 12/24/48s ölçümleri state.json içinde ayrı tutulur. Aynı sembolün iki borsa kaydı bağımsız iki coin sayılmaz.

<details>
<summary>Öncelik listesinin 12/24/48 saat sonuçlarını aç</summary>

| Coin | Borsa | İlk gerçek gözlem TR | Referans | 12s % | 24s % | 48s % |
|---|---|---|---:|---:|---:|---:|
| LUNAUSDT | OKX | 26.10.2026 16:56 | 0.04159 | — | — | — |
| METUSDT | OKX | 26.10.2026 16:56 | 0.31085 | — | — | — |
| CRVUSDT | OKX | 26.10.2026 16:56 | 0.3495 | — | — | — |
| NIGHTUSDT | MEXC | 26.10.2026 16:56 | 0.03791 | — | — | — |
| ONDOUSDT | MEXC | 26.10.2026 16:56 | 0.41274 | — | — | — |
| ARBUSDT | MEXC | 26.10.2026 17:50 | 0.171355 | — | — | — |
| CELOUSDT | OKX | 26.10.2026 19:50 | 0.079105 | — | — | — |
| POLUSDT | OKX | 26.10.2026 19:50 | 0.091045 | — | — | — |
| ONDOUSDT | OKX | 26.10.2026 19:50 | 0.41515 | — | — | — |
| WLFIUSDT | OKX | 26.10.2026 19:50 | 0.053445 | — | — | — |
| MOVRUSDT | MEXC | 26.10.2026 19:50 | 1.0922 | — | — | — |

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

MEXC: incelenen 1034, aday 72; kapanış 26.10.2026 19:00 TR; fiyat gözlemi 26.10.2026 19:49 TR.
V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |
|---|---|---:|---:|---|---|
| PARTIUSDT | Erken dönüş, Yeni kırılım | 13.77 | 1.58 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| TRUMPUSDT | Erken dönüş | 1.81 | 2.05 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| NOTUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 0.27 | 2.10 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| BLESSUSDT | Erken dönüş | 0.64 | 1.96 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| FARTCOINUSDT | Erken dönüş | 3.10 | 1.84 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| GIGGLEUSDT | Erken dönüş | 2.02 | 1.64 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| PIUSDT | Erken dönüş | 1.01 | 1.51 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| WLFIUSDT | Erken dönüş | 1.91 | 1.64 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| CFXUSDT | Erken dönüş | 1.01 | 2.74 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| MINUSDT | Erken dönüş | 1.74 | 2.13 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| MOVRUSDT | Erken dönüş | 1.56 | 3.64 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ONDOUSDT | Erken dönüş | 2.92 | 3.45 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| POWERUSDT | Erken dönüş | 3.12 | 4.24 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| PUMPUSDT | Erken dönüş | 1.00 | 2.06 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| RVNUSDT | Erken dönüş | 4.98 | 3.21 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; gözlem fiyatı kapanıştan uzaklaştı |
| ETCUSDT | Erken dönüş | 0.79 | 1.59 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| SHIBUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 0.14 | 1.64 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| AEROUSDT | Erken dönüş, Yatay fiyat / hacim artışı | -1.48 | 2.62 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| COOKIEUSDT | Erken dönüş | -0.21 | 2.10 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| HUSDT | Erken dönüş | 5.08 | 2.53 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| LINEAUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 0.51 | 2.24 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| NATIXUSDT | Erken dönüş | 4.14 | 2.00 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| ADAUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 0.39 | 1.98 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| APEXUSDT | Erken dönüş | 1.04 | 1.55 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| BICOUSDT | Erken dönüş | 0.53 | 1.95 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| DOGEUSDT | Erken dönüş | 0.69 | 1.74 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| FLOCKUSDT | Erken dönüş | 0.71 | 1.65 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; gözlem fiyatı grubun izlediği seviyenin altında |
| GALAUSDT | Erken dönüş | 0.63 | 1.57 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| LINKUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 1.01 | 1.70 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| OWLUSDT | Erken dönüş | 11.51 | 1.94 | Yok | yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| POLUSDT | Erken dönüş | 2.73 | 2.00 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| PONSUSDT | Erken dönüş | 3.50 | 1.77 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XPLUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 2.34 | 1.98 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| STRKUSDT | Erken dönüş | 1.25 | 1.76 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| BULLAUSDT | Yeni kırılım | 67.33 | 6.15 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; makas geniş |
| SOILUSDT | Yeni kırılım | 12.68 | 1.70 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş |
| BEATUSDT | Yeni kırılım | 21.59 | 6.31 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| CLANKERUSDT | Yeni kırılım | 7.55 | 2.46 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| TRIAUSDT | Yeni kırılım | 4.83 | 5.56 | Yok | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| CHIPUSDT | Yeni kırılım | 16.43 | 1.66 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş |
| NIGHTUSDT | Yeni kırılım | 7.34 | 3.20 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| YBUSDT | Yeni kırılım | 2.69 | 1.66 | Yok | düşük hacim; gözlem fiyatı grubun izlediği seviyenin altında |
| CVXUSDT | Yatay fiyat / hacim artışı | 2.97 | 2.16 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ENAUSDT | Yatay fiyat / hacim artışı | 3.66 | 1.83 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ZECUSDT | Yatay fiyat / hacim artışı | 3.13 | 1.79 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| PENGUUSDT | Yatay fiyat / hacim artışı | 1.16 | 2.85 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| LUNAMUSDT | Yatay fiyat / hacim artışı | -0.32 | 1.51 | RSI PU teyitli | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| AGRSUSDT | Yatay fiyat / hacim artışı | -7.60 | 2.16 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| M87USDT | Yatay fiyat / hacim artışı | 1.08 | 2.90 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| UNIUSDT | Yatay fiyat / hacim artışı | 3.78 | 1.89 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| PEPEUSDT | Yatay fiyat / hacim artışı | -0.18 | 1.64 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XCXUSDT | Yatay fiyat / hacim artışı | -0.66 | 1.69 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| INJUSDT | Yatay fiyat / hacim artışı | 2.73 | 2.31 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| LITUSDT | Yatay fiyat / hacim artışı | -1.87 | 2.70 | RSI PU teyitli | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| LYNUSDT | Yatay fiyat / hacim artışı | -0.22 | 4.83 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ARUSDT | Yatay fiyat / hacim artışı | 0.76 | 1.73 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| DINUSDT | Yatay fiyat / hacim artışı | -0.09 | 18.44 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| ETHFIUSDT | Yatay fiyat / hacim artışı | 3.42 | 1.75 | RSI PU teyitli | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| FEGUSDT | Yatay fiyat / hacim artışı | 0.24 | 5.44 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| FILUSDT | Yatay fiyat / hacim artışı | -0.40 | 1.87 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| MAPOUSDT | Yatay fiyat / hacim artışı | -0.18 | 3.14 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| SOLUSDT | Yatay fiyat / hacim artışı | 0.28 | 1.76 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| VIRTUALUSDT | Yatay fiyat / hacim artışı | -0.46 | 1.53 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| WELFUSDT | Yatay fiyat / hacim artışı | -1.50 | 1.95 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| WXTUSDT | Yatay fiyat / hacim artışı | -0.02 | 1.96 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| BTCMTUSDT | Yatay fiyat / hacim artışı | 0.03 | 1.62 | RSI PU teyitli | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| CRYPGPTUSDT | Yatay fiyat / hacim artışı | -0.23 | 1.53 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| IOTAUSDT | Yatay fiyat / hacim artışı | -0.51 | 1.82 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| SUIUSDT | Yatay fiyat / hacim artışı | 0.35 | 1.69 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| WBTCUSDT | Yatay fiyat / hacim artışı | -0.24 | 7.27 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| WLDUSDT | Yatay fiyat / hacim artışı | -2.54 | 1.60 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| EVAUSDT | Yatay fiyat / hacim artışı | -0.09 | 1.83 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |

OKX: incelenen 338, aday 90; kapanış 26.10.2026 19:00 TR; fiyat gözlemi 26.10.2026 19:46 TR.
V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |
|---|---|---:|---:|---|---|
| PARTIUSDT | Erken dönüş, Yeni kırılım | 13.73 | 17.55 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| CELOUSDT | Erken dönüş | 2.73 | 7.20 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| DGBUSDT | Erken dönüş | 2.58 | 2.42 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| DOGEUSDT | Erken dönüş | 0.67 | 2.29 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| ETCUSDT | Erken dönüş | 0.95 | 2.04 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| SUSHIUSDT | Erken dönüş | 0.89 | 2.46 | RSI PU teyitli | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| AXSUSDT | Erken dönüş | 1.05 | 1.56 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| LDOUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 2.02 | 1.55 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| RESOLVUSDT | Erken dönüş | 4.18 | 1.84 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| SNXUSDT | Erken dönüş | 0.35 | 1.70 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| TRUMPUSDT | Erken dönüş | 1.81 | 1.83 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| AAVEUSDT | Erken dönüş | 0.18 | 3.06 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| ACEUSDT | Erken dönüş | 1.06 | 2.10 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| AVAXUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 1.10 | 4.94 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| FETUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 0.23 | 2.24 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| JITOSOLUSDT | Erken dönüş | 1.05 | 12.64 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| JTOUSDT | Erken dönüş | 3.01 | 3.55 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| LINKUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 0.83 | 3.96 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| MANAUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 0.84 | 2.73 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| MORPHOUSDT | Erken dönüş | -0.96 | 3.03 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| NEIROUSDT | Erken dönüş | 0.55 | 2.99 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| NIGHTUSDT | Erken dönüş, Yeni kırılım | 7.37 | 3.26 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ONDOUSDT | Erken dönüş | 3.13 | 3.97 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| POLUSDT | Erken dönüş | 2.72 | 9.29 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| PONSUSDT | Erken dönüş | 3.50 | 3.09 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| PUMPUSDT | Erken dönüş | 1.00 | 2.44 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| RENDERUSDT | Erken dönüş | 2.53 | 2.58 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| WLFIUSDT | Erken dönüş | 1.87 | 3.96 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XAPLDUSDT | Erken dönüş | 2.54 | 5.08 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XCRWVUSDT | Erken dönüş | 4.68 | 43.89 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XIRENUSDT | Erken dönüş | 5.85 | 11.39 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XSHAZUSDT | Erken dönüş | 5.18 | 21.81 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ZILUSDT | Erken dönüş | 0.89 | 5.87 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| NOTUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 0.32 | 1.66 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| BIOUSDT | Erken dönüş, Yatay fiyat / hacim artışı | -0.58 | 4.57 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| HMSTRUSDT | Erken dönüş, Yatay fiyat / hacim artışı | -0.42 | 2.17 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| SCRUSDT | Erken dönüş | 1.65 | 2.46 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| VELODROMEUSDT | Erken dönüş | -0.92 | 2.67 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| ADAUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 0.44 | 1.95 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| CFXUSDT | Erken dönüş | 1.03 | 1.94 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| IMXUSDT | Erken dönüş | 1.00 | 1.89 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| PENDLEUSDT | Erken dönüş | 0.35 | 1.59 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| SEIUSDT | Erken dönüş, Yatay fiyat / hacim artışı | -0.04 | 1.69 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| XPLUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 2.32 | 1.92 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| ZENUSDT | Erken dönüş | 0.14 | 1.69 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| BANDUSDT | Erken dönüş | 0.15 | 1.97 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| ONEUSDT | Erken dönüş | 0.91 | 1.63 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| SATSUSDT | Erken dönüş, Yatay fiyat / hacim artışı | -0.05 | 1.51 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| SENTUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 2.63 | 1.52 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| SPACEUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 0.08 | 1.85 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| TRBUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 0.23 | 1.56 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| XTSLAUSDT | Yeni kırılım | 5.86 | 21.02 | Yok | ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| CHIPUSDT | Yeni kırılım | 16.12 | 4.09 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş |
| XAVGOUSDT | Yeni kırılım | 2.41 | 6.25 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XDELLUSDT | Yeni kırılım | 2.58 | 76.97 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XINTCUSDT | Yeni kırılım | 4.24 | 11.19 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XLITEUSDT | Yeni kırılım | 6.77 | 16.23 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XRKLBUSDT | Yeni kırılım | 3.06 | 11.29 | Yok | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| ZECUSDT | Yatay fiyat / hacim artışı | 3.14 | 3.84 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ENAUSDT | Yatay fiyat / hacim artışı | 3.60 | 1.61 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| CVCUSDT | Yatay fiyat / hacim artışı | 3.37 | 2.64 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| VVVUSDT | Yatay fiyat / hacim artışı | 2.23 | 2.12 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ACHUSDT | Yatay fiyat / hacim artışı | -0.45 | 2.29 | RSI PU teyitli | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XLMUSDT | Yatay fiyat / hacim artışı | 0.07 | 2.04 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| MONUSDT | Yatay fiyat / hacim artışı | 4.27 | 1.63 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| UNIUSDT | Yatay fiyat / hacim artışı | 3.67 | 1.72 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| 1INCHUSDT | Yatay fiyat / hacim artışı | 0.07 | 2.34 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ARUSDT | Yatay fiyat / hacim artışı | 0.73 | 2.46 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| BETHUSDT | Yatay fiyat / hacim artışı | -0.64 | 2.59 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ETHFIUSDT | Yatay fiyat / hacim artışı | 3.46 | 2.20 | RSI PU teyitli | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| SOLUSDT | Yatay fiyat / hacim artışı | 0.28 | 2.65 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| SUIUSDT | Yatay fiyat / hacim artışı | 0.41 | 2.13 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| TAOUSDT | Yatay fiyat / hacim artışı | 0.87 | 3.28 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XEWYUSDT | Yatay fiyat / hacim artışı | 0.68 | 2.30 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| QTUMUSDT | Yatay fiyat / hacim artışı | 0.19 | 1.61 | RSI PU teyitli | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| INJUSDT | Yatay fiyat / hacim artışı | 2.98 | 2.10 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| LITUSDT | Yatay fiyat / hacim artışı | -1.91 | 2.73 | RSI PU teyitli | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| STETHUSDT | Yatay fiyat / hacim artışı | -0.25 | 6.23 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| UMAUSDT | Yatay fiyat / hacim artışı | -0.08 | 5.87 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XRPUSDT | Yatay fiyat / hacim artışı | -0.21 | 2.00 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XSKHYUSDT | Yatay fiyat / hacim artışı | 1.29 | 3.00 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| FILUSDT | Yatay fiyat / hacim artışı | -0.39 | 1.61 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| JUPUSDT | Yatay fiyat / hacim artışı | -1.02 | 1.60 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| OKSOLUSDT | Yatay fiyat / hacim artışı | 0.29 | 1.58 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| PEOPLEUSDT | Yatay fiyat / hacim artışı | -0.36 | 1.84 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| TNSRUSDT | Yatay fiyat / hacim artışı | -0.60 | 1.92 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| VIRTUALUSDT | Yatay fiyat / hacim artışı | -0.38 | 1.98 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| WLDUSDT | Yatay fiyat / hacim artışı | -2.50 | 1.92 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| AVNTUSDT | Yatay fiyat / hacim artışı | -1.07 | 1.56 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| CETUSUSDT | Yatay fiyat / hacim artışı | -0.88 | 1.74 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |

İki borsada toplam 134 farklı sembol. Ortak semboller bağımsız iki başarı sayılmaz.

Eşikler başlangıç deneyidir; daha çok aday daha yüksek başarı demek değildir. Yazılım testleri kârlılık kanıtı değildir. Dört saatlik mum ve zamanlayıcı gecikmesi ilk hareketin kaçmasına yol açabilir. SAR yön desteğidir; getiri garantisi değildir.

## Bu döngüde yeni gelenler

PARTIUSDT · OKX
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 26.10.2026 19:46 TR; fiyat 0.037785
24s %13.73; ilgili hacim 17.551x; makas %0.24
ortalamadan uzak; yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

CELOUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.079025
24s %2.73; ilgili hacim 7.1963x; makas %0.09
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

DGBUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.00341
24s %2.58; ilgili hacim 2.4209x; makas %0.23
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

DOGEUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.077275
24s %0.67; ilgili hacim 2.2905x; makas %0.01
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

ETCUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 7.564
24s %0.95; ilgili hacim 2.0404x; makas %0.03
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

SUSHIUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.2016
24s %0.89; ilgili hacim 2.4572x; makas %0.10
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; teyitli RSI pozitif uyumsuzluk desteği

AXSUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.94855
24s %1.05; ilgili hacim 1.5631x; makas %0.03
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

RESOLVUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.01674
24s %4.18; ilgili hacim 1.8381x; makas %0.12
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı

SNXUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.19645
24s %0.35; ilgili hacim 1.7029x; makas %0.15
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

TRUMPUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 1.6845
24s %1.81; ilgili hacim 1.8262x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

AAVEUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 135.3
24s %0.18; ilgili hacim 3.0632x; makas %0.03
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

ACEUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.13928
24s %1.06; ilgili hacim 2.1021x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

AVAXUSDT · OKX
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 8.911
24s %1.10; ilgili hacim 4.9377x; makas %0.02
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

FETUSDT · OKX
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.17425
24s %0.23; ilgili hacim 2.2408x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

JITOSOLUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 132.1
24s %1.05; ilgili hacim 12.639x; makas %0.10
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı

JTOUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.43385
24s %3.01; ilgili hacim 3.5468x; makas %0.02
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

LINKUSDT · OKX
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 11.442
24s %0.83; ilgili hacim 3.9644x; makas %0.02
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

MANAUSDT · OKX
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.078525
24s %0.84; ilgili hacim 2.7314x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

MORPHOUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 2.0663
24s %-0.96; ilgili hacim 3.0264x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

NEIROUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 6.6295e-05
24s %0.55; ilgili hacim 2.9916x; makas %0.08
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

NIGHTUSDT · OKX
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 26.10.2026 19:46 TR; fiyat 0.039667
24s %7.37; ilgili hacim 3.2615x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

ONDOUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.41435
24s %3.13; ilgili hacim 3.9693x; makas %0.02
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

POLUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.090985
24s %2.72; ilgili hacim 9.2886x; makas %0.03
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

PONSUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.244
24s %3.50; ilgili hacim 3.0862x; makas %0.08
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

PUMPUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.0042435
24s %1.00; ilgili hacim 2.436x; makas %0.07
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

RENDERUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 1.7285
24s %2.53; ilgili hacim 2.5823x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

WLFIUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.053395
24s %1.87; ilgili hacim 3.9554x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XAPLDUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 18.425
24s %2.54; ilgili hacim 5.0816x; makas %0.16
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XCRWVUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 56.425
24s %4.68; ilgili hacim 43.892x; makas %0.09
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XIRENUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 26.1
24s %5.85; ilgili hacim 11.395x; makas %0.08
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XSHAZUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 24.15
24s %5.18; ilgili hacim 21.814x; makas %0.17
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ZILUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.0020015
24s %0.89; ilgili hacim 5.8655x; makas %0.35
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; teyitli RSI pozitif uyumsuzluk desteği

NOTUSDT · OKX
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.00036885
24s %0.32; ilgili hacim 1.6631x; makas %0.08
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

BIOUSDT · OKX
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.022215
24s %-0.58; ilgili hacim 4.5743x; makas %0.14
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

HMSTRUSDT · OKX
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.0001404
24s %-0.42; ilgili hacim 2.1746x; makas %0.14
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

SCRUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.019465
24s %1.65; ilgili hacim 2.4571x; makas %0.26
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

VELODROMEUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.029835
24s %-0.92; ilgili hacim 2.6692x; makas %0.23
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

ADAUSDT · OKX
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.20475
24s %0.44; ilgili hacim 1.9467x; makas %0.05
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

CFXUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.04769
24s %1.03; ilgili hacim 1.9388x; makas %0.04
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

PENDLEUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 1.96
24s %0.35; ilgili hacim 1.5869x; makas %0.10
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

SEIUSDT · OKX
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.05231
24s %-0.04; ilgili hacim 1.6886x; makas %0.08
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

XPLUSDT · OKX
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.07329
24s %2.32; ilgili hacim 1.9183x; makas %0.03
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

ZENUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 5.7115
24s %0.14; ilgili hacim 1.6869x; makas %0.09
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

BANDUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.20115
24s %0.15; ilgili hacim 1.9702x; makas %0.25
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

ONEUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:46 TR; fiyat 0.001309
24s %0.91; ilgili hacim 1.6313x; makas %0.15
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

SATSUSDT · OKX
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 1.0028e-08
24s %-0.05; ilgili hacim 1.5068x; makas %0.10
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

SENTUSDT · OKX
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.02053
24s %2.63; ilgili hacim 1.5239x; makas %0.10
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

SPACEUSDT · OKX
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.003631
24s %0.08; ilgili hacim 1.8478x; makas %0.06
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

TRBUSDT · OKX
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 17.235
24s %0.23; ilgili hacim 1.5631x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

XTSLAUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 26.10.2026 19:46 TR; fiyat 395.04
24s %5.86; ilgili hacim 21.022x; makas %0.02
ortalamadan uzak; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

XAVGOUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 26.10.2026 19:46 TR; fiyat 329.41
24s %2.41; ilgili hacim 6.2463x; makas %0.01
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

XDELLUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 26.10.2026 19:46 TR; fiyat 470.56
24s %2.58; ilgili hacim 76.969x; makas %0.10
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

XINTCUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 26.10.2026 19:46 TR; fiyat 90.79
24s %4.24; ilgili hacim 11.191x; makas %0.02
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

XRKLBUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 26.10.2026 19:46 TR; fiyat 54.49
24s %3.06; ilgili hacim 11.287x; makas %0.11
düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

ZECUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 1233
24s %3.14; ilgili hacim 3.8404x; makas %0.01
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ENAUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.20696
24s %3.60; ilgili hacim 1.6055x; makas %0.02
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

CVCUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.024085
24s %3.37; ilgili hacim 2.642x; makas %0.54
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

VVVUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 24.8
24s %2.23; ilgili hacim 2.1204x; makas %0.08
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ACHUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.0050125
24s %-0.45; ilgili hacim 2.2851x; makas %0.14
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

XLMUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.16836
24s %0.07; ilgili hacim 2.0419x; makas %0.01
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

MONUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.02178
24s %4.27; ilgili hacim 1.6343x; makas %0.09
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

UNIUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 7.0455
24s %3.67; ilgili hacim 1.7206x; makas %0.01
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

1INCHUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.088065
24s %0.07; ilgili hacim 2.3378x; makas %0.10
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ARUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 3.3885
24s %0.73; ilgili hacim 2.4578x; makas %0.09
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

BETHUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 2314.4
24s %-0.64; ilgili hacim 2.5924x; makas %0.08
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ETHFIUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.63465
24s %3.46; ilgili hacim 2.2023x; makas %0.02
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

SOLUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 101.09
24s %0.28; ilgili hacim 2.6453x; makas %0.01
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

SUIUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.9113
24s %0.41; ilgili hacim 2.1301x; makas %0.02
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

TAOUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 251.54
24s %0.87; ilgili hacim 3.2787x; makas %0.01
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XEWYUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 152.87
24s %0.68; ilgili hacim 2.3033x; makas %0.05
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

QTUMUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.82625
24s %0.19; ilgili hacim 1.6112x; makas %0.16
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

INJUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 7.815
24s %2.98; ilgili hacim 2.1017x; makas %0.03
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

LITUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 3.0881
24s %-1.91; ilgili hacim 2.7328x; makas %0.01
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

STETHUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 2314
24s %-0.25; ilgili hacim 6.2327x; makas %0.05
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

UMAUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.3538
24s %-0.08; ilgili hacim 5.8714x; makas %0.11
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XRPUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 1.2904
24s %-0.21; ilgili hacim 2.0048x; makas %0.01
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XSKHYUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 141.26
24s %1.29; ilgili hacim 2.9959x; makas %0.04
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

FILUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.9087
24s %-0.39; ilgili hacim 1.6145x; makas %0.02
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

JUPUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.27805
24s %-1.02; ilgili hacim 1.5998x; makas %0.04
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

OKSOLUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 101.03
24s %0.29; ilgili hacim 1.5825x; makas %0.17
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

PEOPLEUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.007491
24s %-0.36; ilgili hacim 1.8414x; makas %0.05
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

TNSRUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.02956
24s %-0.60; ilgili hacim 1.9228x; makas %0.20
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

VIRTUALUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.6163
24s %-0.38; ilgili hacim 1.977x; makas %0.03
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

WLDUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.43865
24s %-2.50; ilgili hacim 1.9164x; makas %0.02
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

AVNTUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.11117
24s %-1.07; ilgili hacim 1.5612x; makas %0.10
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

CETUSUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:46 TR; fiyat 0.021175
24s %-0.88; ilgili hacim 1.7351x; makas %0.14
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

PARTIUSDT · MEXC
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 26.10.2026 19:49 TR; fiyat 0.038145
24s %13.77; ilgili hacim 1.5787x; makas %0.24
ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

TRUMPUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 1.6815
24s %1.81; ilgili hacim 2.0507x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

NOTUSDT · MEXC
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.0003695
24s %0.27; ilgili hacim 2.0971x; makas %0.32
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

BLESSUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.008177
24s %0.64; ilgili hacim 1.9575x; makas %0.34
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

FARTCOINUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.12729
24s %3.10; ilgili hacim 1.8401x; makas %0.09
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

GIGGLEUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 30.095
24s %2.02; ilgili hacim 1.6426x; makas %0.03
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

PIUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.07653
24s %1.01; ilgili hacim 1.5121x; makas %0.10
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

WLFIUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.05339
24s %1.91; ilgili hacim 1.6414x; makas %0.07
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

CFXUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.04764
24s %1.01; ilgili hacim 2.7414x; makas %0.08
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

MINUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.0031095
24s %1.74; ilgili hacim 2.1317x; makas %0.03
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı

MOVRUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 1.0922
24s %1.56; ilgili hacim 3.642x; makas %0.36
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

POWERUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.07827
24s %3.12; ilgili hacim 4.2384x; makas %0.08
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

PUMPUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.0042405
24s %1.00; ilgili hacim 2.0584x; makas %0.02
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

RVNUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.001341
24s %4.98; ilgili hacim 3.2089x; makas %0.75
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; gözlem fiyatı kapanıştan uzaklaştı

ETCUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 7.565
24s %0.79; ilgili hacim 1.5944x; makas %0.13
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

SHIBUSDT · MEXC
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 4.8515e-06
24s %0.14; ilgili hacim 1.6385x; makas %0.10
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

AEROUSDT · MEXC
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.68045
24s %-1.48; ilgili hacim 2.6168x; makas %0.13
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

COOKIEUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.0088385
24s %-0.21; ilgili hacim 2.1024x; makas %0.21
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

HUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.05535
24s %5.08; ilgili hacim 2.5346x; makas %0.25
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

LINEAUSDT · MEXC
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.002518
24s %0.51; ilgili hacim 2.2381x; makas %0.08
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

ADAUSDT · MEXC
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.20455
24s %0.39; ilgili hacim 1.9847x; makas %0.05
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

APEXUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.2207
24s %1.04; ilgili hacim 1.548x; makas %0.27
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

BICOUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.01492
24s %0.53; ilgili hacim 1.9462x; makas %0.13
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

DOGEUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.077185
24s %0.69; ilgili hacim 1.7399x; makas %0.01
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

FLOCKUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.040705
24s %0.71; ilgili hacim 1.6497x; makas %0.96
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; gözlem fiyatı grubun izlediği seviyenin altında

GALAUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.0017415
24s %0.63; ilgili hacim 1.5685x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; teyitli RSI pozitif uyumsuzluk desteği

LINKUSDT · MEXC
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 11.434
24s %1.01; ilgili hacim 1.6982x; makas %0.03
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

OWLUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.0005305
24s %11.51; ilgili hacim 1.9369x; makas %0.26
yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

POLUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.09099
24s %2.73; ilgili hacim 1.9972x; makas %0.02
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

PONSUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.24415
24s %3.50; ilgili hacim 1.7683x; makas %0.01
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XPLUSDT · MEXC
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.07326
24s %2.34; ilgili hacim 1.9772x; makas %0.03
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

STRKUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 19:49 TR; fiyat 0.045595
24s %1.25; ilgili hacim 1.7584x; makas %0.02
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

SOILUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 26.10.2026 19:49 TR; fiyat 0.12826
24s %12.68; ilgili hacim 1.7032x; makas %1.62
ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş

BEATUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 26.10.2026 19:49 TR; fiyat 0.08362
24s %21.59; ilgili hacim 6.3132x; makas %0.10
ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

CLANKERUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 26.10.2026 19:49 TR; fiyat 13.64
24s %7.55; ilgili hacim 2.4624x; makas %0.29
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

TRIAUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 26.10.2026 19:49 TR; fiyat 0.002795
24s %4.83; ilgili hacim 5.5603x; makas %0.36
düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

YBUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 26.10.2026 19:49 TR; fiyat 0.06585
24s %2.69; ilgili hacim 1.6621x; makas %0.24
düşük hacim; gözlem fiyatı grubun izlediği seviyenin altında

CVXUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 2.4655
24s %2.97; ilgili hacim 2.1606x; makas %0.04
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ENAUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.20664
24s %3.66; ilgili hacim 1.8332x; makas %0.07
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ZECUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 1231.7
24s %3.13; ilgili hacim 1.7906x; makas %0.01
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

LUNAMUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.00034772
24s %-0.32; ilgili hacim 1.515x; makas %0.53
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; teyitli RSI pozitif uyumsuzluk desteği

AGRSUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.24275
24s %-7.60; ilgili hacim 2.1613x; makas %1.61
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

M87USDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 1.668e-05
24s %1.08; ilgili hacim 2.9032x; makas %0.12
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

UNIUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 7.0305
24s %3.78; ilgili hacim 1.8928x; makas %0.04
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

PEPEUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 4.377e-06
24s %-0.18; ilgili hacim 1.644x; makas %0.09
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XCXUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.0022715
24s %-0.66; ilgili hacim 1.6895x; makas %0.38
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

INJUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 7.808
24s %2.73; ilgili hacim 2.3114x; makas %0.08
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

LITUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 3.0799
24s %-1.87; ilgili hacim 2.6979x; makas %0.13
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

ARUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 3.384
24s %0.76; ilgili hacim 1.7273x; makas %0.06
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

DINUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.0045765
24s %-0.09; ilgili hacim 18.445x; makas %0.68
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

ETHFIUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.63415
24s %3.42; ilgili hacim 1.7461x; makas %0.02
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

FEGUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 2.9635e-05
24s %0.24; ilgili hacim 5.4364x; makas %0.44
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

FILUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.90795
24s %-0.40; ilgili hacim 1.8662x; makas %0.01
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

MAPOUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.0012235
24s %-0.18; ilgili hacim 3.1365x; makas %0.40
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

SOLUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 101.09
24s %0.28; ilgili hacim 1.764x; makas %0.01
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

VIRTUALUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.6157
24s %-0.46; ilgili hacim 1.5264x; makas %0.03
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

WELFUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.06665
24s %-1.50; ilgili hacim 1.951x; makas %0.18
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

WXTUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.017994
24s %-0.02; ilgili hacim 1.9616x; makas %0.03
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

BTCMTUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.6551
24s %0.03; ilgili hacim 1.6185x; makas %0.70
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; teyitli RSI pozitif uyumsuzluk desteği

CRYPGPTUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.0909
24s %-0.23; ilgili hacim 1.5336x; makas %0.15
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

IOTAUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.042295
24s %-0.51; ilgili hacim 1.8196x; makas %0.17
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

SUIUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.91015
24s %0.35; ilgili hacim 1.694x; makas %0.01
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

WBTCUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 79828
24s %-0.24; ilgili hacim 7.2701x; makas %0.00
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

WLDUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 0.43745
24s %-2.54; ilgili hacim 1.5991x; makas %0.02
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

EVAUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 19:49 TR; fiyat 43.915
24s %-0.09; ilgili hacim 1.8305x; makas %0.48
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

## V5 gerçek gözlemden sonraki sonuçlar

Her borsa/token için ilk gerçek fiyat bir ana kayıttır. Gruplar örtüşebilir; grup sayıları bağımsız başarı gibi toplanmaz. Bir gruba sonradan ilk giriş, o andaki gerçek fiyatla ayrıca ölçülür. Getiriler ücret/kayma dahil değildir; eksik ölçüm boş kalır.

| Coin | Borsa | İlk grup | Gerçek gözlem TR | Fiyat | 12s % | 24s % | 48s % |
|---|---|---|---|---:|---:|---:|---:|
| GALFTUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.8066 | — | — | — |
| XQCOMUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 177.525 | — | — | — |
| XGOOGLUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 322.39 | — | — | — |
| ARBUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.170775 | — | — | — |
| ASTRUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.0064895 | — | — | — |
| LUNAUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.041805 | — | — | — |
| METUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.31295 | — | — | — |
| XLITEUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 780.53 | — | — | — |
| SPKUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.01838 | — | — | — |
| XLRCXUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 234.725 | — | — | — |
| CRVUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.35035 | — | — | — |
| XASMLUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 1596.95 | — | — | — |
| IMXUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.1405 | — | — | — |
| CHIPUSDT | OKX | Yeni kırılım | 26.10.2026 15:39 | 0.049285 | — | — | — |
| PYTHUSDT | OKX | Yeni kırılım | 26.10.2026 15:39 | 0.075005 | — | — | — |
| DOODUSDT | OKX | Yeni kırılım | 26.10.2026 15:39 | 0.0023005 | — | — | — |
| DYDXUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 15:39 | 0.108095 | — | — | — |
| LDOUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 15:39 | 0.36995 | — | — | — |
| BICOUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 15:39 | 0.014945 | — | — | — |
| ILVUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 15:39 | 3.099 | — | — | — |
| SPCMUSDT | MEXC | Tutunma | 26.10.2026 15:43 | 0.0008465 | — | — | — |
| TAUSDT | MEXC | Tutunma | 26.10.2026 15:43 | 0.05873 | — | — | — |
| UMXUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.049465 | — | — | — |
| CAKEUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 2.1035 | — | — | — |
| ARBUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.170855 | — | — | — |
| BANKUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.02771 | — | — | — |
| NIGHTUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.038025 | — | — | — |
| NOMUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.001673 | — | — | — |
| SOONUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.3149 | — | — | — |
| UPCUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.12305 | — | — | — |
| GHXUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.009755 | — | — | — |
| TAGUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.0005201 | — | — | — |
| HYPEUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 77.435 | — | — | — |
| METUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.31225 | — | — | — |
| ONDOUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.413185 | — | — | — |
| SAGAUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.01787 | — | — | — |
| 4USDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.01169 | — | — | — |
| NATIXUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.000163895 | — | — | — |
| RUNEUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.6316 | — | — | — |
| MIUUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 9.35e-10 | — | — | — |
| BULLAUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 0.139074 | — | — | — |
| NEXUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 8.0765e-07 | — | — | — |
| PLAYUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 0.017415 | — | — | — |
| QNTUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 220.56 | — | — | — |
| CHIPUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 0.048875 | — | — | — |
| PYTHUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 0.075095 | — | — | — |
| DGMAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.01041 | — | — | — |
| PENGUUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.007525 | — | — | — |
| SHMUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 3.845e-05 | — | — | — |
| HMNDUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.0026355 | — | — | — |
| LYNUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.01345 | — | — | — |
| XLMUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.16945 | — | — | — |
| TRXUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.3313 | — | — | — |
| MONUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.021545 | — | — | — |
| DOGSUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 3.596e-05 | — | — | — |
| PARTIUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.037785 | — | — | — |
| CELOUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.079025 | — | — | — |
| DGBUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.00341 | — | — | — |
| DOGEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.077275 | — | — | — |
| ETCUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 7.564 | — | — | — |
| SUSHIUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.2016 | — | — | — |
| AXSUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.94855 | — | — | — |
| RESOLVUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.01674 | — | — | — |
| SNXUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.19645 | — | — | — |
| TRUMPUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 1.6845 | — | — | — |
| AAVEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 135.3 | — | — | — |
| ACEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.139285 | — | — | — |
| AVAXUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 8.911 | — | — | — |
| FETUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.17425 | — | — | — |
| JITOSOLUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 132.105 | — | — | — |
| JTOUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.43385 | — | — | — |
| LINKUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 11.442 | — | — | — |
| MANAUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.078525 | — | — | — |
| MORPHOUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 2.06625 | — | — | — |
| NEIROUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 6.6295e-05 | — | — | — |
| NIGHTUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.0396665 | — | — | — |
| ONDOUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.41435 | — | — | — |
| POLUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.090985 | — | — | — |
| PONSUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.244 | — | — | — |
| PUMPUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.0042435 | — | — | — |
| RENDERUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 1.7285 | — | — | — |
| WLFIUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.053395 | — | — | — |
| XAPLDUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 18.425 | — | — | — |
| XCRWVUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 56.425 | — | — | — |
| XIRENUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 26.1 | — | — | — |
| XSHAZUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 24.15 | — | — | — |
| ZILUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.0020015 | — | — | — |
| NOTUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.00036885 | — | — | — |
| BIOUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.022215 | — | — | — |
| HMSTRUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.0001404 | — | — | — |
| SCRUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.019465 | — | — | — |
| VELODROMEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.029835 | — | — | — |
| ADAUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.20475 | — | — | — |
| CFXUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.04769 | — | — | — |
| PENDLEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 1.96 | — | — | — |
| SEIUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.05231 | — | — | — |
| XPLUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.07329 | — | — | — |
| ZENUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 5.7115 | — | — | — |
| BANDUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.20115 | — | — | — |
| ONEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.001309 | — | — | — |
| SATSUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 1.0028e-08 | — | — | — |
| SENTUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.02053 | — | — | — |
| SPACEUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 0.003631 | — | — | — |
| TRBUSDT | OKX | Erken dönüş | 26.10.2026 19:46 | 17.235 | — | — | — |
| XTSLAUSDT | OKX | Yeni kırılım | 26.10.2026 19:46 | 395.045 | — | — | — |
| XAVGOUSDT | OKX | Yeni kırılım | 26.10.2026 19:46 | 329.41 | — | — | — |
| XDELLUSDT | OKX | Yeni kırılım | 26.10.2026 19:46 | 470.555 | — | — | — |
| XINTCUSDT | OKX | Yeni kırılım | 26.10.2026 19:46 | 90.79 | — | — | — |
| XRKLBUSDT | OKX | Yeni kırılım | 26.10.2026 19:46 | 54.49 | — | — | — |
| ZECUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 1232.965 | — | — | — |
| ENAUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.206955 | — | — | — |
| CVCUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.024085 | — | — | — |
| VVVUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 24.8 | — | — | — |
| ACHUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.0050125 | — | — | — |
| XLMUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.16836 | — | — | — |
| MONUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.02178 | — | — | — |
| UNIUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 7.0455 | — | — | — |
| 1INCHUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.088065 | — | — | — |
| ARUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 3.3885 | — | — | — |
| BETHUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 2314.35 | — | — | — |
| ETHFIUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.63465 | — | — | — |
| SOLUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 101.085 | — | — | — |
| SUIUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.9113 | — | — | — |
| TAOUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 251.535 | — | — | — |
| XEWYUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 152.865 | — | — | — |
| QTUMUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.82625 | — | — | — |
| INJUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 7.815 | — | — | — |
| LITUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 3.08815 | — | — | — |
| STETHUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 2314.045 | — | — | — |
| UMAUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.3538 | — | — | — |
| XRPUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 1.29045 | — | — | — |
| XSKHYUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 141.265 | — | — | — |
| FILUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.9087 | — | — | — |
| JUPUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.27805 | — | — | — |
| OKSOLUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 101.025 | — | — | — |
| PEOPLEUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.007491 | — | — | — |
| TNSRUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.02956 | — | — | — |
| VIRTUALUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.6163 | — | — | — |
| WLDUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.43865 | — | — | — |
| AVNTUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.111175 | — | — | — |
| CETUSUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 19:46 | 0.021175 | — | — | — |
| PARTIUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.038145 | — | — | — |
| TRUMPUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 1.6815 | — | — | — |
| NOTUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0003695 | — | — | — |
| BLESSUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.008177 | — | — | — |
| FARTCOINUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.127285 | — | — | — |
| GIGGLEUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 30.095 | — | — | — |
| PIUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.07653 | — | — | — |
| WLFIUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.05339 | — | — | — |
| CFXUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.04764 | — | — | — |
| MINUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0031095 | — | — | — |
| MOVRUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 1.09225 | — | — | — |
| POWERUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.07827 | — | — | — |
| PUMPUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0042405 | — | — | — |
| RVNUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.001341 | — | — | — |
| ETCUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 7.565 | — | — | — |
| SHIBUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 4.8515e-06 | — | — | — |
| AEROUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.68045 | — | — | — |
| COOKIEUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0088385 | — | — | — |
| HUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.05535 | — | — | — |
| LINEAUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.002518 | — | — | — |
| ADAUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.20455 | — | — | — |
| APEXUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.2207 | — | — | — |
| BICOUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.01492 | — | — | — |
| DOGEUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.077185 | — | — | — |
| FLOCKUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.040705 | — | — | — |
| GALAUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0017415 | — | — | — |
| LINKUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 11.4335 | — | — | — |
| OWLUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.0005305 | — | — | — |
| POLUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.09099 | — | — | — |
| PONSUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.244153 | — | — | — |
| XPLUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.07326 | — | — | — |
| STRKUSDT | MEXC | Erken dönüş | 26.10.2026 19:49 | 0.045595 | — | — | — |
| SOILUSDT | MEXC | Yeni kırılım | 26.10.2026 19:49 | 0.12826 | — | — | — |
| BEATUSDT | MEXC | Yeni kırılım | 26.10.2026 19:49 | 0.08362 | — | — | — |
| CLANKERUSDT | MEXC | Yeni kırılım | 26.10.2026 19:49 | 13.64 | — | — | — |
| TRIAUSDT | MEXC | Yeni kırılım | 26.10.2026 19:49 | 0.002795 | — | — | — |
| YBUSDT | MEXC | Yeni kırılım | 26.10.2026 19:49 | 0.06585 | — | — | — |
| CVXUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 2.4655 | — | — | — |
| ENAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.20664 | — | — | — |
| ZECUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 1231.74 | — | — | — |
| LUNAMUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.00034772 | — | — | — |
| AGRSUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.24275 | — | — | — |
| M87USDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 1.668e-05 | — | — | — |
| UNIUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 7.0305 | — | — | — |
| PEPEUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 4.377e-06 | — | — | — |
| XCXUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.0022715 | — | — | — |
| INJUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 7.808 | — | — | — |
| LITUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 3.0799 | — | — | — |
| ARUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 3.384 | — | — | — |
| DINUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.0045765 | — | — | — |
| ETHFIUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.63415 | — | — | — |
| FEGUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 2.9635e-05 | — | — | — |
| FILUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.90795 | — | — | — |
| MAPOUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.00122355 | — | — | — |
| SOLUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 101.085 | — | — | — |
| VIRTUALUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.6157 | — | — | — |
| WELFUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.06665 | — | — | — |
| WXTUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.0179935 | — | — | — |
| BTCMTUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.6551 | — | — | — |
| CRYPGPTUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.0909 | — | — | — |
| IOTAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.042295 | — | — | — |
| SUIUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.91015 | — | — | — |
| WBTCUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 79828.225 | — | — | — |
| WLDUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 0.43745 | — | — | — |
| EVAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 19:49 | 43.915 | — | — | — |

### Grupların ayrı ölçümleri

| Grup | Borsa | Süre | Ölçülen / kayıt | Medyan % | BTC üstü puan | Kontrol üstü puan |
|---|---|---:|---:|---:|---:|---:|
| Erken dönüş | MEXC | 12s | 0/49 | — | — | — |
| Erken dönüş | MEXC | 24s | 0/49 | — | — | — |
| Erken dönüş | MEXC | 48s | 0/49 | — | — | — |
| Erken dönüş | OKX | 12s | 0/63 | — | — | — |
| Erken dönüş | OKX | 24s | 0/63 | — | — | — |
| Erken dönüş | OKX | 48s | 0/63 | — | — | — |
| Yatay fiyat / hacim artışı | MEXC | 12s | 0/45 | — | — | — |
| Yatay fiyat / hacim artışı | MEXC | 24s | 0/45 | — | — | — |
| Yatay fiyat / hacim artışı | MEXC | 48s | 0/45 | — | — | — |
| Yatay fiyat / hacim artışı | OKX | 12s | 0/51 | — | — | — |
| Yatay fiyat / hacim artışı | OKX | 24s | 0/51 | — | — | — |
| Yatay fiyat / hacim artışı | OKX | 48s | 0/51 | — | — | — |
| Yeni kırılım | MEXC | 12s | 0/15 | — | — | — |
| Yeni kırılım | MEXC | 24s | 0/15 | — | — | — |
| Yeni kırılım | MEXC | 48s | 0/15 | — | — | — |
| Yeni kırılım | OKX | 12s | 0/12 | — | — | — |
| Yeni kırılım | OKX | 24s | 0/12 | — | — | — |
| Yeni kırılım | OKX | 48s | 0/12 | — | — | — |
| Tutunma | MEXC | 12s | 0/2 | — | — | — |
| Tutunma | MEXC | 24s | 0/2 | — | — | — |
| Tutunma | MEXC | 48s | 0/2 | — | — | — |

## Önceki V4 kayıtları — yeni kayıt alınmıyor

Eski gerçek giriş fiyatları korunur; bunlar yeni grupların geçmişte yakaladığı örnekler değildir. 12/24/48s ölçümleri ayrı sürdürülür.

## Gerçek gözlemden sonraki ölçümler

Her sürüm ve borsanın ilk gerçek alış/satış orta fiyatı ayrı kaydedilir. Aynı coin grup değiştirse de yeni bağımsız örnek sayılmaz. Hedef saatten sonraki ilk dakika kapanışı kullanılır; gecikme 60 saniyeden küçüktür. Ücret/kayma dahil net kâr değildir. Henüz oluşmamış veya eksik ölçümler boş kalır.

8 borsa kaydı, 8 farklı sembol. Ortak semboller iki bağımsız başarı gibi toplanmaz.

| Borsa | Süre | Ölçülen | Medyan % | BTC üstü puan | Kontrol üstü puan | Kontrol ölçülen |
|---|---:|---:|---:|---:|---:|---:|
| MEXC | 12s | 5/8 | -1.21 | -1.18 | -1.83 | 5 |
| MEXC | 24s | 0/8 | — | — | — | 0 |
| MEXC | 48s | 0/8 | — | — | — | 0 |

| Coin | Borsa | İlk grup | Gerçek gözlem TR | Referans fiyat | 12s % | 24s % | 48s % |
|---|---|---|---|---:|---:|---:|---:|
| BULLAUSDT | MEXC | Yeni kırılım | 26.10.2026 11:48 | 0.1130635 | — | — | — |
| CAPUSDT | MEXC | Tutunma | 26.10.2026 00:23 | 0.10956 | -21.28 | — | — |
| CPHUSDT | MEXC | Tutunma | 26.10.2026 11:48 | 0.0035595 | — | — | — |
| GBCKUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.0048565 | -0.59 | — | — |
| MIUUSDT | MEXC | Yeni kırılım | 26.10.2026 03:52 | 8.85e-10 | 5.08 | — | — |
| NEXUSDT | MEXC | Yeni kırılım | 26.10.2026 11:48 | 7.95e-07 | — | — | — |
| STONKSUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.0020883 | -19.28 | — | — |
| TAUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.06203 | -1.21 | — | — |

Karşılaştırma için en az 1–2 haftalık gerçek kayıt beklenir. Gruplar, borsalar ve ortak coinler dikkate alınmadan bir kazanma oranı iddia edilmez.


<!-- coin-priority-raw:end -->

</details>
