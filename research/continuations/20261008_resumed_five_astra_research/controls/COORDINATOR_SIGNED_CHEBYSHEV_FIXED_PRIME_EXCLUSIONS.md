> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Original signed-source content: exclusions at7,11,13

Coordinator proof,8 October2026. Independent review is required. This note
supersedes the finite-only7/13 scope in COORDINATOR_SIGNED_CHEBYSHEV_SOURCE_PERIODS.
That earlier note was already admitted in a request and remains unchanged.
The earlier theorem at11 and all source/normalization definitions are reused.

The conclusion is an INFINITE FIXED-PRIME theorem on the exact original
N_u=9^(18+32u), u>=0. It supplies no quantitative ALL-prime upper bound for
c and no proof deciding e+pi. The actual content remains h=g_B^2*c.

## Reused source-period proof and receipt scope

Classical Lucas/Kummer/Vandermonde congruences and Gaussian Chebyshev
evaluation are reused. The preceding note's archive/primary-literature
gate applies. A5turn5 did not evaluate these three uniform exclusions.
Its independent content theorem is still a separate audit obligation.

Let z=-1+2i, C_n=T_n(z), with real/imaginary parts a_n,b_n. Keep
B=b_(N-1)*C_N(t)-b_N*C_(N-1)(t), d=a_N*b_(N-1)-a_(N-1)*b_N,
g_B=gcd(b_N,b_(N-1)), U=-eta(K), I=eta(B^2), V'=(I-d^2)/g_B^2.
Here C_n(t)=T_n(2t-1), eta=sum of endpoint coefficients times factorial.

The already proved full-source reduction is

    U mod p depends ONLY on N mod p^2.

It follows from truncating at r<p (the factorial tail vanishes) and using
the paid integer formula

    [x^r]T_n(1-2x)=(-1)^r*(n/r)*2^(2r-1)*binom(n+r-1,2r-1),
    x=1-t, 1<=r<p.

The division by r is a unit. Vandermonde and v_p(binom(p^2,j))>=1 for
j<p^2 prove the period without reducing a nonunit recurrence division.

The COMPLETE first-source cycles, computed with two independent exact
coefficient formulas, have these exceptional classes:

| p | cycle length | classes where U=0 mod p |
| --- | --- | --- |
| 7 | 21 | 13,17,18 |
| 11 | 5 | none |
| 13 | 39 | 32,36 |

