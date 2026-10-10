> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Small-root and boundary continuation of Rivoal's simultaneous exponential--logarithm forms

Checked: 2026-08-26 UTC

## Verdict and exact scope

This note revisits the corrected Rivoal construction at



$$
N\in\{3,4,6\},\qquad
\zeta_N=e^{2\pi i/N},\qquad \eta_N=1-\zeta_N.
\tag{1}
$$



These cases were not covered by the earlier estimate requiring
$|\eta_N|<1$.  That restriction is unnecessary for the identity.  The
logarithmic remainder continues holomorphically to
$\mathbb C\setminus[1,\infty)$, and every $\eta_N$ in (1) lies in that
domain.  The continued integral has no pole on its path.

The boundary root $N=2$, for which $\eta_2=2$, is treated separately in
Section 11.  The sharper analysis gives four rigorous conclusions.

1. On every admissible proportional ray

   

$$
c=n,\qquad d=\lambda n,\qquad f=\mu n,
   \qquad \lambda\geq2,\quad\mu\geq1,
   \tag{2}
$$



   with fixed rational $\lambda,\mu$ and compatible integers $n$, the
   combined unscaled form is eventually nonzero and in fact grows
   exponentially.  Uniformly over the three roots, its exponential rate is
   at least

   

$$
1.64828\ldots .
   \tag{3}
$$



   Thus no denominator clearing, minimal or otherwise, can turn a
   proportional ray into a norm contraction.  This is an all-degree
   asymptotic no-go theorem, not a finite-data extrapolation.

2. Exact coefficientwise denominator clearing is often far smaller than
   the earlier safe factor $d!^2G$.  A finite exact scan does find one
   genuine locally contracting cleared value:

   

$$
(N;c,d,f)=(6;0,3,0),\qquad
   q_{min}|\Lambda|=0.6483138992\ldots<1.
   \tag{4}
$$



   It does not give a product-formula contradiction.  The simultaneous
   conjugate has the same size, but the two off-diagonal formal cyclotomic
   evaluations have modulus $21.12417\ldots$.  When the cyclotomic
   coefficient field is disjoint from $\mathbb Q(s)$, the exact
   four-embedding relative norm has distinguished value

   

$$
187.5555998647\ldots>1.
   \tag{5}
$$



   If the intersection is instead the real quadratic subfield, those
   off-diagonal maps move $s$ to an uncontrolled conjugate; bare
   algebraicity still gives no global contraction.

3. At $N=2$, the lower-half-plane boundary value is mathematically
   well-defined and is exactly the branch that isolates $e+\pi$.  Its
   monodromy term cannot be omitted.  More strongly, exact coefficientwise
   clearing gives an all-index obstruction: for every admissible triple,
   every nonzero cleared distinguished value has modulus at least one.
   Thus $N=2$ cannot provide even a local norm contraction in this
   specialization.

4. The theorem below rules out every proportional growth regime and shows
   why the exact exceptional case (4) gives no contradiction, but it is not
   claimed to be an all-index
   theorem for every highly non-proportional sequence of triples.  No
   viable regime was found in the exact scan, and the boundary asymptotics
   in Section 8 rule out the main fixed-parameter escapes.  A hypothetical
   sparse sequence in which the ratios in (2) degenerate and the exact
   coordinate denominators undergo exceptional cancellation remains a
   separate arithmetic question.  This residual caveat is narrower than
   the old $|\eta|^M$ estimate, but it must not be suppressed.

Nothing here proves that $e+\pi$ is algebraic or transcendental.

## 1. Primary source and notation

The source is T. Rivoal, “Simultaneous Padé approximants to the Euler,
exponential and logarithmic functions,” *Journal de Théorie des Nombres de
Bordeaux* 27 (2015), 565--589,
[DOI 10.5802/jtnb.914](https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.914/).
As explained and hashed in `sources/root_of_unity_exp_log_pade_audit.md`,
the statement used here is the author-corrected 2021 version of Theorem 3,
not the misprinted journal statement:
<https://rivoal.perso.math.cnrs.fr/articles/explog.pdf>.

Let $c,d,f$ be nonnegative integers satisfying



$$
d\geq2c,\qquad f\geq c.
\tag{6}
$$



