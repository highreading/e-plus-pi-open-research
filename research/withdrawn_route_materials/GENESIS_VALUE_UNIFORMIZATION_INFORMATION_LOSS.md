> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Value-uniformization: exact global bridge and information loss

Status: bounded analytic Genesis gate, discarded. This is not an irrationality theorem, not an audit, and not a new approximation family.

## Proposed global operation

Let F(x)=exp(x)+4 arctan(x) on [0,1]. Its derivative is strictly positive, F(0)=1, and F(1)=S=e+pi. Push the measure F'(x)dx forward by F. This is a nonlinear operation on the entire actual profile, and it supplies a proved rationality consequence:

    integral_0^1 F(x)^j F'(x)dx = (S^(j+1)-1)/(j+1), j>=0.

Thus S rational makes every displayed integral rational. More generally, for every rational polynomial P, its antiderivative A can be taken rational, and the integral of P(F)F' is A(S)-A(1). One might hope that the full family of rational nonlinear integrals imposes a new coupling constraint on the two actual laws.

## Exact information-loss lemma

For any strictly increasing C^1 function f:[0,1]->[u,v], the pushforward f_*(f'(x)dx) is Lebesgue measure restricted to [u,v]. Indeed, substitution t=f(x) proves the identity against every continuous test function. Consequently, any subsequent operation that reads only this pushforward measure is completely independent of the interior profile f.

In particular, this construction does not retain the two defining laws of F. If S=r were rational, the same entire pushforward object would be produced by the rational polynomial f_r(x)=1+(r-1)x. This is a countermodel to an obstruction based only on the pushed-forward object; it is not a countermodel preserving the actual exponential and arctangent laws. Keeping those laws as separately labelled information would require a new operation, and no arithmetic closure of the labels follows from the rational pushforward moments.

The normalized increasing map U=(F-1)/(S-1) similarly has U_*(U'dx) equal to uniform probability on [0,1] for every actual value of S. Its normalized power integrals are 1/(j+1) without any rationality hypothesis. This stronger identity shows that normalization alone can erase the scalar obstruction entirely.

## Archive and primary-literature gate

Archive query, run 2026-10-02 UTC: `push.?forward.{0,70}(uniform|moment)|value.{0,30}uniformiz|shuffle.{0,30}(endpoint|integral)|iterated.{0,20}integral.{0,50}rational`, over sources and work Markdown. It found the earlier positive Gamma pushforward in main/SHIFTED_SHORT_FIXED_DIMENSION_TRANSCENDENCE_OBSTRUCTION.md; no exact value-uniformization candidate was located by that bounded query. This is not a novelty assertion. The existing Genesis protocol already excludes a continuation through moment determinants or iterated-integral signatures.

Fresh online queries were `Chen iterated integrals shuffle algebra change of variables primary paper` and `polynomial pullback pushforward uniform measure moments fundamental theorem calculus rational endpoint`.

Opened primary documents:

- Luque--Thibon, *Pfaffian and Hafnian Identities in Shuffle Algebras*, https://arxiv.org/pdf/math/0204026, full 29-page PDF, especially its introduction defining iterated integrals and Chen's product identity. The proposed nonlinear power-integral descendants lie in this already public integral/shuffle machinery.
- Hain, *Iterated Integrals and Algebraic Cycles: Examples and Prospects*, https://arxiv.org/pdf/math/0109204, full 45-page PDF. This is an author survey, used only to delimit the established iterated-integral and period framework; no unseen numerical independence theorem is imported.

Verdict: the exact scalar-to-global implication is valid, but its object forgets the laws needed for a contradiction. Its immediate moment, shuffle, signature or rotation descendants are public essential cores and are discarded. No new tool is retained. A future candidate must use a different operation that demonstrably keeps the law-dependent information instead of restoring it by an unproved faithfulness requirement.
