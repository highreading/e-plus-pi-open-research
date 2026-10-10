> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# M34 proper large pole: complete coefficient perturbation and no-small-form window

Author: Agent 3 / analysis, 2026-10-02. Original bounded analytic result. Fresh archive and primary-literature gate: PROPER_LARGE_POLE_FULL_STACK_GATE.md. Root owns the proper moment/period identity, exact rational alpha recurrence, prefix denominator clearers, limiting coefficient algebra and actual primitive content. This note proves the complete limiting-root mechanism, uniform FULL coefficient perturbation, and a scale/gcd-independent no-small-form conclusion in an explicitly ultra-large window. It does NOT claim this for arbitrary m/k tending to infinity.

## 1. Full proper moment interface and actual limit polynomial

Let mu(y^r)=D_(2r), with mu the probability pushforward of exp(-t)dt under y=(1-t)^2. Let sigma_e be the compact exponential measure

    sigma_e(f)=integral_0^1 exp(x)f(x^2)dx,
    g_r=sigma_e(y^r)=eD_(2r)-(2r)!.

Root's proper regime is m>=3k-1, so every used moment 0<=r<=R=3k-2 is proper. With c_m=4^m/binom(2m-2,m-1), the response equals the positive probability measure

    nu_m(f)=c_m/(2pi) integral_0^infinity
                                    f(x^2)(1+x^2)^(-m)dx,
    nu_(m,r)=product_(j=1)^r(2j-1)/(2m-2j-1), nu_(m,0)=1.

Define the ENTIRE pole tail

    T_(m,r)=c_m integral_1^infinity x^(2r)(1+x^2)^(-m)dx.

Then the actual compact pole moment is2pi nu_(m,r)-T_(m,r), and its rational part alpha_(m,r) satisfies Root's exact identity

    alpha_(m,r)=pi nu_(m,r)-T_(m,r).

Thus the COMPLETE fixed-width polynomial is

    beta_(k,m)(s)=det[C_m;R_m+s V_m],
    C_(i,j)=D_(2(i+j))-nu_(m,i+j),
    (R_m+sV_m)_(i,j)
              =-(2i+2j)!+(s+pi)nu_(m,i+j)-T_(m,i+j),
    0<=i<k, 0<=j<2k.                                      (1)

The pi-containing representation in (1) is an exact real expression for the rational moments; it is not a claim of irrational rational coordinates. The tail cancels the pi part to give Root's actual rational alpha. At S=e+pi, adding the full eC rows gives the actual physical compact block. Both exponential and pole contributions, and all tail terms, remain included.

For each fixed k, the coefficientwise limit is the actual affine polynomial

    beta_(k,infinity)(s)
          =det[mu-delta_0; -(2r)!+(s+pi)delta_(r,0)]
          =det[mu-delta_0; sigma_e+(s-e+pi)delta_0].        (2)

No claim of rank-m gain survives this limit. In particular the point mass occurs at0, and the shift is s-e+pi; changing either sign would change the complete target.

For k>=24, define strictly positive COMPLETE mixed coefficients

    D_k=(-1)^k det[mu-delta_0;sigma_e],
    B_k=(-1)^k [z]det[mu-delta_0;sigma_e+z delta_0].

The proof below gives

    beta_(k,infinity)(s)=b_k(s-s_(k,infinity)),
    b_k=(-1)^k B_k!=0,
    s_(k,infinity)=e-pi-d_k,  d_k=D_k/B_k>0.                (3)

Root's limiting coefficient algebra, also apparent by taking the s coefficient of the integer moment matrix in the first line of (2), makes b_k a NONZERO INTEGER. Therefore |b_k|>=1. The constant coefficient can contain pi in the limit, even though each finite-m polynomial has rational coefficients.

## 2. Limiting conditional positivity and endpoint normalization

Put rho_0=mu-delta_0 and

    F_k(x)=det M_[rho_0 product_i(y-x_i),k].

The inherited Gamma tail comparison applies to compact nodes x_i in[0,1]. With

    C_k=3exp(-2k-1)(k^2-1)^(k-1)/[4k16^(k-1)],
    L=sup_[-1,1]|p|^2,

the positive tail for k-1 nodes is at least C_k L, while the complete negative compact mu contribution and the delta_0 contribution sum to at most2^k L. For k>=24, C_k>2^k by the exact threshold proof in the preceding short-family notes. For full k-node configurations the positive tail gains k^2-1, while the total negative bound is at most2^(k+1)L. Thus F_k(x)>0 for ALL compact configurations.

