> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 306 — all-$n$ normalized ordinary-$j=2$ $M$-bridge

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain Item 291's ordinary-$j=2$ connection minor



$$
M_r=-11\det\begin{pmatrix}f_0&d_0\\ f_1&d_1\end{pmatrix},
 \qquad r=6n+e,\quad e\in\{1,5\},
$$



and Item 294's gauge $g_0=1$,



$$
\frac{g_n}{g_{n+1}}=\mathcal R(r),\qquad
 \mathcal R(r)=
 \frac{r(r+6)(2r+9)^2(2r+15)^2}
 {78732(r+1)^2(r+2)(r+4)(r+5)^2}.
$$



Let $C(x)$ be Item 237's certified algebraic series.

> **PROVED — all-$n$ normalized-$M$ bridge.**  On both ordinary
> rays and for every $n\geq0$,
> 

$$
> \boxed{
> \frac{16^nM_{6n+e}}{g_n}
>   =\lambda_e[x^{6n+e}]C(x)},
> \qquad
> \lambda_1=-\frac{891}{100},\quad
> \lambda_5=\frac{3897234}{41405}.
>
$$



The proof is not an extrapolation from the old finite fit.  It consists of
eight cleared Hermite identities over $\mathbb Q(r)$, an exact
meromorphic-beta endpoint lemma, three identically zero tensor numerators,
and three exact initial identities on each ray.

This proves recurrence membership and identifies the normalized $M$ line.
It does **not** realize the independent $L$ minor, prove moving-prime
nonvanishing, or supply a weighted-density theorem.  Hence



$$
\boxed{\text{new booking}=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling}=1/105\text{ per }6M}.
$$



## 2. The exact beta-period determinant

Use the notation of the open checkpoint:



$$
H=\frac{r+1}{2},\qquad b_0=-\frac{2r}{3},\qquad
 b_1=b_0-1,\qquad \rho=\frac{r}{2(2r+3)}.
$$



Put



$$
w_r(u)=u^r(1-u^2)^{b_0-1}(1-iu)^r,
$$



and define the meromorphically continued Euler periods



$$
A_r=\operatorname{FP}\!\int_0^1w_r(u)(1+iu)\,du,\qquad
 B_r=\operatorname{FP}\!\int_0^1w_r(u)
                  \frac{(1+iu)^4}{1-u^2}\,du.
$$



Write $A_r=X+iY$ and $B_r=S+iT$, and let
$\beta(a,b)=B(a,b)$ denote Euler's beta function.  Formula (A) of
the checkpoint gives exactly



$$
\begin{aligned}
 f_0&=\frac{2Y}{\beta(H+1/2,b_0)},&
 f_1&=\frac{2\rho T}{\beta(H+1/2,b_1)},\\
 d_0&=\frac{C_0\kappa_0X}{\beta(H,b_0)},&
 d_1&=\frac{C_1\kappa_1S}{\beta(H,b_1)}.
\end{aligned}
$$



Besides the checkpoint identity



$$
rC_1\kappa_1=(r+3)\rho C_0\kappa_0,
$$



the beta shifts give



$$
\frac{\beta(H+1/2,b_1)\beta(H,b_0)}
 {\beta(H+1/2,b_0)\beta(H,b_1)}=\frac r{r+3}.
$$



Thus the two determinant coefficients coincide, and



$$
M_r=\eta(r)\Omega_r,\qquad
 \Omega_r=\operatorname{Im}(A_r\overline{B_r})=YS-XT,
$$





$$
\eta(r)=-\frac{22\rho C_0\kappa_0}
 {\beta(H+1/2,b_1)\beta(H,b_0)}.
$$



Gamma shifting simplifies its six-step quotient to the rational function



$$
\boxed{
 \frac{\eta(r+6)}{\eta(r)}=
 \frac{64(r+3)(2r+3)(2r+9)}{27r(r+2)(r+4)}.}
 \tag{2.1}
$$



This is the normalization factor that was missing from a raw wedge
comparison.

## 3. Exact endpoint functional

The specialized real integrals can diverge at $u=1$.  The proof does not
discard a literal endpoint value.  It uses the same meromorphic Euler
continuation that defines the normalized beta functionals.

For every monomial primitive, define



$$
\operatorname{FP}\!\int_0^1
 u^{L-1}(1-u^2)^{\gamma-1}\,du
 =\frac12B(L/2,\gamma),
