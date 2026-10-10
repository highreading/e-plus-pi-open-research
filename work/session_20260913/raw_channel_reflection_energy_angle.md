> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual channel angle: subexponential reflection and an exact boundary-energy correction

Date: 2026-09-13. Original bounded continuation by audit_computations.

This note attacks the unprojected angle delta_n in
`raw_high_ratio_quasilocal_approximation.md`. It proves a
subexponential bound for the underlying *unweighted* channel
decomposition by identifying its exact involution with polynomial
reflection in the Borel–Legendre basis. For the actual F_b energy,
the remaining loss becomes an explicit positive double sum of
two-by-two boundary spectral residues. A bound for that scalar
sum would give the desired subexponential actual angle bound.

No subexponential estimate for the weighted sum is asserted here.
The original seeds and both parity factors remain unchanged.

## 1. The component involution is actual polynomial reflection

Let N=2n and use the symmetric raw basis



$$
E_k(x)=\frac{k!}{a_1\cdots a_k}\mathcal BQ_k(x),
\quad a_k=\frac{k^2}{\sqrt{4k^2-1}},\quad
Q_k(t)=\frac{i^k}{c_k}P_k(-it),\quad
c_k=2^{-k}\binom{2k}{k}.
\tag{1}
$$



Here B is the coefficient Borel transform and P_k is ordinary
Legendre. The elementary product identity
`k!/(a_1...a_k)=c_k sqrt(2k+1)` gives



$$
E_k(x)=\sqrt{2k+1}\,i^k\mathcal B[P_k(-ix)].
\tag{2}
$$



Let C_N be the coefficient matrix of reflection:



$$
E_k(1-x)=\sum_{j=0}^{N-1}(C_N)_{jk}E_j(x),
\qquad 0\le k<N.
\tag{3}
$$



It is upper triangular, real, and satisfies C_N^2=I.
The branch identity is a polynomial identity in x:



$$
E_k=p_k^{(0)}(\mathcal T)1+
p_k^{(1)}(\mathcal T)(\sqrt3x-\sqrt3/2),
\quad
\mathcal T=D x(x-1)D+x^2-x+1.
\tag{4}
$$



To prove (4), the two initial rows give E_0 and E_1, and the
same nonzero-pivot five-term recurrence then gives every row.
Reflection commutes with T; its two initial functions in (4)
have signs + and −. Consequently C_N acts on a coefficient
vector whose branch polynomial is `(f_0,f_1)` by replacing it
with `(f_0,-f_1)`.

In particular the actual full vanishing spaces



$$
Z_\sigma=\operatorname{span}
\{Q_\sigma(K_N)K_N^jv_\sigma:0\le j<n-m_\sigma\},
\quad v_0=e_0,\quad v_1=e_1-(\sqrt3/2)e_0
\tag{5}
$$



are respectively + and − eigenspaces of C_N, restricted to
their displayed dimensions. All polynomial paths in (5) stay
below N, since the component degrees are below n. This uses
the original parity node polynomials Q_sigma, not a common
polynomial or a changed seed.

## 2. A subexponential bound for the finite reflection matrix

The following explicit estimate holds for every N>=6:



$$
\boxed{\|C_N\|\le 6N\exp(2\sqrt{3N}).}
\tag{6}
$$



Here is a proof that does not estimate translation by the
exponential of a crude derivative-matrix norm.

For a coefficient vector c, put
`p(t)=sum_(k<N)c_k sqrt(2k+1)i^k P_k(t)`. This is an
isometry from Euclidean coefficient space onto polynomials
of degree below N in `L2([-1,1],dt/2)`. The corresponding
raw polynomial is `B[p(-ix)]`. Define the backward divided
difference on that finite polynomial space by



$$
Tp(t)=\frac{p(t)-p(0)}t.
$$



Differentiation in x corresponds exactly to −iT. Reflection
is ordinary parity composed with translation by one; parity
is unitary in the Legendre coefficient norm. It is therefore
enough to bound `exp(-iT)`.

The finite generating identity



$$
G_s p(t):=\sum_{j=0}^{N-1}s^jT^jp(t)
=\frac{tp(t)-sp(s)}{t-s}
\tag{7}
$$



holds also at t=s by its removable value. For `|s|=r<=1/4`,
we claim



$$
\|G_s p\|_2\le6N e^{3Nr}\|p\|_2.
\tag{8}
$$



The standard polynomial integral formula
`P_k(z)=pi^(-1) integral_0^pi (z+sqrt(z^2-1)cos u)^k du`
gives `|P_k(z)|<=exp(k|z|)`: use
`|sqrt(z^2-1)|<=sqrt(1+|z|^2)` and
`|z|+sqrt(1+|z|^2)=exp(asinh|z|)<=exp|z|`.
The formula itself follows by summing in k near zero and
integrating the geometric series to obtain the Legendre
generating function; the resulting coefficient identities
are polynomials, so hold for all complex z. Thus no choice
of the square root affects the formula.

