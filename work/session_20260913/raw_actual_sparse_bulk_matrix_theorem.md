> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An actual sparse bulk high-matrix theorem

Date: 2026-09-13. Original continuation by audit_computations.

Independent root review passes in `raw_actual_sparse_bulk_root_review.md`.

This note discharges the conditional sparse regime in Section 8 of
`raw_bulk_limiting_kernel_eigenvalue_bounds.md`. Its input is the
now independently reviewed uniform kernel error `O(log(n)/n)` in
`raw_quantitative_fixed_cut_transport.md`. The many-node Cauchy
bounds were independently reviewed in
`raw_bulk_limiting_kernel_independent_review.md`; the rate was
reviewed in `raw_quantitative_fixed_cut_independent_review.md`.

The conclusion concerns the actual high rows, actual spectral
nodes, and actual amplitudes. It proves quantitative independence
for a well-spaced logarithmically growing selection of columns,
and a relative determinant asymptotic in the exact normalization.
It does not assert full high-row rank or endpoint concentration.

## 1. Fixed constants and actual selected nodes

Fix `0<alpha<beta<=1`. Write



$$
c_-=\alpha^2/4,\qquad c_+=(\beta+1)^2/4,\qquad
q(c)=(\sqrt{c+1}-\sqrt c)^2,
$$





$$
q_-=q(c_+),\quad q_+=q(c_-),\quad
\tau=\frac{\alpha q_-}{2\sqrt{c_+(c_++1)}},\qquad
\tau_s=\tau(\beta-\alpha)/4.
\tag{1}
$$



For either parity use the exact limiting column vectors



$$
\begin{aligned}
a_0(c)&=\sqrt2(c+1)^{-1/4}
\begin{pmatrix}q(c)^{1/4}\cosh\eta(c)\\
q(c)^{-1/4}\sinh\eta(c)\end{pmatrix},\\
a_1(c)&=\frac{\sqrt6}{3}(c+1)^{-1/4}
\begin{pmatrix}q(c)^{1/4}\sinh\eta(c)\\
q(c)^{-1/4}\cosh\eta(c)\end{pmatrix},\qquad
\eta(c)=\frac1{2\sqrt c}.
\end{aligned}
\tag{2}
$$



The following constants bound the first component below and
the full vector norm above, for both parities on `[c_-,c_+]`:



$$
a_*=(c_++1)^{-1/4}q_-^{1/4}
\min\left\{\sqrt2,\frac{\sqrt6}{3}
\sinh\frac1{2\sqrt{c_+}}\right\}>0,
\qquad
A_*=\sqrt2 q_-^{-1/4}\exp\frac1{2\sqrt{c_-}}.
\tag{3}
$$



Set



$$
c_*=a_*^2q_-^2,\qquad
C_s=-2\log\frac{\tau_s}{4e}>0.
\tag{4}
$$



Choose any fixed `0<kappa<1/C_s`, and put



$$
m=m_n=\lfloor\kappa\log n\rfloor,\qquad
\theta=C_s\kappa<1.
\tag{5}
$$



All subsequent assertions are for sufficiently large integer `n`,
so `2<=m<=n-1`. With `a=ceil(alpha n)` and `b=floor(beta n)`,
select the actual integer indices



$$
l_i=a+\left\lfloor\frac{(i-1)(b-a)}{m-1}\right\rfloor,
\quad 1\le i\le m,\qquad
c_i=\frac{\xi_{l_i}}{(2n)^2},\quad
\sigma_i=l_i\bmod2,\quad q_i=q(c_i).
\tag{6}
$$



The established eigenvalue enclosures
`l(l+1)+3/4<=xi_l<=l(l+1)+1` imply
`c_i in [c_-,c_+]`. Since `m=O(log n)`, eventually
`m-1<=(b-a)/2`. For `j>i`, subtracting floors gives



$$
l_j-l_i\ge(j-i)\left(\frac{b-a}{m-1}-1\right)
\ge\frac{(\beta-\alpha)n}{4m}(j-i).
$$



