> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the full mixed kernel and first transition, with a two-return extension

## Abstract

The three new parent mixed notes pass this independent mathematical audit, subject to one computational-complexity correction: binary search requires $O(\log d)$ evaluations of the digit expression, not automatically $O(\log d)$ **bit operations**.

The principal audited conclusions are as follows.

1. The normalized Newton-product jets of the actual columns $Q_IW_r$ are exactly the asserted $U_a$-array, where $a=|I|$ is the number of retained rational Cauchy columns. This auxiliary count is not a replacement for the original index $d$.
2. The joint generating kernel is correct at both parities of $a$. Its odd-parameter derivative term is indispensable.
3. The mixed costs $F_q(p)$, their increments $D_p$, the strict monotonicity of $D_p$, and the factorial and atom exclusions are correct at their stated scope.
4. On the first $2L$ original return columns, the stronger statement
   

$$
S_p\notin R_{p+1}
$$


   holds at both parities under the stated finite cutoffs. The proof must clear both unit denominators. The even candidate is indeed
   

$$
\omega^{2p+1}a^{\rho-2}b^{p-\rho+1}.
$$


5. The complete first attaining mixed compound is correctly identified. At an equality $D_{p+1}=L_d$, the pure and one-$W$ contributions have the same binary depth and explicitly derived odd relative prefactors. Their sum reduces to
   

$$
\det[R_p;v_{\rm new}+S_p].
$$


   This conclusion does not follow merely from the ranks of the two summands.

The new result proved after the audit is a two-return extension:


$$
\boxed{
\operatorname{rank}_{\mathbb F_2}
[R_{p+1};U_p(0,\bullet);U_p(1,\bullet)]=p+2.
}
$$


It yields an attaining complete common-column cofactor **one size beyond the first transition**, including the equality case, on the same explicit infinite original subfamily. A division-free Cramer consequence is then given with both complete coefficient borders and their common normalization retained.

No terminal coefficient upper bound, all-prime gcd bound sufficient for the global objective, primitive whole-error decay, producer retirement, or rationality decision for $e+\pi$ is obtained.

---

## 1. Original objects and arithmetic interface

### 1.1 Unchanged original domain and boundaries

Throughout,


$$
\boxed{k=9^{18+32u},\qquad u\ge0,\qquad d=k-1.}
$$


Thus


$$
d\equiv2\pmod3,\qquad v_2(d)=4,\qquad d\equiv208\pmod{256}.
$$



The finite ranges are unchanged:

- top-source row: $0\le n<d$;
- original return order: $0\le r<d$;
- a top jet is used only when $n+j<d$;
- residual row $i$, $0\le i\le d+1$, is original physical row $d+i$.

In particular, the physical terminal and final data remain


$$
\boxed{
2k-1=2d+1,\quad
3k-2=3d+1,\quad
(6k-4)!=(6d+2)!,\quad
6k-5=6d+1.
}
$$



### 1.2 Complete sequences and forcing

Retain


$$
a_0=1,\qquad a_n=1-na_{n-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad w_n=(-1)^n,\qquad c_n=u_n-w_n,
$$


and


$$
\rho_0=0,\qquad
\rho_{n+1}+\rho_n=\frac1{2n+1},\qquad
r_n=-f_n+4\rho_n.
$$



The complete returns are


$$
\sigma_n=u_{n+1}+u_n=c_{n+1}+c_n
$$


and


$$
\tau_n=-(2n+2)!-(2n)!+\frac4{2n+1}.
$$


With


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),
$$


the actual integer forcing is


$$
\boxed{
T_n=-\Lambda_k\bigl((2n+2)!+(2n)!\bigr)
+\frac{4\Lambda_k}{2n+1}.
}
$$


Neither factorial summand is removed.

### 1.3 Actual contents, clearers, gcd, denominator, and whole error

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


with $0\le m<2k$, $0\le j<k$.

The least entry clearer of right column $j$ is


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3).
$$


Define the actual all-prime gcds


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),\qquad
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


The least simultaneous coefficient clearer of $H_k/\Lambda_k^k$, and its content after clearing, are


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},\qquad
\frac{G_k}{d_{H,k}}.
}
$$



The original rectangles remain


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


For


$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
\mathscr L_k=\delta_{2k-1}(Y_k),
$$


the established interface is


$$
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k\mid \Lambda_k\mathscr L_k\mathscr R_k.
$$



The retained sign and nonvanishing results give


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
$$


No binary lower divisor is substituted for $G_k$.

### 1.4 Complete corrected columns

Put


$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1),\qquad
\mathcal A_dy=\Delta^d(P_dy).
$$


This operation is applied only to the first $d$ original rows and retains


$$
\Omega_k=\prod_{n<d}P_d(n).
$$



For


$$
b(t)=4t^2+6t+3,
$$


the complete top forcing block is


$$
F_k(n,j)=
-\Lambda_k\sum_{h=0}^{d}(-1)^h\binom dh
P_d(n+h)b(n+h+j)(2(n+h+j))!,
\qquad n,j<d.
$$


Here


$$
b(t)(2t)!=(2t+2)!+(2t)!.
$$



Write


$$
F_k=-\Lambda_kD_fK_dD_f,\qquad
D_f=\operatorname{diag}((2n)!)_{n<d},
$$


and


$$
\eta_d^F=\det K_d.
$$


The oddness of $\eta_d^F$ and of every leading principal determinant of $K_d$ is established reuse.

Retain


$$
\alpha=v_2((2d)!),\qquad
\beta=v_2((2d-2)!),\qquad \alpha-\beta=5,
$$




$$
h_d=(2d-2)!,\qquad
\widehat D_f=h_dD_f^{-1},
$$




$$
N_d=\widehat D_f\operatorname{adj}(K_d)\widehat D_f,
\qquad
\delta_k=\Lambda_k\eta_d^Fh_d^2,
$$




$$
f_k=(-\Lambda_k)^d\eta_d^F
\left(\prod_{n<d}(2n)!\right)^2.
$$



The complete bottom forcing is


$$
R(i,j)=
\frac{\Lambda_k}{2(d+i+j)+1}
-\frac{\Lambda_k}{4}b(d+i+j)(2(d+i+j))!,
\quad i\le d+1,\ j<d.
$$



All full return divisions remain


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
+\frac{\delta_k}{2^{\alpha+3}D_r}
(\Delta^r\sigma)_{\rm bot}.
$$


For $\psi_0=r,\ \psi_1=w$, both full borders are


$$
\boxed{
\mathfrak b_\varepsilon
=RN_d\Lambda_k(\mathcal A_d\psi_\varepsilon)_{\rm top}
+\frac{\delta_k\Lambda_k}{4}(\psi_\varepsilon)_{\rm bot},
\qquad \varepsilon=0,1.
}
$$


Thus


$$
\mathcal Q_k(s)
=[x,z^{(0)},\ldots,z^{(d-1)},\mathfrak b_0+s\mathfrak b_1].
$$



Set


$$
L_d=\alpha-12,\qquad
M_d=\alpha-d+1,\qquad
\gamma_k=\delta_k/2^{2\beta}.
$$


The actual odd scalar is


$$
\boxed{\gamma_k=\Lambda_k\eta_d^F\operatorname{odd}(h_d)^2.}
$$


The exact simultaneous decomposition is


$$
\mathcal Q_k(s)
=RN_d\mathcal A_k(s)+2^{L_d}\gamma_k\mathcal W_k(s),
$$


where


$$
\mathcal W_k(s)=
\left[
2^{M_d}\frac{c_{\rm bot}}2,\
(\eta_r^{(d+i)})_{r<d},\
2^\alpha\Lambda_k(r+sw)_{\rm bot}
\right],
$$


and


$$
\eta_r^{(m)}=\frac{\Delta^r\sigma_m}{2^{r+1}r!}.
$$


