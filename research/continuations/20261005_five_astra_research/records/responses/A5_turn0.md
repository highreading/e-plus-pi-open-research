> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5 report: an exact Gram bridge and a two-channel factorization of the primitive denominator

## Summary and status

I do **not** obtain an unconditional proof or disproof of the irrationality of $S=e+\pi$, nor an exclusion of a new positive proportional window.

I do obtain two exact arithmetic structural results for the specified factorial $B$-only center:

1. **An exact bridge to derivative-minor arithmetic.** The Gram center is obtained by replacing the last high derivative row with an explicitly constructed integer metric row. The resulting endpoint denominator contraction is exactly a positive weighted norm, multiplied by an identified cofactor-content quotient. This bridge does **not** identify the Gram center with the previously studied last-high-row center.

2. **An intrinsic, two-channel denominator factorization.** After the common two-column lift content has been removed, the final Gram gcd and the actual reduced denominator admit explicit factorizations in a saturated rank-two coefficient lattice. One factor measures primitive norm cancellation; the other measures cancellation of the remaining scalar denominator. Their product is the actual $q$, with no missing endpoint gcd.

These results apply at every finite normal index in their stated domain. On $b/n\to c$, $0<c<1/1000$, their eventual applicability and the full signed error remain dependent on the supplied **author-level, not independently reviewed** proportional analytic theorem.

The principal remaining obstruction is quantitative: neither of the two explicitly isolated denominator factors presently has a suitable growing-dimension arithmetic rate.

---

## 1. Inherited results used, without upgrading their status

The supplied sources support the following dependency ledger.

| Input | Status retained here | Use |
|---|---|---|
| `PROPORTIONAL_ACTUAL_CENTER_SIGNED_RATE.md` | Original author theorem; not independently reviewed | Eventual normality, nonzero coordinates, and the **complete signed** center error |
| `PROPORTIONAL_PRIMITIVE_CENTER_INTERFACE.md` | Original author connection; not independently reviewed | Identification of the actual lift and factorial metric; comparison with its intrinsic height identity |
| `GROWING_DEGREE_ARITHMETIC.md` | Author paper proof with reported formal checks; independent review pending | Exact Rodrigues rows and complete rational endpoint rows |
| `MULTIROW_REMAINDER_RESEARCH.md` | Author deduction | The relaxed high-row space, actual endpoint lift, and its injectivity |

I use only the supplied text. I have not accessed the listed local paths or primary-record URLs.

Fix an integer allocation


$$
b=b(n),\qquad \frac bn\longrightarrow c,\qquad 0<c<\frac1{1000},
$$


and an allowed depth


$$
1\le m=m(n)\le \left\lfloor\frac{b-1}{2}\right\rfloor.
$$


Thus $b\to\infty$; this is distinct from all excluded fixed-$b$ families.

Write the actual two-column lift as


$$
\Psi=[u,v],\qquad
B(P,Q)=Pu+Qv,
$$


where the reconstructed endpoint pair is $(P,Q)=(A(1),B(1))$. In particular,


$$
\mathbf e u=0,\qquad \mathbf e v=1,\qquad
\mathbf e=(1,\ldots,1).
$$



Set


$$
\ell=n+m+1,\qquad
\omega_j=(\ell)_j,\qquad
\Omega=\operatorname{diag}(\omega_0^2,\ldots,\omega_b^2).
$$


The center under discussion is exactly


$$
\mathfrak c_n=\frac{u^T\Omega v}{u^T\Omega u}.
\tag{1.1}
$$


No target-dependent metric is introduced.

The inherited analytic conclusion is


$$
\operatorname{sign}(\mathfrak c_n-S)=(-1)^{n+1},
\qquad
\log|\mathfrak c_n-S|
=-(2+c)\log(1+\sqrt2)\,n+o(n).
\tag{1.2}
$$


It includes the full exponential residual, both logarithmic sectors, and the coordinate-zero endpoint correction. All subsequent rate implications retain that dependency.

---

# Part I. An exact bridge from this Gram center to derivative-minor arithmetic

## 2. The relaxed space and its zero-endpoint line

For this section, take any finite index


