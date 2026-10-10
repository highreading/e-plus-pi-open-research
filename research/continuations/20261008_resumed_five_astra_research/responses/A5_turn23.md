> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Eliminating the common Fermat quotient from the fourth-depth source collision

## Abstract and outcome

The cubic-harmonic fourth-depth separation lemma is **not proved or refuted in this report**. In particular, no original-family counterexample is produced, and no unconditional bound


$$
e_p\le C+j_p
$$


with a fixed absolute $C$, or quantitatively significant fixed-$N$ coverage theorem, is claimed.

There is, however, a concrete elimination that was not carried out in FULL22.

The four evaluated defects can be recombined so that the **same actual scalar**


$$
\rho_p=\frac{4^{p-1}}{p+1}
$$


appears in all four prime-base states. Substitution into the complete source columns gives an exact equation


$$
\boxed{\binom{16U}{V}=\mathbf d_{p,N}-\rho_p\mathbf v_{p,N}.}
$$


Both vectors on the right are explicitly evaluated using the Hermite coefficients, the exact upper- and lower-half products, the original forced transports, and the **actual divided Gaussian coefficients**. In particular, the constant $-\delta^2$ is present in $\mathbf d_{p,N}$.

This leads to the following new conclusions.

1. The explicit Fermat factor can be eliminated from one complete source constraint:
   

$$
\boxed{\mathscr Z_{p,N}
   :=\det(\mathbf v_{p,N},\mathbf d_{p,N})
   =\det\!\left(\mathbf v_{p,N},\binom{16U}{V}\right).}
$$


   A fully evaluated cubic formula for $\mathscr Z_{p,N}\bmod p^4$ is given below. It contains no occurrence of $q_p(4)$ or $\mu_p$.

2. On the assigned branch $j_p=0$, a component of $\mathbf v_{p,N}$ is a unit. This is proved in the original objects from the adjacent Hermite determinant and the actual determinant condition; it is not an extra Gaussian-unit or Fermat-quotient hypothesis.

3. After an actual third collision, the fourth source pair is an explicitly invertible linear transformation of:
   - the fourth digit of the evaluated, Fermat-free compatibility value $\mathscr Z_{p,N}$; and
   - one congruence between the actual Fermat quotient and an explicitly evaluated target determined by the complete Gaussian source columns.

4. A sufficient all-prime rational clearer for the cubic compatibility expression is proved. Its factorial division is justified term by term and is **not** a division of $U,V$, or of the mixed invariant.

These statements resolve the **eliminability question**, but not the required numerical noncoincidence. The remaining issue is stated precisely in Section 10. No conclusion about the rationality or irrationality of $e+\pi$, and no retirement of the original producer, follows.

No numerical computation is performed or requested.

---

## 1. Original objects and exact scope

Throughout,


$$
\boxed{N=9^{18+32u}=3^{36+64u},\qquad u\in\mathbb Z_{\ge0},}
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


with


$$
C_0=1,\qquad C_1=2t-1,\qquad
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
\eta(H)=\sum_j j![z^j]H(1-z),\qquad
E(H)=\sum_j(-1)^j j![t^j]H(t).
$$


Put


$$
\mathcal H=t(1-t)(1+t^2)^2,\qquad K=\mathcal H C_m^2,
$$




$$
U=-\eta(K),\qquad V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
$$


The actual content and primitive source normalization are unchanged:


$$
\operatorname{cont}(W_{\rm raw})=g_B^2c,
$$




$$
\tau=U/c,\qquad \nu=V/c,\qquad
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2.
$$


The retained original-domain results give $U,V,M>0$.

### 1.1 The reduced $K$-arc and complete credit

Let


$$
L(x)=(x-1)(x-9)(x-25),\qquad
A_K(x)=13x^3-455x^2+3502x-5850.
$$


The actual reduction is


$$
R_K=\frac{A_K(\ell^2)}{30L(\ell^2)}=\frac{a_K}{d_K},
\qquad \gcd(a_K,d_K)=1,
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
c_p=\min(v_p(U),v_p(V)),\qquad
t_p=v_p(U)-c_p,
$$




$$
z_p=v_p(y_K),\qquad b_p=v_p(b^\circ),\qquad
h_p=v_p(Q_{N-1}^{\rm H}Q_N^{\rm H}).
$$


The complete credit is


$$
\boxed{H_p=h_p+2b_p+2(z_p-t_p)_+.}
$$


It remains attached to the actual Hermite endpoints $N-1,N$.

We retain the original set


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


No converse identification of this set from its necessary source congruences is used. In particular, membership retains the original block condition.

For $p\in\mathcal S_N$, set


$$
r=n-p,\qquad s=\ell-p=r-6,\qquad
a=\frac{p-1}{2},\qquad k=a+1,\qquad \chi=2k!.
$$


The retained boundary result is


$$
\boxed{13\le r<N,\qquad s\ge7,\qquad r,s\text{ odd},\qquad k\le N-6.}
$$


Also


$$
p^2\mid U,V,\qquad p\nmid d_K.
$$



Finally,


$$
B_p=(H_p-2)_+,\qquad
e_p=[c_p-2-B_p]_+,\qquad
j_p=v_p(J_N^{\rm aff}).
$$



The primary case is


$$
B_p=j_p=0,\qquad p^3\mid U,V.
$$


The required conclusion is


$$
\left(\frac{16U}{p^3},\frac V{p^3}\right)\not\equiv(0,0)\pmod p.
$$



---

## 2. Complete finite columns being used

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


Thus the two affine forcing coordinates are respectively $1$ and $(-1)^j$; neither system is replaced by its homogeneous part.

At $x=\ell^2$, put


$$
\begin{aligned}
\mathcal P&=-8x^3-1116x^2-8150x+151,\\
\mathcal Q&=76x^2+2408x+5637,\\
\mathcal F&=4x^2+492x+5463,\\
\mathcal G&=4x^2+556x-3325,
\end{aligned}
$$


and


$$
\mathscr A=2\ell((2\ell+1)\mathcal Q-\mathcal P),\qquad
\mathscr B=-2\ell\mathcal Q,
$$




$$
\mathscr C_U=\mathcal F-\mathcal P+2\ell\mathcal Q,\qquad
\mathscr C_E=\mathcal G+\mathcal P-2(\ell+1)\mathcal Q.
$$


The centered columns are


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



For the unchanged six-step transport, let


$$
T_j=\begin{pmatrix}-4j&1\\1&0\end{pmatrix},\qquad
T=T_{\ell+5}\cdots T_\ell.
$$


Starting from $f_0=g_0=0$, use


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
C^{\rm e}=C_F^E-(P,Q)g_6.
$$


Consequently,


$$
V=C^{\rm s}-\Pi\Theta_\ell-\Omega\Theta_{\ell-1},
$$




$$
E_F=C^{\rm e}-\Pi\Phi_\ell-\Omega\Phi_{\ell-1}.
$$



Define


