> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An unavoidable factorial height in the actual primitive mixed invariant

## Abstract and status

The rationality or irrationality of $e+\pi$ remains unresolved.

This report addresses the primitive-normalization question left open in turn20. Its main result is a **uniform lower bound**, not the hoped-for exponential upper bound.

Let


$$
d_{\rm mix}
=\gcd\!\left(\mathfrak D_{s;p},
             \mathfrak A_{p,N},\mathfrak B_{p,N}\right),
$$


and let


$$
A_{\rm mix}=\frac{\mathfrak A_{p,N}}{d_{\rm mix}},\qquad
B_{\rm mix}=\frac{\mathfrak B_{p,N}}{d_{\rm mix}},\qquad
D_{\rm mix}=\frac{\mathfrak D_{s;p}}{d_{\rm mix}}
$$


be the actual simultaneous primitive normalization. All Gaussian divisions have already been performed in these integers.

For every original admissible pair $(N,p)$, the new theorem proves


$$
\boxed{
\max\{|A_{\rm mix}|,|B_{\rm mix}|\}
\ge N^{(p-1)/2}e^{-16N},
}
\tag{A}
$$


and


$$
\boxed{
D_{\rm mix}\ge N^{(p-1)/2}e^{-28N}.
}
\tag{B}
$$


Consequently, the actual all-prime common divisor satisfies


$$
\boxed{
d_{\rm mix}
\le \mathfrak D_{s;p}\,N^{-(p-1)/2}e^{28N}.
}
\tag{C}
$$



These are constraints on the **actual numerical gcd and clearer**, not on formal coefficient contents. They follow from:

- the complete source and endpoint columns;
- the source-specific identity
  

$$
\Phi_j-e\Theta_j=O(1/j),
$$


  derived from their finite exponential moments;
- the actual divided Gaussian target, whose height is exponential;
- two finite Hermite approximants, at the admissible indices $(p-1)/2$ and $(p+1)/2$;
- ordinary integer separation.

Thus the proposed exponential primitive-height mechanism cannot work on any unbounded family of remaining admissible pairs. This is a pointwise, uniform obstruction. It does **not** assert that the remaining collision set is nonempty at infinitely many original indices.

The result does not bound the surviving depth mass by $O(N)$. The separate aggregate obligation remains: the complete surviving exponents must be captured by one fixed-$N$ integer, or by an aggregate with a proved total logarithmic height bill $O(N)$. A concrete, weaker-than-third-depth-avoidance continuation lemma is formulated below, with a genuine fixed-$N$ aggregate payment.

No original-sized computation, prime scan, old certificate, or new numerical computation is required.

---

# 1. Original objects and exact scope

## 1.1 Original index domain and divided Gaussian data

Throughout,


$$
\boxed{
N=9^{18+32u}=3^{36+64u},\qquad u\in\mathbb Z_{\ge0},
}
$$


and


$$
n=2N,\qquad m=N-3,\qquad \ell=2N-6.
$$


The physical terminal remains $n=2N$.

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


where


$$
C_0=1,\qquad C_1=2t-1,\qquad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$



The actual Gaussian normalization is


$$
g_B=\gcd(b_{N-1},b_N)>0,
$$




$$
\alpha=\frac{b_{N-1}}{g_B},\qquad
\beta=\frac{b_N}{g_B},\qquad
\delta=\frac{a_Nb_{N-1}-a_{N-1}b_N}{g_B}.
$$


Thus


$$
F=\alpha C_N-\beta C_{N-1},\qquad
F(\pm i)=\delta,\qquad \gcd(\alpha,\beta)=1.
$$



Every source valuation used below is a valuation **after this actual division**. No undivided Gaussian square column is substituted.

For an integer polynomial $H$, put


$$
\eta(H)=\sum_j j![z^j]H(1-z),\qquad
E(H)=\sum_j(-1)^j j![t^j]H(t).
$$


Define


$$
\mathcal H=t(1-t)(1+t^2)^2,\qquad K=\mathcal H C_m^2,
$$




$$
U=-\eta(K),\qquad V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
$$



The retained original content and primitive source normalization are


$$
\operatorname{cont}(W_{\rm raw})=g_B^2c,
$$




$$
\tau=U/c,\qquad \nu=V/c,\qquad
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2,
$$


with


$$
U>0,\qquad V>0,\qquad M>0.
$$



The supplied divided Gaussian height bound is


$$
H_G:=\alpha^2+\beta^2+\delta^2
<\frac{5^{4N}}{g_B^2}.
\tag{1.1}
$$



## 1.2 Actual reduced $K$-arc and complete all-prime credit

Let


$$
L(x)=(x-1)(x-9)(x-25),
$$




$$
A_K(x)=13x^3-455x^2+3502x-5850.
$$


At $x=\ell^2$, retain the actual lowest-term reduction


$$
R_K=\frac{A_K(\ell^2)}{30L(\ell^2)}
=\frac{a_K}{d_K},
$$


where


$$
g_{\rm arc}
=90\,5^{\varepsilon_5}19^{\varepsilon_{19}}31^{\varepsilon_{31}},
$$




$$
\varepsilon_5=\mathbf1_{u\equiv1\pmod5},\qquad
\varepsilon_{19}=\mathbf1_{u\equiv3\pmod9},\qquad
\varepsilon_{31}=\mathbf1_{u\equiv5,7\pmod{15}},
$$


and


$$
a_K=A_K(\ell^2)/g_{\rm arc},\qquad
d_K=30L(\ell^2)/g_{\rm arc}.
$$


In particular,


$$
\gcd(a_K,d_K)=1.
$$



Put


$$
E_K=E(K),\qquad y_K=d_KE_K-a_K,
$$


so


$$
\gcd(d_K,y_K)=1.
$$



The intrinsic factors remain


$$
\gamma=\gcd(\tau,y_K),\qquad
b^\circ=\gcd(\gamma,a_K),\qquad
r^\circ=\gamma/b^\circ.
$$



For every prime $p$, define


$$
c_p=\min\{v_p(U),v_p(V)\},\qquad
t_p=v_p(U)-c_p,
$$




$$
z_p=v_p(y_K),\qquad
b_p=v_p(b^\circ),\qquad
h_p=v_p(Q_{N-1}^{\mathrm H}Q_N^{\mathrm H}).
$$


The complete credit is


$$
\boxed{
H_p=h_p+2b_p+2(z_p-t_p)_+.
}
\tag{1.2}
$$


Thus the actual turn15 product multiplier has


$$
\boxed{
v_p(\kappa_N^{\rm prod})=[c_p-H_p]_+.
}
\tag{1.3}
$$



No Hermite credit is moved from $N-1,N$ to a residual or anchoring index.

---

# 2. Complete finite columns, forcing, and the remaining branch

## 2.1 Both original forced systems

For exactly $0\le j\le n$,


$$
\Theta_0=\Phi_0=0,\qquad \Theta_1=\Phi_1=1.
$$


For exactly $1\le j\le n-1$,


$$
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2,
$$




$$
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j.
\tag{2.1}
$$



The full finite affine matrices are


$$
\begin{pmatrix}\Theta_{j+1}\\\Theta_j\\1\end{pmatrix}
=
\begin{pmatrix}-4j&1&2\\1&0&0\\0&0&1\end{pmatrix}
\begin{pmatrix}\Theta_j\\\Theta_{j-1}\\1\end{pmatrix},
$$




$$
\begin{pmatrix}\Phi_{j+1}\\\Phi_j\\(-1)^{j+1}\end{pmatrix}
=
\begin{pmatrix}-4j&1&2\\1&0&0\\0&0&-1\end{pmatrix}
\begin{pmatrix}\Phi_j\\\Phi_{j-1}\\(-1)^j\end{pmatrix}.
\tag{2.2}
$$



Both forcing coordinates are retained.

## 2.2 All four corrected constants

At $x=\ell^2$, let


$$
\begin{aligned}
\mathcal P(x)&=-8x^3-1116x^2-8150x+151,\\
\mathcal Q(x)&=76x^2+2408x+5637,\\
\mathcal F(x)&=4x^2+492x+5463,\\
\mathcal G(x)&=4x^2+556x-3325.
\end{aligned}
$$


Define


$$
\mathscr A=2\ell((2\ell+1)\mathcal Q-\mathcal P),
\qquad
\mathscr B=-2\ell\mathcal Q,
$$




$$
\mathscr C_U=\mathcal F-\mathcal P+2\ell\mathcal Q,
$$




$$
\mathscr C_E=\mathcal G+\mathcal P-2(\ell+1)\mathcal Q.
$$


The complete centered $K$-columns are


$$
16U=\mathscr C_U-\mathscr A\Theta_\ell-\mathscr B\Theta_{\ell-1},
$$




$$
16E_K=\mathscr C_E+\mathscr A\Phi_\ell+\mathscr B\Phi_{\ell-1}.
\tag{2.3}
$$



At the physical terminal,


$$
V=C_V-P\Theta_n-Q\Theta_{n-1},
$$




