> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact seed-boundary pencils and the adjacent two-branch Casoratian

Date: 2026-09-13. Original bounded continuation by audit_computations.

The inputs are `raw_boundary_free_moment_intertwiner.md`,
`raw_spectral_branch_generating_function.md`, and
`raw_branch_shifted_positivity_theorem.md`. The generic root-preservation
shortcut has already been excluded in `raw_hermite_biehler_scope.md`.
No new root diagnostic or canonical degree solve is used here.

**Proved:** each actual branch has an exact finite boundary-cofactor
pencil; this natural pencil cannot be transformed by constant strict
equivalence into a Hermitian pencil with positive semidefinite spectral
mass once its index is large enough. In contrast, the determinant of
two adjacent branch rows is exactly a characteristic polynomial of a
finite real symmetric matrix, and hence has real, weakly interlacing
zeros. These latter zeros are not the individual branch zeros.

## 1. The exact row matrices and seeds

Put (a_0=0), (a_j=j^2/\sqrt{4j^2-1}) for (j\ge1), and
(\lambda_j=j(j+1)). The symmetric five-diagonal matrix is



$$
K_{j,j}=d_j=a_j^2+a_{j+1}^2-\lambda_j,\quad
K_{j,j+1}=-a_{j+1},\quad K_{j,j+2}=a_{j+1}a_{j+2}.
\tag{1}
$$



The two polynomial solutions (p_j^{(0)},p_j^{(1)}) of
(Kp=\xi p) have seeds



$$
(p_0^{(0)},p_1^{(0)})=(1,\sqrt3/2),\qquad
(p_0^{(1)},p_1^{(1)})=(0,1).
\tag{2}
$$



The recurrence at zero and one omits negative indices. It determines
all subsequent entries because (a_{j+1}a_{j+2}>0).

The rational matrix (\mathcal K=D^{-1}KD), where
(D_{jj}=\sqrt{2j+1}), has entries



$$
\begin{aligned}
\mathcal K_{j,j+2}&=U_j=
\frac{(j+1)^2(j+2)^2}{(2j+1)(2j+3)},&
\mathcal K_{j,j+1}&=-\frac{(j+1)^2}{2j+1},\\
\mathcal K_{j,j}&=d_j,&
\mathcal K_{j,j-1}&=-\frac{j^2}{2j+1},\\
\mathcal K_{j,j-2}&=
\frac{j^2(j-1)^2}{(2j+1)(2j-1)}.
\end{aligned}
\tag{3}
$$



Its actual branches are (r^{(0)},r^{(1)}), with seeds
((1,1/2)), ((0,1)). They differ from (D^{-1}p^{(1)}) only
by the fixed factor (\sqrt3). All finite principal compressions
of (\mathcal K) and (K) therefore have the same characteristic
polynomial.

## 2. The individual branch is a nonprincipal boundary determinant

For (k\ge2), define the (k\)-by-(k) rational pencil
(\mathcal B_k^{(\sigma)}(\xi)) as follows. Its first (k-1)
rows are the rows (0,\ldots,k-2) of
(\mathcal K-\xi I), restricted to columns (0,\ldots,k-1).
Its last row is



$$
\ell_0=(-1/2,1,0,\ldots),\qquad
\ell_1=(1,0,0,\ldots),
\tag{4}
$$



respectively. Let



$$
C_k=\prod_{j=0}^{k-2}U_j
=\frac{((k-1)!)^2(k!)^2}{(2k-3)!!(2k-1)!!}>0.
\tag{5}
$$



Then the exact determinant identities, including signs, are



$$
\boxed{\det\mathcal B_k^{(0)}=-C_k r_k^{(0)},
\qquad \det\mathcal B_k^{(1)}=C_k r_k^{(1)}.}
\tag{6}
$$



