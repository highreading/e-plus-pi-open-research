> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A $2$-adic closure of the primitive $\pi$-component in the high critical-Fourier region

## 1. Scope and theorem

Let



$$
n=2r,\qquad K=k-1,\qquad r\geq1,\qquad K\geq2r,
\tag{1}
$$



and consider



$$
J_{n,k}
 =\int_0^1\frac{x^n(1-x)^n}{(1+x^2)^k}\,dx.
\tag{2}
$$



The inequality $K\geq2r$ is exactly $k>n$.  In the accepted Fourier
normalization, let $C_0$ be the central integral Fourier coefficient and
write



$$
J_{n,k}=R_{n,k}+Q_{n,k}\pi,\qquad
 Q_{n,k}=\frac{C_0}{2^{2k}}>0.
\tag{3}
$$



If $R_{n,k}\neq0$, reduce



$$
\frac{R_{n,k}}{Q_{n,k}}=\frac AB,\qquad
 A\in\mathbb Z,\quad B\in\mathbb Z_{>0},\quad \gcd(A,B)=1,
\tag{4}
$$



and orient the primitive form as



$$
\mathcal L_{n,k}=A+B\pi=\frac{B}{Q_{n,k}}J_{n,k}>0.
\tag{5}
$$



This note proves three all-degree statements.

First,



$$
\boxed{
 v_2(C_0)
 =r+s_2(K)+(r\bmod2)v_2(K),}
\tag{6}
$$



where $s_2(K)$ is the number of ones in the binary expansion of $K$.

Second, with $v_2(0)=+\infty$,



$$
\boxed{
 v_2(R_{n,k})
 \geq-k-\lfloor\log_2K\rfloor.}
\tag{7}
$$



Consequently, when $R_{n,k}\neq0$,



$$
v_2(A/B)\geq
 k-r-s_2(K)-(r\bmod2)v_2(K)-\lfloor\log_2K\rfloor.
\tag{8}
$$



Third, uniformly along every sequence satisfying



$$
k\geq\frac1{35}n\log n,
\tag{9}
$$



the primitive $\pi$-form in (5) tends to $+\infty$, provided
$R_{n,k}\neq0$.  If $R_{n,k}=0$, lowest terms give
$(A,B)=(0,1)$, so the primitive $\pi$-form is exactly $\pi$, not a
divergent quantity.  It is nevertheless bounded away from zero, and its
minimally matched primitive $e+\pi$ form tends to $+\infty$; this case
is treated separately in Section 9.

The accepted theorem already proves divergence of the fully matched
primitive $e+\pi$ forms for



$$
n<k\leq\frac1{35}n\log n,
\tag{10}
$$



while the present theorem proves that the primitive $\pi$-component
cannot tend to zero in the complementary high region.  These are
different conclusions.  For $R\neq0$, divergence of
$\mathcal L_{n,k}$ alone does not imply divergence after minimal
coefficient matching and final content removal: the final content may
contain a large divisor of $\gcd(q_n,B)$.  No all-$k$ theorem for the
fully matched primitive $e+\pi$ forms is claimed here.  The result does
not prove any arithmetic statement about $e+\pi$.

## 2. The exact beta-moment sum for $C_0$

After $x=\tan t$, define



$$
H_{n,k}(t)
 =\sin^{2r}t\,(\cos t-\sin t)^{2r}
  \cos^{2(K-2r)}t.
\tag{11}
$$



The central Fourier coefficient is



$$
C_0
 =2^{2K}\frac1{2\pi}\int_0^{2\pi}H_{n,k}(t)\,dt.
\tag{12}
$$



Expanding $(\cos t-\sin t)^{2r}$, all terms with an odd sine or cosine
power have zero full-period mean.  For



$$
S(m,\ell)
 =\frac{(2m)!(2\ell)!}{m!\,\ell!\,(m+\ell)!},
\tag{13}
$$



the standard even beta moment is



$$
\frac1{2\pi}\int_0^{2\pi}
 \sin^{2m}t\cos^{2\ell}t\,dt
 =\frac{S(m,\ell)}{2^{2(m+\ell)}}.
