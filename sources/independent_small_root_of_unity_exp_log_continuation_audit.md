> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the small-root and boundary Rivoal continuation theorem

Checked: 2026-08-26 UTC

## Audited object and verdict

I audited sources/small_root_of_unity_exp_log_continuation.md as frozen at
SHA-256

7d29527a514c2a81619645e01d899d6c271864b02da9025609125410c431070c.

I independently reconstructed $A,B,E$ from the Rodrigues formula,
re-derived both continuations and all field clearings, supplied a global
contour and endpoint bounds for the complex saddle, checked the rate
minimization symbolically, and certified the complete finite scan using
rational intervals.

**Verdict: accepted with exactly the limitations stated in the source.**

- The continuation at $N=3,4,6$, the all-fixed-proportional-ray growth
  theorem, and the eventual nonvanishing theorem are correct.
- The $N=6$, $(c,d,f)=(0,3,0)$ local contraction and its adverse
  off-diagonal factors are correct.
- The $N=2$ Plemelj sign, choice of lip isolating $e+\pi$, and the
  all-index lower bound for every nonzero cleared value are correct.
- This is not an all-sequence theorem for $N=3,4,6$. Coupled degenerate
  ratios and exceptional sparse coordinate-denominator cancellation remain
  outside its scope.

The source's saddle paragraph stated the right contour geometry but did not
display its proof. Sections 4--6 below give an explicit lower contour, a
one-sign-change polynomial proving a unique maximum, endpoint suppression,
and the nonzero leading Gaussian coefficient. Thus the proportional-ray
theorem is independently closed rather than inferred from numerical data.

The independent certificate consists of

- scripts/independent_small_root_continuation_audit.py;
- results/independent_small_root_continuation_audit.json.

The script does not import the source implementation of the Rivoal
polynomials. All decisions involving $e,\pi,\sqrt3$ use exact rational
intervals.

## 1. Continuation and branches

Let $C=c+d$, $M=2c+d+1$, and
$A(x)=\sum_{m=0}^{C}a_mx^m$. Because $B$ is the truncation through
degree $C$ of $A(x)\log(1-x)$, while the Padé order is $M>C$, direct
tail summation gives, initially for $|x|<1$,



$$
R_{\log}(x)
=-x^M\int_0^1\frac{t^{M-1}A(1/t)}{1-xt}\,dt.
\tag{A1}
$$



The coefficient of $x^n$, $n\ge M$, on the right is
$-\sum_m a_m/(n-m)$, the logarithmic tail coefficient. Moreover,



$$
t^{M-1}A(1/t)=t^cP(t)
$$



is a polynomial. On compact subsets of
$\mathbb C\setminus[1,\infty)$, the denominator in (A1) is uniformly
separated from zero for $0\le t\le1$. The right side is holomorphic
there, and the identity theorem continues the principal logarithm
remainder to the slit plane.

For $N=3,4,6$, $\operatorname {Im}\eta_N<0$, so
$1-\eta_Nt\ne0$ on $[0,1]$. Also



$$
1-\eta_N=\zeta_N,\qquad
\operatorname {Arg}\zeta_N=\frac{2\pi}{N}\in(0,\pi).
$$



Thus the branch $\log\zeta_N=2\pi i/N$ and the ordinary real-path
continued integral are correct.

## 2. Rodrigues reconstruction and $A(1)$

With



$$
H_{d,f}(u)=\sum_{r=0}^{d}(-1)^r
\binom{f+r}{f}\frac{u^r}{(d-r)!},
$$



coefficient extraction gives



$$
P(u)=\frac1{c!}\frac{d^c}{du^c}
\bigl(u^c(1-u)^cH_{d,f}(u)\bigr).
\tag{A2}
$$



Insert (A2) in (A1), integrate by parts $c$ times, and use



$$
\frac{d^c}{du^c}\frac{u^c}{1-xu}
=\frac{c!}{(1-xu)^{c+1}}.
$$



All boundary terms vanish. This reproduces the source's exact continued
remainder, including the sign. At $u=1$, only the term in which all
$c$ derivatives hit $(1-u)^c$ survives:



$$
A(1)=P(1)=(-1)^cH_{d,f}(1).
\tag{A3}
$$



The sign assertion for $f\ge1$ follows from



