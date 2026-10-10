> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A boundary-free moment intertwiner, a spectral gap, and two parity branches

Date: 2026-09-13. Original bounded continuation by audit_results.

**Proved here:** a second-order, boundary-free self-adjoint combination
of the actual Borel–Legendre operators; an exact five-diagonal moment
intertwining relation; a uniform upper bound on its finite row blocks;
a separated Sylvester resolvent with an explicit gap; and a rigorous
infinite spectral representation whose columns satisfy an order-four
recurrence with one nonzero initial amplitude on each parity branch.

These statements do not prove the top-two nullspace concentration bound,
an endpoint cofactor estimate, or a bound on the primitive denominator.
The remaining boundary forcing is kept explicitly.

## 1. Existing inputs and the new cancellation

Use the actual F_k from raw_borel_legendre_literature.md, with leading
coefficient 1/k!, and put lambda_k=k(k+1). The previously proved
operators and ladder are



$$
\mathcal J=xD^2+D+x,
\qquad \mathscr L=D^2x^2D^2+Dx^2D,
$$




$$
\mathscr LF_k=\lambda_kF_k,\qquad
\mathcal JF_k=(k+1)F_{k+1}+k\beta_kF_{k-1},
\quad \beta_k=\frac{k^2}{4k^2-1}.
\tag{1}
$$



At k=0 the second summand is absent. Direct composition gives



$$
\mathcal J^2=
x^2D^4+4xD^3+(2x^2+2)D^2+4xD+x^2+1.
$$



Consequently the new combination is only second order:



$$
\boxed{
\mathcal T:=\mathcal J^2-\mathcal J-\mathscr L
=D\,x(x-1)D+(x^2-x+1).}
\tag{2}
$$



For arbitrary polynomials f,g,



$$
\langle f,\mathcal Tg\rangle-\langle\mathcal Tf,g\rangle
=[x(x-1)(fg'-f'g)]_0^1=0.
\tag{3}
$$



Thus the boundary jets that obstruct the separate J ladder cancel
exactly. This is not obtained by imposing extra endpoint conditions
on F_k or the selected approximation polynomial.

## 2. Explicit row and column coefficients

In the original normalization, (1) and (2) give for all k>=0



$$
\begin{aligned}
\mathcal TF_k={}&(k+1)(k+2)F_{k+2}-(k+1)F_{k+1}\\
&+[(k+1)^2\beta_{k+1}+k^2\beta_k-\lambda_k]F_k\\
&-k\beta_kF_{k-1}
+k(k-1)\beta_k\beta_{k-1}F_{k-2},
\end{aligned}
\tag{4}
$$



with all negative-index terms omitted.

To make this row matrix symmetric, define



$$
a_0=0,\quad a_k=\frac{k^2}{\sqrt{4k^2-1}}\ (k\ge1),
\qquad E_k=\frac{k!F_k}{a_1\cdots a_k}.
\tag{5}
$$



The empty product is1. The ladder becomes



$$
\mathcal JE_k=a_{k+1}E_{k+1}+a_kE_{k-1}.
$$



Let J be this symmetric Jacobi matrix and Lambda=diag(lambda_k).
The symmetric row matrix K of T is therefore



$$
K=J^2-J-\Lambda,
\tag{6}
$$



with coefficients



$$
\begin{array}{ll}
K_{k,k}=a_k^2+a_{k+1}^2-\lambda_k,&
K_{k,k+1}=-a_{k+1},\\
K_{k,k+2}=a_{k+1}a_{k+2},&K_{j,k}=K_{k,j}.
\end{array}
\tag{7}
$$



Equation (6) initially denotes a banded matrix identity on finitely
supported sequences; no self-adjoint realization of this row matrix
on unweighted sequence space is assumed.

On the column side use the orthonormal shifted Legendre basis
phi_l=sqrt(2l+1)P_l(2x-1). Set



