> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Limited review of the direct-selector height obstruction

Verdict: PASS WITH AN EXPLICIT HYPOTHESIS QUALIFICATION. The integer selector normalization, rational logarithmic component, elementary e-approximation input, general denominator inequality, eventual scalar divergence, and rational-correction inequality are valid. The asymptotic correction conclusions (16)–(17) must explicitly retain d_n=o(n log n), in addition to their stated height assumptions. Without that degree hypothesis the O(n+d) term cannot be discarded.

Scope is limited to the new claims in ../DIRECT_SELECTOR_HEIGHT_OBSTRUCTION_DRAFT.md and the dependency arguments needed for them. The inspected dependencies were ../EXPONENTIAL_COMPANION_HEIGHT_TRADEOFF.md, for its elementary integral bound and rational reference denominator, and ../SCALAR_FORCING_CENTER_DRAFT.md, for the scalar complete-error identity. The old normality, inverse, quotient, and coordinate reviews remain closed. No old computation, prime table, or numerical check was repeated. The scalar source's 5-adic section is unnecessary to this verdict and is not reviewed here.

The logarithmic saddle corollary remains conditional on Agent 2's stated author asymptotic. This document does not independently review that saddle proof. Likewise, the separate positive-selector arc expansion in Section 6 is outside this examination; its application of the height obstruction is valid conditional on the quoted uniform complete-error statement.

## Integer normalization and the complete logarithmic component

Let n>=1 and L(t)=sum_(i=0)^d a_i t^i be a nonzero primitive integer polynomial, H=sum |a_i|. Put V(t)=t^2-t+1/2 and

    K(t)=2^n t^n D_t^n[V(t)^n L(t)]/n!,
    U=K(1), A=|U|, N=2n+d.

The polynomial 2^n V^n L is integral. Acting on a monomial, D^n/n! multiplies its coefficient by an integer binomial coefficient. Thus K is integral and has degree at most N. The nonzero-forcing hypothesis is exactly U!=0, so A is a positive integer.

Write q_s=[z^s]Q0(z)^n. For a monomial selector t^i, both the forcing coefficient and D_t^n[V^n t^i] at t=1 are the sum of

    q_s (2n+i-s)!/(n+i-s)!

over s with n+i-s>=0. Terms differentiated below order n are zero. Linearity therefore proves, with its exact scale,

    F_L=sum_i a_i fP_i=(n!/2^n)U.

For the logarithmic residual the same coefficient calculation inside the full moment integral gives

    sum_i a_i eF_i=-(n!/2^n)calL(K/(1-t)).

Since calL(1/(1-t))=pi, division by F_L yields

    beta=pi-calL(K/(1-t))/U
        =calL((K-U)/(t-1))/U.

The sign is correct. The divided difference is an integer polynomial of degree at most N-1. This establishes rationality of beta without dropping either conjugate endpoint or truncating a complete residual.

The moment formula obtained by integrating t=(1+iu)/2 shows that den(calL(t^j)) divides 2^j(j+1). Consequently

    D_N=2^(N-1)lcm(1,...,N)

clears the divided-difference moment, and den(beta) divides A D_N. The weaker size inequality in the draft is therefore valid. The elementary bound lcm(1,...,N)<=16^N gives log D_N=O(n+d). Minimality of D_N is neither used nor claimed.

## Exponential estimate and forcing height

The saved complete exponential coefficient estimate gives

    |sum_i a_i eE_i|<=27 M^n H/(n+1), M=1+sqrt(2),

because (sqrt(2))^(-i)<=1. After division by the actual forcing,

    |e-alpha|<=27(2M)^n H/[(n+1)n! A].

Alpha is rational. Its error is strictly positive by the elementary lower bound proved below; no assumption about irrationality of e+pi is involved.

The positive binomial expression for fP_i shows 0<fP_0<=fP_i<=2^i fP_0: the ratio of consecutive binomial factors is (2n+i-2l)/(n+i), which lies between one and two in the contributing range. With the retained reference estimate fP_0<=2n!M^n/sqrt(n), this proves

    A<=2^(n+d+1) H M^n/sqrt(n).

