> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent verification of the block-Loewner determinant and selected-channel scope

Date: 2026-09-13. Reviewer and bounded extension: audit_computations.

This verifies root's complete note `raw_block_loewner_determinant.md`,
Sections 1–4, using the exact matrix resolvent in
`raw_branch_matrix_christoffel_darboux.md`.
The algebra, strict positivity, even-size determinant, and boundary
normalization all pass. Sections 4–5 spell out valid selected-channel
consequences and their limitation for the actual high-row minors.
No numerical experiment is used.

## 1. Resolvent Gram factorization and strict positivity

Fix (N\ge2). Write (K_N=K_{[0,N-1]}),
(B=\iota_N\Gamma_N\in\mathbb R^{N\times2}), and



$$
M_N(x)=B^T(xI-K_N)^{-1}B.
$$



For distinct real nodes (x_1,\ldots,x_r\notin\operatorname{spec}K_N),
define (R_i=(x_iI-K_N)^{-1}). The Loewner matrix has (2\)-by-(2)
blocks



$$
L_{ij}=\frac{M_N(x_i)-M_N(x_j)}{x_j-x_i}
=B^TR_iR_jB\quad(i\ne j),\qquad
L_{ii}=-M_N'(x_i)=B^TR_i^2B.
\tag{1}
$$



Thus



$$
L=V^TV,\qquad V=[R_1B,\ldots,R_rB].
\tag{2}
$$



To verify strict positivity, put



$$
d(t)=\prod_{i=1}^r(x_i-t),\quad
W=[B,K_NB,\ldots,K_N^{r-1}B],
$$



and let the (i)-th column of (T) be the coefficients, in powers
(1,t,\ldots,t^{r-1}), of (\prod_{j\ne i}(x_j-t)).
Then the exact factorization is



$$
\boxed{V=d(K_N)^{-1}W(T\otimes I_2).}
\tag{3}
$$



The matrix (d(K_N)) is invertible by the node restriction. With
(\Delta(x)=\prod_{i<j}(x_j-x_i)), evaluation of those scalar
polynomials at the nodes gives



$$
\det T=(-1)^{r(r-1)/2}\Delta(x),\qquad
\det(T\otimes I_2)=\Delta(x)^2.
\tag{4}
$$



Indeed the evaluation matrix is diagonal; the product of its diagonal
entries is ((-1)^{r(r-1)/2}\Delta^2), and the ordinary evaluation
Vandermonde has determinant (\Delta).

If (2r\le N), the boundary Krylov matrix (W) has full column
rank. To see this directly, (K_N^jB) has support only in the last
(2j+2) rows. Its first potentially nonzero two-row block is



$$
\Gamma_{N-2j}\Gamma_{N-2j+2}\cdots\Gamma_N.
\tag{5}
$$



Each factor is invertible. Ordering the last (2r) rows from the
bottom two-row block upward makes their square submatrix block
triangular with these invertible diagonal blocks. Therefore



$$
\boxed{L\succ0\quad\text{whenever }2r\le N.}
\tag{6}
$$



This is strict positive definiteness of the full two-channel Loewner
matrix. No sign condition on scalar branch evaluation minors is used.

## 2. The exact even-size determinant and its normalization

Suppose (N=2r). The Krylov matrix (W) is square. Reversing the
order of two-row blocks has positive permutation sign, since every
block exchange moves four scalar entries. From (5),



$$
\boxed{\det W=\prod_{m=1}^{r}(\det\Gamma_{2m})^m>0.}
\tag{7}
$$



The exact factor is



$$
\det\Gamma_j=a_{j-1}a_j^2a_{j+1}.
\tag{8}
$$



For example, the two diagonal blocks at (N=4) are (\Gamma_4)
and (\Gamma_2\Gamma_4), so their determinant product is
(\det\Gamma_2(\det\Gamma_4)^2), as (7) requires. This is an
algebraic normalization illustration, not a computed root sample.

Taking determinants in (3) and then squaring gives



$$
\boxed{\det L=
\frac{\left[\prod_{m=1}^{r}(\det\Gamma_{2m})^m\right]^2
\Delta(x)^4}
{\prod_{i=1}^{r}\det(x_iI-K_N)^2}.}
\tag{9}
$$



Both the Vandermonde power four and the powers (m) in (7) are
therefore correct. The off-spectrum restriction is needed for this
resolvent formula; poles have not been silently replaced by limits.

For (2r<N), one still has the exact rectangular formula



$$
\det L=\Delta(x)^4
\det\left(W^T d(K_N)^{-2}W\right)>0.
\tag{10}
$$



Replacing its final Gram determinant by a square determinant of (W)
would be incorrect unless (N=2r).

## 3. Cancellation of all denominators in the whole branch evaluation matrix

Let



$$
U_N(x)=\begin{pmatrix}R_0(x)\\\vdots\\R_{N-1}(x)\end{pmatrix},
\qquad P_N(x)=\begin{pmatrix}R_N(x)\\R_{N+1}(x)\end{pmatrix},
$$



where (R_k=(p_k^{(0)},p_k^{(1)})) has the actual symmetric seeds.
The exact recurrence identity is



$$
U_N(x)=(xI-K_N)^{-1}B P_N(x).
\tag{11}
$$



For (N=2r), form the full two-channel evaluation matrix



$$
Y=[U_N(x_1),\ldots,U_N(x_r)]\in\mathbb R^{N\times N}.
$$