For unit-U cases no further arithmetic is needed: c=gcd(U,V') is a unit
at that p regardless of g_B. All such cases are reused, not recomputed.

## Gaussian transfer periods with explicit finite verification

Use the actual Chebyshev transfer matrix

    T(z) = [[2z,-1],[1,0]].

Since C_(n+1)=2z*C_n-C_(n-1), a matrix period is a period for BOTH actual
adjacent Gaussian values. In the Gaussian residue rings, the following
bounded identities hold:

    T(-1+2i)^24 = I_2 (mod7),
    T(-1+2i)^84 = I_2 (mod13).

Both identities are verified by exact modular matrix powering in the
complete-period certificate. No group-order theorem is assumed. For the
first identity write T^24=I+7A over the integral Gaussian ring. The finite
binomial expansion gives (I+7A)^7=I (mod49), since the linear term has49
and each remaining term also has at least49. Hence

    T^168 = I_2 (mod49).

This is enough to control b_N/7,b_(N-1)/7 and d/7 modulo7 whenever those
imaginary coefficients are divisible by7. No full polynomial is evaluated.

## The three7-adic cases

Every original N is9 modulo24. Therefore knowing N modulo49 determines
N modulo168 as well: the fixed modulo24 component and modulo7 component
determine the required modulo24*7 residue. The entire N mod49 cycle has
length21, so BOTH the modulo7 polynomial jets and modulo49 Gaussian
values return after21 original u steps.

At each of the three zero-U classes, b_N and b_(N-1) are divisible by7,
and at least one divided coefficient is a unit. Put

    B_tilde=B/7, d_tilde=d/7.

The following table reuses the five NEW original source-jet receipt's
three7-adic cases. All displayed divisions were exact before reduction.

| u mod21 | b_N/7 mod7 | b_(N-1)/7 mod7 | d/7 mod7 | (I-d^2)/49 mod7 |
| --- | --- | --- | --- | --- |
| 13 | 2 | 3 | 0 | 3 |
| 17 | 1 | 1 | 6 | 1 |
| 18 | 4 | 0 | 2 | 5 |

The last column can also be read directly as

    eta(B_tilde^2)-d_tilde^2 (mod7).

Its complete source needs ONLY degrees0 through6 and their factorial
weights. It consequently depends only on the modulo7 Chebyshev jets,
which have period49, and the divided Gaussian values, which have period168.
These are already synchronized by the original21-step cycle. Thus the
three rows cover EVERY zero-U case, not only u13,17,18.

In all three classes v_7(g_B)=1 and v_7(I-d^2)=2. Dividing by the ACTUAL
g_B^2, rather than49, only multiplies the last-column residue by the
inverse square of the unit g_B/7. Its being a unit is unchanged. Hence
v_7(V')=0 and v_7(c)=0. Together with the reused unit-U cases, this proves

    7 does not divide c at EVERY original index.

## The two13-adic cases

The complete N mod169 cycle has length39. Original N is9 modulo12, and
N modulo7 has period3 in u because9 has order3 modulo7 and the32-step
multiplier preserves that order. Thus u->u+39 preserves N modulo84=12*7.
The modulo13 Gaussian pair has period84 by the explicit transfer identity;
the modulo13 polynomial jet has period169. Both are synchronized by the
39-step original u cycle.

The two zero-U cases reuse the original p^5 receipt reduced modulo13:

| u mod39 | a_N | b_N | a_(N-1) | b_(N-1) | d | I-d^2 |
| --- | --- | --- | --- | --- | --- | --- |
| 32 | 4 | 6 | 5 | 5 | 3 | 3 |
| 36 | 11 | 10 | 10 | 6 | 5 | 1 |

All entries are modulo13. In both rows g_B is a13-adic unit and I-d^2
is a unit. The complete source and Gaussian periods prove these rows cover
all corresponding infinite classes. Therefore V' is a unit there. Combining
with all other unit-U cases gives

    13 does not divide c at EVERY original index.

At11 the earlier five-case unit-U proof already covers every original u.
Consequently gcd(c,7*11*13)=1 on the exact prescribed infinite sequence.
Together with A5turn5's separate accepted3/5 and dyadic claims, the local
consequence is c=4*c_odd with gcd(c_odd,15015)=1. That combined statement
remains subject to the independent audit of its underlying content theorem.

## Larger complete receipt and the remaining scope

The longer source-period algorithm independently uses jet modulus7^5,
Gaussian modulus7^3 and combined N modulus403368. It closes7203 classes,
reusing6174 unit-U cases and the three old original jets, and evaluates only
1026 previously unresolved source classes. Every divided V is a unit.
At13 its39 classes reuse both old original jets and all37 unit-U cases;
no new complete source computation is needed. The larger receipt agrees
with the SHORT proof above, which suffices without importing a7203-row
table into a prompt. The full JSON remains available locally for audit.

The general jet-period budget in that larger check is proved as follows.
For precision p^s and retained degree r<J, let b=floor(log_p(2J-3)) and
d=max_(1<=r<J)v_p(r). With L=p^(s+b+d), Vandermonde gives every binomial
difference divisible by p^(s+d); the exact division by r loses at most d.
Thus every coefficient is periodic modulo p^s with N period L. This pays
the nonunit coefficient divisions instead of silently working in F_p.

Neither proof computes h/lambda/G/q beyond the already proved content
identity. It does not control primes>=17 or their depths, establish a
uniform upper bound for c, or imply nonzero primitive whole-error decay.
The scripts are parent-authored, bounded, and ran with keys/network denied.
