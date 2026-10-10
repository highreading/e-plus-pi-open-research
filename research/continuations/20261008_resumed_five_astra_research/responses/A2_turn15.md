> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Audit of the complete five-column perturbation, the linear mixed-return window, and a second full-rank cancellation

## 1. Conclusions and proof status

The rationality or irrationality of $e+\pi$ remains unresolved.

This report has three main conclusions.

1. **The new complete perturbation theorem in A4 turn 22 passes.**  
   With the reference pencil defined by its actual six-column cofactors—not by substituting an approximate inverse into the corrected pencil—the first perturbation is
   

$$
2^{-(L_d+7)}
   \bigl(\mathcal P_k^{[5]}-\mathcal P_k^{[5],{\rm C}}\bigr)_{r}(i)
   \equiv
   \binom i5\,\kappa_d(r)\pmod2,
$$


   where
   

$$
\kappa_d(r)=S_5(r)+\eta_{r+2d+(r\mathbin{\&}d)}.
$$


   Both complete coefficient-border differences are zero at this layer. The values
   $\kappa_d(2)=\kappa_d(3)=1$ prove rank exactly one. This conclusion includes the changes in the selected pivot columns; the direct bottom-return summand alone would not prove it.

2. **The parent general kernel, linear mixed-rank theorem, and complete equality-tie formula pass under their stated finite hypotheses.**  
   In particular, the odd-parameter derivative is necessary, all higher mixed rows satisfy
   

$$
U_{p+1}(z)=U_p(z)+U_p(z+1),
$$


   and, on the stated original columns,
   

$$
\operatorname{rank}[R_{p+1};U_p(0);\ldots;U_p(h-1)]=p+h.
$$


   After paying every leading-sector scalar, the equality-tie contribution is indeed
   

$$
\det\!\left[
   R_p;\
   v_{\rm new}+V_{h-1};\
   V_0+V_1;\
   \ldots;\
   V_{h-2}+V_{h-1}
   \right].
$$


   Thus the asserted complete common-column cofactors attain $F_q(p)$ on the same infinite original rotation subfamily. This is individual cofactor existence, not an unchanged all-rank elimination algorithm.

3. **A new full-rank result is proved here: the next aggregate binary digit also vanishes.**  
   Let
   

$$
D_k=\det[w_*,v^{(0)},\ldots,v^{(d)}],\qquad
   \mathfrak m_d=\min_{1\le p\le d}\mathcal L_p(d),
$$


   with the exact definitions below. Then, at every original index,
   

$$
\boxed{2^{\mathfrak m_d+2}\mid D_k.}
   \tag{1.1}
$$


   The proof retains all product counts, all factorial-forcing patterns, the atom-in-bottom patterns, and the near-minimal $N_d$-minors. The decisive strengthening is that the normalized minimal full-rank stack has **two independent binary row relations**, not merely one.

Statement (1.1) is a newly proved **lower-divisibility result**, not an upper bound for the mixed excess. It does not show that the payment $\frac{11}{4}d^2+O(d\log d)$ is attained. The first two aggregate digits at that nominal payment are now proved to be zero.

The new results of my turn 14 are used at their proved scope; this report does **not** label them DIFFERENT-reviewed.

---

## 2. Original objects and exact arithmetic interface

### 2.1 Domain and physical boundary

Throughout,


$$
\boxed{k=9^{18+32u},\quad u\ge0,\qquad d=k-1.}
\tag{2.1}
$$


Consequently,


$$
v_2(d)=4,\qquad d\equiv2\pmod3,\qquad d\equiv208\pmod{256}.
$$



The retained sequences are


$$
a_0=1,\qquad a_n=1-na_{n-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad
w_n=(-1)^n,\qquad c_n=u_n-w_n,
$$


and


$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad r_n=-f_n+4\rho_n.
$$



The complete returns are


$$
\sigma_n=u_{n+1}+u_n=c_{n+1}+c_n
$$


and


$$
\boxed{\tau_n=-(2n+2)!-(2n)!+\frac4{2n+1}.}
\tag{2.2}
$$



Set


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),\qquad
T_n=\Lambda_k\tau_n.
$$


Thus


$$
T_n=-\Lambda_k\bigl((2n+2)!+(2n)!\bigr)
+\frac{4\Lambda_k}{2n+1};
$$


neither factorial term is deleted.

Top-source rows satisfy $0\le n<d$. Original return orders satisfy $0\le r<d$. Residual row $i$, $0\le i\le d+1$, is original physical row $d+i$. The last physical row and terminal data remain


$$
\boxed{
2d+1=2k-1,\qquad
3d+1=3k-2,\qquad
(6k-4)!,\qquad 6k-5.
}
\tag{2.3}
$$



### 2.2 Actual clearers, contents, gcd, denominator, and whole error

The original affine determinant is


$$
H_k(s)=
\det\left[
(c_{m+j})\
\middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right]
=H_{0,k}+H_{1,k}s,
$$


where $0\le m<2k$, $0\le j<k$.

The individual least right-column entry clearers are


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3).
$$


Retain


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),\qquad
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


The least simultaneous coefficient clearer of $H_k/\Lambda_k^k$, and the content after that clearing, are exactly


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
}
\tag{2.4}
$$



The original rectangles are


$$
Z_k=
\left[
(c_{m+j})_{\substack{m<2k\\j<k}}
\ \middle|\
(T_{m+j})_{\substack{m<2k\\j<k-1}}
\right],
$$




$$
Y_k=
\left[
(\sigma_{m+j})_{\substack{m<2k-1\\j<k}}
\ \middle|\
(T_{m+j})_{\substack{m<2k-1\\j<k}}
\right].
$$


Their actual maximal-minor contents satisfy


$$
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k\mid \Lambda_k\mathscr L_k\mathscr R_k,
$$


where


$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
\mathscr L_k=\delta_{2k-1}(Y_k).
$$



The established sign and nonvanishing results retain


$$
q_k=\frac{|H_{1,k}|}{G_k}>0,\qquad
p_k=-\frac{(-1)^kH_{0,k}}{G_k},
$$


and


$$
\boxed{
0<\ell_k=q_k(e+\pi)-p_k
=\frac{|H_k(e+\pi)|}{G_k}.
}
\tag{2.5}
$$


All gcds here are all-prime gcds. No binary divisor or selected error summand replaces these quantities.

### 2.3 Complete forcing and corrected columns

Put


$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1),\qquad
\mathcal A_dy=\Delta^d(P_dy),
$$


with determinant payment


$$
\Omega_k=\prod_{n=0}^{d-1}P_d(n).
$$


The operator acts only on the first $d$ original rows.

For $b(t)=4t^2+6t+3$, the complete top forcing is


$$
F_k(n,j)=
-\Lambda_k\sum_{h=0}^d(-1)^h\binom dh
P_d(n+h)b(n+h+j)(2(n+h+j))!,
\quad n,j<d.
$$


The identity


$$
b(t)(2t)!=(2t+2)!+(2t)!
$$


shows explicitly that this is the full forcing.

Write


$$
F_k=-\Lambda_kD_fK_dD_f,\qquad
D_f=\operatorname{diag}((2n)!)_{n<d},
\qquad \eta_d^F=\det K_d.
$$


The oddness of all leading principal determinants of $K_d$ is established reuse.

Retain


$$
h_d=(2d-2)!,\qquad
\beta=v_2(h_d),\qquad
\alpha=v_2((2d)!)=\beta+5,
$$




$$
\widehat D_f=h_dD_f^{-1},\qquad
N_d=\widehat D_f\operatorname{adj}(K_d)\widehat D_f,
$$




$$
\delta_k=\Lambda_k\eta_d^Fh_d^2,\qquad
F_k^{-1}=-N_d/\delta_k,
$$


and


$$
f_k=(-\Lambda_k)^d\eta_d^F
\left(\prod_{n<d}(2n)!\right)^2.
$$



The bottom forcing is exactly


$$
R(i,j)=
\frac{\Lambda_k}{2(d+i+j)+1}
-\frac{\Lambda_k}{4}b(d+i+j)(2(d+i+j))!,
\quad i\le d+1,\ j<d.
\tag{2.6}
$$



Every Newton divisor remains


$$
D_r=2^rr!,\qquad
\mathfrak D_d=\prod_{r<d}D_r.
$$


Define


$$
\mathsf a_n=\frac{(\mathcal A_dc)_n}{2^d},
\qquad
t_n^{(r)}
=\frac{(\mathcal A_d\Delta^r\sigma)_n}
       {2^{\alpha+1}D_r}.
$$


Then


$$
x=RN_d\mathsf a+\frac{\delta_k}{2^{d+2}}c_{\rm bot},
$$




