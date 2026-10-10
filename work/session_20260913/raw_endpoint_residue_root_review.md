> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root mathematical review of the endpoint residue theorem

Date: 2026-09-13. Reviewer: root. FULL PASS.
This supplements raw_even_endpoint_residue_independent_review.md.

I checked raw_even_endpoint_residue_asymptotic.md in full. The original
residue has a minus sign; on even n, replacing (z-1)^(n+1) by
-(1-z)^(n+1) cancels it. The counterclockwise circle integral therefore
has precisely the positive 1/(2pi i) normalization displayed there.

The algebraic b-map and its imaginary-part identity correctly imply
strict angular decrease of Re h in the upper half-plane and increase
in the lower half-plane. On the original z-circle, this makes the
even part maximal at +/-r. The additional factor 1/|1-z| selects +r
uniquely. This establishes a global gap with no sampled maximum.
The branch and nonzero denominators are justified on the open disk.

At r=rho the first derivative vanishes and the angular curvature is
kappa=rho^2(25+11sqrt(5))/4=5/2+sqrt(5). The whole-circle amplitude
is uniformly bounded and converges, using the already proved actual
factor theorem. A Gaussian majorant and the compact phase gap justify
dominated convergence on the expanding scaled interval. The prefactor
is e^H B_s/[(1-rho)sqrt(2pi kappa)], with no missing factor rho from dz.

The quotient of exterior and interior constants is exactly
pi rho A_s/B_s: the common transport cancels, and the curvature ratio
is rho^(-10). Thus the actual reduced rational value obeys

    (e+pi)-N_n/Z_n ~ (-1)^(n/2) C_app rho^(5n),
    C_app=4pi rho A_s/B_s>0.

The signed Re contribution is factorially smaller. The eventual sign
of Z matches that of u_n and of Vlead_n. Finally, reduction multiplies
this relative error by the positive integer q_n; it does not remove
that integer. The exact remaining criterion is q_n rho^(5n)->0 on
a chosen even subsequence. This arithmetic claim remains unproved.
