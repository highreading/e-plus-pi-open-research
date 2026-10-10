> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A sharper actual large-prime extremal-content bound and the factorial-scaling obstruction

Date: 2026-09-13. Original bounded continuation by audit_sources; the prime-power last-column obstruction in §4 was suggested by root and independently checked here. Independent review passed: raw_extremal_height_root_review.md.

For the actual extremal maximal-minor content $F_n$, this note proves


$$
\boxed{\log F_{n,>3n}\le n^2\log n+O(n^2).}
$$


The preceding elementary bound had leading term $3n^2\log n$. The improvement uses the actual finite-difference matrix and an integral row normalization, with every clearing factor supported on primes at most $3n$.

An $O(n^2)$ bound is not proved. Dividing by one additional $n!$ makes the normalized entries $\exp(O(n))$, but a fixed actual entry shows that its denominator cannot be cleared by a uniform $\exp(Cn)$ factor. A second exact prime-power family refutes uniform $n!$-divisibility of the integral normalized rows. These obstructions concern this straightforward normalization; they do not exclude a better determinant identity or another basis.

## 1. The exact actual reduction

Let $X_n$ be the $(2n+1)$-by-$2n$ matrix with rows $k=n,\ldots,3n$, columns $B_j,C_j$, $0\le j<n$, and entries


$$
(X_n)_{k,B_j}=(k)_j,\qquad
(X_n)_{k,C_j}=k!\tau_{k-j},\qquad
\tau_a=[z^a]\arctan z.
$$


Write $F_n>0$ for the gcd of all its maximal minors. Every low-A-degree condition is retained.

The reviewed finite-difference reduction in
raw_high_smith_finite_difference_reduction.md §4 gives, for $p>3n$,


$$
X_n\sim_{\mathbb Z_p}\operatorname{diag}(I_n,\mathcal G_n),
$$


where


$$
(\mathcal G_n)_{r,j}
=\sum_{s=0}^n(-1)^{n-s}\binom ns
(n+r+s)!\tau_{n+r+s-j},
\quad 0\le r\le n,\quad 0\le j<n.
\tag{1}
$$


The elimination is integral before inverting the falling-factorial Vandermonde, whose determinant is a product of $j!$, $j<n$. Thus it preserves all large-prime Smith depths. The matrix $\mathcal G_n$ has full column rank over $\mathbb Q$, because the actual $X_n$ does.

Put


$$
L=L_{3n}=\operatorname{lcm}(1,2,\ldots,3n)
$$


and introduce the new matrix


$$
\boxed{
Z_{r,j}=\frac{L}{(n+r)!}(\mathcal G_n)_{r,j}
=\sum_{s=0}^n(-1)^{n-s}\binom ns
\frac{(n+r+s)!}{(n+r)!}\,
L\tau_{n+r+s-j}.
}
\tag{2}
$$


Every entry is an integer. Indeed the factorial ratio is an integer, and each nonzero $\tau_a$ has denominator $a$, where


$$
1\le n+r+s-j\le3n.
$$


Thus $L\tau_a\in\mathbb Z$ term by term.

The row multiplier $L/(n+r)!$ is a unit in $\mathbb Z_p$ for every $p>3n$. Therefore


$$
v_p(F_n)=
\min_{\substack{I\subset\{0,\ldots,n\}\\|I|=n}}
v_p(\det Z[I,:]),\qquad p>3n.
\tag{3}
$$


This is an equality at every prime-power depth. It is not merely a rational row-rank equivalence.

## 2. Actual normalized entry bounds

For fixed $r$, let


$$
t_s=\binom ns\frac{(n+r+s)!}{(n+r)!},\qquad 0\le s\le n.
$$


For $1\le s\le n$,


$$
\frac{t_{s-1}}{t_s}
=\frac{s}{(n-s+1)(n+r+s)}
\le\frac{n}{2n+r}\le\frac12.
$$


Since $|\tau_a|\le1$,


$$
\boxed{
|Z_{r,j}|
\le L\sum_{s=0}^n t_s
\le2L\frac{(2n+r)!}{(n+r)!}.
}
\tag{4}
$$


This retains the actual factorial ratios instead of bounding the original unnormalized rows by $(3n)!$.

