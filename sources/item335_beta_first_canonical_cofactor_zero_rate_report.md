> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 335 — the first canonical beta cofactor has zero divisor rate

Checked: 2026-09-01 (Beijing time)

## 1. Strict verdict and capacity-first selection

Retain



$$
q_0=q_1=1,
\qquad
q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\ge2),
\tag{1.1}
$$



and, for $n\ge5$, put



$$
A=4n-2,
\qquad
a=q_{n-1},\quad b=q_n,\quad c=q_{n-2},
\qquad m=n-2.
\tag{1.2}
$$



Item 316 makes an actual centered half-bound failure equivalent to one exact
canonical digit word.  In its sign chamber, write



$$
\sigma=\operatorname{sgn}(E_m),
\qquad
\epsilon=(-1)^n\sigma,
\qquad
\Delta=\sigma E_{m+1}-a.
\tag{1.3}
$$



Item 333 proves that $\Delta$ is a saturated integral coordinate.  After
setting $\Delta=0$, its first surviving top-boundary coordinate is



$$
\boxed{
\mathfrak z_m
=\epsilon(\delta_m-w_m\delta_{m-1}),}
\qquad
w_m=A-4.
\tag{1.4}
$$



This coordinate is genuinely canonical: it uses the actual top Ostrowski
digits and their half-language bounds.  It is not another formal recurrence
identity counted as an obstruction.

The exact load formula is



$$
\boxed{
\mathfrak z_j
=(1+w_jw_{j-1})J_{j-2}-w_jJ_{j-3}-J_j
=\epsilon(\delta_j-w_j\delta_{j-1})
\quad(3\le j\le m).}
\tag{1.5}
$$



At the top, if $L$ denotes the lower-digit part of $\Delta$, Item 333's
unimodular coordinate becomes



$$
\boxed{
L-a+\epsilon\delta_{m-1}
=\Delta+A\mathfrak z_m.}
\tag{1.6}
$$



Thus an actual collision, for which $\Delta=0$, forces the exact quotient



$$
\boxed{
\frac{L-a+\epsilon\delta_{m-1}}{A}=\mathfrak z_m.}
\tag{1.7}
$$



The factor $A$ and the primitive quotient $\mathfrak z_m$ are the first
canonical arithmetic content left after the old defect is removed.

Capacity admission immediately decides this candidate.  The exact
half-language gives



$$
0\le\delta_m\le\frac{w_m}{2},
\qquad
0\le\delta_{m-1}\le w_{m-1}=A-8,
\tag{1.8}
$$



and therefore



$$
|\mathfrak z_m|<(4n)^2.
\tag{1.9}
$$



The apparent zero branch is not a hidden reservoir.  The bounds in (1.8)
give the exact equivalence



$$
\boxed{
\mathfrak z_m=0
\iff
\delta_m=\delta_{m-1}=0.}
\tag{1.10}
$$



Strip the forced zero boundary and continue one depth down; let
$\mathfrak z_*$ be the first nonzero adjacent cofactor encountered.  The
Item-316 lower window makes the digit word nonzero above the bottom digit, so
this first survivor always exists and satisfies the uniform theorem



$$
\boxed{
1\le|\mathfrak z_*|
\le w_mw_{m-1}<A^2.}
\tag{1.11}
$$



Consequently, for every divisor $Q\mid b$,



$$
\boxed{
\sum_p
\min\{v_p(Q),v_p(\mathfrak z_*)\}\log p
=\log\gcd(Q,|\mathfrak z_*|)
<2\log A.}
\tag{1.12}
$$



Since $\log b=n\log n+O(n)$, the entire divisor or valuation capacity of
the first canonical cofactor is zero rate on the beta scale.

The closure extends to every fixed-complexity top-cofactor portfolio.  A
fixed number of $\mathfrak z_j$'s, inserted into a bounded-degree
polynomial with polynomial-height coefficients, has only $O(\log n)$
total prime-power mass whenever its value is nonzero.

This is a global zero-rate/no-go theorem, not a target exclusion.  A growing
number of depths, growing degree or coefficient height, a global cofactor
involving the full lower word, or canonical complement redigitization may
still have $n\log n$-scale height.  Those directions remain open.

