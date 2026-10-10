> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Positive reconstruction weights: universal error regime and the first depth-dependent correction

Author: Codex continuation Agent 3, 2026-10-02. Original mathematics, not independently examined. This completes the metric progress saved before the second bounded audit. It builds on FIXED_B_UNIVERSAL_FIRST_CORRECTION.md and retains the actual B-coefficient reconstruction, each coordinate endpoint, and the complete forcing residual. The exact convex-combination identity is existing archive material; the asymptotic coordinate spread and third-order depth law below are the new author deductions.

All assertions have FIXED b>=3 and d=b-1. Constants and eventual thresholds may depend on b. No growing-b tuning or uniformity claim is supplied.

## 1. Arbitrary positive diagonal rational metrics cannot change the fixed-b exponential regime

Let u=K T^(-1)fP and v=e0+K T^(-1)fQ, with the actual K=Z(I+Dpol)^(-n). For all sufficiently large n, every u_j, 0<=j<=b, is nonzero. Define the actual rational coordinate quotients

    c_j=v_j/u_j.

For ANY positive diagonal rational matrix W_n, with no restriction on its n-dependence or on weight ratios, the actual Gram center is exactly

    c_W=(u^T W_n v)/(u^T W_n u)=sum_j alpha_j(n)c_j,
    alpha_j(n)=(W_n)_jj u_j^2/sum_k (W_n)_kk u_k^2,
    alpha_j>=0, sum_j alpha_j=1.                  (1)

Coordinate zero retains its e0 term. No comparison of reduced denominators is implicit in (1).

Write sigma=sqrt(2), M=1+sigma and gamma=-(d+sigma/8). Each of the FINITELY MANY actual coordinates has the uniform expansion

    c_j-(e+pi)=(-1)^(n+1)4pi M^(-2n-b)
                        [1+gamma/n+O_b(n^-2)].    (2)

Thus, independently of all weights,

    c_W-(e+pi)=(-1)^(n+1)4pi M^(-2n-b)
                        [1+gamma/n+O_b(n^-2)].    (3)

In particular the nonzero leading logarithmic term and universal first correction cannot be canceled by a positive diagonal rational reconstruction metric at fixed b. This includes weights whose ratios grow faster than any polynomial or exponential. All coordinates have the same eventual sign, so positive convexity blocks the cancellation.

This classification is stronger than a bounded-condition-number argument: it remains valid when W_n becomes arbitrarily ill-conditioned. It does not apply to signed combinations, arbitrary off-diagonal metrics, a changed contact/reconstruction problem, or growing b. It is an analytic error-regime result, not an exclusion of shrinking primitive forms for all metrics; their denominators remain separate.

## 2. Second-order coordinate spread

Let eta_b denote the second relative coefficient for the final coordinate j=b. Set

    s_0=d, s_j=b-j for 1<=j<=b.

Then

    c_j-(e+pi)=(-1)^(n+1)4pi M^(-2n-b)
        [1+gamma/n+(eta_b-s_j)/n^2+O_b(n^-3)].     (4)

The shared coefficient eta_b is not evaluated here. All coefficients in these fixed-dimensional expansions are common to the two parities; the only leading parity dependence is the displayed sign.

For arbitrary positive weights, (1) therefore gives the sharper, uniform statement

    c_W-(e+pi)=(-1)^(n+1)4pi M^(-2n-b)
       [1+gamma/n+(eta_b-sbar(n))/n^2+O_b(n^-3)],
    sbar(n)=sum_j alpha_j(n)s_j in [0,d].          (5)

No smoothness of alpha_j(n) is required. A second-coefficient cancellation is possible only if eta_b lies in the explicit interval [0,d], and then requires an actual convex weight selection with that mean. Regardless of this interval question, the larger terms in (5) persist, so such a cancellation cannot change the exponential rate.

### Deriving (2) and (4) from actual rows

Each row j of K is led by its final-column coefficient, and that coefficient is nonzero at large n. For j>=1,

    K_(j,d)=(-1)^(d-j+1)binom(d,j-1)n^(d-j+1)[1+O_b(1/n)]
                                                        (j<=b),
    K_(j,d-1)/K_(j,d)=-s_j/(dn)+O_b(n^-2).

