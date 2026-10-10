> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The exact smooth divisor and prime-power saturation of the extremal content

Date: 2026-09-13. Original bounded continuation by audit_sources. Independent review passed: raw_extremal_smooth_divisor_independent_review.md.

This note makes the visible small-prime divisor of the actual extremal content completely explicit, before localization. On every degree $n=p^a$, $p>3$, $a\ge1$, it then proves the exact valuation


$$
\boxed{v_p(F_n)=\frac{2n(n-1)}{p-1}-2an.}
$$


The integer normalized matrix from the height improvement has a unit maximal minor at this prime. Thus its maximal-minor content has no additional $p$-factor at all, despite the large factorial factors of the original matrix.

This is an all-index obstruction to assuming an additional common factorial divisor of that normalized content. It does not prove that the remaining $n^2\log n$ term in the large-prime height bound is necessary: a fixed-prime deficit has only $O(n^2)$ logarithmic weight, and other primes or a selected determinant could still supply an improvement.

## 1. The finite-difference block gives a global content equality

Retain the actual matrix $X_n$ with rows $k=n,\ldots,3n$ and columns $B_j,C_j$, $0\le j<n$:


$$
(X_n)_{k,B_j}=(k)_j,\qquad
(X_n)_{k,C_j}=k!\tau_{k-j}.
$$


Let $F_n>0$ be its maximal-minor content. The integral row operation of raw_high_smith_finite_difference_reduction.md leaves the first $n$ rows unchanged and replaces the last $n+1$ by consecutive $n$-th differences. It is a unimodular lower triangular row operation. The result is


$$
\begin{pmatrix}V&C_0\\0&\mathcal G_n\end{pmatrix},
\qquad
\det V=\prod_{j=0}^{n-1}j!,
\tag{1}
$$


where $V$ has the first $n$ actual rows and the $n$ falling-factorial columns, and


$$
(\mathcal G_n)_{r,j}
=\sum_{s=0}^n(-1)^{n-s}\binom ns
(n+r+s)!\tau_{n+r+s-j},
\quad 0\le r\le n,\quad0\le j<n.
\tag{2}
$$



There is an exact global equality, stronger in normalization than merely localizing (1):


$$
\boxed{
F_n=V_n\,\theta_n,\qquad
V_n=\prod_{j=0}^{n-1}j!,\qquad
\theta_n=\gcd_{|I|=n}|\det\mathcal G_n[I,:]|.
}
\tag{3}
$$


To prove it, every maximal minor of the transformed matrix uses all $2n$ columns and $2n$ of its $2n+1$ rows. If it omits one of the first $n$ rows, the $B$-column block has rank at most $n-1$, so its determinant is zero. Every other maximal minor equals $\det V$ times an $n$-minor of $\mathcal G_n$. Unimodular row operations preserve the entire determinantal ideal over $\mathbb Z$. This proves (3), including all small-prime multiplicities.

The characteristic-zero full column rank of $X_n$ guarantees that the positive gcds in (3) are nonzero.

## 2. Exact weighted-minor formula and an explicit smooth divisor

Let


$$
L=L_{3n},\qquad
Z_{r,j}=\frac{L}{(n+r)!}(\mathcal G_n)_{r,j}.
$$


The preceding height note proves that $Z$ is an integer matrix. Define, with unchanged increasing row order,


$$
\delta_t=\det Z[\{0,\ldots,n\}\setminus\{t\},:],
\quad
c_t=\frac{(2n)!}{(n+t)!},\quad0\le t\le n,
$$


and put


$$
P_n=\prod_{r=0}^{n-1}(n+r)!,\qquad
h_n=\gcd_{0\le t\le n}|c_t\delta_t|>0.
$$


Each $c_t$ is an integer supported on primes at most $2n$. Row scaling gives exactly


$$
\det\mathcal G_n[\widehat t,:]
=\frac{P_n}{L^n}\,c_t\delta_t.
$$


Taking positive contents, as fractional $\mathbb Z$-ideals in $\mathbb Q$, and using (3) gives the actual integer identity


$$
\boxed{F_n=V_n\,\frac{P_n}{L^n}\,h_n.}
\tag{4}
$$


It is not necessary to assume $L^n\mid P_n$. Since each minor on the left of the preceding display is an integer, valuation comparison shows that


$$
\frac{L^n}{\gcd(P_n,L^n)}\mid c_t\delta_t
$$


for every $t$, hence divides $h_n$. Therefore


$$
\boxed{
S_n:=V_n\,\frac{P_n}{\gcd(P_n,L^n)}
\quad\hbox{is an integer divisor of }F_n.
}
\tag{5}
$$


It is supported on primes at most $3n$.

The logarithm of this visible divisor has the full leading order


$$
\log S_n=2n^2\log n+O(n^2).
\tag{6}
$$


Indeed


$$
V_nP_n=\prod_{k=0}^{2n-1}k!,
\qquad
\log\prod_{k=0}^{2n-1}k!=2n^2\log n+O(n^2),
$$


by elementary factorial summation. The removed gcd has logarithm at most
$n\log L_{3n}=O(n^2)$. This is precisely the factorial-size reduction already reflected in the new large-prime bound $n^2\log n+O(n^2)$; it is not an additional reduction of that remaining term.

Because all factors $c_t$ and $V_nP_n/L^n$ are units above $3n$, (4) also retains the exact equality of large-prime contents:


$$
v_q(F_n)=v_q(h_n)=\min_t v_q(\delta_t),
\qquad q>3n.
\tag{7}
$$


The weight factors cannot be discarded at small primes.