$$
z^{(r)}
=RN_dt^{(r)}
+\frac{\delta_k}{2^{\alpha+3}D_r}(\Delta^r\sigma)_{\rm bot},
$$


and, for $\psi_0=r,\ \psi_1=w$,


$$
\mathfrak b_h
=RN_d\Lambda_k(\mathcal A_d\psi_h)_{\rm top}
+\frac{\delta_k\Lambda_k}{4}(\psi_h)_{\rm bot}.
$$


Thus


$$
\mathcal Q_k(s)
=[x,z^{(0)},\ldots,z^{(d-1)},\mathfrak b_0+s\mathfrak b_1].
\tag{2.7}
$$



The useful exact decomposition is


$$
\mathcal Q_k(s)=RN_d\mathcal A_k(s)
+2^{L_d}\gamma_k\mathcal W_k(s),
\tag{2.8}
$$


where


$$
L_d=\alpha-12,\qquad M_d=\alpha-d+1,
$$




$$
\gamma_k=\frac{\delta_k}{2^{2\beta}}
=\Lambda_k\eta_d^F\operatorname{odd}(h_d)^2,
$$


and


$$
\mathcal W_k(s)=
\left[
2^{M_d}\frac{c_{\rm bot}}2,\
(\eta_r^{(d+i)})_{r<d},\
2^\alpha\Lambda_k(r+sw)_{\rm bot}
\right].
$$


Here


$$
\eta_r^{(m)}=\frac{\Delta^r\sigma_m}{2^{r+1}r!}.
$$



Also,


$$
R=R^{\rm C}-2^{\alpha-2}V,
$$




$$
R^{\rm C}(i,j)=\frac{\Lambda_k}{2(d+i+j)+1},
\qquad
V(i,j)=\frac{\Lambda_kb(d+i+j)(2(d+i+j))!}{2^\alpha}.
\tag{2.9}
$$


Both displayed matrices are integral on the original finite ranges.

### 2.4 Paid five-column interface

The selected common columns are


$$
S=[x,z^{(1)},z^{(0)},z^{(5)},z^{(4)}].
$$


The already evaluated pivot depths $5,19,39,72$, their actual odd quotients, and the exact payments are reused:


$$
|\mu_{3,k}|^{d-2}g_k^{[2]}
=2^{13}|\mu_{2,k}|^{d-1}g_k^{[3]},
$$




$$
|\mu_{4,k}|^{d-3}g_k^{[3]}
=2^{19}|\mu_{3,k}|^{d-2}g_k^{[4]},
$$




$$
|\mu_{5,k}|^{d-4}g_k^{[4]}
=2^{32}|\mu_{4,k}|^{d-3}g_k^{[5]}.
$$


In particular,


$$
\nu_k=64+\nu_k^{[5]}.
$$



With $\lambda_d^{\rm tr}=d\alpha+4d+4$,


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_{5,k}|^{d-4}G_k
=
|f_k|\,2^{\lambda_d^{\rm tr}+d+69}
\mathfrak D_d\,g_k^{[5]}.
}
\tag{2.10}
$$


No local calculation below changes this all-prime identity or asserts that any odd quotient equals the integer $1$.

---

## 3. Audit of the complete $P_5-P_{5,{\rm C}}$ perturbation

### 3.1 The actual changed pivot

Let $\Pi$ be the complete selected pivot on residual rows $0,\ldots,4$, and let $V_S$ be its selected-column block on the remaining residual rows. Thus


$$
\det\Pi=2^{72}\mu,\qquad
M=\frac{V_S\operatorname{adj}(\Pi)}{2^{72}},
$$


and


$$
\mathcal P_k^{[5]}=\frac{\mu C-MU}{2}.
$$



For an arbitrary original column label $a$, define


$$
B_a=R^{\rm C}N_dA_a,
$$


using its actual top source $A_a$, including the border sources. Let $\Pi^{\rm C}$ be the selected pivot formed from the $B$-columns. Then, exactly,


$$
\Pi-\Pi^{\rm C}
=
-2^{\alpha-2}V[0{:}4,:]N_dA_S
+2^{L_d}\gamma_k\mathcal W_S[0{:}4,:].
\tag{3.1}
$$


Thus the pivot itself changes.

The correct reference is


$$
\mathcal P^{[5],{\rm C}}_{k,a}(i)
=
\frac{\det[B_S,B_a][\{0,1,2,3,4,i\}]}{2^{73}},
\qquad 5\le i\le d+1.
\tag{3.2}
$$


The actual cofactor identity is


$$
\mathcal P^{[5]}_{k,a}(i)
=
\frac{\det[\mathcal C^{[5]},\mathcal Q_{k,a}]
[\{0,1,2,3,4,i\}]}{2^{73}}.
\tag{3.3}
$$


Indeed, the numerator is


$$
\det\Pi\,\mathcal Q_{k,a}(i)
-
V_S(i)\operatorname{adj}(\Pi)\mathcal Q_{k,a}[0{:}4]
=2^{72}(\mu C-MU).
$$



This normalization is essential. It is not a reference obtained by keeping the actual $\mu$ while replacing only an inverse.

If $\mu^{\rm C},M^{\rm C}$ denote the corresponding reference quantities, then the exact difference also has the form


$$
2(\mathcal P-\mathcal P^{\rm C})
=
(\mu-\mu^{\rm C})C^{\rm C}
-(M-M^{\rm C})U^{\rm C}
+\mu\,\Delta C-M\,\Delta U.
\tag{3.4}
$$


The first two terms are the pivot feedback. The six-column expansion below evaluates them together with the direct corrections.

### 3.2 Both complete border-source payments

Put


$$
B_h^{\rm top}=\Lambda_k(\mathcal A_d\psi_h)_{\rm top}.
$$


The claimed bounds are


$$
\boxed{
2^d\mid N_dB_1^{\rm top},\qquad
2^{d+1}\mid N_dB_0^{\rm top}.
}
\tag{3.5}
$$



For $w_n=(-1)^n$,


$$
\Delta^jw_n=(-2)^jw_n.
$$


In the product rule for $\Delta^d(P_dw)$, the polynomial difference contributes $2^h$ and the $w$-difference contributes $2^{d-h}$. Hence


$$
2^d\mid\Lambda_k\mathcal A_dw.
$$


Multiplication by the integral matrix $N_d$ proves the first bound.

For the constant border, retain


$$
r=-f+4\rho.
$$



Every entry of $\mathcal A_df$ in top row $n$ is an integer combination of factorials divisible by $(2n)!$. Therefore


$$
\widehat D_f\,\Lambda_k\mathcal A_df
$$


is divisible by the full integer $h_d$. Consequently,


$$
2^\beta\mid N_d\Lambda_k\mathcal A_df.
$$



For $g_n=(2n+1)^{-1}$, the recurrence is


$$
(\Delta+2)\rho=g,
$$


and


$$
\Delta^tg_n
=\frac{(-2)^tt!}{\prod_{a=0}^t(2n+2a+1)}.
$$


Since $\rho_n$ has odd denominator, induction from


$$
\Delta^t\rho=\Delta^{t-1}g-2\Delta^{t-1}\rho
$$


gives


$$
v_2(\Delta^t\rho_n)\ge t-1\qquad(t\ge1).
$$


Thus each term in $\Delta^d(P_d\,4\rho)$ with $h<d$ has depth at least


$$
h+(d-h-1)+2=d+1;
$$


the $h=d$ term has depth at least $d+2$.

A necessary bookkeeping clarification is that the displayed product denominator in $\Delta^tg_n$ need not itself divide $\Lambda_k$. Integrality after multiplication by $\Lambda_k$ follows from the **finite-difference sum of the original reciprocals**, all of whose denominators are in the retained range. No larger least-clearer claim is being made.

Finally,


$$
\beta=2d-s_2(d)-5\ge d+1
$$


on the original domain. This proves the second bound in (3.5), including the factorial part of $r$.

### 3.3 The two border differences

Every product-reference border, and every factorial-forcing version of it, retains the corresponding factor in (3.5). A direct bottom-border correction has the additional factor $2^\alpha$, and on bottom rows


$$
4\mid \Lambda_kr_m.
$$



Every term in the determinant difference contains at least one correction. Thus, before division by $2^{73}$, the linear-border difference has depth at least $L_d+d$, and the constant-border difference has depth at least $L_d+d+1$. Therefore


$$
\boxed{
v_2(\mathcal P_{\mathfrak b_1}-\mathcal P_{\mathfrak b_1}^{\rm C})
\ge L_d+d-73,
}
\tag{3.6}
$$




$$
\boxed{
v_2(\mathcal P_{\mathfrak b_0}-\mathcal P_{\mathfrak b_0}^{\rm C})
\ge L_d+d+1-73.
}
\tag{3.7}
$$


