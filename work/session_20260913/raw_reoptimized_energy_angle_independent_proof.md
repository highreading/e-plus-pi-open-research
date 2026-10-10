> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent proof of the reoptimized supported-energy angle bound

Date: 2026-09-13. Derivation and verification by audit_computations,
following root's positive-power support proposal. This uses the
reviewed reflection estimate from
`raw_channel_reflection_energy_angle.md`; it does not repeat that
proof or assume that reflection commutes with the full finite F.

The result concerns a reoptimized cutoff b. It bounds the actual
unprojected energy angle delta_(n,b), proves that the actual retained
vanishing matrix has rank n−O(n^(3/4)), and controls its projection
in the stated energy normalization. The old cutoff b=ceil(2sqrt n)
defines a different metric; the same minimum-angle bound for that
particular metric is not asserted here.

## 1. A positive-power support lemma

Set N=2n, K=K_N, C=C_N and



$$
M=2n+1,\qquad H=MI-K.
$$



The reviewed spectral bounds imply



$$
\frac14I\preceq H\preceq
(4n^2+2n+5/8)I,
\qquad \operatorname{cond}H\le25n^2\quad(n\ge2).
\tag{1}
$$



C preserves every coordinate prefix. Its exact commutator with K
has right support in coordinates N−2,N−1. Consequently, if w is
supported through index s and s+2r<N, then



$$
H^rCw=CH^rw.
\tag{2}
$$



To check the endpoint condition, expand [H^r,C] as a sum of
`H^(r-1-j)[H,C]H^j`. For j<=r−1, H^jw is supported through
`s+2j<=s+2r−2<=N−3`; every commutator term is zero. This
proves (2) without an infinite-operator argument.

Suppose a positive polynomial has the form



$$
F(K)=\prod_{i=1}^h(\beta_iI-K)
=\prod_{i=1}^h[(\beta_i-M)I+H]
=\sum_{j=0}^h f_jH^j,
\qquad \beta_i>M.
\tag{3}
$$



All coefficients f_j are positive. For a vector supported through
s with s+h<N, every even term j=2r satisfies



$$
(Cw)^TH^{2r}Cw=\|CH^rw\|^2
\le\|C\|^2 w^TH^{2r}w.
$$



For an odd term j=2r+1, (1)-(2) give



$$
(Cw)^TH^{2r+1}Cw
=\|CH^rw\|_H^2
\le\|C\|^2\operatorname{cond}H\,
w^TH^{2r+1}w.
$$



Summing with the positive coefficients in (3) proves



$$
\boxed{\|Cw\|_F\le L_n\|w\|_F,
\quad L_n:=\|C\|\sqrt{\operatorname{cond}H}
\le60n^2e^{2\sqrt{6n}}\quad(n\ge3),
\quad s+h<N.}
\tag{4}
$$



This is a supported-vector inequality. It need not hold with this
constant on the whole finite space. That distinction avoids the
large full conjugated-reflection norm appearing in the earlier
boundary-residue approach.

## 2. The exact actual factor split with a variable cutoff

Choose an integer cutoff b satisfying 2sqrt n<=b<n. Put all nodes
0,...,b into their original low parity factors; if needed, move
one last high root into the longer low list. Label the remaining
equal high lists as in the ratio note:



$$
\alpha_1<\beta_1<\cdots<\alpha_h<\beta_h,
\quad F_a(t)=\prod(\alpha_i-t),\quad
F_b(t)=\prod(\beta_i-t),\quad R=F_a/F_b.
\tag{5}
$$



Use F=F_b(K) in (3)-(4). The roots are actual prolate nodes.
For every high index l>b,



$$
\xi_l-(2n+3/4)\ge l(l+1)-2n\ge b^2/2.
\tag{6}
$$



They therefore exceed the M in (3) for all the relevant large n.
The exact interlacing telescoping bound gives



$$
\boxed{r_0I\preceq R(K)\preceq I,
\qquad r_0=b^2/(2n^2).}
\tag{7}
$$



Indeed the first numerator at the spectral upper endpoint is at
least b²/2, and the final denominator is at most n². The case of
an empty equal high product is immediate; the stated asymptotic
choices have h>0 eventually.

Let the low factors be L_sigma, their degrees ell_sigma, and
`d_sigma=n-m_sigma`, with m_sigma the *original* parity counts.
The actual seed vectors remain



$$
v_0=e_0,\qquad v_1=e_1-(\sqrt3/2)e_0,
\qquad
W_\sigma=[L_\sigma(K)K^jv_\sigma]_{0\le j<d_\sigma}.
\tag{8}
$$



There are still n−1 columns in the combined family. Up to fixed
column signs and ordering the full actual matrix is unchanged:



$$
Z=F[\,R(K)W_a,W_b\,].
\tag{9}
$$



Only its auxiliary metric and factorization depend on b.

## 3. Ratio approximation at the enlarged gap

Use the positive normalized partial-fraction weights and the
Chebyshev construction from the ratio note. The spectral interval
has length at most 6n²; (6) gives the real pole-coordinate bound
`z_beta>=1+b²/(6n²)`. Since `cosh u<=1+u²` for 0<=u<=1,
the same exact argument supplies a degree-m polynomial p_m with



$$
\boxed{\|R(K)-p_m(K)\|
\le\varepsilon:=2\exp[-(m+1)b/(\sqrt6 n)].}
\tag{10}
$$



Because F is also a function of K, (10) holds in F-energy with
the same epsilon and no extra condition number.

The surrogate spaces `[p_m(K)W_a,W_b]` are pure and opposite
component spaces for C, provided their maximal degree stays below
the finite boundary. Their common support index is at most



$$
s\le n+2\ell_{\max}+2m-1\le n+b+2+2m.
\tag{11}
$$



