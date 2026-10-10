> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact change of variable from the Item426 period kernel to Items306/309

2026-09-13. Auxiliary identity, not a completed finite-field Witt bridge.

Item426's phase kernel uses u=x(1-x), Q=(1+x)(1+x^2), and

    u^r Q^(-2r/3-1-nu) dx, nu=0,1.

Make the involutive substitution

    z=(1-x)/(1+x), x=(1-z)/(1+z).

Then direct rational algebra gives

    u=2z(1-z)/(1+z)^2,
    Q=4(1+z^2)/(1+z)^3,
    dx=-2 dz/(1+z)^2.

Writing X(z)=z(1-z)/(1+z^2)^(2/3), exactly as in Item309, gives

    u/Q^(2/3)=2^(-1/3)X(z).

With compatible local branches, the two differentials are therefore

    u^r Q^(-2r/3-1) dx
       =-2^(-r/3-1) [(1+z)/(1+z^2)] X(z)^r dz,

    u^r Q^(-2r/3-2) dx
       =-2^(-r/3-3) [(1+z)^4/(1+z^2)^2] X(z)^r dz.

The bracketed factors are precisely Item309's phi_0 and phi_1. The map sends

    x=0,1,-1,i,-i,infinity
    to z=1,0,infinity,-i,i,-1,

respectively. In particular Item426 endpoint integrals with base x=0 become old-kernel integrals based at z=1, not at z=0. Under a six-step increase of r the common 2^(-r/3) normalization changes by1/4; the relative nu normalization is the constant1/4.

This explicit identity explains why the formal period recurrence is closely related to the archived two-form Hermite identities. It permits pulling those rational differential identities through the substitution; one need not infer a relationship merely from similar characteristic polynomials.

The identity by itself does not identify the actual finite-field zero-constant primitives T_nu(zeta), their Cartier sections, or the two endpoint functionals R_j,L_j. At actual exponents, Frobenius powers and the inherited branches must be retained. In particular a phase meromorphic finite part must not silently replace a primitive with a nontrivial characteristic-p additive constant. A completed Item426 bridge still needs this actual-coordinate audit and a nonzero initial exterior state.
