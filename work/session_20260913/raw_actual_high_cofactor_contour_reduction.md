> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual adjacent high-row cofactors as one contour functional

Date: 2026-09-13. Original bounded continuation by audit_computations.

This note turns the reviewed branch generating functions into an exact formula for actual bordered high-row cofactor quotients. It keeps both canonical endpoint rows. The formula gives a concrete uniform relative-integral estimate that would control adjacent quotients, but that estimate is not proved here.

## 1. The actual nonzero bordered determinant

Use the **unreflected** polynomial $U_n(x)$ from the high-row equations. For $n\ge2$, put



$$
r=n-1,\qquad a=n+1,\qquad b=2n-1=a+r-1.
$$



For a test polynomial $f\in\mathcal P_n$, let



$$
\tau_n(f)=\int_0^1f(x)T_n(x)dx,\qquad
\beta_n(f)=\sum_{j=0}^n(-1)^jf^{(j)}(1),
$$



where $T_n=\mathcal B K_n(1,\cdot)$. The actual normalized polynomial satisfies



$$
\int U_nF_k=0\ (a\le k\le b),\quad
\tau_n(U_n)=-4,\quad\beta_n(U_n)=1.
\tag{1}
$$



The accepted all-degree bordered rank theorem proves independence of these $n+1$ functionals. Choose the fixed monomial columns $1,x,\ldots,x^n$. Set $c_k=2^{-k}\binom{2k}{k}$, and define $D_n$ as the determinant with its first $r$ rows



$$
\left(c_k\int_0^1x^jF_k(x)dx\right)_{j=0}^n,
\qquad k=a,\ldots,b,
$$



and its last two rows $(\tau_n(x^j))_j,(\beta_n(x^j))_j$, in that order. Then



$$
\boxed{D_n\ne0.}
\tag{2}
$$



This is an actual canonical determinant with known endpoint functionals, not a generic minor of the high-row matrix. The row rescaling is explicit and nonzero. In particular,



$$
\beta_n(x^j)=(-1)^j j!\sum_{h=0}^j\frac{(-1)^h}{h!}.
$$



## 2. Exact analytic row generating functions

Define



$$
H_j(z)=\sum_{k\ge0}c_k\left(\int_0^1x^jF_k(x)dx\right)z^k,
\qquad H(z)=(H_0(z),\ldots,H_n(z)).
$$



The reviewed generating function gives explicitly



$$
H_j(z)=\frac1{\pi\sqrt{1-z^2}}\int_0^\pi
\mathcal L_j\!\left(\frac{z(1+\cos\theta)}{1-z^2}\right)d\theta,
$$




$$
\mathcal L_j(w)=\int_0^1x^je^{wx}dx
=\partial_w^j\frac{e^w-1}{w},
\tag{3}
$$



where the apparent value at zero is $1/(j+1)$. These functions are holomorphic for $|z|<1$. For each fixed $0<\rho<1$, the direct integral also gives the uniform bound



$$
|H_j(z)|\le\frac{\exp(2\rho/(1-\rho^2))}{\sqrt{1-\rho^2}}
\quad (|z|\le\rho,\ j\ge0).
\tag{4}
$$



To relate (3) explicitly to the spectral branches, decompose
$x^j=f_{0j}(T)v_0+f_{1j}(T)v_1$ in the exact finite positive-two-measure representation. Then



$$
H_j(z)=\int f_{0j}(\xi)\mathcal P_0(z;\xi)d\mu_0(\xi)
+\frac1{\sqrt3}\int f_{1j}(\xi)\mathcal P_1(z;\xi)d\mu_1(\xi).
\tag{5}
$$



The factor $1/\sqrt3$ follows from the reviewed normalization of the odd branch. The amplitude theorem gives $g_l^2=\exp(-2l\log l+O(l))$, while the branch generating function is bounded by $\exp(C_\rho(l+1))$ at the actual nodes. After multiplication by any fixed polynomial $f_{\sigma j}$, the series for (5) converges absolutely and locally uniformly in the disk. Thus (5) is a justified generating-function identity, not a truncated spectral expansion. Its constants are not asserted uniform in the column degree $j$.

## 3. One common contour functional

For $z_1,\ldots,z_r$ in the unit disk, define



$$
\Phi_n(\mathbf z)=\det
\begin{pmatrix}
H(z_1)\\ \vdots\\H(z_r)\\
(\tau_n(x^j))_{j=0}^n\\
(\beta_n(x^j))_{j=0}^n
\end{pmatrix},\qquad
\Delta(\mathbf z)=\prod_{p<q}(z_q-z_p).
$$



Each contour below is the counterclockwise circle $|z_i|=\rho$, for any fixed $0<\rho<1$. For a symmetric Laurent polynomial $F$, put



$$
\mathcal I_n[F]=\frac{(-1)^{r(r-1)/2}}{r!(2\pi i)^r}
\oint\cdots\oint
\Delta(\mathbf z)\Phi_n(\mathbf z)F(\mathbf z)
\prod_{p=1}^r\frac{dz_p}{z_p^{2n}}.
\tag{6}
$$



