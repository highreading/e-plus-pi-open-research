> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the two historical index-restriction syntheses

Date: 2026-09-13. Reviewer: audit_computations.

**FULL PASS at their stated scope.** This review covers all sections of
`raw_shrinking_subsequence_index_restrictions.md` and
`raw_neighbor_support_shrinking_index_addendum.md`. The latter supersedes
the former's mandatory divisor, as its introduction explicitly says.
The subsequently proved uniform ternary and full $n-1$ theorems
strengthen the available divisor further; their exact update is kept
separate in `raw_three_neighbor_support_index_update.md`.

No new canonical degree or prime scan was performed. The finitely many
displayed integer and rational certificates were recomputed exactly.
The historical positive-density conclusions remain valid for the
specific lower divisors they name. They are not upper bounds for the
actual reduced denominator, and their density constants must not be
transferred to a larger divisor without a new proof.

## 1. Uniform thresholds and simultaneous divisibility

For even $n\ge8$, an odd prime divisor of $n$ has
$n=mp$, with $m\ge2$ even. For $p\ge5$,
$2mp<p^m$ starts at $m=2$, since $4p<p^2$, and persists
on increasing $m$. At $p=3$, the stated range forces $m\ge4$,
where $6m<3^m$ likewise starts and persists. Since
$v_p(n!)\ge m$, the strict Taylor-loss threshold is uniformly
satisfied, including primes growing with the index.

For even $n\ge16$ and $p\mid n+1$, write $n+1=mp$, where
$m$ is odd. If $m=1$, the factorial exponent is zero, so the
claimed divisor is trivial at this prime; no endpoint-unit inference
is needed. If $m=3$, then $p\ge7$ and
$2n=6p-2<p^2$. If $m\ge5$, then $2mp<p^{m-1}$ follows
from the initial inequality $10p<p^4$ and induction. The lower
bound $v_p(n!)\ge m-1$ proves the strict threshold in both cases.
The two excluded pairs identified in the source are precisely the
small failures relevant to this argument.

The supports of $n$ and $n+1$ are disjoint. Therefore the prime
powers can indeed be multiplied at one actual index, while the exact
dyadic valuation is retained separately. On $n+1=p^\nu$, the old
prime-power-minus-one contribution is exactly
$p^{v_p(n!)}$; the larger divisor must not include it twice. The
threshold-free formula in the newer note is also valid: if its proposed
exponent is positive, the theorem supplies the stronger full factorial
exponent, and otherwise that prime contributes one.

All these deductions use the actual reduction
$q_n=|Z_n|/\gcd(|Z_n|,|N_n|)$, via the previously reviewed numerator
unit theorem. They do not promote a displayed clearing factor to a
primitive denominator without accounting for the gcd.

## 2. Exact weight budgets and excluded families

Legendre's formula gives each displayed identity
$v_p(n!)\log p=n\log p/(p-1)-s_p(n)\log p/(p-1)$.
The digit correction is nonnegative and is bounded by
$\log n+\log p$ for each supported prime. Summing gives the
stated $O((\log n)^2)$ error, because the supported radical divides
$n$ or $n(n+1)$, respectively. This remains valid for
$p=n+1>n$: its weight and one-digit correction cancel exactly.

The optional prime-power term in the earlier note has logarithm
$n\log p/(p-1)-\log(n+1)$, with the two supports correctly kept
disjoint. The exact dyadic correction is zero at $n\equiv0\pmod4$
and one at $n\equiv2\pmod4$. Thus both exact budget identities,
including their constant dyadic term, check.

The relative-error input has a nonzero limiting constant. Shrinking
therefore requires $\log q_n-\alpha n\to-\infty$. A lower divisor
has no larger logarithm, so its exact budget must also tend to minus
infinity. This proves the stated necessary conditions, and then the
eventual $B+O((\log n)^2/n)$ support-weight bounds. No converse is
asserted.

The fixed sets $\{3,5,7,11\}$ and $\{3,5,7,13\}$ have weight
strictly above $B$, by exact certificates. For the second set I
recomputed



$$
A=2^{18}3^65^37^213=15216574464000,
 \qquad A8^{60}>13^{60}.
$$



Since $\phi<13/8$, this proves the required strict rate inequality.
The first set's rational logarithm certificate in
`raw_appell_column_endpoint_independent_review.md` also retains a
strict rational margin. Fixed-prime digit losses are $O(\log n)$,
so both exclusions are uniform.

For $n+1=p^{12k}$, Fermat's congruence supplies each fixed prime
other than the base itself; if the base belongs to the fixed set, the
reviewed prime-power theorem supplies its missing factor. The loss is
$\log(n+1)$, so the error constant is independent of the varying
base and exponent. For the extended family $n=a^{12}-1$, each fixed
prime divides either $a$, giving the minus-one residue, or its
twelfth power minus one. This proves the asserted extension to every
odd integer base, without any factorization assumption.

The historical CRT union is exactly



$$
\frac23\frac25\frac27
 \left(1-\frac9{11}\frac{11}{13}\right)
 =\frac{32}{1365}.
$$



This was also recomputed as an exact rational number. The factors refer
to uniform residue classes among even indices; multiplication by two
is invertible modulo each odd prime. Inclusion–exclusion on the last
two primes is therefore valid.

