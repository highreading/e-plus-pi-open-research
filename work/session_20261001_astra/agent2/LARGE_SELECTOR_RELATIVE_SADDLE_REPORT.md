> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Relative endpoint saddle report

New author analytic proof; no numerical computation, repeated checks, or independent review. The saved high-high adjacent-pair theorem is preserved.

For the exact upper endpoint integral, uniformly on

    m=rho n log n+O(n log n/log log n), rho>0 fixed,

the new result is

    log|J_m|=m log 2-n log(m/n)+O_rho(n),
    J_(m+1)/J_m=-2i[1+O_rho(1/log n)].

Both assertions follow from a stronger relative formula. Put lambda=n/m, nu=1/n, alpha=(1+i)/2, and

    C0(x)=1-x+(1+i)x^2/4,
    phi(t)=log t+(2/lambda)log C0(lambda t)
       +log(1-lambda t/2)-(1+nu)log(1-alpha lambda t).

Let t_s be its exact critical point near 1/2, and beta=-phi''(t_s), with the square root tending to +2. Then

    J_m=[i/(2alpha)](2alpha)^(-n)(-2i)^m lambda^(n+1)
            exp(n phi(t_s)) sqrt(2pi/n) beta^(-1/2)
            [1+O(1/n)].

The relative error is uniform for sufficiently small lambda and large n. The proof bounds distant parts of the original segment, deforms only a central pole-free rectangle to a horizontal contour through t_s, and proves uniform Gaussian dominance there. It therefore controls competing contributions without an unproved global saddle decomposition.

The exact original-coordinate saddle solves

    n V'/V+m A'/A-(n+1)/w=0.

Its leading displacement is alpha-i n/(4m)+O((n/m)^2). This corrects the earlier provisional alpha+1/(8kappa) location. The full exact root is used in the theorem. In particular n phi(t_s) contains a phase correction of order n^2/m, which is retained rather than discarded.

The adjacent ratio implies, eventually,

    max(|Im J_m|,|Im J_(m+1)|)>=|J_m|/2.

Combine this with any of the preserved high-high eligible edges. Both endpoints retain log|U|=(1/2+o(1))n log log n, while at least one has a large normalized logarithmic error. The main complete-exponential estimate is factorially small and cannot cancel that error.

An explicit finite rule selects the first high-high edge and then the endpoint maximizing |Im(Z_j/U_j)| using the already defined finite Gaussian-rational sums. Their saved truncation error is negligible relative to the proved lower bound. No search was executed. For that selected sequence,

    log|c_(n,j)-(e+pi)|
        =j log 2-(3/2+o(1))n log log n,

so the complete rational error itself diverges and its leading n log n rate is rho log 2. The exact adjusted j must remain in the subleading formula.

Conditional on the main actual dyadic denominator theorem,

    liminf log(q_(n,j)|c_(n,j)-(e+pi)|)/(n log n)
        >=3rho log 2.

This uses the fully reduced q. It is a scoped divergence result for the selected family, and for at least one endpoint of each guaranteed high-high edge. It does not exclude every eligible node or other selectors, and it proves no irrationality statement.

Full proof and phase conventions: LARGE_SELECTOR_RELATIVE_SADDLE.md. Both new files require read-back before completion is reported.
