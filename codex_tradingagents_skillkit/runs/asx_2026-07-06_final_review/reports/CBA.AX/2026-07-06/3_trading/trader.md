# Trader Report - CBA.AX

## Tool Outputs Used
- Research Manager recommendation: Hold.
- Market reference metrics: market:CBA.AX:2026-07-06:001, market:CBA.AX:2026-07-06:002, market:CBA.AX:2026-07-06:003, market:CBA.AX:2026-07-06:004, market:CBA.AX:2026-07-06:007.

## Action Consistency Check
**Action**: HOLD

The action is based on setup quality after the Research Manager rating, not on moving averages alone. Rating and action are aligned by current setup quality.

Threshold result: HOLD score band. score is inside the HOLD band or directional research/execution gates are incomplete

## Setup Quality Assessment
Setup score +0: research alignment +0, trend +0, momentum +0, support/resistance +0, reward/risk +1, volatility/event risk -1, volume confirmation +0. Score band: HOLD score band.

## Setup Thresholds
BUY requires Research Manager Buy/Overweight, setup score >= +4, and execution confirmation from positive trend, momentum, and support/resistance. SELL requires Research Manager Sell/Underweight, setup score <= -4, and downside execution confirmation from negative trend, momentum, and support/resistance. HOLD applies when score is between -3 and +3, or when a directional score lacks research alignment or execution confirmation.

A positive score such as +6 can remain HOLD when confirmation is missing, because the score alone is not sufficient. BUY/SELL require both Research Manager alignment and execution confirmation.

## Research Rating Alignment
Research Manager rating: Hold
Trader action: HOLD
Reason for agreement or difference: Rating and action are aligned by current setup quality.

## Trend / Momentum / Volatility
- Trend regime: latest close 164.66 is above the 10 EMA, below the 50 SMA, and above the 200 SMA; trend component +0.
- Momentum: RSI 52.67, MACD -0.28; momentum component +0.
- Volatility: ATR 3.06; ASX event/liquidity caution component -1.

## Support / Resistance / Confirmation / Invalidation
Reference price: 164.66. Confirmation level: 166.19. Invalidation / caution level: 163.13.

## Reward-Risk Assessment
Reward/risk component: +1. The setup requires confirmation because a paper-study action is valid only when research alignment, trend/momentum, support/resistance, reward/risk, volatility/event risk, and volume confirmation are coherent.

## Event Risk and Liquidity Check
ASX-specific liquidity/spread/event caution is included. No broker order book, ASX depth feed, ex-date calendar, or live spread tool was used, so execution confidence remains capped.

## Rating-Action Tension
Rating and action are aligned by current setup quality.

## Paper-study price framework
Reference price: 164.66 using market:CBA.AX:2026-07-06:001 from source date 2026-07-06. Confirmation level: 166.19 using ATR and trend-level spacing (market:CBA.AX:2026-07-06:007). Invalidation / caution level: 163.13. This is a paper-study framework and not an entry order.

## FINAL TRANSACTION PROPOSAL
FINAL TRANSACTION PROPOSAL: **HOLD**

## Evidence Gaps
- No live order book, intraday liquidity, options chain, or broker execution tool was used.

## Memory Update
* Durable facts to retain: This run is a paper-study Codex-session workflow; Python prepared evidence and Codex wrote role interpretation.
* Prior mistake to avoid: Do not let template claims override metric evidence, filing section status, or as-of-date controls.
* Open questions: None for this artifact beyond disclosed evidence gaps.
* Evidence references: market:CBA.AX:2026-07-06:001, market:CBA.AX:2026-07-06:007
* Staleness / expiry: Evidence is valid only for trade date 2026-07-06; refresh before reuse.
