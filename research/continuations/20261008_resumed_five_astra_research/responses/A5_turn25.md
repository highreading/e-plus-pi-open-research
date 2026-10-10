> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# An actual norm–reflection certificate for Gaussian source contact

## Abstract

This report has two separate outcomes.

1. **Different audit of the new normalization-rigidity corollary in A3turn22 §3.8:** the corollary is correct with its stated convention $D'>0$. Every integer realization of the **same two mixed ratios** is a positive integer multiple of the actual primitive triple. The factorial-height consequences remain pointwise. They neither establish an infinite family of eligible pairs nor apply automatically to FULL24’s different compatibility value.

2. **New research on the actual Gaussian source:** an explicit norm certificate is derived from the complete physical-terminal source, both real and imaginary Gaussian norm equations, and the prescribed prime-half data. Its four factors are identified. One is the original raw source $4g_B^2V$; a second is an **actual reflected Gaussian source**, involving the adjacent values at $p-N,p-N+1$, while keeping the original physical moment index $N$. That reflected source is proved positive.

The resulting certificate is an integer polynomial of total degree at most $16$ in the real and imaginary parts of the **evaluated normalized Gaussian Lucas quotient**. Its contact multiplicities are exact. In particular, on an explicitly testable regular class with $p\equiv3,5\pmod8$, fourth source contact imposes a fully displayed congruence on the three prescribed binomial-harmonic sums. A singular-gradient subcase gives an exclusion test using only the first two Gaussian harmonic levels.

These are new proved restrictions, not a proof of universal fourth-contact separation. No original pair satisfying simultaneous fourth contact is exhibited, and no such pair is ruled out merely by its residue class modulo $8$. The rationality or irrationality of $e+\pi$ remains unresolved.

---

## 1. Different audit: normalization rigidity, and only normalization rigidity

The object under audit is the additional corollary in A3turn22 §3.8, not that source’s audit of FULL21.

Let


$$
(A_{\rm mix},B_{\rm mix},D_{\rm mix})\in\mathbb Z^3,
\qquad D_{\rm mix}>0,
$$


be the actual primitive triple:


$$
\gcd(A_{\rm mix},B_{\rm mix},D_{\rm mix})=1.
$$


Its two ratios are


$$
\frac{A_{\rm mix}}{D_{\rm mix}},
\qquad
\frac{B_{\rm mix}}{D_{\rm mix}}.
$$



### Proposition 1.1 — Exact rigidity

Suppose


$$
A',B'\in\mathbb Z,\qquad D'\in\mathbb Z_{>0},
$$


and


$$
\frac{A'}{D'}=\frac{A_{\rm mix}}{D_{\rm mix}},
\qquad
\frac{B'}{D'}=\frac{B_{\rm mix}}{D_{\rm mix}}.
$$


Then there is a positive integer $t$ such that


