> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete first-source periods at three fixed primes

Coordinator derivation,8 October2026. This reuses classical binomial
congruences and the actual signed producer; it introduces no new producer.
The exact content remains h=g_B^2*c, c=gcd(U,V'), V'=(I-d^2)/g_B^2.
No uniform ALL-prime c estimate or primitive-error decay is proved here.

## Overlap and primary-literature gate

A5turn5 evaluates the original primes3 and5 but no uniform7/11/13 theorem.
The closed parent u0..7,p7/11/13 jets are only24 finite pairs. Scoped searches
in the current signed-producer reports/gates found no completed periodic
reduction of this actual U. This is a scoped check, not exhaustive absence.
The classical Lucas/Kummer machinery is reused. Andrew Granville's primary
Introduction,including its Lucas and prime-power discussion, was read at
https://dms.umontreal.ca/~andrew/Binomial/intro.html . No absent image formula
is silently treated as read; the precise elementary congruence needed below
is proved directly by Vandermonde, so no unread theorem supplies a hypothesis.

## The actual source truncated modulo p

Put C_n(t)=T_n(2t-1), H(t)=t(1-t)(1+t^2)^2 and K=H*C_(N-3)^2.
The source is eta(Q)=sum_r [ (t-1)^r ]Q * r!, and U=-eta(K).
With x=1-t,

    H(1-x)=4x-12x^2+16x^3-12x^4+5x^5-x^6.

Every factorial r! vanishes modulo p for r>=p. Therefore the COMPLETE
source, modulo p, is exactly

    U = -sum_(r=0)^(p-1) (-1)^r r!
        [x^r](H(1-x)*T_(N-3)(1-2x)^2)  (mod p).

The omitted tail is paid by factorial divisibility, not heuristically small.
For1<=r<p the exact integer Chebyshev coefficient is

    [x^r]T_n(1-2x)
      =(-1)^r * n/r * 2^(2r-1) * binom(n+r-1,2r-1).

The division by r is a unit modulo p; over Z it is performed BEFORE reduction.
This identity also follows from the already retained coefficient recurrence
a_(r+1)=-2(n^2-r^2)*a_r/((r+1)(2r+1)), a_0=1. The parent checks both formulas
at every computed coefficient rather than dividing the recurrence in F_p.

For0<=k<=2p-3<p^2, Vandermonde gives

    binom(a+p^2,k)-binom(a,k)
      =sum_(j=1)^k binom(p^2,j)*binom(a,k-j)=0 (mod p).

Indeed v_p(binom(p^2,j))=2-v_p(j)>=1 for1<=j<p^2. This last valuation follows
from binom(p^2,j)=(p^2/j)*binom(p^2-1,j-1); the second factor is a p-adic
unit by the elementary base-p expansion of (1+X)^(p^2-1) modulo p.
Thus every retained Chebyshev coefficient, and therefore actual U modulo p,
depends ONLY on N modulo p^2. The reduction holds for every actual N>=3.

## All original indices at p=11

On the prescribed original sequence N_u=9^(18+32u),

    N_0=3 (mod121),  9^32=81 (mod121).

The complete cycle is

| u mod5 | N_u mod121 | U mod11 |
| --- | --- | --- |
| 0 | 3 | 5 |
| 1 | 1 | 10 |
| 2 | 81 | 10 |
| 3 | 27 | 1 |
| 4 | 9 | 2 |

Multiplication by81 carries the final9 back to3, so these FIVE cases cover
EVERY u>=0, not merely the first five indices. The coefficient formula and
the displayed degree6 H make each U entry a bounded exact calculation.
The complete receipt is signed_chebyshev_first_source_period_certificate.json.
All five entries are units, hence

    11 does not divide U, and consequently 11 does not divide actual c,
    at EVERY prescribed original index.

This is an infinite fixed-prime theorem. It is not an ALL-prime bound.

## What the complete cycles show at7 and13

The N mod49 cycle has length21. U vanishes modulo7 exactly at the classes
u=13,17,18 modulo21. The N mod169 cycle has length39. U vanishes modulo13
at u=32,36 modulo39. Therefore U's being a unit at the first eight original
indices cannot by itself justify a uniform7/13 content exclusion.

NEW parent source jets at the FIVE first uncovered actual original indices
(13,7),(17,7),(18,7),(32,13),(36,13), with p^5 precision, pay every Gaussian
coefficient and g_B^2 division. They give v_p(c)=0 in all five cases.
At the7 cases, v_7(g_B)=1 and v_7(I-d^2)=2; the divided V' is a unit.
At the13 cases, g_B and I-d^2 are units. These five exact local conclusions
remain finite until the Gaussian evaluation and divided source have their
own complete periodic proof. No uniform7/13 theorem is asserted here.

## Security and remaining obligation

Both new scripts are parent-authored and use bounded mathematical inputs.
They ran in the key/network-denying sandbox. They do not load credentials,
run returned code, or recompute closed h/lambda/G/q receipts. The proof still
needs a quantitative uniform ALL-prime c estimate, followed by the actual
primitive whole-error comparison. Excluding another fixed prime does not
settle the rationality of e+pi.