$$



continued meromorphically.  Then



$$
L B(L/2,\gamma+1)=2\gamma B(L/2+1,\gamma),
$$



because both sides become
$L\gamma B(L/2,\gamma)/(L/2+\gamma)$.  Therefore



$$
\operatorname{FP}\!\int_0^1
 \frac d{du}\bigl(u^L(1-u^2)^\gamma\bigr)\,du=0.
 \tag{3.1}
$$



After expanding $(1\mp iu)^{r+1}N(u)$, every exact term in the
Hermite certificates is a finite sum of (3.1).  Hence its selected beta
functional is exactly zero in both conjugate charts and for every shift.
This is a meromorphic gamma identity, not a convergence assertion.

## 4. The eight cleared Hermite identities

Set $x=iu$.  For $q\geq0$, define



$$
\begin{aligned}
 \mathcal T_{r,q}(x^k)={}&(k+r+1)x^k-(k+2r+2)x^{k+1}\\
 &+\left(k-2q-1-\frac r3\right)x^{k+2}
 +\left(2q-k-\frac{2r}{3}\right)x^{k+3}.
\end{aligned}
 \tag{4.1}
$$



For $0\leq m\leq3$, the checker proves



$$
\begin{aligned}
 (-1)^m(1+x)x^{6m}(1-x)^{6m}
 &=(A_{m0}+A_{m1}x+A_{m2}x^2)(1+x^2)^{4m}
   +\mathcal T_{r,4m-1}P^A_m,\\
 (-1)^m(1+x)^4x^{6m}(1-x)^{6m}
 &=(B_{m0}+B_{m1}x+B_{m2}x^2)(1+x^2)^{4m+1}
   +\mathcal T_{r,4m}P^B_m.
\end{aligned}
 \tag{4.2}
$$



The first line at $m=0$ is trivial.  In the second line,



$$
B_0=\left(\frac{5r+6}{2r+3},
                 \frac{5r+12}{2r+3},0\right),\qquad
 P^B_0=-\frac{3(1+x)}{2r+3}.
$$



The primitive degrees are at most $12m-2$ and $12m+1$,
respectively.  In the original variable, the plus-chart remainder is
$A_{m0}+iA_{m1}u-A_{m2}u^2$, and the minus chart is its
conjugate; likewise for $B$.

For a compact exact table, write
$\operatorname{poly}[c_0,\ldots,c_d]=\sum c_kr^k$, and put



$$
\begin{aligned}
 \Delta^A_m&=2^{5m}\prod_{a=1}^{2m}(r+3a)
                  \prod_{a=0}^{2m-1}(2r+3+6a),\\
 \Delta^B_m&=2^{5m}\prod_{a=1}^{2m}(r+3a)
                  \prod_{a=0}^{2m}(2r+3+6a).
\end{aligned}
$$



The checkpoint's $m=1$ $A$-row is recovered exactly.  The missing
$m=2,3$ rows are



$$
\begin{aligned}
 A_2={729\Big(& (r+1)(r+11)U_{20},
 (r+11)U_{21},-5(r+4)(r+11)(2r+3)U_{22}\Big)\over\Delta^A_2},\\
 A_3={19683\Big(& (r+1)(r+17)U_{30},
 -(r+17)U_{31},-5(r+4)(r+17)(2r+3)U_{32}\Big)\over\Delta^A_3},
\end{aligned}
$$



where



$$
\begin{aligned}
U_{20}&=\operatorname{poly}[-89054640,25524720,46689048,15900441,2394959,168711,4441],\\
U_{21}&=\operatorname{poly}[5225472000,8768165760,5864465088,2076552984,423392285,49806965,3136807,81871],\\
U_{22}&=\operatorname{poly}[135216864,135261900,49220877,8373817,676143,20927],\\
U_{30}&=\operatorname{poly}[20942453776536000,36659620567906560,25983743383705104,
10126778772601440,2443313048810400,385180581942555,40452551284507,
2808266695710,123786376150,3137643735,34810639],\\
U_{31}&=\operatorname{poly}[-56470012113715200,-80143286788546560,-41462068740755904,
-8783141729399424,172686277294560,512627515914420,125849309936693,
16293473265893,1276322661890,60720467390,1618359161,18559481],\\
U_{32}&=\operatorname{poly}[2797364967045120,3668964930177120,1979924313051648,
588323588529168,107301069610203,12550060297103,946282931262,
44527495502,1190090967,13798307].
\end{aligned}
$$



