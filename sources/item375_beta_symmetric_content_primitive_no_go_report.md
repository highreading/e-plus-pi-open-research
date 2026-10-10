> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 375 — content normalization closes the constant symmetric loophole

Checked: 2026-09-01 (Beijing time)

## 1. Verdict and admission

Item 373 reduces every bounded-degree top-symmetric first quotient with a
nonconstant univariate numerator to beta-scale height on a positive-singleton-
mass subsequence.  Its only formally sub-beta exception was a
constant/coefficient-content numerator.  Item 375 closes that exception as a
**symmetric mechanism**.

Let a prime-independent rational residual built from the actual symmetric
integers



$$
P=\prod_{j\in\mathcal J}Z_j,
\qquad
E=e_{N-1}(Z)=\sum_j P/Z_j
\tag{1.1}
$$



be represented by $A(P,E)/B(P,E)$.  Normalize the representation by integer
content, cancel the primitive polynomial gcd, and reduce the remaining scalar
ratio.  If the reduced numerator has constant primitive part, then that part
is necessarily $\pm1$.  Hence at every genuine $t$-away singleton prime where
the denominator is a unit, the residual valuation is exactly the valuation of
one reduced scalar integer $\alpha$.

The fully saturated content carrier is therefore



$$
\mathcal C_{\rm cont}
=\gcd\!\left(\mathcal U_{1,1},\operatorname{rad}|\alpha|\right),
\qquad
\log\mathcal C_{\rm cont}\le \log|\alpha|.
\tag{1.2}
$$



Consequently:

1. if the total reduced scalar numerator height is $b^{o(1)}$, its captured
   singleton mass is $o(\log b)$;
2. if the captured content mass is at least $\eta\log b$, then necessarily
   $\log|\alpha|\ge\eta\log b$, so the content is already beta-scale;
3. if one quotes only the primitive polynomial height while omitting
   coefficient content, the height is representation-dependent and gives no
   arithmetic bound;
4. after coefficient-content saturation, the remaining primitive numerator
   is $\pm1$ and captures no prime.

Thus no admissible positive-linear carrier exists in the content-degenerate
class.  A separately proved small scalar $\alpha_n$ with
$\mathcal U_{1,1}(n)\mid\alpha_n$ would still be a genuine zero-rate theorem,
but it would be a new actual arithmetic correlation, not a consequence of the
symmetric variables.  No such scalar is constructed here.  Booking remains
zero.

## 2. Actual singleton setting

Assume the genuine Item-316 target and use the actual nonzero load set
$\mathcal J$.  Item 373 proves



$$
S^{\rm sym}
=\frac{P}{\gcd(P,(|t|E)^N)}
\tag{2.1}
$$



and, for every prime $p>A$,



$$
v_p(S^{\rm sym})=1
\iff
p\nmid t\ \text{ and }\ \#\{j:p\mid Z_j\}=1.
\tag{2.2}
$$



The genuine externally saturated singleton carrier is



$$
\mathcal U_{1,1}
=\gcd\!\left(Q^{[1]},\operatorname{rad}_{>A}(S^{\rm sym})\right).
\tag{2.3}
$$



If $t=0$, then (2.1) gives $S^{\rm sym}=1$ and hence
$\mathcal U_{1,1}=1$; the branch is already trivial.  In the nontrivial case
below, $t\ne0$.

For every $p\mid\mathcal U_{1,1}$,



$$
v_p(P)=1,
\qquad
p\nmid E.
\tag{2.4}
$$



Thus a first-quotient residual $R(P,E)$ creates an extra digit in
$P R(P,E)$ exactly when $v_p(R(P,E))\ge1$.  Item 375 classifies that condition
when the primitive numerator of $R$ is constant.

## 3. Representation-invariant normalization

Let



$$
R(X,Y)=\frac{A(X,Y)}{B(X,Y)},
\qquad
A,B\in\mathbb Z[X,Y],
\qquad
A B\ne0.
\tag{3.1}
$$



The degrees may be bounded by any fixed constant; the normalization theorem
itself does not require a degree bound.  Write



$$
A=aA_0,
\qquad
B=bB_0,
\qquad
a=\operatorname{cont}(A)>0,
\quad
b=\operatorname{cont}(B)>0,
\tag{3.2}
$$



with $A_0,B_0$ primitive.  Cancel their primitive gcd in
$\mathbb Z[X,Y]$:



$$
A_0=H A_1,
\qquad
B_0=H B_1,
\qquad
\gcd(A_1,B_1)=1,
\tag{3.3}
$$



where Gauss's lemma lets $H,A_1,B_1$ all be chosen primitive up to sign.
Finally put



