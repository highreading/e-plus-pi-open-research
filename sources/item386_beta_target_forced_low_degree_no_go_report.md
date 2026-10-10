> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 386 — target-free low-degree beta conics and exact gcd-overlap closure

Checked: 2026-09-01 (Beijing time)

## 1. Verdict and strategic scope

Assume the genuine Item-316 target and retain Item 358's externally
$t$-saturated singleton-squarefree carrier $\mathcal U_{1,1}$.  Items
373--381 classify the first low-degree cancellation varieties in the top
symmetric load coordinates, but Item 381 deliberately does not construct a
polynomial forced by the actual target.  This item determines that logical
bridge.

The answer is negative in the strongest formal sense available from the
endpoint algebra.

> **TARGET-SINGLETON FREEDOM THEOREM.**  Fix an exact-zero stratum, a sign
> chamber, and a prime $p\mid b$.  After imposing the exact Item-316
> endpoint modulo $p$, every retained signed load remains an independent
> coordinate.  After additionally imposing a singleton hit at any retained
> row and inverting every outside load, the outside load vector ranges over
> the complete torus $(\mathbb F_p^\times)^{N-1}$.

Consequently no nonzero prime-independent rational split line, binary
Pell/norm form, or ternary conic from Item 381 is a formal consequence of
the Item-316 target plus singleton incidence.  More generally, if
$F_n(T_1,\ldots,T_k)$ is a primitive homogeneous form of degree $d$,
then its singleton-chart restriction is a nonzero torus polynomial.  If



$$
d(k-1)<p-1,
\tag{1.1}
$$



it does not even vanish as a function on the complete formal target
singleton torus.  Every linear or quadratic form in $T_1,T_2,T_3$
satisfies (1.1) for the tied primes $p>A$.

There is also one unconditional actual-family capacity closure.  Put



$$
G_k=\gcd(T_1,\ldots,T_k).
\tag{1.2}
$$



At every actual singleton prime, $T_1$ is a unit.  Therefore



$$
\boxed{
\gcd(\mathcal U_{1,1},G_k)=1,
\qquad
\log\gcd(\mathcal U_{1,1},G_k)=0.}
\tag{1.3}
$$



Thus the coordinate-gcd statistics $g_{12}$ and $g_{123}$ listed in
Item 381 have exactly zero overlap with the missing singleton mass.  They may
remain useful as archimedean factors in a norm lower bound, but they cannot
be singleton carriers.

This globally closes the entire Item-381 low-degree menu as a
**target-forced** mechanism: its gcd part has zero actual overlap, while its
split-line, primitive-norm, and conic parts require an additional accidental
correlation at the unique canonical point.  No such correlation follows
from Item 316 or the load recurrences.

The theorem does not prove that the unique actual point avoids every moving
form.  Hence it does not prove
$\log\mathcal U_{1,1}=o(\log b)$, does not reduce $\Gamma_Q$, and books
no mass.  Its strategic effect is to remove low-degree conic classification
from the list of target-generated carriers: further work must first supply
an independently proved actual-point divisibility theorem.

## 2. Endpoint load coordinates

Retain



$$
A=4n-2,
\qquad m=n-2,
\qquad
w_1=7,
\qquad
w_j=4j+2\ (2\le j\le m),
\qquad
w_{m+1}=A.
\tag{2.1}
$$



Let $d_1,\ldots,d_m$ be formal digits and use Item 365's signed loads



$$
X_j=w_jd_{j-1}-d_j
\qquad(3\le j\le m).
\tag{2.2}
$$



They form an integral triangular coordinate system:



$$
\mathbb Z[d_1,\ldots,d_m]
=\mathbb Z[d_1,d_2,X_3,\ldots,X_m].
\tag{2.3}
$$



Indeed, $d_j=w_jd_{j-1}-X_j$ reconstructs all later digits from
$d_2,X_3,\ldots,X_j$.

Let



$$
\Delta_\sigma=\sigma E_{m+1}-a
\tag{2.4}
$$



be the exact endpoint defect in a fixed sign chamber.  The coefficient of
$d_1$ in $E_{m+1}$ is



$$
C_n=K(w_2,\ldots,w_m,A).
\tag{2.5}
$$



The appended-tail bridge is



$$
aC_n=bS+(-1)^n,
\tag{2.6}
$$



so



$$
\gcd(C_n,b)=1.
\tag{2.7}
$$



For every $p\mid b$, $\sigma C_n$ is therefore a unit modulo every
power of $p$.  Solving (2.4) for $d_1$ gives Item 365's exact coordinate
isomorphism



