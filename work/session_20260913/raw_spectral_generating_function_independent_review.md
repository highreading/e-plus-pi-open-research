> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the spectral generating functions

Date: 2026-09-13. Reviewer: audit_computations.

Reviewed `raw_spectral_branch_generating_function.md`, Sections 1–6. **All substantive claims pass.** The bounds concern individual branches; they do not lower-bound an actual mixed determinant.

## 1. Differential equation and normalization

If $f(w)=y(-iw)$, the prolate equation becomes



$$
(1+w^2)f''+2wf'-(\xi-3/4+w^2/4)f=0.
$$



Substitution $f=e^{-w/2}V$ gives exactly



$$
(1+w^2)V''-(w-1)^2V'+(1-w-\xi)V=0.
$$



The Laplace change of variable $x=(u+1)/2$ has the factor $1/\sqrt2$, so
$\int_0^1e^{wx}\psi_l(x)dx=(\mu_l/\sqrt2)e^{w/2}y_l(-iw)$.
For odd parity, dividing by the stated amplitude produces
$i e^{w/2}y_l(-iw)/(\sqrt3 y_l'(0))=V_1/\sqrt3$.
Its derivative at zero is one before division by $\sqrt3$, as required. Thus the $\sqrt3$ in the definition of $r_k^{(1)}$ is essential and correct. The varying row factor $\sqrt{2k+1}$ is also removed correctly.

The original high moments use the unreflected polynomial $U_n$. The stated sign change in its odd spectral component after reflection is correct and does not change the branch functions themselves.

## 2. Extension in the parameter and in the generating variable

Expanding the second-order equation gives the displayed recurrence



$$
(j+2)(j+1)v_{j+2}=(j+1)v_{j+1}
+[\xi-j(j+1)-1]v_j+jv_{j-1}.
$$



The stated parity-dependent degree caps follow by induction. Averaging multiplies $v_j$ by $c_j=2^{-j}\binom{2j}{j}$, which preserves polynomial dependence on $\xi$. For each fixed Taylor coefficient, agreement at the infinitely many distinct nodes of the corresponding parity proves a polynomial identity. The spectrum does not need a finite accumulation point for this argument.

The slit plane is star-shaped about zero, hence simply connected. For $\eta=z/(1-z^2)$, the real-part identity in the note is correct. If $s\eta$ is on the imaginary axis with $s>0$, then $z$ is purely imaginary and $|s\eta|<1$ for $|z|<1$, $s\le2$. Thus the entire integration path avoids both singular slit rays. Compact subsets of the disk produce compact subsets of the slit plane. Analytic ODE dependence, compact integration, and the polynomial coefficient identity justify the full unit disk and entire dependence on $\xi$.

## 3. Abel equation

The ratio $c_{j+1}/c_j=(2j+1)/(j+1)$ yields exactly the four-term recurrence displayed as equation (12) in the reviewed note. Reading the coefficient of $\eta^{j+2}$ in its equation (11) recovers those four terms with the same signs. In particular the $\eta^3$ term acts on $a_{j-1}$ with multiplier $(2j-1)(2j+1)(2j+3)$. This confirms the left-placement of powers of $\eta$ relative to the Euler operator.

The two analytic initial coefficients determine all later coefficients; the multiplicities in the indicial factor $\theta^2(\theta-1)^2$ do not introduce additional analytic degrees of freedom into the claimed solutions.

## 4. Explicit growing-parameter bound

The two quadratic factors $1-z^2\pm isz$ have all roots on the unit circle for $0\le s\le2$. This includes the double-root endpoint. Their product therefore gives the claimed lower bound for $|1+w^2|$, uniformly along every straight segment used by the ODE estimate.

For $h=\sqrt{1+|\xi|}$, the matrix of the scaled state $(V,V'/h)$ is



$$
\begin{pmatrix}0&h\\b/h&a\end{pmatrix}.
$$



Its induced column-sum norm is $\max(|b|/h,h+|a|)$. The note's common upper bound follows from
$|\xi|+W+1\le h^2(W+1)^2$ and $h\ge1$. Both initial states have norm at most $3/2$. Parametrizing the complex segment by arc length and applying Gronwall therefore gives exactly its exponential constant. The square-root prefactor and Cauchy radius factor are correct.

There is no hidden dependence on a growing eigenfunction norm in this proof. It gives $\exp(O(k))$ for $|\xi|=O((k+1)^2)$, but only an upper bound. An actual determinant can still be much smaller than the product of these entry bounds.

## 5. Follow-on exact reduction

`raw_actual_high_cofactor_contour_reduction.md` retains all high rows and both actual endpoint rows in one contour determinant. Its elementary-symmetric insertions encode adjacent high-row cofactors coherently. That reduction is exact; its required relative noncancellation estimate is stated separately and is not supplied by the generating-function upper bound.
