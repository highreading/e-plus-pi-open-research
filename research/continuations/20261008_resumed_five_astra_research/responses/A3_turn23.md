> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 Turn 23 — Different audit of A5 Turn 23 and large-prime endpoint arithmetic

## Executive conclusions

This report has two separate purposes.

1. **Different audit of the complete A5 Turn 23 report.**  
   The new common-$\rho_p$ factorization, validated pivot, Fermat-free compatibility identity, fourth-pair transformation, cubic coefficients, additive carry, local clearing statement, and critical-safe division rules **pass at their stated hypotheses**. No substantive algebraic correction is needed. In particular:
   - both lower-half constants are correct;
   - the actual Gaussian subtraction $-\delta^2$ remains present;
   - the endpoint quadratic gives no independent third constraint after the appropriate source equation is imposed;
   - none of these equivalences proves numerical noncollision.

2. **New research on $G_N$ at primes $p>2N$.**  
   The following statements are proved here in the original square producer:
   - the actual least arc clearers $D_N$ and $\lambda_N$ are odd, and both divide
     

$$
\operatorname{lcm}(1,3,5,\ldots,2N-1);
$$


     exact formulas below account for all cancellations in their reduction;
   - at every $p>2N$, the final gcd valuation is determined by an explicit two-case formula retaining the complete endpoint cancellation;
   - writing $\gamma=\gcd(\tau,y_K)$, the large-prime parts satisfy
     

$$
\boxed{\gamma_{>2N}\mid G_{>2N}\mid
     \gamma_{>2N}\,|\delta|_{>2N}^{\,2}},
$$


     and the actual primitive denominator satisfies
     

$$
\boxed{
     (\tau/\gamma)_{>2N}\mid(q_N)_{>2N}
     \mid(\tau/\gamma)_{>2N}\,|\delta|_{>2N}^{\,2}.
     }
$$


   - the part of $G_{>2N}$ beyond $r^\circ_{>2N}$ has the proved bill
     

$$
\boxed{
     \frac{G_{>2N}}{r^\circ_{>2N}}
     \mid (a_K\delta^2)_{>2N},
     \qquad
     \frac{G_{>2N}}{r^\circ_{>2N}}
     <10N^6\frac{5^{4N}}{g_B^2}.
     }
$$


   - the prime $2$ is paid separately:
     

$$
\boxed{
     v_2(g_B)=1,\quad v_2(c)=2,\quad
     \tau,\delta,M,\lambda,A,q_N\ \text{are odd},\quad v_2(G)=0.
     }
$$



These are genuine denominator-support and valuation results, not a claim that the remaining large-prime contact is bounded sufficiently for the global objective. The determinant-unit contact that survives primitive division is made explicit below, including a factorial evaluation with specified integer coefficients. Its required quantitative bound remains open.

The nonzero whole primitive error has **not** been proved to tend to zero. Consequently, no conclusion about the rationality or irrationality of $e+\pi$ follows.

---

# Part I. Original objects and exact scope

## 1. Original indices, contents, and finite systems

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


The physical terminal is $n=2N$. No residual index is substituted for $N$.

Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


where


$$
C_0=1,\qquad C_1=2t-1,\qquad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$



The actual Gaussian division is


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



For an integer polynomial $H$, retain


$$
\eta(H)=\sum_j j![z^j]H(1-z),\qquad
E(H)=\sum_j(-1)^j j![t^j]H(t).
$$


Put


$$
\mathcal H=t(1-t)(1+t^2)^2,\qquad
K=\mathcal H C_m^2,
$$




$$
U=-\eta(K),\qquad
V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
$$


The actual content statement is unchanged:


$$
\operatorname{cont}(W_{\rm raw})=g_B^2c.
$$


The primitive source data are


$$
\tau=U/c,\qquad \nu=V/c,\qquad
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2,
$$


with


$$
U,V,M>0,\qquad \gcd(\tau,\nu)=1.
$$



In particular, $c$ is not replaced by $\gcd(16U,V)$; that replacement would be wrong at the prime $2$.

### 1.1 Both finite forcings

For exactly $0\le j\le n$,


$$
\Theta_0=\Phi_0=0,\qquad \Theta_1=\Phi_1=1,
$$


and for exactly $1\le j\le n-1$,


$$
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2,
$$




$$
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j.
$$



Equivalently, their complete affine matrices are


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


No homogeneous replacement is made.

## 2. Complete corrected columns

At $x=\ell^2$, define


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



The complete $K$-columns are


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



Thus all four source/endpoint constants are retained, including both $-\delta^2$ and $4\alpha\beta$.

For the unchanged six-step transport, let


$$
T_j=\begin{pmatrix}-4j&1\\1&0\end{pmatrix},\qquad
T=T_{\ell+5}\cdots T_\ell.
$$


Starting from zero forcing vectors, use


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


so that


$$
V=C^{\rm s}-\Pi\Theta_\ell-\Omega\Theta_{\ell-1},
$$




$$
E_F=C^{\rm e}-\Pi\Phi_\ell-\Omega\Phi_{\ell-1}.
$$


The last recurrence step is exactly $\ell+5=n-1$.

Set


$$
\mathsf M_c=
\begin{pmatrix}\mathscr A&\mathscr B\\\Pi&\Omega\end{pmatrix},
\qquad
\mathbf C=\binom{\mathscr C_U}{C^{\rm s}},
\qquad
\mathbf u=\binom{16U}{V}.
$$


Retain


$$
\Delta=\det\mathsf M_c<0,
$$




$$
\mathscr I_1=\Pi\mathscr C_U-\mathscr A C^{\rm s},\qquad
\mathscr I_2=\Omega\mathscr C_U-\mathscr B C^{\rm s},
$$




$$
J_N^{\rm aff}=\gcd(\mathscr I_1,\mathscr I_2)>0,
$$


and


$$
\operatorname{adj}(\mathsf M_c)\mathbf C
=\binom{\mathscr I_2}{-\mathscr I_1}.
$$



The previously proved numerical bills remain


$$
\alpha^2+\beta^2+\delta^2<\frac{5^{4N}}{g_B^2},
$$




$$
|\Delta|,\ J_N^{\rm aff}
<
10^{10}(2N)^{15}\frac{5^{4N}}{g_B^2}.
$$


They are conditioning/height statements about these actual divided quantities, not general bounds on evaluated source contact.

## 3. Arc credit and the interval scope of the audit

The already reduced $K$-arc is


$$
R_K=\frac{A_K(\ell^2)}{30L(\ell^2)}=\frac{a_K}{d_K},
$$


where


$$
L(x)=(x-1)(x-9)(x-25),
$$




$$
A_K(x)=13x^3-455x^2+3502x-5850,
$$




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
d_K=30L(\ell^2)/g_{\rm arc},\qquad
\gcd(a_K,d_K)=1.
$$



Put


$$
y_K=d_KE_K-a_K,\qquad
\gamma=\gcd(\tau,y_K),
$$




$$
b^\circ=\gcd(\gamma,a_K),\qquad r^\circ=\gamma/b^\circ.
$$


For every prime,


$$
c_p=\min(v_p(U),v_p(V)),\qquad
t_p=v_p(U)-c_p,
$$




$$
z_p=v_p(y_K),\qquad b_p=v_p(b^\circ),\qquad
h_p=v_p(Q_{N-1}^{\rm H}Q_N^{\rm H}),
$$


and the complete credit is


$$
\boxed{H_p=h_p+2b_p+2(z_p-t_p)_+.}
$$



The interval audit concerns precisely


$$
\mathcal S_N=
\left\{
\begin{array}{l|l}
p&
N<p<2N,\ p\nmid L(\ell^2),\\
&d_{p,N}^{\rm block}=p^2,\quad
v_p(\Delta)\le v_p(J_N^{\rm aff})
\end{array}
\right\}.
$$


The block condition is not removed or replaced by necessary congruences.

For $p\in\mathcal S_N$, set


$$
r=n-p,\qquad s=\ell-p=r-6,\qquad
a=\frac{p-1}{2},\qquad k=a+1,\qquad \chi=2k!.
$$


The admitted boundaries are


$$
13\le r<N,\qquad s\ge7,\qquad r,s\text{ odd},\qquad k\le N-6,
$$


and


$$
p^2\mid U,V,\qquad p\nmid d_K.
$$


Finally,


$$
B_p=(H_p-2)_+,\qquad
e_p=[c_p-2-B_p]_+,\qquad
j_p=v_p(J_N^{\rm aff}).
$$



The audit below does not extend any prime-base state formula to $p>2N$. Such an extension would leave the original finite domain.

---

# Part II. Different audit of all new A5 Turn 23 claims

## 4. Common-$\rho_p$ factorization of all four actual prime-base states — PASS

The exact FULL22 coefficient evaluation was already differently audited. It gives


$$
w_j=p\mathsf b_j\mathsf T_{p,j}\qquad(1\le j\le a),
$$


