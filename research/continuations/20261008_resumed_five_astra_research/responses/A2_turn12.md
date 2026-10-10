> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A short, fully paid cofactor recursion for the original Newton–Cauchy pencil

## 1. Result and proof status

The rationality or irrationality of $e+\pi$ remains unresolved. I do **not** prove the requested upper bound


$$
\nu_k\le \frac{15}{4}k^2+O(k\log k).
$$



I do prove three further, source-specific cofactor evaluations in the **complete paid pencil** of turn11. They give actual successive pivots of binary depths


$$
\boxed{13,\qquad 19,\qquad 32.}
$$



More precisely, retain the original paid columns:

* $x$: the first contact column;
* $y=z^{(1)}$: the weighted Newton contact-return column of order $1$;
* $z^{(0)}$, $z^{(5)}$, $z^{(4)}$: the actual weighted Newton columns of orders $0,5,4$.

The full divisors are used:


$$
D_r=2^rr!,\qquad D_0=1,\quad D_1=2,\quad
D_4=384,\quad D_5=3840.
$$


In particular, the odd parts of $D_4,D_5$ are not omitted.

For the nested complete common-source matrices


$$
\begin{aligned}
\mathcal C^{[2]}&=[x,y],\\
\mathcal C^{[3]}&=[x,y,z^{(0)}],\\
\mathcal C^{[4]}&=[x,y,z^{(0)},z^{(5)}],\\
\mathcal C^{[5]}&=[x,y,z^{(0)},z^{(5)},z^{(4)}],
\end{aligned}
$$


the actual maximal-minor contents satisfy


$$
\boxed{
v_2\bigl(\operatorname{content}_q(\mathcal C^{[q]})\bigr)
=
\begin{cases}
5,&q=2,\\
19,&q=3,\\
39,&q=4,\\
72,&q=5.
\end{cases}}
\tag{1.1}
$$


The $q=2$ result is established reuse. The other three values are proved below.

Each valuation is attained on the first $q$ residual physical rows. Moreover, for every increasing $q$-tuple $M=(i_0,\ldots,i_{q-1})$ of residual row indices,


$$
\boxed{
\frac{\det\mathcal C^{[q]}[M,:]}{2^{t_q}}
\equiv
\frac{\prod_{a<b}(i_b-i_a)}
     {\prod_{j=0}^{q-1}j!}
\pmod2,
\qquad
(t_3,t_4,t_5)=(19,39,72).
}
\tag{1.2}
$$


The quotient on the right is an integer.

These evaluations give three paid eliminations of the complete coefficient pencil. If $\mathcal P_k^{[2]}=\mathcal P_k$ is exactly the turn11 pencil, the resulting integer pencil $\mathcal P_k^{[5]}$ has size $(d-3)\times(d-3)$, retains every uneliminated common column and both coefficient borders, and satisfies


$$
\boxed{
\nu_k=64+\nu_k^{[5]},
\qquad
\nu_k^{[5]}
=
v_2\gcd\bigl(
|P_{0,k}^{[5]}|,\,
|P_{1,k}^{[5]}|
\bigr).
}
\tag{1.3}
$$



Equation (1.3) is an **exact evaluated payment, not an upper bound**. A fixed number of evaluated pivots cannot control the growing residual coefficient pair.

The turn10 construction and the turn11 paired theorem are reused at their stated mathematical scope. Their different full audits remain pending; nothing here declares those audits complete.

---

## 2. Original objects, domain and normalization

### 2.1 The unchanged infinite domain

Throughout,


$$
\boxed{
k=9^{18+32u},\qquad u\ge0,\qquad d=k-1.
}
\tag{2.1}
$$


Thus


$$
v_2(d)=4,\qquad d\equiv2\pmod3.
\tag{2.2}
$$


Every original $d$ is certainly at least $64$. This elementary lower bound is used below only to justify fixed-depth congruences; it does not replace the original domain.

Retain


$$
a_0=1,\qquad a_n=1-na_{n-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad
w_n=(-1)^n,\qquad c_n=u_n-w_n,
$$


and


$$
\rho_0=0,\qquad
\rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad r_n=-f_n+4\rho_n.
\tag{2.3}
$$



The complete returns are


$$
\sigma_n=u_{n+1}+u_n=c_{n+1}+c_n
$$


and


$$
\boxed{
\tau_n=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
\tag{2.4}
$$



Set


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),
\qquad
T_n=\Lambda_k\tau_n.
$$


Hence


$$
\boxed{
T_n
=
-\Lambda_k\bigl((2n+2)!+(2n)!\bigr)
+\frac{4\Lambda_k}{2n+1}.
}
\tag{2.5}
$$



The original determinant remains


$$
H_k(s)=
\det\left[
(c_{m+j})\
\middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right]
=H_{0,k}+H_{1,k}s,
\tag{2.6}
$$


with


$$
0\le m<2k,\qquad 0\le j<k.
$$



Its physical terminal is unchanged:


$$
\boxed{
\text{moment }3k-2,\qquad
\text{factorial }(6k-4)!,\qquad
\text{last odd denominator }6k-5.
}
\tag{2.7}
$$



### 2.2 Actual clearers, contents and primitive normalization

The individual least right-column entry clearers are


$$
\Lambda_{k,j}
=
\operatorname{lcm}(1,3,\ldots,4k+2j-3),
\qquad 0\le j<k,
\tag{2.8}
$$


and the common least entry clearer is $\Lambda_k$.

Retain the all-prime final gcd


$$
\boxed{G_k=\gcd(|H_{0,k}|,|H_{1,k}|).}
\tag{2.9}
$$


For the rational coefficient pair $H_k/\Lambda_k^k$, put


$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


Its actual least simultaneous coefficient clearer and subsequent content are


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
}
\tag{2.10}
$$



The actual original rectangles are


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
\tag{2.11}
$$


Write


$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
\mathscr L_k=\delta_{2k-1}(Y_k).
$$


The established interface is


$$
\boxed{
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k
\mid\Lambda_k\mathscr L_k\mathscr R_k.
}
\tag{2.12}
$$



At every original index, the accepted sign and nonvanishing results give


$$
q_k=\frac{|H_{1,k}|}{G_k}>0,
\qquad
p_k=-\frac{(-1)^kH_{0,k}}{G_k},
$$


and


$$
\boxed{
0<\ell_k
=q_k(e+\pi)-p_k
=\frac{|H_k(e+\pi)|}{G_k}.
}
\tag{2.13}
$$


These remain the actual primitive denominator and the nonzero whole evaluated error.

---

## 3. The paid pencil being continued

This section records the reused objects needed for the new derivations. It does not repeat the proofs of the weighted Newton divisions or of the depth-five pair.

### 3.1 Annihilator, forcing block and factorial adjugate

