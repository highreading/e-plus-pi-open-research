> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Global Hermite interpolation at the actual dyadic denominator nodes

Date: 2026-09-13. Original bounded construction by audit_computations.

This proves explicit norm bounds for the global scalar Hermite interpolation
map in the requested scaled monomial and local jet coordinates. It then
composes that map with the independently reviewed local actual branch
multiplication maps. All node-dependent determinant amplitudes are retained.
The resulting finite quotient-module operator is exact, but is not identified
with the exceptional Schur block from the high-row rank problem.

## 1. Actual nodes and precisely specified norms

Write $N=2n$, and retain exactly the denominator from
`raw_rational_surrogate_rank_improvement.md`:



$$
M_n=2n+3/4=N+3/4,\quad
J=1+\lfloor\log_2(N/4)\rfloor,\quad
\nu=\left\lceil\frac{4\sqrt{3N}}{\log3}\right\rceil,\quad D=\nu J,
$$





$$
\rho_j=\frac32N2^j,\qquad x_j=N+3/4+\rho_j,
\qquad 0\le j<J.
\tag{1}
$$



Thus $D=O(\sqrt N\log N)$. All statements below hold for sufficiently
large even $N$; the interpolation estimates themselves need only $N\ge8$.

The global polynomial coordinate is $y=z/N^2$. Put



$$
\alpha_j=x_j/N^2,\qquad
r_j=\frac12\sqrt{x_j}\log N,\qquad\eta_j=r_j/N^2.
\tag{2}
$$



The radius $r_j$ is precisely half the complex radius in
`raw_intermediate_holomorphic_jet_bounds.md`. The exact nodes satisfy



$$
0<\alpha_j<1,\qquad |\alpha_i-\alpha_j|\ge1/N\quad(i\ne j),
\qquad N^{-2}\le\eta_j\le1.
\tag{3}
$$



Indeed $2^{J-1}\le N/4$, so
$\alpha_{J-1}\le3/8+1/N+3/(4N^2)<1$. Consecutive gaps are
$3\cdot2^j/(2N)\ge3/(2N)$. Finally $x_j\ge2N$, $x_j<N^2$,
and (2) give the radius bounds in (3).

Let $\mathcal P_{D-1}$ consist of polynomials
$f(y)=\sum_{k=0}^{D-1}c_ky^k$, with the Euclidean coefficient norm
$\|f\|_{\rm coef}=(\sum|c_k|^2)^{1/2}$. Give the jet space
$\bigoplus_{j=0}^{J-1}\mathbb C^\nu$ its ordinary Euclidean norm.
Define the exact linear map



$$
(\mathcal E f)_{j,r}
=[t^r]f(\alpha_j+\eta_jt)
=\frac{\eta_j^r}{r!}f^{(r)}(\alpha_j),
\qquad0\le r<\nu.
\tag{4}
$$



Equivalently, for the actual-parameter polynomial $f(z/N^2)$, these are
its Taylor derivatives scaled by $r_j^r/r!$ at $z=x_j$. No raw
derivative norm or unscaled monomial norm is substituted for (4).

## 2. Explicit global interpolation and inverse bounds

The evaluation matrix has entries



$$
\mathcal E_{(j,r),k}=
\begin{cases}\binom{k}{r}\alpha_j^{k-r}\eta_j^r,&k\ge r,\\0,&k<r.
\end{cases}
$$



Every entry has magnitude at most $2^D$, by (3), and the matrix is
$D$-by-$D$. Hence



$$
\boxed{\|\mathcal E\|_2\le D2^D.}
\tag{5}
$$



Here is an explicit inverse, including its local radius normalization. Set



$$
q_j(y)=\prod_{i\ne j}
\left(\frac{y-\alpha_i}{\alpha_j-\alpha_i}\right)^\nu,
\qquad
\frac1{q_j(\alpha_j+w)}=\sum_{s\ge0}b_{j,s}w^s.
$$



For $0\le r<\nu$, define the Hermite cardinal polynomial



$$
H_{j,r}(y)=q_j(y)\,\eta_j^{-r}(y-\alpha_j)^r
\sum_{s=0}^{\nu-1-r}b_{j,s}(y-\alpha_j)^s.
\tag{6}
$$



Its degree is at most $D-1$. At node $j$, the truncated reciprocal
makes its local Taylor expansion equal to $t^r$ modulo $t^\nu$.
At every other node it has a zero of order at least $\nu$. Therefore



$$
\mathcal E H_{j,r}=e_{j,r},\qquad
\mathcal E^{-1}v=\sum_{j,r}v_{j,r}H_{j,r}.
\tag{7}
$$



For quantitative control, let $\|\cdot\|_1$ denote the sum of the
absolute values of the monomial coefficients. It is submultiplicative.
By (3),



$$
\|q_j\|_1\le(2N)^{D-\nu}.
\tag{8}
$$



On the circle $|w|=1/(2N)$, each factor
$1+w/(\alpha_j-\alpha_i)$ has magnitude at least $1/2$. Thus
Cauchy's coefficient bound gives



