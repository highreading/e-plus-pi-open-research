> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Laguerre squares in the common kernel: exact parametrization and the factorial--gcd barrier

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
s=e+\pi,\qquad w=1-i,
$$



and let $L_k$ denote the standard Laguerre polynomial, normalized by



$$
\int_0^\infty e^{-t}L_j(t)L_k(t)\,dt=\delta_{jk}.
\tag{1}
$$



There is a lossless rational parametrization of every square residual



$$
F(x)=q(1-x)^2,
 \qquad q\in\mathbb Q[t],
\tag{2}
$$



which satisfies the common endpoint equality



$$
A(F)=F(i)=F(-i),
 \qquad
 A(F)=\int_0^\infty e^{-t}F(1-t)\,dt.
\tag{3}
$$



Write



$$
q=\sum_{k=0}^n c_kL_k,
 \quad
 u_k=\operatorname {Re}L_k(w),
 \quad
 v_k=\operatorname {Im}L_k(w).
\tag{4}
$$



For a rational vector $d=(d_0,\ldots,d_n)$, put



$$
d_0=0,qquad v\mathbin\cdot d=0,qquad
 U=u\mathbin\cdot d,qquad
 \Delta=d\mathbin\cdot d-U^2.
\tag{5}
$$



Then every choice with $U\ne0$ gives a nonconstant solution through



$$
\boxed{c=\rho\{\Delta e_0+2Ud\},\qquad \rho\in\mathbb Q^*.}
\tag{6}
$$



Conversely, every nonconstant rational solution occurs in (6).  Since
$v_1=1$, one may take $d_2,\ldots,d_n$ freely and set



$$
d_1=-\sum_{k=2}^n v_kd_k.
\tag{7}
$$



After clearing (6) to a primitive polynomial $Q\in\mathbb Z[t]$, put



$$
m=Q(w)\in\mathbb Z.
\tag{8}
$$



The common coefficient is $m^2$, and an exact output formula is



$$
\boxed{
 I_Q:=\int_0^1Q(1-x)^2
       \left(e^x+\frac4{1+x^2}\right)dx
     =m^2s-b_Q>0,}
\tag{9}
$$



where



$$
\begin{aligned}
 R_Q(t)&=\frac{Q(t)^2-m^2}{t^2-2t+2}\in\mathbb Z[t],\\
 T_Q&=\int_0^\infty e^{-u}Q(1+u)^2\,du\in\mathbb Z,\\
 b_Q&=T_Q-4\int_0^1R_Q(t)\,dt\in\mathbb Q.
 \end{aligned}
\tag{10}
$$



If $b_Q=B/D$ in lowest terms, $D>0$, and



$$
g=\gcd(B,m^2),
\tag{11}
$$



then the primitive integer output pair is exactly



$$
\boxed{
 (\alpha,\beta)=
 \left(\frac{Dm^2}{g},\frac Bg\right),
 \qquad
 \alpha=\operatorname {den}\left(\frac{b_Q}{m^2}\right).}
\tag{12}
$$



Thus



$$
\alpha s-\beta=\frac Dg I_Q
                =\alpha\frac{I_Q}{m^2}>0.
\tag{13}
$$



Since $\deg R_Q\le2n-2$, formula (10) also gives the elementary
denominator restriction



$$
D\mid\operatorname {lcm}(1,2,\ldots,2n-1).
\tag{13a}
$$



This exposes the precise arithmetic issue.  If $n=\deg Q$, then



$$
|m|\ge n!,
\tag{14}
$$



so the unnormalized coefficient has factorial-square size.  Nevertheless,
the gcd in (11) can in principle cancel most or all of that size.  A
Bernstein--Walsh and Markov argument below gives the rigorous lower bound



$$
\boxed{
 \frac{I_Q}{m^2}\ge
 \frac{3}{16n^2C^{2n}},
 \qquad
 C=4.61158178930871498088\ldots .}
\tag{15}
$$



Consequently any sequence of primitive forms from this construction which
tends to zero must exhibit factorial-scale exceptional gcd growth:



$$
\frac{g\,n^2C^{2n}}{D m^2}\longrightarrow\infty.
\tag{16}
$$



No such gcd construction, and no upper bound excluding it, is proved here.
The exact parametrization is therefore a new local tool and (16) is an exact
obstruction, but this note does **not** prove irrationality or transcendence
of $e+\pi$.

