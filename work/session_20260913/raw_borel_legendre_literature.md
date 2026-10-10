> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The raw Borel–Legendre sequence: exact structure and applicability of positivity theorems

Date: 2026-09-13. Bounded continuation of the actual raw-arctangent family.
This note supplies auxiliary identities and precise obstructions. It does not
bound the normalized whole remainder and does not prove the main irrationality
claim. The formulas below are derived for the actual sequence, not for an
analytically similar Bessel or multiple-orthogonal family.

## 1. Actual object and the missing quantitative question

Use the monic raw Legendre polynomial and its coefficient Borel transform



$$
Q_k(t)=\frac{2^ki^k}{\binom{2k}{k}}P_k(-it)
       =\frac{k!}{(2k)!}\frac{d^k}{dt^k}(1+t^2)^k,
 \qquad F_k(x)=\mathcal BQ_k(x).
\tag{1}
$$



Here $\mathcal B(\sum q_dt^d)=\sum q_dx^d/d!$, and $P_k$ is ordinary
Legendre. Thus



$$
F_k(x)=\frac{k!}{(2k)!}
 \sum_{\substack{0\le d\le k\\d\equiv k\ (2)}}
 \binom{k}{(k+d)/2}\frac{(k+d)!}{(d!)^2}x^d.
\tag{2}
$$



The actual matched polynomial $P_B$ obeys
$\int_0^1P_BF_k=0$, $n+1\le k\le2n-1$. The whole endpoint remainder is
$\int_0^1P_BG_n$, where $G_n>0$ is the explicit kernel in
`raw_arctan_positive_kernel_attempt.md`. Neither the sign of individual
coefficients in (2) nor the positivity of that kernel controls the signed
cancellation in this integral.

Prior archive checks: the old raw endpoint note contains the two-integral,
Taylor-integral, and contour representations. The old constrained Chebyshev
counterexamples concern a different Machin family. The current-session
`raw_arctan_borel_chebyshev_obstruction.md` independently gives exact interior
counterexamples for the actual blocks at n=4 and n=5. Those finite
counterexamples refute a theorem for every n, but do not refute a possible
eventual or selected-subsequence theorem.

## 2. Two exact terminating hypergeometric formulas

For m>=0,



$$
\frac{F_{2m}(x)}{Q_{2m}(0)}
 ={}_2F_3\left(\begin{matrix}-m,m+\tfrac12\\
 \tfrac12,\tfrac12,1\end{matrix};-\frac{x^2}{4}\right),
\tag{3}
$$