$$
\mathsf M_c=
\begin{pmatrix}\mathscr A&\mathscr B\\ \Pi&\Omega\end{pmatrix},
\qquad
\mathbf C=\binom{\mathscr C_U}{C^{\rm s}},
\qquad
\mathbf u=\binom{16U}{V},
$$


and retain


$$
\Delta=\det\mathsf M_c<0,
$$




$$
\mathscr I_1=\Pi\mathscr C_U-\mathscr A C^{\rm s},\qquad
\mathscr I_2=\Omega\mathscr C_U-\mathscr B C^{\rm s},
$$




$$
J_N^{\rm aff}=\gcd(\mathscr I_1,\mathscr I_2)>0.
$$


In particular,


$$
\operatorname{adj}(\mathsf M_c)\mathbf C
=\binom{\mathscr I_2}{-\mathscr I_1}.
$$



The supplied bound


$$
J_N^{\rm aff},|\Delta|
<
10^{10}(2N)^{15}\frac{5^{4N}}{g_B^2}
$$


is retained at its stated scope. It is not used below to infer a valuation bound for a different numerical expression.

---

## 3. Recombining all four evaluated defects

This section uses the exact product evaluation established in FULL22. It does not rederive that evaluation.

All quantities in this section lie in $\mathbb Z_{(p)}$.

For $0\le h\le a$, let


$$
\mathsf h_{a,h}=\frac{(2a-h)!}{(a-h)!\,h!},
$$


and for $1\le j\le a$, let


$$
\mathsf b_j=\frac{4^j j!((j-1)!)^2}{2(2j)!}.
$$


Define the exact products


$$
\mathsf S_{p,h}
=
\prod_{t=1}^{h}
\frac{(1-2p/(2t-1))(1-p/t)}
     {(1-2p/t)(1-p/(2t-1))},
$$




$$
\mathsf T_{p,j}
=
\prod_{v=1}^{j-1}\left(1-\frac{p^2}{v^2}\right).
$$


Empty products are $1$. All their displayed denominators are $p$-adic units.

Retain the weights


$$
A_h^+=2h^2-p(2h+1),
$$




$$
\widetilde A_h^-=2h(h-2)-p(2h-1),
$$




$$
A_j^-=2j(j+2)-p(2j+3).
$$



The actual common scalar is


$$
\boxed{\rho_p=\frac{4^{p-1}}{p+1}=1+p\mu_p,}
\qquad
\mu_p=\frac{q_p(4)-1}{p+1}.
$$



### 3.1 Explicit upper- and lower-half vectors

Define


$$
\boxed{
\mathbf A_p^+
=
\chi
\binom{
\displaystyle\sum_{h=0}^{a}(-1)^h\mathsf h_{a,h}\mathsf S_{p,h}
}{
\displaystyle\frac1{p-1}
\sum_{h=0}^{a}(-1)^hA_h^+\mathsf h_{a,h}\mathsf S_{p,h}
},
}
\tag{3.1}
$$




$$
\boxed{
\mathbf A_p^-
=
\chi
\binom{
\displaystyle\sum_{h=0}^{a}\mathsf h_{a,h}\mathsf S_{p,h}
}{
\displaystyle\frac1{p-1}
\sum_{h=0}^{a}\widetilde A_h^-\mathsf h_{a,h}\mathsf S_{p,h}
}.
}
\tag{3.2}
$$



The lower-half vectors, including their complete constants, are


$$
\boxed{
\mathbf L_p^+
=
\binom{
\displaystyle p\sum_{j=1}^{a}\mathsf b_j\mathsf T_{p,j}
}{
\displaystyle
\frac{1+p\sum_{j=1}^{a}A_j^+\mathsf b_j\mathsf T_{p,j}}{p-1}
},
}
\tag{3.3}
$$




$$
\boxed{
\mathbf L_p^-
=
\binom{
\displaystyle p\sum_{j=1}^{a}(-1)^{j+1}\mathsf b_j\mathsf T_{p,j}
}{
\displaystyle
\frac{-1+p\sum_{j=1}^{a}(-1)^{j+1}A_j^-\mathsf b_j\mathsf T_{p,j}}{p-1}
}.
}
\tag{3.4}
$$



The constants $+1$ and $-1$ in the second coordinates are indispensable.

### Proposition 3.1 — Exact common-factor form of the four prime-base states

In the original finite systems,


$$
\boxed{
\binom{\Theta_p}{\Theta_{p-1}}
=\rho_p\mathbf A_p^++\mathbf L_p^+,
\qquad
\binom{\Phi_p}{\Phi_{p-1}}
=\rho_p\mathbf A_p^-+\mathbf L_p^-.
}
\tag{3.5}
$$



#### Proof

The exact FULL22 normalized factor is


$$
\frac{\rho_p\mathsf S_{p,h}-1}{p}
=
\frac{\mathsf S_{p,h}-1}{p}+\mu_p\mathsf S_{p,h}.
$$


Insert this into the four exact defect formulas.

For the first coordinates, use


$$
Q_a^{\rm H}=\sum_h(-1)^h\mathsf h_{a,h},
\qquad
P_a^{\rm H}=\sum_h\mathsf h_{a,h}.
$$


The anchor and the $-1$ in the normalized factor combine to give precisely the upper sums in (3.1)–(3.2), multiplied by $\rho_p$.

For the neighboring coordinates, use the already established weighted identities


$$
\sum_h(-1)^h A_h^+\mathsf h_{a,h}
=Q_k^{\rm H}-2pQ_a^{\rm H},
$$




$$
\sum_h\widetilde A_h^-\mathsf h_{a,h}
=P_k^{\rm H}-2pP_a^{\rm H}.
$$


After substituting


$$
\Theta_{p-1}=-1-\chi Q_k^{\rm H}+p\sigma_1^+,
$$


the constant numerator left over is $+1$. After substituting


$$
\Phi_{p-1}=1-\chi P_k^{\rm H}+p\sigma_1^-,
$$


it is $-1$. The remaining terms are exactly (3.3)–(3.4). ∎

This proposition is a recombination of the **evaluated actual defects**. It does not replace them by independent variables or arbitrary base states.

---

## 4. Substitution into all four complete columns

For $0\le j\le r$, define the shifted homogeneous transport and both forced returns by


$$
S_0=I,\qquad \mathbf h_0^+=\mathbf h_0^-=0,
$$




$$
S_{j+1}=T_{p+j}S_j,
$$




$$
\mathbf h_{j+1}^+
=T_{p+j}\mathbf h_j^++\binom20,
$$




$$
\boxed{
\mathbf h_{j+1}^-
=T_{p+j}\mathbf h_j^--\binom{2(-1)^j}{0}.
}
\tag{4.1}
$$


The minus sign in the last line follows from $p$ being odd.

No new continuant identity is needed. The already evaluated FULL22 kernel gives, for $j\ge1$,