Define


$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1),
$$




$$
(\mathcal A_d y)_n
=
\sum_{i=0}^d(-1)^i\binom di P_d(n+i)y_{n+i}.
\tag{3.1}
$$


Since $d$ is even,


$$
\mathcal A_d y=\Delta^d(P_dy).
\tag{3.2}
$$



The row operation acts only on the first $d$ rows, and has determinant


$$
\Omega_k=\prod_{n=0}^{d-1}P_d(n),
\tag{3.3}
$$


an explicitly retained odd integer.

Put


$$
\mathfrak b(t)=4t^2+6t+3.
$$


The complete forcing block is


$$
F_k(n,j)
=
-\Lambda_k
\sum_{i=0}^d(-1)^i\binom di
P_d(n+i)\mathfrak b(n+i+j)(2(n+i+j))!,
\quad n,j<d.
\tag{3.4}
$$


Thus both factorial terms are retained.

With


$$
D_f=\operatorname{diag}((2n)!)_{n<d},
$$


write


$$
F_k=-\Lambda_kD_fK_dD_f.
$$


The reused congruence is


$$
K_d(n,j)\equiv\binom{n+j}{j}\pmod2.
\tag{3.5}
$$


Consequently $\eta_d=\det K_d$ and every leading principal determinant of $K_d$ are odd.

Retain


$$
f_k=(-\Lambda_k)^d\eta_d
\left(\prod_{n=0}^{d-1}(2n)!\right)^2,
\tag{3.6}
$$




$$
h_d=(2d-2)!,\qquad
\beta_d=v_2(h_d),\qquad
\alpha_d=v_2((2d)!),
$$




$$
\widehat D_f=h_dD_f^{-1},
\qquad
N_d=\widehat D_f\,\operatorname{adj}(K_d)\,\widehat D_f,
\qquad
\delta_k=\Lambda_k\eta_dh_d^2.
\tag{3.7}
$$


Then


$$
F_k^{-1}=-N_d/\delta_k,
\qquad
v_2(\delta_k)=2\beta_d,
\qquad
\alpha_d=\beta_d+5.
\tag{3.8}
$$



### 3.2 Complete bottom forcing and weighted contact columns

Residual row $i$, $0\le i<d+2$, is the original physical row


$$
m=d+i.
$$


Let $R=B/4$, where $B$ is the complete bottom forcing block. Exactly,


$$
\boxed{
R(i,j)
=
\frac{\Lambda_k}{2(d+i+j)+1}
-\frac{\Lambda_k}{4}
\mathfrak b(d+i+j)(2(d+i+j))!,
\quad j<d.
}
\tag{3.9}
$$



Set


$$
D_r=2^rr!,\qquad
\mathfrak D_d=\prod_{r=0}^{d-1}D_r,
\qquad
o_d=\operatorname{odd}(d!).
\tag{3.10}
$$


The complete weighted Newton divisions by every $D_r$ are established reuse.

Define the top source columns


$$
\mathsf a_n=\frac{(\mathcal A_dc)_n}{2^d},
\qquad
t_n^{(r)}
=
\frac{(\mathcal A_d\Delta^r\sigma)_n}
     {2^{\alpha_d+1}D_r},
\quad n<d,\quad r<d.
\tag{3.11}
$$


The exact corrected residual columns are


$$
\boxed{
x=RN_d\mathsf a+\frac{\delta_k}{2^{d+2}}c_{\rm bot},
}
\tag{3.12}
$$




$$
\boxed{
z^{(r)}
=
RN_dt^{(r)}
+
\frac{\delta_k}{2^{\alpha_d+3}D_r}
(\Delta^r\sigma)_{\rm bot}.
}
\tag{3.13}
$$


Thus $y=z^{(1)}$.

For the border, set $\psi_0=r,\ \psi_1=w$. Its two complete coefficient columns are


$$
\boxed{
\mathfrak b_j
=
\frac{\delta_k\Lambda_k}{4}(\psi_j)_{\rm bot}
+
RN_d\Lambda_k(\mathcal A_d\psi_j)_{\rm top},
\qquad j=0,1.
}
\tag{3.14}
$$


No part of $\Lambda_kr$ or of the literal $\Lambda_kw$ is omitted.

The turn11 pencil is therefore


$$
\mathcal Q_k(s)=
[x,z^{(0)},z^{(1)},\ldots,z^{(d-1)},\mathfrak b_0+s\mathfrak b_1].
\tag{3.15}
$$



Every column of $\mathcal Q_k(s)$, coefficientwise in $s$, is constant across its residual rows modulo $2$. This includes both columns in (3.14).

### 3.3 Reused pair and original remaining depth

The established pair theorem gives


$$
x_i\equiv1\pmod2,
$$




$$
32\mid x_i y_j-x_jy_i,
\qquad
\frac{x_i y_j-x_jy_i}{32}\equiv j-i\pmod2.
\tag{3.16}
$$


In particular,


$$
\Pi_{2,k}=\mathcal C^{[2]}[\{0,1\},:],
\qquad
\det\Pi_{2,k}=32\mu_k,
\qquad \mu_k\text{ odd}.
\tag{3.17}
$$



After putting $x,y$ first, partition


$$
\begin{pmatrix}\Pi_{2,k}&U_{2,k}(s)\\
V_{2,k}&C_{2,k}(s)\end{pmatrix},
$$


and define


$$
M_{2,k}=\frac{V_{2,k}\operatorname{adj}(\Pi_{2,k})}{32},
\qquad
\mathcal P_k(s)
=
\frac{\mu_kC_{2,k}(s)-M_{2,k}U_{2,k}(s)}2.
\tag{3.18}
$$


This is exactly the original turn11 integer pencil, not a substitute.

Its remaining common columns are all $d-1$ columns with return indices


$$
0,2,3,\ldots,d-1.
$$


Its last column is the complete affine border.

Write


$$
\det\mathcal P_k(s)=P_{0,k}+P_{1,k}s,
\qquad
g_k^{[2]}=\gcd(|P_{0,k}|,|P_{1,k}|),
\qquad
\nu_k=v_2(g_k^{[2]}).
\tag{3.19}
$$



The old binary column payment is


$$
\lambda_d=d\alpha_d+4d+4.
\tag{3.20}
$$


The exact all-prime transfer is


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_k|^{d-1}G_k
=
|f_k|\,2^{\lambda_d+d+5}\mathfrak D_d\,g_k^{[2]}.
}
\tag{3.21}
$$



In particular,


$$
\boxed{
v_2(G_k)=\chi_k+\nu_k,
}
\tag{3.22}
$$


where the exact original digit-sum expression remains


$$
\boxed{
\chi_k
=
d^2+4d+29+(d+4)s_2(d)
-3\sum_{n=0}^{d-1}s_2(n).
}
\tag{3.23}
$$


