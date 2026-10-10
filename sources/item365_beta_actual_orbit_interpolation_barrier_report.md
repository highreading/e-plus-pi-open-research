> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 365 — endpoint freeness and the actual-orbit interpolation barrier

Checked: 2026-09-01 (Beijing time)

## 1. Strict verdict and capacity admission

Assume the genuine canonical Item-316 target.  Retain



$$
A=4n-2,
\qquad m=n-2,
\qquad a=q_{n-1},\quad b=q_n,\quad c=q_{n-2},
\tag{1.1}
$$



the sign chamber $\sigma\in\{\pm1\}$, and the endpoint defect



$$
\Delta_\sigma=\sigma E_{m+1}-a.
\tag{1.2}
$$



Let $\mathcal U_{1,1}$ be Item 358's actual $t$-avoiding,
singleton-squarefree carrier.  Its admission ceiling remains



$$
0\le\log\mathcal U_{1,1}\le\log Q\le\log b.
\tag{1.3}
$$



For a target-specific cancellation to change this capacity, it must produce
a candidate-independent nonzero integer $H_n$ such that



$$
\mathcal U_{1,1}\mid H_n,
\qquad
\log|H_n|=o(\log b)
\tag{1.4}
$$



for zero rate, or at least a strict sub-one-copy height for a quantitative
gain.  A polynomial which is merely zero modulo each candidate prime, whose
coefficients depend on that same prime, does not pass this admission test.

Item 365 reaches a two-part decision.

1. **Endpoint equality alone does not lower the externally $t$-saturated
   row-only singleton degree.**  In integral load coordinates the coefficient
   of $d_1$ in $\Delta_\sigma$ is a unit modulo every prime dividing $b$.
   Hence the endpoint target leaves every row load freely variable, even
   after a fixed exact-zero stratification.
2. **The canonical box and the actual orbit do collapse degree, but not in
   an admissible way.**  Tensor interpolation on the digit box gives a
   $p$-dependent representative of total degree $O(n^2)$.  At fixed $n$,
   however, the genuine actual target orbit is empty or a single canonical
   word, so the singleton indicator has the trivial degree-zero
   representative zero at a hit.  The quotient is likewise only a
   candidate-dependent scalar.  Neither construction supplies (1.4).

Thus endpoint-only cancellation for the row-only carrier is closed, while a
cancellation which essentially mixes the internal $t$-coordinate with the
canonical box, and uniform cross-$n$, cross-prime height compression, remain
open.  The actual orbit is too small for a Zariski-density or
interpolation-injectivity lower bound.  Booking is zero.

## 2. Integral load coordinates and the endpoint unit

Use Item 350's signed loads



$$
x_j=w_jd_{j-1}-d_j
\qquad(3\le j\le m).
\tag{2.1}
$$



They give the integral triangular coordinate system



$$
\mathbb Z[d_1,\ldots,d_m]
=\mathbb Z[d_1,d_2,x_3,\ldots,x_m].
\tag{2.2}
$$



Let



$$
S=P_m,
\qquad
\widehat\Delta_0=K(w_2,\ldots,w_m,A).
\tag{2.3}
$$



The coefficient of $d_1$ in $E_{m+1}$ is
$\widehat\Delta_0$.  This follows either from the prefix recurrence or by
reading the $i=0$ coefficient in Item 316's appended signed sum.  The
appended-tail bridge is



$$
\boxed{
a\widehat\Delta_0=bS+(-1)^n.}
\tag{2.4}
$$



Since $\gcd(a,b)=1$, (2.4) gives



$$
\boxed{\gcd(\widehat\Delta_0,b)=1.}
\tag{2.5}
$$



The later digits $d_j$, $j\ge2$, are reconstructed from $d_2$ and the
loads and contain no $d_1$.  Therefore, in the load coordinate ring,



$$
[d_1]\Delta_\sigma=\sigma\widehat\Delta_0.
\tag{2.6}
$$



