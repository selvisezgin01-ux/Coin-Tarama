# Coin Tarama Meme — V7

Son gözlem: 30.10.2026 23:23 TR

🟡 Erken radar: giriş değildir. 🟢🎯 Otomatik giriş ölçütleri: manuel harita/kontrat kontrolü bekler. 🔵 15dk güçlenme: aynı girişin devamı.
Beş ağ korunur: Solana, Ethereum, BNB Chain, Robinhood ve HyperEVM. Yeni havuz yaşı tokenin tüm yaşamı değildir.
MCAP 50–500bin USD; FDV yerine geçmez. İlk gerçek V7 uygunluk gözleminden sonraki 2tam5dk taban ve ayrı kapalı5dk hacim mumu aranır. İlk haber için bu mumlar beklenmez.
İlk fiyattan %25 yükseliş yasağı V7 koşulu değildir. Seçilen havuzun erişilen geçmişindeki sert düşüş, ilk taban kaybı, tabandan uzama ve güvenlik engelleri ayrı değerlendirilir. Başlangıç/ara geçmiş eksikse giriş teyitsizdir.
İlk likit taban geçmiş MCAP varsayımıyla geriye taşınmaz. Bilinmeyen risk/akış/kotasyon yeşil giriş olmaz. Eski V6 kayıtları yeni V7 başarısı sayılmaz.

## Keşif ve kapsam

{
  "discovery": {
    "mode": "bounded_fallback_collector_unavailable_or_stale",
    "errors": [],
    "pages": [
      {
        "chain": "solana",
        "page": 1,
        "returned": 20,
        "complete": false
      },
      {
        "chain": "ethereum",
        "page": 1,
        "returned": 20,
        "complete": false
      },
      {
        "chain": "bnb",
        "page": 1,
        "returned": 20,
        "complete": false
      },
      {
        "chain": "robinhood",
        "page": 1,
        "returned": 20,
        "complete": false
      }
    ],
    "complete": false
  },
  "started_ms": 1793391706084,
  "scan_finished_ms": 1793391781675,
  "session_id": "41122434019",
  "errors": [
    "robinhood:0x87c610ef377146ec3ada7602fa0385acd485407d: gecko_request_reserved_for_buy_pressure"
  ],
  "discovery_mode": "bounded_fallback_collector_unavailable_or_stale",
  "candles_evaluated": 3,
  "selected_for_candles": 4,
  "candles_budget_waiting": 5,
  "groups": {
    "solana": {
      "requested_quotes": 60,
      "fresh_quotes": 60,
      "quote_unknown": 0
    },
    "ethereum": {
      "requested_quotes": 60,
      "fresh_quotes": 60,
      "quote_unknown": 0
    },
    "bnb": {
      "requested_quotes": 60,
      "fresh_quotes": 39,
      "quote_unknown": 21
    },
    "robinhood": {
      "requested_quotes": 60,
      "fresh_quotes": 52,
      "quote_unknown": 8
    },
    "hyperevm": {
      "requested_quotes": 8,
      "fresh_quotes": 8,
      "quote_unknown": 0
    }
  },
  "requests": {
    "raw.githubusercontent.com:ok": 1,
    "api.geckoterminal.com:ok": 7,
    "api.dexscreener.com:ok": 9,
    "gecko:reserved_for_buy_pressure": 1
  }
}

Sürekli keşif toplayıcısı ayrı yerel süreçtir; bilgisayar uyursa/kapanırsa kesilir. Bayat/yok feed halinde sınırlı GitHub keşfi açıkça fallback sayılır. Tam zincir kapsamı veya kesintisiz1dk sözü yoktur.
Kimlik defteri: 824 token; ayrıntılı fiyat/mum okumaları bütçelidir. Kota nedeniyle bekleyen kimlikler sessizce silinmez.

## Bildirim evreleri