$$
E_F=C_F^E-P\Phi_n-Q\Phi_{n-1},
\tag{2.4}
$$


where


$$
P=n\alpha^2+(n-2)\beta^2,
$$




$$
Q=4(n-1)(n-2)\beta^2-2(n-1)\alpha\beta,
$$




$$
\boxed{
C_V=\alpha^2+(2n-3)\beta^2-\delta^2,
}
$$




$$
\boxed{
C_F^E=\alpha^2+(5-2n)\beta^2+4\alpha\beta.
}
\tag{2.5}
$$



Neither $-\delta^2$ nor $4\alpha\beta$ is omitted.

## 2.3 Exact six-step transport

Let


$$
T_j=\begin{pmatrix}-4j&1\\1&0\end{pmatrix},
\qquad
T=T_{\ell+5}\cdots T_\ell.
$$


Starting from $f_0=g_0=0$, use exactly the six updates


$$
f_{j+1}=T_{\ell+j}f_j+\binom20,
$$




$$
g_{j+1}=T_{\ell+j}g_j+\binom{2(-1)^j}{0},
\qquad 0\le j\le5.
$$


Then


$$
(\Pi,\Omega)=(P,Q)T,
$$




$$
C^{\rm s}=C_V-(P,Q)f_6,\qquad
C^{\rm e}=C_F^E-(P,Q)g_6.
$$


Thus


$$
V=C^{\rm s}-\Pi\Theta_\ell-\Omega\Theta_{\ell-1},
$$




$$
E_F=C^{\rm e}-\Pi\Phi_\ell-\Omega\Phi_{\ell-1}.
\tag{2.6}
$$



The largest original recurrence step remains


$$
\ell+5=n-1.
$$



Set


$$
\Delta=\mathscr A\Omega-\mathscr B\Pi<0,
$$




$$
\mathscr I_1=\Pi\mathscr C_U-\mathscr A C^{\rm s},\qquad
\mathscr I_2=\Omega\mathscr C_U-\mathscr B C^{\rm s},
$$




$$
J_N^{\rm aff}=\gcd(\mathscr I_1,\mathscr I_2)>0.
$$


The supplied bounds are


$$
|\Delta|,\ J_N^{\rm aff}
<
10^{10}(2N)^{15}\frac{5^{4N}}{g_B^2}.
\tag{2.7}
$$



We also use the supplied safe coefficient bounds


$$
|\mathscr A|,|\mathscr B|,|\mathscr C_U|,|\mathscr C_E|
<10^5n^7,
$$




$$
|\Pi|,|\Omega|,|C^{\rm s}|,|C^{\rm e}|
<10^5n^8H_G.
\tag{2.8}
$$


These immediately imply


$$
|\mathscr I_2|<2\cdot10^{10}n^{15}H_G.
\tag{2.9}
$$



The finite transports, determinant sign, coefficient bounds, forcing determinant, charts, and turn15 all-prime credit are reused at their supplied scopes. This report does not describe the pending different review of turn20 as completed.

## 2.4 The actual remaining branch

We continue


$$
\mathcal S_N=
\left\{
\begin{array}{l|l}
p&
N<p<2N,\quad p\nmid L(\ell^2),\\
&d_{p,N}^{\rm block}=p^2,\quad
v_p(\Delta)\le v_p(J_N^{\rm aff})
\end{array}
\right\}.
\tag{2.10}
$$


In particular,


$$
p^2\mid U,\qquad p^2\mid V.
$$



Write


$$
r=n-p,\qquad s=r-6=\ell-p,\qquad k=\frac{p+1}{2}.
$$


The retained finite-boundary calculation gives


$$
\boxed{
13\le r<N,\quad r\text{ odd},\quad
s\ge7,\quad s\text{ odd},\quad k\le N-6.
}
\tag{2.11}
$$


Also,


$$
p\nmid d_K.
$$



Define


$$
B_p=(H_p-2)_+,\qquad
e_p=[c_p-2-B_p]_+.
\tag{2.12}
$$


Then


$$
[c_p-H_p]_+=[2-H_p]_++e_p.
\tag{2.13}
$$


The first two layers are already paid:


$$
\sum_{p\in\mathcal S_N}[2-H_p]_+\log p
\le4N\log2.
\tag{2.14}
$$



---

# 3. The reused mixed invariant and its actual normalization

## 3.1 Residual-relative states and complete Hermite seed

For $0\le j\le r$, put


$$
x_j=\Theta_{p+j}-\Theta_j,\qquad
y_j=\Phi_{p+j}+\Phi_j.
$$


Their complete recurrences are


$$
x_{j+1}+4(p+j)x_j-x_{j-1}=-4p\Theta_j,
$$




$$
y_{j+1}+4(p+j)y_j-y_{j-1}=4p\Phi_j,
\qquad 1\le j\le r-1.
\tag{3.1}
$$



Define


$$
\mathfrak D_{j;p}=x_jy_{j-1}-x_{j-1}y_j.
$$


With


$$
\mathfrak M_{j;p}
=-\bigl(\Theta_j\Phi_{p+j}+\Phi_j\Theta_{p+j}\bigr),
$$


the retained exact evolution is


$$
\mathfrak D_{j+1;p}
=-\mathfrak D_{j;p}+4p\mathfrak M_{j;p}.
\tag{3.2}
$$



The Hermite integers have


$$
P_0^{\mathrm H}=Q_0^{\mathrm H}=1,\qquad
P_1^{\mathrm H}=3,\quad Q_1^{\mathrm H}=1,
$$




$$
Z_{a+1}=(4a+2)Z_a+Z_{a-1},
\qquad 1\le a\le N-1.
\tag{3.3}
$$


Let $\chi=2k!$. Both pairs of actual defects are retained:


$$
\sigma_0^+
=\frac{\Theta_p-\chi Q_{k-1}^{\mathrm H}}p,\qquad
\sigma_1^+
=\frac{\Theta_{p-1}+1+\chi Q_k^{\mathrm H}}p,
$$




$$
\sigma_0^-
=\frac{\Phi_p-\chi P_{k-1}^{\mathrm H}}p,\qquad
\sigma_1^-
=\frac{\Phi_{p-1}-1+\chi P_k^{\mathrm H}}p.
\tag{3.4}
$$


These are integers by the supplied universal base congruences.

Put


$$
\begin{aligned}
\Lambda_\sigma={}&
P_k^{\mathrm H}\sigma_0^+
+P_{k-1}^{\mathrm H}\sigma_1^+
-Q_k^{\mathrm H}\sigma_0^-
-Q_{k-1}^{\mathrm H}\sigma_1^-,\\
\Xi_\sigma={}&
\sigma_1^+\sigma_0^--\sigma_0^+\sigma_1^-.
\end{aligned}
$$


If


$$
\mathfrak f_{1;p}=0,\qquad
\mathfrak f_{j+1;p}=\mathfrak M_{j;p}-\mathfrak f_{j;p},
$$


then, because $s$ is odd,


$$
\boxed{
\mathfrak D_{s;p}
=
2(-1)^{k-1}\chi^2
+p\chi\Lambda_\sigma+p^2\Xi_\sigma
+4p\mathfrak f_{s;p}.
}
\tag{3.5}
$$



The reused conclusions are


$$
p\nmid\mathfrak D_{s;p},
\tag{3.6}
$$


and


$$
\boxed{
16p\,3^{\ell+s-6}(\ell-2)!(s-2)!
<
\mathfrak D_{s;p}
<
8p\,6^{\ell+s-4}(\ell-2)!(s-2)!.
}
\tag{3.7}
$$



In particular, $\mathfrak D_{s;p}>0$.

The binding normalization mismatch remains


$$
v_p(\mathfrak D_{s;p})=0,\qquad
v_p((\ell-2)!(s-2)!)=1.
\tag{3.8}
$$


No division by this factorial product will be made.

## 3.2 Actual mixed minors

Use column vectors


$$
\mathbf t_j=\binom{\Theta_j}{\Theta_{j-1}},
\qquad
\mathbf f_j=\binom{\Phi_j}{\Phi_{j-1}},
$$


and define


$$
\mathsf M_c=
\begin{pmatrix}
\mathscr A&\mathscr B\\
\Pi&\Omega
\end{pmatrix},
\qquad
\mathbf C=\binom{\mathscr C_U}{C^{\rm s}},
\qquad
\mathbf u=\binom{16U}{V}.
$$


Then


$$
\mathbf u=\mathbf C-\mathsf M_c\mathbf t_\ell.
$$



The actual residual source and relative endpoint columns are


$$
\mathbf R=\mathbf C-\mathsf M_c\mathbf t_s,
$$




$$
\mathbf E=
\binom{
16E_K-\mathscr C_E+\mathscr A\Phi_s+\mathscr B\Phi_{s-1}
}{
C^{\rm e}-E_F+\Pi\Phi_s+\Omega\Phi_{s-1}
}.
\tag{3.9}
$$