$$
t_l=\frac{l+1}{2\sqrt{(2l+1)(2l+3)}},\quad t_{-1}=0.
$$



Multiplication by x-1/2 has off-diagonal coefficients t_l. Hence the
column matrix of T is



$$
\boxed{S=\Lambda+\tfrac34 I+X^2,}
\tag{8}
$$



where X represents multiplication by x-1/2. Explicitly



$$
S_{l,l}=\lambda_l+\tfrac34+t_{l-1}^2+t_l^2,
\qquad S_{l,l+2}=t_lt_{l+1},
\qquad S_{l,l+1}=0.
\tag{9}
$$



Thus the column matrix splits into two parity blocks. Its quadratic
potential satisfies 3/4<=x^2-x+1<=1 on [0,1].

## 3. Exact moment displacement and all truncation terms

Define the scaled actual moments



$$
\mathsf M_{k,l}=\langle E_k,\phi_l\rangle.
$$



Equations (3),(7),(9) give the entrywise, finite-sum identity



$$
\boxed{K\mathsf M=\mathsf M S.}
\tag{10}
$$



Every individual entry uses only indices at distance at most2; no
convergence of an infinite matrix product is needed for (10).

Let I=[a,b] and Jc=[m,N] be finite index intervals (the notation Jc
here is an interval, not the differential operator). Write
M=mathsf M_(I,Jc), K_I=K_(I,I), S_Jc=S_(Jc,Jc). Then



$$
\boxed{
M S_{Jc}-K_I M
=K_{I,I^c}\mathsf M_{I^c,Jc}
-\mathsf M_{I,Jc^c}S_{Jc^c,Jc}=:\mathcal E.}
\tag{11}
$$



The first term uses only the four exterior row indices
a-2,a-1,b+1,b+2, omitting negative indices. It is supported on the
first two and last two rows of I. The second term uses only exterior
column indices m-2,m-1,N+1,N+2 and is supported on the first two and
last two columns. Therefore rank E<=8, and rank E<=6 when m=0.
This rank is a bound on displacement, not a claim that the full
moment matrix is a bounded-rank perturbation.

For example, when b=2n-1 the two upper exterior row channels include
coefficients a_(2n-1)a_(2n) and a_(2n)a_(2n+1), both of order n^2.
They cannot be discarded. Because S has only distance-two off-diagonals,
its cross-boundary block has at most one nonzero entry in each exterior
row and at most two in each interior column. Hence for every interval



$$
\|S_{Jc^c,Jc}\|\le\sqrt2\sup_l t_lt_{l+1}
=\frac1{3\sqrt{10}}.
\tag{12}
$$



When the interval has length at least4, its first two and last two
columns are disjoint, and the sharper bound 1/(6sqrt5)<1/12 holds.
The exact supremum follows from
t_l^2=1/16+1/[16(2l+1)(2l+3)], which is decreasing. The row boundary
block instead has norm O(b^2). Root's independent review caught the
short-interval distinction; it has no effect on the spectral gap.

## 4. A uniform upper bound for the row block

The following estimates concern finite vectors, so they do not depend
on a choice of domain for the unbounded Jacobi matrix J:



$$
\boxed{J^2-\Lambda\le\tfrac98 I,\qquad
K_{[a,b]}\le(b+\tfrac74)I.}
\tag{13}
$$



Here the first inequality is a quadratic-form inequality on every
finitely supported vector. The compression of J^2 includes the
paths leaving the interval and returning to it; it is not replaced
by the square of a truncated J.

**Proof.** For k>=1,



$$
a_k\le\frac k2+\frac1{12k}.
\tag{14}
$$



Indeed, with u=1/(4k^2)<=1/4, the elementary inequality
(1-u)^(-1/2)<=1+2u/3 follows by squaring: the difference from1 is
u[1/3-8u/9-4u^2/9]>=u/12.

The absolute row-sum upper bound for J^2-Lambda is



$$
r_k=a_k^2+a_{k+1}^2+a_ka_{k-1}+a_{k+1}a_{k+2}
-k(k+1).
$$



