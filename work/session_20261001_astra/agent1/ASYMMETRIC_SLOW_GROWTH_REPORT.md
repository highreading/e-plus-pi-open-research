> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Asymmetric slow-growth research report

Scope: a=2n, c=n, b=max(1,floor(log n)), contact M=3n+b, endpoint matching B(1)=C(1). Work is offline and confined to this directory. Previous companion-audit artifacts are preserved unchanged; that audit was not continued.

The exact high equations use the changing complex-segment weight t^n:

    ell_j(t^r)=1/(2n+1+r-j)!,
    ell_beta(t^r)+L(t^(n+r)Cstar)=0,
    0<=r<=n+b-2.

Together with matching, these are n+b equations in n+b+2 rational unknowns. There are at least two rational solution directions. Nonzero matched endpoints and a controlled choice of direction remain separate rank/height questions.

When the weighted (n+1)-by-(n+1) Gram matrix G_n is invertible and b>=2, projection reconstructs Cstar. The remaining beta system has b-2 high constraints plus matching. Singular cases and b=1 are explicitly retained in the full formulation. Contact M+1 adds one equation and ordinarily removes one free direction; no normality conclusion follows from counting.

The complete endpoint formula is

    X=-sum beta_j Epartial_(2n-j)-sum gamma_i sigma_(n+i),
    Y=sum beta_j=sum gamma_i,
    R(1)=X+Y(e+pi).

The weighted CD formula, under its additional finite normality hypotheses, contains the essential rational shift -sigma_n in X/Y because L(t^n/(1-t))=pi-sigma_n. Both partial-exponential and second-kind terms are retained.

A new uniform complete-tail estimate is

    |R(1)|<=e||beta||_1/(3n)!
                  +4rho^(2n+b-1)||gamma||_rho,
    rho=1/sqrt(2).

On the projected domain it becomes

    |R(1)|<=||beta||_1[e/(3n)!
                 +4rho^(2n+b-1)Kappa_n/(2n+1-b)!],

where Kappa_n is an explicitly defined weighted sum of entries of G_n^(-1). The proof also supplies contour determinant bounds with every dimension, selector and conditioning factor displayed. None is interpreted as a quotient by dividing two upper bounds.

For primitive integral B,C, the integer derivative recurrence for F proves that Delta_clear=(2n)! clears A. With

    g_ep=gcd(|Delta_clear X|,|Delta_clear Y|),

actual rational reduction gives

    q=|Delta_clear Y|/g_ep,
    |L_int|=Delta_clear |R(1)|/g_ep.

Consequently the explicit post-clearing bound is

    |L_int|<=||beta||_1/g_ep *
       [e(2n)!/(3n)!
        +4Kappa_n 2^(-n)(sqrt(2)n)^(b-1)].

The exponential term has logarithm -n log n+O(n); the displayed logarithmic-tail factor has logarithm -n log 2+O((log n)^2). This changes the formal analytic/arithmetic budget, but does not settle it: weighted conditioning, integral direction height and final endpoint cancellation remain uncontrolled.

One subroute is rigorously stopped. The conservative inverse bound

    Khat_n=(n+1)^2 n^(n/2)2^(n^2+3n)
                   lcm(1,...,3n+1)^(n+1)

is a valid ceiling on Kappa_n when G_n is nonsingular. Substituting it into the positive normalized error certificate forces that certificate to diverge, independently of q>=1. This excludes that coarse certificate, not the family or differently rebuilt estimates.

A concrete different allocation for a follow-up is a=n+1, c=n, with the same slowly growing b and contact 2n+b+1. Its weight is fixed t rather than t^n. No indices for that alternative were evaluated and no success is claimed. The requested allocation remains open through sharper weighted conditioning or direct quotient estimates.

The old quadratic slack argument for b of order n has not been imported: its ordinary Legendre ratio hypotheses are unavailable for this weight, and the present high-row count is only of order log n. Slow b alone does not control the actual quotient.

Evidence: the initial formal identity execution passed, and check_asymmetric_slow_growth.py subsequently passed all 15 symbolic controls. The latter verified that the generated companion checker, successful certificate and stdout stayed unchanged. These checks support the written formulas; no weighted rank, uniform conditioning, denominator growth or nonvanishing theorem was computed or inferred.

Deliverables:

- ASYMMETRIC_SLOW_GROWTH.md: full derivation, uniform estimates, exact endpoint reduction, stopped certificate and remaining gaps.
- ASYMMETRIC_SLOW_GROWTH_REPORT.md: this report.
- check_asymmetric_slow_growth.py and asymmetric_slow_growth_checks.json: necessary symbolic controls.
- asymmetric_formal_evidence.json: initial integral and dimension checks.

No irrationality, primitive shrinking, actual-family divergence, or equivalence to an excluded construction is established.
