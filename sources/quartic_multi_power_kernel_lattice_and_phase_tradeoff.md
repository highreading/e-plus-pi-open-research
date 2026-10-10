> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Adjacent quartic powers: rational kernels, endpoint lattices, and a phase tradeoff

Date: 2026-08-27.

## 1. Scope and outcome

For even $n$, put



$$
Q(x)=1+x^4,\qquad P_n(x)=x^n(1-x)^n,\qquad
 J_{n,k}=\int_0^1\frac{P_n(x)}{Q(x)^k}\,dx.                 \tag{1}
$$



When $k>n/2$, the Hermite reduction has the form



$$
J_{n,k}=R_{n,k}
 +\frac{L_{n,k}}{2\sqrt2}\log(1+\sqrt2)
 +\left(\frac{E_{n,k}}{4\sqrt2}+\frac{b_{n,k}}8\right)\pi, \tag{2}
$$



where all four displayed coordinates are rational. This note studies
integer combinations of $m\geq3$ adjacent powers. Its main conclusions
are as follows.

1. There is a new exact beta-integral formula for the odd coordinate $b$.
   Together with the known formulas for $L$ and $E$, it shows that the
   three-power cross product $C=L\times E$ leaves a genuinely rational
   form $A+B\pi$. Its $B$-coordinate has a phase-independent, fixed
   nonzero sign at $k\asymp n\log n$:

   

$$
C\mathbin\cdot b
     \sim-\frac{16}{\pi^3}A_+|I|^2r^{15}.                  \tag{3}
$$



   The integral value still has an oscillatory leading projection, but
   after division by $B$ it is uniformly at most

   

$$
\exp\{-nr+O(nr^2)\},\qquad r=(4k/n)^{-1/4}.            \tag{4}
$$



   This is a genuine rational approximation to $\pi$, not a
   quadratic-field form.

2. Four powers admit an exact phase-removing kernel. In the leading saddle
   model its polynomial is proportional to

   

$$
(g_+-t)(t-g_i)(t-\overline {g_i}).                     \tag{5}
$$



   Its combined integral has a phase-free, fixed sign. The same
   polynomial, however, annihilates the leading quadrature saddle which
   supplies the rational $\pi$-coordinate. Thus four powers remove the
   real phase only by also removing the leading $B$-term. The exact
   residual $B$-term is governed by the next saddle coefficient or the
   exponentially smaller real saddle; it is not lower-bounded here.

3. The exact integer kernel lattice can be described without a coarse
   Siegel lemma. If $A$ is the two-row integer matrix obtained from $L,E$,
   then

   

$$
\det\ker_{\mathbb Z}A
     =\frac{\sqrt{\det(AA^T)}}{\delta_2(A)},                 \tag{6}
$$



   where $\delta_2(A)$ is the gcd of its $2\times2$ minors. More
   importantly, if $M=(L,E,R,b/8)^T$ is the fully cleared four-row matrix,
   the lattice of rational endpoint pairs produced from the $L,E$-kernel
   has exact index

   

$$
[\mathbb Z^2:\Gamma]=\frac{\delta_4(M)}{\delta_2(A)}.   \tag{7}
$$



   For $m\geq5$, the full coordinate kernel has rank at least $m-4$.
   Thus growing $m$ automatically introduces exact zero relations. A
   shortest vector in the $L,E$-kernel can therefore be a zero form; its
   small height says nothing by itself about a useful nonzero $A+B\pi$.

4. Ordinary finite differences can reduce the leading dyadic-cleared
   exponent from $\log 8$ to $\log 7$, but no further in the
   proportional-order regime. A larger exact cancellation would require
   primitive endpoint content. A bounded exact scan finds that the main
   dyadic rational-endpoint denominator persists through differences, but
   the observed valuation has not been proved for all parameters.

