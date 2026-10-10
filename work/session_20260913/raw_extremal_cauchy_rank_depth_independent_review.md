> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the Cauchy congruence, rank and Smith-depth theorem

Date: 2026-09-13. Reviewer: audit_results.

Target: raw_extremal_cauchy_congruence_rank_and_depth.md, Sections 1–8.
The normalization was checked against
raw_extremal_smooth_divisor_and_prime_power_saturation.md.

**Verdict: PASS.** The congruence holds modulo the entire integer $n$;
the rank formula is valid for every odd prime dividing $n$, including
the multiple-block regime $T<n$. The larger saturated family, its
specified original minor and exact valuation, the truncated Smith
equivalence, and the higher-precision finite cutoff all check.
No numerical degree or prime scan was performed.

One optional wording clarification was sent to the author: in Section 3,
the matrix is *supported on* the congruence class (5); some entries
inside that class vanish because their quotient index is even.
The actual block calculation already preserves these zeros, so this
does not affect any theorem.

## 1. Exact integer normalization and global content

The arctangent index in the full sum satisfies


$$
1\le n+r+s-j\le3n.
$$


Thus $L_{3n}\tau_{n+r+s-j}$ is always an integer, including the
zero even-index cases. The factorial ratio is also an integer.
The displayed matrix $Z$ is therefore integral without a
termwise cancellation argument.

The finite-difference row operation on the original matrix is integral
lower triangular with diagonal one. Its first $n$ rows are unchanged,
and each remaining row is the $n$-th difference ending at that
original row. It kills the falling-factorial $B$ columns below the
first block. That first block has determinant $\prod_{j<n}j!$, by
the Vandermonde formula on consecutive integers.

A maximal minor uses all $2n$ columns. Omitting one of the first
$n$ rows gives $B$-column rank below $n$, hence determinant zero.
All other maximal minors factor by that same first-block determinant.
Unimodular row operations preserve the determinantal ideal, proving
the global content equality used in Section 1.

The exact scalar identity underlying (2) is


$$
\binom ns\,s!
=n(s-1)!\binom{n-1}{s-1}.
$$


Multiplying by $\binom{n+r+s}{s}$ gives (2). Every remaining factor
is integral, so separating $s=0$ proves
$Z=(-1)^n\mathcal C_n+n\mathcal A_n$ over $\mathbb Z$.
There is no division by $s$ in the resulting divisibility argument.

## 2. The finite-field support and all residue blocks

Let $p\mid n$ be odd, $a=\lfloor\log_p(3n)\rfloor$ and $T=p^a$.
Then $v_p(L)=a$, $3n<pT$, and $2n/T<p$.
For $1\le m\le2n$, an odd $m$ contributes nontrivially modulo
$p$ precisely when $v_p(m)=a$. These are $m=Th$ with
$1\le h<p$ odd. For such $h$,


$$
(-1)^{(Th-1)/2}
=(-1)^{(T-1)/2}(-1)^{(h-1)/2},
$$


since $T$ is odd. This proves the exact coefficient formula (4);
for even $h$ both sides vanish.

Write $n=qT+b$. For a column residue $j_0$, the number of columns
is $C=q+\epsilon$, where $\epsilon=1$ exactly when $j_0<b$.
The associated row residue
$r_0=j_0-b+\epsilon T$ belongs to $0,\ldots,T-1$, and its count
is $R=q+1$ exactly when $r_0\le b$. On these rows and columns,


$$
(n+r-j)/T=q+\epsilon+u-v=C+u-v.
$$


All these indices are positive: their minimum is one. Their maximum
is below $p$, either from the original index bound or directly from
the residue-block counts. Blocks with no columns may be discarded;
blocks with columns but no rows have rank zero, as (7) states.

## 3. Parity-Cauchy ranks, including $T<n$

Write $u=2U+\varepsilon_u$, $v=2V+\varepsilon_v$.
On an allowed parity pair, $C+\varepsilon_u-\varepsilon_v$ is odd,
and the sign in $\tau_{C+u-v}$ factors into one fixed sign times
$(-1)^U(-1)^V$. Thus row and column sign changes leave the matrix
with entries


$$
\frac1{C+\varepsilon_u-\varepsilon_v+2U-2V}.
$$


Every denominator is nonzero modulo $p$. Row and column parameters
are distinct modulo $p$, since their differences are nonzero even
integers of magnitude below $p$. The Cauchy determinant formula
therefore gives full possible rank to each allowed parity block.

For $R=C$, the two matching parity sizes are equal: same parity
when $C$ is odd, opposite parity when $C$ is even.
For $R=C+1$, the first $C$ rows already contain an invertible
square block. For $R=C-1$, the two row parity counts are each no
larger than their matching column counts. Thus the total rank is
exactly $\min(R,C)$, with the empty cases included.