Use the reversed polynomials $A,B,E$ from equations (7)--(13) of the
accepted audit.  Thus



$$
R_{\log}(x)=A(x)\log(1-x)-B(x),
\qquad
R_{\exp}(x)=A(x)e^x-E(x),
\tag{7}
$$



with orders $2c+d+1$ and $f+d+1$, respectively.  Put



$$
M=2c+d+1,\qquad C=c+d,\qquad F=f+2c.
\tag{8}
$$



At a root in (1), use the branch



$$
\log(1-\eta_N)=\log\zeta_N=\frac{2\pi i}{N}.
\tag{9}
$$



The combined form is



$$
\begin{aligned}
\Lambda_N(c,d,f)
&=2iA(\eta_N)R_{\exp}(1)+NA(1)R_{\log}(\eta_N)\\
&=2iA(1)A(\eta_N)(e+\pi)
 -2iA(\eta_N)E(1)-NA(1)B(\eta_N).
\end{aligned}
\tag{10}
$$



## 2. A continuation formula on the correct slit plane

Because $B$ is the Taylor truncation of $A(x)\log(1-x)$ through degree
$C$, direct summation of the logarithmic tail gives, initially for
$|x|<1$,



$$
R_{\log}(x)
=-x^M\int_0^1\frac{t^{M-1}A(1/t)}{1-xt}\,dt.
\tag{11}
$$



The numerator in the integrand is a polynomial: since
$A(x)=x^CP(1/x)$,



$$
t^{M-1}A(1/t)=t^cP(t).
\tag{12}
$$



For every compact subset of



$$
\Omega=\mathbb C\setminus[1,\infty),
\tag{13}
$$



the denominator in (11) is bounded away from zero uniformly for
$0\leq t\leq1$.  The right side is therefore holomorphic on $\Omega$.
The identity theorem continues (11), with the principal logarithm, from
the unit disk to all of $\Omega$.

For $N=3,4,6$, $\operatorname{Im}\eta_N<0$.  Consequently
$1-\eta_Nt\ne0$ throughout $[0,1]$, and (11) is an ordinary absolutely
convergent integral.  No principal value or indentation is involved.

## 3. Rodrigues reduction and a one-dimensional exact remainder

Define the real polynomial



$$
H_{d,f}(u)=
\sum_{r=0}^d(-1)^r\binom{f+r}{f}\frac{u^r}{(d-r)!}.
\tag{14}
$$



Re-indexing Rivoal's double sum gives the exact Rodrigues identity



$$
P(u)=\frac1{c!}\left(\frac d{du}\right)^c
\bigl(u^c(1-u)^cH_{d,f}(u)\bigr).
\tag{15}
$$



Indeed, differentiating
$u^{c+r}(1-u)^c$ produces exactly the inner binomial sum in the
coefficient formula for $P$.  Integrating (11) by parts $c$ times is
legitimate because $u^c(1-u)^c$ kills all boundary terms.  The elementary
identity



$$
\left(\frac d{du}\right)^c\frac{u^c}{1-xu}
=\frac{c!}{(1-xu)^{c+1}}
\tag{16}
$$



then gives the continued remainder in the useful exact form



$$
\boxed{
R_{\log}(x)=(-1)^{c-1}x^M
\int_0^1
\frac{u^c(1-u)^cH_{d,f}(u)}{(1-xu)^{c+1}}\,du,
\qquad x\in\Omega.}
\tag{17}
$$



Expanding $(1-uy)^d$ also gives



$$
H_{d,f}(u)=\frac1{d!f!}
\int_0^\infty y^f(1-uy)^de^{-y}\,dy,
\tag{18}
$$



so (17) is exactly the analytic continuation of the double integral in the
accepted audit, not a new formal approximation.

There is a useful nondegeneracy at $u=1$.  Equation (15) gives



$$
A(1)=P(1)=(-1)^cH_{d,f}(1).
\tag{19}
$$



If $f\geq1$, then



$$
\operatorname{sgn}H_{d,f}(1)=(-1)^d,
\qquad A(1)\ne0.
\tag{20}
$$



For even $d$, this is immediate from (18).  For odd $d$, split the
integral at $y=1$ and put $y=1\mp t$.  On $0<t<1$, the ratio of the
negative-side weight to the positive-side weight is



