> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Zero dyadic average for the entire first-Witt radical support

Status: new auxiliary theorem assembled from exact identities in this
continuation and accepted after dedicated independent review in
`witt_independent_review.md`. It is an
upper estimate on a divisibility support, not an irrationality proof,
and it does not sum unbounded valuation multiplicities.

## The actual support

Retain the normalization and first-Witt interpretation of Items424–427.
For an ordinary rank-zero row p in P_m with p^2>4m+1, put

    kappa_(m,p)=A_m/p mod p,
    W_kappa(m)=sum_(p in P_m, p^2>4m+1, kappa_(m,p)=0) log p.

Then there are positive absolute constants c,C such that, for all
sufficiently large X,

    sum_(X<m<=2X) W_kappa(m)
       <= C X^2 exp(-c(log log X)^(1/9)).             (1)

In particular the sum is o(X^2), and W_kappa(m)=o(m) in density.
This covers both the j=0 unbooked cell and the j>=1 booked-overlap cells.
Each contribution is the radical of a post-baseline event; it is not a
new positive divisor lower bound.

## 1. Actual states, rather than continued complex periods

Write

    4m+1=(2j+1)p-2s,   p=2r+6s+3,
    s>=1, j>=0, r>=0.

At fixed p,j, consecutive actual rows have s increasing by2 and r
decreasing by6; their number N is p/12+O(1), less than p.
For the fixed-p differential P_0=u^rQ^(2s), take its degree-below-p,
zero-constant primitive T_0. Item426's four-section map gives H_0 and
the three rational/logarithmic/circular coordinates E_j(H_0).

The exact operators, contiguity and exterior observation are established
in `witt_exterior_recurrence_attempt.md`. Their characteristic-p
correction is essential: the raw periods have an x^p ambiguity. The
endpoint map kills that ambiguity because its corresponding polynomial
H_F=xD_j+uQ gives the exact differential d(xF_j), with zero endpoint
values. The projected coordinates therefore obey the homogeneous
order-three recurrence and contiguity used below.

Let f=L_j(H_0), g=R_j(H_0). Form their three-state exterior product
w=(w_01,w_02,w_12) in the three consecutive r-rows. There is an exact
rational matrix T_w(r), independent of j,p, with

    w(r-6)=T_w(r)w(r),
    r*kappa(r)=v(r)w(r).                              (2)

These identities are used only where their rational denominators are
units. Denominator zeros will be counted explicitly, not inverted.
The limits T_w(r)->W and v(r)->v exist. They are the rational matrix
and row displayed in the preceding note, with

    det(v,vW,vW^2)=243/705100000 !=0.                  (3)

Every eigenvalue of W is nonzero, and no quotient of distinct
eigenvalues is a root of unity. These are consequences of the already
verified cubic nondegeneracy under a rational scale and exterior square.

Most importantly, `witt_actual_exterior_rank.md` proves the actual
nonzero-state assertion independently of any phase continuation:
whenever r>=12, 3j+1<p, and2j+2<p, w(r) can be zero only at a root
of one fixed primitive sextic S_6(r). Thus there are at most six such
starts. The exact26-by26 determinant proving this assertion is part
of that note's symbolic certificate. No assumption about random initial
values or independent primes is used.

## 2. Nonzero observation determinants at every fixed spacing

Choose integer polynomials q(r), d(r) that clear T_w and v, respectively,
with their exact degrees D,E and nonzero leading coefficients. Since
the rational functions have finite limits, write

    M(r)=q(r)T_w(r),       V(r)=d(r)v(r),
    lc_D(M)=L=lc(q)W,     lc_E(V)=a v,

where a=lc(d). For a positive integer h, the observation of w(r)
at r,r-6h,r-12h is represented after denominator clearing by the
three polynomial rows

    V(r),
    V(r-6h) M(r-6(h-1))...M(r),
    V(r-12h) M(r-6(2h-1))...M(r).

Their determinant J_h(r) is an integer polynomial of degree at most
3E+3Dh. Its coefficient at that degree is

    a^3 det(v,vL^h,vL^(2h)) !=0.                     (4)