Choose any nonzero maximal minor of $Z$, which exists by its full rational column rank. Hadamard's inequality and (4) give


$$
|\det Z[I,:]|
\le (2L\sqrt n)^n
\prod_{r\in I}\frac{(2n+r)!}{(n+r)!}.
\tag{5}
$$


The factorial ratio increases with $r$, so the last product is at most the one with $r=1,\ldots,n$. In particular it is at most $(3n)^{n^2}$. By (3), the positive integer $F_{n,>3n}$ divides this nonzero integer minor. Consequently


$$
\boxed{
F_{n,>3n}
\le (2L_{3n}\sqrt n)^n
\prod_{r=1}^n\frac{(2n+r)!}{(n+r)!}
\le (2L_{3n}\sqrt n)^n(3n)^{n^2}.
}
\tag{6}
$$



Only an elementary exponential bound for the lcm is needed. For $N\ge2$,


$$
L_N\mid L_{\lceil N/2\rceil}\binom{N}{\lfloor N/2\rfloor}.
$$


For a prime whose highest power below $N$ exceeds $\lceil N/2\rceil$, the displayed binomial supplies its one missing power; all lower powers are already in the first lcm. This proves the divisibility prime by prime. Iterating and using $\binom{N}{\lfloor N/2\rfloor}\le2^N$ gives


$$
\log L_N\le
(2N+\lceil\log_2N\rceil)\log2.
$$


In particular $L_{3n}\le6n\,64^n$. Thus one completely explicit consequence of (6) is


$$
\boxed{
F_{n,>3n}\le
(12n^{3/2})^n(192n)^{n^2}.
}
\tag{7}
$$


It proves the claimed leading bound $n^2\log n+O(n^2)$ without a prime number theorem.

For comparison with the preceding bound in
raw_accessory_norm_resultant_and_height.md §6, that argument removed the factors $j!$ from the original columns and bounded a remaining minor by
$(2n)^n2^{6n^2}((3n)!)^n$. Its logarithm was $3n^2\log n+O(n^2)$. Equations (2)–(7) improve that actual large-prime leading term. The weaker cubic-log norm-resultant height is not used.

The reviewed divisibility for the original unbordered high content,
$v_p(D_n)\le v_p(F_n)$ for $p>3n$, transfers this same bound to its large-prime part. It does not bound the separate scalar $Z_n$ in the endpoint factorization
$\mathcal E_n=(-1)^nF_nZ_n$; this scalar should not be confused with the matrix $Z$ in (2).

## 3. The tempting extra factorial scaling and its exact denominators

Define


$$
Y_{r,j}=\frac{(\mathcal G_n)_{r,j}}{n!(n+r)!}
=\frac{Z_{r,j}}{L\,n!}.
$$


Its entries do satisfy the favorable Archimedean bound


$$
\boxed{
|Y_{r,j}|
\le 2\binom{2n+r}{n}
\le2^{3n+1}.
}
\tag{8}
$$


But its known common integer clearer is $L\,n!$, whose logarithm is $n\log n+O(n)$, not $O(n)$. Clearing a maximal minor with $(L\,n!)^n$ reproduces the remaining $n^2\log n$ term. The fact that these are only small-prime denominators does not reduce the size of the resulting rational numerator.

There is an exact actual obstruction to replacing that common denominator by a uniform $\exp(Cn)$ bound. For every odd $n$, equation (1) at $r=j=0$ has only even $s$ terms and gives


$$
(\mathcal G_n)_{0,0}=(n-1)!\,b_n,
$$


where


$$
b_n=(-1)^{(n+1)/2}
\sum_{\substack{0\le s\le n\\s\ {\rm even}}}
(-1)^{s/2}\binom ns(n)_s.
\tag{9}
$$


Here $(n)_s=n(n+1)\cdots(n+s-1)$ is rising, with $(n)_0=1$. Every nonconstant summand is divisible by $n$. Hence


$$
b_n\equiv(-1)^{(n+1)/2}\pmod n,
\qquad \gcd(b_n,n)=1.
\tag{10}
$$


In particular the entry is nonzero. Since


$$
Y_{0,0}=\frac{b_n}{n^2(n-1)!},
$$