The centered half-bound is not proved.  Booking and beta capacity reduction
remain zero.

## 2. Canonical digits and the target window

Set



$$
w_1=7,
\qquad
w_j=4j+2\quad(2\le j\le m),
\qquad
w_{m+1}=A.
\tag{2.1}
$$



Let $Q_{-1}=0,Q_0=1$ and



$$
Q_j=w_jQ_{j-1}+Q_{j-2}.
\tag{2.2}
$$



Then $Q_m=a$, $Q_{m-1}=c$, and every $0\le R<a$ has canonical digits



$$
R=\sum_{i=1}^{m}\delta_iQ_{i-1},
\tag{2.3}
$$





$$
0\le\delta_1\le6,
\qquad
0\le\delta_i\le w_i\quad(2\le i\le m),
\tag{2.4}
$$





$$
\delta_i=w_i\Longrightarrow\delta_{i-1}=0.
\tag{2.5}
$$



The actual Item-316 target additionally has



$$
\frac{a}{2c}\le R<\frac a2.
\tag{2.6}
$$



The upper inequality is exactly the canonical half-language; in particular,
it gives the top bound in (1.8).  The lower inequality implies



$$
R>\frac{w_m}{2}\ge7,
\tag{2.7}
$$



because $a=w_mc+q_{n-3}$.  Since the largest word supported only at
$\delta_1$ is $6$, every target word has a nonzero digit with index at
least two.

This small observation is what guarantees that the first survivor in
Section 5 occurs at an index where the load formula (1.5) is defined.  No
bounded census is used.

## 3. Suffix loads and first quotients

Retain Item 323's suffix recurrence



$$
H_m=1,\quad H_{m+1}=0,
\qquad
N_m=N_{m+1}=0,
\tag{3.1}
$$





$$
H_{j-1}=w_{j+1}H_j+H_{j+1},
\tag{3.2}
$$





$$
N_{j-1}=w_{j+1}N_j+N_{j+1}+\delta_{j+1}.
\tag{3.3}
$$



For the actual sign chamber, put



$$
\kappa=|E_m|,
\qquad
J_j=\kappa H_j+\epsilon N_j.
\tag{3.4}
$$



Item 330 proves that $J_j$ is the exact first quotient of the lifted
transducer.  The inverse load formula is



$$
\delta_j=N_{j-2}-w_jN_{j-1}-N_j
\qquad(2\le j\le m).
\tag{3.5}
$$



Applying (3.5) at two adjacent indices gives



$$
\begin{aligned}
\delta_j-w_j\delta_{j-1}
={}&(1+w_jw_{j-1})N_{j-2}\\
&-w_jN_{j-3}-N_j.
\end{aligned}
\tag{3.6}
$$



The corresponding homogeneous suffix combination vanishes:



$$
(1+w_jw_{j-1})H_{j-2}
-w_jH_{j-3}-H_j=0.
\tag{3.7}
$$



Multiplying (3.6) by $\epsilon$, substituting (3.4), and using (3.7)
proves the load identity (1.5).  The large common $\kappa H$ state cancels
exactly, leaving a canonical integer of polynomial size.

This cancellation is the reason $\mathfrak z_j$, rather than an arbitrary
large $J_j$, is the first arithmetic cofactor to audit after Item 333.

## 4. Exact top quotient after the target defect

Item 333 writes the target defect as



$$
\Delta
=L-a+u\delta_{m-1}+v\delta_m,
\tag{4.1}
$$



where



$$
u=\epsilon(Aw_m+1),
\qquad
v=-\epsilon A.
\tag{4.2}
$$



Using (1.4),



$$
\begin{aligned}
u\delta_{m-1}+v\delta_m
&=\epsilon\delta_{m-1}
-A\epsilon(\delta_m-w_m\delta_{m-1})\\
&=\epsilon\delta_{m-1}-A\mathfrak z_m.
\end{aligned}
\tag{4.3}
$$



Therefore



$$
L-a+\epsilon\delta_{m-1}
=\Delta+A\mathfrak z_m,
\tag{4.4}
$$



