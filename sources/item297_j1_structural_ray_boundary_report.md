> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 297 — boundary renormalization on the three structural $j=1$ rays

Date: 2026-08-31

## 1. Exact outcome

Item 296 isolates the coefficient-singular rays



$$
(s,j,p)=(2,1,4h+15),\quad(4,2,4h+27),\quad(6,3,4h+39). \tag{1.1}
$$



Put $H=h+3j$. On every ray, $p=4H+3$. The apparent vanishing
$Q_j(h)\equiv0\pmod p$ does not generically remove a term from the
Item 293 recurrence. Instead, $E_H^*$ has a possible simple boundary
pole, and



$$
B_H:=pE_H^*                         \tag{1.2}
$$



is $p$-integral. The exact reduced recurrence is



$$
\boxed{\sum_{k\ne j}Q_k(h)E_{h+3k}^*
       +\frac{Q_j(h)}p B_H\equiv0\pmod p.}                   \tag{1.3}
$$



All terms in (1.3) are defined modulo $p$. Outside the finite drop
table in Section 4, $Q_j(h)/p$ is a unit. Thus the structural
coefficient zero is generically canceled by the boundary pole; it gives
no lower-order recurrence and no nonvanishing theorem.

## 2. Raw Chebyshev capacity first

For each fixed $s\in\{2,4,6\}$, let $W_s(H_0)$ be the logarithmic
mass of prime rows with $h\leq H_0$. Since $6s+3\equiv3\pmod {12}$,



$$
\begin{aligned}
W_s(H_0)
={}&\vartheta(4H_0+6s+3;12,7)
   +\vartheta(4H_0+6s+3;12,11)+O(1)\\
\sim{}&2H_0.                                                \tag{2.1}
\end{aligned}
$$



The rays are exact shifts of the same prime diagonal:



$$
4h+39=4(h+3)+27=4(h+6)+15.                    \tag{2.2}
$$



Consequently their union also has mass asymptotic to $2H_0$, not
$6H_0$. The rays have linear raw capacity, but (1.3) supplies no
exclusion on them.

## 3. Boundary residue and integrality

Let



$$
K_0(z)=(1-z)^{2H}(1+z),\qquad
K_1(z)=(1-z)^{2H}(1+z)^4,                                  \tag{3.1}
$$



and write $K_{\nu,r}=[z^r]K_\nu(z)$.  Put $s_*=-p/6$, so
$2s_*=-p/3$ and $3s_*=-p/2$.  The four Item 222 Pochhammer
quotients reduce symbolically, for arbitrary $H$, as



$$
\begin{aligned}
X:\quad&\frac{(s_*+1)_t}{(3s_*+2)_t}
 =\frac{(1-p/6)_t}{(2-p/2)_t}
 \equiv\frac1{t+1}, &&0\leq t\leq H,\\
Y:\quad&\frac{(H+1)_t}{(2s_*+H+2)_t}
 =\frac{(H+1)_t}{(H+2-p/3)_t}
 \equiv\frac{H+1}{H+t+1}, &&0\leq t\leq H,\\
U:\quad&\frac{(s_*)_t}{(3s_*)_t}
 =\frac{(-p/6)_t}{(-p/2)_t}, &&0\leq t\leq H+2,\\
V:\quad&\frac{(H+1)_t}{(2s_*+H+1)_t}
 =\frac{(H+1)_t}{(H+1-p/3)_t}
 \equiv1, &&0\leq t\leq H+1.
                                                               \tag{3.2}
\end{aligned}
$$



The $U$-quotient at $t=0$ is $1$.  For $t\geq1$, its
apparently singular first factors cancel over $\mathbb Q$:



$$
\frac{(-p/6)_t}{(-p/2)_t}
 =\underbrace{\frac{-p/6}{-p/2}}_{=,1/3}
  \frac{(1-p/6)_{t-1}}{(1-p/2)_{t-1}}
 \equiv\frac13\pmod p.                                  \tag{3.3}
$$



This cancellation is performed before reduction.  The remaining
denominator representatives lie in the intervals



$$
\begin{array}{c|c}
X&2,\ldots,H+1\\
Y&H+2,\ldots,2H+1\\
U&1,\ldots,H+1\\
V&H+1,\ldots,2H+1.
\end{array}                                                \tag{3.4}
$$



