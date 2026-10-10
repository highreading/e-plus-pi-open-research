> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact fixed-index closure of native sign outputs

Checked: 2026-08-27 UTC.

## 1. Verdict

Fix an integer $N\geq2$ for which



$$
(1-i)^N=R_N+iI_N,\qquad
 a=-I_N\geq0,\qquad b=\frac{N!-R_N}{2}>0,\qquad A=a+b. \tag{1}
$$



Put



$$
w(t)=e^{-t}t^N,\qquad
 B_N=\int_0^1w(t)\,dt,\qquad
 J(t)=\int_t^1w(s)\,ds,\qquad
 \mu(t)=t(a+bt)e^{-t}.                                 \tag{2}
$$



For a strict native profile let



$$
G=\mu H,\qquad \nu=w+G',\qquad
 v=t^2-2t+2,\qquad q=\frac{H-1}{v^2},                 \tag{3}
$$



and require



$$
G(0)=G(1)=0,\qquad 0<G<\mu,\qquad \nu>0              \tag{4}
$$



on the open interval.  We additionally require $q\in C^\infty[0,1]$
and integral Taylor coefficients through order three at both endpoints.
The output is



$$
{\cal L}_N(G)=\int_0^1R(t)\nu(t)\,dt,\qquad
 R(t)=e+\frac{4e^t}{v(t)}.                            \tag{5}
$$



There is a unique $\tau_N\in(0,1)$ such that



$$
\boxed{\mu(\tau_N)=J(\tau_N).}                       \tag{6}
$$



Define



$$
E_N(t)=\min\{\mu(t),J(t)\},                           \tag{7}
$$





$$
{\cal L}^{\min}_N
 ={\cal L}_N(0)-\int_0^1R'(t)E_N(t)\,dt,\qquad
 {\cal L}^{0}_N={\cal L}_N(0).                        \tag{8}
$$



The exact fixed-$N$ result is



$$
\boxed{
 \left\{{\cal L}_N(G):G\text{ satisfies (3)--(4) and the integral jets}\right\}
 =({\cal L}^{\min}_N,{\cal L}^{0}_N).}                \tag{9}
$$



Consequently the closure is



$$
\boxed{[{\cal L}^{\min}_N,{\cal L}^{0}_N].}          \tag{10}
$$



Every interior value in (9) can be swept by an affine family of strict
profiles whose members have *identical endpoint germs*.  Thus imposing the
endpoint lattice does not shrink the closure.

This disproves the proposed fixed-index closure
$[(e+2)B_N,{\cal L}^{0}_N]$.  In fact,



$$
\boxed{{\cal L}^{\min}_N>(e+2)B_N}                   \tag{11}
$$



for every fixed admissible $N$.  The looser endpoint $(e+2)B_N$ is
approached only asymptotically as $N\to\infty$, which is why it gives the
correct sharp scaled diameter in the preceding package.

There are also two certified finite arithmetic scans.  They concern two
different denominators, which must not be conflated.  After translating by
$N!(e+\pi)$, the exact attainable **coordinate** interval is



$$
{\cal C}_N=(\alpha_N,\beta_N)
 :=({\cal L}^{\min}_N-N!(e+\pi),
    {\cal L}^{0}_N-N!(e+\pi)).                         \tag{12}
$$



An exact rational-interval replay first proves that, for every admissible


$$
N\in\{3,4,8,9,10,11,12,16,17,18,19,20\},             \tag{13}
$$


there is a reduced coordinate $\rho=c/D\in{\cal C}_N$ with


$$
D\leq\lfloor\sqrt{N!}\rfloor.                        \tag{14}
$$


For $N=2$, no integer lies in ${\cal C}_2$, so the bound $D\leq1$
produces no hit.

The denominator $D$ in (14) is **not** the denominator of the induced
rational approximant to $s=e+\pi$.  Since $(c,D)=1$, put



$$
g=\gcd(N!,|c|),\qquad
 -\frac{\rho}{N!}=-\frac{c/g}{N!D/g}=:\frac{P}{Q}.
                                                               \tag{14a}
$$



