> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 370 — q-free singleton residual saturation after endpoint elimination

Checked: 2026-09-01 (Beijing time)

## 1. Verdict and capacity admission

Item 367 isolates one possible sub-beta branch.  A prime-independent carrier
can have height $o(\log b)$ inside its affine-rational class only after its
$q$-dependent part cancels, leaving a residual



$$
H_n=\frac{\gamma_n}{D_n},
\qquad
0<|H_n|=b_n^{o(1)}.
\tag{1.1}
$$



For this residual to change the ledger, the genuine actual-family implication



$$
\boxed{\mathcal U_{1,1}(n)\mid H_n}
\tag{1.2}
$$



must be proved.  Here $\mathcal U_{1,1}$ is Item 358's externally
$t$-saturated, singleton-squarefree carrier.  If (1.2) holds, then



$$
\log\mathcal U_{1,1}\le\log|H_n|=o(\log b),
\tag{1.3}
$$



which closes the branch at zero rate.  Thus the q-free residual passes the
capacity screen.

Item 370 does not construct such an $H_n$.  It proves a broad exact
classification for endpoint-reduced rational identities:

> **GENERIC SINGLETON-CHART SATURATION.**  After eliminating the genuine
> Item-316 endpoint, let a prime-independent rational residual have an
> integral numerator $G_n$ and a denominator which is a unit on every
> externally $t$-saturated singleton chart.  If the residual is forced to
> vanish on every possible singleton chart, then modulo the relevant prime
> 

$$
> G_n\in\left(\prod_{j\in\mathcal J_n}X_j\right).
>
$$


> Therefore a numerator of load degree below $N=|\mathcal J_n|$, or one
> omitting any active load, must be the zero polynomial modulo that prime.
> Every captured prime then divides the integer coefficient content of
> $G_n$.

Consequently a primitive nonzero bounded-window residual captures no prime
by such an identity.  A nonzero sub-beta coefficient content would be a real
carrier, but none is constructed.  The zero numerator and candidate-dependent
CRT constants are inadmissible.  Full-support degree-$N$ states and
correlations holding only at the unique canonical point remain open.

Booking is zero.

## 2. The actual singleton family

Assume the genuine Item-316 target at an index $n\ge5$.  It fixes the centered
remainder, unique canonical word, sign, small error, and endpoint.  After
omitting exact-zero integer rows, write



$$
\mathcal J_n=\{j:Z_{j,n}\ne0\},
\qquad
N=|\mathcal J_n|.
\tag{2.1}
$$



If $N=0$, then $\mathcal U_{1,1}=1$ and the branch is trivial, so assume
$N\ge1$.  The actual singleton primes are



$$
\mathcal P_{1,1}(n)
=
\left\{
\begin{array}{l|l}
p& A<p<A^2, v_p(Q_n)=1, p\nmid t_n,\\
&\#\{j\in\mathcal J_n:p\mid Z_{j,n}\}=1
\end{array}
\right\},
\tag{2.2}
$$



and



$$
\mathcal U_{1,1}(n)=\prod_{p\in\mathcal P_{1,1}(n)}p.
\tag{2.3}
$$



For each $p\in\mathcal P_{1,1}(n)$, let $j(p)$ be its unique hit row.  The
outside loads and $t_n$ are $p$-units.  This is the genuine first-occurrence
and all-outside-row avoidance condition, not Item 350's former selected-hit
relaxation.

Item 346 proves that positive beta-scale $t$-avoiding radical mass requires
$N=\Omega(n)$.  Therefore a fixed or sublinear row portfolio must be closed
before it can be considered a positive-mass mechanism.

## 3. The endpoint-reduced residual class

Use Item 365's integral load coordinates



$$
X_j=w_jd_{j-1}-d_j.
\tag{3.1}
$$



For every $p\mid b$, the coefficient of $d_1$ in the endpoint defect is a
$p$-unit.  Hence, after imposing $\Delta_\sigma=0$ modulo $p$, the row loads
are independent coordinates:



$$
\frac{\mathbb F_p[d_1,d_2,X_1,\ldots,X_N]}{(\Delta_\sigma)}
\cong
\mathbb F_p[d_2,X_1,\ldots,X_N].
\tag{3.2}
$$



The relabeling $X_1,\ldots,X_N$ refers only to the retained rows in
$\mathcal J_n$.

Item 370 treats rational functions



