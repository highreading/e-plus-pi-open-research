> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Condensation and contiguous-transfer barriers for the equal secant jets

Checked: 2026-08-27 UTC.

## 1. Verdict

Put



$$
F(x)=\frac1{2\cosh\sqrt x}.
\tag{1}
$$



The two equal-parity determinants in the unbalanced centered-cosh
construction admit exact Toeplitz, Desnanot--Jacobi, and contiguous-Padé
descriptions.  Those descriptions do not prove their all-parameter
nonvanishing.  They identify the missing information more sharply:

* scalar Padé normality leaves a six-dimensional boundary quotient under
  one full continued-fraction step;
* the equal $\sigma=1$ jet sits inside the flagged $\sigma=0$ jet with
  codimension three, and the basis-change determinant is explicit;
* Desnanot--Jacobi introduces shifted, off-diagonal Hermite--Padé minors
  rather than a smaller copy of the original determinant; and
* even a coprime rational Markov function with three positive simple nodes
  can make the first nontrivial equal jet vanish exactly.

Thus an argument based only on ordinary resultants, positive nodes,
interlacing, or nonzero scalar continued-fraction coefficients cannot prove
the desired secant theorem.  A special secant boundary-minor identity is
still needed.

An exact finite-field replay tests every admissible pair in both equal jets
through $M=120$: all $7081$ determinants are nonzero modulo



$$
p=2^{61}-1.                       \tag{2}
$$



This proves nonvanishing for that finite grid over $\mathbb Q$, but it is
not extrapolated.  No conclusion about $e+\pi$ follows.

## 2. Cleared quadratic jets

For polynomials or formal series $D,N$, with $D(0)\ne0$, define



$$
\begin{split}
 {\cal E}_m(D,N)={}&D^2{\cal P}_{m-1}
                 +DN{\cal P}_{m-1}
                 +N^2{\cal P}_{m-1},\\
 {\cal F}_m(D,N)={}&D^2{\cal P}_{m+1}
                 +DN{\cal P}_{m}
                 +N^2{\cal P}_{m-1}.
 \end{split}                                                \tag{3}
$$



Let $\Theta_m(D,N)$ be the coefficient determinant of the displayed
basis of ${\cal E}_m(D,N)$ in rows $0,\ldots,3m-1$, and let
$\Psi_m(D,N)$ be the corresponding determinant for
${\cal F}_m(D,N)$ in rows $0,\ldots,3m+2$.  Multiplication by the unit
$D^{-2}$ is lower triangular on every initial coefficient jet.  Hence



$$
\Theta_m(D,N)\ne0
 \iff
 \det [y^i]\{y^j,y^jK,y^jK^2:0\leq j<m\}_{0\leq i<3m}\ne0,
 \quad K=N/D,                                               \tag{4}
$$



and the analogous statement holds for $\Psi_m$ and multiplier counts
$(m+2,m+1,m)$.  These are precisely the cleared forms of the equal jets
in equations (7)--(8) of the coupled-parity theorem, with $m=2r$.

The flagged space has an exact shear invariance:



$$
{\cal F}_m(D,N-yD)={\cal F}_m(D,N). \tag{5}
$$



Indeed, the new terms in $D(N-yD){\cal P}_m$ and
$(N-yD)^2{\cal P}_{m-1}$ lie in the preceding, larger multiplier
blocks.  Applying the inverse shear proves equality.

## 3. Four contiguous Padé identities

Let $Q_{L,D}$ be the denominator of the normal $[L/D]$ Padé pair for
$F$, normalized by $Q_{L,D}(0)=1$.  Put



$$
\begin{array}{lll}
 A_M=Q_{M,M+1},&B_M=Q_{M+1,M},&C_M=Q_{M,M},\\
 B_{M-1}=Q_{M,M-1},&R_M=Q_{M+1,M-1}.&
 \end{array}                                                \tag{6}
$$



Padé uniqueness gives nonzero constants $a_M,b_M,c_M,d_M$ such that



$$
\begin{split}
 A_M-B_M&=c_MxC_M,\\
 B_M-C_M&=b_MxB_{M-1},\\
 C_M-B_{M-1}&=a_MxC_{M-1},\\
 C_M-R_M&=d_MxB_{M-1}.
 \end{split}                                                \tag{7}
$$



