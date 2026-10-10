> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the uniform Gamma–Christoffel comparison

## Executive assessment

The coordinator’s new analytic argument is correct for the **same complete compact determinants and the same actual primitive pairs**. In particular, Sections 2–8 establish, unconditionally,


$$
\boxed{
\frac12R_k\le \varepsilon_k\le \frac98R_k,\qquad
0<\varepsilon_{k+1}\le \frac14\varepsilon_k
\quad(k\ge64),
}
$$


where


$$
\varepsilon_k=e+\pi-\frac{p_k}{q_k},
\qquad
R_k=\frac{J_k^\nu}{J_{k-1}^{(1+x)^2\nu}}.
$$



The two integration orders in Section 8 have the stated normalizations. The relative Loewner comparison has the correct direction. The complete overlap and negative-atom contributions are paid before passing to the full error. No physical moment beyond the original finite boundary is required.

There are three important qualifications.

1. **The Christoffel minimum for a general positive measure needs a nondegeneracy hypothesis.** Its degree-$(k-1)$ moment matrix must be positive definite. This hypothesis is satisfied by every measure actually used here, including $P_x\nu$.

2. **Section 9 is a correct conditional selector theorem, not an arithmetic growth theorem.** It removes the need for balanced neighboring denominators when selecting an infinite successful subsequence. No bound on the actual $\Delta_k$ or $q_k$ is supplied.

3. **The adjacent selector does not automatically preserve the sparse original index set**
   

$$
\mathcal O=\{K_u=9^{18+32u}:u\ge0\}.
$$


   Even if $k\in\mathcal O$, its selected index may be $k+1\notin\mathcal O$. Below I give a scope-correct selector using consecutive members of $\mathcal O$.

The proof actually gives a further asymptotic statement:


$$
\boxed{\frac{\varepsilon_k}{R_k}\longrightarrow1.}
$$


This strengthens the constant-factor comparison, but it still supplies no missing all-prime content estimate.

Thus the exact ordinary-error rate and adjacent contraction are now proved. The rationality or irrationality of $e+\pi$ remains unresolved.

---

## 1. Exact objects, finite boundaries, and reused results

### 1.1 The original compact polynomial

Throughout,


$$
k\ge2,\qquad 0\le m<2k,\qquad 0\le j<k.
$$


Retain the complete recurrences


$$
a_0=1,\qquad a_d=1-da_{d-1},
$$




$$
c_n=a_{2n}-(-1)^n,
$$




$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
$$




$$
r_n=-(2n)!+4\rho_n.
$$



Write


$$
C_{mj}=c_{m+j},\qquad
\mathcal R_{mj}=r_{m+j},\qquad
w_m=(-1)^m,\qquad v_j=(-1)^j,
$$


and


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5).
$$


The integer affine polynomial under review is exactly


$$
H_k(s)=
\det[C\mid \Lambda_k\mathcal R+s\Lambda_kwv^T]
=H_{0,k}+H_{1,k}s.
\tag{1.1}
$$



Its boundaries are


$$
m+j\le3k-2,\qquad
\text{maximum factorial }(6k-4)!,\qquad
\text{last odd denominator }6k-5.
\tag{1.2}
$$



Set $s_0=e+\pi$, and retain the **actual all-prime gcd**


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|).
$$


For the accepted signs, and in particular for every $k\ge64$,


$$
q_k=\frac{|H_{1,k}|}{G_k},\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k}.
\tag{1.3}
$$


Then


$$
\varepsilon_k=s_0-\frac{p_k}{q_k}
=\frac{|H_k(s_0)|}{|H_{1,k}|},
$$


whereas the whole primitive error is


$$
\boxed{
\ell_k=q_k\varepsilon_k
=\frac{|H_k(s_0)|}{G_k}>0.
}
\tag{1.4}
$$



The cancellation of $G_k$ in $\varepsilon_k$ does not cancel it from $\ell_k$.

### 1.2 The exact measures

The charge measure and compact measure are


$$
d\mu(x)=
\frac{e^{-1}}{2\sqrt x}
\left(e^{-\sqrt x}+\mathbf1_{(0,1)}(x)e^{\sqrt x}\right)\,dx,
$$




$$
L=\mu-\delta_{-1},
$$


and


$$
d\nu(x)=
\frac{e^{\sqrt x}+4/(1+x)}{2\sqrt x}
\mathbf1_{(0,1)}(x)\,dx.
\tag{1.5}
$$



The complete endpoint identity is


$$
\nu_n=e\,c_n+s_0(-1)^n+r_n.
\tag{1.6}
$$


It retains both the factorial endpoint and the full arctangent correction.

For $x=t^2>1$,


$$
\boxed{d\mu_{\rm ext}(x)=e^{-1}e^{-t}\,dt,\qquad t>1.}
\tag{1.7}
$$


There is no normalization of $\mu_{\rm ext}$ to a probability measure.

For a finite positive measure $m$, put


$$
J_n(m)=\det\left(\int x^{a+b}\,dm(x)\right)_{0\le a,b<n},
\qquad J_0(m)=1.
$$


Also set


$$
d\nu_+(y)=(1+y)^2\,d\nu(y),\qquad
J_k^\nu=J_k(\nu),\qquad
J_{k-1}^+=J_{k-1}(\nu_+).
$$



### 1.3 Full conditioned quantities

The accepted determinant identities can be written explicitly as


$$
(-1)^kH_k(s_0)=\Lambda_k^kJ_k^\nu D_k,
\qquad
(-1)^kH_{1,k}=\Lambda_k^kJ_{k-1}^+S_k,
\tag{1.8}
$$


where


$$
\begin{aligned}
D_k={}&
\frac1{(k!)^2J_k^\nu}
\int V(x)^2V(y)^2
\prod_{i=1}^k\prod_{j=1}^k(x_i-y_j)\,
dL^k(x)\,d\nu^k(y),
\end{aligned}
\tag{1.9}
$$


and


$$
\begin{aligned}
S_k={}&
\frac1{k!(k-1)!J_{k-1}^+}
\int V(x)^2V(y)^2
\prod_{i=1}^k(x_i+1)
\prod_{i=1}^k\prod_{j=1}^{k-1}(x_i-y_j)\,
d\mu^k(x)\,d\nu_+^{k-1}(y).
\end{aligned}
\tag{1.10}
$$



These are analytic normalizations, not new integer normalizations.

The disappearance of the contact atom from (1.10) is exact: an $x_i=-1$ makes the factor $x_i+1$ vanish. The atom remains fully present in (1.9). Terms with two contact atoms vanish because of the squared Vandermonde.

