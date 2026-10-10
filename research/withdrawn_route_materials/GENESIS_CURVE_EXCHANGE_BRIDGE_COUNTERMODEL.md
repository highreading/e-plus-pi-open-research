> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Curve exchange: exact bridge and a rational-data countermodel

Agent 2 original bounded candidate test, 2026-10-03. Status: DISCARDED, not a Genesis survivor. This note records the precise mechanism and its bridge failure; it does not pursue an old approximation family.

## 1. Candidate and completed mechanism gate

Put E(x)=exp(x) and C(x)=4 arctan(x). The proposed operation, locally near x=1 for s near S=e+pi, is

    R_s(x)=C^(-1)(s-E(x))=tan((s-exp(x))/4).

It exchanges an exponential curve output with the complementary circular cumulative coordinate. Its actual logical bridge is exact:

    R_s(1)=1  iff  s=e+pi.

The desired falsifiable obstruction would be: when s is rational, no rational unit corner can be fixed, because a rigid geometric index or arithmetic multiplier forces a forbidden compatibility. It is NOT assumed as an axiom.

Archive search covered Matkowski means, quasi-arithmetic mean, complement/inverse, boundary exchange, clock exchange and rational fixed point. The matching inherited `work/item340_beta_full_complement_loop_correlation_report.md` was opened at its definition and theorem. It concerns a canonical Ostrowski residue-complement loop, not these real inverse curves; it is acknowledged overlap in terminology only. Other matches were unrelated Schur inverses.

Online queries covered different-generator inverse-sum means; inverse-complement reflections; mean invariance; and complementary cumulative-coordinate exchange. Opened and read full primary Tibor Kiss, Regular solutions of a functional equation derived from the invariance problem of Matkowski means, https://arxiv.org/pdf/2203.16862, introduction and Section 2. Its public operation M(f,g)=(f+g)^(-1)(f(u)+g(v)) uses exactly the same additive-generator/inverse coordinate mechanism. The fixed level set f(u)+g(v)=s has coordinate transition v=g^(-1)(s-f(u)); thus R_s is a level-set transition of that existing operation. Also opened the primary Devillet–Matkowski inverse-composition/addition paper, https://arxiv.org/pdf/1807.04811. There is no essential-new-operation claim.

Decision: discard at the public-mechanism gate. The elementary calculations below additionally identify why local geometry, rational initial differential data and finite circular jets cannot provide the missing arithmetic implication. They are countermodels, not a retained independence program.

## 2. Actual local structure

The function F=E+C has F'(x)=exp(x)+4/(1+x^2)>0. Hence s near S gives a unique local fixed point x_s=F^(-1)(s), depending analytically on s. At the actual unit point,

    R'_S(1)=-e/2.

