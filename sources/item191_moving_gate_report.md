> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 191 — actual lift gates on the moving rank-two determinant locus

Checked: 2026-08-30 (Beijing time)

## 1. Scope and outcome

Stay in the Item 174/180 cell



$$
2m=jp+s,\qquad p\ge7,\qquad
 0\le s\le(p-1)/3,\qquad s\equiv j\pmod2,
\tag{1.1}
$$



with $p\le4m+1<p^2$, $\kappa=0$, and the moving entry condition



$$
\Delta_{p,s}=0.                \tag{1.2}
$$



This item separates two logically different supports:

1. **entry support:** the primes satisfying (1.2);
2. **lift support:** the nested subsets on which $A_0=0$, and then
   $A_0=A_1=B_0=0$.

The entry-support problem remains open.  In particular, no positive weighted
mass of determinant roots is proved here.

> **PROVED — actual scalar-free gate formula.**  The three digits
> $A_0,A_1,B_0$ on every moving row are given exactly by the local Hasse
> recurrence (2.2), the endpoint sums (2.3), and the determinant carry
> (2.5)--(2.7).  No Cartier scalar is divided by, so proportional nonzero
> rows and zero rows are treated uniformly.

> **PROVED — regular high-$j$ lift tail.**  On every determinant-zero row
> satisfying
> 

$$
>                   3j-1\ge p,\qquad2j+2\le p,          \tag{1.3}
>
$$


> the first relative Bockstein is exact and
> 

$$
>                         \boxed{A_0=B_0=0}.             \tag{1.4}
>
$$


> Thus $p^2\mid c_m$.  The next digit $A_1$ is not forced.

> **PROVED — capacity of this tail is zero.**  Conditions (1.1), (1.3)
> imply $6m\ge p(p+1)$.  Hence the logarithmic weight of all primes
> accessible to (1.4) is $O(\sqrt m)=o(m)$.  Any fixed number of further
> copies on this tail still has zero exponential rate.

> **PROVED COMPUTATION — finite actual-family witnesses.**  Exact Hasse
> reconstruction for every entry root $p\le71$ and every admissible $j$
> gives 138 rows.  All 41 regular-tail rows obey (1.4).  Three rows pass the
> cubic gate; two lie in the proved regular tail:
> 

$$
> (m,p,s,j)=(404,47,9,17),\qquad(859,71,14,24).         \tag{1.5}
>
$$


> Thus $47^3\mid c_{404}$ and $71^3\mid c_{859}$ by the frozen
> normalization ledger.  Other regular-tail rows, for example
> $(m,p,s,j)=(34,13,3,5)$, have $A_1\ne0$.  The tail hypotheses therefore
> realize both outcomes in the actual family and do not force a cubic copy.

**OPEN.**  Positive weighted determinant-root mass, positive weighted
second- or third-layer mass away from (1.3), and any usable fourth/fifth
layer remain unproved.  Finite survival proportions are not extrapolated.
Nothing here decides the arithmetic nature of $e+\pi$.

## 2. Exact archive-native coordinates

Put $k_0=4m+1$, $k_1=k_0+1$.  For a pole



$$
\xi\in\{-1,i,-i\},\qquad
 U_\xi(t)=u(\xi+t),\qquad V_\xi(t)=Q(\xi+t)/t,
$$



define



$$
C_{\nu,\xi,r}=[t^r]\frac{U_\xi(t)^{6m}}
                              {V_\xi(t)^{k_\nu}}.
\tag{2.1}
$$



These coefficients are not obtained by an inexact power-series division.
Writing $D=U_\xi V_\xi$ and



$$
W=6m\,U_\xi'V_\xi-k_\nu U_\xi V_\xi',
$$



logarithmic differentiation gives the exact recurrence



$$
D(t)C'(t)=W(t)C(t).                                   \tag{2.2}
$$



Coefficient comparison determines $C_{r+1}$ from earlier coefficients.
When $r+1$ contains a factor of $p$, the implementation keeps the exact
factorial valuation as precision reserve before performing the exact
division.  This proves, rather than assumes, the required $p^4$ precision.

The endpoint coordinates modulo $p^4$ are



$$
\begin{aligned}
 L_\nu&=4C_{\nu,-1,k_\nu-1}
       +4\Re C_{\nu,i,k_\nu-1},\\
 E_\nu&=-4\Im C_{\nu,i,k_\nu-1},                       \tag{2.3}
\end{aligned}
$$



and, with



$$
h_\xi(n)=(-\xi)^{-n}-(1-\xi)^{-n},
$$





$$
X_\nu=pR_\nu=
 \sum_{n=1}^{k_\nu-1}\frac pn
 \sum_{\xi\in\{-1,i,-i\}}
 C_{\nu,\xi,k_\nu-1-n}h_\xi(n).                       \tag{2.4}
$$



In the $e=1$ range, $v_p(n)\le1$; consequently every $p/n$ in
(2.4) is interpreted as the integral factor
$p^{1-v_p(n)}(n/p^{v_p(n)})^{-1}$ in $\mathbb Z_p$.  Conjugate terms
make (2.3)--(2.4) rational.