For every prime $p\mid b$ and every $r\ge1$, this coefficient is a unit
modulo $p^r$.  Solving for $d_1$ gives the exact all-power coordinate theorem



$$
\boxed{
\frac{(\mathbb Z/p^r\mathbb Z)
[d_1,d_2,x_3,\ldots,x_m]}{(\Delta_\sigma)}
\cong
(\mathbb Z/p^r\mathbb Z)[d_2,x_3,\ldots,x_m].}
\tag{2.7}
$$



No factorization of $b$ or division by a moving nonunit is used.  Equation
(2.7) strengthens the endpoint part of Item 333 in precisely the load chart
needed here: every row load survives as a free coordinate.

## 3. Endpoint-only singleton degree survives every exact-zero stratum

Fix an exact-zero stratum.  Let $\mathcal J\subseteq\{3,\ldots,m\}$ be
the retained nonzero integer rows and put $N=|\mathcal J|$.  If $N=0$,
the singleton carrier is $1$ and the branch is trivial, so assume $N\ge1$.
Algebraically,
set $x_i=0$ for $i\notin\mathcal J$ and omit those rows from the incidence
indicator.  Reducing (2.7) modulo $p$ gives



$$
\boxed{
\frac{\mathbb F_p[d_1,d_2,x_3,\ldots,x_m]}
{(\Delta_\sigma,x_i:i\notin\mathcal J)}
\cong
\mathbb F_p[d_2,x_j:j\in\mathcal J].}
\tag{3.1}
$$



Thus Item 362's row-only singleton complement is still a function of $N$
independent field coordinates.  Its minimal reduced total degree on the
endpoint target is exactly



$$
\boxed{
D_{p,N}^{\rm end}
=
\begin{cases}
N(p-1),&p\nmid N,\\
(N-1)(p-1),&p\mid N.
\end{cases}}
\tag{3.2}
$$



In particular,



$$
D_{p,N}^{\rm end}\ge(N-1)(p-1).
\tag{3.3}
$$



On the actual Item-316 word,
$N\le m-2=n-4<p$.  Therefore only the first branch of (3.2) occurs in
the tied range, and its exact degree is $N(p-1)$.  The $p\mid N$ branch is
retained solely to state the complete ambient finite-field theorem.

If the fresh singleton mass had positive beta rate, Item 346 implies
$N=\Omega(n)$, while $p>A$ gives $p-1\ge A=\Omega(n)$.  Hence the endpoint
degree remains $\Omega(n^2)$.  The exact endpoint equality and exact-zero
stratification therefore cannot provide a cancellation of Item 362's
row-only carrier after Item 358 has already imposed $p\nmid t$ externally.

This theorem still concerns the formal endpoint target.  Canonical digit
bounds are not polynomial equations and are analyzed separately next.

## 4. The canonical box admits lower-degree interpolation

The rectangular digit box is



$$
\mathcal B_m
=\{0,\ldots,6\}
\times\prod_{i=2}^{m}\{0,\ldots,w_i\}.
\tag{4.1}
$$



Every tied prime satisfies $p>A>w_i$ and $p>7$.  Therefore all nodes in
each coordinate are distinct in $\mathbb F_p$.  Tensor Lagrange interpolation
gives an evaluation isomorphism



$$
\boxed{
\left\{
F:\deg_{d_1}F\le6,
\ \deg_{d_i}F\le w_i\ (2\le i\le m)
\right\}
\xrightarrow{\ \sim\ }
\operatorname{Fun}(\mathcal B_m,\mathbb F_p).}
\tag{4.2}
$$



Consequently the singleton indicator, after substituting the load recurrence,
does have a $p$-dependent representative on the canonical box with total
degree at most



$$
\boxed{
6+\sum_{i=2}^{m}w_i
=2m^2+4m=O(n^2).}
\tag{4.3}
$$