For completeness, subtract the two relevant Padé identities in each line.
The numerator constants cancel, so division by $x$ lowers the error order
and the numerator degree by one.  The quotient is respectively a
denominator of type $[M/M]$, $[M/(M-1)]$, $[(M-1)/(M-1)]$, or
$[M/(M-1)]$.  Normality makes that denominator unique up to a nonzero
scalar.  Exact degrees, again supplied by the strictly positive secant
Toeplitz minors, make all four scalars nonzero.

Write $\widehat P(y)=y^{\deg P}P(1/y)$, and set



$$
X_M=\widehat C_M,
 \qquad                  Y_M=y\widehat B_M.                \tag{8}
$$



Reversing the middle two identities in (7) gives the exact transfer



$$
\boxed{
 \binom{X_M}{Y_M}
 =
 \begin{pmatrix}
 a_M&1\\ a_My&b_M+y
 \end{pmatrix}
 \binom{X_{M-1}}{Y_{M-1}},
 \qquad \det=a_Mb_M\ne0.}                                 \tag{9}
$$



The actual $\sigma=1$ pair is
$(\widehat A_M,y\widehat B_M)=(c_MX_M+Y_M,Y_M)$.
Because a constant change of the binary pair acts through its symmetric
square on each multiplier shift,



$$
\Theta_m(\widehat A_M,y\widehat B_M)
                         =c_M^{3m}\Theta_m(X_M,Y_M).        \tag{10}
$$



Thus (10) is a nonzero rescaling, not a new nonvanishing assumption.

For $\sigma=0$, reverse the last identity in (7).  If
$N_0=y^2\widehat R_M$, then



$$
N_0=yX_M-d_MY_{M-1}.               \tag{11}
$$



Equations (5) and (11) give



$$
\Psi_m(X_M,N_0)
 =\pm d_M^{3m+1}\Psi_m(X_M,Y_{M-1}),                     \tag{12}
$$



where the harmless sign depends on column order.  Hence the canonical
pairs in (10) and (12) represent exactly the two secant jets.

## 4. Why one scalar continued-fraction step leaves six dimensions

The symmetric-square matrix of the transfer (9), in the ordered quadratic
basis $(X^2,XY,Y^2)$, is



$$
\begin{pmatrix}
 a_M^2&2a_M&1\\
 a_M^2y&a_M(2y+b_M)&y+b_M\\
 a_M^2y^2&2a_My(y+b_M)&(y+b_M)^2
 \end{pmatrix},                                           \tag{13}
$$



up to transpose according to whether generators are stored by rows or
columns.  Its determinant is $(a_Mb_M)^3$, but its entries have degree as
large as two.  The inverse has the same degree bound.  Consequently, for
$m\geq2$,



$$
{\cal E}_{m-2}(X_{M-1},Y_{M-1})
 \subseteq {\cal E}_{m}(X_M,Y_M)
 \subseteq {\cal E}_{m+2}(X_{M-1},Y_{M-1}).               \tag{14}
$$



In the admissible secant range the three summands are direct: reducing a
putative relation modulo $X$ and modulo $Y$, and using coprimality and
the multiplier degree bounds, forces all three multipliers to vanish.
Thus the first inclusion in (14) has codimension exactly six.  The constant
determinant of (9) does not make a finite multiplier window invariant.
Those six boundary directions are the first nontrivial $m=2$, or
$r=1$, equal jet.

There is also an exact relation between the two parities.  From (9),



$$
Y_M=yX_M+b_MY_{M-1}.               \tag{15}
$$



It follows that



$$
{\cal E}_m(X_M,Y_M)\subseteq{\cal F}_m(X_M,Y_{M-1}).     \tag{16}
$$



Adjoin to the standard basis of the left side the three columns



$$
y^mX_M^2,\qquad y^{m+1}X_M^2,\qquad
                 y^mX_MY_{M-1}.                            \tag{17}
$$



The result is a basis of the right side.  Relative to the standard flagged
basis, its change-of-basis determinant is



$$
\pm b_M^{3m}.                \tag{18}
$$



Indeed, the $m$ columns $y^jX_MY_M$ contribute $b_M^m$, and the
$m$ columns $y^jY_M^2$ contribute $b_M^{2m}$; all remaining pivots
are one.  Thus the flagged determinant adds an exact three-dimensional
boundary quotient to the equal determinant.  Equation (18) is a coupling,
but not a factorization of either leading jet into the other and a known
resultant.

