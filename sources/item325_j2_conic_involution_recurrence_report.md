> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 325 - conic involution, complete moments, and the irreducible moving-exponent state

Checked: 2026-09-01 (Beijing time)

## 1. Scope and verdict

Retain the actual ordinary-$j=2$ rows



$$
p=2r+6s+3,\qquad r\geq1\text{ odd},\qquad 3\nmid r,\qquad s\geq1,
 \tag{1.1}
$$



and the fixed-$M$ relation



$$
2M=5r+14s+7.                 \tag{1.2}
$$



Put



$$
n=\frac{p-1}{2},\qquad m=s-1,\qquad
 q=n-m=r+2s+2=2(M-p)+1,                               \tag{1.3}
$$





$$
h_j=\frac{(1/2)_j}{j!2^j},\qquad H_m=\sum_{j=0}^m h_j,
 \qquad \epsilon=\left(\frac2p\right).               \tag{1.4}
$$



Item 322 proves, on the $\ell_r\ne0\pmod p$ chart after the old
determinant gate $D_{r,s}=0$, that the original collision is equivalent
to



$$
H_m=\Theta_{r,s}\pmod p.       \tag{1.5}
$$



It also writes $H_m$ as a rationally weighted moment on the fixed conic
but leaves open identities that work only after summation.  This item finds
such an identity and then audits its exact limitation.

Define



$$
K_p(x)=\chi\!\left(x(1-x/2)\right),\qquad
 W_q=\sum_{x\in\mathbf F_p\setminus\{0,1\}}
       \frac{x^qK_p(x)}{1-x}.                         \tag{1.6}
$$



The actual exponent is always odd and satisfies



$$
\frac p3<q\le n.              \tag{1.7}
$$



> **PROVED - the puncture disappears after the conic involution.**  Put
> 

$$
> R_q(x)=\frac{x^q-(2-x)^q}{2(1-x)}.
> \tag{1.8}
>
$$


> This is a polynomial, $R_q(1)=-q$, and
> 

$$
> \boxed{
> H_{n-q}=\epsilon-
> \sum_{x\in\mathbf F_p}R_q(x)K_p(x).}
> \tag{1.9}
>
$$


> Thus Item 322's punctured rational moment has an exact
> summation-specific completion on the fixed conic.

> **PROVED - every complete centered moment is explicit.**  Since $q$
> is odd,
> 

$$
> R_q(1+y)=-\sum_{j=0}^{(q-1)/2}\binom q{2j+1}y^{2j},
> \tag{1.10}
>
$$


> and, throughout this range of $j$,
> 

$$
> \sum_{y\in\mathbf F_p}y^{2j}\chi(1-y^2)
> =-(-1)^{n-j}\binom nj.                              \tag{1.11}
>
$$


> Consequently the actual period has the exact terminating form
> 

$$
> \boxed{
> H_{n-q}=\epsilon\left\{1-(-1)^n
> \sum_{j=0}^{(q-1)/2}(-1)^j
> \binom q{2j+1}\binom nj\right\}.}                  \tag{1.12}
>
$$



> **PROVED - exact moving-exponent state.**  If
> 

$$
> T_q=\sum_{x\in\mathbf F_p}x^qK_p(x),\qquad
> Y_q=H_{n-q},                                        \tag{1.13}
>
$$


> then, for $0\le q<n$,
> 

$$
> \boxed{
> \begin{pmatrix}Y_{q+1}\\T_{q+1}\end{pmatrix}
> =
> \begin{pmatrix}
> 1&1\\
> 0&\dfrac{2q+1}{q+1}
> \end{pmatrix}
> \begin{pmatrix}Y_q\\T_q\end{pmatrix},}
> \tag{1.14}
>
$$


> with the explicit seed
> 

$$
> Y_0=\epsilon,\qquad T_0=-(-1)^n\epsilon.            \tag{1.15}
>
$$


> Every diagonal factor in the actual range is a unit.

> **PROVED - sharp bounded-complexity limitations.**
>
> 1. The punctured pointwise weight has all $p-1$ multiplicative
>    Fourier modes nonzero.
> 2. The orbit polynomial $R_q$ has minimal possible degree $q-1$
>    on the active conic points.  On actual rows this is
>    $q-1>p/3-1$.
> 3. Formula (1.12) has exactly $(q+1)/2>p/6$ nonzero centered modes;
>    neither their coefficients nor their individual complete moments
>    vanish.
> 4. The rank-two system (1.14) has no rational rank-one gauge of uniformly
>    bounded degree.  In characteristic $p$, any such gauge has reduced
>    denominator degree at least $(p-1)/2$.

