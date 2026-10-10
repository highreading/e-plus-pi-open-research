> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: dual product, Mahler bound, and comparison family

Date: 2026-09-13. Reviewer: root. FULL PASS.

Reviewed raw_dual_product_mahler_and_factorization_obstruction.md against
the passed full-circle second-kind identity and the actual normalization.

The identity P=vB/v0 follows with the displayed reciprocal variable and
the normalized circle integral. Its constant term is one. The sector
estimate bounds each of its coefficients by sec(1); moments above its
degree vanish because the identity holds on a disk. The closed-disk
positivity argument is valid at radius cos(1): the integrand is strictly
positive off finitely many points, and the polynomial density cannot
vanish on a set of positive measure.

The use of Mahler measure is exact even when v has degree below n or U
has a root at zero. Both normalized factors have constant one and hence
Mahler measure at least one. Multiplicativity, Jensen and Parseval give
the asserted logarithmic radial excess, without implying pointwise
control of either factor. The contour formula preserves the clockwise
orientation and factorials from the preceding reviewed note.

The explicit comparison is valid on n divisible by four. Each half-plane
root collection is invariant under conjugation; its factors have constant
and leading coefficient one. Squaring the argument gives degree n, the
required final coefficient c_m, and product 1+c_m^2 z^(2n). All roots are
outside the unit disk. The factorial coefficient map retains the exact
root-product normalization. The exponential lower estimate follows from
the conjugate-pair factors at a positive argument and R_n<=sqrt(2).

The rational-density extension also passes: all fixed coefficients are
rational; the other inequalities have strict margins in finite degree.
Perturbations preserve parity and the constant term, so the proposed
coefficient error gives a product lower bound 1-t^2/4 on [-1,0]. This is
at least 1/(1+t) for 0<=t<=1. No denominator-height estimate is asserted.

The comparison intentionally does not satisfy the same weighted Cauchy
identity or the actual high-order Padé equation. It is a valid obstruction
only to deductions from the listed scalar consequences in isolation.
It is not a counterexample to a claim about the canonical HP family.
No proof of irrationality, signed contour bound, or endpoint gcd estimate
follows from this result.
