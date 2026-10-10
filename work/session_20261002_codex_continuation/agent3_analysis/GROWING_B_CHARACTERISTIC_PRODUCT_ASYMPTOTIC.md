> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A uniform growing-size signed error for the actual B reconstruction

Author: Codex continuation Agent 3, 2026-10-02. Original analysis, not independently reviewed. This follows the completed bounded arithmetic audit and the fixed-size metric calculation. All quantities below belong to the actual B reconstruction, including its coefficient-zero endpoint. No denominator estimate or assertion about rationality of e+pi follows.

Put sigma=sqrt(2), M=1+sigma, a=sigma/(2M), beta=sigma M/2, d=b-1. Let n tend to infinity through either parity and allow integer b=b(n)>=3 with

    b=o(n^(1/4)).                                      (1)

The original contact matrix T, B reconstruction K and forcing vectors fP,fQ are retained exactly. For every positive diagonal rational metric W_n, define

    xi=T^(-1)fP, u=Kxi, v=e0+KT^(-1)fQ,
    c_W=u^T W_n v/(u^T W_n u).

Then T is nonsingular, every u_j is nonzero, and the COMPLETE actual center has

    c_W-(e+pi)=(-1)^(n+1)4pi M^(-2n-b)(1+o(1)),          (2)

uniformly over those positive weights. The little-o in (2) depends only on n,b. In particular the permitted factorial metrics, even with their depth varying over the permitted range, are included. No fixed-b implicit constant is used to justify (2).

Taking b=floor(n^theta), 0<theta<1/4, supplies the additional factor exp(-log(M)n^theta+O(1)) relative to a fixed-size center. This gain is stronger than any fixed power of n. Its logarithm divided by n still tends to -2log M. The proportional allocation b~lambda n is outside this result.

## 1. Searches and attribution before this target

Archive queries included growing-b, uniform-b, growing dimension, Toeplitz saddle, Gaussian, characteristic polynomial, cofactor product, top coordinate, and the n>=512 b^4 log n range. The first broad query was overinclusive; it was narrowed to the October 1 contact-normality/contact-inverse sources and the growing-block filenames.

Relevant overlap:
- work/session_20261001_astra/agent3/CONTACT_NORMALITY_RESEARCH.md proves contact normality on n>=512 b^4 log n. Its complex circle integral is the same contact matrix. The present result derives relative Gaussian asymptotics and the complete ACTUAL center, on the little-o domain (1), rather than importing its fixed-size constants or replaying its accepted review.
- work/session_20261001_astra/agent3/CONTACT_INVERSE_RESEARCH.md provides the exact complete exponential-forcing identity and the uniform coefficient bound used in Section 5.
- work/session_20261001_astra/agent2/RATIONAL_SADDLE_SELECTOR.md gives a direct-selector curvature gain. Its selector is prescribed in advance and is distinct from the inverse-derived actual Gram center here.
- work/session_20260913/raw_growing_low_node_minor_theorem.md concerns another endpoint matrix and a logarithmic number of selected nodes. It is not a theorem for this center.
- Our FIXED_B_UNIVERSAL_FIRST_CORRECTION.md contains the fixed-size limiting constants and exact cofactor insertion. The current proof tracks the dimension anew.

Current primary-source searches:
- site:arxiv.org Toeplitz determinant varying size localized weight Gaussian unitary ensemble Laplace asymptotic small dimension
- site:arxiv.org Toeplitz determinants varying weight Gaussian unitary localized Gross Witten double scaling
- site:arxiv.org Hermite Pade approximants growing degree number functions asymptotics double scaling
- site:arxiv.org Hermite Pade growing number functions asymptotic

