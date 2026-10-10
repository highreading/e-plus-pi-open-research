> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Holomorphic and repeated-node jet bounds in the intermediate positive regime

Date: 2026-09-13. Original addendum by audit_computations to
`raw_intermediate_positive_parameter_conditioning.md`.

This extends that note's new boundary-energy estimate to a shrinking relative
complex neighborhood of each real parameter. It gives upper bounds for actual
branch jets and inverse jets at the repeated denominator nodes. It does not
give a confluent interpolation inverse or determinant lower bound.

## 1. Statement

Use the actual $P_N$, seeds, and normalizations from the preceding note.
For real $x\ge2N$, put



$$
\rho_N(x)=\sqrt x\log N,\qquad
H_N(x)=1+(\log N)^2+N\log N/\sqrt x.
\tag{1}
$$



On the half-plane $\Re z>N+3/4$, define the nonvanishing holomorphic
scalar



$$
d_N(z)=\left[
\frac{\det(zI-K_N)}{\prod_{h=0}^{N-1}a_{h+1}a_{h+2}}
\right]^{1/2},
\tag{2}
$$



using its positive square root on the real positive axis. This is possible
because the row eigenvalues are real and at most $N+3/4$. Define
$\mathcal P_N(z)=P_N(z)/d_N(z)$. The exact Casoratian gives
$\det\mathcal P_N=(-1)^N$, so its two singular values have product one.

For all sufficiently large $N$, uniformly for $x\ge2N$ and
$|z-x|\le\rho_N(x)$,



$$
\boxed{\max\{\|\mathcal P_N(z)\|,
\|\mathcal P_N(z)^{-1}\|\}
\le (1+x)^{(N\bmod2)/2}\exp\{C H_N(x)\}.}
\tag{3}
$$



The constant is absolute. In particular, for every integer $r\ge0$,



$$
\boxed{\max\{\|\mathcal P_N^{(r)}(x)\|,
\|(\mathcal P_N^{-1})^{(r)}(x)\|\}
\le\frac{r!}{\rho_N(x)^r}
(1+x)^{(N\bmod2)/2}e^{C H_N(x)}.}
\tag{4}
$$



After changing the absolute constant, the same actual-scale bounds hold:



$$
\boxed{\max\left\{
\frac{\|P_N^{(r)}(x)\|}{d_N(x)},
d_N(x)\|(P_N^{-1})^{(r)}(x)\|\right\}
\le\frac{r!}{\rho_N(x)^r}
(1+x)^{(N\bmod2)/2}e^{C H_N(x)}.}
\tag{5}
$$



All derivatives in these formulas are with respect to the actual parameter,
not a rescaled variable. The constants do not depend on $r$.

## 2. A relative boundary-resolvent perturbation estimate

For each preceding cut $j\le N$, let



$$
B_j(z)=\iota_j^T(zI-K_j)^{-1}\iota_j,\qquad
d=x-\lambda_{\max}(K_j).
$$



The spectral bound gives $d\ge x-j-3/4\ge x/3$ for all large $N$.
With $h=z-x$, $H=xI-K_j$, and $Y=H^{-1/2}\iota_j$, exactly



$$
B_j(z)-B_j(x)
=Y^*[(I+hH^{-1})^{-1}-I]Y.
$$



The columns of $V=YB_j(x)^{-1/2}$ are orthonormal. Therefore, whenever
$|h|<d$,



$$
\boxed{\|B_j(x)^{-1/2}[B_j(z)-B_j(x)]B_j(x)^{-1/2}\|
\le\frac{|h|}{d-|h|}.}
\tag{6}
$$



This uses a real positive energy factorization only at the real center. It
does not assert positivity of a complex resolvent or replace a complex
bilinear expression by a squared norm.

On the disk in (3), $\rho_N(x)/x\le\log N/\sqrt{2N}\to0$, uniformly
in $x$. Thus (6) is at most



$$
C\log N/\sqrt x.
\tag{7}
$$



