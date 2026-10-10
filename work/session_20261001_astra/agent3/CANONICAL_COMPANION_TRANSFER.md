> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Canonical B-only center and direct-selector companion transfer

Original author synthesis, not an independent review. Work is offline. The two main transfer drafts and the necessary reconstruction/height passages of agent1/RECONSTRUCTED_SELECTOR_HEIGHT.md supply the stated inputs. The completed CANONICAL_ADJOINT_DERIVATIVE files and their calculations are retained without replay. The finite irrationality-measure source for pi remains an explicit main-agent dependency.

The exact canonical center belongs to the direct-selector construction with rational correction r=kappa. Its canonical energy gives a stronger exponential-error budget than a crude selector-height ceiling. A sufficiently small combined companion denominator is not established; its precise integer gcd and required threshold are identified below.

## 1. Domain, metric, and fraction-free data

Use the actual contact matrix T, reconstruction Krec=Z(I+D)^(-n), and two forcing columns fP,fQ. Here Z multiplies a coefficient polynomial by t-1. Assume T is nonsingular. For the factorial B-only metric take

    b>=3, 1<=m<=floor((b-1)/2), ell=n+m+1,
    omega_j=(ell)_j, Omega=diag(omega_j^2), 0<=j<=b,
    tau=(ell-b)!/ell!, W=tau^2 Omega.

The falling factorial (ell)_0 is one. Thus omega_0=1. These are the actual B-only weights; no full-coefficient metric is used.

For the analytic estimates below restrict further to even n in the retained slow-growth range

    n>=16, 3<=b<=n, n>=512 b^4 log n.

This includes every fixed b>=3 and allowed fixed m at all sufficiently large even n. It also includes the explicitly retained allocation

    even n>=2^96,
    b=floor(log n), m=floor((b-1)/2).

Normality and the quantitative inverse are used in their retained author scope, without a new independent acceptance claim.

Use the integral row normalization from the selector-height note:

    c0=2^n n!, d_i=(n+i)!/n!, D0=diag(d_i),
    M=c0 D0 T, Delta=det M!=0,
    J=(2^n/n!)fP in Z^b,
    C=Krec adj(M)D0,
    x=CJ,
    Dg=x^T Omega x>0,
    z=C^T Omega x,
    g=gcd_i |z_i|, S_z=sum_i |z_i|.

M,C,x,z are integral. The letter Dg denotes a scalar Gram contraction, not differentiation. In particular

    z^T J=Dg>0,
    u=Krec T^(-1)fP=((n!)^2/Delta)x,
    v=e0+Krec T^(-1)fQ.

The vector z is nonzero. These exact identities, rather than an unreduced coefficient clearer, determine the canonical selector.

## 2. Primitive selector and direct forcing normalization

Define

    G(t)=sum_i (z_i/g)t^i,
    d=deg G<=b-1,
    H=sum_i |[t^i]G|=S_z/g.

This is primitive in Z[t]. Its sign is fixed by z, so its forcing is positive. The direct-selector convention is

    V(t)=t^2-t+1/2,
    K_G(t)=(2^n/n!) t^n D_t^n(V(t)^n G(t)),
    U=K_G(1), A=|U|.

Because 2^n V^n=(2t^2-2t+1)^n and D^n/n! preserves integrality, K_G belongs to Z[t]. The retained forcing identity gives

    U=(2^n/n!) coeff(G)^T fP
      =coeff(G)^T J=Dg/g>0.

Consequently the EXACT direct normalization is

    A=Dg/g,
    F_n(G)=coeff(G)^T fP=(n!/2^n)A,
    eta=1/F_n(G)=2^n/(n! A).

In particular g divides Dg. The factor n!/2^n separates the forcing normalization of the canonical derivative note from A in the direct-selector drafts; they must not be identified.

The normalized actual adjoint is exactly

    lambda=(2^n/n!) z/Dg=eta coeff(G),
    lambda^T fP=1.

For example, this follows by dividing the selector-height note's identity

    T^(-T)Krec^T W u
       =[c0(n!)^2 tau^2/Delta^2]z

by

    a=u^T W u=[(n!)^4 tau^2/Delta^2]Dg.

Only common scalars have canceled. No assertion about factorial content inside z is used.

## 3. Both rational companions and the endpoint correction

