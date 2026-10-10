> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Nonproportional classification for the small-root Rivoal forms

Checked: 2026-08-26 UTC

## Verdict

Retain the notation and the exact coefficientwise clearing
$q_N(c,d,f)$ of
`sources/small_root_of_unity_exp_log_continuation.md`.  Thus



$$
c,d,f\in\mathbb Z_{\geq0},\qquad d\geq2c,\qquad f\geq c,
 \tag{1}
$$





$$
\zeta_N=e^{2\pi i/N},\qquad \eta_N=1-\zeta_N,
 \qquad N\in\{3,4,6\},
 \tag{2}
$$



and $q_N$ is the least positive rational integer which clears the
coordinates of both coefficients of



$$
\Lambda_N(c,d,f)=U_N(e+\pi)+V_N
 \tag{3}
$$



in the integral basis of $\mathbb Q(i,\zeta_N)$.  In particular,
$q_N\geq1$.

The proportional-ray theorem in the preceding note extends to **every**
unbounded admissible sequence:



$$
\boxed{
\begin{aligned}
 q_3(c,d,f)|\Lambda_3(c,d,f)|&\longrightarrow\infty,\\
 q_4(c,d,f)|\Lambda_4(c,d,f)|&\longrightarrow\infty
\end{aligned}}
\tag{4}
$$



whenever $\max(c,d,f)\to\infty$.  At the neutral root,



$$
\boxed{
 \liminf_{\max(c,d,f)\to\infty}
 q_6(c,d,f)|\Lambda_6(c,d,f)|\geq \frac6{e^2}.
}
\tag{5}
$$



The meaning of (5) is sequential: it holds along every admissible sequence
on which the maximum tends to infinity.  The value $6/e^2$ is attained
as the unscaled limit on



$$
c=1,\qquad f=1,\qquad d\longrightarrow\infty,
 \tag{6}
$$



because $|\Lambda_6(1,d,1)|\to6/e^2$.  The other superficially dangerous
edge $c=f=0$ has $|\Lambda_6|\sim6e^{-2}/d$, but its exact clearing
satisfies $q_6\geq d^2/2$, as proved in the preceding note.

Thus there is no residual sparse nonproportional escape cone for these
three roots.  This is a theorem about the distinguished local form and its
exact coefficientwise denominator.  It does not control all conjugates of
$e+\pi$, and therefore does not prove algebraicity or transcendence.

## 1. Exact integral and a uniform form of the auxiliary polynomial

Put



$$
H_{d,f}(u)=\sum_{r=0}^d(-1)^r
 \binom{f+r}{f}\frac{u^r}{(d-r)!}.
 \tag{7}
$$



The two identities used below are



$$
A(1)=(-1)^cH_{d,f}(1)
 \tag{8}
$$



and



$$
R_{\log}(\eta_N)=(-1)^{c-1}\eta_N^{d+2c+1}
 \int_0^1
 \frac{u^c(1-u)^cH_{d,f}(u)}
 {(1-\eta_Nu)^{c+1}}\,du.
 \tag{9}
$$



Both were proved exactly in the preceding note.  For $d>0$, set



$$
\beta=\frac d{d+f}\in(0,1].
 \tag{10}
$$



Reversing the summation index in (7) gives



$$
H_{d,f}(u)=(-1)^d\binom{d+f}{d}u^dT_{d,f}(u),
 \tag{11}
$$



where



$$
T_{d,f}(u)=\sum_{q=0}^d
 \frac{(-1)^q}{q!u^q}
 \frac{d^{\underline q}}{(d+f)^{\underline q}}.
 \tag{12}
$$



The following uniformity in $f$, which is needed at the projective
edges, is slightly stronger than the fixed-ray statement.

**Lemma 1.**  On every compact set $K\subset\mathbb C\setminus\{0\}$,



$$
T_{d,f}(u)=e^{-\beta/u}\bigl(1+O_K(d^{-1})\bigr)
 \tag{13}
$$



as $d\to\infty$, uniformly for every integer $f\geq0$.
Consequently,