Since `sum_(k<N)(2k+1)=N^2`, Cauchy–Schwarz gives
`|p(z)|<=N exp(N|z|)||p||_2`. For real `|t|>=2r`, (7)
therefore has absolute value at most
`2|p(t)|+|p(s)|`. For real `|t|<=2r`, regard (7) as a
divided difference of `h(z)=zp(z)`. On the disk `|z|<=2r`,
Cauchy's derivative bound from disks of radius r gives
`|p'(z)|<=(N/r)e^(3Nr)||p||_2`. The straight segment from
s to t lies in that disk, so
`|G_s p(t)|<=3N e^(3Nr)||p||_2`. Combining the two real
regions in L2 proves the slightly loose constant (8).

The exact finite-dimensional Cauchy formula is



$$
e^{-iT}p=\frac1{2\pi i}\int_{|s|=r}
e^{-i/s}G_s p\,\frac{ds}{s}.
\tag{9}
$$



Taking its residue at zero gives precisely `sum (-iT)^j/j!`.
Equations (8)-(9) bound its norm by
`6N exp(1/r+3Nr)`. Choosing `r=(3N)^(-1/2)`, admissible
for N>=6, proves (6).

In particular this estimate includes the actual seed offset:
it was derived from (2)-(4), rather than from an invented
orthogonal parity decomposition of the raw coordinate basis.

## 3. What (6) proves for angles before energy weighting

For two disjoint subspaces on which an involution J acts
respectively by +1 and −1, let c be their largest principal-
angle cosine. The norm of J on their sum is exactly



$$
\|J\|^2=\frac{1+c}{1-c}.
\tag{10}
$$



One proof uses a principal pair of unit vectors with inner
product c. In its orthonormal two-dimensional coordinates J
has matrix `[[1,-2c/sqrt(1-c^2)],[0,-1]]`; its largest
singular value is `sqrt((1+c)/(1-c))`. Orthogonal direct
sums over principal pairs give (10); unmatched directions
contribute norm one. Empty-channel cases are immediate.

If each space is separately orthonormalized, the smallest
singular value of their juxtaposition is sqrt(1-c). Applied
to the actual unweighted spaces (5), (6) therefore gives



$$
\delta_n^{\rm unweighted}
\ge\sqrt{\frac2{1+\|C_N\|^2}}
\ge\frac1{6N}e^{-2\sqrt{3N}}.
\tag{11}
$$



This is a genuine all-index subexponential channel-angle
bound, but its norm is not yet the F_b energy norm required
by the ratio-localization note.

## 4. The exact involution for the actual energy angle

Use the actual low/high split from that note and write
`F=F_b(K_N)>0`. Its two energy-normalized spaces are



$$
F^{1/2}R(K_N)W_a=F^{-1/2}Z_a,
\qquad F^{1/2}W_b=F^{-1/2}Z_b,
\tag{12}
$$



up to the already fixed channel signs. The identities follow
from `Z_a=F_a(K_N)W_a`, `Z_b=F_b(K_N)W_b`; they preserve
the original factors and seeds exactly. Hence the relevant
involution on their sum is the restriction of



$$
J_F=F^{-1/2}C_NF^{1/2}.
\tag{13}
$$



Writing `S=F^(-1/2)(Z_a+Z_b)`, its exact relation to the
delta_n in the ratio note is



$$
\boxed{\delta_n^2=
\frac2{1+\|J_F|_S\|^2}
\ge\frac2{1+\|J_F\|^2}.}
\tag{14}
$$



The use of F^(-1/2), rather than F^(1/2), is essential:
the spaces in the old notation are F^(1/2)[R W_a,W_b],
whereas the reflection eigenspaces are the full Z spaces.

## 5. The finite failure of commutation is an actual rank-two boundary term

Let iota_N inject into the last two coordinates, and put



$$
\Gamma_N=\begin{pmatrix}
a_{N-1}a_N&0\\-a_N&a_Na_{N+1}
\end{pmatrix},\qquad
U_N=C_{N+2}[0{:}N-1,\{N,N+1\}].
\tag{15}
$$



Thus U_N consists of the first N coefficients of the two
actual reflected polynomials E_N(1-x), E_(N+1)(1-x).
The exact commutator is



$$
\boxed{K_NC_N-C_NK_N=U_N\Gamma_N^T\iota_N^T.}
\tag{16}
$$



For clarity, this follows by first using the infinite
polynomial-coefficient identity KC=CK. It is legitimate on
each finite coefficient vector since all columns involved
have finite support. If P is the first-N projection, then
`(I-P)CP=0` by triangularity, whereas `(I-P)KP` occupies
exactly the next two coordinates and equals
`iota_out Gamma_N^T iota_N^T`. Taking the first N rows of
the commutation identity gives (16), with the displayed
positive sign. No infinite Hilbert-space realization of K
or C is needed.

In particular (6) gives the explicit bound
`||U_N||<=6(N+2)exp(2sqrt(3(N+2)))`. The boundary matrix
has norm O(N^2). However the rank-two identity alone does
not make C_N commute with F_b(K_N).

## 6. An exact positive scalar boundary-residue target

