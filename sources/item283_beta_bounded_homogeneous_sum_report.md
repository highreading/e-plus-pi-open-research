> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 283 — bounded homogeneous sums have only an $O(n)$ cancellation quotient

Checked: 2026-08-31 (Beijing time)

## 1. Declared class and verdict

Retain



$$
q_0=q_1=1,\qquad q_{n+2}=(4n+6)q_{n+1}+q_n,            \tag{1.1}
$$





$$
P_0(X)=0,\quad P_1(X)=1,\quad
P_{h+2}(X)=(4X+4h+6)P_{h+1}(X)+P_h(X),                 \tag{1.2}
$$



and



$$
\mathcal C_h(n)=q_nq_{n+h+1}-q_{n+1}q_{n+h}.            \tag{1.3}
$$



Item 282 isolated additive tied-minimum cancellation as the first place
where a sum can see a prime absent from every individual return.  This
item closes the broad bounded-complexity homogeneous class below.

Fix once and for all:

* a sparsity bound $T$;
* a common total monomial degree $K$;
* a coefficient degree/height bound; and
* a constant $\Lambda>0$.

For every $n$, choose at most $T$ monomials



$$
\mathcal A_j(n)
 :=\prod_{\ell=1}^K P_{h_{j,\ell}(n)}(n),               \tag{1.4}
$$



with gaps $h_{j,\ell}(n)\ge2$ satisfying



$$
L_j(n):=\sum_{\ell=1}^K(h_{j,\ell}(n)-1)
\le{\Lambda n\over\log n}.                             \tag{1.5}
$$



The gaps may move arbitrarily with $n$, but for admission they are
specified independently of the target prime, its factorization, and its
unknown valuation.

Let $c_j(n)\in\mathbb Z$ be prime-independent coefficients with



$$
\log\max_j(1,|c_j(n)|)=O(\log n).                       \tag{1.6}
$$



This includes evaluations of fixed bounded-degree integer polynomials
and fixed rational polynomials after one fixed denominator is cleared.
Zero-coefficient terms are omitted.  Define



$$
\mathcal R(n)=\sum_jc_j(n)\mathcal A_j(n).              \tag{1.7}
$$



The associated homogeneous scalar-Casoratian sum is



$$
\mathcal S(n)=\sum_jc_j(n)\mathcal D_j(n),\qquad
\mathcal D_j(n)
 :=\prod_{\ell=1}^K\mathcal C_{h_{j,\ell}(n)}(n).       \tag{1.8}
$$



The conservative residual height is



$$
H_\Sigma(n)
 :=\log\left(\sum_j|c_j(n)|\mathcal A_j(n)\right).      \tag{1.9}
$$



It does not take credit for archimedean cancellation.

Let $Q$ be any target divisor of $q_n$.  In particular, $Q$ may
be any explicitly declared surviving target inside



$$
\overline q_{m,n}={q_n\over\gcd(q_n,D_m)}.              \tag{1.10}
$$



For a nonzero residual $\mathcal R(n)$, put



$$
B(n)=\gcd_j|c_j(n)\mathcal A_j(n)|,                     \tag{1.11}
$$





$$
G_0=\gcd(Q,B),\qquad
G_\Sigma=\gcd(Q,\mathcal R),\qquad
\mathcal X_\Sigma={G_\Sigma\over G_0}.                 \tag{1.12}
$$



The factor $G_0$ is the common product/coefficient baseline.
$\mathcal X_\Sigma$ is the genuinely sum-only cancellation quotient.

> **PROVED — exact cancellation invariant.**
> 

$$
> \boxed{
> \gcd(Q,\mathcal S)=\gcd(Q,\mathcal R),\qquad
> \mathcal X_\Sigma\mid{\mathcal R\over B}.}            \tag{1.13}
>
$$



> **PROVED — uniform height ceiling for the whole declared class.**
> 

$$
> \boxed{
> \log\mathcal X_\Sigma
> \le\log\left|{\mathcal R\over B}\right|
> \le
> \log\left(
> {\sum_j|c_j|\mathcal A_j\over B}
> \right)
> =O(n).}                                               \tag{1.14}
>
$$



If the sum forces the entire target, $Q\mid\mathcal R$, then



