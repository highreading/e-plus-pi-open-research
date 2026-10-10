> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A sharper pullback-radius ceiling from an integral first jet

Root original deduction, 2026-10-02. This is a working research theorem with a complete author proof and a new exact rational constant certificate. It has not received independent review. It concerns an arctangent pullback construction; it does not decide the rationality of e+pi.

## 1. Target, archive check and primary sources

The archive's `sources/universal_pullback_radius_bound.md`, independently reviewed at its original scope, proves the sharp unrestricted holomorphic ceiling R*=5.262410788162385... for endpoint-fixing maps avoiding 1+i and 1-i. Its Section 3 explicitly leaves the integral-Hurwitz class unaddressed. `sources/sparse_multijet_pullback_radius_improvement.md` proves a lower construction radius greater than1.747, with phi'(0)=1. Searches of sources/work for derivative radius bounds, integer first jets and Pick jet constraints found no completion of the present target. The old unrestricted theorem was read and is not re-proved or counted as new.

Primary searches concerned multipoint Schwarz-Pick and interpolation derivatives. Opened Marco Abate, *Multipoint Julia theorems*, author-hosted primary text https://pagine.dm.unipi.it/abate/articoli/artric/files/multiJulia.pdf, especially its introduction and hyperbolic difference-quotient formulation. Opened Kim, Ma and Ma, *Estimates of the hyperbolic metric on the twice punctured plane*, primary publisher PDF https://www.acadsci.fi/mathematica/Vol40/vol40pp875-887.pdf, for the omitted-value metric context. Opened the NIST DLMF elliptic/hypergeometric equations https://dlmf.nist.gov/19.4 and https://dlmf.nist.gov/15.10, taking care that K in this note uses the parameter, whereas DLMF Chapter19 uses the modulus. The applied Schwarz-Pick argument below is classical; no new general interpolation theorem is claimed.

## 2. Constants and theorem

Let

    F(w)=4 arctan(w/(2-w)),
    Omega=C minus {1-i,1+i},
    H(z)=sum_(k>=0) binom(2k,k)^2 z^k/16^k.

At z1=(1+i)/2 write H(z1)=A+iB. Both A>B>0. Define

    t=B/A=1/R*,
    a=2pi(A^2-B^2),
    R_j=[|t-j/a|+jt/a]^(-1/2), j in Z.             (1)

The denominator in (1) is positive for every integer j. The exact rational certificate proves

    1<a t<2,
    max_(j in Z) R_j=R_1,
    R_1<3.644263188060718.                         (2)

Theorem. Suppose phi is holomorphic on a disk |z|<R, R>1, has real Taylor coefficients, fixes phi(0)=0 and phi(1)=1, and avoids 1+i and1-i on that disk. If phi'(0)=j is an integer, then

    R<=R_j<=R_1<3.644263188060718.                 (3)

In particular every endpoint-fixing integral-Hurwitz polynomial satisfies this ceiling for the Taylor radius of F composed with phi. Only its first jet is needed for the upper bound; the higher integral jets can impose additional restrictions.

High-precision diagnostics give

    a=7.0598510014710295051...,
    t=0.1900269743763573432...,
    R_0=2.293994504823929...,
    R_1=3.644263188060717...,
    R_2=2.607331352435247....

The strict bound in (2) is certified by rational arithmetic, not those diagnostics.

## 3. Normalized covering map

Let p:D->Omega be the universal covering normalized by p(0)=0 and p'(0)>0. Reflection in the real axis lifts to reflection in the diameter through0. Therefore p is real on that diameter, and the lift of the real path from0 to1 ends at a positive real point. The inherited modular-uniformization calculation identifies this point as t=B/A: its hyperbolic distance from0 is2 artanh(t), precisely the distance between0 and1 in Omega. Thus

    p(t)=1.

