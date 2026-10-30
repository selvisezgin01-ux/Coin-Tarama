# 1 coin — V2 anlamlı hareket, sessiz birikim ve holder örneği

Exact same Solana mints1 andSPSC. Same single `1 coin` workflow, new state
`scanner-state-1-coin-v2`. V1 source branch and immutable source SHA remain in
`archive`, together with prior events, delivery receipts and pending messages.
All existing observed quote history, sampled trades and wallet baselines are
preserved. Old small pending notifications are archived, not replayed.

## Notifications

Single swaps notify only when amount >= max($100,0.1% of observed main-pool USD
liquidity). Smaller swaps stay in the sampled ledger and suppression counters.
This is a size filter, not a verified bot detector. A large trade is not proof of
wallet wealth, independent investors or smart money.

Quiet accumulation examines15/60minute windows from the retained observed pool:
at least3 buys, >=65% USD buy share, sampled net buys >= max($150,0.1% liquidity)
for15minutes (1.5x that threshold for60minutes), and observed price band <=2%.
Incomplete/truncated trade samples, stale reads or observation gaps block the
positive label. This is observed quote flatness, not a closed-candle pattern.
Repeated quiet notifications are suppressed for60minutes unless net buying
increases >=50%. Overlapping windows produce one notification, not independent
coin successes. Distributed small purchases can qualify even if no individual
swap reaches its notification threshold. Gross wash/churn volume is not net buys.

Wallet signatures are recorded but do not each create notifications. Parsed
changes for the watched exact mints notify only at >= max($200,0.15% liquidity),
valued at the contemporaneous indicative token price. Balance changes may be
transfers; no automatic buy/sell attribution. Price alerts1% and liquidity5%
alerts remain separately labeled; USD liquidity changes include price effects.

## Holder and relationship data

An initial candidate cohort comes from exact-mint Rugcheck top-holder account
addresses. Rugcheck source freshness is unknown. The account contents are then
revalidated using the documented public Solana RPC `getMultipleAccounts`:
exact mint/owner/balance plus finalized source slot. Missing/closed accounts are
unknown, not sold or assigned zero. Known AMM/locker owners are excluded. An owner
can hold unobserved accounts; this is not verified total wealth or a global
current top20 ranking. No largest-account scan is attempted after the prior
public-tier denial.

Watched seed owners' exact token accounts are discovered with the documented
`getTokenAccountsByOwner` method when available. Signatures for both owner and
known token-account addresses are checked. This includes token-account transfers
which need not reference the receiving owner in `accountKeys`.

Direct parsed transfers between non-infrastructure owner addresses are stored as
evidence edges, and sampled group balance changes are shown. They do not prove
common ownership, collusion, a fresh wallet or independent traders. Unverified
provider insider-group labels do not create ownership groups or positive alerts.
Only transactions actually parsed within the bounded watch contribute edges.

Source endpoint is documented public `https://api.mainnet.solana.com`.
The live probe verified40 known accounts. Public endpoints have no SLA and can
return403/429; method-specific denials/backoffs and unavailable data are exposed.
No credential, wallet signing, trading or paid API is used.

## Validation

`python -m unittest test_one_coin_v2 -q`

Sources:

- <https://solana.com/docs/rpc/http/getmultipleaccounts>
- <https://solana.com/docs/rpc/http/gettokenaccountsbyowner>
- <https://solana.com/docs/rpc/http/getsignaturesforaddress>
- <https://solana.com/docs/references/clusters>

This remains a bounded sampled watch, not complete real-time on-chain indexing,
guaranteed token safety, trading entry or realized profit.
