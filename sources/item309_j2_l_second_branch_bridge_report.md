> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 309 — the ordinary-$j=2$ $L$-minor and the $y=-1$ algebraic branch

Checked: 2026-08-31 (Beijing time)

## 1. Scope and strict verdict

Retain Items 291, 294, and 306 on



$$
r=6n+e,\qquad e\in\{1,5\},\qquad
 L_r=9\det(f,b),\qquad M_r=-11\det(f,d),
$$



and Item 294's gauge $g_0=1$,



$$
\frac{g_n}{g_{n+1}}=
 \mathcal R(r)=
 \frac{r(r+6)(2r+9)^2(2r+15)^2}
 {78732(r+1)^2(r+2)(r+4)(r+5)^2}.
$$



This item isolates a structurally forced second algebraic branch.

> **PROVED — exact second branch and exact tail-form inversion.**  The
> phase-specialized two $A$-tail one-forms become, after $t=1/z$,
> two rational forms times one common algebraic power $X(z)^r$.  The
> corresponding local inverse at $z=0$ is exactly the $y=-1$ branch
> of Item 237's algebraic curve.  That branch satisfies Item 237's same
> globally certified differential operator and coefficient recurrence.

> **PROVED — all-$n$ actual-$L$ second-branch bridge.**  On both
> rays and for every $n\geq0$,
> 

$$
> \frac{16^nL_{6n+e}}{g_n}=\mu_e a_{6n+e},
> \qquad
> \mu_1=-\frac{729}{50},\qquad
> \mu_5=\frac{6377292}{41405},
> \tag{1.1}
>
$$


> where $a_r$ is the second-branch coefficient defined below.
>
> The proof is not a finite promotion.  A common beta normalization turns
> actual $L$ into a two-cycle period determinant.  Every exact Hermite
> primitive has zero meromorphic finite part at all four endpoints, so
> Item 306's full tensor identity proves recurrence membership.  Three
> exact initial identities on each ray then identify the $y=-1$ branch.

This is a global translation theorem, but it is not a density theorem or
capacity reduction:



$$
\boxed{\text{new booking}=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling remains }1/105\text{ per }6M}.
$$



## 2. The two phase-tail forms invert to one common kernel

Put



$$
q=-\frac{2r+3}{3}=-\frac{2r}{3}-1,
 \qquad q_\nu=q-\nu,
 \qquad \epsilon_\nu=1+3\nu,
$$



and retain Item 250's meromorphically continued phase tails



$$
\mathcal X_\nu(r)=\operatorname{FP}\!\int_0^1
 t^{q_\nu}(1-t)^r(1+t)^{\epsilon_\nu}
 (1+t^2)^{q_\nu}\,dt.
 \tag{2.1}
$$



Define



$$
X(z)=\frac{z(1-z)}{(1+z^2)^{2/3}},
 \qquad
 \phi_0(z)=\frac{1+z}{1+z^2},
 \qquad
 \phi_1(z)=\frac{(1+z)^4}{(1+z^2)^2}.
 \tag{2.2}
$$



Under $t=1/z$, the power of $z$ is



$$
-3q_\nu-r-\epsilon_\nu-2=r,
$$



and



$$
q_\nu+\frac{2r}{3}=-1-\nu.
$$



The sign from $dt=-z^{-2}dz$ and
$(z-1)^r=-(1-z)^r$ cancels because $r$ is odd.  Hence, as an exact
meromorphic one-form identity with its inherited orientation,



$$
\boxed{
 \mathcal X_\nu(r)=\operatorname{FP}\!\int_{\infty}^{1}
 \phi_\nu(z)X(z)^r\,dz.}
 \tag{2.3}
$$



No convergence statement is hidden here: (2.3) is obtained first in a
common convergent parameter region and then continued meromorphically, or
equivalently checked by the displayed exponent identity.

This is the structural reason that the second branch is not an arbitrary
new numerator.  It is forced by the actual two phase tails.

## 3. The pinned upper-beta period uses the same two one-forms

Set



