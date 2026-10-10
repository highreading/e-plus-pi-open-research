> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational trace and the entire positive-radical tower

Status: conditional structural theorem / bridge filter. Not a solution of the main problem; no new paradigm or retained Genesis route is claimed. The proposed idea that positive-root enrichment must break the hypothetical e--pi field exchange is false at the purely algebraic level.

## Gate

Archive queries: finite-order automorphism, involution, real-closed, field reflection, Artin--Schreier. The inspected archive hits were unrelated conic/jet involutions; Agent3 independently identified the scalar-field involution as a true conditional consequence, without a completion extension. The radical-tower extension below was not present in those inspected sources. This is a bounded archive check.

Fresh public queries covered finite-order automorphisms of algebraically closed fields and Fermat-curve function fields/coordinate exchange. Opened primary papers https://arxiv.org/pdf/1409.3063 and https://www.numdam.org/item/ASNSP_1997_4_24_3_551_0.pdf on established curve automorphism theory. The latter's initial full PDF fetched, while a subsequent text find failed; no unseen extracted result is used. Opened Keith Conrad's complete author proof https://kconrad.math.uconn.edu/blurbs/galoistheory/artinschreier.pdf and the initial full https://www.sa-logic.org/sajl-v2-i2/10-Luciano-SAJL.pdf; a later positional fetch of the latter failed. Fermat-coordinate symmetry, Kummer/field-automorphism extension and Artin--Schreier are classical public mechanisms. This algebraic-symmetry route is DISCARDED by the novelty gate; only the following short exact implication is retained as a candidate filter.

## General theorem, independent of the e+pi question

Let x,y>0 be real, x transcendental, and x+y=r in Q, r>0. Set

    L_n=Q(x^(1/n),y^(1/n)),
    L=union_(n>=1) L_n = Q(x^q,y^q : q in Q),

where all powers denote their actual positive real branches and the union is directed by divisibility. There is a field automorphism sigma of L of order2 satisfying

    sigma(x^q)=y^q,  sigma(y^q)=x^q  (q in Q).

Thus rational trace is compatible with a coherent exchange of ALL positive rational powers. Positivity of these designated roots does not itself force preservation of the ambient real ordering.

Proof. For each n, U^n+V^n-r is absolutely irreducible. Indeed choose a root alpha of U^n-r in Qbar. It is simple since r!=0. As a polynomial in V over Qbar[U], V^n+(U^n-r) is Eisenstein at U-alpha: the constant term is divisible exactly once, the intermediate coefficients vanish, and the leading coefficient is1. For n=1 irreducibility is immediate. Hence the same polynomial is irreducible over Q(U).

Since u=x^(1/n) is transcendental, substitution U->u identifies Q(U) with Q(u) and preserves irreducibility. The actual positive v=y^(1/n) satisfies v^n+u^n=r and has degree n over Q(u). Therefore the function field of U^n+V^n=r embeds faithfully as Q(u,v). Interchanging U,V defines a field involution sigma_n with sigma_n(u)=v and sigma_n(v)=u.

For n|m, the actual positive branches satisfy x^(1/n)=(x^(1/m))^(m/n) and the same equality for y. Consequently sigma_m restricts to sigma_n. They define a compatible involution on the directed union L. It is nonidentity because x=y would imply x=r/2 rational. Every rational power lies in one such field, proving the claimed formula. This is a proof using classical irreducibility and coordinate symmetry, not a new axiom.

## Conditional application to the actual constants

If S=e+pi=r is rational, the theorem applies with x=e,y=pi. In particular the hypothetical symmetry survives adjoining every exp(q)=e^q for rational q together with every positive pi^q. No rational-power-only algebraic contradiction follows merely from distinguishing the verbal origins of these elements.

Already at n=1 the fixed field is Q(e*pi). To see this, Q(e)=Q(t) under t->e, sigma(t)=r-t, and p=t(r-t) is fixed. The element t has degree2 over Q(p), satisfying t^2-r t+p=0; the nontrivial exchange gives the quadratic fixed field exactly Q(p).

The automorphism is NOT order preserving: e<3<pi, so e-3<0 but sigma(e-3)=pi-3>0. These separate inequalities have elementary exact bounds: e<49/18<3, and the alternating arctangent lower sum through j=7 gives pi>135904/45045>3. Neither uses any rationality assumption about S.

It is also not continuous for the inherited real topology. A rational sequence q_j->e is fixed pointwise by sigma. Continuity at e would imply sigma(e)=lim sigma(q_j)=e, whereas sigma(e)=pi. This proves the exact missing convergence bridge rather than silently imposing it.

No extension preserving the ambient real ordering or analytic evaluation is implied. If one asks for a finite-order extension to an algebraically closed field while fixing i, classical Artin--Schreier supplies an obstruction: a nonidentity finite-order automorphism has order2 and sends i to -i. Such a fixed-i extension is not supplied by scalar rational trace in the first place, so that obstruction cannot refute the main hypothesis.

## Consequence for candidate construction

Adding all designated positive rational powers, rational trace/norm and finite field operations remains compatible with the hypothetical exchange. A future operation must prove an additional value-sensitive condition from the actual defining laws. Merely requiring an automorphism to preserve exp as a function or real limits would insert a new, unproved extension premise. The present note excludes that unsupported shortcut; it does not prove that e+pi is rational, irrational or undecidable.
