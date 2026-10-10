> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact Cauchy congruence, block rank, and truncated Smith depths at primes dividing n

Date: 2026-09-13. Original bounded continuation by audit_sources, starting from root's proposed first-layer congruence. Independent review passed: raw_extremal_cauchy_rank_depth_independent_review.md.

The normalized integer matrix from the actual extremal problem satisfies an exact congruence modulo $n$, stronger than a congruence modulo one prime:


$$
Z_{r,j}\equiv(-1)^nL_{3n}\tau_{n+r-j}\pmod n.
$$


For every odd prime $p\mid n$, put


$$
T=p^{\lfloor\log_p(3n)\rfloor},\qquad b=n\bmod T,\quad0\le b<T.
$$


This note proves the full rank formula


$$
\boxed{\operatorname{rank}_{\mathbb F_p}Z
=n-\min(b,T-1-b).}
$$


It also gives the exact equality of the Smith exponents of $Z$ and the simpler integer Cauchy matrix, truncated at $v_p(n)$, and an explicit finite sum valid at every higher precision.

As a consequence, the previous saturation theorem extends from $n=p^\nu$ to


$$
n=mp^\nu,\qquad 3m<p,
$$


where the original extremal content satisfies


$$
\boxed{v_p(F_n)=\frac{2n(n-m)}{p-1}-2\nu n.}
$$


The congruence-depth contribution is at most $n\log n$ in logarithmic size. No improvement to the leading large-prime height term follows from these results alone.

## 1. Definitions and rechecked normalization

Use


$$
(\mathcal G_n)_{r,j}
=\sum_{s=0}^n(-1)^{n-s}\binom ns
(n+r+s)!\tau_{n+r+s-j},
\quad0\le r\le n,\quad0\le j<n,
$$




$$
L=L_{3n},\qquad
Z_{r,j}=\frac{L}{(n+r)!}(\mathcal G_n)_{r,j}\in\mathbb Z.
$$


Here $\tau_a=0$ for positive even $a$, and
$\tau_a=(-1)^{(a-1)/2}/a$ for positive odd $a$.

The global block argument in raw_extremal_smooth_divisor_and_prime_power_saturation.md was rechecked before this extension: the row transformation is unimodular; every nonzero full-column minor retains all $n$ top B rows; its determinant factors by $\prod_{j=0}^{n-1}j!$. Thus


$$
F_n=\left(\prod_{j=0}^{n-1}j!\right)
\operatorname{content}_n(\mathcal G_n)
$$


holds over $\mathbb Z$, not just after localization. The weighted-minor identity and the factorial-valuation sum in that note remain unchanged.

Define the simpler integer matrix


$$
(\mathcal C_n)_{r,j}=L\tau_{n+r-j}.
\tag{1}
$$


It has the same dimensions as $Z$, and all its Taylor indices are between 1 and $2n$.

## 2. The entire nonconstant sum is divisible by n

For every $1\le s\le n$, the following is an identity of integers:


$$
\boxed{
\binom ns\frac{(n+r+s)!}{(n+r)!}
=n(s-1)!\binom{n-1}{s-1}\binom{n+r+s}{s}.
}
\tag{2}
$$


All factors $L\tau_{n+r+s-j}$ are integers. Separating the $s=0$ term therefore gives


$$
\boxed{Z=(-1)^n\mathcal C_n+n\mathcal A_n,\qquad
\mathcal A_n\in\operatorname{Mat}_{n+1,n}(\mathbb Z).}
\tag{3}
$$


This proves the congruence modulo $n$, including all its prime-power factors. It avoids any dependence on a finite-field exponential or a guessed divisibility of a rational summand.

## 3. The exact finite-field support and its coefficients

Fix an odd prime $p\mid n$, and write


$$
T=p^a,\qquad a=\lfloor\log_p(3n)\rfloor.
$$


Then $v_p(L)=a$, and


$$
3n<pT,\qquad 2n/T<2p/3<p.
$$


For $1\le m\le2n$, the value $L\tau_m$ is zero modulo $p$ unless $m$ is an odd multiple of $T$. If $m=T h$, then $1\le h<p$, and


$$
L\tau_{Th}=
\frac{L}{T}(-1)^{(T-1)/2}\tau_h
\quad\hbox{in }\mathbb F_p,
\tag{4}
$$


where the right side is zero for even $h$. For odd $h$, the sign identity follows by writing


$$
(Th-1)/2=(T-1)/2+T(h-1)/2.
$$


The scalar $L/T$ is a $p$-unit.

By (3), $Z\bmod p$ is therefore supported on


$$
r-j\equiv-n\pmod T.
\tag{5}
$$


After permuting rows and columns by their residues modulo $T$, it is a direct sum of small rectangular blocks. No approximation is involved in this block decomposition.

