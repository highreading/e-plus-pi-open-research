> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 Turn 0 — Complete paid adjacent determinants and a proved contraction of the actual rational errors

## 1. Result and proof status

The rationality or irrationality of


$$
s_0=e+\pi
$$


remains unresolved.

This report makes a substantive analytic advance for the **same complete compact determinant family**, without introducing a new producer or changing its primitive normalization:

> **New adjacent-contraction theorem.** For every $k\ge64$, the actual primitive rational zeros satisfy
> 

$$
> 0<\varepsilon_{k+1}\le \frac14\varepsilon_k,
> \qquad
> \varepsilon_k:=e+\pi-\frac{p_k}{q_k}.
> \tag{1.1}
>
$$


> Consequently,
> 

$$
> p_{k+1}q_k-p_kq_{k+1}>0
> \qquad(k\ge64).
> \tag{1.2}
>
$$



The proof does not invoke an interlacing theorem for the signed mixed functional. Its new ingredient is an evaluated inverse-moment estimate for the positive factorial ensemble already underlying the accepted conditioning argument. That estimate removes the exponential losses which previously prevented adjacent comparison.

A second consequence is a sharper, evaluated approximation rate. Put


$$
\mathfrak a=17+12\sqrt2.
$$


Then, for every $k\ge64$,


$$
\boxed{
\frac{1}{k^2\mathfrak a^{\,k-1}}
\le
e+\pi-\frac{p_k}{q_k}
\le
\frac{42}{\mathfrak a^{\,k-1}}.
}
\tag{1.3}
$$


In particular,


$$
\lim_{k\to\infty}
-\frac1k\log\left(e+\pi-\frac{p_k}{q_k}\right)
=\log(17+12\sqrt2).
\tag{1.4}
$$



These are statements about the **ordinary rational error**. They do not establish decay of the whole primitive error


$$
\ell_k=q_k(e+\pi)-p_k.
$$



The paid adjacent identity is independently validated below, including its signs, common-clearer factor, finite boundaries, and both final all-prime gcds. The new contraction gives the following evaluated comparison for its actual reduced cross difference:


$$
\boxed{
\frac{3q_kq_{k+1}}{4k^2\mathfrak a^{\,k-1}}
\le
\Delta_k:=p_{k+1}q_k-p_kq_{k+1}
\le
\frac{42q_kq_{k+1}}{\mathfrak a^{\,k-1}}.
}
\tag{1.5}
$$


In particular, the adjacent Schur numerator is no longer an unevaluated scalar of unknown sign.

What remains unresolved is its **arithmetic size after primitive reduction**. The report proves neither $\Delta_k=O(1)$ nor a suitable sublinear bound relative to $q_{k+1}$. It also proves no denominator-growth law strong enough to establish whole-error divergence.

The $k=32$ content-envelope refutation is retained as a completed finite result. It is not recomputed, and it is not extrapolated to an infinite domain.

---

## 2. Exact family and accepted inputs

### 2.1 Complete moments and physical boundaries

For the compact family,


$$
k\ge2,\qquad 0\le m<2k,\qquad 0\le j<k.
$$


The complete sequences are


$$
a_0=1,\qquad a_d=1-da_{d-1},
$$




$$
c_n=a_{2n}-(-1)^n,
$$




$$
\rho_0=0,\qquad
\rho_{n+1}+\rho_n=\frac1{2n+1},
$$




$$
r_n=-(2n)!+4\rho_n.
$$



Define


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5)
$$


and


$$
H_k(s)=
\det\left[
(c_{m+j})\ \middle|\
\bigl(\Lambda_k[r_{m+j}+s(-1)^{m+j}]\bigr)
\right]
=H_{0,k}+H_{1,k}s.
\tag{2.1}
$$



The period matrix in the right block has rank one, so the determinant is affine. The last original moment is exactly


$$
r_{3k-2};
$$


the largest factorial is $(6k-4)!$, and the last possible odd denominator is $6k-5$.

The actual final normalization is


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$




$$
q_k=\frac{|H_{1,k}|}{G_k},\qquad
p_k=-\frac{\operatorname{sgn}(H_{1,k})H_{0,k}}{G_k}.
\tag{2.2}
$$


No lower divisor of $G_k$ is substituted for $G_k$ in these definitions.

### 2.2 Accepted analytic scope

The supplied sign theorem gives, for $k\ge32$,


$$
(-1)^kH_k(s_0)>0,\qquad
(-1)^kH_{1,k}>0.
\tag{2.3}
$$


Thus


$$
\ell_k:=q_ks_0-p_k=\frac{|H_k(s_0)|}{G_k}>0,
\qquad
\varepsilon_k=\frac{\ell_k}{q_k}
=\frac{|H_k(s_0)|}{|H_{1,k}|}.
\tag{2.4}
$$



The independently accepted A4 Turn 20 bounds are


$$
\frac1{16k^2\,204^{k-1}}
\le \varepsilon_k
\le \frac{336}{11^{k-1}},
\qquad k\ge64.
\tag{2.5}
$$


They concern the same primitive pair (2.2).

The accepted raw scale is


$$
\log|H_k(s_0)|=4k^2\log k+O(k^2),
\tag{2.6}
$$


not the older, weaker leading-$2$ estimate.

### 2.3 Accepted arithmetic scope

Write


$$
D_{k-1}^{\mathrm{Lag}}
=\prod_{r=0}^{k-2}(r!)^2,
$$




$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3),
\qquad
E_k=\frac{\Lambda_k^k}{\prod_{j=0}^{k-1}\Lambda_{k,j}}.
$$


The established statements are:

* $\Lambda_{k,j}$ is the actual least clearer of the complete raw rational column $j$;
* $E_k$ is the exact column-extraction factor;
* the product, including shared prime powers, satisfies
  

$$
D_{k-1}^{\mathrm{Lag}}E_k\mid G_k.
  \tag{2.7}
$$



These are reused results. They do not evaluate $G_k$.

The proposed envelope


$$
G_k\mid
D_{k-1}^{\mathrm{Lag}}E_k\,2^{2k^2}\Lambda_k^{2k}
\tag{2.8}
$$


