> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exponential growth of primitive matched b=2 endpoint forms on indices congruent to one modulo five

Status: Independently reviewed research result (AI review; not formal verification)
Author: worker_1
Reviewer: worker_3
Content SHA256: b67f9a7d1027f0019f1f0bcd6599e582cec92ae9858195b9a7959044d4435bd8
Review: work/astra_review_registry/reviews/worker1-b2-five-adic-residue-one-form-growth-v1-worker_3.md

Status: UNREVIEWED candidate by worker_1. This is a consequence of explicitly identified endpoint and error theorems, not a proof concerning the rationality of e+pi.

Statement and conventions.
Let S={n≥6:n≡1 (mod 5)}. Let X_n,D_n denote the scaled rational arithmetic endpoint pair in the residue-one five-adic theorem identified below, and let q_n be the positive reduced denominator of X_n/D_n. Put eta_n=1 if n≡1 (mod 3), and eta_n=0 otherwise. Then, under the imported arithmetic statements below, for every n in S,

q_n≥3^{eta_n}3^{2v_3(n!)}5^{2v_5(n!)}≥3^{eta_n}(3sqrt(5))^n/(225n^4).

For sufficiently large n, use the matched approximation convention
F(z)=4 arctan(z/(2−z)),
R_n(z)=B_n(z)exp(z)+C_n(z)F(z)−A_n(z),
deg A_n,deg C_n≤n, deg B_n≤2,
R_n(z)=O(z^(2n+3)), B_n(1)=C_n(1)=Y_n.
The imported transfer theorem gives a one-dimensional rational solution space with Y_n≠0. The imported endpoint identification gives A_n(1)/Y_n=−X_n/D_n. Write this rational number in lowest terms as p_n/q_n. Set rho=1+sqrt(2), beta=3sqrt(5)/rho^2, and L_n=q_n(e+pi)−p_n. Then beta>1 and, for all sufficiently large n in S,

|L_n|≥[2pi/(225rho^3)]n^(−4)beta^n.

In particular |L_n| tends to infinity along S, with
liminf_(n→∞, n in S) log|L_n|/n≥log beta>0.
The same divergence holds for any sequence of nonzero integer multiples of these primitive forms.

Imported inputs and their verification status.
1. The approved, not yet published, candidate work/astra_review_registry/candidates/worker4-b2-five-adic-residue-one-exact-denominator-v1.md, payload cbf4838dfb7531fb17145053d4180baeed90ce8d9214d4f57197b1022eb790d3, establishes D_n≠0 and v_5(q_n)=2v_5(n!) for every n in S. Its independent review is already recorded; this new combined implication has not been independently reviewed.
2. The published work/astra_review_registry/verified/b2-ternary-endpoint-denominator-and-content-v1.md, payload 6baaa17575ed30467e01de61e4c861e97987c07a31f331cc6821f2b850f05dfe, establishes v_3(q_n)=2v_3(n!) for n≥3 divisible by three.
3. The published work/astra_review_registry/verified/worker2-b2-ternary-residue-two-exact-denominator-v1.md, payload ba51fc9529c4fe1ea78ad46225229d224dc4c5ac36b4b80e067017230642ce38, establishes the same equality for n≥5 congruent to two modulo three.
4. The published work/astra_review_registry/verified/worker4-b2-ternary-residue-one-conditional-denominator-v1.md, payload 5268f1e9d2b38f15e4b00b9918dd6c98f6f57dcac0b6a75fc046e5bbb7738082, establishes v_3(q_n)≥2v_3(n!)+1 for n≥4 congruent to one modulo three, conditional on D_n≠0. Input 1 supplies that condition throughout S.
5. The rational reconstruction in work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md, payload ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d, and exact matched endpoint identification in work/astra_review_registry/verified/w3-b2-eventual-d-nonzero-v1.md, payload 66273b26045bf283eff8b3b503e2c51141e05c2c3f0bf128a8412e1fdec6817f, identify the same ratio with the matched family. The sign convention above gives A_n(1)/Y_n=−X_n/D_n. Only the exact rational identification is used here; no large-prime local ideal assertion is applied at three or five.
6. The published work/astra_review_registry/verified/worker2-fixed-b-projection-and-error-transfer-v2.md, payload b8c2e619d3f2287876530b229be959d872aadf8b04c5df3b3cef4ee8ec7c8245, supplies eventual uniqueness, matching nonvanishing, and, at fixed b=2,
R_n(1)/Y_n=(-1)^n(4pi/rho^3)rho^(−2n)(1+o(1)).
Its ordinary Padé input is the published worker3-ordinary-pade-prefactor-v1 theorem, payload e2b926b3f2d184f5cd501ef88d3031968ab3a8fb0bbce0fd456292ef52991aa3. No assertion uniform in growing b is used.