## 4. Every surviving block has its full possible rank

Write $n=qT+b$, $0\le b<T$, and fix a column residue $j_0$, $0\le j_0<T$. Its columns have the form


$$
j=j_0+vT,\qquad0\le v<C,
$$


where


$$
C=
\begin{cases}q+1,&j_0<b,\\q,&j_0\ge b.\end{cases}
$$


Ignore a block with $C=0$. The associated row residue is


$$
r_0=j_0-b+\epsilon T,\qquad
\epsilon=\begin{cases}1,&j_0<b,\\0,&j_0\ge b.\end{cases}
$$


Its rows are $r=r_0+uT$, $0\le u<R$, with


$$
R=
\begin{cases}q+1,&r_0\le b,\\q,&r_0>b.\end{cases}
$$


In particular $R,C\in\{q,q+1\}$, and


$$
\frac{n+r-j}{T}=q+\epsilon+u-v=C+u-v.
$$


Up to the common nonzero scalar in (4) and the factor $(-1)^n$, the block is exactly


$$
\bigl(\tau_{C+u-v}\bigr)_{0\le u<R,\ 0\le v<C}.
\tag{6}
$$



All occurring positive indices in (6) are less than $p$. Split rows and columns by the parity of $u,v$. Each nonzero parity block, after row and column sign changes, is a Cauchy matrix $1/(C+u-v)$. Its denominators are nonzero modulo $p$, and its row and column parameters are distinct modulo $p$. The Cauchy determinant formula therefore makes every square submatrix of an allowed parity block nonsingular.

If $R=C$, the parity counts match: for odd $C$ the nonzero blocks match equal parities, and for even $C$ they match opposite parities, each of equal size. Thus the square block is invertible. If $R=C+1$, its first $C$ rows already give this invertible square. If $R=C-1$, the two parity blocks have row counts no larger than their corresponding column counts, so both have full row rank. The zero-size cases obey the same conclusion. Therefore


$$
\boxed{\operatorname{rank}(6)=\min(R,C).}
\tag{7}
$$



## 5. Counting the deficient blocks

A block loses one column rank precisely when $j_0<b$ but $r_0>b$. In that case


$$
0\le j_0<b,\qquad j_0>2b-T.
$$


Their number is


$$
b-\max(0,2b-T+1)=\min(b,T-1-b).
$$


Every other block has full column rank. Since the original column count is $n$, this proves


$$
\boxed{
\operatorname{rank}_{\mathbb F_p} Z
=n-\min(b,T-1-b).
}
\tag{8}
$$



For $n<T$, the formula reduces to
$\max(0,2n-T+1)$, as in root's proposed shifted-identity case. For $T=n$, it gives rank $n$, with the prior scalar $[I_n;0]$ matrix. For $T<n$, (6)–(7) account for all the additional blocks rather than treating them as one diagonal.

Because both $n$ and $T$ are divisible by $p$, so is $b$. The alternative $b=T-1$ is impossible. Thus full rank occurs if and only if $b=0$.

Writing $n=mp^\nu$ with $p\nmid m$, one always has $a\ge\nu$. The condition $T\mid n$ is therefore $a=\nu$, equivalently


$$
\boxed{Z\bmod p\text{ has full column rank }
\Longleftrightarrow 3m<p.}
\tag{9}
$$


There is no such full-rank case for $p=3$.

For the normalized maximal-minor content
$\Theta_Z=\operatorname{content}_n(Z)$, the rank formula yields the rigorous first-layer divisor


$$
\boxed{
v_p(\Theta_Z)\ge \min(b,T-1-b).
}
\tag{10}
$$


Indeed there are exactly this many nonunit Smith invariant factors, each contributing at least one to their sum. Equation (10) is a lower bound on the full valuation, not an equality unless the rank is full.

## 6. Exact original depth in the larger saturated family

Suppose $n=mp^\nu$ and $3m<p$. Then $T=p^\nu$, $b=0$. The first $n$ rows $r=0,\ldots,n-1$ contain exactly $m$ rows and $m$ columns in each residue block. By the square case of (7), their determinant is a $p$-unit.

In the global weighted-minor identity from the preceding note,


$$
F_n=\left(\prod_{j=0}^{n-1}j!\right)
\frac{P_n}{L^n}h_n,\qquad
P_n=\prod_{r=0}^{n-1}(n+r)!,
$$


the associated weight is $c_n=1$. Hence $h_n$ is a $p$-unit and


$$
v_p(F_n)=\sum_{k=0}^{2n-1}v_p(k!)-\nu n.
$$


Since $2n<p^{\nu+1}$ and $p^e\mid2n$ for $1\le e\le\nu$,


