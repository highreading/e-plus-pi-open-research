> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual high-row problem as a projected vanishing module and a two-dimensional determinant

Date: 2026-09-13. Original bounded continuation by audit_computations.

Independent review: `raw_high_multipoint_independent_review.md`
passes all substantive claims. Its explicit small-error range and
one display correction have been incorporated.

This note concerns exactly the rows `n+1,...,2n-1` and the actual
parity-selected prolate nodes `0,...,n`, for `n>=2`. It adds two
explicit constructions to the earlier abstract remainder factor
`A_rem`: a finite polynomial-of-Krylov construction using both node
polynomials, and a complementary two-dimensional determinant for
the actual finite kernel angle. A second representation uses only
the boundary matrices at cuts `n+1` and `2n` and gives a smaller
Schur-complement target.

No lower bound for the new determinant is proved. The distinction
between a small determinant formula and a uniformly controlled
inverse inside that formula is retained throughout.

## 1. Conventions and the prescribed matrices

Use the symmetric branches



$$
R_k(\xi)=(p_k^{(0)}(\xi),p_k^{(1)}(\xi)),\quad
R_0=(1,0),\quad R_1=(s,1),\quad s=\sqrt3/2.
$$



Let `Y` have rows `R_0,...,R_n` and columns given by evaluation in
channel `sigma_l=l mod 2` at `xi_l`, for `0<=l<=n`. Define



$$
Y_{\rm hi}=\bigl[p_k^{(\sigma_l)}(\xi_l)\bigr]_%
{n+1\le k\le2n-1,\ 0\le l\le n},\qquad
S=Y\,D_g,\qquad H=Y_{\rm hi}D_g,\qquad
D_g=\operatorname{diag}(g_0,\ldots,g_n).
\tag{1}
$$



The amplitudes are the actual nonzero amplitudes in
`raw_spectral_amplitude_factorial_theorem.md`. They are not discarded
or replaced by their asymptotic scale. The low determinant theorem
proves that `Y`, hence `S`, is invertible. Positive row normalization
by the radicals `d_(k,n)` does not change `ker H`; it does change
singular values and is not suppressed in a singular-value claim.

Write



$$
m_0=\left\lceil\frac{n+1}{2}\right\rceil,\qquad
m_1=\left\lfloor\frac{n+1}{2}\right\rfloor,\qquad
Q_\sigma(\xi)=\prod_{\substack{0\le l\le n\\l\equiv\sigma\ (2)}}
(\xi-\xi_l).
\tag{2}
$$



Each `Q_sigma` is monic of degree `m_sigma`. Neither is replaced
by the product over the other channel or by a common continuum
approximation.

## 2. An exact vanishing-module basis and its triangular high block

The rows `R_0,...,R_(2n-1)` form a basis of the vector polynomials
whose two components both have degree at most `n-1`. In that space
the kernel of the selected evaluation map in (1) has the following
explicit basis:



$$
Q_0(\xi)\xi^j(1,0),\quad 0\le j<n-m_0;\qquad
Q_1(\xi)\xi^j(0,1),\quad 0\le j<n-m_1.
\tag{3}
$$



There are `n-1` vectors. This is an exact basis because vanishing
at the distinct nodes of a channel is equivalent to divisibility
of that component by its node polynomial.

Order (3) by its highest interleaved monomial index: degree `d` in
channel zero has index `2d`, and degree `d` in channel one has
index `2d+1`. These indices are exactly



$$
n+1,n+2,\ldots,2n-1.
\tag{4}
$$



For even `n=2r`, the zero-channel indices are `2r+2,2r+4,...,4r-2`
and the one-channel indices are `2r+1,2r+3,...,4r-1`. For odd
`n=2r+1`, they are `2r+2,2r+4,...,4r` and
`2r+3,2r+5,...,4r+1`. Empty ranges, including the zero-channel
range when `n=2`, cause no exception.

Express the ordered vectors (3) in the branch basis and let their
coefficient columns form



$$
Z=\begin{pmatrix}Z_L\\ Z_H\end{pmatrix},\qquad
Z_L\in\mathbb R^{(n+1)\times(n-1)},\quad
Z_H\in\mathbb R^{(n-1)\times(n-1)}.
\tag{5}
$$



Let `h_k^p` denote the determinant of the coefficient matrix of
`R_0,...,R_(k-1)` in the interleaved monomial basis. Its individual
positive diagonal entries will be denoted `ell_k`, so that



$$
\ell_{2j}=(a_1\cdots a_{2j})^{-1},\qquad
\ell_{2j+1}=(a_2\cdots a_{2j+1})^{-1},\qquad
h_k^p=\prod_{i=0}^{k-1}\ell_i.
$$



Because the coefficient transform is lower triangular, a vector
in (3) with highest index `k` has no branch coefficients above
`k`, and its coefficient at `R_k` is `1/ell_k`. Consequently