This is a genuine algebraic collapse from the unrestricted Item-362 degree
when $p$ is large.  It is not a capacity theorem.  The interpolation
coefficients use inverses of factorials modulo the candidate $p$ and change
with $p$; (4.2) supplies no candidate-independent integer lift and no
archimedean upper bound of the form (1.4).

The tensor rank is



$$
B_m=7\prod_{i=2}^{m}(w_i+1).
\tag{4.4}
$$



Continuant recursion gives



$$
\prod_{i=1}^{m}w_i\le a
\le\prod_{i=1}^{m}(w_i+1),
\tag{4.5}
$$



and



$$
\sum_{i=2}^{m}\log\left(1+\frac1{w_i}\right)=O(\log m).
\tag{4.6}
$$



Therefore



$$
\boxed{\log B_m=\log a+O(\log n)=(1+o(1))\log b.}
\tag{4.7}
$$



Unstructured box interpolation has beta-scale rank, not sublinear
complexity.

## 5. Exact canonical-window rank

Canonical Ostrowski words are in bijection with integers $0\le R<a$.
The intermediate half-window is



$$
\left\lceil\frac{a}{2c}\right\rceil
\le R\le\frac{a-1}{2}.
\tag{5.1}
$$



It therefore contains exactly



$$
\boxed{
M_n
=\frac{a+1}{2}
-\left\lceil\frac{a}{2c}\right\rceil}
\tag{5.2}
$$



canonical words.  Since $a/c<A$,



$$
M_n=\frac a2-O(A),
\qquad
\boxed{\log M_n=(1+o(1))\log b.}
\tag{5.3}
$$



For $p>A$, distinct digit words remain distinct modulo $p$ coordinatewise.
The evaluation algebra on the window therefore has dimension exactly $M_n$.
The Markov and half-language restrictions do not by themselves create a
low-rank family; their function space is still beta-scale.

## 6. The genuine fixed-$n$ actual orbit has rank at most one

The actual target is much thinner than the canonical window.  At fixed $n$,



$$
\kappa=\operatorname{nint}(a^2/b),
\qquad
R_{\rm act}=|a^2-\kappa b|
\tag{6.1}
$$



are fixed integers.  If $R_{\rm act}$ lies in the window, the Ostrowski
expansion supplies one unique canonical word.  The sign, endpoint, small
error, and quotient conditions either accept this word or reject it.  Hence



$$
\boxed{|\mathcal O_n|\le1,}
\tag{6.2}
$$



where $\mathcal O_n$ denotes the genuine fixed-$n$ actual target orbit.

This exact fact prevents the desired Zariski-density argument.  Restriction
from the $M_n$-dimensional window function algebra to $\mathcal O_n$ has
rank at most one and kernel dimension at least $M_n-1$ when the orbit is
nonempty.  At a singleton hit,



$$
\Phi_{p,N}|_{\mathcal O_n}=0
\tag{6.3}
$$



has the trivial degree-zero representative.  This is exact but contains no
arithmetic gain: the zero integer has no usable logarithmic height.

The same point applies to Item 362's first quotient.  On the one-point orbit,



$$
\frac{\Phi_{p,N}}p
\equiv
-q_p\left(t\prod_{i\ne j(p)}Z_i\right)\pmod p
\tag{6.4}
$$



is represented by one constant scalar.  That scalar depends on $p$ and on
the actual word.  Degree zero on one point is not a uniform quotient theorem.

Across different $n$, the number of variables, the continued-fraction word,
the target prime, and the actual point all change.  No fixed ambient variety
or cross-$n$ Zariski-density theorem is presently available.

## 7. Why pointwise cancellation does not pass admission

Let $\mathcal P_{1,1}$ be the actual singleton-squarefree prime set.  Suppose
one obtains a candidate-independent integer evaluation $h_n\ne0$ satisfying



$$
p\mid h_n\qquad(p\in\mathcal P_{1,1}).
\tag{7.1}
$$



The primes are distinct, so exactly