Consequently growing adjacent-power windows are not proved to improve the
factorial-matching or Roth threshold. Nor is there a rigorous endpoint
denominator no-go: the needed lower bound on the determinant divisors in
(7), or equivalently an upper bound on primitive content, remains absent.
Nothing here classifies $e+\pi$.

## 2. All four beta coordinates

Write, for $j\geq0$,



$$
\begin{aligned}
 I_j&=I_{n,k+j}
 =\int_0^\infty\frac{[y(1+iy)]^n}{(1+y^4)^{k+j}}\,dy,\\
 A_{+,j}&=\int_0^\infty
 \frac{y^n(1+y)^n}{(1+y^4)^{k+j}}\,dy,\\
 A_{-,j}&=\int_0^\infty
 \frac{y^n(1-y)^n}{(1+y^4)^{k+j}}\,dy .                    \tag{8}
 \end{aligned}
$$



Since $n$ is even, $A_{-,j}>0$. Reflection for the gamma function and the
beta integral, followed by the quartic residue filter, give the known
identities



$$
\boxed{
 L_j=(-1)^{n/2}\frac{2\sqrt2}{\pi}\Re I_j,\qquad
 E_j=\frac{\sqrt2}{\pi}(A_{+,j}+A_{-,j}).}                  \tag{9}
$$



There is an equally simple identity for $b_j$.

**Proposition 2.1.** If $n$ is even and $k>(2n+1)/4$, then



$$
\boxed{
 b_j=-\frac1\pi\left\{A_{+,j}-A_{-,j}
       +2(-1)^{n/2}\Im I_j\right\}.}                        \tag{10}
$$



Consequently



$$
\boxed{
 b_j+\frac{E_j}{\sqrt2}
 =\frac2\pi\left\{A_{-,j}-(-1)^{n/2}\Im I_j\right\}.}       \tag{11}
$$



To prove (10), recall that the $b$-coordinate selects the monomials
$m=n+q\equiv1\pmod4$. For such $m$,



$$
\sin\frac{\pi(3-m)}4=(-1)^{(m-1)/4}.
$$



The sign in the Hermite residue sum cancels this sine, while $q$ is odd.
It follows that



$$
b_j=-\frac4\pi\int_0^\infty
 \frac{y^nS_n(y)}{(1+y^4)^{k+j}}\,dy,                       \tag{12}
$$



where



$$
S_n(y)=\sum_{n+q\equiv1\ (4)}\binom nq y^q.
$$



The exact roots-of-unity filter is



$$
4S_n(y)=(1+y)^n-(1-y)^n
 +2\Re\left(i^{\,n-1}(1+iy)^n\right).                      \tag{13}
$$



For even $n$,



$$
\Re(i^{\,n-1}I_j)=(-1)^{n/2}\Im I_j,
$$



and (10)--(11) follow. No asymptotic argument or choice of a complex
integration contour enters this proof.

## 3. Three powers give a rational $A+B\pi$

Suppress $n,k$ in the notation and put



$$
C=(L_1E_2-L_2E_1,\ L_2E_0-L_0E_2,\ L_0E_1-L_1E_0).       \tag{14}
$$



Then, exactly,



$$
C\mathbin\cdot L=C\mathbin\cdot E=0,                      \tag{15}
$$



and therefore



$$
\boxed{C\mathbin\cdot J=C\mathbin\cdot R
       +\frac{C\mathbin\cdot b}{8}\pi.}                    \tag{16}
$$



All quantities in (16), apart from $\pi$, are rational.

### 3.1 The leading degree-two polynomial

Put



$$
r=(4k/n)^{-1/4}.
$$



The fixed-amplitude saddle expansions, uniformly for fixed $j$, have the
form



$$
\begin{aligned}
 I_j&=I_0\{g_i^j+O(n^{-1})\},\\
 A_{+,j}&=A_{+,0}\{g_+^j+O(n^{-1})\},\\
 J_{n,k+j}&=J_{n,k}\{g_-^j+O(n^{-1})\},                    \tag{17}
 \end{aligned}