$$
H_{d,f}(1)=\frac1{d!f!}\int_0^\infty y^f(1-y)^de^{-y}\,dy.
$$



For odd $d$, pair $y=1-t$ with $y=1+t$ for $0<t<1$. The magnitude
ratio of the negative term to the positive term is



$$
\left(\frac{1+t}{1-t}\right)^f e^{-2t}>1,
$$



because $f\ge1$ and
$\log((1+t)/(1-t))>2t$; the remaining $t>1$ part is negative.
Consequently
$\operatorname {sgn}H_{d,f}(1)=(-1)^d$, and $A(1)\ne0$ on every
proportional ray.

The independent implementation constructs $P$ by (A2), reverses it to
obtain $A$, and obtains $B,E$ only afterward by Taylor truncation.
This is independent of the double-sum implementation accompanying the
source.

## 3. Uniform interior asymptotic for $H$

Put $c=n,d=\lambda n,f=\mu n$, where $\lambda\ge2,\mu\ge1$ are fixed
rationals and $n$ runs through compatible integers. Replacing $r$ by
$d-q$ gives exactly



$$
H_{d,f}(u)=(-1)^d\binom{d+f}{d}u^d
\sum_{q=0}^{d}\frac{(-1)^q}{q!u^q}
\frac{d^{\underline q}}{(d+f)^{\underline q}}.
\tag{A4}
$$



For fixed $q$,



$$
\frac{d^{\underline q}}{(d+f)^{\underline q}}
=\left(\frac{\lambda}{\lambda+\mu}\right)^q
\left(1+O(q^2/n)\right).
$$



Every factor $(d-j)/(d+f-j)$ is no greater than $d/(d+f)$, so the
factorial $q!$ supplies a summable uniform majorant on compact sets
separated from $u=0$. Therefore



$$
H_{d,f}(u)=(-1)^d\binom{d+f}{d}u^d
\exp\!\left(-\frac{\lambda}{(\lambda+\mu)u}\right)
\left(1+O(n^{-1})\right)
\tag{A5}
$$



uniformly on every such compact set. At $u=1$, (A3)--(A5) reproduce the
source's asymptotic for $A(1)$.

## 4. Explicit lower contour and unique saddle

Write



$$
\alpha=\frac{2\pi}{N},\qquad
\zeta=e^{i\alpha},\qquad \eta=1-\zeta.
$$



After (A5), the exponential base in the logarithmic remainder is



$$
\Phi(u)=\eta^{\lambda+2}
\frac{u^{\lambda+1}(1-u)}{1-\eta u}.
\tag{A6}
$$



Make the real Möbius change



$$
r=\frac{u}{1-u},\qquad u=\frac{r}{1+r}.
$$



Then



$$
\Phi(u(r))=\eta^{\lambda+2}
\frac{r^{\lambda+1}}
{(1+r)^{\lambda+1}(1+\zeta r)}.
\tag{A7}
$$



The two non-endpoint critical points satisfy



$$
r^2-\lambda r-(\lambda+1)\bar\zeta=0.
\tag{A8}
$$



The root corresponding to the lower $u$-saddle is



$$
r_*=
\frac{\lambda+
\sqrt{\lambda^2+4(\lambda+1)e^{-i\alpha}}}{2}
=Re^{i\theta}.
\tag{A9}
$$



The radicand lies strictly in the sector
$-\alpha<\arg z<0$. Its principal square root lies in
$(-\alpha/2,0)$, and adding the positive real number $\lambda$
preserves that sector. Hence



$$
-\frac{\alpha}{2}<\theta<0.
\tag{A10}
$$



Take the explicit ray $r=te^{i\theta}$, $0<t<\infty$. Under the
Möbius map it is a circular arc from $u=0$ to $u=1$, lies in the
lower half-plane, and passes through $u_*$ when $t=R$. Rotating the
positive $r$-axis clockwise to this ray crosses neither $r=-1$ nor



$$
r=-\bar\zeta,
$$



the image of the pole $u=1/\eta$, whose argument is
$\pi-\alpha>0$. Thus this is a legal deformation.

Put



$$
a=\cos\theta,\qquad b=\cos(\theta+\alpha).
$$



Direct logarithmic differentiation of (A7) yields



$$
t\frac d{dt}\log|\Phi(u(te^{i\theta}))|
=\frac{P(t)}
{(1+2at+t^2)(1+2bt+t^2)},
\tag{A11}
$$



