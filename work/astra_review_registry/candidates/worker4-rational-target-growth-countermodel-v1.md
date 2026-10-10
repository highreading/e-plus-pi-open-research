> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational targets are compatible with alternating exponential error and divergent integer forms

Status: UNVERIFIED CANDIDATE
Author: worker_4
Content SHA256: c76bd9a3bb0782ba45ef5b2a5dd2bff28a0f9b092e6dd476f3dbb2984b81fc1e

Verification status: author-audited; independent review pending.

Statement. Let λ=1+√2 and let C>0 be any fixed real constant. There exist reduced rational numbers p_n/q_n, with q_n>0, converging to the rational target 1 such that

1−p_n/q_n = (−1)^n C λ^(−2n)(1+ε_n),
|ε_n| ≤ (14/C)(λ²/15)^n,
q_n ≥ (3√5)^n/(1125 n^4),
|q_n−p_n| → ∞,

and, for Δ_n=p_(n+1)q_n−p_nq_(n+1),

Δ_n = (−1)^n |Δ_n| ≠ 0,
|Δ_n| ∼ 15C(1+λ^(−2))(225/λ²)^n → ∞.

These assertions hold with the same error prefactor C=4π/λ³ used in the matched b=2 asymptotic, if desired. The construction does not assert any matched endpoint or polynomial order conditions.

Construction and proof. For every integer n≥1 define

q_n=15^n,
T_n=Cq_nλ^(−2n),
m_n=1+15 floor(T_n/15),
p_n=q_n+(−1)^(n+1)m_n.

Since T_n>0, m_n is a positive integer. Also m_n≡1 modulo 15, so it is coprime to q_n. The identity p_n≡(−1)^(n+1)m_n modulo q_n therefore gives gcd(p_n,q_n)=1. Thus q_n is the actual positive reduced denominator, rather than an unreduced choice of scale.

Write t_n=T_n−15 floor(T_n/15), so 0≤t_n<15. Then m_n−T_n=1−t_n lies in (−14,1], and hence |m_n−T_n|≤14. Consequently

1−p_n/q_n=(−1)^n m_n/q_n
=(−1)^n Cλ^(−2n)(1+ε_n),

where ε_n=(m_n−T_n)/T_n satisfies the displayed bound. Because λ²=3+2√2<15, ε_n→0 and p_n/q_n→1. Moreover T_n=C(15/λ²)^n→∞, so m_n→∞ and |q_n−p_n|=m_n→∞.

For the denominator bound, 15/(3√5)=√5>1 and 1125 n^4≥1. Therefore 15^n≥(3√5)^n/(1125 n^4) for every n≥1.

Direct subtraction gives

Δ_n=(−1)^n15^n(m_(n+1)+15m_n).

The factor in parentheses is positive, proving the exact sign and nonvanishing assertions. The rounding estimate yields m_n=C(15/λ²)^n+O(1). Substitution gives

|Δ_n|=15C(1+λ^(−2))(225/λ²)^n+O(15^n).

The remainder is negligible because 15/(225/λ²)=λ²/15<1. This proves the asserted asymptotic and divergence.

Scope and dependencies. This is an elementary counterexample to an implication from the displayed abstract approximation estimates to irrationality of the target. It neither satisfies nor challenges the additional defining equations of the actual matched b=2 family, and gives no conclusion about the rationality of e+π. It does not depend on approval of the separate adjacent-determinant candidate or on any analytic transfer theorem. Choosing C=4π/λ³ requires only that this is a fixed positive real number.

Evidence: work/astra_20260929/worker_4/note_000160.md, read completely at bytes 0–1598, file SHA-256 17ca8abafa69991684561be0516048bcc059f5868acd5e688b424987935aba2f. The proof above checks the construction directly; no finite numerical evidence is used. No unresolved mathematical dependency is identified within this scoped statement. Independent review remains required before publication.