# Coin Tarama 3 — kısa öncelik listesi

Son kontrol: 27.10.2026 03:44 TR.

Geniş havuz: 50 borsa kaydı / 49 sembol. İşlem koşulu elemesini geçen: 4 farklı sembol. Bildirim ve üst liste: en fazla 5 farklı coin.

**Öncelik, kârlılık veya güvenli işlem garantisi değildir.** Hacim/makas, güncel fiyat, yapı ve uzama kontrollerinden geçenler sıralanır. Yalnız yatay hacim hazırlığı bildirilmez. Aday yoksa liste doldurulmaz.

| Coin | Fiyat borsası | Geçen borsalar | Grup | Gerçek gözlem TR | Fiyat | Makas % | Yapı mesafesi % |
|---|---|---|---|---|---:|---:|---:|
| QNTUSDT | MEXC | MEXC | Geri testte tutunma / SAR, Tutunma | 27.10.2026 03:44 | 203.095 | 0.04 | 5.83 |
| CLANKERUSDT | MEXC | MEXC | Yeni kırılım | 27.10.2026 03:44 | 13.645 | 0.22 | 6.14 |
| TELUSDT | MEXC | MEXC | Erken dönüş | 27.10.2026 03:44 | 0.0015175 | 0.20 | 8.55 |
| XKORUUSDT | OKX | OKX | Yeni kırılım | 27.10.2026 03:44 | 11.475 | 0.26 | 10.33 |

Sıralama: en çok 4x sayılan göreli hacim, kapanış konumu, dar makas ve aynı borsanın hacmi. Farklı borsaların hacimleri toplanmaz. Bu sıra başarı olasılığı değildir.

Başlangıç elemesi: en az 100.000 USDT kapalı 24s hacim, en çok %0,5 makas, izlenen seviyeyi koruyan güncel fiyat, kapanıştan en çok 1 ATR uzaklık, EMA20 üstüne en çok 2,5 ATR uzama ve yapı referansına en çok %12 mesafe. 20x üzeri hacim ayrıca incelemede kalır. Bunlar daha iyi sonuç verdiği kanıtlanmış yeni strateji eşikleri değildir.

