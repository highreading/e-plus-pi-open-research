> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational-center coordination interface

New author research only; the prior contact inverse remains provisional and is not re-audited.

For Child 4: RATIONAL_CENTER_ASYMPTOTICS.md, Section 2, gives an exact rational formula for the full-coefficient center from the two forcing columns and adj(T). All factors from B=Q+(z-1)v and reconstruction of A,C are retained. No reduced-denominator conclusion is drawn. The algebraic coefficient L(1-1/sqrt(2)) is defined by the rational adjoint solve; testing its value does not require e+pi.

For Child 2: with its rational B weights, the B-only center is obtained by replacing H=R^T W R with diag(w_j^2) in the same formulas. That center need not equal the full-coefficient center. The new exact error decomposition retains the endpoint term and both exponential and logarithmic components. It does not replace the complete pi-error term or independently rederive the complete functional certificate.

The main new analytic statement is the signed additive enclosure

    |(-1)^(n+1)(t-e-pi)/A_n-L(zstar)|
      <=Nlambda[(12+(b-1)^2)/n+rho_(n,b)],

where zstar=1-1/sqrt(2), A_n=2n!(sqrt(2)-1)^n sqrt(pi/(cn)), c=(2+sqrt(2))/2, and rho_(n,b) is explicit and at most exp(-n) in the slow range. The proof keeps both conjugate endpoints via an exact real-arc integral.

The missing substantive lemma is a uniform lower bound for |L(zstar)|/Nlambda above this additive remainder. Without it, the leading sign and a nonzero two-sided error estimate are not established on an unbounded growing-b set. The current research stops at this gap rather than extrapolating a fixed-b expansion.

No old certificates were changed and no new HP samples or checker replays were performed.
