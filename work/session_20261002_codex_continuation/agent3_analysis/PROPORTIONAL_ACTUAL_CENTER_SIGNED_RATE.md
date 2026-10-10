> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The complete actual center at a small positive proportional allocation

Author: continuation Agent 3, 2026-10-02. Original author theorem, not independently reviewed. This note completes the scalar complex-contour step after SMALL_RATIO_ACTUAL_CHARACTERISTIC_ZERO_FREE.md. Every actual reconstruction coordinate, both signed circle sectors, the full exponential residual and the endpoint correction are retained.

Set sigma=sqrt(2), M=1+sigma, and c0=1/1000, using the sharpened interface in SMALL_RATIO_CONSTANT_UPGRADE.md. Fix ANY 0<c<c0 and any integer allocation b=b(n) with b/n->c. Let W_n be ANY positive diagonal actual B-coefficient metric, allowed to depend arbitrarily on n; the fixed factorial metrics are included. Then, for all sufficiently large n, the exact contact matrix is normal, every actual reconstructed B coordinate u_j is nonzero, and the complete actual center satisfies

    sign(c_W(n)-(e+pi))=(-1)^(n+1),
    -(1/n)log|c_W(n)-(e+pi)| -> (2+c)log M.             (1)

The assertion includes both parities. Its n-exponential improvement over the fixed-b rate is c log M. The explicit c0 is very conservative; this theorem does not claim the full proportional interval below the auxiliary equilibrium transition. Constants and the threshold in n may depend on the fixed c and the allocation's convergence to c. No primitive-denominator estimate or conclusion about rationality of e+pi follows.

## 1. Exact inputs and target checks

Use the exact original complex functional nu_(n,r), the full gamma insertion R_j, and P_j,F_j,E_j,D in PROPORTIONAL_B_EXACT_SELBERG_PROGRESS.md. Put d=b-1,

    A_j(q)=nu_(n,d)(R_j product_l(z_l^(-1)+q)),
    B_j=|K_(j,d)|sigma^(-d),
    s_0=(-1)^(d+1), s_j=(-1)^(d-j+1) for 1<=j<=d, s_b=1.

The original sector and actual-expectation arguments, with the explicit range refinement in SMALL_RATIO_CONSTANT_UPGRADE.md, prove the following deliberately weakened bounds uniformly across all these coordinates:

    Re(s_j R_j/B_j)>=1/100, |R_j|<=5 B_j,
    B_j Z_d(q)/400 <= |A_j(q)| <= 6 B_j Z_d(q)           (2)

on |q|<=3/4 or 2<=|q|<=3. Here Z_d(q) is the POSITIVE principal absolute partition on I=(-3pi/4,3pi/4), with the SAME n and dimension d. The lower bound is obtained by estimating the actual phase variance and all odd outer sectors, not by replacing the expectation by its modulus. For positive real q in these regions, s_j A_j(q)>0. In the same allocation D=det H_b>0 on both parities.

Before this target, archive rg queries proportional, double scaling, shifted saddle and (2+c) found the old b^4 log n normality, high-row proportional bounds, varying-Toeplitz hypotheses, and the team's current exact Selberg reduction. They did not locate a complete actual proportional-center rate at the searched scope. No accepted normality audit or old finite-center check was replayed. No global novelty claim is inferred.