and


$$
w_{p-h}=(-1)^h\chi\mathsf h_{a,h}\rho_p\mathsf S_{p,h}
\qquad(0\le h\le a),
$$


where


$$
\mathsf h_{a,h}=\frac{(2a-h)!}{(a-h)!\,h!},
\qquad
\mathsf b_j=\frac{4^j j!((j-1)!)^2}{2(2j)!},
$$




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
\prod_{v=1}^{j-1}\left(1-\frac{p^2}{v^2}\right),
$$


and


$$
\boxed{\rho_p=\frac{4^{p-1}}{p+1}=1+p\mu_p.}
$$



All remaining denominators here are units at the selected $p$.

The complete moment formulas are


$$
\Theta_p=\sum_{j=1}^p w_j,\qquad
\Phi_p=\sum_{j=1}^p(-1)^{j+1}w_j.
$$


The neighboring formulas, including their different constants, are


$$
\Theta_{p-1}+1
=\frac{p+\sum_{j=1}^p A_j^+w_j}{p-1},
$$




$$
\Phi_{p-1}-1
=\frac{-p+\sum_{j=1}^p(-1)^{j+1}A_j^-w_j}{p-1},
$$


where


$$
A_j^+=2j^2-p(2j+1),\qquad
A_j^-=2j(j+2)-p(2j+3).
$$


For the upper half,


$$
A_{p-h}^+=A_h^+,\qquad
A_{p-h}^-=\widetilde A_h^-,
$$


with


$$
\widetilde A_h^-=2h(h-2)-p(2h-1).
$$



Consequently, define


$$
\mathbf A_p^+
=
\chi
\binom{
\sum_{h=0}^{a}(-1)^h\mathsf h_{a,h}\mathsf S_{p,h}
}{
\frac1{p-1}
\sum_{h=0}^{a}(-1)^hA_h^+\mathsf h_{a,h}\mathsf S_{p,h}
},
$$




$$
\mathbf A_p^-
=
\chi
\binom{
\sum_{h=0}^{a}\mathsf h_{a,h}\mathsf S_{p,h}
}{
\frac1{p-1}
\sum_{h=0}^{a}\widetilde A_h^-\mathsf h_{a,h}\mathsf S_{p,h}
},
$$


and


$$
\mathbf L_p^+
=
\binom{
p\sum_{j=1}^{a}\mathsf b_j\mathsf T_{p,j}
}{
\frac{1+p\sum_{j=1}^{a}A_j^+\mathsf b_j\mathsf T_{p,j}}{p-1}
},
$$




$$
\mathbf L_p^-
=
\binom{
p\sum_{j=1}^{a}(-1)^{j+1}\mathsf b_j\mathsf T_{p,j}
}{
\frac{-1+p\sum_{j=1}^{a}(-1)^{j+1}A_j^-\mathsf b_j\mathsf T_{p,j}}{p-1}
}.
$$



The first coordinates follow immediately by splitting the two moment sums. In the alternating upper half,


$$
(-1)^{p-h+1}(-1)^h=1
$$


because $p$ is odd.

For the neighbors, subtracting $1$ from the first neighboring formula leaves


$$
\frac{p-(p-1)+\sum A_j^+w_j}{p-1}
=\frac{1+\sum A_j^+w_j}{p-1};
$$


adding $1$ in the second leaves


$$
\frac{-p+(p-1)+\sum(-1)^{j+1}A_j^-w_j}{p-1}
=\frac{-1+\sum(-1)^{j+1}A_j^-w_j}{p-1}.
$$


This independently checks both indispensable lower-half constants.

Hence


$$
\boxed{
\binom{\Theta_p}{\Theta_{p-1}}
=\rho_p\mathbf A_p^++\mathbf L_p^+,
\qquad
\binom{\Phi_p}{\Phi_{p-1}}
=\rho_p\mathbf A_p^-+\mathbf L_p^-.
}
$$



This is an exact factorization of the actual states, not a free-state parametrization.

## 5. Shifted transport and all four complete columns — PASS

For $0\le j\le r$, put


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
\mathbf h_{j+1}^-
=T_{p+j}\mathbf h_j^--\binom{2(-1)^j}{0}.
$$


The last minus sign is correct: the original alternating forcing is
$2(-1)^{p+j}=-2(-1)^j$.

For completeness, the already proved integer continuant is


$$
\mathcal K_m(x)=
\sum_{v=0}^{\lfloor m/2\rfloor}
\binom{m-v}{v}(-4)^{m-2v}(x+v+1)_{m-2v},
$$


with $\mathcal K_{-1}=0$. It supplies


$$
S_j=
\begin{pmatrix}
\mathcal K_j(p-1)&\mathcal K_{j-1}(p)\\
\mathcal K_{j-1}(p-1)&\mathcal K_{j-2}(p)
\end{pmatrix},
$$


and both full forced returns


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



Linearity therefore gives


$$
\binom{\Theta_{p+j}}{\Theta_{p+j-1}}
=
\rho_pS_j\mathbf A_p^+
+S_j\mathbf L_p^++\mathbf h_j^+,
$$




$$
\binom{\Phi_{p+j}}{\Phi_{p+j-1}}
=
\rho_pS_j\mathbf A_p^-
+S_j\mathbf L_p^-+\mathbf h_j^-.
$$



Substitution gives all four claimed columns:


$$
16U=
\mathscr C_U-(\mathscr A,\mathscr B)
\bigl(\rho_pS_s\mathbf A_p^+
+S_s\mathbf L_p^++\mathbf h_s^+\bigr),
$$




$$
V=
\alpha^2+(2n-3)\beta^2-\delta^2
-(P,Q)
\bigl(\rho_pS_r\mathbf A_p^+
+S_r\mathbf L_p^++\mathbf h_r^+\bigr),
$$




$$
16E_K=
\mathscr C_E+(\mathscr A,\mathscr B)
\bigl(\rho_pS_s\mathbf A_p^-
+S_s\mathbf L_p^-+\mathbf h_s^-\bigr),
$$




$$
E_F=
\alpha^2+(5-2n)\beta^2+4\alpha\beta
-(P,Q)
\bigl(\rho_pS_r\mathbf A_p^-
+S_r\mathbf L_p^-+\mathbf h_r^-\bigr).
$$



The largest shifted recurrence step is $p+r-1=n-1$. The Gaussian quantities are the divided $\alpha,\beta,\delta$.

Writing


$$
S=S_s,\qquad \mathbf h=\mathbf h_s^+,
$$




$$
\mathbf v=\mathsf M_cS\mathbf A_p^+,\qquad
\mathbf d=\mathbf C-\mathsf M_c(S\mathbf L_p^++\mathbf h),
$$


one obtains


$$
\boxed{\mathbf u=\mathbf d-\rho_p\mathbf v.}
$$


The second component of $\mathbf d$ contains the actual $-\delta^2$, through $C^{\rm s}$. This point is essential and passes.

## 6. Validated pivot and exact numerical compatibility — PASS

The Hermite sequence is the original finite sequence


$$
P_0^{\rm H}=Q_0^{\rm H}=1,\qquad
P_1^{\rm H}=3,\quad Q_1^{\rm H}=1,
$$




$$
Z_{b+1}=(4b+2)Z_b+Z_{b-1},\qquad 1\le b\le N-1.
$$


Its adjacent determinant is


$$
P_k^{\rm H}Q_a^{\rm H}-P_a^{\rm H}Q_k^{\rm H}
=2(-1)^a.
$$



Since $\mathsf S_{p,h}\equiv1\pmod p$, the passed weighted identities give


$$
\mathbf A_p^+
\equiv\chi\binom{Q_a^{\rm H}}{-Q_k^{\rm H}},
\qquad
\mathbf A_p^-
\equiv\chi\binom{P_a^{\rm H}}{-P_k^{\rm H}}\pmod p.
$$


Thus


$$
\det(\mathbf A_p^+,\mathbf A_p^-)
\equiv-2(-1)^a\chi^2\pmod p.
$$


Because $k<p$, this determinant is a unit. In particular,
$\mathbf A_p^+$ is primitive over $\mathbb Z_{(p)}$.

Also $\det S=(-1)^s=-1$. For
$\mathbf v^-=\mathsf M_cS\mathbf A_p^-$,


$$
\det(\mathbf v,\mathbf v^-)
\equiv2(-1)^a\chi^2\Delta\pmod p.
$$



To distinguish this local pivot exponent from the actual arc denominator
$\lambda_N$, write


$$
\lambda_p^{\rm piv}=\min(v_p(v_1),v_p(v_2)).
$$


The adjugate identity gives


$$
\operatorname{adj}(\mathsf M_c)\mathbf v
=\Delta S\mathbf A_p^+.
$$


The vector on the right, after division by $\Delta$, is primitive. Hence


$$
\boxed{
\lambda_p^{\rm piv}\le v_p(\Delta)\le j_p.
}
$$