$$
H=\frac{r+1}{2},\qquad b_0=-\frac{2r}{3},\qquad b_1=b_0-1,
 \qquad \rho=\frac{r}{2(2r+3)}.
$$



Item 306's periods are



$$
\begin{aligned}
 A_r&=\operatorname{FP}\!\int_0^1
 u^r(1-u^2)^{b_0-1}(1-iu)^r(1+iu)\,du,\\
 B_r&=\operatorname{FP}\!\int_0^1
 u^r(1-u^2)^{b_0-1}(1-iu)^r
 \frac{(1+iu)^4}{1-u^2}\,du.
\end{aligned}
$$



Writing $s_r=i^{r+1}\in\{1,-1\}$, substitution $z=iu$ gives



$$
\int_0^i\phi_0(z)X(z)^r\,dz=s_rA_r,
 \qquad
 \int_0^i\phi_1(z)X(z)^r\,dz=s_rB_r,
 \tag{3.1}
$$



and the path to $-i$ gives the conjugates with the same real sign
$s_r$.  Therefore Item 306's exact formulas become



$$
\begin{aligned}
 f_0&=\frac{1}{i s_r B(H+1/2,b_0)}
 \left(\int_0^i-\int_0^{-i}\right)\phi_0X^r\,dz,\\
 f_1&=\frac{\rho}{i s_r B(H+1/2,b_1)}
 \left(\int_0^i-\int_0^{-i}\right)\phi_1X^r\,dz.
\end{aligned}
\tag{3.2}
$$



Thus both $f$ and the phase tails live in the same rank-three twisted
period family.  Formula (3.2) is a beta-normalized contour identity, not a
fit.

The beta factors are nonzero on the theorem domain: $r>0$, $r$ is
odd, and $3\nmid r$, so neither $b_0,b_1$ nor their relevant sums
with $H+1/2$ meet a gamma pole.

## 4. The actual endpoint coefficient and exact period determinant

For the Frobenius-free meromorphic phase reduction, write



$$
\mathcal X_\nu=\mathsf a_\nu E+\mathsf b_\nu C,
 \qquad C=2^q.
 \tag{4.1}
$$



The coefficient recurrence is



$$
(3q+k)v_{k+2}=1-(q+k)v_k.
 \tag{4.2}
$$



This is exactly the $c$-coordinate recurrence used in Item 250.  The
finite-field resonant correction $c-1$ changes only the separate affine
coordinate $d$, not $b$.  Consequently the $b_\nu$ in (4.1) are
the actual pinned $b_\nu$ in



$$
L_r=9(f_0b_1-f_1b_0).
$$



Item 250 proved $\mathsf a_\nu=\kappa_rf_\nu$.  Eliminating the common
period $E$ therefore gives the exact period determinant



$$
\boxed{
 L_r=\frac{9}{2^q}
 \det\!\begin{pmatrix}
 f_0&f_1\\
 \mathcal X_0&\mathcal X_1
 \end{pmatrix}.}
 \tag{4.3}
$$



There is one further decisive simplification.  With



$$
a=H+\frac12=\frac{r+2}{2},\qquad b=-\frac{2r}{3},
$$



the beta shift is



$$
\frac{B(a,b-1)}{B(a,b)}
 =\frac{a+b-1}{b-1}
 =\frac{r}{2(2r+3)}=\rho.                       \tag{4.4}
$$



Thus the two components in (3.2) have one common normalization.  If



$$
\delta=(0,i)-(0,-i),\qquad \Gamma=(\infty,1),
$$



and



$$
\Delta_r=det\!\begin{pmatrix}
 \int_\delta\phi_0X^r dz&\int_\delta\phi_1X^r dz\\
 \int_\Gamma\phi_0X^r dz&\int_\Gamma\phi_1X^r dz
 \end{pmatrix},
$$



then (4.3) becomes



$$
\boxed{L_r=\eta_L(r)\Delta_r},\qquad
 \eta_L(r)=
 \frac{9}{i\,s_r\,2^qB((r+2)/2,-2r/3)}.          \tag{4.5}
$$



