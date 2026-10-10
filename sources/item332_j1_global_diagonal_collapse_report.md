> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 332 — global diagonal collapse of the fixed-(j=1) cubic carriers

Date: 2026-09-01

## 1. Outcome and capacity first

Item 329 expresses the factor actually selected by the ordinary
fixed-(j=1) collision as one coefficient of the fixed cubic power



$$
P(t)^{4M},\qquad P(t)=2-4t+3t^2-t^3.                       \tag{1.1}
$$



This item determines what that coefficient becomes on the true moving
row.  Put



$$
F(t)={P(t)\over2}=1-2t+{3\over2}t^2-{1\over2}t^3           \tag{1.2}
$$



and define the characteristic-zero diagonal



$$
\boxed{
 b_h=[t^{2h}]F(t)^{4h/3}.}                                  \tag{1.3}
$$



The main theorem is the exact identity over $\mathbb Q$



$$
\boxed{
 c_h^*={2(4h+3)\over3}\,b_h\qquad(h\geq1).}                \tag{1.4}
$$



On every actual row



$$
M=3h+4s+2,\qquad p=4h+6s+3,                               \tag{1.5}
$$



the normalized Item-329 carrier satisfies



$$
\boxed{
 2^{-4M}K_{M,2h}\equiv b_h\pmod p.}                        \tag{1.6}
$$



Every displayed denominator and every factor connecting $b_h$,
$c_h^*$, and $K_{M,2h}$ is a $p$-unit.  Consequently the bridge
from the original collision is exactly



$$
\boxed{
\text{ordinary collision}\Longrightarrow c_h^*=0
\quad\Longleftrightarrow\quad b_h=0
\quad\Longleftrightarrow\quad K_{M,2h}=0\pmod p.}          \tag{1.7}
$$



Every zero in (1.7) is taken modulo $p$; the identity (1.4) itself is
the separate characteristic-zero statement over $\mathbb Q$.

Thus the fixed cubic Cartier carrier is a valuable new representation of
the old selected factor, but it is not a new independent period.

The dual carrier collapses as well.  An explicit rational number $j_s$
defined below satisfies $j_s=-3A_s$ exactly, where $A_s$ is Item 308's
coefficient and $X_s=2^{2s}A_s$.  With



$$
\overline L_{M,p}=2^{-4M}L_{M,p},                           \tag{1.8}
$$



one has



$$
\boxed{
 \overline L_{M,p}\equiv-3X_s+(4h+3)b_h\pmod p.}           \tag{1.9}
$$



Hence $K$ and $L$ recover precisely the selected and opposite
Item-308 factors.  They do not increase codimension.

No weighted zero-density theorem for $b_h$ is proved.  Therefore



$$
\boxed{
 \text{new linear log rate}=0,\qquad
 \text{new fixed-}j=1\text{ capacity reduction}=0.}        \tag{1.10}
$$



The retained ceiling remains $1/36$ per $6M$.

## 2. Exponent reduction on the actual row

For any unit series $G(t)=1+U(t)$, any rational exponent $a$, and any
integer $n\geq0$,



$$
[t^n]G(t)^a
 =\sum_{k=0}^n{a\choose k}[t^n]U(t)^k.                      \tag{2.1}
$$



Thus the coefficient is a polynomial in $a$ of degree at most $n$,
written in the binomial basis.  If $n<p$, all $k!$ in (2.1) are
$p$-units, so the coefficient depends only on $a\bmod p$.

For (1.5), put $n=2h$.  Direct calculation gives



$$
4M-{4h\over3}={8p\over3},\qquad n=2h<p.                   \tag{2.2}
$$



Because



$$
2^{-4M}K_{M,2h}=[t^{2h}]F(t)^{4M},                        \tag{2.3}
$$



equations (2.1)--(2.3) prove (1.6).  Moreover



$$
4M+1-{4h+3\over3}={8p\over3}.                             \tag{2.4}
$$



Combining (2.4) with Item 329's selected-factor formula



$$
c_h^*\equiv(4M+1)2^{1-4M}K_{M,2h}\pmod p                 \tag{2.5}
$$



already predicts the reduction of $c_h^*$ to the right side of (1.4).
The next section proves that relation exactly in characteristic zero.

## 3. Exact characteristic-zero Hermite collapse

Retain Item 237's polynomials



$$
Q(y)=1+y+{y^2\over2},\qquad
 A(y)={20+14y+4y^2\over3},\qquad
 B(y)=2-5y-3y^2.                                           \tag{3.1}
