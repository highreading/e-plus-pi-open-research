> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 294 — exact half-integer gauge of the ordinary-$j=2$ connection-minor operator

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain Item 291's two connection minors



$$
L_n=9\det(f,b),\qquad M_n=-11\det(f,d),              \tag{1.1}
$$



on the rays $r=6n+e$, $e\in\{1,5\}$.  The Item-291 finite
reconstruction proposed an order-three, degree-seventeen recurrence for
both $L_n$ and $16^nM_n$.

> **PROVED — exact operator conjugacy.**  The reconstructed operator is
> exactly a hypergeometric gauge of Item 237's already certified
> algebraic-coefficient operator, restricted to
> 

$$
>                         h=\frac r2=3n+\frac e2.             \tag{1.2}
>
$$


> This is a polynomial identity, not a fit.

This theorem identifies the missing proof but does not supply it.  An
operator identity does not show that a new sequence lies in its kernel.
For $16^nM_n$, a remarkably simple bridge to Item 237 holds on the
declared twelve exact rows of each ray, but has no all-$n$ certificate.
For $L_n$, an exact two-row determinant proves that the corresponding
normalized sequence is not even the single algebraic coefficient line
already certified by Item 237.

Thus the Item-291 recurrence remains **EXACT FINITE ONLY / OPEN** for both
connection minors.  No Frobenius or density conclusion follows, and



$$
\boxed{\text{new Route-1 booking}=0}.                       \tag{1.3}
$$



## 2. The certified Item-237 operator

Let $C(x)$ be Item 237's algebraic series and put



$$
c_m=[x^m]C(x).                       \tag{2.1}
$$



Item 237 proved a differential-operator identity whose coefficient form
is



$$
\sum_{j=0}^3p_j(m/2)c_{m+6j}=0                 \tag{2.2}
$$



for every coefficient index $m$.  Each $p_j\in\mathbb Q[h]$ has
degree sixteen.  In particular, (2.2) applies to odd $m=r$; no
extension by numerical interpolation is being made.

For a fixed residue $e\in\{1,5\}$, define



$$
q_j^{(e)}(n)=p_j\!\left(3n+\frac e2\right).                 \tag{2.3}
$$



The Item-291 phase labels are reversed relative to $e$: its label 5
is the ray $e=1$, while its label 1 is the ray $e=5$.

## 3. Exact conjugacy of all four coefficients

Let $P_j^{(e)}(n)$ denote the four reconstructed Item-291 coefficient
polynomials on the ray $e$.  Put



$$
\mathcal R(r)=
 \frac{r(r+6)(2r+9)^2(2r+15)^2}
 {78732(r+1)^2(r+2)(r+4)(r+5)^2},
 \qquad 78732=4\cdot3^9.                                  \tag{3.1}
$$



The exact identity is



$$
\boxed{
 \frac{P_{j+1}^{(e)}(n)/q_{j+1}^{(e)}(n)}
      {P_j^{(e)}(n)/q_j^{(e)}(n)}
 =\mathcal R(r+6j),\qquad j=0,1,2.}                         \tag{3.2}
$$



The checker proves all six instances after cross multiplication in
$\mathbb Q[n]$.  The largest cleared degree is 39.  This also explains
the previously mysterious degree-five and degree-nine cores: they are
the Item-237 cores evaluated at the half-integer affine arguments in
(2.3).

Define $g_0=1$ and



$$
\frac{g_n}{g_{n+1}}=\mathcal R(6n+e).     \tag{3.3}
$$



Equation (3.2) says precisely that



$$
\sum_{j=0}^3P_j^{(e)}(n)y_{n+j}=0
 \quad\Longleftrightarrow\quad
 \sum_{j=0}^3q_j^{(e)}(n)\frac{y_{n+j}}{g_{n+j}}=0.         \tag{3.4}
$$



This is an equivalence of formal recurrences over $\mathbb Q$.  It is
not a proof of the left side for a specified $y$.

## 4. The exact finite bridge for $M$

On the twelve recorded values $0\leq n\leq11$ of each ray, exact
rational arithmetic gives



$$
\frac{16^nM_n}{g_n}=\lambda_e c_{6n+e},                    \tag{4.1}
$$



where



$$
\lambda_1=-\frac{891}{100},\qquad
                 \lambda_5=\frac{3897234}{41405}.           \tag{4.2}
$$



