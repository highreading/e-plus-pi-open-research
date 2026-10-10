> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual B-Gram adjoint: positive-moment reduction

Original author research, not independently audited. No numerical scan or old-check replay. SCALAR_CENTER_CONTIGUOUS and all previous notes are preserved. This note uses the saved arbitrary-polynomial arc identity and its scalar mass estimate, not the sign or denominator of the full-coefficient center.

## 1. Actual construction and domain

Take even n>=2^96, b=floor(log n), m=floor((b-1)/2), d=b-1. Write r=sqrt(2), rho=1/r, chi=r-1, c=r/(2chi), z*=1-rho. The previously justified inequality n>=512(b+1)^4 log n ensures the retained provisional contact-normality domain. Put a0=n+m+1, w_j=(a0-b)!/(a0-j)!, W=diag(w_j^2), 0<=j<=b.

Let T_ij=[z^(n+i-j)]exp(z)(1-z+z^2/2)^n, and fP,fQ be the two actual forcing columns defined in the retained contact construction. Let J=(I+D)^(-n), Krec=ZJ, where Z multiplies by z-1. Define

    x=T^(-1)fP, u=Krec x, a=u^T W u,
    lambda=T^(-T)Krec^T W u/a,
    kappa=u^T W e0/a,
    tB=kappa+lambda^T fQ.

Then lambda^T fP=1. The endpoint term kappa is part of the actual Q-column e0+Krec T^(-1)fQ. No full-triple reconstruction metric occurs here.

There is an exact unnormalized adjoint polynomial that retains both inverse factors. Set

    Delta=det T, X=adj(T)fP,
    V=X^T Krec^T W Krec X>0,
    ell=adj(T)^T Krec^T W Krec X.

Then lambda=ell/V. Define P(z)=sum_i ell_i z^i and N_P=sum_i |ell_i|rho^i. Thus P is nonzero, and P/V=L_lambda. All these are rational construction data. No clearing-height or reduced-denominator bound is asserted.

## 2. Exact real polynomial on the arc

For z(theta)=1-rho exp(i theta), define

    a_k=(-rho)^k sum_(i=k)^d binom(i,k)ell_i,
    C(x)=sum_(k=0)^d a_k T_k(1-x),

where T_k is the Chebyshev polynomial specified by T_0=1, T_1=y, T_(k+1)=2yT_k-T_(k-1). Then exactly

    Re P(z(theta))=C(1-cos theta).

Write C(x)=sum_(j=0)^d C_j x^j. Its explicit coefficients are

    C_0=P(z*),
    C_j=(-1)^j sum_(k=j)^d
          a_k 2^j k(k+j-1)!/((k-j)!(2j)!), j>=1.

This follows by differentiating T_k at 1, or by its displayed recurrence. It is an invertible triangular transformation from the coefficients ell to C: first expanding P(1-rho y), then changing from powers/cosines to Chebyshev polynomials, and finally substituting 1-x are all invertible. Consequently not all C_j vanish.

In particular the first local correction is

    C_1=rho P'(z*)-rho^2 P''(z*).

Indeed z(theta)-z*=rho(1-cos theta)-i rho sin theta, whose squared real part begins -2rho^2 x. This correction can be nonzero even when the saddle value vanishes. All C_j lie in Q(sqrt(2)) and are explicit linear contractions of ell. No coefficient is defined using e+pi.

## 3. Positive moments and explicit bounds

Put h(theta)=r cos theta-1 and

    J_n=integral_(-pi/4)^(pi/4) h(theta)^n dtheta,
    mu_j=J_n^(-1) integral h(theta)^n(1-cos theta)^j dtheta.

Then mu_0=1 and every mu_j>0. Equivalently, changing variable x=1-cos theta gives

    J_n mu_j=2 integral_0^(z*)
        (chi-r x)^n x^j /sqrt(2x-x^2) dx.

This exact positive measure is independent of the adjoint. Its positivity is not a Toeplitz entrywise-sign assertion.

The retained scalar arc bound is

    J_n>=chi^n sqrt(pi/(cn))(1-10/n).

Also h(theta)^n<=chi^n exp(-n theta^2) and 1-cos theta<=theta^2/2. Therefore, for n>=16 and j>=1,

    mu_j <= U_j(n)
      =sqrt(c) Gamma(j+1/2)
         /[sqrt(pi)(1-10/n) 2^j n^j].

The bound is valid for every j, including growing j: extend the nonnegative Gaussian integral to the real line. No fixed-degree asymptotic is used.

A useful explicit lower bound is

    mu_j >= L_j(n)
      =2(sqrt(2)-1) exp(-8)/sqrt(pi) * (3n)^(-j), j>=1.