its reduced denominator $q_n$ has the exact valuations


$$
\boxed{
v_p(q_n)=v_p((n-1)!)+2v_p(n),\qquad p\mid n.
}
\tag{11}
$$



To see the uniform consequence, fix any finite set $S$ of odd primes, set $N_S=\prod_{p\in S}p$, and take $n=N_S^a$, $a\to\infty$. Legendre's factorial-valuation formula gives


$$
\liminf_{a\to\infty}\frac{\log q_n}{n}
\ge\sum_{p\in S}\frac{\log p}{p-1}.
\tag{12}
$$


The sums on the right are unbounded as finite sets of odd primes grow. For example Euler's elementary divergence of $\sum_p1/p$ implies this; that divergence follows because otherwise the Euler products would be bounded, whereas their expansions bound the harmonic sums from above and these diverge. Thus there is no absolute constant $C$ with $q_n\le e^{Cn}$ for every odd $n$.

Multiplication by $L_{3n}$ does not repair this obstruction for the further-scaled integer matrix $Z/n!=L_{3n}Y$. At each fixed $p\in S$, it removes at most $\lfloor\log_p(3n)\rfloor=O(\log n)$ powers, so the same limit lower bound (12) holds for that entry's reduced denominator.

This is an obstruction to this entrywise exponential-denominator shortcut, not a proof that a maximal-minor numerator cannot be much smaller. Determinant cancellations, another basis, or a content identity are still possible.

## 4. A second exact obstruction on a prime-power family

Root suggested the following complementary last-column test. Let


$$
n=p^a,\qquad p>3\text{ prime},\qquad a\ge2,
$$


and take $r=0,j=n-1$. Then


$$
Q:=\frac{(\mathcal G_n)_{0,n-1}}{n!}
=\sum_{s=0}^n(-1)^{n-s}\binom ns
\frac{(n+s)!}{n!}\tau_{s+1}.
\tag{13}
$$


The $s=0$ term is $(-1)^n$. For $1\le s<n$,


$$
v_p\binom ns=a-v_p(s),\qquad
v_p\frac{(n+s)!}{n!}=v_p(s!).
$$


For the first identity, write
$\binom ns=(n/s)\binom{n-1}{s-1}$; each factor
$(n-t)/t$, $1\le t<s<n$, is a $p$-unit congruent to $-1$.
The second identity follows from $v_p(n+t)=v_p(t)$ for $t<n$.

Every nonzero term of (13) in this range has valuation


$$
a+v_p((s-1)!)-v_p(s+1)\ge1.
$$


If $s+1<n$, then $v_p(s+1)\le a-1$. If $s=n-1$, its exceptional denominator has valuation $a$, but $(n-2)!$ has a $p$-factor because $a\ge2$. Finally the $s=n$ term is zero: $n$ is odd, so $\tau_{n+1}=0$. Thus


$$
Q\equiv(-1)^n\pmod p.
$$


Because $v_p(L_{3n})=a$ for $p>3$, equation (2) gives the exact valuation


$$
\boxed{
v_p(Z_{0,n-1})=a,
\qquad
v_p(n!)=\frac{p^a-1}{p-1}>a.
}
\tag{14}
$$


So the proposed additional row divisor $n!$ does not divide even this actual entry on an infinite family. No finite scan is used to establish (9)–(14).

## 5. The remaining determinant-level target

The improvement (6) is unconditional and retains every large-prime exponent. An $O(n^2)$ bound would require an additional mechanism. One sufficient concrete route is to find a nonzero maximal minor $\delta_n$ of the integer matrix (2) whose small-prime part is at least


$$
(n!)^n\exp(-O(n^2)).
$$


Together with (6), that would leave a large-prime part of size $\exp(O(n^2))$. The present row normalization, the finite-difference entry recurrences, and the adjacent unit-chart condensation do not prove such a divisor. The obstructions above show why it cannot simply be asserted entry by entry.

The exact content factorization through the primitive dual polynomial likewise retains a separate scalar denominator contribution. It does not supply this missing small-prime divisor or an upper bound for the primitive endpoint denominator. No bound for a shrinking nonzero integer form, and no proof concerning the rationality of $e+\pi$, is claimed.
