> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Quantitative audit of the native integer--Bernstein realization

Checked: 2026-08-27 UTC.

## 1. Verdict

This note quantifies the integer--Bernstein construction in
`common_kernel_native_sign_integer_bernstein_existence.md`.  It does not
change the sign-existence classification proved there.

Let



$$
(1-i)^N=R_N+iI_N,\qquad
 a=-I_N\geq0,\qquad b=\frac{N!-R_N}{2}>0,\qquad A=a+b,       \tag{1}
$$



and assume $N\geq2$ and $I_N\leq0$.  The first quantitative improvement
is that the right endpoint coefficient need not equal $A$.  Put



$$
g_0=(A,b),\qquad \ell=\frac{A}{g_0},\qquad
 \epsilon=\frac1{eA\ell}.                                  \tag{2}
$$



Then $A\mid b\ell$, and the right profile constructed below has integral
Taylor jets through order three.  In particular, if $a=0$, then
$\ell=1$, rather than $\ell=A$.

For one explicit one-sided smoothing of the crossing, let $q_N$ denote the
smooth target profile and let $P_N\in\mathbb Z[t]$ be the explicit Hermite
polynomial in Section 4.  Set



$$
r_N=q_N-P_N,qquad
 M_{j,N}=\lVert r_N^{(j)}\rVert_\infty\quad(3\leq j\leq5). \tag{3}
$$



Section 5 proves the following fully effective estimate for the nearest-
integer Bernstein polynomial:



$$
\boxed{
 \left\|\{\widehat B_n(r_N)\}'''-r_N'''\right\|_\infty
 \leq
 \frac{3M_{3,N}+\tfrac{57}{2}M_{4,N}+\tfrac14M_{5,N}}n
 +\frac{96}{n-3}.}                                      \tag{4}
$$



It holds whenever



$$
n\geq8,\qquad n>\frac98M_{4,N}.                         \tag{5}
$$



Under (5), the endpoint jets through order three agree *exactly*.  Thus the
same right side bounds the complete $C^3$ error, with the lower derivative
errors obtained by integration from an endpoint.

Section 6 gives an explicit positive sign tolerance $\eta_N$.  Therefore
every integer



$$
n\geq n_N^{\rm suff}:=
 \max\left\{
 N,10,
 \left\lfloor\frac98M_{4,N}\right\rfloor+1,
 \left\lceil
 \frac{3M_{3,N}+\tfrac{57}{2}M_{4,N}+\tfrac14M_{5,N}+192}
      {\eta_N}
 \right\rceil
 \right\}                                               \tag{6}
$$



produces a sign-controlled integer polynomial.  All quantities in (6) are
defined by explicit elementary functions and one finite integral.

The asymptotic size of this certified degree is



$$
\boxed{
 \log n_N^{\rm suff}
 \leq \frac N2\log A+O(N\log N)
 =\left(\frac12+o(1)\right)N^2\log N.}                  \tag{7}
$$



By contrast, every sign-controlled native polynomial, whether constructed by
Bernstein approximation or otherwise, obeys the previously proved lower
bound



$$
(\deg h)^4\geq\frac{(N!-R_N)(N+1)}{54e},               \tag{8}
$$



so only



$$
\log\deg h\geq
 \left(\frac14+o(1)\right)N\log N                       \tag{9}
$$



is forced.  Thus (7) is a rigorous sufficient-degree estimate for this
particular smoothed realization, not an estimate of the least possible
degree.  There is a factor of order $2N$ between the leading logarithmic
scales in (7) and (9).

The coefficient and rational-output bounds are also explicit.  If



$$
Q_{N,n}=P_N+\widehat B_n(r_N),\qquad
 h_{N,n}(x)=1+(1+x^2)^2Q_{N,n}(1-x),                    \tag{10}
$$



then



$$
\boxed{
 \log H(h_{N,n})\leq n\log6+O(N\log N),}                \tag{11}
$$



where $H$ is coefficient height.  The integral-coordinate denominator
satisfies the exact divisibility



$$
\boxed{D_{N,n}\mid\operatorname {lcm}(1,2,\ldots,n+5).} \tag{12}
$$



