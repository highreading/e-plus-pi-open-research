> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual two-law polynomial observations: a bounded arithmetic-closure filter

Status: proved conditional support, not a retained Genesis mechanism. This note keeps both actual global laws and assumes the scalar rationality hypothesis only where it is explicitly written. The essential polynomial-observability and exponential-polynomial zero-order tools are classical and were gated below. No irrationality conclusion or new paradigm is claimed.

## Exact object and proposed transfer

Write E(x)=exp(x), C(x)=4 atan(x), with the real branch near x=1. A polynomial geometric observation is

    f_P(x)=P(E(x),C(x),x),  P in Qbar[X,Y,Z].

Its endpoint jet is the sequence f_P^(j)(1). The exact scalar input S=e+pi=q in Q gives E(1)=e and C(1)=q-e. It does not assert that the separate state coordinates or observation derivatives are algebraic.

A tempting transfer would be to choose a nonconstant observation of the two states and infer an algebraic complete endpoint jet from an algebraic endpoint or a rational geometric closure. The theorem below proves the opposite jet conclusion CONDITIONAL ON the scalar hypothesis, for every polynomial observation that actually depends on E or C. Therefore an independently proved algebraic-jet transfer would be a decisive extra theorem, not an automatic closure rule. This is not an unconditional counterexample with a rational actual S. It does not exclude an operation that proves a particular second algebraic scalar by an independent mechanism.

## Theorem: finite detection of a transcendental endpoint derivative

Assume S=q in Q. Let P belong to Qbar[X,Y,Z], let

    d=deg_(X,Y) P >= 1,  H=deg_Z P,
    L=(d+1)(H+1).

Then there is an integer j with 0<=j<=L-1 such that f_P^(j)(1) is transcendental. Consequently all endpoint derivatives are algebraic if and only if P belongs to Qbar[Z]. If f_P(1) is algebraic, the detecting j is positive.

The coefficient field Qbar can be replaced by Q throughout. The conclusion is conditional on S being rational; it is compatible with that hypothesis and is not a contradiction to it.

### Proof

Put t=x-1 and

    g(t)=4 atan(1+t)-pi.

This is an analytic germ at zero with g(0)=0 and all Taylor coefficients rational: g'(t)=4/[1+(1+t)^2] has rational Taylor coefficients. Introduce an indeterminate U and form the polynomial in U with analytic coefficients

    A(U,t)=P(U exp(t),q-U+g(t),1+t).

Every Taylor coefficient A_j(U)=[t^j]A(U,t) belongs to Qbar[U], and

    f_P^(j)(1)=j! A_j(e).

Let P_d(X,Y,Z) be the nonzero component homogeneous of degree d in X,Y. The coefficient of U^d in A is exactly

    R(t)=P_d(exp(t),-1,1+t)
        =sum_(a=0)^d p_a(1+t) exp(a t),

where p_a are polynomials over Qbar of degree at most H, and at least one is nonzero. The lower-degree state components, q, and the complete arctangent increment g(t) do not affect this leading coefficient. None of them is being discarded from the actual observation; this is a coefficient extraction in an exact polynomial identity.

R is not identically zero. Indeed, distinct integer exponential rates are linearly independent over polynomials. One elementary proof takes the largest a with p_a nonzero, divides by exp(a t), and lets real t tend to positive infinity: the remaining terms decay exponentially while the nonzero polynomial p_a(1+t) cannot do so. Repeating would force every p_a to vanish.

The monic constant-coefficient operator

    product_(a=0)^d (D-a)^(H+1),  D=d/dt,

of order L annihilates R. Therefore R cannot have all derivatives of orders 0 through L-1 zero at the ordinary point t=0: uniqueness for this homogeneous linear initial-value problem would imply R identically zero. Choose j in that range with [t^j]R nonzero. Then A_j(U) has degree exactly d, since its U^d coefficient is nonzero. Its evaluation A_j(e) is transcendental: an algebraic value would give a nonzero polynomial over Qbar satisfied by e, contradicting the classical transcendence of e. Multiplication by nonzero j! preserves transcendence.

This proves the forward claim. If P depends only on Z, every derivative of P(x) at the algebraic point x=1 is algebraic, proving the stated equivalence. QED.