The complete compact-node identities are

    D_k=1/k! integral_[0,1]^k Vand(x)^2 F_k(x) d sigma_e^k,
    B_k=1/(k-1)! integral_[0,1]^(k-1) Vand(x)^2
                             product_i x_i^2 F_k(x,0)
                                             d sigma_e^(k-1). (4)

They prove D_k,B_k>0, including the entire limiting compact exponential density. The point insertion0 kills the upper delta: F_k(x,0)=det M_[mu y product_i(y-x_i),k]. Both coefficients in (4) are genuine full determinant/cofactor quantities.

For k>=100 the same conditional-root proof gives all roots z_j>A=ak^2, a=1/(48e^4). Its negative bound for rho_0((y-A)Qp^2) includes BOTH the mu compact contribution and the point0 term; each is bounded before comparison with the Gamma tail. For any final compact node0<=u<=1,

    exp(-2k/A)<=F_k(x,u)/F_k(x,0)<=1.

Replacing all k nodes by0 yields

    L_*=exp(-2/a)<=F_k(x)/F_k^0<=1,
    F_k^0=det M_[mu y^k,k]>0.                              (5)

Let Lambda_(sigma_e,k)(0) be the ordinary endpoint Christoffel minimum for the ACTUAL exponential compact measure and degree<k. Equations (4)--(5) give

    L_* Lambda_(sigma_e,k)(0)
                  <=d_k<=L_*^(-1)Lambda_(sigma_e,k)(0).     (6)

For dgamma=y^(-1/2)dy, the reference endpoint kernel is

    K_(gamma,k)(0)=sum_(l=0)^(k-1)
              (2l+1/2)[binom(2l,l)/4^l]^2.

The elementary recurrence for the central binomial ratio gives binom(2l,l)/4^l>=1/(2sqrt(l)) for l>=1; hence K_(gamma,k)(0)>=k/2. Since dsigma_e<=e dgamma/2,

    d_k<=e exp(2/a)/k.                                    (7)

For the matching lower bound, the same ratio recurrence gives binom(2l,l)/4^l<=1/sqrt(l+1), hence K_(gamma,k)(0)<=2k. Since dsigma_e>=dgamma/2, equations (6) give d_k>=exp(-2/a)/(4k). Thus d_k is of order1/k with explicit absolute comparisons, and the surviving finite root tends e-pi, rather than S.

A deliberately coarse explicit threshold sufficient for the later deduction is

    K_*=max(100,ceil[4e exp(2/a)]).

For k>=K_*, d_k<=1/4. The elementary bounds3<pi<22/7 and8/3<e<11/4 imply1/4<pi-e<1/2, so

    -3/4<s_(k,infinity)<0,
    |s_(k,infinity)|<1,
    |beta_(k,infinity)(S)|/H(beta_(k,infinity))
                               =2pi+d_k>2pi>6.            (8)

Here H is the coefficient maximum, also meaningful for the real limit polynomial. The threshold in (8) is explicit and coarse; it is not silently replaced by a small numerical k.

## 3. Uniform FULL coefficient perturbation with the ENTIRE tail

For any real polynomial p, put ||p||_1=sum_j|[s^j]p|. This norm is submultiplicative. Assume k>=24 and m>=6k. For every used r>=1,

    0<nu_(m,r)<=nu_(m,1)=1/(2m-3),                         (9)

because the consecutive moment ratios are at most1 for r<=R<=m/2. The zeroth response remains exactly1.

For x>=1,1+x^2>=2x. Therefore EVERY used tail satisfies

    0<=T_(m,r)<=c_m2^(-m)/(m-2r-1)<=8m2^(-m).             (10)

This is the full tail, not just its zeroth moment. The central-binomial maximum bound gives c_m<=8m. For m>=16,8m^2 2^(-m)<=1; the assertion holds at16 and its consecutive ratio is less than1. Also5/(2m-3)<=3/m for m>=9. Since pi+1<5, the polynomial coefficient norm of EVERY entry difference between the finite matrix (1) and its limit is at most

    5/(2m-3)+8m2^(-m)<=4/m.                               (11)

Top entries satisfy the still smaller response difference in (9). Thus BOTH row blocks are controlled. No fixed-k moment convergence was used as a uniform inverse-conditioning estimate.

Set the completely explicit quantities

    M_k=(6k)!+5,
    L_k=8k(2k)![M_k+1]^(2k-1).                            (12)

Every limit-matrix entry has polynomial norm at most M_k: its largest factorial/derangement index is6k-4, and the constant pi plus linear response adds less than5. With N=2k and delta=4/m<=1, determinant multilinearity and the N! permutation terms give

    ||beta_(k,m)-beta_(k,infinity)||_1
      <=N![(M_k+delta)^N-M_k^N]
      <=N! N delta (M_k+1)^(N-1)
      =L_k/m.                                              (13)