where



$$
\begin{aligned}
P(t)={}&(\lambda+1)
+\bigl((\lambda+1)a+(2\lambda+1)b\bigr)t\\
&+\lambda(1+2ab)t^2
+\bigl((\lambda-1)a-b\bigr)t^3-t^4.
\end{aligned}
\tag{A12}
$$



Every coefficient other than the leading $-1$ is strictly positive.

- For $N=4,6$, (A10) gives $a,b>0$. If $x=-\theta$, then
  $0<x<\alpha/2<\alpha-x<\pi$, so
  $a=\cos x>b=\cos(\alpha-x)$. The intermediate coefficients are
  positive.
- For $N=3$, $x=-\theta\in(0,\pi/3)$ and

  

$$
b=\cos(2\pi/3-x)
   =-\frac12\cos x+\frac{\sqrt3}{2}\sin x.
$$



  Hence the coefficient of $t$ is

  

$$
\frac12\cos x+
  (2\lambda+1)\frac{\sqrt3}{2}\sin x>0.
$$



  Also $b>-1/2$, so $1+2ab>0$, and $a>b$, so
  $(\lambda-1)a-b>0$.

Descartes' rule gives exactly one positive root of $P$. Equation (A8)
says $R$ is such a root. The critical point is simple because the
discriminant in (A9) has nonzero imaginary part. The derivative in (A11)
is positive near zero and negative at infinity, so $u_*$ is the unique
strict global maximum of $|\Phi|$ on the contour. The upper saddle is
not on this contour and has contour coefficient zero.

## 5. Endpoint suppression

Equation (A4) and the falling-factorial bound give, for $u\ne0$,



$$
|H_{d,f}(u)|
\le \binom{d+f}{d}|u|^d
\exp\!\left(\frac{d}{(d+f)|u|}\right).
\tag{A13}
$$



On $1/n\le|u|\le\varepsilon$, the two competing terms in the exponent
are



$$
(\lambda+1)n\log|u|
+\frac{\lambda}{(\lambda+\mu)|u|}.
$$



Their derivative is positive on that interval for large $n$, because



$$
\frac{\lambda}{(\lambda+\mu)(\lambda+1)}<1.
$$



The maximum is at the fixed $\varepsilon$. Choosing $\varepsilon$
small makes this endpoint rate strictly smaller than the saddle rate.

For $|u|\le1/n$, use the original sum and



$$
\binom{f+r}{r}\le\frac{(f+d)^r}{r!}.
$$



Then



$$
|H_{d,f}(u)|
\le\sum_{r=0}^{d}
\frac{(\lambda+\mu)^r}{r!(d-r)!}
=\frac{(1+\lambda+\mu)^d}{d!}.
\tag{A14}
$$



The exact remainder has the additional factor
$|u|^c\le n^{-n}$, so this disk contributes
$\exp(-\Omega(n\log n))$. Near $u=1$, (A5) is uniform and
$(1-u)^n$ suppresses a fixed endpoint neighborhood. The transition
pieces are controlled by (A13)--(A14). Neither endpoint contributes on
the saddle scale.

## 6. Leading coefficient, branch phase, and noncancellation

In a fixed neighborhood of $u_*$, the exact remainder and (A5) give



$$
(-1)^{c+d-1}\binom{d+f}{d}
\int_\Gamma e^{n\varphi(u)}
g(u)\left(1+O(n^{-1})\right)\,du,
\tag{A15}
$$



with



$$
g(u)=\frac{\eta}{1-\eta u}
\exp\!\left(-\frac{\lambda}{(\lambda+\mu)u}\right).
\tag{A16}
$$



The logarithms in $\varphi$ are continued along $\Gamma$. On every
compatible subsequence, all original powers are integral, so
$e^{n\varphi}$ is exactly the original integrand; no hidden branch
factor occurs.

Parameterize the contour locally as



$$
u=u_*+e^{i\beta}\tau+O(\tau^2),\qquad \tau\in\mathbb R.
$$



The unique strict maximum gives



$$
\operatorname {Re}
\left(\varphi''(u_*)e^{2i\beta}\right)<0.
$$



Taylor expansion and the convergent complex Gaussian integral yield