The variable coordinate is a sum of only four beta moments; see (71) below.
Nevertheless, neither (11), (12), nor the sign inequalities control the
reduced content



$$
g_{N,n}=\gcd(N!,c_{N,n}).                              \tag{13}
$$



Consequently this quantitative realization does **not** prove the Roth-scale
condition



$$
\frac{g_{N,n}}{D_{N,n}}\geq(N!)^{1/2+\delta}            \tag{14}
$$



on any subsequence, and it also does not prove that (14) is impossible.  The
precise surviving arithmetic problem is the gcd of the four-beta-moment
numerator in (71).  This note deliberately makes no congruence-selection
claim about that gcd.

## 2. The optimized right endpoint and the crossing scale

Put



$$
w(t)=e^{-t}t^N,\qquad
 J(t)=\int_t^1w(s)\,ds,\qquad
 \mu(t)=t(a+bt)e^{-t}.                                  \tag{15}
$$



With $\epsilon$ from (2), set



$$
\Phi(y)=\frac{y^2}{y+\epsilon},\qquad
 G_L(t)=\mu(t)(1-4t^2),\qquad
 G_R(t)=\Phi(J(t)).                                     \tag{16}
$$



As in the qualitative construction,



$$
G_L'>0\quad(0<t\leq1/4),\qquad
 G_R'=-\Phi'(J)w>-w,                                    \tag{17}
$$



and $G_L-G_R$ is strictly increasing on $[0,1/4]$.  Its unique zero in
that interval is denoted by $\tau$.

For $s=1-t$, direct series division gives



$$
\boxed{
 \frac{G_R(1-s)}{\mu(1-s)}
 =\ell s^2+
 \left\{\ell(1-N)-A\ell^2+\frac{b\ell}{A}\right\}s^3
 +O(s^4).}                                              \tag{18}
$$



The cubic coefficient is integral because $A\mid b\ell$.  This proves the
claim following (2).

We now record explicit lower scales at the crossing.  Define



$$
j_N=\frac{e^{-1}(1-4^{-(N+1)})}{N+1},\qquad
 \gamma_N=\Phi(j_N).                                    \tag{19}
$$



Since $J(1/4)\geq j_N$, monotonicity gives



$$
G_L(\tau)=G_R(\tau)\geq\gamma_N.                       \tag{20}
$$



Let $\theta_N>0$ be the positive solution of



$$
a\theta_N+b\theta_N^2=\frac{\gamma_N}{2};              \tag{21}
$$



equivalently,



$$
\boxed{
 \theta_N=
 \frac{\gamma_N}{a+\sqrt{a^2+2b\gamma_N}}.}            \tag{22}
$$



Because $\mu(t)\leq at+bt^2$, every point at which
$G_L(t)\geq\gamma_N/2$ has $t\geq\theta_N$.

The elementary bounds



$$
\gamma_N\asymp\frac1N,\qquad b\sim A\sim\frac{N!}{2},
 \qquad\frac{a^2}{b\gamma_N}\longrightarrow0           \tag{23}
$$



follow from $a\leq2^{N/2}$, $|R_N|\leq2^{N/2}$, and
$\epsilon\leq1/(eA)$.  Hence



$$
\theta_N\sim\sqrt{\frac{\gamma_N}{2b}},\qquad
 -\log\theta_N=\frac12\log A+O(\log N).                \tag{24}
$$



## 3. A quantitative one-sided smoothing

Fix the explicit nonnegative, even $C^\infty$ function



$$
\rho(u)=c_0
 \begin{cases}
 \exp\{-1/(1-u^2)\},&|u|<1,\\
 0,&|u|\geq1,
 \end{cases}
 \qquad
 c_0^{-1}=\int_{-1}^1\exp\{-1/(1-u^2)\}\,du .
$$



It is supported in $[-1,1]$ and has integral one.  Define



$$
\sigma_\delta(z)=\int_{-1}^1|z-\delta u|\rho(u)\,du.   \tag{25}
$$



Convexity, symmetry, and the support condition give



