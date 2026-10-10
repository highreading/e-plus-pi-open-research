> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: the Schur boundary limit and operator topologies

Date: 2026-09-13. Reviewer: root. FULL PASS.

Reviewed raw_even_schur_boundary_limit.md against the explicit circular
polynomial recurrence and the previously reviewed correction identity.

The recurrence parameter m/(m+j) and its final value 1/2 are correct.
On every compact w-disk the map B->(wB+a)/(1+awB) contracts hyperbolic
distance by at most |w|. The first constant-parameter step puts all
starting states in a compact disk; comparison of finitely many final
parameters followed by the contraction limit is uniform. The selected
fixed-point solution gives exactly the displayed beta(z), with constant
term 1/2 and the specified square-root branch.

The finite beta_m are inner, but the analytic continuation of beta near
z=1 has boundary modulus strictly below one on an arc. Thus its Hardy
norm b is strictly below one. Local coefficient convergence and bounded
Hardy norms give weak convergence; the norm defect sqrt(1-b^2) follows
by expansion of the squared difference, not by an assumption of strong
convergence.

The exact model-space identity and its dimension n+1 are correct.
The multiplier adjoints converge strongly on fixed polynomial inputs
and then on the whole space. This proves the stated weak projection
limit. Its action on z has quadratic form 3/4 and norm squared
1/2+b^2/4; the strict difference correctly rules out a projection and
strong convergence of projections.

The quadratic correction has the correct sign absorbed in beta_m.
For the cubic correction, only the Laurent moment n+2 survives: both
base measures are even, so n+3 vanishes. The coefficient identities
follow either from the backward shift or expansion of p/Psi at infinity;
the degree n-1 coefficient of Psi is zero. The two Riesz vectors are
1 and P_m z. These verify every term in the rank-two formula. Its
singular values have common size a_m sqrt(3)/2 by parity and the norms
of beta_m, S*beta_m, and P_m z.

The strong-but-not-norm quadratic limit and weak-but-not-strong cubic
limit are valid with the stated defects. Applying the quadratic
correction to the varying input beta_m gives the precise counterexample
to passing local limits through that operator on an uncontrolled varying
solution. The note does not mistake this example for the actual R_n.

The remaining need for joint boundary coordinates is mathematically
substantive and should be retained in any proposed factor-limit proof.