Both are strictly above $L_d+7$.

These same entrywise payments also prove reference-border integrality. Reference-return integrality follows from the established pure six-column payments.

### 3.4 Exhaustion of the return-column correction patterns

The target before division by $2^{73}$ is the coefficient at depth $L_d+80$, so terms of depth at least $L_d+81$ are invisible.

Let $h$ count bottom corrections and $v$ count factorial-forcing corrections. All of the following are invisible:

| Pattern | Sufficient raw payment |
|---|---:|
| $h\ge2$ | $2L_d$ |
| $h\ge1,\ v\ge1$ | $2L_d+10$ |
| $h=0,\ v\ge2$ | $2L_d+20$ |
| one atom bottom correction | $L_d+M_d$ |
| one factorial correction, no bottom correction | $(L_d+10)+c_5+2E_6+B_6$ |

Here


$$
c_5=30,\quad 2E_6=46,\quad B_6=20,
$$


so the last line is $L_d+106$. All inequalities have large slack on the original domain.

The only surviving class is therefore:

> one weighted-return bottom correction, five pure-Cauchy product columns, and the atom in the product.

This exhausts the correction expansion; no direct-$W$ shortcut is used.

### 3.5 Unique minimal forcing/source minor and normalization

Define


$$
e_n=v_2\!\left(\frac{h_d}{(2n)!}\right),\qquad
E_p=\sum_{n=d-p}^{d-1}e_n,
\qquad
\mathcal T_p=\{d-p,\ldots,d-1\}.
$$


Since


$$
e_n-e_{n+1}=1+v_2(n+1)>0,
$$


the unique index pair attaining the minimum $2E_p$ is


$$
I=J=\mathcal T_p.
$$



For this pair, Jacobi’s identity gives


$$
\det N_d[\mathcal T_p,\mathcal T_p]
=
\left(\prod_{j\in\mathcal T_p}\frac{h_d}{(2j)!}\right)^2
(\eta_d^F)^{p-1}
\det K_d[0{:}d-p-1,0{:}d-p-1].
\tag{3.8}
$$


The final two factors are odd. Thus the minimum is attained, not merely bounded below.

For $p=5$, the three payments are


$$
B_5=12,\qquad 2E_5=30,\qquad
c_5+\lambda_5=30+8=38,
$$


where


$$
\lambda_j=j+v_2(j!).
$$


Their sum is


$$
12+30+38=80.
$$


The bottom scalar $2^{L_d}\gamma_k$, followed by the actual division $2^{73}$, gives precisely $L_d+7$.

All remaining factors—$\Lambda_k^5$, odd factorial parts, the odd part of (3.8), the odd source factor, and the odd Cauchy denominators—are retained before reduction. Each reduces to $1$ in $\mathbb F_2$; none is being identified with the integer $1$.

### 3.6 Evaluation of the feedback functional

The contact parity is


$$
\eta_n=\operatorname{Tr}\bigl(\omega^{n+2}+(n+1)\omega^n\bigr),
\qquad \omega^2+\omega+1=0.
$$


Its period-six values are


$$
(\eta_0,\ldots,\eta_5)=(1,0,0,1,1,1).
$$



For the first mixed row at $p=5$, Lucas reduction gives


$$
S_5(r)
=\sum_{t\in\{0,1,4,5\}}
\binom{r+t}{t}\eta_{r+t},
$$


and hence


$$
S_5(r)=
\begin{cases}
\operatorname{Tr}(\omega^{r+1}),&r\mathbin{\&}4=0,\\
\operatorname{Tr}(\omega^{r+2}),&r\mathbin{\&}4\ne0.
\end{cases}
\tag{3.9}
$$



The complete one-correction Laplace sum is the determinant of


$$
U_d(0),\ U_d(1),\ U_d(2),\ U_d(3),\ S_5
$$


on the return columns


$$
(1,0,5,4,r).
$$


The previously established four-column source unit is reused, not recomputed.

On the selected four returns,


$$
S_5=U_d(0)=(1,1,1,0).
$$


Adding $U_d(0)$ to the last row therefore leaves only the final entry


$$
S_5(r)+U_d(0,r).
$$


The audited original-source law gives


$$
U_d(0,r)=\eta_{r+2d+(r\mathbin{\&}d)}.
$$


Thus the complete functional is


$$
\boxed{
\kappa_d(r)=S_5(r)+\eta_{r+2d+(r\mathbin{\&}d)}.
}
\tag{3.10}
$$



For the residual row set $M_i=\{0,1,2,3,4,i\}$,


$$
\frac{V(M_i)}{\Phi_6}=\binom i5.
$$


Consequently,


$$
\boxed{
\mathcal P^{[5]}_{k,r}(i)-\mathcal P^{[5],{\rm C}}_{k,r}(i)
\equiv
2^{L_d+7}\gamma_k\binom i5\kappa_d(r)
\pmod{2^{L_d+8}}.
}
\tag{3.11}
$$



Because the low four bits of $d$ vanish,


$$
S_5(2)=0,\quad U_d(0,2)=1,\qquad
S_5(3)=1,\quad U_d(0,3)=0.
$$


Therefore


$$
\kappa_d(2)=\kappa_d(3)=1.
$$


At $i=5$, the row factor is $1$, proving exact difference depth $L_d+7$.

**Audit verdict: PASS.** The normalized complete difference has rank exactly one, with both border factors zero. It is not a valuation of a whole residual entry or a terminal coefficient.

---

## 4. Audit of the full mixed kernel

### 4.1 Integer normalization precedes parity

For an actual Cauchy forcing set $I$ of size $p$, put


$$
Q_I(i)=\prod_{b\in I}(2(d+i+b)+1).
$$


For $W_r(i)=\eta_r^{(d+i)}$, the full finite product rule gives


$$
2^jj!\mid \Delta^j(Q_IW_r)(i).
$$


Indeed,


$$
\frac{\Delta^tQ_I(i)}{2^tt!}\equiv\binom pt\pmod2,
$$


because $Q_I$ is a polynomial in $2i$ with odd constant factors. Also,


$$
\frac{\Delta^sW_r(i)}{2^ss!}
=\binom{r+s}{r}\eta_{r+s}^{(d+i)}.
$$



Therefore


$$
\frac{\Delta^j(Q_IW_r)(0)}{2^jj!}
\equiv
\sum_{t=0}^{\min(p,j)}
\binom pt\binom{r+j-t}{r}\eta_{r+j-t}.
$$


For $j=p+z$, this becomes


$$
\boxed{
U_p(z,r)=
\sum_{t=0}^p\binom pt\binom{r+z+t}{r}\eta_{r+z+t}.
}
\tag{4.1}
$$



The independence from the pole choices occurs only at this normalized parity precision. The actual $Q_I$, its odd factors, and the full divisions remain in the integer calculation.

The physical condition is


$$
p+z\le d+1
$$


at bottom starting row $i=0$, or $i+p+z\le d+1$ after a shift. These are the bounds used below.

### 4.2 Derivation of the odd derivative term

Write


$$
a=1+\omega Y,\qquad b=1+\omega^2Y,\qquad S=X+Y,
$$




$$
B_p(Y)=\left(\frac{\omega^2+\omega Y}{1+\omega Y}\right)^p
=\omega^{2p}\frac{b^p}{a^p}.
$$


The binomial generating identity gives


$$
H_p(X,Y)=\frac{B_p(Y)}{1+\omega S}.
$$



The factor $z+r+t+1$ in $\eta_{z+r+t}$ requires both the $X,Y$ Euler derivative and the derivative in the binomial-filter index. With $\varepsilon=p\bmod2$,


$$
YB_p'(Y)=
\varepsilon\,\frac{\omega^2YB_{p-1}}{a^2},
$$


and the filter-index contribution is


$$
\varepsilon\,\frac{\omega B_{p-1}}{a(1+\omega S)}.
$$


Combining them yields


$$
YB_p'+\varepsilon\frac{\omega B_{p-1}}a
=
\varepsilon\frac{\omega B_{p-1}}{a^2}.
$$



Thus the complete kernel is


$$
\boxed{
\sum_{z,r\ge0}U_p(z,r)X^zY^r
=
\operatorname{Tr}\left[
B_p(Y)\frac{\omega+S}{(1+\omega S)^2}
+
\varepsilon\frac{\omega B_{p-1}(Y)}
{a^2(1+\omega S)}
\right].
}
\tag{4.2}
$$


When $p=0$, the second term is zero and $B_{-1}$ is not used.

Dropping the second term at odd $p$ is invalid. For example, at $p=1,z=r=0$, the direct value is
$\eta_0+\eta_1=1$, whereas the first term alone has trace zero.