The companion rows $B_m$ for $m=1,2,3$ are stored coefficient by
coefficient in the canonical JSON.  In compact form they are



$$
\begin{aligned}
B_1&={27\bigl(-(r+1)V_{10},V_{11},-(r+4)(2r+3)V_{12}\bigr)\over\Delta^B_1},\\
B_2&={729\bigl((r+1)V_{20},V_{21},-(r+4)(2r+3)V_{22}\bigr)\over\Delta^B_2},\\
B_3&={19683\bigl((r+1)V_{30},-V_{31},-(r+4)(2r+3)V_{32}\bigr)\over\Delta^B_3}.
\end{aligned}
$$



All $V_{mk}$ coefficient lists, including the degree-13 $m=3$
cores, are in `hermite_and_tensor.coordinate_rows` of the canonical JSON;
they are inputs to, not outputs guessed from, the terminal proof.

The constructive certificate avoids listing the long primitive numerators.
If $\alpha_j/\Delta$ is a displayed remainder, $Y$ is the left
side of (4.2), $d=(1+x^2)^{q+1}$, and



$$
E_\ell=\Delta[x^\ell]Y-\sum_{j=0}^2\alpha_j[x^{\ell-j}]d,
$$



then a triangular recurrence constructs the primitive.  Its final three
cleared polynomials are identically zero in all eight cases.  Negative
subscripts are defined explicitly as zero; the production checker never
uses Python negative indexing.

## 5. Exact tensor cancellation

For each shift, form the three skew coordinates



$$
W_m=\bigl(A_{m0}B_{m1}-B_{m0}A_{m1},
 A_{m0}B_{m2}-B_{m0}A_{m2},
 A_{m1}B_{m2}-B_{m1}A_{m2}\bigr).
$$



Let $p_0,\ldots,p_3$ be Item 237's proved operator and define



$$
\tau_0=1,\qquad
 \frac{\tau_{m+1}}{\tau_m}
 =16\mathcal R(r+6m)
 \frac{\eta(r+6m+6)}{\eta(r+6m)}.
$$



Direct common-denominator clearing in $\mathbb Q[r]$ gives



$$
\boxed{\sum_{m=0}^3p_m(r/2)\tau_mW_m=(0,0,0).}
 \tag{5.1}
$$



The three production common-denominator degrees are all 106.  Every
cleared numerator coefficient list is empty after trimming, i.e. the zero
polynomial.  No value of $r$ is sampled in this step.

This three-coordinate calculation is exactly the full tensor calculation,
not an exterior-power shortcut.  If $A_{mp},B_{mp}$ are the real
$x$-chart coordinates, their $u$-chart coordinates are
$i^pA_{mp},i^pB_{mp}$.  Hence entry $(p,q)$ of
$(A^+\otimes B^- - B^+\otimes A^-)/(2i)$ is



$$
\frac{i^p(-i)^q}{2i}
 \bigl(A_{mp}B_{mq}-B_{mp}A_{mq}\bigr).             \tag{5.2}
$$



The diagonal entries vanish, and the six off-diagonal entries are fixed
nonzero phases times the three coordinates in $W_m$, with the appropriate
orientation sign.  The production checker also clears and verifies all nine
tensor entries directly; its JSON records their phases and source exterior
coordinates.

By (3.1), the exact terms in (4.2) have zero selected beta functional.
By Section 2, the remaining wedge is exactly $M_r/\eta(r)$.
Consequently, if



$$
Z_n=\frac{16^nM_{6n+e}}{g_n},
$$



then (5.1)--(5.2) are precisely



$$
\sum_{m=0}^3p_m((6n+e)/2)Z_{n+m}=0.
 \tag{5.3}
$$



This proves recurrence membership independently of the finite fit.

## 6. Identification with the algebraic coefficient line

Item 237 proves, for every coefficient index,



$$
\sum_{m=0}^3p_m(r/2)[x^{r+6m}]C(x)=0.
$$



The forward polynomial $p_3(h)$ has strictly positive coefficients;
therefore $p_3(r/2)>0$ for every $r>0$, including the initial
half-integer $h=1/2$.

The checker evaluates the original Item 250 tail definitions, not the new
recurrence, at $n=0,1,2$ on each ray.  All six exact identities agree
with the constants $\lambda_1,\lambda_5$ displayed in Section 1.  Their
row-stream SHA-256 is

