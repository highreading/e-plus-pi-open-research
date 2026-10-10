> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: actual Hardy factor allocation

Date: 2026-09-13. Reviewer: root. FULL PASS for sections 1--7 of
raw_actual_dual_hardy_factor_allocation.md as first saved, ending with
equation (26). Later additions require separate review.

The finite Bernstein--Szego moment replacement is proved correctly.
The two measures give the same monic orthogonal polynomial Psi and
its norm. The annihilated Laurent polynomials span all degrees -n to n:
after multiplication by z^n their span is Psi P_n+F P_n. Coprimality
holds because the roots lie on opposite sides of the unit circle, and
both degrees are n. The intersection is exactly the span of Psi F.
This establishes the norm identity for all polynomials of degree <=n,
without asserting equality of any higher moments.

The sharp scalar accretivity proof and actual energy identity give
||v||_w^2<=e v0. Combining the exact norm identity with the earlier
sector lower bound for v0 yields the stated Hardy constant e sec(1).
Evaluation at zero independently gives the sharper upper bound v0<=e c_m.

The Mahler identity remains valid for deficient degree of v and for
zero roots of U. Since F has no closed-disk zeros and constant one,
its mean logarithm is zero. Jensen thus gives constant outward radial
excess. This uses the actual energy equation and is not contradicted
by the preceding comparison family, which omits that equation.

For fixed disks below cos(1), the earlier actual zero exclusion
permits the logarithm normalized at zero. Harnack and the positive
harmonic Fourier coefficient bound have the correct factors 2r/(R-r)
and 2/R^j. The resulting root-power-sum discrepancies are uniform in n
at every fixed order. Direct expansion checks the second and fourth
comparison sums: m and -m(m-2)/(2(2m-1)), respectively. These are
complex power sums, not absolute powers.

The signed Hardy pairing retains the clockwise contour orientation:
parametrizing the left semicircle with increasing angle reverses it
and gives the factor -pi in normalized Haar measure. Its kernel is
square integrable. Parseval and Cauchy--Schwarz justify the pairing
and the interval using C_*^2-1, since the constant coefficient of R
is exactly one. Reality follows from conjugation symmetry.

No relative smallness of the explicit kernel's nonconstant Hardy
coefficients is proved. The note correctly retains this analytic
question and the original primitive endpoint gcd as separate barriers.