### 4.3 All higher rows at both parities

Expanding


$$
(1+\omega(X+Y))^{-2}
=(a+\omega X)^{-2}
=\sum_{v\ge0}\frac{\omega^{2v}X^{2v}}{a^{2v+2}}
$$


gives, for even $p$,


$$
\boxed{
\begin{aligned}
U_p(2v,Y)
&=\operatorname{Tr}\left(
\omega^{2p+2v+1}\frac{b^{p+1}}{a^{p+2v+2}}
\right),\\
U_p(2v+1,Y)
&=\operatorname{Tr}\left(
\omega^{2p+2v}\frac{b^p}{a^{p+2v+2}}
\right).
\end{aligned}}
\tag{4.3}
$$



For odd $p$, the even coefficient combines the two terms of (4.2) using


$$
\omega^2b^2+1=\omega a^2,
$$


and the odd coefficient uses


$$
ab+1=Y(1+Y).
$$


The result is


$$
\boxed{
\begin{aligned}
U_p(2v,Y)
&=\operatorname{Tr}\left(
\omega^{2p+2v}\frac{b^{p-1}}{a^{p+2v}}
\right),\\
U_p(2v+1,Y)
&=\operatorname{Tr}\left(
\omega^{2p+2v}
\frac{b^{p-1}Y(1+Y)}{a^{p+2v+3}}
\right).
\end{aligned}}
\tag{4.4}
$$


Every denominator has unit constant term.

Finally, Pascal’s identity applied directly to (4.1) gives


$$
\boxed{U_{p+1}(z,r)=U_p(z,r)+U_p(z+1,r)\pmod2.}
\tag{4.5}
$$


This derivation is independent of the generating-function simplifications and works at both parities.

**Audit verdict: PASS.**

---

## 5. Audit of the coupled rank for arbitrary mixed combinations

To distinguish the dyadic remainder from the sequence $\rho_n$, write


$$
d=2L+\varrho.
$$


Assume


$$
\boxed{
L\ \text{dyadic},\quad
\varrho\ge4\ \text{even},\quad
p\ge\varrho+1,\quad
\varrho+p\le L,\quad
1\le h\le\varrho-1.
}
\tag{5.1}
$$


All return columns in this section are the original columns $0\le r<2L\le d$.

### 5.1 The actual atom-source spaces

Let $U_j=U_d(j,\bullet)$. The paid minimizing atom-source row lists are


$$
R_q=
\begin{cases}
(U_0,\ldots,U_{q-2}),&q\text{ odd},\\
(U_0,\ldots,U_{q-3},U_{q-2}+U_{q-1}),&q\text{ even}.
\end{cases}
\tag{5.2}
$$



These are not arbitrary choices. If


$$
R_j^\uparrow=(d+1)_j,\qquad
\mathcal B_q(d)=2^{\binom q2}\prod_{j=0}^{q-2}R_j^\uparrow,
$$


the exact source atom expansion on $\mathcal T_q$ is


$$
\frac{\det A_S[\mathcal T_q]}{\mathcal B_q(d)}
=
\sum_{j=0}^{q-1}
(\pm)\,
\frac{\Delta^j\mathsf a_{d-q}}{2^j}
\frac{R_{q-1}^\uparrow}{R_j^\uparrow}
\det U^{\mathbb Z}[\{0,\ldots,q-1\}\setminus\{j\},S_{\rm ret}].
\tag{5.3}
$$


At odd $q$, only the last atom position survives parity. At even $q$, the last two survive and add. Thus both atom positions at even sizes have been paid.

The passed rectangular theorem supplies


$$
\dim R_{p+1}=p,\qquad \dim R_p=p-1.
$$


For odd $p$, the required first $p+1$ contact rows are available because
$\varrho+p$ is odd and $L$ is even:


$$
\varrho+p\le L\quad\Longrightarrow\quad
\varrho+p+1\le L.
\tag{5.4}
$$



### 5.2 Both unit denominators and the finite root candidate

Apply the same finite binary column convolution


$$
C_d(Y)=(ab)^d.
$$


It is unit triangular on the first $2L$ parity columns, and


$$
a^{2L}\equiv b^{2L}\equiv1\pmod{Y^{2L}}.
$$


This is a parity-rank operation only.

The even-$d$ top rows satisfy


$$
C_dU_d(2l)
=\operatorname{Tr}\left(
\omega^{2d+2l+1}\frac{b^{2d+1}}{a^{2l+2}}
\right),
$$




$$
C_dU_d(2l+1)
=\operatorname{Tr}\left(
\omega^{2d+2l}\frac{b^{2d}}{a^{2l+2}}
\right).
$$


A source vector in $R_{p+1}$ therefore has the form


$$
\operatorname{Tr}\left(\frac{b^{2\varrho}Q}{a^p}\right),
\qquad \deg Q\le p-1.
\tag{5.5}
$$



Put $V_z=U_p(z,\bullet)$. Equations (4.3)–(4.4), after the same convolution, give the candidate numerators:

For odd $p$,


$$
Q_{2v}=\omega^{2p+2v}a^{\varrho-2v}b^{p-\varrho-1},
$$




$$
Q_{2v+1}=\omega^{2p+2v}
a^{\varrho-2v-3}b^{p-\varrho-1}Y(1+Y).
\tag{5.6}
$$



For even $p$,


$$
Q_{2v}=\omega^{2p+2v+1}
a^{\varrho-2v-2}b^{p-\varrho+1},
$$




$$
Q_{2v+1}=\omega^{2p+2v}
a^{\varrho-2v-2}b^{p-\varrho}.
\tag{5.7}
$$



Under (5.1), every displayed exponent is nonnegative and every candidate has degree at most $p-1$.

Suppose an arbitrary binary combination $Q_{\rm mix}$ of these candidates belongs to the source space. Clearing **both** unit denominators gives


$$
b^pN+a^pN^\sigma\equiv0\pmod{Y^{2L}},
\qquad
N=b^{2\varrho}(Q+Q_{\rm mix}).
\tag{5.8}
$$


Its degree is at most


$$
2\varrho+2p-1\le2L-1.
$$


Hence (5.8) is an exact polynomial identity.

At the root of $a$, the polynomial $b$ is a unit. Therefore


$$
a^p\mid Q+Q_{\rm mix}.
$$


Since $\deg(Q+Q_{\rm mix})<p$, the only possible source numerator is


$$
\boxed{Q=Q_{\rm mix}.}
\tag{5.9}
$$



This reduction handles arbitrary mixed combinations, not just one-row nonmembership.

### 5.3 Odd $p$: two coefficient obstructions for each pair

Write $p=2m_c+1$. The source numerator is


$$
Q=aQ_{\rm old}+c_{\rm new}\omega^{2d+p+1},
\qquad c_{\rm new}\in\mathbb F_2,
$$


where


$$
Q_{\rm old}
=
\omega^{2d}\sum_{l=0}^{m_c-1}
\omega^{2l}
(c_{{\rm odd},l}+c_{{\rm even},l}\omega b)
a^{2(m_c-l-1)}.
\tag{5.10}
$$


Every candidate in (5.6) is divisible by $a$, so evaluation at the root of $a$ forces $c_{\rm new}=0$.

Put


$$
A=a^2,\qquad b^2=\omega(1+\omega A),\qquad
t=\frac{p-\varrho-1}{2}.
$$


After division by $a$, pair the even candidate $z=2v$ with the preceding odd candidate $z=2v-1$. With


$$
s=\varrho/2-v-1,
$$


they are


$$
E_v=\omega^{2p+2v+t}aA^s(1+\omega A)^t,
$$




$$
O_{v-1}=\omega^{2p+2v-2+t}
A^s(1+\omega A)^tY(1+Y).
$$



Their $YA^s$-coefficients are equal. The permitted source coefficient at
$l=t+v$ is $\omega^{2d+2l}c_{{\rm even},l}$. The ratio is


$$
\omega^{2p+1-2d-t}
=\omega^{\varrho/2-2d}
=\omega^{-L}\notin\mathbb F_2.
\tag{5.11}
$$


Thus exactly one nonzero member of the pair is impossible.

If both occur, their $Y$-terms cancel, but


$$
a+\omega Y(1+Y)=b^2
$$


gives


$$
E_v+O_{v-1}
=
\omega^{2p+2v+t+1}A^s(1+\omega A)^{t+1}.
$$


Its $A^s$-coefficient has the same forbidden ratio (5.11). Since the $Y$-coefficient is zero, the corresponding even-source coefficient must be zero; the remaining constant coefficient would require a nonbinary odd-source coefficient.

For an arbitrary nonzero combination, choose its lowest $A$-degree. Only the indicated pair, or the isolated $z=0$ row, can contribute there. Higher-$A$-degree candidates cannot repair either coefficient obstruction.

