> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Direct forcing selectors: height, denominators, and scoped exclusions

Status: new main-agent author deductions, not independently reviewed. This note preserves the previously unsaved scalar and selector obstructions and extends the height budget to rational endpoint corrections. It does not establish irrationality or rationality of e+pi. Existing proofs and certificates remain unchanged.

## 1. Construction and exact normalization

Let n>=1. Write Q0(z)=1-z+z^2/2, V(t)=t^2-t+1/2, M=1+sqrt(2), and S=e+pi. For i>=0 define the rational forcing coordinates

    fP_i=[z^(n+i)]Q0(z)^n D_z^n(1/(1-z)),
    fQ_i=[z^(n+i)]Q0(z)^n D_z^n((exp(z)+F(z))/(1-z)),
    F(z)=4 arctan(z/(2-z)).

Split fQ=fExp+fLog. The complete analytical decomposition is

    fExp_i=e fP_i+eE_i,
    fLog_i=pi fP_i+eF_i.

Let L(t)=sum_(i=0)^d a_i t^i be a primitive integer polynomial, H=sum_i |a_i|>=1. Assume its actual forcing contraction F_L=sum_i a_i fP_i is nonzero. Define

    c(L)=sum_i a_i fQ_i/F_L=alpha+beta,
    alpha=sum_i a_i fExp_i/F_L,
    beta=sum_i a_i fLog_i/F_L.

All three quantities are rational. No coefficient-sign assumption is made, and no contact matrix or inverse is used.

Define the integer polynomial

    K(t)=2^n t^n D_t^n[V(t)^n L(t)]/n!,
    U=K(1), A=|U|>0, N=2n+d.

Indeed 2^n V^n L has integer coefficients, and D^n/n! multiplies each monomial coefficient by an integer binomial coefficient. Its degree after differentiation and multiplication by t^n is at most N.

Coefficient extraction gives exactly

    F_L=(n!/2^n)U.                                    (1)

For each monomial t^i, expand V^n=t^(2n)Q0(1/t) and differentiate: the summands on both sides of (1) are [z^s]Q0^n times (2n+i-s)!/(n+i-s)! whenever n+i-s>=0. This proves the identity for arbitrary L by linearity.

With the established moment functional calL(g)=integral_-1^1 g((1+iu)/2)du, the complete logarithmic identity similarly gives

    sum_i a_i eF_i=-(n!/2^n)calL(K(t)/(1-t)).

Since calL(1/(1-t))=pi,

    beta=calL((K(t)-U)/(t-1))/U.                      (2)

Both conjugate endpoints and the full logarithmic contribution remain in (2).

## 2. Complete exponential accuracy and logarithmic denominator

Cauchy's estimate for the complete exponential residual on |z|=sqrt(2) gives

    |eE_i|<=27 M^n (sqrt(2))^(-i)/(n+1).

Therefore (1) implies

    0<|e-alpha|<=27(2M)^n H/[(n+1)n! A].              (3)

The strict positivity follows because alpha is rational and e is irrational. The upper bound retains A; replacing it by one would lose useful normalization information.

The polynomial (K-U)/(t-1) is integral and has degree at most N-1. Each moment calL(t^j) has denominator dividing 2^j(j+1). Thus, with

    D_N=2^(N-1)lcm(1,...,N),

formula (2) proves

    den(beta)<=A D_N.                                (4)

The coarse bound lcm(1,...,N)<=16^N implies log D_N=O(n+d). No minimality of this moment clearer is asserted.

The positive forcing entries obey

    0<fP_0<=fP_i<=2^i fP_0,
    fP_0<=2n!M^n/sqrt(n).

These follow from the positive binomial formula for fP_i and the established endpoint bounds. They imply, even for sign-changing L,

    A<=2^(n+d+1) H M^n/sqrt(n).                       (5)

They are used here only for an absolute height bound, not to assert positivity of F_L.

## 3. Rational approximation input for e

