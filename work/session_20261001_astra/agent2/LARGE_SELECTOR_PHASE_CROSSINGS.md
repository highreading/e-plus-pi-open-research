> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Real-parameter phase crossings of the large selector

New author analytic research, not independently reviewed. LARGE_SELECTOR_RELATIVE_SADDLE.md is preserved; its separately assigned examination is not duplicated. The main LARGE_SELECTOR_PHASE_SPARSITY_DRAFT.md was read as an author deduction. This note supplies new complex-parameter remainder control, real phase derivatives, and exact parity-crossing coordinates. It does not claim integer avoidance or exclusion of all exceptional nodes. No numerical computations, scans, or additive-enclosure replay were performed.

## 1. Domain and the continuation being defined

Fix rho>0 and C>0. For sufficiently large integer n define the real block

    I_n=[M_-,M_+],
    M_-=rho n log n-C n log n/log log n,
    M_+=rho n log n+C n log n/log log n.

The analytic results hold without restricting n to powers of two. Arithmetic applications below restrict to the stated parity-eligible integer nodes and invoke their separate denominator result.

Write

    alpha=(1+i)/2,
    V(w)=w^2-w+1/2,
    A(w)=(2w^2-1)^2,
    C0(x)=1-x+(1+i)x^2/4,
    w=alpha-i x/2=alpha(1-alpha x), 0<=x<=1.

On this segment,

    V(w)=(x/2)(1-x/2),
    A(w)=(-2i) C0(x)^2.

Define Log C0(x) by analytic continuation from Log C0(0)=0 in a thin simply connected neighborhood of [0,1]. This is possible because

    Re C0(x)=(1-x/2)^2>=1/4

on that interval. Fix log(-2i)=log 2-i pi/2. For complex zeta define the continued power along the segment by

    A(w)^zeta=exp(zeta[log 2-i pi/2+2 Log C0(x)]).

At x=1 this logarithm is the real logarithm of A(1/2)=1/4. It is continuous along the entire segment, including its upper endpoint. For every integer zeta=m it agrees with the original integer power.

The continuation is

    J_n(zeta)=integral_(1/2)^alpha
                V(w)^n exp(zeta Log A(w))/w^(n+1) dw.       (1)

The integer n powers in (1) require no additional branch. The segment avoids w=0. Its chosen Log A is bounded, so differentiation under this finite contour integral proves that J_n is entire in zeta. This gives one specified continuation, rather than asserting that interpolation from the integer values is unique.

In particular, for real m, the rapidly rotating factor is exactly exp(-i pi m/2). The continuation retains that factor; it does not periodically reset its argument.

## 2. Exact saddle functions and leading approximation

For real m>0 set lambda=n/m and nu=1/n. Use the analytic phase from the retained relative-saddle construction:

    phi(t;lambda,nu)=log t+(2/lambda)Log C0(lambda t)
       +Log(1-lambda t/2)
       -(1+nu)Log(1-alpha lambda t).

The logarithms other than log t equal zero at lambda=0; log t is real on the positive axis near 1/2. The term (2/lambda)Log C0(lambda t) has a removable limit -2t. Thus

    phi(t;0,nu)=log t-2t.

Let t_s(lambda,nu) be the analytic solution of phi_t=0 near 1/2 and set

    F(lambda,nu)=phi(t_s;lambda,nu),
    beta(lambda,nu)=-phi_tt(t_s;lambda,nu).

The branches are continued from

    t_s(0,nu)=1/2,
    F(0,nu)=-log 2-1,
    beta(0,nu)=4,
    Log beta(0,nu)=log 4.

Define, for complex zeta near a sufficiently large positive real number,

    H_n(zeta)=[i/(2alpha)](2alpha)^(-n)
       exp(zeta(log 2-i pi/2))(n/zeta)^(n+1)
       exp(n F(n/zeta,nu)) sqrt(2pi/n)
       exp(-Log beta(n/zeta,nu)/2).                       (2)

The power n+1 is integral. Its logarithm, when used to specify a phase, is continued from positive n/zeta. The other branches in (2) have just been fixed. H_n is holomorphic and nonzero on the neighborhoods used below.

The retained real-parameter leading functions have the analytic expansion

    F(lambda,nu)=-log 2-1
       +lambda[-1/8+3i/8+nu alpha/2]+O(lambda^2).          (3)

The remainder in (3) is analytic with uniformly bounded derivatives on a fixed smaller parameter neighborhood, uniformly for nu in [0,1]. This statement concerns F itself. It does not yet license differentiating the relative error J_n/H_n-1.

