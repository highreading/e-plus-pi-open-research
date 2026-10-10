> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Reduced-denominator valuations of the three-term matched filter on two progressions

Status: UNVERIFIED CANDIDATE
Author: worker_4
Content SHA256: 41527527f21a77d80f491516b9a2ca7f0386a152bd1afac6cfdc2ebbec48cbd0

UNVERIFIED author submission for independent review.

This claim gives an elementary denominator lemma and its application to the complete matched b=2 endpoint ratios. It concerns the filter with weights (1,6,1)/8. It establishes no irrationality statement and assumes no sharper asymptotic expansion for the filtered error.

Let n≥11 satisfy n≡2 or 11 modulo 15. Let rho_j=A_j/q_j, for j=n,n+1,n+2, be rational numbers written in lowest terms, with q_j>0. Define

rho_tilde_n=(rho_n+6rho_{n+1}+rho_{n+2})/8,
Q_n=den(rho_tilde_n),
a=v_3(n!), b=v_5(n!), t=v_3(n+1).

Here den denotes the positive reduced denominator, and v_p(0)=+infinity. The following are the explicit hypotheses of the abstract lemma:

(3) v_3(q_n)=2a, v_3(q_{n+1})=2(a+t), and v_3(q_{n+2})≥2(a+t)+1.

(5a) If n≡11 modulo 15, then v_5(q_n)=v_5(q_{n+1})=2b and v_5(q_{n+2})≥2b+1.

(5b) If n≡2 modulo 15, then v_5(q_n)=2b, v_5(q_{n+1})≥2b+1, and v_5(q_{n+2})≤2b−1.

Under these hypotheses, rho_tilde_n is nonzero and

v_3(Q_n)=v_3(q_{n+2})≥2v_3(n!)+3.

Moreover,

v_5(Q_n)=v_5(q_{n+2}) if n≡11 modulo 15,
v_5(Q_n)=v_5(q_{n+1}) if n≡2 modulo 15.

In either case v_5(Q_n)≥2v_5(n!)+1. Consequently

Q_n≥135·3^(2v_3(n!))·5^(2v_5(n!))
   ≥3(3sqrt(5))^n/(5n^4).

Proof of the abstract lemma.

For a reduced rational A/q, if v_p(q)>0 then v_p(A/q)=−v_p(q). Always v_p(A/q)≥−v_p(q), including A=0. If one summand has strictly smaller p-adic valuation than every other summand, their sum has that same valuation. Indeed, division by the summand of least valuation leaves a unit plus elements of pZ_p.

Both allowed progressions satisfy n≡2 modulo three, so t≥1 and n+2 is a ternary unit. Under (3), the three numerator summands have valuations

v_3(rho_n)=−2a,
v_3(6rho_{n+1})=1−2(a+t),
v_3(rho_{n+2})=−v_3(q_{n+2})≤−2(a+t)−1.

All denominator exponents used for these equalities are positive. The third valuation is strictly smaller than the first two. Division by eight does not change a ternary valuation. Hence rho_tilde_n has valuation −v_3(q_{n+2}), proving its nonvanishing and the exact ternary denominator identity. Since t≥1, its lower bound is 2a+3.

Suppose first n≡11 modulo 15. Neither n+1 nor n+2 is divisible by five. Under (5a), the valuations of rho_n, 6rho_{n+1}, rho_{n+2} are respectively

−2b, −2b, −v_5(q_{n+2})≤−2b−1.

The third term uniquely has least valuation. Both six and eight are five-adic units, so v_5(Q_n)=v_5(q_{n+2}).

Suppose instead n≡2 modulo 15. Again neither added factorial factor is divisible by five. Under (5b),

v_5(rho_n)=−2b,
v_5(6rho_{n+1})=−v_5(q_{n+1})≤−2b−1,
v_5(rho_{n+2})≥−v_5(q_{n+2})≥1−2b.

The middle term uniquely has least valuation. The last inequality remains valid if rho_{n+2}=0 or its denominator is a five-adic unit; no equality between rational valuation and negative denominator valuation is assumed in that case. This proves v_5(Q_n)=v_5(q_{n+1}).

Since Q_n is an integer, the two prime-power lower bounds multiply to give the factor 3^3·5=135. Legendre's formula, with s_p(n) the base-p digit sum, gives

3^(2v_3(n!))5^(2v_5(n!))=(3sqrt(5))^n/[3^(s_3(n))5^(s_5(n)/2)].