\tag{14}
$$



Every surviving term has $m+\ell=K$, so (12)--(14) give



$$
\boxed{
 C_0=\sum_{j=0}^r
 \binom{2r}{2j}S(r+j,K-r-j).}
\tag{15}
$$



Legendre's identity $v_2(M!)=M-s_2(M)$, together with
$s_2(2M)=s_2(M)$, gives



$$
\begin{aligned}
 v_2(S(m,K-m))
 &=(2m-s_2(m))+(2K-2m-s_2(K-m))\\
 &\quad-(m-s_2(m))-(K-m-s_2(K-m))
 -(K-s_2(K))\\
 &=s_2(K).
 \end{aligned}
\tag{16}
$$



Thus all summands in (15) have the same initial $2$-adic valuation.
The cancellation among their odd parts is determined exactly next.

## 3. The common numerator and its odd polynomial

Put



$$
q=K-2r\geq0
\tag{17}
$$



and define empty products to be one:



$$
A_j^{(r)}=\prod_{t=0}^{j-1}(2r+1+2t),\qquad
 B_j^{(q)}=\prod_{t=0}^{j-1}(2q+1+2t).
\tag{18}
$$



A direct quotient of factorials gives



$$
\frac{S(r+j,K-r-j)}{S(r,K-r)}
 =
 \prod_{s=1}^j
 \frac{2r+2s-1}{2K-2r-2s+1}.
\tag{19}
$$



The common denominator in (19), as $j$ varies, is



$$
D_r(K)
 =\prod_{t=0}^{r-1}
 \bigl(2K-(2r+1+2t)\bigr)
 =B_r^{(q)}.
\tag{20}
$$



It is odd for every integer $K$.  Reversing the unused denominator
factors gives



$$
\frac{C_0}{S(r,K-r)}
 =\frac{N_r(K)}{D_r(K)},
\tag{21}
$$



where



$$
N_r(K)=\sum_{j=0}^r
 \binom{2r}{2j}A_j^{(r)}B_{r-j}^{(q)}
 \in\mathbb Z[K].
\tag{22}
$$



The exact polynomial factorization is



$$
\boxed{
 N_r(K)=2^rK^{\,r\bmod2}P_r(K),}
\tag{23}
$$



where $P_r(K)\in\mathbb Z[K]$ is odd for every integer $K$.
This is stronger than merely checking (6) at individual values of $K$.

### Proof of (23)

Introduce the even exponential generating functions



$$
\mathcal A(z)=
 \sum_{j\geq0}A_j^{(r)}\frac{z^{2j}}{(2j)!},
\qquad
 \mathcal B(z)=
 \sum_{j\geq0}B_j^{(q)}\frac{z^{2j}}{(2j)!}.
\tag{24}
$$



Since



$$
A_j^{(r)}=2^j(r+\tfrac12)_j,
\tag{25}
$$



Kummer's transformation of ${}_1F_1$ gives



$$
\begin{aligned}
 \mathcal A(z)
 &={}_1F_1\left(r+\tfrac12;\tfrac12;\frac{z^2}{2}\right)\\
 &=e^{z^2/2}
 \sum_{u=0}^r r^{\underline u}
 \frac{2^uz^{2u}}{(2u)!}.
 \end{aligned}
\tag{26}
$$



The identical formula with $r,u$ replaced by $q,v$ holds for
$\mathcal B$.  Because



$$
N_r(K)=(2r)![z^{2r}]\mathcal A(z)\mathcal B(z),
\tag{27}
$$



coefficient extraction yields the exact identity



$$
\frac{N_r(K)}{2^r}=(2r-1)!!\sum_{\substack{u,v,w\geq0\\u+v+w=r}}
 \binom r{u,v,w}
 \frac{r^{\underline u}q^{\underline v}}
 {(2u-1)!!(2v-1)!!}.
\tag{28}
$$



