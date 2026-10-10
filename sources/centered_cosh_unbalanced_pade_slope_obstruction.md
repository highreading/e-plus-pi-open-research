> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An unbalanced centered-cosh Padé decomposition and the one-third slope obstruction

Checked: 2026-08-27 UTC

## 1. Scope and verdict

Put



$$
F(x)=\frac1{2\cosh\sqrt x}=\sum_{j\geq0}f_jx^j,
 \qquad {\cal P}_a=\mathbb Q[x]_{\leq a},                 \tag{1}
$$



with ${\cal P}_a=0$ for $a<0$.  This note gives an exact
all-parameter decomposition for one parity block of the unbalanced
centered-cosh lower lift.  If the last constrained $x$-coefficient is



$$
B=2M+\sigma,
 \qquad \sigma\in\{0,1\},                                \tag{2}
$$



and the factor degree is $d=M+r$, the block is



$$
V_{M,r}^{(\sigma)}=
 \left\{C\in{\cal P}_{M+r}:
 [x^j](FC)=0\quad(M+r+1\leq j\leq2M+\sigma)\right\}.     \tag{3}
$$



For $1\leq r\leq M$, it is the direct sum of shifted denominators
from the two neighboring normal Padé entries on the anti-diagonal
$L+D=2M+\sigma$.  In the codimension-positive range, its product
image is a three-summand direct sum of dimension $6r-3\sigma$.
The codimension in ${\cal P}_{2d}$ is exactly



$$
\boxed{\delta=2M-4r+3\sigma+1=3(B-d)-d+1.}              \tag{4}
$$



Thus $B-d$, the number of tail equations in one parity block, has a
sharp structural transition at one third of the factor degree.  In the
original lower lift this is



$$
M=\frac{n+t}{4}+O(1),\qquad
 r=\frac{n-t}{4}+O(1),\qquad
 \delta=\frac{3t-n}{2}+O(1).                              \tag{5}
$$



The exact minimum-degree question reduces to one explicit square jet
determinant.  Exact secant grids make that determinant nonzero, but this
note does **not** extrapolate those grids.  In particular, it does not
claim an all-parameter nonvanishing theorem for that determinant, nor
does a one-block statement rule out cancellation between the two
parity blocks.

The arithmetic ledger is nevertheless decisive about the currently
proved majorants.  The relevant Padé entries have a common Schur
clearing and primitive coefficient height $\exp(O(M^2))$.  A direct
minor construction on the product image costs $O(rM^2)$ in logarithmic
height.  Even an optimistic structured reduction back to $O(M^2)$
would be quadratic in $n$, whereas centered Schwarz gain is only
$2t\log n+O(n)$.  Hence an unbalanced linear tail does not evade the
present $n^2$-versus-$n\log n$ loss.  This is a limitation of the
proved height method, not a proof that a much smaller primitive vector
cannot exist.

## 2. Normal Padé entries on one anti-diagonal

For nonnegative $L,D$, let $(P_{L,D},Q_{L,D})$ denote a Padé pair



$$
\deg P_{L,D}=L,\qquad \deg Q_{L,D}=D,\qquad
 FQ_{L,D}-P_{L,D}=O(x^{L+D+1}),                            \tag{6}
$$



with nonzero denominator constant.  All entries used below are normal.
Indeed, set



$$
H(y)=2F(-y)=\sec\sqrt y
     =\prod_{\nu\geq0}(1-t_\nu y)^{-1}
     =\sum_{j\geq0}h_jy^j,
 \qquad t_\nu=\frac4{\pi^2(2\nu+1)^2}>0.                 \tag{7}
$$



After row and column signs, the denominator determinant is



$$
\det[f_{L+i-j}]_{i,j=1}^{D}
   =\mathord\pm2^{-D}s_{(L^D)}(t_0,t_1,\ldots)\ne0.       \tag{8}
$$



The same Jacobi--Trudi argument with the terminal denominator column or
the numerator row appended proves that the denominator and numerator
have the exact degrees in (6).  This remains valid when $L<D$; in
particular it covers the lower anti-diagonal entry used when
$\sigma=1$.

Define



$$
\begin{array}{c|c|c}
       &\text{numerator degree}&\text{denominator degree}\\ \hline
 (P,Q)&M+\sigma&M\\
 (R,G)&M+1-\sigma&M+2\sigma-1.
 \end{array}                                               \tag{9}
