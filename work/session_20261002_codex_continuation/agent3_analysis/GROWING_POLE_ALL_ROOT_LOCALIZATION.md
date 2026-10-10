> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# M31 continuation: complete middle coefficients and every-root localization

Author: Agent 3 / analysis, 2026-10-02. Original analysis. Fresh gate: GROWING_POLE_MIDDLE_ROOT_GATE.md. Root owns actual normalized response, rational moments, primitive clearers/content and coefficient growth. This note uses the preceding GROWING_POLE_ORDER_SHORT_COMPLETE_PRODUCT.md with its full normalized-Taylor convention. No audit of Root's content certificates is performed.

## 1. Result for the actual stack

Keep the exact notation of the complete product theorem: k>=131072, 1<=m<=k, S=e+pi, beta(s)=det[C;R+sV], a=1/(48e^4), L0=exp(-4/a), ell=log(1+sqrt(2)), and kappa_m=[(m-1)!/(1/2)_(m-1)]^m. ALL actual moment terms and endpoint jets remain in this polynomial.

Write b_l=[t^l]beta(S+t). The full middle coefficients satisfy, for 0<=l<m,

    |b_l|<=F* I_l B_(k,m,l)/l!,
    B_(k,m,l)=2^[l(m+l-2)] k^[2l(m-l)] exp(3l),             (1)

where I_l is the genuine positive compact insertion integral

    I_l=1/(k-l)! integral_[0,1]^(k-l) Vand(x)^2
                             product_i(1+x_i)^(2l)
                                           d sigma_m^(k-l),
    I_0=det G_(sigma_m,k),  I_k=1,
    F*=det M_[mu(y+1)^k,k]>0.

The leading coefficient has the exact previous lower bound

    |b_m|=|beta_m|>=L0 kappa_m F* I_m.                     (2)

Every complex root s_j, with multiplicity, therefore obeys the explicit complete estimate

    log|s_j-S| <= -4ell k +2m log k
         +(4ell+log4+3)(m-1)+(m-1)(2m-3)log2
         +C0+log(6m)+4/a+log2,                            (3)
    C0=log[32pi^2(3+2sqrt(2))^2].

Thus ALL roots, without assuming real-rootedness, satisfy

    max_j |s_j-S|<=exp[-4k log(1+sqrt(2))
                                     +O(m^2+m log(k+1))],  (4)

with an absolute constant. In particular, for m=o(sqrt(k)), the individual upper exponent is -4k log(1+sqrt(2))+o(k). No individual lower error bound is asserted.

A clean fully quantified range is

    k>=131072, 1<=m<=floor(sqrt(k))
                  ==> max_j|s_j-S|<=exp(-k/2).              (5)

This range is genuinely growing, and all constants include the full derivative response. Hyperbolicity remains a separate question; (3)--(5) do not require it.

## 2. Complete derivative insertion; the exact Vandermonde order matters

The preceding theorem's ALL-coefficient identity is

    b_l=(-1)^k/[l!(k-l)!] integral Vand(x)^2
       ·nu_(u_1)...nu_(u_l)
         {Vand(u)^2 product_(a,i)(u_a-x_i)^2 F(x,u)}
                                             d sigma_m^(k-l). (6)

Here nu includes every actual derivative through m-1. Introduce v_a=u_a+1 and let

    cross_0=product_i(1+x_i)^(2l),  r=k^(-2).

For a multivariate polynomial P(v), define its absolute Taylor coefficient norm at this radius by ||P||_r=sum_alpha |[v^alpha]P|r^|alpha|. This norm is submultiplicative. The following estimates are exact finite polynomial estimates, not a complex positive-ensemble substitution.

First, the COMPLETE conditional comparison gives 0<F(x,u)<=F* when all x,u are real in [-1,1]. F has degree at most k in each inserted variable. Repeated Markov in these separate variables yields

    |[v^alpha]F(x,v-1)|
                   <=F* k^(2|alpha|)/product_a alpha_a!,
    ||F(x,v-1)||_r<=F* exp(l k^2r)=F*exp(l).               (7)

