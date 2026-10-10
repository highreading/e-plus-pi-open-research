> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Conditional dyadic approximation depth and exponential index gaps

Status: Independently reviewed research result (AI review; not formal verification)
Author: main
Reviewer: worker_3
Content SHA256: 29db0d226d2991d949f69ee25fe70b23795e8c56ff01ad7459c5dacae39f7ba8
Review: work/astra_review_registry/reviews/conditional-dyadic-depth-and-index-gaps-worker_3.md

STATUS AND SCOPE
Unverified candidate submitted for independent review. This is a conditional theorem about denominator and error sequences. Its application to the actual b=1 construction requires the separately identified arithmetic and analytic inputs below. It supplies neither an upper bound on actual reduced denominators nor an irrationality proof.

STATEMENT
Write ρ=1+√2 and use natural logarithms. Let I be an unbounded subset of the positive integers. For n∈I, let q_n be a positive integer, E_n a positive real number, and c_n a finite real number. Let ν∈Z_2, with n≠ν for n∈I. Normalize v_p(p)=1. Suppose a constant A>0, independent of n, satisfies, for all sufficiently large n∈I:
(1) v_2(q_n)≥max{0,3n/2−c_n−A log(n+2)};
(2) v_5(q_n)≥n/2−A log(n+2) and v_13(q_n)≥n/6−A log(n+2);
(3) c_n≤v_2(n−ν)+A log(n+2);
(4) log E_n=−2n logρ+r_n, where r_n=o(n).

Define
δ=[(3/2)log2+(1/2)log5+(1/6)log13−2logρ]/log2.
Then 0<δ<1. For every unbounded S⊆I along which q_n E_n→0, and every ε with 0<ε<δ, all sufficiently large n∈S satisfy
v_2(n−ν)≥(δ−ε)n.
If S is enumerated increasingly as n_1<n_2<⋯, then all sufficiently large j satisfy
n_{j+1}−n_j≥2^((δ−ε)n_j).
In particular,
liminf_j log(n_{j+1}−n_j)/n_j≥δ log2.

If hypothesis (4) is strengthened to r_n=O(log(n+2)), there is a constant B>0 such that, eventually along S,
v_2(n−ν)≥δn−B log(n+2),
and, after increasing B if necessary,
n_{j+1}−n_j≥2^(δn_j)/(n_j+2)^B.

PROOF
Distinct prime contributions to a positive integer denominator add. Dropping the maximum in (1) preserves its lower-bound direction, so (1) and (2) give
log q_n≥[(3/2)log2+(1/2)log5+(1/6)log13]n−c_n log2−K log(n+2)
for a constant K. Put t_n=v_2(n−ν). Substituting (3) and (4), and enlarging K, gives
log(q_n E_n)≥δn log2−t_n log2−K log(n+2)+r_n.
Along a shrinking subsequence the left side is eventually negative. Therefore
t_n>δn−[K/log2]log(n+2)+r_n/log2.
Because r_n=o(n), this proves the asserted depth bound with every fixed ε>0.

For two consecutive surviving indices, the nonarchimedean triangle inequality gives
v_2(n_{j+1}−n_j)≥min{t_{n_j},t_{n_{j+1}}}≥(δ−ε)n_j.
Their difference is a nonzero ordinary integer, so its ordinary absolute value is at least 2 raised to its 2-adic valuation. This proves the gap bound and its logarithmic liminf formulation.

Under the stronger remainder hypothesis, the same calculation gives t_n≥δn−K_1 log(n+2). The real function δx−K_1 log(x+2) is increasing for all sufficiently large x. Thus the minimum of the two depth lower bounds is at least δn_j−K_1 log(n_j+2). Exponentiation gives the stated polynomial-loss refinement.

For positivity of δ, observe that ρ²=3+2√2<6<√40=2^(3/2)5^(1/2), and 13^(1/6)>1. For δ<1, the required inequality is √10·13^(1/6)<ρ². Its sixth powers satisfy 13000<ρ^12=19601+13860√2. These are exact inequalities.

LIMIT OF THE CONCLUSION
Deep approximation and large gaps are compatible with a unique simple analytic root. For an explicit abstract example, set N_0=15 and N_{j+1}=N_j+2^(N_j). The 2-adic series
ν*=15+Σ_{j≥0}2^(N_j)
converges and lies in 15+16Z_2. Since N_j=15+Σ_{k<j}2^(N_k), its tail has valuation
v_2(ν*−N_j)=N_j.
The function F(X)=X−ν* is analytic with derivative 1 and has a unique simple root. Nevertheless its values at the unbounded ordinary integers N_j have valuation N_j, and the gaps equal 2^(N_j). Because δ<1, these indices satisfy the necessary depth condition above. This example concerns general analytic simple roots; no identification with the actual b=1 root or denominator sequence is asserted. It does not establish that such approximation occurs for the actual root.

APPLICATION DEPENDENCIES AND EVIDENCE
The existing derivations motivating the hypotheses are recorded in work/astra_20260929/main/note_000062.md and work/astra_20260929/main/note_000063.md. The actual b=1 dyadic denominator normalization and exceptional-root comparison belong to work/session_20260927/hp_b1_odd_dyadic_actual_numerator.md and work/session_20260927/hp_b1_odd_dyadic_germs_independent_review.md. The leading contributions at 5 and 13 belong to work/session_20260927/hp_b1_uniform_five_thirteen_and_even_exclusion.md and work/session_20260927/hp_b1_uniform_5_13_independent_review.md. The analytic error exponent belongs to work/session_20260927/fixed_exponential_degree_error_theorem.md. These paths identify dependencies; this claim does not independently certify those source results. For application, q_n must be the actual positive reduced denominator, E_n the corresponding nonzero approximation error, and I restricted to indices where the endpoint quotient and scalar comparison are valid. Exclusion of other dyadic disks is a separate input.

SELF-AUDIT
The proof uses lower bounds on actual denominator valuations, with every inequality direction displayed. It uses no auxiliary-content estimate, no pending prefactor constant, and no uniformity for growing b. The ultrametric step retains arbitrary valuation depths and uses distinct integer indices. The remaining research gap is an upper bound on approximation depth for the specific root, or another argument ruling out the surviving indices; simple-root factorization and finite congruence certificates do not by themselves provide that bound.