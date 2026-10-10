> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Nondecomposable exterior sums of root-of-unity remainders

## Exact linear tail elimination, a genuine rank-gap exception, and the remaining intrinsic-height barrier

Checked: 2026-08-27 UTC

## 1. Scope and verdict

This note studies a construction which is strictly larger than the
decomposable two-column construction in
sources/root_unity_corrected_exterior_primitive_height_audit.md.
Let $E_\nu$ be a reduced endpoint space of dimension $\nu$.  Instead of
requiring one Pluecker vector $C\wedge D$, allow an arbitrary



$$
p\in\bigwedge^2E_\nu.              \tag{1}
$$



Every such $p$ gives a rational linear combination of pairwise
Wronskians.  The combination retains the common origin order and has a
corrected polynomial endpoint at $i\pi$.  Since
$\dim\bigwedge^2E_\nu={\nu\choose2}$, one can kill all corrected
coefficients above a fixed target degree by linear algebra with
$\nu=O(\sqrt{n+D})$.  The loss in origin order is therefore only
$O(\sqrt n)$ when $D\asymp n$.

There are five exact conclusions.

1. The construction is valid for every exterior vector, without a
   Pluecker relation.  A rank-gap criterion, not dimension counting alone,
   is necessary and sufficient for a nonzero low-degree endpoint.
2. It is genuinely outside the prior decomposable-pair audit.  On every
   usable grid row with $\nu\ge4$, the selected alternating matrix has
   rank at least four and hence cannot equal one wedge $C\wedge D$.
3. Dimension counting has a real failure.  At

   

$$
(m,n,D,\nu,d)=(2,11,11,7,2),                \tag{2}
$$



   the minimal choice ${7\choose2}=21>20=n+D-d$ has a
   three-dimensional high-tail kernel, but that kernel is exactly the
   full corrected-map kernel: both the tail and full ranks are $18$.
   Every putative quadratic is zero.
   Increasing to $\nu=8$ restores a rank gap of two.
4. The tempting stronger claim that the full-endpoint corrected map always
   has the largest rank allowed by parity is false.  At the exact tuple

   

$$
(m,n,D)=(2,21,7),                      \tag{2a}
$$



   the full rank is $26$, versus parity cap $27$, and the tail rank
   on degrees $3,\ldots,28$ is $23$, versus parity cap $25$.  Its
   actual low-degree rank gap is nevertheless three.  Thus this refutes a
   proposed route to a universal rank-gap proof, not the rank gap itself.
5. The construction does not currently beat the height/capacity barrier.
   The minimal full-endpoint variant $E_\nu=\mathbb Q[z]_{\le D}$,
   $\nu=D+1=O(\sqrt n)$, has monomial basis height one and therefore
   removes the endpoint-lattice basis cost.  Nevertheless the auxiliary
   interpolation height and the exterior tail-kernel height remain.  Every
   finite leading $r=1$ measure margin recorded below is negative.  The
   universal interpolation bound is still on the $n^2\log n$ scale,
   whereas the centered analytic gain is only on the $n\log n$ scale.

Thus nondecomposable exterior sums are a legitimate conditional survivor,
not a proof or a no-go classification.  What remains is an all-parameter
rank-gap theorem and, more importantly, an intrinsic saturated
remainder/content theorem on the $O(n\log n)$ scale.  No conclusion about
the arithmetic nature of $e+\pi$ is claimed.

The deterministic replay files are

* scripts/root_unity_nondecomposable_exterior_sum_certificate.py;
* results/root_unity_nondecomposable_exterior_sum_certificate.json.

## 2. Exact exterior-sum identity

Put



$$
M=m(n+1),\qquad
 \Phi_{m,n}(X)=\prod_{j=0}^{m-1}(X-j)^{n+1}.               \tag{3}
$$



For $2\le\nu\le D+1$, define $E_\nu\subseteq\mathbb Q[z]_{\le D}$
by the $D+1-\nu$ constraints



$$
\sum_{a=0}^Dc_a
 \mathcal L\!\left((X^q\Phi_{m,n})^{(a)}\right)=0,
 \qquad 0\le q\le D-\nu.                                  \tag{4}
$$



