> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Quadratic pole depth and the actual critical convergence window

2026-10-02. Original author analysis, Agent 3. This continues the exact reflected family after the proved n log n signed divergence. Determinant positivity and final-denominator arithmetic are attributed to Agent 2. No rationality conclusion for e+pi is claimed.

## Fresh target gate

Before deriving the quadratic-depth regime, archive searches covered

    reflection.*(n^2|n²|quadratic|critical)
    reflected.*(quadratic|critical|competition)
    pole.depth.*(n^2|n²)
    h.{0,20}(n^2|n²)
    laguerre.*mixture.

The broad h/n² query produced unrelated Gram heights and root-of-unity output reports. The narrowed queries produced only the present n log n note, `sources/bessel_padic_hypergeometric_zero_pade_barrier.md` Section 2.1, and `sources/root_unity_unconstrained_parity_segre_collapse_audit.md` opening results. I read the latter two: they concern respectively p-adic reflection in x(x+1) and a root-of-unity parity/Segre problem, not this growing two-pole center. The reflected finite coefficient representation and prior n log n proof are exact internal overlap. Search absence makes no global novelty claim.

Fresh primary queries:

- `site:arxiv.org Laguerre polynomials large parameters moderate deviations confluent hypergeometric`
- `site:arxiv.org binomial factorial moments Laplace asymptotic saddle Laguerre`
- `site:arxiv.org Hermite Pade exponential two point large degree critical saddle`

Opened and read the relevant parameter discussion:

- Dunster, Gil, Segura, https://arxiv.org/pdf/1705.01190, introduction/turning-point regimes. Uniform Laguerre expansions are method overlap, but the separated scaled turning-point conditions are not imported into our simultaneous limit.
- Temme, Toranzo, Dehesa, https://arxiv.org/pdf/1705.03627, Section 2 and its stated large-parameter regimes. Fixed degree at large parameter is distinct from our degree of order n^(3/2) and parameter n.
- Kuijlaars, Stahl, Van Assche, Wielonsky, https://arxiv.org/pdf/math/0510278, integral/saddle motivation in Section 3.1. Exponential Hermite-Pade saddle geometry is classical overlap; no claim about the pi endpoint is imported.

The analytic proof below instead uses the exact finite sums, their one-variable Gaussian law, and the Laguerre equation. The positive-zero fact and finite series were freshly opened earlier at https://dlmf.nist.gov/18.16 and https://dlmf.nist.gov/18.5.

## 1. Exact actual family and notation

Let n=4k tend to infinity, h>=1 integer, N=n+h, lambda=N/n², and R=sqrt(N/n). Assume lambda lies in a compact subinterval of (0,infinity). Use

    F0=(1-2w+2w²)^N/[w^(N+1)(1-w)^h], F1=wF0,
    Ri=Res0 Fi-Res1 Fi,
    Ai=Res1(e^(w-1)Fi), Bi=Res0(e^w Fi),
    T=(h-1)!, mi=T(Ai-Ri), F=m1 F0-m0 F1,
    U=T(A1R0-A0R1)>0.

The positive finite sums D,D1,C,E,A,Aplus and the Laguerre mixture B(z) are exactly those in `REFLECTED_KERNEL_NLOGN_SIGNED_DIVERGENCE.md` Section 1. With epsilon=(-1)^h,

    R0=epsilon(D-C), R1=-epsilon(D1+E),
    A0=epsilon A, A1=epsilon Aplus,
    B0=epsilon B(1), B1=epsilon B'(1),
    B(0)=D, -B'(0)=D1.

Let alpha=-B(F)/U, beta=-4 Im P(a)/U, and c=alpha+beta, where F=P'+r0/w+r1/(w-1) and a=(1+i)/2. These are the full actual outputs.

## 2. Uniform quadratic-depth residue asymptotics

