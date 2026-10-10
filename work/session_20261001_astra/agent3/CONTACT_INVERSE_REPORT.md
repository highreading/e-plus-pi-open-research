> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Contact inverse: completed author report

Status: uniform quantitative author derivation, conditional on the explicitly provisional exact contact reduction pending Child 4. No independent audit is claimed.

For n>=16, 2<=b<=n, n>=512b^4 log n, both actual rational endpoint forcing columns are retained in the exact b-by-b Toeplitz solve. With r=sqrt(2), M=1+r and D_r=diag((-r)^j), the evaluated inverse bound is

    ||D_r T^(-1)f||_2 <= K0 M^(-n)||D_r f||_2,
    K0=2048b sqrt(n)(16b^2 n)^(b-1)
                   binom(2b-2,b-1)/((b-1)!)^2.

A localization proof by separated Lagrange interpolation and an accretivity estimate establish this bound for the entire scaled operator, including odd-n negative tails. No determinant-only estimate or Neumann series is used.

The two forcing columns satisfy fQ=(e+pi)fP+residual, with explicit bounds for both complete residual functions. Reconstruction retains the finite inverse of (D+1)^n, the actual B endpoint constant, and the full moment reconstruction of C and A. Sections 9.1–9.5 of CONTACT_INVERSE_RESEARCH.md complete the constants that the initial save marked pending.

For the explicitly defined positive rational full-coefficient norm W and weights wmin>=(2n)^(-b), the full rational endpoint lift satisfies

    ||Phi(P,Q)-(P+(e+pi)Q)Phi(1,0)||_W
       <= exp(-n/8)||Phi(1,0)||_W |Q|.

This is a relative directional estimate. It does not imply a small absolute correction or a small primitive form.

The actual B lift Psi gives Sigma=Psi^T diag(w^2)Psi. Explicit bounds are provided for Sigma11, its rational center, and det(Sigma)/Sigma11. In particular endpoint matching gives the exact lower bound

    det(Sigma)/Sigma11 >= 1/sum_j w_j^(-2).

The full-coefficient Gram matrix lies between Sigma and 3Sigma. For Child 2's multi-row weights, retain instead its complete certificate

    G=2[e2 e2^T+Z Sigma], eta=dk,
    G11=2Z Sigma11,
    det G/G11=2(1+Z det(Sigma)/Sigma11).

The pi-error term is not dropped. The actual rational center is Sigma12/Sigma11; no reduced-denominator estimate follows from its closeness to e+pi. Child 4 owns that arithmetic. Integral lifting multipliers cancel against each endpoint gcd.

The multi-row interface applies for b>=3 in Child 2's stated subtraction range. The inverse estimates cover b=2 as well, using the unsubtracted full-tail identity there.

No new HP scans, prior checker replays, prime scans, or networking were performed. Earlier artifacts are preserved. Deliverables: CONTACT_INVERSE_RESEARCH.md, CONTACT_INVERSE_REPORT.md, CONTACT_INVERSE_INTERFACE.md, and the already saved scalar identity checks. Final read-back is the remaining artifact-verification step.
