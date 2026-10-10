> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The centered closer-root construction

## Exact normality, fixed-degree pole asymptotics, diagonal clearing, and the dilation barrier

Checked: 2026-08-27 UTC

## 1. Scope and result

Consider



$$
R(z)=C(z)+2\cosh z\,P(z),\qquad
 \deg P\le n,\quad \deg C\le D,                               \tag{1}
$$



with



$$
\operatorname {ord}_{z=0}R\ge n+D+1.        \tag{2}
$$



At the closer root



$$
z_*=\frac{i\pi}{2}=\frac{i(s-e)}2,\qquad s=e+\pi,             \tag{3}
$$



one has $R(z_*)=C(z_*)$.  Thus, if $s$ were algebraic, the
endpoint would again be a polynomial in $e$ over the fixed field
$\mathbb Q(s,i)$.  This note gives an all-parameter audit of this
construction.  Its conclusions are:

1. The system is normal for every $n,D$.  Up to a scalar, its unique
   solution has one parity only.  After writing

   

$$
\epsilon=\mathbf 1_{n\equiv D\equiv1\pmod2},\quad
    N=\lfloor n/2\rfloor,\quad K=\lfloor D/2\rfloor,             \tag{4}
$$



   it is

   

$$
C(z)=z^\epsilon Q(z^2),\qquad P(z)=z^\epsilon U(z^2),        \tag{5}
$$



   where $-U/Q$ is the $[N/K]$ Padé approximant to

   

$$
g(x)=\frac1{2\cosh\sqrt x}.                    \tag{6}
$$



   The actual endpoint degree is $d=2K+\epsilon$, and

   

$$
\operatorname {ord}_0R
       =\epsilon+2(N+K+1)
       =n+D+1+\mathbf1_{n\equiv D\equiv0\pmod2}.                \tag{7}
$$



2. For each fixed $K\ge1$, the primitive endpoint polynomial satisfies
   the exact scale-invariant asymptotic

   

$$
\boxed{
    \frac{|Q_{N,K}(-\pi^2/4)|}{H(Q_{N,K})}
     =c_K(2K+1)^{-2N}
       \left(1+O_K(\rho_K^N)\right),}
    \qquad
    \rho_K=\left(\frac{2K+1}{2K+3}\right)^2<1,                 \tag{8}
$$



   with the explicit positive rational constant $c_K$ in (34) below.
   The closer endpoint therefore gives a genuine exponentially small
   *relative* value.  It does not by itself control the primitive cofactor
   content.

3. For $D=2$, the endpoint height and value are completely explicit in
   terms of two consecutive Euler numbers.  The remaining arithmetic issue
   is one gcd; see (38)--(43).  Finite data do not replace a bound for this
   gcd.

4. On the diagonal $K=N$, a theorem of Dzyadyk gives

   

$$
-\log\frac{|Q_{N,N}(-\pi^2/4)|}{H(Q_{N,N})}
            =4N\log N+O(N).                                    \tag{9}
$$



   Mandatory endpoint clearing does not hide a dyadic content.  In fact the
   cleared integer polynomial is primitive and has height at least
   $2^{4N}=16^N$.  Hence its achieved relative exponent is only
   $O(\log N)$, while the degree in $e$ is $2N+O(1)$.  The explicit
   all-height measures for $e$ are fully compatible with this value.

5. A pure frequency dilation is exactly neutral after mandatory clearing
   and primitive gcd.  The centered/sech class is not that dilation: after
   setting $w=2z$, its endpoint coefficient has half-integer phase.  The
   exact example $n=8,D=2$ is recorded in (74).  A fixed real symmetric
   frequency band which vanishes at $i\pi/2$ is divisible by $2\cosh z$,
   so it cannot remove the half-integer cosine zero lattice.

Nothing in this note proves that $e+\pi$ is algebraic or transcendental.

## 2. Parity reduction and the Padé problem

Write $n=2N+a$ and $D=2K+b$, where $a,b\in\{0,1\}$.  Because
$2\cosh z$ is even, the jet equations split into their even and odd
parts.  The even block has $N+K+2$ unknowns and



$$
N+K+\lfloor(a+b)/2\rfloor+1                  \tag{10}
$$



