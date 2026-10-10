> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Sharp real-output width of the native sign family

Checked: 2026-08-27 UTC.

## 1. Verdict

Let



$$
(1-i)^N=R_N+iI_N,\qquad
 a=-I_N\geq0,\qquad b=\frac{N!-R_N}{2}>0,\qquad A=a+b,       \tag{1}
$$



where $N\geq2$ and $I_N\leq0$.  Put



$$
w(t)=e^{-t}t^N,\qquad B_N=\int_0^1w(t)\,dt,\qquad
 \mu(t)=t(a+bt)e^{-t}.                                  \tag{2}
$$



For a native real sign profile, write



$$
G=\mu H,\qquad \nu=w+G',\qquad
 v=t^2-2t+2,\qquad q=\frac{H-1}{v^2}.                   \tag{3}
$$



The strict sign and range conditions are



$$
G(0)=G(1)=0,\qquad 0<G<\mu,\qquad \nu>0               \tag{4}
$$



on the open interval.  Define the positive output



$$
{\cal L}_N(G)=\int_0^1R(t)\nu(t)\,dt,
 \qquad
 R(t)=e+\frac{4e^t}{t^2-2t+2}.                         \tag{5}
$$



This note proves three quantitative statements.

First, every native sign output lies in the universal interval



$$
\boxed{
 (e+2)B_N<{\cal L}_N(G)<5eB_N.}                       \tag{6}
$$



Consequently the diameter of *any* native output family is at most



$$
\boxed{(4e-2)B_N,\qquad
 N(4e-2)B_N\longrightarrow4-\frac2e.}                 \tag{7}
$$



In particular, no native family can have output width $w_N$ with
$Nw_N\to\infty$.

Second, the scale in (7) is genuinely attained, even after imposing the
integer endpoint jets required by exact-moment integer approximation.  More
precisely, let ${\cal W}_N$ be the supremum of
$|{\cal L}_N(G_1)-{\cal L}_N(G_0)|$ over pairs satisfying (3)--(4) such
that $q_0,q_1\in C^\infty[0,1]$, their Taylor coefficients through order
three at both endpoints are integers, and the two functions have identical
endpoint germs.  Along the admissible indices $I_N\leq0$,



$$
\boxed{
 \lim_{N\to\infty}N{\cal W}_N=4-\frac2e.}             \tag{8}
$$



The lower bound is constructive.  The entire affine segment between the two
profiles remains strict and has the same endpoint germs, so it sweeps an
open output interval.

Third, one fixed choice gives a completely explicit bound.  For every
admissible $N\geq8$, there are such profiles $G_-,G_+$ with



$$
\boxed{
 {\cal L}_N(G_-)-{\cal L}_N(G_+)\geq\frac{c_*}{N},
 \quad
 c_*=16e^{-4}\left(\frac{e^{3/4}}{17}
                    -\frac{e^{1/4}}{25}\right)
 >0.}                                                   \tag{9}
$$



Numerically, $c_*=0.0214420147290\ldots$, whereas the sharp limiting
constant in (8) is



$$
4-2/e=3.2642411176571\ldots .                         \tag{10}
$$



The arithmetic conclusion is deliberately limited.  An interval of width
$c/N$ guarantees a rational output coordinate with denominator only
$D=O(N)$, not uniformly $o(N)$.  The sufficient exact-moment condition
$Nw_N\to\infty$ is impossible here by (7).  Moreover, even the sharp
native width cannot by itself close the crude rational-case contradiction:
the universal output multiplier is $5eB_N$, while



$$
\frac{5e}{4e-2}=1.5317495919507\ldots>1.              \tag{11}
$$



Thus this theorem quantifies both the available analytic freedom and its
precise width-only limitation.  It proves neither irrationality nor
transcendence of $e+\pi$.

## 2. Integrating-factor identity and the universal upper bound

The native integrating-factor identity is