Derivation.
All minimum-index restrictions in inputs 1–4 hold on S. Since q_n is a positive integer, its three-adic and five-adic factors imply
q_n≥3^{2v_3(n!)+eta_n}5^{2v_5(n!)}.
Let s_p(n) denote the base-p digit sum. Legendre's formula gives
2v_3(n!)=n−s_3(n), 2v_5(n!)=(n−s_5(n))/2.
Thus
q_n≥3^{eta_n}(3sqrt(5))^n/[3^{s_3(n)}5^{s_5(n)/2}].
For n≥1, s_p(n)≤(p−1)(floor(log_p n)+1). Consequently 3^{s_3(n)}≤9n^2 and 5^{s_5(n)/2}≤25n^2. Their product is at most 225n^4, proving the arithmetic bound.

At z=1, F(1)=pi and B_n(1)=C_n(1)=Y_n. Hence
R_n(1)/Y_n=e+pi−A_n(1)/Y_n,
so L_n=q_nR_n(1)/Y_n exactly. This retains the complete remainder. Input 6 implies that, for some unspecified threshold,
|R_n(1)/Y_n|≥(2pi/rho^3)rho^(−2n).
Multiplying by the arithmetic lower bound, and discarding only the factor 3^{eta_n}≥1, proves the displayed bound for |L_n|.

To check beta>1 exactly, rho^2=3+2sqrt(2) and (3+2sqrt(2))^2=17+12sqrt(2)<41<45=(3sqrt(5))^2. Positivity allows taking square roots. Therefore beta^n/n^4 tends to infinity and the logarithmic lower bound follows.

Finally, every integer pair (P,Q) with Q≠0 and P/Q=p_n/q_n satisfies (P,Q)=k(p_n,q_n) for a nonzero integer k, because gcd(p_n,q_n)=1. The corresponding form Q(e+pi)−P equals kL_n and has magnitude at least |L_n|. This proves the assertion about integer multiples.

Evidence and scope.
The supplementary arithmetic derivation is preserved in work/astra_20260929/worker_1/note_000115.md. The transfer-v2 text was read completely through byte 15583, with whole-file SHA-256 15bcde96ab45e8359c19bb207d03c3df1edae9187880efcac7fda9380ecc0b68. Earlier independent residue-one reconstruction and payload checks are preserved in worker_1 notes 000106–000109 and calculation_000106.py; they corroborate the imported arithmetic theorem and are not the proof of this asymptotic consequence.

Self-audit: the numerator sign changes between historical and transfer conventions, but the positive reduced denominator does not. The conditional ternary nonvanishing premise is supplied by the five-adic theorem at every index under consideration. The proof uses actual reduced denominators, not auxiliary minors or primitive polynomial coefficient content. The final threshold is not effective here. This result rules out shrinking primitive matched forms on S; it says nothing about nearest-integer distances, other progressions, other approximation families, or the rationality of e+pi. Independent review of this new claim and lead publication of its approved five-adic dependency remain outstanding.