Aynı sembol tek satırda gösterilir; yalnız elemeden geçen borsalar listelenir. Sembol eşleşmesi bağımsız kontrat kimliği teyidi değildir. Geniş havuz ve eski ölçümler korunur. [Tanınan OKX hisse tokenlerinin kaynağı](https://www.okx.com/help/okx-to-list-tokenized-stocks-for-trading). Liste 2026-10-26 tarihinde kontrol edildi; yeni hisse tokenlerinin eklenmesi gerekebilir.

## Eleme özeti

- 13 borsa kaydı: EMA20 uzaklığı fazla veya bilinmiyor
- 5 borsa kaydı: olağandışı hacim katsayısı; ayrıca inceleme
- 18 borsa kaydı: tanınan tokenleştirilmiş hisse
- 8 borsa kaydı: yalnız hazırlık; ek teknik teyit yok
- 2 borsa kaydı: güncel fiyat kapanıştan uzak veya veri eksik
- 10 borsa kaydı: yapı bozulma mesafesi geniş veya bilinmiyor
- 9 borsa kaydı: makas geniş veya bilinmiyor
- 3 borsa kaydı: izlenen seviye kaybedilmiş veya bilinmiyor
- 16 borsa kaydı: hacim 100.000 USDT altında

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
| XKORUUSDT | OKX | 27.10.2026 03:44 | 11.475 | — | — | — |
| QNTUSDT | MEXC | 27.10.2026 03:44 | 203.095 | — | — | — |
| CLANKERUSDT | MEXC | 27.10.2026 03:44 | 13.645 | — | — | — |
| TELUSDT | MEXC | 27.10.2026 03:44 | 0.0015175 | — | — | — |

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

MEXC: incelenen 1035, aday 21; kapanış 27.10.2026 03:00 TR; fiyat gözlemi 27.10.2026 03:42 TR.
V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |
|---|---|---:|---:|---|---|
| BULLAUSDT | Tutunma | 65.36 | 6.15 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; makas geniş |
| MIUUSDT | Tutunma | 15.00 | 10.54 | Yok | 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; makas geniş |
| NEXUSDT | Tutunma | 27.54 | 4.42 | Yok | yapı bozulma mesafesi geniş |
| PVTUSDT | Tutunma | 1.31 | 2.22 | RSI PU teyitli | düşük hacim; makas geniş |
| MASKUSDT | Erken dönüş | 1.77 | 2.54 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| TUTUSDT | Erken dönüş | 1.76 | 2.31 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| USUSDT | Erken dönüş | 29.10 | 21.17 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı kapanıştan uzaklaştı |
| AIAUSDT | Erken dönüş | 2.57 | 2.69 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| BASECATUSDT | Erken dönüş | 19.04 | 4.39 | Yok | yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| TELUSDT | Erken dönüş | 8.36 | 2.34 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| AINUSDT | Yeni kırılım | 85.60 | 14.54 | RSI PU teyitli | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş |
| TAGUSDT | Yeni kırılım | 45.52 | 2.18 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş; gözlem fiyatı grubun izlediği seviyenin altında |
| CLANKERUSDT | Yeni kırılım | 5.07 | 2.46 | Yok | Ek eşik uyarısı yok |
| PARTIUSDT | Yeni kırılım | 16.12 | 1.58 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş |
| QUSDT | Yeni kırılım | 249.24 | 19.70 | RSI PU teyitli | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş |
| SYNUSDT | Yeni kırılım | 16.30 | 2.55 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| QNTUSDT | Geri testte tutunma / SAR, Tutunma | 7.24 | 8.08 | Yok | geri testte SAR desteği; devam garantisi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| FUELUSDT | Yatay fiyat / hacim artışı | 0.38 | 5.48 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| DVOUSDT | Yatay fiyat / hacim artışı | -0.18 | 2.23 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| IMXUSDT | Yatay fiyat / hacim artışı | 0.38 | 1.52 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| TOWERUSDT | Yatay fiyat / hacim artışı | -0.30 | 1.66 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |

OKX: incelenen 343, aday 29; kapanış 27.10.2026 03:00 TR; fiyat gözlemi 27.10.2026 03:39 TR.
V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |
|---|---|---:|---:|---|---|
| GRVTUSDT | Erken dönüş | 7.07 | 2.33 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| FLUIDUSDT | Erken dönüş | 2.08 | 1.75 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| BATUSDT | Erken dönüş | 0.28 | 2.02 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| PARTIUSDT | Yeni kırılım | 16.07 | 17.55 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş |
| XTSLAUSDT | Yeni kırılım | 5.96 | 21.02 | Yok | ortalamadan uzak |
| XAAOIUSDT | Yeni kırılım | 8.37 | 2.92 | RSI PU teyitli | Ek eşik uyarısı yok |
| XAMDUSDT | Yeni kırılım | 3.53 | 3.99 | RSI PU teyitli | Ek eşik uyarısı yok |
| XAVGOUSDT | Yeni kırılım | 2.96 | 3.43 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XCOHRUSDT | Yeni kırılım | 8.59 | 4.46 | RSI PU teyitli | ortalamadan uzak; düşük hacim |
| XDRAMUSDT | Yeni kırılım | 3.36 | 50.69 | Yok | Ek eşik uyarısı yok |
| XGEVUSDT | Yeni kırılım | 5.81 | 12.67 | Yok | ortalamadan uzak; düşük hacim |
| XINTCUSDT | Yeni kırılım | 5.28 | 11.19 | RSI PU teyitli | Ek eşik uyarısı yok |
| XINTWUSDT | Yeni kırılım | 9.98 | 7.21 | Yok | düşük hacim |
| XLITEUSDT | Yeni kırılım | 10.08 | 16.23 | RSI PU teyitli | ortalamadan uzak |
| XMRVLUSDT | Yeni kırılım | 3.07 | 8.36 | RSI PU teyitli | Ek eşik uyarısı yok |
| XMUUSDT | Yeni kırılım | 2.57 | 4.84 | RSI PU teyitli | Ek eşik uyarısı yok |
| XNVDAUSDT | Yeni kırılım | 2.03 | 4.54 | RSI PU teyitli | Ek eşik uyarısı yok |
| XSMHUSDT | Yeni kırılım | 2.80 | 35.11 | RSI PU teyitli | düşük hacim |
| XSOXLUSDT | Yeni kırılım | 8.84 | 12.65 | RSI PU teyitli | Ek eşik uyarısı yok |
| XTQQQUSDT | Yeni kırılım | 4.02 | 12.10 | Yok | Ek eşik uyarısı yok |
| XARMUSDT | Yeni kırılım | 7.49 | 1.89 | Yok | ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XDELLUSDT | Yeni kırılım | 2.56 | 76.97 | RSI PU teyitli | Ek eşik uyarısı yok |
| XKORUUSDT | Yeni kırılım | 6.40 | 1.69 | RSI PU teyitli | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XRKLBUSDT | Yeni kırılım | 3.33 | 11.29 | RSI PU teyitli | Ek eşik uyarısı yok |
| XSKHYUSDT | Yeni kırılım | 4.06 | 1.56 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| XLMUSDT | Yatay fiyat / hacim artışı | 0.75 | 2.46 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| OPUSDT | Yatay fiyat / hacim artışı | 0.72 | 1.90 | RSI PU teyitli | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ZKUSDT | Yatay fiyat / hacim artışı | 1.05 | 2.23 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| VELODROMEUSDT | Yatay fiyat / hacim artışı | 0.68 | 1.69 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |

İki borsada toplam 49 farklı sembol. Ortak semboller bağımsız iki başarı sayılmaz.

Eşikler başlangıç deneyidir; daha çok aday daha yüksek başarı demek değildir. Yazılım testleri kârlılık kanıtı değildir. Dört saatlik mum ve zamanlayıcı gecikmesi ilk hareketin kaçmasına yol açabilir. SAR yön desteğidir; getiri garantisi değildir.

## Bu döngüde yeni gelenler

GRVTUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 03:39 TR; fiyat 0.21321
24s %7.07; ilgili hacim 2.3314x; makas %0.15
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

BATUSDT · OKX
Gruplar: Erken dönüş
Gözlem 27.10.2026 03:39 TR; fiyat 0.14842
24s %0.28; ilgili hacim 2.0213x; makas %0.13
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

XAAOIUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 03:39 TR; fiyat 73.69
24s %8.37; ilgili hacim 2.9219x; makas %0.22
Ek eşik uyarısı yok; teyitli RSI pozitif uyumsuzluk desteği

XAMDUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 03:39 TR; fiyat 537.75
24s %3.53; ilgili hacim 3.9946x; makas %0.02
Ek eşik uyarısı yok; teyitli RSI pozitif uyumsuzluk desteği

XCOHRUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 03:39 TR; fiyat 225.63
24s %8.59; ilgili hacim 4.4618x; makas %0.06
ortalamadan uzak; düşük hacim; teyitli RSI pozitif uyumsuzluk desteği

XDRAMUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 03:39 TR; fiyat 49.47
24s %3.36; ilgili hacim 50.69x; makas %0.20
Ek eşik uyarısı yok

XGEVUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 03:39 TR; fiyat 861.89
24s %5.81; ilgili hacim 12.67x; makas %0.28
ortalamadan uzak; düşük hacim

XINTWUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 03:39 TR; fiyat 17.675
24s %9.98; ilgili hacim 7.2061x; makas %0.28
düşük hacim

XMRVLUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 03:39 TR; fiyat 236.49
24s %3.07; ilgili hacim 8.3626x; makas %0.04
Ek eşik uyarısı yok; teyitli RSI pozitif uyumsuzluk desteği

XMUUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 03:39 TR; fiyat 917.22
24s %2.57; ilgili hacim 4.8447x; makas %0.03
Ek eşik uyarısı yok; teyitli RSI pozitif uyumsuzluk desteği

XNVDAUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 03:39 TR; fiyat 217.16
24s %2.03; ilgili hacim 4.5448x; makas %0.02
Ek eşik uyarısı yok; teyitli RSI pozitif uyumsuzluk desteği

XSMHUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 03:39 TR; fiyat 546.98
24s %2.80; ilgili hacim 35.112x; makas %0.30
düşük hacim; teyitli RSI pozitif uyumsuzluk desteği

XSOXLUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 03:39 TR; fiyat 93.21
24s %8.84; ilgili hacim 12.647x; makas %0.09
Ek eşik uyarısı yok; teyitli RSI pozitif uyumsuzluk desteği

XTQQQUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 03:39 TR; fiyat 69.35
24s %4.02; ilgili hacim 12.095x; makas %0.12
Ek eşik uyarısı yok

XARMUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 03:39 TR; fiyat 226.95
24s %7.49; ilgili hacim 1.8919x; makas %0.03
ortalamadan uzak; düşük hacim; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

XKORUUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 27.10.2026 03:39 TR; fiyat 11.52
24s %6.40; ilgili hacim 1.694x; makas %0.17
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; teyitli RSI pozitif uyumsuzluk desteği

OPUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 27.10.2026 03:39 TR; fiyat 0.11242
24s %0.72; ilgili hacim 1.8962x; makas %0.01
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

ZKUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 27.10.2026 03:39 TR; fiyat 0.012207
24s %1.05; ilgili hacim 2.2253x; makas %0.07
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

PVTUSDT · MEXC
Gruplar: Tutunma
Gözlem 27.10.2026 03:42 TR; fiyat 0.0001008
24s %1.31; ilgili hacim 2.2182x; makas %0.60
düşük hacim; makas geniş; teyitli RSI pozitif uyumsuzluk desteği

MASKUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 03:42 TR; fiyat 0.40145
24s %1.77; ilgili hacim 2.5371x; makas %0.32
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

TUTUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 03:42 TR; fiyat 0.017523
24s %1.76; ilgili hacim 2.3085x; makas %1.04
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

USUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 03:42 TR; fiyat 0.00528
24s %29.10; ilgili hacim 21.173x; makas %0.38
ortalamadan uzak; yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı kapanıştan uzaklaştı

AIAUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 03:42 TR; fiyat 0.074555
24s %2.57; ilgili hacim 2.6908x; makas %0.47
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

BASECATUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 03:42 TR; fiyat 0.010385
24s %19.04; ilgili hacim 4.3933x; makas %0.48
yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

TELUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 27.10.2026 03:42 TR; fiyat 0.0015175
24s %8.36; ilgili hacim 2.336x; makas %0.20
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

AINUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 27.10.2026 03:42 TR; fiyat 0.07002
24s %85.60; ilgili hacim 14.537x; makas %0.86
24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; makas geniş; teyitli RSI pozitif uyumsuzluk desteği

SYNUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 27.10.2026 03:42 TR; fiyat 0.18663
24s %16.30; ilgili hacim 2.5464x; makas %0.14
ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

DVOUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 27.10.2026 03:42 TR; fiyat 0.0048509
24s %-0.18; ilgili hacim 2.2331x; makas %0.02
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

IMXUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 27.10.2026 03:42 TR; fiyat 0.13905
24s %0.38; ilgili hacim 1.523x; makas %0.12
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

TOWERUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 27.10.2026 03:42 TR; fiyat 0.0001345
24s %-0.30; ilgili hacim 1.6568x; makas %1.19
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

## V5 gerçek gözlemden sonraki sonuçlar

Her borsa/token için ilk gerçek fiyat bir ana kayıttır. Gruplar örtüşebilir; grup sayıları bağımsız başarı gibi toplanmaz. Bir gruba sonradan ilk giriş, o andaki gerçek fiyatla ayrıca ölçülür. Getiriler ücret/kayma dahil değildir; eksik ölçüm boş kalır.

| Coin | Borsa | İlk grup | Gerçek gözlem TR | Fiyat | 12s % | 24s % | 48s % |
|---|---|---|---|---:|---:|---:|---:|
| GALFTUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.8066 | -2.05 | — | — |
| XQCOMUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 177.525 | 1.92 | — | — |
| XGOOGLUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 322.39 | -0.93 | — | — |
| ARBUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.170775 | -0.80 | — | — |
| ASTRUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.0064895 | -0.35 | — | — |
| LUNAUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.041805 | 0.75 | — | — |
| METUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.31295 | 2.06 | — | — |
| XLITEUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 780.53 | 6.78 | — | — |
| SPKUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.01838 | 3.37 | — | — |
| XLRCXUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 234.725 | 2.10 | — | — |
| CRVUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.35035 | -2.64 | — | — |
| XASMLUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 1596.95 | 0.26 | — | — |
| IMXUSDT | OKX | Erken dönüş | 26.10.2026 15:39 | 0.1405 | -1.07 | — | — |
| CHIPUSDT | OKX | Yeni kırılım | 26.10.2026 15:39 | 0.049285 | 5.04 | — | — |
| PYTHUSDT | OKX | Yeni kırılım | 26.10.2026 15:39 | 0.075005 | -0.33 | — | — |
| DOODUSDT | OKX | Yeni kırılım | 26.10.2026 15:39 | 0.0023005 | -18.63 | — | — |
| DYDXUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 15:39 | 0.108095 | -0.95 | — | — |
| LDOUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 15:39 | 0.36995 | 0.50 | — | — |
| BICOUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 15:39 | 0.014945 | 0.30 | — | — |
| ILVUSDT | OKX | Yatay fiyat / hacim artışı | 26.10.2026 15:39 | 3.099 | -0.94 | — | — |
| SPCMUSDT | MEXC | Tutunma | 26.10.2026 15:43 | 0.0008465 | -3.79 | — | — |
| TAUSDT | MEXC | Tutunma | 26.10.2026 15:43 | 0.05873 | 5.93 | — | — |
| UMXUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.049465 | -13.70 | — | — |
| CAKEUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 2.1035 | 1.88 | — | — |
| ARBUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.170855 | -0.96 | — | — |
| BANKUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.02771 | -7.07 | — | — |
| NIGHTUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.038025 | 4.59 | — | — |
| NOMUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.001673 | -0.90 | — | — |
| SOONUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.3149 | -2.10 | — | — |
| UPCUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.12305 | 1.26 | — | — |
| GHXUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.009755 | -1.09 | — | — |
| TAGUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.0005201 | 32.38 | — | — |
| HYPEUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 77.435 | 1.67 | — | — |
| METUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.31225 | 2.32 | — | — |
| ONDOUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.413185 | 0.04 | — | — |
| SAGAUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.01787 | 0.78 | — | — |
| 4USDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.01169 | -0.51 | — | — |
| NATIXUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.000163895 | 21.65 | — | — |
| RUNEUSDT | MEXC | Erken dönüş | 26.10.2026 15:43 | 0.6316 | -0.63 | — | — |
| MIUUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 9.35e-10 | -0.53 | — | — |
| BULLAUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 0.139074 | 10.56 | — | — |
| NEXUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 8.0765e-07 | -5.63 | — | — |
| PLAYUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 0.017415 | -5.54 | — | — |
| QNTUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 220.56 | -7.76 | — | — |
| CHIPUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 0.048875 | 5.90 | — | — |
| PYTHUSDT | MEXC | Yeni kırılım | 26.10.2026 15:43 | 0.075095 | -0.63 | — | — |
| DGMAUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.01041 | -9.70 | — | — |
| PENGUUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.007525 | 0.20 | — | — |
| SHMUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 3.845e-05 | 0.13 | — | — |
| HMNDUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.0026355 | -4.72 | — | — |
| LYNUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.01345 | 3.87 | — | — |
| XLMUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.16945 | 0.09 | — | — |
| TRXUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.3313 | -0.54 | — | — |
| MONUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 0.021545 | 1.23 | — | — |
| DOGSUSDT | MEXC | Yatay fiyat / hacim artışı | 26.10.2026 15:43 | 3.596e-05 | -0.89 | — | — |
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
| GRVTUSDT | OKX | Erken dönüş | 27.10.2026 03:39 | 0.213205 | — | — | — |
| BATUSDT | OKX | Erken dönüş | 27.10.2026 03:39 | 0.14842 | — | — | — |
| XAAOIUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 73.69 | — | — | — |
| XAMDUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 537.745 | — | — | — |
| XCOHRUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 225.63 | — | — | — |
| XDRAMUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 49.47 | — | — | — |
| XGEVUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 861.89 | — | — | — |
| XINTWUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 17.675 | — | — | — |
| XMRVLUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 236.485 | — | — | — |
| XMUUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 917.215 | — | — | — |
| XNVDAUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 217.165 | — | — | — |
| XSMHUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 546.985 | — | — | — |
| XSOXLUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 93.21 | — | — | — |
| XTQQQUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 69.35 | — | — | — |
| XARMUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 226.955 | — | — | — |
| XKORUUSDT | OKX | Yeni kırılım | 27.10.2026 03:39 | 11.52 | — | — | — |
| OPUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 03:39 | 0.112425 | — | — | — |
| ZKUSDT | OKX | Yatay fiyat / hacim artışı | 27.10.2026 03:39 | 0.012207 | — | — | — |
| PVTUSDT | MEXC | Tutunma | 27.10.2026 03:42 | 0.0001008 | — | — | — |
| MASKUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.40145 | — | — | — |
| TUTUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.0175235 | — | — | — |
| USUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.00528 | — | — | — |
| AIAUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.074555 | — | — | — |
| BASECATUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.010385 | — | — | — |
| TELUSDT | MEXC | Erken dönüş | 27.10.2026 03:42 | 0.0015175 | — | — | — |
| AINUSDT | MEXC | Yeni kırılım | 27.10.2026 03:42 | 0.07002 | — | — | — |
| SYNUSDT | MEXC | Yeni kırılım | 27.10.2026 03:42 | 0.186635 | — | — | — |
| DVOUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 03:42 | 0.00485085 | — | — | — |
| IMXUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 03:42 | 0.13905 | — | — | — |
| TOWERUSDT | MEXC | Yatay fiyat / hacim artışı | 27.10.2026 03:42 | 0.0001345 | — | — | — |

### Grupların ayrı ölçümleri

| Grup | Borsa | Süre | Ölçülen / kayıt | Medyan % | BTC üstü puan | Kontrol üstü puan |
|---|---|---:|---:|---:|---:|---:|
| Geri testte tutunma / SAR | MEXC | 12s | 0/1 | — | — | — |
| Geri testte tutunma / SAR | MEXC | 24s | 0/1 | — | — | — |
| Geri testte tutunma / SAR | MEXC | 48s | 0/1 | — | — | — |
| Erken dönüş | MEXC | 12s | 17/59 | 0.04 | 0.10 | -0.19 |
| Erken dönüş | MEXC | 24s | 0/59 | — | — | — |
| Erken dönüş | MEXC | 48s | 0/59 | — | — | — |
| Erken dönüş | OKX | 12s | 13/68 | 0.26 | 0.32 | -0.53 |
| Erken dönüş | OKX | 24s | 0/68 | — | — | — |
| Erken dönüş | OKX | 48s | 0/68 | — | — | — |
| Yatay fiyat / hacim artışı | MEXC | 12s | 10/51 | -0.23 | -0.17 | -0.27 |
| Yatay fiyat / hacim artışı | MEXC | 24s | 0/51 | — | — | — |
| Yatay fiyat / hacim artışı | MEXC | 48s | 0/51 | — | — | — |
| Yatay fiyat / hacim artışı | OKX | 12s | 5/56 | -0.80 | -0.74 | -1.17 |
| Yatay fiyat / hacim artışı | OKX | 24s | 0/56 | — | — | — |
| Yatay fiyat / hacim artışı | OKX | 48s | 0/56 | — | — | — |
| Yeni kırılım | MEXC | 12s | 8/23 | -0.76 | -0.71 | -1.29 |
| Yeni kırılım | MEXC | 24s | 0/23 | — | — | — |
| Yeni kırılım | MEXC | 48s | 0/23 | — | — | — |
| Yeni kırılım | OKX | 12s | 4/27 | -0.34 | -0.28 | -1.98 |
| Yeni kırılım | OKX | 24s | 0/27 | — | — | — |
| Yeni kırılım | OKX | 48s | 0/27 | — | — | — |
| Tutunma | MEXC | 12s | 2/8 | 1.07 | 1.12 | 0.08 |
| Tutunma | MEXC | 24s | 0/8 | — | — | — |
| Tutunma | MEXC | 48s | 0/8 | — | — | — |

## Önceki V4 kayıtları — yeni kayıt alınmıyor

Eski gerçek giriş fiyatları korunur; bunlar yeni grupların geçmişte yakaladığı örnekler değildir. 12/24/48s ölçümleri ayrı sürdürülür.

## Gerçek gözlemden sonraki ölçümler

Her sürüm ve borsanın ilk gerçek alış/satış orta fiyatı ayrı kaydedilir. Aynı coin grup değiştirse de yeni bağımsız örnek sayılmaz. Hedef saatten sonraki ilk dakika kapanışı kullanılır; gecikme 60 saniyeden küçüktür. Ücret/kayma dahil net kâr değildir. Henüz oluşmamış veya eksik ölçümler boş kalır.

8 borsa kaydı, 8 farklı sembol. Ortak semboller iki bağımsız başarı gibi toplanmaz.

| Borsa | Süre | Ölçülen | Medyan % | BTC üstü puan | Kontrol üstü puan | Kontrol ölçülen |
|---|---:|---:|---:|---:|---:|---:|
| MEXC | 12s | 8/8 | -2.13 | -1.79 | -2.12 | 8 |
| MEXC | 24s | 4/8 | -5.25 | -4.69 | -2.80 | 4 |
| MEXC | 48s | 0/8 | — | — | — | 0 |

| Coin | Borsa | İlk grup | Gerçek gözlem TR | Referans fiyat | 12s % | 24s % | 48s % |
|---|---|---|---|---:|---:|---:|---:|
| BULLAUSDT | MEXC | Yeni kırılım | 26.10.2026 11:48 | 0.1130635 | 35.79 | — | — |
| CAPUSDT | MEXC | Tutunma | 26.10.2026 00:23 | 0.10956 | -21.28 | -9.24 | — |
| CPHUSDT | MEXC | Tutunma | 26.10.2026 11:48 | 0.0035595 | -3.05 | — | — |
| GBCKUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.0048565 | -0.59 | -1.27 | — |
| MIUUSDT | MEXC | Yeni kırılım | 26.10.2026 03:52 | 8.85e-10 | 5.08 | — | — |
| NEXUSDT | MEXC | Yeni kırılım | 26.10.2026 11:48 | 7.95e-07 | -10.87 | — | — |
| STONKSUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.0020883 | -19.28 | -24.35 | — |
| TAUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.06203 | -1.21 | -0.18 | — |

Karşılaştırma için en az 1–2 haftalık gerçek kayıt beklenir. Gruplar, borsalar ve ortak coinler dikkate alınmadan bir kazanma oranı iddia edilmez.


<!-- coin-priority-raw:end -->

</details>