$$
|b_{j,s}|\le2^{D-\nu}(2N)^s.
\tag{9}
$$



Using $\eta_j^{-r}\le N^{2r}$ and
$\|(y-\alpha_j)^k\|_1\le2^k$, (6)--(9) imply



$$
\begin{aligned}
\|H_{j,r}\|_1
&\le (4N)^{D-\nu}(2N^2)^r
 \sum_{s=0}^{\nu-1-r}(4N)^s\\
&\le\nu(4N)^{D-1}(N/2)^r
\le\nu(4N)^{2D}.
\end{aligned}
\tag{10}
$$



The Euclidean norm of a coefficient column is at most its coefficient
one-norm. Applying the Frobenius bound to the $D$ inverse columns yields



$$
\boxed{\|\mathcal E^{-1}\|_2
\le\sqrt D\,\nu(4N)^{2D}.}
\tag{11}
$$



In particular, if



$$
\mathfrak h_N=D^{3/2}\nu\,2^D(4N)^{2D},
$$



then



$$
\boxed{\operatorname{cond}_2\mathcal E\le\mathfrak h_N,
\qquad\log\mathfrak h_N=O(D\log N)
=O(\sqrt N\log^2N).}
\tag{12}
$$



The two separate norm bounds (5), (11), not just their product, are explicit.
The estimates are deliberately crude and use no numerical condition-number
experiment. Repeating each scalar coefficient and jet coordinate for two
components gives $\mathcal E_2=\mathcal E\otimes I_2$, up to an
irrelevant coordinate permutation. Its operator and inverse norms are exactly
those of $\mathcal E$.

## 3. The actual global quotient-module multiplication map

Let



$$
\widehat Q(y)=\prod_{j=0}^{J-1}(y-\alpha_j)^\nu.
\tag{13}
$$



The actual rational-surrogate denominator satisfies
$Q(N^2y)=(-1)^D N^{2D}\widehat Q(y)$. A vector polynomial modulo
$\widehat Q$ is represented uniquely by its two components of degree
less than $D$, with their standard scaled monomial coefficient norm.

Using the actual adjacent branch matrix and its reviewed seed normalization,
define the $2D$-by-$2D$ operator



$$
\boxed{\mathcal M_N f
=\operatorname{rem}_{\widehat Q}
 [P_N(N^2y)f(y)].}
\tag{14}
$$



The remainder is componentwise. This is a globally defined finite operator
formed from the actual polynomial branches, not an asymptotic replacement.

Define the positive node amplitudes



$$
d_j=d_N(x_j)=
\left[
\frac{\det(x_jI-K_N)}{\prod_{h=0}^{N-1}a_{h+1}a_{h+2}}
\right]^{1/2}>0,
\quad\mathscr D=\bigoplus_{j=0}^{J-1}d_j I_{2\nu}.
\tag{15}
$$



They are distinct and are not set equal. Let $\mathcal T_j$ be the exact
truncated block Toeplitz multiplication map on jets modulo $t^\nu$ for



$$
A_j(t)=P_N(x_j+r_jt)/d_j,
\qquad\mathscr T=\bigoplus_j\mathcal T_j.
$$



The independently reviewed local jet theorem gives



$$
\|\mathscr T\|,\|\mathscr T^{-1}\|\le
\mathfrak l_N:=2\exp\{C\sqrt N\log N\}.
\tag{16}
$$



The even cut $N=2n$ has no odd seed power. The bound is uniform in the
node and in the multiplicity: on the doubled local disk the coefficients of
both $A_j$ and $A_j^{-1}$ are bounded by a geometric sequence, and
their coefficient norm sums bound the two convolution norms.

Since polynomial remainders modulo $\widehat Q$ preserve all the jets
in (4), the exact composition identity is



$$
\boxed{\mathcal M_N=
\mathcal E_2^{-1}\mathscr D\mathscr T\mathcal E_2,
\qquad
\mathcal M_N^{-1}=
\mathcal E_2^{-1}\mathscr T^{-1}\mathscr D^{-1}\mathcal E_2.}
\tag{17}
$$



This also proves invertibility. Equivalently, the matrix determinant is a
unit in the quotient ring, because every $x_j$ lies strictly above the
actual row spectrum. The analytic inverse jets give its exact inverse in
that quotient ring, not an approximation.

## 4. Standard coefficient norms, with every amplitude retained

Put $d_{\max}=\max_jd_j$, $d_{\min}=\min_jd_j$, and
$\mathfrak B_N=\mathfrak h_N\mathfrak l_N$. Equations (12),
(16), and (17) imply both upper and lower bounds



$$
\boxed{\frac{d_{\max}}{\mathfrak B_N}
\le\|\mathcal M_N\|\le\mathfrak B_N d_{\max},
\qquad
\frac1{\mathfrak B_N d_{\min}}
\le\|\mathcal M_N^{-1}\|\le\frac{\mathfrak B_N}{d_{\min}}.}
\tag{18}
$$



