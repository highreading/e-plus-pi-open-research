> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 301 — exact reduction of the structural boundary scalar

Date: 2026-08-31

## 1. Outcome and capacity first

On the structural rays $s=2j$, $j=1,2,3$, put $H=h+3j$.
Then $p=4H+3$, and Item 297 proves



$$
B_H:=pE_H^*\equiv-\frac34X_HV_H-9U_HY_H\pmod p.       \tag{1.1}
$$



The union of the three shifted boundary diagonals has raw Chebyshev mass
asymptotic to $2H$, not $6H$.  The retained conditional fixed-$j=1$
ceiling is $1/36$ per $6m$.  Consequently only an all-$H$ identity
or a weighted zero-density theorem could change capacity.

This item proves an all-$H$ simplification: $U_H,V_H,X_H$ are
elementary, and the whole boundary scalar reduces to one residual moment
$Y_H$.  It also proves that every boundary-neighbor condition obtained
from the actual recurrence is exactly the old $E_h^*$ gate on unit rows,
and is automatic on the complete finite set of nonunit rows.  Thus it adds
no independent codimension.

No nonvanishing or weighted-density theorem for $Y_H$, $B_H$, or
$E_h^*$ is proved.  The booked rate, divisibility exponent, and capacity
reduction are all zero.

## 2. Root-of-unity evaluation of $U_H,V_H$

For a polynomial $K(z)=\sum_nK_nz^n$, the exact parity filters are



$$
\sum_t(-1)^tK_{2t}=\frac{K(i)+K(-i)}2,\qquad
 \sum_t(-1)^tK_{2t+1}=\frac{K(i)-K(-i)}{2i}.          \tag{2.1}
$$



Here $K_1(z)=(1-z)^{2H}(1+z)^4$, so



$$
K_1(i)=-4(-2i)^H,\qquad K_1(-i)=-4(2i)^H.           \tag{2.2}
$$



Item 297's definition has weight $1$ on the constant even term and
weight $1/3$ on all other even terms.  Hence, if



$$
e_H=(-1)^{H/2}2^H\quad(H\text{ even}),\qquad
 d_H=(-1)^{(H-1)/2}2^H\quad(H\text{ odd}),            \tag{2.3}
$$



then (2.1)--(2.2) give, for every $H$,



$$
\begin{array}{c|cc}
 &U_H&V_H\\ \hline
H\text{ even}&(2-4e_H)/3&0\\
H\text{ odd}&2/3&4d_H.
\end{array}                                                \tag{2.4}
$$



These are identities over $\mathbb Q$, before reduction modulo $p$.

## 3. Weighted odd-filter evaluation of $X_H$

Let $K_0(z)=(1-z)^{2H}(1+z)$.  Integrating the odd filter gives



$$
X_H=\frac1i\int_0^1\bigl(K_0(iu)-K_0(-iu)\bigr)\,du.       \tag{3.1}
$$



Indeed, the coefficient of $K_{0,2t+1}$ on the right is
$2\int_0^1u^{2t+1}du=1/(t+1)$, with the required sign
$(-1)^t$.

In the first integral set $w=1-iu$.  An exact antiderivative is



$$
i\left(\frac{2w^{2H+1}}{2H+1}
          -\frac{w^{2H+2}}{2H+2}\right),qquad 1\leq w\leq1-i. \tag{3.2}
$$



The second integral is its complex conjugate.  Substituting
$(1-i)^{2H}=(-2i)^H$ in (3.1)--(3.2) yields



$$
X_H=
\begin{cases}
\displaystyle \frac{4(e_H-1)}{2H+1}+\frac1{H+1},
   &H\text{ even},\\
\displaystyle -\frac{2d_H+2H+3}{(2H+1)(H+1)},
   &H\text{ odd}.
\end{cases}                                                \tag{3.3}
$$



Thus three of Item 297's four boundary sums have elementary closed forms.

## 4. The single residual moment $Y_H$

The same odd filter, now with the weight
$(H+1)/(H+t+1)$, gives the exact integral



$$
Y_H=2(H+1)\operatorname {Im}
 \int_0^1u^{2H}(1-iu)^{2H}(1+iu)\,du.                \tag{4.1}
$$



Put $q(u)=u(1-iu)$ and



$$
J_n=\int_0^1q(u)^n\,du.      \tag{4.2}
$$



Since $1+iu=3/2-q'(u)/2$, integration in (4.1) gives



$$
Y_H=-\frac{H+1}{2H+1}\operatorname {Im}(1-i)^{2H+1}
       +3(H+1)\operatorname {Im}J_{2H}.              \tag{4.3}
$$



There is also an exact first-order evaluation of the moment.  From
$q'(u)^2=1-4iq(u)$ and $q''(u)=-2i$,



$$
J_0=1,\qquad
(1-i)^n(1-2i)=nJ_{n-1}-i(4n+2)J_n\quad(n\geq1).       \tag{4.4}
$$



