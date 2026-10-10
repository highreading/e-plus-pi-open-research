> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Proportional review and quantitative estimate, stage 6

Status: limited independent review of Main's Stage 8, conditional on inherited complete insertion and nonvanishing identities; separate original author proof of a quantitative determinant estimate. The new quantitative proof has not received independent review. S denotes the actual e+pi. No favorable arithmetic content bound or irrationality conclusion is established.

## 1. Scope and source

Primary source read in full through the controller: work/parallel_batch_01/main/PROPORTIONAL_VARIATIONAL_THRESHOLD_STAGE8.md. Historical complete moment, insertion, and nonvanishing identities are inherited hypotheses. Earlier endpoint-scale and multiplicity work is not repeated or reviewed.

Fix 0<rho<1, m=ceil(rho k), r=k-m, and assume k is sufficiently large that r>=1 and the inherited threshold k>=131072 holds. Set tau=m/k and s=r/k=1-tau. For K=[1/2,1], define

 Z_(r,m)=D_r(x^(2m)dx on K),
 E_tau(mu)=double integral log|x-z| dmu(x)dmu(z)+2tau integral log|x| dmu(x).

On the real interval the absolute value in the external logarithm is unnecessary; it is retained when extending the functional to the plane below.

## 2. Limited review of Stage 8

Singular-weight comparison: VALID. If deg p<r, q=(1+y)^m p has degree below k, so its squared supremum is at most k^2 times its Lebesgue squared norm by the shifted Legendre kernel. Splitting at y=k^(-2) gives contributions at most 2k and k times that norm. The lower comparison follows from y^(-1/2)>=1. Applying the actual sigma_m multiplier therefore gives exactly

 2^(-r)H_(r,m)<=J_(r,m)<=[3k(e+c_m)/2]^r H_(r,m).

This handles the singularity on the actual polynomial subspace and does not assume a bounded density ratio.

Change of basis: VALID. For y=2x-1, the measure contributes 2^(2m+1) to each of r rows of the Gram scaling. The polynomial basis has triangular diagonal 2^i, i=0,...,r-1, contributing its determinant squared, 2^(r(r-1)). The total exponent is 2mr+r^2, as stated.

Empirical upper bound: VALID. The empirical measure has mass r/k, not one. Including its diagonal in the cutoff energy introduces -rM in the exponent; restoring it requires +rM. For fixed cutoff M the changing masses and m/k converge in a compact space after normalization. Decreasing cutoff maxima converge to the true maximum: extract maximizers along increasing cutoffs, test their weak limit at every fixed cutoff, and then let that fixed cutoff increase. This proves the asserted interchange and only an o(k^2) error by that argument alone.

Jensen lower bound: VALID with its stated probability normalization. The pair count is r(r-1), the external term is 2mr, and the Lebesgue-to-probability conversion contributes minus r times the entropy. The candidate has inverse-square-root endpoint bounds, including at the transition; its logarithmic energy and entropy are finite. For a fixed candidate at rho, rounding changes the quadratic coefficients by O_rho(k), which disappears after division by k^2. The quantitative proof below instead uses tau=m/k, avoiding rounding until the end.

Candidate and potential inequality: VALID. For a=max(1/2,tau^2), omega_a is the arcsine probability measure and eta_a=(sqrt(a)/x)omega_a is a probability measure. The density of mu_tau=omega_a-tau eta_a is nonnegative since tau<=sqrt(a), and its mass is 1-tau. The displayed Stieltjes transforms have the branch behaving as z at infinity; on the left real component their square root is negative. Thus in the detached-support case the weighted-potential derivative is (1-a/x)/[-sqrt((a-x)(1-x))]>0. The potential is below its support constant on the omitted interval, in the correct direction for a maximum problem.

Zero-mass energy: the conclusion is VALID, but the phrase about truncation and smoothing in Stage 8 compresses an integrability step. An explicit proof without an imported asymptotic or potential-theory theorem is given in Section 4 below. The candidate has a bounded logarithmic potential by the interval-mass bound there, so every finite-energy competitor has finite mutual energy with it. This supplies the missing justification needed to expand the signed energy and pass through the regularization. Competitors of energy minus infinity cannot improve the maximum.

