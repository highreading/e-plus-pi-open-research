> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete diagonal error/content threshold — Stage 1

Author: Child 3, current Astra continuation. Status: new author derivation using the inherited complete signed-product and exact primitive-moment interfaces. No independent review is claimed. S is the actual real number e+pi; its rationality remains unresolved.

## 1. Result and scope

For the actual diagonal family m=k, k>=131072, write beta(T)=sum_{j=0}^k beta_j T^j. Let I_j=delta beta_j be the complete integer coefficients described below, g=gcd(I_0,...,I_k)>0, P(T)=sum_j(I_j/g)T^j, and A_k=|I_k/g|. Then

    log|beta(S)/beta_k| = -(log 4)k^2 -(1/2)k log k + O(k).          (1)

The implied constant is absolute. This is a proved two-term expansion, not merely an O(k log k) bracket. Explicit finite bounds appear in (17). The improvement is an elementary determinant-level comparison for the actual narrow endpoint bump, whose cost is O(k), even though the pointwise maximum of the weight grows like sqrt(k).

Put D_k=det[1/(i+j+1/2)]_{0<=i,j<k},

    kappa_k=[4^(k-1)/binom(2k-2,k-1)]^k,
    U_k=(e+10pi^2/3+16k^2(4/5)^k)/2,
    U=(e+10pi^2/3+1)/2,
    C=4/a=192e^4,   a=1/(48e^4).

For all k>=131072, U_k<=U. For each fixed positive integer v, an explicit sufficient condition for the actual primitive value to beat v^(-k) is

    A_k < kappa_k/[D_k(v U_k)^k].                              (2)

A necessary condition for beating that target is

    A_k < exp(C) 2^k kappa_k/[v^k D_k].                        (3)

Consequently the logarithmic threshold for A_k is

    (log 4)k^2 +(1/2)k log k + O_v(k),                         (4)

with a completely explicit O_v(k) interval below. This is a threshold on the ACTUAL primitive leading coefficient, after the final gcd, not on a raw response or a guaranteed divisor. No arithmetic theorem establishing (2) is supplied here.

## 2. Exact inherited objects; every endpoint jet is retained

The sources actually read are BACKGROUND_MAP.md in the current main directory and, under work/session_20261002_codex_continuation/:

- agent3_analysis/GROWING_POLE_ORDER_SHORT_COMPLETE_PRODUCT.md;
- main/GROWING_POLE_ACTUAL_NORM_CONTENT_BUDGET.md;
- agent3_analysis/GROWING_POLE_ALL_ROOT_LOCALIZATION.md;
- main/GENERAL_POLE_RANK_M_PRIMITIVE_INTERFACE.md.

The following complete identities and positivity theorem are inherited author results, not newly audited here. Let mu be the pushforward of exp(-t)dt, t>=0, by y=(1-t)^2. For d=k-1,

    nu_k(f)=sum_{j=0}^d a_j f^(j)(-1),
    a_j=2^j binom(d,j)(2(d-j)-1)!!/(2d-1)!!,
    a_d=1/(1/2)_d,
    rho_k=mu-nu_k.

All terms of this finite functional remain present. On 0<=y<=1 put

    dgamma=y^(-1/2)dy,
    c_k=4^k/binom(2k-2,k-1),
    dsigma_k=(exp(sqrt(y))+c_k(1+y)^(-k)) dgamma/2.

For the k-by-2k blocks C_ij=rho_k(y^(i+j)), V_ij=nu_k(y^(i+j)), and the complete rational block R, the actual compact moments are eC+R+SV, S=e+pi. Hence the exact row operation gives beta(S)=det[C;sigma_k].

The inherited conditional comparison, valid for k>=131072, gives

    exp(-C) F*_k det G_(sigma_k,k)
        <= |beta(S)| <= F*_k det G_(sigma_k,k),
    sign beta(S)=(-1)^k,
    F*_k=det M_[mu(y+1)^k,k]>0.                              (5)

The complete confluent leading-coefficient formula specializes EXACTLY to

    beta_k=(-1)^[k+binom(k,2)] kappa_k F*_k.                  (6)