Uniformly for lambda in such a compact interval,

    D1/D = R-1/4+o(1),                                      (1)
    log(D/C)=n/R+o(1),                                      (2)
    B(1)/D=exp[-R+1/4-lambda/4](1+o(1)),                    (3)
    A/C=exp[R-3/4-lambda/4](1+o(1)),                        (4)
    Aplus/A=R(1+o(1)), E/C=R(1+o(1)),                       (5)
    (log B)''(z)=-lambda/2+o(1), 0<=z<=1.                  (6)

In particular B(1)>0 eventually. The complete normalization is

    U/T=2R D A(1+o(1)).                                    (7)

On a fixed compact lambda interval, the additive o(1) remainders in (1)-(4) and (6), and the relative remainders in (5)-(7), can all be bounded by O(n^-1/2). The Gaussian proof below has third standardized derivative O(n^-1/2), fourth standardized derivative O(n^-1), and integrable central Gaussian moments; the Laguerre reciprocal-cube remainder has the same O(n^-1/2) bound. This quantitative bound also applies to the two separate relative remainders in (12). The error term in (2) therefore tends to zero; it is not merely o(sqrt(n)). The constant terms in (3)-(4) determine the critical window below.

### Proof of the binomial constants

On X=N-2l>=n+1 interpolate the product weights

    p_t(X)=binom(N,(N-X)/2) product_(j=1)^n(X+t j)/n!,
    -1<=t<=1.

The t=1 and t=-1 partition sums are D and C, apart from the negligible D range X<=n. Stirling differentiation and strict concavity give a unique saddle

    X_t=nR-t n/4+O(R+n/R),

uniformly in t, and variance (N/2)(1+o(1)). The mean differs from the saddle by O(R), hence its mean divided by n is

    E_t X/n=R-t/4+o(1).                                  (8)

Indeed the saddle equation to order R^-2 is

    -X/N+sum_(j=1)^n 1/(X+t j)=0,

whose substitution X=nR+a n gives -2a-t/2=0. The third logarithmic derivative times N^(3/2) is O(n^-1/2), supplying the local Gaussian law and moment generating function convergence. The lattice spacing 2 is negligible. Concavity and Stirling estimates give Gaussian central tails and exponential bounds beyond a fixed relative neighborhood. The endpoint range X<=n is down by exp[-n log R+O(n)]. These estimates are uniform for bounded linear tilts in X/(n+1).

For the logarithmic partition derivative, the same expansion, with the Gaussian moments retained, gives

    E_t sum_(j=1)^n j/(X+t j)
       =n/(2R)-5t n/(24R²)+O(n/R³+1/R).

The term odd in t integrates to zero from -1 to 1. Since R is of order sqrt(n), its remaining error is o(1). Integrating proves (2). Taking t=1 in (8), and changing n to n+1 in the normalization, proves (1). Taking t=-1 gives E_C X/(n+1)=R+1/4+o(1).

### Proof of the Laguerre constants without a positivity substitution

On any fixed central range X/(nR) bounded above and below, normalize

    Q_m(z)=L_m^(n)(z)/binom(m+n,n), mu=m/(n+1).

The reciprocal root sums from the differential equation are

    s1=mu,
    s2=(mu²+mu)/(n+2),
    s3=(2mu+1)(mu²+mu)/[(n+2)(n+3)].

Here mu is of order sqrt(n), s2=lambda+o(1), and s3=O(n^-1/2). Positivity of Laguerre roots implies the smallest root is at least s3^(-1/3), which tends to infinity. The product over roots therefore proves, with two z derivatives and uniformly for bounded z,

    log Q_m(z)=-mu z-(mu²+mu)z²/[2(n+2)]+o(1).             (9)

The central D measure has

    r=E_D mu=R-1/4+o(1), Var_D mu=lambda/2+o(1),

and its centered moment generating functions converge to the Gaussian ones. The second term in (9) is -lambda z²/2+o(1) on that measure. Combining it with the Gaussian moment generating function gives

    B(z)/D=exp[-r z-lambda z²/4](1+o(1))                 (10)

