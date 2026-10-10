> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 200 — forced Cartier content, normalized common-log gcd, and a local-resultant no-go

Checked: 2026-08-30 (Beijing time)

## 1. Scope and verdict

Retain Item 197's exact integers



$$
C_\nu(m)=[z^{4m+\nu}]
 \frac{(1-z)^{6m}(1+z)^{1+3\nu}}
      {(1+z^2)^{4m+1+\nu}},\qquad \nu=0,1.             \tag{1.1}
$$



This item separates their already forced first Cartier divisor from the
genuinely open second-digit radical.

> **PROVED — the raw gcd has a forced exponential radical.**  Let
> $\mathcal P_m$ be the frozen rank-zero Cartier prime set and put
> 

$$
> F_m=\prod_{p\in\mathcal P_m}p.
>
$$


> Then
> 

$$
>                         \boxed{F_m\mid C_0(m),C_1(m).}           \tag{1.2}
>
$$


> This $F_m$ is exactly the archive's squarefree Cartier product
> $G_m$, not a new content source.  Its $j=0$ subproduct is
> 

$$
> D_m=\prod_{4m+1<p\le6m}p.                                     \tag{1.3}
>
$$


> Along every $m=2^a$, $C_0(m)$ is odd and hence nonzero, while
> 

$$
> \log D_m=2m+o(m).
>
$$


> Consequently neither the nonzero raw gcd nor its radical can have an
> $\exp(o(m))$ upper bound.  This says nothing negative about the
> normalized exceptional radical below.

> **PROVED — the correct normalized target.**  Define the integers
> 

$$
>                    \overline C_\nu(m)=C_\nu(m)/F_m.              \tag{1.4}
>
$$


> If $R_m$ is Item 197's radical of PNT-side common-log rows, then
> 

$$
>                 \boxed{R_m\mid
>                 \gcd(\overline C_0(m),\overline C_1(m)).}        \tag{1.5}
>
$$


> Thus (1.5), not a raw-gcd bound, is the possible route to a
> subexponential theorem.

> **PROVED — exact overlap with the booked ledger.**  Every Item 194 PNT
> row has $p^2>6m$, hence top prime-power layer $q_p=p$, and has
> $p<2m$.  It lies in $\mathcal P_m\cap\mathcal H_m$, where
> $\mathcal H_m$ is Item 149's post-$G_m$ rank-one set.  The forced
> factor $F_m=G_m$ was divided out before $U_m,V_m,c_m$ were defined,
> and Item 149 already books the first post-$G_m$ digit at every such
> prime.  The common-log radical therefore cannot be added as an
> independent reservoir without a separate valuation theorem.

> **PROVED SCOPED NO-GO — two local recurrence rows do not close the
> normalized gate.**  The exact scalar coefficient recurrence has a
> rank-three target matrix with the nonzero kernel
> $\mathbb Z(0,2,2,1)$.  For every Item 194 row the same statement holds
> over $\mathbb Z/p^2\mathbb Z$.  Hence the congruences
> $p\mid\overline C_0,\overline C_1$ leave a genuine projective local
> state; a two-row Casoratian or local resultant is identically unable to
> rule them out.  This does not rule out a global transfer, a larger
> resultant, or a new $p$-adic argument.

> **EXACT FINITE ONLY.**  The replay checks $m\le160$, including 4,787
> forced-prime incidences and 701 PNT-side rows.  It finds no common second
> digit.  No nonoccurrence, density, or asymptotic claim is inferred.

> **OPEN.**  No proof gives
> $\log R_m=o(m)$, and the stronger bound
> $\log\operatorname{rad}\gcd(\overline C_0,\overline C_1)=o(m)$
> is also open.

## 2. The complete forced divisor

For a positive modulus $q$, put



$$
d_q(N,K)=
 \begin{cases}
 2r,&K\equiv0\pmod q,\\
 2r+3(q-t),&K\equiv t\pmod q,\quad1\le t<q,
 \end{cases}
 \quad r\equiv N\pmod q,\quad0\le r<q.              \tag{2.1}
$$



The rank-zero prime set is