Put (c_N=\prod_{j=0}^{N-1}a_{j+1}a_{j+2}). The reviewed
Casoratian identity, and the fact that (N) is even, give
(\det P_N(x)=\det(xI-K_N)/c_N). Substituting this in (11)
cancels every resolvent denominator in (9) before squaring:



$$
\boxed{\det Y=\frac{\det W}{c_N^r}\Delta(x)^2
=\Delta(x)^2\prod_{m=1}^{r-1}
(\det\Gamma_{2m})^{-(r-m)}.}
\tag{12}
$$



The simplification uses the exact identity
(c_N=\prod_{m=1}^{r}\det\Gamma_{2m}).
All signs are positive in the specified node-block and row orders.

Equation (12) is a polynomial identity in the nodes. Consequently it
extends to all nodes, including those on the finite row spectrum.
For distinct nodes it is nonzero. Thus the whole-low-row two-channel
evaluation matrix has full column rank whenever at least (2r)
consecutive rows starting at zero are retained. For more than (2r)
rows, use its first (2r) rows. No off-spectrum hypothesis is needed
for this polynomial consequence.

For clarity, the rational branch normalization gives a different,
fully rational constant. Write (r_k=(r_k^{(0)},r_k^{(1)})) and let
(Y_r) have rows (k=0,\ldots,2r-1) and the two rational branch
columns at every node. In the notation



$$
C_k=\prod_{j=0}^{k-2}U_j
=\frac{((k-1)!)^2(k!)^2}{(2k-3)!!(2k-1)!!},
$$



one has



$$
\boxed{\det Y_r=\Delta(x)^2
\prod_{m=1}^{r-1}C_{2m+1}^{-1}.}
\tag{13}
$$



One way to check this without radicals is to group the rational
recurrence into two-row blocks. Its forward block has determinant
(U_{2j}U_{2j+1}), and the degree-(m) leading block of the
polynomial solution has determinant (C_{2m+1}^{-1}). Multiplying
those leading determinants for (m=0,\ldots,r-1), with the seed
block of determinant one, proves (13). It also agrees with (12)
after the exact row radicals and the odd factor (1/\sqrt3)
are restored.

## 4. Valid selected-channel lower bounds

There is a useful consequence for a selected **Gram** matrix. Choose
one unit vector (v_i\in\mathbb R^2) at each node and a complementary
orthonormal vector (w_i). Let (L_v) be the (r\)-by-(r) Gram
matrix of the columns (R_iBv_i). Rotate the full block Loewner
matrix by these orthogonal channel bases, then permute the selected
channels first. The Schur determinant formula and the Hadamard
inequality imply



$$
\boxed{\det L_v\ge
\frac{\det L}{\prod_{i=1}^r\|R_iBw_i\|^2}>0.}
\tag{14}
$$



Explicitly, if the complementary Gram block is (D), then
(\det L=\det L_v\det(D-C^TL_v^{-1}C)
\le\det L_v\det D\le\det L_v\prod_iD_{ii}).
The denominators in (14) are nonzero because the full set of channels
is independent. The rough bound



$$
\|R_iBw_i\|\le
\frac{\|B\|}{\operatorname{dist}(x_i,\operatorname{spec}K_N)}
$$



may be inserted if an explicit but weaker lower bound is wanted.
Nonunit chosen channels contribute their squared norms separately.

There is also a direct actual-branch version without resolvents.
Select one of the two actual branch columns at each node in (12)
or (13), and call the resulting (N\)-by-(r) matrix (Y_v).
Let (Y_{w,i}) be its complementary branch column at node (i).
Then, for (N=2r),



$$
\boxed{\det(Y_v^TY_v)\ge
\frac{(\det Y)^2}{\prod_{i=1}^r\|Y_{w,i}\|^2}>0.}
\tag{15}
$$



Use (13) if rational branches are desired. The identity and bound
hold for any distinct real nodes, including row-spectrum nodes.
For more low rows, the Gram matrix only increases in positive
semidefinite order, so the bound from its first (2r) rows remains
valid. Multiplying selected physical spectral columns by known
nonzero amplitudes multiplies the determinant by the product of
their squared amplitudes; this is an exact scaling, not a new
nonvanishing assumption.

## 5. Why this does not establish scalar sign regularity or the high-row bound

The selected-channel determinants in (14)–(15) are Gram determinants,
not signed scalar evaluation minors. In (15), Cauchy–Binet writes
the left side as a sum of squares over **all** (r\)-row minors.
A positive lower bound does not select the desired high-row minor
or make all these minors have one sign.

Likewise, deleting the low rows subtracts their positive semidefinite
Gram contribution. The lower bound for the whole Gram matrix does
not survive that subtraction without an additional estimate. If the
number of nodes exceeds (N/2), the full two-channel Loewner matrix
has more columns than rows and cannot be positive definite; selected
channels in that regime require a separate rank argument.

The exact remaining bridge is therefore quantitative control after
the prescribed low-row deletion, or a direct estimate of the
corresponding Schur complement. Neither strict positivity of the
block Loewner kernel nor the block-Vandermonde identity supplies it
by itself. The proposed determinant theorem is valid and useful,
while the scalar alternating-channel sign and high-row conditioning
claims remain unproved.

Further original extension: `raw_separated_channel_low_evaluation.md`
proves the determinant for independent channel node sets, handles odd
matrix sizes and every permutation sign, and gives an explicit inverse
by separate Lagrange interpolation. At the actual initial prolate
nodes it proves an all-index exponential bound for the inverse of the
unweighted **low-row** evaluation matrix. The prescribed high rows
remain a separate componentwise polynomial-remainder matrix.
