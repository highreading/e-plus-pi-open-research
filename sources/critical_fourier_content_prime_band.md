> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A forced prime band in the critical Fourier content

Date: 2026-08-26.

## 1. Outcome

For positive even $n$ and $k>n$, retain the notation of
critical_quadratic_power_fourier_barrier.md:



$$
J_{n,k}=\int_0^1\frac{x^n(1-x)^n}{(1+x^2)^k}\,dx
 =\frac1{2^{2k-2}L_k}
  \left(T_{n,k}+\frac{L_kC_0}{4}\pi\right),                                \tag{1}
$$



where



$$
L_k=\operatorname{lcm}(1,\ldots,k-1),
 \qquad
 h_{n,k}=\gcd(4T_{n,k},L_kC_0).                                           \tag{2}
$$



This note proves that the hoped-for bound



$$
\log h_{n,k}=O(n\log n)                                                   \tag{3}
$$



cannot hold uniformly for unrestricted $k>n$.  In fact there is a forced
squarefree divisor



$$
\boxed{
 \prod_{\substack{p\ \operatorname{prime}\\ (k-1)/2<p\leq 2(k-n-1)/3}}p
 \ \mid\ h_{n,k}.}                                                          \tag{4}
$$



Consequently, whenever $n=o(k)$, the prime number theorem gives



$$
\log h_{n,k}\geq\left(\frac16+o(1)\right)k.                                \tag{5}
$$



For example, along even $n$ and $k=n^2$,



$$
\log h_{n,n^2}\geq\left(\frac16+o(1)\right)n^2,
$$



which is not $O(n\log n)$.  Combined with the already proved bound



$$
h_{n,k}\leq L_kC_0\leq64^{k-1}\gamma^n,
 \qquad \gamma=\frac{1+\sqrt2}{2},                                          \tag{6}
$$



this shows



$$
\log h_{n,k}=\Theta(k)
 \quad\text{whenever }n=o(k),                                                \tag{7}
$$



with absolute implied constants along every such sequence.

Two further exact $2$-adic statements are proved below.  Write



$$
n=2r,\qquad K=k-1,
$$



and let $s_2(K)$ denote the sum of the binary digits of $K$.  Then



$$
\boxed{
 v_2(C_0)=r+s_2(K)+(r\bmod 2)v_2(K),
 \qquad 2^K\mid T_{n,k}.}                                                   \tag{8a}
$$



Both assertions hold in every admissible degree $K\geq2r$; neither is a
finite-data conjecture.  The first comes from an exact super-Catalan formula
and a coefficientwise $2$-adic argument.  The second comes from a
$\mathbb Q_2(i)$ line integral between the fourth roots of unity.

Formula (4) is a lower-divisibility theorem, not an exact formula for all of
$h_{n,k}$.  An exact local formula in terms of the rational/$\pi$ coordinate
ratio is proved in Section 3.  It also explains why primes larger than $k-1$
can occur; a finite exact example is



$$
h_{2,26}=37\,350\,144
 =2^8\,3^2\,13\,29\,43,                                                     \tag{8}
$$



so $43>k-1$ divides the content.  Thus neither $h_{n,k}\mid L_k$ nor a
prime-support restriction to primes below $k$ is valid.

## 2. Fourier notation

Put



$$
\ell=k-n-1,\qquad c=k-1=\ell+n,
$$



and



$$
P_n(y)=i^{-n}(y-1)^n\bigl((1+i)y+1-i\bigr)^n
 \in\mathbb Z[i][y].                                                        \tag{9}
$$



Then $\deg P_n=2n$ and the Fourier polynomial is



$$
G_{n,k}(y)=P_n(y)(1+y)^{2\ell}.                                             \tag{10}
$$



For $-(k-1)\leq m\leq k-1$,



$$
C_m=[y^{c+m}]G_{n,k}(y),
 \qquad C_{-m}=\overline{C_m}.                                               \tag{11}
$$



Write $C_m=A_m+iB_m$ for $m>0$, and define



$$
N_m=A_m\sin\frac{m\pi}{2}
     -B_m\left(1-\cos\frac{m\pi}{2}\right)\in\mathbb Z.                   \tag{12}
$$



The rational Fourier coordinate is



$$
S_{n,k}:=\sum_{m=1}^{k-1}\frac{N_m}{m}
 =\frac{T_{n,k}}{L_k}.                                                       \tag{13}
$$