Also,


$$
R=R^{\rm C}-2^{\alpha-2}V,
$$


with


$$
R^{\rm C}(i,j)=\frac{\Lambda_k}{2(d+i+j)+1},
\qquad
V(i,j)=
\frac{\Lambda_kb(d+i+j)(2(d+i+j))!}{2^\alpha}.
$$


These are exact integer identities on the stated finite ranges.

### 1.5 Previously paid five-column interface

The selected columns


$$
[x,z^{(1)},z^{(0)},z^{(5)},z^{(4)}]
$$


and their depths $5,19,39,72$ are reuse. Their actual odd quotients are not replaced by $1$.

The paid all-prime identities remain


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



To avoid collision with the mixed Newton weights below, write


$$
\lambda_{\rm tr}=d\alpha+4d+4.
$$


The established full transfer is


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_{5,k}|^{d-4}G_k
=
|f_k|\,2^{\lambda_{\rm tr}+d+69}\mathfrak D_d\,g_k^{[5]}.
}
\tag{1.1}
$$


No calculation establishing this interface is repeated here.

---

## 2. Established premises used in the audit

The following are reused at their already audited scope.

1. **Integral contact jets and shift-independent parity.**
   

$$
\Delta^j\eta_r^{(m)}
   =2^j(r+1)_j\eta_{r+j}^{(m)},
   \qquad
   \eta_r^{(m)}\equiv\eta_r\pmod2.
$$



2. **Exact contact parity.** In
   

$$
\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1),
$$


   

$$
\eta_n
   =\operatorname{Tr}\!\left(\omega^{n+2}+(n+1)\omega^n\right).
   \tag{2.1}
$$


   Trace and conjugation act coefficientwise, leaving formal variables fixed.

3. **Full rising source division.**
   

$$
U^{\mathbb Z}_{jr}(n)
   =\frac{\Delta^jt_n^{(r)}}{2^j(d+1)_j}\in\mathbb Z,
   \qquad n+j<d,
$$


   and its parity is independent of $n$.

4. **Atom jets.**
   

$$
A_j(n):=\frac{\Delta^j\mathsf a_n}{2^j}\in\mathbb Z,
   \qquad A_j(n)\equiv1\pmod2
$$


   whenever $n+j<d$.

5. **Source payment.** With
   

$$
\mathcal B_p(d)
   =2^{\binom p2}\prod_{j=0}^{p-2}(d+1)_j,
   \qquad
   B_p(d)=v_2(\mathcal B_p(d)),
$$


   every $p$-source minor with an atom and $p-1$ returns is divisible by the full integer $\mathcal B_p(d)$. An all-return source minor has the additional rising factor $(d+1)_{p-1}$.

6. **Rectangular rank.** If $L$ is dyadic, $2L\le d$, $\rho=d\bmod L$, and
   

$$
\rho+2m\le L,
$$


   then the first $2m$ normalized contact rows have rank $2m$ on the first $2L$ original return columns.

7. **Mixed Cauchy payment with free columns.** The full finite Newton theorem for several weighted returns and arbitrary free integer columns is available. The atom is only a free column in that theorem; it is not assigned an unproved factorial-jet divisor.

The new rank-one result of A4 turn 22, its new border-difference bounds, and the turn 21 all-order similarity theorem are **not** used as independently audited premises in this report. Their separate different-review obligations remain separate.

---

## 3. Audit of the full mixed Newton-product jets

### 3.1 The exact product column

Choose $a$ actual rational Cauchy forcing-column indices $I\subset\{0,\ldots,d-1\}$, and put


$$
Q_I(i)=\prod_{b\in I}(2(d+i+b)+1),
\qquad
W_r(i)=\eta_r^{(d+i)}.
$$



Here


$$
\boxed{a=|I|}
$$


is an auxiliary mixed-compound count. It is not the original even parameter $d$, and it need not equal the number of product columns when factorial columns are also selected.

For every admissible order $j$,


$$
2^jj!\mid\Delta^j(Q_IW_r)(i).
\tag{3.1}
$$



To verify the normalized parity, write $Q_I$ as a polynomial in $2i$. Its degree-$b$ coefficient is congruent to $\binom ab$, because each constant factor is odd. In


$$
\frac{\Delta^tQ_I(i)}{2^tt!},
$$


terms of degree less than $t$ vanish; terms of degree greater than $t$ retain an additional factor $2$; and the degree-$t$ term contributes $1$ after dividing by $t!$. Thus


$$
\frac{\Delta^tQ_I(i)}{2^tt!}\equiv\binom at\pmod2.
\tag{3.2}
$$



The return identity gives


$$
\frac{\Delta^sW_r(i)}{2^ss!}
\equiv\binom{r+s}{r}\eta_{r+s}\pmod2.
\tag{3.3}
$$


In the finite product rule, the factor $\binom jt$ cancels the factorial ratio exactly. Hence


$$
\boxed{
\frac{\Delta^j(Q_IW_r)(0)}{2^jj!}
\equiv
\sum_{t=0}^{\min(a,j)}
\binom at\binom{r+j-t}{r}\eta_{r+j-t}
\pmod2.
}
\tag{3.4}
$$



The odd factors in these integer divisions are taken before parity is reduced.

For $j=a+z$, changing $t$ to $a-t$ yields


$$
\boxed{
U_a(z,r)=
\sum_{t=0}^{a}
\binom at\binom{r+z+t}{r}\eta_{r+z+t}.
}
\tag{3.5}
$$


The leading unused weighted-return row is


$$
S_a(r)=U_a(0,r).
$$



The same formula with $a=d$ gives the parity of the actual top source:


$$
U^{\mathbb Z}_{jr}(n)\equiv U_d(j,r)\pmod2.
$$


This follows from the established full rising identity after putting $t=d-h$. Thus the complete mixed array couples


$$
\boxed{\text{top rows }U_d\quad\text{and bottom rows }U_a,}
$$


with their different parameters retained.

### 3.2 Both-parity generating kernel

Put


$$
a(Y)=1+\omega Y,\qquad b(Y)=1+\omega^2Y,\qquad S=X+Y,
$$


and


$$
B_e(Y)=\left(\frac{\omega^2+\omega Y}{1+\omega Y}\right)^e
=\omega^{2e}\frac{b(Y)^e}{a(Y)^e}.
$$



The finite binomial generating identity


$$
\sum_{z,r\ge0}\binom{t+z+r}{r}X^zY^r
=\frac{(1-Y)^{-t}}{1-X-Y}
$$


gives


$$
H_e(X,Y)=\frac{B_e(Y)}{1+\omega S}.
$$



Let


$$
E=X\frac{\partial}{\partial X}+Y\frac{\partial}{\partial Y}.
$$


The factor $r+z+t+1$ in (2.1) gives


$$
\sum_{z,r\ge0}U_e(z,r)X^zY^r
=
\operatorname{Tr}\bigl((\omega^2+1)H_e+EH_e+T_e\bigr),
$$


where


$$
T_e=(e\bmod2)\,
\frac{\omega B_{e-1}(Y)}
{a(Y)(1+\omega S)}.
$$



The derivative of the numerator factor is


$$
YB_e'(Y)
=(e\bmod2)\frac{\omega^2YB_{e-1}(Y)}{a(Y)^2}.
$$


Consequently,


$$
YB_e'
+(e\bmod2)\frac{\omega B_{e-1}}a
=(e\bmod2)\frac{\omega B_{e-1}}{a^2}.
$$


Combining the remaining denominator derivative gives the full kernel


$$
\boxed{
\sum_{z,r\ge0}U_e(z,r)X^zY^r
=
\operatorname{Tr}\!\left[
B_e(Y)\frac{\omega+S}{(1+\omega S)^2}
+(e\bmod2)
\frac{\omega B_{e-1}(Y)}
{a(Y)^2(1+\omega S)}
\right].
}
\tag{3.6}
$$