$$
\left(\frac{1+t}{1-t}\right)^f e^{-2t}>1,
\tag{21}
$$



because
$\log((1+t)/(1-t))>2t$; the part with $t>1$ is also strictly negative.
This proves (20).

## 4. Exact coefficientwise denominator clearing at fixed small $N$

Write



$$
\Lambda_N=U_Ns+V_N,
\qquad s=e+\pi,
\tag{22}
$$



where



$$
U_N=2iA(1)A(\eta_N),
\qquad
V_N=-2iA(\eta_N)E(1)-NA(1)B(\eta_N).
\tag{23}
$$



Let $L_N=\mathbb Q(i,\zeta_N)$.  For $N=4$,
$\mathcal O_{L_N}=\mathbb Z[i]$.  For $N=3,6$, the discriminants of
$\mathbb Q(i)$ and $\mathbb Q(\sqrt{-3})$ are coprime, so



$$
\mathcal O_{L_N}=\mathbb Z[i,\zeta_N]
\tag{24}
$$



with integral basis $1,\zeta_N,i,i\zeta_N$.

Define $q_N(c,d,f)$ to be the least positive rational integer for which



$$
q_NU_N,\ q_NV_N\in\mathcal O_{L_N}.
\tag{25}
$$



This is an exact, finite definition.  It is evaluated by writing the two
numbers in the bases above and taking the lcm of their reduced coordinate
denominators.  In particular, it is not the crude common denominator from
a coefficient-height estimate.  The earlier safe clearing proves



$$
q_N(c,d,f)\mid d!^2\operatorname{lcm}(\ell_C,F!).
\tag{26}
$$



Under the temporary hypothesis $s\in\overline{\mathbb Q}$, choose
$\delta\geq1$ such that $\delta s$ is integral.  Then



$$
X_N=\delta q_N\Lambda_N
=(q_NU_N)(\delta s)+\delta q_NV_N
\tag{27}
$$



is an algebraic integer.  The word “least” in (25) is coefficientwise: a
special algebraic relation involving the unknown $s$ could conceivably
make a smaller multiplier work for that particular $s$.  Formula (25) is
the least universal clearing obtained before using such unknown relations.

For example, at $(c,d,f)=(1,2,1)$, the exact values are



$$
q_3=4,\qquad q_4=1,\qquad q_6=2,
\tag{28}
$$



whereas the safe factor in (26) is $24$ in all three cases.  This is why
the small-root question cannot be decided using $d!^2G$ alone.

## 5. Which conjugate embeddings are genuinely analytic?

For $N=4$, $\zeta_4=i$.  The two embeddings of $L_4$ are identity
and complex conjugation.  Since the distinguished value of $s=e+\pi$ is
real, these two factors of (27) are exact complex conjugates and their
product is



$$
|X_4|^2.
\tag{29}
$$



There is no independent “small second embedding”: it has exactly the same
modulus.

For $N=3,6$, the two quadratic fields in (24) are linearly disjoint.
There are four cyclotomic embeddings, obtained by independently choosing



$$
i\mapsto\pm i,
\qquad
\zeta_N\mapsto\zeta_N^{\pm1}.
\tag{30}
$$



Only the identity and the simultaneous change of both signs are the
analytic value (10) and its complex conjugate.  The two off-diagonal
embeddings fix one of $i,\zeta_N$ and conjugate the other.  They do not
turn (10) into a Padé remainder for $e+\pi$; they must be evaluated from
the algebraic expression (22)--(23).  Ignoring them is precisely the error
that would make (4) look promising.

There is a compositum caveat.  The biquadratic field $L_N$ contains the
real subfield $\mathbb Q(\sqrt3)$.  Since the distinguished copy of
$\mathbb Q(s)$ is real,



$$
L_N\cap\mathbb Q(s)\in\{\mathbb Q,\mathbb Q(\sqrt3)\}.
\tag{30a}
$$



If the intersection is $\mathbb Q$, all four maps in (30) extend while
fixing the distinguished $s$.  If it is $\mathbb Q(\sqrt3)$, only the
identity/simultaneous-conjugation pair fixes that intersection; an
off-diagonal map must be accompanied by an embedding of $\mathbb Q(s)$
that sends $\sqrt3$ to $-\sqrt3$.  Its value involves an uncontrolled
conjugate of $s$, not an analytic Padé remainder.  Thus the intersection
case does not remove the off-diagonal cost; it relocates it to unknown
conjugates of $s$.

