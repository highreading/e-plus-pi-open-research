> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational corrections exact for both ordinary and exponential periods

2026-10-02. Original author target after the rational pole-distribution interfaces. The question is whether extra rational poles can suppress the companion error while introducing no extra constants and no new e residue response. This gate gives an exact classification and arithmetic interface; it does not claim improved approximation.

## Search and overlap before this target

Archive query terms included `D^2+D`, second/first derivatives, twisted residues, rational correction/antiderivative, exponential exact rational functions, and rational gauges. Read `sources/explicit_mixed_pair_tensor_gauge_no_go.md`, especially the rational splitting equation R′+R=r in Section8. This is explicit overlap: a rational twisted primitive introduces no new exponential constant. Read the integral/error specialization in `sources/independent_root_of_unity_exp_log_pade_audit.md`; the archived warning about incomplete mixed norm/height arguments applies. The root's current integral first-jet pullback work concerns avoiding two arctangent branch points with integral Hurwitz jets; this is a different local principal-part question.

Fresh primary search concerned rational exactness under ordinary/exponential Hermite reduction, rational interpolation, and rational quadrature. Opened Bostan–Chyzak–Lairez–Salvy full paper https://arxiv.org/pdf/1805.03445, Sections1 and3, for generalized reduction and integration-factor exactness. A Vanderbilt author-hosted rational-interpolation PDF timed out, and the requested PMC rational-approximation article returned a browser gate; neither is counted as an opened full paper. Generalized Hermite reduction is classical. The specialization below supplies the actual joint residue test, endpoint translation and final-denominator interface for this project.

## 1. Exact classification

Let K∈Q(w). The following are equivalent:

    (a) Res_c K=Res_c(e^w K)=0 at every finite pole c;
    (b) K=H″+H′ for some H∈Q(w).                    (1)

The exponential residue at an algebraic pole is understood analytically; its e^c factor is nonzero and the test is algebraic in the principal-part coefficients.

Proof. (b) implies (a), since K=(H′+H)′ and e^wK=(e^wH′)′. For the converse, ordinary zero residues give K=J′ with rational J. Integration by parts in each Laurent series gives Res_c(e^wJ)=−Res_c(e^wJ′)=0. A rational J has a rational solution of H′+H=J exactly when its exponential residues vanish: solve the finite principal part downwards at each pole, where the last compatibility equation is precisely that residue; solve the polynomial part by the finite inverse `1−D+D²−...` of1+D. The local solutions and polynomial solution sum to a global rational H. Then K=J′=H″+H′. All equations and unique principal-part solutions are defined overQ, so H can be chosen inQ(w). Uniqueness is up to a rational solution of H″+H′=0; the only such functions are constants.

This also proves that arbitrary extra algebraic poles with both exactness tests cannot add an independent period in this class.

## 2. Complete target and endpoint effect

Let F be any of the existing matched kernels with R(F)=A(F)=U!=0, rational primitive P, and actual center

    c=−[B(F)+4Im P(a)]/U, a=(1+i)/2.

Take H∈Q(w) with no pole on the vertical path and set F_H=F+H″+H′. The joint exactness theorem retains

    R(F_H)=A(F_H)=U, B(F_H)=B(F),
    P_H=P+H′+H,
    c_H=c−delta/U,
    delta=4Im[H′(a)+H(a)]∈Q.                       (2)

Thus the actual complete signed error is

    e+pi−c_H=(e+pi−c)+delta/U.                     (3)

The exponential integral is unchanged exactly. The companion integral changes by the exact endpoint difference of H′+H. Any extra poles contribute zero ordinary logarithmic and zero exponential residue constants. If H′(a)+H(a) has zero imaginary part, the complete center and reduced denominator are exactly unchanged. If it does not, the mechanism is an explicit rational translation, whose denominator must be retained.

There is no existence gain from allowing extra poles without coefficient/endpoint restrictions: every rational delta is already realized by H=(delta/2)w. Hence arbitrary rational H alone does not supply a new approximation theorem. Its possible value must come from a quantitatively controlled coefficient family and its final evaluated content.

## 3. Exact final denominator after correction

Write the ORIGINAL complete rational numerator B(F)+4ImP(a)=X/Q with X∈Z,Q>0, and delta=A/d in lowest terms. Then

    c_H=−(dX+QA)/(QdU),
    q_H=Qd|U|/gcd(QdU,dX+QA).                     (4)

This equation includes all cancellation between the exponential numerator, primitive endpoint, and added correction. No external clearing multiplier is itself the denominator.

For an integral rational H with poles only0 and1, the negative-power endpoint values are Gaussian integers. Polynomial powers at a can introduce dyadic denominators. For additional rational poles c, values (a−c)^(-j) introduce the Gaussian norm of a−c in the denominator, with its actual power and coefficient content. The exactness of introduced periods does not remove this endpoint denominator.

