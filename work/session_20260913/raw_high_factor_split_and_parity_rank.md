> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Positive high-node factors: individual parity rank and the obstruction to common removal

Date: 2026-09-13. Original bounded continuation by audit_computations.

Independent review: `raw_high_factor_split_independent_review.md`
passes the actual parity-rank, cross-cut-rank and Loewner-comparison
claims. Its support-lemma scope clarification is incorporated.

This note attacks the actual matrix `Z_L` in
`raw_high_multipoint_complementary_reduction.md`. It proves an
`O(sqrt n)` nullity bound for each of its two parity blocks. It
also proves that the coordinate coupling of an actual positive
high-factor polynomial has rank `n-O(sqrt n)`. Thus the proposed
factor split does not, by itself, reduce the full two-channel
problem to the low nodes. No extra numerical solve is used.

## 1. A rigorous split with at most O(sqrt n) exceptional nodes

Fix `n>=2`, let `K=K_(2n)`, and let `P_L` restrict a vector to
coordinates `0,...,n`. The established spectral bound is



$$
\lambda_{\max}(K)\le M_n:=2n+3/4.
\tag{1}
$$



The actual prolate nodes satisfy



$$
l(l+1)+3/4\le\xi_l\le l(l+1)+1.
\tag{2}
$$



Put



$$
j_n=\left\lfloor\frac{\sqrt{1+8n}-1}{2}\right\rfloor.
\tag{3}
$$



For every `l>j_n`, the even integer `l(l+1)-2n` is at least
two, so



$$
\xi_l-M_n\ge2.
\tag{4}
$$



We deliberately include *all* indices `0,...,j_n` among the
potentially exceptional nodes. Some of their nodes might also
lie above the row spectrum; nothing below requires deciding that.
There are at most `sqrt(2n)+1` such indices.

For `sigma=0,1`, retain the original parity node polynomial and
write



$$
\begin{aligned}
L_\sigma(t)&=\prod_{\substack{0\le l\le j_n\\l\equiv\sigma\ (2)}}
(t-\xi_l),&\ell_\sigma&=\deg L_\sigma,\\
F_\sigma(t)&=\prod_{\substack{j_n<l\le n\\l\equiv\sigma\ (2)}}
(\xi_l-t),&h_\sigma&=\deg F_\sigma.
\end{aligned}
\tag{5}
$$



Thus `Q_sigma=(-1)^(h_sigma)L_sigma F_sigma` and, by (1), (4),



$$
\boxed{F_\sigma(K)>0.}
\tag{6}
$$



An empty high product is the identity. Let



$$
m_0=\lceil(n+1)/2\rceil,\quad m_1=\lfloor(n+1)/2\rfloor,
\quad d_\sigma=n-m_\sigma,
\quad v_0=e_0,\quad v_1=e_1-(\sqrt3/2)e_0.
$$



Up to the common column sign `(-1)^(h_sigma)`, the actual parity
block of `Z_L` is the map on polynomials `deg u<d_sigma`



$$
\mathcal Z_\sigma u
=P_LF_\sigma(K)L_\sigma(K)u(K)v_\sigma.
\tag{7}
$$



The full `Z_L` is the juxtaposition of these two maps with their
previously specified ordering. Its spectral amplitudes still enter
the separate cardinal matrix `S=Y_low diag(g_l)`; no amplitude
has been changed by (5)--(7).

## 2. A positive test proves individual parity rank up to O(sqrt n)

Define



$$
q_\sigma=\left\lfloor\frac{n-\sigma}{2}\right\rfloor.
\tag{8}
$$



The finite Krylov support property says that `p(K)v_sigma` is
supported in coordinates `0,...,n` whenever `deg p<=q_sigma`.
Indeed its maximal possible index is `2 deg p+sigma`.
Moreover a nonzero polynomial of that degree cannot give the zero
vector: its highest interleaved branch coefficient is nonzero,
by the triangular coefficient basis theorem.

Suppose `mathcal Z_sigma u=0` and



$$
\deg u+\ell_\sigma\le q_\sigma.
\tag{9}
$$



Put `w=L_sigma(K)u(K)v_sigma`. The vector `w` is supported in
the retained coordinates. Taking its inner product with (7) gives



$$
0=w^TP_L^TP_LF_\sigma(K)w=w^TF_\sigma(K)w.
$$



Positivity (6) implies `w=0`. The triangular property just stated
then implies the polynomial `L_sigma u` is zero, hence `u=0`.

It follows that the kernel of (7) has trivial intersection with
the polynomial subspace of degrees at most `q_sigma-ell_sigma`.
Counting its codimension in the `d_sigma`-dimensional domain gives