$$



Its exact selected residual is



$$
c_h^*=[y^{2h}](1+y)^{-2h-1}Q(y)^{(4h+3)/3}
                          \bigl(hA(y)+B(y)\bigr).           \tag{3.2}
$$



Let



$$
H_h(y)=(1+y)^{-2h-1}Q(y)^{4h/3}                           \tag{3.3}
$$



and



$$
R(y)=-{1\over2}(y+1)(y+2)(y^2+2y+2).                     \tag{3.4}
$$



Writing $\vartheta_y=y\,d/dy$, direct rational differentiation gives
the all-$h$ identity



$$
\boxed{
 Q(y)\bigl(hA(y)+B(y)\bigr)-{2(4h+3)\over3}
 =H_h(y)^{-1}(\vartheta_y-2h)\bigl(R(y)H_h(y)\bigr).}      \tag{3.5}
$$



The coefficient of $y^{2h}$ on the right side vanishes identically.
Therefore



$$
c_h^*={2(4h+3)\over3}[y^{2h}]H_h(y).                      \tag{3.6}
$$



Now make the exact residue substitution



$$
t={y\over1+y},\qquad
 F\!\left({y\over1+y}\right)={Q(y)\over(1+y)^3}.          \tag{3.7}
$$



The Jacobian contributes $(1+y)^{2h-1}$ to the coefficient of degree
$2h$, and hence



$$
[t^{2h}]F(t)^{4h/3}=[y^{2h}]H_h(y).                       \tag{3.8}
$$



Equations (3.6)--(3.8) prove (1.4) for every $h$, not by interpolation
or by a finite congruence check.

## 4. One fixed algebraic diagonal and the old degree-six curve

Set



$$
\psi(t)=F(t)^{2/3},\qquad \psi(t)^3=F(t)^2.               \tag{4.1}
$$



Then



$$
b_h=[t^{2h}]\psi(t)^{2h}.                                 \tag{4.2}
$$



For the full diagonal, define



$$
a_n=[t^n]\psi(t)^n,qquad
 \mathcal A(x)=\sum_{n\geq0}a_nx^n.                       \tag{4.3}
$$



Let $T=T(x)$ be the unique formal Lagrange solution



$$
T=x\psi(T).                                               \tag{4.4}
$$



Lagrange inversion gives