## 3. The late and early cuts remain controlled

For $j\ge A\log N$, the proved real boundary estimate is



$$
B_j(x)=b_j(x)(I+E_j),\quad b_j=m(x/j^2)/j^2>0,
\quad\|E_j\|\le C_0(\log N/j+\log N/\sqrt x).
$$



Equations (6)--(7) convert this directly into the complex estimate with the
same right side and an enlarged absolute constant: indeed
$\|B_j(z)-B_j(x)\|\le\|B_j(x)\|\,|h|/(d-|h|)$.
The exact formula $T_j(z)=\Gamma_j^{-1}B_j(z)^{-1}$, and
$\Gamma_j=(j^2/4)(I+O(1/j))$, consequently give



$$
T_j(z)=\lambda(x/j^2)(I+E_j^{\mathbb C}(z)),\qquad
\|E_j^{\mathbb C}(z)\|
\le C_1(\log N/j+\log N/\sqrt x).
\tag{8}
$$



The scalar in (8) is evaluated at the real center and is positive. This is
sufficient for a uniform bound, and no holomorphic asymptotic expansion of
that scalar has been assumed. Taking $A$ sufficiently large ensures that
all these errors are at most $1/2$, for all large $N$. Their sum is
$O(H_N(x))$.

For the preceding cuts from a sufficiently large fixed $J_*$ to
$J_N=O(\log N)$, the exact real estimate from the preceding note is
$T_j(x)=\tau_j(I+O(1/j))$, $\tau_j>0$, uniformly in $x\ge2N$.
Since $\Gamma_j=(j^2/4)(I+O(1/j))$, its exact inversion also shows
that $B_j(x)$ is a positive scalar times $I+O(1/j)$. Applying (6)
again gives



$$
T_j(z)=\tau_j(I+O(1/j+\log N/\sqrt x)).
\tag{9}
$$



Choose $J_*$ large enough once and for all. These errors are at most
$1/2$, and their sum is
$O(1+\log\log N+(\log N)^2/\sqrt x)$, which is absorbed in $H_N$.

For either fixed initial cut, each entry of $P_J(z)$ has degree at most
$\lceil J/2\rceil$. On the disk $|z-x|\le\rho_N(x)$,
$|z|\le2x$ and all $|z-\lambda_i(K_J)|\ge x/2$, eventually.
The exact Casoratian therefore gives



$$
\frac{\|P_J(z)\|}{|\det P_J(z)|^{1/2}}
\le C_J(1+x)^{(J\bmod2)/2}.
\tag{10}
$$



The inverse normalized matrix has the same norm because it is two-by-two
and its determinant has magnitude one. This preserves the actual even and
odd seed costs.

For any invertible two-by-two factor $A$,
$\|A\|/|\det A|^{1/2}=\sqrt{\operatorname{cond}_2 A}$.
Apply this to the exact ordered transfer product, using
$\log\operatorname{cond}(I+E)\le3\|E\|$. All scalar factors cancel
after determinant normalization. Equations (8)--(10) prove (3), including
its inverse bound.

## 4. Cauchy bounds and the actual determinant scale

The entire disk in (3) lies in $\Re z>N+3/4$, for all large $N$.
Thus $\mathcal P_N$ and its inverse are holomorphic on a neighborhood
of that closed disk. Matrix Cauchy estimates prove (4).

Writing the determinant in terms of the actual row eigenvalues gives



$$
\log\frac{d_N(x+h)}{d_N(x)}
=\frac12\sum_{i=1}^N
\log\left(1+\frac{h}{x-\lambda_i(K_N)}\right).
$$



For $|h|\le\rho_N(x)$, $|h|/(x-\lambda_i)\le1/2$, eventually.
Since $|\log(1+u)|\le2|u|$ on that disk,



$$
\left|\log\frac{d_N(x+h)}{d_N(x)}\right|
\le\frac{N\rho_N(x)}{x-N-3/4}
\le\frac{3N\log N}{\sqrt x}.
\tag{11}
$$



