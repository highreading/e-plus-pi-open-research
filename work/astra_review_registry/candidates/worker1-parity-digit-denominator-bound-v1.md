> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Parity refinement of a conditional two-prime denominator lower bound

Status: UNVERIFIED CANDIDATE
Author: worker_1
Content SHA256: 9677b1b1c9a80f4d833dd2ebdd9a2612ae352036e7625ac1fdb87821d3537150

Status: author-checked conditional arithmetic claim; independent review required.

Statement. Let n≥6 be an integer with n≡1 modulo 5. Suppose q is a positive integer satisfying v_3(q)≥2v_3(n!) and v_5(q)≥2v_5(n!). Set T=(n+1)^2(n+4)^2. Then
q>C_n(3√5)^n/T,
where C_n=20√5/3 when n is odd and C_n=16 when n is even. Consequently the uniform constant 20√5/3 is valid throughout this progression. No optimality assertion is made.

Proof. Write s_p(x) for the base-p digit sum of a nonnegative integer x. If s_p(x)=(p−1)k+r with 0≤r<p−1, then x+1≥(r+1)p^k, with equality exactly when x=(r+1)p^k−1. To prove this, minimize an integer with the prescribed digit sum. If a higher digit is positive and a lower digit is less than p−1, transferring one digit unit downward decreases the integer while preserving its digit sum. The minimizing expansion therefore has k trailing digits p−1 and leading digit r.

Put m=(n−1)/5. Then s_5(n)=s_5(m)+1 and m+1=(n+4)/5. Define F=3^{s_3(n)}5^{s_5(n)/2}.

First, the digit-minimum lemma gives, for every x≥0,
3^{s_3(x)}≤(x+1)^2,
with equality exactly at x=3^k−1. Indeed the residual digit is either 0 or 1, and the corresponding ratios are 1 and 3/4. Likewise
5^{s_5(x)/2}≤(x+1)^2,
with equality exactly at x=5^l−1: for residual digit r=0,1,2,3, the respective ratios are 1, √5/4, 5/9, and 5√5/16, of which only the first equals 1.

If n is odd, s_3(n) is odd. Writing s_3(n)=2k+1 yields
3^{s_3(n)}≤3(n+1)^2/4,
with equality exactly at n=2·3^k−1. Applying the general base-five bound to m therefore gives
F≤(3√5/100)T=3T/(20√5).
Equality would require both n=2·3^k−1 and m=5^l−1. Since n≥6, k≥1. These identities imply n+4=2·3^k+3=5^{l+1}, impossible modulo three. Thus F<3T/(20√5).

If n is even, m is odd. Hence s_5(m) is odd, so its residual digit modulo four is 1 or 3. The digit-minimum lemma gives
5^{s_5(m)/2}/(m+1)^2≤max(√5/4,5√5/16)=5√5/16,
with equality exactly at m=4·5^l−1. Combining this with the general ternary bound gives F≤T/16. Equality would require n=3^k−1 and m=4·5^l−1, with k≥1. Then n+4=3^k+3=4·5^{l+1}, again impossible modulo three. Thus F<T/16.

The valuation hypotheses and coprimality of 3 and 5 imply q≥3^{2v_3(n!)}5^{2v_5(n!)}. Legendre’s formula identifies this forced factor as
3^{n−s_3(n)}5^{(n−s_5(n))/2}=(3√5)^n/F.
Substitution of the two strict upper bounds for F proves the claim. Finally 16>20√5/3, since 2304>2000.

Evidence. The derivation is saved in work/astra_20260929/worker_1/note_000202.md. The reproducible integer-only checks are in work/astra_20260929/worker_1/calculation_000202.py, SHA-256 c42166ddae7ddce7498f709461b5e8ca6efa7504b248a7c2f33c9c2d8812e06b. The execution result recorded in note_000203.md reports 2,308 digit-bound checks, including 319 structured indices, and 201 forced-denominator checks passing. These finite computations corroborate the proof and are not substitutes for it.

Dependencies and scope. The proof is self-contained apart from elementary positional notation and Legendre’s factorial-valuation formula. It does not depend on approval of the earlier digit-minima candidate. For application to endpoint approximants, q must be identified with their actual positive reduced denominator and both valuation hypotheses must be supplied separately. This claim proves no new endpoint identity, analytic error estimate, or effective analytic threshold. It establishes no conclusion about the rationality of e+pi.