Consequently,


$$
\boxed{
\varepsilon_k=R_k\frac{D_k}{S_k},
\qquad
R_k=\frac{J_k^\nu}{J_{k-1}^+}.
}
\tag{1.11}
$$



### 1.4 Closed conditioning estimates reused

Let


$$
Z_k=\det((2k+2a+2b)!)_{0\le a,b<k}.
$$


Let $E_D,E_S$ denote the normalized exterior contributions obtained from (1.9) and (1.10) by restricting all $x_i>1$.

Reuse the accepted complete conditioning and atom estimates from A4 Turn 20:


$$
|D_k-E_D|\le e^{-k}Z_k d_k,
\qquad
|S_k-E_S|\le e^{-k}Z_k d_k^+,
\tag{1.12}
$$


where


$$
\mathcal C_k=\frac{\binom{4k-1}{2k-2}}{(2k)!},
\quad
z_k=(e-e^{-1})\mathcal C_k,
\quad
b_k=\frac{e8^k}{4}\mathcal C_k,
$$




$$
d_k=e^{z_k}(1+b_k)-1,
\qquad
d_k^+=2^k(e^{z_k}-1).
$$


For every $k\ge64$,


$$
e^kd_k\le2\cdot4^{-k},
\qquad
e^kd_k^+\le2\cdot4^{-k}.
\tag{1.13}
$$



No conditioning, overlap, atom, column-clearer, or retired-matrix calculation is repeated below.

---

## 2. Independent derivation of the inverse-square Gamma bound

Define


$$
M_0=((2k+2a+2b)!)_{a,b<k},
\qquad
M_{-1}=((2k-2+2a+2b)!)_{a,b<k}.
$$



The proposed inequality is


$$
\boxed{
0<M_{-1}\le c_kM_0,\qquad
c_k=\frac9{(k-1)^2}.
}
\tag{2.1}
$$



### 2.1 The finite Jacobi matrix and its terminal row

Take


$$
\alpha=2k-2,\qquad N=2k-1.
$$


For the positive Gamma weight


$$
t^\alpha e^{-t}\,dt,\qquad t>0,
$$


the monic Laguerre recurrence gives the $N\times N$ Jacobi matrix with diagonal


$$
d_i=2i+\alpha+1=2i+2k-1,\qquad 0\le i<N,
$$


and off-diagonal entries


$$
\sqrt{j(j+\alpha)},\qquad 1\le j<N.
$$



These recurrence and quadrature facts require $\alpha>-1$, which is satisfied. They are used here only as an auxiliary Gamma-polynomial argument, not as a replacement for the compact mixed matrix.

Put


$$
b=k-1,\qquad a_i=i+k-1.
$$


For $0\le i\le N-2=2k-3$, the two possible off-diagonal magnitudes are


$$
\sqrt{a_i^2-b^2},
\qquad
\sqrt{a_{i+1}^2-b^2},
$$


and the diagonal is $a_i+a_{i+1}$. At $i=0$, the first displayed quantity is zero, exactly as required by the finite boundary.

For $a>0$, $0\le b\le a$,


$$
\sqrt{a^2-b^2}\le a-\frac{b^2}{2a}.
$$


Therefore the Gershgorin lower endpoint of such a row is at least


$$
\frac{b^2}{2}
\left(\frac1{a_i}+\frac1{a_{i+1}}\right).
$$


Here $a_i,a_{i+1}\le3k-3$, so this is at least


$$
\frac{(k-1)^2}{3k-3}=\frac{k-1}{3}.
\tag{2.2}
$$



The last row is different and must not be treated as an interior row. Its index is $i=2k-2$, its diagonal is $6k-5$, and it has only the lower off-diagonal. Bounding that entry by $a_i=3k-3$ gives lower endpoint


$$
6k-5-(3k-3)=3k-2.
$$


Thus every eigenvalue, hence every Gaussian node $t_j$, satisfies


$$
\boxed{t_j\ge\frac{k-1}{3}.}
\tag{2.3}
$$



The physical terminal row is correctly retained.

### 2.2 Why the degree-$2N$ Gaussian comparison is one-sided

Let $Q_N$ be the monic degree-$N$ orthogonal polynomial. Gaussian quadrature has positive weights $\omega_j$ and is exact through degree $2N-1$.

For completeness, exactness follows by dividing a polynomial of degree at most $2N-1$ by $Q_N$; orthogonality removes the quotient term, while the remainder is interpolated at the nodes. Positivity of the weights follows by applying this exactness to the squares of the degree-$(N-1)$ Lagrange cardinal polynomials.

Now let $\deg P\le N-1$. The quadrature is exact for $P^2$. For


$$
f(t)=t^2P(t)^2,
$$


let $a\ge0$ be its coefficient of $t^{2N}$, taking $a=0$ if its degree is smaller. Then


$$
f-aQ_N^2
$$


has degree at most $2N-1$. Since $Q_N(t_j)=0$,


$$
\int f(t)t^\alpha e^{-t}\,dt
-\sum_j\omega_jf(t_j)
=
a\int Q_N(t)^2t^\alpha e^{-t}\,dt
\ge0.
\tag{2.4}
$$



Thus exactness at degree $2N$ is not being asserted. The required conclusion is a lower quadrature bound, proved algebraically.

Using (2.3),


$$
\begin{aligned}
\int P(t)^2t^{2k-2}e^{-t}\,dt
&=\sum_j\omega_jP(t_j)^2\\
&\le\frac9{(k-1)^2}
\sum_j\omega_jt_j^2P(t_j)^2\\
&\le\frac9{(k-1)^2}
\int P(t)^2t^{2k}e^{-t}\,dt.
\end{aligned}
\tag{2.5}
$$



Apply this to $P(t)=p(t^2)$, $\deg p\le k-1$. This proves (2.1).

### 2.3 Factorial boundary

The largest weighted degree in the final integral is


$$
(2k-2)+2N=6k-4.
$$


The quadrature’s exact moments stop at weighted degree


$$
(2k-2)+(2N-1)=6k-5.
$$


The final positive norm in (2.4) uses degree $6k-4$.

Hence:

- auxiliary odd degrees occur;
- no factorial degree exceeds $6k-4$;
- no original successor moment $r_{3k-1}$ is introduced;
- no extra physical row or corrected charge is added.

**Decision: Section 2 is accepted.**

---

## 3. Exterior matrix comparisons and uniform constants

### 3.1 Bernoulli’s inequality in the required direction