The elementary cyclotomic factor remains adverse for $N=3,4$ and neutral
for $N=6$:



$$
\operatorname{Norm}(1-\zeta_3)=3,
\qquad
\operatorname{Norm}(1-i)=2,
\qquad
\operatorname{Norm}(1-\zeta_6)=1.
\tag{31}
$$



## 6. Sharp fixed-slope asymptotics

This section replaces the crude $|\eta|^M$ estimate by the actual complex
saddle.

Let $c=n,d=\lambda n,f=\mu n$ as in (2).  Define



$$
\mathcal E(\lambda,\mu)
=(\lambda+\mu)\log(\lambda+\mu)
-\lambda\log\lambda-\mu\log\mu.
\tag{32}
$$



Reversing the index in (14) gives the exact identity



$$
H_{d,f}(u)=(-1)^d\binom{d+f}{d}u^d
\sum_{q=0}^d\frac{(-1)^q}{q!u^q}
\frac{d(d-1)\cdots(d-q+1)}
{(d+f)(d+f-1)\cdots(d+f-q+1)}.
\tag{33}
$$



Uniformly on compact subsets avoiding $u=0$, the finite sum in (33) is



$$
\exp\!\left(-\frac{\lambda}{(\lambda+\mu)u}\right)
\left(1+O(n^{-1})\right).
\tag{34}
$$



This follows by fixing $q$, taking the ratio limit in (33), and using the
factorial $q!$ for a uniform dominated tail.  At $u=1$, equations
(19), (33), and (34) give



$$
A(1)=(-1)^{c+d}\binom{d+f}{d}
e^{-\lambda/(\lambda+\mu)}
\left(1+O(n^{-1})\right).
\tag{35}
$$



For a fixed $N$, let $u_N(\lambda)$ be the unique root in the lower
half-plane of



$$
(\lambda+1)(1-u)(1-\eta_Nu)-\zeta_Nu=0.
\tag{36}
$$



The other root is in the upper half-plane.  The only pole of the integrand
in (17), $1/\eta_N$, is also in the upper half-plane.  The interval
$[0,1]$ can therefore be deformed downward through
$u_N(\lambda)$.  The quadratic equation shows that this is the only
critical point in that half-plane; the real part of the phase tends to
$-\infty$ at both endpoints.  The two descending arcs from the simple
saddle end at $0$ and $1$, while the complementary upward saddle is
separated by the pole.  The one-saddle steepest-descent expansion is thus
valid without a second term that could cancel it.

Put



$$
\begin{aligned}
\varphi_{N,\lambda}(u)={}&
(\lambda+2)\operatorname{Log}\eta_N
+(\lambda+1)\operatorname{Log}u\\
&+\operatorname{Log}(1-u)-\operatorname{Log}(1-\eta_Nu),
\end{aligned}
\tag{37}
$$



with the branches continued along that lower contour, and define



$$
\chi_N(\lambda)=
\operatorname{Re}\varphi_{N,\lambda}(u_N(\lambda)).
\tag{38}
$$



Equations (17), (33)--(34), and the quadratic saddle expansion give the
sharp asymptotic



$$
\boxed{
R_{\log}(\eta_N)
=(-1)^{c+d-1}\binom{d+f}{d}
K_{N,\lambda,\mu}\,n^{-1/2}
e^{n\varphi_{N,\lambda}(u_N(\lambda))}
\left(1+O(n^{-1})\right),}
\tag{39}
$$



where $K_{N,\lambda,\mu}\ne0$.  Its modulus is explicitly



$$
|K_{N,\lambda,\mu}|=
\left|\frac{\eta_N
e^{-\lambda/((\lambda+\mu)u_N)}}
{1-\eta_Nu_N}\right|
\sqrt{\frac{2\pi}{|\varphi_{N,\lambda}''(u_N)|}}.
\tag{40}
$$



In particular,



$$
\frac1n\log|R_{\log}(\eta_N)|
\longrightarrow\mathcal E(\lambda,\mu)+\chi_N(\lambda).
\tag{41}
$$



The exponential remainder is factorially smaller:



$$
|R_{\exp}(1)|\leq\frac e{(d+f+1)!}.
\tag{42}
$$



The exact coefficient bound from the accepted audit gives
$|A(\eta_N)|=\exp(O(n))$ on a fixed ray.  Combining (35), (39), and
(42),



$$
\frac{2iA(\eta_N)R_{\exp}(1)}
{NA(1)R_{\log}(\eta_N)}
=\exp\bigl(-(\lambda+\mu)n\log n+O(n)\bigr).
\tag{43}
$$



Thus there is no cancellation between the two summands in (10), and



$$
\boxed{
\frac1n\log|\Lambda_N(n,\lambda n,\mu n)|
\longrightarrow
\rho_N(\lambda,\mu):=
2\mathcal E(\lambda,\mu)+\chi_N(\lambda).}
\tag{44}
$$



This also proves eventual nonvanishing on every fixed ray.

## 7. The rate is positive in the entire admissible region

The positivity in (3) can be checked analytically, not merely from a grid.
At the saddle, the envelope theorem gives



$$
\frac{\partial\chi_N}{\partial\lambda}
=\log|\eta_Nu_N(\lambda)|.
\tag{45}
$$



Also,



$$
\frac{\partial\mathcal E}{\partial\lambda}
=\log\left(1+\frac\mu\lambda\right),
\qquad
\frac{\partial\mathcal E}{\partial\mu}
=\log\left(1+\frac\lambda\mu\right)>0.
\tag{46}
$$



Hence $\rho_N$ is minimized first at $\mu=1$.  It remains to check
monotonicity in $\lambda$.

Here is a short exact modulus check.  Put $L=\lambda+1$,
$w=\eta_Nu_N$, and $v=w/\sqrt{\eta_N}$.  The two roots in the
$v$-variable have product one.  If
$v+v^{-1}=a+ib$ and $y=|v|^2<1$, then



$$
\frac{a^2y}{(1+y)^2}+\frac{b^2y}{(1-y)^2}=1,
\tag{47}
$$



whose left side is strictly increasing in $0<y<1$.  For $N=3$,
substitution of $y=1/|\eta_3|$ leaves
$(L-1)/L^2>0$ on the right side of $1-(47)$; for $N=4$ it leaves
$(2L-5)/L^2>0$.  Therefore



$$
|\eta_Nu_N|>1\qquad(N=3,4).
\tag{48}
$$



For $N=6$, the normalized trace is particularly simple:



$$
v+v^{-1}=\sqrt3+\frac iL.
\tag{49}
$$



Substitution in (47) shows



$$
|u_6(\lambda)|>\left(\frac{\lambda}{\lambda+1}\right)^2.
\tag{50}
$$



For completeness, after substituting
$y=(L-1)^4/L^4$, the numerator of $1-(47)$, expanded in
$t=L-3\geq0$, is



$$
\begin{aligned}
{}&12t^{14}+424t^{13}+7192t^{12}+77320t^{11}
+585380t^{10}+3282160t^9\\
&+13979129t^8+45741108t^7+115153853t^6
+221419630t^5\\
&+319558808t^4+335307040t^3+241643432t^2
+107018384t+21971329,
\end{aligned}
\tag{51}
$$



which is positive.  Equations (45), (48), and (50) now give



$$
\frac{\partial\rho_N(\lambda,1)}{\partial\lambda}>0
\qquad(\lambda\geq2).
\tag{52}
$$



The global minimum is therefore at $(\lambda,\mu)=(2,1)$.  Direct
evaluation of the quadratic root gives



$$
\begin{array}{c|c|c}
N&\chi_N(2)&\rho_N(2,1)\\ \hline
3& 0.2822984707\ldots&4.1013834804\ldots\\
4&-0.6819432105\ldots&3.1371417992\ldots\\
6&-2.1708046194\ldots&1.6482803903\ldots
\end{array}
\tag{53}
$$



The positivity also follows from coarse rational enclosures of the radicals
and the power series for $\log$; the decimals only display the much larger
margin.  Equations (44) and (53) prove the proportional-ray no-go asserted
in the verdict.  Since $|\Lambda_N|\to\infty$ already before clearing,
the exact value of $q_N\geq1$ cannot rescue such a ray.

## 8. Boundary asymptotics

