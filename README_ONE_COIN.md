# 1 coin

Independent watch for exactly two Solana mints:

- 1: `GMvCfcZg8YvkkQmwDaAzCtHDrrEtgE74nQpQ7xNabonk`
- SPSC: `4nswj3o1Lo9iWYvvRJxUD8vbCy9ay7QQoXYcncHNbonk`

No new-token age or market-cap entry filter. Does not trade or sign transactions.
Existing Coin5/Meme/Shortcu/pilot rules, histories and notifications are untouched.

## Operation

Workflow **1 coin**, `one-coin.yml`. Separate state branch `scanner-state-1-coin`.
Approximately five-minute observations inside bounded110-minute sessions. Hourly
GitHub schedule keeps one independent session/concurrency group; queued jobs and
external sources can introduce gaps. Report/state retain actual times, errors,
provider backoffs and interval statistics. A successful job is not full coverage.

Every new sampled swap after the first live baseline is logged and queued for
GitHub Issue notification, including small purchases/sales. Several new events
are grouped in one Issue; durable markers recover delivery after checkpoint
failure. Notifications contain exact copyable mint and Solscan transaction link.
First baseline trades are historical context, not retroactive live alerts.

Price changes of at least1% between successful observations and liquidity changes
of at least5% receive separate events. USD liquidity changes include price effects;
they alone do not prove LP withdrawal. Discovered main-pool changes reset price
comparisons between pools. The two most liquid exact-base-mint pools are sampled.
Quote-oriented pools, unreturned pools and centralized exchanges are not covered.

USD directional buy/sell amounts come from sampled swap records, not transaction
counts. Multi-pool routing is deduplicated by signature and direction using the
largest observed leg; this remains a sampled-leg measure, not verified net wallet
spend across an entire atomic transaction. Sample limits, invalid records and
uncovered intervals remain explicit.

Large trades >= max($500,0.5% of main-pool liquidity) add an initiator wallet to the
bounded watchlist (up to12 dynamic addresses, two rotated per cycle). They are
large observed trades, not verified whale wealth, smart money or independent
ownership. Newly observed buyers are not necessarily newly created wallets.

## Wallet monitoring

PublicNode's documented free Solana RPC is used read-only. A429/access block
causes a15-minute global backoff; no inaccessible interval is called empty/healthy.
Its public tier denied `getTokenLargestAccounts` with403 in the live probe. That
specific method is disabled for24hours while independently permitted signature
reads continue. Live largest-holder coverage is therefore unavailable unless a
later permitted read actually succeeds; Rugcheck snapshots do not fill this gap.
Selected seed wallets are checked each cycle. New signatures are notified even
if transaction details are pending. Failed transactions are explicitly labeled.
At most12 transaction details are read/cycle; remaining details are queued.
Signature pagination is checkpointed without advancing past an uncovered range.
The first signature history is a baseline. Unobserved old history is not backfilled
as a new movement. RPC availability and retention do not guarantee complete history.

Seed labels:

- `2LoNg8b8wYneseTQ4FYEVQxSJWp12tsLE799oUdYPDHB`: Solscan title
  **Squad Vault "WLFI - Treasury"**.
  <https://solscan.io/account/2LoNg8b8wYneseTQ4FYEVQxSJWp12tsLE799oUdYPDHB>
- `2x6Uhxmaot1cpiRisNwUcaQFPJCryGE4aTdpTYhYLENS`: wallet associated with
  WLFI in a Lookonchain publication; not independently authenticated as sole/main
  treasury. <https://www.binance.com/en/square/post/30239515666658>

Neither label claims coverage of the complete WLFI entity or cryptographic proof
of corporate ownership. Arkham automation is not connected and has no API key.

Parsed token balance changes and explicit source/destination token transfers are
recorded separately from swaps. A direct recipient can join the bounded watchlist.
An edge is an observed transfer, never proof of common ownership. SOL funding,
all-mint transfers, every holder, global new-wallet creation, wallet wealth,
exchange-attribution and arbitrary multi-hop clusters are not comprehensively
indexed. Report these as unavailable, not negative evidence.

Every15minutes, read-only RPC attempts the largest20 token accounts and their
parsed balances. Known AMM/locker owners are excluded. The same sampled owner's
balance changes are notified as account-balance changes, not purchases. A dropped
top20 account is not assigned a zero balance; owners may hold unobserved accounts,
so the aggregate is not their verified complete holding.

Rugcheck report snapshots retain holders, authorities and provider-reported
insider-network data. Their source freshness is unknown (`detectedAt` is not a
last-update guarantee). They do not trigger verified holder accumulation alerts.
No score or absence of a warning guarantees token safety.

## Validation

`python -m unittest test_one_coin -q`

Official reference sources:

- <https://docs.dexscreener.com/api/reference>
- <https://api.geckoterminal.com/docs/index.html>
- <https://solana.com/docs/rpc/http/getsignaturesforaddress>
- <https://solana.com/docs/rpc/http/gettransaction>
- <https://solana.publicnode.com/>
- <https://api.rugcheck.xyz/swagger/index.html>