Write calL(P)=integral_{-1}^1 P((1+iu)/2)du. The direct logarithmic companion is

    beta=calL((K_G-A)/(t-1))/A.

To specify the exponential companion finitely, set

    P_G(s)=sum_i [t^i]G [z^(n+i)]Q0(z)^n exp(sz)
          =sum_l p_l s^l,
    Q0(z)=1-z+z^2/2,
    e_j=sum_(k=0)^j 1/k!.

Then

    sum_l p_l(n+l)!=F_n(G),
    alpha=eta sum_l p_l(n+l)! e_(n+l).

All sums are finite, with l<=n+d. This defines alpha rationally without using the unknown e+pi. The exact retained exponential integral gives epsilon_E=alpha-e.

The normalized polynomial appearing in the logarithmic residual is

    t^n D^n(V^n L_lambda)=K_G/A.

Thus its complete logarithmic residual is epsilon_F=beta-pi, including both conjugate endpoints. There is no additional rational term hidden in beta.

The actual endpoint constant is

    r=kappa=(u^T W e0)/(u^T W u)
           =Delta x_0/[(n!)^2 Dg].                 (1)

Here omega_0=1 is essential to the last expression. Therefore

    tB=kappa+lambda^T fQ=alpha+beta+r,
    gamma=r+beta,
    tB-(e+pi)=(alpha-e)+(gamma-pi).                 (2)

The correction r has not been absorbed into alpha. Its denominator cost belongs to gamma. These are the precise companions to which the main transfer inequalities apply.

## 4. Actual reduced denominator of gamma

Put

    F2=(n!)^2,
    N=2n+d,
    L_N=2^(N-1) lcm(1,...,N).

L_N is the moment clearer used in the direct-selector draft. Define the integer

    T_G=L_N calL((K_G-A)/(t-1)).

Then beta=T_G/(L_N A). For an expression entirely in the unprimitive integer data, set

    G_z(t)=sum_i z_i t^i=gG(t),
    K_z=(2^n/n!)t^n D^n(V^n G_z)=gK_G,
    T_z=L_N calL((K_z-Dg)/(t-1))=g T_G.

In particular T_z is an integer and its displayed factor g is genuine.

Define

    Rnum=Delta x_0,
    h_r=gcd(F2 Dg,|Rnum|),
    v_r=den(r)=F2 Dg/h_r,                           (3)

and

    Xi=L_N Delta x_0+F2 T_z,
    Ltot=F2 L_N Dg,
    h_gamma=gcd(Ltot,|Xi|).

The ACTUAL positive reduced denominator requested in the task is

    B=den(gamma)=Ltot/h_gamma.                      (4)

These formulas use gcd(a,0)=a. Thus x_0=0 gives r=0 and v_r=1; Xi=0 gives gamma=0 and B=1. No nonzero correction numerator is presumed.

The separate reduced denominator of beta is

    B_beta=L_N A/gcd(L_N A,|T_G|).

Hence B divides lcm(v_r,B_beta), and in particular

    log B<=log v_r+log A+log L_N.                   (5)

The joint gcd in (4) can improve this bound. It cannot be replaced by either separate gcd, nor by selector content g. The two terms of Xi can cancel modulo primes even when their separate reduced denominators are large.

One further common factor can be removed with a proved reason. Let rho=gcd(x)>0, write x=rho x*, and define

    z*=C^T Omega x*, g*=gcd(z*), D*=x*^T Omega x*.

Then z=rho z*, g=rho g*, Dg=rho^2 D*, and T_z=rho T_* with integral T_*. Formula (4) becomes

    B=F2 L_N rho D*/
       gcd(F2 L_N rho D*,|L_N Delta x*_0+F2 T_*|).  (6)

This removes the common response content rho from numerator and denominator once. No coprimality or additional cancellation involving rho and g* is assumed. The separate identities are

    H=||z*||_1/g*, A=rho D*/g*,
    r=Delta x*_0/(F2 rho D*).

## 5. A sharper canonical exponential budget

The direct-selector bound in the main exclusion draft is

    |alpha-e|<=E,
    E=27(2M0)^n H/[(n+1)n! A],
    M0=1+sqrt(2).                                  (7)

In the present canonical setting the coefficient gcd cancels exactly from this numerical bound:

    H/A=S_z/Dg,
    E=27(2M0)^n S_z/[(n+1)n! Dg].                 (8)

