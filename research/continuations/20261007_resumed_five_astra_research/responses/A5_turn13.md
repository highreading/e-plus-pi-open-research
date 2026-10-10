> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Eventual signed nonvanishing for the actual compact residual determinant

## 1. Main result and proof status

The rationality or irrationality of $e+\pi$ remains unresolved.

There is, however, a new unconditional analytic result for the **actual compact family**. The overlap of the two positive measures and the negative atom can be controlled at the whole-determinant level.

Throughout, retain the original compact matrix boundaries


$$
k\ge2,\qquad 0\le m<2k,\qquad 0\le j<k,
$$


and the residual specified in the assignment:


$$
T^{(k)}_{rj}
=
\int x^jP_{k+r}(x)\,d\mu(x)
-
(-1)^jP_{k+r}(-1),
\qquad 0\le r,j<k.
$$



Define the positive factorial determinant


$$
Z_k
=
\det\bigl((2k+2i+2j)!\bigr)_{0\le i,j<k}.
$$



### New theorem

For every integer $k\ge64$,


$$
\boxed{
\frac12e^{-2k}Z_k
\le
\det T^{(k)}
\le
2e^{-k}Z_k.
}
\tag{1.1}
$$


In particular,


$$
\boxed{\det T^{(k)}>0\qquad(k\ge64).}
\tag{1.2}
$$



The same comparison method also proves nonvanishing of the **actual affine coefficient**, not merely of its rank-one period matrix:


$$
\boxed{(-1)^kH_{1,k}>0\qquad(k\ge64).}
\tag{1.3}
$$



Consequently, on the explicit infinite set


$$
\mathcal K=\{64,65,66,\ldots\},
$$


the actual primitive denominator is defined, and the whole primitive error is strictly positive:


$$
\boxed{
q_k=\frac{|H_{1,k}|}{G_k},\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k},
\qquad
0<q_k(e+\pi)-p_k.
}
\tag{1.4}
$$


Here, without replacement by a frame content or a restricted-prime divisor,


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|)
$$


is the final **ALL-prime** gcd of the original integer coefficient pair.

The theorem does **not** prove that these positive whole errors tend to zero. It closes the previous analytic nonvanishing gate on $\mathcal K$; the decisive remaining gate is primitive arithmetic normalization.

The cutoff $64$ is convenient rather than optimized. No finite computation is used to establish it.

---

## 2. Exact measures, complete moments, and finite boundaries

### 2.1 The actual density of $\mu$

The full charge measure is


$$
d\eta(t)=e^{t-1}\,dt,\qquad t\le1,
$$


and $\mu$ is its pushforward under $x=t^2$. Therefore


$$
\boxed{
d\mu(x)
=
\frac{e^{-1}}{2\sqrt{x}}
\left(e^{-\sqrt{x}}+
\mathbf 1_{(0,1)}(x)e^{\sqrt{x}}\right)\,dx,
\qquad x>0.
}
\tag{2.1}
$$



Thus, with $s=\sqrt{x}$,

- on the exterior region $x>1$,
  

$$
d\mu(x)=e^{-1}e^{-s}\,ds,\qquad s>1;
  \tag{2.2}
$$


- the exact mass of the overlap region is
  

$$
\boxed{\mu([0,1])=1-e^{-2}.}
  \tag{2.3}
$$



In particular, the positive branch of the charge inside $[0,1]$ is not omitted.

The signed functional remains


$$
L(f)=\int f\,d\mu-f(-1).
\tag{2.4}
$$


The negative atom has mass exactly $-1$.

### 2.2 The full compact weight

The compact measure is exactly


$$
\boxed{
d\nu(x)
=
\frac{e^{\sqrt{x}}+4/(1+x)}{2\sqrt{x}}\,
\mathbf 1_{(0,1)}(x)\,dx.
}
\tag{2.5}
$$


Equivalently,


$$
\int f(x)\,d\nu(x)
=
\int_0^1 f(t^2)\left(e^t+\frac4{1+t^2}\right)\,dt.
$$



Its density is positive throughout $(0,1)$. Hence all its finite polynomial Gram matrices are positive definite, and its monic orthogonal polynomials $P_n$ exist uniquely.

Write


$$
J_k^\nu
=
\det(\nu_{i+j})_{0\le i,j<k},
\qquad
\nu_n=\int x^n\,d\nu(x).
$$


Then $J_k^\nu>0$.

The complete weight satisfies


$$
3\le e^t+\frac4{1+t^2}<7
\qquad(0\le t\le1).
$$


Consequently,


$$
\boxed{
3^kh_k\le J_k^\nu\le7^kh_k,
}
\tag{2.6}
$$


where


$$
h_k=
\det\left(\frac1{2i+2j+1}\right)_{i,j<k}
=
\frac{2^{k(k-1)}
\left(\prod_{j=1}^{k-1}j!\right)^2}
{\prod_{i,j=0}^{k-1}(2i+2j+1)}.
\tag{2.7}
$$



These are inequalities for the full weight, not a replacement of it.

### 2.3 Complete rational corrections

Retain


$$
a_0=1,\qquad a_d=1-da_{d-1},
\qquad
c_n=a_{2n}-(-1)^n,
$$


and


$$
\rho_0=0,\qquad
\rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad
r_n=-(2n)!+4\rho_n.
\tag{2.8}
$$



The full moment identity is


