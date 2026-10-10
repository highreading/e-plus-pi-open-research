> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 continuation: the moving prime cancels from the actual scalar channel

## Scope and main result

I obtain a new local conclusion for the **actual falling-factorial Gram center**, not an irrationality decision.

Let


$$
K=2001,\qquad n=p-1,\qquad b=\frac{p-1}{K},\qquad m=1,
$$


where $p\equiv1\pmod K$ is prime. At every finite index where the actual endpoint map is invertible, I prove, for all sufficiently large such primes,


$$
\boxed{p\nmid q_n.}
$$



This conclusion includes the scalar channel. In the notation of the supplied lattice factorization,


$$
\boxed{v_p(h)=v_p(D_0)=v_p(\gamma)=v_p(k)=0.}
$$


Thus the scalar channel contributes no denominator at $p$, whether or not its residual numerator $r$ is a unit.

There is also a useful strengthening of the previous norm calculation. The **actual matching row** determines the reduction of the zero-endpoint direction. Its norm is governed by one explicit quartic, rather than by anisotropy on an entire binary plane. Consequently the result above holds on all sufficiently large primes $p\equiv1\pmod{2001}$; the additional quadratic-character progression from the previous draft is unnecessary.

The unresolved factorial partial sums do remain in the local endpoint map and in the numerator residue. I identify them explicitly below. I do **not** assert that they are units.

All infinite applications to the normalized proportional center retain the supplied proportional analytic theorem’s author-level dependency status. The local algebra itself is proved below on its stated finite domain.

---

## 1. Finite domain and notation

For the local calculations, assume


$$
p\ \text{odd prime},\qquad n=p-1,\qquad b\ge5,\qquad 2b-3<p.
\tag{1.1}
$$


The original metric is


$$
\omega_j=\frac{(p+1)!}{(p+1-j)!},
\qquad
\Omega=\operatorname{diag}(\omega_0^2,\ldots,\omega_b^2).
\tag{1.2}
$$


These are falling weights throughout.

Write


$$
P=L_{p-1},\quad U=L_p,\quad A=P(1),\quad B=U(1),
$$




$$
f=\frac{2^{p-1}}{((p-1)!)^2},
\qquad
G=Aw_U-Bw_P=\frac{2^{2p+1}}p.
\tag{1.3}
$$


The actual endpoint rows are


$$
t_j=\frac{A T_j(U)-B T_j(P)}G,
\qquad
x_j=\frac{w_P T_j(U)-w_U T_j(P)}G,
\tag{1.4}
$$


and the matching row is


$$
\boldsymbol{s}=\boldsymbol e+\boldsymbol t.
$$



The relaxed high block has rows


$$
R_{lj}=E_{p-1+l,l+j-1},
\qquad 1\le l\le b-2,\quad 0\le j\le b.
\tag{1.5}
$$


Set


$$
\mathcal W=\ker_{\mathbb Q}\begin{bmatrix}R\\ \boldsymbol s\end{bmatrix},
\qquad
\mathscr L=\mathcal W\cap\mathbb Z^{b+1}.
\tag{1.6}
$$



When the endpoint map is invertible, choose the adapted saturated-lattice basis


$$
\mathscr L=\mathbb Zz_0\oplus\mathbb Zz_1,
\qquad
\boldsymbol e z_0=0,\qquad
\boldsymbol e z_1=h>0.
\tag{1.7}
$$


Here $z_0$ is primitive and


$$
\boldsymbol e(\mathscr L)=h\mathbb Z.
$$



The endpoint scalars are


$$
\xi=\boldsymbol xz_0,\qquad \eta=\boldsymbol xz_1.
$$


Let


$$
\xi=\frac a{D_0},\qquad \eta=\frac{b_{\rm end}}{D_0},
\qquad
\gcd(D_0,a,b_{\rm end})=1,
\tag{1.8}
$$


with $D_0>0$ minimal. Retain


$$
\gamma=\gcd(h,a,b_{\rm end}),\qquad
k=\frac{hD_0}{\gamma},\qquad
a'=\frac a\gamma,\qquad b'=\frac{b_{\rm end}}\gamma.
\tag{1.9}
$$



No reduction modulo $p$ will be made until the relevant rational quantities have been shown $p$-integral.

---

# 2. The complete endpoint rows are $p$-integral

Put


$$
\varepsilon=\left(\frac{-1}{p}\right)\in\{1,-1\}.
$$



### 2.1 The Legendre reductions

