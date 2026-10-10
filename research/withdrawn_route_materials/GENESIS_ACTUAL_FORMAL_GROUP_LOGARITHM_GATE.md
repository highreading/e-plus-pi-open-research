> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual two-law formal-group logarithm: public core and arithmetic boundary

Author: Agent 3. Date: 2026-10-02 UTC. Status: candidate DISCARDED at the primary-literature gate. This is a short original preflight, not a proof review, and it does not open a formal-group, algebraization or p-adic route.

## 1. Proposed object and exact bridge

Set L(z)=exp(z)+4 arctan(z)-1 on the germ at zero. Then L(0)=0, L'(0)=5 and L has rational Taylor coefficients. Its normalized logarithm ell=L/5 has linear term z. The operation

    G(x,y)=ell^(-1)(ell(x)+ell(y))=L^(-1)(L(x)+L(y))

is a formal power series in Q[[x,y]], with identity zero, commutativity, associativity and formal inverse ell^(-1)(-ell(x)). These statements follow directly by applying ell to each identity. They hold without a hypothesis about e+pi.

For S=e+pi, ell(1)=(S-1)/5. Thus S=q in Q is exactly the assertion that the actual rational state 1 has rational logarithm (q-1)/5. This is a valid scalar-to-object bridge, but adds no arithmetic closure assertion.

The analytic inverse is unambiguous on the nonnegative real axis: L'(x)=exp(x)+4/(1+x^2)>0 and L maps [0,infinity) onto [0,infinity). This gives an actual associative nonnegative-real semigroup. We do not infer convergence of the origin bivariate formal series at (1,1), nor a global group law on all real numbers. Indeed L(R)=(-1-2pi,infinity), which is not closed under addition.

## 2. Archive and fresh primary gate

Archive query, over sources and work Markdown files:

    formal.?group|formal logarithm|group logarithm|Lazard|Hazewinkel|inverse.generator|inverse.?composition.{0,40}(addition|mean)

Matches include Agent 2's GENESIS_CURVE_EXCHANGE_BRIDGE_COUNTERMODEL.md Sections 1-2 and the analytic GENESIS_ACTUAL_ENDPOINT_SWAP_FIELD.md: both already discard the additive-generator/inverse-composition core. The former credits opened primary inverse-sum mean papers https://arxiv.org/pdf/2203.16862 and https://arxiv.org/pdf/1807.04811. The older sources/item267_generalized_jacobian_frobenius_report.md also mentions a missing formal-group logarithm/p-adic realization; it is not an available bridge.

Fresh online queries:

- Lazard 1955 Sur les groupes de Lie formels à un paramètre logarithme caractéristique zéro pdf
- one dimensional formal group logarithm rational coefficients inverse addition characteristic zero formal group law primary
- formal group law logarithm algebraic point rational logarithm analytic group rational coefficients

Opened primary author paper: Harald Fripertinger and Jens Schwaiger, On 1-dimensional formal group laws in characteristic zero (June 5, 2014), full five-page PDF, https://imsc.uni-graz.at/fripertinger/papers/formal_group_law_jens.pdf. Lemma 4 constructs precisely f^(-1)(f(x)+f(y)); Theorem 5 characterizes characteristic-zero one-dimensional formal group laws by this operation, including uniqueness of the normalized logarithm.

Opened original primary article: Michel Lazard, Sur les groupes de Lie formels à un paramètre, Bulletin de la Société Mathématique de France 83 (1955), 251-274, https://www.numdam.org/item/10.24033/bsmf.1462.pdf. Its introduction explicitly treats analytic group-coordinate Taylor laws, arbitrary coefficient rings and classification of one-parameter formal laws.

This is an exact essential public match, not a conclusion from unsuccessful searching. Under the Genesis protocol the route is discarded immediately. No integrality criterion, p-adic continuation or algebraization theorem is developed.

## 3. Short rational-state countermodel

Take ell_0(z)=z+z^2, a normalized rational polynomial logarithm. It is strictly increasing on [0,infinity), and ell_0(1)=2 is rational. The corresponding local formal group has rational coefficients and all of the same formal axioms. Nevertheless

    1 op_0 1=ell_0^(-1)(4)=(sqrt(17)-1)/2

is irrational. Thus even a rational logarithm at a rational state does not force rational closure under the actual continued operation. This countermodel addresses that generic inference; it does not preserve the actual exp/arctan laws and does not decide S.

## 4. Actual-law translated-germ boundary

For the actual L define the continued translation near zero

    T_1(x)=L^(-1)(L(x)+L(1)).

Then T_1(0)=1 and differentiating the defining identity gives

    T_1'(0)=L'(0)/L'(1)=5/(e+2).

This number is transcendental: algebraicity of it would imply algebraicity of e. This conclusion is unconditional, and would remain true under the hypothetical rationality of S. Consequently a rational logarithm at state 1 would not make this translated analytic germ algebraic or rational in its Taylor coefficients. Rational coefficients of the origin formal law do not imply rational values or rational germs after continuation to a nonzero state.

The endpoint implication supplied by rational S is exactly the rational logarithm value. No further exact arithmetic output or direct endpoint exclusion has been derived. The public formal-group core is not retained as a Genesis candidate; this note records only the precise bridge and two closure failures.