$$
g=\gcd(a,b),
\qquad
\alpha=a/g,
\qquad
\beta=b/g.
\tag{3.4}
$$



Then



$$
\boxed{
R(X,Y)=\frac{\alpha A_1(X,Y)}{\beta B_1(X,Y)},
\quad
\gcd(\alpha,\beta)=1,
\quad
A_1,B_1\text{ primitive and coprime}.}
\tag{3.5}
$$



This reduced scalar ratio and reduced primitive pair are independent of
multiplying the original numerator and denominator by a common nonzero
integer or primitive polynomial, up to simultaneous signs.

Call (3.5) **numerator-content-degenerate** if $A_1$ is constant.  A constant
primitive integer polynomial is $\pm1$, so the whole class is exactly



$$
\boxed{
R(X,Y)=\frac{\pm\alpha}{\beta B_1(X,Y)},
\qquad
B_1\text{ primitive}.}
\tag{3.6}
$$



If the entire variable part is constant, then coprimality additionally forces
$B_1=\pm1$, and $R=\pm\alpha/\beta$.

This is the requested characterization.  Syntactically complicated
cancellations do not create another case: after exact cancellation they land
in (3.6), or their reduced numerator remains nonconstant and lies outside the
constant/content branch.

## 4. Exact singleton valuation theorem

Fix $p\mid\mathcal U_{1,1}$ and assume the reduced denominator is a $p$-unit
at the actual point:



$$
p\nmid \beta B_1(P,E).
\tag{4.1}
$$



This unit condition is compulsory; a vanishing denominator gives no defined
first quotient.  From (3.6),



$$
\boxed{v_p(R(P,E))=v_p(\alpha).}
\tag{4.2}
$$



Together with $v_p(P)=1$, this gives



$$
\boxed{
v_p(P R(P,E))\ge2
\iff
p\mid\alpha.}
\tag{4.3}
$$



No value of $P$, $E$, the denominator, or the canonical word contributes a
new numerator zero inside this class.  The exact set captured after all
already mandatory filters is



$$
\begin{aligned}
\mathcal C_{\rm cont}
&=\gcd\!\left(
Q^{[1]},
\operatorname{rad}_{>A}(S^{\rm sym}),
\frac{\operatorname{rad}|\alpha|}
{\gcd(\operatorname{rad}|\alpha|,\operatorname{rad}|t|)}
\right)\\
&=\gcd\!\left(\mathcal U_{1,1},\operatorname{rad}|\alpha|\right).
\end{aligned}
\tag{4.4}
$$



The second equality uses the fact that $\mathcal U_{1,1}$ is already
$t$-away.  In particular, a content-degenerate residual covers every actual
singleton prime only if



$$
\boxed{\mathcal U_{1,1}\mid\operatorname{rad}|\alpha|.}
\tag{4.5}
$$



Replacing the right side by $|\alpha|$ is equivalent because
$\mathcal U_{1,1}$ is squarefree.

## 5. Primitive height versus arithmetic height

The coefficient height of $A_1,B_1$ alone cannot control (4.4).  For every
nonzero integer $c$,



$$
\frac{cA}{cB}=\frac AB
\tag{5.1}
$$



has arbitrarily large displayed contents but the same rational function.
Conversely,



$$
c\frac AB
\tag{5.2}
$$



has the same primitive polynomial pair and an arbitrarily large reduced
scalar numerator.  Thus a height that discards $\alpha$ is not an arithmetic
height for divisibility carriers.

The representation-invariant numerator height relevant to (4.4) must include
$|\alpha|$.  In the mechanism ledger, mandatory coefficient-content
saturation separates this external scalar contribution from the symmetric
primitive factor; it is not an algebraic cancellation that preserves $R$.
The remaining symmetric numerator is $\pm1$ and has valuation zero at every
prime satisfying (4.1).  If the scalar is instead retained and audited as a
separate carrier, its capacity is bounded tautly by



$$
\boxed{
\log\mathcal C_{\rm cont}
\le\log\operatorname{rad}|\alpha|
\le\log|\alpha|.}
\tag{5.3}
$$



Therefore



$$
\log|\alpha|=o(\log b)
\quad\Longrightarrow\quad
\log\mathcal C_{\rm cont}=o(\log b).
\tag{5.4}
$$



More sharply, for every fixed $\eta>0$,



$$
\log\mathcal C_{\rm cont}\ge\eta\log b
\quad\Longrightarrow\quad
\log|\alpha|\ge\eta\log b.
\tag{5.5}
$$



Hence positive-linear content cannot be hidden behind sub-beta primitive
height.  It either disappears under mandatory coefficient-content
saturation, or is paid for by a beta-scale scalar numerator.

## 6. Portfolios and integral carriers

