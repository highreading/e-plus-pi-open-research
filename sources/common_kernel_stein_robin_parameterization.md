> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A Stein operator and the exact Robin lattice for common-kernel forms

Checked: 2026-08-27 UTC.

## 1. Verdict

Define



$$
A(F)=\sum_{k\geq0}(-1)^kF^{(k)}(1)
     =\int_0^\infty e^{-t}F(1-t)\,dt
\tag{1}
$$



for a polynomial $F$, and introduce the first-order operator



$$
\boxed{\mathcal TP=(1-x)P'(x)-xP(x).}
\tag{2}
$$



This operator gives an exact integral parameterization of the kernel:



$$
\boxed{A(\mathcal TP)=0,\qquad
 \mathcal T:\mathbb Z[x]\overset{\sim}{\longrightarrow}
       \{H\in\mathbb Z[x]:A(H)=0\}.}
\tag{3}
$$



Consequently every integer polynomial satisfying



$$
A(F)=F(i)=F(-i)=a\in\mathbb Z
\tag{4}
$$



has one and only one representation



$$
F=a+\mathcal TP,qquad P\in\mathbb Z[x],
\tag{5}
$$



where $P$ obeys the two real Robin conditions



$$
(1-i)P'(i)-iP(i)=0,qquad
 (1+i)P'(-i)+iP(-i)=0.
\tag{6}
$$



The full integer lattice in (6) is explicit. Put



$$
R_1=1+2x+x^3,qquad R_2=9x-x^2+4x^3.
\tag{7}
$$



Then



$$
\boxed{
 P=(1+x^2)^2Q+uR_1+vR_2,qquad
 Q\in\mathbb Z[x],\quad u,v\in\mathbb Z.}
\tag{8}
$$



Equations (5) and (8) are a lossless parameterization of the entire
integer common-kernel plane, not an ansatz.

There is also an exact output formula. Write



$$
G_P=\frac{\mathcal TP}{1+x^2}=\sum_{j\geq0}g_jx^j\in\mathbb Z[x].
\tag{9}
$$



Then



$$
\boxed{
 \int_0^1F(x)\left(e^x+\frac4{1+x^2}\right)dx
 =a(e+\pi)-a-P(0)+4\sum_{j\geq0}\frac{g_j}{j+1}.}
\tag{10}
$$



This turns the search for positive common-kernel forms into one integer
polynomial $Q$, two integers $u,v$, and the inequality
$a+\mathcal TP\geq0$ on $[0,1]$.

The parameterization also isolates a revealing near miss. The unconstrained
ODE $a+\mathcal TP=0$ has the entire solution



$$
P_*(x)=a\frac{e^{1-x}-1}{1-x}.
\tag{11}
$$



For every $N\geq1$, set



$$
a_N=N!,\qquad
 P_N(x)=N!\sum_{j=0}^{N-1}\frac{(1-x)^j}{(j+1)!}
       \in\mathbb Z[x].
\tag{12}
$$



The Taylor telescoping is exact:



$$
\boxed{a_N+\mathcal TP_N=(1-x)^N.}
\tag{13}
$$



Thus, before imposing (6), there is an elementary positive integer residual
whose weighted integral tends to zero. It fails the common endpoint
conditions by exactly



$$
\mathcal TP_N(i)=(1-i)^N-N!\ne0.
\tag{14}
$$



The missing step is therefore sharply localized: correct the two exterior
Robin data in (14), within the lattice (8), while retaining positivity and
decay after primitive output normalization. No such all-degree correction is
proved here. In particular, this note does not prove irrationality or
transcendence of $e+\pi$.

## 2. The Stein identity

For a polynomial $P$, put $h(t)=P(1-t)$. Equation (1) gives



$$
A(\mathcal TP)=
 \int_0^\infty e^{-t}\{-t h'(t)-(1-t)h(t)\}\,dt.
\tag{15}
$$



Integration by parts yields



$$
\int_0^\infty e^{-t}t h'(t)\,dt
 =\int_0^\infty e^{-t}(t-1)h(t)\,dt,
\tag{16}
$$



so (15) is zero. This proves the first assertion in (3).

The operator $\mathcal T$ is injective on polynomials. Indeed, a nonzero
solution of $\mathcal TP=0$ would be



$$
P(x)=c\frac{e^{-x}}{1-x},
\tag{17}
$$



which is not a polynomial. More arithmetically, if $P$ has degree $m$,
then $\mathcal TP$ has degree $m+1$, with leading coefficient the
negative of the leading coefficient of $P$.

For every $N\geq1$, the map



$$
\mathcal T:\mathbb Q[x]_{\leq N-1}\longrightarrow
 \ker(A:\mathbb Q[x]_{\leq N}\to\mathbb Q)
\tag{18}
$$



is therefore an injection between two $N$-dimensional spaces, hence an
isomorphism.

It is also integral in both directions. If
$H=\sum_{j=0}^Nh_jx^j\in\mathbb Z[x]$ lies in $\ker A$, solve
$\mathcal TP=H$ downward from the leading coefficient. The coefficient of
$x^{k+1}$ contains $-p_k$ plus integer combinations of already known
higher $p_j$'s. Thus every coefficient of $P$ is an integer. The
remaining constant discrepancy has $A$-value zero and is consequently
zero. This proves the integral bijection (3).

## 3. From endpoint evaluation to Robin data

Let $F$ satisfy (4). Then $H=F-a$ is an integer element of $\ker A$,
so (3) gives the unique $P\in\mathbb Z[x]$ in (5). The endpoint equations
are



$$
0=\mathcal TP(\pm i)
   =(1\mp i)P'(\pm i)\mp iP(\pm i),
\tag{19}
$$



which are (6). Conversely, (5)--(6) immediately imply (4).

Since $P$ has real coefficients, the two equations in (6) are conjugate.
Equivalently,



$$
1+x^2\mid\mathcal TP.
\tag{20}
$$



This proves that (9) has integer coefficients once the lattice in (6) is
identified.

## 4. Exact integer solution of the Robin congruence

Divide $P$ by the monic polynomial $(1+x^2)^2$:



$$
P=(1+x^2)^2Q+R,qquad Q\in\mathbb Z[x],\quad\deg R\leq3.
\tag{21}
$$



The first term in (21) has $\mathcal T$-image divisible by $1+x^2$.
Write



$$
R=\alpha+\beta x+\gamma x^2+\delta x^3.
\tag{22}
$$



Reduction modulo $1+x^2$ gives



$$
\mathcal TR\equiv
 2\beta+2\gamma-4\delta
 +x(-\alpha-\beta+3\gamma+3\delta).
\tag{23}
$$



It vanishes precisely when



$$
\gamma=\frac{2\alpha-\beta}{9},qquad
 \delta=\frac{\alpha+4\beta}{9}.
\tag{24}
$$



For integral coefficients this is equivalent to



$$
\alpha=u,quad \beta=2u+9v,quad
 \gamma=-v,quad\delta=u+4v,qquad u,v\in\mathbb Z.
\tag{25}
$$



Equations (21) and (25) prove (8). For reference,



$$
\frac{\mathcal TR_1}{1+x^2}=2-3x-x^2,qquad
 \frac{\mathcal TR_2}{1+x^2}=9-11x-4x^2.
\tag{26}
$$



For the free part one has



$$
\frac{\mathcal T((1+x^2)^2Q)}{1+x^2}
 =(1-x)\{4xQ+(1+x^2)Q'\}-x(1+x^2)Q.
\tag{27}
$$



This makes every coefficient in (9) explicit and integral.

## 5. The output coordinate

The exponential part of the integral has an exact boundary primitive:



$$
\frac d{dx}\{e^x(1-x)P(x)\}=e^x\mathcal TP(x).
\tag{28}
$$



Therefore



$$
\int_0^1 e^xF(x)\,dx=a(e-1)-P(0)
 =ae-a-P(0).
\tag{29}
$$



Equations (9) and (20) give



$$
\int_0^1\frac{4F(x)}{1+x^2}\,dx
 =a\pi+4\int_0^1G_P(x)\,dx
 =a\pi+4\sum_j\frac{g_j}{j+1}.
\tag{30}
$$



Adding (29) and (30) proves (10).

If an integer antiderivative is required, the least positive multiplier
which makes $D G_P$ the derivative of an integer polynomial is



$$
D_P=\operatorname {lcm}_{g_j\ne0}
       \frac{j+1}{\gcd(j+1,g_j)}.
\tag{31}
$$



Multiplying $F$ and $a$ by $D_P$ recovers the denominator-free form
used elsewhere in the archive. Formula (10) keeps the exact rational output
visible before that harmless common scaling.

## 6. Positive Taylor truncations and their exact failure

Equation (28) shows that the entire solution of
$a+\mathcal TP=0$, regular at $x=1$, is (11). Put $t=1-x$.
For a finite Taylor block,



$$
\mathcal T\left(\sum_{j=0}^{N-1}\frac{t^j}{(j+1)!}\right)
 =-1+\frac{t^N}{N!}.
\tag{32}
$$



Multiplication by $N!$ proves (12)--(13). The coefficients are integral
because $(j+1)!\mid N!$, and replacing $t$ by $1-x$ preserves
integrality. The residual is nonnegative on $[0,1]$, and



$$
0<\int_0^1(1-x)^N
 \left(e^x+\frac4{1+x^2}\right)dx
 \leq\frac{e+4}{N+1}\longrightarrow0.
\tag{33}
$$



But (13) at $x=i$ gives (14). For $N=1$, the two sides have different
moduli; for $N=2$, $(1-i)^2=-2i$; and for $N\geq3$,
$N!>2^{N/2}=|(1-i)^N|$. Thus (14) never vanishes.

There is a useful all-degree strengthening for positive Taylor blocks. Let
$w=1-i$, and suppose



$$
f(t)=\sum_{j=0}^Nc_jt^j,qquad c_j\in\mathbb Q_{\geq0},
\tag{34}
$$



is used as the residual polynomial $F(x)=f(1-x)$. If it satisfies the
common-kernel equality, then



$$
\sum_jc_jj!=A(F)=F(i)=\sum_jc_jw^j.
\tag{35}
$$



Taking real parts gives



$$
\sum_jc_j\{j!-\operatorname {Re}(w^j)\}=0.
\tag{36}
$$



The braces vanish for $j=0,1$ and are strictly positive for every
$j\geq2$. For $j=2$, this is immediate from $w^2=-2i$; for
$j\geq3$, use $j!>|w|^j=2^{j/2}$. Hence $c_j=0$ for all
$j\geq2$. The imaginary part of (35) then gives $-c_1=0$. Therefore



$$
\boxed{
 f(t)\text{ with nonnegative monomial coefficients satisfies (35)}
 \Longrightarrow f(t)=c_0.}
\tag{37}
$$



Thus no positive combination of the telescoping Taylor blocks can repair
the Robin defect. A successful positive residual must have signed monomial
coefficients while remaining nonnegative on $[0,1]$, or use a different
mechanism altogether.

The positive residual construction therefore fails for exactly the two
Robin constraints, not for lack of integrality, positivity, or decay. A
successful correction must use (8) without losing (33) after primitive
normalization. That is the exact surviving problem.

## 7. Certificate and scope

The deterministic symbolic certificate is

    scripts/common_kernel_stein_robin_certificate.py

and its frozen output is

    results/common_kernel_stein_robin_certificate.json

It checks the Stein identity, the integral inverse on exhaustive finite
coefficient boxes, the Robin remainder equations, the lattice basis (8),
the quotient formulas (26)--(27), the output-coordinate identity, and the
Taylor telescoping through degree 40. It also checks the strict coefficient
inequality behind (34)--(37) through degree 200. The all-degree assertions are the
symbolic proofs above; finite checks are not used as substitutes.

This parameterization is a new local tool for the positive common-kernel
search. It neither constructs an all-degree Robin correction nor determines
the arithmetic nature of $e+\pi$.