$$
\boxed{
{Q\over G_0}\mid{\mathcal R\over B},\qquad
\log{Q\over G_0}=O(n).}                                \tag{1.15}
$$



Thus a bounded homogeneous sum can close only an $O(n)$-height
leftover after the common product baseline.  It cannot add an
$n\log n$-scale cancellation factor.

At the Item-265 beta saddle,



$$
{n\log n\over6m}\longrightarrow\theta>0,
$$



so



$$
{O(n)\over6m}=O(1/\log n)\longrightarrow0.             \tag{1.16}
$$



The sum-only quotient therefore has zero Route-1 rate.  Its local
logarithm may still be a positive constant times $n$; no stronger
uniform $o(n)$ statement is claimed.

The baseline $G_0$ remains an Item-282 product-return channel.  No
theorem here bounds it by $O(n)$.  Consequently the full beta problem
does not close and booking remains zero.

There is also an exact fixed-identity dichotomy.

* If $\mathcal R(n)\ne0$, then its height is $O(n)$, whereas
  $\log q_n=n\log n+O(n)$.  Hence for all sufficiently large such
  $n$,
  

$$
q_n\nmid\mathcal R(n),\qquad q_n\nmid\mathcal S(n).   \tag{1.17}
$$


  A nonzero bounded-height residual identity cannot force full
  $q_n$-divisibility.
* If $\mathcal R(n)=0$, homogeneity gives
  $q_n\mid\mathcal S(n)$, but the residual is zero and supplies no
  nonzero integer whose height bounds $q_n$.  This is a syzygy, not
  an admissible height certificate.

Proper target divisibility is not excluded.  When it occurs, equations
(1.13)–(1.15) identify and bound its genuinely additive part exactly.

## 2. Residual height with moving gaps

Item 276 proved



$$
(4n+6)^{h-1}\le P_h(n)
\le\{4(n+h)\}^{h-1}.                                   \tag{2.1}
$$



For a monomial (1.4), multiplication gives



$$
\log\mathcal A_j(n)
\le L_j(n)\log\{4(n+L_j(n)+1)\}.                       \tag{2.2}
$$



By (1.5),



$$
L_j(n)=O(n/\log n),\qquad
\log\{4(n+L_j(n)+1)\}=O(\log n),
$$



and therefore



$$
\boxed{\log\mathcal A_j(n)=O(n)}                       \tag{2.3}
$$



uniformly over $j$.  Fixed sparsity and (1.6) now give



$$
\boxed{H_\Sigma(n)=O(n).}                              \tag{2.4}
$$



This is why gaps may move throughout the full $O(n/\log n)$ residual
height budget without leaving the theorem.

No lower bound for $|\mathcal R|$ is used.  The cancellation quotient
is normalized by the exact common divisor $B$, so even large common
product factors do not contaminate the sum-only height.

## 3. Homogeneous scalar reduction

The one-factor congruence is



$$
\mathcal C_h(n)
\equiv-P_h(n)q_{n+1}^{\,2}\pmod {q_n}.                 \tag{3.1}
$$



Every monomial has the same total degree $K$.  Hence, modulo every
$Q\mid q_n$,



$$
\mathcal D_j(n)
\equiv
\bigl(-q_{n+1}^{\,2}\bigr)^K\mathcal A_j(n)\pmod Q.     \tag{3.2}
$$



Summing gives



$$
\boxed{
\mathcal S(n)
\equiv
\bigl(-q_{n+1}^{\,2}\bigr)^K\mathcal R(n)\pmod Q.}      \tag{3.3}
$$



Adjacent beta denominators are coprime, so the displayed boundary factor
is a unit modulo $Q$.  Therefore



$$
\gcd(Q,\mathcal S)=\gcd(Q,\mathcal R),                 \tag{3.4}
$$



which is the first half of (1.13).

This common-unit reduction is precisely why homogeneity is required.
For nonhomogeneous sums, different monomial degrees carry different
powers of $q_{n+1}^{\,2}$.  They may still cancel, but no single
primitive residual sum (1.7) controls them.  That class remains open.

## 4. Exact cancellation quotient

Because $B$ divides every term in (1.7), write



$$
c_j\mathcal A_j=BT_j,\qquad
\mathcal R=BR',                                        \tag{4.1}
$$



