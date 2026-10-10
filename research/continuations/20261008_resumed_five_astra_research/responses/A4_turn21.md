> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 Turn 21: Audit of the rising source divisor and an all-order dyadic source-rank theorem

## 1. Conclusions and scope

The parent rising-divisor and dyadic-kernel note **passes the independent audit at its stated scope**.

In particular:

1. The divisor
   

$$
2^j(d+1)_j
$$


   is an **integer divisor, at every prime**, of the actual weighted contact jet. Its proof uses the complete turn12 product rule, including all shifts and factorial factors.

2. The new parity $U$ is not the earlier parity $J$. Their integer normalizers differ, and this difference is essential.

3. The joint generating kernel is correct. Its derivation retains the Euler derivative in $j+r$. The scalar simplification uses the actual original congruence $d\equiv2\pmod3$.

4. Multiplication by $(1+Y+Y^2)^d$ gives a finite unit triangular **column transformation of the normalized parity matrix**. It is not, by itself, a division or elimination theorem for the complete integer pencil.

5. The even/odd block identity, the literal digit Kronecker ratio, and the symbolic unit blocks of sizes $2,8,32$ are correct.

6. The specified $33$-column **top-source** minor has valuation exactly
   

$$
960.
$$


   This does not evaluate a complete corrected cofactor or bound either terminal coefficient.

The principal new result of this report is not another fixed minor. It is an **evaluated all-order dyadic rank description of the deformed source kernel**. The deformation matrix is explicitly similar, over $\mathbb F_4$, to two scalar multiples of finite translation matrices. Consequently, its determinant, nullity, and unit cases can be evaluated without leaving a growing determinant unevaluated.

A second new conclusion is negative but exact:

> The older nominal source depth cannot be attained at any rank $q\ge18$, for any choice of the $q-1$ original contact-return columns accompanying the atom source.

The additional rising divisor forces this failure. The corrected source normalization is given below, and it is attained for the source-unit blocks certified by the new theorem.

None of these results proves


$$
\nu_k^{[5]}\le \frac{15}{4}k^2-64+O(k\log k),
$$


or an all-prime bound for $G_k$. The rationality or irrationality of $e+\pi$ remains unresolved.

---

## 2. Original objects and the retained paid interface

### 2.1 Domain, rows, columns, and physical terminal

Throughout,


$$
\boxed{
k=9^{18+32u},\qquad u\ge0,\qquad d=k-1.
}
\tag{2.1}
$$



The relevant original-domain congruences are


$$
d\equiv2\pmod3,\qquad v_2(d)=4,\qquad d\equiv16\pmod{64}.
\tag{2.2}
$$



Indeed, $k$ is divisible by $3$, while


$$
v_2(9^{18+32u}-1)=v_2(9-1)+v_2(18+32u)=3+1=4.
$$


Also


$$
k=81^{9+16u},
$$


and


$$
81^{9+16u}=(1+80)^{9+16u}\equiv17\pmod{64}.
$$



The index conventions remain:

- top-source row: $0\le n<d$;
- original return-column order: $0\le r<d$;
- a jet used in the finite top matrix satisfies $n+j<d$;
- residual row $i$, $0\le i<d+2$, is physical row $m=d+i$.

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
\tag{2.3}
$$



With


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),
$$


the complete integer forcing is


$$
\boxed{
T_n=-\Lambda_k\bigl((2n+2)!+(2n)!\bigr)
+\frac{4\Lambda_k}{2n+1}.
}
\tag{2.4}
$$



The original determinant is


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

Its physical terminal remains


$$
\boxed{
3k-2,\qquad (6k-4)!,\qquad 6k-5
}
\tag{2.5}
$$


for the last moment, factorial, and odd denominator respectively.

### 2.2 Actual clearers, contents, denominator, and whole error

The individual least right-column entry clearers remain


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3),
\qquad 0\le j<k.
$$



The final gcd is the actual all-prime gcd


$$
\boxed{G_k=\gcd(|H_{0,k}|,|H_{1,k}|).}
\tag{2.6}
$$


If


$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}),
$$


then the least simultaneous clearer of the rational coefficient pair
$H_k/\Lambda_k^k$, and its subsequent content, are exactly


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
}
\tag{2.7}
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


Writing their maximal-minor contents as


$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
\mathscr L_k=\delta_{2k-1}(Y_k),
$$


the established interface is


$$
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k
\mid \Lambda_k\mathscr L_k\mathscr R_k.
\tag{2.8}
$$



At every original index, the established sign and nonvanishing results give


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
\tag{2.9}
$$


No source normalization below replaces this denominator or this whole error.

### 2.3 Complete corrected columns and retained odd scalars

Put


$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1),
$$




$$
(\mathcal A_dy)_n
=\sum_{h=0}^d(-1)^h\binom dhP_d(n+h)y_{n+h}.
$$


Since $d$ is even,


$$
\mathcal A_dy=\Delta^d(P_dy).
$$


The annihilator acts only on the original first $d$ rows, and its determinant is


$$
\Omega_k=\prod_{n<d}P_d(n).
$$



Let


$$
b(t)=4t^2+6t+3.
$$


The complete forcing block is


$$
F_k(n,j)=
-\Lambda_k\sum_{h=0}^d(-1)^h\binom dh
P_d(n+h)b(n+h+j)(2(n+h+j))!,
\quad n,j<d.
\tag{2.10}
$$


Here


$$
b(t)(2t)!=(2t+2)!+(2t)!,
$$


so neither factorial term has been lost.

With


$$
D_f=\operatorname{diag}((2n)!)_{n<d},
\qquad F_k=-\Lambda_kD_fK_dD_f,
$$


write


$$
\eta_d^F=\det K_d.
$$


The established Pascal congruence gives oddness of $\eta_d^F$ and of every leading principal determinant of $K_d$.

Retain


$$
\alpha=v_2((2d)!),\qquad
\beta=v_2((2d-2)!),\qquad
\alpha-\beta=5,
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


and


$$
f_k=\det F_k
=(-\Lambda_k)^d\eta_d^F
\left(\prod_{n<d}(2n)!\right)^2.
\tag{2.11}
$$



The complete bottom forcing is


$$
\boxed{
R(i,j)=
\frac{\Lambda_k}{2(d+i+j)+1}
-\frac{\Lambda_k}{4}b(d+i+j)(2(d+i+j))!,
\quad i<d+2,\ j<d.
}
\tag{2.12}
$$



Every weighted source division is the full division


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



The exact corrected columns are


$$
\boxed{
x=RN_d\mathsf a+\frac{\delta_k}{2^{d+2}}c_{\rm bot},
}
\tag{2.13}
$$




$$
\boxed{
z^{(r)}=RN_dt^{(r)}
+\frac{\delta_k}{2^{\alpha+3}D_r}
(\Delta^r\sigma)_{\rm bot}.
}
\tag{2.14}
$$



For $\psi_0=r$, $\psi_1=w$, both affine coefficient borders are