$$
S_j=
\begin{pmatrix}
\mathcal K_j(p-1)&\mathcal K_{j-1}(p)\\
\mathcal K_{j-1}(p-1)&\mathcal K_{j-2}(p)
\end{pmatrix},
$$


and


$$
\mathbf h_j^+
=
2\sum_{t=0}^{j-1}
\binom{\mathcal K_{j-t-1}(p+t)}
      {\mathcal K_{j-t-2}(p+t)},
$$




$$
\mathbf h_j^-
=
-2\sum_{t=0}^{j-1}(-1)^t
\binom{\mathcal K_{j-t-1}(p+t)}
      {\mathcal K_{j-t-2}(p+t)}.
$$


Here $\mathcal K_{-1}=0$, and every $\mathcal K$ is the explicit integer polynomial from FULL22.

Linearity of the two original forced systems now gives


$$
\boxed{
\binom{\Theta_{p+j}}{\Theta_{p+j-1}}
=
\rho_pS_j\mathbf A_p^+
+S_j\mathbf L_p^+
+\mathbf h_j^+,
}
\tag{4.2}
$$




$$
\boxed{
\binom{\Phi_{p+j}}{\Phi_{p+j-1}}
=
\rho_pS_j\mathbf A_p^-
+S_j\mathbf L_p^-
+\mathbf h_j^-.
}
\tag{4.3}
$$



Consequently the complete source columns are


$$
\boxed{
16U=
\mathscr C_U
-(\mathscr A,\mathscr B)
\bigl(\rho_pS_s\mathbf A_p^+
      +S_s\mathbf L_p^++\mathbf h_s^+\bigr),
}
\tag{4.4}
$$




$$
\boxed{
V=
\alpha^2+(2n-3)\beta^2-\delta^2
-(P,Q)
\bigl(\rho_pS_r\mathbf A_p^+
      +S_r\mathbf L_p^++\mathbf h_r^+\bigr).
}
\tag{4.5}
$$


Both endpoint columns are


$$
\boxed{
16E_K=
\mathscr C_E
+(\mathscr A,\mathscr B)
\bigl(\rho_pS_s\mathbf A_p^-
      +S_s\mathbf L_p^-+\mathbf h_s^-\bigr),
}
\tag{4.6}
$$




$$
\boxed{
E_F=
\alpha^2+(5-2n)\beta^2+4\alpha\beta
-(P,Q)
\bigl(\rho_pS_r\mathbf A_p^-
      +S_r\mathbf L_p^-+\mathbf h_r^-\bigr).
}
\tag{4.7}
$$



These are exact identities, not merely congruences. They retain the divided Gaussian coefficients and all four constants.

The largest shifted step is


$$
p+r-1=n-1.
$$


No Hermite index above $k\le N-6$ has been introduced by this substitution.

### 4.1 The exact two-source equation

Set


$$
S=S_s,\qquad \mathbf h=\mathbf h_s^+,
$$


and define


$$
\boxed{
\mathbf v_{p,N}=\mathsf M_cS\mathbf A_p^+,
}
\tag{4.8}
$$




$$
\boxed{
\mathbf d_{p,N}
=\mathbf C-\mathsf M_c(S\mathbf L_p^++\mathbf h).
}
\tag{4.9}
$$


Then


$$
\boxed{\mathbf u=\mathbf d_{p,N}-\rho_p\mathbf v_{p,N}.}
\tag{4.10}
$$



The vector $\mathbf d_{p,N}$ contains the actual $-\delta^2$ through $C^{\rm s}$. Thus (4.10) is not an elimination in a free Gaussian quadratic form.

---

## 5. A validated pivot and exact Fermat elimination

### 5.1 Primitivity in the original objects

Modulo $p$, the exact products satisfy $\mathsf S_{p,h}\equiv1$. Hence


$$
\mathbf A_p^+
\equiv\chi\binom{Q_a^{\rm H}}{-Q_k^{\rm H}},
\qquad
\mathbf A_p^-
\equiv\chi\binom{P_a^{\rm H}}{-P_k^{\rm H}}.
\tag{5.1}
$$


The adjacent Hermite determinant is


$$
P_k^{\rm H}Q_a^{\rm H}-P_a^{\rm H}Q_k^{\rm H}
=2(-1)^a.
$$


It follows directly from the stated Hermite recurrence: the determinant changes sign at each step and has initial value $2$.

Therefore


$$
\boxed{
\det(\mathbf A_p^+,\mathbf A_p^-)
\equiv-2(-1)^a\chi^2\pmod p.
}
\tag{5.2}
$$


Since $k<p$, the right side is a unit. In particular, $\mathbf A_p^+$ is primitive over $\mathbb Z_{(p)}$.

Every $T_j$ has determinant $-1$, and $s$ is odd, so


$$
\det S=-1.
$$


Consequently, with


$$
\mathbf v^-_{p,N}=\mathsf M_cS\mathbf A_p^-,
$$


we have


$$
\boxed{
\det(\mathbf v_{p,N},\mathbf v^-_{p,N})
\equiv2(-1)^a\chi^2\Delta\pmod p.
}
\tag{5.3}
$$



More generally, put


$$
\lambda_p=\min(v_p(v_1),v_p(v_2)).
$$


Then


$$
\boxed{\lambda_p\le v_p(\Delta)\le j_p.}
\tag{5.4}
$$


Indeed,


$$
\operatorname{adj}(\mathsf M_c)\mathbf v
=\Delta S\mathbf A_p^+,
$$


and $S\mathbf A_p^+$ is primitive. If both components of $\mathbf v$ were divisible by $p^{v_p(\Delta)+1}$, this equality would be impossible.

Thus, on the primary branch $j_p=0$, at least one actual component $v_i$ is a unit. No unit assumption about $q_p(4)$, $\mu_p$, $\alpha$, $\beta$, or $\delta$ has been inserted.

### 5.2 The Fermat-free compatibility value

Define the actual numerical rational


$$
\boxed{
\mathscr Z_{p,N}
=\det(\mathbf v_{p,N},\mathbf d_{p,N}).
}
\tag{5.5}
$$


Equation (4.10) gives the exact identity


$$
\boxed{
\mathscr Z_{p,N}
=\det(\mathbf v_{p,N},\mathbf u).
}
\tag{5.6}
$$


The explicitly singled-out Fermat factor has disappeared completely.

This is a numerical-value identity. It is not a claim that a coefficient resultant bounds the valuation of its evaluation.

Suppose now that $j_p=0$, and choose $i\in\{1,2\}$ with $p\nmid v_i$. Since multiplication by a matrix with unit determinant preserves the minimum valuation of a vector,


$$
\boxed{
c_p
=
\min\left(
v_p\!\left(\frac{d_i}{v_i}-\rho_p\right),
v_p(\mathscr Z_{p,N})
\right).
}
\tag{5.7}
$$


For example, when $i=1$,


$$
\mathscr Z_{p,N}=v_1u_2-v_2u_1,
$$


