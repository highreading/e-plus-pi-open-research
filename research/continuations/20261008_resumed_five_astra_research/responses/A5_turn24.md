> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Generic prime-half Gaussian arithmetic in the original source columns

## 1. Different proof audit of the sharper determinant bound

This audit concerns the new bound in A3turn21 §19.1 and the prerequisites needed for it. It does **not** reopen the already reviewed FULL18/19 source theorem, and it does not constitute the pending different review of FULL23.

Throughout this report the original indices are


$$
N=9^{18+32u}=3^{36+64u},\qquad u\ge0,
$$


and


$$
n=2N,\qquad m=N-3,\qquad \ell=n-6.
$$



The outcome of this first audit is **PASS**. In fact, a slightly stronger constant follows from the actual transported quadratic forms:


$$
\boxed{
0<|\Delta|
<
1{,}696{,}500{,}000\,n^{14}\frac{5^{2N}}{g_B^2}
<
3\cdot10^9n^{14}\frac{5^{2N}}{g_B^2}.
}
\tag{1.1}
$$



The argument below keeps the older $J_N^{\rm aff}$ bill separate.

### 1.1 Legality of the actual Gaussian division

Write


$$
C_j(t)=T_j(2t-1),\qquad C_j(i)=a_j+ib_j,
$$


with


$$
C_0=1,\qquad C_1=2t-1,\qquad
C_{j+1}=(4t-2)C_j-C_{j-1}.
$$


At $t=i$, the recurrence coefficient is $-2+4i$.

Define


$$
\omega_j=\operatorname{Im}\bigl(C_j(i)\overline{C_{j-1}(i)}\bigr).
$$


The recurrence gives


$$
\omega_j=4|C_{j-1}(i)|^2+\omega_{j-1},\qquad \omega_1=2.
$$


Thus $\omega_j>0$. In particular,


$$
a_Nb_{N-1}-a_{N-1}b_N=-\omega_N\ne0.
$$


Consequently $b_{N-1},b_N$ cannot both vanish, and the actual quantities


$$
g_B=\gcd(b_{N-1},b_N)>0,
$$




$$
\alpha=\frac{b_{N-1}}{g_B},\qquad
\beta=\frac{b_N}{g_B},\qquad
\delta=\frac{a_Nb_{N-1}-a_{N-1}b_N}{g_B}
$$


are integers, with


$$
\gcd(\alpha,\beta)=1,\qquad \delta\ne0.
$$


This proves real nonvanishing; it does not assert that $\delta$ is a unit at any particular prime.

Since


$$
2\sqrt5+\frac15<5,
$$


the Gaussian recurrence, starting from $1$ and $-1+2i$, gives


$$
|C_j(i)|\le5^j.
$$


Therefore


$$
H_2:=\alpha^2+\beta^2
\le
\frac{5^{2N-2}+5^{2N}}{g_B^2}
=
\frac{26}{25}\frac{5^{2N}}{g_B^2}.
\tag{1.2}
$$



### 1.2 The finite six-step transport used in the audit

Set


$$
x_j=4(\ell+j),\qquad 0\le j\le5,
$$


and define


$$
a_0^*=1,\quad a_1^*=x_0,\qquad
b_0^*=0,\quad b_1^*=1,
$$




$$
a_{j+1}^*=x_ja_j^*+a_{j-1}^*,\qquad
b_{j+1}^*=x_jb_j^*+b_{j-1}^*.
$$


These are precisely the coefficients of the original transport from $\ell$ to $n=\ell+6$. Its last recurrence step is $\ell+5=n-1$.

The terminal Gaussian row is


$$
P=n\alpha^2+(n-2)\beta^2,
$$




$$
Q=4(n-1)(n-2)\beta^2-2(n-1)\alpha\beta.
$$


The exact transported coefficients are


$$
\Pi=Pa_6^*-Qa_5^*,\qquad
\Omega=-Pb_6^*+Qb_5^*.
$$


Using the last recurrence step before estimating yields


$$
\begin{aligned}
\Pi={}&
na_6^*\alpha^2
+2(n-1)a_5^*\alpha\beta
+(n-2)a_4^*\beta^2,\\
\Omega={}&
-nb_6^*\alpha^2
-2(n-1)b_5^*\alpha\beta
-(n-2)b_4^*\beta^2.
\end{aligned}
\tag{1.3}
$$


This cancellation is useful: it avoids charging the full $Q$-bound at sixth transport depth.

For $0\le j\le6$,


$$
|a_j^*|,\ |b_j^*|\le(5n)^j.
\tag{1.4}
$$


Indeed, $x_j<4n$, and the induction step follows from


$$
4n(5n)^j+(5n)^{j-1}<(5n)^{j+1}.
$$



By $2|\alpha\beta|\le H_2$, (1.3)–(1.4) give


$$
\begin{aligned}
|\Pi|,\ |\Omega|
&\le
\max\!\bigl(n(5n)^6,(n-2)(5n)^4\bigr)H_2
+(n-1)(5n)^5H_2\\
&\le
\bigl(15625n^7+3125n^6\bigr)H_2\\
&\le18750n^7H_2.
\end{aligned}
\tag{1.5}
$$



This is a different estimate from the $Pa_6^*-Qa_5^*$ triangle bound used in the new source claim.

### 1.3 The coefficient bounds and strict nonvanishing of $\Delta$

At $x=\ell^2$, put


$$
\begin{aligned}
\mathcal P&=-8x^3-1116x^2-8150x+151,\\
\mathcal Q&=76x^2+2408x+5637,
\end{aligned}
$$


and


$$
\mathscr A=2\ell((2\ell+1)\mathcal Q-\mathcal P),
\qquad
\mathscr B=-2\ell\mathcal Q.
$$


The coefficient sums give, directly,


$$
|\mathscr A|<70000n^7,\qquad
|\mathscr B|<17000n^5.
\tag{1.6}
$$


For example,


$$
\frac{\mathscr A}{2\ell}
=
8\ell^6+152\ell^5+1192\ell^4+4816\ell^3
+10558\ell^2+11274\ell+5486,
$$


whose coefficient sum is $33486$, while the coefficient sum of $2\ell\mathcal Q$ is $16242$.

The determinant is the actual integer


$$
\Delta=\mathscr A\Omega-\mathscr B\Pi.
$$



For completeness, the nonzero part of the conditioning claim can be checked without any modular inversion. Put


$$
b_K=-\mathscr B>0,\qquad R_j=\mathscr A b_j^*-b_Ka_j^*.
$$


Then


$$
R_{j+1}=x_jR_j+R_{j-1},\qquad R_0=-b_K,
$$


and


$$
R_1=2\ell S(\ell),
$$


where


$$
S(\ell)=
8\ell^6-152\ell^5+1192\ell^4-4816\ell^3
+10558\ell^2-11274\ell+5486.
$$


On the original domain $\ell\ge20$,


$$
S(\ell)>8\ell^5>\mathcal Q(\ell^2).
$$


Hence $R_1>b_K$, and $R_2,R_3,\ldots,R_6$ are positive and increasing.

Equation (1.3) now gives


$$
-\Delta
=nR_6\alpha^2+2(n-1)R_5\alpha\beta+(n-2)R_4\beta^2.
$$


If


$$
t=\frac{R_3}{R_4}\in(0,1),
\qquad
x=\frac{R_5}{R_4}=4(n-2)+t,
$$


the determinant of this quadratic form, divided by $R_4^2$, is


$$
\begin{aligned}
&n(n-2)\bigl(4(n-1)x+1\bigr)-(n-1)^2x^2\\
&=
16(n-1)(n-2)^2+n(n-2)
-4(n-1)(n-2)^2t-(n-1)^2t^2\\
&>
12(n-1)(n-2)^2-1>0.
\end{aligned}
$$