$$
\boxed{
\mathfrak b_h
=\frac{\delta_k\Lambda_k}{4}(\psi_h)_{\rm bot}
+RN_d\Lambda_k(\mathcal A_d\psi_h)_{\rm top},
\qquad h=0,1.
}
\tag{2.15}
$$


Thus


$$
\mathcal Q_k(s)=
[x,z^{(0)},z^{(1)},\ldots,z^{(d-1)},
 \mathfrak b_0+s\mathfrak b_1].
$$



The audited turn12 eliminations are reused, not recalculated. Their complete content depths are $5,19,39,72$, with actual odd pivot quotients $\mu_{2,k},\ldots,\mu_{5,k}$. They give


$$
\nu_k=64+\nu_k^{[5]}.
$$


The full transfer remains


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_{5,k}|^{d-4}G_k
=
|f_k|\,2^{\lambda_d+d+69}\mathfrak D_d\,g_k^{[5]},
}
\tag{2.16}
$$


where


$$
\lambda_d=d\alpha+4d+4,\qquad
g_k^{[5]}=\gcd(|P_{0,k}^{[5]}|,|P_{1,k}^{[5]}|).
$$


In particular,


$$
\boxed{
v_2(G_k)=\chi_k+64+\nu_k^{[5]},
}
\tag{2.17}
$$




$$
\chi_k=
d^2+4d+29+(d+4)s_2(d)-3\sum_{n<d}s_2(n).
$$



The residual pencil $\mathcal P_k^{[5]}$ still includes both coefficient borders, all return orders $2,3,6,\ldots,d-1$, and physical rows


$$
d+5,\ldots,2d+1.
$$



---

## 3. Audit of the rising integer divisor

### 3.1 Full product-rule normalization

Set


$$
Q_h(n)=\prod_{a=h}^{d-1}(2n+2a+1),
\qquad
o_d=\operatorname{odd}(d!),
$$


and retain the integers


$$
\eta_t^{(m)}
=\frac{\Delta^t\sigma_m}{2^{t+1}t!}.
$$



The finite-difference product rule is


$$
\Delta^N(fg)(n)
=\sum_{h=0}^N\binom Nh
\Delta^hf(n)\,\Delta^{N-h}g(n+h).
$$


Also


$$
\Delta^hP_d(n)
=2^h\frac{d!}{(d-h)!}Q_h(n).
$$



Consequently,


$$
\begin{aligned}
\Delta^j(\mathcal A_d\Delta^r\sigma)_n
={}&2^{d+j+r+1}d!
\sum_{h=0}^d\binom{d+j}{h}Q_h(n)\\
&\qquad\cdot
\frac{(d-h+r+j)!}{(d-h)!}
\eta_{d-h+r+j}^{(n+h)}.
\end{aligned}
\tag{3.1}
$$


Dividing by the actual normalizer


$$
2^{\alpha+1}D_r=2^{\alpha+r+1}r!,
\qquad
\alpha=d+v_2(d!),
$$


gives the full turn12 identity


$$
\frac{\Delta^jt_n^{(r)}}{2^j(r+1)_j}
=
o_d\sum_{h=0}^d
\binom{d+j}{h}Q_h(n)
\binom{d-h+r+j}{r+j}
\eta_{d-h+r+j}^{(n+h)}.
\tag{3.2}
$$



This calculation does not commute $\mathcal A_d$ with $\Delta$.

### 3.2 Exact factorial cancellation

The identity used in the parent note is


$$
\frac{(r+1)_j}{(d+1)_j}
\binom{d+j}{h}
\binom{d-h+r+j}{r+j}
=
\binom dh\binom{d-h+r+j}{r}.
\tag{3.3}
$$


Indeed, both sides equal


$$
\frac{d!\,(d-h+r+j)!}
     {h!\,(d-h)!\,r!\,(d-h+j)!}.
$$



Multiplying (3.2) by $(r+1)_j/(d+1)_j$ therefore proves


$$
\boxed{
\frac{\Delta^jt_n^{(r)}}{2^j(d+1)_j}
=
o_d\sum_{h=0}^d
\binom dhQ_h(n)
\binom{d-h+r+j}{r}
\eta_{d-h+r+j}^{(n+h)}.
}
\tag{3.4}
$$



Every summand is an integer. Thus


$$
\boxed{
2^j(d+1)_j\mid \Delta^jt_n^{(r)}
}
\tag{3.5}
$$


as an integer divisibility statement, not merely a binary one.

Its binary depth is


$$
\begin{aligned}
v_2\bigl(2^j(d+1)_j\bigr)
&=j+v_2((d+j)!)-v_2(d!)\\
&=\boxed{2j+s_2(d)-s_2(d+j)}.
\end{aligned}
\tag{3.6}
$$


Relative to $2^jj!$, the additional depth is


$$
\boxed{
v_2\binom{d+j}{j}
=s_2(d)+s_2(j)-s_2(d+j).
}
\tag{3.7}
$$



For the actual source range $j<d$, its cumulative contribution through $q$ rows is $O(q\log d)$. It is not a new quadratic binary saving.

**Audit verdict: PASS.**

---

## 4. The different normalizations $U$ and $J$

Define the integral normalized jets


$$
U^{\mathbb Z}_{j,r}(n)
=\frac{\Delta^jt_n^{(r)}}{2^j(d+1)_j},
$$




$$
J^{\mathbb Z}_{j,r}(n)
=\frac{\Delta^jt_n^{(r)}}{2^j(r+1)_j}.
$$


Their reductions modulo $2$ will be denoted $U_{j,r}$ and $J_{j,r}$.

The exact relation is


$$
\boxed{
\binom{d+j}{j}U^{\mathbb Z}_{j,r}(n)
=
\binom{r+j}{j}J^{\mathbb Z}_{j,r}(n).
}
\tag{4.1}
$$


Neither normalized parity may simply be substituted for the other.

Reducing (3.4), using oddness of $o_d,Q_h(n)$ and the established shift independence


$$
\eta_t^{(m)}\equiv\eta_t\pmod2,
$$


gives


$$
\boxed{
U_{j,r}
=\sum_{t=0}^d\binom dt
  \binom{t+j+r}{r}\eta_{t+j+r}
\quad\text{in }\mathbb F_2.
}
\tag{4.2}
$$


The top row $n$ disappears only at this normalized parity precision.

Over


$$
\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1),
$$


the established contact sequence is


$$
\eta_m
=\operatorname{Tr}\!\left(
\omega^{m+2}[1+(m+1)\omega]
\right).
\tag{4.3}
$$


Here and below trace acts coefficientwise on formal series; it fixes the formal variables.

Since $d$ is even, $\binom dt$ vanishes modulo $2$ for odd $t$. Setting $s=j+r$ therefore yields


$$
\boxed{
U_{j,r}
=
\operatorname{Tr}\!\left(
\omega^{s+2}[1+(s+1)\omega]\,
[z^r](1+z)^s[1+\omega(1+z)]^d
\right).
}
\tag{4.4}
$$



This is the asserted all-order coefficient formula. No condition $r+j<16$ has been used.

---

## 5. Audit of the joint kernel and its finite column operation