so the map


$$
(u_1,u_2)\longmapsto(u_1,\mathscr Z_{p,N})
$$


has unit determinant $v_1$.

### 5.3 The exact remaining Fermat-quotient target

The first source collision implies


$$
d_i/v_i\equiv\rho_p\equiv1\pmod p.
$$


Therefore the following quotient is integral in $\mathbb Z_{(p)}$:


$$
\boxed{
q^*_{p,N;i}
=
\frac{(p+1)d_i-v_i}{p\,v_i}.
}
\tag{5.8}
$$


It is completely determined by (3.1)–(3.4), the original forced transports, and the actual divided Gaussian columns.

Since


$$
u_i
=-\frac{p\,v_i}{p+1}
\bigl(q_p(4)-q^*_{p,N;i}\bigr),
$$


equation (5.7) becomes


$$
\boxed{
c_p=
\min\left(
1+v_p(q_p(4)-q^*_{p,N;i}),
v_p(\mathscr Z_{p,N})
\right).
}
\tag{5.9}
$$



This target is not freely chosen. Conversely, its being an actual target does not prove that the actual Fermat quotient avoids it.

### Theorem 5.1 — Exact fourth-depth reduction after an actual third collision

Assume


$$
p\in\mathcal S_N,\qquad B_p=j_p=0,\qquad p^3\mid U,V.
$$


Then


$$
q_p(4)-q^*_{p,N;i}\in p^2\mathbb Z_{(p)},
\qquad
\mathscr Z_{p,N}\in p^3\mathbb Z_{(p)}.
$$


Define


$$
\mathfrak q_{p,N;i}
=\frac{q_p(4)-q^*_{p,N;i}}{p^2}\pmod p,
$$




$$
\mathfrak z_{p,N}
=\frac{\mathscr Z_{p,N}}{p^3}\pmod p.
$$


If $i=1$, then


$$
\boxed{
\binom{16U/p^3}{V/p^3}
\equiv
\binom{
-\dfrac{v_1}{p+1}\mathfrak q_{p,N;1}
}{
-\dfrac{v_2}{p+1}\mathfrak q_{p,N;1}
+\dfrac{\mathfrak z_{p,N}}{v_1}
}
\pmod p.
}
\tag{5.10}
$$


If $i=2$, then


$$
\boxed{
\binom{16U/p^3}{V/p^3}
\equiv
\binom{
-\dfrac{v_1}{p+1}\mathfrak q_{p,N;2}
-\dfrac{\mathfrak z_{p,N}}{v_2}
}{
-\dfrac{v_2}{p+1}\mathfrak q_{p,N;2}
}
\pmod p.
}
\tag{5.11}
$$



In either case the displayed transformation has unit determinant. Hence


$$
\boxed{
\left(\frac{16U}{p^3},\frac V{p^3}\right)\not\equiv(0,0)
\iff
(\mathfrak q_{p,N;i},\mathfrak z_{p,N})\not\equiv(0,0).
}
\tag{5.12}
$$



#### Proof

The divisibilities follow from (5.9) and the assumed third collision. Equations (5.10)–(5.11) follow from the exact formula for $u_i$ and


$$
\mathscr Z=v_1u_2-v_2u_1.
$$


Their determinants are $-1/(p+1)$, a unit. ∎

This theorem is an exact reduction of the actual problem. It is **not** a nonvanishing theorem.

---

## 6. Evaluating the Fermat-free compatibility through fourth precision

The compatibility value in (5.5) can be evaluated without retaining a named, unevaluated determinant of prime-base states.

Let


$$
H_t^{(d)}=\sum_{v=1}^t v^{-d},
$$


and reuse the FULL22 coefficients


$$
L_{1,h}=\frac32H_h^{(1)}-H_{2h}^{(1)},
$$




$$
L_{2,h}=\frac{15}{4}H_h^{(2)}-3H_{2h}^{(2)},
$$




$$
L_{3,h}=\frac{63}{8}H_h^{(3)}-7H_{2h}^{(3)},
$$




$$
E_{2,h}=\frac{L_{1,h}^2+L_{2,h}}2,
\qquad
E_{3,h}
=\frac{L_{1,h}^3+3L_{1,h}L_{2,h}+2L_{3,h}}6.
$$


Write


$$
H_{0,h}=1,\qquad H_{1,h}=L_{1,h},\qquad
H_{2,h}=E_{2,h},\qquad H_{3,h}=E_{3,h}.
$$



For $0\le d\le3$, define the explicitly evaluated vectors


$$
\mathbf A_d^+
=
\chi
\binom{
\displaystyle\sum_{h=0}^{a}(-1)^h\mathsf h_{a,h}H_{d,h}
}{
\displaystyle\frac1{p-1}
\sum_{h=0}^{a}(-1)^hA_h^+\mathsf h_{a,h}H_{d,h}
},
\tag{6.1}
$$




$$
\mathbf A_d^-
=
\chi
\binom{
\displaystyle\sum_{h=0}^{a}\mathsf h_{a,h}H_{d,h}
}{
\displaystyle\frac1{p-1}
\sum_{h=0}^{a}\widetilde A_h^-\mathsf h_{a,h}H_{d,h}
}.
\tag{6.2}
$$


For the lower halves, put


$$
\mathbf B_0^+
=
\binom{
\displaystyle\sum_{j=1}^{a}\mathsf b_j
}{
\displaystyle\frac1{p-1}\sum_{j=1}^{a}A_j^+\mathsf b_j
},
\qquad
\mathbf B_2^+
=
\binom{
\displaystyle\sum_{j=1}^{a}\mathsf b_jH_{j-1}^{(2)}
}{
\displaystyle\frac1{p-1}\sum_{j=1}^{a}A_j^+\mathsf b_jH_{j-1}^{(2)}
},
\tag{6.3}
$$


and


$$
\mathbf B_0^-
=
\binom{
\displaystyle\sum_{j=1}^{a}(-1)^{j+1}\mathsf b_j
}{
\displaystyle\frac1{p-1}\sum_{j=1}^{a}(-1)^{j+1}A_j^-\mathsf b_j
},
$$




$$
\mathbf B_2^-
=
\binom{
\displaystyle\sum_{j=1}^{a}(-1)^{j+1}\mathsf b_jH_{j-1}^{(2)}
}{
\displaystyle\frac1{p-1}\sum_{j=1}^{a}(-1)^{j+1}A_j^-\mathsf b_jH_{j-1}^{(2)}
}.
\tag{6.4}
$$



The established product expansions give


$$
\boxed{
\mathbf A_p^\pm
\equiv\mathbf A_0^\pm+p\mathbf A_1^\pm
+p^2\mathbf A_2^\pm+p^3\mathbf A_3^\pm
\pmod{p^4},
}
\tag{6.5}
$$




$$
\boxed{
\mathbf L_p^\pm
\equiv
\pm\frac1{p-1}\binom01
+p\mathbf B_0^\pm-p^3\mathbf B_2^\pm
\pmod{p^4}.
}
\tag{6.6}
$$



