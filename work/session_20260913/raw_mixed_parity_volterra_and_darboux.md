> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact coupling of the parity kernels and the eliminated fourth-order equation

Date: 2026-09-13. Original continuation by audit_computations.

This continues the all-index mixed oscillation problem without extending
the finite degree checks. It gives exact positive Volterra recurrences,
individual Stieltjes ratios, and the differential equation and first jets
after a whole parity is eliminated. These do not yet prove the required
bound of m+1 zeros for the remaining m-dimensional space.

## 1. A normalized, positive two-kernel recurrence

Use beta_k=k^2/(4k^2-1), alpha_m=Q_(2m)(0)>0 and
b_m=Q'_(2m+1)(0)>0. Define



$$
E_m(x)=F_{2m}(x)/\alpha_m,\qquad
O_m(x)=F_{2m+1}(x)/b_m,\qquad
(I f)(x)=\int_0^x f(t)\,dt.
$$



Thus E_m(0)=1 and O_m'(0)=1. The raw recurrence and its coefficient
Borel transform give



$$
\alpha_{m+1}=\beta_{2m+1}\alpha_m,\qquad
\frac{b_m}{\alpha_m}=\frac{(2m+1)^2}{4m+1},\qquad
\frac{\alpha_{m+1}}{b_m}=\frac1{4m+3}.
\tag{1}
$$



The middle identity also follows by evaluating
`(1+t^2)Q_k'=k t Q_k+k^2 Q_(k-1)/(2k-1)` at zero for odd k.
Consequently the two actual parity kernels obey



$$
\boxed{E_{m+1}-E_m=(4m+3)I O_m,}
\tag{2}
$$





$$
\boxed{(2m+1)^2 O_m=(4m+1)I E_m+4m^2 O_{m-1}.}
\tag{3}
$$



For m=0 put O_(-1)=0; then E_0=1,O_0=x. These identities hold for every
m, not just for large m. In particular



$$
O_m=\frac{D(E_{m+1}-E_m)}{4m+3},\qquad
(2m+1)^2 O'_m-4m^2O'_{m-1}=(4m+1)E_m.              \tag{4}
$$



Writing a_m=4m+3, c_m=(4m+1)/(2m+1)^2 and
 d_m=4m^2/(2m+1)^2, the exact transfer is



$$
\binom{E_{m+1}}{O_m}
=\begin{pmatrix}1+a_mc_m I^2&a_md_m I\\c_m I&d_m\end{pmatrix}
\binom{E_m}{O_{m-1}}.                              \tag{5}
$$



It factors into an upper and a lower triangular matrix with nonnegative
Volterra entries. For m>=1 its operator determinant is d_m>0.
The inverse is not a positive Volterra matrix. Formula (5) therefore
cannot itself be treated as a variation-diminishing transformation of
arbitrary signed high-block coefficient combinations.

For a high block, (4) expresses every opposite-parity member as the
derivative of a difference of two neighboring normalized same-parity
members. The end member immediately above the high block is retained
in this identity; deleting it would change the space.

## 2. Each consecutive ratio is Stieltjes, but its measure moves with m

The reviewed strict imaginary-root interlacing in
`raw_borel_legendre_literature.md` implies the following exact rational
representation. Let the positive imaginary roots of F_(2m) and
F_(2m+1)/x be a_1,...,a_m and b_1,...,b_m, respectively. Then



$$
0<a_1<b_1<a_2<b_2<\cdots<a_m<b_m,
$$



and



$$
\frac{F_{2m+1}(\sqrt y)}{\sqrt y F_{2m}(\sqrt y)}
=\frac1{2m+1}+\sum_{j=1}^m\frac{w_{m,j}}{y+a_j^2},
\qquad w_{m,j}>0.                                \tag{6}
$$



Indeed the ratio is `(2m+1)^(-1) product(y+b_j^2)/product(y+a_j^2)`.
Its residue at -a_j^2 has the same number j-1 of negative factors in
numerator and denominator, hence is positive. Polynomial division fixes
the constant at infinity. No unknown common measure is used in (6).

