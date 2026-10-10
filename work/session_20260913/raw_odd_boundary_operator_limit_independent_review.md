> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the odd boundary operator limit

Date: 2026-09-13. Reviewer: audit_sources.
Status: PASS. No mathematical correction required.

Reviewed in full: raw_odd_boundary_operator_limit.md, with its dependencies raw_odd_exact_two_mode_boundary_matrices.md and raw_odd_explicit_circle_boundary_kernels.md. The conclusion is convergence to fixed boundary matrices, conditional use of their nonzero determinants, and no quantitative convergence rate.

## 1. Cayley normalization and finite moments

The map $u(t)\mapsto(1-iy)^m u((1+iy)/(1-iy))$ changes the scalar circle norm into a positive constant times $(1+y^2)^{-2m-2}dy$. Its squared polynomial moments exist through degree $2m+1$. The stated recurrence is used only through $j=2m$; consequently its next polynomial still has a finite norm. At every fixed distance from $m$ its off-diagonal coefficient tends to $\sqrt3/2$.

The rational matrix becomes exactly


$$
a_0(y)=\frac12\begin{pmatrix}0&1+iy\\1-iy&0\end{pmatrix}.
$$


Multiplication loses a single degree, so its exterior map is


$$
(I-P_m)a_0P_m=\frac{a_{m+1,m}}2\iota_{m+1}J_b e_m,
\qquad J_b=\begin{pmatrix}0&i\\-i&0\end{pmatrix}.
$$


The adjoint has the same $J_b$; there is no missing minus sign. Thus $U_m,V_m$ and the order $Q_m=E_m^{-1}A_{0,m}^{-1}$ in the source are correct.

## 2. The actual endpoint and its phase

The original endpoint $t=0$ is $y=i$, and the transformed polynomial is multiplied there by $2^m$. This common scalar disappears on normalizing the Riesz vector.

The monic Rodrigues evaluation and its consecutive ratio give


$$
Q_j(i)=(2i)^j\frac{(\beta-j)_j}{(2\beta-2j)_j},\qquad
\frac{q_j(i)}{q_{j-1}(i)}
=i\sqrt{\frac{(2\beta-j)(2\beta-2j-1)}
 {j(2\beta-2j+1)}}.
$$


Both factors in the squared ratio decrease with $j$, and their value at $j=m$ exceeds three. This supplies the uniform geometric majorant, not merely pointwise convergence.

The Riesz coefficients are conjugated values $q_j(i)$. After reversing indices, multiplication of the whole vector by $i^m$ therefore produces $i^r$, not $(-i)^r$, at index $r$. Normalization gives


$$
v_\infty(r)=\sqrt{2/3}(i/\sqrt3)^r(1,0)^{\mathsf T}.
$$


The phase convention must be used for the finite $D_{3,m}$ when asserting entrywise convergence. Its change conjugates that bordered matrix by diagonal unitary factors and leaves its determinant and $s_m$ unchanged. The source explicitly makes this phase choice.

## 3. Functional calculus and the order of limits

The proof does not assume an infinite orthonormal-polynomial basis for the varying Cauchy measure. This is essential, since that measure has only finitely many moments.

For a fixed local input and a fixed polynomial, finite recurrence paths prove convergence of all required coefficients and squared norms. For a bounded continuous function, first choose a polynomial approximation on a fixed interval $[-R,R]$, $R>\sqrt3$. Its exterior squared error is bounded by a fixed polynomial. Bound that tail by higher fixed moments, take $m\to\infty$, and only then send their order to infinity. Compact support of the limiting spectral measure makes the tail bound vanish. All moment orders are fixed before taking $m\to\infty$, so every required moment eventually exists.

This proves norm convergence of each fixed projected column. The same argument applies to the adjoint symbol and to the exterior input at reversed index $-1$. The latter gives norm convergence of the two adjoint columns of $W_m$, hence operator-norm convergence of this map into $\mathbb C^2$. It is stronger than mere entrywise convergence and is justified as stated.

The finite extensions by identities, and by $I/2$ for $A_{0,m}$, preserve the required uniform inverse bounds and disappear in the strong limit. Accretivity proves invertibility of $E_+$: it applies to both the operator and its adjoint, giving closed range and zero orthogonal complement. Selfadjointness of $Y_+$ proves invertibility of $I\pm iY_+$, hence $A_{0,+}$. The inverse identity then gives strong inverse convergence. No unproved invertibility of the actual perturbed limiting operator is used here.

## 4. Boundary determinants and scope

The finite-rank maps $U_m$, the endpoint vectors, and $W_m$ converge in norm in the required fixed coordinates; $Q_m$ converges strongly with a uniform norm bound. These facts suffice for every entry of $D_{2,m},D_{3,m}$ to converge to the displayed matrices. Their entries use the correct factor order.

If both limiting determinants are nonzero, the exact finite determinant quotient gives a nonzero limit of $s_m$, hence $\log|s_m|=o(m)$. Neither the finite all-index nonvanishing results nor convergence alone establishes these two limiting nonvanishing statements.

No repair, new sample, or additional hypothesis is needed for the source theorem. The fixed determinant condition is the precise remaining analytic question.