For $t\ge1$,


$$
(t^2-1)^k
=t^{2k}(1-t^{-2})^k
\ge t^{2k}-kt^{2k-2}.
$$


For $0<t<1$, the expression on the right is nonpositive. Consequently, for every polynomial $p$ of degree at most $k-1$,


$$
\begin{aligned}
\int_{t>1}p(t^2)^2(t^2-1)^ke^{-t}\,dt
&\ge
p^T(M_0-kM_{-1})p\\
&\ge(1-\gamma_k)p^TM_0p,
\end{aligned}
\tag{3.1}
$$


where


$$
\gamma_k=kc_k=\frac{9k}{(k-1)^2}.
$$



This is the correct direction: extending the right-hand side to $0<t<1$ adds a nonpositive contribution.

### 3.2 Conditional exterior matrices

For $y=(y_1,\ldots,y_k)\in[0,1]^k$, let


$$
B_D(y)_{ab}
=
\int_{x>1}x^{a+b}\prod_{j=1}^k(x-y_j)\,d\mu_{\rm ext}(x).
$$


On $x>1$,


$$
(x-1)^k\le\prod_j(x-y_j)\le x^k.
$$


Using the exact density (1.7),


$$
e^{-1}(1-\gamma_k)M_0
\le B_D(y)\le e^{-1}M_0.
\tag{3.2}
$$



For a tuple $y\in[0,1]^{k-1}$, define


$$
B_+(y)_{ab}
=
\int_{x>1}x^{a+b}(x+1)
\prod_{j=1}^{k-1}(x-y_j)\,d\mu_{\rm ext}(x).
$$


The pointwise bounds


$$
(x+1)\prod_j(x-y_j)\ge(x-1)^k,
$$




$$
(x+1)\prod_j(x-y_j)\le x^k+x^{k-1}
$$


give


$$
e^{-1}(1-\gamma_k)M_0
\le B_+(y)
\le e^{-1}(M_0+M_{-1})
\le e^{-1}(1+c_k)M_0.
\tag{3.3}
$$



Only these positive exterior matrices are compared in Loewner order. No Loewner comparison is applied directly to the full signed determinant.

For positive definite matrices, $A\ge aB>0$ implies


$$
\det A\ge a^k\det B
$$


by conjugation with $B^{-1/2}$. Thus (3.2)–(3.3) imply the proposed determinant comparisons, including the factor $e^{-k}$.

### 3.3 Uniform estimates for every $k\ge64$

First,


$$
\gamma_k\le\frac16
\quad\Longleftrightarrow\quad
k^2-56k+1\ge0.
$$


At $k=64$, the last polynomial equals $513$, and it increases thereafter.

Second,


$$
\frac{k\gamma_k}{1-\gamma_k}
=\frac{9k^2}{k^2-11k+1}\le11
$$


is equivalent to


$$
2k^2-121k+11\ge0.
$$


At $64$, this equals $459$, and it increases thereafter.

Since


$$
\log(1-x)\ge-\frac{x}{1-x}\qquad(0\le x<1),
$$


we obtain


$$
(1-\gamma_k)^k\ge e^{-11}.
\tag{3.4}
$$


Also,


$$
(1+c_k)^k\le e^{kc_k}=e^{\gamma_k}
\le e^{1/6}<\frac32.
\tag{3.5}
$$



Averaging the conditional determinants against their normalized positive compact Vandermonde measures gives


$$
e^{-k-11}Z_k\le E_D\le e^{-k}Z_k,
\tag{3.6}
$$




$$
e^{-k-11}Z_k\le E_S\le\frac32e^{-k}Z_k.
\tag{3.7}
$$



Every exterior variable contributes $e^{-1}$, so the determinant factor is $e^{-k}$, not $e^{-1}$.

### 3.4 Full, separately estimated determinants

From (1.13), $d_k,d_k^+\le2\cdot4^{-k}$. For $k\ge64$,


$$
2\cdot4^{-k}\le\frac12e^{-11};
$$


for example,


$$
4\cdot3^{11}=708588<4^{10}\le4^{64}.
$$


Using (1.12), (3.6), and (3.7),


$$
\boxed{
\frac12e^{-k-11}Z_k\le D_k\le2e^{-k}Z_k,
}
$$




$$
\boxed{
\frac12e^{-k-11}Z_k\le S_k\le2e^{-k}Z_k.
}
\tag{3.8}
$$



This proves the coordinator’s Sections 3–4 and yields its preliminary comparison


$$
\frac{e^{-11}}4R_k\le\varepsilon_k\le4e^{11}R_k.
\tag{3.9}
$$



---

## 4. The two integration orders in the correlated comparison

This is the central new bridge.

### 4.1 Raw exterior quantities

Define


$$
\mathcal D_{\rm ext}=J_k^\nu E_D,
\qquad
\mathcal S_{\rm ext}=J_{k-1}^+E_S.
$$


Their complete positive integral formulas are


$$
\begin{aligned}
\mathcal D_{\rm ext}
={}&\frac1{(k!)^2}
\int_{x_i>1}\int
V(x)^2V(y)^2
\prod_{i=1}^k\prod_{j=1}^k(x_i-y_j)\,
d\nu^k(y)\,d\mu_{\rm ext}^k(x),
\end{aligned}
\tag{4.1}
$$


and


$$
\begin{aligned}
\mathcal S_{\rm ext}
={}&\frac1{k!(k-1)!}
\int_{x_i>1}\int
V(x)^2V(y)^2
\prod_{i=1}^k(x_i+1)
\prod_{i=1}^k\prod_{j=1}^{k-1}(x_i-y_j)\,
d\nu_+^{k-1}(y)\,d\mu_{\rm ext}^k(x).
\end{aligned}
\tag{4.2}
$$



All integrands here are nonnegative. Interchanging the integrations is justified directly; all polynomial moments involved are finite.

### 4.2 Compact variables first

For fixed $x_1,\ldots,x_k>1$, put


$$
P_x(y)=\prod_{i=1}^k(x_i-y).
$$


Andréief’s determinant identity gives


$$
\frac1{k!}\int V(y)^2\prod_{j=1}^kP_x(y_j)\,d\nu^k(y)
=J_k(P_x\nu),
$$


and


$$
\frac1{(k-1)!}\int V(y)^2
\prod_{j=1}^{k-1}P_x(y_j)\,d\nu_+^{k-1}(y)
=J_{k-1}(P_x\nu_+).
$$


Therefore


