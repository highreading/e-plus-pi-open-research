> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The central Bessel obstruction: adjoint and Hilbert-determinant no-go

Checked: 2026-08-27 UTC.

## 1. Scope

Let $p=2m+1$ be an odd prime. In $\mathbb F_p$, put



$$
B_0=0,\qquad B_1=1,\qquad
B_{r+1}=\frac{2r-1}{2r+1}(2B_r-B_{r-1})\quad(1\le r<m),
\tag{1}
$$



and



$$
D_m=B_{m-1}-2B_m,\qquad
\beta_m=\sum_{r=1}^m\frac{B_r}{r}.
\tag{2}
$$



Every denominator in (1)--(2) is a unit modulo $p$. The previously
proved central Laguerre reduction says that the forbidden simultaneous root
is exactly



$$
D_m=\beta_m=0.
\tag{3}
$$



This note gives an exact coefficient-adjoint formulation and evaluates the
ambient corrected Hilbert determinant. The ambient form is nondegenerate
for every $p\ge5$. However, the determinant of its restriction to the
one-dimensional resonant ODE-solution space is, up to an explicit unit,
exactly $\beta_m$. Thus the Cauchy determinant does not prove (3)
impossible: after its known factor is removed, the remaining determinant is
the original obstruction.

## 2. Coefficient matrix and the transpose adjoint

Set



$$
K(z)=\sum_{j=0}^{m-1}k_jz^j,\qquad k_j=B_{j+1},
\tag{4}
$$



and consider



$$
\mathcal L K
=2z(1-z)^2K'(z)+(1-2z+3z^2)K(z).
\tag{5}
$$



Let $T=T_m$ be the $m\times m$ lower triangular matrix, with rows and
columns numbered $0,\ldots,m-1$, whose only nonzero entries are



$$
T_{r,r}=2r+1,\qquad
T_{r,r-1}=2-4r,\qquad
T_{r,r-2}=2r-1,
\tag{6}
$$



when the indicated column exists. These are the coefficients of
$[z^r]\mathcal LK$. If $e_0=(1,0,\ldots,0)^t$, direct coefficient
comparison with (1) gives



$$
Tk=e_0,\qquad
\det T=\prod_{r=0}^{m-1}(2r+1).
\tag{7}
$$



The coefficient of $z^m$ is the row



$$
\rho^tk=(2m-1)k_{m-2}+(2-4m)k_{m-1}
         =(2m-1)D_m,
\tag{8}
$$



with the first term omitted for $m=1$. The coefficient of $z^{m+1}$
is $(2m+1)k_{m-1}=0$. Finally, for



$$
c_j=\frac1{j+1}\quad(0\le j<m),
\tag{9}
$$



one has $c^tk=\beta_m$. The Schur-complement formula therefore gives the
two exact bordered determinants



$$
\boxed{
\det\begin{pmatrix}T&e_0\\ \rho^t&0\end{pmatrix}
=-(\det T)(2m-1)D_m,}
\tag{10}
$$





$$
\boxed{
\det\begin{pmatrix}T&e_0\\ c^t&0\end{pmatrix}
=-(\det T)\beta_m.}
\tag{11}
$$



All displayed factors outside $D_m,\beta_m$ are units in
$\mathbb F_p$.

The literal transpose adjoint adds no relation. If $T^ty=c$, then



$$
\beta_m=c^tT^{-1}e_0=y^te_0=y_0,
\tag{12}
$$



and its backward recurrence is



$$
(2j+1)y_j-2(2j+1)y_{j+1}+(2j+3)y_{j+2}
=\frac1{j+1},
\qquad y_m=y_{m+1}=0.
\tag{13}
$$



Thus the adjoint computes the same scalar $\beta_m$; it does not constrain
it independently.

## 3. The corrected Hilbert form and its determinant

Let



$$
C_{ij}=\frac1{i+j+2}\quad(0\le i,j<m),
\qquad
R=2C-e_{m-1}e_{m-1}^t.
\tag{14}
$$



The denominators in $C$ range from $2$ to $2m=p-1$, so they are all
units. The Cauchy determinant evaluation is



$$
\det C=
\frac{\displaystyle\prod_{0\le i<j<m}(j-i)^2}
     {\displaystyle\prod_{i,j=0}^{m-1}(i+j+2)},
\tag{15}
$$



which is nonzero modulo $p$. The bottom diagonal entry of the inverse is



$$
(C^{-1})_{m-1,m-1}
=2m\binom{2m-1}{m-1}^{\!2}.
\tag{16}
$$



For clarity, (16) follows directly from the diagonal Cauchy-inverse formula:
its numerator is
$\bigl(\prod_{r=1}^m(m+r)\bigr)^2$, while its denominator is
$2m((m-1)!)^2$. The matrix determinant lemma now gives the exact rational
identity



$$
\boxed{
\det R=2^m(\det C)
\left(1-m\binom{2m-1}{m-1}^{\!2}\right).}
\tag{17}
$$



Modulo $p=2m+1$,



$$
\binom{2m-1}{m-1}=\binom{p-2}{m-1}
\equiv(-1)^{m-1}m,
\tag{18}
$$



