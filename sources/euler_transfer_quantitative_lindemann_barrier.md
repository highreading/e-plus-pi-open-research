> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Euler transfer to a small exponential: exact height reduction and the
# exponent-two quantitative Lindemann barrier

Date: 2026-08-27 (UTC)

## 1. Question and verdict

Assume, solely in order to test this route, that


$$
({\rm H})\qquad s=e+\pi\in\overline{\mathbb Q}.
\tag{1}
$$


For a reduced rational number $r=p/q$ approximating $e$, put


$$
\beta_r=i(s-r)\in K:=\mathbb Q(s,i).
\tag{2}
$$


Euler's identity gives the exact transfer


$$
\exp(\beta_r)+1
 =1-\exp\bigl(i(e-r)\bigr),
\qquad
 |\exp(\beta_r)+1|
 =2\left|\sin\frac{e-r}{2}\right|.
\tag{3}
$$


Consequently, when $|e-r|\leq1$,


$$
\frac{2}{\pi}|e-r|
 \leq |\exp(\beta_r)+1|
 \leq |e-r|.
\tag{4}
$$



The result of the audit is an exact no-go for all presently available
quantitative Lindemann estimates applied in this direct way.

> **Exponent-two barrier.**  The algebraic numbers $\beta_r$ have bounded
> degree and logarithmic height $\log q+O_s(1)$.  The convergents
> $p_m/q_m$ of $e$ satisfy
> 

$$
> -\frac{\log |\exp(\beta_{p_m/q_m})+1|}{\log q_m}=2+o(1),
> \tag{5}
>
$$


> and on the explicit subsequence $m=3k-2$,
> 

$$
> q_m^2|\exp(\beta_{p_m/q_m})+1|<\frac1{2k}\longrightarrow0.
> \tag{6}
>
$$


> Hence a uniform lower bound
> 

$$
> |\exp(i(s-p/q))+1|\geq C_s q^{-\kappa}
> \tag{7}
>
$$


> would contradict (1) if $\kappa<2$, and would also contradict (1) if
> $\kappa=2$ and $C_s>0$.  Bounds with $\kappa>2$ are compatible with
> the known approximants.
>
> Nesterenko--Waldschmidt's uniform simultaneous exponential estimate,
> optimized over its free parameter, has a height coefficient strictly
> larger than $1266D$, where
> $D=[\mathbb Q(\beta_r):\mathbb Q]$.  A completely explicit uniform
> specialization given below has an exponent $\kappa_{\rm NW}(d)>2$, with
> $d=[\mathbb Q(s):\mathbb Q]$, by many orders of magnitude.  Thus it
> cannot meet (7) at the required exponent-two threshold.

No degree or height is assumed for $s$.  Throughout the note


$$
d=[\mathbb Q(s):\mathbb Q],\qquad h_s=h(s)
\tag{8}
$$


remain unknown fixed parameters.  No conclusion about the arithmetic nature
of $e+\pi$ is claimed.

## 2. Exact degree and height bookkeeping

Let $h$ be the absolute logarithmic Weil height.  Translation by a rational
number and the elementary height inequalities give


$$
h(s-r)\leq h_s+h(r)+\log2,
 \qquad
 h(r)\leq h_s+h(s-r)+\log2.
\tag{9}
$$


Multiplication by the root of unity $i$ preserves height, so


$$
|h(\beta_r)-h(r)|\leq h_s+\log2.
\tag{10}
$$


For $2\leq p/q\leq3$,


$$
\log q\leq h(p/q)=\log\max(|p|,q)\leq\log q+\log3.
\tag{11}
$$


Combining (10) and (11),


$$
\log q-h_s-\log2
 \leq h(\beta_r)
 \leq\log q+h_s+\log6.
\tag{12}
$$



Also


$$
[\mathbb Q(s-r):\mathbb Q]=d,
 \qquad
 D_r:=[\mathbb Q(\beta_r):\mathbb Q]\leq2d,
\tag{13}
$$


because $\mathbb Q(s-r)=\mathbb Q(s)$ and
$\beta_r\in\mathbb Q(s,i)$.  These statements track the unknown degree and
height rather than silently treating them as absolute constants.

There is a parallel naive-length calculation.  Write the primitive minimal
polynomial of $s$ as


$$
P_s(X)=\sum_{j=0}^d a_jX^j,\qquad
 L_s=\sum_{j=0}^d|a_j|.