Indeed (y+1)^k kills every upper jet through order k-1. In the lower k-variable confluent coefficient, the Vandermonde square has total vanishing order k(k-1), so the highest derivative k-1 in each variable is forced and all derivatives fall on that square. Its coefficient and the integration factorial produce exactly kappa_k, with no omitted jet, Taylor factorial, or basis factor.

Equations (5)-(6) imply

    beta(S)/beta_k=(-1)^binom(k,2) theta_k detG_(sigma_k,k)/kappa_k,
    exp(-C)<=theta_k<=1.                                    (7)

Both the full value and leading coefficient are nonzero. In particular the comparison error is ONE-SIDED in the diagonal case: log theta_k lies in [-C,0]. We do not need or infer individual-root localization. The previously read all-root theorem has a different useful parameter range and is not extended to m=k by a product estimate.

For exact arithmetic, let B_k be the odd part of binom(2k-2,k-1), L_n=lcm(1,...,n),

    E_(k,k)=B_k 2^(3k+2) L_k L_(6k),
    delta=B_k^k E_(k,k)^k,
    I_j=delta beta_j,  g=gcd(I_0,...,I_k),  A_k=|I_k/g|.

These are the complete inherited clearers and final coefficient gcd. No replacement of g by a partial or guaranteed content is made. Scaling (7) gives the exact identity

    |P(S)|=A_k theta_k detG_(sigma_k,k)/kappa_k.              (8)

## 3. Elementary O(k) determinant comparison for the actual compact weight

The coarse pointwise comparison only yields an O(k log k) logarithmic determinant interval. We instead estimate the trace of the bump in the reference orthonormal basis and apply determinant AM-GM.

Write y=x^2. Since dgamma=2dx on [0,1], its degree-i orthonormal polynomial in y is

    p_i(y)=sqrt((4i+1)/2) P_(2i)(sqrt(y)),

where P_n is the ordinary Legendre polynomial. Thus the reference kernel is

    K_k(x^2)=sum_{i=0}^{k-1}(2i+1/2)P_(2i)(x)^2.            (9)

An elementary Laplace integral gives, for -1<x<1 and n>=1,

    P_n(x)=(1/pi) integral_0^pi
                 (x+i sqrt(1-x^2) cos phi)^n dphi.

Taking absolute values, using 1-u<=exp(-u), symmetry about pi/2, and sin phi>=2phi/pi on [0,pi/2], yields

    |P_n(x)| <= sqrt(pi)/sqrt(2n(1-x^2)).

The same representation also gives |P_n(x)|<=1 on [-1,1]. For i>=1 and 0<=x<=1/2,

    (2i+1/2)P_(2i)(x)^2
        <=5pi/[8(1-x^2)] <=5pi/6.

The i=0 term is 1/2. Consequently

    K_k(x^2)<=5pi k/6       for 0<=x<=1/2,
    K_k(x^2)<=k^2           for 0<=x<=1.                    (10)

Let G=G_(gamma,k), H=G_[gamma(1+y)^(-k),k], and M=G^(-1/2)HG^(-1/2). Then M is positive definite and

    tr M=2 integral_0^1 K_k(x^2)(1+x^2)^(-k)dx.

The exact beta integral cancels the growing bump normalization:

    J_k=integral_0^infinity (1+x^2)^(-k)dx
       =(pi/2) binom(2k-2,k-1)/4^(k-1),
    c_k J_k=2pi.                                           (11)

Split the trace at x=1/2 and use (10), (11), and c_k<=8k. This proves

    c_k tr M <= (10pi^2/3)k+16k^3(4/5)^k.                  (12)

The first term comes from the whole half-line beta integral, which is an upper bound for the short-interval integral. The second comes from the remaining interval, where (1+x^2)^(-k)<=(4/5)^k.

Because exp(x)<=e,

    G_(sigma_k,k) <= (eG+c_k H)/2

in Loewner order. Determinant monotonicity and AM-GM on the k positive eigenvalues of (eI+c_k M)/2 now give

    detG_(sigma_k,k)/D_k
       <= [(e+c_k tr M/k)/2]^k <= U_k^k.