They are positive and strictly below $p=4H+3$.  Thus all remaining
denominators are $p$-units for every actual boundary $H\geq4$, and
(3.2)--(3.3) give



$$
\begin{aligned}
X={}&\sum_{t=0}^{H}\frac{(-1)^tK_{0,2t+1}}{t+1},\\
Y={}&\sum_{t=0}^{H}
       \frac{(-1)^t(H+1)K_{0,2t+1}}{H+t+1},\\
U={}&K_{1,0}+\frac13\sum_{t=1}^{H+2}(-1)^tK_{1,2t},\\
V={}&\sum_{t=0}^{H+1}(-1)^tK_{1,2t+1}
                                      \qquad\text{in }\mathbb F_p.    \tag{3.5}
\end{aligned}
$$



Item 222's exact phase formula at index $H$ is



$$
E_H^*=\frac H p xv+\frac{9(4H+1)}{2p}uy.             \tag{3.6}
$$



The lower-case quantities are $p$-integral by the preceding audit and
reduce to $X,Y,U,V$.  Multiplying (3.6) by $p$, then using
$H\equiv-3/4$ and $4H+1\equiv-2\pmod p$, proves for every $H$



$$
\boxed{B_H\equiv-\frac34XV-9UY\pmod p.}  \tag{3.7}
$$



This is a sequence-specific finite hypergeometric representation, not
an unrestricted-state model.

For completeness, integrality of every nonboundary term in (1.3) follows
from the proved gauge and the Item 237 coefficient formula.  Put
$Q=1+y+y^2/2$, $A=(20+14y+4y^2)/3$, and
$B=2-5y-3y^2$.  For $N=H+3t$, reduction below degree $p$ gives



$$
c_N^*\equiv[y^{(p-3)/2+6t}]
(1+y)^{(p+1)/2-6t}Q(y)^{4t}\bigl(NA(y)+B(y)\bigr)\pmod p.   \tag{3.8}
$$



For $t=0$, the relevant coefficient is zero because



$$
-3\binom{1/2}{2}-\frac{17}{2}\binom{1/2}{3}
-4\binom{1/2}{4}=0.                                        \tag{3.9}
$$



For $t=1$, the target is the formal top degree but its leading
coefficient $4t-4$ vanishes.  For $t=2$, the target degree $M+10$
exceeds the polynomial degree $M+6$, where $M=(p+1)/2$.  Hence
$c_{H+3t}^*\equiv0\pmod p$ in every needed below-$p$ case.

It remains to audit the gauge valuations uniformly.  Item 243's gauge is
fixed by



$$
\mathcal G_1=-\frac{49}{18},\qquad
 \mathcal G_2=\frac{4235}{1944},\qquad
 \frac{\mathcal G_{r+3}}{\mathcal G_r}=\rho(r),              \tag{3.10}
$$



where



$$
\rho(r)=
\frac{r(4r+1)(4r+5)(4r+7)(4r+9)(4r+11)(4r+15)^2}
{864(r+1)(r+2)(2r+1)^2(2r+3)(2r+5)^2(4r+3)}.                \tag{3.11}
$$



The initial gauges have prime support contained in
$\{2,3,5,7,11\}$, hence are $p$-units because $p\geq19$.  At
every earlier step $r\leq H-6$, all positive factors in (3.11) are
strictly below $p$.  At the critical steps the complete audit is



$$
\begin{array}{c|c|c}
\text{step}&\text{only }p\text{-factor}&v_p(\rho)\\ \hline
r=H-3&(4(H-3)+15)^2=p^2&2\\
r=H&4H+3=p\text{ in the denominator}&-1\\
r=H+3,\ p>19&\text{none}&0\\
r=H+3,\ (H,p)=(4,19)&(2(H+3)+5)^2=p^2\text{ in the denominator}&-2.
\end{array}                                                \tag{3.12}
$$



The factors $4r+c$ at $r=H$ are $p+\delta$, with
$\delta=-2,2,4,6,8,12$; at $r=H+3$, their offsets are
$10,14,16,18,20,24$.  None is a multiple of the odd prime $p$.
The only possible collision among the remaining $r=H+3$ denominator
factors solves $2(H+3)+5=p$, namely $H=4,p=19$.  This proves



