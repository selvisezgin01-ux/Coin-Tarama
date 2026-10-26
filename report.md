> Bu onceki V4 raporudur. [Guncel Coin Tarama 3 raporunu ac](https://github.com/selvisezgin01-ux/Coin-Tarama/blob/scanner-state-v5/report.md). Eski gercek gozlem sonuclari guncel raporda ayri izlenmeye devam eder.

# Coin Tarama 3 — yeni kırılım ve tutunma

**Deneysel canlı tarama; başarı üstünlüğü doğrulanmadı.**

V3 otomasyonu ve bildirimleri ayrı çalışır. Yeni adaylar bu sürümün kendi bildirim başlığıyla gönderilir; yerel pilot kayıtları ayrıdır. Puan başarı olasılığı değildir.

MEXC: incelenen 1034, aday 5; kapanış 26.10.2026 11:00 TR; fiyat gözlemi 26.10.2026 11:48 TR.
V4 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Grup | 24s % | Kırılım yaşı (mum) | PU | Uyarılar |
|---|---|---:|---:|---|---|
| CPHUSDT | Tutunma | 0.36 | 18 | Yok | yapı bozulma mesafesi geniş; düşük hacim; makas geniş |
| TAUSDT | Tutunma | 10.30 | 3 | Yok | düşük hacim |
| MIUUSDT | Yeni kırılım | 88.00 | 1 | Yok | 24 saatlik yükseliş yüksek; 72 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş; düşük hacim; makas geniş |
| BULLAUSDT | Yeni kırılım | 13.13 | 0 | Yok | yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi |
| NEXUSDT | Yeni kırılım | 31.85 | 1 | Yok | 24 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş |

OKX: incelenen 321, aday 0; kapanış 26.10.2026 11:00 TR; fiyat gözlemi 26.10.2026 11:44 TR.
V4 live prefilter: >=-10% rolling 24h, no upper return cap, >=10k USDT volume.

| Coin | Grup | 24s % | Kırılım yaşı (mum) | PU | Uyarılar |
|---|---|---:|---:|---|---|

İki borsada toplam 5 farklı sembol. Ortak semboller bağımsız iki başarı sayılmaz.

Arşiv karşılaştırmasında yeni sürüm kontrol coinlerine karşı üstünlük göstermedi. Coin Tarama 3 ayrı bir ileri dönem deneyidir; önceki sürüm de çalışır.

## Bu döngüde yeni gelenler

CPHUSDT · MEXC
Fiyat 0.0035595 | 24s %0.36 | hacim 1.88x | makas %0.98
grup: tutunma; yapı bozulma mesafesi geniş; düşük hacim; makas geniş; düşük hacim; makas teyidi gerekli

BULLAUSDT · MEXC
Fiyat 0.1130635 | 24s %13.13 | hacim 6.15x | makas %0.35
grup: yeni kırılım; yapı bozulma mesafesi geniş; ilk kapanış; sonraki mumda tutunma henüz gözlenmedi; ilk kırılım kapanışı; sonraki mum teyidi yok

NEXUSDT · MEXC
Fiyat 7.95e-07 | 24s %31.85 | hacim 4.42x | makas %0.20
grup: yeni kırılım; 24 saatlik yükseliş yüksek; ortalamadan uzak; yapı bozulma mesafesi geniş

## Gerçek gözlemden sonraki ölçümler

Her sürüm ve borsanın ilk gerçek alış/satış orta fiyatı ayrı kaydedilir. Aynı coin grup değiştirse de yeni bağımsız örnek sayılmaz. Hedef saatten sonraki ilk dakika kapanışı kullanılır; gecikme 60 saniyeden küçüktür. Ücret/kayma dahil net kâr değildir. Henüz oluşmamış veya eksik ölçümler boş kalır.

8 borsa kaydı, 8 farklı sembol. Ortak semboller iki bağımsız başarı gibi toplanmaz.

| Borsa | Süre | Ölçülen | Medyan % | BTC üstü puan | Kontrol üstü puan | Kontrol ölçülen |
|---|---:|---:|---:|---:|---:|---:|
| MEXC | 12s | 0/8 | — | — | — | 0 |
| MEXC | 24s | 0/8 | — | — | — | 0 |
| MEXC | 48s | 0/8 | — | — | — | 0 |

| Coin | Borsa | İlk grup | Gerçek gözlem TR | Referans fiyat | 12s % | 24s % | 48s % |
|---|---|---|---|---:|---:|---:|---:|
| BULLAUSDT | MEXC | Yeni kırılım | 26.10.2026 11:48 | 0.1130635 | — | — | — |
| CAPUSDT | MEXC | Tutunma | 26.10.2026 00:23 | 0.10956 | — | — | — |
| CPHUSDT | MEXC | Tutunma | 26.10.2026 11:48 | 0.0035595 | — | — | — |
| GBCKUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.0048565 | — | — | — |
| MIUUSDT | MEXC | Yeni kırılım | 26.10.2026 03:52 | 8.85e-10 | — | — | — |
| NEXUSDT | MEXC | Yeni kırılım | 26.10.2026 11:48 | 7.95e-07 | — | — | — |
| STONKSUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.0020883 | — | — | — |
| TAUSDT | MEXC | Yeni kırılım | 26.10.2026 00:23 | 0.06203 | — | — | — |

Karşılaştırma için en az 1–2 haftalık gerçek kayıt beklenir. Gruplar, borsalar ve ortak coinler dikkate alınmadan bir kazanma oranı iddia edilmez.