Here the second inequality uses `b-a>=(beta-alpha)n/2` for
large `n`. The actual spectral gap and the derivative of `q`
then give the uniform separation



$$
\boxed{|q_i-q_j|\ge\frac{\tau_s}{m}|i-j|.}
\tag{7}
$$



No parity restriction or replacement of actual nodes by a
continuum grid enters (6)-(7).

## 2. A polynomial lower bound for the selected limiting Gram

Define



$$
\mathcal L_{ij}=
\frac{q_iq_j}{1-q_iq_j}\,
a_{\sigma_i}(c_i)^Ta_{\sigma_j}(c_j).
\tag{8}
$$



For `K_ij=q_iq_j/(1-q_iq_j)`, the exact two-component
decomposition `L=D_0 K D_0+D_1 K D_1` and the first component
bound in (3) imply `lambda_min(L)>=a_*^2 lambda_min(K)`.
The exact inverse diagonal is



$$
(K^{-1})_{ii}=q_i^{-2}(1-q_i^2)
\prod_{j\ne i}\left(\frac{1-q_iq_j}{q_i-q_j}\right)^2.
\tag{9}
$$



Writing `r=m-1`, (7), the inverse trace, and
`sum_(j=0)^r binom(r,j)^2=binom(2r,r)` yield



$$
\lambda_{\min}(\mathcal L)
\ge c_*\left(\frac{\tau_s}{m}\right)^{2r}
\frac{(r!)^2}{\binom{2r}{r}}
\ge c_*\left(\frac{\tau_s}{4e}\right)^{2m}
\ge c_*n^{-\theta}.
\tag{10}
$$



The middle inequality follows from `r!>=(r/e)^r`,
`binom(2r,r)<=4^r`, `r/m>=1/2`, and `tau_s/(4e)<1`.
The final inequality uses `m<=kappa log n`. Also the feature
expansion or the diagonal bound gives



$$
\|\mathcal L\|\le C_Lm,\qquad
C_L=\frac{A_*^2q_+^2}{1-q_+^2}.
\tag{11}
$$



Both actual parity components remain present in (8).

## 3. Exact normalization of the actual high columns

Use the symmetric polynomial branches `p_k^(sigma)` and the
positive spectral phase of `g_l` from the accepted branch and
amplitude notes. Form the actual `(n-1) by m` matrix



$$
H_{k,i}=g_{l_i}p_k^{(\sigma_i)}(\xi_{l_i}),
\qquad n+1\le k\le2n-1,
\qquad G_{\rm act}=H^TH.
\tag{12}
$$



For the even upper cut retain exactly



$$
s_{2n}(x)=\Lambda_{(2n,2)}(x)(2n)^{-1/2},\qquad
\Lambda_{(N,J)}(x)=
\prod_{j=J+2,J+4,\ldots,N}\lambda(x/j^2),
\quad \lambda(c)=1/q(c).
$$



Define the positive diagonal scales



$$
d_i=g_{l_i}s_{2n}(\xi_{l_i})\xi_{l_i}^{p_{\sigma_i}},
\quad p_0=3/2,\quad p_1=1,\quad D=\operatorname{diag}(d_i),
\qquad \widehat H=HD^{-1},\quad
\widehat G=D^{-1}G_{\rm act}D^{-1}=\widehat H^T\widehat H.
\tag{13}
$$



The audited quantitative high-kernel theorem, equation (21) of
`raw_quantitative_fixed_cut_transport.md`, now gives



$$
\max_{i,j}|\widehat G_{ij}-\mathcal L_{ij}|
\le C_{\alpha,\beta}\frac{\log n}{n}.
\tag{14}
$$



Its high-kernel formula uses `x=c n^2`, whereas (6) uses the
upper-cut parameter `c_i=xi_(l_i)/(2n)^2`. Substituting `c=4c_i`
there gives exactly (8) and (14); the associated compact interval
is fixed. Each chosen parity entry is bounded by the uniform
two-by-two matrix error. The error constant is independent of
`m` and of the selected actual indices in this bulk interval.