The first diagonal coefficient is positive. Thus the form is positive definite, and $(\alpha,\beta)\ne(0,0)$ proves


$$
\Delta<0.
\tag{1.7}
$$



Finally, (1.2), (1.5), and (1.6) imply


$$
\begin{aligned}
|\Delta|
&<(70000n^7+17000n^5)\,18750n^7H_2\\
&\le1{,}631{,}250{,}000\,n^{14}H_2\\
&\le1{,}696{,}500{,}000\,n^{14}\frac{5^{2N}}{g_B^2}.
\end{aligned}
$$


This proves (1.1), and in particular repairs no defect in the requested $3\cdot10^9$ bound: that bound is valid.

### 1.4 What this audit does not pay

The complete transported source constant is


$$
\begin{aligned}
C^{\rm s}={}&
(1-nf_6)\alpha^2
+2(n-1)f_5\alpha\beta\\
&+(1-(n-2)f_4)\beta^2-\delta^2.
\end{aligned}
$$


The remainders


$$
\mathscr I_1=\Pi\mathscr C_U-\mathscr A C^{\rm s},
\qquad
\mathscr I_2=\Omega\mathscr C_U-\mathscr B C^{\rm s}
$$


therefore contain respectively $+\mathscr A\delta^2$ and $+\mathscr B\delta^2$.

Accordingly, the retained bill is still


$$
\boxed{
J_N^{\rm aff}
=\gcd(\mathscr I_1,\mathscr I_2)
<
10^{10}n^{15}\frac{5^{4N}}{g_B^2}.
}
\tag{1.8}
$$


The $H_2$-bound for $\Delta$ does not prove this stronger exponential scale for $J_N^{\rm aff}$.

Both bills are after the actual division:


$$
\Delta_{\rm raw}=g_B^2\Delta,\qquad
\mathscr I_{j,\rm raw}=g_B^2\mathscr I_j.
$$


The sharpened consequence that may legitimately be booked is


$$
\boxed{
\log|\Delta|
<
2N\log5+14\log(2N)+\log(3\cdot10^9)-2\log g_B.
}
\tag{1.9}
$$


It is a conditioning-loss bill, not a new bound for source contact or for the final gcd.

---

## 2. Original objects and the exact branch under study

For an integer polynomial $H$, retain


$$
\eta(H)=\sum_j j![z^j]H(1-z),
\qquad
E(H)=\sum_j(-1)^j j![t^j]H(t).
$$


Set


$$
F=\alpha C_N-\beta C_{N-1},\qquad F(\pm i)=\delta,
$$




$$
\mathcal H=t(1-t)(1+t^2)^2,\qquad K=\mathcal H C_m^2,
$$




$$
U=-\eta(K),\qquad V=\eta(F^2)-\delta^2,\qquad c=\gcd(U,V).
$$


The established original-domain normalization is unchanged:


$$
\operatorname{cont}(W_{\rm raw})=g_B^2c,
$$




$$
\tau=U/c,\qquad \nu=V/c,\qquad
W_{\rm prim}=\tau F^2+\nu K,\qquad M=\tau\delta^2,
$$


with $U,V,M>0$.

### 2.1 The four complete finite columns

The states exist only in the original finite system:


$$
\Theta_0=\Phi_0=0,\qquad \Theta_1=\Phi_1=1,
$$


and, for exactly $1\le j\le n-1$,


$$
\Theta_{j+1}+4j\Theta_j-\Theta_{j-1}=2,
$$




$$
\Phi_{j+1}+4j\Phi_j-\Phi_{j-1}=2(-1)^j.
\tag{2.1}
$$


Thus the affine forcing coordinates are $1$ and $(-1)^j$, respectively.

In addition to $\mathcal P,\mathcal Q$, define


$$
\mathcal F=4x^2+492x+5463,\qquad
\mathcal G=4x^2+556x-3325,
\qquad x=\ell^2,
$$




$$
\mathscr C_U=\mathcal F-\mathcal P+2\ell\mathcal Q,
\qquad
\mathscr C_E=\mathcal G+\mathcal P-2(\ell+1)\mathcal Q.
$$


Then


$$
16U=\mathscr C_U-\mathscr A\Theta_\ell-\mathscr B\Theta_{\ell-1},
$$




$$
16E_K=\mathscr C_E+\mathscr A\Phi_\ell+\mathscr B\Phi_{\ell-1}.
\tag{2.2}
$$


At the physical terminal,


$$
V=C_V-P\Theta_n-Q\Theta_{n-1},
$$




$$
E_F=C_F^E-P\Phi_n-Q\Phi_{n-1},
\tag{2.3}
$$


where


$$
\boxed{C_V=\alpha^2+(2n-3)\beta^2-\delta^2,}
$$




$$
\boxed{C_F^E=\alpha^2+(5-2n)\beta^2+4\alpha\beta.}
\tag{2.4}
$$



For the six-step transfer


$$
T_j=\begin{pmatrix}-4j&1\\1&0\end{pmatrix},
\qquad T=T_{\ell+5}\cdots T_\ell,
$$


use the full returns


$$
f_0=g_0=0,
$$




$$
f_{j+1}=T_{\ell+j}f_j+\binom20,
\qquad
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
\tag{2.5}
$$


These are the complete source and endpoint constants; they are not interchangeable.

### 2.2 Credit and membership are not weakened

Let


$$
L(x)=(x-1)(x-9)(x-25),
$$




$$
A_K(x)=13x^3-455x^2+3502x-5850.
$$


The already reduced $K$-arc is


$$
R_K=\frac{A_K(\ell^2)}{30L(\ell^2)}=\frac{a_K}{d_K},
$$


where


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


This closed calculation is reused, not repeated.

Put


$$
y_K=d_KE_K-a_K,\qquad
\gamma=\gcd(\tau,y_K),
$$




$$
b^\circ=\gcd(\gamma,a_K),\qquad r^\circ=\gamma/b^\circ.
$$


The Hermite sequences have their original range $0\le b\le N$:


$$
P_0^{\rm H}=Q_0^{\rm H}=1,\quad
P_1^{\rm H}=3,\quad Q_1^{\rm H}=1,
$$




$$
Z_{b+1}=(4b+2)Z_b+Z_{b-1},\qquad 1\le b\le N-1.
$$


For every prime,


$$
c_p=\min(v_p(U),v_p(V)),\qquad t_p=v_p(U)-c_p,
$$




$$
z_p=v_p(y_K),\qquad b_p=v_p(b^\circ),\qquad
h_p=v_p(Q_{N-1}^{\rm H}Q_N^{\rm H}),
$$


and the complete credit is


$$
\boxed{H_p=h_p+2b_p+2(z_p-t_p)_+.}
\tag{2.6}
$$



The unchanged branch is


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
\tag{2.7}
$$


The original block condition is retained as a condition on the original finite block; it is not replaced by necessary source congruences.

For $p\in\mathcal S_N$, write


$$
r=n-p,\qquad s=r-6,\qquad
a=\frac{p-1}{2},\qquad k=a+1,\qquad \chi=2k!.
$$


The retained boundary result is


$$
\boxed{
13\le r<N,\qquad s\ge7,\qquad r,s\text{ odd},\qquad k\le N-6.
}
\tag{2.8}
$$


Also $p^2\mid U,V$ and $p\nmid d_K$. Set


$$
B_p=(H_p-2)_+,\qquad
e_p=[c_p-2-B_p]_+,\qquad j_p=v_p(J_N^{\rm aff}).
$$



The primary case remains


$$
p\in\mathcal S_N,\qquad B_p=j_p=0,\qquad p^3\mid U,V.
\tag{2.9}
$$



---

## 3. A source-specific Gaussian reduction on the generic branch