This is an exact representation of the actual pinned $L$-minor, not a
representation of a fitted sequence.

## 5. Exact Hermite endpoints and actual-$L$ recurrence

Item 306's two form reductions are identities of rational one-forms and
are therefore independent of the choice of cycles.  For kind
$\nu\in\{0,1\}$ and shift $m\in\{0,1,2,3\}$, every nonzero exact
primitive has the form



$$
\Pi_{\nu,m}(z)=
 z^{r+1}(1-z)^{r+1}
 (1+z^2)^{-4m-\nu-2r/3}P_{\nu,m}(z),              \tag{5.1}
$$



where $P_{\nu,m}$ is the rational polynomial certified in Item 306.
The $(\nu,m)=(0,0)$ reduction is the identity and has zero primitive.
The endpoint audit is complete:

* at $z=0$ and $z=1$, (5.1) has a zero of order at least $r+1$;
* at $z=\pm i$, every local exponent lies in
  $\mathbb Z-2r/3$;
* at $z=\infty$, every exponent lies in
  $\mathbb Z+2r/3$.

Because $3\nmid r$, no endpoint expansion contains exponent zero.
Therefore every exact primitive has meromorphic finite part zero at both
ends of both $\delta$ and $\Gamma$.  No literal divergent endpoint is
dropped.

Consequently Item 306's three cleared exterior-tensor identities — and
its restored nine tensor coordinates — apply verbatim to $\Delta_r$.
It remains only to compare normalizations.  Under $r\mapsto r+6$,



$$
q\mapsto q-4,\qquad s_{r+6}=-s_r,
$$



and gamma shifting gives



$$
\frac{B((r+2)/2,-2r/3)}
 {B((r+8)/2,-2(r+6)/3)}
 =-\frac{64(r+3)(2r+3)(2r+9)}
 {27r(r+2)(r+4)}.                                  \tag{5.2}
$$



Hence



$$
\boxed{
 \frac{\eta_L(r+6)}{\eta_L(r)}
 =16\frac{\eta_M(r+6)}{\eta_M(r)}.}               \tag{5.3}
$$



The left side of Item 306's tensor cancellation for $L_r/g_n$ thus has
exactly the same shift weight as its cancellation for $16^nM_r/g_n$:



$$
\mathcal R(r)\frac{\eta_L(r+6)}{\eta_L(r)}
 =16\mathcal R(r)\frac{\eta_M(r+6)}{\eta_M(r)}.
$$



It follows symbolically that



$$
\boxed{
 \sum_{m=0}^3p_m(r/2)
 \frac{L_{r+6m}}{g_{n+m}}=0,
 \qquad r=6n+e.}                                   \tag{5.4}
$$



Thus actual $L/g$ belongs to the operator.  No finite row is used in
this membership proof.

## 6. The exact $y=-1$ local branch

Item 237 uses



$$
x=\frac{y(1+y)}{Q(y)^{2/3}},\qquad
 Q(y)=1+y+\frac{y^2}{2},
$$



and



$$
C(x(y))=\frac{N(y)}{D(y)^3}.
$$



Put $y=z-1$.  Then



$$
Q(z-1)=\frac{1+z^2}{2},
 \qquad x=-2^{2/3}X(z).
 \tag{6.1}
$$



Since $X(z)=z+O(z^2)$, there is a unique inverse
$z=z(X)\in X\mathbb Q[[X]]$.  Define



$$
\mathcal A(X)=\frac{N(z(X)-1)}{D(z(X)-1)^3}
              =\sum_{r\geq0}a_rX^r.
 \tag{6.2}
$$



The exact rational parametrization is



$$
\boxed{
 \mathcal A(X(z))=
 \frac{6(1+z^2)^2(8z^3+25z^2-24z+9)}
 {(2z^3+z^2+6z-3)^3}.}
 \tag{6.3}
$$



Also



$$
X'(z)=-\frac{2z^3+z^2+6z-3}{3(1+z^2)^{5/3}}.
 \tag{6.4}
$$



The branch selection is explicit: $z(0)=0$, hence $y(0)=-1$,
whereas Item 237's original Taylor branch has $y(0)=0$.

