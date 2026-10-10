> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the positive row-eigenvalue count

Date: 2026-09-13. Reviewer: audit_computations.

Reviewed `raw_positive_row_eigenvalue_count.md` in full. The
quadratic-form comparison, dyadic counting argument, constants,
and stated scope pass. No correction is requested.

## 1. Coefficient and boundary estimates

The identity

    a_j^2-j^2/4 = j^2/[4(4j^2-1)] <= 1/12

holds for every `j>=1`. The stated upper bound
`a_j<=j/2+1/(8j)` is also valid; for example it follows from
`(1-u)^(-1/2)<=1+u` on `0<=u<=1/4` after substitution.
The diagonal estimate is

    b_k <= -k^2/2-k/2+5/12.

Arithmetic--geometric mean on the two distance-two coefficients
gives

    c_k+c_(k-2) <= k^2/2+k/2+11/12.

At `k=0,1`, using a nonnegative bound for the missing negative-index
coefficient only enlarges the upper bound. Thus the uniform
`b_k+c_k+c_(k-2)<=4/3` estimate is sound at the left boundary too.

Extending the vector by zero beyond the finite right endpoint
includes the outgoing distance-two square terms. Their added
diagonal pieces are precisely accounted for when the squares are
completed, so no returning path is lost. Bounding the nearest
neighbor cross terms gives at most `a_k+a_(k+1)` on coordinate
`k`; this is at most `k+3/4`, including `k=0`. The resulting
potential `k+3` is a valid upper bound. In particular the form
comparison is in the correct direction for bounding positive
eigenvalues from above.

## 2. Dyadic path comparison

Deleting the negative distance-two square terms across the dyadic
cuts increases the comparison form. In a block starting at `a=2^j`,
the potential is at most `2a+2<=4a` and every retained edge has
weight at least `a^2/4`. Each reflection parity gives one free-end
path; their two lengths sum to at most `a`.

The free-end path eigenvalues are

    4 sin^2(pi r/(2m)),  0<=r<m,

including the one-vertex case. Concavity of sine on `[0,pi/2]`
gives `sin(pi r/(2m))>=r/m`. A positive comparison eigenvalue
therefore requires `r<2m/sqrt(a)`. Counting these integers by
`1+2m/sqrt(a)` is conservative and valid also when this upper
bound exceeds the path dimension. Summing both paths yields
`2+2sqrt(a)` per nonempty dyadic block. The isolated index zero
contributes at most one eigenvalue.

Finite-dimensional min--max preserves the form ordering, proving
the stated explicit bound

    n_+(K_N) <= 1+2(J+1)+2 sum_(j=0)^J 2^(j/2).

The geometric sum is `O(sqrt N)` and the additive term is
`O(log N)`, so the asserted all-index square-root bound follows.

## 3. Scope relative to the factor split

The conclusion counts the actual positive row eigenvalues. It does
not give a distance between any remaining eigenvalue and a column
node, nor a projected minor bound. On the nonpositive spectral
subspace all positive-node factors are positive definite, exactly
as stated. Off-diagonal coordinate compressions do not inherit
that positive definiteness. The root note correctly leaves this
projection obstruction open.

This review uses only the exact inequalities and finite-dimensional
spectral theory. It includes no new eigenvalue sample or numerical
degree solve.
