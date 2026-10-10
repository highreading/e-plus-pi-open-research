> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Three integral jets give an omission-radius ceiling below 2.809622

Root original deduction, 2026-10-02. Author proof and exact new rational certificate; no independent review. The main irrationality question remains open and research is active.

## Target and prior-work check

Before beginning, searches of sources and the earlier session for third-jet radius, Schwarzian, higher-jet omission and integral Pick constraints located earlier endpoint beta-jet work, but no completed integral-Hurwitz pullback omission ceiling using three derivatives. The first two jets were established in the current session. A fresh primary-literature search and read of Marco Abate, *Multipoint Julia theorems*, https://arxiv.org/html/2101.03559v1, confirmed the standard iterated hyperbolic-difference-quotient framework. DLMF15.10, https://dlmf.nist.gov/15.10, supplies the hypergeometric differential equation. Neither source claims this integral-jet application or a solution of the main problem.

## Statement

Let phi have real Taylor coefficients, be holomorphic on the disk |z|<R, satisfy phi(0)=0 and phi(1)=1, and omit both 1+i and 1-i. If phi'(0), phi''(0), phi'''(0) are integers, then

    R < 2.809621359339520.                          (1)

The test number is an exact rational. Rejection on that single disk excludes every larger disk by restriction. No numerical monotonicity assertion is needed. This bounds the Taylor disk available to the archived endpoint-fixing integral-Hurwitz pullbacks of the original logarithmic function. It does not give a denominator estimate or a proof about e+pi.

## The local inverse's Schwarzian

Use the normalized covering p and its local inverse xi from the first-jet note. Write a=p'(0)>0, t=xi(1)>0 and ell=a xi''(0). The real-path lift fixes the endpoint xi composed with phi at t, independently of the sign of the initial derivative. Existing exact rational enclosures give

    a = 7.0598510014710295...,
    t = 0.19002697437635734...,
    ell = 0.68178771180186722....

For the elliptic parameter z, the equation for H=2K/pi is

    H'' + P H' + Q H = 0,
    P=(1-2z)/(z(1-z)), Q=-1/(4z(1-z)).

The ratio of two independent solutions has Schwarzian

    2Q-P'-P^2/2 = (1-z+z^2)/(2z^2(1-z)^2).

The covering coordinate xi is a Mobius transform of that ratio. Its affine parameter is z=(1-i(w-1))/2, so the chain rule gives the exact identity

    S xi(w) = ((w-1)^2-3)/(2(1+(w-1)^2)^2),
    S xi(0) = -1/4.

Since S xi=xi'''/xi'-(3/2)(xi''/xi')^2, put

    eta = -1/4 + (3/2)ell^2,
    xi'''(0)=eta/a.                                (2)

These formulas are exact, independent of the numerical enclosures.

## First and second integer choices

Set R to the rational test number in (1), s=1/R and f=the lifted xi composed with phi. Let h(z)=f(Rz)=z g(z). The first-jet piecewise bound already proved in this session excludes every integer j=phi'(0) except j=1 at this radius. Put

    x=R/a, y=Rt,
    g(0)=x, g(s)=y,
    g1(z)=(g(z)-x)/(z(1-xg(z))).

For k=phi''(0),

    B_k=g1(0)=R^2(k+ell)/(2a(1-x^2)),
    Z=g1(s)=R^2(t-1/a)/(1-tR^2/a).                (3)

The coefficient restriction |B_k|<=1 leaves k=-2,-1,0. For k=-2 and -1, the exact certificate proves

    Z > (B_k+s)/(1+sB_k),

contradicting Schwarz-Pick. Thus k=0 is forced. Its B=B_0 lies strictly between0 and1.

## Third integer choices and contradiction

For l=phi'''(0), the chain rule with j=1,k=0 gives f'''(0)=(l+eta)/a. Expand

    g(z)=x+alpha z+beta z^2+O(z^3),
    alpha=R^2 ell/(2a), beta=R^3(l+eta)/(6a).

Define g2(z)=(g1(z)-B)/(z(1-Bg1(z))). The prescribed values are

    C_l=g2(0)
       = [beta/(1-x^2)+xB^2]/(1-B^2),
    T=g2(s)=(Z-B)/(s(1-BZ)).                      (4)

All denominators are strictly positive by rational intervals. Because C_l increases affinely with l, the exact inequalities C_1>1 and C_(-2)<-1 leave only l=-1 and l=0. Both have |C_l|<1, and Schwarz-Pick would require

    -s <= (T-C_l)/(1-C_l T) <= s.                 (5)

For l=-1 the exact lower interval endpoint exceeds s. For l=0 the exact upper interval endpoint is below -s. Thus every integral third derivative is excluded, proving (1).

## Exact certificate and scope

THIRD_JET_RADIUS_CERTIFICATE.json records all input intervals, the exact Schwarzian, eta, forced derivatives and the two strict third-stage rejections. third_jet_radius_certificate.py consumes the compact rational outward intervals from SECOND_JET_RADIUS_CERTIFICATE.json; those intervals were proved from hypergeometric tails and Machin alternating series. The new computation uses only rational arithmetic. It adds no repeated old-data scan.

The decimal root2.809621359339519149... was used only to choose a convenient rational test point. The proof is the exact rejection at2.809621359339520. This substantially improves the first-jet3.6443... and second-jet3.4751... ceilings. Sharpness among all integral jets, existence of a pullback approaching this ceiling, and the arithmetic cost of any such pullback remain separate open targets.
