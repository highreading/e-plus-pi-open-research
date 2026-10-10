> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The positive derivative-kernel family diverges after primitive matching

Date: 2026-08-26

## Result

Put



$$
G(x)=16\arctan(x/5)-4\arctan(x/239),
 \qquad
 G'(x)=\frac{80}{x^2+25}-\frac{956}{x^2+57121}.
 \tag{1}
$$



For every positive even integer $n$, put $m=n/2$ and



$$
W_n(x)=x^{2n}(1-x^2)^n,
 \qquad
 \frac{a_n}{b_n}
 =\left(\frac{239^2\,57122}{25\,26}\right)^m
 \quad ((a_n,b_n)=1).
 \tag{2}
$$



Let



$$
L_n(y)=(a_n-b_n)y+57121a_n-25b_n
 \tag{3}
$$



and let $P_n$ be the primitive part of
$W_n(x)L_n(x^2)^2$.  The two positive integrals



$$
I_{e,n}=\int_0^1P_n(x)e^x\,dx,
 \qquad
 I_{\pi,n}=\int_0^1P_n(x)G'(x)\,dx
 \tag{4}
$$



give respectively a rational integer form in $1,e$ and a rational form
in $1,\pi$.  Reduce each coordinate pair to a primitive integer pair,
match the positive coefficients of $e$ and $\pi$ with the least
positive integer multipliers, and finally divide the resulting pair in
$1,e+\pi$ by its content.

**Theorem.**  The values of these final primitive matched forms tend to
$+\infty$ as $n$ tends to infinity through the positive even integers.
More precisely, for constants $c,C>0$ independent of $n$, their values
are at least



$$
c\exp\left(\frac43n\log n-Cn\right).
 \tag{5}
$$



Thus positivity and exact pole interpolation do remove the logarithms,
but this family cannot produce primitive integer forms in $1,e+\pi$
that tend to zero.  The proof does **not** assume that the separate
exponential-coordinate gcd, the separate $\pi$-coordinate gcd, or the
final content equals one.

## 1. Exact primitive interpolation polynomial

The ratio in (2) reduces before taking its $m$-th power:



$$
\frac{57121\,57122}{25\,26}
 =\frac{125494837}{25},
 \qquad
 125494837=13^3 239^2.
 \tag{6}
$$



Consequently



$$
a_n=125494837^m,
 \qquad
 b_n=25^m=5^n.
 \tag{7}
$$



The content of (3) is



$$
\begin{aligned}
 \delta_n
 &=\gcd(a_n-b_n,57121a_n-25b_n)\\
 &=\gcd(a_n-b_n,57096)\\
 &=
 \begin{cases}
  2196=2^2 3^2 61,&m\text{ odd},\\
  4392=2^3 3^2 61,&m\text{ even}.
 \end{cases}
 \end{aligned}
 \tag{8}
$$



Here $57096=2^3 3^2 13\,61$.  To verify the last line, write
$A=125494837$.  One has



$$
v_2(A-25)=2,
 \quad v_2(A+25)=1,
 \quad v_3(A-25)=3,
 \quad v_{61}(A-25)=1,
 \quad 13\mid A,\quad 13\nmid25.
$$



The odd-prime and 2-adic forms of the lifting-the-exponent lemma, followed
by truncation at the valuations of $57096$, give (8).  The middle equality
in (8) follows by subtracting $25(a_n-b_n)$ and using
$\gcd(a_n,a_n-b_n)=1$.

Define



$$
u_n=\frac{a_n-b_n}{\delta_n},
 \qquad
 v_n=\frac{57121a_n-25b_n}{\delta_n},
 \qquad
 \ell_n(y)=u_ny+v_n.
 \tag{9}
$$



Then $\gcd(u_n,v_n)=1$, and the primitive polynomial is exactly



$$
P_n(x)=x^{2n}(1-x^2)^n\ell_n(x^2)^2.
 \tag{10}
$$



This is primitive by Gauss's lemma.  Since $n$ is even and $u_n,v_n>0$,
it is nonnegative on the whole real axis and is not identically zero.

At the two imaginary poles,



$$
\ell_n(-25)=\frac{57096a_n}{\delta_n},
 \qquad
 \ell_n(-57121)=\frac{57096b_n}{\delta_n}.
 \tag{11}
