> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 189 — the moving-root collision frontier

Checked: 2026-08-30 (Beijing time)

## 1. Scope and verdict

Stay in the Item 174/180 rank-two cell $e=1,\kappa=0$.  For a prime
$p\ge7$, put



$$
Z_p=\left\{0\le s\le N_p:=\left\lfloor{p-1\over3}\right\rfloor:
                 \Delta_{p,s}=0\right\},
 \qquad r_p=|Z_p|.
\tag{1.1}
$$



The desired theorem $r_p=o(p)$ is still open.  The useful new reduction is
that it is enough to control *collisions of root differences*.

> **PROVED — collision-to-root-count theorem.**  Define
> 

$$
> C_p(h)=\#\{s:s,s+h\in Z_p\}.
> \tag{1.2}
>
$$


> If $C_p(h)\le B$ for every $1\le h\le N_p$, then
> 

$$
> r_p\le {1+\sqrt{1+8BN_p}\over2}.
> \tag{1.3}
>
$$


> In particular, a uniform Sidon theorem $C_p(h)\le1$ would prove
> $r_p=O(\sqrt p)$.  A weaker uniform short-shift estimate
> $C_p(h)=O(h)$ for $1\le h<H$, with
> $H\asymp N_p^{1/3}$, would already prove $r_p=O(p^{2/3})$.

This identifies a precise Route-1 frontier rather than assuming the desired
root bound.

> **PROVED — exact shift identities, but growing state.**  The fixed maps
> $H,K$ give exact coefficient relations between levels $s$ and $s+h$.
> Their coefficient windows have width $O(h)$, not bounded width.  Direct
> elimination therefore does not yet prove $C_p(h)\le1$ or $O(h)$.

> **PROVED — bounded-window recurrence obstruction.**  An exact
> characteristic-zero evaluation matrix rules out every scalar recurrence
> of order at most six whose cleared polynomial coefficients have degree at
> most six in the coefficient index $P$ and ten in $s$.  This is a
> rigorous exclusion only inside the displayed ansatz; it is not a theorem
> that no bounded-order recurrence exists.

> **FINITE EXACT EVIDENCE — no asymptotic extrapolation.**  The complete
> scan through $p=5000$ contains 712 roots among 516,374 admissible pairs
> for 666 primes.  Every one of the 666 root sets is Sidon.  Four additional
> complete prime scans at $p=10007,20011,30011,50021$ have respectively
> $2,2,1,0$ roots.  These facts motivate the collision frontier but do not
> prove it.

Nothing here proves the global Route-1 density statement or decides the
arithmetic nature of $e+\pi$.

## 2. The collision theorem

Every unordered pair of distinct roots has one positive difference.  Hence



$$
{r_p\choose2}=\sum_{h=1}^{N_p}C_p(h).
\tag{2.1}
$$



If $C_p(h)\le B$, equation (2.1) gives



$$
{r_p(r_p-1)\over2}\le BN_p,
\tag{2.2}
$$



which is exactly (1.3).  Thus the Sidon property gives



$$
r_p\le {1+\sqrt{1+8N_p}\over2}=O(\sqrt p).
\tag{2.3}
$$



There is also a local version.  Partition $\{0,\ldots,N_p\}$ into
$J=\lceil(N_p+1)/H\rceil$ consecutive blocks of length at most $H$, and
let $u_j$ be the number of roots in the $j$-th block.  Pairs in one block
have difference below $H$, so Cauchy--Schwarz gives



$$
\sum_{h=1}^{H-1}C_p(h)
 \ge\sum_{j=1}^{J}{u_j\choose2}
 \ge {1\over2}\left({r_p^2\over J}-r_p\right).
\tag{2.4}
$$



If $C_p(h)\le C h^\alpha$ for $1\le h<H$, then (2.4) implies



$$
r_p=O_C\left({N_p\over H}+\sqrt{N_pH^\alpha}\right).
\tag{2.5}
$$