### 5.1 Joint generating series, including the Euler derivative

For each nonnegative integer $t$,


$$
\sum_{j,r\ge0}\binom{t+j+r}{r}X^jY^r
=\frac{(1-Y)^{-t}}{1-X-Y}.
\tag{5.1}
$$


This follows by summing first in $r$, then in $j$.

Put $S=X+Y$ and


$$
B(Y)=
\left(\frac{\omega^2+\omega Y}{1+\omega Y}\right)^d.
$$


The corresponding weighted series is


$$
\mathcal F(X,Y)
=\sum_{t=0}^d\binom dt\omega^t
 \sum_{j,r\ge0}\binom{t+j+r}{r}
 (\omega X)^j(\omega Y)^r
=\frac{B(Y)}{1+\omega S}.
\tag{5.2}
$$



Let


$$
\mathcal E=X\frac{\partial}{\partial X}
          +Y\frac{\partial}{\partial Y}.
$$


The factor $1+(j+r+1)\omega$ in (4.3) requires


$$
\sum_{j,r\ge0}U_{j,r}X^jY^r
=
\operatorname{Tr}\!\left(
\omega^2[(1+\omega)+\omega\mathcal E]\mathcal F
\right).
\tag{5.3}
$$



Because $d$ is even, the derivative of $B(Y)$ vanishes in characteristic $2$. The derivative of the denominator does not vanish:


$$
\mathcal E(1+\omega S)^{-1}
=\frac{\omega S}{(1+\omega S)^2}.
$$


Using $1+\omega=\omega^2$, equation (5.3) becomes


$$
\boxed{
\sum_{j,r\ge0}U_{j,r}X^jY^r
=
\operatorname{Tr}\!\left(
\omega^2B(Y)
\frac{\omega^2+\omega S}{(1+\omega S)^2}
\right).
}
\tag{5.4}
$$



The Euler derivative is therefore retained with exactly the required factor.

### 5.2 Scalar simplification

Let


$$
C(Y)=(1+Y+Y^2)^d.
$$


Since


$$
1+Y+Y^2=(1+\omega Y)(1+\omega^2Y)
$$


and


$$
\omega^2+\omega Y=\omega^2(1+\omega^2Y),
$$


we have


$$
C(Y)B(Y)
=\omega^{2d}(1+\omega^2Y)^{2d}.
$$


The scalar outside the trace is consequently


$$
\omega^{2d+2}.
$$


At the original $d\equiv2\pmod3$, this scalar is $1$. Hence


$$
\boxed{
C(Y)\sum_{j,r\ge0}U_{j,r}X^jY^r
=
\operatorname{Tr}\!\left(
(1+\omega^2Y)^{2d}
\frac{\omega^2+\omega S}{(1+\omega S)^2}
\right).
}
\tag{5.5}
$$



**Audit verdict: PASS, including the exponent and scalar.**

### 5.3 What the column transformation does—and does not do

If $C(Y)=\sum c_hY^h$, define the finite upper-triangular matrix


$$
T_q(C)_{a,b}=
\begin{cases}
c_{b-a},&a\le b,\\
0,&a>b,
\end{cases}
\qquad 0\le a,b<q.
$$


Its diagonal entries are $1$. Thus


$$
\det T_q(C)=1.
$$


The first $q$ transformed columns depend only on the first $q$ original columns. In particular, multiplication by $C(Y)$ preserves both rank and determinant of each leading $q\times q$ normalized parity block.

This is a literal finite operation. No infinite inverse or projected matrix is used.

There is also an integral lift on the already normalized top-jet array: use the integer coefficients of $(1+Y+Y^2)^d$ in the same finite triangular matrix. However, the kernel identity (5.5) remains a parity identity.

For clarity about the varying source divisors, let the raw contact numerators be


$$
N_r=(\mathcal A_d\Delta^r\sigma)_{\rm top}.
$$


A triangular operation on $N_r/D_r$, when expressed on raw columns with the original $D_r$ normalizers retained, has coefficients


$$
c_{b-a}\frac{D_b}{D_a},\qquad a\le b.
\tag{5.6}
$$


These are integers because $D_a\mid D_b$. This explicitly records the varying $D_r$ payments.

It does not authorize any of the following:

- division of the whole corrected pencil by the source row factors;
- omission of transformed bottom corrections;
- replacement of either affine border by a source parity;
- use of an $\mathbb F_4$ auxiliary similarity as an integer unimodular operation.

No such whole-pencil operation is asserted here.

---

## 6. Audit of the undeformed blocks and the literal Kronecker ratio

Since $v_2(2d)=5$, the numerator in (5.5) has first nonconstant term in degree $32$. Thus, for leading blocks of size at most $32$, the transformed matrix is


$$
E_{j,r}=\binom{j+r}{r}\varepsilon_{j+r},
$$


where


$$
(\varepsilon_0,\ldots,\varepsilon_5)=(1,1,1,0,0,1)
$$


with period $6$.

### 6.1 Even/odd block identity

For a leading block of size $2m$, reorder rows and columns by parity. Lucas reduction gives


$$
\boxed{
E_{2m}=
\begin{pmatrix}
C_m&A_m\\
A_m&0
\end{pmatrix},
}
\tag{6.1}
$$


where


$$
A_m(h,l)=\binom{h+l}{l}\theta_{h+l},
\qquad
\theta=(1,0,1)\text{ of period }3.
$$



The odd/odd block vanishes because


$$
\binom{2(h+l+1)}{2l+1}\equiv0\pmod2.
$$


The two off-diagonal blocks are identical. Therefore


$$
\det E_{2m}=\det(A_m)^2
\quad\text{in characteristic }2.
\tag{6.2}
$$



### 6.2 Digit matrices and their ratio

Let $m=2^a$, and put


$$
P_m(h,l)=\binom{h+l}{l}\pmod2,
\qquad
D_\omega=\operatorname{diag}(\omega^h),
$$




$$
B_\omega=D_\omega P_mD_\omega.
$$


Lucas’s theorem gives the literal tensor decomposition of $P_m$ into copies of


$$
\begin{pmatrix}1&1\\1&0\end{pmatrix}.
$$



At digit $i$, put $x=\omega^{2^i}$. The corresponding factors of $B_\omega$ and $B_{\omega^2}$ are


$$
B(x)=\begin{pmatrix}1&x\\x&0\end{pmatrix},
\qquad
B(x^2)=\begin{pmatrix}1&x^2\\x^2&0\end{pmatrix}.
$$


Direct multiplication gives


$$
\boxed{
B(x)^{-1}B(x^2)
=x\begin{pmatrix}1&0\\1&1\end{pmatrix}.
}
\tag{6.3}
$$


Multiplying the digit scalars yields


$$
\prod_{i=0}^{a-1}\omega^{2^i}
=\omega^{2^a-1}
=\omega^{m-1}.
$$


Hence


$$
\boxed{
B_\omega^{-1}B_{\omega^2}
=\omega^{m-1}J_a,
\qquad
J_a=\bigotimes_{i=1}^a
\begin{pmatrix}1&0\\1&1\end{pmatrix},
\qquad J_a^2=I.
}
\tag{6.4}
$$



