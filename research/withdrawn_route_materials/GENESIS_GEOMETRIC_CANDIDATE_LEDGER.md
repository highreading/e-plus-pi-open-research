> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Genesis geometric/dynamical candidate ledger

Agent 2 original research, 2026-10-02. Governing protocol: ../main/GENESIS_STAGE_PROTOCOL.md. This ledger records mechanism-level rejection, not a claim that the main rationality question has been decided. The completed determinant, moment, selector and Smith constructions are closed for this stage.

## G1. Additive arrival-time suspension — DISCARDED

Proposed object: take a two-symbol cyclic base, put roof values e and pi on its successive states, and suspend it. Equivalently take the rotation x -> x+(e+pi) on R/Z. Its two-state primitive return period is e+pi; the circle rotation has a finite orbit exactly if e+pi is rational.

Falsifiable target: show that this particular rotation has no finite orbit using the geometric construction of its two roof pieces. The exact logical bridge is present, but the target merely restates irrationality as a classical arithmetic orbit condition. Adding a new name for the two pieces would not create a new mechanism.

Archive query: suspension, roof function, phase reset, return time, rational flow and coupled flow across inherited Markdown research. The returned matches concerned administrative workflow only; no substantive matched suspension construction was located in that bounded query.

Online mechanism queries: suspension flow roof function return time circle rotation arithmetic periodic orbit; renewal flow, suspension, rational period. Opened and read the full primary Iommi–Jordan–Todd, Recurrence and transience for suspension flows, https://arxiv.org/pdf/1209.6542, especially Section 2.3 defining the suspension and its roof-time sums. The first attempted university download failed and is not counted as a read. The primary paper makes the essential public suspension construction explicit.

Decision: discard immediately. Its missing theorem is precisely the arithmetic independence we seek; familiar flow/rotation independence is disallowed by the Genesis protocol. No new lemma or numerical experiment is pursued for G1.

## G2. Cut-and-glue exponential/circular length — DISCARDED

Proposed object: an additive dissection group of oriented geometric pieces, representing the exponential segment with length e and a unit semicircle with length pi. A rational total would identify the scalar length of their disjoint union with that of a rational interval. One would seek an additional length-angle or boundary invariant obstructing that identification.

Falsifiable target: a dissection invariant vanishing on rational intervals but nonzero on this union, with an independently proved implication from rational total length to the allowed dissection equivalence. That implication is not automatic: equal scalar measure generally does not imply scissors equivalence. Adding it as an axiom would assume the required obstruction.

Archive query: scissors, Dehn invariant, cut-and-glue, translation surface. No substantive internal geometric mechanism was found in the bounded Markdown query.

Online mechanism queries: scissors congruence Dehn invariant volume transcendental length exponential circle; additive geometric valuation, mixed-dimensional scissors congruence. Opened and read the full primary Goodwillie, Scissors Congruence with Mixed Dimensions, https://arxiv.org/pdf/1410.7120, its introduction and Sections 1 and 3. Its universal valuation, cone/piece group and convolution of boundary invariants already supply the essential proposed operation. Also opened the primary Baseilhac–Benedetti quantum scissors paper, https://arxiv.org/pdf/math/0201240, as a check against an attempted quantum variant; no variant is pursued.

Decision: discard. The essential scissors/valuation mechanism is public, and the needed implication from rational total measure to geometric equivalence was unproved. No rebranding through boundary charge, quantum state sums or refined Dehn invariants is retained.

## Current scope

These are rejected mechanisms, not bounded-search novelty survivors. The next candidate must specify an operation whose proved bridge carries the actual rational normalization and does not merely encode e+pi into a rotation, a scalar geometric measure, a period torsor or a familiar independence conjecture.

## G3. Noncommutative two-clock development — DISCARDED

Proposed operation: lift the two clocks into labelled coordinate directions before concatenation. The path goes from (0,0) to (e,0), then to (e,pi); projection by (x,y) -> x+y retains the actual sum. Develop this path into a noncommutative nilpotent geometry, using a second-level area or higher ordered path invariant to distinguish the exponential and circular pieces after their scalar sum has been taken.

Falsifiable target: prove that a rational projected endpoint forces a rational (or zero) higher geometric charge, while the fixed path has an incompatible charge. This is the required logical bridge; it does not follow from a rational scalar endpoint.

Archive query: path signature, iterated integral, Chen integral, tree-like path, noncommutative path/flow/interface, commutator area and signed area. The returned internal matches concerned unrelated analytic jets. No substantive path-development mechanism was located in that bounded query.

