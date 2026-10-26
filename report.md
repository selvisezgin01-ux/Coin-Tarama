# Coin Tarama 3 — erken dönüş / hacim / geri test

**Deneysel canlı tarama; başarı üstünlüğü doğrulanmadı.**

V3 otomasyonu ve bildirimleri ayrı çalışır. Yeni adaylar Coin Tarama 3 başlığıyla bildirilir; yerel 50 coinlik pilot kayıtları ayrıdır. Puan başarı olasılığı değildir.

Üç ek grup birbirinin alternatifi: erken dönüş, yatay fiyat/hacim artışı, geri testte tutunma/SAR. Önceki yeni kırılım ve tutunma yolları da korunur. Bir token birden çok gruba uyabilir; bağımsız başarı gibi toplanmaz.

246 coinlik geçmiş kontrolünde bilinen tasarım örnekleri hariç yeni birleşim 1423, eski V4 724 olay üretti. Ölçülen 12s kapanış medyanı sırasıyla -%0,33 ve -%0,50; yeni birleşimin kontrol üstü medyan farkı -0,29 puan. Bu, kazanç veya üstünlük kanıtı değildir. Eski arşiv, canlı ön eleme ve işlem maliyetlerini tam temsil etmez.

Erken dönüşte önceki mum EMA20 altındayken üç mumluk yakın tepenin hacimle geri alınması aranır; yükselen EMA20 veya eski 20 mum tepesini aşması zorunlu değildir. Yatay hacim yükseliş onayı veya kesin toplama değildir. Geri testte sabit kırılım seviyesi, gerçek dönüş, dar taban, azalan hacim ve SAR alt konumu aranır.

MEXC: incelenen 1042, aday 35; kapanış 26.10.2026 15:00 TR; fiyat gözlemi 26.10.2026 15:43 TR.
V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |
|---|---|---:|---:|---|---|
| SPCMUSDT | Tutunma | 0.15 | 1.57 | Yok | Ek eşik uyarısı yok |
| TAUSDT | Tutunma | 6.60 | 1.86 | Yok | düşük hacim; gözlem fiyatı grubun izlediği seviyenin altında |
| UMXUSDT | Erken dönüş | 25.75 | 26.24 | Yok | yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| CAKEUSDT | Erken dönüş | 1.59 | 1.73 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ARBUSDT | Erken dönüş | 2.96 | 3.59 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| BANKUSDT | Erken dönüş | 9.61 | 7.10 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı kapanıştan uzaklaştı |
| NIGHTUSDT | Erken dönüş | 2.57 | 2.88 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| NOMUSDT | Erken dönüş, Yeni kırılım | 13.59 | 2.36 | Yok | yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı kapanıştan uzaklaştı |
| SOONUSDT | Erken dönüş | 4.20 | 4.44 | Yok | yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| UPCUSDT | Erken dönüş | -0.24 | 684.52 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| GHXUSDT | Erken dönüş | -0.15 | 2.47 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| TAGUSDT | Erken dönüş | 0.80 | 4.46 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| HYPEUSDT | Erken dönüş | 0.94 | 1.75 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| METUSDT | Erken dönüş | 4.56 | 1.74 | RSI PU teyitli | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ONDOUSDT | Erken dönüş | 2.18 | 1.81 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| SAGAUSDT | Erken dönüş | 0.90 | 1.54 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| 4USDT | Erken dönüş | 0.35 | 1.65 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| NATIXUSDT | Erken dönüş | -1.17 | 1.87 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| RUNEUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 1.07 | 1.73 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| MIUUSDT | Yeni kırılım | 57.63 | 10.54 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; makas geniş |
| BULLAUSDT | Yeni kırılım | 51.23 | 6.15 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; makas geniş |
| NEXUSDT | Yeni kırılım | 40.38 | 4.42 | Yok | 24 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; gözlem fiyatı kapanıştan uzaklaştı |
| PLAYUSDT | Yeni kırılım | 17.37 | 3.04 | RSI PU teyitli | yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| QNTUSDT | Yeni kırılım | 18.20 | 8.08 | Yok | ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| CHIPUSDT | Yeni kırılım | 5.60 | 1.66 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| PYTHUSDT | Yeni kırılım | 6.44 | 1.52 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| DGMAUSDT | Yatay fiyat / hacim artışı | -0.94 | 2.36 | RSI PU teyitli | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| PENGUUSDT | Yatay fiyat / hacim artışı | 1.78 | 2.96 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| SHMUSDT | Yatay fiyat / hacim artışı | 0.00 | 1.73 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| HMNDUSDT | Yatay fiyat / hacim artışı | -2.12 | 1.73 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| LYNUSDT | Yatay fiyat / hacim artışı | 2.44 | 2.86 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XLMUSDT | Yatay fiyat / hacim artışı | -0.24 | 2.32 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| TRXUSDT | Yatay fiyat / hacim artışı | 0.49 | 1.62 | RSI PU teyitli | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| MONUSDT | Yatay fiyat / hacim artışı | 1.83 | 1.71 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| DOGSUSDT | Yatay fiyat / hacim artışı | -0.03 | 1.67 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |

