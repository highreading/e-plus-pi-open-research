> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A uniform local boundary resolvent limit and the scalar two-step growth factor

Date: 2026-09-13. Original bounded continuation by audit_computations,
following root's constant-Jacobi limit proposal.

This proves the limit directly for the actual row matrix, uniformly
on positive compact parameter intervals, with an (O(1/N)) error.
No theorem about global matrix convergence, no unproved root property,
and no numerical limit is used. The exact local geometric resolvent
supplies the required localization.

## 1. The limiting half-line matrix

Let (L\) on (\ell^2(\mathbb N_0)\) have diagonal (-1/2\)
and off-diagonal (1/4\). It is bounded self-adjoint with spectrum
in ([-1,0]\). For (c>0\), put



$$
q(c)=(\sqrt{c+1}-\sqrt c)^2\in(0,1),\qquad
m(c)=4q(c)=8\bigl(c+1/2-\sqrt{c(c+1)}\bigr).
\tag{1}
$$



The exact boundary resolvent vector is



$$
w(c)=(cI-L)^{-1}e_0,qquad w_j(c)=m(c)q(c)^j.
\tag{2}
$$



Indeed (q+q^{-1}=4c+2) verifies the interior recurrence and
((c+1/2)m-(1/4)mq=1) verifies the boundary row. The sequence
is square summable, and the positive resolvent is unique. In
particular



$$
\langle e_0,(cI-L)^{-1}e_0\rangle=m(c),\qquad
\|(cI-L)^{-1}e_0\|^2=-m'(c)=\frac{m(c)^2}{1-q(c)^2}.
\tag{3}
$$



The derivative identity also follows by differentiating the resolvent;
it agrees with the explicit expression in (1).

## 2. Reversing and extending the finite parity blocks

Recall (K_N=K_{0,N}-J_N), where (K_{0,N}\) is the actual
principal compression of (J^2-\Lambda\). Its parity blocks are
tridiagonal. For each of the two boundary indices (N-2,N-1\),
reverse the corresponding parity block from that index toward zero,
divide by (N^2\), and extend it to (\ell^2(\mathbb N_0)\) by
a zero tail. Call the resulting bounded self-adjoint matrix (A_N\).
The boundary vector is now (e_0\). This construction is performed
separately for each parity; their dimensions may differ by one.

At depth (j\) inside the finite block, the original index is
(l=N-\beta-2j\), with (\beta=1\) or (2\). The diagonal
entry is (d_l/N^2\), where



$$
d_l=-l(l+1)/2+1/4+\delta_l+\delta_{l+1},
\quad 0\le\delta_l\le1/12.
$$



The next off-diagonal entry, when present, is
(a_{l-1}a_l/N^2\), with
(a_{l-1}a_l=l(l-1)/4+\varepsilon_{l-2}\) and
(0\le\varepsilon_{l-2}\le1/6\). These formulas give the
following convenient bounds for all depths, including the zero tail,
when (N\ge8\):



$$
\boxed{|(A_N-L)_{j,j}|\le\frac{4(j+1)}N,
\qquad |(A_N-L)_{j,j+1}|\le\frac{2(j+1)}N.}
\tag{4}
$$



For interior entries, use (N-l=\beta+2j\) in the displayed
quadratic coefficients. For omitted boundary couplings and the tail,
the absolute differences are at most (1/2\), while their depth
is at least (N/2-O(1)\), so the same bounds apply. This includes
the differing odd/even truncation lengths.

The estimates (4) do **not** say that (A_N\to L\) in operator
norm: the differences far from the boundary remain of order one.
They are useful after application to the localized vector (2).

## 3. Quantitative localized resolvent comparison

Fix (0<c_0\le c\le c_1<\infty\), and assume
(N\ge\max\{8,4/c_0\}\). The reviewed inequality
(K_{0,N}\preceq(9/8)I\), also valid after extension by zero,
implies



$$
\|(cI-A_N)^{-1}\|\le2/c_0.
\tag{5}
$$



