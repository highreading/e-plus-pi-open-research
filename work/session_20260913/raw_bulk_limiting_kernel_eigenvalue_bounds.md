> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Many-node bounds for the actual limiting bulk kernel

Date: 2026-09-13. Original bounded continuation by audit_computations.

This note studies the explicit limiting kernel in
`raw_actual_branch_column_asymptotics.md` on an increasing number
of actual bulk nodes. It proves that its least eigenvalue is
exponentially small on the scale `exp(-Theta(n))`, whereas its
determinant has scale `exp(-Theta(n^2))` when the number of nodes
is proportional to `n`. The lower eigenvalue bound uses the
exact Cauchy inverse, rather than losing an unnecessary factor
of `n` in the exponent by using only a determinant bound.

The exact perturbation accuracy needed to transfer the result to
the actual high kernel is stated below. The currently proved
unquantified `o(1)` convergence does not meet that requirement.
No new degree, node, or numerical solve is used.

Continuation update: `raw_quantitative_fixed_cut_transport.md` has
since proved, and received independent review of, the uniform rate
`O(log(n)/n)`. The conditional sparse regime in Section 8 is now
proved for the actual matrix in
`raw_actual_sparse_bulk_matrix_theorem.md`. The unquantified-rate
wording below records the state at this note's derivation; the
full-density stability obstruction remains after that upgrade.

## 1. Actual bulk nodes and explicit fixed constants

Fix `0<alpha<beta<=1`. Select any increasing list of distinct
indices



$$
\lceil\alpha n\rceil\le l_1<\cdots<l_m
\le\lfloor\beta n\rfloor,
\qquad c_i=\frac{\xi_{l_i}}{(2n)^2},\qquad
\sigma_i=l_i\bmod2.
\tag{1}
$$



Only nonempty selections are considered. Set



$$
c_- =\alpha^2/4,\qquad c_+=(\beta+1)^2/4,
\qquad q(c)=(\sqrt{c+1}-\sqrt c)^2,
$$





$$
q_-=q(c_+),\qquad q_+=q(c_-),\qquad
\tau=\frac{\alpha q_-}{2\sqrt{c_+(c_++1)}}.
\tag{2}
$$



These constants satisfy `0<q_-<q_+<1` and `tau>0`.
The actual node bounds imply `c_-<=c_i<=c_+`. For the upper
bound, `xi_l<=l(l+1)+1` gives
`4c_i<=beta^2+beta/n+1/n^2<=(beta+1)^2`.

For two selected indices `l_i<l_j`, the same bounds give



$$
\xi_{l_j}-\xi_{l_i}
\ge(l_j-l_i)(l_i+l_j+1)-1/4
\ge2\alpha n(l_j-l_i).
$$



Also `-q'(c)=q(c)/sqrt(c(c+1))`, which is at least
`q_-/sqrt(c_+(c_++1))` on the chosen interval. Consequently



$$
\boxed{q_-\le q_i:=q(c_i)\le q_+,\qquad
|q_i-q_j|\ge\frac\tau n|i-j|.}
\tag{3}
$$



This spacing statement uses the actual nodes and permits skipped
indices. Their reversed ordering in `q` causes no sign problem
in any squared determinant below.

## 2. The actual parity vector columns stay in the kernel

The limiting column vectors, in the symmetric normalization, are



$$
\begin{aligned}
a_0(c)&=\sqrt2(c+1)^{-1/4}
\begin{pmatrix}q(c)^{1/4}\cosh\eta(c)\\
q(c)^{-1/4}\sinh\eta(c)\end{pmatrix},\\
a_1(c)&=\frac{\sqrt6}{3}(c+1)^{-1/4}
\begin{pmatrix}q(c)^{1/4}\sinh\eta(c)\\
q(c)^{-1/4}\cosh\eta(c)\end{pmatrix},
\qquad \eta(c)=\frac1{2\sqrt c}.
\end{aligned}
\tag{4}
$$



Define the actual selected limiting matrix



$$
\mathcal L_{ij}
=\frac{q_iq_j}{1-q_iq_j}
\,a_{\sigma_i}(c_i)^Ta_{\sigma_j}(c_j).
\tag{5}
$$



Both vector components are positive on the interval. The
following explicit constants suffice:



$$
a_*=(c_++1)^{-1/4}q_-^{1/4}
\min\left\{\sqrt2,\frac{\sqrt6}{3}
\sinh\frac1{2\sqrt{c_+}}\right\}>0,
$$





$$
A_*=\sqrt2\,q_-^{-1/4}
\exp\frac1{2\sqrt{c_-}}.
\tag{6}
$$



