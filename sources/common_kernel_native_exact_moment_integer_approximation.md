> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact rational-moment preservation under integer $C^3$ approximation

Checked: 2026-08-27 UTC.

## 1. Verdict

Fix integers



$$
a\geq0,\qquad b\geq0,\qquad a+b>0,
$$



and put



$$
W(t)=(a+bt)t(2-t)^2,\qquad
 \ell(f)=4\int_0^1W(t)f(t)\,dt.                       \tag{1}
$$



These are exactly the native sign-possible weights.  This note proves:

**Exact-moment integer approximation theorem.**  Let
$f\in C^\infty[0,1]$ satisfy



$$
\frac{f^{(j)}(0)}{j!},\quad
 \frac{f^{(j)}(1)}{j!}\in\mathbb Z
 \qquad(0\leq j\leq3),                                \tag{2}
$$



and suppose $\ell(f)\in\mathbb Q$.  Then there are
$P_n\in\mathbb Z[t]$ such that



$$
P_n^{(j)}(0)=f^{(j)}(0),\qquad
 P_n^{(j)}(1)=f^{(j)}(1)
 \quad(0\leq j\leq3),                                 \tag{3}
$$





$$
\boxed{\ell(P_n)=\ell(f),\qquad
 \|P_n-f\|_{C^3[0,1]}\longrightarrow0.}               \tag{4}
$$



There is no hidden image restriction beyond rationality:



$$
\boxed{\ell(\mathbb Z[t])=\mathbb Q.}                \tag{5}
$$



More generally, for every nonzero $B\in\mathbb Z[t]$,



$$
\ell(B\mathbb Z[t])=\mathbb Q.                       \tag{6}
$$



The proof is constructive in principle but supplies no useful bound for the
degree or coefficient height needed to represent the initial rational moment.
It therefore solves the qualitative exact-moment approximation problem, not
the quantitative primitive-content problem.

There is also a precise Farey consequence and a precise warning.

* If, for infinitely many $N$, a $C^3$-stable family of strict real sign
  profiles sweeps an interval of rational output coordinates of width $w_N$
  with

  

$$
Nw_N\longrightarrow\infty, \tag{7}
$$



  then this theorem produces integer profiles with reduced output denominator
  $D_N=o(N)$.  The positive integral argument would then prove that
  $e+\pi$ is irrational.

* An interval of width merely $c/N$ does **not** force a rational of
  denominator $O(\sqrt N)$.  One-sided Farey gaps next to $1/2$ give an
  explicit counterexample.  Thus interval width without positional
  information cannot justify the proposed square-root-denominator step.

No family satisfying (7) is proved here.  In fact, the global native raw
output bounds place every sign output in an interval of width $O(1/N)$;
therefore $Nw_N\to\infty$ cannot occur within this native family.  The
conditional statement identifies a sufficient threshold for a more general
construction, not an expected native mechanism.  In particular, this note
does not prove that $e+\pi$ is irrational or transcendental.

## 2. The exact image of an integral moment

We first prove a general lemma.

**Moment-image lemma.**  If $V\in\mathbb Z[t]$ is nonzero, then



$$
{\cal H}_V:=
 \left\{\int_0^1V(t)P(t)\,dt:P\in\mathbb Z[t]\right\}
 =\mathbb Q.                                          \tag{8}
$$



Write $V(t)=\sum_{j=0}^dv_jt^j$.  Its monomial moments are



$$
r_n=\int_0^1V(t)t^n\,dt
 =\sum_{j=0}^d\frac{v_j}{n+j+1}
 =\frac{F(n)}{\prod_{j=0}^d(n+j+1)},                  \tag{9}
$$



where $F\in\mathbb Z[n]$, $\deg F\leq d$, and $F\ne0$.  The last
assertion follows either from the distinct partial-fraction poles or from the
fact that a nonzero polynomial cannot have every moment zero.

Fix a prime $p$.  Among the $d+1$ integers
$-1,-2,\ldots,-d-1$, at least one, say $-c$, is not a root of $F$.
For all sufficiently large $k$, take



$$
n_k=p^k-c\geq0.             \tag{10}
$$



Then



$$
v_p(F(n_k))=v_p(F(-c)),
$$



whereas the denominator in (9) contains $n_k+c=p^k$.  Hence



$$
v_p(r_{n_k})\longrightarrow-\infty.       \tag{11}
$$



Choose a nonzero $h\in{\cal H}_V$ and scale
${\cal G}={\cal H}_V/h$, so $1\in{\cal G}$.  Equation (11) says that,
for every prime $p$, the $p$-adic valuations in ${\cal G}$ are
unbounded below.  Given $k$, choose