Write the canonical digits



$$
L_\nu=\sum_r\ell_{\nu,r}p^r,\quad
 X_\nu=\sum_rx_{\nu,r}p^r,\quad
 E_\nu=\sum_re_{\nu,r}p^r.                             \tag{2.5}
$$



For the $A$-minor define



$$
S^A_r=\sum_{h=0}^r
 (\ell_{1,h}x_{0,r-h}-\ell_{0,h}x_{1,r-h}),
 \qquad q^A_{-1}=0,                                    \tag{2.6}
$$





$$
\tau^A_r\equiv S^A_r+q^A_{r-1}\pmod p,\quad
 0\le\tau^A_r<p,\qquad
 q^A_r={S^A_r+q^A_{r-1}-\tau^A_r\over p}.              \tag{2.7}
$$



Use the same construction with $x_{\nu,r}$ replaced by
$e_{\nu,r}$ for $\tau^B_r$.  The quotient in (2.7) is an ordinary
integer carry, possibly negative.  Since (1.2) is exactly the entry
condition, $\tau^A_0=\tau^B_0=0$, and



$$
\boxed{A_0=\tau^A_1,\quad
                     A_1=\tau^A_2,\quad
                     B_0=\tau^B_1.}                    \tag{2.8}
$$



Equations (2.1)--(2.8) are the requested actual formulas.  They depend on
$(m,p)$, not just on the first Cartier row, and they retain every lower
Hasse band and determinant carry.

## 3. Proof of the regular lift tail

Let



$$
P_1=x^{3s}(1-x)^{3s}Q^{p-2s-2},\qquad P_0=QP_1.      \tag{3.1}
$$



Their degrees are $3p-6$ and $3p-3$.  The first Cartier images are the
two Item 174 rows, and (1.2) says their exterior product vanishes.  Therefore
every integral lift of a mod-$p$ null relation has $p$-divisible
resonant coefficients at $x^{p-1}$ and $x^{2p-1}$.  These are exactly
the problematic primitive denominators: the polynomial degree is at most
$3p-3$, so among $1,\ldots,3p-2$, only $p$ and $2p$ are divisible
by $p$.  At the first resonance the coefficient is a multiple of $p$.
At the second it is a multiple of $p$, and division by the remaining
factor $2$ is permitted because $p$ is odd.  Every other primitive
denominator is a $p$-adic unit.  Hence the null combination has a
$p$-integral primitive $T$ of degree at most $3p-2$.

This construction uses the row kernel as a module and never chooses or
inverts a nonzero row entry.  If the Cartier matrix has rank one, its one
kernel relation is lifted.  If one or both Cartier rows vanish, the larger
kernel supplies the corresponding independent relations; the argument
below applies to each.  Thus zero-row cases are included, not removed by a
pivot convention.

Set



$$
F={u^{3j}\over Q^{2j+1}},\qquad
 N=T\{3j\,u'Q-(2j+1)Q'u\}.                             \tag{3.2}
$$



Then $\deg N\le3p+2$.  The four-section Cartier filter gives the first
relative Bockstein differential