The elementary integral proof saved in EXPONENTIAL_COMPANION_HEIGHT_TRADEOFF.md supplies, for every epsilon>0, a constant C_epsilon>0 such that every rational u/v, v>=1, satisfies

    |e-u/v|>=C_epsilon v^(-2-epsilon).                (6)

Its explicit version is

    |e-u/v|>1/[144*2^m*(2m+1)*v^2],
    m=min{j>=1:(2j+1)!/j!>=6v}.

The factor 2^m(2m+1)=v^o(1) proves (6), with a positive constant covering the remaining bounded denominators. This dependency is an elementary author proof, not an invented citation or numerical observation.

## 4. Actual reduced denominator bound

Let q be the positive reduced denominator of c(L). Because alpha=c(L)-beta, (4) bounds the reduced denominator of alpha by q A D_N. Combining (3) and (6) gives

    q^(2+epsilon)>=
      C_epsilon (n+1)n! /
      [27(2M)^n H A^(1+epsilon) D_N^(2+epsilon)].       (7)

Consequently

    (2+epsilon)log q>=log(n!)-log H
       -(1+epsilon)log A-O_epsilon(n+d).             (8)

The q in these formulas is the denominator after complete rational reduction. Neither U, a coefficient clearer, nor a polynomial lifting multiplier is substituted for it.

Suppose d_n=o(n log n) and the finite nonnegative quantities

    h=limsup log H_n/(n log n),
    a=limsup log A_n/(n log n)

exist as extended sequence bounds with finite values. Taking a lower limit in (8), then epsilon decreasing to zero, proves

    liminf log q_n/(n log n)>=max(0,(1-h-a)/2).        (9)

Equation (5) implies a<=h under the stated degree condition. Hence

    liminf log q_n/(n log n)>=max(0,1/2-h).           (10)

In particular, degree plus logarithmic height o(n log n) forces the lower bound 1/2. Coefficient positivity is unnecessary.

If h<1/2 and the complete error is eventually nonzero with log|c_n-S|>=-O(n), then q_n|c_n-S| tends to infinity. This is a scoped exclusion of those particular primitive forms. It does not exclude a selector with a factorially small complete error.

Conversely, if log q_n=O(n), d_n=o(n log n), and log H_n,log A_n=O(n log n), equation (8) forces

    liminf [log H_n+log A_n]/(n log n)>=1.            (11)

This is a necessary combined arithmetic-height budget, not a sufficient construction.

## 5. Explicit scalar exclusion

For L=1, the saved SCALAR_FORCING_CENTER_DRAFT.md gives

    c_n=fQ_0/fP_0,
    c_n-S=eE_0/fP_0-v_n/p_n(1),
    log|c_n-S|=-2n log M+O(1),

with eventual sign (-1)^(n+1). Its rational pi companion has denominator at most 160^n, and its exponential companion satisfies

    |e-alpha_n|<81/(sqrt(n)n!).

For completeness an explicit denominator bound follows from the explicit version of (6). Put V=q_n160^n. If q_n<n! and n>=160, then m(V)<=2n, because

    (4n+1)!/(2n)!>=n^(2n+1)>6*160^n n!>6V.

Comparison of the exponential error bounds gives

    q_n^2>n!/[58320*102400^n*sqrt(n)],

and hence

    q_n>sqrt(n!)/(256*320^n*n^(1/4)).                 (12)

If q_n>=n!, the weaker inequality (12) holds immediately. Thus (12) holds for n>=160.

The accepted reference bounds and the complete scalar identity imply, eventually,

    |c_n-S|>=exp(-s)s^n, s=M^(-2).

Therefore

    q_n|c_n-S|>=
      exp(-s)s^n sqrt(n!)/(256*320^n*n^(1/4)) -> infinity. (13)

This is an all-index author exclusion of the scalar primitive forms. It supersedes the former search for a favorable upper denominator bound for this scalar construction. It does not change earlier local valuation results, which remain valid in their own scopes.

## 6. Positive selectors and the logarithmic saddle selector

For nonnegative integer coefficients, degree at most floor(log n), and log H=o(n log n), the saved logarithmic arc expansion shows eventual common sign of all eF_i in the window. In detail, put a0=1-1/sqrt(2). The relative error in the leading coordinate approximation is at most

    (sqrt(pi)/2) i^2 M^i/n,