The summation-specific identity is therefore real, but it does not create
a fixed-size trace or a weighted zero theorem.  The strict ledger effect is



$$
\boxed{\text{new capacity reduction}=0},\qquad
 \boxed{\text{new booking}=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling}=1/105\text{ per }6M}.
 \tag{1.16}
$$



## 2. Admission, actual implication, and raw capacity

The theorem is admitted only after both earlier logical gates:

1. the old coefficient determinant $D_{r,s}=0$; and
2. the nondegenerate chart $\ell_r\ne0\pmod p$.

On this locus Item 322 gives the exact unit factorization



$$
\mathcal E_{r,s}=
 \ell_rB_s\frac{9\kappa_r}{2}(-1)^m\epsilon
 (H_m-\Theta_{r,s})\pmod p.                           \tag{2.1}
$$



Substitution of (1.12) therefore proves the actual-family implication



$$
\boxed{
 \text{original collision}\Longleftrightarrow
 \Theta_{r,s}=\epsilon\left\{1-(-1)^n
 \sum_{j=0}^{(q-1)/2}(-1)^j
 \binom q{2j+1}\binom nj\right\}\pmod p.}
 \tag{2.2}
$$



This is not an auxiliary condition invented independently of the original
collision.  Conversely, it remains internal to the already retained
ordinary-$j=2$ branch and cannot be booked as new mass.

Item 322 proves that rows usable through an adjacent $p,p+6$ transfer
have $o(M)$ logarithmic mass.  Removing that zero-rate subfamily leaves
the isolated single-row complement with the same raw ceiling



$$
\mathcal C_{\max}=\frac1{105}
 =0.009523809523809523\ldots\quad\text{per }6M.        \tag{2.3}
$$



Even perfect closure of this branch could only remove (2.3); it could not
increase the booked lower bound.  The present identities do not bound the
prime support of (2.2), so they remove none of it.

The $\ell_r=0$ chart and the rank-at-most-one connection chart are not
discarded.  They remain outside (2.1)-(2.2) and require the division-free
residual or an individual coordinate, exactly as in Items 318 and 322.

## 3. The conic involution removes the puncture after summation

The conic kernel is invariant under the affine involution



$$
\iota(x)=2-x,
 \qquad
 (2-x)\left(1-\frac{2-x}{2}\right)
 =x\left(1-\frac x2\right).
 \tag{3.1}
$$



The points $x=0,2$ have $K_p(x)=0$.  Thus the domain in (1.6) can be
regarded as $\mathbf F_p\setminus\{1\}$ without changing the sum.  After
the substitution $x\mapsto2-x$,



$$
W_q=-\sum_{x\ne1}\frac{(2-x)^qK_p(x)}{1-x}.          \tag{3.2}
$$



Averaging (1.6) and (3.2) gives



$$
W_q=\sum_{x\ne1}R_q(x)K_p(x).                       \tag{3.3}
$$



The numerator in (1.8) vanishes at $x=1$, so $R_q$ is a polynomial.
L'Hopital's elementary polynomial limit gives



$$
R_q(1)=-q.                   \tag{3.4}
$$



Also $K_p(1)=\chi(1/2)=\epsilon$.  Hence



$$
W_q=\sum_{x\in\mathbf F_p}R_q(x)K_p(x)+q\epsilon.   \tag{3.5}
$$



Item 322's exact relation



$$
H_{n-q}=\epsilon(q+1)-W_q    \tag{3.6}
$$



now proves (1.9).  The endpoint $x=1$ is responsible for the surviving
$\epsilon$; it has not been silently omitted.

This does not contradict Item 322's pointwise rational-degree barrier.
The denominator disappears only after pairing the two points in each
$\iota$-orbit and retaining the endpoint correction.

## 4. Complete centered moments and the binomial convolution

Write $x=1+y$.  Since actual $q$ is odd,



$$
\begin{aligned}
 R_q(1+y)
 &=\frac{(1+y)^q-(1-y)^q}{-2y}\\
 &=-\sum_{j=0}^{(q-1)/2}\binom q{2j+1}y^{2j},
\end{aligned}                                               \tag{4.1}
$$



which proves (1.10).  The shifted kernel is



$$
K_p(1+y)=\epsilon\chi(1-y^2).                         \tag{4.2}
$$



For $0\le j\le(q-1)/2\le(n-1)/2$, Euler's criterion gives