which is (1.6).  On the actual target $\Delta=0$, so $A$ divides the
left side and the exact quotient is $\mathfrak z_m$.

Both pieces are small:



$$
\log A=O(\log n),
\qquad
\log^+|\mathfrak z_m|=O(\log n).
\tag{4.5}
$$



Thus neither the compulsory factor $A$ nor its primitive top quotient can
carry positive beta-scale mass.  Dividing by already visible content cannot
improve this conclusion.

## 5. The canonical first-survivor theorem

Let



$$
\ell=\max\{i:\delta_i>0\}.
\tag{5.1}
$$



Section 2 gives $2\le\ell\le m$.  Define



$$
j_*=
\begin{cases}
m,&\ell=m,\\
\ell+1,&\ell<m.
\end{cases}
\tag{5.2}
$$



For every $j>j_*$, both $\delta_j$ and $\delta_{j-1}$ vanish, so



$$
\mathfrak z_j=0.
\tag{5.3}
$$



If $\ell<m$, then



$$
\mathfrak z_{j_*}
=-\epsilon w_{\ell+1}\delta_\ell\ne0.
\tag{5.4}
$$



If $\ell=m$, the half-language gives two cases.  When
$\delta_{m-1}=0$,



$$
\mathfrak z_m=\epsilon\delta_m\ne0.
\tag{5.5}
$$



When $\delta_{m-1}\ge1$,



$$
\delta_m-w_m\delta_{m-1}
\le-\frac{w_m}{2}<0.
\tag{5.6}
$$



Thus $\mathfrak z_{j_*}\ne0$ in every case.  Monotonicity of the weights
and the digit bounds give



$$
1\le|\mathfrak z_{j_*}|
\le w_{j_*}w_{j_*-1}
\le w_mw_{m-1}<A^2.
\tag{5.7}
$$



Equations (5.3)-(5.7) prove that $\mathfrak z_*:=\mathfrak z_{j_*}$ is
exactly the first nonzero adjacent load cofactor encountered when the zero
top boundary is stripped.  It is selected canonically and is always a
nonzero integer, not a formal indeterminate.

## 6. Prime-power mass and fixed-complexity closure

For any nonzero integer $V$,



$$
\sum_p v_p(V)\log p=\log|V|.
\tag{6.1}
$$



Taking $V=\mathfrak z_*$ and using (5.7) gives



$$
\sum_p v_p(\mathfrak z_*)\log p<2\log A.
\tag{6.2}
$$



More specifically, for any declared full or proper target $Q\mid b$,



$$
\begin{aligned}
\sum_p\min\{v_p(Q),v_p(\mathfrak z_*)\}\log p
&=\log\gcd(Q,|\mathfrak z_*|)\\
&<2\log A.
\end{aligned}
\tag{6.3}
$$



Item 265 gives



$$
\log b=n\log n+O(n),
\tag{6.4}
$$



and therefore



$$
\boxed{
\frac{
\log\gcd(Q,|\mathfrak z_*|)
}{\log b}
\longrightarrow0.}
\tag{6.5}
$$



The same conclusion holds after any compulsory factors are removed.

There is also a uniform fixed-complexity closure.  Fix nonnegative integers
$K,D,C$.  Choose at most $K$ cofactor values $\mathfrak z_j$, and let



$$
P_n\in\mathbb Z[X_1,\ldots,X_K]
\tag{6.6}
$$



have total degree at most $D$ and coefficient height at most $A^C$.
Every canonical digit word satisfies



$$
|\mathfrak z_j|\le A^2.
\tag{6.7}
$$



Hence, for



$$
V_n=P_n(\mathfrak z_{j_1},\ldots,\mathfrak z_{j_K}),
\tag{6.8}
$$



one has



$$
|V_n|
\le
\binom{D+K}{K}A^{C+2D}.
\tag{6.9}
$$



Whenever $V_n\ne0$,



$$
\boxed{
\sum_pv_p(V_n)\log p
\le(C+2D)\log A+O_{K,D}(1)
=O_{K,D,C}(\log n).}
\tag{6.10}
$$



