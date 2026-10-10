> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 378 — top-symmetric transversality and the surviving cancellation tube

Checked: 2026-09-01 (Beijing time)

## 1. Verdict and capacity admission

Items 373 and 375 close nonconstant univariate first quotients in
$E_{N-1}$ and the constant/content remainder.  Item 378 treats bounded-degree
polynomials in a fixed number of actual top elementary symmetric coordinates



$$
T_s=E_{N-s}(Z),
\qquad
1\le s\le k,
\tag{1.1}
$$



where $k$ and the polynomial degree are fixed while $N$ grows.

The capacity admission is exact.  If a nonzero integral residual $R_n$ in
these coordinates satisfies



$$
\mathcal U_{1,1}(n)\mid R_n,
\qquad
\log|R_n|=o(\log b_n),
\tag{1.2}
$$



then the actual singleton-squarefree mass is zero-rate.  A strict fractional
height bound could also reduce capacity.  Thus a genuine sub-beta residual
would matter.

Item 378 proves the following strongest positivity theorem available for this
class.

* Positive singleton mass forces all fixed top coordinates $T_1,\ldots,T_k$
  onto one common beta-scale, with only $b^{o(1)}$ ratios between them.
* After primitive/content normalization, a polynomial is beta-scale whenever
  its leading homogeneous form is quantitatively transverse at the actual
  projective point.
* Transversality is automatic if the leading form becomes coefficientwise
  one-sign after the reciprocal substitution
  $T_s=P e_s(1/Z)$.  This cone strictly contains same-sign polynomials in the
  $T_s$ and includes mixed-sign Schur/Newton gaps.
* Every hypothetical sub-beta value outside the content branch forces the
  actual reciprocal point into an exponentially thin form-value tube around
  the leading projective cancellation variety.

Mixed-sign reciprocal transforms can have genuine positive zeros.  Positivity
alone does not exclude that variety, and no actual-family avoidance theorem is
proved.  No sub-beta actual carrier is constructed.  Booking remains zero.

## 2. Actual positive loads and singleton mass

Assume the genuine Item-316 target.  Remove exact-zero rows and write



$$
\mathcal J=\{j:Z_j\ne0\},
\qquad
N=|\mathcal J|,
\qquad
0<Z_j<A^2.
\tag{2.1}
$$



If $N<k$, omit nonexistent top coordinates; a positive-mass subsequence has
$N=\Omega(n)$ and hence $N\ge k$ eventually.  Put



$$
P=\prod_{j\in\mathcal J}Z_j,
\qquad
x_j=Z_j^{-1}.
\tag{2.2}
$$



The complement identity is



$$
\boxed{T_s=e_{N-s}(Z)=P e_s(x_1,\ldots,x_N).}
\tag{2.3}
$$



Assume along a subsequence that, for a fixed $\eta>0$,



$$
\log\mathcal U_{1,1}\ge\eta\log b.
\tag{2.4}
$$



Every prime counted by $\mathcal U_{1,1}$ lies in $(A,A^2)$, and one load
$Z_j<A^2$ cannot contain two such primes.  Therefore at least



$$
r\ge\frac{\eta\log b}{2\log A}
=\left(\frac\eta2+o(1)\right)n
\tag{2.5}
$$



distinct rows have $Z_j>A$.

## 3. A common beta-scale for all fixed top coordinates

Let



$$
M=T_1=E_{N-1}(Z).
\tag{3.1}
$$



One summand of $M$ omits at most one of the $r$ large rows, so



$$
\boxed{
M>A^{r-1},
\qquad
\log M\ge\left(\frac\eta2+o(1)\right)\log b.}
\tag{3.2}
$$



There is also an exact adjacent-ratio bound.  For $m=N-s$, double-counting
extensions of an $(m-1)$-subset gives



$$
m e_m(Z)
=\sum_{|I|=m-1}
\left(\prod_{i\in I}Z_i\right)
\left(\sum_{j\notin I}Z_j\right).
\tag{3.3}
$$



Since the inner sum has $s+1$ terms, each in $[1,A^2)$,



$$
\boxed{
\frac{N-s}{(s+1)A^2}
\le\frac{T_{s+1}}{T_s}
\le\frac{N-s}{s+1}
\qquad(1\le s<k).}
\tag{3.4}
$$



The coarse uniform consequence



$$
R_*^{-1}\le\frac{T_s}{M}\le R_*,
\qquad
R_*=(N A^2)^k,
\qquad
\log R_*=o(\log b)
\tag{3.5}
$$



holds for every fixed $s\le k$.  Thus all fixed top coordinates have the
same beta-scale.  Here $N\le n-4$ and
$\log b=(1+o(1))n\log A$, so the asserted estimate for $R_*$ follows.
This statement uses the actual positive loads and the positive
singleton-mass hypothesis, not an ambient independent-coordinate model.

## 4. Primitive multivariate transversality theorem

Let $C_n\in\mathbb Z[X_1,\ldots,X_k]$ be the primitive part after removing
integer coefficient content as in Item 375.  Assume



