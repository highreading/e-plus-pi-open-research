> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Simultaneous index restrictions on a hypothetically shrinking even subsequence

Date: 2026-09-13. Original synthesis and elementary consequences by
audit_sources. Independent review: **FULL PASS**, recorded in
raw_index_restriction_syntheses_independent_review.md.

The inputs concern the same canonical reduced rational $p_n/q_n$:
the exact dyadic theorem, the reviewed Appell coefficient/endpoint-unit
theorem, the reviewed odd-prime-power-minus-one theorem, and the reviewed
signed relative-error asymptotic. No unknown cofactor factor is retained
as a denominator divisor. No prime scan or new canonical solve is used.

The main new consequences are a simultaneous divisor valid at every
even $n\ge8$, an exact necessary index-weight budget, exclusion of
every sufficiently large $n=p^{12k}-1$, and a positive-density
obstruction to covering all possible subsequences using those
index-only lower valuations. The last statement is explicitly about
the proven mandatory divisor, not an upper bound for the actual $q_n$.

## 1. Inputs and a uniform form of the Appell divisor

Let


$$
\alpha=5\log\phi,\quad \phi=(1+\sqrt5)/2,\quad
 \beta=\tfrac32\log2,\quad B=\alpha-\beta.
$$


For even $n$, put


$$
a_n=v_2(q_n)=n+2\left\lfloor\frac{n+2}{4}\right\rfloor
 =\frac32n+\epsilon_n^{(2)},\quad
 \epsilon_n^{(2)}=
 \begin{cases}0&n\equiv0\pmod4,\\1&n\equiv2\pmod4.\end{cases}
$$


Use a different symbol for the approximation error:


$$
E_n=e+\pi-p_n/q_n
 =C(-1)^{n/2}e^{-\alpha n}(1+o(1)),\qquad C>0.
$$


Thus the primitive form $L_n=q_n(e+\pi)-p_n$ shrinks on a subsequence
if and only if $q_ne^{-\alpha n}\to0$ there.

The Appell theorem proves


$$
p\mid n,\quad v_p(n!)>\lfloor\log_p(2n)\rfloor
 \quad\Longrightarrow\quad v_p(q_n)\ge v_p(n!)
$$


for odd primes $p$. Its threshold can be removed uniformly in the
present even range:


$$
\boxed{n\ge8\text{ even},\ p\mid n\text{ odd}
 \quad\Longrightarrow\quad v_p(q_n)\ge v_p(n!).}       \tag{1}
$$


Indeed write $n=mp$, where $m$ is even and at least two. For
$p\ge5$, $2mp<p^m$ at $m=2$, because $4p<p^2$, and the
inequality persists as $m$ increases. For $p=3$, $n\ge8$
forces $m\ge4$; $6m<3^m$ holds at four and persists thereafter.
In either case $v_p(n!)\ge m>\lfloor\log_p(2n)\rfloor$.
This argument is uniform in primes growing with $n$.

If $n+1=p^\nu$ is an odd prime power, the second reviewed theorem is


$$
v_p(q_n)=\frac{n}{p-1}-\nu.                           \tag{2}
$$


Its extra-arctangent-power proof is wholly all-index. Such $p$
does not divide $n$, and it is unique if it exists.

Define


$$
M(n)=\prod_{\substack{p\mid n\\p\ {\rm odd}}}p^{v_p(n!)},
\quad
 J(n)=
 \begin{cases}
 p^{\,n/(p-1)-\nu},&n+1=p^\nu,\ p\text{ odd prime},\\
 1,&\text{otherwise}.
 \end{cases}
$$


Then all forced prime powers can be combined at one index:


$$
\boxed{\Lambda(n):=2^{a_n}M(n)J(n)\mid q_n
 \qquad(n\ge8\text{ even}).}                          \tag{3}
$$


The coprimality of the three displayed supports is essential.
Equation (3) does not combine different prime-power-minus-one
families at the same $n$.

## 2. Exact necessary budget and its uniform logarithmic version

Put


$$
\Phi(n)=\sum_{\substack{p\mid n\\p\ {\rm odd}}}v_p(n!)\log p,
\qquad
 S(n)=\sum_{\substack{p\mid n\\p\ {\rm odd}}}\frac{\log p}{p-1}.
$$


Let $w(n)=\log p/(p-1)$ and $b(n)=\nu\log p=\log(n+1)$ when
$n+1=p^\nu$, and set both to zero otherwise. Legendre's formula gives


$$
\Phi(n)=nS(n)-D(n),\qquad
 D(n)=\sum_{\substack{p\mid n\\p\ {\rm odd}}}
       \frac{s_p(n)\log p}{p-1}\ge0.                  \tag{4}
$$


Here $s_p(n)$ is the sum of the base-$p$ digits of $n$.
The following elementary bound is uniform:


$$
D(n)\le\omega_{\rm odd}(n)\log n+\log\operatorname{rad}_{\rm odd}(n)
 \le\frac{(\log n)^2}{\log3}+\log n.                 \tag{5}
$$