$$
n\ge b\ge3,\qquad
1\le m\le \left\lfloor\frac{b-1}{2}\right\rfloor
$$


at which the actual relaxed endpoint map is an isomorphism.

Use the integer derivative rows from the growing-degree source:


$$
R_{lj}=E_{n+l,l+j-1},
\qquad 1\le l\le b-2,\quad 0\le j\le b.
$$


Let $R$ denote this $(b-2)\times(b+1)$ matrix. Removing nonzero row factors does not change its rational kernel.

The actual relaxed coefficient space is


$$
\mathcal W
=\ker_{\mathbb Q}\begin{bmatrix}R\\ \mathbf s\end{bmatrix},
\qquad
\mathbf s=\mathbf e+\mathbf t.
\tag{2.1}
$$


It has dimension two. Let $\mathbf x$ be its actual reconstructed $A$-endpoint row. The endpoint map is


$$
z\longmapsto (\mathbf xz,\mathbf ez).
\tag{2.2}
$$



Introduce the following notation to avoid confusing the lift column $u$ with a cumulative derivative row:


$$
\tau=n+1,\qquad f=\frac{2^n}{(n!)^2},
$$




$$
A=L_n(1),\qquad B=L_{n+1}(1),
$$


and let $\mathbf p,\mathbf r\in\mathbb Z^{b+1}$ be


$$
p_0=r_0=0,
$$




$$
p_j=\sum_{i=1}^j E_{n,i-1},
\qquad
r_j=\sum_{i=1}^j\frac{E_{n+1,i}}{n+1}.
\tag{2.3}
$$


The exact integrality of the latter divisions is one of the supplied Rodrigues identities.

Let $w_P,w_U,G$ have the source conventions:


$$
G=A w_U-Bw_P
=\frac{(-1)^n2^{2n+3}}{\tau}\ne0.
$$


Put


$$
T_P=T_0(L_n),\qquad T_U=T_0(L_{n+1}).
$$


The complete endpoint rows are


$$
\mathbf t=t_0\mathbf e+\frac{f}{\tau G}\mathbf L,
\qquad
\mathbf L=\tau B\,\mathbf p-2A\,\mathbf r,
\tag{2.4}
$$


where


$$
t_0=\frac{A T_U-BT_P}{G},
$$


and


$$
\mathbf x=x_0\mathbf e+
\frac{f}{\tau G}
\bigl(\tau w_U\mathbf p-2w_P\mathbf r\bigr),
\qquad
x_0=\frac{w_PT_U-w_UT_P}{G}.
\tag{2.5}
$$


These identities retain the full partial-exponential and second-kind terms.

Define the integer matrix


$$
K_0=
\begin{bmatrix}
R\\
\mathbf e\\
\mathbf L
\end{bmatrix}.
\tag{2.6}
$$


It has $b$ rows and $b+1$ columns. On $\mathbf ez=0$, equation (2.4) shows that


$$
\mathbf sz=0\quad\Longleftrightarrow\quad \mathbf Lz=0.
$$


Consequently,


$$
\ker_{\mathbb Q}K_0
=\mathcal W\cap\ker\mathbf e.
\tag{2.7}
$$


The endpoint isomorphism makes this a one-dimensional line, so $K_0$ has rank $b$.

Let


$$
z^{\rm raw}_j=(-1)^{b+j}\det(K_0\text{ with column }j\text{ deleted}),
$$




$$
\nu=\gcd_j|z^{\rm raw}_j|>0,
\qquad
z_0=\frac{z^{\rm raw}}{\nu}.
\tag{2.8}
$$


Then $z_0$ is a primitive integer generator of the zero-$B(1)$ line.

### New exact endpoint simplification

Set


$$
\xi=\mathbf xz_0.
$$


Then


$$
\boxed{\displaystyle
\xi=\frac fA\,\mathbf pz_0\ne0,
\qquad
u=\frac{z_0}{\xi}.}
\tag{2.9}
$$



**Proof.** Since $\mathbf ez_0=\mathbf Lz_0=0$,


$$
\mathbf rz_0=\frac{\tau B}{2A}\,\mathbf pz_0.
$$