It is an evaluated payment, with


$$
\chi_k=k^2+O(k\log k),
$$


not an upper bound for $\nu_k$.

---

## 4. New uniform jet identities for the actual top sources

The next calculations retain every product-rule term. In particular, they do **not** assume that $\mathcal A_d$ commutes with $\Delta$.

### 4.1 Exact weighted contact jets

Define


$$
Q_h(n)=\prod_{a=h}^{d-1}(2n+2a+1),
$$


and retain the integers


$$
\eta_t^{(m)}
=
\frac{\Delta^t\sigma_m}{2^{t+1}t!}.
\tag{4.1}
$$



The established sequence divisibility and polynomial difference formula are


$$
2^{t+1}t!\mid\Delta^t\sigma_m,
$$




$$
\Delta^hP_d(n)
=
2^h\frac{d!}{(d-h)!}Q_h(n).
\tag{4.2}
$$



For $j,r\ge0$, the finite-difference product rule gives


$$
\Delta^j(\mathcal A_d\Delta^r\sigma)
=
\Delta^{d+j}(P_d\Delta^r\sigma).
$$


Substituting (4.2) and the definition of $\eta$, then using


$$
\alpha_d=d+v_2(d!),
$$


gives the exact identity


$$
\boxed{
\frac{\Delta^jt_n^{(r)}}{2^j(r+1)_j}
=
o_d
\sum_{h=0}^d
\binom{d+j}{h}Q_h(n)
\binom{d-h+r+j}{r+j}
\eta_{d-h+r+j}^{(n+h)}.
}
\tag{4.3}
$$


Here $(r+1)_j=(r+1)\cdots(r+j)$, with empty product $1$.

In particular,


$$
\boxed{
2^j(r+1)_j\mid \Delta^jt_n^{(r)},
\qquad
2^jj!\mid\Delta^jt_n^{(r)}.
}
\tag{4.4}
$$



The sum in (4.3) is the full weighted Newton source. It includes all differences of $P_d$, all source shifts, and the full factorial normalization.

### 4.2 Every normalized atom jet is odd

The reused atom formula is


$$
(\mathcal A_dw)_n=2^d(-1)^nU_d(n),
$$


where


$$
U_d(n)=
\sum_{h=0}^d
\binom dh\frac{d!}{(d-h)!}Q_h(n).
\tag{4.5}
$$



For $t\ge1$,


$$
2^t\mid\Delta^tU_d(n),
\qquad
\frac{\Delta^tU_d(n)}{2^t}\equiv0\pmod2.
\tag{4.6}
$$


Indeed:

* the $h=0$ contribution, after the division by $2^t$, contains
  $d!/(d-t)!$, hence the even factor $d$, unless it is zero;
* every $h\ge1$ coefficient already contains the even factor $d$.

Also $U_d(n)$ is odd.

Since


$$
\Delta^j\bigl((-1)^nU_d(n)\bigr)
=
(-1)^{n+j}
\sum_{t=0}^j\binom jt2^{j-t}\Delta^tU_d(n),
$$


we obtain


$$
\frac{\Delta^j((-1)^nU_d(n))}{2^j}
\equiv1\pmod2.
\tag{4.7}
$$



For the $u$-part, the same product rule shows


$$
2^{d+j}d!j!\mid
\Delta^j(\mathcal A_du)_n.
\tag{4.8}
$$


After division by $2^{d+j}$, that contribution is even.

Because $c=u-w$, equations (4.7)–(4.8) prove the new uniform identity


$$
\boxed{
\frac{\Delta^j\mathsf a_n}{2^j}\equiv1\pmod2,
\qquad
v_2(\Delta^j\mathsf a_n)=j.
}
\tag{4.9}
$$


Only jets lying inside the stated top-row range are used in the finite matrices below.

### 4.3 Evaluation of the contact-jet parities

The following source facts are reused from the evaluated turn11 contact calculation:


$$
\theta_t=\frac{\Delta^tu_0}{2^tt!},
\qquad
\eta_t=\theta_t+(t+1)\theta_{t+1},
$$




$$
\theta_{t+2}\equiv\theta_{t+1}+\theta_t\pmod2,
\qquad
(\theta_0,\theta_1,\theta_2)\equiv(1,0,1),
\tag{4.10}
$$


and


$$
\eta_t^{(m)}\equiv\eta_t\pmod2.
\tag{4.11}
$$


Thus $\theta$ has period $3$ modulo $2$.

We now evaluate the general low-order jet in (4.3), not just the previously selected $r=1,j=0$ source.

Put $t=d-h$. Modulo $2$, the right side of (4.3) becomes


$$
\sum_{t=0}^d
\binom{d+j}{t+j}
\binom{t+j+r}{j+r}\eta_{t+j+r}.
\tag{4.12}
$$


Vandermonde’s identity gives


$$
\binom{d+j}{t+j}\binom{t+j+r}{j+r}
=
\sum_{a=0}^r
\binom ra
\binom{d+j}{j+a}
\binom{d-a}{t-a}.
\tag{4.13}
$$



Suppose


$$
r+j<16.
\tag{4.14}
$$


Since $16\mid d$, the low four binary digits of $d+j$ are those of $j$. For $a\ge1$, $j+a>j$ and $j+a<16$, so its binary digits cannot be a subset of those of $j$. Therefore


$$
\binom{d+j}{j+a}\equiv0\pmod2
\quad(a\ge1),
$$


whereas


$$
\binom{d+j}{j}\equiv1\pmod2.
$$


Consequently (4.12) reduces to


$$
\varepsilon_{r+j}
:=
\sum_{t=0}^d\binom dt\eta_{t+r+j}\pmod2.
\tag{4.15}
$$



This sum can be completely evaluated. Write $d=2D$. From (4.10),


$$
\eta_{2h}\equiv\theta_h,\qquad
\eta_{2h+1}\equiv\theta_{h+1}\pmod2.
$$


Lucas reduction, followed by $(1+E)^D=E^{2D}$ on the sequence $\theta$, gives


$$
\varepsilon_{2a}\equiv\theta_{a+d},
\qquad
\varepsilon_{2a+1}\equiv\theta_{a+d+1}.
\tag{4.16}
$$


Since $d\equiv2\pmod3$,


$$
\boxed{
(\varepsilon_0,\ldots,\varepsilon_5)
=(1,1,1,0,0,1),
\qquad
\varepsilon_{j+6}=\varepsilon_j.
}
\tag{4.17}
$$



Thus the new evaluated jet congruence is


$$
\boxed{
\frac{\Delta^jt_n^{(r)}}{2^j(r+1)_j}
\equiv\varepsilon_{r+j}\pmod2,
\qquad r+j<16.
}
\tag{4.18}
$$