$$
\boxed{
\frac{(\mathbb Z/p^r\mathbb Z)
[d_1,d_2,X_3,\ldots,X_m]}{(\Delta_\sigma)}
\cong
(\mathbb Z/p^r\mathbb Z)[d_2,X_3,\ldots,X_m].}
\tag{2.8}
$$



This is the key target-forcing audit.  The endpoint consumes $d_1$, not
one of the row loads.  Thus no polynomial relation among the retained loads
is supplied by the target.

Fix an exact-zero stratum and relabel its retained loads
$X_1,\ldots,X_N$.  On a fixed actual sign chamber, the positive load is
$Z_i=\eta_iX_i$ with $\eta_i\in\{\pm1\}$.  Multiplication by the fixed
units $\eta_i$ does not change (2.8).  On the singleton chart at row
$r$, impose



$$
Z_r=0,
\qquad
Z_i\ne0\quad(i\ne r),
\tag{2.9}
$$



and localize at the outside loads and the already external $t$-coordinate.
Equation (2.8) proves that the outside vector ranges over the full torus



$$
\boxed{(Z_i)_{i\ne r}\in(\mathbb F_p^\times)^{N-1}.}
\tag{2.10}
$$



This statement includes genuine earlier- and later-row avoidance at the
formal singleton chart.  It is not a selected-hit relaxation.

## 3. Top-symmetric chart and algebraic independence

For $1\le s\le N-1$, put



$$
T_s=e_{N-s}(Z_1,\ldots,Z_N).
\tag{3.1}
$$



On the singleton chart, let $L=N-1$ and write the outside loads as
$z_1,\ldots,z_L$.  Then



$$
T_s=e_{L+1-s}(z_1,\ldots,z_L),
\qquad
T_1=\prod_{i=1}^{L}z_i\ne0.
\tag{3.2}
$$



With $y_i=z_i^{-1}$, the exact projective coordinates are



$$
\boxed{
\frac{T_s}{T_1}=e_{s-1}(y_1,\ldots,y_L)
\qquad(2\le s\le N-1).}
\tag{3.3}
$$



The elementary symmetric polynomials
$e_1(y),\ldots,e_L(y)$ are algebraically independent over every field.
Hence every initial subset



$$
e_1(y),\ldots,e_{k-1}(y)
\tag{3.4}
$$



is algebraically independent.  Therefore the homomorphism



$$
\mathbb F_p[U_2,\ldots,U_k]
\longrightarrow
\mathbb F_p[y_1^{\pm1},\ldots,y_L^{\pm1}],
\qquad
U_s\longmapsto e_{s-1}(y),
\tag{3.5}
$$



is injective for $k\le N$.

Let $F(T_1,\ldots,T_k)$ be a nonzero homogeneous form of degree $d$.
Because $T_1$ is a unit on the chart,



$$
F(T_1,\ldots,T_k)
=T_1^dF(1,e_1(y),\ldots,e_{k-1}(y)).
\tag{3.6}
$$



Injectivity of (3.5) shows that the second factor is a nonzero polynomial.
Its total degree is at most



$$
d(k-1).
\tag{3.7}
$$



If (1.1) holds, this degree is below $p-1$.  A nonzero polynomial of
total degree below $p-1$ cannot vanish on all of
$(\mathbb F_p^\times)^L$: induct on $L$, using that a nonzero
univariate polynomial of degree below $p-1$ has fewer than $p-1$
nonzero roots.  This proves the function-level part of the theorem.

For the actual tied range $p>A=4n-2$, every linear or quadratic form in
the first three top coordinates has



$$
d(k-1)\le4<p-1.
\tag{3.8}
$$



Thus no nonzero primitive reduction of any Item-381 split line, binary
quadratic, or ternary quadratic vanishes on the complete formal
target-singleton torus.

## 4. Exact closure of the coordinate-gcd branch

Let $p\mid\mathcal U_{1,1}$, and let $r=r(p)$ be its unique actual hit
row.  Since the outside loads are $p$-units,



$$
T_1=e_{N-1}(Z)
\equiv\prod_{i\ne r}Z_i\not\equiv0\pmod p.
\tag{4.1}
$$



Therefore $p\nmid G_k$ for every $k\ge1$.  The carrier
$\mathcal U_{1,1}$ is squarefree, so multiplying (4.1) over all its primes
proves (1.3).

In particular,



$$
\boxed{
\gcd(\mathcal U_{1,1},g_{12})
=\gcd(\mathcal U_{1,1},g_{123})=1.}
\tag{4.2}
$$