$$
\sigma_\delta\geq|z|,\qquad
 0\leq\sigma_\delta(z)-|z|\leq\delta,qquad
 |\sigma_\delta'|\leq1,                                \tag{26}
$$



and $\sigma_\delta(z)=|z|$ for $|z|\geq\delta$.  Moreover, for every
fixed $j\geq2$,



$$
\|\sigma_\delta^{(j)}\|_\infty
 =C_j\delta^{1-j},                                      \tag{27}
$$



where $C_j=\|\sigma_1^{(j)}\|_\infty$ is an absolute constant.

Write $d(t)=G_L(t)-G_R(t)$.  For $N\geq3$, take



$$
\delta_N=\frac{\gamma_N}{8}.                           \tag{28}
$$



Indeed, $-d(0)=G_R(0)\geq\gamma_N$.  For $N=3$, the estimates in the
qualitative proof give $d(1/4)>11/64$, while for $N\geq4$ they give a
still larger fixed lower bound.  Since $\gamma_N\leq1/(N+1)$, (28) is
strictly smaller than both endpoint gaps.  For the isolated case $N=2$,
replace (28) by



$$
\delta_2=\min\{\gamma_2/8,-d(0)/4,d(1/4)/4\}.          \tag{29}
$$



On $[0,1/4]$, define



$$
G(t)=\frac{G_L(t)+G_R(t)-\sigma_{\delta_N}(d(t))}{2},  \tag{30}
$$



and glue it to $G_L$ on the left and $G_R$ on the right wherever
$|d|\geq\delta_N$.  Equations (25)--(29) make this gluing $C^\infty$.
Unlike a two-sided uniform perturbation of the minimum, (26) gives the useful
one-sided fact



$$
\min(G_L,G_R)-\frac{\delta_N}{2}\leq G
 \leq\min(G_L,G_R).                                    \tag{31}
$$



Thus the upper barrier $G<\mu$ is automatic.  On the smoothing support,
the monotonicity of the two branches about their crossing gives



$$
\min(G_L,G_R)\geq G_L(\tau)-\delta_N
 \geq\gamma_N-\delta_N,                                \tag{32}
$$



and hence $G>0$.  Every point in this support satisfies
$t\geq\theta_N$ by (21)--(22).

Differentiating (30) gives a convex combination of $G_L'$ and $G_R'$.
On the smoothing support and on the whole right branch,



$$
\boxed{
 G'(t)+w(t)\geq
 \epsilon^2e^{-1}\theta_N^N=:\rho_N.}                  \tag{33}
$$



Indeed,



$$
G_R'+w=\frac{\epsilon^2}{(J+\epsilon)^2}w,
$$



and $J+\epsilon<1$, $t\geq\theta_N$.  The left branch has the larger
margin $G_L'+w>w$.

Set



$$
H=G/\mu,qquad v(t)=t^2-2t+2,qquad
 q_N(t)=\frac{H(t)-1}{v(t)^2}.                          \tag{34}
$$



The unchanged endpoint neighborhoods and (18) give



$$
q_N(t)=-t^2-2t^3+O(t^4)                               \tag{35}
$$



at zero, while, with



$$
C_N=\ell(1-N)-A\ell^2+\frac{b\ell}{A}\in\mathbb Z,    \tag{36}
$$



one has



$$
q_N(1-s)=-1+(\ell+2)s^2+C_Ns^3+O(s^4).                \tag{37}
$$



Therefore all endpoint Taylor coefficients through order three are integers.
Also $0\leq H\leq1$, so



$$
-1\leq q_N\leq0.              \tag{38}
$$



For later asymptotics, fixed-order differentiation of the explicit formulas
gives



$$
\boxed{
 1+\max_{0\leq j\leq5}\|q_N^{(j)}\|_\infty
 \leq C(1+A\ell)^C(N+1)^C}                             \tag{39}
$$



with an absolute effective constant $C$.  Here is a complete reason that
no hidden factorial scale occurs in (39).  On the smoothing support,
$\mu\geq G_L\geq7\gamma_N/8$.  On the right, $\mu$ only increases.  The
derivatives through order five of $J$ are bounded by a fixed polynomial in
$N$; the derivatives of $\Phi$ are bounded by a fixed polynomial in
$\epsilon^{-1}=eA\ell$; and (27)--(28) cost only a fixed polynomial in
$N$.  The left profile is $1-4t^2$.  Repeated product, quotient, and chain
rules now prove (39).  In particular,