## Boundary examples and precise limitations

For P=X+Y the endpoint is q under the hypothesis, but its first derivative is e+2, transcendental. Thus even the actual total observation has no algebraic tangent consequence.

For any positive integer d take

    P=(X+Y-q)^d.

Its endpoint derivatives of orders 0 through d-1 vanish, while

    f_P^(d)(1)=d! (e+2)^d

is transcendental. Here H=0 and L-1=d, so the finite detection bound is sharp. Arbitrarily many algebraic or zero endpoint derivatives can coexist with the hypothetical rational total; bounded jets alone therefore do not create an arithmetic closure.

The theorem addresses polynomial observations, not arbitrary analytic changes of coordinates, rational observations with possible pole cancellations, or a full classification of algebraic differential outputs. No such extension is asserted. A nonconstant polynomial in the state variables cannot become independent of them along the actual germ in the way required by a fully algebraic endpoint jet; the proof uses the complete actual laws rather than a deformation of them.

The conclusion also does not say every derivative is transcendental. The displayed powers give explicit zero lower derivatives. It says some derivative in a quantified finite range is transcendental whenever the polynomial genuinely depends on the states.

## Archive and primary mechanism gate

Before treating endpoint-jet extraction as a possible tool, the archive search covered work Markdown with `observab`, `Lie.derivative`, `exponential.polynomial`, `zero.order`, and `multiplicity.estimate`. Relevant sources inspected were:

- main/GENESIS_PERIODIC_FINITE_TYPE_BOUNDARY.md: its classical constant-coefficient exponential-polynomial solution discussion and the existing example F'(1)=e+2.
- agent1_arithmetic/GENESIS_SYNCHRONIZED_REPLICATION_BACKBONE.md: its ordinary algebraic classification of algebraic P(e)+c pi outputs, which is support and does not transfer arithmetic closure.
- agent3_analysis/GENESIS_TWO_LAW_TRANSPORT_COMMUTATOR_GATE.md: its exact two-law transport and the explicit loss of the scalar parameter under natural noncommuting comparisons.
- agent2_selector/GENESIS_CURVE_EXCHANGE_BRIDGE_COUNTERMODEL.md, Section5: complete Taylor field Q(e) for the already discarded inverse-generator map. The present statement classifies a different, full polynomial observation class; it does not reopen that inverse map.

The many old weighted-moment observability hits concern completed selector recurrences and were not treated as a Genesis route or reused here.

Fresh public queries included `polynomial dynamical systems algebraic observability Lie derivatives polynomial primary paper`, `exponential polynomial multiplicity zero constant coefficient differential equation order bound primary paper`, and the exact primary titles found by those searches.

Opened and read relevant full primary texts:

1. John Baillieul, *Controllability and observability of polynomial dynamical systems*, Nonlinear Analysis5 (1981),543-552, https://d-biswa.github.io/Teaching/RM20_JB_ContObsvPoly.pdf . Section1 defines polynomial Lie derivatives; Section3, especially Theorem3.1 and its proof, identifies observation indistinguishability with equality of complete Lie-derivative jets and gives finitely verifiable algebraic conditions. Thus Lie-jet extraction as a geometric observation operation has an established public essential core.
2. Dmitry Novikov and Boris Shapiro, *On global non-oscillation of linear ordinary differential equations with polynomial coefficients*, https://arxiv.org/pdf/1503.04026 . Definition1 and the constant-coefficient discussion around equation(5) were read. They explicitly place polynomial-times-exponential solutions and multiplicity/disconjugacy questions in the classical linear-ODE setting. Only the elementary order-L initial-value uniqueness argument is used in this note; none of their stronger global zero bounds is imported.

The MDPI full-text open and the Max Planck JACM PDF open failed; they are not counted as reads or proof sources.

Gate conclusion: the essential observability/zero-order mechanism is public and is discarded as a Genesis candidate. The theorem is a scoped, exact support filter for future genuinely different operations. A different new tool must prove the needed scalar-to-object arithmetic consequence without assuming polynomial observation jets are algebraic. Genesis construction continues; this checkpoint is not a closeout.