If (4.1) were proved for every $n$, then (2.2)--(3.4) would prove the
candidate recurrence for $16^nM_n$.  No coefficient-kernel identity,
WZ divergence, Hermite reduction, or rational-parametrization identity
for (4.1) is present.  Therefore (4.1) is labelled **EXACT FINITE ONLY**.
It is the precise remaining scalar bridge, not a theorem inferred from
twelve values.

The simplification $H_\nu^\flat=-11d_\nu$ is essential here: it removes
the old lower-tail summand and makes $M_n$ the pure connection minor in
(1.1).  It does not by itself prove (4.1).

## 5. Why the same direct reuse fails for $L$

Put $\widetilde L_n=L_n/g_n$.  The first two rows give the exact
determinants



$$
\det\!\begin{pmatrix}
 \widetilde L_0&c_e\\
 \widetilde L_1&c_{e+6}
 \end{pmatrix}
 =
 \begin{cases}
  5045260/243,&e=1,\\
  97069100/189,&e=5.
 \end{cases}                                               \tag{5.1}
$$



Both are nonzero.  Likewise, with
$\widetilde B_n=16^nM_n/g_n$,



$$
\det\!\begin{pmatrix}
 \widetilde L_0&\widetilde B_0\\
 \widetilde L_1&\widetilde B_1
 \end{pmatrix}
 =
 \begin{cases}
  -2774893/15,&e=1,\\
  2802229606440/57967,&e=5.
 \end{cases}                                               \tag{5.2}
$$



Consequently normalized $L$ is neither the existing Item-237
coefficient line nor the observed normalized-$M$ line.  This is a
sharp obstruction only to the **single already certified solution-line
reuse**.  It does not exclude a second algebraic numerator, a larger
period module, a WZ certificate, or another annihilating operator proof.

## 6. Rational and modular singular factors

Over $\mathbb Q$, every factor of the forward coefficient
$P_3^{(e)}(n)$, including its positive quintic core, is positive for
$n\geq0$.  Hence a future proof of the recurrence would give a regular
forward rational recurrence.

The situation modulo an actual row prime



$$
p=2r+6s+3                            \tag{6.1}
$$



is different.  Every denominator factor in (3.1) is a $p$-unit:
$r+1,r+2,r+4,r+5<p$, and $p>3$.  Its numerator is nonzero modulo
$p$ except on



$$
\begin{array}{c|c}
 s=1&2r+9=p,\\
 s=2&2r+15=p.
 \end{array}                                               \tag{6.2}
$$



Thus the gauge is not invertible on the first two actual layers.

After primitive integral clearing, $P_3^{(e)}$ contains all six
linear factors



$$
2r+9,2r+15,2r+21,2r+27,2r+33,2r+39.       \tag{6.3}
$$



They vanish respectively on $s=1,2,\ldots,6$.  The remaining quintic
core can also vanish modulo an actual prime; no unit theorem for it is
proved.  Therefore even a future rational recurrence theorem would not
automatically be an all-row invertible $p$-adic transport.

## 7. Admission and capacity

The proved result recognizes the candidate operator and localizes two
separate missing identities.  It supplies no new collision-forced
integer, no all-prime exclusion, and no weighted zero estimate.  The raw
ordinary-$j=2$ ceiling remains



$$
\frac{2}{35}\text{ per }M
                   =\frac1{105}\text{ per }6M.               \tag{7.1}
$$



Recurrence closure, even if later completed, would still have to be
connected to Frobenius or a genuine moving-prime density theorem before
any capacity could be booked.

## 8. Reproduction and strict labels

From the portable archive root:

~~~
python scripts/item294_j2_half_integer_gauge_certificate.py \
  --output results/item294_j2_half_integer_gauge_certificate.json
python scripts/item294_j2_half_integer_gauge_certificate.py \
  --output results/item294_j2_half_integer_gauge_certificate_replay.json
~~~

### PROVED

* The six cleared polynomial identities (3.2), and hence the exact
  half-integer gauge conjugacy (3.4).
* The rational and modular singular-factor audit in Section 6.
* The two exact nonproportionality witnesses (5.1)--(5.2).

### EXACT FINITE ONLY

* The bridge (4.1) on exactly twelve values of each ray.
* The original Item-291 recurrence residuals at their declared finite
  bounds.

### OPEN

* An all-$n$ proof of (4.1).
* A second algebraic or period realization for normalized $L$.
* The candidate recurrence for either connection minor.
* Any Frobenius, nonvanishing, weighted-density, or capacity theorem.