It is uniform in the actual top row $n$.

The restriction $r+j<16$ is essential. It is not silently extended to growing orders.

---

## 5. Evaluated three-, four- and five-column top-source minors

### 5.1 A uniform source-minor divisor

Let


$$
A=[\mathsf a,t^{(r_1)},\ldots,t^{(r_{q-1})}]
$$


be any $d\times q$ source matrix using one atom-contact column and $q-1$ actual weighted contact-return sources.

Newton expansion in the top row index writes $A$ as an integer binomial matrix times its finite-difference rows.

For a selected set of jet orders


$$
j_0<j_1<\cdots<j_{q-1},
$$


equations (4.4) and (4.9) permit extraction of


$$
2^{j_0+\cdots+j_{q-1}}.
$$


Expanding the remaining determinant in its atom column, every term also contains the factorial payments from $q-1$ contact rows. The smallest possible such payment discards the largest factorial valuation.

It follows that every $q$-minor of $A$ is divisible by


$$
2^{b_q},
\qquad
\boxed{
b_q=
\frac{q(q-1)}2+\sum_{j=0}^{q-2}v_2(j!).
}
\tag{5.1}
$$



This is a uniform lower divisor. The next calculation shows that it is attained for the particular source columns used here.

### 5.2 The source-specific valuation table

Use the ordered source sets


$$
\begin{aligned}
A^{[3]}&=[\mathsf a,t^{(1)},t^{(0)}],\\
A^{[4]}&=[\mathsf a,t^{(1)},t^{(0)},t^{(5)}],\\
A^{[5]}&=[\mathsf a,t^{(1)},t^{(0)},t^{(5)},t^{(4)}].
\end{aligned}
\tag{5.2}
$$



Equations (4.9) and (4.18) give the following table. An unadorned number is an exact valuation.



$$
\begin{array}{c|ccccc}
j&
\Delta^j\mathsf a&
\Delta^jt^{(1)}&
\Delta^jt^{(0)}&
\Delta^jt^{(5)}&
\Delta^jt^{(4)}
\\ \hline
0&0&0&0&0&\ge1\\
1&1&2&1&2&1\\
2&2&\ge4&3&3&3\\
3&3&\ge7&\ge5&7&4\\
4&4&7&\ge8&\ge9&8
\end{array}
\tag{5.3}
$$



For example,


$$
v_2(\Delta^2t^{(5)})
=
v_2(4\cdot6\cdot7)=3,
$$


because $\varepsilon_7=1$, while


$$
v_2(\Delta^2t^{(1)})\ge
v_2(4\cdot2\cdot3)+1=4,
$$


because $\varepsilon_3=0$.

Let


$$
T_q=\{d-q,\ldots,d-1\}.
$$


Replacing consecutive source rows by their forward-difference rows is a determinant-one operation.

For $q=3$, the unique lowest-valuation permutation uses


$$
t^{(1)}\text{ at order }0,\quad
t^{(0)}\text{ at order }1,\quad
\mathsf a\text{ at order }2.
$$


Its valuation is $0+1+2=3$.

For $q=4$, the unique lowest-valuation permutation uses


$$
t^{(1)},\ t^{(0)},\ t^{(5)},\ \mathsf a
$$


at orders $0,1,2,3$, respectively. Its valuation is


$$
0+1+3+3=7.
$$


If the atom is not used at order $3$, the last row contributes at least $5$, so the total is at least $8$. If the atom is used there, the table shows that the displayed assignment is the only one of valuation $7$.

For $q=5$, the unique lowest-valuation permutation uses


$$
t^{(1)},\ t^{(0)},\ t^{(5)},\ t^{(4)},\ \mathsf a
$$


at orders $0,1,2,3,4$. Its valuation is


$$
0+1+3+4+4=12.
$$


If the atom is not used in the last row, that row contributes at least $7$, and the total is at least $13$. With the atom in the last row, the displayed assignment is again the unique minimum.

The normalized factors in these distinguished products are all odd. Therefore


$$
\boxed{
v_2\det A^{[q]}[T_q,:]=b_q,
\qquad
(b_3,b_4,b_5)=(3,7,12).
}
\tag{5.4}
$$



This evaluates the top-source minors; it does not merely assign them names.

---

## 6. Complete forcing minors and factorial-adjugate payments

### 6.1 Vandermonde normalization

For an increasing $q$-tuple $M=(i_0,\ldots,i_{q-1})$, define


$$
\Phi_q=\prod_{j=0}^{q-1}j!,
\qquad
\mathcal N_q(M)
=
\frac{\prod_{a<b}(i_b-i_a)}{\Phi_q}.
\tag{6.1}
$$


The quotient is an integer because


$$
\mathcal N_q(M)
=
\det\left[\binom{i_a}{j}\right]_{0\le a,j<q}.
\tag{6.2}
$$



### 6.2 Complete bottom forcing minors

The rational Cauchy part of (3.9) has determinant


$$
\frac{
\Lambda_k^q\,2^{q(q-1)}
V(M)V(I)
}{
\prod_{i\in M,\ j\in I}(2(d+i+j)+1)
}.
\tag{6.3}
$$


Every denominator is odd.

Put


$$
c_q=q(q-1)+2v_2(\Phi_q).
\tag{6.4}
$$


Thus


$$
(c_3,c_4,c_5)=(8,16,30).
$$



The factorial correction in every entry of $R$ has valuation at least


$$
\alpha_d-2.
$$


Since $16\mid d$,


$$
v_2(d!)\ge d/2+d/4,
\qquad
\alpha_d\ge 7d/4.
\tag{6.5}
$$


At every original index, $\alpha_d-2\ge110$, which is well above the precision needed here.

Consequently the complete $R$, not just its rational part, satisfies


$$
\boxed{
2^{c_q}\mid\det R[M,I],
\qquad q=3,4,5,
}
\tag{6.6}
$$


and for the consecutive terminal column set $T_q$,


$$
\boxed{
\frac{\det R[M,T_q]}{2^{c_q}}
\equiv \mathcal N_q(M)\pmod2.
}
\tag{6.7}
$$



The factorial term remains in every exact matrix. It has only been reduced modulo a justified power of $2$.

### 6.3 Exact factorial-adjugate valuations

Let


$$
e_n=v_2\!\left(\frac{h_d}{(2n)!}\right).
$$


The last values, in reverse order, are


$$
\boxed{
e_{d-1}=0,\quad
e_{d-2}=1,\quad
e_{d-3}=3,\quad
e_{d-4}=4,\quad
e_{d-5}=7.
}
\tag{6.8}
$$


These follow from


$$
e_{d-1-r}
=
\sum_{s=1}^r\bigl(1+v_2(d-s)\bigr)
\tag{6.9}
$$