Online synonym queries: signature of bounded-variation path, iterated integrals, tree-like equivalence, Chen concatenation, noncommutative path development and rational endpoint. Opened and read the full primary Hambly–Lyons, Uniqueness for the signature of a path of bounded variation and the reduced path group, https://arxiv.org/pdf/math/0507536, Sections 1.2–1.4. It explicitly contains the concatenation homomorphism, controlled differential equations, tensor signature, Cartan development and Heisenberg area. Also opened the fresh primary Teichmann–Schachermayer–Tissot-Daguette, An Elementary Proof of the Hambly-Lyons Uniqueness Theorem, https://arxiv.org/pdf/2609.12283. Its winding-number/subinterval mechanism is public; changing to that geometric version would not repair novelty.

Basic bridge countermodel: for any positive rational q>e, take the two-clock path with lengths e and q-e. Its projected endpoint is the rational q, but its mixed ordered integral is e(q-e). That number is transcendental: if it were algebraic, e would solve the algebraic quadratic X^2-qX+e(q-e)=0. Thus a rational projected sum is compatible with a transcendental second-level charge. The example is not the actual pi path; it refutes the proposed general inference needed to turn its extra geometric information into a contradiction. Any valid specialization would require an additional independently proved relation for the actual circular clock.

Decision: discard. The essential noncommutative operation is already public, and the rational-sum-to-higher-charge bridge fails in an explicit positive-clock countermodel. No new independence assumption, numerical signature experiment or higher-level variant is pursued.

## G4. Complementary inverse-curve exchange — DISCARDED

Precise operation: R_s(x)=tan((s-exp(x))/4), locally near the unit corner. It fixes 1 exactly when s=e+pi. Fresh archive query and opened internal complement-loop source, fresh mechanism-synonym queries, full primary Matkowski-mean/inverse-generator sources, actual local structure and the complete countermodel are saved in `GENESIS_CURVE_EXCHANGE_BRIDGE_COUNTERMODEL.md`.

Its essential inverse-additive-generator mechanism is public generalized quasi-arithmetic/Matkowski mean machinery; changing its interpretation to a curve exchange does not repair novelty. The local fixed-point index is +1 throughout the parameter neighborhood and has no rationality implication.

The bounded bridge test supplies a stronger explicit countermodel: B_N=C+x^N(6-E-C), N>=26, is positive/increasing, has rational Taylor coefficients and rational polynomial differential realization, matches any prescribed finite number of unit circular jets at 0, yet E(1)+B_N(1)=6 exactly. A valid new mechanism must use the GLOBAL fixed circular normalization rather than initial rational data, finite jets or local inverse geometry alone. This is a proved scope limitation, not a new core obstruction or an approximation family.

Current survivor count: zero. The discarded mechanisms remain discarded even when their actual e+pi specialization is unresolved.

## Conditional bridge filter after G4

Root's complementary full-monodromy/order-zero countermodel is recorded in `../main/GENESIS_EXACT_MONODROMY_ZERO_ORDER_COUNTERMODEL.md`; it is not rederived here. Our rational polynomial differential-system countermodel retains a different property. Neither result is upgraded to an actual fixed-global-law counterexample.

An additional logical filter is CONDITIONAL: if S were rational, then (6-S)x^N would be a rational-coefficient polynomial correction of the actual F=exp(x)+4 arctan(x). It preserves branch increments and is D-finite; on closed right sectors it is negligible compared with the leading exponential. It shifts F(1) to6. This is NOT an unconditional rational-coefficient D-finite counterexample with rational endpoint, since the coefficient is rational only under the hypothesis being tested. It shows why intersecting generic analytic and differential classes cannot by itself contradict that hypothesis. The exact fixed coupled global laws, beyond the broad classes, would still be needed.

No further inverse-generator, interpolation, rotation, singularity-grading or generic-flow variant has been opened as a Genesis candidate. A next candidate has not yet been formulated with a defensible new core and its required global numerical bridge. This is an open research checkpoint, not a stop or a claimed exhaustion of geometric possibilities.

## G5. Rational-initial-data exponential rotor — DISCARDED AT GATE

This was the next nonadditive law-coupled bridge checked, not a developed route. For q in Q define the entire operation

    K_q(z)=exp(i(qz-z-exp(z)+1)).

It has K_q(0)=1 and Taylor coefficients in Q(i). It is the rotor component of U'=U, K'=i(q-1-U)K with (U,K)(0)=(1,1). The actual global numerical implication is proved by substitution:

    S=q  implies  K_q(1)=exp(i(q-e))=-1.

No rational tangent, rational labelled equivalence, or algebraicity of exp(iq) is inferred. A proposed general lemma would forbid algebraic K_q(1) for every rational q. It would suffice for the main question, but it is a nested-exponential value-independence lemma, not a new geometric law.

