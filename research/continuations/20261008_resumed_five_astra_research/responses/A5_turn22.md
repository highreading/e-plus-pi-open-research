> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fourth-precision arithmetic in the original Gaussian–Hermite columns

## Abstract and proof status

The rationality or irrationality of $e+\pi$ remains unresolved.

The one-extra-depth assertion assigned in this turn is **not proved or refuted below**. In particular, no bound


$$
c_p\le 3+B_p+v_p(J_N^{\rm aff})
$$


is claimed on the whole remaining interval.

The new result is an arithmetic evaluation of data that the supplied third-digit calculation retained as exact but unevaluated base defects. More precisely:

1. The four actual Hermite-anchored defects
   

$$
\sigma_0^+,\ \sigma_1^+,\ \sigma_0^-,\ \sigma_1^-
$$


   are evaluated modulo $p^3$, using explicit finite Hermite coefficients, reciprocal-power sums, and the actual base-$4$ Fermat quotient. No $p$-base state remains on the right-hand sides.

2. The upper-half factorial terms admit an exact normalization against the **actual Hermite coefficients**. In this normalization their common terminal factorial cancels algebraically. The resulting factor is
   

$$
\frac{4^{p-1}}{p+1}
   \prod_{t=1}^{h}
   \frac{(1-2p/(2t-1))(1-p/t)}
        {(1-2p/t)(1-p/(2t-1))}.
$$


   Its cubic expansion is evaluated explicitly. No Wilson-quotient nonvanishing assertion is used.

3. An explicit integer continuant resolves the next term of both signed quotient systems. This gives complete source and endpoint evaluations modulo $p^4$, including the full fourth source digit after an actual third collision.

4. The same calculation is placed in both existing critical-safe charts. In the endpoint chart the full additive difference, including both Hermite defect pairs and the mixed forcing return, is retained modulo $p^4$.

These are new arithmetic evaluations, not a fifth valuation-contact definition. They narrow the unresolved fourth-depth calculation, but do not establish its nonvanishing. No aggregate coverage assertion is made.

No numerical computation has been performed or is requested.

---

## 1. Original objects and the exact target

Throughout,


$$
\boxed{N=9^{18+32u}=3^{36+64u},\qquad u\in\mathbb Z_{\ge0},}
$$


and


$$
n=2N,\qquad m=N-3,\qquad \ell=2N-6.
$$


The physical terminal is $n=2N$.

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


with


$$
C_0=1,\quad C_1=2t-1,\quad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$


The Gaussian division is the actual integer division


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
F=\alpha C_N-\beta C_{N-1},\qquad F(\pm i)=\delta.
$$



For an integer polynomial $H$, retain


$$
\eta(H)=\sum_jj![z^j]H(1-z),\qquad
E(H)=\sum_j(-1)^jj![t^j]H(t).
$$


Put


$$
\mathcal H=t(1-t)(1+t^2)^2,\qquad K=\mathcal H C_m^2,
$$




$$
U=-\eta(K),\qquad V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
$$


The actual content and primitive source data remain


$$
\operatorname{cont}(W_{\rm raw})=g_B^2c,
$$




$$
\tau=U/c,\qquad \nu=V/c,\qquad
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2,
$$


with $U,V,M>0$.

### 1.1 Complete credit

Let


$$
L(x)=(x-1)(x-9)(x-25),\qquad
A_K(x)=13x^3-455x^2+3502x-5850.
$$


The actual reduced $K$-arc is


$$
R_K=\frac{A_K(\ell^2)}{30L(\ell^2)}=\frac{a_K}{d_K},
$$


where


$$
g_{\rm arc}=90\,5^{\varepsilon_5}19^{\varepsilon_{19}}31^{\varepsilon_{31}},
$$




$$
\varepsilon_5=\mathbf1_{u\equiv1\pmod5},\quad
\varepsilon_{19}=\mathbf1_{u\equiv3\pmod9},\quad
\varepsilon_{31}=\mathbf1_{u\equiv5,7\pmod{15}},
$$


and


$$
a_K=A_K(\ell^2)/g_{\rm arc},\qquad
d_K=30L(\ell^2)/g_{\rm arc}.
$$


In particular, $\gcd(a_K,d_K)=1$.

Write


$$
E_K=E(K),\qquad y_K=d_KE_K-a_K,
$$




$$
\gamma=\gcd(\tau,y_K),\qquad
b^\circ=\gcd(\gamma,a_K),\qquad r^\circ=\gamma/b^\circ.
$$


For every prime,


$$
c_p=\min(v_p(U),v_p(V)),\qquad t_p=v_p(U)-c_p,
$$




$$
z_p=v_p(y_K),\qquad b_p=v_p(b^\circ),\qquad
h_p=v_p(Q_{N-1}^{\rm H}Q_N^{\rm H}).
$$


The complete credit is exactly


$$
\boxed{H_p=h_p+2b_p+2(z_p-t_p)_+.}
$$


No part of this credit is moved to a varying anchor.

We continue the unchanged set


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
$$


Thus $p^2\mid U,V$. Put


$$
r=n-p,\qquad s=r-6=\ell-p,\qquad
a=\frac{p-1}{2},\qquad k=a+1.
$$


The retained boundary calculation gives


$$
\boxed{13\le r<N,\quad s\ge7,\quad r,s\text{ odd},\quad k\le N-6.}
$$


Also $p\nmid d_K$.

Finally,


$$
B_p=(H_p-2)_+,\qquad
e_p=[c_p-2-B_p]_+,\qquad j_p=v_p(J_N^{\rm aff}).
$$



The requested assertion is that $16U$ and the available critical-safe $\zeta_{p,N}$ are not both divisible by


$$
p^{\,4+B_p+j_p}.
$$


The existing chart lemma makes this equivalent to


$$
c_p\le3+B_p+j_p.
$$


Its fixed-$N$ aggregate consequence is reuse, not a new result of this report.

---

## 2. Complete columns and reused lifting data

### 2.1 Both finite forced systems

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
$$


Equivalently, the full affine matrices retain their forcing coordinates:


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
$$



At $x=\ell^2$, let


$$
\begin{aligned}
\mathcal P&=-8x^3-1116x^2-8150x+151,\\
\mathcal Q&=76x^2+2408x+5637,\\
\mathcal F&=4x^2+492x+5463,\\
\mathcal G&=4x^2+556x-3325.
\end{aligned}
$$


Set


$$
\mathscr A=2\ell((2\ell+1)\mathcal Q-\mathcal P),\qquad
\mathscr B=-2\ell\mathcal Q,
$$




$$
\mathscr C_U=\mathcal F-\mathcal P+2\ell\mathcal Q,\qquad
\mathscr C_E=\mathcal G+\mathcal P-2(\ell+1)\mathcal Q.
$$


The corrected columns are


$$
16U=\mathscr C_U-\mathscr A\Theta_\ell-\mathscr B\Theta_{\ell-1},
$$




