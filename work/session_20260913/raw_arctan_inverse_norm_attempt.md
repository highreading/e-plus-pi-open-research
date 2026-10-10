> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The actual normalized raw polynomial: an exact residual determinant and the unresolved upper bound

Date: 2026-09-13. Bounded independent attempt at an upper bound for
$M_n=\int_0^1|P_n|$, with the actual normalization B(1)=1.

**Status:** no upper bound of the form $n!\exp(O(n))$ is proved here.
The new result is an exact positive Gram-determinant quotient and an
explicit factorial-scale endpoint functional. It identifies the precise
Archimedean lower-bound problem left after the existing nonvanishing
theorem. It does not promote nonvanishing or coefficientwise closeness
to a quantitative inverse bound.

## 1. Existing dependencies and exact normalization

The actual raw family has
$A+Be^z+C\arctan z=O(z^{3n+1})$, degrees at most n,
$C(1)=4B(1)$, and



$$
P_B(x)=\sum_{j=0}^nB_j\frac{(1-x)^{n-j}}{(n-j)!}.
$$



The inverse change of variables gives
$B_{n-j}=(-1)^jP_B^{(j)}(1)$. Hence define the actual functional



$$
\beta_n(P)=\sum_{j=0}^n(-1)^jP^{(j)}(1)=B(1).
\tag{1}
$$



Let $F_k=\mathcal BQ_k$ be the sequence in
`raw_borel_legendre_literature.md` and put



$$
T_n=\mathcal B_tK_n(1,t),\qquad
 K_n(t,s)=\sum_{k=0}^n\frac{Q_k(t)Q_k(s)}{h_k}.
$$



The polynomial T_n has degree n. The exact reduced equations for P_n are



$$
\int_0^1P_nF_k=0\quad(n+1\le k\le2n-1),
 \qquad \int_0^1P_nT_n=-4,\qquad \beta_n(P_n)=1.
\tag{2}
$$



The bordered-rank proof and its endpoint determinant theorem establish
that the n+1 functionals in (2) are independent. The scalar B(1) really
is nonzero before normalization; (2) therefore selects one actual
polynomial, not an arbitrary vector in a larger nullspace.

I inspected the old exact determinant ratio
$A(1)/B(1)=\Delta_A/(n!\Delta_B)$, its cofactor interpretation, and
the coarse Hadamard estimate. Its dyadic proof establishes nonzero
$\Delta_B$, but it provides no comparison of absolute values of
cofactors and $\Delta_B$. That comparison is precisely what is needed
for the present norm question.

## 2. The endpoint functional has an explicit factorial-size representer

Work in $\mathcal P_n$ with the real L2(0,1) inner product. Let
$J_k(x)=P_k(2x-1)$, so $\int_0^1J_kJ_l=\delta_{kl}/(2k+1)$.
The Riesz representer of (1) is the explicit rational polynomial



$$
Z_n(x)=\sum_{k=0}^n(2k+1)b_kJ_k(x),\qquad
 b_k=\sum_{j=0}^k(-1)^j\frac{(k+j)!}{(k-j)!j!}.
\tag{3}
$$



Indeed $J_k^{(j)}(1)=(k+j)!/((k-j)!j!)$, which follows directly from
the shifted Legendre coefficient formula. Thus
$\langle Z_n,P\rangle=\beta_n(P)$ for every P of degree at most n.
The same functional on monomials is
$\beta_n(x^j)=(-1)^jD_j$, where
$D_j=j!\sum_{r=0}^j(-1)^r/r!$ is the derangement integer. In particular
$\beta_n(x)=0$; it is not evaluation at x=1 or a positive integration
functional on [0,1].

Put $A_k=(2k)!/k!$. Reversing the finite sum in (3) yields



$$
b_k=(-1)^kA_k
 \sum_{r=0}^k\frac{(-1)^r}{r!}\frac{(k)_{\underline r}}
                                  {(2k)_{\underline r}}.
