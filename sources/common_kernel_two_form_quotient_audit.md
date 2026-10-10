> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Common-kernel identity, saturated lattice, and the two-form quotient obstruction

## Status

This note audits the polynomial construction



$$
f(x)=a+(1+x^2)H'(x),\qquad a\in\mathbf Z,\quad H\in\mathbf Z[x],
$$



and the condition



$$
A(g):=\sum_{k=0}^{\deg g}(-1)^k g^{(k)}(1),
\qquad A((1+x^2)H')=0.
$$



The integral identity is exact and has no hidden denominator.  The corrected
saturated lattice computations give rigorously valid finite small linear
forms.  They do **not** give an all-degree theorem, and therefore do not prove
that $e+\pi$ is irrational.

The strongest conceptual outcome is a precise audit of the proposed
second-successive-minimum route.  Two independent small forms would indeed
remove the need to prove either form nonzero separately.  However, in the
natural two-dimensional quotient, Minkowski forces the missing estimate to be
$\lambda _1/\Delta\to\infty$.  Under the hypothesis that $e+\pi$ is
rational one necessarily has $\lambda _1=O(\Delta)$ and
$\lambda _2\gg 1$.  Thus a determinant or transference argument does not
supply the missing estimate for free: the estimate itself distinguishes the
irrational case from the rational case.

The exact finite certificate accompanying this note is
`scripts/common_kernel_two_form_certificate.py`, with recorded output
`results/common_kernel_two_form_certificate.json`.

## 1. Exact integral identity

For a polynomial $g$, also put



$$
B(g):=\sum_{k=0}^{\deg g}(-1)^k g^{(k)}(0).
$$



Repeated integration by parts, or direct differentiation of the finite sum,
gives



$$
\int_0^1 g(x)e^x\,dx=eA(g)-B(g).                 \tag{1}
$$



If $f=a+(1+x^2)H'$, then



$$
f(i)=a,
$$



and the common-kernel condition gives $A(f)=a$.  Therefore (1) gives



$$
\int_0^1 f(x)e^x\,dx=ae-B(f).                   \tag{2}
$$



On the rational-kernel side,



$$
4\int_0^1\frac{f(x)}{1+x^2}\,dx
=4a\int_0^1\frac{dx}{1+x^2}+4\int_0^1H'(x)\,dx
=a\pi+4(H(1)-H(0)).                             \tag{3}
$$



Combining (2) and (3),



$$
\boxed{
\int_0^1 f(x)\left(e^x+\frac4{1+x^2}\right)dx
=a(e+\pi)+b,
\quad b=4(H(1)-H(0))-B(f)\in\mathbf Z .}
                                                               \tag{4}
$$



The endpoint conditions $f(0)=f(1)=0$ are useful for the small-polynomial
search but are not needed for (4).  The identity also holds over $\mathbf R$:
integrality is needed only to conclude $(a,b)\in\mathbf Z^2$.

One can equivalently write



$$
A(g)=\int_0^\infty e^{-t}g(1-t)\,dt,             \tag{5}
$$



because the Taylor expansion of a polynomial is finite and
$\int_0^\infty e^{-t}t^kdt=k!$.

## 2. Exact one-row reduction after imposing the endpoints

Write, with no loss from an irrelevant constant term,



$$
H(x)=\sum_{m=1}^{M}h_mx^m,
\qquad h_m\in\mathbf Z,
$$



and put



$$
u_j=A(x^j)=(-1)^j {!j}.
$$



The useful recurrence is



$$
u_0=1,\qquad u_j=1-ju_{j-1}.                    \tag{6}
$$



The two endpoint equations are



$$
a+h_1=0,
\qquad a+2\sum_{m=1}^{M}mh_m=0.
$$



If



$$
S=\sum_{m=2}^{M}mh_m,
$$



then these equations are exactly



$$
h_1=-2S,
\qquad a=2S.                                    \tag{7}
$$



The remaining common-kernel condition is the single integer equation



$$
\boxed{
\sum_{m=2}^{M}c_mh_m=0,
\qquad
c_m=m\bigl(u_{m-1}+u_{m+1}-4\bigr).}            \tag{8}
$$



Conversely, every integer solution of (8), with $h_1,a$ defined by (7),
gives exactly one endpoint-zero common-kernel polynomial.  Explicitly,



$$
f(x)=\sum_{m=2}^{M}mh_m
\left(x^{m-1}+x^{m+1}-2x^2\right).              \tag{9}
$$



The second integral coordinate is also a one-row functional:



$$
\boxed{
b=\sum_{m=2}^{M}d_mh_m,
\qquad
d_m=(-1)^m(m^2+m+1)m!+4(1-m).}                 \tag{10}
$$



To check (10), use



$$
B(x^j)=(-1)^j j!,
$$



apply it to each summand in (9), and use
$H(1)=\sum_{m=2}^{M}(1-2m)h_m$.

Equations (7)--(10) are a simpler exact model of the lattice than the original
three-row constraint matrix.

## 3. Exact coefficient image

Let $\Gamma_M$ be the image in $\mathbf Z^2$ of the lattice (8) under
$h\mapsto(a,b)$, with $a,b$ given by (7) and (10).

### Theorem 1

For every $M\ge 6$,



$$
\boxed{\Gamma_M=8\mathbf Z\times2\mathbf Z.}    \tag{11}
$$



### Proof

First prove the containment.  Recurrence (6) gives, modulo 8,



$$
u_n\equiv
\begin{cases}
1,&n\ \hbox{even},\\
1-n,&n\ \hbox{odd}.
\end{cases}                                     \tag{12}
$$



Indeed, an even value $u_{2r}\equiv1$ gives
$u_{2r+1}\equiv1-(2r+1)$; the next recurrence gives
$u_{2r+2}\equiv1+4r(r+1)\equiv1\pmod8$.

If $m$ is odd, (12) gives



$$
u_{m-1}+u_{m+1}-4\equiv-2\pmod8.
$$



If $m$ is even, it gives



$$
u_{m-1}+u_{m+1}-4\equiv-2m-2\pmod8.
$$



In both cases,



$$
c_m\equiv-2m\pmod8,
\qquad \frac{c_m}{2}\equiv-m\pmod4.             \tag{13}
$$



Divide (8) by 2 and reduce modulo 4.  Equation (13) yields



$$
S=\sum_{m=2}^{M}mh_m\equiv0\pmod4.
$$



Thus $a=2S$ is divisible by 8.  Formula (10) shows immediately that every
$d_m$ is even for $m\ge2$, so $b$ is even.  Hence
$\Gamma_M\subseteq8\mathbf Z\times2\mathbf Z$.

For the reverse containment it is enough to work at $M=6$.  The vectors,
listed as $(h_2,h_3,h_4,h_5,h_6)$,



$$
(-55,30,6,0,0),
\qquad
(-687,1352,-693,0,15)
$$



satisfy (8) and give respectively



$$
(a,b)=(8,-178),
\qquad (a,b)=(0,2).
$$



Consequently $(8,0)=(8,-178)+89(0,2)$ also lies in the image.  Zero-padding
the two witnesses proves the result for every $M\ge6$.  ∎

This exact image description is useful when testing a hypothetical rational
value of $e+\pi$: if $e+\pi=p/q$, then the zero direction
$(8q,-8p)$ always belongs to $\Gamma_M$.

## 4. Saturation audit

The first temporary probe formed primitive integer multiples of individual
rational nullspace rays.  Such rays need not span the full integer kernel;
that procedure can return a proper sublattice.  Its candidates were valid,
but its search was incomplete and its old coefficients and rates must not be
used.

The corrected procedure applies row Hermite normal form to $C^T$.  In
python-flint's convention,



$$
H=TC^T,
$$



where $T\in\mathrm{GL}_n(\mathbf Z)$.  The rows of $T$ corresponding to
zero rows of $H$ form the full saturated integer kernel.  Here is the short
proof.  If $zC^T=0$ and $w=zT^{-1}$, then $w\in\mathbf Z^n$ and
$wH=0$.  The nonzero HNF rows are linearly independent, so the coordinates
of $w$ on those rows vanish.  Thus $z=wT$ is an integer combination of
the zero-row vectors.  The converse is immediate.

Appending exact scaled shifted-Chebyshev coordinates is injective, and
LLL/BKZ uses integer row operations, so the corrected reduced rows remain in
exactly this saturated lattice.

## 5. The exact two-form irrationality lemma

### Lemma 2

Let $\alpha\in\mathbf R$.  Suppose that for every index $D$ in an
unbounded sequence there are two integer pairs



$$
\gamma_{D,j}=(a_{D,j},b_{D,j})\in\mathbf Z^2,
\qquad j=1,2,
$$



such that



$$
a_{D,1}b_{D,2}-a_{D,2}b_{D,1}\ne0              \tag{14}
$$



and



$$
|a_{D,j}\alpha+b_{D,j}|\le\varepsilon_D,
\qquad j=1,2,
\qquad \varepsilon_D\longrightarrow0.           \tag{15}
$$



Then $\alpha$ is irrational.

### Proof

If $\alpha=p/q$ in lowest terms, then



$$
q(a\alpha+b)=ap+bq\in\mathbf Z.
$$



Condition (14) says that the two coefficient pairs do not both lie on the
one-dimensional zero line $ap+bq=0$.  Hence at least one of the two forms
is nonzero and has modulus at least $1/q$, contradicting (15).  ∎

The important requirements are simultaneous bounds for both forms at the
same $D$, and exact nonproportionality.  This lemma is a genuine way to
avoid a separate sign proof for each individual form.

## 6. The correct real quotient norm

Let $V_D$ be the real vector space of degree-bounded polynomials satisfying
the common-kernel and endpoint conditions, parametrized by real $H$.  Let
$\Lambda_D\subset V_D$ be the integral-$H$ lattice, and define the real
linear coordinate map



$$
T_D:V_D\longrightarrow\mathbf R^2,
\qquad T_D(f)=(a,b).
$$



Let $W_D=\ker T_D$, and put $\Gamma_D=T_D(\Lambda_D)$.  On the quotient
$V_D/W_D$, use the quotient sup norm



$$
\|y\|_{q,D}
=\inf\{\|f\|_{[0,1]}: f\in V_D,\ T_D(f)=y\}.   \tag{16}
$$



It is legitimate that the minimizing correction in $W_D$ is real rather
than integral.  Formula (4) holds over $\mathbf R$, and every
$w\in W_D$ has both coordinates zero, hence exact integral zero.  Therefore
for $\alpha=e+\pi$,



$$
|a\alpha+b|
\le (e-1+\pi)\|(a,b)\|_{q,D}
<5\|(a,b)\|_{q,D}.                               \tag{17}
$$



Let $B_D$ be the unit ball of (16), and let $\lambda_1(D)\le\lambda_2(D)$
be the two successive minima of the rank-two lattice $\Gamma_D$ with
respect to $B_D$.  Lemma 2 shows that



$$
\lambda_2(D)\longrightarrow0                    \tag{18}
$$



would prove that $e+\pi$ is irrational.

## 7. What Minkowski does, and what it does not do

Define the normalized covolume



$$
\Delta_D=\frac{\operatorname{covol}(\Gamma_D)}{\operatorname{area}(B_D)}.
$$



Minkowski's second theorem in dimension two gives



$$
2\Delta_D
\le\lambda_1(D)\lambda_2(D)
\le4\Delta_D.                                   \tag{19}
$$



Consequently, a proved lower bound $\lambda_1(D)\ge L_D$ forces (18) only
when



$$
\boxed{\frac{\Delta_D}{L_D}\longrightarrow0.}   \tag{20}
$$



Equivalently, the needed estimate is



$$
\frac{\lambda_1(D)}{\Delta_D}\longrightarrow\infty. \tag{21}
$$



A generic lower bound obtained from the smallest semiaxis and the minimum
Euclidean length of a nonzero coefficient vector is only
$\lambda_1\gg\Delta_D$ in the observed anisotropic geometry.  That is not
enough for (20).

The rational hypothesis makes the issue exact.  Suppose
$\alpha=p/q$.  Any two independent vectors in $\Gamma_D\subset\mathbf Z^2$
include one for which $|a\alpha+b|\ge1/q$.  By (17),



$$
\lambda_2(D)\ge\frac1{5q}.                       \tag{22}
$$



Combining (22) with the upper half of (19),



$$
\lambda_1(D)\le20q\Delta_D.                     \tag{23}
$$



Thus (21) is already incompatible with rationality.  Proving (21) by a
supposedly automatic determinant or transference estimate would in fact be
proving the missing irrationality statement.

## 8. Exact rational toy model

The phenomenon is transparent in the norm



$$
N_{\varepsilon,\alpha}(m,n)
=\sqrt{\varepsilon^2m^2+(m\alpha+n)^2}
\quad\text{on }\mathbf Z^2.                      \tag{24}
$$



Its metric covolume has order $\varepsilon$.  If
$\alpha=p/q$, then



$$
N_{\varepsilon,\alpha}(q,-p)=\varepsilon q.
$$



Every independent vector has transverse coordinate of modulus at least
$1/q$.  A Bezout vector supplies an independent vector with transverse
coordinate exactly $1/q$.  Hence, as $\varepsilon\to0$,



$$
\lambda_1\asymp\varepsilon,
\qquad
\lambda_2\asymp1.                               \tag{25}
$$



The one exponentially cheap direction consumes the whole determinant.  This
is the rational model that a second-minimum proof must rule out.

## 9. Exact finite certificate

At `g_degree=40`, the first two corrected saturated reduced rows recorded in
the certificate give



$$
(a_1,b_1)=
(461515305521655600,-2704421761901323052),
$$





$$
(a_2,b_2)=
(-805266044026219440,4718757942649659800).
$$



Their exact coefficient determinant is



$$
a_1b_2-a_2b_1=559082349120\ne0.                  \tag{26}
$$



Their exact shifted-Chebyshev $\ell^1$ bounds are



$$
\frac{1672003183159179573}{4835703278458516698824704}
$$



and



$$
\frac{195801091420686753}{302231454903657293676544}.
$$



Since $|T_k(2x-1)|\le1$ on $[0,1]$, these fractions bound the two sup
norms.  Formula (17) therefore gives rigorous form bounds after multiplication
by 5.  The certificate also uses rational series bounds for $e$ and Machin's
formula for $\pi$ to certify the positive intervals



$$
5.1157995729364323971\cdot10^{-7}
<a_1(e+\pi)+b_1
<5.1273467686318537787\cdot10^{-7},
$$





$$
3.1677069535554310227\cdot10^{-7}
<a_2(e+\pi)+b_2
<3.1878548543639173210\cdot10^{-7}.
$$



These are finite exact certificates, not an all-degree result.

## 10. Quotient-ellipsoid diagnostics only

For diagnosis, the sup norm was replaced by the Euclidean norm of the shifted-
Chebyshev coefficient vector.  The real quotient minimization is then a
rational quadratic program, and the image lattice is reduced as a two-
dimensional ellipsoidal lattice.  The replay script is
`scripts/common_kernel_quotient_ellipsoid_diagnostic.py`, and its recorded
output is `results/common_kernel_quotient_ellipsoid_diagnostic.json`.
High-precision calculations gave:

| $M$ | $\log\lambda_1$ | $\log\lambda_2$ | log metric covolume |
|---:|---:|---:|---:|
| 20 | -14.0724 | -13.2770 | -27.3493 |
| 40 | -28.8564 | -28.8024 | -57.6738 |
| 60 | -45.0609 | -43.8189 | -88.8809 |
| 80 | -60.0780 | -59.6484 | -119.7436 |

The minor-semi-axis logs at the same degrees were approximately
$-30.2805,-60.5984,-91.8034,-122.6652$, while the major semiaxis stayed near
$1.16$.  The cheap-axis slope converged numerically to $-(e+\pi)$; at
$M=40$ the discrepancy was about $2.3\cdot10^{-28}$.

At $M=40$, Gauss reduction returned the exact coefficient basis



$$
(4984753974472,-29210032614300),
$$





$$
(-10232246126032,59959677967978),
$$



whose determinant is 16, the index of $8\mathbf Z\times2\mathbf Z$.  The
first ratio $-b/a$, after reduction, is continued-fraction convergent number
28 of $e+\pi$; the second is the following semiconvergent.  Thus the
ellipsoid reduction is numerically rediscovering ordinary rational
approximations to $e+\pi$.  This is useful confirmation of the rational-model
analysis, but it is not evidence for an independent all-degree theorem.

## 11. Sign and explicit-family obstructions

### 11.1 The root-interval label in the temporary probe

`sympy.Poly.intervals` returns isolating intervals for real roots.  The old
variable name `intervals_nonnegative` was misleading: it did not certify
nonnegativity.  The displayed candidates have simple roots in $(0,1)$ and
change sign.  Their finite nonvanishing is certified by rational bounds as in
Section 9, not by positivity.

### 11.2 Endpoint multiplicity

If $f\in\mathbf Z[x]$, $(1-x)^r\mid f$, and
$A(f)=f(i)=a\ne0$, then



$$
r!\mid a.                                       \tag{27}
$$



Indeed, all derivatives below order $r$ vanish at 1, and every derivative
of order at least $r$ is divisible by its factorial and hence by $r!$.

Let $N=\deg f$, put $z=-1+2i$, and set



$$
R=\left|z-\sqrt{z^2-1}\right|=4.611581789\ldots,
$$



choosing the square-root branch for which the modulus is greater than 1.
The shifted-Chebyshev expansion and its Fourier coefficient bounds give



$$
|f(i)|\le \frac{2R}{R-1}R^N\|f\|_{[0,1]}.
$$



Together with (27),



$$
\|f\|_{[0,1]}
\ge \frac{r!}{(2R/(R-1))R^N}.                   \tag{28}
$$



Thus any construction with $r\ge\delta N$ eventually has growing, not
shrinking, norm.  In particular, powers of $x(1-x)$ cannot provide the
desired nonzero-target all-degree family.

### 11.3 Perfect squares

If $P\in\mathbf Z[x]$ has degree $n$ and nonzero leading coefficient,
then (5) and Laguerre orthogonality give



$$
A(P^2)=\int_0^\infty e^{-t}P(1-t)^2dt\ge(n!)^2. \tag{29}
$$



The reason is that the monic degree-$n$ polynomial of least squared norm for
the weight $e^{-t}$ is $(-1)^n n!L_n(t)$, with squared norm $(n!)^2$.
If $A(P^2)=P(i)^2\ne0$, then $|P(i)|\ge n!$.  The same shifted-Chebyshev
bound as above yields



$$
\|P^2\|_{[0,1]}
\ge \frac{(n!)^2}{(2R/(R-1))^2R^{2n}},          \tag{30}
$$



which diverges.  Hence the most direct globally nonnegative square mechanism
cannot produce a shrinking common-kernel family.

There is also a Gaussian-integer obstruction to the other elementary positive
ansatz.  Put $q(x)=x(1-x)$.  If
$f=qP^2$ and $f(i)$ is real, write $P(i)=u+iv$ with
$u,v\in\mathbf Z$.  Since $q(i)=1+i$, reality requires



$$
u^2+2uv-v^2=0.
$$



The ratio $u/v=-1\pm\sqrt2$ is irrational unless $u=v=0$.  Thus this
ansatz has only the zero target.

These no-go statements do not rule out every polynomial nonnegative only on
$[0,1]$, but they explain why the obvious square and fixed-factor sign
constructions fail.

## 12. Remaining live statement

The exact two-form lemma is viable.  The finite saturated lattice supplies
many excellent independent pairs.  What is missing is an all-degree theorem
that makes both quotient minima tend to zero by an argument not already
equivalent to irrationality.  In the determinant formulation, the precise
missing estimate is (21).  The rational model and the continued-fraction
diagnostic show that no generic volume, determinant, HNF, LLL, or
transference estimate can be expected to prove it without additional
structure.