For $e=0$, the second term is zero and $B_{-1}$ is not used.

The odd term cannot be deleted. At $e=1,z=r=0$,


$$
U_1(0,0)=\eta_0+\eta_1=1.
$$


The first kernel term alone has trace $0$; the second contributes $1$.

**Verdict: PASS.** The odd derivative is mathematically necessary, not an optional presentation choice.

### 3.3 Explicit generating rows

Extracting coefficients of $X$ from (3.6) also gives the full row array.

For even $e$,


$$
\boxed{
\begin{aligned}
U_e(2h,Y)
&=\operatorname{Tr}\!\left(
\omega^{2e+2h+1}\frac{b^{e+1}}{a^{e+2h+2}}
\right),\\
U_e(2h+1,Y)
&=\operatorname{Tr}\!\left(
\omega^{2e+2h}\frac{b^e}{a^{e+2h+2}}
\right).
\end{aligned}}
\tag{3.7}
$$



For odd $e$,


$$
\boxed{
\begin{aligned}
U_e(2h,Y)
&=\operatorname{Tr}\!\left(
\omega^{2e+2h}\frac{b^{e-1}}{a^{e+2h}}
\right),\\
U_e(2h+1,Y)
&=\operatorname{Tr}\!\left(
\omega^{2e+2h}
\frac{b^{e-1}Y(1+Y)}{a^{e+2h+3}}
\right).
\end{aligned}}
\tag{3.8}
$$



For example, the even-$X$ coefficient at odd $e$ uses


$$
\omega^2b^2+1=\omega a^2;
$$


the odd-$X$ coefficient uses


$$
ab+1=Y(1+Y).
$$


These identities account directly for the simplifications.

In particular,


$$
\boxed{
S_p(Y)=
\begin{cases}
\displaystyle
\operatorname{Tr}\!\left(
\omega^{2p}\frac{b^{p-1}}{a^p}
\right),&p\ \text{odd},\\[3mm]
\displaystyle
\operatorname{Tr}\!\left(
\omega^{2p+1}\frac{b^{p+1}}{a^{p+2}}
\right),&p\ \text{even}.
\end{cases}}
\tag{3.9}
$$



These are the simplified rows asserted in the parent notes.

### 3.4 Finite scope

The formal kernel is used only for coefficients corresponding to actual jets:


$$
a+z\le d+1,
$$


or, from a shifted residual start $i$,


$$
i+a+z\le d+1.
$$


Then


$$
d+r+i+a+z\le 3d.
$$


This is a return index, so its successor moment is at most $3d+1$, exactly the retained original terminal.

No return $r\ge d$, no factorial beyond $(6k-4)!$, and no enlarged physical row range is introduced.

---

## 4. Audit of every mixed cost and its minimizer

### 4.1 Notation

To distinguish cost sums from the row $S_p$, define


$$
\lambda_j=j+v_2(j!)=2j-s_2(j),
\qquad
\Sigma_n=\sum_{j=0}^{n-1}\lambda_j.
$$


Then


$$
c_n=2\Sigma_n.
$$



Put


$$
e_n=v_2\!\left(\frac{h_d}{(2n)!}\right),
\qquad
E_p=\sum_{n=d-p}^{d-1}e_n,
$$




$$
v_j(d)=v_2((d+1)_j),
\qquad
\mathsf T_p=\Sigma_p+2E_p+B_p,
$$


with $\Sigma_0=\mathsf T_0=0$.

### 4.2 Atom in the product, no factorial column

Consider a $q$-common-column minor containing the atom. Suppose it uses

- $p$ product columns;
- $h=q-p$ bottom-return corrections;
- no factorial column of $R$;
- the atom in the product part.

The exact lower payment is


$$
hL_d+c_p+2E_p+B_p+\sum_{j=p}^{q-1}\lambda_j.
$$


Equivalently,


$$
\boxed{
F_q(p)=qL_d+\Sigma_q+\mathsf T_p-pL_d,
\qquad 1\le p\le q.
}
\tag{4.1}
$$



### 4.3 Factorial columns

If $v$ of the $p$ product columns use the factorial part of $R$, there are


$$
a=p-v
$$


rational Cauchy columns. The lower payment is


$$
(q-p)L_d+v(\alpha-2)
+\Sigma_a+\Sigma_{a+q-p}
+2E_p+B_p.
\tag{4.2}
$$


The difference from $F_q(p)$ is


$$
v(\alpha-2)
-(\Sigma_p-\Sigma_a)
-(\Sigma_q-\Sigma_{q-v}).
$$


Since each of the two differences contains $v$ terms and $\lambda_j\le2q$ in the relevant range,


$$
\boxed{
(4.2)-F_q(p)\ge v(\alpha-2-4q).
}
\tag{4.3}
$$



This is a comparison of complete determinant terms. It does not delete the factorial part entrywise.

### 4.4 Atom in $W$, including $p=0$

If the atom is a bottom correction, $h\ge1$. It retains its full factor $2^{M_d}$, and the remaining $p$ top sources are all returns. Their extra payment is


$$
\epsilon_p=
\begin{cases}
v_{p-1}(d),&p\ge1,\\
0,&p=0.
\end{cases}
$$


Only $h-1$ bottom columns are weighted returns; the atom is free.

Relative to the corresponding formal atom-in-product bound, the extra payment is


$$
M_d+\epsilon_p-\lambda_{a+h-1}.
$$


For


$$
m=m_d=1+\lfloor\log_2d\rfloor,
$$




$$
M_d\ge d-m+1,\qquad
\epsilon_p\ge p-m-2,
$$


where the latter inequality remains true at $p=0$. Therefore


$$
\boxed{
M_d+\epsilon_p-\lambda_{a+h-1}
\ge d+p-2q+2v+1-2m
\ge d-2q+1-2m.
}
\tag{4.4}
$$



The formal $p=0$ value is


$$
F_q(0)=qL_d+\Sigma_q,
$$


and


$$
F_q(0)-F_q(1)=L_d>0.
$$



Thus, under


$$
\boxed{
q\le d,\qquad
\alpha-2>4q,\qquad
d-2q+1-2m>0,
}
\tag{4.5}
$$


the minimum of the lower payments over all correction patterns is exactly


$$
\min_{1\le p\le q}F_q(p).
$$



**Verdict: PASS**, including the all-bottom case $p=0$. The atom has not been given a weighted-return divisor.

### 4.5 Exact increments

For $p\ge2$,


$$
D_p=\mathsf T_p-\mathsf T_{p-1}
=\lambda_{p-1}+2e_{d-p}+(p-1)+v_{p-2}(d).
$$


Using


$$
e_{d-p}=2p-2+s_2(d-p)-s_2(d-1)
$$


and


$$
v_{p-2}(d)=p-2+s_2(d)-s_2(d+p-2),
$$


we obtain


$$
\boxed{
D_p=
8p-9+s_2(d)-2s_2(d-1)
+2s_2(d-p)-s_2(p-1)-s_2(d+p-2).
}
\tag{4.6}
$$



Furthermore,


$$
\boxed{
D_{p+1}-D_p
=1+v_2(p)+2(1+v_2(d-p))+1+v_2(d+p-1)
\ge4.
}
\tag{4.7}
$$


Thus the increments are strictly increasing.

At the lower endpoint,


$$
D_2=4<L_d.
$$


At the upper endpoint, $D_d>L_d$, for example because its contribution $2e_0=2\beta$ alone exceeds $L_d=\beta-7$.

Define


$$
s=\min\{r\in\{2,\ldots,d\}:D_r\ge L_d\},
\qquad
p=s-1,\qquad q=s=p+1.
\tag{4.8}
$$


Then


$$
D_p<L_d\le D_q.
$$



