> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 381 — binary norms, ternary Newton stability, and the first live conics

Checked: 2026-09-01 (Beijing time)

## 1. Verdict and admission

Item 378 proves that every bounded-degree top-symmetric residual is beta-scale
unless its leading reciprocal form enters an exponentially thin mixed-sign
cancellation tube.  Item 381 classifies the first such varieties: homogeneous
quadratic forms in the top two or three coordinates



$$
T_s=E_{N-s}(Z)=P e_s(x),
\qquad
x_j=Z_j^{-1}>0.
\tag{1.1}
$$



The results are as follows.

1. Binary quadratics admit a complete discriminant classification.  Definite
   forms are quantitatively beta-scale.  Rationally split forms reduce to
   explicit positive cancellation lines.  Irreducible indefinite forms never
   vanish at the rational actual point, but can be Pell-small; their exact
   lower bound is controlled by $\gcd(T_1,T_2)^2$ and a primitive norm.
2. For ternary quadratics, the coefficientwise reciprocal-positive cone can
   be written by six explicit inequalities.
3. The sharper normalized Newton boundary, which is outside that
   coefficientwise cone, satisfies an exact sum-of-squares identity.  Two
   distinct singleton rows force a $b^{o(1)}$ quantitative separation, so this
   entire boundary is beta-scale.
4. Definite ternary forms are beta-scale by an integral eigenvalue bound.
5. General indefinite ternary conics remain live.  An explicit irreducible
   conic vanishes at a positive unequal-load point strictly inside the Newton
   cone.  Thus positivity, digit bounds, and Newton inequalities alone cannot
   exclude actual mixed-sign isotropy.

No actual canonical cancellation carrier is constructed.  The surviving
arithmetic is a primitive norm/isotropy problem at the moving actual point.
Booking remains zero.

## 2. Actual scale and notation

Assume the genuine Item-316 target and a positive-singleton-mass subsequence



$$
\log\mathcal U_{1,1}\ge\eta\log b
\tag{2.1}
$$



for fixed $\eta>0$.  Item 378 proves, with $M=T_1$ and fixed $s$,



$$
\log M\ge\left(\frac\eta2+o(1)\right)\log b,
\qquad
R_*^{-1}\le\frac{T_s}{M}\le R_*,
\qquad
R_*=b^{o(1)}.
\tag{2.2}
$$



All polynomial coefficient contents are first separated as in Item 375.  The
forms below are primitive, have coefficient height



$$
B_n=b^{o(1)},
\tag{2.3}
$$



and may be divided only by a clearing denominator of the same sub-beta
height.  Such a denominator does not change a beta-scale lower bound.

The exact actual ratio interval for the binary chart is inherited from
Item 378:



$$
\boxed{
\frac{N-1}{2A^2}
\le u:=\frac{T_2}{T_1}=\frac{e_2(x)}{e_1(x)}
\le\frac{N-1}{2}.}
\tag{2.4}
$$



## 3. Complete binary quadratic classification

Let



$$
Q(X,Y)=aX^2+bXY+cY^2,
\qquad
\gcd(a,b,c)=1,
\qquad
\Delta=b^2-4ac.
\tag{3.1}
$$



### 3.1 Definite forms

If $\Delta<0$, then $a$ and $c$ have the same sign and $Q$ is definite.
After replacing $Q$ by $-Q$ if necessary, $a>0$ and



$$
4aQ(X,Y)
=(2aX+bY)^2+(4ac-b^2)Y^2.
\tag{3.2}
$$



Since $4ac-b^2$ is a positive integer and $a\le B_n$,



$$
\boxed{
|Q(T_1,T_2)|
\ge\frac{T_2^2}{4B_n}
\ge\frac{M^2}{4B_nR_*^2}
=b^{\eta+o(1)}.}
\tag{3.3}
$$



Thus every irreducible definite binary form is closed.

### 3.2 Square discriminant

If $\Delta=s^2$ is a square and $a\ne0$, then