Taking $H\asymp N_p^{1/(\alpha+2)}$ yields



$$
r_p=O_C\left(p^{(\alpha+1)/(\alpha+2)}\right).
\tag{2.6}
$$



The case $\alpha=1$ is the advertised $O(p^{2/3})$ route.  These are
unconditional combinatorial implications; the hypotheses on $C_p(h)$
remain open for the determinant.

## 3. What the fixed maps give exactly

Retain Item 185's notation



$$
A_s=A_0H^s,
 \quad A_0={(1-x)^2\over(1-x^4)^2},
 \quad H={(1-x)^5\over(1-x^4)^2},
 \quad K=x^3H.
\tag{3.1}
$$



For every $h\ge0$, direct multiplication gives



$$
(1-x^4)^{2h}A_{s+h}=(1-x)^{5h}A_s.
\tag{3.2}
$$



If $a_n(s)=[x^n]A_s$, coefficient comparison is the exact recurrence



$$
\sum_{q=0}^{2h}(-1)^q{2h\choose q}a_{n-4q}(s+h)
 =\sum_{q=0}^{5h}(-1)^q{5h\choose q}a_{n-q}(s).
\tag{3.3}
$$



Similarly, for $B_s=A_0K^s=x^{3s}A_s$,



$$
\sum_{q=0}^{2h}(-1)^q{2h\choose q}[x^{n-4q}]B_{s+h}
 =\sum_{q=0}^{5h}(-1)^q{5h\choose q}[x^{n-3h-q}]B_s.
\tag{3.4}
$$



Equations (3.3)--(3.4) are genuine all-degree recurrences.  They are not a
bounded-state scalar recurrence for $\Delta_{p,s}$: the windows extend by
up to $8h$ on the left and $5h$ on the right.  Combining them with the
four-term coefficient recurrence of Item 180 replaces the windows by
transfer matrices whose length, degree, and possible pivot set still grow
with $h$.

This was the last direct collision elimination attempted here.  Imposing
$\Delta_{p,s}=\Delta_{p,s+h}=0$ produces two bilinear endpoint conditions,
but eliminating the intervening coefficient states does not leave a
verified nonzero bounded-degree resultant in $(s,h)$.  No sign invariant
survives reduction modulo $p$: Item 180 already gives nonzero negative
integer lifts divisible by $p$.  Therefore this section proves the shift
identities and diagnoses the growing-state obstruction; it does **not**
claim a collision bound.

## 4. Explicit bounded-recurrence test

To distinguish a proved recurrence from a guessed specialized one, define
$\mathcal D(P,s)$ over characteristic zero by the same coefficient formula
as $\Delta_{p,s}$, using the coefficient indices $P-r$ and $P-3s-r$,
but do not reduce modulo the defining prime $P$.

The certificate tests the complete ansatz



$$
\sum_{k=0}^{6}P_k(P,s)\mathcal D(P,s+k)=0,
 \qquad \deg_P P_k\le6,
 \quad \deg_sP_k\le10.
\tag{4.1}
$$



It evaluates (4.1) for every $40\le P\le160$ and every admissible shift,
then reduces the resulting integer matrix modulo the prime $65521$.  The
matrix has shape



$$
3348\times539
\tag{4.2}
$$



and exact rank $539$.  Full rank modulo one prime proves full column rank
over $\mathbb Q$.  Hence no nonzero recurrence (4.1) exists.  Clearing a
rational recurrence's denominators reduces it to this statement only when
the cleared bidegrees remain within the displayed window.

This test does not exclude:

1. higher order or degree;
2. an identity existing only in characteristic $p$;
3. coefficients containing $p$-specific accessory data not rational in
   $(P,s)$.

Indeed, after specializing the defining characteristic, exact linear
algebra at $p=1009$ and $p=2003$ finds a one-dimensional order-three,
degree-ten recurrence space for each finite sequence.  Order two at degree
ten and order three at degree nine both have full rank.  The two normalized
recurrence vectors have different hashes.  This is a finite specialized
fit, not an all-$p$ recurrence theorem.