with $T_j,R'\in\mathbb Z$ and



$$
R'=\sum_jT_j.
$$



Let $p^s\Vert Q$, put $u=v_p(B)$, and put
$v=v_p(R')$.  Then



$$
v_p(G_\Sigma)=\min\{s,u+v\},\qquad
v_p(G_0)=\min\{s,u\}.                                  \tag{4.2}
$$



Their difference is



$$
v_p(\mathcal X_\Sigma)
=
\begin{cases}
0,&s\le u,\\
\min\{s-u,v\},&s>u.
\end{cases}                                            \tag{4.3}
$$



In both cases



$$
v_p(\mathcal X_\Sigma)\le v_p(R').
$$



Therefore



$$
\boxed{\mathcal X_\Sigma\mid R'={\mathcal R\over B},}   \tag{4.4}
$$



proving the second half of (1.13).

The triangle inequality gives



$$
\left|{\mathcal R\over B}\right|
\le{\sum_j|c_j|\mathcal A_j\over B}.                   \tag{4.5}
$$



Combining (2.4), (4.4), and (4.5) proves (1.14).

If $Q\mid\mathcal R$, then $G_\Sigma=Q$, so



$$
\mathcal X_\Sigma={Q\over G_0}.
$$



Equation (4.4) then proves (1.15).  This is the exact actual-family
implication: a forced target splits into a common product baseline and
an $O(n)$-height cancellation leftover.

## 5. Tied minima are the only additive source

Fix $p^s\Vert Q$, and for nonzero terms put



$$
u_j=v_p(c_j\mathcal A_j),\qquad u=\min_j u_j.           \tag{5.1}
$$



The exponent $u$ is exactly $v_p(B)$.

If the minimum occurs at a unique index $j_0$, then after division by
$p^u$, the $j_0$-term is a unit and every other term is divisible by
$p$.  Hence



$$
\boxed{v_p(\mathcal R)=u.}                             \tag{5.2}
$$



The sum adds no depth and $p\nmid\mathcal X_\Sigma$.

If at least two terms attain $u$, then



$$
v_p(\mathcal R)
=u+v_p\!\left(
\sum_j{c_j\mathcal A_j\over p^u}
\right).                                               \tag{5.3}
$$



The second term may be positive.  This is the tied-minimum cancellation
branch.  Equations (4.3)–(4.5) show that all of its target contribution,
across all primes simultaneously, is contained in the one explicit
integer $\mathcal R/B$.

In particular, even if every monomial is a $p$-unit, two or more unit
terms may cancel modulo $p$.  A sum can touch a prime which no selected
return sees.  The theorem does not deny that phenomenon; it proves that
its entire normalized contribution has only $O(n)$ logarithmic height.

## 6. The product baseline is not new sum information

The common baseline is



$$
G_0=\gcd(Q,B).
$$



For every nonzero term,



$$
G_0\mid\gcd(Q,c_j\mathcal A_j).                        \tag{6.1}
$$



Prime by prime,



$$
\gcd(Q,c_j\mathcal A_j)
\mid\gcd(Q,c_j)\gcd(Q,\mathcal A_j).                   \tag{6.2}
$$



The coefficient contribution has logarithm at most



$$
\log|c_j|=O(\log n).
$$



The other factor is exactly an Item-282 product-return capture.  Thus
$G_0$ contains no new additive cancellation information: up to an
$O(\log n)$ fixed-coefficient factor, it lies in the already isolated
product channel.

It follows that a bounded homogeneous sum cannot repair failure of the
weighted-return cover merely by reclassifying the same common factor.
The only genuinely new object is $\mathcal X_\Sigma$, already bounded
by (1.14).

## 7. Fixed algebraic identities and target divisibility

The beta height is



$$
\log q_n=n\log n+(\log4-1)n+O(\log n).                 \tag{7.1}
$$



Suppose $\mathcal R(n)\ne0$.  Equations (1.9) and (2.4) give



$$
\log|\mathcal R(n)|\le H_\Sigma(n)=O(n).               \tag{7.2}
$$



For all sufficiently large $n$, (7.1)–(7.2) imply



$$
0<|\mathcal R(n)|<q_n.
$$



Thus $q_n\nmid\mathcal R(n)$.  Equation (3.4), with $Q=q_n$, also
gives $q_n\nmid\mathcal S(n)$.  This proves the nonzero branch of
(1.17).

If instead a formal or moving identity makes



$$
\mathcal R(n)=0,                                       \tag{7.3}
$$



then (3.3) gives $q_n\mid\mathcal S(n)$.  But the residual integer in
(7.3) is zero.  The divisibility does not imply



$$
q_n\le|\mathcal R(n)|
$$



and therefore supplies no height bound.  If the scalar sum also
vanishes, the identity is completely tautological; if it does not, its
own unnormalized height must be analyzed and is not the $O(n)$
residual certificate considered here.

For a proper target $Q$, a prime-independent identity or congruence may
force $Q\mid\mathcal R$.  The theorem does not rule this out.  It
forces the exact consequence



$$
{Q\over\gcd(Q,B)}\mid{\mathcal R\over B},               \tag{7.4}
$$



whose logarithmic height is $O(n)$.  Thus no fixed identity in the
declared class can hide an additional $n\log n$-scale sum-only factor.

Allowing coefficients chosen from the factorization of $Q$, the
target prime, or $v_p(q_n)$ would make such congruences tautological
and is excluded from admission.

## 8. Item-265 capacity implication

Choose any declared target



$$
Q\mid\overline q_{m,n}.
$$



The factorization



$$
\gcd(Q,\mathcal S)
=G_0\mathcal X_\Sigma                                  \tag{8.1}
$$



is exact.  Its two parts have different status.

1. $G_0$ is product-return capture plus at most $O(\log n)$ of
   coefficient height.  It remains governed by Item 282's open
   high-efficiency/weighted-cover lemma.
2. $\mathcal X_\Sigma$ is the entire sum-only contribution and has
   $\log\mathcal X_\Sigma=O(n)=o(n\log n)$.

Therefore bounded-complexity homogeneous sums create no new positive
Route-1 rate beyond the product baseline.  A locally linear
$\log\mathcal X_\Sigma\asymp n$ is not excluded, but equation (1.16)
shows that it has zero rate at the balanced global normalization.

No strict improvement to the Item-265 high-singleton ceiling follows,
because $G_0$ can still carry the unresolved product mass.

## 9. Strict labels

### PROVED

* The $O(n)$ residual height for the full declared moving-gap class.
* The homogeneous scalar/residual reduction (3.3)–(3.4).
* The exact cancellation invariant
  $\mathcal X_\Sigma\mid\mathcal R/B$.
* The uniform $O(n)$ logarithmic ceiling for all sum-only capacity.
* The forced-target implication $Q/G_0\mid\mathcal R/B$.
* The unique-minimum theorem and tied-minimum split.
* The nonzero/zero fixed-identity dichotomy.
* The product-baseline decomposition and Item-265 de-overlap.

### PROVED SCOPED NO-GO

* No nonzero bounded-height residual in the declared class can force
  full $q_n$-divisibility for all large $n$.
* An identically zero residual identity gives no height certificate.
* Bounded-complexity homogeneous sums cannot add an
  $n\log n$-scale factor beyond their common product baseline.
* Hence their genuinely additive contribution has zero Route-1 rate.

### EXACT FINITE ONLY

* The deterministic checker replays moving-gap monomial heights,
  homogeneous scalar reduction, cancellation divisibility, target
  implication, unique/tied minima, and the zero-identity branch.
* Its cancellation examples are algebraic witnesses only, not a density
  statement or exceptional-prime census.

### OPEN

* The Item-282 common product baseline and weighted-return cover.
* Nonhomogeneous sums with different boundary-unit powers.
* Unbounded sparsity or total degree, arbitrary block/Hankel
  determinants, and target-independent constructions outside this
  class.
* The uniform prime-power-height or little-oh squarefull theorem and the
  clearing/transverse matching correlation.
* Route 1 and every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}                 \tag{9.1}
$$



## 10. Deterministic replay

From the archive root:

~~~text
python scripts/item283_beta_bounded_homogeneous_sum_certificate.py ^
  --output results/item283_beta_bounded_homogeneous_sum_certificate_replay.json
~~~

The checker is Python-standard-library only, deterministic, and uses
exact integer arithmetic.  The canonical result and replay must be
byte-identical.