$$
16E_K=\mathscr C_E+\mathscr A\Phi_\ell+\mathscr B\Phi_{\ell-1}.
$$



At the physical terminal,


$$
V=C_V-P\Theta_n-Q\Theta_{n-1},
$$




$$
E_F=C_F^E-P\Phi_n-Q\Phi_{n-1},
$$


where


$$
P=n\alpha^2+(n-2)\beta^2,
$$




$$
Q=4(n-1)(n-2)\beta^2-2(n-1)\alpha\beta,
$$




$$
\boxed{C_V=\alpha^2+(2n-3)\beta^2-\delta^2,}
$$




$$
\boxed{C_F^E=\alpha^2+(5-2n)\beta^2+4\alpha\beta.}
$$



### 2.2 Six-step transport and determinant data

Let


$$
T_j=\begin{pmatrix}-4j&1\\1&0\end{pmatrix},\qquad
T=T_{\ell+5}\cdots T_\ell.
$$


Starting with $f_0=g_0=0$, use exactly


$$
f_{j+1}=T_{\ell+j}f_j+\binom20,\qquad
g_{j+1}=T_{\ell+j}g_j+\binom{2(-1)^j}{0},
\quad 0\le j\le5.
$$


Then


$$
(\Pi,\Omega)=(P,Q)T,
$$




$$
C^{\rm s}=C_V-(P,Q)f_6,\qquad
C^{\rm e}=C_F^E-(P,Q)g_6,
$$


and


$$
V=C^{\rm s}-\Pi\Theta_\ell-\Omega\Theta_{\ell-1},
$$




$$
E_F=C^{\rm e}-\Pi\Phi_\ell-\Omega\Phi_{\ell-1}.
$$


The last transport step is $\ell+5=n-1$.

Retain


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


The supplied exponential bound


$$
J_N^{\rm aff},\,|\Delta|
<
10^{10}(2N)^{15}\frac{5^{4N}}{g_B^2}
$$


is reused at its stated scope.

### 2.3 The actual anchored defects and quotient systems

The Hermite integers satisfy


$$
P_0^{\rm H}=Q_0^{\rm H}=1,\quad
P_1^{\rm H}=3,\quad Q_1^{\rm H}=1,
$$




$$
Z_{b+1}=(4b+2)Z_b+Z_{b-1},\qquad 1\le b\le N-1.
$$


Put


$$
\chi=2k!.
$$


The actual integral defects are


$$
\sigma_0^+=\frac{\Theta_p-\chi Q_a^{\rm H}}p,\qquad
\sigma_1^+=\frac{\Theta_{p-1}+1+\chi Q_k^{\rm H}}p,
$$




$$
\sigma_0^-=\frac{\Phi_p-\chi P_a^{\rm H}}p,\qquad
\sigma_1^-=\frac{\Phi_{p-1}-1+\chi P_k^{\rm H}}p.
$$



For the residual operator


$$
\mathcal L_jZ=Z_{j+1}+4jZ_j-Z_{j-1},
$$


retain


$$
\mathcal L_j\mathcal A=\mathcal L_j\mathcal B=0,
\quad
(\mathcal A_0,\mathcal A_1)=(1,0),\quad
(\mathcal B_0,\mathcal B_1)=(0,1),
$$


and


$$
\mathcal L_j\mathcal D=-4\mathcal A_j,\quad
\mathcal L_j\mathcal E=-4\mathcal B_j,\quad
\mathcal L_j\mathcal T=-4\Theta_j,\quad
\mathcal L_j\mathcal W=-4\Phi_j.
$$


The seeds of $\mathcal D$ are $(0,-4)$; the other three seed pairs are zero. All residual steps satisfy $1\le j\le r-1$.

The anchored columns are


$$
Z_{0,j}^+
=\chi(\mathcal A_jQ_a^{\rm H}-\mathcal B_jQ_k^{\rm H})+\Theta_j,
$$




$$
Z_{1,j}^+
=\chi(\mathcal D_jQ_a^{\rm H}-\mathcal E_jQ_k^{\rm H})
+\mathcal T_j+\mathcal A_j\sigma_0^++\mathcal B_j\sigma_1^+,
$$




$$
Z_{0,j}^-
=\chi(\mathcal A_jP_a^{\rm H}-\mathcal B_jP_k^{\rm H})-\Phi_j,
$$




$$
Z_{1,j}^-
=\chi(\mathcal D_jP_a^{\rm H}-\mathcal E_jP_k^{\rm H})
-\mathcal W_j+\mathcal A_j\sigma_0^-+\mathcal B_j\sigma_1^-,
$$


with $Z_j^\pm=Z_{0,j}^\pm+pZ_{1,j}^\pm$.

The supplied exact quotient systems are


$$
\Theta_{p+j}=Z_j^++p^2\mathfrak e_j^+,\qquad
\Phi_{p+j}=Z_j^-+p^2\mathfrak e_j^-,
$$




$$
\mathfrak e_0^\pm=0,\qquad \mathfrak e_1^\pm=-4\sigma_0^\pm,
$$




$$
\mathfrak e_{j+1}^\pm+4(p+j)\mathfrak e_j^\pm-\mathfrak e_{j-1}^\pm
=-4Z_{1,j}^\pm.
$$



The already evaluated second corrections have zero seeds and


$$
\mathcal L_j\mathcal D^{\langle2\rangle}=-4\mathcal D_j,\quad
\mathcal L_j\mathcal E^{\langle2\rangle}=-4\mathcal E_j,
$$




$$
\mathcal L_j\mathcal T^{\langle2\rangle}=-4\mathcal T_j,\quad
\mathcal L_j\mathcal W^{\langle2\rangle}=-4\mathcal W_j.
$$


Thus


$$
\begin{aligned}
Y_j^+={}&\mathcal D_j\sigma_0^++\mathcal E_j\sigma_1^+\\
&+\chi(\mathcal D_j^{\langle2\rangle}Q_a^{\rm H}
-\mathcal E_j^{\langle2\rangle}Q_k^{\rm H})
+\mathcal T_j^{\langle2\rangle},
\end{aligned}
$$




$$
\begin{aligned}
Y_j^-={}&\mathcal D_j\sigma_0^-+\mathcal E_j\sigma_1^-\\
&+\chi(\mathcal D_j^{\langle2\rangle}P_a^{\rm H}
-\mathcal E_j^{\langle2\rangle}P_k^{\rm H})
-\mathcal W_j^{\langle2\rangle}.
\end{aligned}
$$


In particular,


$$
\mathcal L_jY^\pm=-4Z_{1,j}^\pm,\qquad
Y_0^\pm=0,\quad Y_1^\pm=-4\sigma_0^\pm.
$$



These third-precision results are reused, not reproved.

---

# Part I. A new arithmetic evaluation of the anchored defects

## 3. Explicit coefficients and the new cubic arithmetic term

All congruences in this part take place in


$$
\mathbb Z_{(p)}=\{x/y\in\mathbb Q:p\nmid y\}.
$$