- If $D_q>L_d$, $p$ is the unique minimizing product count once the minor size reaches $q$.
- If $D_q=L_d$, the only minimizing counts are $p$ and $q$.

Before that transition, at every size $j\le p$, the unique minimum is the pure count $j$.

### 4.6 Quantitative location in the original domain

Because $v_2(d)=4$,


$$
s_2(d-1)=s_2(d)+3.
$$


Subtracting $L_d=2d-s_2(d)-12$ from (4.6) gives the particularly useful exact formula


$$
\boxed{
D_r-L_d
=8r-2d-3
+2s_2(d-r)-s_2(r-1)-s_2(d+r-2).
}
\tag{4.9}
$$


The digit terms imply


$$
\boxed{\left|p-\frac d4\right|\le\frac m4+1.}
\tag{4.10}
$$


Thus $p=d/4+O(\log d)$, with an explicit uniform bound.

**Complexity repair.** Monotonicity permits $O(\log d)$ evaluations of (4.6). With ordinary bit arithmetic, each evaluation reads $O(\log d)$-bit integers, so an immediate implementation has $O((\log d)^2)$ bit cost. An $O(\log d)$ claim is justified only in an explicitly stated unit-cost word/popcount model. This repair does not affect the mathematical minimizer.

---

## 5. Independent audit of the stronger both-parity nonmembership lemma

Assume


$$
\boxed{
d=2L+\rho,\quad L\text{ dyadic},\quad
\rho\ge4\text{ even},\quad
p\ge\rho+1,\quad
\rho+p\le L.
}
\tag{5.1}
$$


All row spaces in this section are on the first $2L$ original return columns.

Write


$$
U_j=U_d(j,\bullet).
$$


The atom-cofactor row spaces are


$$
R_q=
\begin{cases}
\operatorname{span}(U_0,\ldots,U_{q-2}),&q\text{ odd},\\
\operatorname{span}(U_0,\ldots,U_{q-3},U_{q-2}+U_{q-1}),
&q\text{ even}.
\end{cases}
\tag{5.2}
$$



### 5.1 The common finite convolution

Use


$$
C_d(Y)=(a(Y)b(Y))^d\in\mathbb F_2[Y].
$$


Its constant term is $1$, so multiplication by $C_d$ is an invertible triangular transformation on the first $2L$ parity coordinates.

This is only a rank-preserving transformation of the finite parity matrix. It is not an integer operation on the corrected pencil.

From (3.7), because the original $d$ is even,


$$
\boxed{
\begin{aligned}
C_dU_{2h}
&=\operatorname{Tr}\!\left(
\omega^{2d+2h+1}\frac{b^{2d+1}}{a^{2h+2}}
\right),\\
C_dU_{2h+1}
&=\operatorname{Tr}\!\left(
\omega^{2d+2h}\frac{b^{2d}}{a^{2h+2}}
\right).
\end{aligned}}
\tag{5.3}
$$



Since


$$
a^{2L}\equiv b^{2L}\equiv1\pmod{Y^{2L}},
$$


we may reduce $d=2L+\rho$ at this finite precision.

### 5.2 Clearing both denominators

Every combination from $R_{p+1}$ has the form


$$
\operatorname{Tr}\!\left(\frac{b^{2\rho}Q}{a^p}\right),
\qquad \deg Q\le p-1,
\tag{5.4}
$$


with binary coefficient restrictions described below.

A hypothetical equality with $C_dS_p$ gives


$$
b^pN+a^pN^\sigma=0\pmod{Y^{2L}),
\tag{5.5}
$$


where the closing parenthesis in this congruence means reduction modulo $Y^{2L}$, and


$$
N=
\begin{cases}
b^{2\rho}Q+\omega^{2p}a^\rho b^{\rho+p-1},
&p\text{ odd},\\
b^{2\rho}Q+\omega^{2p+1}a^{\rho-2}b^{\rho+p+1},
&p\text{ even}.
\end{cases}
\tag{5.6}
$$


Equivalently, without typographical shorthand,


$$
b^pN+a^pN^\sigma\equiv0\pmod{Y^{2L}}.
$$



Both denominators $a^p$ and $b^p$ have been cleared. In either parity,


$$
\deg(b^pN+a^pN^\sigma)\le2\rho+2p-1\le2L-1.
$$


Therefore the congruence is an exact polynomial identity.

At the root of $a$, $b$ is a unit. Hence $a^p\mid N$. The unique possible degree-$\le p-1$ numerator is


$$
\boxed{
Q_0=
\begin{cases}
\omega^{2p}a^\rho b^{p-\rho-1},&p\text{ odd},\\
\omega^{2p+1}a^{\rho-2}b^{p-\rho+1},&p\text{ even}.
\end{cases}}
\tag{5.7}
$$


Indeed, this candidate makes $N=0$, and $Q-Q_0$ would otherwise be divisible by $a^p$ while having degree less than $p$.

The even candidate follows directly from the **full even kernel**:


$$
C_dS_p
=\operatorname{Tr}\!\left(
\omega^{2p+1}a^{d-p-2}b^{d+p+1}
\right).
$$


After finite exponent reduction and multiplication by $a^p$, its contribution to $N$ is exactly


$$
\omega^{2p+1}a^{\rho-2}b^{\rho+p+1}.
$$


Thus the admitted exponent $\rho-2$ is correct.

### 5.3 Odd $p$: the extra tied source row

Let $p=2m_c+1$. The old paired rows have numerator


$$
Q_{\rm old}
=\omega^{2d}\sum_{h=0}^{m_c-1}
\omega^{2h}
(c_{{\rm odd},h}+c_{{\rm even},h}\omega b)
a^{2(m_c-h-1)},
\tag{5.8}
$$


where all $c$'s lie in $\mathbb F_2$.

The extra row in $R_{p+1}$ is


$$
U_{p-1}+U_p.
$$


Using $\omega b+1=\omega^2a$, (5.3) gives


$$
C_d(U_{p-1}+U_p)
=\operatorname{Tr}\!\left(
\omega^{2d+p+1}\frac{b^{2d}}{a^p}
\right).
$$


Hence


$$
Q=aQ_{\rm old}+c_{\rm new}\omega^{2d+p+1}.
\tag{5.9}
$$



The candidate $Q_0=\omega^{2p}a^\rho b^{p-\rho-1}$ vanishes at the root of $a$, so (5.9) forces $c_{\rm new}=0$. The remaining candidate is


$$
Q_{{\rm old},0}
=\omega^{2p}a^{\rho-1}b^{p-\rho-1}.
$$



Put


$$
A=a^2,\qquad
B=b^2=\omega(1+\omega A),
$$




$$
s=\frac{\rho-2}{2},\qquad
t=\frac{p-\rho-1}{2}=m_c-\frac\rho2.
$$


Then


$$
Q_{{\rm old},0}
=\omega^{2p+t}aA^s(1+\omega A)^t.
$$



The decomposition


$$
\mathbb F_4[Y]=\mathbb F_4[A]\oplus Y\mathbb F_4[A]
$$


is unique. Thus “the coefficient of $YA^s$” is unambiguous. In the candidate it is


$$
\omega^{2p+1+t}.
$$


In the allowed space (5.8), it must equal


$$
\omega^{2d+2t}c_{{\rm even},t}.
$$


Their ratio is


$$
\omega^{2p+1-2d-t}
=\omega^{\rho/2-2d}
=\omega^{-L}.
$$


A dyadic $L$ is nonzero modulo $3$, so $\omega^{-L}\notin\mathbb F_2$. This is impossible.

The earlier odd-only exclusion from $R_p$ uses the same coefficient obstruction without the extra row. Its weaker hypothesis $\rho\ge2$ suffices there.

### 5.4 Even $p$: both atom positions retained

Let $p=2m_c$. Then $R_{p+1}$ consists of the first $p$ contact rows, and