For the first inequality use
$s_p(n)/(p-1)\le\lfloor\log_p n\rfloor+1$; for the second
use $3^{\omega_{\rm odd}(n)}\le n$.

The exact logarithm of the mandatory divisor relative to the shrinking
scale is


$$
\log\Lambda(n)-\alpha n
 =n\{S(n)+w(n)-B\}-D(n)-b(n)
       +\epsilon_n^{(2)}\log2.                       \tag{6}
$$


If $L_n\to0$ along even indices tending to infinity, (3) and the
relative-error theorem force


$$
\boxed{
 n\{S(n)+w(n)-B\}-D(n)-b(n)
       +\epsilon_n^{(2)}\log2\longrightarrow-\infty.} \tag{7}
$$


This is stronger than merely a nonpositive limiting exponential rate.
In particular


$$
\limsup\{S(n)+w(n)\}\le B
       =5\log\phi-\tfrac32\log2
       \approx1.366338354458.                        \tag{8}
$$


More precisely (5)--(7) give the necessary eventual upper bound


$$
S(n)+w(n)\le B+O((\log n)^2/n),                       \tag{9}
$$


and retain the divergent deficit required in (7).

For every fixed odd squarefree $d$ satisfying


$$
\sum_{p\mid d}\frac{\log p}{p-1}>B,                  \tag{10}
$$


a shrinking subsequence contains only finitely many multiples of $2d$.
Indeed on those multiples the fixed primes alone make
$\log q_n-\alpha n\ge c_dn-O_d(\log n)$ for some $c_d>0$.
Thus their primitive forms grow exponentially. This is an elementary
divisibility sieve with all prime-power multiplicities already accounted
for. It is a necessary restriction, not a theorem that the remaining
residue classes supply small denominators.

## 3. A uniform excluded family: every twelfth prime-power exponent

Let $\mathcal P=\{3,5,7,13\}$, and put


$$
c_*=\frac{\log3}{2}+\frac{\log5}{4}
       +\frac{\log7}{6}+\frac{\log13}{12}-B>0.         \tag{11}
$$


This strict comparison has an elementary exact certificate. Multiplying
by twelve, it is equivalent to


$$
A:=2^{18}3^6 5^3 7^2 13>\phi^{60}.
$$


One has $\phi<13/8$, and the integer comparison
$A\,8^{60}>13^{60}$ proves the inequality. Here
$A=15216574464000$; numerically $c_*\approx0.123391405949$.
Only the exact comparison is used.

For every odd prime $p$, if $n+1=p^{12k}$, Fermat's elementary
congruence shows that every $r\in\mathcal P\setminus\{p\}$
divides $n$, since $r-1\mid12$. If $p\notin\mathcal P$,
all four primes divide $n$. If $p\in\mathcal P$, equation (2)
supplies the missing prime's factorial-depth contribution.
The fixed-prime factorial errors are $O(\log n)$; the loss for
the replaced prime is $12k\log p=\log(n+1)$. Consequently,
uniformly over all these indices,


$$
\boxed{\log q_n-\alpha n\ge c_*n-O(\log n),
 \qquad n+1=p^{12k},\ p\text{ odd prime},\ k\ge1.}     \tag{12}
$$


The constant in the error is independent of $p,k$: only primes
in the fixed set $\mathcal P$ need be used.
Thus every hypothetically shrinking even subsequence eventually
avoids every index of this form, and the actual primitive forms
grow exponentially on the entire displayed family.

For a fixed prime $p$, other forbidden exponent divisibilities can
be read from multiplicative orders: if a finite set
$\mathcal R$ of odd primes distinct from $p$ satisfies


$$
\frac{\log p}{p-1}+\sum_{r\in\mathcal R}\frac{\log r}{r-1}>B,
$$


then sufficiently large exponents divisible by every
$\operatorname{ord}_r(p)$ are excluded. Equation (12) supplies
a single uniform choice and requires no table of orders.

## 4. Why the present index-only lower bounds cannot cover a subsequence

There is a positive-density set of even indices on which the entire
mandatory divisor (3) stays below the shrinking threshold by a fixed
exponential factor.

For positive integers $X$, averaging over $n=2,4,\ldots,2X$ gives


$$
\frac1X\sum_{k=1}^X S(2k)
 \le\sum_{p\ {\rm odd}}\frac{\log p}{p(p-1)}
 \le\sum_{j=1}^{\infty}
       \frac{\log(2j+1)}{2j(2j+1)}
 \le \mu_0:=\frac{5\log3+3}{12}<1.                  \tag{13}
$$


The first bound uses $\lfloor X/p\rfloor/X\le1/p$.
For the last bound retain the $j=1$ term $\log3/6$. For
$j\ge2$, use


$$
\frac{\log(2j+1)}{2j(2j+1)}
 \le\frac{\log(3j)}{4j^2}.
$$


The function on the right is decreasing for real $j\ge1$.
Its sum from two is at most its integral from one, equal to
$(\log3+1)/4$. This proves (13) without any prime-distribution
theorem.

Markov's inequality therefore shows that the lower proportion, among
even indices, having $S(n)\le1$ is at least