$$



Thus $(P,Q)=(P_{M+\sigma,M},Q_{M+\sigma,M})$ and


$$
(R,G)=(P_{M+1-\sigma,M+2\sigma-1},
Q_{M+1-\sigma,M+2\sigma-1})
$$

.  For $M=1,\sigma=0$, the
second denominator is the constant $G=1$.

Both entries have total index $B=2M+\sigma$.  Subtracting their Padé
identities gives



$$
RQ-PG=O(x^{B+1}).                 \tag{10}
$$



The left side has degree at most $B+1$, and exactly one summand has
that degree: it is $RQ$ when $\sigma=0$, and $-PG$ when
$\sigma=1$.  Normality therefore gives



$$
\boxed{RQ-PG=\kappa x^{B+1},\qquad\kappa\ne0.}           \tag{11}
$$



If $Q$ and $G$ had a common root, (11) would force that root to be
zero.  Their constant terms are nonzero, so



$$
\gcd(Q,G)=1.                  \tag{12}
$$



The distinction in (9) is essential.  For even $B$, the companion is
the upper entry $[(M+1)/(M-1)]$.  For odd $B$, it is the lower
entry $[M/(M+1)]$.  Treating both terminal parities with the same
companion gives a wrong dimension count.

## 3. Exact factor-space decomposition

Let



$$
c=B-d=M+\sigma-r                                      \tag{13}
$$



be the number of equations in (3).  They have full row rank.  When
$c>0$, select the terminal $c$ coefficient columns



$$
2r-\sigma+1,\ldots,M+r.           \tag{14}
$$



With rows indexed by $M+r+1,\ldots,2M+\sigma$, the selected square
matrix is, up to row and column signs and a factor $2^{-c}$,



$$
[h_{c+i-j}]_{i,j=0}^{c-1},\qquad
 \det[h_{c+i-j}]_{i,j=0}^{c-1}=s_{(c^c)}(t)>0.            \tag{15}
$$



The assertion is immediate when $c=0$.  Hence



$$
\dim V_{M,r}^{(\sigma)}=2r-\sigma+1.              \tag{16}
$$



The Padé zero blocks in (6) show that



$$
Q{\cal P}_{r-\sigma}\subseteq V_{M,r}^{(\sigma)},
 \qquad
 G{\cal P}_{r-1}\subseteq V_{M,r}^{(\sigma)}.            \tag{17}
$$



For the first inclusion, both the denominator-degree and
numerator-degree bounds must be used; the latter removes the final shift
when $\sigma=1$.  For the second inclusion the numerator bound is
active when $\sigma=0$, while the denominator bound is active when
$\sigma=1$.

If $QA+GB=0$ with
$\deg A\leq r-\sigma$ and $\deg B\leq r-1<M$, then
(12) gives $Q\mid B$, hence $A=B=0$.  The dimensions in (16)--(17)
now agree, proving the exact direct sum



$$
\boxed{
 V_{M,r}^{(\sigma)}
   =Q{\cal P}_{r-\sigma}\ \oplus\ G{\cal P}_{r-1}.}     \tag{18}
$$



This proof is all-parameter.  It uses one positive rectangular Schur
minor, not a finite rank pattern.

## 4. Product image and its codimension

Squaring (18) gives the sum



$$
\left(V_{M,r}^{(\sigma)}\right)^2
 =Q^2{\cal P}_{2r-2\sigma}
  +QG{\cal P}_{2r-\sigma-1}
  +G^2{\cal P}_{2r-2}.                                    \tag{19}
$$



Assume



$$
M\geq2r-\sigma.                  \tag{20}
$$



Then (19) is direct.  Indeed, reduce



$$
Q^2A+QGB+G^2C=0                                         \tag{21}
$$



modulo $Q$.  Equations (12) and (20) give $Q\mid C$ and



$$
\deg C\leq2r-2<M,
$$



so $C=0$.  After division by $Q$, the same argument gives
$Q\mid B$, while



$$
\deg B\leq2r-\sigma-1<M,
$$



so $B=0$, and then $A=0$.  Therefore



$$
\boxed{
 \left(V_{M,r}^{(\sigma)}\right)^2
 =Q^2{\cal P}_{2r-2\sigma}\ \oplus\
  QG{\cal P}_{2r-\sigma-1}\ \oplus\
  G^2{\cal P}_{2r-2}.}                                   \tag{22}
