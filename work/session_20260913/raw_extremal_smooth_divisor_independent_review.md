> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the smooth divisor and prime-power saturation theorem

Date: 2026-09-13. Reviewer: audit_computations.
Reviewed: `raw_extremal_smooth_divisor_and_prime_power_saturation.md`,
with definitions checked against `raw_high_smith_finite_difference_reduction.md`,
`raw_extremal_large_prime_height_improvement.md`, and
`raw_extremal_dual_polynomial_and_content_identity.md`.

**Outcome: PASS.** All global content identities, integer-divisor claims,
the entire normalized matrix modulo p, the closed valuation, and the
specified original minor are correct. No degree or prime scan was used.
The proof below independently establishes each new all-index step.

One optional terminology clarification was sent to the author: the
content calculation uses fractional Z-ideals inside Q, rather than
ideals of the field Q. This does not change any formula.

## 1. Actual matrix and characteristic-zero nondegeneracy

The convention is tau_m=[z^m]arctan(z), not 4arctan(z): tau_m=0 for
positive even m, and tau_m=(-1)^((m-1)/2)/m for positive odd m.
Every entry k!tau_(k-j) of X_n is integral because 1<=k-j<=k.
The actual rows are ALL k=n,...,3n, with both column degrees strictly
below n. In particular the lowest k=n equation has not been dropped.

The required nonzero characteristic-zero content is an already reviewed
input, whose proof was checked at `raw_high_content_extremal_valuation_bound.md`,
Section 1. A nonzero kernel vector of X_n would reconstruct a triple
of degree at most n-1 and order at least 3n+1. Multiplication by z-1
would give a nonzero degree-at-most-n triple with that same origin
order and both B,C endpoint values zero. The established nonzero
actual endpoint determinant excludes it. Thus rank_Q X_n=2n.
No assertion that this endpoint determinant is a unit at arbitrary
small or large primes is used in the present argument.

## 2. The content factor V_n is global, including small primes

Define the row operation directly in increasing original row order.
Keep rows k=n,...,2n-1. The new row with index r=0,...,n is

    sum_(s=0)^n (-1)^(n-s) binom(n,s) row_(n+r+s).

Its latest original row is k=2n+r, with coefficient 1. The complete
row transformation is therefore integral lower triangular with all
diagonal entries 1, hence unimodular over Z. The n-th difference
annihilates every falling factorial (k)_j, j<n. The top-left block V
has determinant product_(j=0)^(n-1)j!: falling factorials are monic,
and the consecutive-row Vandermonde is the product of these factorials.

After the operation the block matrix is

    [ V  C0 ]
    [ 0   G ].

A maximal square minor uses 2n of its 2n+1 rows. If it omits a top
row, the first n columns have rank at most n-1, so that determinant
is zero. Otherwise it contains all top rows and exactly n bottom
rows, and its determinant is det(V) times the corresponding n-minor
of G. Thus the determinantal ideal of the transformed matrix is
exactly V_n times the n-th determinantal ideal of G.

For completeness, unimodular left multiplication preserves that ideal
globally: Cauchy--Binet writes every new maximal minor as an integer
linear combination of the old ones; applying the inverse unimodular
matrix proves the reverse inclusion. Consequently

    F_n=V_n gcd_(|I|=n) |det G[I,:]|                       (R1)

is an equality of positive integers before ANY localization. Inverting
det(V), or assuming it is a p-unit, is unnecessary here.

## 3. Row scaling, weighted gcd, and the actual integer divisor

Put L=lcm(1,...,3n). In the row-scaled matrix Z each summand is

    (-1)^(n-s)binom(n,s) [(n+r+s)!/(n+r)!]
                       L tau_(n+r+s-j).

The factorial ratio is an integer, and the arctangent index is between
1 and 3n. Thus Z is integral term by term, including at small primes.
For a minor omitting row t, undoing its n row scalings gives

    det G[hat(t),:]
      =L^(-n) product_(r!=t)(n+r)! delta_t
      =[P_n/L^n] c_t delta_t,                             (R2)

because product_(r!=t)(n+r)!=P_n(2n)!/(n+t)!.
All row orders are increasing; no omitted-row cofactor sign is needed
when taking absolute gcds. Every c_t is an integer, and c_n=1.

Taking the positive generator of the resulting fractional Z-ideal,
(R1),(R2) prove

    F_n=V_n [P_n/L^n] h_n,
    h_n=gcd_t |c_t delta_t|.                              (R3)

Possible zero minors cause no difficulty; at least one is nonzero
by the characteristic-zero rank argument.

To check the integer-divisor conclusion without concealing a rational
factor, write g=gcd(P_n,L^n), P_n=gP', L^n=gL', with gcd(P',L')=1.
Every integer minor in (R2) implies L' divides c_t delta_t. Hence
L' divides h_n and

    F_n=(V_n P') [h_n/L'].

Both displayed factors are integers, proving that the stated
S_n=V_nP_n/g divides F_n. There is no assumption L^n|P_n.
Its prime support is indeed at most 3n (in fact the numerator's
support is already at most 2n-1).