For either parity, the first component is at least `a_*`, and
the vector norm is at most `A_*`. The latter follows by
bounding `q^(1/4)` and `q^(-1/4)` by `q_-^(-1/4)`, the
scalar `(c+1)^(-1/4)` by one, and
`sqrt(cosh^2 eta+sinh^2 eta)` by `exp(eta)`.

Let



$$
\mathcal K_{ij}=\frac{q_iq_j}{1-q_iq_j}.
\tag{7}
$$



Writing the two components of (4) as diagonal matrices `D_0,D_1`
gives the exact Gram decomposition



$$
\boxed{\mathcal L=D_0\mathcal K D_0+D_1\mathcal K D_1,
\qquad \lambda_{\min}(\mathcal L)
\ge a_*^2\lambda_{\min}(\mathcal K).}
\tag{8}
$$



The lower bound follows from the first term and the minimum
diagonal entry of `D_0`. The other component is retained as a
positive semidefinite term, not replaced by a scalar constant.
Thus the proof applies to every actual parity pattern in (1).

## 3. Exact scalar determinant and inverse diagonal

For distinct `q_i` in `(0,1)`, the Cauchy determinant is



$$
\det\mathcal K
=\frac{\displaystyle\prod_i q_i^2
\prod_{i<j}(q_i-q_j)^2}
{\displaystyle\prod_{i,j}(1-q_iq_j)}>0.
\tag{9}
$$



One obtains this by writing the matrix `1/(1-q_iq_j)` as
a row-scaled Cauchy matrix with row variables `1/q_i` and
column variables `q_j`; the powers of `q_i` cancel except
for the two diagonal factors in (7). Alternatively clearing
denominators makes the numerator alternating in the two
sets of variables, and its degree and the one-point case
give the same identity.

Taking the ratio of the principal cofactor to (9) gives



$$
\boxed{
(\mathcal K^{-1})_{ii}
=q_i^{-2}(1-q_i^2)
\prod_{j\ne i}
\left(\frac{1-q_iq_j}{q_i-q_j}\right)^2.}
\tag{10}
$$



This identity avoids estimating the inverse by dividing a
coarse matrix norm by the small determinant.

Put `r=m-1`. From (3),



$$
\prod_{j\ne i}|q_i-q_j|
\ge(\tau/n)^r(i-1)!(m-i)!.
$$



Since `1-q_iq_j<=1`, summing (10) and using the binomial
identity `sum_(j=0)^r binom(r,j)^2=binom(2r,r)` yields



$$
\operatorname{tr}(\mathcal K^{-1})
\le q_-^{-2}(n/\tau)^{2r}
\frac{\binom{2r}{r}}{(r!)^2}.
$$



For a positive definite matrix, its largest inverse eigenvalue
is at most its inverse trace. Therefore



$$
\boxed{
\lambda_{\min}(\mathcal K)
\ge q_-^2(\tau/n)^{2r}\frac{(r!)^2}{\binom{2r}{r}}.}
\tag{11}
$$



For `r>=1`, the elementary bounds `r!>=(r/e)^r` and
`binom(2r,r)<=4^r` also give



$$
\lambda_{\min}(\mathcal K)
\ge q_-^2\left(\frac{\tau r}{2en}\right)^{2r}.
\tag{12}
$$



For `m=1`, (11) reads `lambda_min>=q_-^2`, with the usual
empty-product convention, and is valid directly.

Combining with (8), define the explicit lower bound



$$
\boxed{
b_{m,n}:=a_*^2q_-^2(\tau/n)^{2(m-1)}
\frac{((m-1)!)^2}{\binom{2m-2}{m-1}},\qquad
\lambda_{\min}(\mathcal L)\ge b_{m,n}>0.}
\tag{13}
$$



## 4. The least eigenvalue really has exponential, not quadratic-exponential, scale

The positive feature expansion of the full vector kernel is



$$
\mathcal L_{ij}
=\sum_{s\ge1}\sum_{u=0}^1
\bigl(q_i^s[a_{\sigma_i}(c_i)]_u\bigr)
\bigl(q_j^s[a_{\sigma_j}(c_j)]_u\bigr).
\tag{14}
$$



Truncating at `s=h` has rank at most `2h`. Its positive
semidefinite tail has norm at most its trace, hence at most



$$
\frac{mA_*^2q_+^{2(h+1)}}{1-q_+^2}.
\tag{15}
$$



Choose `h=floor((m-1)/2)`, so the truncation has rank below
`m`. The min--max principle gives



$$
\boxed{
\lambda_{\min}(\mathcal L)
\le\frac{mA_*^2}{1-q_+^2}\,q_+^m.}
\tag{16}
$$



In particular exponential smallness cannot be avoided even
though both vector components have been kept.

