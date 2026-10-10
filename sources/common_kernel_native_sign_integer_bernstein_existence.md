> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Integer Bernstein approximation gives native sign-controlled residuals

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
t=1-x,\qquad u=1+x^2,\qquad
 {\cal T}P=(1-x)P'-xP,
$$



and write



$$
(1-i)^N=R_N+iI_N,\qquad M_N=N!-R_N.                 \tag{1}
$$



For $N\geq2$, let



$$
K_N(x)=I_N-\frac{M_N}{2}(1-x)                         \tag{2}
$$



be the native integral Taylor--Robin correction.  Given 

$$
h\in
\mathbb Z[x]
$$

, define



$$
F_{N,h}(x)=(1-x)^N+{\cal T}(hK_N)(x).                \tag{3}
$$



The preceding endpoint theorem proved that a sign-controlled admissible
$h$ is impossible when $I_N>0$, or equivalently when
$N\equiv5,6,7\pmod8$.  This note proves the exact converse.

**Native sign-existence theorem.**  For every $N\geq2$ with



$$
I_N\leq0                       \tag{4}
$$



there exists a polynomial $h\in\mathbb Z[x]$ such that



$$
\boxed{
 h\equiv1\pmod{(1+x^2)^2},\qquad h(0)=0,\qquad
 0\leq h\leq1\ \hbox{on }[0,1],\qquad F_{N,h}\geq0.} \tag{5}
$$



Combining this theorem with the endpoint obstruction gives the exact
existence classification



$$
\boxed{
 \text{an admissible sign-controlled }h\text{ exists}
 \quad\Longleftrightarrow\quad
 N\not\equiv5,6,7\pmod8.}                              \tag{6}
$$



The construction has two parts.  First, an explicit transform of the
incomplete-gamma tail produces a smooth real profile satisfying all
inequalities with strict interior margins and with arithmetically compatible
Taylor jets at both endpoints.  Second, simultaneous approximation by
polynomials with integer coefficients transfers the profile to an actual
integer polynomial without losing the inequalities.

This is an existence theorem only.  It gives no useful upper bound for the
least possible degree or coefficient height.  In view of the preceding
factorial-quarter-root lower bound, any approximating degree is necessarily
enormous.  More importantly, the theorem gives no control of the reduced
rational-output denominator or primitive content.  It therefore does not
prove an arithmetic classification of $e+\pi$.

## 2. The differential inequality in tail coordinates

Assume (4) and set



$$
a=-I_N\geq0,\qquad b=\frac{M_N}{2}>0,\qquad A=a+b.    \tag{7}
$$



All three numbers are integers.  For a real profile



$$
H(t)=h(1-t)
$$



define



$$
\begin{aligned}
 w(t)&=e^{-t}t^N,\\
 J(t)&=\int_t^1 w(s)\,ds,\\
 \mu(t)&=t(a+bt)e^{-t},\\
 G(t)&=\mu(t)H(t).
 \end{aligned}                                         \tag{8}
$$



The exact integrating-factor identity is