Most importantly, bounded order alone gives no root-count theorem.  Over an
odd finite field the nonzero period-two sequence $u_s=1-(-1)^s$ satisfies
$u_{s+2}-u_s=0$ and vanishes at half of its indices.  A future recurrence
argument must add a nondegeneracy, monodromy, valuation, or collision
theorem.

## 5. Exact finite collision census

The deterministic vector recurrence was independently cross-checked against
the scalar Item 180 recurrence for every prime through $251$, and its
$p\le2000$ ordered root list agrees entry-for-entry with the frozen
Item 185 data.

For the complete interval $7\le p\le5000$, the exact totals are



$$
\begin{array}{l|r}
\text{primes}&666\\
\text{admissible pairs}&516{,}374\\
\text{zero pairs}&712\\
\text{maximum roots for one prime}&5\\
\text{maximum multiplicity of one positive difference within one prime}&1.
\end{array}
\tag{5.1}
$$



The root-count histogram is



$$
\begin{array}{c|rrrrrr}
r_p&0&1&2&3&4&5\\ \hline
\#p&181&304&143&31&6&1.
\end{array}
\tag{5.2}
$$



Thus every finite root set in this range is Sidon.  The ordered root-list
digest is

```text
2460e06779742aecd53f4e38723aa59ce099a48b1a5ade4bfb1edee21666541e
```

The additional complete-prime spot checks are



$$
\begin{array}{c|l}
p& s\text{-roots}\\ \hline
10007&1743,2001\\
20011&4002,6669\\
30011&6002\\
50021&\varnothing.
\end{array}
\tag{5.3}
$$



No linear root population appears in these tests.  Equations (5.1)--(5.3)
are exact finite evidence only.  In particular, “all scanned sets are
Sidon” is not extrapolated to unscanned primes.

## 6. Route scope

If the Sidon property were proved uniformly, (2.3) would close the
$r_p=o(p)$ adversary lemma for the Item 174/180 $\kappa=0$, rank-two
moving determinant.  Item 180's transference theorem would then give the
corresponding mean zero-mass conclusion.

That would still not prove:

- nonvanishing of every moving determinant;
- a pointwise density theorem for every $m$;
- the other Route-1 cells or mechanisms;
- Route 2;
- irrationality or any arithmetic classification of $e+\pi$.

The precise open frontier left by this item is therefore



$$
\boxed{\text{prove }C_p(h)\le1,
 \quad\text{or at least }C_p(h)=O(h)
 \text{ on a long short-shift range}.}
\tag{6.1}
$$



## 7. Reproduction

The certificate uses exact integer and finite-field arithmetic.  NumPy is
used only to batch independent modular recurrences and row operations in
signed 64-bit arrays; the certified prime range is capped so every
intermediate product stays within that exact range.  The runtime dependency
and frozen Item 185 JSON hash are recorded in the canonical output.  The
frozen canonical/replay pair used bundled CPython 3.12.13 with NumPy 2.3.5.

From `work/`, the default output is beside the script.  From archived
`scripts/`, it is written to the sibling `results/` directory.

```powershell
$python = Join-Path $env:USERPROFILE `
  '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $python work/item189_collision_route_certificate.py `
  --scan-limit 5000 `
  --large-primes 10007 20011 30011 50021 `
  --output work/item189_collision_route_certificate_replay.json
```

Status separation:

- **PROVED:** collision lemmas (2.1)--(2.6), shift identities
  (3.2)--(3.4), and the finite-dimensional full-rank obstruction
  (4.1)--(4.2).
- **FINITE EXACT ONLY:** the Sidon census, large-prime spot checks, and
  specialized recurrence fits.
- **OPEN:** every unconditional sublinear bound for $r_p$, including the
  Sidon and $O(h)$-collision statements.