Suppose now the number of selected nodes is at least `rho n`
for a fixed `rho>0`, as it is for the complete bulk interval
with sufficiently large `n`. Then `r>=rho n/2` eventually
and `r<=n`. Formula (12), followed by (8), bounds the least
eigenvalue below by `exp(-C n)` with constants depending
only on `alpha,beta,rho`; (16) bounds it above by
`exp(-c n)` after a possible change of constants. Thus



$$
\boxed{e^{-C n}\le\lambda_{\min}(\mathcal L)
\le e^{-c n}\quad(m\asymp n),}
\tag{17}
$$



for some positive fixed `c,C` and all sufficiently large `n`.
Prefactors in (13), (16) have been absorbed only in this
asymptotic display; their explicit forms remain available.
The trace bound gives `||mathcal L||<=m A_*^2q_+^2/(1-q_+^2)`.
Thus its ordinary condition number also has exponential
order on such a bulk set.

## 5. Determinants have a different scale

Equation (9) and the spacing in (3) give the explicit bound



$$
\det\mathcal L
\ge a_*^{2m}\det\mathcal K
\ge a_*^{2m}q_-^{2m}(\tau/n)^{m(m-1)}
\left(\prod_{j=1}^{m-1}j!\right)^2.
\tag{18}
$$



The first inequality is determinant monotonicity for positive
definite matrices applied to the first Gram term in (8).
The denominator of (9) is at most one, and the product of
integer spacings is `prod_(j=1)^(m-1) j!`.

For a matching scale in the other direction, list the
eigenvalues of `mathcal L` in decreasing order. The rank
truncation argument (15) gives, for every `1<=j<=m`,



$$
\lambda_j(\mathcal L)
\le C_*m\,q_+^{2\lceil j/2\rceil},
\qquad C_*=A_*^2/(1-q_+^2).
$$



Therefore



$$
\det\mathcal L
\le(C_*m)^m q_+^{2\sum_{j=1}^m\lceil j/2\rceil}.
\tag{19}
$$



For `m` proportional to `n`, (13) already implies the
lower bound `exp(-C n^2)` after multiplication of the
eigenvalue bounds. The exponent in (19) is of order `m^2`,
and its positive `m log(C_*m)` term is smaller order. Thus