$$
\boxed{
 F_{N,h}(1-t)=e^t\{G'(t)+w(t)\}.}                      \tag{9}
$$



Thus the sign condition is simply



$$
G'\geq-w.                      \tag{10}
$$



Also



$$
\mu'(t)=e^{-t}\{a(1-t)+bt(2-t)\}>0\qquad(0<t<1),     \tag{11}
$$



so $\mu$ is strictly increasing.  The inequalities $0\leq H\leq1$
are equivalent to



$$
0\leq G\leq\mu.               \tag{12}
$$



We will build a smooth $G$ satisfying (10)--(12), with endpoint shapes
chosen for integral approximation.

## 3. Two explicit strict subsolutions

Let



$$
\epsilon=\frac1{eA^2},\qquad
 \Phi(y)=\frac{y^2}{y+\epsilon}\quad(y\geq0).           \tag{13}
$$



Then



$$
\Phi'(y)=\frac{y(y+2\epsilon)}{(y+\epsilon)^2}
          =1-\frac{\epsilon^2}{(y+\epsilon)^2},         \tag{14}
$$



and hence



$$
0\leq\Phi'(y)<1.               \tag{15}
$$



Consider the two profiles



$$
\begin{aligned}
 G_L(t)&=\mu(t)(1-4t^2),\\
 G_R(t)&=\Phi(J(t)).
 \end{aligned}                                         \tag{16}
$$



On $0<t\leq1/4$, logarithmic differentiation gives



$$
\frac{\mu'}\mu
 =\frac1t+\frac b{a+bt}-1
 \geq\frac1t-1\geq3,
$$



whereas



$$
\frac{8t}{1-4t^2}\leq\frac83.
$$



Therefore



$$
G_L'(t)>0
              \qquad(0<t\leq1/4).                      \tag{17}
$$



For the right profile, $J'=-w$, so (14)--(15) give



$$
-w<G_R'<0
              \qquad(0<t<1).                           \tag{18}
$$



Both branches therefore satisfy the strict differential inequality (10).

They cross before $1/4$.  Indeed,



$$
G_L(0)=0<G_R(0).               \tag{19}
$$



At $t=1/4$, one has $G_R<J$, while $G_L>J$.  The latter
claim is uniform in $N$, as follows.

For $N=2$, $(a,b)=(2,1)$, and



$$
G_L(1/4)=\frac{27}{64}e^{-1/4},\qquad
 J(1/4)<\int_{1/4}^1s^2\,ds=\frac{21}{64}.             \tag{20}
$$



The elementary series estimate



$$
e^{1/4}<1+\frac14+\frac1{32}\sum_{j\geq0}12^{-j}
          =\frac{113}{88}<\frac97
$$



shows that the first quantity in (20) exceeds the second.  For $N=3$,
$(a,b)=(2,4)$, and



$$
G_L(1/4)=\frac9{16}e^{-1/4}>\frac{27}{64}>\frac14>J(1/4). \tag{21}
$$



For every $N\geq4$, one has $b\geq14$.  Indeed $b=14$ at $N=4$,
and for $N\geq5$,



$$
b\geq\frac{N!-2^{N/2}}2>14.
$$



Since
$e^{-1/4}>3/4$,



$$
G_L(1/4)
 \geq\frac{3b}{64}e^{-1/4}
 \geq\frac{126}{256}
 >\frac1{N+1}>J(1/4).                                  \tag{22}
$$



Consequently there is a first crossing



$$
\tau=\min\{t\in(0,1/4):G_L(t)=G_R(t)\}.              \tag{23}
$$



Define the continuous piecewise-smooth profile



$$
G_0(t)=
 \begin{cases}
 G_L(t),&0\leq t\leq\tau,\\
 G_R(t),&\tau\leq t\leq1.
 \end{cases}                                           \tag{24}
$$



It satisfies $0<G_0<\mu$ on $(0,1)$.  On the left this follows
from $H_L=1-4t^2$.  At the crossing,



$$
G_R(\tau)=\mu(\tau)(1-4\tau^2)<\mu(\tau).
$$



Thereafter $G_R$ decreases and $\mu$ increases, proving the claim
on the right.  Equations (17)--(18) give



$$
G_0'>-w                        \tag{25}
$$



on both smooth pieces.

## 4. Smoothing the one interior corner

Only the derivative jump at $\tau$ remains.  We record the elementary
smoothing step because strictness matters later.

The crossing is transverse: $G_L'(\tau)>0>G_R'(\tau)$.  Thus, on a compact
interval $U\Subset(0,1/4)$ around $\tau$, the piecewise function (24) is
exactly $G_0=\min(G_L,G_R)$.  Choose a smooth even function
$\sigma_\delta:\mathbb R\to\mathbb R$ such that



$$
\sigma_\delta(z)=|z|\quad(|z|\geq\delta),\qquad
 |\sigma_\delta'(z)|\leq1,\qquad
 |\sigma_\delta(z)-|z||\leq\delta.
$$



Such a function is obtained by smoothing the corner of $|z|$ inside
$(-\delta,\delta)$ with a monotone odd derivative taking values in
$[-1,1]$.  On $U$, set



$$
G(t)=\frac{G_L(t)+G_R(t)-
 \sigma_\delta(G_L(t)-G_R(t))}{2}.
$$



Choose $\delta$ smaller than $|G_L-G_R|$ at the two endpoints of $U$.
Then this formula agrees identically with the appropriate branch near those
endpoints, so it glues smoothly to (24) outside $U$, without a cutoff term.
Moreover,



$$
G'=\frac{1-\sigma_\delta'}2G_L'
    +\frac{1+\sigma_\delta'}2G_R'.
$$



The two coefficients are nonnegative and sum to one.  Both branch derivatives
are strictly greater than $-w$ on $U$, so the displayed convex combination
has the same property.  Its difference from $\min(G_L,G_R)$ is at most
$\delta/2$.  Taking $\delta$ sufficiently small, and using the positive
distance of both branches from $0$ and $\mu$ on $U$, therefore preserves



$$
0<G<\mu,\qquad G'>-w           \tag{26}
$$



throughout $U$.  Outside $U$, use (24).  This produces a $C^\infty$
function $G$ on $(0,1)$, equal to $G_L$ near zero and to $G_R$ near
one, and satisfying (26) everywhere.

Define



$$
H(t)=
 \begin{cases}
 G(t)/\mu(t),&0<t\leq1,\\
 1,&t=0.
 \end{cases}                                           \tag{27}
$$



Because the left branch is unchanged near zero, $H=1-4t^2$ there.
The right branch is analytic at one and vanishes quadratically there, as
shown below.  Hence $H\in C^\infty[0,1]$.  Equations (9) and (26) yield



$$
H(0)=1,\quad H(1)=0,\quad 0<H<1\ (0<t<1),\quad
 F_H(1-t)>0\ (0<t<1).                                  \tag{28}
$$



Here $F_H$ denotes the expression in (9) for the real profile $H$.

## 5. The endpoint jets land on the integer lattice

Put



$$
v(t)=1+(1-t)^2=t^2-2t+2
$$



and define



$$
q(t)=\frac{H(t)-1}{v(t)^2}.     \tag{29}
$$



Near zero, $H=1-4t^2$, so direct expansion gives



$$
q(t)=-t^2-2t^3+O(t^4).         \tag{30}
$$



For the other endpoint, put $s=1-t$.  From (8),



$$
\begin{aligned}
 J(1-s)
 &=e^{-1}\left\{s+\frac{1-N}{2}s^2+O(s^3)\right\},\\
 \mu(1-s)
 &=e^{-1}\left\{A-bs+O(s^2)\right\}.
 \end{aligned}                                         \tag{31}
$$



Using $\epsilon=e^{-1}A^{-2}$ in $G_R=J^2/(J+\epsilon)$, one obtains



$$
H(1-s)
 =As^2+\{-A^3+A(1-N)+b\}s^3+O(s^4).                  \tag{32}
$$



Since $v(1-s)=1+s^2$, equations (29) and (32) give



$$
q(1-s)
 =-1+(A+2)s^2+\{-A^3+A(1-N)+b\}s^3+O(s^4).           \tag{33}
$$



Every displayed coefficient in (30) and (33) is an integer.  Equivalently,



$$
\boxed{
 \frac{q^{(j)}(0)}{j!},\ \frac{q^{(j)}(1)}{j!}
 \in\mathbb Z\qquad(0\leq j\leq3).}                  \tag{34}
$$



The choice $\epsilon=1/(eA^2)$, rather than an arbitrary small positive
number, is precisely what makes the leading coefficient in (32) the integer
$A$ and the cubic coefficient integral as well.

## 6. Simultaneous approximation by integer polynomials

We need the following standard consequence of simultaneous integer Bernstein
approximation.

**Integer $C^3$-approximation lemma.**  Let $f\in C^3[0,1]$ satisfy



$$
\frac{f^{(j)}(0)}{j!},\ \frac{f^{(j)}(1)}{j!}
 \in\mathbb Z\qquad(0\leq j\leq3).                    \tag{35}
$$



Then there are $Q_n\in\mathbb Z[t]$ such that



$$
\|Q_n-f\|_{C^3[0,1]}\to0,     \tag{36}
$$



and, for all sufficiently large $n$, $Q_n$ has exactly the same endpoint
jets through order three as $f$.

For completeness, reduce this directly to the published theorem.  The ideals
$(t^4)$ and $((t-1)^4)$ are comaximal in $\mathbb Z[t]$; explicitly,



$$
(-20t^3+70t^2-84t+35)t^4
 +(20t^3+10t^2+4t+1)(t-1)^4=1.
$$



Therefore
the Chinese remainder theorem supplies $P\in\mathbb Z[t]$ matching the
two integral Taylor polynomials in (35).  The function $r=f-P$ has all
derivatives through order three equal to zero at both endpoints.

Draganov's nearest-integer Bernstein polynomial is



$$
\widehat B_n(r)(t)
=\sum_{k=0}^n
\left\langle r(k/n){n\choose k}\right\rangle
t^k(1-t)^{n-k}\in\mathbb Z[t],                        \tag{37}
$$



where $\langle\cdot\rangle$ denotes a nearest integer.  Theorem 1.3 of
the cited paper assumes



$$
r(0),r(1),r'(0),r'(1)\in\mathbb Z,qquad
 r^{(j)}(0)=r^{(j)}(1)=0\quad(2\leq j\leq3),
$$



and gives



$$
\|\{\widehat B_n(r)\}'''-r'''\|_\infty
 \leq C\left\{
 \omega_\varphi^2(r''',n^{-1/2})+
 \omega_1(r''',n^{-1})+
 \frac{\|r'''\|_\infty+1}{n}\right\}\longrightarrow0. \tag{38}
$$



The same operator converges uniformly to $r$; the standard interpolation
inequality between the zeroth and third derivatives then gives convergence of
the first two derivatives as well.  Thus
$Q_n=P+\widehat B_n(r)$ satisfies (36).  Notice that (37) has ordinary
monomial integer coefficients: each rounded scalar is an integer and each
$t^k(1-t)^{n-k}$ lies in $\mathbb Z[t]$.  This is stronger than merely
being integer-valued on some lattice or having unrestricted rational Bernstein
coefficients.  Finally,
$Q_n^{(j)}(0)/j!$ and $Q_n^{(j)}(1)/j!$ are integers.  Their convergence
to the corresponding integers in (35) makes them equal for all sufficiently
large $n$, proving the last assertion.

The reference used here is B. R. Draganov, ``Simultaneous approximation by
Bernstein polynomials with integer coefficients,'' *Journal of Approximation
Theory* **237** (2019), 1--16,
https://doi.org/10.1016/j.jat.2018.08.003; preprint
https://arxiv.org/abs/1804.08248.

Apply the lemma to the smooth function $q$ in (29).  We next verify that
the strict real inequalities survive for every sufficiently accurate member of
the sequence.

## 7. Endpoint-stable transfer of all inequalities

Write



$$
E_n=Q_n-q,\qquad H_n=1+v^2Q_n.                         \tag{39}
$$



Because the endpoint jets through order three agree, repeated integration
gives, near either endpoint $\xi\in\{0,1\}$,



$$
|E_n(t)|\leq\frac16\|E_n'''\|_\infty|t-\xi|^3,
 \qquad
 |E_n'(t)|\leq\frac12\|E_n'''\|_\infty|t-\xi|^2.      \tag{40}
$$



At zero, (30) says that $q=-t^2+O(t^3)$.  Equations (39)--(40) therefore
give the explicit endpoint margins



$$
1-H_n(t)=4t^2+O(t^3),\qquad H_n(t)=1+O(t^2)            \tag{41}
$$



as $t\downarrow0$, uniformly for every sufficiently large $n$.  At one,
(32) and (40) give



$$
H_n(t)=A(1-t)^2+O((1-t)^3).                            \tag{42}
$$



Since $A>0$, these formulas give, for every sufficiently large $n$,



$$
0<H_n(t)<1
$$



on fixed punctured neighborhoods of both endpoints.  On the remaining
compact subinterval, (28) has a positive distance from both boundary values,
so uniform convergence proves



$$
0\leq H_n\leq1\quad(0\leq t\leq1)              \tag{43}
$$



for all sufficiently large $n$.  The endpoint values are exact:
$H_n(0)=1$ and $H_n(1)=0$.

The residual is a continuous linear expression in $H_n,H_n'$.  Away from
zero, the strict inequality in (28) and $C^1$ convergence preserve its sign.
If $a>0$, its value at zero is $a$, so this also handles a neighborhood of
zero.  If $a=0$, use the exact local profile $H=1-4t^2$.  Formula (9)
then gives



$$
F_H(1-t)=2bt+O(bt^2)+t^N.                              \tag{44}
$$



Because (39) makes the perturbation in $H$ of order
$O(\|E_n'''\|t^3)$ and that in $H'$ of order
$O(\|E_n'''\|t^2)$, its contribution to the residual is
$O(b\|E_n'''\|t^4)$.  Equation (44) therefore preserves nonnegativity near
zero as well.  Hence, for every sufficiently large $n$,



$$
F_{H_n}(1-t)\geq0
                         \qquad(0\leq t\leq1).          \tag{45}
$$



Finally set



$$
h_n(x)=H_n(1-x).               \tag{46}
$$



Since $Q_n\in\mathbb Z[t]$, substitution in (39) gives



$$
h_n(x)=1+(1+x^2)^2Q_n(1-x)\in\mathbb Z[x].            \tag{47}
$$



Equations (43), (45), and (47), together with the exact endpoint values, prove
every assertion in (5), and hence the classification (6).

## 8. Scope, degree, and arithmetic output

The theorem closes the purely analytic existence question for this native
correction: the endpoint sign is the only obstruction to existence when degree
and height are unrestricted.  It does not contradict the earlier lower bound



$$
(\deg h)^4\geq\frac{M_N(N+1)}{54e},            \tag{48}
$$



because the integer Bernstein approximation may use arbitrarily high degree.
No quantitative claim about its least sufficient degree is made here.

Nor does positivity settle primitive normalization.  The earlier exact audit
shows that the raw common-kernel integral is of order $1/N$, but its primitive
value additionally contains the factor $D_{N,h}/g_{N,h}$.  The present
approximation theorem does not bound this ratio, and it does not reach the
stronger Roth-scale content threshold.  Thus (6) is a sign-existence
classification, not an arithmetic classification of $e+\pi$.

The deterministic replay checks the Gaussian recurrence, all symbolic
derivative identities, the uniform crossing inequalities, the two endpoint
series through the required order, and exact integral Hermite interpolation for
representative parameters.  It does not replace the cited all-degree
approximation theorem with a finite computation.

From the research directory run

    python3 scripts/common_kernel_native_sign_integer_bernstein_certificate.py
    sha256sum -c results/common_kernel_native_sign_integer_bernstein_hashes.sha256

The replay uses exact symbolic and rational CPU arithmetic.  No hardware
accelerator is useful, and its RAM use is negligible relative to the available
$50$ GiB.