To prove this, first regard the two initial coordinates (u_0,u_1)
as free. The recurrence rows (0,\ldots,k-3) successively eliminate
(u_2,\ldots,u_{k-1}), with pivots (U_0,\ldots,U_{k-3}).
Moving the first two columns to the end has even sign. The remaining
recurrence row equals (-U_{k-2}u_k), since its omitted next
coordinate is (u_k). Its two coefficients, followed by the seed
row in (4), give determinant (-U_{k-2}r_k^{(0)}) in the first
case and (+U_{k-2}r_k^{(1)}) in the second. This proves (6).
The argument includes (k=2), with an empty elimination product.

The symmetric version replaces (\mathcal K) by (K) and the
even boundary row by ((-\sqrt3/2,1,0,\ldots)). Its two
determinants are respectively



$$
-\Bigl(\prod_{j=0}^{k-2}a_{j+1}a_{j+2}\Bigr)p_k^{(0)},
\qquad
+\Bigl(\prod_{j=0}^{k-2}a_{j+1}a_{j+2}\Bigr)p_k^{(1)}.
\tag{7}
$$



The recurrence's last row is missing, and an extra condition is
imposed at the left seed. This distinction from a principal
self-adjoint compression is essential.

## 3. A family-specific obstruction to a positive self-adjoint pencil

Both pencils above have the form (A-\xi B), where



$$
B=\operatorname{diag}(1,\ldots,1,0),\qquad
\operatorname{rank}B=k-1.
\tag{8}
$$



They are regular: the proved shifted coefficient positivity makes
their branch determinants nonzero polynomials. However their degrees
satisfy



$$
\deg\det\mathcal B_k^{(0)}\le\lfloor k/2\rfloor,
\quad
\deg\det\mathcal B_k^{(1)}\le\lfloor(k-1)/2\rfloor.
\tag{9}
$$



Here is an elementary obstruction using precisely these actual
degrees and seeds. A regular Hermitian pencil (A-\xi B) of size
(k), with (B\ge0) and rank (k-1), has determinant degree
at least (k-2). Indeed a constant congruence makes



$$
B=\begin{pmatrix}I_{k-1}&0\\0&0\end{pmatrix},\qquad
A=\begin{pmatrix}M&h\\h^*&\alpha\end{pmatrix}.
$$



If (\alpha\ne0), its determinant has degree (k-1).
If (\alpha=0), its determinant is
(-h^*\operatorname{adj}(M-\xi I)h). Regularity forces
(h\ne0), and its leading coefficient is a nonzero signed
multiple of (\|h\|^2); its degree is (k-2).

Constant invertible left and right multipliers preserve both the
determinant degree and the rank of the spectral coefficient. Thus



$$
\boxed{\begin{gathered}
\mathcal B_k^{(0)},\mathcal B_k^{(1)}
\text{ have no constant strict equivalence to a Hermitian pencil}\
\text{with positive semidefinite mass for }k\ge5;\\
\text{the same obstruction already applies to }\mathcal B_4^{(1)}.
\end{gathered}}
\tag{10}
$$



In particular these pencils have no simultaneous positive definite
symmetrizing metric. Such a metric would commute with their already
symmetric spectral coefficient (B), so its product with (B)
would still be positive semidefinite, contradicting (10).

This result does not rule out a smaller self-adjoint representation
after a genuine deflation of the pencil, nor a Hermitian pencil with
indefinite mass. It does not prove nonreal zeros. It rules out the
direct positive-mass route from the exact finite boundary problem.

There is an equivalent spectral warning. In the symmetric version
put (M=K_{[0,k-2]}),
(h=(K_{j,k-1})_{0\le j\le k-2}), and let (\ell) be its
seed vector in the first (k-1) coordinates. For (k\ge3) the
last seed coordinate is zero, and the boundary determinant equals



$$
-\det(M-\xi I)\,\ell^T(M-\xi I)^{-1}h.
\tag{11}
$$



The resolvent is



