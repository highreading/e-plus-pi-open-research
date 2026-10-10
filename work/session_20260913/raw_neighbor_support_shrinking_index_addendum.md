> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Combined n(n+1) denominator support and remaining shrinking-index candidates

Date: 2026-09-13. Original synthesis by audit_sources.

**Dependency status: all inputs reviewed.** The new theorem in
raw_appell_neighbor_content_and_denominator.md has passed the full
independent audit raw_appell_neighbor_content_independent_review.md by
audit_computations. The deductions here do not reprove its integral
Jucys--Murphy argument. The earlier dyadic, Appell-at-$n$,
prime-power-minus-one, and relative-error inputs are also reviewed.
This synthesis has also passed independent review, recorded in
raw_index_restriction_syntheses_independent_review.md. Its density
claims concern its displayed historical divisor only.

This is a distinct extension of
raw_shrinking_subsequence_index_restrictions.md. The new mandatory
divisor combines all odd primes dividing $n(n+1)$ at the same index.
It supersedes that note's smaller index-only divisor; its prior
positive-density conclusion should not be applied to this larger
divisor without the new argument in Section 4 below.

Retain


$$
\alpha=5\log\phi,\quad \phi=(1+\sqrt5)/2,\quad
 \beta=\tfrac32\log2,\quad B=\alpha-\beta,
$$




$$
a_n=v_2(q_n)=\tfrac32n+\epsilon_n^{(2)},\quad
 \epsilon_n^{(2)}\in\{0,1\}\quad(n\ {\rm even}),
$$


and $L_n=q_n(e+\pi)-p_n$. The reviewed relative error implies


$$
|L_n|=Cq_ne^{-\alpha n}(1+o(1)),\qquad C>0.
$$



## 1. A uniform threshold with the prime n+1 handled explicitly

The new input states that for every $p\mid n+1$, the actual
exponential endpoint numerator is a $p$-unit, while


$$
n!\mid\operatorname{cont}\widehat Q_n,\qquad
 v_p(\widehat P_a(1))\ge v_p(n!)-\lfloor\log_p(2n)\rfloor.
$$


Consequently, when the right side is positive, the actual reduced
denominator obeys $v_p(q_n)\ge v_p(n!)$. The analogous implication
at odd $p\mid n$ is already proved.

These statements imply the following uniform result:


$$
\boxed{n\ge16\ {\rm even},\quad p\mid n(n+1),\ p\ {\rm odd}
 \quad\Longrightarrow\quad v_p(q_n)\ge v_p(n!).}       \tag{1}
$$


For $p\mid n$, the previous addendum proved the threshold at every
even $n\ge8$. For $p\mid n+1$, write $n+1=mp$, where $m$
is odd. If $m=1$, then $p=n+1>n$ and $v_p(n!)=0$; (1) is
trivial and needs no numerator-unit inference.

Suppose $m\ge3$. Then $v_p(n!)\ge m-1$. If $m=3$, the
restriction $n\ge16$ forces $p\ge7$; hence
$2n=6p-2<p^2=p^{m-1}$. If $m\ge5$, for every $p\ge3$,


$$
2mp<p^{m-1}.
$$


It holds at $m=5$, since $10p<p^4$, and persists on increasing
$m$, since multiplication by $p$ outgrows multiplication by
$(m+1)/m$. Therefore


$$
v_p(n!)\ge m-1>\lfloor\log_p(2n)\rfloor.
$$


This proves (1) uniformly even when $p$ grows with $n$. The two
small failures of this simple threshold test are $n=8,p=3$ and
$n=14,p=5$; no assertion about the latter's actual reduction is
needed. The former is covered separately by the already proved
prime-power-minus-one formula.

Define the explicit integer


$$
\boxed{
 \Lambda_+(n)=2^{a_n}
 \prod_{\substack{p\mid n(n+1)\\p\ {\rm odd}}}p^{v_p(n!)}.
 }                                                   \tag{2}
$$


Since the supports of $n$ and $n+1$ are disjoint,


$$
\boxed{\Lambda_+(n)\mid q_n\qquad(n\ge16\ {\rm even}).} \tag{3}
$$


On $n+1=p^\nu$, the known exact additional factor was already
$p^{v_p(n!)}$; it must not be multiplied in a second time.

There is also a threshold-free version at every positive even index:


$$
2^{a_n}
 \prod_{\substack{p\mid n(n+1)\\p\ {\rm odd}}}
 p^{\max\{0,v_p(n!)-\lfloor\log_p(2n)\rfloor\}}
 \mid q_n.                                           \tag{4}
$$


If the maximum is positive the theorem gives the stronger full
factorial exponent; otherwise its contribution is one. Equation (4)
is useful for a global formula, but (3) is stronger in the large-index
range relevant to shrinkage.

## 2. The exact simultaneous weight budget

Let