$$



Its dimension is



$$
(2r-2\sigma+1)+(2r-\sigma)+(2r-1)=6r-3\sigma.           \tag{23}
$$



The ambient product space is ${\cal P}_{2d}$, of dimension
$2M+2r+1$.  Subtracting (23) proves (4).  Notice also that



$$
\delta=2(M-2r+\sigma)+\sigma+1.                          \tag{24}
$$



Thus (20) is exactly the positive-codimension regime permitted by the
parity of $\delta$: $\delta\geq1$ when $\sigma=0$, and
$\delta\geq2$ when $\sigma=1$.

Dimension alone always gives a nonzero product of degree at most
$\delta$, because



$$
\dim(V^2)+\dim{\cal P}_{\delta}-(2d+1)=1.                \tag{25}
$$



Whether degree $\delta$ is the exact minimum is a determinant
question, not a dimension theorem.

## 5. The exact high-tail determinant

Order the columns in (22) by increasing monomial multiplier, and let
${\mathsf H}_{M,r}^{(\sigma)}$ be their coefficient matrix in the
rows



$$
x^\delta,x^{\delta+1},\ldots,x^{2d}.              \tag{26}
$$



There are $6r-3\sigma$ rows and the same number of columns.  Hence



$$
\boxed{
 \det{\mathsf H}_{M,r}^{(\sigma)}\ne0
 \quad\Longleftrightarrow\quad
 \min\{\deg T:0\ne T\in(V_{M,r}^{(\sigma)})^2\}=\delta.}                \tag{27}
$$



This determinant has a useful small-jet form.  Reversal preserves the
high-tail rank.  Write



$$
\widehat Q(y)=y^{\deg Q}Q(1/y),\qquad
 \widehat G(y)=y^{\deg G}G(1/y).                          \tag{28}
$$



Both are units in $\mathbb Q[[y]]$.

If $\sigma=0$, put



$$
H(y)=y^2\frac{\widehat G(y)}{\widehat Q(y)}.       \tag{29}
$$



After reordering columns and multiplying by the unit
$\widehat Q^2$, (27) is the coefficient determinant through degree
$6r-1$ of



$$
\begin{array}{lll}
 1,y,\ldots,y^{2r};&
 H,yH,\ldots,y^{2r-1}H;&
 H^2,yH^2,\ldots,y^{2r-2}H^2.
 \end{array}                                               \tag{30}
$$



If $\sigma=1$, put instead



$$
K(y)=y\frac{\widehat Q(y)}{\widehat G(y)}.        \tag{31}
$$



After factoring the unit $\widehat G^2$, the determinant is the
coefficient determinant through degree $6r-4$ of



$$
\left\{y^j,\ y^jK,\ y^jK^2:0\leq j\leq2r-2\right\}.     \tag{32}
$$



Equations (30)--(32) are exact identities, not numerical models.  They
also identify the missing theorem very sharply: it is a type-I
Hermite--Padé perfectness statement for a ratio of two neighboring
secant Padé denominators.

At $r=1,\sigma=1$, (32) is automatically nonzero.  Indeed
$K=k_1y+O(y^2)$, with $k_1\ne0$, and the coefficient matrix of
$1,K,K^2$ through degree two has determinant $k_1^3$.

For comparison, at $r=1,\sigma=0$, write



$$
H=y^2(r_0+r_1y+r_2y^2+r_3y^3+O(y^4)).                   \tag{33}
$$



With the column order in (30), the determinant is



$$
r_0\left(2r_1^3-3r_0r_1r_2+r_0^2r_3\right).             \tag{34}
$$



This is not forced by coprimality.  Nor can it currently be justified by
an ordinary positive-alphabet or Stieltjes argument: exact secant data
show that the relevant reversed quotient eventually loses the required
coefficient signs, and its denominators need not have only real roots.
Thus (34), and a fortiori its all-$r$ analogue, needs a genuinely
signed Schur or special Padé-minor proof.

## 6. Translation to the lower-lift parameters

For the original endpoint space of degree $D=n-1$, write



$$
C(z)=C_0(z^2)+zC_1(z^2).                                 \tag{35}
$$



For $\epsilon\in\{0,1\}$, the corresponding factor block has