A small H by itself is therefore not needed to control E. What matters here is the canonical ratio H/A.

Reuse the retained canonical energy estimates before deflation. Let

    Hplus=(n+1)^(b-1), Hminus=(n+b)^(b-1),
    K0=2048 b sqrt(n)(16b^2 n)^(b-1)
                       binom(2b-2,b-1)/((b-1)!)^2,
    Ccan=18b Hplus Hminus K0 2^(b-1)/wmin,
    f0=(fP)_0.

The retained SPD equation and norm estimates give

    ||lambda||_2<=sqrt(||Cmetric^(-1)||_2/a)
                <=Ccan/f0,
    Cmetric=T(Krec^T W Krec)^(-1)T^T.              (9)

This is the existing canonical energy estimate, not an inference from an averaged sign and not a repeated calculation of its constants.

The retained forcing-circle identity supplies

    f0=n! Zplus,
    Zplus=(1/(2pi)) integral_(−pi)^pi
                         (1+sqrt(2)cos theta)^n dtheta.

For even n, the full weight is nonnegative. On |theta|<=1/sqrt(n), Bernoulli's inequality gives

    (1+sqrt(2)cos theta)^n>=M0^n/2.

Integrating just this interval proves the useful lower bound

    f0>=n! M0^n/(2pi sqrt(n)).                     (10)

Combining (9),(10) with ||lambda||_1=2^n H/(n! A) yields

    H/A<=2pi sqrt(bn) Ccan/(2M0)^n.                (11)

On the other hand the retained universal direct forcing bound gives

    A/H<=2^(d+1)(2M0)^n/sqrt(n).                   (12)

Thus the canonical ratio is bounded on both sides, without any primitive-content assumption. In particular

    27 sqrt(n)/[2^(d+1)(n+1)n!]
        <= E <=54pi sqrt(bn) Ccan/[(n+1)n!].       (13)

The inequalities concern the chosen positive bound E, not a lower bound on the actual exponential error.

Uniformly in the stated slow-growth domain,

    log Ccan=O(b log(n+b)),
    b log(n+b)=o(n log n).

This follows directly from the displayed finite expression and wmin^(-1)<=(2n)^b. Therefore, with X_n=n log n,

    (-log E)/X_n ->1.                              (14)

This holds for fixed b and for the logarithmic allocation, indeed throughout every unbounded even slow-growth sequence. It requires neither log H=o(X_n) nor a favorable selector gcd.

A second useful consequence of (11),(12) is

    log A-log H=n log(2M0)+O(b log(n+b)+log n).

In particular

    (log A-log H)/X_n ->0.                         (15)

Height and forcing normalization have the same factorial-scale logarithmic rate, even though neither individual rate is established.

## 6. Exact conditions for the general small-selector theorem

The degree condition d=o(X_n) already holds in the normality domain. The two remaining small-selector requirements are exactly

    log H=log S_z-log g=o(X_n),                    (16)
    log den(r)=log(F2 Dg)-log h_r=o(X_n).          (17)

By (15), condition (16) is equivalent to log A=o(X_n), or

    log Dg-log g=o(X_n).

These equations specify how much of the ACTUAL coefficient norm and correction denominator must cancel. They do not use a factorial clearer as a substitute for either reduced quantity.

If (16),(17) hold on an unbounded normal sequence, then (5), log L_N=O(n+d), and (15) give log B=o(X_n). Together with (14), the main transfer theorem then supplies its primitive-error divergence conclusion, conditional on the quantitative pi input.

No such unbounded sequence for the actual factorial Gram selector with b>=3 has been proved from the supplied inputs. This is a limitation of the available arithmetic estimates, not a claim that such a sequence cannot exist. Fixing b does not by itself prove (16) or (17). If x_0=0 happens on a proposed sequence, (17) holds automatically there, but no such infinite zero set is asserted.

## 7. The sharper combined-denominator threshold

The exact E rate (14) permits a more general application than the two separate small-selector conditions. Assume the main agent supplies a valid pi inequality with finite exponent mu and a uniform positive constant, and retain the e inequality with exponent nu=2+epsilon.

For this SAME canonical center and these SAME companions, the transfer draft gives, whenever E<=(C_pi/2)B^(-mu),

    den(tB)|tB-e-pi|
       >=(C_pi/2) C_e^(1/nu) E^(-1/nu)B^(-(mu+1)).