$$
4aQ(X,Y)
=\bigl(2aX+(b-s)Y\bigr)
 \bigl(2aX+(b+s)Y\bigr).
\tag{3.4}
$$



Hence the only exact positive zeros are the rational lines



$$
\frac YX=-\frac{2a}{b-s}
\quad\text{or}\quad
\frac YX=-\frac{2a}{b+s},
\tag{3.5}
$$



when the displayed ratio is positive.  The cases $a=0$ and $\Delta=0$
reduce to the same linear-factor statement directly.

If neither positive line meets the interval (2.4), and its distance from that
interval is at least $b^{-o(1)}$, both factors have beta-scale magnitude and
$Q(T)$ is beta-scale.  If a line meets the interval, positivity does not
exclude



$$
q_nT_2-r_nT_1=0
\tag{3.6}
$$



with sub-beta integers $q_n,r_n$.  This is an actual one-point correlation,
not a generic symmetric identity.

### 3.3 Nonsquare indefinite forms

Assume $\Delta>0$ is not a square.  Then $Q$ is irreducible over
$\mathbb Q$ and cannot vanish at the rational point $T_2/T_1$.  Put



$$
g_{12}=\gcd(T_1,T_2),
\qquad
T_1=g_{12}q,
\qquad
T_2=g_{12}r,
\qquad
\gcd(q,r)=1.
\tag{3.7}
$$



The exact norm factorization is



$$
\boxed{
Q(T_1,T_2)=g_{12}^2Q(q,r),
\qquad
Q(q,r)\in\mathbb Z\setminus\{0\},
\qquad
|Q(T_1,T_2)|\ge g_{12}^2.}
\tag{3.8}
$$



If the two real roots are not positive, all three coefficients have one sign
up to an overall sign, so Item 378 already closes the form.  The only live
irreducible binary forms have a positive irrational root meeting or
approaching (2.4).

Bound (3.8) is sharp at the level of positive rational points: Pell equations
such as



$$
q^2-2r^2=\pm1
\tag{3.9}
$$



have arbitrarily large positive solutions.  Therefore positivity and
coefficient height cannot improve (3.8).  A sub-beta actual value in this
class requires both



$$
g_{12}=b^{o(1)}
\quad\text{and}\quad
|Q(q,r)|=b^{o(1)}.
\tag{3.10}
$$



Controlling this moving primitive norm is the exact surviving binary
arithmetic statistic.

## 4. Exact ternary reciprocal-positive cone

Write a primitive ternary quadratic as



$$
\begin{aligned}
Q(X_1,X_2,X_3)
={}&aX_1^2+bX_1X_2+cX_1X_3+dX_2^2\\
&+eX_2X_3+fX_3^2.
\end{aligned}
\tag{4.1}
$$



For $N\ge4$, substitute $X_s=e_s(x)$.  Terms of reciprocal weights
$2,3,5,6$ inherit the signs of $a,b,e,f$.  At weight $4$, the coefficients of
the monomial types $(2,2)$, $(2,1,1)$, and $(1,1,1,1)$ are respectively



$$
d,
\qquad
c+2d,
\qquad
4c+6d.
\tag{4.2}
$$



Consequently the reciprocal transform is coefficientwise nonnegative if and
only if



$$
\boxed{
a,b,d,e,f\ge0,
\qquad
2c+3d\ge0.}
\tag{4.3}
$$



It is coefficientwise nonpositive if and only if all inequalities in (4.3)
are reversed.  This is an exact classification, because $d\ge0$ and
$2c+3d\ge0$ automatically imply $c+2d\ge0$.

Every nonzero form satisfying (4.3), or its negative version, is beta-scale by
Item 378.  Thus the first ternary cancellation variety must lie outside this
six-inequality cone.

## 5. Exact stability of the normalized Newton boundary

The sharp $e_1,e_2,e_3$ Newton inequality gives the mixed-sign form