Let Pi_lambda be the orthogonal spectral projections of the
actual finite K_N. Repeated eigenvalues are permitted. For
its scalar polynomial `F(t)=product_i(beta_i-t)>0` on the
row spectrum, define the continuous divided-ratio kernel



$$
\psi_F(\lambda,\mu)=
\frac{\sqrt{F(\mu)/F(\lambda)}-1}{\lambda-\mu},
\quad
\psi_F(\lambda,\lambda)
=-\frac{F'(\lambda)}{2F(\lambda)}.
\tag{17}
$$



It is positive on the whole real spectral square when high
factors are present, and zero for the empty product F=1.
Let the two positive two-by-two residue matrices be



$$
A_\lambda=U_N^T\Pi_\lambda U_N,\qquad
B_\mu=\Gamma_N^T\iota_N^T\Pi_\mu\iota_N\Gamma_N.
\tag{18}
$$



The B_mu are precisely the positive residues of the already
proved boundary Weyl matrix M_N(z). The A_lambda are the
residues of the other explicit two-column boundary resolvent
`U_N^T(zI-K_N)^(-1)U_N`. Define one nonnegative scalar



$$
\boxed{\Theta_N^2=
\sum_{\lambda,\mu\in\operatorname{spec}K_N}
\psi_F(\lambda,\mu)^2
\operatorname{tr}(A_\lambda B_\mu).}
\tag{19}
$$



This sum is the exact norm identity



$$
\boxed{\Theta_N=\|F^{-1/2}C_NF^{1/2}-C_N\|_{\rm HS}.}
\tag{20}
$$



Indeed, for distinct eigenvalues, the (lambda,mu) block
of (16) is `(lambda-mu) Pi_lambda C_N Pi_mu`.
Multiplying by (17) gives the same block of `J_F-C_N`.
For equal eigenvalues both commutator and difference blocks
are zero, including every block of a multiple eigenspace.
The squared Hilbert–Schmidt norm of
`Pi_lambda U_N Gamma_N^T iota_N^T Pi_mu` is exactly
`tr(A_lambda B_mu)`. Orthogonality of the spectral blocks
then proves (20). In particular diagonal terms in (19)
are zero, and no unproved simple-spectrum hypothesis or
inverse eigenvalue-gap bound is used.

Combining (6), (14), and (20) proves the concrete estimate



$$
\boxed{\delta_n\ge
\left\{\frac2{1+
[6N e^{2\sqrt{3N}}+\Theta_N]^2}\right\}^{1/2},
\qquad N=2n\ge6.}
\tag{21}
$$



Thus `log(1+Theta_(2n))=o(n)` is a specific sufficient
scalar estimate for a subexponential bound on the actual
energy angle. A bound `Theta_(2n)<=exp(O(sqrt(n)log n))`
would give that same useful scale for `1/delta_n`.
This is stronger than merely specifying an abstract Gram
determinant: every ingredient is an explicit actual
two-column boundary residue and the prescribed high roots.

## 7. What elementary bounds still lose

The mean value theorem applied to sqrt(F) gives



$$
\sup_{\lambda,\mu}\psi_F(\lambda,\mu)
\le\frac12\sqrt{\operatorname{cond}F(K_N)}
\sum_i\frac1{\beta_i-M_n},\qquad M_n=2n+3/4.
\tag{22}
$$



For the cutoff b=ceil(2sqrt n), eventually b<n. The actual
node bound gives `beta_i-M_n>=l_i^2/2` for every retained
high node, and consequently the final sum is at most `2/b`.
The same estimates give



$$
\operatorname{cond}F(K_N)
\le\prod_{l=1}^n\left(1+\frac{12n^2}{l^2}\right)
\le\exp[(\log13+2)n].
\tag{23}
$$



For the last inequality use `1+12(n/l)^2<=13(n/l)^2`
and `n!>=(n/e)^n`. The product over all l only enlarges
the product over the actual retained high list.

Equations (19), (22) and the Hilbert–Schmidt norm of (16)
then give only an exponential upper bound for Theta_N.
The new subexponential estimate (6) therefore does not by
itself prove a subexponential energy-angle bound. What is
missing is control of the actual boundary spectral weight
in (19) when the divided-ratio kernel is large. The previously
proved positive-parameter boundary resolvent estimates do
not immediately provide that weighted two-parameter sum.

The exact obstruction is now localized: unweighted component
reflection has only subexponential norm, and all additional
loss is the positive boundary correction (19). Proving a
subexponential bound for that correction, or only for its
restriction to the actual vanishing sum in (14), would make
the ratio-localization rank reduction effective after
reoptimizing the low cutoff. No such bound, complete high-
matrix rank theorem, endpoint angle, or irrationality result
is claimed here.

Closed normalization controls: `check_raw_channel_reflection_boundary.py`
checks only N=2,3, using the actual raw basis. Reflection squared,
the sign and orientation of the rank-two commutator, and the
`exp(-iT)` translation identity all pass exactly. Outputs are in
`raw_channel_reflection_boundary_checks.json`. These controls do
not replace the all-degree proofs or estimate the weighted sum.
