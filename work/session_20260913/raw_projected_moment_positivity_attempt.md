> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual projected Legendre moments: positive entries, mixed maximal minors

Date: 2026-09-13. Bounded continuation by audit_results. The only tested
degrees are the predeclared n=4 and n=5. No canonical raw triple was
constructed, and no further index search was performed.

**Result:** the actual projected-moment matrix has strictly positive
entries, but its natural-order maximal minors have both signs. At n=4
and n=5, no independent row/column sign changes can make those maximal
minors have a common sign. This is a separate counterexample at the
integrated-moment level; it is not inferred from the previously found
coefficient-minor or collocation counterexamples.

## 1. Exact object and strict entry positivity

Use the actual monic raw Borel polynomials



$$
F_k(x)=\frac{k!}{(2k)!}
\sum_{\substack{0\le d\le k\\d\equiv k\pmod2}}
\binom{k}{(k+d)/2}\frac{(k+d)!}{(d!)^2}x^d,
$$



and the ordinary shifted Legendre polynomials
L_l(x)=P_l(2x-1). The matrix under consideration is



$$
M^{(n)}_{k,l}=\int_0^1F_k(x)L_l(x)\,dx,
\quad n+1\le k\le2n-1,\quad0\le l\le n,
\tag{1}
$$



with rows and columns in increasing degree order.

Rodrigues and l integrations by parts give



$$
\boxed{
M^{(n)}_{k,l}
=\frac1{l!}\int_0^1F_k^{(l)}(x)x^l(1-x)^l\,dx>0.}
\tag{2}
$$



All boundary terms vanish. The strict inequality follows because
k>l and F_k has positive nonzero coefficients in its parity support,
so F_k^(l) is positive on(0,1).

For exact arithmetic, the elementary monomial moment is



$$
\int_0^1x^dL_l(x)\,dx
=
\begin{cases}
\dfrac{(d!)^2}{(d-l)!(d+l+1)!},&d\ge l,\\
0,&d<l.
\end{cases}
$$



Therefore



$$
\boxed{
M^{(n)}_{k,l}
=\frac{k!}{(2k)!}
\sum_{\substack{l\le d\le k\\d\equiv k\pmod2}}
\binom{k}{(k+d)/2}
\frac{(k+d)!}{(d-l)!(d+l+1)!}.}
\tag{3}
$$



The factorial in front of each displayed sum is a multiplicative
factor. Formula(3) was also checked independently by direct integration
of every polynomial pair in the declared test set.

## 2. A complete n=4 counterexample

The rows correspond to k=5,6,7, and the columns to l=0,1,2,3,4.
The exact matrix is



$$
M^{(4)}=
\begin{pmatrix}
2521/15120&23/336&59/6048&1/672&1/30240\\
863/7920&3371/73920&1451/133056&281/332640&1/10080\\
424679/5765760&248903/7413120&85643/12355200&
2833/2471040&409/7413120
\end{pmatrix}.
\tag{4}
$$



For a column set I, write Delta_I=det M[:,I]. Two opposite maximal
minors are



$$
\boxed{
\Delta_{012}=-\frac{11162964481}{5214603018240000}<0,\qquad
\Delta_{013}=\frac{29585981}{208584120729600}>0.}
\tag{5}
$$



Among all ten maximal minors, six are negative and four are positive;
none vanishes.

Even the order-two minors already have both signs. With rows k=5,6,



$$
\det M_{\{5,6\},\{0,1\}}
=\frac{14701}{101606400}>0,
$$




$$
\det M_{\{5,6\},\{0,3\}}
=-\frac{53567}{2514758400}<0.
\tag{6}
$$



The complete order-two enumeration has21 positive and9 negative
minors, with no zero.

Thus entry positivity supplied by Rodrigues does not extend to total
positivity or maximal-minor sign regularity in the actual natural
degree order.

## 3. Row and column sign changes cannot repair the maximal minors

This stronger statement has a short exact certificate, rather than
depending on an exhaustive sign search.

For an r-by-(r+2) matrix with nonzero maximal minors, label the columns
0,...,r+1 and put



$$
e_{ij}=\operatorname{sgn}\Delta_{\{0,\ldots,r+1\}\setminus\{i,j\}}.
$$



If row and column sign changes made every natural-order maximal minor
have one common sign, then there would exist signs c_i and a common
sign tau such that



$$
e_{ij}=\tau c_i c_j.
$$



Indeed a maximal minor acquires the product of all row signs and all
selected column signs; its omitted pair supplies the stated form.
It follows that every triangle product e_ij e_ik e_jk must equal tau.

For (4), the triangle with omitted columns0,1,2 has



$$
e_{01}e_{02}e_{12}
=\operatorname{sgn}(\Delta_{234}\Delta_{134}\Delta_{034})=-1,
$$



whereas the triangle0,1,3 has