$$
\mathcal G_N(X)
=2(N-2)X_2^2-3(N-1)X_1X_3.
\tag{5.1}
$$



It is outside (4.3), yet it admits an exact stability identity.  For
$i\ne j$, let



$$
e_r^{(ij)}=e_r(x_h:h\notin\{i,j\}).
\tag{5.2}
$$



Direct coefficient comparison in reciprocal degree four gives



$$
\boxed{
2(N-2)e_2^2-3(N-1)e_1e_3
=\sum_{i<j}(x_i-x_j)^2
\left(\bigl(e_1^{(ij)}\bigr)^2-e_2^{(ij)}\right).}
\tag{5.3}
$$



The kernel is positive:



$$
\bigl(e_1^{(ij)}\bigr)^2-e_2^{(ij)}
=\sum_{h\ne i,j}x_h^2
+\sum_{\substack{h<\ell\\h,\ell\ne i,j}}x_hx_\ell>0.
\tag{5.4}
$$



Positive singleton mass supplies two distinct singleton rows $i,j$ for large
$n$.  Their loads are distinct: one integer below $A^2$ cannot contain their
two distinct primes larger than $A$.  Hence



$$
|x_i-x_j|
=\frac{|Z_i-Z_j|}{Z_iZ_j}>A^{-4}.
\tag{5.5}
$$



There is at least one outside row, and every outside reciprocal exceeds
$A^{-2}$.  Keeping only that square in (5.4) yields



$$
2(N-2)e_2^2-3(N-1)e_1e_3>A^{-12}.
\tag{5.6}
$$



Since $T_s=P e_s$ and $M=P e_1$,



$$
\boxed{
\frac{\mathcal G_N(T_1,T_2,T_3)}{M^2}
>\frac{A^{-12}}{N^2}=b^{-o(1)}.}
\tag{5.7}
$$



Thus the normalized Newton boundary is quantitatively separated by the
actual singleton incidence and is beta-scale.  This is stronger than merely
noting strict Newton inequality.

More generally, a nonnegative sub-beta linear combination of a
reciprocal-positive ternary quadratic and $\mathcal G_N$ remains beta-scale,
provided the two certified pieces have the same sign.  Call this the
**Newton-certified quadratic cone**.

## 6. Definite ternary forms

Associate to (4.1) the doubled integral symmetric matrix



$$
\mathsf A_Q=
\begin{pmatrix}
2a&b&c\\
b&2d&e\\
c&e&2f
\end{pmatrix},
\qquad
2Q(T)=T^{\mathsf T}\mathsf A_QT.
\tag{6.1}
$$



If $\mathsf A_Q$ is positive or negative definite, then
$|\det\mathsf A_Q|\ge1$.  Its two largest singular values are at most $6B_n$,
so its smallest absolute eigenvalue is at least $(6B_n)^{-2}$.  Therefore



$$
\boxed{
|Q(T_1,T_2,T_3)|
\ge\frac{M^2}{72B_n^2}
=b^{\eta+o(1)}.}
\tag{6.2}
$$



Every definite irreducible ternary conic is closed.

## 7. Irreducible conics that really survive

Indefinite ternary forms behave differently from binary forms: an irreducible
nonsingular conic can have positive rational zeros.  This already occurs
strictly inside the positive Newton cone.

Take the predeclared positive unequal loads



$$
(Z_1,Z_2,Z_3,Z_4)=(1,1,2,2).
\tag{7.1}
$$



They give



$$
(T_1,T_2,T_3)=(12,13,6)
\tag{7.2}
$$



and the nonsingular quadratic



$$
\boxed{169X_1X_3-72X_2^2=0.}
\tag{7.3}
$$



The normalized Newton gap is strictly positive:



$$
2(N-2)T_2^2-3(N-1)T_1T_3
=4\cdot169-9\cdot72=28.
\tag{7.4}
$$



Thus (7.3) is not a Newton-boundary artifact.  Its matrix has nonzero
determinant, so the quadratic is irreducible over $\mathbb Q$.  Adding a
constant $1$ gives a primitive bounded-height polynomial with value $1$ at
this ambient positive point.