The complete endpoint constants and forcing give exactly


$$
\mathbf E=\mathsf M_c(\mathbf f_\ell+\mathbf f_s).
\tag{3.10}
$$



Define


$$
\mathfrak A_{p,N}=\det(\mathbf R,\mathbf u),
\qquad
\mathfrak B_{p,N}=\det(\mathbf u,\mathbf E).
\tag{3.11}
$$


Thus


$$
\mathfrak A_{p,N}=R_1V-R_2\,16U,
$$




$$
\mathfrak B_{p,N}=16U\,E_2-VE_1.
$$



Here “raw mixed minor” means **before mixed primitive normalization**. It does not mean before Gaussian division.

The retained complete additive identity is


$$
\boxed{
\mathfrak B_{p,N}
=R_1E_2-R_2E_1-\Delta\mathfrak D_{s;p}.
}
\tag{3.12}
$$


Through (3.5), this contains both Hermite defect pairs and the entire mixed forcing return.

## 3.3 Actual least simultaneous mixed clearer

Let


$$
d_{\rm mix}
=\gcd(\mathfrak D_{s;p},\mathfrak A_{p,N},\mathfrak B_{p,N})>0,
$$




$$
A_{\rm mix}=\mathfrak A_{p,N}/d_{\rm mix},\qquad
B_{\rm mix}=\mathfrak B_{p,N}/d_{\rm mix},
$$




$$
D_{\rm mix}=\mathfrak D_{s;p}/d_{\rm mix}.
\tag{3.13}
$$


Then


$$
\frac{\mathfrak A_{p,N}}{\mathfrak D_{s;p}}
=\frac{A_{\rm mix}}{D_{\rm mix}},\qquad
\frac{\mathfrak B_{p,N}}{\mathfrak D_{s;p}}
=\frac{B_{\rm mix}}{D_{\rm mix}},
$$


and


$$
\gcd(A_{\rm mix},B_{\rm mix},D_{\rm mix})=1.
$$


This is the least simultaneous clearer of these two auxiliary rational numbers.

It is not the original two-arc clearer $D$.

By (3.6),


$$
\boxed{
v_p(d_{\rm mix})=v_p(D_{\rm mix})=0
\quad(p\in\mathcal S_N).
}
\tag{3.14}
$$



## 3.4 Reused charts and numerical bounds

At every $p\in\mathcal S_N$, the supplied corrected-column argument gives


$$
\min\{v_p(R_1),v_p(E_1)\}=0.
$$


Choose


$$
\zeta_{p,N}=
\begin{cases}
\mathfrak A_{p,N},&p\nmid R_1,\\
\mathfrak B_{p,N},&p\mid R_1.
\end{cases}
$$


Then, including determinant-critical primes,


$$
\boxed{
c_p-2=
\min\left\{
v_p(16U/p^2),v_p(\zeta_{p,N}/p^2)
\right\}.
}
\tag{3.15}
$$



For


$$
\vartheta_j=(-1)^{j-1}\Theta_j,\qquad
\varphi_j=(-1)^{j-1}\Phi_j,
$$


the reused bounds are


$$
0<\vartheta_j\le\varphi_j,
$$




$$
2\,3^{j-2}(j-1)!
\le\vartheta_j\le\varphi_j
\le6^{j-1}(j-1)!,\qquad j\ge2.
\tag{3.16}
$$


These magnitudes are increasing.

Let


$$
F_j^*=1+\vartheta_j+\varphi_j+\vartheta_{j-1}+\varphi_{j-1}.
$$


The retained mixed-minor upper bound is


$$
\boxed{
|\mathfrak A_{p,N}|,\ |\mathfrak B_{p,N}|
<
10^{12}n^{16}H_GF_s^*F_\ell^*.
}
\tag{3.17}
$$



The new work starts with the arithmetic consequences of these actual columns, not with another determinant or chart proof.

---

# 4. New theorem: factorial primitive height

## Theorem 4.1 — Uniform obstruction to exponential mixed normalization

Let $N$ be an original index and $p\in\mathcal S_N$. Put


$$
a=\frac{p-1}{2},\qquad k=a+1,
$$


and


$$
H_{\rm num}=\max\{|A_{\rm mix}|,|B_{\rm mix}|\}.
$$


Then


$$
\boxed{
H_{\rm num}\ge N^a e^{-16N},
}
\tag{4.1}
$$




$$
\boxed{
D_{\rm mix}\ge N^a e^{-28N}.
}
\tag{4.2}
$$



Equivalently,


$$
\boxed{
\gcd(\mathfrak D_{s;p},\mathfrak A_{p,N},\mathfrak B_{p,N})
\le
\mathfrak D_{s;p}\,N^{-a}e^{28N}.
}
\tag{4.3}
$$



The proof in fact does not use the double-collision or determinant-depth conditions in the definition of $\mathcal S_N$. It applies to the same actual mixed objects at every prime in the original non-arc interval for which the retained boundaries (2.11) hold.

The following lemmas give the complete derivation.

---

## 4.1 The source-specific exponential comparison

### Lemma 4.2

For every original state index $1\le j\le n$,


$$
\boxed{
\rho_j:=\Phi_j-e\Theta_j
=
\frac{\displaystyle\int_0^1e^tC_j(t)\,dt-e+(-1)^j}{2j},
}
\tag{4.4}
$$


and therefore


$$
\boxed{|\rho_j|<3/j.}
\tag{4.5}
$$



### Proof

The supplied finite moment identities are


$$
\eta(C_j)=1-2j\Theta_j,\qquad
E(C_j)=(-1)^j-2j\Phi_j.
$$


For any polynomial $H$, finite integration by parts gives


$$
\int_0^1e^tH(t)\,dt=e\,\eta(H)-E(H).
$$


Applying this to $C_j$,


$$
\int_0^1e^tC_j(t)\,dt
=e-(-1)^j+2j(\Phi_j-e\Theta_j),
$$


which proves (4.4).

Since $|C_j(t)|\le1$ on $0\le t\le1$,


$$
\left|\int_0^1e^tC_j(t)\,dt\right|\le e-1.
$$


Hence


$$
|\rho_j|
\le\frac{(e-1)+e+1}{2j}
=\frac ej<\frac3j.
$$


∎

This comparison depends on both actual affine forcings and their actual boundary constants. It is not an arbitrary relation between two homogeneous solutions.

---

## 4.2 A sign supplied by the corrected $K$-source constant

### Lemma 4.3

At every original admissible pair,


$$
\boxed{R_1<0.}
\tag{4.6}
$$



### Proof

For $x=\ell^2\ge1$,


$$
\mathcal P(x)<0,\qquad
\mathcal Q(x)>0,\qquad
\mathcal F(x)>0.
$$


Thus


$$
\mathscr A>0,\qquad \mathscr B<0.
$$



Moreover,


$$
\begin{aligned}
\mathscr A-\mathscr C_U
&=4\ell^2\mathcal Q-(2\ell-1)\mathcal P-\mathcal F.
\end{aligned}
$$


The first and last terms satisfy


$$
\begin{aligned}
4x\mathcal Q(x)-\mathcal F(x)
={}&304x^3+9628x^2+22056x-5463\\
>{}&0\qquad(x\ge1).
\end{aligned}
$$


Since $-(2\ell-1)\mathcal P>0$, it follows that


$$
\mathscr A>\mathscr C_U.
$$



Now $s\ge7$ is odd, so


$$
\Theta_s\ge1,\qquad \Theta_{s-1}<0.
$$


Consequently,


$$
\mathscr A\Theta_s+\mathscr B\Theta_{s-1}
\ge\mathscr A>\mathscr C_U.
$$


Therefore


$$
R_1=\mathscr C_U-\mathscr A\Theta_s-\mathscr B\Theta_{s-1}<0.
$$


∎

This is a numerical statement in the original residual-source column. It is not a free-input example.

---

## 4.3 A new exact integer relation for the primitive coordinates

Define


$$
\mathbf v=\operatorname{adj}(\mathsf M_c)\mathbf C
=\binom{\mathscr I_2}{-\mathscr I_1}.
\tag{4.7}
$$



### Lemma 4.4

The actual primitive mixed coordinates satisfy


$$
\boxed{
\Delta D_{\rm mix}\mathbf t_\ell
+B_{\rm mix}(\mathbf t_\ell-\mathbf t_s)
+A_{\rm mix}(\mathbf f_\ell+\mathbf f_s)
=D_{\rm mix}\mathbf v.
}
\tag{4.8}
$$



### Proof

Let


$$
\mathbf x=\mathbf t_\ell-\mathbf t_s,\qquad
\mathbf y=\mathbf f_\ell+\mathbf f_s.
$$


Then


$$
\det(\mathbf x,\mathbf y)=\mathfrak D_{s;p}.
$$



Over $\mathbb Q$, set


$$
\mathbf a=\mathsf M_c^{-1}\mathbf u
=\frac{\mathbf v}{\Delta}-\mathbf t_\ell.
$$


