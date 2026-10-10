> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the first even-degree P coefficient gate

Date: 2026-09-13. Reviewer: audit_sources.

**Result: pass.** I independently checked
`raw_even_P_first_dyadic_gate.md`, including the new one-gap
bordered-Cauchy estimate, the two actual coefficient rows, and the
common-scale top-block identity. The proof establishes the strict
inequality for p_1 in every even degree n>=2. Its p_2 gate remains
open; the note correctly treats exact top-block vanishing as only
one part of that problem.

## 1. The one-gap alternant and its exact factor

Let M={0,...,R-2,R}, with M={1} for R=1, and let

    f(m)=(-1)^m product_(i=1)^(R-1)(x_i-2m),

where the x_i are distinct odd integers. Write delta for the forward
difference in m. The shift calculation in the note is correct:
delta^j f(0)=(-1)^j(S_2+I)^j g(0), with
g(s)=product_i(x_i-s). Since (S_2+I)/2 preserves Z[s],
delta^j f(0) is divisible by 2^j.

The values of f at the nodes in M are represented by the Newton
series through index R; higher binomial coefficients vanish at
these nonnegative nodes. The terms of degree <=R-2 have zero
divided difference of order R-1. The binomial of degree R-1
contributes 1/(R-1)!. Reducing the falling factorial (m)_R modulo
the monic node polynomial leaves leading coefficient 1 at degree
R-1, because the sum of the modified nodes is one larger than the
sum of 0,...,R-1. Consequently

    [M]f = delta^(R-1)f(0)/(R-1)! + delta^R f(0)/R!.

I independently derived the determinant factor from the ordinary
bordered Cauchy alternant. Its denominator is a product of odd
units. Its numerator contains V(x)V(2M), followed by the divided
difference in the pole variable 2m. The factors are

    V(2M)=2^(R(R-1)/2) R product_(j=0)^(R-1) j!,
    [2M]f=2^(-(R-1))[M]f.

Thus, up to sign and odd units, the determinant is exactly

    V(x) 2^((R-1)(R-2)/2) product_(j=0)^(R-2) j!
      times [R delta^(R-1)f(0)+delta^R f(0)].

This is the factor in the note. Its bracket has valuation at least
R-1 for odd R and at least R for even R. These are precisely the
parity bounds in the original consecutive-pole estimate. No claim
that the modified determinant is an odd multiple of the old one
is needed. For R=1 the bracket is f(1), an odd unit, so the
empty-product case is included. A parity translation of the poles
only changes the odd x_i and an irrelevant common sign.

For a square Cauchy block, the pole Vandermonde gains the factor
R and all denominator factors remain odd. This also cannot lower
the original valuation bound.

## 2. The c_(n-2) determinant and its normalization

For n=2R, deleting the actual c_(n-2) coordinate leaves R even
poles {0,2,...,2R-4,2R} and R odd poles {1,3,...,2R-1}. The
nonzero C-border terms split into one square block and one
bordered block, both with R columns. Applying Section 1 to the
modified block gives the same lower bound L_(n-1) as for the
original leading C coordinate. If the endpoint border instead
belongs to the exponential block, both C blocks are square and
the original pure bound 2S(n) is retained.

The exponential columns have degrees 0,...,n. Their integral
binomial alternant gives the lower bound S(n+1) for the numerator
factorials. The largest possible sum of selected row-factorial
valuations is H_n+phi(2n), at rows {2n,...,3n}. Therefore the
C-border terms have valuation at least

    S(n+1)-H_n-phi(2n)+L_(n-1).

The other border assignment has the stated strictly positive gap
2+n+2phi(n-1)-c_(n-1)^val. The coordinate cofactor quotient has
no appended-row factorial, and subtracting V_n gives

    v_2(c_(n-2)) >= -n-2phi(n-1)-2 epsilon,

with epsilon=1 for n=2 mod 4 and zero otherwise. This proof uses
lower bounds for all row sets and does not require identifying a
unique least term in the modified minor.

## 3. The h_2 row, including the degree-two boundary case

The ordinary Taylor reconstruction of a_(n-2) contains only
nonnegative arctangent indices. Extending its negative row by
t_(-1)=1 supplies exactly the additional term -c_(n-1).
The only other newly encountered index is -2 at column c_n, whose
parity entry is zero. Hence the modified row is exactly the row
for h_2=a_(n-2)-c_(n-1), rather than an inferred cancellation
between two separate coefficient estimates.

All nonzero signed Cauchy denominators are odd and nonzero; the
possible denominator -1 does not affect either alternant identity
or the integer Vandermonde lower bounds. The ordinary row index
k=n-2 is nonnegative for every even n>=2. Thus
1/(k-j)!=j! binom(k,j)/k!, with binom(k,j)=0 for j>k,
continues to justify the factorial bounds for the exponential
blocks. There is no negative factorial in the argument.

For additional clarity, the bound on the exponential-border terms
can be obtained by expanding that border directly: omission of
column ell leaves numerator factorial valuation
S(n+1)-phi(ell)>=S(n), and the factor -4 contributes 2. This
avoids any row-range assumption from a specialized Lambda
alternant. The largest sum of n row-factorial valuations is still
H_n. Together with the pure C bound this gives the stated gap
2+n+2phi(n)-c_n^val.

The C-border bound is V_n-n, so v_2(h_2)>=-n. At n=2 the added
row is k=0; its exponential entries are (1,0,0) and its only
negative odd C entry is t_(-1)=1. All the preceding bounds and
the R=1 one-gap argument still apply.

Now p_1=2(a_n c_(n-2)-h_2 c_n). Both products in parentheses
have valuation at least

    -2n-2phi(n-1)-2 epsilon = v_2(p_0),

by the previously reviewed leading A, leading C, and Xi results.
The explicit factor 2 proves

    v_2(p_1) >= v_2(p_0)+1

for every even n>=2, including the possibility p_1=0.

## 4. The coherent top contribution and what it does not prove

Reversal gives exactly

    z^(-2n) P(z)=U^2+(1+t^2)(VU'-V'U), t=1/z.

At the common top exponential row set, the same cofactor scale
applies to U=kappa(Q_n-lambda Q_(n-1)) and V=-S_U.
For T_U=U^2+(1+t^2)(US_U'-U'S_U), I independently used the
inhomogeneous second-kind Legendre equations to obtain

    T_U' = 2n lambda kappa^2
           (Q_n S_(n-1)-Q_(n-1) S_n)
         = -2n lambda kappa^2 h_(n-1).

The cross term is odd. The diagonal Wronskian constants are
(2m+1)h_m. Hence the exact affine formula (13), including its
minus sign and its common kappa^2 factor, is correct in both
parities. Its quadratic coefficient vanishes identically.

For the full actual triple, the low Taylor reconstruction gives
V=-S_U-E_B exactly. The sign in the correction
(1+t^2)(E_B'U-E_BU') is consequently correct. The recently proved
B-coefficient theorem gives

    v_2([t^s]E_B) >= phi(n)-phi(n-s) >= 0

for 0<=s<=n, by the integer binomial inequality
phi(j)+phi(n-s-j)<=phi(n-s).

The actual p_2 still contains cross terms between the top
cofactor vector and other row sets, terms involving two other
row sets, and the displayed E_B correction. Exact vanishing of
the top quadratic coefficient does not bound these terms at
v_2(p_0)+1. The note explicitly leaves that step open. No
all-even triple-root exclusion or squarefreeness claim follows
from this first gate alone.

No new canonical degrees, prime ranges, or numerical root scans
were used in this review.