Proof: restrict both halves of the arc to 1/sqrt(n)<=|theta|<=sqrt(2/n). There x>=theta^2/3>=1/(3n), while h/chi>=1-c theta^2>=1-4/n. For n>=16, (1-4/n)^n>=exp(-8). The two intervals have total length 2(sqrt(2)-1)/sqrt(n), and J_n<=chi^n sqrt(pi/n). These give the assertion. For j=0 use the exact value 1 instead of these bounds.

Thus the complete logarithmic contribution, for even n, is exactly

    epsilon_F=-(2n! J_n/V) sum_(j=0)^d C_j mu_j.       (1)

This is a finite positive-moment representation with an explicit signed coefficient vector.

## 4. Retaining the other two contributions

The complete error is

    tB-(e+pi)=kappa+epsilon_E+epsilon_F.

The saved exponential coefficient estimate, applied to P/V, gives

    |epsilon_E| <= 9 N_P M^n/[V(n+1)], M=1+sqrt(2).

In particular define the explicit budget

    B_n=[V|kappa|+9N_P M^n/(n+1)]/(2n! J_n).

No projection estimate is needed to retain kappa: it is computed from the actual B metric. For a budget containing no unevaluated integral use

    Bhat_n=[V|kappa|+9N_P M^n/(n+1)]
       /[2n! chi^n sqrt(pi/(cn))(1-10/n)].

Then B_n<=Bhat_n, and (1) implies

    | -V(tB-e-pi)/(2n!J_n)-sum C_j mu_j |<=Bhat_n.   (2)

This establishes a complete-error comparison before making any sign inference.

## 5. Quantitative algebraic gates

The simplest improved saddle gate is

    |C_0| > sum_(j=1)^d |C_j| U_j(n)+Bhat_n.         (3)

It proves a nonzero complete error with sign opposite C_0. It replaces the global O(d^2 N_P/n) remainder by explicit local contractions, with the j-th term suppressed by n^(-j). It does not assume these contractions are small.

More generally, choose a sign sigma in {+1,-1}. Define bounds L_0=U_0=1 and

    G_sigma=sum_(sigma C_j>0) |C_j| L_j
                  -sum_(sigma C_j<0) |C_j| U_j.

If

    G_sigma>Bhat_n,                                  (4)

then the complete error is nonzero, has sign -sigma, and

    |tB-e-pi| >= (2n!J_n/V)(G_sigma-Bhat_n).

Proof: positivity of every moment bounds sigma sum C_j mu_j below by G_sigma; apply (2). This is a concrete finite system of algebraic signs and weighted inequalities on the actual adjugate contractions, together with an explicit elementary analytic budget.

A particularly direct structural target is a common sign for C_0,...,C_d. If this holds, choose any nonzero C_k. The logarithmic contribution cannot vanish; the COMPLETE contribution is nonzero once |C_k|L_k>Bhat_n (using L_0=1). No derivative remainder or cancellation between polynomial terms remains in that case. Common sign has not been proved for the actual adjoint.

If C_0=...=C_(k-1)=0, another sufficient gate is

    |C_k|L_k > sum_(j=k+1)^d |C_j|U_j+Bhat_n.        (5)

This supplies a rigorous route past saddle vanishing, rather than declaring the leading coefficient nonzero without proof. Exact vanishing C_0=0 is still equivalent to divisibility of P by 2z^2-4z+1. But (4),(5) address the resulting higher terms and their quantitative scale. The first successor to test is rho P'(z*)-rho^2P''(z*).

The map ell -> (C_0,...,C_d), the positive moments, and all budgets are explicit. The remaining task is to prove one of these inequalities, or a suitable sign cone, for ell=adj(T)^T Krec^T W Krec adj(T)fP along the specified even indices.

## 6. Limits of positivity and current outcome

Even-index Toeplitz accretivity guarantees a positive real quadratic form in the correctly scaled variables. The present evaluation instead pairs different directions after two inverse factors and reconstruction. No entrywise positivity, positive C_j, or positive P(z*) follows from accretivity alone. The positive measure in Section 3 is an arc measure; its polynomial factor may change sign.

This note proves the exact coefficient transformation, moment bounds, and conditional complete-error lower bounds. It does not prove that the actual adjoint satisfies any gate on an unbounded set. Uniform signed nonvanishing of the B-only center remains open. The reduction is stronger than an unspecified leading coefficient: it identifies every algebraic coefficient, supplies explicit moment bounds, retains the endpoint/exponential budget, and offers a gate that remains meaningful if the saddle value is exactly zero.

No numerical evidence, denominator transfer, independent audit, or irrationality conclusion is asserted. The saved scalar recurrence remains untouched. Selector-height and reduced-coordinate arithmetic remain with their assigned agents.