Since


$$
A_m=\omega^2B_\omega+\omega B_{\omega^2},
$$


we obtain


$$
A_m
=\omega^2B_\omega
\left(I+\omega^{m+1}J_a\right).
\tag{6.5}
$$


For even $a$, $m\equiv1\pmod3$, so


$$
\left(I+\omega^2J_a\right)^2
=(1+\omega)I\ne0.
$$


Thus $A_m$, and therefore $E_{2m}$, is a unit for $m=1,4,16$.

This proves the parent’s unit blocks


$$
\boxed{2,\ 8,\ 32}
$$


symbolically, without a matrix scan.

---

## 7. Full rising row payments and the exact source33 valuation

### 7.1 A stronger all-prime source-minor divisor

Write


$$
S_j=(d+1)_j=\frac{(d+j)!}{d!}.
$$


The sequence $S_j$ is a divisibility chain:


$$
S_j\mid S_{j+1}.
$$



Consider any source matrix


$$
A=[\mathsf a,t^{(r_1)},\ldots,t^{(r_{q-1})}],
\qquad q\le d,
$$


using the actual weighted contact columns.

The established atom identity is


$$
\frac{\Delta^j\mathsf a_n}{2^j}\equiv1\pmod2,
\qquad
v_2(\Delta^j\mathsf a_n)=j.
\tag{7.1}
$$



Finite Newton expansion and (3.5) now show that every $q$-minor of $A$ is divisible by the full integer


$$
\boxed{
\mathcal B'_q
=
2^{\binom q2}\prod_{j=0}^{q-2}S_j.
}
\tag{7.2}
$$


To check this, choose increasing jet orders $j_0<\cdots<j_{q-1}$. Extract $2^{\sum j_a}$, then expand in the atom column. The remaining $q-1$ contact factors form a subsequence of the divisibility chain $S_j$, and their product is divisible by $\prod_{j=0}^{q-2}S_j$. The integer Newton matrix preserves this divisibility through Cauchy–Binet.

Thus the binary lower depth is


$$
\boxed{
b'_q
=\binom q2+\sum_{j=0}^{q-2}
v_2\!\left(\frac{(d+j)!}{d!}\right).
}
\tag{7.3}
$$



For consecutive source rows, this payment is especially explicit. If $\mathcal J$ is their jet matrix, form


$$
W_{j,0}
=\frac{S_{q-1}}{S_j}
 \frac{\Delta^j\mathsf a_n}{2^j},
\qquad
W_{j,a}
=\frac{\Delta^jt_n^{(r_a)}}{2^jS_j}.
$$


Every entry is integral, and