$$
\boxed{
\mathcal D_{\rm ext}
=\frac1{k!}\int V(x)^2J_k(P_x\nu)\,d\mu_{\rm ext}^k(x),
}
\tag{4.3}
$$




$$
\boxed{
\mathcal S_{\rm ext}
=\frac1{k!}\int V(x)^2\prod_i(x_i+1)
J_{k-1}(P_x\nu_+)\,d\mu_{\rm ext}^k(x).
}
\tag{4.4}
$$



These are precisely the coordinator’s formulas. Neither contains a missing $k!$ or $J$-factor.

### 4.3 Exterior variables first

Conversely, integrating $x$ first yields


$$
\mathcal D_{\rm ext}
=\frac1{k!}\int V(y)^2\det B_D(y)\,d\nu^k(y),
\tag{4.5}
$$


and


$$
\mathcal S_{\rm ext}
=\frac1{(k-1)!}\int V(y)^2\det B_+(y)\,d\nu_+^{k-1}(y).
\tag{4.6}
$$



Dividing (4.5) by $J_k^\nu$, or (4.6) by $J_{k-1}^+$, gives an average against a probability measure because


$$
\int V(y)^2\,dm^n(y)=n!J_n(m).
$$



Thus both integration orders lead to the same normalized $E_D,E_S$.

### 4.4 Compact and Gamma boundaries

In $J_k(P_x\nu)$, the largest moment degree is


$$
2(k-1)+k=3k-2.
$$


In $J_{k-1}(P_x\nu_+)$, it is


$$
2(k-2)+k+2=3k-2.
$$



In the exterior-first order, every Gram weight $Q_+$, $Q_-$, or $\prod_{j=1}^k(x-y_j)$ has degree $k$. The largest exterior $x$-degree is therefore


$$
2(k-1)+k=3k-2,
$$


which becomes Gamma factorial degree $6k-4$ under $x=t^2$.

Both integration orders stay exactly inside the original compact and factorial boundaries.

---

## 5. Christoffel monotonicity and the relative slope comparison

### 5.1 Exact hypotheses for the weighted Christoffel minimum

For a finite positive measure $m$ whose degree-$(k-1)$ moment matrix is positive definite,


$$
R_k(m):=
\frac{J_k(m)}{J_{k-1}((1+y)^2m)}
=
\min_{\substack{\deg p\le k-1\\p(-1)=1}}
\int p(y)^2\,dm(y).
\tag{5.1}
$$



One way to verify the identity is to add an atom $t\delta_{-1}$ to the moment matrix. The determinant lemma identifies the coefficient of $t$ as


$$
J_k(m)\,K_{k-1}^m(-1,-1),
$$


while extracting the atom in the determinant integral identifies it as


$$
J_{k-1}((1+y)^2m).
$$


The constrained minimum is the reciprocal evaluation-kernel norm.

A measure with too few support points need not satisfy this nonsingular formula. That is the needed qualification to “any positive compact measure.”

Here $\nu$, and every $P_x\nu$ with $x_i>1$, have positive density on $(0,1)$. Hence all required moment matrices are positive definite.

### 5.2 Pointwise weight comparison

On $0\le y\le1$,


$$
\prod_i(x_i-1)\le P_x(y)\le\prod_i x_i.
$$


Applying these inequalities to every admissible polynomial in (5.1), and then taking minima, gives


$$
\prod_i(x_i-1)R_k(\nu)
\le R_k(P_x\nu)
\le\prod_i x_iR_k(\nu).
\tag{5.2}
$$



This is a comparison of polynomial minima. It is not an unsupported monotonicity assertion for a quotient of determinants.

The ratio of the integrands in (4.3) and (4.4) is


$$
\frac{R_k(P_x\nu)}{\prod_i(x_i+1)}.
$$


Define $\mathcal S_-$ by replacing $\prod_i(x_i+1)$ in (4.4) by $\prod_i(x_i-1)$. Then (5.2) implies


$$
\boxed{
R_k(\nu)\mathcal S_-
\le\mathcal D_{\rm ext}
\le R_k(\nu)\mathcal S_{\rm ext}.
}
\tag{5.3}
$$



For the upper bound, the intermediate factor is


$$
\prod_i\frac{x_i}{x_i+1}\le1.
$$


For the lower bound, the factor $\prod_i(x_i-1)$ is retained exactly in $\mathcal S_-$.

### 5.3 Comparing the two slope integrals

For fixed $y\in[0,1]^{k-1}$, let $B_-(y)$ be the Gram matrix for


$$
Q_-(x)=(x-1)\prod_{j=1}^{k-1}(x-y_j).
$$


Then


$$
B_+(y)-B_-(y)=2C(y),
$$


where $C(y)$ is the Gram matrix for


$$
\prod_{j=1}^{k-1}(x-y_j)\,d\mu_{\rm ext}(x).
$$



All these are positive exterior forms. Pointwise,


$$
0\le\prod_j(x-y_j)\le x^{k-1}\qquad(x>1),
$$


so


$$
0\le C(y)\le e^{-1}M_{-1}.
\tag{5.4}
$$


From (3.3),


$$
B_+(y)\ge e^{-1}(1-\gamma_k)M_0.
$$


The crucial Loewner chain is therefore


$$
C(y)
\le e^{-1}M_{-1}
\le e^{-1}c_kM_0
\le\frac{c_k}{1-\gamma_k}B_+(y).
\tag{5.5}
$$


The last direction is correct: the lower bound for $B_+$ supplies an upper bound for $e^{-1}M_0$ in terms of $B_+$.

It follows that


$$
\boxed{
B_-(y)\ge(1-\delta_k)B_+(y),
\qquad
\delta_k=\frac{2c_k}{1-\gamma_k}
=\frac{18}{k^2-11k+1}.
}
\tag{5.6}
$$



For $k\ge64$,


$$
k\delta_k
=\frac{2\gamma_k}{1-\gamma_k}
\le\frac25.
$$


In particular $0<\delta_k<1$, and Bernoulli gives


$$
(1-\delta_k)^k\ge1-k\delta_k\ge\frac35.
\tag{5.7}
$$



Taking determinants and then integrating against the same positive compact measure,


$$
\mathcal S_-\ge(1-\delta_k)^k\mathcal S_{\rm ext}
\ge\frac35\mathcal S_{\rm ext}.
$$


Together with (5.3),


$$
\frac35R_k(\nu)\mathcal S_{\rm ext}
\le\mathcal D_{\rm ext}
\le R_k(\nu)\mathcal S_{\rm ext}.
$$



