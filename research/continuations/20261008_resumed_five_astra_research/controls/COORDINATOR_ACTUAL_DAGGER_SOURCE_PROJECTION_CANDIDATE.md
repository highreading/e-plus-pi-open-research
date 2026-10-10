> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A second actual critical coordinate via a fixed macro projection

Coordinator derivation, 9 October2026. NEW parent application; DIFFERENT
proof audit PENDING. The general actual stationary law is now DIFFERENT-
passed in FULL A4turn25, with its harmless beta-zero hypothesis repaired
to L>=3 (the original domain has L>=62). The argument here uses the
complete actual law, not the old free exceptional-module perturbation.
This is a local evaluated proof candidate, not a full kernel, valuation
upper bound, primitive-error theorem or decision about e+pi.

Before the new calculation, scoped exact Desktop/current MD/TEX/TXT
searches for i_dagger, the proposed shifted coordinate, and standalone
7242 find no matching earlier source evaluation. Hash substrings are
excluded from the substantive search. Primary
[Davis, arXiv1301.6285](https://arxiv.org/abs/1301.6285), abstract read,
concerns p-adic limits of factorial units and infinite-power binomial
coefficients. That topic is relevant classical reuse, but no unread body
theorem is imported and no limit theorem is needed here. Kummer carries
and the finite factorial-unit identity below are standard reuse. This
is a scoped overlap filter, not an exhaustive novelty assertion.

## 1. Original coordinate and all finite boundaries

Keep the original A1/A4 ternary family and window. Write

    P=3^S, S>=31, g=P/27=3^(S-3), chi=3g+u,
    6/25<u/g<87/250, v3(u)=5, u/243=1 mod9,
    J_D=D/2=3621g+u, D=7242g+2u, I=3u-2.

Define the NEW coordinates

    i0=(g-1)/2-u+243,
    i_dagger=i0+1=(g-1)/2-u+244.

For sufficiently large ORIGINAL tuples both lie strictly inside0..I,
since i0>(1/2-87/250)g+242 and
I-i_dagger>(4*6/25-1/2)g-246. Their grades are13 and14 modulo27.
They differ from the earlier i_star=(g-1)/2 and its closed test.

Use actual q_v=(81vP-1)/2 for v=1,3,5,7,9, literal monic remainders
C_d, actual finite quotients P_d/P_(d+1), and the full14-term Omega source.
The passed exact recurrences give

    y C_d=C_(d+1)+b_(J_D)x^D,
    y P_d=P_(d+1)-b_(J_D),
    b_a=binom(D+a-1,a), b_(J_D) in27Z_3.

The polynomial y^(d+1) in C_(d+1)=y^(d+1)-x^D P_(d+1) is above EVERY
requested q_v-i0. Thus no monomial boundary can contribute at these poles.
The actual finite P_(d+1) has coefficient b_a at exponent J_D-a,
with exactly0<=a<=J_D. No infinite quotient is substituted.

## 2. A uniform finite carry-and-unit lemma

For exactly0<=n<=3621 set

    t_n=b_(n*g+243), B_n=binom(7242+n,n).

The addition controlling t_n is

    (D-1)+(n*g+243)
       =(7242+n)g+(2u+242).

The low-g addition (2u-1)+243 has NO carries. The low five digits of
2u-1 are all2, its digit5 is1 and its digit6 is0, since u has digits
1,0 there. Adding243 changes digit5 from1 to2 and changes no other
digit. Also2u+242<g on the original window. Hence all carries occur
in the coarse addition7242+n, and Kummer gives EXACTLY

    v3(t_n)=v3(B_n).                                  (1)

For completeness the finite factorial-unit identity is

    unit(N!)=(-1)^v3(N!)*prod_j (digit_j(N)!) mod3.

It follows by recursively separating multiples of3 from a factorial;
the complete unit blocks contribute(-1)^floor(N/3), with the remaining
digit factorial, and the recursion sums the factorial valuation.
In the binomial unit, the sign is(-1)^(number of carries). The high
digits and carry count are identical to those of B_n. At the low digits,
all digit-factorial ratios cancel except digit5, which contributes
2!/(1!*1!)=2. Thus

    t_n/3^v3(t_n)=2*B_n/3^v3(B_n) mod3.               (2)

Equations(1)--(2) are valid UNIFORMLY in the admitted u and g. They DO
NOT assert t_n=2B_n modulo27; that stronger unproved congruence is not
used. Only exact valuation and the leading unit are compared.

## 3. Complete source projection, with individual division paid

The14 sources are EXACTLY

    M=7299: (b,c)=(122,1),(41,3);
    M=7245: b=14,15,16,41,42,43,95,96,97 with c=18;
    M=7245: b=131,132,133 with c=-9.

Here M*g=D+t+Delta. Since9 divides both M,

    (1-y)^(M*g)=(1-y^g)^M mod27.                    (3)

To prove(3), put (1-y)^g=(1-y^g)+3E; the ninth-power expansion has
every nonconstant error in27Z[y], then raise to M/9. This is a finite
integer identity at the required precision, without a limit theorem.

For a source (M,b,c) at pole v, put

    R_(v,b)=(2187v-1)/2-27b,
    l=n+R_(v,b)-3621.

The target exponent q_v-i0-bP is R_(v,b)g+u-243. The coefficient
equation J_D-a+l*g=that target gives a=n*g+243. Its ACTUAL finite
range is exactly0<=n<=3621; binom(M,l)=0 outside0<=l<=M.
Using the literal C_d recurrence BEFORE reduction gives

    C_(v,i_dagger)
       =-sum_sources c*sum_n (-1)^l binom(M,l)t_n mod27. (4)

The NEW fixed arithmetic receipt verifies TERM BY TERM the paid targets
e_v=0,1,0,0,2 for v=1,3,5,7,9:

    3^e_v divides c*(-1)^l binom(M,l)B_n.             (5)

Together with(1), this pays the SAME target for every actual term in(4).
For terms at exact target depth, (2) gives their divided residue; terms
at larger depth are zero on both sides. Therefore the actual individual
pole divisions are now legitimate, with

    C_(v,i_dagger)/3^e_v
       =-2*sum_sources sum_n
           c*(-1)^l binom(M,l)B_n/3^e_v mod3.        (6)

Only at this newly paid coordinate is the general whole-numerator law
replaced by separately divided pole coefficients. No such permission is
assumed at arbitrary critical indices.

## 4. Exact finite receipt and its scope

[ACTUAL_DAGGER_FIXED_MACRO_PROJECTION_RECEIPT.json](ACTUAL_DAGGER_FIXED_MACRO_PROJECTION_RECEIPT.json)
is COMPLETE/CLOSED. Coordinator-authored exact integer binomial recurrences
form rows7245/7299 and B_n for n=0..3621. No rational recurrence division
is taken modulo27: each ordinary integer division is checked exact first.
All14 sources and five poles retain their actual finite boundaries.
There are152197 active term checks, all paid target checks PASS.

The resulting divided residues in(6) are

| v | e_v | Actual C_v/3^e_v modulo3 |
|---|---:|---:|
|1|0|0|
|3|1|0|
|5|0|0|
|7|0|0|
|9|2|0|

Each individual source subtotal also vanishes at its target. The bounded
calculation takes0.108 seconds in the no-network/no-key math sandbox.
It is a fixed macro arithmetic certificate, not an original-length source
table, a matrix solve, a random sample, or a rerun of the old729/full14
scans. Do not repeat this CLOSED receipt. Its uniform application requires
the proof of(1)--(4), which remains assigned for DIFFERENT review.

## 5. Whole stationary consequence, and remaining work

The HIGH coefficient zeta_i_dagger is also zero: the literal yP_d
recurrence reduces it to the same v=9 unit-source projection. That
projection has every term divisible by9 by(1),(5); every other source
coefficient is divisible by3. The boundary b_(J_D) is already paid.
At i0, HIGH has grade12 whereas q_9 has grade13, and LOW has grade12
whereas its five requested pole grades are13. Hence both contributions
vanish there by the DIFFERENT-passed actual general stationary law.

At i_dagger the whole numerator, before /3^29, is

    N_i=3^29(zeta_i-C1_i-2C5_i-C7_i)
          -4*3^28 C3_i-4*3^27 C9_i mod3^30.

Using the paid residues above and the actual nonzero interface unit a
gives the NEW parent proof candidate

    eta_i0=eta_i_dagger=0, h_i0=eta_i0+eta_i_dagger=0. (7)

This evaluates a second actual critical location. It provides no full
kernel/rank or leading-force compatibility and no modulo9 lift. The
main A1turn23 request is independently evaluating the remaining critical
coordinates; this unsent note should be compared against its completed
proof before another task is assigned. The true full leading kernel,
first-four ACTUAL next digit, physical7/source34, complete binary paired
upper, other primes, least clearer/ALL-prime G and same-index positive
primitive whole-error decay remain OPEN. No global conclusion follows.
