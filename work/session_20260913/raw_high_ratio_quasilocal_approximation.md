> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Interlacing high-factor ratios: positive resolvents and quantitative localization

Date: 2026-09-13. Original bounded continuation by audit_computations.

Independent review: `raw_high_ratio_quasilocal_independent_review.md`
passes the residue, approximation, coordinate-tail, numerical-rank
and energy-normalization statements, with the explicit remaining
combined-channel conditioning loss retained.

This note continues the actual `Z_L` factorization and
`raw_high_factor_split_and_parity_rank.md`. It proves an explicit
polynomial approximation for the ratio of the two high factors.
The resulting coordinate-tail and energy-metric bounds are
uniform and require only `O(sqrt n)` exceptional nodes. They yield
a small-rank approximation to the energy projection defect.
The separate angle between the two input channel spaces remains
an explicit condition when converting that approximation into
a statement about their combined image.

## 1. Increase the low cutoff by only O(sqrt n)

Let `n>=2`, `K=K_(2n)`, and write



$$
a_n=-4n^2+3/8,\qquad M_n=2n+3/4,\qquad
\operatorname{spec}K\subset[a_n,M_n].
\tag{1}
$$



Set `b_n=min(n,ceil(2sqrt n))`. Include all nodes indexed
`0,...,b_n` in their respective low parity factors. All remaining
nodes satisfy



$$
\xi_l-M_n\ge l(l+1)-2n\ge2n\quad(l>b_n).
\tag{2}
$$



If one high parity list is longer, move its last root into its
low factor. This adds at most one more exceptional node and
leaves equal high counts. The total exceptional count is at
most `ceil(2sqrt n)+2`, and both original node polynomials
remain unchanged, including their overall signs.

Choose labels `sigma_a,sigma_b` for the remaining lists so that



$$
\alpha_1<\beta_1<\alpha_2<\beta_2<\cdots<\alpha_h<\beta_h,
$$



and define



$$
F_a(t)=\prod_{i=1}^h(\alpha_i-t),\qquad
F_b(t)=\prod_{i=1}^h(\beta_i-t),\qquad R(t)=F_a(t)/F_b(t).
\tag{3}
$$



If no high pair remains, take `R=1`; all approximation and
tail bounds below are then immediate. Otherwise all poles are
at least `2n` above `M_n`. The telescoping interlacing bound
from the preceding note improves to



$$
\boxed{\frac2n\le R(t)\le1\quad(t\in[a_n,M_n]).}
\tag{4}
$$



Indeed the lower bound is
`(alpha_1-M_n)/(beta_h-M_n)`, whose numerator is at least
`2n` and denominator at most `n^2`. The empty case also
satisfies (4) for `n>=2`.

## 2. Exact partial fractions and positive normalized weights

The ratio has the exact representation



$$
\boxed{R(t)=1-\sum_{i=1}^h\frac{c_i}{\beta_i-t},\qquad
c_i=(\beta_i-\alpha_i)
\prod_{j\ne i}\frac{\beta_i-\alpha_j}{\beta_i-\beta_j}>0.}
\tag{5}
$$



For `j<i`, both factors in the corresponding quotient are
positive; for `j>i`, both are negative. This proves the strict
positivity of every residue weight. Evaluation at each simple
pole fixes the coefficients in (5), and the common value one
at infinity fixes the polynomial part. Expansion at infinity
also gives



$$
\sum_i c_i=\sum_i(\beta_i-\alpha_i)
\le\beta_h-\alpha_1.
\tag{6}
$$



More useful than this absolute sum is the normalization



$$
\omega_i=\frac{c_i}{\beta_i-M_n}>0,\qquad
\boxed{\sum_i\omega_i=1-R(M_n)<1.}
\tag{7}
$$



Thus `1-R` is a positive subconvex combination of the
normalized resolvents



$$
f_i(t)=\frac{\beta_i-M_n}{\beta_i-t},\qquad 0<f_i(t)\le1
\quad(t\in[a_n,M_n]).
\tag{8}
$$



Equations (5)--(8) retain the actual roots. They neither replace
the two lists by common nodes nor invoke a scalar total
positivity theorem.

There is also a useful exact sign property in the actual row
basis. Let `D=diag((-1)^k)`. The symmetric matrix `D K D`
has positive entries in both off-diagonal bands and is
irreducible. For every `beta>lambda_max(K)`, its resolvent
`(beta I-D K D)^(-1)` is entrywise strictly positive: add a
sufficiently large scalar multiple of the identity to make
`D K D` nonnegative, and use the convergent nonnegative
Neumann series. Irreducibility makes every entry strictly
positive after sufficiently many powers.

