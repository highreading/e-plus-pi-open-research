> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Period pullbacks for $\pi$: analytic radius versus Hermite--Padé arithmetic

Date: 2026-08-26

## Status and scope

This note investigates representations



$$
\pi=F(1)
$$



in which $F$ has rational or algebraic Taylor coefficients, is analytic in
a disk strictly larger than the unit disk, and might be paired with $e^z$
in a type-I Hermite--Padé construction.  The main constructive result is the
elementary logarithmic G-function



$$
\boxed{F(z)=4\arctan\!\frac{z}{2-z}
       =4\int_0^z\frac{dt}{t^2-2t+2}.}                 \tag{1}
$$



It has three useful properties simultaneously:

1. $F(1)=\pi$;
2. its Taylor series at zero has exact radius $\sqrt2>1$;
3. every exponential jet $F^{(k)}(0)$ is an integer.

Property 3 removes the quadratic *denominator-clearing* loss from the high
Hermite--Padé jet matrix.  It does **not** control the size of the primitive
integer kernel, the primitive endpoint pair, or the endpoint remainder.  The
elementary Hadamard bound is still $\exp(O(n^2\log n))$, and a finite exact
probe through degree 15 produces growing rather than small endpoint forms.
Consequently nothing in this note proves irrationality or transcendence of
$e+\pi$.

For comparison, the particularly clean beta/hypergeometric representation



$$
H(z)=3\,{}_2F_1\!\left(\frac12,\frac12;\frac32;\frac z4\right),
 \qquad H(1)=\pi,                                    \tag{2}
$$



has the larger exact radius 4 and exponentially bounded coefficient
denominators, but its $m$-th jet has reduced dyadic denominator exactly
$2^{3m}$.  This gives a precise analytic-radius/arithmetic tradeoff.

Theorems, finite experiments, and unverified future possibilities are
explicitly separated below.