The logarithmic order is correct. V_nP_n=product_(k=0)^(2n-1) k!,
and elementary summation or integral comparison gives

    log(V_nP_n)=2n^2 log n+O(n^2).

The removed gcd has logarithm at most n log L=O(n^2). The lcm estimate
can be proved without a prime number theorem: L_N divides
L_ceil(N/2) times binom(N,floor(N/2)), as a prime's one possibly missing
highest power is supplied by that binomial. Iteration gives log L_N=O(N).
Thus log S_n has the stated leading term. At q>3n, all c_t and every
factor in V_nP_n/L^n are q-units, yielding the exact large-prime
valuation equality in the source note. Discarding these weights at
small primes would be incorrect.

## 4. The full matrix modulo p on n=p^a

Assume n=p^a, p>3, a>=1. Since p^a<=3n<p^(a+1), v_p(L)=a.
I checked each class of summands separately; there is no cancellation
argument hidden in the reduction.

For 1<=s<n, binom(n,s) has valuation a-v_p(s)>=1. One elementary proof
that binom(n-1,s-1) is a p-unit is the polynomial identity

    (1+X)^(p^a-1) = (1+X^(p^a))/(1+X) mod p:

its coefficients through degree n-1 are (-1)^j. Combine this with
binom(n,s)=(n/s)binom(n-1,s-1). All other factors of the summand in Z
are integers, so these terms vanish modulo p.

For s=n, the factorial ratio consists of n consecutive positive
integers and hence contains a multiple of p. L tau is again integral.
That term vanishes modulo p even when its arctangent coefficient is
zero. No denominator can cancel the factorial's p-factor after the
L normalization.

The sole remaining term is (-1)^n L tau_m with m=n+r-j and
1<=m<=2n. If m is odd, its valuation is a-v_p(m); if m is even it is
zero. Thus it survives only when m is a multiple of n. The only such
indices in this range are n and 2n, and 2n is even. Therefore survival
is exactly r=j. As j<n, the entire final row r=n vanishes. The
surviving value is

    (-1)^n L tau_n
      =(-1)^((n+1)/2) L/n =:u,

which is a p-unit. Hence, with the original increasing row and column
orders retained,

    Z mod p = u [ I_n ; 0 ].                              (R4)

This is an all-entry statement. It proves delta_n is a p-unit, all
other delta_t are zero modulo p, and h_n is a p-unit because c_n=1.
Higher valuations of the other minors are irrelevant. The exclusions
p=2,3 are material: the parity and/or v_p(L)=a arguments would change.

## 5. Closed valuation and smooth-divisor saturation

Equation (R3) and the p-unit h_n give

    v_p(F_n)=sum_(k=0)^(2n-1)v_p(k!)-na.                    (R5)

For each 1<=e<=a, the range 0,...,2n-1 partitions into blocks of
length p^e, since p^e divides 2n. Consequently

    sum_(k=0)^(2n-1) floor(k/p^e)=2n^2/p^e-n.

There are no terms e>a because 2n<p^(a+1). Summing and using
p^a=n yields

    v_p(F_n)=2n(n-1)/(p-1)-2an
            =2n[1+p+...+p^(a-1)-a].                       (R6)

The last form confirms nonnegativity and gives zero exactly at a=1.
This is an exact sum of valuations, not a leading-order approximation.

Each factorial (n+r)!, 0<=r<n, contains the integer n and therefore
has valuation at least a. Thus v_p(P_n)>=na=v_p(L^n), and the gcd
removed in S_n has valuation exactly na. Formula (R5) is therefore
also v_p(S_n), proving v_p(F_n/S_n)=0. Saturation concerns the
specified smooth divisor at this prime; it is not a statement that
all remaining content is trivial.

## 6. The specified first 2n rows really give the saturated minor

Select the original rows n,...,3n-1. Restricting the same row operation
to these rows remains unit lower triangular: the retained differences
are exactly r=0,...,n-1, and their latest original rows are 2n+r,
ending at 3n-1. It does not refer to the omitted original row 3n.
The selected determinant is therefore

    det(V) det G[rows 0,...,n-1].

In (R2) this is precisely t=n, with c_n=1 and the p-unit delta_n.
Its p-valuation is the value (R6), equal to that of the full content.
It is nonzero over Q because its normalized determinant is a p-unit.
Thus no unspecified minor choice, favorable pivot, or finite search
is being used on these prime-power degrees.

## 7. Scope of the resulting obstruction

The normalized maximal-minor content is a p-unit on every n=p^a,
p>3. This excludes a proposed universal divisor that demands a
positive p-part of n! in that content. It does not exclude a large
smooth divisor assembled differently from other primes, nor does it
show that the remaining n^2 log n large-prime upper bound is sharp.
For a fixed p, an O(n^2) logarithmic correction can absorb this deficit.

The source note correctly keeps F_n separate from the primitive-dual
scalar in the endpoint identity and from the primitive endpoint
ratio. None of the reviewed identities bounds that separate scalar
or proves irrationality of e+pi. No mathematical repair is required.