so the last factor in (17) is



$$
1-m^3=1-(-1/2)^3=\frac98\pmod p.
\tag{19}
$$



Consequently



$$
\boxed{\det R\ne0\pmod p\quad\text{for every }p\ge5.}
\tag{20}
$$



For $p=3,m=1$, the factor $9/8$ and $\det R$ both vanish; directly,
$D_1=-2\ne0\pmod3$, so this exceptional degeneracy is not a central root.

## 4. The Frobenius anomaly and the restricted determinant

The full residual of (5) is



$$
\mathcal LK=1+(2m-1)D_mz^m.
\tag{21}
$$



Termwise integration in $\mathbb F_p[z]$ must retain the degree-$p$
anomaly. Namely, for



$$
H(z)=2z(1-z)^2K(z)^2,
$$



one has



$$
\int_0^1H'=H(1)-H(0)-[z^p]H=-2B_m^2.
\tag{22}
$$



Multiplying (21) by $K$, integrating by parts with (22), and putting



$$
J_m=\int_0^1z^mK(z)\,dz
$$



gives the exact congruence



$$
\boxed{
k^tRk
=2\int_0^1zK(z)^2\,dz-B_m^2
=\beta_m+(2m-1)D_mJ_m.}
\tag{23}
$$



All integrals remaining in (23) have denominators at most $p-1$.
In particular, only under the resonance condition $D_m=0$ does (23)
specialize to



$$
\boxed{k^tRk=\beta_m.}
\tag{24}
$$



This conditional is essential.

Let $A$ be the $(m-1)\times m$ matrix formed by rows
$1,\ldots,m-1$ of $T$, and put



$$
\gamma=\prod_{r=1}^{m-1}(2r+1).
\tag{25}
$$



The submatrix of $A$ in columns $1,\ldots,m-1$ is lower triangular
with determinant $\gamma$. Hence $A$ has full row rank, its kernel is
the line spanned by $k$, and its signed maximal-minor vector is exactly
$\gamma k$. The standard one-dimensional bordered-Gram identity gives



$$
\boxed{
\det\begin{pmatrix}R&A^t\\ A&0\end{pmatrix}
=(-1)^{m-1}\gamma^2 k^tRk.}
\tag{26}
$$



One quick proof of (26) is to reduce $A$ by invertible row and column
operations to $(I_{m-1}\ 0)$; the block determinant then retains only the
quadratic form on the one-dimensional kernel. Tracking the signed
maximal-minor vector gives the factor $\gamma^2$ and the displayed sign.

Combining (24) and (26), conditional on the central root $D_m=0$, yields



$$
\boxed{
\det\begin{pmatrix}R&A^t\\ A&0\end{pmatrix}
=(-1)^{m-1}\gamma^2\beta_m.}
\tag{27}
$$



Thus the desired nonvanishing is indeed a determinant nonvanishing
problem, but the determinant in (27) is not the ambient Cauchy determinant.
Since $R$ is invertible for $p\ge5$, its Schur complement rewrites (27)
as



$$
\det\begin{pmatrix}R&A^t\\ A&0\end{pmatrix}
=(-1)^{m-1}(\det R)\det(AR^{-1}A^t).
\tag{28}
$$



The factor $\det R$ is the known nonzero quantity (17). The remaining
compressed determinant vanishes if and only if $\beta_m$ does. Evaluating
the Cauchy factor therefore removes only a unit and leaves exactly the
original forbidden condition.

## 5. Why ambient nondegeneracy is insufficient

Nondegeneracy is not anisotropy. In fact, for $m\ge3$, every
nondegenerate quadratic form in $m$ variables over an odd finite field is
isotropic. An elementary proof diagonalizes the form and considers its
first three nonzero coefficients $a,b,c$: the two sets



$$
\{ax^2:x\in\mathbb F_p\},\qquad
\{-c-by^2:y\in\mathbb F_p\}
$$



both have $(p+1)/2$ elements, so they intersect and give a nonzero vector
$(x,y,1)$ on which the form vanishes.

Even in dimension two, the particular pre-resonant recurrence line can be
isotropic while $R$ is nondegenerate. At $p=5,m=2$,



$$
k=(1,2/3)^t,\qquad k^tRk=5/3=0\pmod5,
\qquad D_2=-1/3\ne0\pmod5.
\tag{29}
$$



This is not a compatible central counterexample, because the final
resonance row fails. It is an explicit warning that $\det R\ne0$ cannot
control the norm of the recurrence-selected line. When the final row does
hold, (27) says that controlling that norm is precisely the still-open
condition $\beta_m\ne0$.

## 6. Verdict

The adjoint, the two elementary bordered resultants, and the corrected
Hilbert form all lead to exact determinant formulas. The Cauchy formula
proves the strongest available ambient statement: $R$ is nondegenerate
for every central prime $p\ge5$. It does not prove nonvanishing on the
unique resonant ODE-solution line. The Gram determinant of that line is
$\beta_m$ itself, up to the explicit unit square in (27). Continuing to
take adjoints or Schur complements therefore loops back to (3), rather than
creating an independent constraint.

