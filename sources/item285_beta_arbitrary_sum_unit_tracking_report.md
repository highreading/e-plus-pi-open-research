> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 285 — arbitrary-sum cancellation and exact boundary-unit tracking

Checked: 2026-08-31 (Beijing time)

## 1. Verdict

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
\mathcal C_h(n)=q_nq_{n+h+1}-q_{n+1}q_{n+h}.           \tag{1.3}
$$



Item 283 imposed bounded sparsity and bounded total degree only to prove
its conservative residual height bound.  Neither hypothesis is needed
by the cancellation-divisor argument itself.

> **PROVED — arbitrary-complexity normalized-sum theorem.**
> Let $\{T_j(n)\}_{j\in J_n}$ be any finite nonempty collection of
> nonzero integers.  The cardinality of $J_n$, the algebraic degrees,
> and all internal gaps may grow arbitrarily.  Put
> 

$$
> R=\sum_{j\in J_n}T_j,\qquad
> B=\gcd_{j\in J_n}|T_j|,                               \tag{1.4}
>
$$


> and assume $R\ne0$.  For every positive integer target $Q$, set
> 

$$
> G_0=\gcd(Q,B),\qquad G=\gcd(Q,R),\qquad X={G\over G_0}.
>
$$


> Then
> 

$$
> \boxed{X\mid {R\over B}.}                             \tag{1.5}
>
$$


> In particular, the explicit conservative-height assumption
> 

$$
> H_{\rm norm}(n):=
> \log\!\left({\sum_j|T_j(n)|\over B(n)}\right)=O(n)    \tag{1.6}
>
$$


> implies
> 

$$
> \boxed{\log X=O(n)=o(n\log n).}                       \tag{1.7}
>
$$



This is the broadest sum class closed here: arbitrary sparsity and
degree, conditional only on a nonzero normalized residual and the
stated conservative $O(n)$ height.  For capacity admission the terms
must still be specified independently of the target factorization and
unknown prime-adic depths; otherwise (1.6) can be made tautological.

For a forced target $Q\mid R$, equation (1.5) becomes the exact
actual-family implication



$$
\boxed{
{Q\over\gcd(Q,B)}\mid {R\over B},\qquad
\log {Q\over\gcd(Q,B)}=O(n).}                           \tag{1.8}
$$



Thus all genuinely additive capture beyond the common baseline has
only $O(n)$ logarithmic height.  The baseline itself remains the
Item-282 product-return channel.

For nonhomogeneous Casoratian sums, exact unit tracking produces a
polynomial in the boundary unit



$$
u_n=-q_{n+1}^{\,2}\pmod Q.                             \tag{1.9}
$$



Two exact conditional closures are proved:

1. a small integer lift $v\equiv u_n\pmod Q$ whose evaluated
   normalized $\ell^1$-height is $O(n)$; or
2. a monic integer annihilator $M(u_n)\equiv0\pmod Q$ whose nonzero
   resultant with the normalized residual polynomial has logarithmic
   height $O(n)$.

Either condition forces the same $O(n)$ cancellation ceiling.  The
canonical lift $v=-q_{n+1}^2$, and equivalently the tautological
annihilator $M(U)=U+q_{n+1}^2$, cost



$$
2\log q_{n+1}=2n\log n+O(n),                           \tag{1.10}
$$



so they are not admissible $O(n)$-height certificates.

Multiplication by powers of $\mathcal C_1$ can homogenize a
*newly designed* scalar sum at no residual cost because $P_1=1$.
It changes $F(u_n)$ to $F(1)$, however, and therefore does not
transport divisibility of the original nonhomogeneous sum.

No low-height lift or annihilator is presently proved for the actual
family.  No common-product baseline theorem is added.  Hence booking is
zero.

## 2. Universal cancellation quotient

Because $B\mid T_j$ for every $j$, write



$$
T_j=Bt_j,\qquad R=Br,\qquad r=\sum_jt_j.                \tag{2.1}
$$



Let $p^s\Vert Q$, put $b=v_p(B)$, and put $a=v_p(r)$.
Since $B\mid R$, $G_0\mid G$, and



