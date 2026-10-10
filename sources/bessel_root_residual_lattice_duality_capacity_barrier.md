> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The Bessel root residual as an exact lattice quotient

Checked: 2026-08-27 UTC.

## 1. Verdict

Let $\rho=\rho_{p,r}\in\mathbb Z_p$ be an ordinary zero of the
canonical Bessel-index interpolation, let $n\equiv r\pmod p$, and put



$$
a=v_p(n-\rho)=v_p(q_n),\qquad P=p^a.
\tag{1}
$$



The preceding parameter Hermite--Padé reduction leaves an integer
polynomial $B(x)=\det\mathcal B(x)$.  To prove a digit-depth bound by
this route, one would like



$$
v_p(B(\rho))\geq a,\qquad B(n)\ne0,
\tag{2}
$$



with small primitive coefficient height.

This note gives the exact lattice and dual optimization behind (2).
The result is a sharp no-go for transference or capacity arguments that
use only this congruence.

1. For every $B\in\mathbb Z[x]$,

   

$$
\boxed{v_p(B(\rho))\geq a
   \quad\Longleftrightarrow\quad P\mid B(n).}
   \tag{3}
$$



   Thus at the required depth the special root disappears completely
   from the residual congruence.
2. In degree at most $d$, the coefficient lattice in (3) has the
   exact basis

   

$$
P,\quad x-n,\quad (x-n)x,\quad\ldots,\quad
   (x-n)x^{d-1},
   \tag{4}
$$



   determinant $P$, and coefficient-dual lattice

   

$$
\mathbb Z^{d+1}
   +\frac1P\mathbb Z(1,n,\ldots,n^d).
   \tag{5}
$$


3. The $d$ independent short directions in (4) all satisfy
   $B(n)=0$ and are therefore unusable.  In the quotient by those
   directions, evaluation at $n$ identifies the surviving lattice
   exactly with $P\mathbb Z$.
4. If $B$ is primitive and $B(n)\ne0$, then, with
   $H_1(B)$ denoting the sum of the absolute values of its
   coefficients,

   

$$
\boxed{
   a\log p\leq
   \log H_1(B)+\deg(B)\log(n+1).}
   \tag{6}
$$



   Conversely, the primitive linear polynomial

   

$$
B_*(x)=x+(P-n)
   \tag{7}
$$



   has $B_*(n)=P$.  When $P\geq n$, its complexity is at most

   

$$
\log(P+1)+\log(n+1)
   =a\log p+O(\log(n+1)).
   \tag{8}
$$



Hence the optimal primitive residual complexity is
$a\log p+O(\log n)$ in the high-depth regime.  Constructing a
sub-$n\log n$ residual by lattice reduction is therefore equivalent,
up to a negligible logarithm, to already knowing



$$
a\log p=o(n\log n).
\tag{9}
$$



This does not rule out an auxiliary with additional arithmetic
structure.  It proves that determinant, transference, and coefficient
capacity alone cannot manufacture the missing saving from (2).

No bound (9), and no irrationality or transcendence result, is proved.

## 2. Congruence collapse at the root depth

For an integral polynomial,



$$
B(X)-B(Y)=(X-Y)C_B(X,Y)
\tag{10}
$$



with $C_B\in\mathbb Z[X,Y]$.  Since $n,\rho\in\mathbb Z_p$,
equation (1) gives



$$
B(\rho)\equiv B(n)\pmod {p^a\mathbb Z_p}.
\tag{11}
$$



The integer $B(n)$ lies in $p^a\mathbb Z_p$ exactly when it is
divisible by $P=p^a$ in $\mathbb Z$.  This proves (3), in both
directions.  Notice that (3) uses the exact target depth $a$.
At any deeper modulus, information about further digits of $\rho$
would re-enter.

Equation (3) also explains a basic circularity.  If $B(n)\ne0$, then



$$
P\leq |B(n)|.
\tag{12}
$$



Any archimedean estimate for $B(n)$ that is strong enough to prove
(9) has already supplied the desired bound for $P$.

## 3. The coefficient lattice and its dual

For $d\geq0$, write a coefficient vector as
$\boldsymbol b=(b_0,\ldots,b_d)$ and define



$$
\begin{aligned}
 E_n(\boldsymbol b)&=\sum_{j=0}^{d}b_jn^j,\\
 \Lambda_d(n;P)&=
 \{\boldsymbol b\in\mathbb Z^{d+1}:E_n(\boldsymbol b)\in P\mathbb Z\},\\
 K_d(n)&=\ker(E_n:\mathbb Z^{d+1}\to\mathbb Z).
\end{aligned}
\tag{13}
$$