$$
S_+(n)=\sum_{\substack{p\mid n(n+1)\\p\ {\rm odd}}}
               \frac{\log p}{p-1},\qquad
 D_+(n)=\sum_{\substack{p\mid n(n+1)\\p\ {\rm odd}}}
               \frac{s_p(n)\log p}{p-1}.
$$


Legendre's formula applies even if $p=n+1$: in that case its
two terms cancel exactly, giving $v_p(n!)=0$.
Thus


$$
\log\Lambda_+(n)-\alpha n
 =n\{S_+(n)-B\}-D_+(n)+\epsilon_n^{(2)}\log2.          \tag{5}
$$


Uniformly,


$$
0\le D_+(n)
 \le\omega_{\rm odd}(n(n+1))\log n+
           \log\operatorname{rad}_{\rm odd}(n(n+1))
 =O((\log n)^2).                                     \tag{6}
$$


Indeed the first inequality uses the number of base-$p$ digits,
including the one-digit case $p>n$; both prime-product terms are
bounded using $\operatorname{rad}_{\rm odd}(n(n+1))\le n(n+1)$.

Every hypothetically shrinking even subsequence must therefore satisfy


$$
\boxed{
 n\{S_+(n)-B\}-D_+(n)+\epsilon_n^{(2)}\log2
       \longrightarrow-\infty.}                     \tag{7}
$$


In particular


$$
\limsup S_+(n)\le B,\qquad
 S_+(n)\le B+O((\log n)^2/n)\quad\hbox{eventually}.     \tag{8}
$$


These conditions combine primes at one actual index. They do not
replace full prime-power valuations by radicals in the denominator:
the radical only identifies the support in (2), while its exponents
are the full $v_p(n!)$.

## 3. Stronger explicit exclusions and polynomial families

For any fixed odd squarefree integer $d$ with


$$
\sum_{p\mid d}\frac{\log p}{p-1}>B,                  \tag{9}
$$


every sufficiently large even index satisfying $d\mid n(n+1)$
has exponentially growing primitive form. Each prime can independently
divide either neighbor, and the loss from the fixed factorial digit
sums is only $O_d(\log n)$.

The choices


$$
d_1=3\cdot5\cdot7\cdot11,\qquad
 d_2=3\cdot5\cdot7\cdot13
$$


both satisfy (9), by the previously reviewed exact constant
comparisons. For each $d_i$, the Chinese remainder theorem gives
exactly sixteen even residue classes modulo $2d_i$, obtained by
choosing zero or minus one at its four odd primes.

Their union has relative density, among even indices,


$$
\frac{2}{3}\frac{2}{5}\frac{2}{7}
 \left[1-\left(1-\frac2{11}\right)
          \left(1-\frac2{13}\right)\right]
 =\boxed{\frac{32}{1365}}.                           \tag{10}
$$


This finite union already supplies explicit exponential divergence
on more than two percent of even indices. It is only an illustrative
subset of all exclusions supplied by the full budget (7).

There is also an unconditional-in-the-base polynomial family:


$$
\boxed{n=a^{12}-1,\qquad a\ge3\ {\rm odd\ integer}.}   \tag{11}
$$


For every $r\in\{3,5,7,13\}$, either $r\mid a$, giving
$n\equiv-1\pmod r$, or Fermat's congruence gives
$a^{12}\equiv1\pmod r$, giving $n\equiv0\pmod r$.
Thus $d_2\mid n(n+1)$, whether or not $a$ is prime or a
prime power. Uniformly on (11),


$$
\log q_n-\alpha n\ge c_*n-O(\log n),\qquad
 c_*=\sum_{r\mid d_2}\frac{\log r}{r-1}-B
       \approx0.123391405949>0.                     \tag{12}
$$


The exact positivity certificate is


$$
(2^{18}3^65^37^213)\,8^{60}>13^{60},
 \qquad \phi<13/8.
$$


Equation (11) strictly extends the earlier prime-base families
$n=p^{12k}-1$; no factorization hypothesis on $a$ survives.

## 4. An improved mean bound: positive-density candidates remain

Crude doubling of the previous loose bound for the mean of $S(n)$
is inconclusive. A short sharper bound suffices.
Put


$$
\mu_*=\sum_{p\ {\rm odd}}\frac{\log p}{p(p-1)}.
$$


Retain the primes $3,5,7,11,13$ explicitly. Every other odd prime
is an odd integer at least seventeen; the composite integers nine
and fifteen do not contribute. With $j\ge8$,


$$
\frac{\log(2j+1)}{2j(2j+1)}
 \le\frac{\log(3j)}{4j^2}.
$$


The right-hand function is decreasing for $j\ge1$, so its tail
sum is at most its integral from seven. Therefore


$$
\mu_*\le \overline\mu:=
 \frac{\log3}{6}+\frac{\log5}{20}+\frac{\log7}{42}
 +\frac{\log11}{110}+\frac{\log13}{156}
 +\frac{\log21+1}{28}<\frac12.                       \tag{13}
$$


This bound uses no prime-distribution theorem or prime scan.
For an exact elementary check of the strict half, use


