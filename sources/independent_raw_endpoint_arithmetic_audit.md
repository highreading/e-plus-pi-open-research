> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the raw-arctangent endpoint arithmetic

Date: 2026-08-26 UTC

## Verdict

**ACCEPT.**  I found no mathematical, normalization, implementation, or
archival error in
`sources/raw_arctan_endpoint_arithmetic.md`, its generator, or its archived
degree-$30$ result.  The determinant scaling in Theorem 2.1 agrees exactly
with `sources/raw_arctan_bordered_rank_proof.md`; the cofactor and primitive
gcd formulas have the correct factorial factors; the Hadamard constant in
the displayed height bound is valid; and the augmented-determinant identity
for the first unconstrained coefficient is correct.

The acceptance is deliberately limited to what the source note claims.  The
formula for $\nu_2(\Delta_{B,n})$ is an all-degree theorem conditional only on
the accepted bordered-rank proof.  The displayed pattern for
$\nu_2(\beta_n)$ and the nonvanishing of the first unconstrained coefficient
are finite statements through $n=30$, not all-degree theorems.

The audited input hashes were

```text
acac24cea15e633f78ccfed584301fd67e5e462eb046db1d5f95db0102b4fce9  sources/raw_arctan_endpoint_arithmetic.md
b52e0aa858ac5e7ee63c6b4c291127348b0ea951cc3fb9ee42242ea0677b0084  sources/raw_arctan_bordered_rank_proof.md
122f36869da34d6e5a7dd3631c775357829dd9ee71e79653c75a46c69c9a96ba  scripts/raw_arctan_endpoint_arithmetic.py
9435f5cffa4ad39ec719378b5ed5a567f9369001474c74c9e8fc8f45327f2db5  results/raw_arctan_endpoint_arithmetic_n30.json
```

## 1. Index translation and determinant scaling

The endpoint note uses degree $n$ and puts $m=n+1$.  The bordered-rank proof
uses polynomial degree less than $m$ and then puts $\ell=m-1$.  Thus its
square matrix $T_\ell$ is exactly $T_n$ in the endpoint note, with the same
row set

$$
\{\ell+1,\ldots,3\ell\}=\{n+1,\ldots,3n\}.
$$

For each jet index $k$, the integral row of $J_n$ is $k!$ times the
coefficient row.  Hence dividing the $2n$ jet rows contributes exactly

$$
\prod_{k=n+1}^{3n}k!
$$

to the determinant when one returns to the integral matrix.

The coordinate change used in the endpoint note is genuinely unimodular.
Writing $\widetilde B(z)=\sum_{j=0}^{n-1}\widetilde b_jz^j$ gives

$$
b_0=x-\widetilde b_0,
\qquad
b_j=\widetilde b_{j-1}-\widetilde b_j\ (1\le j<n),
\qquad
b_n=\widetilde b_{n-1},
$$

and the analogous formulas hold for $C$.  Each transformation matrix has
determinant $\pm1$.  In the new endpoint columns, the last two rows are
$y-4x$ and $x$, whose $2$-by-$2$ pivot determinant is also $\pm1$.
Eliminating those columns leaves the normalized coefficient matrix $T_n$.
Consequently the exact scaling needed for valuations is

$$
\Delta_{B,n}
=\pm\left(\prod_{k=n+1}^{3n}k!\right)\det T_n.       \tag{A1}
$$

This proves equation (16) of the endpoint note.  The separately treated
case $n=0$ is also correct: the determinant of the border row and $u_B$ is
$-1$, so its $2$-adic valuation is zero.

As an independent finite check, I built both matrices directly from their
definitions.  For every $0\le n\le13$, the quotient of the two sides of
(A1), without the sign, was exactly $1$ in absolute value.  With the stated
row and column ordering the observed sign was $(-1)^{n+1}$.

## 2. Exact $2$-adic formula

The notation in the two source notes matches as follows:

$$
A(q)=S(q),\qquad g(q)=G(q),\qquad \beta(q)=H(q).
$$

The last equality is exact, including parity.  If $h=q-1$, the parity term
in the rank proof is $h$ for even $h$ and $h+1$ for odd $h$, which is

$$
(q-1)+\mathbf 1_{2\mid q}.
$$

For even $n=2r$, the unique least-valuation term in the rank proof is the
$S_0$ term.  Its valuation gives