This example has no positive singleton mass and is not promoted to the actual
beta family.  It proves that positivity, unequal loads, and strict Newton
inequalities do not logically exclude irreducible conic cancellation.

For a general ternary form, put



$$
g_{123}=\gcd(T_1,T_2,T_3),
\qquad
T=g_{123}v,
\qquad
\gcd(v_1,v_2,v_3)=1.
\tag{7.5}
$$



Then



$$
\boxed{Q(T)=g_{123}^2Q(v).}
\tag{7.6}
$$



If $Q$ is anisotropic at the actual rational point, $Q(v)$ is a nonzero
integer and (7.6) gives only $|Q(T)|\ge g_{123}^2$.  If it is isotropic,
exact cancellation is possible.  Indefinite integral conics can also carry
large primitive points with bounded nonzero norm.  Hence a new theorem must
control actual isotropy or the primitive values $Q(v)$; cone inequalities do
not provide it.

## 8. Capacity decision and surviving statistics

Item 381 closes the following low-degree classes:

1. definite binary and ternary quadratics;
2. binary split forms whose positive factor lines stay $b^{-o(1)}$ away from
   the actual ratio interval;
3. the exact ternary reciprocal-positive coefficient cone (4.3);
4. the normalized Newton boundary and the Newton-certified cone;
5. sub-beta denominators and scalar content as escapes from these bounds.

The first surviving statistics are exactly:



$$
\boxed{
\begin{array}{ll}
\text{binary:}&g_{12}\ \text{and the primitive Pell/norm value }Q(q,r),\\
\text{ternary:}&g_{123},\ \text{rational isotropy, and }Q(v).
\end{array}}
\tag{8.1}
$$



The actual canonical digit bounds place the projective coordinates in a
$b^{o(1)}$ box, and singleton incidence separates the normalized Newton
boundary, but neither presently controls (8.1).  No actual nonzero sub-beta
carrier with $\mathcal U_{1,1}$ divisibility is constructed.  Therefore



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{8.2}
$$



## 9. Strict labels

### PROVED

* The complete binary discriminant classification (3.2)-(3.10).
* The exact ternary reciprocal-positive coefficient cone (4.2)-(4.3).
* The normalized Newton stability identity and singleton separation
  (5.3)-(5.7).
* The definite ternary eigenvalue bound (6.2).
* The exact primitive gcd/norm factorizations (3.8) and (7.6).
* Zero booking.

### PROVED SCOPED NO-GO

* Definite binary and ternary quadratic cancellation carriers.
* Reciprocal-positive and Newton-certified ternary quadratics.
* Rational split lines uniformly separated from the actual ratio interval.
* Primitive/content normalization and sub-beta denominators as escapes.

### EXACT FINITE ONLY

* The replay's predeclared discriminants, Pell pairs, reciprocal coefficient
  tables, Newton identities, positive-load conic point, and scale controls.
* The point $(1,1,2,2)$ is ambient only and is not an actual beta target or
  density datum.

### OPEN

* Actual rational split-line correlations.
* Binary primitive Pell/norm values and $g_{12}$.
* Ternary actual isotropy, primitive conic norms, and $g_{123}$.
* Higher-degree mixed-sign varieties, growing coordinate count, and
  beta-height nonlinear compression.
* The singleton bound, $\Xi_Q$, squarefull excess, beta capacity, Route 1,
  and $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.}
\tag{9.1}
$$



No canonical, master, status, checkpoint, research-log, or audit file is
edited by this work package.

## 10. Deterministic replay

From the archive root:

~~~text
python work/item381_beta_low_degree_symmetric_cancellation_classification_certificate.py ^
  --output work/item381_beta_low_degree_symmetric_cancellation_classification_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer/rational
arithmetic.  All forms, loads, and norm controls are predeclared.  It performs
no actual prime census, target search, factor search, or half-bound scan.