$$
\ell^T(M-\xi I)^{-1}h
=\sum_{\mu\in\operatorname{spec}M}
\frac{\omega_\mu}{\mu-\xi},\qquad
\omega_\mu=\ell^TP_\mu h\in\mathbb R.
\tag{12}
$$



For the ranges in (10), the supports of (\ell) and (h) are
disjoint, so (\sum_\mu\omega_\mu=\ell^Th=0).
The rational function is not zero by (6). Its nonzero residues must
therefore include both signs. It is not the Cauchy transform of a
one-sign scalar measure, even though (M) itself is symmetric.

## 4. The adjacent two-branch determinant is a characteristic polynomial

Define the adjacent Casoratian



$$
\mathscr C_N(\xi)=
\det\begin{pmatrix}
r_N^{(0)}(\xi)&r_N^{(1)}(\xi)\\
r_{N+1}^{(0)}(\xi)&r_{N+1}^{(1)}(\xi)
\end{pmatrix}\qquad(N\ge1).
\tag{13}
$$



Then



$$
\boxed{\det(K_{[0,N-1]}-\xi I)
=C_{N+1}\mathscr C_N(\xi),\qquad
C_{N+1}=\frac{(N!)^2((N+1)!)^2}{(2N-1)!!(2N+1)!!}.}
\tag{14}
$$



For (N\ge2), eliminate the first (N-2) recurrence rows as
before. The final two truncated rows are



$$
-U_{N-2}u_N,qquad
\frac{N^2}{2N-1}u_N-U_{N-1}u_{N+1}.
$$



Their coefficient determinant is (U_{N-2}U_{N-1}) times
the determinant of the two future rows in the free seed basis.
The actual two seed columns have determinant one. Multiplying the
earlier pivots gives (14), with no additional sign. For (N=1),
the existing initial formulas give
(\mathscr C_1=1/4-3\xi/4) and (C_2=4/3), so (14)
is (1/3-\xi=(4/3)\mathscr C_1).

Equivalently, in symmetric normalization,



$$
\det(K_{[0,N-1]}-\xi I)
=\Bigl(\prod_{j=0}^{N-1}a_{j+1}a_{j+2}\Bigr)
\det\begin{pmatrix}p_N^{(0)}&p_N^{(1)}\\
p_{N+1}^{(0)}&p_{N+1}^{(1)}\end{pmatrix}.
\tag{15}
$$



The factors agree exactly after converting (p) to (r); no
radical or seed normalization is suppressed.

It follows from finite real symmetric spectral theory that every
zero of (\mathscr C_N) is real, counted with multiplicity, and
the zeros for (N) and (N+1) weakly interlace. The leading
coefficient is ((-1)^N/C_{N+1}), so its degree is exactly (N).
At least one zero is positive for every (N\ge1): the Rayleigh
quotient of the first coordinate vector is (K_{00}=1/3>0).

These are zeros of the *combined* determinant. They do not prove
negative real zeros or interlacing for either individual branch.
The actual scalar branch still uses the signed boundary expression
(11), whereas (14) imposes the two right boundary conditions
(u_N=u_{N+1}=0) and leaves both left initial coordinates free.

## 5. The useful next structure

The natural next consequence is a matrix Christoffel–Darboux identity
for the two branch columns, with both right boundary channels kept.
It can supply a positive matrix resolvent and a matrix Gram kernel.
It must not be replaced by a positive scalar measure for either
individual branch, which (12) explicitly excludes in the stated
ranges. Quantitative mixed-cofactor bounds would still need estimates
that retain the relative orientation of those two channels.

Verification: `check_raw_branch_boundary_identities.py` uses generic
symbolic band coefficients and an arbitrary even seed to check the
Casoratian signs at sizes 2 and 3 and the individual boundary signs
at sizes 3 and 4. All passed, recorded in
`raw_branch_boundary_identity_checks.json`. These are closed symbolic
normalization controls, not a root diagnostic or additional HP solve.