and $16\mid d$.

For any $q$-element sets $I,J$,


$$
v_2\det N_d[I,J]
\ge
\sum_{i\in I}e_i+\sum_{j\in J}e_j.
\tag{6.10}
$$


The minimum on each side is attained uniquely at $T_q$.

Put


$$
E_q^F=\sum_{n\in T_q}e_n.
$$


Then


$$
(E_3^F,E_4^F,E_5^F)=(4,8,15).
\tag{6.11}
$$



For the principal set, Jacobi’s complementary-minor identity gives


$$
\det\operatorname{adj}(K_d)[T_q,T_q]
=
\eta_d^{\,q-1}
\det K_d[T_q^c,T_q^c].
\tag{6.12}
$$


The complementary block is a leading principal block of $K_d$, so both factors on the right are odd.

Hence


$$
\boxed{
v_2\det N_d[T_q,T_q]=2E_q^F.
}
\tag{6.13}
$$


Every other pair $(I,J)\ne(T_q,T_q)$ has strictly larger valuation.

This explicitly pays the factorial diagonal and the adjugate minor. Oddness of $\eta_d$ alone would not supply (6.13).

### 6.4 Both bottom corrections remain harmless at the stated depths

For $x$, the bottom correction in (3.12) has valuation at least


$$
2\beta_d-d-1=2\alpha_d-d-11.
\tag{6.14}
$$



For every weighted contact-return column, (3.13) and the full division by $D_r$ give the uniform lower bound


$$
2\beta_d-\alpha_d-2=\alpha_d-12.
\tag{6.15}
$$


Define


$$
L_d=\alpha_d-12.
\tag{6.16}
$$


At every original index,


$$
L_d\ge100.
$$



Thus, for all the selected columns,


$$
\mathcal C^{[q]}
\equiv RN_dA^{[q]}\pmod{2^{L_d}}.
\tag{6.17}
$$


An entrywise error divisible by $2^{L_d}$ changes any fixed minor by a multiple of $2^{L_d}$, since all other entries are integers. In particular, none of these corrections can change a residue at depths $19,39,72$.

---

## 7. Evaluation of the complete higher cofactors

For a fixed residual row set $M$ of size $q$, Cauchy–Binet gives


$$
\det(RN_dA^{[q]})[M,:]
=
\sum_{\substack{|I|=q\\|J|=q}}
\det R[M,I]\,
\det N_d[I,J]\,
\det A^{[q]}[J,:].
\tag{7.1}
$$



The source-minor divisor (5.1), the forcing divisor (6.6), and the factorial-adjugate bounds show that every term is divisible by


$$
2^{c_q+2E_q^F+b_q}.
$$


The term $I=J=T_q$ attains this depth when $\mathcal N_q(M)$ is odd. Every other term is divisible by one additional power of $2$.

By (5.4), (6.7), and (6.13), the distinguished term has normalized residue $\mathcal N_q(M)$. The retained bottom corrections vanish at the required precision.

The complete result is therefore


$$
\boxed{
t_q=c_q+2E_q^F+b_q,
\qquad
(t_3,t_4,t_5)=(19,39,72),
}
\tag{7.2}
$$


and


$$
\boxed{
2^{t_q}\mid\det\mathcal C^{[q]}[M,:],
\qquad
\frac{\det\mathcal C^{[q]}[M,:]}{2^{t_q}}
\equiv\mathcal N_q(M)\pmod2.
}
\tag{7.3}
$$



For $M=(0,1,\ldots,q-1)$, $\mathcal N_q(M)=1$. Thus the first $q$ residual physical rows attain the content valuation.

### Theorem 7.1 — higher complete-source contents

Let


$$
\mathscr C_k^{[q]}
=
\gcd_{|M|=q}
\left|\det\mathcal C^{[q]}[M,:]\right|.
$$


Then, at every original index,


$$
\boxed{
v_2(\mathscr C_k^{[3]})=19,\qquad
v_2(\mathscr C_k^{[4]})=39,\qquad
v_2(\mathscr C_k^{[5]})=72.
}
\tag{7.4}
$$



Their odd parts have not been evaluated.

Define the actual attaining cofactors


$$
\Pi_{q,k}=\mathcal C^{[q]}[\{0,\ldots,q-1\},:],
$$




$$
\boxed{
\det\Pi_{q,k}=2^{t_q}\mu_{q,k},
\qquad
\mu_{q,k}\text{ odd}.
}
\tag{7.5}
$$


For $q=2$, set $\mu_{2,k}=\mu_k$.

---

## 8. The actual next pivots in the paid residual pencils

The cofactor evaluations give exact entries of the successive Schur pencils.

### 8.1 First new pivot: depth $13$ in the original $\mathcal P_k$

For residual physical index $i\ge2$, the $z^{(0)}$-entry of the original $\mathcal P_k$ is


$$
\boxed{
(\mathcal P_k)_{i-2,z^{(0)}}
=
\frac{
\det\mathcal C^{[3]}[\{0,1,i\},:]
}{2^6}.
}
\tag{8.1}
$$


Indeed, the bordered determinant equals $32$ times the integer Schur numerator in (3.18), which is twice the corresponding entry of $\mathcal P_k$.

Equation (7.3) therefore gives


$$
\boxed{
2^{13}\mid(\mathcal P_k)_{i-2,z^{(0)}},
\qquad
\frac{(\mathcal P_k)_{i-2,z^{(0)}}}{2^{13}}
\equiv\binom i2\pmod2.
}
\tag{8.2}
$$


In particular,


$$
\boxed{
(\mathcal P_k)_{0,z^{(0)}}=2^{13}\mu_{3,k},
\qquad \mu_{3,k}\text{ odd}.
}
\tag{8.3}
$$


The actual content of this column has binary valuation exactly $13$.

### 8.2 Second and third new pivots

After the paid three-column elimination defined below, the $z^{(5)}$-column satisfies


$$
\boxed{
(\mathcal P_k^{[3]})_{i-3,z^{(5)}}
=
\frac{
\det\mathcal C^{[4]}[\{0,1,2,i\},:]
}{2^{20}},
\qquad i\ge3.
}
\tag{8.4}
$$


Hence


$$
\boxed{
v_2\bigl(\operatorname{content}(\mathcal P_k^{[3]}\text{ column }z^{(5)})\bigr)
=19,
}
$$




$$
\frac{(\mathcal P_k^{[3]})_{i-3,z^{(5)}}}{2^{19}}
\equiv\binom i3\pmod2,
$$


and


$$
\boxed{
(\mathcal P_k^{[3]})_{0,z^{(5)}}=2^{19}\mu_{4,k}.
}
\tag{8.5}
$$



Similarly,