$$
v_p(X)
=\min\{s,b+a\}-\min\{s,b\}
=
\begin{cases}
0,&s\le b,\\
\min\{s-b,a\},&s>b.
\end{cases}                                             \tag{2.2}
$$



Thus $v_p(X)\le v_p(r)$ for every prime $p$, proving



$$
X\mid r={R\over B}.                                    \tag{2.3}
$$



The triangle inequality gives



$$
\left|{R\over B}\right|
\le{\sum_j|T_j|\over B}.                               \tag{2.4}
$$



Equations (2.3)–(2.4) prove (1.5)–(1.7), with no use of
the size of $J_n$, monomial degree, recurrence order, or gap pattern.

If $R=0$, divisibility may hold identically, but there is no nonzero
integer $R/B$ whose height bounds $X$.  As in Item 283, this is a
syzygy branch, not a height certificate.  The theorem deliberately
requires $R\ne0$.

## 3. Item-265 de-overlap and product baseline

Let $D_m$ denote the relevant two-copy clearing reservoir from
Item 265, and put



$$
\overline q_{m,n}={q_n\over\gcd(q_n,D_m)}.              \tag{3.1}
$$



Every theorem in this report holds for an arbitrary declared target



$$
Q\mid\overline q_{m,n}.                                \tag{3.2}
$$



This removes the clearing overlap before sum capacity is measured.
For any residual terms $T_j$,



$$
G_0=\gcd(Q,B)\mid\gcd(Q,T_j)                           \tag{3.3}
$$



for every $j$.  In a continuant monomial, this is common
coefficient/product capture.  It is not new additive information and
remains within the Item-282 weighted-return problem.

The new additive factor is exactly



$$
X={\gcd(Q,R)\over\gcd(Q,B)}.                            \tag{3.4}
$$



Under (1.6), it has $O(n)$ logarithmic height.  At the Item-265 beta
saddle,



$$
{n\log n\over6m}\longrightarrow\theta>0,
$$



so



$$
{\log X\over6m}=O(1/\log n)\longrightarrow0.            \tag{3.5}
$$



The sum-only quotient has zero normalized Route-1 rate.  Equation
(3.5) says nothing new about the unresolved baseline $G_0$.

## 4. Exact nonhomogeneous boundary-unit polynomial

Let



$$
\mathcal A_j(n)=\prod_{\ell=1}^{k_j}P_{h_{j,\ell}}(n),
\qquad
\mathcal D_j(n)=\prod_{\ell=1}^{k_j}\mathcal C_{h_{j,\ell}}(n), \tag{4.1}
$$



where the degrees $k_j$ need not agree.  Let $c_j(n)\in\mathbb Z$
and define



$$
\mathcal S(n)=\sum_jc_j\mathcal D_j.                    \tag{4.2}
$$



The one-factor identity is



$$
\mathcal C_h(n)\equiv
-P_h(n)q_{n+1}^{\,2}\pmod {q_n}.                        \tag{4.3}
$$



Adjacent beta denominators are coprime, hence



$$
u:=-q_{n+1}^{\,2}                                      \tag{4.4}
$$



is a unit modulo every $Q\mid q_n$.  Put



$$
k_0=\min_jk_j,\qquad e_j=k_j-k_0,
\qquad a_j=c_j\mathcal A_j,                             \tag{4.5}
$$



and form the grouped polynomial



$$
F(U)=\sum_ja_jU^{e_j}\in\mathbb Z[U].                  \tag{4.6}
$$



Equal powers may be combined; leaving them uncombined gives the same
evaluation.  Multiplying (4.3) over each monomial gives



$$
\boxed{
\mathcal S\equiv u^{k_0}F(u)\pmod Q.}                   \tag{4.7}
$$



Since $u^{k_0}$ is a unit,



$$
\boxed{\gcd(Q,\mathcal S)=\gcd(Q,F(u)).}                \tag{4.8}
$$



Here $F(u)$ means evaluation at any integer representative of the
residue class $u\pmod Q$; the gcd in (4.8) is independent of that
choice.

Set



$$
B=\gcd_j|a_j|.                                         \tag{4.9}
$$