The j=b formula reads K_(b,d)=1 and K_(b,d-1)=0. For j=0,

    K_(0,d)=(-1)^(d+1)(n)_d,
    K_(0,d-1)/K_(0,d)=-1/(n+d-1)
                                    =-s_0/(dn)+O_b(n^-2).

Coefficients for each lower inverse row are O(n^-2) or smaller relative to the final inverse row. At leading order all inverse rows are proportional, so these lower-row contributions only rescale numerator and denominator and cancel. The next inverse-row contribution first changes a normalized selector at order n^-2. This proves (2), including its actual endpoint and complete exponential/logarithmic terms.

For the explicit second spread, use the scaled inverse/cofactor matrix Q(n) of the fixed-b note, with Q0=r l^T, r_i=binom(d,i)sigma^(-i), l_i=binom(d,i)sigma^i. Let R_d be its final row and R_(d-1) the preceding row. The exact cofactor insertion identities are

    (adj H)_(d,i)=(-1)^(d+i)det H_d <e_(d-i)(z^(-1))>,
    (adj H)_(d-1,i)=(-1)^(d-1+i)det H_d
                                 <e1(z)e_(d-i)(z^(-1))>.

These follow from the two missing-power Vandermonde alternants. Here < . > is the normalized complex d-particle functional; positivity is used only for its limiting Gaussian moments.

Put k=d-i. The first NONPROPORTIONAL perturbation of the preceding inverse row is

    (Q1)_(d-1,i)-d sigma (Q1)_(d,i)
          =sigma r_d l_i B(k),
    B(k)=[2k+2sigma d-d^2]/(4a),
    a=sigma/(2M).                                 (6)

To derive it, the extra insertion e1(exp(it_l)) is
d+iX/sqrt(n)-sum_l x_l^2/(2n)+..., X=sum_l x_l. For one term exp(-iY/sqrt(n)) in e_k(z^(-1)), Y=sum over k selected variables, the nonproportional correction is

    E[XY]+sigma E[X^2]-E[sum_l x_l^2]/2
        =k/(2a)+sigma d/(2a)-d^2/(4a).

The first two terms come respectively from the mixed insertion and the actual exp(-sigma exp(it)) odd phase. This yields (6). All common scalar cofactor corrections cancel in the displayed row difference.

For the two forcing binomial weights xminus=sigma-1 and xplus=sigma+1, E_x[k]=d/(1+x). Therefore

    sigma[E_xminus B(k)-E_xplus B(k)]=d.           (7)

Indeed (1+xminus)=sigma, (1+xplus)=sigma M, and M(2-sigma)=sigma. Normalizing the row-j reconstruction, its preceding-row coefficient -s_j/(dn) times the order-1/n nonproportional perturbation in (6)-(7) gives -s_j/n^2. Every other lower row has too small a nonproportional part to affect this order. The coordinate-zero endpoint and complete exponential forcing are factorially small relative to every fixed inverse power of the logarithmic term. Thus (4) follows.

## 3. The actual factorial depth first enters at third order

Return to the permitted actual factorial metrics

    (W_m)_jj=w_(m,j)^2,
    w_(m,j)=(n+m+1-b)!/(n+m+1-j)!,
    1<=m<=floor(d/2).

For fixed m, coordinate zero has alpha_0=O_b(n^-2), while

    alpha_(r+1)->p_r=binom(d,r)^2/binom(2d,d),
    0<=r<=d.

This limiting hypergeometric distribution has

    E[r]=d/2,
    Var(r)=d^2/[4(2d-1)].                         (8)

In particular E[s]=d/2, so the second error coefficient is eta_b-d/2 for EVERY permitted fixed m. It is independent of depth. This sharpens the preceding universal-first-correction theorem by one coefficient.