$$
\nu_2(\det T_n)
=S(n)-\sum_{k=2n+1}^{3n}\nu_2(k!)
  +3G(r)+H(r+1).                                  \tag{A2}
$$

For odd $n=2r+1$, it is the $S_*$ term.  The factorial sum for $S_*$ equals
that for $S_0$, because
$\nu_2((2n)!)=\nu_2((2n+1)!)$, and its extra Vandermonde term is
$\nu_2(n)=0$ because $n$ is odd.  Therefore

$$
\nu_2(\det T_n)
=S(n)-\sum_{k=2n+1}^{3n}\nu_2(k!)
  +2G(r+1)+G(r)+H(r+1).                           \tag{A3}
$$

Adding the jet-row contribution in (A1) cancels precisely the range
$2n+1,\ldots,3n$, leaving the ranges and formulas in equations (11) and
(12) of the endpoint note.  No factorial range, parity term, or exceptional
$n=0$ term is missing.

I recomputed $\Delta_{B,n}$ as an integer determinant, independently of the
archived script's closed formula, through $n=16$.  The direct valuations
agreed with Theorem 2.1 in all 17 cases.  The last four new adversarial test
values were

| $n$ | direct $\nu_2(\Delta_{B,n})$ | Theorem 2.1 |
|---:|---:|---:|
| 13 | 399 | 399 |
| 14 | 468 | 468 |
| 15 | 541 | 541 |
| 16 | 616 | 616 |

The leading-order statement $D_n=3n^2+O(n\log n)$ is also consistent: the
factorial range contributes $3n^2/2+O(n\log n)$, $S(n)$ contributes
$n^2/2+O(n\log n)$, and the $G,H$ block contributes
$n^2+O(n\log n)$.

## 3. Cofactor ratios and primitive normalization

For any full-row-rank $(N-1)$-by-$N$ matrix $J$, the signed maximal-minor
vector $w$ spans $\ker J$, and an appended row $u$ satisfies

$$
\det\begin{pmatrix}J\\u\end{pmatrix}=u(w)
$$

up to the one fixed sign convention used for every appended row.  Ratios
therefore have no sign ambiguity.  In this problem,

$$
u_B(w)=B(1),\qquad
u_A(w)=n!A(1),\qquad
u_M(w)=M!q_{M,n}.
$$

It follows exactly that

$$
\frac{A(1)}{B(1)}
=\frac{\Delta_{A,n}}{n!\Delta_{B,n}},
\qquad
\frac{q_{M,n}}{B(1)}
=\frac{\Delta_{M,n}}{M!\Delta_{B,n}}.             \tag{A4}
$$

The integral row $u_A$ is scaled correctly.  Its $B$ coordinates are
$-n!\sum_{r=0}^{n-j}1/r!$, and its $C$ coordinates are
$-n!\sum t_r$ over the same range.  The first are integral because
$r!\mid n!$, and the second because each odd denominator $r\le n$ divides
$n!$.

Since Proposition 2.1 of the endpoint-remainder note proves $B(1)\ne0$,
the pair $(\Delta_{A,n},n!\Delta_{B,n})$ is a nonzero integral
representative of the endpoint ratio.  Dividing it by

$$
h_n=\gcd(|\Delta_{A,n}|,n!|\Delta_{B,n}|)
$$

therefore gives the primitive endpoint pair, up to one common sign.  For a
prime $p$,

$$
\nu_p(\beta_n)
=\nu_p(n!\Delta_{B,n})
 -\min\{\nu_p(\Delta_{A,n}),\nu_p(n!\Delta_{B,n})\},
$$

which is exactly equation (27), including the convention
$\nu_p(0)=+\infty$.

For $0\le n\le13$, I independently formed the signed maximal-minor vector
from all $2n+2$ deleted-column determinants, checked $J_nw=0$, recovered
$A$ from the low Taylor equations, and compared primitive pairs.  In every
case the endpoint pair obtained directly was the same, up to sign, as the
pair obtained from $(\Delta_A,n!\Delta_B)$.  Both identities in (A4) also
held exactly.  Thus no small-degree counterexample was found to the cofactor,
factorial-scaling, or gcd-normalization claims.

The table's values of $\nu_2(\Delta_A)$ beyond the direct determinant range
are legitimate derived values, not claimed direct determinants.  For
example, at $n=18$,

$$
\nu_2(18!\Delta_B)=16+806=822,
\qquad
\nu_2(\beta_{18})=28,
$$