$$
Q=\omega^{2d}\sum_{h=0}^{m_c-1}
\omega^{2h}
(c_{{\rm odd},h}+c_{{\rm even},h}\omega b)
a^{p-2h-2}.
\tag{5.10}
$$



The candidate is


$$
Q_0=\omega^{2p+1}a^{\rho-2}b^{p-\rho+1}.
$$


Put


$$
s=\frac{\rho-2}{2},\qquad
t=\frac{p-\rho}{2}=m_c-\frac\rho2.
$$


Because $p$ is even and $p\ge\rho+1$, in fact $p\ge\rho+2$, so $t\ge1$. Now


$$
Q_0=\omega^{2p+1+t}bA^s(1+\omega A)^t.
$$


Its $YA^s$-coefficient is $\omega^{2p+t}$. The allowed coefficient in (5.10) is


$$
\omega^{2d+2t}c_{{\rm even},t}.
$$


Again the ratio is


$$
\omega^{2p-2d-t}
=\omega^{\rho/2-2d}
=\omega^{-L}\notin\mathbb F_2.
$$


The indicated paired row is in range: $\rho\ge4$ gives $t\le m_c-2$.

This proves the even exclusion without deleting either tied atom position in $R_p$.

### 5.5 Ranks, nesting, and the parity-dependent cutoff

If $p$ is even, the rank of $R_{p+1}$ uses the first $p$ contact rows, and


$$
\rho+p\le L
$$


is the required rectangular cutoff.

If $p$ is odd, $R_{p+1}$ uses rows through $U_p$, so one needs the first $p+1$ contact rows. Here $\rho+p$ is odd and $L$ is even; hence


$$
\rho+p\le L\quad\Longrightarrow\quad
\boxed{\rho+p+1\le L.}
$$


This additional unit of cutoff is paid, not rounded away.

The rectangular theorem therefore gives


$$
\dim R_p=p-1,\qquad \dim R_{p+1}=p.
$$


Moreover,


$$
R_p\subset R_{p+1}.
$$


At an odd-to-even step the new row is a sum of the next two ordinary rows; at an even-to-odd step that sum lies in the two ordinary rows replacing it.

We have proved


$$
\boxed{S_p\notin R_{p+1}}
$$


at both parities.

**Verdict: PASS**, including the finite degree cutoff, both denominator clearings, root candidate, binary coefficient obstruction, extra odd-$p$ row, and even-$p$ atom tie.

---

## 6. Audit of the complete attaining compound and the equality scalar

A lower cost need not be attained. This section checks the full leading determinant, including all prefactors.

### 6.1 Exact source normalization at the minimal top rows

Let


$$
I_p=\{d-p,\ldots,d-1\},\qquad n_p=d-p,
\qquad S_j^{\rm rise}=(d+1)_j.
$$


For an atom and $p-1$ returns, finite difference transformation on these consecutive top rows gives the exact identity


$$
\frac{\det A_S[I_p,:]}{\mathcal B_p(d)}
=
\sum_{j=0}^{p-1}
(-1)^j A_j(n_p)
\frac{S_{p-1}^{\rm rise}}{S_j^{\rm rise}}
\det U^{\mathbb Z}[\{0,\ldots,p-1\}\setminus\{j\},S_{\rm ret}].
\tag{6.1}
$$



Let


$$
O_p=\mathcal B_p(d)/2^{B_p(d)},\qquad
\vartheta_p=(-1)^{p-1}O_pA_{p-1}(n_p).
$$


This is an actual odd integer.

- If $p$ is odd, only $j=p-1$ survives at the minimal binary depth.
- If $p$ is even, precisely $j=p-2,p-1$ survive.

In the even case the two surviving terms can be represented over $\mathbb Z_{(2)}$ by the last row


$$
U^{\mathbb Z}_{p-2,\bullet}(n_p)
-\zeta_pU^{\mathbb Z}_{p-1,\bullet}(n_p),
\qquad
\zeta_p=
\frac{(d+p-1)A_{p-2}(n_p)}{A_{p-1}(n_p)}.
\tag{6.2}
$$


The ratio $\zeta_p$ is an explicitly specified odd unit. It reduces to $1$, giving the required sum of the two rows over $\mathbb F_2$.

Thus the source factor is not assumed odd for every return subset. Its complete leading parity is the appropriate determinant of $R_p$, multiplied by the derived odd prefactor $\vartheta_p$.

### 6.2 Actual minimal $N_d$-minor

Write


$$
\xi_n=\frac{h_d/(2n)!}{2^{e_n}},
\qquad
K_t^{\rm lead}=\det K_d[\{0,\ldots,t-1\},\{0,\ldots,t-1\}],
$$


with $K_0^{\rm lead}=1$.

Jacobi’s complementary-minor identity gives


$$
\boxed{
\frac{\det N_d[I_p,I_p]}{2^{2E_p}}
=
\mathfrak n_p:=
\left(\prod_{n\in I_p}\xi_n^2\right)
(\eta_d^F)^{p-1}K_{d-p}^{\rm lead}.
}
\tag{6.3}
$$


Every displayed factor is an actual odd integer.

Because the $e_n$ strictly decrease, every other pair of $p$-index sets costs at least one extra binary power. This is the unique minimum, not merely an available principal minor.

### 6.3 Exact Cauchy and Newton prefactor

For the first $n=p+h$ residual rows


$$
M_n=\{0,\ldots,n-1\}
$$


and $p$ minimal Cauchy poles $I_p$, the exact mixed Cauchy identity has prefactor


$$
\frac{\Lambda_k^p\,2^{p(p-1)}\Phi_p^2}
{\prod_{i=0}^{n-1}Q_{I_p}(i)},
\qquad
\Phi_p=\prod_{j=0}^{p-1}j!.
$$


After its binary part $2^{c_p}$ is extracted, the remaining unit is


$$
\boxed{
\mathfrak c_{p,n}
=
\frac{\Lambda_k^p\operatorname{odd}(\Phi_p)^2}
{\prod_{i=0}^{n-1}Q_{I_p}(i)}
\in\mathbb Z_{(2)}^\times.
}
\tag{6.4}
$$


The odd denominators remain displayed.

On these consecutive residual rows, the Newton transformation is finite and determinant one. The polynomial columns become the first $p$ coordinate columns. The remaining determinant is exactly the determinant of the jets


$$
\Delta^{p+z}(Q_{I_p}W_r)(0),\qquad 0\le z<h.
$$


Extracting their full divisors gives


$$
\prod_{j=p}^{n-1}2^jj!,
$$


and their normalized parity is


$$
U_p(0,\bullet),\ldots,U_p(h-1,\bullet).
$$



### 6.4 Full leading Laplace stack

For a fixed selected set of $n-1$ original returns, summing over which $h$ returns lie in $W$ is precisely the Laplace expansion of


$$
\boxed{
[R_p;U_p(0,\bullet);\ldots;U_p(h-1,\bullet)].
}
\tag{6.5}
$$


There is no extra $h!$: each subset occurs once in the determinant expansion.

The signs agree with the Laplace signs. The atom is the first selected column; grouping the product returns before the $W$ returns induces exactly the same permutation as grouping the corresponding columns in the row-stack determinant.

The actual leading prefactor is represented by


$$
\boxed{
\mathfrak u_{p,n}
=
\gamma_k^h\,
\mathfrak c_{p,n}\,
\mathfrak n_p\,
\vartheta_p
\prod_{j=p}^{n-1}\operatorname{odd}(j!).
}
\tag{6.6}
$$


It is a specified odd unit, independent of which return subset supplies the $W$-columns.

All the following have now been accounted for:

- the actual $\gamma_k$;
- the complete Cauchy denominator product;
- the minimal $N_d$-minor and its complementary $K_d$-determinant;
- the full source division;
- the atom coefficient;
- both even-source atom positions;
- every odd factorial factor in the bottom Newton division.