Thus the genuine reduced denominator is $Q=N!D/g$.  Every coordinate hit
in (13) has $Q>\lfloor\sqrt{N!}\rfloor$, as the exact table in Section 6
records.

Separately, the replay certifies genuine reduced approximants $P/Q$ in



$$
e+\pi-\frac{{\cal L}^{0}_N}{N!}
 <\frac PQ<
 e+\pi-\frac{{\cal L}^{\min}_N}{N!},\qquad
 Q\leq\lfloor\sqrt{N!}\rfloor                         \tag{14b}
$$



at the six finite indices



$$
N\in\{25,33,43,88,164,331\}.                         \tag{14c}
$$



These finite hits prove no irrationality or transcendence statement.  The
exact-moment theorem realizes the corresponding translated coordinate
$\rho=-N!P/Q$ qualitatively, but a rational-case contradiction requires an
unbounded sequence with a sufficiently small coordinate denominator, while a
Roth argument requires infinitely many distinct height-controlled
approximants with a strict exponent gain.  Neither follows from either finite
table.

## 2. The actual lower envelope

The sign inequality in (4) gives $G'>-w$.  Integrating from $t$ to $1$
and using $G(1)=0$ yields



$$
G(t)<J(t).                                             \tag{15}
$$



The range inequality gives $G(t)<\mu(t)$.  Hence every strict profile
satisfies



$$
0<G(t)<E_N(t).                                        \tag{16}
$$



Now $\mu$ is strictly increasing:



$$
\mu'(t)=e^{-t}\{a(1-t)+bt(2-t)\}>0\qquad(0<t<1),     \tag{17}
$$



whereas $J'=-w<0$.  Since



$$
\mu(0)=0<J(0)=B_N,\qquad \mu(1)=A/e>J(1)=0,          \tag{18}
$$



equation (6) has exactly one solution, and



$$
E_N(t)=
 \begin{cases}
  \mu(t),&0\leq t\leq\tau_N,\\
  J(t),&\tau_N\leq t\leq1.
 \end{cases}                                           \tag{19}
$$



Because



$$
R'(t)=\frac{4e^t(2-t)^2}{v(t)^2}>0,                  \tag{20}
$$



the affine identity



$$
{\cal L}_N(G)={\cal L}_N(0)-\int_0^1R'(t)G(t)\,dt    \tag{21}
$$



and (16) prove the strict inclusions in (9).

The endpoint in (8) has a useful density interpretation.  Away from the
single corner at $\tau_N$,



$$
\nu_*(t):=w(t)+E_N'(t)=
 \begin{cases}
  w(t)+\mu'(t),&0<t<\tau_N,\\
  0,&\tau_N<t<1.
 \end{cases}                                           \tag{22}
$$



It has total mass