$$
\nu_n=e\,a_{2n}+\pi(-1)^n+r_n
=e\,c_n+(e+\pi)(-1)^n+r_n.
\tag{2.9}
$$


Indeed, finite integration by parts gives


$$
\int_0^1e^tt^{2n}\,dt=e\,a_{2n}-(2n)!,
$$


while the arctangent recurrence gives


$$
4\int_0^1\frac{t^{2n}}{1+t^2}\,dt
=\pi(-1)^n+4\rho_n.
$$


Both endpoint contributions remain present.

Set


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),
$$




$$
\Phi=(c_{j+m})_{\substack{0\le j<k\\0\le m<2k}},
\qquad
\mathcal R_{mj}=r_{m+j},
\qquad
w_m=(-1)^m,\quad v_j=(-1)^j.
$$


The integer affine polynomial remains


$$
\boxed{
H_k(s)=
\det\left[\Phi^T\mid
\Lambda_k\mathcal R+s\Lambda_kwv^T
\right]
=H_{0,k}+H_{1,k}s.
}
\tag{2.10}
$$



The largest moment index is exactly


$$
m+j=3k-2,
$$


and the largest factorial degree is exactly


$$
2(3k-2)=6k-4.
$$


The physical bottom-right rational moment is $r_{3k-2}$, whose largest odd denominator is $6k-5$. No successor row or column is introduced.

---

## 3. Reused compression and the whole-integral normalization

Put $s_0=e+\pi$. From (2.9), adding $e\Lambda_k$ times each contact column to its corresponding right column gives


$$
H_k(s_0)
=
\Lambda_k^k\det[\Phi^T\mid N],
\qquad
N_{mj}=\nu_{m+j}.
\tag{3.1}
$$



The orthogonal compression from Turn 12 is valid under the present hypotheses:


$$
\boxed{
H_k(s_0)
=
(-1)^{k^2}\Lambda_k^kJ_k^\nu\det T^{(k)}.
}
\tag{3.2}
$$



For clarity, its mechanism is short. Replace the monomial row polynomials by


$$
P_0,P_1,\ldots,P_{2k-1}.
$$


This is a unitriangular row transformation. The lower compact block vanishes by orthogonality, and the upper compact block is triangular with diagonal entries equal to the positive squared norms of $P_0,\ldots,P_{k-1}$. Exchanging the two $k$-column groups gives the sign $(-1)^{k^2}$.

This is an identity for the evaluation of the already-defined integer polynomial. It creates no new arithmetic normalization.

### 3.1 A consecutive-polynomial alternant with its actual normalization

For $x=(x_1,\ldots,x_k)$, let


$$
V(x)=\prod_{i<j}(x_j-x_i),
$$


and define the symmetric polynomial


$$
A_k(x)
=
\frac{\det(P_{k+r}(x_i))_{\substack{0\le r<k\\1\le i\le k}}}{V(x)}.
$$


The quotient extends polynomially to coincident points.

The exact identity needed below is


$$
\boxed{
A_k(x)
=
\frac1{k!J_k^\nu}
\int_{[0,1]^k}
V(y)^2
\prod_{i=1}^k\prod_{j=1}^k(x_i-y_j)\,
d\nu^k(y).
}
\tag{3.3}
$$



One derivation is to integrate the full Vandermonde $V(y,x)$ against $V(y)d\nu^k(y)$. Replacing its monomial rows by $P_0,\ldots,P_{2k-1}$ preserves its determinant. In the expansion along the $y$-columns, orthogonality kills every choice except the first $k$ polynomial rows. Their integral is $k!J_k^\nu$, leaving the displayed consecutive-polynomial determinant.

The measure


$$
\frac{V(y)^2\,d\nu^k(y)}{k!J_k^\nu}
\tag{3.4}
$$


is therefore a probability measure. Its support is genuinely $[0,1]^k$, as required in every estimate below.

### 3.2 The signed determinant, including the atom

Finite determinant integration gives


$$
\det T^{(k)}
=
\frac1{k!}\int V(x)^2A_k(x)\,dL^k(x).
\tag{3.5}
$$



Expanding $L=\mu-\delta_{-1}$, all terms containing two or more atoms vanish because of the squared Vandermonde. Thus


$$
\boxed{
\det T^{(k)}=D_{\mu,k}-D_{a,k},
}
\tag{3.6}
$$


where


$$
D_{\mu,k}
=
\frac1{k!}\int V(x)^2A_k(x)\,d\mu^k(x),
\tag{3.7}
$$


and


$$
D_{a,k}
=
\frac1{(k-1)!}
\int
V(x)^2\prod_{i=1}^{k-1}(x_i+1)^2
A_k(-1,x_1,\ldots,x_{k-1})\,
d\mu^{k-1}(x).
\tag{3.8}
$$



This is the orthogonally normalized version of A4 Turn 16’s $\mathcal I_k-\mathcal J_k$ formula. No sign assumption is being made about either complete term.

All these integrals converge absolutely: their integrands are finite polynomials, $\mu$ has every polynomial moment, and $\nu$ is compactly supported.

---

## 4. A whole-minor estimate that controls determinant conditioning

The key improvement is not an entrywise moment estimate. It is a bound for the complementary minors that arise when particles enter the overlap region.

For integers $n,\alpha\ge0$, define