The second inequality is an actual hypothesis of $\mathcal S_N$, not a general theorem about arbitrary primes.

Therefore, on $j_p=0$, an actual component $v_i$ is a unit. No Gaussian-unit, Fermat-quotient-unit, or non-Wieferich assumption has entered.

Define


$$
\mathscr Z_{p,N}=\det(\mathbf v,\mathbf d).
$$


Then


$$
\boxed{
\mathscr Z_{p,N}=\det(\mathbf v,\mathbf u).
}
$$


The explicitly isolated $\rho_p$ cancels exactly.

For a unit component $v_i$,


$$
\boxed{
c_p=
\min\left(
v_p(d_i/v_i-\rho_p),\ v_p(\mathscr Z_{p,N})
\right).
}
$$


This follows from a unit-determinant change of coordinates on $\mathbf u$, since $16$ is a unit at the selected odd prime.

The first source collision implies $d_i/v_i\equiv1\pmod p$, so


$$
q^*_{p,N;i}
=\frac{(p+1)d_i-v_i}{p\,v_i}
$$


is $p$-integral. Direct calculation yields


$$
u_i=-\frac{p\,v_i}{p+1}\bigl(q_p(4)-q^*_{p,N;i}\bigr),
$$


and hence


$$
\boxed{
c_p=
\min\left(
1+v_p(q_p(4)-q^*_{p,N;i}),\
v_p(\mathscr Z_{p,N})
\right).
}
$$



This passes as a numerical identity. It is not a numerical noncoincidence theorem.

## 7. Unit fourth-pair transformation — conditional PASS

Assume exactly


$$
p\in\mathcal S_N,\qquad B_p=j_p=0,\qquad p^3\mid U,V.
$$


Then


$$
q_p(4)-q^*_{p,N;i}\in p^2\mathbb Z_{(p)},\qquad
\mathscr Z_{p,N}\in p^3\mathbb Z_{(p)}.
$$


Put


$$
\mathfrak q_{p,N;i}
=\frac{q_p(4)-q^*_{p,N;i}}{p^2}\pmod p,
\qquad
\mathfrak z_{p,N}
=\frac{\mathscr Z_{p,N}}{p^3}\pmod p.
$$



For $i=1$,


$$
\binom{16U/p^3}{V/p^3}
\equiv
\begin{pmatrix}
-\dfrac{v_1}{p+1}&0\\[1mm]
-\dfrac{v_2}{p+1}&\dfrac1{v_1}
\end{pmatrix}
\binom{\mathfrak q_{p,N;1}}{\mathfrak z_{p,N}}
\pmod p.
$$


For $i=2$,


$$
\binom{16U/p^3}{V/p^3}
\equiv
\begin{pmatrix}
-\dfrac{v_1}{p+1}&-\dfrac1{v_2}\\[1mm]
-\dfrac{v_2}{p+1}&0
\end{pmatrix}
\binom{\mathfrak q_{p,N;2}}{\mathfrak z_{p,N}}
\pmod p.
$$


Both determinants are $-1/(p+1)$, a unit.

Thus the claimed equivalence is correct:


$$
\left(\frac{16U}{p^3},\frac V{p^3}\right)\not\equiv(0,0)
\iff
(\mathfrak q_{p,N;i},\mathfrak z_{p,N})\not\equiv(0,0).
$$



The divisions by $p^2$ and $p^3$ are paid only by the actual third collision. The displayed transformation does not prove that either side is nonzero.

## 8. All cubic coefficients and the additive carry — PASS

Let


$$
H_t^{(d)}=\sum_{v=1}^t v^{-d},
$$


and


$$
L_{1,h}=\frac32H_h^{(1)}-H_{2h}^{(1)},
$$




$$
L_{2,h}=\frac{15}{4}H_h^{(2)}-3H_{2h}^{(2)},
$$




$$
L_{3,h}=\frac{63}{8}H_h^{(3)}-7H_{2h}^{(3)}.
$$


Define


$$
H_{0,h}=1,\qquad H_{1,h}=L_{1,h},
$$




$$
H_{2,h}=\frac{L_{1,h}^2+L_{2,h}}2,
$$




$$
H_{3,h}=
\frac{L_{1,h}^3+3L_{1,h}L_{2,h}+2L_{3,h}}6.
$$



The finite formal logarithm of $\mathsf S_{p,h}$, through degree three, is


$$
pL_{1,h}+\frac{p^2}{2}L_{2,h}+\frac{p^3}{3}L_{3,h}.
$$


Exponentiation therefore gives


$$
\mathsf S_{p,h}
\equiv1+pH_{1,h}+p^2H_{2,h}+p^3H_{3,h}\pmod{p^4}.
$$


The lower product gives


$$
\mathsf T_{p,j}
\equiv1-p^2H_{j-1}^{(2)}\pmod{p^4}.
$$



For $0\le d\le3$, let $\mathbf A_d^\pm$ be obtained from
$\mathbf A_p^\pm$ by replacing $\mathsf S_{p,h}$ by $H_{d,h}$.
Let


$$
\mathbf B_0^+
=\sum_{j=1}^a\mathsf b_j
\binom{1}{A_j^+/(p-1)},\qquad
\mathbf B_2^+
=\sum_{j=1}^a\mathsf b_jH_{j-1}^{(2)}
\binom{1}{A_j^+/(p-1)},
$$


and


$$
\mathbf B_0^-
=\sum_{j=1}^a(-1)^{j+1}\mathsf b_j
\binom{1}{A_j^-/(p-1)},\qquad
\mathbf B_2^-
=\sum_{j=1}^a(-1)^{j+1}\mathsf b_jH_{j-1}^{(2)}
\binom{1}{A_j^-/(p-1)}.
$$


Then both upper and lower expansions are


$$
\mathbf A_p^\pm
\equiv\sum_{d=0}^3p^d\mathbf A_d^\pm\pmod{p^4},
$$




$$
\mathbf L_p^\pm
\equiv
\pm\frac1{p-1}\binom01
+p\mathbf B_0^\pm-p^3\mathbf B_2^\pm
\pmod{p^4}.
$$


In particular, no lower-half cubic sign is missing.

Set


$$
\mathbf w=\binom{\mathscr I_2}{-\mathscr I_1}.
$$


Using $\det S=-1$,


$$
\boxed{
\mathscr Z_{p,N}
=
\det(S\mathbf A_p^+,\mathbf w-\Delta\mathbf h)
+\Delta\det(\mathbf A_p^+,\mathbf L_p^+).
}
$$


This identity uses the adjugate, not an inverse of $\Delta$.

Write $S=(s_{ij})$, $\mathbf h=(h_1,h_2)^t$, and define


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
$$


Let


$$
\mathcal T(X_1,X_2)=t_1^{\rm elim}X_1+t_2^{\rm elim}X_2.
$$


Then the four coefficients are exactly


$$
Z_0=\mathcal T(\mathbf A_0^+),
$$




$$
Z_1=\mathcal T(\mathbf A_1^+)
+\Delta\det(\mathbf A_0^+,\mathbf B_0^+),
$$




$$
Z_2=\mathcal T(\mathbf A_2^+)
+\Delta\det(\mathbf A_1^+,\mathbf B_0^+),
$$




$$
Z_3=\mathcal T(\mathbf A_3^+)
+\Delta\det(\mathbf A_2^+,\mathbf B_0^+)
-\Delta\det(\mathbf A_0^+,\mathbf B_2^+).
$$


Therefore


$$
\boxed{
\mathscr Z_{p,N}\equiv
Z_0+pZ_1+p^2Z_2+p^3Z_3\pmod{p^4}.
}
$$



These $Z_d$ are $p$-dependent rational coefficients, not base-$p$ digits. After a third collision, the fourth digit is


$$
\boxed{
\mathfrak z_{p,N}\equiv
\frac{Z_0+pZ_1+p^2Z_2+p^3Z_3}{p^3}\pmod p.
}
$$


The entire numerator must be formed before division. Replacing this expression by $Z_3\bmod p$ would be wrong.

## 9. The $48\operatorname{lcm}^4/\chi$ bill — PASS at its exact scope

Let


$$
\mathcal L=\operatorname{lcm}(1,\ldots,p-1).
$$



For an odd prime $q$, the possible denominator exponent of $\mathsf b_j$ is bounded using


$$
\sum_{d\ge1}\left(
\left\lfloor\frac{2j}{q^d}\right\rfloor
-\left\lfloor\frac j{q^d}\right\rfloor
-2\left\lfloor\frac{j-1}{q^d}\right\rfloor
\right).
$$


Writing $j=Aq^d+r$, the summand is at most $1$, and it vanishes once $q^d>2j$. Thus the reduced denominator exponent is at most
$\lfloor\log_q(2j)\rfloor$.

At $2$, a particularly direct calculation is


$$
v_2((2j)!)=j+v_2(j!),
$$