$$
\boxed{
 \mathcal A(x)={xT'(x)\over T(x)}
 ={1\over1-T\psi'(T)/\psi(T)}.}                           \tag{4.5}
$$



Under the substitution (3.7),



$$
{t\over\psi(t)}={y(1+y)\over Q(y)^{2/3}},                 \tag{4.5a}
$$



which is exactly Item 237's algebraic change of variable.  Thus the
following curve is not merely another curve of the same degree; it is the
old parametrized curve in the $t$-coordinate.

In the present case



$$
4T^3=x^3P(T)^2,                                           \tag{4.6}
$$



and the rational readout in (4.5) is



$$
{ -3T^3+9T^2-12T+6\over 3T^3-3T^2-4T+6}.                \tag{4.7}
$$



Thus the diagonal lies on one fixed degree-six algebraic curve.  Its even
section is



$$
\mathcal B(z)=\sum_{h\geq0}b_hz^h
 ={\mathcal A(\sqrt z)+\mathcal A(-\sqrt z)\over2}.        \tag{4.8}
$$



With the harmless formal extension (c_0^*=2), equation (1.4) becomes the
generating-series identity



$$
\sum_{h\geq0}c_h^*z^h
 =2\mathcal B(z)+{8\over3}z\mathcal B'(z).                 \tag{4.9}
$$



This is the structural reason the Item-329 Cartier carrier creates no new
period: its moving-index diagonal recovers Item 237's already pinned
algebraic residual on the same degree-six curve.

## 5. The dual $J/L$ carrier collapses to the opposite old factor

Let



$$
m=2s+5,\qquad \mu_s=-{2s+1\over4},                        \tag{5.1}
$$



and define



$$
j_s=[x^m]R_{\mu_s}(1+x)(1+x^2)^{-2s-1}
                         (1+x)^{3s+1/2}.                    \tag{5.2}
$$



Item 329's quintic satisfies the exact identity



$$
R_{\mu_s}(t)=3N_s(t).                                     \tag{5.3}
$$



Comparison with Item 308's definition



$$
A_s=-[x^{2s+5}]{(1+x)^{3s+1/2}N_s(1+x)\over(1+x^2)^{2s+1}}
                                                                    \tag{5.4}
$$



therefore gives, over $\mathbb Q$,



$$
\boxed{
 j_s=-3A_s,\qquad X_s=-{2^{2s}\over3}j_s.}                \tag{5.5}
$$



On the actual row,



$$
M-\mu_s={3p\over4},\qquad
 4M-(-2s-1)=3p,\qquad
 (-6M-1)-(3s+1/2)=-{9p\over2}.                             \tag{5.6}
$$



Because $m<p$, the same binomial-basis argument as in Section 2 applies
to every exponent and to the linear parameter in $R_M$.  It proves



$$
\boxed{
 J_{M,2s+5}\equiv j_s\pmod p.}                             \tag{5.7}
$$



Also, $4M=3p-2s-1$ and Fermat's theorem give



$$
2^{-4M}\equiv2^{2s-2}\pmod p.                            \tag{5.8}
$$



Since Item 329 defines



$$
L_{M,p}=4J_{M,2s+5}+3(4M+1)K_{M,2h},                    \tag{5.9}
$$



equations (1.6), (2.4), and (5.5)--(5.8) yield (1.9).  In
particular,



$$
-{2\over3}\overline L_{M,p}
 \equiv2X_s-c_h^*=c^-_{h,s}\pmod p.                       \tag{5.10}
$$



The complete zero chart is therefore



$$
\boxed{
\begin{aligned}
\text{selected original factor:}\quad
 &p\mid K_{M,2h}\Longleftrightarrow p\mid b_h,\\
\text{opposite factor:}\quad
 &p\mid L_{M,p}
   \Longleftrightarrow p\mid\bigl(-3X_s+(4h+3)b_h\bigr),\\
\text{full container:}\quad
 &p\mid D_{s,\epsilon}
   \Longleftrightarrow
   p\mid b_h\ \text{or}\\
   p\mid\bigl(-3X_s+(4h+3)b_h\bigr).
\end{aligned}}                                             \tag{5.11}
$$



Only the first line is forced by the original ordinary collision.

## 6. Denominators and the exact integer normalization

The unit algebraic series $\psi$ in (4.1) belongs to
$\mathbb Z[1/6][[t]]$.  Indeed, after all lower coefficients have been
determined, the coefficient of degree $r$ in $\psi^3=F^2$ has the
form



$$
3\psi_r+\text{a polynomial in }\psi_1,\ldots,\psi_{r-1}.  \tag{6.1}
$$



This proves inductively that no denominator prime other than $2$ or
$3$ occurs.  Equivalently, the binomial expansion of $F^{2/3}$ gives
an exponential denominator bound degree by degree.  Hence



$$
b_h\in\mathbb Z[1/6].                                     \tag{6.2}
$$



Equation (5.2), together with the half-binomial denominator bound, proves
similarly that



$$
j_s\in\mathbb Z[1/6].                                     \tag{6.3}
$$



Every actual prime is at least $13$, so these denominators are units.

There is also an exact integer normalization of the cubic coefficient:



$$
\boxed{
 \kappa_{M,h}=2^{h-4M}K_{M,2h}\in\mathbb Z.}              \tag{6.4}
$$



To prove it, substitute $t=\sqrt2u$:



$$
\kappa_{M,h}=[u^{2h}]
 \bigl(1-2\sqrt2u+3u^2-\sqrt2u^3\bigr)^{4M}.              \tag{6.5}
$$



Every monomial of even total degree contains an even number of the two
odd-degree $\sqrt2$-terms, so its contribution is integral.  On the
actual row,



$$
\boxed{
 \kappa_{M,h}\equiv2^h b_h\pmod p.}                       \tag{6.6}
$$



Thus even the strongest immediate power-of-two normalization leaves the
same old diagonal target.

## 7. Capacity audit and scoped no-go

The exact fixed-$M$ support has raw logarithmic mass



$$
{M\over6}+o(M),                                           \tag{7.1}
$$



or $1/36$ per $6M$.  The present identities do not reduce it.

First, a bounded collection of fixed $h$-targets or fixed $s$-targets
contains only $O(1)$ rows at fixed $M$, hence at most
$O(\log M)=o(M)$ raw mass.  Such targets cannot control the isolated
bulk.

Second, the fixed algebraic descriptions and Eisenstein--Cauchy bounds give



$$
\log\max\{1,|\operatorname{num}(b_h)|\}=O(h),\qquad
 \log\max\{1,|\operatorname{num}(j_s)|\}=O(s).            \tag{7.2}
$$



But $h=3M-2p$ and $s$ both move through $\Theta(M)$ rows.  Summing
the componentwise bounds in (7.2) gives only $O(M^2)$, while taking the
minimum with (7.1) simply returns the raw bound.

Most importantly, Sections 2--5 prove the following global, sharply scoped
no-go:



$$
\boxed{
\begin{gathered}
\text{normalizing the Item-329 }K,J,L\text{ carriers by their constant}\\
\text{powers and reducing their exponent parameters modulo the actual }p\\
\text{below the target degree recovers exactly }c_h^*\text{ and }2X_s-c_h^*;\\
\text{it cannot by itself create a new independent condition or codimension.}
\end{gathered}}                                             \tag{7.3}
$$



This closes the natural strategy of treating the reduced fixed algebraic
coefficient as a second period.  It does **not** close the specific
arithmetic of $b_h$.  Prime-factor localization, average-gcd bounds,
monodromy, or a weighted non-concentration theorem for



$$
\sum_{\substack{p\text{ in the actual interval}\\
                  p\mid\operatorname{num}(b_{3M-2p})}}
 \log p=o(M)                                                \tag{7.4}
$$



remain admissible and would close the original fixed-$j=1$ scalar gate.

## 8. Exact controls and strict labels

The deterministic checker replays the same five rows preselected in
Item 329.  Here bars denote multiplication by $2^{-4M}$ modulo $p$:



$$
\begin{array}{c|cc|ccc|cc}
(M,h,s,p)&b_h&j_s&\overline K&J&\overline L&c^+&c^-\\ \hline
(9,1,1,13)&0&7&0&7&2&0&3\\
(12,2,1,17)&9&16&9&16&10&15&16\\
(34,8,2,47)&0&6&0&6&2&0&30\\
(30,4,4,43)&42&12&42&12&0&16&0\\
(32,2,6,47)&14&0&14&0&13&40&7.
\end{array}                                                 \tag{8.1}
$$



All entries in (8.1) are residues modulo the displayed prime.

- **PROVED:** the exact identity (1.4); the normalized actual-row bridge
  (1.6); the fixed diagonal and degree-six curve (4.1)--(4.8); the exact
  dual collapse (5.5); the normalized $L$-chart (1.9); denominator support
  at $2,3$; the integer normalization (6.4); and the scoped global no-go
  (7.3).

- **SCOPED FROBENIUS/FIXED-TARGET NO-GO:** exponent reduction of these
  carriers recovers the old selected/opposite rank-one factors and cannot
  be booked as new codimension.  The sequence-specific arithmetic of the
  resulting diagonal is not closed.

- **EXACT FINITE ONLY:** the five preselected rows in (8.1).  No scan or
  finite census is used asymptotically, and no row is promoted to a new
  full Item-264 collision.

- **OPEN:** (7.4); weighted density for the opposite factor if the larger
  container envelope is pursued; $\mathcal W_{\rm off}(M)=o(M)$;
  $\mathcal W_D(M)=o(M)$; fixed-$j=1$ closure; Route 1; and every
  conclusion about $e+\pi$.

- **NOT CLAIMED:** universal nonvanishing; sublinear carrier height; a new
  independent period; a monodromy or average-gcd theorem; a prime scan;
  positive capacity; or any ledger improvement.

The ledger remains



$$
\boxed{
 \text{capacity booked}=0,\qquad
 \text{fixed-}j=1\text{ ceiling}={1\over36}\text{ per }6M.} \tag{8.2}
$$



No canonical, master, or status file is edited by this research package.

## 9. Deterministic replay

From the archive root, run

~~~text
python work/item332_j1_global_diagonal_collapse_certificate.py --output work/item332_j1_global_diagonal_collapse_certificate.replay.json
~~~

The checker pins canonical Items 237, 308, and 329.  It proves the Hermite
identity in $\mathbb Q(h,y)$, checks the actual-row exponent identities,
reconstructs the degree-six Lagrange curve and rational readout, proves
$R_{-(2s+1)/4}=3N_s$, reconstructs all five exact rational $b_h,j_s$
controls, and checks the normalized $K,J,L$ and selected/opposite factor
charts.  It performs no prime scan.
