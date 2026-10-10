> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root independent review of the actual sparse bulk theorem

Date: 2026-09-13. Reviewed `raw_actual_sparse_bulk_matrix_theorem.md`.
Verdict: the actual growing-matrix theorem passes.

The uniform quantitative high-kernel estimate and the Cauchy
inverse bound have each already passed separate independent
reviews. The present deduction keeps their constants uniform
over the selected actual nodes, which is the essential extra
point for a growing matrix.

The integer index construction has the claimed gap for large n:
the endpoint rounding loses at most two indices overall, and
the difference of floors loses at most one. Since m=O(log n),
these errors are absorbed in the stated factor four. The exact
spectral enclosure gives xi_j-xi_i >=2 alpha n(l_j-l_i), and
the derivative magnitude of q on the fixed parameter interval
is at least q_-/sqrt(c_+(c_++1)). Thus the gap constant tau_s
is correct. No selected parity is being held fixed implicitly.

The first component of either limiting column is uniformly
nonzero on the fixed interval. The positive Cauchy congruence
therefore yields the least-eigenvalue bound. The inverse-trace
sum uses the binomial-square identity, so no missing factor m
is introduced. Applying r!>=(r/e)^r and r/m>=1/2 gives the
displayed weaker base tau_s/(4e). Because that base is below
one and m<=kappa log n, the resulting n^(-theta) lower bound
has the correct direction.

The exact d_i in the actual Gram congruence retain g_l, the
upper even-cut scalar product, and the unequal powers of xi.
The factor-four conversion between xi/n^2 and xi/(2n)^2 is
explicit and correct. A uniform entry error C log n/n gives
operator error at most m times that amount. Dividing by the
proved least eigenvalue supplies eta_n=O(log^2 n n^(-1+theta)),
which tends to zero since theta<1. Congruence by the limiting
positive Gram matrix proves the two relative Loewner inequalities,
the actual singular-value bound, and the condition estimates.

Finally the log-determinant error is at most 2m eta_n once
eta_n<=1/2. Hence it tends to zero at the stated rate and the
physical determinant recovers exactly the product d_i^2.
This is a relative determinant theorem for a particular growing
actual selection. It does not establish an inverse for the full
high matrix, consecutive clusters, or the endpoint kernel angle.
The generic rank consequence is weaker than the already proved
individual-parity rank bound; the new content here is the specific
column selection, quantitative conditioning, and relative Gram
determinant asymptotic.