The infinity-normalized ratio
`rhat_m=(2m+1)F_(2m+1)/(sqrt(y)F_(2m))` has first moment



$$
\boxed{rhat_m(y)=1+
\frac{4m^2(12m^2-1)}{16m^2-1}\,\frac1y+O(y^{-2}).} \tag{7}
$$



To verify this, the coefficient of x^(k-2) in the monic polynomial
`k!F_k(x)` is



$$
A_k=\frac{k^2(k-1)^2}{2(2k-1)}.
$$



The coefficient in (7) is A_(2m+1)-A_(2m), which simplifies to the
displayed expression. Thus these normalized ratios cannot all be Padé
approximants of one fixed Stieltjes function already matching its first
nonconstant infinity coefficient. Their discrete measures and total
masses change with m. This only rules out that direct fixed-measure
identification; it does not rule out a different transformed or
parameter-dependent multiple-orthogonality representation.

## 3. The exact order-r elimination has a smooth fourth-order intertwiner

Choose r distinct high indices of parity sigma, and let
`f_i=F_(k_i)` in increasing order. The preceding note proves that
`W(f_1,...,f_r)` has no zero for x>0. The monic differential operator



$$
A_r f=\frac{W(f_1,\ldots,f_r,f)}{W(f_1,\ldots,f_r)}
\tag{8}
$$



is therefore well defined with smooth real rational coefficients on
(0,infinity). Its kernel is exactly the selected same-parity space.
The original operator is



$$
L=x^2D^4+4xD^3+(x^2+2)D^2+2xD,
\qquad LF_k=k(k+1)F_k.
$$



Right division of A_r L by the monic A_r yields



$$
\boxed{A_r L=\widetilde L_r A_r,\qquad
\widetilde L_r=x^2D^4+(2r+4)xD^3+\cdots.}          \tag{9}
$$



The remainder has order below r and annihilates all r selected
functions. Their nonzero Wronskian forces that remainder to be zero.
The displayed third-derivative coefficient follows by comparing the
terms of order r+3; the coefficient of D^(r-1) in A_r cancels.
Hence every remaining transformed function satisfies the SAME exact
fourth-order equation `Ltilde_r g=k(k+1)g`.

This is an actual Darboux intertwining statement. It does not reduce the
order to two, and no common right-endpoint condition has been produced.

## 4. The origin jets of the remaining kernel are explicit and signed

Put sigma'=1-sigma, kappa_j=(sigma+2j)(sigma+2j+1), and



$$
P_r(z)=\prod_{j=0}^{r-1}(z-\sigma-2j),\qquad
\mathcal S=\sum_{i=1}^r k_i(k_i+1)-\sum_{j=0}^{r-1}\kappa_j.
$$



The same-parity Taylor coefficient Vandermonde gives a basis of the
kernel with leading powers `x^sigma,x^(sigma+2),...,x^(sigma+2r-2)`.
Consequently



$$
A_r=x^{-r}\left[P_r(\theta)+x^2 B_r(\theta)+O(x^4)\right],
\quad\theta=xD,
$$





$$
\boxed{B_r(z)=b_r\prod_{j=0}^{r-2}(z-\sigma-2j),\qquad
b_r=-\frac{2r\mathcal S}{[(\sigma+2r)(\sigma+2r-1)]^2}.}
\tag{10}
$$



Here O(x^4) denotes an operator series in x^2 with polynomial theta
coefficients of degree at most r-1 beyond the first term. To check the
coefficient B_r, its degree is at most r-1 because A_r is monic. On the
first r-1 leading powers, annihilation forces its roots
`sigma,sigma+2,...,sigma+2r-4`. For the last leading power, the ratio of
the next coefficient to the leading one is
`S/[(sigma+2r)(sigma+2r-1)]^2`: it is the (r-1)-st divided difference
of the monic Newton polynomial of degree r, divided by the corresponding
one of degree r-1. Evaluating P_r at sigma+2r then gives (10).
This also proves (10) for r=1, with an empty product.