For orientation, the principal constructions have the following different
strengths.  `Integral jets' means integrality of every derivative at zero,
which is the normalization naturally seen by the high Hermite--Padé matrix.

| function taking the value $\pi$ at 1 | exact/proved radius | coefficient field | jet arithmetic |
|---|---:|---|---|
| $4\arctan z$ | $1$ | $\mathbb Q$ | integral, but 1 is on the Taylor boundary |
| $16\arctan(z/5)-4\arctan(z/239)$ | $5$ | $\mathbb Q$ | growing 5- and 239-power denominators |
| $4\arctan(z/(2-z))$ | $\sqrt2$ | $\mathbb Q$ | **all jets integral** |
| $3\,{}_2F_1(\tfrac12,\tfrac12;\tfrac32;z/4)$ | $4$ | $\mathbb Q$ | reduced dyadic jet denominator $2^{3m}$ |
| Ramanujan reciprocal $16/S(z)$ | $>5$ proved | $\mathbb Q$ | exponential fixed-prime denominators; G-status unproved |

The Machin row is the already studied accelerated-arctangent model.  Its
larger analytic disk comes with destructive fixed-prime arithmetic.  Formula
(1) occupies the opposite point in this tradeoff: a more modest analytic
gain, but an integral high-jet matrix.

## 1. The integral-jet Möbius pullback

### Theorem 1

Let $F$ be defined by (1), with the branch at zero.  Then:

1. $F(1)=\pi$.
2. The Taylor series of $F$ at zero has exact radius $\sqrt2$.
3. If $\tau_k=F^{(k)}(0)$, then $\tau_k\in\mathbb Z$ for every
   $k\geq0$.  More precisely, with $q\geq0$,

   

$$
\begin{aligned}
   \tau_{4q+1}&=(-1)^q\frac{2(4q)!}{4^q},\\
   \tau_{4q+2}&=(-1)^q\frac{2(4q+1)!}{4^q},\\
   \tau_{4q+3}&=(-1)^q\frac{(4q+2)!}{4^q},\\
   \tau_{4q+4}&=0.                                  \tag{3}
   \end{aligned}
$$



4. $F$ is a rational-coefficient G-function.  If
   $F(z)=\sum_{k\geq0}c_kz^k$, then the first $N$ coefficients have a
   common denominator dividing

   

$$
2^{\lceil N/2\rceil}\operatorname{lcm}(1,2,\ldots,N)
   =\exp(O(N)).                                      \tag{4}
$$



#### Proof

Set $u=t/(2-t)$.  Direct differentiation gives



$$
\frac{du}{1+u^2}=\frac{dt}{t^2-2t+2}.
$$



As $t$ runs from 0 to 1, $u$ runs from 0 to 1.  Therefore



$$
F(1)=4\int_0^1\frac{du}{1+u^2}=4\arctan(1)=\pi.    \tag{5}
$$



The derivative is



$$
F'(z)=\frac4{z^2-2z+2}.                            \tag{6}
$$



Its two poles are $1+i$ and $1-i$, both of modulus $\sqrt2$.
They are genuine simple poles of $F'$, hence logarithmic singularities of
$F$.  There is no singularity closer to zero, proving the exact radius.

Write



$$
\frac1{z^2-2z+2}=\sum_{m\geq0}d_mz^m.             \tag{7}
$$



The coefficient recurrence, or partial fractions at $1\pm i$, gives



$$
d_{4q+r}=\frac{(-1)^q}{4^q}
 \begin{cases}
  1/2,&r=0,\\
  1/2,&r=1,\\
  1/4,&r=2,\\
  0,&r=3.
 \end{cases}                                        \tag{8}
$$



Since $\tau_k=4(k-1)!d_{k-1}$ for $k\geq1$, (8) is exactly (3).
For the first two nonzero residue classes, the even factors among
$1,\ldots,4q$ already give



$$
v_2((4q)!)\geq2q;
$$



for the third, $v_2((4q+2)!)\geq2q+1$.  These inequalities prove directly
that every quotient in (3) is integral, including all small cases.

Dividing (3) by $k!$ gives the ordinary Taylor coefficients



$$
\begin{aligned}
 c_{4q+1}&=(-1)^q\frac{2^{1-2q}}{4q+1},\\
 c_{4q+2}&=(-1)^q\frac{2^{1-2q}}{4q+2},\\
 c_{4q+3}&=(-1)^q\frac{2^{-2q}}{4q+3},\\
 c_{4q+4}&=0.                                      \tag{9}
 \end{aligned}
$$



Formula (4) follows.  The standard elementary Chebyshev estimate
$\log\operatorname{lcm}(1,\ldots,N)=O(N)$ may be obtained by bounding
the primes in $(x/2,x]$ with the central binomial coefficient and summing
over prime powers.  Formula (9) also bounds the numerator heights by
$\exp(O(k))$.  Finally (6) implies the differential equation



$$
(z^2-2z+2)F''(z)+(2z-2)F'(z)=0.                  \tag{10}
$$



Thus $F$ is holonomic over $\mathbb Q(z)$, has rational coefficients
of exponential height, and has exponentially bounded common denominators:
it is a G-function. $\square$

### Residue form and the period-eight signs

For checking signs independently, partial fractions give



$$
d_m=2^{-(m+1)/2}\sin\!\frac{(m+1)\pi}{4}.        \tag{11}
$$



Consequently



$$
\tau_k=4(k-1)!\,2^{-k/2}\sin\!\frac{k\pi}{4}.   \tag{12}
$$



Although (12) is written with square roots, its values are the rational
integers in (3).  Its sign pattern for $k\bmod8$ is



$$
(+,+,+,0,-,-,-,0),                               \tag{13}
$$



which supplies a convenient independent period-eight check on (3).

## 2. Exact effect on the endpoint-matched high-jet matrix

The following proposition is the main arithmetic reason that (1) is more
interesting than a mere change of analytic variable.

### Proposition 2

Fix $n\geq1$.  There exist polynomials $A,B,C\in\mathbb Q[z]$, not all
zero and of degree at most $n$, such that



$$
A(z)+B(z)e^z+C(z)F(z)=O(z^{3n+1}),               \tag{14}
$$



and



$$
C(1)=B(1).                                        \tag{15}
$$



The high-jet-plus-endpoint system determining $B,C$ is an integer matrix;
no factorial or power-of-two row clearing is required.  After an integral
choice of $B,C$, multiplication of the complete triple by $n!$ clears
all coefficients of $A$.  Hence the universal denominator-clearing cost is
at most



$$
n!=\exp(O(n\log n)),                              \tag{16}
$$



not a product of $2n$ row denominators of total logarithmic size
$\Theta(n^2)$.

At $z=1$, the cleared triple gives an integer linear form



$$
\widetilde A(1)+\widetilde B(1)(e+\pi).          \tag{17}
$$



No assertion is made that either integer in (17) is nonzero.

#### Proof

Write



$$
B(z)=\sum_{j=0}^n b_jz^j,\qquad
 C(z)=\sum_{j=0}^n c_jz^j.                         \tag{18}
$$



For $k\geq j$, Leibniz's rule gives



$$
\left.\frac{d^k}{dz^k}(z^je^z)\right|_{z=0}=(k)_j,
$$





$$
\left.\frac{d^k}{dz^k}(z^jF(z))\right|_{z=0}
 =(k)_j\tau_{k-j},                                \tag{19}
$$



where $(k)_j=k!/(k-j)!$.  Every number in (19) is an integer by
Theorem 1.  Use the $2n$ high jets



$$
k=n+1,n+2,\ldots,3n                              \tag{20}
$$



together with the endpoint row



$$
-\sum_{j=0}^n b_j+\sum_{j=0}^n c_j=0.            \tag{21}
$$



This is a homogeneous integer matrix with $2n+1$ rows and $2n+2$
columns, so it has a nonzero rational, hence after one projective clearing an
integral, kernel vector $(b,c)$.

For $0\leq k\leq n$, define the coefficient of $z^k$ in $A$ to be
minus the $k$-th derivative at zero of $Be^z+CF$, divided by $k!$.
The numerator is an integer by (19).  Since $k!\mid n!$, multiplication by
$n!$ clears every coefficient of $A$.  Equations (20) and the definition
of $A$ give (14), while (21) gives (15).  Evaluation at one, using
$F(1)=\pi$, proves (17). $\square$

### What Proposition 2 does and does not save

Let $M_n$ be the $(2n+1)\times(2n+2)$ integer matrix in the proof.  If it
has full row rank, a signed-maximal-minor vector generates its kernel.  A
typical entry satisfies the coarse bound



$$
|(k)_j\tau_{k-j}|
 \leq (3n)^n\,4(3n)!\qquad(k\leq3n).              \tag{22}
$$



Hadamard therefore gives only



$$
\log H(B,C)=O(n^2\log n).                         \tag{23}
$$



This is a **raw cofactor upper bound**, not a lower bound for the primitive
kernel and not a primitive endpoint-height theorem.  Maximal minors can have
a large common gcd, and the endpoint pair can have a further gcd not shared
by the polynomial coefficients.  In fact a large all-degree cofactor divisor
can be proved explicitly.

### Proposition 2A (forced common content of all maximal cofactors)

For an integer $r\geq0$, write



$$
\operatorname{odd}(r!)=\frac{r!}{2^{v_2(r!)}}.    \tag{23a}
$$



For $t\geq0$, put



$$
q_t=\left\lfloor\frac{t+1}{4}\right\rfloor,
 \qquad
 \delta_t=2q_t+1-s_2(q_t),
 \qquad
 D_t=2^{\delta_t}\operatorname{odd}(t!),           \tag{23b}
$$



where $s_2$ is the binary digit sum.  Also put



$$
\begin{aligned}
 \Lambda_n&=\left(\prod_{j=0}^{n-1}j!\right)^2,\\
 \Gamma_n&=\prod_{t=0}^{n-2}D_t,\\
 d_s&=\left\lfloor\frac{s-1}{4}\right\rfloor,
 &\epsilon_s&=2d_s-s_2(d_s),\\
 R_s&=2^{\epsilon_s}\operatorname{odd}((s-1)!),
 &\Omega_n^*&=\prod_{s=1}^{n-1}R_s.
 \end{aligned}                                      \tag{23c}
$$



Every signed maximal cofactor of the integer matrix $M_n$ is divisible by



$$
\boxed{\Xi_n=\Lambda_n\Gamma_n\Omega_n^*}.        \tag{23d}
$$



Empty products are one, and



$$
\log\Xi_n=2n^2\log n+O(n^2).                     \tag{23e}
$$



#### Proof

For a nonzero jet with $m=4q+r$, $r\in\{1,2,3\}$, formula (3) gives



$$
v_2(\tau_m)=2q+1-s_2(q).                          \tag{23f}
$$



The function on the right is strictly increasing in $q$: if $a$ is the
number of trailing ones in the binary expansion of $q$, its increment at
$q+1$ is $1+a$.  Also, division in (3) uses only powers of two, so



$$
\operatorname{odd}((m-1)!)\mid\tau_m.            \tag{23g}
$$



Delete one column of $M_n$, and expand the resulting square determinant
along its endpoint row.  Each term is a $2n$-by-$2n$ high determinant
in which exactly two columns of the original matrix have been omitted.

Every high entry in either column of degree $j$ contains the literal factor



$$
(k)_j=j!\binom{k}{j}.                             \tag{23h}
$$



If the two omitted columns have degree indices $r,s\in\{0,\ldots,n\}$,
the product of the retained factorial-column factors, divided by
$\Lambda_n$, is $(n!)^2/(r!s!)$, an integer.  Thus $\Lambda_n$ divides
each endpoint-expansion term.

Consider the high part of the column belonging to $c_j$, and set
$t=n-j$.  Its entries are



$$
(k)_j\tau_{k-j},\qquad n+1\leq k\leq3n.          \tag{23i}
$$



Here $m=k-j\geq t+1$.  The least possible $q$ among the nonzero jets is
$q_t=\lfloor(t+1)/4\rfloor$; if $t+1$ is a multiple of four, the first
jet is zero and the following jet has exactly that value of $q$.  Equations
(23f)--(23g) show, after the factor $j!$ in (23h) has been removed, that
every entry in this high $C$-column is still divisible by
$D_t$.  Zero entries cause no exception.

Each high determinant retains at least $n-1$ of the $n+1$ columns from
the $C$-block.  The divisors $D_t$ form a divisibility chain, so their
retained product is divisible by $D_0D_1\cdots D_{n-2}=\Gamma_n$.

It remains to inspect the residual integer after extracting $j!D_t$.  Put
$s=k-n$, so $1\leq s\leq2n$ and $k-j=s+t$.  For every odd prime $p$,
the residual $U_{k,j}$ satisfies



$$
\begin{aligned}
 v_p(U_{k,j})
 &=v_p\binom{k}{j}+v_p(\tau_{s+t})-v_p(t!)\\
 &\geq v_p((s+t-1)!)-v_p(t!)\\
 &\geq v_p((s-1)!).
 \end{aligned}                                      \tag{23j}
$$



For its dyadic valuation, set



$$
q_m=\left\lfloor\frac{s+t}{4}\right\rfloor,
 \qquad q_t=\left\lfloor\frac{t+1}{4}\right\rfloor.
$$



Writing $t+1=4q_t+r$ and $s-1=4d_s+a$, with $0\leq r,a<4$, gives
$q_m-q_t\geq d_s$.  The function
$\delta(q)=2q+1-s_2(q)$ is increasing, while
$s_2(q+d)\leq s_2(q)+s_2(d)$.  Therefore, for a nonzero entry,



$$
v_2(U_{k,j})
 \geq\delta(q_m)-\delta(q_t)
 \geq2d_s-s_2(d_s)=\epsilon_s.                   \tag{23k}
$$



Thus a residual $C$-entry assigned to high row $s$ is divisible by
$R_s$.  The $R_s$ form a divisibility chain.  In every Leibniz monomial,
the retained $C$-columns are assigned to at least $n-1$ distinct rows,
so their row-factor product is divisible by
$R_1\cdots R_{n-1}=\Omega_n^*$.  These factors were found successively:
first $j!$, then $D_t$, then $R_s$ in the residual matrix.  Hence they
multiply even though they share primes; there is no coprimality or
double-counting assumption.  This proves (23d).

Finally



$$
\sum_{t<n}\log(t!)=\frac12n^2\log n+O(n^2),
$$



while removing or restoring all powers of two changes the relevant sums by
only $O(n^2)$.  The factors $\Lambda_n,\Gamma_n,\Omega_n^*$ contribute
respectively $1,\tfrac12,\tfrac12$ times $n^2\log n$.  This proves
(23e). $\square$

There is also a sharper height consequence.  The high-column estimates



$$
\|B_j\|_2\leq\sqrt{2n}(3n)^j,
 \qquad
 \|C_j\|_2\leq4\sqrt{2n}(3n)!
$$



show, after the endpoint-row expansion, that every raw maximal cofactor is
at most



$$
\exp\!\left(\frac72n^2\log n+O(n^2)\right).
$$



Indeed there are at most $n+1$ retained $C$-columns, contributing the
leading constant 3, while the sum of all retained $B$-degrees is at most
$n(n+1)/2$.  If $M_n$ has full row rank, its signed-cofactor vector spans
the kernel and has common divisor at least $\Xi_n$.  Consequently its
primitive $(B,C)$-kernel satisfies



$$
\log H(B,C)\leq\frac32n^2\log n+O(n^2).          \tag{23l}
$$



Reconstructing $A$ and multiplying by $n!$ changes this only by
$O(n\log n)$.  This corrects raw determinant bookkeeping substantially,
but the surviving $\exp((3/2+o(1))n^2\log n)$ upper bound remains far too
large for a fixed analytic radius.  Additional primitive endpoint control
is still absent.  The exact finite probe in Section 7 records all three
proved divisor components, the full cofactor gcd, the polynomial-triple gcd,
and the endpoint-pair gcd separately.

The analytic radius $\sqrt2$ supplies only geometric decay
$r^{-3n}$, for fixed $1<r<\sqrt2$, before coefficient growth is taken
into account.  That cannot beat the coarse upper bound (23).  A successful
use of (1) would therefore need a structured determinant evaluation,
primitive-content theorem, non-diagonal degree choice, or an integral
remainder representation much sharper than raw Hadamard.

## 3. Optimality inside the real Möbius pullback family

The map in (1) is not an arbitrary lucky shift.  It is the unique
radius-maximizer among real Möbius changes of variable fixing 0 and 1.

### Theorem 3

Every nonconstant real Möbius map $u$ with $u(0)=0$ and $u(1)=1$ can
be written



$$
u_a(z)=\frac{z}{a-(a-1)z}.                        \tag{24}
$$



For $a>1$, put $F_a(z)=4\arctan u_a(z)$, continued from zero along the
real interval.  Then $F_a(1)=\pi$, and its exact Taylor radius is



$$
\rho(a)=\frac{a}{\sqrt{(a-1)^2+1}}.              \tag{25}
$$



Moreover



$$
\rho(a)\leq\sqrt2,                               \tag{26}
$$



with equality only at $a=2$.  Thus (1) is the unique optimal member of
this family.

#### Proof

The normal form (24) follows by writing a Möbius map fixing zero as
$Az/(Cz+D)$, imposing $A=C+D$, and dividing by $A$.  Direct
differentiation gives



$$
F_a'(z)=\frac{4a}{(a-(a-1)z)^2+z^2}.             \tag{27}
$$



The two poles are the solutions of $u_a(z)=\pm i$:



$$
z_\pm=\frac{\pm ia}{1\pm i(a-1)}.                \tag{28}
$$



Both have modulus (25), and both are genuine poles of (27).  Finally



$$
\rho(a)^2=\frac{a^2}{a^2-2a+2}.                  \tag{29}
$$



Differentiation, or completing the square in the denominator, shows that
this is uniquely maximized for $a=2$, where it equals 2. $\square$

This theorem is deliberately narrow.  Higher-degree rational pullbacks need
not obey the bound $\sqrt2$, so (26) is not a no-go theorem for all
algebraic substitutions.

### Cyclotomic coefficients enlarge the distinguished radius but not all conjugate radii

There is a natural algebraic-coefficient extension.  For $k>2$, set



$$
c_k=\cot\frac{\pi}{k},\qquad
 \mathcal F_k(z)=k\int_0^z
 \frac{c_k\,dt}{(t-1)^2+c_k^2}.                    \tag{29a}
$$



The Taylor coefficients lie in $\mathbb Q(c_k)$, $\mathcal F_k(0)=0$,
and



$$
\mathcal F_k(1)
 =k\arctan\frac1{c_k}=\pi.                        \tag{29b}
$$



The distinguished pair of poles is $1\pm ic_k$, so its radius is



$$
\sqrt{1+c_k^2}=\csc\frac{\pi}{k}.                \tag{29c}
$$



Thus $k=6$ gives radius 2, and $k=8$ gives
$\sqrt{4+2\sqrt2}=2.613\ldots$.  This does not automatically give a
rational-coefficient function of the same radius, because field conjugation
also moves the poles and changes the endpoint branch.

The cases $k=6,8$ make the loss exact.

For $k=6$, $c_6=\sqrt3$.  Its conjugate is $-\sqrt3$, and the conjugate
Taylor function is exactly $-\mathcal F_6$, with endpoint $-\pi$.  Hence
the rational trace is zero.  More generally, for
$\alpha=a+b\sqrt3\in\mathbb Q(\sqrt3)$,



$$
\operatorname{Tr}(\alpha\mathcal F_6)(1)
 =2b\sqrt3\,\pi.                                  \tag{29d}
$$



It is a rational multiple of $\pi$ only in the zero case $b=0$.

For $k=8$, put $c=1+\sqrt2$.  The conjugate
$c'=1-\sqrt2$ gives



$$
\mathcal F_{8,c}(1)=\pi,\qquad
 \mathcal F_{8,c'}(1)=-3\pi.                     \tag{29e}
$$



Indeed $1/c'=-(1+\sqrt2)$, whose principal arctangent is
$-3\pi/8$.  The ordinary trace $T=\mathcal F_{8,c}+\mathcal F_{8,c'}$
therefore has rational Taylor coefficients and $T(1)=-2\pi$.  With
$y=(z-1)^2$, direct conjugate addition gives



$$
T'(z)=16\frac{y-1}{y^2+6y+1}.                    \tag{29f}
$$



Thus $-T/2$ is a rational-coefficient elementary function taking the value
$\pi$, but its exact radius is the smaller conjugate radius



$$
\sqrt{1+(1-\sqrt2)^2}
 =\sqrt{4-2\sqrt2}=1.082\ldots<\sqrt2.            \tag{29g}
$$



The two conjugate pole pairs are distinct, so no cancellation occurs.  A
weighted trace cannot avoid this while retaining a rational multiple of
$\pi$: if $\alpha=a+b\sqrt2$, then



$$
\operatorname{Tr}(\alpha\mathcal F_8)(1)
 =(-2a+4b\sqrt2)\pi,                              \tag{29h}
$$



which is a rational multiple of $\pi$ only when $b=0$.  In that case
both conjugates occur with nonzero equal rational weights.  These two exact
examples illustrate, without asserting a general trace theorem, why a large
distinguished cyclotomic radius can be lost under rational descent.

## 4. A beta/hypergeometric representation with radius 4

### Theorem 4

Define



$$
H(z)=3\,{}_2F_1\!\left(\frac12,\frac12;\frac32;\frac z4\right).
$$



Then



$$
H(z)=3\sum_{m=0}^{\infty}
 \frac{\binom{2m}{m}}{16^m(2m+1)}z^m,             \tag{30}
$$



$H(1)=\pi$, and the exact Taylor radius is 4.  The first $N$
coefficients have one common denominator of size $\exp(O(N))$.  On the
other hand, the reduced denominator of $H^{(m)}(0)$ has exact
2-adic exponent $3m$:



$$
v_2\bigl(H^{(m)}(0)\bigr)=-3m.                  \tag{31}
$$



#### Proof

The binomial expansion under an elementary beta integral gives



$$
H(z)=3\int_0^1\left(1-\frac{zt^2}{4}\right)^{-1/2}dt,             \tag{32}
$$



which is equivalent to (30).  At $z=1$,



$$
H(1)=3\int_0^1\frac{dt}{\sqrt{1-t^2/4}}
 =6\arcsin\frac12=\pi.                            \tag{33}
$$



The hypergeometric singularity at $z=4$ is genuine; equivalently, the
integrand in (32) first develops its endpoint square-root singularity there.
Thus the radius is exactly 4.

For $m\leq N$, the denominator in (30) divides



$$
16^N\operatorname{lcm}(1,2,\ldots,2N+1),         \tag{34}
$$



which is $\exp(O(N))$.  Finally



$$
H^{(m)}(0)=
 \frac{3m!\binom{2m}{m}}{16^m(2m+1)}.             \tag{35}
$$



Legendre's formula and
$v_2\binom{2m}{m}=s_2(m)$ give



$$
v_2(m!)+v_2\binom{2m}{m}-4m
 =(m-s_2(m))+s_2(m)-4m=-3m,                      \tag{36}
$$



since $2m+1$ and 3 are odd.  This proves (31). $\square$

### Consequence for naive jet clearing

If (2) replaces (1), a high-jet row containing $H^{(k)}(0)$ needs a
factor divisible by $2^{3k}$ under the straightforward derivative
normalization.  Across $\Theta(n)$ rows with $k=\Theta(n)$, the product
of these row factors has logarithm $\Theta(n^2)$.  These row factors are
common to all maximal minors and can partly or wholly disappear when the
kernel is made primitive, so this observation is **not** a primitive-height
lower bound.  It is nevertheless the precise bookkeeping defect absent from
the integral-jet function (1).

## 5. Simple linear inverse-trigonometric families

Two elementary root-of-unity lemmas explain why the most obvious linear
scalings do not produce a better rational-coefficient candidate.

### Lemma 5

If $r\in\mathbb Q$ and $\arcsin(r)/\pi\in\mathbb Q$, then



$$
r\in\{0,\pm\tfrac12,\pm1\}.                      \tag{37}
$$



If $r\in\mathbb Q$, $\arctan(r)/\pi\in\mathbb Q$, and the tangent is
finite, then



$$
r\in\{0,\pm1\}.                                 \tag{38}
$$



#### Proof

If $\theta/\pi\in\mathbb Q$, then $e^{i\theta}$ is a root of unity.
Thus $2\sin\theta$ is a rational algebraic integer whenever
$\sin\theta\in\mathbb Q$, hence an ordinary integer of absolute value at
most 2.  This proves (37).

If $r=\tan\theta\in\mathbb Q$, then



$$
e^{2i\theta}=\frac{1+ir}{1-ir}\in\mathbb Q(i).   \tag{39}
$$



The roots of unity in $\mathbb Q(i)$ are $\pm1,\pm i$.  Solving (39)
for the finite values of $r$ gives $0,\pm1$. $\square$

Consequently a rational linear family $A\arctan(rz)$ evaluating to $\pi$
has radius at most 1.  A rational linear family $A\arcsin(rz)$ that is
analytic past the endpoint has $|r|=1/2$ and radius 2.  The quadratic
hypergeometric desingularization in (2) raises that radius from 2 to 4 by
using



$$
{}_2F_1\!\left(\frac12,\frac12;\frac32;x\right)
 =\frac{\arcsin\sqrt{x}}{\sqrt{x}},               \tag{40}
$$



rather than a linear inverse-sine pullback.

## 6. Modular transformations: a reciprocal candidate outside the verified G-class

Ramanujan's classical modular identity is



$$
S(1)=\frac{16}{\pi},\qquad
 S(z)=\sum_{m=0}^{\infty}
 \binom{2m}{m}^{\!3}(42m+5)\frac{z^m}{2^{12m}}.   \tag{41}
$$



It appears in S. Ramanujan, *Modular equations and approximations to
$\pi$*, Quarterly Journal of Mathematics 45 (1914), equation (29); a
modern WZ proof is S. B. Ekhad and D. Zeilberger, *A WZ proof of Ramanujan's
Formula for Pi*, arXiv:math/9306213.

Formally set



$$
R(z)=\frac{16}{S(z)}.                             \tag{42}
$$



Then $R(1)=\pi$, and $R$ has rational Taylor coefficients.  There is a
fully elementary zero-free disk:

### Proposition 6

The function $R$ in (42) is analytic in a disk of radius strictly larger
than 5.  If $R(z)=\sum r_mz^m$, the reduced denominator of $r_m$ divides



$$
5^{m+1}2^{12m}.                                   \tag{43}
$$



#### Proof

Since $\binom{2m}{m}\leq4^m$, on $|z|=5$, with $x=5/64$,



$$
\begin{aligned}
 |S(z)-5|
 &\leq\sum_{m\geq1}(42m+5)x^m\\
 &=\frac{42x}{(1-x)^2}+\frac{5x}{1-x}\\
 &=\frac{14915}{3481}<5.                           \tag{44}
 \end{aligned}
$$



Rouché's theorem shows that $S$ has no zero in $|z|\leq5$.  The strict
inequality persists on a slightly larger circle, proving the first claim.

Write $S(z)=T(z/4096)$, where $T(w)\in\mathbb Z[[w]]$ and $T(0)=5$.
The coefficient recurrence for $16/T(w)$ shows inductively that its
$m$-th coefficient has denominator dividing $5^{m+1}$.  Substitution
of $w=z/4096$ proves (43). $\square$

This is an interesting analytic/arithmetic representation, but it is **not
accepted here as a G-function construction**.  G-functions are not known to
be closed under reciprocals, and no proof is supplied that the particular
reciprocal (42) is holonomic or is an elementary period function.  Modular
$1/\pi$ series therefore do not automatically answer the present search
for a period/G-function representing $\pi$.  They remain a possible
broader non-holonomic direction.

## 7. Finite exact Hermite--Padé experiment

The script

```text
scripts/mobius_arctan_hp_probe.py
```

constructs the integer matrix in Proposition 2, computes its exact rational
rank and primitive integral kernel, reconstructs $A$, clears by $n!$, and
then performs two distinct gcd reductions:

1. the gcd of the complete polynomial triple after low-coefficient clearing;
2. the gcd of the endpoint pair $(A(1),B(1))$, which need not divide the
   polynomial coefficients.

When the high matrix has full row rank, the script also evaluates one maximal
minor.  Dividing the signed minor by the corresponding coordinate of the
primitive kernel gives the gcd of **all** maximal cofactors.  Thus the output
separates raw determinant size from common cofactor content.

The signs and base-10 decades of the endpoint forms are certified using exact
rational intervals: a factorial-series enclosure for $e$ and alternating
Machin-series enclosures for $\pi$.  No floating-point sign decision enters
the certificate.

The frozen output is

```text
results/mobius_arctan_hp_n15.json
```

Its SHA-256 is

```text
ff0405c94960eb27940b4684de0dcab05cab5b6dd0311abc27f5ed1d85a7691b
```

and the generating script has SHA-256

```text
d812595d92abff631366a889aa8c6e8a13402ace684c93c1fffe56b8032981b6
```

The principal finite observations are:

- the high matrix has the expected full row rank for every $1\leq n\leq15$;
- the first unconstrained Taylor coefficient is nonzero in every tested
  degree, so the imposed order $3n+1$ is exact in this range;
- at $n=1$, the endpoint pair is $(0,0)$, despite a nonzero polynomial
  triple;
- for every $2\leq n\leq15$, the endpoint form is certified nonzero, but
  none has absolute value below 1; its magnitude grows rapidly;
- the common maximal-cofactor content is often large, so a raw Hadamard
  estimate is genuinely different from primitive-kernel height; nevertheless
  the surviving primitive polynomial and endpoint heights also grow quickly
  in the tested range.

Here `cof. digits' is the number of decimal digits in the gcd of all signed
maximal cofactors, `forced digits' is the number in the proved divisor
$\Xi_n=\Lambda_n\Gamma_n\Omega_n^*$, `full gcd' is the common factor removed from the complete
triple after the universal $n!$ scaling, and `endpoint gcd' is the later
gcd of $(A(1),B(1))$.  The column `poly. digits' is the number of decimal
digits in the largest coefficient of the primitive polynomial triple.  For a
nonzero endpoint form $L_n$, the final column certifies
$10^d\leq|L_n|<10^{d+1}$.