Energy evaluation and branches: VALID. Write C_a=log((1-a)/4), L_a=2log((1+sqrt(a))/2). The support weighted potential is ell_tau=s C_a+tau L_a, and integral log x dmu_tau=(1+tau)L_a-tau log a. Consequently

 E_tau(mu_tau)=s^2 C_a+2tau L_a-tau^2 log a.

Adding log4+(1-tau^2)log2 gives both stated Phi branches. At the transition they agree. This is a property of the auxiliary determinant, not an arithmetic or polynomial-root assertion.

Optimizer: VALID. On the first branch the derivative is positive through 1/sqrt(2). On the second branch Phi''=2log((1-tau^2)/(8tau^2))<0. Its derivative starts positive and tends to -2log2 as tau tends to one. Thus there is exactly one maximum in the stated open interval. The claim is analytic optimization only.

No normalization or formula correction is required. The finite-energy passage is expanded below rather than silently treated as an unavailable theorem.

## 3. Original result and explicit two-sided bounds

Let mu=mu_tau, let nu=mu/s have density f, and define

 L_tau=double integral log|x-z| dnu(x)dnu(z),
 h_tau=integral f log f dx,
 M_tau=8/sqrt(1-a), a=max(1/2,tau^2).

For k>=2, r>=1, the following estimates hold:

 k^2 E_tau(mu)-r L_tau-r h_tau-log(r!)
 <=log Z_(r,m)
 <=k^2 E_tau(mu)+2r log k+2pi s M_tau k+8s tau-r log2-log(r!).       (1)

In particular, for tau in any fixed compact subinterval of (0,1),

 log Z_(r,m)=k^2 E_tau(mu_tau)+O(k log k),                         (2)

with a uniform constant on that compact interval. This includes compact intervals crossing 1/sqrt(2). Neither endpoint tau=0 nor tau=1 is included in this uniformity statement. The lower estimate is Jensen; the new upper estimate uses explicit circle regularization, not weak convergence.

## 4. Interval mass, logarithmic integrability, and signed energy

The candidate satisfies 0<=mu<=omega_a. The arcsine density on an interval of length 1-a has interval mass bounded by a constant times the square root of interval length divided by 1-a. To see this directly, scale to [0,1], split at 1/2, and bound 1/sqrt(t(1-t)) by sqrt(2)/sqrt(t) on the left and by sqrt(2)/sqrt(1-t) on the right; integrate on an interval, whose integral is largest when pushed toward the relevant endpoint. The deliberately generous constant above gives, for every real x and h>0,

 mu({t:|t-x|<h})<=M_tau sqrt(h).                              (3)

The same bound holds for complex centers, since projection onto the real line only enlarges the set. Layer integration gives a uniform finite bound for integral -log|z-t| dmu(t) when all distances are at most one, since integral_0^infinity M_tau exp(-u/2)du=2M_tau. In particular the candidate's potential is finite and bounded on K and its mutual energy with every finite measure on K is finite.

For the signed-energy fact, let delta be a compactly supported real signed measure of mass zero whose logarithmic kernel is absolutely integrable against |delta| tensor |delta|. Use

 -log d=(1/2) integral_0^infinity [exp(-td^2)-exp(-t)]dt/t, d>0.

First integrate over a finite t-interval. The constant term vanishes because delta has mass zero. The Gaussian kernel exp(-t|z-w|^2) is positive definite in the plane: its Fourier transform is a nonnegative Gaussian, so its quadratic integral against a real signed measure is nonnegative. Therefore the truncated quadratic integral for -log is nonnegative.

For each fixed d, the integrand in brackets has a constant sign as a function of t. Its truncated integral in absolute value is at most the absolute value of the full integral, namely |log d|. Dominated convergence under the stated logarithmic integrability gives

 double integral log|z-w| ddelta(z)ddelta(w)<=0.                (4)