$$



where



$$
\begin{aligned}
 g_i&=1-r^4-ir^5-\frac34r^6+\frac{7i}{32}r^7+O(r^8),\\
 g_+&=1-r^4-r^5+\frac34r^6-\frac7{32}r^7+O(r^8),\\
 g_-&=1-r^4+r^5+\frac34r^6+\frac7{32}r^7+O(r^8).           \tag{18}
 \end{aligned}
$$



Also



$$
\frac{A_{-,0}}{|I_0|}=\exp\{-nr+O(nr^2)\},                \tag{19}
$$



and in a fixed critical window
$A_{-,0}=J_{n,k}(1+e^{-\Omega(k)})$. The latter identity follows because
the two integrands agree on $[0,1]$, while the $y>1$ tail is exponentially
smaller.

Let $Z=I_0$, $g=g_i$, $p=g_+$, and let



$$
P_C(t)=C_0+C_1t+C_2t^2.                                   \tag{20}
$$



In the leading geometric model, (15) becomes



$$
P_C(p)=0,\qquad \Re\{ZP_C(g)\}=0.                          \tag{21}
$$



Thus one root is $p$, while the second is phase-dependent. When the
denominator below is nonzero, it is



$$
\tau=\frac{\Re\{Z(g-p)g\}}{\Re\{Z(g-p)\}},\qquad
 P_C(t)\asymp(t-p)(t-\tau).                                \tag{22}
$$



The limiting case in which the denominator vanishes is obtained by
homogeneous continuity and corresponds to a root at infinity. Formula
(22) makes clear why the value at the real saddle can still change sign.

### 3.2 The $b$-determinant has fixed sign

For real $p$, complex $g=x+iy$, and complex $Z$, direct expansion gives



$$
\det\begin{pmatrix}
 \Re Z&\Re Zg&\Re Zg^2\\
 1&p&p^2\\
 \Im Z&\Im Zg&\Im Zg^2
 \end{pmatrix}
 =(-\Im g)|Z|^2|p-g|^2.                                    \tag{23}
$$



Because $C\cdot E=0$, equation (11) may be used in place of $b$. The
constants in (9) and (11), including the parity signs, then yield



$$
\boxed{
 C\mathbin\cdot b
 =-\frac8{\pi^3}A_{+,0}|I_0|^2
 \left\{(-\Im g_i)|g_+-g_i|^2
       +O(n^{-1}+e^{-nr+O(nr^2)})\right\}.}                 \tag{24}
$$



Now



$$
(-\Im g_i)|g_+-g_i|^2=2r^{15}(1+O(r)),                    \tag{25}
$$



so, whenever $nr^{15}\to\infty$,



$$
\boxed{C\mathbin\cdot b
 \sim-\frac{16}{\pi^3}A_{+,0}|I_0|^2r^{15}<0.}             \tag{26}
$$



This includes every fixed window
$c_1n\log n\leq k\leq c_2n\log n$. The conclusion is independent of the
phase of $I_0$. It is therefore an all-large-parameter nonvanishing
theorem, not an inference from the finite scan.

### 3.3 The value retains the real phase

A second elementary determinant identity is



$$
\det\begin{pmatrix}
 \Re Z&\Re Zg&\Re Zg^2\\
 1&p&p^2\\
 1&m&m^2
 \end{pmatrix}
 =\Re\{Z(p-g)(m-g)(m-p)\}.                                 \tag{27}
$$



Taking $m=g_-$, equations (9) and (17) give



$$
\boxed{
 C\mathbin\cdot J
 =\frac{4(-1)^{n/2}}{\pi^2}A_{+,0}J_{n,k}
 \left[
 \Re\{I_0(g_+-g_i)(g_--g_i)(g_--g_+)\}
 +O(|I_0|/n)
 \right].}                                                 \tag{28}
$$



The product of differences is