Let G_(sigma')(lambda,x) be the analytic opposite-parity fundamental
solution normalized to have coefficient one at x^sigma'. Its j-th
coefficient is a degree-j monic Newton polynomial in lambda divided by
`((sigma'+2j)!/sigma'!)^2`. Define the normalized eliminated kernel



$$
H_r(\lambda,x)=\frac{x^{r-\sigma'}}{P_r(\sigma')}
 A_rG_{\sigma'}(\lambda,x).
\tag{11}
$$



Since P_r(sigma')!=0, it is analytic in x^2 at zero and starts with 1.
Its coefficient of x^(2j) is a polynomial of degree j in lambda, with
exact leading coefficient



$$
\boxed{\ell_j=
\frac{P_r(\sigma'+2j)}{P_r(\sigma')}
\frac1{((\sigma'+2j)!/\sigma'!)^2}.}                \tag{12}
$$



In particular its first coefficient is



$$
[x^2]H_r=\begin{cases}
\displaystyle\frac{(\lambda-2)/12+b_r}{3-2r},&\sigma=0,\\[6pt]
\displaystyle\frac{\lambda/4+b_r}{1-2r},&\sigma=1.
\end{cases}                                       \tag{13}
$$



For r>=2 in the even elimination, or r>=1 in the odd elimination,
this has STRICTLY NEGATIVE slope in lambda. Therefore the coefficient
minor in any two increasing remaining eigenvalues and columns 1,x^2
is negative. The totally nonnegative Newton coefficient argument used
for the original same-parity family cannot be copied to this mixed
image. This is an exact all-index sign obstruction to that particular
proof, not a disproof of a weaker zero count.

The leading coefficient signs in (12) are `(-1)^min(j,r-1)` for even
elimination and `(-1)^min(j,r)` for odd elimination. Any useful signed
kernel or oscillation theorem must account for this initial alternation.

## 5. Why the ordinary Wronskian theorems have not yet become applicable

Zhang--Filipuk, *On Certain Wronskians of Multiple Orthogonal Polynomials*,
https://arxiv.org/pdf/1402.1569 , prove their sign and zero-count results
for actual multiple-orthogonal polynomial paths whose weight functions
satisfy the stated AT-system conditions. Their Section 1.1 also records
the classical Karlin--Szegő result for ordinary orthogonal polynomials.
The rotated full Borel--Legendre family does not satisfy scalar Favard
orthogonality, as already checked in `raw_borel_legendre_literature.md`.
No fixed weights and normal multi-index path giving the mixed functions
in (11) have been established. Individual interlacing (6) does not
supply those hypotheses; (7) identifies an obstruction to the simplest
common-Markov-function identification.

There is an all-index obstruction to making the ACTUAL eliminated
operator a scalar selfadjoint equation by choosing a positive weight.
The coefficient of D^3 in (9) forces that weight to be proportional to
x^r: formal selfadjointness requires `a_3=2(w a_4)'/w`.

Write the lowest origin part of Ltilde as `x^(-2) ptilde(theta)`.
The lowest-order part of the intertwining identity gives



$$
\widetilde p_r(z)=\begin{cases}
(z-r)(z+r)(z+r-1)^2,&\sigma=0,\\
(z-r-1)(z+r)^2(z+r-1),&\sigma=1.
\end{cases}                                                   \tag{14}
$$



Indeed the original indicial polynomial is `theta^2(theta-1)^2`,
while `P_r(t-2)/P_r(t)=(t-sigma-2r)/(t-sigma)`; substitute
`t=z+r` in the leading intertwining identity. For the weight x^r,
the formal adjoint of this lowest operator is
`x^(-2) ptilde(1-r-theta)`. Its roots would therefore have to be
symmetric under z -> 1-r-z. For even elimination r>=2, the largest
root r would map to 1-2r, strictly below the smallest root -r.
For odd elimination r>=1, the largest root r+1 would map to -2r,
again strictly below the smallest root -r. Both are impossible.

The remaining even case r=1 also fails, at the next origin coefficient.
Put A=D+a with a=-f'/f and lambda_*=k_1(k_1+1). Then
`a=-(lambda_*/2)x+O(x^3)`. Direct coefficient comparison in A L=Ltilde A
shows



$$
\begin{split}
\widetilde a_2&=x^2+6-2ax-4x^2a',\\
\widetilde a_1&=4x-4a+2a^2x+4x^2aa'-18xa'-6x^2a''.
\end{split}
$$



With its forced weight w=x, the required first-derivative coefficient
would be `a_2'+a_2/x-6/x`. The actual minus required value is



$$
x+2a^2x+4x^2aa'-4xa'-2x^2a''
=(1+2\lambda_*)x+O(x^3)\ne0.                         \tag{15}
$$



Thus for EVERY nonempty actual same-parity seed block, the monic
order-r elimination in (8) has no positive weight making its
fourth-order intertwiner formally selfadjoint. This rules out the direct
scalar Sturm import for that operator. It does not rule out a matrix or
indefinite-space representation, and does not disprove the desired zero
bound. No arbitrary substitute sequence or finite extrapolation is used.

## 6. Remaining mathematical target

Equations (2)--(5) give a faithful positive integral coupling of the two
original kernels. Equations (9)--(13) give a faithful local differential
and Taylor description AFTER eliminating one entire high parity.
The needed all-index statement remains that every nonzero combination
of its m remaining eigenfunctions has at most m+1 zeros in (0,1).
A theorem controlling the signed kernel (11), or a verified positive
multiple-orthogonality model for it, would address that question.
None of the identities above proves such a theorem, and no additional
degree scan or numerical extrapolation was used.


## 7. A positive Volterra inverse of the original operator

There is nonetheless useful positivity BEFORE parity elimination.
Let s(x)=sin(x)/x, with s(0)=1, and S(x)=integral_0^x s(t)dt.
On 0<x<1 all these factors are positive. Since
`(x^2s')'+x^2s=0`, the actual operator factors exactly as



$$
\boxed{L=D\,s^{-1}D\,x^2s^2D\,s^{-1}D.}           \tag{16}
$$



For analytic f, both intermediate quantities
`x^2s^2(f'/s)'` and its derivative vanish at zero. Integrating (16)
with those actual origin conditions gives the equivalent equation



$$
f=f(0)+f'(0)S+\lambda\mathcal Kf,\qquad
\mathcal K=I M_s I M_{1/(x^2s^2)} I M_s I,          \tag{17}
$$



for Lf=lambda f. The apparent x^(-2) factor is harmless: the two
integrations on its right produce a function of order at least x^2.
All four integration kernels and all multiplication weights are
nonnegative. An alternative explicit kernel is



$$
(\mathcal Kf)(x)=\int_0^x\frac{du}{u}
 \int_0^u\frac{\sin(u-t)}t\int_0^t f(v)\,dv\,dt.   \tag{18}
$$



It follows either by setting v=f', w=xv in `(x^2v')'+x^2v=lambda If`,
or by differentiating (17). The inner sin(u-t) is positive in the
actual triangle 0<t<u<1. If f>=0 is nonzero on an interval before x,
then Kf(x)>0.

For an explicit convergence bound, set c0=sin(1)>0. On [0,1],
`c0<=s<=1`. For any d>=0,



$$
\mathcal K(x^d)\le
\frac{c_0^{-2}x^{d+2}}{(d+1)^2(d+2)^2}.            \tag{19}
$$



This follows directly by performing the four positive integrals in
(17) after bounding the weights by 1,1,c0^(-2)x^(-2),1. Iteration
proves local uniform convergence in lambda of



$$
G_0(\lambda,x)=\sum_{j\ge0}\lambda^j\mathcal K^j1,
\qquad
G_1(\lambda,x)=\sum_{j\ge0}\lambda^j\mathcal K^jS.  \tag{20}
$$



In fact the respective terms are bounded by
`c0^(-2j) x^(2j)/(2j)!^2` and
`c0^(-2j) x^(2j+1)/(2j+1)!^2`, since 0<S(x)<=x.
The series solve (17) uniquely and hence equal the normalized analytic
fundamental solutions used in (11). Every lambda derivative of either
kernel is strictly positive for x in (0,1) and lambda>=0, including at
lambda=0. This is absolute monotonicity in the spectral parameter.

Equation (16) also gives an elementary endpoint-sensitive Rolle bound:
if analytic f has q>=2 distinct interior zeros and Lf is not identically
zero, then Lf has at least q-2 distinct interior zeros. The first two
weighted differentiations lose at most two; each of the last two
regains an endpoint zero at 0 from the actual analytic conditions.
If an intermediate derivative vanishes identically, f belongs to the
corresponding zero-free or two-dimensional initial span, so it cannot
supply a counterexample with q>=2 (with the case Lf=0 excluded).

The positive operator K and the absolute monotonicity in (20) still do
not supply a variation theorem for an arbitrary mixture of its two
initial-data branches at interlaced, different eigenvalues. In
particular one cannot infer that every positive sum of TP kernels is
TP, or that the resolvent in (20) is a mixed two-channel Chebyshev
kernel. The already proved n=4,5 ordinary-Chebyshev counterexamples
make that scope restriction concrete.

Exact normalization controls for the previously used seeds (5),(6),
(5,7),(6,8) are in `raw_parity_elimination_jet_checks.json`, reproduced
by `check_raw_parity_elimination_jets.py`. They check (10)--(13) through
the x^4 jet symbolically in lambda and are not additional degree scans.
The all-index proofs above do not depend on these controls.

## 8. A further actual-family limit on direct Hermite--Biehler imports

The Christoffel-related Legendre parity weights before Borel transformation
are useful structure, but they do not make arbitrary ACTUAL parity mixtures
real-rooted. This limitation follows in every sufficiently large block from
the already proved same-parity ECT theorem, without a degree scan.

Take any 2s+1 selected normalized parity polynomials e_j(y), y=x^2,
and any s distinct positive points y_1,...,y_s. The 2s homogeneous conditions

    e(y_i)=e'(y_i)=0  (1<=i<=s)

have a nonzero solution in their (2s+1)-dimensional span. The ECT bound,
counting multiplicity, implies that these are exactly double zeros,
that e has no other positive zero, and that e''(y_i)!=0. In particular
e has one sign on the complement of these points; choose that sign positive.
Then e''(y_i)>0 at every one of them. The lowest selected normalized
polynomial e_1 is positive for all y>0. For small epsilon>0,

    e_epsilon(y)=e(y)+epsilon e_1(y)

has a conjugate pair of nonreal roots near EACH y_i. Explicitly, writing
`y=y_i+sqrt(epsilon) z` and dividing by epsilon gives the locally uniform
limit `(e''(y_i)/2)z^2+e_1(y_i)`, whose two roots are simple and nonreal.
Small disjoint disks and the elementary continuity of polynomial roots
prove that all s pairs persist. This argument uses only exact ECT and
local root perturbation, not numerical root diagnostics.

Thus an r-dimensional actual parity block permits mixtures with at least
floor((r-1)/2) distinct nonreal conjugate pairs in its squared variable.
For the high block this number grows with n. It does not contradict the
ECT property on the positive interval or the proposed mixed n-zero bound.
It DOES prevent uniformly applying a theorem whose input hypothesis is
that each arbitrary parity mixture has only real roots with at most a
fixed number of interlacing defects.

For example, the primary paper Kozhan--Tyaglov, *A generalized
Hermite--Biehler theorem*, https://arxiv.org/pdf/2302.07018 , describes
one broken interlacing location; its Theorem 3.1 still assumes that the
underlying p and q have simple real strictly interlacing zeros before
the displayed multiplication by z. Those hypotheses have not been
verified for the arbitrary mixtures needed here, and the construction
above rules out a direct universal real-rootedness assertion. A different
matrix or indefinite-space representation could still help, but would
need an actual index bound rather than a formal invocation of that theorem.