The actual mixed minors satisfy


$$
\mathfrak A_{p,N}=\Delta\det(\mathbf x,\mathbf a),
\qquad
\mathfrak B_{p,N}=\Delta\det(\mathbf a,\mathbf y).
$$


The elementary two-dimensional determinant identity gives


$$
\mathbf x\,\mathfrak B_{p,N}
+\mathbf y\,\mathfrak A_{p,N}
=\Delta\mathfrak D_{s;p}\mathbf a
=\mathfrak D_{s;p}\mathbf v
-\Delta\mathfrak D_{s;p}\mathbf t_\ell.
$$


All terms here are integers. Dividing by the proved common divisor $d_{\rm mix}$ gives (4.8). ∎

The temporary rational notation in this proof introduces no $p$-adic inversion of $\Delta$. Equation (4.8) is an integer identity at every prime.

---

## 4.4 The mixed denominator is controlled by the numerator pair

### Lemma 4.5

At every original admissible pair,


$$
\boxed{
D_{\rm mix}\le10H_{\rm num}.
}
\tag{4.9}
$$



### Proof

Put


$$
T=|\Theta_\ell|=\vartheta_\ell,\qquad
S=\Theta_s=\vartheta_s.
$$


The supplied growth gives $0<S<T$. Since $\ell$ is even and $s$ is odd,


$$
|x_s|=T+S<2T.
$$


Also,


$$
y_s=\Phi_\ell+\Phi_s=-\varphi_\ell+\varphi_s,
$$


so $|y_s|<\varphi_\ell$. By Lemma 4.2,


$$
\varphi_\ell\le eT+3/\ell<3T
$$


on the original domain.

We next check the target term quantitatively. Since $N\ge3^{36}$, the polynomial factor in (2.9) is smaller than $e^N$, while $H_G<e^{7N}$. Thus


$$
|\mathscr I_2|<e^{8N}.
\tag{4.10}
$$


On the other hand,


$$
T\ge(\ell-1)!=(2N-7)!
\ge(N-3)^{N-3}>e^{20N}.
\tag{4.11}
$$


For the last inequality, one may use $N-3\ge3N/4$ and
$\log(N-3)>\log N-1>35$. Hence


$$
|\mathscr I_2|<T/2.
$$



The first coordinate of (4.8) is


$$
D_{\rm mix}(\Delta\Theta_\ell-\mathscr I_2)
=-B_{\rm mix}x_s-A_{\rm mix}y_s.
$$


Since $\Delta$ is a nonzero integer,


$$
|\Delta\Theta_\ell-\mathscr I_2|
\ge T-|\mathscr I_2|>T/2.
$$


Therefore


$$
D_{\rm mix}\frac T2
<
H_{\rm num}(|x_s|+|y_s|)
<5TH_{\rm num}.
$$


This proves (4.9). ∎

Thus the possibility of a huge denominator with two exponentially tiny raw real quotients is excluded in these actual columns.

---

## 4.5 The relevant integer linear form is not identically zero

Put


$$
W_0=B_{\rm mix}+\Delta D_{\rm mix}.
\tag{4.12}
$$



### Lemma 4.6

The integer pair


$$
(A_{\rm mix},W_0)
$$


is not $(0,0)$.

### Proof

If $A_{\rm mix}=W_0=0$, then


$$
B_{\rm mix}=-\Delta D_{\rm mix}.
$$


Equation (4.8) becomes


$$
\mathbf v=\Delta\mathbf t_s.
$$


Multiplying by $\mathsf M_c$, and using
$\mathsf M_c\mathbf v=\Delta\mathbf C$, gives


$$
\mathbf C=\mathsf M_c\mathbf t_s.
$$


Thus $\mathbf R=0$, contrary to $R_1<0$ from Lemma 4.3. ∎

The nonvanishing needed in the arithmetic separation is therefore validated in the actual original objects.

---

## 4.6 Finite Hermite separation, with no external irrationality-measure theorem

The following standard-looking estimate is proved here from the specified finite Hermite recurrence.

### Lemma 4.7

For $0\le j\le N$,


$$
\boxed{
Q_j^{\mathrm H}e-P_j^{\mathrm H}
=
\frac{(-1)^j}{j!}
\int_0^1e^t t^j(1-t)^j\,dt.
}
\tag{4.13}
$$


Hence


$$
\boxed{
|Q_j^{\mathrm H}e-P_j^{\mathrm H}|
<
\frac{3j!}{(2j+1)!}.
}
\tag{4.14}
$$


Also,


$$
Q_j^{\mathrm H}\le6^j j!.
\tag{4.15}
$$



### Proof

Let


$$
f_j(t)=\frac{t^j(1-t)^j}{j!},\qquad
I_j=\int_0^1e^tf_j(t)\,dt.
$$


For $j\ge1$, direct differentiation gives


$$
f_{j+1}''=f_{j-1}-(4j+2)f_j.
$$


Both $f_{j+1}$ and $f_{j+1}'$ vanish at $0,1$. Two integrations by parts therefore give


$$
I_{j+1}=I_{j-1}-(4j+2)I_j.
$$


The initial values are


$$
I_0=e-1,\qquad I_1=3-e.
$$


Thus $(-1)^jI_j$ satisfies the same recurrence and seeds as
$Q_j^{\mathrm H}e-P_j^{\mathrm H}$, proving (4.13).

The beta integral is


$$
\int_0^1t^j(1-t)^j\,dt=\frac{(j!)^2}{(2j+1)!}.
$$


Using $e^t<3$ proves (4.14).

Finally, $Q_j^{\mathrm H}>0$, and these denominators are nondecreasing. Thus


$$
Q_{j+1}^{\mathrm H}
\le(4j+3)Q_j^{\mathrm H}
\le6(j+1)Q_j^{\mathrm H},
$$


which proves (4.15) by induction. ∎

The factorial in $f_j$ is part of an explicitly defined rational polynomial used to prove a Hermite approximation identity. It is not a claimed divisor of an original source, mixed determinant, or return.

Only $j=a,a+1=k\le N-6$ will be used below.

---

## 4.7 An evaluated lower bound before asymptotic simplification

### Proposition 4.8

Let


$$
T=|\Theta_\ell|,\qquad S=\Theta_s,\qquad
F_0=10|\mathscr I_2|+4S+1.
$$


Then


$$
\boxed{
H_{\rm num}
\ge
\left(
Q_k^{\mathrm H}\frac{F_0}{T}
+\frac{3a!}{(2a+1)!}
\right)^{-1}.
}
\tag{4.16}
$$



### Proof

The first coordinate of (4.8), together with


$$
\Phi_j=e\Theta_j+\rho_j,
$$


gives


$$
(W_0+eA_{\rm mix})\Theta_\ell
=
D_{\rm mix}\mathscr I_2
+(B_{\rm mix}-eA_{\rm mix})\Theta_s
-A_{\rm mix}(\rho_\ell+\rho_s).
$$


By Lemma 4.5,


$$
D_{\rm mix}\le10H_{\rm num}.
$$


Also,


$$
|B_{\rm mix}-eA_{\rm mix}|<4H_{\rm num},
$$


and, since $s\ge7$ and $\ell>s$,


$$
|\rho_\ell+\rho_s|
<3/\ell+3/s<1.
$$


Therefore


$$
\boxed{
|W_0+eA_{\rm mix}|
\le H_{\rm num}\frac{F_0}{T}.
}
\tag{4.17}
$$



For $j=a,k$, define the actual integers


$$
J_j=W_0Q_j^{\mathrm H}+A_{\rm mix}P_j^{\mathrm H}.
$$


The adjacent Hermite determinant is


$$
P_k^{\mathrm H}Q_a^{\mathrm H}
-P_a^{\mathrm H}Q_k^{\mathrm H}
=2(-1)^a.
$$


Thus, if both $J_a$ and $J_k$ vanished, then
$W_0=A_{\rm mix}=0$, contrary to Lemma 4.6. At least one of these integers has absolute value at least $1$.

For that index $j$,


$$
\begin{aligned}
1
&\le |J_j|\\
&=\left|
Q_j^{\mathrm H}(W_0+eA_{\rm mix})
-A_{\rm mix}(eQ_j^{\mathrm H}-P_j^{\mathrm H})
\right|\\
&\le
H_{\rm num}
\left(
Q_k^{\mathrm H}\frac{F_0}{T}
+\frac{3a!}{(2a+1)!}
\right).
\end{aligned}
$$


The Hermite error bound decreases from $a$ to $k=a+1$. This proves (4.16). ∎

No determinant-$2$ factor has been inverted modulo a prime. The argument only uses that a nonzero integer has absolute value at least $1$.

---

## 4.8 Uniform evaluation of the height bill

We now evaluate the right side of (4.16).

From (4.10) and the supplied state bound,


$$
|\mathscr I_2|<e^{8N},
\qquad
S\le6^{s-1}(s-1)!\le e^{2N}N^s.
$$


Therefore


