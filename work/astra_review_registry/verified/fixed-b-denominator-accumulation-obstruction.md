> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Discrete normalized-denominator limits under a fixed asymptotic error

Status: Independently reviewed research result (AI review; not formal verification)
Author: worker_2
Reviewer: main
Content SHA256: 8856456ac04468cc66d2df3437479c78af462b09f4ec42934a54b4bd30c239d3
Review: work/astra_review_registry/reviews/fixed-b-denominator-accumulation-obstruction-main.md

Author: worker_2. Status: unverified candidate submitted for independent review.

Statement and hypotheses.
Let ρ=1+√2 and fix an integer b≥1. Put C_b=4π/ρ^(b+1). Let α be a real number and r_n=p_n/q_n rational numbers in lowest terms, with q_n>0, defined for all sufficiently large positive integers n. Assume the exact asymptotic hypothesis

α−r_n = (−1)^n C_b ρ^(−2n)(1+η_n), where η_n→0.

Define x_n=q_n/ρ^(2n). If α=a/d is rational, with integers a,d, d>0 and gcd(a,d)=1, then every finite accumulation point L of x_n belongs to

{ kρ^(b+1)/(4πd) : k=1,2,3,... }.

In particular, zero cannot be an accumulation point, and every finite accumulation point is transcendental. Consequently, the existence of any finite algebraic accumulation point of x_n proves that α is irrational, provided the stated error hypothesis holds.

Proof.
Assume α=a/d. The numbers m_n=a q_n−d p_n are integers and satisfy the exact identity

m_n=d q_n(α−r_n).

For sufficiently large n, 1+η_n>0. The asymptotic hypothesis therefore makes m_n nonzero with sign (−1)^n. Thus

k_n=(−1)^n m_n=d C_b x_n(1+η_n)

is a positive integer for every sufficiently large n.

Let n_j tend to infinity along a subsequence for which x_(n_j)→L<∞. Since x_n>0, L≥0. The preceding identity gives

k_(n_j)→d C_b L.

A convergent sequence of positive integers is eventually constant. Hence there is an integer k≥1 such that k_(n_j)=k eventually, and d C_b L=k. This proves the displayed description of finite accumulation points and excludes L=0.

For any k≥1, the number A=kρ^(b+1)/(4d) is nonzero and algebraic. The quotient A/π is transcendental: if it were algebraic, then its nonzero reciprocal multiplied by A would make π algebraic, contrary to the classical transcendence of π. Thus every permitted finite accumulation point is transcendental. The irrationality criterion follows by contraposition.

A further conditional consequence is

liminf_(n→∞) q_n/ρ^(2n) ≥ ρ^(b+1)/(4πd)

under rationality α=a/d. Indeed, k_n≥1 implies x_n≥1/[d C_b(1+η_n)] for all sufficiently large n. This is a necessary consequence of rationality and the assumed error, not an independently established estimate for the research denominator sequence.

Dependencies and evidence.
The proof above is self-contained apart from the classical theorem that π is transcendental. The asymptotic formula is an explicit hypothesis, not a conclusion certified by this claim. The motivating audited formula is recorded in work/astra_20260929/worker_2/note_000009.md; the precursor arithmetic observation is in work/astra_20260929/worker_2/note_000011.md. Relevant analytic sources are work/astra_20260929/worker_3/note_000003.md, work/session_20260913/unequal_degree_hp_attempt.md, and work/session_20260927/fixed_exponential_degree_error_theorem.md. Application requires identifying the target α and the rational approximants with their correct sign and normalization, then establishing precisely the displayed error hypothesis.

Scope and self-audit.
The integer argument handles subsequences containing either or both parities because k_n includes the alternating sign. Eventual nonvanishing follows from the assumed asymptotic itself. The parameter b is fixed throughout; no uniformity for growing b is asserted. Each x_n is algebraic, but a limit of algebraic numbers need not be algebraic, so termwise algebraicity supplies none of the missing accumulation-point hypothesis. No existence, boundedness, or algebraicity of an accumulation point is established here. No upper bound on the actual reduced denominator and no conclusion about the rationality of e+π follows without additional results.