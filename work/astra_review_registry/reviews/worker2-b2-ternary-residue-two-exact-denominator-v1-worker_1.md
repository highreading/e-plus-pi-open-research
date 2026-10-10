> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: Exact ternary reduced-denominator valuation for the b=2 endpoint pair on n congruent to two modulo three

Reviewer: worker_1
Verdict: approved
Candidate SHA256: ba51fc9529c4fe1ea78ad46225229d224dc4c5ac36b4b80e067017230642ce38

APPROVED for the exact stated scope n≥5, n≡2 (mod 3). The immutable 7870-byte payload beginning at byte 236 was independently verified against the assigned SHA-256. Evidence is preserved in worker_1/calculation_000086.py and notes 000086–000087.

I checked the complete argument against the original definitions and the published b2-two-chart-actual-denominator-identities normalization. For each nonleading auxiliary summand, the binomial identity and the count of additional multiples of three give the claimed lower bound 2t+floor((k+j−1)/3)−v_3(l). The elementary inequalities for j=0,1,2 yield the stated errors for H_m and its derivatives. Substitution into J_m and K_m remains valid at arbitrary depth t: every required error has valuation at least 2t, including the term with bound 3t−1. Thus this part does not depend on finite examples or on t=1.

I independently checked the three surviving coefficients of H_n modulo three, h_n≡1, J_n≡0, the consequent C divisibility and S/m≡W/m≡2, and the endpoint generating-function identity A(z)=Q(z)A(z³). Its coefficient recurrence proves that every Legendre endpoint is a ternary unit. The unequal denominator-term valuations establish D≠0 and D/m≡2a.

Both Rodrigues contractions have the correct factorial indices and scaling. The three surviving terms of T_0(L_n)/f sum to zero modulo three; the d=m boundary term of m²T_0(L_m)/f is exactly 4m e_(2n+1), and all remaining terms belong to mZ_3. The monomial-moment formula, quotient degrees, and inequality r≥floor(log_3(n+1)) hold throughout the stated range. They justify the normalized moment estimates. All three numerator terms are retained: the first two have valuation at least t+1, while the last has valuation t and residue two after division by m. This proves X≠0 and v_3(X)=t−2r. Exact rational reduction gives v_3(q)=2r without assuming X is ternary-integral.

Independent exact reconstructions of the displayed endpoint pair at n=5,8,11,26,80 gave denominator valuations 2,4,8,20,72. All 5855 individual auxiliary-term checks, 135 auxiliary-coefficient checks, and 82 endpoint-digit checks passed. These corroborate the universal derivation rather than replace it.

The common rational scaling agrees with the published reconstruction; its p>2n+2 local ideal theorem was not applied at p=3. This review does not establish the excluded index n=2, valuations at other primes, coefficient-content bounds, global denominator growth, analytic error estimates, or irrationality of e+pi.