$$
(g_+-g_i)(g_--g_i)(g_--g_+)=-4r^{15}(1+O(r)).             \tag{29}
$$



Thus the leading value contains $\Re I_0$ and can approach a phase zero.
Nevertheless (24) gives a uniform nonzero denominator, and hence



$$
\boxed{
 \left|\pi+\frac{8C\cdot R}{C\cdot b}\right|
 =\frac{8|C\cdot J|}{|C\cdot b|}
 \leq C_0\frac{J_{n,k}}{|I_0|}
 =\exp\{-nr+O(nr^2)\}.}                                    \tag{30}
$$



Here $C_0$ is uniform in a fixed critical window. Scaling $C$ to its
primitive integer representative does not change (30). At
$k\sim cn\log n$, the exponent in (30) is



$$
-\frac{n}{(4c\log n)^{1/4}}(1+o(1)).                       \tag{31}
$$



This analytic approximation is real but subfactorial. Whether its fully
reduced rational height is only subfactorial, or instead has the expected
$\exp(\Theta(k))$ endpoint size, is an arithmetic content question.

## 4. Four powers: phase removal also removes the leading $b$-term

For $L_0,L_1,L_2,L_3$, define



$$
\begin{aligned}
 q_0&=L_1L_3-L_2^2,\\
 q_1&=L_1L_2-L_0L_3,\\
 q_2&=L_0L_2-L_1^2,\\
 Q_L(t)&=q_0+q_1t+q_2t^2.                                  \tag{32}
 \end{aligned}
$$



The two Hankel identities



$$
\sum_{j=0}^2q_jL_j=\sum_{j=0}^2q_jL_{j+1}=0               \tag{33}
$$



are exact. Put



$$
e_0=\sum_{j=0}^2q_jE_j,\qquad
 e_1=\sum_{j=0}^2q_jE_{j+1},                               \tag{34}
$$



and let $c_0,c_1,c_2,c_3$ be the coefficients of



$$
W(t)=e_1Q_L(t)-e_0tQ_L(t).                                \tag{35}
$$



Explicitly,



$$
c=(e_1q_0,\ e_1q_1-e_0q_0,\ e_1q_2-e_0q_1,\ -e_0q_2).    \tag{36}
$$



Equations (33)--(35) prove the exact cancellations



$$
c\mathbin\cdot L=c\mathbin\cdot E=0.                      \tag{37}
$$



In the geometric model,



$$
q_2=-\frac8{\pi^2}|I_0|^2(\Im g_i)^2,\qquad
 Q_L(t)=q_2(t-g_i)(t-\overline {g_i}),                      \tag{38}
$$



and



$$
e_0=\frac{\sqrt2}{\pi}A_{+,0}q_2|g_+-g_i|^2,\qquad
 e_1=g_+e_0.                                                \tag{39}
$$



Consequently



$$
W(t)=e_0(g_+-t)q_2(t-g_i)(t-\overline {g_i}).              \tag{40}
$$



At the real integral saddle this gives



$$
\begin{aligned}
 c\mathbin\cdot J
 &\sim \frac{\sqrt2}{\pi}A_{+,0}J_{n,k}q_2^2
 |g_+-g_i|^2(g_+-g_-)|g_--g_i|^2\\
 &\sim-\frac{512\sqrt2}{\pi^5}
 A_{+,0}J_{n,k}|I_0|^4r^{45}<0.                            \tag{41}
 \end{aligned}
$$



Here is an explicit error justification. After factoring
$|I_0|$ from each $L$ row, $A_{+,0}$ from the $E$ row, and $J_{n,k}$ from
the value row, every one of the finitely many normalized moments in
(32)--(36) differs from its geometric value by $O(n^{-1})$; the
$A_-$ contribution to the normalized $E$ row is
$e^{-2nr+O(nr^2)}$. The expression $c\cdot J$ is a fixed polynomial of
degree four in the $L$ entries, degree one in the $E$ entries, and degree
one in the value entries. All its first derivatives are uniformly bounded
on the normalized moment box. The mean-value theorem therefore gives the
absolute expansion