Now substitute


$$
\mathcal D_{\rm ext}=J_k^\nu E_D,\qquad
\mathcal S_{\rm ext}=J_{k-1}^+E_S,\qquad
R_k(\nu)=J_k^\nu/J_{k-1}^+.
$$


The compact determinant factors cancel exactly:


$$
\boxed{\frac35E_S\le E_D\le E_S.}
\tag{5.8}
$$



More precisely, the proof gives


$$
\boxed{(1-\delta_k)^kE_S\le E_D\le E_S.}
\tag{5.9}
$$



**Decision: the correlated comparison in Section 8 is accepted.**

---

## 6. Paying the full perturbations

The exterior slope lower bound (3.7) and the complete errors (1.12) give


$$
\frac{|D_k-E_D|}{E_S}\le e^{11}d_k,
\qquad
\frac{|S_k-E_S|}{E_S}\le e^{11}d_k^+.
$$


Thus the proposed common relative allowance


$$
\tau_k=2e^{11}4^{-k}
\tag{6.1}
$$


is valid.

For every $k\ge64$,


$$
\tau_k<\frac1{100}.
$$


Indeed,


$$
200e^{11}<200\cdot3^{11}
=35429400<4^{13}=67108864\le4^{64}.
\tag{6.2}
$$



Since $E_D/E_S\in[3/5,1]$,


$$
\frac{3/5-\tau_k}{1+\tau_k}
\le\frac{D_k}{S_k}
\le\frac{1+\tau_k}{1-\tau_k}.
\tag{6.3}
$$


Both the numerator and denominator in these comparisons are positive. At $\tau_k\le1/100$, the displayed endpoints are bounded by


$$
\frac{59}{101}>\frac12,
\qquad
\frac{101}{99}<\frac98.
$$


Therefore


$$
\boxed{
\frac12R_k\le\varepsilon_k\le\frac98R_k
\qquad(k\ge64).
}
\tag{6.4}
$$



The full $D_k$, including all overlap and the actual negative atom, is used here. The full extracted slope $S_k$ is also used. The exterior estimates have not silently replaced either full object.

### 6.1 A further consequence: asymptotic equivalence

Retaining (5.9), rather than replacing it by $3/5$, gives


$$
\frac{(1-\delta_k)^k-\tau_k}{1+\tau_k}
\le\frac{D_k}{S_k}
\le\frac{1+\tau_k}{1-\tau_k}.
\tag{6.5}
$$


Since


$$
(1-\delta_k)^k\ge1-k\delta_k,
$$


we have the explicit bounds


$$
1-\frac{k\delta_k+2\tau_k}{1+\tau_k}
\le\frac{D_k}{S_k}
\le1+\frac{2\tau_k}{1-\tau_k}.
\tag{6.6}
$$


Here


$$
k\delta_k=\frac{18k}{k^2-11k+1}=O(k^{-1}),
\qquad
\tau_k=O(4^{-k}).
$$


Hence


$$
\boxed{
\frac{D_k}{S_k}=1+O(k^{-1}),
\qquad
\frac{\varepsilon_k}{R_k}=1+O(k^{-1}).
}
\tag{6.7}
$$



This is an unconditional additional consequence of the audited proof.

---

## 7. Exact ordinary-error rate and adjacent contraction

### 7.1 The evaluated rate

Reuse the accepted compact Christoffel estimates


$$
\frac{3}{2k^2A^{k-1}}\le R_k\le\frac{28}{A^{k-1}},
\qquad
A=(3+2\sqrt2)^2=17+12\sqrt2.
\tag{7.1}
$$


Combining these with (6.4),


$$
\boxed{
\frac{3}{4k^2A^{k-1}}
\le\varepsilon_k
\le\frac{63}{2A^{k-1}},
\qquad k\ge64.
}
\tag{7.2}
$$



Taking logarithms,


$$
\frac{k-1}{k}\log A-\frac{\log(63/2)}k
\le-\frac{\log\varepsilon_k}{k}
$$


and


$$
-\frac{\log\varepsilon_k}{k}
\le
\frac{k-1}{k}\log A+
\frac{2\log k+\log(4/3)}k.
$$


Therefore


$$
\boxed{
\lim_{k\to\infty}-\frac{\log\varepsilon_k}{k}
=\log A.
}
\tag{7.3}
$$



Equivalently,


$$
\log\varepsilon_k=-(k-1)\log A+O(\log k).
$$



This is the exact logarithmic rate of the **ordinary** error. It is not a rate theorem for $\ell_k$.

### 7.2 The fixed-measure Christoffel contraction

The measure $\nu$ is independent of $k$. Let $p$ minimize $R_k$, with


$$
\deg p\le k-1,\qquad p(-1)=1.
$$


Then


$$
\widetilde p(x)=p(x)\frac{1-2x}{3}
$$


has degree at most $k$, satisfies $\widetilde p(-1)=1$, and on $[0,1]$,


$$
\left|\frac{1-2x}{3}\right|\le\frac13.
$$


Consequently,


$$
\boxed{R_{k+1}\le\frac19R_k.}
\tag{7.4}
$$



This comparison uses the same fixed compact measure, not a $k$-dependent conditional measure $P_x\nu$.

Using (6.4),


$$
\varepsilon_{k+1}
\le\frac98R_{k+1}
\le\frac18R_k
\le\frac14\varepsilon_k.
$$


Thus


$$
\boxed{
0<\varepsilon_{k+1}\le\frac14\varepsilon_k
\quad\text{for every }k\ge64.
}
\tag{7.5}
$$



At size $k+1$, the permitted original boundaries are


$$
3(k+1)-2=3k+1,\quad (6k+2)!,\quad 6k+1.
$$


The adjacent comparison uses that next compact object at its own boundary; it does not add a successor moment to the size-$k$ object.

### 7.3 The weaker stride-13 claim

The coordinator’s earlier stride estimate is also valid:


$$
\frac{\varepsilon_{k+13}}{\varepsilon_k}
\le\frac{16e^{22}}{9^{13}}
<\frac{16}{81}<\frac12,
$$


because $e<3$. It is now superseded by (7.5).

### 7.4 Actual rational separation and denominator consequences

The rational zeros


$$
z_k=\frac{p_k}{q_k}=s_0-\varepsilon_k
$$


are strictly increasing for every $k\ge64$. Therefore


$$
\Delta_k=p_{k+1}q_k-p_kq_{k+1}
$$


is a positive integer, and