$$
\mathcal P_m=\{p\text{ odd prime}:d_p(6m,4m+1)\le p-2,
                  \ d_p(6m,4m+2)\le p-2\}.          \tag{2.2}
$$



To prove (1.2), write $N=ap+r$, $K=bp+t$.  In characteristic
$p$,



$$
\frac{u^N}{Q^K}\,dx=f(x)^pP(x)\,dx,               \tag{2.3}
$$



where $\deg P=d_p(N,K)$.  If this degree is at most $p-2$, then
$P=T'$ in $\mathbb F_p[x]$, and (2.3) is the exact differential
$d(f^pT)$.  Its residue at $-1$ is zero.  Item 197's integral bridge



$$
\operatorname {Res}_{-1}\frac{u^{6m}}{Q^{4m+1+\nu}}dx
 =2^{-2m-1-2\nu}C_\nu(m)                            \tag{2.4}
$$



then gives $p\mid C_\nu(m)$.  Applying this to both $\nu$ proves
(1.2).  The defining set (2.2) is literally the archived definition of
$G_m$, so



$$
\boxed{F_m=G_m}.        \tag{2.5}
$$



There is also an exact row parametrization.  Every $p\in\mathcal P_m$
has unique integers $j\ge0$ and $s$ such that



$$
4m+1=(2j+1)p-2s,qquad
 1\le s\le\frac{p-3}{6},                             \tag{2.6}
$$



and



$$
6m=(3j+1)p+r,qquad r=\frac{p-6s-3}{2}.             \tag{2.7}
$$



Indeed, if $b=\lfloor(4m+1)/p\rfloor$, the two inequalities in
(2.2), together with $3(4m+1)-2(6m)=3$, force $b=2j$ and



$$
d_p(6m,4m+1)=p-3,qquad d_p(6m,4m+2)=p-6.           \tag{2.8}
$$



The case $j=0$ in (2.6) is exactly
$4m+1<p\le6m$, proving (1.3) and $D_m\mid F_m$.

## 3. Why the raw radical cannot be subexponential

Modulo two, $1+z^2=(1+z)^2$.  Therefore (1.1) gives the exact parity
identities



$$
C_0(m)\equiv[z^{4m}](1+z)^{-2m-1}
          \equiv\binom{6m}{4m}\pmod2,               \tag{3.1}
$$





$$
C_1(m)\equiv[z^{4m+1}](1+z)^{-2m}
          \equiv\binom{6m}{4m+1}\equiv0\pmod2.      \tag{3.2}
$$



For $m=2^a$, Lucas' theorem makes $\binom{6m}{4m}$ odd.  Hence the
pair is nonzero on this infinite subsequence.  Since $D_m$ is squarefree
and divides both coordinates,



$$
D_m\mid\operatorname {rad}\gcd(C_0(m),C_1(m))
 \quad(m=2^a).                                        \tag{3.3}
$$



The prime number theorem gives



$$
\log D_m=\vartheta(6m)-\vartheta(4m+1)=2m+o(m).      \tag{3.4}
$$



Equations (3.3)--(3.4) rigorously exclude a raw
$\exp(o(m))$ gcd or radical bound.  They are the reason that every
recurrence or resultant must first remove $F_m$.

## 4. Normalization and exact Item 149 overlap

Because $F_m$ is squarefree, Item 197's equivalence



$$
\ell_{0,0}=\ell_{1,0}=0
 \iff p^2\mid C_0(m),C_1(m)                         \tag{4.1}
$$



becomes, prime by prime for $p\in\mathcal P_m$,



$$
p^2\mid C_0,C_1
 \iff p\mid\overline C_0,\overline C_1.             \tag{4.2}
$$



Multiplication over the exceptional PNT rows proves (1.5).

Now take an Item 194 row, so $j\ge1$ and $3j+1<p$.  Equation (2.7)
has $0\le r<p$, and therefore



$$
6m<(3j+2)p\le p^2.                                  \tag{4.3}
$$



Thus the largest $p$-power at most $4m+1$ is $q_p=p$.  Also



$$
p\le\frac{6m}{3j+1}\le\frac32m<2m.                \tag{4.4}
$$