Then



$$
\boxed{D_n=\mathcal I_n[1].}
\tag{7}
$$



For proof, expand each of the first $r$ determinant rows by Cauchy's coefficient formula. Antisymmetrizing their factors $z_p^{-i}$, $0\le i<r$, gives



$$
\det(z_p^{-i})_{i,p}
=(-1)^{r(r-1)/2}\Delta(\mathbf z)
\prod_pz_p^{-(r-1)}.
$$



Combining this with the factor $z_p^{-(a+1)}$ gives exponent $a+r=2n$ in (6). The two endpoint rows are fixed and unaffected by antisymmetrization. This also checks the sign and the factor $r!$.

## 4. All adjacent cofactors in one polynomial

Take the extended high-row index list $a,a+1,\ldots,a+r$, and retain the same two endpoint rows. For $0\le j\le r$, let $D_n^{[j]}$ be its square determinant after omitting the high row of index $a+r-j$; keep the other high rows in increasing order. Thus $D_n^{[0]}=D_n$, and $D_n^{[1]}$ replaces only the last old high row $b$ by $b+1$.

With $e_j$ denoting the elementary symmetric polynomial,



$$
\boxed{D_n^{[j]}=\mathcal I_n[e_j(z_1^{-1},\ldots,z_r^{-1})].}
\tag{8}
$$



This is the elementary alternant identity for the exponents $0,\ldots,r$ with $r-j$ omitted. For a direct proof, use
$u^r=e_1u^{r-1}-e_2u^{r-2}+\cdots+(-1)^{r-1}e_r$
at each $u=z_p^{-1}$. In the determinant only the missing exponent survives; moving its row into increasing order cancels the sign of its coefficient. The resulting ratio is $e_j$, with no further sign.

Consequently the exact adjacent-cofactor polynomial is



$$
\boxed{\sum_{j=0}^r\frac{D_n^{[j]}}{D_n}s^j
=\frac{\mathcal I_n[\prod_{p=1}^r(1+s/z_p)]}{\mathcal I_n[1]}.}
\tag{9}
$$



In particular,



$$
\boxed{\frac{D_n^{[1]}}{D_n}
=\frac{\mathcal I_n[\sum_pz_p^{-1}]}{\mathcal I_n[1]}.}
\tag{10}
$$



For the original high rows $F_k$ without the factors $c_k$, the adjacent quotient is $c_b/c_{b+1}=2n/(4n-1)$ times (10). Thus its normalization is completely specified.

These determinants are adjacent maximal minors of the actual extended bordered matrix. Formula (9) resums them coherently before taking absolute values. It is not an estimate obtained by separately multiplying upper bounds on their entries.

## 5. A concrete sufficient relative-integral estimate

Define the normalized total variation of (6) by



$$
\mathfrak C_n(\rho)=
\frac1{r!(2\pi)^r|D_n|}
\int_{|z_1|=\cdots=|z_r|=\rho}
|\Delta(\mathbf z)\Phi_n(\mathbf z)|
\prod_{p=1}^r\frac{|dz_p|}{\rho^{2n}}.
\tag{11}
$$



It is finite, and $\mathfrak C_n(\rho)\ge1$ by the triangle inequality. Equations (8)–(10) prove the exact sufficient bounds



$$
\left|\frac{D_n^{[j]}}{D_n}\right|
\le\binom rj\rho^{-j}\mathfrak C_n(\rho),
\qquad
\left|\frac{D_n^{[1]}}{D_n}\right|
\le\frac{n-1}{\rho}\mathfrak C_n(\rho).
\tag{12}
$$



A bound $\mathfrak C_n(\rho)=O(1)$ on one fixed-radius contour would therefore establish an $O(n)$ actual adjacent high-row cofactor quotient and coherent bounds on the entire adjacent-cofactor polynomial. More flexibly, every identity holds with an n-dependent radius $\rho_n$; the same conclusion follows if $\inf_n\rho_n>0$ and $\mathfrak C_n(\rho_n)=O(1)$. A contour approaching a saddle near the disk boundary may be essential, so no claim that a fixed radius is effective is made. Other contour deformations within the analytic domain, or a direct estimate of the signed ratio in (10), could also be used if total variation is too crude.

This is the concrete remaining obstruction: the reviewed generating-function estimates bound the numerator of (11), but do not lower-bound $|\mathcal I_n[1]|$ relative to that absolute integral. Nonzero $D_n$, positivity of the scalar spectral measures, and analyticity inside the disk do not provide that relative estimate. The contour functional is generally complex and oscillatory; it is not a probability measure. Neither (9) nor (12) proves a norm bound or endpoint noncancellation for the selected HP polynomial without an additional estimate.

The fixed second-order equation in w, with $\xi$ as its spectral parameter, does not by itself remove the growing determinant: its columns involve different polynomial factors $f_{\sigma j}$ of degrees up to $\lfloor n/2\rfloor$, and both endpoint rows remain. The multiple-contour representation retains that structure instead of replacing it by an unjustified fixed-dimensional determinant.

No new HP degree, spectral node, or numerical fit is used in this reduction.