The covering derivative is p'(0)=a. To check its exact normalization, the inherited inverse lambda coordinate is tau(z)=i K(1-z)/K(z), with K using the parameter. Its derivative is

    tau'(z)=-i pi/[4z(1-z)K(z)^2].

This follows from the hypergeometric differential equation's Wronskian, whose constant is fixed by K(z)->pi/2 and K(1-z)~(1/2)log(16/z) at0. Since |z1(1-z1)|=1/2 and Im(tau(z1))=(A^2-B^2)/(A^2+B^2), the curvature-minus-one density is

    lambda_Omega(0)=1/[pi(A^2-B^2)].

A normalized disk covering has lambda_Omega(0)p'(0)=lambda_D(0)=2. This gives a exactly as in (1), without changing the curvature convention.

The real-path assertion also resolves the covering branch. A real-coefficient phi maps [0,1] into the real axis; any backtracking there is homotopic to the straight path while avoiding the two off-axis punctures. The lift of phi therefore has endpoint t, rather than an arbitrary deck translate. No unproved nearest-branch selection is used.

## 4. One Schur step and the radius inequality

Lift phi to f:D_R->D with f(0)=0, so phi=p composed with f. Then

    f(1)=t, f'(0)=j/a.

Set h(z)=f(Rz). By Schwarz's lemma h(z)=z g(z), with g holomorphic fromD into the closed unit disk. Its specified values are

    g(0)=Rj/a,
    g(1/R)=Rt.

The boundary-constant case, if present, is included by continuity. Schwarz-Pick on these two real values gives

    |Rt-Rj/a|/[1-R^2 jt/a]<=1/R.                 (4)

For an admissible nonboundary pair the denominator is positive: both specified values lie in(-1,1). Multiplying (4) yields

    R^2[|t-j/a|+jt/a]<=1,

which is (3). If a boundary case made the denominator zero, equality of the two boundary values would force j/a=t, hence j=a t, contradicting the certified fact1<a t<2 and integer j. Thus no exceptional division is hidden.

For j<=0 the bracket in (1) is t+|j|(1-t)/a and increases as j moves away from0. For positive j<a t it is t-j(1-t)/a and decreases toward a t. For j>a t it is j(1+t)/a-t and increases away from a t. Hence1<a t<2 reduces the global integer maximum to j=1 or2, together with j=0. The new certificate compares those three exactly and gives R_1 as the maximum.

## 5. Sharpness with only the first-jet constraint

The bound R_1 is attained in the larger class where coefficients are real and only phi'(0)=1 is constrained. Put R=R_1 and x=R/a. The equality in (4) is realized by

    g(z)=(x+z)/(1+xz),
    h(z)=z g(z),
    phi(z)=p(h(z/R)).

Here h mapsD intoD, phi(0)=0, phi'(0)=1, and (4) at equality ensures phi(1)=1. Thus the upper bound is sharp for this intermediate analytic class. The remaining derivative jets of this extremal map are not asserted to be integral; this is not an arithmetic construction attaining the bound.

## 6. New exact certificate and implications

`FIRST_JET_RADIUS_CERTIFICATE.json` records rational intervals for A,B,t,a,pi, the inequality1<a t<2, comparison of j=0,1,2, and the strict decimal upper bound. The new script sums H through180 using the inherited geometric tail bound as a definition-level helper. It encloses pi by the alternating arctangent series in the classical identity pi=16 arctan(1/5)-4 arctan(1/239), each through index100. Exact square comparisons give (2). The old universal-radius certificate is not rerun.

The integer first jet lowers the analytic ceiling from5.2624... to3.6443.... The known integral-Hurwitz construction with radius greater than1.747 remains admissible; a substantial interval is still open. Since this ceiling is a fixed constant, it supplies no factorial-scale arithmetic gain and no bound on the primitive endpoint gcd. A successful mixed approximation still needs its complete actual denominator argument.

The next original target is to apply further Schur steps to the second and higher integral jets, with the branch and elliptic normalization above retained. Research continues; no main-problem stopping condition has been met.