The endpoint-normality theorem gives $\dim E_\nu=\nu$.  For every
$C\in E_\nu$, the unique auxiliary form satisfies



$$
\begin{aligned}
 R_C(z)&=C(z)+(1+e^z)T_C(z,e^z)=O(z^{L_\nu}),\\
 L_\nu&=M+D+1-\nu,\\
 \beta_C(z)&=T_C(z,-1).
 \end{aligned}                                             \tag{5}
$$



Choose any basis $C_1,\ldots,C_\nu$ and put



$$
\begin{aligned}
 \Delta_{ij}
   &=W(C_i,C_j)-\{C_i\beta_{C_j}-C_j\beta_{C_i}\},\\
 \mathcal W_{ij}&=W(R_{C_i},R_{C_j}).
 \end{aligned}                                             \tag{6}
$$



For arbitrary rational coordinates $x=(x_{ij})_{i<j}$, define



$$
\Delta_x=\sum_{i<j}x_{ij}\Delta_{ij},\qquad
 \mathcal W_x=\sum_{i<j}x_{ij}\mathcal W_{ij}.             \tag{7}
$$



The pairwise endpoint identity is linear, hence



$$
\mathcal W_x(i\pi)=\Delta_x(i\pi).\tag{8}
$$



Also, if $F=z^L(f_0+f_1z+\cdots)$ and
$G=z^L(g_0+g_1z+\cdots)$, the terms of degree $2L-1$ in
$FG'-GF'$ cancel.  Thus every pair in (6), and therefore their sum,
satisfies



$$
\operatorname {ord}_0\mathcal W_x
                         \ge2L_\nu.                         \tag{9}
$$



If $\Delta_x\ne0$, then $\Delta_x(i\pi)\ne0$, since a nonzero rational
polynomial cannot vanish at the transcendental number $i\pi$.

### 2.1 The exact coefficient map

Let



$$
E_{b,a}=[z^b]\beta_{z^a},\qquad
 Q=Q_{m,n},\qquad E^Q=QE\in\mathbb Z^{(n+1)\times(D+1)}.  \tag{10}
$$



In ambient monomial exterior coordinates $p_{uv}$, $u<v$, the integer
coefficient map $p\mapsto Q\Delta_p$ is



$$
\boxed{
 (\mathcal A_Q)_{\ell,(u,v)}
 =Q(v-u)\mathbf1_{\ell=u+v-1}
  -E^Q_{\ell-u,v}+E^Q_{\ell-v,u},}                         \tag{11}
$$



where an out-of-range entry is zero.  Formula (11) is the same corrected
map as in the two-dimensional audit; only its domain has been enlarged
from a decomposable exterior line to all of $\bigwedge^2E_\nu$.

## 3. Tail elimination and the necessary rank gap

Fix a target degree $d\ge0$.  Set



$$
N={\nu\choose2},\qquad S=n+D-d.        \tag{12}
$$



After restricting (11) to $\bigwedge^2E_\nu$, let
$\mathcal T_{>d}$ be the $S$-row map formed by coefficient degrees
$d+1,\ldots,n+D$, and let $\mathcal T_{\rm all}$ be the full map.
If $N>S$, then $\ker\mathcal T_{>d}\ne0$, but the resulting endpoint
is usable precisely when



$$
\boxed{
 \operatorname {rank}\mathcal T_{\rm all}
  >\operatorname {rank}\mathcal T_{>d}.}                  \tag{13}
$$



Indeed, the tail rows are rows of the full map, so (13) is equivalent to



$$
\ker\mathcal T_{>d}\not\subseteq
 \ker\mathcal T_{\rm all}.                                \tag{14}
$$



This proves both sufficiency and necessity.  The exceptional tuple (2)
shows that (13) cannot be deleted from the argument.

For $D/n\to\delta>0$, fixed $d$, and any fixed oversampling factor
$\tau>1$, taking $N\sim\tau S$ gives



$$
\nu\sim\sqrt{2\tau(1+\delta)n},\qquad
 L_\nu-n=(m-1+\delta)n-O(\sqrt n).                         \tag{15}
$$



Thus the tail elimination has no leading analytic-order cost.

## 4. Saturated integer kernels and nondecomposability