## 2. Laguerre reduction of the common endpoint conditions

The standard polynomials are



$$
L_k(t)=\sum_{j=0}^k(-1)^j\binom kj\frac{t^j}{j!}.
\tag{17}
$$



Their Rodrigues formula and $k$ integrations by parts prove (1).  Hence,
for (2) and (4),



$$
A(F)=\int_0^\infty e^{-t}q(t)^2\,dt
     =\sum_{k=0}^n c_k^2.
\tag{18}
$$



Also



$$
F(i)=q(w)^2,
 \qquad
 q(w)=(u+iv)\mathbin\cdot c.
\tag{19}
$$



The coefficients of $q$ are real.  If $q\ne0$, then the left side of
(18) is positive.  The condition that $q(w)^2$ equal this positive real
number first forces $q(w)$ to be real: the only other way a complex square
can be real is for its base to be purely imaginary, in which case the square
is nonpositive.  Thus (3) is equivalent to



$$
\boxed{v\mathbin\cdot c=0,qquad
        c\mathbin\cdot c=(u\mathbin\cdot c)^2.}
\tag{20}
$$



Indeed, the first equation makes $q(w)$ real, the second identifies its
square with (18), and conjugation then gives the equality at $-i$.

The constant vector $e_0=(1,0,\ldots,0)$ is a rational point of (20),
because $L_0=1$.  Formula (6) is the stereographic parametrization of this
rational quadric, with the apparent tangent exception removed by positivity.

## 3. Proof that the parametrization is lossless

Let $d$ satisfy (5), let $c$ be the expression in braces in (6), and
temporarily take $\rho=1$.  Since $u_0=1$ and $v_0=0$,



$$
v\mathbin\cdot c=0,
\tag{21}
$$



and



$$
u\mathbin\cdot c=\Delta+2U^2=d\mathbin\cdot d+U^2.
\tag{22}
$$



Because $d_0=0$,



$$
\begin{aligned}
 c\mathbin\cdot c
 &=\Delta^2+4U^2(d\mathbin\cdot d)\\
 &=\{d\mathbin\cdot d+U^2\}^2.
 \end{aligned}
\tag{23}
$$



Equations (21)--(23) prove (20).  Multiplication by $\rho$ preserves the
homogeneous equations.

For the converse, let $c\in\mathbb Q^{n+1}$ be a nonconstant solution of
(20) and put



$$
r=u\mathbin\cdot c,qquad
 d=c-c_0e_0,qquad
 U=u\mathbin\cdot d=r-c_0.
\tag{24}
$$



If $U=0$, then (20) gives



$$
\sum_{k=1}^n c_k^2=r^2-c_0^2=0.
\tag{25}
$$



Over $\mathbb R$, this forces every $c_k$, $k\ge1$, to vanish,
contrary to nonconstancy.  Therefore $U\ne0$.  Moreover,



$$
d\mathbin\cdot d-U^2
 =(r^2-c_0^2)-(r-c_0)^2=2c_0U.
\tag{26}
$$



Substitution in the right side of (6) now gives



$$
\Delta e_0+2Ud=2Uc.
\tag{27}
$$



Taking $\rho=(2U)^{-1}$ recovers the original vector.  This proves the
claimed surjectivity.  Finally,



$$
L_1(w)=1-w=i,
\tag{28}
$$



so $v_1=1$ and (7) is an explicit rational parametrization of the
hyperplane in (5).

## 4. Integral clearing and the factorial endpoint coefficient

Clearing the monomial coefficients of a rational $q$, and then dividing by
their gcd, gives a primitive $Q\in\mathbb Z[t]$.  The two equations (20)
are homogeneous, so they survive this normalization.

The inverse change from monomials to Laguerre polynomials is integral:



$$
\boxed{
 t^j=j!\sum_{k=0}^j(-1)^k\binom jkL_k(t).}
\tag{29}
$$



It follows either by substituting (17) and applying binomial inversion, or by
checking coefficients.  Thus, if



$$
Q(t)=\sum_{j=0}^na_jt^j=\sum_{k=0}^nc_kL_k(t),
\tag{30}
$$



then every $c_k$ is an integer.  Since $Q\in\mathbb Z[t]$ and
$w\in\mathbb Z[i]$, equation (20) also gives