$$
1\le d=\deg C_n\le d_0,
\qquad
\|C_n\|_\infty\le B_n,
\qquad
\log B_n=o(\log b),
\tag{4.1}
$$



where $k,d_0$ are fixed.  Write



$$
C_n=H_{d,n}+H_{d-1,n}+\cdots+H_{0,n}
\tag{4.2}
$$



into homogeneous parts.  Let $D_n$ be a nonzero clearing denominator with
$1\le |D_n|\le B_n$, and assume $C_n(T)/D_n$ is a defined actual residual.

Call the leading form **transverse** along the subsequence if there is
$K_n\ge1$ with



$$
\log K_n=o(\log b),
\qquad
|H_{d,n}(T_1,\ldots,T_k)|\ge\frac{M^d}{K_n}.
\tag{4.3}
$$



The number of monomials of total degree at most $d_0$ is fixed.  Equations
(3.5) and (4.1) give



$$
\left|C_n(T)-H_{d,n}(T)\right|
\le L_{k,d_0}B_n(R_*M)^{d-1},
\qquad
L_{k,d_0}=\binom{k+d_0}{d_0}.
\tag{4.4}
$$



By (3.2),



$$
\frac{L_{k,d_0}B_nK_nR_*^{d-1}}M=o(1).
\tag{4.5}
$$



Hence, for large $n$,



$$
\boxed{
|C_n(T)|\ge\frac{M^d}{2K_n},
\qquad
\log\left|\frac{C_n(T)}{D_n}\right|
\ge\left(\frac{d\eta}{2}+o(1)\right)\log b.}
\tag{4.6}
$$



Thus a transverse nonconstant primitive polynomial is beta-scale.  Scalar
content cannot repair this: retaining content only increases numerator
height, while removing it is exactly Item 375's mandatory separation.

## 5. Reciprocal-positive leading forms

The transversality condition has a broad exact sufficient criterion.  Since
$H_{d,n}$ is homogeneous of ordinary coordinate degree $d$, define its
reciprocal transform



$$
\Phi_{d,n}(x_1,\ldots,x_N)
=H_{d,n}\bigl(e_1(x),\ldots,e_k(x)\bigr).
\tag{5.1}
$$



Equation (2.3) gives



$$
H_{d,n}(T)=P^d\Phi_{d,n}(x),
\qquad
M^d=P^d e_1(x)^d.
\tag{5.2}
$$



Suppose $\Phi_{d,n}$ is nonzero and all its nonzero monomial coefficients
have one sign.  Every coefficient has absolute value at least one, every
monomial has reciprocal degree at most $kd$, and



$$
A^{-2}<x_j\le1,
\qquad
e_1(x)\le N.
\tag{5.3}
$$



Therefore



$$
\boxed{
\frac{|H_{d,n}(T)|}{M^d}
=\frac{|\Phi_{d,n}(x)|}{e_1(x)^d}
\ge\frac{A^{-2kd}}{N^d}.}
\tag{5.4}
$$



The reciprocal of the right side has logarithm $O_{k,d}(\log A+\log N)
=o(\log b)$, so (4.3) is automatic.

Call these leading forms the **reciprocal-positive cone**.  It contains every
form whose coefficients in the $X_s$ already have one sign, because every
$e_s(x)$ has positive monomial coefficients.  It also contains genuinely
mixed-sign forms after cancellation in the elementary-symmetric basis.

## 6. A mixed-sign family closed exactly

For $2\le s\le k-1$, consider



$$
G_s(X)=X_s^2-X_{s-1}X_{s+1}.
\tag{6.1}
$$



Its reciprocal transform is



$$
e_s(x)^2-e_{s-1}(x)e_{s+1}(x)
=s_{(2^s)}(x),
\tag{6.2}
$$



by the dual Jacobi--Trudi identity.  The Schur polynomial on the right is the
sum of tableau monomials and has nonnegative integer coefficients.  It is
nonzero and strictly positive at the actual positive reciprocal point.
Consequently (5.4) applies:



$$
\boxed{
T_s^2-T_{s-1}T_{s+1}
\text{ is beta-scale on every positive-singleton-mass subsequence}.}
\tag{6.3}
$$



Thus mixed signs in the displayed $T$-coordinates do not by themselves create
a live cancellation mechanism.  The relevant sign test is after reciprocal
expansion.

For $s=1$, the analogous identity uses $T_0=P$ and is available when the
already existing product coordinate is admitted.  Equation (6.3) stays
strictly inside $T_1,\ldots,T_k$ by taking $s\ge2$.

## 7. The surviving projective cancellation tube

Let $H_{d,n}$ now have a mixed-sign reciprocal transform.  Suppose a nonzero
actual value is sub-beta:



$$
0<\left|\frac{C_n(T)}{D_n}\right|=b^{o(1)}.
\tag{7.1}
$$



Equations (4.4) and (5.2) imply the exact form-value estimate