equations.  The odd block has $N+K+a+b$ unknowns and



$$
N+K+\lceil(a+b)/2\rceil                      \tag{11}
$$



equations.  Once full row rank is proved, the even nullity is one unless
$a=b=1$, and the odd nullity is one precisely when $a=b=1$.  This gives
(4)--(5).

Put $x=z^2$ and



$$
h(x)=2\cosh\sqrt x=2\sum_{j\ge0}\frac{x^j}{(2j)!}.            \tag{12}
$$



Then (1)--(2) reduce exactly to



$$
Q(x)+h(x)U(x)=O(x^{N+K+1}),qquad
                \deg U\le N,\quad\deg Q\le K.                 \tag{13}
$$



Multiplication by $g=1/h$ gives



$$
U(x)+Q(x)g(x)=O(x^{N+K+1}),                \tag{14}
$$



which is the $[N/K]$ Padé equation for $g$.  Formula (7) follows once
the first omitted coefficient in (13) is known to be nonzero.

## 3. All-parameter normality from a Schur minor

The canonical product is



$$
\cosh\sqrt x=\prod_{\ell=0}^{\infty}(1+t_\ell x),\qquad
 t_\ell=\frac4{\pi^2(2\ell+1)^2}>0.                            \tag{15}
$$



Consequently



$$
\frac1{(2j)!}=e_j(t_0,t_1,\ldots),          \tag{16}
$$



where $e_j$ is an elementary symmetric function.  Eliminating $Q$
from (13), the coefficients $u_0,\ldots,u_N$ of $U$ obey the $N$
high equations



$$
\sum_{j=0}^N\frac{u_j}{(2(K+r-j))!}=0,qquad r=1,\ldots,N,     \tag{17}
$$



with the convention that a negative factorial coefficient is zero.  The
minor in columns $j=1,\ldots,N$ is



$$
\det\left[e_{K+r-j}\right]_{r,j=1}^N
          =s_{(N^K)}(t_0,t_1,\ldots)>0.                         \tag{18}
$$



This is the dual Jacobi--Trudi identity.  Strict positivity follows because
all $t_\ell$ are positive and the rectangular Schur polynomial is not
zero.  Thus (17) has rank $N$.

Two adjacent square minors settle the possible defects.  If the coefficient
of $x^K$ in $Q$ vanished, the $N+1$ equations with row indices
$K,K+1,\ldots,K+N$ would have determinant



$$
\det\left[e_{K+r-j}\right]_{r,j=0}^N>0.                       \tag{19}
$$



If the coefficient of $x^{N+K+1}$ in the remainder vanished, the rows
$K+1,\ldots,K+N+1$ would instead have determinant



$$
\det\left[e_{K+r+1-j}\right]_{r,j=0}^N>0.                    \tag{20}
$$



Both are again rectangular Schur values.  Therefore



$$
\deg Q=K,\qquad [x^{N+K+1}](Q+hU)\ne0,              \tag{21}
$$



For completeness, the parity block not selected in (5) is also controlled
by (20).  After removing its initial factor $z$, when present, its degree
pair is one of



$$
(N-1,K-1),\qquad (N,K-1),\qquad (N-1,K),\qquad (N,K),
$$



according as $a+b=0,1,1,2$.  The jet conditions ask that block for one
order more than the normal Padé order of that degree pair.  Its analogue
of the nonzero minor (20) therefore forces the whole block to vanish; a
negative degree simply means that the corresponding part is absent.
Thus (18)--(20) prove uniqueness, normality, and the exact order (7) for
all $n,D$.  No finite rank extrapolation is used here.

## 4. Cofactors, primitive height, and mandatory endpoint clearing

Write



$$
g(x)=\sum_{j\ge0}a_jx^j,qquad
 a_j=\frac{E_{2j}}{2(2j)!},                                    \tag{22}
$$



where $E_{2j}$ is the signed Euler number.  If
$Q=\sum_{j=0}^Kq_jx^j$, its high equations are



$$
\sum_{j=0}^Kq_ja_{N+\ell-j}=0,qquad
             \ell=1,\ldots,K.                                 \tag{23}
$$



Let $v_j$ be $(-1)^j$ times the determinant obtained by deleting column
$j$ from the $K$-by-$(K+1)$ matrix in (23).  If $L$ clears all
cofactor denominators and