The generating function in the supplied integer normalization is


$$
\sum_{k\ge0}L_k(y)z^k
=
\bigl(1-4(2y-1)z-4z^2\bigr)^{-1/2}.
\tag{2.1}
$$


In characteristic $p$, writing $d=(p-1)/2$,


$$
F(z)^{-1/2}=F(z)^d\bigl(F(z)^{-1/2}\bigr)^p.
$$


Coefficient extraction at degrees $p-1$ and $p$ gives


$$
\boxed{P(y)\equiv\varepsilon\pmod p,}
\qquad
\boxed{U(y)\equiv4y^p-2\pmod p.}
\tag{2.2}
$$


In particular,


$$
\boxed{A\equiv\varepsilon,\qquad B\equiv2\pmod p.}
\tag{2.3}
$$


Thus $A$ is a unit in the integer $L_k$-normalization used here.

This computation matters: one cannot first reduce a monic Legendre normalization whose leading-coefficient denominator contains $p$, nor invert $n+1=p$ in $\mathbb F_p$.

Also


$$
f\equiv1\pmod p,\qquad pG=2^{2p+1}\equiv8\pmod p.
\tag{2.4}
$$



### 2.2 Second-kind values

Since $P(y)-A$ has all coefficients divisible by $p$,


$$
\frac{P(y)-A}{y-1}\in p\mathbb Z[y].
$$


Its degree is at most $p-2$. The relevant moment denominators are therefore $p$-units, and


$$
\boxed{v_p(w_P)\ge1.}
\tag{2.5}
$$



The Wronskian now gives


$$
A(pw_U)-B(pw_P)=pG,
$$


hence


$$
\boxed{v_p(w_U)=-1,\qquad pw_U\equiv8\varepsilon\pmod p.}
\tag{2.6}
$$


This is an exact use of the pole in $G$, not an inversion of $p$ modulo $p$.

### 2.3 Complete partial-exponential rows

For $0\le j\le b$, put


$$
F_j^{(p)}=\sum_{a=0}^{p-1-j}\frac1{a!}\pmod p.
\tag{2.7}
$$


Every factorial occurring in $T_j(P)$ or $T_j(U)$ has argument below $2p$, so its $p$-adic pole order is at most one.

Because every nonconstant coefficient of $P$ is divisible by $p$, while the constant coefficient multiplies the $p$-integral partial sum $F_j^{(p)}$,


$$
\boxed{T_j(P)\in\mathbb Z_{(p)}.}
\tag{2.8}
$$


For $U$, only its degree-$p$ coefficient contributes to $pT_j(U)$ modulo $p$. Wilson’s theorem gives


$$
\frac p{(p+a)!}\equiv-\frac1{a!}\pmod p
\qquad(0\le a<p),
$$


so


$$
\boxed{pT_j(U)\equiv-4F_j^{(p)}\pmod p.}
\tag{2.9}
$$



Substitution into the **complete** endpoint formulas (1.4) proves


$$
\boxed{t_j,x_j\in\mathbb Z_{(p)},}
\tag{2.10}
$$


with reductions


$$
\boxed{
t_j\equiv-\frac{\varepsilon}{2}F_j^{(p)},
\qquad
x_j\equiv-\varepsilon\,T_j(P)\pmod p.
}
\tag{2.11}
$$


Indeed, the $w_PT_j(U)$ contribution to $x_j$, after multiplication by $p/(pG)$, vanishes modulo $p$; the $w_UT_j(P)$ contribution does not.

Thus the actual matching row reduces to


$$
\boxed{s_j\equiv1-\frac{\varepsilon}{2}F_j^{(p)}\pmod p.}
\tag{2.12}
$$



---

# 3. The actual matching row makes $h$ a unit

The Rodrigues identity yields, for $0\le a\le b-3$,


$$
x^{p+a}H_{p+a}(x)\equiv x^{2p}x^aH_a(x)\pmod p.
$$


All derivative orders in (1.5) are below $p$. Hence


$$
R_{a+1,j}\equiv
\left.\frac{d^{a+j}}{dx^{a+j}}\bigl(x^aH_a(x)\bigr)\right|_{x=1}.
\tag{3.1}
$$


The polynomial on the right is monic of degree $2a$. Therefore


$$
R_{a+1,j}\equiv0\quad(j>a),\qquad
R_{a+1,a}\equiv(2a)!\ne0\pmod p.
\tag{3.2}
$$



Consequently:

* the first $b-2$ columns of $R$ form an invertible triangular block modulo $p$;
* any integral vector in $\ker R$ has its first $b-2$ coordinates divisible by $p$;
* the reduction of the high-row kernel is supported on the last three coordinates.

Put


$$
s=b-2.
$$


On these three coordinates, the matching row is


$$
\left(1-\frac{\varepsilon}{2}F_s^{(p)},
1-\frac{\varepsilon}{2}F_{s+1}^{(p)},
1-\frac{\varepsilon}{2}F_{s+2}^{(p)}\right).
$$


Its successive differences are nonzero:


$$
F_{j+1}^{(p)}-F_j^{(p)}
=-\frac1{(p-1-j)!}
=(-1)^j j!\pmod p.
\tag{3.3}
$$


Thus the restrictions of $\boldsymbol e$ and $\boldsymbol s$ to the three-dimensional tail are linearly independent.

It follows that


$$
\operatorname{rank}_{\mathbb F_p}[R;\boldsymbol s]=b-1,
\qquad
\operatorname{rank}_{\mathbb F_p}[R;\boldsymbol s;\boldsymbol e]=b.
\tag{3.4}
$$


These unit minors show that the corresponding kernels over $\mathbb Z_p$ are obtained without a hidden $p$-saturation defect. Moreover $\boldsymbol e$ maps the local rank-two kernel onto $\mathbb Z_p$.

Since localization of $\mathscr L$ is that kernel,


$$
\boxed{v_p(h)=0.}
\tag{3.5}
$$



This is a statement about the **actual matching row**. High-row rank alone would not prove it.

---

## 4. The reduction of the actual zero-endpoint direction

The tail of $z_0$ satisfies both


$$
z_{0,s}+z_{0,s+1}+z_{0,s+2}=0
$$


and


$$
F_s^{(p)}z_{0,s}
+F_{s+1}^{(p)}z_{0,s+1}
+F_{s+2}^{(p)}z_{0,s+2}=0.
$$


Using (3.3), their one-dimensional kernel is


$$
\boxed{
(z_{0,s},z_{0,s+1},z_{0,s+2})
\equiv
\lambda\,(-(s+1),s,1)\pmod p,
\quad \lambda\ne0.
}
\tag{4.1}
$$


The scalar $\lambda$ is nonzero because $z_0$ is primitive and all preceding coordinates are divisible by $p$.

Notice that the constant factorial partial sum $F_s^{(p)}$ has canceled from this direction. It does **not** cancel from the second endpoint direction or from the numerator residue below.

---

# 5. Exact scalar-channel formulas on the saturated lattice

Let the integer cumulative row be


$$
\mathsf p_0=0,\qquad
\mathsf p_j=\sum_{i=1}^jE_{p-1,i-1}.
\tag{5.1}
$$


Write


$$
P_0=\boldsymbol{\mathsf p}z_0,\qquad
P_1=\boldsymbol{\mathsf p}z_1,\qquad
T_P=T_0(P).
$$



The complete endpoint formulas, together with the matching equation, give a particularly useful identity:


$$
\boxed{
\boldsymbol xz
=
\frac{f}{A}\boldsymbol{\mathsf p}z
-\frac{T_P+w_P}{A}\boldsymbol ez
\qquad(z\in\mathcal W).
}
\tag{5.2}
$$



For completeness, the cumulative-row expressions are


$$
\boldsymbol t=t_0\boldsymbol e+
\frac{f}{pG}\left(pB\boldsymbol{\mathsf p}-2A\boldsymbol{\mathsf u}\right),
$$




$$
\boldsymbol x=x_0\boldsymbol e+
\frac{f}{pG}\left(pw_U\boldsymbol{\mathsf p}-2w_P\boldsymbol{\mathsf u}\right).
$$


Eliminate $\boldsymbol{\mathsf u}z$ using
$(\boldsymbol e+\boldsymbol t)z=0$. The Wronskian gives the coefficient $f/A$, and


$$
x_0-\frac{w_P}{A}(1+t_0)
=-\frac{T_P+w_P}{A}.
$$


This proves (5.2) while retaining the entire $T_P+w_P$ term.

Therefore


$$
\boxed{
\xi=\frac{fP_0}{A},
\qquad
\eta=\frac{fP_1-h(T_P+w_P)}{A}.
}
\tag{5.3}
$$


In particular,


$$
v_p(\xi)=v_p(P_0),
\qquad
v_p(\eta)=v_p\!\left(fP_1-h(T_P+w_P)\right).
\tag{5.4}
$$