## 3. New holomorphic relative-remainder lemma

There are absolute constants lambda_0>0, n_0, C_0 and delta=1/512 such that, for n>=n_0 and any real mu with 0<n/mu<=lambda_0,

    J_n(zeta)=H_n(zeta)(1+e_n(zeta)),
    |e_n(zeta)|<=C_0/n                                  (4)

throughout the complex disk

    |zeta-mu|<=2delta mu.

The function e_n is holomorphic there. Unlike a bound only at real or integer m, this lemma supplies derivative control.

Here is the complex-uniform argument. Put lambda_c=n/mu>0 and eta=zeta/mu, so |eta-1|<=1/256. Scale the original real segment using x=lambda_c t, without moving its endpoints with zeta. After factoring out the explicit exponential and lambda_c^(n+1), the phase is

    phi_eta(t)=log t+(2eta/lambda_c)Log C0(lambda_c t)
       +Log(1-lambda_c t/2)
       -(1+nu)Log(1-alpha lambda_c t).                    (5)

Its limit is log t-2eta t, whose saddle is 1/(2eta), uniformly near 1/2. The entire central saddle construction is therefore a compact analytic perturbation with respect to eta as well as lambda_c and nu.

The required global tail bound holds for complex eta, not just for real m. For 0<=x<=1 the retained exact segment identities imply

    log|C0(x)|<=-7x/16,
    0<=Arg C0(x)<=x^2<=x.

The argument estimate follows from

    tan Arg C0(x)=x^2/[4(1-x/2)^2]<=x^2.

Consequently

    Re(2zeta Log C0(x))
       <=-[7 Re zeta/8-2|Im zeta|]x.

For the specified eta disk,

    7 Re eta/8-2|Im eta|>=3/4.

The remaining factors satisfy

    |(1-x/2)/(1-alpha x)|<=1,
    |1-alpha x|^(-1)<=sqrt(2).

Thus the modulus of the scaled integrand is at most

    sqrt(2)t^n exp(-3nt/4), 0<=t<=1/lambda_c.             (6)

With fixed cutoffs a=1/16 and B=8, the lower real tail is bounded by sqrt(2)a^(n+1)/(n+1). The upper real tail is bounded by a constant times exp(n(log 8-6))/n, because the derivative of log t-3t/4 is at most -5/8 for t>=8. Both have a fixed exponential gap below the central saddle modulus, whose limiting phase is -Log(2eta)-1. This gap is uniform on the eta disk after decreasing lambda_0.

On a fixed thin rectangle around [a,B], all logarithms in (5) are analytic. The saddle t_eta is analytic near 1/(2eta). Its imaginary part is smaller than 1/64 for lambda_0 sufficiently small. Shift the middle segment to a horizontal segment through t_eta, with short vertical connectors. This deformation is inside that rectangle; it preserves the chosen branches and avoids w=0 and the zeros of C0. The connectors have a uniform strict phase gap by continuity from the eta-near-one limiting phase.

On the horizontal segment,

    phi_eta''(t)=-1/t^2+O(lambda_c)

uniformly. Since Re(1/(u+iv)^2)>1/100 for a<=u<=8 and |v|<=1/64, its real phase is uniformly strictly concave. It has its unique maximum at the saddle. Derivatives through sixth order are uniformly bounded on a fixed saddle neighborhood. The Gaussian curvature has positive real part and remains close to 4eta^2.

Integration on a symmetric neighborhood of t_eta now gives a relative O(1/n) error uniformly in this COMPLEX eta disk. After scaling by n^(-1/2), the first cubic term integrates to zero by oddness; the quartic and squared-cubic terms have size O(1/n). Higher Taylor terms are bounded using the fixed derivative bounds. The region outside |t-t_eta|<=n^(-2/5) has an exp(-c n^(1/5)) bound from the strict real concavity. The Gaussian integral is nonzero, with its square root continued from eta=1, lambda_c=0. Equation (6) and the connector gaps handle the remaining contour pieces.

Finally set lambda_zeta=lambda_c/eta. The natural saddle coordinate satisfies

    t_s(lambda_zeta,nu)=eta t_eta,
    F_eta=F(lambda_zeta,nu)-Log eta,
    beta_eta=eta^2 beta(lambda_zeta,nu).

Here Log eta is its branch near zero at eta=1. The factors eta^(-n) from the phase and eta^(-1) from the Gaussian combine with lambda_c^(n+1) to give lambda_zeta^(n+1). Thus the resulting leading formula is EXACTLY (2), with consistent branches. This proves (4) as a bound on the holomorphic ratio, not just on unrelated real leading approximations.