$$
F_0\le e^{9N}N^s.
\tag{4.18}
$$



Since $\ell-1=2N-7\ge N$, the elementary factorial lower bound gives


$$
T\ge(\ell-1)!
\ge\left(\frac Ne\right)^{\ell-1}
\ge N^\ell e^{-3N}.
\tag{4.19}
$$


Hence


$$
\frac{F_0}{T}\le e^{12N}N^{s-\ell}
=e^{12N}N^{-p}.
\tag{4.20}
$$



By Lemma 4.7,


$$
Q_k^{\mathrm H}\le6^kk!\le e^{2N}N^k.
$$


Consequently,


$$
Q_k^{\mathrm H}\frac{F_0}{T}
\le e^{14N}N^{k-p}
=e^{14N}N^{-a}.
\tag{4.21}
$$



Because $p>N$, we have $a>N/2$. Thus


$$
\frac{3a!}{(2a+1)!}
=
\frac3{(a+1)(a+2)\cdots(2a+1)}
\le3\left(\frac2N\right)^{a+1}
\le e^{2N}N^{-a}.
\tag{4.22}
$$



Combining (4.16), (4.21), and (4.22),


$$
H_{\rm num}\ge e^{-15N}N^a.
$$


The slightly relaxed stated bound


$$
H_{\rm num}\ge e^{-16N}N^a
$$


follows.

This proves (4.1) with an explicit absolute constant, uniformly on the original domain.

---

## 4.9 From numerator height to the actual clearer

It remains to bound the actual raw real quotient with an explicit exponential bill.

From (3.16),


$$
F_j^*\le3\cdot6^{j-1}(j-1)!\qquad(j\ge2).
$$


Using (3.7) and (3.17),


$$
\begin{aligned}
\frac{\max(|\mathfrak A_{p,N}|,|\mathfrak B_{p,N}|)}
     {\mathfrak D_{s;p}}
&<
\frac{729}{64}\,10^{12}
n^{16}H_G
\frac{(\ell-1)(s-1)}p\,2^{\ell+s}\\
&<
10^{14}n^{18}H_G\,2^{\ell+s}.
\end{aligned}
$$


Here $\ell+s<3N$. On the original domain, the polynomial factor is less than $e^N$, $H_G<e^{7N}$, and $2^{\ell+s}<e^{3N}$. In particular,


$$
\boxed{
\frac{\max(|\mathfrak A_{p,N}|,|\mathfrak B_{p,N}|)}
     {\mathfrak D_{s;p}}
<e^{12N}.
}
\tag{4.23}
$$



Primitive normalization does not change this real quotient:


$$
\frac{H_{\rm num}}{D_{\rm mix}}
=
\frac{\max(|\mathfrak A_{p,N}|,|\mathfrak B_{p,N}|)}
     {\mathfrak D_{s;p}}.
$$


Thus


$$
D_{\rm mix}>e^{-12N}H_{\rm num}
\ge N^ae^{-28N}.
$$


This proves (4.2), and (4.3) follows from
$d_{\rm mix}=\mathfrak D_{s;p}/D_{\rm mix}$.

Theorem 4.1 is proved. ∎

---

# 5. The new all-prime gcd constraint and its exact force

## 5.1 All-prime formulation

Theorem 4.1 gives the following actual arithmetic inequality:


$$
\boxed{
\begin{aligned}
\sum_{\substack{q\\ q\ {\rm prime}}}
\Bigl(
v_q(\mathfrak D_{s;p})
-\min\{&
v_q(\mathfrak D_{s;p}),\\
&v_q(\mathfrak A_{p,N}),
v_q(\mathfrak B_{p,N})\}
\Bigr)\log q\\
&\ge \frac{p-1}{2}\log N-28N.
\end{aligned}
}
\tag{5.1}
$$



This is not merely the primitive definition: the substantive new assertion is the explicit lower bound on the sum.

It includes the prime $2$ and every other prime. Moreover, the chosen prime $p$ contributes zero, by (3.6). Hence all of the lower bound is carried by primes other than the source-collision prime:


$$
\boxed{
\sum_{\substack{q\ne p\\q\ {\rm prime}}}
v_q(D_{\rm mix})\log q
\ge\frac{p-1}{2}\log N-28N.
}
\tag{5.2}
$$



Thus the actual mixed clearer retains a factorial logarithmic mass at other primes even though it is a unit at the prime whose source depth is being tested.

No individual valuation classification at those other primes is claimed.

## 5.2 Quantified obstruction to the proposed exponential-height mechanism

Since $p>N$,


$$
\log H_{\rm num}\ge\frac N2\log N-16N,
$$




$$
\log D_{\rm mix}\ge\frac N2\log N-28N.
\tag{5.3}
$$



For any fixed constant $C$, if


$$
\log N>2(C+28),
$$


then every eligible pair at that original $N$ satisfies


$$
D_{\rm mix}>e^{CN}.
$$


Likewise, $\log N>2(C+16)$ forces
$H_{\rm num}>e^{CN}$.

Accordingly:

- a uniform exponential bound for the actual primitive numerator pair cannot hold on an unbounded family of eligible pairs;
- the actual simultaneous clearer does not remove the factorial arithmetic height;
- the small raw real quotient does not become a small-height integer pair after the largest available common integral division.

There is an important quantifier limitation. The theorem does not prove that $\mathcal S_N$ is nonempty for arbitrarily large original $N$. If the remaining branch eventually disappears, a bound stated only on that branch can be vacuous. The obstruction proved here is uniform at every pair that actually occurs.

## 5.3 What has not been ruled out

The result does not classify all possible repaired auxiliaries.

It does not rule out:

- an additional, separately proved integral normalization that changes the auxiliary;
- a different fixed-$N$ integer;
- a source-specific bound on the complete post-credit depths;
- exceptional large endpoint credits that reduce a separately paid quotient;
- a continuation theorem excluding sufficiently deep additive cancellation.

It rules out the particular hoped-for mechanism in which the **actual simultaneous primitive normalization of the turn20 mixed ratios** is itself expected to have exponential arithmetic height.

The unavailable division by


$$
(\ell-2)!(s-2)!
$$


has not been used, and its valuation mismatch remains in force.

---

# 6. Surviving depth: local divisibility versus aggregate payment

## 6.1 The complete local divisor direction survives normalization

At $p\in\mathcal S_N$, both raw mixed minors are divisible by $p^{c_p}$. Since $p\nmid d_{\rm mix}$,


$$
p^{c_p}\mid A_{\rm mix},\qquad
p^{c_p}\mid B_{\rm mix}.
$$


The positive integer


$$
\mathcal N_{p,N}=A_{\rm mix}^2+B_{\rm mix}^2
$$


therefore satisfies


$$
v_p(\mathcal N_{p,N})\ge2c_p.
$$



The paid second-layer quotient is


$$
\mathcal N_{p,N}^{(2)}
=\frac{\mathcal N_{p,N}}{p^4}\in\mathbb Z_{>0}.
\tag{6.1}
$$


To retain the entire credit $B_p=(H_p-2)_+$, define


$$
\boxed{
\mathcal C_{p,N}
=
\frac{\mathcal N_{p,N}^{(2)}}
{\gcd(\mathcal N_{p,N}^{(2)},p^{2B_p})}.
}
\tag{6.2}
$$


Every division is integral, and


$$
\boxed{
p^{2e_p}\mid\mathcal C_{p,N}.
}
\tag{6.3}
$$



This direction retains:

- the complete source depth;
- all $(H_p-2)_+$ credits;
- determinant-critical primes;
- the actual divided Gaussian source.

No equality for the valuation of a sum of two squares is assumed. At some primes the norm can have additional cancellation; only the valid lower valuation bound is used.

## 6.2 The new lower bound on the unpaid local norm height

Theorem 4.1 implies


$$
\mathcal N_{p,N}\ge H_{\rm num}^2
\ge N^{p-1}e^{-32N}.
$$


Since $p<2N$, and $4\log(2N)<N$ on the original domain,


$$
\boxed{
\log \mathcal N_{p,N}^{(2)}
\ge(p-1)\log N-33N.
}
\tag{6.4}
$$



Thus even after the two proved source layers are removed, the uncredited primitive norm still has factorial logarithmic height.

For the fully credited quotient, the honest consequence is only


$$
\boxed{
\log\mathcal C_{p,N}
\ge
(p-1)\log N-33N-2B_p\log p.
}
\tag{6.5}
$$


No unsupported upper bound for $B_p$ is inserted.

This distinction matters. The theorem disproves the unmodified primitive-height expectation; it does not prove that every possible paid post-credit quotient remains large.

## 6.3 Aggregate capture is a separate obligation

For any subset $\mathcal T\subseteq\mathcal S_N$,


$$
\prod_{p\in\mathcal T}p^{2e_p}
\mid
\prod_{p\in\mathcal T}\mathcal C_{p,N}.
\tag{6.6}
$$


This is a valid aggregate divisor statement.

It is not an $O(N)$ height payment. To obtain such a payment from (6.6), one would still need