Every nonminimal $N_d$-term is higher. Every omitted atom row in (6.1) is higher. Other correction patterns are higher under (4.5) and the strict cost comparison.

### 6.5 Strict first transition

Let $q=p+1$ and suppose


$$
D_p<L_d<D_q.
$$


The unique minimum class has $p$ product columns and one $W$-return. Its normalized leading determinant is


$$
\mathfrak u_{p,q}\det[R_p;S_p].
$$


By Section 5, this stack has rank $p$. Some $p$ original return columns therefore attain the complete depth


$$
\boxed{
F_q(p)=L_d+c_p+2E_p+B_p+\lambda_p.
}
\tag{6.7}
$$



This is the whole leading compound, not an isolated correction summand.

### 6.6 Equality: an explicit relative unit

Now suppose


$$
D_q=L_d,\qquad q=p+1.
$$


The two minimum classes are:

- the pure $q$-product contribution;
- the one-$W$, $p$-product contribution.

Their common depth is


$$
F_q(p)=F_q(q)=\Theta_q.
$$



To make the relative normalization explicit, put


$$
\ell_i=2(2d+i-q)+1,\qquad 0\le i<q.
$$


Using (6.3)–(6.6), one obtains


$$
\boxed{
\frac{\mathfrak u_{p,q}}{\mathfrak u_{q,q}}
=
-\frac{
\gamma_k
\left(\prod_{i=0}^{q-1}\ell_i\right)
K_{d-p}^{\rm lead}A_{p-1}(d-p)}
{
\Lambda_k\operatorname{odd}(p!)
\,\xi_{d-q}^{\,2}\eta_d^F
K_{d-q}^{\rm lead}
\operatorname{odd}((d+1)_{p-1})
A_p(d-q)
}.
}
\tag{6.8}
$$


This is an actual odd unit in $\mathbb Z_{(2)}$, not an arbitrary relative scalar.

The actual $\gamma_k$ is visible here. In fact,


$$
\frac{\gamma_k}
{\Lambda_k\eta_d^F\xi_{d-q}^{\,2}}
=\operatorname{odd}((2(d-q))!)^2,
$$


so every factor in (6.8) is explicitly odd. Its reduction is therefore $1$.

This calculation concerns the relative **leading prefactors**. The normalized source minors themselves remain the determinants appearing in the Laplace stack; they have not individually been assigned odd value.

Choose


$$
v_{\rm new}=
\begin{cases}
U_{p-1}+U_p,&p\text{ odd},\\
U_{p-1},&p\text{ even}.
\end{cases}
$$


Then


$$
R_q=\operatorname{span}(R_p,v_{\rm new}),
$$


and the indicated basis change has determinant one over $\mathbb F_2$. Therefore the complete normalized sum is


$$
\boxed{
\det[R_p;v_{\rm new}]
+\det[R_p;S_p]
=
\det[R_p;v_{\rm new}+S_p].
}
\tag{6.9}
$$



Because $S_p\notin R_q$, the last row in (6.9) is not in $R_p$. The combined stack has rank $p$, and some $p$ original return columns attain the tied depth.

**Verdict: PASS.** The equality claim is justified by the exact normalizations, not by a summand-rank argument or an assumed relative sign.

---

## 7. The explicit infinite original subfamily

Use the same original interval


$$
\boxed{
\frac98\,2^a<k<\frac76\,2^a,
\qquad
a=\lfloor\log_2k\rfloor,
\qquad
L=2^{a-1}.
}
\tag{7.1}
$$


Then


$$
d=2L+\rho,\qquad
\frac L4-1<\rho<\frac L3-1.
\tag{7.2}
$$



All original indices are already enormous. In particular,


$$
9^{18}>2^{54},
$$


so $m=m_d\ge55$, $L=2^{m-2}$, and elementary inequalities such as


$$
L>3m+9,\qquad d>5m+20
$$


hold throughout the original domain.

Because $2L$ is divisible by $32$ and $v_2(d)=4$,


$$
\rho\equiv16\pmod{32}.
$$


Thus $\rho\ge16$ and is even.

Using (4.10),


$$
p-\rho
>\frac{L-m-1}{4},
$$


so $p\ge\rho+1$. Also,


$$
\rho+p+1
<
\frac{11L}{12}+\frac m4+\frac34
<L.
$$


Hence both parity-dependent rectangular cutoffs are satisfied with slack.

For later use, let $n=p+2$. Again by (4.10),


$$
4n\le d+m+12,
$$


and therefore


$$
\alpha-2-4n\ge d-2m-14>0.
$$


Likewise,


$$
d-2n+1-2m
\ge\frac d2-\frac{5m}{2}-5>0.
$$


Thus the factorial and atom exclusions hold not only at the first transition but also one size beyond it.

Finally,


$$
(18+32u)\log_2 9
$$


is an irrational rotation modulo $1$, since unique prime factorization implies $\log_2 9\notin\mathbb Q$. Every tail hits the nonempty open interval corresponding to (7.1). Therefore (7.1) contains infinitely many original indices.

No parity condition on $p$, and no distribution assumption concerning equality $D_{p+1}=L_d$, is imposed.

**Verdict: PASS.** The infinite subfamily is genuinely original and requires no conjectural filter. The old $u=0$ digit receipt is neither needed nor rerun.

---

## 8. New theorem: two mixed return directions beyond the source space

This section is a new proved result, not part of the independent audit of the parent notes.

Let


$$
J_p=U_p(1,\bullet).
$$



### Theorem 8.1

Under (5.1),


$$
\boxed{
\operatorname{rank}_{\mathbb F_2}
[R_{p+1};S_p;J_p]=p+2
}
\tag{8.1}
$$


on the first $2L$ original return columns.

Thus $S_p$ and $J_p$ are jointly independent modulo $R_{p+1}$, at both parities of $p$.

### Proof

Suppose


$$
\alpha_0S_p+\beta_0J_p\in R_{p+1},
\qquad \alpha_0,\beta_0\in\mathbb F_2.
$$


We show $\alpha_0=\beta_0=0$.

From (3.7)–(3.8),


$$
J_p(Y)=
\begin{cases}
\displaystyle
\operatorname{Tr}\!\left(
\omega^{2p}\frac{b^{p-1}Y(1+Y)}{a^{p+3}}
\right),&p\text{ odd},\\[3mm]
\displaystyle
\operatorname{Tr}\!\left(
\omega^{2p}\frac{b^p}{a^{p+2}}
\right),&p\text{ even}.
\end{cases}
\tag{8.2}
$$



After multiplication by the same $C_d$, both denominator clearings, and the same root argument as in Section 5, the unique possible numerator $Q$ is as follows.

#### Even $p=2m_c$

Put


$$
s=\frac{\rho-2}{2},\qquad t=\frac{p-\rho}{2}.
$$


The candidate is


$$
Q_{\alpha_0,\beta_0}
=
a^{\rho-2}b^{p-\rho}
\left(\alpha_0\omega^{2p+1}b+\beta_0\omega^{2p}\right).
\tag{8.3}
$$


Its degree is at most $p-1$, and the cleared polynomial has degree at most $2\rho+2p-1<2L$, exactly as before.

If $\alpha_0=1$, its $YA^s$-coefficient is the same obstructed coefficient as for $S_p$. The $\beta_0$-term is a polynomial in $A$, so it cannot alter that coefficient. The ratio to the allowed binary coefficient is $\omega^{-L}$, a contradiction.

Thus $\alpha_0=0$. If $\beta_0=1$, the candidate becomes


$$
\omega^{2p+t}A^s(1+\omega A)^t.
$$


It has no $Y$-part. Therefore all allowed coefficients $c_{{\rm even},h}$ must vanish. Its $A^s$-coefficient would then have to equal