Equation (1) is equivalently



$$
J_{n,k}=2^{-(2k-2)}\left(S_{n,k}+\frac{C_0}{4}\pi\right).                 \tag{14}
$$



## 3. Exact ratio, residue, and prime-power valuation formulas

### 3.1 The reduced coordinate ratio

The primitive integer pair in (1) is



$$
\left(\frac{4T_{n,k}}{h_{n,k}},
       \frac{L_kC_0}{h_{n,k}}\right).
$$



Therefore, if



$$
z_{n,k}:=\frac{4S_{n,k}}{C_0}
          =\frac{4T_{n,k}}{L_kC_0}
          =\frac{a_{n,k}}{b_{n,k}},
 \qquad \gcd(a_{n,k},b_{n,k})=1,\ b_{n,k}>0,                               \tag{15}
$$



then



$$
\boxed{
 b_{n,k}=\frac{L_kC_0}{h_{n,k}},
 \qquad
 h_{n,k}=\frac{L_kC_0}{\operatorname{den}(z_{n,k})}.}                        \tag{16}
$$



Thus the content problem is exactly the denominator problem for the ratio of
the rational coordinate to the coefficient multiplying $\pi/4$.

For a prime $p$, use the normalized valuation $v_p(p)=1$, also on
rationals, with the convention $v_p(0)=+\infty$, and put



$$
\lambda_p=v_p(L_k),\quad
 \sigma_p=v_p(S_{n,k}),\quad
 c_p=v_p(C_0),\quad
 \varepsilon_p=v_p(4).
$$



Since $T_{n,k}=L_kS_{n,k}$, equation (2) gives the exact prime-power
classification



$$
\boxed{
 v_p(h_{n,k})
 =\lambda_p+\min\bigl(\varepsilon_p+\sigma_p,c_p\bigr).}                    \tag{17}
$$



Equivalently,



$$
v_p(b_{n,k})
 =\max\bigl(0,c_p-\varepsilon_p-\sigma_p\bigr).                             \tag{18}
$$



Equations (17)--(18) include primes not dividing $L_k$.  For such a prime,
$\lambda_p=0$, and extra content occurs precisely when the scaled rational
coordinate and $C_0$ share positive $p$-adic valuation.  This is the
mechanism behind the factor 43 in (8).

### 3.2 Hermite reduction and the residue at $i$

Let



$$
f_{n,k}(x)=\frac{x^n(1-x)^n}{(1+x^2)^k}.
$$



The previously proved Fourier formula shows that the logarithmic coordinate is
zero.  Hermite reduction therefore gives a unique $\omega_{n,k}\in\mathbb Q$ and
$Q_{n,k}\in\mathbb Q[x]$, with $\deg Q_{n,k}\leq2k-3$, such that



$$
f_{n,k}(x)
 =\frac{\omega_{n,k}}{1+x^2}
  +\frac{d}{dx}\left(\frac{Q_{n,k}(x)}{(1+x^2)^{k-1}}\right).                \tag{19}
$$



After clearing the denominator, (19) is the exact polynomial identity



$$
x^n(1-x)^n
 =\omega_{n,k}(1+x^2)^{k-1}
 +(1+x^2)Q_{n,k}'(x)-2(k-1)xQ_{n,k}(x).                                     \tag{20}
$$



A derivative of a rational function has zero residue at every finite pole, so



$$
\omega_{n,k}=2i\operatorname*{Res}_{x=i}f_{n,k}(x).                         \tag{21}
$$



Integrating (19) from 0 to 1 gives



$$
J_{n,k}
 =\frac{\omega_{n,k}}4\pi
  +\frac{Q_{n,k}(1)}{2^{k-1}}-Q_{n,k}(0).                                   \tag{22}
$$



Comparison with (14) yields



$$
\omega_{n,k}=\frac{C_0}{2^{2k-2}},
 \qquad
 \frac{Q_{n,k}(1)}{2^{k-1}}-Q_{n,k}(0)
 =\frac{S_{n,k}}{2^{2k-2}}.                                                  \tag{23}
$$



Consequently



$$
z_{n,k}
 =4\,
 \frac{Q_{n,k}(1)/2^{k-1}-Q_{n,k}(0)}
      {2i\operatorname*{Res}_{x=i}f_{n,k}(x)}.                              \tag{24}
$$