OKX: incelenen 326, aday 20; kapanış 26.10.2026 15:00 TR; fiyat gözlemi 26.10.2026 15:39 TR.
V5 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Uyan gruplar | 24s % | İlgili hacim katı | PU | Uyarılar |
|---|---|---:|---:|---|---|
| GALFTUSDT | Erken dönüş | 0.99 | 7.17 | RSI PU teyitli | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş |
| XQCOMUSDT | Erken dönüş | 1.08 | 9.33 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XGOOGLUSDT | Erken dönüş | 0.41 | 3.41 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| ARBUSDT | Erken dönüş, Yatay fiyat / hacim artışı | 2.91 | 2.11 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| ASTRUSDT | Erken dönüş, Yeni kırılım | 6.13 | 12.68 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| LUNAUSDT | Erken dönüş | 1.98 | 11.50 | RSI PU teyitli | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| METUSDT | Erken dönüş | 4.25 | 3.62 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XLITEUSDT | Erken dönüş | 1.05 | 8.04 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| SPKUSDT | Erken dönüş | 1.95 | 4.60 | RSI PU teyitli | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XLRCXUSDT | Erken dönüş | 1.65 | 18.37 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| CRVUSDT | Erken dönüş | 2.28 | 1.73 | Yok | erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| XASMLUSDT | Erken dönüş | 1.27 | 1.92 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| IMXUSDT | Erken dönüş | 1.95 | 1.62 | Yok | düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| CHIPUSDT | Yeni kırılım | 5.42 | 4.09 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| PYTHUSDT | Yeni kırılım | 6.39 | 1.52 | Yok | ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında |
| DOODUSDT | Yeni kırılım | 65.51 | 22.34 | Yok | 24 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| DYDXUSDT | Yatay fiyat / hacim artışı | 2.40 | 1.82 | RSI PU teyitli | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| LDOUSDT | Yatay fiyat / hacim artışı | 1.24 | 2.32 | RSI PU teyitli | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| BICOUSDT | Yatay fiyat / hacim artışı | -0.87 | 2.57 | Yok | yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |
| ILVUSDT | Yatay fiyat / hacim artışı | 0.29 | 2.35 | Yok | düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi |

İki borsada toplam 51 farklı sembol. Ortak semboller bağımsız iki başarı sayılmaz.

Eşikler başlangıç deneyidir; daha çok aday daha yüksek başarı demek değildir. Yazılım testleri kârlılık kanıtı değildir. Dört saatlik mum ve zamanlayıcı gecikmesi ilk hareketin kaçmasına yol açabilir. SAR yön desteğidir; getiri garantisi değildir.