For k>=2, (14) gives



$$
r_k\le\frac34+\frac16
+\frac{5/2+25/12}{24}
+\frac{1/4+1/9+1/2+1/12}{144}
=\frac{361}{324}<\frac98.
\tag{15}
$$



The bounds on the two cross ratios use
k/(k-1)+(k-1)/k<=5/2 and
(k+1)/(k+2)+(k+2)/(k+1)<=25/12.
For the two remaining rows,



$$
r_0=\frac13+\frac4{\sqrt{45}}<1,
\qquad r_1=-\frac35+\frac{36}{\sqrt{525}}<1.
$$



For instance sqrt5>2 and sqrt525>45/2 suffice. Bounding each off-diagonal
quadratic term by the sum of the corresponding diagonal squares
proves the first inequality in (13).

Also (14) implies a_k+a_(k+1)<=k+5/8 for k>=1, and a_1<5/8 handles
k=0. The norm of the truncated J is at most b+5/8. Subtracting that
truncated J from the compressed first operator proves the second
inequality in (13).

## 5. The separated Sylvester resolvent and its sign

The variational bound on (8) gives



$$
S_{[m,N]}\ge[m(m+1)+\tfrac34]I.
$$



For the actual high row block I=[n+1,2n-1], (13) gives
K_I<=(2n+3/4)I. Therefore, whenever



$$
g_{n,m}:=m(m+1)-2n>0,
\tag{16}
$$



the spectra in (11) are separated by at least g_(n,m), and



$$
\boxed{
M=\int_0^\infty e^{tK_I}\mathcal E e^{-tS_{Jc}}dt,
\qquad \|M\|\le\frac{\|\mathcal E\|}{g_{n,m}}.}
\tag{17}
$$



Differentiating the integrand proves the Sylvester equation, while
the spectral gap proves convergence and uniqueness. The same bound
holds in Frobenius norm. For m comparable to n the gap is of order
n^2, rather than merely a formal eigenvalue difference.

There is a further exact positivity statement about this inverse.
Conjugate K by diag((-1)^k): both its distance-one and distance-two
off-diagonals become nonnegative. Conjugate S by
diag((-1)^(floor(l/2))): its distance-two off-diagonals become
nonpositive. After these two sign changes, the matrix of
X -> X S-K X is a positive-definite symmetric matrix with nonpositive
off-diagonal entries. Its inverse is entrywise nonnegative. One proof
chooses c at least its largest eigenvalue and diagonal entry, then
expands the inverse as c^(-1)sum_(r>=0)(I-A/c)^r; every summand is
entrywise nonnegative and the spectral radius is less than1.

This is positivity of a separated resolvent. The transformed forcing
in (11) need not have one sign, so it supplies no unproved sign pattern
for the actual moments or their maximal minors.

The limitation of (17) is concrete: the row boundary coefficients
are of order n^2, the same scale as the useful gap. An absolute bound
on them gives an order-one feedback, not an O(1/n) graph bound or a
strict contraction. A coherent estimate of the four exterior moment
channels is still required. Moreover the full low column block
[0,n-2] has small eigenvalues and is not separated by (16).

## 6. A genuine self-adjoint realization and its complete eigenbasis

The preceding identities were finite. To justify an infinite spectral
expansion, define a specific operator on L2(0,1), rather than assume
one from formal symmetry alone.

Let A0 be the self-adjoint diagonal operator in the complete Legendre
basis phi_l, with eigenvalues lambda_l and domain



$$
\mathcal D(A_0)=\left\{f:\sum_l\lambda_l^2
|\langle f,\phi_l\rangle|^2<\infty\right\}.
$$



On polynomials A0=D x(x-1)D. Its resolvent is compact, since the
diagonal resolvent entries tend to0. Multiplication by
V=x^2-x+1 is bounded and self-adjoint. Thus