In particular cancelling an original dyadic numerator obstruction requires delta to have a prescribed dyadic residue modulo the integral numerator lattice. Achieving that congruence does not prove (3) is small in the real norm. This is the remaining joint arithmetic/analytic problem, and it is not supplied by exactness or an arbitrary endpoint rational shift.

## 4. A quantitative dyadic degree gate for integral principal parts

Continue the same controlled-endpoint target with an explicit integral class. Suppose H has integer polynomial coefficients of degree at mostD and integer principal-part coefficients at finitely many real rational poles; poles on the vertical path are excluded. The depths and locations of those real rational poles are otherwise arbitrary.

For EVERY real rational c,

    (a−c)^(-1)∈Z_(2)[i],                          (5)

where Z_(2) denotes rationals with odd denominator. To see this elementarily, write c=u/b in lowest terms, b>0. The inverse is

    2b[(b−2u)−bi]/[(b−2u)²+b²].

If b is odd the denominator has2-valuation1 and both numerator coordinates have valuation at least1. If v2(b)=1, then b−2u is divisible by4 and the denominator has valuation2; both numerator coordinates have valuation at least3. If v2(b)>=2, then v2(b−2u)=1, the denominator has valuation2, and again both numerator coordinates have valuation at least3. This proves (5), including c=1/2 as an algebraic endpoint statement, though that pole is inadmissible on the integration path.

Thus the entire negative-power principal part of H′+H has2-integral Gaussian endpoint coordinates regardless of its pole depth. Its contribution to delta has valuation at least2. For the polynomial part, v2(Im a^j)>=−ceil(j/2), and integer differentiation does not lower this bound. Consequently

    v2(delta)>=2−ceil(D/2).                        (6)

Now suppose the original complete kernel has v2(B(F))=−t, t>=1, and its primitive Pi is2-integral, as do the actual unilateral eligible kernels and EVERY reflected repair kernel (t=v2(N!) for the latter). If

    D<=2t+2,

then (6) gives v2(delta)>=1−t>−t. Hence the correction CANNOT cancel the lowest dyadic layer of B(F), and the ACTUAL denominator remains

    v2(q_H)=t+v2(U).                              (7)

This holds for arbitrary real-rational pole depths in the stated integral principal-part class. Access to that lowest layer first becomes possible at D=2t+3: H=w^(2t+3) has v2(delta)=−t, since its odd highest power has valuation−(t+2) in the imaginary part and the derivative term has strictly higher valuation. This establishes a sharp threshold for valuation access, not a theorem that all dyadic bits cancel or that the real error becomes small.

For the reflected repair t=v2((n+h)!)=n+h−s2(n+h). Thus rational corrections with integral real-pole principal parts and polynomial degree O(n) retain its compulsory h-sized dyadic cost when h/n tends to infinity. Rational principal-part coefficients with their own dyadic denominators or nonreal poles are outside this quantitative class; their endpoint costs require a separate complete numerator analysis. No all-rational correction exclusion is claimed.

## 5. The same degree gate with odd-leading integer denominators

The preceding degree obstruction also holds for another broad integral class, allowing nonreal algebraic poles. Let H=P/Q with P,Q∈Z[w] and the leading coefficient of Q ODD. Divide at infinity, writing H=J+R/Q, degR<degQ=d. The coefficients of J and R have odd denominators, since long division only divides by the odd leading coefficient. Let D=degJ (with no polynomial part interpreted as degree below0).

Put varpi=1−i, so a=1/varpi. The Gaussian integer

    varpi^d Q(a)

is congruent to the odd leading coefficient modulo varpi and is therefore a Gaussian unit at2; its norm is odd. The same argument works when R has odd-denominator coefficients. If m=degR<d,

    R(a)/Q(a)=varpi^(d−m)
                  [varpi^m R(a)]/[varpi^d Q(a)]∈Z_(2)[i].

The derivative of R/Q has denominator Q², also with odd leading coefficient, and is proper. It too has2-integral Gaussian endpoint value. Thus the entire proper rational part of H′+H contributes to delta with valuation at least2, even when Q has nonreal or irrational algebraic roots. The polynomial part J has2-integral coefficients, so the same estimate (6) and exact denominator consequence (7) hold.

In particular arbitrary pole depth in a MONIC integer denominator cannot reach a new negative dyadic endpoint layer. To evade this quantitative gate while keeping D<=2t+2, a new construction must leave both stated integral classes, for example through an even leading denominator with nonintegral local coefficients. That possibility is not excluded, but its actual endpoint numerator and denominator must be analyzed instead of treating pole degree alone as its arithmetic cost.

The current target stops at these structural/quantitative gates: the identities remove uncontrolled constants and expose a necessary degree cost, but no coefficient family with improved COMPLETE primitive rate has been produced. These extensions continue the same controlled-endpoint target; the classical reduction/valuation tools are credited in the initial gate, and no generic Hermite-reduction novelty is claimed.