The prefactor $(2r-1)!!$ in (28) is essential; omitting it makes the
identity false, although it is an odd factor and therefore does not change
the parity argument.

Every denominator on the right of (28) is odd.  It follows that
$N_r/2^r\in\mathbb Z_{(2)}[K]$.  On the other hand,
$N_r\in\mathbb Z[K]$, so every coefficient of $N_r/2^r$ lies both in
$\mathbb Z[1/2]$ and in $\mathbb Z_{(2)}$.  Their intersection is
$\mathbb Z$.  Therefore



$$
G_r(K):=\frac{N_r(K)}{2^r}\in\mathbb Z[K].
\tag{29}
$$



To determine its parity as an integer-valued function, reduce (28)
modulo two.  For $u\geq2$, $r^{\underline u}$ is even; for every
integer $q$ and $v\geq2$, $q^{\underline v}$ is even.  The four
possibilities $u,v\leq1$ give



$$
G_r(K)\equiv1+r+rq\pmod2.
\tag{30}
$$



Thus $G_r(K)$ is odd for even $r$, while for odd $r$,



$$
G_r(K)\equiv q\equiv K\pmod2.
\tag{31}
$$



When $r$ is odd, evaluate the rational function $N_r(K)/D_r(K)$
from (19)--(22) at $K=0$.  This is polynomial/rational continuation,
not an evaluation of the beta factorials outside their domain; the
denominator $D_r(0)$ is nonzero.  The successive factors in (19) then
give $(-1)^j$, and



$$
\sum_{j=0}^r(-1)^j\binom{2r}{2j}
 =\operatorname{Re}(1+i)^{2r}=0.
\tag{32}
$$



Hence $G_r(0)=0$, and



$$
G_r(K)=K P_r(K)
\tag{33}
$$



for some $P_r\in\mathbb Z[K]$.

It remains to show that $P_r$ is also odd at even $K$.  Since it has
integer coefficients, it suffices to show $P_r(0)=G_r'(0)$ is odd.
Differentiate the triple sum in (28), remembering that $q=K-2r$.
At $K=0$, $q$ is even.  The derivative of
$q^{\underline v}$ is even for $v\geq3$, and
$r^{\underline u}$ is even for $u\geq2$.  The only possibly odd
contributions have $(u,v)=(0,1),(1,1),(0,2),(1,2)$.  For odd $r$,
their parities are respectively



$$
1,\qquad0,\qquad\frac{r-1}{2},\qquad\frac{r-1}{2}.
\tag{34}
$$



The last two cancel.  The odd prefactor in (28) changes nothing, so
$G_r'(0)\equiv1\pmod2$.  Equation (31) handles odd $K$, while
$P_r(K)\equiv P_r(0)\pmod2$ handles even $K$.  This proves (23).
$\square$

## 4. Exact valuation of $C_0$

Equations (16), (20), (21), and (23) now give



$$
\begin{aligned}
 v_2(C_0)
 &=v_2(S(r,K-r))+v_2(N_r(K))-v_2(D_r(K))\\
 &=s_2(K)+r+(r\bmod2)v_2(K),
 \end{aligned}
\tag{35}
$$



which proves (6).  In particular, no unproved assertion about cancellation
among the positive summands in (15) remains.

The first normalized polynomials are



$$
P_1=1,\qquad
 P_2=K^2+9K-35,\qquad
 P_3=K^2+39K-229.
\tag{36}
$$



These examples are illustrative only; the proof above applies to every
$r$.

## 5. Rational coordinates of the monomial integrals

For $0\leq m\leq2K$, put



$$
I_{m,k}=\int_0^1\frac{x^m}{(1+x^2)^k}\,dx.
\tag{37}
$$



Expanding $x^{2r}(1-x)^{2r}$ gives



$$
J_{n,k}
 =\sum_{\nu=0}^{2r}(-1)^\nu
 \binom{2r}{\nu}I_{2r+\nu,k}.
\tag{38}
$$



### 5.1 Even monomials

For $0\leq a\leq K$, let