This lemma does not introduce numerical threshold values for lambda_0,n_0,C_0. They are fixed uniform analytic constants whose existence follows from the displayed compact neighborhoods, derivative bounds, and strict gaps. No effective integer threshold is claimed here.

## 4. Derivatives of the error, justified by Cauchy estimates

Increase n_0 so that C_0/n<=1/2. Define

    ell_n(zeta)=Log(1+e_n(zeta))

by the branch near zero. It is holomorphic on the preceding disks and satisfies |ell_n|<=2C_0/n. Cauchy's estimates on radius delta mu yield, for every fixed integer j>=0,

    |ell_n^(j)(mu)|
       <=2C_0 j!/[n(delta mu)^j].                        (7)

In particular the first two derivatives have bounds O(1/(n mu)) and O(1/(n mu^2)). Equation (7) is the missing derivative control. No derivative is taken merely because a real relative remainder was O(1/n).

On the positive real domain of this lemma, J_n is nonzero. The phase defined in the next section is therefore an exact continuously unwrapped phase, not a finite-order approximation to one.

## 5. Reduced phase, monotonicity, and curvature

For real m in that domain put

    gamma_n=(1-n)pi/4,
    psi_n(m)=gamma_n+n Im F(n/m,1/n)
       -(1/2)Im Log beta(n/m,1/n)+Im ell_n(m),
    Theta_n(m)=-m pi/2+psi_n(m).                          (8)

Then J_n(m)=|J_n(m)| exp(i Theta_n(m)) exactly. The constant gamma_n follows from the arguments of i/(2alpha) and (2alpha)^(-n). The square-root branch and the relative logarithm have already been specified. For real m, the factor (n/m)^(n+1) contributes no argument.

With lambda=n/m, analytic differentiation of F and Log beta, followed by (7), gives

    psi_n'(m)=-3n^2/(8m^2)
       +O(n^3/m^3+n/m^2+1/(nm)),                         (9)

    psi_n''(m)=3n^2/(4m^3)
       +O(n^3/m^4+n/m^3+1/(nm^2)).                       (10)

All implied constants in (9)-(10) are absolute within the small-lambda analytic domain. For example Im F_lambda(0,nu)=3/8+nu/4; the remaining F derivatives and the beta derivatives are bounded. The two remainder-derivative terms in (9)-(10) are precisely those furnished by (7).

On the fixed-rho block, and also on its padded block

    I_n^+=[M_--n,M_++n],

these estimates imply, for all sufficiently large n,

    n^2/(4m^2)<=-psi_n'(m)<=n^2/(2m^2),                  (11)
    n^2/(2m^3)<=psi_n''(m)<=n^2/m^3.                     (12)

Indeed the relative errors are O(n/m+1/n+m/n^3), which tend to zero uniformly there. The reduced phase is therefore strictly decreasing and strictly convex. More precisely its first and second leading coefficients in (9)-(10) have uniform relative error O_rho,C(1/log n).

This proves analytic monotonicity and curvature. It supplies no arithmetic separation of its level crossings from integers.

## 6. What is meant by a crossing in an integer parity class

For an integer m=2j+epsilon, epsilon in {0,1},

    dist(Theta_n(m),pi Z)
       =dist(psi_n(m)-epsilon pi/2,pi Z).                 (13)

Accordingly define the parity interpolant

    H_(n,epsilon)(m)=exp(i pi m/2-i epsilon pi/2)J_n(m).

At the integer nodes of parity epsilon it equals (-1)^j J_n(m). Its real-axis crossings are exactly the levels

    psi_n(r_(epsilon,k))=epsilon pi/2+k pi.               (14)

These are the relevant slowly varying crossings for the integer problem. They are NOT generally zeros of Im J_n(r) at noninteger r: the original continuation still contains the fast factor exp(-i pi r/2). This distinction fixes the interpolation convention rather than hiding a branch change.

The original continuation's own real crossings solve Theta_n(r)=k pi. They are also unique at each available level because Theta_n'=-pi/2+psi_n'<0, but their spacing is approximately two. Equation (14) is the crossing parametrization used below for each fixed integer parity.

By (11), each level in the image of I_n^+ has exactly one root in that interval. An exact parametrization is therefore

    r_epsilon(k)=psi_n^(-1)(epsilon pi/2+k pi).            (15)

The inverse is real analytic on the open level range. Extending k to a real parameter gives

    r_epsilon'(k)=pi/psi_n'(r_epsilon(k))<0,
    r_epsilon''(k)=-pi^2 psi_n''(r_epsilon(k))
                             /psi_n'(r_epsilon(k))^3>0.  (16)