$$
\log\left(1+\max_{j\leq5}\|q_N^{(j)}\|_\infty\right)
 =O(N\log N).                                           \tag{40}
$$



## 4. An explicit integral Hermite polynomial

Let



$$
\begin{aligned}
 E_0(t)&=(-20t^3+70t^2-84t+35)t^4,\\
 E_1(t)&=(20t^3+10t^2+4t+1)(t-1)^4.
 \end{aligned}                                         \tag{41}
$$



Then $E_0+E_1=1$, $E_0\equiv0\pmod {t^4}$, and
$E_1\equiv0\pmod{(t-1)^4}$.  Define the two endpoint Taylor polynomials



$$
T_0(t)=-t^2-2t^3,
 \qquad
 T_1(t)=-1+(\ell+2)(t-1)^2-C_N(t-1)^3                 \tag{42}
$$



and take



$$
P_N(t)=E_1(t)T_0(t)+E_0(t)T_1(t)\in\mathbb Z[t].      \tag{43}
$$



It has degree at most ten and matches the endpoint jets of $q_N$ through
order three.  Thus $r_N=q_N-P_N$ has zero endpoint jets through order
three.  A convenient explicit coefficient bound is



$$
\|P_N\|_1\leq
 \Pi_N:=1680+209\{1+4(\ell+2)+8|C_N|\}.                \tag{44}
$$



This follows from
$\|E_0\|_1=209$, $\|E_1\|_1\leq560$,
$\|T_0\|_1=3$, and
$\|T_1\|_1\leq1+4(\ell+2)+8|C_N|$.  In particular,



$$
\log(1+\Pi_N)=O(N\log N).                              \tag{45}
$$



Combining (39), (43), and (44) proves



$$
\log(1+M_{3,N}+M_{4,N}+M_{5,N})=O(N\log N).           \tag{46}
$$



## 5. An explicit $C^3$ nearest-Bernstein estimate

We prove (4), rather than importing the unspecified absolute constant in the
published modulus estimate.

**Lemma 5.1.**  Let $r\in C^5[0,1]$ and suppose



$$
r^{(j)}(0)=r^{(j)}(1)=0\qquad(0\leq j\leq3).           \tag{47}
$$



Write $M_j=\|r^{(j)}\|_\infty$ for $3\leq j\leq5$.

For



$$
\widehat B_n(r)(t)=\sum_{k=0}^n
 \left\langle r(k/n){n\choose k}\right\rangle
 t^k(1-t)^{n-k},                                       \tag{48}
$$



equations (4)--(5) hold, and the endpoint jets through order three of
$\widehat B_n(r)$ vanish exactly.

*Proof.*  Taylor's theorem gives, for $k=1,2,3$,



$$
|r(k/n)|\leq\frac{\|r^{(4)}\|_\infty}{24}(k/n)^4.     \tag{49}
$$



The largest of the products in (49) with ${n\choose k}$ is bounded by
$9\|r^{(4)}\|_\infty/(16n)$.  Thus (5) makes the first four rounded
scalars zero; reflection gives the same conclusion for the last four.

Write



$$
\widehat b_k=
 {n\choose k}^{-1}
 \left\langle r(k/n){n\choose k}\right\rangle .        \tag{50}
$$



For the endpoint positions handled by (49), and for the remaining interior
positions, respectively,



$$
\begin{aligned}
 |\widehat b_k-r(k/n)|
 &\leq \frac{27M_4}{8n^4}
 &&(k\in\{0,1,2,3,n-3,n-2,n-1,n\}),\\
 |\widehat b_k-r(k/n)|
 &\leq \frac1{2{n\choose k}}
 &&(4\leq k\leq n-4).
 \end{aligned}                                         \tag{51}
$$



The third derivative identity and the $\ell^1$-norm $8$ of a third
difference now imply, after splitting endpoint and interior contributions,