Every denominator displayed below is a $p$-adic unit.

For $0\le h\le a$, define the integer


$$
\boxed{\mathsf h_{a,h}=\frac{(2a-h)!}{(a-h)!\,h!}.}
$$


For $1\le j\le a$, put


$$
\boxed{\mathsf b_j=\frac{4^j j!((j-1)!)^2}{2(2j)!}.}
$$


The latter quantities are $p$-adic units and can be formed without a division by $p$:


$$
\mathsf b_1=1,\qquad
\mathsf b_{j+1}=\frac{2j^2}{2j+1}\mathsf b_j
\quad(1\le j<a).
$$



Write


$$
H_t^{(d)}=\sum_{v=1}^t\frac1{v^d},\qquad H_0^{(d)}=0.
$$


Here $t\le2a=p-1$, so these are $p$-integral.

For $0\le h\le a$, set


$$
L_{1,h}=\frac32H_h^{(1)}-H_{2h}^{(1)},
$$




$$
L_{2,h}=\frac{15}{4}H_h^{(2)}-3H_{2h}^{(2)},
$$




$$
L_{3,h}=\frac{63}{8}H_h^{(3)}-7H_{2h}^{(3)},
$$


and


$$
E_{2,h}=\frac{L_{1,h}^2+L_{2,h}}2,
$$




$$
E_{3,h}
=\frac{L_{1,h}^3+3L_{1,h}L_{2,h}+2L_{3,h}}6.
$$



The new prime-specific scalar is the **actual** Fermat quotient


$$
q_p(4)=\frac{4^{p-1}-1}{p},
$$


and


$$
\boxed{\mu_p=\frac{q_p(4)-1}{p+1}\in\mathbb Z_{(p)}.}
$$


To obtain $\mu_p\bmod p^3$, the numerator $4^{p-1}-1$ must first be known modulo $p^4$, before its paid division by $p$.

Define the following explicitly evaluated cubic expression:


$$
\boxed{
\mathcal J_{p,h}
=\mu_p+L_{1,h}
+p(E_{2,h}+\mu_pL_{1,h})
+p^2(E_{3,h}+\mu_pE_{2,h}).
}
\tag{3.1}
$$


Finally, put


$$
A_h^+=2h^2-p(2h+1),
$$




$$
\widetilde A_h^-=2h(h-2)-p(2h-1),
$$


and, for the lower half,


$$
A_j^-=2j(j+2)-p(2j+3).
$$



None of these quantities is a newly named source-contact valuation. They are explicit arithmetic coefficients.

---

## 4. New theorem: all four defects modulo $p^3$

### Theorem 4.1

For every original $N$ and every $p\in\mathcal S_N$, the four actual defects satisfy


$$
\boxed{
\begin{aligned}
\sigma_0^+\equiv{}&
\chi\sum_{h=0}^{a}(-1)^h\mathsf h_{a,h}\mathcal J_{p,h}\\
&+\sum_{j=1}^{a}\mathsf b_j
       \bigl(1-p^2H_{j-1}^{(2)}\bigr)
\pmod{p^3},
\end{aligned}}
\tag{4.1}
$$




$$
\boxed{
\begin{aligned}
\sigma_0^-\equiv{}&
\chi\sum_{h=0}^{a}\mathsf h_{a,h}\mathcal J_{p,h}\\
&+\sum_{j=1}^{a}(-1)^{j+1}\mathsf b_j
       \bigl(1-p^2H_{j-1}^{(2)}\bigr)
\pmod{p^3},
\end{aligned}}
\tag{4.2}
$$




$$
\boxed{
\begin{aligned}
\sigma_1^+\equiv\frac1{p-1}\Bigg\{&
1+\chi(Q_k^{\rm H}-2Q_a^{\rm H})\\
&+\chi\sum_{h=0}^{a}(-1)^h
 A_h^+\mathsf h_{a,h}\mathcal J_{p,h}\\
&+\sum_{j=1}^{a}A_j^+\mathsf b_j
       \bigl(1-p^2H_{j-1}^{(2)}\bigr)
\Bigg\}\pmod{p^3},
\end{aligned}}
\tag{4.3}
$$


and


$$
\boxed{
\begin{aligned}
\sigma_1^-\equiv\frac1{p-1}\Bigg\{&
-1+\chi(P_k^{\rm H}-2P_a^{\rm H})\\
&+\chi\sum_{h=0}^{a}
 \widetilde A_h^-\mathsf h_{a,h}\mathcal J_{p,h}\\
&+\sum_{j=1}^{a}(-1)^{j+1}A_j^-\mathsf b_j
       \bigl(1-p^2H_{j-1}^{(2)}\bigr)
\Bigg\}\pmod{p^3}.
\end{aligned}}
\tag{4.4}
$$



Thus all four base defects needed for fourth precision are evaluated without using $\Theta_p,\Theta_{p-1},\Phi_p,\Phi_{p-1}$ on the right-hand sides.

The sums in (4.1)–(4.4) are not unspecified factorial moments: every summand is the displayed integer Hermite coefficient times an explicitly evaluated reciprocal-power polynomial, or the displayed $p$-unit rational coefficient. In particular, the new cubic term is exactly $E_{3,h}+\mu_pE_{2,h}$.

### Proof

#### Step 1: the actual Hermite coefficients

Let


$$
Y_a(x)=\sum_{j=0}^{a}
\frac{(a+j)!}{j!(a-j)!}x^j.
$$


A direct factorial-coefficient identity gives


$$
Y_{a+1}(x)=(4a+2)xY_a(x)+Y_{a-1}(x),
$$


with $Y_0=1$, $Y_1=1+2x$. Consequently,


$$
P_a^{\rm H}=Y_a(1),\qquad
Q_a^{\rm H}=(-1)^aY_a(-1).
$$


Reversing the coefficients gives


$$
\boxed{
P_a^{\rm H}=\sum_{h=0}^{a}\mathsf h_{a,h},\qquad
Q_a^{\rm H}=\sum_{h=0}^{a}(-1)^h\mathsf h_{a,h}.
}
\tag{4.5}
$$



We will also need two weighted evaluations:


$$
\boxed{
\sum_{h=0}^{a}(-1)^h A_h^+\mathsf h_{a,h}
=Q_k^{\rm H}-2pQ_a^{\rm H},
}
\tag{4.6}
$$




$$
\boxed{
\sum_{h=0}^{a}\widetilde A_h^-\mathsf h_{a,h}
=P_k^{\rm H}-2pP_a^{\rm H}.
}
\tag{4.7}
$$



Here is an explicit verification. Put


$$
R_a(z)=\sum_{h=0}^{a}\mathsf h_{a,h}z^h,\qquad
D=z\frac d{dz}.
$$


The coefficient ratios give


$$
D^2R_a-(p+z)DR_a+azR_a=0.
\tag{4.8}
$$


The factorial coefficients also give


$$
Y_{a+1}(x)
=(1+2(a+1)x)Y_a(x)+2x^2Y_a'(x).
$$