so


$$
v_2(\mathsf b_j)
=j-1+2v_2((j-1)!)\ge0.
$$


Hence


$$
\operatorname{den}(\mathsf b_j)\mid\mathcal L.
$$



The sufficient harmonic denominators are


$$
H_{1,h}:2\mathcal L,\qquad
H_{2,h}:8\mathcal L^2,\qquad
H_{3,h}:48\mathcal L^3.
$$


A second coordinate introduces one factor $p-1$, which divides $\mathcal L$.

Every $\mathbf A_d^+$ contains the displayed factor $\chi$, and each $Z_d$ is linear in these vectors. In each determinant product only one second-coordinate denominator occurs. Consequently


$$
\boxed{
\frac{48\mathcal L^4}{\chi}
\left(Z_0+pZ_1+p^2Z_2+p^3Z_3\right)\in\mathbb Z.
}
$$


Also $p\nmid48\mathcal L^4\chi$.

This proves the claimed integrality. Its scope must be kept exact:

- it clears the **displayed cubic truncation**;
- the division by $\chi$ is justified term by term in that expression;
- it does not divide $U,V$, the mixed minors, or the original producer;
- it is not the actual least arc clearer;
- it gives no fixed-$N$ numerator-height or aggregate-coverage theorem.

## 10. Endpoint quadratic and absence of a third independent constraint — PASS

Retain


$$
\mathbf t_j=\binom{\Theta_j}{\Theta_{j-1}},\qquad
\mathbf f_j=\binom{\Phi_j}{\Phi_{j-1}},
$$




$$
\mathbf R=\mathbf C-\mathsf M_c\mathbf t_s,
$$


and the complete relative endpoint


$$
\mathbf E=
\binom{
16E_K-\mathscr C_E+\mathscr A\Phi_s+\mathscr B\Phi_{s-1}
}{
C^{\rm e}-E_F+\Pi\Phi_s+\Omega\Phi_{s-1}
}.
$$


The signs give


$$
\mathbf E=\mathsf M_c(\mathbf f_\ell+\mathbf f_s).
$$



The actual mixed minors are


$$
\mathfrak A=\det(\mathbf R,\mathbf u),\qquad
\mathfrak B=\det(\mathbf u,\mathbf E).
$$


Their complete additive endpoint identity remains


$$
\boxed{
\mathfrak B
=
R_1E_2-R_2E_1-\Delta\mathfrak D_{s;p},
}
$$


where


$$
\mathfrak D_{s;p}
=
2(-1)^a\chi^2+p\chi\Lambda_\sigma
+p^2\Xi_\sigma+4p\mathfrak f_{s;p},
$$




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




$$
\mathfrak f_{s;p}
=
-\sum_{t=1}^{s-1}(-1)^t
(\Theta_t\Phi_{p+t}+\Phi_t\Theta_{p+t}).
$$


All four defects are the actual anchored defects already evaluated in FULL22.

Now


$$
\mathbf E=\mathbf E_0+\rho_p\mathbf v^-,
\qquad
\mathbf E_0=\mathsf M_c(S\mathbf L_p^-+\mathbf h_s^-+\mathbf f_s).
$$


Thus


$$
\begin{aligned}
\mathfrak B={}&\det(\mathbf d,\mathbf E_0)\\
&+\rho_p\bigl(\det(\mathbf d,\mathbf v^-)
-\det(\mathbf v,\mathbf E_0)\bigr)
-\rho_p^2\det(\mathbf v,\mathbf v^-).
\end{aligned}
$$


The quadratic coefficient is a unit modulo $p$ when $j_p=0$. That does not make the evaluated quadratic nonzero.

Indeed, if $v_1$ is a unit,


$$
\mathfrak A
=
\left(\frac{R_1v_2}{v_1}-R_2\right)u_1
+\frac{R_1}{v_1}\mathscr Z,
$$




$$
\boxed{
\mathfrak B
=
\left(E_2-\frac{E_1v_2}{v_1}\right)u_1
-\frac{E_1}{v_1}\mathscr Z.
}
$$


Modulo any tested power of $p$, imposing $u_1\equiv0$ leaves only a multiple of the same compatibility value $\mathscr Z$.

If only $v_2$ is a unit, the corresponding formulas are


$$
\mathfrak A
=
\left(R_1-\frac{R_2v_1}{v_2}\right)u_2
+\frac{R_2}{v_2}\mathscr Z,
$$




$$
\mathfrak B
=
\left(\frac{E_2v_1}{v_2}-E_1\right)u_2
-\frac{E_2}{v_2}\mathscr Z.
$$


This supplies the same conclusion in the other pivot chart.

Thus the “first source equation” wording must be interpreted in the applicable pivot chart, or simply as an identity modulo the ideal generated by the two source entries. No independent third condition is created.

The safe original chart remains


$$
\min(v_p(R_1),v_p(E_1))=0,
\qquad
\zeta=
\begin{cases}
\mathfrak A,&p\nmid R_1,\\
\mathfrak B,&p\mid R_1,
\end{cases}
$$


with


$$
c_p-2=
\min\bigl(v_p(16U/p^2),v_p(\zeta/p^2)\bigr).
$$


No inverse of $\Delta$ is used.

## 11. Critical-safe normalization and precision — PASS

Let $\lambda_p^{\rm piv}=\min(v_p(v_1),v_p(v_2))$.

If $c_p<\lambda_p^{\rm piv}$, then
$c_p<\lambda_p^{\rm piv}\le j_p$, so the assigned upper-depth target is already automatic.

Otherwise


$$
\mathbf v'=\mathbf v/p^{\lambda_p^{\rm piv}},\qquad
\mathbf d'=\mathbf d/p^{\lambda_p^{\rm piv}}
$$


are $p$-integral, because


$$
\mathbf d=\mathbf u+\rho_p\mathbf v.
$$


A component $v_i'$ is a unit, and


$$
\boxed{
c_p=\lambda_p^{\rm piv}
+\min\left(
v_p(d_i'/v_i'-\rho_p),\
v_p\det(\mathbf v',\mathbf d')
\right).
}
$$


The normalized Fermat target is integral only after
$c_p\ge\lambda_p^{\rm piv}+1$.

The precision requirements in A5 Turn 23 are correct:

- $q_p(4)\bmod p^3$ requires $4^{p-1}-1\bmod p^4$ before division by $p$.
- $q^*\bmod p^3$ requires $(p+1)d_i-v_i\bmod p^4$ before division by $p$.
- The fourth compatibility digit requires the whole cubic numerator modulo $p^4$, then division by $p^3$.
- At $\mathsf d=4+B_p+j_p$, exact products and exact forced transports are required; cubic truncation alone is insufficient.
- If $a_G=v_p(g_B)$, divided Gaussian linear data modulo $p^{\mathsf d}$ require raw numerators modulo $p^{a_G+\mathsf d}$. Raw quadratic columns divided by $g_B^2$ require
  

$$
p^{2a_G+\mathsf d}.
$$


  The unit part of the actual divisor must also be retained.
- Forming $\mathbf v',\mathbf d'\bmod p^{\mathsf d-\lambda_p^{\rm piv}}$ from numerator precision $p^{\mathsf d}$ is valid.
- Forming $\det(\mathbf v,\mathbf d)/p^{2\lambda_p^{\rm piv}}$ directly requires numerator precision $p^{\mathsf d+\lambda_p^{\rm piv}}$ for that same normalized determinant precision.

The original credit $H_p$, including $h_p,b_p,z_p,t_p$, is not determined by a calculation that stops before an unresolved valuation terminates.

## 12. Audit status

| A5 Turn 23 claim | Verdict and exact qualification |
|---|---|
| Common $\rho_p$ in all four actual base states | **PASS** |
| Lower-half constants $+1,-1$ | **PASS** |
| Both shifted forcing signs and finite boundary | **PASS** |
| All four complete source/endpoint substitutions | **PASS** |
| Exact $\mathbf u=\mathbf d-\rho_p\mathbf v$ | **PASS**, with actual $-\delta^2$ |
| $\lambda_p^{\rm piv}\le v_p(\Delta)\le j_p$ | **PASS**; second inequality is the $\mathcal S_N$ hypothesis |
| Fermat-free numerical compatibility | **PASS**, not numerical independence |
| Unit fourth-pair transformation | **PASS after an actual third collision** |
| All four cubic coefficients and whole carry | **PASS** |
| $48\mathcal L_{p-1}^4/\chi$ integrality | **PASS for the displayed truncation only** |
| Endpoint quadratic gives an extra independent condition | **No such conclusion is valid**; A5 correctly rejects it |
| Critical normalization and precision before division | **PASS** |
| Earlier mixed least-clearer and height results | Reused at their already differently audited scopes |
| Pending-review wording for FULL20–22 | **Ledger repair only:** those audits are now passed at their exact scopes |
| Universal fourth-depth numerical noncollision | **OPEN** |
| Fixed absolute paid cap or significant aggregate coverage | **OPEN** |

