> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Polynomial conditioning of the actual adjacent two-branch matrix

Date: 2026-09-13. Original bounded continuation by audit_computations,
following root's proposed global normalization.

This proves a polynomial, rather than exponential, condition-number
bound for the actual adjacent (2\)-by-(2) branch matrix at
(x=cN^2), uniformly on every positive compact interval of (c).
The proof does not assume a limit for the branches or their roots.
It uses the exact transfer and estimates that stay uniform when
(x/j^2) is unbounded at the early cuts.

## 1. Exact objects and uniform resolvent bounds at all preceding cuts

For cut (j\ge2), write



$$
P_j(x)=\begin{pmatrix}p_j^{(0)}(x)&p_j^{(1)}(x)\\
p_{j+1}^{(0)}(x)&p_{j+1}^{(1)}(x)\end{pmatrix},\qquad
T_j(x)=M_j(x)^{-1}\Gamma_j^T.
$$



The exact recurrence is (P_j=T_jP_{j-2}). Let (K_j) denote
the actual principal row compression, and
(K_{0,j}) the compression of (J^2-\Lambda). The reviewed bounds
are



$$
(-j^2+3/8)I\preceq K_j\preceq(j+3/4)I,\quad
K_{0,j}\preceq(9/8)I,\quad \|J_j\|\le j.
\tag{1}
$$



Fix a final index (N) and (x\ge c_0N^2), with (c_0>0).
For (N\) sufficiently large, uniformly over (8\le j\le N),



$$
R_j=(xI-K_j)^{-1},\quad R_{0,j}=(xI-K_{0,j})^{-1},\quad
\|R_j\|,\|R_{0,j}\|\le2/x,
\tag{2}
$$



and



$$
\|R_j-R_{0,j}\|\le4j/x^2.
\tag{3}
$$



For example, (N\ge\max\{8,4/c_0\}) ensures
(x\ge4N\ge2(j+3/4)), and the bounds follow from (1) and
the resolvent identity. No upper bound on (x/j^2) has been used.

The aligned parity-block comparison from
`raw_two_step_channel_transport.md` has matrix difference at most
(2j), for either parity of (j). With (2), it yields



$$
|(R_j)_{j-2,j-2}-(R_j)_{j-1,j-1}|\le16j/x^2.
\tag{4}
$$



The parity-conjugate resolvent identity also gives



$$
|(R_j)_{j-2,j-1}|\le4j/x^2.
\tag{5}
$$



These are the same estimates as before with their true (x)-scale
retained, instead of replacing (x) by constants times (j^2).

## 2. A normalized transfer error uniform in the large parameter

Write (\Gamma_j=\bigl(\begin{smallmatrix}d_1&0\\\ell&d_2\end{smallmatrix}\bigr)),
(m_j=\operatorname{tr}M_j/2),
(\gamma_j=(d_1+d_2)/2), and (\tau_j=\gamma_j/m_j>0).
The elementary bounds, for (j\ge8), are



$$
\sigma_{\min}(\Gamma_j)\ge j^2/8,\quad
\|\Gamma_j\|\le j^2/2,\quad
\|\Gamma_j^T-\gamma_jI\|\le7j/4,
\tag{6}
$$



with (0<d_2-d_1\le3j/2), ( |\ell|\le j).
Since (R_j\succeq I/(x+j^2)),



$$
M_j\succeq\frac{j^4}{64(x+j^2)}I,\quad
m_j\le\frac{j^4}{2x},\quad
\gamma_j\ge j^2/8,
\quad m_j/\gamma_j\le4j^2/x.
\tag{7}
$$



Expanding the transformed off-diagonal entry using (2),(5) gives



$$
|(M_j)_{12}|\le j^5/x^2+j^3/x.
$$



The diagonal difference has the four bounds



$$
4j^5/x^2+3j^3/x+4j^4/x^2+2j^2/x.
$$



They come respectively from (4), the difference (d_1^2-d_2^2),
the cross term, and the $\ell^2$ term. Taking half that diagonal
difference plus the off-diagonal absolute value gives the safe estimate



$$
\|M_j-m_jI\|\le5j^5/x^2+4j^3/x.
\tag{8}
$$



Now use the exact normalization identity



$$
\frac{T_j}{\tau_j}-I
=M_j^{-1}\left[
\frac{m_j}{\gamma_j}(\Gamma_j^T-\gamma_jI)
-(M_j-m_jI)\right].
$$



Equations (6)–(8) prove



$$
\boxed{T_j=\tau_j(I+E_j),\qquad
\|E_j\|\le64(1+j^2/x)(11/j+5j/x).}
\tag{9}
$$



This is the required uniform bound at all preceding cuts. In
particular, with



$$
K=704(1+1/c_0),
$$



one has