This is the original coefficient/product baseline, before grouping
equal degrees.  It divides every coefficient of $F$.  Consequently



$$
F_0(U):={F(U)\over B}\in\mathbb Z[U].                  \tag{4.10}
$$



No content-primitivity assumption is imposed on $F_0$.  Any extra
common content created by cancellation inside one homogeneous degree
slice is itself additive residual information, not silently moved into
the product baseline.

## 5. Small-unit-lift criterion

Let $v\in\mathbb Z$ satisfy



$$
v\equiv u\pmod Q,\qquad \gcd(v,Q)=1.                   \tag{5.1}
$$



Then (4.8) becomes



$$
\gcd(Q,\mathcal S)=\gcd(Q,F(v)).                       \tag{5.2}
$$



Assume $F(v)\ne0$, and define the conservative evaluated height



$$
H_v:=
\log\!\left(
{\sum_j|a_j|\,|v|^{e_j}\over B}
\right).                                               \tag{5.3}
$$



Apply Section 2 to the integer terms $a_jv^{e_j}$.  Because $v$ is
a $Q$-unit, their common $Q$-baseline is still
$\gcd(Q,B)$.  Therefore



$$
\boxed{
X_v:={\gcd(Q,\mathcal S)\over\gcd(Q,B)}
\mid {F(v)\over B}.}                                   \tag{5.4}
$$



If $H_v=O(n)$, then



$$
\boxed{\log X_v=O(n).}                                 \tag{5.5}
$$



If $Q\mid\mathcal S$, the exact target consequence is



$$
\boxed{
{Q\over\gcd(Q,B)}\mid {F(v)\over B}.}                  \tag{5.6}
$$



This closes arbitrary sparsity, degree, and moving gaps whenever the
evaluated normalized height (5.3) is proved $O(n)$.

The canonical integer representative is



$$
v_0=-q_{n+1}^{\,2}.                                    \tag{5.7}
$$



If the sum is genuinely nonhomogeneous, some $e_j\ge1$.  Since
$|a_j|/B$ is a positive integer,



$$
H_{v_0}\ge\log|v_0|
=2\log q_{n+1}
=2n\log n+O(n).                                       \tag{5.8}
$$



Thus the direct canonical lift spends the very $n\log n$ height that
the argument must save.  Choosing the symmetric least residue may be
much smaller for individual targets, but no uniform actual-family
$O(n)$ bound for that residue is known.

## 6. Laurent tracking does not remove the lift cost by itself

One may instead factor the largest boundary power.  If
$d=\max_je_j$, equation (4.7) can be written using



$$
\widetilde F(V)=V^dF(V^{-1})                           \tag{6.1}
$$



and the inverse unit $u^{-1}\pmod Q$.  This is an exact Laurent
reparametrization.  It does not by itself create a small integer
representative of $u^{-1}$, nor a small denominator clearing.

Evaluating at the canonical integer $v_0$ and clearing the negative
powers multiplies by $v_0^d$, again costing at least



$$
d\log|v_0|=\Omega(n\log n)                             \tag{6.2}
$$



when $d\ge1$.  A separately proved small lift of $u^{-1}$, or a
low-height algebraic relation for it, would be admissible; it is not a
consequence of Laurent notation alone.

## 7. Designed homogenization with $\mathcal C_1$

Because



$$
P_1(n)=1,\qquad \mathcal C_1(n)\equiv u\pmod Q,         \tag{7.1}
$$



put $K=\max_jk_j$ and define a new scalar sum



$$
\mathcal S^{\rm hom}
:=\sum_jc_j\mathcal D_j\mathcal C_1^{\,K-k_j}.          \tag{7.2}
$$



Every term now has total Casoratian degree $K$, while its residual
monomial is still $\mathcal A_j$.  Hence



$$
\boxed{
\mathcal S^{\rm hom}
\equiv u^K\sum_ja_j
=u^KF(1)\pmod Q.}                                      \tag{7.3}
$$



This is exact, uses no extra continuant height, and allows Section 2 or
Item 283 to control the newly designed homogeneous sum whenever
$\sum_ja_j\ne0$ has normalized height $O(n)$.