## 3. Both mean bounds and all positivity certificates

In the earlier mean bound, replacing odd primes by all odd integers
gives the stated upper bound. The comparison



$$
\frac{\log(2j+1)}{2j(2j+1)}
 \le\frac{\log(3j)}{4j^2}
$$



holds termwise. The right side is decreasing for $j\ge1$, and its
integral from one is $(\log3+1)/4$. Adding the retained first term
gives $\mu_0=(5\log3+3)/12$. Markov's inequality then proves the
stated lower density for $S(n)\le1$. Removing three fixed
prime-power families costs only $O(\log X)$ indices. Outside them,
the optional weight is at most $\log11/10<1/4$, giving the claimed
strict exponential gap.

In the newer mean bound, the five retained primes are all odd primes
below seventeen. The remaining terms are bounded by the odd-integer
tail from seventeen onward. Integrating the same decreasing comparison
from seven gives $(\log21+1)/28$, exactly as stated.

I recomputed every proposed rational upper bound for the six logarithms
by evaluating the first thirteen terms of the exponential series with
exact rational arithmetic. In every case the finite sum already exceeds
the relevant integer. Their substitution gives exactly



$$
\frac{91867}{184800}<\frac12.
$$



Thus $\overline\mu<1/2$ has a complete exact certificate. The
exponential-gap positivity certificate also recomputes correctly:



$$
(8/5)^{20}>2^6(11/4)^5,
 \qquad \phi>8/5,\quad e<11/4.
$$



For the two supported residues modulo an odd prime, the count over
$n=2k$, $1\le k\le X$, is bounded by $2X/p+1$. An explicit
check avoids a generic two-class rounding assumption: the classes of
$k$ are zero and $(p-1)/2$, and their total count is



$$
\left\lfloor\frac Xp\right\rfloor+
 \left\lfloor\frac{X+(p+1)/2}{p}\right\rfloor
 \le\frac{2X}p+1.
$$



The resulting rounding error is
$X^{-1}\sum_{p\le2X+1}\log p/(p-1)=o(1)$, as proved by replacing
primes by all integers. Markov's inequality at $5/4$ therefore
gives precisely $1-(8/5)\overline\mu>1/5$, and the digit correction
has the helpful nonnegative sign in the subsequent upper bound on
the mandatory divisor.

These are genuine lower-density statements, not independence assumptions
about divisibility by infinitely many primes. Their parametrized versions
follow by the same nonnegative averaging argument.

## 4. Pairwise normalization and the dominant-prime bonus

For even $m>n$, both reduced numerators are odd and the exact dyadic
denominator exponent strictly increases. Hence the determinant
$p_mq_n-p_nq_m$ is nonzero and has dyadic valuation exactly $a_n$.
Its odd part is divisible by the gcd of any two proved mandatory odd
divisors. This proves the integer lower bound used in the pairwise
inequalities.

The difference of the two approximation errors is



$$
C(-1)^{n/2}e^{-\alpha n}
 \left(1-(-1)^{(m-n)/2}e^{-\alpha(m-n)}\right)(1+o(1)),
$$



uniformly over even $m>n\to\infty$. Uniformity follows by taking
the supremum of the individual relative errors over indices at least
$n$; the displayed main factor stays bounded away from zero because
$m-n\ge2$. Substituting
$q_j=|L_j|e^{\alpha j}/C(1+o(1))$ gives exactly the factor $C$,
exponent $e^{-\alpha m}$, denominator, and common gcd in the
source's pairwise bound. Its logarithmic and fast-shrinkage consequences
have the correct orientations. The adjacent odd-quotient conditions
also agree with their original exact derivation; they concern the
actual neighboring denominators, not an upper bound inferred from a
lower divisor.

For the fixed-m bonus, $n+1=mp^\nu$ with $p>3m$ has
$m<p$, so $\nu$ is the full valuation and the factorial baseline
is exactly
$m(p^\nu-1)/(p-1)-\nu=v_p(n!)$. If two distinct primes met these
hypotheses, each prime would divide the other's cofactor, forcing both
$p>3q$ and $q>3p$, an impossibility. Thus at most one seed bonus
is present at an index. The vanishing seed proves one extra prime
factor, and that prime is at most $n+1$. Adding its logarithm cannot
remove a fixed exponential margin. The proof does not bound the unknown
higher seed depth from above.

## 5. Audit conclusion and historical scope

Both files pass in full for exactly the divisors they define. Their
strict positivity certificates, uniform prime thresholds, union density,
mean tails, pairwise formulas, and dominant-prime argument are correct.
Their scope repeatedly and correctly distinguishes



$$
\text{an upper bound for a proved lower divisor}
 \quad\text{from}\quad
 \text{an upper bound for the actual }q_n.
$$



The newer $n-1$ and uniform ternary theorems permit a larger mandatory
divisor. In extending to $n-1$, one must handle the single prime
$p=n-1$ separately: its factorial exponent is one, but the available
Taylor-loss threshold fails. Omitting that unproved prime power costs
only $\log(n-1)$. The separate update note records this exception,
the controlled deep five-adic class, and a new mean calculation; it does
not reuse either historical density constant without proof.