This is a blockwise argument for arbitrary $q$; it does not silently
use $q=0$ or $q=1$. Consequently it covers $T<n$.

## 4. Counting defects and the full-rank criterion

Only $C=q+1,R=q$ loses column rank. Its residues satisfy


$$
0\le j_0<b,\qquad j_0>2b-T.
$$


The exact count is


$$
b-\max(0,2b-T+1)=\min(b,T-1-b).
$$


Summing ranks over the residue blocks proves (8).

Full rank requires $b=0$ or $b=T-1$. Because $p$ divides
both $n$ and $T$, it divides $b$, while it does not divide
$T-1$; the latter alternative is impossible.
If $n=mp^\nu$ with $p\nmid m$, then $a\ge\nu$.
Hence $T\mid n$ is equivalent to $a=\nu$, which is equivalent
to $3m<p$. This proves (9), including the exclusion of $p=3$.

The rank deficiency equals the number of nonunit Smith factors.
Each contributes at least one to the content valuation, giving
(10). The note correctly makes no equality claim for that valuation
when the deficiency is positive.

## 5. Specified original minor and exact saturated valuation

When $3m<p$, $T=p^\nu$, and the first $n=mT$ rows have
exactly $m$ members in every residue block, matching the columns.
Their determinant is a $p$-unit by the preceding square-block
argument. In the weighted-minor formula this is $\delta_n$, whose
weight $c_n$ is exactly one. Thus the weighted content $h_n$,
not merely the unweighted normalized content, is a $p$-unit.

The original valuation is therefore


$$
v_p(F_n)=\sum_{k=0}^{2n-1}v_p(k!)-\nu n.
$$


Since $2n<p^{\nu+1}$ and $p^e\mid2n$ for $e\le\nu$,


$$
\sum_{k=0}^{2n-1}\left\lfloor k/p^e\right\rfloor
=2n^2p^{-e}-n.
$$


Summation gives the exact formula


$$
v_p(F_n)=\frac{2n(n-m)}{p-1}-2\nu n.
$$


Also $v_p(P_n)\ge\nu n$, since every factorial in $P_n$
contains the factor $n$. Hence the visible smooth divisor has
the same valuation.

Restricting the triangular row transformation to the first $2n$
original rows is legitimate: its last retained difference ends at
the original row $3n-1$ and uses no later row. The original square
minor on rows $n,\ldots,3n-1$ therefore has exactly the displayed
valuation and is nonzero. The existence claim is accompanied by a
fully specified row set.

## 6. Smith exponents through the entire congruence depth

The first $n$ rows of $\mathcal C_n$ have full rational rank,
by the same two parity-Cauchy determinants, now over $\mathbb Q$.
The original full-column-rank theorem also makes every exponent of
$Z$ finite. Let $\nu=v_p(n)$, allowing $p=2$ in this section.
The sign $(-1)^n$ is a unit.

After putting $\mathcal C_n$ in Smith form over $\mathbb Z_p$,
the perturbation remains divisible by $p^\nu$.
Every pivot with exponent $a_i<\nu$ retains that exponent.
Eliminating its off-pivot entries uses coefficients divisible by
$p^{\nu-a_i}$; the resulting correction to the residual block
has valuation at least $2\nu-a_i\ge\nu$.
Induction removes exactly those smaller pivots and leaves a block
all of whose entries are divisible by $p^\nu$. This proves
$\min(e_i,\nu)=\min(a_i,\nu)$ in sorted order.

It also follows by identifying the two matrices over
$\mathbb Z_p/(p^\nu)$ and their finite invariant-factor data.
Neither argument determines an exponent at or above $\nu$.
Equations (13) and (14) follow by summing and then combining primes.
The integer product in (14) is at most $n^n$; the stated
$n\log n$ logarithmic ceiling concerns this specific truncated
divisor, not the actual untruncated content.

The proposed exact Cauchy-product evaluation of the remaining Smith
data is legitimate: a nonzero selected minor must have matching
parity-block sizes, and its valuation is obtained from the two
Cauchy product formulas and the known factor $L^k$. The
Vandermonde and denominator factors, apart from that separately
displayed $L^k$, have magnitude at most $2n$.

## 7. Higher precision and its limitation

For $h>\nu$, the $s$-th nonconstant summand contains the
integer factor $n(s-1)!$. If $s\ge p(h-\nu)+1$, its valuation is
at least


$$
\nu+\lfloor(s-1)/p\rfloor\ge h.
$$


All other factors remain integral, so such summands vanish modulo
$p^h$ without any assumption about cancellation. This proves the
cutoff (15). For $h\le\nu$, the complete congruence (3) already
removes all positive-$s$ summands.

This is an exact finite-level matrix formula, not a stabilization
or an upper bound on eventual Smith depths. The note retains that
distinction, along with the separate primitive-dual endpoint scalar
and unresolved irrationality target.