$$
m=Q(w)\in\mathbb Z[i]\cap\mathbb R=\mathbb Z,
 \qquad
 m^2=\sum_{k=0}^nc_k^2.
\tag{31}
$$



A nonzero solution has $m\ne0$.  At the leading coefficient,



$$
c_n=(-1)^n n!a_n.
\tag{32}
$$



For a degree-$n$ integer polynomial, $|a_n|\ge1$.  Equations
(31)--(32) prove the factorial lower bound (14).

## 5. Exact rational output and primitive normalization

Change variables $t=1-x$ in the exponential part of (9).  Equation (31)
gives



$$
\begin{aligned}
 \int_0^1e^xQ(1-x)^2\,dx
 &=e\int_0^1e^{-t}Q(t)^2\,dt\\
 &=em^2-e\int_1^\infty e^{-t}Q(t)^2\,dt\\
 &=em^2-T_Q.
 \end{aligned}
\tag{33}
$$



The last equality follows from $t=1+u$.  Expanding the integer polynomial
$Q(1+u)^2$ and using



$$
\int_0^\infty e^{-u}u^j\,du=j!
\tag{34}
$$



proves $T_Q\in\mathbb Z$.

Both $w$ and $\bar w$ are roots of $Q(t)^2-m^2$.  Their monic minimal
polynomial is



$$
H(t)=(t-w)(t-\bar w)=t^2-2t+2.
\tag{35}
$$



Monic division therefore proves $R_Q\in\mathbb Z[t]$.  On the rational
kernel side,



$$
\begin{aligned}
 4\int_0^1\frac{Q(1-x)^2}{1+x^2}\,dx
 &=4\int_0^1\frac{Q(t)^2}{H(t)}\,dt\\
 &=m^2\pi+4\int_0^1R_Q(t)\,dt.
 \end{aligned}
\tag{36}
$$



Adding (33) and (36) proves (9)--(10).

Write $b_Q=B/D$ in lowest terms.  Multiplication of (9) by $D$ gives
the integer pair $(Dm^2,B)$.  Because $\gcd(B,D)=1$,



$$
\gcd(Dm^2,B)=\gcd(m^2,B)=g.
\tag{37}
$$



Division by $g$ proves (12)--(13).  In particular, the coefficient
$\alpha$ is not a proxy based on polynomial height: it is exactly the
reduced denominator of the rational output ratio $b_Q/m^2$.
Moreover, $R_Q$ has degree at most $2n-2$, so integrating its integer
monomials proves (13a).

## 6. A rigorous analytic lower bound and the necessary gcd growth

Let $n=\deg Q\ge1$ and



$$
S=\max_{0\le t\le1}|Q(t)|.
\tag{38}
$$



Scale the interval to $[-1,1]$, and put



$$
z_0=2w-1=1-2i,
 \qquad
 \Phi=z_0+\sqrt{z_0^2-1},
\tag{39}
$$



where the square-root sign is chosen so that $|\Phi|>1$.  Define



$$
C=|\Phi|=4.61158178930871498088\ldots .
\tag{40}
$$



For completeness, the Bernstein--Walsh estimate needed here has a short
one-variable proof.  If $P(z)=Q((z+1)/2)$ and



$$
G(\zeta)=\zeta^nP\left(\frac{\zeta+\zeta^{-1}}2\right),
\tag{41}
$$



then $G$ is a polynomial.  On $|\zeta|=1$, its modulus is at most
$S$.  Since $z_0=(\Phi+\Phi^{-1})/2$, the maximum-modulus principle at
$\zeta=\Phi^{-1}$ gives



$$
|m|=|Q(w)|\le C^nS.
\tag{42}
$$



Markov's inequality on $[0,1]$ is



$$
\max_{[0,1]}|Q'|\le2n^2S.
\tag{43}
$$



At a point where $|Q|=S$, one of the two adjacent intervals of length



$$
\delta=\frac1{4n^2}
\tag{44}
$$



lies in $[0,1]$.  Equations (43)--(44) show that $|Q|\ge S/2$ on that
interval.  The weight in the $t$-coordinate obeys



$$
e^{1-t}+\frac4{t^2-2t+2}\ge3
 \qquad(0\le t\le1).
\tag{45}
$$



It follows that



$$
I_Q\ge\frac{3S^2}{16n^2}.
\tag{46}
$$



Combining (42) and (46) proves (15).  Equations (12)--(15) also give the
fully arithmetic form



