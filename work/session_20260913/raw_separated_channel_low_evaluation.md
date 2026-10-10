> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Separated-channel evaluation: exact determinants, interpolation, and a uniform low-matrix inverse

Date: 2026-09-13. Original bounded extension by audit_computations,
following root's separated-channel observation.

This extends `raw_block_loewner_determinant.md` and
`raw_block_loewner_independent_review.md`. It concerns the actual two
polynomial branches and consecutive rows starting at zero. It proves
an exact determinant and an exponential inverse bound at the actual
initial prolate nodes. It does not assert an inverse bound for the
prescribed high-row interval.

## 1. A triangular vector-polynomial basis with its exact leading factors

Let (r_k=(r_k^{(0)},r_k^{(1)})) be the rational branches, with
seeds ((1,0)), ((1/2,1)). Use the interleaved monomial rows



$$
e_0(\xi)=(1,0),\ e_1(\xi)=(0,1),\
e_2(\xi)=(\xi,0),\ e_3(\xi)=(0,\xi),\ldots.
$$



For (N\ge1), the rows (r_0,\ldots,r_{N-1}) are related to
(e_0,\ldots,e_{N-1}) by a lower triangular rational matrix
(H_N), and



$$
\begin{aligned}
(H_N)_{2j,2j}&=\prod_{h=0}^{j-1}U_{2h}^{-1},\\
(H_N)_{2j+1,2j+1}&=\prod_{h=0}^{j-1}U_{2h+1}^{-1},
\end{aligned}\qquad
U_k=\frac{(k+1)^2(k+2)^2}{(2k+1)(2k+3)}.
\tag{1}
$$



Empty products equal one. The degree caps prove triangularity. For
an even row's first component, the only term producing its new top
degree in the recurrence is (\xi r_{2j-2}^{(0)}). For an odd
row's second component it is (\xi r_{2j-1}^{(1)}). This proves
(1) by induction and also proves that all diagonal entries are
strictly positive. Consequently



$$
\boxed{h_N:=\det H_N
=\prod_{k=0}^{N-3}U_k^{-\lfloor(N-1-k)/2\rfloor}>0.}
\tag{2}
$$



The product is empty when (N\le2). With
(m=\lceil N/2\rceil), (q=\lfloor N/2\rfloor), the rows form
a basis of all vector polynomials



$$
(f_0,f_1),\qquad \deg f_0<m,\quad \deg f_1<q.
\tag{3}
$$



For the symmetric branches (R_k=(p_k^{(0)},p_k^{(1)})), the
same assertion holds with seeds ((1,0)), ((\sqrt3/2,1)).
Their triangular coefficient matrix (H_N^p) has diagonal



$$
(H_N^p)_{2j,2j}=(a_1\cdots a_{2j})^{-1},\qquad
(H_N^p)_{2j+1,2j+1}=(a_2\cdots a_{2j+1})^{-1}.
\tag{4}
$$



The special seed offset affects lower entries, not these factors.

## 2. Independent node sets in the two channels

Take distinct (x_1,\ldots,x_m) within channel zero and distinct
(y_1,\ldots,y_q) within channel one. Coincidences between the two
sets are allowed. Let the (N\)-by-(N) matrix (Y_r) have rows
(r_0,\ldots,r_{N-1}) evaluated in those selected channels, with
all channel-zero columns first and then all channel-one columns.
Write (\Delta(x)=\prod_{i<j}(x_j-x_i)), and similarly for (y),
with empty Vandermondes equal to one. Then



$$
\boxed{\det Y_r=(-1)^{s_N}h_N\Delta(x)\Delta(y),\qquad
s_N=q(m-1)-q(q-1)/2.}
\tag{5}
$$



To verify the sign, reorder the interleaved monomial rows so that
all channel-zero monomials precede all channel-one monomials. The
number of crossings is
(\sum_{j=0}^{q-1}(m-1-j)=s_N). The resulting evaluation matrix
is the block diagonal pair of ordinary Vandermonde matrices. Multiply
by the triangular coefficient determinant (2). Thus (5) includes
every row and column permutation sign.

When (N=2r), (s_N=r(r-1)/2), and



$$
h_{2r}=\prod_{j=1}^{r-1}C_{2j+1}^{-1},\qquad
C_k=\prod_{i=0}^{k-2}U_i.
$$



Interleaving paired channel columns with (x_i=y_i) introduces the
same sign again and gives the previously proved positive constant
times (\Delta(x)^2).