Archive search used Schanuel, nested exponential, exponential tower and exp(i e) across inherited Markdown. It located the exact already-discarded analytic candidate A1 in `../agent3_analysis/GENESIS_ANALYTIC_CANDIDATE_LEDGER.md`, whose statement and gate were opened. The rational initial normalization above changes the presentation, not the endpoint nested-exponential mechanism. The older `work/session_20260913/classical_hypotheses_audit.md` also records exp(ie)=-exp(ir) under a rational sum.

Fresh online synonym queries covered Schanuel, nested exponentials, exp(i e), exponential towers, and algebraic roots of exponential polynomials. Opened both full primary Kirby papers: *Finitely Presented Exponential Fields*, https://arxiv.org/pdf/0912.4019, especially Section 9 and Theorem 9.2; and *Exponential algebraicity in exponential fields*, https://arxiv.org/pdf/0810.4285, its introduction, Theorems 1.1–1.4 and Section 7. The first explicitly treats nested exponential/logarithmic transcendence questions through the public exponential-field/Schanuel program. The second's unconditional weak Schanuel result over exponentially algebraically closed base fields does not supply the desired numerical assertion over Q.

For clarity, Schanuel would imply the proposed stronger lemma: the two inputs 1 and i(q-e) are Q-linearly independent, while they and exp(1)=e all lie in Qbar(e). If K_q(1) were algebraic, the relevant field would have transcendence degree one, violating Schanuel's n=2 lower bound. This is a CONDITIONAL observation only, and using it as an axiom is disallowed.

Decision: discard immediately as an archived and public nonlinear exponential-independence mechanism. No rational-rotor nonreturn assertion is proved, no dynamical variant is pursued, and this rational initial-data normalization is not counted as a new core tool. Survivor count remains zero.

## G6. Fractional-period cyclic rotor product — DISCARDED

This separate nonadditive tool takes the G5 endpoint condition only as input and attempts a global cyclic product over shifts 2pi i j/n. Full archive/primary gate and the proved exact calculation are in `GENESIS_CYCLIC_ROTOR_PRODUCT_GATE.md`. The nested exponential cancels, but the COMPLETE evaluated product is exp(i n q-pi(q-1)(n-1)), transcendental for EVERY rational q and n>=2. The gauge whose cyclic product is 1 instead makes the endpoint input transcendental under the rational-S hypothesis.

The essential trace-zero exponential norm/root-of-unity filter is public and archived. The calculation prevents treating an analytic cyclic product as a number-field norm; it does not settle S or provide an essentially new tool. No product/gauge variant is pursued. Survivor count remains zero. Genesis remains active; this is a bounded failed candidate, not a closeout or an exhaustion claim.

## Polynomial observation-jet extraction — PUBLIC CORE; SUPPORT FILTER ONLY

The exact all-polynomial arithmetic-closure statement and its fresh archive/primary gate are saved in `GENESIS_POLYNOMIAL_OBSERVATION_JET_FILTER.md`. Under S=q in Q, any P(exp(x),4 atan(x),x) with state degree d>=1 and x-degree H has a transcendental derivative at x=1 of some order at most (d+1)(H+1)-1. The H=0 bound is sharp for (exp(x)+4 atan(x)-q)^d. Both actual laws remain fixed.

Polynomial Lie-jet observation and exponential-polynomial zero-order extraction have established public essential cores, read in Baillieul1981 and Novikov--Shapiro2015. They are not retained as a Genesis operation. The statement is conditional support against silently adding algebraic tangent/jet preservation to a rational scalar closure. It does not forbid an independently proved transfer to one particular second algebraic output. No rational-observation or general differential-algebra extension is opened. Survivor count remains zero; original operation construction remains active.

## G7. Rational-parameter critical fixed-point extraction — DISCARDED AT GATE

Precise nonadditive operation: for the actual F=exp+4 atan and q in Q, form the Newton germ

    N_q(z)=z-[F(z)-q]/F'(z).

It uses the full interior law, not only its endpoint. The exact input is N_q(1)=1 if and only if S=q, because F'(1)=e+2 is nonzero. A proposed obstruction would forbid the rational point1 as a superattracting fixed point for this rational-parameter family. Such a theorem would suffice, but merely constructing its fixed point is an equivalent reformulation, not the missing arithmetic obstruction.

The basic exact properties are worth keeping as support. N_q has rational Taylor coefficients at0 since F has rational Taylor coefficients there and F'(0)=5. It satisfies N_q(0)=(q-1)/5. Under S=q the point1 has multiplier N_q'(1)=0, while

    N_q''(1)=(e-2)/(e+2)