$$
\boxed{\det\mathcal J=\mathcal B'_q\det W.}
\tag{7.4}
$$


This pays all odd parts of the rising factors as well as their binary parts.

### 7.2 The parent’s $q=33$ arithmetic

At the original $d\equiv16\pmod{64}$, for $0\le j\le31$,


$$
v_2(S_j)=v_2(j!)+\mathbf1_{\{j\ge16\}}.
\tag{7.5}
$$


For the factors $d+a$, $1\le a\le31$, only $a=16$ differs from $v_2(a)$, and it contributes one additional power of $2$.

Also


$$
\sum_{j=0}^{31}v_2(j!)
=\sum_{j=0}^{31}(j-s_2(j))
=496-80=416.
$$


Therefore


$$
\boxed{
b'_{33}=528+416+16=960.
}
\tag{7.6}
$$



The payment $v_2(S_j)$ is nondecreasing, and


$$
v_2(S_{32})-v_2(S_{31})
=v_2(d+32)=4.
\tag{7.7}
$$


Thus, in the atom-column expansion of (7.4), the unique cheapest atom row is $j=32$. Its normalized atom entry is odd.

The remaining contact cofactor is the leading $32\times32$ matrix $U$, whose determinant is $1$ by Sections 5–6. Consequently,


$$
\boxed{
v_2\det[\mathsf a,t^{(0)},\ldots,t^{(31)}]
       [\{d-33,\ldots,d-1\},:]
=960.
}
\tag{7.8}
$$



The uniqueness asserted here is the uniqueness of the cheapest **atom row**, not the uniqueness of a permutation inside the $32$-column contact cofactor.

This is exactly the parent’s top-source conclusion. No corrected source33 cofactor, factorial-adjugate total, border unit, or terminal coefficient bound has been inferred.

---

## 8. The extra divisor disproves the older growing nominal depth

The older source depth was


$$
b_q=\binom q2+\sum_{j=0}^{q-2}v_2(j!).
$$


The new divisor gives


$$
\boxed{
b'_q-b_q
=\sum_{j=0}^{q-2}v_2\binom{d+j}{j}.
}
\tag{8.1}
$$



At every original $d$, the first additional carry occurs at $j=16$:


$$
v_2\binom{d+16}{16}=1.
$$


Hence, for every $q\ge18$,


$$
b'_q>b_q.
$$



### Theorem 8.1 — failure of the old nominal source-unit depth

For every original index and every $18\le q\le d$, no $q$-minor formed from one atom source and $q-1$ actual weighted contact sources can have valuation $b_q$.

#### Proof

Every such minor is divisible by $2^{b'_q}$, and $b'_q>b_q$. ∎

This is stronger than failure of one proposed column order. It rules out the older nominal depth for every choice of the contact-return columns.

Equivalently, the older normalized contact entry satisfies


$$
\frac{\Delta^jt_n^{(r)}}{2^jj!}
=\binom{d+j}{j}\,U^{\mathbb Z}_{j,r}(n).
\tag{8.2}
$$


The old parity matrix therefore acquires rows forced to vanish by the rising carry factors. Its growing source-unit hypothesis cannot remain valid.

The corrected normalization is $\mathcal B'_q$, not $\mathcal B_q$. The next sections prove genuine all-order attainment criteria for this corrected normalization.

---

## 9. The actual deformation after degree $32$

Put


$$
H_\omega(S)=\frac{\omega^2+\omega S}{(1+\omega S)^2}.
$$


The transformed kernel is


$$
\operatorname{Tr}\bigl((1+\omega^2Y)^{2d}H_\omega(X+Y)\bigr).
$$



The numerator is explicitly


$$
\boxed{
(1+\omega^2Y)^{2d}
=(1+\omega Y^2)^d
=\sum_{v\subseteq_{\rm bit}d}\omega^vY^{2v}.
}
\tag{9.1}
$$


Thus its coefficients are evaluated by the actual bits of $d$; they are not arbitrary deformation parameters.

Let $V$ denote the transformed normalized parity matrix. Reordering a leading $2m\times2m$ block by parity gives


$$
\boxed{
V_{2m}=
\begin{pmatrix}
C_m(d)&A_m(d)\\
A_m(d)&0
\end{pmatrix},
}
\tag{9.2}
$$


where the joint kernels of the two blocks are


$$
\sum_{h,l\ge0}A_m(d)_{h,l}x^hy^l
=
\operatorname{Tr}\!\left(
\frac{\omega(1+\omega y)^d}
     {1+\omega^2(x+y)}
\right),
\tag{9.3}
$$




$$
\sum_{h,l\ge0}C_m(d)_{h,l}x^hy^l
=
\operatorname{Tr}\!\left(
\frac{\omega^2(1+\omega y)^d}
     {1+\omega^2(x+y)}
\right).
\tag{9.4}
$$


The displayed kernels are understood coefficientwise before restricting $h,l<m$.

For example, the entries have the explicit finite digit forms


$$
\boxed{
A_m(d)_{h,l}
=
\sum_{\substack{v\subseteq_{\rm bit}d\\v\le l\\
h\mathbin{\&}(l-v)=0}}
\operatorname{Tr}(\omega^{h+l+v+2}),
}
\tag{9.5}
$$




$$
\boxed{
C_m(d)_{h,l}
=
\sum_{\substack{v\subseteq_{\rm bit}d\\v\le l\\
h\mathbin{\&}(l-v)=0}}
\operatorname{Tr}(\omega^{h+l+v+1}).
}
\tag{9.6}
$$


These formulas evaluate the deformation coefficients. The following theorem evaluates their collective rank.

---

## 10. An explicit finite similarity for the deformation matrix

Let $m=2^a$, and put


$$
e=d\bmod m,\qquad 0\le e<m.
$$


Define


$$
p(z)=1+\omega z,\qquad q(z)=1+\omega^2z.
$$


For a series $g(z)$, let $T_m(g)$ be its finite upper-triangular coefficient matrix:


$$
T_m(g)_{h,l}=[z^{\,l-h}]g(z),\qquad h\le l.
$$



Since $m$ is a power of $2$,


$$
p(z)^m\equiv q(z)^m\equiv1\pmod{z^m}.
$$


Therefore $T_m(p^d)=T_m(p^e)$, and similarly for $q$.

The block in (9.2) is


$$
\boxed{
A_m(d)
=\omega^2B_\omega T_m(q^e)
+\omega B_{\omega^2}T_m(p^e).
}
\tag{10.1}
$$


Using the audited ratio (6.4),


$$
A_m(d)
=\omega^2B_\omega
\left[I+\lambda J_aT_m\!\left((p/q)^e\right)\right]
T_m(q^e),
\qquad
\lambda=\omega^{m+1}.
\tag{10.2}
$$



The exterior factors are invertible. It remains to evaluate


$$
L_{m,e}=J_aT_m((p/q)^e).
$$



### Theorem 10.1 — explicit all-order deformation similarity

On the $m$-dimensional space


$$
\mathcal V_m=\mathbb F_4[z]_{<m},
$$


the operator $L_{m,e}$ is similar to


$$
\boxed{
\omega^{2e}\mathsf J_{m-e}
\ \oplus\
\omega^{m-e}\mathsf J_e,
}
\tag{10.3}
$$


where $\mathsf J_n$ is the finite translation operator


$$
h(z)\longmapsto h(z+1)
\quad\text{on }\mathbb F_4[z]_{<n}.
$$



#### Proof

For row coefficient vectors, $J_a$ represents $f(z)\mapsto f(z+1)$. Hence


$$
L_{m,e}f
=\left(\frac{p(z)}{q(z)}\right)^e f(z+1)
\pmod{z^m}.
\tag{10.4}
$$



Consider the two subspaces


$$
W_1=p(z)^e\mathbb F_4[z]_{<m-e},
$$




$$
W_2=q(z)^{m-e}\mathbb F_4[z]_{<e}.
$$


Their dimensions are $m-e$ and $e$. They intersect trivially: a polynomial in their intersection would be divisible by


$$
p^eq^{m-e},
$$


a polynomial of degree $m$, while having degree less than $m$. Thus


$$
\mathcal V_m=W_1\oplus W_2.
$$



The identities


$$
p(z+1)=\omega^2q(z),\qquad
q(z+1)=\omega p(z)
\tag{10.5}
$$


give, for $f=p^eh$,


$$
L_{m,e}f=\omega^{2e}p^eh(z+1).
$$


Thus the restriction to $W_1$ is $\omega^{2e}\mathsf J_{m-e}$.

For $f=q^{m-e}h$,


$$
L_{m,e}f
=\omega^{m-e}p^mq^{-e}h(z+1)\pmod{z^m}.
$$


The finite congruences $p^m\equiv q^m\equiv1\pmod{z^m}$ imply


$$
p^mq^{-e}\equiv q^{m-e}\pmod{z^m}.
$$


The resulting polynomial has degree less than $m$, so the restriction to $W_2$ is


$$
\omega^{m-e}q^{m-e}h(z+1).
$$


This is $\omega^{m-e}\mathsf J_e$. ∎

This proof is finite. Translation has not been treated as a ring automorphism of $\mathbb F_4[z]/(z^m)$; it is the explicitly defined linear operator on degree-$<m$ polynomial representatives. The two invariant subspaces validate every truncation used in the argument.

### 10.1 Evaluated determinant and nullity

Every polynomial has a unique representation


$$
h(z)=A(z^2+z)+zB(z^2+z).
$$


Therefore


$$
h(z+1)=h(z)
\quad\Longleftrightarrow\quad B=0.
$$


It follows that


$$
\dim\ker(I+\mathsf J_n)=\left\lceil\frac n2\right\rceil,
\qquad
\mathsf J_n^2=I.
\tag{10.6}
$$


For $c\ne1$,


$$
(I+c\mathsf J_n)^2=(1+c^2)I,
$$


so $I+c\mathsf J_n$ is invertible.

Theorem 10.1 consequently gives the evaluated determinant


$$
\boxed{
\det(I+\lambda L_{m,e})
=
(1+\lambda\omega^{2e})^{m-e}
(1+\lambda\omega^{m-e})^e.
}
\tag{10.7}
$$



For the actual $\lambda=\omega^{m+1}$, the two possible singular cases are:

- $e\equiv m+1\pmod3$, from the first block;
- $e\equiv2m+1\pmod3$, from the second block.

These residues are distinct because $m\not\equiv0\pmod3$. The remaining residue is $e\equiv1\pmod3$.

For $m\ge2$, both $m$ and the actual $e$ are even. Hence


$$
\boxed{
\kappa_m(d):=\dim\ker A_m(d)=
\begin{cases}
\dfrac{m-e}{2},&e\equiv m+1\pmod3,\\[2mm]
\dfrac e2,&e\equiv2m+1\pmod3,\\[2mm]
0,&e\equiv1\pmod3.
\end{cases}
}
\tag{10.8}
$$



The nullspaces are also explicit in the polynomial coordinates of (10.2):

- in the first case, they come from
  

$$
p^e(z^2+z)^t,\qquad 0\le t<\frac{m-e}{2};
$$


- in the second case, they come from
  

$$
q^{m-e}(z^2+z)^t,\qquad 0\le t<\frac e2.
$$



Thus this is an evaluated rank and kernel description, not a named determinant criterion.

For completeness, the scalar in the determinant of $A_m(d)$ is


$$
\boxed{
\det A_m(d)=
\omega^{m(m+1)}
(1+\omega^{m+1+2e})^{m-e}
(1+\omega^{2m+1-e})^e.
}
\tag{10.9}
$$


Empty-dimensional factors are omitted. Since $A_m(d)$ has entries in $\mathbb F_2$, a nonzero value in (10.9) is necessarily $1$.

---

## 11. Exact rank of the growing leading normalized source blocks

The determinant alone is not the whole rank calculation. We now evaluate the full block (9.2).

Put


$$
V_m=B_\omega T_m(q^e),\qquad
W_m=B_{\omega^2}T_m(p^e),\qquad
T=V_m^{-1}W_m.
$$


Then


$$
A_m=\omega^2V_m+\omega W_m,
\qquad
C_m=\omega V_m+\omega^2W_m.
$$



Multiplying the two block rows in (9.2) by $V_m^{-1}$, set


$$
a=\omega^2I+\omega T,\qquad
c=\omega I+\omega^2T.
$$


Since


$$
c+\omega a=\omega^2I,
$$


a block row operation gives


$$
\begin{pmatrix}c&a\\a&0\end{pmatrix}
\sim
\begin{pmatrix}\omega^2I&a\\a&0\end{pmatrix}.
$$


Eliminating the lower-left block shows


$$
\operatorname{rank}V_{2m}
=m+\operatorname{rank}(a^2).
\tag{11.1}
$$



The matrix $a$ is similar to


$$
\omega^2(I+\lambda L_{m,e}).
$$


By Theorem 10.1, a singular translation block of even dimension $n$ contributes nullity $n/2$ to $a$, but nullity $n$ to $a^2$. The other block is invertible. Therefore


$$
\dim\ker(a^2)=2\kappa_m(d).
$$



Because the finite column transformation $T_{2m}(C)$ preserves rank, we obtain the main theorem.

### Theorem 11.1 — all-order dyadic rank and unit theorem

Let $m=2^a\ge2$, and suppose $2m\le d$, so that the leading block uses actual source rows and actual return columns. Put $e=d\bmod m$. Then


$$
\boxed{
\operatorname{rank}_{\mathbb F_2}
(U_{j,r})_{0\le j,r<2m}
=2m-2\kappa_m(d),
}
\tag{11.2}
$$


where $\kappa_m(d)$ is explicitly given by (10.8).

In particular,


$$
\boxed{
\det(U_{j,r})_{j,r<2m}=1
}
$$


if and only if


$$
\boxed{
e\equiv1\pmod3,
\quad\text{or}\quad
e=0\ \text{and}\ m\equiv1\pmod3.
}
\tag{11.3}
$$


The block of size $2$ is a unit separately, as already audited.

For growing $m\ge32$ on the original domain, $e>0$, because bit $4$ of $d$ is present. Thus the unit condition simplifies to


$$
\boxed{d\bmod m\equiv1\pmod3.}
\tag{11.4}
$$



This theorem evaluates the actual $d$-dependent deformation at every dyadic order in the finite source range.

---

## 12. Original-bit consequences and genuine growing source attainment

### 12.1 The first visible deformation is not harmless

The original indices satisfy the stronger fixed congruence


$$
\boxed{d\equiv208\pmod{256}.}
\tag{12.1}
$$


Indeed,


$$
81^{9+16u}
=(1+80)^{9+16u}
\equiv1+80(9+16u)
\equiv209\pmod{256}.
$$



The all-order theorem therefore gives the following symbolic evaluations:



$$
\begin{array}{c|c|c|c}
m&e=d\bmod m&\kappa_m(d)&
\operatorname{rank}U_{2m}\\ \hline
16&0&0&32\\
32&16&0&64\\
64&16&0&128\\
128&80&40&176\\
256&208&0&512
\end{array}
\tag{12.2}
$$



These are consequences of the proved rank formula and the original congruence, not scans of source matrices.

In particular, the first growing block beyond the parent’s cutoff behaves differently from a frozen numerator:


$$
\boxed{U_{64}\text{ is a unit}.}
$$


The undeformed matrix $E_{64}$, by contrast, is singular. Thus ignoring the numerator after degree $32$ gives an incorrect rank prediction.

### 12.2 Corrected source normalization is attained at all certified unit sizes

Let $s=2m$, and suppose $s+1\le d$. Consider the actual source columns


$$
A^{(s+1)}
=[\mathsf a,t^{(0)},\ldots,t^{(s-1)}].
$$


In (7.4), with $q=s+1$, the last rising payment is strictly larger than every earlier one:


$$
v_2(S_s)-v_2(S_{s-1})=v_2(d+s)>0.
$$


Thus the atom column of $W\bmod2$ is supported only at row $s$. Its entry there is $1$. Hence


$$
\boxed{
\frac{
\det A^{(s+1)}[\{d-s-1,\ldots,d-1\},:]
}{
\mathcal B'_{s+1}
}
\equiv
\det(U_{j,r})_{0\le j,r<s}
\pmod2.
}
\tag{12.3}
$$



Combining this with Theorem 11.1 proves:

### Corollary 12.1 — all-order attaining top-source minors

For every original index and every dyadic $m$ satisfying


$$
2m+1\le d
$$


and the unit condition (11.3),


$$
\boxed{
v_2\det
[\mathsf a,t^{(0)},\ldots,t^{(2m-1)}]
[\{d-2m-1,\ldots,d-1\},:]
=b'_{2m+1}.
}
\tag{12.4}
$$



The quotient by the full integer $\mathcal B'_{2m+1}$ is odd. Its odd part is not evaluated.

If the dyadic unit condition fails, (12.3) proves that this particular source minor has depth at least $b'_{2m+1}+1$. The exact additional binary depth is not supplied by a parity rank calculation.

### 12.3 Unbounded certified unit ranks occur within the original domain

This is not merely a list of fixed blocks.

Let


$$
k_0=9^{18},\qquad g=9^{32}.
$$


Then


$$
v_2(g-1)=8.
$$


For every $a\ge8$, $g$ has exact order $2^{a-8}$ modulo $2^a$. This follows inductively from


$$
v_2(g^{2^t}-1)=8+t.
$$


Consequently


$$
u\longmapsto d= k_0g^u-1\pmod{2^a}
$$


runs through every residue congruent to $208\pmod{256}$.

In particular, for every $a\ge8$, there is an infinite congruence class of original $u$'s for which


$$
d\bmod2^a=208.
$$


Since $208\equiv1\pmod3$, Theorem 11.1 certifies a unit block of size $2^{a+1}$ at all sufficiently large indices in that class, and Corollary 12.1 gives an attaining source minor of size $2^{a+1}+1$.

The congruence class can be specified by a finite binary lifting recursion. Starting with $u_8=0$, lift a solution


$$
k_0g^{u_a}\equiv209\pmod{2^a}
$$


by


$$
u_{a+1}=u_a+\epsilon_a2^{a-8},
$$


where


$$
\epsilon_a\equiv
\frac{k_0g^{u_a}-209}{2^a}\pmod2.
$$


This is a mathematical construction, not a request to execute a computation.

The full-domain theorem remains (11.2). The congruence classes above merely demonstrate unbounded source-unit attainment inside the unchanged original domain. They do not establish a complete growing corrected flag for every $u$, or any whole-error estimate on those indices.

---

## 13. An evaluated wider-column source-completion criterion

The rank description also gives a concrete way to move beyond a singular leading block without naming an unevaluated determinant.

Let $m,M$ be powers of $2$, with


$$
m\ge2,\qquad M\ge2m,\qquad 2M\le d.
$$


Put


$$
e=d\bmod M,\qquad R=M-m.
$$


Let $A_{m,M}(d)$ be the first $m$ rows and first $M$ columns of the block $A(d)$ in (9.3).

Define


$$
n_{m,M}(d)=m-|e-(M-m)|.
$$


Then the row-nullity is


$$
\boxed{
\dim\ker_{\rm row}A_{m,M}(d)=
\begin{cases}
\dfrac{\max(0,n_{m,M}(d))}{2},
   &e\equiv M+1\pmod3,\\[2mm]
0,&e\not\equiv M+1\pmod3.
\end{cases}
}
\tag{13.1}
$$



### Proof

In the $M$-dimensional representation (10.2), a combination of the first $m$ rows of $B_\omega$ has polynomial form


$$
f(z)=p(z)^{M-m}g(z),\qquad \deg g<m.
\tag{13.2}
$$


This follows directly from the high-digit tensor factors: their first row contributes


$$
\prod_{i=\log_2m}^{\log_2M-1}
(1+\omega^{2^i}z^{2^i})
=p^{M-m}.
$$



The kernel spaces from Theorem 10.1 are explicit.

If $e\equiv M+1\pmod3$, the kernel consists of


$$
f=p^eh,\qquad h(z+1)=h(z),\qquad \deg h<M-e.
$$


If $e\ge R$, equation (13.2) requires


$$
g=p^{e-R}h,
$$


leaving invariant polynomials of degree less than $M-e$.

If $e<R$, invariance of $h=p^{R-e}g$ forces divisibility by both
$p^{R-e}$ and $q^{R-e}$, because translation interchanges $p$ and $q$ up to nonzero scalars. Since $pq=1+z+z^2$ is translation-invariant, one obtains


$$
g=q^{R-e}h_0,\qquad
h_0(z+1)=h_0(z),
$$


with


$$
\deg h_0<2m-M+e.
$$


These two dimensions are exactly the first line of (13.1).

The other possible kernel of the full $M$-block has form


$$
f=q^{M-e}h,\qquad h(z+1)=h(z),\qquad \deg h<e.
$$


For such an $f$ to be divisible by $p^R$, the invariant polynomial $h$ must be divisible by both $p^R$ and $q^R$. Its degree would then be at least


$$
2R\ge M>e,
$$


unless it is zero. Thus this second kernel contributes no dependency among the first $m$ rows. ∎

Now take the first $2m$ rows and first $2M$ columns of the normalized contact matrix. After the finite column transformation and parity reordering, it is


$$
\begin{pmatrix}
C_{m,M}&A_{m,M}\\
A_{m,M}&0
\end{pmatrix}.
$$


It has full row rank $2m$ if and only if $A_{m,M}$ has full row rank $m$.

Therefore (13.1) is an evaluated source-unit completion criterion:

> Whenever the right side of (13.1) is zero, some $2m$ actual original return columns among $0,\ldots,2M-1$ give a unit normalized contact minor on jet rows $0,\ldots,2m-1$.

Finite Cauchy–Binet transfers this existence from the triangularly transformed matrix back to the original normalized parity matrix. Adding the atom in jet row $2m$, with the full payment $\mathcal B'_{2m+1}$, then gives an attaining top-source minor at the corrected depth $b'_{2m+1}$.

This proves source-basis existence at explicitly characterized growing widths. It does not yet specify a nested list of complete corrected pivots or their odd interpolation denominators.

---

## 14. What transfers to complete corrected cofactors

The established complete cofactor criterion may be reused with the stronger source divisor.

For $q\le d$, define


$$
c_q=q(q-1)+2\sum_{j=0}^{q-1}v_2(j!),
$$




$$
E_q^F
=\sum_{r=0}^{q-1}\sum_{s=1}^r(1+v_2(d-s)),
$$


and


$$
\boxed{
t'_q=c_q+2E_q^F+b'_q.
}
\tag{14.1}
$$



If an actual selected source minor attains $b'_q$, and


$$
\boxed{t'_q<L_d,\qquad L_d=\alpha-12,}
\tag{14.2}
$$


then the already established complete Cauchy–Binet argument gives


$$
v_2(\operatorname{content}_q(\mathcal C^{[q]}))=t'_q
$$


and the same normalized Vandermonde row residues.

All hypotheses now have explicit meanings:

- the source-unit hypothesis is supplied, for the stated cases, by Corollary 12.1 or Section 13;
- the source payment is the full $\mathcal B'_q$;
- the factorial-adjugate weights remain $E_q^F$;
- the complete forcing remains (2.12);
- both bottom corrections remain in the exact columns;
- the strict inequality (14.2) is still required.

This is a conditional complete-cofactor consequence with an evaluated source hypothesis. It is not a theorem permitting deletion of corrections beyond $L_d$.

The window remains only $O(\sqrt d)$. Indeed,


$$
t'_q\ge t_q\ge\frac52q(q-1),
$$


whereas $L_d=O(d)$.

---

## 15. The precise correction obstruction, with evaluated correction jets

The source similarity does not normalize the complete corrected pencil. The discrepancy can be stated explicitly in the original objects.

Let


$$
\delta_k=2^{2\beta}\delta_k^\circ,
\qquad \delta_k^\circ\ \text{odd}.
$$


Since


$$
\Delta^r\sigma_m=2D_r\eta_r^{(m)},
$$


the contact correction in (2.14) is exactly


$$
\boxed{
E_r(i)
=2^{L_d}\delta_k^\circ\eta_r^{(d+i)}.
}
\tag{15.1}
$$


Its residual-row jets are


$$
\boxed{
\Delta_i^jE_r(i)
=
2^{L_d+j}\delta_k^\circ(r+1)_j
\eta_{r+j}^{(d+i)}.
}
\tag{15.2}
$$



Thus the bottom correction has the rising factor $(r+1)_j$, not the top-source factor $(d+1)_j$. This is a concrete reason why the new top-source normalization cannot be silently imposed on the whole pencil.

The atom correction remains


$$
\boxed{
E_{\mathsf a}(i)
=\frac{\delta_k}{2^{d+2}}c_{d+i},
}
\tag{15.3}
$$


and its jets are obtained from the complete $c=u-w$, not from $u$ alone.

Both coefficient borders remain exactly (2.15). Their passage through any growing elimination still requires the actual Cramer divisions, odd pivot quotients, and row payments.

There is also the unavoidable rank obstruction:


$$
\operatorname{rank}\!\left(
RN_d[\mathsf a,t^{(0)},\ldots,t^{(d-1)}]
\right)\le d.
$$


The complete common-column matrix has $d+1$ columns. Therefore the retained corrections must eventually provide essential rank. A pure-source theorem, however strong, cannot finish all common-column elimination.

### Concrete follow-on obligation

The next corrected-layer lemma should use the evaluated source kernel spaces above together with the exact jets (15.2)–(15.3). It must determine, at and beyond $t'_q=L_d$:

1. which mixed source/correction compound first survives;
2. an attaining cofactor on actual residual physical rows;
3. every integral Cramer division and its actual odd quotient;
4. the contribution of both affine borders to the final joint coefficient depth.

At rank $d+1$, the pure $RN_dA$ compound is identically zero, so this lemma must explicitly identify a nonzero correction contribution rather than regard corrections as errors.

No such growing corrected-compound theorem is proved here.

---

## 16. Global arithmetic and analytic status

The actual remaining binary quantity is


$$
\boxed{
\nu_k^{[5]}
=
\min\bigl(v_2(P_{0,k}^{[5]}),v_2(P_{1,k}^{[5]})\bigr).
}
\tag{16.1}
$$


The proposed quadratic target remains


$$
\boxed{
\nu_k^{[5]}
\le\frac{15}{4}k^2-64+O(k\log k)
\quad(k=9^{18+32u}).
}
\tag{16.2}
$$



Neither an entry algorithm, an evaluated source rank, nor an attaining source minor supplies this upper bound.

The exact all-prime normalization remains


$$
\frac{|P_{1,k}^{[5]}|}{g_k^{[5]}}
=\frac{|H_{1,k}|}{G_k}=q_k,
$$




$$
\frac{|P_{0,k}^{[5]}+P_{1,k}^{[5]}(e+\pi)|}{g_k^{[5]}}
=\frac{|H_k(e+\pi)|}{G_k}
=\ell_k>0.
\tag{16.3}
$$



The other prime obligations remain separate:

- the established ternary content results give only their stated range for $v_3(G_k)$;
- they are not a substitute for the distinct higher ternary block theorem;
- the $p\ge5$ content descents and the HIGH large-prime exclusions are not consequences of source parity units;
- Uniform56 and the separately labelled endpoint or producer obligations receive no new status from this report.

The closed same-$H$ analytic estimate is reused without repetition:


$$
\log|H_k(e+\pi)|
\ge
4k^2\log k+
\left(15\log2-\frac92\log3+\frac4{85}\right)k^2
+o(k^2).
$$


The previously stated whole-error divergence implication remains conditional on the independent all-prime controls. In its intended application, that implication would retire this producer as a source of primitive whole-error decay; it would not decide the rationality of $e+\pi$.

The separate binary producer also remains separate, with its original


$$
b=9^{18+32u},\qquad n=4002b,
$$


reconstruction indices $0,\ldots,b$, physical terminal $z_b=0$, corrected columns


$$
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
$$


and complete return


$$
\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f.
$$


No source-kernel conclusion here is transferred to its contents, clearers, denominator, or final gcd.

---

## 17. Computation scope and proof-status ledger

No tools have been used. No original-index matrix, source array, old $9216$ filter check, $k32/k33$ computation, or fixed33 scan has been rerun.

No new bounded computation is indispensable, so **no computation is proposed**. The small arithmetic in Sections 7 and 12 is displayed algebraically. The growing conclusions follow from finite polynomial-space similarities and invariant-subspace proofs, not from extrapolation of a finite receipt.

The literature gate is retained at its stated scope. No unread external theorem, one-sided Hankel dilation theorem, or generic inverse theorem has been imported.

| Statement | Status |
|---|---|
| Full turn12 weighted source identity and $D_r=2^rr!$ payments | Established reuse; independently checked where used |
| Rising integer divisor $2^j(d+1)_j$ | **Parent claim passes; proved at all primes** |
| Distinction and exact relation between $U$ and $J$ | **Proved** |
| Joint kernel, Euler derivative, and scalar simplification | **Parent claim passes** |
| Finite triangular normalized-parity column operation | **Proved at its stated scope** |
| Literal Kronecker ratio and unit blocks $2,8,32$ | **Parent claim passes symbolically** |
| Specified source33 valuation $960$ | **Parent claim passes; top-source only** |
| Full rising source-minor divisor $\mathcal B'_q$ | **New proved all-prime formulation** |
| Impossibility of old nominal depth $b_q$ for $q\ge18$ | **New proved obstruction** |
| Explicit similarity (10.3) of the deformation matrix | **New proved all-order theorem** |
| Dyadic determinant, nullity, and full leading rank | **New evaluated all-order theorem** |
| Corrected-depth source attainment at certified dyadic sizes | **New proved source theorem** |
| Wider-column completion criterion (13.1) | **New evaluated source-rank theorem** |
| Complete cofactor transfer using $b'_q$ | **Conditional on the strict correction window** |
| Exact bottom-correction jets (15.2) | **Proved in the original corrected columns** |
| Growing corrected elimination and terminal coefficient-pair upper bound | **Open** |
| Other odd-prime descents, HIGH exclusions, Uniform56, higher ternary theorem | **Separate statuses unchanged** |
| Unconditional rationality or irrationality of $e+\pi$ | **Unresolved** |

---

## Final conclusion

The complete parent note passes its independent audit. Its exact integer rising divisor, joint kernel, finite parity-column operation, symbolic small unit blocks, and source33 depth $960$ are all valid with the stated boundaries and normalizations.

The main new result is the explicit finite similarity


$$
\boxed{
J_aT_m\!\left(
\left(\frac{1+\omega z}{1+\omega^2z}\right)^e
\right)
\sim
\omega^{2e}\mathsf J_{m-e}
\oplus
\omega^{m-e}\mathsf J_e,
\qquad e=d\bmod m.
}
$$


It evaluates the actual deformation at every dyadic order. In particular,


$$
\boxed{
\operatorname{rank}U_{2m}=2m-2\kappa_m(d),
}
$$


with the explicit cases in (10.8), and it gives genuine growing source-unit attainment at the corrected full rising normalization.

At the same time, the additional divisor proves that the older nominal source-unit depth is impossible at every rank $q\ge18$. Any continuation that still assumes that old depth must be repaired before it can be used.

The exact remaining bottleneck is the growing **corrected** compound calculation after the bottom corrections become visible, followed by joint control of the two complete terminal coefficients. The evaluated correction jets


$$
\Delta_i^jE_r(i)
=
2^{L_d+j}\delta_k^\circ(r+1)_j\eta_{r+j}^{(d+i)}
$$


show precisely why the top rising payment cannot be transferred unchanged to that layer.

All original indices, finite boundaries, complete forcing and returns, physical terminal, full $D_r$ divisions, odd scalars, actual contents and least simultaneous clearer, all-prime $G_k$, primitive $q_k$, and nonzero whole error $\ell_k$ have been retained. No unconditional rationality or irrationality conclusion for $e+\pi$ has been obtained.