is **refuted**, not open: the supplied $k=32$ certificate disproves it.

---

## 3. Independent audit of the nested array

Define


$$
\sigma_n=c_{n+1}+c_n=a_{2n+2}+a_{2n},
\tag{3.1}
$$


and, importantly,


$$
\boxed{
\tau_n=r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
\tag{3.2}
$$


The arctangent correction in (3.2) is indispensable.

Start with the rational determinant $H_k(s)/\Lambda_k^k$.

1. In descending order $m=2k-1,\ldots,1$, replace row $m$ by $R_m+R_{m-1}$.
2. In descending order $j=k-1,\ldots,1$, replace right column $j$ by the sum of right columns $j$ and $j-1$.

Descending order ensures that each addition uses the original neighboring row or column. Both transformations have determinant one.

After the row operation, the period term vanishes from every row except row $0$. After the column operation, it also vanishes from every right column except column $0$.

Order the columns as


$$
T_0,C_0,T_1,C_1,\ldots,T_{k-1},C_{k-1}.
$$


The number of crossings is


$$
k+(k-1)+\cdots+1=\frac{k(k+1)}2,
$$


so the permutation sign is


$$
\omega_k=(-1)^{k(k+1)/2}.
\tag{3.3}
$$



The resulting infinite array is exactly:



$$
\begin{array}{ll}
\mathscr M_{0,T_0}(s)=s-1,
&
\mathscr M_{r,T_0}(s)=\tau_{r-1}\quad(r\ge1),\\[2mm]
\mathscr M_{0,C_j}=c_j,
&
\mathscr M_{r,C_j}=\sigma_{r+j-1}\quad(r\ge1),\\[2mm]
\mathscr M_{0,T_j}=\tau_{j-1}\quad(j\ge1),
&
\mathscr M_{r,T_j}
=\tau_{r+j-1}+\tau_{r+j-2}
\quad(r,j\ge1).
\end{array}
\tag{3.4}
$$



Its leading $2k\times2k$ determinant is


$$
\det\mathscr M_k(s)
=\omega_k\frac{H_k(s)}{\Lambda_k^k}.
\tag{3.5}
$$



Thus the nesting claim is correct: increasing $k$ adds precisely rows $2k,2k+1$ and columns $T_k,C_k$. No discarded correction is required to obtain that nesting.

---

## 4. Paid bordering identity and both final gcds

Fix an adjacent pair and set


$$
\lambda=\Lambda_{k+1},\qquad
t=\frac{\Lambda_{k+1}}{\Lambda_k}\in\mathbb Z_{>0}.
$$


Multiply every $T$-column in the relevant enlarged array by $\lambda$. All entries are integral, except for the indeterminate occurring as $\lambda(s-1)$.

Let


$$
F(s)=\det\mathscr M_k^{[\lambda]}(s),\qquad
F^+(s)=\det\mathscr M_{k+1}^{[\lambda]}(s).
$$


Then


$$
F(s)=\omega_k t^kH_k(s),\qquad
F^+(s)=\omega_{k+1}H_{k+1}(s).
\tag{4.1}
$$



In particular, their **actual coefficient contents** are


$$
\operatorname{cont}(F)=t^kG_k,\qquad
\operatorname{cont}(F^+)=G_{k+1}.
\tag{4.2}
$$



### 4.1 Blocks and terminal audit

Partition the enlarged matrix as


$$
\begin{pmatrix}
\lambda(s-1)&b&\beta\\
d&B_0&U\\
\delta&V&W
\end{pmatrix},
\tag{4.3}
$$


where $B_0$ has size $2k-1$.

The new blocks include


$$
\beta=(\lambda\tau_{k-1},c_k),
$$




$$
U_{r,0}=\lambda(\tau_{r+k-1}+\tau_{r+k-2}),\qquad
U_{r,1}=\sigma_{r+k-1},
\quad 1\le r\le2k-1,
$$




$$
\delta=
\begin{pmatrix}
\lambda\tau_{2k-1}\\
\lambda\tau_{2k}
\end{pmatrix},
$$


and


$$
W=
\begin{pmatrix}
\lambda(\tau_{3k-1}+\tau_{3k-2})&\sigma_{3k-1}\\
\lambda(\tau_{3k}+\tau_{3k-1})&\sigma_{3k}
\end{pmatrix}.
\tag{4.4}
$$



The largest underlying moment is $r_{3k+1}$, which is precisely


$$
3(k+1)-2.
$$


The largest factorial is $(6k+2)!$, and the last odd denominator is $6k+1$. These are the physical boundaries of the $k+1$ matrix, not additional successor moments.

### 4.2 Integer Schur numerators

Put


$$
D=\det B_0,
$$




$$
\mathcal S=DW-V\operatorname{adj}(B_0)U,
$$




$$
\mathcal t=D\beta-b\operatorname{adj}(B_0)U,
$$




$$
\mathcal z=D\delta-V\operatorname{adj}(B_0)d,
$$


and


$$
\mathcal K=\det\mathcal S,\qquad
\mathcal T=\mathcal t\,\operatorname{adj}(\mathcal S)\mathcal z.
\tag{4.5}
$$


All these quantities are integers.

The coefficient of $s$ in $F$ is


$$
F_1=\lambda D.
\tag{4.6}
$$


The accepted slope nonvanishing therefore gives $D\ne0$ for $k\ge32$.

Eliminating $B_0$ leaves the $3\times3$ block


$$
\frac1D
\begin{pmatrix}
F(s)&\mathcal t\\
\mathcal z&\mathcal S
\end{pmatrix}.
$$


The simultaneous row and column reordering needed to place $B_0$ first has total sign $1$. Hence


$$
F^+(s)
=
D\cdot D^{-3}
\det
\begin{pmatrix}
F(s)&\mathcal t\\
\mathcal z&\mathcal S
\end{pmatrix},
$$


which proves


$$
\boxed{
D^2F^+(s)=\mathcal K F(s)-\mathcal T.
}
\tag{4.7}
$$



Coefficient comparison gives


$$
F_1=\lambda D,\qquad
F_1^+=\frac{\lambda\mathcal K}{D}.
\tag{4.8}
$$


Thus $\mathcal K\ne0$ on the same nonvanishing domain.

Equation (4.7) pays the division by $D^2$: its integer numerator is coefficientwise divisible by $D^2$. It does not authorize any additional division of $H_k$ or $H_{k+1}$.

The denominator-free identity is polynomial and remains valid at singular specializations. The divided formulas use $D\ne0$.

### 4.3 Sign audit

For $k\ge32$,


$$
\operatorname{sgn}D
=\omega_k(-1)^k.
\tag{4.9}
$$


Furthermore,


$$
\operatorname{sgn}\mathcal K
=\operatorname{sgn}(D F_1^+)
=(-1)^k,
\tag{4.10}
$$


because


$$
\frac{\omega_{k+1}}{\omega_k}=(-1)^{k+1}.
$$



The sign of $\mathcal T$ does not follow from this algebra alone. It will be settled by the new contraction theorem.

### 4.4 Adjacent resultant and primitive reduction

Writing $F=F_0+F_1s$ and $F^+=F_0^++F_1^+s$, equation (4.7) yields


$$
D(F_0F_1^+-F_0^+F_1)=\lambda\mathcal T.
\tag{4.11}
$$



The primitive orientations in (2.2) give


$$
\Delta_k
=
-\frac{H_{0,k}H_{1,k+1}-H_{0,k+1}H_{1,k}}
{G_kG_{k+1}}.
$$


Also,


$$
\omega_k\omega_{k+1}=(-1)^{k+1}.
$$


Consequently,


$$
\boxed{
D\,t^kG_kG_{k+1}\Delta_k
=(-1)^k\lambda\mathcal T.
}
\tag{4.12}
$$



Both actual all-prime gcds occur in (4.12). Neither can be replaced by $D_{k-1}^{\mathrm{Lag}}E_k$, its adjacent analogue, or a guessed envelope.

The exact rational gap is


$$
\boxed{
\frac{p_{k+1}}{q_{k+1}}-\frac{p_k}{q_k}
=\frac{\mathcal T}{\lambda D\mathcal K}.
}
\tag{4.13}
$$


Equivalently,


$$
\varepsilon_{k+1}
=\varepsilon_k-\frac{\mathcal T}{\lambda D\mathcal K}.
\tag{4.14}
$$



The A5 Turn 14 bordering and normalization identities are therefore independently validated.

---

## 5. Exact measure representation and the retained loss terms

The new argument uses the accepted measure representation, not a modified pencil.

Define


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
\tag{5.1}
$$



The overlap mass and negative atom are exactly


$$
\mu([0,1])=1-e^{-2},
\qquad
L=\mu-\delta_{-1}.
\tag{5.2}
$$



The endpoint identities give


$$
\nu_n=e\,c_n+r_n+s_0(-1)^n.
\tag{5.3}
$$


Thus replacing the right block by the $\nu$-moment block at $s=s_0$ is a determinant-preserving addition of $e$ times the corresponding contact columns.

Let


$$
J_k^\nu=\det(\nu_{i+j})_{i,j<k},
$$




$$
d\nu_+(y)=(1+y)^2\,d\nu(y),\qquad
J_{k-1}^+=\det\left(\int y^{i+j}\,d\nu_+(y)\right)_{i,j<k-1}.
$$



Define


$$
\mathcal D_k=\frac{(-1)^kH_k(s_0)}{\Lambda_k^kJ_k^\nu},
\qquad
S_k=\frac{(-1)^kH_{1,k}}{\Lambda_k^kJ_{k-1}^+}.
\tag{5.4}
$$



Using normalized compact Vandermonde ensembles,


$$
A_k(x)=
\mathbb E_{\nu,k}\prod_{i=1}^k\prod_{j=1}^k(x_i-y_j),
$$


one has


$$
\mathcal D_k
=\frac1{k!}\int V(x)^2A_k(x)\,dL^k(x).
\tag{5.5}
$$


Similarly,


$$
S_k=
\frac1{k!}\int V(x)^2
\prod_{i=1}^k(x_i+1)\,
\mathbb E_{\nu_+,k-1}
\prod_{i=1}^k\prod_{j=1}^{k-1}(x_i-y_j)
\,d\mu^k(x).
\tag{5.6}
$$



In (5.6), the contact atom disappears because a simultaneous compact atom at $-1$ creates the exact cross factor $(-1-x_i)$, which vanishes when $x_i=-1$. It is not deleted by approximation.

### 5.1 Accepted complete overlap and atom bounds

Put


$$
Z_k=\det((2k+2i+2j)!)_{i,j<k},
$$




$$
\kappa_k=
\frac{\binom{4k-1}{2k-2}}{(2k)!},
\qquad
\zeta_k=(e-e^{-1})\kappa_k,
\qquad
b_k=\frac{e\,8^k}{4}\kappa_k.
\tag{5.7}
$$



Let $\mathcal D_k^{\mathrm{ext}}$ and $S_k^{\mathrm{ext}}$ denote the contributions with all contact variables $x_i>1$. The accepted complementary-minor estimates give


$$
|\mathcal D_k-\mathcal D_k^{\mathrm{ext}}|
\le e^{-k}Z_k\,d_k,
$$




$$
|S_k-S_k^{\mathrm{ext}}|
\le e^{-k}Z_k\,d_k^+,
\tag{5.8}
$$


where


$$
d_k=e^{\zeta_k}(1+b_k)-1,
\qquad
d_k^+=2^k(e^{\zeta_k}-1).
\tag{5.9}
$$



The first bound includes **both the entire overlap contribution and the entire negative-atom contribution**.

For completeness, the accepted coefficient-functional estimate


$$
\kappa_k\le\frac{16^k}{(2k)!}
\le\left(\frac{36}{k^2}\right)^k
$$


implies, for $k\ge64$,


$$
e^{\zeta_k}<2,\qquad
e^{\zeta_k}-1\le6\kappa_k.
$$


Hence


$$
d_k\le 2\cdot8^k\kappa_k,\qquad
d_k^+\le2\cdot8^k\kappa_k,
$$


and therefore


$$
\boxed{
d_k,d_k^+\le2\cdot4^{-k}<\frac1{64}
\qquad(k\ge64).
}
\tag{5.10}
$$



No new moment or physical row is used in these estimates.

---

## 6. New evaluated inverse-moment lemma

The previous exterior shift estimate lost a factor $e^{-k}$, and the previous slope upper bound lost a factor $2^k$. Both can be avoided.

### Lemma 6.1 — Inverse-square control for the same factorial ensemble

Let $(s_1,\ldots,s_k)\in(0,\infty)^k$ have probability density


$$
\frac1{k!Z_k}
V(s_1^2,\ldots,s_k^2)^2
\prod_{i=1}^k s_i^{2k}e^{-s_i}.
\tag{6.1}
$$


Then


$$
\boxed{
\mathbb E\sum_{i=1}^k\frac1{s_i^2}
\le \frac1{2(2k-1)}.
}
\tag{6.2}
$$


Moreover, for every $u\ge0$,


$$
\boxed{
\mathbb E\prod_{i=1}^k
\left(1+\frac{u}{s_i^2}\right)
\le
\exp\!\left(\frac{u}{2(2k-1)}\right).
}
\tag{6.3}
$$



#### Proof of (6.2)

Write the unnormalized density as $P(s)$. Away from coincident coordinates,


$$
\frac{\partial}{\partial s_i}\log P
=
\frac{2k}{s_i}-1
+4s_i\sum_{j\ne i}\frac1{s_i^2-s_j^2}.
$$


Integration by parts is legitimate: the density has sufficient vanishing at zero, exponential decay at infinity, and a polynomial squared-Vandermonde factor at collisions.

Summing the identities $\int\partial_{s_i}P=0$ gives


$$
0=
2k\,\mathbb E\sum_i\frac1{s_i}
-k
+4\,\mathbb E\sum_{i<j}\frac1{s_i+s_j}.
$$


The last term is nonnegative, so


$$
\mathbb E\sum_i\frac1{s_i}\le\frac12.
\tag{6.4}
$$



Next integrate $\partial_{s_i}(P/s_i)$. Summing over $i$, the pair terms cancel:


$$
\sum_i\sum_{j\ne i}\frac1{s_i^2-s_j^2}=0.
$$


Thus


$$
(2k-1)\mathbb E\sum_i\frac1{s_i^2}
=
\mathbb E\sum_i\frac1{s_i}.
$$


Combining this identity with (6.4) proves (6.2).

#### Proof of (6.3)

Set


$$
M=((2k+2i+2j)!)_{i,j<k},
\qquad
M_-=((2k-2+2i+2j)!)_{i,j<k}.
$$


Both are positive Gram matrices. Andréief’s identity gives


$$
\mathbb E\prod_i\left(1+\frac{u}{s_i^2}\right)
=
\frac{\det(M+uM_-)}{\det M}.
\tag{6.5}
$$


Put


$$
B=M^{-1/2}M_-M^{-1/2}\succeq0.
$$


Differentiating (6.5) at $u=0$ shows


$$
\operatorname{tr}B
=
\mathbb E\sum_i\frac1{s_i^2}.
$$


Therefore


$$
\log\det(I+uB)
\le u\,\operatorname{tr}B
\le \frac{u}{2(2k-1)},
$$


which proves (6.3). ∎

### Boundary qualification

The largest factorial in $M$ is $(6k-4)!$; that in $M_-$ is $(6k-6)!$. The inverse-moment argument lowers powers. It does not enlarge the original factorial boundary.

This is not a new Smith-form diagonalization or a change of producer. It is a quantitative estimate for the positive reference ensemble already represented by $Z_k$.

---

## 7. Constant-factor comparison with the compact Christoffel quantity

Let


$$
a_k^*=\frac1{2(2k-1)}.
$$



Under $x_i=s_i^2$, the exact exterior density contributes the factor $e^{-k}$, and the ensemble in Lemma 6.1 supplies the remaining normalized integral.

### 7.1 Exterior determinant

For $x_i>1$ and $0\le y_j\le1$,


$$
0\le
\prod_{i,j}\left(1-\frac{y_j}{x_i}\right)
\le1.
$$


Also,


$$
\prod_{i,j}\left(1-\frac{y_j}{x_i}\right)
\ge
1-k\sum_i\frac1{x_i}.
$$


After insertion of the indicator that every $x_i>1$, this lower inequality remains valid on the whole positive orthant: if one $x_i\le1$, its right side is nonpositive.

Consequently,


$$
\boxed{
1-ka_k^*
\le
\frac{\mathcal D_k^{\mathrm{ext}}}{e^{-k}Z_k}
\le1.
}
\tag{7.1}
$$



### 7.2 Exterior slope

The normalized slope factor is


$$
\prod_i\left(1+\frac1{x_i}\right)
\prod_{i,j}\left(1-\frac{y_j}{x_i}\right),
\qquad j=1,\ldots,k-1.
$$


On the exterior it is at least


$$
1-(k-1)\sum_i\frac1{x_i}.
$$


For the upper bound, discard the second product and use Lemma 6.1 with $u=1$. Thus


$$
\boxed{
1-(k-1)a_k^*
\le
\frac{S_k^{\mathrm{ext}}}{e^{-k}Z_k}
\le e^{a_k^*}.
}
\tag{7.2}
$$



This replaces the earlier exponential exterior losses by uniform constants.

### 7.3 Restoring the complete overlap and negative atom

For $k\ge64$,


$$
ka_k^*\le\frac{32}{127},
\qquad
(k-1)a_k^*\le\frac14,
\qquad
a_k^*\le\frac1{254}.
$$


Combining (5.8)–(5.10), (7.1), and (7.2) gives


$$
\frac{\mathcal D_k}{e^{-k}Z_k}
\ge \frac{95}{127}-\frac1{64}
>\frac{23}{32},
$$




$$
\frac{\mathcal D_k}{e^{-k}Z_k}
\le\frac{65}{64}<\frac{33}{32},
$$


and


$$
\frac{S_k}{e^{-k}Z_k}
\ge\frac34-\frac1{64}
>\frac{23}{32}.
$$


Finally, $e^x\le(1-x)^{-1}$ for $0\le x<1$, so


$$
\frac{S_k}{e^{-k}Z_k}
\le\frac{254}{253}+\frac1{64}
<\frac{33}{32}.
$$



We have proved the uniform complete-moment comparison


$$
\boxed{
\frac{23}{32}
\le
\frac{\mathcal D_k}{e^{-k}Z_k},
\frac{S_k}{e^{-k}Z_k}
\le
\frac{33}{32}
\qquad(k\ge64).
}
\tag{7.3}
$$



The signed contact atom and the full overlap have been restored before forming any error ratio.

---

## 8. The new adjacent-contraction theorem

Define the compact extremal quantity


$$
R_k^\nu=\frac{J_k^\nu}{J_{k-1}^+}.
\tag{8.1}
$$



The rank-one atom update of the positive compact moment matrix gives


$$
R_k^\nu
=
\frac1{K_{k-1}^\nu(-1,-1)}
=
\min_{\substack{\deg p\le k-1\\p(-1)=1}}
\int_0^1p(x)^2\,d\nu(x).
\tag{8.2}
$$


Indeed, the coefficient of an added atom $u\delta_{-1}$ is both
$J_k^\nu K_{k-1}^\nu(-1,-1)$ and $J_{k-1}^+$. The minimum follows from the evaluation-functional norm.

From (5.4),


$$
\varepsilon_k
=R_k^\nu\,\frac{\mathcal D_k}{S_k}.
$$


Thus (7.3) proves


$$
\boxed{
\frac{23}{33}R_k^\nu
\le\varepsilon_k
\le\frac{33}{23}R_k^\nu.
}
\tag{8.3}
$$


In particular, the simpler constants


$$
\frac23R_k^\nu\le\varepsilon_k\le\frac32R_k^\nu
\tag{8.4}
$$


are valid.

### Theorem 8.1 — Actual adjacent contraction

For every $k\ge64$,


$$
0<\varepsilon_{k+1}\le\frac14\varepsilon_k.
$$



#### Proof

Let $p$ be the minimizer in (8.2). The polynomial


$$
\widetilde p(x)=p(x)\frac{1-2x}{3}
$$


has degree at most $k$, satisfies $\widetilde p(-1)=1$, and on $[0,1]$ obeys


$$
|\widetilde p(x)|^2\le\frac19|p(x)|^2.
$$


Hence


$$
R_{k+1}^\nu\le\frac19R_k^\nu.
$$


Using (8.4),


$$
\varepsilon_{k+1}
\le\frac32R_{k+1}^\nu
\le\frac16R_k^\nu
\le\frac14\varepsilon_k.
$$


Strict positivity is already supplied by (2.3), and also follows from (7.3). ∎

Using the sharper constants in (8.3) would give


$$
\frac{\varepsilon_{k+1}}{\varepsilon_k}
\le\frac{121}{529}<\frac14.
$$


The simpler quarter-contraction is sufficient below.

### 8.1 The previously open Schur contraction is now proved

Equations (4.7)–(4.8) imply


$$
\frac{\varepsilon_{k+1}}{\varepsilon_k}
=
1-\frac{\mathcal T}{\mathcal K F(s_0)}.
$$


Therefore


$$
\boxed{
\frac34
\le
\frac{\mathcal T}{\mathcal K F(s_0)}
<1
\qquad(k\ge64).
}
\tag{8.5}
$$



This proves, with a stronger constant, the adjacent-contraction lemma proposed in A5 Turn 14.

In particular,


$$
\operatorname{sgn}\mathcal T
=\operatorname{sgn}(\mathcal K F(s_0))
=\omega_k.
\tag{8.6}
$$


Together with (4.9)–(4.10), this verifies that the gap in (4.13) is positive.

No Markov zero-monotonicity theorem has been applied to $L$. Such an application would require hypotheses not supplied by a signed measure with overlap. The proof instead uses the positive compact extremal problem and explicitly controlled complete mixed determinants.

---

## 9. Evaluated approximation rate and actual reduced cross difference

### 9.1 Sharper evaluated error bounds

A4 Turn 20 established, with


$$
\beta=3+2\sqrt2,\qquad \mathfrak a=\beta^2=17+12\sqrt2,
$$


that


$$
\frac{3}{2k^2\mathfrak a^{\,k-1}}
\le R_k^\nu
\le
\frac{28}{\mathfrak a^{\,k-1}}.
\tag{9.1}
$$



The hypotheses are exactly those present here: $\nu$ is positive on $[0,1]$, has density at least $3/2$ in the $x$-coordinate, and total mass less than $7$. The lower estimate is the Legendre evaluation-kernel bound; the upper estimate uses the normalized Chebyshev test polynomial.

Combining (9.1) with (8.4) proves (1.3):


$$
\frac1{k^2\mathfrak a^{\,k-1}}
\le\varepsilon_k
\le\frac{42}{\mathfrak a^{\,k-1}}.
\tag{9.2}
$$


Since $33<\mathfrak a<34$, an entirely rational version is


$$
\boxed{
\frac1{k^2\,34^{k-1}}
\le\varepsilon_k
\le\frac{42}{33^{k-1}}.
}
\tag{9.3}
$$



These improve the accepted $204/11$ bounds, but do not alter the primitive pair.

Multiplication by the actual $q_k$ gives


$$
\boxed{
\frac{q_k}{k^2\mathfrak a^{\,k-1}}
\le\ell_k
\le\frac{42q_k}{\mathfrak a^{\,k-1}}.
}
\tag{9.4}
$$



Thus the assignment’s sufficient target


$$
q_k=o(11^{k-1})
$$


remains sufficient. The new proof also supplies the less restrictive sufficient condition


$$
q_k=o(\mathfrak a^{\,k-1}).
$$


Neither denominator condition has been proved.

The exact exponential comparison is


$$
\boxed{
\log\ell_k
=
\log q_k-(k-1)\log\mathfrak a+O(\log k).
}
\tag{9.5}
$$


The unknown term is the actual primitive denominator, not an analytic remainder.

### 9.2 Actual adjacent cross difference

The contraction gives


$$
\frac34\varepsilon_k
\le
\varepsilon_k-\varepsilon_{k+1}
<\varepsilon_k.
\tag{9.6}
$$


Therefore


$$
\Delta_k
=q_kq_{k+1}(\varepsilon_k-\varepsilon_{k+1})
$$


is a positive integer, and


$$
\boxed{
\frac{3q_kq_{k+1}}{4k^2\mathfrak a^{\,k-1}}
\le\Delta_k
\le
\frac{42q_kq_{k+1}}{\mathfrak a^{\,k-1}}.
}
\tag{9.7}
$$



For comparison, using only the accepted $204/11$ bounds after proving contraction gives the weaker but valid checkpoint


$$
\frac{3q_kq_{k+1}}{64k^2\,204^{k-1}}
\le\Delta_k
\le
\frac{336q_kq_{k+1}}{11^{k-1}}.
\tag{9.8}
$$



The exact paid expression is now


$$
\boxed{
\Delta_k
=
\frac{\lambda|\mathcal T|}
{|D|\,t^kG_kG_{k+1}}>0.
}
\tag{9.9}
$$



Thus the sign and relative scale of the **actual reduced** cross difference are proved. Its absolute arithmetic size is not.

An equivalent logarithmic statement is


$$
\log\Delta_k
=
\log q_k+\log q_{k+1}
-(k-1)\log\mathfrak a+O(\log k).
\tag{9.10}
$$



### 9.3 An explicit, but insufficient, absolute ceiling

The accepted slope-height estimate and product divisor give


$$
q_k\le \mathscr Q_k,
$$


where


$$
\mathscr Q_k=
\frac{
\Lambda_k^k4^kk!\,28^{k-1}h_{k-1}
\prod_{r=0}^{k-1}(2k+4r)!
}{
D_{k-1}^{\mathrm{Lag}}E_k
},
\tag{9.11}
$$


and the rational factor is explicitly


$$
h_m=
\frac{
2^{m(m-1)}\prod_{j=1}^{m-1}(j!)^2
}{
\prod_{i,j=0}^{m-1}(2i+2j+1)
}.
$$


Consequently,


$$
0<\Delta_k
\le
\frac{42\,\mathscr Q_k\mathscr Q_{k+1}}{33^{k-1}}.
\tag{9.12}
$$


This is a fully specified $k$-dependent ceiling, but its logarithm still has order $k^2\log k$. It does not approach the arithmetic strength required for primitive decay.

Conversely, integrality of $\Delta_k$ gives


$$
q_kq_{k+1}\ge\frac{\mathfrak a^{\,k-1}}{42}
\qquad(k\ge64).
\tag{9.13}
$$


Unlike the earlier transition-only bound, this holds at every adjacent pair in the tail. Nevertheless, it is only weak exponential lower growth. It is compatible with $q_k=o(11^k)$ and does not resolve the whole-error target.

---

## 10. A sharper arithmetic bottleneck: no balanced-denominator hypothesis is needed

The new contraction yields a useful exact reduction:


$$
\frac{\Delta_k}{q_{k+1}}
=
\ell_k\left(1-\frac{\varepsilon_{k+1}}{\varepsilon_k}\right).
$$


Hence


$$
\boxed{
\frac{\Delta_k}{q_{k+1}}
<\ell_k
\le
\frac43\frac{\Delta_k}{q_{k+1}}.
}
\tag{10.1}
$$



The cancellation of $G_{k+1}$ in this particular ratio is legitimate and explicit:


$$
\boxed{
\frac{\Delta_k}{q_{k+1}}
=
\frac{|\mathcal T|}
{t^kG_k|\mathcal K|}.
}
\tag{10.2}
$$


Equation (9.9), however, still requires both gcds for $\Delta_k$ itself.

### 10.1 Conditional irrationality implication

Let $\mathcal I$ be an infinite subset of the original indices


$$
\{9^{18+32u}:u\ge0\}.
$$


If one proves


$$
\Delta_k=o(q_{k+1})
\qquad(k\to\infty,\ k\in\mathcal I),
\tag{10.3}
$$


then (10.1) gives


$$
0<\ell_k\longrightarrow0
\qquad(k\in\mathcal I).
$$


If $s_0=A/B$ were rational, then


$$
\ell_k=\frac{Aq_k-Bp_k}{B}\ge\frac1B,
$$


a contradiction.

A bounded primitive cross difference on $\mathcal I$ would suffice:


$$
\Delta_k\le C.
\tag{10.4}
$$


Indeed, the already established $q_n\to\infty$ gives


$$
\ell_k\le\frac{4C}{3q_{k+1}}\longrightarrow0.
$$



Thus the additional balanced-neighbor condition proposed in A5 Turn 14 is unnecessary once contraction is proved. A bound on $\Delta_k$ alone would suffice.

This is a **conditional deduction**, not a proved arithmetic bound.

### 10.2 A concrete follow-on lemma

One precise arithmetic target is:

> **Paid sublinear-resultant lemma.** On an explicitly specified infinite subset $\mathcal I$ of the original indices,
> 

$$
> 0<\Delta_k\le \frac{q_{k+1}}{k}.
> \tag{10.5}
>
$$



It would imply


$$
0<\ell_k\le\frac4{3k}\longrightarrow0.
$$



In terms of the complete adjacent integer data, (10.5) is exactly


$$
k\lambda|\mathcal T|
\le
|D|\,t^kG_k\,|H_{1,k+1}|.
\tag{10.6}
$$


Every division and gcd in this formulation is specified.

The lemma is open. Naming it does not solve it. What has been proved in this report is the analytic comparison that makes it sufficient and eliminates the formerly separate adjacent-order obligation.

---

## 11. Same infinite original indices

Put


$$
K_u=9^{18+32u},\qquad B=9^{32}.
$$


All the new compact theorems hold at every $K_u$.

Iterating the adjacent contraction gives


$$
\varepsilon_{BK}
\le4^{-(B-1)K}\varepsilon_K.
\tag{11.1}
$$


Thus consecutive rational zeros on the original progression are strictly increasing.

Define their actual primitive cross difference


$$
\Delta^{\mathrm{orig}}_u
=
p_{BK}q_K-p_Kq_{BK}>0.
$$


Both $K$ and $BK$ are odd, so the coefficient version, with both final gcds, is


$$
\Delta^{\mathrm{orig}}_u
=
\frac{
H_{0,K}H_{1,BK}-H_{0,BK}H_{1,K}
}{
G_KG_{BK}
}.
\tag{11.2}
$$



Moreover,


$$
\boxed{
\left(1-4^{-(B-1)K}\right)\ell_K
\le
\frac{\Delta^{\mathrm{orig}}_u}{q_{BK}}
<\ell_K.
}
\tag{11.3}
$$



This keeps the whole evaluated error and both primitive rationals on the same infinite original index set. It does not identify the compact producer with the separate binary reconstruction.

The arithmetic quantity in (11.3) remains uncontrolled. No inference of whole-error decay or divergence is made from its positivity.

---

## 12. The completed $k=32$ refutation and its exact scope

The coordinator-certified finite calculation is retained as an input; it has not been re-run here.

The supplied receipt reports


$$
v_2(G_{32})=3375,\qquad
v_2(D_{31}^{\mathrm{Lag}})=780.
$$


Since $E_{32}$ and $\Lambda_{32}$ are odd, the proposed envelope has


$$
v_2(B_{32})=780+2048=2828.
$$


Thus the excess is exactly


$$
3375-2828=547,
$$


in agreement with


$$
\frac{G_{32}}{\gcd(G_{32},B_{32})}=2^{547}.
\tag{12.1}
$$



Therefore the all-$k\ge32$ envelope is false. Any replacement retaining the same other factors and using an allowance $2^{Ck^2}$ would already require


$$
C\ge\frac{3375-780}{32^2}
=\frac{2595}{1024}
$$


at this one index. This is only a necessary finite compatibility check, not a proposed infinite theorem.

The same receipt establishes:

* $q_{32}$ has $6437$ decimal digits;
* $G_{32}$ has $2054$ decimal digits;
* $D_{31}^{\mathrm{Lag}}E_{32}\mid G_{32}$;
* after trial division by every prime at most $187$, the remaining factor of $G_{32}$ is $1$;
* the complete primitive whole error satisfies
  

$$
q_{32}(e+\pi)-p_{32}\ge10^{4857}>1.
$$



These conclusions establish exactly one auxiliary compact instance. They neither prove infinite divergence nor exclude later or original-index primitive decay.

The new contraction theorem concerns $k\ge64$, so no retrospective adjacent-contraction assertion at $k=32$ is inferred from it.

---

## 13. Why the arithmetic problem survives the new analytic theorem

The earlier obstruction had two parts:

1. no proved ordering or contraction of neighboring actual rational zeros;
2. no control of the adjacent resultant after both final gcds.

The first is now resolved by Theorem 8.1. The second is not.

In fact, (8.5) shows that the complete Schur numerator has the raw size


$$
\frac34|\mathcal K F(s_0)|
\le|\mathcal T|
<|\mathcal K F(s_0)|.
\tag{13.1}
$$


It is not an intrinsically small integer numerator. Smallness of the primitive resultant would have to come from the paid arithmetic normalization.

Let


$$
\Gamma_k=\frac{G_k}{D_{k-1}^{\mathrm{Lag}}E_k}.
$$


The accepted raw scale gives


$$
\log q_k
=
3k^2\log k-\log\Gamma_k+O(k^2).
\tag{13.2}
$$


Neither the contraction nor positivity bounds $\Gamma_k$ from above or below at the required scale.

At primes beyond the moment-denominator range, the same mixed-pencil obstruction remains. For


$$
A_k=[C\mid\Lambda_k\mathcal R],\qquad
u_k=\Lambda_kw,\qquad
z_k=(0,\ldots,0,v)^T,
$$


simultaneous divisibility is governed by


$$
\det A_k\equiv0,\qquad
z_k^T\operatorname{adj}(A_k)u_k\equiv0\pmod p.
\tag{13.3}
$$


Rank loss or nullvector nontransversality can force both. Analytic positivity over $\mathbb R$ does not exclude these events over finite fields, and does not bound their prime-power depth.

Accordingly:

* the sign of $\mathcal T$ is now known;
* the sign of every adjacent primitive cross difference is now known;
* the rational approximation rate is now known exactly at exponential scale;
* the all-prime primitive normalization is still the unresolved arithmetic bottleneck.

No supplied classical kernel, Smith-form, or zero-monotonicity theorem closes that bottleneck for this same mixed pencil.

---

## 14. Normalization and original-producer ledger

### 14.1 Compact least clearers and actual contents

For the rational polynomial $H_k/\Lambda_k^k$, define


$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


Its actual least simultaneous coefficient clearer and remaining content are


$$
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
\tag{14.1}
$$


After both payments, the primitive affine pair is exactly $H_k/G_k$, up to orientation.

For a saturated integer contact basis $X$, put


$$
B_{rj}^{X}=\sum_mX_{rm}r_{m+j},
\qquad
u_r=\sum_mX_{rm}(-1)^m.
$$


The least entry clearer remains


$$
L_X=
\frac{\Lambda_k}
{\gcd\!\left(\Lambda_k,\{\Lambda_kB_{rj}^{X}\}_{r,j}\right)}.
$$


Actual row contents are


$$
\gcd\bigl(L_Xu_r,\{L_XB_{rj}^{X}\}_j\bigr).
$$


If


$$
L_X^k\det\mathcal M_X(s)=A_0+A_1s,
$$


the actual least simultaneous coefficient clearer and remaining content are


$$
\frac{L_X^k}{\gcd(L_X^k,A_0,A_1)},
\qquad
\frac{\gcd(A_0,A_1)}{\gcd(L_X^k,A_0,A_1)}.
\tag{14.2}
$$



Individual monic-row clearers, actual row and column contents, and the saturation payment


$$
\frac{|\det C_k|}{\delta_{k,2k-1}}
$$


remain separate. The direct determinant argument does not assign them guessed values.

### 14.2 Separate binary producer

The original binary domain remains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


Its contact indices are $0,\ldots,b-1$, while its physical reconstruction includes $0,\ldots,b$, with


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


The forcing $h^F$, correction $e_0$, and division by $4b!$ are not removed.

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



The norm $Q=x_0^Tx_0$, actual corrected-column contents, least simultaneous clearer, and final all-prime scalar gcd of that producer are not evaluated by this report. Its established valuation


$$
v_3(q^{\mathrm{bin}})
=n-\frac{b+15}{2}
$$


is not transferred to $q_k$.

The original-domain projection obligation therefore remains distinct and unresolved.

---

## 15. Bounded exact arithmetic: no repeated $k=32$ calculation

No finite computation is needed for the proofs in §§6–10.

If the coordinator admits one further arithmetic diagnostic after the stated archive/literature gate, a $k=32\to33$ extension can reuse the completed $k=32$ certificate rather than repeat it.

### Inputs

Use the certified


$$
H_{0,32},\ H_{1,32},\ G_{32},\ p_{32},\ q_{32}
$$


as fixed inputs.

Extend the complete recurrences only to

* $a_0,\ldots,a_{194}$;
* $\rho_0,\ldots,\rho_{97}$;
* $c_0,\ldots,c_{97}$ and $r_0,\ldots,r_{97}$.

Set


$$
\Lambda_{33}=\operatorname{lcm}(1,3,\ldots,193).
$$


The common-clearer step is exactly


$$
t=\frac{\Lambda_{33}}{\Lambda_{32}}
=191\cdot193=36863.
$$


Indeed, the other new odd integer $189=3^3\cdot7$ is already cleared by $\Lambda_{32}$.

Form the complete $66\times66$ matrices defining $H_{33}(0)$ and $H_{33}(1)$. If any column compression is used, its entire determinant scalar must be recorded and restored.

### Expected verifiable outputs

1. Exact $H_{0,33}$ and $H_{1,33}$, with determinant certificates.
2. The actual all-prime gcd $G_{33}$, with both divisibility checks and a Bézout identity.
3. The actual primitive pair
   

$$
q_{33}=-\frac{H_{1,33}}{G_{33}},
   \qquad
   p_{33}=\frac{H_{0,33}}{G_{33}},
$$


   using the accepted sign $H_{1,33}<0$.
4. The exact integer
   

$$
\Delta_{32}=p_{33}q_{32}-p_{32}q_{33}
$$


   and the exact rational number $\Delta_{32}/q_{33}$.
5. If the adjacent border is also certified, exact $D,\mathcal K,\mathcal T$ and zero residuals for
   

$$
D^2F^+-\mathcal K F+\mathcal T,
   \qquad
   D\,t^{32}G_{32}G_{33}\Delta_{32}-\lambda\mathcal T,
$$


   where
   

$$
F=t^{32}H_{32},\qquad F^+=-H_{33}.
$$



No numerical value or sign of $\Delta_{32}$ is predicted here. The new uniform contraction theorem starts at $64$. This calculation would evaluate one new adjacent arithmetic instance; it would establish neither an infinite resultant bound nor an original-index instance.

---

## 16. Final assessment

### New proved statements

For the actual complete compact family, with its original moments and final gcds:

1. The paid nested and bordering identities are independently validated:
   

$$
D^2F^+=\mathcal K F-\mathcal T,
$$


   

$$
D\,t^kG_kG_{k+1}\Delta_k=(-1)^k\lambda\mathcal T.
$$



2. The new factorial-ensemble estimate
   

$$
\mathbb E\sum_i s_i^{-2}\le\frac1{2(2k-1)}
$$


   gives a constant-factor comparison between the actual rational error and the compact Christoffel extremal quantity.

3. The previously open adjacent analytic obligation is resolved:
   

$$
0<\varepsilon_{k+1}\le\frac14\varepsilon_k
   \qquad(k\ge64).
$$



4. The actual rational errors have the evaluated exponential rate
   

$$
\frac1{k^2(17+12\sqrt2)^{k-1}}
   \le\varepsilon_k
   \le
   \frac{42}{(17+12\sqrt2)^{k-1}}.
$$



5. Every adjacent primitive cross difference in that tail is positive and satisfies the explicit comparison (9.7).

### Conditional deduction

A proved bound


$$
\Delta_k=o(q_{k+1})
$$


on an infinite subset of the original indices would imply irrationality of $e+\pi$. A bounded $\Delta_k$ would suffice; balanced neighboring denominators are not additionally required.

### Finite arithmetic status

The $k=32$ content envelope is definitively refuted at that finite auxiliary index. Its large whole error is also a finite result. Neither conclusion is extended to an infinite domain.

### Exact remaining bottleneck

The analytic adjacent-order problem is no longer the obstacle. The remaining compact-family obligation is an all-prime arithmetic estimate strong enough to control


$$
\frac{\Delta_k}{q_{k+1}}
=
\frac{|\mathcal T|}
{t^kG_k|\mathcal K|}
\asymp \ell_k
$$


on one admissible infinite original-index set.

Equivalently, the actual primitive denominators must be controlled against the now evaluated approximation scale. In particular, the assigned sufficient condition


$$
q_k=o(11^{k-1})
$$


remains unproved.

Thus this continuation proves a genuine adjacent contraction and evaluates the ordinary-error exponential rate, while preserving the complete overlap, negative atom, finite endpoints, all paid divisions, and both primitive gcd payments. It does **not** yet prove whole-error decay or divergence on an infinite original domain, and it does **not** resolve the rationality or irrationality of $e+\pi$.
