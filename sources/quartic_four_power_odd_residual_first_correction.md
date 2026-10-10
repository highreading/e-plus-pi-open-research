> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The first surviving odd coordinate in the four-power quartic kernel

Date: 2026-08-27.

## 1. Scope and conclusion

For even $n$, let



$$
J_{n,k}=\int_0^1\frac{x^n(1-x)^n}{(1+x^4)^k}\,dx
 =R_{n,k}
 +\frac{L_{n,k}}{2\sqrt2}\log(1+\sqrt2)
 +\left(\frac{E_{n,k}}{4\sqrt2}+\frac{b_{n,k}}8\right)\pi. \tag{1}
$$



The four-power construction in the companion multi-power note produces
rational coefficients $c_0,\ldots,c_3$ satisfying



$$
c\mathbin\cdot L=c\mathbin\cdot E=0.                       \tag{2}
$$



Its leading polynomial is proportional to



$$
(g_+-t)(t-g_i)(t-\overline {g_i}),
$$



so the leading positive and complex saddle contributions to $c\cdot b$
vanish. This note computes the first term which survives that
cancellation.

Put



$$
r=(4k/n)^{-1/4},\qquad \varepsilon_n=(-1)^{n/2},
$$



and write



$$
I=I_{n,k}=\int_0^\infty
 \frac{[y(1+iy)]^n}{(1+y^4)^k}\,dy,\qquad
 A_+=\int_0^\infty\frac{y^n(1+y)^n}{(1+y^4)^k}\,dy.         \tag{3}
$$



Let $\vartheta=\arg I$. The answer is phase-dependent:



$$
\boxed{
 c\mathbin\cdot b
 =-\frac{4096\varepsilon_n}{\pi^6}
 \frac{A_+|I|^5}{n}r^{43}
 \left\{\sin(\vartheta+\phi(r))+o(1)\right\},\qquad
 \phi(r)=\frac\pi4+2r+O(r^2),}                              \tag{4}
$$



uniformly on every subsequence on which the sine is bounded away from
zero. The first real-saddle correction is smaller there:



$$
\frac2\pi\,c\mathbin\cdot A_-
 \sim-\frac{1024\sqrt2}{\pi^6}
 A_+J_{n,k}|I|^4r^{45}.                                    \tag{5}
$$



Thus the odd coordinate is rigorously nonzero, with the sign prescribed by
(4), on phase-selected subsequences. It is not eventually of one sign.
The phase crosses both signs throughout every fixed critical window.
There is no proof here that $c\cdot b\ne0$ for every sufficiently large
integer power: powers occur within phase distance $O(r^5)$ of the moving
zeros, and exponentially sharper separation would be needed near the
point where (4) and (5) balance.

When the sine is bounded below by a fixed positive constant, the rational
$\pi$-form satisfies



$$
\boxed{
 \left|\pi+\frac{8c\cdot R}{c\cdot b}\right|
 \asymp nr^2\frac{J_{n,k}}{|I|}
 =\exp\{-nr+O(nr^2+\log n)\}.}                             \tag{6}
$$



This has the same subfactorial exponential scale as the three-power form,
with the additional polynomial factor $nr^2$. Primitive coefficient and
endpoint content are audited separately below. No all-parameter primitive
height theorem is obtained, and nothing here classifies $e+\pi$.

## 2. Exact four-power construction and the odd beta identity

For brevity write $L_j=L_{n,k+j}$ and $E_j=E_{n,k+j}$. Define



$$
\begin{aligned}
 q_0&=L_1L_3-L_2^2,\\
 q_1&=L_1L_2-L_0L_3,\\
 q_2&=L_0L_2-L_1^2,                                       \tag{7}\\
 e_0&=\sum_{j=0}^2q_jE_j,\qquad
 e_1=\sum_{j=0}^2q_jE_{j+1},
 \end{aligned}
$$



and



