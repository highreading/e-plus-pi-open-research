> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# All fixed-size low-node minors and their singular-value scales

Date: 2026-09-13. Original continuation by audit_results, following
root's endpoint-polynomial reduction. Independent audit requested.

This note proves the complete determinant asymptotic and all singular-
value orders for a fixed number of distinct actual prolate nodes and
proportionally separated large rows. The proof takes enough Taylor
terms before applying finite Cauchy–Binet. In particular it does not
use an entrywise first-order approximation inside a determinant whose
leading term can have much higher order.

Every node, row proportion, and the number of columns is fixed. No
claim with a growing number of nodes or adjacent large row indices
is made.

## 1. Actual normalization and theorem

Use E_k=c_k sqrt(2k+1)F_k and the actual spectral data from
raw_fixed_node_branch_asymptotics.md and its passing independent
review. Write



$$
L_k=\int_0^1E_k(x)dx>0,\qquad
M_{k,\ell}=\frac{\langle E_k,\psi_\ell\rangle}
 {L_k\psi_\ell(1)}
=\frac{g_\ell p_k^{(\ell\bmod2)}(\xi_\ell)}
 {L_k\psi_\ell(1)}.
\tag{1}
$$



The endpoint values psi_l(1) and amplitudes g_l are nonzero by the
reviewed spectral proofs. This normalization is phase invariant.
Each node uses its own matching parity branch; the nodes may have
either or both parities.

Fix an integer m>=1, distinct positive real t_1,...,t_m, and
distinct actual nodes xi_(ell_1),...,xi_(ell_m). Put



$$
k_i(n)=\lfloor t_i n\rfloor,\quad
\zeta_j=\xi_{\ell_j},\quad x_i=t_i^{-1/2},\quad
q=\frac{m(m-1)}2,\quad
\mathsf A_n=(M_{k_i(n),\ell_j})_{i,j=1}^m.
\tag{2}
$$



The rows k_i(n) are positive and distinct for sufficiently large n.
For a vector v=(v_1,...,v_m), use
Delta(v)=product_(i<j)(v_j−v_i).

**Theorem.** As n tends to infinity,



$$
\boxed{
\det\mathsf A_n
=\frac{(-1)^q}{\prod_{r=0}^{m-1}r!}
 \Delta(\zeta_1,\ldots,\zeta_m)
 \Delta(x_1,\ldots,x_m)
 n^{-q/2}\bigl(1+O(n^{-1/2})\bigr).}
\tag{3}
$$



The implicit constant depends on the fixed nodes, proportions and m.
Its leading coefficient is nonzero. If both the t_i and the zeta_j
are in increasing order, that coefficient is positive, because the
x_i are then decreasing and Delta(x) has sign (−1)^q.

Moreover, in decreasing singular-value order s_1>=...>=s_m,



$$
\boxed{
s_j(\mathsf A_n)=\Theta\bigl(n^{-(j-1)/2}\bigr),
\quad 1\le j\le m.}
\tag{4}
$$



Here Theta means two positive bounds depending only on the same
fixed data. In particular the least singular value is of order
n^(-(m−1)/2), and the condition number is of order n^((m−1)/2).

## 2. Endpoint Taylor polynomials in the spectral parameter

Define the normalized endpoint eigenfunction



$$
f_\ell(y)=\frac{\psi_\ell(1-y)}{\psi_\ell(1)}.
$$