$$
A(1)=(-1)^{c+d}\binom{d+f}{d}e^{-\beta}
 \bigl(1+O(d^{-1})\bigr),
 \tag{14}
$$



uniformly in $c$ and $f$ (subject to (1)).

**Proof.**  Write



$$
R_q=\frac{d^{\underline q}}{(d+f)^{\underline q}}
 =\prod_{j=0}^{q-1}\frac{d-j}{d+f-j}.
$$



Every factor is between zero and $\beta$.  For $q\leq d/2$, a
telescoping product estimate gives



$$
|R_q-\beta^q|\leq C\frac{q^2}{d};
 \tag{15}
$$



the constant can be chosen independently of $f$.  Indeed,



$$
\beta-\frac{d-j}{d+f-j}
 =\frac{jf}{(d+f)(d+f-j)}
 \leq\frac{2j}{d}
$$



in that range, and the difference of two products of factors in
$[0,1]$ is at most the sum of the factor differences.  After division
by $q!|u|^q$, (15) is summable uniformly on $|u|\geq\delta>0$.
The tails $q>d/2$ of both the finite series and the exponential series
are smaller than the corresponding factorial tails.  Thus



$$
T_{d,f}(u)=\sum_{q=0}^{\infty}
 \frac{(-\beta/u)^q}{q!}+O_K(d^{-1}).
$$



The exponential is bounded away from zero on $K$, so the error may be
made relative.  Equation (14) follows from (8), (11), and $u=1$.
$\square$

The exact exponential remainder will always be negligible below.  We use



$$
0<|R_{\exp}(1)|\leq\frac e{(d+f+1)!}.
 \tag{16}
$$



A convenient uniform coefficient estimate from the accepted audit is



$$
|A(\eta_N)|\leq
 (c+d+1)|\eta_N|^{c+d}(c+1)(d+1)2^c
 \binom{d+2c}{c}\binom{d+f}{d},
 \tag{17}
$$



after harmlessly replacing $|\eta_N|^{c+d}$ by
$\max(1,|\eta_N|)^{c+d}$ if necessary.  Formulae (16)--(17), together
with the separate lower asymptotics for $A(1)$ and $R_{\log}$ proved
below, show uniformly in every growing regime that



$$
\frac{A(\eta_N)R_{\exp}(1)}
 {A(1)R_{\log}(\eta_N)}\longrightarrow0.
 \tag{18}
$$



Here is the uniform bookkeeping, stated explicitly to avoid using an
asymptotic for $\Lambda_N$ circularly.  Put
$B_{d,f}=\binom{d+f}{d}$.  We first evaluate $A(1)$ and
$R_{\log}$ separately, and only then make the following comparisons.

* If $c/d\geq\epsilon>0$, then $c\leq d/2$, and the compact-slope
  or $f$-dominant saddle estimates below give

  

$$
\log|A(1)R_{\log}(\eta_N)|=2\log B_{d,f}+O_{N,\epsilon}(d).
$$



  On the other hand, (17) gives
  $\log|A(\eta_N)|\leq\log B_{d,f}+O_N(d)$.  Hence the logarithm of
  the ratio in (18) is at most

  

$$
-\log((d+f+1)!)-\log B_{d,f}+O_{N,\epsilon}(d)
  \leq-d\log d+O_{N,\epsilon}(d).
$$



* If $c=o(d)$, the endpoint estimates (41) and (49), before they are
  inserted into $\Lambda_N$, give

  

$$
\begin{aligned}
  \log|A(1)R_{\log}(\eta_N)|={}&2\log B_{d,f}
  +(d+2c+1)\log|\eta_N|\\
  &+\log(c!)-(c+1)\log d-2\beta
  +O_N(1+c^2/d).
  \end{aligned}
$$



  Since $|\eta_N|\geq1$, (16)--(17) and the elementary bound
  $\log\binom{d+2c}{c}=O(c\log(d/c+2))$ show that the logarithm of
  the ratio in (18) is at most

  

$$
-\log((d+f+1)!)+
  O_N\!\left(c\log(d/c+2)+c+\log d+c^2/d\right).