Consequently, if

    beta_rate=limsup log B/X_n
                   <1/[2(mu+1)],                 (18)

then the complete primitive errors diverge, and

    liminf log(den(tB)|tB-e-pi|)/X_n
                   >=1/2-(mu+1)beta_rate>0.        (19)

The strict inequality also guarantees exponential/logarithmic error separation. A weaker bound beta_rate<1/mu would suffice for eventual nonzero complete error by this method, without necessarily proving primitive-error divergence.

Substituting the ACTUAL denominator (4), the remaining condition is precisely

    limsup [log(F2 L_N Dg)-log h_gamma]/X_n
                   <1/[2(mu+1)].                 (20)

For example it suffices to prove, for some fixed delta>0, eventually

    log h_gamma>=log(F2 L_N Dg)
                  -(1/[2(mu+1)]-delta)X_n.        (21)

This is the quantitative joint-gcd threshold. Since log L_N=o(X_n), it can equivalently be written using 2log(n!)+log Dg in the rate expression. Formula (6) gives the corresponding threshold after response content has been removed explicitly.

There is no theorem here that this gcd is large enough. Conversely a failure to prove separate small H and small den(r) does not rule out (20), since the numerator Xi retains possible cancellation between r and beta.

## 8. Fixed b versus growing b: what the ceilings do and do not prove

The selector-height note gives cofactor and reconstruction ceilings which imply

    log S_z, log Dg
       <=2(b-1)log(n!)+O(nb+b^2 log(n+b)).          (22)

These are upper bounds on unprimitive integers. They do not state their actual asymptotic sizes or provide lower bounds for g, h_r, or h_gamma.

For fixed b>=3, the error term in (22) is o(X_n). Thus the available ceilings are

    log S_z, log Dg <=[2(b-1)+o(1)]X_n,
    log(F2 L_N Dg)<=[2b+o(1)]X_n.

They are far too large to establish (16),(17), or the threshold (20). A proved lower bound log g>=2(b-1)X_n-o(X_n) would be one sufficient way to make H subfactorial when combined with these ceilings; it is NOT established or necessary, since S_z itself might be smaller than its ceiling. The exact requirement remains (16). The same distinction applies to the correction and joint gcds.

For b=floor(log n), the leading ceiling in (22) has order n(log n)^2, while its O(nb) part already has order X_n. Thus even a claimed cancellation of the displayed 2(b-1)log(n!) term would not by itself prove an o(X_n) residual. Both the actual integer sizes and the precision of their gcd cancellation must be controlled at the X_n scale. At larger b in the slow domain the same need is stronger.

The small estimates log det(Krec^T Omega Krec)=O(b^2 log(n+b)) and log d_(b-1)=O(b log(n+b)) from the reconstruction note do not settle this issue. In its divisibility bound

    g divides d_(b-1) Delta rho det(Krec^T Omega Krec),

the determinant Delta and response content rho remain uncontrolled at the relevant scale. A bound on where content can occur is not a lower bound on how much content actually occurs.

No scalar b=1 result or coordinate-selector result is transferred to this factorial Gram family. The stipulated m-range starts at b=3.

## 9. Outcome and dependency ledger

The exact bridge is now explicit:

    G=z/g, H=||z||_1/g, A=Dg/g,
    lambda=(2^n/(n! A))coeff(G),
    r=kappa=Delta x_0/((n!)^2Dg),
    tB=alpha+(r+beta),
    den(r+beta)=F2 L_N Dg/
       gcd(F2 L_N Dg,|L_N Delta x_0+F2 T_z|).

The new analytic consequence is the canonical factorial error budget (-log E)/(n log n)->1 on genuinely unbounded even slow-growth normality regimes, without assuming favorable primitive selector content. The missing application input is an adequately small actual combined companion denominator, equivalently the quantitative gcd threshold (20). Neither the separate subfactorial conditions nor that sharper joint condition is proved here for an unbounded canonical family.

All complete-error assertions retain kappa and both companions. The finite-measure theorem for pi, including its source, exponent, and uniform quantifiers, remains with the main agent; no citation or numerical exponent is invented. The result is an original conditional synthesis, not independent review, and it makes no assertion about the rationality or irrationality of e+pi itself.
