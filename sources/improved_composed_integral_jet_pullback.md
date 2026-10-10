> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A strictly larger-radius pullback with integral derivative jets

## Scope and result

Let



$$
F(w)=4\arctan\frac{w}{2-w}
=4\int_0^w\frac{dt}{t^2-2t+2},
\qquad F(1)=\pi,
\tag{1}
$$



and define



$$
\phi(z)=z-\frac{z^3}{6}+\frac{5z^4}{24}-\frac{z^5}{24},
\qquad
G(z)=F(\phi(z)).
\tag{2}
$$



Then



$$
\phi(0)=0,\qquad \phi(1)=1,\qquad G(1)=\pi.
\tag{3}
$$



The two principal conclusions are:

1. every derivative $G^{(n)}(0)$ is an integer; and
2. the Taylor radius of $G$ is strictly larger than $\sqrt2$.

The second assertion is certified by an exact Schur--Cohn recursion, not
by floating root finding.  High-precision roots give the diagnostic value



$$
\rho(G)=1.4597454685987641723\ldots,
\tag{4}
$$



compared with $\rho(F)=\sqrt2=1.41421356237\ldots$.

This is the first pullback found in this project that improves the analytic
radius while retaining integral derivative jets in every order.  It does
not, by itself, prove anything about the arithmetic nature of $e+\pi$.
The standard diagonal endpoint-matched Hermite--Padé forms built from it
actually grow faster in the finite tested range.

## 1. All-order integrality by composition

The nonzero derivative jets of $\phi$ at the origin are



$$
\phi'(0)=1,\qquad
\phi''(0)=0,\qquad
\phi^{(3)}(0)=-1,\qquad
\phi^{(4)}(0)=5,\qquad
\phi^{(5)}(0)=-5.
\tag{5}
$$



Thus $\phi$ is an integral Hurwitz series:



$$
\phi(z)=\sum_{n\ge1}b_n\frac{z^n}{n!},
\qquad b_n\in\mathbb Z.
\tag{6}
$$



The already proved jet formula for (1) is



$$
F^{(k)}(0)
=4(k-1)!2^{-k/2}\sin\frac{k\pi}{4}\in\mathbb Z.
\tag{7}
$$



Faà di Bruno's formula gives



$$
G^{(n)}(0)
=\sum_{k=1}^n
F^{(k)}(0)
B_{n,k}\!\left(
\phi'(0),\phi''(0),\ldots,\phi^{(n-k+1)}(0)
\right),
\tag{8}
$$



where every partial Bell polynomial $B_{n,k}$ has integer coefficients.
Equations (5), (7), and (8) prove



$$
\boxed{G^{(n)}(0)\in\mathbb Z\quad(n\ge0).}
\tag{9}
$$



The independent exact script recomputes these jets through order $100$
from the rational derivative of $G$, but that finite calculation is only
a check of the all-order argument.

## 2. Why ordinary integral polynomial compositions cannot improve the radius

There is a simple obstruction if one insists that the ordinary
coefficients of the composing polynomial be integers.  Let
$\psi\in\mathbb Z[z]$ have degree $d\ge1$,
$\psi(0)=0$, and $\psi(1)=1$.  If its leading coefficient is $a_d$,
the product of the moduli of the $d$ roots of



$$
\psi(z)=1+i
$$



is



$$
\frac{|1+i|}{|a_d|}
=\frac{\sqrt2}{|a_d|}
\le\sqrt2.
\tag{10}
$$



At least one root therefore has modulus at most



$$
2^{1/(2d)}.
\tag{11}
$$



For $d\ge2$, this is strictly below $\sqrt2$.  For $d=1$, the
endpoint conditions force $\psi(z)=z$, giving exactly $\sqrt2$.
Thus no ordinary integer-coefficient polynomial composition can improve
the original radius.

The polynomial $\phi$ in (2) escapes this obstruction in the precise
way needed here: its ordinary coefficients are rational, but its derivative
jets (5) are integral.

## 3. Exact location of the singularity boundary

The only finite singularities of the continued germ $F(w)$ are



$$
w=1+i,\qquad w=1-i.
\tag{12}
$$



Consequently the candidate singularities of $G=F\circ\phi$ are the
solutions of



$$
\phi(z)=1\pm i.
\tag{13}
$$



None is cancelled.  Indeed,



$$
G'(z)=
\frac{4\phi'(z)}
\{\phi(z)-(1+i)\}\{\phi(z)-(1-i)\}}.
\tag{14}
$$