which tends uniformly to zero for i<=floor(log n), since log M<1. Positive weighted averaging with the positive fP_i then gives

    log|c_n(L_n)-S|=-2n log M+O(log n)

and eventual sign (-1)^(n+1), after retaining the factorially smaller exponential contribution. Equations (9)-(10) exclude shrinking primitive forms for these selectors.

This includes the positive forcing-column Gram center sum_i 2^i fP_i fQ_i / sum_i 2^i fP_i^2 in a logarithmic window. Multiplying its selector coefficients by 2^n/n! makes them positive integers of height exp(O(n)); dividing out coefficient content can only improve that height bound. It is distinct from reconstructed coefficient Gram centers.

For the sign-changing selector

    L_m(t)=(2t^2-4t+1)^(2m), 0<=m<=log n,

its degree is 4m and its coefficient l1 height is exactly 7^(2m). Agent 2's RATIONAL_SADDLE_SELECTOR.md reports an author theorem proving nonzero forcing denominator and

    c_n(L_m)-S=(-1)^(n+1)4pi s^(n+m+1/2)(1+o(1))

uniformly in this range. Its reported textual Gamma correction is retained: Gamma(m+1/2)>=sqrt(pi)/2, not necessarily one.

Conditional on that stated saddle theorem, the complete error has logarithm -2n log M+O(log n). Equation (9) forces

    log(q_n|c_n(L_m)-S|)
       >=(1/2-o(1))n log n-2n log M-O(log n) -> infinity. (14)

The saddle-zero polynomial improvement survives analytically but cannot defeat this denominator growth. This does not exclude higher-degree selectors outside the stated height/degree regime.

## 7. New extension: rational endpoint corrections

Reconstructed centers can contain a rational endpoint correction. Suppose the actual center is

    c=r+alpha+beta,

where alpha,beta are the direct-selector components above and r is rational with positive reduced denominator v_r. Let q=den(c). Then den(alpha)<=q v_r A D_N. Repeating the same proof yields

    (2+epsilon)(log q+log v_r)
      >=log(n!)-log H-(1+epsilon)log A-O_epsilon(n+d). (15)

Thus the rational correction must be counted in the arithmetic budget. If log v_r/(n log n) has finite upper limit v, equation (9) becomes

    liminf log q/(n log n)>=max(0,(1-h-a)/2-v).        (16)

When log q=O(n) and all three logarithmic heights are O(n log n), a necessary condition is

    liminf [log H+log A+2log v_r]/(n log n)>=1.        (17)

A large correction denominator can therefore prevent an unjustified extension of the direct-selector no-go theorem to reconstructed centers. This is an exact dependency, not evidence that such a correction supplies useful approximants.

For the actual B reconstruction Psi, write

    u=Krec T^(-1)fP,
    v=e0+Krec T^(-1)fQ.

A coordinate center with u_j!=0 is

    v_j/u_j=delta_(j,0)/u_j+
       [e_j^T Krec T^(-1)fQ]/[e_j^T Krec T^(-1)fP].

The row e_j^T Krec T^(-1) is a rational selector that can be made primitive integral; the correction vanishes for j>0. Similarly the B-only Gram center has rational selector proportional to T^(-T)Krec^T W u and rational correction u^T W e0/(u^T W u). Formula (15) applies only after deriving the actual selector height, forcing normalization, and correction denominator for these rows.

## 8. Remaining research

The obstruction concentrates the unresolved bridge in actual selector height, its forcing normalization, any rational correction, and complete cancellation. It does not classify arbitrary high-height selectors or reconstructed centers. Larger-degree families must derive new denominator and complete-error estimates, rather than assume the logarithmic-degree asymptotics persist.

This note is an author proof awaiting the one narrowly necessary examination assigned to Child 4. It saves the previously unsaved branch exclusions and the new correction-denominator extension. No old numerical check is repeated and no unconditional conclusion about e+pi is claimed.
