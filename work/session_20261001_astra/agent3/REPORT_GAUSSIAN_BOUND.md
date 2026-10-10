> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Agent 3 report: Gaussian Vandermonde refinement

Status: proved analytic refinement. Full proof and normalization ledger are in GAUSSIAN_VANDERMONDE_BOUND.md in this directory. No numerical computation, HP degree sample, or prime scan was used.

The proposed identity is correct:

    (2pi)^(-d) integral_(R^d) exp(-a sum theta_i^2)Delta(theta)^2 dtheta
      =(2pi)^(-d/2)(2a)^(-d^2/2) product_(j=1)^d j!.

The proof constructs monic Hermite polynomials by differentiation, derives their norms by integration by parts, and proves the determinant integration identity by expanding permutations. It includes the one-dimensional Gaussian constant and every factorial. No named multiple-integral evaluation is assumed.

With a=2R/pi^2, replace the old J_d(R) by

    J_VdM,d(R)=(2pi)^(-d/2)(4R/pi^2)^(-d^2/2)
                                              product_(j=1)^d j!.

The determinant bounds remain C_G E_n(R)^d J_VdM,d(R)/d! for differences and C_G [E_n(R)/(R+1)]^d J_VdM,d(R)/d! for ordinary functionals. Their domains are respectively d<=b and d<=b+1. The actual applications are d=b for D_V,D_W and d=b+1 for T. Agent 2's source-domain edit is not duplicated.

The exact improvement factor, for unchanged row bounds and radius, is

    B_old/B_new
      =2^(d(d-1)) Gamma(d^2/2)
           /[Gamma(d/2) product_(j=1)^d j!].

It is independent of R. Elementary trapezoidal estimates for factorial sums and exact half-integer Gamma identities justify

    log(B_old/B_new)
      =(d^2/2)log(2d)+d^2/4-(3d/2)log d+O(d).

Therefore for b=floor(n/2), d=b or b+1, and any fixed lambda>0 with R=lambda n>20,

    log(B_old/B_new)
      =n^2 log n/8+n^2/16+O(n log n).

The new Gaussian factor has no n^2 log n loss. With its outside 1/d! retained explicitly,

    log[J_VdM,d(lambda n)/d!]
      =(n^2/8)log(pi^2/(8lambda))-3n^2/16+O_lambda(n).

The proof records the full C_G and E_n contributions, the reference value |p_(n+1)(0)|, the reciprocal-root correction, the high-row product (3/4)^((b-1)(b-2)/2), the special V/W row bounds, and the outside 1/d!. Explicit coefficient estimates give log M_V,log M_W=O(n), while the reference and fixed-disk factors contribute O(n^2). Hadamard and the outside factorial contribute O(n log n).

For these explicit choices, the three new cofactor upper-bound expressions have logarithm

    -n^2 log n/2+O_lambda(n^2),

compared with -3n^2 log n/8+O_lambda(n^2) for the old radial expressions. The removed positive n^2 log n/8 cost was an artifact of replacing the Vandermonde by a radial power. These statements concern bounding expressions, not determinant asymptotics.

The remaining normalization gaps are unchanged: a lower bound/nonvanishing theorem for D_V, nonvanishing and cancellation control for D_W+T, and estimates for the actual reduced denominator q including the endpoint gcd. The exact primitive form still satisfies |L|=q|D_W+T|/|D_V|. Small absolute cofactors do not bound this quotient, and the positive auxiliary Gaussian does not make the complex contour integrand positive.

Files written only under work/session_20261001_astra/agent3/:

- GAUSSIAN_VANDERMONDE_BOUND.md — complete proof, exact endpoint bounds, factorial/Gamma estimates, and normalization ledger.
- REPORT_GAUSSIAN_BOUND.md — this report.

The completed b=1 certificate and growing-degree audit are preserved. This bounded task stops here; no fixed-b theorem is repeated and no new arithmetic or nonvanishing conclusion is claimed.