$$
\|\{\widehat B_n(r)-B_n(r)\}'''\|_\infty
 \leq\frac{27M_4}{n}+\frac{96}{n-3}.                   \tag{52}
$$



For the classical term, put
$\alpha_n=(n)_3/n^3$.  If $K$ is binomial with parameters
$(n-3,t)$, and $U_1,U_2,U_3$ are independent uniform variables on
$[0,1]$, then the integral formula for a third finite difference gives



$$
\{B_n(r)\}'''(t)=
 \alpha_n\,\mathbb E\,
 r'''\left(\frac{K+U_1+U_2+U_3}{n}\right).             \tag{53}
$$



The argument $X$ in (53) satisfies



$$
|\mathbb E(X-t)|\leq\frac{3}{2n},\qquad
 \mathbb E(X-t)^2\leq\frac1{2n}\quad(n\geq7).         \tag{54}
$$



Since $1-\alpha_n\leq3/n$, first-order Taylor expansion of $r'''$,
with the quadratic remainder bounded by $M_5/2$, gives



$$
\|\{B_n(r)\}'''-r'''\|_\infty
 \leq\frac{3M_3+\tfrac32M_4+\tfrac14M_5}{n}.          \tag{55}
$$



Equations (52) and (55) prove (4).  The vanishing of the first and last four
rounded scalars proves the endpoint assertion.  $\square$

This is a quantitative specialization of B. R. Draganov,
``Simultaneous approximation by Bernstein polynomials with integer
coefficients,'' *J. Approx. Theory* **237** (2019), 1--16,
Theorem 1.2 and Theorem 2.3,
https://doi.org/10.1016/j.jat.2018.08.003; preprint
https://arxiv.org/abs/1804.08248.  The theorem number is 1.2 in the published
preprint; the qualitative source's reference to Theorem 1.3 should be read as
the displayed simultaneous estimate, not as a distinct hypothesis.

## 6. A fully explicit sign tolerance and degree

Define a second elementary tail lower bound



$$
j_{1,N}=\frac{e^{-1}(1-2^{-(N+1)})}{N+1},\qquad
 \gamma_{1,N}=\Phi(j_{1,N}).                            \tag{56}
$$



Set



$$
\boxed{
 \eta_N=\min\left\{
 \frac14,
 \frac{\rho_N}{10A},
 \frac{\gamma_{1,N}}{4A},
 \frac{\theta_N^2\gamma_N}{4A},
 \frac{e^{-2}4^{-N}}{4A}
 \right\}.}                                            \tag{57}
$$