$$
\boxed{
(\mathcal P_k^{[4]})_{i-4,z^{(4)}}
=
\frac{
\det\mathcal C^{[5]}[\{0,1,2,3,i\},:]
}{2^{40}},
\qquad i\ge4.
}
\tag{8.6}
$$


Thus


$$
\boxed{
v_2\bigl(\operatorname{content}(\mathcal P_k^{[4]}\text{ column }z^{(4)})\bigr)
=32,
}
$$




$$
\frac{(\mathcal P_k^{[4]})_{i-4,z^{(4)}}}{2^{32}}
\equiv\binom i4\pmod2,
$$


and


$$
\boxed{
(\mathcal P_k^{[4]})_{0,z^{(4)}}=2^{32}\mu_{5,k}.
}
\tag{8.7}
$$



These are evaluated actual pivots, with source-specific normalized residues. No affine-border unit has been assumed.

---

## 9. Paid interpolation of every remaining column and both borders

### 9.1 Integer Cramer divisions and odd denominators

For $q=3,4,5$, put the selected $q$ columns first and partition the complete permuted $\mathcal Q_k(s)$ as


$$
\begin{pmatrix}
\Pi_{q,k}&U_{q,k}(s)\\
V_{q,k}&C_{q,k}(s)
\end{pmatrix}.
\tag{9.1}
$$


Define


$$
\boxed{
M_{q,k}
=
\frac{V_{q,k}\operatorname{adj}(\Pi_{q,k})}{2^{t_q}}.
}
\tag{9.2}
$$


Every entry is an integer: its numerator is a $q$-minor of the complete selected columns, and (7.3) proves the required division.

Exactly,


$$
V_{q,k}\Pi_{q,k}^{-1}
=
M_{q,k}/\mu_{q,k}.
\tag{9.3}
$$


The remaining denominator is the actual odd integer $\mu_{q,k}$, not an assumed unit over $\mathbb Z$.

The interpolation residues follow from (7.3). They are the interpolation coefficients for the integer-valued polynomial basis


$$
1,\binom i1,\ldots,\binom i{q-1}
$$


on nodes $0,\ldots,q-1$, reduced modulo $2$.

For example, for $q=3$,


$$
\boxed{
(V_{3,k}\Pi_{3,k}^{-1})_i
\equiv
\left(
1+i+\binom i2,\,
i,\,
\binom i2
\right)\pmod2.
}
\tag{9.4}
$$


For every $q$ here, the coefficient sum is $1\pmod2$.

### 9.2 Complete even Schur numerators

Set


$$
\mathcal V_k^{[q]}(s)
=
\mu_{q,k}C_{q,k}(s)-M_{q,k}U_{q,k}(s).
\tag{9.5}
$$


This is an integer pencil.

Every column of the original $\mathcal Q_k(s)$ is row-constant modulo $2$, coefficientwise in $s$, and the interpolation coefficients sum to $1$. Therefore


$$
\mathcal V_k^{[q]}(s)\equiv0\pmod2.
$$


The additional division


$$
\boxed{
\mathcal P_k^{[q]}(s)
=
\frac{\mathcal V_k^{[q]}(s)}2
}
\tag{9.6}
$$


is integral for the **whole** pencil.

Only the last column depends on $s$. Write


$$
\det\mathcal P_k^{[q]}(s)
=
P_{0,k}^{[q]}+P_{1,k}^{[q]}s,
$$




$$
g_k^{[q]}
=
\gcd(|P_{0,k}^{[q]}|,|P_{1,k}^{[q]}|),
\qquad
\nu_k^{[q]}=v_2(g_k^{[q]}).
\tag{9.7}
$$



The uneliminated common columns, in their retained order, are



$$
\begin{array}{c|l|c}
q&\text{return indices remaining}&\text{pencil size}\\ \hline
2&0,2,3,4,5,\ldots,d-1&d\\
3&2,3,4,5,\ldots,d-1&d-1\\
4&2,3,4,6,\ldots,d-1&d-2\\
5&2,3,6,\ldots,d-1&d-3.
\end{array}
\tag{9.8}
$$



All omitted indices in this table have been eliminated by the displayed paid cofactors. None has been discarded.

---

## 10. Exact coefficient and all-prime transfers

### 10.1 Column signs

Relative to the original order in (3.15), the selected orders have signs


$$
\epsilon_2=-1,\qquad
\epsilon_3=-1,\qquad
\epsilon_4=+1,\qquad
\epsilon_5=+1.
\tag{10.1}
$$


The change from $q=3$ to $q=4$ moves column $5$ across columns $2,3,4$, giving three transpositions. The next change moves column $4$ across columns $2,3$, giving two.

Let


$$
\det\mathcal Q_k(s)=I_{0,k}+I_{1,k}s.
$$


For $n_q=d+2-q$, the block determinant gives


$$
\boxed{
\mu_{q,k}^{\,n_q-1}I_{i,k}
=
\epsilon_q\,2^{t_q+n_q}P_{i,k}^{[q]},
\qquad i=0,1.
}
\tag{10.2}
$$



In particular,


$$
\mu_{3,k}^{d-2}I_{i,k}
=-2^{d+18}P_{i,k}^{[3]},
$$




$$
\mu_{4,k}^{d-3}I_{i,k}
=2^{d+37}P_{i,k}^{[4]},
$$




$$
\mu_{5,k}^{d-4}I_{i,k}
=2^{d+69}P_{i,k}^{[5]}.
\tag{10.3}
$$



### 10.2 The three successive paid identities

Comparing successive versions of (10.2) yields


$$
\boxed{
\mu_{3,k}^{d-2}P_{i,k}^{[2]}
=
2^{13}\mu_k^{d-1}P_{i,k}^{[3]},
}
\tag{10.4}
$$




$$
\boxed{
\mu_{4,k}^{d-3}P_{i,k}^{[3]}
=
-2^{19}\mu_{3,k}^{d-2}P_{i,k}^{[4]},
}
\tag{10.5}
$$




$$
\boxed{
\mu_{5,k}^{d-4}P_{i,k}^{[4]}
=
2^{32}\mu_{4,k}^{d-3}P_{i,k}^{[5]}.
}
\tag{10.6}
$$



Taking actual all-prime gcds gives


$$
|\mu_{3,k}|^{d-2}g_k^{[2]}
=
2^{13}|\mu_k|^{d-1}g_k^{[3]},
$$




$$
|\mu_{4,k}|^{d-3}g_k^{[3]}
=
2^{19}|\mu_{3,k}|^{d-2}g_k^{[4]},
$$




$$
|\mu_{5,k}|^{d-4}g_k^{[4]}
=
2^{32}|\mu_{4,k}|^{d-3}g_k^{[5]}.
\tag{10.7}
$$



Thus