The next results are new derivations for the actual Gaussian data. They use classical Chebyshev identities, binomial Frobenius, and unit-root lifting. No general Lucas nonvanishing theorem is being imported.

The main point is that the two adjacent Gaussian values are not free residues. They arise from one actual Gaussian Lucas quotient, an explicitly prescribed prime-dependent power, and a norm identity.

### 3.1 A half-angle algebra adapted to $C_j(i)$

Put


$$
w=-1+2i,\qquad z=-1+i.
$$


Work first in the algebra obtained by adjoining $x,y$ with


$$
x^2=i,\qquad y^2=z.
$$


Let


$$
\eta=x+y.
$$


Because $i-z=1$,


$$
\eta^{-1}=x-y.
$$


Moreover,


$$
\eta^2=w+2xy,\qquad (2xy)^2=w^2-1.
$$


Hence the usual Chebyshev formula gives the exact identity


$$
C_j(i)=T_j(w)=\frac{\eta^{2j}+\eta^{-2j}}2.
\tag{3.1}
$$



For $h\ge0$, let $\mathsf U_h(w)$ be the second-kind Chebyshev polynomial, with


$$
\mathsf U_{-1}=0,\qquad \mathsf U_0=1,\qquad
\mathsf U_{h+1}=2w\mathsf U_h-\mathsf U_{h-1}.
$$


If desired, its coefficients are explicitly


$$
\mathsf U_h(w)
=
\sum_{v=0}^{\lfloor h/2\rfloor}
(-1)^v\binom{h-v}{v}(2w)^{h-2v}.
$$


Define


$$
D_h=\mathsf U_h-\mathsf U_{h-1},\qquad
E_h=\mathsf U_h+\mathsf U_{h-1}.
\tag{3.2}
$$


The half-angle identities are


$$
\frac{\eta^{2h+1}+\eta^{-(2h+1)}}2=xD_h,
$$




$$
\frac{\eta^{2h+1}-\eta^{-(2h+1)}}2=yE_h.
\tag{3.3}
$$


They follow either from the Laurent formulas or by checking $h=0,1$ and the common recurrence with coefficient $2w$.

### 3.2 The actual prime-base Gaussian pair

For an odd prime $p$, define the Gaussian integers


$$
\mathsf X_p
=
\sum_{\substack{0\le j\le p-1\\j\ {\rm even}}}
\binom pj\,i^{(p+1-j)/2}z^{j/2},
\tag{3.4}
$$




$$
\mathsf Y_p
=
\sum_{\substack{1\le j\le p\\j\ {\rm odd}}}
\binom pj\,i^{(p-j)/2}z^{(j+1)/2}.
\tag{3.5}
$$


These are not freely selected quotient variables. Expanding $(x\pm y)^p$ shows exactly that


$$
\mathsf X_p=\frac{x}{2}(\eta^p+\eta^{-p}),
\qquad
\mathsf Y_p=\frac{y}{2}(\eta^p-\eta^{-p}).
\tag{3.6}
$$



Now use the actual relation


$$
2N=p+r,\qquad r=2h+1,\qquad h=\frac{r-1}{2}.
$$


Equations (3.1), (3.3), and (3.6) give


$$
\boxed{
C_N(i)=D_h\mathsf X_p+E_h\mathsf Y_p,
}
$$




$$
\boxed{
C_{N-1}(i)=D_{h-1}\mathsf X_p+E_{h-1}\mathsf Y_p.
}
\tag{3.7}
$$


Here $h\ge6$. This is the generic $r$-dependent reduction, not the $r=1$ arc specialization.

The adjacent transformation is nondegenerate at every odd prime:


$$
D_{h-1}E_h-D_hE_{h-1}=2.
\tag{3.8}
$$


Indeed,


$$
D_{h-1}E_h-D_hE_{h-1}
=
2(\mathsf U_{h-1}^2-\mathsf U_h\mathsf U_{h-2})=2.
$$


Thus no additional $r$-dependent denominator is hidden in (3.7).

### 3.3 The two prime-base quantities satisfy an exact norm relation

From (3.6),


$$
\boxed{
\frac{\mathsf X_p^2}{i}-\frac{\mathsf Y_p^2}{z}=1,
\qquad\text{equivalently}\qquad
z\mathsf X_p^2-i\mathsf Y_p^2=iz.
}
\tag{3.9}
$$


This removes the possibility of treating $\mathsf X_p,\mathsf Y_p$, or their higher digits, as independent.

Put


$$
I_p=i^{(p+1)/2},\qquad
\Gamma_p=z^{(p+1)/2}.
\tag{3.10}
$$


Since $p\mid\binom pj$ for $1\le j\le p-1$,


$$
\mathsf X_p\equiv I_p\pmod p,\qquad
\mathsf Y_p\equiv\Gamma_p\pmod p.
\tag{3.11}
$$


Both $I_p$ and $\Gamma_p$ are units in $\mathbb Z_{(p)}[i]$: $i$ is a unit and $z\bar z=2$.

There is also a direct, exact link to FULL23’s common Fermat scalar:


$$
z^8=16,
$$


so


$$
\boxed{
\Gamma_p^8=16\,4^{p-1},
\qquad
\rho_p=\frac{\Gamma_p^8}{16(p+1)}.
}
\tag{3.12}
$$


Thus the Fermat factor appearing in all four original prime-base states is already tied to the leading term of the actual Gaussian prime-half arithmetic. It is not independent of that arithmetic.

### 3.4 One actual Gaussian Lucas quotient, evaluated through fourth precision

Define the actual Gaussian integer


$$
\mathscr L_p=\frac{\mathsf Y_p-\Gamma_p}{p}.
$$


Its complete evaluation is


$$
\boxed{
\mathscr L_p
=
\sum_{\substack{1\le j\le p-2\\j\ {\rm odd}}}
\frac{i^{(p-j)/2}z^{(j+1)/2}}{j}
\prod_{t=1}^{j-1}\left(1-\frac pt\right).
}
\tag{3.13}
$$


To prove this, use


$$
\frac1p\binom pj
=
\frac{(-1)^{j-1}}j
\prod_{t=1}^{j-1}\left(1-\frac pt\right).
$$


For odd $j$, the sign is $+1$. Every denominator in (3.13) is below $p$, hence a $p$-adic unit. The quotient is nevertheless an ordinary Gaussian integer because its original binomial expression is one.

For the fourth-precision specialization, write


$$
H_{j-1}=\sum_{t=1}^{j-1}\frac1t,\qquad
H_{j-1}^{(2)}=\sum_{t=1}^{j-1}\frac1{t^2},
$$


and define the three evaluated Gaussian sums


$$
L_0=
\sum_{\substack{1\le j\le p-2\\j\ {\rm odd}}}
\frac{i^{(p-j)/2}z^{(j+1)/2}}j,
$$




$$
L_1=
\sum_{\substack{1\le j\le p-2\\j\ {\rm odd}}}
\frac{i^{(p-j)/2}z^{(j+1)/2}}j\,H_{j-1},
$$




$$
L_2=
\frac12
\sum_{\substack{1\le j\le p-2\\j\ {\rm odd}}}
\frac{i^{(p-j)/2}z^{(j+1)/2}}j
\bigl(H_{j-1}^2-H_{j-1}^{(2)}\bigr).
$$


Expansion of the product in (3.13) proves


$$
\mathscr L_p\equiv L_0-pL_1+p^2L_2\pmod{p^3},
$$


and therefore


$$
\boxed{
\mathsf Y_p\equiv
\Gamma_p+pL_0-p^2L_1+p^3L_2\pmod{p^4}.
}
\tag{3.14}
$$



The norm identity determines the other prime-base value from this one. Put


$$
W_p=
\frac{i+(i/z)\mathsf Y_p^2-I_p^2}{I_p^2}.
\tag{3.15}
$$