Suppose $E=Q-q_N$ has the same endpoint jets through order three and
$\|E'''\|_\infty\leq\eta_N$.  Integration from zero gives



$$
|E(t)|\leq\eta_Nt^3/6,qquad
 |E'(t)|\leq\eta_Nt^2/2.                               \tag{58}
$$



Integration from one gives the analogous two bounds with $t$ replaced by
$1-t$.  We use the former on the left and the latter at the right endpoint.

On the left branch, direct differentiation gives



$$
G_L'\geq e^{-1/4}
 \left(\frac a{16}+\frac{13bt}{16}\right).             \tag{59}
$$



Using $\mu\leq t(a+bt)$, $\mu'\leq a+2bt$, $v^2\leq4$, and
$|(v^2)'|\leq8$, equations (58)--(59) show that the residual perturbation
$|(\mu v^2E)'|$ is less than one half of $G_L'$ when
$\eta_N\leq1/4$.  The same estimates preserve $0\leq H+v^2E\leq1$
there.

On the smoothing support and the right branch,



$$
|(\mu v^2E)'|<5A\eta_N\leq\rho_N/2,                   \tag{60}
$$



so (33) preserves the residual sign.  Before $t=1/2$, the lower profile
margin is at least a fixed one of $\gamma_N$ and $\gamma_{1,N}$; the upper
margin is at least $3\theta_N^2\gamma_N$.  The middle two terms in (57)
preserve both inequalities.  Finally, for $t\geq1/2$, writing $s=1-t$
gives



$$
H(t)\geq
 \frac{e^{-2}4^{-N}s^2}{A(s+\epsilon)}.
$$



The last term in (57), together with (58), preserves positivity at the right
endpoint.  The upper margin only increases after the crossing.  Thus (57) is
a valid explicit $C^3$ sign-and-range tolerance.

For $n\geq6$, $96/(n-3)\leq192/n$.  Lemma 5.1 and (57) therefore prove
(6).

It remains to extract its scale.  From (2), (23)--(24), (33), and (57),



$$
-\log\eta_N
 =-\log\left(\frac{\rho_N}{10A}\right)+O(N\log N)
 =\frac N2\log A+O(N\log N).                           \tag{61a}
$$



Equations (46) and (61a) prove (7).

## 7. Coefficient height

Let $m_k=\langle r_N(k/n){n\choose k}\rangle$.  Since
$|r_N|\leq1+\Pi_N$,



$$
\begin{aligned}
 \|\widehat B_n(r_N)\|_1
 &\leq\sum_{k=0}^n|m_k|2^{n-k}\\
 &\leq(1+\Pi_N)3^n+2^n.                                \tag{61b}
 \end{aligned}
$$



Here coefficient $\ell^1$-norm is used, and the last $2^n$ is the total
nearest-rounding allowance.  Consequently



$$
\|Q_{N,n}\|_1
 \leq\Pi_N+(1+\Pi_N)3^n+2^n.                           \tag{62}
$$



Substitution $t=1-x$ costs at most $2^n$, and
$\|(1+x^2)^2\|_1=4$.  Hence



$$
\boxed{
 \|h_{N,n}\|_1\leq
 1+4\,2^n\{\Pi_N+(1+\Pi_N)3^n+2^n\}.}                 \tag{63}
$$



Equations (45) and (63) prove (11).

The global integer quotient



$$
\mathcal Q_{N,n}(x)=
 \frac{F_{N,h_{N,n}}(x)-N!}{1+x^2}\in\mathbb Z[x]     \tag{64}
$$



has the same exponential-height scale:



$$
\log H(\mathcal Q_{N,n})
 \leq n\log6+O(N\log N+\log n).                        \tag{65}
$$



For completeness, (65) follows without any height-preserving division
assumption.  If $U=(1+x^2)V$, the coefficient recurrence
$v_j=u_j-v_{j-2}$ gives
$\|V\|_1\leq(\deg V+1)\|U\|_1$.  Apply this to
${\cal T}((h-1)K_N)$, using
$\|K_N\|_1\leq2A$ and
$\|{\cal T}Y\|_1\leq(2\deg Y+1)\|Y\|_1$, and then add the fixed base
quotient.

## 8. The four-beta-moment coordinate

This section gives the exact arithmetic simplification.  Put



$$
u=1+x^2,\qquad
 K_N(x)=I_N-\frac{N!-R_N}{2}(1-x),qquad
 Y=u^2Q_{N,n}(1-x)K_N(x).                              \tag{66}
$$



Since ${\cal T}Y=(1-x)Y'-xY$, one integration by parts gives



$$
\boxed{
 \int_0^1\frac{{\cal T}Y}{u}\,dx
 =K_N(0)-\int_0^1Q_{N,n}(t)(a+bt)t(2-t)^2\,dt.}         \tag{67}
$$



The boundary term is $K_N(0)$ because $Q_{N,n}(1)=-1$; the factor
$(1-x)$ kills the other endpoint.  Formula (67) independently confirms the
sign and normalization of the root's four-moment reduction.

Write



$$
(a+bt)t(2-t)^2
 =4at+4(b-a)t^2+(a-4b)t^3+bt^4                       \tag{68}
$$



and put



$$
(c_1,c_2,c_3,c_4)=(4a,4(b-a),a-4b,b).                \tag{69}
$$



Let $Q_N^*\in\mathbb Z[x]$ be the fixed base quotient from the native
construction and set



$$
C_N^*=-N!-P_N^{(0)}(0)+4\int_0^1Q_N^*(x)\,dx+4K_N(0).
                                                                    \tag{70}
$$



Then the exact non-$e+\pi$ coordinate is



$$
\boxed{
 \frac{c_{N,n}}{D_{N,n}}
 =C_N^*-4\int_0^1P_N(t)(a+bt)t(2-t)^2\,dt
 -4\sum_{k=0}^nm_k\sum_{j=1}^4c_j
 \frac{(k+j)!(n-k)!}{(n+j+1)!}.}                       \tag{71}
$$



This is the promised four-beta-moment formula.  It is exact before any
reduction of the rational number.

Because $Q_{N,n}(t)(a+bt)t(2-t)^2$ is an integer polynomial of degree at
most $n+4$, while $\deg Q_N^*\leq N-2$ and $n\geq N$, equation (71)
proves (12).  Equivalently,



$$
\log D_{N,n}\leq\psi(n+5)
 =(1+o(1))n,                                            \tag{72}
$$



where $\psi(m)=\log\operatorname {lcm}(1,\ldots,m)$.  The elementary
Chebyshev bound also gives $\psi(m)\leq m\log4$.

The sign estimate for the raw form gives



$$
\frac1{N+1}\leq
 L_{N,n}=N!(e+\pi)+\frac{c_{N,n}}{D_{N,n}}
 \leq\frac{5e}{N+1}.                                   \tag{73}
$$



Thus



$$
|c_{N,n}|\leq D_{N,n}
 \left\{N!(e+\pi)+\frac{5e}{N+1}\right\},             \tag{74}
$$



and in particular



$$
\log|c_{N,n}|\leq\psi(n+5)+\log N!+O(1).              \tag{75}
$$



These are genuine denominator and numerator-height bounds, but they are
one-sided in the wrong direction for primitive normalization.

## 9. Roth ledger and exact remaining gap

After reduction, put



$$
g_{N,n}=\gcd(N!,c_{N,n}),\qquad
 q_{N,n}^{\rm rat}=\frac{N!D_{N,n}}{g_{N,n}}.           \tag{76}
$$



The exact approximation error is



$$
\frac1{(N+1)N!}\leq
 \left|(e+\pi)-\frac{p_{N,n}}{q_{N,n}^{\rm rat}}\right|
 \leq\frac{5e}{(N+1)N!}.                              \tag{77}
$$



As proved in the separate Roth criterion, a fixed $\delta>0$ and



$$
q_{N,n}^{\rm rat}\leq(N!)^{1/2-\delta}                \tag{78}
$$



for infinitely many $N$ would prove that $e+\pi$ is transcendental.
Equation (78) is exactly (14).

The present quantitative Bernstein analysis proves only



$$
D_{N,n}\mid\operatorname {lcm}(1,\ldots,n+5),\qquad
 g_{N,n}\leq N!.                                       \tag{79}
$$



It supplies neither a lower bound for $D_{N,n}$ nor a nontrivial upper or
lower bound for $g_{N,n}$.  In particular, (79) is compatible both with
complete cancellation $D_{N,n}=1, g_{N,n}=N!$ and with no useful
cancellation.  Coefficient height does not resolve this: (63)--(65) bound
the size of the integer forms, but a gcd is not bounded above by coefficient
height at the scale needed in (14).

Therefore the rigorous conclusion is narrowly scoped:

* the smoothed Bernstein realization is quantitatively effective;
* its certified sufficient degree is on the scale (7), far above the
  universal lower scale (9);
* its rational coordinate is exactly the four-moment expression (71);
* no Roth-scale subsequence, and no impossibility theorem for such a
  subsequence, follows without a new local-content theorem for (71).

This is an arithmetic gap, not a claim that $e+\pi$ is or is not
transcendental.

## 10. Replay

The deterministic certificate verifies the optimized endpoint series,
Hermite CRT identity and jets, the integration-by-parts sign in (67), the
four beta moments in (71), the coefficient-norm inequalities on exact test
polynomials, and the asymptotic scales for representative allowed residue
classes.

From the research directory run

    python3 scripts/common_kernel_integer_bernstein_quantitative_arithmetic_certificate.py

The replay uses exact symbolic/rational arithmetic apart from clearly marked
high-precision diagnostic evaluations of $\theta_N$ and $\rho_N$.  It uses
negligible RAM and no accelerator.
