> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Increasing the proved actual-complex proportional range to 1/1000

Agent 3, 2026-10-02. Original author refinement, not independently reviewed. This strengthens the uniform interface in SMALL_RATIO_ACTUAL_CHARACTERISTIC_ZERO_FREE.md and is the version used by PROPORTIONAL_ACTUAL_CENTER_SIGNED_RATE.md. Set c1=1/1000. All assertions here hold for sufficiently large n uniformly over 3<=b<=c1 n, every actual coordinate j and the stated complex q regions.

The target was checked by archive rg for c0, 1/1000, refined sector, Gamma ratio and (1+sigma/n); the hits were the previous deliberately conservative zero-free proof and unrelated old gamma/arithmetic contexts. Primary searches for strongly convex characteristic expectations and Toeplitz/Hankel gamma insertions reopened the full concentration paper https://arxiv.org/pdf/2006.05393 and Hermite-Pade paper https://arxiv.org/html/1502.06695. General variance/interpolation frameworks are established literature; this numerical range is derived below for the actual insertion. No global novelty claim is made.

## 1. A sharper gamma insertion estimate

For the degree-k reference term in the exact gamma representation, expand (u+sigma)^k rather than making the earlier shift-only estimate. One obtains

    integral u^(n-1)e^(-u)(u+sigma)^k du / Gamma(n+k)
      =sum_(l=0)^k binom(k,l) sigma^l Gamma(n+k-l)/Gamma(n+k)
      <=sum_(l=0)^k binom(k,l)(sigma/n)^l
      =(1+sigma/n)^k <= exp(sigma k/n).                 (1)

Every denominator in the gamma ratio is at least n because l<=k. All actual middle-coordinate references are positive combinations of the same terms. Consequently

    |S_j|=|s_jR_j/B_j|<=exp(sigma d/n)<1.002            (2)

in the present range, at EVERY circle configuration.

On the main gamma region u>=(19/20)n, k<=d<=c1 n implies, for large n,

    k arcsin(sigma/u)<=0.0015,
    (1-sigma/u)^k>=exp(-0.0015).

The selected products thus have real part at least cos(0.0015)exp(-0.0015)>0.998. The normalized small gamma tail is still O(exp(-gamma n)) uniformly, by the original shift and gamma lower-tail argument. The complete normalized insertion therefore satisfies

    Re S_j>=0.99                                       (3)

eventually, at every circle configuration and every coordinate. The earlier 0.01 lower bound had been uniform all the way up to d<n and was unnecessarily weak on this smaller allocation.

## 2. Actual characteristic noncancellation

Retain the original complex phase, ordered-chamber Hessian >=a n I and variance

    Var(Phi)<=36 d/(a n)<=36/(1000a), a=1-sigma/2.

Equations (2),(3) give the actual rotated principal expectation bound

    Re E[S_j exp(i(Phi-E Phi))]
       >=0.99-1.002 sqrt(36/(1000a))>0.63.               (4)

The strict last inequality follows already from a>0.292 and sqrt(36/(1000*0.292))<0.352. It applies uniformly for |q|<=3/4 or 2<=|q|<=3, including complex q with nonzero phase mean. The actual phase is retained.

The SAME adjacent-norm odd-sector bound is still exponentially small: its logarithmic bracket is at most -1.7n+7d+O(log n)<-n eventually in this range. With (2) controlling the insertion on all sectors, their normalized total is O(exp(-n)). Hence the strengthened full-circle bounds are

    (1/2)B_j Z_d(q)<=|A_j(q)|<=2B_j Z_d(q),             (5)

and A_j(q) is zero-free on the two original regions. For positive real q, s_j A_j(q)>0. Omitting the characteristic and the insertion gives principal determinant real expectation at least 1-sigma^2/(2000a)>0.996; the same outer bound proves det H_b>0 on BOTH parities.

The full positive ABSOLUTE base partition is at most twice the principal partition throughout this range, also with the same n and adjacent norms. This bound is used only for remote contour and residual estimates; it is not substituted for the actual central integral.

## 3. Compatible scalar contour margins

The proportional stationary radii lie within 0.001 of one for c<=c1. Use epsilon=1/10 instead of the previous 1/20 and require |r-1|<=1/1000. Put A_r=(r+r^(-1))/2 and B_r=(r-r^(-1))/2. Then 1<=A_r<1.000001, B_r^2<1.01*10^(-6), and

    |g(r exp(i theta))|^2=1+2sigma A_r cos theta+2cos^2 theta+2B_r^2,
    |h(r exp(i theta))|^2=1-2sigma A_r cos theta+2cos^2 theta+2B_r^2.

On |theta|<=epsilon, cos theta>0.995. Differentiating these quadratics shows that the second angular derivative of log modulus is <-1/2 for g and <-3 for h: their squared-modulus second derivatives are respectively <-6.73 and <-1.09, while their squared moduli are <5.831 and <0.17201. The nonpositive squared-first-derivative term only strengthens these bounds. The characteristic second angular derivative is <=30c<=0.03. Thus the limiting and eventual finite-n local curvature margins used in the center proof remain valid.

For epsilon<=|theta|<=pi, convexity of the g quadratic in cos theta reduces the maximum to cos epsilon or -1; the latter is smaller. The Taylor inequality cos epsilon<=0.995005 gives a relative squared-modulus gap >0.0058, hence

    |g(r exp(i theta))|<=g(r) exp(-1/400).

For epsilon<=|theta|<=pi/4, the h quadratic likewise reduces the maximum to cos epsilon or 1/sigma; the latter is smaller. Its relative squared-modulus gap is >0.03, so the SAME weaker exp(-1/400) bound holds. All estimates can use the rational enclosures 1.414<sigma<1.415 and the bounds above.

The remote characteristic/main ratio is at most a polynomial times

    exp[-n/400+d log(4/0.58)].

Since log(4/0.58)<2, d/n<=c1 gives an eventual strictly negative exponent, at most -0.0005n before polynomial factors. Thus remote contours stay negligible throughout this larger range. Both minus endpoint connectors have length at most 0.001 and |h|<=0.002, whereas the real saddle has h>=sigma-1>0.4; they remain exponentially smaller too.

Replacing only these explicit interface/margin constants upgrades the complete actual-center theorem to ANY fixed 0<c<1/1000. The exact saddle algebra, every coordinate, parity signs, complete residuals and metric convexity are unchanged. The allocation now supplies the genuine leading gain c log M, still with no asserted primitive-denominator improvement.