## 5. The exact Desnanot lattice does not close on the diagonal

Let



$$
K(y)=\sum_{n\geq1}k_ny^n,
 \qquad K(y)^2=\sum_{n\geq2}\ell_ny^n,
\tag{19}
$$



with coefficients of negative index defined to be zero.  For $p,q\geq0$
define the two-block Toeplitz minor



$$
D_{p,q}^{(s)}=
 \det\left(
 [k_{s+i-j}]_{\substack{0\leq i<p+q\\0\leq j<p}}
 \ \middle|\
 [\ell_{s+i-j}]_{\substack{0\leq i<p+q\\0\leq j<q}}
 \right).                                                  \tag{20}
$$



Eliminating the monomial block in (4) gives



$$
\Delta_m(K)=D_{m,m}^{(m)}.   \tag{21}
$$



Desnanot--Jacobi, using the first and last rows and the last column of each
block, gives for every $p,q\geq1$



$$
\boxed{
 D_{p,q}^{(s)}D_{p-1,q-1}^{(s+1)}
 =D_{p-1,q}^{(s+1)}D_{p,q-1}^{(s)}
  -D_{p,q-1}^{(s+1)}D_{p-1,q}^{(s)}.}                     \tag{22}
$$



On substituting $p=q=s=m$, the smaller diagonal minor on the left is
$D_{m-1,m-1}^{(m+1)}$, whereas the desired preceding equal jet is
$D_{m-1,m-1}^{(m-1)}$.  Four shifted off-diagonal minors occur on the
right.  They do not even have a common sign on the genuine secant data:
the replay records a sign change between $M=2$ and $M=5$ in two of
the $m=2$ factors while $\Delta_2$ remains nonzero.  Hence (22) is an
exact integrable-lattice identity, but not a one-dimensional positive
recurrence.

## 6. A positive-node counterexample at the first boundary

For a parameter $t$, put



$$
K_t(y)=y\left(\frac1{1-y}+\frac1{1-2y}+\frac{t}{1-3y}\right).           \tag{23}
$$



A direct six-by-six determinant evaluation gives



$$
\boxed{\Delta_2(K_t)
 =(4t-1)(t^3-25t^2-13t+1).}                               \tag{24}
$$



In particular, at $t=1/4$,



$$
\begin{split}
 -\frac{729}{16}y
 +\left(\frac{81}{4}-27y\right)K_{1/4}
 +(y-3)K_{1/4}^2
 ={}&-\frac{y^6(11y-3)}
 {(y-1)^2(2y-1)^2(3y-1)^2}.
 \end{split}                                               \tag{25}
$$



The left side therefore vanishes through order five, and the equal jet is
singular.  Nevertheless $K_{1/4}/y$ is the Cauchy generating function of
three positive masses, at the positive nodes $1,2,3$, with weights
$1,1,1/4$.  In the coprime representation



$$
K_{1/4}=
 \frac{-y(38y^2-39y+9)}{4(y-1)(2y-1)(3y-1)},              \tag{26}
$$



the ordinary numerator--denominator resultant is $-4096\ne0$, and all
three denominator roots are simple.  This is an exact obstruction to any
proof using only positive Markov nodes, coprimality, interlacing, or an
ordinary resultant.  It does not contradict the special secant conjecture.

## 7. Finite replay and logical boundary

The companion files are

* `scripts/centered_cosh_equal_jet_condensation_barrier_certificate.py`;
* `results/centered_cosh_equal_jet_condensation_barrier_certificate.json`;
* `results/centered_cosh_equal_jet_condensation_barrier_hashes.sha256`.

The replay checks (7), (9), (11), (18), (22), and (24)--(26) exactly.  It
also computes every admissible equal-jet determinant in (4), for both
parities, through $M=120$ modulo the prime (2).  A nonzero modular value
is a rigorous certificate that the corresponding rational determinant is
nonzero.  The scan covers $3600$ $\sigma=1$ rows and $3481$
$\sigma=0$ rows.  Its finite scope is part of the output schema.

What remains unproved is precisely an all-$M,m$ nonvanishing theorem for
the special secant boundary quotients left by (14), (16), and (22).  No
finite scan, generic positivity assertion, or scalar Padé recurrence is
promoted to such a theorem here.