The congruence $W_p\in p\mathbb Z_{(p)}[i]$ follows from (3.11), or directly from


$$
i(1+z^p)\equiv i(1+z)^p=i^{p+1}=I_p^2\pmod p.
$$


Equation (3.9) gives


$$
\left(\frac{\mathsf X_p}{I_p}\right)^2=1+W_p,
\qquad
\frac{\mathsf X_p}{I_p}\equiv1\pmod p.
$$


Since $2$ is a unit,


$$
\boxed{
\mathsf X_p
\equiv
I_p\left(1+\frac{W_p}{2}-\frac{W_p^2}{8}
+\frac{W_p^3}{16}\right)\pmod{p^4}.
}
\tag{3.16}
$$


This is the uniquely determined root with residue $I_p$, not an additional sign assumption.

For an entirely explicit fourth-precision input to (3.16), let


$$
W_0=\frac{i+(i/z)\Gamma_p^2-I_p^2}{I_p^2},
\qquad
\kappa_p=\frac{i}{zI_p^2}.
$$


Then


$$
\begin{aligned}
W_p\equiv W_0+\kappa_p\bigl[
&2p\Gamma_pL_0
+p^2(L_0^2-2\Gamma_pL_1)\\
&+p^3(2\Gamma_pL_2-2L_0L_1)
\bigr]\pmod{p^4}.
\end{aligned}
\tag{3.17}
$$


Thus (3.14), (3.16), and (3.17) are a complete prime-half Gaussian reduction through $p^4$. The displayed sums are evaluated binomial-harmonic expressions with prescribed weights; no independent higher Gaussian quotient has been introduced.

### 3.5 The actual Gaussian gcd has a useful arithmetic restriction

The preceding reduction is supplemented by an exact restriction on exceptional Gaussian division.

The Chebyshev identity


$$
T_N(w)^2+T_{N-1}(w)^2
-2wT_N(w)T_{N-1}(w)=1-w^2=4+4i
$$


gives the following two integer identities. Write


$$
A=a_N,\qquad B=a_{N-1},\qquad g=g_B.
$$


Then


$$
\boxed{
AB+1=\frac g2(A+B)(\alpha+\beta)+g^2\alpha\beta,
}
\tag{3.18}
$$




$$
\boxed{
(A+B)^2-4
=g^2(\alpha+\beta)^2-4g(A\alpha+B\beta).
}
\tag{3.19}
$$



If an odd prime $p\mid g$, these imply


$$
AB\equiv-1,\qquad (A+B)^2\equiv4\pmod p,
$$


hence


$$
(A-B)^2\equiv8\pmod p.
$$


Therefore


$$
\boxed{
p\mid g_B,\ p\text{ odd}
\quad\Longrightarrow\quad
\left(\frac2p\right)=1
\quad\Longrightarrow\quad
p\equiv1\text{ or }7\pmod8.
}
\tag{3.20}
$$


In particular, on the congruence classes $p\equiv3,5\pmod8$, the raw Gaussian values need no $p$-power gcd removal:


$$
v_p(g_B)=0.
\tag{3.21}
$$



There is also an exact ramified-prime payment. The imaginary recurrence gives


$$
b_j\equiv2j\pmod4.
$$


One of two adjacent indices is odd, so


$$
\boxed{v_2(g_B)=1.}
\tag{3.22}
$$


For the original odd $N$, specifically, $b_N\equiv2\pmod4$.

These are genuine numerical restrictions on the actual Gaussian denominator. They do **not** prove fourth-depth source separation.

### 3.6 Exceptional primes and precision before division

The half-angle algebra uses square roots of $i$ and $z$, both units away from $2$. Its discriminants introduce no odd ramified prime. The formulas above invert only $2$, $i$, $z$, and integers below $p$. In particular, there is no hidden inversion of $w=-1+2i$, so $p=5$ is not an additional Gaussian-algebra exception.

For $p\in\mathcal S_N$, all primes are already $>5$. The cases $2,3,5$ are outside this interval argument and remain in the all-prime producer; (3.22) records, rather than suppresses, the ramified Gaussian payment.

Let


$$
a_G=v_p(g_B),\qquad g_B=p^{a_G}g_0,\qquad p\nmid g_0.
$$


For target precision $p^{\mathsf d}$:

* a divided linear Gaussian datum requires its actual numerator modulo
  

$$
p^{a_G+\mathsf d};
$$


* a raw quadratic Gaussian source column divided by $g_B^2$ requires its numerator modulo
  

$$
\boxed{p^{2a_G+\mathsf d}.}
$$



Thus (3.14)–(3.17) alone are a sufficient raw fourth-precision calculation only when $a_G=0$. If $a_G>0$, use the exact product (3.13), the exact even-binomial formula (3.4), or the corresponding unit-root lifting to the required larger raw modulus **before** dividing.

No fifth-digit nonvanishing claim is involved here. This is the necessary precision payment for the same fourth-depth divided source test.

---

## 4. The actual divided Gaussian columns

The new reduction now enters the original columns, not an auxiliary eigenvalue model.

Define the actual Gaussian values from (3.7):


$$
G_-:=D_{h-1}\mathsf X_p+E_{h-1}\mathsf Y_p,
\qquad
G_+:=D_h\mathsf X_p+E_h\mathsf Y_p.
$$


Then exactly


$$
G_-=C_{N-1}(i),\qquad G_+=C_N(i).
$$


Write


$$
A_-=\operatorname{Re}G_-,\quad B_-=\operatorname{Im}G_-,
\qquad
A_+=\operatorname{Re}G_+,\quad B_+=\operatorname{Im}G_+,
$$


and


$$
D_G=A_+B_--A_-B_+.
\tag{4.1}
$$


The actual divided quantities are


$$
\boxed{
\alpha=B_-/g_B,\qquad
\beta=B_+/g_B,\qquad
\delta=D_G/g_B.
}
\tag{4.2}
$$


In particular, $\delta$ is not being varied independently of $\alpha,\beta$.

The complete raw quadratic dictionary is


$$
\widehat P=nB_-^2+(n-2)B_+^2,
$$




$$
\widehat Q=
4(n-1)(n-2)B_+^2-2(n-1)B_-B_+,
$$




$$
\boxed{
\widehat C_V=B_-^2+(2n-3)B_+^2-D_G^2,
}
$$




$$
\boxed{
\widehat C_F^E=B_-^2+(5-2n)B_+^2+4B_-B_+.
}
\tag{4.3}
$$


Every entry is divisible by $g_B^2$, and


$$
(P,Q,C_V,C_F^E)
=
g_B^{-2}(\widehat P,\widehat Q,\widehat C_V,\widehat C_F^E).
\tag{4.4}
$$



Equations (3.13)–(3.17), (4.1), and (4.3) therefore evaluate the actual divided Gaussian source and endpoint coefficients. They retain both the $-\delta^2$ source constant and the $4\alpha\beta$ endpoint constant.

---

## 5. Substitution into FULL23’s complete elimination

FULL23’s recombination, pivot theorem, and compatibility identity are used at their stated scope. Their pending different review is not represented as completed here.

### 5.1 The four prime-base vectors being retained

For $0\le h'\le a$, let