### 6.1 An explicit scalar formula

Let


$$
\mathbf w=\binom{\mathscr I_2}{-\mathscr I_1}.
$$


Since $\det S=-1$, elementary determinant algebra gives


$$
\begin{aligned}
\mathscr Z_{p,N}
&=\det(\mathsf M_cS\mathbf A_p^+,
        \mathbf C-\mathsf M_c(S\mathbf L_p^++\mathbf h))\\
&=\boxed{
\det(S\mathbf A_p^+,\mathbf w-\Delta\mathbf h)
+\Delta\det(\mathbf A_p^+,\mathbf L_p^+).
}
\end{aligned}
\tag{6.7}
$$


No division by $\Delta$ occurs.

For complete scalar evaluation, write $S=(s_{ij})$, $\mathbf h=(h_1,h_2)^t$, and set


$$
\begin{aligned}
t_1^{\rm elim}
={}&s_{11}(-\mathscr I_1-\Delta h_2)
-s_{21}(\mathscr I_2-\Delta h_1)
+\frac{\Delta}{p-1},\\
t_2^{\rm elim}
={}&s_{12}(-\mathscr I_1-\Delta h_2)
-s_{22}(\mathscr I_2-\Delta h_1).
\end{aligned}
\tag{6.8}
$$


Thus the linear expression


$$
\mathcal T(X_1,X_2)
=t_1^{\rm elim}X_1+t_2^{\rm elim}X_2
$$


is completely specified by the actual Gaussian column, the original shifted transport, and its full positive forcing return.

Define


$$
\begin{aligned}
Z_0={}&\mathcal T(\mathbf A_0^+),\\
Z_1={}&\mathcal T(\mathbf A_1^+)
       +\Delta\det(\mathbf A_0^+,\mathbf B_0^+),\\
Z_2={}&\mathcal T(\mathbf A_2^+)
       +\Delta\det(\mathbf A_1^+,\mathbf B_0^+),\\
Z_3={}&\mathcal T(\mathbf A_3^+)
       +\Delta\det(\mathbf A_2^+,\mathbf B_0^+)
       -\Delta\det(\mathbf A_0^+,\mathbf B_2^+).
\end{aligned}
\tag{6.9}
$$



### Theorem 6.1 — Evaluated cubic compatibility

For every original $N$ and $p\in\mathcal S_N$,


$$
\boxed{
\mathscr Z_{p,N}
\equiv Z_0+pZ_1+p^2Z_2+p^3Z_3\pmod{p^4}.
}
\tag{6.10}
$$



#### Proof

Insert (6.5)–(6.6) into (6.7).

The constant part of $\mathbf L_p^+$ contributes


$$
\frac{\Delta}{p-1}(\mathbf A_p^+)_1,
$$


which is already included in $t_1^{\rm elim}$.

The remaining determinant is


$$
\Delta\det\!\left(
\sum_{d=0}^3p^d\mathbf A_d^+,
p\mathbf B_0^+-p^3\mathbf B_2^+
\right).
$$


Collecting terms below $p^4$ gives exactly (6.9). ∎

Every summand in (6.9) is evaluated by the displayed Hermite coefficients, reciprocal-power sums, and integer continuants. No $\Theta_p,\Theta_{p-1},\Phi_p,\Phi_{p-1}$, undefined correction sequence, or Fermat quotient remains in this compatibility expression.

### 6.2 The additive carry is not $Z_3$ alone

The quantities $Z_0,Z_1,Z_2,Z_3$ depend on the actual $p,N$. They are **not base-$p$ digits**.

After an actual third collision, the correct fourth compatibility digit is


$$
\boxed{
\mathfrak z_{p,N}
\equiv
\frac{Z_0+pZ_1+p^2Z_2+p^3Z_3}{p^3}\pmod p.
}
\tag{6.11}
$$


The whole numerator must first be formed modulo $p^4$. Its divisibility by $p^3$ follows from (5.6) and the actual third collision.

Replacing (6.11) by $Z_3\bmod p$ would discard the lower-order additive carry and would be invalid.

---

## 7. A proved local clearing bill

This section supplies an all-prime integrality statement for the new cubic expression. It supplies no exponential numerator-height theorem.

Let


$$
\mathcal L_{p-1}=\operatorname{lcm}(1,\ldots,p-1).
$$



### Lemma 7.1

For $1\le j\le a$, the reduced denominator of $\mathsf b_j$ divides $\mathcal L_{p-1}$.

#### Proof

For an odd prime $q$, a possible denominator valuation is


$$
v_q((2j)!)-v_q(j!)-2v_q((j-1)!).
$$


At each power $q^d$, its contribution is


$$
\left\lfloor\frac{2j}{q^d}\right\rfloor
-\left\lfloor\frac j{q^d}\right\rfloor
-2\left\lfloor\frac{j-1}{q^d}\right\rfloor.
$$


Write $j=Aq^d+r$, $0\le r<q^d$.

If $r>0$, the contribution is


$$
\left\lfloor\frac{2r}{q^d}\right\rfloor-A\le1.
$$


If $r=0$, it is $2-A\le1$. Contributions vanish above $q^d>2j$. Hence the denominator exponent is at most


$$
\lfloor\log_q(2j)\rfloor\le\lfloor\log_q(p-1)\rfloor.
$$



At $q=2$, the factor $4^j/2=2^{2j-1}$ pays any possible denominator contribution; the same floor estimate suffices. Thus the denominator divides $\mathcal L_{p-1}$. ∎

The harmonic expressions have sufficient denominator bounds


$$
L_{1,h}:\ 2\mathcal L_{p-1},\qquad
E_{2,h}:\ 8\mathcal L_{p-1}^2,\qquad
E_{3,h}:\ 48\mathcal L_{p-1}^3.
$$


The second coordinate of every upper or lower vector introduces just the additional factor $p-1$, which divides $\mathcal L_{p-1}$.

Let


$$
\mathscr Z_{p,N}^{[4]}=Z_0+pZ_1+p^2Z_2+p^3Z_3
$$


as an exact rational expression.

### Proposition 7.2 — Paid integrality of the cubic certificate



$$
\boxed{
\mathcal Z_{p,N}
=
\frac{48\mathcal L_{p-1}^{\,4}}{\chi}\,
\mathscr Z_{p,N}^{[4]}
\in\mathbb Z.
}
\tag{7.1}
$$


Moreover,


$$
p\nmid 48\mathcal L_{p-1}^{\,4}\chi.
$$



#### Proof

Every $\mathbf A_d^+$ contains the displayed factor $\chi$, and (6.9) is linear in these vectors. Thus the division by $\chi$ is justified term by term.

For $\mathcal T(\mathbf A_d^+)/\chi$, a sufficient denominator is $48\mathcal L_{p-1}^4$: the first coordinate encounters at most one additional $p-1$, and the second coordinate already contains that factor.