$$
Z_{n,\alpha}
=
\frac1{n!}
\int_{[0,\infty)^n}
V(s_1^2,\ldots,s_n^2)^2
\prod_{i=1}^n s_i^{2\alpha}e^{-s_i}\,ds_i.
$$


Set $Z_{0,\alpha}=1$. Determinant integration gives


$$
Z_{n,\alpha}
=
\det\bigl((2\alpha+2i+2j)!\bigr)_{0\le i,j<n}.
\tag{4.1}
$$


In particular, $Z_k=Z_{k,k}>0$.

Define the explicit number


$$
\boxed{
K_k=
\frac{\binom{4k-1}{\,2k-2\,}}{(2k)!}.
}
\tag{4.2}
$$



### Lemma 4.1 — Evaluated complementary-minor bound

For $0\le m\le k$,


$$
\boxed{
\frac{Z_{k-m,k+2m}}{Z_k}
\le
\frac{K_k^m}{\displaystyle\prod_{i=0}^{m-1}((2i)!)^2}
\le K_k^m.
}
\tag{4.3}
$$



#### Proof

Let


$$
M=\bigl((2k+2i+2j)!\bigr)_{0\le i,j<k}.
$$


The numerator in (4.3) is the trailing principal minor obtained by deleting the first $m$ rows and columns of $M$. Jacobi’s complementary-minor identity therefore gives


$$
\frac{Z_{k-m,k+2m}}{Z_k}
=
\det\bigl((M^{-1})_{ij}\bigr)_{0\le i,j<m}.
\tag{4.4}
$$



Now consider the inner product


$$
\langle f,g\rangle_k
=
\int_0^\infty f(s)g(s)s^{2k}e^{-s}\,ds.
$$


The matrix $M$ is its Gram matrix on


$$
1,s^2,\ldots,s^{2k-2}.
$$



The squared norm of the coefficient functional $[s^{2i}]$ on this even-polynomial space is $(M^{-1})_{ii}$. Enlarging the space to all polynomials of degree at most $2k-2$ can only increase that functional norm.

Use the monic generalized Laguerre polynomials


$$
Q_r(s)=(-1)^rr!L_r^{(2k)}(s),\qquad 0\le r\le2k-2.
$$


Their coefficient formula and squared norms are


$$
Q_r(s)
=
(-1)^rr!\sum_{d=0}^r
(-1)^d\binom{r+2k}{r-d}\frac{s^d}{d!},
\tag{4.5}
$$




$$
\langle Q_r,Q_r\rangle_k=r!(r+2k)!.
\tag{4.6}
$$



These formulas do not require an uninspected structural theorem. From Rodrigues’ formula,


$$
Q_r(s)
=
(-1)^rs^{-2k}e^s
\frac{d^r}{ds^r}\bigl(e^{-s}s^{r+2k}\bigr).
$$


Integrating by parts $r$ times proves orthogonality against degrees below $r$, and gives


$$
\langle Q_r,s^r\rangle_k=r!(r+2k)!.
$$


Since $Q_r-s^r$ has lower degree, this also proves (4.6).

The ratio of the absolute coefficient of $s^d$ to the absolute constant coefficient is


$$
\frac{r(r-1)\cdots(r-d+1)}
{d!(2k+1)(2k+2)\cdots(2k+d)}
\le\frac1{d!},
\tag{4.7}
$$


because $r\le2k-2$.

Consequently,


$$
(M^{-1})_{ii}
\le
\frac1{((2i)!)^2}
\sum_{r=0}^{2k-2}
\frac{Q_r(0)^2}{r!(r+2k)!}.
$$


The sum is explicitly


$$
\begin{aligned}
\sum_{r=0}^{2k-2}
\frac{Q_r(0)^2}{r!(r+2k)!}
&=
\frac1{(2k)!}
\sum_{r=0}^{2k-2}\binom{2k+r}{2k}\\
&=
\frac{\binom{4k-1}{2k-2}}{(2k)!}
=K_k.
\end{aligned}
\tag{4.8}
$$


Hadamard’s inequality applied to the positive-definite matrix in (4.4) proves (4.3). ∎

This is the step that pays for determinant conditioning. Small relative errors in individual factorial moments would not establish (4.3).

### 4.2 Explicit factorial bounds for $Z_k$

The determinant is not left without quantitative evaluation. One has


$$
\boxed{
\prod_{i=0}^{k-1}(2i)!(2k+2i)!
\le Z_k
\le
\prod_{i=0}^{k-1}(2k+4i)!.
}
\tag{4.9}
$$



The upper bound is Hadamard’s inequality.

For the lower bound, perform Gram–Schmidt on the even monomials in the preceding inner product. The monic even polynomial of degree $2i$ has squared norm at least that of the unrestricted monic orthogonal polynomial of degree $2i$, namely


$$
(2i)!(2k+2i)!.
$$


Multiplying the successive Gram–Schmidt norms proves the lower bound.

All factorial moments used in this section have degree at most


$$
2k+4(k-1)=6k-4.
$$


Thus this comparison does not enlarge the original maximal factorial boundary.

---

## 5. Exterior domination of the complete signed determinant

Set


$$
a_{\mathrm{in}}=1-e^{-2},
\qquad
z_k=e\,a_{\mathrm{in}}K_k=(e-e^{-1})K_k,
$$


and


$$
b_k=\frac{e\,8^k}{4}K_k.
\tag{5.1}
$$



### 5.1 The all-exterior contribution has a positive lower bound