\tag{14}
$$


Then $\xi_r=s-p/q$ is a root of the degree-$d$ integer polynomial


$$
Q_{p,q}(X)=q^dP_s(X+p/q).
\tag{15}
$$


Since $Q_{p,q}$ and the minimal polynomial of $\xi_r$ have the same
degree, primitive normalization can only decrease the length.  If
$2\leq p/q\leq3$,


$$
L(\xi_r)\leq L(Q_{p,q})
 \leq q^d4^dL_s.
\tag{16}
$$



## 3. Direct application of the sharp explicit simultaneous theorem

The primary source used here is Yu. Nesterenko and M. Waldschmidt,
*On the approximation of the values of exponential function and logarithm by
algebraic numbers*, Theorem 1, arXiv:math/0002047
(published in *Mat. Zapiski* 2 (1996), 23--42):

<https://arxiv.org/abs/math/0002047>

In the notation of that theorem, take


$$
\theta=\beta_r,\qquad \alpha=-1,\qquad
 \beta=\beta_r,
\tag{17}
$$


so that its second approximation term $|\theta-\beta|$ is exactly zero.
Let $D=D_r$, choose


$$
\log A=D^{-1},\qquad \log B=h(\beta_r),
 \qquad E=e^x\quad(x\geq1).
\tag{18}
$$


All hypotheses of their Theorem 1 are then met.  Since
$|\beta_r|>1$ for $|e-r|\leq1$, the theorem gives


$$
|\exp(\beta_r)+1|\geq \exp\{-\mathcal N_r(x)\},
\tag{19}
$$


where


$$
\begin{split}
 \mathcal N_r(x)={}&211D
 \bigl(h(\beta_r)+3\log D+2\log(e^x|\beta_r|)+10\bigr)\\
 &\times\bigl(1+2e^x|\beta_r|+6x\bigr)
 \bigl(3.3D\log(D+2)+x\bigr)x^{-2}.
\end{split}
\tag{20}
$$


This is the exact specialization; in particular, the varying height occurs
only in the first factor.

For a fixed $D$ and a limiting modulus $M>0$, the best coefficient of
$h(\beta_r)$ furnished by this theorem is


$$
\kappa_{\rm NW}^{\rm opt}(D,M)
 =211D\min_{x\geq1}
 \frac{(1+2Me^x+6x)(3.3D\log(D+2)+x)}{x^2}.
\tag{21}
$$


The minimum exists.  Moreover every $x\geq1$ satisfies


$$
\frac{(1+2Me^x+6x)(3.3D\log(D+2)+x)}{x^2}>6,
\tag{22}
$$


and hence


$$
\kappa_{\rm NW}^{\rm opt}(D,M)>1266D>2.
\tag{23}
$$


Thus even optimizing the theorem's free parameter cannot approach the needed
threshold.

For a single completely explicit bound, take $x=2$.  Since


$$
|\beta_r|=|\pi+e-r|\leq\pi+1,qquad D_r\leq2d,
\tag{24}
$$


monotonicity of the displayed positive factors gives


$$
|\exp(\beta_r)+1|
 \geq C(s)q^{-\kappa_{\rm NW}(d)},
\tag{25}
$$


where $C(s)>0$ is effective in $d,h_s$, and one may take


$$
\boxed{
 \kappa_{\rm NW}(d)=
 \frac{211(2d)}4
 \bigl(13+2e^2(\pi+1)\bigr)
 \bigl(3.3(2d)\log(2d+2)+2\bigr).
}
\tag{26}
$$


For example, even the formal smallest case $d=1$ gives an exponent above
$8\times10^4$, rather than an exponent at most $2$.

As a cross-check, Theorem 2 of the same primary source and (16) give the
weaker but simpler estimate


$$
|e-p/q|=|\pi-(s-p/q)|
 \geq C'(s)q^{-1.2\cdot10^6d^2(1+\log d)}.
\tag{27}
$$


Again its exponent is far on the compatible side of the barrier.

## 4. The rational approximants hit exponent two exactly

Henry Cohn's primary proof gives


$$
e=[2;1,2,1,1,4,1,1,6,\ldots],
\tag{28}
$$


with


$$
a_{3k-2}=1,\qquad a_{3k-1}=2k,\qquad a_{3k}=1
 \quad(k\geq1).
\tag{29}
$$


