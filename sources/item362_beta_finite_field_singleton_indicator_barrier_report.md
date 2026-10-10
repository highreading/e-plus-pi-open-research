> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 362 — finite-field singleton indicators and the Frobenius-height barrier

Checked: 2026-09-01 (Beijing time)

## 1. Strict verdict and capacity admission

Assume the genuine canonical Item-316 target.  Retain



$$
A=4n-2,
\qquad m=n-2,
\qquad Q\mid b,
\qquad t=c-\kappa,
\tag{1.1}
$$



and, after omitting every exact-zero row, write



$$
\mathcal J=\{j:\mathfrak z_j\ne0\},
\qquad
Z_j=|\mathfrak z_j|,
\qquad
0<Z_j<A^2.
\tag{1.2}
$$



If $N=|\mathcal J|=0$, then the singleton carrier is $1$ and this
branch is already trivial, so below assume $N\geq1$.  On the actual word,
$N\leq m-2=n-4<p$; the ambient cases $p\mid N$ treated below are
included for the complete finite-field theorem, not because they occur in
the actual tied range.

Item 358 isolates the fresh singleton-squarefree carrier



$$
\mathcal U_{1,1}
=\prod_{\substack{A<p<A^2,\ p\mid Q,\ v_p(Q)=1,\ p\nmid t\\
\#\{j\in\mathcal J:p\mid Z_j\}=1}}p.
\tag{1.3}
$$



Its raw capacity is still



$$
0\le\log\mathcal U_{1,1}\le\log Q\le\log b.
\tag{1.4}
$$



Item 362 studies the one carrier class left open by Item 358: polynomial
functions over the varying field $\mathbb F_p$, including the relations
$Y^p-Y$ and direct Frobenius/Cartier evaluations which compute that same
exact indicator function.  It proves:

1. The exact $t$-avoiding singleton indicator has a unique reduced
   representative of total degree at least $N(p-1)$ for $N=|\mathcal J|$;
   its degree in every participating variable is $p-1$.
2. The integral load recurrence is a triangular coordinate change.  Before
   the endpoint equation and canonical box are imposed, it cannot lower the
   row-only reduced degree.
3. The exact candidate-by-candidate indicator loop is merely another formula
   for (1.3).  Its canonical integer lift has height at least
   $(p-1)\log p$ at every hit, so aggregating hits expands, rather than
   compresses, the unresolved mass by a factor at least $A$.
4. Modulo $p^2$, the first quotient is a moving Fermat quotient.  The
   mod-$p$ indicator identity forces no second digit.

Thus bounded-degree exact polynomial-function carriers, bounded-depth
ordinary arithmetic circuits, kernel additions using $Y^p-Y$, and the
canonical reduced integer lift are closed as zero-rate mechanisms.  An
actual target-specific cancellation or distribution theorem remains open.
No capacity is booked.

## 2. The finite-field function algebra

Fix an odd prime $p$ and $N\ge1$.  Put



$$
\mathscr A_{p,N}
=\frac{\mathbb F_p[T,Y_1,\ldots,Y_N]}
{(T^p-T,Y_1^p-Y_1,\ldots,Y_N^p-Y_N)}.
\tag{2.1}
$$



Evaluation identifies $\mathscr A_{p,N}$ with all functions
$\mathbb F_p^{N+1}\to\mathbb F_p$.  Every function has a unique reduced
representative satisfying



$$
\deg_T,\deg_{Y_1},\ldots,\deg_{Y_N}\le p-1.
\tag{2.2}
$$



For completeness, existence follows by repeatedly replacing $X^p$ by $X$.
Uniqueness follows by induction on the number of variables: a nonzero
univariate polynomial of degree at most $p-1$ cannot vanish at all $p$
field elements, and its coefficients are reduced functions in the remaining
variables.  The reduction $X^e\mapsto X^{e-(p-1)}$ for $e\ge p$ never
increases total degree.  Consequently the total degree of the unique reduced
representative is a lower bound for every polynomial representing the same
function.

The functions



$$
\mathbf z_p(Y)=1-Y^{p-1},
\qquad
\mathbf n_p(Y)=Y^{p-1}
\tag{2.3}
$$



are respectively the zero and nonzero indicators.  The relation $Y^p-Y$
is the zero function; adding its multiples can change a formal lift but
cannot change the unique reduced class.

## 3. Exact singleton indicator and its minimal degree

The $t$-avoiding singleton indicator is



$$
\mathcal I_{p,1}(T;Y)
=T^{p-1}
\sum_{j=1}^{N}
(1-Y_j^{p-1})
\prod_{i\ne j}Y_i^{p-1}.
\tag{3.1}
$$



It equals one exactly when $T\ne0$ and exactly one $Y_j$ is zero, and equals
zero otherwise.  Define its complementary vanishing carrier



$$
\Phi_{p,N}=1-\mathcal I_{p,1}.
\tag{3.2}
$$



Thus $\Phi_{p,N}=0$ precisely on the desired finite-field locus.  Expanding
(3.2) gives its already reduced representative:



$$
\boxed{
\Phi_{p,N}
=1
-T^{p-1}\sum_{j=1}^{N}\prod_{i\ne j}Y_i^{p-1}
+N T^{p-1}\prod_{i=1}^{N}Y_i^{p-1}.}
\tag{3.3}
$$



The $N$ partial-product monomials in (3.3) are distinct, have nonzero
coefficient $-1$, and have total degree $N(p-1)$.  The full-product
coefficient is $N$ modulo $p$.  Hence the minimal total degree is exactly



$$
\boxed{
\deg\Phi_{p,N}
=
\begin{cases}
(N+1)(p-1),&p\nmid N,\\
N(p-1),&p\mid N.
\end{cases}}
\tag{3.4}
$$



In every case



$$
\boxed{\deg\Phi_{p,N}\ge N(p-1).}
\tag{3.5}
$$



Every participating variable has individual degree $p-1$.  One can also
see the unavoidable $p-1$ directly: fixing $T=1$ and all rows except one
to one restricts the complement function to $Y^{p-1}$.

If $p\nmid t$ is imposed externally, the row-only complement is



$$
\phi_{p,N}(Y)
=1-
\sum_{j=1}^{N}(1-Y_j^{p-1})\prod_{i\ne j}Y_i^{p-1}.
\tag{3.6}
$$



Its exact minimal degree is $N(p-1)$ when $p\nmid N$ and
$(N-1)(p-1)$ when $p\mid N$.  This is the version relevant when the
$t$-avoidance has already been performed by Item 358's saturation.

## 4. The entire low-incidence indicator tower

The same argument is not confined to singletons.  For $2\le L\le N+1$,
let



$$
\mathcal I_{p,<L}
=T^{p-1}
\sum_{k=1}^{L-1}
\sum_{\substack{S\subseteq\{1,\ldots,N\}\\|S|=k}}
\prod_{j\in S}(1-Y_j^{p-1})
\prod_{i\notin S}Y_i^{p-1}.
\tag{4.1}
$$



This detects $t$-avoiding incidence between one and $L-1$.  In
$1-\mathcal I_{p,<L}$, choose a set $S$ of size $L-1$ and take the constant
term from every factor $(1-Y_j^{p-1})$, $j\in S$.  The resulting monomial



$$
T^{p-1}\prod_{i\notin S}Y_i^{p-1}
\tag{4.2}
$$



has coefficient $-1$ and cannot arise from a smaller zero set.  It therefore
survives reduction and gives



$$
\boxed{
\deg(1-\mathcal I_{p,<L})
\ge (N-L+2)(p-1).}
\tag{4.3}
$$



If $t$-avoidance is imposed externally, removing the factor $T^{p-1}$ gives
the analogous lower bound



$$
\boxed{(N-L+1)(p-1).}
\tag{4.4}
$$



For every $L=o(N)$ both bounds are still $\Omega(Np)$.  Thus passing from
the singleton layer to a slowly growing Item-354 threshold does not create
a bounded-degree exact indicator.

## 5. The canonical load recurrence does not hide the ambient degree

Use Item 350's signed loads



$$
x_j=w_jd_{j-1}-d_j=-\epsilon\mathfrak z_j
\qquad(3\le j\le m).
\tag{5.1}
$$



The map



$$
(d_1,\ldots,d_m)
\longleftrightarrow
(d_1,d_2,x_3,\ldots,x_m)
\tag{5.2}
$$



is an integral triangular automorphism, with inverse
$d_j=w_jd_{j-1}-x_j$.  On any fixed exact-zero stratum, the remaining
$x_j$ are still independent load coordinates before the endpoint target and
canonical inequalities are imposed.

Modulo $p$, this integral determinant is still a unit.  Composition with the
linear load map cannot increase the reduced functional degree, and composition
with its linear inverse gives the reverse inequality.  Hence the minimal
finite-field functional degree is invariant under the load change.  Therefore
the row-only degree in (3.6), and the external-$t$ low-incidence lower bound
(4.4), survive every uniform argument using only the load recurrence.

This is deliberately scoped.  The unique canonical target is one integer
point after the endpoint equation, digit bounds, signs, and small-quotient
windows are imposed.  A special cancellation on that thinner arithmetic
set is not ruled out; proving one would be a new actual-family theorem, not
a consequence of the recurrence or Frobenius relation alone.

## 6. Exact actual candidate loop

Evaluate (3.3) at the genuine target values $(t,Z_j)$.  The finite-field
truth table gives the exact identity



$$
\boxed{
\mathcal U_{1,1}
=\prod_{\substack{A<p<A^2\\p\mid Q^{[1]}}}
\gcd\bigl(p,\Phi_{p,N}(t;Z)\bigr),}
\tag{6.1}
$$



where



$$
Q^{[1]}=\prod_{v_p(Q)=1}p.
\tag{6.2}
$$



Indeed, the gcd in (6.1) is $p$ exactly when $p\nmid t$ and exactly one
$Z_j$ is divisible by $p$; otherwise it is one.  Equivalently one may use
$\phi_{p,N}$ from (3.6) after restricting the product to $p\nmid t$.

Equation (6.1) is an actual-family implication, but it is a candidate loop,
not a common carrier.  Its exponent and polynomial change with the prime
being tested, and enumerating the factors already requires the candidate
prime divisors of $Q^{[1]}$.  It therefore has the same raw capacity as
(1.3):



$$
\log\mathcal U_{1,1}\le\log Q\le\log b.
\tag{6.3}
$$



No density estimate follows from the exact truth table.

## 7. Integer height dilation

The canonical reduced lift is not only high-degree; at every hit it is
archimedeanly large.  Put



$$
P=\prod_{i=1}^{N}Z_i^{p-1}.
\tag{7.1}
$$



Over the integers, the row part of the singleton indicator is



$$
\sum_j(1-Z_j^{p-1})\prod_{i\ne j}Z_i^{p-1}
=P\left(\sum_j Z_j^{-(p-1)}-N\right)\le0.
\tag{7.2}
$$



Suppose $p$ is a $t$-avoiding singleton and $j$ is its unique row.  Then
$Z_j\ge p$, while every other $Z_i\ge1$.  Equations (3.2) and (7.2) give



$$
\boxed{
\Phi_{p,N}(t;Z)
\ge p^{p-1}>0.}
\tag{7.3}
$$



The same bound holds for the externally $t$-restricted lift
$\phi_{p,N}(Z)$.  Conversely,



$$
\phi_{p,N}(Z)
\le1+N\prod_i Z_i^{p-1}
<1+N A^{2N(p-1)}.
\tag{7.4}
$$



Thus this exact lift has a per-hit logarithmic height at least



$$
(p-1)\log p\ge A\log p,
\tag{7.5}
$$



because $p>A$.  If $\mathcal F$ denotes the product of the hit-specific
canonical lifts, then



$$
\boxed{
\log|\mathcal F|
\ge A\log\mathcal U_{1,1}.}
\tag{7.6}
$$



So the direct finite-field lift expands the desired mass by a factor at
least $A\asymp n$.  A height bound on these candidate-dependent integers is
strictly worse than the original one-copy bound.

There is also a degree version of the capacity test.  If
$\log\mathcal U_{1,1}\ge\eta\log b$ for fixed $\eta>0$, then, since
$\log p<2\log A$, there are



$$
r\ge\frac{\eta\log b}{2\log A}=\left(\frac\eta2+o(1)\right)n
\tag{7.7}
$$



distinct singleton primes.  A row cannot contain two primes larger than
$A$ because $Z_j<A^2$, so $N\ge r=\Omega(n)$.  Equations (3.5) and
$p-1\ge A$ then force



$$
\boxed{\deg\Phi_{p,N}\ge NA=\Omega(n^2)}
\tag{7.8}
$$



throughout any positive-mass counterconfiguration.

## 8. Frobenius and Cartier states

Adding a multiple of $Y_i^p-Y_i$ changes a polynomial representative but
not its reduced function class.  Since reduction never raises degree, such
kernel additions cannot beat (3.4)-(3.5).

For an ordinary binary arithmetic circuit whose multiplication depth is
$d$, starting from variables of degree one, the formal degree is at most
$2^d$.  Hence an exact $t$-away singleton circuit without a primitive
$p$-power gate has



$$
\boxed{d\ge\left\lceil\log_2(N(p-1))\right\rceil.}
\tag{8.1}
$$



Repeated squaring attains logarithmic depth for $Y^{p-1}$, so (8.1) is not
an exponential circuit lower bound.  It does show that a fixed-depth state
cannot work for growing $p$.  Declaring Frobenius $Y\mapsto Y^p$ to be one
primitive operation merely hides the same issue: under an integer lift it
multiplies logarithmic size by $p$, and the resulting zero/nonzero test still
has the height dilation (7.3)-(7.6).

This section closes only exact polynomial functions, ordinary bounded-depth
circuits, and direct Frobenius evaluations of their canonical integer lifts.
It proves no lower bound for an arbitrary $F$-crystal or Cartier-state
dimension, and it does not rule out a new trace, character-sum, large-sieve,
or target-specific Cartier theorem which uses more than the indicator truth
table.

## 9. Modulo $p$ is not modulo $p^2$

Let $j$ be the unique row divisible by $p$ and set



$$
V_j=t\prod_{i\ne j}Z_i.
\tag{9.1}
$$



Since $p\nmid V_j$ and $Z_j^{p-1}$ is divisible by $p^{p-1}$, every term
containing $Z_j^{p-1}$ vanishes modulo $p^2$.  Therefore



$$
\boxed{
\Phi_{p,N}(t;Z)
\equiv1-V_j^{p-1}\pmod{p^2}.}
\tag{9.2}
$$



Writing



$$
q_p(V)=\frac{V^{p-1}-1}{p}\pmod p
\tag{9.3}
$$



for the Fermat quotient gives



$$
\boxed{
\frac{\Phi_{p,N}(t;Z)}p
\equiv-q_p(V_j)\pmod p.}
\tag{9.4}
$$



The original singleton condition forces the mod-$p$ zero in (6.1), but it
does not force $q_p(V_j)=0$.  This failure is uniform, not the result of a
prime scan.  For every odd prime $p$, take the declared ambient tied-range
control



$$
t=1,
\qquad
(Z_1,Z_2)=(p,p-1).
\tag{9.5}
$$



The binomial theorem gives



$$
(p-1)^{p-1}\equiv1+p\pmod{p^2},
\tag{9.6}
$$



so $q_p(p-1)=1$ and



$$
v_p\bigl(\Phi_{p,2}(1;p,p-1)\bigr)=1.
\tag{9.7}
$$



This declared family is not promoted to a canonical Item-316 word.  Its
role is to prove that the finite-field indicator identity itself has no
universal second-digit lift.  Any actual $p^2$ theorem would have to come
from new endpoint or canonical-box arithmetic.

## 10. The exact missing theorem

The finite-field method can become useful only if the actual target supplies
an additional compression not present in the truth table.  One sufficient
form would be a nonzero, candidate-independent integer $H_n$ such that



$$
p\mid H_n
\quad\text{for every }p\mid\mathcal U_{1,1},
\qquad
\log|H_n|=o(\log b).
\tag{10.1}
$$



Then $\log\mathcal U_{1,1}\le\log|H_n|=o(\log b)$.  Item 362 proves that
$H_n$ cannot be obtained merely by taking the exact reduced singleton
indicator, adding Frobenius-kernel relations, or multiplying its
candidate-specific integer evaluations.

A different possible input would be an actual-family extra-digit theorem
forcing $p^2\mid\Phi_{p,N}(t;Z)$ at singleton primes, followed by a weighted
zero-density theorem for



$$
q_p\left(t\prod_{i\ne j(p)}Z_i\right)=0.
\tag{10.2}
$$



Neither implication is presently proved, and (9.5)-(9.7) show that the first
does not follow from the indicator identity alone.  The direct target remains



$$
\boxed{\log\mathcal U_{1,1}=o(\log b),}
\tag{10.3}
$$



followed by Item 358's growing low-incidence theorem.

## 11. Strict labels

### PROVED

* Unique reduced finite-field representation and exact degree formula
  (3.3)-(3.5).
* The all-$L$ low-incidence degree lower bound (4.3).
* Recurrence-only degree preservation under the triangular load coordinates.
* The actual candidate-loop identity (6.1).
* Canonical-lift height dilation (7.3)-(7.8).
* The Frobenius-kernel and bounded multiplication-depth barriers.
* The exact mod-$p^2$ Fermat-quotient bridge (9.2)-(9.4).
* The all-odd-prime ambient construction proving no universal second digit.

### PROVED SCOPED NO-GO

* Bounded-degree exact polynomial-function indicators as a zero-rate carrier.
* Fixed multiplication-depth indicators without a primitive $p$-power gate.
* Adding $Y^p-Y$ kernel relations to lower the unique reduced degree.
* Canonical reduced lifts or their candidate products as height compression.
* These statements do not exclude target-specific cancellation, large-sieve,
  trace, monodromy, or moving-Fermat-quotient theorems.

### EXACT FINITE ONLY

* The replay's small-field truth tables, declared degree cases, triangular
  load check, candidate loop, and all-odd-prime symbolic-family instances.
* No declared row is an actual target or density datum.

### OPEN

* A candidate-independent $H_n$ satisfying (10.1).
* Any actual extra-digit implication and the moving Fermat-quotient density.
* The actual singleton and growing low-incidence bounds.
* $\Xi_Q$, Item 265's excess, $H_Q$, $K_Q$, and $\Gamma_Q$.
* The centered half-bound, beta capacity, Route 1, and $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{11.1}
$$



No canonical, master, status, checkpoint, or research-log file is edited by
this work package.

## 12. Deterministic replay

From the archive root:

~~~text
python work/item362_beta_finite_field_singleton_indicator_barrier_certificate.py ^
  --output work/item362_beta_finite_field_singleton_indicator_barrier_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer
arithmetic.  It performs no prime census, target search, or half-bound scan
and promotes no declared row.
