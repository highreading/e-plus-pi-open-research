> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Robin localizers force a prime-window output denominator

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
u=1+x^2,\qquad {\cal T}P=(1-x)P'-xP.
$$



This note studies the following general attempt to repair the non-Robin
Taylor near-solution.  Let $K\in\mathbb Z[x]$, and divide



$$
{\cal T}K=uG+(\alpha+\beta x),
 \qquad G\in\mathbb Z[x],\quad \alpha,\beta\in\mathbb Z.       \tag{1}
$$



We use the convention $\deg0=-\infty$.

Replace $K$ by $hK$, where



$$
h\in\mathbb Z[x],\qquad h\equiv1\pmod {u^2}.                 \tag{2}
$$



Condition (2) gives



$$
h(\pm i)=1,\qquad h'(\pm i)=0,                              \tag{3}
$$



so multiplication by $h$ preserves both exterior Robin defects of
$K$.  A sparse example considered previously is



$$
h_m=x^{4m}(m+1-mx^4).                                      \tag{4}
$$



The main theorem here applies to every high-order localizer, not just
(4).  Suppose



$$
h(0)=0,\qquad n=\operatorname {ord}_0h,\qquad d=\deg h.
$$



Set



$$
S_h=\frac{{\cal T}(hK)-{\cal T}K}{u}\in\mathbb Z[x],
 \qquad e_h=\deg S_h.                                      \tag{5}
$$



For every odd prime satisfying



$$
p>\frac{e_h+1}{2},\qquad
 p-1>\deg G,\qquad p<n,\qquad p\nmid\alpha,                 \tag{6}
$$



the reduced denominator of $4\int_0^1S_h(x)\,dx$ contains $p$
to exact exponent one.  Consequently



$$
\boxed{
 \prod_{\substack{(e_h+1)/2<p<n\\
                   p-1>\deg G,\ p\nmid\alpha}}p
 \ \bigg|\ 
 \operatorname {den}\!\left(4\int_0^1S_h\right).}           \tag{7}
$$



This is an all-parameter congruence theorem.  It already includes the two
remainder moments, the $G$-channel, and the derivative channel; it is not
a statement inferred from the finite behavior of (4).

If one clears an antiderivative coefficient by coefficient, the resulting
clearing multiplier is a multiple of the reduced denominator in (7).
Thus the same prime product is forced for both reduced-output clearing and
the stronger coefficientwise convention.

For fixed $K,G,\alpha,\beta$, with $\alpha\ne0$, one has the
upper bound $e_h\leq d+O_K(1)$.  Hence, if



$$
n\geq\left(\frac12+\varepsilon\right)d                     \tag{8}
$$



for some fixed $\varepsilon>0$, the prime number theorem gives



$$
\log\operatorname {den}\!\left(4\int_0^1S_h\right)
 \geq\varepsilon d+o(d).                                   \tag{9}
$$



Adding a fixed rational base output or removing primitive output content
costs only its fixed denominator and the target coefficient.  Thus (9)
survives whenever their combined logarithmic size is $o(d)$.

There is also an analytic loss.  If $0\leq h\leq1$ on $[0,1]$, then
$h(1)=1$.  For every fixed nonzero $K$, the first nonzero endpoint jet
of ${\cal T}(hK)$ is independent of $h$.  Shifted Markov inequalities
therefore give only a polynomially small lower bound for its weighted
$L^1$-norm.  Combining that bound with (7) shows that the
denominator-cleared weighted norm diverges exponentially throughout the
high-order regime (8).

The restriction (8) is real.  Congruence and endpoint data alone do not
forbid moment annihilation.  The exact polynomial



$$
\begin{aligned}
 q_*={}&-1+117x-795x^2+1687x^3-1230x^4+222x^6,\\
 h_*={}&1+u^2q_*
\end{aligned}                                               \tag{10}
$$



satisfies