$$
T=A_0+V,\qquad\mathcal D(T)=\mathcal D(A_0)
\tag{18}
$$



is self-adjoint and has compact resolvent. The resolvent identity
preserves compactness, and the spectral theorem supplies a complete
orthonormal eigenbasis. This selects the natural Legendre realization;
no unproved common boundary condition for the fourth-order operator
mathscr L is being used. Every polynomial, in particular every E_k,
lies in this domain, and (2) agrees with (18) there.

Write its ordered eigenpairs as T psi_l=xi_l psi_l. The min-max
principle and 3/4<=V<=1 give



$$
\boxed{\lambda_l+\tfrac34\le\xi_l\le\lambda_l+1.}
\tag{19}
$$



These disjoint intervals prove that all eigenvalues are simple.
Reflection x -> 1-x commutes with T. Applying the same min-max bounds
on the two reflection-parity subspaces shows that psi_l has parity
(-1)^l; the separated even and odd intervals have their original
alternating order.

One also gets an explicit high-mode perturbation estimate. Write
T=A0+7/8+W, with ||W||<=1/8. Project the eigenvalue equation off phi_l.
For l>=1 the other diagonal eigenvalues are at distance at least
2l-1/8. Consequently



$$
\|(I-|\phi_l\rangle\langle\phi_l|)\psi_l\|_2
\le\frac1{16l-1}.
\tag{20}
$$



Choosing the eigenfunction's phase to make its phi_l coefficient
nonnegative gives ||psi_l-phi_l||<=sqrt2/(16l-1). This is an
eigenfunction estimate, not a proved concentration statement about
the actual HP nullspace.

There is also a uniform projection estimate that avoids summing the
individual eigenfunction errors. Let P_<=d project onto phi_0,...,phi_d,
and let Q_<=d project onto psi_0,...,psi_d. Then



$$
\boxed{\|P_{\le d}-Q_{\le d}\|
\le\frac1{16d+15}\qquad(d\ge0).}
\tag{20a}
$$



To prove it, subtract 7/8 from T and write T'=A0+W, ||W||<=1/8.
For X=(I-P_<=d)Q_<=d, regarded as a map from the low T' subspace
into the high A0 subspace, the exact equation is



$$
A_{0,\mathrm{hi}}X-XT'_{\mathrm{lo}}
=-(I-P_{\le d})WQ_{\le d}.
$$



The gap is at least lambda_(d+1)-lambda_d-1/8=2d+15/8.
The same separated semigroup integral as in (17), now with one
bounded-below unbounded diagonal operator, converges in operator norm
and bounds X by (1/8)/(2d+15/8). Equivalently its columns can first be
expanded in the complete A0 basis; uniqueness follows from separation.
Interchanging A0 and T' gives the identical bound on
(I-Q_<=d)P_<=d. The norm of the difference of two orthogonal projections
is the maximum of these two cross-projection norms, proving (20a).

For a polynomial P of degree at most n this gives



$$
\|(I-Q_{\le n})P\|\le\frac{\|P\|}{16n+15},
$$




$$
\big|\|P_{\le n-2}P\|-\|Q_{\le n-2}P\|\big|
\le\frac{\|P\|}{16n-17}\qquad(n\ge2).
\tag{20b}
$$



Thus the Legendre top-two concentration target and its T spectral
counterpart differ by a rigorously controlled O(1/n) error. This also
applies to any weaker target whose scale dominates 1/n. It still
does not authorize dropping the high spectral tail from a moment
identity when the test functions have growing norms.

## 7. An order-four spectral recurrence with two parity branches

Define u_k(l)=<E_k,psi_l>. Since E_k is in the domain of the
self-adjoint T, (7) and (18) give, without any boundary limit,



$$
\begin{aligned}
\xi_lu_k={}&a_{k+1}a_{k+2}u_{k+2}-a_{k+1}u_{k+1}\\
&+(a_k^2+a_{k+1}^2-\lambda_k)u_k
-a_ku_{k-1}+a_ka_{k-1}u_{k-2}.
\end{aligned}
\tag{21}
$$