Substitute this into (2.5):


$$
\begin{aligned}
\mathbf xz_0
&=\frac f{\tau G}
\left(\tau w_U-\frac{\tau B}{A}w_P\right)\mathbf pz_0\\
&=\frac fG\left(w_U-\frac BA w_P\right)\mathbf pz_0
=\frac fA\,\mathbf pz_0.
\end{aligned}
$$


Here $A\ne0$, as supplied by the positive transformed Legendre endpoints. If $\xi=0$, the nonzero vector $z_0$ would have both endpoints zero, contradicting the endpoint isomorphism. Normalization to endpoint $(1,0)$ proves the formula for $u$. ∎

In particular, the zero-endpoint direction can be constructed entirely from integer derivative data before introducing the partial-exponential and second-kind endpoint constants. This does **not** remove those constants from the second lift column or the full center.

---

## 3. The Gram row is not the omitted derivative row

Define


$$
T=z_0^T\Omega z_0\in\mathbb Z_{>0},
\qquad
\mathbf w=z_0^T\Omega\in\mathbb Z^{b+1}.
\tag{3.1}
$$


The new high block is


$$
H=
\begin{bmatrix}
R\\
\mathbf w
\end{bmatrix}.
\tag{3.2}
$$



This is the crucial distinction:

- the previously considered derivative-minor center uses the additional derivative row $R_{b-1}$;
- the specified Gram center instead uses the metric row $\mathbf w$.

There is no reason for these rows, or their endpoint quotients, to coincide.

Let


$$
z_*=v-\mathfrak c_n u.
$$


Using (1.1) and $u=z_0/\xi$,


$$
\mathbf wz_*=z_0^T\Omega(v-\mathfrak c_nu)=0.
$$


Also $z_*\in\mathcal W$, with


$$
\mathbf xz_*=-\mathfrak c_n,\qquad
\mathbf ez_*=1.
\tag{3.3}
$$


Thus the one-dimensional coefficient space cut out by $H$ and the matching row $\mathbf s$ has endpoint quotient


$$
\frac{X}{Y}=-\mathfrak c_n.
\tag{3.4}
$$


The minus sign is indispensable: $X/Y$ is the $A(1)/B(1)$ quotient, whereas the Gram center approximates $+S$.

---

## 4. Exact content accounting in the metric-row bridge

Let $\mu>0$ be the gcd of **all** maximal minors of $H$. This includes any common row content; it is not an endpoint gcd. Define


$$
\mathcal B(a,b)=\frac{\det[H;a;b]}{\mu}.
\tag{4.1}
$$


This is an integer-valued alternating form on integer rows.

Set


$$
\sigma=-\mathcal B(\mathbf e,\mathbf r),\qquad
\chi=-\mathcal B(\mathbf e,\mathbf p),\qquad
\kappa=\mathcal B(\mathbf r,\mathbf p).
\tag{4.2}
$$


All three are integers. Define the complete endpoint contractions


$$
D=\tau B\chi-2A\sigma,
$$




$$
Q=2w_P\sigma-\tau w_U\chi,
$$




$$
V=\sigma\mathcal A_n-\chi\mathcal B_n-\kappa,
\tag{4.3}
$$


where the last two calligraphic scalars are the supplied complete adjacent Rodrigues contractions:


$$
T_P=f\mathcal A_n,\qquad
T_U=\frac{2f}{\tau}\mathcal B_n.
$$



### Exact bridge theorem

On the finite normal domain above,


$$
\boxed{\displaystyle
D=-\frac{\nu T}{\mu}\ne0,}
\tag{4.4}
$$


and


$$
\boxed{\displaystyle
\mathfrak c_n=-\frac{Q+2fV}{D}.}
\tag{4.5}
$$



**Proof of the norm denominator.** From (4.2),


$$
D=-\mathcal B(\mathbf e,\mathbf L).
$$


Moving $\mathbf w$ past two rows makes no sign change, so


$$
\begin{aligned}
\mu\mathcal B(\mathbf e,\mathbf L)
&=\det[R;\mathbf w;\mathbf e;\mathbf L]\\
&=\det[R;\mathbf e;\mathbf L;\mathbf w]\\
&=z^{\rm raw}\cdot\mathbf w
=\nu z_0^T\Omega z_0=\nu T.
\end{aligned}
$$