Thus, if a high pair is present, (5) proves



$$
\boxed{D R(K)D\text{ is positive definite and has strictly
negative off-diagonal entries}.}
\tag{8a}
$$



In the standard terminology it is a symmetric nonsingular
M-matrix. Its inverse positivity can also be seen directly
from the reciprocal partial fractions



$$
R(t)^{-1}=1+\sum_i\frac{d_i}{\alpha_i-t},\qquad
d_i=(\beta_i-\alpha_i)
\prod_{j\ne i}\frac{\alpha_i-\beta_j}{\alpha_i-\alpha_j}>0.
\tag{8b}
$$



Every pole in (8b) is above the row spectrum, so
`D R(K)^(-1)D` is entrywise strictly positive. In the empty
case both matrices are simply the identity. These are
actual coordinate sign statements. They do not place all
vectors of the two low-factor Krylov spaces in a common
positive cone; arbitrary polynomial coefficients and the
two distinct seed vectors remain present.

## 3. An explicit uniform polynomial approximation

Put `L_n=M_n-a_n`, `d=L_n/2`, `z(t)=(t-(a_n+M_n)/2)/d`.
For a pole `beta>M_n`, write `z_beta=z(beta)>1`. For any
integer `m>=0`, the expression



$$
q_{m,\beta}(t)=
\frac{1-T_{m+1}(z(t))/T_{m+1}(z_\beta)}{\beta-t}
\tag{9}
$$



is a polynomial of degree at most `m`: its numerator vanishes
at `t=beta`, so the linear division is exact. On the spectral
interval,



$$
\left|\frac{\beta-M_n}{\beta-t}
-(\beta-M_n)q_{m,\beta}(t)\right|
\le\frac1{T_{m+1}(z_\beta)}
\le2e^{-(m+1)\operatorname{arcosh}z_\beta}.
\tag{10}
$$



Here `|T_(m+1)(z(t))|<=1`, while
`T_(m+1)(z_beta)=cosh((m+1)arcosh z_beta)>0`.
By (1), (2), `L_n<=6n^2` and



$$
z_\beta=1+\frac{2(\beta-M_n)}{L_n}
\ge1+\frac2{3n}.
$$



For `0<=u<=1`, `cosh u<=1+u^2`; this follows termwise
from the power series and `cosh 1-1<1`. Consequently



$$
\operatorname{arcosh}z_\beta\ge\sqrt{\frac2{3n}}.
\tag{11}
$$



Use the actual positive weights from (7) to define



$$
p_m(t)=1-\sum_i\omega_i(\beta_i-M_n)q_{m,\beta_i}(t).
\tag{12}
$$



It has degree at most `m`; (7), (10), and (11) prove



$$
\boxed{
\max_{t\in[a_n,M_n]}|R(t)-p_m(t)|
\le\varepsilon_{m,n}:=
2\exp\left(-(m+1)\sqrt{\frac2{3n}}\right).}
\tag{13}
$$



There is no residue-sum growth hidden in this estimate, because
the normalized weights sum to less than one. In particular,
for every fixed `A>0`, degree



$$
m+1\ge\sqrt{3n/2}\,\log(2n^A)
\tag{14}
$$



gives error at most `n^(-A)`. This degree is
`O_A(sqrt n log n)`. If the error is at most `1/n`, (4)
also implies `p_m(t)>=1/n` on the spectral interval, so the
approximating polynomial is certainly nonzero.

## 4. Coordinate tails and the exact F_b energy norm

Functional calculus in (13) gives



$$
\|R(K)-p_m(K)\|\le\varepsilon_{m,n}.
\tag{15}
$$



Since `K` has bandwidth two, a vector `w` supported in
coordinates `0,...,s` has `p_m(K)w` supported through
coordinate `s+2m`, with truncation at the finite endpoint.
Therefore



$$
\boxed{
\|P_{>s+2m}R(K)w\|
\le\varepsilon_{m,n}\|w\|.}
\tag{16}
$$



More generally (16) is an operator-norm bound from the entire
coordinate prefix to its distant tail, not just a statement
about a selected vector. This is consistent with the exact
large cross-cut rank proved previously: full exact rank and
small singular values in a distant tail are different facts.