$$
M_{a,k}
 =B\left(a+\tfrac12,k-a-\tfrac12\right)
 =\int_{-\infty}^{\infty}
 \frac{x^{2a}}{(1+x^2)^k}\,dx
\tag{39}
$$



and define the rational remainder



$$
E_{a,k}=I_{2a,k}-\frac14M_{a,k}.
\tag{40}
$$



Integrating the derivative of
$x^{2a-1}(1+x^2)^{1-k}$ over $[0,1]$ gives, for $a\geq1$,



$$
E_{a,k}
 =\frac{2a-1}{2k-2a-1}E_{a-1,k}
 -\frac{1}{2^{k-1}(2k-2a-1)}.
\tag{41}
$$



Indeed, $M_{a,k}$ satisfies the homogeneous part of the same recurrence.
The change $x\mapsto1/x$ in the tail integral gives the exact reflection



$$
E_{a,k}+E_{K-a,k}=0.
\tag{42}
$$



If $K$ is even, (42) gives $E_{K/2,k}=0$.  If $K$ is odd, applying
(41) to the two central, reflected entries gives



$$
E_{(K-1)/2,k}=\frac1{2^kK},\qquad
 E_{(K+1)/2,k}=-\frac1{2^kK}.
\tag{43}
$$



Here $K$ is odd, so both anchors have valuation $-k$.  Every numerator
and denominator multiplying a previous $E$ in (41), or in its backward
version, is odd; the inhomogeneous term has valuation at least
$-(k-1)$.  Propagating from (42)--(43) proves



$$
\boxed{v_2(E_{a,k})\geq-k}
\tag{44}
$$



for all $0\leq a\leq K$, with $v_2(0)=+\infty$.

### 5.2 Odd monomials

For $0\leq a<K$, set $\lambda=K-a$.  The substitution $u=x^2$,
followed in the tail by $t=1/(1+u)$, gives



$$
\begin{aligned}
 I_{2a+1,k}
 =\frac12\Bigg[
 B(a+1,\lambda)
 -\sum_{j=0}^a(-1)^j\binom aj
 \frac{2^{-(\lambda+j)}}{\lambda+j}
 \Bigg].
 \end{aligned}
\tag{45}
$$



This is rational.  Since $1\leq\lambda+j\leq K$, each term in the finite
sum, including the outside factor $1/2$, has valuation at least



$$
-1-K-\lfloor\log_2K\rfloor
 =-k-\lfloor\log_2K\rfloor.
\tag{46}
$$



The beta term satisfies the same bound; for example,


$$
B(a+1,\lambda)=\frac{a!(\lambda-1)!}{K!}
$$


and $v_2(K!)\leq K-1$ already gives a stronger estimate after the
outside factor $1/2$.  Therefore



$$
\boxed{
 v_2(I_{2a+1,k})
 \geq-k-\lfloor\log_2K\rfloor.}
\tag{47}
$$



## 6. The rational-coordinate bound

The even terms in (38) contribute their rational parts $E_{r+j,k}$;
the odd terms are wholly rational.  Thus



$$
\begin{aligned}
 R_{n,k}
 &=\sum_{j=0}^r\binom{2r}{2j}E_{r+j,k}\\
 &\quad-
 \sum_{j=0}^{r-1}\binom{2r}{2j+1}
 I_{2(r+j)+1,k}.
 \end{aligned}
\tag{48}
$$



This is an integer binomial combination.  The nonarchimedean triangle
inequality applied to (44) and (47) proves (7).

From (3) and (6),



$$
v_2(Q_{n,k})
 =r+s_2(K)+(r\bmod2)v_2(K)-2k.
\tag{49}
$$



Subtracting (49) from (7) proves (8).  If



$$
\ell_2=\lfloor\log_2K\rfloor,
\tag{50}
$$



then



$$
s_2(K)\leq\ell_2+1,\qquad
 (r\bmod2)v_2(K)\leq\ell_2,
\tag{51}
$$



so the conservative consequence requested for the high-region argument is



$$
\boxed{
 v_2(A/B)\geq D_{n,k}:=k-r-3\ell_2-1.}