This proves (4.4), including $\mu\mid\nu T$.

**Proof of the complete numerator.** The endpoint formulas (2.4)–(2.5) give


$$
Y=\mathcal B(\mathbf e+\mathbf t,\mathbf e)
=\frac f{\tau G}D.
$$


Writing


$$
\mathbf J=\tau w_U\mathbf p-2w_P\mathbf r,
$$


one has


$$
\mathcal B(\mathbf e,\mathbf J)=Q,\qquad
\mathcal B(\mathbf L,\mathbf J)=-2\tau G\kappa.
$$


Expansion yields


$$
X=\frac f{\tau G}
\left[x_0D+(1+t_0)Q-2f\kappa\right].
$$


Direct substitution of $x_0,t_0$ and the identity $G=Aw_U-Bw_P$ gives


$$
x_0D+t_0Q=2T_P\sigma-\tau T_U\chi.
$$


Hence


$$
X=\frac f{\tau G}(Q+2fV).
$$


Now use (3.4). ∎

If


$$
d_{\rm con}=\gcd(|\sigma|,|\chi|,|\kappa|),
$$


the three contractions can be divided by $d_{\rm con}$, exactly as in the source. Then


$$
D^*=-\frac{\nu T}{\mu d_{\rm con}},
\qquad
\mathfrak c_n=-\frac{Q^*+2fV^*}{D^*}.
\tag{4.6}
$$


In particular,


$$
\mu d_{\rm con}\mid \nu T.
$$


This identifies the high-row, cofactor, and contraction contents separately.

For any positive integer $\Lambda$ clearing the complete pair, put


$$
N=\Lambda(Q^*+2fV^*),\qquad Z=\Lambda D^*.
$$


The **actual** primitive center remains


$$
q_n=\frac{|Z|}{\gcd(|Z|,|N|)},\qquad
p_n=-\frac{\operatorname{sign}(Z)N}{\gcd(|Z|,|N|)}.
\tag{4.7}
$$


Neither $\mu$, $\nu$, nor $d_{\rm con}$ is substituted for this final gcd.

This gives a valid bridge for applying the source’s complete valuation gate to the Gram center—but with the new metric-dependent minors. Fixed-$b$ seed transfers do not transfer to these growing matrices.

---

# Part II. Intrinsic arithmetic after all common lift content is removed

## 5. A saturated coefficient lattice and an adapted basis

The following theorem is finite-dimensional integer algebra. Its proof does not require any asymptotic theorem.

Let


$$
\mathscr L=\mathcal W\cap\mathbb Z^{b+1}.
$$


It is a saturated rank-two lattice. The endpoint sum has image


$$
\mathbf e(\mathscr L)=h\mathbb Z
$$


for a unique integer $h>0$.

Choose $z_1\in\mathscr L$ with


$$
\mathbf ez_1=h.
$$


Then


$$
\mathscr L=\mathbb Zz_0\oplus\mathbb Zz_1.
\tag{5.1}
$$


Indeed, subtracting a suitable multiple of $z_1$ makes the endpoint sum zero, and the integer zero-sum line is precisely $\mathbb Zz_0$.

Put


$$
\xi=\mathbf xz_0,\qquad \eta=\mathbf xz_1.
$$


Let $D_0$ be the least positive integer clearing both numbers:


$$
\xi=\frac a{D_0},\qquad
\eta=\frac b{D_0},
$$


where


$$
a\ne0,\qquad \gcd(D_0,a,b)=1.
\tag{5.2}
$$


Here the integer $b$ in (5.2) is an endpoint numerator; to avoid ambiguity below, denote it by $b_{\rm end}$.

Define


$$
\gamma=\gcd(h,a,b_{\rm end}),
$$




$$
k=\frac{hD_0}{\gamma}>0,\qquad
a'=\frac a\gamma,\qquad b'=\frac{b_{\rm end}}\gamma.
\tag{5.3}
$$



### Exact least-denominator formula