$$
\sum_{p\in\mathcal T}\log\mathcal C_{p,N}=O(N),
$$


which is not proved.

Even before the additional credits,


$$
\log\prod_{p\in\mathcal T}\mathcal N_{p,N}^{(2)}
\ge
\sum_{p\in\mathcal T}\bigl((p-1)\log N-33N\bigr).
\tag{6.7}
$$


There is therefore no justification for multiplying the individual primitive norms and calling the resulting bill exponential.

Nor would a hypothetical exponential bound for each of potentially $O(N/\log N)$ individual auxiliaries, by itself, prove an exponential aggregate bill.

The $p$-dependent Hermite indices used in Theorem 4.1 serve only as finite rational-approximation comparisons. They are not treated as embeddings of one global algebraic number, and no product formula is invoked.

## 6.4 No new $O(N)$ bound on the depth mass is booked

The exact surviving mass remains


$$
\sum_{p\in\mathcal S_N}e_p\log p.
$$


The established source bound still gives the coarse estimate


$$
\sum_{p\in\mathcal S_N}e_p\log p
\le\log c
\le\log N!+O(N).
\tag{6.8}
$$


The new primitive-clearer theorem does not improve this to $O(N)$.

Its progress is different: it resolves the local primitive-height question negatively, at the quantified scope stated above, and prevents that unavailable height saving from being used in an aggregate argument.

---

# 7. A repaired, concrete continuation objective

The preceding theorem suggests abandoning the size of the individual primitive mixed pair as the principal certificate. A weaker local depth theorem coupled to a **single already bounded fixed-$N$ integer** would avoid both obstructions.

Here is one precise continuation target.

## Open lemma — one-extra-depth coefficient saturation

For every original $N$ and every $p\in\mathcal S_N$, let


$$
j_p=v_p(J_N^{\rm aff}),\qquad B_p=(H_p-2)_+,
$$


and choose the actual critical-safe chart $\zeta_{p,N}$ from Section 3.4.

Prove that the two actual integers $16U$ and $\zeta_{p,N}$ are **not both divisible** by


$$
\boxed{p^{\,4+B_p+j_p}.}
\tag{7.1}
$$



No quotient in (7.1) is presumed integral. This is a divisibility assertion about the complete original integers.

By the exact chart identity, the lemma would imply


$$
c_p\le3+B_p+j_p,
$$


and hence


$$
\boxed{e_p\le1+j_p.}
\tag{7.2}
$$



This is strictly weaker than universal third-depth avoidance. For example, when $B_p=j_p=0$, it permits $c_p=3$.

## 7.1 Its aggregate payment is genuinely fixed-$N$

Every $p\in\mathcal S_N$ satisfies


$$
v_p\binom{2N}{N}=1.
$$


Consequently, (7.2) would give the single fixed-$N$ divisor statement


$$
\boxed{
\prod_{p\in\mathcal S_N}p^{e_p}
\mid
J_N^{\rm aff}\binom{2N}{N}.
}
\tag{7.3}
$$


Its whole logarithmic bill is


$$
\log J_N^{\rm aff}+2N\log2=O(N).
\tag{7.4}
$$



Thus this particular follow-on lemma addresses both obligations:

1. it does not require a false exponential bound for each primitive mixed pair;
2. it supplies aggregate capture in one actual fixed-$N$ integer.

Determinant-critical primes are retained. On the present branch,


$$
v_p(\Delta)\le j_p,
$$


but the lemma is tested in the critical-safe chart and does not invert $\Delta$.

## 7.2 The arithmetic step still missing

The open lemma requires excluding the complete additive cancellation in the available chart at the depth in (7.1).

In the endpoint chart, the relevant integer is exactly


$$
\begin{aligned}
\zeta_{p,N}
={}&R_1E_2-R_2E_1\\
&-\Delta\left(
2(-1)^{k-1}\chi^2
+p\chi\Lambda_\sigma+p^2\Xi_\sigma
+4p\mathfrak f_{s;p}
\right).
\end{aligned}
\tag{7.5}
$$


In the residual-source chart, it is exactly


$$
\begin{aligned}
\zeta_{p,N}
={}&
\mathscr I_1(\Theta_s-\Theta_\ell)
+\mathscr I_2(\Theta_{s-1}-\Theta_{\ell-1})\\
&+\Delta(
\Theta_s\Theta_{\ell-1}-\Theta_{s-1}\Theta_\ell).
\end{aligned}
\tag{7.6}
$$



The new Archimedean separation theorem does not exclude these $p$-adic cancellations. Equation (7.1), or a comparable source-specific theorem with a proved aggregate payment, remains an open obligation.

No claim that this lemma is true is made here.

---

# 8. Why this argument lies outside the supplied homogeneous formal filter

The archive obstruction concerns formal auxiliaries generated from one homogeneous Bessel recurrence and its first shifts or jets. No classification of the present two forced columns follows from that result.

The extra mechanism used here is explicit:

1. The two actual moment identities imply
   

$$
\Phi_j-e\Theta_j
   =
   \frac{\int_0^1e^tC_j(t)\,dt-e+(-1)^j}{2j}.
$$


   Both affine forcings and both boundary contributions are necessary.

2. The divided Gaussian column fixes the small-height target
   

$$
\mathbf v=\binom{\mathscr I_2}{-\mathscr I_1}.
$$



3. The complete mixed columns yield the integral relation (4.8), in which terminal factorial states are compared with residual states and that actual target.

4. Finite Hermite approximation and integer nonvanishing then force a large primitive coefficient.

The arithmetic payment is fully visible: the Hermite denominators and errors at $a,k$ lead to the factor $N^{(p-1)/2}e^{-O(N)}$. This mechanism produces a **height obstruction**, not an unpaid height saving.

No theorem from the unread Appell-Wronskian paper is imported. No identification with its objects is asserted. No Kurepa or Wilson nonvanishing claim is used.

---

# 9. Retained lift, finite precision, and division ledger

The new height theorem is exact and does not require a residue computation. Nevertheless, the source-specific continuation target must preserve the turn19 lift in full.

## 9.1 Both residual correction systems

For $1\le j\le r-1$, write


$$
\mathcal L_j Z=Z_{j+1}+4jZ_j-Z_{j-1}.
$$


The homogeneous residual columns have


$$
\mathcal L_j\mathcal A=\mathcal L_j\mathcal B=0,
$$




$$
(\mathcal A_0,\mathcal A_1)=(1,0),\qquad
(\mathcal B_0,\mathcal B_1)=(0,1).
$$


The first corrections are


$$
\mathcal L_j\mathcal D=-4\mathcal A_j,\qquad
\mathcal L_j\mathcal E=-4\mathcal B_j,
$$




$$
\mathcal L_j\mathcal T=-4\Theta_j,\qquad
\mathcal L_j\mathcal W=-4\Phi_j,
$$


with


$$
(\mathcal D_0,\mathcal D_1)=(0,-4),
$$


and zero pairs for $\mathcal E,\mathcal T,\mathcal W$.

The two complete anchored columns are


$$
Z_{0,j}^+
=\chi(\mathcal A_jQ_{k-1}^{\mathrm H}
-\mathcal B_jQ_k^{\mathrm H})+\Theta_j,
$$




$$
\begin{aligned}
Z_{1,j}^+
={}&\chi(\mathcal D_jQ_{k-1}^{\mathrm H}
-\mathcal E_jQ_k^{\mathrm H})
+\mathcal T_j\\
&+\mathcal A_j\sigma_0^+
+\mathcal B_j\sigma_1^+,
\end{aligned}
$$


and


$$
Z_{0,j}^-
=\chi(\mathcal A_jP_{k-1}^{\mathrm H}
-\mathcal B_jP_k^{\mathrm H})-\Phi_j,
$$




$$
\begin{aligned}
Z_{1,j}^-
={}&\chi(\mathcal D_jP_{k-1}^{\mathrm H}
-\mathcal E_jP_k^{\mathrm H})
-\mathcal W_j\\
&+\mathcal A_j\sigma_0^-
+\mathcal B_j\sigma_1^-.
\end{aligned}
\tag{9.1}
$$


Put $Z_j^\pm=Z_{0,j}^\pm+pZ_{1,j}^\pm$.

The exact quotient states satisfy


$$
\Theta_{p+j}=Z_j^++p^2\mathfrak e_j^+,\qquad
\Phi_{p+j}=Z_j^-+p^2\mathfrak e_j^-,
$$




$$
\mathfrak e_0^\pm=0,\qquad
\mathfrak e_1^\pm=-4\sigma_0^\pm,
$$




$$
\mathfrak e_{j+1}^\pm
+4(p+j)\mathfrak e_j^\pm-\mathfrak e_{j-1}^\pm
=-4Z_{1,j}^\pm.
\tag{9.2}
$$



The second corrections have zero seeds and


$$
\mathcal L_j\mathcal D^{\langle2\rangle}=-4\mathcal D_j,\quad
\mathcal L_j\mathcal E^{\langle2\rangle}=-4\mathcal E_j,
$$