$$
(A',B',D')=t(A_{\rm mix},B_{\rm mix},D_{\rm mix}).
$$



#### Proof

Set $t=D'/D_{\rm mix}\in\mathbb Q_{>0}$. Equality of the two ratios gives


$$
A'=tA_{\rm mix},\qquad B'=tB_{\rm mix}.
$$


Primitivity of the triple supplies integers $u,v,w$ satisfying


$$
uA_{\rm mix}+vB_{\rm mix}+wD_{\rm mix}=1.
$$


Multiplying by $t$,


$$
t=uA'+vB'+wD'\in\mathbb Z.
$$


Since $D',D_{\rm mix}>0$, this integer is positive. ∎

This proof does **not** require
$\gcd(A_{\rm mix},B_{\rm mix})=1$. Primitivity of the triple is the correct hypothesis.

The sign convention is essential. Without $D'>0$, the multiplier need not be positive. A zero denominator is not an integer realization of either ratio.

### Pointwise height consequence

At each original pair to which the retained FULL21 estimates apply, with


$$
a=\frac{p-1}{2},
$$


one already has


$$
\max(|A_{\rm mix}|,|B_{\rm mix}|)
\ge N^ae^{-16N},
\qquad
D_{\rm mix}\ge N^ae^{-28N}.
$$


Therefore Proposition 1.1 gives, at that same pair,


$$
\max(|A'|,|B'|)\ge N^ae^{-16N},
\qquad
D'\ge N^ae^{-28N}.
$$



**Audit outcome: PASS.** No repair is needed beyond retaining the stated positive-denominator convention.

This conclusion does not assert that eligible pairs occur for infinitely many original $N$. It also does not transfer these height lower bounds to FULL24’s compatibility value or to the new certificate below: those are different invariants.

---

## 2. Original scope and retained source data

Throughout,


$$
\boxed{N=9^{18+32u}=3^{36+64u},\qquad u\ge0,}
$$


and


$$
n=2N,\qquad m=N-3,\qquad \ell=n-6.
$$



Let


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


with


$$
C_0=1,\quad C_1=2t-1,\quad
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
F=\alpha C_N-\beta C_{N-1},\qquad F(\pm i)=\delta.
$$



For an integer polynomial $H$, retain


$$
\eta(H)=\sum_jj![z^j]H(1-z),
\qquad
E(H)=\sum_j(-1)^jj![t^j]H(t).
$$


Set


$$
\mathcal H=t(1-t)(1+t^2)^2,\qquad K=\mathcal H C_m^2,
$$




$$
U=-\eta(K),\qquad V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
$$


The established original-domain normalization remains


$$
\operatorname{cont}(W_{\rm raw})=g_B^2c,
$$




$$
\tau=U/c,\qquad \nu=V/c,\qquad
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2,
$$


with $U,V,M>0$.

### 2.1 Literal membership and credit

The prime set is unchanged:


$$
\mathcal S_N=
\left\{
\begin{array}{l|l}
p&
N<p<2N,\quad p\nmid L(\ell^2),\\
&d_{p,N}^{\rm block}=p^2,\quad
v_p(\Delta)\le v_p(J_N^{\rm aff})
\end{array}
\right\},
$$


where


$$
L(x)=(x-1)(x-9)(x-25).
$$


The original finite-block condition is retained literally. No converse characterization of membership from source congruences is asserted.

For $p\in\mathcal S_N$, write


$$
r=n-p,\qquad s=r-6,\qquad
a=\frac{p-1}{2},\qquad k=a+1,\qquad \chi=2k!.
$$


The retained boundaries are


$$
\boxed{13\le r<N,\quad s\ge7,\quad r,s\text{ odd},\quad k\le N-6.}
$$


Also $p^2\mid U,V$ and $p\nmid d_K$.

The actual credit remains


$$
H_p=h_p+2b_p+2(z_p-t_p)_+,
$$


where


$$
c_p=\min(v_p(U),v_p(V)),\qquad t_p=v_p(U)-c_p,
$$




$$
z_p=v_p(y_K),\quad b_p=v_p(b^\circ),\quad
h_p=v_p(Q_{N-1}^{\rm H}Q_N^{\rm H}).
$$


Consequently,


$$
B_p=(H_p-2)_+,\qquad
e_p=[c_p-2-B_p]_+,\qquad
j_p=v_p(J_N^{\rm aff}).
$$



The primary hypotheses are


$$
\boxed{p\in\mathcal S_N,\qquad B_p=j_p=0,\qquad p^3\mid U,V.}
\tag{2.1}
$$



### 2.2 Complete finite columns

The states are defined only for $0\le j\le n$, with


$$
\Theta_0=\Phi_0=0,\qquad \Theta_1=\Phi_1=1,
$$


and, for exactly $1\le j\le n-1$,


$$
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2,
$$




$$
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j.
\tag{2.2}
$$



At $x=\ell^2$, let


$$
\begin{aligned}
\mathcal P&=-8x^3-1116x^2-8150x+151,\\
\mathcal Q&=76x^2+2408x+5637,\\
\mathcal F&=4x^2+492x+5463,\\
\mathcal G&=4x^2+556x-3325,
\end{aligned}
$$




$$
\mathscr A=2\ell((2\ell+1)\mathcal Q-\mathcal P),\qquad
\mathscr B=-2\ell\mathcal Q,
$$




$$
\mathscr C_U=\mathcal F-\mathcal P+2\ell\mathcal Q,\qquad
\mathscr C_E=\mathcal G+\mathcal P-2(\ell+1)\mathcal Q.
$$


The $K$-columns are


$$
16U=\mathscr C_U-\mathscr A\Theta_\ell-\mathscr B\Theta_{\ell-1},
$$




$$
16E_K=\mathscr C_E+\mathscr A\Phi_\ell+\mathscr B\Phi_{\ell-1}.
\tag{2.3}
$$



The Gaussian columns at the physical terminal are


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
\boxed{C_V=\alpha^2+(2n-3)\beta^2-\delta^2,}
$$




$$
\boxed{C_F^E=\alpha^2+(5-2n)\beta^2+4\alpha\beta.}
\tag{2.5}
$$



For


$$
T_j=\begin{pmatrix}-4j&1\\1&0\end{pmatrix},
\qquad T=T_{\ell+5}\cdots T_\ell,
$$


the full six-step returns are


$$
f_0=g_0=0,
$$




$$
f_{j+1}=T_{\ell+j}f_j+\binom20,\qquad
g_{j+1}=T_{\ell+j}g_j+\binom{2(-1)^j}{0},
\quad 0\le j\le5.
$$


Thus


$$
(\Pi,\Omega)=(P,Q)T,
$$




$$
C^{\rm s}=C_V-(P,Q)f_6,\qquad
C^{\rm e}=C_F^E-(P,Q)g_6.
$$



The conditioning quantities remain


$$
\Delta=\mathscr A\Omega-\mathscr B\Pi<0,
$$




$$
\mathscr I_1=\Pi\mathscr C_U-\mathscr A C^{\rm s},\qquad
\mathscr I_2=\Omega\mathscr C_U-\mathscr B C^{\rm s},
$$




$$
J_N^{\rm aff}=\gcd(\mathscr I_1,\mathscr I_2).
$$


The separate established bills are reused:


$$
0<|\Delta|<3\cdot10^9n^{14}\frac{5^{2N}}{g_B^2},
$$




$$
J_N^{\rm aff}<10^{10}n^{15}\frac{5^{4N}}{g_B^2}.
$$


The $\delta^2$-terms in the second bill are not removed by the first.

---

## 3. The evaluated inputs: no free Gaussian or quotient digits

The prime-half identities and exact products from FULL23–24 are reused here at their stated scope. Their pending different review is not represented as completed by this report.

Put


$$
w=-1+2i,\qquad z=-1+i.
$$


Let


$$
\mathsf U_{-1}=0,\quad \mathsf U_0=1,\quad
\mathsf U_{h+1}=2w\mathsf U_h-\mathsf U_{h-1},
$$




$$
D_h=\mathsf U_h-\mathsf U_{h-1},\qquad
E_h=\mathsf U_h+\mathsf U_{h-1}.
$$


For


$$
h=\frac{r-1}{2},
$$


FULL24 gives


$$
C_N(i)=D_h\mathsf X_p+E_h\mathsf Y_p,
$$




$$
C_{N-1}(i)=D_{h-1}\mathsf X_p+E_{h-1}\mathsf Y_p,
\tag{3.1}
$$


and


$$
\mathsf X_p^2=i+\frac{i}{z}\mathsf Y_p^2.
\tag{3.2}
$$



### 3.1 An exact normalization by $z$

Every summand defining $\mathsf Y_p$ is divisible by $z$. Define


$$
Z_p=\frac{\mathsf Y_p}{z}\in\mathbb Z[i],
\qquad
Z_0=z^a,
$$


and


$$
\mathcal L_p=\frac{\mathsf Y_p-\Gamma_p}{pz}\in\mathbb Z[i],
\qquad
\Gamma_p=z^{a+1}.
$$


Then


$$
\boxed{Z_p=Z_0+p\mathcal L_p.}
\tag{3.3}
$$


This is an exact Gaussian-integer division. At every prime under study, $z$ is a unit because $z\bar z=2$.

The evaluated quotient is


$$
\boxed{
\mathcal L_p=
\sum_{\substack{1\le j\le p-2\\j\ {\rm odd}}}
\frac{i^{(p-j)/2}z^{(j-1)/2}}{j}
\prod_{t=1}^{j-1}\left(1-\frac pt\right).
}
\tag{3.4}
$$


It is not an adjustable parameter.

For fourth precision, define


$$
\Lambda_0=
\sum_{\substack{1\le j\le p-2\\j\ {\rm odd}}}
\frac{i^{(p-j)/2}z^{(j-1)/2}}j,
$$




$$
\Lambda_1=
\sum_{\substack{1\le j\le p-2\\j\ {\rm odd}}}
\frac{i^{(p-j)/2}z^{(j-1)/2}}j\,H_{j-1},
$$




$$
\Lambda_2=
\frac12
\sum_{\substack{1\le j\le p-2\\j\ {\rm odd}}}
\frac{i^{(p-j)/2}z^{(j-1)/2}}j
\bigl(H_{j-1}^2-H_{j-1}^{(2)}\bigr).
$$


Then


$$
\boxed{
Z_p\equiv
Z_0+p\Lambda_0-p^2\Lambda_1+p^3\Lambda_2
\pmod{p^4}.
}
\tag{3.5}
$$


Every denominator displayed here is a $p$-adic unit.

### 3.2 Both real and imaginary norm equations

For a Gaussian variable $Z=x+iy$, put


$$
\sigma(Z)=i+izZ^2.
$$


Equation (3.2) becomes


$$
\boxed{\mathsf X_p^2=\sigma(Z_p).}
\tag{3.6}
$$


Explicitly,


$$
\operatorname{Re}\sigma=-x^2+y^2+2xy,
$$




$$
\operatorname{Im}\sigma=1-x^2+y^2-2xy.
\tag{3.7}
$$


If $\mathsf X_p=u+iv$, the two constraints are therefore


$$
u^2-v^2=-x^2+y^2+2xy,
$$




$$
2uv=1-x^2+y^2-2xy.
\tag{3.8}
$$


In particular,


$$
R_p:=|\mathsf X_p|^2\in\mathbb Z_{>0},
$$


and


$$
\boxed{
R_p^2
=|\sigma(Z_p)|^2
=2(x^2+y^2)^2-2x^2+2y^2-4xy+1.
}
\tag{3.9}
$$



The selected roots are prescribed:


$$
\mathsf X_p\equiv I_p:=i^{(p+1)/2}\pmod p,
\qquad
R_p\equiv1\pmod p.
\tag{3.10}
$$


Thus neither the sign of $\mathsf X_p$ nor the sign of the real norm root is free locally.

### 3.3 The prescribed $\Gamma_p$ and the common Hermite scalar

The exact coupling is


$$
\boxed{
\Gamma_p^8=16\,4^{p-1},
\qquad
\rho_p=\frac{\Gamma_p^8}{16(p+1)}.
}
\tag{3.11}
$$


For $p=8t+c$, let $\vartheta=(-4)^t$. The actual leading values are:

| $c=p\bmod8$ | $I_p$ | $\Gamma_p$ | $Z_0=\Gamma_p/z$ | $v_p(g_B)$ |
|---|---:|---:|---:|---:|
| $1$ | $i$ | $\vartheta z$ | $\vartheta$ | may be positive |
| $3$ | $-1$ | $-2i\vartheta$ | $\vartheta z$ | $0$ |
| $5$ | $-i$ | $2(1+i)\vartheta$ | $-2i\vartheta$ | $0$ |
| $7$ | $1$ | $-4\vartheta$ | $2(1+i)\vartheta$ | may be positive |

Also


$$
|Z_0|^2=2^a\equiv\left(\frac2p\right)\pmod p.
$$


Since the original $N\equiv1\pmod8$,


$$
r\equiv2-p\pmod8.
$$


Thus the short index $h=(r-1)/2$ is still the actual one; it has not been chosen independently of $p,N$.

### 3.4 Complete Hermite data entering the coefficients

The Hermite sequences retain their range $0\le b\le N$:


$$
P_0^{\rm H}=Q_0^{\rm H}=1,\qquad
P_1^{\rm H}=3,\quad Q_1^{\rm H}=1,
$$




$$
Z_{b+1}=(4b+2)Z_b+Z_{b-1},
\qquad 1\le b\le N-1.
$$



For $0\le h'\le a$, and $1\le j\le a$, define


$$
\mathsf h_{a,h'}=\frac{(2a-h')!}{(a-h')!\,h'!},
\qquad
\mathsf b_j=\frac{4^j j!((j-1)!)^2}{2(2j)!},
$$




$$
\mathsf S_{p,h'}=
\prod_{t=1}^{h'}
\frac{(1-2p/(2t-1))(1-p/t)}
     {(1-2p/t)(1-p/(2t-1))},
$$




$$
\mathsf T_{p,j}=
\prod_{v=1}^{j-1}\left(1-\frac{p^2}{v^2}\right).
$$


Use the weights


$$
A_{h'}^+=2h'^2-p(2h'+1),
$$




$$
\widetilde A_{h'}^-=2h'(h'-2)-p(2h'-1),
\qquad
A_j^-=2j(j+2)-p(2j+3).
$$


The four exact vectors are


$$
\mathbf A_p^+
=\chi
\binom{\sum_{h'=0}^a(-1)^{h'}\mathsf h_{a,h'}\mathsf S_{p,h'}}
{\dfrac1{p-1}\sum_{h'=0}^a(-1)^{h'}A_{h'}^+
       \mathsf h_{a,h'}\mathsf S_{p,h'}},
$$




$$
\mathbf A_p^-
=\chi
\binom{\sum_{h'=0}^a\mathsf h_{a,h'}\mathsf S_{p,h'}}
{\dfrac1{p-1}\sum_{h'=0}^a\widetilde A_{h'}^-
       \mathsf h_{a,h'}\mathsf S_{p,h'}},
$$




$$
\mathbf L_p^+
=\binom{p\sum_{j=1}^a\mathsf b_j\mathsf T_{p,j}}
{\dfrac{1+p\sum_{j=1}^a A_j^+\mathsf b_j\mathsf T_{p,j}}{p-1}},
$$




$$
\mathbf L_p^-
=\binom{p\sum_{j=1}^a(-1)^{j+1}\mathsf b_j\mathsf T_{p,j}}
{\dfrac{-1+p\sum_{j=1}^a(-1)^{j+1}A_j^-\mathsf b_j\mathsf T_{p,j}}{p-1}}.
\tag{3.12}
$$


The lower constants $+1,-1$ remain present.

For $0\le j\le r$,


$$
S_0=I,\qquad \mathbf h_0^+=\mathbf h_0^-=0,
$$




$$
S_{j+1}=T_{p+j}S_j,
$$




$$
\mathbf h_{j+1}^+=T_{p+j}\mathbf h_j^++\binom20,
$$




$$
\mathbf h_{j+1}^-=T_{p+j}\mathbf h_j^--\binom{2(-1)^j}{0}.
\tag{3.13}
$$


Then


$$
\binom{\Theta_{p+j}}{\Theta_{p+j-1}}
=\rho_pS_j\mathbf A_p^++S_j\mathbf L_p^++\mathbf h_j^+,
$$




$$
\binom{\Phi_{p+j}}{\Phi_{p+j-1}}
=\rho_pS_j\mathbf A_p^-+S_j\mathbf L_p^-+\mathbf h_j^-.
\tag{3.14}
$$


The last step is $p+r-1=n-1$. Thus every terminal state used below includes the actual products, the prescribed $\Gamma_p^8$, and the complete forcing return.

In particular, with


$$
v_1=(\mathscr A,\mathscr B)S_s\mathbf A_p^+,
$$




$$
d_1=\mathscr C_U-(\mathscr A,\mathscr B)
       (S_s\mathbf L_p^++\mathbf h_s^+),
$$


the first source is equivalently


$$
\boxed{
\mathcal F_{p,N}^{\Gamma}
:=16(p+1)d_1-\Gamma_p^8v_1
=256(p+1)U.
}
\tag{3.15}
$$


No unit assumption on $v_1$ and no division by $\Delta$ is used in this identity.

---

## 4. A new, explicit polynomial reduction of the complete second source

This section begins the new derivation.

### 4.1 A terminal quadratic form retaining $-\delta^2$

Set


$$
Q_{00}=1-n\Theta_n,
$$




$$
Q_{01}=(n-1)\Theta_{n-1},
$$




$$
\begin{aligned}
Q_{11}
&=(2n-3)-(n-2)\Theta_n
       -4(n-1)(n-2)\Theta_{n-1}\\
&=1-(n-2)\Theta_{n-2}.
\end{aligned}
\tag{4.1}
$$


The second equality uses exactly the recurrence step $n-1$.

Writing


$$
B_-=b_{N-1},\qquad B_+=b_N,\qquad
D_G=a_Nb_{N-1}-a_{N-1}b_N,
$$


the complete source is


$$
\boxed{
g_B^2V
=Q_{00}B_-^2+2Q_{01}B_-B_++Q_{11}B_+^2-D_G^2.
}
\tag{4.2}
$$


The final term is the complete raw $-\delta^2$-contribution.

For use with $Z_p=\mathsf Y_p/z$, define


$$
d_-=D_{h-1},\quad e_-=zE_{h-1},\qquad
d_+=D_h,\quad e_+=zE_h.
$$


Thus


$$
G_-=d_-\mathsf X_p+e_-Z_p=C_{N-1}(i),
$$




$$
G_+=d_+\mathsf X_p+e_+Z_p=C_N(i).
\tag{4.3}
$$



Let


$$
\mathcal E_\pm=G_\pm-\overline{G_\pm},
\qquad
\mathcal J=G_-\overline{G_+}-G_+\overline{G_-}.
$$


Then


$$
\mathcal E_\pm=2iB_\pm,\qquad
\mathcal J=2iD_G.
$$


Consequently,


$$
\boxed{
4g_B^2V=
\mathcal J^2-
\left(Q_{00}\mathcal E_-^2
+2Q_{01}\mathcal E_-\mathcal E_+
+Q_{11}\mathcal E_+^2\right).
}
\tag{4.4}
$$



### 4.2 Explicit reduction using both norm equations

In this subsection $Z=x+iy$ is a polynomial variable. Work with formal $X,\bar X$ satisfying


$$
X^2=\sigma(Z),\qquad \bar X^2=\overline{\sigma(Z)}.
$$


These monic relations permit reduction to the basis


$$
1,\ X,\ \bar X,\ X\bar X.
$$


No field or irreducibility assumption is required.

Put


$$
r_-=e_-Z-\bar e_-\bar Z,\qquad
r_+=e_+Z-\bar e_+\bar Z,
$$


and


$$
\begin{aligned}
j_0&=(e_-\bar e_+-e_+\bar e_-)Z\bar Z,\\
j_1&=(d_-\bar e_+-d_+\bar e_-)\bar Z,\\
j_2&=(e_-\bar d_+-e_+\bar d_-)Z=-\bar j_1,\\
j_3&=d_-\bar d_+-d_+\bar d_-.
\end{aligned}
\tag{4.5}
$$


Then


$$
\mathcal J=j_0+j_1X+j_2\bar X+j_3X\bar X.
$$



Define


$$
\begin{aligned}
\mathcal Q_0={}&
Q_{00}(r_-^2+d_-^2\sigma+\bar d_-^2\bar\sigma)\\
&+2Q_{01}(r_-r_++d_-d_+\sigma+\bar d_-\bar d_+\bar\sigma)\\
&+Q_{11}(r_+^2+d_+^2\sigma+\bar d_+^2\bar\sigma),
\end{aligned}
$$




$$
\mathcal Q_1=
2\left[
Q_{00}r_-d_-+
Q_{01}(r_-d_++r_+d_-)+
Q_{11}r_+d_+
\right],
$$




$$
\mathcal Q_{11}=
-2\left[
Q_{00}|d_-|^2+
Q_{01}(d_-\bar d_++d_+\bar d_-)+
Q_{11}|d_+|^2
\right].
\tag{4.6}
$$



Now set


$$
\boxed{
A_\star=
j_0^2+j_1^2\sigma+j_2^2\bar\sigma
+j_3^2\sigma\bar\sigma-\mathcal Q_0,
}
$$




$$
\boxed{
B_\star=
2(j_0j_1+j_2j_3\bar\sigma)-\mathcal Q_1,
}
$$




$$
\boxed{
D_\star=
2(j_0j_3+j_1j_2)-\mathcal Q_{11}.
}
\tag{4.7}
$$


Here


$$
A_\star,D_\star\in\mathbb Z[x,y],
\qquad
B_\star\in\mathbb Z[i][x,y].
$$


The reduced polynomial in (4.4) is exactly


$$
\boxed{
A_\star+B_\star X+\bar B_\star\bar X+D_\star X\bar X.
}
\tag{4.8}
$$



#### Verification of the new reduction

Squaring


$$
j_0+j_1X+j_2\bar X+j_3X\bar X
$$


and replacing $X^2,\bar X^2$ gives:

- constant coefficient
  

$$
j_0^2+j_1^2\sigma+j_2^2\bar\sigma+j_3^2\sigma\bar\sigma;
$$


- coefficient of $X$
  

$$
2(j_0j_1+j_2j_3\bar\sigma);
$$


- coefficient of $\bar X$, the conjugate of the preceding coefficient;
- coefficient of $X\bar X$
  

$$
2(j_0j_3+j_1j_2).
$$



Expanding the quadratic form in $\mathcal E_\pm$ gives respectively
$\mathcal Q_0,\mathcal Q_1,\bar{\mathcal Q}_1,\mathcal Q_{11}$.
Subtracting proves (4.7)–(4.8).

The conjugation relations in (4.5) also prove that $A_\star,D_\star$ are real integer polynomials. This establishes integrality coefficient by coefficient.

---

## 5. The actual four-sign norm and its reflected source

### 5.1 The integer norm polynomial

Define


$$
K_\star=A_\star D_\star-|B_\star|^2,
$$




$$
H_\star=
A_\star^2+D_\star^2|\sigma|^2
-2\operatorname{Re}(B_\star^2\sigma),
$$


and


$$
\boxed{
\mathscr P_{p,N}(x,y)
=H_\star^2-4K_\star^2|\sigma|^2
\in\mathbb Z[x,y].
}
\tag{5.1}
$$



All its coefficients are explicitly given by (4.1), (4.5)–(4.7), with the complete terminal states evaluated by (3.12)–(3.14). Thus $\Gamma_p^8$ remains in the actual Hermite data entering these coefficients.

The degree bounds are


$$
\deg A_\star\le4,\qquad
\deg B_\star\le3,\qquad
\deg D_\star\le2,
$$


hence


$$
\boxed{\deg\mathscr P_{p,N}\le16.}
\tag{5.2}
$$



At the actual $Z_p$, abbreviate $A_\star(Z_p),B_\star(Z_p),D_\star(Z_p)$ by $A_\star,B_\star,D_\star$, and put


$$
\mathcal C_\pm=H_\star\pm2R_pK_\star.
$$


Then


$$
\mathscr P_{p,N}(\operatorname{Re}Z_p,\operatorname{Im}Z_p)
=\mathcal C_+\mathcal C_-.
\tag{5.3}
$$



More explicitly,


$$
\mathcal C_+
=(A_\star+D_\star R_p)^2
-4\operatorname{Re}(B_\star\mathsf X_p)^2,
$$




$$
\boxed{
\mathcal C_-=
(A_\star-D_\star R_p)^2
+4\operatorname{Im}(B_\star\mathsf X_p)^2.
}
\tag{5.4}
$$



To verify these identities, use


$$
2\operatorname{Re}(B_\star\mathsf X_p)^2
=|B_\star|^2R_p+\operatorname{Re}(B_\star^2\sigma),
$$


and the corresponding identity for the imaginary part. No resultant is left unnamed: (5.1) is the evaluated four-sign product.

### 5.2 The second real factor is an actual reflected Gaussian value

Set


$$
J=p-N.
$$


The original boundaries imply


$$
2\le J\le N-13,\qquad J+1\le N-12.
$$


Thus all reflected Gaussian indices lie inside the original finite range.

The half-angle identities already used in FULL24 also give the difference-angle formulas


$$
D_h\mathsf X_p-E_h\mathsf Y_p=C_{p-N}(i),
$$




$$
D_{h-1}\mathsf X_p-E_{h-1}\mathsf Y_p=C_{p-N+1}(i).
\tag{5.5}
$$


Indeed, replacing the addition of the prime and residual half-angles by their difference changes exactly the sign of the $E_h\mathsf Y_p$ term.

Therefore changing $\mathsf X_p$ to $-\mathsf X_p$, while retaining the actual $\mathsf Y_p$, gives


$$
G_-^\dagger=-C_{J+1}(i),\qquad
G_+^\dagger=-C_J(i).
\tag{5.6}
$$



Define the integer


$$
D^\dagger=a_Jb_{J+1}-a_{J+1}b_J
$$


and the **reflected source value**


$$
\boxed{
V^\dagger_{p,N}
=
Q_{00}b_{J+1}^2
+2Q_{01}b_{J+1}b_J
+Q_{11}b_J^2
-(D^\dagger)^2.
}
\tag{5.7}
$$


The moment coefficients are still those at the physical index $N$. This is an auxiliary reflected value, not a replacement original producer.

Equations (4.4), (4.8), and (5.6) prove


$$
A_\star+D_\star R_p+2\operatorname{Re}(B_\star\mathsf X_p)
=4g_B^2V,
$$




$$
A_\star+D_\star R_p-2\operatorname{Re}(B_\star\mathsf X_p)
=4V^\dagger_{p,N}.
$$


Consequently,


$$
\boxed{
\mathcal C_+=16g_B^2V\,V^\dagger_{p,N},
}
\tag{5.8}
$$


and


$$
\boxed{
\mathscr P_{p,N}(\operatorname{Re}Z_p,\operatorname{Im}Z_p)
=
16g_B^2V\,V^\dagger_{p,N}\,\mathcal C_-.
}
\tag{5.9}
$$



This is an actual value identity. It is stronger information than the statement that some polynomial coefficient or formal resultant is nonzero.

### 5.3 The reflected source is positive

We prove a needed nonvanishing statement about the actual factor in (5.8).

The finite moment identities and Chebyshev product formulas give, for arbitrary real $u,v$,


$$
\eta\bigl((uC_N-vC_{N-1})^2\bigr)
=Q_{00}u^2+2Q_{01}uv+Q_{11}v^2.
\tag{5.10}
$$


In particular,


$$
V^\dagger_{p,N}
=\eta\bigl((b_{J+1}C_N-b_JC_{N-1})^2\bigr)-(D^\dagger)^2.
$$



We use the following elementary moment lower bound.

### Lemma 5.1

If a real polynomial $H$ has degree $d$ and leading coefficient $h_d$, then


$$
\int_0^\infty e^{-x}H(x)^2\,dx\ge (h_dd!)^2.
$$



#### Proof

Let


$$
L_d(x)=\sum_{j=0}^d(-1)^j\binom dj\frac{x^j}{j!}.
$$


Its Rodrigues expression is


$$
L_d(x)=\frac{e^x}{d!}\frac{d^d}{dx^d}(e^{-x}x^d).
$$


Repeated integration by parts gives


$$
\int_0^\infty e^{-x}H(x)L_d(x)\,dx=(-1)^dh_dd!.
$$


Applying the same identity to $H=L_d$ gives


$$
\int_0^\infty e^{-x}L_d(x)^2\,dx=1.
$$


Cauchy–Schwarz proves the assertion. ∎

The adjacent imaginary coefficients $b_J,b_{J+1}$ are not both zero, by the retained Gaussian adjacent-value nonvanishing. Hence


$$
b_{J+1}C_N-b_JC_{N-1}
$$


has degree at least $N-1$, with a nonzero integer multiple of the Chebyshev leading coefficient. Since


$$
\eta(H^2)=\int_0^\infty e^{-x}H(1-x)^2\,dx,
$$


Lemma 5.1 gives


$$
\eta\bigl((b_{J+1}C_N-b_JC_{N-1})^2\bigr)
\ge 2^{4N-6}((N-1)!)^2.
\tag{5.11}
$$



The retained Gaussian bound $|C_j(i)|\le5^j$ gives


$$
|D^\dagger|
\le |C_J(i)|\,|C_{J+1}(i)|
\le5^{2J+1},
$$


and therefore


$$
(D^\dagger)^2\le5^{4N-50}.
$$


For the original $N$, the lower bound (5.11) is larger than $5^{4N}$. For example, for $N\ge68$,


$$
(N-1)!\ge16^{N-16},
$$


so


$$
2^{4N-6}((N-1)!)^2
\ge2^{12N-134}>2^{10N}>5^{4N}.
$$


Thus


$$
\boxed{V^\dagger_{p,N}>0.}
\tag{5.12}
$$



It follows that $\mathcal C_+>0$ at every original pair under consideration. If $\mathcal C_-\ne0$, then it too is positive, and the evaluated integer in (5.9) is positive.

### 5.4 Exact clearing and what is not being normalized

Equation (5.9) proves the all-prime integrality statement


$$
\boxed{
\frac{\mathscr P_{p,N}(\operatorname{Re}Z_p,\operatorname{Im}Z_p)}
     {16g_B^2}
=V\,V^\dagger_{p,N}\,\mathcal C_-\in\mathbb Z.
}
\tag{5.13}
$$


Its least rational denominator is $1$.

This is a pointwise division of the evaluated value. It is not a claim that $g_B^2$ divides every coefficient of $\mathscr P_{p,N}$. No additional content is silently removed, and this value is not substituted for the primitive mixed triple or for the final producer.

---

## 6. Exact classification of norm-factor contact

Let


$$
a_G=v_p(g_B),
\qquad
\mu_p^{\rm ref}=v_p(V^\dagger_{p,N}).
$$


When $\mathcal C_-\ne0$, set


$$
\kappa_p^{\rm cross}=v_p(\mathcal C_-).
$$



From (5.8)–(5.9),


$$
\boxed{
v_p(\mathcal C_+)=2a_G+v_p(V)+\mu_p^{\rm ref},
}
\tag{6.1}
$$




$$
\boxed{
v_p\bigl(\mathscr P_{p,N}(Z_p)\bigr)
=2a_G+v_p(V)+\mu_p^{\rm ref}+\kappa_p^{\rm cross}.
}
\tag{6.2}
$$


Here and below $\mathscr P_{p,N}(Z_p)$ abbreviates evaluation at its real and imaginary parts.

These are exact receiving multiplicities, not lower bounds obtained from a nonzero coefficient.

### 6.1 Residue tests use actual leading data

Under even the first raw source collision, define


$$
\xi_p=\operatorname{Re}\bigl(B_\star(Z_0)I_p\bigr)\pmod p.
$$


All coefficients in this expression use the actual terminal Hermite data, with the actual $\Gamma_p^8$. Since $Z_p\equiv Z_0\pmod p$,


$$
A_\star+D_\star+2\xi_p\equiv0\pmod p.
$$


The reflected factor satisfies


$$
4V^\dagger_{p,N}\equiv-4\xi_p\pmod p.
$$


Therefore


$$
\boxed{\mu_p^{\rm ref}=0\iff \xi_p\ne0\pmod p.}
\tag{6.3}
$$



Similarly, because $\mathcal C_+\equiv0\pmod p$ and $R_p\equiv1$,


$$
\mathcal C_-\equiv-4K_\star(Z_0)\pmod p.
$$


Hence


$$
\boxed{
\kappa_p^{\rm cross}=0
\iff K_\star(Z_0)\ne0\pmod p.
}
\tag{6.4}
$$



These are early, fully evaluated residue tests. They require neither the second nor the third digit of an independently chosen Gaussian quotient.

### 6.2 The unpaid classes $p\equiv3,5\pmod8$

FULL24 gives $a_G=0$ on these classes.

Write


$$
B_\star(Z_0)=b_R+ib_I\pmod p.
$$



For $p\equiv3\pmod8$, $I_p=-1$, so


$$
A_\star+D_\star=2b_R,
\qquad
4V^\dagger_{p,N}\equiv4b_R,
$$


and


$$
\mathcal C_-\equiv(A_\star-D_\star)^2+4b_I^2\pmod p.
\tag{6.5}
$$


Since $-1$ is a nonsquare modulo $p$,


$$
\boxed{
\mathcal C_-\equiv0
\iff
A_\star=D_\star,\quad b_I=0
\pmod p.
}
\tag{6.6}
$$


Thus the cross-factor collision in this class requires two simultaneous real residue conditions.

For $p\equiv5\pmod8$, $I_p=-i$, so


$$
A_\star+D_\star=-2b_I,
\qquad
4V^\dagger_{p,N}\equiv-4b_I,
$$


and


$$
\mathcal C_-\equiv(A_\star-D_\star)^2+4b_R^2\pmod p.
\tag{6.7}
$$


Now $-1$ is a square. If $\iota^2=-1$ in $\mathbb F_p$, then


$$
\boxed{
\mathcal C_-\equiv0
\iff
A_\star-D_\star=\pm2\iota b_R\pmod p.
}
\tag{6.8}
$$


The two signs describe the same norm condition; they do not select a new Gaussian quotient.

At all depths, for $p\equiv3\pmod4$,


$$
\boxed{
\kappa_p^{\rm cross}
=
2\min\!\left(
v_p(A_\star-D_\star R_p),
v_p(2\operatorname{Im}(B_\star\mathsf X_p))
\right),
}
\tag{6.9}
$$


unless both quantities vanish exactly, in which case $\mathcal C_-=0$.
This follows from anisotropy of a sum of two squares modulo such a prime, after factoring out the smaller common power.

For $p\equiv1\pmod4$, the corresponding exact rule is the sum of the valuations of


$$
A_\star-D_\star R_p
\pm2\iota\,\operatorname{Im}(B_\star\mathsf X_p)
$$


in $\mathbb Z_p$, where either lift of $\iota^2=-1$ may be used. Additional split-prime cancellation must therefore be retained.

### 6.3 The paid classes $p\equiv1,7\pmod8$

In these classes $a_G$ may be positive. The same identities remain valid, but the original source is the divided value $V$, not $g_B^2V$.

The residue formulas are:

- $p\equiv1\pmod8$, $I_p=i$:
  

$$
A_\star+D_\star=2b_I,\qquad
  4V^\dagger_{p,N}\equiv4b_I,
$$


  

$$
\mathcal C_-\equiv(A_\star-D_\star)^2+4b_R^2;
$$


- $p\equiv7\pmod8$, $I_p=1$:
  

$$
A_\star+D_\star=-2b_R,\qquad
  4V^\dagger_{p,N}\equiv-4b_R,
$$


  

$$
\mathcal C_-\equiv(A_\star-D_\star)^2+4b_I^2.
$$



If


$$
g_{\rm ref}=\gcd(b_J,b_{J+1}),
$$


then $g_{\rm ref}^2\mid V^\dagger_{p,N}$. Thus its actual valuation is already included in $\mu_p^{\rm ref}$. The adjacent Chebyshev norm identity shows, just as for the original adjacent pair, that an odd prime dividing both reflected imaginary coefficients must have $(2/p)=1$. No reflected Gaussian payment is therefore hidden on $p\equiv3,5\pmod8$.

### 6.4 The regular norm class

Call an original pair **norm-regular** when


$$
\xi_p\ne0,\qquad K_\star(Z_0)\ne0\pmod p.
\tag{6.10}
$$


This is a pointwise definition by actual residue tests, not an existence or mass assertion.

On the unpaid classes $p\equiv3,5\pmod8$, norm-regularity gives


$$
\boxed{
v_p\bigl(\mathscr P_{p,N}(Z_p)\bigr)=v_p(V).
}
\tag{6.11}
$$


The evaluated certificate is then a positive, nonzero integer.

Consequently, under (2.1), at a norm-regular pair,


$$
\boxed{
p^4\mid U,V
\iff
p^4\mid\mathcal F_{p,N}^{\Gamma}
\quad\text{and}\quad
p^4\mid\mathscr P_{p,N}(Z_p).
}
\tag{6.12}
$$


This equivalence uses no Gaussian coordinates chosen independently of the prescribed quotient.

---

## 7. A stronger explicit restriction on the evaluated harmonic quotient

Equation (6.12) becomes useful only if the norm-polynomial value is evaluated, rather than left as a named resultant. We now give that evaluation through the required precision.

This section concerns the norm-regular unpaid class, so $a_G=0$, and assumes the actual third collision.

### 7.1 Fixed-degree coefficient evaluation

Write


$$
\mathscr P_{p,N}(x,y)=\sum_{i+j\le16}c_{ij}x^iy^j.
$$


The coefficients $c_{ij}\in\mathbb Z$ are obtained by the explicit operations (4.1), (4.5)–(4.7), and (5.1). No large-index symbolic elimination remains.

Let


$$
Z_0=x_0+iy_0.
$$


For $a,b\ge0$, define the integer coefficient evaluation


$$
D_{ab}
=
\sum_{\substack{i\ge a,\ j\ge b\\i+j\le16}}
\binom ia\binom jb\,c_{ij}x_0^{i-a}y_0^{j-b}.
\tag{7.1}
$$


This is the divided partial derivative, written as a finite integer sum; no factorial denominator is introduced.

Write the actual harmonic values as


$$
\Lambda_d=u_d+iv_d,\qquad d=0,1,2.
$$


They are the prescribed sums in §3.1, not independent base-$p$ digits.

Define


$$
T_0=D_{00},
$$




$$
T_1=D_{10}u_0+D_{01}v_0,
$$




$$
\begin{aligned}
T_2={}&-D_{10}u_1-D_{01}v_1\\
&+D_{20}u_0^2+D_{11}u_0v_0+D_{02}v_0^2,
\end{aligned}
$$




$$
\begin{aligned}
T_3={}&D_{10}u_2+D_{01}v_2\\
&-2D_{20}u_0u_1-D_{11}(u_0v_1+u_1v_0)-2D_{02}v_0v_1\\
&+D_{30}u_0^3+D_{21}u_0^2v_0
 +D_{12}u_0v_0^2+D_{03}v_0^3.
\end{aligned}
\tag{7.2}
$$



### Proposition 7.1 — Whole evaluated fourth norm residue

At the actual pair,


$$
\boxed{
\mathscr P_{p,N}(Z_p)
\equiv T_0+pT_1+p^2T_2+p^3T_3\pmod{p^4}.
}
\tag{7.3}
$$



#### Proof

Insert


$$
Z_p\equiv Z_0+p\Lambda_0-p^2\Lambda_1+p^3\Lambda_2\pmod{p^4}
$$


into the integer polynomial $\mathscr P_{p,N}$. The binomial expansion about $(x_0,y_0)$, collected through total perturbation degree three, gives exactly (7.2). Terms of perturbation degree at least four are divisible by $p^4$. ∎

Because actual third contact implies $p^3\mid\mathscr P_{p,N}(Z_p)$,


$$
T_0+pT_1+p^2T_2\in p^3\mathbb Z_{(p)}.
$$


Therefore the necessary fourth-contact condition is the following explicit congruence:


$$
\boxed{
\begin{aligned}
D_{10}u_2+D_{01}v_2\equiv{}&
-\frac{T_0+pT_1+p^2T_2}{p^3}\\
&+2D_{20}u_0u_1+D_{11}(u_0v_1+u_1v_0)+2D_{02}v_0v_1\\
&-D_{30}u_0^3-D_{21}u_0^2v_0
-D_{12}u_0v_0^2-D_{03}v_0^3
\pmod p.
\end{aligned}
}
\tag{7.4}
$$



Every term is prescribed by:

- the original $p,N,r$;
- the actual $\Gamma_p$ and its eighth-power coupling;
- the complete upper- and lower-half Hermite products;
- the full positive forcing return;
- the actual three weighted Gaussian harmonic sums.

The whole lower-order carry is present. The quotient in the first line must be formed modulo $p^4$ before division by $p^3$.

### 7.2 Exact necessary and sufficient scope

On the norm-regular unpaid class, under the actual third collision:

- (7.4) is equivalent to $p^4\mid V$;
- (7.4), together with
  

$$
\mathcal F_{p,N}^{\Gamma}/p^3\equiv0\pmod p,
$$


  is equivalent to simultaneous fourth source contact;
- failure of either condition proves $c_p=3$.

Thus this is not merely the unchanged FULL24 residue with a new name. It is a bounded-degree, explicitly evaluated restriction on the actual binomial-harmonic quotient, obtained after eliminating the second Gaussian root by **both** norm equations and identifying the actual companion factors.

No necessary-and-sufficient reformulation can be logically stronger than the original source equations themselves. The added content here is the arithmetic structure: the degree bound, the reflected positive factor, the exact extra contact multiplicities, and the explicit harmonic constraint.

### 7.3 A proved lower-Gaussian-data exclusion class

Suppose additionally


$$
D_{10}\equiv D_{01}\equiv0\pmod p.
\tag{7.5}
$$


Then the left side of (7.4) vanishes, so the third Gaussian harmonic value $\Lambda_2$ drops out entirely.

Accordingly:

> **Corollary 7.2 — Pointwise exclusion using two Gaussian harmonic levels.**  
> Let an original pair satisfy (2.1), $p\equiv3,5\pmod8$, and norm-regularity (6.10). Suppose (7.5) holds. If the right side of (7.4), evaluated using the actual $\Lambda_0,\Lambda_1$ and complete Hermite data, is nonzero modulo $p$, then simultaneous fourth source contact is impossible and $c_p=3$.

This is a quantified actual class specified without the fourth Gaussian harmonic contribution. Its hypotheses are explicit tests in the original objects. The report does not establish that this class is nonempty, infinite, or of positive mass in $\mathcal S_N$.

### 7.4 The regular-gradient restriction

If


$$
(D_{10},D_{01})\not\equiv(0,0)\pmod p,
$$


then (7.4) confines the evaluated pair $(u_2,v_2)\bmod p$ to one affine line.

There is also a precise finite-ring interpretation. If, for example, $D_{10}$ is a unit, then for every


$$
y\equiv y_0\pmod p\quad\text{modulo }p^4
$$


there is exactly one


$$
x\equiv x_0\pmod p\quad\text{modulo }p^4
$$


satisfying


$$
\mathscr P_{p,N}(x,y)\equiv0\pmod{p^4}.
$$


To see this, lift one digit at a time. At each stage the new $x$-digit occurs with the unit coefficient $D_{10}\bmod p$, so it is uniquely determined.

Hence, among the $p^6$ formal residue pairs for


$$
\mathcal L_p\bmod p^3
$$


with the prescribed base $Z_0$, exactly $p^3$ lie on this norm-certificate graph.

This is a classification of possible local residues, **not a count of actual primes or original pairs**. The actual $\mathcal L_p$ is the single binomial-harmonic value (3.4). A unit derivative does not show that this value avoids the graph.

---

## 8. What the classification does and does not decide

### 8.1 No congruence-class contradiction has been proved

The results above distinguish the classes sharply:

- $p\equiv3,5\pmod8$: no $p$-power Gaussian gcd removal is needed;
- $p\equiv3\pmod8$: cross-factor contact is anisotropic and its valuation is even;
- $p\equiv5\pmod8$: the cross norm splits, and cancellation on either split branch must be retained;
- $p\equiv1,7\pmod8$: the actual $g_B^2$-payment remains, with the same split/inert distinction for the cross factor.

These facts do **not** prove a contradiction from the first and second source collisions.

The complete endpoint data do not add an independent third source equation. At a unit $v_1$, the retained exact identity


$$
\mathfrak B_{p,N}
=
\left(E_2-\frac{E_1v_2}{v_1}\right)u_1
-\frac{E_1}{v_1}\mathscr Z_{p,N}
$$


already shows that the endpoint chart reduces to the same source pair. The four prime-base defects must therefore not be counted as four independent source constraints.

### 8.2 Formal compatibility is not actual compatibility

When the gradient in §7.4 is a unit and the first source has fourth contact, norm-compatible local branches remain after imposing the prescribed base values and the complete fixed Hermite data. Both norm roots lift with their prescribed residues.

But the additional requirement


$$
\mathcal L_p=\text{the exact sum in (3.4)}
$$


selects one numerical point. No proof here determines whether that point lies on the fourth-contact graph at every assigned pair.

Accordingly:

- no compatible fourth-contact **original pair** has been exhibited;
- no entire congruence class of original pairs has been excluded;
- formal lifting is not being substituted for the missing numerical theorem.

### 8.3 Exact outstanding follow-on lemma

A concrete next obligation is now:

> **Evaluated norm–harmonic separation lemma — open.**  
> At every original norm-regular pair satisfying (2.1) with $p\equiv3,5\pmod8$, prove that either
> 

$$
> \mathcal F_{p,N}^{\Gamma}/p^3\not\equiv0\pmod p,
>
$$


> or the explicitly evaluated congruence (7.4) fails.

This is not an unevaluated resultant assertion. The polynomial coefficients and all harmonic terms have been specified, and its validity would imply $c_p=3$ on that actual class.

Separate obligations remain to control:

1. reflected-factor contact $\xi_p=0$;
2. cross-factor contact $K_\star(Z_0)=0$;
3. the paid $p\equiv1,7\pmod8$ cases;
4. quantitatively useful membership and coverage inside the literal $\mathcal S_N$.

---

## 9. Division costs, larger targets, and determinant-critical primes

The original target is still


$$
\boxed{\mathsf d=4+B_p+j_p.}
$$



For the original divided source:

- a divided linear Gaussian datum modulo $p^{\mathsf d}$ requires raw precision
  

$$
p^{a_G+\mathsf d};
$$


- a raw quadratic column divided by $g_B^2$ requires
  

$$
\boxed{p^{2a_G+\mathsf d}.}
$$



These costs have not decreased.

If the norm certificate is used and the finite losses
$\mu_p^{\rm ref},\kappa_p^{\rm cross}$ are known, then (6.2) shows that testing $v_p(V)\ge\mathsf d$ by the polynomial certificate requires its raw value modulo


$$
\boxed{
p^{2a_G+\mathsf d+\mu_p^{\rm ref}+\kappa_p^{\rm cross}}.
}
\tag{9.1}
$$


Using $\mathcal C_+$ instead removes the cross-factor loss but still requires


$$
p^{2a_G+\mathsf d+\mu_p^{\rm ref}}.
$$


The norm method can therefore cost **more** precision on exceptional branches. Those extra digits pay multiplication losses; they are not a new fifth-depth research claim.

At larger precision, use the exact product (3.4), the exact Hermite products (3.12), and both full returns. The cubic expansion (3.5) alone is not sufficient.

For determinant-critical primes, retain the established bound


$$
\lambda_p:=\min(v_p(v_1),v_p(v_2))
\le v_p(\Delta)\le j_p.
$$


If $c_p\ge\lambda_p$, form


$$
\mathbf v'=\mathbf v/p^{\lambda_p},
\qquad
\mathbf d'=\mathbf d/p^{\lambda_p}
$$


only after obtaining the unnormalized vectors to the required precision. One component of $\mathbf v'$ is a unit, and


$$
c_p=\lambda_p+
\min\left(
v_p(d'_i/v'_i-\rho_p),
v_p\det(\mathbf v',\mathbf d')
\right).
$$


There is no inversion of $\Delta$.

The actual $H_p,B_p$, including the endpoint valuations at $N-1,N$, are still required. A computation stopped at $p^4$ cannot determine a valuation continuing beyond that modulus.

No fixed-$N$ interval aggregate is proposed here. The new reflected and norm values depend on $p$; no mass theorem follows from their congruence-class descriptions.

---

## 10. Preservation of the original returns and normalizations

The new certificate does not replace any original normalization or forcing identity.

### 10.1 Mixed chart and least simultaneous clearer

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


Retain


$$
\mathbf R=\mathbf C-\mathsf M_c\mathbf t_s,
\qquad
\mathbf E=\mathsf M_c(\mathbf f_\ell+\mathbf f_s),
$$




$$
\mathfrak A_{p,N}=\det(\mathbf R,\mathbf u),\qquad
\mathfrak B_{p,N}=\det(\mathbf u,\mathbf E).
$$


The safe chart is still


$$
\zeta_{p,N}=
\begin{cases}
\mathfrak A_{p,N},&p\nmid R_1,\\
\mathfrak B_{p,N},&p\mid R_1,
\end{cases}
$$


with


$$
\min(v_p(R_1),v_p(E_1))=0,
$$




$$
c_p-2=
\min\bigl(v_p(16U/p^2),v_p(\zeta_{p,N}/p^2)\bigr).
$$



The four actual defects are


$$
\sigma_0^+=\frac{\Theta_p-\chi Q_a^{\rm H}}p,\quad
\sigma_1^+=\frac{\Theta_{p-1}+1+\chi Q_k^{\rm H}}p,
$$




$$
\sigma_0^-=\frac{\Phi_p-\chi P_a^{\rm H}}p,\quad
\sigma_1^-=\frac{\Phi_{p-1}-1+\chi P_k^{\rm H}}p.
$$


With


$$
\Lambda_\sigma=
P_k^{\rm H}\sigma_0^++P_a^{\rm H}\sigma_1^+
-Q_k^{\rm H}\sigma_0^--Q_a^{\rm H}\sigma_1^-,
$$




$$
\Xi_\sigma=\sigma_1^+\sigma_0^--\sigma_0^+\sigma_1^-,
$$


and


$$
\mathfrak f_{s;p}
=-\sum_{t=1}^{s-1}(-1)^t
(\Theta_t\Phi_{p+t}+\Phi_t\Theta_{p+t}),
$$


the complete mixed denominator and endpoint difference remain


$$
\mathfrak D_{s;p}
=2(-1)^a\chi^2+p\chi\Lambda_\sigma
+p^2\Xi_\sigma+4p\mathfrak f_{s;p},
$$




$$
\mathfrak B_{p,N}=R_1E_2-R_2E_1-\Delta\mathfrak D_{s;p}.
$$


Thus


$$
d_{\rm mix}
=\gcd(\mathfrak D_{s;p},\mathfrak A_{p,N},\mathfrak B_{p,N}),
$$




$$
(A_{\rm mix},B_{\rm mix},D_{\rm mix})
=\frac1{d_{\rm mix}}
(\mathfrak A_{p,N},\mathfrak B_{p,N},\mathfrak D_{s;p})
$$


is unchanged, including its all-prime least simultaneous clearing property.

### 10.2 Source and endpoint returns

The source balance is


$$
(\nu\mathscr A-16\tau\Pi)\Theta_\ell
+(\nu\mathscr B-16\tau\Omega)\Theta_{\ell-1}
=\nu\mathscr C_U-16\tau C^{\rm s}.
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
\boxed{\varrho_{j-1}=\varrho_{j+1}+4j\varrho_j-2\Delta.}
$$



After the actual arc clearing, let


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


The whole relation


$$
z_\ell^{\rm ret}w_{\ell-1}
-z_{\ell-1}^{\rm ret}w_\ell
=-16\Delta(UX+VY)
$$


is retained without dividing by $\Delta$.

### 10.3 Canonical endpoint payment

For exactly $0\le b\le N$,


$$
\mathcal R_{b;N}=d_KP_b^{\rm H}U+Q_b^{\rm H}y_K,
$$




$$
\Psi_j^{(b)}=Q_b^{\rm H}\Phi_j-P_b^{\rm H}\Theta_j.
$$


Its forcing is


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


The retained endpoint payment remains


$$
\mathcal R_{N-1;N}<0<\mathcal R_{N;N},
$$




$$
\frac{c(r^\circ)^2}{\kappa_N^{\rm prod}}
\mid\mathcal R_{N-1;N}\mathcal R_{N;N},
\qquad
v_p(\kappa_N^{\rm prod})=[c_p-H_p]_+.
$$


No credit is reassigned to $a,k$ or to the reflected Gaussian indices.

The older interface clearers


$$
Q_{\rm loc}(n)=\prod_{b=0}^{12}(n-b),
\qquad
\mathcal L_n=\operatorname{lcm}(1,\ldots,n)
$$


remain separate, as does


$$
\frac{2\mathcal L_n}{j^2-1}
=\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}.
$$


Likewise, FULL23’s proved termwise $\chi$-division and sufficient local clearer
$48\operatorname{lcm}(1,\ldots,p-1)^4$ concern its particular cubic expression only. They are not divisions of the original producer or of the new reflected source.

---

## 11. Both arcs, the all-prime final gcd, and the whole error

The two arcs remain


$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,
\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


Their quotient polynomial degrees are at most $2N-2$.

The already completed $K$-arc reduction is reused:


$$
R_K=\frac{A_K(\ell^2)}{30L(\ell^2)}=\frac{a_K}{d_K},
$$




$$
A_K(x)=13x^3-455x^2+3502x-5850,
$$




$$
g_{\rm arc}
=90\,5^{\varepsilon_5}19^{\varepsilon_{19}}31^{\varepsilon_{31}},
$$




$$
\varepsilon_5=\mathbf1_{u\equiv1\pmod5},\quad
\varepsilon_{19}=\mathbf1_{u\equiv3\pmod9},\quad
\varepsilon_{31}=\mathbf1_{u\equiv5,7\pmod{15}},
$$




$$
a_K=A_K(\ell^2)/g_{\rm arc},\qquad
d_K=30L(\ell^2)/g_{\rm arc}.
$$


Thus


$$
y_K=d_KE_K-a_K,\quad
\gamma=\gcd(\tau,y_K),\quad
b^\circ=\gcd(\gamma,a_K),\quad
r^\circ=\gamma/b^\circ
$$


remain the actual quantities.

The square-arc return has zero seeds at $0,1$:


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
\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
-2\alpha\beta\xi_{n-1}}2,
$$


with no step above $n-1$.

After reducing both arcs completely, retain


$$
\boxed{D=\operatorname{lcm}(\operatorname{den}R_F,\operatorname{den}R_K),}
$$




$$
X=D(E_F-R_F),\qquad Y=D(E_K-R_K).
$$


Independently reduce


$$
\tau R_F+\nu R_K=\frac b\lambda,
\qquad \gcd(b,\lambda)=1,\quad\lambda>0.
$$


Then


$$
E=\tau E_F+\nu E_K,\qquad A=\lambda E-b,
$$




$$
\boxed{G=\gcd(M,A)\quad\text{over all primes},}
$$




$$
\boxed{p_N=A/G,\qquad q_N=\lambda M/G.}
\tag{11.1}
$$


Because $\gcd(\lambda,A)=1$, this remains the actual primitive pair.

The original polynomial and complete error are


$$
P_N(t)=\frac{F(t)^2+(V/U)K(t)}{\delta^2}
=\frac{W_{\rm prim}(t)}M,
$$




$$
\boxed{
\epsilon_N=
\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0.
}
\tag{11.2}
$$


The source balance gives $\eta(W_{\rm prim})=M$, and finite integration by parts with both arcs gives


$$
\epsilon_N=e+\pi-\frac{A}{\lambda M}.
$$


Hence, at the same original indices,


$$
\boxed{q_N(e+\pi)-p_N=q_N\epsilon_N>0.}
\tag{11.3}
$$



The retained whole-error enclosure is


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


Thus


$$
\boxed{
q_NJ_N=\frac{\lambda_N}{G_N}
\bigl(\tau_NJ_F+\nu_NJ_K\bigr).
}
\tag{11.4}
$$


Both positive summands remain.

A proof of decay of (11.4) along an infinite subsequence of these same original indices would prove irrationality. No such decay estimate is obtained here.

---

## 12. Proof status and bounded arithmetic

### 12.1 Status ledger

| Statement | Status |
|---|---|
| New normalization-rigidity corollary | **Different audit passed**, with $D'>0$ retained |
| Primitive mixed-ratio factorial obstruction | Reused pointwise; not reproved or transferred |
| FULL23–24 Gaussian and Hermite input identities | Reused at stated scope; no completed different review claimed here |
| Explicit reduction (4.7)–(4.8) of the complete source | **New proved identity** |
| Integer norm polynomial of degree at most $16$ | **New proved construction** |
| Identification of the real companion with actual reflected Gaussian indices | **New proved identity** |
| Positivity of $V^\dagger_{p,N}$ | **New proved statement** |
| Actual paid value certificate (5.9), (5.13) | **New proved all-prime integrality and factorization** |
| Split/inert cross-contact classification and exact multiplicities | **New proved restrictions** |
| Evaluated harmonic condition (7.4) | **New proved necessary/sufficient test on the stated regular class** |
| Lower-Gaussian-data exclusion Corollary 7.2 | **Proved conditional, pointwise exclusion** |
| Nonempty or infinite occurrence of the exclusion class | Not proved |
| Universal fourth-contact separation | Open |
| Absolute paid-depth bound or significant fixed-$N$ coverage | Not proved |
| Original primitive denominator and nonzero whole error | Retained unchanged |
| Rationality or irrationality of $e+\pi$ | Unresolved |

### 12.2 Bounded exact arithmetic specification

No original-sized arithmetic calculation is needed for the proofs above, and none is requested.

An optional new finite checksum may be used solely to inspect the source-to-norm algebra:

- **Inputs:**  
  $w=-1+2i$, $z=-1+i$; the finite recurrence for
  $\mathsf U_{-1},\ldots,\mathsf U_6$; hence
  

$$
d_-=D_5,\ e_-=zE_5,\ d_+=D_6,\ e_+=zE_6;
$$


  three indeterminates $Q_{00},Q_{01},Q_{11}$; and polynomial variables
  $x,y,X,\bar X$.

- **Relations for reduction:**
  

$$
i^2=-1,\qquad
  X^2=i+iz(x+iy)^2,\qquad
  \bar X^2=-i-i\bar z(x-iy)^2.
$$



- **Expected verifiable outputs:**
  1. the remainder of (4.4) minus (4.8) is the zero polynomial;
  2. the four-sign product of (4.8) equals (5.1);
  3. its total degree in $x,y$ is at most $16$;
  4. all coefficients of that product are ordinary integers.

- **Scope:**  
  This checks the finite $h=6$ specialization of the displayed algebra. It certifies neither membership in $\mathcal S_N$ nor numerical source separation at an original pair. The general proofs above do not depend on this checksum.

---

## Final conclusion

The audited normalization-rigidity corollary is valid: with positive denominators, every integer realization of the same two mixed ratios is a positive integer multiple of their actual primitive triple. Its height obstruction remains pointwise and confined to those ratios.

The main new result is the actual norm–reflection identity


$$
\boxed{
\mathscr P_{p,N}(Z_p)
=
16g_B^2V\,V^\dagger_{p,N}\,
\left[
(A_\star-D_\star R_p)^2
+4\operatorname{Im}(B_\star\mathsf X_p)^2
\right],
}
$$


where:

- $\mathscr P_{p,N}\in\mathbb Z[x,y]$ has degree at most $16$;
- $Z_p$ is the prescribed binomial-harmonic Lucas value;
- both real and imaginary norm equations are imposed;
- the same prescribed $\Gamma_p$ supplies the Hermite scalar through $\Gamma_p^8$;
- $V^\dagger_{p,N}>0$ is an actual reflected Gaussian source at indices $p-N,p-N+1$, evaluated against the unchanged physical moment index $N$.

This gives exact paid contact multiplicities and a new evaluated harmonic restriction, including the lower-Gaussian-data exclusion of Corollary 7.2. It does not justify an absolute depth bound from a nonzero coefficient, a unit derivative, or a formal local solution.

The immediate mathematical bottleneck is numerical: at the same original pairs, one must prove that the actual first-source value (3.15) and the explicit norm-harmonic condition (7.4) cannot both have fourth contact, and then control the reflected, cross-factor, and Gaussian-division exceptional branches with their full costs. No infinite eligible family or fixed-$N$ mass estimate has been established.

Finally, the all-prime $G_N$, actual primitive $q_N$, both least arc clearers, and the positive whole error remain unchanged. The required same-index decay


$$
\frac{\lambda_N}{G_N}
\bigl(\tau_NJ_F+\nu_NJ_K\bigr)\longrightarrow0
$$


is still unproved. Thus the new norm-compatible restrictions advance the original source-contact analysis, but do not decide whether $e+\pi$ is rational or irrational.