$$
\frac{F_{2m+1}(x)}{Q'_{2m+1}(0)}
 =x\,{}_2F_3\left(\begin{matrix}-m,m+\tfrac32\\
 \tfrac32,\tfrac32,1\end{matrix};-\frac{x^2}{4}\right).
\tag{4}
$$



These follow directly from (2): divide consecutive nonzero coefficients,
and use $(2j)!=4^jj!(1/2)_j$ and
$(2j+1)!=4^jj!(3/2)_j$. The series terminate, so no convergence or
analytic-continuation assumption is involved. In particular these are not
the usual Bessel polynomials, whose support and factorial weights differ.

## 3. An exact Bessel generating function

Set $c_k=2^{-k}\binom{2k}{k}$. Then



$$
\boxed{\sum_{k\ge0}c_kF_k(x)z^k
  =\frac{e^{u}I_0(u)}{\sqrt{1-z^2}},\qquad
   u=\frac{xz}{1-z^2}.}
\tag{5}
$$



Indeed the ordinary Legendre generating function gives
$\sum c_kQ_k(t)z^k=(1-2tz-z^2)^{-1/2}$. Expand the right side in t and
apply the Borel transform coefficientwise. The result is



$$
(1-z^2)^{-1/2}
 {}_1F_1\left(\tfrac12;1;\frac{2xz}{1-z^2}\right),
$$



which is (5) by the Kummer–Bessel identity
${}_1F_1(1/2;1;2u)=e^uI_0(u)$.
For reference the general identity is recorded in
[DLMF 13.6.9](https://dlmf.nist.gov/13.6.E9).

This argument is valid first as a formal power series. It also gives an
analytic identity for |z|<1 and every complex x. To check uniform convergence
on compact sets, dominate by the series with |x| and |z|; all coefficients
in (2) are nonnegative, and the resulting right side is finite for real
0<=|z|<1. Thus coefficient contours strictly inside the unit disk are valid.

An alternative positive representation for the generating function is
$e^uI_0(u)=\pi^{-1}\int_0^\pi e^{u(1+\cos\theta)}d\theta$. Formula (5)
can support contour or saddle estimates for individual polynomials and
their endpoint jets. It does not supply a uniform inverse bound for an
n-dependent block of moment equations.

## 4. Real-root preservation and strict imaginary-axis interlacing

The coefficient multiplier $\gamma_d=1/d!$ preserves real-rootedness.
One direct check of the Pólya–Schur hypothesis is



$$
\mathcal B(1+x)^N=\sum_{d=0}^N\binom Nd\frac{x^d}{d!}=L_N(-x).
$$



Ordinary Laguerre orthogonality makes its zeros positive, so this last
polynomial has all zeros negative. The finite Jensen-polynomial criterion
therefore applies. The exact criterion and the pencil/interlacing theorem
are Theorems 1.7(iv) and 1.5 in
[Borcea–Brändén, *Multivariate Pólya–Schur classification problems in the
Weyl algebra*](https://arxiv.org/pdf/math/0606360), pp.4–5. Those theorem
statements were read; the whole classification paper was not independently
reproved here.

A useful strictness fact has an elementary proof. For a real-rooted P of
degree d, put $P^{\rm rev}(z)=z^dP(1/z)$. Then



$$
\mathcal BP(x)=P^{\rm rev}(D)\frac{x^d}{d!}.
\tag{6}
$$



If P has a zero of multiplicity s at zero, its reversal has degree d-s
and only real nonzero roots. Factor the operator on the right into d-s
factors D-r with real r!=0. For a real-rooted f, every new root of
$(D-r)f$ away from the roots of f solves $f'/f=r$. On every gap
$(f'/f)'=-\sum m_a/(x-a)^2<0$. Thus all such new roots are simple;
an inherited root of multiplicity m loses one multiplicity. Starting
from x^d, after d-s operations the only possible multiple root is zero,
with exactly multiplicity s. Consequently $\mathcal BP$ has only simple
roots whenever s<=1. The degree and real-root count also follow at each
step by the same monotonicity and the endpoint limits of f'/f.

Now $p_k(y)=i^{-k}Q_k(iy)$ is a nonzero real multiple of ordinary
Legendre. Every real pencil of consecutive p_k is real-rooted by
interlacing. Each nonzero such pencil has a zero at zero of multiplicity
at most one: its even part has a nonzero constant unless absent, and its
odd part has a nonzero linear coefficient. Apply (6) to every pencil.
Since Borel transformation commutes with the rotation, the transformed
consecutive pair is real-rooted and interlacing. It cannot have a common
root: a linear combination canceling the derivatives there would have a
multiple root, contradicting the strictness just proved. Hence all roots
of F_k are simple and on the imaginary axis, and consecutive F_k have
strictly interlacing imaginary-axis roots.

This conclusion is about roots after a complex rotation. It is compatible
with failure of the Chebyshev property for a consecutive high block on
the real interval (0,1). It cannot be used as a real-interval
variation-diminishing theorem for that block.

## 5. Fourth-order equation and exact Green identity

The raw Legendre equation is
$(1+t^2)Q_k''+2tQ_k'=k(k+1)Q_k$. Write $F_k=\sum f_jx^j$, so that the
coefficient of t^j in Q_k is j!f_j. Then



$$
(j+2)^2(j+1)^2f_{j+2}
 +[j(j+1)-k(k+1)]f_j=0.
\tag{7}
$$



Therefore, with D=d/dx,



$$
\boxed{\mathscr LF_k=k(k+1)F_k,\quad
 \mathscr L=D^2x^2D^2+Dx^2D
 =x^2D^4+4xD^3+(x^2+2)D^2+2xD.}
\tag{8}
$$



For arbitrary polynomials F,G define



$$
\mathfrak b(F,G)=F(x^2G'')'-F'x^2G''
 -G(x^2F'')'+G'x^2F''+x^2(FG'-F'G).
\tag{9}
$$



Direct differentiation cancels the cross terms and yields
$\mathfrak b'=F\mathscr LG-G\mathscr LF$. Every term vanishes at zero.
In particular, for k!=l,



$$
[l(l+1)-k(k+1)]\int_0^1F_kF_l\,dx
   =\mathfrak b(F_k,F_l)(1).
\tag{10}
$$



At x=1 this boundary form depends only on the first four jets:



$$
\mathfrak b(F,G)(1)=FG'''-F'''G+2(FG''-F''G)
 -F'G''+F''G'+FG'-F'G.
\tag{11}
$$



Thus mixed Gram entries have an exact endpoint representation with a
fixed-size skew boundary matrix and spectral denominator. This is useful
structure, although a bound on the inverse of a growing Gram or constrained
moment matrix still requires a separate estimate.

Formal symmetry does not mean the polynomials satisfy a common
self-adjoint boundary condition on [0,1]. For example F0=1 and F1=x give
$\mathfrak b(F_0,F_1)(1)=1$, not zero. This already prevents placing the
entire sequence in one self-adjoint L2(0,1) domain with these distinct
eigenvalues and the usual inner product.

## 6. Exact obstructions to importing scalar Krall or total positivity

There is a stronger scalar orthogonality obstruction than the boundary
example. The monic polynomials $R_k=k!F_k$ begin



$$
R_0=1,\ R_1=x,\ R_2=x^2+\tfrac23,\quad
 R_3=x^3+\tfrac{18}{5}x,\quad
 R_4=x^4+\tfrac{72}{7}x^2+\tfrac{72}{35}.
$$



If a quasi-definite scalar moment functional made them orthogonal, the
monic Favard recurrence would read
$R_{k+1}=(x-a_k)R_k-b_kR_{k-1}$. Parity forces a_k=0. At k=3, comparison
of x^2 coefficients forces $b_3=-234/35$; its constant term would then
be 156/35, whereas R4 has constant 72/35. This is a contradiction.
Thus no quasi-definite scalar functional, even signed or complex, makes
the entire sequence orthogonal. Invertible affine changes of variable
and nonzero degreewise scalings do not remove a three-term-recurrence
obstruction.

The primary paper
[Kwon–Littlejohn–Yoon, *Construction of differential operators having
Bochner–Krall orthogonal polynomials as eigenfunctions*](https://mathsci.kaist.ac.kr/bk21/morgue/research_report_pdf/04-21.pdf)
was checked through its definitions and main introductory hypotheses.
It starts with a quasi-definite orthogonalizing functional and a classical
functional plus finite point distributions. The existence of a polynomial
differential eigen-equation by itself is not that hypothesis. The
contradiction above prevents this application to our entire sequence.

Nor can the actual real F_k be orthogonal for a standard positive diagonal
Sobolev inner product $\sum_j\int f^{(j)}g^{(j)}d\mu_j$: the constant
must have positive norm, so $\mu_0$ is nonzero, while
$\langle F_0,F_2\rangle=\int(x^2/2+1/3)d\mu_0>0$.
This does not classify more general nondiagonal or indefinite Sobolev
pairings, and no claim about all such pairings is made.

The ordinary Bessel coefficient-matrix total positivity studied in
[Díaz–Mainar–Rubio, *Polynomial Total Positivity and High Relative Accuracy
Through Schur Polynomials*](https://link.springer.com/article/10.1007/s10915-023-02323-1),
Section5.3, concerns a different polynomial basis. The actual coefficient
array here is not totally nonnegative in increasing degree and power:
the minor with rows F1,F2 and columns 1,x equals -1/3. Thus the ordinary
Bessel collocation theorem has no direct application. A separated-parity
minor theorem would require its own hypotheses and proof.

## 7. Recent multiple-Bessel literature: an exact moment coincidence,
but no applicable normality or positivity conclusion

[Mañas, *Bessel-Like Multiple Orthogonal Polynomials of Mixed Type*,
arXiv:2608.00781v2](https://arxiv.org/html/2608.00781v2), dated 20 August
2026, Proposition6.3 uses moments $\mathcal L_j(z^d)=1/\Gamma(d+\alpha_j+2)$.
Our factorial functionals have exactly these moments with
$\alpha_j=n-j$. However, Definition3.1 requires noninteger separation
of the column parameters, whereas these differences are integers. The
formula-specific admissibility convention does not silently remove that
regularity hypothesis. Also our constraints use the high Legendre block,
not the initial monomial blocks in its multiple-orthogonality definition.
The paper explicitly treats its factorization as algebraic and asserts
no positivity. Its introductory hypotheses, normality setup, one-row
reduction, and relevant conclusion were inspected; a full independent
audit of the 70-page preprint was not performed. No acceptance or
completeness claim is inferred from the preprint alone.

It remains possible to derive a confluent/resonant formula by taking
limits, but one must prove the rank and normalization survive and then
show that the actual high-block constraints are obtained. A resemblance
of reciprocal-Gamma moments alone does neither.

## 8. Ranked concrete next steps and limits of these results

1. Use (5), (8), and (11) to derive uniform estimates for endpoint jets and
   the actual constrained moment matrix, including its smallest relevant
   singular value or a determinant quotient. A bound for a fixed number
   of F_k is insufficient when both block size and index grow with n.
2. Seek a direct signed-integral estimate for the uniquely matched P_B,
   retaining its endpoint normalization. The existing positive kernel
   estimate and exact nonvanishing/distinctness result leave the absolute
   mass and signed cancellation separate and uncontrolled.
3. Investigate resonant reciprocal-Gamma determinant identities only if
   an exact bridge to the high Legendre block can first be shown. This
   is more concrete than importing a general multiple-orthogonality
   positivity assertion whose parameters do not apply.

The imaginary-axis interlacing, fourth-order equation, and Bessel
generating function are rigorous auxiliary structure. They do not supply
the missing exponential cancellation or primitive-denominator estimate.

## 9. Independent exact controls

`check_raw_borel_structure.py` constructs Q_k directly from Rodrigues,
then applies the coefficient transform without using the proposed
hypergeometric or generating-function formulas. It verifies (3)–(5) and
(8) for degrees 0 through 8, and the differentiated Green identity and
zero-endpoint boundary for all 81 pairs in that range. All checks pass;
the exact output is `check_raw_borel_structure.json`. These finite
controls are supplementary to the all-degree derivations above.
