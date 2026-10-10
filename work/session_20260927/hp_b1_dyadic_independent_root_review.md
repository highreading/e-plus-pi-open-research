> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent root review: actual dyadic numerator and the six-class exclusion

Date:2026-09-27. FULL PASS.
Source:hp_b1_dyadic_numerator_and_six_class_exclusion.md.

I checked the actual endpoint normalization against the passed adjacent
scalar formula and the ternary note. The same rational numerator is used
throughout; no coefficient denominator is substituted for reduced q.

The divided-power parity argument is correct: paired terms in a square
vanish modulo2 and every nonconstant middle coefficient has an even
central binomial multiplier. For even n this makes H_n odd and all
nonconstant g_s(n) even. In A-H, odd s additionally have even binom(n,s),
while even s have D_even-1 divisible4. Thus A-H vanishes modulo4.

For k=n+1 odd, the weights are locally integral at2. The s=2 identity
w_2=(k-1)^2 g_2(k) is exact. The s=0, s=2 and even s>=4 cases exhaust
B-K modulo4; the odd s terms vanish. This proves B-K=2 modulo4 and
C=K A-H B=2 modulo4, hence exact valuation1.

I independently derived the Legendre endpoint sum as the constant term
of(2+z+2/z)^k. It is the same sum as equation(13) and proves both the
general ceil(k/2) lower bound and its one-power improvement for k>=2.
The second-kind convolution then has the claimed valuation bound.
For even n, its contribution is at least3 while the factorial C term
has valuation at most2, so no cancellation between these terms is
possible. This proves the exact all-even numerator valuation without
an asymptotic threshold or an omitted small-index case.

Both terms of Delta_n have valuation at least n/2+2. Subtracting the
exact numerator valuation gives v2(q_n)>=2v2(n!)-n/2 whenever Delta
is nonzero. On n=2 modulo6 the independent ternary theorem guarantees
that nonzero endpoint and exact ternary depth2v3(n!). These divisors
belong to the SAME reduced q, so their simultaneous use is justified.

The same family's proved evaluated-error exponent is
-2log(1+sqrt(2)). The resulting positive gap is exactly
log(6sqrt(2)/(1+sqrt(2))^2)=log(18sqrt(2)-24).
The strict inequality18sqrt(2)>25 follows from648>625. This verifies
the sign of the claimed exponential divergence, not just a decimal.

The accepted scope is the stated n=2 modulo6 subsequence. The proof
does not establish a denominator theorem on other residue classes,
exclude all degree-one approximants, or imply irrationality of e+pi.
No new canonical degree calculation was needed for this review.