$$
\boxed{\|E_j\|\le K(1/j+j/x)\quad(8\le j\le N).}
\tag{10}
$$



The constant depends on the final lower ratio (c_0), not on
(x/j^2), which can tend to infinity as (j) stays fixed.

## 3. Accumulating from a fixed initial cut

Choose a fixed even integer (J_0\ge\max\{8,4K\}), and use
(J=J_0) if (N) is even and (J=J_0+1) if (N) is odd.
For all sufficiently large (N\), ensure also
(N\ge4K/c_0). Then every cut (j=J+2,J+4,\ldots,N) has
(\|E_j\|\le1/2). Factor the exact product as



$$
P_N(x)=\left(\prod_{j=J+2,J+4,\ldots,N}\tau_j(x)\right)
\mathcal U_{N,J}(x)P_J(x).
\tag{11}
$$



The scalar product is positive and has no effect on condition numbers.
The actual ordered product (\mathcal U\) satisfies



$$
\begin{aligned}
\log\operatorname{cond}\mathcal U
&\le3\sum_j\|E_j\|\\
&\le\frac{3K}{2}\log(N/J)+\frac{3K}{2c_0}.
\end{aligned}
\tag{12}
$$



Indeed (\log(1+t)-\log(1-t)\le3t) for (0\le t\le1/2),
and the step-two sums obey



$$
\sum_j1/j\le\tfrac12\log(N/J),\qquad
\sum_jj/x\le N^2/(2x)\le1/(2c_0).
$$



Thus the cumulative error is (O(\log N)), yielding a polynomial
bound, rather than being incorrectly discarded as (o(1)).

## 4. The fixed starting matrix costs at most one power of (x)

The exact Casoratian identity gives



$$
\det P_J(x)=
\frac{\det(K_J-xI)}{\prod_{h=0}^{J-1}a_{h+1}a_{h+2}}.
\tag{13}
$$



For fixed (J) and (x\ge2(J+3/4)), the absolute numerator
is at least ((x/2)^J). Each entry of (P_J) has degree at most
(\lceil J/2\rceil), and its coefficients are fixed. Hence
there is a finite constant (A_J) such that



$$
\operatorname{cond}P_J(x)
=\frac{\|P_J(x)\|^2}{|\det P_J(x)|}
\le A_J x^{2\lceil J/2\rceil-J}.
\tag{14}
$$



Thus the even initial cut has bounded condition number as
(x\to\infty), and the odd initial cut costs at most (O(x)).
This uses the already proved determinant and degree identities,
not a guessed limiting leading matrix. The threshold is harmless
because (J) is fixed while (x\ge c_0N^2\to\infty).

## 5. Uniform polynomial conditioning theorem

Fix (0<c_0\le c_1<\infty). Combining (11)–(14), for all
sufficiently large (N) and every (x\in[c_0N^2,c_1N^2]), gives



$$
\boxed{\operatorname{cond}P_N(x)\le C N^A,
\qquad A=3K/2+2,\quad K=704(1+1/c_0).}
\tag{15}
$$



The finite constant (C) depends only on (c_0,c_1) and the
two fixed initial cuts determined by (c_0). The exponent is
deliberately generous. The theorem is stated for sufficiently
large (N); a small-index interval could contain a finite row
eigenvalue, where the adjacent matrix is singular, so those cases
have not been absorbed into a nonexistent uniform constant.

In rational normalization,



$$
P_N=
\operatorname{diag}(\sqrt{2N+1},\sqrt{2N+3})\,
\begin{pmatrix}r_N^{(0)}&r_N^{(1)}\\r_{N+1}^{(0)}&r_{N+1}^{(1)}\end{pmatrix}
\operatorname{diag}(1,1/\sqrt3).
$$



These two diagonal transformations change the condition number by
at most a fixed factor (three suffices). Thus (15) holds for the
actual rational adjacent branch matrix as well.

## 6. Exact consequence for any separately proved determinant exponent

Let (\sigma_1\ge\sigma_2>0) be the two singular values.
The theorem implies, uniformly on the positive compact parameter range,



$$
\boxed{\log\sigma_i(P_N(cN^2))
=\tfrac12\log|\det P_N(cN^2)|+O(\log N),\quad i=1,2.}
\tag{16}
$$



It follows simply from their product being the determinant magnitude
and their ratio being the condition number. Therefore any independently
proved normalized determinant limit gives the same half-limit for
both singular values. This statement does not assume the proposed
determinant limit in its proof.

The conclusion controls every coherent two-component input at a
single spectral parameter, up to polynomial factors. It remains
distinct from a condition-number estimate for a growing mixed
evaluation matrix at many nodes. The componentwise remainder
matrix after the prescribed low-row deletion remains unresolved;
neither (15) nor a scalar determinant exponent supplies its cofactor
lower bound or an irrationality proof.