$$
\boxed{Z_H\text{ is upper triangular},\qquad
\det Z_H=\prod_{k=n+1}^{2n-1}\ell_k^{-1}
=\frac{h_{n+1}^p}{h_{2n}^p}>0.}
\tag{6}
$$



No hypothesis about the high evaluation matrix is needed for (6).
Evaluating the identities (3) gives



$$
Z_L^TY+Z_H^TY_{\rm hi}=0.
$$



Thus the old remainder matrix has the following more explicit form:



$$
\boxed{Y_{\rm hi}=-Z_H^{-T}Z_L^TY,\qquad
H=-Z_H^{-T}Z_L^TS,\qquad
A_{\rm rem}=-Z_H^{-T}Z_L^T.}
\tag{7}
$$



In particular `rank H=rank Z_L`. The invertible high triangular
block is harmless for this kernel identity, but its size cannot be
ignored in a lower bound for a row-normalized singular value.

## 3. A finite polynomial-of-Krylov formula for every column

Use the exact symmetric finite matrix `K_(2n)` from the branch
recurrence, and set



$$
v_0=e_0,\qquad v_1=e_1-se_0.
$$



The inverse-coefficient identities in
`raw_separated_channel_low_evaluation.md` imply that the coefficient
column in (5) belonging to `Q_sigma xi^j e_sigma` is exactly



$$
\boxed{Z_{\sigma,j}=Q_\sigma(K_{2n})K_{2n}^{\,j}v_\sigma.}
\tag{8}
$$



Indeed, the largest degree in this polynomial is at most `n-1`.
Starting from `e_0`, multiplication by a power of `K` reaches index
at most twice the power; starting from `e_1`, it reaches at most
twice the power plus one. All such indices are at most `2n-1`.
No path exits the finite compression, so (8) has no hidden boundary
error. The identity also includes the lower terms of each node
polynomial, by linearity.

Equations (5), (8) say that the only unknown kernel geometry is the
projection onto rows `0,...,n` of a completely specified two-channel
polynomial-of-Krylov matrix. This is stronger than defining its
entries by high polynomial remainders, but it is not a positive
Gram representation: the two columns use different polynomials
`Q_0(K)` and `Q_1(K)`, and the two seed vectors differ.

## 4. Exact complementary minors with explicit cardinal vectors

Define the actual amplitude-weighted low cardinal coefficient
vectors



$$
a_l=S^{-T}e_l\qquad(0\le l\le n).
\tag{9}
$$



These vectors are explicit without any high-row solve. In channel
`sigma_l`, form the cardinal polynomial