Finite-energy positive competitors on K have finite absolute logarithmic self-energy because distances there are at most 1/2. The bounded candidate potential proves mutual integrability. Thus (4) applies to competitor minus candidate and proves Main's maximality assertion from the potential inequality. It also applies to the circle measures used below: their self- and mutual logarithmic integrals are finite by the circle mean formula, and their mutual integrals with mu are finite by (3). No smoothing theorem is required.

## 5. Quantitative extension of the equilibrium inequality

Let U_mu(z)=integral log|z-t|dmu(t). If x is real and |z-x|<=epsilon, the triangle inequality gives

 U_mu(z)-U_mu(x)<=integral log(1+epsilon/|x-t|)dmu(t).

Apply layer integration to the right side and then (3):

 integral log(1+epsilon/|x-t|)dmu(t)
 <=M_tau sqrt(epsilon) integral_0^infinity (exp(u)-1)^(-1/2)du
 =pi M_tau sqrt(epsilon).                                   (5)

The last integral equals pi by the substitution exp(-u)=v. All integrands are nonnegative, so Tonelli applies.

For x in K and epsilon<=1/4, |z|>=1/4 and

 |log|z|-log x|<=4epsilon.

The verified real equilibrium inequality U_mu(x)+tau log x<=ell_tau therefore implies throughout the epsilon-neighborhood of K

 U_mu(z)+tau log|z|<=ell_tau+delta_epsilon,
 delta_epsilon=pi M_tau sqrt(epsilon)+4tau epsilon.            (6)

On the support of mu equality with ell_tau holds. For any positive measure eta of mass s in this neighborhood for which the energies are finite, expansion and (4) yield

 E_tau(eta)-E_tau(mu)
 =2 integral [U_mu+tau log|z|]d(eta-mu)+E_0(eta-mu)
 <=2s delta_epsilon.                                         (7)

The plane extension is only a regularization device; it does not change the real equilibrium problem or assert a new maximizing measure in the plane.

## 6. Circle regularization and all finite terms

For integration nodes x_1,...,x_r in K, replace each node by the uniform probability measure sigma_i on the complex circle of radius epsilon centered at x_i, and set eta=(1/k)sum_i sigma_i. Its mass is exactly r/k=s.

The elementary circle mean identity is

 integral log|z-(x+epsilon exp(it))|dt/(2pi)
 =log max(|z-x|,epsilon).

It follows from the convergent logarithmic power series when one radius is strictly smaller than the other and then by continuity at equality. It gives each circle's self-energy exactly log epsilon. Averaging successively over two circles gives mutual energy at least log|x_i-x_j|: after one average replace log max(distance,epsilon) by the smaller log distance, and average again. Also, if epsilon<x_i, the mean of log|z| on the circle is exactly log x_i.

Let

 H=2sum_(i<j)log|x_i-x_j|+2m sum_i log x_i.

Using tau=m/k and the circle identities gives

 H<=k^2 E_tau(eta)-r log epsilon
 <=k^2 E_tau(mu)+2s k^2 delta_epsilon-r log epsilon.             (8)

The subtracted self-energy is essential. At coincident nodes the original integrand vanishes, so the inequality remains valid in its extended interpretation. Circle overlaps do not cause an infinite energy: the same mean formula gives finite mutual circle energy bounded below by log epsilon.

Choose epsilon=k^(-2), valid for k>=2. Then (8) becomes

 H<=k^2 E_tau(mu)+2r log k+2pi s M_tau k+8s tau.

The determinant integral is exactly (1/r!) integral_(K^r) exp(H) dx. Its integration volume is (1/2)^r. Taking the supremum bound retains both finite factors and proves the upper half of (1), including -r log2-log(r!). No asymptotic theorem is used.

## 7. Jensen lower bound and uniform constants

Express Lebesgue measure on the support of mu as f^(-1)dnu. Its endpoint exceptions have measure zero; the candidate is positive in the support interior. Jensen gives exactly

 log Z>=-log(r!)+r(r-1)L_tau+2mr integral log x dnu-rh_tau.