$$
\begin{aligned}
 M_j
 &:=\sum_y y^{2j}\chi(1-y^2)\\
 &=\sum_{k=0}^n(-1)^k\binom nk
       \sum_y y^{2(j+k)}.                              \tag{4.3}
\end{aligned}
$$



In the indicated range, $2(j+k)$ reaches a positive multiple of
$p-1=2n$ only when $k=n-j$.  The corresponding power sum is $-1$,
while all others are zero.  Therefore



$$
M_j=-(-1)^{n-j}\binom n{n-j}
    =-(-1)^{n-j}\binom nj,                             \tag{4.4}
$$



which proves (1.11).  Substitution of (4.1), (4.2), and (4.4) into (1.9)
gives (1.12).

Every binomial coefficient in (1.12) is nonzero modulo $p$, because



$$
0\le j\le n<p,\qquad 1\le2j+1\le q<p.                \tag{4.5}
$$



Thus the direct centered expansion has exactly $(q+1)/2$ nonzero terms,
and every complete moment (4.4) is nonzero.  This is not a noncancellation
theorem for their total.  Exact cancellations remain possible and are the
arithmetic issue in (2.2).

## 5. Two sharp linear-complexity barriers

### 5.1 Full pointwise multiplicative Fourier support

On $\mathbf F_p^*$, define the punctured weight by



$$
u_q(1)=0,\qquad u_q(x)=\frac{x^q}{1-x}\quad(x\ne1).   \tag{5.1}
$$



The exact polynomial-function identity is



$$
\boxed{
 u_q(x)=x^q\sum_{k=0}^{p-2}(k+1)x^k.}                 \tag{5.2}
$$



At $x=1$, the right side is
$1+2+\cdots+(p-1)=0\pmod p$.  At $x\ne1$, let
$S(x)=1+x+\cdots+x^{p-2}$.  Then $S(x)=0$ and differentiation of
$(x-1)S(x)=x^{p-1}-1$ gives



$$
S(x)+xS'(x)=\frac1{1-x},                            \tag{5.3}
$$



which is (5.2).  All coefficients $1,2,\ldots,p-1$ are nonzero, and
multiplication by $x^q$ only permutes the $p-1$ exponent classes.
Since these monomials are the unique multiplicative Fourier basis on
$\mathbf F_p^*$, the support is exactly $p-1$.

Consequently ordinary pointwise Mellin completion cannot express the
punctured weight with a bounded number of character modes.  The involution
of Section 3 is a genuine summation-specific operation, not a sparse
pointwise Fourier rewrite.

### 5.2 Minimal degree after orbit averaging

For odd $q$, the numerator of (1.8) has leading coefficient $2$, so



$$
\deg R_q=q-1.                 \tag{5.4}
$$



Suppose a polynomial of degree smaller than $q-1$ agreed with $R_q$
at every active nonendpoint conic point
$x\in\mathbf F_p\setminus\{0,1,2\}$.  Their difference would have
$p-3$ roots but degree $q-1\le(p-3)/2<p-3$, so it would be the zero
polynomial, contradicting its degree.  Thus $q-1$ is the exact minimal
degree even after exploiting the conic involution.

The actual inequalities (1.7) imply



$$
\deg R_q=q-1>\frac p3-1,
 \qquad \frac{q+1}{2}>\frac p6.                       \tag{5.5}
$$



The puncture is gone, but linear complexity remains.

## 6. Exact rank-two recurrence and rank-one gauge barrier

Define $T_q$ as in (1.13).  Pointwise in $\mathbf F_p$,



$$
K_p(x)=x^n(1-x/2)^n.                                  \tag{6.1}
$$



Expanding the second factor and using finite-field power sums shows that,
for $0\le q\le n$, only the term with index $n-q$ survives.  Hence



$$
\boxed{T_q=-h_{n-q}.}                                  \tag{6.2}
$$



It follows that



$$
\frac{T_{q+1}}{T_q}
 =\frac{h_{n-q-1}}{h_{n-q}}
 =\frac{4(n-q)}{2(n-q)-1}
 =\frac{2q+1}{q+1}\pmod p.                            \tag{6.3}
$$



Also



$$
\begin{aligned}
 W_{q+1}-W_q
 &=\sum_{x\ne0,1}\frac{x^{q+1}-x^q}{1-x}K_p(x)\\
 &=\epsilon-T_q.                                       \tag{6.4}
\end{aligned}
$$



Together with $Y_q=\epsilon(q+1)-W_q$, equation (6.4) gives
$Y_{q+1}=Y_q+T_q$, proving (1.14).  Finally,



$$
H_n=(1-1/2)^n=\epsilon,qquad
 T_0=-h_n=-(-1)^n\epsilon,                             \tag{6.5}
