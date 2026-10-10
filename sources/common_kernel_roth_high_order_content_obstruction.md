> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A Roth criterion and a high-order content obstruction for the native common kernel

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
u=1+x^2,\qquad t=1-x,\qquad
 {\cal T}P=(1-x)P'-xP,
$$



and write



$$
(1-i)^N=R_N+iI_N,\qquad M_N=N!-R_N,
$$





$$
K_N(x)=I_N-\frac{M_N}{2}(1-x)\qquad(N\geq2).           \tag{1}
$$



Let $h\in\mathbb Z[x]$ satisfy



$$
h\equiv1\pmod {u^2},\qquad h(0)=0,\qquad
 0\leq h(x)\leq1\quad(0\leq x\leq1),                   \tag{2}
$$



and set



$$
F_{N,h}(x)=t^N+{\cal T}(hK_N)(x).                     \tag{3}
$$



Assume that $F_{N,h}$ is one-signed on $[0,1]$.  The native sign
identity then makes it nonnegative and gives



$$
\frac1{N+1}\leq
 L_{N,h}:=\int_0^1F_{N,h}(x)
 \left(e^x+\frac4{1+x^2}\right)dx
 \leq\frac{5e}{N+1}.                                   \tag{4}
$$



Write its exact rational coordinate in lowest terms as



$$
L_{N,h}=N!(e+\pi)+\frac{c_{N,h}}{D_{N,h}},
 \qquad D_{N,h}>0,\quad (c_{N,h},D_{N,h})=1,            \tag{5}
$$



and put



$$
g_{N,h}=\gcd(N!,c_{N,h}).                              \tag{6}
$$



This note proves two complementary facts.

**Conditional Roth criterion.**  If, for some fixed
$0<\delta<1/2$, infinitely many $N\to\infty$ admit such a
sign-controlled $h$ with



$$
\boxed{\frac{g_{N,h}}{D_{N,h}}
 \geq(N!)^{1/2+\delta},}                                \tag{7}
$$



then $e+\pi$ is transcendental.

**High-order arithmetic obstruction.**  Fix
$0<\eta<1/2$.  Suppose in addition that, along a sequence
$N\to\infty$,



$$
d=\deg h,\qquad r=\operatorname {ord}_0h,\qquad
 r\geq\left(\frac12+\eta\right)d.                       \tag{8}
$$



Then



$$
\boxed{\log D_{N,h}\geq(\eta-o(1))d,}                  \tag{9}
$$





$$
\boxed{\log\frac{g_{N,h}}{D_{N,h}}
 \leq-(\eta-o(1))d.}                                    \tag{10}
$$



Thus (7) is impossible throughout the local, high-origin-order
regime (8).  The obstruction is much stronger than a failure to gain
a fixed Roth exponent: the available output content is exponentially
smaller than the reduced rational denominator on the $d$-scale.

The canonical sparse integer localizer



$$
h_m=x^{4m}(m+1-mx^4)                                   \tag{11}
$$



has $r=4m$, $d=4m+4$, and is therefore covered.  If its native
residual is one-signed along any sequence $N\to\infty$, then



$$
\log D_{N,h_m}\geq(2-o(1))m,\qquad
 \log\frac{g_{N,h_m}}{D_{N,h_m}}\leq-(2-o(1))m.          \tag{12}
$$



By contrast, the nonlocal CRT family with
$\operatorname {ord}_0h=20q$ and $\deg h=48q+13$ has limiting
ratio $5/12<1/2$.  Its decisive prime interval below is empty.  That
family also has no proved native sign law and no proved numerator-content
law.  Equations (9)--(10) do not apply to it.

The theorem is a rigorous obstruction for (8), not a construction of
(7), and it does not classify $e+\pi$.

## 2. Primitive rational approximation and the Roth threshold

Multiplying (5) by $D_{N,h}$ gives the integer coefficient pair



$$
N!D_{N,h},\qquad c_{N,h}.
$$



Because $(c_{N,h},D_{N,h})=1$,



