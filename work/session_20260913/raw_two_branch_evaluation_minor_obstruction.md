> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact leading coefficients and a two-branch evaluation-minor obstruction

Date: 2026-09-13. Original bounded symbolic continuation by audit_results.

The two actual branches have opposite large-node minor orientations
on every adjacent even/odd row pair. Three consecutive rows then
exclude any row/column permutation or diagonal sign pattern making
the unrestricted two-branch evaluation matrix sign regular of order2.
This holds also on sufficiently far actual prolate spectral columns.
It does not settle the signs or conditioning of the growing finite
truncation with both row and spectral indices of order n.

No coefficient/root scan or new canonical degree solve was performed.
All formulas below follow from exact leading polynomial coefficients and
identities in the symbolic index m.

## 1. Rational normalization and the centered operator

Put u=x−1/2 and c_k=2^(−k)binom(2k,k). The exact finite T-module
identity from the two-measure representation becomes



$$
c_kF_k(x)=r_k^{(0)}(T)1+r_k^{(1)}(T)u.             \tag{1}
$$



Indeed v_1=sqrt3 u, and the rational odd branch is
r_k^(1)=sqrt3 p_k^(1)/sqrt(2k+1). Thus(1) has no unrecorded
square-root multiplier. In this variable,



$$
T=(u^2-1/4)D_u^2+2uD_u+u^2+3/4,
$$




$$
Tu^d=u^{d+2}+[d(d+1)+3/4]u^d
                         -\frac{d(d-1)}4u^{d-2}.   \tag{2}
$$



Let A_k=c_k/k! and rho_k=k²(k−1)²/[2(2k−1)]. For k>=2,
the exact leading terms of the actual Borel–Legendre polynomial are



$$
c_kF_k(x)=A_k[x^k+\rho_k x^{k-2}+O(x^{k-4})].     \tag{3}
$$



Here the coefficient of t^(k−2) in the monic Q_k is
k(k−1)/[2(2k−1)]; applying the coefficient Borel transform supplies
the additional factor k(k−1). Formula(3) is a polynomial leading-term
statement; for a missing lower degree the coefficient is zero.

After x=u+1/2, the first four coefficients divided by A_k are



$$
\begin{array}{c|c}
\text{power}&\text{coefficient}\\ \hline
u^k&1\\
u^{k-1}&k/2\\
u^{k-2}&k(k-1)/8+\rho_k\\
u^{k-3}&k(k-1)(k-2)/48+\rho_k(k-2)/2.
\end{array}                                                     \tag{4}
$$



The next coefficient of T^M u^sigma below its leading degree is



$$
T^Mu^\sigma=u^{2M+\sigma}
             +S_{M,\sigma}u^{2M+\sigma-2}+\cdots,
$$




$$
S_{M,\sigma}=\sum_{j=0}^{M-1}[(2j+\sigma)(2j+\sigma+1)+3/4]
=\frac{M[16M^2+(24\sigma-12)M+5]}{12},
\quad \sigma\in\{0,1\}.                            \tag{5}
$$



To obtain this next coefficient one uses the degree-preserving term
in(2) once and the degree-raising term at every other step. A lowering
term in(2) instead creates a deficit of four and cannot contribute.
Thus(5) is valid in every degree, not an extrapolated recurrence fit.

## 2. The first two coefficients of all four branch types

For m>=1 write a_m=A_(2m)>0 and b_m=A_(2m+1)>0. Then



$$
\begin{aligned}
r_{2m}^{(0)}(\xi)
 &=a_m[\xi^m+E_0(m)\xi^{m-1}+\cdots],\\
r_{2m+1}^{(0)}(\xi)
 &=\frac{2m+1}{2}b_m[\xi^m+O_0(m)\xi^{m-1}+\cdots],\\
r_{2m}^{(1)}(\xi)
 &=m a_m[\xi^{m-1}+E_1(m)\xi^{m-2}+\cdots],\\
r_{2m+1}^{(1)}(\xi)
 &=b_m[\xi^m+O_1(m)\xi^{m-1}+\cdots],
\end{aligned}                                                     \tag{6}
$$



with exact rational functions



$$
\boxed{\begin{aligned}
E_0(m)&=\frac{m(16m^3-4m^2-13m+4)}{6(4m-1)},\\
O_0(m)&=\frac{m(16m^3+20m^2-17m-3)}{6(4m+1)},\\
E_1(m)&=\frac{(m-1)(16m^3+4m^2-19m+5)}{6(4m-1)},\\
O_1(m)&=\frac{m(16m^3+28m^2+5m-1)}{6(4m+1)}.
\end{aligned}}                                                     \tag{7}
$$