The lower pointwise comparison dsigma_k>=dgamma/2 gives the other side:

    2^(-k) D_k <= detG_(sigma_k,k) <= U_k^k D_k.            (13)

For k>=64, 16k^2(4/5)^k<=1. One explicit verification is (4/5)^8<1/5, so the assertion holds at 64; the ratio of consecutive k^2(4/5)^k terms is less than one for k>=64. This proves U_k<=U throughout the required range.

Thus, with

    eta_k=log(detG_(sigma_k,k)/D_k),

we have the explicit improvement

    -k log 2 <= eta_k <= k log U_k <= k log U.              (14)

No uniform varying-weight asymptotic theorem was used. The bound uses the actual bump normalization and the actual compact measure. It is not a pointwise bounded-weight assertion.

## 4. Exact Cauchy determinant and quantified reference expansion

Cauchy's determinant identity and the even-Legendre monic norms give equivalent exact formulas

    D_k=product_{0<=i<j<k}(j-i)^2 /
             product_{0<=i,j<k}(i+j+1/2)
       =product_{i=0}^{k-1}
             2^(4i+1)/[(4i+1)binom(4i,2i)^2].              (15)

Here D_1=2. A useful quantified version is as follows. Let H_n=sum_{i=1}^n 1/i and H_n^(2)=sum_{i=1}^n 1/i^2. For k>=2,

    log D_k=-(log 4)k^2+k log(4pi)+log(2/pi)
                      -(1/8)H_(k-1)+E_k,
    -H_(k-1)^(2)/144 <= E_k <=37 H_(k-1)^(2)/1152.          (16)

For completeness, the elementary Stirling remainder bounds

    log(n!)=(n+1/2)log n-n+(1/2)log(2pi)+r_n,
    1/(12n+1)<r_n<1/(12n)

imply r_n=1/(12n)+e_n with -1/(144n^2)<e_n<0. Therefore

    log binom(4i,2i)=4i log2-(1/2)log(2pi i)-1/(16i)+d_i,
    -1/(2304i^2)<=d_i<=1/(288i^2).

Substitution in the i-th factor of (15), together with

    0<=z-log(1+z)<=z^2/2, z=1/(4i),

gives log of that factor equal to -4i log2+log pi-1/(8i)+epsilon_i, where

    -1/(144i^2)<=epsilon_i<=37/(1152i^2).

Summing proves (16). In particular E_k has a finite limit, so the reference expansion has an O(1) remainder after its displayed harmonic term.

The exact kappa_k is retained in all finite thresholds. Stirling also gives

    log kappa_k=(k/2)log k+(k/2)log pi-3/8+O(1/k).

For an explicit finite remainder, set n=k-1. Then

    log kappa_k=(k/2)log(pi n)+k/(8n)+r'_k,
    -k/(72n^2)<=r'_k<=k/(576n^2).

This follows from the same remainder calculation for binom(2n,n).

Combining (7), (13), and the exact kappa yields the entirely explicit error-product bracket

    log D_k-log kappa_k-k log2-C
       <= log|beta(S)/beta_k|
       <= log D_k-log kappa_k+k log U_k.                    (17)

Equations (16)-(17) prove (1). Define the exact reference threshold exponent

    Lambda_k=log kappa_k-log D_k.

It has the more detailed REFERENCE expansion

    Lambda_k=(log4)k^2+(1/2)k log k-k log(4sqrt(pi))
                          +(1/8)log k+C_ref+O(1/k),        (18)

where C_ref is a finite constant determined by the convergent epsilon_i sum and the harmonic constant. Formula (16) and the explicit r'_k bounds are sufficient if no named limiting constants are desired.

The actual ratio is -Lambda_k+eta_k+log theta_k. Since eta_k is presently controlled only to O(k), neither the displayed reference coefficient of k nor its logarithmic term is claimed as a coefficient of the actual ratio. The actual proved expansion is exactly (1).

## 5. Rational-target criterion and arithmetic handoff

Equations (8), (13) imply

    A_k exp(-C) D_k/(2^k kappa_k)
        <= |P(S)| <= A_k U_k^k D_k/kappa_k.                 (19)