$$
\boxed{
 \alpha s-\beta
 \ge\frac{3Dm^2}{16n^2C^{2n}g}
 \ge\frac{3D(n!)^2}{16n^2C^{2n}g}.}
\tag{47}
$$



Therefore a sequence with $\alpha s-\beta\to0$ necessarily satisfies
(16).  Equivalently, the gcd must be at least



$$
\frac{D(n!)^2}{n^2C^{2n}}
\tag{48}
$$



times a factor tending to infinity.  This is the exact denominator/gcd
obstruction.  It explains why continuous minimization of $I_Q/m^2$ is not
arithmetic evidence: primitive normalization is controlled by (11), not by
the real norm alone.

## 7. Low-degree formulas and finite arithmetic diagnostics

Degree one has no nonconstant solution.  Indeed,
$L_1(w)=i$, so the imaginary equation in (20) kills the $L_1$
coefficient.

In degree two there is one nonconstant projective solution:



$$
(c_0,c_1,c_2)=(1,2,-2),
 \qquad
 Q(t)=1+2t-t^2.
\tag{49}
$$



It has



$$
m=3,qquad
 R_Q=t^2-2t-4,qquad
 T_Q=20,qquad
 b_Q=\frac{116}{3}.
\tag{50}
$$



Thus its primitive form is



$$
27(e+\pi)-116
 =42.21661101531863879\ldots .
\tag{51}
$$



Degree three already gives a one-parameter rational family.  Put



$$
d=(0,-r-z/3,r,z).
\tag{52}
$$



Up to the harmless scalar factor $9$, formula (6) gives



$$
\begin{aligned}
 Q_{r,z}(t)={}&9r^2-36rz-35z^2\\
 &+(18r^2+78rz+80z^2)t\\
 &-(9r^2+42rz+45z^2)t^2\\
 &+(3rz+5z^2)t^3.
 \end{aligned}
\tag{53}
$$



The constant degeneration is exactly $3r+5z=0$.  Otherwise,



$$
Q_{r,z}(w)=M=27r^2+36rz+35z^2>0,
\tag{54}
$$



and



$$
\frac{b_{Q_{r,z}}}{M^2}
 =\frac{N(r,z)}{15M^2},
\tag{55}
$$



where



$$
\begin{aligned}
 N(r,z)={}&46980r^4+188190r^3z+277227r^2z^2\\
           &+189840rz^3+92575z^4.
 \end{aligned}
\tag{56}
$$



Consequently the primitive coefficient is exactly



$$
\alpha(r,z)=\frac{15M^2}{\gcd(N(r,z),15M^2)}.
\tag{57}
$$



The certificate exhausts all primitive integer directions
$|r|,|z|\le500$, excluding (52)'s constant degeneration.  Among the
608,926 signed directions, the smallest $\alpha$ is $27$, and the
numerically smallest positive primitive form is the embedded degree-two
pair $(27,116)$.  This is an exact finite search; it is not an all-degree
bound.

The certificate also derives and checks the analogous three-parameter
quartics in degree four.  In the genuine-degree box
$|r|,|y|,|z|\le50$, $z\ne0$, it exhausts 848,084 signed primitive
directions.  The smallest coefficient is $819$; the numerically smallest
form in that box is



$$
847(e+\pi)-4535
 =428.3136862953661873\ldots .
\tag{58}
$$



Sparse all-degree directions through degree sixteen make the primitive
coefficient grow rapidly.  Those records are only diagnostics.  Neither
they nor continuous real optimization control the exceptional gcd in
(11).

## 8. Certificate and scope

The deterministic certificate is

    scripts/laguerre_square_common_kernel_certificate.py

and its frozen output is

    results/laguerre_square_common_kernel_certificate.json

It checks Laguerre orthogonality through degree twelve by exact factorial
moments, the forward and inverse parametrization on deterministic rational
samples through degree ten, integral clearing, the output formula, the
factorial coefficient bound, the degree-two identity, and the degree-three
and degree-four quartic formulas.  The parameter-box searches use exact
integer arithmetic.  Decimal values are explicitly diagnostic and are not
used in any proof.

The surviving question is now precise: construct an all-degree family for
which the gcd in (11) has the exceptional size required by (16), while the
reduced rational output approaches $e+\pi$; or prove that such gcd growth
cannot occur.  Neither conclusion is obtained here.