is transcendental. Thus a nonlinear operation can prove an algebraic multiplier from the scalar equality without proving an algebraic whole jet. This does not contradict the polynomial-observation filter: division by F' is essential here. For every real q sufficiently near S, the unique nearby root x_q of F(x)=q is superattracting under N_q. The local superattracting type is therefore unchanged under q variation and does not distinguish rational q.

The actual F is multivalued in the complex plane; N_q is a germ and a meromorphic function on the corresponding continued logarithmic covering away from zeros of F'. It is NOT asserted to be a single-valued meromorphic Newton map of an entire function on C. A complete circular branch increment delta F=4 pi k changes N_q by -4 pi k/F'. No entire-Newton basin theorem is transferred across this distinction.

Archive search used `Newton map`, `Newton.method`, `Newton.iterat`, `superattract`, `polynomial.like`, and `straightening` across work and sources Markdown. The substantive Newton hit in sources/nonpolynomial_integral_hurwitz_pullback.md concerns numerical root estimates, not an arithmetic fixed-point extraction; no matching Genesis operation was found in this bounded search. The broad straightening hit was unrelated integral normalization. These are not novelty claims.

Fresh primary queries used Newton map / entire function / simple zero / superattracting fixed point / rational Taylor / arithmetic fixed point. Opened Ruckert--Schleicher, *On Newton's Method for Entire Functions*, https://arxiv.org/pdf/math/0505652 . Its Section2.1 defines N_f=id-f/f' and gives the fixed-point multiplier (m-1)/m for a root of multiplicity m; Section2.3 describes the established Newton-map operation. This is the essential same operation. Its entire-function basin conclusions are not used for the present logarithmic F. The attempted Numdam direct PDF fetch failed and is not counted as a read.

Decision: discard immediately as the public Newton critical-point mechanism. No basin, straightening, relaxed-Newton or rational-fixed-point variant is pursued. The exact conditional multiplier0 versus transcendental second derivative is scoped support, not a Genesis survivor. Survivor count remains zero; research remains active.

## G8. Rational-parameter warped-circle completion — DISCARDED

The precise full-law metric, exact endpoint bridge, primary gate and strong compact countermodel are saved in `GENESIS_WARPED_CIRCLE_COMPLETION_GATE.md`. With F=exp+4 atan, r_q=q-F and g_q=dx²+r_q²dtheta², the circle collapses at x=1 exactly when q=S. Its normalized cone angle is e+2, but rational q does not force an orbifold or finitely branched smooth completion.

The unconditional countermodel r=(1-x²)exp(-x²/4), -1<x<1, has a rational complete germ, rational initial data, rational finite pole positions, the fixed rational-coefficient ODE r''=(x²/4-5/2)r, positive bounded rational-polynomial curvature K=5/2-x²/4, a geodesic equator and compact sphere completion. Both normalized cone angles are 2exp(-1/4), transcendental. Exact Gauss--Bonnet includes both defects. This is a generic completion countermodel, not a deformation of the actual two laws or a decision about S.

Opened Battaglia et al2022's full conic-curvature primary and Borzellino et al2006 Section7's finite cyclic cone criterion. Warped/conic completion is public; the proposed arithmetic completion rule also fails. No conic Ricci, spectral, finite-cover or branched-completion continuation is opened. Survivor count remains zero; original geometric construction remains active.

## G9. Law-coupled marked SL2 axis preflight — EXACT ARCHIVE DUPLICATE; STOPPED

Preflight object was M(x)=[[E,1],[EA-1,A]], with E=exp(x), A=4 atan(x), determinant1, rational initial matrix and trace at1 equal to S. The hypothesized new step concerned an arithmetic marked axis, not merely algebraic spectrum. The FIRST archive search located the exact complete root construction `../main/GENESIS_SL2_ARITHMETIC_FRAME_FILTER.md`, G-R9. Its actual full-law moving conjugator and arithmetic-frame obstruction already cover this preflight. The source was read for overlap; no independent audit, eigenline theorem, determinant expansion or continuation was performed. Root also directed an immediate stop of this duplicate.

Fresh queries covered marked SL2 axis, character varieties, rational trace versus conjugator and algebraic eigenvalues. Opened Goldman, *Trace coordinates on Fricke spaces of some simple hyperbolic surfaces*, https://arxiv.org/pdf/0901.1404 , Section2.1 Theorem2.1.1 and its distinct-eigenvalue proof; it gives the classical single-matrix character core. Also opened his author document https://www.math.umd.edu/~wmg/CC.pdf . No unread later sections are imported. Decision: immediate discard as exact archived and public mechanism. No new result is claimed. Root ledger is consulted before the next construction. Survivor count remains zero; Genesis research remains active.