$$



  The error is $o(d\log d)$, uniformly for $f\geq c$, whereas the
  first term is at most $-d\log d+O(d)$.

* If $d$ is fixed and $f\to\infty$, (17) is polynomial in $f$,
  (16) is factorially small, and the separate nonzero logarithmic
  estimates in Section 2 are polynomial (or have the nonzero limit (27)).

These three comparisons prove (18) without presupposing an asymptotic for
the sum $\Lambda_N$.  Thus all asymptotics for $\Lambda_N$ below come
from



$$
\Lambda_N\sim NA(1)R_{\log}(\eta_N).
 \tag{19}
$$



## 2. A fixed integral never vanishes

The boundary $d=O(1), f\to\infty$ requires a nonvanishing statement
which was left open in Section 8 of the preceding note.  Define



$$
I_{c,d,N}=\int_0^1
 \frac{u^{c+d}(1-u)^c}{(1-\eta_Nu)^{c+1}}\,du.
 \tag{20}
$$



**Lemma 2.**  For every admissible $c,d$ and
$N\in\{3,4,6\}$,



$$
I_{c,d,N}\ne0.
 \tag{21}
$$



**Proof.**  Euler's beta integral gives



$$
I_{c,d,N}=B(c+d+1,c+1)
 {}_2F_1(c+1,c+d+1;2c+d+2;\eta_N).
 \tag{22}
$$