Negative-index terms are omitted. Because the leading coefficient
a_(k+1)a_(k+2) is always nonzero, the k=0 equation determines u_2
from u_0,u_1; the subsequent equations determine the entire sequence.
Thus u_k is a polynomial in the spectral parameter xi_l times these
two initial amplitudes. This is a fixed-order recurrence in the row
index k, not yet a scalar recurrence for the balanced-index cofactors.

Here E_0=1 and E_1=sqrt3 x. Reflection parity gives



$$
\begin{array}{c|cc}
&u_0&u_1\\ \hline
l\text{ even}&g_l&(\sqrt3/2)g_l\\
l\text{ odd}&0&g_l .
\end{array}
\tag{22}
$$



Every displayed amplitude g_l is nonzero. For even l, g_l is the
phi_0 coefficient of psi_l. In the even block of (9), all consecutive
distance-two coefficients t_j t_(j+1) are strictly positive. If that
initial coefficient vanished, the first eigenvector equation would
force the next to vanish, and induction would force the whole
eigenvector to be zero. For odd l, u_1 is one half the phi_1 coefficient
because sqrt3 x=(sqrt3/2)phi_0+(1/2)phi_1; the identical induction in
the odd block proves its nonvanishing.

Equations (21),(22) therefore define two explicit polynomial solution
branches p_k^(0)(xi), p_k^(1)(xi), with initial values
(1,sqrt3/2) and (0,1), respectively, such that



$$
\boxed{\langle E_k,\psi_l\rangle
=g_l p_k^{(l\bmod2)}(\xi_l).}
\tag{23}
$$



No four endpoint-jet observations remain in this representation.
For any polynomial P, completeness and Cauchy–Schwarz justify



$$
\langle P,E_k\rangle
=\sum_{l=0}^\infty
\langle P,\psi_l\rangle\,
g_l p_k^{(l\bmod2)}(\xi_l),
\tag{24}
$$



with absolute convergence for every fixed k. Indeed both coefficient
sequences are square summable, being the spectral coefficients of
the two L2 functions P and E_k. No uniform interchange in growing
k or n is asserted.

The actual high orthogonalities are exactly the vanishing of (24)
for k=n+1,...,2n-1. This is a concrete two-branch spectral interpolation
formulation with positive squared amplitudes in the associated Gram
representation. It does not make all its mixed determinants positive.

## 8. The next missing estimate

The useful new relation is (11), and the useful new spectral gap is
(16). A route to the top-two graph estimate would now need a
quantitative estimate of the coherent four row-boundary channels,
or a uniform interpolation/cofactor estimate for the two polynomial
branches in (23) at the actual nodes xi_l with their actual weights.
The fixed recurrence order alone does not imply a fixed-order
balanced-n recurrence: that operation deletes one high row, adds two,
and changes the degree-constrained input space.

The O(1/l) change from Legendre eigenfunctions to psi_l is controlled,
but polynomial degree truncation is not exact in the psi basis.
Truncating (24) because P has degree at most n would therefore be
incorrect. Nor does (19) give the initial amplitudes g_l or their
relative size. Those are precise further data the spectral route
must control before claiming a uniform nullspace-angle bound.

## 9. Verification scope

check_raw_boundary_free_intertwiner.py verifies the formal operator
identity on an arbitrary symbolic function, five predeclared exact
moment pairs (0,0),(1,2),(4,3),(5,4),(7,5), and the rational constant
in the uniform row-bound proof. All passed and are recorded in
raw_boundary_free_intertwiner_checks.json. No canonical HP triple,
new integer-relation search, or increasing degree scan was constructed.

The domain, completeness, spectral bounds, parity, and amplitude
nonvanishing claims above are analytic proofs, not consequences of
those finite controls.

