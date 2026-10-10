> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A small positive ratio with zero-free actual complex characteristic expectations

Author: Codex continuation Agent 3, 2026-10-02. Original author proof, not independently reviewed. Unlike the auxiliary equilibrium calculation, this note retains the original complex symbol, the actual reconstruction insertion, and every odd signed outer sector. It proves a zero-free interface; the complete scalar forcing saddle and center-rate theorem are the next step.

Set c0=10^(-10). For all sufficiently large n, all 3<=b<=c0 n, d=b-1, and every actual coefficient coordinate 0<=j<=b, let

    A_j(q)=nu_(n,d)(R_j(z) product_(l=1)^d(z_l^-1+q)).    (1)

The original unnormalized COMPLEX functional nu and exact full-K insertion R_j are used, with no contact determinant division. Then

    A_j(q)!=0 for every |q|<=3/4 or 2<=|q|<=3.            (2)

The result is uniform in q,j,b. It also proves det H_b!=0 on this small PROPORTIONAL allocation, on either parity. The constant c0 is deliberately conservative; no optimization is attempted. The endpoint and complete-eE terms in the exact coordinate/Gram formulas remain intact and are not declared negligible merely from (2).

## 1. Target checks and the variance theorem used

Pre-target archive rg queries included Brascamp, Poincare, phase variance, characteristic zero-free, orthogonal arc norm and Legendre evaluation in the October 1 analytic sources and the current continuation. No matching actual complex expectation theorem was found by the bounded search. The previous pointwise reconstruction sector lemma is an input, not an independent audit.

Primary-source searches:
- Brascamp Lieb variance inequality strongly convex probability density original paper 1976
- site:arxiv.org Brascamp Lieb inequality beta ensemble convex potential variance linear statistics
- Brascamp Lieb 1976 variance inequality extensions Brunn Minkowski Prekopa Leindler diffusion equation J Functional Analysis 22 366 389