There is no positivity inference for a signed contraction F_L. Only its absolute value is bounded. The reference upper estimate can also be obtained from the established integral representation of binom(2n,n)p_n(1) and the scalar circle bound |1+sqrt(2)cos u|<=M exp(-u^2/16); integration gives a constant smaller than two. No new asymptotic estimate for an inverse is needed.

## Elementary rational-approximation bound for e

For m>=1 put D_m=(2m+1)!/m! and f_m(x)=x^m(1-x)^m/m!. Its integral satisfies

    1/D_m<I_m:=integral_0^1 e^x f_m(x) dx<3/D_m.

Repeated integration by parts gives I_m=e a_m-b_m, with a_m,b_m integers. The nonzero endpoint derivatives have absolute values binom(m,l)(m+l)!/m!, so

    |a_m|<=2^m D_m/(2m+1).

For an integer denominator v>=1 choose m minimally with D_m>=6v. Then D_m<12v(2m+1), vI_m<1/2, and a_m!=0: otherwise I_m would be a positive integer less than 1/2.

For a rational u/v, the integer T=a_m u-b_m v satisfies

    vI_m=a_m v(e-u/v)+T.

If T!=0, the distance from vI_m to T is greater than 1/2, giving a stronger lower bound than the one below. If T=0, division by a_m and the two bounds for D_m give

    |e-u/v|>1/[144*2^m*(2m+1)*v^2].

Replacing v by any real upper bound V>=v is permitted: m(v)<=m(V), and every displayed denominator factor is increasing. This proves the explicit uniform inequality used by the draft.

Minimality gives D_(m-1)<6V, while D_(m-1)=m(m+1)...(2m-1)>=m^m. Hence m log m<log(6V), and 2^m(2m+1)=V^o(1). Thus for every epsilon>0 there is C_epsilon>0 with

    |e-u/v|>=C_epsilon v^(-2-epsilon)

for all rational u/v, v>=1. The bounded-denominator remainder is covered by a positive constant. The proof establishes this input directly; it is not a citation or numerical assumption.

## Reduced-denominator obstruction

Let q=den(c(L)). Since alpha=c(L)-beta, its reduced denominator is at most q A D_N. Combining the preceding lower and upper bounds gives

    q^(2+epsilon)>=C_epsilon (n+1)n! /
       [27(2M)^n H A^(1+epsilon)D_N^(2+epsilon)].

All cancellations in c(L) are allowed before q is defined. Rearrangement gives precisely

    (2+epsilon)log q>=log(n!)-log H
       -(1+epsilon)log A-O_epsilon(n+d).

For a sequence with d=o(n log n), finite h=limsup log H/(n log n), and finite a=limsup log A/(n log n), taking a lower limit and then epsilon down to zero proves

    liminf log q/(n log n)>=max(0,(1-h-a)/2).

The forcing height estimate implies a<=h, yielding max(0,1/2-h). In particular d+log H=o(n log n) forces the lower bound 1/2. This is a denominator lower bound; an exponential error upper envelope alone cannot convert it into divergence of actual primitive forms.

If the complete error is eventually nonzero and its logarithm is bounded below by -O(n), the same lower bound with h<1/2 does imply q|c-S| tends to infinity. That extra complete-error hypothesis is essential. Conversely log q=O(n), together with the degree hypothesis and bounded factorial-scale heights, forces the combined height budget stated in (11).

## Scalar all-index divergence

For L=1 the Rodrigues identity gives fP_0=n!binom(2n,n)A_n>0. The complete logarithmic residual is

    eF_0=-n!binom(2n,n)v_n.

Indeed the coefficient identity first produces t^n p_n inside the moment. The difference (t^n-1)/(1-t) has degree n-1, so orthogonality removes it. Therefore

    c_n-S=eE_0/fP_0-v_n/A_n,
    beta_n=pi-v_n/A_n.