For the determinant terms, the worst cases are


$$
\det(\mathbf A_2^+,\mathbf B_0^+)/\chi,
\qquad
\det(\mathbf A_0^+,\mathbf B_2^+)/\chi.
$$


In each product only one second-coordinate denominator occurs. Lemma 7.1 and the harmonic bounds again give a divisor of $48\mathcal L_{p-1}^4$.

Finally, $p>3$, all entries of the lcm are below $p$, and $k<p$. ∎

This division by $\chi$ is **not** an assertion that $\chi$ divides $U,V$, either mixed minor, or the original producer. It is a proved common factor of this newly displayed linear expression.

As a pointwise consequence, an actual third collision gives $p^3\mid\mathcal Z_{p,N}$, and


$$
p^4\nmid\mathcal Z_{p,N}\quad\Longrightarrow\quad c_p=3.
$$


No nonvanishing or coverage of this certificate has been established.

The lcm in (7.1) is a sufficient local clearer, not an actual least original clearer. An exponential denominator bill alone does not bound the numerator, and $\mathcal Z_{p,N}$ depends on $p$. It is therefore **not** the requested fixed-$N$, exponential-height aggregate certificate.

---

## 8. The endpoint chart retains its full additive difference

Define


$$
\mathbf t_j=\binom{\Theta_j}{\Theta_{j-1}},\qquad
\mathbf f_j=\binom{\Phi_j}{\Phi_{j-1}},
$$




$$
\mathbf R=\mathbf C-\mathsf M_c\mathbf t_s,
$$


and


$$
\mathbf E=
\binom{
16E_K-\mathscr C_E+\mathscr A\Phi_s+\mathscr B\Phi_{s-1}
}{
C^{\rm e}-E_F+\Pi\Phi_s+\Omega\Phi_{s-1}
}.
$$


The complete endpoint columns give


$$
\mathbf E=\mathsf M_c(\mathbf f_\ell+\mathbf f_s).
$$



The actual mixed minors remain


$$
\mathfrak A_{p,N}=\det(\mathbf R,\mathbf u),\qquad
\mathfrak B_{p,N}=\det(\mathbf u,\mathbf E).
$$


The supplied safe-chart result is reused at its stated scope:


$$
\min(v_p(R_1),v_p(E_1))=0,
$$




$$
\zeta_{p,N}=
\begin{cases}
\mathfrak A_{p,N},&p\nmid R_1,\\
\mathfrak B_{p,N},&p\mid R_1.
\end{cases}
$$


It gives


$$
c_p-2=
\min\left(v_p(16U/p^2),v_p(\zeta_{p,N}/p^2)\right).
$$



The residual-source formula remains


$$
\begin{aligned}
\mathfrak A_{p,N}={}&
\mathscr I_1(\Theta_s-\Theta_\ell)
+\mathscr I_2(\Theta_{s-1}-\Theta_{\ell-1})\\
&+\Delta(\Theta_s\Theta_{\ell-1}
-\Theta_{s-1}\Theta_\ell).
\end{aligned}
\tag{8.1}
$$



For the endpoint chart, retain


$$
\Lambda_\sigma=
P_k^{\rm H}\sigma_0^+
+P_a^{\rm H}\sigma_1^+
-Q_k^{\rm H}\sigma_0^-
-Q_a^{\rm H}\sigma_1^-,
$$




$$
\Xi_\sigma=\sigma_1^+\sigma_0^--\sigma_0^+\sigma_1^-,
$$


and the whole mixed forcing return


$$
\mathfrak f_{s;p}
=
-\sum_{t=1}^{s-1}(-1)^t
\bigl(\Theta_t\Phi_{p+t}+\Phi_t\Theta_{p+t}\bigr).
$$


Then


$$
\mathfrak D_{s;p}
=
2(-1)^a\chi^2+p\chi\Lambda_\sigma
+p^2\Xi_\sigma+4p\mathfrak f_{s;p},
$$


and the exact additive difference is


$$
\boxed{
\mathfrak B_{p,N}
=
R_1E_2-R_2E_1
-\Delta\left(
2(-1)^a\chi^2+p\chi\Lambda_\sigma
+p^2\Xi_\sigma+4p\mathfrak f_{s;p}
\right).
}
\tag{8.2}
$$



Equations (3.5), (4.2), and (4.3) substitute the evaluated four defects and both forced systems into every term of (8.2). Nothing is divided by $\Delta$.

### 8.1 Why the apparent quadratic Fermat constraint is not an extra equation

Put


$$
\mathbf E_0
=\mathsf M_c(S\mathbf L_p^-+\mathbf h_s^-+\mathbf f_s).
$$


Then


$$
\mathbf E=\mathbf E_0+\rho_p\mathbf v^-_{p,N}.
$$


Therefore


$$
\begin{aligned}
\mathfrak B_{p,N}
={}&\det(\mathbf d,\mathbf E_0)\\
&+\rho_p\bigl(
\det(\mathbf d,\mathbf v^-)
-\det(\mathbf v,\mathbf E_0)
\bigr)
-\rho_p^2\det(\mathbf v,\mathbf v^-).
\end{aligned}
\tag{8.3}
$$


Its quadratic coefficient is nonzero modulo $p$ when $j_p=0$, by (5.3). That fact does **not** establish nonvanishing of the evaluated quadratic.

Indeed, if $v_1$ is a unit, the exact source elimination gives


$$
\mathfrak A_{p,N}
=
\left(\frac{R_1v_2}{v_1}-R_2\right)u_1
+\frac{R_1}{v_1}\mathscr Z_{p,N},
\tag{8.4}
$$




$$
\boxed{
\mathfrak B_{p,N}
=
\left(E_2-\frac{E_1v_2}{v_1}\right)u_1
-\frac{E_1}{v_1}\mathscr Z_{p,N}.
}
\tag{8.5}
$$


Thus, after the complete first source equation is imposed, the endpoint-chart equation reduces to the same compatibility value. It supplies no additional independent restriction on the actual Fermat quotient.

This is the precise obstruction to treating the four defect formulas as four independent source constraints. Their shared Fermat quotient can be eliminated, but the endpoint identity does not generate a third independent source condition.

### 8.2 The actual mixed normalization is not changed

Retain


$$
d_{\rm mix}
=\gcd(\mathfrak D_{s;p},\mathfrak A_{p,N},\mathfrak B_{p,N}),
$$




$$
A_{\rm mix}=\mathfrak A_{p,N}/d_{\rm mix},\qquad
B_{\rm mix}=\mathfrak B_{p,N}/d_{\rm mix},\qquad
D_{\rm mix}=\mathfrak D_{s;p}/d_{\rm mix}.
$$


This is the actual least simultaneous clearer of the two mixed ratios.

The FULL21 bounds


$$
\max(|A_{\rm mix}|,|B_{\rm mix}|)
\ge N^{(p-1)/2}e^{-16N},
$$