Let $\alpha^3=4$, and put



$$
C_-(x)=\mathcal A(-x/\alpha).
$$



Then $y=z(-x/\alpha)-1$ satisfies Item 237's curve equation



$$
x^3(y^2+2y+2)^2-4y^3(1+y)^3=0.
$$



Indeed, after substituting $y=z-1$ and
$X^3=z^3(1-z)^3/(1+z^2)^2$, its numerator is



$$
-4z^3(1-z)^3-4(z-1)^3z^3=0.
$$



Item 237's differential certificate clears to the zero polynomial in the
parameter $y$, so it applies to every local branch, including $C_-$.
Thus $C_-$, and therefore each fixed-residue coefficient line below,
satisfies the same exact operator.

For $r=e+6n$ with $e\in\{1,5\}$,



$$
[x^r]C_-(x)=-2^{-2e/3}16^{-n}a_r.
 \tag{6.5}
$$



Hence



$$
\boxed{16^{-n}a_{6n+e}\text{ satisfies Item 237's exact
 order-three recurrence on both rays}.}
 \tag{6.6}
$$



This is a global theorem about the second branch.  Together with the
independent actual-$L$ recurrence (5.4), it gives the all-$n$ bridge
after the initial identities below.

Lagrange inversion gives a convenient exact coefficient definition:



$$
a_r=\frac1r[z^{r-1}]\mathcal A'(z)
 \left(\frac{(1+z^2)^{2/3}}{1-z}\right)^r,
 \qquad r\geq1.
 \tag{6.7}
$$



## 7. Exact initial identities and independent replay

The deterministic checker evaluates $L_r$ from Item 250's original
phase states and evaluates $a_r$ from (6.7), independently of either
recurrence.  The six rows



$$
n=0,1,2,\qquad e\in\{1,5\},
$$



prove the constants in (1.1).  Both sides already satisfy the same
order-three recurrence, and Item 306 proves $p_3(r/2)>0$ for every
$r>0$.  These six original-tail identities therefore prove (1.1) for
every $n\geq0$.

For implementation replay, the checker additionally evaluates the rows



$$
0\leq n\leq11,\qquad e\in\{1,5\},
$$



all 24 rows satisfy (1.1).  Their row-stream SHA-256 is

~~~text
8f3c5a179360b4d220e459556eadae6f0a473052b7bd989049e29289bc2a132a
~~~

Canonical and replay JSON are byte-identical with SHA-256

~~~text
b44200c2e3fe16fca4518e45b40540230db43deee496d84c43336907ef304c5a
~~~

Only $n=0,1,2$ on each ray are theorem inputs.  The later rows are
deterministic replays and are labelled **EXACT FINITE ONLY**.

## 8. Pole, denominator, and orientation audit

The characteristic-zero theorem has no exceptional actual $r$.

* $X'(0)=1$, so the local inverse at $z=0$ is unique.
* $D(z-1)$ has constant term $-3$, so the Taylor coefficients of
  $\mathcal A$ introduce only powers of 3 before Lagrange extraction.
* In (6.7), generalized-binomial denominators have prime factors at most
  $r$, together with 3.  Every actual prime satisfies
  $p=2r+6s+3>2r+3$, so these are $p$-units.
* The denominators of $\mu_1,\mu_5$ have prime factors among
  $2,5,7,13$, all below the relevant actual rows on their rays.
* The orientation sign in (2.3) is $(-1)^{r+1}=+1$; reversing it would
  change both finite constants and is explicitly excluded by the checker.
* The beta parameters in (3.2) are nonintegral because $3\nmid r$, so
  no beta-resonant actual row is used.
* The Hermite-coordinate denominator roots are
  

$$
-3,-6,-9,-12,-15,-18
$$


  and
  

$$
-3/2,-9/2,-15/2,-21/2,-27/2,-33/2,-39/2.
$$


* The primitive coefficients have only the possible integer poles
  $r=-1,-2,\ldots,-38$.