| $n$ | rank | cof. digits | forced digits | full gcd | endpoint gcd | poly. digits | certified sign | $d$ |
|---:|---:|---:|---:|---:|---:|---:|:---:|---:|
| 1 | 3 | 1 | 1 | 1 | 0 | 1 | zero | -- |
| 2 | 5 | 1 | 1 | 2 | 1 | 4 | $-$ | 0 |
| 3 | 7 | 3 | 2 | 6 | 1 | 8 | $+$ | 4 |
| 4 | 9 | 6 | 4 | 8 | 9 | 18 | $+$ | 10 |
| 5 | 11 | 12 | 8 | 40 | 288 | 30 | $+$ | 18 |
| 6 | 13 | 20 | 14 | 48 | 100 | 45 | $-$ | 31 |
| 7 | 15 | 32 | 23 | 144 | 60 | 64 | $+$ | 47 |
| 8 | 17 | 47 | 34 | 1152 | 980 | 86 | $-$ | 65 |
| 9 | 19 | 65 | 50 | 1152 | 35840 | 113 | $+$ | 87 |
| 10 | 21 | 87 | 68 | 11520 | 36288 | 141 | $-$ | 112 |
| 11 | 23 | 115 | 91 | 11520 | 100800 | 173 | $+$ | 141 |
| 12 | 25 | 144 | 116 | 138240 | 813120 | 209 | $-$ | 174 |
| 13 | 27 | 179 | 146 | 138240 | 21288960 | 251 | $+$ | 210 |
| 14 | 29 | 219 | 180 | 1935360 | 21415680 | 293 | $+$ | 249 |
| 15 | 31 | 263 | 218 | 29030400 | 5381376 | 340 | $+$ | 293 |