Let $E_k$ be the part of $D_{\mu,k}$ where every $x_i>1$.

For $x_i>1$ and $0\le y_j\le1$, formula (3.3) gives


$$
\prod_i(x_i-1)^k
\le A_k(x)\le
\prod_i x_i^k.
\tag{5.2}
$$


In particular, $E_k>0$.

Using $x_i=s_i^2$ and the exact exterior density (2.2),


$$
E_k\le e^{-k}Z_k.
\tag{5.3}
$$



For a lower bound, put $s_i=t_i+1$. Then


$$
(s_i^2-1)^k=(t_i^2+2t_i)^k\ge t_i^{2k},
$$


and, pair by pair,


$$
\left|(t_j+1)^2-(t_i+1)^2\right|
=
|t_j-t_i|(t_j+t_i+2)
\ge |t_j^2-t_i^2|.
$$


The density contributes exactly $e^{-2k}e^{-\sum t_i}$. Hence


$$
\boxed{
e^{-2k}Z_k\le E_k\le e^{-k}Z_k.
}
\tag{5.4}
$$



The shift loses only an exponential factor in $k$, not a factor of order $\exp(-c k^2\log k)$.

### 5.2 The complete overlap contribution

Suppose exactly $m$ of the $k$ variables lie in $[0,1]$, and the other $k-m$ lie above $1$.

From (3.3),


$$
|A_k(x)|\le\prod_{\mathrm{outside}}x_i^k.
$$


The squared Vandermonde among the inside variables is at most $1$. Each inside–outside pair contributes at most $x_{\mathrm{outside}}^2$. After integrating the inside variables using their exact total mass $a_{\mathrm{in}}$, the absolute contribution is at most


$$
\frac{a_{\mathrm{in}}^m}{m!}\,
e^{-(k-m)}
Z_{k-m,k+2m}.
\tag{5.5}
$$


The combinatorial factor here includes the choice of the inside variables and the original factor $1/k!$.

Summing over $m\ge1$ and applying Lemma 4.1 gives


$$
\boxed{
|D_{\mu,k}-E_k|
\le
e^{-k}Z_k\bigl(e^{z_k}-1\bigr).
}
\tag{5.6}
$$



### 5.3 The entire atom contribution

Now consider (3.8), with exactly $m$ of its $k-1$ positive-measure variables inside $[0,1]$.

For the actual atom at $-1$,


$$
|-1-y_j|\le2,
$$


so


$$
|A_k(-1,x_1,\ldots,x_{k-1})|
\le
2^k\prod_{\mathrm{outside}}x_i^k.
\tag{5.7}
$$


Furthermore,


$$
(x_i+1)^2\le
\begin{cases}
4,&0\le x_i\le1,\\
4x_i^2,&x_i>1.
\end{cases}
\tag{5.8}
$$



The same inside–outside Vandermonde accounting therefore yields


$$
\begin{aligned}
|D_{a,k}|
&\le
2^k4^{k-1}
\sum_{m=0}^{k-1}
\frac{a_{\mathrm{in}}^m}{m!}
e^{-(k-1-m)}
Z_{k-1-m,k+2m+2}\\
&\le
\boxed{
e^{-k}Z_k\,b_ke^{z_k}.
}
\end{aligned}
\tag{5.9}
$$



This bounds the **whole** atom term, even where its sign would help. It is not discarded or replaced by a single endpoint estimate.

### 5.4 A completely explicit cancellation bound

Combining (5.4), (5.6), and (5.9),


$$
\det T^{(k)}
\ge
e^{-2k}Z_k(1-\varepsilon_k),
\tag{5.10}
$$


where


$$
\varepsilon_k
=
e^k\left[e^{z_k}(1+b_k)-1\right].
\tag{5.11}
$$


Also,


$$
|\det T^{(k)}|
\le e^{-k}Z_ke^{z_k}(1+b_k).
\tag{5.12}
$$



The quantities in these inequalities can be bounded without a finite numerical search. Since


$$
K_k\le\frac{16^k}{(2k)!}
\le\left(\frac{36}{k^2}\right)^k,
\tag{5.13}
$$


where $e<3$ and $n!\ge(n/e)^n$ were used, $k\ge64$ implies $K_k<1/6$. Thus


$$
z_k<\frac12,\qquad e^{z_k}<2,\qquad e^{z_k}-1\le6K_k.
$$


It follows that


$$
\begin{aligned}
\varepsilon_k
&\le
6\cdot3^kK_k+\frac32\,24^kK_k\\
&\le
2\cdot24^kK_k
\le
\boxed{\frac{2\cdot384^k}{(2k)!}}.
\end{aligned}
\tag{5.14}
$$


Finally, for $k\ge64$,


$$
\frac{2\cdot384^k}{(2k)!}
\le
2\left(\frac{864}{k^2}\right)^k
\le2\cdot4^{-k}<\frac12.
\tag{5.15}
$$



Equations (5.10)–(5.15) prove (1.1).

This is a whole-multiple-integral comparison: the all-exterior integral dominates the sum of the absolute overlap error and the absolute atom contribution.

---

## 6. The actual affine slope is also nonzero on the same infinite set

The period matrix having rank one does not, by itself, prove that $H_{1,k}\ne0$. Its cofactors could cancel. Here the actual coefficient admits a separate whole-integral comparison.

### 6.1 Exact coefficient extraction