The decomposition


$$
Q(Y)=Q_{\rm even}(A)+YQ_{\rm odd}(A)
$$


is unique, so this is an exact polynomial-basis argument.

### 5.4 Even $p$

Write $p=2m_c$. Now the full source space is


$$
Q=
\omega^{2d}\sum_{l=0}^{m_c-1}
\omega^{2l}
(c_{{\rm odd},l}+c_{{\rm even},l}\omega b)
a^{p-2l-2}.
\tag{5.12}
$$


Set


$$
t=\frac{p-\varrho}{2},\qquad
s=\varrho/2-v-1.
$$


The candidates are


$$
E_v=\omega^{2p+2v+1+t}bA^s(1+\omega A)^t,
$$




$$
O_v=\omega^{2p+2v+t}A^s(1+\omega A)^t.
$$



Only $E_v$ has a $YA^s$-coefficient. Relative to the permitted source phase at $l=t+v$, its ratio is


$$
\omega^{2p-2d-t}
=\omega^{-L}\notin\mathbb F_2.
$$


Thus its coefficient must vanish. With $E_v$ absent, $O_v$ has the same forbidden ratio in its $A^s$-coefficient. Choosing the lowest $A$-degree again excludes every nonzero mixed combination.

All indicated source indices lie in $0,\ldots,m_c-1$.

### 5.5 Rank verdict

The preceding argument proves that the $h$ mixed rows are independent modulo the larger source space. Therefore


$$
\boxed{
\operatorname{rank}[R_{p+1};V_0;\ldots;V_{h-1}]=p+h,
\qquad 1\le h\le\varrho-1.
}
\tag{5.13}
$$



**Audit verdict: PASS**, including the finite cutoff, both denominators, the unique candidate, both parities, and arbitrary binary combinations.

---

## 6. Complete leading-sector payments and all equality ties

### 6.1 Exact costs and minimizer

Define


$$
\lambda_j=j+v_2(j!),\qquad
S_n=\sum_{j=0}^{n-1}\lambda_j,
$$




$$
B_p=\binom p2+\sum_{j=0}^{p-2}v_2((d+1)_j),
\qquad
T_p=S_p+2E_p+B_p,
$$


with $S_0=T_0=B_0=E_0=0$.

Since $c_p=2S_p$, the no-factorial, atom-in-product payment for a $q$-minor is


$$
\boxed{
F_q(p)=(q-p)L_d+S_p+S_q+2E_p+B_p
=qL_d+S_q+T_p-pL_d.
}
\tag{6.1}
$$



For $p\ge2$,


$$
D_p:=T_p-T_{p-1}
=
8p-9+s_2(d)-2s_2(d-1)+2s_2(d-p)
-s_2(p-1)-s_2(d+p-2).
\tag{6.2}
$$


Moreover,


$$
\boxed{
D_{p+1}-D_p
=
1+v_2(p)+2(1+v_2(d-p))+1+v_2(d+p-1)\ge4.
}
\tag{6.3}
$$


Thus the minimizer is unique except for a possible adjacent tie.

Let


$$
s=\min\{r\ge2:D_r\ge L_d\},\qquad p=s-1.
$$


Then


$$
D_p<L_d\le D_{p+1},
\qquad p=d/4+O(\log d).
\tag{6.4}
$$



The mathematical minimizer statement passes. A minor complexity qualification is appropriate: binary search uses $O(\log d)$ evaluations and comparisons of the digit expression. Literal elementary bit complexity also includes the cost of those evaluations; an $O(\log d)$ total bit-operation claim would require an additional computational model assumption.

### 6.2 Exclusion of the other correction patterns

For $v>0$ factorial corrections, let $a=p-v$. The complete lower payment is


$$
(q-p)L_d+v(\alpha-2)+S_a+S_{a+q-p}+2E_p+B_p.
$$


Its difference from $F_q(p)$ is at least


$$
v(\alpha-2-4q).
$$



If the atom is a bottom correction, its full factor $2^{M_d}$, the all-return source payment, and the missing weighted-return jet give an additional lower payment of at least


$$
d-2q+1-2m_d,
\qquad m_d=1+\lfloor\log_2d\rfloor.
$$


This includes the all-bottom case $p=0$. The formal $p=0$ cost exceeds $F_q(1)$ by $L_d>0$.

Hence, under


$$
\boxed{
q\le d,\qquad
\alpha-2>4q,\qquad
d-2q+1-2m_d>0,
}
\tag{6.5}
$$


the only minimizing product count is $p$ at a strict crossing, or the two counts $p,p+1$ at equality.

### 6.3 Every leading-sector scalar

Here is an explicit relative normalization, rather than an appeal to source and bottom rank alone.

Use the first $q$ residual rows and the minimal forcing/source pair
$\mathcal T_b,\mathcal T_b$ in a sector with $b$ product columns. Let


$$
Q_{\mathcal T_b}(i)
=\prod_{j\in\mathcal T_b}(2(d+i+j)+1).
$$


After the exact Cauchy identity, finite Newton transformation, and full source normalization, the scalar outside the normalized stacked matrix is


$$
2^{F_q(b)}\Xi_{q,b},
$$


where


$$
\boxed{
\begin{aligned}
\Xi_{q,b}
={}&\gamma_k^{q-b}
\frac{\Lambda_k^b\operatorname{odd}(\Phi_b)^2}
{\prod_{i=0}^{q-1}Q_{\mathcal T_b}(i)}
\frac{\det N_d[\mathcal T_b,\mathcal T_b]}{2^{2E_b}}\\
&\times
\frac{\mathcal B_b(d)}{2^{B_b}}
\prod_{j=b}^{q-1}\operatorname{odd}(j!).
\end{aligned}}
\tag{6.6}
$$


The exact atom coefficients remain inside the normalized source rows:


$$
\frac{R_{b-1}^\uparrow}{R_j^\uparrow}
\frac{\Delta^j\mathsf a_{d-b}}{2^j}.
\tag{6.7}
$$



Every factor in (6.6) is an explicitly retained odd unit in $\mathbb Z_{(2)}$. In particular:

- the Cauchy row denominators are not dropped;
- the complementary $K_d$-determinant is retained through the actual $N_d$-minor;
- $\gamma_k$ is retained in full;
- every odd factorial part is retained;
- the odd atom multipliers in (6.7) are retained before parity;
- both tied atom positions at even $b$ reduce to coefficient $1$.

Thus


$$
\Xi_{q,b}\equiv1\pmod2.
$$


This is exactly the relative-unit information required at binary leading precision.

For the first $q$ residual rows, the finite Newton matrix is unit triangular. The Cauchy polynomial columns force orders $0,\ldots,b-1$; the remaining orders are exactly $b,\ldots,q-1$. The minimal $N_d$-pair is unique. Every other $N_d$-pair costs an additional power of two. The strict conditions (6.5) exclude all factorial and atom-in-bottom competitors.

Therefore the complete leading $b$-sector—not just one bottom determinant—is the indicated Laplace stack.

### 6.4 Strict crossing

Let $q=p+h$ and $V_z=U_p(z)$. At a strict crossing,


$$
D_{p+1}>L_d,
$$


the complete leading contribution is


$$
\det[R_p;V_0;\ldots;V_{h-1}].
\tag{6.8}
$$


Equation (5.13) proves that this has row rank $q-1$. Some $q-1$ original coordinate columns therefore give an odd determinant, and the associated complete common-column minor has exact valuation


$$
\boxed{F_q(p).}
\tag{6.9}
$$



### 6.5 Equality tie

At


$$
D_{p+1}=L_d,
$$


the two and only two minimum counts are $p,p+1$.

Choose


$$
v_{\rm new}=
\begin{cases}
U_d(p-1)+U_d(p),&p\text{ odd},\\
U_d(p-1),&p\text{ even}.
\end{cases}
$$


Then $R_{p+1}$ is obtained from $[R_p;v_{\rm new}]$ by a binary determinant-one basis change.

By (4.5), the bottom rows in the $p+1$-sector are


$$
W'_z=V_z+V_{z+1},\qquad 0\le z<h-1.
$$


The determinant-one change


$$
(V_0,\ldots,V_{h-1})
\longmapsto
(V_{h-1},W'_0,\ldots,W'_{h-2})
$$


and the relative scalar calculation (6.6) show that the sum of the two complete minimum sectors is


$$
\boxed{
\det[R_p;\
v_{\rm new}+V_{h-1};\
W'_0;\ldots;W'_{h-2}].
}
\tag{6.10}
$$



This is a sum of the two sectors, not the determinant of either sector in isolation.

Equation (5.13) implies