There is also a direct numerical-rank bound across *any*
coordinate cut. The cross block of `p_m(K)` has rank at
most `2m` by its bandwidth. Compressing (15) and using this
rank approximation gives



$$
\boxed{\sigma_{2m+1}\bigl(R(K)[L,H]\bigr)
\le\varepsilon_{m,n}.}
\tag{16a}
$$



As usual the statement is empty if the index exceeds the
block size. Thus the full cross block of the ratio, not just
the distant portion of its columns, has numerical rank
`O_A(sqrt n log n)` to error `n^(-A)`.

The inverse ratio has the same localization with an explicit
polynomial loss. By (4), the positive normalized weights in
(8b) sum to
`R(M_n)^(-1)-1<=n/2-1`. Applying the very same normalized
resolvent polynomials, now at the poles `alpha_i`, constructs
a degree-`m` polynomial `tilde p_m` with



$$
\|R(K)^{-1}-\widetilde p_m(K)\|
\le(n/2)\varepsilon_{m,n}.
\tag{16b}
$$



The coordinate-tail and cross-block bounds (16), (16a) follow
for `R(K)^(-1)` with that additional factor `n/2`.

Let `F=F_b(K)>0` and use the energy norm
`||w||_F=||F^(1/2)w||`. All three operators `F,R(K),p_m(K)`
commute, so



$$
\boxed{\|(R(K)-p_m(K))w\|_F
\le\varepsilon_{m,n}\|w\|_F.}
\tag{17}
$$



There is no factor `cond(F)` in (17). Ordinary coordinate
projection need not be a contraction in this norm. The
corresponding correct energy statement uses the orthogonal
projection onto `F^(1/2)` of the enlarged coordinate prefix:
the distance of `F^(1/2)R(K)w` from that subspace is at most
the right side of (17).

## 5. Application to the two actual Krylov families

Let `L_sigma` now denote the low factor after the enlarged
cutoff and optional one-root transfer in Section 1, and write
`ell_sigma=deg L_sigma`. The original domain dimensions remain
`d_sigma=n-m_sigma`, where `m_sigma` counts all nodes of that
parity. Put



$$
W_\sigma=[L_\sigma(K)K^jv_\sigma]_{0\le j<d_\sigma}.
\tag{18}
$$



Their columns are independent by the same triangular
vector-polynomial argument as before. Up to their fixed column
signs and ordering, the full vanishing matrix and its retained
block are



$$
Z=F[\,R(K)W_a,\ W_b\,],\qquad Z_L=P_LZ.
\tag{19}
$$



This expression preserves both original parity polynomials.
Replace only the ratio by `p_m` and set



$$
\widetilde X=[p_m(K)W_a,W_b].
\tag{20}
$$



The columns of (20) lie in the first `n+1+r` coordinates,
where it is sufficient to take



$$
r=\min\{n-1,\ 2(m+\max_\sigma\ell_\sigma)\}.
\tag{21}
$$



For example their maximal index in channel `sigma_a` is at
most `2(m+ell_a+d_a-1)+sigma_a`. The unmultiplied other
channel has the same bound without `2m`; direct substitution
of the two parity domain dimensions gives (21). If the
expression reaches the full finite dimension, the displayed
cap merely gives the whole space.

For fixed `A` and the choice (14), `r=O_A(sqrt n log n)`.
Eventually the maximal indices are strictly below `2n`, so
the polynomial coefficient identities are exact and (20)
has independent columns whenever `p_m` is nonzero. Its two
components are still the different-channel polynomials
`p_m L_a u_a` and `L_b u_b`; they cannot cancel each other.

## 6. An unconditional small-rank approximation to the normalized energy defect

The following normalization makes the remaining loss explicit.
Let `X_a=R(K)W_a`, `X_b=W_b`, and form the individual
positive Gram matrices



$$
G_a=X_a^TFX_a,\qquad G_b=W_b^TFW_b.
$$



Define



$$
E_a=F^{1/2}X_aG_a^{-1/2},\quad
E_b=F^{1/2}W_bG_b^{-1/2},\qquad E=[E_a,E_b].
\tag{22}
$$



Each channel separately has orthonormal columns. Their
juxtaposition is not assumed orthonormal or uniformly
well-conditioned. Replace `R` by `p_m` only in `E_a` to
obtain `tilde E`. Since `R(K)>=2I/n` and commutes with `F`,



$$
W_a^TFW_a\preceq\frac{n^2}{4}G_a.
$$



Together with (17), this proves