Thus fixed-cardinality products, bounded-degree determinants, and other
fixed-complexity polynomial portfolios in these boundary cofactors are all
zero rate.

If $V_n=0$, (6.10) is not a divisor-mass statement.  An independently
proved exact zero/nonzero contradiction could still exclude the target and
is not ruled out.  What is closed is booking positive prime-power mass from
a nonzero fixed-complexity boundary-cofactor value.

## 7. Scope, proper targets, and admission decision

The actual-family chain is



$$
\text{half-bound failure}
\Longrightarrow
\text{Item-316 canonical target}
\Longrightarrow
\Delta=0
\Longrightarrow
\text{the exact quotient (1.7)}.
\tag{7.1}
$$



The first-survivor selection additionally uses only the actual target window
and the canonical digit bounds.  No ambient digit point is called an actual
collision.

The candidate fails the capacity screen decisively:



$$
\boxed{
\text{raw first-cofactor capacity}
\le2\log(4n)=o(n\log n).}
\tag{7.2}
$$



This remains true for every proper divisor $Q\mid b$, by (6.3).  It does
not prove a centered residue lower bound modulo $Q$, and Item 282's product
baseline is neither divided out nor rebooked.

The theorem closes:

* the primitive top Bezout quotient as a positive-mass reservoir;
* recursive stripping of zero top pairs followed by the first nonzero
  adjacent cofactor;
* every fixed number of such boundary cofactors at bounded polynomial
  complexity; and
* valuation claims supported only on their nonzero integer values.

It does not close:

* a portfolio whose number of depths grows with $n$;
* degree or coefficient height growing fast enough to reach $n\log n$;
* a full-word cofactor involving the exponentially large lower contribution
  $L$;
* an exact sign or nonvanishing contradiction specialized to the actual
  target; or
* canonical complement redigitization or an external arithmetic period.

Those are the smallest remaining ways for this branch to regain admissible
height.  Another fixed boundary quotient should not be promoted as strategic
progress.

## 8. Strict labels

### PROVED

* The exact adjacent load-cofactor identity (1.5).
* The exact target quotient (1.6)-(1.7).
* The zero-top equivalence (1.10).
* Existence, nonvanishing, and the $A^2$ bound for the canonical first
  survivor (5.1)-(5.7).
* The exact proper-target mass bound (6.3).
* The fixed-complexity polynomial-height theorem (6.6)-(6.10).
* The actual-family and capacity audits in Section 7.

### PROVED GLOBAL ZERO-RATE / SCOPED NO-GO

* The first canonical arithmetic cofactor after quotienting by the old
  target defect has zero divisor and valuation rate on the $n\log n$ beta
  scale.
* Recursively stripping zero top pairs does not rescue the mechanism: the
  first nonzero survivor is still smaller than $A^2$.
* Every fixed-cardinality, bounded-degree, polynomial-coefficient-height
  portfolio of adjacent boundary cofactors has zero rate when nonzero.

### EXACT FINITE ONLY

* The deterministic replay's declared canonical words, load identities,
  top-quotient decompositions, first-survivor rows, and factorizations.
* These rows replay the formulas and are never promoted to a target census,
  a half-bound theorem, or a prime-distribution theorem.

### OPEN

* The original all-digit exclusion and centered half-bound.
* Growing-depth or growing-complexity canonical cofactor portfolios.
* Exact target-specific sign, nonvanishing, gcd-distribution, or valuation
  theorems not supplied by ordinary height.
* Full-word lower-coordinate arithmetic and canonical complement
  redigitization.
* A proper-target residue lower bound, weighted zero-density theorem, or beta
  capacity reduction.
* Route 1 and every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{8.1}
$$



No canonical, master, status, checkpoint, or research-log file is edited by
this work package.

## 9. Deterministic replay

From the archive root:

~~~text
python work/item335_beta_first_canonical_cofactor_zero_rate_certificate.py ^
  --output work/item335_beta_first_canonical_cofactor_zero_rate_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer
arithmetic.  It performs no half-bound scan, no exceptional-prime scan, and
promotes no bounded row.
