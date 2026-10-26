# Coin Tarama 3 — kısa öncelik listesi

Son kontrol: 26.10.2026 23:37 TR.

Geniş havuz: 20 borsa kaydı / 19 sembol. İşlem koşulu elemesini geçen: 2 farklı sembol. Bildirim ve üst liste: en fazla 5 farklı coin.

**Öncelik, kârlılık veya güvenli işlem garantisi değildir.** Hacim/makas, güncel fiyat, yapı ve uzama kontrollerinden geçenler sıralanır. Yalnız yatay hacim hazırlığı bildirilmez. Aday yoksa liste doldurulmaz.

| Coin | Fiyat borsası | Geçen borsalar | Grup | Gerçek gözlem TR | Fiyat | Makas % | Yapı mesafesi % |
|---|---|---|---|---|---:|---:|---:|
| COMPUSDT | MEXC | MEXC, OKX | Erken dönüş | 26.10.2026 23:37 | 21.79 | 0.09 | 4.29 |
| ARXUSDT | MEXC | MEXC | Erken dönüş | 26.10.2026 23:37 | 0.2252 | 0.18 | 10.00 |

Sıralama: en çok 4x sayılan göreli hacim, kapanış konumu, dar makas ve aynı borsanın hacmi. Farklı borsaların hacimleri toplanmaz. Bu sıra başarı olasılığı değildir.

Başlangıç elemesi: en az 100.000 USDT kapalı 24s hacim, en çok %0,5 makas, izlenen seviyeyi koruyan güncel fiyat, kapanıştan en çok 1 ATR uzaklık, EMA20 üstüne en çok 2,5 ATR uzama ve yapı referansına en çok %12 mesafe. 20x üzeri hacim ayrıca incelemede kalır. Bunlar daha iyi sonuç verdiği kanıtlanmış yeni strateji eşikleri değildir.