## Bu döngüde yeni gelenler

GALFTUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:39 TR; fiyat 0.8066
24s %0.99; ilgili hacim 7.1678x; makas %0.57
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş; teyitli RSI pozitif uyumsuzluk desteği

XQCOMUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:39 TR; fiyat 177.53
24s %1.08; ilgili hacim 9.3322x; makas %0.11
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XGOOGLUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:39 TR; fiyat 322.39
24s %0.41; ilgili hacim 3.4053x; makas %0.04
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında

ARBUSDT · OKX
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 15:39 TR; fiyat 0.17078
24s %2.91; ilgili hacim 2.1129x; makas %0.03
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı grubun izlediği seviyenin altında; teyitli RSI pozitif uyumsuzluk desteği

ASTRUSDT · OKX
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 26.10.2026 15:39 TR; fiyat 0.0064895
24s %6.13; ilgili hacim 12.683x; makas %0.05
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

LUNAUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:39 TR; fiyat 0.041805
24s %1.98; ilgili hacim 11.504x; makas %0.17
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

METUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:39 TR; fiyat 0.31295
24s %4.25; ilgili hacim 3.6208x; makas %0.10
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XLITEUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:39 TR; fiyat 780.53
24s %1.05; ilgili hacim 8.0355x; makas %0.08
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

SPKUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:39 TR; fiyat 0.01838
24s %1.95; ilgili hacim 4.5969x; makas %0.11
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

XLRCXUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:39 TR; fiyat 234.72
24s %1.65; ilgili hacim 18.371x; makas %0.00
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

CRVUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:39 TR; fiyat 0.35035
24s %2.28; ilgili hacim 1.7273x; makas %0.09
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XASMLUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:39 TR; fiyat 1597
24s %1.27; ilgili hacim 1.9173x; makas %0.12
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

IMXUSDT · OKX
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:39 TR; fiyat 0.1405
24s %1.95; ilgili hacim 1.6161x; makas %0.28
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

CHIPUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 26.10.2026 15:39 TR; fiyat 0.049285
24s %5.42; ilgili hacim 4.0903x; makas %0.18
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

PYTHUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 26.10.2026 15:39 TR; fiyat 0.075005
24s %6.39; ilgili hacim 1.5197x; makas %0.04
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında

DOODUSDT · OKX
Gruplar: Yeni kırılım
Gözlem 26.10.2026 15:39 TR; fiyat 0.0023005
24s %65.51; ilgili hacim 22.34x; makas %0.22
24 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

DYDXUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 15:39 TR; fiyat 0.10809
24s %2.40; ilgili hacim 1.8159x; makas %0.05
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

LDOUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 15:39 TR; fiyat 0.36995
24s %1.24; ilgili hacim 2.3239x; makas %0.08
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

BICOUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 15:39 TR; fiyat 0.014945
24s %-0.87; ilgili hacim 2.5708x; makas %0.20
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ILVUSDT · OKX
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 15:39 TR; fiyat 3.099
24s %0.29; ilgili hacim 2.3494x; makas %0.39
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

SPCMUSDT · MEXC
Gruplar: Tutunma
Gözlem 26.10.2026 15:43 TR; fiyat 0.0008465
24s %0.15; ilgili hacim 1.5675x; makas %0.24
Ek eşik uyarısı yok

UMXUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:43 TR; fiyat 0.049465
24s %25.75; ilgili hacim 26.236x; makas %0.42
yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

CAKEUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:43 TR; fiyat 2.1035
24s %1.59; ilgili hacim 1.7349x; makas %0.05
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

ARBUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:43 TR; fiyat 0.17086
24s %2.96; ilgili hacim 3.5921x; makas %0.06
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

BANKUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:43 TR; fiyat 0.02771
24s %9.61; ilgili hacim 7.096x; makas %0.43
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı kapanıştan uzaklaştı

NIGHTUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:43 TR; fiyat 0.038025
24s %2.57; ilgili hacim 2.8849x; makas %0.08
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

NOMUSDT · MEXC
Gruplar: Erken dönüş, Yeni kırılım
Gözlem 26.10.2026 15:43 TR; fiyat 0.001673
24s %13.59; ilgili hacim 2.3613x; makas %0.12
yapı bozulma mesafesi geniş; düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; gözlem fiyatı kapanıştan uzaklaştı

SOONUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:43 TR; fiyat 0.3149
24s %4.20; ilgili hacim 4.4408x; makas %0.19
yapı bozulma mesafesi geniş; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

UPCUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:43 TR; fiyat 0.12305
24s %-0.24; ilgili hacim 684.52x; makas %0.24
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

GHXUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:43 TR; fiyat 0.009755
24s %-0.15; ilgili hacim 2.4709x; makas %0.21
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

TAGUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:43 TR; fiyat 0.0005201
24s %0.80; ilgili hacim 4.462x; makas %0.88
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

HYPEUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:43 TR; fiyat 77.435
24s %0.94; ilgili hacim 1.7487x; makas %0.04
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

METUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:43 TR; fiyat 0.31225
24s %4.56; ilgili hacim 1.7429x; makas %0.03
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

ONDOUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:43 TR; fiyat 0.41319
24s %2.18; ilgili hacim 1.8142x; makas %0.07
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

SAGAUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:43 TR; fiyat 0.01787
24s %0.90; ilgili hacim 1.5366x; makas %0.11
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

4USDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:43 TR; fiyat 0.01169
24s %0.35; ilgili hacim 1.6505x; makas %0.34
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

NATIXUSDT · MEXC
Gruplar: Erken dönüş
Gözlem 26.10.2026 15:43 TR; fiyat 0.0001639
24s %-1.17; ilgili hacim 1.8663x; makas %3.78
düşük hacim; erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

RUNEUSDT · MEXC
Gruplar: Erken dönüş, Yatay fiyat / hacim artışı
Gözlem 26.10.2026 15:43 TR; fiyat 0.6316
24s %1.07; ilgili hacim 1.727x; makas %0.47
erken dönüş; uzun trend teyidi henüz aranmadı; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

PLAYUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 26.10.2026 15:43 TR; fiyat 0.017415
24s %17.37; ilgili hacim 3.0383x; makas %0.40
yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında; teyitli RSI pozitif uyumsuzluk desteği

QNTUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 26.10.2026 15:43 TR; fiyat 220.56
24s %18.20; ilgili hacim 8.0847x; makas %0.12
ortalamadan uzak; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

CHIPUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 26.10.2026 15:43 TR; fiyat 0.048875
24s %5.60; ilgili hacim 1.6648x; makas %0.31
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi

PYTHUSDT · MEXC
Gruplar: Yeni kırılım
Gözlem 26.10.2026 15:43 TR; fiyat 0.075095
24s %6.44; ilgili hacim 1.5238x; makas %0.07
ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; gözlem fiyatı grubun izlediği seviyenin altında

DGMAUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 15:43 TR; fiyat 0.01041
24s %-0.94; ilgili hacim 2.3556x; makas %0.19
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

PENGUUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 15:43 TR; fiyat 0.007525
24s %1.78; ilgili hacim 2.961x; makas %0.11
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

SHMUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 15:43 TR; fiyat 3.845e-05
24s %0.00; ilgili hacim 1.7267x; makas %0.26
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

HMNDUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 15:43 TR; fiyat 0.0026355
24s %-2.12; ilgili hacim 1.7328x; makas %0.80
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; makas geniş

LYNUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 15:43 TR; fiyat 0.01345
24s %2.44; ilgili hacim 2.8606x; makas %0.30
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

XLMUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 15:43 TR; fiyat 0.16945
24s %-0.24; ilgili hacim 2.3233x; makas %0.06
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

TRXUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 15:43 TR; fiyat 0.3313
24s %0.49; ilgili hacim 1.6173x; makas %0.06
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi; teyitli RSI pozitif uyumsuzluk desteği

MONUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 15:43 TR; fiyat 0.021545
24s %1.83; ilgili hacim 1.7056x; makas %0.14
yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

DOGSUSDT · MEXC
Gruplar: Yatay fiyat / hacim artışı
Gözlem 26.10.2026 15:43 TR; fiyat 3.596e-05
24s %-0.03; ilgili hacim 1.6658x; makas %0.06
düşük hacim; yatay hacim; toplama veya yükseliş teyidi değildir; deneysel ek grup; geçmiş karşılaştırmada tutarlı üstünlük gösterilmedi

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

### Grupların ayrı ölçümleri

| Grup | Borsa | Süre | Ölçülen / kayıt | Medyan % | BTC üstü puan | Kontrol üstü puan |
|---|---|---:|---:|---:|---:|---:|
| Erken dönüş | MEXC | 12s | 0/17 | — | — | — |
| Erken dönüş | MEXC | 24s | 0/17 | — | — | — |
| Erken dönüş | MEXC | 48s | 0/17 | — | — | — |
| Erken dönüş | OKX | 12s | 0/13 | — | — | — |
| Erken dönüş | OKX | 24s | 0/13 | — | — | — |
| Erken dönüş | OKX | 48s | 0/13 | — | — | — |
| Yatay fiyat / hacim artışı | MEXC | 12s | 0/10 | — | — | — |
| Yatay fiyat / hacim artışı | MEXC | 24s | 0/10 | — | — | — |
| Yatay fiyat / hacim artışı | MEXC | 48s | 0/10 | — | — | — |
| Yatay fiyat / hacim artışı | OKX | 12s | 0/5 | — | — | — |
| Yatay fiyat / hacim artışı | OKX | 24s | 0/5 | — | — | — |
| Yatay fiyat / hacim artışı | OKX | 48s | 0/5 | — | — | — |
| Yeni kırılım | MEXC | 12s | 0/8 | — | — | — |
| Yeni kırılım | MEXC | 24s | 0/8 | — | — | — |
| Yeni kırılım | MEXC | 48s | 0/8 | — | — | — |
| Yeni kırılım | OKX | 12s | 0/4 | — | — | — |
| Yeni kırılım | OKX | 24s | 0/4 | — | — | — |
| Yeni kırılım | OKX | 48s | 0/4 | — | — | — |
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
| MEXC | 12s | 4/8 | -10.25 | -10.21 | -9.87 | 4 |
| MEXC | 24s | 0/8 | — | — | — | 0 |
| MEXC | 48s | 0/8 | — | — | — | 0 |

| Coin | Borsa | İlk grup | Gerçek gözlem TR | Referans fiyat | 12s % | 24s % | 48s % |
|---|---|---|---|---:|---:|---:|---:|
| BULLAUSDT | MEXC | Yeni kırılım | 26.10.2026 11:48 | 0.1130635 | — | — | — |
| CAPUSDT | MEXC | Tutunma | 26.10.2026 00:23 | 0.10956 | -21.28 | — | — |
| CPHUSDT | MEXC | Tutunma | 26.10.2026 11:48 | 0.0035595 | — | — | — |
| GBCKUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.0048565 | -0.59 | — | — |
| MIUUSDT | MEXC | Yeni kırılım | 26.10.2026 03:52 | 8.85e-10 | — | — | — |
| NEXUSDT | MEXC | Yeni kırılım | 26.10.2026 11:48 | 7.95e-07 | — | — | — |
| STONKSUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.0020883 | -19.28 | — | — |
| TAUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.06203 | -1.21 | — | — |

Karşılaştırma için en az 1–2 haftalık gerçek kayıt beklenir. Gruplar, borsalar ve ortak coinler dikkate alınmadan bir kazanma oranı iddia edilmez.