From (4), separating the three diagonals and shifting their indices,



$$
\|(A_N-L)w(c)\|
\le\frac8N\|((j+1)w_j(c))_{j\ge0}\|.
\tag{6}
$$



The two shifted norms are bounded by the same weighted norm: for
the lower diagonal the coefficient (j\) multiplies (w_{j-1}\),
and for the upper diagonal ((j+1)\) multiplies (w_{j+1}\).
Thus no estimate of an unweighted far tail has been substituted.

Put (q_0=q(c_0)\), (m_0=m(c_0)\), and



$$
F_0=m_0\sqrt{\frac{1+q_0^2}{(1-q_0^2)^3}}.
$$



Since (m,q\) decrease with (c\), the weighted norm in (6) is
at most (F_0\). The resolvent identity therefore gives the
**vector** estimate



$$
\boxed{\|(cI-A_N)^{-1}e_0-(cI-L)^{-1}e_0\|
\le\frac{16F_0}{c_0N}.}
\tag{7}
$$



It follows both that the boundary scalar resolvent differs from
(m(c)\) by at most this amount and that



$$
\left|\langle e_0,(cI-A_N)^{-2}e_0\rangle+m'(c)\right|
\le\frac{48F_0}{c_0^2N}.
\tag{8}
$$



For (8), compare the squared norms of the vectors in (7), whose
norms are at most (2/c_0\) and (1/c_0\). No differentiation
of an unspecified (O(1/N)\) remainder is used.

## 4. Restoring the opposite-parity coupling

Let



$$
\mathcal R_N(c)=(cI-K_N/N^2)^{-1},\qquad
\mathcal R_{0,N}(c)=(cI-K_{0,N}/N^2)^{-1}.
$$



The actual perturbation has norm
(\|J_N/N^2\|\le1/N\). Both resolvents have norm at most
(2/c_0\), using the reviewed upper bounds and the chosen lower
bound on (N\). Hence



$$
\|\mathcal R_N-\mathcal R_{0,N}\|\le\frac4{c_0^2N},
\quad
\|\mathcal R_N^2-\mathcal R_{0,N}^2\|
\le\frac{16}{c_0^3N}.
\tag{9}
$$



The boundary compression of (\mathcal R_{0,N}\) is diagonal,
and its two entries are the parity boundary values treated in
(7). Its squared compression has the two values in (8).
Therefore



$$
\boxed{\begin{aligned}
\|\iota_N^T\mathcal R_N(c)\iota_N-m(c)I_2\|
&\le D_1/N,\\
\|\iota_N^T\mathcal R_N(c)^2\iota_N+m'(c)I_2\|
&\le D_2/N,
\end{aligned}}
\tag{10}
$$



with the explicit constants



$$
D_1=4/c_0^2+16F_0/c_0,\qquad
D_2=16/c_0^3+48F_0/c_0^2.
$$



This proves the two-channel local limit for both parities and all
large (N\), including their noncommuting coupling.

## 5. The boundary matrix and exact transfer limits

The explicit boundary coupling satisfies



$$
\left\|\frac{\Gamma_N}{N^2}-\frac14I\right\|\le\frac1N,
\qquad \|\Gamma_N/N^2\|\le1/2\quad(N\ge8).
\tag{11}
$$



For its two diagonal entries use
(a_{N-1}a_N=N(N-1)/4+O(1)\),
(a_Na_{N+1}=N(N+1)/4+O(1)\), with errors at most (1/6\);
its off-diagonal entry is (-a_N/N^2\). The bound in (11)
then follows directly from (a_N\le N/2+1/(12N)\).

Recall the exact identities, with (x=cN^2\),



$$
\frac{M_N(x)}{N^2}
=\left(\frac{\Gamma_N}{N^2}\right)^T
\iota_N^T\mathcal R_N(c)\iota_N
\left(\frac{\Gamma_N}{N^2}\right),
$$