$$



It follows that



$$
\begin{aligned}
 T_n:=P_n(5i)
 &=650^n\left(\frac{57096a_n}{\delta_n}\right)^2,\\
 P_n(239i)
 &=(57121\,57122)^n
   \left(\frac{57096b_n}{\delta_n}\right)^2
 =T_n.
 \end{aligned}
 \tag{12}
$$



Thus the proposed interpolation identity is exact after primitive
normalization, not merely projective.

## 2. Every coordinate explicitly

Use the convention that $\binom nr=0$ outside $0\leq r\leq n$.  Write



$$
P_n(x)=\sum_{k=n}^{2n+2}c_{n,k}x^{2k}.
 \tag{13}
$$



Then



$$
\begin{aligned}
 c_{n,k}={}&v_n^2(-1)^{k-n}\binom n{k-n}
 +2u_nv_n(-1)^{k-n-1}\binom n{k-n-1}\\
 &+u_n^2(-1)^{k-n-2}\binom n{k-n-2}.
 \end{aligned}
 \tag{14}
$$



Let $!j=j!\sum_{r=0}^j(-1)^r/r!$ be the derangement number.  Termwise
integration gives the exact exponential coordinates



$$
I_{e,n}=q_ne-p_n,
 \qquad
 q_n=\sum_{k=n}^{2n+2}c_{n,k}\,!(2k),
 \qquad
 p_n=\sum_{k=n}^{2n+2}c_{n,k}(2k)!.
 \tag{15}
$$



Both integers are positive.  Indeed,



$$
(2k)!=\int_0^\infty e^{-t}t^{2k}\,dt,
 \qquad
 !(2k)=\int_0^\infty e^{-t}(t-1)^{2k}\,dt,
$$



so that



$$
p_n=\int_0^\infty e^{-t}P_n(t)\,dt>0,
 \qquad
 q_n=\int_0^\infty e^{-t}P_n(t-1)\,dt>0.
 \tag{16}
$$



Put



$$
g_{e,n}=\gcd(p_n,q_n),
 \qquad
 \bar p_n=p_n/g_{e,n},
 \qquad
 \bar q_n=q_n/g_{e,n}.
 \tag{17}
$$



Then $\bar q_ne-\bar p_n=I_{e,n}/g_{e,n}>0$ is the primitive
exponential pair.

For $s\in\{5,239\}$, define the exact integer quotient



$$
H_{s,n}(x)=\frac{P_n(x)-T_n}{x^2+s^2}
 =\sum_{j=0}^{2n+1}h_{s,n,j}x^{2j}\in\mathbb Z[x].
 \tag{18}
$$



If $c_{n,k}$ is extended by zero below $k=n$, its coefficients can be
computed without polynomial division ambiguity from



$$
h_{s,n,2n+1}=c_{n,2n+2},
 \qquad
 h_{s,n,j-1}=c_{n,j}-s^2h_{s,n,j}\quad(1\leq j\leq2n+1),
 \tag{19}
$$



with the constant identity $c_{n,0}-T_n=s^2h_{s,n,0}$.
Equations (1), (12), and (18), together with Machin's identity, give



$$
\begin{aligned}
 I_{\pi,n}
 &=\rho_n+T_n\pi,\\
 \rho_n
 &=\sum_{j=0}^{2n+1}
   \frac{80h_{5,n,j}-956h_{239,n,j}}{2j+1},\\
 16\arctan(1/5)-4\arctan(1/239)&=\pi.
 \end{aligned}
 \tag{20}
$$



This displays explicitly why no logarithm remains: division by each even
quadratic has a constant remainder, and equality of those two constants
turns the two arctangent terms into $T_n\pi$.

For a completely integral normalization, put



$$
\mathcal L_n=\operatorname{lcm}(1,3,5,\ldots,4n+3),
 \tag{21}
$$





$$
A_n^{(0)}=\sum_{j=0}^{2n+1}
 \frac{\mathcal L_n}{2j+1}
 (80h_{5,n,j}-956h_{239,n,j}),
 \qquad
 B_n^{(0)}=\mathcal L_nT_n,
 \tag{22}
$$



and