This is the requested residue/endpoint interpretation of the full content.
It is exact, but it also shows the difficulty of an all-prime closed formula:
one must control common prime powers between a high-order residue at $i$ and
the two rational endpoint values of the Hermite remainder.

As a concrete residue check, when $n=2$ one obtains for every $k\geq3$



$$
C_0
 =\frac{(2k-2)\binom{2k-2}{k-1}}
        {(2k-5)(2k-3)}.                                                      \tag{25}
$$



One proof expands $x^2(1-x)^2=x^2-2x^3+x^4$.  The odd moment is rational.
For



$$
I_r=\int_0^1\frac{x^{2r}}{(1+x^2)^k}\,dx,
$$



integration of the derivative of
$x^{2r-1}(1+x^2)^{1-k}$ shows that the coefficient of $\pi/4$ satisfies



$$
a_r=\frac{2r-1}{2k-2r-1}a_{r-1},
 \qquad
 a_0=\frac{\binom{2k-2}{k-1}}{4^{k-1}}.
$$



The coefficient for $I_1+I_2$, multiplied by $4^{k-1}$, is exactly
(25).  Formula (25) does not by itself determine $h_{2,k}$, because the
rational endpoint coordinate in (24) can contribute additional common primes,
as (8) illustrates.

## 4. The prime-band theorem

### Theorem

Let $n$ be positive and even, $k>n$, and let $p$ be a prime satisfying



$$
\frac{k-1}{2}<p\leq\frac{2(k-n-1)}3.                                       \tag{26}
$$



Then



$$
p\mid C_{-p},\qquad p\mid C_0,\qquad p\mid C_p,qquad
 p\mid N_p,qquad p\mid T_{n,k},qquad p\mid h_{n,k}.                       \tag{27}
$$



### Proof

Recall $c=k-1=\ell+n$.  Set



$$
r=c-p=\ell+n-p.
$$



The lower inequality in (26) gives $0<r<p$.  Since
$p>(\ell+n)/2>\ell/2$, while the upper inequality gives
$3p\leq2\ell$, there is a unique integer $s$ with



$$
2\ell=3p+s,
 \qquad 0\leq s<p.                                                         \tag{28}
$$



In the characteristic-$p$ ring $(\mathbb Z[i]/p\mathbb Z[i])[y]$,
Freshman's dream gives



$$
(1+y)^{2\ell}
 =(1+y)^{3p+s}
 \equiv(1+y)^s(1+y^p)^3\pmod p.                                             \tag{29}
$$



Let



$$
R(y)=P_n(y)(1+y)^s.
$$



Then



$$
\deg R\leq2n+s,
$$



and a direct subtraction using (28) yields



$$
r-(2n+s)
 =2p-\ell-n
 =2p-c>0.                                                                   \tag{30}
$$



Thus $\deg R<r<p$.  The right side of



$$
G_{n,k}(y)\equiv R(y)(1+y^p)^3\pmod p.                                   \tag{31}
$$



has support only in the four intervals



$$
[jp,jp+\deg R],\qquad j=0,1,2,3.
$$



The three exponents



$$
r=c-p,\qquad p+r=c,\qquad2p+r=c+p
$$



lie in the gaps immediately following the first three intervals.  Their
coefficients in $G_{n,k}$ therefore vanish modulo $p$.  By (11), these
coefficients are $C_{-p},C_0,C_p$, proving the first three divisibilities in
(27).  Since $N_p$ is an integer linear combination of the real and imaginary
parts of $C_p$, $p\mid N_p$.

Finally, $p>(k-1)/2$ implies $v_p(L_k)=1$, and $p$ is the only multiple
of $p$ in $1,\ldots,k-1$.  In



$$
T_{n,k}=\sum_{m=1}^{k-1}\frac{L_k}{m}N_m,
$$



every term with $m\ne p$ is divisible by $p$, while the $m=p$ term is
divisible by $p$ because $p\mid N_p$.  Hence $p\mid T_{n,k}$.  Also
$p\mid L_kC_0$, so (2) gives $p\mid h_{n,k}$. $\square$

Taking the product over all primes satisfying (26) proves (4).  Notice that the
argument proves more than is needed for the gcd: the same prime divides a
three-coefficient Fourier band $C_{-p},C_0,C_p$.

## 5. Asymptotic consequence and the failed uniform bound

Let



$$
\vartheta(x)=\sum_{p\leq x}\log p.
$$



Equation (4) gives the rigorous finite inequality



