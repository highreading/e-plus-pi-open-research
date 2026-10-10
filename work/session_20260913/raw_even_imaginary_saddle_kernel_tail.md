> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform imaginary-node kernel tail for the even exterior saddle

Date: 2026-09-13. Original bounded lemma by audit_sources.
Independent review requested.

This proves the missing norm convergence of the actual scalar Cauchy evaluation kernel at


$$
y_s=-i/\sqrt5
$$


for the even common Cayley measure. It does not reuse the special Rodrigues endpoint ratio at $y=\pm i$.

## 1. Positive recurrence on the imaginary axis

Let $m\ge1$, $\beta=2m+1$, and let $q_j^{(m)}$, $0\le j\le m$, be the positive-leading orthonormal polynomials for a positive constant times $(1+y^2)^{-\beta}dy$. Put $\eta=1/\sqrt5$. Their recurrence is


$$
a_jq_j=yq_{j-1}-a_{j-1}q_{j-2},\qquad
a_j^2=\frac{j(2\beta-j)}{(2\beta-2j)^2-1},\quad a_0=0.
$$


Parity and induction give


$$
q_j(-i\eta)=(-i)^j d_j,\qquad d_j>0,
$$


where


$$
a_jd_j=\eta d_{j-1}+a_{j-1}d_{j-2}.
$$


Thus, with $r_j=d_j/d_{j-1}$,


$$
r_1=\eta/a_1,\qquad
r_j=\frac{\eta+a_{j-1}/r_{j-1}}{a_j}\quad(j\ge2).        \tag{1}
$$



The coefficients $a_j$ increase with $j$. Indeed, writing $x=\beta-j$, their square is $(\beta^2-x^2)/(4x^2-1)$, which decreases as $x>1/2$ increases. For $j\le m$,


$$
a_j^2\le a_m^2
=\frac{m(3m+2)}{(2m+1)(2m+3)}<\frac34.
$$


In particular every ratio satisfies


$$
r_j\ge\frac{\eta}{a_j}>\frac2{\sqrt{15}}.               \tag{2}
$$



## 2. Uniform two-step growth

For every $m\ge20$ and $2\le j\le m$,


$$
\boxed{r_jr_{j-1}\ge\frac{11}{10}.}                    \tag{3}
$$


From (1)-(2),


$$
r_jr_{j-1}
\ge\frac{\eta^2}{a_ja_{j-1}}+\frac{a_{j-1}}{a_j}.       \tag{4}
$$



For $2\le j\le9$, the first summand alone suffices. Monotonicity in $j$ gives


$$
a_ja_{j-1}\le a_9^2
\le\frac{9(4m+2)}{(4m-16)^2-1}
\le\frac{82}{455}.
$$


The last rational function decreases for $m\ge20$, as is immediate on writing $x=4m-16$ and differentiating $(x+18)/(x^2-1)$. Therefore


$$
\eta^2/(a_ja_{j-1})\ge91/82>11/10.
$$



For $10\le j\le m$, the exact ratio identity is


$$
\frac{a_{j-1}^2}{a_j^2}
=\frac{j-1}{j}\frac{2\beta-j+1}{2\beta-j}
 \frac{2\beta-2j-1}{2\beta-2j+3}
\ge\frac9{10}\frac{2m+1}{2m+5}\ge\frac{41}{50}.
$$


Also $\eta^2/(a_ja_{j-1})>4/15$. Hence (4) is at least
$\sqrt{41/50}+4/15>11/10$. This proves (3).

Let


$$
t_{m,r}=d_{m-r}/d_m,\quad 0\le r\le m.
$$


Pairing successive factors in its reciprocal product and using (2) for a possible unpaired factor proves


$$
t_{m,r}\le\frac{\sqrt{15}}2
       \left(\frac{10}{11}\right)^{\lfloor r/2\rfloor},
\quad m\ge20.                                         \tag{5}
$$


This is a summable uniform squared-tail bound. It controls every reversed index, not only a fixed distance from the top.

## 3. The fixed-distance ratio limit

For every fixed integer $k$,


$$
a_{m-k}\longrightarrow a_*=\sqrt3/2.
$$


The limiting ratio map in (1) is


$$
T(r)=c+\frac1r,\qquad c=\frac2{\sqrt{15}}.
$$


Its positive fixed point is


$$
R=\frac{c+\sqrt{c^2+4}}2=\sqrt{5/3}.                    \tag{6}
$$


For completeness, the initial state far below a fixed final window cannot invalidate this limit. In any fixed window near $m$, the actual ratios lie in a fixed compact interval for all sufficiently large $m$. The lower bound is $c$. When $a_j\ge1/2$, (1)-(2) give the upper bound


$$
r_j\le2\eta+\frac{3}{2\eta}=\frac{19}{2\sqrt5}<5.
$$


Thus one may use the interval $[c,5]$.

The constant two-step map has derivative


$$
(T^2)'(r)=\frac1{(cr+1)^2}
\le\left(\frac{15}{19}\right)^2<1
\quad(r\ge c).
$$


Its iterates therefore converge uniformly to $R$ for starting states in $[c,5]$. For a fixed final window, the actual maps in (1) converge uniformly to $T$ on the needed compact intervals. Compare these finite compositions, take $m\to\infty$ first, and then let the window length tend to infinity. This proves


$$
r_{m-k}\longrightarrow R
$$


for every fixed $k$. Consequently


$$
t_{m,r}\longrightarrow (3/5)^{r/2}
\quad\hbox{for every fixed }r.                         \tag{7}
$$


No convergence rate is inferred from this fixed-window argument.

## 4. Normalization, phases, and the complete kernel limit

The normalized Riesz vector for evaluation at $-i\eta$ has original coefficients proportional to
$\overline{q_j(-i\eta)}=i^j d_j$. Reverse $j=m-r$ and multiply the whole vector by the harmless phase $(-i)^m$. Its coordinates then become


$$
k_{m,r}=(-i)^r
 \frac{d_{m-r}}{\left(\sum_{j=0}^m d_j^2\right)^{1/2}},
\quad 0\le r\le m.
$$


Extend them by zero for $r>m$.

The bound (5) and dominated summation give


$$
\sum_{r=0}^m t_{m,r}^2\longrightarrow
\sum_{r\ge0}(3/5)^r=\frac52.
$$


Therefore the full norm limit, not merely coefficientwise convergence, is


$$
\boxed{\displaystyle
k_m\longrightarrow k_s,\qquad
k_s(r)=\sqrt{2/5}\,(-i\sqrt{3/5})^r,\quad r\ge0.}        \tag{8}
$$


The normalized evaluation row is its conjugate transpose, so its phase is the opposite one.

An all-$m$ tail majorant is available without checking any finite list. Every normalized coefficient has modulus at most one. For $m<20$, there are only indices $r\le19$. Combining this observation with (5), the constant $C=(11/10)^{10}>\sqrt{15}/2$ gives


$$
|k_{m,r}|\le C(10/11)^{\lfloor r/2\rfloor}
\quad\hbox{for all }m\ge1,\ r\ge0.
$$


In particular, for every $N\ge0$,


$$
\left(\sum_{r\ge N}|k_{m,r}|^2\right)^{1/2}
\le C\sqrt{\frac2{1-(10/11)^2}}\,
       (10/11)^{\lfloor N/2\rfloor}.                    \tag{9}
$$


This uniform tail is deliberately coarse but sufficient for all the stated operator pairings.

The common positive scalar in the Cauchy measure cancels from the normalized kernel. The lemma supplies only this normalized vector; the actual exterior evaluation amplitude still requires the original Cayley scalar and endpoint normalization to be retained in its separate argument.