See H. Cohn, *A short proof of the simple continued fraction expansion of
e*, Amer. Math. Monthly 113 (2006), 57--62:

<https://arxiv.org/abs/math/0601660>

For any simple continued fraction and its convergents $p_m/q_m$,


$$
\frac1{q_m(q_m+q_{m+1})}
 <\left|e-\frac{p_m}{q_m}\right|
 <\frac1{q_mq_{m+1}}.
\tag{30}
$$


Using $q_{m+1}=a_{m+1}q_m+q_{m-1}$ gives


$$
\frac1{(a_{m+1}+2)q_m^2}
 <\left|e-\frac{p_m}{q_m}\right|
 <\frac1{a_{m+1}q_m^2}.
\tag{31}
$$


On $m=3k-2$, the next partial quotient is $a_{m+1}=2k$, so


$$
q_m^2\left|e-\frac{p_m}{q_m}\right|<\frac1{2k}\to0.
\tag{32}
$$


Equations (4), (31), and the elementary lower growth
$q_m\geq F_{m+1}$ prove (5) and (6).

This is not just a property of one chosen family.  The current sharp theorem
for rational approximation to values of $E$-functions implies that the
irrationality exponent of $e=\exp(1)$ is exactly $2$: S. Fischler and
T. Rivoal, *Rational approximations to values of E-functions*, Theorem 1,
arXiv:2312.12043v2 (10 July 2025):

<https://arxiv.org/abs/2312.12043>

For every $\varepsilon>0$, there is $c_\varepsilon>0$ such that


$$
\left|e-\frac pq\right|\geq c_\varepsilon q^{-2-\varepsilon}
\tag{33}
$$


for all integers $p$ and positive integers $q$.  Thus no rational or
Pad\'e family can supply infinitely many errors of exponent
$2+\delta$ for a fixed $\delta>0$.  Equations (31)--(33) identify the
sharp approximation scale on both sides.

## 5. Why Baker theory does not give a missing bound

Taking a logarithm of (3) suggests the small quantity


$$
\beta_r-i\pi=i(e-r).
\tag{34}
$$


Although $i\pi$ is a logarithm of the algebraic number $-1$, the other
term $\beta_r$ is an **additive algebraic number**, not a logarithm of an
algebraic number.  Standard Baker--Matveev theorems concern algebraic linear
combinations of logarithms of algebraic numbers.  Writing
$\beta_r=\log(e^{\beta_r})$ is unusable because
$e^{\beta_r}$ is transcendental by Lindemann--Weierstrass.  Therefore a
classical linear-form-in-logarithms theorem does not apply to (34); the
simultaneous Hermite--Lindemann estimate in Section 3 is the appropriate
uniform theorem.

## 6. Audit of the newer fixed-exponent transcendence measure

Fischler--Rivoal's newer primary paper *A new transcendence measure for the
values of the exponential function at algebraic arguments*, Theorem 1 and
Proposition 1, arXiv:2502.17992, improves the height exponent for
$P(e^\alpha)$ when the algebraic exponent $\alpha$ is fixed:

<https://arxiv.org/abs/2502.17992>

It does not provide a uniform improvement here.  In this route the exponent
is $\alpha=\beta_r$, which changes with $r$, whereas the constant in that
theorem is explicitly allowed to depend on $\alpha$.  Taking
$P(X)=X+1$ gives polynomial height $H(P)=1$, so all dependence on $q$
is hidden in the varying constant.  The paper's explicit Proposition 1
indeed contains the denominator $d(1/\alpha)$, the house of
$1/\alpha$, and additional powers of those quantities.  It therefore does
not replace the uniform varying-exponent estimate (20).

## 7. Exact stopping criterion for this route

Under (1), the following new local theorem would suffice:

> There exist $C_s>0$ and $\kappa\leq2$ such that, for every reduced
> $p/q$ sufficiently close to $e$,
> 

$$
> |\exp(i(s-p/q))+1|\geq C_s q^{-\kappa}.
> \tag{35}
>
$$



If $\kappa<2$, ordinary convergents contradict (35).  If $\kappa=2$,
the explicit subsequence (32) contradicts it.  Existing uniform
Hermite--Lindemann estimates give only $\kappa\gg_d1>2$, while the sharp
rational approximation theory of $e$ gives the compatible lower scale
$2+\varepsilon$.  The gap is therefore not an unoptimized constant or an
unexploited Pad\'e family: it is exactly the endpoint exponent $2$.