The coefficient vectors of (4) form a basis of
$\Lambda_d(n;P)$.  Indeed, eliminate a polynomial's leading
coefficient successively by subtracting multiples of
$(x-n)x^{j-1}$.  The final constant is its value at $n$, hence a
multiple of $P$.  The basis matrix is triangular with diagonal
$(P,1,\ldots,1)$, so



$$
[\mathbb Z^{d+1}:\Lambda_d(n;P)]
 =\det\Lambda_d(n;P)=P.
\tag{14}
$$



Moreover,



$$
0\longrightarrow K_d(n)\longrightarrow\Lambda_d(n;P)
 \mathop{\longrightarrow}^{E_n}P\mathbb Z
 \longrightarrow0
\tag{15}
$$



is exact.  The kernel has the $d$ primitive vectors
$(x-n)x^{j-1}$, each of ordinary $\ell^1$-height $n+1$.
Thus small successive minima or a small covolume vector need not
produce a usable residual: the first $d$ independent directions may
all evaluate to zero.

For the standard coefficient pairing, (13) also gives the dual lattice
directly:



$$
\boxed{
 \Lambda_d(n;P)^*
 =\mathbb Z^{d+1}
  +\mathbb Z\,\frac{(1,n,\ldots,n^d)}{P}.}
\tag{16}
$$



The inclusion from right to left follows from the congruence defining
$\Lambda_d(n;P)$.  Conversely, the right side has index $P$ over
$\mathbb Z^{d+1}$, which is the dual index forced by (14).
The nonintegral generator in (16) is exactly the evaluation functional
divided by $P$.  It is the elementary dual certificate for every
height lower bound below.

## 4. Primitive $\ell^1$-height optimization

Let $\operatorname{cont}(B)$ be the positive gcd of the coefficients
of a nonzero integral polynomial, and call $B$ primitive if its
content is $1$.  Define



$$
\mu_d(n;P)=
 \min\{H_1(B):
 \deg B\leq d,\ \operatorname{cont}(B)=1,\
 B(n)\in P\mathbb Z\setminus\{0\}\}.
\tag{17}
$$



For $n\geq2$ and $d\geq1$, evaluation gives



$$
\boxed{\mu_d(n;P)\geq\max\{1,P/n^d\}.}
\tag{18}
$$



There is also a matching elementary construction at fixed degree.
Write the truncated base-$n$ expansion



$$
P=Qn^d+\sum_{j=0}^{d-1}r_jn^j,
\qquad 0\leq r_j<n.
\tag{19}
$$



Let $R(x)=Qx^d+\sum_{j<d}r_jx^j$.  If $R$ is primitive, retain it.
Otherwise its content divides $R(n)=p^a$, so every common prime
divisor is $p$.  In that case put



$$
B(x)=R(x)+(x-n).
\tag{20}
$$



All coefficients of $R$ were divisible by $p$, whereas the
coefficient of $x$ in (20) is congruent to $1\pmod p$.
Any common divisor of the coefficients of $B$ must divide
$B(n)=P$, so (20) is primitive.  In either case,



$$
\boxed{
 \mu_d(n;P)
 \leq
 \left\lfloor\frac{P}{n^d}\right\rfloor
 +d(n-1)+n+1.}
\tag{21}
$$



Thus the usual determinant-versus-dimension balance is real, but it
does not save the evaluated height.  Multiplying (18) and (21) by
$n^d$ places the natural scale back at $P$.

For the exact complexity needed in the Bessel argument, put



$$
\mathcal C_d(n;P)=
 \inf_B\{
 \log H_1(B)+\deg(B)\log(n+1)\},
\tag{22}
$$



over the same primitive, nonzero-evaluation set as in (17).  Equations
(12) and



$$
|B(n)|\leq H_1(B)(n+1)^{\deg B}
\tag{23}
$$



give



$$
\boxed{\mathcal C_d(n;P)\geq\log P.}
\tag{24}
$$



For every $d\geq1$, the primitive polynomial (7) gives



$$
\boxed{
 \mathcal C_d(n;P)
 \leq
 \log(1+|P-n|)+\log(n+1).}
\tag{25}
$$



In particular, if $P\geq n$, then



$$
\log P\leq\mathcal C_d(n;P)
 \leq\log(P+1)+\log(n+1).
\tag{26}
$$



This is the claimed matching optimization.

There is an even sharper weighted formulation.  Set



$$
\|\boldsymbol b\|_{1,n+1}
 =\sum_{j=0}^{d}|b_j|(n+1)^j.
\tag{27}
$$



Every lattice point outside $K_d(n)$ has



$$
\|\boldsymbol b\|_{1,n+1}
 \geq|E_n(\boldsymbol b)|\geq P.
\tag{28}
$$