$$
d_\epsilon=\left\lfloor\frac{n-1-\epsilon}{2}\right\rfloor,
 \qquad
 B_\epsilon=\left\lfloor\frac{n+t-\epsilon}{2}\right\rfloor.           \tag{36}
$$



Its constraints are the consecutive interval
$d_\epsilon+1,\ldots,B_\epsilon$.  Write



$$
B_\epsilon=2M_\epsilon+\sigma_\epsilon,qquad
 r_\epsilon=d_\epsilon-M_\epsilon.                       \tag{37}
$$



Whenever $1\leq r_\epsilon\leq M_\epsilon$, Sections 2--5 apply
verbatim.  Uniformly in the parity choices,



$$
\begin{aligned}
 d_\epsilon&=\frac n2+O(1),&
 B_\epsilon-d_\epsilon&=\frac t2+O(1),\\
 M_\epsilon&=\frac{n+t}{4}+O(1),&
 r_\epsilon&=\frac{n-t}{4}+O(1),\\
 \delta_\epsilon&=\frac{3t-n}{2}+O(1),&
 6r_\epsilon-3\sigma_\epsilon&=\frac32(n-t)+O(1).
 \end{aligned}                                             \tag{38}
$$



Thus a tail with $t/n>1/3$ moves each single block into a
positive, eventually linearly growing codimension.  A polynomial of
degree at most one in $x$, equivalently an even quadratic in $z$,
would require a rank failure in an increasingly overdetermined high
coefficient system.  More precisely, the rows of degrees
$2,3,\ldots,2d$ outnumber the product-image dimension by



$$
\delta-2.                    \tag{39}
$$



This explains the observed one-third transition without extrapolating
the determinant.

There is an important logical boundary.  The full even endpoint-product
image is



$$
V_0^2+xV_1^2.                    \tag{40}
$$



High terms from the two summands may cancel.  Separate nonvanishing of
the one-block determinants would not by itself prove that (40) has no
quadratic.  A full slope theorem needs either a coupled determinant or a
special intersection theorem for these two product spaces.

## 7. A uniform Schur clearing

The secant alphabet has



$$
e_j(t_0,t_1,\ldots)=\frac1{(2j)!}.                \tag{41}
$$



For a general entry $[L/D]$, the transformed denominator cofactors
are



$$
S_k=s_{((L+1)^k,L^{D-k})}(t),\qquad0\leq k\leq D.        \tag{42}
$$



Up to a common nonzero scalar, the original denominator is
$\sum_{k=0}^DS_kx^k$.  This applies to both $Q$ and $G$ in (9).

Put



$$
W_{M,\sigma}=(M+\sigma)(M+1),\qquad
 {\mathfrak D}_{M,\sigma}=
 \prod_{p\leq4M+2\sigma}
 p^{\left\lfloor2W_{M,\sigma}/(p-1)\right\rfloor}.       \tag{43}
$$



Then ${\mathfrak D}_{M,\sigma}$ clears every cofactor in (42) for
both entries in (9).  To see this, use dual Jacobi--Trudi.  Every term is
a product of elementary functions $e_{a_i}=1/(2a_i)!$, with



$$
\sum_i a_i=|\lambda|\leq W_{M,\sigma},qquad
 \max_i a_i\leq2M+\sigma.                                \tag{44}
$$



For every prime $p$,



$$
v_p\!\left(\prod_i(2a_i)!\right)
 \leq\sum_i\frac{2a_i}{p-1}
 \leq\frac{2W_{M,\sigma}}{p-1},                           \tag{45}
$$



and no prime larger than $4M+2\sigma$ occurs.  This proves the
clearing assertion term by term.

There is also an $\exp(O(M^2))$ coefficient bound after clearing.
For (42), dropping all row constraints in the tableau and retaining the
strict columns gives



$$
S_k\leq e_D^Le_k=\frac1{((2D)!)^L(2k)!}.                 \tag{46}
$$



The usual estimates



$$
\sum_{p\leq X}\frac{\log p}{p-1}\leq\log X+O(1),
 \qquad
 \log N!=N\log N-N+O(\log N)                             \tag{47}
$$



show that the $2M^2\log M$ terms in
$\log{\mathfrak D}_{M,\sigma}$ and the factorial denominator in
(46) cancel.  Uniformly for all cofactors of $Q$ and $G$,



$$
\boxed{
 {\mathfrak D}_{M,\sigma}S_k\in\mathbb Z,qquad
 \log\max_k|{\mathfrak D}_{M,\sigma}S_k|=O(M^2).}        \tag{48}
