> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the actual scalar boundary-rank obstruction

Date: 2026-09-13. Reviewer: audit_computations.
Reviewed: `raw_polynomial_difference_boundary_rank.md`, Sections 1--6.

**PASS.** All stated rank formulas and scope restrictions check; no
correction identified.

The key support bridge is valid for the actual finite matrix. If
`deg(L_b u)<n`, every polynomial path from the original component seed
has maximal row index below `2n`, including the shifted odd seed.
Consequently the established triangular two-component representation
is injective on these polynomials. The positive high factor preserves
nonzero norms. This proves that the actual scalar measure has at least
`d+h=n-ell_b` distinct support points, without requiring simple row
spectrum or assuming that the low factor is nonzero at every row node.

For the polynomial q of degree h-1, both `qu-v` and the exceptional
zero-input cases lie below that scalar injectivity threshold. Hence
boundary cancellation is a polynomial identity, and the kernel is
exactly the displayed low-degree subspace. This proves
`rank=max(h-1-r,0)`, including h=1 and maximal truncation r=d.

For the rational ratio, clearing its denominator gives a polynomial
of degree at most d+h-1. The same support argument applies. Strict
interlacing makes F_a,F_b coprime, so the kernel consists precisely of
multiples of F_b. Its dimension is `max(d-r-h,0)`, giving
`rank=min(d-r,h)`. The full-rank h conclusion for the rank-one
resolvent sum follows: each factor in an h-term factorization must
have rank h if their product does. In particular the Jacobi boundary
coefficient cannot vanish at this actual cutoff.

The final first-channel compression Z^T(... )C is correctly retained.
The uncompressed rank formula does not establish its rank or a sign
for the mixed Schur operator. The general codimension restriction
bound is used only for the uncompressed operator, where it applies.

The reflection identity also has the stated sign. From C u=u and
C q(K)v=-q(K)v one gets
`u^T(C^T-C)q(K)v=2u^Tq(K)v`. The support condition is sufficient for
the exact polynomial commutation and holds for retained-degree inputs
at the chosen square-root cutoff. The argument correctly distinguishes
commutation from selfadjointness in the actual coefficient metric.

No numerical calculation or generic positive-matrix substitute was
used in this review. The result is an exact obstruction to deriving
small boundary rank solely from the one-degree drop in F_b-F_a.