The mixed normalization is unchanged:


$$
d_{\rm mix}=\gcd(\mathfrak D_{s;p},\mathfrak A,\mathfrak B),
$$




$$
(A_{\rm mix},B_{\rm mix},D_{\rm mix})
=\frac1{d_{\rm mix}}(\mathfrak A,\mathfrak B,\mathfrak D_{s;p}).
$$


It is the primitive triple, and $D_{\rm mix}$ is the actual least simultaneous clearer. Its established lower bounds and the immediate normalization-rigidity corollary concern these same two ratios, not all original producers.

Also, the older splitting theorem requiring $p\mid2N-1=\ell+5$ does not apply to $\mathcal S_N$, because that condition forces $p\mid\ell^2-25$. No fixed-prime index-density statement is converted into fixed-$N$ interval coverage.

---

# Part III. New research on the actual endpoint gcd at $p>2N$

## 13. Begin with the determinant-unit complement

The closed all-prime determinant-deep result is reused exactly:


$$
\boxed{
v_p(\Delta)>v_p(J_N^{\rm aff})
\ \Longrightarrow\ c_p\le v_p(J_N^{\rm aff}).
}
$$


Its proof uses the integer identities


$$
16\Pi U-\mathscr A V
=\mathscr I_1+\Delta\Theta_{\ell-1},
$$




$$
16\Omega U-\mathscr B V
=\mathscr I_2-\Delta\Theta_\ell,
$$


without determinant division. It includes primes above $2N$.

It does **not** apply to determinant-unit primes. For


$$
p>n,\qquad p\nmid\Delta,
$$


the actual source equation instead gives the exact contact identity


$$
\operatorname{adj}(\mathsf M_c)\mathbf u
=
\binom{\mathscr I_2}{-\mathscr I_1}
-\Delta\binom{\Theta_\ell}{\Theta_{\ell-1}},
$$


and therefore


$$
\boxed{
c_p=
\min\left(
v_p(\mathscr I_2-\Delta\Theta_\ell),\
v_p(-\mathscr I_1-\Delta\Theta_{\ell-1})
\right).
}
$$


This is an equivalence, not a cap.

All states here have indices at most $\ell<n<p$. No $\Theta_p$ or $\Phi_p$ is introduced.

## 14. Precise support of the fully reduced arc clearers

### Theorem 14.1 — Actual arc denominator support

Let


$$
\mathcal O_n=\operatorname{lcm}(1,3,5,\ldots,n-1).
$$


For every original $N$,


$$
\boxed{
\operatorname{den}(R_F)\mid\mathcal O_n,\qquad
d_K\mid\mathcal O_n,\qquad
D\mid\mathcal O_n,\qquad
\lambda\mid D.
}
$$


In particular,


$$
\boxed{2\nmid D\lambda,\qquad p>2N\Longrightarrow p\nmid D\lambda.}
$$



#### Proof: integral degree support

Because $F(\pm i)=\delta$, the polynomial $F^2-\delta^2$ is divisible by $1+t^2$. Division by this monic polynomial gives


$$
\frac{F^2-\delta^2}{1+t^2}\in\mathbb Z[t].
$$


Also


$$
\frac K{1+t^2}
=t(1-t)(1+t^2)C_m^2\in\mathbb Z[t].
$$


Both quotient degrees are at most $n-2$.

Thus integration gives


$$
R_F,\ R_K\in
\frac1{\operatorname{lcm}(1,\ldots,n-1)}\mathbb Z.
$$


This argument is valid after the actual Gaussian division because $F\in\mathbb Z[t]$. An unreduced formula displaying $g_B^2$ in a denominator cannot introduce genuine extra arc-denominator primes.

#### Proof: the square-arc recurrence removes the prime $2$

The supplied square-arc recurrence has zero seeds at $0,1$:


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


Only $1\le j\le n-1$ is used.

For even $j\le n-2$, the positive odd integers $j-1,j+1$ are coprime and at most $n-1$. Hence


$$
(j^2-1)\mid\mathcal O_n,
\qquad
\mathcal O_n\ell_j\in\mathbb Z.
$$



Define


$$
x_j=\frac{\mathcal O_n\xi_j}{16},\qquad
y_j=\frac{\mathcal O_n\upsilon_j}{16}.
$$


Their recurrences have integer coefficients and integer forcing:


$$
x_{j+1}=4y_j-2x_j-x_{j-1}+\mathcal O_n b_j,
$$




$$
y_{j+1}=-4x_j-2y_j-y_{j-1}
+\mathcal O_n\ell_j-\mathcal O_n a_j.
$$


Therefore $x_j,y_j\in\mathbb Z$ through the physical terminal.

Using the actual output,


$$
R_F=
\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
-2\alpha\beta\xi_{n-1}}2,
$$


we obtain


$$
\boxed{
F_{\mathcal O}:=\mathcal O_nR_F
=
8\bigl(\alpha^2x_n+\beta^2x_{n-2}
-2\alpha\beta x_{n-1}\bigr)\in8\mathbb Z.
}
$$


Thus $\operatorname{den}(R_F)\mid\mathcal O_n$.

For $R_K=a_K/d_K$, the established exact reduction gives $d_K$ odd. Combined with the integral degree bound, this gives $d_K\mid\mathcal O_n$.

Finally, an integer combination of $R_F,R_K$ has reduced denominator dividing their least simultaneous clearer. Since $\tau,\nu$ are integers,
$\lambda\mid D$. ∎

### 14.1 Exact least-clearer formulas, including all cancellations

The preceding theorem does not assert that $D=\mathcal O_n$, or that every small prime occurs.

Set


$$
K_{\mathcal O}=\mathcal O_nR_K
=\mathcal O_n a_K/d_K\in\mathbb Z.
$$


Then the exact least simultaneous clearer is


$$
\boxed{
D=
\frac{\mathcal O_n}
{\gcd(\mathcal O_n,F_{\mathcal O},K_{\mathcal O})}.
}
$$


Indeed, prime by prime, its exponent is the maximum denominator exponent needed for the two rational numbers.

Independently reducing the actual arc combination gives


$$
s_{\mathcal O}
=\gcd(\mathcal O_n,\tau F_{\mathcal O}+\nu K_{\mathcal O}),
$$




$$
\boxed{
\lambda=\frac{\mathcal O_n}{s_{\mathcal O}},\qquad
b=\frac{\tau F_{\mathcal O}+\nu K_{\mathcal O}}{s_{\mathcal O}}.
}
$$


These are the actual reduced $b,\lambda$, including cancellation between the two arcs.

Equivalently, if $f_D=DR_F$ and $k_D=DR_K$, then


$$
s_D=\gcd(D,\tau f_D+\nu k_D),\qquad
\lambda=D/s_D,\qquad b=(\tau f_D+\nu k_D)/s_D.
$$



These formulas establish exact support and reduction. No unreduced displayed denominator is treated as least.

## 15. The prime $2$, separately paid

The recurrence modulo $2$ gives $C_j\equiv1\pmod2$. The doubling identity


$$
C_{2j}=2C_j^2-1
$$


therefore gives


$$
C_{2j}\equiv1\pmod8
$$


as an integer-polynomial congruence. The recurrence modulo $4$ then gives


$$
C_{2j+1}\equiv2t-1\pmod4.
$$



Since $N$ is odd,


$$
8\mid b_{N-1},\qquad b_N\equiv2\pmod4.
$$


Hence


$$
v_2(g_B)=1,\qquad 4\mid\alpha,\qquad \beta\text{ odd}.
$$


Also $a_{N-1}$ is odd, so


$$
\delta=a_N\alpha-a_{N-1}\beta
$$


is odd.

Because $C_{N-1}\equiv1\pmod8$,


$$
F^2
=\alpha^2C_N^2-2\alpha\beta C_NC_{N-1}
+\beta^2C_{N-1}^2
\equiv1\pmod8.
$$


It follows that


$$
E_F\equiv\eta(F^2)\equiv1\pmod8,\qquad
V=\eta(F^2)-\delta^2\equiv0\pmod8.
$$



Using the already established $v_2(U)=2$,


$$
v_2(c)=2,\qquad \tau\text{ odd},\qquad \nu\text{ even}.
$$


Thus $M=\tau\delta^2$ is odd.

Theorem 14.1 gives $D,\lambda$ odd and $v_2(R_F)\ge3$. The exact $K$-arc reduction has $a_K,d_K$ odd, so $\nu R_K$ is $2$-adically even. Therefore the fully reduced arc numerator $b$ is even. Since


$$
E=\tau E_F+\nu E_K
$$


is odd,


$$
A=\lambda E-b
$$


is odd.

Consequently


$$
\boxed{v_2(G)=0,\qquad q_N\text{ odd}.}
$$