\tag{52}
$$



For (52), $R\neq0$ is understood.  Once $D_{n,k}>0$, coprimality in
(4) forces $B$ to be odd and



$$
2^{D_{n,k}}\mid A.
\tag{53}
$$



Cancellation in $R$ can only increase the left side of (7); it cannot
weaken (52).

## 7. Two elementary analytic estimates

Let



$$
\gamma=\frac{1+\sqrt2}{2}.
\tag{54}
$$



The identity



$$
\sin t(\cos t-\sin t)
 =\frac{\sin2t+\cos2t-1}{2}
\tag{55}
$$



shows that its absolute value is at most $\gamma$.  Equations
(11)--(12) therefore imply



$$
C_0\leq2^{2K}\gamma^n,
\qquad
 Q_{n,k}=\frac{C_0}{2^{2K+2}}
 \leq\frac{\gamma^n}{4}<\gamma^n.
\tag{56}
$$



For a lower bound on $J_{n,k}$, set



$$
t=\frac14\sqrt{\frac nk}.
\tag{57}
$$



Since $k>n$, $0<t<1/4$.  On $x\in[t,2t]$,



$$
x\geq t,\qquad
 1-x\geq1-2t,\qquad
 1+x^2\leq1+4t^2=1+\frac{n}{4k}.
\tag{58}
$$



The interval has length $t$.  The elementary inequalities



$$
\log(1-2t)\geq-4t=-\sqrt{\frac nk},
\qquad
 \left(1+\frac{n}{4k}\right)^k\leq e^{n/4}
\tag{59}
$$



now give, line by line,



$$
\begin{aligned}
 J_{n,k}
 &\geq
 t^{n+1}(1-2t)^n
 \left(1+\frac{n}{4k}\right)^{-k}\\
 &\geq
 \left(\frac14\sqrt{\frac nk}\right)^{n+1}
 \exp\left(-n\sqrt{\frac nk}-\frac n4\right).
 \end{aligned}
\tag{60}
$$



No asymptotic saddle-point estimate is hidden in (60).

## 8. Uniform divergence when $R\neq0$

Assume $R_{n,k}\neq0$ and $D_{n,k}>0$.  If $A>0$, equations
(5) and (53) give



$$
\mathcal L_{n,k}\geq A\geq2^{D_{n,k}}.
\tag{61}
$$



If $A<0$, positivity in (5) gives $B\pi>|A|$, so



$$
B>\frac{2^{D_{n,k}}}{\pi}
\tag{62}
$$



and hence



$$
\mathcal L_{n,k}
 =\frac{B}{Q_{n,k}}J_{n,k}
 \geq\frac{2^{D_{n,k}}J_{n,k}}{\pi\gamma^n}.
\tag{63}
$$



The right side of (63) is also a valid weakening of (61), because
$J_{n,k}\leq1<\pi\gamma^n$.  Thus (63) holds for both signs of nonzero
$A$.

Combining (52), (60), and (63) gives



$$
\begin{aligned}
 \log\mathcal L_{n,k}
 &\geq
 (k-r-1)\log2-3\log K\\
 &\quad +(n+1)\left(\frac12\log\frac nk-\log4\right)
 -n\sqrt{\frac nk}-\frac n4
 -n\log\gamma-\log\pi.
 \end{aligned}
\tag{64}
$$



We used $3\ell_2\log2\leq3\log K$.

It remains to check uniformity for arbitrarily large $k$, not merely
for $k$ near the boundary (9).  Regard the right side of (64) as a
function $\Phi_n(k)$ of a real variable, with $K=k-1$.  Its derivative
satisfies



$$
\Phi_n'(k)
 \geq
 \log2-\frac3{k-1}-\frac{n+1}{2k},
\tag{65}
$$



because differentiating $-n\sqrt{n/k}$ contributes a positive term.
Uniformly for $k\geq n\log n/35$, the right side of (65) is positive
for all sufficiently large $n$.  Therefore the lower bound is minimized
at the left boundary.