$$
D_{\rm mix}\ge N^{(p-1)/2}e^{-28N}
$$


are reused at their stated scope, without repeating their proof or representing pending different review as completed.

They prohibit assigning exponential height to those same primitive mixed ratios. They do not automatically prove a height theorem, upper or lower, for the different expression $\mathcal Z_{p,N}$.

---

## 9. Higher credit, determinant-critical primes, and precision before division

The actual target remains


$$
\boxed{p^{\mathsf d},\qquad \mathsf d=4+B_p+j_p.}
$$



### 9.1 A critical-safe version of the new elimination

The bound


$$
\lambda_p\le v_p(\Delta)\le j_p
$$


was proved in (5.4).

If $c_p<\lambda_p$, then the desired upper bound is already automatic. Otherwise $c_p\ge\lambda_p$, and


$$
\mathbf v'=\mathbf v/p^{\lambda_p},\qquad
\mathbf d'=\mathbf d/p^{\lambda_p}
$$


are legitimate $p$-integral vectors: integrality of $\mathbf d'$ follows from


$$
\mathbf d=\mathbf u+\rho_p\mathbf v.
$$


At least one $v'_i$ is a unit. Therefore


$$
\boxed{
c_p=\lambda_p+
\min\left(
v_p\!\left(d'_i/v'_i-\rho_p\right),
v_p\det(\mathbf v',\mathbf d')
\right).
}
\tag{9.1}
$$



This uses only paid powers of $p$, not division by $\Delta$. If $c_p\ge\lambda_p+1$, one can also define the integral quotient


$$
q^{*\prime}_{p,N;i}
=\frac{(p+1)d'_i-v'_i}{p\,v'_i}
$$


and obtain the corresponding Fermat-quotient version of (9.1).

For the original chart test, determinant-critical primes still use the supplied safe choice of $\zeta_{p,N}$. The full additive endpoint difference (8.2) remains the relevant integer identity.

### 9.2 Required numerator moduli

Every division must be preceded by sufficient numerator precision.

**At fourth depth:**

- To compute $q_p(4)\bmod p^3$, first form
  

$$
4^{p-1}-1\pmod{p^4},
$$


  then divide by $p$.

- To compute $q^*_{p,N;i}\bmod p^3$, first form
  

$$
(p+1)d_i-v_i\pmod{p^4},
$$


  then divide by $p$, then divide by the actual unit $v_i$.

- To compute $\mathfrak q_{p,N;i}$, first form the difference of the two quotient values modulo $p^3$, and only then divide by $p^2$. The actual third collision proves this division.

- To compute $\mathfrak z_{p,N}$, first form the **whole** numerator in (6.11) modulo $p^4$, and only then divide by $p^3$.

**At the assigned larger precision $p^{\mathsf d}$:**

- Use the exact products $\mathsf S_{p,h},\mathsf T_{p,j}$, not only the cubic truncation.

- In the original defect route, form
  

$$
\rho_p\mathsf S_{p,h}-1\pmod{p^{\mathsf d}}
$$


  before its paid division by $p$. This gives the defect precision $p^{\mathsf d-1}$.

- Use the exact shifted transport and both exact forcing returns through $r$, or equivalently the exact FULL22 continuant identities.

- If $a_G=v_p(g_B)$, an actual divided linear Gaussian quantity modulo $p^{\mathsf d}$ requires its numerator modulo
  

$$
p^{a_G+\mathsf d}.
$$


  A raw quadratic Gaussian column divided afterward by $g_B^2$ requires
  

$$
\boxed{p^{2a_G+\mathsf d}.}
$$



- To form $\mathbf v',\mathbf d'\bmod p^{\mathsf d-\lambda_p}$, first form their unnormalized numerators modulo $p^{\mathsf d}$, then divide by the proved $p^{\lambda_p}$.

- If instead one forms
  

$$
\det(\mathbf v,\mathbf d)/p^{2\lambda_p}
$$


  directly, its numerator must be known modulo
  

$$
p^{\mathsf d+\lambda_p}
$$


  to obtain the normalized determinant modulo $p^{\mathsf d-\lambda_p}$. Forming the normalized vectors first avoids an unnecessary precision loss.

The values $h_p,b_p,z_p,t_p$, and hence $B_p$, must still be determined from the original objects. A computation terminating at $p^4$ does not determine a valuation that continues beyond $p^4$.

---

## 10. What remains unproved after the elimination

The elimination has a definite mathematical effect: it removes the explicitly singled-out Fermat quotient from one full source constraint. It does **not** remove the numerical-value contact problem.

In the primary case, the unresolved assertion is now the following fully evaluated statement.

> **Fourth-depth numerical noncoincidence — open.**  
> Let $N=9^{18+32u}$, let $p\in\mathcal S_N$, assume $B_p=j_p=0$, and suppose $p^3\mid U,V$. Choose the proved unit component $v_i$. Using (3.1)–(4.9) and (6.1)–(6.9), prove that at least one of
> 

$$
> \boxed{
> \frac{Z_0+pZ_1+p^2Z_2+p^3Z_3}{p^3}
> }
>
$$


> and
> 

$$
> \boxed{
> \frac1{p^2}\left[
> \frac{4^{p-1}-1}{p}
> -\frac{(p+1)d_i-v_i}{p\,v_i}
> \right]
> }
>
$$


> is nonzero modulo $p$.

All divisions in this statement are justified by the actual lower collisions and the proved unit pivot. All lower-order carries remain.

A stronger, Fermat-free follow-on lemma would be


$$
\frac{Z_0+pZ_1+p^2Z_2+p^3Z_3}{p^3}\not\equiv0\pmod p
$$


under the same original hypotheses. That would settle the primary case immediately. It is not proved here, and its failure alone would not be a counterexample to the primary lemma: the remaining actual Fermat-quotient difference could still be nonzero.

### 10.1 Why the available arguments stop here

There is no proved reason that the evaluated compatibility value must have valuation exactly three. Nor is there a theorem excluding


$$
q_p(4)\equiv q^*_{p,N;i}\pmod{p^3}
$$


when that compatibility value vanishes modulo $p^4$.

The target in this congruence is actual, not free. Nevertheless:

- unit pivots establish equivalence, not noncoincidence;
- a nonzero quadratic coefficient in the endpoint chart does not prevent cancellation of its evaluated value;
- removing the displayed Fermat factor does not establish independence between the remaining Hermite, harmonic, Gaussian, and forcing data;
- the sufficient local clearer in Section 7 does not give a fixed-$N$ exponential-height numerator;
- no nonempty, quantitatively significant subset of $\mathcal S_N$ has been proved to pass the new compatibility test.

Thus neither the requested absolute paid depth cap nor significant aggregate coverage has been obtained.

### 10.2 Scope of FULL17

The particular FULL17 original-index splitting theorem assumes


$$
p\mid2N-1=\ell+5.
$$


But this implies


$$
p\mid\ell^2-25,
$$


which is excluded by $p\in\mathcal S_N$. That theorem therefore does not apply on the present non-arc branch.

No Gaussian-unit or non-Wieferich hypothesis from that theorem has been imported here. No fixed-prime index-density statement is being converted into fixed-$N$ interval coverage.

Smaller primes and primes $p>2N$ remain separate open obligations.

---

## 11. Preservation of the original returns and primitive producer

The new elimination changes no original normalization.

### 11.1 Source and endpoint balances

The source balance remains


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
\boxed{
\varrho_{j-1}=\varrho_{j+1}+4j\varrho_j-2\Delta.
}
$$



After actual arc clearing, put


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
\boxed{
\sigma_{j-1}^{\rm ret}
=\sigma_{j+1}^{\rm ret}+4j\sigma_j^{\rm ret}
+2D\Delta(-1)^j.
}
$$


Both signed forcing returns are retained, as is


$$
z_\ell^{\rm ret}w_{\ell-1}
-z_{\ell-1}^{\rm ret}w_\ell
=-16\Delta(UX+VY).
$$



For exactly $0\le b\le N$, retain


$$
\mathcal R_{b;N}=d_KP_b^{\rm H}U+Q_b^{\rm H}y_K.
$$


With


$$
\Psi_j^{(b)}=Q_b^{\rm H}\Phi_j-P_b^{\rm H}\Theta_j,
$$


the forcing is


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


The retained signed payment is


$$
\mathcal R_{N-1;N}<0<\mathcal R_{N;N},
$$




$$
\frac{c(r^\circ)^2}{\kappa_N^{\rm prod}}
\mid\mathcal R_{N-1;N}\mathcal R_{N;N},
\qquad
v_p(\kappa_N^{\rm prod})=[c_p-H_p]_+.
$$



The older rational interface retains its own paid clearers


$$
Q_{\rm loc}(n)=\prod_{b=0}^{12}(n-b),\qquad
\mathcal L_n=\operatorname{lcm}(1,\ldots,n),
$$


with


$$
\frac{2\mathcal L_n}{j^2-1}
=\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}.
$$