Second, for compact x_i in [0,1],

    ||product_(a,i)(v_a-1-x_i)^2||_r
       <=cross_0 product_(a,i)[1+r/(1+x_i)]^2
       <=cross_0 exp[2r l(k-l)]<=cross_0 exp(2l).           (8)

Finally the Vandermonde is unchanged by translation and is homogeneous of degree l(l-1). Its absolute norm is at most

    ||Vand(v)^2||_r<=(2r)^[l(l-1)].                        (9)

The true jet coefficients satisfy a_j j!<=2^j. Applying l copies of the FULL jet functional to a Taylor series therefore selects coefficients with alpha_a<=m-1 and weights bounded by2^|alpha|. Since r<=1 and |alpha|<=l(m-1),

    |nu_(u_1)...nu_(u_l)(P)|
                <=(2/r)^[l(m-1)] ||P(v-1)||_r.             (10)

Combining (7)--(10), the integrand in (6), in absolute value, is at most

    F* cross_0 exp(3l)
             ·(2/r)^[l(m-1)](2r)^[l(l-1)]
       =F* cross_0 exp(3l)
                         2^[l(m+l-2)] k^[2l(m-l)].         (11)

Integrating (11) proves (1), including its factorial normalization. The vanishing order in (9) is crucial: it removes l(l-1) powers of the derivative radius. Omitting it would falsely impose an extra m-dependent power of log k in the useful growing range. Formula (11) bounds the complete actual integrand; no middle-coefficient positivity sign is inferred.

## 3. Exact insertion ratios and the Cauchy root disk

The classical normalized-jet identity and its successive-value factorization imply

    I_m/I_l=product_(r=l)^(m-1)
                       K_[sigma_m(y+1)^(2r),k-r](-1).      (12)

This is the ACTUAL compact measure for the current m. By dsigma_m<=6m dgamma, 1<=(1+y)^(2r)<=4^r and the uniform reference bound from the preceding theorem,

    log K_[sigma_m(y+1)^(2r),k-r](-1)
       >=4ell(k-r)-2log(k-r)-C0-log(6m)-r log4.

Consequently, for h=m-l>=1,

    (1/h)log(I_l/I_m)
       <=-4ell k +(4ell+log4)(m-1)+2log k+C0+log(6m).      (13)

Equations (1)--(2) give

    (|b_l/b_m|)^(1/h)
       <=(L0^(-1) B_(k,m,l) I_l/[kappa_m l! I_m])^(1/h).

Dropping only the nonnegative cost reductions log kappa_m and log l!, use

    l<=m-1,
    l(m+l-2)/(m-l)<=(m-1)(2m-3),
    l/(m-l)<=m-1,
    4/(ah)<=4/a.

These bounds and (13) show that log M, where M=max_(l<m)|b_l/b_m|^(1/(m-l)), is bounded by the right side of (3) without its final log2.

The standard Cauchy argument gives ALL roots in |t|<=2M: for |t|>2M,

    sum_(l<m)|b_l t^l|/|b_m t^m|
       <=sum_(h=1)^m(M/|t|)^h<1.

The leading term cannot be canceled, proving (3). This uses the full polynomial; it is not a bound on an isolated pi coordinate or only on the constant term.

For the explicit range (5), m<=sqrt(k), ell<1, log4<2, log2<1, C0<15 and 4/a<15552. Equation (3) is at most

    -(4ell-2log2)k
                 +2sqrt(k)log k+9sqrt(k)+15571+log k.

Here 4ell-2log2=2log[(3+2sqrt(2))/2]>2log2>1. The remaining positive terms are less than k/2 for k>=131072. One can verify the threshold without approximate constants: sqrt(131072)<363 and log(131072)=17log2<17 give their sum less than31197<65536. After division by k each of the three functions 2log k/sqrt(k),9/sqrt(k),(15571+log k)/k decreases on this range. This proves (5).

## 4. Justified leading-coefficient versus ACTUAL height relation

Let Pi(s)=A_m product_j(s-s_j) be Root's FINAL primitive polynomial, containing all moment clearers and the complete final gcd. Put R_k=max_j|s_j-S|. Whenever m R_k tends to0, each elementary symmetric coefficient obeys uniformly for 0<=r<=m

    A_(m-r)/A_m
       =(-1)^r binom(m,r)S^r[1+O(m R_k)].                  (14)

