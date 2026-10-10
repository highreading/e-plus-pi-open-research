> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent finite certificate for positive-residue seeds

Date: 2026-09-13. Reviewer: audit_sources.

**Finite arithmetic PASS.** The seed atlas
small_residue_exact_seeds.json and its construction
check_small_residue_exact_seeds.py have been checked by the distinct
exact construction check_small_residue_seeds_independent.py.
The complete independent output is
small_residue_seeds_independent_certificate.json.

Only degrees $k=0,\ldots,6$, primes $p\in\{3,5,7,11,13\}$,
and pairs with $2k<p$ were used. No large-degree approximant,
prime sweep, or factorization was performed. The large factorization
fields in the original atlas are not needed or validated by this
certificate.

**Theorem dependency: FULL PASS.** The general transfer in
raw_positive_residue_schur_and_endpoint_transfer.md has passed its
separate audit raw_positive_residue_transfer_independent_review.md.
The finite residues and their all-index positive-class consequences
below therefore have no outstanding dependency on that proof.

## 1. Distinct construction and original normalization

The original atlas uses rational Toeplitz determinants and their
cofactors. The independent checker uses:

1. An integer Appell Wronskian for $M_D^{[k]}(1)$, divided by
   its explicit integer Vandermonde.
2. The integer matrix of the first $k$ derivatives at one of
   $(1+\partial_t^2)^k[t^{k+j}]$, $0\le j\le k$.
   Its signed maximal cofactors give a kernel vector, divided by
   their integer gcd to produce primitive $b$.
3. $U_j=(k+j)!b_j$, $S=(1+t^2)^kU$, and the original coefficient
   relation $w_{k+r}=S_{k+r}/r!$. Dividing $W/t^k$ by
   $(t-1)^k$ reconstructs $V$, with integrality and zero remainder
   checked exactly.
4. The original reversed divided derivative
   

$$
\widehat Q_j=\binom{3k-j}{k}S_{3k-j}
   \quad(0\le j\le2k),
$$


   followed by multiplication by the exponential Taylor series
   through degree $2k$. This obtains the actual integral
   $\widehat P_e$ coefficient vector and its value at one.

Every determinant uses integer Bareiss elimination with divisibility
assertions. The only rational arithmetic uses exact fractions.
No inverse modulo a prime with nonunit determinant is taken. The
kernel matrix has rank $k$ over $\mathbb Q$, certified by a
nonzero maximal cofactor, so its primitive vector agrees up to sign
with the original actual one. Its orientation is selected by agreement
of the sign of $V(1)$ with the independently computed $M_D(1)$,
as in the original atlas.

All seven complete vectors and values $M_D,b,V,V(1),P_e(1)$
agree exactly with the atlas. At degree one this atlas uses
$V_1=t-2$ and $P_{e,1}(1)=5$, the simultaneous negative of the
earlier $V_1=2-t,\ P_{e,1}(1)=-5$ convention. Unit conclusions
and the ratio $P_e(1)/V(1)=-5$ are unchanged.

## 2. Exact modular certificate

Each entry below is $(M_D^{[k]}(1),\widehat P_{e,k}(1))\bmod p$.
A dash denotes $2k\ge p$, outside the requested theorem range.

| $k$ | $p=3$ | $p=5$ | $p=7$ | $p=11$ | $p=13$ |
|---:|:---:|:---:|:---:|:---:|:---:|
| 0 | (1,1) | (1,1) | (1,1) | (1,1) | (1,1) |
| 1 | (2,2) | (4,0) | (6,5) | (10,5) | (12,5) |
| 2 | — | (0,1) | (1,2) | (1,3) | (2,12) |
| 3 | — | — | (5,3) | (6,4) | (1,0) |
| 4 | — | — | — | (7,4) | (2,11) |
| 5 | — | — | — | (6,0) | (6,7) |
| 6 | — | — | — | — | (0,9) |

In particular both $p=7,k=2,3$ satisfy the unit criterion.
At eleven the sole failure in the allowed positive range is $k=5$,
through the numerator. At thirteen the failures are $k=3$, through
the numerator, and $k=6$, through the determinant.
These are failures of the stated sufficient seed test; no contrary
actual denominator theorem is inferred.

## 3. Finite good residue sets and simultaneous denominators

Combining these positive seeds with the already reviewed classes
$0,-1$, and with $+1$ when $p\ne5$, gives