$$
\boxed{e^{-C' n^2}\le\det\mathcal L
\le e^{-c' n^2}\quad(m\asymp n).}
\tag{20}
$$



This explains the distinction requested here: the determinant
is quadratically exponential, but the smallest eigenvalue is
only linearly exponential in the bulk size. A determinant-only
inverse estimate would lose a full factor of `n` in the
exponent and demand an unnecessarily strong error bound.

## 6. Exact normalization of the actual high kernel

Let `G_actual` be the Gram matrix of the prescribed high-row
columns at the selected indices in (1):



$$
(G_{\rm actual})_{ij}
=g_{l_i}g_{l_j}
\sum_{k=n+1}^{2n-1}
p_k^{(\sigma_i)}(\xi_{l_i})p_k^{(\sigma_j)}(\xi_{l_j}).
$$



For the even upper cut `2n`, retain the exact scalar
`s_(2n)(x)=Lambda_(2n,2)(x)(2n)^(-1/2)` and set



$$
d_i=g_{l_i}s_{2n}(\xi_{l_i})\xi_{l_i}^{p_{\sigma_i}},
\qquad p_0=3/2,\quad p_1=1,\qquad
\widehat G=\operatorname{diag}(d_i)^{-1}
G_{\rm actual}\operatorname{diag}(d_i)^{-1}.
\tag{21}
$$



Every `d_i` is positive on these actual real nodes. The
previously proved kernel convergence says that the entries
of `hat G` converge uniformly to (5) on this bulk domain.
It currently supplies only an unquantified error



$$
\max_{i,j}|\widehat G_{ij}-\mathcal L_{ij}|\le\epsilon_n,
\qquad \epsilon_n=o(1).
\tag{22}
$$



The actual amplitudes, scalar products, unequal column powers,
and selected parities have all been kept in (21). In
particular no factorial amplitude is silently folded into
the limiting constant.

## 7. An honest stability threshold

For a real symmetric matrix satisfying an entrywise error
bound as in (22), its operator error is at most `m epsilon_n`.
Weyl's inequality and (13) therefore give the sufficient
condition



$$
\boxed{
\epsilon_n\le\frac{b_{m,n}}{2m}
\quad\Longrightarrow\quad
\lambda_{\min}(\widehat G)\ge\frac{b_{m,n}}2>0.}
\tag{23}
$$



For the normalized actual feature matrix this gives a
smallest singular value at least `sqrt(b_(m,n)/2)`.
For the original feature matrix its diagonal column scaling
in (21) must be restored; one safe bound incurs
`min_i d_i`. This is a bound for the selected bulk columns,
not a claim about all columns down to index zero.

More quantitatively, if



$$
\eta_n=m\epsilon_n/b_{m,n}<1,
$$



then



$$
(1-\eta_n)\mathcal L\preceq\widehat G
\preceq(1+\eta_n)\mathcal L.
\tag{24}
$$



Thus the determinant is between `(1-eta_n)^m` and
`(1+eta_n)^m` times the limiting determinant. For
`eta_n<=1/2`,



$$
\left|\log\frac{\det\widehat G}{\det\mathcal L}\right|
\le2m\eta_n\le\frac{2m^2\epsilon_n}{b_{m,n}}.
\tag{25}
$$



Relative determinant convergence would follow, for example,
from `m^2 epsilon_n/b_(m,n)->0`. Both that requirement and
the rank threshold (23) have exponential scale in `n`, not
the stronger scale `exp(-C n^2)` suggested by a crude
determinant-only argument.

The current `o(1)` convergence in (22) gives no comparison
with these exponentially small quantities. Even positive
semidefiniteness by itself does not supply such stability:
subtracting the least eigenvalue times its unit eigenvector
projector from `mathcal L` gives a positive semidefinite
singular matrix at operator distance exactly that eigenvalue.
By (16), such a rank-destroying error can itself be
exponentially small. This is a matrix stability observation,
not a proposed counterexample for the actual kernel.

A structured error theorem might use more than the norm
bound (22). Without one, the explicit missing accuracy is
(23), with (25) for relative determinants. The exponentially
small lower-cut contribution alone does not resolve this:
the total error still contains the unquantified fixed-cut
column error, and even an exponential rate would need a
constant strong enough for (23).

## 8. A quantitative transfer regime for sparse, well-spaced selections

There is a useful intermediate regime that requires less accuracy
than the full-density case. This paragraph is conditional on an
actual uniform entrywise rate `epsilon_n=O(log n/n)`; that rate
is not proved in this note and is stronger than the currently
used unquantified convergence.

Choose `m>=2` indices approximately equally spaced from
`ceil(alpha n)` to `floor(beta n)`. Explicitly, with
`a=ceil(alpha n)`, `b=floor(beta n)`, set



$$
l_i=a+\left\lfloor\frac{(i-1)(b-a)}{m-1}\right\rfloor,
\qquad 1\le i\le m.
\tag{26}
$$



For sufficiently large `n` and `m-1<=(b-a)/2`, their
differences are at least
`(beta-alpha)n|i-j|/(4m)`. To see this, subtract the two
floors and use `(b-a)/(m-1)-1>=(b-a)/(2(m-1))`, then
`b-a>=(beta-alpha)n/2`. Thus (3) improves to



$$
|q_i-q_j|\ge\frac{\tau_s}{m}|i-j|,
\qquad \tau_s=\tau(\beta-\alpha)/4.
\tag{27}
$$



The same exact inverse argument now gives



$$
\lambda_{\min}(\mathcal L)
\ge a_*^2q_-^2(\tau_s/m)^{2r}
\frac{(r!)^2}{\binom{2r}{r}}
\ge a_*^2q_-^2\left(\frac{\tau_s}{4e}\right)^{2m},
\quad r=m-1.
\tag{28}
$$



Here `r/m>=1/2`; also `tau_s/(4e)<1`, as is evident
from its definition and the interval spacing. Put
`C_s=-2log(tau_s/(4e))>0`. For any fixed
`0<kappa<1/C_s`, taking `m=floor(kappa log n)` gives



$$
\lambda_{\min}(\mathcal L)\ge c\,n^{-C_s\kappa},
\qquad
\frac{m^2\epsilon_n}{\lambda_{\min}(\mathcal L)}
=O\bigl((\log n)^3 n^{-1+C_s\kappa}\bigr)\longrightarrow0.
\tag{29}
$$



Therefore the hypothesized rate would prove positive definiteness
of the actual normalized Gram on this logarithmically growing
selection, and relative determinant convergence by (25).
Restoring its nonzero column scales proves independence of those
actual high-row columns. The result would not cover a consecutive
cluster of the same number of nodes: such a cluster still has
spacing of order `1/n`, rather than the improved `1/m` used
in (27). It also would not settle the full-density problem.

## 9. Scope of the new many-node result

The limiting matrix is now quantitatively positive definite
for arbitrarily many actual bulk nodes, with explicit
determinant and least-eigenvalue bounds and the true parity
vector columns. This strengthens the prior fixed-size
positivity statement.

What remains unproved is the accuracy needed to transfer
that many-node bound to the actual high-row matrix, and
control of nodes whose scaled parameter tends to zero.
Neither a full high-kernel rank theorem nor the final
amplitude-weighted cardinal angle follows from (17) alone.
No statement about the primitive denominator or irrationality
is inferred.