\tag{4}
$$



For k>=1 each factor $(k-a)/(2k-a)$ is at most 1/2. The terms in the
last alternating sum decrease in magnitude, its first two terms are
1 and -1/2, and for each fixed r the quotient tends to 2^(-r). Therefore



$$
\tfrac12A_k\le |b_k|\le A_k,\qquad
 \frac{(-1)^kb_k}{A_k}\longrightarrow e^{-1/2}.
\tag{5}
$$



The limit follows by domination by $2^{-r}/r!$, after extending the
finite summand by zero for r>k. Since
$A_{k-1}/A_k=1/[2(2k-1)]$, the final term dominates the sum of squares
in $\|Z_n\|_2^2=\sum_{k=0}^n(2k+1)b_k^2$. More explicitly the terms
below n are at most $(2n-1)(4/3)A_{n-1}^2$, using
$A_{k-1}\le A_k/2$. Relative to the last term this is O(n^(-2)).
Together with the elementary central-binomial asymptotic this proves



$$
\boxed{\|Z_n\|_2\sim
       \sqrt{\frac2\pi}\,e^{-1/2}4^n n!.}
\tag{6}
$$



Thus factorial scales arise in the exact endpoint functional already.
This is a statement about its full representer. Projection off the high
moment span can substantially change its norm, so (6) is not an estimate
for the normalized P_n by itself.

## 3. Exact Gram quotient for the actual solution

Let $\Pi_n$ be the orthogonal projection onto $\mathcal P_n$, and set



$$
H_k=\Pi_nF_k\quad(n+1\le k\le2n-1),\qquad
 W_n=T_n+4Z_n.
\tag{7}
$$



Projection is essential: F_k itself can have degree larger than n.
The equations (2) are equivalent to



$$
P_n\perp\mathcal S_n,
 \quad\langle P_n,Z_n\rangle=1,\qquad
 \mathcal S_n=\operatorname{span}(H_{n+1},\ldots,H_{2n-1},W_n).
\tag{8}
$$



Independence of the original functionals gives dim S_n=n and
$Z_n\notin\mathcal S_n$. Define



$$
Z_n^\perp=Z_n-\operatorname{proj}_{\mathcal S_n}Z_n,
 \qquad \delta_n=\|Z_n^\perp\|_2>0.
\tag{9}
$$



The one-dimensional complement and (8) give the exact formula



$$
\boxed{P_n=\frac{Z_n^\perp}{\delta_n^2},
       \qquad\|P_n\|_2=\delta_n^{-1}.}
\tag{10}
$$



If $\mathcal G(v_1,\ldots,v_r)$ denotes the Gram determinant, the
Schur-complement formula proves



$$
\boxed{\|P_n\|_2^2=
 \frac{\mathcal G(H_{n+1},\ldots,H_{2n-1},W_n)}
      {\mathcal G(H_{n+1},\ldots,H_{2n-1},W_n,Z_n)}.}
\tag{11}
$$



Both determinants are strictly positive. This is an identity in the
actual endpoint normalization; no arbitrary scaling of high rows or a
cofactor remains in their ratio.

There is also a two-dimensional version. Let
$V_n=\operatorname{span}(H_{n+1},\ldots,H_{2n-1})^\perp$, and denote
the projections of Z_n,T_n onto V_n by z_n,t_n. Then



$$
\|P_n\|_2^2=
 \frac{\|t_n+4z_n\|_2^2}
      {\|t_n\|_2^2\|z_n\|_2^2-\langle t_n,z_n\rangle^2}.
\tag{12}
$$



The denominator is the squared area of the actual two projected
endpoint vectors. A small norm of t_n is compatible with either a
controlled or an exceptionally small area. Their angle must be estimated.

For every real polynomial P of degree at most n,



$$
\|P\|_1\le\|P\|_2\le(n+1)\|P\|_1.
\tag{13}
$$