$$
\frac34\varepsilon_k
\le z_{k+1}-z_k
=\frac{\Delta_k}{q_kq_{k+1}}
<\varepsilon_k.
\tag{7.6}
$$


Since $\Delta_k\ge1$,


$$
q_kq_{k+1}\ge\frac1{\varepsilon_k}
\ge\frac{2A^{k-1}}{63}.
\tag{7.7}
$$


It follows that


$$
\boxed{
\limsup_{k\to\infty}\frac{\log q_k}{k}
\ge\frac12\log A.
}
\tag{7.8}
$$



The already proved fact $q_k\to\infty$ also remains valid: positive errors tending to zero exclude infinitely many occurrences of a bounded denominator range. This does not require $s_0$ to be irrational.

Neither denominator divergence nor (7.8) proves divergence or decay of the whole primitive error.

### 7.5 What is now closed in A5 Turn 14

The open analytic contraction target in A5 Turn 14 was equivalent to


$$
\frac{z_{k+1}-z_k}{\varepsilon_k}\ge\frac12.
$$


It is now proved in the stronger form


$$
\boxed{
\frac34\le
\frac{z_{k+1}-z_k}{\varepsilon_k}
<1.
}
\tag{7.9}
$$



In the notation of the paid adjacent recurrence,


$$
D^2F^+=\mathcal K F-\mathcal T,
$$


this says


$$
\boxed{
\frac34\le
\frac{\mathcal T}{\mathcal K F(s_0)}
<1.
}
\tag{7.10}
$$


Thus the complete adjacent scalar does not vanish and has the required sign.

The arithmetic identity remains, with all its payments,


$$
D\,t^kG_kG_{k+1}\Delta_k
=(-1)^k\lambda\mathcal T,
\qquad
\lambda=\Lambda_{k+1},\quad t=\lambda/\Lambda_k.
\tag{7.11}
$$


The factors $D$, $t^k$, and both actual all-prime gcds remain indispensable. The new analysis determines the sign and relative analytic gap, not the growth of the reduced integer $\Delta_k$.

---

## 8. Section 9: the minimum-denominator selector

### 8.1 A general selector lemma

The following elementary form makes the hypotheses transparent.

**Lemma.** Suppose two actual primitive pairs satisfy


$$
0<\varepsilon_n\le\theta\varepsilon_m,\qquad 0\le\theta<1,\qquad m<n.
$$


Let


$$
\Delta_{m,n}=p_nq_m-p_mq_n>0,
$$


and choose $i\in\{m,n\}$ with the smaller actual denominator, breaking ties by choosing $m$. Then


$$
\boxed{
0<q_i\varepsilon_i
\le
\sqrt{\frac{\Delta_{m,n}\varepsilon_m}{1-\theta}}.
}
\tag{8.1}
$$



**Proof.** Since


$$
\Delta_{m,n}
=q_mq_n(\varepsilon_m-\varepsilon_n)
\ge(1-\theta)q_mq_n\varepsilon_m,
$$


we have


$$
q_mq_n\varepsilon_m
\le\frac{\Delta_{m,n}}{1-\theta}.
$$


Also,


$$
q_i\le\sqrt{q_mq_n},
\qquad
\varepsilon_i\le\varepsilon_m.
$$


Therefore


$$
q_i\varepsilon_i
\le\sqrt{q_mq_n}\,\varepsilon_m
\le
\sqrt{\frac{\Delta_{m,n}\varepsilon_m}{1-\theta}}.
$$


Strict positivity is the previously proved nonzero whole-error statement. ∎

### 8.2 Application to adjacent compact indices

Take $m=k$, $n=k+1$, and $\theta=1/4$. Then


$$
\boxed{
0<q_{i(k)}\varepsilon_{i(k)}
\le\sqrt{\frac43\Delta_k\varepsilon_k}.
}
\tag{8.2}
$$


Using (7.2),


$$
\boxed{
0<q_{i(k)}\varepsilon_{i(k)}
\le
\sqrt{\frac{42\Delta_k}{A^{k-1}}}.
}
\tag{8.3}
$$



This selector uses only the two actual integers $q_k,q_{k+1}$. It makes no choice based on the unknown value of $s_0$.

If, on a specified infinite set $I\subseteq\{64,65,\ldots\}$,


$$
\Delta_k=o(A^{k-1}),
\tag{8.4}
$$


then the selected whole errors tend to zero. Since $i(k)\ge k$, the selected indices are unbounded; repetitions can be removed.

If $s_0=a/b$ were rational, every positive whole error would satisfy


$$
q_is_0-p_i=\frac{aq_i-bp_i}{b}\ge\frac1b,
$$


contradicting (8.3)–(8.4).

Thus:



$$
\boxed{
\text{The Section 9 sufficient condition is correct.}
}
$$



Bounded $\Delta_k$ on an infinite set is a special case. A balanced neighboring-denominator assumption is unnecessary for this subsequence conclusion.

### 8.3 What Section 9 does not prove

No supplied argument proves:

- bounded $\Delta_k$ on an infinite set;
- $\Delta_k=o(A^{k-1})$;
- $q_k=o(A^{k-1})$;
- any replacement for the actual all-prime gcds in these assertions.

The selector is therefore a **conditional implication**. It is not a newly established irrationality proof.

The reported $13281$-digit value of $\Delta_{32}$, even if fully certified elsewhere, is one finite value. It neither verifies nor refutes an asymptotic little-$o$ hypothesis. Its numerical certification is not supplied in this packet and is not repeated here.

---

## 9. Preserving the same infinite original indices

### 9.1 The scope issue

All analytic results above hold at every integer $k\ge64$, so in particular at


$$
K_u=9^{18+32u}.
$$


However, the adjacent selector


$$
i(K_u)\in\{K_u,K_u+1\}
$$


may choose $K_u+1$, which is not an original index.

Thus an adjacent $\Delta_{K_u}$-bound would still be a valid route to irrationality through the compact family, but it would not, without an additional argument, produce the demanded whole-error sequence **at the same original indices**.

This is a scope correction, not a failure of the selector inequality.

### 9.2 An original-index selector

Put


$$
B=9^{32},\qquad K=K_u,\qquad L=K_{u+1}=BK.
$$


Iterating (7.5),


$$
0<\varepsilon_L\le4^{-(L-K)}\varepsilon_K.
\tag{9.1}
$$


Define the actual original-index cross difference


$$
\Delta_u^{\mathcal O}
=p_Lq_K-p_Kq_L>0.
\tag{9.2}
$$


Choose


$$
i_{\mathcal O}(u)\in\{K_u,K_{u+1}\}
$$