$$
v_{\rm new}\notin
\operatorname{span}(R_p,V_0,\ldots,V_{h-1}).
$$


Hence the rows in (6.10) are independent: a relation with a nonzero coefficient of $v_{\rm new}+V_{h-1}$ contradicts that exclusion, and a relation without it contradicts independence of the $V$-rows modulo $R_p$.

Thus some original columns attain the tied depth


$$
\boxed{F_q(p)=F_q(p+1).}
\tag{6.11}
$$



**Audit verdict: PASS**, including complete relative normalization and cancellation between the tied sectors.

### 6.6 The same infinite original interval

Let


$$
a_k=\lfloor\log_2k\rfloor,\qquad L=2^{a_k-1},
$$


and retain the interval


$$
\boxed{
\frac98\,2^{a_k}<k<\frac76\,2^{a_k}.
}
\tag{6.12}
$$


Then


$$
d=2L+\varrho,\qquad
L/4-1<\varrho<L/3-1.
$$


At original indices, $\varrho$ is divisible by $16$.

The digit formula gives $p=d/4+O(m_d)$. Therefore


$$
p-\varrho=L/2-3\varrho/4+O(m_d)>0,
$$


and


$$
L-\varrho-p=L/2-5\varrho/4+O(m_d)>0,
$$


with linear slack. For every $h\le\varrho-1$,


$$
q=p+h\le p+\varrho-1<d/2
$$


with linear slack, proving (6.5). For example, the elementary sufficient bound
$L>128(m_d+4)$ is far weaker than the sizes in the original domain.

All selected returns satisfy $r<2L\le d$. The largest used mixed Newton order is $q-1$, within the original residual boundary.

The fractional parts of


$$
(18+32u)\log_2 9
$$


form an irrational rotation, since unique factorization proves
$\log_2 9\notin\mathbb Q$. Every tail is dense, so (6.12) contains infinitely many original indices.

No parity or equality-distribution assumption is needed. The conclusion is cofactor existence at each


$$
p+1\le q\le p+\varrho-1,
$$


not a nested complete elimination flag beyond the already proved window.

---

## 7. The exact coefficient pair retained from turn 14

Define the complete finite map


$$
\mathscr T(y)
=RN_d(\mathcal A_dy)_{\rm top}
+\frac{\delta_k}{4}y_{\rm bot}.
$$


It annihilates every original forcing column:


$$
\mathscr T(T_j)=0,\qquad j<d.
$$



The finite identity


$$
y=\frac12\sum_{r=0}^{d-1}
\left(-\frac{\Delta}{2}\right)^r(\Delta+2)y
+2^{-d}\Delta^dy
$$


therefore gives


$$
\boxed{\mathfrak b_0=\Lambda_k2^{-d}\mathscr T(\Delta^dr).}
\tag{7.1}
$$


The right side still contains both $-\Delta^df$ and $4\Delta^d\rho$.

Put


$$
\theta_r^{(m)}=\frac{\Delta^ru_m}{2^rr!},
$$




$$
v^{(r)}=\frac{\mathscr T(\Delta^ru)}{2^\alpha D_r},
\quad 0\le r\le d,
\qquad
w_*=\frac{\mathscr T(w)}{2^d}.
$$


The full rising-factor product rule, with $\eta$ replaced by $\theta$, proves integrality, including the full new divisor


$$
D_d=2^dd!.
$$


The order-$d$ column is a re-expression of the existing terminal border, not a new original return.

Exactly,


$$
z^{(r)}=v^{(r)}+(r+1)v^{(r+1)},\qquad
x=2^{\alpha-d}v^{(0)}-w_*.
$$


Let


$$
a_r=(-1)^{d-r}\frac{d!}{r!},\qquad
\varkappa_d=2^{\alpha-d}d!,\qquad
\mathfrak c_k=\Lambda_k2^\alpha d!.
$$


The determinant-one finite transformation gives


$$
\widehat{\mathcal Q}_k(s)=
\left[
\varkappa_dv^{(d)}-w_*,
\ (v^{(r)}-a_rv^{(d)})_{r<d},
\ \mathfrak b_0+s\mathfrak c_kv^{(d)}
\right].
\tag{7.2}
$$



Writing $\det\mathcal Q_k(s)=I_{0,k}+I_{1,k}s$, both exact coefficient identities are retained:


$$
\boxed{
I_{1,k}
=-\mathfrak c_k
\det[w_*,v^{(0)},\ldots,v^{(d)}],
}
\tag{7.3}
$$


and


$$
\boxed{
\begin{aligned}
I_{0,k}
={}&
\varkappa_d\det[v^{(0)},\ldots,v^{(d)},\mathfrak b_0]\\
&-\sum_{r=0}^d\frac{d!}{r!}
\det[w_*,v^{(0)},\ldots,\widehat{v^{(r)}},
\ldots,v^{(d)},\mathfrak b_0].
\end{aligned}}
\tag{7.4}
$$



The physical maximum remains


$$
(2d+1)+d=3d+1=3k-2.
$$


No factorial beyond the original terminal is introduced.

These are the turn-14 identities (7.11)–(7.12), retained without changing their proof-review status.

---

## 8. New full-rank result: the next aggregate digit is zero

### 8.1 Exact full-rank normalization

Set


$$
n=d+2,\qquad A_d=v_2(d!)=\alpha-d.
$$


The determinant in (7.3) has the exact decomposition


$$
[w_*,v^{(0)},\ldots,v^{(d)}]
=
RN_d[\mathsf a_w,\mathsf v^{(0)},\ldots,\mathsf v^{(d)}]
+2^{L_d}\gamma_k[2^{A_d}w,\theta_0,\ldots,\theta_d],
\tag{8.1}
$$


where


$$
\mathsf a_w=\frac{\mathcal A_dw}{2^d},
\qquad
\mathsf v^{(r)}
=\frac{\mathcal A_d\Delta^ru}{2^\alpha D_r}.
$$



The source payment for an atom-containing $p$-minor remains $B_p$. Define


$$
\boxed{
\mathcal L_p
=(n-p)L_d+S_p+S_n+2E_p+B_p
=nL_d+S_n+T_p-pL_d.
}
\tag{8.2}
$$


Also define the formal all-bottom payment


$$
\mathcal L_0=nL_d+S_n.
$$


Since $T_1=0$,


$$
\mathcal L_0-\mathcal L_1=L_d>0.
$$



The same strictly increasing $D_p$ determines the minimum


$$
\mathfrak m_d=\min_{1\le p\le d}\mathcal L_p.
$$


Every minimizing count, and every count with
$\mathcal L_p\le\mathfrak m_d+1$, lies in


$$
\left|p-\frac d4\right|\le m_d+3.
\tag{8.3}
$$


In particular, these counts lie in $5\le p\le d/3$ on the original domain.

### 8.2 A global exclusion of factorial-forcing competitors

This step is needed because a result only about the minimizing no-factorial strip would not yet evaluate a whole determinant digit.

For an actual forcing column $j$, define


$$
g_j=v_2((2(d+j))!)-\alpha.
$$


Every entry in column $j$ of $V$ is divisible by $2^{g_j}$, and


$$
e_j+g_j
=2d+s_2(j)-s_2(d+j)-5
\ge 2d-m_d-6.
\tag{8.4}
$$


Write


$$
C_d^{\rm fac}=2d-m_d-6.
$$



Consider a full-rank term with:

- $p$ product columns;
- $v\ge1$ factorial-forcing columns;
- $a=p-v$ Cauchy columns;
- $h=n-p$ bottom columns.

The factorial diagonal and the column payments (8.4) give at least


$$
E_p+E_a+vC_d^{\rm fac}.
$$



Every bottom $\theta$-column has the full $2^jj!$ jet divisor. The bottom atom $2^{A_d}w$ has the same binary payment through order $n-1=d+1$: its $w$-jet provides $2^j$, and


$$
v_2(j!)\le v_2((d+1)!)=A_d.
$$


Odd factorial denominators are retained in $\mathbb Z_{(2)}$; no new integer-pencil division is asserted.

The multiple-return argument therefore gives the lower payment


$$
\mathcal F(p,v)
=
(n-p)L_d+v(\alpha-2+C_d^{\rm fac})
+E_p+E_a+B_p+S_a+S_{n-v}.
\tag{8.5}
$$



Compare this with $\mathcal L_a$. Since $\alpha-2-L_d=10$,


$$
\mathcal F(p,v)-\mathcal L_a
=
v(10+C_d^{\rm fac})
+(E_p-E_a)+(B_p-B_a)
-(S_n-S_{n-v}).
\tag{8.6}
$$


The elementary marginal bounds give


$$
E_p-E_a\ge v(2a+v-1-m_d),
$$