In particular

    2pi r^2/n^2<=|r_epsilon'(k)|<=4pi r^2/n^2,
    4pi^2 r^3/n^4<=r_epsilon''(k)<=64pi^2 r^3/n^4.        (17)

For two successive levels in the same parity class, the positive distance between their roots is, for an intermediate xi,

    pi/(-psi_n'(xi))
       =(8pi/3)(xi/n)^2[1+O_rho,C(1/log n)].              (18)

Thus same-parity crossings have spacing asymptotic to (8pi/3)rho^2(log n)^2. The two parity families interlace, since their phase levels alternate at spacing pi/2. Their combined adjacent spacing is asymptotic to (4pi/3)rho^2(log n)^2.

The number of crossings of one parity in the original block is

    [psi_n(M_-)-psi_n(M_+)]/pi+O(1)
      =(3C/(4pi rho^2)) n/(log n log log n)(1+o(1)).      (19)

This counts real crossings, not integer exceptional nodes. It is a new consequence of the derivative bounds, compatible with the main author's discrete sparsity deduction without treating that deduction as an independently reviewed input.

## 7. Certified local conversion between distance and phase

Put B_-=M_--n, B_+=M_++n and define explicit global slope bounds on the padded block

    vmin=n^2/(4B_+^2),
    vmax=n^2/(2B_-^2).                                  (20)

The padding supplies phase variation at least n*vmin on each side, tending to infinity. Hence every nearest parity level to a point m in I_n has a crossing inside I_n^+ for sufficiently large n.

For an integer m in I_n of parity epsilon, let d_n(m) be its distance to the crossing set in (14) inside I_n^+. Write

    delta_n(m)=dist(Theta_n(m),pi Z), 0<=delta_n<=pi/2.

The mean value theorem, minimizing over all available levels, gives the exact quantitative comparison

    vmin d_n(m)<=delta_n(m)<=vmax d_n(m).                 (21)

The crossing with nearest phase level and the crossing with nearest real coordinate need not be identified to prove (21); applying the slope bounds to each level and then minimizing suffices.

A local refinement at a particular crossing r is

    |psi_n(m)-psi_n(r)-psi_n'(r)(m-r)|
       <=n^2(m-r)^2/(2B_-^3),                            (22)

when the segment between m and r stays in I_n^+. This is a controlled curvature remainder. It can refine a crossing enclosure but is not an exponentially accurate explicit formula for its location.

Equations (15), (21), and (22) give rigorous crossing coordinates and error conversion while retaining the exact saddle and relative-error phase. No truncation of (3) is used as an exact root location.

## 8. The precision forced by bounded complete primitive errors

Now take n=2^s and an eligible integer m in I_n, so that the actual U(n,m) is nonzero. Use the separate main arithmetic and exponential author statements only in their stated scopes. Let c_(n,m) be the direct-selector rational quotient and q_(n,m) its ACTUAL positive reduced denominator. Put

    K_(n,m)=2^(n+2)|J_n(m)|/|U(n,m)|>0,
    Lambda=2n+8m,
    B_E=3 Lambda^n exp(Lambda/(n+1))
               /((n+1)(n!)^2 |U(n,m)|).                  (23)

The complete logarithmic contribution has magnitude K_(n,m) sin delta_n(m). The entire exponential contribution has magnitude at most B_E. Thus

    K_(n,m) sin delta_n(m)-B_E
       <=|c_(n,m)-(e+pi)|
       <=K_(n,m) sin delta_n(m)+B_E.                    (24)

Combining (21), sin delta>=2delta/pi, and sin delta<=delta gives

    q[(2/pi)K vmin d_n(m)-B_E]_+
       <=q|c_(n,m)-(e+pi)|
       <=q[K vmax d_n(m)+B_E].                          (25)

Both q and the complete exponential term are retained. In particular, proximity to a crossing alone is not sufficient for a bounded primitive form unless qB_E is also controlled.

For a fixed H>0, boundedness q|c-(e+pi)|<=H necessarily implies

    sin delta_n(m)<=(H/q+B_E)/K.                         (26)

If the right side is less than one, this yields

    d_n(m)<=pi(H/q+B_E)/(2K vmin).                       (27)

Conversely, if H/q>B_E, the explicit sufficient condition

    d_n(m)<=(H/q-B_E)/(K vmax)                           (28)

implies q|c-(e+pi)|<=H. No claim that the hypothesis H/q>B_E holds at the prospective exceptional nodes is made. Equations (27)-(28) are necessity and conditional sufficiency, not equivalent statements after dropping the exponential residual.

## 9. Exponentially narrow integer windows with the actual dyadic cost

On eligible nodes the separate dyadic theorem gives

    q>=q2,
    q2=2^(3n/2+2m-s2(n)-s2(n+4m)).                      (29)

This is a lower bound for the fully reduced denominator; no clearer or raw forcing magnitude is substituted for q. Replacing H/q by H/q2 in (27) gives a weaker necessary condition using explicitly known arithmetic data.

The preserved relative saddle magnitude and the uniform main bound for U imply

    log K>=m log 2-(3n/2)log log n-O_rho,C(n).            (30)

Consequently

    H/(q2 K)
      <=H exp(-3m log 2+(3n/2)log log n+O_rho,C(n)).      (31)

For the second term the U factors cancel exactly before estimation:

    B_E/K=3 Lambda^n exp(Lambda/(n+1))
               /((n+1)(n!)^2 2^(n+2)|J_n(m)|).

It follows uniformly that

    B_E/K<=exp(-n log n-m log 2
                         +2n log log n+O_rho,C(n)).     (32)

Thus a bounded primitive form necessarily has

    delta_n(m)<=exp(-kappa_rho n log n+o_rho,C,H(n log n)),
    d_n(m)<=exp(-kappa_rho n log n+o_rho,C,H(n log n)),   (33)

where

    kappa_rho=min(3rho log 2,1+rho log 2)>0.              (34)

The polynomial factor 1/vmin=O_rho((log n)^2) does not alter this exponential scale. More explicitly, use (27) with q2 and the sum of the two displayed bounds (31)-(32); that is the finite-parameter condition, with their uniform analytic constants retained.

The exact m remains in (31)-(32). Its adjustment O(n log n/log log n) is o(n log n), but is NOT negligible at a finer phase scale. The use of rho in (33) is only at the stated leading exponential scale.

The second exponent in (34) is necessary in this argument: even an extremely large q does not permit discarding possible cancellation of the logarithmic term against the complete exponential residual. The relevant phase window then contains its B_E/K allowance. We do not assert qB_E tends to zero.

## 10. The exact unresolved integer-avoidance assertion

All crossings in (15) are exact analytic roots with proven uniqueness and curvature. What remains unproved is their quantitative separation from the parity lattice.

One precise sufficient assertion for all-node primitive divergence would be: for every fixed H>0 and all sufficiently large dyadic n, every eligible integer m in I_n satisfies

    dist(m,{r_(epsilon,k): epsilon=m mod 2})
       > pi(H/q2+B_E)/(2K vmin),                        (35)

with quantities as in (20), (23), and (29). By (27), this would exclude primitive magnitude at most H. It is stronger than needed if q is much larger than q2, but requires no unknown denominator upper estimate.

A simpler sufficient asymptotic version is a proved uniform separation

    dist(m,{r_(epsilon,k)})
       >=exp(-(kappa_rho-epsilon0)n log n)               (36)

for some fixed 0<epsilon0<kappa_rho and every eligible node in the block eventually. The estimates above would then force primitive divergence. Neither (35) nor (36) has been established.

Strict monotonicity, positive curvature, interlacing, spacing of order log^2 n, and the crossing count (19) do not imply either integer-avoidance statement. In particular they do not exclude a sparse sequence of roots exponentially close to eligible integers. Exact coincidences are also not excluded here by an all-index argument.

The relative saddle error is now differentiably controlled, but its leading bound is still O(1/n) in phase. Using only that phase enclosure would typically leave an uncertainty of order (log n)^2/n in a crossing coordinate. This is enormously larger than the windows (33). A finite-order expansion of F can leave still larger uncertainty. The analytic inverse definition (15) is rigorous, but it cannot be replaced by a finite-order root approximation to infer arithmetic separation.

Thus the new work characterizes the isolated crossing geometry and converts integer proximity into the correct complete primitive-error scale. It does not close the exceptional-node problem or prove irrationality.

## 11. Preservation and status

The new analytic results are the holomorphic extension with uniform relative remainder, its Cauchy derivative bounds, reduced-phase monotonicity and convexity, exact parity-interpolant crossings, and the distance-to-phase inequalities. The arithmetic consequences are conditional on the named actual-denominator and complete-exponential inputs; the analytic argument is not certified by those arithmetic facts.

No earlier file is changed, no independent examination is undertaken, and no completed computation is repeated. This note and LARGE_SELECTOR_PHASE_CROSSINGS_REPORT.md require saved-file read-back before completion is reported.