For a real indeterminate $z$, the same column operation as in (3.1) gives


$$
H_k(s_0+z)
=
\Lambda_k^k
\det\bigl[\Phi^T\mid N+zwv^T\bigr].
\tag{6.1}
$$


The right block is the moment block of


$$
\nu+z\delta_{-1}.
$$



Extracting the coefficient of $z$ in the two-measure determinant gives


$$
\begin{aligned}
\frac{H_{1,k}}{\Lambda_k^k}
={}&
\frac1{k!(k-1)!}
\int
V(x)^2V(y)^2
\prod_{j=1}^{k-1}(y_j+1)^2\\
&\quad\cdot
\prod_{i=1}^{k}(-1-x_i)
\prod_{i=1}^{k}\prod_{j=1}^{k-1}(y_j-x_i)
\,d\mu^k(x)\,d\nu^{k-1}(y).
\end{aligned}
\tag{6.2}
$$



Why is $\mu$, rather than $L$, present here? Any term containing the contact atom at $-1$ and the extracted compact atom at $-1$ has a vanishing cross factor. Thus its cancellation is exact. It is not an omission of the negative atom.

Define the positive compact measure


$$
d\nu_+(y)=(1+y)^2\,d\nu(y),
$$


and


$$
J_{k-1}^+
=
\frac1{(k-1)!}\int V(y)^2\,d\nu_+^{k-1}(y)>0.
$$


Equation (6.2) becomes


$$
\boxed{
\frac{(-1)^kH_{1,k}}{\Lambda_k^k}
=
J_{k-1}^+S_k,
}
\tag{6.3}
$$


where


$$
S_k=
\frac1{k!}\int V(x)^2
\prod_{i=1}^k(x_i+1)\,
\mathbb E_+\!\left[
\prod_{i=1}^{k}\prod_{j=1}^{k-1}(x_i-y_j)
\right]d\mu^k(x).
\tag{6.4}
$$


Here $\mathbb E_+$ is expectation for the normalized, positive $(k-1)$-particle ensemble associated with $\nu_+$.

### 6.2 Exterior and overlap bounds

If every $x_i>1$, then


$$
(x_i+1)\prod_{j=1}^{k-1}(x_i-y_j)
\ge
(x_i+1)(x_i-1)^{k-1}
\ge(x_i-1)^k.
$$


The all-exterior contribution to $S_k$ is therefore at least $e^{-2k}Z_k$.

For arbitrary inside–outside configurations,


$$
(x_i+1)\left|\prod_{j=1}^{k-1}(x_i-y_j)\right|
\le
\begin{cases}
2,&x_i\in[0,1],\\
2x_i^k,&x_i>1.
\end{cases}
$$


Hence the absolute overlap contribution is at most


$$
2^ke^{-k}Z_k(e^{z_k}-1).
\tag{6.5}
$$


Its ratio to the exterior lower bound is at most


$$
2^ke^k(e^{z_k}-1)
\le
6\cdot6^kK_k
\le
\frac{6\cdot96^k}{(2k)!}
\le
\frac{2\cdot384^k}{(2k)!}.
$$


It is less than $1/2$ for $k\ge64$.

We have therefore proved


$$
\boxed{
\frac12e^{-2k}Z_k
\le S_k
\le2^{k+1}e^{-k}Z_k,
\qquad k\ge64.
}
\tag{6.6}
$$


Together with (6.3),


$$
\boxed{
\frac12e^{-2k}\Lambda_k^kJ_{k-1}^+Z_k
\le
(-1)^kH_{1,k}
\le
2^{k+1}e^{-k}\Lambda_k^kJ_{k-1}^+Z_k.
}
\tag{6.7}
$$



This proves actual slope nonvanishing on exactly the same infinite set as residual nonvanishing. It does not extrapolate A4’s finite $k=3$ residue.

---

## 7. Whole primitive errors, actual denominators, and the remaining arithmetic scale

By (3.2) and Theorem 1,


$$
\operatorname{sgn}H_k(s_0)=(-1)^k
=\operatorname{sgn}H_{1,k}
\qquad(k\ge64).
$$


Thus the primitive whole error


$$
\ell_k=q_ks_0-p_k
$$


satisfies


$$
\ell_k=\frac{|H_k(s_0)|}{G_k}>0.
$$



### 7.1 Bounds retaining the final ALL-prime gcd

The proved whole-error bounds are


$$
\boxed{
\frac{e^{-2k}\Lambda_k^kJ_k^\nu Z_k}{2G_k}
\le
\ell_k
\le
\frac{2e^{-k}\Lambda_k^kJ_k^\nu Z_k}{G_k}.
}
\tag{7.1}
$$


The actual denominator satisfies


$$
\boxed{
\frac{e^{-2k}\Lambda_k^kJ_{k-1}^+Z_k}{2G_k}
\le
q_k
\le
\frac{2^{k+1}e^{-k}\Lambda_k^kJ_{k-1}^+Z_k}{G_k}.
}
\tag{7.2}
$$



Using (2.6) and (4.9) gives fully explicit factorial budgets:


$$
\boxed{
\frac{(3/e^2)^k\Lambda_k^kh_k
\prod_{i=0}^{k-1}(2i)!(2k+2i)!}{2G_k}
\le\ell_k
}
\tag{7.3}
$$


and