$$
\boxed{
\operatorname{nullity}\mathcal Z_\sigma
\le\min\left\{d_\sigma,
\max\{0,d_\sigma-q_\sigma-1+\ell_\sigma\}\right\}.}
\tag{10}
$$



The outer minimum covers empty or very short polynomial spaces.
In the actual parity conventions this is



$$
\begin{array}{c|cc}
&\sigma=0&\sigma=1\\ \hline
n\text{ even}
&\max(0,\ell_0-2)&\ell_1\\
n\text{ odd}
&\max(0,\ell_0-1)&\max(0,\ell_1-1),
\end{array}
\tag{11}
$$



with each entry also capped by `d_sigma`. Every entry is
`O(sqrt n)`. Thus each channel separately has rank at least
`n/2-O(sqrt n)`. This statement applies to the actual nodes and
actual seed vectors, including every degree and every possible
location of the exceptional low nodes.

This does **not** bound the nullity of the combined block by the
sum of the two bounds. Two individually injective maps can have
intersecting images. The intersection of the two actual image
spaces is part of the original multipoint obstruction.

## 3. What would work for a common positive factor

The following elementary lemma identifies the useful mechanism
behind the proposed rank reduction.

**Support lemma.** Let `F>0` be an `N`-by-`N` real symmetric
matrix. Let `P` retain the first `a` coordinates, with
`a+r<=N`. Suppose a
full-column-rank matrix `W` has its image supported in the first
`a+r` coordinates. Then



$$
\operatorname{nullity}(PFW)\le r.
\tag{12}
$$



Proof: restrict `F` to its first `a+r` columns. Its first `a`
rows have row rank `a`, since their first `a`-by-`a` block is
a positive definite principal submatrix. Their kernel in that
`a+r`-dimensional coordinate space has dimension `r`.
Intersecting it with the injectively parametrized image of `W`
proves (12).

If instead `a+r>N`, replace `r` by `N-a` in the proof;
the resulting bound is at most the stated `r`. Thus the same
conclusion also covers that harmless truncated-support case.

Thus if a *common* high factor could be removed while leaving a
full-rank family supported only `O(sqrt n)` coordinates beyond
the cut, the desired small rank-defect statement would follow.
For the actual two channels, however, (7) has `F_0` on one
family and `F_1` on the other. These cannot simply be replaced by
one common factor in (12).

One exact common-factor expression is



$$
\bigl[F_0(K)W_0,F_1(K)W_1\bigr]
=F_0(K)F_1(K)
\bigl[F_1(K)^{-1}W_0,F_0(K)^{-1}W_1\bigr],
\tag{13}
$$



where `W_sigma` consists of `L_sigma(K)K^j v_sigma`.
The inverses on the right destroy the support property used in
(12). The next section gives an exact large-rank statement about
this failure, not just an entrywise observation that inverses may
be dense.

## 4. Exact cross-cut rank of a high-factor polynomial and its inverse

The actual `K` has bandwidth two, with every outer-band entry



$$
K_{i,i+2}=a_{i+1}a_{i+2}>0.
$$



Let `f` be any polynomial of degree `h` with nonzero leading
coefficient, where `2h<=n+1`. Split coordinates after `n` into
`L={0,...,n}` and `H={n+1,...,2n-1}`. Then



$$
\boxed{\operatorname{rank}f(K)[L,H]=\min(2h,n-1).}
\tag{14}
$$



For `h=0` the block is zero. For positive `h`, put
`a=n+1` and `r=min(2h,n-1)`. Take the `r` rows
`a-2h,...,a-2h+r-1` and the `r` columns `a,...,a+r-1`.
The `(i,j)` entry of this selected block has index separation
`2h+j-i`. It is zero for `j>i`, because `f(K)` has bandwidth
`2h`. On its diagonal the only path of length `h` reaching
distance `2h` consists entirely of steps of size two. Its entry
is



$$
\operatorname{lc}(f)
\prod_{t=0}^{h-1}a_{a-2h+i+2t+1}a_{a-2h+i+2t+2}\ne0.
\tag{15}
$$



Lower-degree terms in `f` cannot reach that distance. Thus this
minor is triangular with nonzero diagonal, proving the lower
bound in (14). The bandwidth leaves at most `2h` nonzero rows
in the full cross block, and there are only `n-1` high columns;
these give the matching upper bound.

For the actual factors `F_sigma`, the assumption `2h<=n+1`
always holds when `n>=2`: indices zero and one are in the low
set, so each high parity count is at least one below its full
parity count. Therefore (14) applies and yields



$$
\operatorname{rank}F_\sigma(K)[L,H]
=\min(2h_\sigma,n-1)=n-O(\sqrt n).
\tag{16}
$$