This is stronger than a zero-rate estimate: the weighted overlap is
identically zero on every actual target.

For a binary primitive normalization



$$
T_1=g_{12}q,
\qquad T_2=g_{12}r,
\qquad\gcd(q,r)=1,
\tag{4.3}
$$



the same theorem gives $q\in\mathbb F_p^\times$ and



$$
\frac rq\equiv\frac{T_2}{T_1}
=\sum_{i\ne r(p)}Z_i^{-1}\pmod p.
\tag{4.4}
$$



Thus a primitive Pell/norm factor $Q(q,r)$ captures $p$ only if the
actual moving sum in (4.4) happens to lie on the corresponding root locus.
Section 3 proves that this is not forced by the target chart.

Similarly, after division by $g_{123}$, a ternary conic condition reduces
modulo $p$ to



$$
Q(1,e_1(y),e_2(y))=0.
\tag{4.5}
$$



This nonzero degree-at-most-four polynomial is not identically zero on the
formal target torus.  Rational isotropy at the unique actual point would be
a new arithmetic coincidence, not inherited Item-316 structure.

## 5. What has and has not been removed

The Item-381 survivor list now separates exactly as follows.

| Statistic | Actual or formal decision |
|---|---|
| $g_{12},g_{123}$ | exact actual overlap with $\mathcal U_{1,1}$ is zero |
| rational split line | not formally forced by Item 316 plus singleton incidence |
| primitive binary Pell/norm value | not formally forced; requires the actual ratio correlation (4.4) |
| indefinite ternary conic/isotropy | not formally forced; requires the actual-point correlation (4.5) |

Accordingly, none of these objects is an admitted target-generated carrier.
A successful continuation must first construct a prime-independent nonzero
integer $H_n$ and prove an actual-family implication such as



$$
\mathcal U_{1,1}\mid H_n,
\qquad
0<|H_n|=b^{o(1)},
\tag{5.1}
$$



or prove a strict weighted version.  Merely choosing a moving split line or
conic through the unique actual point is circular; its coefficients encode
the point and provide no independent height bound.

The formal freedom theorem cannot exclude a correlation holding only at the
unique canonical word.  Item 365 proves that this actual orbit has rank at
most one, so Zariski freedom of the ambient target chart is not a
distribution theorem for that point.  Consequently



$$
\boxed{
\Delta\log\mathcal U_{1,1}=0,
\qquad
\Delta\Gamma_Q=0,
\qquad
\Delta r_1=0.}
\tag{5.2}
$$



The equality in (5.2) means no ledger change, not that the unresolved
quantities vanish.

## 6. Strict labels

### PROVED

* The target-singleton freedom theorem (2.8)--(2.10).
* The exact projective chart (3.2)--(3.3).
* Algebraic injectivity of every fixed top-symmetric projective coordinate
  set (3.5).
* The finite-field torus nonvanishing theorem under (1.1).
* Exact coprimality (1.3) and (4.2) for all coordinate-gcd statistics.
* The target-forcing decisions for split lines, primitive binary norms, and
  ternary conics.
* Zero booking.

### PROVED GLOBAL SCOPED NO-GO

* No nonzero prime-independent homogeneous linear or quadratic relation in
  $T_1,T_2,T_3$ is forced by the Item-316 endpoint and singleton incidence.
* The statement holds at arbitrary homogeneous degree whenever
  $d(k-1)<p-1$.
* Coordinate gcds have identically zero actual overlap with
  $\mathcal U_{1,1}$.
* Hence the complete Item-381 low-degree list has zero incremental capacity
  as a target-forced mechanism.

### EXACT FINITE ONLY

* The deterministic replay's declared recurrence, endpoint-unit,
  coordinate-reconstruction, singleton-chart, symmetric-ratio, and gcd
  controls.
* Its residue points are formal algebraic controls, not actual Item-316
  targets and not a prime-density census.

### OPEN

* An accidental correlation at the unique actual canonical point satisfying
  (5.1), or a weighted substitute.
* The full singleton and growing low-incidence bounds.
* $\Xi_Q$, squarefull excess, $H_Q$, $K_Q$, and $\Gamma_Q$.
* The centered half-bound, beta capacity, Route 1, and $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{6.1}
$$



No canonical, master, status, checkpoint, research-log, or root-audit file is
edited by this work package.

## 7. Deterministic replay

From the archive root:

~~~text
python work/item386_beta_target_forced_low_degree_no_go_certificate.py ^
  --output work/item386_beta_target_forced_low_degree_no_go_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer or
finite-field arithmetic.  It performs no target search, prime census,
factor search, or half-bound scan.