In particular the factorial-scale amplitudes, scalar transport
products, and unequal powers have not been replaced by their
asymptotics. Reflection of the original polynomial merely changes
the sign of odd spectral columns; applying that same column-sign
diagonal to both sides preserves every rank, singular-value and
determinant assertion below.

## 4. Relative Gram control and actual independence

The entry bound (14) implies



$$
\|\widehat G-\mathcal L\|
\le C_{\alpha,\beta}m\frac{\log n}{n}.
$$



Combining with (10), set



$$
\eta_n=\frac{C_{\alpha,\beta}}{c_*}
m(\log n)n^{-1+\theta}
=O_{\alpha,\beta,\kappa}
\bigl((\log n)^2n^{-1+\theta}\bigr)\longrightarrow0.
\tag{15}
$$



The normalized error
`L^(-1/2)(Ghat-L)L^(-1/2)` has norm at most `eta_n`.
Consequently the actual matrices satisfy



$$
\boxed{(1-\eta_n)\mathcal L\preceq\widehat G
\preceq(1+\eta_n)\mathcal L.}
\tag{16}
$$



For sufficiently large `n`, `eta_n<=1/2`, and therefore



$$
\boxed{\lambda_{\min}(\widehat G)
\ge\frac{c_*}{2}n^{-\theta},\qquad
\sigma_{\min}(\widehat H)
\ge\sqrt{c_*/2}\,n^{-\theta/2}.}
\tag{17}
$$



Thus these `m=floor(kappa log n)` actual high columns are
linearly independent. A safe statement before removing the
physical column scales is



$$
\sigma_{\min}(H)
\ge\left(\min_i d_i\right)
\sqrt{c_*/2}\,n^{-\theta/2}.
\tag{18}
$$



This last inequality retains the amplitude loss explicitly.
From (11) and (16) one also obtains the normalized bounds



$$
\operatorname{cond}(\widehat G)
\le C(\log n)n^\theta,\qquad
\operatorname{cond}(\widehat H)
\le C\sqrt{\log n}\,n^{\theta/2}.
\tag{19}
$$



All constants in the asymptotic statements depend only on the
fixed interval and the chosen `kappa`.

## 5. Relative determinant convergence

Taking determinants in (16) yields



$$
(1-\eta_n)^m\le
\frac{\det\widehat G}{\det\mathcal L}
\le(1+\eta_n)^m.
$$



Since `eta_n<=1/2` eventually, this proves the quantitative
relative determinant theorem



$$
\boxed{
\left|\log\frac{\det\widehat G}{\det\mathcal L}\right|
\le2m\eta_n
=O\bigl((\log n)^3n^{-1+\theta}\bigr)=o(1).}
\tag{20}
$$



Restoring the exact diagonal from (13) gives



$$
\boxed{\det G_{\rm act}
=\left(\prod_{i=1}^m d_i^2\right)
\det\mathcal L\,
\exp\!\left[O\bigl((\log n)^3n^{-1+\theta}\bigr)\right].}
\tag{21}
$$



This is a relative asymptotic for a growing actual high-row Gram
minor, rather than an asymptotic only for its individual entries.

## 6. The remaining scale distinction

Equations (17)-(21) prove the formerly conditional sparse bulk
claim. They also imply that the full actual high matrix has rank
at least `floor(kappa log n)` for large `n`.

For a full-density selection `m` proportional to `n`, the limiting
least eigenvalue instead has size `exp(-Theta(n))`. The present
entry error `O(log(n)/n)` does not reach that stability scale.
For a consecutive logarithmic cluster the improved spacing (7)
also fails. Neither case is covered by this theorem.

The theorem does not settle the full high-matrix inverse, the
two-dimensional kernel's endpoint angle, parameters tending to
zero, the whole HP remainder, or primitive denominator growth.
It supplies an actual sparse multipoint determinant and singular-
value result with all physical column normalizations retained.