At $k=n\log n/35$, division by $n$ gives



$$
\frac{\Phi_n(k)}n
 =
 \frac{\log2}{35}\log n
 -\frac12\log\left(\frac{\log n}{35}\right)
 +O(1),
\tag{66}
$$



which tends to $+\infty$.  Equations (64)--(66) prove



$$
\boxed{
 \mathcal L_{n,k}\longrightarrow+\infty
 \qquad\text{uniformly for }
 k\geq n\log n/35,\ R_{n,k}\neq0.}
\tag{67}
$$



The proof remains valid if $k$ grows faster than every prescribed
function of $n$; monotonicity (65) is exactly what prevents a hidden
upper restriction on $k$.

## 9. The case $R=0$

If $R_{n,k}=0$, equation (4) in lowest terms is



$$
(A,B)=(0,1),
\qquad
 \mathcal L_{n,k}=\pi.
\tag{68}
$$



It would be false to call the primitive $\pi$-form divergent in this
case.  It is instead a fixed nonzero obstruction to component smallness.

The actual matched $e+\pi$ form does diverge.  Let



$$
E_n=q_ne-p_n>0,\qquad
 \gcd(p_n,q_n)=1,\qquad q_n\geq n^n
\tag{69}
$$



be the accepted primitive beta-integral $e$-form.  Since the
$\pi$-coefficient in (68) is one, minimal matching gives



$$
E_n+q_n\pi=q_n(e+\pi)-p_n.
\tag{70}
$$



Its coefficient content is $\gcd(p_n,q_n)=1$, so it is already
primitive, and



$$
E_n+q_n\pi\geq q_n\pi\geq\pi n^n
 \longrightarrow+\infty.
\tag{71}
$$



Thus the exceptional zero rational coordinate cannot rescue the family.
No assertion that $R$ is always nonzero is needed.

## 10. Exact finite certificate

The companion script performed the following independent exact checks.

* For all 1,296 pairs
  

$$
1\leq r\leq12,\qquad2r\leq K\leq120,
$$


  it verified the beta sum (15), the common-denominator identity
  (21)--(22), the corrected EGF identity (28), the exact valuation (6),
  and the odd normalized numerator.
* It constructed $P_r$ symbolically for $1\leq r\leq12$, verified
  exact division in $\mathbb Z[K]$, and checked odd values independently.
* For all 700 pairs
  

$$
1\leq r\leq10,\qquad2r\leq K\leq80,
$$


  it reconstructed every $E_{a,k}$, every odd integral (45), and
  $R_{n,k}$, and verified (7)--(8).  The smallest finite valuation slack
  in (7) was one.
* For nine selected pairs, it independently constructed the full
  Gaussian-integer Fourier polynomial.  Its $C_0,R,Q$ agreed exactly
  with the beta-moment and monomial-coordinate construction.
* No $R=0$ case occurred in that finite box, but the theorem does not
  extrapolate this observation.

The floating high-scale table in the JSON is diagnostic only.  The
uniform limit is proved symbolically by (64)--(66).

## 11. Reproduction and limitations

From the archive root, run

    python -m py_compile scripts/independent_critical_fourier_two_adic_closure_certificate.py
    python scripts/independent_critical_fourier_two_adic_closure_certificate.py

For a byte-identical rerun without replacing the archived JSON:

    python scripts/independent_critical_fourier_two_adic_closure_certificate.py \
      --output /tmp/independent_critical_fourier_two_adic_closure.json
    cmp results/independent_critical_fourier_two_adic_closure.json \
      /tmp/independent_critical_fourier_two_adic_closure.json

The source, script, and result hashes are reported together after the
byte-identical rerun and formatting audits.  The high-region theorem is a
no-go result for this particular critical-Fourier construction.  It does
not by itself control the final matching content when $R\neq0$.  For
example, already at $n=2,k=10$, the matching gcd and the final content
can both equal $7$, so parity does not force primitive content one.  It
does not prove that $e+\pi$ is rational, irrational, algebraic, or
transcendental.