$$
\boxed{
\ell_k
\le
\frac{2(7/e)^k\Lambda_k^kh_k
\prod_{i=0}^{k-1}(2k+4i)!}{G_k}.
}
\tag{7.4}
$$



The upper bound in (7.4), before division by $G_k$, improves Turn 12’s displayed factorial budget by the factor


$$
\frac{2}{(3e)^kk!}.
$$


The principal advance is nevertheless the new **lower bound and sign theorem**, not this supplementary upper-bound saving.

### 7.2 The raw factorial scale is now a proved two-sided scale

From (4.9),


$$
\log Z_k=4k^2\log k+O(k^2).
$$


The compact Gram factor contributes $O(k^2)$ to the logarithm, and the established lcm bound contributes $O(k^2)$. Hence


$$
\boxed{
\log|H_k(e+\pi)|
=
4k^2\log k+O(k^2).
}
\tag{7.5}
$$



Previously, this scale was only an upper budget for the whole error. It is now also a lower scale for the actual nonzero evaluation.

Accordingly,


$$
\boxed{
\log\ell_k
=
4k^2\log k-\log G_k+O(k^2).
}
\tag{7.6}
$$


This is not a divergence theorem: $\log G_k$ remains unknown.

The established divisor


$$
D_{k-1}=\prod_{r=0}^{k-2}(r!)^2
\mid\delta_{k,2k-1}\mid G_k
$$


has logarithm only $k^2\log k+O(k^2)$. It remains insufficient to settle (7.6).

### 7.3 A concrete consequence in terms of the actual primitive denominator

This subsection concerns the ordinary rational approximation error


$$
s_0-\frac{p_k}{q_k}=\frac{\ell_k}{q_k}.
$$


It must not be confused with the whole error $\ell_k$.

Since


$$
3^{k-1}h_{k-1}\le J_{k-1}^+\le28^{k-1}h_{k-1},
$$


and


$$
\frac{h_k}{h_{k-1}}
=
\frac{16^{k-1}}
{(4k-3)\binom{4k-4}{2k-2}^{\,2}},
\tag{7.7}
$$


the elementary central-binomial bounds imply


$$
\frac1{(4k-3)16^{k-1}}
\le
\frac{h_k}{h_{k-1}}
\le
\frac{4k-3}{16^{k-1}}.
$$


Combining these with (7.1)–(7.2) yields


$$
\boxed{
\frac{112}{(4k-3)896^k}
\le
\frac{\ell_k}{q_k}
\le
84(4k-3)\left(\frac7{16}\right)^{k-1},
\qquad k\ge64.
}
\tag{7.8}
$$



Thus the actual primitive rationals approach $e+\pi$ from below. This still does not imply irrationality, because multiplication by their actual denominators may destroy decay.

Two precise arithmetic implications follow.

* A sufficient condition for irrationality is that, on an infinite subset of $\mathcal K$,
  

$$
\boxed{
  q_k(4k-3)\left(\frac7{16}\right)^{k-1}\longrightarrow0.
  }
  \tag{7.9}
$$


* A necessary condition for this family’s whole errors to tend to zero is
  

$$
\boxed{
  q_k=o(k\,896^k).
  }
  \tag{7.10}
$$



Both statements concern


$$
q_k=\frac{|H_{1,k}|}{G_k},
$$


not a raw slope, a polynomial clearer, or a denominator from another family.

### 7.4 Conditional irrationality implication

For example, if on an infinite $K\subseteq\mathcal K$ one proves


$$
\frac{
2(7/e)^k\Lambda_k^kh_k
\prod_{i=0}^{k-1}(2k+4i)!
}{G_k}
\longrightarrow0,
\tag{7.11}
$$


then $e+\pi$ is irrational.

Indeed, nonvanishing has now been proved at those same indices. If $e+\pi=A/B$ were rational, then


$$
0<\ell_k=\frac{Aq_k-Bp_k}{B}
$$


would imply $\ell_k\ge1/B$, contradicting (7.11).

Condition (7.11), or the potentially more useful actual-denominator condition (7.9), remains unproved.

---

## 8. Arithmetic payments and primitive basis invariance

The real integral comparisons do not evaluate or alter the arithmetic ledger.

### 8.1 The full moment block has least entry clearer exactly $\Lambda_k$

There is a small exact clarification available here. The complete right moment block contains every $r_n$ for $0\le n\le3k-2$, and


$$
r_n+r_{n-1}
=
-(2n)!-(2n-2)!+\frac4{2n-1}.
\tag{8.1}
$$


If an integer $L$ clears all these moments, then


$$
\frac{4L}{2n-1}\in\mathbb Z.
$$


Because $2n-1$ is odd, $2n-1\mid L$. Therefore


$$
\boxed{
\text{the least entry clearer of the full unprojected right block is }\Lambda_k.
}
\tag{8.2}
$$



This does not say that $\Lambda_k$ is the least clearer after contact projection.

Nor does it say that $\Lambda_k^k$ is the least simultaneous clearer of the two determinant coefficients.

For the rational polynomial $H_k(s)/\Lambda_k^k$, put


$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


Its exact least simultaneous coefficient clearer is


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
}
\tag{8.3}
$$


and the content remaining after that clearing is


$$
\boxed{\frac{G_k}{d_{H,k}}.}
\tag{8.4}
$$


After both payments, the primitive coefficient pair is exactly $H_k/G_k$, up to common sign.