Evaluating this at $x=\pm1$, in reversed-coefficient form,


$$
Q_k^{\rm H}=(2p-1)Q_a^{\rm H}-2DR_a(-1),
$$




$$
P_k^{\rm H}=(2p+1)P_a^{\rm H}-2DR_a(1).
$$


Combining these with (4.8) at $z=-1$ and $z=1$ proves (4.6)–(4.7).

These are evaluations in the actual finite Hermite sequence, not in freely chosen endpoint values.

#### Step 2: split the prime-base Chebyshev moment

Let


$$
q(z)=T_p(1-2z).
$$


The exact Chebyshev coefficient formula is


$$
[z^j]q(z)
=(-4)^j\frac{p^2\prod_{v=1}^{j-1}(p^2-v^2)}{(2j)!},
\qquad 1\le j\le p.
$$


Define


$$
w_j=-\frac{j![z^j]q(z)}{2p}.
$$


Then, for $1\le j\le a$,


$$
\boxed{
w_j=p\mathsf b_j
\prod_{v=1}^{j-1}\left(1-\frac{p^2}{v^2}\right).
}
\tag{4.9}
$$


The endpoint moment identities give


$$
\Theta_p=\sum_{j=1}^{p}w_j,\qquad
\Phi_p=\sum_{j=1}^{p}(-1)^{j+1}w_j.
\tag{4.10}
$$



The leading term is exactly


$$
w_p=4^{p-1}(p-1)!.
\tag{4.11}
$$


Moreover,


$$
\frac{w_{j+1}}{w_j}
=\frac{2(j^2-p^2)}{2j+1}.
\tag{4.12}
$$



For $0\le h\le a$, put


$$
R_h(x)=
\prod_{t=1}^{h}
\frac{1-x/(2t-1)}{1-x/t},
\qquad R_0(x)=1.
$$


Backward use of (4.12) yields


$$
w_{p-h}
=(-1)^h\,4^{p-1}(p-1)!
\frac{(2h)!}{4^h(h!)^3}R_h(2p).
\tag{4.13}
$$



On the other hand, since $\chi=(p+1)a!$,


$$
\chi\mathsf h_{a,h}
=(p+1)(p-1)!
\frac{(2h)!}{4^h(h!)^3}R_h(p).
\tag{4.14}
$$


Therefore


$$
\boxed{
w_{p-h}
=(-1)^h\chi\mathsf h_{a,h}
\frac{4^{p-1}}{p+1}\frac{R_h(2p)}{R_h(p)}.
}
\tag{4.15}
$$



Equation (4.15) is the new exact arithmetic normalization. The entire terminal factor $(p-1)!$ cancels between the actual upper-half moment term and its actual Hermite coefficient. This is an algebraic cancellation in the displayed ratio; it is not a claimed divisor of $U,V$, a mixed minor, or the original producer.

#### Step 3: evaluate the normalized factor to cubic order

Fermat’s theorem gives


$$
\frac{4^{p-1}}{p+1}=1+p\mu_p
$$


exactly in $\mathbb Z_{(p)}$.

For $d=1,2,3$,


$$
\log\frac{R_h(2p)}{R_h(p)}
=
\sum_{d\ge1}
\frac{(2^d-1)p^d}{d}
\left(H_h^{(d)}-\sum_{t=1}^{h}(2t-1)^{-d}\right).
$$


This identity is used only as a finite formal expansion through degree three. Since


$$
\sum_{t=1}^{h}(2t-1)^{-d}
=H_{2h}^{(d)}-2^{-d}H_h^{(d)},
$$


the first three coefficients are precisely $L_{1,h},L_{2,h},L_{3,h}$. Thus


$$
\frac{R_h(2p)}{R_h(p)}
\equiv
1+pL_{1,h}+p^2E_{2,h}+p^3E_{3,h}
\pmod{p^4}.
$$


It follows that


$$
\boxed{
\frac{
\displaystyle\frac{4^{p-1}}{p+1}
\frac{R_h(2p)}{R_h(p)}-1
}{p}
\equiv\mathcal J_{p,h}\pmod{p^3}.
}
\tag{4.16}
$$



Every division here is paid:

- $q_p(4)$ is integral by Fermat’s theorem;
- the numerator in (4.16) is divisible by $p$;
- $p+1$, $t$, $2t-1$, $2$, and $6$ are units at the present primes.

For the lower half, (4.9) gives


$$
\frac{w_j}{p}
\equiv
\mathsf b_j(1-p^2H_{j-1}^{(2)})
\pmod{p^3}.
\tag{4.17}
$$



Combining (4.5), (4.10), (4.15)–(4.17) proves (4.1)–(4.2).

#### Step 4: retain and evaluate both neighboring base defects

The identity


$$
T_{p-1}(1-2z)
=(1-2z)q(z)-\frac2p z(1-z)q'(z)
$$


and the two factorial functionals give


$$
\boxed{
\Theta_{p-1}+1
=\frac{p+\sum_{j=1}^{p}A_j^+w_j}{p-1},
}
\tag{4.18}
$$




$$
\boxed{
\Phi_{p-1}-1
=\frac{-p+\sum_{j=1}^{p}(-1)^{j+1}A_j^-w_j}{p-1}.
}
\tag{4.19}
$$


For the upper half,


$$
A_{p-h}^+=A_h^+,\qquad
A_{p-h}^-=\widetilde A_h^-.
$$


Substitute (4.15) into (4.18)–(4.19), add the respective anchors
$\chi Q_k^{\rm H}$, $\chi P_k^{\rm H}$, and use (4.6)–(4.7).
After the paid division by $p$, the constant terms are respectively


$$
\frac{1+\chi(Q_k^{\rm H}-2Q_a^{\rm H})}{p-1},
\qquad
\frac{-1+\chi(P_k^{\rm H}-2P_a^{\rm H})}{p-1}.
$$


Equations (4.16)–(4.17) now give (4.3)–(4.4). ∎

### 4.1 Exact higher-precision version

The proof also gives an exact formula, before truncation. Replace $\mathcal J_{p,h}$ in (4.1)–(4.4) by


$$
\frac{
\displaystyle\frac{4^{p-1}}{p+1}
\frac{R_h(2p)}{R_h(p)}-1
}{p},
$$


and replace


$$
\mathsf b_j(1-p^2H_{j-1}^{(2)})
$$


by


$$
\mathsf b_j\prod_{v=1}^{j-1}\left(1-\frac{p^2}{v^2}\right).
$$


The resulting four formulas are exact identities in $\mathbb Z_{(p)}$, equal to the original integer defects.

For arbitrary precision, this exact product form is preferable to extending a logarithmic expansion through degrees whose factorial denominators might contain $p$. It supplies no nonvanishing theorem, but its division and precision requirements are unambiguous.

---

# Part II. The complete fourth source and endpoint digit

## 5. An evaluated integer kernel

For $m\ge0$, define