$$
e^{n\varphi(u_*)}g(u_*)e^{i\beta}
\sqrt{\frac{2\pi}
{-n\varphi''(u_*)e^{2i\beta}}}
\left(1+O(n^{-1})\right).
\tag{A17}
$$



The square-root branch is selected by the oriented contour. The
coefficient is nonzero: $g(u_*)\ne0$, the saddle is simple, and no
second saddle lies on the contour. After Gaussian rescaling, odd local
terms integrate to zero, giving the relative $O(n^{-1})$ correction.
Taking moduli in (A17) cancels the tangent factor and gives



$$
\left|
\frac{\eta e^{-\lambda/((\lambda+\mu)u_*)}}
{1-\eta u_*}
\right|
\sqrt{\frac{2\pi}{|\varphi''(u_*)|}},
$$



the source's $|K_{N,\lambda,\mu}|$.

The exact exponential remainder



$$
R_{\exp}(1)=
\frac{(-1)^c}{d!f!}
\int_0^1t^d(1-t)^fe^t\,dt
$$



is nonzero and has modulus at most $e/(d+f+1)!$. Since
$A(\eta)=\exp(O(n))$, the ratio of the exponential summand to the
nonzero logarithmic summand is



$$
\exp\bigl(-(\lambda+\mu)n\log n+O(n)\bigr).
$$



There is no cancellation. Combining the binomial factors from $A(1)$
and (A15) gives



$$
\lim_{n\to\infty}\frac1n\log|\Lambda_N|
=2\mathcal E(\lambda,\mu)+\chi_N(\lambda),
$$



and proves eventual nonvanishing.

## 7. Rate minimization

At the simple saddle, the envelope theorem gives



$$
\partial_\lambda\chi_N=\log|\eta_Nu_N|.
$$



The entropy derivatives are correct, so the rate is strictly increasing
in $\mu$, and it suffices to take $\mu=1$.

Put $w=\eta u$, $v=w/\sqrt\eta$, and
$v+v^{-1}=a+ib$. If $y=|v|^2<1$, writing
$v=\sqrt y e^{i\vartheta}$ gives



$$
\frac{a^2y}{(1+y)^2}
+\frac{b^2y}{(1-y)^2}=1.
\tag{A18}
$$



The left side is strictly increasing on $0<y<1$. Exact substitution at
$y=1/|\eta|$ gives



$$
1-\mathrm{LHS}=
\begin{cases}
(L-1)/L^2,&N=3,\\
(2L-5)/L^2,&N=4,
\end{cases}
\qquad L=\lambda+1\ge3.
$$



Thus $y>1/|\eta|$ whenever $y<1$; if $y\ge1$, the desired
$|\eta u|>1$ is immediate.

For $N=6$, the lower root has $|v|<1$. Indeed,
$\eta=e^{-i\pi/3}$, while (A10) and the Möbius map give
$\arg u_*\in(-\pi/6,0)$. Hence
$\arg v=\arg(\sqrt\eta\,u_*)\in(-\pi/3,-\pi/6)$. If
$v=re^{i\vartheta}$, the imaginary part of $v+v^{-1}$ is
$(r-r^{-1})\sin\vartheta$. It is positive, while
$\sin\vartheta<0$, so $r<1$. Moreover,



$$
v+v^{-1}=\sqrt3+\frac iL.
$$



Substitution of $y=(L-1)^4/L^4$ in (A18) gives the degree-14
polynomial in the source. The independent symbolic expansion reproduces
all 15 positive coefficients. Hence



$$
|u_6|>
\left(\frac{\lambda}{\lambda+1}\right)^2.
$$



The rate is strictly increasing in $\lambda,\mu$, so the global minimum
is at $(2,1)$. Exact rational boxes certify



$$
e^{\rho_3}\in
[60.4238249797683\ldots,60.4238249797684\ldots],
$$





$$
e^{\rho_4}\in
[23.0379256498678\ldots,23.0379256498679\ldots],
$$





$$
e^{\rho_6}\in
[5.19803354844985\ldots,5.19803354844986\ldots].
$$



Display logarithms reproduce the three source rates, including
$\rho_6=1.6482803903057923\ldots>0$. Positivity was decided by rational
intervals rather than floating-point signs.

## 8. Boundary regimes

For fixed $c,f$ and $d\to\infty$, (A4) near $u=1$ gives