The degrees (2.8) are at most $2p-2$, so the prime satisfies Item 149's
definition of $\mathcal H_m$.  This proves the exact containment



$$
\boxed{\{\text{Item 194 PNT rows at }m\}
        \subseteq\mathcal P_m\cap\mathcal H_m.}      \tag{4.5}
$$



The bookkeeping consequence is exact.  The first $F_m=G_m$ copy was
removed in forming $U_m,V_m$.  Item 149 then proves one post-$G_m$
copy on $\mathcal H_m$, including every prime in (4.5).  The condition
(4.2) is a further normalized log-row gate on those same primes, not an
independent product that can simply be multiplied into the content ledger.

## 5. Unit audit and the unconditional support ceiling

At PNT scale, (2.6) gives the disjoint intervals



$$
\frac4{2j+1}<\frac pm<\frac6{3j+1},qquad j=0,1,2,\ldots .       \tag{5.1}
$$



Their total length is



$$
\mathfrak C=\sum_{j\ge0}\left(\frac6{3j+1}-\frac4{2j+1}\right)
 =-4\log2+\frac\pi{\sqrt3}+3\log3.                  \tag{5.2}
$$



The $j=0$ interval has length two.  The Item 194 $j\ge1$ cell
therefore has coefficient



$$
c_{\rm even}=\mathfrak C-2
 =-4\log2+\frac\pi{\sqrt3}+3\log3-2
 =0.3370475079987658\ldots                              \tag{5.3}
$$



**per $m$**.  In the normalization used for $\log R_m/(6m)$, the
same ceiling is



$$
\boxed{\frac{c_{\rm even}}6
 =0.0561745846664610\ldots\quad\text{per }6m.}        \tag{5.4}
$$



Thus, without any zero theorem,



$$
\limsup_{m\to\infty}\frac{\log R_m}{6m}
 \le\frac{c_{\rm even}}6.                             \tag{5.5}
$$



The corrected Item 197 record now states both units explicitly.  Its
qualitative conclusion survives: the Cauchy-height ceiling
$0.5273022954534049\ldots$ per $6m$ is still much weaker than (5.4).

## 6. Exact diagonal and four-step recurrence

Put



$$
\phi(z)=\frac{(1-z)^6}{z^4(1+z^2)^4},\qquad
 a_0(z)=\frac{1+z}{1+z^2},\qquad
 a_1(z)=\frac{(1+z)^4}{z(1+z^2)^2}.                  \tag{6.1}
$$



Then



$$
C_\nu(m)=\operatorname {CT}_z a_\nu(z)\phi(z)^m,qquad
 \sum_{m\ge0}C_\nu(m)t^m
 =\operatorname {CT}_z\frac{a_\nu(z)}{1-t\phi(z)}.  \tag{6.2}
$$



This is a bivariate rational diagonal after the standard constant-term
encoding.  Consequently each raw sequence is algebraic, hence P-recursive.
This structural fact alone gives no coefficientwise gcd theorem.

For the local recurrence, define



$$
\sum_{k\ge0}g_{m,k}v^k
 =\frac{(1-v)^{6m}(1-2v)^{6m}}
        {(1-2v+2v^2)^{4m+2}}.                       \tag{6.3}
$$



Exact local substitution at $-1$ gives



$$
C_0=g_{m,4m}-2g_{m,4m-1}+2g_{m,4m-2},\qquad
 C_1=g_{m,4m+1}.                                     \tag{6.4}
$$



Logarithmic differentiation of (6.3) gives, with $g_{m,k}=0$ for
$k<0$,



$$
\begin{aligned}
 -2(k+1)g_{m,k+1}={}&(20m-8-10k)g_{m,k}\\
 &+2(10k+10-20m)g_{m,k-1}\\
 &+4(10m-5k-6)g_{m,k-2}\\
 &+8(k+1-4m)g_{m,k-3}.                              \tag{6.5}
\end{aligned}
$$



The two target rows imply the useful exact identity



$$
\boxed{
 2(4m+1)g_{m,4m}
 =(10m+2)(10m+3)C_0
 -(4m+1)(10m+1)C_1.}                                \tag{6.6}
$$