This is the FULL coefficient vector in the original s variable, including every coefficient up to the actual degree, not merely a bound at S. Relative to the ACTUAL limiting nonzero slope,

    epsilon_(k,m):=||beta_(k,m)-beta_(k,infinity)||_1/|b_k|
                              <=L_k/(m|b_k|)<=L_k/m.       (14)

The sharper expression with |b_k| is retained for Root's coefficient algebra; using |b_k|>=1 only supplies a conservative universal threshold. In particular

    log L_k=12k^2 log k+O(k^2),                             (15)

with an absolute constant. This bound is deliberately not a claim about the actual primitive height or final gcd.

## 4. Actual roots: one bounded root, all others outside bounded regions

The degree of beta_(k,m) is at most k because only its k lower rows depend on s. For every fixed k>=24, (13) proves coefficientwise convergence to the NONZERO affine polynomial (3). Rouché's theorem on any fixed circle of radius R>|s_(k,infinity)| therefore gives exactly one root inside that circle for all sufficiently large m. It converges to s_(k,infinity). Every other root, IF PRESENT, leaves every fixed bounded region. No unproved assertion of exact finite-m degree k is needed.

There is also an explicit uniform statement. Suppose k>=K_* and epsilon_(k,m)<=6^(-k). On |s|=6, the limit polynomial has modulus at least|b_k|(6-3/4), while the perturbation is at most|b_k|epsilon6^k<=|b_k|. Thus the actual polynomial has EXACTLY ONE root inside |s|<6.

If epsilon is zero the polynomial equals its affine limit and its unique root is the limit root. Otherwise, around the finite limit root take the circle |s-s_(k,infinity)|=2epsilon. Its points have |s|<1, so the perturbation is at most|b_k|epsilon and the limiting term has modulus2|b_k|epsilon. Hence the unique bounded actual root satisfies

    |s_(k,m)-s_(k,infinity)|<=2epsilon_(k,m).               (16)

It is REAL and simple: the coefficients are real, and a disk symmetric about the real axis contains exactly one root counted with multiplicity. It is negative, since its limiting center has absolute value greater than1/4 and2epsilon<=2·6^(-k)<1/4. All other roots, if present, have modulus greater than6. In particular this ultra-large-m regime supplies no actual root approaching S, which lies in(0,6), while the unique bounded root stays negative. The conclusion refers to this specified window, not arbitrary m/k tending to infinity.

## 5. COMPLETE primitive no-small-form deduction independent of gcd

Take

    k>=K_*,
    m>=max(6k,ceil[6^k L_k/|b_k|]).                        (17)

Then epsilon<=6^(-k). A purely explicit sufficient version, requiring no information about the magnitude of the actual slope, is

    m>=6^k L_k.                                            (18)

Using S<6, the value error and actual coefficient height obey

    |beta_(k,m)(S)-beta_(k,infinity)(S)|
                         <=|b_k|epsilon6^k<=|b_k|,
    H(beta_(k,m))<=|b_k|(1+epsilon)<=2|b_k|.

Equation (8) then implies

    |beta_(k,m)(S)|>|b_k|(2pi-1)>5|b_k|
                                      >H(beta_(k,m)).       (19)

Let P be ANY final primitive integer polynomial obtained by nonzero scalar integerization of this actual beta, after its COMPLETE final common content. Both value and coefficient height scale by the same absolute factor, so (19) survives EXACTLY:

    |P(S)|>H(P)>=1.                                        (20)

Thus these complete primitive forms cannot be small, regardless of their final gcd. This statement concerns the present fixed-width determinant polynomials; it is not a restriction on arbitrary widened polynomial directions or unrelated constructions.

The conservative sufficient threshold has log m at least12k^2 log k+O(k^2), with the additional k log6 included in (18). No result here closes the entire domain m/k->infinity, the proportional-large-pole transition, or a polynomial-sized m window. Root's exact proper clearers and tail recurrence remain separate from this analytic coefficient-norm estimate.

## 6. Bounded-route completion and Genesis readiness

The current bounded M34 route is complete: full limit polynomial, signed positive limiting coefficients at k>=24, finite-root limit e-pi-d_k, explicit whole coefficient perturbation retaining the tail, uniform root-count thresholds, and a FINAL primitive no-small-form deduction independent of gcd. No missing step is concealed in an inverse-conditioning assumption.

Human Genesis steering now requests fundamentally different mechanisms and discards essential public-literature routes after these bounded current tasks finish. No further extension of this moment/determinant route is started here. Ready for Root's next original target and novelty coordination. The main e+pi problem remains unresolved.