$$
B_p-B_a\ge v(2a+v-m_d-2),
$$


and


$$
S_n-S_{n-v}\le v(2d+3-v).
$$


Hence


$$
\boxed{
\mathcal F(p,v)\ge
\mathcal L_a+
v(4a+3v-3m_d-2).
}
\tag{8.7}
$$



If $p=a+v\ge m_d+2$, then


$$
4a+3v-3m_d-2\ge3p-3m_d-2\ge4,
$$


so


$$
\mathcal F(p,v)\ge\mathfrak m_d+4.
$$



For $p\le m_d+1$, the exact digit formula gives


$$
D_{m_d+2}\le11m_d+7,
$$


and therefore, for $a\le m_d+1$,


$$
\mathcal L_a-\mathfrak m_d
\ge L_d-D_{m_d+2}
\ge2d-12m_d-19.
$$


Even allowing the negative part of (8.7),


$$
\mathcal F(p,v)-\mathfrak m_d
\ge
2d-3m_d^2-17m_d-21>4
$$


on the original domain.

Thus:


$$
\boxed{\text{Every factorial-forcing term has depth at least }
\mathfrak m_d+4.}
\tag{8.8}
$$


This is a global statement over all product counts, not an entrywise deletion of $V$.

### 8.3 Atom-in-bottom competitors

Without a factorial-forcing correction, an atom-in-bottom term has all-return top sources. Its source payment exceeds $B_p$ by


$$
v_2((d+1)_{p-1}).
$$


For $p\ge5$, this is at least $3$, because the rising product contains $d+2$ and $d+4$, of valuations $1$ and $2$.

The factor $2^{A_d}$ pays the bottom atom’s missing factorial-jet valuation as above. Hence these terms have depth at least


$$
\mathcal L_p+3\ge\mathfrak m_d+3.
$$


For $p\le4$, including $p=0$, the cost is separated from the minimum by the large small-$p$ gap just used.

Therefore


$$
\boxed{\text{Every atom-in-bottom term has depth at least }
\mathfrak m_d+3.}
\tag{8.9}
$$



### 8.4 Exact fixed-$I,J$ aggregate

It remains to treat no-factorial terms with the atom in the product.

For fixed forcing/source sets $I,J$, each of size $p$, summing over **all choices of product contact columns** is an exact block determinant. The Cauchy identity gives the common scalar


$$
C_p(I)=
\frac{\Lambda_k^p2^{p(p-1)}\Phi_pV(I)}
{\prod_{i=0}^{n-1}Q_I(i)}.
\tag{8.10}
$$


The upper block consists of the $p$ source rows $A[J,:]$. The lower block consists of the rows


$$
\Delta^j(Q_IW)(0),\qquad p\le j\le n-1,
$$


with the bottom atom column set to zero, since the atom is constrained to be a product column.

This identity is the Laplace expansion over the actual contact-column choices. It is not a selected summand.

At $I=J=\mathcal T_p$, transform the consecutive top rows to forward differences. Multiply the atom column by $R_{p-1}^\uparrow$, divide top row $j$ by
$2^jR_j^\uparrow$, and divide bottom row $j$ by $2^jj!$. The resulting matrix $Z_p$ is integral and has:

- top atom entry
  

$$
\frac{R_{p-1}^\uparrow}{R_j^\uparrow}
  \frac{\Delta^j\mathsf a_{w,d-p}}{2^j};
$$


- top contact entries
  

$$
\frac{\Delta^j\mathsf v_{d-p}^{(r)}}
  {2^jR_j^\uparrow};
$$


- bottom atom entries zero;
- bottom contact entries
  

$$
\frac{\Delta^j(Q_{\mathcal T_p}\theta_r)(0)}{2^jj!}.
$$



Exactly, the minimal-pair aggregate is


$$
\boxed{2^{\mathcal L_p}\Xi_{n,p}\det Z_p,}
\tag{8.11}
$$


with the full odd unit $\Xi_{n,p}$ from (6.6).

### 8.5 Two independent row relations

Let


$$
K_\theta^{(D)}(j,r)
=
\sum_{t=0}^D
\binom Dt\binom{r+j+t}{r}\theta_{r+j+t}\pmod2.
$$


The full source product rule and bottom mixed-jet rule identify the top and bottom contact parities of $Z_p$ with


$$
K_\theta^{(d)}(j,r),
\qquad
K_\theta^{(p)}(z,r),
$$


respectively.

The normalized $w$-atom jets are odd. One direct verification is


$$
\frac{\Delta^{d+j}(P_dw)}{2^{d+j}}
=
(\pm)w\sum_h\binom{d+j}{h}\frac{\Delta^hP_d}{2^h}.
$$


Terms with $h\ge2$ are even because $h!\mid\Delta^hP_d/2^h$; the $h=1$ term is even because $d$ is even; the $h=0$ term is odd.

For $p\ge5$, the first two top atom entries of $Z_p$ are even. Thus top rows $0$ and $1$, modulo two, have zero atom coordinate.

Set $D=d-p$. The exact binomial shift relation is


$$
K_\theta^{(d)}(j)
=
(1+E)^D K_\theta^{(p)}(j),
$$


where $E$ shifts the contact-row index. Since the bottom count is


$$
h=n-p=D+2,
$$


the bottom rows include orders $0,\ldots,D+1$. Hence


$$
\boxed{
K_\theta^{(d)}(0)
=\sum_{t=0}^D\binom DtK_\theta^{(p)}(t),
}
\tag{8.12}
$$




$$
\boxed{
K_\theta^{(d)}(1)
=\sum_{t=0}^D\binom DtK_\theta^{(p)}(t+1).
}
\tag{8.13}
$$



These are two independent row relations in the full normalized matrix: one has coefficient $1$ on top row $0$, the other on top row $1$, and neither uses the other top row.

Therefore


$$
\operatorname{rank}_{\mathbb F_2}Z_p\le n-2.
$$


For an integral matrix, binary corank at least two implies divisibility of its determinant by $4$: lift binary elimination using odd pivots and factor $2$ from the remaining two rows. Thus


$$
\boxed{4\mid\det Z_p.}
\tag{8.14}
$$



This strengthens the turn-14 nominal cancellation. The lower-rank $\eta$-window does not contradict it: here the bottom count is $d+2-p$, which supplies precisely the two shift relations and is outside $h\le\varrho-1$.

### 8.6 Near-minimal $N_d$-minors are retained

Write


$$
w(I,J)=\sum_{i\in I}e_i+\sum_{j\in J}e_j-2E_p.
$$


If $w(I,J)\ge2$, the ordinary lower payment already places the term at depth at least $\mathcal L_p+2$.

A weight-one pair can occur only when $p$ is odd. Let $b=d-p$. The only one-set change of weight one is


$$
\mathcal T'_p=\{b-1,b+1,\ldots,d-1\},
$$


because


$$
e_{b-1}-e_b=1+v_2(b)=1.
$$


Thus the only candidate pairs are