For example, the block with amplitude $d_{\max}$ has norm at least
$d_{\max}/\mathfrak l_N$, since the norm of its inverse-normalized
block is at most $\mathfrak l_N$. Conjugation by $\mathcal E_2$
loses at most $\mathfrak h_N$. The inverse lower bound is analogous.
Thus



$$
\boxed{\left|\log\operatorname{cond}\mathcal M_N
-\log(d_{\max}/d_{\min})\right|
\le2\log\mathfrak B_N=O(\sqrt N\log^2N).}
\tag{19}
$$



This formula shows precisely where the unavoidable scalar variation enters
the globally composed operator in standard monomial norms.

For an explicitly weighted alternative, set



$$
\sigma_N(y)=\sum_jd_jH_{j,0}(y),\qquad
s_N(y)=\sum_jd_j^{-1}H_{j,0}(y).
$$



Their local jets are respectively the constants $d_j$ and $d_j^{-1}$.
In particular $\sigma_Ns_N=1$ modulo $\widehat Q$. Let
$\mathcal S_N$ be scalar multiplication by $\sigma_N$ modulo
$\widehat Q$, on each vector component. Exactly



$$
\mathcal S_N=\mathcal E_2^{-1}\mathscr D\mathcal E_2,
\qquad
\mathcal W_N:=\mathcal S_N^{-1}\mathcal M_N
=\mathcal E_2^{-1}\mathscr T\mathcal E_2.
$$



Hence



$$
\boxed{\|\mathcal W_N\|,\|\mathcal W_N^{-1}\|
\le\mathfrak B_N=
\exp\{O(\sqrt N\log^2N)\}.}
\tag{20}
$$



This is an exact globally composed subexponential operator and inverse in
standard scaled monomial norms, after the explicitly stated scalar quotient
weight. Equivalently, the actual map $\mathcal M_N$ has those bounds
from the standard input norm to the output norm
$\|h\|_{\rm out}=\|\mathcal S_N^{-1}h\|_{\rm coef}$.
This output weight is not identified with the physical endpoint metric.
Nor is $s_N$ the Taylor truncation of the global analytic function
$1/d_N(z)$: its higher local jets are zero by its stated definition.
The positive node values do not assert positivity or invertibility of
$\sigma_N(K_N)$ on the original row space. The proved isomorphism here
is multiplication in the quotient by $\widehat Q$.

## 5. The amplitude distinction is quantitatively necessary

Because all actual nodes lie above the row spectrum,



$$
\frac{d}{dx}\log d_N(x)=\frac12\operatorname{tr}(xI-K_N)^{-1}>0.
$$



Thus $d_{\max}=d_{J-1}$, $d_{\min}=d_0$. The known lower spectral
bound is $\lambda_i(K_N)\ge-N^2+3/8$. Also
$2^{J-1}\ge N/8$, so



$$
x_{J-1}\ge N+3/4+3N^2/16,
\qquad x_0=5N/2+3/4.
$$



For all sufficiently large $N$, these inequalities imply, for every row
eigenvalue,



$$
\frac{x_{J-1}-\lambda_i}{x_0-\lambda_i}
=1+\frac{x_{J-1}-x_0}{x_0-\lambda_i}\ge\frac{17}{16}.
$$



For clarity, the numerator increment is at least $3N^2/32$ once
$N\ge16$, while the denominator is at most
$N^2+5N/2+3/8\le(6/5)N^2$ in the same range. Their quotient exceeds
$1/16$. Taking the determinant ratio yields



$$
\boxed{d_{\max}/d_{\min}\ge(17/16)^{N/2}.}
\tag{21}
$$



Since $\sqrt N\log^2N=o(N)$, (19) and (21) show that the **unweighted**
actual quotient operator $\mathcal M_N$ has condition number at least
$\exp(cN)$ for some $c>0$ and all sufficiently large $N$.
This is fully consistent with the subexponential weighted theorem (20).
Dropping the distinct $d_j$ would lose a real exponential scale.

## 6. Exact scope of the new reduction

The following are now proved for the actual dyadic denominator:

1. Global Hermite evaluation and interpolation in the exact norms (4) have
   the explicit bounds (5), (11).
2. Actual branch multiplication on the full two-component quotient module
   has the exact factorization and inverse (17).
3. Its standard-norm conditioning is the amplitude ratio up to a
   subexponential factor, as in (19); its explicitly weighted form and
   inverse satisfy (20).

The exceptional matrix in the rank reduction is a particular
$(k+2)$-by-$k$ projected Schur block with
$k=D+O(\sqrt N)$. The map (14) instead acts on a complete
two-component quotient module of dimension $2D$. No identity identifying
these maps, their subspaces, or their metrics has been proved here.
In particular the low-factor constraints, the retained-row projection,
the actual cardinal/amplitude matrix $S$, and the physical map
$S^{-1}F_{LL}^{-1/2}U_e$ from the exceptional reduction have not been
replaced by (20). An exact bridge retaining those operations is the next
mathematical requirement before this interpolation theorem could imply
a bound for the high-row kernel or the endpoint remainder.