The retained Hermite denominators are all odd, by their recurrence. With
$z_2=1$, $t_2=b_2=h_2=0$, the complete credit is


$$
H_2=2,\qquad [c_2-H_2]_+=0.
$$


Thus the source normalization, arc clearing, final gcd, and credit at $2$ are all accounted for separately.

## 16. Exact large-prime valuation conditions

For the rest of this part, let $p>n=2N$. Then


$$
p\nmid d_KD\lambda.
$$



Define the actual rational endpoint differences


$$
\mathcal F_{\rm end}=E_F-R_F,\qquad
\mathcal K_{\rm end}=E_K-R_K=\frac{y_K}{d_K}.
$$


They are $p$-integral. Since $b/\lambda=\tau R_F+\nu R_K$,


$$
\boxed{
A=\lambda\bigl(\tau\mathcal F_{\rm end}
+\nu\mathcal K_{\rm end}\bigr).
}
$$


In particular,


$$
v_p(A)
=
v_p\bigl(\tau\mathcal F_{\rm end}
+\nu\mathcal K_{\rm end}\bigr).
$$



This retains both possible cancellations:

- $E=\tau E_F+\nu E_K$ can itself have cancellation;
- the fully reduced $b$ can have cancellation between the two arcs.

More explicitly, if $e=v_p(E)$ and $\beta_b=v_p(b)$, then


$$
v_p(A)=\min(e,\beta_b)\quad\text{when }e\ne\beta_b,
$$


whereas for $e=\beta_b=w<\infty$,


$$
v_p(A)
=w+v_p\left(\lambda E/p^w-b/p^w\right).
$$


The equal-valuation carry cannot be omitted.

Write


$$
t=v_p(\tau),\qquad d=v_p(\delta),\qquad z=v_p(y_K).
$$


Since $\gcd(\tau,\nu)=1$, $t>0$ implies $p\nmid\nu$.

### Theorem 16.1 — Actual large-prime gcd valuation

Let $g_p=v_p(G)$.

1. If $z<t$, then
   

$$
\boxed{g_p=z.}
$$



2. If $z\ge t$, put
   

$$
\widehat\tau=\tau/p^t,
$$


   

$$
\mathcal W_p
   =
   \widehat\tau\,\mathcal F_{\rm end}
   +\nu\,\frac{y_K/p^t}{d_K}.
$$


   This is $p$-integral, and
   

$$
\boxed{
   g_p=t+\min\bigl(2d,v_p(\mathcal W_p)\bigr).
   }
$$



#### Proof

We have


$$
v_p(M)=t+2d,
\qquad
g_p=\min(v_p(M),v_p(A)).
$$



If $z<t$, then $t>0$, so $\nu$ is a unit. The two terms in
$\tau\mathcal F_{\rm end}+\nu y_K/d_K$ have valuations at least $t$ and exactly $z$. Their valuations are unequal, so the sum has valuation $z$. Since $z<t\le t+2d$, $g_p=z$.

If $z\ge t$, the exact endpoint sum factors as


$$
\tau\mathcal F_{\rm end}+\nu y_K/d_K
=p^t\mathcal W_p.
$$


Taking the minimum with $t+2d$ proves the formula. ∎

### 16.1 The required distinctions

If $p\nmid\delta$, then $d=0$, and the theorem reduces to


$$
\boxed{
v_p(G)=\min(t,z).
}
$$


Thus a large prime with $p\nmid\tau\delta$ cannot divide $G$, while a prime dividing $\tau$ but not $\delta$ contributes exactly the truncated $K$-endpoint contact.

If $p\mid\delta$ but $p\nmid\tau$, then $t=0$, and


$$
\boxed{
v_p(G)=
\min\left(
2d,\
v_p(\tau\mathcal F_{\rm end}+\nu\mathcal K_{\rm end})
\right).
}
$$


Here the complete square- and $K$-endpoint cancellation is indispensable.

If $p\mid\tau\delta$, then:
- for $z<t$, no additional $\delta$-depth is obtained;
- for $z\ge t$, the additional depth is precisely
  $\min(2d,v_p(\mathcal W_p))$.

### 16.2 Actual primitive denominator valuations

Because $p\nmid\lambda$,


$$
v_p(q_N)=t+2d-g_p.
$$


Thus


$$
\boxed{
v_p(q_N)=
\begin{cases}
t+2d-z,&z<t,\\[1mm]
[\,2d-v_p(\mathcal W_p)\,]_+,&z\ge t.
\end{cases}
}
$$


In particular, when $p\nmid\delta$,


$$
\boxed{v_p(q_N)=[t-z]_+.}
$$



These are valuations of the actual primitive denominator, not of an auxiliary clearer.

## 17. A proved large-prime factor comparison and its bill

For a positive integer $a$, write


$$
a_{>n}=\prod_{p>n}p^{v_p(a)}.
$$


Use $|\delta|_{>n}$ when $\delta$ is signed.

Since


$$
v_p(\gamma)=\min(t,z),
$$


Theorem 16.1 gives


$$
0\le v_p(G)-v_p(\gamma)\le2v_p(\delta).
$$


Therefore


$$
\boxed{
\gamma_{>n}\mid G_{>n}\mid
\gamma_{>n}|\delta|_{>n}^{\,2}.
}
$$



If


$$
H_{>n}=G_{>n}/\gamma_{>n},
$$


then $H_{>n}$ is an integer divisor of $|\delta|_{>n}^{\,2}$, and


$$
(q_N)_{>n}
=
(\tau/\gamma)_{>n}
\frac{|\delta|_{>n}^{\,2}}{H_{>n}}.
$$


Consequently


$$
\boxed{
(\tau/\gamma)_{>n}\mid(q_N)_{>n}
\mid(\tau/\gamma)_{>n}|\delta|_{>n}^{\,2}.
}
$$



This proves that the large-prime denominator cofactor is, up to a divisor of $\delta^2$, exactly the large-prime cofactor of $\tau/\gcd(\tau,y_K)$.

The additional $\delta$-part has the actual divided Gaussian bill


$$
H_{>n}\le\delta^2<\frac{5^{4N}}{g_B^2}.
$$


This is valid even when a large prime divides $g_B$: the bound concerns the actual divided $\delta$.

There is also a small source-specific numerator bill. On the original domain $x=\ell^2>100$,


$$
0<A_K(x)<14x^3.
$$


Since $g_{\rm arc}\ge90$ and $x<4N^2$,


$$
\boxed{0<a_K<10N^6.}
$$


Because $b^\circ\mid a_K$ and $\gamma=b^\circ r^\circ$,


$$
\boxed{
\frac{G_{>n}}{r^\circ_{>n}}
\mid(a_K\delta^2)_{>n},
}
$$


and


$$
\boxed{
\frac{G_{>n}}{r^\circ_{>n}}
<10N^6\frac{5^{4N}}{g_B^2}.
}
$$



This is a proved payment for the part beyond $r^\circ_{>n}$. It does not pay the remaining $r^\circ$-contact, and it does not itself establish a limit for the whole primitive error.

## 18. The determinant-unit contact after actual primitive division

Let $p>n$ and $p\nmid\Delta$. Put $\kappa=c_p$ and $c_0=c/p^\kappa$, a $p$-adic unit. Define the actual integer vector


$$
\boldsymbol\xi_p
=
\frac1{p^\kappa}
\left[
\binom{\mathscr I_2}{-\mathscr I_1}
-\Delta\binom{\Theta_\ell}{\Theta_{\ell-1}}
\right].
$$


The source-contact identity in Section 13 proves that this division is paid and that $\boldsymbol\xi_p$ is primitive at $p$.

Multiplying by $\mathsf M_c$ gives


$$
\boxed{
\mathscr A\xi_{p,1}+\mathscr B\xi_{p,2}
=16c_0\Delta\,\tau,
}
$$




$$
\boxed{
\Pi\xi_{p,1}+\Omega\xi_{p,2}
=c_0\Delta\,\nu.
}
$$


All coefficients are the actual divided columns, including the $-\delta^2$ inside $\mathscr I_1,\mathscr I_2$.

For $h\ge1$, the condition $p^h\mid\gamma$ is therefore exactly


$$
\mathscr A\xi_{p,1}+\mathscr B\xi_{p,2}\equiv0\pmod{p^h},
$$




$$
\boxed{
d_K\bigl(
\mathscr C_E+\mathscr A\Phi_\ell+\mathscr B\Phi_{\ell-1}
\bigr)-16a_K
\equiv0\pmod{p^h}.
}
$$


The second congruence is $16y_K\equiv0\pmod{p^h}$.

A unit determinant makes this a well-conditioned contact problem. It supplies no reason that the actual forced state must avoid either congruence.

For the extra $\delta$-contact, the square endpoint in Theorem 16.1 is explicitly


$$
\begin{aligned}
\mathcal F_{\rm end}
={}&\alpha^2+(5-2n)\beta^2+4\alpha\beta
-P\Phi_n-Q\Phi_{n-1}\\
&-\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
-2\alpha\beta\xi_{n-1}}2,
\end{aligned}
$$