$$
\log h_{n,k}
 \geq
 \vartheta\!\left(\frac{2(k-n-1)}3\right)
 -\vartheta\!\left(\frac{k-1}2\right).                                      \tag{32}
$$



If $n=o(k)$, the prime number theorem $\vartheta(x)=x+o(x)$ turns (32)
into



$$
\begin{aligned}
 \log h_{n,k}
 &\geq
 \frac{2(k-n-1)}3-\frac{k-1}2+o(k)\\
 &=\frac{k-4n-1}{6}+o(k)
 =\left(\frac16+o(1)\right)k,
 \end{aligned}                                                             \tag{33}
$$



which is (5).  The prime band has positive length once $k>4n+1$, although a
particular short finite interval need not contain a prime.

Along $k=n^2$, equation (33) grows quadratically in $n$, disproving (3).
Together with (6), it also proves (7).  In the formerly critical regime
$k\asymp n\log n$, the forced content already has logarithm at least
$(1/6+o(1))k$; this is a genuine exponential cancellation in the primitive
$\pi$-coefficient.  The present theorem does not show that this cancellation
is sufficient for a successful $e+\pi$ construction, because it gives no
matching upper formula for all remaining prime powers in (17).

## 6. Exact $2$-adic structure

### 6.1 The central coefficient in every degree

Put $n=2r$ and $K=k-1$, so $K\geq2r$.  For nonnegative integers
$a,b$, define the super-Catalan integer



$$
\mathcal S(a,b)=
 \frac{(2a)!(2b)!}{a!b!(a+b)!}.                                           \tag{34}
$$



Expanding $(\cos t-\sin t)^{2r}$ in the full-period mean defining $C_0$
and observing that all odd mixed moments vanish gives



$$
\boxed{
 C_0=\sum_{j=0}^{r}\binom{2r}{2j}
       \mathcal S(r+j,K-r-j).}                                             \tag{35}
$$



Indeed,



$$
4^K\frac1{2\pi}\int_0^{2\pi}
 \sin^{2a}t\cos^{2b}t\,dt=\mathcal S(a,b)
 \quad(a+b=K),                                                             \tag{36}
$$



which proves (35) directly.  Legendre's formula
$v_2(m!)=m-s_2(m)$ gives, for $a+b=K$,



$$
v_2\bigl(\mathcal S(a,b)\bigr)=s_2(K).                                   \tag{37}
$$



The cancellation among the terms of (35) can also be determined exactly.
Normalize by its $j=0$ term.  A factorial cancellation gives



$$
\frac{\mathcal S(r+j,K-r-j)}{\mathcal S(r,K-r)}
 =\prod_{t=0}^{j-1}
   \frac{2r+1+2t}{2K-2r-1-2t}.                                            \tag{38}
$$



Define the odd polynomial



$$
D_r(K)=\prod_{t=0}^{r-1}
          \bigl(2K-(2r+1+2t)\bigr)                                       \tag{39}
$$



and the common numerator



$$
F_r(K)=D_r(K)\sum_{j=0}^{r}\binom{2r}{2j}
       \prod_{t=0}^{j-1}
       \frac{2r+1+2t}{2K-2r-1-2t}.                                       \tag{40}
$$



Although (40) is displayed as a rational expression, cancellation against
$D_r$ shows immediately that $F_r\in\mathbb Z[K]$.  We next prove the
stronger coefficientwise divisibility $2^r\mid F_r$ in $\mathbb Z[K]$.

Set $q=K-2r\geq0$, and, for an integer $a\geq0$, introduce the formal
series



$$
f_a(z)=\sum_{j\geq0}
 \frac{\prod_{t=0}^{j-1}(2a+1+2t)}{(2j)!}z^{2j}.
$$



The binomial convolution in (40) is exactly



$$
F_r(K)=(2r)![z^{2r}]f_r(z)f_q(z).                                        \tag{41}
$$



Formal differentiation of $e^{z^2/2}$, or direct coefficient comparison,
gives



$$
f_a(z)=e^{z^2/2}P_a(z),
 \qquad
 P_a(z)=\sum_{u=0}^{a}\binom au
          \frac{z^{2u}}{(2u-1)!!},                                        \tag{42}
$$



where $(-1)!!=1$.  Consequently



$$
\frac{F_r(K)}{2^r}
 =(2r-1)!!
 \sum_{\substack{u,v,w\geq0\\u+v+w=r}}
 \frac{r!}{w!}\binom ru\binom qv
 \frac1{(2u-1)!!(2v-1)!!}.                                                \tag{43}