$$
\boxed{
\mathcal K_m(x)
=
\sum_{v=0}^{\lfloor m/2\rfloor}
\binom{m-v}{v}(-4)^{m-2v}
(x+v+1)_{m-2v},
}
\tag{5.1}
$$


where $(x)_d=x(x+1)\cdots(x+d-1)$. Set $\mathcal K_{-1}=0$.

These are integer polynomials. No factorial denominator in a binomial coefficient is inverted modulo $p$: the binomial coefficient is first its ordinary integer value.

They satisfy


$$
\mathcal K_0=1,\qquad \mathcal K_1=-4(x+1),
$$




$$
\boxed{
\mathcal K_m(x)
=-4(x+m)\mathcal K_{m-1}(x)+\mathcal K_{m-2}(x).
}
\tag{5.2}
$$



For completeness, (5.2) follows coefficientwise from Pascal’s identity. For a fixed $v$, after taking out the common rising factorial, the required scalar identity reduces to


$$
v\binom{m-1-v}{v}
=(m-2v)\binom{m-1-v}{v-1},
$$


including the boundary term by its usual zero convention.

Thus $\mathcal K_{j-t-1}(p+t)$ is the exact impulse kernel from a forcing at residual step $t$ to state $j$.

---

## 6. New theorem: the cubic remainder of both quotient systems

### Theorem 6.1

For $0\le j\le r$, the actual states satisfy the exact identities


$$
\boxed{
\Theta_{p+j}
=
Z_j^++p^2Y_j^+
-4p^3\sum_{t=1}^{j-1}
\mathcal K_{j-t-1}(p+t)Y_t^+,
}
\tag{6.1}
$$




$$
\boxed{
\Phi_{p+j}
=
Z_j^-+p^2Y_j^-
-4p^3\sum_{t=1}^{j-1}
\mathcal K_{j-t-1}(p+t)Y_t^-.
}
\tag{6.2}
$$


Empty sums are zero. Consequently, modulo $p^4$, the kernels in these sums may be replaced by $\mathcal K_{j-t-1}(t)$.

### Proof

The reused equations give


$$
\mathcal L_jY^\pm=-4Z_{1,j}^\pm.
$$


Therefore, for the shifted operator,


$$
Y_{j+1}^\pm+4(p+j)Y_j^\pm-Y_{j-1}^\pm
=-4Z_{1,j}^\pm+4pY_j^\pm.
$$


Subtracting from the exact equation for $\mathfrak e^\pm$,


$$
(\mathfrak e-Y)_{j+1}^\pm
+4(p+j)(\mathfrak e-Y)_j^\pm
-(\mathfrak e-Y)_{j-1}^\pm
=-4pY_j^\pm.
$$


Both initial differences are zero. The integer impulse kernel (5.1) therefore gives


$$
\mathfrak e_j^\pm-Y_j^\pm
=-4p\sum_{t=1}^{j-1}
\mathcal K_{j-t-1}(p+t)Y_t^\pm.
$$


Substitute this in the exact anchored state identities. ∎

This result does not introduce another contact valuation. It explicitly resolves the next forcing term of the existing quotient systems. The forcing still contains the actual $\sigma^\pm$, which Theorem 4.1 now evaluates to the precision required here.

All shifted steps end at


$$
p+r-1=n-1.
$$



---

## 7. All four complete columns modulo $p^4$

Put, as in the supplied third-digit calculation,


$$
B_U=\mathscr C_U-\mathscr A Z_s^+-\mathscr B Z_{s-1}^+,
$$




$$
B_V=C_V-PZ_r^+-QZ_{r-1}^+.
$$


For the evaluated row kernels, set


$$
W_{U,t}
=\mathscr A\mathcal K_{s-t-1}(t)
+\mathscr B\mathcal K_{s-t-2}(t),
\qquad 1\le t\le s-1,
$$




$$
W_{V,t}
=P\mathcal K_{r-t-1}(t)
+Q\mathcal K_{r-t-2}(t),
\qquad 1\le t\le r-1.
$$


Here $\mathcal K_{-1}=0$ handles the last terms exactly.

Theorem 6.1 yields


$$
\boxed{
\begin{aligned}
16U\equiv{}&
B_U-p^2(\mathscr A Y_s^++\mathscr B Y_{s-1}^+)\\
&+4p^3\sum_{t=1}^{s-1}W_{U,t}Y_t^+
\pmod{p^4},
\end{aligned}}
\tag{7.1}
$$




$$
\boxed{
\begin{aligned}
V\equiv{}&
B_V-p^2(PY_r^++QY_{r-1}^+)\\
&+4p^3\sum_{t=1}^{r-1}W_{V,t}Y_t^+
\pmod{p^4}.
\end{aligned}}
\tag{7.2}
$$



Both endpoint columns are, at the same precision,


$$
\boxed{
\begin{aligned}
16E_K\equiv{}&
\mathscr C_E+\mathscr A Z_s^-+\mathscr B Z_{s-1}^-\\
&+p^2(\mathscr A Y_s^-+\mathscr B Y_{s-1}^-)\\
&-4p^3\sum_{t=1}^{s-1}W_{U,t}Y_t^-
\pmod{p^4},
\end{aligned}}
\tag{7.3}
$$




$$
\boxed{
\begin{aligned}
E_F\equiv{}&
C_F^E-PZ_r^--QZ_{r-1}^-\\
&-p^2(PY_r^-+QY_{r-1}^-)\\
&+4p^3\sum_{t=1}^{r-1}W_{V,t}Y_t^-
\pmod{p^4}.
\end{aligned}}
\tag{7.4}
$$



In particular, the square source still contains $-\delta^2$, and the square endpoint still contains $4\alpha\beta$.

### 7.1 The evaluated fourth source digit after an actual third collision

Suppose the reused third source digit vanishes, so that


$$
p^3\mid U,V.
$$


Only under that hypothesis are the following divisions by $p^3$ used:


$$
\boxed{
\begin{aligned}
\frac{16U}{p^3}\equiv{}&
\frac{B_U-p^2(\mathscr A Y_s^++\mathscr B Y_{s-1}^+)}{p^3}\\
&+4\sum_{t=1}^{s-1}W_{U,t}Y_t^+
\pmod p,
\end{aligned}}
\tag{7.5}
$$




$$
\boxed{
\begin{aligned}
\frac{V}{p^3}\equiv{}&
\frac{B_V-p^2(PY_r^++QY_{r-1}^+)}{p^3}\\
&+4\sum_{t=1}^{r-1}W_{V,t}Y_t^+
\pmod p.
\end{aligned}}
\tag{7.6}
$$


Their numerators must first be formed modulo $p^4$. Their divisibility by $p^3$ follows from (7.1)–(7.2) and the actual third collision.

Together with Theorem 4.1 and the explicit kernel (5.1), these formulas evaluate the fourth digit in the original objects. They do not leave an undefined fourth correction sequence or an unevaluated factorial functional.