The first equality applies when $\xi\ne0$, with the usual infinite-valuation convention otherwise.

Because the **whole row** $\boldsymbol x$ is $p$-integral, both $\xi$ and $\eta$ are $p$-integral. Their least common denominator satisfies


$$
\boxed{v_p(D_0)=0.}
\tag{5.5}
$$


Combining this with $v_p(h)=0$ gives


$$
\boxed{
v_p(\gamma)=0,\qquad v_p(k)=0.
}
\tag{5.6}
$$



This resolves the denominator side of the actual scalar channel. No unit assertion for $\xi,\eta$, or $r$, is needed.

---

# 6. A matching-specific norm calculation: an explicit quartic

This section develops a new consequence of the matching calculation; it is not an appeal to the earlier anisotropy theorem under review.

For $2\le j\le b$,


$$
\frac{\omega_j}{p}\equiv(-1)^{j-2}(j-2)!\pmod p.
\tag{6.1}
$$


Every weighted coordinate of a vector in $\ker R\cap\mathbb Z^{b+1}$ is divisible by $p$.

The first two high rows determine the first two weighted coordinates after division by $p$. The required congruences are


$$
\frac{E_{p,r}}p
\equiv2(-1)^{r-1}(r-1)!
\qquad(1\le r<p),
\tag{6.2}
$$




$$
\frac{E_{p+1,r}}p
\equiv2r(-1)^{r-3}(r-3)!
\qquad(3\le r<p).
\tag{6.3}
$$


To justify these without a modular division error:

* in $x^pH_p(x)$, every term other than the leading one contributes a multiple of $p^2$ to positive derivatives of order below $p$;
* in $x^{p+1}H_{p+1}(x)$, for orders at least three, only
  

$$
x^{2p+2}-(p+1)^2x^{2p+1}
$$


  survives after division by $p$ and reduction modulo $p$.

For a high-kernel vector $z$, put


$$
d_j=(-1)^{j-2}(j-2)!z_j,\qquad j=s,s+1,s+2.
$$


The two row equations then give


$$
\frac{z_0}{p}\equiv2\sum_{j=s}^{s+2}(j-1)d_j,
\qquad
\frac{(p+1)z_1}{p}\equiv-2\sum_{j=s}^{s+2}j\,d_j.
\tag{6.4}
$$


Here the subscripts in (6.4) are coordinate indices, not lattice-basis labels.

For the actual lattice vector $z_0$, use (4.1), and put


$$
c_s=(-1)^{s-2}(s-2)!.
$$


The nonzero coordinates of $\operatorname{diag}(\omega_j)z_0/p$, modulo $p$, are therefore


$$
\lambda c_s
\bigl(
2(1-s),\ 4s,\ -(s+1),\ -s(s-1),\ s(s-1)
\bigr).
\tag{6.5}
$$


They occur at coordinate indices $0,1,s,s+1,s+2$.

Consequently, for


$$
T=z_0^T\Omega z_0,
$$


one has


$$
\boxed{
\frac{T}{p^2}
\equiv
\lambda^2c_s^2\,N(s)\pmod p,
}
\tag{6.6}
$$


where


$$
\begin{aligned}
N(s)
&=4(s-1)^2+16s^2+(s+1)^2+2s^2(s-1)^2\\
&=\boxed{2s^4-4s^3+23s^2-6s+5.}
\end{aligned}
\tag{6.7}
$$



Thus


$$
p\nmid N(b-2)
\quad\Longrightarrow\quad
\boxed{v_p(T)=2.}
\tag{6.8}
$$


For any $z_1\in\mathscr L$, all weighted coordinates are divisible by $p$, so


$$
V_0=z_0^T\Omega z_1
\quad\text{satisfies}\quad v_p(V_0)\ge2.
$$


Hence


$$
\boxed{
v_p\bigl(\gcd(T,V_0)\bigr)=2
}
\tag{6.9}
$$


under the same quartic nonvanishing condition.

### Specialization to $b=(p-1)/K$

Modulo $p$,


$$
s=b-2\equiv-2-\frac1K.
$$


Define the fixed positive integer


$$
\boxed{
J_K=173K^4+210K^3+95K^2+20K+2.
}
\tag{6.10}
$$


Expansion of (6.7) gives


$$
K^4N\!\left(-2-\frac1K\right)=J_K.
$$


Therefore


$$
p\nmid KJ_K\quad\Longrightarrow\quad p\nmid N(s).
\tag{6.11}
$$