$$
\gcd(N!D_{N,h},c_{N,h})
 =\gcd(N!,c_{N,h})=g_{N,h}.                             \tag{13}
$$



Consequently



$$
p_{N,h}=-\frac{c_{N,h}}{g_{N,h}},\qquad
 q_{N,h}=\frac{N!D_{N,h}}{g_{N,h}}                     \tag{14}
$$



are coprime integers, $q_{N,h}>0$, and



$$
\boxed{
 \left|(e+\pi)-\frac{p_{N,h}}{q_{N,h}}\right|
 =\frac{L_{N,h}}{N!}.}                                 \tag{15}
$$



The sign bounds (4) therefore yield



$$
\frac1{(N+1)N!}
 \leq
 \left|(e+\pi)-\frac{p_{N,h}}{q_{N,h}}\right|
 \leq\frac{5e}{(N+1)N!}.                               \tag{16}
$$



Condition (7) is equivalent, without a hidden constant, to



$$
q_{N,h}\leq(N!)^{1/2-\delta}.                          \tag{17}
$$



Suppose first that $e+\pi=A/B$ is rational in lowest terms.  The
strict lower bound in (16) says that $p_{N,h}/q_{N,h}\ne A/B$.
Hence elementary separation of unequal reduced rationals gives



$$
\left|(e+\pi)-\frac{p_{N,h}}{q_{N,h}}\right|
 \geq\frac1{Bq_{N,h}},
$$



which contradicts (16)--(17) for large $N$.

Suppose instead that $e+\pi$ is algebraic irrational.  Take
$\varepsilon=2\delta$.  Then



$$
(1/2-\delta)(2+\varepsilon)
 =1-\delta-2\delta^2<1.                                 \tag{18}
$$



It follows from (16)--(18) that, for all sufficiently large members of
the sequence,



$$
\left|(e+\pi)-\frac{p_{N,h}}{q_{N,h}}\right|
 <q_{N,h}^{-2-\varepsilon}.                             \tag{19}
$$



The denominators are unbounded: otherwise only finitely many rational
numbers can lie in a fixed bounded interval with those denominators,
whereas (16) gives nonzero errors tending to zero.  Equation (19) then
contradicts Roth's theorem.  The rational and algebraic-irrational cases
exhaust the real algebraic numbers, proving the conditional criterion.

The Roth theorem used here is K. F. Roth, *Rational approximations to
algebraic numbers*, Mathematika **2** (1955), 1--20,
doi:10.1112/S0025579300000644.

## 3. The sign-forced degree scale

For completeness, the degree input needed below has a short direct
proof.  Put



$$
H(t)=h(1-t),\qquad a=-I_N,\qquad b=\frac{M_N}{2}.
$$



The congruence and interval bounds in (2) imply



$$
H(0)=1,\qquad H(1)=0,\qquad0\leq H\leq1.               \tag{20}
$$



The integrating-factor identity



$$
\int_0^1e^{-t}F_{N,h}(1-t)\,dt
 =\int_0^1e^{-t}t^N\,dt>0                              \tag{21}
$$



follows by writing
${\cal T}Y=-tY'-(1-t)Y$ and integrating
$(te^{-t}Y)'$ for $Y(t)=h(1-t)K_N(1-t)$; both boundary terms
vanish.  It shows that a one-signed residual must be nonnegative.
Moreover, if



$$
B_N=\int_0^1e^{-t}t^N\,dt,
$$



then $e^{-1}/(N+1)\leq B_N\leq1/(N+1)$, while the ratio of the
full weight in (4), in the $t$-coordinate, to $e^{-t}$ lies between
$e$ and $5e$.  This proves (4).  The endpoint value is
$F_{N,h}(1)=-I_N$, so $a\geq0$, while $b>0$.
Direct differentiation gives



$$
\left(t(a+bt)e^{-t}H(t)\right)'
 =e^{-t}\{F_{N,h}(1-t)-t^N\}.                           \tag{22}
$$



Integrating (22) from $t$ to $1$, and using nonnegativity, gives