$$
\boxed{
|\mu_{5,k}|^{d-4}g_k^{[2]}
=
2^{64}|\mu_k|^{d-1}g_k^{[5]},
}
\tag{10.8}
$$


and, since every displayed $\mu$ is proved odd,


$$
\boxed{
\nu_k=13+\nu_k^{[3]}
=32+\nu_k^{[4]}
=64+\nu_k^{[5]}.
}
\tag{10.9}
$$



The original odd factor $\mu_k$ has not been replaced by $1$. Its exact contribution is visible in (10.4), (10.7), and (10.8).

### 10.3 Full transfer back to $G_k$

The reused pre-pair identity is


$$
\delta_k^{d+2}\Omega_kH_{i,k}
=
f_k\,2^{\lambda_d}\mathfrak D_d I_{i,k}.
\tag{10.10}
$$


Combining it with the $q=5$ case of (10.3) gives


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_{5,k}|^{d-4}G_k
=
|f_k|\,2^{\lambda_d+d+69}\mathfrak D_d\,g_k^{[5]}.
}
\tag{10.11}
$$



This retains the full:

* annihilator determinant $\Omega_k$;
* clearer $\delta_k=\Lambda_k\eta_dh_d^2$;
* forcing determinant $f_k$;
* old binary column payment $2^{\lambda_d}$;
* product $\mathfrak D_d=\prod_{r<d}2^rr!$, including every odd part;
* paired payment $2^5$;
* new cofactor and row-division payments;
* actual odd interpolation factors;
* actual all-prime residual gcd.

At $2$,


$$
\boxed{
v_2(G_k)=\chi_k+64+\nu_k^{[5]}.
}
\tag{10.12}
$$



### 10.4 Actual primitive denominator and whole error

Because all coefficient pairs are related by the same fully paid rational scalars,


$$
\boxed{
\frac{|P_{1,k}^{[5]}|}{g_k^{[5]}}
=
\frac{|P_{1,k}|}{g_k^{[2]}}
=
\frac{|H_{1,k}|}{G_k}
=q_k,
}
\tag{10.13}
$$


and


$$
\boxed{
\frac{|P_{0,k}^{[5]}+P_{1,k}^{[5]}(e+\pi)|}{g_k^{[5]}}
=
\frac{|H_k(e+\pi)|}{G_k}
=\ell_k>0.
}
\tag{10.14}
$$


These are exact normalization identities, not numerical evaluations of $q_k$ or $\ell_k$.

---

## 11. What the recursion controls—and its precise obstruction

### 11.1 A proved general cofactor criterion

The calculations above give a reusable criterion in this particular paid pencil.

Choose one atom-contact source and $q-1$ actual weighted Newton sources. Let $A^{[q]}$ be their top source matrix, and let $T_q=\{d-q,\ldots,d-1\}$. Define


$$
b_q=\binom q2+\sum_{j=0}^{q-2}v_2(j!),
$$




$$
c_q=q(q-1)+2\sum_{j=0}^{q-1}v_2(j!),
$$




$$
E_q^F
=
\sum_{r=0}^{q-1}\sum_{s=1}^r(1+v_2(d-s)).
\tag{11.1}
$$



Suppose the actual source minor satisfies


$$
v_2\det A^{[q]}[T_q,:]=b_q,
\tag{11.2}
$$


and


$$
c_q+2E_q^F+b_q<L_d.
\tag{11.3}
$$


Then the same complete Cauchy–Binet argument proves


$$
\boxed{
v_2\bigl(\operatorname{content}_q(\mathcal C^{[q]})\bigr)
=
c_q+2E_q^F+b_q,
}
\tag{11.4}
$$


with the normalized row residues $\mathcal N_q(M)$.

This is a controlled cofactor criterion with explicit factorial and correction budgets. Its hypotheses were evaluated above for $q=3,4,5$.

### 11.2 Why this is not yet a growing-rank upper bound

Three distinct obstructions remain.

**First: the source-unit hypothesis has not been proved for a growing flag.**  
The parity evaluation (4.18) is proved only for $r+j<16$. Once those orders grow, the omitted terms in (4.13) need not be even. Their values depend on further binary digits of the original $d$. Extending the low-order table without proving those terms would be invalid.

**Second: the retained bottom corrections eventually enter.**  
The present argument compares complete corrected minors with $RN_dA^{[q]}$ only below the explicit depth


$$
L_d=\alpha_d-12=O(d).
$$


The candidate compound depths grow quadratically in $q$. Therefore the entrywise congruence used here cannot justify deletion of bottom corrections throughout a full $q\asymp d$ recursion.

There is also an exact rank obstruction: the product


$$
RN_d[\mathsf a,t^{(0)},\ldots,t^{(d-1)}]
$$


has rank at most $d$, but the complete common-column matrix has $d+1$ columns. Every $(d+1)$-minor of the pure product vanishes. Thus the full common-column elimination **must eventually use the retained bottom corrections**. They are not merely technical remainders.

**Third: the final affine coefficient pair still requires joint control.**  
Even an evaluated full common-column content does not automatically make the terminal constant or linear border a unit. Both complete coefficient borders must pass through the same paid recursion, and their final joint depth must be bounded without discarding a tie or cancellation.

These are mathematical obstructions to the attempted uniform continuation, not questions that a fixed finite determinant check resolves.

### 11.3 Concrete follow-on obligation

A concrete next lemma should construct a growing nested flag of actual common columns, extending


$$
[x,z^{(1)},z^{(0)},z^{(5)},z^{(4)}],
$$


and evaluate its corrected Schur pivots after the bottom corrections become visible.

It must provide:

1. an attaining cofactor at each stage, with every Cramer division proved integral;
2. the actual odd interpolation denominator at that stage;
3. a cumulative quadratic upper budget for the remaining paid binary pivots;
4. a bound for the joint terminal affine coefficient pair.

Equivalently, after the present evaluated payments, the exact remaining binary target is


$$
\boxed{
\nu_k^{[5]}
\le
\frac{15}{4}k^2-64+O(k\log k)
\qquad(k=9^{18+32u}).
}
\tag{11.5}
$$


The fixed constant $64$ does not affect the leading asymptotic target.

Statement (11.5) is open. The new cofactor chain reduces and specifies the problem, but does not prove this upper bound.

---

## 12. Boundary and forcing audit

Every new operation stays within the original finite objects.

* The annihilator still acts only on the original first $d$ rows.
* All $d$ complete common forcing columns remain in $F_k$ and $R$.
* Both factorial terms in the forcing are retained in (3.4) and (3.9).
* The rational return is annihilated only in the stated top rows; its full bottom contribution remains.
* Every selected Newton order belongs to $0,\ldots,d-1$.
* The new pivots use original physical rows
  

$$
m=d,d+1,\ldots,d+4.
$$


