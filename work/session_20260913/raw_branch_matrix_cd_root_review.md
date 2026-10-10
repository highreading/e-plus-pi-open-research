> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the two-channel CD identity and uniform bounds

Date: 2026-09-13. Root verification of
`raw_branch_matrix_christoffel_darboux.md`.

**Verdict: the identities and their growing-index estimates pass.**

The three edges crossing a cut N are exactly (N-2,N), (N-1,N),
and (N-1,N+1), with coefficients encoded by Gamma_N. Summation
of the two symmetric recurrence equations therefore gives (y-x)
times the row Gram sum and the stated right boundary form minus
the left boundary form. The absent negative rows make the left
endpoint form zero without imposing an additional seed equation.
Differentiation in y at y=x gives the displayed diagonal CD form.

The interior equation is (xI-K_N)U_N=iota_N Gamma_N P_N.
Together with the independently reviewed Casoratian determinant,
this justifies both inverses and the positive resolvent formula.
The symmetry needed to multiply the Green identity follows already
from its diagonal zero boundary form. The divided difference is
therefore (M(x)-M(y))/(y-x), and its diagonal is -M'(x), with the
correct sign. Its residues and block Gram kernel are positive
semidefinite. The injection into the last two coordinates is
injective on each eigenspace by backward recurrence using nonzero
distance-two coefficients, so no spectral point is silently lost.

The lower bound on K_N retains the positive compression of J^2;
it does not substitute J_N^2. The upper bound is the previously
reviewed row bound. The crude estimates for Gamma_N follow by
separating its diagonal and single off-diagonal entry. Both
numerical inequalities used to simplify those estimates hold for
N>=8. Under N>=4/c0, xI-K_N has eigenvalues between c0 N^2/2
and (c1+1)N^2. Applying the inverse and squared inverse to the
two-column injection then yields exactly the constants in (17)
and (18). Congruence by P_N proves the coherent energy comparison,
including nonzero combinations of both channels.

For the adjacent determinant lower bound, every finite eigenvalue
lies at most N+3/4, and the product of the rational recurrence
pivots is at most ((N+1)!)^2. There are N nontrivial factors in
(N+1)!, so the stated elementary factorial upper bound is valid.
The resulting exponential determinant lower bound combined with
the already reviewed uniform generating-function upper bound
gives the smallest-singular-value estimate by the exact 2-by-2
identity sigma_min=|det|/sigma_max. The fixed normalization factors
between r and p do not change the exponential scale or the
stated weighted Gram comparison.

All these statements involve a coherent pair of channels at one
parameter, or its matrix divided-difference kernel. The note
correctly leaves the actual large scalar mixed evaluation matrix
uncontrolled. No numerical pattern or unproved limit was used in
this review.