$$
1-\mu_0=\frac{9-5\log3}{12}\approx0.292244879722.     \tag{14}
$$


Remove the three sets $n+1=3^\nu,5^\nu,7^\nu$, whose combined
count through $2X$ is $O(\log X)$. On every remaining index the
optional prime-power weight is either zero or


$$
w(n)\le\frac{\log11}{10}<\frac14.
$$


Here $\log x/(x-1)$ decreases for $x\ge3$.
For such indices, $D(n),b(n)\ge0$ and
$\epsilon_n^{(2)}\le1$, so


$$
\boxed{\log\Lambda(n)\le(\alpha-\eta)n+\log2,\qquad
 \eta=B-\frac54>0.}                                 \tag{15}
$$


The exact positivity of $\eta$ can also be certified without decimal
approximations: $\phi>8/5$, $e<11/4$, and
$(8/5)^{20}>2^6(11/4)^5$ imply
$\phi^{20}>2^6e^5$. Numerically
$\eta\approx0.116338354458$.

Thus at least the lower density (14) passes every current index-only
valuation budget with the fixed exponential margin (15). This is
not a claim that $q_n\le\Lambda(n)$, that the actual denominators
are small on this set, or that any shrinking subsequence exists.
It proves that the known mandatory divisor alone cannot exclude all
candidates, even after combining all primes at each index.

A parameterized version gives further bounds if desired. For any
$\mu_0<c<B$, indices with $S(n)\le c$ have lower even density
at least $1-\mu_0/c$. Choose $t\in(0,B-c)$. Only finitely many
primes have $\log p/(p-1)>t$, and their prime-power-minus-one sets
have density zero. Off those sets the mandatory divisor has a gap
at least $B-c-t>0$. This remains an elementary lower-divisor
statement, with no assumptions about actual cancellation.

## 5. Further joint restrictions from two selected shrinking indices

The index sieve does not replace the exact spacing restrictions.
Write $q_n=2^{a_n}o_n$, $o_n$ odd. For even $m>n$,


$$
v_2(p_mq_n-p_nq_m)=a_n,
$$


since both reduced numerators are odd and $a_m>a_n$.
Let $G_{n,m}=\gcd(M(n)J(n),M(m)J(m))$, an explicitly known
mandatory odd common divisor. The actual odd denominator gcd is
at least $G_{n,m}$. The uniform relative-error comparison gives


$$
|L_nL_m|\ge
 \frac{C\,2^{a_n}G_{n,m}\,e^{-\alpha m}}
 {1-(-1)^{(m-n)/2}e^{-\alpha(m-n)}}(1+o(1)),          \tag{16}
$$


uniformly for even $m>n\to\infty$. The factor in the denominator
stays between two fixed positive constants, so if both forms are
small and $s_j=-\log|L_j|$, then


$$
\boxed{s_n+s_m\le
 \alpha m-a_n\log2-\log G_{n,m}+O(1).}               \tag{17}
$$


The bounded term is uniform over pairs. This follows by substituting
$q_j=|L_j|e^{\alpha j}/C(1+o(1))$ into the full gcd-normalized
integer determinant bound; no estimate for a different rational is used.

For example, suppose a proposed subsequence satisfies
$|L_j|\le e^{-\delta j}$. For any two of its large indices $m>n$,


$$
(\alpha-\delta)m\ge
 (\beta+\delta)n+\log G_{n,m}+O(1).                  \tag{18}
$$


The dyadic lower bound alone forces $\delta\le B<\alpha$ for
any such infinite subsequence, so the denominator below is positive.
If $\delta>B/2$, its successive indices must have asymptotic ratio
at least


$$
\frac{\beta+\delta}{\alpha-\delta}>1.
$$


This is only a speed-dependent gap restriction. Arbitrarily slow
shrinkage does not acquire a geometric gap from (18). If the selected
indices share fixed odd prime divisors, their factorial depths can be
inserted into $\log G_{n,m}$, strengthening the restriction.

The previously proved adjacent-index conditions also remain:
on a shrinking subsequence both


$$
\frac{o_{n-2}}{\gcd(o_{n-2},o_n)},\qquad
 \frac{o_{n+2}}{\gcd(o_n,o_{n+2})}
$$


must tend to infinity. The Appell and minus-one theorems provide
lower bounds on neighboring denominators, not upper bounds or
bounded values of these quotients. They therefore do not turn this
necessary condition into an exclusion of the positive-density
budget-passing set in Section 4.

## 6. Precise remaining arithmetic input

The results now exclude many simultaneous divisibility patterns and
an explicit uniform family of prime-power exponents. They leave a
positive-density set of indices for which the known mandatory divisor
is exponentially too small to force nonshrinking. To close this
particular arithmetic route one needs an additional lower bound for
the actual denominator beyond $\Lambda(n)$, for example from primes
outside the supports of $n$ and the known prime-power $n+1$
families, or a constraint on actual neighboring odd gcds strong enough
to contradict (17) or the adjacent quotient conditions. No such
additional estimate is established here.
