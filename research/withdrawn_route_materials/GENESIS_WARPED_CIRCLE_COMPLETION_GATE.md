> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Warped-circle completion: exact actual bridge and compact rational-curvature countermodel

Status: discarded Genesis candidate. The actual operation retains the complete interior exp/arctangent law, but its essential cone-completion framework is public and the proposed arithmetic completion rule fails. No rationality decision or new global mechanism is claimed.

## Precise operation and numerical bridge

For a scalar q define F(x)=exp(x)+4 atan(x) on the real branch and

    r_q(x)=q-F(x),
    g_q=dx^2+r_q(x)^2 dtheta^2,  theta in R/(2 pi Z).

This is an intrinsic rotationally symmetric Riemannian metric wherever r_q is positive. It is not asserted to be an isometric surface of revolution in Euclidean three-space; the axial coordinate x is already arclength and the radius slope can exceed1.

The exact scalar-to-object implication is

    q=S=e+pi  iff  r_q(1)=0.

Since F'(x)=exp(x)+4/(1+x^2)>0, under this equality r_q is positive on [0,1), and the metric completion collapses the circle at the finite axial coordinate1. If q is rational, the COMPLETE Taylor germ of r_q and g_q at0 has rational coefficients, and the outer radius r_q(0)=q-1 is rational. No separate arithmetic assertion about e or pi has been introduced.

The interior curvature is exactly

    K_q(x)=-r_q''(x)/r_q(x)
          =[exp(x)-8x/(1+x^2)^2]/[q-exp(x)-4 atan(x)].

Thus the operation retains interior information after the endpoint reduction. Its curvature is not merely a function of the scalar S. It need not be positive on the whole interval.

Put t=1-x. Under q=S,

    r_q(1-t)=(e+2)t+O(t^2).

The distance to the collapsed circle is t: every path has length at least its axial-coordinate change, and a meridian attains that length. The circumference divided by the radial distance consequently tends to

    2 pi (e+2).

The normalized tangent-cone angle is e+2, which is transcendental. A smooth point would require normalized angle1; a finite orbifold quotient would require 1/m for a positive integer m. Even allowing a finite branched cover followed by a finite orbifold quotient can only multiply the normalized angle by a nonzero rational factor, and cannot turn e+2 into a rational value.

The proposed contradiction step was a general arithmetic completion rule: rational analytic germ, rational axial collapse coordinate and rational curvature/initial laws would force finite orbifold or finite branched smooth completion. That step has NOT been derived from S rational. The countermodel below refutes this rule in a substantially stronger generic setting. It does not change or decide the actual F.

## Unconditional compact countermodel with positive polynomial curvature

Consider the entire even radius

    r(x)=(1-x^2) exp(-x^2/4),  -1<x<1,
    g=dx^2+r(x)^2 dtheta^2.

All Taylor coefficients at0 are rational. The initial data are r(0)=1 and r'(0)=0; the equatorial circle is geodesic. The radius is positive inside the interval and vanishes at the two rational axial coordinates -1 and1. Its first-order endpoint slopes are

    r'(1)=-2 exp(-1/4),
    r'(-1)=2 exp(-1/4).

An exact differentiation gives

    r''(x)=[x^2/4-5/2]r(x),
    K(x)=-r''(x)/r(x)=5/2-x^2/4.

Hence the complete curvature law is a rational-coefficient polynomial, bounded between 9/4 and5/2 on [-1,1]. The radius satisfies a second-order linear ODE with rational polynomial coefficients and rational initial data. No numerical integration, guessed equality, or arithmetic endpoint assumption enters this construction.

The metric completion is compact and topologically a two-sphere: each endpoint circle is collapsed to one pole. Near each pole, circumference/radial-distance tends to

    2 pi alpha,  alpha=2 exp(-1/4).

By classical Lindemann-Weierstrass, exp(-1/4) is transcendental; so alpha is transcendental. Thus neither pole is a smooth point or a finite Riemannian orbifold point, nor can any nonzero finite branching/quotient factor make its normalized angle rational. No claim is made that the absolute product 2 pi alpha is algebraic or transcendental; the proven arithmetic assertion concerns the normalized angle alpha.

This supplies an UNCONDITIONAL counterexample with all the following properties simultaneously:

- complete rational radius/metric germ at0 and rational initial data;
- fixed finite linear polynomial ODE over Q;
- bounded positive rational-polynomial Gaussian curvature;
- rational finite axial distance to both collapsed circles;
- compact topological-sphere completion and an equatorial geodesic;
- irrational, indeed transcendental, normalized tangent-cone angles.

Gauss-Bonnet does not repair the arithmetic completion claim. Directly,

    integral K dA=-2 pi [r'(1)-r'(-1)]=8 pi exp(-1/4).

The two cone defects sum to 4 pi-8 pi exp(-1/4), so the total is exactly4 pi, as required by the Euler characteristic2. The interior integral and singular defects cancel normally; rational curvature coefficients do not make the curvature integral rational.

The simpler one-sided preliminary radius (1-x)exp(2x-x^2), with K=6-4(1-x)^2 and normalized endpoint angle e, also works. The even construction above strengthens it to compactness, two rational poles, positive bounded polynomial curvature and a geodesic equator. Neither is presented as an essentially new geometric paradigm: both are explicit polynomial-Gaussian Jacobi profiles within classical warped/conic geometry.

## Archive and primary mechanism gate

The initial object, scalar bridge and falsifiable completion claim were stated before this gate. Archive search covered work and sources Markdown with `cone.angle`, `conical.metric`, `warped.product`, `orbifold`, `Troyanov` and `Gaussian.curvature`. All returned curvature hits concern old analytic saddle Hessians rather than Riemannian conical completion. No same Genesis construction was located in that bounded archive search; this is not a global novelty assertion.

Fresh public searches used prescribed curvature / conical singularity / rotational warped metric / rational curvature / irrational cone angle / Jacobi equation / finite orbifold cone angle. Opened full relevant primary sources:

1. Battaglia, Jevnikar, Wang and Yang, *Prescribing Gaussian curvature on surfaces with conical singularities and geodesic boundary*, https://arxiv.org/pdf/2011.01505 . Its introduction defines an arbitrary positive cone angle 2 pi(1+alpha), explicitly allows angles above and below2 pi, and places the operation in the established prescribed-conic-curvature framework. No existence theorem from that paper is imported for our explicit metric.
2. Borzellino, Jordan-Squire, Petrics and Sullivan, *On the existence of infinitely many closed geodesics on orbifolds of revolution*, https://arxiv.org/pdf/math/0602595 . Section7 was opened and read, including the finite cyclic quotient tangent-cone criterion and the normalized-angle condition1/m. Its closed-geodesic and Euclidean-embedding claims are not imported for our intrinsic warped metric. The finite-quotient tangent-cone condition applies intrinsically.

Troyanov's original author PDF timed out; the CORE PDF returned403; the later published author PDF returned502. These are not counted as reads. The successful full primary reads above are the gate sources.

Decision: discard. Warped-circle/conic completion has a public essential core, and its proposed rational-data-to-finite-orbifold arithmetic rule is false. The actual scalar equality supplies a cone at a rational axis, not a smooth or finite-orbifold completion. Requiring such a completion would add the decisive missing property rather than prove it. No orbifold, curvature-flow, spectral or branched-cover variant is pursued. Genesis survivor count remains zero; construction work remains active until root steering or the quota/proof stop.