$$
\sum_{k=0}^{2n-1}v_p(k!)
=2n^2\sum_{e=1}^{\nu}p^{-e}-\nu n
=\frac{2n(n-m)}{p-1}-\nu n.
$$


Therefore


$$
\boxed{
v_p(F_n)=\frac{2n(n-m)}{p-1}-2\nu n.
}
\tag{11}
$$


The same visible smooth divisor is saturated at $p$, and the first $2n$ original rows $n,\ldots,3n-1$ form a nonzero minor attaining this valuation. The row-restriction argument is the same unimodular triangular one used in the prime-power note.

## 7. A Smith-depth lift through the whole modulus n

The congruence (3) gives more than (8). Let $\nu=v_p(n)$, now allowing any prime divisor $p$ of $n$, and let


$$
a_1\le\cdots\le a_n
$$


be the Smith exponents of the integer matrix $\mathcal C_n$ over $\mathbb Z_p$. It has full rational column rank: its first $n$ rows split into square parity Cauchy blocks with nonzero rational determinants. Let $e_i$ be the corresponding exponents of $Z$.

Then


$$
\boxed{\min(e_i,\nu)=\min(a_i,\nu)
\quad(1\le i\le n).}
\tag{12}
$$


Here the sign $(-1)^n$ is a unit and has no effect.

A direct proof avoids assuming that determinantal congruences alone identify every exponent. Put $\mathcal C_n$ in Smith form by invertible row and column operations over $\mathbb Z_p$; (3) becomes a diagonal Smith matrix plus a matrix divisible by $p^\nu$. For every diagonal exponent $a_i<\nu$, its pivot is $p^{a_i}$ times a unit. The off-pivot entries in its row and column are divisible by $p^\nu$, so eliminating them uses integral coefficients and changes the remaining block only by terms still divisible by $p^\nu$. Remove these pivots successively. All entries in the remaining block are divisible by $p^\nu$. This proves exactly (12).

In particular


$$
v_p(\Theta_Z)\ge\sum_i\min(a_i,\nu).
\tag{13}
$$


If every $a_i<\nu$, all Smith exponents, and hence the complete content valuation, agree with those of $\mathcal C_n$. If any $a_i\ge\nu$, their deeper values are not determined by (12).

For a global formulation, let $d_i(\mathcal C_n)$ be its positive integer Smith invariant factors. Then


$$
\boxed{
\prod_{i=1}^n\gcd(d_i(\mathcal C_n),n)\mid\Theta_Z.
}
\tag{14}
$$


This product is at most $n^n$. Its logarithm is therefore at most $n\log n$, so even a full evaluation of this particular truncated divisor would not remove the leading $n^2\log n$ height term.

The Smith data in (12) are data of an explicit Cauchy matrix, without factorial differences. If desired they can be computed from exact product formulas: a nonzero minor of $\mathcal C_n$ splits by original row parity $n+r$ against the opposite column parity. Its absolute determinant is $L^k$ times the products of the corresponding row and column Vandermondes divided by
$\prod(n+r-j)$. Apart from the separately displayed factor $L^k$, every factor in those Cauchy products is an integer of magnitude at most $2n$. Taking valuations of these product formulas and their determinantal minima gives the $a_i$. No closed minimization beyond the first-layer formula (8) is claimed here.

## 8. A finite formula at every higher precision

The exact expansion (2) also controls which difference levels can survive modulo $p^h$. If $h>\nu=v_p(n)$, any term with


$$
s\ge p(h-\nu)+1
$$


has


$$
v_p\bigl(n(s-1)!\bigr)\ge
\nu+\left\lfloor\frac{s-1}{p}\right\rfloor\ge h.
$$


All other factors in (2), including $L\tau$, are integers. Hence modulo $p^h$ it suffices to retain the terms


$$
\boxed{0\le s\le\min\{n,p(h-\nu)\}.}
\tag{15}
$$


For $h\le\nu$, only $s=0$ is needed, as in (3).

The retained positive-$s$ term is explicitly


$$
(-1)^{n-s}n(s-1)!
\binom{n-1}{s-1}
\binom{n+r+s}{s}
L\tau_{n+r+s-j}.
$$


Thus (15) is a finite sum of shifted arctangent Cauchy matrices multiplied by known integer row factors. It is an exact congruence of the original normalized matrix; no lift, carry, or unspecified polynomial part is dropped.

Formula (15) is not an upper bound for the eventual content depth. As $h$ increases, more shifts can contribute, and the singular part still needs to be analyzed. It provides a concrete next finite-level problem, with controlled truncation, instead of assuming that the first-layer rank determines all multiplicities.

No new finite-degree or prime scan is used anywhere in this note. The primitive-dual endpoint scalar remains separate, and no irrationality conclusion follows from these small-prime results.