$$
g_{N,K}=\gcd_{0\le j\le K}(Lv_j),             \tag{24}
$$



then



$$
Q_{N,K}^{\rm prim}(x)
               =\sum_{j=0}^K\frac{Lv_j}{g_{N,K}}x^j             \tag{25}
$$



up to sign.  This is the exact endpoint-only primitive normalization.  The
height of the auxiliary $P$ does not occur in a transcendence measure at
the endpoint.  Elementary factorial clearing gives



$$
\log H(Q_{N,K}^{\rm prim})=O_K(N\log N),    \tag{26}
$$



but this upper bound is not a primitive-content asymptotic.

Now suppose temporarily that $s=e+\pi$ is algebraic.  Choose
$\delta\in\mathbb Z_{>0}$ such that $\theta=\delta s$ is an algebraic
integer.  For a primitive integer endpoint
$C(z)=\sum_{j=0}^dc_jz^j$, the canonical integral polynomial is



$$
\begin{aligned}
 \mathcal P_C(X)
  &=(2\delta)^d C\left(\frac{i(s-X)}2\right)\\
  &=\sum_{j=0}^dc_ji^j2^{d-j}\delta^{d-j}
       (\theta-\delta X)^j\in\mathcal O_{\mathbb Q(s,i)}[X],    \tag{27}
 \end{aligned}
$$



and



$$
\mathcal P_C(e)=(2\delta)^dC(i\pi/2).      \tag{28}
$$



If $\Theta$ is the house of $\theta$, then



$$
H(\mathcal P_C)\le(d+1)H(C)
             \max\{2\delta,\Theta+\delta\}^{d}.                \tag{29}
$$



The inverse substitution is



$$
C(z)=(2\delta)^{-d}\mathcal P_C(s+2iz).
$$



Consequently, for fixed hypothetical $s$ and $\delta$,



$$
\left|\log H(\mathcal P_C)-\log H(C)\right|
       =O_{s,\delta}\!\left(d+\log(d+1)\right).                \tag{29a}
$$



The exponent in (27) is the *actual* degree $d=2K+\epsilon$, not the
formal bound $D$.  Mechanical use of $(2\delta)^D$ when $d<D$
introduces a common factor $(2\delta)^{D-d}$, which primitive
normalization removes.

Before inserting $s$, the exactly cleared endpoint polynomial is



$$
\mathscr C(T)=i^{-\epsilon}2^dC(iT/2)\in\mathbb Z[T]. \tag{30}
$$



Its primitive version is obtained by dividing the ordinary gcd of its
coefficients.  Because $C$ is primitive, that gcd is a power of $2$ of
exponent at most $d$.  Hence, for fixed $d$, both its height and its
value differ from those of $C$ by constants depending only on $d$.

## 5. Fixed endpoint degree: exact pole dominance

The Euler--beta formula gives the absolutely convergent moment expansion



$$
a_N=(-1)^N\sum_{\ell\ge0}w_\ell t_\ell^N,qquad
 w_\ell=\frac{(-1)^\ell}{\alpha_\ell},\quad
 t_\ell=\alpha_\ell^{-2},\quad
 \alpha_\ell=\frac{(2\ell+1)\pi}{2}.                            \tag{31}
$$



Normalize $q_0=1$ and set



$$
T(t)=t^KQ(-1/t).                         \tag{32}
$$



Equation (23) says that $T$ is monic and orthogonal to
$1,t,\ldots,t^{K-1}$ for the signed discrete weights
$w_\ell t_\ell^{N+1-K}$.  The algebraic Heine formula, obtained by
Cauchy--Binet, is



$$
T(t)=
 \frac{\displaystyle
  \sum_{|S|=K}\left(\prod_{\ell\in S}w_\ell
  t_\ell^{N+1-K}\right)\Delta(t_S)^2
  \prod_{\ell\in S}(t-t_\ell)}
 {\displaystyle
  \sum_{|S|=K}\left(\prod_{\ell\in S}w_\ell
  t_\ell^{N+1-K}\right)\Delta(t_S)^2}.                         \tag{33}
$$