$$
\mathcal L_j\mathcal T^{\langle2\rangle}=-4\mathcal T_j,\quad
\mathcal L_j\mathcal W^{\langle2\rangle}=-4\mathcal W_j.
$$


Thus the retained next digits are


$$
\begin{aligned}
Y_j^+={}&
\mathcal D_j\sigma_0^++\mathcal E_j\sigma_1^+\\
&+\chi(
\mathcal D_j^{\langle2\rangle}Q_{k-1}^{\mathrm H}
-\mathcal E_j^{\langle2\rangle}Q_k^{\mathrm H})
+\mathcal T_j^{\langle2\rangle},
\end{aligned}
$$




$$
\begin{aligned}
Y_j^-={}&
\mathcal D_j\sigma_0^-+\mathcal E_j\sigma_1^-\\
&+\chi(
\mathcal D_j^{\langle2\rangle}P_{k-1}^{\mathrm H}
-\mathcal E_j^{\langle2\rangle}P_k^{\mathrm H})
-\mathcal W_j^{\langle2\rangle},
\end{aligned}
\tag{9.3}
$$


with


$$
\mathfrak e_j^\pm\equiv Y_j^\pm\pmod p.
$$



All residual recurrence steps end at $r-1$, and all shifted original steps end at $p+r-1=n-1$.

## 9.2 Complete source and endpoint evaluations

Define


$$
B_U=\mathscr C_U-\mathscr A Z_s^+-\mathscr B Z_{s-1}^+,
$$




$$
B_V=C_V-PZ_r^+-QZ_{r-1}^+.
$$


The actual double collision proves $p^2\mid B_U,B_V$, and


$$
\mathscr L_U
\equiv B_U/p^2-\mathscr A Y_s^+-\mathscr B Y_{s-1}^+
\equiv16U/p^2\pmod p,
$$




$$
\mathscr L_V
\equiv B_V/p^2-PY_r^+-QY_{r-1}^+
\equiv V/p^2\pmod p.
\tag{9.4}
$$



The complete endpoint evaluations remain


$$
\begin{aligned}
16E_K\equiv{}&
\mathscr C_E+\mathscr A Z_s^-+\mathscr B Z_{s-1}^-\\
&+p^2(\mathscr A Y_s^-+\mathscr B Y_{s-1}^-)
\pmod{p^3},
\end{aligned}
$$




$$
\begin{aligned}
E_F\equiv{}&
C_F^E-PZ_r^--QZ_{r-1}^-\\
&-p^2(PY_r^-+QY_{r-1}^-)
\pmod{p^3}.
\end{aligned}
\tag{9.5}
$$



No new nonvanishing of $(\mathscr L_U,\mathscr L_V)$ is asserted.

## 9.3 Paid divisions and precision

- If $a=v_p(g_B)$, raw linear Gaussian data require precision $p^{a+h}$ to obtain the divided coefficients modulo $p^h$.
- Raw quadratic Gaussian data require precision $p^{2a+h}$ before division by $g_B^2$.
- The defects $\sigma^\pm$ require one paid division by $p$. Their values modulo $p^{h-1}$ require numerator precision modulo $p^h$.
- The second-collision carries require two paid divisions by $p$.
- No determinant inversion occurs in the mixed identity, the primitive-height theorem, or the critical-safe chart.
- The exact mixed division is by $d_{\rm mix}$, and no larger common divisor is presumed.
- The norm divisions by $p^4$ and by the gcd in (6.2) are proved.
- Deeper use of $H_p$ requires validated information about the actual $h_p,b_p,z_p,t_p$; a third-precision endpoint computation does not automatically determine these deeper valuations.
- The original arc divisions and final all-prime gcd remain separate.

The open lemma (7.1) may require higher source precision than $p^3$. Writing its exact required modulus does not evaluate or prove its nonvanishing.

---

# 10. Preservation of the complete original producer

## 10.1 Source and endpoint balances

The source balance remains


$$
\begin{aligned}
&(\nu\mathscr A-16\tau\Pi)\Theta_\ell
+(\nu\mathscr B-16\tau\Omega)\Theta_{\ell-1}\\
&\hspace{12mm}
=\nu\mathscr C_U-16\tau C^{\rm s}.
\end{aligned}
\tag{10.1}
$$


For


$$
T_{\rm end}=\tau(E_F-\delta^2)+\nu E_K,
$$


the complete endpoint balance is


$$
\begin{aligned}
16T_{\rm end}={}&
16\tau(C^{\rm e}-\delta^2)+\nu\mathscr C_E\\
&+(\nu\mathscr A-16\tau\Pi)\Phi_\ell
+(\nu\mathscr B-16\tau\Omega)\Phi_{\ell-1}.
\end{aligned}
\tag{10.2}
$$



## 10.2 Complete returns

The centered source return has


$$
z_\ell=16\Omega U-\mathscr B V,\qquad
z_{\ell-1}=\mathscr A V-16\Pi U,
$$




$$
z_j=-\Delta\Theta_j+\varrho_j,
$$




$$
\varrho_\ell=\mathscr I_2,\qquad
\varrho_{\ell-1}=-\mathscr I_1,
$$




$$
\varrho_{j-1}=\varrho_{j+1}+4j\varrho_j-2\Delta.
$$


Hence


$$
z_{j-1}=z_{j+1}+4jz_j.
$$



After the actual arc clearing below, let


$$
k_E=D\mathscr C_E-16DR_K,\qquad
f_E=DC^{\rm e}-DR_F.
$$


The endpoint return is


$$
w_\ell=16\Omega Y+\mathscr B X,\qquad
w_{\ell-1}=-16\Pi Y-\mathscr A X,
$$




$$
w_j=D\Delta\Phi_j+\sigma_j,
$$




$$
\sigma_\ell=\Omega k_E+\mathscr Bf_E,\qquad
\sigma_{\ell-1}=-\Pi k_E-\mathscr Af_E,
$$




$$
\sigma_{j-1}
=\sigma_{j+1}+4j\sigma_j+2D\Delta(-1)^j.
$$


The retained determinant identity is


$$
z_\ell w_{\ell-1}-z_{\ell-1}w_\ell
=-16\Delta(UX+VY).
\tag{10.3}
$$


No division by $\Delta$ is made.

For exactly $0\le a\le N$, the canonical Hermite returns remain


$$
\mathcal R_{a;N}=d_KP_a^{\mathrm H}U+Q_a^{\mathrm H}y_K.
$$


With


$$
\Psi_j^{(a)}=Q_a^{\mathrm H}\Phi_j-P_a^{\mathrm H}\Theta_j,
$$


their forcing is


$$
\Psi_{j+1}^{(a)}+4j\Psi_j^{(a)}-\Psi_{j-1}^{(a)}
=2\bigl(Q_a^{\mathrm H}(-1)^j-P_a^{\mathrm H}\bigr),
$$


and


$$
\begin{aligned}
16\mathcal R_{a;N}
={}&d_K\bigl(
P_a^{\mathrm H}\mathscr C_U+
Q_a^{\mathrm H}\mathscr C_E+
\mathscr A\Psi_\ell^{(a)}+
\mathscr B\Psi_{\ell-1}^{(a)}
\bigr)\\
&-16Q_a^{\mathrm H}a_K.
\end{aligned}
\tag{10.4}
$$



The supplied signed-return facts remain


$$
\mathcal R_{N-1;N}<0<\mathcal R_{N;N},
$$




$$
|\mathcal R_{N-1;N}|,\ |\mathcal R_{N;N}|
<d_K36^NN!,
$$


with


$$
v_2(U)=2,\qquad v_2(y_K)=1,\qquad d_K\text{ odd}.
$$


The all-prime product payment is unchanged:


$$
\boxed{
\frac{c(r^\circ)^2}{\kappa_N^{\rm prod}}
\mid
\mathcal R_{N-1;N}\mathcal R_{N;N}.
}
\tag{10.5}
$$



No factorial divisibility is inferred from the size of either return.

## 10.3 Literal terminal $K$-column boundary

For completeness, the original thirteen-weight terminal description remains equivalent to the centered column. Its weights are


$$
(w_0,\ldots,w_{12})
=(1,8,58,168,399,-176,-916,-176,399,168,58,8,1).
$$


For exactly $1\le k\le11$,


$$
r_{k+1}=r_{k-1}+4(n-k)r_k,
$$




$$
s_{k+1}^*=s_{k-1}^*+4(n-k)s_k^*,
$$




$$
\kappa_{k+1}=\kappa_{k-1}+4(n-k)\kappa_k-2,
$$




$$
\omega_{k+1}=\omega_{k-1}+4(n-k)\omega_k-2(-1)^k,
$$


with the supplied seeds


$$
(r_0,s_0^*)=(1,0),\quad(r_1,s_1^*)=(0,1),
$$




$$
\kappa_0=\kappa_1=\omega_0=\omega_1=0.
$$