$$
\begin{gathered}
 h_*(0)=0,\qquad h_*(1)=1,\qquad h_*'(1)=0,\\
 \int_0^1u q_*\,dx=\int_0^1xu q_*\,dx=0,                   \tag{11}\\
 h_*(1/2)=-2513/512<0.
\end{gathered}
$$



Thus the two moments can be annihilated exactly if sign control is
discarded.  The theorem leaves open nonlocal families with
$d\geq(2-o(1))n$, sign-changing cancellations, or a new mechanism which
couples the other output channels arithmetically.

This package proves neither irrationality nor transcendence of
$e+\pi$.

## 2. The product identity and the two defect moments

The Stein operator obeys



$$
{\cal T}(hK)=h\,{\cal T}K+(1-x)h'K.                       \tag{12}
$$



Write



$$
h=1+u^2q,\qquad
 r=uq=\frac{h-1}{u}.                                      \tag{13}
$$



Since



$$
h'=u(4xq+uq'),
$$



both $r$ and $h'/u$ are integer polynomials.  Substitution of (1) in
(12) gives the exact quotient



$$
\boxed{
 S_h=(h-1)G+r(\alpha+\beta x)
       +(1-x)\frac{h'}uK.}                                 \tag{14}
$$



The two rational defect moments singled out by the remainder in (1) are



$$
I_0(h)=\int_0^1uq\,dx=\int_0^1r\,dx,
 \qquad
 I_1(h)=\int_0^1xuq\,dx=\int_0^1xr\,dx.                   \tag{15}
$$



They cannot be annihilated by a nontrivial bounded positive localizer.
Indeed, (13) gives



$$
\begin{aligned}
 I_0(h)&=-\frac\pi4+\int_0^1\frac{h(x)}{1+x^2}\,dx,\\
 I_1(h)&=-\frac{\log2}{2}
            +\int_0^1\frac{xh(x)}{1+x^2}\,dx.              \tag{16}
\end{aligned}
$$



If $0\leq h\leq1$ and $h\not\equiv1$, then



$$
-\frac\pi4<I_0(h)<0,\qquad
 -\frac{\log2}{2}<I_1(h)<0.                               \tag{17}
$$



Both moments are rational because $r\in\mathbb Z[x]$.  Since the open
intervals in (17) lie strictly between $-1$ and $0$, neither moment
can be zero or an integer.

More generally, without a sign assumption, (16) gives the exact
denominator tradeoff.  If a positive integer $D$ clears both moments,
then



$$
\boxed{
 D\lVert h\rVert_{L^1[0,1]}
 \geq
 \max\left\{
 \left\lVert\frac{D\pi}{4}\right\rVert_{\mathbb Z},
 2\left\lVert\frac{D\log2}{2}\right\rVert_{\mathbb Z}
 \right\}.}                                                \tag{18}
$$



Here $\lVert y\rVert_{\mathbb Z}$ denotes distance to the nearest
integer.  In particular, $I_0=I_1=0$ forces



$$
\lVert h\rVert_1\geq\log2.           \tag{19}
$$



Equation (18) is an exact reduction, not a uniform lower bound: arbitrary
integer denominators can simultaneously approximate the two displayed
real numbers.  Extra arithmetic information about the denominators
attainable by localizers is essential.  The prime-window theorem supplies
that information in the high-order regime.

## 3. The forced low coefficients

Write



$$
r(x)=\sum_{j=0}^{d-2}r_jx^j.
$$



From $ur=h-1$, coefficient comparison gives



$$
r_j+r_{j-2}=h_j-\delta_{j0},\qquad r_{-1}=r_{-2}=0.       \tag{20}
$$



Since $h_0=\cdots=h_{n-1}=0$, induction in (20) gives



$$
\boxed{
 r_{2k}=(-1)^{k+1},\qquad r_{2k+1}=0
 \quad(2k,2k+1<n).}                                       \tag{21}
$$



This dense alternating prefix is forced by the congruence and the
localization order.  It cannot be changed by any high-degree coefficients
of $h$.

As a first consequence, let



$$
D_0=\operatorname {den}I_0(h),\qquad
 D_1=\operatorname {den}I_1(h).
$$



For every odd prime



$$
\frac d2<p\leq n,                                        \tag{22}
$$



the denominator $D_0$ contains $p$ exactly once, while $I_1(h)$
is $p$-integral.  Indeed, among the denominators
$1,\ldots,d-1$ in



$$
I_0=\sum_{j=0}^{d-2}\frac{r_j}{j+1},
$$



only $j+1=p$ is divisible by $p$, and its numerator is
$r_{p-1}=\pm1$.  In



$$
I_1=\sum_{j=0}^{d-2}\frac{r_j}{j+2},
$$



the only possible $p$-denominator has numerator
$r_{p-2}=0$.  Thus



$$
\boxed{
 \prod_{d/2<p\leq n}p\mid D_0.}                            \tag{23}
$$



This already rules out integral or polynomial-denominator control of the
$\alpha$-moment for every localizer with $n>(1/2+\varepsilon)d$.

## 4. Proof of the full output-denominator theorem

The preceding prime survives every term of (14).  Let $p$ satisfy
(6).  Since $p<n$, the coefficient of degree $p-1$ in the first
term of (14) is



$$
[x^{p-1}](h-1)G=-[x^{p-1}]G=0.                           \tag{24}
$$



The polynomial $h'/u$ has order $n-1$, so the derivative term in
(14) also has zero coefficient in degree $p-1<n-1$.  Finally, (21)
gives



$$
[x^{p-1}]\,r(\alpha+\beta x)
 =\alpha r_{p-1}+\beta r_{p-2}
 =\pm\alpha.                                               \tag{25}
$$



Therefore



$$
[x^{p-1}]S_h=\pm\alpha.            \tag{26}
$$



In the monomial integral



$$
\int_0^1S_h(x)\,dx
 =\sum_{j=0}^{e_h}\frac{[x^j]S_h}{j+1},                   \tag{27}
$$



condition $2p>e_h+1$ says that $p$ occurs in exactly one
denominator, namely $j+1=p$.  Since $p\nmid\alpha$, equations
(26)--(27) prove



$$
v_p\left(\int_0^1S_h\right)=-1.                          \tag{28}
$$



The prime is odd, so multiplication by four does not change (28).
Distinct primes multiply, proving (7).

For a convenient degree bound, if $k=\deg K$ and $g=\deg G$, then



$$
e_h\leq\max\{d+g,\ d-1,\ d+k-2\}=d+O_K(1).               \tag{29}
$$



Let $\vartheta(y)=\sum_{p\leq y}\log p$.  Equations (7), (8), (29),
and $\vartheta(y)=y+o(y)$ give (9).

There are two harmless bookkeeping extensions.

First, repeated integration by parts gives



$$
\int_0^1e^x{\cal T}P(x)\,dx=-P(0).                       \tag{30}
$$



Because $h(0)=0$, the exponential-coordinate change from $K$ to
$hK$ is the integer $K(0)$.  Thus the nonintegral output change is
exactly $4\int S_h$.

Second, suppose the unlocalized common form has rational coordinate
$\rho_0$, of reduced denominator $D_{\rm base}$.  Every prime in
(6) which also avoids $D_{\rm base}$ remains in the denominator of



$$
\rho_0+K(0)+4\int_0^1S_h.               \tag{31}
$$



If the common target is $a$, primitive content removal can cancel at
most a divisor of $a$.  Hence the primitive denominator scale loses at
most the factor



$$
|a\alpha|D_{\rm base}.                   \tag{32}
$$



Here this sentence is used only when $a\alpha\ne0$.  In particular,
(9) is unchanged whenever the logarithm of (32) is $o(d)$.

## 5. The weighted-norm loss

Assume now that



$$
0\leq h\leq1\quad(0\leq x\leq1).  \tag{33}
$$



At $x=1$, (2) gives



$$
h(1)=1+4q(1)\equiv1\pmod4.
$$



The only such integer in $[0,1]$ is one, so



$$
h(1)=1.                      \tag{34}
$$



The shifted Markov inequality



$$
\lVert h'\rVert_\infty\leq2d^2\lVert h\rVert_\infty
$$



and (33)--(34) imply



$$
\int_0^1h(x)\,dx\geq\frac1{8d^2}.
                                                                    \tag{35}
$$



This is already enough to show that a natural $L^1$ multiplier cost,
after clearing the forced denominator in (7), diverges exponentially.
There is a version intrinsic to the correction $K$.

Let



$$
s=\operatorname {ord}_{x=1}K.
$$



Then $K^{(s)}(1)\ne0$.  In the coordinate $t=1-x$, the first term of
$hK$ is unchanged because $h(1)=1$.  Direct substitution in the
Stein operator gives



$$
\boxed{
 \bigl({\cal T}(hK)\bigr)^{(s)}(1)
 =-(s+1)K^{(s)}(1).}                                      \tag{36}
$$



Put $D=d+\deg K+1$.  Iterating the shifted Markov inequality and then
using the elementary $L^1$ spike bound gives, for every polynomial
$P$ of degree at most $D$,



$$
\begin{aligned}
 \lVert P^{(s)}\rVert_\infty
     &\leq2^sD^{2s}\lVert P\rVert_\infty,\\
 \int_0^1|P(x)|\,dx
     &\geq\frac{\lVert P\rVert_\infty}{8D^2}.              \tag{37}
\end{aligned}
$$



Applying (37) to $P={\cal T}(hK)$ and using (36) yields



$$
\boxed{
 \int_0^1|{\cal T}(hK)|\,dx
 \geq
 \frac{(s+1)|K^{(s)}(1)|}
      {2^{s+3}(d+\deg K+1)^{2s+2}}.}                       \tag{38}
$$



Since



$$
e^x+\frac4{1+x^2}\geq3\quad(0\leq x\leq1),
$$



the same weighted norm has three times the lower bound in (38).  For
fixed $K,G,\alpha,\beta$, equations (7)--(9) and (38) prove



$$
\operatorname {den}\!\left(4\int S_h\right)
 \int_0^1|{\cal T}(hK)|
       \left(e^x+\frac4{1+x^2}\right)dx
 \longrightarrow+\infty                                  \tag{39}
$$



along every family satisfying (8), apart from the fixed factors in
(32).  Thus the high-order multiplier cannot simultaneously localize a
fixed correction and keep its denominator-cleared weighted norm small.

Equation (39) is an absolute-norm statement.  It does not rule out a new
signed cancellation between ${\cal T}(hK)$ and another varying
polynomial.  Such a cancellation would have to use structure absent from
the localizer alone.

## 6. The sparse family and the Taylor correction

For (4), put $y=x^4$.  The elementary identity



$$
y^m(m+1-my)-1
 =-(y-1)^2\sum_{j=0}^{m-1}(j+1)y^j                      \tag{40}
$$



and $x^4-1=(x^2-1)u$ prove



$$
h_m-1
 =-u^2(x^2-1)^2\sum_{j=0}^{m-1}(j+1)x^{4j}.               \tag{41}
$$



Thus (2) holds.  Moreover,



$$
\begin{gathered}
 \operatorname {ord}_0h_m=4m,\qquad
 \deg h_m=4m+4,\\
 h_m'=4m(m+1)x^{4m-1}(1-x^4)\geq0,\qquad
 0\leq h_m\leq1,                                         \tag{42}\\
 \int_0^1h_m\,dx
 =\int_0^1(1-x)h_m'\,dx
 =\frac{8m+5}{(4m+1)(4m+5)}.
\end{gathered}
$$



The new theorem therefore gives, for fixed correction data,



$$
\log\operatorname {den}\!\left(4\int S_{h_m}\right)
 \geq2m+o(m),                                             \tag{43}
$$



up to the fixed factors in (32).  This explains the dense harmonic
denominators of (4) without relying on their term-by-term closed form.

For the Taylor near-solution, write



$$
(1-i)^N=R_N+iI_N,\qquad M_N=N!-R_N,
$$



and take the particular nonlocalized defect correction



$$
K_N(x)=I_N-\frac{M_N}{2}(1-x).                            \tag{44}
$$



For $N\geq2$, $M_N/2\in\mathbb Z$, and direct calculation gives



$$
\boxed{
 {\cal T}K_N
 =-\frac{M_N}{2}(1+x^2)+(M_N-I_Nx).}                      \tag{45}
$$



Thus the invariant constant remainder in (1) is



$$
\alpha=M_N>0.                \tag{46}
$$



The unlocalized residual $F_N^*=(1-x)^N+{\cal T}K_N$ is a common form
with target $N!$.  Multiplication by any $h$ satisfying (2) preserves
the exact correction of its two Robin defects.  Equations (7), (31), and
(46) show precisely
what must be paid in the rational output: all primes in the localizer
window survive except those dividing the fixed integer
$M_ND_{\rm base}$.  Since



$$
\log M_N=N\log N+O(N),
$$



and the unlocalized common polynomial has degree at most $N$, the
quotient of its target-zero part by the monic polynomial $1+x^2$ has
degree at most $N-2$.  Its rational coordinate therefore has denominator
dividing
$\operatorname {lcm}(1,\ldots,N-1)$.  Thus
$\log D_{\rm base}=O(N)$, and taking $d\gg N\log N$ leaves an
exponential forced denominator.  This is particularly damaging when
$d$ must be made much larger than the factorial-size coefficients in
(44) in order to localize them.

The result does not exclude a construction whose degree is at least twice
its initial localization order, or a construction in which several
varying channels cancel the prime-window residues.

## 7. Exact scope witness

The polynomial in (10) has



$$
q_*(1)=q_*'(1)=0.
$$



Consequently $h_*(0)=0,h_*(1)=1,h_*'(1)=0$.  Direct integration gives



$$
\begin{aligned}
 \int_0^1(1+x^2)q_*\,dx&=0,\\
 \int_0^1x(1+x^2)q_*\,dx&=0.                              \tag{47}
\end{aligned}
$$



Expanded out,



$$
\begin{aligned}
 h_*={}&222x^{10}-786x^8+1687x^7-3033x^6+3491x^5\\
       &\quad-2821x^4+1921x^3-797x^2+117x,                \tag{48}
\end{aligned}
$$



and substitution of $x=1/2$ gives the negative value in (11).

This example is important for scope.  There is no universal algebraic
incompatibility among (2), both endpoint conditions, and both zero
moments.  What fails is sign-controlled localization.  Likewise, the
prime interval in (7) can disappear once $d$ reaches approximately
$2n$.  The present theorem is therefore a sharp obstruction for a
local, high-order multiplier, not for every conceivable polynomial
multiplier.

## 8. Replay and status

From the research directory run

    python3 scripts/common_kernel_robin_localizer_moment_denominator_certificate.py
    sha256sum -c results/common_kernel_robin_localizer_moment_denominator_hashes.sha256

The deterministic replay checks (12)--(15), the forced coefficient
prefix, the exact prime valuations in both isolated moments and the full
quotient, the sparse identities through $m=100$, the Taylor correction
(45), the endpoint-jet identity, and the signed zero-moment witness.
Finite checks certify normalizations and examples only; the
all-parameter results are the proofs above.

The theorem rules out polynomial-denominator control, and in fact forces
an exponential denominator, for every high-order localizer in (8).  The
nonlocal and cross-channel regimes remain open.  No arithmetic
classification of $e+\pi$ is claimed.