The same exact integral isolates the principal non-proportional boundaries.

First fix $c,f$ and let $d\to\infty$.  Uniform endpoint Laplace
expansion in (17) gives



$$
\begin{aligned}
A(1)&\sim(-1)^{c+d}\frac{d^f}{f!e},\\
R_{\log}(\eta_N)&\sim
(-1)^{c+d-1}\frac{c!}{f!e}
d^{f-c-1}\eta_N^{d+2c+1}\zeta_N^{-(c+1)},
\end{aligned}
\tag{54}
$$



and hence



$$
|\Lambda_N|\sim
\frac{Nc!}{(f!)^2e^2}
d^{2f-c-1}|\eta_N|^{d+2c+1}.
\tag{55}
$$



The exponential-remainder summand is again factorially smaller.  Thus the
boundary grows exponentially for $N=3,4$.  For $N=6$, where
$|\eta_6|=1$, it grows polynomially except at the two lowest exponents;
for $c=f=0$ it is asymptotic to $6e^{-2}/d$.

That last decay still cannot survive exact clearing.  When $c=f=0$, put



$$
D_d=d!\sum_{j=0}^d\frac{(-1)^j}{j!},
\qquad
Z_d=d!\sum_{j=0}^d\frac{(-\eta_6)^j}{j!}.
\tag{56}
$$



They satisfy



$$
D_d=dD_{d-1}+(-1)^d,
\qquad
Z_d=dZ_{d-1}+(-\eta_6)^d.
\tag{57}
$$



For every prime $p\mid d$, both rightmost terms are units modulo every
prime above $p$.  The coefficient $U_6$ in (23) therefore forces



$$
v_p(q_6(0,d,0))\geq2v_p(d!)-v_p(2).
\tag{58}
$$



If $d=pk$, then $p^{v_p(d!)}\geq p^k\geq pk=d$.  Consequently



$$
q_6(0,d,0)\geq\frac{d^2}{2},
\qquad
q_6(0,d,0)|\Lambda_6|\longrightarrow\infty.
\tag{59}
$$



Second, if $c,d$ are fixed and $f\to\infty$, the highest term in
(14) gives



$$
H_{d,f}(u)=(-1)^d\frac{f^d}{d!}u^d+O(f^{d-1})
\tag{60}
$$



uniformly on $[0,1]$.  Except for a possible zero of the fixed explicit
integral in (17), the logarithmic summand is polynomial of degree $2d$
in $f$, while the exponential summand is factorially small.  For
$c=d=0$, the limit is instead $2\pi i$.  This boundary supplies no
systematic small form.  The possible fixed-integral zeros mentioned here
are part of the residual sparse arithmetic caveat in the verdict, not a
claimed opportunity.

## 9. The unique local contraction in the exact scan

For $(N;c,d,f)=(6;0,3,0)$, exact reconstruction gives



$$
\begin{aligned}
A(x)&=-1+x-\frac{x^2}{2}+\frac{x^3}{6},\\
B(x)&=x-\frac{x^2}{2}+\frac{x^3}{3},\\
E(x)&=-1,
\end{aligned}
\tag{61}
$$



and (25) gives $q_6=9$.  Put $\zeta=\zeta_6$.  At the distinguished
embedding,



$$
Y:=9\Lambda_6
=i(1+3\zeta)s+12-9\zeta-3i-9i\zeta.
\tag{62}
$$



Its coordinates in the basis $1,\zeta,i,i\zeta$ are



$$
(12,-9,s-3,3s-9).
\tag{63}
$$



Multiplying the identity value by its simultaneous complex conjugate gives



$$
|Y|^2=
13s^2-(78+45\sqrt3)s+234+135\sqrt3
=0.4203109119\ldots .
\tag{64}
$$



The off-diagonal pair gives



$$
13s^2-(78-45\sqrt3)s+234-135\sqrt3
=446.2306224679\ldots .
\tag{65}
$$



Their product is the exact four-cyclotomic-evaluation polynomial



$$
\boxed{
169s^4-2028s^3+6093s^2-54s+81
=187.5555998647\ldots>1.}
\tag{66}
$$