Here is the exact zero theorem being used.  In the notation of
[DLMF 15.13](https://dlmf.nist.gov/15.13), let $N(a,b,C)$ denote the
number of zeros of the principal branch of ${}_2F_1(a,b;C;z)$ in



$$
|\operatorname{ph}(1-z)|<\pi.
$$



For real $a,b,C$, if



$$
a,b,C,C-a,C-b\notin\{0,-1,-2,\ldots\},\qquad
 b\geq a,\qquad C\geq a+b,
 \tag{23}
$$



then [DLMF 15.13.1](https://dlmf.nist.gov/15.13.E1), citing
Hans-J. Runckel, *On the zeros of the hypergeometric function*,
Math. Ann. **191** (1971), 53--58, gives



$$
N(a,b,C)=0\qquad(a>0).
 \tag{24}
$$



The non-strict inequality in (23) explicitly includes the zero-balanced
case $C=a+b$.  In (22), take



$$
a=c+1,\qquad b=c+d+1,\qquad C=2c+d+2=a+b.
$$



All five parameters in the exclusion in (23) are positive integers,
$b\geq a$, and $a>0$.  Moreover,



$$
1-\eta_N=\zeta_N,\qquad
 0<\arg\zeta_N=\frac{2\pi}{N}<\pi,
$$



so $z=\eta_N$ lies strictly in Runckel's cut domain.  Along Euler's
path,



$$
1-\eta_Nu=(1-u)+u\zeta_N
$$



is the chord from $1$ to $\zeta_N$; it is never zero and is on the
principal branch.  Finally, $B(c+d+1,c+1)>0$.  Thus neither the beta
prefactor nor a branch convention introduces a zero, and (21) follows.
$\square$

If $d$ is fixed, then (7) is a polynomial in $f$, uniformly for
$0\leq u\leq1$, with leading term



$$
H_{d,f}(u)=(-1)^d\frac{f^d}{d!}u^d+O(f^{d-1}).
 \tag{25}
$$



Equations (8)--(9), (20)--(21), and (25) imply, for fixed $c,d$ with
$d\geq1$,



$$
|A(1)R_{\log}(\eta_N)|
 =\frac{|\eta_N|^{d+2c+1}|I_{c,d,N}|}{(d!)^2}
 f^{2d}\bigl(1+O(f^{-1})\bigr).
 \tag{26}
$$



It therefore tends to infinity.  If $d=0$, admissibility forces
$c=0$.  In this case the coefficient formula and the two truncation
identities are especially simple:



$$
A(x)=1,\qquad B(x)=0,\qquad
 E_f(x)=S_f(x):=\sum_{n=0}^f\frac{x^n}{n!}.
$$



Consequently



$$
\Lambda_N(0,0,f)=2i\bigl(e+\pi-S_f(1)\bigr)
 \longrightarrow2\pi i.
 \tag{27}
$$



This raw limit is nonzero but does not by itself prove (4).  The exact
coefficientwise clearing does.  Since $U_N=2i$ and
$V_N=-2iS_f(1)$, one has, for every $N$,



$$
q_N(0,0,f)=\operatorname{den}\bigl(2S_f(1)\bigr),
$$



where $\operatorname{den}$ denotes the positive reduced denominator.
These denominators tend to infinity.  Indeed, the rationals $2S_f(1)$
are strictly increasing and remain in a fixed bounded interval, whereas
there are only finitely many rationals in that interval whose reduced
denominator is at most any prescribed $M$.  Hence



$$
q_N(0,0,f)|\Lambda_N(0,0,f)|\longrightarrow\infty.
 \tag{27a}
$$



Thus every fixed-$d$ sequence has the claimed cleared behavior.

## 3. Uniform compact-slope and $f$-dominant estimates

Suppose first that, for some fixed $\epsilon>0$ and $M<\infty$,



$$
d\to\infty,\qquad \frac cd\geq\epsilon,\qquad
 \frac fd\leq M.
 \tag{28}
$$



Then $c\to\infty$, and



$$
\lambda=\frac dc\in[2,\epsilon^{-1}],\qquad
 \mu=\frac fc\in[1,M/\epsilon]
$$



range in a compact subset of the admissible slope region.  The explicit
one-saddle contour and the endpoint estimates in the independent audit of
the preceding note are uniform on this compact set.  Hence its asymptotic
formula remains valid for moving $\lambda,\mu$, and the global rate
bound there gives



$$
\log|\Lambda_N(c,d,f)|\geq
 (1.64828\ldots+o(1))c.
 \tag{29}
$$



In particular, the form tends to infinity.

Now suppose



$$
d\to\infty,\qquad \frac cd\geq\epsilon,\qquad
 \frac fd\longrightarrow\infty.
 \tag{30}
$$



This edge needs a uniform estimate, rather than pointwise nonvanishing.
Put $\lambda=d/c$ and $\beta=d/(d+f)$.  The saddle phase and saddle
point are independent of $\beta$.  On the explicit lower contour from
the independent audit, Lemma 1 replaces the auxiliary factor by
$e^{-\beta/u}$.  Since



$$
\lambda\in[2,\epsilon^{-1}],\qquad \beta\in[0,1],
$$



the saddle is simple and separated from both endpoints and the pole,
uniformly; the amplitude



$$
\frac{\eta_Ne^{-\beta/u_*}}{1-\eta_Nu_*}
 \tag{31}
$$



is continuous and bounded away from zero.  The same one-saddle Gaussian
calculation therefore gives, uniformly in (30),



$$
\log|R_{\log}(\eta_N)|
 =\log\binom{d+f}{d}+c\chi_N(d/c)-\frac12\log c+O_{N,\epsilon}(1),
 \tag{32}
$$



and Lemma 1 at $u=1$ gives



$$
\log|A(1)|=\log\binom{d+f}{d}+O(1).
 \tag{33}
$$



The continuous function $\chi_N$ is bounded on
$[2,\epsilon^{-1}]$.  Since



$$
\binom{d+f}{d}=\prod_{j=1}^d\left(1+\frac fj\right)
 \geq\left(1+\frac fd\right)^d,
 \tag{34}
$$



equations (19), (32)--(34) give



$$
\log|\Lambda_N|
 \geq2d\log\left(1+\frac fd\right)-O_{N,\epsilon}(d)
 \longrightarrow\infty.
 \tag{35}
$$



This proves a genuinely uniform $f$-dominant bound; Lemma 2 alone would
not have sufficed for the moving-parameter problem.

## 4. Endpoint saddle when $c=o(d)$

This is the remaining projective edge.  The required estimate is as
follows.

**Lemma 3 (uniform endpoint saddle).**  If



$$
d\to\infty,\qquad c=o(d),\qquad f\geq c,
 \tag{36}
$$



then, uniformly in $f$,



$$
\boxed{
\begin{aligned}
 \log|\Lambda_N(c,d,f)|={}&
 \log N+2\log\binom{d+f}{d}
 +(d+2c+1)\log|\eta_N|\\
 &+\log(c!)-(c+1)\log d
 -\frac{2d}{d+f}
 +O_N\!\left(1+\frac{c^2}{d}\right).
\end{aligned}}
\tag{37}
$$



If $c$ remains bounded, the stronger uniform equivalent is



$$
\boxed{
 |\Lambda_N|=
 N\binom{d+f}{d}^{\!2}|\eta_N|^{d+2c+1}
 \frac{c!}{d^{c+1}}
 e^{-2d/(d+f)}\bigl(1+O_{N,c}(d^{-1})\bigr).
}
\tag{38}
$$



**Proof.**  After (11), write the integral in (9) as



$$
J_{N}(c,d,f)=\int_0^1
 \frac{u^{d+c}(1-u)^cT_{d,f}(u)}
 {(1-\eta_Nu)^{c+1}}\,du.
 \tag{39}
$$



For bounded $c$, put $t=d(1-u)$, split first at $u=1/2$, and
use Lemma 1 on the endpoint half.  There



$$
\begin{aligned}
 u^{d+c}&=e^{-t}\bigl(1+O_c((1+t)^2/d)\bigr),\\
 (1-u)^c\,du&=d^{-c-1}t^c\,dt,\\
 (1-\eta_Nu)^{-c-1}
 &=\zeta_N^{-c-1}\bigl(1+O_{N,c}(t/d)\bigr),\\
 T_{d,f}(u)&=e^{-\beta}
 \bigl(1+O_{N,c}((1+t)/d)\bigr).
\end{aligned}
\tag{40}
$$



The errors are dominated by a fixed polynomial times $e^{-t/2}$.
The part $u\leq1/2$, estimated from the truncated sum exactly as in
(45d)--(45e) below, is exponentially smaller; those estimates are uniform
in $f$ and do not use $c\to\infty$.  Since
$\int_0^\infty t^ce^{-t}\,dt=c!$,



$$
J_N(c,d,f)=
 \zeta_N^{-c-1}e^{-\beta}\frac{c!}{d^{c+1}}
 \bigl(1+O_{N,c}(d^{-1})\bigr),
 \tag{41}
$$



uniformly for $0\leq\beta\leq1$.

It remains to justify the logarithmic estimate when $c\to\infty$ and
$c/d\to0$.  Put $\lambda=d/c\to\infty$, and use the phase



$$
\psi_{N,\lambda}(u)=
 (\lambda+1)\operatorname{Log}u+
 \operatorname{Log}(1-u)-
 \operatorname{Log}(1-\eta_Nu).
 \tag{42}
$$



The branches are continued from $(0,1)$ along the lower contour.  Make
the Möbius change



$$
r=\frac{u}{1-u},\qquad u=\frac r{1+r}.
$$



The lower saddle is the image of



$$
r_*=\frac{\lambda+
 \sqrt{\lambda^2+4(\lambda+1)\overline{\zeta_N}}}{2}
 =Re^{i\theta},\qquad -\frac\pi N<\theta<0.
 \tag{43}
$$



Use the explicit ray $r=xe^{i\theta}$, $0<x<\infty$.  Rotating the
positive real ray to it crosses neither $r=-1$ nor the pole
$r=-\overline{\zeta_N}$.  Thus it is a legal deformation of (39).
Although (42) is written with logarithms, all powers in (39) are integral;
the continued logarithms merely record their phase on the deformed path.
The apparent pole of $T_{d,f}$ at $u=0$ is cancelled exactly by
$u^d$, as is clear from (12).  Hence neither a branch cut nor the
factorization creates an extra endpoint contribution.
The Descartes calculation in the independent audit applies for every
$\lambda\geq2$: on this ray the derivative of
$|e^{\psi_{N,\lambda}}|$ has exactly one positive zero, at $R$, and
changes from positive to negative.  Hence this is the unique contributing
saddle and its contour coefficient is one.

For completeness, the uniform endpoint nature of that saddle can be seen
without invoking a fixed-slope limit.  Expansion of (43) gives



$$
r_*=\lambda+\overline{\zeta_N}+O_N(\lambda^{-1}),
 \quad
 u_*=1-\lambda^{-1}+O_N(\lambda^{-2}),
 \quad
 \psi_{N,\lambda}''(u_*)=-\lambda^2
 \bigl(1+O_N(\lambda^{-1})\bigr).
 \tag{44}
$$



If the ray is scaled as $r=\lambda xe^{i\theta}$, then, uniformly on
compact subsets of $0<x<\infty$,



$$
\operatorname{Re}\psi_{N,\lambda}(u(r))+\log\lambda
 =-x^{-1}-\log x+O_N(\lambda^{-1}).
 \tag{45}
$$



The limiting function has its unique nondegenerate maximum at $x=1$.
To make the domination uniform also in the moving band $x\to0$, put
$\alpha=2\pi/N$ and choose positive constants



$$
\kappa_N=\cos(\pi/N),\qquad
 s_N=\min_{\phi\in[\pi/N,2\pi/N]}\sin\phi.
$$



Because $-\pi/N<\theta<0$, both constants apply on the saddle ray:
$\cos\theta\geq\kappa_N$ and
$\sin(\alpha+\theta)\geq s_N$.  The exact scaled phase is



$$
\begin{aligned}
 G_\lambda(x)
 &:={\rm Re}\,\psi_{N,\lambda}(u(\lambda xe^{i\theta}))+\log\lambda\\
 &=-(\lambda+1)\log\left|1+
       \frac{e^{-i\theta}}{\lambda x}\right|
   -\log|1+\zeta_N\lambda xe^{i\theta}|+\log\lambda.
\end{aligned}
 \tag{45a}
$$



Taking a real part in the first modulus and an imaginary part in the
second gives the global bound



$$
G_\lambda(x)\leq
 -(\lambda+1)\log\left(1+\frac{\kappa_N}{\lambda x}\right)
 -\log(s_Nx).
 \tag{45b}
$$



If $t=\lambda x\geq1$, then


$$
\log(1+\kappa_N/t)\geq
 \kappa_N/((1+\kappa_N)t)
$$

.  Hence, as $x\downarrow0$,



$$
G_\lambda(x)\leq-K_N/x+\log(1/x)+O_N(1)
 \tag{45c}
$$



for a fixed $K_N>0$.  If instead $1/3\leq t\leq1$, (45b) is at most
$-K_N'\lambda+O_N(\log\lambda)$.  Notice that
$|u|\geq1/2$ implies $t\geq1/3$, by
$2t\geq|1+r|\geq1-t$.  For large $x$, (45b) simply gives
$G_\lambda(x)\leq-\log(s_Nx)$.  Thus one can choose fixed
$0<a<1<b$, independently of $\lambda$, so that the part with
$|u|\geq1/2$ and $x\notin[a,b]$ has a fixed phase loss from the
saddle.  On $[a,b]$, (45) converges uniformly to



$$
h(x)=-x^{-1}-\log x,
$$



whose unique maximum is $h(1)=-1$, with $h''(1)=-1$.  It follows
that this compact part has a quadratic loss outside an
$O(c^{-1/2})$ neighborhood of the saddle.

It remains only to bound the genuine $u=0$ endpoint, where Lemma 1 is
not uniform.  From (12), because $0\leq R_q\leq1$,



$$
|u^dT_{d,f}(u)|
 \leq |u|^d\exp(1/|u|)\qquad(d^{-1}\leq|u|\leq1/2),
 \tag{45d}
$$



and the right side is at most $\exp(-d\log2+2)$.  For
$|u|\leq d^{-1}$, the finite sum gives



$$
|u^dT_{d,f}(u)|
 \leq\sum_{k=0}^d\frac{|u|^k}{(d-k)!}
 \leq\frac{d+1}{d!}.
 \tag{45e}
$$



On $|u|\leq1/2$, the remaining factor
$|u|^c|1-u|^c/|1-\eta_Nu|^{c+1}$ is at most $C_N^{c+1}$.  Moreover, on
the full saddle ray,



$$
\int |du|=\int_0^\infty
 \frac{\lambda\,dx}{|1+\lambda xe^{i\theta}|^2}
 \leq\int_0^\infty\frac{dt}{1+2\kappa_Nt+t^2}=O_N(1),
$$



because $\cos\theta\geq\kappa_N$.  The two endpoint bounds therefore
have logarithms $-\Omega_N(d)+O_N(c)$ and
$-d\log d+O_N(d+c)$, respectively.  By (44), the saddle logarithm is
$-c(1+\log\lambda)+O_N(c/\lambda+\log d)=-o(d)$.
Thus both endpoint pieces are uniformly negligible.  This proves the
required global majorant and excludes every endpoint contribution,
including the formerly uncovered moving transition band.

In the local coordinate
$x=R/\lambda+O(c^{-1/2})$, Taylor's theorem has uniformly bounded
normalized derivatives.  Lemma 1 supplies the nonzero amplitude



$$
\frac{e^{-\beta/u_*}}{1-\eta_Nu_*}
 =\frac{e^{-\beta}}{\zeta_N}
 \bigl(1+O_N(\lambda^{-1})\bigr),
 \tag{46}
$$



and the exact finite-series error is $O(d^{-1})$.  The local Gaussian
therefore has a nonzero leading coefficient.  No conjugate saddle lies on
the contour, so no second term can cancel it.  Taking the modulus of the
oriented Gaussian gives



$$
\begin{aligned}
 \log|J_N|={}&c\operatorname{Re}\psi_{N,\lambda}(u_*)
 -\beta\operatorname{Re}(u_*^{-1})
 -\log|1-\eta_Nu_*|\\
 &+\frac12\log\frac{2\pi}{c|\psi_{N,\lambda}''(u_*)|}
 +O_N(1).
\end{aligned}
\tag{47}
$$



The branch phase and tangent phase have disappeared only because (47) is
a modulus; neither coefficient is zero.  From (44),



$$
\begin{aligned}
 \operatorname{Re}\psi_{N,\lambda}(u_*)
 &=-1-\log\lambda+O_N(\lambda^{-1}),\\
 \log|\psi_{N,\lambda}''(u_*)|
 &=2\log\lambda+O_N(\lambda^{-1}),\\
 \operatorname{Re}(u_*^{-1})&=1+O_N(\lambda^{-1}),\\
 \log|1-\eta_Nu_*|&=O_N(\lambda^{-1}).
\end{aligned}
\tag{48}
$$



Substitution into (47), followed by Stirling's formula, yields



$$
\log|J_N|=
 \log(c!)-(c+1)\log d-\beta
 +O_N\!\left(1+\frac{c}{\lambda}\right)
 =\log(c!)-(c+1)\log d-\beta
 +O_N\!\left(1+\frac{c^2}{d}\right).
 \tag{49}
$$



Finally, (9), (11), (14), (18), and (49) prove (37); (14), (18), and
(41) prove (38).  $\square$

## 5. Consequences of the endpoint estimate

For $N=3,4$, respectively $|\eta_N|=\sqrt3,\sqrt2$.  From
$f\geq c$,



$$
\binom{d+f}{d}\geq\binom{d+c}{c}\geq\frac{d^c}{c!}.
 \tag{50}
$$



Thus the right side of (37) is bounded below by



$$
d\log|\eta_N|+(c-1)\log d-\log(c!)
 -O_N(1+c^2/d),
 \tag{51}
$$



which tends to infinity when $c=o(d)$.  This includes bounded $c$,
where (38) gives the sharper statement directly.

For $N=6$, $|\eta_6|=1$.  If $c\to\infty$ while $c=o(d)$,
(37) and (50) give



$$
\log|\Lambda_6|
 \geq(c-1)\log d-\log(c!)-O(1+c^2/d)
 \longrightarrow\infty.
 \tag{52}
$$



Indeed, the main lower bound is
$(c-1)\log(d/c)-\log c$, whereas
$c^2/d=o(c\log(d/c))$.

It remains only to list bounded $c$, for which (38) is uniform in
$f$.

* If $c=0,f=0$, then

  

$$
|\Lambda_6|\sim\frac6{e^2d},
$$



  but the exact result $q_6(0,d,0)\geq d^2/2$ gives
  $q_6|\Lambda_6|\to\infty$.

* If $c=0,f\geq1$, then
  $\binom{d+f}{d}\geq d+1$, and (38) tends to infinity.

* If $c=1,f=1$, then

  

$$
|\Lambda_6(1,d,1)|\longrightarrow\frac6{e^2}.
  \tag{53}
$$



* If $c=1,f\geq2$, then
  $\binom{d+f}{d}\geq\binom{d+2}{2}$, and (38) tends to infinity.

* For every fixed $c\geq2$, (50) and (38) give growth at least of
  order $d^{c-1}$.

Since $q_6\geq1$, (53) is the only finite asymptotic lower edge.

## 6. Exhaustion of every admissible sequence

Let an admissible sequence satisfy $\max(c,d,f)\to\infty$.  If $d$
is bounded, pass to a subsequence on which $c,d$ are fixed.  Then
$f\to\infty$, and Section 2 applies.

Suppose instead that $d\to\infty$.  Every subsequence has a further
subsequence of one of the following types.

1. $c/d\to0$.  Sections 4--5 apply.
2. $c/d\geq\epsilon>0$ and $f/d$ is bounded.  Section 3, equation
   (29), applies.
3. $c/d\geq\epsilon>0$ and $f/d\to\infty$.  Section 3, equation
   (35), applies.

For $N=3,4$, every case with $d\geq1$ tends to infinity already before
clearing, while the sole $d=0$ edge tends to infinity after the exact
clearing (27a).  For $N=6$, every case tends to infinity except (53),
which tends to $6/e^2$; the cleared $c=f=0$ edge and the $d=0$ edge
also tend to infinity.  The subsequence principle proves (4)--(5).

## 7. Scope and relation to finite diagnostics

The proof uses only:

* the exact continued remainder and Rodrigues reduction;
* the explicit one-saddle lower contour already independently audited;
* the uniform falling-factorial estimate in Lemma 1;
* Runckel's zero count with its boundary case $C=a+b$; and
* the exact denominator arguments on the two clearing-sensitive boundary
  edges.

Finite scans are useful cross-checks, but no finite scan is used to infer
(4) or (5).  The expanded exact scan archived as
`results/small_root_rivoal_exp_log_expanded_4096.json` contains $4096$
triples for each root,



$$
0\leq c\leq15,\qquad
 2c\leq d\leq2c+15,\qquad
 c\leq f\leq c+15.
$$



It finds no $q_N|\Lambda_N|<1$ for $N=2,3,4$, and again finds only
the isolated value $(N;c,d,f)=(6;0,3,0)$ for $N=6$.  This case, for
which $q_6|\Lambda_6|<1$, remains exactly as described in the preceding
note:
it is finite, it does not contradict the sequential limit (5), and its
off-diagonal cyclotomic values prevent the proposed norm contraction.

The independent numerical reconstruction in
*scripts/nonproportional_small_root_diagnostics.py*, archived in
*results/nonproportional_small_root_diagnostics.json*, evaluates (39)
without importing the earlier polynomial implementation.  Its endpoint
logarithmic residuals stay within $0.541$ on the deliberately mixed
test set (including $c=8,d=160,f=800$); its compact-slope
$f$-dominant residuals stay bounded while $f/d$ ranges up to $100$;
and its two Euler-integral quadratures agree to the recorded 90-decimal
working precision.  These are diagnostics only.  Runckel's theorem and the
contour estimates, not the observed residuals, prove the result.

Most importantly, (4)--(5) close only the local small-root Rivoal family.
They neither settle $e+\pi$ nor supply bounds for the uncontrolled
conjugates that would be needed under the temporary algebraicity
hypothesis.