$$
\frac1{g_l}\frac{Q_{\sigma_l}(\xi)}
{(\xi-\xi_l)Q_{\sigma_l}'(\xi_l)},
\tag{10}
$$



set the other component to zero, and change from monomial
coefficients to the low branch coefficients. The resulting vector
is (9). The factor `1/g_l` in (10) is essential.

For a pair `0<=j<k<=n`, let `I` be its increasing complement among
the `n+1` columns. Then



$$
\boxed{
\det H[:,I]
=(-1)^{n+j+k}\frac{h_{2n}^p}{h_{n+1}^p}
\det S\;\det[Z_L,a_j,a_k].}
\tag{11}
$$



To check the sign and orientation, put `T=Z_L^T S` and `r=n-1`.
Appending `e_j^T,e_k^T` below `T` and expanding on the bottom two
rows gives



$$
\det\begin{pmatrix}T\\e_j^T\\e_k^T\end{pmatrix}
=(-1)^{j+k+1}\det T[:,I].
$$



Multiplying `[Z_L,a_j,a_k]^T` on the right by `S` yields exactly
that displayed block matrix. Finally (7) contributes
`(-1)^r/det Z_H`, giving (11). The two exponents combine as
`r+j+k+1=n+j+k`.

The common nonzero factor in (11) is independent of the deleted
pair. Thus every actual high cofactor ratio reduces to the
corresponding two-cardinal determinant. All amplitude ratios, node
Vandermondes, and branch normalizations remain accounted for.

## 5. A normalized two-dimensional determinant exactly measures the finite angle

The following construction is conditional on `rank Z_L=n-1`.
This rank is itself part of the unresolved finite problem. Let



$$
P_Z=I-Z_L(Z_L^TZ_L)^{-1}Z_L^T,\qquad
\mathscr C=S^{-1}P_ZS^{-T}.
\tag{12}
$$



Then `P_Z` is an orthogonal projector of rank two. The matrix
`mathscr C` is positive semidefinite of rank two and its image is
exactly `ker H`, by (7). In particular its entries are



$$
\mathscr C_{jk}=a_j^TP_Za_k.
\tag{13}
$$



The Gram determinant and its Schur complement give



$$
\det[Z_L,a_j,a_k]^2
=\det(Z_L^TZ_L)\det\mathscr C[\{j,k\},\{j,k\}].
\tag{14}
$$



Let `T_*={n-1,n}` and define



$$
\boxed{
\mathfrak d_n=
\frac{\det\mathscr C[T_*,T_*]}
{e_2(\mathscr C)},\qquad
e_2(\mathscr C)=\frac{(\operatorname{tr}\mathscr C)^2
-\operatorname{tr}(\mathscr C^2)}2>0.}
\tag{15}
$$



This is a normalized two-dimensional determinant. Equivalently,
choose any orthonormal columns `V` spanning `ker Z_L^T`, and put
`N=S^{-1}V`. Then



$$
\mathfrak d_n=
\frac{\det(N[T_*,:])^2}{\det(N^TN)}.
\tag{16}
$$



Changing `V` changes neither expression. In particular (16) does
not rely on an arbitrary normalization of the two-dimensional
kernel. If `O=N(N^TN)^(-1/2)`, then `O` is an orthonormal basis
of `ker H`, and `mathfrak d_n=det(O[T_*,:])^2`. Therefore, if
`theta_1,theta_2` are its two principal angles to the last two
coordinate directions,



$$
\boxed{\mathfrak d_n=\cos^2\theta_1\cos^2\theta_2.}
\tag{17}
$$



Consequently, for `0<=epsilon_n<=1`,



$$
\mathfrak d_n\ge1-\varepsilon_n^2
\quad\Longrightarrow\quad
\|\Pi_{0,\ldots,n-2}|_{\ker H}\|\le\varepsilon_n.
\tag{18}
$$



Conversely, that projection bound implies
`mathfrak d_n >= (1-epsilon_n^2)^2`. An eventual lower bound
`mathfrak d_n >= 1-C/n^2` would prove the finite `O(1/n)`
top-two angle target. The weaker
`1-mathfrak d_n=o(log n/n)` would give the correspondingly weaker
angle scale needed in the current spectral route.

For comparison with the older graph criterion, (11), (14), and
Cauchy--Binet also give



$$
\mathfrak d_n
=\frac{\det H[:,0,\ldots,n-2]^2}{\det(HH^T)}.
\tag{19}
$$



Equation (19) alone is the old cofactor geometry. What is added here
is the explicit representation (8)--(16) by the two node polynomials
and the cardinal polynomials (10). The inverse `Z_L^T Z_L` inside
(12) is still of growing size. Writing a two-by-two determinant
does not constitute a bound for this inverse or prove its rank.

## 6. A boundary-only Gram representation with displacement rank at most eight

There is another exact way to construct the matrix entering (19)
without summing all high rows. Use the boundary matrices `E_N`,
`P_N`, and `Gamma_N` from
`raw_branch_matrix_christoffel_darboux.md`, and write



$$
\mathcal W_N(x,y)=E_N(x)^T\Gamma_NP_N(y)
-P_N(x)^T\Gamma_N^TE_N(y).
$$



For distinct actual nodes, the amplitude-weighted high column Gram
`G=H^T H` has entries



$$
\boxed{
G_{ij}=g_ig_j\,e_{\sigma_i}^T
\frac{\mathcal W_{2n}(\xi_i,\xi_j)
-\mathcal W_{n+1}(\xi_i,\xi_j)}{\xi_j-\xi_i}
e_{\sigma_j}\quad(i\ne j).}
\tag{20}
$$



On the diagonal the quotient is replaced by the derivative in its
second variable. This follows from the exact Green identity over
the interval `n+1,...,2n-1`; the two cuts are precisely `n+1`
and `2n`. It remains a polynomial identity at any apparent pole of
a rational transfer representation. It is safer to evaluate the
polynomial boundary rows there than to divide by a vanishing
Casoratian.

For each cut put



$$
b_{N,l}=g_lP_N(\xi_l)e_{\sigma_l},\qquad
c_{N,l}=g_l\Gamma_N^TE_N(\xi_l)e_{\sigma_l}.
$$



Let `B_N,C_N` collect these as two-by-`n+1` matrices and let
`X=diag(xi_0,...,xi_n)`. Then (20) gives



$$
\boxed{
GX-XG=C_{2n}^TB_{2n}-B_{2n}^TC_{2n}
-C_{n+1}^TB_{n+1}+B_{n+1}^TC_{n+1}.}
\tag{21}
$$



The rank of the right side is at most eight. This is a fixed-rank
displacement identity for the *prescribed high interval*, not the
positive full-low Loewner matrix. Each cut separately contributes a
positive full-low Gram kernel after division; their difference is
positive semidefinite because it is the actual high Gram. That
positivity does not lower-bound its designated nonzero eigenvalues
or any particular maximal minor.

The sharp coherent branch growth theorem supplies the size of the
boundary factors at nodes with `l` comparable to `n`. The local
complex transport theorem can supply controlled derivatives there.
Neither makes the two-cut difference in (20) entrywise diagonal or
permits replacing its mixed-node determinants by products of
one-point determinants.

## 7. A half-sized Schur-complement target retaining both parity chains

For a further concrete reduction, let `I={0,...,n-2}` and split it
into even indices `I_0` and odd indices `I_1`. Their sizes are



$$
t_0=\lceil(n-1)/2\rceil,\qquad
t_1=\lfloor(n-1)/2\rfloor.
$$



Partition the principal Gram block from (20) as



$$
G[I,I]=\begin{pmatrix}A&C\\C^T&B\end{pmatrix},
\qquad G[I,T_*]=\begin{pmatrix}F_0\\F_1\end{pmatrix}.
\tag{22}
$$



When `A>0`, set



$$
\boxed{\mathcal S=B-C^TA^{-1}C.}
\tag{23}
$$



This is a `t_1`-by-`t_1` determinant problem, about half the size of
the original `n-1` square evaluation minor. Since (22) is a Gram
matrix, `mathcal S>=0`. Its positive definiteness is equivalent to
invertibility of the full low-node block, given `A>0`.

Under this condition the actual kernel graph over `T_*` is obtained
from only two right sides:



$$
X_1=-\mathcal S^{-1}(F_1-C^TA^{-1}F_0),\qquad
X_0=-A^{-1}(F_0+CX_1).
\tag{24}
$$



The graph in spectral orthonormal coordinates is `[X_0;X_1]`, with
the low coordinates restored to their original order. All amplitude
factors in these equations are those of (20). For example, the
following are sufficient estimates, for any desired error scale
`epsilon_n`:



$$
\|A^{-1}F_0\|=O(\varepsilon_n),\qquad
\|A^{-1}C\|=O(1),\qquad
\|\mathcal S^{-1}(F_1-C^TA^{-1}F_0)\|=O(\varepsilon_n).
\tag{25}
$$



If also `B>0`, a useful dimensionless determinant is



$$
\Delta_{\rm par}=
\det\bigl(I-B^{-1/2}C^TA^{-1}CB^{-1/2}\bigr).
\tag{26}
$$



Every eigenvalue of the matrix inside (26) lies in `[0,1]`.
Therefore `Delta_par>=d_n>0` implies



$$
\mathcal S\succeq d_n B.
\tag{27}
$$



The implication follows because a product of numbers in `[0,1]`
is at most each factor. Thus (26) is a specific smaller multipoint
determinant whose quantitative lower bound controls the parity
coupling loss. Estimates for the individual parity Gram blocks
and the projected right sides in (25) remain necessary. Their
invertibility is not inferred from the single-parameter two-channel
conditioning theorem.

For `n=2`, `t_1=0`; the Schur determinant is the empty determinant
one and (24) reduces to the single `A` equation. The asymptotic
target concerns increasing `n` and needs no special use of this case.

## 8. What this reduces, and what is still missing

The unknown high-row geometry has now been isolated in three
equivalent concrete forms:

1. The low projection (8) of the two distinct node-polynomial
   Krylov families, with its exact harmless high triangular factor.
2. The normalized two-dimensional determinant (15), constructed
   from the two top cardinal vectors after removing the range of
   that projected family.
3. The half-sized Schur determinant (26), whose entries are supplied
   by the boundary-only formula (20) rather than by all high rows.

An original next intermediate theorem can therefore target (25)--(27)
or the equivalent near-one bound in (18). These are not new
kernel-only exponential estimates: they compare the exact
different-node, different-channel terms that survived the earlier
one-point transport analysis.

No such comparison is established here. The known exponential
low interpolation bound and polynomial conditioning of each
adjacent branch matrix do not control the smallest singular value
of `Z_L`, the projected cardinal determinant in (15), or the
Schur complement in (23). In particular an `O(1/n)` pointwise
off-channel transport error may accumulate and may be amplified
by the inverse of a multipoint block. Treating that inverse as
already bounded would simply assume the missing theorem.

Finally, even a successful finite angle estimate must be combined
with the separate row-normalized residual and singular-value
conditions in `raw_relative_spectral_truncation.md`. This note
makes no conclusion about the primitive denominator or the
arithmetic nature of `e+pi`.

Verification control: `check_raw_high_multipoint_reduction.py`
checks the Krylov identity, both parity index patterns, the
triangular factor, every complementary sign, the amplitude
cardinals, and the normalized determinant equality at two small
abstract sizes with deliberately artificial rational band entries
and nodes. The exact results are in
`raw_high_multipoint_reduction_checks.json`. These are algebraic
normalization controls, not additional spectral samples or
canonical Hermite--Padé degree constructions.
