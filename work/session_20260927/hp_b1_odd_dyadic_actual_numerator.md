> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Odd-index dyadic germs of the actual b=1 numerator

Date: 2026-09-27. Author: root. Status: Sections 1–2 and their exact valuation conclusions FULL PASS in
hp_b1_odd_dyadic_germs_independent_review.md. Section 3 is a written
root corollary whose separate independent transfer review was not
completed before closeout; do not silently extend the germ review to it. This finishes the
calculation already running when the user requested early termination.

Use exactly H, K, A, B, C, Qpart and Delta from
`hp_b1_ternary_actual_denominator.md`; in particular K means the b=1
quantity K_(n+1), and C=K A-H B is the normalized actual numerator.
This note concerns the actual reduced quotient, not a coefficient clearer.

## 1. Dyadic index interpolation with a rigorous finite cutoff

Set R=b+2c, s=b+c and epsilon=(-1)^b/(2^c b!c!). On each disk
X=a+8Y with a in {1,3,5,7}, use the restricted series

H(X)=sum epsilon (X)_R (X)_s,

A(X)=sum epsilon (X)_R (X)_s D(2X-R),

where D(Z)=sum_(j>=0)(Z)_j. For K and B, the R=0 terms are
2 and 2D(2X+1). For R>=1 their summands are respectively

epsilon (X)_(R-1)(X+1)_s (2X+2-R)

and this expression multiplied by D(2X+1-R).

These expressions avoid division by X+1 on a dyadic disk. At actual
nonnegative integer indices they equal the finite Rodrigues contractions:
the falling products terminate before a negative argument of D can survive.

Every falling product of length L on such a disk has Gauss valuation
at least floor(L/2)+floor(L/4)+floor(L/8)>=7L/8-3.
Also c+v2(b!c!)<=R and s>=R/2. Thus each H/A kernel has
Gauss valuation >=5R/16-6 and each K/B kernel >=5R/16-7.
The D factors, whose argument has slope 16, are integral restricted
series. Their terms of length j have Gauss valuation at least floor(j/2).
These estimates establish convergence in Q2<Y>, independently of
any finite index data.

For precision 2^10, omit R>=55: the lower bound 5R/16-7 is
then strictly greater than 10. Omit j>=20 in each D. The finite
calculation checks coefficientwise integrality of EVERY retained H and
K kernel before performing modular division; the omitted terms are
already integral by the tail bounds. Thus all four germs are integral,
and products propagate the stated precision without a loss of guard bits.

## 2. Complete coefficient certificate, not integer samples

`check_hp_b1_odd_dyadic_germs.py` computes all coefficients modulo
1024, using exact integer falling polynomials and division only after
checking the requisite powers of two. The denominator's remaining odd
part is inverted modulo 1024. Its output is
`hp_b1_odd_dyadic_germs_checks.json`.

The full polynomials C(a+8Y), modulo 1024, are:

| a | C(a+8Y) modulo 1024 |
|---|---|
| 1 | 216Y+32Y^2+768Y^3+512Y^4 |
| 3 | 652+296Y+544Y^2+128Y^3 |
| 5 | 564+184Y+672Y^2+768Y^3+512Y^4 |
| 7 | 824+808Y+480Y^2+128Y^3 |

These represent all coefficients of the corresponding infinite series
to the stated precision. They are not values at four HP indices.

At X=1, H=K=0 exactly, so C(1)=0 exactly. The first row gives
C(1+8Y)/(8Y)=1 mod2 as an integral restricted series. The next
two rows give C/4=1 mod2. The last row gives C(7+8Y)/8=1+Y mod2.
The latter restricted series has exactly one zero eta in Z2, with
eta=1 mod2, and factors as (Y-eta) times a restricted unit of
constant reduction 1. This follows from Hensel and division by the
simple root; all higher coefficients reduce to zero. Put nu=7+8eta.
Consequently nu belongs to 15+16Z2 and the exact valuations are

* n=1 mod8, n>=9: v2(C_n)=v2(n-1).
* n=3 or 5 mod8: v2(C_n)=2.
* n=7 mod8: v2(C_n)=v2(n-nu).

The last equality allows infinite valuation. No assertion that nu is
an irrational, rational, or noninteger number has been proved. In
particular, the coefficient certificate does not imply a Diophantine
upper bound for v2(n-nu).

## 3. Actual denominator consequence outside the exceptional disk

For odd n outside 15 mod16, the preceding theorem gives
c_n=v2(C_n)=O(log n), including c_n=3 on n=7 mod16.
The already proved Legendre endpoint bound
v2(P_k)>=ceil(k/2)+1 for k>=2 gives
v2(Delta_n)>=(n+1)/2+2 for odd n>=3: use the even factor n+1
in its first term and the explicit factor 2 in its second term.
All H and K are integers.

The second-kind bound
v2(Q_k)>=3+ceil((k-1)/2)-floor(log2 k)
implies v2(Qpart_n)>=n/2-O(log n). The factorial component in
the actual numerator has valuation
n+1-2v2(n!)+c_n=-n+O(log n).
It therefore has uniquely least valuation for sufficiently large n in
these classes. Reduction of the actual rational quotient gives

v2(q_n)>=2v2(n!)-(n+1)/2+2-c_n
          =3n/2-O(log n).

Eventual Delta nonvanishing is supplied by the accepted fixed-b analytic
theorem. If the separate uniform-prime theorem at 5 and 13 passes
independent review, their factorial contributions can be combined with
this bound at the SAME n, giving

liminf log(q_n)/n >= (3/2)log2+(1/2)log5+(1/6)log13
                     > 2log(1+sqrt(2))

along odd n outside 15 mod16. The strict inequality can be checked
without decimals: the sixth power of the exponential base on the left
is 2^9*5^3*13=832000, while
(1+sqrt(2))^12 < (5/2)^12 < 832000.

Thus the gcd-reduced integer forms diverge on these classes, subject
only to that explicitly separate prime theorem's review. The dyadic
valuation theorem itself does not require the 5/13 result. It leaves
one dyadic analytic root as the precise obstruction; no whole-family
exclusion or rationality/irrationality proof is claimed.