where the $\xi_j$ in this display are the square-arc return, not the normalized source vector. The notation distinguishes them by context; both are completely specified finite original objects.

Thus the remaining $\mathcal W_p$-congruence includes the entire square arc and the entire $K$-arc. It is not a free Gaussian target.

## 19. Explicit factorial evaluation of the surviving numerical equations

The preceding contact identities can be made more concrete without introducing states above $n$, and without assuming that factorial-functional values are units.

For $j\ge1$, define integer Chebyshev weights


$$
w_{j,0}=1,
$$




$$
\boxed{
w_{j,r}
=
2^{2r-1}
\left[
\binom{j+r}{2r}
+\binom{j+r-1}{2r}
\right],
\qquad 1\le r\le j.
}
$$


Then


$$
C_j(t)=(-1)^j\sum_{r=0}^j(-1)^r w_{j,r}t^r.
$$


This is the usual Chebyshev coefficient formula written without a remaining factorial denominator. In particular, no $(2r)!$ is inverted modulo $p$.

The square identity gives


$$
C_m^2=\frac{C_\ell+1}{2}.
$$


Also


$$
\mathcal H(t)=t-t^2+2t^3-2t^4+t^5-t^6,
$$




$$
\mathcal H(1-z)
=4z-12z^2+16z^3-12z^4+5z^5-z^6.
$$



Let $(x+1)_d=(x+1)\cdots(x+d)$. Define the following explicitly expanded degree-six polynomials:


$$
\begin{aligned}
A_6(x)
={}&(x+1)_6-5(x+1)_5+12(x+1)_4\\
&-16(x+1)_3+12(x+1)_2-4(x+1)\\
={}&x^6+16x^5+112x^4+414x^3
+835x^2+850x+332,
\end{aligned}
$$


and


$$
\begin{aligned}
B_6(x)
={}&(x+1)_6+(x+1)_5+2(x+1)_4\\
&+2(x+1)_3+(x+1)_2+(x+1)\\
={}&x^6+22x^5+192x^4+842x^3
+1932x^2+2164x+903.
\end{aligned}
$$



Applying the two factorial functionals term by term gives the exact identities


$$
\boxed{
2U
=
332+\sum_{r=0}^{\ell}
(-1)^r w_{\ell,r}\,r!\,A_6(r),
}
$$




$$
\boxed{
2E_K
=
-903-\sum_{r=0}^{\ell}
w_{\ell,r}\,r!\,B_6(r).
}
$$


For example, the constants arise from


$$
-\eta(\mathcal H)=332,\qquad -E(\mathcal H)=903.
$$


Every factorial originally used in this derivation has index $r+d\le\ell+6=n$.

Hence


$$
\boxed{
-2y_K
=
d_K\left[
903+\sum_{r=0}^{\ell}w_{\ell,r}r!B_6(r)
\right]+2a_K.
}
$$


This is a specified positive integer on the original domain. Positivity does not prevent divisibility by a large prime.

For the square source, put


$$
\mathcal H_j^-=\sum_{r=0}^j(-1)^r w_{j,r}r!,
\qquad
\mathcal H_j^+=\sum_{r=0}^j w_{j,r}r!.
$$


The coefficient formula gives


$$
\eta(C_j)=\mathcal H_j^-,
\qquad
E(C_j)=(-1)^j\mathcal H_j^+.
$$


Using the exact Chebyshev product identities,


$$
\boxed{
V=
\frac{\alpha^2}{2}(\mathcal H_n^-+1)
+\frac{\beta^2}{2}(\mathcal H_{n-2}^-+1)
-\alpha\beta(\mathcal H_{n-1}^--1)
-\delta^2,
}
$$


and


$$
\boxed{
E_F=
\frac{\alpha^2}{2}(\mathcal H_n^++1)
+\frac{\beta^2}{2}(\mathcal H_{n-2}^++1)
+\alpha\beta(\mathcal H_{n-1}^++3).
}
$$


These formulas retain the actual Gaussian division and the exact $-\delta^2$.

### 19.1 The numerical congruence that survives division by $c$

For $p>n$, let


$$
\kappa_V=v_p(V).
$$


For every $h\ge1$,


$$
p^h\mid\gamma
$$


is equivalent to the two conditions


$$
v_p(U)\ge\kappa_V+h,
\qquad
v_p(y_K)\ge h.
$$


Indeed, positive $\tau$-depth means $v_p(U)>v_p(V)$, so the actual content exponent is $c_p=\kappa_V$.

Substituting the evaluations above gives the concrete surviving system


$$
\boxed{
332+\sum_{r=0}^{\ell}
(-1)^r w_{\ell,r}r!A_6(r)
\equiv0\pmod{p^{\kappa_V+h}},
}
$$




$$
\boxed{
d_K\left[
903+\sum_{r=0}^{\ell}w_{\ell,r}r!B_6(r)
\right]+2a_K
\equiv0\pmod{p^h},
}
$$


where $\kappa_V$ is the valuation of the fully displayed actual square-source expression for $V$.

This is not a proof of avoidance. It identifies the outstanding arithmetic content after primitive division.

In particular:

- all original degree-range factorials are units at $p>n$;
- the coefficient arrays and factorial evaluations are nevertheless sums that may vanish modulo $p$;
- neither polynomial coefficient primitivity nor invertibility of the individual factorials makes either displayed sum a unit;
- the $-\delta^2$ in $V$ cannot be dropped before division by $c$. If one first works modulo $p^{2v_p(\delta)}$ and then divides by a nonunit $c$, the available precision decreases.

### 19.2 Precision after primitive and Gaussian division

The exact local relation is


$$
v_p(A)
=
v_p\!\left(
U\mathcal F_{\rm end}+V\mathcal K_{\rm end}
\right)-c_p.
$$


Thus a test for $p^h\mid A$ requires the raw endpoint combination through $p^{c_p+h}$, not merely $p^h$.

Similarly:

- $\tau,\nu\bmod p^h$ require $U,V\bmod p^{c_p+h}$, followed by division by the actual $c$, including its unit part;
- the division $y_K/p^t$ in $\mathcal W_p$ requires numerator precision $p^{t+h}$ for a result modulo $p^h$;
- raw Gaussian quadratic data require the additional $2v_p(g_B)$ precision already specified in the audit;
- arc denominators are units at these large primes, but that does not make their numerators units.

No original-sized computation is requested by this precision ledger.

## 20. What is paid, and the concrete follow-on lemma

The new result pays the discrepancy between $G_{>n}$ and
$r^\circ_{>n}$ by the explicit integer $a_K\delta^2$. It does not bound the remaining contact represented by the two evaluated congruences in Section 19.

A concrete sufficient large-prime follow-on statement is:

> **Large-prime determinant-unit contact bound — open.**  
> Prove, for all original $N$, an absolute constant $C$ such that
> 

$$
> \sum_{\substack{p>2N\\p\nmid\Delta}}
> \left[
> \min\!\left(
> [v_p(U)-v_p(V)]_+,\,v_p(y_K)
> \right)-v_p(a_K)
> \right]_+\log p
> \le CN,
>
$$


> using the actual $U,V,y_K,a_K$ evaluated above.

The summand is exactly $v_p(r^\circ)$. If this lemma were proved, Section 17 would give an exponential bound for the determinant-unit large-prime part of $G$, with the actual Gaussian division included.

This is an **open quantitative contact assertion**, not a new payment merely because it has been written as a sum. Its remaining arithmetic content is the simultaneous congruence of Section 19 at the depths that survive $c$.

Even that lemma would not, by itself, settle the global problem. One would still have to combine all prime ranges and the actual final gcd in a bound for the whole primitive error.

---

# Part IV. Preservation of returns, least denominators, and the whole error

## 21. Both signed returns and the complete Hermite credit remain

The source balance is unchanged:


$$
\begin{aligned}
&(\nu\mathscr A-16\tau\Pi)\Theta_\ell
+(\nu\mathscr B-16\tau\Omega)\Theta_{\ell-1}\\
&\hspace{10mm}=\nu\mathscr C_U-16\tau C^{\rm s}.
\end{aligned}
$$


For


$$
T_{\rm end}=\tau(E_F-\delta^2)+\nu E_K,
$$


the endpoint balance is


$$
\begin{aligned}
16T_{\rm end}={}&
16\tau(C^{\rm e}-\delta^2)+\nu\mathscr C_E\\
&+(\nu\mathscr A-16\tau\Pi)\Phi_\ell
+(\nu\mathscr B-16\tau\Omega)\Phi_{\ell-1}.
\end{aligned}
$$



The source return retains


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



With the actual least $D$, let


$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K),
$$




$$
k_E=D\mathscr C_E-16DR_K,\qquad
f_E=DC^{\rm e}-DR_F.
$$