$$
H_{d,f}(u)=
(-1)^d\frac{d^f}{f!}u^de^{-1/u}(1+o(1)).
$$



Thus $A(1)\sim(-1)^{c+d}d^f/(f!e)$. Watson's endpoint calculation gives



$$
\int_0^1
\frac{u^{c+d}(1-u)^ce^{-1/u}}
{(1-\eta u)^{c+1}}\,du
\sim
\frac{c!}{e}d^{-c-1}\zeta^{-(c+1)},
$$



reproducing the constants in the source's (54)--(55).

For $N=6,c=f=0$, reversal gives



$$
A(1)=(-1)^dD_d/d!,\qquad
A(\eta_6)=(-1)^dZ_d/d!.
$$



If $p\mid d$, the recurrences



$$
D_d=dD_{d-1}+(-1)^d,\qquad
Z_d=dZ_{d-1}+(-\eta_6)^d
$$



show that both numerators are units at every prime above $p$.
Integrality of $2qA(1)A(\eta_6)$ forces



$$
v_p(q)\ge2v_p(d!)-v_p(2),
$$



hence $q\ge d^2/2$. Since the unscaled form is asymptotic to
$6e^{-2}/d$, the cleared form diverges.

For fixed $c,d$ and $f\to\infty$,



$$
H_{d,f}(u)=
(-1)^d\frac{f^d}{d!}u^d+O(f^{d-1})
$$



uniformly. This gives the source's degree-$2d$ behavior unless the
fixed integral vanishes. These boundary calculations are not claimed to
cover every coupled sequence.

## 9. Fields, exact clearings, and the exceptional $N=6$ value

For $N=4$, the coefficient ring is $\mathbb Z[i]$. For $N=3,6$,
the discriminants of $\mathbb Q(i)$ and
$\mathbb Q(\sqrt{-3})$ are coprime, so



$$
\mathcal O_{\mathbb Q(i,\zeta_N)}
=\mathbb Z[i,\zeta_N]
$$



with integral basis $1,\zeta_N,i,i\zeta_N$. The lcm of reduced
coordinate denominators is exactly the least universal rational-integer
clearing. The independent reconstruction verifies in all $4\cdot441$
scan cases that it divides



$$
d!^2\operatorname {lcm}(\ell_{c+d},(f+2c)!).
$$



At $(c,d,f)=(1,2,1)$, it independently obtains



$$
q_2=1,\qquad q_3=4,\qquad q_4=1,\qquad q_6=2.
$$



Since the distinguished $\mathbb Q(s)$ is real,



$$
\mathbb Q(s)\cap\mathbb Q(i,\zeta_N)
\in\{\mathbb Q,\mathbb Q(\sqrt3)\}
\qquad(N=3,6).
$$



If the intersection is $\mathbb Q$, all four coefficient-field maps
extend while fixing $s$. If it is $\mathbb Q(\sqrt3)$, only
simultaneous conjugation fixes the intersection; an off-diagonal map must
be paired with an embedding of $\mathbb Q(s)$ sending $\sqrt3$ to
$-\sqrt3$, and involves an uncontrolled conjugate of $s$. No
linear-disjointness assumption is hidden.

For $(N;c,d,f)=(6;0,3,0)$, the independent reconstruction gives $q=9$
and



$$
|9\Lambda_6|^2
\in[0.42031091193926711988636706084064529\ldots,
      0.42031091193926711988636706084064530\ldots],
$$





$$
\text{off-diagonal pair}
\in[446.23062246798764836552894480469\ldots,
      446.23062246798764836552894480470\ldots],
$$





$$
\text{four-evaluation product}
\in[187.55559986474670839187068528964\ldots,
      187.55559986474670839187068528965\ldots].
$$



The exact product polynomial is



$$
169s^4-2028s^3+6093s^2-54s+81.
$$



The exceptional local contraction therefore cannot yield a product-formula
contradiction in either intersection case.

## 10. Aggressive $N=2$ audit

For $x=2-i\varepsilon$,



$$
1-(2-i\varepsilon)t=1-2t+i\varepsilon t.
$$



Sokhotski--Plemelj gives



$$
\lim_{\varepsilon\downarrow0}
\int_0^1\frac{h(t)}{1-(2-i\varepsilon)t}\,dt
=
\operatorname {PV}\int_0^1\frac{h(t)}{1-2t}\,dt
-\frac{i\pi}{2}h(1/2).
\tag{A19}
$$