$$
\mathscr H_n=\frac{G_n(d_2,X_1,\ldots,X_N)}
{V_n(d_2,X_1,\ldots,X_N)},
\tag{3.3}
$$



where:

1. $G_n,V_n$ have integer coefficients independent of the candidate prime;
2. $G_n$ is the integral numerator after the endpoint reduction;
3. $V_n$ is nonzero and a unit on every singleton chart under discussion;
4. the actual specialization of (3.3), when integral, is the residual (1.1).

The unit condition is necessary.  A rational expression whose denominator
vanishes on the target chart is not a defined carrier and cannot infer
divisibility of its numerator.

The phrase **generically forced on a singleton chart** means a polynomial
identity in the localized endpoint quotient, not an equality observed only
at the unique actual digit word.  That distinction is the scope boundary of
the theorem.

## 4. Exact singleton-chart kernel

Fix a prime $p\mid b$ and put



$$
R_p=\mathbb F_p[d_2,X_1,\ldots,X_N].
\tag{4.1}
$$



On the $j$-th singleton chart, impose $X_j=0$ and invert every outside load
and the already external $t$-coordinate.  Because the inverted elements are
not in the prime ideal $(X_j)$, contraction back to $R_p$ gives exactly



$$
\ker(R_p\longrightarrow R_{p,j})=(X_j).
\tag{4.2}
$$



The product of all singleton-chart maps therefore has kernel



$$
\bigcap_{j=1}^{N}(X_j).
\tag{4.3}
$$



The $X_j$ are distinct prime variables, so



$$
\boxed{
\bigcap_{j=1}^{N}(X_j)
=
\left(\prod_{j=1}^{N}X_j\right).}
\tag{4.4}
$$



This statement is unchanged by the $p$-unit denominator in (3.3): a rational
function with unit denominator is zero on a chart exactly when its numerator
is zero there.

Thus a nonzero generic numerator forced to vanish on every singleton chart
must satisfy



$$
\deg_X G_n\ge N
\tag{4.5}
$$



and must involve every active load.  If $\deg_XG_n<N$, or if one active load
is absent, then



$$
\boxed{G_n\equiv0\pmod p}
\tag{4.6}
$$



as a polynomial, not merely at the actual point.

This is the exact q-free residual analogue of the all-row product barrier,
now after the genuine endpoint elimination and with rational $p$-unit
denominators included.

## 5. Bounded windows and portfolios

Suppose a numerator $G_\ell$ is assigned a set $S_\ell$ of singleton charts.
The same proof gives



$$
G_\ell\in
\bigcap_{j\in S_\ell}(X_j)
=
\left(\prod_{j\in S_\ell}X_j\right)
\pmod p,
\tag{5.1}
$$



unless $G_\ell$ is the zero polynomial modulo $p$.  Therefore its noncontent
branch has



$$
\deg_XG_\ell\ge|S_\ell|.
\tag{5.2}
$$



For a portfolio whose assigned chart sets cover all active rows,



$$
\bigcup_{\ell=1}^{r}S_\ell=\{1,\ldots,N\},
\tag{5.3}
$$



the numerators which remain in their noncontent branches necessarily satisfy



$$
\boxed{
\sum_{\ell\in\mathcal L_{\rm nc}}\deg_XG_\ell
\ge
\sum_{\ell\in\mathcal L_{\rm nc}}|S_\ell|,}
\tag{5.4}
$$



where $\mathcal L_{\rm nc}$ is the set of noncontent portfolio members.  If
every member is noncontent and the assigned sets cover all rows, the right
side is at least $N$.  In particular:

* a fixed window omitting a possible hit row cannot give one nonzero generic
  residual for the entire singleton family;
* a fixed number of fixed-degree residuals covers only $O(1)$ rows;
* a sublinear total load-degree portfolio cannot cover the $N=\Omega(n)$
  regime required for positive beta mass entirely through noncontent
  branches; the remaining charts must enter coefficient-content branches.

An iterated recurrence can reach total degree $N$ with fixed state dimension,
for example by accumulating $\prod_jX_j$.  Equation (5.4) does not close that
linear-depth branch.

## 6. The coefficient-content carrier

For a nonzero integer polynomial, define



$$
\operatorname{cont}(G_n)
=gcd\{\text{nonzero coefficients of }G_n\}>0.
\tag{6.1}
$$