Opened [Chen, Xu and Zhao, modified-Bessel determinant asymptotics](https://arxiv.org/abs/2402.11233), including the [full 41-page paper](https://arxiv.org/pdf/2402.11233). Their extended Gross-Witten-Wadia symbol and critical double-scaling regime differ from this concentrated small-size domain. An attempted HTML v2 URL returned 404; the actual primary PDF succeeded.

Opened [Kuijlaars, Van Assche and Wielonsky, quadratic exponential Hermite-Pade](https://arxiv.org/abs/math/0302357), and [Driver and Temme, exponential Hermite-Pade polynomials](https://ir.cwi.nl/pub/4749/), including the [full CWI report](https://ir.cwi.nl/pub/4749/04749D.pdf). These supply methodological overlap in multi-parameter saddle analysis, with different approximation systems. The exact cofactor/Schur methodology is already established in [Garcia-Garcia and Tierz](https://arxiv.org/abs/1706.02574), read for the preceding target. No source theorem for (2), or claim of global novelty from search absence, is made.

## 2. Exact cofactor characteristic products

Set D=diag((-sigma)^i), H=(-1)^n DTD^(-1). Its moments are

    H_ij=(1/(2pi)) integral_(-pi)^pi
          (1+sigma cos t)^n exp(-sigma exp(it)) exp(i(j-i)t) dt.

For r variables z_l=exp(it_l), define the unnormalized complex functional

    nu_(n,r)(F)=1/[r!(2pi)^r] integral F(z)
        product_l [(1+sigma cos t_l)^n exp(-sigma z_l)]
        product_(p<q)|z_q-z_p|^2 dt_1...dt_r.

Thus det H_r=nu_(n,r)(1). No finite-n positivity is assumed. With e_k denoting an elementary symmetric polynomial, the missing-power alternant gives the exact FULL cofactor formula

    adj(H_b)_(j,i)=(-1)^(i+j)
       nu_(n,d)(e_(d-i)(z^(-1)) e_(d-j)(z)), 0<=i,j<=d.  (3)

At z_l=1 the insertion equals binom(d,i)binom(d,j). The top-row version of (3) is a special case. For every complex zeta,

    sum_(i=0)^d sigma^i e_(d-i)(z^(-1))
                             (1 +/- zeta/sigma)^i
       =product_(l=1)^d (z_l^(-1)+sigma +/- zeta).         (4)

The exact force-circle and two-endpoint force-arc identities are

    fP_i=n!/(2pi) integral_(-pi)^pi
                  (1+sigma cos s)^n(1+exp(is)/sigma)^i ds,

    eF_i=(-1)^(n+1)2n! integral_(-pi/4)^(pi/4)
                  (sigma cos s-1)^n(1-exp(is)/sigma)^i ds.

Retain both conjugate logarithmic endpoints and their orientation. Combining (3),(4) removes the cofactor sum exactly. Define Fplus_j as nu_(n,d) applied to

    e_(d-j)(z) n!/(2pi) integral_(-pi)^pi
       (1+sigma cos s)^n product_l(z_l^(-1)+sigma+exp(is)) ds,

and Fminus_j similarly with 2n!, the arc interval, sigma cos s-1 and minus exp(is). Then

    (T^(-1)fP)_j=(-1)^n sigma^(-j) Fplus_j/det H_b,
    (T^(-1)eF)_j=-sigma^(-j) Fminus_j/det H_b.            (5)

The determinant is not canceled until its nonzero relative asymptotic has been proved. Formula (5) avoids inversion of a rank-one limiting matrix.

## 3. Uniform localization, including the tails

The following estimates use absolute constants independent of b. The functions have unique absolute maxima at zero, and there is c>0 with

    |1+sigma cos t|<=M exp(-c t^2), -pi<=t<=pi,
    0<=sigma cos s-1<=M^(-1)exp(-c s^2), |s|<=pi/4.

The first assertion includes the negative-base portion for odd n. It follows by continuity away from zero and its strictly negative quadratic logarithm at zero. For sufficiently small arguments,

    log((1+sigma cos t)/M)=-a t^2+O(t^4),
    log(M(sigma cos s-1))=-beta s^2+O(s^4).

Localize all determinant variables, and the additional forcing variable when present, to the Euclidean ball

    sum_l t_l^2+s^2<=R^2,  R^2=b n^(-3/4).              (6)

Under (1), R tends to zero. On this ball the combined quartic exponent error is O(nR^4)=O(b^2 n^(-1/2)). The circle Vandermonde divided by the real Vandermonde obeys

    product_(p<q)|exp(it_q)-exp(it_p)|^2
       =Delta(t)^2 exp(O(b R^2)),

including collisions by continuous extension of sinc. Its error is O(b^2 n^(-3/4)). The analytic symbol phase and amplitude, divided by exp(-r sigma), differ by O(sqrt(b)R+R^2).

The normalized elementary symmetric insertion differs from its value at one by at most sqrt(b)R: it is an average of exp(i sum of selected t_l). Each normalized product in (4) differs from one by O(bR), since its individual logarithms have bound C(|t_l|+|s|). At zero their values are

    e_(d-j)(1)=binom(d,j),
    product plus=(2+sigma)^d, product minus=sigma^d.

Thus every determinant/cofactor/forced integral has pointwise relative local error bounded by

    C[b^(3/2)n^(-3/8)+b^2n^(-1/2)+b^2n^(-3/4)].         (7)

For the tails, |exp(it_q)-exp(it_p)|<=|t_q-t_p|. Also |e_k(z)|<=binom(r,k); the plus product normalized at zero has modulus <=1 and the minus product has modulus <=M^d. The symbol amplitude contributes at most exp(Cb) after its zero value is removed. Consequently the absolute tail divided by the corresponding Gaussian leading integral is bounded by

    exp(Cb^2) times a Gaussian/Vandermonde radial tail
                  beyond sum t_l^2+s^2=R^2.

The homogeneous squared Vandermonde gives radial shape r^2/2 for an r-variable determinant, and (d^2+1)/2 with the extra scalar force variable. Replacing the Gaussian curvatures by their smaller common constant c changes the total integral by at most exp(Cb^2). The elementary exponential-moment bound on that radial gamma integral therefore gives the absolute relative tail

    integral_(Q>R^2) exp(-cnQ)Delta(t)^2 dt ds
       <=exp(-cnR^2/2) integral exp(-(c/2)nQ)Delta(t)^2 dt ds,

where Q=sum t_l^2+s^2 and the absent scalar variable is omitted for determinants. Homogeneous scaling compares the final integral with the target Gaussian integral by a constant raised to at most b^2/2. The additional global factors are exp(O(b)). Hence

    <=exp(-c' b n^(1/4)+C' b^2),                        (8)

after adjusting positive absolute constants. This tends to zero under (1). It controls the original compact-domain tail as well as extending the local Gaussian integral to all Euclidean space. There is no finite complex measure interpreted as positive: positivity is used only for the absolute Gaussian comparison.

Let epsilon_(n,b) denote a sufficiently large constant times the bracket in (7), plus (8) with adjusted constants. It tends to zero whenever b=o(n^(1/4)). Equations (7),(8) apply uniformly in every cofactor index.

In particular

    det H_r=C_r M^(rn)n^(-r^2/2)(1+O(epsilon_(n,b))),
    C_r=exp(-r sigma) product_(l=0)^(r-1)l!
          /[2^(r(r+1)/2)pi^(r/2)a^(r^2/2)], r=d,b.       (9)

These are relative estimates with positive leading constants, so det H_b is nonzero eventually on both parities.

## 4. Actual inverse and coefficient reconstruction

The forced Gaussian integrals give uniformly in j

    Fplus_j=binom(d,j)(2+sigma)^d
       C_d M^(dn)n^(-d^2/2)
       [n!M^n/(2sqrt(pi a n))](1+O(epsilon_(n,b))),

    Fminus_j=binom(d,j)sigma^d
       C_d M^(dn)n^(-d^2/2)
       [2n!M^(-n)sqrt(pi/(beta n))]
                                      (1+O(epsilon_(n,b))).

Dividing only now, their ratio is

    Fminus_j/Fplus_j=4pi M^(-2n-b)(1+O(epsilon_(n,b))).   (10)

The constants use sqrt(a/beta)=M^(-1) and sigma/(2+sigma)=M^(-1). Thus, for r_j=binom(d,j)sigma^(-j),

    xi_j=(-1)^n exp(sigma)(2^d/d!)n!n^d r_j
                                      (1+O(epsilon_(n,b))),
    (T^(-1)eF)_j/xi_j=(-1)^(n+1)4pi M^(-2n-b)
                                      (1+O(epsilon_(n,b))). (11)

These estimates alone do not license arbitrary subtraction by K. Track that step explicitly. In the ascending monomial basis A=(I+Dpol)^(-n) has

    A_(r,l)=(-1)^(l-r)(n)_(l-r)binom(l,r), l>=r,

where (n)_k is rising factorial. Since Z multiplies by t-1,

    K_(0,l)=(-1)^(l+1)(n)_l,
    K_(j,l)=(-1)^(l-j+1)[(n)_(l-j+1)binom(l,j-1)
                         +(n)_(l-j)binom(l,j)], 1<=j<=d,
    K_(b,d)=1,

with the missing terms zero, including the l=j-1 edge. For every row j and l=d-k<d in its support,

    |K_(j,d-k)/K_(j,d)|<= (1+d/n)n^(-k).

Row b has no lower-column contribution. Because r_(d-k)/r_d=binom(d,k)sigma^k, the sum of absolute lower-column contributions relative to the top column is at most

    (1+d/n)[(1+sigma/n)^d-1]=O(b/n).                     (12)

Hence every u_j is nonzero and its sign comes from the top-column term. Applying (11),(12) to numerator and denominator proves the actual coordinate logarithmic error (10), with additional uniform O(b/n) relative error. This is a quantitative reconstruction step, not a formal rank-one substitution.

## 5. Complete exponential forcing and the endpoint

The exact forcing decomposition fQ-(e+pi)fP=eF+eE is retained. The inherited full exponential coefficient estimate, uniform in i, is

    |eE_i|<=27 M^n sigma^(-i)/(n+1).

Absolute cofactor localization gives |nu_d(e_(d-i)(z^-1)e_(d-j)(z))| at most a constant times its positive Gaussian leading scale binom(d,i)binom(d,j). After multiplication by D_i, the powers sigma^i in that bound cancel those in eE_i. Summing the binomial coefficients supplies 2^d. Comparing with the nonzero plus forcing, and then applying (12), gives for every actual coefficient row

    |(KT^(-1)eE)_j/u_j|
       <=C [2/(2+sigma)]^d/(n!sqrt(n)).                 (13)

This is factorially smaller than M^(-2n-b) uniformly in (1). The coefficient-zero endpoint is e0_0=1 and all other endpoint coordinates vanish. From (11),(12),

    |1/u_0|<=C d!/[sigma^d n! n^(2d)].                 (14)

Here (n)_d/n^d=exp(O(d^2/n))=1+o(1). The bound (14) is also factorially smaller than M^(-2n-b) uniformly in (1). Both terms concern the complete residual functions and exact endpoint, not their first Taylor coefficient.

Every actual coordinate c_j=v_j/u_j therefore satisfies (2) with one common uniform error bound. Finally

    c_W=sum_(j=0)^b alpha_j c_j,
    alpha_j=W_jj u_j^2/(sum_l W_ll u_l^2)>=0,
    sum_j alpha_j=1.

Exact convexity propagates the same bound to every positive diagonal metric, however its rational weights vary with n. This proves (2).

## 6. Scope of the parameter gain

The result changes a size-dependent prefactor into a stretched exponential when b grows polynomially below n^(1/4). It does not change the leading exponential rate in n, and positive diagonal tuning cannot cancel the common leading error anywhere in this uniform domain.

The bound concerns approximation error only. Actual rational reduced denominators can depend on b, the depth, and the metric through combined content. The fixed-b odd-prime atlas is not transferred to varying b or altered weights. Proportional b, indefinite or off-diagonal metrics, and other reconstructions remain separate questions. This authored result has no independent review and does not establish rationality or irrationality of e+pi.