* Across the three required transitions, the $\eta$-denominator roots
  are $0,-2,-4,-6,-8,-10,-12,-14,-16$, while the gauge-denominator
  roots are
  

$$
-1,-2,-4,-5,-7,-8,-10,-11,-13,-14,-16,-17.
$$


* The exact endpoint exponents for all eight shifted primitives are
  recorded separately in the certificate.  At $0,1$ there is a zero of
  order at least $r+1$; at $\pm i$ and $\infty$, the exponents lie
  in $\mathbb Z-2r/3$ and $\mathbb Z+2r/3$, respectively.  None is
  zero on the actual rays.

All listed rational poles are negative.  Hence $g_n$, $\eta_L$, the
Hermite coordinates, and the forward recurrence coefficient are nonzero
over $\mathbb Q$ for every actual $r$.

This does not remove Item 294's modular-gauge warning.  The rational gauge
is noninvertible on the first two actual $s$-layers, and the primitive
forward coefficient has the six structural singular layers
$s=1,\ldots,6$.  Any future mod-$p$ use of (1.1) must be cleared and
audited layer by layer; a characteristic-zero branch identity alone is not
an all-row unit theorem.

## 9. Full gate and capacity audit

The independent minor $L_r$ is not itself a collision gate.  The actual
necessary determinant remains



$$
D_r=cL_r+M_r,
 \qquad c=2^{2s}.
 \tag{9.1}
$$



The proved bridges in Items 306 and 309 give



$$
\frac{16^nD_r}{g_n}
 =c\,\mu_ea_r+\lambda_e[x^r]C_+(x),
 \tag{9.2}
$$



where



$$
\lambda_1=-\frac{891}{100},\qquad
 \lambda_5=\frac{3897234}{41405},
$$



and $C_+$ is Item 237's $y=0$ branch.  Thus the minimal plausible
enlargement is not a new unrelated period: it is the two-branch module
$\langle C_+,C_-\rangle$ of the same algebraic curve.

Equation (9.2) only translates the gate.  The smallest remaining
arithmetic theorem would be a weighted moving-prime estimate for the
actual tied combination



$$
2^{2s}\mu_ea_{6n+e}
 +\lambda_e[x^{6n+e}]C_+(x)\equiv0
 \pmod{p},
 \qquad p=2(6n+e)+6s+3,
 \tag{9.3}
$$



with the singular layers separately cleared.  To reduce the ordinary
$j=2$ ceiling, one needs the total logarithmic mass of those prime rows
to be $o(M)$, not merely a recurrence or isolated nonvanishing examples.
Moreover, $D=0$ remains only the row-rank-drop condition; the actual
period incidence from Item 291 is still stronger.

Accordingly Item 309 books zero.

## 10. Reproduction and labels

From the portable archive root:

~~~text
python scripts/item309_j2_l_second_branch_bridge_certificate.py
python scripts/item309_j2_l_second_branch_bridge_certificate.py \
  --output results/item309_j2_l_second_branch_bridge_certificate_replay.json
~~~

### PROVED

* The exact tail-form inversion (2.3), including orientation.
* The beta-contour representation (3.2) and period determinant (4.3).
* The common-beta identity (4.4) and actual period determinant (4.5).
* The complete finite-part endpoint audit for all eight reductions
  (seven nonzero primitives and one identity) in (5.1).
* Item 306's three independent and nine restored tensor cancellations as
  applied to the actual $L$ determinant.
* The normalization quotient (5.3) and actual-$L$ recurrence (5.4).
* The explicit $y=-1$ branch (6.1)--(6.5).
* The all-$n$ recurrence theorem (6.6) for the second branch.
* The six exact original-tail initial identities and the all-$n$ bridge
  (1.1).
* The full characteristic-zero pole and branch-coefficient
  denominator audit.

### EXACT FINITE ONLY

* The 18 comparison rows beyond the six theorem-required initials.

### OPEN

* A fully cleared all-layer mod-$p$ two-branch gate.
* Any all-prime or weighted-density theorem, capacity reduction, Route-1
  completion, or conclusion about $e+\pi$.