If S=u/v in lowest terms, v>=1, then v^k P(u/v) is an integer. The inherited complete nonvanishing theorem says P(S)!=0, so necessarily |P(S)|>=v^(-k). Thus (2) excludes that hypothetical denominator v for any k where its actual arithmetic inequality holds. It does not require P to be irreducible or all its roots to be real.

More precisely, the exact threshold is

    T_k(v)=kappa_k/[v^k theta_k detG_(sigma_k,k)],
    |P(S)|<v^(-k) iff A_k<T_k(v),

and its logarithm satisfies

    Lambda_k-k log v-k log U_k
       <= log T_k(v)
       <= Lambda_k-k log v+k log2+C.                       (20)

This gives both (2) and (3), with all constants explicit. The width of (20) is at most k log(2U)+C, an O(k) uncertainty rather than an O(k log k) uncertainty.

At the k^2 scale, if along an unbounded subsequence

    limsup log A_k/k^2 < log4,

then the complete primitive values beat every fixed rational-denominator target eventually along that subsequence. If the corresponding liminf exceeds log4, they do not beat such targets eventually.

At the critical k^2 scale, if along an unbounded subsequence

    log A_k=(log4)k^2+c k log k+O(k),

then c<1/2 suffices to beat every fixed v eventually; c>1/2 prevents beating any fixed v eventually. The case c=1/2 requires the linear-scale arithmetic and compact-weight information retained in (20). These are conditional implications, not assertions about the actual unknown A_k.

An alternative exact sufficient condition on the final content is

    g > delta F*_k D_k (v U_k)^k,

because |I_k|=delta kappa_k F*_k. A necessary condition is

    g > exp(-C) delta F*_k D_k (v/2)^k.

This reformulation preserves the tail determinant, full clearer, and final gcd. The leading-coefficient interface (20) is preferable for comparing arithmetic outputs: it cancels the huge common tail norm and identifies the precise permissible primitive scale. It does not repeat the coarser 4k^2 log k total-content budget as its conclusion.

## 6. Limitations and next useful interface

1. The unresolved arithmetic quantity is A_k=|I_k/g| with the actual ALL-coefficient gcd g. A guaranteed factorial divisor, a saturated subblock, or the leading raw norm alone does not verify (2).

2. The exact remaining analytic term is eta_k=log(detG_(sigma_k,k)/D_k), bounded in (14). A coefficient of k for the actual ratio would require a sharper limit/asymptotic for eta_k. This stage neither imports an unavailable uniform varying-weight theorem nor claims that the endpoint bump has o(k) determinant cost. The elementary O(k) comparison already resolves the requested k log k term.

3. The bounded factor theta_k remains in [exp(-C),1]. It is harmless for the two resolved scales but remains present in the exact criterion.

4. No individual-root localization or height/leading-coefficient comparability is inferred at m=k. The proof only needs the full value and exact top coefficient. The actual polynomial may have complex roots.

5. The same trace argument for compact Gram dimension n and pole order m gives

       c_m tr(G_(gamma,n)^(-1)G_[gamma(1+y)^(-m),n])
           <=(10pi^2/3)n+16m n^2(4/5)^m.

   Hence the untwisted compact determinant comparison is also O(n) when m is proportional to n and tends to infinity. For m<k, however, the leading coefficient retains a positive (k-m)-dimensional determinant with the extra weight (1+y)^(2m). The diagonal cancellation no longer removes it. No explicit proportional-regime k^2 coefficient is claimed from the present calculation; that would require a separate quantified analysis of the twisted determinant.

6. The next useful arithmetic interface is a bound or construction for the actual A_k at the boundary

       log A_k=(log4)k^2+(1/2)k log k+O(k),

   or a strict saving on either resolved scale. The next useful analytic refinement, only if that boundary becomes arithmetically accessible, is the linear term of eta_k. Different-polynomial/resultant coupling remains Main's separate scope.

No fixed/slow-growing exclusion, ultra-large-pole exclusion, historical audit, networking, dependency installation was performed in this stage. The new finite reference checks, if successful, supplement this derivation and do not verify the inherited all-degree arithmetic or positivity theorems.