with the smaller actual denominator.

Both possible outputs are original indices. Applying (8.1) with


$$
\theta=4^{-(L-K)}\le\frac14
$$


gives


$$
\boxed{
0<q_{i_{\mathcal O}(u)}
\varepsilon_{i_{\mathcal O}(u)}
\le
\sqrt{\frac{42\Delta_u^{\mathcal O}}{A^{K_u-1}}}.
}
\tag{9.3}
$$



Consequently the original-domain condition


$$
\boxed{
\Delta_u^{\mathcal O}=o(A^{K_u-1})
\quad\text{on a specified infinite set of }u
}
\tag{9.4}
$$


would prove irrationality using only whole errors at original indices.

Because all $K_u$ are odd, the signs in the primitive normalization give the exact paid expression


$$
\boxed{
\Delta_u^{\mathcal O}
=
\frac{
H_{0,K_u}H_{1,K_{u+1}}
-H_{0,K_{u+1}}H_{1,K_u}
}{
G_{K_u}G_{K_{u+1}}
}.
}
\tag{9.5}
$$


The right side is positive by (9.1). Both final gcds remain present.

This is a concrete scope-correct follow-on lemma. Its analytic implication is proved; its arithmetic hypothesis (9.4) is open.

For comparison, the same original endpoints satisfy


$$
q_{K_u}q_{K_{u+1}}
\ge\frac{2A^{K_u-1}}{63},
$$


and hence


$$
\limsup_{u\to\infty}
\frac{\log q_{K_u}}{K_u}
\ge\frac{\log A}{B+1}.
\tag{9.6}
$$


Again, this is a lower-growth result, not a primitive-decay result.

---

## 10. Whole-error obligations and the unchanged arithmetic normalization

### 10.1 Exact sufficient and necessary denominator conditions

Multiplying (7.2) by the actual $q_k$,


$$
\boxed{
\frac{3q_k}{4k^2A^{k-1}}
\le\ell_k
\le\frac{63q_k}{2A^{k-1}}.
}
\tag{10.1}
$$



On any specified unbounded set of indices:

- a sufficient condition for $\ell_k\to0$ is
  

$$
q_k=o(A^{k-1});
  \tag{10.2}
$$


- a necessary condition for $\ell_k\to0$ is
  

$$
q_k=o(k^2A^{k-1}).
  \tag{10.3}
$$



These are conditions for the success of this primitive-error construction, not necessary conditions for irrationality of $e+\pi$ itself.

The accepted statement $q_k=o(33^{k-1})$ is also sufficient, since $33<A$.

The stronger asymptotic equivalence (6.7) gives


$$
\ell_k=q_kR_k(1+O(k^{-1})),
$$


but it supplies no arithmetic bound for $q_k$.

### 10.2 Clearers and contents remain distinct

Reuse the exact column clearers


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3).
$$


The least clearer of the entire raw right array remains $\Lambda_k$.

The established extracted factor and contact-minor divisor are


$$
E_k^{\rm arith}
=\prod_{j=0}^{k-1}\frac{\Lambda_k}{\Lambda_{k,j}},
\qquad
D_{k-1}^{\rm cont}=\prod_{r=0}^{k-2}(r!)^2,
$$


with


$$
D_{k-1}^{\rm cont}E_k^{\rm arith}\mid G_k.
\tag{10.4}
$$


They are lower divisors of $G_k$, not its value.

For the rational polynomial $H_k/\Lambda_k^k$, let


$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


Its actual least simultaneous coefficient clearer is


$$
\frac{\Lambda_k^k}{d_{H,k}},
$$


and its content after that clearing is


$$
\frac{G_k}{d_{H,k}}.
\tag{10.5}
$$


None of these quantities is evaluated by the Gamma comparison.

If a saturated contact basis $X$ is used, define


$$
B_{rj}^X=\sum_mX_{rm}r_{m+j},
\qquad
u_r=\sum_mX_{rm}(-1)^m.
$$


Its actual projected entry clearer remains


$$
L_X=
\frac{\Lambda_k}{
\gcd(\Lambda_k,\{\Lambda_kB_{rj}^X\}_{r,j})
}.
$$


Its row contents remain the actual gcds


$$
\gcd\bigl(L_Xu_r,\{L_XB_{rj}^X\}_j\bigr).
$$


If


$$
L_X^k\det\mathcal M_X(s)=A_0+A_1s,
$$


the least simultaneous coefficient clearer and remaining content remain


$$
\frac{L_X^k}{\gcd(L_X^k,A_0,A_1)},
\qquad
\frac{\gcd(A_0,A_1)}{\gcd(L_X^k,A_0,A_1)}.
\tag{10.6}
$$



No contact frame is selected in the present proof. Accordingly, no monic-row clearer, frame index, actual row content, subsequent column content, or final gcd is silently divided out.

### 10.3 The raw leading-$4$ scale is unchanged

The accepted raw estimates remain


$$
\log|H_k(s_0)|=4k^2\log k+O(k^2),
\qquad
\log|H_{1,k}|=4k^2\log k+O(k^2).
$$


The new theorem refines their difference:


$$
\log|H_k(s_0)|-\log|H_{1,k}|
=-(k-1)\log A+O(\log k).
$$


It does not change the leading-$4$ raw scale.

If


$$
\Gamma_k=\frac{G_k}{D_{k-1}^{\rm cont}E_k^{\rm arith}},
$$


then the established arithmetic bookkeeping still gives


$$
\log q_k
=3k^2\log k-\log\Gamma_k+O(k^2).
\tag{10.7}
$$


Thus successful primitive decay would require very substantial additional actual content. The present positive-matrix argument supplies no control over that content, especially its large-prime support and prime-power depth.

The conjectural content envelope remains conjectural. If proved, its consequence would be failure of primitive decay for this compact family—not rationality of $e+\pi$.

---

## 11. The original binary producer remains separate

The compact theorem applies at the original parameter values, but it is not an identification with the binary producer.

That producer retains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0,
$$


contact indices $0,\ldots,b-1$, physical reconstruction indices $0,\ldots,b$, and the terminal condition


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


In particular, $h^F$, $e_0$, $4b!$, and the division by $2^a$ are not removed.

The complete return remains


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f,
$$


and the paid valuation statement remains only


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)\ge\chi-a,
\qquad
\chi=v_2\binom{n+b-1}{b-1}.
$$


The subtraction of $a$ is indispensable.

Its norm


$$
Q=x_0^Tx_0,
$$


