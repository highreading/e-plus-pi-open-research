> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent verification of the approximant-module shared-core theorem

Date: 2026-09-13. Reviewer: audit_results, checking root's proposed
all-index argument before its final source note is saved.

The argument is valid. For every n>=1 and p>3n, the shared
extended matrix C_n^+ in raw_adjacent_high_content_condensation.md
has full row rank 2n-1 modulo p. Consequently its integer maximal-
minor content zeta_n has no prime factor above 3n.

## 1. Exact module and a row-reduced basis

Put K=F_p and M=3n+1. The approximant module is

    A+B E_T+C F_T =0 modulo z^M,

where E_T,F_T are the Taylor polynomials through degree M-1=3n.
All their denominators are units under the exact prime hypothesis.
It is the free K[z]-module with basis rows

    (z^M,0,0), (-E_T,1,0), (-F_T,0,1).

Its determinant is z^M. To reduce leading rows, take a dependence
among their leading coefficient vectors and choose a row of largest
degree participating with nonzero coefficient. Replace that row
by the corresponding linear combination, multiplying the other
rows by the required nonnegative powers of z to align degrees.
The chosen row has a nonzero constant coefficient in the row
operation, so the operation is unimodular over K[z]. Its new
degree is strictly smaller. The new row cannot be zero, because
the basis remains linearly independent over K(z).

The sum of nonnegative row degrees decreases at every such step;
therefore the process stops with independent leading vectors.
If its sorted row degrees are d_1,d_2,d_3, the determinant degree
is then their sum, giving d_1+d_2+d_3=M. This reasoning does
not require any characteristic-zero analytic series.

For a polynomial combination of this basis, the highest degree
cannot cancel: its coefficient is a nontrivial combination of
a subset of the independent leading vectors. Consequently

    dim_K{module rows of degree <=r}
       =sum_i max(0,r-d_i+1).

This is the required predictable-degree formula, with every
component A,B,C included in the row degree.

## 2. Applying the established minimal-degree bound

The degree<=n-1 slice of this full module is exactly V_n^- in
raw_large_prime_nullity_and_smith.md. The previously proved
dimension bound <=1 therefore applies without an endpoint
restriction. It implies d_1>=n-1: a smaller d_1 would alone
contribute at least two dimensions at degree n-1. It also implies
d_2>=n, because otherwise two basis rows contribute dimensions.

The determinant degree then gives d_3<=n+2. All three terms at
r=n+1 are nonnegative without truncation, and hence

    dim_K{module rows of degree <=n+1}
       =sum_i(n+2-d_i)=3(n+2)-(3n+1)=5.

The sorted possibilities are precisely

    (n,n,n+1), (n-1,n+1,n+1), (n-1,n,n+2).

In particular the module proof does not yet eliminate the last
profile, which is the one permitting a deficient H_n. It does
prove the larger shared-core dimension unconditionally.

## 3. The dimension bridge keeps the degree of A

Given B,C of degree <=n+1, there is exactly one polynomial A
of degree <=n+1 canceling the first n+2 Taylor coefficients.
The remaining constraints are precisely the rows k=n+2,...,3n
of C_n^+. Thus reconstruction of A is a linear bijection
between its kernel and the module slice of degree <=n+1.

The coefficient space of B,C has dimension 2n+4. The kernel
dimension five therefore gives row rank 2n-1. No Taylor row
beyond degree 3n is invoked; the fact that p can equal 3n+1
introduces no division by p. This is also why the conclusion
holds under p>3n, not merely the stronger adjacent-degree
hypothesis p>3n+3 used elsewhere.

Every such prime sees a unit maximal minor of C_n^+. Therefore
v_p(zeta_n)=0 at all p>3n, including every prime-power exponent.
In a unit (2n-2)-minor chart where the old common core has rank
only 2n-2, its old residual rho entries all vanish modulo p.
Full rank of the extended core forces a unit in at least one
of its two new-column rho entries, exactly as root proposed.

This closes the zeta_n target, while leaving the original H_n
rank and the other adjacent-content correction minors open.

## 4. Final saved source confirmation

I subsequently read the complete saved source
raw_shared_core_large_prime_saturation.md, including Sections4–5,
and rechecked the exact V_n^- dependency against
raw_large_prime_nullity_and_smith.md. The final source passes;
no mathematical correction is needed.

In particular the degree<=D formula is valid for every D>=n+1:
all three terms D−d_i+1 are nonnegative by d_3<=n+2. For
n+1<=D<=3n, reconstructing A through degree D leaves precisely
the rows D+1,...,3n, whose denominators remain units. Thus the
fixed-jet eventual-degree full-rank corollary is correctly scoped.
It is not an adjacent-index rank theorem with a moving jet order.

The residual shared-row unit statement is also exact: after a
unit (2n−2) old-core pivot, a deficient old shared core forces
all four old residual entries to vanish modulo p, whereas full
rank of the extended core forces one of its two new entries to
be a unit. This provides a full shared-row pivot for the next
matrix, but not necessarily an old-matrix pivot or a unit
two-column new block. The final source retains these limits
and the correct direction of zeta_n | gcd(D_n,D_(n+1)).