$$



The apparently rational polynomial in (43) is coefficientwise $2$-integral.
Indeed, with falling factorials $x^{\underline v}$,



$$
\frac{r!}{w!}\binom qv
 =\binom rv(r-v)^{\underline u}q^{\underline v},
 \qquad w=r-u-v,                                                          \tag{44}
$$



and every remaining denominator in (43) is odd.  Since $F_r\in\mathbb Z[K]$,
this $2$-integrality proves $F_r/2^r\in\mathbb Z[K]$.  Write



$$
F_r(K)=2^rY_r(K),
 \qquad Y_r(K)\in\mathbb Z[K].                                           \tag{45}
$$



The $j=0$ term of (40) also shows that $Y_r$ is monic of degree $r$.

It remains to determine the parity of $Y_r(K)$.  Reduce (43)--(44) modulo
$2$.  The odd double factorials disappear.  If $r$ is even, evaluation at
$q=0$ leaves only $v=0$, and only $u=0$ survives because
$r^{\underline u}$ is even for $u\geq1$.  At $q=1$, only $v=0,1$
can occur, and the $v=1$ part contains the even factor $\binom r1$.
Since $q=K-2r$ has the same parity as $K$, this proves



$$
Y_r(0)\equiv Y_r(1)\equiv1\pmod2
 \quad(r\ {\rm even}).                                                    \tag{46}
$$



Because a polynomial over $\mathbb F_2$ has the same value at every pair of
integers of the same parity, (46) says that $Y_r(K)$ is odd for every
integer $K$.

Suppose now that $r$ is odd.  Substitution $K=0$ in (38) makes its
$j$-th product equal to $(-1)^j$.  Hence



$$
\frac{F_r(0)}{D_r(0)}
 =\sum_{j=0}^{r}(-1)^j\binom{2r}{2j}
 =2^r\cos\frac{r\pi}{2}=0.                                                \tag{47}
$$



It follows from (45) that $Y_r(K)=KZ_r(K)$ with $Z_r\in\mathbb Z[K]$.
The same reduction of (43) at $q=1$ leaves, after the cancelling $v=0$
part, only the term $v=1,u=0$; therefore $Y_r(1)\equiv1\pmod2$.
For even $K$, it remains to check $Z_r(0)=Y_r'(0)$.  Since the shift
$q=K-2r$ is even, its reduction and its derivative at $K=0$ may be
computed at $q=0$.  In the derivative of $q^{\underline v}$, only
$v=1,2$ can contribute modulo $2$.  The $v=1,u=0$ term contributes
$1$, all its $u\geq1$ terms vanish, and the $v=2$ terms with
$u=0,1$ have equal parity and cancel; its terms with $u\geq2$ vanish.
Thus $Y_r'(0)\equiv1\pmod2$.  We have proved



$$
Y_r(K)=
 \begin{cases}
  \text{an odd integer},&r\text{ even},\\
  K\,Z_r(K),\quad Z_r(K)\text{ odd},&r\text{ odd}.
 \end{cases}                                                              \tag{48}
$$



Combining (37)--(40), (45), and (48), and noting that $D_r(K)$ is odd,
proves the exact all-degree formula



$$
\boxed{
 v_2(C_0)=s_2(K)+r+(r\bmod2)v_2(K).}                                      \tag{49}
$$



### 6.2 A fourth-root line integral and $2^K\mid T_{n,k}$

Let $E=\mathbb Q_2(i)$, normalize its valuation by $v_2(2)=1$, and put
$\delta=i-1$, so $v_2(\delta)=1/2$.  The $2$-adic logarithm converges at
$i=1+\delta$, and $\log i=0$ because $i$ is torsion.  Therefore the
finite Laurent expansion (11), integrated term by term from $1$ to $i$,
gives



$$
\frac1{2i}\int_1^i y^{-K-1}G_{n,k}(y)\,dy=S_{n,k}.                        \tag{50}
$$



For completeness, the $m=0$ term on the left is $C_0\log i=0$.  Pairing
the $m$ and $-m$ terms for $m>0$ gives



$$
\frac1{2i m}
 \left(C_m(i^m-1)-\overline{C_m}(i^{-m}-1)\right)
 =\frac{N_m}{m},                                                           \tag{51}
$$



which proves (50) with exactly the sign convention of (12).