For $K=2001$, only finitely many primes are excluded by $p\mid J_K$. Dirichlet’s theorem supplies infinitely many primes $p\equiv1\pmod K$, and all sufficiently large such primes satisfy (6.11).

This widens the previous infinite subfamily: no Legendre-symbol condition is required.

---

# 7. The final gcd and actual primitive denominator at the moving prime

Retain the exact intrinsic definitions


$$
\delta=\gcd(T,|V_0|),\quad
t=\frac T\delta,\quad
v_0=\frac{V_0}{\delta},
$$




$$
\alpha=\gcd(t,|a'|),\qquad
r=\frac{a'v_0-b't}{\alpha}.
\tag{7.1}
$$


The actual primitive denominator and final Gram gcd are


$$
q_n=\frac t\alpha\,\frac{k}{\gcd(k,|r|)},
\qquad
g_B=k\delta\alpha\gcd(k,|r|).
\tag{7.2}
$$



Under (6.11),


$$
v_p(T)=v_p(\delta)=2,
\qquad
v_p(t)=v_p(\alpha)=0.
$$


Section 5 proved $v_p(k)=0$. Thus


$$
\boxed{v_p(q_n)=0.}
\tag{7.3}
$$


More explicitly,


$$
\boxed{
v_p(A_B)=2,\qquad v_p(g_B)=2,\qquad v_p(H_B)\ge2.
}
\tag{7.4}
$$


The two powers in the norm are exactly removed by the final gcd.

The requested scalar difference satisfies


$$
\boxed{
v_p(k)-v_p(r)=-v_p(r)\le0.
}
\tag{7.5}
$$


If $r=0$, the right side is interpreted as $-\infty$, and the exact gcd formula still gives no $p$-factor in $q_n$.

The exact depth of $r$ is a numerator question, not a remaining denominator question at this prime. I give its finite-dimensional residue obstruction next.

---

# 8. The unresolved local factorial functions, explicitly identified

The preceding denominator result does not say that the endpoint map is invertible modulo $p$.

From (4.1) and (5.1),


$$
P_0\equiv
\lambda\bigl((s+1)E_{p-1,s}+E_{p-1,s+1}\bigr)\pmod p.
$$


Since derivatives of $x^p$ of orders $1,\ldots,p-1$ vanish modulo $p$,


$$
(s+1)E_{p-1,s}+E_{p-1,s+1}
\equiv H_{p-1}^{(s+1)}(1)\pmod p.
$$


Therefore


$$
\boxed{
\xi\equiv
\varepsilon\lambda\,\mathcal J_p(s)\pmod p,
\qquad
\mathcal J_p(s)=H_{p-1}^{(s+1)}(1)\pmod p.
}
\tag{8.1}
$$



This is an explicit truncated factorial function. Let


$$
c_t=[z^t]\frac1{1-z+z^2/2},
\qquad
c_0=c_1=1,\quad c_t=c_{t-1}-\frac12c_{t-2}.
$$


For $t<p$, the coefficient of $z^t$ in
$(1-z+z^2/2)^{p-1}$ is $c_t$ modulo $p$. Hence


$$
\boxed{
\mathcal J_p(s)=
(-1)^{s+1}
\sum_{t=0}^{p-s-2}
(-1)^t(t+s+1)!\,c_t
\pmod p.
}
\tag{8.2}
$$


No unit property of (8.2) is proved here.

In particular, the least lift denominator can still have a $p$-factor:


$$
d_B=\frac{h|a|}{\gamma},
\qquad
\boxed{v_p(d_B)=v_p(\xi).}
\tag{8.3}
$$


This possible lift denominator does **not** survive in the actual center denominator, by (7.3).

### 8.1 An explicit three-dimensional formula for $r\bmod p$

Set


$$
a_s=(-1)^ss!,\qquad
\beta=\frac{2\varepsilon-F_s^{(p)}}{a_s},
$$


and define tail vectors


$$
v=(-(s+1),s,1),\qquad w=(1-\beta,\beta,0).
\tag{8.4}
$$


Their endpoint sums are $0$ and $1$, and both satisfy the matching equation modulo $p$.

Let


$$
C_s=\operatorname{diag}\bigl(1,-(s-1),s(s-1)\bigr),
$$




$$
M_s=I_3+4aa^T+4bb^T,
\quad
a=(s-1,s,s+1)^T,\quad b=(s,s+1,s+2)^T.
$$


Put


$$
\mathcal B_s(u,v)=(C_su)^TM_s(C_sv).
\tag{8.5}
$$


Then $\mathcal B_s(v,v)=N(s)$.

The exact center is


$$
\mathfrak c_n=\frac{\xi V_0/T-\eta}{h}.
$$


All divisions in the following reduction are now by proven units:


$$
\boxed{
\mathfrak c_n\equiv
\varepsilon\left[
T_s(P)-\beta E_{p-1,s}
+
\mathcal J_p(s)\frac{\mathcal B_s(v,w)}{N(s)}
\right]\pmod p.
}
\tag{8.6}
$$


The basis parameters $\lambda$ and the freedom to replace $z_1$ by $z_1+az_0$ cancel.

Since


$$
\mathfrak c_n=\frac{r}{k(t/\alpha)}
$$


and $k(t/\alpha)$ is a $p$-unit,


$$
v_p(r)=v_p(\mathfrak c_n).
\tag{8.7}
$$


Thus a nonzero value in (8.6) proves $v_p(r)=0$; a zero value means that higher precision is required. Neither outcome changes $v_p(q_n)=0$.

The partial-exponential term in (8.6) can be evaluated with all denominators retained. Writing


$$
P(y)=\sum_{m=0}^{p-1}P_my^m,
$$


one has $p\mid P_m$ for $m\ge1$, and


$$
\boxed{
T_s(P)\equiv
\varepsilon F_s^{(p)}
-\sum_{m=s+1}^{p-1}
\left(\frac{P_m}{p}\right)
\sum_{a=0}^{m-s-1}\frac1{a!}
\pmod p.
}
\tag{8.8}
$$


The divisions $P_m/p$ are exact integer divisions before reduction. Formula (8.8), or the exact identity


$$
T_s(P)=f\left(\mathcal A_{p-1}-\mathsf p_s\right),
\tag{8.9}
$$


retains the complete factorial contraction.

Equations (8.2), (8.6), and (8.8) are the precise unresolved local numerator functions. There is no heuristic unit declaration.

---

# 9. A block extension: endpoint denominators vanish above $n$

There is a useful extension beyond the single prime $p=n+1$.

### Proposition 9.1 — endpoint integrality above the degree

For every $n\ge b\ge3$, every $0\le j\le b$, and every odd prime $p>n$,


$$
\boxed{x_j,t_j\in\mathbb Z_{(p)}.}
\tag{9.1}
$$


Consequently the endpoint denominator $D_0$, whenever defined, has no prime factor greater than $n$.

#### Proof

The case $p=n+1$ was proved above.

Suppose $p\ge n+2$. The second-kind moment denominators are $p$-units, and


$$
G=\frac{(-1)^n2^{2n+3}}{n+1}
$$


is a $p$-unit. It remains to prove integrality of $T_j(L_n)$ and $T_j(L_{n+1})$.

If their factorial indices are below $p$, there is nothing to prove. Otherwise use the polynomial reflection congruence


$$
P_{p-1-r}(X)\equiv P_r(X)\pmod p
\qquad(0\le r\le(p-1)/2).
\tag{9.2}
$$


It follows directly from the hypergeometric coefficients: the parameters
$-k,k+1$ are interchanged modulo $p$ by $k\mapsto p-1-k$.
In the $L_k$-normalization,


$$
L_{p-1-r}(y)\equiv
\varepsilon(-4)^{-r}L_r(y)\pmod p.
\tag{9.3}
$$



Thus $L_n\bmod p$ has degree at most $p-1-n$, and $L_{n+1}\bmod p$ has degree at most $p-2-n$, in precisely the range where a factorial denominator could contain $p$. Their surviving terms have respective partial-sum indices at most $p-1-j$ and $p-2-j$. Every other coefficient contains the factor $p$ needed to cancel the sole possible factorial pole.

This proves the required $T$-integrality. Substitution in the complete formulas (1.4) proves (9.1). ∎

This proof does not invert a possibly vanishing Legendre endpoint. It uses the Wronskian $G$, which is a unit in this range.

### 9.2 A bounded-dimensional obstruction for nearby primes

Let


$$
p=n+d,\qquad 1\le d\le b/2,\qquad 2b-3<p.
$$


For high-row indices $l\ge2d-1$, write $n+l=p+(l-d)$. The same Rodrigues reduction gives a triangular unit pivot at column


$$
j=l-2d+1.
$$


There are $b-2d$ such pivots.

Eliminating these columns over $\mathbb Z_p$ leaves:

* exactly $2d+1$ tail variables;
* $2d-2$ remaining high equations;
* one actual matching equation;
* the actual endpoint-sum and reconstructed endpoint rows.

All elimination denominators are units. The remaining high equations must still be **saturated over $\mathbb Z_p$**; one cannot reduce a row that is entirely divisible by $p$ before dividing out its actual local content.

For fixed $d$, this gives a finite-dimensional obstruction of dimension $2d+1$. After saturation, the local index $h$ is a unit exactly when the endpoint-sum row is not in the row span of the saturated constraints modulo $p$. Proposition 9.1 has already removed new endpoint denominators $D_0$ from this block.

For $d=1$, the obstruction is the three-dimensional problem solved in Sections 3–8. For $d\ge2$, I have not proved the necessary saturated-rank and metric noncancellation assertions.

This is the exact limit of the block extension:

* fixed-width blocks give bounded-dimensional problems, but not linear prime mass;
* a width proportional to $n$ could contain linear logarithmic prime mass, but the residual dimension then grows proportionally to $n$;
* Dirichlet’s theorem for one progression does not supply simultaneous primality of several prescribed nearby linear forms.

Accordingly, the new block lemma does not yet provide a global denominator rate.

---

# 10. Audit of the five-state extension to arbitrary fixed $b$

The extension claimed by A2 is valid for **raw contractions after the displayed forced row divisions**, provided the allocation parameter $b$ is held fixed during the congruence comparison. There is no need to enlarge the five scalar state coordinates.

There is, however, no uniform bounded-degree polynomial representation as $b\to\infty$.

Let


$$
S_n=(h_n,u_n,v_n,\mathcal A_n,\mathcal M_n).
$$


The supplied five-state transition is linear in $S_n$, with coefficients of degree at most three in $n$. Thus the state at $n+l-1$ is linear in $S_n$, with polynomial coefficient degree at most $3(l-1)$.

The jet recurrence gives polynomial expressions over $\mathbb Z[1/2]$ for all required derivatives. More specifically:

* $E_{n,r}$, expressed in $S_n$, has coefficient degree at most $r$;
* $E_{n+1,r}$, expressed in $S_n$, has coefficient degree at most $r+1$;
* for $k\ge1,r\ge1$, the exactly divided quantity
  

$$
E_{k,r}/k
$$


  has coefficient degree at most $r$ in the state at $k-1$.

The last statement follows from


$$
\frac{E_{k,r}}k
=
\frac{H_k^{(r)}(1)}k
+\sum_{a=1}^r
\binom ra(k-1)_{a-1}H_k^{(r-a)}(1),
\tag{10.1}
$$


together with the normalized derivative recurrence. No inverse of $k$ occurs on the right after expressing the normalized jets through the previous state.

For matched degree $b$, use the first high row undivided and rows $l\ge2$ divided by $n+l$. Their coefficient degrees in $n$ are bounded by


$$
b+1\quad(l=1),\qquad
4l+b-4\quad(2\le l\le b-1).
$$


The sum of these bounds is


$$
3b^2-7b+5.
$$


The cumulative rows contribute at most $b-1$ and $b$. Therefore the raw complete contraction $V^{(b)}_n$ can be represented as a polynomial over $\mathbb Z[1/2]$ with


$$
\boxed{
\deg_n V^{(b)}\le3b^2-5b+4,
\qquad
\deg_{S}V^{(b)}\le b+1.
}
\tag{10.2}
$$



These are explicit quantitative bounds. They imply:

1. **For each fixed $b$:** the supplied all-prime-power transfer of $S_n$ extends to these raw contractions at every odd prime, including primes dividing some $n+l$, because the forced divisions have already been eliminated by polynomial identities.

2. **For proportional $b$:** the same construction still uses five base scalar values, but needs jets and shifts of order $b$; the contraction’s state degree grows linearly and its coefficient degree can grow quadratically in $b$.

3. **What does not transfer automatically:** maximal-minor content division, full contraction-content division, the saturated lattice basis, the metric row constructed from $z_0$, and the final endpoint gcd. None is a fixed polynomial operation on the five-state vector.

4. **Changing $b$ changes the function:** a congruence between $V^{(b)}_n$ and $V^{(b)}_r$ holds with the same $b$. It is not a congruence between $V^{(b(n))}_n$ and $V^{(b(r))}_r$.

Thus A2’s fixed-$b$ interface is sound at the raw level, but it is not a uniform finite-seed denominator theorem for the proportional family.

---

# 11. Whole evaluated error and what the new result does not prove

On the enlarged infinite subfamily


$$
n=p-1,\qquad b=(p-1)/2001,\qquad m=1,
$$


the local results above prove, at every normal index and for all sufficiently large primes in the progression,


$$
p\nmid q_n.
$$



Let


$$
\mathfrak c_n=\frac{p_n}{q_n},\qquad
\gcd(p_n,q_n)=1,\quad q_n>0.
$$


If the supplied proportional signed-error theorem is accepted with its stated dependencies, then


$$
\epsilon_n=\mathfrak c_n-(e+\pi)\ne0
$$


eventually, and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{2001}\right)\log(1+\sqrt2)\,n+o(n).
$$