The retained reference estimates give sign(v_n)=(-1)^n and

    2exp(-s)s^n<=|v_n|/A_n<=8s^n/(1-s)^2,
    s=M^(-2).

The lower forcing estimate fP_0>=n!M^(n-1)/sqrt(n) follows from the retained endpoint lower bound A_n>=(1-s)(M/4)^n and binom(2n,n)>=4^n/(2sqrt(n)), using (1-s)/2=1/M. Thus

    |e-alpha_n|=|eE_0/fP_0|<81/(sqrt(n)n!).

The reference rational companion has denominator at most 160^n. This follows using the integer transformed Legendre polynomial, its positive endpoint P_n<=5^n, the divided-difference moment clearer 2^(n-1)lcm(1,...,n), and the lcm estimate above. This is an upper bound for that companion denominator, not an identification with q_n.

Set V=q_n160^n. If q_n<n! and n>=160, then

    (4n+1)!/(2n)!>=n^(2n+1)>6*160^n n!>6V.

The middle strict inequality follows from n!<=n^n and n>=160. Hence m(V)<=2n. Comparing the explicit e lower bound with the exponential upper bound gives

    q_n^2>n!/[58320*102400^n*sqrt(n)],
    q_n>sqrt(n!)/(256*320^n*n^(1/4)).

The constants use 4n+1<=5n and sqrt(58320)<256. If q_n>=n!, the latter weaker inequality is immediate. Thus this denominator inequality holds for every n>=160.

The exponential error is o(s^n). Consequently, eventually at every integer index,

    sign(c_n-S)=(-1)^(n+1),
    |c_n-S|>=exp(-s)s^n.

Multiplying by the explicit denominator lower bound proves q_n|c_n-S| tends to infinity. The error comparison has an eventual threshold, which is not asserted to be 160. This is an exclusion of shrinking scalar primitive forms along every unbounded index sequence in this scalar family. It is not an exclusion of reconstructed coordinate centers or of other selectors.

## Rational corrections and conditional corollaries

For c=r+alpha+beta with v_r=den(r), one has

    den(alpha)<=q v_r A D_N.

Exactly the same argument gives

    (2+epsilon)(log q+log v_r)
      >=log(n!)-log H-(1+epsilon)log A-O_epsilon(n+d).

This all-size inequality needs no asymptotic degree assumption. Its asymptotic consequences do: (16) and (17) must retain d=o(n log n). Under that hypothesis, with the finite limsup height bounds in the draft, the reduced-q lower bound is max(0,(1-h-a)/2-v). If log q=O(n) and log H, log A, log v_r are O(n log n), taking epsilon down to zero proves

    liminf [log H+log A+2log v_r]/(n log n)>=1.

The stated bounded-height assumptions justify passing epsilon to zero in this last inequality. The numerator height of r is not required for this denominator argument. Its actual positive reduced denominator must be retained.

For reconstructed B coordinates, the correction is delta_(j,0)/Psi_(j,1), and it vanishes for j>0. Applying this obstruction still requires the primitive integral normalization and height of the actual selector row; it does not authorize identifying an adjugate row clearer with that height.

Conditional on Agent 2's author theorem for L_m=(2t^2-4t+1)^(2m), 0<=m<=log n, its forcing is nonzero and its signed complete asymptotic has logarithm -2n log M+O(log n). Its degree is 4m and coefficient l1 height is 7^(2m). The latter follows because its coefficients alternate and substitution t=-1 turns their absolute sum into 7^(2m). Thus the proved height obstruction yields the stated divergence conditional on that asymptotic. The textual Gamma lower-bound repair belongs to the cited author theorem and is not independently reaudited here.

No conclusion concerning the rationality or irrationality of e+pi follows. The obstruction rules out the specified low-height direct-selector route only when its additional complete-error lower information is available. It leaves high-height selectors, eligible reconstructed coordinates, and possible factorially small complete errors outside such an exclusion.
