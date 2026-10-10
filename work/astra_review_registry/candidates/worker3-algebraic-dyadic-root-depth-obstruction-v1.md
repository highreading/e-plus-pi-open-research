> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Elementary obstruction to linear dyadic approximation depth at algebraic roots

Status: UNVERIFIED CANDIDATE
Author: worker_3
Content SHA256: 3efb8a94a32696dc881df697f9d4aa6995eb2935c5fc12341db35ef6f7d2cf1d

UNVERIFIED CANDIDATE FOR INDEPENDENT REVIEW.

Statement. Normalize v₂(2)=1 and v₂(0)=+∞. Let α∈Z₂ be algebraic over Q. Choose any nonzero polynomial P(X)=Σ_{k=0}^d a_k X^k∈Z[X] satisfying P(α)=0, and put A=Σ_{k=0}^d |a_k|. Necessarily d≥1 and A≥1. For every positive integer n with P(n)≠0,

v₂(n−α) ≤ d log₂ n + log₂ A.

Proof. The identity

P(n)−P(α)=(n−α) Σ_{k=1}^d a_k Σ_{j=0}^{k−1} n^{k−1−j} α^j

holds in Q₂. The second factor belongs to Z₂, so P(n)≠0 implies v₂(P(n))≥v₂(n−α). For every nonzero ordinary integer m, divisibility by 2^{v₂(m)} gives 2^{v₂(m)}≤|m|. Applying this to m=P(n), and using n≥1, yields

2^{v₂(n−α)}≤2^{v₂(P(n))}≤|P(n)|≤A n^d.

Taking base-two logarithms proves the assertion.

Consequence 1. Fix η>0 and K≥0. There are only finitely many positive integers n satisfying

v₂(n−α)≥ηn−K log₂(n+2).

Indeed, outside the finite integer zero set of P, the asserted inequalities would require ηn≤d log₂ n+K log₂(n+2)+log₂ A, which fails for all sufficiently large n. Integer zeros of P contribute at most d exceptions, including any possible n=α.

Consequence 2. Let α₁,…,α_s∈Z₂ be a fixed finite collection. If an unbounded sequence of positive integers n satisfies

max_i v₂(n−α_i)≥ηn−K log₂(n+2),

then at least one α_i is transcendental over Q. If every α_i were algebraic, Consequence 1 would make the union of the corresponding exceptional integer sets finite. More specifically, any fixed root supplying this depth for infinitely many indices must be transcendental.

Scope and dependencies. This is an unconditional elementary lemma about algebraic elements of Z₂. It uses only polynomial factorization, valuation integrality, and an ordinary absolute-value bound for an integer polynomial. It does not depend on the finite dyadic coefficient certificate, analytic tail estimates, ordinary Padé asymptotics, or the conditional denominator theorem. Application to the research family requires a separately justified implication from shrinking primitive forms to linear dyadic approximation depth. No algebraicity or transcendence assertion about the actual germ roots is proved here; transcendental roots need not satisfy such approximation bounds. Therefore this claim does not exclude every sparse subsequence and is not an irrationality proof for e+π.

Evidence and relationship to prior work. The full derivation is contained above and requires no numerical evidence or external sources. It strengthens the rational-root observation recorded in work/astra_20260929/worker_3/note_000016.md. The separately audited application is work/astra_review_registry/candidates/conditional-dyadic-depth-and-index-gaps.md, registry content SHA-256 29db0d226d2991d949f69ee25fe70b23795e8c56ff01ad7459c5dacae39f7ba8; that application's hypotheses are not certified by this lemma. Independent approval is pending.