$$
y=\frac{A}{p^rB}\in{\cal G},\qquad
 r\geq k,\qquad p\nmid AB.
$$



Multiplication by $Bp^{r-k}$ gives $A/p^k\in{\cal G}$.  Bezout applied
to $A$ and $p^k$, together with $1\in{\cal G}$, gives



$$
\frac1{p^k}\in{\cal G}.      \tag{12}
$$



For $m=\prod p_i^{k_i}$, the integers $m/p_i^{k_i}$ have gcd one.
Another Bezout identity applied to the elements $1/p_i^{k_i}$ gives
$1/m\in{\cal G}$.  Thus ${\cal G}=\mathbb Q$, and since
$h\mathbb Q=\mathbb Q$, equation (8) follows.

Apply the lemma to $V=4W$ to obtain (5), and to $V=4WB$ to obtain (6).
In particular, if



$$
B_0=t^4(1-t)^4,               \tag{13}
$$



then



$$
\ell(B_0\mathbb Z[t])=\mathbb Q.             \tag{14}
$$



## 3. Reduction to a zero-moment, zero-jet function

The ideals $(t^4)$ and $((t-1)^4)$ are comaximal in
$\mathbb Z[t]$.  One explicit identity is



$$
(-20t^3+70t^2-84t+35)t^4
 +(20t^3+10t^2+4t+1)(t-1)^4=1.                       \tag{15}
$$



Consequently (2) and the Chinese remainder theorem give
$H\in\mathbb Z[t]$ with exactly the endpoint jets (2).  Since
$\ell(f-H)\in\mathbb Q$, equation (14) gives
$R\in B_0\mathbb Z[t]$ satisfying



$$
\ell(R)=\ell(f-H).             \tag{16}
$$



Set



$$
P_0=H+R,\qquad g=f-P_0.        \tag{17}
$$



Then



$$
g^{(j)}(0)=g^{(j)}(1)=0\quad(0\leq j\leq3),
 \qquad \ell(g)=0.                                    \tag{18}
$$



It remains to approximate $g$ by integer polynomials with the properties
in (18) exactly.

## 4. An exact differential parametrization of the moment kernel

Let



$$
\nu=\operatorname {ord}_0W=
 \begin{cases}
 1,&a>0,\\
 2,&a=0
 \end{cases},
 \qquad r=5-\nu.                                      \tag{19}
$$



Thus $W=t^\nu w$, where $w$ is smooth and nonzero on $[0,1]$, and
$W(1)=a+b>0$.  Define



$$
J(t)=\int_0^tW(u)g(u)\,du,\qquad
 S(t)=\frac{J(t)}{W(t)^2}\quad(0<t\leq1).             \tag{20}
$$



The zero jets in (18) give $g=t^4\gamma_0$ near zero.  Therefore



$$
J=t^{\nu+5}j_0,\qquad
 S=t^{5-\nu}s_0=t^rs_0                               \tag{21}
$$



with smooth $j_0,s_0$.  At the other endpoint, $\ell(g)=0$ gives
$J(1)=0$, and $g=(1-t)^4\gamma_1$ gives



$$
S=(1-t)^5s_1                 \tag{22}
$$



with smooth $s_1$.  Thus (20) extends to a smooth function on the closed
interval.

Differentiating $W^2S=J$ gives the exact first-order identity



$$
\boxed{{\cal D}S:=2W'S+WS'=g.}                       \tag{23}
$$



For every polynomial $U$,



$$
\boxed{\ell({\cal D}U)
 =4\int_0^1(W^2U)'\,dt
 =4[W^2U]_0^1.}                                      \tag{24}
$$



This is the mechanism that will preserve the moment exactly.

## 5. Weighted integer Bernstein approximation

For $n\geq1$, let



$$
z_{n,k}=
 \left\langle S(k/n){n\choose k}\right\rangle,\qquad
 S_n(t)=\sum_{k=0}^nz_{n,k}t^k(1-t)^{n-k}\in\mathbb Z[t],             \tag{25}
$$



where brackets denote a nearest integer.  Equations (21)--(22) imply, for
all sufficiently large $n$,



$$
z_{n,k}=0\quad(0\leq k<r),\qquad
 z_{n,k}=0\quad(n-4\leq k\leq n).                     \tag{26}
$$



Indeed, for fixed $k<r$,



$$
S(k/n){n\choose k}=O(n^{k-r})\longrightarrow0,
$$



and the right-end estimate is the same with order five.  Hence



$$
t^r(1-t)^5\mid S_n.           \tag{27}
$$



Let $B_nS$ be the ordinary Bernstein polynomial and put