$$



which proves the initialized state (1.15).

The recurrence is bounded-rank, but it still contains the accumulated
period coordinate $Y_q$.  A rational triangular gauge that made



$$
I_q=Y_q-R(q)T_q               \tag{6.6}
$$



constant would have to solve



$$
\boxed{
 \frac{2x+1}{x+1}R(x+1)-R(x)=1.}                      \tag{6.7}
$$



There is no rational solution in characteristic zero.  Indeed, a finite
translation chain of poles could end only at the zero $-1/2$ or the pole
$-1$ of the coefficient; those two points are not congruent modulo
$\mathbf Z$.  Thus $R$ would be a polynomial.  Positive degree is
impossible from the leading term at infinity.  A constant would have to be
$1$ at infinity and $-1$ at $x=-1/2$, a contradiction.

Now work over $\overline{\mathbf F}_p$, $p\ge5$.  Translation orbits
have length $p$.  A pole on an orbit not containing $-1/2,-1$ repeats
at all $p$ points.  On the exceptional orbit put



$$
z=-\frac12,\qquad w=-1=z+\frac{p-1}{2}.               \tag{6.8}
$$



Away from $z,w$, neighboring pole orders are equal.  The simple zero at
$z$ and simple pole at $w$ force the order on



$$
z+1,z+2,\ldots,w                                      \tag{6.9}
$$



to exceed the order on the complementary arc by one.  If a finite pole
exists, the least profile therefore consists of one simple pole at each of
the $(p-1)/2$ points in (6.9).  If no finite pole exists, the same
polynomial contradiction as above applies.  Thus every rational solution,
if one exists, satisfies



$$
\boxed{\deg\operatorname{den}R\ge\frac{p-1}{2}.}       \tag{6.10}
$$



This is the moving-exponent counterpart of Item 252's scalar Gosper
barrier.  The exact rank-two recurrence exists, but a uniformly
bounded-degree rational rank-one reduction does not.

## 7. Why this does not yield weighted zero density

Three distinct facts must not be conflated:

1. Equation (1.9) removes the rational puncture after summation.
2. Equation (1.14) gives an exact initialized rank-two recurrence.
3. Neither equation bounds primes for which the actual target (2.2) is
   met.

The polynomial degree, direct moment count, and rank-one gauge degree all
grow linearly with $p$.  Moreover the fixed-$M$ step of Item 322 changes
the collision modulus from $p$ to $p+6$, whereas (1.14) lives inside a
single field $\mathbf F_p$.  Finally, no recurrence for the connection
target $\Theta_{r,s}$ matching (1.14) is proved.

Thus the result closes the following proposed shortcuts:

* bounded-support pointwise multiplicative Fourier completion;
* bounded-degree polynomial compression after the conic involution; and
* bounded-degree rational rank-one scalarization of the exact
  moving-exponent system.

It does **not** close a higher-rank arithmetic construction that uses the
actual connection target, a nonlinear factorization of the terminating
convolution, an average gcd theorem, or a weighted zero-density theorem.

## 8. Deterministic replay

The standard-library checker verifies the actual formulas on every declared
row through $p\le199$, including direct conic and centered-moment sums.
It verifies the initialized recurrence on every exponent for every prime
through $149$, and the pointwise full-Fourier identity through $89$.
It separately verifies the exceptional pole-orbit length in (6.9).

All row counts, samples, and digests are **EXACT FINITE ONLY**.  The
all-prime theorems are the involution, power-sum, root-count, recurrence,
and pole-orbit proofs above.

## 9. Strict labels

**PROVED**

* the exact conic-involution completion (1.9);
* the complete centered moments (1.11) and binomial convolution (1.12);
* the actual collision reformulation (2.2) on the declared chart;
* full pointwise multiplicative Fourier support;
* exact minimal orbit-polynomial degree $q-1$;
* the exact initialized rank-two recurrence (1.14)-(1.15);
* the rank-one rational-gauge barrier (6.10); and
* zero capacity booking and zero capacity reduction.

**EXACT FINITE ONLY / DIAGNOSTIC**

* every bounded replay count, sample, and digest in the certificate.

**OPEN**

* weighted zero density for (2.2) after the determinant gate;
* cancellation or factor localization in (1.12);
* a higher-rank arithmetic invariant coupled to $\Theta_{r,s}$;
* control of the $\ell_r=0$ and rank-at-most-one charts;
* any reduction of the retained $1/105$ ceiling; and
* any new Route-1 booking or conclusion about $e+\pi$.