$$
F_{N,H}(1-t)=e^t\{G'(t)+w(t)\}=e^t\nu(t).             \tag{12}
$$



Since $G(0)=G(1)=0$, the density in (3) has fixed total mass:



$$
\boxed{\int_0^1\nu(t)\,dt=B_N.}                      \tag{13}
$$



A direct differentiation gives



$$
\boxed{
 R'(t)=\frac{4e^t(2-t)^2}{(t^2-2t+2)^2}>0,\qquad
 R(0)=e+2,\qquad R(1)=5e.}                            \tag{14}
$$



Thus ${\cal L}_N(G)/B_N$ is a strict weighted average of $R$, proving
(6)--(7).  Integration by parts also gives the exact affine functional



$$
\boxed{
 {\cal L}_N(G)={\cal L}_N(0)-\int_0^1R'(t)G(t)\,dt,
 \qquad
 {\cal L}_N(0)=\int_0^1R(t)w(t)\,dt.}                \tag{15}
$$



Finally, the substitution $t=1-y/N$, together with dominated convergence,
gives



$$
NB_N=\int_0^N e^{-(1-y/N)}(1-y/N)^N\,dy
 \longrightarrow e^{-1}.                             \tag{16}
$$



The elementary bounds



$$
\frac1{e(N+1)}\leq B_N\leq\frac1{N+1}               \tag{17}
$$



will also be used below.

## 3. A strict base profile with integral endpoint jets

Fix an integer $m\geq2$, put $c=1/m$, and define



$$
g_0=(A,b),\qquad \ell=\frac{A}{g_0},\qquad
 \epsilon_c=\frac{c}{eA\ell},\qquad
 \Phi_c(y)=\frac{cy^2}{y+\epsilon_c}.                 \tag{18}
$$



Then $A\mid b\ell$, and



$$
0\leq\Phi_c'(y)
 =c\left(1-\frac{\epsilon_c^2}{(y+\epsilon_c)^2}\right)<c. \tag{19}
$$



Let



$$
J(t)=\int_t^1w(s)\,ds,\qquad
 G_L(t)=\mu(t)(1-4t^2),\qquad
 G_{R,c}(t)=\Phi_c(J(t)).                              \tag{20}
$$



On $(0,1/4]$, one has $G_L'>0$, while



$$
G_{R,c}'=-\Phi_c'(J)w,
 \qquad w+G_{R,c}'>(1-c)w.                            \tag{21}
$$



The two branches cross transversely before $1/4$.  Indeed,
$G_L(0)=0<G_{R,c}(0)$, whereas $G_{R,c}(1/4)<J(1/4)<G_L(1/4)$.
The last inequality was proved in the native sign-existence construction;
for completeness, its elementary cases are



$$
\begin{array}{c|c}
 N=2&G_L(1/4)=27e^{-1/4}/64>21/64>J(1/4),\\
 N=3&G_L(1/4)=9e^{-1/4}/16>1/4>J(1/4),
 \end{array}                                           \tag{22}
$$



and for $N\geq4$, $b\geq14$ gives



$$
G_L(1/4)\geq\frac{3b}{64}e^{-1/4}
 >\frac1{N+1}>J(1/4).                                 \tag{23}
$$



The difference $G_L-G_{R,c}$ is strictly increasing on $[0,1/4]$, so
this crossing is unique there.  Take the left branch before the crossing and
the right branch afterward, continuing identically with $G_{R,c}$ all the
way to $1$.  In a sufficiently small compact neighborhood
$U\Subset(0,1/4)$ of the crossing only, smooth the resulting corner from
below by the standard smooth convex regularization of the local minimum.
Outside $U$, leave the two selected pieces unchanged.  Because the
smoothed derivative on $U$ is a convex combination of the two branch
derivatives, this produces
$G_{N,c}\in C^\infty[0,1]$, unchanged in endpoint neighborhoods, with



$$
\boxed{
 G_{N,c}(0)=G_{N,c}(1)=0,\quad
 0<G_{N,c}<\mu,\quad
 w+G_{N,c}'\geq(1-c)w.}                               \tag{24}
$$



The local regularization may and will be chosen no larger than either branch
on $U$.  Together with the selected pieces outside $U$, this gives



$$
G_{N,c}\leq G_L\quad(0\leq t\leq1/4),
 \qquad G_{N,c}=G_{R,c}\quad\hbox{near }t=1.          \tag{25}
$$



It remains to check the endpoint lattice.  Put $s=1-t$.  Direct series
division gives



$$
\frac{G_{R,c}(1-s)}{\mu(1-s)}
 =\ell s^2+
 \left\{\ell(1-N)-\frac{A\ell^2}{c}
                 +\frac{b\ell}{A}\right\}s^3+O(s^4). \tag{26}
$$



Since $c=1/m$, the cubic coefficient



$$
C_{N,m}=\ell(1-N)-mA\ell^2+\frac{b\ell}{A}           \tag{27}
$$



is an integer.  Consequently the function $q_{N,c}$ from (3) has



$$
\begin{aligned}
 q_{N,c}(t)&=-t^2-2t^3+O(t^4) &&(t\to0),\\
 q_{N,c}(1-s)&=-1+(\ell+2)s^2+C_{N,m}s^3+O(s^4)
 &&(s\to0).                                           \tag{28}
 \end{aligned}
$$



Thus all endpoint Taylor coefficients through order three are integers.

## 4. An ordered mass-transfer perturbation

Let



$$
\rho(u)=c_0
 \begin{cases}
  \exp\{-1/(1-u^2)\},&|u|<1,\\
  0,&|u|\geq1,
 \end{cases}
 \qquad \int_{-1}^1\rho(u)\,du=1,                    \tag{29}
$$



and define the early probability density



$$
u(t)=16\rho(16t-3).                                   \tag{30}
$$



It is supported in $(1/8,1/4)$.  For the late cutoff put



$$
\eta(x)=
 \begin{cases}e^{-1/x},&x>0,\\0,&x\leq0,\end{cases}
 \qquad
 S(x)=\frac{\eta(x)}{\eta(x)+\eta(1-x)},              \tag{31}
$$





$$
\chi(y)=S(4(y-1))S(4(2-y)),\qquad
 \chi_N(t)=\chi(N(1-t)).                              \tag{32}
$$



Then $0\leq\chi\leq1$, it is supported in $(1,2)$, and it equals one
on $[5/4,7/4]$.  Set



$$
C_N^\chi=\int_0^1w(t)\chi_N(t)\,dt.                 \tag{33}
$$



Use the base profile in Section 3 with $m=4$, so $c=1/4$, and take
$\lambda=1/2$.  Define $K_N$ by



$$
K_N(0)=0,\qquad
 K_N'(t)=\lambda C_N^\chi u(t)-\lambda w(t)\chi_N(t). \tag{34}
$$



The two terms in (34) have equal integrals and ordered disjoint supports for
$N\geq8$.  Therefore



$$
K_N\in C^\infty[0,1],\qquad K_N\geq0,\qquad
 K_N=0\ \hbox{in endpoint neighborhoods},\qquad
 0\leq K_N\leq\lambda C_N^\chi.                       \tag{35}
$$



Put



$$
G_-=G_{N,1/4},\qquad G_+=G_{N,1/4}+K_N.              \tag{36}
$$



The differential inequality follows immediately from (24) and (34):



$$
w+G_+'\geq(1-c-\lambda)w=\frac14w>0.                \tag{37}
$$



The upper range barrier is also preserved.  Indeed,



$$
K_N\leq\frac12B_N\leq\frac1{2(N+1)}\leq\frac1{18}. \tag{38}
$$



If $K_N(t)>0$ and $t\leq1/4$, then $t>1/8$, and (25) gives



$$
\mu(t)-G_-(t)\geq4t^2\mu(t)
 \geq\frac{b}{1024e}>1                                \tag{39}
$$



for $N\geq8$, because $b\geq(8!-2^4)/2=20152$ and $e<3$.
For $t\geq1/4$, $G_-=G_{R,c}$; since $\mu$ increases and
$G_{R,c}$ decreases, the gap is increasing, and its value at $1/4$
already exceeds $\mu(1/4)-G_L(1/4)>1$.  Equations (38)--(39) prove
$G_+<\mu$.  Positivity is automatic from $G_->0$ and $K_N\geq0$.

Because $K_N$ vanishes in endpoint neighborhoods, the two associated
$q$'s have identical endpoint germs and hence retain (28).  More generally,
every



$$
G_\theta=G_-+\theta K_N,\qquad 0\leq\theta\leq1,      \tag{40}
$$



is strict and has those same integral endpoint jets.

Using (15), followed by integration by parts in (34), gives the exact output
difference



$$
\begin{aligned}
 \Delta_N&={\cal L}_N(G_-)-{\cal L}_N(G_+)
           =\int_0^1R'K_N\\
 &=\lambda C_N^\chi
 \left\{
 \frac{\int_0^1R(t)w(t)\chi_N(t)\,dt}{C_N^\chi}
 -\int_0^1R(t)u(t)\,dt
 \right\}.                                            \tag{41}
 \end{aligned}
$$



On the support of $u$, $R\leq R(1/4)$, and on the support of
$\chi_N$, $R\geq R(3/4)$ for $N\geq8$.  Moreover, on
$5/4\leq y=N(1-t)\leq7/4$, one has $t\geq25/32$ and



$$
t^N\geq e^{-56/25}>e^{-3},\qquad e^{-t}\geq e^{-1}. \tag{42}
$$



The $t$-interval has length $1/(2N)$, so



$$
C_N^\chi\geq\frac{e^{-4}}{2N}.                       \tag{43}
$$



Equations (41)--(43), together with



$$
R(3/4)-R(1/4)
 =64\left(\frac{e^{3/4}}{17}-\frac{e^{1/4}}{25}\right), \tag{44}
$$



prove (9).

The constant in (9) is strictly positive already from
$25e^{1/2}>25>17$; its decimal value is recorded only for orientation.

## 5. Sharpness of the upper constant

We now vary the harmless auxiliary choices in Section 4.  Fix
$0<\alpha<\alpha'<\beta'<\beta$, and choose a smooth cutoff
$0\leq\chi\leq1$, supported in $(\alpha,\beta)$, which equals one on
$[\alpha',\beta']$.  Choose $0<\delta<1/8$ and a smooth probability
density $u_\delta$ supported in $(\delta,2\delta)$.  Finally take the base profile with
$c=1/m$, and choose any $0<\lambda<1-c$.

For all sufficiently large admissible $N$, the two supports are ordered.
The construction (33)--(40), with $u_\delta$ and this $\chi$, remains
valid.  The only point needing comment is the upper barrier.  On the fixed
early support,



$$
\mu-G_{N,c}\geq4t^2\mu\gg_{\delta}b,                \tag{45}
$$



whereas $0\leq K_N\leq B_N\leq1/(N+1)$.  The displayed lower bound
increases on $[\delta,1/4]$, and after $1/4$ the gap itself increases
because $\mu'>0>G_{R,c}'$.  Since $b=(N!-R_N)/2\to\infty$, (45)
therefore proves the barrier for all sufficiently large $N$.

Let



$$
M_\chi=\int_0^\infty e^{-y}\chi(y)\,dy,
 \qquad \overline R_{u,\delta}=\int_0^1R(t)u_\delta(t)\,dt. \tag{46}
$$



The same substitution as in (16), now on the fixed compact support of
$\chi$, yields



$$
NC_N^\chi\longrightarrow e^{-1}M_\chi,
 \qquad
 \frac{\int Rw\chi_N}{C_N^\chi}\longrightarrow R(1). \tag{47}
$$



Therefore the corresponding output difference satisfies



$$
\boxed{
 N\Delta_N\longrightarrow
 \frac{\lambda}{e}M_\chi\{R(1)-\overline R_{u,\delta}\}.} \tag{48}
$$



Letting successively $m\to\infty$, $\lambda\uparrow1-1/m$,
$\delta\downarrow0$, $\alpha'\downarrow0$, and
$\beta'\to\infty$, the right side of (48) approaches



$$
\frac{R(1)-R(0)}e=4-\frac2e.                         \tag{49}
$$



Thus $\liminf N{\cal W}_N\geq4-2/e$.  Equation (7) supplies the reverse
limsup, proving (8).  Notice that every approximating pair in this argument
has identical endpoint *germs*, not merely equal jets through order three.

## 6. Exact rational-grid consequence and obstruction

Every open real interval of width $w>0$ contains a rational $c/D$ with



$$
1\leq D\leq\lfloor1/w\rfloor+1.                      \tag{50}
$$



In the native normalization,


$$
{\cal L}_N(G)=N!(e+\pi)+{\mathfrak c}_N(q),            \tag{50a}
$$


where ${\mathfrak c}_N(q)$ is the affine real moment coordinate that
becomes $c/D$ for a rational polynomial profile.  Thus translating by the
fixed term $N!(e+\pi)$ does not change widths.  The affine family (40)
sweeps an open interval in ${\mathfrak c}_N$ of exactly the width
$\Delta_N$.  Its endpoint jets are integral and fixed.  Therefore the
exact-moment integer approximation theorem applies to any rational coordinate
selected by (50), while strict sign control survives a sufficiently close
$C^3$ approximation.

If $w_N\sim C/N$, equation (50) guarantees only



$$
D\leq\frac{N}{C}+O(1)=O(N).                          \tag{51}
$$



It does not guarantee $D=o(N)$, and one-sided Farey gaps show that no such
conclusion follows from width alone.  The stronger condition



$$
Nw_N\longrightarrow\infty                            \tag{52}
$$



would imply $D=o(N)$, but (7) proves that (52) cannot occur in this native
family.

There is a second, constant-level obstruction to the crudest rational-case
argument.  If $e+\pi=u/v\in\mathbb Q$, then $v\mid N!$ for all
sufficiently large $N$, and every reduced rational output coordinate
$c/D$ gives



$$
{\cal L}_N(G)=N!\frac uv+\frac cD,\qquad
 D{\cal L}_N(G)\in\mathbb Z_{>0}.                     \tag{53}
$$



A width-only grid choice has $D\leq w_N^{-1}+1$.  Combined only with the
universal upper bound in (6), it gives


$$
D{\cal L}_N(G)\leq(w_N^{-1}+1)5eB_N.                 \tag{53a}
$$


Here the contribution $5eB_N$ from the additive $+1$ is $o(1)$.
Thus this comparison could force the positive integer below one only if,
asymptotically,



$$
\frac{w_N}{B_N}>5e.                                  \tag{54}
$$



But (7) gives $w_N/B_N\leq4e-2<5e$.  Equivalently, in the $N$-scaled
normalization, the largest possible width constant is $4-2/e$, while the
universal output upper constant is $5$.  This proves only a limitation of
the width-only argument: more precise positional or arithmetic information
could still be useful.

## 7. Scope and replay

The all-parameter conclusions are the integrating-factor formula (15), the
universal range (6), the explicit $c_*/N$ construction (9), the sharp
same-germ asymptotic diameter (8), and the rational-grid limitation
(50)--(54).  No finite computation is used to infer any of these statements.

From the research directory run

    python3 scripts/common_kernel_native_sign_output_range_sharp_width_certificate.py

The deterministic replay checks all symbolic identities, endpoint series,
explicit constants, and representative exact admissible parameters.  It
uses no accelerator and has a 2 GiB RAM cap.
