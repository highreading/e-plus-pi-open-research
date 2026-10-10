> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational-center arithmetic report

The limited normality review is complete and was read back: PASS for n>=16, 2<=b<=n, n>=512 b^4 log n, including the stated unbounded allocation. No defect was found in the scoped theorem. This does not review the new quantitative inverse theorem or cover proportional b.

RATIONAL_CENTER_ARITHMETIC.md contains new exact arithmetic for the multi-row complete-bound matrix

    Sigma=Psi^T diag(w_j^2)Psi,
    G=2[e2 e2^T+zeta Sigma], eta=d_k.

This G has center Sigma12/Sigma11. Child 3's full-coefficient Gram matrix contains additional A/C terms and generally has a different center. The note records both exact conversions; it does not identify their reduced denominators through a norm comparison.

The actual B lift can be constructed using the b by b Toeplitz adjugate and both endpoint forcing columns. With w_j=tau(lambda)_j, the common factorial factor and the adjugate denominator cancel before reducing the center. The resulting denominator is an exact gcd of weighted integer contractions, not a lift clearer.

The stronger saturated-lift description is

    Phi=(1/d)K[[g1,g2 t],[0,g2 c_perp]],
    det-minor-content(K)=1,
    chi=g1 g2 c_perp=gcd(d,t2(d Vprim)).

Let A_*,H_*,C_* be the integer Gram contractions of the B blocks of K with weights (lambda)_j, and D_*=A_*C_*-H_*^2>0. Then

    kappa=gcd(g1 A_*,|g2(t A_*+c_perp H_*)|),
    q=g1 A_*/kappa.

All factors are retained. With r_*=gcd(A_*,|H_*|),

    r_* divides kappa, kappa/r_* divides chi.

The primitive center direction's minimal integral lifting factor—and its endpoint gcd—is exactly d kappa/(chi r_*). It cancels from the primitive full remainder and is not q.

The direct connection to the COMPLETE directional defect is

    q^2 det(G)/G11^2
      =[(g2 c_perp)^2 D_*+d^2 A_*/(zeta tau^2)]/kappa^2.

The second term retains the pi error. Since eta^2 G11>=2 for this normalization, a shrinking center certificate necessarily requires

    kappa/[(g2 c_perp)sqrt(D_*)] -> infinity.

The note also proves primewise restrictions from D_*=A_*C_*-H_*^2, including an exact valuation when v_p(D_*)<v_p(A_*). These hold at every prime, including 2. No random coprimality is assumed.

For fixed n,b, the actual weight contractions are integer polynomials in lambda=n+m+1. Their finite-difference recurrences and capped gcd-valuation congruences give an exact update mechanism across admissible subtraction depths. The weighted determinant retains all projected-minor content; in particular lambda^2 divides it. These statements are not a recurrence theorem as n,b grow.

With Lambda0=18(b+1)L_k^2/[A_k^2(k+1)!^2d^2], the two exact remaining budgets are

    E=Lambda0 kappa^2/A_*,
    F=[2d_k^2 g1^2 A_*^2+Lambda0 chi^2 A_*D_*]/kappa^2.

Useful same-index asymptotics for both remain open. The inverse paper's orientation estimate alone does not determine the gcd. No irrationality conclusion is claimed.

Actual verification: the new saved symbolic checker ran successfully, exit code 0, PASS_NEW_SYMBOLIC_IDENTITIES, 21 checks; all six specified input hashes remained unchanged. The checks concern new formal identities and an abstract polynomial example, not contact-family samples. The paper supplies the divisibility proofs. Supporting files are check_rational_center_structure.py, rational_center_structure_checks.json, and rational_center_structure_stdout.txt. No old audit or its 907 checks was repeated.