In particular, on an Item 194 row, a normalized common zero forces
$p^2\mid g_{m,4m}$, since $p\nmid2(4m+1)$.

## 7. The exact local-resultant obstruction

Set $n=4m$ and order the local state as



$$
(x,y,z,w)=(g_{m,n},g_{m,n-1},g_{m,n-2},g_{m,n-3}).  \tag{7.1}
$$



Impose $C_0=C_1=0$ and use recurrence rows $k=n,n-1$.  The resulting
three homogeneous constraints on the state have matrix



$$
M_m=
 \begin{pmatrix}
 1&-2&2&0\\
 -20m-8&40m+20&-40m-24&8\\
 -8m&20m-2&-40m&40m+4
 \end{pmatrix}.                                      \tag{7.2}
$$



They satisfy



$$
M_m(0,2,2,1)^T=0,                                   \tag{7.3}
$$



while the minor in the first three columns is



$$
-16(4m+1).                   \tag{7.4}
$$



Thus $M_m$ has rank exactly three over $\mathbb Q$, and over
$\mathbb Z/p^2\mathbb Z$ whenever $p\nmid2(4m+1)$.  For an admissible
row, $4m+1\equiv-2s\not\equiv0\pmod p$.  Combining this with (4.2)
shows that a normalized common zero leaves exactly the nonzero local line



$$
(x,y,z,w)\equiv\lambda(0,2,2,1)\pmod {p^2}.          \tag{7.5}
$$



This proves a precise no-go: the two adjacent recurrence rows, their
Casoratian, or their local linear resultant cannot prove nonoccurrence of
the normalized common zero.  They have the kernel (7.5) identically, not
merely at exceptional numerical inputs.

A global transfer from $g_{m,0}=1$ could still test whether the actual
state meets (7.5).  The direct forward form of (6.5) divides successively
by $2(k+1)$; clearing it without exploiting cancellations introduces
$2^{4m+1}(4m+1)!$, of logarithmic size $\Theta(m\log m)$.  Therefore
that naive cleared transfer cannot itself yield the desired
$\exp(o(m))$ obstruction.  A cancellation-aware global resultant,
another diagonal representation, or a genuine mod-$p^2$ Frobenius
identity remains possible and is not excluded by this item.

## 8. Deterministic replay and status

The self-contained standard-library checker

`scripts/item200_common_log_gcd_certificate.py`

performs the following exact tasks.

1. It computes (1.1) by a finite binomial sum and independently by
   (6.3)--(6.5).
2. It verifies (1.2), the exact row parametrization (2.6)--(2.8), and
   $D_m\mid F_m$.
3. It checks the exact Item 149 containment (4.5) row by row.
4. It verifies the parity identities, target identity (6.6), matrix kernel
   (7.3), and minor (7.4).
5. It records the finite normalized-gcd and common-second-digit diagnostics
   with a SHA-256 row digest.

The canonical and replay JSON are required to be byte-identical.  The
checker contains no host path, timestamp, elapsed time, floating-point
identity, or external numeric backend.  The manifest uses archive-relative
`sources/`, `scripts/`, and `results/` keys and pins the relevant Items 194,
197, boundary-Cartier, and Item 149 theorem dependencies.

### PROVED

- The full forced divisor $F_m=G_m$, its interval subproduct $D_m$,
  and the raw-radical obstruction along $m=2^a$.
- The normalized bridge (1.5) and exact containment in
  $\mathcal P_m\cap\mathcal H_m$.
- The corrected per-$m$/per-$6m$ capacity units.
- The diagonal, scalar recurrence, target identity, and rank-three local
  kernel.
- The scoped failure of the two-row local resultant.

### EXACT FINITE ONLY

- Every row count, bit size, digest, and common-zero nonoccurrence in the
  canonical replay.

### OPEN

- $\log R_m=o(m)$, or any stronger uniform subexponential bound for the
  normalized gcd/radical.
- A cancellation-aware global recurrence/resultant controlling (7.5).
- A mod-$p^2$ Frobenius, Witt, or equivalent lift that rules out or counts
  the normalized common zeros.
- Any additional Route-1 content rate or conclusion about $e+\pi$.