Opened the primary [Brascamp and Lieb paper](https://www.sciencedirect.com/science/article/pii/0022123676900045) and the full [Magazinov and Peled concentration paper](https://arxiv.org/pdf/2006.05393). The classical variance inequality is established literature:

    Var(f)<=E[grad f^T (Hess V)^(-1) grad f]
             <=lambda^(-1) E||grad f||^2

for a density exp(-V) with Hess V>=lambda I on a convex domain. Standard approximation applies at the diverging boundary and collision potentials below. This specific actual phase and outer-sector argument is supplied here. No theorem for the present expectation is imported from a modulus-only ensemble.

## 2. The principal positive density controls the ACTUAL phase

Let I=(-3pi/4,3pi/4), g(t)=1+sigma cos t>0 there, z=exp(it). At fixed q in (2), form the positive principal partition

    Z_r(q)=1/[r!(2pi)^r] integral_(I^r) |Delta(z)|^2
       product_l[g(t_l)^n exp(-sigma cos t_l)|z_l^-1+q|]dt.

On one ordered chamber the negative logarithm has particle potential

    V_q(t)=-n log g(t)+sigma cos t-log|exp(-it)+q|

and pair potential -2log(2sin((t_k-t_l)/2)). The chamber is convex. Direct differentiation gives

    (-log g)''=sigma(cos t+sigma)/g(t)^2
                       >=sigma/M=2a on I.

The final two particle terms have second derivative bounded below by -22 uniformly for q in (2): distance from the characteristic zero circle is at least 1/4, giving the bound 4+16 for the logarithmic second derivative, and sigma<2. The pair Hessian is positive semidefinite. Hence for large n,

    Hess V_total>=a n I.

Choose a continuous phase for the nonzero characteristic factor on I and put

    Phi(t)=sum_l[-sigma sin t_l+arg(exp(-it_l)+q)].

Its particle derivative has modulus at most sigma+4<6. Applying the classical variance inequality on the chamber to this symmetric linear statistic gives

    Var_q(Phi)<=36r/(a n)<=36c0/a.                       (3)

For complex q its mean need not vanish; subtract that exact mean rather than assuming symmetry. Let S_j=s_jR_j/B_j be the normalized actual insertion from PROPORTIONAL_RECONSTRUCTION_SECTOR_LEMMA.md. It satisfies Re S_j>=1/100 and |S_j|<=5 pointwise for every circle configuration. Therefore

    Re E_q[S_j exp(i(Phi-E_q Phi))]
       >=1/100-5 E_q|Phi-E_q Phi|
       >=1/100-5sqrt(36c0/a)>1/200.                       (4)

This estimates the original oscillatory phase. The positive density is only an auxiliary absolute-value measure; its phase has not been discarded. Thus the principal contribution to s_j A_j(q)/(B_j Z_d(q)), after a known unit-modulus mean-phase rotation, has real part greater than 1/200.

## 3. An arc norm lower bound with no b^2 comparison loss

To control the FULL circle, it is essential to compare adjacent positive partitions, not to divide unrelated large Gaussian bounds. Fix delta=1/4 and L=tan(delta/2). Define

    B_delta=L^2/[(1+L)^2(1+L^2)] in (0,1),
    g_delta=1+sigma cos delta.

For every monic complex polynomial p of degree k, let

    F(x)=(1-ix)^k p((1+ix)/(1-ix)).

It has degree at most k and F(-i)=2^k exactly. Expand F in the orthonormal Legendre basis on [-L,L]. The formula for the usual Legendre polynomial implies

    |P_l(-i/L)|<=[2(1+L)/L]^l.

Its squared evaluation kernel is at most
(k+1)^2[2(1+L)/L]^(2k)/(2L). Cauchy-Schwarz and F(-i)=2^k yield

    integral_(-delta)^delta |p(exp(it))|^2 dt
       >=4L/[(1+L^2)(k+1)^2] B_delta^k.                 (5)

The circle change of variables contributes the denominator (1+x^2)^(k+1), which is bounded by (1+L^2)^(k+1); every scale in (5) is retained.

On this smaller arc the positive characteristic weight is at least
(1/4)exp(-sigma)g_delta^n. Thus its monic orthogonal-polynomial norm h_k, with dt/(2pi), satisfies

    h_k>=C_delta g_delta^n B_delta^k/(k+1)^2,             (6)

with a fixed positive C_delta uniform in q. By the exact Gram/Andreief factorization, Z_r(q)=product_(k=0)^(r-1)h_k. The same norms use the same n and q at every dimension; this is an actual adjacent-partition comparison.

## 4. All outer sectors, including the odd signs

Outside I, |g(t)|<=sigma-1=M^(-1). Its one-particle absolute weight, integrated with dt/(2pi), is at most

    C M^(-n),

uniformly in q, since exp(-sigma cos t)<=exp(sigma) and |z^-1+q|<=4. If k out of r particles lie outside I, bound every cross/outer Vandermonde factor by four. The exact combinatorial normalization then gives

    sector absolute integral/Z_r(q)
       <=1/k! [C r^2(4/B_delta)^r (M g_delta)^(-n)]^k.   (7)

This follows by dividing by the SAME h_(r-k),...,h_(r-1) in (6); no r^2-scale discrepancy is introduced. Elementary evaluations give

    log(M g_delta)>1.7, log(4/B_delta)<7.

For r<=c0n the bracket in (7) is at most exp(-n) eventually. Summing k>=1 gives at most 2exp(-n). For odd n the corresponding original sectors have the signs (-1)^(nk); the absolute bound controls their possible cancellation, rather than changing them to positive sectors.

The normalized actual insertion has modulus at most five EVERYWHERE on the circle. Thus the full actual outer-sector contribution, divided by B_j Z_d(q), has modulus at most 10exp(-n). This is smaller than half the principal margin in (4) eventually.

Combining (4),(7) proves the quantitative full-circle bound

    (1/400)B_j Z_d(q)<=|A_j(q)|<=6B_j Z_d(q),            (8)

and therefore (2). For positive real q in these domains the principal mean phase is zero by reflection, and the full conjugate integral is real. Its sign is precisely s_j, with the same lower margin.

## 5. Actual contact normality in the same proportional range

For det H_b omit the characteristic factor and use insertion one. The principal particle potential is -nlog g+sigma cos t, with Hessian at least a n for large n. The phase is -sigma sum sin t, has reflection mean zero and variance at most sigma^2 b/(a n). Hence its principal real expectation is at least 1-sigma^2c0/(2a)>1/2.

The same monic arc comparison omits the harmless characteristic upper/lower constants. Its full odd/even outer-sector sum remains exponentially smaller than the principal positive partition. Thus det H_b>0 eventually for every b<=c0n, on BOTH parities. The actual contact matrix T differs only by its stated nonzero diagonal/parity normalization, so it is nonsingular on this domain.

This conclusion uses the actual complex expectation and signed outer sectors. It does not import the earlier b^4 log n theorem or extrapolate its constants.

## 6. What has and has not been obtained

All actual reconstruction coordinates have a zero-free characteristic expectation on fixed complex q domains that contain neighborhoods of both shifted proportional forcing saddles. The bounds are uniform across the coordinates and retain normality. This is a concrete interface for the remaining scalar contour analysis.

The integrated plus/minus forcing must still be analyzed on those contours to establish nonzero signed actual coordinate error and its n-exponent. The endpoint and complete-eE expressions stay in the exact full-coordinate/Gram identity. No primitive-denominator estimate, family exclusion or rationality conclusion for e+pi is made by this note.