### 8.2 Contact-row clearers and frame indices remain distinct

Let


$$
C_k=(c_{i+j})_{i,j<k},\qquad D=\det C_k,
$$


and let


$$
p_m(x)=x^m-(1,x,\ldots,x^{k-1})C_k^{-1}w_m,
\qquad k\le m<2k.
$$


The established theorem gives $D<0$ for $k\ge2$.

The exact primitive polynomial clearer remains


$$
d_m=
\frac{|D|}
{\gcd\bigl(|D|,\operatorname{adj}(C_k)w_m\bigr)}.
\tag{8.5}
$$


If $\delta_k$ is the gcd of all maximal contact minors, the high-coefficient lattice index and independent-frame index are respectively


$$
I_k^{\rm lat}=\frac{|D|}{\delta_k},
\qquad
J_k^{\rm frame}
=
\frac{\prod_{m=k}^{2k-1}d_m}{I_k^{\rm lat}}.
\tag{8.6}
$$


The latter is an exact compulsory scalar-gcd factor when that nonsaturated frame is used. It is not an evaluation of the residual gcd.

For completeness, let $R$ denote the rational functional $R(x^n)=r_n$, and set


$$
f_r=d_{k+r}p_{k+r},\qquad
u_r=f_r(-1),\qquad
E_{rj}=\Lambda_kR(f_rx^j).
$$


The actual least clearer of the scalar entry coefficients in the original monic row is


$$
h_r=
\frac{\Lambda_kd_{k+r}}
{\gcd(\Lambda_kd_{k+r},\Lambda_ku_r,E_{r0},\ldots,E_{r,k-1})},
\tag{8.7}
$$


and their least simultaneous entry clearer is $\operatorname{lcm}_rh_r$.

If one instead follows the paid primitive-row route, its least rational-entry clearer and actual row content are


$$
\ell_r^{\rm row}
=
\frac{\Lambda_k}{\gcd(\Lambda_k,E_{r0},\ldots,E_{r,k-1})},
$$




$$
\kappa_r=
\gcd\left(
\ell_r^{\rm row}u_r,\,
\frac{\ell_r^{\rm row}E_{r0}}{\Lambda_k},\ldots,
\frac{\ell_r^{\rm row}E_{r,k-1}}{\Lambda_k}
\right).
\tag{8.8}
$$


After these divisions, let $\gamma_j$ be the actual column contents. The multiplier relative to the monic contact determinant is


$$
T_k^{\rm paid}
=
\frac{\prod_r d_{k+r}\ell_r^{\rm row}}
{\prod_r\kappa_r\prod_j\gamma_j}.
\tag{8.9}
$$


The final gcd must still be taken after this route.

All these exact payments produce the same primitive rational zero and the same positively oriented whole error as (1.4). This is the established rational-basis invariance of the primitive coefficient pair.

No value of $d_m,h_r,\kappa_r,\gamma_j,\delta_k$, or $G_k$ is inferred from the real orthogonal compression.

---

## 9. What obstruction was removed, and what was not

### 9.1 Entrywise smallness was not a valid determinant argument

Even a matrix whose entries are perturbed by arbitrarily small relative amounts can become singular. For example,


$$
\begin{pmatrix}1&1\\1&1+\varepsilon\end{pmatrix}
$$


has determinant $\varepsilon$, while changing its bottom-right entry by $-\varepsilon$ makes the determinant zero.

For the actual factorial moment problem, the relevant missing quantities were complementary minors, equivalently entries and minors of an inverse Gram matrix. Lemma 4.1 bounds precisely those quantities. This is why the overlap estimate now controls the determinant rather than merely its entries.

### 9.2 Ordinary Gram positivity was insufficient

The cross factors in A4’s $\mathcal I_k-\mathcal J_k$ representation change sign on the overlap region, and the atom must be subtracted. Contact nonsingularity and the inertia of $C_k$ therefore did not prove residual nonsingularity.

The new argument does not assert that those signed integrands are positive. It proves that their possibly adverse parts are too small to cancel the explicitly positive exterior contribution.

### 9.3 The finite pole result is not promoted

The supplied


$$
13\mathcal D_3(X)\equiv X+7\pmod{13}
$$


remains a finite coefficient theorem. The unique-corner-pole lemma retains its exact hypotheses $p=6k-5$ prime and $p\nmid\det C_k$.

Neither statement proves an infinite nonzero residue theorem. The present all-$k\ge64$ slope theorem is independent of that unproved modular extrapolation.

### 9.4 No primitive decay follows from the new sign theorem

The raw whole evaluation has now been proved to have factorial scale. Whether the final gcd cancels enough of that scale remains unknown.

Thus the new result does not turn the known lower divisor $D_{k-1}$ into the actual gcd, and does not turn the finite $k=3$ large positive error into an infinite divergence theorem.

---

## 10. Separation from the original binary producer

The new proof concerns the compact family on $k\ge64$. It does not identify that family with the original binary construction.

The latter retains exactly


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


with contact indices $0,\ldots,b-1$, physical reconstruction indices $0,\ldots,b$, and terminal condition


$$
z_b=0.
$$



Its complete corrected columns remain


$$
x=\frac12RA^{-1}f,
\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad
x=2^ax_0.
$$


Neither $h^F$, $e_0$, $4b!$, nor the physical terminal is removed.

The return scalar remains


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f.
$$


After the paid division, the recorded return estimate gives only


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$