with two z derivatives. This proves (3) and (6).

The C mixture for A uses m=X-n-1, so its mean mu is R-3/4+o(1), with the same variance lambda/2. Substitution z=-1 in (9) gives (4). The positive (X,k) coefficient sum defining A has its corresponding Aplus term divided by that A term exactly X/(n+1+k). Its k scale is O(sqrt(n)), and its X/n scale is R(1+o(1)); hence (5).

It remains to control the noncentral Laguerre terms, since B is not defined by an arbitrary positive-modulus replacement. The finite series gives |Q_m(z)|<=exp(|z|m/(n+1)), and analogous polynomial-times-exponential derivative bounds. Together with the binomial/product concavity estimates, this makes the outer tails negligible relative to the central mass, even after the exp(O(sqrt(n))) forcing tilt. At the remote X of order N the binomial large-deviation loss is of order N while that bound is only exp(O(n)). Central Q_m is positive on [0,1]; the possibly signed remote polynomial contributions are exponentially negligible. This proves eventual positivity of the actual mixture and justifies (10) and its derivatives. It does not replace an oscillatory contour by a modulus ensemble.

Finally, C/D=exp[-n/R+o(1)] tends to zero. In

    U/T=Aplus(D-C)+A(D1+E),

equations (1)-(5) give (7), independently of whether A is larger or smaller than D.

## 3. Full actual alpha: the two competing terms

The exact projected numerator is

    B(F)/T=D1 B(1)+D B'(1)
              +Aplus B(1)-A B'(1)+E B(1)-C B'(1).          (11)

By (6), its first pair is

    -[lambda/2+o(1)] D B(1).

The next pair, after division by U/T, is (1+o(1))B(1)/D. The last pair is smaller by C/A, which tends to zero by (4). Equations (2)-(4) also give

    B(1)/A=e exp[n/R-2R](1+o(1)).

Consequently the ACTUAL alpha has the uniform additive asymptotic

    alpha = e [R/(4n)] exp[n/R-2R](1+o(1))
               -exp[-R+1/4-lambda/4](1+o(1)),             (12)

where the total remainder is o of the sum of the two displayed positive magnitudes. Near lambda=1 the two terms can compete after a finer shift, so (12) is not advertised as a relative one-term expansion at that cancellation. Near lambda=1/2 the second term is exponentially negligible, and the first term is the complete leading alpha.

## 4. Both actual primitive endpoints remain controlled

For the complete upward segment from bar(a) to a,

    J_i=-2i integral Fi(w)dw,
    |J0|<=4*2^h, |J1|<=2*2^h.

This is the direct bound for F0=(2V/w)^n(2V/[w(1-w)])^h/w: on the segment |2V/w|<=1 and 0<=2V/[w(1-w)]<=2. Both endpoints are included. The exact period identity is

    pi-beta=(m1J0-m0J1)/U.

Now |mi|/T=O(R(D+A)), while U/T~2RDA. A central binomial term gives log D and log C equal to N log2+n log R+O(n), and A>=C. Hence uniformly in this quadratic regime

    |pi-beta|<=O(2^h(1/A+1/D))
               <=exp[-n log R+O(n)]
               =exp[-(n/2)log n+O(n)].                  (13)

The full exponential contour at both poles is exactly B(F)+e U. Thus the COMPLETE signed target error is

    e+pi-c=e-alpha+pi-beta,                              (14)

with alpha given by (12) and the two-endpoint term bounded by (13).

## 5. Phase limits and an explicit convergent critical sequence

If lambda tends to a fixed kappa<1/2, the first term of (12) diverges positively and dominates the second: c tends to positive infinity. If lambda tends to kappa>1/2, both displayed terms tend to zero, so c tends to pi and e+pi-c tends to e. At lambda tending to 1/2, the ratio limit alone gives no verdict; a smaller shift changes the finite limit.

For the unshifted choice N=n²/2+O(1),

    alpha=e/(4sqrt(2n))(1+o(1)), c->pi.