For the actual nodes (\xi_0,\ldots,\xi_{N-1}), use channel
(l\bmod2) at (\xi_l), and keep the columns in increasing
spectral index. Their interleaving cancels the sign in (5). Thus



$$
\boxed{\det Y_{r,\mathrm{low}}
=h_N\Delta(\xi_0,\xi_2,\ldots)
\Delta(\xi_1,\xi_3,\ldots)>0.}
\tag{6}
$$



Only strict ordering within each parity is needed, and it follows
from the reviewed prolate spectral bounds. In particular the actual
counts among nodes (0,\ldots,n) fit (3) with (N=n+1).
The same formula holds for symmetric branches with (h_N^p) in
place of (h_N).

## 3. An explicit inverse by two independent Lagrange interpolations

Suppose coefficients (c_k) are sought so that
(\sum_{k=0}^{N-1}c_k r_k) takes prescribed values (v_i) at
the channel-zero nodes and (w_j) at the channel-one nodes.
Construct



$$
f_0(\xi)=\sum_{i=1}^{m}v_i
\prod_{h\ne i}\frac{\xi-x_h}{x_i-x_h},\qquad
f_1(\xi)=\sum_{j=1}^{q}w_j
\prod_{h\ne j}\frac{\xi-y_h}{y_j-y_h}.
\tag{7}
$$



Let (b) be their interleaved monomial coefficient vector. Then



$$
\boxed{c=H_N^{-T}b.}
\tag{8}
$$



Indeed (Y_r^Tc) is the requested value vector, and the coefficient
vector of (\sum c_kr_k) is (H_N^Tc). This proves the inverse
formula with its orientation. It applies without any spectral
parameter restrictions or numerical degree construction.

## 4. The scaled coefficient inverse has a polynomial norm bound

There is a particularly simple exact realization of the inverse in
symmetric normalization. Let (K_N=K_{[0,N-1]}), let (e_j^T)
denote coordinate rows, and write (s=\sqrt3/2). Whenever the
indicated degree index is below (N),



$$
\xi^j(1,0)=e_0^T K_N^jU_N(\xi),\qquad
\xi^j(0,1)=(e_1^T-se_0^T)K_N^jU_N(\xi),
\tag{9}
$$



where (U_N=(R_0;\ldots;R_{N-1})). Multiplication by (K) moves
an index by at most two. The maximal index in the first formula is
(2j<N), and in the second it is (2j+1<N). No path leaves the
compression in these formulas, so the infinite recurrence gives
exactly (9), with no omitted boundary term.

Set (\xi=N^2z), and let (\widetilde H_N^p) be the coefficient
matrix of (R_0(N^2z),\ldots,R_{N-1}(N^2z)) in the interleaved
monomial basis in (z). Formula (9), divided by (N^{2j}), gives
each row of its inverse.

The reviewed bounds



$$
(-N^2+3/8)I\preceq K_N\preceq(N+3/4)I
$$



imply (\|K_N\|\le N^2) for (N\ge2). Therefore every even
row of ((\widetilde H_N^p)^{-1}) has Euclidean norm at most one,
and every odd row has norm at most (\sqrt{1+s^2}=\sqrt7/2).
The Frobenius norm consequently yields



$$
\boxed{\| (\widetilde H_N^p)^{-1}\|\le\frac{\sqrt{7N}}2
\qquad(N\ge2).}
\tag{10}
$$



This is a bound for the inverse coefficient transform, not an
unjustified bound obtained by inverting entrywise estimates.

## 5. Exponential interpolation bound at the actual parity nodes

The actual spectral enclosure is



$$
l(l+1)+3/4\le\xi_l\le l(l+1)+1.
\tag{11}
$$



In a parity channel write (\eta_i=\xi_{2i+\sigma}/N^2),
(i=0,\ldots,t-1), where (t=m) or (q). All its nodes lie
in ([0,1]). For (i\ne j), (11) gives the convenient bound



$$
|\xi_{2j+\sigma}-\xi_{2i+\sigma}|
\ge2|j-i|(i+j+1).
\tag{12}
$$



For example, with (j>i) the lower bound before simplification is
(4(j-i)(i+j+\sigma+1/2)-1/4). Subtracting the right side
of (12) leaves at least (2(j-i)(i+j)-1/4>0), since
(i+j\ge1).

Thus every scaled Lagrange denominator satisfies