The JSON contains the complete exact arrays for every primitive
$(A_n,B_n,C_n)$, every primitive high-kernel vector, every primitive
endpoint pair, the actual cofactor gcd and its 2-adic valuation, and hashes of
the exact rational endpoint enclosures.  These are finite diagnostics only.
They neither prove the rank pattern nor exclude a non-diagonal or otherwise
structured construction.

## 8. Conclusions and remaining obligations

The search produced one genuinely favorable period representation:



$$
F(z)=4\arctan\frac{z}{2-z},\qquad F(1)=\pi,\qquad
 \operatorname{rad}_0(F)=\sqrt2,\qquad F^{(k)}(0)\in\mathbb Z.     \tag{45}
$$



It rigorously removes high-row denominator clearing from the most direct
endpoint-matched mixed Hermite--Padé system.  This is stronger arithmetically
than the radius-4 beta/hypergeometric representation, whose jets have exact
dyadic denominator $2^{3m}$, and stronger in analytic radius than the raw
$4\arctan z$ representation.

What remains open is precisely what is needed for a Diophantine conclusion:

1. an all-degree rank theorem for the endpoint-bordered matrix (or a
   construction that bypasses it);
2. an all-degree nonvanishing theorem for the primitive endpoint pair;
3. a primitive height/content estimate much sharper than raw Hadamard;
4. an endpoint remainder bound that survives primitive integer
   normalization.

Until all four are supplied, (45) is a new constructive lead, not a proof
about the arithmetic nature of $e+\pi$.