Neither these nor the local clearer in Section 7 replace the least arc clearer.

### 11.2 Both arcs and the actual primitive denominator

Retain


$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


The quotient polynomial degrees are at most $2N-2$.

The square-arc return has zero seeds at $0,1$, and


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


Its physical output is


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
E=\tau E_F+\nu E_K,\qquad A=\lambda E-b,
$$




$$
\boxed{G=\gcd(M,A),}
$$


where the gcd is over **all primes**, and


$$
\boxed{p_N=A/G,\qquad q_N=\lambda M/G.}
$$


Since $\gcd(\lambda,A)=1$, these are the actual primitive numerator and denominator.

### 11.3 The nonzero whole error at the same original indices

The original polynomial remains


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


Both positive summands in the weight remain.

The exact source balance gives


$$
\eta(W_{\rm prim})=M.
$$


Finite integration by parts and the two arcs therefore give


$$
\epsilon_N=e+\pi-\frac{A}{\lambda M},
$$


and hence, at the same original indices,


$$
\boxed{
q_N(e+\pi)-p_N=q_N\epsilon_N>0.
}
$$



The retained whole-error enclosure is


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


Thus


$$
\boxed{
q_NJ_N=\frac{\lambda_N}{G_N}
\bigl(\tau_NJ_F+\nu_NJ_K\bigr).
}
$$


Both terms on the right are positive. No bound for this whole expression follows from the new elimination.

---

## 12. Proof-status and computation ledger

| Item | Status |
|---|---|
| Original index domain, finite boundaries, physical terminal | Retained unchanged |
| Actual Gaussian division, content $g_B^2c$, source normalization | Retained unchanged |
| Complete corrected source and endpoint columns | Reuse at stated scope |
| FULL22 four-defect arithmetic and explicit continuants | Reused, not re-evaluated |
| Common actual factorization of all four prime-base states, (3.5) | **New proved recombination** |
| Exact complete source equation $\mathbf u=\mathbf d-\rho_p\mathbf v$ | **New proved substitution** |
| Validated pivot bound $\lambda_p\le v_p(\Delta)\le j_p$ | **New proved statement** |
| Fermat-free numerical compatibility identity, (5.6), (6.7) | **New proved elimination** |
| Explicit cubic compatibility coefficients, (6.9)–(6.10) | **New proved arithmetic evaluation** |
| Whole-carry fourth-depth equivalence, (5.10)–(5.12) | **New proved equivalence** |
| Sufficient local clearer and justified $\chi$-division, (7.1) | **New proved integrality statement** |
| Full endpoint additive difference and both signed forcing returns | Retained |
| Primitive mixed-height obstruction | Reuse at its exact scope; no new audit claimed |
| Nonzero fourth source pair for every assigned original pair | **Open** |
| Genuine original-family counterexample to that assertion | Not produced |
| Fixed absolute paid depth cap $e_p\le C+j_p$ | Not proved |
| Significant aggregate coverage or fixed-$N$ exponential certificate | Not proved |
| Smaller-prime and $p>2N$ obligations | Separate and open |
| Actual $D,\lambda,G,q_N$ and positive whole error | Retained unchanged |
| Rationality or irrationality of $e+\pi$ | Unresolved |

### Computation status

No finite arithmetic computation is indispensable to the new proofs. The new outputs are the exact factorizations, determinant elimination, four cubic coefficients, valuation equivalences, and clearing statement derived above.

Accordingly, no original-sized solve, prime scan, old source table, closed $p=23$ receipt, or optional constant calculation is requested.

A finite evaluation of the two residues in Theorem 5.1 at a certified original pair would establish only that pair. It would not settle the infinite original-family assertion.

---

## Final conclusion

The common actual Fermat quotient **can be eliminated from one complete Gaussian–Hermite source constraint**. The resulting compatibility value has the explicit fourth-precision evaluation


$$
\boxed{
\mathscr Z_{p,N}
\equiv Z_0+pZ_1+p^2Z_2+p^3Z_3\pmod{p^4},
}
$$


with every Hermite/harmonic coefficient, lower-half term, source constant, and forcing contribution retained.

On the zero-$j_p$ branch, the required pivot is proved to be a unit in the original objects. After an actual third collision, the original fourth source pair vanishes exactly when both the evaluated compatibility digit and the remaining actual Fermat-quotient difference vanish.

That is the exact remaining bottleneck. Neither simultaneous vanishing nor its exclusion is established here. The endpoint chart does not provide an additional independent equation: its complete additive difference reduces to the same two source constraints.

Thus this continuation proves a source-specific arithmetic elimination and its precise division bill, but **does not close the fourth-depth separation lemma or any paid aggregate substitute**. The all-prime final gcd, actual primitive denominator, both reduced arcs, and nonzero whole error remain unchanged at $N=9^{18+32u}$. No conclusion about $e+\pi$ follows.