Fresh primary queries included beta ensemble empirical measure large deviations compact interval varying potential equilibrium Guionnet; Borot Guionnet asymptotic expansion beta matrix models multi cut large deviation empirical measure; Toeplitz determinants coalescing saddle moments Pan Prokhorov 2025; and Hermite Pade approximation multiple orthogonal polynomials quadratic exponential asymptotics Kuijlaars Wielonsky. Opened the current [Pan/Prokhorov record](https://arxiv.org/abs/2407.04852), the full [Mano/Tsuda Hermite-Pade paper](https://arxiv.org/html/1502.06695), the [Borot/Guionnet one-cut record](https://arxiv.org/abs/1107.1167), its [multi-cut record](https://arxiv.org/abs/1303.1045), and primary [Guionnet lecture notes](https://perso.ens-lyon.fr/aguionne/ColumbiaCBMS.pdf). The current 2024 Cambridge multi-cut article was returned with its Theorem 1.1 and Section 3 in the search result at https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/asymptotic-expansion-of-beta-matrix-models-in-the-multicut-regime/058A845F012888985503D86AF99D63F5 ; a later direct opening and DOI opening failed internally. Classical determinant, Schur, empirical-law and saddle methods overlap this work. The field here diverges at the principal boundaries, so the continuous-field theorem is NOT applied without modification: the necessary elementary truncation argument is given below.

## 2. The empirical law needed, including its boundary hypothesis

Write Z_r(0) for the positive principal partition with weight g(t)^n exp(-sigma cos t), g(t)=1+sigma cos t. Under x=tan(t/2), I becomes (-M,M); apart from constants its density is

    Delta(x)^2 product_l [(M^2-x_l^2)^n
                    /(1+x_l^2)^(n+r) exp(-sigma cos t(x_l))].

For r/n->c the order-r^2 field is

    V_c(x)=(1+1/c)log(1+x^2)-(1/c)log(M^2-x^2).

The unique principal equilibrium has density

    mu_c(x)=C/pi *sqrt(A^2-x^2)/[(1+x^2)(M^2-x^2)],
    A^2=M^2 c(c+2)/[M^2+(c+1)^2],
    C=sqrt((M^2+1)(M^2+(c+1)^2))/c, |x|<=A.           (3)

Its resolvent is

    R_c(z)=V_c'(z)/2-C sqrt(z^2-A^2)/[(z^2+1)(M^2-z^2)].

Removal of the poles at i and M and the 1/z behavior prove normalization. The jump gives (3). The derivative of the Euler-Lagrange gap for A<x<M is 2C sqrt(x^2-A^2)/[(1+x^2)(M^2-x^2)]>0, and reflection handles the left side. Thus the variational inequality holds on the whole principal interval. Strict positivity of logarithmic energy on mass-zero signed measures gives uniqueness.

For completeness, the empirical law follows directly with the divergent boundary field. Truncate both V_c and the kernel -log|x-y| above a level L, making bounded continuous functions on the compact interval. The corresponding empirical energy bounds the negative log-density divided by r^2 from below, with only the diagonal correction O(L/r) and the bounded amplitude correction O(1/r). The truncated V_(r/n) converges uniformly to truncated V_c. The interval volume contributes O(r), hence no r^2 term. A normalization lower bound is obtained by placing the particles near separated quantiles of (3), in boxes of width r^(-3). Its density is bounded for this fixed c and its support lies strictly inside (-M,M). The spacing is bounded below by a constant times |i-j|/r; this controls the truncated diagonal and proves that the discrete logarithmic energies converge to the equilibrium energy. The box volume costs only O(r log r)=o(r^2).

On any closed weak set of probability measures excluding mu_c, compactness and uniqueness give a positive energy gap for some sufficiently large truncation L: otherwise a sequence of minimizing measures and then L->infinity would produce another minimizer of the untruncated energy. These upper and lower bounds imply convergence in probability of the empirical measure to mu_c. Since test functions below are bounded continuous, convergence holds in expectation too. Any bounded order-r characteristic tilt preserves this argument. The divergence of V_c at the boundaries is thereby handled explicitly.

## 3. Recovering the ACTUAL holomorphic phase, uniformly in j

Define

    L_c(q)=integral log(z(x)^(-1)+q) dmu_c(x).

Near q=M use log q+log(1+z^(-1)/q). Near q=M^(-1) use -it(x)+log(1+q z(x)); the reflection mean of -it is zero. These are holomorphic branches and real on the relevant positive real arguments.

On fixed compact neighborhoods of these arguments, f_q(t)=log|exp(-it)+q| and its derivatives are uniformly bounded. Along the positive tilt exp(s sum_l f_q), 0<=s<=1, the ordered-chamber Hessian remains >=a n I for large n, a=1-sigma/2. The Brascamp-Lieb estimate gives

    Var_s(sum_l f_q)<=C r/n.

Twice integrating the logarithmic moment-generating derivative gives

    log[Z_r(q)/Z_r(0)]
       =E_0 sum_l f_q+O(r/n),
    (1/n)log[Z_r(q)/Z_r(0)] -> c Re L_c(q).             (4)

The bounded derivatives and a finite-net argument make this convergence uniform on compact q sets. This is a positive-ensemble calculation only for the real part. Equation (2) now gives the real part of the actual log at the same scale.

Take D_+={|q-M|<1/5} and D_-={|q-M^(-1)|<1/5}. They lie inside the zero-free regions (2). Define the ACTUAL holomorphic logarithms

    H_(j,n)(q)=(1/n)Log[A_j(q)/(s_j B_j Z_d(0))],

anchored real at q=M or M^(-1) respectively. The real-part error from (2) is O(1/n), uniformly in j. Harmonic interior derivative estimates, followed by integration of the Cauchy-Riemann equations from the real anchor, give

    H_(j,n) -> c L_c

uniformly across ALL j on every compact subdomain, together with any fixed number of complex derivatives. This is a convergence statement for the original oscillatory A_j. Zero-freeness and the real anchor determine its phase; no modulus-only phase has been substituted.

## 4. Exact shifted limiting saddles and their phase difference

Put

    g(zeta)=1+(sigma/2)(zeta+zeta^(-1)),
    h(zeta)=(sigma/2)(zeta+zeta^(-1))-1,
    Phi_+(zeta)=log g(zeta)+c L_c(sigma+zeta),
    Phi_-(zeta)=log h(zeta)+c L_c(sigma-zeta).

Their positive-real stationary points near one are EXACTLY

    r_+=2/(2+c), r_-=2M/(2M-c),                       (5)

and

    Phi_+(r_+)-Phi_-(r_-)=(2+c)log M.                   (6)

Here is an algebraic derivation and receipt. Set E=M^2+(c+1)^2 and B=M^2+1. For real q>1 or 0<q<1, put T=(q+1)/|q-1|>1 and

    G(T)=integral (1/2)log(T^2+x^2) dmu_c(x).

Then L_c(q)=log|q-1|+G(T)-G(1). The resolvent gives

    G'(T)=-T[(c+1)/(c(1-T^2))+1/(c(M^2+T^2))]
           +C sqrt(T^2+A^2)/[(1-T^2)(M^2+T^2)].         (7)

An antiderivative, up to a constant, is

    G(T)=(c+1)/(2c)log(T^2-1)-(1/(2c))log(M^2+T^2)
          +(c+1)/c acoth(sqrt(1+A^2)*y)
          -(1/c)atanh(sqrt(M^2-A^2)*y/M),
    y=T/sqrt(T^2+A^2).

Let q_+=sigma+r_+, q_-=sigma-r_-, and set

    T_+=M^2(2sigma+c)/(2sigma M+c),
    T_-=M^2(2sigma-c)/(2sigma M+c),
    P_+=c^2+(sigma+3)c+B, P_-=c^2+(1-sigma)c+B.

The radicals simplify to

    sqrt(T_+^2+A^2)=M sqrt(B) P_+/[sqrt(E)(2sigma M+c)],
    sqrt(T_-^2+A^2)=M sqrt(B) P_-/[sqrt(E)(2sigma M+c)].

Substitution into (7) proves both stationary equations in (5) by rational arithmetic in Q(sqrt(2),c). For (6), set k_+=M(2sigma+c)/P_+, k_-=M(2sigma-c)/P_-, and k1_+=(c+1)k_+, k1_-=(c+1)k_-. Define the positive ratios

    aa=(q_+-1)/(1-q_-), bb=(T_+^2-1)/(T_-^2-1),
    cc=(M^2+T_+^2)/(M^2+T_-^2),
    dd=[(k1_++1)/(k1_+-1)]/[(k1_-+1)/(k1_--1)],
    ee=[(1+k_+)/(1-k_+)]/[(1+k_-)/(1-k_-)].

Twice the phase difference equals

    c log(aa^2 bb dd)+log[(g(r_+)/h(r_-))^2 bb dd/(cc ee)].

Direct rational simplification gives aa^2 bb dd=M^2 and the second logarithm's argument M^4. This proves (6). The exact symbolic receipt proportional_saddle_algebra.json records zero residuals for both stationary equations, both radical squares, and these two factors. It is an algebra receipt rather than a finite-center sampling argument.

## 5. Actual finite-n saddles and local noncancellation

For each coordinate use the actual phases

    Psi_(j,n),+(zeta)=log g(zeta)+H_(j,n)(sigma+zeta),
    Psi_(j,n),-(zeta)=log h(zeta)+H_(j,n)(sigma-zeta).

Section 3 gives uniform C^3 convergence on fixed neighborhoods of one. The real branches remain real on a real interval. Their limiting second radial derivatives are positive. To check the needed uniform margin explicitly, on |theta|<=1/10 and |r-1|<=1/1000, direct differentiation gives

    d^2/dtheta^2 Re log g(r exp(i theta))<-1/2,
    d^2/dtheta^2 Re log h(r exp(i theta))<-3.

The characteristic correction has second angular derivative bounded by 30c: on these arcs the characteristic factors are at distance at least 1/4 from zero, so |L_c'|<=4 and |L_c''|<=16. Thus the limiting angular curvature is <-1/4 for both phases. The choice c<c0 leaves a large margin, as certified by the rational contour inequalities in SMALL_RATIO_CONSTANT_UPGRADE.md. Their real radial curvature near the real stationary point is consequently positive.

The ordinary implicit-function/strict-monotonicity argument therefore produces real finite-n stationary points r_(j,n),+ and r_(j,n),- converging uniformly in j to (5). Put

    lambda_(j,n),+/-=r_(j,n),+/-^2 Psi_(j,n),+/-''(r_(j,n),+/-)>0.

These lambdas are uniformly bounded away from zero and infinity. The actual phase on each small circular arc has its first derivative zero and the expansion

    Psi(r exp(i theta))=Psi(r)-lambda theta^2/2+O(theta^3),

with uniformly bounded remainder. The conjugate symmetry makes the leading Gaussian contribution real and positive. On |theta|<=n^(-2/5), the exponent's cubic remainder is o(1). On n^(-2/5)<=|theta|<=1/10, uniform negative angular curvature gives exponential suppression. Hence the local ACTUAL integrals are, uniformly in j,

    exp(n Psi(r)) sqrt(2pi/(n lambda)) (1+o(1)).        (8)

No assumption that the saddle stays at one, no fixed-b remainder constant, and no replacement of a complex integral by a positive modulus integral enter (8).

## 6. Remote contours and the true forcing endpoints

The plus integral can be deformed from the unit circle to radius r_(j,n),+ because its integrand g(zeta)^n A_j(sigma+zeta) dzeta/(i zeta) is analytic on the intervening annulus. The minus integral is an open arc from exp(-i pi/4) to exp(i pi/4). Deform it to the circular arc at radius r_(j,n),- and KEEP the two radial endpoint connectors. Integer powers make the integrands single-valued on these annuli.

For all sufficiently large n, all these radii satisfy |r-1|<1/1000. Directly from the quadratic expressions in cos theta for |g(r exp(i theta))|^2 and |h(r exp(i theta))|^2, one has the coarse bounds

    |g(r exp(i theta))|<=g(r) exp(-1/400)
      for 1/10<=|theta|<=pi,
    |h(r exp(i theta))|<=h(r) exp(-1/400)
      for 1/10<=|theta|<=pi/4.                          (9)

Every such contour argument has |q|<3, so the full absolute base partition and |R_j|<=5B_j give

    |A_j(q)|<=10 B_j Z_d(0) 4^d.                       (10)

The full absolute base differs from its principal partition by at most 2exp(-n), by the same adjacent-norm outer-sector estimate used in the zero-free theorem. At a real saddle the zero-free lower bound gives

    |A_j(q_s)|>=(B_j/400)Z_d(0) min(1,|1-q_s|)^d,

where the final base is at least 0.58 for either forcing. Thus the remote/main exponential ratio is bounded by a polynomial in n times

    exp[-n/400+d log(4/0.58)],

which tends to zero exponentially because log(4/0.58)<2 and d/n->c<c0=1/1000. This controls the plus negative-symbol arcs and all their parity signs as well.

At either original minus endpoint h(exp(+-i pi/4))=0. On its radial connector, |h(zeta)|<=0.002, whereas h(r)>0.4. Equation (10) therefore makes both exact connectors exponentially smaller still. They are not deleted by an endpoint approximation. Combining (8)-(10) yields the full actual formulas

    P_j=(n!/(2pi)) s_j B_j Z_d(0)
       exp(n Psi_(j,n),+(r_(j,n),+))
       sqrt(2pi/(n lambda_(j,n),+)) (1+o(1)),

    F_j=2n! s_j B_j Z_d(0)
       exp(n Psi_(j,n),-(r_(j,n),-))
       sqrt(2pi/(n lambda_(j,n),-)) (1+o(1)).           (11)

These include every coordinate. In particular P_j and F_j have sign s_j, all P_j are nonzero, and F_j/P_j>0. Equations (6),(11) give

    sup_(0<=j<=b) |(1/n)log(F_j/P_j)+(2+c)log M|->0.    (12)

## 7. Full exponential forcing and endpoint dominance

The exact uniform full-residual bound from CONTACT_INVERSE_RESEARCH.md Section 9.3 is

    |eE_i|<=27 M^n sigma^(-i)/(n+1).

Since |e_(d-i)(z^(-1))|<=binom(d,i), its COMPLETE insertion is at most 27 M^n 2^d/(n+1). The reconstruction and full absolute-base bounds give

    |E_j|<=270 B_j Z_d(0) M^n 2^d/(n+1).

For the plus real saddle g(r)>=M and q_s>2, so the lower bound on A_j has characteristic factor at least one. Formula (11) therefore gives

    |E_j/P_j|<=C 2^d/(n! sqrt(n))
              =exp(-n log n+O(n)),                    (13)

uniformly in j. These are bounds for the full E residual, not the first missing Taylor term.

For the actual coefficient-zero endpoint, D<=2 Z_b(0). With the SAME n, adjacent partition factorization gives Z_b(0)/Z_d(0)=h_d, where h_d is a positive monic circle norm. The trial polynomial z^d gives h_d<=exp(sigma)M^n. Also B_0=(n)_d sigma^(-d)>1 eventually. The lower bound for P_0 thus yields

    |D/P_0|<=C sqrt(n)/(n! B_0)
            =exp(-n log n+O(n)).                       (14)

All other endpoint coordinates are exactly zero. Equations (13),(14) are factorially smaller than (12), on this very same proportional allocation.

## 8. Complete coordinates and all positive actual metrics

The exact coordinate identity remains

    c_j-(e+pi)=E_j/P_j+(-1)^(n+1)F_j/P_j
                            +(-1)^n delta_(j,0)D/P_j.

Using (12)-(14) proves, uniformly in every j, the sign in (1) and its limiting n-rate. Since u_j=(-1)^n P_j/D is nonzero, the exact Gram identity becomes the positive convex average

    c_W-(e+pi)=sum_j [W_jj u_j^2/(sum_l W_ll u_l^2)]
                                      [c_j-(e+pi)].

Every coordinate has the same eventual error sign. The uniform minimum and maximum of their magnitudes sandwich ANY such convex average, even when metric weights vary arbitrarily rapidly with n. Thus (1) holds for the full actual center, including the fixed b-coefficient factorial Gram choices on a growing b allocation.

The proof obtains a genuine n-exponential improvement by changing the allocation b~cn. Fixed positive metric tuning alone does not change this leading exponent. The arithmetic cost of this growing allocation remains a separate required calculation; the present theorem asserts no numerator-versus-primitive-denominator win.