$$



Primitive gcd removal can only reduce this height.  No lower bound for
that content is asserted.

## 8. Determinant height and centered Schwarz ledger

Use the cleared Padé vectors from (48) in the product basis (22).  Its
integer coefficient matrix has logarithmic entry height $O(M^2)$.
The high-tail determinant has



$$
s=6r-3\sigma                 \tag{49}
$$



columns.  Consequently, a direct maximal-minor or cofactor
construction has the rigorous generic bound



$$
\log H_{\rm cof}=O(rM^2+r\log r).                \tag{50}
$$



This is an upper bound for an explicit cofactor representative whenever
the required rank gap exists.  It is not a lower bound for the smallest
primitive representative.  A special Smith/content theorem could make
the primitive vector much smaller.

For the lower lift, every factor has origin order at least
$n+t+1$.  Its polarized product has



$$
L=2(n+t+1),\qquad K=2n-2,qquad A=L-K=2t+4.              \tag{51}
$$



In centered frequencies $-2,-1,0,1,2$, Schwarz optimization gives



$$
G_{n,t}=A\log\frac{A}{e\pi}-K\log\frac\pi2,
 \qquad
 G_{n,t}=2\tau n\log n+O(n)\quad(t/n\to\tau>0).          \tag{52}
$$



The lift itself adds only polynomial factors to the analytic
coefficient norm: from $|[z^j](2\cosh z)^{-1}|\leq1/2$, Taylor
convolution bounds the auxiliary coefficients by the endpoint
coefficient $\ell^1$-norm times $O(n)$.

For fixed $1/3<\tau<1$, (38) gives



$$
M=\frac{1+\tau}{4}n+O(1),\qquad
 r=\frac{1-\tau}{4}n+O(1).                               \tag{53}
$$



Thus the ordinary determinant bound (50) is $O(n^3)$, even though the
determinant dimension is only $O(n)$.  Suppose optimistically that a
new structured quotient theorem removed the entire factor $r$ and
reduced both endpoint and analytic logarithmic heights to the input
Padé scale $O(M^2)=O(n^2)$.  This would still dominate the available
gain $O(n\log n)$.

For a primitive even quadratic $T=a+bx$, evaluated at
$x=-\pi^2/4$, the same rational-$s=e+\pi$ degree-two measure ledger
as in the lower-lift audit has sufficient margin



$$
G_{n,t}-\log H_{\rm an}-2\log H(T)-O(n).                 \tag{54}
$$



Neither (50) nor the optimistic $O(M^2)$ replacement makes the
certified lower bound for (54) positive.  To change that conclusion one
needs at least one of the following genuinely new inputs:

* primitive content cancelling all but $O(n\log n)$ of the
  $O(M^2)$ Padé scale;
* a direct survivor formula whose intrinsic height is
  $O(n\log n)$, bypassing the cofactor/Schur scale; or
* an analytic construction with gain of order $n^2$.

Equation (54) is a majorant comparison.  It does not prove that the
actual primitive height is $\Omega(n^2)$.

## 9. Exact finite diagnostics and logical status

The companion certificate verifies, with exact rational arithmetic:

* normality of both anti-diagonal Padé entries, including the
  $[M/(M+1)]$ lower entry;
* the cross identity (11) and coprimality;
* the factor decomposition (18), product direct sum (22), and
  codimension (4);
* both reversed jet descriptions (30) and (32);
* nonzero secant high-tail determinants on the displayed bounded grid;
* the exact lower-lift parameter map (36)--(38) on a bounded grid; and
* the clearing divisibility in (43)--(48) on small exact rows.

The finite determinant rows are diagnostics only.  The all-parameter
theorems are (8)--(25), the equivalences (27)--(32), the parameter and
height implications (35)--(54), and the automatic
$r=1,\sigma=1$ case.  No all-parameter secant determinant
nonvanishing, no coupled two-parity slope theorem, and no conclusion
about the arithmetic nature of $e+\pi$ is claimed.

The replay artifacts are:

* `scripts/centered_cosh_unbalanced_pade_slope_obstruction_certificate.py`;
* `results/centered_cosh_unbalanced_pade_slope_obstruction_certificate.json`;
* `results/centered_cosh_unbalanced_pade_slope_obstruction_hashes.sha256`.
