> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A factorial-Pascal model for the balanced centered-cosh Padé pair

## Integral endpoint formulas and an $O(q^2)$ primitive-height bound

Checked: 2026-08-27 UTC

## 1. Statement

Put



$$
H(y)=\sec\sqrt y,\qquad C(y)=\cos\sqrt y=H(y)^{-1}.
$$



Let $p/B$ be the normal diagonal Padé approximant of type
$[q/q]$ to $H$, and put



$$
A_m=[y^m]\frac{p(y)^2}{B(y)}.
$$



The balanced centered-cosh construction uses the primitive direction
formed by $A_{4q}$ and $A_{4q+1}$.  This note gives an integral
model for that direction in which the defining matrix contains only
binomial coefficients.

For $1\le r\le q$ and $0\le i\le q$, define



$$
W_{r,i}=\binom{2(q+r)}{2i},
 \qquad
 d_i=\det W^{(i)},                                      \tag{1}
$$



where $W^{(i)}$ is obtained by deleting column $i$.  All these
minors are positive.  Define



$$
e_k=\sum_{i=0}^k(-1)^{k-i}\binom{2k}{2i}d_i
 \qquad(0\le k\le q).                                  \tag{2}
$$



Then a Padé pair is



$$
\boxed{
 p(y)=\sum_{i=0}^q\frac{d_i}{(2i)!}y^i,
 \qquad
 B(y)=\sum_{k=0}^q\frac{e_k}{(2k)!}y^k.}                \tag{3}
$$



In particular, all numerator and denominator coefficients are
integers in their natural even-factorial bases.

Let $U_j=|E_{2j}|$, so that



$$
H(y)=\sum_{j\ge0}\frac{U_j}{(2j)!}y^j,
$$



and put



$$
T_j=\sum_{a=0}^j\binom{2j}{2a}U_aU_{j-a}.              \tag{4}
$$



For $m\le4q+1$, define the integer



$$
\boxed{
 w_m=
 2\sum_{i=0}^q\binom{2m}{2i}d_iU_{m-i}
 -\sum_{k=0}^q\binom{2m}{2k}e_kT_{m-k},}                \tag{5}
$$



where a summand with a negative subscript is omitted.  Then



$$
\boxed{A_m=\frac{w_m}{(2m)!}\qquad(m\le4q+1).}         \tag{6}
$$



Consequently the primitive balanced polynomial is, up to an irrelevant
global sign,



$$
\boxed{
 C_q^{\rm prim}(x)=
 \operatorname{prim}\!\left(
 (8q+2)(8q+1)w_{4q}+w_{4q+1}x
 \right).}                                               \tag{7}
$$



The universal nonvanishing theorem for the same Padé pair shows that
both displayed coefficients before primitive reduction are nonzero.

Most importantly, (1)--(7) give the sharper all-parameter bound



$$
\boxed{
 \log H(C_q^{\rm prim})
 \le 3(\log2)q^2+O(q\log q).}                            \tag{8}
$$



Thus the endpoint primitive height is $\exp(O(q^2))$, not merely the
previously proved $\exp(O(q^2\log q))$.  This is an upper bound for
the local endpoint polynomial.  It is not a bound for the normalized
global lift and does not classify $e+\pi$.

## 2. The Pascal kernel

Write a prospective numerator in the even-factorial basis,



$$
p(y)=\sum_{i=0}^q\frac{d_i}{(2i)!}y^i.
$$



For $q<n\le2q$, direct convolution with $C$ gives



$$
(2n)![y^n](pC)
 =(-1)^n\sum_{i=0}^q(-1)^i\binom{2n}{2i}d_i.             \tag{9}
$$



The standard cofactor identity for the $q$-by-$(q+1)$ matrix
$W$ says that $((-1)^id_i)_{i=0}^q$ lies in its right
kernel.  Hence $(d_i)$ lies in the right kernel of the matrix with
entries $(-1)^iW_{r,i}$, and every expression in (9) vanishes.

For completeness, the minors in (1) are positive.  This is the strict
total positivity of the Pascal matrix: if the row indices and column
indices are strictly increasing and every row index exceeds every
column index, the relevant binomial minor is the positive generating
sum of nonintersecting northeast lattice-path families.  Here the row
indices are



$$
2q+2,2q+4,\ldots,4q
$$



and every retained column index belongs to $\{0,2,\ldots,2q\}$, so
the strict case applies.  In particular $W$ has rank $q$, all
$d_i$ are positive, and the kernel is one-dimensional.

For $0\le k\le q$, convolution gives



$$
(2k)![y^k](pC)
 =\sum_{i=0}^k(-1)^{k-i}\binom{2k}{2i}d_i=e_k.           \tag{10}
$$



Define $B$ by (3).  Equation (10) makes the coefficients of
$B-pC$ vanish through degree $q$, and (9) makes them vanish from
degree $q+1$ through degree $2q$.  Therefore



$$
B-pC=O(y^{2q+1}),
 \qquad
 BH-p=H(B-pC)=O(y^{2q+1}).                               \tag{11}
$$



Moreover $B(0)=p(0)=d_0>0$, and $d_q>0$.  Appending to $W$ the
row with index $n=q$ and expanding the resulting square determinant
along that row gives



$$
e_q=(-1)^q
 \det\left(\binom{2n}{2i}\right)_{
             \substack{q\le n\le2q\\0\le i\le q}}.
$$



Strict total positivity makes this determinant positive, so
$e_q\ne0$.  Thus both polynomials in (3) have degree exactly $q$,
and (3) is the normal diagonal Padé pair in a particular positive
normalization.

