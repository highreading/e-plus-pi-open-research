> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Correction of the low-row interpretation — 7 October 2026

The coordinator incorrectly inferred that all six extracted profiles vanished
from the five zero aggregate coefficients and the absence of paid-division
counters. That inference was false. The saved computation itself was unchanged
and already gives a0=14 and bprof0=20, as A2turn2 correctly derives by hand.

Reading the actual saved profile arrays gives:

| Profile | Nonzero entries | Value at ell0 |
|---|---:|---:|
| first-column leading a |414|14|
| first-column JK bprof |414|20|
| first-column011 correction |3|0|
| second-column leading g |0|0|
| second-column JK dprof |0|0|
| second-column011 correction |0|0|

The three nonzero first011 entries are at ell5046,5047,5048, with values1,2,1.
Thus the original five zero COEFFICIENT values survive this one-row diagnostic;
they follow in the displayed dictionary because the second-column extracted
profiles vanish. Source/dictionary completeness and the observable-order
omissions still need independent mathematical review. Constant000 first
corrections are not among these six profiles and have not been asserted zero.

No code correction was made to force a desired answer. The original certificate,
profile bytes and prompt snapshots are preserved. A separate diagnostic file
reproduces the coefficient result and the hand-checkable lowest row. The
interpretation receipt records the actual nonzero counts and profile-file hash.
The all-zero-profile assertion in later assignments is explicitly withdrawn.
This is an evidence-interpretation correction, not evidence of an API attack.

The source completeness, primitive growing-depth contraction, all-prime gcd
and whole nonzero same-index error remain separate mathematical obligations.