But the original sum is controlled by $F(u)$, whereas (7.3) is
controlled by $F(1)$.  In general,



$$
Q\mid F(u)\quad\not\Longrightarrow\quad Q\mid F(1),    \tag{7.4}
$$



and the converse also fails.  Thus $\mathcal C_1$-homogenization is a
valid construction tool only when one is free to replace the scalar
sum.  It is not a certificate for an already given nonhomogeneous
collision.  The deterministic checker contains exact actual-sequence
witnesses where the two target captures differ; these witnesses refute
a universal transfer but are not used as asymptotic evidence.

## 8. Low-height annihilator and resultant criterion

The direct lift is the degree-one case of a broader exact closure.
Let



$$
M(U)\in\mathbb Z[U]                                    \tag{8.1}
$$



be monic and specified independently of the factorization of $Q$,
with



$$
M(u)\equiv0\pmod Q.                                    \tag{8.2}
$$



Retain $F_0=F/B$ from (4.10), and define



$$
\Delta=\operatorname{Res}_U(M,F_0)\in\mathbb Z.        \tag{8.3}
$$



Let $p^s\Vert Q$ and $p^x\Vert X_v$, where $X_v$ denotes the
quotient in (5.4), equivalently defined directly by (4.8).  If $x>0$,
then modulo $p^x$,



$$
M(u)=0,\qquad F_0(u)=0.                                \tag{8.4}
$$



The integral Sylvester-Bézout identity



$$
A(U)M(U)+C(U)F_0(U)=\Delta                             \tag{8.5}
$$



evaluated at an integer representative of $u$ gives



$$
p^x\mid\Delta.
$$



Prime by prime,



$$
\boxed{X_v\mid\Delta.}                                 \tag{8.6}
$$



No choice of a small integer representative is needed.

If $\Delta\ne0$ and



$$
\log|\Delta|=O(n),                                     \tag{8.7}
$$



then



$$
\boxed{\log X_v=O(n).}                                 \tag{8.8}
$$



If $Q\mid\mathcal S$, then



$$
\boxed{{Q\over\gcd(Q,B)}\mid\Delta.}                   \tag{8.9}
$$



A convenient conservative sufficient condition for (8.7) is the
standard resultant norm bound.  If



$$
r=\deg M,\qquad d=\deg F_0,
$$



then



$$
|\Delta|
\le\|M\|_2^{\,d}\|F_0\|_2^{\,r}.                      \tag{8.10}
$$



Thus



$$
d\log\|M\|_2+r\log\|F_0\|_2=O(n)                      \tag{8.11}
$$



is sufficient.  This formulation permits growing degree, sparsity, or
coefficient sets as long as their total conservative resultant budget
is $O(n)$.

If $\Delta=0$, $M$ and $F_0$ have a common algebraic factor.  The
zero resultant contains no nonzero integer height certificate.  A
quotient, subresultant, or separate identity analysis would be needed;
no automatic capacity bound is claimed.

The tautological annihilator



$$
M_0(U)=U+q_{n+1}^{\,2}                                 \tag{8.12}
$$



satisfies (8.2) even as an integer identity, but



$$
\log\|M_0\|_2=2n\log n+O(n).                           \tag{8.13}
$$



It fails (8.11), exactly as the canonical lift fails (5.3).

## 9. Why formal coefficient height is insufficient

A small formal coefficient list does not control evaluation at a
moving residue class.  Abstractly, for a modulus $Q$ and a unit $u$,



$$
F(U)=U^{\varphi(Q)}-1                                  \tag{9.1}
$$



has coefficient $\ell^1$-norm $2$, yet



$$
F(u)\equiv0\pmod Q.                                    \tag{9.2}
$$



The target dependence has merely moved into the degree
$\varphi(Q)$.  This is not an admitted beta construction: it depends
on $Q$ and its arithmetic, and its evaluation/degree budget is not
$O(n)$.  It is an exact logical warning that coefficient height alone
cannot replace (5.3) or (8.11).

The same issue affects a sum of many low-looking Laurent terms:
unbounded sparsity or exponents can encode the modulus unless the
normalized evaluated height or resultant budget is explicitly bounded.
Section 2 closes arbitrary complexity only after that budget is proved.