$$
E_n^{\rm rnd}=S_n-B_nS
 =\sum_ke_{n,k}t^k(1-t)^{n-k},\qquad |e_{n,k}|\leq\frac12.            \tag{28}
$$



Split this error into the centrally rounded part



$$
R_n=\sum_{r\leq k\leq n-5}
 e_{n,k}t^k(1-t)^{n-k}
$$



and the finitely many omitted endpoint channels.  The support of $R_n$
is contained in $r\leq k\leq n-5$.
For integers $j,\lambda\geq0$, differentiating the raw Bernstein channels
and normalizing the resulting nonnegative Bernstein basis gives



$$
\begin{aligned}
 \|t^\lambda R_n^{(j)}\|_\infty
 \leq{}&
 \frac{(n)_j}{2(n-j+1)_\lambda}
 \sum_{\alpha=0}^j{j\choose\alpha}\\
 &\mathrel{\phantom{\leq}}
 \times
 \max_{r\leq k\leq n-5}
 \frac{(k-\alpha+1)_\lambda}{{n\choose k}}.            \tag{29}
\end{aligned}
$$



Terms with an invalid falling factorial are simply absent.  Here
$(x)_j$ in the prefactor is falling, while
$(k-\alpha+1)_\lambda$ and $(n-j+1)_\lambda$ in the ratio are rising.
The identity behind (29) is



$$
\frac{(k)_\alpha(n-k)_{j-\alpha}}
 {{n-j\choose k-\alpha}}
 =\frac{(n)_j}{{n\choose k}},                         \tag{30}
$$



together with



$$
\frac{{n-j\choose k-\alpha}}
 {{n-j+\lambda\choose k-\alpha+\lambda}}
 =
 \frac{(k-\alpha+1)_\lambda}{(n-j+1)_\lambda}.         \tag{31}
$$



The endpoint ratios in (29) now give all the decay that is needed.
When $\nu=1$, so $r=4$,



$$
\|(E_n^{\rm rnd})^{(j)}\|_\infty=O(n^{j-4})
 \quad(0\leq j\leq3),\qquad
 \|t(E_n^{\rm rnd})^{(4)}\|_\infty=O(n^{-1}).          \tag{32}
$$



When $\nu=2$, so $r=3$,



$$
\begin{aligned}
 \|(E_n^{\rm rnd})^{(j)}\|_\infty&=O(n^{j-3})
 &&(0\leq j\leq2),\\
 \|t(E_n^{\rm rnd})^{(3)}\|_\infty&=O(n^{-1}),&
 \|t^2(E_n^{\rm rnd})^{(4)}\|_\infty&=O(n^{-1}).       \tag{33}
\end{aligned}
$$



For example, the only new endpoint ratios are



$$
\begin{array}{c|c}
4\leq k\leq n-5&
\displaystyle\frac{k+1}{{n\choose k}}=O(n^{-4})\\[2mm]
3\leq k\leq n-5&
\displaystyle\frac{k+1}{{n\choose k}}=O(n^{-3}),\quad
\displaystyle\frac{(k+1)(k+2)}{{n\choose k}}=O(n^{-3}).
\end{array}                                           \tag{34}
$$



Each maximum occurs at one of the two indicated endpoints, as follows
directly by taking the ratio of consecutive terms.

The omitted endpoint channels obey the same estimates.  On the left their
classical coefficients are $O(n^{k-r})$ for $k<r$; after $j$
derivatives and multiplication by $t^\lambda$, direct rescaling
$t=y/n$ gives $O(n^{j-r-\lambda})$.  On the right, writing
$k=n-h$ with $h<5$, the coefficient is $O(n^{h-5})$, and rescaling
$1-t=y/n$ gives $O(n^{j-5})$.  Thus adding these finitely many channels
does not change (32)--(33).

Because $S$ is smooth, the classical Bernstein polynomials converge to
$S$ simultaneously through the fourth derivative.  Combining this fact
with (32)--(33), and writing $E_n=S_n-S$, gives:



$$
\begin{array}{ll}
\nu=1:&
 E_n,\ldots,E_n^{(3)}\to0,\quad tE_n^{(4)}\to0,\\[1mm]
\nu=2:&
 E_n,\ldots,E_n^{(2)}\to0,\quad
 tE_n^{(3)}\to0,\quad t^2E_n^{(4)}\to0,
\end{array}                                           \tag{35}
$$



uniformly on $[0,1]$.

## 6. Completion of exact-moment approximation

Put



$$
G_n={\cal D}S_n=2W'S_n+WS_n'. \tag{36}
$$



This is an integer polynomial.  By (19) and (27),



$$
t^4(1-t)^4\mid G_n,           \tag{37}
$$