$$
c\mathbin\cdot J
 =-\frac{512\sqrt2}{\pi^5}A_{+,0}J_{n,k}|I_0|^4
 \left\{r^{45}+O(r^{46}+n^{-1}+e^{-2nr+O(nr^2)})\right\}.   \tag{41a}
$$



Thus the sufficient condition $nr^{45}\to\infty$ makes every displayed
moment perturbation $o(r^{45})$. It holds at $k\asymp n\log n$, since
$nr^{45}=n/(4k/n)^{45/4}\asymp n/(\log n)^{45/4}\to\infty$.
No oscillatory phase occurs in (41).

But (40) also says



$$
W(g_i)=W(\overline {g_i})=W(g_+)=0.                        \tag{42}
$$



By (11), these are exactly the leading $E$- and quadrature-$b$ saddles.
Hence the leading term of $c\cdot b$ is zero. The exact residual comes
from the $O(n^{-1})$ saddle corrections and from $A_-$. The bounded
certificate finds no exact zero of $c\cdot b$, but it supplies no
all-parameter lower bound. Thus the four-power construction exchanges the
phase problem for a primitive $b$-content problem; it does not solve it.

## 5. Exact integer kernel and endpoint-image lattices

Choose one common rational denominator which makes all relevant coordinate
columns integral. For the $L,E$ rows write



$$
A=\begin{pmatrix}
 \lambda_0&\cdots&\lambda_{m-1}\\
 \epsilon_0&\cdots&\epsilon_{m-1}
 \end{pmatrix}\in M_{2,m}(\mathbb Z),                       \tag{43}
$$



and suppose it has rank two. Let $\delta_j(N)$ denote the gcd of all
$j\times j$ minors of an integer matrix $N$.

### 5.1 Covolume and successive minima

The saturated kernel



$$
\mathcal K_{LE}=\ker_{\mathbb Z}A                           \tag{44}
$$



has rank $d=m-2$ and exact Euclidean covolume



$$
\boxed{
 \det\mathcal K_{LE}
 =\frac{\sqrt{\det(AA^T)}}{\delta_2(A)}.}                   \tag{45}
$$



One proof is to take the exterior product of the two row vectors. Its
Euclidean norm is $\sqrt{\det(AA^T)}$; division by the gcd of its Pluecker
coordinates gives the primitive normal two-vector, whose norm is the
covolume of the saturated orthogonal kernel.

For $m=3$, this specializes to an exact primitive-height formula:



$$
c_{\rm prim}
 =\frac{1}{\delta_2(A)}
 (\lambda_1\epsilon_2-\lambda_2\epsilon_1,\
  \lambda_2\epsilon_0-\lambda_0\epsilon_2,\
  \lambda_0\epsilon_1-\lambda_1\epsilon_0),                \tag{46}
$$



and



$$
\|c_{\rm prim}\|_2
 =\frac{\sqrt{\det(AA^T)}}{\delta_2(A)}.                    \tag{47}
$$



Thus no estimate which omits the minor gcd can determine the primitive
height of the three-power form.

Let $v_d$ be the volume of the $d$-dimensional Euclidean unit ball and
assume all entries of $A$ have absolute value at most $H$. Minkowski's
first theorem gives a nonzero $c\in\mathcal K_{LE}$ with



$$
\boxed{
 \|c\|_\infty\leq
 2\left(\frac{\sqrt{\det(AA^T)}}{v_d\delta_2(A)}\right)^{1/d}
 \leq2\left(\frac{mH^2}{v_d}\right)^{1/d}.}                 \tag{48}
$$



If $\mu_1,\ldots,\mu_d$ are the Euclidean successive minima, Minkowski's
second theorem gives