## 3. Exact Schur specialization formulas

The preceding construction also turns the special secant-alphabet
Schur values into Pascal minors.  Put



$$
S_k=s_{((q+1)^k,q^{q-k})},
 \qquad
 \Sigma_i=s_{(q^q,i)},
$$



under the specialization



$$
e_j=\frac1{(2j)!},
 \qquad
 h_j=\frac{U_j}{(2j)!}.
$$



The Jacobi--Trudi cofactor normalization is



$$
B_{\rm JT}(y)=\sum_{k=0}^q(-1)^kS_ky^k,
 \qquad
 p_{\rm JT}(y)=\sum_{i=0}^q\Sigma_i y^i.
$$



Both this pair and (3) span the same one-dimensional Padé solution,
and their constant coefficients are respectively $S_0$ and $d_0$.
It follows that



$$
\boxed{
 \frac{\Sigma_i}{S_0}=\frac{d_i}{(2i)!d_0},
 \qquad
 \frac{S_k}{S_0}=\frac{(-1)^ke_k}{(2k)!d_0}.}            \tag{12}
$$



Thus every Schur value needed for the numerator and denominator is an
explicit integer Pascal minor or an explicit binomial transform of
such minors, up to the single common factor $S_0/d_0$.  The minors
do not collapse to a simple factorial product in the computed data;
(12), rather than an unsupported product extrapolation, is the exact
all-parameter formula used here.

## 4. Endpoint integrality

Let



$$
E(y)=BH-p.
$$



Since $\operatorname{ord}_0E\ge2q+1$, the exact identity



$$
\frac{p^2}{B}
 =2Hp-H^2B+\frac{E^2}{B}                                \tag{13}
$$



shows that



$$
A_m=[y^m](2Hp-H^2B)\qquad(m\le4q+1).                   \tag{14}
$$



The definition (4) is precisely



$$
H(y)^2=\sum_{j\ge0}\frac{T_j}{(2j)!}y^j.               \tag{15}
$$



Multiplying the two convolutions in (14) by $(2m)!$ now gives (5)
and (6).  Every quantity in (5) is an integer.

The balanced centered-cosh pair in the original $x$-variable uses



$$
F(x)=\frac1{2\cosh\sqrt x}=\frac12H(-x).
$$



If $(P,Q)$ is its positive diagonal Padé normalization, then
$p_*(y)=2P(-y)$, $B_*(y)=Q(-y)$ is a positive scalar multiple of
(3).  Hence



$$
[y^m]\frac{p_*^2}{B_*}=4(-1)^m[x^m]\frac{P^2}{Q}.       \tag{16}
$$



For the even-odd endpoint pair, (16) turns the original primitive
direction $a_{4q}-a_{4q+1}x$ into
$A_{4q}+A_{4q+1}x$.  Clearing the two factorials in (6) gives
(7).

## 5. Height estimate

Set $D=\max_i d_i$.  In row $n=q+r$, the Euclidean norm of any
retained part of $W$ is bounded by



$$
\left(\sum_j\binom{2n}{j}^2\right)^{1/2}
 =\binom{4n}{2n}^{1/2}<2^{2n}.                            \tag{17}
$$



Hadamard's inequality therefore gives



$$
D<\prod_{n=q+1}^{2q}2^{2n}=2^{3q^2+q}.                  \tag{18}
$$



Equation (2) gives the uniform bound



$$
|e_k|\le2^{2q}D.                                        \tag{19}
$$



The beta-value formula for the secant Euler numbers gives the elementary
estimate



$$
U_j\le(2j)!\qquad(j\ge0).                               \tag{20}
$$



Consequently (4) implies



$$
0<T_j\le(j+1)(2j)!.                                     \tag{21}
$$



For $m\le4q+1$, each summand in the first sum of (5), apart from
$d_i$, is at most $(2m)!$.  Each summand in the second sum, apart
from $e_k$, is at most $(m+1)(2m)!$.  Hence



$$
|w_m|
 \le(q+1)(2m)!D\left(2+(m+1)2^{2q}\right).              \tag{22}
$$



Using $m\le4q+1$, (7), (18), and (22) gives the completely explicit
bound



$$
\begin{split}
 H(C_q^{\rm prim})
 &\le (8q+2)(8q+1)(q+1)(8q+2)!\\
 &\quad\cdot 2^{3q^2+q}\left(2+(4q+2)2^{2q}\right).
                                                               \tag{23}
 \end{split}
$$



Taking logarithms proves (8), because every term in (23) other than
$2^{3q^2}$ contributes only $O(q\log q)$.

## 6. Logical boundary and replay

The factorial-Pascal transformation removes a spurious factorial cost
from the earlier row-by-row clearing.  It proves a genuine quadratic
log-height upper bound for the primitive endpoint pair.  It does not
show that this height is small enough for the analytic measure ledger:
the Schwarz gain in the balanced family is only $2q\log q+O(q)$, and
the normalized global lift still has to be controlled.  Nor does this
upper bound estimate the exact endpoint gcd or prove any lower bound.

The companion files are:

* `scripts/centered_cosh_factorial_pascal_height_certificate.py`;
* `results/centered_cosh_factorial_pascal_height_certificate.json`;
* `results/centered_cosh_factorial_pascal_height_hashes.sha256`.

The deterministic replay checks the Pascal cofactor kernel, the
factorial-basis Padé identities, the Schur ratios, the endpoint integer
formula, the explicit bounds, and agreement with direct rational
series on a declared exact grid.  Finite checks are not used in the
all-parameter proof.