When (30a) has trivial intersection, (66) is exactly the relative norm over
$\mathbb Q(s)$.  When the intersection is $\mathbb Q(\sqrt3)$, (64)
is the relative norm for the pair fixing the distinguished $s$, while
the remaining absolute-norm factors involve an uncontrolled conjugate of
$s$.  In neither case does bare algebraicity certify a global norm below
one.

The intervals archived by the script are rigorous rational enclosures.
They use the positive series for $e$ and alternating Machin series for
$\pi$, so (64)--(66) do not rely on floating-point sign decisions.
For a general integrality multiplier $\delta$, all four formal values of
$X_6=\delta Y$ acquire the expected factor $\delta$, and the
four-evaluation polynomial acquires $\delta^4$.  Thus the only locally
contracting cleared case in the stated scan either expands after the four
relative embeddings (the disjoint case), or leaves the remaining
$s$-conjugate factors uncontrolled (the real-quadratic intersection
case).  It never supplies the strict global norm estimate required for a
contradiction.

## 10. Exact finite diagnostics

The script `scripts/small_root_rivoal_exp_log.py` performs all arithmetic in
exact rational coordinates before numerical evaluation.  Its default scan
contains $441$ triples for each $N=2,3,4,6$:



$$
0\leq c\leq6,
\quad2c\leq d\leq2c+6,
\quad c\leq f\leq c+8.
\tag{67}
$$



It verifies (26), checks the continued integral (17) against direct
polynomial evaluation for $N=3,4,6$, archives the two exact boundary
values at $N=2$, evaluates the saddles in (53), and certifies the
intervals in (64)--(66).  The scan finds no cleared value below one for
$N=2,3,4$, and exactly the case (61) for $N=6$.  These finite statements
are diagnostics only; the all-degree content is the asymptotic theorem in
Sections 6--7, the boundary result (59), and the exact $N=2$ theorem
below.

## 11. Complete $N=2$ boundary-value analysis

For $N=2$, $\zeta_2=-1$ and $\eta_2=2$ lies on the logarithmic
branch cut.  The relevant boundary values of the principal branch are



$$
\begin{aligned}
R_{\log}^{+}(2)
&:=\lim_{\epsilon\downarrow0}R_{\log}(2-i\epsilon)
 =i\pi A(2)-B(2),\\
R_{\log}^{-}(2)
&:=\lim_{\epsilon\downarrow0}R_{\log}(2+i\epsilon)
 =-i\pi A(2)-B(2).
\end{aligned}
\tag{68}
$$



Here the superscript records the sign of the resulting $i\pi$, not the
half-plane from which $x$ approaches.  In particular,



$$
R_{\log}^{+}(2)-R_{\log}^{-}(2)=2\pi iA(2).
\tag{69}
$$



This boundary continuation follows directly, including its monodromy
term, from the exact tail (11).  Put



$$
h(t)=t^{M-1}A(1/t)=t^cP(t).
\tag{70}
$$



The Sokhotski--Plemelj boundary formula gives



$$
\lim_{\epsilon\downarrow0}
\int_0^1\frac{h(t)}{1-(2-i\epsilon)t}\,dt
=\operatorname {PV}\!\int_0^1\frac{h(t)}{1-2t}\,dt
-\frac{i\pi}{2}h(1/2).
\tag{71}
$$



Since $M-1=C+c$,



$$
2^{M-1}h(1/2)=2^CP(1/2)=A(2).
\tag{72}
$$



Multiplying (71) by $-2^M$ proves the first line of (68), as well as



$$
B(2)=2^M\operatorname {PV}\!\int_0^1
\frac{h(t)}{1-2t}\,dt.
\tag{73}
$$



The other lip is analogous.  Thus the continuation is rigorous, but it is
not an ordinary real-path remainder integral.  In (17) the same
indentation appears as a Hadamard finite part for a pole of order $c+1$.
Discarding the indentation discards exactly the term $\pm i\pi A(2)$.
Equivalently,



$$
|R_{\log}^{+}(2)|^2=B(2)^2+\pi^2A(2)^2,
\tag{74}
$$



Thus the Taylor order at the origin does not suppress the explicit
monodromy component at this boundary point.

The plus boundary in (68) is precisely the one relevant to the present
problem.  It gives



$$
\begin{aligned}
\Lambda_2^+
&=2iA(2)R_{\exp}(1)+2A(1)R_{\log}^{+}(2)\\
&=2iA(1)A(2)s-2iA(2)E(1)-2A(1)B(2).
\end{aligned}
\tag{75}
$$