The **whole primitive evaluated error** is exactly


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n\ne0.
}
\tag{11.1}
$$


Its rate remains


$$
\log|q_n(e+\pi)-p_n|
=
\log q_n
-\left(2+\frac1{2001}\right)\log(1+\sqrt2)\,n+o(n).
\tag{11.2}
$$



Removing one moving prime from $q_n$ does not bound the sum of contributions from the other primes. In particular, this result proves neither a favorable global denominator rate nor an exclusionary one.

The project remains open.

---

## (1) New result and proof status

**Proved here by explicit finite arithmetic:**

* At $n=p-1$, the genuine endpoint rows $\boldsymbol x,\boldsymbol t$ are $p$-integral, with reductions (2.11).
* The actual matching row gives
  

$$
v_p(h)=0,
$$


  and fixes the primitive zero-endpoint tail direction (4.1).
* The complete endpoint map on the saturated lattice is (5.3), yielding
  

$$
v_p(D_0)=v_p(\gamma)=v_p(k)=0.
$$


* The matching-specific norm is controlled by
  

$$
N(s)=2s^4-4s^3+23s^2-6s+5.
$$


  Consequently, for all sufficiently large primes $p\equiv1\pmod{2001}$,
  

$$
\boxed{p\nmid q_n}
$$


  at every finite normal index.