If the pair (7.5)–(7.6) is nonzero, then


$$
\boxed{c_p=3,\qquad e_p=[1-B_p]_+\le1.}
\tag{7.7}
$$


This implication is rigorous. Universal nonvanishing of the pair is not established.

---

## 8. The same fourth precision in the exact critical-safe charts

Let


$$
\mathbf t_j=\binom{\Theta_j}{\Theta_{j-1}},\qquad
\mathbf f_j=\binom{\Phi_j}{\Phi_{j-1}},
$$




$$
\mathsf M_c=
\begin{pmatrix}\mathscr A&\mathscr B\\ \Pi&\Omega\end{pmatrix},
\qquad
\mathbf C=\binom{\mathscr C_U}{C^{\rm s}},
\qquad
\mathbf u=\binom{16U}{V}.
$$


Retain the actual columns


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
$$


Then


$$
\mathbf E=\mathsf M_c(\mathbf f_\ell+\mathbf f_s).
$$



The actual mixed minors are


$$
\mathfrak A_{p,N}=\det(\mathbf R,\mathbf u),\qquad
\mathfrak B_{p,N}=\det(\mathbf u,\mathbf E).
$$


The supplied chart lemma gives


$$
\min(v_p(R_1),v_p(E_1))=0,
$$


and permits the exact choice


$$
\zeta_{p,N}=
\begin{cases}
\mathfrak A_{p,N},&p\nmid R_1,\\
\mathfrak B_{p,N},&p\mid R_1.
\end{cases}
$$


It yields


$$
c_p-2
=
\min\left(v_p(16U/p^2),v_p(\zeta_{p,N}/p^2)\right).
$$


This remains valid at determinant-critical primes.

### 8.1 Residual-source chart

Here the actual additive formula is


$$
\begin{aligned}
\zeta_{p,N}={}&
\mathscr I_1(\Theta_s-\Theta_\ell)
+\mathscr I_2(\Theta_{s-1}-\Theta_{\ell-1})\\
&+\Delta(\Theta_s\Theta_{\ell-1}
-\Theta_{s-1}\Theta_\ell).
\end{aligned}
\tag{8.1}
$$


Substitution of (6.1) at $j=s,s-1$, with its explicit cubic kernel, evaluates this entire expression modulo $p^4$. Neither $\mathscr I_i$ nor $\Delta$ is divided.

### 8.2 Endpoint chart: the full additive difference

Define, as in the supplied mixed identity,


$$
\Lambda_\sigma=
P_k^{\rm H}\sigma_0^+
+P_a^{\rm H}\sigma_1^+
-Q_k^{\rm H}\sigma_0^-
-Q_a^{\rm H}\sigma_1^-,
$$




$$
\Xi_\sigma=\sigma_1^+\sigma_0^--\sigma_0^+\sigma_1^-.
$$


Because $s$ is odd, the mixed forcing return is


$$
\mathfrak f_{s;p}
=
-\sum_{t=1}^{s-1}(-1)^t
\bigl(\Theta_t\Phi_{p+t}+\Phi_t\Theta_{p+t}\bigr).
$$


Consequently the full endpoint-chart difference, at the new precision, is


$$
\boxed{
\begin{aligned}
\zeta_{p,N}\equiv{}&
R_1E_2-R_2E_1\\
&-\Delta\Bigg[
2(-1)^a\chi^2+p\chi\Lambda_\sigma+p^2\Xi_\sigma\\
&\qquad\quad
-4p\sum_{t=1}^{s-1}(-1)^t
\Bigl\{
\Theta_t(Z_t^-+p^2Y_t^-)
+\Phi_t(Z_t^++p^2Y_t^+)
\Bigr\}
\Bigg]
\pmod{p^4}.
\end{aligned}}
\tag{8.2}
$$


The endpoint factors $E_1,E_2$ in the first line are evaluated by the complete formulas (7.3)–(7.4).

Thus (8.2) includes:

- both actual defect pairs, now evaluated by Theorem 4.1;
- the entire mixed forcing return to the required precision;
- both complete endpoint constants;
- the exact source/endpoint subtraction;
- determinant-critical primes, without inverting $\Delta$.

The cubic state terms are unnecessary inside the sum in (8.2), because that sum is multiplied by $p$ and is required only modulo $p^3$. They are not discarded from the source or endpoint columns themselves.

---

# Part III. Precision, force, and the remaining obstruction

## 9. Precision before division

The necessary working precision must be selected before any quotient is taken.

### 9.1 Fourth precision

For (7.1)–(8.2), a sufficient consistent bill is:

- actual divided Gaussian coefficients modulo $p^4$;
- Hermite data at $a,k$ modulo $p^4$;
- actual defects $\sigma^\pm\bmod p^3$, supplied by Theorem 4.1;
- $Z_{0,j}^\pm\bmod p^4$;
- $Z_{1,j}^\pm\bmod p^3$;
- $Y_j^\pm\bmod p^2$;
- the cubic kernel contraction only modulo $p$.

If $a_G=v_p(g_B)$, then:

- to form a divided linear Gaussian quantity modulo $p^4$, its actual numerator is required modulo $p^{a_G+4}$, followed by division by the proved $p^{a_G}$ and the actual unit part of $g_B$;
- if a raw quadratic Gaussian column is formed and divided afterwards, it is required modulo
  

$$
\boxed{p^{\,2a_G+4}}
$$


  before division by $g_B^2$.

A raw square test modulo $p^4$ is not a divided square test when $a_G>0$.

### 9.2 The assigned modulus may be larger

The actual target modulus is


$$
p^{\mathsf d},\qquad \mathsf d=4+B_p+j_p.
$$


When $\mathsf d>4$, the fourth-digit formulas alone do not decide the assigned assertion.

At that precision:

1. Use the exact product version of Theorem 4.1.
2. Form its normalized product numerator modulo $p^{\mathsf d}$ before the paid division by $p$, obtaining $\sigma^\pm\bmod p^{\mathsf d-1}$.
3. Use the exact identities (6.1)–(6.2), with $\mathcal K_m(p+t)$, rather than their fourth-precision truncations.
4. Form the complete divided Gaussian columns modulo $p^{\mathsf d}$. A raw quadratic route requires $p^{2a_G+\mathsf d}$.
5. Use the exact chart identities without determinant inversion.

Any deeper determination of $B_p$ must use the actual $h_p,b_p,z_p,t_p$. A calculation modulo $p^4$ does not determine a valuation that continues beyond its modulus.

### 9.3 What has and has not been paid

The new harmonic denominators are units. The Hermite coefficient quotients are first ordinary integers. The continuants are integer polynomials. The only new nonunit division is the explicitly paid division by $p$ in the Fermat quotient or in the normalized factor.

There is no new division by:

- $\Delta$;
- a terminal factorial;
- a residual factorial;
- a coefficient content presumed to divide a numerical value;
- a hypothetical mixed common divisor.

---

## 10. Why this does not yet prove saturation

