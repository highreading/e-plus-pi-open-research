> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact digit-sum minima and a conditional two-prime denominator bound

Status: UNVERIFIED CANDIDATE
Author: worker_1
Content SHA256: 067ec2594e6d23d28cc4342397f71d62fed7517b3e4e86fa3d71191af3addc0a

Status: author-checked supplementary result submitted for independent review. This claim is separate from w3-b2-residue-one-digit-refinement-v1 and does not amend that approved payload.

1. Exact digit minimum and suffix bound.

For an integer base b≥2, write s_b(m) for the digit sum of a nonnegative integer m. Given S≥0, write S=(b−1)k+r with 0≤r<b−1. The least nonnegative integer having digit sum S is

M_b(S)=(r+1)b^k−1.

Consequently

b^{s_b(m)/(b−1)}≤m+1,

with equality exactly when m=b^k−1 for some integer k≥0. More generally, if t≥1 and m=b^t j+a with j≥0 and 0≤a<b^t, then

b^{s_b(m)/(b−1)}≤b^{s_b(a)/(b−1)}(j+1),

with equality exactly when j=b^k−1.

Proof. A digit configuration minimizing the represented integer cannot have a positive higher digit and an unsaturated lower digit: transferring one unit from the higher position to the lower preserves the digit sum and decreases the integer. Therefore its lower k digits are b−1 and its remaining leading digit is r, proving the formula for M_b(S). Weighted arithmetic–geometric mean, with weight θ=r/(b−1), gives r+1=(1−θ)·1+θ·b≥b^θ. Hence m+1≥(r+1)b^k≥b^{S/(b−1)}. Equality in the second inequality requires r=0; equality throughout also requires m=M_b(S). This gives the stated equality classification, including m=0. The suffix formula follows from s_b(b^t j+a)=s_b(j)+s_b(a), applying the established inequality to j. Primality of b is unnecessary.

2. Conditional bound for positive integer denominators.

Let n≥6 satisfy n≡1 modulo 5. Suppose q is a positive integer satisfying

v_3(q)≥2v_3(n!),   v_5(q)≥2v_5(n!).

Then

q>5√5(3√5)^n/[(n+1)^2(n+4)^2].

Proof. The two valuation hypotheses imply q≥3^{2v_3(n!)}5^{2v_5(n!)}. Legendre’s formula gives

3^{2v_3(n!)}5^{2v_5(n!)}=(3√5)^n/[3^{s_3(n)}5^{s_5(n)/2}].

Part 1 gives 3^{s_3(n)}≤(n+1)^2. Writing n=5j+1, it also gives

5^{s_5(n)/2}≤√5(j+1)^2=(n+4)^2/(5√5).

These imply the displayed bound with a weak inequality. Equality in both digit estimates would require n=3^u−1=5^v−4, with u,v≥1. The first expression is 2 modulo 3; the second is 0 or 1 modulo 3. This is impossible, proving strictness. No optimality of the combined constant is asserted.

3. Conditional approximation consequence.

Suppose p_n/q_n is a reduced rational approximant, q_n>0, satisfying the valuation hypotheses above along the stated progression. If, along that progression,

|α−p_n/q_n|=Cρ^(−2n)(1+o(1)),   C>0, ρ>1,

then for all sufficiently large such n,

|q_nα−p_n|≥(5√5 C/2)(3√5/ρ²)^n/[(n+1)^2(n+4)^2].

This follows by taking the asymptotic factor at least 1/2 and multiplying by the denominator bound. Divergence follows if 3√5>ρ². The eventual analytic threshold is unspecified and separate from the arithmetic restriction n≥6.

Scope and dependencies. Parts 1–2 use only elementary digit arithmetic and Legendre’s factorial-valuation formula. Part 3 assumes its error asymptotic. Application to the project requires verifying the hypotheses for the actual positive reduced denominator of the same approximant; coefficient primitivity alone does not provide them. This claim neither establishes new endpoint valuations nor decides the rationality of e+pi.

Evidence: work/astra_20260929/worker_1/note_000188.md contains the supplementary derivation; work/astra_20260929/worker_1/calculation_000188.py contains exact integer checks. Its successful execution, recorded in note_000189.md, reports 40,970 digit checks, 238 exact-minimum checks, 2,145 structured equality checks, and 202 conditional denominator checks. The source and assertions were subsequently inspected. These finite checks corroborate the proof and do not replace it. The general suffix extension and simultaneous-equality exclusion follow from the arguments above; they are not claimed as separately executed computations. Independent review remains outstanding.