$$
e_{01}e_{03}e_{13}
=\operatorname{sgn}(\Delta_{234}\Delta_{124}\Delta_{024})=+1.
\tag{7}
$$



The five required signs are verified by the exact minors



$$
\begin{aligned}
\Delta_{234}&=-1258199/4097188085760000,\\
\Delta_{134}&=-424733/163887523430400,\\
\Delta_{034}&=-2062663/286803166003200,\\
\Delta_{124}&=+3338711/8194376171520000,\\
\Delta_{024}&=-37733323/11472126640128000.
\end{aligned}
$$



The opposite triangle products contradict the necessary sign identity.
Hence no independent row/column sign pattern repairs the maximal
minors in this degree order. Positive row rescaling or passing to
orthonormal shifted Legendre columns also leaves the obstruction
unchanged. Reflection of the integration variable introduces the
column signs (-1)^l and is covered by the same argument.

This statement concerns sign changes and the natural column order.
It does not classify arbitrary permutations or non-diagonal changes
of polynomial basis.

## 4. The second declared degree

At n=5 the matrix has rows k=6,7,8,9 and columns0,...,5.
Every entry is again strictly positive. Its fifteen maximal minors
consist of eight positive and seven negative values, with none zero.
For example,



$$
\Delta_{0123}
=\frac{29497730631318297221}
{422550867697160574468096000000}>0,
$$




$$
\Delta_{0124}
=-\frac{2274417054371032231}
{704251446161934290780160000000}<0.
\tag{8}
$$



The order-two minors have70 positive and20 negative values, with none
zero. The omitted-pair triangle products also have both signs, so no
row/column sign reorientation repairs the natural-order maximal
minors at n=5 either.

These exact counterexamples refute an all-degree positivity or
sign-regularity theorem of the proposed form. They do not prove
failure at every later index or rule out an eventual or separately
selected subsequence property.

## 5. Why the earlier coefficient obstruction was not enough

The earlier inverse-extension note proves that the Cauchy–Binet
expansion of the monomial projected moments has summands of both
signs. That fact does not determine the sign of the sum. Integration
and a change of test basis could in principle have produced a
sign-regular matrix despite those summands.

The present calculation therefore used the actual integrated moments
directly. It establishes the failure after integration and after the
shifted Legendre projection, which the earlier coefficient theorem
did not by itself establish.

For any selected row and column lists, the exact determinant integral is



$$
\det M
=\frac1{r!}\int_{[0,1]^r}
\det[F_{k_i}(x_a)]_{i,a}
\det[L_{l_j}(x_a)]_{j,a}\,dx_1\cdots dx_r.
\tag{9}
$$



Equivalently, by multilinearity and Rodrigues,



$$
\det M
=\frac1{\prod_j l_j!}
\int_{[0,1]^r}
\det[F_{k_i}^{(l_j)}(x_j)]_{i,j}
\prod_jx_j^{l_j}(1-x_j)^{l_j}\,dx_1\cdots dx_r.
\tag{10}
$$



In these formulas the adjacent displayed factors are multiplied.
Individual positive derivative entries in (10) do not give a
nonnegative determinant. Equations(5) and(8) show directly that such
a determinant-positivity conclusion cannot hold for all the selected
actual moments.

## 6. The narrower endpoint problem remains distinct

The high moment block has a two-dimensional kernel in degree at most
n. The actual endpoint matching adds a further row, selecting a line
before the scalar normalization. Its signed cofactors are different
from the maximal minors of the unbordered block tested here.

More explicitly, in the original x coordinate append the actual row
P -> integral(P T_n)+4 beta_n(P) to the high moment matrix in the
L_l basis. Let Delta_l^border be its maximal minor with column l
deleted. A kernel coefficient vector is proportional to



$$
((-1)^l\Delta_l^{\rm border})_{l=0}^n.
$$



Since L_l(1)=1, its endpoint noncancellation ratio is exactly



$$
\boxed{
\frac{|\sum_l(-1)^l\Delta_l^{\rm border}|}
{\sum_l|\Delta_l^{\rm border}|}.}
\tag{11}
$$



The projected-moment counterexample does not estimate this ratio.
A quantitative alternating cofactor pattern or an appropriate
bordered determinant comparison could still control the selected
endpoint. It must use the actual matching row; high-block positivity
alone cannot supply that selection.

## 7. Reproducibility and scope

check_raw_projected_moment_signs.py constructs only the two matrices
n=4,5 from(3). It independently integrates all their polynomial
entries, enumerates every maximal minor and every order-two minor,
and checks all column sign assignments as a supplementary control.
The short proof(7) is the independent mathematical certificate for
the sign-reorientation obstruction.

All exact entries, minors, signs, and omitted-pair triangle products
are saved in raw_projected_moment_signs.json. No floating-point
comparison is used in the counterexamples.