The replay does not use a merely rational nullspace.  It applies the
following exact lattice lemma twice.

> **Transformed-Hermite kernel lemma.**  Let
> $A\in\mathbb Z^{r\times s}$.  Compute a row Hermite normal form
>
> 

$$
>                              H=UA^T,                      \tag{16}
>
$$


>
> with $U\in\mathrm {GL}_s(\mathbb Z)$.  The rows of $U$ corresponding
> to zero rows of $H$ form a basis of the saturated lattice
> $\ker(A)\cap\mathbb Z^s$.

To prove the lemma, write any $x^T\in\mathbb Z^s$ uniquely as $y^TU$.
Then $Ax=0$ is equivalent to $y^TH=0$.  The nonzero rows of a row HNF
are linearly independent, so precisely the coordinates of $y$
corresponding to zero HNF rows are free.  Unimodular LLL reduction of those
rows preserves the same saturated lattice.

First apply the lemma to the row-primitive clearing of (4), producing a
saturated endpoint basis matrix $B\in\mathbb Z^{(D+1)\times\nu}$.  Its
second exterior embedding is



$$
(\wedge^2B)_{(a,b),(i,j)}
   =B_{a,i}B_{b,j}-B_{b,i}B_{a,j}.                         \tag{17}
$$



Then apply the lemma to the row-primitive tail map
$\mathcal T_{>d}\wedge^2B$.  This gives a saturated integer tail-kernel
basis.  The replay LLL-reduces it and performs a documented bounded search
with coefficients in $\{-1,0,1\}$.  This search finds convenient short
vectors; it is not a shortest-vector certificate.

For $x\in\bigwedge^2\mathbb Q^\nu$, form the alternating matrix
$S_x=(x_{ij})$.  A nonzero exterior two-vector is decomposable if and
only if



$$
\operatorname {rank}S_x=2.   \tag{18}
$$



Every selected usable vector with $n\ge3$ has exact rank $4,6$, or
$8$.  These outputs are therefore genuinely unavailable to the
decomposable pair/Segre construction.  Conversely, the rational skew
normal form writes a rank-$2k$ vector as a sum of $k$ simple wedges.
So the construction is exactly a sum of pairwise Wronskians, not a hidden
single determinant.  It escapes the Pluecker equations but retains the
same common analytic order and additive height bookkeeping.

## 5. Intrinsic normalization and centered Schwarz gain

Let $C_1,\ldots,C_\nu$ now be the saturated integer basis and let
$\overline R_i=QR_{C_i}$.  For an integral exterior vector $x$, put



$$
N_{Q,x}=Q\Delta_x\in\mathbb Z[z],\qquad
 c_x=\operatorname {cont}(N_{Q,x}),\qquad
 P_x=N_{Q,x}/c_x.                                          \tag{19}
$$



The corresponding cleared analytic sum is



$$
\overline{\mathcal W}_x
   =\sum_{i<j}x_{ij}W(\overline R_i,\overline R_j)
   =Q^2\mathcal W_x.                                      \tag{20}
$$



Therefore



$$
F_x:=\frac{\overline{\mathcal W}_x}{Qc_x},\qquad
 F_x(i\pi)=P_x(i\pi),\qquad
 H(F_x)=\frac{H(\overline{\mathcal W}_x)}{Qc_x}.           \tag{21}
$$



Equation (21) is the intrinsic analytic normalization used in every
reported height.  It includes the exterior coefficient vector and the
actual corrected content; it is not the height of an arbitrarily scaled
basis.

There is a useful exact sharpening of the usual circle estimate.  The
frequencies of $F_x$ are $0,\ldots,2m$.  Multiplying by $e^{-mz}$
centers them at $-m,\ldots,m$, preserves the origin multiplicity, does
not change coefficient height, and satisfies



$$
|e^{-mi\pi}F_x(i\pi)|=|F_x(i\pi)|.\tag{22}
$$



Hence the circle exponential factor is $e^{m\rho}$, not $e^{2m\rho}$.
With



$$
A=L_\nu-n,\qquad
 \rho_*=\frac{2A}{m},\qquad
 \mathcal G_\nu^{\rm ctr}
 =A\log\frac{2A}{e\pi m}-n\log\pi,                         \tag{23}
