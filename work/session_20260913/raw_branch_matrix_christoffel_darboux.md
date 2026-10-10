> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The two-branch Green identity, positive matrix resolvent, and uniform energy bounds

Date: 2026-09-13. Original bounded continuation by audit_computations.

This continues `raw_branch_boundary_pencils_and_casoratian.md`.
All branch normalizations and the finite matrix (K) are exactly those
of `raw_boundary_free_moment_intertwiner.md`. No new root scan or
canonical Hermite–Padé construction is used.

The positive object below retains **both** branch channels. It does
not turn either individual boundary-cofactor pencil into a positive
scalar spectral problem.

## 1. The exact right and left Green forms

Write the row vector



$$
R_k(\xi)=(p_k^{(0)}(\xi),p_k^{(1)}(\xi)).
$$



Its seeds are (R_0=(1,0)), (R_1=(\sqrt3/2,1)). Set all
negative-index rows equal to zero. For a cut (N\ge1), put



$$
E_N(\xi)=\begin{pmatrix}R_{N-2}(\xi)\\R_{N-1}(\xi)\end{pmatrix},
\qquad P_N(\xi)=\begin{pmatrix}R_N(\xi)\\R_{N+1}(\xi)\end{pmatrix},
$$





$$
\Gamma_N=
\begin{pmatrix}
a_{N-1}a_N&0\\-a_N&a_Na_{N+1}
\end{pmatrix}.
\tag{1}
$$



Define



$$
W_N(x,y)=E_N(x)^T\Gamma_NP_N(y)
-P_N(x)^T\Gamma_N^TE_N(y),\qquad W_0=0.
\tag{2}
$$



Then for (0\le a\le b),



$$
\boxed{(y-x)\sum_{k=a}^{b}R_k(x)^TR_k(y)
=W_{b+1}(x,y)-W_a(x,y).}
\tag{3}
$$



This is a polynomial identity in two independent variables. To prove
it, multiply (KR(y)=yR(y)) on the left by (R(x)^T), subtract
the transposed equation at (x), and sum over the interval.
Internal terms cancel by symmetry of (K). Exactly three edges cross
the right cut:



$$
(N-2,N):a_{N-1}a_N,\quad
(N-1,N):-a_N,\quad
(N-1,N+1):a_Na_{N+1}.
$$



They give (1)–(2). The same three edges at the left cut enter with
opposite sign. There are no left-boundary terms at zero, because the
negative-index rows are absent. Thus the special seed conditions do
not introduce an omitted boundary observation in (3).

In particular,



$$
\boxed{(y-x)\sum_{k=0}^{N-1}R_k(x)^TR_k(y)=W_N(x,y).}
\tag{4}
$$



At (x=y), (4) first gives (W_N(x,x)=0). Differentiating in (y)
then gives the exact diagonal matrix Christoffel–Darboux identity