The new arithmetic calculation removes a specific ambiguity: the four anchored defects cannot be varied independently. Their cubic digits obey (4.1)–(4.4), including the same actual Fermat quotient and the displayed signed Hermite weights.

That constraint is not, by itself, nonvanishing of (7.5)–(7.6).

After a third collision, the unresolved fourth-depth cancellation is between:

1. the actual Gaussian carries
   

$$
\frac{B_U-p^2(\mathscr A Y_s^++\mathscr B Y_{s-1}^+)}{p^3},
   \qquad
   \frac{B_V-p^2(PY_r^++QY_{r-1}^+)}{p^3},
$$


   formed with the divided $\alpha,\beta,\delta$; and

2. the explicitly evaluated cubic forcing contractions in (7.5)–(7.6), whose base defects now have the arithmetic evaluation of Theorem 4.1.

Nothing proved here prevents both differences from vanishing.

In particular:

- no assumption that $q_p(4)$, $\mu_p$, or a harmonic expression is a unit has been made;
- even a unit coefficient of a next digit would not exclude its exceptional deeper child;
- the turn17 original-index splitting theorem is not applicable merely because a prime occurs here;
- its arc, Gaussian-unit, and non-Wieferich hypotheses have not been established on $\mathcal S_N$.

Also, at a fixed prime $p$, at most one original $N$ lies in $N<p<2N$, because successive original indices differ by $3^{64}>2$. Fixed-prime index counts therefore do not supply aggregate interval coverage.

### 10.1 Concrete follow-on lemma

The first new nonvanishing problem is now the following.

> **Cubic-harmonic fourth-depth separation — open.**  
> Let $N$ be original and $p\in\mathcal S_N$, with $B_p=j_p=0$. Suppose the admitted third source digit vanishes. Substitute the explicit defect formulas (4.1)–(4.4) into the two actual signed quotient systems and into (7.5)–(7.6). Prove that the resulting pair is nonzero modulo $p$, using the actual divided Gaussian row and its complete constant $C_V$.

This is the zero-credit, determinant-unit portion of the requested one-extra-depth assertion, now with the previously opaque base digits arithmetically evaluated. For $B_p+j_p>0$, the corresponding nonvanishing is required at the larger modulus specified in Section 9.2.

The lemma is not asserted to be true on the strength of a unit slope, coefficient resultant, or formal recurrence classification.

### 10.2 Aggregate status

The first two paid layers and the conditional implication


$$
e_p\le1+j_p
\quad\Longrightarrow\quad
\prod_{p\in\mathcal S_N}p^{e_p}
\mid J_N^{\rm aff}\binom{2N}{N}
$$


remain reuse.

The new fourth-digit evaluation would certify $e_p\le1$ at every prime where its pair is nonzero. No quantitatively significant coverage of such primes has been proved. Hence no new $O(N)$ bound for


$$
\sum_{p\in\mathcal S_N}e_p\log p
$$


is booked.

---

## 11. Reused primitive mixed-height obstruction

For completeness, the actual mixed normalization remains


$$
d_{\rm mix}
=\gcd(\mathfrak D_{s;p},\mathfrak A_{p,N},\mathfrak B_{p,N}),
$$




$$
A_{\rm mix}=\mathfrak A_{p,N}/d_{\rm mix},\quad
B_{\rm mix}=\mathfrak B_{p,N}/d_{\rm mix},\quad
D_{\rm mix}=\mathfrak D_{s;p}/d_{\rm mix}.
$$


It is the least simultaneous clearer of the two mixed ratios, not the original two-arc clearer.

The supplied theorem gives, pointwise on its stated original scope,


$$
\max(|A_{\rm mix}|,|B_{\rm mix}|)
\ge N^{(p-1)/2}e^{-16N},
$$




$$
D_{\rm mix}\ge N^{(p-1)/2}e^{-28N},
$$


and $p\nmid D_{\rm mix}$.

These results, the finite Hermite separation, and the mixed chart lemma are reused without repeating their proofs. The different audit described as pending in the assignment is not represented as completed here.

The new digit evaluation does not restore the disproved expectation that the actual primitive mixed pair has exponential height. Nor does the existence of a small real mixed quotient pay the arithmetic height of an aggregate.

---

# Part IV. Preservation of the original producer

## 12. Complete source, endpoint, and Hermite returns

The source balance is unchanged:


$$
\begin{aligned}
&(\nu\mathscr A-16\tau\Pi)\Theta_\ell
+(\nu\mathscr B-16\tau\Omega)\Theta_{\ell-1}\\
&\hspace{12mm}=\nu\mathscr C_U-16\tau C^{\rm s}.
\end{aligned}
$$


For


$$
T_{\rm end}=\tau(E_F-\delta^2)+\nu E_K,
$$


the endpoint balance remains


$$
\begin{aligned}
16T_{\rm end}={}&
16\tau(C^{\rm e}-\delta^2)+\nu\mathscr C_E\\
&+(\nu\mathscr A-16\tau\Pi)\Phi_\ell
+(\nu\mathscr B-16\tau\Omega)\Phi_{\ell-1}.
\end{aligned}
$$



The source return has


$$
z_\ell^{\rm ret}=16\Omega U-\mathscr B V,\qquad
z_{\ell-1}^{\rm ret}=\mathscr A V-16\Pi U,
$$




$$
z_j^{\rm ret}=-\Delta\Theta_j+\varrho_j,
$$




$$
\varrho_\ell=\mathscr I_2,\qquad
\varrho_{\ell-1}=-\mathscr I_1,
$$




$$
\varrho_{j-1}=\varrho_{j+1}+4j\varrho_j-2\Delta.
$$



After the actual arc clearing below, let


$$
k_E=D\mathscr C_E-16DR_K,\qquad
f_E=DC^{\rm e}-DR_F.
$$


The endpoint return has


$$
w_\ell=16\Omega Y+\mathscr B X,\qquad
w_{\ell-1}=-16\Pi Y-\mathscr A X,
$$




$$
w_j=D\Delta\Phi_j+\sigma_j^{\rm ret},
$$




$$
\sigma_\ell^{\rm ret}=\Omega k_E+\mathscr Bf_E,\qquad
\sigma_{\ell-1}^{\rm ret}=-\Pi k_E-\mathscr Af_E,
$$




$$
\sigma_{j-1}^{\rm ret}
=\sigma_{j+1}^{\rm ret}+4j\sigma_j^{\rm ret}
+2D\Delta(-1)^j.
$$


The complete determinant identity is


$$
z_\ell^{\rm ret}w_{\ell-1}
-z_{\ell-1}^{\rm ret}w_\ell
=-16\Delta(UX+VY).
$$


There is no division by $\Delta$.

For exactly $0\le b\le N$, the canonical returns remain


$$
\mathcal R_{b;N}=d_KP_b^{\rm H}U+Q_b^{\rm H}y_K.
$$


With


$$
\Psi_j^{(b)}=Q_b^{\rm H}\Phi_j-P_b^{\rm H}\Theta_j,
$$