Then


$$
\mathsf A=\sum_{k=0}^{12}w_k(n-k)r_k,\qquad
\mathsf B=\sum_{k=0}^{12}w_k(n-k)s_k^*,
$$




$$
\mathsf C_U=679936-\sum_{k=0}^{12}w_k(n-k)\kappa_k,
$$




$$
\mathsf C_E=-1849344+\sum_{k=0}^{12}w_k(n-k)\omega_k,
$$


and


$$
4096U=\mathsf C_U-\mathsf A\Theta_n-\mathsf B\Theta_{n-1},
$$




$$
4096E_K=\mathsf C_E+\mathsf A\Phi_n+\mathsf B\Phi_{n-1}.
\tag{10.6}
$$


These are retained finite identities, not recalculated claims about numerical gcds.

The rational interface remains on $2\le j\le n-1$:


$$
s_j=\frac1j-2\Theta_j,
$$




$$
s_{j-1}=s_{j+1}+4js_j+\frac2{j^2-1}.
$$


Its payments remain


$$
Q_{\rm loc}(n)=\prod_{a=0}^{12}(n-a),\qquad
\mathcal L_n=\operatorname{lcm}(1,\ldots,n),
$$


with


$$
\frac{2\mathcal L_n}{j^2-1}
=\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}.
$$


Neither is substituted for the least arc clearer.

## 10.4 Both arcs and the least original clearers

Retain


$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


The monic quotient degrees are at most $2N-2$.

The square-arc return has zero seeds at $0,1$ and, through the physical terminal,


$$
\xi_{j+1}=4\upsilon_j-2\xi_j-\xi_{j-1}+16b_j,
$$




$$
\upsilon_{j+1}
=-4\xi_j-2\upsilon_j-\upsilon_{j-1}+16(\ell_j-a_j),
$$


where


$$
\ell_j=
\begin{cases}
0,&j\text{ odd},\\
(1-j^2)^{-1},&j\text{ even}.
\end{cases}
$$


The physical output is


$$
R_F=
\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
-2\alpha\beta\xi_{n-1}}2.
\tag{10.7}
$$



After reducing both arcs completely,


$$
\boxed{
D=\operatorname{lcm}(\operatorname{den}R_F,\operatorname{den}R_K).
}
$$


Set


$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$


Independently reduce


$$
\tau R_F+\nu R_K=\frac b\lambda,\qquad
\gcd(b,\lambda)=1,\quad\lambda>0.
$$


Then


$$
E=\tau E_F+\nu E_K,\qquad
A=\lambda E-b,
$$




$$
\boxed{G=\gcd(M,A),}
$$


where the gcd is over **all primes**, and


$$
\boxed{
p_N=A/G,\qquad q_N=\lambda M/G.
}
\tag{10.8}
$$


Because $\gcd(\lambda,A)=1$, this is the actual primitive pair.

The auxiliary $D_{\rm mix}$ does not replace $D$, $\lambda$, $G$, or $q_N$.

---

# 11. The complete strictly positive whole error

The original polynomial remains


$$
P_N(t)
=\frac{F(t)^2+(V/U)K(t)}{\delta^2}
=\frac{W_{\rm prim}(t)}M.
$$


Its whole error is


$$
\boxed{
\epsilon_N=
\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0.
}
\tag{11.1}
$$



The strict positivity follows from the retained positive source coefficients and the nonzero nonnegative polynomial integrand.

The exact source balance gives


$$
\eta(W_{\rm prim})
=\tau(\delta^2+V)-\nu U=M.
$$


Thus


$$
\int_0^1e^tW_{\rm prim}(t)\,dt=eM-E.
$$


Both complete arcs give


$$
4\int_0^1\frac{W_{\rm prim}(t)}{1+t^2}\,dt
=\pi M+\frac b\lambda.
$$


Therefore


$$
\epsilon_N=e+\pi-\frac{A}{\lambda M},
$$


and at the same original indices,


$$
\boxed{
q_N(e+\pi)-p_N=q_N\epsilon_N>0.
}
\tag{11.2}
$$



The complete rational enclosure remains


$$
3J_N<\epsilon_N<7J_N,\qquad
J_N=\frac{J_F+(V/U)J_K}{\delta^2},
$$


where


$$
J_F=
\alpha^2\frac{2N^2-1}{4N^2-1}
+\beta^2\frac{2(N-1)^2-1}{4(N-1)^2-1},
$$


and, with $j_a=(1-4a^2)^{-1}$,


$$
J_K=\frac{61}{420}
+\frac{
916j_m-399(j_{m+1}+j_{m-1})
-58(j_{m+2}+j_{m-2})
-(j_{m+3}+j_{m-3})
}{8192}.
$$


Hence


$$
\boxed{
q_NJ_N
=\frac{\lambda_N}{G_N}
\bigl(\tau_NJ_F+\nu_NJ_K\bigr).
}
\tag{11.3}
$$



Both positive summands are retained. Neither an exponential-only error nor a mixed component replaces the whole error.

The new lower bound for an auxiliary mixed clearer does not establish a corresponding bound for the actual primitive denominator $q_N$. No conclusion about $q_N\epsilon_N$, producer retirement, or the rationality of $e+\pi$ follows from it alone.

---

# 12. Proof-status and computation ledger

| Item | Status |
|---|---|
| Original domain, terminal $2N$, divided Gaussian data, actual contents | Retained unchanged |
| Complete corrected columns and six-step forcing transport | Reuse at supplied scope |
| Residual-relative determinant, Hermite defects, positivity and factorial size | Reuse at supplied scope |
| $K$-row primitivity and both critical-safe charts | Reuse at supplied scope |
| Turn15 all-prime credit $H_p$ | Reuse, with every term retained |
| Exact moment comparison $\Phi_j-e\Theta_j=O(1/j)$ in the actual states | Proved here by finite integration by parts |
| Actual residual sign $R_1<0$ | Proved here from the corrected $K$-constant |
| Primitive integer relation (4.8) | Proved here |
| Evaluated finite Hermite separation (4.16) | Proved here |
| $H_{\rm num}\ge N^{(p-1)/2}e^{-16N}$ | **New proved uniform bound** |
| $D_{\rm mix}\ge N^{(p-1)/2}e^{-28N}$ | **New proved uniform bound** |
| All-prime gcd constraint (4.3), (5.1) | **New proved arithmetic obstruction** |
| Complete local post-credit norm divisibility | Proved, but no aggregate $O(N)$ height bound |
| One-extra-depth coefficient saturation lemma | Open |
| Fixed-$N$ aggregate consequence (7.3) | Conditional on that lemma |
| $O(N)$ surviving depth mass | Not proved |
| Smaller-prime and $p>2N$ obligations | Separate and open |
| Retirement of the original producer | Not proved |
| Rationality or irrationality of $e+\pi$ | Unresolved |

The pending different review of turn20 is not represented as completed.

## Computation status

No numerical computation has been performed.

No bounded exact arithmetic calculation is indispensable to the new theorem. Its new inputs are the displayed polynomial identities, finite moment identities, and Hermite recurrence; the required outputs are derived symbolically in Sections 4.1–4.9.

Accordingly:

- no original-sized recurrence or matrix calculation is proposed;
- no prime scan is proposed;
- no old $p23$ certificate is rerun;
- no optional constant check is requested.

A finite numerical evaluation of the mixed gcd at selected pairs would establish only those finite values and is unnecessary for the uniform lower bound proved here.

---

# Final conclusion

The actual primitive normalization of the turn20 mixed invariant has now been quantitatively constrained:



$$
\boxed{
\max\{|A_{\rm mix}|,|B_{\rm mix}|\}
\ge N^{(p-1)/2}e^{-16N},
\qquad
D_{\rm mix}\ge N^{(p-1)/2}e^{-28N}.
}
$$



Equivalently, the actual all-prime mixed gcd cannot remove at least


$$
\frac{p-1}{2}\log N-O(N)
$$


of the determinant’s logarithmic arithmetic height. This surviving denominator mass lies away from the chosen prime $p$, where the mixed determinant remains a unit.

This is a new, source-specific, original-object obstruction to the hoped-for exponential primitive-height mechanism. It is stronger than the earlier observation that an attractive factorial division was unavailable: it measures how much arithmetic height necessarily survives **the largest legitimate simultaneous common division**.

The exact remaining interval bottleneck is not the unit determinant, the chart, or the primitive definition. It is a quantified bound on the full post-credit additive cancellation in the actual source-specific integers, together with capture across all remaining primes by one fixed-$N$ certificate or a genuinely $O(N)$-height aggregate. The open saturation lemma in Section 7 gives one explicit, weaker-than-third-depth-avoidance target with such an aggregate payment.

The smaller-prime and $p>2N$ obligations remain separate and open. The original all-prime final gcd, actual primitive denominator, both arcs, and strictly positive whole error remain unchanged. **No proof or disproof of irrationality of $e+\pi$, and no retirement of the producer, follows at this stage.**