Because r=ks and m=k tau, the two quadratic terms with r^2 in place of r(r-1) equal k^2 E_tau(mu). This proves the lower half of (1).

The integrability needed for Jensen is absolute integrability of each logarithmic term. Pair logarithms follow from (3), external logarithms are bounded on K, and entropy follows from the explicit density bound

 f(x)<=1/[s pi sqrt((x-a)(1-x))].

For tau in a compact interval inside (0,1), s and 1-a are bounded below. Substitution x=a+(1-a)t bounds the positive entropy uniformly by an integrable multiple of [t(1-t)]^(-1/2) times 1+|log t|+|log(1-t)|. Its negative part is bounded using -u log u<=1/e for 0<u<=1 and the bounded support length. The same compact parameter bounds and (3) bound |L_tau| uniformly. Thus (1) proves (2) uniformly, including across the support transition. This uniformity is a proved domination statement, not an inference from continuity of a formal energy formula.

## 8. Rounding and actual finite-k threshold

The explicit formula E_tau(mu_tau)=s^2 C_a+2tau L_a-tau^2 log a is locally Lipschitz on (0,1). Each branch is smooth away from the transition and has bounded one-sided derivatives at the transition; the formulas agree there. Since |tau-rho|<=1/k, replacing tau by rho in k^2 E costs O_rho(k).

The actual comparisons retained from Stage 8 are

 R=|beta(S)/beta_m|=xi D_k(sigma_m)/(kappa_m J_(r,m)), |log xi|<=192e^4,
 H_(r,m)=2^(2mr+r^2)Z_(r,m),
 2^(-r)H<=J<=[3k(e+c_m)/2]^r H,
 log D_k(sigma_m)=-(log4)k^2+O(k log k),
 log kappa_m=O(k log k).

They are explicit determinant comparisons and inherited complete identities, not substitutions for endpoint terms. Combining them with (1) gives

 log T_(k,m)(v)=k^2 Phi(tau)-m log v+O(k log k)
              =k^2 Phi(rho)-m log v+O_rho(k log k),             (9)

where the remainder is independent of v. The constants can be chosen uniformly for rho in a compact subinterval of (0,1), provided k is large enough to keep tau in a slightly larger such interval.

Here the exact piecewise function is

 Phi(rho)=4rho log(1+sqrt(2))-3rho^2 log2, rho<=1/sqrt(2),
 Phi(rho)=(1+rho)^2 log(1+rho)+(1-rho)^2 log(1-rho)
          -2rho^2 log rho+(1-3rho^2)log2, rho>=1/sqrt(2).

For suitable C_rho and all sufficiently large eligible k, writing B=k^2 Phi(rho)-m log v, equation (9) gives

 log A<B-C_rho k log k  ==>  |P(S)|<v^(-m),
 |P(S)|<v^(-m)          ==>  log A<B+C_rho k log k.

Every occurrence of A means the ACTUAL primitive leading coefficient A=|I_m|/g, with the full physical clearer inside I_m and the final all-coefficient gcd g. The exact criterion remains A<T_(k,m)(v). Under a hypothetical rational S of reduced denominator v, inherited nonzero evaluation prevents |P(S)|<v^(-m). No inequality crossing this threshold for the actual A has been proved.

## 9. Outcome and limits

The new quantitative upper estimate preserves the diagonal self-energy, integration volume, factorial, external field, and endpoint normalization. Together with Jensen it improves o_rho(k^2) to O_rho(k log k). Compact-parameter uniformity across the support transition is justified explicitly. No limit coefficient for the k log k remainder, uniformity at rho=0 or rho=1, primitive-content bound, or irrationality theorem is asserted.

The limited review accepts Stage 8's stated mathematical conclusions under its inherited hypotheses, with an explicit completion of its finite-energy passage. The circle-regularization argument is original research in this stage and remains an author proof requiring separate review. No code execution, numerical evidence, networking, installations, or old audit was used.