$$
\Phi=\mathcal C(F^{p-1}F'T\,dx)
      ={u^{3j-1}H\over Q^{2j+2}}\,dx,                  \tag{3.3}
$$



where



$$
H(x)=\sum_{r=0}^6
 \left(\sum_{z=0}^{p-1}[x^{pr-4z}]N\right)x^r,
 \qquad\deg H\le6.                                    \tag{3.4}
$$



The degree bound follows directly: for $r=7$, the smallest possible
index $7p-4(p-1)=3p+4$ is already larger than $\deg N$.

Under (1.3), (3.3) becomes



$$
\Phi=\left({u\over Q}\right)^p
 u^{3j-1-p}H Q^{p-2j-2}\,dx.                           \tag{3.5}
$$



The residual factor is a polynomial of degree at most



$$
2(3j-1-p)+6+3(p-2j-2)=p-2.                            \tag{3.6}
$$



In characteristic $p$, every differential $f^pG(x)\,dx$ with
$\deg G\le p-2$ is exact.  Hence (3.5) is exact.  To make its control of
the scalar-free wedges explicit, let $\Omega$ be any lifted null
combination.  Integration by parts gives



$$
\Omega=d(F^pT)-p\Psi,\qquad
 \mathcal C\Psi=\Phi.                                  \tag{3.7}
$$



Because $F$ vanishes at both endpoints, the exact boundary term in
(3.7) contributes no endpoint coordinate.  Exactness of $\Phi$ gives
$L(\Psi)\equiv E(\Psi)\equiv0\pmod p$.  Therefore



$$
L(\Omega),E(\Omega)\equiv0\pmod {p^2},\qquad
 X(\Omega)=pR(\Omega)=-p^2R(\Psi)\equiv0\pmod {p^2}.   \tag{3.8}
$$



For a rank-one Cartier matrix, (3.8) lifts its unique row relation modulo
$p^2$, so every two-by-two endpoint minor vanishes modulo $p^2$.  For
a zero row or a rank-zero matrix, applying (3.8) to a basis of the larger
kernel gives the same conclusion directly.  Thus both the $A$- and
$B$-wedges acquire one further power of $p$ in every case, which is
precisely (1.4) by (2.8).

The argument stops at $A_1$: it is the next Hasse digit plus the carry
in (2.7).  Exactness of (3.5) gives no identity for it.  The actual-family
counterpair in Section 5 confirms that this is not merely an ambient
freedom statement.

## 4. Entry mass, lift mass, and capacity

For a fixed $m$, define nested prime sets



$$
\begin{aligned}
 Z_1(m)&=\{p:\Delta_{p,s}=0\},\\
 Z_2(m)&=\{p\in Z_1(m):A_0=0\},\\
 Z_3(m)&=\{p\in Z_2(m):A_1=B_0=0\}.                    \tag{4.1}
\end{aligned}
$$



Their certified contribution is



$$
\sum_{p\in Z_1(m)}\log p+
 \sum_{p\in Z_2(m)}\log p+
 \sum_{p\in Z_3(m)}\log p.                            \tag{4.2}
$$



Thus a lift theorem has no value without an entry-support theorem.  Item 180
proves only the conditional statement that $r_p=o(p)$ would make the
mean entry mass zero-rate.  Neither that root-count hypothesis nor positive
entry mass is proved.

For the only uniform lift family obtained here, (1.3) and (1.1) give



$$
6m=3jp+3s\ge p(p+1),                                  \tag{4.3}
$$



so



$$
\sum_{p\text{ in the tail}}\log p
 \le\vartheta(\sqrt{6m})=O(\sqrt m).                  \tag{4.4}
$$



This is zero after division by (6m), even if every tail entry passed any
fixed number of deeper gates.

For scale, the absolute rank-two entry ceiling from Item 168 is



$$
C_2=6-\pi/\sqrt3-3\log3
   =0.8903637697\ldots\quad\text{per }m.                \tag{4.5}
$$



Hence even the impossible optimistic assumption that every rank-two
candidate is an entry root and every one is cubic has capacity only



$$
{3C_2\over6}=0.4451818849\ldots\quad\text{per }6m.     \tag{4.6}
$$



This is below the current unresolved Route-1 amount
$1.0196329836\ldots$ per $6m$.  Item 168's still stronger all-cell
cubic ceiling is also below the full threshold.  A successful Route-1
argument therefore needs positive entry mass plus substantially deeper
layers, or an independent sequential-matching gain.

## 5. Exact finite replay

The certificate scans every prime $7\le p\le71$, every admissible
determinant root $s$, and every $j$ allowed by (1.1) and
$4m+1<p^2$.  It reconstructs every coordinate modulo $p^4$.



$$
\begin{array}{l|r}
\text{entry groups }(p,s)&14\\
\text{actual rows }(p,s,j)&138\\
\text{rows with }A_0=0&54\\
\text{regular-tail rows}&41\\
\text{regular-tail failures of }A_0=B_0=0&0\\
\text{cubic-gate rows}&3
\end{array}                                             \tag{5.1}
$$



The cubic rows are



$$
\begin{array}{c|c|c|c|c}
m&p&s&j&\text{scope}\\\hline
404&47&9&17&\text{regular tail}\\
859&71&14&24&\text{regular tail}\\
1112&67&13&33&\text{outer value }2j+2>p.
\end{array}                                             \tag{5.2}
$$



The last row is an exact finite witness but is outside theorem (1.3).
There are 90 finite rows on the $3j-1<p$ side; six have $A_0=0$, and
none passes the cubic gate.  These counts are diagnostics only.  They do
not estimate a limiting survival probability, and most entry groups in
this small range lie on already-known thin affine rays.

## 6. Classification and artifacts

**PROVED**

- the actual Hasse-coordinate and scalar-free carry formulas
  (2.1)--(2.8);
- the conditional-on-entry regular tail (1.3)--(1.4);
- the zero-capacity bound (4.3)--(4.4);
- the exact finite gate witnesses (1.5), (5.2).

**EXPERIMENTAL / FINITE ONLY**

- all gate frequencies and interpolation behavior for $p\le71$;
- the outer cubic row in (5.2) as evidence for a possible boundary formula;
- any suggestion that $A_1$ is random or equidistributed.

**OPEN**

- positive weighted mass of $Z_1(m)$, pointwise or in a form usable by
  the content ledger;
- positive weighted mass of $Z_2(m)$ or $Z_3(m)$ outside the small tail;
- a uniform formula for $A_1$, including the outer boundary;
- fourth/fifth layers with sufficient capacity;
- the arithmetic nature of $e+\pi$.

Portable staged artifacts:

- `sources/item191_moving_gate_report.md`
- `scripts/item191_moving_gate_certificate.py`
- `results/item191_moving_gate_certificate.json`
- `results/item191_moving_gate_certificate_replay.json`
- `results/item191_moving_gate_hashes.sha256`

The certificate resolves Item 163 dependencies beside itself after archival,
and otherwise uses the pinned desktop archive.  It uses only standard-library
integer arithmetic.  Canonical and replay runs with the same parameters must
be byte-identical.
