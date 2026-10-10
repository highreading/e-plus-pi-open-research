> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Canonical adjoint derivative report

Original author research, conditional on the retained provisional contact reduction and quantitative estimates. No independent review, numerical scan, or old-control replay. The preceding deflation and B-adjoint files are preserved.

The principal advance is a proved derivative bound for the ACTUAL canonical residual H after G=psi^r H. Set B=F_n(G)/fP_0>0, h=b-1-2r, and

    Ccan=18 b (n+1)^(b-1)(n+b)^(b-1)
                         K0 2^(b-1)/wmin,
    L_r,h=sum_(j=0)^h [t^j]psi^(-r), r>=1,
    L_0,h=1,
    E_k=sqrt(sum_(j=k)^h binom(j,k)^2 A^(2(j-k))).

Then

    |H^(k)(A)|/k! <= B Ccan L_r,h E_k.

K0 is the explicit retained inverse constant, stated in the main note. The proof combines the exact positive-circle identity fP_0=n! Zplus with the canonical SPD equation C lambda=fP/a, where C=T K^(-1)T^T. It bounds point evaluations by canonical energy; it does not infer them from an averaged positive quantity. All factorial and exponential scales cancel in the displayed bound.

Consequently, for q=deg H,

    |H(a*)| >= 1/(2^q B Ccan L_r,h E_0).

For odd r, if psi does not divide J_r=rH+(t-1)H', there is also

    |J_r(a*)| >=
        1/(2^q B Ccan L_r,h(rE_0+E_1/sqrt(2))).

These use the nonzero integer resultants. The actual scale B is retained; no selector-height substitute is introduced.

A new rational projection recurrence provides exact deflation control. With M_s multiplication by psi^s, C_s=M_s^T C M_s, Y_s=C_s^(-1)M_s^T fP, and a_s=fP^T M_sY_s, canonical divisibility is exactly a_s=a_0. Each next step subtracts a nonnegative quadratic form in the two rational remainder coordinates of Y_s modulo psi. The main note supplies both the coefficient projection and its Taylor recurrence at A.

The odd secondary obstruction is likewise exact: form E from the independent rows of the remainder matrix times the operator r+(t-1)D. Then

    deltaJ=(E Y_r)^T(E C_r^(-1)E^T)^(-1)(E Y_r),
    psi divides J_r iff deltaJ=0.

There are at most two rows. For residual degree capacity h<=1 this vanishing is impossible. For h>=2 its exclusion for the canonical family remains an explicit unresolved rational zero condition.

Every endpoint correction is retained through an explicit weighted projection formula for kappa. The main note also retains the complete exponential contribution and all higher arc coefficients. The new derivative upper bounds do not yet prove the remainder-dominance inequality, so unbounded-family complete nonvanishing remains open.

Domain: even n, 3<=b<=n, n>=16, n>=512b^4 log n, with the allowed factorial weights. This includes the retained logarithmic allocation for even n>=2^96.

Operational completion requires successful saving and full read-back of both new files.