The subtraction of $a$ is retained.

The original norm $Q=x_0^Tx_0$, corrected-column contents, least simultaneous clearer, and final all-prime scalar gcd are not evaluated here. The original denominator valuation


$$
v_3(q^{\rm bin})=n-\frac{b+15}{2}
$$


is not transferred to the compact denominator $q_k$.

The compact theorem can of course be reindexed by $k=9^{18+32u}$, since those indices exceed $64$. That is only an indexing observation, not a transfer of binary arithmetic.

---

## 11. Finite checks and a bounded next arithmetic request

### 11.1 A small auxiliary exact check of the new minor normalization

This is a hand-checkable auxiliary calculation, not evidence extrapolated to infinite size.

At $k=2$,


$$
M=
\begin{pmatrix}
4!&6!\\
6!&8!
\end{pmatrix}
=
\begin{pmatrix}
24&720\\
720&40320
\end{pmatrix},
$$


so


$$
\det M=449280.
$$


The first complementary-minor ratio is


$$
\frac{Z_{1,4}}{Z_{2,2}}
=
\frac{40320}{449280}
=
\frac7{78}
=
(M^{-1})_{00}.
$$


The explicit full-space coefficient norm is


$$
K_2=\frac{\binom72}{4!}=\frac78.
$$


Thus the exact minor identity and the direction of the bound


$$
\frac7{78}\le\frac78
$$


agree.

This calculation checks only the normalization of Lemma 4.1. The infinite theorem follows from its proof and the inequalities in §5.

### 11.2 No finite computation is needed for the analytic theorem

The cutoff proof, residual sign, slope sign, and all displayed analytic bounds require no computer calculation.

The supplied $k=2,\ldots,10$ Smith data and the already checked $k=3$ primitive pair are not recomputed.

### 11.3 Optional bounded arithmetic audit at the first proved index

A useful next calculation should target the **actual final gcd**, rather than another abstract contact-lattice search.

Take precisely $k=64$.

#### Complete bounded inputs

1. Generate
   

$$
a_0,\ldots,a_{380},
   \qquad a_0=1,\quad a_d=1-da_{d-1}.
$$


2. Generate
   

$$
\rho_0,\ldots,\rho_{190},
   \qquad \rho_0=0,\quad
   \rho_{n+1}+\rho_n=\frac1{2n+1}.
$$


3. Set
   

$$
c_n=a_{2n}-(-1)^n,\qquad
   r_n=-(2n)!+4\rho_n
   \quad(0\le n\le190).
$$


4. Set
   

$$
\Lambda=\operatorname{lcm}(1,3,\ldots,379).
$$


5. Form the two $128\times128$ integer matrices defining $H_{64}(0)$ and $H_{64}(1)$, with
   

$$
0\le m<128,\qquad0\le j<64.
$$



#### Expected verifiable outputs

- Exact integers
  

$$
H_{0,64}=H_{64}(0),\qquad
  H_{1,64}=H_{64}(1)-H_{64}(0),
$$


  with inspectable determinant certificates.
- The actual gcd
  

$$
G_{64}=\gcd(|H_{0,64}|,|H_{1,64}|),
$$


  certified by divisibility and a Bézout identity. This certifies the ALL-prime gcd without requiring prime factorization.
- The actual least determinant-coefficient clearer and remaining content from (8.3)–(8.4).
- The primitive pair
  

$$
q_{64}=H_{1,64}/G_{64}>0,\qquad
  p_{64}=-H_{0,64}/G_{64}.
$$


- Exact rational comparisons of
  

$$
\frac{112q_{64}}{253\cdot896^{64}}
  \quad\text{and}\quad
  84\cdot253\left(\frac7{16}\right)^{63}q_{64}
$$


  with $1$.

By (7.8), these last two numbers are respectively a lower and an upper bound for the **whole** primitive error at $k=64$. For example, a lower bound exceeding $1$ would rigorously certify a large whole error at that one index.

Such an output would have only its stated finite scope. It would not establish a formula or asymptotic law for $G_k$ or $q_k$.

---

## 12. Conclusion

The new proved advance is a determinant-level exterior/overlap comparison for the actual measures and the actual negative atom. It gives, for every $k\ge64$,


$$
\det T^{(k)}>0,
\qquad
(-1)^kH_{1,k}>0,
$$


and hence a nonzero, positively oriented whole primitive error at those same indices.

The proof pays explicitly for:

- the exact exterior density $e^{-1}e^{-s}\,ds$;
- the full overlap mass $1-e^{-2}$;
- the complete compact weight $e^t+4/(1+t^2)$;
- the entire negative-atom contribution;
- determinant conditioning through evaluated complementary-minor bounds;
- the original finite moment boundaries;
- and the final primitive normalization through the actual ALL-prime $G_k$.

The previous analytic nonvanishing bottleneck is therefore closed on the explicit infinite compact domain $k\ge64$.

The exact remaining bottleneck is arithmetic:


$$
\boxed{
\text{control the actual }G_k
\text{, equivalently the actual }q_k,
\text{ strongly enough that }\ell_k\to0.
}
$$


A concrete sufficient target is (7.9), or the whole-error gcd condition (7.11). No such estimate is proved here.

Accordingly, this report establishes a new infinite signed nonvanishing theorem and quantitative primitive-error constraints, but **does not establish either rationality or irrationality of $e+\pi$**.