If $\phi(z)-(1+i)$ has multiplicity $m$ at $z_0$, then
$\phi'(z)$ has multiplicity exactly $m-1$ there, while the other
factor in the denominator is nonzero.  Hence (14) has a simple pole at
$z_0$.  The same argument applies to $1-i$.  Every point in (13) is
therefore a genuine logarithmic singularity, and the Taylor radius of
$G$ is the least modulus of those roots.

## 4. Exact Schur--Cohn proof that the radius exceeds $\sqrt2$

Because $\phi$ has real coefficients, the two root sets in (13) are
complex conjugates and have the same moduli.  Put



$$
q(z)=\phi(z)-(1+i),\qquad r=\sqrt2,
$$



and form the reciprocal polynomial



$$
\begin{aligned}
P_0(w)
&=w^5q(r/w)\\
&=-(1+i)w^5+\sqrt2\,w^4
-\frac{\sqrt2}{3}w^2+\frac56w-\frac{\sqrt2}{6}.
\end{aligned}
\tag{15}
$$



The roots of $q$ all satisfy $|z|>r$ exactly when all roots of
$P_0$ lie in the open unit disk.

For a polynomial



$$
P(w)=a_0w^n+a_1w^{n-1}+\cdots+a_n,
$$



write



$$
P^*(w)=\overline{a_n}w^n+\overline{a_{n-1}}w^{n-1}
+\cdots+\overline{a_0},
\tag{16}
$$



and, when $|a_0|>|a_n|$, define its Schur transform



$$
\mathcal S(P)(w)
=\frac{\overline{a_0}P(w)-a_nP^*(w)}{w}.
\tag{17}
$$



The numerator in (17) has zero constant term.  The Schur--Cohn recursion
says that $P$ has all its roots in the open unit disk if and only if
$|a_0|>|a_n|$ and $\mathcal S(P)$ does; repeated application reduces
the assertion to a nonzero constant polynomial.

Starting with (15), the five exact differences
$|a_0|^2-|a_n|^2$ encountered under this recursion are



$$
\frac{35}{18},
\qquad
\frac{919}{324},
\qquad
\frac{90755}{13122},
\tag{18}
$$





$$
\frac{31025233225}{816293376},
\qquad
\frac{
20206728833189212829375
}{
60719765548297125888
}.
\tag{19}
$$



Every number in (18)--(19) is strictly positive.  Hence all roots of
$P_0$ lie strictly inside the unit disk.  It follows that every root of
$\phi(z)=1+i$, and by conjugation every root of
$\phi(z)=1-i$, has modulus strictly greater than $\sqrt2$.  Therefore



$$
\boxed{\rho(G)>\sqrt2.}
\tag{20}
$$



This is an exact algebraic certificate.  High-precision root finding is
used only for the decimal in (4).

## 5. Exact finite endpoint-matched systems

For $1\le n\le15$, an exact program constructs



$$
A_n(z)+B_n(z)e^z+C_n(z)G(z)=O(z^{3n+1}),
\qquad
C_n(1)=B_n(1),
\tag{21}
$$



with all three degrees at most $n$.  The high-jet matrix is integral by
(9).  In every one of the $15$ cases:

1. the $(2n+1)$-by-$(2n+2)$ high-jet-plus-endpoint matrix has full row
   rank;
2. its projective kernel is one-dimensional;
3. the first unconstrained coefficient at order $3n+1$ is nonzero; and
4. a directed rational interval certifies the reduced endpoint form is
   nonzero.

The certified base-ten decades of the fully reduced endpoint magnitudes,
for $n=1,\ldots,15$, are



$$
0,\ 2,\ 9,\ 19,\ 34,\ 53,\ 77,\ 106,\ 138,\ 176,\
219,\ 263,\ 318,\ 374,\ 439.
\tag{22}
$$



These values grow faster than those of the original radius-$\sqrt2$
pullback in the same diagonal construction.  The likely cause is that the
more complicated jet sequence has much less forced determinant content;
this is an interpretation of the finite data, not an all-degree theorem.
The radius improvement therefore opens a new analytic option but does not
make the standard diagonal endpoint forms small.

## 6. Reproducible artifacts and next question

The exact radius and jet certificate is
scripts/improved_composed_pullback_certificate.py, with output
results/improved_composed_pullback_certificate.json.

The exact finite Hermite--Padé probe is
scripts/composed_integral_pullback_hp_probe.py, with output
results/composed_integral_pullback_hp_n15.json.

The next structural question is whether a non-diagonal or
singularity-softened family can exploit (20) while retaining enough
determinant content to control primitive height.  Neither the present
Schur certificate nor the finite diagonal scan answers that question.