Parametrize the $2$-adic line segment by $y=1+\delta t$, $0\leq t\leq1$
in the rigid-analytic sense.  The three polynomial factors satisfy



$$
y-1=\delta t,\qquad
 (1+i)y+1-i=2(1-t),\qquad
 1+y=\delta(t-1-i).                                                        \tag{52}
$$



Since $n=2r$, $\ell=K-n$, and $dy=\delta\,dt$, equations (9)--(10) give



$$
\int_1^i y^{-K-1}G_{n,k}(y)\,dy
 =u\,\delta^{\,2K+n+1}
 \int_0^1
 t^n(1-t)^n(t-1-i)^{2\ell}
 (1+\delta t)^{-K-1}\,dt,                                                 \tag{53}
$$



where $u$ is a $2$-adic unit.  Thus the explicit factor in (53) has
valuation



$$
v_2\bigl(\delta^{2K+n+1}\bigr)=K+r+\frac12.                              \tag{54}
$$



We record the elementary denominator estimate needed for the remaining
integral.  Put $a=\lfloor\log_2K\rfloor$.  For every $\nu\geq0$ and
$0\leq j\leq2K$,



$$
\frac \nu2+v_2\binom{K+\nu}{\nu}-v_2(\nu+j+1)\geq-(a+1).                 \tag{55}
$$



For $\nu=0$, this follows from $\nu+j+1\leq2K+1<2^{a+2}$.
For $\nu\geq2$,
one may discard the nonnegative binomial valuation: otherwise a violation
would force



$$
2^{a+2+\lfloor \nu/2\rfloor}
 \leq \nu+j+1\leq \nu+2K+1
 \leq \nu+2^{a+2}-1,
$$



contrary to the elementary strict reverse inequality for
$a\geq1,\nu\geq2$.  For $\nu=1$, the only extra case is
$\nu+j+1=2^{a+2}$, which forces
$K=2^{a+1}-1$ and is compensated by
$v_2\binom{K+1}{1}=a+1$.  This proves (55).

Write the polynomial in (53) as



$$
t^n(1-t)^n(t-1-i)^{2\ell}=\sum_{j=0}^{2K}p_jt^j,
 \qquad p_j\in\mathbb Z_2[i],                                            \tag{56}
$$



and use the uniformly convergent expansion



$$
(1+\delta t)^{-K-1}
 =\sum_{\nu\geq0}(-1)^\nu
   \binom{K+\nu}{\nu}\delta^\nu t^\nu.                                    \tag{57}
$$



Termwise integration contributes the denominator $\nu+j+1$.  Equations
(55)--(57) therefore show that the last integral in (53) has valuation at
least $-(a+1)$.  The terms tend $2$-adically to zero, so the same estimate
also justifies the termwise rigid-analytic integration.

Finally, (50), (53), and (54), including the factor $1/(2i)$, give



$$
v_2(S_{n,k})\geq K+r-a-\frac32\geq K-a-\frac12.                           \tag{58}
$$



The number $S_{n,k}$ is rational, so its normalized $2$-adic valuation is
an integer.  Hence



$$
v_2(S_{n,k})\geq K-a.
$$



Since $T_{n,k}=L_kS_{n,k}$ and $v_2(L_k)=a$, this proves



$$
\boxed{2^K\mid T_{n,k}.}                                                  \tag{59}
$$



### 6.3 Primitive and fully matched consequences

The two exact $2$-adic results remove the complete power of $2$ from the
primitive $\pi$-coefficient, but they do not control its odd part.  Indeed,
put $a=\lfloor\log_2K\rfloor$.  The elementary inequality



$$
a+r+s_2(K)+(r\bmod2)v_2(K)\leq K+2                                      \tag{60}
$$



holds for every $K\geq2r$.  Here is a proof for completeness.  If $r$ is
even, $r\leq K/2$, and $a+s_2(K)\leq K/2+2$: write
$K=2^a+m$ and use $s_2(m)\leq m/2+1$ for $m>0$, with $m=0$
immediate.  If $r$ is odd, write $K=2^vu$, with $u$ odd.  For $v=0$,
use $r\leq(K-1)/2$ and $s_2(m)\leq(m+1)/2$ for the odd
$m=K-2^a$.  For $v=1$, the required estimate reduces to
$\lfloor\log_2u\rfloor+s_2(u)\leq u$.  For $v\geq2$, one has
$r\leq K/2-1$, while, with $b=\lfloor\log_2u\rfloor$,