$$
\omega^{2d+2t}c_{{\rm odd},t}.
$$


The ratio is again


$$
\omega^{2p-2d-t}=\omega^{-L}\notin\mathbb F_2.
$$


So $\beta_0=0$.

#### Odd $p=2m_c+1$

The candidate is


$$
Q_{\alpha_0,\beta_0}
=
\omega^{2p}a^{\rho-3}b^{p-\rho-1}
\left(\alpha_0a^3+\beta_0Y(1+Y)\right).
\tag{8.4}
$$


Here $\rho\ge4$ is essential: the candidate vanishes at the root of $a$. The extra tied source-row coefficient in (5.9) is therefore zero.

After division by $a$, put


$$
s_1=\frac{\rho-4}{2},\qquad
t=\frac{p-\rho-1}{2}.
$$


The $\beta_0$-part is


$$
\beta_0\omega^{2p+t}
A^{s_1}(1+\omega A)^tY(1+Y).
$$


If $\beta_0=1$, its $YA^{s_1}$-coefficient is


$$
\omega^{2p+t}.
$$


The $\alpha_0$-part begins at $A^{s_1+1}$ and cannot change this coefficient.

The relevant allowed paired row is $h=t+1$, which lies in range because $\rho\ge4$. Its allowed coefficient is


$$
\omega^{2d+2(t+1)}c_{{\rm even},t+1}.
$$


Their ratio is


$$
\omega^{2p-2d-t-2}
=\omega^{\rho/2-2d}
=\omega^{-L}\notin\mathbb F_2.
$$


Thus $\beta_0=0$. The remaining $\alpha_0=1$ case is precisely the already proved odd $S_p$-obstruction, so $\alpha_0=0$.

This proves joint independence. Since $\dim R_{p+1}=p$, (8.1) follows. ∎

No growing determinant computation is used. The proof works in the original finite coordinate space and uses the full odd/even $U_p$-kernel.

---

## 9. New complete cofactor attainment one size beyond the first transition

Let $p$ be defined by (4.8), and now take


$$
n=p+2.
$$


Assume the exclusions (4.5) at this size and the rank hypotheses (5.1). Section 7 verifies all of them on the explicit infinite original subfamily.

### 9.1 Strict crossing

If


$$
D_{p+1}>L_d,
$$


the unique minimum at size $n$ still has $p$ product columns. It has two $W$-returns.

By the fully normalized compound formula of Section 6, its leading stack is


$$
[R_p;S_p;J_p].
$$


Theorem 8.1 implies that this stack has rank $p+1$. Therefore some $p+1$ original return columns, together with the atom, attain


$$
\boxed{
F_{p+2}(p)
=
2L_d+c_p+2E_p+B_p+\lambda_p+\lambda_{p+1}.
}
\tag{9.1}
$$



All other product counts, factorial patterns, atom-in-$W$ patterns, and nonminimal $N_d$-terms are strictly higher.

### 9.2 Equality at the first crossing

Suppose


$$
D_{p+1}=L_d.
$$


At size $p+2$, the minimum counts are now

- $p$ products and two $W$-returns;
- $p+1$ products and one $W$-return.

A direct consequence of (3.5) is the parameter recursion


$$
\boxed{
U_{e+1}(z,r)=U_e(z,r)+U_e(z+1,r).
}
\tag{9.2}
$$


It is simply Pascal’s identity in the auxiliary binomial filter. In particular,


$$
S_{p+1}=S_p+J_p.
\tag{9.3}
$$



The two complete leading contributions are therefore


$$
\det[R_p;S_p;J_p]
$$


and


$$
\det[R_p;v_{\rm new};S_p+J_p].
$$


Their normalized prefactors are again the actual odd units (6.6). Their relative unit is obtained from the same calculation as (6.8), with the row product now running over $0\le i<p+2$; hence both reduce to $1$.

By multilinearity over $\mathbb F_2$, their sum is


$$
\boxed{
\det[R_p;S_p+v_{\rm new};J_p+v_{\rm new}].
}
\tag{9.4}
$$


Theorem 8.1 shows that the last two rows are independent modulo $R_p$: any relation between them would place a nonzero combination of $S_p,J_p$ in $R_{p+1}$.

Thus (9.4) has rank $p+1$, and some $p+1$ original returns attain the same depth (9.1).

### 9.3 An attaining original-column flag through the two new sizes

The cost analysis also shows that for every size $j\le p$, the unique minimum is pure. Under the rectangular cutoffs, $R_j$ has rank $j-1$, so the complete cofactor depth is $\Theta_j$.

The row spaces are nested up to $R_p$. At the first transition the relevant space is

- $R_p+\langle S_p\rangle$ in the strict case;
- $R_p+\langle S_p+v_{\rm new}\rangle$ in the equality case.

At the next size it is extended respectively by

- $J_p$;
- $J_p+v_{\rm new}$.

Consequently, coordinate-basis extension gives a nested set of **original** return columns through these two mixed sizes. It can begin with the already established columns


$$
1,0,5,4.
$$


No transformed parity column is installed in the integer pencil, and no selection algorithm or original-sized solve is proposed.

We have therefore proved, on the same infinite original subfamily:

- pure attaining cofactors through the exact pretransition size $p$;
- the first complete mixed attaining cofactor at size $p+1$;
- a further complete mixed attaining cofactor at size $p+2$, including equality cancellation.

This is stronger than merely restating the lower bound beyond the quarter window.

---

## 10. A paid Cramer consequence retaining both full borders

The new attaining common cofactor gives a legitimate arithmetic consequence, but not a terminal upper bound.

Let $n=p+2$, and let


$$
t_n=F_n(p).
$$


Choose the attaining $n$ common columns from Section 9 and their first $n$ residual rows. Write


$$
\det\Pi_{n,k}=2^{t_n}\mu_{n,k},
\qquad \mu_{n,k}\ \text{odd}.
$$


This is the actual complete cofactor; $\mu_{n,k}$ is not assigned value $1$.

Every $n$-minor of these selected common columns is divisible by $2^{t_n}$, by the full mixed lower-payment theorem on arbitrary residual row sets. If $V_{n,k}$ is the block of their remaining rows, then


$$
M_{n,k}=\frac{V_{n,k}\operatorname{adj}(\Pi_{n,k})}{2^{t_n}}
$$


is integral.

Define


$$
\mathcal E_n=[-M_{n,k}\mid\mu_{n,k}I].
$$


Then


$$
\mathcal E_n\mathcal C^{[n]}=0.
$$


There is no division by the odd cofactor in this row numerator.

For the remaining columns set


$$
\mathcal P_k^{\langle n\rangle}(s)
=\mathcal E_n\mathcal Q_{k,\rm remaining}(s).
$$


No unproved further division by $2$ is made.

Both full borders remain exactly


$$
\boxed{
\mathcal E_n\mathfrak b_\varepsilon
=
(\mathcal E_nR)N_d\Lambda_k(\mathcal A_d\psi_\varepsilon)_{\rm top}
+
2^{L_d+\alpha}\gamma_k\Lambda_k
\mathcal E_n(\psi_\varepsilon)_{\rm bot}.
}
\tag{10.1}
$$


Thus the constant border still contains $-f+4\rho$, the linear border still contains $w$, and both pass through the same integral row numerator.

Let $g_k^{\langle n\rangle}$ be the actual all-prime gcd of the two determinant coefficients of this new residual pencil. The block determinant identity gives, up to a common sign,


$$
2^{t_n}\det\mathcal P_k^{\langle n\rangle}(s)
=
\mu_{n,k}^{\,d+1-n}\det\mathcal Q_k(s).
\tag{10.2}
$$


This identity holds coefficientwise in $s$.

The already paid five-column relation is