$$
g_{\pi,n}=\gcd(|A_n^{(0)}|,B_n^{(0)}),
 \qquad
 A_n=A_n^{(0)}/g_{\pi,n},
 \qquad
 B_n=B_n^{(0)}/g_{\pi,n}.
 \tag{23}
$$



Then



$$
L_{\pi,n}=A_n+B_n\pi
 =\frac{\mathcal L_n}{g_{\pi,n}}I_{\pi,n}>0,
 \qquad \gcd(A_n,B_n)=1,\quad B_n>0.
 \tag{24}
$$



For completeness, positivity in (4) is elementary: $P_n\geq0$, and



$$
G'(x)=\frac{4545780-876x^2}
 {(x^2+25)(x^2+57121)}>0
 \qquad(0\leq x\leq1).
 \tag{25}
$$



Equations (14)--(24) are exact formulas for every raw, primitive, and
denominator-cleared coordinate.  No claim that either gcd in (17) or (23)
has a simple exact formula is needed below.

## 3. The primitive exponential coefficient is superexponential

The following standard consequence of Euler's continued fraction is useful.

**Rational-approximation lemma.**  There is an absolute constant
$c_e>0$ such that every reduced $p/q$, $q\geq1$, satisfies



$$
\left|e-\frac pq\right|
 \geq\frac{c_e}{q^2\log(2q)}
 \geq\frac{c_e}{q^3}.
 \tag{26}
$$



One short proof uses



$$
e=[2;1,2,1,1,4,1,1,6,1,\ldots].
$$



If the rational is not covered by Legendre's convergent criterion, its
error is at least $1/(2q^2)$.  If it is a convergent $P_k/Q_k$, the
standard lower bound is



$$
\left|e-\frac{P_k}{Q_k}\right|
 >\frac1{Q_k(Q_{k+1}+Q_k)}
 >\frac1{(a_{k+1}+2)Q_k^2}.
$$



Here $a_{k+1}=O(k)$, while $Q_k\geq F_{k+1}$, so
$k=O(\log(2Q_k))$.  This proves the first inequality in (26); the second
uses $\log(2q)\leq q$.  The same lemma and proof are recorded in
`sources/algebraic_translation_approximation_no_go.md`.

The approximation represented by (15) is extremely accurate even after
unknown gcd cancellation, because



$$
e-\frac{\bar p_n}{\bar q_n}
 =e-\frac{p_n}{q_n}
 =\frac{I_{e,n}}{q_n}.
 \tag{27}
$$



First, on $[0,1]$,



$$
I_{e,n}\leq e(u_n+v_n)^2.
 \tag{28}
$$



Also



$$
\frac{u_n+v_n}{u_n}
 =57122+\frac{57096b_n}{a_n-b_n}<57123,
 \tag{29}
$$



because $a_n/b_n\geq125494837/25>57097$.

For the denominator, substitute $x=t-1$ in (16).  On
$x\geq4n+4$,



$$
P_n(x)
 =x^{2n}(x^2-1)^n(u_nx^2+v_n)^2
 \geq2^{-n}u_n^2x^{4n+4}.
$$



Integrating only over $[4n+4,4n+5]$ gives



$$
q_n\geq
 2^{-n}u_n^2e^{-(4n+6)}(4n+4)^{4n+4}.
 \tag{30}
$$



Therefore



$$
0<\frac{I_{e,n}}{q_n}
 \leq
 \frac{57123^2\,2^n e^{4n+7}}
 {(4n+4)^{4n+4}}.
 \tag{31}
$$



Combining (26), (27), and (31) yields the explicit lower bound



$$
\bar q_n\geq
 c_e^{1/3}
 \frac{(4n+4)^{(4n+4)/3}}
 {57123^{2/3}2^{n/3}e^{(4n+7)/3}},
 \tag{32}
$$



and hence



$$
\log\bar q_n\geq\frac43n\log n-O(n).
 \tag{33}
$$



This is the step that rigorously controls the otherwise unknown gcd
$g_{e,n}$.

## 4. The primitive $\pi$-coefficient is only exponential

Primitive reduction in (23) can only decrease the positive coefficient,
so



$$
B_n\leq\mathcal L_nT_n.
$$



Using the elementary bound
$\operatorname{lcm}(1,2,\ldots,N)\leq16^N$, equations (7), (12), and
(21) give