Equation (4.6) is equivalent to



$$
p\mid\operatorname{cont}(G_n).
\tag{6.2}
$$



Consequently, if one prime-independent numerator of degree below $N$ is
generically forced on all singleton charts for every actual
$p\in\mathcal P_{1,1}(n)$, then



$$
\boxed{
\mathcal U_{1,1}(n)\mid\operatorname{cont}(G_n).}
\tag{6.3}
$$



For a portfolio in which every assigned numerator has
$\deg_XG_\ell<|S_\ell|$, the corresponding statement is



$$
\mathcal U_{1,1}(n)\mid
\prod_{\ell=1}^{r}\operatorname{cont}(G_\ell)
\tag{6.4}
$$



More generally, (6.4) applies to the subcarrier supported on charts whose
assigned numerator falls into the content branch; noncontent charts retain
the degree cost (5.4).

This gives the complete capacity decision for the closed class.  If



$$
0<\log\operatorname{cont}(G_n)=o(\log b),
\tag{6.5}
$$



or the analogous portfolio sum is $o(\log b)$, then (6.3) or (6.4) is a real
zero-rate carrier.  No such nonzero actual residual is produced here.

If $G_n$ is primitive, then $\operatorname{cont}(G_n)=1$, so no prime can be
captured by the generic low-degree identity.  If $G_n=0$, its ``content'' is
not a nonzero carrier and the residual is inadmissible.

## 7. Inadmissible escapes and exact scope

Three apparent escapes do not change the theorem.

1. **Zero residual.**  The identity $G_n=0$ has no nonzero integer height and
   gives no divisibility bound.
2. **Candidate-dependent constants.**  Taking $G_{n,p}=p$ or assembling
   separate CRT constants merely inserts the candidate prime into the
   formula.  It is not prime-independent and is outside (3.3).
3. **Vanishing denominator.**  A quotient with $V_n=0$ on a singleton chart
   is undefined, not an extra numerator zero.

The no-go is deliberately scoped to identities on the generic localized
singleton charts.  The actual canonical orbit has one point.  A polynomial
could vanish accidentally at that point without belonging to (4.4); proving
that such a coincidence holds for the moving actual primes would be a new
arithmetic correlation theorem.  Item 370 neither assumes nor excludes it.

## 8. The surviving residual classes

After Item 370, a successful q-free continuation must do one of the
following:

1. construct a nonzero sub-beta coefficient content satisfying (6.3) from
   the actual canonical word;
2. prove a correlation specific to the unique canonical point, rather than
   a generic chart identity;
3. use a full-support degree-$N$ recurrence and prove cancellation or a
   weighted height bound beyond the raw product estimate;
4. use arithmetic operations such as gcd, radical, trace, or a quotient
   theorem not represented by the $p$-unit rational class (3.3).

No member of these classes is constructed here.

## 9. Strict labels

### PROVED

* The endpoint-reduced localized singleton-chart kernel (4.2)-(4.4).
* The p-unit rational-denominator reduction.
* The load-degree and full-support lower bound (4.5)-(4.6).
* The portfolio total-degree bound (5.4).
* The exact coefficient-content carrier implication (6.3)-(6.4).
* Zero booking.

### PROVED SCOPED NO-GO

* Primitive nonzero generic residuals of load degree below $N$.
* Generic bounded-window residuals omitting a possible active row.
* Bounded portfolios with total noncontent load degree below the number of
  covered singleton charts.
* Unit rational denominators as an escape from numerator saturation.

### EXACT FINITE ONLY

* The replay's sparse-monomial intersections, declared coefficient-content
  rows, and product-accumulator support controls.
* No declared prime or polynomial is promoted to an actual beta target or
  density datum.

### OPEN

* A nonzero sub-beta content satisfying the actual implication (6.3).
* Correlations holding only at the unique canonical point.
* Full-support degree-$N$ recurrences and beta-height product cancellation.
* Nonlinear gcd/radical, trace, quotient, and finite-field arithmetic outside
  the class.
* The actual singleton bound, growing low incidence, $\Xi_Q$, squarefull
  excess, beta capacity, Route 1, and $e+\pi$.

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
python work/item370_beta_q_free_residual_saturation_no_go_certificate.py ^
  --output work/item370_beta_q_free_residual_saturation_no_go_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer sparse
polynomials.  It performs no actual prime census, target search, or half-bound
scan.