$$
a+s_2(K)+v\leq2b+2v+1
 \leq2^{b+v-1}+3\leq K/2+3.
$$


These estimates prove (60).

Equations (49), (59), and (60) imply



$$
v_2(L_kC_0)\leq v_2(4T_{n,k}).
$$



The definition (2) of $h_{n,k}$ therefore gives



$$
\boxed{
 v_2(h_{n,k})=v_2(L_kC_0),\qquad
 B_{n,k}:=\frac{L_kC_0}{h_{n,k}}\ \text{is odd}.}                          \tag{61}
$$



Now let $q_ne-p_n$ be the primitive beta-integral $e$-form used in the
matched construction.  Its elementary two-step recurrence shows that both
$p_n$ and $q_n$ are odd.  Put



$$
d=\gcd(q_n,B_{n,k}),\qquad
 q_n=dq_0,\qquad B_{n,k}=dB_0,
$$



and let



$$
M=-B_0p_n+q_0A_{n,k},\qquad
 C=\frac{q_nB_{n,k}}d=dq_0B_0                                             \tag{62}
$$



be the constant and common $e,\pi$ coefficients of the raw matched form.
The standard reduction modulo primes dividing $q_0B_0$ proves
$\gcd(M,q_0B_0)=1$.  Hence the final content has the exact description



$$
\boxed{g_{n,k}=\gcd(M,C)=\gcd(M,d).}                                     \tag{63}
$$



In particular $d$ and $g_{n,k}$ are odd, so no hidden power of $2$
is lost at the final matching stage.  There is, however, no bound here for
their odd parts.  This is a genuine remaining obstruction, not merely a
logical possibility.  At $n=2,k=10$, exact arithmetic gives



$$
(A_{2,10},B_{2,10})=(-149056,135135),\qquad
 (p_2,q_2)=(19,7),\qquad d=g_{2,10}=7.                                   \tag{64}
$$



Thus divergence or a lower bound for the primitive $\pi$-form alone cannot
be promoted to the fully primitive matched $e+\pi$-form without controlling
the odd gcd in (63).

## 7. Exact diagnostic validation

The independent script

    scripts/critical_fourier_content_prime_band_probe.py

uses exact Gaussian-integer polynomial arithmetic.  For every even
$2\leq n\leq20$ and every $n+1\leq k\leq160$, it verifies:

1. the three coefficient divisibilities in (27) for every prime in (26);
2. $p\mid N_p,T_{n,k},h_{n,k}$;
3. the full squarefree product in (4) divides $h_{n,k}$;
4. the global exact identity
   $\operatorname{den}(4T/(L_kC_0))=L_kC_0/h_{n,k}$;
5. the super-Catalan identity (35), the valuation formula (49), and
   $2^{k-1}\mid T_{n,k}$;
6. the primitive parity conclusion (61) and the exact warning example (64).

This box contains 1,490 cases and 2,495 forced-prime incidences.  The script also
records the exact contents along $k=n^2$ for even $2\leq n\leq30$.  These
calculations are diagnostics only; the proof of (4) and the asymptotic
counterexample use no finite computation.

## 8. What is and is not classified

The following statements are now proved:

* the exact denominator identity (16);
* the exact all-prime valuation formulas (17)--(18);
* the residue/endpoint representation (24);
* the forced prime band (4), including its three Fourier-coefficient source;
* the exact central valuation (49) and the exact divisibility (59);
* complete removal of the $2$-part in (61), and the exact final-content
  identity (63);
* failure of every uniform $O(n\log n)$ upper bound when $k$ is
  unrestricted;
* the correct coarse order $\log h_{n,k}=\Theta(k)$ for $n=o(k)$.

What remains unproved is a closed formula, or a sharp upper bound below (6), for
the residual valuations $\sigma_p=v_p(S_{n,k})$ in (17).  In particular,
primes arising simultaneously from the residue coordinate $C_0$ and the
Hermite endpoint coordinate can exceed $k$, as (8) proves.  Finite data are
not used to conjecture these residual valuations away.  Equally importantly,
the present results give no useful uniform upper bound for the odd matching
gcd $d$ or the odd final content $g_{n,k}$ in (63).  Consequently this
note closes the $2$-adic and primitive-$\pi$ arithmetic, but it does not
establish divergence for the fully primitive matched $e+\pi$ forms in the
unrestricted high-$k$ regime.