$$
t(a+bt)e^{-t}H(t)
 \leq\int_t^1e^{-s}s^N\,ds
 \leq\frac1{N+1}.                                      \tag{23}
$$



Markov's inequality on $[0,1]$ gives
$\lVert H'\rVert_\infty\leq2d^2$.  At
$t=1/(3d^2)$, equation (20) therefore gives $H(t)\geq1/3$.
Keeping only the $bt^2$ term on the left of (23) and using
$e^{-t}\geq e^{-1}$ yields



$$
\boxed{d^4\geq\frac{M_N(N+1)}{54e}.}                   \tag{24}
$$



Since $|R_N|\leq2^{N/2}=o(N!)$,



$$
M_N=N!(1+o(1)),\qquad
 \log M_N=\log N!+o(1).                                 \tag{25}
$$



Equations (24)--(25) imply



$$
\log N!=o(d),\qquad \log M_N=o(d),\qquad N=o(d).        \tag{26}
$$



The enormous separation in (26) is what turns the prime-window
denominator below into a primitive-content obstruction.

## 4. Exact native quotient and its forced coefficient

The defect polynomial (1) satisfies



$$
\boxed{
 {\cal T}K_N
 =-\frac{M_N}{2}u+(M_N-I_Nx).}                          \tag{27}
$$



Define



$$
S_{N,h}
 =\frac{{\cal T}(hK_N)-{\cal T}K_N}{u}\in\mathbb Z[x],
 \qquad v=\frac{h-1}{u}\in\mathbb Z[x].                 \tag{28}
$$



The product rule and (27) give