It is analytic, with f_l(0)=1. Transforming the reviewed differential
equation T psi=xi psi, where
T psi=[x(x−1)psi']'+(x²−x+1)psi, gives



$$
y(1-y)f''+(1-2y)f'+(\xi-1+y-y^2)f=0.
\tag{5}
$$



Write f_l(y)=sum_(r>=0)a_r(xi_l)y^r. The coefficients are determined
by a_0=1, a_r=0 for negative indices, and for r>=1



$$
\boxed{
r^2a_r(\xi)
=[r(r-1)+1-\xi]a_{r-1}(\xi)
 -a_{r-2}(\xi)+a_{r-3}(\xi).}
\tag{6}
$$



Indeed the coefficient of y^(r−1) in (5) is
r²a_r+[xi−1−r(r−1)]a_(r−1)+a_(r−2)−a_(r−3).
This proves (6), including its small-index cases without introducing
negative derivatives. In particular a_1=1−xi. Induction gives



$$
\deg a_r=r,\qquad
[\xi^r]a_r(\xi)=\frac{(-1)^r}{(r!)^2}.
\tag{7}
$$



Thus these are one sequence of polynomials in the node, independent
of which actual eigenfunction realizes it.

For each fixed R>=0 and the finitely many nodes under consideration,
Taylor's formula on the real interval 0<=y<=1 gives uniformly



$$
f_{\ell_j}(y)=\sum_{r=0}^R a_r(\zeta_j)y^r
 +O_R(y^{R+1}).
\tag{8}
$$



The constant can be taken to be the largest appropriate derivative
bound on this compact interval, over this finite node set. Entire
continuation is more than is needed: C^(R+1) regularity suffices for
(8). No bound uniform in a moving node set is asserted.

## 3. Endpoint moments and the effect of integer rounding

Let



$$
\mu_r(k)=\frac{\int_0^1(1-x)^rE_k(x)dx}{L_k}.
$$



The positive endpoint-moment theorem in Section8 of the preceding
note gives, for each fixed r>=0,



$$
\mu_r(k)=r!k^{-r/2}\bigl(1+O_r(k^{-1/2})\bigr).
\tag{9}
$$



For r=0, the identity mu_0=1 is exact. Positivity of E_k makes
the integrated Taylor remainder in (8) bounded by a constant
times mu_(R+1)(k), even though the eigenfunction itself need not
have one sign.

Put epsilon=n^(-1/2). Since k_i(n)=t_i n+O(1), (9) yields



$$
\mu_r(k_i(n))
=\epsilon^r\bigl(r!x_i^r+O_r(\epsilon)\bigr),
\quad 0\le r\le R+1,
\tag{10}
$$



uniformly over the finite index sets. The additional relative
error from rounding is O(1/n), smaller than the retained
O(epsilon) error. Also mu_r(k_i)=O(epsilon^r). This explicitly
includes the floor in (2).

Combining (1), (8) and positivity gives the finite matrix expansion



$$
\mathsf A_n=\mathsf U_n^{(R)}\mathsf C^{(R)}
 +O(\epsilon^{R+1}),
\quad
(\mathsf U_n^{(R)})_{ir}=\mu_r(k_i(n)),\quad
(\mathsf C^{(R)})_{rj}=a_r(\zeta_j),
\tag{11}
$$



where r=0,...,R. The final error holds entrywise and in every
matrix norm in this fixed dimension.

## 4. Determinant proof with enough Taylor orders

Take R=q=m(m−1)/2. This choice always satisfies R>=m−1.
All entries of A_n and U_n C are bounded by fixed constants,
so the determinant, as a fixed-degree polynomial in its entries,
is Lipschitz on this bounded set. Equation (11) therefore gives



$$
\det\mathsf A_n
=\det(\mathsf U_n^{(q)}\mathsf C^{(q)})
 +O(\epsilon^{q+1}).
\tag{12}
$$



This is the step that requires more Taylor orders when m is large.
A remainder of order epsilon² in each entry would not suffice.

Apply ordinary finite Cauchy–Binet to the product in (12). A term
corresponding to indices 0<=r_1<...<r_m<=q is



$$
\det(\mu_{r_s}(k_i))_{i,s=1}^m
 \det(a_{r_s}(\zeta_j))_{s,j=1}^m.
\tag{13}
$$



Factoring epsilon^(r_s) from each moment column and using (10)
bounds it by O(epsilon^(sum r_s)). The unique index set with
sum r_s=q is {0,1,...,m−1}; every other set has sum at least
q+1. There are finitely many such sets because m and q are fixed.
The distinguished moment determinant is



$$
\begin{aligned}
\det(\mu_r(k_i))_{\substack{1\le i\le m\\0\le r\le m-1}}
&=\epsilon^q\left[
 \left(\prod_{r=0}^{m-1}r!\right)\Delta(x_1,\ldots,x_m)
 +O(\epsilon)\right].
\end{aligned}
\tag{14}
$$



The nonzero Vandermonde follows because the t_i are distinct.
The corresponding coefficient determinant is exact: by (7),
the change from monomials 1,xi,...,xi^(m−1) to a_0,...,a_(m−1)
is triangular with the indicated diagonal. Therefore



$$
\det(a_r(\zeta_j))_{\substack{0\le r\le m-1\\1\le j\le m}}
=\frac{(-1)^q}{\prod_{r=0}^{m-1}(r!)^2}
 \Delta(\zeta_1,\ldots,\zeta_m).
\tag{15}
$$



Insert (14)–(15) in (12)–(13). Every other term and the original
Taylor error are O(epsilon^(q+1)). Since the distinguished leading
constant is nonzero, this proves (3) with the stated relative error.
The argument includes m=1: q=0, the single entry tends to1.

## 5. All singular-value orders

For every integer r with 0<=r<=m−1, truncate (11) before degree r,
that is, retain Taylor degrees 0,...,r−1. Its rank is at most r.
For r=0 this is the zero matrix. Taylor's remainder and (9) give
an operator-norm error O(epsilon^r). The variational characterization
of singular values, or the elementary rank-approximation inequality,
therefore gives



$$
s_{r+1}(\mathsf A_n)\le C_r\epsilon^r.
\tag{16}
$$



For completeness the rank-approximation inequality follows by
restricting A_n to the nullspace of the rank-r approximant, which
has dimension at least m−r, and applying the min–max formula.
Thus no positivity of the full mixed matrix is used.

By (3), |det A_n|>=c epsilon^q for sufficiently large n. Since
the product of its singular values equals its determinant magnitude,
the upper bounds (16), applied to every factor except the j-th, give



$$
s_j(\mathsf A_n)
=\frac{|\det\mathsf A_n|}{\prod_{i\ne j}s_i(\mathsf A_n)}
\ge c_j\epsilon^{\,q-\sum_{i\ne j}(i-1)}
=c_j\epsilon^{j-1}.
\tag{17}
$$



Equation (3) ensures all singular values are nonzero at these n,
so this division is valid. Together with (16), (17) proves (4).

## 6. Exact scope and relevance to the main analytic obstruction

For the row-normalized actual moments <E_k,psi_l>/L_k, multiply
A_n on the right by the fixed invertible diagonal of psi_l(1).
Its determinant acquires their product, and all singular-value
orders in (4) remain the same. Similarly one can include or remove
the fixed nonzero factors g_l for these fixed nodes.

Removing the row factors L_(k_i) is different: they grow like
e^(2sqrt(k_i))/(2pi k_i^(3/4)) and are not uniformly comparable
when the t_i differ. Thus (4) is explicitly a theorem in the
normalization (1), not an unscaled singular-value theorem for the
original high rows.

This establishes eventual nonvanishing and a precise polynomial
conditioning hierarchy for every fixed-size low-node block with
proportionally separated rows. It explains its leading rank-one
appearance without mistaking that limiting rank for exact rank.
The proof uses q=m(m−1)/2 Taylor orders and constants from the
chosen eigenfunctions and Vandermonde gaps. It does not supply
control as m grows, as nodes move, or when proportions coalesce.
In particular it must not be substituted for the unresolved
inverse estimate on the growing actual high-row matrix or the
primitive final remainder.