Indeed (3) makes v cyclic, and distinct eigenvalues stay distinct
after every h-th power by the non-root-of-unity condition. Diagonalizing
over the splitting field gives a nonzero Vandermonde determinant.
Thus (4) is an exact symbolic nonidentity, not a claim that a real
limiting matrix approximates a finite-field matrix.

With one fixed B>=2, the absolute value of the integer in(4) is at
most B^(C_0 h+C_1), for fixed constants. Taking

    K_p=floor(c_0 log p)

with a sufficiently small positive c_0 makes this coefficient nonzero
and smaller in absolute value than p for every h<=K_p, once p is
large. J_h therefore remains a nonzero polynomial modulo p uniformly
over those spacings. Its degree, and the degrees of the required
transfer and observation denominators, are O(h+1).

For a fixed h<=K_p, an all-zero three-term progression of kappa values
can start only at a root of J_h, a root of a cleared denominator, a
zero exterior state, or a terminal incomplete-state row. There are
O(h+1) such starts. Constants are independent of j as long as the two
explicit endpoint-map inequalities in Section1 hold. Actual r-values
are distinct modulo p, because the step is6 and the interval length
is less than p.

Remove the starting point of every all-zero progression with spacing
at most K_p. At most O(K_p^2) points are removed. Each remaining block
of length K_p is three-term-progression-free. Thus, uniformly in j,

    Z_j(p)<=N r_3(K_p)/K_p+O(K_p^2+K_p),              (5)

where Z_j counts actual first-Witt zeros in the full fixed-p,j interval.
The quantitative progression theorem cited in
`fixed_prime_roth_density.md` gives

    Z_j(p)<=C p exp(-c(log log p)^(1/9)).              (6)

The qualitative conclusion needs only Roth's original theorem. The
quantitative input is Bloom–Sisask, [The Kelley–Meka bounds for sets free
of three-term arithmetic progressions](https://arxiv.org/pdf/2309.02353),
Theorem1. The exact version was checked in the earlier independent
Roth review. No Diophantine approximation version of Roth is invoked.

## 3. Uniform summation across all j

The uniformity in(6) permits a direct sum, without interchanging
infinitely many fixed-j limits. On X<m<=2X, discard primes

    p<=sqrt(12X)+2.

Their entire radical weight for any one m is O(sqrt X), by Chebyshev,
so the total discarded contribution is O(X^(3/2)). This includes
possible primes outside the endpoint-map range; no statement about
their multiplicity is needed.

For every remaining actual row, the inequality2s<=(p-3)/3 gives

    j=(4m+1+2s-p)/(2p)<=4X/p-1/3.

Consequently3j+1<=12X/p<p and2j+2<p, for all sufficiently large X.
Both endpoint-map hypotheses hold uniformly. Also p<6m<=12X and,
for a fixed p, the number of possible j is O(X/p+1).

Write delta(t)=exp(-c(log log t)^(1/9)) for large t, reducing c if
necessary. It is decreasing. Exchanging the nonnegative sums and using
(6) gives

    sum_(X<m<=2X) W_kappa(m)
      <=O(X^(3/2))
        + C sum_(sqrt(12X)<p<=12X) (X/p+1)p delta(p)log p
      <=O(X^(3/2))+O(X^2 delta(sqrt(12X))).           (7)

Only Chebyshev's bounds sum_(p<=Y)log p=O(Y) and
sum_(p<=Y)p log p=O(Y^2) are used. Since log log sqrt(12X)
=log log X+O(1), adjusting constants yields(1).

Markov's inequality proves W_kappa(m)=o(m) in density. One may also
select a density-one subsequence with this limit. This does not control
every m or exclude a sparse favorable subsequence for the main mixed
construction.

## 4. Exact limits of the result

By Item427's valuation identity, every fixed higher tower layer is a
subset of the first-Witt support. Thus every fixed finite union of
higher radical layers also has zero dyadic average. This does not
justify summing all valuation layers. A separate depth-moment or
uniform-integrability estimate remains necessary.

The theorem supplies no positive lower bound for the synchronized
content/matching gain Gamma. The main threshold and booked lower rate
remain unchanged. It is a rigorous upper restriction on where further
arithmetic gains may lie, and improves the strategic understanding of
the archive's uncompleted Witt route.
