> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of all fixed-size low-node minors

Date: 2026-09-13. Reviewer: audit_sources.

Reviewed `raw_fixed_size_low_node_minor_theorem.md` against the
fixed-node and positive endpoint-moment theorem already reviewed
in `raw_fixed_node_branch_independent_review.md`.

**Verdict: all claims pass.** No correction is requested. The
number of nodes, nodes themselves, and distinct positive row
proportions are fixed throughout. No numerical sample was used.

## 1. Endpoint recurrence and normalization

The quotient psi_l(1-y)/psi_l(1) is valid because the endpoint
has already been proved nonzero. Under x=1-y, the differential
equation becomes exactly

    y(1-y) f''+(1-2y) f'+(xi-1+y-y^2) f=0.

Its y^(r-1) coefficient has r^2 a_r from the two derivative
terms, and [xi-1-r(r-1)] a_(r-1)+a_(r-2)-a_(r-3)
from the others. This verifies equation (6), including r=1,2
with the zero negative-index convention. Its leading term
recursively multiplies by -xi/r^2, giving exactly
(-1)^r/(r!)^2 at degree r.

Taylor's remainder is uniform on [0,1] for the finite chosen
node set. The constant is allowed to depend on their finitely
many derivatives. Positivity of E_k then bounds the integrated
signed remainder by the positive endpoint moment mu_(R+1).
The actual L_k, endpoint value, and amplitude normalizations
in equation (1) are preserved, including mixed node parities.

## 2. Rounding and determinant precision

For fixed t_i>0, floor(t_i n)=t_i n+O(1). In each fixed moment,
this causes relative error O(1/n), which is smaller than the
O(n^(-1/2)) error already present. Thus every column indexed
by r in the finite moment matrix is

    epsilon^r [r! (t_i^(-1/2))^r+O(epsilon)],
    epsilon=n^(-1/2).

The choice R=q=m(m-1)/2 ensures that the entry remainder is
O(epsilon^(q+1)). All matrix entries stay bounded and the
dimension is fixed, so determinant multilinearity, or its
bounded derivatives on a bounded set, gives the same absolute
error for the determinant. This step is essential: a fixed
first-order entry expansion would not justify the result for
arbitrary fixed m.

In finite Cauchy–Binet, the unique ordered set of m distinct
nonnegative degrees with sum q is {0,...,m-1}. Every other
set contributes O(epsilon^(q+1)) or smaller. The number of
sets is fixed, so no summation growth is omitted.

For the distinguished set, factoring r! from moment column r
gives Delta(x_1,...,x_m) with x_i=t_i^(-1/2). The coefficient
matrix has polynomial-degree rows and node columns; its
monomial evaluation determinant is the transpose of the usual
Vandermonde and still has sign Delta(zeta_1,...,zeta_m).
The diagonal polynomial changes contribute
(-1)^q/prod(r!)^2. Their product is therefore precisely

    [(-1)^q/prod(r!)] Delta(zeta) Delta(x) epsilon^q.

When the t_i and nodes are both increasing, Delta(x) has sign
(-1)^q, so the leading determinant is positive. The m=1 case
has q=0 and is covered by the same proof.

## 3. Every singular-value order

Truncating before degree r gives a matrix of rank at most r,
with operator-norm error O(epsilon^r). This proves
s_(r+1)<=C_r epsilon^r by the standard rank-approximation
inequality. For r=0 the zero approximant and bounded entries
give the same statement.

The nonzero leading determinant makes the full matrix
invertible for all sufficiently large n. Dividing its lower
determinant bound by the upper bounds for every singular
value other than s_j gives

    s_j >= c_j epsilon^(q-sum_(i!=j)(i-1))
        = c_j epsilon^(j-1).

This argument correctly gives all orders, not just the least
singular value. It uses no positivity of the mixed moment
matrix and does not discard any row or column normalization.

## 4. Scope

Restoring fixed nonzero endpoint or amplitude column factors
preserves these singular-value orders with fixed comparison
constants. Removing the row factors L_(floor(t_i n)) is
different: their stretched-exponential sizes vary with the
row proportions. The note correctly states its theorem only
in the displayed normalization.

No bound uniform in a growing number of nodes, moving nodes,
or coalescing row proportions is supplied. In particular the
Taylor truncation order, eigenfunction derivative constants,
and Vandermonde constants cannot be treated as uniform in
those regimes. The fixed-size theorem does not settle the
inverse estimate for the full actual high-row matrix.