The minus boundary instead replaces $s=e+\pi$ by $e-\pi$.  Thus
changing lips does not improve an estimate for the desired number; it
changes the number being isolated.

There is an exact all-index obstruction at the plus boundary.  Define
$q_2(c,d,f)$ to be the least positive integer for which



$$
\begin{aligned}
a&=2q_2A(1)B(2),\\
b&=2q_2A(1)A(2),\\
g&=2q_2A(2)E(1)
\end{aligned}
\qquad\text{all belong to }\mathbb Z.
\tag{76}
$$



This is the exact coefficientwise clearing in $\mathbb Z[i]$, and it
still divides the safe factor in (26).  Equation (75) becomes



$$
q_2\Lambda_2^+=-a+i(bs-g),
\qquad
|q_2\Lambda_2^+|^2=a^2+(bs-g)^2.
\tag{77}
$$



We first record a uniform elementary estimate.  Whenever $A(1)\ne0$,



$$
\left|s-\frac{E(1)}{A(1)}\right|
=\left|\pi+\frac{R_{\exp}(1)}{A(1)}\right|>1.
\tag{78}
$$



Indeed, $d!A(1)$ is a nonzero integer by equation (11) of the accepted
audit, while (42) gives



$$
\left|\frac{R_{\exp}(1)}{A(1)}\right|
\leq\frac{e\,d!}{(d+f+1)!}.
\tag{79}
$$



If $f\geq1$, the right side is at most $e/2<3/2$, so (78) follows
from $\pi>3$.  If $f=0$, admissibility forces $c=0$.  For $d=0$,
the quotient in (78) is $R_{\exp}(1)/A(1)=e-1$, and (78) is immediate.
For $d=1$, one has $A(1)=0$.  For $d\geq2$, the right side of (79)
is at most $e/(d+1)\leq e/3<1$, again proving (78).  These estimates use
only the elementary bounds $e<3<\pi$.

Now suppose the cleared value in (77) is nonzero.  If $b=0$, it is a
nonzero Gaussian integer and has modulus at least one.  If $b\ne0$ and
$a\ne0$, (77) again gives modulus at least one.  Finally, if $b\ne0$
and $a=0$, then $A(1)A(2)\ne0$ and $B(2)=0$, while



$$
|q_2\Lambda_2^+|
=|b|\left|s-\frac{E(1)}{A(1)}\right|>1
\tag{80}
$$



by (78).  Therefore



$$
\boxed{
q_2\Lambda_2^+\ne0
\quad\Longrightarrow\quad
|q_2\Lambda_2^+|\geq1
}
\tag{81}
$$



for every admissible triple, with no asymptotic restriction.  Under the
temporary algebraicity hypothesis, multiplying by any positive integral
clearing $\delta$ for $s$ only increases this distinguished modulus.
Moreover, $\mathbb Q(s)\subset\mathbb R$ is disjoint from
$\mathbb Q(i)$, and the other coefficient-field embedding sends (77) to
its complex conjugate.  Their relative product is therefore
$\delta^2|q_2\Lambda_2^+|^2\geq1$.  Thus the $N=2$ boundary
specialization is well-defined, but it is an exact all-index no-go for a
contraction at the two coefficient-field places.  As elsewhere, bare
algebraicity supplies no favorable control at the other conjugates of
$s$.

## Conclusion

Analytic continuation makes Rivoal's corrected construction fully valid at
$N=3,4,6$, while boundary continuation makes the relevant $N=2$ branch
equally precise; neither reveals a successful norm contraction.  At
$N=2$, the monodromy term gives the exact all-index lower bound (81).
For $N=3,4,6$, the
actual saddle, rather than the crude $|\eta|^M$ factor, proves that every
admissible proportional ray grows exponentially and is eventually
nonzero.  Exact minimal coordinate clearing exposes one small isolated
$N=6$ value, but its off-diagonal embeddings either make the four-place
relative norm greater than $187$ or move an uncontrolled conjugate of
$s$.  The fixed-root construction therefore
has a rigorous broad asymptotic barrier and no identified viable regime;
only the explicitly stated highly non-proportional sparse-denominator
question remains outside the theorem.
