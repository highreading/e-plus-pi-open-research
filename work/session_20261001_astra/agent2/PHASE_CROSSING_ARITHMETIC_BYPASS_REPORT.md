> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Arithmetic bypass report

Status: new author deductions, not independently reviewed. Earlier phase, derivative-controlled continuation, saddle, and block results are preserved. No numerical phase scan or new computation was performed.

Main document: PHASE_CROSSING_ARITHMETIC_BYPASS.md.

The exact matching parity roots remain r_(epsilon,k)=psi_n^(-1)(epsilon*pi/2+k*pi). The necessary proximity for bounded complete primitive error remains exp(-kappa_rho n log n+o(n log n)), kappa_rho=min(3rho log 2,1+rho log 2).

NEW QUALITATIVE SEPARATION. Exact integration of the rational Laurent polynomial gives

    J_n(m)=R_complex+(U/2^n)Log(1+i), R_complex in Q(i),
    Im J_n(m)=r+U*pi/2^(n+2), r in Q.

Since eligible U!=0, irrationality of pi excludes exact eligible integer crossings. It does not exclude exponentially close crossings.

QUANTITATIVE ARITHMETIC GAP. Put T=n log n and a_rho=rho log 2. A hypothetical bound |pi-p/q|>=C q^(-mu), combined with an actual logarithmic denominator rate log den(beta)<=bT+o(T), would suffice only if mu b<min(2a_rho,1). The current denominator upper bound gives b=8a_rho, which does not meet that budget. No unexamined numerical irrationality exponent is invoked.

ADJACENT SELECTORS. Every rational combination has primitive integer coefficients a,b and selector L_m(a+bL_1)/c, where c=gcd(a+b,4). If h=max(|a|,|b|), its primitive polynomial coefficient height satisfies

    log H_sel=2m log 7+log h-log c+O(log(m+1)).

The complete forcing and companion numerators combine linearly. Forcing is aU_0+bU_1!=0; opposite coefficient parity guarantees this. The only forbidden primitive direction is explicitly (U_1/g_U,-U_0/g_U), up to sign.

The complete rational endpoint determinant Delta=U_0Z_1-U_1Z_0 is nonzero by different dyadic valuations. With D=n!(n+4m+4)! O_(2n+4m+4), A_j=D Z_j, and

    g=gcd(aA_0+bA_1,D(aU_0+bU_1)),

one has exactly

    q=D|aU_0+bU_1|/g,
    q|c-S|=D|aR_0+bR_1|/g,
    g divides |D^2 Delta|.

The individual dyadic denominator floor survives except when a is odd and v2(b)=v2(n+4m+4)-1. That exception requires an explicit high-order congruence calculation with the same coefficients used for real cancellation.

COST AND OBSTRUCTION. Let G=exp(a_rho T+o(T)) measure the full logarithmic amplitude, E_*=exp(-T+o(T)) bound the full exponential numerator, and eta=|aU_0+bU_1|/(h(|U_0|+|U_1|)). If q<=exp(d_q T), eta>=exp(-ell T), and normalized logarithmic cancellation is at most exp(-tT), sufficient conditions are

    t>d_q+ell+a_rho, d_q+ell<1,

with strict margins absorbing o(T). Outside the dyadic tie, bounded primitive forms necessarily require cancellation at least exp(-kappa_rho T+o(T)).

Using generic rational cancellation and no favorable gcd, the available full bound is D[G/Q+(Q+1)E_*]. Its minimum majorant is at least 2D sqrt(G E_*), which diverges because log D~4rho n(log n)^2. This rejects that certificate, not the actual family.

Full-residual Dirichlet cancellation does give forms of magnitude below any prescribed epsilon with nonzero forcing, at coefficient cost log h<=log D+log G+log(1/epsilon)+O(1). These forms may be zero. The exact full cancellation slope is a nonconstant rational fractional-linear transform of S=e+pi, and is rational exactly when S is rational. The two-selector family parametrizes every rational center, so this generic construction provides no new nonvanishing theorem or irrationality result.

The remaining task is therefore precise: stronger arithmetic separation for the pi endpoint forms, or coefficients with certified COMPLETE cancellation, useful actual denominator reduction, and a proved nonzero primitive form. Cancelling only a leading saddle term supplies none of those obligations.