so its endpoint jets through order three vanish exactly.  Also
$S_n(1)=0$, $W(0)=0$, and (24) give



$$
\ell(G_n)=0.                 \tag{38}
$$



Finally, three differentiations give



$$
\begin{aligned}
 \{{\cal D}E_n\}'''
 ={}&2W''''E_n+7W'''E_n'+9W''E_n''\\
 &+5W'E_n'''+WE_n''''.                                \tag{39}
\end{aligned}
$$



When $\nu=1$, $W=t\,w$, so (35) controls the last term and all preceding
terms directly.  When $\nu=2$, $W=t^2w$ and $W'=t\,w_1$, so the second
line of (35) controls the last two terms; the first three use only derivatives
through order two.  Lower derivatives are easier.  Hence



$$
\|G_n-g\|_{C^3[0,1]}
 =\|{\cal D}(S_n-S)\|_{C^3[0,1]}\longrightarrow0.      \tag{40}
$$



Set



$$
P_n=P_0+G_n.                 \tag{41}
$$



Equations (17)--(18), (37)--(40) prove (3)--(4).

## 7. What an output interval would and would not prove

Every open interval of length $w>0$ contains a rational $c/D$ with



$$
1\leq D\leq\lfloor1/w\rfloor+1.              \tag{42}
$$



Indeed, take $D=\lfloor1/w\rfloor+1$; the grid $D^{-1}\mathbb Z$ has
spacing strictly smaller than $w$.

Suppose a strict, $C^3$-stable real sign family at index $N$ sweeps an
output-coordinate interval of width $w_N$.  Choose the rational coordinate
in (42), apply the exact-moment theorem to the corresponding real profile,
and take a sufficiently accurate integer approximant.  Strict sign control
survives, and its rational coordinate is unchanged.  After reduction its
denominator is at most the $D$ in (42).

If $e+\pi=u/v$ were rational, then $v\mid N!$ for all sufficiently large
$N$.  For the positive common-kernel integral



$$
L_{N,h}=N!(e+\pi)+\frac cD,\qquad
 0<L_{N,h}\leq\frac{5e}{N+1},                         \tag{43}
$$



the number $DL_{N,h}$ would be a positive integer.  Under (7), equation
(42) gives $D=o(N)$, so (43) would give $0<DL_{N,h}<1$, a contradiction.
This proves the conditional irrationality statement in Section 1.

The square-root-denominator inference requires much more.  Let
$Q=\lfloor C\sqrt N\rfloor$.  Every reduced rational $p/q>1/2$ with
$q\leq Q$ satisfies



$$
\frac pq-\frac12=\frac{2p-q}{2q}\geq\frac1{2Q}.       \tag{44}
$$



Consequently, for any fixed $c,C>0$ and all sufficiently large $N$, an
interval of length $c/N$ placed immediately to the right of $1/2$, while
excluding $1/2$, contains no rational with denominator at most
$C\sqrt N$.  More generally, a width $o(N^{-1/2})$ can hide in this
one-sided Farey gap.  Thus a width bound of order $1/N$, even with a fixed
positive constant, does not force $D=O(\sqrt N)$.

If $Nw_N\to\infty$, the elementary grid bound (42) already yields the
weaker but sufficient conclusion $D=o(N)$; no square-root Farey theorem is
needed.  If only $w_N\geq c/N$ is known, additional positional information,
a large enough explicit constant, or a genuinely stronger width estimate is
required.

For the native family, (43), together with the corresponding positive lower
bound, places all possible output coordinates in a total interval of length
at most $O(1/N)$ (indeed at most $5e/(N+1)$ already from the displayed
upper bound and positivity).  Hence the hypothesis $Nw_N\to\infty$ is
globally unavailable here.  The moment-preservation theorem removes the
integer-approximation obstruction, but it does not remove this analytic
width/Farey obstruction.

## 8. Scope and replay

The all-parameter results are:

* the moment-image lemma (8);
* the exact-moment integer $C^3$ approximation theorem (4);
* the conditional irrationality implication from $Nw_N\to\infty$;
* the explicit Farey-gap obstruction (44).

The theorem is qualitative in degree and height.  It neither supplies an
interval satisfying (7)—which the native global $O(1/N)$ range actually
precludes—nor improves primitive-content estimates for a single profile.
Finite symbolic checks are used only to replay algebra and the weighted
Bernstein identities, never to extrapolate an approximation or
number-theoretic claim.

From the research directory run

    python3 scripts/common_kernel_native_exact_moment_integer_approximation_certificate.py

The deterministic replay uses exact symbolic and rational CPU arithmetic.
No hardware accelerator is useful, and the RAM guard is $40$ GiB.
