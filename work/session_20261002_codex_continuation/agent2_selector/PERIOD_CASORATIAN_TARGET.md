> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual quotient minor through a beta-period / Casoratian representation

2026-10-02. New structural subtarget of the parent-requested constant-shift recurrence problem. Goal: express the actual three-output scalar τ_n, or an equivalent regular quotient determinant, in a form whose nonvanishing can be proved uniformly for n=4k and m≈ρn log n. The whole positive-axis statement remains open.

Archive search before pursuing this subtarget: `Hahn`, `dual.Hahn`, `Jacobi.*Casorat`, `Casorat.*Jacobi`, `beta.*moment.*quotient`, and `quotient.*beta.*moment` in the prior session and sources. The relevant opened overlap was `sources/mixed_cubic_large_prime_two_pole_obstruction.md`, Sections 3–4: its terminating Hahn/Heun-type coefficients concern a different two-pole modular contraction and explicitly do not get a generic root-separation escape. No present actual-W quotient determinant formula was located. A separate search for observability/Casorati/desingularization located generic archived recurrences but no usable proof for this output.

Online primary-paper searches: "Hahn dual Hahn Casorati determinant zeros positive negative exceptional polynomials", "Hahn polynomials Darboux Casoratian determinants nonzero theorem", "Jacobi polynomials beta integral discrete derivative Rodrigues formula", "Antonio Duran Exceptional Hahn Jacobi orthogonal polynomials arxiv 2016 Casorati", and "Antonio Duran exceptional dual Hahn orthogonal polynomials arxiv nonvanishing Casorati".

Opened relevant primary full texts:

- Roy Oste and Joris Van der Jeugt, *Doubling (Dual) Hahn Polynomials: Classification and Applications*, arXiv:1507.01821, https://arxiv.org/pdf/1507.01821. It relates contiguous Hahn/dual-Hahn pairs and Christoffel/Geronimus transformations; identification of our exact polynomial with such a family has not been established.
- Antonio J. Durán, *Exceptional Hahn and Jacobi orthogonal polynomials*, arXiv:1510.02579, https://arxiv.org/pdf/1510.02579. Its Casorati determinants require explicit parameter/admissibility hypotheses to infer nonvanishing and positive measures. Those hypotheses cannot be borrowed before an exact identification.
- Antonio J. Durán, *Exceptional Charlier and Hermite orthogonal polynomials*, arXiv:1309.1175, https://arxiv.org/pdf/1309.1175. Same classical Casorati/Darboux mechanism; no direct application is presently claimed. A later corrigendum concerns completeness arguments, which are unnecessary for the present finite determinant target.
- Yi Zhou and Mark van Hoeij, *Desingularization and p-Curvature of Recurrence Operators*, arXiv:2202.08931, https://arxiv.org/pdf/2202.08931, Sections 2.1–2.2. Apparent singularities can be removed by left multiples, with order-dependent bounds; generic desingularization does not supply an n-independent shift count here.

Overlap and new obligation: beta moments, Christoffel transformations, and Casorati nonvanishing criteria are classical. The missing project-specific work is an exact representation for the actual n+1 weighted difference and a uniform verification of its signs, parameters, or integer units. No novelty is asserted for those generic mechanisms.

## A first exact period coordinate

Let n=2r, V(w)=w²−w+1/2, q(w)=2w²−1, and write b_j=[w^j]V(w)^n. The symmetric complete beta period of the original rational integrand, interpreted by analytic continuation / finite parts where necessary, has the ratio

    H_n(m)=Σ_(k=0)^(n−1) b_(2k+1) 2^(r−k)
         (1/2)_(k−r)/(2m+3/2)_(k−r)

to the base period C_m=2^(−1/2)B(1/2,2m+1). Here the factorials in this displayed ratio are rising factorials, extended to negative integer indices by the gamma ratio. All half-integer arguments avoid gamma poles. This expression is a rational function of m.

The formula follows term by term from the symmetric even powers w^(2(k−r)) in V(w)^n/w^(n+1); odd powers integrate to zero on the symmetric finite-part cycle. Each even term contributes 2^(r−k−1/2)B(k−r+1/2,2m+1).

This is an auxiliary period coordinate of the exact recurrence module. It is not an approximation to the actual contour I and not a replacement for W. The actual output applied to this homogeneous period is

    F_n(m)=Σ_(j=0)^(n+1) (-1)^(n+1−j) binom(n+1,j)
             U(n,m+j)H_n(m+j) C_(m+j)/C_m,

where C_(m+j)/C_m=(2m+1)_(2j)/(2m+3/2)_(2j). This coefficient can be compared with the direct pole-cancelled polynomial-period reduction. Nonvanishing of F alone does not establish nonvanishing of the full three-output determinant.

Exact symbolic exploration will test whether this coordinate and the endpoint coordinates admit a recognisable hypergeometric or positive Casoratian representation. It will not fit recurrences to sampled W values.

## Exact initial period-coordinate evidence

`derive_beta_period_coordinate.py` performs the stated gamma-ratio reductions over Q(m), then applies the actual U-weighted n+1 difference. The data and factorizations are saved in `beta_period_coordinate_n4.json` / `.log` and `beta_period_coordinate_n8.json` / `.log`.

For n=4,

    H_4=−16m(8m²−24m−23)/[3(4m+3)].

For n=8,

    H_8=−32m(512m⁶−17920m⁵+75712m⁴+244160m³
              −222152m²−775600m−387367)
          /[105(4m+3)(4m+5)(4m+7)].

The transformed period coefficient F_n has a positive-coefficient numerator and a positive linear-factor denominator in both exact cases. Its numerator degree is 5n/2 and denominator degree 5n/2+1; the denominator is ∏_(j=0)^(5n/2)(4m+3+2j). Thus F_4,F_8 are strictly positive for m≥0. These are whole-function symbolic results rather than sampled contour values. They suggest a positive beta-integral identity for this single period output. Such an identity is not proved for all n, and positivity of one output coordinate would still not force the three-output determinant nonzero.

The initially considered shortcut "constant coefficient uniquely dominates 2-adically in the τ numerator" was rejected on the already saved exact n=4,8 polynomials. Their primitive numerator constant-term valuations are 9 and 14 respectively, while the minimal coefficient valuations are 0. The exact valuation arrays are in `weighted_observability_integer_obstruction.json`; this attempt provides no all-integer nonvanishing theorem.