$$
\frac{2^d}{d!}\det\mathcal K_{LE}
 \leq v_d\prod_{j=1}^d\mu_j
 \leq2^d\det\mathcal K_{LE}.                                \tag{49}
$$



For cancellation of only the single log row $\lambda$, the corresponding
exact formulas are



$$
\det\ker_{\mathbb Z}\lambda
 =\frac{\|\lambda\|_2}{\delta_1(\lambda)},\qquad
 \|c\|_\infty\leq
 2\left(\frac{\sqrt mH}{v_{m-1}\delta_1(\lambda)}
 \right)^{1/(m-1)}.                                        \tag{50}
$$



The exponents $2/(m-2)$ and $1/(m-1)$ show the formal benefit of a
growing window. They are upper bounds only; covolume gives no lower bound
for the first minimum, and it does not ensure that the short vector gives
a nonzero period.

### 5.2 The endpoint quotient is the relevant lattice

Using the same common coordinate units, write the fully cleared matrix as



$$
M=\begin{pmatrix}A\\ B\end{pmatrix}\in M_{4,m}(\mathbb Z),
 \qquad
 B=\begin{pmatrix}\rho_0&\cdots&\rho_{m-1}\\
                   \beta_0&\cdots&\beta_{m-1}
   \end{pmatrix},                                          \tag{51}
$$



where the last two rows represent $R$ and $b/8$. Suppose $M$ has rank
four. Define



$$
\Gamma=B(\mathcal K_{LE})\subset\mathbb Z^2.               \tag{52}
$$



Then $\Gamma$ has full rank two and



$$
\boxed{[\mathbb Z^2:\Gamma]
 =\frac{\delta_4(M)}{\delta_2(A)}.}                         \tag{53}
$$



Here is a short proof. Projection onto the first two coordinates gives the
exact sequence of finite abelian groups



$$
0\longrightarrow\mathbb Z^2/\Gamma
 \longrightarrow\mathbb Z^4/M\mathbb Z^m
 \longrightarrow\mathbb Z^2/A\mathbb Z^m
 \longrightarrow0.                                         \tag{54}
$$



The orders of the last two groups are respectively $\delta_4(M)$ and
$\delta_2(A)$, proving (53).

The full coordinate kernel has rank



$$
\operatorname {rank}\ker_{\mathbb Z}M=m-4.                \tag{55}
$$



Thus every full-rank window with $m\geq5$ contains exact zero
combinations of the $J_{n,k+j}$. On any five selected columns which have
rank four, the alternating vector of $4\times4$ minors is one explicit
nonzero relation; if their rank is lower, a relation comes from smaller
nonzero minors. If the cleared entries are bounded by $H$, the displayed
maximal-minor coefficients are at most $16H^4$ by Hadamard. The
four-row analogue of (45) can give potentially much shorter zero relations
when $m$ grows.

This distinction is essential. The shortest vectors in
$\mathcal K_{LE}$ can lie in $\ker M$ and produce exactly zero. Useful
nonzero rational forms are controlled by the two-dimensional quotient



$$
\mathcal K_{LE}/\ker M\simeq\Gamma,                         \tag{56}
$$



not by the first minimum of $\mathcal K_{LE}$. Formula (53), plus a height
bound for lifting a short vector of $\Gamma$, is the exact arithmetic
problem. Neither is supplied by a generic Siegel lemma.

For the one-log kernel, the analogous endpoint image is
three-dimensional and, when all four rows have full rank, has index



$$
\frac{\delta_4(M)}{\delta_1(\lambda)}                       \tag{57}
$$



in the three selected endpoint-coordinate units.

## 6. Sizes at the critical scale

Let



$$
d_k=3(k-1)-s_2(k-1),\qquad D_k=2^{d_k}.                    \tag{58}
$$



The exact monomial denominator theorem makes $D_k$ a common denominator
of $L_k,E_k$. The odd coordinate $b_k$ has the smaller common denominator