For a prescribed real theta, put

    L_n=(1/2)log n+log(4sqrt(2))+theta,
    R*_n=[sqrt(L_n²+8n)-L_n]/4,
    N_n=nearest integer to n(R*_n)², h_n=N_n-n.           (15)

These are valid positive integer depths for all sufficiently large n=4k. R*_n solves n/R*_n-2R*_n=L_n. Changing N by at most 1/2 changes that expression by O(n^-3/2); lambda_n tends to 1/2. Therefore (12)-(14) prove

    alpha_n -> exp(1+theta), beta_n -> pi,
    c_n -> pi+exp(1+theta),
    e+pi-c_n -> e-exp(1+theta).                           (16)

In particular theta=0 gives an explicit sequence of the ACTUAL rational centers converging to e+pi. Its depth is

    h_n=n²/2 - n^(3/2)log n/(4sqrt(2))
             -[log(4sqrt(2))+theta]n^(3/2)/(2sqrt(2))
             +O(n log² n).                              (17)

For the closed formula (15), the prefactor sqrt(lambda)/4 differs from its limit 1/(4sqrt(2)) by O(log n/sqrt(n)). Thus theta=0 gives |c_n-(e+pi)|=O(log n/sqrt(n)); (13) is much smaller. A sharper explicit implicit rule retains that prefactor: solve

    Psi(n,N)=n/R-2R+log(R/(4n))=theta, R=sqrt(N/n),

for positive real N near n²/2, then take the nearest integer N. The derivative with respect to N is -1/(2R³)-1/(nR)+1/(2N), of order -n^-3/2. This exact leading curve gives c->pi+exp(1+theta), and at theta=0 it restores |c_n-(e+pi)|=O(n^-1/2). The displayed closed rule remains valid for the limits (16)-(17). The signed finer residual at theta=0 is not determined by either leading rule. No monotonicity between consecutive integer depths, exponentially small rounding error, or irrationality criterion is inferred from (16).

## 6. Complete primitive denominator ledger

Retain Agent 2's exact final primitive formula. Write O_N for the odd part of lcm(1,...,N), E_raw=N! B(F), and Pi_raw=4 Im P(a). Then

    q=N! O_N U / gcd(N! O_N U,
                       O_N E_raw+N! O_N Pi_raw).          (18)

This includes the factorial at the deeper origin pole, projection content, and BOTH primitive endpoints. Agent 2's all-h parity theorem, Section 5 of `REFLECTION_DISTRIBUTED_POLE_REPAIR.md`, proves

    v2(q)=v2(N!)+v2(U)>=v2(N!)+1,
    q>=2^(N-s2(N)+1).                                   (19)

The normalization (7) preserves T=(h-1)!; it does not silently remove that integer factor from (18). Analytically,

    log U=log((h-1)!)+2N log2+2n log R+O(n).

At the theta=0 critical convergence sequence, the compulsory actual denominator satisfies

    liminf log q/n² >= (log2)/2.                         (20)

Convergence in (16) therefore leaves a substantial arithmetic need: to obtain q|e+pi-c|->0 one would have to prove actual nonzero tuned errors smaller than exp[-(log2/2+o(1))n²], together with whatever larger primitive q survives. The present finite-sum expansion proves convergence and the full phase interface, not that error rate. A generic estimate, a choice of real theta, or the small change in the formal exponent caused by one integer step cannot be substituted for a lower or upper theorem about that much finer actual lattice residual.

For theta!=0, or for either fixed noncritical phase, the complete target error has a nonzero limiting magnitude or diverges. Equations (19)-(20) then prove q|e+pi-c| diverges on those sequences. For the convergent theta=0 sequence neither the closed-rule O(log n/sqrt(n)) nor exact-curve O(n^-1/2) upper estimate proves or disproves q|e+pi-c|->0; a polynomial upper bound must not be turned into a lower bound. That finer actual residual is the separate discrete-lattice question.