$$
c=(e_1q_0,\ e_1q_1-e_0q_0,\
    e_1q_2-e_0q_1,\ -e_0q_2).                              \tag{8}
$$



The two Hankel identities



$$
\sum_{j=0}^2q_jL_j=\sum_{j=0}^2q_jL_{j+1}=0
$$



prove (2) exactly.

The beta-coordinate identities are



$$
\begin{aligned}
 L_j&=\varepsilon_n\frac{2\sqrt2}{\pi}\Re I_j,\\
 E_j&=\frac{\sqrt2}{\pi}(A_{+,j}+A_{-,j}),\\
 b_j+\frac{E_j}{\sqrt2}
 &=\frac2\pi(A_{-,j}-\varepsilon_n\Im I_j),                 \tag{9}
 \end{aligned}
$$



where



$$
\begin{aligned}
 I_j&=\int_0^\infty
 \frac{[y(1+iy)]^n}{(1+y^4)^{k+j}}\,dy,\\
 A_{\pm,j}&=\int_0^\infty
 \frac{y^n(1\pm y)^n}{(1+y^4)^{k+j}}\,dy.
 \end{aligned}
$$



Since $c\cdot E=0$, (9) gives the exact decomposition



$$
\boxed{
 c\mathbin\cdot b
 =\frac2\pi\left(c\mathbin\cdot A_-
       -\varepsilon_n c\mathbin\cdot\Im I\right).}          \tag{10}
$$



The two terms in (10) will be treated separately.

## 3. The quadratic-in-shift saddle correction

After $y=ru$, the complex integral is



$$
I_j=r^{n+1}\int_0^\infty e^{n\psi_i(u;r)}h(u;r)^j\,du,     \tag{11}
$$



where



$$
\psi_i(u;r)=\log u+\log(1+iru)
 -\frac1{4r^4}\log(1+r^4u^4),\qquad
 h(u;r)=\frac1{1+r^4u^4}.                                  \tag{12}
$$



Let $u_i$ be the contributing critical point, and put



$$
g_i=h(u_i;r),\qquad \ell(u)=\log h(u;r).
$$



The standard one-saddle expansion with the fixed amplitudes $h^j$ gives,
uniformly for $0\leq j\leq3$,



$$
\frac{I_j}{I_0}
 =g_i^j\left[
 1+\frac1n\{a_i j(j-1)+\beta_i j\}+O(n^{-2})
 \right].                                                  \tag{13}
$$



The uniformity here is literal in every fixed critical window. The
relevant critical point stays in a fixed neighborhood of $1$,
$|\psi_i''(u_i)|$ stays bounded away from zero, and all derivatives of
$\psi_i$ and of the finite family $h^j$, $0\leq j\leq3$, needed through
the second correction are uniformly bounded there. The analytic Morse
change of variable therefore has a uniform radius and a uniform Taylor
remainder. On the complementary part of the already-deformed
steepest-descent contour the real part drops by a fixed quadratic amount;
the poles of $h$ have modulus $r^{-1}$ and hence leave every such fixed
neighborhood as $r\to0$. Gaussian integration then makes the remainder
in the normalized ratio (13) $O(n^{-2})$, uniformly in $r$ and in these
four values of $j$.

Only the coefficient of $j(j-1)$ will survive the four-power
determinant. It is