Consequently both $|d_N(x+h)/d_N(x)|$ and its reciprocal are bounded
by $\exp\{3N\log N/\sqrt x\}$. Combine this with (3), and apply
Cauchy directly to $P_N(z)/d_N(x)$ and
$d_N(x)P_N(z)^{-1}$, to obtain (5).

The logarithmic derivatives themselves also have the exact formula and bound



$$
\left|\frac{d^r}{dx^r}\log d_N(x)\right|
\le\frac{(r-1)!N}{2(x-N-3/4)^r},\qquad r\ge1.
\tag{12}
$$



## 5. A uniformly conditioned local jet multiplication isomorphism

There is one finite inverse conclusion that follows without a many-node
interpolation estimate. Fix any multiplicity $\nu\ge1$, and use the local
coordinate $t=2(z-x)/\rho_N(x)$. Set



$$
A_x(t)=P_N(x+\rho_N(x)t/2)/d_N(x).
$$



By (3) and (11), both $A_x$ and $A_x^{-1}$ have norm at most



$$
E_N(x)=(1+x)^{(N\bmod2)/2}\exp\{C H_N(x)\}
$$



on $|t|\le2$. Their Taylor coefficient matrices therefore satisfy
$\|A_{x,k}\|,\|(A_x^{-1})_k\|\le E_N(x)2^{-k}$.
On vector Taylor polynomials modulo $t^\nu$, give the coefficient vectors
their ordinary Euclidean norm. Multiplication by $A_x$ is the exact
lower block Toeplitz matrix



$$
\mathcal T_{x,\nu}=(A_{x,r-s})_{0\le s\le r<\nu}.
$$



The convolution norm is bounded by the coefficient norm sum. The Taylor
product identity $A_xA_x^{-1}=I$ shows that the inverse Toeplitz matrix
is exactly the analogous truncation for $A_x^{-1}$. Hence



$$
\boxed{\|\mathcal T_{x,\nu}\|\le2E_N(x),\qquad
\|\mathcal T_{x,\nu}^{-1}\|\le2E_N(x).}
\tag{13}
$$



These estimates are uniform in the multiplicity, not merely for a fixed
number of derivatives. For finitely many distinct actual denominator nodes
$x_i$, the direct-sum operator has both bounds with
$2\max_iE_N(x_i)$. This statement preserves the per-node determinant scale
$d_N(x_i)$ and the local radius $\rho_N(x_i)/2$: they specify the exact
input/output jet coordinates. It must not be reinterpreted as a bound in an
unweighted monomial or physical endpoint norm.

Thus multiplication by the actual two-by-two branch matrix is invertible on
these local quotient modules, with the explicit bounds (13). Its conditioning
is subexponential in $N$ for even cuts (in particular $N=2n$) or on a
bounded quadratic range $x\le C'N^2$. For arbitrary odd cuts and unbounded
$x$, the displayed $(1+x)$ seed factor in the condition bound remains.
No claim that the exceptional Schur matrix equals this multiplication map is
made.

## 6. What this does and does not supply for repeated nodes

For $N=2n$, every rational-surrogate denominator node lies in
$[2N,C'N^2]$, and the seed power in (3)--(5) is absent. Thus the actual
matrix and inverse jets through the required multiplicity
$\nu=O(\sqrt n)$ have the explicit factorial-Cauchy bound (5), with
overall scale $\exp\{O(\sqrt n\log n)\}$.

This controls individual two-branch jets and the specific local
multiplication isomorphism (13) in the newly needed intermediate range. The
passage between a global polynomial subspace and the direct sum of its local
jets is a different, many-node Hermite interpolation map. Its least singular
value in the required physical norm is not a consequence of (13). That
many-node lower bound, and the bridge from it to the actual exceptional Schur
block with parity factors and physical normalization retained, remain
additional mathematical problems.