$$
D_k^{(b)}=2^{\,2(k-1)-s_2(k-1)}.                           \tag{59}
$$



For a fixed number of adjacent powers, saddle asymptotics give



$$
\begin{aligned}
 \log A_{+,0}
 &=-\frac n4\log(4k/n)-\frac n4+nr+O(nr^2+\log n),\\
 \log |I_0|
 &=-\frac n4\log(4k/n)-\frac n4+O(nr^2+\log n),\\
 \log J_{n,k}
 &=-\frac n4\log(4k/n)-\frac n4-nr+O(nr^2+\log n).          \tag{60}
 \end{aligned}
$$



For fixed $m$, use the terminal clearing $D_{k+m-1}$. The largest integer
in the resulting $L,E$ matrix has



$$
\log H=3k\log2-\frac n4\log(4k/n)-\frac n4+nr
 +O(nr^2+\log n+\log k).                                    \tag{61}
$$



At $k\asymp n\log n$, this is $(3\log2+o(1))k$. The generic
bounds (48) and (50) consequently give only



$$
\log\|c\|_\infty
 \leq\frac{(6\log2+o(1))k}{m-2}+O(\log m)                   \tag{62}
$$



for the rational $L,E$-kernel, and half that leading numerator for the
one-row kernel. These bounds improve as $m$ grows, but (55)--(56) show why
the improvement can consist entirely of short zero identities.

For an arbitrary sign-changing coefficient vector,



$$
\left|\sum_{j=0}^{m-1}c_jJ_{n,k+j}\right|
 \leq m\|c\|_\infty J_{n,k}.                                \tag{63}
$$



This is the only unconditional all-vector estimate. There is no positive
lower bound, because the polynomial multiplier can change sign and because
exact zero relations occur once $m\geq5$. Multiplication by the published
uniform rational-endpoint clearing denominator contributes $\exp(O(k))$,
which dominates the raw $J$-decay in (60). Since that denominator is an
upper clearing bound rather than a lower primitive-height bound, this
observation is not a no-go theorem.

## 7. Finite differences and the optimal $8$-to-$7$ gain

The most elementary growing-window vector is the $s$-th finite difference:



$$
\begin{aligned}
 K_{s,k}
 &=\sum_{j=0}^s(-1)^j\binom sjJ_{n,k+j}\\
 &=\int_0^1\frac{x^{n+4s}(1-x)^n}{(1+x^4)^{k+s}}\,dx>0.     \tag{64}
 \end{aligned}
$$



Let $s=uk$, where $0<u\leq1$, and let $n=o(k)$. On the $k$-scale the
maximizer has $x^4=u$ for $u<1$ and approaches the endpoint for $u=1$.
Elementary Laplace bounds give



$$
\log K_{s,k}=-kh(u)+o(k),\qquad
 h(u)=(1+u)\log(1+u)-u\log u.                              \tag{65}
$$



The terminal quartic-coordinate denominator has



$$
\log D_{k+s}=3(1+u)k\log2+o(k).                            \tag{66}
$$



Hence the naively cleared value satisfies



$$
\log(D_{k+s}K_{s,k})
 =k\{3(1+u)\log2-h(u)\}+o(k).                              \tag{67}
$$



The function in braces is strictly convex. Since



$$
h'(u)=\log\frac{1+u}{u},
$$



its minimum occurs at $u=1/7$, and the minimum is exactly



$$
\boxed{3(1+1/7)\log2-h(1/7)=\log7.}                        \tag{68}
$$



Thus proportional-order finite differences can improve the raw
dyadic-cleared scale from $8^k$ to $7^k$, but cannot make it decay. Extra
rational-endpoint clearing only increases this pre-primitive scale. This
is not yet a primitive no-go, because a common coordinate content may
remove part or all of the factor in (67).

There is a useful exact finite diagnostic. For every tested



