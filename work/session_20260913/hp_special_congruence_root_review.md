> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root review of the special HP index congruences

2026-09-13. Reviewed Sections3–5 of
`hp_b1_special_gcd_and_denominator.md` independently of its finite checks.
The odd-prime-power congruence theorem is valid.

The expansion of h_n=H_n(1) has summands

    (-1)^b 2^(-c) (n)_(b+2c) binomial(n,b+c) binomial(b+c,c).

The derivative value u_n=H'_n(1) replaces the falling-factorial index by
b+2c+1. Both formulas follow by extracting the term of total degree
b+2c from the n-th power and the remaining term from the exponential.
Each series is finite at an integer n.

For r>=s, the function (n)_r binomial(n,s) preserves congruences modulo
every p^a. To check this, split its difference into the difference of
the falling factorial, which is an integer polynomial, and the
difference of the binomial coefficient. Vandermonde and
k binomial(v,k)=v binomial(v-1,k-1) bound the latter's valuation below
by a-floor(log_p s) when p^a divides the index difference. Meanwhile
(n)_r is divisible by r!, whose valuation is at least floor(log_p s).
The two terms therefore each have valuation at least a. Zero falling
factorials and s=0 cause no exceptions.

This elementary lemma itself works at p=2 as well. The restriction to
odd p is required when multiplying by the factor2^(-c) in the actual
H and u sums. The displayed h_1,h_3 counterexample correctly prevents
extending the final sequence theorem to2.

For two indices, taking the union of their finite nonzero summand sets
is legitimate: terms outside it vanish at both indices. Thus the
argument does not exchange an unproved p-adic infinite limit with a
sum. Multiplication by n preserves the congruence, giving it also for
j_n=n h_n+u_n.

It follows that a common root modulo p^(a+1) projects to a common root
modulo p^a. This compatibility does not assert that every lower root
has a lift. The exact h_1=j_2=0 gives the claimed obligatory divisor
oddpart(n-1) of gcd(h_n,j_(n+1)). It is not an upper bound.

The finite truncation r<ap at precision p^a follows from the factor r!
in each summand; no cancellation can invalidate this valuation lower
bound. Finally, for the earlier endpoint-gcd gate p>2n+2, reducing n
modulo p leaves n unchanged. The note is correct that this congruence
alone cannot settle that gate or bound the final reduced denominator.