$$
\begin{aligned}
 B_n
 &\leq16^{4n+3}57096^2(650\cdot125494837)^n\\
 &=C_0C_1^n,
 \end{aligned}
 \tag{34}
$$



where one may take



$$
C_0=16^3 57096^2,
 \qquad
 C_1=16^4\,650\,125494837.
$$



Thus



$$
\log B_n=O(n).
 \tag{35}
$$



No lower bound for $g_{\pi,n}$, and no extrapolation from its finite
values, is being used.

## 5. Minimal matching and its final content

Set



$$
d_n=\gcd(\bar q_n,B_n),
 \qquad
 \bar q_n=d_nq_{0,n},
 \qquad
 B_n=d_nB_{0,n}.
 \tag{36}
$$



The least positive coefficient matching is



$$
\begin{aligned}
 \mathcal W_n
 &=B_{0,n}(\bar q_ne-\bar p_n)
   +q_{0,n}(A_n+B_n\pi)\\
 &=M_n+C_n(e+\pi)>0,
 \end{aligned}
 \tag{37}
$$



where



$$
M_n=-B_{0,n}\bar p_n+q_{0,n}A_n,
 \qquad
 C_n=d_nq_{0,n}B_{0,n}.
 \tag{38}
$$



Let $g_n=\gcd(|M_n|,C_n)$ be the final content.  The two input pairs are
primitive and $\gcd(q_{0,n},B_{0,n})=1$.  Reducing (38) modulo each prime
power dividing $q_{0,n}$, and then each one dividing $B_{0,n}$, shows



$$
\gcd(M_n,q_{0,n}B_{0,n})=1.
$$



Consequently the exact all-degree content bound is



$$
g_n\mid d_n.
 \tag{39}
$$



This is stronger than a square-free assertion and is all that is needed;
the observed finite equality $g_n=1$ is not assumed.

Salikhov's finite irrationality measure for $\pi$ implies that there is
a constant $c_\pi>0$ such that



$$
|A+B\pi|\geq c_\pi B^{-7}
 \qquad(A\in\mathbb Z,\ B\in\mathbb Z_{\geq1}).
 \tag{40}
$$



Both summands in (37) are positive.  Equations (36), (39), and (40) give



$$
\begin{aligned}
 \frac{\mathcal W_n}{g_n}
 &\geq\frac{q_{0,n}L_{\pi,n}}{g_n}
 \geq\frac{\bar q_nL_{\pi,n}}{B_n^2}
 \geq c_\pi\frac{\bar q_n}{B_n^9}.
 \end{aligned}
 \tag{41}
$$



Finally, (33) and (35) turn (41) into (5).  This proves the theorem.

## 6. Exact finite regression probe

The companion script

`scripts/positive_derivative_kernel_probe.py`

reconstructs all coordinates with Python integers and `Fraction`, verifies
both pole evaluations, performs both primitive reductions and minimal
matching, and writes

`results/positive_derivative_kernel_probe.json`.

For the ten even indices $2\leq n\leq20$, the final content is exactly
one.  The coefficient-matching gcd itself is not always one: it is $29$
at $n=8$ and $53$ at $n=18$.  The computed base-10 logarithms of the
positive final values begin



$$
42.8767773204,\quad81.5166772853,\quad122.615264194,
$$



and reach $434.711007102$ at $n=20$.  These finite calculations are
regression evidence only.  The divergence theorem is the all-$n$ argument
in Sections 3--5.

## Reference for the $\pi$ measure

V. Kh. Salikhov, “On the irrationality measure of $\pi$,” *Russian
Mathematical Surveys* **63**:3 (2008), 570--572,
[DOI 10.1070/RM2008v063n03ABEH004543](https://doi.org/10.1070/RM2008v063n03ABEH004543).
Its exponent $7.6063\ldots<8$ gives (40), including all signs and the
finitely many small denominators, after decreasing one fixed positive
constant.

## Scope

The result is a no-go theorem for this particular positive,
derivative-kernel, pole-interpolating family.  It does not rule out other
positive kernels, varying pole sets, sign-changing constructions, or other
ways of coupling approximations to $e$ and $\pi$.  It also does not
prove any unconditional arithmetic statement about $e+\pi$.