The elementary bounds s_p(n)≤(p−1)(floor(log_p n)+1) give 3^(s_3(n))≤9n^2 and 5^(s_5(n)/2)≤25n^2. Their product proves the displayed coarse exponential lower bound. No sharpness is asserted.

Application to the matched b=2 ratios.

For this application define rho_j=−X_j/D_j using the complete rational endpoint contractions of the published b2-two-chart-actual-denominator-identities record. Thus X_j includes both partial-exponential contractions, both moment contributions, and the correction term −2f_j H_{j+1}(1)W_j, with f_j=2^j/(j!)^2. Its common nonzero raw endpoint scale cancels before taking rho_j. The q_j used here are the positive reduced denominators of these rational numbers, not polynomial coefficient contents or auxiliary maximal minors. Records using X_j/D_j have exactly the same q_j.

Assume D_n,D_{n+1},D_{n+2} are nonzero. The published local statements imply all the abstract hypotheses:

At three, the successive index residues are 2,0,1. The residue-two and residue-zero theorems give the first two equalities in (3). The residue-one theorem gives v_3(q_{n+2})≥2v_3((n+2)!)+1. Since n+2 is not divisible by three, v_3((n+2)!)=a+t, as required.

If n≡11 modulo 15, the successive residues modulo five are 1,2,3. The residue-one and residue-two theorems give the equalities in (5a); the residue-three theorem gives its strict lower bound. All three factorials have five-adic valuation b.

If n≡2 modulo 15, the successive residues modulo five are 2,3,4. The residue-two theorem gives v_5(q_n)=2b, and the residue-three theorem gives v_5(q_{n+1})≥2b+1. The published residue-four cancellation theorem gives v_5(q_{n+2})≤2v_5((n+2)!)−1=2b−1. Its allowance for a zero numerator causes no difficulty in the proof above. The stronger residue-four congruence modulo 25 is not a dependency.

All arithmetic thresholds are satisfied for the stated n≥11 and residue classes: the smallest such n is 11, and the smallest n≡2 modulo 15 in this range is 17. The cited eventual-nonvanishing theorem supplies all three conditions D_j≠0 for every sufficiently large n. Therefore the filter conclusions hold eventually on both progressions. The threshold n≥11 is arithmetic only; this claim gives no effective analytic or nonvanishing threshold.

Published dependencies, all under work/astra_review_registry/verified/:

b2-two-chart-actual-denominator-identities.md — definition and exact identification of the complete endpoint ratio.
b2-ternary-endpoint-denominator-and-content-v1.md — exact ternary denominator valuation on residue zero.
worker2-b2-ternary-residue-two-exact-denominator-v1.md — exact ternary denominator valuation on residue two.
worker4-b2-ternary-residue-one-conditional-denominator-v1.md — ternary strict lower bound on residue one when D is nonzero.
worker4-b2-five-adic-residue-one-exact-denominator-v1.md — exact five-adic valuation on residue one.
worker4-b2-five-adic-residue-two-exact-denominator-v1.md — exact five-adic valuation on residue two.
w3-b2-five-residue-three-loss-v1.md — strict five-adic lower bound on residue three when D is nonzero.
main-b2-five-adic-residue-four-cancellation-v1.md — five-adic denominator upper bound on residue four from index nine onward.
w3-b2-eventual-d-nonzero-v1.md — eventual nonvanishing for the same endpoint denominator and index.

The preliminary observation is preserved in work/astra_20260929/worker_4/note_000181.md. The subsequent bounded source comparison checked the residue-one ternary, residue-three five-adic, and residue-four five-adic statements directly; the other local dependencies retain their completed reading and assessment. No new endpoint computation was required for this valuation argument, and no fresh independent review of all imported proofs is claimed.

Self-audit and unresolved scope.

The factor six contributes one ternary valuation and no five-adic valuation; division by eight changes neither valuation studied here. Each exact conclusion follows from a unique least valuation, so cancellation among tied leading terms is not being assumed absent. Possible zero numerators in the residue-four input are explicitly allowed. The conclusions concern only this fixed filter and these two progressions. The published leading error asymptotic cancels under this filter and, by itself, supplies no nonzero lower asymptotic for its remaining error. Accordingly the denominator bound alone does not prove divergence of Q_n(e+pi−rho_tilde_n), exclude all filtered shrinking forms, or decide whether e+pi is rational. Independent review of this new claim remains required.