$$
-M_N'(x)
=\left(\frac{\Gamma_N}{N^2}\right)^T
\iota_N^T\mathcal R_N(c)^2\iota_N
\left(\frac{\Gamma_N}{N^2}\right).
$$



Combining (10)–(11) proves



$$
\boxed{\frac{M_N(cN^2)}{N^2}=\frac{m(c)}{16}I+O(N^{-1}),
\qquad -M_N'(cN^2)=\frac{-m'(c)}{16}I+O(N^{-1}),}
\tag{12}
$$



uniformly for (c\in[c_0,c_1]\). The first error is at most
(E_1/N\), the second at most (E_2/N\), where one may take



$$
E_1=D_1/4+3/(4c_0),\qquad E_2=D_2/4+3/(4c_0^2).
$$



The derivative is with respect to (x\), as required; the powers
of (N\) have been retained in the two exact preceding formulas.

Finally the exact branch transfer is (T_N=M_N^{-1}\Gamma_N^T\).
The positive lower bound (M_N/N^2\succeq I/[64(c_1+1)]\)
from the CD theorem permits inversion uniformly. Thus



$$
\boxed{T_N(cN^2)=\lambda(c)I+O(N^{-1}),\qquad
\lambda(c)=\frac4{m(c)}
=(\sqrt c+\sqrt{c+1})^2.}
\tag{13}
$$



An explicit error constant is
(64(c_1+1)[1+\lambda(c_1)E_1]\). Indeed subtract
(\lambda(c)I\), multiply by (M_N/N^2\), and use
(\lambda(c)m(c)/16=1/4\). This proves the proposed scalar
factor with its actual matrix correction.

## 6. Common-parameter transport across a macroscopic cut interval

Fix (x=\chi n^2\), with (\chi\) in a positive compact interval,
and take same-parity cuts from (n\) to (m\le2n\). Equation
(13) applies uniformly with (c=x/N^2\) at every cut. Define



$$
S_{m,n}^{\mathrm{loc}}(x)=
\prod_{N=n+2,n+4,\ldots,m}\lambda(x/N^2).
$$



The product argument in `raw_two_step_channel_transport.md` then
gives



$$
\boxed{P_m(x)=S_{m,n}^{\mathrm{loc}}(x)
\mathcal V_{m,n}(x)P_n(x),\qquad
\|\mathcal V_{m,n}\|+\|\mathcal V_{m,n}^{-1}\|=O(1).}
\tag{14}
$$



The matrices (\mathcal V\) are the actual ordered products;
their distance from the identity need not tend to zero on a full
dyadic interval. The bound is uniform in the specified compact
parameter range. It applies to every vector acted on by the branch
pair, not only to a preferred column.

For (t=m/n\), a Riemann sum gives the explicit exponential scale



$$
\log S_{m,n}^{\mathrm{loc}}(\chi n^2)
=n\int_1^t\operatorname{arsinh}(\sqrt\chi/s)\,ds+O(1).
\tag{15}
$$



The factor (1/2\) from the step size cancels the factor two in
(\log\lambda(c)=2\operatorname{arsinh}\sqrt c\).
The integrand and its derivative are uniformly bounded on the
compact range, so the error is (O(1)\), not merely (o(n)\).
An antiderivative is



$$
s\operatorname{arsinh}(\sqrt\chi/s)
+\sqrt\chi\operatorname{arsinh}(s/\sqrt\chi).
$$



Consequently the norm of (P_m(x)v\) relative to (P_n(x)v\),
for every nonzero vector (v\), has this common exponential
transport factor within constant multiplicative bounds.

## 7. What remains outside this theorem

This proves a local resolvent limit and a common-parameter growth
factor for adjacent branch pairs. It is stronger than a qualitative
ratio limit or global entry upper bound. It does not identify the
limiting ordered matrix correction, make (P_n\) diagonal, control
the componentwise node-polynomial remainders at many parameters,
or lower-bound the actual high-row cofactors. Those operations
still require a comparison that survives the prescribed row
deletion and parameter variation. No irrationality or primitive
height conclusion is drawn from (12)–(15).