$$



Schwarz's lemma gives, when $\rho_*>\pi$,



$$
-\log|P_x(i\pi)|
 \ge2\mathcal G_\nu^{\rm ctr}
   -\log\{(2m+1)(2n+1)H(F_x)\}.                            \tag{24}
$$



Relative to the uncentered estimate, one copy of the gain improves by
$A\log2$, and the total right side improves by $2A\log2$.  This is an
$O(n)$ improvement.  It does not change the $n\log n$ leading term.

For the easiest hypothetical field degree $r=1$, the replay records the
leading diagnostic margin



$$
2\mathcal G_\nu^{\rm ctr}
 -\log\{(2m+1)(2n+1)H(F_x)\}
 -d_x\log H(P_x),                                         \tag{25}
$$



where $d_x=\deg P_x$.  Every usable row in the grid has negative margin.
This finite fact is not extrapolated.

## 6. Exact rank grids

The main diagonal grid uses



$$
m\in\{2,3\},\qquad 2\le n=D\le12,\qquad d=2,              \tag{26}
$$



and the least $\nu$ satisfying ${\nu\choose2}>2n-2$.  The table records
the exact rank gap in (13).



$$
\begin{array}{c|rrrrrrrrrrr}
n&2&3&4&5&6&7&8&9&10&11&12\\ \hline
\nu&3&4&5&5&6&6&6&7&7&7&8\\
m=2&1&2&3&2&3&2&1&2&1&0&1\\
m=3&1&2&3&2&3&2&2&3&2&1&2
\end{array}                                                \tag{27}
$$



The zero in (27) is exactly (2).  At the rescued row $\nu=8$, the gap is
two, the selected skew rank is eight, and



$$
P_x(z)=321146238366967136256
       +32538916993625457427z^2.                            \tag{28}
$$



Every other usable diagonal row has actual degree two.  All selected
Wronskian sums have exact origin order $2L_\nu$, not merely the proved
lower bound.

### 6.1 Minimal full endpoint spaces

For each $n$, choose the least $D$ satisfying



$$
{D+1\choose2}>n+D-2,\qquad \nu=D+1.                       \tag{29}
$$



Then $E_\nu=\mathbb Q[z]_{\le D}$, the endpoint constraint matrix is
empty, and the saturated monomial basis has height one.  On the same
$m,n$ grid, the pairs



$$
(D,\nu)=(2,3),(3,4),(3,4),(4,5),(4,5),(4,5),
 (5,6),(5,6),(5,6),(5,6),(6,7)                            \tag{30}
$$



for $n=2,\ldots,12$ have rank gaps



$$
1,2,2,2,2,2,2,2,2,2,3            \tag{31}
$$



for both $m=2$ and $m=3$.  Every selected row with $n\ge3$ is
nondecomposable, every corrected polynomial has degree two, and every
origin order is exactly $2M$.  These are finite exact statements.

### 6.2 Parity blocks

The reflection identity for the endpoint specialization says that



$$
\widehat\beta=\beta+\frac m2I
 \quad\hbox{reverses parity}.                              \tag{32}
$$



The scalar gauge cancels in the alternating correction.  Therefore mixed
even/odd wedges map only to even output coefficients, whereas same-parity
wedges map only to odd output coefficients.

Let



$$
e=\left\lfloor\frac D2\right\rfloor+1,\qquad
 o=\left\lceil\frac D2\right\rceil,\qquad K=n+D.            \tag{33}
$$



The two exterior block dimensions are $eo$ and
${e\choose2}+{o\choose2}$.  If $c_e,c_o$ count the even and odd
degrees in $0,\ldots,K$, and $t_e,t_o$ count them in
$3,\ldots,K$, the parity-maximal rank predictions are



$$
\begin{aligned}
 R_{\rm all}^{\rm par}
  &=\min(eo,c_e)+
    \min\!\left({e\choose2}+{o\choose2},c_o\right),\\
 R_{>2}^{\rm par}
  &=\min(eo,t_e)+
    \min\!\left({e\choose2}+{o\choose2},t_o\right).
 \end{aligned}                                             \tag{34}
$$