$$
\begin{aligned}
\prod_{j\ne i}|\eta_i-\eta_j|
&\ge \frac{2^{t-1}i!(t-1-i)!}{N^{2(t-1)}}
\prod_{j\ne i}(i+j+1)\\
&\ge\left(\frac{(t-1)!}{N^{t-1}}\right)^2.
\end{aligned}
\tag{13}
$$



For the second inequality use
(i!(t-1-i)!\ge(t-1)!/2^{t-1}) and
(\prod_{j\ne i}(i+j+1)\ge t!/(i+1)\ge(t-1)!).

If (t=1), its cardinal polynomial is simply one. If (t\ge2),
then (N\le2t+1\le5(t-1)) and
((t-1)!\ge((t-1)/e)^{t-1}). The denominator in (13) is
therefore at least ((5e)^{-2(t-1)}). The numerator cardinal
polynomial has coefficient $\ell^1$ norm at most
(\prod_{j\ne i}(1+|\eta_j|)\le2^{t-1}). Every cardinal
coefficient vector consequently has norm at most



$$
(50e^2)^{t-1}.
\tag{14}
$$



Let (E_N) be the interleaved monomial evaluation matrix at these
scaled parity-selected nodes. Its inverse transpose consists of
the cardinal coefficient columns from the two channels. Hence



$$
\|E_N^{-1}\|\le\sqrt N\,(50e^2)^{\lceil N/2\rceil-1}.
\tag{15}
$$



The actual symmetric-branch low evaluation matrix factors as
(Y_{p,\mathrm{low}}=\widetilde H_N^p E_N). Combining (10) and
(15) proves the fully explicit all-index estimate



$$
\boxed{\|Y_{p,\mathrm{low}}^{-1}\|
\le\frac{\sqrt7}{2}N(50e^2)^{\lceil N/2\rceil-1}
\qquad(N\ge2).}
\tag{16}
$$



Equivalently its smallest singular value is at least the reciprocal
of the displayed bound. The earlier branch generating-function upper
bound gives (\|Y_{p,\mathrm{low}}\|\le e^{O(N)}) as well.
Thus this entire low evaluation matrix has at most exponential
condition number, in this exact unweighted normalization.

For rational branches, the relation is



$$
Y_{p,\mathrm{low}}=
\operatorname{diag}(\sqrt{2k+1})\,
Y_{r,\mathrm{low}}\,
\operatorname{diag}(1\text{ on even nodes},1/\sqrt3\text{ on odd nodes}).
$$



Therefore the bound for (\|Y_{r,\mathrm{low}}^{-1}\|) differs
from (16) by at most a factor (\sqrt{2N-1}). For the actual
spectral moment columns (g_l p_k^{(l\bmod2)}(\xi_l)), the
known nonzero amplitudes form one additional diagonal matrix:



$$
\|M_{\mathrm{low}}^{-1}\|
\le\|Y_{p,\mathrm{low}}^{-1}\|\max_{l<N}|g_l|^{-1}.
\tag{17}
$$



Their potentially small size has not been suppressed.

## 6. An exact high-row reduction, and the missing estimate

For the same two node sets, form the node polynomials



$$
Q_0(\xi)=\prod_i(\xi-x_i),\qquad
Q_1(\xi)=\prod_j(\xi-y_j).
$$



Every additional branch row (r_k\), including the desired high
rows, has the same selected node values as the vector polynomial



$$
\bigl(r_k^{(0)}\bmod Q_0, r_k^{(1)}\bmod Q_1\bigr).
\tag{18}
$$



Represent this pair in the low-row basis using (8). If its coefficient
row is (a_k^T), the exact evaluation identity is



$$
Y_{\mathrm{high}}=A_{\mathrm{rem}}Y_{\mathrm{low}},
\tag{19}
$$



where (A_{\mathrm{rem}}) collects those rows. Thus the low matrix
has an explicit determinant and a controlled inverse, while the
remaining rank and conditioning problem is precisely the remainder
coefficient matrix in (18)–(19). Its componentwise reductions use
two different node polynomials and can cancel. The bounds for
(Y_{\mathrm{low}}) do not lower-bound the nonzero singular values
or the cofactors of (A_{\mathrm{rem}}).

This identifies the additional estimate needed after the rigorous
low-row result. It does not infer high-row sign regularity, endpoint
noncancellation, primitive shrinking, or irrationality from a
Vandermonde determinant.