For two fixed depths m,m', the exact factorial products give, at positive row j,

    w_(m,j)^2/w_(m',j)^2
         =1-2(m-m')(b-j)/n+O_(b,m,m')(n^-2).

After normalization of (1),

    alpha_j(m)-alpha_j(m')
       =-2(m-m')[s_j-d/2]p_(j-1)/n+O_(b,m,m')(n^-2)
                                                      (1<=j<=b).

Coordinate-zero changes are too small to contribute to the following first moment at this order. Equations (8) therefore yield

    sbar(m)-sbar(m')
       =-(m-m')d^2/[2(2d-1)n]+O_(b,m,m')(n^-2).  (9)

Use the full coordinate expansion one further order. Its third coefficients are independent of m because the coordinate centers themselves do not use a weight. In their weighted difference the common leading and first terms cancel exactly; the second-coordinate spread in (4) is the first contribution. Changes of the weights of the third-coordinate terms begin only at order n^-4. Thus

    c_(n,b,m)-c_(n,b,m')
       =(-1)^(n+1)4pi M^(-2n-b)
          [(m-m')d^2/(2(2d-1)n^3)
                            +O_(b,m,m')(n^-4)].   (10)

This is the explicit first depth-dependent error correction. Equivalently the third relative coefficient is

    alpha3(b,m)=alpha3(b,1)+(m-1)d^2/[2(2d-1)].

No unknown arithmetic cancellation appears in deriving (10); it is a statement about the fully reconstructed rational centers. Their separate reduced denominators need not agree.

## 4. Consequences for parameter tuning

When m>m', (10) has the SAME eventual sign as the original error. Hence at fixed b:

- even-index centers decrease as permitted m increases, moving farther below e+pi;
- odd-index centers increase as permitted m increases, moving farther above e+pi;
- m=1 eventually minimizes the actual absolute error among the FINITE set of permitted factorial depths.

At b=3 or b=4 only m=1 is permitted, so the comparison has content from b>=5. The magnitude improvement from selecting m=1 instead of another fixed depth occurs at third relative order and does not alter the exponential rate.

Within the actual factorial family, neither the leading term, first correction nor second correction can be tuned with m. An arbitrary positive diagonal rational reweighting can modify the second-coefficient mean in (5), but still cannot remove the leading error regime. Thus this fixed-b weighting route cannot supply the desired exponential improvement while retaining the same contact/reconstruction construction.

Rational weights can also change denominator content, and the genuine denominator reduction must be analyzed for the chosen weights. No denominator equality or lower bound is inherited here. Growing b would require new uniform inverse/cofactor and coordinate-sign estimates; nothing in this paper estimates their b-dependence.

## 5. Search, attribution and remaining work

Pre-target archive queries and exact overlap are recorded in METRIC_CORRECTION_PROGRESS.md. The archived exact convexity identity was used as an input; the coordinate spread, arbitrary-weight uniformity and third-depth law are original author deductions in this continuation.

Current primary sources searched/opened for this target:
- [Garcia-Garcia and Tierz, Toeplitz minors and specializations of skew Schur polynomials](https://arxiv.org/abs/1706.02574), [full accepted PDF](https://repositorio.iscte-iul.pt/bitstream/10071/20917/1/Toeplitz%20minors_postprint.pdf). Exact Schur-insertion methodology is established literature. The specific phase/Gaussian and reconstruction calculations (6)-(10) are supplied here.
- [Wielonsky, Asymptotics of Diagonal Hermite-Pade Approximants to e^z](https://www.i2m.univ-amu.fr/perso/franck.wielonsky/8.pdf). Related strong HP remainder analysis, different family.
- [Mano and Tsuda](https://arxiv.org/html/1502.06695), [Pan and Prokhorov](https://arxiv.org/abs/2407.04852), structural determinant and fixed-size saddle overlap.

Queries: fixed size Toeplitz minors Schur polynomial insertions asymptotic expansion saddle Gaussian; Hermite Pade weighted least squares positive metric asymptotic remainder cancellation.

The absolute second coefficient eta_b is not computed. Its value is unnecessary for the exponential-regime verdict or third-depth comparison, but would decide the formal second-coefficient cancellation interval in (5). This remains a concrete possible follow-up. No global novelty, primitive-form shrinking, irrationality or rationality conclusion is asserted.