To prove (14), expand each r-fold root product around S: its relative error is at most (1+R_k/S)^r-1, and then sum over its binom(m,r) terms. This proof works for conjugate complex roots; it does not assume they are real. In the explicit range (5), mR_k<=sqrt(k)exp(-k/2) tends to0 uniformly.

Thus the ACTUAL coefficient height, with the actual content preserved, satisfies

    H(Pi)/|A_m|
       =max_(0<=r<=m) binom(m,r)S^r[1+O(mR_k)],
    log H(Pi)-log|A_m|
       =m log(1+S)-(1/2)log(m+1)+O(1)+O(mR_k).             (15)

The absolute O(1) in (15) is the ordinary fixed-parameter binomial peak estimate, obtainable from Stirling; S is the fixed number e+pi. For fixed m the exact maximum in (15) is the appropriate constant. For growing m one must RETAIN the m log(1+S) term, rather than asserting a uniform bounded height ratio.

Combining (15) with the COMPLETE primitive product interface now gives, in the range (5),

    log|Pi(S)|=log H(Pi)-m log(1+S)+(1/2)log(m+1)
                  -log kappa_m-log det K_(sigma_m,k,m)+O(1). (16)

The O(1) remains absolute, including the earlier fixed4/a comparison constant. Equation (16) is an analytic relation for the actual final primitive polynomial. It does not establish a favorable actual height, common content growth, or a rationality theorem for e+pi.

## 5. Scope of symmetry and hyperbolicity

The all-root theorem above succeeds without asserting symmetry of the actual reduced jet kernel. In normalized Taylor coordinates h=y+1, the finite matrix T=[C;L] yields the EXACT response reduction

    beta(S+t)=beta(S)det[I_m+t J_m H_eff],
    H_eff=E_(2k)^T T^(-1) [0;E_k],                         (17)

where E_n embeds the first m normalized Taylor coefficients and J_m is the actual symmetric derivative-of-product response matrix. The full two-block inverse in (17) is necessary. Replacing H_eff by the ordinary positive compact jet kernel does not follow from the matching constraints.

For m=3 the raw constant-coefficient jet operator is

    A_3(D)=1+(4/3)D+(4/3)D^2.

It is not a universal real-rootedness preserver: applying it to z^2 produces z^2+(8/3)z+8/3, whose discriminant is -32/9. Thus positivity of the jet coefficients or a stability-preserving argument based only on this operator is insufficient. This is an operator obstruction, not a nonreal-root counterexample for the actual stack.

Root's nine existing exact primitive polynomials, m=3,...,7, all have exactly m real roots by a new exact Sturm count using those supplied coefficients. Those finite observations neither prove all-degree hyperbolicity nor contradict the above operator obstruction. No new actual-content calculation was made.

There is also a rigorously certified failure of the NATURAL symmetry assertion in (17), for the ACTUAL construction at m=k=3. In h=y+1 coordinates, partition the full stack into three-by-three blocks [M,A;B,C]. Then

    H_eff=[B-C A^(-1)M]^(-1).

The exact entries use mu(h^r)=sum_j binom(r,j)D_(2j), nu(h^r)=r!a_r for r<m and0 otherwise, and

    sigma_m(h^r)=sum_j binom(r,j)[eD_(2j)-(2j)!]
                        +c_m integral_0^1(1+x^2)^(r-m)dx.

These are the full actual entries. The small negative powers in the last integral have the usual exact rational-plus-pi reduction; no endpoint is omitted. Exact symbolic cofactors followed by elementary rational bounds for e and pi prove

    55575/10000 < (H_eff)_(0,1)-(H_eff)_(1,0) < 55577/10000.

Thus this actual effective jet matrix is NOT symmetric. The certificate uses the e factorial series through80 and100 alternating terms of Machin's identity for pi, not floating-point sign inference. The script growing_pole_root_symmetry_receipt.py and GROWING_POLE_ROOT_SYMMETRY_RECEIPT.json save the exact cofactor/determinant polynomials, source-attributed Sturm counts and certified interval. This counterexample rejects the natural symmetry substitution only; it does not exclude another symmetrizer or prove nonreal roots. The independent every-root theorem in Sections1--4 remains valid.