so equation (27) gives $\nu_2(\Delta_A)=794$, as printed.

## 4. Hadamard height constant

Put $m=n+1$ and
$R_k=\max\{k^n,k!\}$.  Every high-jet row has Euclidean norm at most

$$
\sqrt{2m}\,R_k.
$$

Indeed, its $B$ entries satisfy $(k)_a\le k^n$, and a nonzero $C$ entry is

$$
(k)_a|\tau_{k-a}|=\frac{k!}{k-a}\le k!.
$$

The border and endpoint rows satisfy

$$
\|(-4,\ldots,-4\mid1,\ldots,1)\|_2=\sqrt{17m},
\qquad
\|u_B\|_2=\sqrt m,
$$

and

$$
\|u_A\|_2
\le n!\sqrt{m(9+\mathcal H_n^2)}
\le \sqrt{2m}\,n!(3+\mathcal H_n).
$$

There are $2n$ high rows, so Hadamard gives the two separate bounds

$$
n!|\Delta_B|
\le \sqrt{17}\,m n!(2m)^n\prod_{k=n+1}^{3n}R_k,
$$

$$
|\Delta_A|
\le \sqrt{34}\,m n!(3+\mathcal H_n)(2m)^n
       \prod_{k=n+1}^{3n}R_k.
$$

The second right-hand side dominates the first and, since $h_n\ge1$,
proves equation (29) exactly as stated.  The factor $\sqrt{34}$, the single
factor $m$, the factor $(2m)^n$, and the outside $n!$ are all accounted for.
I also evaluated the determinant inequalities directly for $0\le n\le13$;
none failed.

## 5. The $\Delta_M$ identity and its logical scope

For $M=3n+1>n$, the polynomial $A$ has no $z^M$ coefficient.  The row
$u_M$ is exactly $M!$ times the coefficient functional

$$
q_{M,n}=[z^M](Be^z+C\arctan z).
$$

The second identity in (A4) follows from the same cofactor vector, and
$B(1)\Delta_{B,n}\ne0$ makes

$$
q_{M,n}\ne0\quad\Longleftrightarrow\quad\Delta_{M,n}\ne0
$$

valid.  The source note correctly warns that full row rank of $J_n$ does not
imply this augmented determinant is nonzero.  An appended row may lie in the
row span even when $J_n$ has full row rank.  The finite nonvanishing test is
therefore not being promoted to an all-degree conclusion.

The independently constructed cofactor vectors and coefficient rows verified
the $\Delta_M$ ratio for every $0\le n\le13$, three degrees beyond the
archived direct-determinant range.

## 6. Reproduction and certificate audit

I reran

```text
python scripts/raw_arctan_endpoint_arithmetic.py \
  --max-n 30 --determinant-check-through 10 --output REGENERATED.json
```

The regenerated file had SHA-256

```text
9435f5cffa4ad39ec719378b5ed5a567f9369001474c74c9e8fc8f45327f2db5
```

and was byte-for-byte identical to
`results/raw_arctan_endpoint_arithmetic_n30.json`.

The JSON contains exactly 31 consecutive records, $n=0,1,\ldots,30$.
Every record reports both

```text
primitive_endpoint_B_matches_observed_pattern = true
first_unconstrained_coefficient_nonzero = true
```

and exactly the 11 records $0\le n\le10$ contain the advertised direct
determinant cross-check block.  The generator uses exact SymPy rationals and
integer determinants; no floating-point comparison enters any certified
claim.

## 7. Residual caveats

1. Theorem 2.1 inherits the bordered-rank proof's unique least-$2$-adic-term
   argument.  This audit checked the index translation, equality cases,
   parity terms, determinant scaling, and small-degree consequences; it found
   no discrepancy in that dependency.
2. No all-degree formula for $\nu_2(\Delta_A)$ is proved.  Accordingly, the
   large all-degree valuation of $\Delta_B$ cannot be interpreted as a large
   valuation of the primitive coefficient $\beta_n$.
3. The formula
   $\nu_2(\beta_n)=n+2\lfloor(n+2)/4\rfloor$ and the nonvanishing of
   $q_{M,n}$ remain finite observations through degree $30$ only.
4. The height bound is rigorous but intentionally coarse, of size
   $\exp(O(n^2\log n))$.  It does not prove endpoint decay, irrationality, or
   transcendence of $e+\pi$.

Subject to those explicitly stated limitations, the endpoint-arithmetic note,
script, and archived result are accepted.