their forcing is


$$
\Psi_{j+1}^{(b)}+4j\Psi_j^{(b)}-\Psi_{j-1}^{(b)}
=2\bigl(Q_b^{\rm H}(-1)^j-P_b^{\rm H}\bigr),
$$


and


$$
\begin{aligned}
16\mathcal R_{b;N}
={}&d_K\bigl(
P_b^{\rm H}\mathscr C_U+Q_b^{\rm H}\mathscr C_E
+\mathscr A\Psi_\ell^{(b)}
+\mathscr B\Psi_{\ell-1}^{(b)}
\bigr)\\
&-16Q_b^{\rm H}a_K.
\end{aligned}
$$


In particular, the retained signs and product payment are


$$
\mathcal R_{N-1;N}<0<\mathcal R_{N;N},
$$




$$
\frac{c(r^\circ)^2}{\kappa_N^{\rm prod}}
\mid
\mathcal R_{N-1;N}\mathcal R_{N;N},
$$


with


$$
v_p(\kappa_N^{\rm prod})=[c_p-H_p]_+.
$$


The endpoint credit remains at $N-1,N$, not at $a,k$.

The old rational interface keeps its own paid clearers


$$
Q_{\rm loc}(n)=\prod_{b=0}^{12}(n-b),\qquad
\mathcal L_n=\operatorname{lcm}(1,\ldots,n),
$$


and


$$
\frac{2\mathcal L_n}{j^2-1}
=\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}.
$$


Neither is substituted for the least arc clearer.

---

## 13. Both reduced arcs and the actual primitive denominator

Retain


$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


The monic quotient degrees are at most $2N-2$.

The square-arc return has zero seeds at $0,1$, and, through the original physical terminal,


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


Its output is


$$
R_F=
\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}-2\alpha\beta\xi_{n-1}}2.
$$


No recurrence step above $n-1$ is used.

After reducing both arcs completely,


$$
\boxed{
D=\operatorname{lcm}(\operatorname{den}R_F,\operatorname{den}R_K).
}
$$


Then


$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$


Independently reduce


$$
\tau R_F+\nu R_K=\frac b\lambda,\qquad
\gcd(b,\lambda)=1,\quad \lambda>0.
$$


Set


$$
E=\tau E_F+\nu E_K,\qquad A=\lambda E-b,
$$




$$
\boxed{G=\gcd(M,A),}
$$


where the gcd is over **all primes**, and


$$
\boxed{p_N=A/G,\qquad q_N=\lambda M/G.}
$$


Since $\gcd(\lambda,A)=1$, this is the actual primitive pair.

No mixed clearer, local modulus, harmonic denominator, or coefficient gcd replaces $D,\lambda,G$, or $q_N$.

---

## 14. The nonzero whole error at the same original indices

The original polynomial is still


$$
P_N(t)=\frac{F(t)^2+(V/U)K(t)}{\delta^2}
=\frac{W_{\rm prim}(t)}M.
$$


Its complete error is


$$
\boxed{
\epsilon_N=
\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0.
}
$$


Both terms in the weight are retained.

The exact source balance gives


$$
\eta(W_{\rm prim})=M,
$$


so finite integration by parts and both arcs give


$$
\epsilon_N=e+\pi-\frac{A}{\lambda M}.
$$


Therefore, at the same original indices,


$$
\boxed{
q_N(e+\pi)-p_N=q_N\epsilon_N>0.
}
$$



The retained rational enclosure is


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


and, with $j_b=(1-4b^2)^{-1}$,


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
q_NJ_N=\frac{\lambda_N}{G_N}
\bigl(\tau_NJ_F+\nu_NJ_K\bigr).
}
$$


Both positive summands remain. No assertion about the size of this whole expression follows from the new local digit calculation.

---

## 15. Proof-status and computation ledger

| Statement | Status |
|---|---|
| Original index domain, physical terminal, Gaussian division, actual content | Retained |
| Complete corrected columns and six-step forcing transport | Reuse at stated scope |
| Anchored lift, both signed quotient systems, complete third digit | Reuse |
| Mixed chart lemma, finite Hermite separation, primitive mixed-height obstruction | Reuse; no repeated proof |
| Exact upper-half normalization against actual Hermite coefficients, (4.15) | **New proved identity** |
| Explicit cubic normalized factor, (3.1), (4.16) | **New proved arithmetic evaluation** |
| All four actual defects modulo $p^3$, (4.1)–(4.4) | **New proved evaluation** |
| Explicit integer kernel and resolved cubic quotient term, (6.1)–(6.2) | **New proved identity** |
| Complete source and endpoint columns modulo $p^4$ | **New proved evaluation** |
| Nonzero fourth source pair implies $c_p=3$, $e_p\le1$ | Proved implication |
| Universal fourth-pair nonvanishing | Open |
| One-extra-depth assertion $c_p\le3+B_p+j_p$ | Not proved or refuted |
| Absolute paid depth cap $e_p\le C+j_p$ | Not proved |
| Quantitatively significant aggregate coverage | Not proved |
| Primary interval mass $O(N)$ | Open |
| Smaller-prime and $p>2N$ obligations | Separate and open |
| Actual $D,\lambda,G,q_N$, and positive whole error | Retained unchanged |
| Producer retirement or a decision about $e+\pi$ | Not established |

### Computation status

No computation is indispensable to the new proofs. Their inputs are the displayed Chebyshev coefficient identity, finite Hermite coefficient identities, and exact forced recurrences. Their outputs are derived symbolically above.

Accordingly, no original-sized matrix calculation, prime scan, old source table, $p=23$ receipt, or optional constant check is requested.

A finite evaluation at selected pairs could establish only those finite values. It could not establish the infinite original-family saturation assertion.

---

# Final conclusion

The new result is an explicit fourth-precision arithmetic evaluation in the unchanged original objects.

The key additional step is not another contact variable. It is the exact normalization


$$
w_{p-h}
=(-1)^h\chi\mathsf h_{a,h}
\frac{4^{p-1}}{p+1}\frac{R_h(2p)}{R_h(p)},
$$


followed by its evaluated cubic expansion. This ties all four actual anchored defects to the same actual Fermat quotient and explicit signed Hermite weights. Together with the evaluated integer kernel, it determines the full fourth source and endpoint digits, including the exact additive mixed-chart difference and all forcing terms.

The remaining bottleneck is numerical noncoincidence in those actual expressions: after the admitted lower collisions, can the complete Gaussian carries and the newly evaluated cubic forcing contractions both cancel at depth


$$
4+B_p+j_p?
$$


No argument given here excludes that cancellation, and no original-family discrepancy has been produced. Thus the primary interval mass is still unpaid.

The all-prime final gcd, actual primitive denominator, both reduced arcs, and strictly positive whole error remain unchanged at


$$
N=9^{18+32u}.
$$


No unconditional proof or disproof of irrationality of $e+\pi$, and no retirement of this producer, follows from the present result.
