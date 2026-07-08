# Trader Report - MSFT

## Tool Outputs Used
- Research Manager recommendation: Underweight.
- Market reference metrics: market:MSFT:2026-07-06:001, market:MSFT:2026-07-06:002, market:MSFT:2026-07-06:003, market:MSFT:2026-07-06:004, market:MSFT:2026-07-06:007.

## Action Consistency Check
**Action**: HOLD

The action is based on setup quality after the Research Manager rating, not on moving averages alone. Rating and action differ because research evidence supports the rating, but setup quality does not yet justify action.

Threshold result: HOLD score band. score is inside the HOLD band or directional research/execution gates are incomplete

## Setup Quality Assessment
Setup score -1: research alignment -2, trend +0, momentum +0, support/resistance +0, reward/risk +1, volatility/event risk +0, volume confirmation +0. Score band: HOLD score band.

## Setup Thresholds
BUY requires Research Manager Buy/Overweight, setup score >= +4, and execution confirmation from positive trend, momentum, and support/resistance. SELL requires Research Manager Sell/Underweight, setup score <= -4, and downside execution confirmation from negative trend, momentum, and support/resistance. HOLD applies when score is between -3 and +3, or when a directional score lacks research alignment or execution confirmation.

A positive score such as +6 can remain HOLD when confirmation is missing, because the score alone is not sufficient. BUY/SELL require both Research Manager alignment and execution confirmation.

## Research Rating Alignment
Research Manager rating: Underweight
Trader action: HOLD
Reason for agreement or difference: Rating and action differ because research evidence supports the rating, but setup quality does not yet justify action.

## Trend / Momentum / Volatility
- Trend regime: latest close 386.74 is above the 10 EMA, below the 50 SMA, and below the 200 SMA; trend component +0.
- Momentum: RSI 48.16, MACD -8.57; momentum component +0.
- Volatility: ATR 12.79; ASX event/liquidity caution component +0.

## Support / Resistance / Confirmation / Invalidation
Reference price: 386.74. Confirmation level: 393.13. Invalidation / caution level: 380.35.

## Reward-Risk Assessment
Reward/risk component: +1. The setup requires confirmation because a paper-study action is valid only when research alignment, trend/momentum, support/resistance, reward/risk, volatility/event risk, and volume confirmation are coherent.

## Event Risk and Liquidity Check
Generic execution/liquidity caution is included. No broker order book, intraday liquidity feed, options chain, or live spread tool was used, so execution confidence remains capped.

## Rating-Action Tension
Rating and action differ because research evidence supports the rating, but setup quality does not yet justify action.

## Paper-study price framework
Reference price: 386.74 using market:MSFT:2026-07-06:001 from source date 2026-07-06. Confirmation level: 393.13 using ATR and trend-level spacing (market:MSFT:2026-07-06:007). Invalidation / caution level: 380.35. This is a paper-study framework and not an entry order.

## FINAL TRANSACTION PROPOSAL
FINAL TRANSACTION PROPOSAL: **HOLD**

## Evidence Gaps
- No live order book, intraday liquidity, options chain, or broker execution tool was used.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:MSFT:2026-07-06:001, market:MSFT:2026-07-06:007
* Staleness / expiry: Evidence is valid only for trade date 2026-07-06; refresh before reuse.