The actual least common denominator of the two-column $B$-lift is


$$
\boxed{\displaystyle d_B=\frac{h|a|}{\gamma}.}
\tag{5.4}
$$


Its primitive integer numerator matrix is


$$
\boxed{\displaystyle
N_B=\operatorname{sign}(a)
\begin{bmatrix}
kz_0 & a'z_1-b'z_0
\end{bmatrix}.}
\tag{5.5}
$$



**Proof.** In the basis $[z_0,z_1]$, the endpoint matrix is


$$
E=
\begin{pmatrix}
a/D_0&b_{\rm end}/D_0\\
0&h
\end{pmatrix}.
$$


Thus


$$
\Psi=[z_0,z_1]E^{-1}
=\frac1{ha}[z_0,z_1]
\begin{pmatrix}
hD_0&-b_{\rm end}\\
0&a
\end{pmatrix}.
\tag{5.6}
$$


Because $[z_0,z_1]$ is a basis of a saturated lattice, it has an integer left inverse. Therefore multiplication by this basis preserves the gcd of all entries of an integer two-column coefficient matrix.

The content of the displayed $2\times2$ matrix is


$$
\gcd(hD_0,a,b_{\rm end}).
$$


Condition (5.2) implies


$$
\gcd(hD_0,a,b_{\rm end})=\gcd(h,a,b_{\rm end})=\gamma:
$$


at a prime dividing both $a$ and $b_{\rm end}$, $D_0$ is a unit. Dividing by this content proves (5.4)–(5.5), and the numerator matrix in (5.5) has joint content one. ∎

This identifies $d_B$ through the actual coefficient lattice and endpoint map—not through a chosen row clearer.

---

## 6. Exact formulas for $A_B,H_B,C_B$

Set


$$
T=z_0^T\Omega z_0,\qquad
V_0=z_0^T\Omega z_1,\qquad
U_0=z_1^T\Omega z_1.
\tag{6.1}
$$


These are integers, with


$$
T>0,\qquad TU_0-V_0^2>0.
$$


From (5.5),


$$
\boxed{
A_B=k^2T,
\qquad
H_B=k(a'V_0-b'T),
}
\tag{6.2}
$$


and


$$
\boxed{
C_B=a'^2U_0-2a'b'V_0+b'^2T.
}
\tag{6.3}
$$



In particular, even after all common lift content has been removed, the first lift column has coefficient content $k$. Therefore


$$
k\mid g_B.
$$


Primitivity of the two-column matrix does not remove this forced column contribution to the final Gram gcd.

The complete center is


$$
\mathfrak c_n=\frac{a'V_0-b'T}{kT}
=\frac{aV_0-b_{\rm end}T}{hD_0T}.
\tag{6.4}
$$



---

## 7. Two-channel factorization of the final gcd and actual $q$

Define


$$
\delta=\gcd(T,|V_0|)>0,\qquad
t=\frac T\delta,\qquad v_0=\frac{V_0}\delta,
$$


so that


$$
\gcd(t,|v_0|)=1.
$$


Next put


