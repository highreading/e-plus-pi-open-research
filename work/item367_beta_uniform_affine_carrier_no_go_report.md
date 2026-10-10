> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 367 — uniform affine-carrier dichotomy across the actual beta family

Checked: 2026-09-01 (Beijing time)

## 1. Verdict and capacity admission

Item 365 shows that the genuine fixed-$n$ target orbit has at most one point.
Consequently pointwise finite-field degree is not a uniform invariant.  Item
367 instead studies a prime-independent integer carrier across $n$.

Let $mathcal U_{1,1}(n)$ be Item 358's actual $t$-avoiding,
singleton-squarefree carrier.  Its unresolved ceiling is



$$
0\le \log \mathcal U_{1,1}(n)\le \log Q_n\le \log b_n.
\tag{1.1}
$$



A useful uniform construction must give an integer $H_n$, independent of the
candidate prime, such that



$$
\mathcal U_{1,1}(n)\mid H_n,
\qquad H_n\ne0,
\tag{1.2}
$$



and either



$$
\log|H_n|=o(\log b_n)
\tag{1.3}
$$



or at least $log|H_n|\le(1-\eta)\log b_n+o(\log b_n)$ for some fixed
$\eta>0$.  The latter would give a fixed fractional capacity saving; the
former would close the singleton branch at zero rate.

Item 367 proves the following scoped no-go.

> **SUB-BETA AFFINE-RATIONAL CARRIER DICHOTOMY.**  Suppose that, after the
> actual endpoint and canonical-box specialization, a candidate-independent
> integer carrier has
> 

$$
> D_nH_n=\alpha_na_n+\beta_nc_n+\gamma_n,
>
$$


> where all four integer coefficients have a common envelope
> $B_n=b_n^{o(1)}$.  If $(\alpha_n,\beta_n)\ne(0,0)$, then
> 

$$
> \log|H_n|=(1+o(1))\log b_n.
>
$$


> Thus this entire genuinely denominator-dependent class cannot give (1.3)
> or any fixed fractional saving.  The only sub-beta branch in the class is
> the $q$-free residual $H_n=\gamma_n/D_n$.

The theorem covers bounded fixed windows of consecutive $q$'s, fixed-degree
rational coefficients in a bounded number of actual digits or loads, and
bounded-order affine recurrences whose **unrolled coefficient height** is
$b^{o(1)}$.  Fixed recurrence order alone is not closed: an order-one product
accumulator already has beta-scale height.

No $q$-free residual with the actual implication (1.2) is constructed.
Therefore the new booking is zero.

## 2. The genuine tied family across $n$

Let $\mathfrak N$ be the set of indices $n\ge5$ for which the hypothetical
Item-316 target holds.  No assertion that $\mathfrak N$ is nonempty is made.
For $n\in\mathfrak N$, put



$$
A=4n-2,
\qquad
a=q_{n-1},\quad b=q_n,\quad c=q_{n-2},
\qquad
b=Aa+c,
\tag{2.1}
$$



where



$$
q_0=q_1=1,
\qquad
q_k=(4k-2)q_{k-1}+q_{k-2}.
\tag{2.2}
$$



The actual centered remainder



$$
R_{\rm act}
=\left|a^2-b\operatorname{nint}(a^2/b)\right|
\tag{2.3}
$$



has one unique canonical Ostrowski word.  The Item-316 sign, small-error, and
endpoint conditions either accept that word or reject it.  On an accepted
word, retain the actual nonzero loads



$$
Z_{j,n}=|w_jd_{j-1}-d_j|,
\qquad j\in\mathcal J_n,
\tag{2.4}
$$



the actual $t_n$, the de-overlapped target $Q_n\mid b_n$, and
$Q_n^{[1]}$.  The exact singleton carrier is