The local fixed-point index is sign(1-R'_s(x_s))=+1 for EVERY nearby s, because R'_s<0. The actual fixed point is repelling since e>2. These geometric properties are stable under small changes of s; no rational/irrational distinction follows from them. The nonalgebraic multiplier does not contradict a rational fixed point or rational parameter.

## 3. Stronger positive-clock countermodel with arbitrary finite circular jets

For every integer N>=26 define

    B_N(x)=C(x)+x^N(6-E(x)-C(x)),  0<=x<=1.

Then ALL of the following are proved:

* E and B_N are increasing real-analytic clocks on [0,1].
* Their Taylor coefficients at 0 are rational, E(0)=1 and B_N(0)=0.
* B_N agrees with the complete unit circular clock C through derivative order N-1 at 0.
* E(1)+B_N(1)=6 exactly, while E(1)=e remains transcendental.
* Both clocks are polynomial outputs of ONE finite-dimensional polynomial differential system with rational coefficients and rational initial data.

These claims do not identify B_N with the actual C globally. That global difference is precisely what any valid actual obstruction must detect.

Proof of positivity: E,C increase. The elementary bounds e<11/4 and pi<22/7 give

    delta=6-e-pi>3/28.

The exponential bound follows by summing through degree 4 and bounding the remaining factorial tail by (1/120)/(1-1/6). The classical circular bound has the direct positive identity

    22/7-pi=integral_0^1 x^4(1-x)^4/(1+x^2) dx>0.

Differentiating the COMPLETE B_N gives

    B'_N=C'(1-x^N)+N x^(N-1)(6-E-C)-x^N E'.

Therefore for 0<x<=1,

    B'_N>=C'(1-x^N)+x^(N-1)(N delta-x e)>0,

because N delta>=26 delta>39/14>11/4>e. At 0 the derivative is 4. The rational Taylor coefficients follow from those of exp and arctan and the integer polynomial x^N; the agreement of jets follows because the added term has a zero of order N at 0. The endpoint identity is exact substitution, with no approximation or numerical experiment.

For the polynomial differential realization, use states x,u,w,c with

    x'=1, u'=u, w'=-2xw^2, c'=4w,
    (x,u,w,c)(0)=(0,1,1,0).

They satisfy u=exp(x), w=1/(1+x^2), c=4 arctan(x). The output b=c+x^N(6-u-c) is an integer polynomial in the states. Thus even rational polynomial dynamics with rational initial data, positivity, and any preassigned finite number of exact circular jets admit a rational terminal clock sum with a transcendental constituent.

In the corresponding inverse exchange R^N_6=B_N^(-1)(6-E), the unit point is fixed and its derivative is

    (R^N_6)'(1)=-e/(N delta-e).

This is negative and the fixed-point index remains +1. No claim that this multiplier is algebraic or transcendental is needed. All inverses in the statement are local inverses with positive B'_N, so no endpoint or zero division is hidden.

## 4. Consequence for further Genesis candidates

An actual bridge must use the GLOBAL fixed unit circular law, or other genuinely additional arithmetic structure. Rational initial data, increasing clocks, arbitrary finite jet agreement, existence of an analytic inverse exchange and its local index are insufficient, as the explicit family above proves. This countermodel does not settle S rationality, does not permit replacing C by B_N in the main problem, and is not nominated as an essentially novel core tool. No further mean/inverse-curve variant will be developed under a new name.

## 5. Exact Taylor field of the actual exchange

This is a bounded clarification of the discarded G4 operation, not a new candidate. It keeps BOTH actual global functions. Let R=R_S. For every j>=1,

    R^(j)(1)=sum_{a=1}^j {j brace a} T_a(1) (-e/4)^a,

where {j brace a} is a Stirling number of the second kind, T_0(t)=t and

    T_(a+1)(t)=(1+t^2) T'_a(t).

Here T_a is the classical tangent derivative polynomial: (d/dz)^a tan(z)=T_a(tan(z)). The formula follows from the classical Bell-polynomial chain rule, since every positive derivative of (S-exp(x))/4 at x=1 is -e/4 and tan(pi/4)=1. Equivalently the exponential-series Bell polynomial B_(j,a)(z,z,...,z) is {j brace a} z^a.

Induction gives T_a in Z[t] with nonnegative coefficients and T_a(1)>0 for every a. For a>=1 the derivative polynomial is nonconstant, and multiplying its derivative by 1+t^2 preserves a positive coefficient. Thus R^(j)(1) is a nonconstant rational polynomial in e of degree EXACTLY j, with leading coefficient T_j(1)(-1/4)^j. Since e is transcendental, EVERY positive-order derivative R^(j)(1) is transcendental. No cancellation of its leading coefficient is possible.

Moreover the field generated over Q by the entire Taylor jet of R at 1 is EXACTLY Q(e): every jet entry belongs to Q(e), while R'(1)=-e/2 generates e. This statement is unconditional for the actual R_S. Under the additional hypothetical assertion S in Q, the defining reflection parameter is rational and the fixed corner is rational, yet this complete actual Taylor field remains Q(e), not Q. Consequently rationality of the total does not supply rational-Taylor closure for this actual global transport. This is a precise failure of that proposed extra implication; it does not contradict the rational-total hypothesis itself and makes no new geometric-independence or novelty claim.

The analytic agent's separately constructed reflection F^(-1)(1+S-F(x)), F=exp+4 arctan, is not literally this map but has the same public inverse-generator core. Its endpoint derivative -5/(e+2) supplies a complementary actual-law rational-transport failure. That result is credited to the analytic agent rather than rederived here.