Aynı sembol tek satırda gösterilir; yalnız elemeden geçen borsalar listelenir. Sembol eşleşmesi bağımsız kontrat kimliği teyidi değildir. Geniş havuz ve eski ölçümler korunur. [Tanınan OKX hisse tokenlerinin kaynağı](https://www.okx.com/help/okx-to-list-tokenized-stocks-for-trading). Liste 2026-10-26 tarihinde kontrol edildi; yeni hisse tokenlerinin eklenmesi gerekebilir.

## Eleme özeti

- 4 borsa kaydı: EMA20 uzaklığı fazla veya bilinmiyor
- 2 borsa kaydı: olağandışı hacim katsayısı; ayrıca inceleme
- 6 borsa kaydı: yalnız hazırlık; ek teknik teyit yok
- 3 borsa kaydı: güncel fiyat kapanıştan uzak veya veri eksik
- 6 borsa kaydı: yapı bozulma mesafesi geniş veya bilinmiyor
- 7 borsa kaydı: makas geniş veya bilinmiyor
- 4 borsa kaydı: izlenen seviye kaybedilmiş veya bilinmiyor
- 10 borsa kaydı: hacim 100.000 USDT altında

Bir kayıtta birden fazla neden olabilir; sayılar bağımsız coinler gibi toplanmaz.
Sıralama sınırı dışında kalan uygun sembol: 0.


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
| COMPUSDT | MEXC | 26.10.2026 23:37 | 21.79 | — | — | — |
| ARXUSDT | MEXC | 26.10.2026 23:37 | 0.2252 | — | — | — |

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

MEXC: incelenen 1029, aday 15; kapanış 26.10.2026 23:00 TR; fiyat gözlemi 26.10.2026 23:36 TR.
V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |
|---|---|---:|---:|---|---|
| BULLAUSDT | Tutunma | 75.15 | 6.15 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; makas geniş |
| MIUUSDT | Tutunma | 16.67 | 10.54 | Yok | 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; makas geniş |
| YBUSDT | Tutunma | 2.12 | 1.66 | Yok | düşük hacim; gözlem fiyatı grubun izlediği seviyenin altında |
| APTMUSDT | Erken dönüş | 1.01 | 2.38 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| QUSDT | Erken dönüş | 83.81 | 6.93 | RSI PU teyitli | 24 saatlik yükseliş yüksek; yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; gözlem fiyatı kapanıştan uzaklaştı |
| ARXUSDT | Erken dönüş | 3.98 | 3.60 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| COMPUSDT | Erken dönüş | -0.41 | 3.84 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| SYMMUSDT | Yeni kırılım | 8.56 | 41.06 | Yok | düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı |
| VERONAUSDT | Yeni kırılım | 24.19 | 93.99 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı kapanıştan uzaklaştı |
| JEANPHILUSDT | Yeni kırılım | 44.78 | 1.59 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; yapı bozulma mesafesi geniş; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| NATIXUSDT | Yeni kırılım | 16.76 | 1.50 | Yok | yapı bozulma mesafesi geniş; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş |
| FUELUSDT | Yatay fiyat / hacim artışı | 0.48 | 5.43 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| TIAUSDT | Yatay fiyat / hacim artışı | 1.89 | 2.17 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| BTCMTUSDT | Yatay fiyat / hacim artışı | -0.33 | 1.67 | RSI PU teyitli | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ALEXUSDT | Yatay fiyat / hacim artışı | 5.83 | 1.76 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |

OKX: incelenen 339, aday 5; kapanış 26.10.2026 23:00 TR; fiyat gözlemi 26.10.2026 23:32 TR.
V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |
|---|---|---:|---:|---|---|
| SENTUSDT | Erken dönüş | 3.48 | 1.75 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| WUSDT | Erken dönüş | 2.48 | 1.92 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| COMPUSDT | Erken dönüş | -0.51 | 2.46 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| FLUIDUSDT | Yatay fiyat / hacim artışı | -2.11 | 1.91 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| LQTYUSDT | Yatay fiyat / hacim artışı | -2.36 | 14.69 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |

İki borsada toplam 19 farklı sembol. Ortak semboller bağımsız iki başarı sayılmaz.

Eşikler başlangıç deneyidir; daha çok aday daha yüksek başarı demek değildir. Yazılım testleri kârlılık kanıtı değildir. Dört saatlik mum ve zamanlayıcı gecikmesi ilk hareketin kaçmasına yol açabilir. SAR yön desteğidir; getiri garantisi değildir.

## Bu döngüde yeni gelenler

WUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 23:32 TR; fiyat 0.012345
24s %2.48; ilgili hacim 1.924x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

COMPUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 23:32 TR; fiyat 21.755
24s %-0.51; ilgili hacim 2.4593x; makas %0.14
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

FLUIDUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 23:32 TR; fiyat 2.188
24s %-2.11; ilgili hacim 1.9127x; makas %0.16
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

LQTYUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 23:32 TR; fiyat 0.1938
24s %-2.36; ilgili hacim 14.687x; makas %0.21
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

APTMUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 23:36 TR; fiyat 0.05199
24s %1.01; ilgili hacim 2.3784x; makas %1.00
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

QUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 23:36 TR; fiyat 0.13414
24s %83.81; ilgili hacim 6.9311x; makas %1.03
24 saatlik yükseliş yüksek; yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; gözlem fiyatı kapanıştan uzaklaştı; teyitli RSI pozitif uyumsuzluk desteği

ARXUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 23:36 TR; fiyat 0.22615
24s %3.98; ilgili hacim 3.6x; makas %0.22
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

COMPUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 23:36 TR; fiyat 21.79
24s %-0.41; ilgili hacim 3.8373x; makas %0.09
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

SYMMUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 26.10.2026 23:36 TR; fiyat 0.0307
24s %8.56; ilgili hacim 41.056x; makas %0.65
düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş; gözlem fiyatı grubun izlediği seviyenin altında; gözlem fiyatı kapanıştan uzaklaştı

VERONAUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 26.10.2026 23:36 TR; fiyat 0.13405
24s %24.19; ilgili hacim 93.99x; makas %0.22
ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı kapanıştan uzaklaştı

JEANPHILUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 26.10.2026 23:36 TR; fiyat 0.0045445
24s %44.78; ilgili hacim 1.5852x; makas %0.02
24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; yapı bozulma mesafesi geniş; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

FUELUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 23:36 TR; fiyat 0.00079595
24s %0.48; ilgili hacim 5.4345x; makas %0.01
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

TIAUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 23:36 TR; fiyat 0.54485
24s %1.89; ilgili hacim 2.1733x; makas %0.17
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ALEXUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 23:36 TR; fiyat 0.0038645
24s %5.83; ilgili hacim 1.7647x; makas %0.39
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
| WUSDT | OKX | Erken dönüş | 26.10.2026 23:32 | 0.012345 | — | — | — |
| COMPUSDT | OKX | Erken dönüş | 26.10.2026 23:32 | 21.755 | — | — | — |
| FLUIDUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 23:32 | 2.188 | — | — | — |
| LQTYUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 23:32 | 0.1938 | — | — | — |
| APTMUSDT | MEXC | Erken dönüş | 26.10.2026 23:36 | 0.05199 | — | — | — |
| QUSDT | MEXC | Erken dönüş | 26.10.2026 23:36 | 0.1341405 | — | — | — |
| ARXUSDT | MEXC | Erken dönüş | 26.10.2026 23:36 | 0.22615 | — | — | — |
| COMPUSDT | MEXC | Erken dönüş | 26.10.2026 23:36 | 21.79 | — | — | — |
| SYMMUSDT | MEXC | Yeni kırılım | 26.10.2026 23:36 | 0.0307 | — | — | — |
| VERONAUSDT | MEXC | Yeni kırılım | 26.10.2026 23:36 | 0.13405 | — | — | — |
| JEANPHILUSDT | MEXC | Yeni kırılım | 26.10.2026 23:36 | 0.0045445 | — | — | — |
| FUELUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 23:36 | 0.00079595 | — | — | — |
| TIAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 23:36 | 0.54485 | — | — | — |
| ALEXUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 23:36 | 0.0038645 | — | — | — |

### Grupların ayrı ölçümleri

| Grup | Borsa | Süre | Ölçülen / kayıt | Medyan % | BTC üstü puan | Kontrol üstü puan |
|---|---|---:|---:|---:|---:|---:|
| Erken dönüş | MEXC | 12s | 0/53 | — | — | — |
| Erken dönüş | MEXC | 24s | 0/53 | — | — | — |
| Erken dönüş | MEXC | 48s | 0/53 | — | — | — |
| Erken dönüş | OKX | 12s | 0/65 | — | — | — |
| Erken dönüş | OKX | 24s | 0/65 | — | — | — |
| Erken dönüş | OKX | 48s | 0/65 | — | — | — |
| Yatay fiyat / hacim artışı | MEXC | 12s | 0/48 | — | — | — |
| Yatay fiyat / hacim artışı | MEXC | 24s | 0/48 | — | — | — |
| Yatay fiyat / hacim artışı | MEXC | 48s | 0/48 | — | — | — |
| Yatay fiyat / hacim artışı | OKX | 12s | 0/53 | — | — | — |
| Yatay fiyat / hacim artışı | OKX | 24s | 0/53 | — | — | — |
| Yatay fiyat / hacim artışı | OKX | 48s | 0/53 | — | — | — |
| Yeni kırılım | MEXC | 12s | 0/19 | — | — | — |
| Yeni kırılım | MEXC | 24s | 0/19 | — | — | — |
| Yeni kırılım | MEXC | 48s | 0/19 | — | — | — |
| Yeni kırılım | OKX | 12s | 0/12 | — | — | — |
| Yeni kırılım | OKX | 24s | 0/12 | — | — | — |
| Yeni kırılım | OKX | 48s | 0/12 | — | — | — |
| Tutunma | MEXC | 12s | 0/5 | — | — | — |
| Tutunma | MEXC | 24s | 0/5 | — | — | — |
| Tutunma | MEXC | 48s | 0/5 | — | — | — |

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