$$
\log3<11/10,\ \log5<13/8,\ \log7<2,\quad
 \log11<12/5,\ \log13<13/5,\ \log21<31/10.
$$


Each follows by comparing its integer argument with
$\sum_{j=0}^{12}r^j/j!<e^r$ at the displayed rational $r$.
Substitution in (13) gives
$\overline\mu<91867/184800<1/2$.
The expression in (13) is approximately $0.492593398672$.

Among $n=2,4,\ldots,2X$, the condition $p\mid n(n+1)$
occupies two disjoint classes modulo $p$. Its count is at most
$2X/p+1$. Consequently


$$
\frac1X\sum_{k=1}^X S_+(2k)
 \le2\mu_*+
 \frac1X\sum_{\substack{p\le2X+1\\p\ {\rm odd}}}
                  \frac{\log p}{p-1}
 \le2\overline\mu+o(1).                              \tag{14}
$$


The error tends to zero without any theorem about primes: replace
the prime sum by all integers and bound it by $O((\log X)^2)$.

Markov's inequality now proves that the set of even indices with
$S_+(n)\le5/4$ has lower relative density at least


$$
\boxed{1-\frac85\overline\mu
       \approx0.211850562125>\frac15.}               \tag{15}
$$


On that entire set, $D_+(n)\ge0$ and
$\epsilon_n^{(2)}\le1$, so the larger mandatory divisor obeys


$$
\boxed{\log\Lambda_+(n)\le(\alpha-\eta)n+\log2,\qquad
 \eta=B-\frac54\approx0.116338354458>0.}              \tag{16}
$$


The exact positivity of $\eta$ was certified in the preceding
synthesis by $\phi>8/5$, $e<11/4$, and
$(8/5)^{20}>2^6(11/4)^5$.

Thus even the stronger all-$p\mid n(n+1)$ divisor leaves a set
of positive lower density, exceeding one fifth of even indices,
on which that divisor falls below the shrinking threshold by a fixed
exponential margin. This does not upper-bound $q_n$, assert
shrinkage there, or exclude additional arithmetic factors.
It identifies precisely why these two supported residue classes
alone do not close the denominator route.

More generally, for every $2\overline\mu<c<B$, indices with
$S_+(n)\le c$ have lower relative density at least
$1-2\overline\mu/c$, and a fixed mandatory-divisor gap $B-c$.
The explicit choice $c=5/4$ keeps both constants simple and strict.

## 5. What changes in the pairwise constraints

The preceding synthesis's gcd-normalized two-index inequalities remain
valid with the larger mandatory odd part


$$
M_+(n)=\prod_{\substack{p\mid n(n+1)\\p\ {\rm odd}}}p^{v_p(n!)}
$$


and $G^+_{n,m}=\gcd(M_+(n),M_+(m))$.
For two selected shrinking indices, $s_j=-\log|L_j|$, one has


$$
s_n+s_m\le\alpha m-a_n\log2-\log G^+_{n,m}+O(1).
$$


This now includes, for example, primes dividing $n+1$ and $m$,
not just primes dividing both degrees. Its proof requires no new
spacing theorem. It still cannot exclude the set in (15) without
additional information about actual denominator factors or actual
neighboring odd gcds: a lower bound for a neighboring denominator
is not an upper bound for the relevant quotient.

## 6. The reviewed fixed-m seed bonuses do not remove this margin

The newer theorem raw_fixed_m_prime_ray_minus_one_denominator.md,
reviewed in raw_fixed_m_minus_one_root_review.md, says that if
$n+1=mp^\nu$, $m$ is odd, and $p>3m$, then


$$
v_p(q_n)=\frac{m(p^\nu-1)}{p-1}-\nu+\kappa_p,\qquad
 \kappa_p\ge0.
$$


The displayed factorial term is exactly $v_p(n!)$: the base-$p$
digits of $mp^\nu-1$ are those of $m-1$, followed by $\nu$
digits $p-1$, and $m<p$. Thus its baseline agrees with (2).
Its seed criterion gives the additional certified factor $p$
when $Q_{m-1}(1)\equiv0\pmod p$.

There is at most one such dominant prime at a given index. If distinct
$p,q$ both met their hypotheses, their respective cofactors would
contain $q$ and $p$; hence $p>3q$ and $q>3p$, a contradiction.
Define $J_{\rm seed}(n)$ to be that additional prime when the
criterion vanishes, and one otherwise. Then the stronger certified
divisor is


$$
J_{\rm seed}(n)\Lambda_+(n)\mid q_n,\qquad
 1\le J_{\rm seed}(n)\le n+1.
$$


It changes the upper estimate for the known mandatory divisor in
(16) by at most $\log(n+1)$, so the fixed exponential gap and
positive-density obstruction remain. This statement retains the
one extra power actually proved by a vanishing first seed; it does
not assume an upper bound for the unknown higher depth $\kappa_p$,
which could contain further arithmetic information.