Since $2^{M-1}h(1/2)=A(2)$, multiplication by the prefactor $-2^M$
in (A1) turns the last term into $+i\pi A(2)$. Therefore



$$
x=2-i0:\quad R_{\log}=+i\pi A(2)-B(2),
$$



whereas $x=2+i0$ gives $-i\pi A(2)-B(2)$. The first lip, and only it,
produces $2iA(1)A(2)(e+\pi)$. The source's sign, PV factor, jump, and
choice of lip are correct.

Let



$$
a=2qA(1)B(2),\quad
b=2qA(1)A(2),\quad
g=2qA(2)E(1)
$$



be the exactly cleared integers. Then



$$
q\Lambda_2^+=-a+i(bs-g).
\tag{A20}
$$



The cases are exhaustive, including $A(1)=0$, $A(2)=0$,
$B(2)=0$, and $a=b=0$.

- If $b=0$, (A20) is a Gaussian integer; when nonzero its modulus is at
  least one.
- If $a\ne0$, its real part is a nonzero integer, so its modulus is at
  least one.
- If $b\ne0,a=0$, then $A(1)A(2)\ne0$, $B(2)=0$, and

  

$$
|q\Lambda_2^+|
  =|b|\left|s-\frac{E(1)}{A(1)}\right|.
$$



Because $d!A(1)$ is a nonzero integer,



$$
\left|\frac{R_{\exp}(1)}{A(1)}\right|
\le\frac{e\,d!}{(d+f+1)!}.
$$



For $f\ge1$, this is at most $e/2<3/2$, and $\pi>3$ gives



$$
\left|\pi+\frac{R_{\exp}(1)}{A(1)}\right|>1.
$$



If $f=0$, admissibility forces $c=0$. The case $d=0$ is direct;
$d=1$ has $A(1)=0$; and $d\ge2$ gives the stronger bound
$e/(d+1)<1$. Hence every nonzero cleared boundary value has modulus at
least one. Multiplying by an integral clearing for algebraic $s$ cannot
reduce it, and the relative $\mathbb Q(i)$-norm is its square.

The independent script verifies the exact PV identity and clearing for all
441 stated $N=2$ scan cases.

## 11. Finite certificate, residual scope, and provenance

The scan covers



$$
0\le c\le6,\qquad
2c\le d\le2c+6,\qquad
c\le f\le c+8.
$$



Exact rational intervals certify $441/441$ values at each of
$N=2,3,4$ at least one, $440/441$ at $N=6$ at least one, and the sole
value below one as $(c,d,f)=(0,3,0)$, $q=9$. There are no undecided
interval cases.

The proof does not cover coupled sequences whose ratios approach a boundary
nonuniformly, exceptional fixed-integral zeros, sparse exceptional
coordinate-denominator cancellation, or an all-index clearing theorem for
the other fixed-$(c,f)$, $N=6$ boundary cases. The source expressly
preserves this caveat.

The frozen source had two nonmathematical defects: equation (8) contained
literal “,qquad” instead of “,\qquad”, and the integrality sentence below
(78) cited local (11) instead of equation (11) of the accepted earlier
audit. Those strings were corrected without changing a mathematical
formula. The corrected source SHA-256 is

c86638fbcc6fbd109d5852c3f04c2035df5c6f1636fe0c2c087b3c7e8d09753d.

A search of the frozen SHA finds only one occurrence of
“This proves (20).”; there was no duplicate sentence to delete. The
independent script and frozen result have SHA-256 values

- b548cc62d932ce7b01be88f13dbbc8e9d94bda4322ceade1dcbfdf377dc93c7f;
- 7f0066d85679c11763e27a6a72d0283c061d04f123db22d04096c6c9c604eeeb.

## Conclusion

The small-root construction gives a rigorous broad no-go theorem: every
fixed admissible proportional ray grows exponentially, $N=2$ has an
exact all-index local obstruction, and the sole finite $N=6$ local
contraction is not a global norm contraction. The lower circular contour,
polynomial (A12), endpoint bounds (A13)--(A14), and nonzero Gaussian term
(A17) close the only materially compressed part of the source proof. The
sparse-regime caveat remains essential. None of these results determines
whether $e+\pi$ is algebraic or transcendental.