$$
\int_0^{\tau_N}\{w+\mu'\}
 =B_N-J(\tau_N)+\mu(\tau_N)=B_N.                      \tag{23}
$$



Thus ${\cal L}^{\min}_N=\int R\nu_*$.  The density is positive on a
nonempty interval contained in $(0,1)$, while $R(t)>R(0)=e+2$ there.
This proves (11).

## 3. Integral-jet profiles approach the lower endpoint

It remains to prove that the endpoint restrictions create no additional
gap.  Define the flat function



$$
\psi(t)=
 \begin{cases}
  e^{-1/t},&t>0,\\
  0,&t=0.
 \end{cases}                                           \tag{24}
$$



For sufficiently small $\eta>0$, the left branch



$$
L_\eta(t)=\mu(t)\{1-\eta\psi(t)\}                     \tag{25}
$$



is strictly increasing and satisfies $0<L_\eta<\mu$ on $(0,1]$.
Indeed,



$$
L_\eta'=\mu'-\eta(\mu'\psi+\mu\psi'),                \tag{26}
$$



and the quotient
$(\mu'\psi+\mu\psi')/\mu'$ is bounded on $(0,1]$.  At zero this is
immediate when $a>0$; when $a=0$, the only extra term is asymptotic to
$e^{-1/t}/t$, which still tends to zero.

Let



$$
g_0=(A,b),\qquad \ell_0=\frac{A}{g_0},\qquad
 \ell_k=k\ell_0,\qquad
 \epsilon_k=\frac1{eA\ell_k},                         \tag{27}
$$



and use the decreasing right branch



$$
P_k(t)=\frac{J(t)^2}{J(t)+\epsilon_k}.                \tag{28}
$$



Its derivative satisfies



$$
P_k'=-\left(1-\frac{\epsilon_k^2}{(J+\epsilon_k)^2}\right)w,
 \qquad w+P_k'>0.                                      \tag{29}
$$



Moreover,



$$
0\leq J-P_k=\frac{J\epsilon_k}{J+\epsilon_k}
 \leq\epsilon_k,                                      \tag{30}
$$



so $P_k\to J$ uniformly.  The increasing branch $L_\eta$ and decreasing
branch $P_k$ have a unique transverse crossing.  Select $L_\eta$ before
the crossing and $P_k$ afterward.  In a small compact neighborhood of that
crossing only, this splice is their local minimum; regularize that local
minimum smoothly from below and leave the selected branches unchanged
outside the neighborhood.  Call the resulting strict smooth function
$G_{\eta,k,\delta}$, where the smoothing error is at most $\delta$.

At the left endpoint,



$$
H=1-\eta\psi,\qquad q=-\frac{\eta\psi}{v^2},          \tag{31}
$$



so every Taylor coefficient of $q$ at zero is zero.  At the right
endpoint, with $s=1-t$, direct series division gives



$$
q(1-s)
 =-1+(\ell_k+2)s^2+
 \left\{\ell_k(1-N)-A\ell_k^2+\frac{b\ell_k}{A}\right\}s^3
 +O(s^4).                                               \tag{32}
$$



The displayed coefficients are integers because $A\mid b\ell_k$.
Therefore $G_{\eta,k,\delta}$ has the required integral endpoint jets.

As $\eta\downarrow0$, $k\to\infty$, and then $\delta\downarrow0$,



$$
G_{\eta,k,\delta}\longrightarrow
 \min\{\mu,J\}=E_N                                    \tag{33}
$$



uniformly.  Equations (20)--(21) show that the corresponding outputs tend to
${\cal L}^{\min}_N$.

## 4. The same germs also approach the upper endpoint

Fix one profile $G=G_{\eta,k,\delta}$ from Section 3.  For sufficiently
small $r>0$, the raw cap



$$
\min\{G(t),r\}                                        \tag{34}
$$



equals $G$ in neighborhoods of both endpoints and equals the constant
$r$ on the middle of the interval.  It has exactly two corners, one where
the increasing endpoint branch reaches $r$, and one where the decreasing
endpoint branch falls below $r$.

Smooth each corner locally from below.  The smoothed derivative is a convex
combination of $G'$ and $0$, so $w+G'>0$ is preserved.  Choosing each
smoothing error below $r/2$ preserves positivity.  Denote the result by
$U_{G,r}$.  Then



$$
0<U_{G,r}\leq G<\min\{\mu,J\},\qquad
 \|U_{G,r}\|_\infty\leq r,                             \tag{35}
$$



and $U_{G,r}$ has exactly the same endpoint germs as $G$.  Hence



$$
{\cal L}_N(U_{G,r})\longrightarrow{\cal L}^{0}_N
 \qquad(r\downarrow0).                                \tag{36}
$$



Every convex combination



$$
G_\theta=(1-\theta)U_{G,r}+\theta G,\qquad 0\leq\theta\leq1, \tag{37}
$$



remains strict and has those same endpoint germs; its output depends
affinely on $\theta$.  Given any value strictly between the two endpoints
in (10), first choose $G$ close enough to $E_N$, then choose $r$ small
enough, and finally use (37).  This proves the reverse inclusion in (9).

## 5. Closed formulas for the translated coordinate

Put



$$
S_N(x)=\sum_{j=0}^N\frac{x^j}{j!},\qquad
 {\cal I}_r(x)=\int_0^x\frac{t^r}{v(t)}\,dt.           \tag{38}
$$



The incomplete-gamma identity is



$$
J(t)=N!\{e^{-t}S_N(t)-e^{-1}S_N(1)\}.                \tag{39}
$$



Thus $\tau_N$ is the unique root of



$$
t(a+bt)
 =N!\{S_N(t)-S_N(1)e^{t-1}\}.                         \tag{40}
$$



On the first branch in (22),



$$
e^t\nu_*(t)
 =t^N+a(1-t)+bt(2-t).                                 \tag{41}
$$



Since every admissible density has total mass $B_N$, equations
(5), (22), and (41) give



$$
\begin{aligned}
 {\cal L}^{\min}_N
 &=eB_N+4{\cal K}_N,\\
 {\cal K}_N
 &=\int_0^{\tau_N}
 \frac{t^N+a(1-t)+bt(2-t)}{v(t)}\,dt,\\
 {\cal L}^{0}_N
 &=eB_N+4{\cal I}_N(1).                               \tag{42}
 \end{aligned}
$$



Also



$$
eB_N=N!e-N!S_N(1).                                   \tag{43}
$$



Subtracting $N!(e+\pi)$ cancels the $e$-term exactly:



$$
\boxed{
 \begin{aligned}
 \alpha_N&=4{\cal K}_N-N!S_N(1)-N!\pi,\\
 \beta_N&=4{\cal I}_N(1)-N!S_N(1)-N!\pi.
 \end{aligned}}                                       \tag{44}
$$



Thus the scan does not numerically subtract two unrelated approximations to
$e$.  The identity $s=e+\pi$ is accounted for symbolically in (43)--(44);
only a rigorous enclosure of $\pi$, and rigorous exponential enclosures
for the root equation (40), remain.

## 6. Exact rational certificate

The certificate uses Python rational integers and fractions throughout.
For $0\leq x\leq1$, the positive Taylor series for $e^x$, with its
geometric ratio tail, gives a rational enclosure; reciprocation gives one
for $e^{-x}$.  Machin's identity



$$
\pi=16\arctan(1/5)-4\arctan(1/239)                   \tag{45}
$$



and alternating Taylor bounds give a rational enclosure of $\pi$.  The
replay then rounds this enclosure outward to a common denominator $10^{750}$;
this preserves rigor while preventing irrelevant growth of relatively-prime
intermediate denominators.

No numerical quadrature is used.  The exact expansion



$$
\frac1{t^2-2t+2}=\sum_{j\geq0}d_jt^j,\qquad
 (d_0,d_1,d_2,d_3)=\left(\frac12,\frac12,\frac14,0\right),
 \qquad d_{j+4}=-\frac14d_j                            \tag{46}
$$



gives



$$
{\cal I}_r(x)=
 \sum_{j\geq0}\frac{d_jx^{r+j+1}}{r+j+1}.             \tag{47}
$$



After $4M$ terms, the absolute tail is at most



$$
\frac{5\,4^{-M}x^{r+4M+1}}
 {4(r+4M+1)(1-x^4/4)}.                                \tag{48}
$$



Equations (40), (44), and (46)--(48) therefore certify rational brackets
for $\tau_N,\alpha_N,\beta_N$.

For each row in the translated-coordinate scan, the replay takes



$$
D_N^{\rm grid}=\lfloor\sqrt{N!}\rfloor,\qquad
 c_N=\lfloor D_N^{\rm grid}\alpha_N^{\,\mathrm{upper}}\rfloor+1
                                                               \tag{49}
$$



and proves exactly that



$$
\alpha_N<\frac{c_N}{D_N^{\rm grid}}<\beta_N.         \tag{50}
$$



It then reduces this coordinate to $c/D$, computes



$$
g=\gcd(N!,|c|),\qquad Q=\frac{N!D}{g},               \tag{50a}
$$



and checks the genuine denominator separately.  The reduced certified
coordinate hits are:

| $N$ | coordinate $c$ | $D$ | $g$ | induced $Q=N!D/g$ |
|---:|---:|---:|---:|---:|
| 3 | $-69$ | $2$ | 3 | 4 |
| 4 | $-140$ | $1$ | 4 | 6 |
| 8 | $-5906748$ | $25$ | 12 | 84000 |
| 9 | $-640055749$ | $301$ | 1 | 109226880 |
| 10 | $-2381602983$ | $112$ | 3 | 135475200 |
| 11 | $-1477593283119$ | $6317$ | 3 | 84051475200 |
| 12 | $-30715789090729$ | $10943$ | 1 | 5241714508800 |
| 16 | $-560812448284037422057$ | $4574143$ | 13 | 7361833300512768000 |
| 17 | $-39308917046903583982636$ | $18859677$ | 4 | 1677037501712821248000 |
| 18 | $-3001925032973772105117101$ | $80014834$ | 1 | 512284869269790769152000 |
| 19 | $-1942317731845540057175773$ | $2724817$ | 1 | 331460637560692383744000 |
| 20 | $-11118475490457748990831310395$ | $779888134$ | 5 | 379478281472346502397952000 |

Every $Q$ in this table is strictly larger than
$\lfloor\sqrt{N!}\rfloor$.

The second scan starts instead with a proposed genuine reduced fraction
$P/Q$, checks $Q\leq\lfloor\sqrt{N!}\rfloor$, sets
$\rho=-N!P/Q$, and certifies $\alpha_N<\rho<\beta_N$.  The three shorter
candidates are



$$
\begin{array}{c|c}
 N&P/Q\\ \hline
 25&18641173568782/3181155778317\\
 33&15543960449313264573/2652609795129689462\\
 43&312765117341153549666363298/53374030160420566409591105.
 \end{array}                                          \tag{50b}
$$



For all six rows, including the much longer exact integers at
$N=88,164,331$, the JSON stores $P,Q$,
$\lfloor\sqrt{N!}\rfloor$, exact SHA-256 digests of both rational margins,
and the SHA-256 digest of the literal string `P/Q`.  Compact identifiers and
certified lower bounds for the two coordinate margins are:

| $N$ | digits $(P,Q)$ | SHA-256(`P/Q`) | left margin | right margin |
|---:|---:|:---|---:|---:|
| 25 | (14,13) | `655258675c37cc72...` | 0.0930918155 | 0.0309675128 |
| 33 | (20,19) | `12cabfdd442c4769...` | 0.0543185063 | 0.0408674709 |
| 43 | (27,26) | `b940e09d13ff3a61...` | 0.0176761238 | 0.0560439514 |
| 88 | (68,68) | `97abf7829b59474c...` | 0.0099591769 | 0.0266138538 |
| 164 | (148,147) | `cfced8915dc5b105...` | 0.0072851366 | 0.0124693696 |
| 331 | (347,346) | `1bdc2d153f7eed14...` | 0.0010620457 | 0.0087631140 |

These are exact rational statements, not decimal membership tests.

## 7. Why the finite hits do not settle $e+\pi$

For a realized reduced rational coordinate $c/D$, the positive form is



$$
0<{\cal L}_{N,h}=N!(e+\pi)+\frac cD=O(1/N).          \tag{51}
$$



If $e+\pi=u/v$ were rational, then $D{\cal L}_{N,h}$ would be a positive
integer only after $v\mid N!$.  A contradiction from (51) would then need
$D=o(N)$.  The bound $D\leq\sqrt{N!}$ is vastly weaker, and a finite list
cannot ensure the unknown divisibility $v\mid N!$.

For Roth, the relevant denominator is instead the genuine $Q=N!D/g$ in
(14a), or the explicitly listed $Q$ in the second scan.  Roth's theorem or
any transcendence measure needs infinitely many distinct approximants
together with an asymptotic height-versus-error inequality.  Six isolated
hits supply neither.  Finally, the exact-moment integer approximation theorem
is qualitative in the degree and coefficient height of the realizing
polynomial.  The rows above therefore certify real arithmetic flexibility at
fixed indices, not irrationality or transcendence of $e+\pi$.

## 8. Replay

From the research directory run

    python3 scripts/common_kernel_native_fixed_N_output_closure_certificate.py

The replay uses exact rational arithmetic for every theorem-facing
inequality.  Decimal strings in its JSON are outward-rounded renderings of
the exact rational brackets.  It uses no accelerator and has a 2 GiB RAM
cap.