## 10. First remaining admissible construction

After the preceding theorems, the first open nonhomogeneous
construction can be stated exactly.

For the actual residual polynomial $F_n$ and a declared
de-overlapped target $Q\mid\overline q_{m,n}$, produce one of:

1. an integer $v_n$, specified without target factorization, such
   that
   

$$
v_n\equiv-q_{n+1}^2\pmod Q,\quad
   \gcd(v_n,Q)=1,\quad
   F_n(v_n)\ne0,
$$


   and
   

$$
\log\!\left(
   {\sum_j|a_{j,n}|\,|v_n|^{e_{j,n}}\over B_n}
   \right)=O(n);                                      \tag{10.1}
$$


   or
2. a monic $M_n\in\mathbb Z[U]$, specified without target
   factorization, such that
   

$$
M_n(-q_{n+1}^2)\equiv0\pmod Q,
$$


   

$$
\operatorname{Res}(M_n,F_n/B_n)\ne0,
$$


   and the conservative budget (8.11) is $O(n)$.      \tag{10.2}

Either is immediately admissible for the sum-only quotient by Sections
5 or 8.  Neither is currently known.  A proof only for the canonical
lift or $M_0$ is not enough, because both cost $n\log n$.

Even success would close only the additive quotient



$$
{\gcd(Q,\mathcal S)\over\gcd(Q,B)}.                    \tag{10.3}
$$



The common product baseline $\gcd(Q,B)$ would still require the
Item-282 weighted-return theorem.  Therefore Item 285 does not by itself
reduce the full beta capacity.

## 11. Strict labels

### PROVED

* The arbitrary-sparsity, arbitrary-degree cancellation theorem
  $X\mid R/B$.
* The $O(n)$ cancellation ceiling under the explicit normalized
  conservative-height assumption (1.6).
* The exact forced-target implication (1.8).
* The Item-265 de-overlap and common product-baseline separation.
* The nonhomogeneous boundary-unit polynomial reduction
  (4.7)–(4.8).
* The small-unit-lift criterion (5.4)–(5.6).
* The exact $\mathcal C_1$-homogenization formula (7.3), and its
  limitation to the newly designed sum.
* The annihilator-resultant divisibility (8.6) and its $O(n)$-height
  closure (8.8)–(8.11).

### PROVED SCOPED NO-GO / BARRIER

* The canonical integer unit lift has conservative height
  $\Omega(n\log n)$ for every genuinely nonhomogeneous sum.
* The tautological degree-one annihilator has coefficient height
  $2n\log n+O(n)$.
* Formal coefficient height alone cannot bound unit evaluation; degree,
  evaluated height, or a resultant budget must be charged.
* $\mathcal C_1$-homogenization does not transfer an arbitrary
  original $F(u)$ collision to $F(1)$.
* These statements are not a no-go for a new low-height lift,
  annihilator, or algebraic relation.

### EXACT FINITE ONLY

* The deterministic checker replays the arbitrary-term quotient,
  unequal-degree actual Casoratian reduction, symmetric unit lifts,
  designed homogenization, non-transfer witnesses, Sylvester
  resultants, zero-resultant identities, and formal degree warnings.
* No exceptional-prime census or asymptotic extrapolation is performed.

### OPEN

* An actual-family low-height unit lift satisfying (10.1).
* An actual-family low-height annihilator/resultant satisfying (10.2).
* Nonhomogeneous sums without either certificate.
* The Item-282 common product baseline and weighted-return cover.
* The uniform beta prime-power-height or little-oh squarefull theorem.
* The clearing/transverse matching correlation, Route 1, and every
  conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new Route-1 rate}=0,\qquad
\text{new beta capacity reduction}=0.}                 \tag{11.1}
$$



## 12. Deterministic replay

From the archive root:

~~~text
python scripts/item285_beta_arbitrary_sum_unit_tracking_certificate.py ^
  --output results/item285_beta_arbitrary_sum_unit_tracking_certificate_replay.json
~~~

The checker is Python-standard-library only, deterministic, and uses
exact integer arithmetic.  The canonical result and replay must be
byte-identical.