The replay checks every $m\in\{2,3\}$, $2\le n\le12$, and
$1\le D\le n$, a total of 154 tuples.  Every off-parity entry is exactly
zero, and both ranks equal (34) on every tuple.  The block decomposition is
an all-parameter consequence of (32); maximality in (34) is, in this note,
only a finite exact pattern.  It cannot be promoted to a theorem: the
exact outside-grid tuple (2a) has block ranks



$$
\begin{array}{c|cc|c}
 &\text{even-output block}&\text{odd-output block}&\text{total}\\ \hline
\text{full map}&14&12&26\\
\text{degrees }3,\ldots,28&12&11&23
\end{array}                                                \tag{34a}
$$



against parity-maximal predictions $15+12=27$ and $13+12=25$,
respectively.  The actual rank gap is still $26-23=3$.  This exact
counterexample rules out parity-maximality as the missing all-parameter
argument, but does not classify when the weaker rank gap (13) holds.

## 7. Height diagnostics and the capacity comparison

The replay records separately

* the saturated endpoint-basis height;
* the induced exterior-basis height;
* the LLL-tail coordinate height;
* the primitive ambient exterior height;
* $H(P_x)$, the exact content $c_x$, and $H(F_x)$; and
* the exact value $P_x(i\pi)$ to high precision as a diagnostic.

The full-endpoint rows demonstrate that endpoint basis height is not the
only obstruction: their basis height is exactly one, while the exterior
tail coordinates and normalized analytic height still grow rapidly.  On
the displayed grid:

* all 44 usable rows have the degree-two form $a+cz^2$;
* only the diagonal row $(m,n,D,\nu)=(3,12,12,8)$ has
  $|P_x(i\pi)|<1$, approximately
  $3.658860076\cdot10^{-4}$;
* its relative small-value exponent is only
  $1.102290008\ldots$, and even its centered leading $r=1$ margin in
  (25) remains negative;
* no usable row has a positive margin in (25).

The first bullet is an observed parity choice of the bounded short-vector
search, not a theorem about the whole low image.  The decimal statements
are not used in any proof.

The universal coefficient theorem explains why the present bounds cannot
settle the asymptotic question.  For fixed $m\ge2$, even the full-endpoint
variant retains



$$
\log C_B=m n^2\log n+O_m(n^2),     \tag{35}
$$



inside the cleared auxiliary remainder bound, whereas (23) is only



$$
\mathcal G_\nu^{\rm ctr}
                         =(m-1)n\log n+O_m(n)              \tag{36}
$$



when $D=\nu-1=O(\sqrt n)$.  Frequency centering improves the $O(n)$
term but does not alter this missing factor of $n$.

This comparison is a no-go only for the current universal majorant.  An
upper bound of order $n^2\log n$ is not a lower bound for the true
intrinsic height.  The construction survives conditionally if one can
prove both a rank gap and intrinsic estimates



$$
\log H(F_x)=a n\log n+o(n\log n),\qquad
 \log H(P_x)=b n\log n+o(n\log n)                          \tag{37}
$$



with the corresponding fixed-degree measure inequality.  No such height
or corrected-content theorem is presently known.

## 8. Replay and logical scope

The certificate performs all coefficient and lattice calculations over
the integers or rationals.  It

1. reconstructs the interpolation map and $Q\Delta$ coefficient map;
2. builds saturated endpoint and tail kernels using the transformed-HNF
   lemma and verifies every transformation exactly;
3. checks the exterior embedding, primitive contents, endpoint identity,
   and complete origin-jet vanishing;
4. records the minimal-$\nu$ diagonal exception and its first rescue;
5. checks the minimal full-endpoint grid, all 154 small parity-rank tuples,
   and the exact outside-grid parity-maximality counterexample (2a); and
   and
6. constructs the complete cleared exponential Wronskian sum for every
   usable row and verifies its endpoint polynomial exactly.

The final run remains below the required 2 GiB resident-memory cap.  The
variable observed RSS is printed but deliberately omitted from the JSON,
so the saved result is deterministic.  The finite rank, height, and value
patterns are not extrapolated, and the bounded LLL-coordinate search is
not claimed to solve a shortest-vector problem.