$$
\begin{array}{c|l}
 p&G_p\\ \hline
 3&\{0,1,2\}\\
 5&\{0,4\}\\
 7&\{0,1,2,3,6\}\\
 11&\{0,1,2,3,4,10\}\\
 13&\{0,1,2,4,5,12\}.
 \end{array}                                          \tag{1}
$$


No negative-residue theorem beyond the independently reviewed
$-1$ class is used here. In particular this table does not yet
claim a uniform seven-adic theorem.

For these five fixed primes, $n\ge26$ implies


$$
v_p(n!)>\lfloor\log_p(2n)\rfloor.
 \tag{2}
$$


To check this uniformly, put $m=\lfloor n/p\rfloor$.
For $p\ge7$, $m\ge2$, and
$2n<2p(m+1)<p^m$, initially because $6<p$ and then by
induction in $m$. For five, $m\ge5$, and for three $m\ge8$;
the same inequality holds already at $m=3$ for five and
$m=4$ for three. Thus $v_p(n!)\ge m$ proves (2).

Accordingly the reviewed positive transfer and the already reviewed
classes yield the single-index divisor


$$
2^{a_n}\prod_{\substack{p\in\{3,5,7,11,13\}\\n\bmod p\in G_p}}
 p^{v_p(n!)}\mid q_n
 \qquad(n\ge26\ {\rm even}).                          \tag{3}
$$


The full-modulus $n-1$ theorem separately proves
$v_5(P_e(1))=1$ when $25\mid n-1$. For $n\ge26$, its
arctangent gap is greater than one, so (3) can be strengthened by
the additional factor


$$
5^{v_5(n!)-1}\quad\hbox{when }n\equiv1\pmod{25}.
 \tag{4}
$$


This residue is disjoint from $G_5$, and there is no double counting.
For the stated gap, $m=\lfloor n/5\rfloor\ge5$ gives
$2n<10(m+1)<5^{m-1}$, hence
$v_5(n!)-\lfloor\log_5(2n)\rfloor\ge2$.
The finite criterion (3)--(4) can be combined with any other reviewed
mandatory divisor by taking their least common multiple, not by
multiplying repeated prime powers.

## 4. A concrete same-index exclusion from these finite classes

Let $H_5$ consist of $n\bmod5\in\{0,4\}$ together with
$n\equiv1\pmod{25}$. It occupies eleven classes modulo twenty-five.
Three is now always available. Every one of the three weights


$$
\frac{\log5}{4}+\frac{\log7}{6}+\frac{\log11}{10},\quad
 \frac{\log5}{4}+\frac{\log7}{6}+\frac{\log13}{12},\quad
 \frac{\log5}{4}+\frac{\log11}{10}+\frac{\log13}{12}
$$


is strictly larger than


$$
5\log\phi-\tfrac32\log2-\tfrac12\log3.
 \tag{5}
$$


The smallest is the last. Its strict positivity can be certified
by raising to the common denominator sixty and comparing


$$
2^{90}3^{30}5^{15}11^6 13^5>\phi^{300}.
 \tag{6}
$$


For example $\phi<809017/500000$ and the corresponding integer
cross-multiplication verify (6); the rational upper bound itself
follows from $r^2-r-1>0,\ r>1$.

Thus, whenever $n\in H_5$ and at least two of the three conditions


$$
n\bmod7\in G_7,\qquad n\bmod11\in G_{11},\qquad
 n\bmod13\in G_{13}
 \tag{7}
$$


hold, (3)--(4) make the actual primitive forms grow exponentially.
The lost single power of five in (4) is a constant logarithmic loss
and does not affect the strict exponential margin.

By the Chinese remainder theorem, the relative density among even
indices of this explicitly excluded finite union is


$$
\frac{11}{25}
 \left[
  \frac57\frac6{11}+\frac57\frac6{13}
       +\frac6{11}\frac6{13}
       -2\frac57\frac6{11}\frac6{13}
 \right]
 =\boxed{\frac{612}{2275}}.
 \tag{8}
$$


This is a simultaneous residue-class result, not a sum of bounds
proved on incompatible index subsequences.

## 5. Scope of older density statements

The positive-density candidate sets in the earlier two synthesis
notes concern exactly their displayed historical mandatory divisors.
The new finite residue factors can enlarge those divisors at indices
outside $n(n+1)$ or the three-neighbor support. Their old numerical
coverage bounds must not be reused for the larger divisor without
another calculation.

This finite certificate does not claim that (1) is the complete set
of good residues, or that seed failures force bad actual valuations.
The complementary negative-residue theorem is a separate pending
input and is not included in (1)--(8). Any later full-modulus lifting
of exceptional positive seeds also requires its own proof.