$$
\mathsf h_{a,h'}=\frac{(2a-h')!}{(a-h')!\,h'!},
$$


and for $1\le j\le a$, let


$$
\mathsf b_j=\frac{4^j j!((j-1)!)^2}{2(2j)!}.
$$


Use the exact products


$$
\mathsf S_{p,h'}
=
\prod_{t=1}^{h'}
\frac{(1-2p/(2t-1))(1-p/t)}
     {(1-2p/t)(1-p/(2t-1))},
$$




$$
\mathsf T_{p,j}
=
\prod_{v=1}^{j-1}\left(1-\frac{p^2}{v^2}\right).
$$


Their displayed denominators are units at the current prime.

The weights are


$$
A_{h'}^+=2h'^2-p(2h'+1),
$$




$$
\widetilde A_{h'}^-=2h'(h'-2)-p(2h'-1),
$$




$$
A_j^-=2j(j+2)-p(2j+3).
$$


Then


$$
\mathbf A_p^+
=
\chi
\binom{
\sum_{h'=0}^a(-1)^{h'}\mathsf h_{a,h'}\mathsf S_{p,h'}
}{
\frac1{p-1}\sum_{h'=0}^a
(-1)^{h'}A_{h'}^+\mathsf h_{a,h'}\mathsf S_{p,h'}
},
$$




$$
\mathbf A_p^-
=
\chi
\binom{
\sum_{h'=0}^a\mathsf h_{a,h'}\mathsf S_{p,h'}
}{
\frac1{p-1}\sum_{h'=0}^a
\widetilde A_{h'}^-\mathsf h_{a,h'}\mathsf S_{p,h'}
},
$$


and


$$
\mathbf L_p^+
=
\binom{
p\sum_{j=1}^a\mathsf b_j\mathsf T_{p,j}
}{
\frac{1+p\sum_{j=1}^aA_j^+\mathsf b_j\mathsf T_{p,j}}{p-1}
},
$$




$$
\mathbf L_p^-
=
\binom{
p\sum_{j=1}^a(-1)^{j+1}\mathsf b_j\mathsf T_{p,j}
}{
\frac{-1+p\sum_{j=1}^a(-1)^{j+1}A_j^-\mathsf b_j\mathsf T_{p,j}}{p-1}
}.
\tag{5.1}
$$


The lower constants $+1$ and $-1$ remain.

FULL23 gives the exact states


$$
\binom{\Theta_p}{\Theta_{p-1}}
=\rho_p\mathbf A_p^++\mathbf L_p^+,
\qquad
\binom{\Phi_p}{\Phi_{p-1}}
=\rho_p\mathbf A_p^-+\mathbf L_p^-.
\tag{5.2}
$$


In the present substitution, the scalar is also exactly


$$
\rho_p=\frac{\Gamma_p^8}{16(p+1)}
$$


by (3.12).

### 5.2 The full $r$-dependent transport, including both returns

For $0\le j\le r$, define


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
\boxed{
\mathbf h_{j+1}^-
=T_{p+j}\mathbf h_j^--\binom{2(-1)^j}{0}.
}
\tag{5.3}
$$


The minus sign in the last equation is required because $p$ is odd.

These are explicitly evaluated by the retained integer kernel


$$
\mathcal K_q(x)
=
\sum_{v=0}^{\lfloor q/2\rfloor}
\binom{q-v}{v}(-4)^{q-2v}(x+v+1)_{q-2v},
\qquad \mathcal K_{-1}=0.
$$


For $j\ge1$,


$$
S_j=
\begin{pmatrix}
\mathcal K_j(p-1)&\mathcal K_{j-1}(p)\\
\mathcal K_{j-1}(p-1)&\mathcal K_{j-2}(p)
\end{pmatrix},
$$




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
\tag{5.4}
$$


The largest shifted step is


$$
p+r-1=n-1.
$$



Consequently all four complete columns are


$$
16U=
\mathscr C_U-(\mathscr A,\mathscr B)
\bigl(\rho_pS_s\mathbf A_p^+
+S_s\mathbf L_p^++\mathbf h_s^+\bigr),
$$




$$
\boxed{
g_B^2V=
\widehat C_V-(\widehat P,\widehat Q)
\bigl(\rho_pS_r\mathbf A_p^+
+S_r\mathbf L_p^++\mathbf h_r^+\bigr),
}
$$




$$
16E_K=
\mathscr C_E+(\mathscr A,\mathscr B)
\bigl(\rho_pS_s\mathbf A_p^-
+S_s\mathbf L_p^-+\mathbf h_s^-\bigr),
$$




$$
\boxed{
g_B^2E_F=
\widehat C_F^E-(\widehat P,\widehat Q)
\bigl(\rho_pS_r\mathbf A_p^-
+S_r\mathbf L_p^-+\mathbf h_r^-\bigr).
}
\tag{5.5}
$$


This is the requested application of the Gaussian reduction to the actual quotient and constants. Neither residual transport has been replaced by the arc-special branch.

### 5.3 Explicit substitution into the four cubic compatibility coefficients

Here is a physical-terminal form of the substitution into


$$
\mathscr Z_{p,N}^{[4]}=Z_0+pZ_1+p^2Z_2+p^3Z_3.
$$



Use the retained harmonic coefficients


$$
L_{1,h'}=\frac32H_{h'}^{(1)}-H_{2h'}^{(1)},
$$




$$
L_{2,h'}=\frac{15}{4}H_{h'}^{(2)}-3H_{2h'}^{(2)},
\qquad
L_{3,h'}=\frac{63}{8}H_{h'}^{(3)}-7H_{2h'}^{(3)},
$$




$$
H_{0,h'}=1,\quad H_{1,h'}=L_{1,h'},
$$




$$
H_{2,h'}=\frac{L_{1,h'}^2+L_{2,h'}}2,
$$




$$
H_{3,h'}=
\frac{L_{1,h'}^3+3L_{1,h'}L_{2,h'}+2L_{3,h'}}6.
$$


Define $\mathbf A_d^+$, $0\le d\le3$, by replacing $\mathsf S_{p,h'}$ in $\mathbf A_p^+$ with $H_{d,h'}$.

Also put


$$
\mathbf B_0^+
=
\binom{
\sum_{j=1}^a\mathsf b_j
}{
\frac1{p-1}\sum_{j=1}^aA_j^+\mathsf b_j
},
$$




$$
\mathbf B_2^+
=
\binom{
\sum_{j=1}^a\mathsf b_jH_{j-1}^{(2)}
}{
\frac1{p-1}\sum_{j=1}^aA_j^+\mathsf b_jH_{j-1}^{(2)}
},
\qquad
\mathbf L_0=\frac1{p-1}\binom01.
$$


Then


$$
\mathbf A_p^+\equiv\sum_{d=0}^3p^d\mathbf A_d^+\pmod{p^4},
$$




$$
\mathbf L_p^+\equiv
\mathbf L_0+p\mathbf B_0^+-p^3\mathbf B_2^+\pmod{p^4}.
\tag{5.6}
$$



Let $R_U=(\mathscr A,\mathscr B)$ and $\widehat R_G=(\widehat P,\widehat Q)$. Define


$$
\mathcal V_d=R_US_s\mathbf A_d^+,
\qquad
\widehat{\mathcal W}_d=\widehat R_GS_r\mathbf A_d^+,
$$




$$
D_0^U=\mathscr C_U-R_U(S_s\mathbf L_0+\mathbf h_s^+),
$$




$$
D_1^U=-R_US_s\mathbf B_0^+,\qquad
D_3^U=R_US_s\mathbf B_2^+,
$$


and


$$
\widehat D_0^G
=\widehat C_V-\widehat R_G(S_r\mathbf L_0+\mathbf h_r^+),
$$




$$
\widehat D_1^G=-\widehat R_GS_r\mathbf B_0^+,\qquad
\widehat D_3^G=\widehat R_GS_r\mathbf B_2^+.
\tag{5.7}
$$


All the Gaussian quantities in these expressions are those of (3.7), (4.1), and (4.3).

The four compatibility coefficients, after actual raw clearing, are


$$
\boxed{
g_B^2Z_0
=\mathcal V_0\widehat D_0^G-D_0^U\widehat{\mathcal W}_0,
}
$$




$$
\boxed{
\begin{aligned}
g_B^2Z_1={}&
\mathcal V_1\widehat D_0^G
+\mathcal V_0\widehat D_1^G\\
&-D_0^U\widehat{\mathcal W}_1
-D_1^U\widehat{\mathcal W}_0,
\end{aligned}
}
$$




$$
\boxed{
\begin{aligned}
g_B^2Z_2={}&
\mathcal V_2\widehat D_0^G
+\mathcal V_1\widehat D_1^G\\
&-D_0^U\widehat{\mathcal W}_2
-D_1^U\widehat{\mathcal W}_1,
\end{aligned}
}
$$




$$
\boxed{
\begin{aligned}
g_B^2Z_3={}&
\mathcal V_3\widehat D_0^G
+\mathcal V_2\widehat D_1^G
+\mathcal V_0\widehat D_3^G\\
&-D_0^U\widehat{\mathcal W}_3
-D_1^U\widehat{\mathcal W}_2
-D_3^U\widehat{\mathcal W}_0.
\end{aligned}
}
\tag{5.8}
$$



These are the same compatibility coefficients expressed at the physical terminal. To check the identification, note that


$$
S_r=TS_s,\qquad
\mathbf h_r^+=T\mathbf h_s^++f_6.
$$


Therefore


$$
\widehat R_GS_r=g_B^2(\Pi,\Omega)S_s,
$$


and


$$
\widehat C_V-\widehat R_Gf_6=g_B^2C^{\rm s}.
$$


Thus the second row in (5.7) is exactly the original divided source row after multiplying by $g_B^2$. Expanding (5.6) gives (5.8).

The term $-D_G^2$ remains inside $\widehat D_0^G$, and hence contributes to every relevant coefficient in (5.8). It has not been discarded during elimination.

### 5.4 A scalar form displaying the remaining Gaussian relation

The substitution can also be written without a new determinant.

Use exact, untruncated products for the moment, and set


$$
v_1=R_US_s\mathbf A_p^+,
$$




$$
d_1=\mathscr C_U-R_U(S_s\mathbf L_p^++\mathbf h_s^+).
$$


Write


$$
S_r\mathbf A_p^+=\binom{x_r}{y_r},
\qquad
S_r\mathbf L_p^++\mathbf h_r^+=\binom{\ell_r}{m_r},
$$


and define the evaluated scalars


$$
T_r=v_1\ell_r+d_1x_r,\qquad
T_{r-1}=v_1m_r+d_1y_r.
$$


Expansion of the physical-terminal second row gives the exact identity


$$
\boxed{
\begin{aligned}
g_B^2\mathscr Z_{p,N}={}&
(v_1-nT_r)B_-^2
+2(n-1)T_{r-1}B_-B_+\\
&+\bigl((2n-3)v_1-(n-2)T_r
-4(n-1)(n-2)T_{r-1}\bigr)B_+^2\\
&-v_1(A_+B_--A_-B_+)^2.
\end{aligned}
}
\tag{5.9}
$$


Every $A_\pm,B_\pm$ here is explicitly obtained from the one actual quotient (3.13), the prescribed power $\Gamma_p$, and the norm root (3.16).

Equation (5.9) is the precise Gaussian value relation that replaces a free quadratic form in $\alpha,\beta,\delta$. It is quartic in the raw adjacent Gaussian coordinates because the actual $\delta$-numerator is quadratic in those coordinates.

Using (5.6) in (5.9), or equivalently the coefficient table (5.8), gives the whole cubic expression. If


$$
a_G=v_p(g_B),
$$


then, after an actual third collision,


$$
\boxed{
\frac{\mathscr Z_{p,N}}{p^3}
\equiv
g_0^{-2}
\frac{g_B^2(Z_0+pZ_1+p^2Z_2+p^3Z_3)}
     {p^{2a_G+3}}
\pmod p.
}
\tag{5.10}
$$


The numerator must first be formed modulo $p^{2a_G+4}$. This is the whole lower-order carry, not $Z_3\bmod p$.

### 5.5 The actual $q^*$-target is coupled to the same Gaussian power

FULL23 proves that, when $j_p=0$, at least one actual component $v_i$ is a unit. Its hypotheses are those of the original objects:


$$
\lambda_p:=\min(v_p(v_1),v_p(v_2))
\le v_p(\Delta)\le j_p,
$$


using the adjacent Hermite determinant and the original source matrix.

For a unit component, retain


$$
q^*_{p,N;i}=\frac{(p+1)d_i-v_i}{p\,v_i}.
$$


By (3.12),


$$
\boxed{
q_p(4)-q^*_{p,N;i}
=
\frac{\Gamma_p^8v_i-16(p+1)d_i}{16p\,v_i}.
}
\tag{5.11}
$$


Thus the remaining quotient test is not a comparison with an independent Fermat variable.

Under the actual third collision, its fourth residue is


$$
\boxed{
\frac{q_p(4)-q^*_{p,N;i}}{p^2}
\equiv
\frac{\Gamma_p^8v_i-16(p+1)d_i}{16p^3v_i}
\pmod p.
}
\tag{5.12}
$$



For $i=2$, define the raw second-row values


$$
\widehat v_2
=(\widehat P,\widehat Q)S_r\mathbf A_p^+,
$$




$$
\widehat d_2
=\widehat C_V-(\widehat P,\widehat Q)
(S_r\mathbf L_p^++\mathbf h_r^+).
$$


Then $v_2=\widehat v_2/g_B^2$, $d_2=\widehat d_2/g_B^2$, and the numerator test in (5.12) becomes


$$
\Gamma_p^8\widehat v_2-16(p+1)\widehat d_2
\pmod{p^{2a_G+4}}.
\tag{5.13}
$$


Again the actual $g_B^2$-division is paid before identifying the fourth divided residue.

---

## 6. What the new substitution proves—and what remains unpaid

### 6.1 New proved statements

The following conclusions are unconditional algebraic results on the stated original scope.

1. The sharpened determinant bound (1.1) holds after actual Gaussian division.

2. On $N=(p+r)/2$, the actual adjacent Gaussian values satisfy the generic reduction (3.7).

3. The prime-base data obey the exact norm relation (3.9), and one actual Gaussian Lucas quotient has the complete evaluation (3.13) and fourth-precision expansion (3.14).

4. The common Fermat scalar satisfies the exact coupling
   

$$
\rho_p=\Gamma_p^8/[16(p+1)].
$$



5. Odd primes dividing $g_B$ must satisfy $p\equiv1,7\pmod8$, and $v_2(g_B)=1$.

6. The resulting actual divided Gaussian arithmetic enters all four original columns by (4.3)–(5.5), and enters the whole cubic compatibility and the actual $q^*$-target by (5.8)–(5.13).

These are more restrictive than assigning arbitrary residues to $\alpha,\beta,\delta$. In particular, the source constant $-\delta^2$ is now visibly tied to the same prime-half Gaussian values as $\alpha,\beta$.

### 6.2 The exact outstanding numerical assertion

The desired primary noncoincidence is still not proved.

A concrete follow-on lemma can now be stated without free Gaussian quotient variables.

> **Actual Gaussian–Lucas fourth-contact lemma — open.**  
> Let $N=9^{18+32u}$, let $p\in\mathcal S_N$, assume $B_p=j_p=0$, and suppose $p^3\mid U,V$.  
> Evaluate $\mathscr L_p$ by (3.13), $\mathsf Y_p=\Gamma_p+p\mathscr L_p$, and $\mathsf X_p$ by the norm identity with residue $I_p$, using the paid raw precision. Form the actual Gaussian coordinates by (3.7), the raw source coefficients by (4.3), and the complete transport by (5.3)–(5.4).  
> Then at least one of the following two **evaluated whole residues** is nonzero:
> 

$$
> g_0^{-2}
> \frac{g_B^2(Z_0+pZ_1+p^2Z_2+p^3Z_3)}
>      {p^{2a_G+3}}
> \pmod p,
>
$$


> 

$$
> \frac{\Gamma_p^8v_i-16(p+1)d_i}{16p^3v_i}
> \pmod p,
>
$$


> where $v_i$ is an actual unit pivot. For $i=2$, the second expression is formed using the paid raw numerator (5.13).

All terms and all divisions in this statement have now been specified in the original objects. The remaining unpaid relation is numerical: the actual binomial-harmonic Gaussian quotient (3.13) could, on present evidence, make both whole evaluated expressions vanish.

The norm relation does not by itself exclude this. Nor does the fact that its derivative at the selected root is a unit. A unit derivative establishes unique lifting of the actual norm branch; it does not establish nonvanishing of the separate source value evaluated on that branch.

Likewise, the restriction $p\mid g_B\Rightarrow p\equiv1,7\pmod8$ pays part of the division analysis but does not rule out fourth source contact in either congruence class.

### 6.3 The rigorous conditional implication

FULL23’s fourth-depth equivalence gives


$$
\left(\frac{16U}{p^3},\frac V{p^3}\right)\not\equiv(0,0)\pmod p
$$


if and only if the two residues just displayed are not both zero.

Therefore, **if** the follow-on lemma is proved, then on the primary branch


$$
c_p=3,\qquad e_p\le1.
$$


More generally, the target remains


$$
\mathsf d=4+B_p+j_p.
$$


A nonzero complete source pair at modulus $p^{\mathsf d}$ would imply


$$
c_p\le3+B_p+j_p,\qquad e_p\le1+j_p.
$$


No such universal assertion or quantitatively significant fixed-$N$ coverage is proved here.

### 6.4 Critical primes and larger paid precision

For $j_p>0$, retain the proved bound


$$
\lambda_p\le v_p(\Delta)\le j_p.
$$


If $c_p\ge\lambda_p$, the vectors


$$
\mathbf v'=\mathbf v/p^{\lambda_p},
\qquad
\mathbf d'=\mathbf d/p^{\lambda_p}
$$


are $p$-integral and one component of $\mathbf v'$ is a unit. The original critical-safe charts remain available; no inversion of $\Delta$ is introduced.

At precision $p^{4+B_p+j_p}$, use:

* the exact Gaussian product (3.13), not merely (3.14);
* the exact products in (5.1), not merely the cubic truncation;
* the full transports and both returns through $r$;
* raw Gaussian precision $a_G+\mathsf d$ for divided linear data, or $2a_G+\mathsf d$ for raw quadratic columns;
* normalization by the proved $p^{\lambda_p}$ before a unit-pivot test.

The actual $h_p,b_p,z_p,t_p$ still determine $B_p$. A calculation stopping at $p^4$ does not determine a valuation continuing beyond that modulus.

### 6.5 No aggregate-height certificate is claimed

This report does not propose the cubic compatibility as a fixed-$N$ aggregate certificate.

For clarity, FULL23’s sufficient clearer says


$$
\mathcal K_p:=48\operatorname{lcm}(1,\ldots,p-1)^4,
\qquad
\mathcal Z_{p,N}:=\frac{\mathcal K_p}{\chi}\mathscr Z_{p,N}^{[4]}
\in\mathbb Z.
$$


The division by $\chi$ is termwise in this particular expression. It is not a division of $U,V$, the mixed minors, or the original producer.

The actual reduced numerator and denominator of
$\mathscr Z_{p,N}^{[4]}/\chi$ are exactly


$$
\frac{\mathcal Z_{p,N}}
     {\gcd(\mathcal Z_{p,N},\mathcal K_p)},
\qquad
\frac{\mathcal K_p}
     {\gcd(\mathcal Z_{p,N},\mathcal K_p)}.
$$


This all-prime normalization supplies no bound for the height of its evaluated numerator. Moreover:

* it depends on $p$;
* a cubic congruence transfers contact only through its stated fourth precision;
* no one fixed-$N$ integer receiving the required contact mass has been produced.

The FULL21 obstruction for the different primitive mixed ratios is not being transferred to this expression. Conversely, an exponential sufficient denominator bill is not being promoted to an exponential numerator-height theorem.

---

## 7. Preservation of the complete endpoint identity and returns

The new Gaussian substitution changes neither the endpoint chart nor its additive identity.

Let


$$
\mathbf t_j=\binom{\Theta_j}{\Theta_{j-1}},
\qquad
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



The actual minors remain


$$
\mathfrak A_{p,N}=\det(\mathbf R,\mathbf u),
\qquad
\mathfrak B_{p,N}=\det(\mathbf u,\mathbf E).
$$


The safe choice is the retained one:


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


and


$$
c_p-2=
\min\bigl(v_p(16U/p^2),v_p(\zeta_{p,N}/p^2)\bigr).
$$



The residual-source identity is


$$
\begin{aligned}
\mathfrak A_{p,N}={}&
\mathscr I_1(\Theta_s-\Theta_\ell)
+\mathscr I_2(\Theta_{s-1}-\Theta_{\ell-1})\\
&+\Delta(\Theta_s\Theta_{\ell-1}
-\Theta_{s-1}\Theta_\ell).
\end{aligned}
\tag{7.1}
$$



For the endpoint identity, the actual defects are


$$
\sigma_0^+=\frac{\Theta_p-\chi Q_a^{\rm H}}p,\qquad
\sigma_1^+=\frac{\Theta_{p-1}+1+\chi Q_k^{\rm H}}p,
$$




$$
\sigma_0^-=\frac{\Phi_p-\chi P_a^{\rm H}}p,\qquad
\sigma_1^-=\frac{\Phi_{p-1}-1+\chi P_k^{\rm H}}p.
$$


Retain


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


and the full mixed return


$$
\mathfrak f_{s;p}
=
-\sum_{t=1}^{s-1}(-1)^t
\bigl(\Theta_t\Phi_{p+t}+\Phi_t\Theta_{p+t}\bigr).
$$


Then


$$
\boxed{
\begin{aligned}
\mathfrak B_{p,N}
={}&R_1E_2-R_2E_1\\
&-\Delta\left(
2(-1)^a\chi^2+p\chi\Lambda_\sigma
+p^2\Xi_\sigma+4p\mathfrak f_{s;p}
\right).
\end{aligned}
}
\tag{7.2}
$$


Both signed state systems in (5.5) enter this whole additive difference.

The actual mixed normalization remains


$$
d_{\rm mix}
=\gcd(\mathfrak D_{s;p},\mathfrak A_{p,N},\mathfrak B_{p,N}),
$$




$$
A_{\rm mix}=\mathfrak A_{p,N}/d_{\rm mix},\quad
B_{\rm mix}=\mathfrak B_{p,N}/d_{\rm mix},\quad
D_{\rm mix}=\mathfrak D_{s;p}/d_{\rm mix}.
$$


It is the actual least simultaneous clearer of the two mixed ratios. It is not replaced by the Gaussian norm normalization or by the local cubic clearer.

### 7.1 Source, endpoint, and canonical Hermite returns

The source balance is unchanged:


$$
\begin{aligned}
&(\nu\mathscr A-16\tau\Pi)\Theta_\ell
+(\nu\mathscr B-16\tau\Omega)\Theta_{\ell-1}\\
&\hspace{15mm}=\nu\mathscr C_U-16\tau C^{\rm s}.
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
\tag{7.3}
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
\tag{7.4}
$$


The complete relation


$$
z_\ell^{\rm ret}w_{\ell-1}
-z_{\ell-1}^{\rm ret}w_\ell
=-16\Delta(UX+VY)
$$


is retained without division by $\Delta$.

For exactly $0\le b\le N$, retain


$$
\mathcal R_{b;N}=d_KP_b^{\rm H}U+Q_b^{\rm H}y_K,
$$




$$
\Psi_j^{(b)}=Q_b^{\rm H}\Phi_j-P_b^{\rm H}\Theta_j,
$$




$$
\Psi_{j+1}^{(b)}+4j\Psi_j^{(b)}-\Psi_{j-1}^{(b)}
=
2\bigl(Q_b^{\rm H}(-1)^j-P_b^{\rm H}\bigr),
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
\tag{7.5}
$$


The original endpoint payment is still


$$
\mathcal R_{N-1;N}<0<\mathcal R_{N;N},
$$




$$
\frac{c(r^\circ)^2}{\kappa_N^{\rm prod}}
\mid \mathcal R_{N-1;N}\mathcal R_{N;N},
\qquad
v_p(\kappa_N^{\rm prod})=[c_p-H_p]_+.
\tag{7.6}
$$


No credit has moved from $N-1,N$ to the prime-base anchors $a,k$.

The older rational interface also retains its separate paid quantities


$$
Q_{\rm loc}(n)=\prod_{b=0}^{12}(n-b),\qquad
\mathcal L_n=\operatorname{lcm}(1,\ldots,n),
$$


and


$$
\frac{2\mathcal L_n}{j^2-1}
=
\frac{\mathcal L_n}{j-1}-\frac{\mathcal L_n}{j+1}.
$$


They do not replace either least arc clearer.

---

## 8. Both arcs, the all-prime gcd, and the whole error

Retain


$$
R_F=4\int_0^1\frac{F^2-\delta^2}{1+t^2}\,dt,
\qquad
R_K=4\int_0^1\frac K{1+t^2}\,dt.
$$


Their quotient polynomial degrees are at most $2N-2$.

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
\frac{\alpha^2\xi_n+\beta^2\xi_{n-2}
-2\alpha\beta\xi_{n-1}}2.
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
\tau R_F+\nu R_K=\frac b\lambda,
\qquad \gcd(b,\lambda)=1,\quad \lambda>0.
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
\boxed{
p_N=A/G,\qquad q_N=\lambda M/G.
}
\tag{8.1}
$$


Since $\gcd(\lambda,A)=1$, this is the actual primitive pair. None of the local normalizations in this report changes it.

The original polynomial and whole error remain


$$
P_N(t)=\frac{F(t)^2+(V/U)K(t)}{\delta^2}
=\frac{W_{\rm prim}(t)}M,
$$




$$
\boxed{
\epsilon_N=
\int_0^1P_N(t)\left(e^t+\frac4{1+t^2}\right)\,dt>0.
}
\tag{8.2}
$$


Both positive weight terms are present. The exact source balance gives


$$
\eta(W_{\rm prim})=M,
$$


and finite integration by parts together with both arcs gives


$$
\epsilon_N=e+\pi-\frac{A}{\lambda M}.
$$


Thus, at the same original indices,


$$
\boxed{
q_N(e+\pi)-p_N=q_N\epsilon_N>0.
}
\tag{8.3}
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


Consequently,


$$
\boxed{
q_NJ_N=\frac{\lambda_N}{G_N}
\bigl(\tau_NJ_F+\nu_NJ_K\bigr).
}
\tag{8.4}
$$


Both positive summands remain.

A proof that the right side of (8.4) tends to zero along an infinite subsequence of these same original indices would prove irrationality: if $e+\pi=A_0/B_0$ were rational, every nonzero value in (8.3) would have absolute value at least $1/B_0$. No such same-index decay estimate is established here.

---

## 9. Proof-status and bounded-arithmetic ledger

| Item | Status |
|---|---|
| Different audit of the new sharper $\Delta$ bill | **Passed**, with the stronger constant in (1.1) |
| Older $J_N^{\rm aff}$ bill | Retained separately; its $\delta^2$ terms remain |
| Generic prime-half Gaussian identities (3.7) | **New proved application** of classical Chebyshev arithmetic |
| Exact norm constraint and one actual quotient (3.9), (3.13) | **New proved source-specific reduction** |
| Fourth-precision Gaussian evaluation (3.14)–(3.17) | **Proved**, with stated raw-division precision |
| $p\mid g_B\Rightarrow p\equiv1,7\pmod8$; $v_2(g_B)=1$ | **New proved arithmetic restrictions** |
| Substitution into all four original columns | **Proved**, with both constants and both returns |
| Substitution into the whole $Z^{[4]}$ and actual $q^*$-target | **Proved**, equations (5.8)–(5.13) |
| FULL23 elimination and pivot theorem | Reuse at stated scope; no self-audit claimed |
| Nonzero fourth residue at every assigned original pair | **Open** |
| Absolute paid depth bound or significant fixed-$N$ mass theorem | **Not proved** |
| Fixed-$N$ aggregate compatibility certificate of exponential height | **Not proposed or proved** |
| Smaller primes and primes $p>2N$ | Separate obligations remain |
| Actual contents, mixed clearer, both arcs, least $D,\lambda$, all-prime $G$, primitive $q_N$ | Retained |
| Irrationality or rationality of $e+\pi$ | **Unresolved** |

### Bounded exact arithmetic

No original-sized solve, prime scan, or numerical evaluation at an original pair is needed for the proofs above, and none is requested.

An optional, bounded symbolic checksum for the new unit-root truncation has the following mathematical specification:

* **Input:** the polynomial
  

$$
S(W)=1+\frac W2-\frac{W^2}{8}+\frac{W^3}{16}
  \quad\text{in }\mathbb Q[W].
$$


* **Expected exact output:**
  

$$
\boxed{
  256\bigl(S(W)^2-1-W\bigr)
  =20W^4-4W^5+W^6.
  }
$$


* **Scope:** this verifies only the displayed finite polynomial identity underlying (3.16). It is not evidence for numerical source noncoincidence at any original pair.

All substantive new statements have derivations above and do not depend on this optional checksum.

---

## Final conclusion

The sharper actual determinant-conditioning bound is valid:


$$
\boxed{
0<|\Delta|
<
3\cdot10^9(2N)^{14}\frac{5^{2N}}{g_B^2}.
}
$$


The proof uses only the $\alpha,\beta$ quadratic form in the actual six-step determinant. It does not reduce the separate $J_N^{\rm aff}$ bill, whose complete constant contains $\delta^2$.

The primary new result is a generic, source-specific Gaussian reduction at


$$
N=\frac{p+r}{2},\qquad 13\le r<N,\quad r\text{ odd}.
$$


It expresses the actual adjacent Gaussian coefficients through one explicitly evaluated Gaussian Lucas quotient, an exact norm relation, and the prescribed power


$$
\Gamma_p=(-1+i)^{(p+1)/2}.
$$


The same power satisfies


$$
\Gamma_p^8=16\,4^{p-1},
$$


so the Gaussian arithmetic and FULL23’s common Fermat scalar are demonstrably coupled. The actual quotient by $g_B$, the complete $-\delta^2$ term, all four columns, and the full transports through physical $2N$ have been substituted into the whole cubic compatibility and its actual $q^*$-target.

What remains unpaid is now an explicit **evaluated Gaussian–Lucas value-contact assertion**: after the admitted lower collisions, one must exclude simultaneous vanishing of (5.10) and (5.12), with the actual quotient (3.13) and all raw precision paid. The norm identity and the new congruence restriction on primes dividing $g_B$ do not yet exclude that cancellation.

No fourth-depth separation theorem, absolute paid-depth substitute, or significant fixed-$N$ coverage theorem follows at present. The all-prime final gcd, actual primitive denominator, and nonzero whole error remain unchanged at $N=9^{18+32u}$. Accordingly, this continuation advances the arithmetic reduction but does not decide the rationality or irrationality of $e+\pi$.