## 3. The normalized matrix modulo the degree's prime

Now suppose


$$
n=p^a,\qquad p>3,\qquad a\ge1.
$$


Since $3n<p^{a+1}$, one has $v_p(L)=a$. In the integer summand expression


$$
Z_{r,j}
=\sum_{s=0}^n(-1)^{n-s}\binom ns
\frac{(n+r+s)!}{(n+r)!}\,
L\tau_{n+r+s-j},
\tag{8}
$$


each factor $L\tau_\nu$ is an integer.

For $1\le s<n$, the binomial coefficient is divisible by $p$. For example,


$$
\binom{p^a}{s}=\frac{p^a}{s}\binom{p^a-1}{s-1}
$$


has valuation $a-v_p(s)\ge1$, since the last binomial is a $p$-unit. Thus all these summands vanish modulo $p$, uniformly in both row and column.

The $s=n$ summand also vanishes: its factorial ratio is a product of $n$ consecutive integers, so it contains a multiple of $p$. This argument needs no cancellation and also applies when the arctangent coefficient itself is zero.

Only $s=0$ remains:


$$
Z_{r,j}\equiv(-1)^nL\tau_{n+r-j}\pmod p.
\tag{9}
$$


Here $1\le n+r-j\le2n$. The quantity $L\tau_m$ can be nonzero modulo $p$ only if $m$ is odd and $v_p(m)=a$. In this interval the only multiples of $p^a=n$ are $n$ and $2n$, and the second is even. Therefore the sole surviving condition is $m=n$, or $r=j$.

Consequently


$$
\boxed{
Z\bmod p=
u\begin{pmatrix}I_n\\0\end{pmatrix},
\qquad
u=(-1)^{(n+1)/2}\frac{L}{n}\in\mathbb F_p^\times.
}
\tag{10}
$$


This is the actual entire normalized matrix, not a claim about a single diagnostic entry.

In particular


$$
v_p(\delta_n)=0,\qquad
\min_t v_p(\delta_t)=0,\qquad
v_p(h_n)=0,
\tag{11}
$$


because $c_n=1$. All other $\delta_t$ are zero modulo $p$, but their higher valuations are not needed.

Equation (10) proves a specified nonzero maximal minor for every degree in this infinite family. It also proves that the normalized maximal-minor content has exactly zero $p$-valuation. Hence it cannot have a universal positive power of $n!$ as a divisor.

## 4. Exact original valuation and saturation of the visible divisor

Taking valuations in (4) and using (11) gives


$$
v_p(F_n)=
\sum_{k=0}^{2n-1}v_p(k!)-na.
\tag{12}
$$


To evaluate the sum, for each $1\le e\le a$, $p^e$ divides $2n$, and


$$
\sum_{k=0}^{2n-1}\left\lfloor\frac{k}{p^e}\right\rfloor
=\frac{2n^2}{p^e}-n.
$$


There is no term with $e>a$, since $2n<p^{a+1}$. Summing the geometric series yields


$$
\sum_{k=0}^{2n-1}v_p(k!)
=\frac{2n(n-1)}{p-1}-an.
$$


Together with (12),


$$
\boxed{
v_p(F_n)=\frac{2n(n-1)}{p-1}-2an.
}
\tag{13}
$$


For $a=1$ this is zero; the formula includes that boundary case.

The smooth divisor (5) is saturated at this prime:


$$
\boxed{v_p(F_n/S_n)=0.}
\tag{14}
$$


Indeed $v_p(P_n)\ge na$, since each factorial $(n+r)!$ contains at least the factor $n=p^a$, and there are $n$ such factors. Thus $v_p(\gcd(P_n,L^n))=na$, and (5) has exactly the valuation (12).

The same unit minor yields an original square minor with that exact valuation. Select the first $2n$ rows of $X_n$, namely $n,\ldots,3n-1$. The finite-difference row transformation restricted to those rows is still lower triangular with determinant one: its last retained difference is $r=n-1$, whose latest original row is $3n-1$. Its determinant is therefore


$$
\det V\ \det\mathcal G_n[\{0,\ldots,n-1\},:].
$$


By (11)–(12), this is nonzero and has $p$-valuation $v_p(F_n)$. No unspecified pivot or row selection is required on these prime-power degrees.

## 5. What this obstructs, and what remains open

The result rules out the proposed uniform route of extracting an additional common factorial factor from the normalized maximal-minor content. For $n=p^a$, $p>3$, that content is a $p$-unit, so every assertion forcing it to contain a positive power of the $p$-part of $n!$ is false. The earlier entry obstruction is now strengthened to an entire-content statement with an exact original Smith-depth consequence.

It does not rule out a divisor of size $(n!)^{\theta n}\exp(-O(n^2))$ supplied by other primes or a specially chosen determinant. For a fixed $p$, the missing logarithmic factorial contribution is only $O(n^2)$, so it can be absorbed in such a correction. It also does not prove a lower bound on the large-prime content. An improvement removing a positive portion of the remaining $n^2\log n$ therefore remains open.

The exact next arithmetic object is $h_n$ in (4), or a selected nonzero $\delta_t$, with the small-prime row weights retained. The finite-difference recurrence, the Frobenius trace factorization, and the adjacent content relation currently do not supply further all-degree smooth divisibility of this integer.

Finally, the endpoint identity $\mathcal E_n=(-1)^nF_nZ_n$ retains its separate primitive-dual scalar $Z_n$. Equations (3)–(14) concern $F_n$ and do not absorb or bound that scalar, the primitive endpoint denominator, or the error in the original approximation to $e+\pi$.