* After the five-column elimination, the residual physical rows are
  

$$
m=d+5,\ldots,2d+1,
$$


  including the original last row.
* The largest return index remains $3d=3k-3$, its successor moment remains $3k-2$, and the terminal factorial remains $(6k-4)!$.
* The literal atom is retained. Its normalized jets in (4.9) are essential to the attaining source minors.
* Both the complete constant border and the complete linear border pass through every interpolation and row division.
* All contents and final gcds in the transfer formulas are actual all-prime gcds.

---

## 13. Analytic and odd-prime consequences: established reuse only

The closed same-$H$ analytic estimate is reused:


$$
\log|H_k(e+\pi)|
\ge
4k^2\log k+
\left(
15\log2-\frac92\log3+\frac4{85}
\right)k^2
+o(k^2).
\tag{13.1}
$$


No Wishart enumeration, Jensen audit, same-$H$ comparison, or logarithm calculation is repeated.

For $k=3^s$ in the original domain, retain


$$
v_3(\mathscr L_k)=v_3(\mathscr R_k)=E_k,
\qquad
E_k=\frac{(k-2)(k-1-2s)}2,
$$


and only the consequent range


$$
\boxed{
E_k\le v_3(G_k)\le2E_k+s+1.
}
\tag{13.2}
$$



The other odd-prime obligations remain:

* for $5\le p\le6k-5$,
  

$$
v_p(\mathscr L_k),v_p(\mathscr R_k)\le B_p(k),
$$


  where
  

$$
B_p(k)=
  k\bigl(2\mathbf1_{p=3}+v_p(\Lambda_k)\bigr)
  +4\sum_{j<k}v_p(j!);
$$


* for $p>6k-5$,
  

$$
v_p(\mathscr L_k)=v_p(\mathscr R_k)=0.
$$



Neither follows from oddness of $\eta_d$ or of any $\mu_{q,k}$.

Conditionally on those separate descents, the sharp ternary payment and a bound


$$
v_2(G_k)\le Ak^2+o(k^2)
$$


give the reused implication


$$
\log\ell_k
\ge
\left(
(19-A)\log2-\frac72\log3-\frac{506}{85}
\right)k^2+o(k^2).
\tag{13.3}
$$


For $A=19/4$, the certified margin is positive:


$$
\frac{57}{4}\log2-\frac72\log3-\frac{506}{85}>0.
$$



Thus the requested binary bound, **together with** the independent other odd-prime descents, would force primitive whole-error divergence and retire this producer as a source of whole-error decay. It would not decide the rationality of $e+\pi$.

The separate original binary producer is unchanged. In particular, its domain $b=9^{18+32u}$, $n=4002b$, physical reconstruction indices $0,\ldots,b$, terminal $z_b=0$, corrected columns


$$
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
$$


and complete return


$$
\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f
$$


remain separate, with their actual contents, norm, clearers, primitive denominator and all-prime final gcd. No transfer from the present cofactor chain to that branch is asserted.

---

## 14. Bounded exact arithmetic and verification scope

No tools have been used. No original-length determinant computation, adjacent scan, capped Smith calculation or closed analytic computation is proposed.

No additional computation is indispensable to the proofs above. The only small arithmetic table that a coordinator may wish to verify independently has bounded inputs:

### Inputs

1. The recurrence over $\mathbb F_2$
   

$$
\theta_0=1,\quad\theta_1=0,\quad
   \theta_{n+2}=\theta_{n+1}+\theta_n.
$$


2. The evaluated period
   

$$
(\varepsilon_0,\ldots,\varepsilon_5)
   =(1,1,1,0,0,1).
$$


3. The twenty pairs
   

$$
r\in\{0,1,4,5\},\qquad 0\le j\le4,
$$


   with factorial ratios $(r+1)_j$; all factors are at most $9$.
4. The five factorial valuations
   

$$
v_2(j!),\qquad 0\le j\le4.
$$



### Expected verifiable outputs

* the contact-jet valuation table (5.3);
* unique principal-source determinant valuations $3,7,12$;
* the forcing/adjugate/source totals
  

$$
8+8+3=19,\qquad
  16+16+7=39,\qquad
  30+30+12=72;
$$


* the successive residual pivot depths
  

$$
19-5-1=13,\quad
  39-19-1=19,\quad
  72-39-1=32.
$$



This finite arithmetic checks the displayed local calculations only. The uniform scope comes from the symbolic jet, Cauchy, adjugate and correction arguments—not from a finite table. None of these checks establishes (11.5).

---

## 15. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Original weighted Newton divisions $D_r=2^rr!$ | Established reuse |
| Original depth-five paired cofactor and odd $\mu_k$ | Established reuse; separate full audit pending |
| All normalized atom jets in (4.9) are odd | **New proved statement** |
| Weighted contact-jet formula (4.3) | **New exact identity** |
| Low-order jet parity evaluation (4.18), $r+j<16$ | **New proved source evaluation** |
| General source-minor divisor $2^{b_q}$ | **New proved lower divisor** |
| Complete cofactor contents $19,39,72$ | **New evaluated theorems** on every original index |
| Actual successive pivots $13,19,32$ | **New evaluated pivots**, with source-specific residues |
| Complete paid interpolation through both borders | **Proved** |
| All-prime transfers (10.7)–(10.11) | **Proved** |
| Exact identity $\nu_k=64+\nu_k^{[5]}$ | **Proved payment, not an upper bound** |
| Uniform $(15/4)k^2$ bound for the actual remaining depth | **Open** |
| Other odd-prime descents and large-prime exclusion | **Independent open obligations** |
| Primitive whole-error divergence | **Conditional**, not established here |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

### Final conclusion

The new result is a short, fully paid cofactor recursion in the **actual original Newton–Cauchy pencil**. Three further complete common-source contents are evaluated:


$$
\boxed{19,\quad39,\quad72,}
$$


yielding actual residual pivots


$$
\boxed{13,\quad19,\quad32}
$$


and the exact identity


$$
\boxed{
v_2(G_k)
=
d^2+4d+29+(d+4)s_2(d)
-3\sum_{n<d}s_2(n)
+64+\nu_k^{[5]}.
}
$$



Every Newton divisor, complete forcing term, bottom correction, coefficient border, physical terminal, odd interpolation denominator and all-prime scalar payment has been retained.

The exact remaining bottleneck is the **growing corrected-cofactor recursion and the joint terminal border depth**, equivalently the uniform bound (11.5) for the actual residual pair. The pure $RN_dA$ approximation cannot finish that recursion: its precision window is bounded by $L_d$, and its rank is too small for all $d+1$ common columns. Any successful continuation must evaluate the bottom corrections where they first become essential and must control both final coefficients together.

No unconditional rationality or irrationality conclusion for $e+\pi$ has been obtained.