Independent review: root checked the operator identity, row-bound
constants, gap, self-adjoint realization, eigenbasis and initial
amplitude arguments. The one requested correction concerned the
short-column-interval factor sqrt2 in (12), now included. The later
uniform projection addendum has been sent for separate review.

## 10. Exact identification with fixed-parameter prolate spheroidal functions

Put u=2x-1 and y_l(u)=psi_l((u+1)/2)/sqrt2, so ||y_l||_(L2(-1,1))=1.
The eigenvalue equation becomes



$$
\left[-D_u(1-u^2)D_u+\frac{u^2}{4}\right]y_l
=(\xi_l-\tfrac34)y_l.
\tag{25}
$$



This is the classical order-zero prolate spheroidal equation with
fixed bandlimit c=1/2. In the convention of
[DLMF30.2.1](https://dlmf.nist.gov/30.2.E1), gamma^2=1/4, mu=0,
and lambda_DLMF=xi_l-1; the usual chi parameter equals xi_l-3/4.
The distinction between the two eigenvalue shifts is essential.
Thus the spectral basis above is an established special-function
family, identified here by an exact transformation.

The finite Fourier relation is classical; it is stated, with an
explicit normalization, in
[DLMF30.15.5](https://dlmf.nist.gov/30.15.E5), and its original setting
is [Slepian–Pollak, Part I (1961)](https://www.math.ucdavis.edu/~saito/data/ONR15/PSWF-I.pdf).
For our purposes one can justify precisely the needed relation
directly. Define



$$
(\mathcal F_cf)(u)=\int_{-1}^1e^{icuv}f(v)\,dv,
\qquad c=\tfrac12.
$$



Let L_c=-D(1-u^2)D+c^2u^2. A direct derivative calculation shows
L_(c,u)e^(icuv)=L_(c,v)e^(icuv). For a polynomial f the two integrations
by parts have zero endpoint terms because 1-v^2 vanishes. The resulting
identity L_c F_c f=F_c L_c f extends to the Legendre operator domain:
polynomials are a graph core, F_c is bounded, its images are smooth,
and the closedness of L_c passes the identity to the graph limit.
Its smooth images lie in the natural domain; for example applying
the differential operator to the smooth integral kernel gives an
L2 function, and its boundary flux vanishes at both endpoints.

The simple spectrum therefore gives nonzero constants mu_l with



$$
\boxed{\mathcal F_{1/2}y_l=\mu_l y_l.}
\tag{26}
$$



To see nonzero without any eigenvalue asymptotics, F_c is injective:
if its entire Fourier transform vanishes on [-1,1], the identity
theorem makes it vanish everywhere, so all polynomial moments of f
vanish; density of polynomials gives f=0. This argument uses c!=0.

The initial amplitudes in (22) now have the exact formulas



$$
\boxed{
g_l=\begin{cases}
\mu_l y_l(0)/\sqrt2,&l\text{ even},\\[2mm]
\sqrt3\,\mu_l y_l'(0)/(\sqrt2\,i),&l\text{ odd}.
\end{cases}}
\tag{27}
$$



The even identity evaluates (26) at0. For odd l, differentiate (26)
at0 and use
g_l=(sqrt3/(2sqrt2)) integral_(-1)^1 v y_l(v)dv and c=1/2.
These formulas are unchanged by a consistent choice of eigenfunction
sign. They express the previously unquantified amplitudes through
classical finite Fourier eigenvalues and central values or derivatives.

For normalization against concentration-operator literature, let
Lambda_l be the eigenvalue of the kernel
sin(c(u-v))/(pi(u-v)) on [-1,1]. Direct multiplication of the finite
Fourier operator and its adjoint gives



$$
\Lambda_l=\frac{c}{2\pi}|\mu_l|^2
=\frac{|\mu_l|^2}{4\pi}.
\tag{28}
$$



No fixed-c large-l asymptotic has yet been imported or proved here.
Equations (27),(28) specify the exact normalization needed before
using that literature to estimate the actual two-branch weights.