$$
\alpha=\gcd(t,|a'|),
\qquad
r=\frac{a'v_0-b't}{\alpha}\in\mathbb Z.
\tag{7.1}
$$


Then


$$
\gcd\left(\frac t\alpha,|r|\right)=1.
\tag{7.2}
$$



### Intrinsic Gram-content theorem

The final Gram gcd and primitive endpoint pair are exactly


$$
\boxed{\displaystyle
g_B=k\,\delta\,\alpha\,\gcd(k,|r|),}
\tag{7.3}
$$




$$
\boxed{\displaystyle
q_n=\frac t\alpha\;\frac{k}{\gcd(k,|r|)},\qquad
p_n=\frac r{\gcd(k,|r|)}.}
\tag{7.4}
$$


In particular $q_n>0$, $\gcd(p_n,q_n)=1$, and $p_n/q_n=\mathfrak c_n$.

**Proof.** By (6.2),


$$
g_B=k\gcd(kT,|a'V_0-b'T|).
$$


Now


$$
T=\delta t,\qquad a'V_0-b'T=\delta\alpha r.
$$


Because $t=\alpha(t/\alpha)$, equation (7.2) gives


$$
\begin{aligned}
\gcd(kT,|a'V_0-b'T|)
&=\delta\alpha
 \gcd\left(k\frac t\alpha,|r|\right)\\
&=\delta\alpha\gcd(k,|r|).
\end{aligned}
$$


This proves (7.3); division of $A_B,H_B$ by that gcd proves (7.4). ∎

The zero-numerator case is included: if $r=0$, (7.2) forces $t/\alpha=1$, and (7.4) gives $p_n=0,q_n=1$. The inherited proportional center theorem excludes this case eventually, since $\mathfrak c_n\to e+\pi>0$.

### Why the factorization is intrinsic

The choice of $z_1$ is only up to


$$
z_1\longmapsto z_1+s z_0,\qquad s\in\mathbb Z.
$$


Under this change,


$$
V_0\mapsto V_0+sT,\qquad
b_{\rm end}\mapsto b_{\rm end}+sa.
$$


Consequently $\delta,t,\gamma,k,\alpha,r$ are unchanged. Reversing the sign of $z_0$ also preserves the factors in (7.4).

Thus (7.4) is not an artefact of an arbitrary lattice basis.

---

## 8. A prime-by-prime survival law valid in growing dimension

For every prime $p$, with $v_p(0)=+\infty$, formula (7.4) gives


$$
\boxed{\displaystyle
v_p(q_n)
=
\max\{0,v_p(t)-v_p(a')\}
+
\max\{0,v_p(k)-v_p(r)\}.}
\tag{8.1}
$$



This formula applies to the actual reduced $q_n$, not a lift denominator.

There is a useful automatic-survival consequence. If


$$
v_p(t)>v_p(a'),
$$


then $p\mid t/\alpha$, so (7.2) forces $r$ to be a $p$-unit. Therefore


$$
\boxed{\displaystyle
v_p(q_n)=v_p(t)-v_p(a')+v_p(k).}
\tag{8.2}
$$


Thus a prime surviving the primitive norm channel cannot simultaneously cancel the scalar channel.

No fixed-prime seed transfer, fixed matrix dimension, or limiting residue argument is used in (8.1)–(8.2).

The corresponding exact global bounds are


$$
\frac{t}{\alpha}\le q_n
\le k\frac{t}{\alpha},
\tag{8.3}
$$




$$
q_n\ge\frac{t}{|a'|},
\tag{8.4}
$$


and, more importantly, the full product identity


$$
q_n=
\underbrace{\frac{t}{\gcd(t,|a'|)}}_{\text{primitive norm channel}}
\underbrace{\frac{k}{\gcd(k,|r|)}}_{\text{scalar cancellation channel}}.
\tag{8.5}
$$



---

# Part III. What this changes—and what it does not prove

## 9. Comparison with the inherited intrinsic height budget

The supplied intrinsic height theorem states


$$
\log A_B
=2\log d_B+2(n+b)\log n+O(n).
\tag{9.1}
$$


The exact new identities give


$$
\log A_B=2\log k+\log T
\tag{9.2}
$$


and


$$
\log g_B
=\log k+\log\delta+\log\alpha
+\log\gcd(k,|r|).
\tag{9.3}
$$


Therefore


$$
\boxed{\displaystyle
\log q_n
=
\log\frac{t}{\alpha}
+
\log\frac{k}{\gcd(k,|r|)}.}
\tag{9.4}
$$



This makes a distinction missing from a single undifferentiated “large gcd” requirement:

- $k\delta\alpha$ is forced content in the final Gram contraction;
- only the additional factor $\gcd(k,|r|)$ represents the remaining scalar cancellation;
- a separate norm denominator $t/\alpha$ survives regardless of that scalar cancellation.

The decomposition is compatible with the exact endpoint simplification


$$
\frac a{D_0}
=\xi=\frac{2^n}{(n!)^2A}\,\mathbf pz_0.
\tag{9.5}
$$


It therefore connects the intrinsic lattice formula to the derivative arithmetic, rather than renaming an unspecified rational inverse.

Nevertheless, (9.5) does not control the reduced numerator $\mathbf pz_0$, and positivity of $T$ does not control $\delta=\gcd(T,V_0)$. These are genuine arithmetic unknowns.

---

## 10. Exact rate criteria, with the complete signed error retained

Write


$$
\tau_c=(2+c)\log(1+\sqrt2),
$$


and define the two nonnegative intrinsic budgets


$$
B_1(n)=\log\frac{t}{\alpha},
\qquad
B_2(n)=\log\frac{k}{\gcd(k,|r|)}.
$$


Then


$$
\log q_n=B_1(n)+B_2(n)
\tag{10.1}
$$


exactly.

Combining this with the inherited complete error gives


$$
\boxed{\displaystyle
\log|q_nS-p_n|
=B_1(n)+B_2(n)-\tau_c n+o(n).}
\tag{10.2}
$$


Moreover $q_nS-p_n\ne0$ eventually, since the complete signed error is eventually nonzero.

Hence:

- A proved bound
  

$$
\limsup_{n\to\infty}\frac{B_1(n)+B_2(n)}n<\tau_c
$$


  would give shrinking nonzero primitive integer forms and prove irrationality.

- A proved bound
  

$$
\liminf_{n\to\infty}\frac{B_1(n)+B_2(n)}n>\tau_c
$$


  would exclude this proportional Gram-center route.

- A sufficient norm-channel obstruction is
  

$$
\liminf_{n\to\infty}
  \frac{\log t-\log|a'|}{n}>\tau_c,
$$


  by (8.4).

None of these quantitative inequalities has been established here.

### Exact obstruction to completing the route

There are now two sharply localized gaps:

1. **Primitive norm content:** control
   

$$
\frac{T/\gcd(T,V_0)}
        {\gcd(T/\gcd(T,V_0),\,|a'|)}.
$$


   Large weighted norm alone does not imply a large reduced norm denominator.

2. **Scalar congruence cancellation:** control
   

$$
\gcd(k,r)
$$


   at the required aggregate depth for growing $b$.

The metric-row bridge does not remove these gaps. It permits complete derivative-minor valuation arguments, but the relevant minors now contain the growing, arithmetically defined row $\mathbf w=\Omega z_0$. Fixed-$b$ modular seeds cannot be applied to them without a new uniform theorem.

---

## 11. Final deliverable

### (1) New result and proof status

**Proved here as exact finite algebra, conditional only on the stated actual endpoint reconstruction and finite normality domain:**

- the integer construction of the primitive zero-endpoint direction $z_0$;
- the endpoint simplification
  

$$
\xi=\frac{2^n}{(n!)^2A}\,\mathbf pz_0;
$$


- the metric-row derivative-minor bridge, including
  

$$
D=-\nu T/\mu\ne0
$$


  and the complete signed endpoint quotient;
- the exact least lift denominator $d_B$, actual contractions $A_B,H_B,C_B$, and final-gcd factorization
  

$$
g_B=k\delta\alpha\gcd(k,|r|);
$$


- the actual primitive denominator factorization
  

$$
q_n=\frac t\alpha\,\frac{k}{\gcd(k,|r|)}
$$


  and its prime-by-prime survival law.

These are new author-level deductions in this report, not independently audited results. Their eventual application on $b/n\to c$ retains the supplied proportional theorem’s author/dependency status.

### (2) Exact remaining bottleneck

Obtain an asymptotic arithmetic estimate for the **sum of the two nonnegative budgets**


$$
\log\frac{t}{\gcd(t,|a'|)}
+
\log\frac{k}{\gcd(k,|r|)}
$$


relative to


$$
(2+c)\log(1+\sqrt2)\,n.
$$


Neither a favorable upper rate nor an exclusionary lower rate has been proved. Consequently the arithmetic nature of $e+\pi$ remains unresolved.

### (3) Computation request

**None is required for the structural lemmas proved above.** I do not request a finite scan as a substitute for the missing growing-dimension valuation theorem. Any later exact computation should report the fully reduced pair from (7.4) and independently compare it with (4.7); agreement at finitely many indices would be a normalization check only, not evidence sufficient to establish either asymptotic rate.