For m=1 the third polynomial is a constant and E_1(1)=0 denotes
the absent next coefficient; no negative polynomial power is added.

For verification before simplification, the same-parity coefficient
ratio in(4) is
b_match(k)=k(k−1)/8+rho_k. The other-parity ratio, after dividing
by k/2, is
b_opp(k)=(k−1)(k−2)/24+rho_k(k−2)/k. Therefore the four entries
of(7) are exactly



$$
\begin{array}{ll}
E_0=b_{\rm match}(2m)-S_{m,0},&
O_0=b_{\rm opp}(2m+1)-S_{m,0},\\
E_1=b_{\rm opp}(2m)-S_{m-1,1},&
O_1=b_{\rm match}(2m+1)-S_{m,1}.
\end{array}                                                       \tag{8}
$$



These identities, and the factorizations used below, were checked as
rational identities in an indeterminate m. No further branch
polynomials were constructed for that check. The reproducible checker
is check_raw_two_branch_leading_minors.py, with output in
raw_two_branch_leading_minors_checks.json; all checks pass.

## 3. Opposite minor signs in every adjacent even/odd row pair

For i<j, sigma in{0,1}, and real x<y, define the same-branch minor



$$
\mathcal D_{i,j}^{\sigma}(x,y)
=r_i^\sigma(x)r_j^\sigma(y)
                   -r_i^\sigma(y)r_j^\sigma(x).     \tag{9}
$$



Every nonzero branch here is positive for xi>=1 by the independently
reviewed shifted coefficient theorem. The sign of(9) on a sufficiently
far interval is thus the sign of the derivative of r_j/r_i there.

For rows i=2m,j=2m+1, the even branch has equal degrees. The exact
subleading difference is



$$
\boxed{E_0(m)-O_0(m)
=-\frac{m(2m-1)(32m^2+1)}{6(4m-1)(4m+1)}<0.}
\tag{10}
$$



Writing f=r_(2m)^0 and g=r_(2m+1)^0, the Wronskian f g'−f'g
has leading coefficient a_m b_m(2m+1)[E_0−O_0]/2 at degree2m−2.
It is strictly negative for every sufficiently large real xi.
In the odd branch the degrees are m−1 and m, so the same Wronskian
has positive leading coefficient m a_m b_m at degree2m−2.
Consequently, for each m>=1 there exists X_m such that



$$
\boxed{\mathcal D_{2m,2m+1}^0(x,y)<0,
\qquad \mathcal D_{2m,2m+1}^1(x,y)>0
\quad (X_m\le x<y).}                              \tag{11}
$$



The threshold is uniform over x,y in that interval for fixed m:
the Wronskians are fixed nonzero polynomials and have their leading
sign beyond their largest real roots. This is stronger than requiring
y/x to stay bounded away from1, but gives no bound for X_m as m grows.

The next adjacent pair has the reversed pattern. For rows2m+1,2m+2,
the even-branch degrees are m,m+1, giving a positive Wronskian.
The odd branch has equal degrees m, and



$$
\boxed{O_1(m)-E_1(m+1)
=-\frac{m(2m+1)(32m^2+32m+9)}{6(4m+1)(4m+3)}<0.}
\tag{12}
$$



Its Wronskian is eventually negative. Finally, the rows2m,2m+2
have a degree increase of one in each branch, so both Wronskians
are eventually positive. Taking the largest of finitely many
thresholds gives the following table simultaneously:



$$
\begin{array}{c|cc}
\text{row pair}&\sigma=0&\sigma=1\\ \hline
(2m,2m+1)&-&+\\
(2m+1,2m+2)&+&-\\
(2m,2m+2)&+&+
\end{array}
\qquad (X_m\le x<y).                              \tag{13}
$$



The argument uses the degree increase for the unequal-degree pairs,
not a conjectured interlacing of branch roots.

## 4. A permutation- and sign-invariant obstruction

Choose two increasing evaluation nodes in each branch, all above
the common threshold in(13). Retain the three rows2m,2m+1,2m+2.
The ratios of signs of the branch-0 and branch-1 minors, for the
three row pairs, are respectively −,−,+.