$$
v_p(\mathcal G_H)=2,\qquad
v_p(\mathcal G_{H+3})=1,\qquad
v_p(\mathcal G_{H+6})=
 \begin{cases}1,&p>19,\\-1,&(H,p)=(4,19).
 \end{cases}                                               \tag{3.13}
$$



At the sole exceptional pair, exact arithmetic gives



$$
E_{10}^*=-\frac{14259854752042485871640576}{221820599898513},
 \qquad v_{19}(E_{10}^*)=1.                                \tag{3.14}
$$



Equations (3.8)--(3.14) prove that the only possible pole in (1.3) is the
simple boundary pole already absorbed into $B_H$.

## 4. Complete finite coefficient-drop table

The checker factors all twelve fixed integers
$\widehat R_k(2),\widehat R_k(4),\widehat R_k(6)$. Combining those
factorizations with the complete Item 296 linear atlas gives every
coefficient that vanishes after the compulsory boundary factor $p$
has been removed:



$$
\begin{array}{c|r|l}
s&p&\text{coefficients absent from the reduced relation}\\ \hline
2&19&Q_0,\ Q_1/p,\ Q_2,\ Q_3\\
2&15131&Q_3\\
2&84211&Q_2\\
2&103423&Q_0\\
4&79&Q_1,\ Q_2/p\\
4&15131&Q_0\\
6&787067&Q_3/p\\
6&1960627367&Q_2.
\end{array}                                                 \tag{4.1}
$$



These are exact factorizations of fixed core values, not results of an
actual-row prime scan.

At $(s,p)=(2,19)$, the first boundary reduction is $0=0$. At
$(2,103423)$ and $(4,15131)$, the $Q_0E_h^*$ term is absent, so
this boundary relation alone imposes no condition on the target
$E_h^*$. At $(6,787067)$, the boundary term is absent and one
relation remains among the three actual values on $s=6,4,2$. All
other finite drops still leave at least two auxiliary values. No row in
(4.1) yields a one-term nonzero constraint on $E_h^*$.

## 5. The three explicit reduced relations

The instances of (1.3) are



$$
\begin{array}{ll}
s=2:&Q_0E_h^*+(Q_1/p)B_{h+3}+Q_2E_{h+6}^*+Q_3E_{h+9}^*=0,\\
s=4:&Q_0E_h^*+Q_1E_{h+3}^*+(Q_2/p)B_{h+6}+Q_3E_{h+9}^*=0,\\
s=6:&Q_0E_h^*+Q_1E_{h+3}^*+Q_2E_{h+6}^*+(Q_3/p)B_{h+9}=0,
\end{array}\qquad(\bmod p).                                \tag{5.1}
$$



On $s=6$, the first three values are actual rows $s=6,4,2$. On
$s=4$, two are actual and one is an outside-but-integral auxiliary
value. On $s=2$, only the target is actual. In every generic case the
boundary scalar survives with unit coefficient. Thus (5.1) is an exact
actual-orbit relation but not a scalar descent or fixed-diagonal
nonvanishing mechanism.

The obstruction is narrowly scoped: it refutes only the proposed use of
the structural coefficient zero as an automatic order drop. It does not
rule out proving that the particular hypergeometric residue (3.3), or a
new combination of the neighboring actual values, has additional
sequence-specific structure.

## 6. Capacity and strict labels

No actual $E_h^*$ gate is removed or sparsified. Therefore



$$
\boxed{\text{new linear log rate}=0,\quad
       \text{new divisibility exponent}=0,\quad
       \text{capacity booked}=0.}                            \tag{6.1}
$$



The retained conditional $j=1$ ceiling is $1/36$ per $6m$.
Moving-prime nonvanishing, weighted density, Route 1, and every
conclusion about $e+\pi$ remain open.

## 7. Reproducibility

From the archive root:

~~~text
python scripts/item297_j1_structural_ray_boundary_certificate.py --output results/item297_j1_structural_ray_boundary_certificate.replay.json
~~~

The checker uses exact standard-library rational, integer-factorization,
and finite-sum arithmetic. It performs no actual-row prime scan.

- **PROVED:** (1.3), (2.1)--(2.2), (3.2)--(3.6), and the complete drop
  table (4.1).
- **OPEN:** any nonvanishing or density theorem for the pinned actual
  $E_h^*$ orbit.
- **NOT CLAIMED:** that a missing coefficient makes the other actual
  values free in the global sequence; only the displayed boundary
  relation loses that constraint.