$$
\begin{aligned}
\frac{|\Phi_{d,n}(x)|}{e_1(x)^d}
&=\frac{|H_{d,n}(T)|}{M^d}\\
&\le
\frac{|C_n(T)|}{M^d}
+\frac{L_{k,d_0}B_nR_*^{d-1}}M.
\end{aligned}
\tag{7.2}
$$



Under (7.1), the first numerator is also $b^{o(1)}$.  Hence (3.2) gives



$$
\boxed{
\frac{|\Phi_{d,n}(1/Z)|}{e_1(1/Z)^d}
\le b^{-\eta/2+o(1)}.}
\tag{7.3}
$$



This is the exact surviving obstruction.  The actual positive projective
point must enter an exponentially thin **form-value tube** around



$$
\boxed{
\mathcal V_{H_n}:\quad
H_{d,n}(T_1,\ldots,T_k)=0,
\quad\text{equivalently}\quad
\Phi_{d,n}(1/Z)=0.}
\tag{7.4}
$$



No Euclidean distance claim is made; gradients may degenerate.  Equation
(7.3) is the invariant statement.  If the leading form vanishes exactly, the
effective degree drops and the same analysis applies to the next nonzero
homogeneous layer.  Reaching a constant after all such drops is precisely the
content/scalar boundary closed in Item 375.

## 8. Why positivity alone cannot remove the variety

The cancellation variety really meets the positive top-symmetric image.  As a
predeclared ambient control, take $N$ odd and $Z_1=\cdots=Z_N=1$.  Then



$$
T_1=N,
\qquad
T_2=\binom N2,
\qquad
2T_2-(N-1)T_1=0.
\tag{8.1}
$$



Thus the primitive polynomial



$$
C_N(X_1,X_2)=2X_2-(N-1)X_1+1
\tag{8.2}
$$



has coefficient height $O(N)$ and the nonzero value $C_N(T)=1$.  Its leading
reciprocal transform has mixed signs and vanishes at the positive point.

This is not an actual beta target: it has no singleton prime mass and is not
promoted to density evidence.  It proves only that positivity and bounded
degree cannot logically replace an actual-family avoidance theorem.  The
positive singleton-mass hypothesis makes $M$ beta-scale, but it does not by
itself prove that the moving canonical reciprocal point avoids every moving
mixed-sign hypersurface (7.4).

## 9. Capacity decision and exact scope

Item 378 closes:

1. all bounded-degree primitive polynomials whose leading form is transverse
   in the sense of (4.3);
2. the entire reciprocal-positive cone, including same-sign coordinate forms;
3. mixed-sign Schur gaps (6.1) and finite products whose leading reciprocal
   transform remains one-sign;
4. sub-beta clearing denominators as an escape from those lower bounds;
5. scalar content as a hidden gain, by Item 375.

The only surviving bounded-degree multivariate class consists of mixed-sign
reciprocal transforms for which the actual canonical point satisfies (7.3),
with exact cancellation (7.4) as its core.  Proving weighted avoidance of
that tube, or deriving a canonical polynomial that actually lies in it and
has the required $\mathcal U_{1,1}$ divisibility, is a new arithmetic problem.

No actual residual satisfying (1.2) is constructed, and no upper bound for
$\mathcal U_{1,1}$ follows merely from the class closure.  Therefore



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{9.1}
$$



## 10. Strict labels

### PROVED

* The actual common-scale theorem (3.2)-(3.5).
* The primitive multivariate transversality theorem (4.3)-(4.6).
* The reciprocal-positive criterion (5.1)-(5.4).
* The mixed-sign Schur-gap corollary (6.1)-(6.3).
* The necessary cancellation-tube estimate (7.2)-(7.4).
* Zero booking.

### PROVED SCOPED NO-GO

* Reciprocal-positive bounded-degree top-symmetric residuals as sub-beta
  carriers on a positive-singleton-mass subsequence.
* Same-sign leading forms, Schur gaps, and sub-beta denominators in this
  class.
* Primitive/content normalization as an escape from the scale theorem.

### EXACT FINITE ONLY

* The replay's predeclared positive loads, elementary-symmetric identities,
  reciprocal transforms, Schur gaps, cancellation examples, and scale boxes.
* The all-one cancellation point is ambient only and is not an actual beta
  target or density datum.

### OPEN

* Actual-family avoidance of the mixed-sign tube (7.3).
* A canonical mixed-sign polynomial with genuine $\mathcal U_{1,1}$
  divisibility and sub-beta nonzero value.
* Growing $k$ or degree, beta-height denominators, and nonlinear gcd/radical
  compression.
* The singleton bound, $\Xi_Q$, squarefull excess, beta capacity, Route 1,
  and $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{10.1}
$$



No canonical, master, status, checkpoint, research-log, or audit file is
edited by this work package.

## 11. Deterministic replay

From the archive root:

~~~text
python work/item378_beta_top_symmetric_multivariate_cancellation_certificate.py ^
  --output work/item378_beta_top_symmetric_multivariate_cancellation_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer/rational
arithmetic.  All loads, forms, and scale controls are predeclared.  It performs
no actual prime census, target search, factor search, or half-bound scan.