An arbitrary permutation of rows reverses both minors for the same
row pair together; it does not change these three sign ratios.
An arbitrary column permutation changes the orientation of the
selected branch-0 pair and the branch-1 pair by fixed factors, hence
multiplies all three ratios by the same sign. The same is true of
arbitrary nonzero diagonal row or column rescaling: row factors
cancel in the comparison, while the ratio of the two column-pair
factors is independent of the row pair.

Therefore the three ratios can never all become positive. It follows
that this 3-by-4 evaluation submatrix cannot have all its nonzero
2-by-2 minors of one sign under any such permutations or rescalings.
In particular the unrestricted two-branch evaluation kernel is
neither totally positive nor sign regular of order2 under a fixed
change of row/column ordering or signs.

This witness occurs in the actual infinite spectral evaluation matrix
as well. For each fixed m, take two sufficiently large even spectral
indices and two sufficiently large odd ones. Their xi_l tend to
infinity and meet the thresholds above. The factors relating r to p
are positive fixed row/branch multipliers, and the actual g_l column
amplitudes in the central-coordinate phase convention are positive.
Thus they do not remove the sign obstruction. The reflected convention
only changes column signs, already allowed in this argument.

This rules out a global order-two sign-regularity theorem on all
spectral columns. It does **not** prove that the specific retained
finite matrix Mtilde, with high rows n+1,...,2n−1 and columns0,...,n,
has such a witness for all sufficiently large n.

## 5. What restricted ordering remains valid

For the single row pair2m,2m+1, a far-tail ordering can make all its
2-by-2 evaluation minors positive: place the branch-0 columns first
in decreasing node order, then branch-1 columns in increasing order.

For within-branch pairs this follows from(11). For a mixed pair,
the ratio of the second row to the first tends to the finite positive
constant (2m+1)b_m/(2a_m) on branch0, while it grows as
(b_m/(m a_m))xi on branch1. Beyond a common threshold every
branch-1 ratio therefore exceeds every branch-0 ratio. This proves
positivity also for the mixed pair in that ordering.

The next adjacent row pair needs the opposite pattern: branch1
first in decreasing order, then branch0 in increasing order. Its
branch-1 ratio tends to a finite constant and its branch-0 ratio
grows linearly. The obstruction in Section4 shows that these
pairwise folded orderings cannot be made into one order valid for
the three-row block. No higher-minor positivity follows from the
valid single-pair ordering.

A different restricted leading structure is visible if only even
rows are kept: the leading branch-1 value is the xi derivative of
the leading branch-0 value, namely m a_m xi^(m−1) versus a_m xi^m.
This resembles confluent polynomial interpolation, but it is not an
exact derivative identity. Equations(7) give the exact mismatch



$$
E_1(m)-\frac{m-1}{m}E_0(m)=\frac{(m-1)(2m-1)}6.
\tag{14}
$$



Thus for m>=2 the polynomial r_(2m)^1−(r_(2m)^0)' has degree m−2
with leading coefficient m a_m(m−1)(2m−1)/6. Likewise the odd rows
have the leading Euler-derivative relation but the exact next mismatch



$$
(m+1/2)O_0(m)-(m-1/2)O_1(m)=\frac{m(m-1)(m+1)}3.
\tag{15}
$$



For m>=2, r_(2m+1)^0−(xi D_xi+1/2)r_(2m+1)^1 therefore has degree
m−1 with leading coefficient b_m m(m−1)(m+1)/3. These formulas
identify precisely the first error in replacing the branches by
value/derivative columns. They do not supply a small error at the
coupled spectral scale, and no confluent Vandermonde determinant is
substituted for the actual matrix.

## 6. Quantitative scope and the remaining finite target

All four subleading ratios in(7) grow as (2/3)m³. The node scale in
the actual growing truncation is xi_l of order n² with m of order n.
Thus the first two terms of(6) are not a uniform asymptotic expansion
on that scale: the subleading-to-leading ratio can itself be of
order n. Using only(6) to assign signs in that coupled regime would
be invalid. Neither the fixed-m threshold X_m nor its growth rate
has been estimated here.

The reviewed relative truncation theorem remains intact: it supplies
an O(n^(−5/2)) row-normalized residual without a finite inverse bound.
The present calculation excludes a global scalar total-positivity
shortcut for that next inverse problem. It leaves open a genuinely
coupled matrix estimate on the actual finite nodes, a structured
factorization allowing the proved alternating branch orientations,
or estimates for particular maximal cofactors. The all-index
shifted positivity and the resulting individual ratio bounds remain
useful inputs but do not force a common sign for these minors.
