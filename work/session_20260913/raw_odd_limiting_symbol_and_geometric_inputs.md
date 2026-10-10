> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact structure of the fixed odd symbol and geometric base inputs

Date: 2026-09-13. Original bounded continuation by audit_sources.
Independent review requested.

This note continues raw_odd_boundary_operator_limit.md. It proves exact structural identities and sharper base bounds. It does not infer invertibility of the actual limiting Toeplitz operator or nonvanishing of its two boundary determinants.

## 1. The commuting two-dimensional matrix algebra

For real $y$, set


$$
R=\sqrt{1+y^2},\quad z=\frac{1+iy}{R},\quad
t=z^2,\quad
a_0=\frac12\begin{pmatrix}0&1+iy\\1-iy&0\end{pmatrix},
\quad J=\begin{pmatrix}0&t\\1&0\end{pmatrix}.
$$


Then


$$
a_0^2=\frac{R^2}{4}I,\qquad
J=\frac{2a_0}{1-iy},\qquad J^*J=I.
$$


In particular $a_0,J,e^J$ commute at each real $y$. With
$c(t)=\sum_{k\ge0}t^k/(2k)!$ and
$s(t)=\sum_{k\ge0}t^k/(2k+1)!$, the actual symbol is


$$
a(y)=a_0e^J
 =\frac{1+iy}{2}s(t)I+c(t)a_0.                         \tag{1}
$$


Its eigenvalues, labelled by the positive and negative eigenvalues of the Hermitian matrix $a_0$, are


$$
\lambda_\pm(y)=\pm\frac R2e^{\pm z},\qquad
\det a(y)=-\frac{1+y^2}{4}.                            \tag{2}
$$


All these identities hold before restricting $y$ to the limiting interval
$[-\sqrt3,\sqrt3]$. On that interval $\Re z\ge1/2$. Thus the symbol is pointwise invertible and its determinant has winding zero on the Fourier circle. Neither fact alone controls matrix partial indices or the kernel of its half-line compression.

The form (1) is a scalar plus scalar times a matrix whose square is scalar. This is the exact algebraic structure relevant to a Daniele--Khrapkov factorization; a factorization theorem still needs its analytic hypotheses and its partial-index conclusion checked separately.

## 2. A sharper accretivity bound for the exponential base

For every complex number $\omega$ on the unit circle,


$$
\Re e^\omega\ge e^{-1}.                               \tag{3}
$$


To prove it, write $u=|\Im\omega|\le1$. The smaller possible real part is
$e^{-\sqrt{1-u^2}}\cos u$. Its logarithm has derivative


$$
\frac{u}{\sqrt{1-u^2}}-\tan u\ge0,
$$


because $\arcsin u\ge u$ and tangent is increasing on $[0,\pi/2)$.
The value at zero is $-1$, proving (3); the endpoint follows by continuity.

Since $J$ is unitary, the spectral theorem gives


$$
\Re e^{J(y)}\ge e^{-1}I,\qquad \|e^{J(y)}\|\le e.        \tag{4}
$$


Therefore the finite compressions and the limiting compression $E_+$ have inverse norm at most $e$. In particular


$$
\|Q_+\|=\|E_+^{-1}A_{0,+}^{-1}\|\le2e.                 \tag{5}
$$


This only sharpens the bound for the already proved invertible base factors.

## 3. All three base inputs are explicit geometric vectors

Let $Y_+$ be the half-line Jacobi matrix with off-diagonal entries
$\sqrt3/2$, and let $e_0$ be its first coordinate. Direct substitution in the recurrence, including the boundary row, proves


$$
(I\pm iY_+)^{-1}e_0
 =\frac23(\mp i/\sqrt3)^r,\quad r\ge0.                 \tag{6}
$$


The inverse of $A_{0,+}$ is


$$
A_{0,+}^{-1}
 =2\begin{pmatrix}
 0&(I-iY_+)^{-1}\\ (I+iY_+)^{-1}&0
 \end{pmatrix}.
$$


Since $U_+=(\sqrt3/4)e^*$, its two transformed columns are


$$
b_1(r)=\begin{pmatrix}0\\3^{-1/2}(-i/\sqrt3)^r\end{pmatrix},
\quad
b_2(r)=\begin{pmatrix}3^{-1/2}(i/\sqrt3)^r\\0\end{pmatrix}. \tag{7}
$$


They are orthogonal, each with norm $1/\sqrt2$, and
$b_2=v_\infty/\sqrt2$.

The third input is


$$
b_v=A_{0,+}^{-1}v_\infty
 =\begin{pmatrix}
 0\\ \sqrt{2/3}\big[(i/\sqrt3)^r+(-i/\sqrt3)^r\big]
 \end{pmatrix},\qquad \|b_v\|=\sqrt3.                   \tag{8}
$$


Indeed $v_\infty=\sqrt{3/2}(I-iY_+)^{-1}e_0$ in its first component and


$$
(I+Y_+^2)^{-1}
=\tfrac12[(I+iY_+)^{-1}+(I-iY_+)^{-1}].
$$


The determinant entries can consequently be computed from just
$E_+^{-1}b_1,E_+^{-1}b_2,E_+^{-1}b_v$, with these exact geometric right-hand sides. No approximation of $A_{0,+}^{-1}$ is needed. Their tails and squared norms are explicit geometric sums.

## 4. Why the elementary scalar factorization does not prove accretivity

Put $y=(\sqrt3/2)(\zeta+\zeta^{-1})$, $|\zeta|=1$, and


$$
l_\pm(\zeta)=1\pm i\zeta/\sqrt3.
$$


Then


$$
1\pm iy=\frac32l_\pm(\zeta)l_\pm(\zeta^{-1}).
$$


These factors have no zeros on the closed disk. A canonical scalar factorization of each off-diagonal entry of $a_0$ is therefore explicit.

Let $D_+(\zeta)=\operatorname{diag}(l_-(\zeta),l_+(\zeta))$ and choose the corresponding exterior factor so that $a_0=D_-D_+$. The exact Toeplitz product rule for an exterior factor on the left and an interior factor on the right reduces the invertibility question for $T(a)$ to that for


$$
T(G),\qquad G=D_+e^J D_+^{-1}.
$$


However $G$ is not pointwise accretive at the actual deformation value one. At $\zeta=i$, where $y=0$, the transformed generator is


$$
D_+JD_+^{-1}
 =\begin{pmatrix}0&2+\sqrt3\\2-\sqrt3&0\end{pmatrix}.
$$


Its square is $I$, so the Hermitian part of its exponential has eigenvalues


$$
\cosh1\pm2\sinh1.
$$


The smaller is negative because $\tanh1>1/2$. This is an exact obstruction to this particular factorization-plus-accretivity shortcut. It is not an obstruction to an alternative factorization, and it does not imply a zero determinant.

The remaining target is still nonvanishing of the two fixed boundary determinants, through a valid factorization or a certified fixed-operator calculation.