$$
(\mathcal T'_p,\mathcal T_p),\qquad
(\mathcal T_p,\mathcal T'_p).
\tag{8.15}
$$


No oddness of their complementary $K_d$-minors is assumed.

For arbitrary source rows $J$, finite Newton expansion shows that the normalized leading source functional is the same minimizing jet functional multiplied by


$$
\mathcal N_p(J)=\frac{V(J)}{\Phi_p}.
$$


Every higher Newton-order selection pays an additional factor $2$. The bottom leading kernel depends only on $|I|=p$. Consequently, the leading fixed-$I,J$ aggregate is a scalar multiple of the same singular contact stack.

For the specific near-minimal set,


$$
\mathcal N_p(\mathcal T'_p)=p,
$$


which is odd when the weight-one case exists. Nevertheless, its complete normalized leading aggregate is zero by (8.12)–(8.13). Its explicit extra $N_d$-weight therefore supplies total depth at least


$$
\mathcal L_p+2.
$$



Thus the near-minimal minors have been included and cancelled at the required precision, not discarded by a presumed inverse-return unit.

Combining (8.11)–(8.15), the no-factorial atom-in-product $p$-sector has depth at least $\mathcal L_p+2$ in the relevant strip. The previously derived factorial comparison


$$
v\bigl(\alpha-4p-3m_d-12\bigr)
$$


is at least $2$ for $5\le p\le d/3$, so the complete sector satisfies


$$
\boxed{
2^{\mathcal L_p+2}\mid
\text{the complete \(p\)-sector},
\qquad 5\le p\le\lfloor d/3\rfloor.
}
\tag{8.16}
$$



### 8.7 The whole next digit

All counts with
$\mathcal L_p\le\mathfrak m_d+1$ lie in the strip covered by (8.16). Every other no-factorial, atom-in-product count already has nominal depth at least $\mathfrak m_d+2$. Equations (8.8)–(8.9) exclude all remaining correction patterns globally.

Therefore


$$
\boxed{
2^{\mathfrak m_d+2}\mid
\det[w_*,v^{(0)},\ldots,v^{(d)}].
}
\tag{8.17}
$$



Equivalently, the whole aggregate digit immediately after the turn-14 cancellation is also zero:


$$
\boxed{
2^{-(\mathfrak m_d+1)}
\det[w_*,v^{(0)},\ldots,v^{(d)}]\equiv0\pmod2.
}
\tag{8.18}
$$



Since


$$
v_2(\mathfrak c_k)=\alpha+A_d,
$$


the complete linear coefficient satisfies


$$
v_2(I_{1,k})\ge\alpha+A_d+\mathfrak m_d+2.
\tag{8.19}
$$



This is a new proved statement in this report. It awaits DIFFERENT review and supplies no upper bound for $v_2(I_{1,k})$.

---

## 9. The next exact obligation

The nominal minimum remains


$$
\mathfrak m_d=\frac{11}{4}d^2+O(d\log d),
$$


but it is not attained at either of its first two aggregate binary layers.

A concrete next obligation is to evaluate


$$
2^{-(\mathfrak m_d+2)}
\det[w_*,v^{(0)},\ldots,v^{(d)}]\pmod2,
\tag{9.1}
$$


including every minimum product count and its near-minimal source/forcing terms.

The new proof identifies the additional information needed.

### 9.1 First lifts of the two shift relations

In the exact normalized matrix $Z_p$, perform the row subtractions corresponding to (8.12)–(8.13), then divide those two certified even rows by $2$. This is an operation on the auxiliary normalized matrix, not on the original integer pencil. Exactly,


$$
\frac{\det Z_p}{4}
$$


is the determinant after those two paid row divisions.

Its parity requires:

- normalized top $\theta$-source jets modulo $4$;
- normalized bottom jets
  

$$
\frac{\Delta^j(Q_I\theta_r)(0)}{2^jj!}\pmod4,
  \qquad p\le j\le d+1;
$$


- the actual atom quotients and rising-factor ratios modulo the same precision;
- the finite source-Newton contributions one payment above the minimum when $J=\mathcal T'_p$.

The parity-only kernel does not provide these first lifts. In particular, dependence on physical base rows and actual pole choices can return at this precision.

### 9.2 Actual inverse returns for the near-minimal $N_d$-minors

For $b=d-p$, let


$$
A=\{0,\ldots,b-1\}.
$$


The weight-one complementary minors are controlled by the actual finite inverse returns


$$
\zeta_p^+
=
e_{b-1}^{\,T}K_d[A,A]^{-1}K_d[A,\{b\}],
$$




$$
\zeta_p^-
=
K_d[\{b\},A]K_d[A,A]^{-1}e_{b-1}.
\tag{9.2}
$$


The leading block is invertible over $\mathbb Z_{(2)}$ by the established odd principal-minor theorem. No symmetry identifies these two returns.

Jacobi’s identity expresses the near-minimal $N_d$-minors using these returns, the actual leading determinant, and the full factorial diagonal factors. Their required residues must be proved, or the corresponding lifted aggregates must be shown to vanish so that these returns are no longer needed at that digit.

This is a precise uniform symbolic obligation. It is not a request for an original-sized inverse or solve.

### 9.3 What would constitute an upper-excess result

For the research objective, repeated zero digits alone are insufficient. A useful eventual theorem must prove noncancellation within a controlled number of layers, for example


$$
v_2\det[w_*,v^{(0)},\ldots,v^{(d)}]
\le \mathfrak m_d+O(d\log d)
$$


on explicitly stated original indices, while retaining (7.4) and all coefficient-transfer factors.

That upper-excess statement remains open. The new result makes the obstruction sharper: there are two independent leading shift relations, and their first $2$-adic lifts, together with the near-boundary inverse returns, govern the next possible layer.

---

## 10. Global arithmetic and analytic scope

The required binary terminal upper remains


$$
\boxed{
\nu_k^{[5]}
\le \frac{15}{4}k^2-64+O(k\log k).
}
\tag{10.1}
$$


Equivalently,


$$
\min(v_2(I_{0,k}),v_2(I_{1,k}))
\le \frac{15}{4}k^2+d+5+O(k\log k),
$$


because


$$
\min(v_2(I_{0,k}),v_2(I_{1,k}))
=d+69+\nu_k^{[5]}.
$$


Nothing proved here establishes this upper bound.

The exact primitive identities remain


$$
\boxed{
\frac{|P_{1,k}^{[5]}|}{g_k^{[5]}}
=\frac{|H_{1,k}|}{G_k}=q_k,
}
$$




$$
\boxed{
\frac{|P_{0,k}^{[5]}+P_{1,k}^{[5]}(e+\pi)|}{g_k^{[5]}}
=\frac{|H_k(e+\pi)|}{G_k}
=\ell_k>0.
}
\tag{10.2}
$$


Neither the pure-Cauchy reference nor its perturbation is substituted into these identities.

The established ternary statements retain only their proved scope. The other odd-prime descents and large-prime exclusions remain separate open obligations. The closed same-$H$ analytic estimate is unchanged:


$$
\log|H_k(e+\pi)|
\ge
4k^2\log k+
\left(15\log2-\frac92\log3+\frac4{85}\right)k^2
+o(k^2).
$$


A producer-retirement conclusion would still require all the independent arithmetic controls. A conclusion restricted to the rotation subfamily would concern only that subfamily. In any event, retirement of this producer would not decide whether $e+\pi$ is rational or irrational.

---

## 11. Proof-status ledger and computation scope

| Statement | Status |
|---|---|
| Complete A4 five-column reference normalization and changed-pivot treatment | **PASS** |
| All first-layer correction patterns | **PASS** |
| Complete constant- and linear-border source payments | **PASS** |
| Both border-difference zeros at $L_d+7$ | **PASS** |
| Evaluated $\kappa_d(r)$, exact rank one, returns $2,3$ | **PASS** |
| Full mixed kernel, including the odd derivative | **PASS** |
| Higher rows at both parities and exact Pascal relation | **PASS** |
| Finite root candidate, both denominators, degree cutoff | **PASS** |
| Arbitrary mixed-combination coefficient constraints | **PASS** |
| Rank $p+h$ modulo $R_{p+1}$ | **PASS under (5.1)** |
| Complete leading-sector relative normalization | **PASS** |
| Full equality-tie sum and attained $F_q(p)$ | **PASS under the displayed hypotheses** |
| Same infinite original interval | **PASS** |
| Turn-14 paired coefficient identities | **Retained at their proved scope; not newly labelled DIFFERENT-reviewed** |
| Two independent full-rank leading relations | **New proved result** |
| Whole divisibility $2^{\mathfrak m_d+2}\mid D_k$ | **New proved result; DIFFERENT audit pending** |
| Next digit (9.1), controlled upper excess, terminal joint upper | **Open** |
| Other-prime control, all-index retirement, $e+\pi$ decision | **Open** |

No tools have been used. No closed source table, first-return receipt, phase-$8192$ calculation, old digit receipt, or original-sized solve has been repeated.

**No new bounded exact arithmetic calculation is indispensable to the proofs above, and none is requested.** The next missing work is a uniform first-lift jet and inverse-return lemma. A finite calculation could authenticate only its specified finite inputs; it would not establish that uniform lemma or the terminal upper.

---

## Final conclusion

The new complete five-column perturbation theorem passes: its first difference layer is an evaluated rank-one matrix, its pivot feedback changes $S_5$ to $\kappa_d$, and both complete coefficient-border differences vanish at that layer.

The parent larger mixed-return theorem also passes. The odd derivative survives exactly where required, the finite root argument excludes every nonzero mixed combination from the larger source space, and the complete relative normalization validates the proposed equality-tie sum. This yields attaining original-column cofactors throughout the stated linear window on the same infinite original interval.

The new full-rank advance is an evaluated further cancellation:


$$
\boxed{
2^{\mathfrak m_d+2}\mid
\det[w_*,v^{(0)},\ldots,v^{(d)}].
}
$$


Two independent shift relations force the second zero digit, and the proof pays all competing product counts and near-minimal forcing/source minors.

The remaining bottleneck is now the first $2$-adic lift of those two relations and its interaction with the actual near-boundary inverse returns, followed by a controlled **noncancellation upper bound** for the complete coefficient pair. The constant coefficient, least clearers, all odd factors, final all-prime gcd, actual primitive denominator, and nonzero whole evaluated error remain unchanged.

No unconditional rationality or irrationality conclusion for $e+\pi$ has been obtained.