* Endpoint integrality extends to every odd prime $p>n$, and nearby-prime arithmetic reduces to the explicit $2d+1$-dimensional saturated problem in Section 9.
* The five-state fixed-$b$ extension admits the quantitative degree bounds (10.2); these bounds are not uniform constants for proportional $b$.

These are new author-level deductions, not independently audited results. Eventual normality and whole-error nonvanishing retain the supplied analytic dependency boundary.

## (2) Exact remaining bottleneck

The selected moving prime is no longer an unresolved denominator obstruction:


$$
v_p(q_n)=0.
$$



The missing global estimate is still a bound for the **actual final denominator**


$$
q_n=
\frac{t}{\gcd(t,|a'|)}
\frac{k}{\gcd(k,|r|)}
$$


over enough primes at the same index to compare $\log q_n$ with


$$
\left(2+\frac1{2001}\right)\log(1+\sqrt2)\,n.
$$



For nearby primes $p=n+d$, the newly bounded follow-on obligation is precise: control the saturated residual system of dimension $2d+1$, its endpoint index $h$, and its actual restricted falling-factorial metric. For a prime block large enough to have linear mass, that dimension is not bounded.

The factorial function $\mathcal J_p(s)$ and the complete residue (8.6) remain unresolved as numerator functions. Their possible vanishing has **not** been concealed by a unit assumption.

## (3) Bounded exact computation request

No computation is needed to make the local arguments infinite.

For an independent algebra audit, I request only the following bounded symbolic calculation, if the coordinator elects to arrange it:

**Inputs**


$$
v=(-(s+1),s,1),\quad
w=(1-\beta,\beta,0),
$$




$$
C_s=\operatorname{diag}(1,-(s-1),s(s-1)),
$$




$$
M_s=I_3+4(s-1,s,s+1)^T(s-1,s,s+1)
       +4(s,s+1,s+2)^T(s,s+1,s+2).
$$



**Expected verifiable output**

1. Exact verification that
   

$$
(C_sv)^TM_s(C_sv)=2s^4-4s^3+23s^2-6s+5.
$$


2. Exact expansion of $(C_sv)^TM_s(C_sw)$, for auditing (8.6).
3. Exact verification that
   

$$
K^4N(-2-1/K)=173K^4+210K^3+95K^2+20K+2.
$$



This is a polynomial-identity audit only. It would not settle the remaining global denominator estimate or the irrationality question.