$$
\boxed{\mathcal U_{1,1}\mid h_n,
\qquad
\log\mathcal U_{1,1}\le\log|h_n|.}
\tag{7.2}
$$



Thus a new upper bound for $|h_n|$ would solve the branch; interpolation
alone does not provide it.  The pointwise representative zero fails the
nonzero condition.  Choosing a separate constant multiple of $p$ for each
candidate and multiplying them reproduces $\mathcal U_{1,1}$ itself, with
no compression.  Combining $p$-dependent box polynomials by the Chinese
remainder theorem similarly supplies no height below the modulus unless an
additional arithmetic theorem is proved.

This is the strongest valid no-go at the actual-orbit level: polynomial
degree collapses completely on the one-point orbit, so degree is not the
right invariant there.  The missing object is a **uniform nonzero height
certificate**, not another pointwise finite-field representative.

## 8. Exact missing theorem and capacity decision

The remaining Builder target is precisely a family $H_n$, independent of
the candidate prime, for which the actual Item-316 implication proves



$$
\mathcal U_{1,1}\mid H_n,
\qquad
0<|H_n|,
\qquad
\log|H_n|=o(\log b),
\tag{8.1}
$$



or a direct weighted zero-density theorem of equivalent strength.  A weaker
strict-fraction height could still reduce beta capacity and should be audited
against the ledger before proof work.

Item 365 proves no such theorem.  It instead closes endpoint-only
cancellation and identifies why box/orbit interpolation cannot be booked:



$$
\boxed{
\text{formal endpoint gain}=0,
\quad
\text{pointwise orbit gain}=0,
\quad
\text{uniform height rate}=\mathrm{OPEN}.}
\tag{8.2}
$$



## 9. Strict labels

### PROVED

* The endpoint load-coordinate unit and all-$p^r$ freeness (2.4)-(2.7).
* Exact-zero-stratum endpoint degree preservation (3.1)-(3.3).
* Canonical-box tensor interpolation and degree bound (4.2)-(4.3).
* Beta-scale box and canonical-window ranks (4.7) and (5.3).
* The fixed-$n$ actual-orbit bound $|\mathcal O_n|\le1$.
* The exact admission implication (7.2).

### PROVED SCOPED NO-GO

* Endpoint equality, with or without exact-zero stratification, as a source
  of reduced degree for the externally $t$-saturated row-only singleton
  function.
* Fixed-$n$ actual-orbit degree as evidence for a nonzero low-height carrier.
* Candidate-by-candidate constants or CRT assembly as automatic height
  compression.
* These results do not close a uniform cross-$n$ interpolation theorem,
  canonical small-quotient distribution, or arbitrary Cartier/$F$-crystal
  mechanism.

### EXACT FINITE ONLY

* The replay's declared continuant bridges, $b^2$ endpoint solutions,
  canonical-language enumeration, tensor interpolation bases, and degree
  controls.
* No declared word is promoted to an actual target or density datum.

### OPEN

* A candidate-independent nonzero $H_n$ satisfying (8.1).
* Uniform cross-$n$ orbit structure or a direct weighted zero-density theorem.
* A cancellation essentially mixing the internal $t$-coordinate with the
  endpoint and canonical box.
* Actual quotient/Fermat correlations and canonical small-quotient arithmetic.
* The singleton and growing low-incidence bounds, $\Xi_Q$, and squarefull
  excess.
* $H_Q$, $K_Q$, $\Gamma_Q$, the centered half-bound, beta capacity, Route 1,
  and $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{9.1}
$$



No canonical, master, status, checkpoint, or research-log file is edited by
this work package.

## 10. Deterministic replay

From the archive root:

~~~text
python work/item365_beta_actual_orbit_interpolation_barrier_certificate.py ^
  --output work/item365_beta_actual_orbit_interpolation_barrier_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer
arithmetic.  It performs no prime census, target search, or half-bound scan
and promotes no declared word.