For fixed $K$, the denominator has the unique dominant subset
$\{0,\ldots,K-1\}$.  At $t=t_0$, every subset containing $0$
vanishes in the numerator, whose unique dominant subset is instead
$\{1,\ldots,K\}$.  Since all corresponding weights and Vandermonde
factors are nonzero, division gives (8), where



$$
\boxed{
 c_K=(2K+1)^{2K-3}
 \left(
  \frac{\Delta(a_1,\ldots,a_K)}
       {\Delta(a_0,\ldots,a_{K-1})}
 \right)^2
 \prod_{j=1}^K(1-a_j),qquad
 a_j=\frac1{(2j+1)^2}.}                                        \tag{34}
$$



All powers of $\pi$ cancel, so $c_K\in\mathbb Q_{>0}$.  The first
values are



$$
c_1=\frac8{27},\quad c_2=\frac{256}{9375},\quad
 c_3=\frac{1024}{823543},\quad
 c_4=\frac{65536}{1937102445}.                                 \tag{35}
$$



The next nonvanishing numerator subset gives the safe error ratio
$\rho_K=t_{K+1}/t_K$ in (8).  Moreover, coefficientwise,



$$
Q_{N,K}(x)\longrightarrow
            \prod_{j=0}^{K-1}(1+t_jx).                          \tag{36}
$$



The constant coefficient is $1$, while
$\sum_{j\ge0}t_j=1/2$; hence the limiting coefficient height is $1$.
This proves that (8) is already normalized by the actual coefficient
height.  Since $2N=n+O(1)$, the relative gain is



$$
\exp\{-n\log(2K+1)+O_K(1)\}.                  \tag{37}
$$



## 6. The exact quadratic family

Let $D=2$, so $K=1$, and put



$$
A_N=(2N+2)(2N+1),\qquad
 G_N=\gcd\left(A_N|E_{2N}|,|E_{2N+2}|\right).                  \tag{38}
$$



Equation (23) gives, up to sign,



$$
Q_N^{\rm prim}(x)=
 \frac{A_N|E_{2N}|+|E_{2N+2}|x}{G_N}.                          \tag{39}
$$



The constant coefficient is the larger one.  Since the second coefficient
is odd and the first is even, mandatory clearing produces the already
primitive polynomial



$$
\mathscr C_N(T)=
 \frac{4A_N|E_{2N}|-|E_{2N+2}|T^2}{G_N},                       \tag{40}
$$



with



$$
H(\mathscr C_N)=\frac{4A_N|E_{2N}|}{G_N}.                     \tag{41}
$$



Using



$$
|E_{2N}|=\frac{4^{N+1}(2N)!}{\pi^{2N+1}}\,\beta(2N+1),        \tag{42}
$$



one obtains the exact relative value



$$
\boxed{
 \frac{|\mathscr C_N(\pi)|}{H(\mathscr C_N)}
   =\frac{\beta(2N+3)}{\beta(2N+1)}-1
   \sim\frac8{3^{2N+3}}.}                                     \tag{43}
$$



For completeness, $\beta(s+2)>\beta(s)$ follows by pairing the
alternating terms in



$$
\beta(s+2)-\beta(s)
   =\sum_{m\ge0}(-1)^m(2m+1)^{-s}
       \left((2m+1)^{-2}-1\right),                              \tag{44}
$$



and the $m=1$ term gives the displayed asymptotic, with the remaining
terms geometrically smaller.

The unresolved arithmetic datum is exactly $G_N$.  Computation of a
finite list of $G_N$'s is not an upper bound for it.  In particular one
must not replace (38) by an observed small gcd and then claim a
transcendence consequence.

For fixed actual degree $d$, the relative-norm $e$-measure in
`root_of_unity_low_degree_polynomial_e_measure.md` says that an algebraic
hypothesis of degree $r=[\mathbb Q(s):\mathbb Q]$ could be contradicted
only if the relative gain exceeded



$$
(r^2d+r+o(1))\log H(\mathscr C_N).           \tag{45}
$$



Combining (8) and (45), a fixed-$K$ contradiction would require



$$
2N\log(2K+1)>
       (r^2d+r+o(1))\log H(\mathscr C_{N,K}).                   \tag{46}
$$