For a finite or growing portfolio $R_1,\ldots,R_L$ in the class (3.6), let
$\alpha_\ell$ be the reduced scalar numerator.  Suppose every actual
singleton prime is captured by at least one defined member.  Equation (4.3)
gives



$$
\boxed{
\mathcal U_{1,1}
\mid
\operatorname{rad}\!\left(\prod_{\ell=1}^L\alpha_\ell\right),
\qquad
\log\mathcal U_{1,1}
\le
\sum_{\ell=1}^L\log|\alpha_\ell|.}
\tag{6.1}
$$



Thus any portfolio with total scalar numerator height $o(\log b)$ is also
zero-rate.  Allowing linearly many individually small contents does not evade
the theorem: their **sum** is the relevant total height, and positive-linear
captured mass forces positive-linear aggregate content height.

If a content-degenerate rational residual is required to be an actual
integer, (3.6) implies



$$
\beta B_1(P,E)\mid\alpha.
\tag{6.2}
$$



This only strengthens the obstruction.  A large variable denominator cannot
compress the numerator; it must already divide the external scalar.

## 7. Admissible and inadmissible scalar branches

There are three exact outcomes.

1. **Primitive saturation.**  Remove the coefficient content.  The numerator
   is $\pm1$, so the captured singleton carrier is $1$.
2. **Retained sub-beta scalar.**  If a new actual theorem proves
   $\mathcal U_{1,1}\mid\alpha_n$ with $0<|\alpha_n|=b^{o(1)}$, then it proves
   the desired zero rate immediately.  Item 375 does not construct such an
   $\alpha_n$.
3. **Retained beta-scale or candidate-built scalar.**  Taking
   $\alpha_n=\mathcal U_{1,1}$, a multiple of it, or a CRT assembly merely
   inserts the target support.  Its height is at least the mass it purports to
   bound, so it supplies no compression.  It is inadmissible as a new
   symmetric gain.

The zero scalar is also inadmissible: it has no nonzero height and makes the
first quotient identically zero without an arithmetic divisibility bound.

## 8. Exact scope and surviving arithmetic

The theorem closes:

* every bounded-degree rational expression in $P,E$ whose reduced primitive
  numerator is constant;
* every symbolic cancellation whose exact reduced numerator becomes
  constant;
* fixed or growing portfolios whose total reduced scalar numerator height is
  sub-beta;
* coefficient content omitted from a claimed primitive-height bound;
* variable $p$-unit denominators and integral specialization as escapes.

It does **not** close:

* a nonconstant primitive polynomial in several symmetric functions whose
  actual canonical value undergoes a one-point arithmetic cancellation;
* beta-height gcd/radical compression of a nonconstant full-support state;
* a genuinely new scalar $\alpha_n$ derived from the canonical word together
  with a proved actual divisibility theorem and a nontrivial height bound;
* the global weighted bound for $\mathcal U_{1,1}$.

Those are arithmetic correlations, not coefficient-content effects.

## 9. Strict labels

### PROVED

* The representation-invariant content/primitive normalization (3.2)-(3.6).
* The exact actual singleton valuation and saturated carrier
  (4.2)-(4.5).
* The content-height capacity bound (5.3)-(5.5).
* The portfolio and integral-specialization bounds (6.1)-(6.2).
* Zero booking.

### PROVED SCOPED NO-GO

* Numerator-content-degenerate bounded-degree symmetric rational carriers as
  a source of positive-linear mass at sub-beta total scalar height.
* Primitive polynomial height with coefficient content omitted as a
  representation-invariant carrier bound.
* Fixed or growing content portfolios with sub-beta aggregate scalar height.
* $p$-unit variable denominators as content compression.

### EXACT FINITE ONLY

* The replay's predeclared sparse-polynomial normalization, scalar valuation,
  saturation, portfolio, and height controls.
* No declared prime, load vector, or scalar is promoted to an actual beta
  target or density datum.

### OPEN

* Nonconstant multivariate symmetric one-point cancellation.
* Beta-height gcd/radical compression and full-support recurrence height.
* A new nonzero sub-beta scalar with a genuine actual
  $\mathcal U_{1,1}$-divisibility theorem.
* The singleton bound, growing low incidence, $\Xi_Q$, squarefull excess,
  beta capacity, Route 1, and $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{9.1}
$$



No canonical, master, status, checkpoint, research-log, or audit file is
edited by this work package.

## 10. Deterministic replay

From the archive root:

~~~text
python work/item375_beta_symmetric_content_primitive_no_go_certificate.py ^
  --output work/item375_beta_symmetric_content_primitive_no_go_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer sparse
polynomials.  All symbolic cases and arithmetic controls are predeclared.  It
performs no actual prime census, factor search, target search, or half-bound
scan.