The last asymptotic follows from `h_sigma=m_sigma-ell_sigma`.
All roots of these polynomials lie strictly above the row spectrum.
Positive definiteness does not reduce this cross-cut rank.

It also does not help by inverting the factors. If `F>0`, the
block inverse formula gives



$$
(F^{-1})_{LH}
=-F_{LL}^{-1}F_{LH}
\bigl(F_{HH}-F_{HL}F_{LL}^{-1}F_{LH}\bigr)^{-1}.
$$



Both outside factors are invertible, so



$$
\boxed{\operatorname{rank}(F_\sigma(K)^{-1})_{LH}
=\operatorname{rank}F_\sigma(K)_{LH}
=\min(2h_\sigma,n-1).}
\tag{17}
$$



Equations (16)--(17) do not prove that every specific Krylov
family in (13) attains this rank. They prove that no general
`O(sqrt n)` cross-cut-rank bound follows from the location of
the high roots or from positive definiteness. A cancellation
specific to those families would require a further theorem.

## 5. The distinct positive factors nevertheless have a useful polynomial comparison

The high-node lists in the two channels alternate. Their counts
differ by at most one. If necessary, transfer the last high root
from the longer list into its `L_sigma` factor. This increases
one exceptional degree by one and leaves equal high counts.
Call the resulting equal-degree factors `F_a,F_b`, with the
channel labels chosen so that their roots satisfy



$$
\alpha_1<\beta_1<\alpha_2<\beta_2<\cdots<\alpha_h<\beta_h.
\tag{18}
$$



Every root is still above `M_n` by at least two. For real `t<=M_n`,



$$
\frac{\alpha_1-t}{\beta_h-t}
\le\prod_{i=1}^h\frac{\alpha_i-t}{\beta_i-t}\le1.
\tag{19}
$$



The right inequality holds termwise. For the left one, pair
`alpha_i-t>=beta_(i-1)-t` for `i>=2` and cancel. The remaining
ratio decreases as `t` increases. By (2), (4),



$$
\alpha_1-M_n\ge2,\qquad
\beta_h-M_n\le n(n+1)+1-M_n\le n^2.
$$



Functional calculus now gives the exact comparison



$$
\boxed{\frac2{n^2}I\preceq F_a(K)F_b(K)^{-1}\preceq I,
\qquad
\frac2{n^2}F_b(K)\preceq F_a(K)\preceq F_b(K).}
\tag{20}
$$



The empty equal-degree case gives the identity and also satisfies
(20). This is a polynomial comparison of the two factors despite
the potentially much larger condition numbers of each factor
separately. No continuum node approximation is used.

Comparison (20) is not a common action on the two column spaces.
After removing `F_b`, one space is changed by the positive operator
`F_a F_b^{-1}` while the other is unchanged. Bounds for that
operator alone do not bound the angle between the two resulting
spaces.

For a simple demonstration of this logical limitation, take the
two-by-two diagonal matrix `K=diag(0,1)`, roots `alpha=2<beta=3`,
and vectors `w_0=(1,1)^T`, `w_1=(2/3,1/2)^T`. The vectors are
independent, both root factors are positive definite, and their
ratio has eigenvalues `2/3,1/2`. Nevertheless



$$
(2I-K)w_0=(3I-K)w_1=(2,1)^T.
\tag{21}
$$



This example is not the actual research matrix or an actual
counterexample to its full rank. It proves that the polynomial
Loewner comparison in (20), by itself, cannot supply the missing
combined-rank argument.

## 6. The precise remaining step

The split gives the following actual progress:

* Each parity block of `Z_L` is within `O(sqrt n)` of full
  column rank, by the positive test (9)--(11).
* After moving at most one root, the high parity factors are
  mutually comparable with a loss at most `n^2/2`, by (20).
* Removing them through the low-coordinate projection is not a
  perturbation of rank `O(sqrt n)`; its exact cross-cut rank is
  `n-O(sqrt n)`, by (16)--(17).

Thus a useful next lemma must control the intersection or angle of



$$
\operatorname{ran}\bigl(P_LF_0(K)W_0\bigr),\qquad
\operatorname{ran}\bigl(P_LF_1(K)W_1\bigr),
\tag{22}
$$



or exploit a special cancellation of their high-coordinate tails
after (13). The individual positivity tests do not compare the
cross terms between these spaces. Their bounds do not yield an
inverse for the full `Z_L` Gram matrix or the near-one cardinal
determinant in the preceding note. The actual amplitude-weighted
cardinals must still be retained when converting a future rank or
angle theorem to the finite spectral kernel.

No conclusion about primitive shrinking or the rationality of
`e+pi` follows from this partial rank theorem.