$$
\boxed{\sum_{k=0}^{N-1}R_k(x)^TR_k(x)
=E_N(x)^T\Gamma_NP_N'(x)
-P_N(x)^T\Gamma_N^TE_N'(x).}
\tag{5}
$$



For real (x) and (N\ge2), this Gram matrix is positive definite.
The first two summands already equal



$$
\begin{pmatrix}7/4&\sqrt3/2\\\sqrt3/2&1\end{pmatrix},
\tag{6}
$$



which has determinant one and least eigenvalue
((11-\sqrt{57})/8>0). Formula (5) is a matrix positivity statement,
not a sign assertion about its off-diagonal entry.

## 2. A positive finite matrix spectral measure

Now let (N\ge2), put (K_N=K_{[0,N-1]}), and let
(\iota_N:\mathbb R^2\to\mathbb R^N) inject into the last two
coordinates. The previous note proves



$$
\det(K_N-\xi I)=
\Bigl(\prod_{j=0}^{N-1}a_{j+1}a_{j+2}\Bigr)\det P_N(\xi).
\tag{7}
$$



Thus (P_N(\xi)) is invertible whenever (\xi\notin\operatorname{spec}K_N).
Define the (2\)-by-(2) rational matrix



$$
M_N(\xi)=\Gamma_N^TE_N(\xi)P_N(\xi)^{-1}.
\tag{8}
$$



It is symmetric, by (W_N(\xi,\xi)=0). More precisely,



$$
\boxed{M_N(\xi)=
\Gamma_N^T\iota_N^T(\xi I-K_N)^{-1}\iota_N\Gamma_N.}
\tag{9}
$$



Indeed the matrix of interior branch rows (U_N=(R_0;\ldots;R_{N-1}))
satisfies



$$
(K_N-\xi I)U_N=-\iota_N\Gamma_NP_N.
$$



Multiplication by the inverses, followed by restriction to its last two
rows, proves (9), including its sign.

If (\Pi_\mu) is the orthogonal spectral projection of (K_N),
then



$$
M_N(\xi)=\sum_\mu\frac{W_\mu}{\xi-\mu},\qquad
W_\mu=\Gamma_N^T\iota_N^T\Pi_\mu\iota_N\Gamma_N\succeq0.
\tag{10}
$$



Every eigenvalue appears. An eigenvector with both last coordinates
zero must have its preceding coordinate zero by the last recurrence
row, then the next preceding one by the next row, and so on. Hence
restriction to the last two coordinates is injective on each
eigenspace. Since (\Gamma_N) is invertible, the rank of (W_\mu)
equals that eigenspace dimension, which is at most two.

The support in (10) is the finite spectrum of the **row matrix** (K_N).
It is not the positive prolate spectrum of the column operator (S).
In particular it need not be negative or positive as a whole. The
previous note shows that it always contains a positive eigenvalue.

## 3. Matrix positivity and the exact divided difference

Multiplying (4) by (P_N(x)^{-T}) and (P_N(y)^{-1}) gives



$$
\boxed{\frac{M_N(x)-M_N(y)}{y-x}
=P_N(x)^{-T}
\left(\sum_{k=0}^{N-1}R_k(x)^TR_k(y)\right)P_N(y)^{-1}.}
\tag{11}
$$



At a real parameter outside the finite spectrum,



$$
\boxed{-M_N'(x)=P_N(x)^{-T}
\left(\sum_{k=0}^{N-1}R_k(x)^TR_k(x)\right)P_N(x)^{-1}\succ0.}
\tag{12}
$$



Equivalently, (9) gives
(-M_N'(x)=\Gamma_N^T\iota_N^T(xI-K_N)^{-2}\iota_N\Gamma_N).
For complex (z) in the upper half-plane,



$$
\operatorname{Im}M_N(z)=-(\operatorname{Im}z)
\Gamma_N^T\iota_N^T(\bar zI-K_N)^{-1}
(zI-K_N)^{-1}\iota_N\Gamma_N\prec0.
\tag{13}
$$



The kernel obtained by replacing (x) in (11) with (\bar x)
is positive semidefinite as a block kernel on any finite collection
of parameters off the spectrum: its right side is explicitly a
Gram kernel. Individual off-diagonal matrix entries or mixed scalar
evaluation determinants need not be positive.

## 4. Uniform two-channel bounds when (x\) is of order (N^2)

Fix (0<c_0\le c_1<\infty), and suppose



$$
c_0N^2\le x\le c_1N^2,\qquad
N\ge\max\{8,4/c_0\}.
\tag{14}
$$



The already proved row bound gives (K_N\preceq(N+3/4)I).
A useful matching crude lower bound is



$$
(-N^2+3/8)I\preceq K_N\preceq(N+3/4)I.
\tag{15}
$$



For the lower bound, compress (K=J^2-J-\Lambda); the compressed
(J^2) is positive semidefinite, while
(\|J_{[0,N-1]}\|\le N-3/8) and
(\|\Lambda_{[0,N-1]}\|=N(N-1)). This yields (15). The compression
of (J^2) has not been replaced by the square of the compressed (J).

The elementary estimates (j/2\le a_j\le(j+1)/2) imply, for
(N\ge8),



$$
\frac{N^2}{8}\le\sigma_{\min}(\Gamma_N)
\le\|\Gamma_N\|\le\frac{N^2}{2}.
\tag{16}
$$



For the lower estimate subtract the norm of its single off-diagonal
entry from its smaller diagonal: this gives
((N^2-3N-2)/4\ge N^2/8). The analogous upper estimate is
((N+1)(N+4)/4\le N^2/2).

From (14)–(16), the two positive matrices satisfy



$$
\boxed{\frac{N^2}{64(c_1+1)}I
\preceq M_N(x)\preceq\frac{N^2}{2c_0}I,}
\tag{17}
$$





$$
\boxed{\frac1{64(c_1+1)^2}I
\preceq-M_N'(x)\preceq\frac1{c_0^2}I.}
\tag{18}
$$



For example, the largest eigenvalue of (xI-K_N) is at most
((c_1+1)N^2), while its smallest is at least (c_0N^2/2).
Apply these inequalities to the resolvent and its square, then use
(16). No accessory limit or fixed-index asymptotic enters these
growing-index estimates.

Combining (12) and (18) proves the following uniform coherent energy
comparison:



$$
\boxed{\frac{P_N(x)^TP_N(x)}{64(c_1+1)^2}
\preceq\sum_{k=0}^{N-1}R_k(x)^TR_k(x)
\preceq\frac{P_N(x)^TP_N(x)}{c_0^2}.}
\tag{19}
$$



This holds for every coherent linear combination of the two branch
columns, not just each column separately. In rational normalization,
let (r_k=(r_k^{(0)},r_k^{(1)})). Cancelling the fixed congruence
(\operatorname{diag}(1,1/\sqrt3)) yields the same constants with



$$
\sum_{k<N}(2k+1)r_k^Tr_k
\quad\text{and}\quad
(2N+1)r_N^Tr_N+(2N+3)r_{N+1}^Tr_{N+1}
\tag{20}
$$



in place of the middle and outer matrices of (19).

## 5. An exponential lower bound for the actual adjacent branch matrix

The characteristic determinant identity supplies a further quantitative
fact at the same growing parameter scale. Write



$$
\mathcal P_N(x)=\begin{pmatrix}r_N^{(0)}(x)&r_N^{(1)}(x)\\
r_{N+1}^{(0)}(x)&r_{N+1}^{(1)}(x)\end{pmatrix}.
$$



Using (U_j\le(j+2)^2) and (15),



$$
\begin{aligned}
|\det\mathcal P_N(x)|
&=\frac{\prod_{\mu\in\operatorname{spec}K_N}|x-\mu|}
{\prod_{j=0}^{N-1}U_j}\\
&\ge\frac{(c_0N^2/2)^N}{((N+1)!)^2}
\ge(c_0/8)^N.
\end{aligned}
\tag{21}
$$



The last inequality uses (((N+1)!)^2\le(N+1)^{2N}\le(2N)^{2N}).
The earlier entire-parameter bound in
`raw_spectral_branch_generating_function.md`, with any fixed disk
radius (0<\rho<1), gives



$$
\max_{j=N,N+1;\ \sigma=0,1}|r_j^{(\sigma)}(x)|\le e^{C N}
$$



for a constant depending only on (c_1,\rho), after increasing it
to cover the finite prefactor. Hence (21) gives



$$
\boxed{\sigma_{\min}(\mathcal P_N(x))\ge e^{-C' N},
\qquad \|\mathcal P_N(x)\|\le e^{C'N}.}
\tag{22}
$$



This is a proved all-index estimate for the actual adjacent two-row,
two-branch matrix at one parameter of order (N^2). It is not a claim
about the growing matrix of many different rows at many different
prolate nodes.

Finally (7) and (x>N+3/4) give
(\operatorname{sign}\det\mathcal P_N(x)=(-1)^N).
Since both nonzero branches are positive for (x>1), this also gives
the exact alternating adjacent comparison



$$
\operatorname{sign}\left(
\frac{r_{N+1}^{(1)}(x)}{r_{N+1}^{(0)}(x)}
-\frac{r_N^{(1)}(x)}{r_N^{(0)}(x)}\right)=(-1)^N
\quad(x>\max\{1,N+3/4\}).
\tag{23}
$$



It is not an individual-root interlacing theorem.

## 6. Remaining scope

The boundary matrix, matrix spectral measure, CD identity, and coherent
energy comparison are exact. They avoid the false scalar positivity
shortcut by retaining the two-dimensional endpoint data throughout.
The unresolved step for actual high-row cofactors remains a comparison
across different spectral parameters and many growing row indices.
Neither the positive matrix kernel nor the exponential bound for each
adjacent (2\)-by-(2) block prevents cancellation or small singular
values in that larger mixed evaluation matrix. No primitive-height or
irrationality conclusion follows from these identities alone.

Verification: the same generic symbolic checker
`check_raw_branch_boundary_identities.py` verifies every entry of (4)
at sizes 2 and 3, with two independent spectral variables and an
arbitrary left seed. Both passed; the results are included in
`raw_branch_boundary_identity_checks.json`. The uniform bounds are
proved above and are not inferred from these controls.