$$
n\in\{4,8,12,16,20,24\},\quad
 k\in\{n+3,n+7,n+11,2n+5\},\quad 0\leq s\leq12,             \tag{69}
$$



put $\ell=k+s$. In lowest terms, all 936 tested coordinates satisfy



$$
\begin{aligned}
 v_2(\operatorname {den}L(K_{s,k}))
 &=v_2(\operatorname {den}E(K_{s,k}))=d_\ell-n/4,\\
 v_2(\operatorname {den}R(K_{s,k}))&=d_\ell-n/4+1.          \tag{70}
 \end{aligned}
$$



The absence of an $s$-dependent gain in (70) supports the endpoint barrier
suggested by (67). Equation (70) is, however, a bounded scan and is
explicitly not used as an all-parameter theorem. Its odd endpoint
denominators and the final gcd after imposing $L,E$ also remain to be
controlled.

## 8. A degree-five saddle relation

All leading saddles above come from one algebraic equation. For the
complexified phase of $P_n(x)/Q(x)^k$, stationarity is



$$
n(1-2x)(1+x^4)-4kx^4(1-x)=0.                              \tag{71}
$$



Put $t=(1+x^4)^{-1}$. Solving the linear equation (71) for $x$ and then
using $x^4=(1-t)/t$ gives



$$
\boxed{
 F_{n,k}(t)=
 t[4k(1-t)-n]^4
 -(1-t)[4k(1-t)-2n]^4=0.}                                  \tag{72}
$$



The relevant substitutions are $x=x_-$, $x=-y_+$, and $x=-iy_i$. Thus



$$
F_{n,k}(g_-)=F_{n,k}(g_+)=F_{n,k}(g_i)
 =F_{n,k}(\overline {g_i})=0.                               \tag{73}
$$



The polynomial has degree five and integer coefficients of height
$O((n+k)^4)$. Therefore trying to annihilate the real saddle exactly by
its generic rational minimal polynomial is not selective: the same
low-degree relation also annihilates the positive and complex leading
saddles. Applying $F_{n,k}$ to the adjacent-power moments is not an exact
recurrence—the saddle approximation has lower-order terms—but it
suppresses all leading period coordinates together. This is the
saddle-level version of the four-power tradeoff in Section 4.

## 9. What is proved and what remains open

The exact results are (10)--(16), the three-power fixed-sign theorem
(24)--(26), the normalized approximation (30), the four-power algebra
(32)--(42), the lattice formulas (45), (53), and the finite-difference
optimization (68). The finite scans establish only the stated bounded
facts.

Three unresolved arithmetic quantities prevent a conclusion about
factorial matching or a Roth argument:

1. the minor gcd $\delta_2(A)$, which determines the primitive
   three-power coefficient height;
2. the quotient determinant $\delta_4(M)/\delta_2(A)$, which determines
   the endpoint-pair lattice once $m\geq4$; and
3. the height of a lift from a short nonzero endpoint pair in $\Gamma$
   back to a coefficient vector, modulo the large exact-zero kernel.

The bounded primitive scan at $k=\operatorname {round}(n\log n)$ finds
that the three-power coefficient vector has between 22 and 143 bits for
$8\leq n\leq40$, while its primitive rational endpoint pair has between
44 and 508 bits. These data are consistent with endpoint height
$\exp(\Theta(k))$, in which case (30) has only a vanishing Roth exponent.
They are not a proof of that height law.

## 10. Reproducible certificate

Run

    python -m py_compile scripts/quartic_multi_power_kernel_lattice_certificate.py
    python scripts/quartic_multi_power_kernel_lattice_certificate.py

The script checks the roots-of-unity filter (13), all geometric determinant
identities, the saddle elimination (72), the exact three- and four-power
kernel identities on 392 parameter pairs, the denominator diagnostic
(69)--(70), and the primitive-height data through $n=40$. The JSON warnings
distinguish exact identities from finite diagnostics.