$$
2^{d+69}\det\mathcal P_k^{[5]}(s)
=
\mu_{5,k}^{\,d-4}\det\mathcal Q_k(s).
$$


Taking all-prime coefficient gcds gives the exact common-normalization identity


$$
\boxed{
2^{t_n}|\mu_{5,k}|^{d-4}g_k^{\langle n\rangle}
=
2^{d+69}|\mu_{n,k}|^{d+1-n}g_k^{[5]}.
}
\tag{10.3}
$$



Combining this with (1.1) yields a new paid transfer:


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_{n,k}|^{d+1-n}G_k
=
|f_k|\,2^{\lambda_{\rm tr}+t_n}
\mathfrak D_d\,g_k^{\langle n\rangle}.
}
\tag{10.4}
$$



Every factor in this identity is the actual integer factor. In particular:

- the old return divisions remain in $\mathfrak D_d$;
- the forcing and top-row payments remain in $f_k,\delta_k,\Omega_k$;
- the new odd Cramer cofactor is retained;
- the gcd is the joint all-prime gcd of the two complete coefficients.

Equation (10.4) is a **paid cofactor consequence**, not an upper bound for $g_k^{\langle n\rangle}$ or $G_k$.

Because both coefficients have undergone the same exact scalar transfer,


$$
\frac{|P_{1,k}^{\langle n\rangle}|}{g_k^{\langle n\rangle}}
=\frac{|H_{1,k}|}{G_k}=q_k,
$$


and


$$
\boxed{
\frac{|P_{0,k}^{\langle n\rangle}
+(e+\pi)P_{1,k}^{\langle n\rangle}|}
{g_k^{\langle n\rangle}}
=
\frac{|H_k(e+\pi)|}{G_k}
=\ell_k>0.
}
\tag{10.5}
$$


The primitive denominator and whole evaluated error have not changed.

---

## 11. Audit and proof-status ledger

| Claim or dependency | Status |
|---|---|
| Previously audited A2 turn 13 source payments, finite Newton theorem, rectangular rank, and quarter-window premises | Reused at their stated scope |
| Full normalized jets of the actual $Q_IW_r$ columns | **PASS: independently derived** |
| Auxiliary Cauchy count distinguished from original $d$ | **PASS; essential distinction** |
| Both-parity joint kernel | **PASS** |
| Odd derivative term | **PASS; indispensable** |
| Simplified odd and even $S_p$ generating rows | **PASS** |
| Exact lower costs $F_q(p)$ | **PASS** |
| Factorial exclusion $\alpha-2>4q$ | **PASS at its stated strict scope** |
| Atom exclusion, including $p=0$ | **PASS** |
| Digit formula $D_p$ and strict monotonicity | **PASS** |
| $O(\log d)$ binary-search evaluations | **PASS** |
| Unqualified $O(\log d)$ bit-operation claim | **REPAIR: specify a word model, or use a larger bit bound** |
| Earlier odd $S_p\notin R_p$ lemma | **PASS at its original hypotheses** |
| Both-parity $S_p\notin R_{p+1}$ | **PASS** |
| Both denominator clearings and exact degree cutoff | **PASS** |
| Correct even candidate $a^{\rho-2}b^{p-\rho+1}$ | **PASS** |
| Extra tied row at odd $p$ | **PASS; explicitly retained** |
| Two atom positions at even $p$ | **PASS; explicitly retained** |
| $R_p\subset R_{p+1}$, ranks, and parity-dependent cutoff | **PASS** |
| Strict one-$W$ complete leading Laplace stack | **PASS** |
| Equality tie, including relative odd prefactors | **PASS: formula (6.8)** |
| Infinite original subfamily without parity/equality filter | **PASS** |
| Joint independence of $U_p(0)$ and $U_p(1)$ modulo $R_{p+1}$ | **New proved theorem** |
| Complete attainment at size $p+2$, strict and tied cases | **New proved theorem** |
| Paid two-border Cramer transfer (10.4) | **New proved consequence** |
| Different audit of A4 turn 22’s new rank-one perturbation and border-difference result | Still separate; not supplied by this report |
| Different audit of turn 21’s all-order similarity theorem | Still separate; not used |
| Joint terminal coefficient upper and all-prime global control | **Open** |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

---

## 12. Exact remaining bottleneck and computation scope

### 12.1 What has advanced

The first transition is no longer only a lower-cost prediction. The complete attaining compound, including its equality cancellation, is proved.

The new two-return theorem advances the complete attaining original-column flag one further size:


$$
n=p+2,\qquad p=\frac d4+O(\log d),
$$


with exact depth (9.1), on the same explicit infinite original subfamily. Formula (10.4) also shows how this new common cofactor can be used without dropping either coefficient border or changing the all-prime normalization.

### 12.2 What remains mathematically unproved

The immediate growing problem is now the higher mixed coupling


$$
[R_p;U_p(0,\bullet),U_p(1,\bullet),\ldots]
$$


and its tied counterpart, beyond the two bottom rows evaluated here.

While the strict exclusions remain valid, higher-order attainment requires actual independence of the additional $U_p$-rows, not merely the cost minimum. When those exclusions fail, factorial columns and atom-in-$W$ patterns can enter the minimum, and the relevant bottom parameter is $a=p-v$, possibly odd. The full kernel derived above is then required.

At terminal size, the exact rank obstruction remains:


$$
\operatorname{rank}(RN_d\mathcal A_k)\le d.
$$


Therefore a $(d+1)$-common-column minor must use a bottom correction, and a full $(d+2)$-column coefficient determinant must use at least two. The two complete borders must be evaluated together through the same paid normalization; a unit in one auxiliary stack does not bound their joint gcd.

The unresolved binary target remains


$$
\boxed{
\nu_k^{[5]}
\le \frac{15}{4}k^2-64+O(k\log k).
}
$$


Neither (9.1) nor (10.4) proves it. Independent odd-prime descent and large-prime obligations also remain.

### 12.3 Bounded calculations

No tools have been used.

No original-sized array, source table, determinant scan, vector solve, old fixed-cofactor calculation, quarter-window calculation, phase check, or $u=0$ digit receipt is proposed or repeated.

No bounded numerical calculation is indispensable to the proofs in this report. The new two-return rank theorem and both tie evaluations are symbolic finite-field and determinant identities with all inputs and normalizations displayed above. Consequently, there is no new computation request for the coordinator to author.

A finite check of selected entries would authenticate only those entries; it would not establish the growing rank theorem, terminal gcd bound, or global objective.

---

## Final conclusion

The three new parent mixed notes are mathematically valid at their exact hypotheses, apart from the stated complexity-language repair. In particular, the stronger both-parity nonmembership lemma and the complete equality-tie attainment survive an independent audit that retains both unit denominators, the physical finite cutoffs, both atom positions where they tie, and the actual relative Cauchy–Newton–source–adjugate–$\gamma_k$ prefactors.

The new result is


$$
\boxed{
\operatorname{rank}[R_{p+1};U_p(0,\bullet);U_p(1,\bullet)]=p+2,
}
$$


which proves complete cofactor attainment at size $p+2$, one size beyond the first mixed transition, in both the strict and equality cases. This holds on the explicit infinite original subfamily


$$
\frac98\,2^{\lfloor\log_2k\rfloor}
<k<
\frac76\,2^{\lfloor\log_2k\rfloor},
\qquad k=9^{18+32u},
$$


without a parity or equality-distribution filter.

The resulting cofactor has a fully paid two-border transfer, but the joint terminal coefficient depth and the all-prime final gcd remain unbounded in the required direction. The actual primitive denominator and nonzero whole error are still


$$
q_k=\frac{|H_{1,k}|}{G_k},
\qquad
0<\ell_k=\frac{|H_k(e+\pi)|}{G_k}
$$


at those same original indices.

Accordingly, the unconditional rationality or irrationality of $e+\pi$ remains unresolved.