The endpoint return retains


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


The exact return identity is


$$
\boxed{
z_\ell^{\rm ret}w_{\ell-1}
-z_{\ell-1}^{\rm ret}w_\ell
=-16\Delta(UX+VY).
}
$$



For exactly $0\le b\le N$,


$$
\mathcal R_{b;N}=d_KP_b^{\rm H}U+Q_b^{\rm H}y_K.
$$


With


$$
\Psi_j^{(b)}=Q_b^{\rm H}\Phi_j-P_b^{\rm H}\Theta_j,
$$


the full forcing remains


$$
\Psi_{j+1}^{(b)}+4j\Psi_j^{(b)}-\Psi_{j-1}^{(b)}
=2(Q_b^{\rm H}(-1)^j-P_b^{\rm H}),
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



The established signed payment stays at the actual endpoints:


$$
\mathcal R_{N-1;N}<0<\mathcal R_{N;N},
$$




$$
\frac{c(r^\circ)^2}{\kappa_N^{\rm prod}}
\mid\mathcal R_{N-1;N}\mathcal R_{N;N},
\qquad
v_p(\kappa_N^{\rm prod})=[c_p-H_p]_+.
$$


No factorial divisibility is inferred from the height of these returns.

The closed thirteen-weight representation is not rerun. Its weights remain


$$
(1,8,58,168,399,-176,-916,-176,399,168,58,8,1),
$$


with the original backward steps $1\le k\le11$. Its rational interface remains on $2\le j\le n-1$, with


$$
Q_{\rm loc}(n)=\prod_{b=0}^{12}(n-b),\qquad
\mathcal L_n=\operatorname{lcm}(1,\ldots,n),
$$


and the paid identity


$$
\frac{2\mathcal L_n}{j^2-1}
=\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}.
$$


These clearers do not replace $D$ or $\lambda$.

## 22. The all-prime final gcd and actual primitive denominator

Retain both arcs:


$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


After the independent complete reduction


$$
\tau R_F+\nu R_K=\frac b\lambda,\qquad
\gcd(b,\lambda)=1,\quad\lambda>0,
$$


put


$$
E=\tau E_F+\nu E_K,\qquad A=\lambda E-b,
$$




$$
\boxed{G=\gcd(M,A)}
$$


over **all primes**, and


$$
\boxed{
p_N=A/G,\qquad q_N=\lambda M/G.
}
$$


Since


$$
\gcd(\lambda,A)=\gcd(\lambda,b)=1,
$$


this is the actual primitive rational pair.

The large-prime analysis does not replace $G$ by $G_{>2N}$, nor does it remove the remaining odd primes at most $2N$.

## 23. The nonzero whole error at the same original indices

The original polynomial is still


$$
P_N(t)
=\frac{F(t)^2+(V/U)K(t)}{\delta^2}
=\frac{W_{\rm prim}(t)}M.
$$


It is nonnegative and not identically zero. Its whole error is


$$
\boxed{
\epsilon_N=
\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0.
}
$$



The exact source balance gives


$$
\eta(W_{\rm prim})
=\tau(\delta^2+V)-\nu U=M.
$$


Finite integration by parts gives


$$
\int_0^1e^tW_{\rm prim}(t)\,dt=eM-E,
$$


while both complete arcs give


$$
4\int_0^1\frac{W_{\rm prim}(t)}{1+t^2}\,dt
=\pi M+\frac b\lambda.
$$


Therefore


$$
\epsilon_N=e+\pi-\frac{A}{\lambda M},
$$


and, at the same original indices,


$$
\boxed{
q_N(e+\pi)-p_N=q_N\epsilon_N>0.
}
$$



The retained rational enclosure is


$$
3J_N<\epsilon_N<7J_N,
\qquad
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


Both are positive polynomial integrals. Thus


$$
\boxed{
q_NJ_N
=\frac{\lambda_N}{G_N}
\bigl(\tau_NJ_F+\nu_NJ_K\bigr),
}
$$


with **both positive summands retained**.

An irrationality conclusion would follow from


$$
q_N\epsilon_N\longrightarrow0
$$


along an infinite sequence of these same original indices: a nonzero integer-linear error for a rational number cannot approach zero. No such limit is established here.

---

# Part V. Proof, conditional, finite-check, and open ledger

## 24. New proved results

The following are proved in this report, without numerical computation:

1. The complete different audit of A5 Turn 23’s new algebraic claims passes at the exact scopes stated above.
2. The actual reduced arc clearers satisfy
   

$$
D,\lambda\mid\operatorname{lcm}(1,3,\ldots,2N-1),
$$


   with exact all-cancellation reduction formulas.
3. The prime $2$ contributes neither to $D,\lambda$ nor to the final $G$; the actual primitive numerator and denominator are odd.
4. Theorem 16.1 gives the complete large-prime valuation conditions, including the $p\mid\tau$ versus $p\mid\delta$ distinction and the residual endpoint carry.
5. The large-prime parts of $G$ and $q_N$ differ from the specified $\gamma$- and $\tau/\gamma$-parts only by divisors of $\delta^2$.
6. The excess beyond $r^\circ_{>2N}$ has the explicit bill $a_K\delta^2$.
7. The surviving primitive contact has the explicit factorial evaluations and congruences in Section 19.

## 25. Conditional implications

- Nonvanishing of the two fourth-depth residues in A5 Turn 23 would settle its primary fourth-depth source-separation case.
- The open contact-mass lemma of Section 20 would give an exponential bill for the determinant-unit large-prime part of the endpoint gcd.
- A proof that the **whole**
  

$$
\frac{\lambda_N}{G_N}(\tau_NJ_F+\nu_NJ_K)
$$


  tends to zero would prove irrationality of $e+\pi$.

None of these premises is proved here.

## 26. Exact remaining bottlenecks

There are two distinct outstanding numerical issues.

### 26.1 Audited interval problem

Under the actual primary third collision, one must still exclude simultaneous vanishing of


$$
\frac{Z_0+pZ_1+p^2Z_2+p^3Z_3}{p^3}\pmod p
$$


and


$$
\frac1{p^2}\left[
\frac{4^{p-1}-1}{p}
-\frac{(p+1)d_i-v_i}{p\,v_i}
\right]\pmod p.
$$


All divisions are paid, but numerical noncoincidence remains unproved.

### 26.2 Large-prime endpoint problem

At determinant-unit $p>2N$, the unresolved contact is the actual simultaneous divisibility in Section 19, after the content exponent $c_p$ has been removed. At primes dividing $\delta$, the remaining additional depth is the explicitly evaluated


$$
v_p(\mathcal W_p)
$$


truncated at $2v_p(\delta)$.

The determinant-deep theorem cannot be transferred to these unit primes. The fact that all degree-range factorials are units does not settle either numerical contact.

## 27. Bounded arithmetic and computation status

No tools were used. No original-sized solve, prime scan, prior receipt, or closed expensive calculation is requested.

The only new coefficient arithmetic is a degree-six polynomial expansion. Its bounded inputs are the six rising factorials $(x+1)_d$, $1\le d\le6$, with coefficient vectors


$$
(-4,12,-16,12,-5,1)
\quad\text{and}\quad
(1,1,2,2,1,1).
$$


The expected verifiable outputs, in ascending powers of $x$, are


$$
\boxed{(332,850,835,414,112,16,1)}
$$


and


$$
\boxed{(903,2164,1932,842,192,22,1)}.
$$


Those expansions and their derivation have already been displayed. Checking them is an auxiliary finite algebra check, not evidence for an infinite noncollision theorem.

There is no pending external computation needed for the proved results. A finite evaluation at a certified original pair could establish only that pair.

---

# Final conclusion

The complete A5 Turn 23 audit passes. Its common-$\rho_p$ elimination is genuine, its pivot is validated in the original divided Gaussian objects, its cubic compatibility retains all additive carry, and its endpoint quadratic supplies no independent third constraint. It does **not** prove numerical noncollision.

The separate large-prime investigation proves more than a formal renaming of $G$: it establishes the support of the **actual reduced** arc clearers, pays the prime $2$, derives exact large-prime valuations of both $G_N$ and the **actual primitive denominator**, and bounds the discrepancy from the surviving $K$-endpoint contact by the explicit divided-Gaussian factor $a_K\delta^2$.

What remains is concrete arithmetic: the specified alternating and nonalternating factorial evaluations must be controlled at the depths surviving $c$, together with the full endpoint carry at primes dividing $\delta$. No theorem here bounds that contact sufficiently to control the whole primitive error.

All original indices, finite boundaries, forcing returns, Gaussian and source divisions, actual contents, least clearers, Hermite credit at $N-1,N$, both arcs, the **all-prime** final gcd, and both positive summands of $q_NJ_N$ remain intact at


$$
\boxed{N=9^{18+32u}.}
$$



**The rationality or irrationality of $e+\pi$ remains unresolved.**