When $P\geq n$, the primitive vector (7) has weighted norm exactly
$P+1$.  Thus the first usable primitive lattice vector in this
evaluation-adapted body has norm in $[P,P+1]$.  No transference
inequality can improve this exact primal-dual obstruction.

## 5. Content cannot be hidden by primitive normalization

Suppose an auxiliary initially produces $B=cB_0$, where
$B_0$ is primitive and $t=v_p(c)$.  If (2) holds, then (3) implies



$$
v_p(B_0(n))\geq\max\{0,a-t\}.
\tag{29}
$$



When $B(n)\ne0$, evaluation therefore gives the explicit
content-aware inequality



$$
\boxed{
 \max\{0,a-t\}\log p
 \leq
 \log H_1(B_0)+\deg(B_0)\log(n+1).}
\tag{30}
$$



Equivalently, retaining the content gives



$$
a\log p
 \leq\log H_1(B)+\deg(B)\log(n+1),
\tag{31}
$$



because $B(n)$ is a nonzero multiple of $P$.  A large $p$-power
content can create apparent local order only by paying the same amount
in archimedean height.  Dividing to the primitive part removes exactly
that order.

## 6. What transference, capacity, and zero estimates would need

### 6.1 Transference

The covolume $P$ in (14) may suggest a coefficient vector of size
roughly $P^{1/(d+1)}$.  But (4) supplies $d$ independent short
kernel vectors before the quotient direction is reached.  The exact
sequence (15), not a loss in a generic transference inequality, forces
every nonkernel value into $P\mathbb Z$.  Passing to the last
successive minimum merely reproduces (24).

### 6.2 Coefficient capacity

Consider any convex-body or coefficient-capacity argument whose
archimedean body is bounded by (27) and whose only nonarchimedean input
is the congruence (3).  Below weighted radius $P$, equation (28)
forces every lattice point it can produce into $K_d(n)$, where
$B(n)=0$.  At radius $P+1$, the explicit primitive point (7) is
already available when $P\geq n$.  Thus the threshold for a usable
point is $P+O(1)$, not $P^{1/(d+1)}$.

This statement is deliberately scoped.  A capacity construction that
uses new local equations, several arithmetically related places, or a
special integral transform is not reduced to $\Lambda_d(n;P)$ and is
not excluded.

### 6.3 A $p$-adic zero estimate

A genuine lower bound for nonzero $B(\rho)$ in terms of
$\deg B$ and $H_1(B)$ would be new arithmetic input.  In fact,
degree one already contains the whole missing problem: the primitive
polynomial



$$
L_n(x)=x-n
\tag{32}
$$



has $H_1(L_n)=n+1$ and



$$
v_p(L_n(\rho))=a.
\tag{33}
$$



Consequently, any uniform zero estimate strong enough to give



$$
v_p(B(\rho))\log p=o(n\log n)
\tag{34}
$$



at degree $1$ and height $n+1$ proves (9) immediately by taking
$B=L_n$.  Conversely, (9) is exactly that restricted
rational-integer approximation estimate.  Strassmann root counts,
local analyticity, or the difference equation alone do not provide
such an arithmetic lower bound.

If one could first prove that $\rho$ is algebraic with controlled
global degree and height, a product-formula argument could become
relevant.  No such algebraicity theorem is known or assumed here.

## 7. Exact survivor

For a residual determinant $B=\det\mathcal B$, one must now supply
structure not present in the one-congruence lattice:

- an independently proved sub-main bound for the primitive
  $H_1(B)$ and its degree;
- nonvanishing of $B(n)$;
- and high order at $\rho$ arising from a special identity rather
  than inserted $p$-power content.

Once those facts hold, (6) gives the digit-depth estimate.  The lattice
theorem proves that none of them follows from the residual congruence,
covolume, or coefficient capacity by itself.

Nothing in this note proves (9), irrationality of a Bessel zero, or
irrationality or transcendence of $e+\pi$.

## 8. Exact certificate

The companion script

    scripts/bessel_root_residual_lattice_duality_certificate.py

checks the explicit lattice basis, determinant and reconstruction,
dual pairings, the primitive base-$n$ construction, fixed-degree
height bounds, the exact weighted lower bound and linear near-attainer,
and content normalization over finite exact boxes.  The all-parameter
statements are proved symbolically above.

Run

    python -m py_compile scripts/bessel_root_residual_lattice_duality_certificate.py
    python scripts/bessel_root_residual_lattice_duality_certificate.py

For byte-identical replay, use

    python scripts/bessel_root_residual_lattice_duality_certificate.py \
      --output /tmp/bessel_root_residual_lattice_duality_certificate.json
    cmp results/bessel_root_residual_lattice_duality_certificate.json \
      /tmp/bessel_root_residual_lattice_duality_certificate.json