$$
\boxed{
 S_{N,h}
 =-\frac{M_N}{2}(h-1)
   +v(M_N-I_Nx)
   +(1-x)\frac{h'}uK_N.}                                \tag{29}
$$



If $h_d$ is the leading coefficient of $h$, then $hK_N$ has
degree $d+1$ and leading coefficient $M_Nh_d/2$.  The unique
degree-$d+2$ term of ${\cal T}(hK_N)$ is
$-M_Nh_dx^{d+2}/2$.  Division by the monic quadratic $u$ proves



$$
\boxed{\deg S_{N,h}=d.}                                \tag{30}
$$



Now let $r=\operatorname {ord}_0h$.  Since
$h-1=-1+O(x^r)$, formal division by $u=1+x^2$ gives the forced
prefix



$$
[x^{2j}]v=(-1)^{j+1},\qquad [x^{2j+1}]v=0
 \quad(2j,2j+1<r).                                      \tag{31}
$$



Let $p$ be an odd prime satisfying



$$
\max\left\{N,\frac{d+1}{2}\right\}<p<r,
 \qquad p\nmid M_N.                                     \tag{32}
$$



In degree $p-1$, the first term of (29) vanishes because
$0<p-1<r$.  The last term vanishes because $h'/u$ has order
$r-1>p-1$.  Since $p-1$ is even and $p-2$ is odd, (31) gives



$$
\boxed{[x^{p-1}]S_{N,h}=\pm M_N.}                      \tag{33}
$$



By (30) and $2p>d+1$, the monomial integral



$$
\int_0^1S_{N,h}(x)\,dx
 =\sum_{j=0}^{d}\frac{[x^j]S_{N,h}}{j+1}                \tag{34}
$$



has exactly one denominator divisible by $p$, namely the term
$[x^{p-1}]S_{N,h}/p$.  Thus



$$
v_p\left(4\int_0^1S_{N,h}\right)=-1.                  \tag{35}
$$



## 5. Survival in the full output

Let



$$
P_N^{(0)}
 =N!\sum_{j=0}^{N-1}\frac{(1-x)^j}{(j+1)!}\in\mathbb Z[x].
$$



It obeys



$$
N!+{\cal T}P_N^{(0)}=t^N.
$$



At $x=i$, equations (27) and
$(1-i)^N=R_N+iI_N$ show that
$t^N+{\cal T}K_N=N!$; the value at $-i$ is its conjugate.
Thus the monic polynomial $u$ divides the integer numerator below,
and



$$
Q_N^*
 =\frac{t^N+{\cal T}K_N-N!}{u}\in\mathbb Z[x],
 \qquad\deg Q_N^*\leq N-2.                              \tag{36}
$$



For the localized form,



$$
Q_{N,h}
 =\frac{F_{N,h}-N!}{u}
 =Q_N^*+S_{N,h}.                                       \tag{37}
$$



Integration by parts gives the exact common-kernel output



$$
L_{N,h}
 =N!(e+\pi)-N!-\bigl(P_N^{(0)}+hK_N\bigr)(0)
   +4\int_0^1Q_{N,h}(x)\,dx.                            \tag{38}
$$



All terms in (38) except the displayed rational integral are integers.
Moreover, the denominator of $\int Q_N^*$ divides
$\operatorname {lcm}(1,\ldots,N-1)$.  Hence every prime in (32) is
integral in the base coordinate.  Equation (35) cannot cancel, and
therefore



$$
\boxed{
 \prod_{\substack{\max\{N,(d+1)/2\}<p<r\\p\nmid M_N}}p
 \ \bigg|\ D_{N,h}.}                                    \tag{39}
$$



Each displayed prime occurs in $D_{N,h}$ to exact exponent one.
This is an all-parameter statement; no asymptotic or finite-grid
extrapolation enters (39).

## 6. Asymptotic content obstruction

Assume (8).  Equations (24)--(26) show that, eventually,
$(d+1)/2>N$.  Taking logarithms in (39), using
$\sum_{p\mid M_N}\log p\leq\log M_N$, gives



$$
\begin{aligned}
 \log D_{N,h}
 &\geq
 \vartheta(r)-\vartheta((d+1)/2)-\log M_N\\
 &\geq(\eta-o(1))d.                                    \tag{40}
\end{aligned}
$$



Here the second line is the prime number theorem together with
$r\geq(1/2+\eta)d$ and (26).  This proves (9).

On the other hand,



$$
g_{N,h}\mid N!,\qquad \log g_{N,h}\leq\log N!=o(d).
$$



Subtracting (40) proves (10).  In particular,



$$
\log q_{N,h}
 =\log N!+\log D_{N,h}-\log g_{N,h}
 \geq(\eta-o(1))d,                                     \tag{41}
$$



whereas every fixed power of $N!$ has logarithm $O(N\log N)=o(d)$.
Thus the denominator in this regime lies far above, rather than below,
the square-root-factorial Roth threshold.

For (11), the exact identities



$$
\operatorname {ord}_0h_m=4m,\qquad \deg h_m=4m+4
$$



give



$$
r-\frac{d+1}{2}=2m-\frac52.
$$



The same proof as (40), now with the exact endpoint ratio, yields
(12).

## 7. What remains open

The obstruction uses the strict geometric hypothesis (8).  It does not
extend formally to the known nonlocal CRT localizers.  For their
parameters



$$
r=20q,\qquad d=48q+13,
$$



one has $r<(d+1)/2$, so (39) contains no prime.  Their separate CRT
identities cancel a lower one-third denominator window, but they prove
neither:

1. that the native residual (3) is one-signed; nor
2. that the numerator $c_{N,h}$ contains a factorial-scale divisor.

Accordingly (7) remains an exact, open arithmetic target in that
nonlocal family.

## 8. Replay and scope

The companion exact certificate

    scripts/common_kernel_roth_high_order_content_obstruction_certificate.py

checks:

1. the Gaussian recurrence and the native defect identity (27);
2. the quotient identity (29), exact degree (30), and forced prefix
   (31);
3. every predicted prime valuation in (33)--(35) on a finite exact
   grid;
4. survival of those primes in the complete rational output (38);
5. the sparse-localizer degree/order formulas and the exact primitive
   normalization (13)--(15).

The finite calculations are regression tests.  The all-parameter
results are the proofs above.  No hardware accelerator is useful, and
the replay stays well below $2$ GiB RAM.