The Padé analysis proves the left side but does not prove the needed
primitive-height estimate on the right.  For $D=2$, (38)--(41) isolate
that missing arithmetic lemma exactly.

## 7. The diagonal and its dyadic clearing

Let $K=N$.  If $A_N(x)/B_N(x)$ is the normalized diagonal
$[N/N]$ Padé approximant to $\cosh\sqrt x$, then



$$
\frac{B_N(x)}{2A_N(x)}                      \tag{47}
$$



is the $[N/N]$ approximant to $g(x)$.  Thus the closer-root denominator
$Q_{N,N}$ is $A_N$, up to a scalar.

The primary source for the diagonal asymptotic is V. K. Dzyadyk,
“The asymptotics of diagonal Padé approximants of $\sin z$, $\cos z$,
$\sinh z$ and $\cosh z$,” *Mathematics of the USSR-Sbornik* **36**
(1980), 231--249,
[MathNet primary record](https://www.mathnet.ru/eng/sm2294), Theorem 2.4.
The inspected PDF had SHA-256

    7c56b8c1e467eb0a54a59d7aeb440763ee9b4d2aa4465e5ecabc39567cb07b39

Dzyadyk's equation (2.18) states, for fixed $z$,



$$
\cosh z-\pi_{2N,2N}(z)
 =\frac{z^{4N+2}}{(2N)!(2N+1)!}
   \frac{\widetilde\gamma_{2N+2}}
        {\widetilde\gamma_{2N}}
   \left(1+O\left(\frac{|z|^2}{N}\right)\right).              \tag{48}
$$



The even analogue of his estimates (1.10), (1.10') gives



$$
\log\left|\frac{\widetilde\gamma_{2N+2}}
                   {\widetilde\gamma_{2N}}\right|=O(N).        \tag{49}
$$



There is no hidden coefficient-height term of order $N\log N$.  Indeed,
Dzyadyk's polynomial $C_{2N}(t)$ has all $N$ positive roots in
$(0,1)$, together with their negatives, and his (1.20) gives



$$
\left|\frac{c_{2N-2j}}{c_{2N}}\right|\le\binom Nj.            \tag{50}
$$



After normalizing the Padé denominator to have constant coefficient $1$,
(50) yields



$$
|[z^{2j}]B_N(z^2)|
 \le \binom Nj\frac{(2N-2j)!}{(2N)!},                          \tag{51}
$$



so $B_N(-\pi^2/4)=1+O(1/N)$.  Expanding $C_{2N}(1+t)$, whose
roots all have modulus at most $2$, similarly gives



$$
|[z^{2j}]A_N(z^2)|\le\frac{4^j}{(2j)!},                       \tag{52}
$$



and therefore $1\le H(A_N)\le2$.  At $z=i\pi/2$, the target
$\cosh z$ is zero.  Equations (48)--(52) and Stirling's formula prove
(9).

The following local theorem tracks the mandatory $2^{d}$ clearing
exactly.

### Dyadic diagonal theorem

Write



$$
A_N(x)=\sum_{j=0}^N\alpha_{N,j}x^j,qquad
                 \alpha_{N,0}=1.                               \tag{53}
$$



Then



$$
v_2(\alpha_{N,N})=-2N,                     \tag{54}
$$



and, if $C_N(x)=\sum_{j=0}^Nc_{N,j}x^j$ is its primitive integer
multiple, then



$$
v_2(c_{N,j})\ge2(N-j),\qquad
 v_2(c_{N,0})=2N,\qquad v_2(c_{N,N})=0.                         \tag{55}
$$



Consequently



$$
\widehat C_N(T)=
   \sum_{j=0}^N(-1)^jc_{N,j}2^{2N-2j}T^{2j}                    \tag{56}
$$



is primitive and



$$
H(\widehat C_N)\ge2^{4N}.                \tag{57}
$$



The same assertion holds after multiplication by the parity monomial
$T^\epsilon$ when $n=D=2N+1$.

To prove the theorem, scale $x=4y$ and put



$$
H_j=\frac{4^j}{(2j)!}.                         \tag{58}
$$



Legendre's formula gives $v_2(H_j)=s_2(j)$.  For $j\ge1$,



$$
\frac{H_j}{2}\equiv C_{j-1}\pmod2,       \tag{59}
$$



because both sides are odd exactly when $j$ is a power of $2$;
here $C_j$ is the Catalan number.  The reversed denominator moment matrix
and the augmented numerator matrix are



$$
M_N=[H_{r+c-1}]_{r,c=1}^N,qquad
 \widehat M_N=[H_{r+c}]_{r,c=0}^N.                              \tag{60}
$$



Factoring $2$ from every row of $M_N$ and from the last $N$ rows of
$\widehat M_N$, (59) reduces their determinants modulo $2$ to



$$
\det[C_{r+c}]_{r,c=0}^{N-1}=1,qquad
 \det[C_{r+c+1}]_{r,c=0}^{N-1}=1.                              \tag{61}
$$



These two Catalan Hankel identities follow directly from the all-one
Stieltjes continued fraction for the Catalan generating function (or its
unit triangular Hankel factorization).  Hence



$$
v_2(\det M_N)=v_2(\det\widehat M_N)=N.        \tag{62}
$$



Cramer's determinant formula is



$$
4^N\alpha_{N,N}
                    =(-1)^N\frac{\det\widehat M_N}{\det M_N},  \tag{63}
$$



which proves (54).  Dividing the high Padé equations by $2$, the same
Catalan matrix is invertible over the local ring $\mathbb Z_{(2)}$.
Therefore every coefficient of $A_N(4y)$ is $2$-adically integral:



$$
v_2(\alpha_{N,j})\ge-2j.               \tag{64}
$$



Primitive clearing of (53), together with equality at $j=N$, gives
(55).  The top coefficient in (56) is odd, while its constant coefficient
has valuation $4N$.  No odd prime can enter the content because
$C_N$ was primitive.  This proves (56)--(57).

Mandatory clearing changes logarithmic height by only $O(N)$, so (9)
also gives



$$
-\log\frac{|\widehat C_N(\pi)|}{H(\widehat C_N)}
       =4N\log N+O(N),qquad
 \frac{4N\log N+O(N)}{\log H(\widehat C_N)}=O(\log N).         \tag{65}
$$



The second estimate uses only (57); it is not an unproved height
asymptotic.

For the canonical integral polynomial (27), (9) and $H(C_N)\ge1$ imply



$$
-\log|\mathcal P_{C_N}(e)|
                         \le4N\log N+O_s(N).                    \tag{66}
$$



This is compatible with both explicit $e$-measures recorded in
`root_of_unity_low_degree_polynomial_e_measure.md`.  For example, in the
all-height Fischler--Rivoal formula, $p\ge k d$, where
$k=[\mathbb Q(s,i):\mathbb Q]$, and the factor



$$
a=(p+1)!\exp(p(p+1)/2)(2q)^{pd}                               \tag{67}
$$



alone makes its guaranteed lower bound at most



$$
\exp(-k p(p+1)/2)=\exp(-\Omega_s(d^2)).\tag{68}
$$



This is much smaller than the certified lower scale implicit in (66),
$\exp(-O(d\log d))$.  When the sharper Ernvall-Hytönen--Matala-aho--
Seppälä height threshold applies, its correction term already contains
$\mathfrak B_{rd}e^{\mathfrak s_{rd}}$, again far beyond $O(d\log d)$.
Thus the canonical diagonal polynomial does not cross a known measure.
An additional, separately proved coefficient-field saturation effect would
be new arithmetic input; it is not supplied by the Padé construction.

## 8. Dilation, the odd shift, and symmetric bands

Let $\lambda,q\in\mathbb Z_{>0}$, let
$C_1(w)=\sum_{j=0}^dc_jw^j$ be primitive, and define



$$
C_q(z)=\frac{C_1(qz)}{g_q},\qquad
             g_q=\gcd_j(c_jq^j).                               \tag{69}
$$



Prime by prime, some $c_j$ is a unit and $j\le d$, so $g_q\mid q^d$.
The base endpoint $i\pi/\lambda$ dilates to $i\pi/(\lambda q)$.
Mandatory clearing gives



$$
(\lambda q\delta)^d C_q\left(\frac{i(s-X)}{\lambda q}\right)
   =\frac{q^d}{g_q}
      (\lambda\delta)^d C_1\left(\frac{i(s-X)}{\lambda}\right).
                                                                    \tag{70}
$$



The scalar $q^d/g_q\in\mathbb Z$ disappears on primitive normalization.
Therefore a pure frequency dilation gives exactly the same primitive
polynomial in $e$, not a new approximation.  Centered exponential type
and endpoint radius scale inversely as well, so the centered Schwarz gain
is unchanged.

This pure-dilation statement must not be confused with (1).  If



$$
f(w)=\frac1{1+e^w},                    \tag{71}
$$



then



$$
\frac1{2\cosh z}=e^z f(2z).                    \tag{72}
$$



Thus the even-shift $f(2z)$ is a dilation of the integer-phase problem,
but the centered/sech class contains the additional odd shift $e^z$.
Equivalently, setting $w=2z$ in (1) and multiplying by $e^{w/2}$ gives



$$
e^{w/2}R(w/2)=e^{w/2}C(w/2)+(1+e^w)P(w/2),                    \tag{73}
$$



whose endpoint coefficient lies at half-integer phase.

The exact $n=8,D=2$ comparison is



$$
\begin{array}{c|c|c}
  \text{class}&C(z)&\text{primitive cleared endpoint}\\ \hline
  q=1\text{ integer phase}&306+31z^2&306-31\pi^2\\
  q=2\text{ even dilation}&153+62z^2&306-31\pi^2\\
  q=2\text{ centered/sech}&124650+50521z^2&498600-50521\pi^2
 \end{array}                                                    \tag{74}
$$



In the middle row, $2^2C(i\pi/2)=2(306-31\pi^2)$, and the factor $2$
is removed primitively.  Exact finite scans in the certificate reproduce
this equivalence for $D=2,3$ and $n\le12$.  They also record the much
larger centered/sech heights in that grid, but no finite inequality is
extrapolated to all $n,D$.

Finally, let



$$
B(z)=b_0+\sum_{j=1}^m b_j(e^{jz}+e^{-jz}),\qquad b_j\in\mathbb R,\qquad
 B(i\pi/2)=0.                                                   \tag{75}
$$



After putting $w=e^z$ and multiplying by $w^m$, one obtains a real
reciprocal polynomial.  Its root $w=i$ forces both the conjugate root
$-i$ and the reciprocal root $1/i=-i$.  Hence it is divisible by
$w^2+1=w(w+w^{-1})$, and therefore



$$
B(z)=2\cosh z\,S(z)                    \tag{76}
$$



for another real symmetric Laurent band $S$.  Such a band retains every
zero $i\pi(k+1/2)$ of $\cosh z$.  If $S$ is nonzero at the first
$K+1$ of those zeros and has no additional zero of smaller modulus, the
same pole-dominance argument as in Section 5 has the identical geometric
base $2K+1$; only its nonzero residue constant changes.  Without the
second hypothesis, zeros of $S$ may add nearer singularities, and zeros
on the cosine lattice may increase multiplicities.  In no case can $S$
cancel the factor in (76).  Thus a symmetric scalar band cannot move the
unavoidable cosine poles outward, although this observation alone is not
a complete Padé classification for every possible $S$.

This conclusion concerns a fixed scalar symmetric band multiplying a
single polynomial $P$.  Independent polynomial coefficients at several
frequencies form a different constrained Hermite--Padé problem and are not
classified here.

## 9. Deterministic replay and logical boundary

The companion files are

* `scripts/root_unity_closer_root_sech_pade_certificate.py`;
* `results/root_unity_closer_root_sech_pade_certificate.json`;
* `results/root_unity_closer_root_sech_pade_hashes.sha256`.

The replay checks exact parity/order identities, the three Schur minors,
cofactor denominators, (34), the quadratic beta identity, the diagonal
Catalan/determinant valuations, primitive endpoint clearing, pure dilation,
the sample (74), and symmetric Laurent divisibility.  High-precision
numbers are diagnostics only.  The all-parameter proofs are the determinant,
pole-dominance, Dzyadyk, and local $2$-adic arguments above.

The remaining fixed-degree arithmetic problem is the primitive cofactor
content in (24), already explicit in (38) for $D=2$.  The diagonal is
rigorously compatible with known $e$-measures.  Neither statement
classifies $e+\pi$.