$$
\mathcal U_{1,1}(n)
=
\prod_{\substack{
A<p<A^2, v_p(Q_n)=1, p\nmid t_n\\
\#\{j\in\mathcal J_n:p\mid Z_{j,n}\}=1}}
p.
\tag{2.5}
$$



This is the actual family used below.  A uniform carrier $H_n$ may depend on
$n$ and on this entire canonical specialization, but not on a chosen prime
from (2.5).

## 3. The admitted affine-rational class

Let $B_n\ge1$ satisfy



$$
\log B_n=o(\log b_n).
\tag{3.1}
$$



A **sub-beta affine-rational continued-fraction carrier** is an integer
$H_n$ for which there exist integers



$$
1\le D_n\le B_n,
\qquad
|\alpha_n|,|\beta_n|,|\gamma_n|\le B_n,
\tag{3.2}
$$



such that



$$
\boxed{
D_nH_n=\alpha_na_n+\beta_nc_n+\gamma_n.}
\tag{3.3}
$$



The coefficients may be arbitrary prime-independent functions of $n$, the
actual sign, canonical digits, loads, or endpoint data; only their final
integer heights are constrained by (3.1)-(3.2).  Thus the theorem is not a
claim that the coefficients are constant or polynomial in $n$.

This class is capacity-admitted.  If $\alpha_n=\beta_n=0$ and $H_n\ne0$,
then



$$
\log|H_n|\le\log B_n=o(\log b_n).
\tag{3.4}
$$



Consequently, proving (1.2) for such a residual would immediately prove
$\log\mathcal U_{1,1}=o(\log b)$.  The theorem below determines exactly why
the denominator-dependent branch cannot do the same.

## 4. A uniform short-linear-form bound

Write $m=n-2$ and



$$
w_1=7,
\qquad
w_i=4i+2\quad(2\le i\le m).
\tag{4.1}
$$



Continuant reversal gives the exact finite continued fraction



$$
\boxed{
\frac ac=[w_m;w_{m-1},\ldots,w_1].}
\tag{4.2}
$$



Every partial quotient in (4.2) is at most $A$.  Let $B<c$, and let
$\alpha,\beta$ be integers with



$$
0<\max(|\alpha|,|\beta|)\le B.
\tag{4.3}
$$



Then



$$
\boxed{
|\alpha a+\beta c|
\ge
\frac{c}{(A+2)B}.}
\tag{4.4}
$$



Here is a complete proof.  The case $\alpha=0$ is immediate.  Otherwise
reduce $-\beta/\alpha=r/s$ to lowest terms, with $1\le s\le B$.  If $r/s$
is not a convergent of $a/c$, Legendre's criterion gives



$$
\left|\frac ac-\frac rs\right|
\ge\frac1{2s^2},
\tag{4.5}
$$



and hence $|sa-rc|\ge c/(2s)$.  If $r/s$ is a proper convergent, let
$s^+$ be the next denominator.  The standard exact convergent bounds and
the partial-quotient ceiling give



$$
\left|\frac ac-\frac rs\right|
>
\frac1{s(s+s^+)},
\qquad
s^+\le(A+1)s.
\tag{4.6}
$$



Therefore $|sa-rc|>c/((A+2)s)$.  The final convergent has denominator $c>B$
and cannot occur.  Restoring the common divisor of $\alpha$ and $\beta$
proves (4.4).

This is an all-$n$ theorem.  It is not a finite irrationality-measure
heuristic and uses no information about which primes divide $b$.

## 5. The affine-rational dichotomy

Assume (3.1)-(3.3).  Since



$$
c<a<Ac,
\qquad
b=Aa+c<A^2c,
\tag{5.1}
$$



one has



$$
\log c=\log b+O(\log n).
\tag{5.2}
$$



Condition (3.1) implies, for all sufficiently large $n$,



$$
2(A+2)B_n^2<c.
\tag{5.3}
$$



Suppose $(\alpha_n,\beta_n)\ne(0,0)$.  From (4.4), (5.3), and
$|\gamma_n|\le B_n$,



$$
|\alpha_na+\beta_nc+\gamma_n|
\ge
\frac{c}{2(A+2)B_n}.
\tag{5.4}
$$



Dividing by $D_n\le B_n$ gives the exact lower bound



$$
\boxed{
|H_n|
\ge
\frac{c}{2(A+2)B_n^2}.}
\tag{5.5}
$$



Conversely, (3.2)-(3.3) give



$$
|H_n|\le B_n(a+c+1).
\tag{5.6}
$$



Equations (3.1), (5.2), (5.5), and (5.6) prove



$$
\boxed{
\log|H_n|=(1+o(1))\log b_n
\quad\text{when }(\alpha_n,\beta_n)\ne(0,0).}
\tag{5.7}
$$



If $\alpha_n=\beta_n=0$, then $H_n=\gamma_n/D_n$ and (3.4) holds.  Thus
there is no third asymptotic regime:



$$
\boxed{
\begin{array}{c|c}
\text{$q$-dependent branch}&\log|H_n|=(1+o(1))\log b_n,\\
\text{$q$-free residual}&\log|H_n|=o(\log b_n).
\end{array}}
\tag{5.8}
$$



If (1.2) is proved in the first branch, the resulting upper bound is still
one full beta copy.  It cannot imply zero rate or any fixed fractional
saving.  If (1.2) is proved in the second branch, it immediately gives zero
rate.  Item 367 identifies this residual but does not construct it.

## 6. Fixed windows and bounded-complexity formulas

Fix $K$.  Repeatedly using (2.2), every $q_{n-r}$ with $0\le r\le K$ is an
integer linear combination of $a=q_{n-1}$ and $c=q_{n-2}$ whose coefficients
are $A^{O_K(1)}$.  Therefore a rational affine expression



$$
\frac{
\sum_{r=0}^{K}u_{r,n}q_{n-r}+v_n
}{D_n}
\tag{6.1}
$$



belongs to the class of Section 3 whenever the original coefficients and
denominator have sub-beta height.

The same applies when those coefficients are fixed-degree rational formulas
in a bounded number of actual canonical digits and loads.  Indeed,



$$
0\le d_i\le A,
\qquad
0<Z_{j,n}<A^2,
\tag{6.2}
$$



so any fixed number of such inputs at fixed algebraic degree has height
$A^{O(1)}=b^{o(1)}$ after clearing a nonzero denominator.

More generally, an affine state recurrence is covered whenever its unrolled
coefficients and denominator satisfy (3.1).  For example, $L=o(n)$ updates
with polynomial-in-$A$ coefficient growth have



$$
\log B_n=O(L\log A)=o(n\log n)=o(\log b).
\tag{6.3}
$$



Hence every genuinely $q$-dependent output of these bounded-window or
sublinear-depth classes has the one-copy obstruction (5.7).

This is a theorem about the **reduced coefficient height**, not syntax.  It
does not claim that every short formula has small unrolled height.

## 7. Why recurrence order alone is not a no-go

The exact singleton union already has the order-one accumulator



$$
P_0=1,
\qquad
P_j=Z_{j,n}P_{j-1},
\qquad
P_N=\prod_{j\in\mathcal J_n}Z_{j,n}.
\tag{7.1}
$$



Thus fixed state dimension and fixed recurrence order do not prevent an
all-row carrier.  But



$$
\log|P_N|<2N\log A,
\tag{7.2}
$$



which is beta-scale when $N=\Theta(n)$.  The accumulator lies outside (3.1)
precisely when it has enough active depth to matter.  This agrees with Item
346: positive linear $t$-avoiding radical mass requires linearly many active
depths.

Consequently Item 367 does **not** claim a bounded-order recurrence no-go.
It closes the bounded-order affine subclass only under the necessary
sub-beta unrolled-height condition.  Nonlinear products, gcd/radical
operations, and beta-height states remain outside the theorem.

## 8. Exact remaining Builder target

Inside the class, the only possible successful object is a nonzero
prime-independent residual



$$
H_n=\frac{\gamma_n}{D_n},
\qquad
\log|H_n|=o(\log b_n),
\tag{8.1}
$$



for which the **actual** implication



$$
\boxed{\mathcal U_{1,1}(n)\mid H_n}
\tag{8.2}
$$



is proved from the canonical Item-316 word.  Pointwise interpolation does not
supply (8.2), and formal endpoint freeness supplies no such residual.  A
uniform quotient, trace, or small-integer identity could in principle do so;
none is known.

Outside the class, one must control an iterated beta-height state by a new
weighted theorem rather than by expression length or recurrence order.

## 9. Strict labels

### PROVED

* The exact cross-$n$ actual-family formulation (2.1)-(2.5).
* The all-$n$ short-linear-form bound (4.4).
* The affine-rational height dichotomy (5.5)-(5.8).
* The fixed-$q$-window reduction and bounded-input corollary.
* Zero capacity booking.

### PROVED SCOPED NO-GO

* Candidate-independent, genuinely $q$-dependent affine-rational carriers
  with sub-beta reduced coefficient and denominator height.
* Bounded fixed-$q$ windows and bounded-order affine recurrences when their
  unrolled coefficient height is sub-beta.
* Such carriers as a source of zero rate or any fixed fractional beta saving.

### EXACT FINITE ONLY

* The replay's declared continued-fraction rows, coefficient boxes, and
  fixed-window reduction matrices.
* No declared row is promoted to an actual target, prime distribution, or
  asymptotic density datum.

### OPEN

* A $q$-free residual satisfying the actual divisibility (8.2).
* Iterated recurrences with beta-height accumulated coefficients.
* Nonlinear polynomial, gcd/radical, trace, and quotient carriers outside
  (3.3).
* The weighted singleton bound, growing low incidence, $\Xi_Q$, and squarefull
  excess.
* The centered half-bound, beta capacity, Route 1, and $e+\pi$.

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
python work/item367_beta_uniform_affine_carrier_no_go_certificate.py ^
  --output work/item367_beta_uniform_affine_carrier_no_go_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer
arithmetic.  It performs no prime census, target search, or half-bound scan.