Here the low lists have at most b+2 roots in total, and
`2ell_max<=b+3`. The equal high count obeys h<=(n−b)/2.
Thus the sufficient condition



$$
\boxed{b+4m+4<n}
\tag{12}
$$



ensures s+h<N. It also ensures that all the polynomial Krylov
identities used for these surrogate component spaces are exact.
When epsilon<r_0, p_m(K)>0, so both surrogate blocks have full
column rank. Their opposite component polynomials cannot cancel,
and hence their combined family is independent as well.

## 4. The supported surrogate angle and the normalized perturbation

By (4), C has norm at most L_n on the entire supported surrogate
sum in its F metric. The exact involution/principal-angle formula
therefore gives a lower bound for the smallest singular value
after each surrogate channel is separately orthonormalized:



$$
\delta_{\rm sur}\ge\sqrt{2/(1+L_n^2)}
\ge d_n,\qquad
d_n=(60n^2)^{-1}e^{-2\sqrt{6n}}.
\tag{13}
$$



Now retain the actual normalization from the ratio note:



$$
E_a=F^{1/2}R(K)W_aG_a^{-1/2},\quad
E_b=F^{1/2}W_bG_b^{-1/2},\quad
G_a=W_a^TR(K)FR(K)W_a,\quad G_b=W_b^TFW_b.
\tag{14}
$$



Each block is exactly orthonormal. Let E=[E_a,E_b], and replace
R by p_m only in its first block to obtain tilde(E). Equations
(7) and (10) imply



$$
\|E-\widetilde E\|\le t:=\varepsilon/r_0.
\tag{15}
$$



In particular the first surrogate block has its smallest singular
value at least 1−t. Separately orthonormalizing that block and the
unchanged second block, then applying (13), gives
`sigma_min(tilde E)>=d_n(1-t)`. Weyl's inequality thus proves



$$
\delta_{n,b}:=\sigma_{\min}(E)
\ge d_n(1-t)-t\ge d_n/2
\quad\text{if }t\le d_n/4.
\tag{16}
$$



The last elementary implication uses d_n<=1. This step does not
confuse the actual Gram normalization with the surrogate one.

A fully explicit sufficient choice is



$$
\frac{(m+1)b}{\sqrt6 n}
\ge2\sqrt{6n}+\log(960n^4/b^2).
\tag{17}
$$



Then epsilon<=r_0 d_n/4. Combining (12),(16),(17) proves



$$
\boxed{\delta_{n,b}\ge
\frac1{120n^2}e^{-2\sqrt{6n}}.}
\tag{18}
$$



For example, b=ceil(n^(3/4)) and the least integer m satisfying
(17) have m=O(n^(3/4)), so (12) holds for all sufficiently large n.
This proves (18) for an actual admissible sequence of energy metrics.

## 5. The resulting actual rank and energy-projection statement

Let L be the first n+1 coordinate space and enlarge it to U so
that every surrogate column is supported there. It suffices to use



$$
r:=\dim U-\dim L\le2(m+\ell_{\max})
\le2m+b+3.
\tag{19}
$$



Let Pi_L^F project orthogonally onto F^(1/2)L. As in the exact
localization note, `(I-Pi_L^F)tilde E` has rank at most r. Hence
for the orthonormal actual combined image
`O=E(E^TE)^(-1/2)`, (15)-(16) give



$$
\sigma_{r+1}((I-\Pi_L^F)O)
\le\frac{\varepsilon}{r_0\delta_{n,b}}.
\tag{20}
$$



Adding A log n to the right side of (17), for any fixed A>0,
makes the right side of (20) at most n^(−A)/2, without changing
the order m=O(n^(3/4)). Thus all but O(n^(3/4)) directions in
the actual combined image have near-unit projection to the retained
energy space. Its exact projection matrix is



$$
F[L,L]^{-1/2}Z_L\,
\operatorname{diag}(G_a^{1/2},G_b^{1/2})^{-1}
(E^TE)^{-1/2},
\tag{21}
$$



with the previously specified harmless column signs and ordering.
Every outside factor is invertible. Consequently



$$
\boxed{\operatorname{rank}Z_L\ge n-1-O(n^{3/4}).}
\tag{22}
$$



The exact high-matrix factorization through the invertible low
evaluation matrix and high triangular block gives the same rank
bound for the actual high evaluation/moment matrix on rows
n+1,...,2n−1 and the parity-selected nodes xi_0,...,xi_n. Actual nonzero
amplitude diagonals do not change rank. They do change metric
conditioning, and are not discarded from any endpoint-angle claim.

More generally, b/sqrt n→infinity and b=o(n) allow
`m=O(n^(3/2)/b+(n/b)log n)=o(n)`, giving an o(n) rank defect.
Balancing b with n^(3/2)/b gives the displayed n^(3/4) scale.

## 6. Scope and the abandoned stronger target

The supported positive-power proof bypasses any bound for the full
Theta_N of the preceding reflection note. It uses the actual
polynomial surrogates before the finite boundary, where only half
as many powers are needed in each positive quadratic term.

The minimum-angle estimate is for the reoptimized F_b metric.
The original b=ceil(2sqrt n) metric, a bound for the full conjugated
reflection, complete high-row rank, and the final amplitude-weighted
two-dimensional endpoint angle remain separate questions.
Neither (18) nor (22) proves primitive shrinking or irrationality.

A predeclared exploratory calculation at n=8,16,32, saved in
`raw_weighted_reflection_exploration.json`, used the original cutoff
and suggested a large disparity between full weighted reflection
and its actual restriction. It was high-precision floating-point,
not interval certified, and is not an input to any proof above.
No HP coefficient system was solved. The proof uses only the
reviewed all-degree identities, support counts, and inequalities.