$$
\boxed{
 a_i=-\frac{\ell'(u_i)^2}{2\psi_i''(u_i)}.}                 \tag{14}
$$



For completeness, expand the amplitude-dependent part of the usual
Laplace coefficient. If $a(u)$ is an analytic amplitude, division by the
same expansion with amplitude one leaves



$$
-\frac{a''(u_i)}{2a(u_i)\psi_i''(u_i)}
 +\frac{a'(u_i)\psi_i'''(u_i)}
        {2a(u_i)\psi_i''(u_i)^2}.                           \tag{15}
$$



For $a=h^j$, one has



$$
\frac{a'}a=j\ell',\qquad
 \frac{a''}a=j\ell''+j^2\ell'^2.
$$



The coefficient of $j^2$, equivalently of $j(j-1)$ after the linear term
is regrouped, is exactly (14).

The critical-point and Hessian series are



$$
\begin{aligned}
 u_i&=1+\frac{i}{4}r+\frac9{32}r^2-\frac{i}{4}r^3
      +\frac{247}{2048}r^4+O(r^5),\\
 -\psi_i''(u_i)&=4+ir-\frac14r^2+O(r^3).
 \end{aligned}
$$



Substitution in (14) gives



$$
\boxed{
 a_i=2r^8+\frac{5i}{2}r^9+O(r^{10}).}                       \tag{16}
$$



The positive row has an analogous expansion



$$
\frac{A_{+,j}}{A_{+,0}}
 =g_+^j\left[
 1+\frac1n\{a_+j(j-1)+\beta_+j\}+O(n^{-2})
 \right],                                                   \tag{17}
$$



but the first variation below shows that neither $a_+$ nor $\beta_+$
contributes to the first surviving odd term.

## 4. An exact first-variation identity

The crucial cancellation is algebraic. Let $Z,g$ be complex, let $p$ be
real, and introduce a formal small parameter $\eta$. Put



$$
\begin{aligned}
 z_j&=Zg^j\left[
 1+\eta\{a\,j(j-1)+b\,j\}\right],\\
 u_j&=p^j\left[
 1+\eta\{d\,j(j-1)+f\,j\}\right],\qquad 0\leq j\leq3.       \tag{18}
 \end{aligned}
$$



Construct the vector $c(\Re z,u)$ from the two real rows
$(\Re z_j)$ and $(u_j)$ by (7)--(8). Direct first-order expansion gives



$$
\boxed{
 \begin{aligned}
 c(\Re z,u)\mathbin\cdot\Im z
 &=4\eta(\Im g)^4|Z|^4|p-g|^2\\
 &\quad{}\times
 \Im\{aZg^2(\overline g-p)\}+O(\eta^2).
                                                               \tag{19}
 \end{aligned}}
$$



Every term containing the linear complex correction $b$, or either
positive-row correction $d,f$, cancels identically. There is a conceptual
reason for the first cancellation: $bj$ is the first variation of a
change in the geometric ratio $g$. If the complex sequence remains
geometric, the real recurrence annihilates its imaginary part exactly.
If the complex sequence is geometric, the same annihilation holds for
every positive row, which explains the cancellation of $d,f$. The
remaining factorization in (19) follows by direct product expansion; it is
verified symbolically by the certificate.

For the quartic saddles, put



$$
K_i(r)=a_i g_i^2(\overline {g_i}-g_+)
       =|K_i(r)|e^{i\phi(r)}.                               \tag{20}
$$



The multiplier series give



$$
\begin{aligned}
 g_i&=1-r^4-ir^5-\frac34r^6+O(r^7),\\
 g_+&=1-r^4-r^5+\frac34r^6+O(r^7),
 \end{aligned}
$$



and (16) therefore yields



$$
\boxed{
 K_i(r)=2(1+i)r^{13}
 +\left(-\frac{11}{2}+\frac{5i}{2}\right)r^{14}
 +O(r^{15}).}                                              \tag{21}
$$



Equivalently,



$$
|K_i(r)|=2\sqrt2\,r^{13}(1+O(r)),\qquad
 \phi(r)=\frac\pi4+2r+O(r^2).                              \tag{22}
$$



Also



$$
(\Im g_i)^4|g_+-g_i|^2=2r^{30}(1+O(r)).                   \tag{23}
$$



## 5. The complete first residual

Apply (19) with $\eta=1/n$, $Z=I$, $g=g_i$, and $p=g_+$. The Hermite
scales in (9) are



$$
\alpha=\varepsilon_n\frac{2\sqrt2}{\pi},\qquad
 \beta=\frac{\sqrt2}{\pi}.
$$



The construction (7)--(8) is homogeneous of degree four in the $L$ row
and degree one in the $E$ row. Hence



$$
\begin{aligned}
 c\mathbin\cdot\Im I
 &=\alpha^4\beta A_+
 \frac4n(\Im g_i)^4|I|^4|g_+-g_i|^2\\
 &\quad{}\times
 \Im\{I K_i(r)\}
 +O\left(\frac{A_+|I|^5}{n^2}
 +\frac{A_-|I|^5}{n}\right).                               \tag{24}
\end{aligned}
$$



The second error in (24) is the contamination of the exact $E$ row by
$A_-$. It cannot appear without the nongeometric $O(1/n)$ correction of
the complex row, because (19) vanishes for a geometric complex row and an
arbitrary first variation of the positive row. At the critical scale,



$$
\frac{A_-}{A_+}=\exp\{-2nr+O(nr^2)\}.                     \tag{25}
$$



Combining (10), (22)--(25), and $\alpha^4=64/\pi^4$ gives the complex
part of (4):



$$
\begin{aligned}
 -\frac{2\varepsilon_n}{\pi}
 c\mathbin\cdot\Im I
 &=-\frac{4096\varepsilon_n}{\pi^6}
 \frac{A_+|I|^5}{n}r^{43}\\
 &\quad{}\times
 \left\{\sin(\vartheta+\phi(r))
 +O\left(r+\frac1{nr^{43}}
 +\frac{e^{-2nr+O(nr^2)}}{r^{43}}\right)\right\}.           \tag{26}
\end{aligned}
$$



The $O(n^{-2})$ moment remainder has been displayed relative to the main
scale $r^{43}/n$: this is the origin of the condition



$$
nr^{43}\longrightarrow\infty.                             \tag{27}
$$



The real part of (10) is determined by the phase-free four-power value.
Indeed $A_{-,j}=J_{n,k+j}$ on $[0,1]$, and the $y>1$ tail is
$e^{-\Omega(k)}$ relative to $J_{n,k}$. The companion four-power calculation,
whose normalized moment polynomial has leading order $r^{45}$, gives



$$
c\mathbin\cdot A_-
 =-\frac{512\sqrt2}{\pi^5}
 A_+J_{n,k}|I|^4r^{45}
 \left\{1+O\left(
 r+\frac1{nr^{45}}
 +\frac{e^{-2nr+O(nr^2)}}{r^{45}}
 +\frac{e^{-\Omega(k)}}{r^{45}}
 \right)\right\}.                                        \tag{28}
$$



Thus (5) follows. Relative to the oscillatory main term in (26), its size
on a phase-selected subsequence is



$$
O\left(nr^2\frac{J_{n,k}}{|I|}\right)
 =\exp\{-nr+O(nr^2+\log n)\}.                              \tag{29}
$$



Equations (25), (27)--(29) rigorously show that neither the $A_-$ row
contamination, the direct $A_-$ term, nor the $O(n^{-2})$ moment error can
dominate (26) when the sine is bounded below.

A convenient single sufficient hypothesis is



$$
r\to0,\qquad nr^{45}\to\infty.                            \tag{30}
$$



It implies (27) and holds at $k\asymp n\log n$, because



$$
nr^{45}\asymp\frac{n}{(\log n)^{45/4}}\longrightarrow\infty.
$$



It also implies $nr\to\infty$ and $k=n/(4r^4)\to\infty$.
Consequently both exponential terms in (28), and the exponentially small
row-contamination term in (26), are $o(1)$ after division by their stated
powers of $r$. This makes the dominance assertion independent of any
unstated comparison between an exponential and a shrinking power.

## 6. Uniform phase selection and the nonvanishing statement

Define the corrected phase



$$
\Phi_{n,k}=\arg I_{n,k}+\phi(r).                           \tag{31}
$$



The neighboring complex-moment ratio and (22) give



$$
\Phi_{n,k+1}-\Phi_{n,k}
 =-r^5+O(r^7+n^{-1}+r/k).                                  \tag{32}
$$



In every fixed critical window



$$
c_1n\log n\leq k\leq c_2n\log n,
$$



the phase is therefore eventually strictly decreasing, its mesh is
$r^5(1+o(1))$, and its total variation tends to infinity.

Fix any $\eta>0$. Uniformly over powers satisfying



$$
|\sin\Phi_{n,k}|\geq\eta,                                 \tag{33}
$$



equations (26), (28), and (30) give



$$
\boxed{
 c\mathbin\cdot b
 =-\frac{4096\varepsilon_n}{\pi^6}
 \frac{A_+|I|^5}{n}r^{43}\sin\Phi_{n,k}
 \left[
 1+O_\eta\left(
 r+\frac1{nr^{43}}
 +nr^2\frac{J_{n,k}}{|I|}
 +\frac{e^{-2nr+O(nr^2)}}{r^{43}}
 \right)
 \right].}                                                 \tag{34}
$$



In particular, (34) is eventually nonzero and



$$
\operatorname {sgn}(c\cdot b)
 =-\varepsilon_n\operatorname {sgn}(\sin\Phi_{n,k})         \tag{35}
$$



on this set.

There is an explicit abundance statement. Write $r_k=(4k/n)^{-1/4}$ and
unwrap the argument in (31) along the critical window. Uniformly there,
(32) implies, for all sufficiently large $n$,



$$
\frac12r_k^5\leq
 \Phi_{n,k}-\Phi_{n,k+1}\leq\frac32r_k^5.                 \tag{35a}
$$



Moreover, if $0\leq t\leq16\pi r_k^{-5}$, then
$r_{k+t}/r_k=1+o(1)$ uniformly, because
$r_k^{-5}/k=O((\log n)^{5/4}/(n\log n))=o(1)$. It follows
from (35a) that every block of



$$
M_k=\left\lceil16\pi r_k^{-5}\right\rceil               \tag{35b}
$$



consecutive powers contained in the critical window has total phase
decrease at least $4\pi$, while its largest single phase step is at most
$2r_k^5=o(1)$. Rounding, within this monotone phase mesh, points congruent
to $\pi/2$ and $3\pi/2$ modulo $2\pi$ therefore gives powers of both
signs, and in particular gives a power with



$$
|\sin\Phi_{n,k}|\geq\frac12.                              \tag{36}
$$



Indeed, the rounded sine has absolute value at least
$\cos(2r_k^5)>1/2$ for all sufficiently large $n$. Hence the exact
rational coordinate $c\cdot b$ is rigorously nonzero on abundant
subsequences and takes both signs.

Conversely, throughout every full critical window there are integer powers
with



$$
|\sin\Phi_{n,k}|=O(r^5),                                  \tag{37}
$$



obtained by rounding a continuous phase zero. Thus no uniform lower bound
by a fixed positive multiple of the $r^{43}/n$ envelope is possible.
To decide all-power nonvanishing one would have to separate the integer
phase from the much narrower balance scale



$$
|\sin\Phi_{n,k}|
 \asymp nr^2\frac{J_{n,k}}{|I|}
 =\exp\{-nr+O(nr^2+\log n)\},                              \tag{38}
$$



where (5) can cancel the oscillatory term. The present saddle expansion
does not provide this arithmetic phase separation. Therefore no claim of
eventual nonvanishing for every integer $k$ is made.

## 7. The normalized rational $\pi$-form

The exact cancellations (2) give



$$
\Lambda_{n,k}=c\mathbin\cdot J
 =c\mathbin\cdot R+\frac{c\mathbin\cdot b}{8}\pi.           \tag{39}
$$



The phase-free value is



$$
\Lambda_{n,k}
 =-\frac{512\sqrt2}{\pi^5}
 A_+J_{n,k}|I|^4r^{45}(1+o(1)).                            \tag{40}
$$



Combining (34) and (40), uniformly under (33), gives the signed formula



$$
\boxed{
 \pi+\frac{8c\cdot R}{c\cdot b}
 =\frac{8\Lambda_{n,k}}{c\cdot b}
 \sim
 \frac{\varepsilon_n\sqrt2\,\pi\,nr^2}
      {\sin\Phi_{n,k}}\frac{J_{n,k}}{|I|}.}                 \tag{41}
$$



Since



$$
\frac{J_{n,k}}{|I|}
 =\exp\{-nr+O(nr^2)\},                                    \tag{42}
$$



equation (6) follows. Four powers therefore do not improve the exponential
quality of the three-power rational approximation; they lose the
polynomial factor $nr^2$. Near the exponentially narrow balance region
(38), the normalized form need not be small. If the complex term vanished
while (5) dominated, then (10) and $c\cdot A_-\sim c\cdot J$ would instead
give



$$
\frac{8c\cdot J}{c\cdot b}\sim4\pi.                       \tag{43}
$$



## 8. Primitive coefficients and endpoint content

All asymptotic formulas above are homogeneous in $c$ and therefore survive
scaling to a primitive integer coefficient vector. They do not determine
the scale needed for that primitive representative.

Suppose a common clearing makes the four $L,E$ columns integers of
absolute value at most $H$. Then the explicit construction gives



$$
|q_j|\leq2H^2,\qquad |e_0|,|e_1|\leq6H^3,\qquad
 \max_j|c_j|\leq24H^5.                                    \tag{44}
$$



This is only a raw upper bound. The primitive coefficient vector is
obtained by dividing the four entries by their full gcd. After the rational
endpoint coordinates are cleared, the pair



$$
(A,B)=\left(c\cdot R,\frac{c\cdot b}{8}\right)
$$



must be divided by a second gcd. Neither content is bounded here.
Consequently the analytic estimate (41) does not by itself determine the
height of the reduced rational approximation.

The exact finite diagnostic at
$k=\operatorname {round}(n\log n)$ gives:



$$
\begin{array}{c|ccccc}
n&8&16&24&32&40\\ \hline
\text{primitive coefficient bits}&120&339&571&887&1157\\
\text{primitive endpoint-pair bits}&144&436&764&1161&1528
\end{array}                                                 \tag{45}
$$



The endpoint signs also vary. These data are consistent with height
$\exp(\Theta(k))$, but they are not a proof. Under that unproved height
law, the approximation exponent would satisfy



$$
\frac{-\log|\pi+8c\cdot R/(c\cdot b)|}{\log H_{\rm prim}}
 \asymp\frac{nr}{k}
 =\left(\frac nk\right)^{5/4}\longrightarrow0              \tag{46}
$$



at $k\asymp n\log n$, far below a Roth-strength exponent. Because an upper
clearing denominator is not a lower primitive-height bound, (46) is a
calibration, not an unconditional no-go.

## 9. Finite diagnostics and reproducible certificate

The exact rational scan checks 1,266 pairs with



$$
4\leq n\leq40,\qquad n\ {\rm even},\qquad
 n+1\leq k\leq\min(100,3n+40),
$$



and finds no zero of $c\cdot b$. It also finds an exact sign change near
$k=59$ for $n=20$, and three sign changes near
$k=117,155,184$ for $n=40$ in the sampled critical windows. The
nonvanishing scan is explicitly diagnostic; the sign variation is
consistent with, but not needed to prove, the phase theorem in Section 6.

Run

    python -m py_compile scripts/quartic_four_power_odd_residual_certificate.py
    python scripts/quartic_four_power_odd_residual_certificate.py

The certificate verifies:

1. the exact first-variation factorization (19);
2. the cancellation of the linear complex correction and both positive-row
   corrections;
3. the saddle correction (16), phase factor (21), and positive outer
   factor (23);
4. the bounded exact nonvanishing and sign scans; and
5. the primitive-height table.

The JSON warnings distinguish symbolic identities from bounded
diagnostics. No README or research-log file is modified.
