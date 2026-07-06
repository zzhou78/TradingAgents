# Trader Report - WOW.AX

## Tool Outputs Used
- Research Manager recommendation: Underweight.
- Market reference metrics: market:WOW.AX:2026-07-02:001, market:WOW.AX:2026-07-02:002, market:WOW.AX:2026-07-02:003, market:WOW.AX:2026-07-02:004, market:WOW.AX:2026-07-02:007.

## Action Consistency Check
**Action**: HOLD

The action is based on setup quality after the Research Manager rating, not on moving averages alone. Rating and action differ because research evidence supports the rating, but setup quality does not yet justify action.

Threshold result: HOLD score band. score is inside the HOLD band or directional research/execution gates are incomplete

## Setup Quality Assessment
Setup score +2: research alignment -2, trend +2, momentum +1, support/resistance +1, reward/risk +1, volatility/event risk -1, volume confirmation +0. Score band: HOLD score band.

## Setup Thresholds
BUY requires Research Manager Buy/Overweight, setup score >= +4, and execution confirmation from positive trend, momentum, and support/resistance. SELL requires Research Manager Sell/Underweight, setup score <= -4, and downside execution confirmation from negative trend, momentum, and support/resistance. HOLD applies when score is between -3 and +3, or when a directional score lacks research alignment or execution confirmation.

A positive score such as +6 can remain HOLD when confirmation is missing, because the score alone is not sufficient. BUY/SELL require both Research Manager alignment and execution confirmation.

## Research Rating Alignment
Research Manager rating: Underweight
Trader action: HOLD
Reason for agreement or difference: Rating and action differ because research evidence supports the rating, but setup quality does not yet justify action.

## Trend / Momentum / Volatility
- Trend regime: latest close 39.35 is above the 10 EMA, above the 50 SMA, and above the 200 SMA; trend component +2.
- Momentum: RSI 64.23, MACD 1.12; momentum component +1.
- Volatility: ATR 0.68; ASX event/liquidity caution component -1.

## Support / Resistance / Confirmation / Invalidation
Reference price: 39.35. Confirmation level: 39.69. Invalidation / caution level: 39.01.

## Reward-Risk Assessment
Reward/risk component: +1. The setup requires confirmation because a paper-study action is valid only when research alignment, trend/momentum, support/resistance, reward/risk, volatility/event risk, and volume confirmation are coherent.

## Event Risk and Liquidity Check
ASX-specific liquidity/spread/event caution is included. No broker order book, ASX depth feed, ex-date calendar, or live spread tool was used, so execution confidence remains capped.

## Rating-Action Tension
Rating and action differ because research evidence supports the rating, but setup quality does not yet justify action.

## Paper-study price framework
Reference price: 39.35 using market:WOW.AX:2026-07-02:001 from source date 2026-07-02. Confirmation level: 39.69 using ATR and trend-level spacing (market:WOW.AX:2026-07-02:007). Invalidation / caution level: 39.01. This is a paper-study framework and not an entry order.

## FINAL TRANSACTION PROPOSAL
FINAL TRANSACTION PROPOSAL: **HOLD**

## Evidence Gaps
- No live order book, intraday liquidity, options chain, or broker execution tool was used.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:WOW.AX:2026-07-02:001, market:WOW.AX:2026-07-02:007
* Staleness / expiry: Evidence is valid only for trade date 2026-07-02; refresh before reuse.