| Evre | Token | Ağ | Gözlem TR | MCAP USD | Bildirim |
|---|---|---|---|---:|---|
| 🟡 ERKEN RADAR | TYGR `0xe1afba9c9898b09f9b8073d5f5cb9d1279fe8e83` | robinhood | 30.10.2026 23:19 | 52529.0 | [Issue #252](https://github.com/selvisezgin01-ux/Coin-Tarama/issues/252) |
| 🟡 ERKEN RADAR | AMAZON `BXnj81MpAEfey3kBYLLAppYSiqthERZmTRm8oMrpump` | solana | 30.10.2026 23:16 | 123536.0 | [Issue #251](https://github.com/selvisezgin01-ux/Coin-Tarama/issues/251) |
| 🟡 ERKEN RADAR | KLEOS `0x389ff560781bd54034e9ad829a965f1b78253b9f` | hyperevm | 30.10.2026 23:15 | 60502.0 | [Issue #250](https://github.com/selvisezgin01-ux/Coin-Tarama/issues/250) |
| 🟡 ERKEN RADAR | HC `8GUoRZCSzjfoA47FRBJ4MuNjjpyn3pWZDTkRePWNpump` | solana | 30.10.2026 23:15 | 266526.0 | [Issue #249](https://github.com/selvisezgin01-ux/Coin-Tarama/issues/249) |

## Kontrat başına son karar

| Kontrat | Durum | Neden |
|---|---|---|
| `bnb:0x000fc84e4525d43ba81aa2e82375b00be6174444` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x01b680a866d8598a1258b9ef9e31d6ae3ffc7777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x0266ada695b468357d2c1ac5d35f6848bd5a2719` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `bnb:0x0531a107edcab3fb56cb9f606f118ac0f3377777` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `bnb:0x05ea4c01a4d29ddc7c6d9bd3a8b08843e90fffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x06155c58c22bf2c98aff1732b0665a16dfc9821c` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `bnb:0x0664a45970bad68d84304b67340b55bd9ba97777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x068e60901182a4e085526f1978c6ed8d4d657af6` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap, liquidity_usd |
| `bnb:0x0770417e479b8ce7c8f59bcedf14ec7a50007777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x0774905cee81990523b7018ef1fcf12d8d757777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x07c756159b43f555d0fe9565aa45cd331108b41e` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `bnb:0x08ff3add33015455efef1f6fe736a46fd98df231` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x0a755689a1db25f87045fc777474f2de267172dd` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x0b239b6d211f1e3e5aac6bd4ff14427dd8ab7777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x0dee012c2f5871c01b5fccc547d1caa30cfaffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x0fdc787480bcabd51cc61c698a4220934920b831` | archived_age | pool_age_over_24h_identity_preserved |
| `bnb:0x104db212eba6b0b57db4fa321e31dfe335a47777` | market_rejected_or_unknown | liquidity, liquidity_usd, market_cap_usd |
| `bnb:0x111e93fbda9cc56dfeefb6aec54f383c3382ffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0x1411454b9e426cc3363e6ed1485fada3ecc325bd` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x155570bb2c6a2407697afbdf2e6f2130c1e67777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x17eecb282b17ffb3447c5f85691f9017fc45ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x1b54f66a54a13302bc374f337dc4ca7ccc907777` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `bnb:0x1dfe1ac74a6b043a2c9bd906996ca50a6725132b` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `bnb:0x1f8a5547b2ae82116cc4159f45cb994d88f6f6ea` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x217e91e177008e6ad702c7b35bca32927ff17777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x235a1e173c0b56f79668169cecae87e7a8ce9c02` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `bnb:0x24bd62dce032fa912be8e260abccc250ad66ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x26b7396a5da57fd1692bce4f724fa3761a16ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x2b1f1925ae965558a6d0795865d512986be00000` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x2bf300356c0e1eec4e8690bb44dd33896c517777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x2cf06050da1be3c9dc05fab42f883304716f3bcc` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `bnb:0x2e1bf0d7222b80eea3ac23beff9507b94a2cffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0x2e622c6b9d3a182476083f315cfc483f10c9843a` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x301f71f01a9ddda1fdf156c0c5d0c3ebf36c7777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x3046633834e46665f6687f8f28b5304bd8f09130` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x32871a8416c210c9342d1c63744a90f1204d7777` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `bnb:0x33d1732f3862899e90143411e80f2de0a6a6369a` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `bnb:0x33f21b4574be238585cab9b062dfc53017b6203b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x359edf52f21e2b98bf55b8901dfede23aeb4ffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0x361ca1922b21de7e9433860c053365ff07877777` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `bnb:0x37481b031c831870a69e08dc524127bbdf3d86fc` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x3748d52b76c523c6021a967fe77deb5b5341ffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0x381e65fac24d13a7df13f68283c1f2e1e2a432c2` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x3ab5950e83e78a5b1628e1165a1f623643707db5` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x3b0d4a26a17bcb4b7ebae96f667c27d97443ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x3ce42d5de4f3b17ef8ba703de537ecfabffdf969` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x3e342a68712cf60725ad0877c3f7b8c5979bffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x3ee83feb7da886cd06ffa698993cd57517f6ffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0x40905d50d779738d231aa028515d9547f45fffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0x44069522a0a853659601ef0bff9ee8167306f811` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `bnb:0x45b07f618d0ed699bdc943020a74247d2c854444` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x468993c3f5091fbb45469ca8b65375a698a2b7a9` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x4818f26b4783d791124395a8405bfeccc7fe7777` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `bnb:0x4934bc5e0b28d926ba7f583a47360a5c3b3bf7b3` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x4ab4595a45b2276f68433ccd381f37fc6fc37777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x4e4cfec8d8b0bcef01a1c70432dac5819c5fa94c` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x516a921f985eecf9e16416974b86f23924a1ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x54fc801d10f78f468307a0e87c76dab48f45e6ea` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0x568d7fecf655eec813d9482f350485d7e46effff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x56a30188774128e3eb2160eb775ddb551316c17a` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `bnb:0x57bd43a51c61bd76deddb64e1a42e5955190f6f8` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `bnb:0x5a057c8d5f4401448a9e97e7a88cdf4c98692992` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x5a11338b1bf54305ce989d5ef27ceeb60b86ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x5c0569f22361dc21c79232f291db6c3539aa3cd5` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `bnb:0x5c53cc275245b036e816ced684337e7d1dffb507` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x5d9977ed0fb1500ead87dc83e1ce57200430ffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0x5e9299f65def24ea5f7f0d362fb51681d75f7777` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `bnb:0x5f1f7c1e3a4f7602367fbd70ca29998197a7ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x640950fe19d3b6b5409d004944e7c7c83085ffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0x64376e5e7f88c7f3b297f568ee5fccee7ac9ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x64525ecd6b661de6c26a5b9f8c68978abf8c603e` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap, liquidity_usd |
| `bnb:0x64c0ab89f71d3b470c1480e2a93a08a189dd1dbc` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x67146b0f1e2dfb44643689d3d212284a256f7777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x67b523390f4b20d792bd57a653e29c30ab40382d` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x69bafe7790a1fba73e87f60a6bf5cc7a32db756d` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x69d0c72f56f5f09e307090207dcf2aacd665ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x6bc57c086bdb597b99f829285561e5125a44c37a` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x6e7b3786c351aaa02c0c7c357263c3b26c70c571` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x6fc175050fb2955a9ea5cf9fa906427231637777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x7085d51eb2d63373ba731273fe26bce80d19ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x714558d939d0bfdc5c45481d9a8aae16d20a7777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x7275cba146d2cead679df90bab2cb4643f58ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x72abfea552bec0ce551ed9bfc3ff6f1315ddffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x72e666026406cd5685710bb7bd7ddac89adeffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x7328a94327d340a73c891b2c30079370ca63cbee` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap, liquidity_usd |
| `bnb:0x75ae48b97cd6938d144476732debada048c2ffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0x77a87b7b65b005ec3275d3f887b035d6aaf8ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x79acade7ac9222e3d7cd0846d67ab761fc2be0d0` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x79b7b1f6206ca53d19f66b808efaf5077559ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x7bee8ae37cfe46ec8d74ac4727012a6c37dcffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x7ce2944fd147fc02eb45cd53877e8fd5c4107777` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `bnb:0x7ce393c4583fa16a3b88fe2382cdfbc1ff2affff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x7d813446cd448bb8bdd48ac4e48b1adac491ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x7ec0949af6575727e851dcdaab1886739dadffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x7f2a39adcebb2450fffa7335b7a3cc9cdccc34b2` | archived_age | pool_age_over_24h_identity_preserved |
| `bnb:0x7f9300306aadc0afd0dc6121334468cbf17a7777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x82301849496fbb9b23237c2b0c69118954d17777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x826e3ad8e38a6f863bb70e14dd560e08975f7e6d` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x84a6e8f683b051d7a035c4ed4e85b7a635247777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x84b5adb47bc6fc495837788e037d7c0a43fcffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0x84d39bc0da4cd443ddb77bdee06a0478c3700e00` | archived_age | pool_age_over_24h_identity_preserved |
| `bnb:0x862ad3f9498b6ef720574486acb3ca5b61f5ffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0x8631c4e6303e25b7e05179b581fe11c202717777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x8829a290f4d9797a69ec471e6ea468d06ba67777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x88711a1d64334dd3fb928433d3444a9dce767777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x89f78eed9f51d9f738c847bb1df026f208a9ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x8aa1664f0fda908a8bf62cc74277ceb90d997777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x8bfcbeb7fe6d32a01088845cd5ea488b39e17777` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `bnb:0x8cf3560ea3811f32774ea2d97c02e80bcb6d9109` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x8d44d337f7e4a5d49873ca063d0d03305587ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x909ccd13c7ff478faf0d18c550c58a46d2e1ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x92361a5764336d28c9f43c86a244a68e0b2fffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x928ef8ffb554503571fb2e3314c32608f06effff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x94bc077f8a2760b43c4d8e0b5b3573b37e88ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x9558a9254890b2a8b057a789f413631b9084f4a3` | archived_age | pool_age_over_24h_identity_preserved |
| `bnb:0x9586e529f179f2a22f00758fa4b33bd6be080621` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x98f61601eaf68dc2dc84ac5be63ac5003f8c7777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x991d72e8fb35ead174878f7fcc94430315ac4793` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x9a70a2aee546f2f224a255831bddc98be5d77777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x9b259cad4dc79fad7d90e356837dfa3f678f7777` | candle_queue | waiting_closed_candles_and_security |
| `bnb:0x9bb0d52bb538a29a1e088f5e30ed9e06e88b65e6` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x9c51e5b7d0dd7997cd9d61ecaad4a6bdfdb09893` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0x9c692c03010ef332461b993523f30b8e4205d8f3` | setup_wait_or_reject | no_closed_bar_after_actual_eligibility |
| `bnb:0x9e656701df2f88cbf29455482085152fc82150b0` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `bnb:0x9e98f3f1dc1e1e7aa5bf7fa405753956ae347e66` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `bnb:0xa02cc033137ca7f12c4a6d03c346197b01f57777` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `bnb:0xa120388a0817181c823fedb22591861ca4e17276` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0xa14f54b89dd0b18368eb7e2eb4287938c5f3b314` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xa261cf879845193d653f1602768acb46d81ba6ea` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xa47bf40359dcb48d324f5c36beab66647415e1f1` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0xa846294787077af6e5f7333c43c6e317e780a3ec` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xa9344923c4aeb9153e0d1776f90974e7627effff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0xa960f0840156df7c8913dc20091b126d9fb87777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xaa26fc13621250ec2d4b5479ba59cd636264ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xabc87207e7170859b4bd78541160dfd52f27ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xacb766c651a29a1e4313375f4c6809136f607777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xb026c86c98d6d70761b8452176bd236051913cbb` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xb080a3b50f9010a2c6847c685f395b2750b47777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xb2abd5f5bb949440fde28685a326041196545759` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xb2c576f3a83db4db218a5773f7fb2dd387fdaf19` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xb3dff4b62163bb7b4ff40625419dbb4d4d6dffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xb413338cf70fa076efe5f487073a356d1efd7777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xb44579780570fb9a4e20163d2bdda8a5cb7effff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xb6818589a8199aed8021e0592ebaa2245c541fad` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xb8c44a47ca87e61004468dd88d0141e6a8e8089f` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xb8ef8d56514876f7e7d6363afa117af0b1d37777` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `bnb:0xb9a4d05391a184d2ee4b8f745fb7beecca997777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xba60efaee9838d77590a1fbf4e3a64a4ae43ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xbac07c71232e9d82f8f2a0017d86cfab18b48a8e` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xbe768f062e7c6c4cbd26349893447546b6b57777` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `bnb:0xc412a9dd96cbfcab6c24df8b47fa8b0de6b3ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xc5c89c50931da431b8b6cc0ff6438ec46d317777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xc638c5e8c4f44f817692719ce2ce07d04616ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xc6d827b3ae03aac93a1e7e1df34d54667060ffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0xc6f637fadd98038950cbb5edd2b686ebe5e6b37a` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xc777a6bcfad96ead7f7a843a4b9b2ac192abffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0xc7d61fc3d0a3517f6ae86c5ce3266ab386735399` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xcac531349f4079ec51290643cb2b24f639ec7777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xcc4185522fb556adaac0895e79033582f02e7777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xccd879e22d2ade878ece138f8f565885b463d6ea` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xcd535d11ee0887e858ff7562b78dd5087b0d7f55` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xce6c655952b863707be23a306770898ce5bed80a` | market_rejected_or_unknown | liquidity, liquidity_usd, market_cap_usd |
| `bnb:0xcffe078fc7bcc45cce11598e66a02404853664f0` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xd080487d5ff4058ac24e60120306b40d006cbbf7` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap, liquidity_usd |
| `bnb:0xd231912bb24c44b73f5c6d8db755e0eabe087777` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `bnb:0xd317cd30a13815f797666fe635250a1b4d9886ea` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xd9e352c736b0c374c1b9e0ccf94a07c307697777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xdb64d7144a5d1266f2ee83e7a4b98d5f8cddffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0xdfb1a0747381a1e616afd65cfb7485afe8c09dbe` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xdff6472542e937cc82862033cbd5ff47e2ba7777` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `bnb:0xe00a3d48cb942f870be741abb263f7ae423bffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0xe1db5fd7a4f917ab6f5a0485bdb7a68ff05b7777` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `bnb:0xe30bf597bd739f2bedf428faa4be6f9e28328878` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xe5083481099607256631ed31ef734b19a0657777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xe6553e30fa6cdf6dbe86e10f4fd649953accffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xe79e759982cc024c1e586527fb4b821b95bd5fe4` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xe7fd9918d766358239e0c50254c986838e9f9ef9` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xe8aed9d4dc2c2cf52b53e71cd9ea34275e7a6a54` | market_rejected_or_unknown | liquidity, liquidity_usd, market_cap_usd |
| `bnb:0xe8fe2af0bc01a2dc246d7be4e6fc80c88969e46c` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `bnb:0xe92666a0db32858f8583137dddd58a3e9005eb15` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xebabaabd4d1cfd84543e142f88fb822de1f9ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xed9acd12dc82957a935be4cc0e8d514735d1ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xef23542224d67049dfcbbd90848529a2acc4ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xef75c7f3d5a2ac0ab779b5e8dc3d638228087777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xf2e0614fe822b6f42b707f8e258ad1931959b710` | archived_age | pool_age_over_24h_identity_preserved |
| `bnb:0xf4d56b1a09d6e8a643204a1b810470846977e725` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `bnb:0xf5e3102b5b9b93d8fa2814050409e0c8b0e1b5c9` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xf68857c5b907e6683994443998705dbc384f7777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xf70f969f0a4c7193dba7279897bdb979a900f596` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xf82a5063873c63c137a153872d0d75c9600dffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xf82b09d97d28c6668055a014eb95d24053ceb050` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap, liquidity_usd |
| `bnb:0xf8f2362a31e8515733a3e7a0909dc9a301827777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xf9af6c0e66e843e4a9dd0879e365620e52aeffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0xf9b969c76481c2e4b0e353bd5f76debeed9a7777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xfa76b0955510949793ab5c6944d39125b1cc517a` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xfc7e279dacd346c540de1f05cd7c1c008ccdffff` | quote_unknown | no_exact_token_pool_quote |
| `bnb:0xfd9af749b43fbe23aa542268a7a5af9b08f8ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `bnb:0xfff90f7c333eb251a4947960f18bbb804f317777` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x00c83aecc790e8a4453e5dd3b0b4b3680501a7a7` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x081131434f93063751813c619ecca9c4dc7862a3` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x0b38210ea11411557c13457d4da7dc6ea731b88a` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x0b59fdb1a233a7477ea14061004b9dd776e73cb3` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x0bab4d517ead5cbffa7309444c444c008c6741af` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x0c1f3412a44ff99e40bf14e06e5ea321ae7b3938` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x10dea67478c5f8c5e2d90e5e9b26dbe60c54d800` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x111111111117dc0aa78b770fa6a738034120c302` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x12109557d91bd3a2f53c945dd211f94556bc7178` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x13578129fc7fd3cb89f7481f8d0dd04e0ab50fe5` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0x14d6c649292c5c9790c5196d1a9ea039307947a1` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x17d5c9e785bbcaa1840fe70e4eda75060244b8de` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x19f0a86da690754bbbc587654cdf7b6e74799cd5` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `ethereum:0x1aaf5355ec10d70334218972421dbb333bdf16ea` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x20c9a9bec730f7d767200a8f2ad0c74c06c8ce3f` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x228af660c0e2c50fc3fedc57c54242895efa56ea` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x253692e393c868c5ae4d442926457177738480ca` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `ethereum:0x255666049ece3dafafce0bf85ded99726d36ff47` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x272b1ea5c348c06f5d62663d3014e26e9fd8e1a9` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `ethereum:0x288407b78e84d221c9700df1b983d0acf4275308` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0x28d9937c4137a9c685d29db4aee1a6f896aec6ea` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x2bf461e447565b19e99f2f22aa2649d0e5063493` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x2ed104cc4475dbd1fb2a3ae5af8e60f6d83ceb2a` | market_rejected_or_unknown | liquidity, liquidity_usd, market_cap_usd |
| `ethereum:0x31b9a6c97dfa728185bf4c086029d9e2640a1268` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x320623b8e4ff03373931769a31fc52a4e78b5d70` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x32b4d049fe4c888d2b92eecaf729f44df6b1f36e` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `ethereum:0x3506424f91fd33084466f402d5d97f05f8e3b4af` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `ethereum:0x3632dea96a953c11dac2f00b4a05a32cd1063fae` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x363ea45b622dbdf5b581b166e2a2e9bf30feedb8` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x385a8c6a5369b1d72dc9ef982034091f702c93a5` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `ethereum:0x389b9cf607a92438b9989e11749b5cab3752390a` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0x3a0ff81672c45f233f8f2ad39044417b04aaa40e` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x3a2e4a74be0cdf7388537aa3616297f6785ad38b` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `ethereum:0x3add3ed3d442a3b51b1bec9daa09cc11489626ea` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0x3e311906706153c8f3e2d1878f5271fdaac8b8f0` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x3f80b1c54ae920be41a77f8b902259d48cf24ccf` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x41765f0fcddc276309195166c7a62ae522fa09ef` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x41e5560054824ea6b0732e656e3ad64e20e94e45` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x4200c12a9fdd8f65fb56674add5c806340acceb5` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `ethereum:0x430792cb87e397d29f9306e0457bd01c7e12e817` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0x441b4a6e121e7501c83d8eaa58bd39e779771ebf` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x44bc8d75c4d5bcbd8bf7d4796715039a53d5ecf2` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `ethereum:0x4657fcf6898df58cb82670fd56589a92c9edd0b5` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `ethereum:0x47d8982457d52d3d59b87fe4913a07deb764c4e5` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x48063c6b5c0c43b2c8a3cfd7e523de80fa57b694` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0x495a19c7f6b071924bfadb4528fee630ab3ff136` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0x49dfe3ef95da5f77071dbe3f24d6767ceccd5422` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x4a7a50a1bff00b4cc8a869205a2cbd72ecade313` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `ethereum:0x4cb0693ed89a9862d35283ee33445bcce967cd65` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x4cd612a3607ca92c099a45852e350fbfb1ba6f81` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x4e969efde11d1fd06fbbc8a58924ba39c2f6d959` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x4f0486b1cfb0864380a047b680987149fe415dac` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0x4feef8b303d324a9de53d02da215ab6f168210b1` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `ethereum:0x4ff1b315146c4005870a116a4bf2c57837e82da4` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x512d0257cd318280740da60d432b5baa7b7480d2` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x514910771af9ca656af840dff83e8264ecf986ca` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x5283d291dbcf85356a21ba090e6db59121208b44` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x595832f8fc6bf59c85c527fec3740a1b7a361269` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x5adc19773129af513b73101fd90a998773d2d020` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x5ae0f4f3a8a16d040a846d98471c759de54d0000` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0x5bf1b2a808598c0ef4af1673a5457d86fe6d7b3d` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x5e07f414c9168736e8353c5ebb1d5475eddb1607` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x61fb0103f813d8791ec054d5104f76fccd3cf9f8` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x68749665ff8d2d112fa859aa293f07a622782f38` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x68ced165d4025549ede426c3849582493acdaae4` | market_rejected_or_unknown | liquidity, liquidity_usd, market_cap_usd |
| `ethereum:0x6aefb76c456ab580cdb4d597d71bfd3236b31ced` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x6bef15d938d4e72056ac92ea4bdd0d76b1c4ad29` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_to_cap |
| `ethereum:0x6c3ea9036406852006290770bedfcaba0e23a0e8` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x6d4d494a4ba7364ca622bf414edc2b827b4e1ce1` | market_rejected_or_unknown | liquidity, liquidity_usd, market_cap_usd |
| `ethereum:0x6e2a43be0b1d33b726f0ca3b8de60b3482b8b050` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `ethereum:0x70d1bf98f917a595713b943b8c10f9f82feec3e9` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `ethereum:0x7163957aeae1d4a52908fd91e75c62d90101dd26` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x7184da290a84937813bdaaace6119920c017c6ea` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x71d24baeb0a033ec5f90ff65c4210545af378d97` | market_rejected_or_unknown | liquidity, liquidity_to_cap |
| `ethereum:0x7b80a6ad4102325f5eb7c1d16f21d8a591484a63` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x7cf9a80db3b29ee8efe3710aadb7b95270572d47` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x7e8539d1e5cb91d63e46b8e188403b3f262a949b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x7f39c581f595b53c5cb19bd0b3f8da6c935e2ca0` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x7fd273c094ca05c8b65cc3bc11d122415377c503` | market_rejected_or_unknown | liquidity, liquidity_usd, market_cap_usd |
| `ethereum:0x80328afaa267e6260065c49926cdf7af6826a970` | market_rejected_or_unknown | liquidity, liquidity_usd, market_cap_usd |
| `ethereum:0x808507121b80c02388fad14726482e061b8da827` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x8290333cef9e6d528dd5618fb97a76f268f3edd4` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x834a12e864b117aabb990336c81f3e379427d363` | market_rejected_or_unknown | liquidity_usd, market_cap_usd |
| `ethereum:0x83b5dbcdcd66f01ff8fc8506061d062f42ce815e` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x84ca8bc7997272c7cfb4d0cd3d55cd942b3c9419` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0x858def6784a10825811d9319444411551117bbf4` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x86abcb60e2c5aaaa46aac4dc0058ce94de3ea1a2` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x86e7f83b2301170d1c16c1b702e4b1b876cf3eb1` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `ethereum:0x86ea42ba0ee511383945ede48e1e96e663b08b4c` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0x879c7062e50fb63c4acc530dc07f3fc05262cd4e` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x887e693d87ec22bca6439275c2869fe6b35c62a4` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x8d174a322c162ebc6ac016931ed43c005668b848` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x8e151537b85c5f3e868ee61c405a59df9612ce59` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x8e816bf5aa29bd5a382f3223be0aa08aebf613d5` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x8fee1d50d59e1ea58e4e80f22ce0887375a29ee8` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `ethereum:0x914a9a2d5aa5455662d81585cd8fc4f9207c38e1` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x9344d129d0c27ce94eae15c5d7c76a85def2e6ea` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0x9401efa3d5fd9a725c18aaedf849d0ff94c1d68a` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x97f5a2e1aea2806cbb6801d12176b9b30cdf63db` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x9916b843426f6eacd2f18a82e84145b65c004ed1` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0x9a65f56daf5d6b75ef841bbaf29da1b2503d315d` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `ethereum:0x9a7442f665092b808efa8158a564ed98b3918ecb` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0x9d0fdcfb65d82d10025776f2a8c326a375ba4844` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0x9d1a7a3191102e9f900faa10540837ba84dcbae7` | market_rejected_or_unknown | pool_age, market_cap_not_50k_500k, liquidity_to_cap |
| `ethereum:0x9d8852eb60a942d66eb3c482073dc018cbf29169` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x9dc9f4a23775019997d8e3c939e1adf8d4a4429a` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0x9eb2a83e6120436f36e2347706af60aad1e14e24` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0x9fc50fb79a86e067cf0ba76281814d62f5a0726a` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0xa12cc123ba206d4031d1c7f6223d1c2ec249f4f3` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0xa35923162c49cf95e6bf26623385eb431ad920d3` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0xa66e1958f5d5fef7736885b24f681f6e978af1c3` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0xa6c0c097741d55ecd9a3a7def3a8253fd022ceb9` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0xb30fe1cf884b48a22a50d22a9282004f2c5e9406` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0xb3121d0f6dffae47d0146a7caa2665c440aaf626` | market_rejected_or_unknown | liquidity, liquidity_usd, market_cap_usd |
| `ethereum:0xb5c6371fc90936b7e7565a2702bbe304dd659795` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0xb7535380a01e91e7b03376a658e18de437e2d56d` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0xb9e4e21e26f1ff9dd7cd4a0164594f61a4c24d1c` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0xbab77a55a57a4b54d14e27a04023dc1193c310e4` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0xbb0e17ef65f82ab018d8edd776e8dd940327b28b` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0xc00e94cb662c3520282e6f5717214004a7f26888` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0xc31b911916b884e26a69b612e4922e847126b276` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0xc38f8d6cf5c525be1566a3f0d0726f5fbc9ed1aa` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0xc54c84323e7698add6fd9fbf09b9fab3f74c51d7` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0xc591e8addb5675e6e1f9d692dac2b9a98d1433b4` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0xc83135cec8aef86574e10efeff9c503d29e754cd` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0xcc8fa225d80b9c7d42f96e9570156c65d6caaa25` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0xcd96d9b7145c2b0234c309dc24ace231f5b486ea` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0xcdf7028ceab81fa0c6971208e83fa7872994bee5` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_to_cap |
| `ethereum:0xd53d623cec2dc675c90c88dec20453c7d9e5ba10` | market_rejected_or_unknown | liquidity, liquidity_usd, market_cap_usd |
| `ethereum:0xd9a57f95ce87ac0846edd09ee7579257521a449c` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0xdba9c3de0d41a4247d74ca17b1a098366fcd9314` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `ethereum:0xdbc464d3c23319470280cd4aa907fe4a424a62f9` | market_rejected_or_unknown | liquidity, liquidity_usd, market_cap_usd |
| `ethereum:0xdc770c8cc8224f46feefbc04e3157f7e968c5010` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0xde4ee8057785a7e8e800db58f9784845a5c2cbd6` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0xded20a18efd9547420c1907d3d73a36c6415724c` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0xe0010654a46c4b98df47a70cb2c509ab380728c8` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `ethereum:0xe45f5252284347d6f319a718837e4506e951ffff` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0xe6e130ede11f22e44c8def95ebf44b677109b424` | market_rejected_or_unknown | liquidity, liquidity_usd, market_cap_usd |
| `ethereum:0xeb964a1a6fab73b8c72a0d15c7337fa4804f484d` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0xecf5d9a6cdd2231179f7fed802ae0533391c1752` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0xf1573edddb75bf7ce165f142a17ed6b5e7f5aa13` | market_rejected_or_unknown | pool_age, liquidity, liquidity_to_cap |
| `ethereum:0xf16b8fbac6e3e6b57c50797b77ccf067f3a9acdd` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0xf339b49164de270971ef24ced2b94ae9e8b2da64` | market_rejected_or_unknown | liquidity, liquidity_usd, market_cap_usd |
| `ethereum:0xf4d122876084968f91c7ffb7e839823272f39843` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `ethereum:0xf57e7e7c23978c3caec3c3548e3d615c346e79ff` | archived_age | pool_age_over_24h_identity_preserved |
| `ethereum:0xf5bba0e35447d55e4f74bb316347db48211634d1` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `ethereum:0xf6f64ff3b62f45c4aa261d61d97e4af800b619bd` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `ethereum:0xff54f150ff527b2faa3ef0ef35f28147109b74ae` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `hyperevm:0x074a60499539bdd3d85c5b28deea6067d9f1ffff` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `hyperevm:0x18f6dd58ddf682c3f197e02cc6917ed1c2417503` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `hyperevm:0x31538bc41c9a171707db639e0830f5f15184cfff` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `hyperevm:0x389ff560781bd54034e9ad829a965f1b78253b9f` | candle_queue | waiting_closed_candles_and_security |
| `hyperevm:0xd1c95876385c7cf5f747c67e68640769556d7e35` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `hyperevm:0xd53dc73ddbc8bfa122e81c87a1a09abde4e93d1b` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `hyperevm:0xee31509a163002f82ae8fc1f31687aa0a3af771e` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `hyperevm:0xf9573bd9313cccdff70f5d05aac0cce77dc88cba` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `robinhood:0x01ec5a5dc83fea756aa67c5d108700e6f9881111` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x04bcdbef7a710b1d8c3b9476728086c6c02da14a` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `robinhood:0x067c771cd6306e7c1c07d1c2c3993b38b11b0ebe` | quote_unknown | no_exact_token_pool_quote |
| `robinhood:0x07ecf67e2e1e6c1177e84cbb556ba3c7ba0ac6de` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x0846d4d1f5c6cbbe9bec47774256fdd684167b6d` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `robinhood:0x08f9d1a93305edc3cf01b5221253f4274ec50742` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x0b74574ef412fa93a212e02b72ac63c32cb282e6` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x0ba11760ad2dd242a35b06197f69f1214db31616` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x0bfc2fbfa2482f8fa514c79e78ede2f238444c38` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x0ca48128a7930f87a2c640dd21cc1593af6319fe` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x0d5e0a9d84f15ff3c9dad1111fad110443394e3b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x0dabaad62ac637f4315aa30c67017d0cf231bb71` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x0dc2912a30a30d6f25d389cc0ef725e877db1111` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `robinhood:0x0f1b7d0d1deb31a07d24bd4841473c5a068a1ff2` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x0f3a84add72fd8aa8c8471b08058f1a89785cfb8` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x105391c09472e506d709c9b5b8648f3b8092a890` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x11ae8b6b4a2333bacbed73903552425bc8f7f9da` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x120c5ec109eabc89caf3ea28445d72efa25fb9e8` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x12eff433b72b5dd72635df95f88a566abd9733d5` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x13206aff518b50c2199d026867d87287e5c103a1` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x14f14c85448ecbd28c07d6215335cf198c40a7f1` | market_rejected_or_unknown | liquidity_usd, market_cap_usd |
| `robinhood:0x183e54c5c041f665e750a78567e2b2791b1925f9` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x189b14fd8068003041625642f9ffc3d7adab0938` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x18b47df6aac7f41583d17af013d9e8421c509083` | quote_unknown | no_exact_token_pool_quote |
| `robinhood:0x18d2ad580c62f9566f7f3f2a4fd44caaf2c5f6ba` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x1a0fb8d289ab107c77be5dc0007c0855bb5a2027` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x1c33ac2c91fc6cdb1f1a6cbee6ebf3be15d531cf` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x1db225de32d3d985f6a89b5eadef4b47f2d51111` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `robinhood:0x1e828432fdc22c11cab58fcd6ad5c0c0ddad1111` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x1f4e33a225512a1d18b84b331e9a6c776a8c1997` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x205560dea79301dce018061a7a3f2df397a7d24a` | market_rejected_or_unknown | liquidity, liquidity_usd, market_cap_usd |
| `robinhood:0x227991c33e8c6618d83b378e347aaa789c059d45` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `robinhood:0x231413fe62b3118b6d82c9cb550f32140181d72b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x23780f8ea1d5ccd60c25386da04f55a17d686f82` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `robinhood:0x244be86d3103fbf935f1b99dc24a83485e12d72b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x26fce492116bdbd14b636d90d113fcd0d1870342` | candle_queue | waiting_closed_candles_and_security |
| `robinhood:0x28490b6c6bbe2ae9ad341588fed727603ba4d29a` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x28d55642d8cddbbb7e0d01d922ff48b4f8528489` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x29fb8e8f4ac7fd57771b2715d7b86aec9ddc54a5` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x2a525a135493e76d61272048980af1bf3dc53f77` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x2aa34bdbc2d10a55e7a3f174099392118879a151` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x2c6daa50b5dd6ec28eff999976c3f9e1a36f3264` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x2ee56162c1cf60b4a27bac8c095f0e6f624f6d8c` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `robinhood:0x30db6fc786caa908877638b0b95681b6e9d9d6e0` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x31f356885a1c91e2d314e5c7f4dcd8625d551111` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `robinhood:0x32185fca3429825677d0973ab6aabf8da78a50b1` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x32295a117a58e349a725baaefcd1a4bc80eed72b` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `robinhood:0x32f4365759286ee7e6c23937b7b2b9d944741edd` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x337675fc2e8411de24809878a4f0b2826af239a1` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x378277007ebbfdac9990796cd90dbf4148eb6e29` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x389ba203b3d11a70a618510c207a90187926dde8` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x39827b784a2f549964de2d924cad7f238a1e3097` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x3998f4109d8f0cd4abb9699e6321dd3688d59e48` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x3a1a5d71ddc27fcc8448f44f0cad1a940619bd55` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x3a9d8b602c05f9f49427e23385794d8be9bd82e2` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `robinhood:0x3e0262edbd873728e0921cc0a32d4b5a415c8ab4` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `robinhood:0x3e84362f7350128e3a3a6aa5b3f6cc40e29cd72b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x3f139b12744cae94ca67569b5121bcccc1b9d72b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x3f4d80cda19086155d8a0e73fb5bb88be1683c8c` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x3f7827126f7592c45b09965cfd8d267ba0190f65` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x3fa1deeeb86e79313d8d0d99f99294a5f5ded3d7` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x415cff3e28567b628e37ae9590e8f9c079206f11` | quote_unknown | no_exact_token_pool_quote |
| `robinhood:0x42428896973ef7137a56c898cece1f405f9e36ea` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `robinhood:0x429110f0dfe44c6d1a47a5ed240bd665ae88d72b` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `robinhood:0x430e5da808eceef1e61580a4a1d6b101fa298c0d` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x4434a685d7bfc12ac91d447c0f47da4e200f32eb` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `robinhood:0x448b04c5c7a67085445dd784eefee68b43be535c` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x449483f003cb7b795828d11f27d64407a612c8ce` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `robinhood:0x44e0bf6a8d236228c6f9a5a90f822101555c2a07` | market_rejected_or_unknown | liquidity, market_cap_usd |
| `robinhood:0x44eb56fd28dcb43138ac97a7ecef74172c40bfe9` | setup_wait_or_reject | selected_pool_initial_history_unknown |
| `robinhood:0x4574b6a9983de0553e4f65f0db475142b4c9baa3` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x46b8b0f5d432f45b74ce19922b7fbd81a9cebd6a` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x4764853896ee4cf198e10a037262b936d63e0087` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `robinhood:0x478c060531ef362d4ad25fb94f279d08ee8ddf10` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x48c576309227b8df8f41c71cacc4b671d0949cdc` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x49c60b50c1a9d5f18c65241be42520b40fa5e681` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x4ab69a41c8c6ddb087bf543dbadc8cfa35ccf377` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x4b8274ae3e3fc9e6fb8cb29884d0389aa8ce36ea` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x4cc3171d677312d97a9b511a353276fd9f10e74d` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x4d01b0b0ca174117e365f6eb4366ea0735e20087` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x4d63798cbf062f4f4cd5219517a34737d072f29d` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x4eb7cd78f4957eb1fd16b51626747422e7210a1e` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x5063c486ebe863f8682e8460c787467798873dd5` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x52a8dcf8747a0763a46fbe7e478ca05efeb49b47` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x5389b2b0db1c76190a939a06288107c8982eb150` | archived_age | pool_age_over_24h_identity_preserved |
| `robinhood:0x539494f344d4993f2459610648ffce7e24c4d72b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x54fc801d10f78f468307a0e87c76dab48f45e6ea` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `robinhood:0x5648dfa3f8a82db163af41f0d4e637290166a98c` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x56cf9e14e527d7613d83c0df7dcf943ec254144b` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `robinhood:0x59857ea6a90809e4c401c81b5cd5a58f5642df9a` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x5a95c55097c616ae513c688428d9909795231111` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x5af033968c2a6fd59fdff462781b74e60215719f` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x5ba541128475ec7c38ec8a367feb37f058bcf735` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x5c0255aaf4d600f82f2ebd7d5385d35d48d13bbd` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x5c1809719ba83005d3267daaa288e1c0b7765340` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x5d16ef576dcf01311314ef243048069f6c71808d` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x5e2fc06336104aeb9569648870c902e77372dc8c` | quote_unknown | no_exact_token_pool_quote |
| `robinhood:0x624a0ef3f8ea8c838202ab273ac0478cbd044e5b` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `robinhood:0x6439c3b221817911794399e312c5629af2a09e6f` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x664171112487c61154e37c1e34038dd2c76a1f93` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x66ce360e79b09f6ec5ec2265c452ee5562ac1e18` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x675ed82e0b8287e8f5767b7603ab8b302f3114cf` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `robinhood:0x680fc45b1a4b9a650e2d93cfdd296261aed1d27a` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `robinhood:0x6a036a92b2cd47d18a457e12d980828e1a7fd72b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x6c29673298073c847ccbee22ce84666c31bbf3dd` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x6cdece2c541cddcd17e8117e032917a06f8c5a96` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x7041f0302dbcfaafc8dde5f430ffc026999f097a` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x70f6e13440b028ff58cbbc5ccef21763268ab390` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `robinhood:0x7396a951f2a7beea02bd888d169ade82c3210087` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x7420f81bcf61902e9bf815cb47de0372441f357f` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x7617192045671950e842abd6f7549f1465e37751` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `robinhood:0x778f31b6308920b414e8c73980b47e248f1d9671` | candle_queue | waiting_closed_candles_and_security |
| `robinhood:0x7a3356b53aaa9f36ea7575a0d6bff7476bc94ecb` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x7c6ef4b3b859e87a190b025ba9aae636f1ef2926` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x7db1dde7e6de95c1b42c3f77bdf6146c0280353c` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x82f7d3854aa4c5e11664252551a47fe666af45bf` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x8340642f25d0735e40c4c481d208e16775adc48b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x85cda7c9d1792d1f9cb4c54561014cd4bed28a3c` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `robinhood:0x862b74ef8b8cc523d7b25d11e85faa73d895e137` | setup_wait_or_reject | no_closed_bar_after_actual_eligibility |
| `robinhood:0x8665ab573fe4c3c407369886468760457f740e47` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x86f0c41c9be5394fecdb5d0276b46a0cf85201ab` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x87c610ef377146ec3ada7602fa0385acd485407d` | data_unknown | gecko_request_reserved_for_buy_pressure |
| `robinhood:0x89c5c1f8fedc75062d4530e90274c4c2301cd6d8` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x8a03b613f090ef20162a11ca9a8c25f4f1611502` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x8a8b5cbb17bf8aa652549152ba3dbf8696650087` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `robinhood:0x8c70e38b48a719a02c74d9e60b1efdae93d27233` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `robinhood:0x8d67b3d369373ed709aa05ba88dd213703dcd6ff` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `robinhood:0x8fe631db4f29dd74d5432b1e1c5b8dd4ce078f82` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x9116b90ced6e159423fbf6b737be8c9b0d9d1111` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x91ccd4e9466f419a4a756be37c597833ea973f9c` | market_rejected_or_unknown | liquidity_usd |
| `robinhood:0x922be556ce73d7b4ea456626a25cd522a5d10087` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x9274dcf253d8c824f2078cc5094f203385380087` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x93894b29eaca563c4510e10f2946a8e578c0e6ab` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x95e762a3af5dd73e33de2624cbbf8349093a0087` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x96bf56b5e05b3da2a7203357d75b784e4477078a` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `robinhood:0x96cbf5f4c0d60a0d8d231e4ed78756736b69519d` | quote_unknown | no_exact_token_pool_quote |
| `robinhood:0x973b794959b9c577a4e9c01e14f6a709796ad72b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x97d64c4724d6825656ce9f994b1c0832d186b361` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x9b8a4c90d1f80c211156d9a198b5c4cfeb396016` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `robinhood:0x9c57b4b1a73f34a6844547d4198f935b5dea7842` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x9cc8a403a0658ffff6753362696eab7563e2c17d` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x9daa8c9f81495a827a07bcec610aded3e68a11cf` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x9ece503f23aa915e92535675a04d71aa0f733c8e` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0x9f2d1ca6592066f4b2a803fb7ea6bd920fbd104a` | quote_unknown | no_exact_token_pool_quote |
| `robinhood:0x9f9e7db6c8f5a14feff65085b317f53c50a6a659` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap, liquidity_usd |
| `robinhood:0x9fdae68d3d89847dad947fce2585c38cf6e5175b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xa0e3732f7fac704ab5799099bc0958fbe6e9fe31` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xa2f890b0f2e5b4fd5623d96a47526620ab5d78c4` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xa35e88e38b86e7772636790efebb5142f97d6398` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xa56299ccc21b40993067f31baa157ba78d45224a` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xa5ec23a6cb6d84cdb253834a67b2971e8b851fb4` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xa66e4d32588224e4e202c65d180b6626d39b3764` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xa748d17361fb4bcfbc3e542f805ec43fc386caf9` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xaa1da541b5c7a098572dfd4ed8186837af51c0dd` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xabbf09478dc3e1576cca03e51c65a08fcef61111` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xae3eb4aa102d2a910443124ab15a8d50c36a272d` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xafeac76bfff347929ab238f4376ededad18ad72b` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `robinhood:0xb4474316964f85a63e2be401bdee50682219d72b` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `robinhood:0xb508d0f071efcef63ff35abe579a0e1701271111` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `robinhood:0xbb6726b2b7ecf6b97853c91ad6a27b6f09f78147` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xbcd68c61250af10e76687c83999af6950bf8d72b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xbe6d622c9b6ff02db29853a690da0c79dd061145` | market_rejected_or_unknown | liquidity_usd, market_cap_usd |
| `robinhood:0xbf409ab561e82139e684f317259d2dc4ba0e8d1c` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xc0e0f8cad1d2e73979add3d5a1901c8cde8e1b16` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xc28eced96c7e4beaae1b2a5afd117247fb3d93f3` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xc3cb14a790b1c40877a8dcbf84ad3f7125c96bce` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xc988e680471dc035d1d5047bd50c16e767d0314d` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xc9f0a2d6cfeb5538c6b35594979cd98dcd6676c1` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `robinhood:0xcabdc91ee9308bdeed970d3fab676f65babe3628` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xcb3f0c6a77425be0f0d79e46b2a6b865a5d2e81f` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `robinhood:0xcb8b6aa98c15c08135ff06cde2f87caf6c6c3a75` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xcc1992ff30e689399e96547b31d5be7a59b72eb7` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `robinhood:0xccd879e22d2ade878ece138f8f565885b463d6ea` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xcd0011cdc6a34ad025b865f3f8b427e744465861` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xcd3faf429077cc8ba5d26fdf0966597b0cbfaca6` | quote_unknown | no_exact_token_pool_quote |
| `robinhood:0xcda048cfa4cca92f9e56931b5afdda4b51eae5c3` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xd086f891229cd123aadfcae7c4b40150a80fd9d7` | archived_age | pool_age_over_24h_identity_preserved |
| `robinhood:0xd51387a06deb6474be5a42a93150370081887c82` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xd5bdbe6077ed9b5859888d238965be5034d679ef` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xd62fc2f07a1abc1e64d5d3a6e09703b9e922b38e` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xd69567358331233a9e820cf21c11ba091b72b8bb` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xd69cb6f17e6497fcba1b43d2b677dd0defb62927` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xd6c303a52f7442031478bafab800e6e172e1b9a3` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xd881b7018bc45fec5051e1ab90e77d2e8c30bf14` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `robinhood:0xd8f29db36c9581c2de6c570c9b1c09dbce22fc55` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xd9dc84dd58aa748ea70822a40ddd620d58bd148e` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xdd4874c7357660d0393b6819b0ea0d9e85e918b4` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `robinhood:0xdee3866191713a08ef0e0659f87b2c51e8e9746d` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `robinhood:0xe00811800fbb3b6e8b82ff9f547030669bce592e` | market_rejected_or_unknown | liquidity_usd |
| `robinhood:0xe09aa20a635d5132fb0765da819191ffde2fd72b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xe1140e2c8d6ad65f06fd763f0383f0650cfe4e9e` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xe1afba9c9898b09f9b8073d5f5cb9d1279fe8e83` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xe25d9a7cf9878a37d021c6b7dd25e0378aceb1d6` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xe30ebeecf385bcb43fff69d860955a7ec8d6d72b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xe4fc539deec7c44694309ed256581b381feeead8` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xe651450c5705e4f47648c485f5431996eb23dc5f` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xe6bd4082d63e0c7cc3dbfa9f8e7611d1e1f6abfb` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xea32f8fbd65ee7595bc29587b746cf7a1599738b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xf0e24367d219d2a0e17ccb62c5d89192e31d368f` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xf1009f27e2e3358ebb6f702747d673eeb3056eba` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xf176ab04510b7e80265110b8b7254b5afc1b640e` | quote_unknown | no_exact_token_pool_quote |
| `robinhood:0xf25b4ec58c7d382ed321d0f7e06fea1d80d57fce` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `robinhood:0xf2a87792d6a4c0b41c1dc56a1b75975f1a45d72b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xf3316d72acb1b31819cd096c4c5ddcfde8210087` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xf461e4ec50bada3810467e85ac32b726bb65d72b` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `robinhood:0xf49edef92b4b553d814e3e60ac14e4bb0b51df20` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xf54f45b75ec1dd478e29974cf896ac237a6c1d96` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xf5b586d9c479329d314dd1fdd608c2b0fea924cc` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xf5bbb390ef02f385fc70fda77efaa3ead81d2c75` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xf5d0c85c5bb7c7e112dd52d8a35f9d8c15c0be7f` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xf986a4feb64b16e7107e037be2336be0f9f5750f` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xfb00a045e4cb5ff07a2205688da417b10de9c07e` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xfee1807d41720a2a82eeb8379af83fd6c6fde513` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `robinhood:0xff5b0860fa54341d83183018d76702902d27d72b` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:21uVRJCf3Ckuzs1xWcvW39yNuLXn35UnUgAeDqw9pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:23A9UQR1v3FayDdkGiUytiEi5LevhrDYhGqqnD6cRo5q` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:27M9MZ3yTUymhyzJuhdh7YvrG1GArGjsggyFzpnkpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:27MAUrTpZFYsQnWQZik59eeHJryXYBVZ7H7yKcwVpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:27MAzAKskbRu32atxqD9pigSD9x8fzNSoLQfnDShpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:289Wmwkdpr38NfvcooygqBwEud33YRYERoXeoHQrEz26` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap, liquidity_usd |
| `solana:2BAnah6cde2y6NAxmtPH4neWFFYE4aHs7aafrw5cpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:2HDC1qoCSP7GF2zA8DHTcWL3haN9oHUsd1ti4NrSpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:2HLKMHoWRHmvGb4uEwUTUL3oVrhW833RfENvhU4qpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:2Tj15thYdNXUQsHWdCBxvXV2sHLAjyUfHxZn8Ksbpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:2UFbdSPSY2uSfAHjrQrS4u3y9EzzpWxtmUcaexoYkGNA` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:2YYmkUD1FDK2qdbyqbKs8w98aLAwzFrG3mTyAZYfpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:2Yti8EALQ48KhmiL5kZKS2MjTGFKqz2iPtufK6jrpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:2bmV39wUDcMDm4khqBn9tWWAwhdo42iAXCFNxgc2pump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:2dEAGLnvaoQR9yki11yFxM7PTokL1UvvH54dQ869pump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:2gdYPqz7ph1cb9taM1NLAMv5Ubs3Wq6yHHMe5Sydpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:2heAX9cgENB2viBU6AfvVw7r5mxhBNcXGvWoydsJszr1` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:2vae76TRv1CiiNjsjyQyBc6kXhcq8atFUjfL2HdBpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:2vb7vkFrZcpn8yurbhucAhmj4b83Ky6aaxXxtx9ipump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:2wYeBQPrHEQonr3YtC6TBgJ7ik9RCLdqYvbStKcD2cYm` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:2yChwtT1fpWbjoYPJGvpUrcMugsAz9JMa3ERLZUgpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:31eNq5kVTM8Jd8ugFxrzbxznGqHh4tJ5jir3M86Npump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:38w8P97enhaSi6NXyiUG9XdxX9EpZFUCmaYGaFa8pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:3LVNzVuucgpyQYhTci1Wg8sjnvxoT6m1CUBvA7oSPeoM` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:3MyiJd3n4zM3TqhixwXZfbfyWHTzMZA4krtyrmTrWRMk` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:3PVFMsvJLN5s6MB9b1uHTKH3pWK8jS4CFF4gh8SSpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:3PsztTvj9dkFT5E42USLmhu6GEZRbAc6fBKMSs1Lpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:3TnYkBq9qjo3w2WwthtaXJVqzZTaw1tSHVhaZon1pump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:3mRUcHa6mAthV1GJ13TB8Tu8XRapJCZ2NL53jFMepump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:3ocEKE26DRXmcv5CsAtoL6od5xhmWDviHX3q3Z6zpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:3pYtPKCixYTmg5kwjE5GxpjUenvyJPfskEzy9wvSpump` | market_rejected_or_unknown | price_usd, liquidity_usd, market_cap_usd |
| `solana:3tbwaoF6SrKkHDqZdiuJz6iquR4xzHAHFMmE7t9ds5UR` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:3veGnzD5HerT8Z2pjpNhe9mWEAuE9hCmZQLdSt3z2dYM` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:3yT51fW6kYyeMppj3woTc5grDAdz6njD7VgnXJG7pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:43eEKp7K9uD5EYZvcjTa61mAuM1WHdmkbPcDoYUibZhb` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:44guUByuDqykw8tEhR5h6DEtiRDp2wXGUeViZg37pump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:49bMZfVozzUpAgVsZZVRyUhq9upU2AG7skXCSEqqygxo` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:4CEfpbEKdsmyLuJiLVCjwYRsVc4LaPP7nprkZoqEHWM5` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:4DNDapHG4ag8TfteZNd4hTrGGWLzbuzchhnLzLVZpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:4DYMzmJVyoz1Md6A6UjRNdZViikxuMHSaRGw3swppump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:4FKfNoLggMBNTmTt5fVQKoXZHHyppCPF7xFxD5dEpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:4H6M5tPECFCKwP6zmQYtxrhMz4QNJxCpVyBqtNhkLG6A` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:4KMnLsjYbaqQmF5VSH5Pz49rbkADBxrjcBRoEwTZpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:4N52BUEU8GppSjYrMhnGuFFfWG6hhMAiFmEfBikppump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:4RsvxAE5zfBa5L5z9pmDa48y3NQMLya29dZYHPhkpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:4qmLchkyBbX7PgBStpo8gkzbe474pgbRy6vMitgepump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:4sneNyF5942bfnCtWwBZBKiwW52Qsfn5jEUdUupHU5v6` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:4xo4E9G4b5Gcm63t9opHtR32y1SvW5tQy65E1yRG66u6` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:52VFaAQzeMbiH7Yd5Sv2a2F78BYhB7oKmhQnBNC7pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:54rYgBjbyokhZtN2BQdt6Uzd5ind2sX6U5b7XUDVpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:5CcbJmMGBvUyLiiwBk6gVomAPvzbd7gxDsHoz7SnS8wc` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:5LHUeD3eTfMkAd3mq1xknXsCnbUCJDUJcypbtzeLpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:5NjfEG3Dggx79HB6jY86P7BvzNuHLbz3PqZcvetXpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:5RUuC4EDohNoajGZtBHTWWPjvjKE8f7qhrnPRGUspump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:5btpmP4vEk3yDy5aNBB67PpiRTTzzn9uhbaYTP9xbonk` | market_rejected_or_unknown | liquidity, liquidity_to_cap, liquidity_usd |
| `solana:5ejdGQn98RQG8jMQPf2zVuMmGXH9VTbCaVCo3eBHpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:5nsEaQXFGfMXQSp9HsW4h2AYZcrrsHAWBViNB1gsuFgW` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:65HfAR1KCGnTUdsEQrys9dDRd6Ryn1e1sW5z7GPRYfKW` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:693QAn4fSv6qEP56TeMYeuBhfANGVh7LLCi6cWqbpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:696G3w4hmfYiPRAzUHHeSbyEx8W6XbRccMgTV8Cupump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:69HKpfQizVny2tvH4Qtz86bBZmrx9SEGRh4pR3Q5pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:6Btg6EMFcSVAVhS4ioEaTEzmAqsMtBGMfE2UEgrrpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:6Bvb4Vt2jd8ERJMsn8GXiyq8ThUxTGTobRaMjvMjpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:6BwJtmykmae3roP4HUEEYPn81q6ABtyhuiSyGDnNpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:6DbyhuPCaoSqALPc6gWH98PMXj2nnATD1dCRK3VBqobx` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:6KKo6ffeeQnP7FDVP7M4dQ91c2A7WD4GoNtP1PyJpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:6N8aKGWZFGWySBnKh2F6P87F9xJBVmLQp4iW6yqMpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:6TR6LccBR588QM14GZMPnaLX666oyfJHi2qzWajRpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:6f1Jit9Wy4y8aqnb6unb3MKskfv3yxykcthFcEGWpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:6iL9cyc73k13dm4ZiYdvet6uYksWTJ53y6JGkxYipump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:6oyntoKSX8uxR47ise5fNpjsthA9aBarMNVdGUNJpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:6yQfL6FWy7M8Q2aedWvQCoVxbXMjWUv2d6BWFAiTsnfq` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:6zCxsbTm3KeGY5MLKdLtXfWrRjugaXqVDn2Sck5ypump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:71KXaNGMit17StEMsXBcWbkW5NkS4DxC1oP6eACaXXBv` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:76gu7GpCDNP7t7MwRPm9TYR1WcUrzAEzAMPhKTBjpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:77g26U8Mir7moMhzSNFbBfCeMpk8PdrJBrDMBN77pump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:7BD66fjAHhGxhmRsdVo6uMoHdR2pU7tq78bjAvqYpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:7CbMey1qGfDPAydEnznPBDQxznSErgGsLWDiRfvpLsCG` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:7Cfwcby5ZvbzdB16YfHRVY1L6Ta8xJgrWpSMdux9pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:7FCMp6ZKkCzwFzF4uqY7vY7utZRBL2tEy3rLA7p1pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:7Jkt3iowL3VaGcNmB4QGmtAN3fCZwjWh7WUceknNpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:7LBxq9UqrKEaLiDQcJapYWSutTrEmvKo4ShEyAvedafd` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:7LTjDDc11prXRo5T34134ahfg9ndSDAAiAkcrZZb45Jy` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:7N3riGnTVrR5vbGPCzECWxBJ42QPoUaQyj11R3o8pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:7PaKzdBckfpbHzWXAowehc6yTDhUzbzddQ7QYFYapump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:7ciG1hugcWAvELgWy3ujR2ngPBk67hU124yW5VZ3n95T` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:7dmQEN4VGkdgopFr1jTnn8pP5Bids7es4hnceYAGpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:7gVJc55479jg38viUBwhxune4tZjYCef3S7UvWn3pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:7j7p25xKY94AUrhYmC7gKNPQrXBDjMBz5oJ4LZPwdeyj` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:7vRuW12zizEXpEQjg5RgbSkv8bkQimCzmbZz5iZvSAhf` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:7xd1mn6TiDuAHnJkLWKdVGb8pXG6jpPvJ7V77b6Kpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:87K3PGWwk1adfJKNpo3SEx5su3JbtNipUwhCau9bpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:8AHbBB8ovF7FLDiZhcgaDSSUvF3MPcdPsQk5mVYiBBy` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:8DwNDsFeo6n7FcS1PuJzZ2jd1teVRoGLBW3mGygkcQz8` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:8GUoRZCSzjfoA47FRBJ4MuNjjpyn3pWZDTkRePWNpump` | candle_queue | waiting_closed_candles_and_security |
| `solana:8SKjVHxmMQu7JbsKECzK5hHjqSRPPMPc8sryzxoxxqDZ` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:8SwfBTQF787An4HiVa2FBxgD46eK5Q3RyUtNyyPztXED` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:8ahAtNeAGJfbn8hCUzNVdtqyDgDJ654FY9yKQNynpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:8hqjb4oizRbXTWAsbk69AtvxcVfQ8tGKBziQuJq1pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:8inHsrgCKiLbbMrkqHxc7LcvPaCUscUiW55QWT8aD9zt` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:8jTLVunxXUuimc6rbZWGuTnXUxKGiEh68YG5JVcpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:8qKAfRFgwMj1mJD6a7YNmgziDf1kXwNSCWcMgabXpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:99oHhtRVUTDZ6D4mrREn6AG9GswzV2qB5nbTVfCZpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:9A5fPVR4Kb2sb7D1dw6raXoBRstWMLnDEz9n2uHbpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:9Ak8V4yShpRXPzB31mEkBpWc6BtHnT9v3sojfedLmfZm` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:9L9MZrRmyZQcir5Q21QDvmYmn5bPGjKoA7CApMdNpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:9MPjhNWJggzvZhbJcYhfcMx9nU1CuCRH2r7aR5ZHpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:9SucVFWzpKzdUTaTpafxM1t6DLqedSCWqC8JowUaLUsW` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:9T3sAnQ7mRWQBa2CRKvRHaUQ4GCCMPvzZpNzYA84aRmH` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:9UF1Y9BnZX1TDdf3b5pSUHAh8mdJjyMXigxkx2zapump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:9fBr7XDURHDUZnzNdMJzd3N38GUVfekCjUdoHaYwpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:9q3ovAPUf5JfBBMJNB2yjZ2nQM37oACLYoGsTa7Qpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:9sGZ8rRUDfLse6t8kwbeBju3RK4bwGPZF9z9aBXPpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:AEAcRNczhVgENM3PPwQCKkrsjgnjuKVM5jbeeY4hFKfH` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:APMC9uzN5Cyak8CAwLEmwhXoXwsvoisi3RPYNqdwpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:AWTLgF3zHU3pY13TieQDVeBP96qrWHZdsDH2ddCKpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:AYQtLTKHUxZZsqWdzEGxXkaezM7z39QJZRgih2EXpump` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `solana:AYZTaK1GLSAz2AWJ42WtobBWXWR8bbWb1i2kTkP7pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:AahA4rREjodxGGaZaq3gMFpvhHms1DDcDbnykfqppump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:AbkttRtWtaa4BwYy2msrBkyRfp8aeET3Ss7ScYqEKv9E` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:Abn47gParvpPXqbQA1gSYgAzpZouE9GjmwKNEgYsjpcD` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:AcGxxzD8YAzmnJbrZBjMwNsULbJLuKdfyJ1YAq7Lpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:An2LJMzdD4vXtgibWiwRZtU9H1okNVB8W7eaunvUpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:AowkmYWw9nQnmkoAcCxfGxCiQaHAgc8u2AE1gZ9P3hJb` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap |
| `solana:AptkjP9G8foK8s8Fx7odoCJLiwGAAWoPWUY3H2QBpump` | market_rejected_or_unknown | price_usd, liquidity_usd, market_cap_usd |
| `solana:B6epCucCTzHyH69UgkR69repUb7iWFgUuY6ZnRj9pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:BB4hRY6DiYoZjUxJgAUeEgDkYwMWp1fWpNnEpusprRkw` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:BFY2d69Fs8hzpwwSAb2bFqE1pruS9UZ9o15XNMHfpump` | market_rejected_or_unknown | price_usd, liquidity_usd, market_cap_usd |
| `solana:BHRAsbC7V8oJzNLAGw9XTmg2iSqjE6EJcY663Jg7BAGS` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:BJL1YYMCrMkUtL1rVmHjfXjyYtYoujqhc7EK9xdJpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:BKdcWFpchEvHk8NK13ofXVZKuASYz4XrmGnnJNV3pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:BQGbRPvh2C8q8keC9Xb3sJGjxqinr9uXPSPXBtUFpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:BRE2526PDV28m5EXuzeKTsj9vWHZz5BxcUjvHLPRpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:BU8CD8Vi8rkFafdvHHP1hCsWRdFouZC9X51mymh7pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:BXnj81MpAEfey3kBYLLAppYSiqthERZmTRm8oMrpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:BXxsEq5rjsd3fb6vt8C7eU8YhjrFtUGNwqM8scXRpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:BZNzHTgm6j268YbAQyVqJNowdBMXWcjQBfJSfNXgmx4t` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap, liquidity_usd |
| `solana:BeKNZdhqQvxpg4ZuCCWponEgtYsmj63UkxkH8SkJHEoQ` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:BgmnbJQzvs55QMH2rrXvGkBSU1NgJHiXT7UAWeY7pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:Boe4yb7edoiqmvqR9BwDCA5FaPxNC6iUNp1K2vytpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:BqknDx1ybL6z3mmJB6erdMHfZuFTogiSnSoH3K6Rpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:Bt6eBUytCqrgi4Eix7aLeRPLcgLtiBV5HjTmQoKkpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:Bt6pp5mRXBo4n93RGiuCJRxFivY5ZJJSGmjDnduuXgPW` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:BvAajwr3f5Xv5ssHkRyyXMXjB7QihtQ4nTJPXF9Ppump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:C4prd5Fm4uE9LG6pxwTXrVv7Z4nTm4xbtJJuDkVapump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:C8im5xEksnHGs5vDG3zMs3aUD5N9P5VRwYyYmg8Upump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:CAsGnkCSWpLZDubYYfMo5eSnajmAfR1ViQ4KpHJKpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:CM9HMUTNbyc2ie5d93xo1BHTh5DxyXuTaonegZGUpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:CPV3dpBr8SKoKyYtLNdL6M2yVS2eYtAsFdFhKGTwsRVq` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:CTU1MVP7YEztpKMRiqGeTcwTNM1rW344YjoRZ8Yh3SaW` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:CUxfHVagFzwXFWNFwtyLCxYQBy9qEouZNy3mUL3qpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:CW5qt88YKArEUPwZw2Bq7ar6QDm9u1Ye8S4AYGeNpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:CZPGVRhiaKWsAw8FLCCmQicngeuiPmQweEPhaGG7pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:CZZZojRHc4wcUFoHqRWeCxG9vGD5NgeY2kJs89j6pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:CkQW8Guh9drVeN58B1TEjFJdGi96rkW1HR7menKopump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:Covjxo4yp8SFYhFWgWvUi8esCQjpbvjPxvve6rQWbdN5` | market_rejected_or_unknown | market_cap_not_50k_500k |
| `solana:DDthBxuecucqGT8rqejBYFuYhuA8h8HTcXys8sN6Y5hd` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:DNCKXXEBg994zPQuiYVowrPSGgPmYeqKJr7aRRKspump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:DZQ3ckHSAs12jzSoVKhLVMpVLgfxLLuerP7RFngipump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:DcEpa1CLxUygZTDZHnWmA2sLfoqxAcpU9XjwvRpepump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:DfbB2eGuUN2XH1wgPk2dpzHfseaASJjeCN4jTyF1Fmiw` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:Dff7vnLTfAzxJyUYvjGtyq8CG8AaSBeZ7aatmdjzpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:Djjrzm3Zg8YBU2imK2qvcckB3W7Sq8nNXTTjTUx4pump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:Dox7uqYKkhyvmUM9JqjsPKTPUr6tFEGqAE5m8g7qpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:DwkMaQ3uwVTHhyAffQATJB1bkHsAWavQnHzVhZRLo3RP` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:E3SsmetuXvCyupp5robny5E9JnbGq7CnHHmDkomhpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:E7G7TZg9L8nw7PnzUEZGpqVg7X6tBPcSATSQkPfipump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:EAtHbbVfzUpJSsufWo8REN4BuYCznEqj8RUoozyVpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:EDUjdHth8HyfQR4MyMMPnxPaRMsX1jMCdSYhVxGMpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:EEcNaNKHsBn65GT6Qf8MzPxA5SfLRDkAXXKZbhQGDLJH` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:EGRWVKzr4CiKjrtuGJ6oovWiPMhRN1xozjeFYZxUpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:EGReCogKc7Daz9NfX1B8nb98nqqdMqqUDecSVBocpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:EGsCM5xzkcdsNgLa2AybL7cHAzGhkqHv2fjj61ZDpd8B` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:EJAjjRdqgqSYhyV4ocKiMPxuJTWn87LzZgvXmfqppump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:EJfZxzW7WMbXY9HysCfJ6XLcbFfF5e1X6SyhKbXjpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:EQsFta6grGSKGBLUKmrvcvvc2ayDcyjQBDsv9ctqpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:ER3Yyr3yTXXGvizA1YFPPmGzL5xajQk7e8nyHWswyBXf` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:ESCba8kYpK9MRA2EKTixRU4RHPUPSnN5wVwXohMdpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:EYzLTsAv2SeduB33UghfskmM27LgXA2T2GEWp5ZCgyST` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:EZf6fcKtUZimRRE3oT8Pqia39WUwBHztqhrC4EM3pump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:Ec9UzAxEstJPQnria8ck5oTXqhGhfb52whqBuqY9pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:EckWA2HBzXTKPz3DSgFpH2YVGediPvxBm2c8egXmpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:Edrs6WGtx6gnXycvvQUXEc3ceA3aMD2hFLCJbvR5pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:EdwG74FnzGDmnhs3HYpGJBqfzcAYvExynY4QVuTRpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:EfbYGTnjzHerFNFGAmRdGWs2GAS9W4agCgYvBuHSpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:EiBLU4tniRNgF7hdshLdmgEwBLDBygue9855qXt6JzSd` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:EsLUcoCDagZP2T6QardPRmikae6WwwMo91xBYokWpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:EwZg81cZ8JZLfC5TGya4gpzTn3aqZaAm9L3rGNQHjy2o` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:F4DW48B2HFKeCmvkvYxPi2rStY3MZXJKwD2UifdSpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:F8TU1B72N5AdVbLmkwb85EiYJk7Cniw8rrpuKxNxpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:F8TsZiLjfoVg3gKkF88kCia6ZWNNXR8kPpLgyekfpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:FMtRZxL5ighXcVGcYVFi8fzG4eVWErq4mPEPZUyTpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:FQV92ckRMuMct2GnrieFJo5PthDcpHbP8p365pbSpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:FRSiZGvtg7FMjXWSN8qZoTmLcsPg7WkRoHJ84uenpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:FTAPgMmh1WwPTgGNgmXa32EufAE5rUh7FYwFaC5bpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:FTN3dksA13LxdYGbVLAuTomW8ns5KpPSRYcZVzQHpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:FXKCz8r6MAVdyottFv8L9nfzGqbnD5Js5wcXD5DXdUy8` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:FYbHtpZpBUi8NbMUC5mdMVP2TQWs9GEWN7mzgobsEtaZ` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:FaXXfxCM9PdQGMHySBoeTKXDXicZHDG3rSLeEbZMpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:FhfJwunZo9LsJiVLQUQfKgSPP8Nn8RP6xHXfasgJuK7B` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:FjngdyxE8TRqn2kGs8BAk55FJCAn3oXgKdPM8FpBpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:FkaMPDYAQ18kYV1ULaNBHqM7jLJC25y6ZJq93maVnQhe` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:FtsNFJdCMmahPKGtsesDQxKEs4vTqjUc2jrgDC1oSnLZ` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:FvRXvrxY1LSJFMREYWr3TvtXJtUiEzPWYfw9DVm5pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:FvT2xT8jcmLXkaT5gLBzM6RK5VqxJsWjQHF9bmFYpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:FvroAc5RYNrWZh5NQcrsdtNJtuqwMb3ZFM6civoVpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:FyG1Jr13zj7U957aw1voxZPU7Rv1iA4YnQKSvTKBpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:G3bUqhSTUXXN2sYrxbg8kEY2SXGKzzKZgKcFTx1Ypump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:GBqaP5PkpTpNFQETjzWxihngwkfv2kE6r9Q5Wofipump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:GEBcV2jZ4gzLzQdHtYHGPdbwVkeppF3AVGQvcm5Ypump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:GKRKCPQxr7BYuhEvNEJjdBHHZdjZUjU4BPwvuW8Ppump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:GKuRWZzEpQQ78vujyXazLsWgfWPL7X4A3JA7xgwRpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:GRgm2SHUaYD6ooPuWPGpjw8vcFnSo5ytx12FEXKbpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:GXGbs2TJNHcrJkHgV6sdLW94EojSSypo65QxwkRjbMWi` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:GXqPiwiBkScgjTM1ryjardYSJKhx1CRT82yQ3dCJt6xW` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k, liquidity_to_cap, liquidity_usd |
| `solana:GZiWefyyohKqDQoJgG2i8VEj2zCNWYSB1vU1JP45pZCL` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:GaU3EJomXPbDAbpWFUY9ZegRRNJTrh5K6QLcKmWhpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:GdTRodabMmVC9DosCrHxFjwqTwo2uz9XvoTVEHnHpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:GzDzTLrMDHvEnd3ymTZqoWKiBxwVsLhn8XiqJdq7pump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:HBsdDrz7ejZVACn1uxXePoiT9vbHYVDZBgQ8Qp8Ypump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:HCRtHewhiQxPQQUbjFri4qrcuC4J1Xs6ctXJY6EysTWN` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:HFobNASZhRLT5WEhQeDjhRrPemVgRZz1S9istAMmpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:HG4Cj8Msuu4ApFumessJygZHiBaTCBzi41iFMCRCpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:HJjC42LnKwromzeDSqrGc7Zs8aBQe2HiQzTxh1bzduEW` | market_rejected_or_unknown | liquidity_usd, market_cap_usd |
| `solana:HP92TWUZDpeoMYazx71MMnUXYDWaHyvohuqhueU8pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:HTFygKQiLdeyKGo3nQjcyTw9LEMB86zYhbt3BoZ3pump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:HTLrfEWjBCSmDAM5iP26Hvrj3Sp7NCWratU9RuVYpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:HWz3UrDqUA3SzKyynAgjEiNZRt8T31E5YT5qDwUYpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:HZ1g3u6hTmm69gEo4yhrFpV2ZhjFHb9iXUburWo1pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:Hdv9xEWCffy8Mh2opjVWbZs3LRLdWEF7pPrqShpFpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:Hfabbuo4uZEXYZSjBPGJ9AqpPuoY4sc6nhm2ZcW6z2zP` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:Hfn11p2dYLyLauoWWdkLwCGmxcb5ukV5Yt7L1rZ5pump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:HgyrRWbymksZdUUmwSapZGqsYsRU22mghCeaYPVApump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:HjdemmspsRYG5yHtH5CCzHQZYNa5JvoySwdDGedZpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:HprqJZu7KGo4xEkZTcViHXCS4Bi993NPJTP8AkvSpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:HqEugm2TfdXQeVjRSD8HCFJAhWTr22YNQeaZEagdpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:HraMnATXYv6L9XKCDT1UT16P49xE5iq6fxSSB2tcpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:HspF9gQS3EwjtAYqU7dnW5NZ9fFrohRhSeibkWq2pump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:HvqqAGvmExFwt7tWCzKFA6jj5ydZvMsDFb2GkamN9fqf` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:HvuDKSCstFfQWsk6ptgxv56uJ9foKVd7JodcvQuTpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:HwGNCJVABCAy4njXAKAuLe8Vbrg6E2pYd9h4JcqXpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:HzFNpMrz92UHuToYQpbj4f73nPY55FeWeurQ5juBpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:HzLAN8SG5s3eVzWpZ24cspyaj6ipSn89xk5HJqBwpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:J3ySiCJgBqwVUNFj7P8Ck1Zfked8kSu4M37kN6Swpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:J57FMHywTihKZAZ7NjRg8yMXGzJ3FuEAMii9dxtMpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:J59VnecixZvXnpLZ3hHiDnWFiZkDQnXTudC94sWQpump` | market_rejected_or_unknown | market_cap_not_50k_500k, liquidity_usd |
| `solana:NSMbMkRwSNrFofg42KdqenM5gkR9pTdHHCttaM1Hype` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:QRDJ5P7oCj9aFker8qkgtJDnihZrchgL6vbArz5RzRq` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:Tsww3wfU5JHgafXW34qf49HyF492h9pJNqt3pGSpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:ZTP8x21uBeLrWcaDR87jgFh4czDqYePscfrqzvcTLEV` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:hzv1EdXSxsFK3K3rbtNqdVjDNX81AbbhLsuhq2Kpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:js8D48mkND4XRQws1VgfjVRLME8pnuBWG7cdED146Yu` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:oAB5GrQR9ZRh3hw4X9WjjquMPHK3ht7bT1xMpYfpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:ra4qZ68oPFuEhHR5hMRpUsGH5riMbRBuMyW68r3pump` | market_rejected_or_unknown | liquidity, market_cap_not_50k_500k |
| `solana:tRpHj5vQ1Vn2LAVyK2oTkFHjSQ4jscgfjwRkmmGpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |
| `solana:vLSgC79JATQZxAYNUfRot8HXc71jnFkzf1Etm6Lpump` | quote_budget_waiting | explicit_quote_queue_no_identity_eviction |

## Gerçek gözlem ve varsayımsal sabit miktar ölçümleri

Aynı ağ+kontrat bütün evre/havuzlarda aynı bağımlı örnektir. Radar, giriş ve güçlenme ayrı bağımsız kazanç sayılmaz.
Kotasyonda alınabileceği varsayılan token miktarı sabitlenir; gerçek alım yoktur. Sonraki satış kotasyonları ve %0.2/%0.5/%1 ilave maliyet senaryoları kaydedilir. Gas/tax/fill bilinmiyorsa gerçekleşmiş net kâr bilinmiyor kalır. Ara yol/stop-hedef sırası tam bilinmez.


V6 arşivi: {"branch": "scanner-state-meme-v6", "sha": "eed96185bdd46f567985a4a220fbef07c957d4d2", "fingerprint": "6125b19ab15e06089dabf2bf29605e95c0211c75678f202917710aec4cc63c82", "entries": 0, "receipts": 0, "note": "Immutable V6 SHA; old references are not V7 signals."}

İlk değerlendirme 50–100farklı kontratta ileriye dönük örnek hedefler; bu sayı kârlılık kanıtı veya sabit bitiş tarihi değildir.