actual corrected-column contents, least simultaneous clearer, and final all-prime scalar gcd remain unevaluated here. Its established valuation


$$
v_3(q^{\rm bin})=n-\frac{b+15}{2}
$$


does not transfer to the compact denominator $q_k$.

The original-domain projection obligation therefore remains open independently of the analytic compact comparison.

---

## 12. Accepted, corrected, and unproved ledger

| Claim | Decision and exact scope |
|---|---|
| Gamma node lower bound $t_j\ge(k-1)/3$ | **Accepted**, for the specified $N=2k-1$, $\alpha=2k-2$, including the true last row. |
| Degree-$2N$ Gaussian lower comparison | **Accepted**; not exact quadrature at degree $2N$, but a positive orthogonal-square remainder. |
| $M_{-1}\le9(k-1)^{-2}M_0$ | **Accepted**, $k\ge2$, with maximum factorial degree $6k-4$. |
| Bernoulli and exterior Loewner directions | **Accepted**. |
| Exterior density factors | **Accepted**: $e^{-1}$ per variable, $e^{-k}$ per determinant. |
| Uniform $k\ge64$ constants | **Accepted**, by explicit polynomial inequalities and fixed exact integer comparisons. |
| Full overlap and atom payment | **Accepted by reuse** of A4 Turn 20, applied to the unchanged full $D_k,S_k$. |
| Two integration orders in Section 8 | **Accepted**, including all $k!$, $(k-1)!$, and compact $J$-normalizations. |
| Weighted Christoffel identity for “any positive compact measure” | **Qualified**: the relevant moment matrix must be positive definite. Valid for every measure used here. |
| Relative comparison $B_-\ge(1-\delta_k)B_+$ | **Accepted**, with $\delta_k=18/(k^2-11k+1)$. |
| Full bound $\frac12R_k\le\varepsilon_k\le\frac98R_k$ | **Proved**, for every $k\ge64$, for the same primitive compact pairs. |
| Exact logarithmic rate $\log A$ | **Proved** for the ordinary error. |
| Adjacent contraction $\varepsilon_{k+1}\le\varepsilon_k/4$ | **Proved**, every $k\ge64$. The previous A5 analytic contraction obligation is closed. |
| $\varepsilon_k/R_k\to1$ | **Additional proved consequence** of the audited relative estimates. |
| Section 9 minimum-denominator selector | **Accepted as a conditional theorem**; no balance hypothesis is needed for the selected subsequence. |
| $\Delta_k=o(A^{k-1})$ or an actual $q_k$ upper growth bound | **Unproved**. |
| Adjacent selector preserves $K_u=9^{18+32u}$ | **Not automatic**. Corrected by the original-endpoint selector (9.3). |
| Original-endpoint condition $\Delta_u^{\mathcal O}=o(A^{K_u-1})$ | **Concrete open arithmetic lemma**. |
| Actual final compact content and original binary projection | **Unresolved**. |
| Reported finite size of $\Delta_{32}$ | **Finite source claim only**, not independently certified here and not evidence of an infinite bound. |
| Irrationality or rationality of $e+\pi$ | **Unresolved**. |

---

## 13. Remaining bottleneck and bounded arithmetic status

### 13.1 A precise sufficient follow-on lemma

A sufficient original-domain arithmetic lemma is:

> On an explicitly specified infinite subset of $u\ge0$,
> 

$$
> \frac{
> H_{0,K_u}H_{1,K_{u+1}}
> -H_{0,K_{u+1}}H_{1,K_u}
> }{
> G_{K_u}G_{K_{u+1}}A^{K_u-1}
> }
> \longrightarrow0.
> \tag{13.1}
>
$$



The numerator has the positive orientation proved above. The two gcds are the actual all-prime gcds of the complete original compact coefficient pairs. Formula (9.3) proves the implication from this lemma to nonzero whole-error decay at original indices.

An alternative sufficient original-domain lemma is


$$
\frac{|H_{1,K_u}|}{G_{K_u}}=o(A^{K_u-1})
$$


on a specified infinite subset.

Neither is proved. Restating these paid quantities does not solve their growth problem; the advance here is that the analytic comparison and the selector implication are now fully evaluated and rigorously established.

### 13.2 No new expensive finite computation is needed

No finite determinant or gcd computation is required for the audited analytic theorem.

The only finite arithmetic checks used in the proof have the bounded inputs $k_0=64$, the polynomial expressions in Section 3, and the integers $3^{11}$, $4^{13}$. Their verifiable outputs are


$$
2\cdot64^2-121\cdot64+11=459>0,
$$




$$
64^2-56\cdot64+1=513>0,
$$




$$
200\cdot3^{11}=35429400<67108864=4^{13}.
$$


The monotonicity arguments then establish the stated inequalities for every $k\ge64$.

These checks have been derived in the report; no coordinator calculation is needed to complete them. No duplicate $k=32$, $k=64$, retired-matrix, or previously closed content calculation is proposed.

A future arithmetic experiment would require its own archive/literature gate and could establish only its explicitly bounded finite scope. It could not, by itself, supply the infinite hypothesis (13.1).

---

## Final conclusion

The complete new Gamma–Christoffel argument survives independent audit. Its strongest conclusions for the unchanged primitive compact pairs are


$$
\boxed{
\frac{\varepsilon_k}{R_k}=1+O(k^{-1}),
}
$$




$$
\boxed{
\frac{3}{4k^2A^{k-1}}
\le e+\pi-\frac{p_k}{q_k}
\le\frac{63}{2A^{k-1}},
\qquad
0<\varepsilon_{k+1}\le\frac14\varepsilon_k
\quad(k\ge64),
}
$$


and


$$
\boxed{
\lim_{k\to\infty}-\frac{\log\varepsilon_k}{k}
=\log(17+12\sqrt2).
}
$$



Section 9 correctly proves that an actual primitive adjacent-resultant bound


$$
\Delta_k=o(A^{k-1})
$$


would suffice through an explicit minimum-denominator selector, without a neighboring-denominator balance assumption. The original-index version requires the corresponding cross difference between consecutive original endpoints, as in (13.1).

The exact remaining bottleneck is still


$$
\boxed{
0<
\ell_{K_u}
=\frac{|H_{K_u}(e+\pi)|}{G_{K_u}}
\longrightarrow0
\quad\text{on one infinite set of original indices}.
}
$$



The analytic contraction is now proved. The required arithmetic cancellation after the actual all-prime gcd is not. Therefore **this report proves neither rationality nor irrationality of $e+\pi$**.