~~~text
5fae948e8572fe1efcc16e99d9f1868d76aa8aae89425e8ed0ae41003031d20e
~~~

The common order-three recurrence, its nonzero forward coefficient, and
these three initials prove the bridge for all $n$.  The older rows
$n\geq3$ are now deterministic replays only; they are not theorem
evidence.

## 7. Complete pole and exceptional-parameter audit

The theorem domain is



$$
r=6n+1\quad\text{or}\quad r=6n+5,\qquad n\geq0.
$$



Thus $r>0$, $r$ is odd, and $3\nmid r$.

* The beta parameters $b_0=-2r/3$ and $b_1=b_0-1$ are
  nonintegral.  The Pochhammer denominators audited in Items 250 and 291
  are nonzero.  The excluded beta-resonant class $3\mid r$ is not
  encountered.
* The coordinate denominators have roots
  $r=-3,-6,-9,-12,-15,-18$ and
  $r=-3/2,-9/2,-15/2,-21/2,-27/2,-33/2,-39/2$.
* The displayed primitive coefficients additionally have possible poles
  $r=-1,-2,\ldots,-38$ from rising products.
* For the three required transition steps, the $\eta$-denominator roots
  are $0,-2,-4,-6,-8,-10,-12,-14,-16$.  The gauge-denominator roots
  are
  $-1,-2,-4,-5,-7,-8,-10,-11,-13,-14,-16,-17$.
* All zeros of the gauge and $\eta$ numerators on those same shifts are
  nonpositive.  Hence $g_n$, every normalization step, and the forward
  recurrence coefficient are nonzero over $\mathbb Q$ on every actual ray.

There is no exceptional actual $r$.

## 8. Exploratory bug provenance

One discarded exploratory probe assembled the unshifted $B$-companion
with an index $-1$; Python then read the last list entry.  It produced a
spurious endpoint mismatch.  The correct base row is the $B_0$ displayed
in Section 4.  The production checker uses an explicit zero function for
every negative subscript and contains no negative-index shortcut.  The bug
affected no packaged identity, result, or theorem.

## 9. Ordinary-$j=2$ gate consequence

The proved gain is a translation theorem for one connection minor:



$$
-11\det(f,d)\quad\longleftrightarrow\quad
 \text{a fixed algebraic coefficient line after the exact gauge}.
$$



The full necessary collision determinant is still



$$
D=9c\det(f,b)-11\det(f,d)=L_rc+M_r.
$$



Nothing here gives an algebraic realization for $L_r$, proves that
$D$ or $M_r$ is nonzero modulo every moving row prime, controls the
singular modular gauge layers, or supplies Frobenius/monodromy independence
or a weighted zero-density estimate.  Therefore no part of the raw
ordinary-$j=2$ capacity is removed.

## 10. Reproduction and strict labels

From the portable archive root:

~~~text
python scripts/item306_j2_normalized_m_bridge_certificate.py \
  --output results/item306_j2_normalized_m_bridge_certificate.json
python scripts/item306_j2_normalized_m_bridge_certificate.py \
  --output results/item306_j2_normalized_m_bridge_certificate_replay.json
~~~

The checker uses only the Python standard library.  Canonical and replay
JSON are byte-identical with SHA-256

~~~text
cd48ec7f4cec273c72371d554c9a4ec55ed3cacde0108f4dc92975ba93dbbc55
~~~

### PROVED

* All eight cleared Hermite reductions, including missing shifts 2 and 3
  in both companions and both conjugate charts.
* The meromorphic-beta exact-term lemma and the determinant normalization
  quotient (2.1).
* All three independent skew-tensor cancellations and all nine restored
  plus/minus tensor coordinates (5.1)--(5.2).
* Recurrence membership (5.3) and the all-$n$ normalized-$M$ bridge
  on both ordinary rays.

### EXACT FINITE ONLY

* No finite prefix is used to promote a recurrence or identity.
* The six exact rows in Section 6 are logically necessary initial values,
  not evidence for the recurrence.  Older extra rows remain implementation
  replays only.

### OPEN

* An algebraic or recurrence realization of the independent $L$ minor.
* All-prime nonvanishing or weighted density for the full ordinary-$j=2$
  collision determinant.
* Any positive capacity booking, Route-1 completion, or conclusion about
  $e+\pi$.