Equations (4.1)--(4.4) are an all-$H$, sequence-specific description,
but they leave one genuine moment.  No zero-density or nonvanishing claim
is inferred from it.

## 5. Complete parity reduction of $B_H$

Suppose first that $H$ is even.  Then $p=4H+3\equiv3\pmod8$, so
Euler's criterion gives



$$
e_H^2=2^{2H}\equiv-\frac12\pmod p.    \tag{5.1}
$$



If $2e_H-1\equiv0$, squaring would give
$1/4\equiv-1/2$, forcing $p=3$, impossible.  Hence
$2e_H-1$ is a $p$-unit.  From (1.1) and (2.4),



$$
\boxed{B_H\equiv6(2e_H-1)Y_H\pmod p},
 \qquad
 \boxed{B_H\equiv0\iff Y_H\equiv0\pmod p}.          \tag{5.2}
$$



If $H$ is odd, then $p\equiv7\pmod8$, and Euler's criterion gives



$$
d_H^2\equiv\frac12\pmod p.       \tag{5.3}
$$



Using $H\equiv-3/4\pmod p$ in the odd formula (3.3) gives



$$
d_HX_H\equiv8+12d_H\pmod p.         \tag{5.4}
$$



Equations (1.1), (2.4), and (5.4) now give



$$
\boxed{B_H\equiv-6(Y_H+4+6d_H)\pmod p},
 \qquad
 \boxed{B_H\equiv0\iff Y_H\equiv-4-6d_H\pmod p}.    \tag{5.5}
$$



All denominators in (5.1)--(5.5) are $p$-units because every actual
boundary has $p\geq19$.

## 6. Exact de-overlap with the pinned target gate

On $s=2j$, define the boundary-neighbor combination



$$
L_j(h)=\frac{Q_j(h)}pB_{h+3j}
       +\sum_{\substack{1\leq k\leq3\\k\ne j}}
          Q_k(h)E_{h+3k}^*.                                \tag{6.1}
$$



Item 297's actual reduced recurrence is exactly



$$
\boxed{L_j(h)=-Q_0(h)E_h^*.}        \tag{6.2}
$$



Therefore, whenever $Q_0(h)$ is a $p$-unit,



$$
L_j(h)=0\iff E_h^*=0.               \tag{6.3}
$$



The boundary-neighbor condition is not a second gate: it is precisely the
old target gate multiplied by a unit.  In particular, on $s=6$, the
combination of $B_{h+9}$ with the two neighboring actual values
$E_{h+3}^*,E_{h+6}^*$ remains only a re-encoding of $E_h^*$.

The complete Item 297 $Q_0$-drop audit is



$$
\begin{array}{c|l}
s& p\text{ with }Q_0(h)\equiv0\pmod p\\ \hline
2&19,\ 103423\\
4&15131\\
6&\text{none}.
\end{array}                                                \tag{6.4}
$$



At every row in (6.4), (6.2) makes $L_j(h)=0$ automatic, irrespective
of $E_h^*$; it therefore cannot constrain the target.  At $p=19$,
all four coefficients in the first reduced relation vanish and the
relation is $0=0$.  Thus neither the unit rows nor the complete finite
drop set supplies independent codimension.

## 7. Capacity, labels, and reproducibility

The exact simplification (5.2), (5.5) does not prove that either residual
condition is sparse.  The identity (6.2) proves that adjoining the
boundary-neighbor combination cannot multiply probabilities or reduce
capacity.



$$
\boxed{\text{new linear log rate}=0,\quad
       \text{new divisibility exponent}=0,\quad
       \text{capacity booked}=0.}                           \tag{7.1}
$$



The conditional fixed-$j=1$ ceiling remains $1/36$ per $6m$.
Moving-prime nonvanishing, weighted density, Route 1, and every conclusion
about $e+\pi$ remain open.

From the archive root, replay with

~~~text
python scripts/item301_j1_boundary_scalar_reduction_certificate.py --output results/item301_j1_boundary_scalar_reduction_certificate.replay.json
~~~

The checker uses exact standard-library integer, rational, and Gaussian-
rational arithmetic.  It independently replays (2.4), (3.3), and
(4.1)--(4.4) for $1\leq H\leq80$, without scanning actual primes.  That
finite replay validates the implementation; the displayed algebra is the
logical basis of the all-$H$ theorem.

- **PROVED:** the all-$H$ formulas (2.4), (3.3), (4.1)--(4.4), the
  boundary reductions (5.2), (5.5), and the actual-recurrence de-overlap
  (6.2)--(6.4).
- **OPEN:** nonvanishing or weighted zero-density for $Y_H$, $B_H$,
  or the pinned $E_h^*$ orbit.
- **NOT CLAIMED:** that the residual moment lacks some further exact
  evaluation, or that unrestricted recurrence states describe the actual
  initial orbit.