$$
\boxed{\|E-\widetilde E\|\le\frac n2\varepsilon_{m,n}.}
\tag{23}
$$



Let `mathcal L` be the first `n+1` coordinate space and
`mathcal U` its enlargement from (21). Let `Pi_L^F,Pi_U^F`
be the ordinary orthogonal projections onto
`F^(1/2)mathcal L` and `F^(1/2)mathcal U`. These spaces
are nested and their dimension difference is `r`.
The columns of `tilde E` belong to the latter space, so



$$
\operatorname{rank}\bigl((I-\Pi_L^F)\widetilde E\bigr)\le r.
$$



Consequently the actual energy defect satisfies



$$
\boxed{
\sigma_{r+1}\bigl((I-\Pi_L^F)E\bigr)
\le\frac n2\varepsilon_{m,n},}
\tag{24}
$$



where singular values are in decreasing order; the same bound
holds for every subsequent singular value. If `r` exceeds the
number of columns the assertion is empty. This is a proved
small numerical-rank statement with all factors in its norm
specified. In particular polynomial accuracy uses only
`O(sqrt n log n)` exceptional directions in this normalization.

## 7. The remaining channel-angle loss and the conditional rank reduction

The full unprojected vanishing matrix is known to have
independent columns. Since `F` and the individual Gram
normalizations are invertible, `E` also has full column rank.
Nevertheless its smallest singular value



$$
\delta_n=\sigma_{\min}(E)>0
\tag{25}
$$



has not been bounded quantitatively. In this normalization it
is exactly



$$
\delta_n^2=1-\|E_a^TE_b\|,
\tag{26}
$$



when both channels are nonempty; an empty channel has
`delta_n=1`. Thus (25) is a precise angle between the two
*unprojected, energy-weighted* channel spaces.

The orthonormal basis of their combined image is
`O=E(E^TE)^(-1/2)`. Right multiplication by this final
normalization gives the rigorous bound



$$
\boxed{
\sigma_{r+1}\bigl((I-\Pi_L^F)O\bigr)
\le\frac{n\varepsilon_{m,n}}{2\delta_n}.}
\tag{27}
$$



These singular values are the principal-angle sines to the
retained energy space. Hence if the right side is `eta<1`,
at least `n-1-r` singular values of the corresponding
retained projection are at least `sqrt(1-eta^2)`.

To identify it with the actual matrix, let `A=F[L,L]>0`
and `B=diag(G_a^(1/2),G_b^(1/2))`. An orthonormal basis
of the retained energy space is `F^(1/2)P_L^T A^(-1/2)`.
Its pairing with `O` is exactly



$$
A^{-1/2}Z_LB^{-1}(E^TE)^{-1/2},
\tag{28}
$$



apart from the already specified harmless signs and column
ordering. All preconditioners in (28) are invertible, so in
particular its rank is the rank of the actual `Z_L`.

An eventual bound `delta_n>=n^(-B_0)` would therefore permit
choosing `A>B_0+1` in (14), giving an actual rank defect at
most `O_(B_0)(sqrt n log n)` and a near-unit lower bound on
all but that many singular values in the normalization (28).
That polynomial channel-angle hypothesis is **not proved**.
The exact bounds (23)--(24) hold without it, while the
conversion to the orthonormal combined image correctly incurs
the factor `1/delta_n` in (27).

## 8. What is gained and what cannot yet be discarded

The positive partial fractions turn the high-factor ratio
into a quantitatively local operator on the scale `sqrt n`.
This explains how a polynomially accurate support reduction
can coexist with the full exact cross-cut ranks in the
preceding note. Moving `O(sqrt n)` roots is essential for
this useful scale: the old guaranteed gap only two against
an interval of length `O(n^2)` would give degree of order
`n log(1/epsilon)` with the same construction.

The energy estimate avoids a gratuitous condition loss from
`F_b`. It does not make the metric disappear. Returning to an
unweighted singular-value bound requires the actual row and
column factors in (28). Returning to the physical finite
kernel angle also requires the amplitude-weighted cardinal
matrix `S=Y_low diag(g_l)` from the multipoint reduction.
Neither its factors nor the channel-angle loss (25) may be
omitted.

No mixed-node determinant lower bound, complete rank theorem,
primitive shrinking theorem, or irrationality conclusion is
asserted. The new quantitative target is (25)--(27): a bound
for one explicit unprojected channel angle would turn the
proved ratio localization into a substantially smaller
remaining exceptional-direction problem.