The first inequality is Cauchy–Schwarz. For the second, the shifted
Legendre reproducing kernel gives
$\|P\|_\infty\le(n+1)\|P\|_2$, and hence
$\|P\|_2^2\le\|P\|_\infty\|P\|_1$.
Consequently the desired factorial upper bound is equivalent, up to
factors absorbed by exp(O(n)), to the following precise missing lemma:



$$
\boxed{\delta_n\ge \frac{e^{-Cn}}{n!}
       \quad\hbox{for one fixed C and all sufficiently large n}.}
\tag{14}
$$



The existing parity-interpolation lower mass bound gives the opposite
direction $\delta_n\le e^{O(n)}/n!$. It does not imply (14).

## 4. Four-jet construction of the Gram entries

No numerical approximation is needed to construct (11). One option is
the shifted Legendre basis used in Section2 and exact rational integrals.
Alternatively, use the low Borel basis F0,...,Fn, whose Gram matrix is G.
Write the row vectors of mixed pairings with high F_k as C. The projected
high Gram block is exactly $CG^{-1}C^T$, not the unprojected high Gram
block. The mixed entries of C, and all off-diagonal entries of G, have
the four-jet formula



$$
\langle F_k,F_l\rangle
 =\frac{\mathfrak b(F_k,F_l)(1)}{l(l+1)-k(k+1)}\quad(k\ne l)
\tag{15}
$$



proved in `raw_borel_legendre_literature.md`. Diagonal entries can be
integrated exactly. Formula (15) supplies structure, but it is not an
inverse estimate: the low Borel basis itself contains factorially small
leading coefficients, and the Schur complements must retain them.

The generating function gives estimates for individual entries and
endpoint jets. An entrywise estimate of bounded exponential size does
not bound the reciprocal of a growing determinant. No theorem converting
these particular four-jet entries into (14) has been established here.

## 5. Why the simplest perturbation attempt fails

Parity spectral divided differences turn the high rows into polynomials
with a low monomial leading term and tails beginning at higher powers.
For indices close to the top retained power, the normalized next tail
coefficient can have scale O(1/n). This is useful algebra, but it is not
enough for a norm perturbation argument in the monomial basis.

Indeed the Gram matrix of 1,x,...,x^d on [0,1] is Hilbert. Let J_d be the
shifted Legendre polynomial. Its leading monomial coefficient is
$\binom{2d}{d}$, while $\|J_d\|_2^2=1/(2d+1)$. Therefore the smallest
eigenvalue of that monomial Gram matrix is at most



$$
\frac1{(2d+1)\binom{2d}{d}^2}=\exp(-d\log16+O(\log d)).
\tag{16}
$$



An O(1/n) coefficient perturbation is far larger than this scale. One
must bound the perturbation after a suitably conditioned change of basis
or estimate the actual determinant directly. Ordinary coefficientwise
closeness and a known nonzero determinant cannot justify (14).

Likewise, the unique least dyadic Laplace summand is not a unique largest
Archimedean summand. Its valuation comparison cannot be used as a reverse
triangle inequality for real absolute values.

## 6. Concrete remaining target

The most useful next analytic result would be a lower bound for the
actual residual (9), equivalently the area in (12), retaining both
endpoint functionals. The available upper estimates for individual
F_k, the exact positive kernel, imaginary-axis interlacing, and the
dyadic rank proof do not supply this lower bound. A factorial upper
bound remains open after this attempt. No implication for primitive
endpoint denominators is inferred from a future norm bound alone.

## 7. Exact normalization controls

`check_raw_inverse_norm.py` independently constructs the monomial
Hilbert matrix, the projected high rows, and both actual endpoint
functionals for n=1,2,4. It verifies (11), reconstructs B and C, and
checks B(1)=1, C(1)=4, and every original high Taylor equation through
degree 3n. All checks pass; exact outputs are saved in
`check_raw_inverse_norm.json`. No growth estimate is inferred from these
finite controls.
