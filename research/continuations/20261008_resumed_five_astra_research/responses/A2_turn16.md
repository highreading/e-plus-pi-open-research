> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A2 Turn 16 — Audit of the complete excess-class reduction, evaluation of the next aggregate digit, and the actual terminal parity defect

## 1. Conclusions and scope

The rationality or irrationality of $e+\pi$ remains unresolved.

The main conclusions of this report are:

1. **The new A4 Turn 24 reduction modulo $2^{\mathcal L_p+3}$ passes.**  
   In particular, its assertion about **every** forcing/source pair $I,J$ is valid. A finite Newton expansion, with the full source divisors retained, supplies two additional binary factors for every such pair. Consequently, every nonminimal $N_d$-pair is invisible modulo $2^{\mathcal L_p+3}$. This is a separate verification of the reduction, not merely agreement about the first two zero digits.

2. **The requested next aggregate digit is zero. In fact, one further digit is zero as well.**  
   With
   

$$
D_k=\det[w_*,v^{(0)},\ldots,v^{(d)}],
   \qquad
   \mathfrak m_d=\min_{1\le p\le d}\mathcal L_p,
$$


   the new global result is
   

$$
\boxed{2^{\mathfrak m_d+4}\mid D_k.}
   \tag{1.1}
$$


   Thus
   

$$
\boxed{\frac{D_k}{2^{\mathfrak m_d+2}}\equiv0\pmod2,}
   \qquad
   \boxed{\frac{D_k}{2^{\mathfrak m_d+3}}\equiv0\pmod2.}
   \tag{1.2}
$$


   The proof evaluates the actual source and physical-pole jets modulo $4$. After the first two certified row divisions, both lifted rows are still in the span of the actual bottom parity rows. Two further divisions are therefore paid.

3. **On the retained infinite rotation interval, the parity corank is usually not two: it is explicitly linear in the parameters.**  
   Write
   

$$
d=2L+\varrho,\qquad L\ \text{dyadic},
$$


   and suppose
   

$$
\varrho\ge4\ \text{even},\qquad p\ge5,\qquad p+\varrho\le L-2.
   \tag{1.3}
$$


   For the actual normalized minimal-pair matrix $Z_p$,
   

$$
\boxed{
   \operatorname{corank}_{\mathbb F_2}\overline Z_p=
   \begin{cases}
   L-p-\varrho+1,&L\equiv1\pmod3,\\[2mm]
   p+\varrho+1,&L\equiv2\pmod3.
   \end{cases}}
   \tag{1.4}
$$


   These hypotheses hold, with linear slack, for every relevant near-minimum product count on the original interval
   

$$
\frac98\,2^{a_k}<k<\frac76\,2^{a_k},
   \qquad a_k=\lfloor\log_2 k\rfloor.
   \tag{1.5}
$$


   Hence an assumed unit $(n-2)$-minor would be wrong there. A source-specific unit block of the **actual** rank is constructed below.

4. **The parent convexity, all-pattern locality, and two-index weighted-partition results pass at their stated scopes.**  
   They are lower-payment and inventory results, not noncancellation theorems. Their $O(d\log d)$ and first-$d/8$-window conclusions are distinguished below from the sharper fixed-digit exclusions used in (1.1).

5. **A further linear-depth consequence is available on the same infinite original interval.**  
   For sufficiently large original indices in (1.5),
   

$$
\boxed{
   v_2(D_k)\ge
   \begin{cases}
   \mathfrak m_d+\lfloor L/16\rfloor+1,&L\equiv1\pmod3,\\[2mm]
   \mathfrak m_d+\lfloor d/8\rfloor+1,&L\equiv2\pmod3.
   \end{cases}}
   \tag{1.6}
$$


   This remains a **lower-divisibility theorem**. It supplies no upper bound for the complete linear coefficient, the complete constant coefficient, or their gcd.

No tools have been used. No old phase scan, source receipt, factorial table, or original-sized solve is repeated.

---

# Part I. Exact objects and arithmetic interface

## 2. Original domain, forcing, and physical terminal

Throughout the dyadic construction,


$$
\boxed{k=9^{18+32u},\quad u\ge0,\qquad d=k-1,\qquad n=d+2.}
\tag{2.1}
$$


In particular,


$$
v_2(d)=4,\qquad d\equiv2\pmod3,\qquad d\equiv208\pmod{256}.
$$



Retain


$$
a_0=1,\qquad a_j=1-ja_{j-1},
$$




$$
u_m=a_{2m},\qquad f_m=(2m)!,\qquad
w_m=(-1)^m,\qquad c_m=u_m-w_m,
$$


and


$$
\rho_0=0,\qquad \rho_{m+1}+\rho_m=\frac1{2m+1},
\qquad r_m=-f_m+4\rho_m.
$$



The complete returns are


$$
\sigma_m=u_{m+1}+u_m,
$$




$$
\boxed{\tau_m=-(2m+2)!-(2m)!+\frac4{2m+1}.}
\tag{2.2}
$$



Set


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),\qquad T_m=\Lambda_k\tau_m.
$$


Both factorial terms remain in $T_m$.

The top-source range is $0\le m<d$; the original return orders are $0\le r<d$; residual row $i$, $0\le i\le d+1$, is physical row $d+i$. Thus the retained terminal is


$$
\boxed{3d+1=3k-2,\qquad (6k-4)!,\qquad 6k-5.}
\tag{2.3}
$$



Put


$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1),\qquad
\mathcal A_dy=\Delta^d(P_dy),
$$


with the original row-operation payment


$$
\Omega_k=\prod_{m=0}^{d-1}P_d(m).
$$



For $b(t)=4t^2+6t+3$, the complete top forcing is


$$
F_k(m,j)=
-\Lambda_k\sum_{h=0}^d(-1)^h\binom dh
P_d(m+h)b(m+h+j)(2(m+h+j))!,
\qquad m,j<d.
\tag{2.4}
$$


The identity


$$
b(t)(2t)!=(2t+2)!+(2t)!
$$


makes the retention of both factorial terms explicit.

Write


$$
F_k=-\Lambda_kD_fK_dD_f,\qquad
D_f=\operatorname{diag}((2m)!)_{m<d}.
$$


The established oddness of all leading principal determinants of $K_d$ is reused.

Let


$$
h_d=(2d-2)!,\qquad
\beta=v_2(h_d),\qquad
\alpha=v_2((2d)!)=\beta+5,
$$




$$
N_d=(h_dD_f^{-1})\operatorname{adj}(K_d)(h_dD_f^{-1}),
$$




$$
\delta_k=\Lambda_k\det(K_d)h_d^2,
\qquad F_k^{-1}=-N_d/\delta_k.
$$



The complete bottom return is


$$
\boxed{
R(i,j)=
\frac{\Lambda_k}{2(d+i+j)+1}
-\frac{\Lambda_k}{4}b(d+i+j)(2(d+i+j))!,
}
\tag{2.5}
$$


for $0\le i\le d+1$, $j<d$.

Define


$$
\mathscr T(y)=RN_d(\mathcal A_dy)_{\rm top}
+\frac{\delta_k}{4}y_{\rm bot}.
\tag{2.6}
$$


It annihilates every original forcing column $T_j$, $j<d$.

Every Newton divisor is the full integer


$$
\boxed{D_r=2^rr!,}
\tag{2.7}
$$


including the divisor $D_d=2^dd!$ in the paired re-expression.

---

## 3. Both exact coefficient borders remain present

The complete corrected pencil is


$$
\mathcal Q_k(s)=
[x,z^{(0)},\ldots,z^{(d-1)},\mathfrak b_0+s\mathfrak b_1],
$$


where


$$
x=\frac{\mathscr T(c)}{2^d},
\qquad
z^{(r)}=\frac{\mathscr T(\Delta^r\sigma)}
{2^{\alpha+1}D_r},
$$




$$
\mathfrak b_0=\Lambda_k\mathscr T(r),
\qquad
\mathfrak b_1=\Lambda_k\mathscr T(w).
$$



The forcing annihilation gives the exact complete-border identity


$$
\boxed{\mathfrak b_0=\Lambda_k2^{-d}\mathscr T(\Delta^dr).}
\tag{3.1}
$$


Its right side contains both $-\Delta^df$ and $4\Delta^d\rho$.

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


The order-$d$ column is the proved re-expression of the existing border; it does not append a new original return.

The passed exact relations are


$$
z^{(r)}=v^{(r)}+(r+1)v^{(r+1)},\qquad
x=2^{\alpha-d}v^{(0)}-w_*.
$$


With


$$
a_r=(-1)^{d-r}\frac{d!}{r!},\qquad
\varkappa_d=2^{\alpha-d}d!,
\qquad
\mathfrak c_k=\Lambda_k2^\alpha d!,
$$


the determinant-one paired transformation gives


$$
\widehat{\mathcal Q}_k(s)=
\left[
\varkappa_dv^{(d)}-w_*,
\ (v^{(r)}-a_rv^{(d)})_{r<d},
\ \mathfrak b_0+s\mathfrak c_kv^{(d)}
\right].
$$



Writing


$$
\det\mathcal Q_k(s)=I_{0,k}+I_{1,k}s,
$$


both exact identities are retained:


$$
\boxed{I_{1,k}=-\mathfrak c_kD_k,}
\tag{3.2}
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
\tag{3.3}
$$



Nothing below replaces (3.3) by a $\theta$-only determinant.

---

## 4. Contents, clearers, all-prime gcd, and whole error

The original affine determinant remains


$$
H_k(s)=
\det\left[
(c_{m+j})\
\middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right]
=H_{0,k}+H_{1,k}s.
$$



The individual least right-column entry clearers are


$$
\Lambda_{k,j}=\operatorname{lcm}(1,3,\ldots,4k+2j-3).
$$



Retain the all-prime integers


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
\qquad
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


The actual least simultaneous coefficient clearer of $H_k/\Lambda_k^k$, and its content after clearing, are


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
}
\tag{4.1}
$$



For the original rectangles


$$
Z_k=
[(c_{m+j})_{m<2k,j<k}\mid(T_{m+j})_{m<2k,j<k-1}],
$$




$$
Y_k=
[(\sigma_{m+j})_{m<2k-1,j<k}\mid
(T_{m+j})_{m<2k-1,j<k}],
$$


their actual maximal-minor contents remain


$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
\mathscr L_k=\delta_{2k-1}(Y_k),
$$


with


$$
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k\mid \Lambda_k\mathscr L_k\mathscr R_k.
$$



The paid five-column interface is reused, not recalculated. In particular, with


$$
f_k=(-\Lambda_k)^d\det(K_d)
\left(\prod_{m<d}(2m)!\right)^2,
\qquad
\mathfrak D_d=\prod_{r<d}2^rr!,
$$


and $\lambda_d^{\rm tr}=d\alpha+4d+4$,


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_{5,k}|^{d-4}G_k
=
|f_k|\,2^{\lambda_d^{\rm tr}+d+69}
\mathfrak D_d\,g_k^{[5]}.
}
\tag{4.2}
$$


Every actual odd factor remains in this identity.

The primitive pair and the whole evaluated error remain


$$
q_k=\frac{|H_{1,k}|}{G_k}>0,\qquad
p_k=-\frac{(-1)^kH_{0,k}}{G_k},
$$




$$
\boxed{
0<q_k(e+\pi)-p_k
=\frac{|H_k(e+\pi)|}{G_k}.
}
\tag{4.3}
$$


No local binary divisor is substituted for $G_k$, and no selected summand is substituted for the positive whole error.

---

# Part II. Independent audits of the parent locality results

## 5. Nominal terminal cost and exact convexity

Let


$$
A_d=v_2(d!)=\alpha-d,\qquad
L_d=\alpha-12,
$$




$$
\gamma_k=\Lambda_k\det(K_d)\operatorname{odd}(h_d)^2.
$$


Then


$$
[w_*,v^{(0)},\ldots,v^{(d)}]
=
RN_d[\mathsf a_w,\mathsf v^{(0)},\ldots,\mathsf v^{(d)}]
+
2^{L_d}\gamma_k[2^{A_d}w,\theta_0,\ldots,\theta_d].
\tag{5.1}
$$



Use


$$
\lambda_j=j+v_2(j!),\qquad
S_b=\sum_{j=0}^{b-1}\lambda_j,
$$




$$
e_j=v_2\!\left(\frac{h_d}{(2j)!}\right),\qquad
E_p=\sum_{j=d-p}^{d-1}e_j,
$$




$$
B_p=\binom p2+\sum_{j=0}^{p-2}v_2((d+1)_j).
$$


The nominal payment is


$$
\boxed{
\mathcal L_p=(n-p)L_d+S_p+S_n+2E_p+B_p.
}
\tag{5.2}
$$


The formal all-bottom cost is $\mathcal L_0=nL_d+S_n$.

Let $s(x)=s_2(x)$. Direct subtraction gives


$$
\Delta_p:=\mathcal L_{p+1}-\mathcal L_p
=
8p-2d+5-s(p)+2s(d-p-1)-s(d+p-1).
\tag{5.3}
$$


For $1\le p\le d-2$,


$$
\begin{aligned}
\Delta_{p+1}-\Delta_p
&=8-\bigl(1-v_2(p+1)\bigr)\\
&\quad+2\bigl(-1+v_2(d-p-1)\bigr)
-\bigl(1-v_2(d+p)\bigr)\\
&=\boxed{4+v_2(p+1)+2v_2(d-p-1)+v_2(d+p)}.
\end{aligned}
\tag{5.4}
$$


All valuation arguments are positive. The terminal shift is $d-p-1$, not $d-p$.

Thus the parent convexity theorem passes. If


$$
p_*=\min\{p:\Delta_p\ge0\},
$$


the complete minimizer set is


$$
\{p_*\}\quad(\Delta_{p_*}>0),
\qquad
\{p_*,p_*+1\}\quad(\Delta_{p_*}=0).
\tag{5.5}
$$



Writing $\mathfrak m_d=\mathcal L_{p_*}$, summation of (5.4) gives


$$
\mathcal L_{p_*+t}-\mathfrak m_d\ge2t(t-1),
$$




$$
\mathcal L_{p_*-t}-\mathfrak m_d\ge2t(t-1)+t.
\tag{5.6}
$$


Consequently, every nominal competitor through excess $B$ satisfies


$$
\boxed{|p-p_*|\le T_B:=\frac{1+\sqrt{1+2B}}2.}
\tag{5.7}
$$



In particular, through excess $3$, only $p_*-1,p_*,p_*+1$ can occur, subject to their actual costs. No equality or parity distribution is assumed.

Bisection requires $O(\log d)$ digit evaluations; the parent’s stated ordinary bit-cost qualification is appropriate.

---

## 6. All-$p$, all-$v$ forcing comparison

Let


$$
b_d=1+\lfloor\log_2d\rfloor.
$$


A term has $p$ product columns, $v$ factorial-forcing columns, and


$$
a=p-v,\qquad h=n-p.
$$



Write


$$
R=R^{\rm C}-2^{\alpha-2}V,
$$


where


$$
R^{\rm C}(i,j)=\frac{\Lambda_k}{2(d+i+j)+1}.
$$



For an actual factorial forcing column $j$,


$$
g_j=v_2((2(d+j))!)-\alpha,
$$


and


$$
e_j+g_j
=2d+s_2(j)-s_2(d+j)-5
\ge2d-b_d-6.
\tag{6.1}
$$



The full source payment is $B_p$ when the atom is in the product. If the atom is a bottom correction, all top sources are contact sources and the payment is stronger by


$$
b_p^{\rm at}:=v_2((d+1)_{p-1}).
\tag{6.2}
$$



The mixed Cauchy/bottom-jet payment is


$$
c_a+\sum_{j=a}^{n-v-1}\lambda_j,
\qquad c_a=2S_a.
$$


This remains valid at $a=0$: the empty Cauchy determinant is $1$, and the remaining statement is the ordinary finite bottom-jet payment. No Cauchy denominator is divided out in that case.

The source/adjoin diagonal bill is at least


$$
E_p+E_a+v(2d-b_d-6).
$$


Subtracting $\mathcal L_p$ yields the parent comparison before any positivity test.

The finite bounds


$$
E_p-E_a\le v(2p+b_d),\qquad
c_p-c_a\le4pv
$$


are immediate from the corresponding marginal sums. Also


$$
\lambda_{b+h}-\lambda_b
=2h-s_2(b+h)+s_2(b)
\le2h+b_d.
$$


Every index here is at most $d+1<2^{b_d}$ on the original family.

Combining these inequalities gives


$$
\boxed{\text{pattern payment}\ge \mathcal L_p+vM_p,}
\qquad
M_p=\alpha-4p-3b_d-12.
\tag{6.3}
$$



This derivation is valid for all $0\le v\le p\le d$, including $a=0$. The restriction $p\le d/3$ was needed only to make $M_p$ positive.

### 6.1 Negative $M_p$ and the all-bottom sector

Uniformly for $0\le p\le d$,


$$
\mathcal L_p=3d^2-2dp+4p^2+O(db_d),
$$


because


$$
S_p=p^2+O(pb_d),\quad
E_p=p^2+O(pb_d),\quad
B_p=p^2+O(pb_d).
$$


If $M_p<0$, then $v\le p$ gives


$$
\text{payment}\ge\mathcal L_p+pM_p
=3d^2+O(db_d).
$$


Since


$$
\mathfrak m_d=\frac{11}{4}d^2+O(db_d),
$$


these terms have a quadratic gap from the minimum.

At $p=0$, the complete all-bottom matrix pays


$$
nL_d+S_n=3d^2+O(db_d).
$$


The bottom atom factor $2^{A_d}$ pays its missing factorial valuation because


$$
v_2(j!)\le v_2((d+1)!)=A_d,\qquad j\le d+1.
$$


Thus the $p=0$ sector is also paid, without an invented source or Cauchy minor.

### 6.2 The parent locality conclusions

At excess $B=O(db_d)$, every remaining pattern has


$$
|p-p_*|\le T_B
$$


and


$$
M_p\ge d-8b_d-20-4T_B>0
$$


at sufficiently large original indices. Therefore


$$
v\le
\frac{B-(\mathcal L_p-\mathfrak m_d)}{M_p}
=O(\log d).
\tag{6.4}
$$



At $B=\lfloor d/8\rfloor$, both $M_p>B$ and


$$
b_p^{\rm at}
=p-1+s_2(d)-s_2(d+p-1)
\ge p-1-b_d>B
$$


hold throughout the localized strip, for sufficiently large original indices.

Hence the complete determinant through that first linear-width window comes only from pure-Cauchy, product-atom patterns.

**Audit verdict: PASS at the stated sufficiently-large-original-index scope.**

These conclusions are broader than a fixed-digit exclusion, but do not evaluate any retained aggregate.

### 6.3 The sharper fixed-digit exclusion already available

For the global fixed-digit argument, the stronger A2 Turn 15 comparison is retained:


$$
\mathcal F(p,v)\ge
\mathcal L_a+
v(4a+3v-3b_d-2),\qquad a=p-v.
\tag{6.5}
$$


If $p\ge b_d+2$, the last factor is at least $4$. If $p\le b_d+1$, the small-$p$ nominal gap gives


$$
\mathcal F(p,v)-\mathfrak m_d
\ge
2d-3b_d^2-17b_d-21>4.
$$


The original indices are far beyond this elementary inequality’s threshold.

Thus, on every original index,


$$
\boxed{\text{every factorial-forcing term has depth at least }
\mathfrak m_d+4.}
\tag{6.6}
$$



This fixed-digit global bound and the parent’s wider asymptotic locality theorem are different statements; neither is being substituted for the other.

---

## 7. Audit of the two-index weighted partition inventory

For $1\le t\le d-1$,


$$
e_{t-1}-e_t=1+v_2(t).
\tag{7.1}
$$


For $I=\{i_0<\cdots<i_{p-1}\}$, set


$$
t_a=d-p+a,\qquad \lambda_a=t_a-i_a.
$$


Then


$$
d-p\ge\lambda_0\ge\cdots\ge\lambda_{p-1}\ge0.
$$


Conversely every partition in that rectangle produces one and only one original index set.

The exact excess is


$$
\begin{aligned}
W_{d,p}(\lambda)
&=\sum_a\sum_{t=t_a-\lambda_a+1}^{t_a}(1+v_2(t))\\
&=\boxed{2|\lambda|+\sum_a
\bigl(s_2(t_a-\lambda_a)-s_2(t_a)\bigr)}.
\end{aligned}
\tag{7.2}
$$


No $v_2(0)$ occurs. At $p=d$, the rectangle is empty.

A second, independent partition $\mu$ is required for $J$. The diagonal excess is


$$
W_{d,p}(\lambda)+W_{d,p}(\mu),
$$


not a one-index weight.

Since $W(\lambda)\ge|\lambda|$, the parent’s suffix locality and its bound


$$
\#\{(\lambda,\mu):W(\lambda)+W(\mu)\le b\}
\le e^{5\sqrt b}
\tag{7.3}
$$


follow exactly as stated. The generating-function estimate is a reuse/application of the classical partition product, not a new partition theorem.

For completeness, the loss-$\le2$ inventory is indeed:

- the minimal pair $(T_p,T_p)$, loss $0$;
- for odd $p$, either one-set shift $(T_p^-,T_p)$, $(T_p,T_p^-)$, loss $1$;
- for odd $p$, the double shift $(T_p^-,T_p^-)$, loss $2$;
- for even $p$ with $v_2(d-p)=1$, either one-set shift, loss $2$.

All other admissible nonempty shapes contain $(2)$ or $(1,1)$, whose weight is at least $3$. Forbidden rectangle shapes are simply absent. At $p=d$, only the full pair exists.

**Audit verdict: PASS.** This is an inventory of diagonal weights. It does not assert oddness of any complementary $K_d$-minor or nonvanishing of any aggregate.

---

# Part III. Different audit of A4 Turn 24, Sections 15–17

## 8. The exact fixed-$I,J$ aggregate and its source normalization

Fix $|I|=|J|=p$. Put


$$
Q_I(i)=\prod_{b\in I}(2(d+i+b)+1).
$$


The exact Cauchy identity contributes


$$
C_p(I)=
\frac{\Lambda_k^p2^{p(p-1)}\Phi_pV(I)}
{\prod_{i=0}^{n-1}Q_I(i)},
\qquad
\Phi_p=\prod_{j=0}^{p-1}j!.
\tag{8.1}
$$


The normalized factor $V(I)/\Phi_p$ is an integer. All displayed denominators are odd.

After summing over **all** product-contact column choices, the result is a block determinant with:

- the $p$ actual top source rows;
- bottom rows
  

$$
\Delta^j(Q_I\theta_r^{(d+\bullet)})(0),
  \qquad p\le j\le d+1;
$$


- bottom atom coordinate $0$.

Thus this is a complete Laplace aggregate, not one contact minor.

Expand the actual source rows $J\subseteq\{0,\ldots,d-1\}$ in the finite Newton basis at $0$. For


$$
U=\{u_0<\cdots<u_{p-1}\}\subseteq\{0,\ldots,d-1\},
$$


the coefficient is a determinant of binomial coefficients and is integral.

Write


$$
\mathcal R_j=(d+1)_j.
$$


The exact source factor for $U$ is


$$
\mathcal F(U)=
2^{\sum_a u_a}\prod_{a=0}^{p-2}\mathcal R_{u_a}.
\tag{8.2}
$$


Indeed, multiply the atom column by $\mathcal R_{u_{p-1}}$, then divide top row $u_a$ by $2^{u_a}\mathcal R_{u_a}$. The normalized atom entry is


$$
\frac{\mathcal R_{u_{p-1}}}{\mathcal R_{u_a}}
\frac{\Delta^{u_a}\mathsf a_w(0)}{2^{u_a}},
$$


and the normalized contact entries are integral.

The minimal factor is


$$
\mathcal F_p=2^{\binom p2}\prod_{j=0}^{p-2}\mathcal R_j.
$$


If


$$
\sigma(U)=\sum_a(u_a-a),
$$


then


$$
\boxed{v_2(\mathcal F(U)/\mathcal F_p)\ge\sigma(U).}
\tag{8.3}
$$



This verifies the source normalization for every $J$, including its actual finite upper boundary.

---

## 9. Why every $I,J$ receives two extra factors

Let


$$
\mathbf K_q(j,r)=
\sum_{t=0}^q\binom qt\binom{r+j+t}{r}\theta_{r+j+t},
\tag{9.1}
$$


and use a bar for reduction modulo $2$. The established source and bottom parity formulas give


$$
\overline{\mathbf K_d(j)}
=(1+E)^{d-p}\overline{\mathbf K_p(j)}.
\tag{9.2}
$$



For the zero-excess source pattern


$$
U_0=\{0,\ldots,p-1\},
$$


the first two normalized atom entries are even when $p\ge3$. The bottom rows contain orders


$$
0,\ldots,d+1-p.
$$


Consequently, top rows $0$ and $1$ give two independent relations:


$$
\overline{\mathbf K_d(0)}
=\sum_{t=0}^{d-p}\binom{d-p}{t}
\overline{\mathbf K_p(t)},
$$




$$
\overline{\mathbf K_d(1)}
=\sum_{t=0}^{d-p}\binom{d-p}{t}
\overline{\mathbf K_p(t+1)}.
\tag{9.3}
$$


Both lie within the physical bottom cutoff.

There is only one source pattern of excess $1$:


$$
U_1=\{0,\ldots,p-2,p\}.
$$


Its normalized atom is supported only at the last row modulo $2$, since


$$
\mathcal R_p/\mathcal R_{p-2}=(d+p-1)(d+p)
$$


is even. Its first two contact rows are again $\overline{\mathbf K_d(0)}$ and $\overline{\mathbf K_d(1)}$, with zero atom coordinates, so the same two relations apply.

All other patterns have source excess at least $2$.

Therefore every fixed-$I,J$ atom-product Cauchy aggregate has two extra binary factors after its universal nominal payment. This proves the crucial assertion of A4 Section 15 independently.

The factorial-adjugate weight is


$$
w(I,J)=
\sum_{i\in I}e_i+\sum_{j\in J}e_j-2E_p.
$$


Strict decrease of the $e_j$ gives


$$
w(I,J)=0\iff I=J=T_p.
$$


Every nonminimal pair has $w(I,J)\ge1$. Hence


$$
\boxed{\text{every nonminimal pair has depth at least }
\mathcal L_p+3.}
\tag{9.4}
$$



This pays the one-set and double-shift competitors in the parent inventory. No value of either near-boundary inverse return $\zeta_p^\pm$ is needed at this precision.

### 9.1 Bottom atom, including $p=3,4$

For $p\ge5$, $b_p^{\rm at}\ge3$. For $p=3,4$, it equals $1$, so another argument is needed.

At the leading all-contact source pattern, expand in the bottom atom column. The remaining contact rows all lie in


$$
\operatorname{span}\{
\overline{\mathbf K_p(0)},\ldots,
\overline{\mathbf K_p(d-1)}
\}.
$$


There are $d+1$ contact columns but at most $d$ spanning rows. Thus that leading layer is zero. Every higher source pattern already pays one more factor.

This supplies the second factor for $p=3,4$, exactly as required.

### 9.2 Minimal scalar and pre-division precision

For $I=J=T_p$, Jacobi’s identity gives


$$
\det N_d[T_p,T_p]
=
\left(\prod_{j\in T_p}\frac{h_d}{(2j)!}\right)^2
\det(K_d)^{p-1}
\det K_d[0{:}d-p-1,0{:}d-p-1].
$$


Its normalized quotient by $2^{2E_p}$ is odd.

The exact odd prefactor is


$$
\begin{aligned}
u_p={}&
\gamma_k^{n-p}\Lambda_k^p
\frac{\det N_d[T_p,T_p]}{2^{2E_p}}
\operatorname{odd}(\Phi_p)^2\\
&\times
\frac{\mathcal F_p}{2^{B_p}}
\frac{\prod_{j=p}^{n-1}\operatorname{odd}(j!)}
{\prod_{i=0}^{n-1}Q_{T_p}(i)}.
\end{aligned}
\tag{9.5}
$$


It is an actual unit in $\mathbb Z_{(2)}$, not the integer $1$.

The resulting matrix is exactly A4’s $Z_p$, with top base $d-p$ and physical poles $T_p$. Thus


$$
\boxed{
\mathcal D_p\equiv
2^{\mathcal L_p}u_p\det Z_p
\pmod{2^{\mathcal L_p+3}},
\quad 5\le p\le d/3.
}
\tag{9.6}
$$



**Audit verdict: PASS.** The nonminimal-pair payment is valid independently of the agreement on two zero digits.

---

# Part IV. New modulo-$4$ evaluation

## 10. Actual $\theta$-values and physical-base correction

The exact recurrence is


$$
\theta_0=1,\qquad\theta_1=0,\qquad
\theta_{r+1}=(2r+1)\theta_r+\theta_{r-1}.
\tag{10.1}
$$


It proves integrality.

Modulo $4$, the two-step matrix on
$(\theta_{2s+1},\theta_{2s})^T$ is


$$
M=\begin{pmatrix}0&1\\3&1\end{pmatrix},
\qquad M^3=-I.
$$


Thus


$$
\theta_{r+6}\equiv-\theta_r\pmod4.
\tag{10.2}
$$


This is a short recurrence derivation, not a factorial-table computation.

The exact physical-base formula gives


$$
\boxed{
\theta_r^{(b)}
\equiv
\theta_r+2b(r+1)\theta_{r+1}\pmod4.
}
\tag{10.3}
$$


Terms of order at least $2$ in the base expansion contain $4$.

This base correction must be retained before division by $2$.

---

## 11. The actual top source modulo $4$

Let


$$
o_d=\frac{d!}{2^{v_2(d!)}},
\qquad
Q_h(b)=\prod_{a=h}^{d-1}(2b+2a+1).
$$


The complete normalized product formula is


$$
\frac{\Delta^j\mathsf v_b^{(r)}}{2^j\mathcal R_j}
=
o_d\sum_{h=0}^d
\binom dh Q_h(b)
\binom{d-h+r+j}{r}
\theta_{d-h+r+j}^{(b+h)}.
\tag{11.1}
$$



Because $16\mid d$, a term $\binom dh$ visible modulo $4$ has $8\mid h$. Indeed,


$$
v_2\binom dh\ge v_2(d)-v_2(h).
$$


For such $h$, both $h$ and $d-h$ are divisible by $8$, and


$$
Q_h(b)\equiv1\pmod4.
$$


The physical base $b+h$ has parity $b$.

Using (10.3) and writing $t=d-h$, we obtain


$$
\boxed{
o_d^{-1}
\frac{\Delta^j\mathsf v_b^{(r)}}{2^j\mathcal R_j}
\equiv
\mathbf K_d(j,r)
+2b(j+1)\mathbf K_d(j+1,r)
\pmod4.
}
\tag{11.2}
$$


The replacement of $j+t+1$ by $j+1$ in the second term is legitimate only modulo $2$, after its displayed factor $2$: every contributing odd $\binom dt$ has even $t$.

The atom is equally explicit. From the full atom formula, every summand with $h\ge1$ contains $d$, while $P_d(b)\equiv1\pmod4$. Therefore


$$
\boxed{
\frac{\Delta^j\mathsf a_w(b)}{2^j}
\equiv(-1)^{b+j}\pmod4.
}
\tag{11.3}
$$


Consequently the actual top atom entry is


$$
\frac{\mathcal R_{p-1}}{\mathcal R_j}(-1)^{b+j}\pmod4
$$


for $Z_p$, with the corresponding maximal-order ratio for a general source pattern.

The odd number $o_d$ has not been discarded: we divide each top row by it in the auxiliary local calculation and restore the exact determinant factor $o_d^p$.

---

## 12. The actual physical-pole jets modulo $4$

For arbitrary $I$, $|I|=p$, put


$$
s_I=\sum_{b\in I}(d+b).
$$


Define


$$
q_\ell=\frac{\Delta^\ell Q_I(0)}{2^\ell\ell!}.
$$


Expansion of $Q_I$ in powers of $i$, followed by
$\Delta^\ell i^t|_{i=0}=\ell!S(t,\ell)$, gives


$$
\boxed{
q_\ell\equiv
\binom p\ell
+2s_I\binom{p-1}\ell
+2\binom{\ell+1}{2}\binom p{\ell+1}
\pmod4.
}
\tag{12.1}
$$


Only the powers $i^\ell$ and $i^{\ell+1}$ can survive after the normalization modulo $4$.

Let


$$
\mathbf B_z(r)=
\frac{\Delta_i^{p+z}
\bigl(Q_I(i)\theta_r^{(d+i)}\bigr)|_{i=0}}
{2^{p+z}(p+z)!}.
$$


The shifted product rule, (10.3), and (12.1) yield


$$
\boxed{
\mathbf B_z
\equiv
\mathbf K_p(z)
+2\left[
\bigl(s_I+p(z+1)\bigr)\mathbf K_{p-1}(z+1)
+\binom p2\mathbf K_{p-2}(z+1)
\right]
\pmod4.
}
\tag{12.2}
$$



Here is the calculation of the base-shift term. It is


$$
2\sum_{\ell=0}^p
\ell\binom p\ell(p+z-\ell+1)\mathbf H_{p+z-\ell+1},
$$


where


$$
\mathbf H_j(r)=\binom{r+j}{r}\theta_{r+j}.
$$


Using $\ell\binom p\ell=p\binom{p-1}{\ell-1}$, its residue becomes


$$
2p(z+1)\mathbf K_{p-1}(z+1);
$$


the remaining term has the even factor $p(p-1)$ and disappears modulo $4$.

Thus (12.2) includes both the actual pole correction $s_I$ and the actual physical-base correction.

For the minimal poles $I=T_p$, with $b=d-p$,


$$
s_I\equiv p+\binom p2\pmod2.
$$


Hence


$$
\boxed{
\mathbf B_z
\equiv
\mathbf K_p(z)+
2\left[
pz\,\mathbf K_{p-1}(z+1)
+\binom p2\mathbf K_{p-2}(z+2)
\right]\pmod4.
}
\tag{12.3}
$$



These formulas evaluate the required modulo-$4$ entries from the original source and physical poles. They are not symbolic-matrix assumptions.

---

## 13. Both first lifts return to the actual bottom row span

Put


$$
D=d-p.
$$


Divide the top rows by the actual odd unit $o_d$. For $j=0,1$, form the exact row


$$
\mathbf R_j=
\text{top row }j-
\sum_{t=0}^D\binom Dt\,\text{bottom row }j+t.
\tag{13.1}
$$


These rows are even by the two parity relations.

Using (11.2) and (12.2), the contact part of $\mathbf R_j/2$ has parity


$$
\begin{aligned}
\mathbf F_j^{(b,I)}
={}&b(j+1)\overline{\mathbf K_d(j+1)}\\
&+\bigl(s_I+p(j+1)\bigr)
\overline{\mathbf K_{d-1}(j+1)}\\
&+pD\,\overline{\mathbf K_{d-2}(j+2)}
+\binom p2\,\overline{\mathbf K_{d-2}(j+1)}.
\end{aligned}
\tag{13.2}
$$



Every row on the right belongs to the span of the available bottom rows.

- For $j=0$, the largest required bottom order is $D+1$.
- For $j=1$, the potentially too-high term has coefficient $b(j+1)=2b=0$ in $\mathbb F_2$; all remaining orders are at most $D+1$.

Thus the physical cutoff $p+(D+1)=d+1$ is respected exactly.

When $p\ge5$, the first two atom entries have valuation at least $3$, because their rising-factor ratios contain $d+2$ and $d+4$. After the first division by $2$, their atom coordinates are still even.

Choose integer $0/1$ lifts of the bottom-row coefficients in (13.2). Subtract those bottom combinations from $\mathbf R_j/2$. Both resulting rows are even and may be divided by $2$ once more.

Therefore


$$
\boxed{16\mid\det Z_p,\qquad 5\le p\le d/3.}
\tag{13.3}
$$



For the minimal source base and poles, the evaluated lifts simplify to


$$
\boxed{
\begin{aligned}
\mathbf F_0&=
p\,\overline{\mathbf K_d(1)}
+\left(p+\binom p2\right)
\overline{\mathbf K_{d-2}(2)},\\
\mathbf F_1&=
p\,\overline{\mathbf K_{d-2}(2)}
+\binom p2\,\overline{\mathbf K_{d-2}(3)}.
\end{aligned}}
\tag{13.4}
$$


This is the complete first-lift evaluation at the requested precision.

No unit $(n-2)$-minor was assumed.

---

## 14. Four extra factors for every forcing/source pair

The preceding argument is not confined to the minimal source pattern.

If $\sigma(U)\le3$ and $p\ge5$, then $U$ contains both $0$ and $1$. Indeed:

- omitting $0$ costs at least $p$;
- retaining $0$ but omitting $1$ costs at least $p-1\ge4$.

For every such $U$, the first two normalized source rows are precisely the rows used in (13.1), and their atom ratios have valuation at least $3$. Hence the same two successive lifts pay four factors.

If $\sigma(U)\ge4$, the source factor (8.3) already pays four factors.

We have therefore proved the stronger universal statement


$$
\boxed{
\text{every fixed-\(I,J\) pure-Cauchy product-atom aggregate has depth }
\ge \mathcal L_p+w(I,J)+4
}
\tag{14.1}
$$


for $5\le p\le d/3$, with the nonnegative Cauchy excess and any complementary-minor valuation still retained.

This strengthens the audited A4 reduction:

- weight-one inverse-return pairs cannot enter before $\mathcal L_p+5$;
- weight-two pairs cannot enter before $\mathcal L_p+6$;
- their actual odd residues are not needed at the digit requested here.

### 14.1 Bottom atoms at the fourth-factor precision

For every $p\ge3$, the leading bottom-atom contact determinant is singular by the span argument in Section 9.1. Thus the complete bottom-atom contribution has depth at least


$$
\mathcal L_p+b_p^{\rm at}+1.
\tag{14.2}
$$


For $p\ge5$, $b_p^{\rm at}\ge3$, so this is at least $\mathcal L_p+4$.

On $p\le d/3$, the factorial correction margin $M_p$ is much greater than $4$ at the original indices.

Consequently,


$$
\boxed{
2^{\mathcal L_p+4}\mid\mathcal D_p,
\qquad 5\le p\le\lfloor d/3\rfloor.
}
\tag{14.3}
$$



---

## 15. Evaluation of the whole next digit

Every count with


$$
\mathcal L_p\le\mathfrak m_d+3
$$


lies in the original logarithmic strip around $d/4$, hence in $5\le p\le d/3$. Those complete sectors are covered by (14.3).

Every other no-factorial count already has nominal depth at least $\mathfrak m_d+4$. This includes the remote small-$p$ and all-bottom cases after their complete atom payment.

Every factorial-forcing term is covered globally by (6.6).

Therefore


$$
\boxed{
D_k\in2^{\mathfrak m_d+4}\mathbb Z
}
$$


on every original index, proving (1.1)–(1.2).

All nominally eligible adjacent product counts, both Cauchy–Binet index sets, the first-two weighted inventories, all atom positions, and all forcing patterns have been included. No selected $p$-sector decides the result.

The odd factors in (9.5), the orientation signs, and the actual $N_d$-minors remain in the exact expansion. Since every complete retained group is already zero at the requested precision, their residues modulo $4$ cannot change the evaluated zero.

---

# Part V. The actual parity rank on the retained infinite interval

## 16. Reduction of the full contact row space

This section determines the exact corank under (1.3). It does not infer terminal rank from the earlier mixed $\eta$-window.

After eliminating the unit atom coordinate, the contact rows have the passed forms:

- for odd $p$,
  

$$
\overline{\mathbf K_d(0)},\ldots,
  \overline{\mathbf K_d(p-2)};
$$


- for even $p$,
  

$$
\overline{\mathbf K_d(0)},\ldots,
  \overline{\mathbf K_d(p-3)},
  \quad
  \overline{\mathbf K_d(p-2)}+\overline{\mathbf K_d(p-1)}.
$$



The bottom rows are


$$
\overline{\mathbf K_p(0)},\ldots,
\overline{\mathbf K_p(D+1)}.
$$



Using (9.2), a monic triangular row reduction gives the exact contact row spaces


$$
\boxed{
\begin{cases}
\operatorname{span}\{\overline{\mathbf K_p(0)},\ldots,
\overline{\mathbf K_p(d-2)}\},&p\text{ odd},\\[1mm]
\operatorname{span}\{\overline{\mathbf K_p(0)},\ldots,
\overline{\mathbf K_p(d-3)},
\overline{\mathbf K_p(d-2)}+\overline{\mathbf K_p(d-1)}\},
&p\text{ even}.
\end{cases}}
\tag{16.1}
$$


For even $p$, $D$ is even, so the final unreduced coefficients at orders $d-2,d-1$ are both $1$.

All these are row operations on the actual $d+1$ contact columns $0\le r\le d$.

---

## 17. A finite polynomial model of the actual parity rows

Work over $\mathbb F_4=\mathbb F_2(\omega)$, with


$$
\omega^2+\omega+1=0.
$$


The parity law is


$$
\theta_r=\operatorname{Tr}(\omega^{r+2}).
$$


For


$$
a=1+\omega Y,\qquad b=1+\omega^2Y,\qquad
S=ab=1+Y+Y^2,
$$


the row generating function is


$$
\sum_{r\ge0}\overline{\mathbf K_p(j,r)}Y^r
=
\operatorname{Tr}\left(
\omega^{j+2+2p}\frac{b^p}{a^{p+j+1}}
\right).
\tag{17.1}
$$



Let


$$
H=4L,\qquad q=2L-p.
$$


Under (1.3),


$$
d+2p\le H.
$$


Since $a^H\equiv1\pmod{Y^H}$, division of the contact columns by the binary unit $S^p$ transforms row $j$, $0\le j\le d-1$, into


$$
P_s(Y)=
\operatorname{Tr}\bigl(\omega^{H+1}(Y+\omega^2)^s\bigr),
\qquad
s=H-2p-j-1=2q-j-1,
\tag{17.2}
$$


modulo $Y^{d+1}$.

This is a finite column operation: only the original coefficients $0,\ldots,d$ are used. The higher-degree polynomial representation is a proof device, not an extension of the physical source range.

---

## 18. Exact rank when $L\equiv2\pmod3$

Now $H\equiv2\pmod3$, so


$$
P_s(Y)=\operatorname{Tr}(Y+\omega^2)^s.
$$


Put $x=Y+\omega^2$. Then $x+1=Y+\omega$, and


$$
x(x+1)=S.
$$


The polynomials


$$
F_s(S)=x^s+(x+1)^s
$$


satisfy


$$
F_0=0,\quad F_1=1,\quad F_{s+2}=F_{s+1}+SF_s.
$$


For $s\ge1$,


$$
F_s(S)=
\sum_j\binom{s-j-1}{j}S^j
\quad\text{in }\mathbb F_2[S].
\tag{18.1}
$$



Every row under consideration has $s\le2q-1$, hence degree in $S$ at most $q-1$.

The $q$ polynomials


$$
F_q,\ldots,F_{2q-1}
$$


form a basis of the polynomials of degree less than $q$. To check the unit determinant, take successive forward differences in $s$. The entry in difference row $i$, coefficient column $j$, is


$$
\binom{q-j-1}{j-i},
$$


which is zero for $j<i$ and $1$ for $j=i$.

The row sets in (16.1) contain this basis. In the even case this follows from $q\le d-2$; the extra combined row stays in the same polynomial space.

Finally, substitution $S=1+Y+Y^2$ is injective on degree-$<q$ polynomials after truncation at $Y^{d+1}$, since $q\le d-2$ and $Y+Y^2$ has order $1$.

Thus the contact rank is exactly $q$. Adding the atom pivot gives


$$
\operatorname{rank}\overline Z_p=q+1,
$$


and


$$
\boxed{\operatorname{corank}\overline Z_p=p+\varrho+1.}
\tag{18.2}
$$



The forward-difference basis above also certifies a unit block of this actual rank; no rank search is assumed.

---

## 19. Exact rank when $L\equiv1\pmod3$

Here


$$
P_s(Y)=\operatorname{Tr}\bigl(\omega^2(Y+\omega^2)^s\bigr).
$$


Define the triangular polynomial operator


$$
\mathcal U f(Y)=
\omega^2f(Y+\omega^2)+\omega f(Y+\omega).
$$


Its leading coefficient is unchanged, so it is invertible on every finite polynomial degree range.

Let


$$
h=2L,\qquad \tau=2(L-p),\qquad A=\tau-\varrho+1.
$$


Then $h\equiv2\pmod3$, and


$$
P_{h+t}=Y^hP_t+F_t(S),
\qquad 0\le t<\tau.
\tag{19.1}
$$



The ordinary low rows are:

- $P_A,\ldots,P_{h-1}$ for odd $p$;
- $P_{A+1},\ldots,P_{h-1},P_A+P_{A-1}$ for even $p$.

They have rank $h-A$.

A combination of the high rows is represented by


$$
f(Y)=\sum_{t<\tau}c_tY^t.
$$


Its low part is


$$
\mathcal U\bigl(f(Y+1)+f(Y)\bigr),
$$


because $\mathcal U$ commutes with translation.

Let


$$
\Delta_1f=f(Y+1)+f(Y).
$$


For the combination to vanish modulo the low row space:

- in the odd case, $\Delta_1f$ is divisible by $Y^A$;
- in the even case, it is divisible by $Y^{A-1}$, with one further coefficient condition.

But $\Delta_1f$ is invariant under $Y\mapsto Y+1$. Thus divisibility by $Y^a$ also gives divisibility by $(Y+1)^a$. Since


$$
\deg\Delta_1f\le\tau-2
$$


and $p+\varrho\le L-2$ gives $\tau\ge2\varrho+4$, either divisibility condition forces


$$
\Delta_1f=0.
$$



The invariant polynomials are exactly


$$
f(Y)=g(T),\qquad T=Y^2+Y.
$$


Indeed every polynomial is uniquely $g(T)+Yh(T)$, and its translation difference is $h(T)$.

For invariant $f$,


$$
\mathcal Uf=g(T+1).
$$


The high coefficients through $Y^{h+\varrho}$ vanish precisely when


$$
g(T+1)\equiv0\pmod{Y^{\varrho+1}},
$$


equivalently,


$$
(X+1)^{\varrho+1}\mid g(X).
$$


Since


$$
\deg g\le L-p-1,
$$


the kernel dimension in the high-row space is exactly


$$
L-p-\varrho-1.
$$



The total contact rank is therefore


$$
(d-1)-(L-p-\varrho-1)=L+p+2\varrho.
$$


Adding the atom pivot gives


$$
\boxed{\operatorname{corank}\overline Z_p=L-p-\varrho+1.}
\tag{19.2}
$$



### 19.1 An explicit unit-block certificate

This rank proof is constructive.

In the high-row polynomial space, use the complement


$$
YT^j,\quad 0\le j<L-p,
$$


together with


$$
T^j,\quad 0\le j\le\varrho.
$$


The remaining kernel basis is


$$
(T+1)^{\varrho+1}T^j,
\quad
0\le j\le L-p-\varrho-2.
$$



For $YT^j$, the low translation difference is $T^j$; the first $L-p$ low coefficient functionals form a unit-triangular block. For $T^j$, the high image is $(T+1)^j$; its first $\varrho+1$ coefficients form another unit block after the unit substitution $T=Y+Y^2$.

Together with the low rows and the atom pivot, these give a certified unit block of size


$$
n-\chi_p,\qquad
\chi_p=L-p-\varrho+1.
$$



Thus the exact rank is proved from the original source kernel, not postulated.

---

## 20. The bounded effective quotient and the first-lift return

Under (1.3), both cases have


$$
3\le\chi_p\le L-1.
$$


In particular, a unit $(n-2)$-minor does not exist.

Use the explicit finite binary bases above, with elementary integral lifts, to put the actual matrix into blocks


$$
\begin{pmatrix}A&B\\C&D\end{pmatrix},
\qquad
A\bmod2=I_{n-\chi_p}.
$$


The complete Schur block is


$$
S_p=D-CA^{-1}B\in2M_{\chi_p}(\mathbb Z_{(2)}),
$$


and


$$
\boxed{
\frac{\det Z_p}{2^{\chi_p}}
=
\pm\det A\,
\det\left(\frac{S_p}{2}\right).
}
\tag{20.1}
$$



This is a bounded effective quotient of the **actual corank**
$\chi_p\le L-1$, not an assumed two-by-two quotient. It is a symbolic finite reduction, not a request for an original-sized solve.

Moreover, choose the null-row basis to begin with the two independent relations (13.1). Their first lifts (13.2) lie in the leading row space. Therefore the first two rows of $S_p/2$ are even. Hence


$$
\boxed{v_2(\det Z_p)\ge\chi_p+2.}
\tag{20.2}
$$



The modulo-$4$ calculation has therefore evaluated the first-lift return in the actual quotient: it is zero on those two distinguished null directions.

Determining a later nonzero effective determinant requires higher source precision; it is not supplied by the rank calculation.

---

# Part VI. A new linear-depth consequence on the same original indices

## 21. Corank versus arbitrary source-jet excess

Let $\chi_p$ be the exact corank from (1.4). Compare a general normalized source pattern $U$ with $U_0$.

If $t$ source orders differ, then:

- the contact part changes in at most $t$ top rows;
- the atom column contributes at most one further rank change.

Thus


$$
\operatorname{corank}\overline Z_U\ge
\max(0,\chi_p-t-1).
$$


Since $\sigma(U)\ge t$, the source excess plus determinant payment is at least


$$
\sigma(U)+\max(0,\chi_p-t-1)\ge\chi_p-1.
$$



Consequently, for every $I,J$,


$$
\boxed{
\text{pure-Cauchy product-atom aggregate depth}
\ge
\mathcal L_p+w(I,J)+\chi_p-1.
}
\tag{21.1}
$$


This includes all source Newton patterns, not only the minimal pattern.

It gives a genuine complete-sector lower bound with a linear extra payment on the retained interval.

---

## 22. Validation in the original rotation interval

On


$$
\frac98\,2^{a_k}<k<\frac76\,2^{a_k},
\qquad L=2^{a_k-1},
$$


write $d=2L+\varrho$. Then


$$
L/4-1<\varrho<L/3-1,
$$


and $\varrho$ is divisible by $16$.

The nominal minimizer obeys


$$
|p_*-d/4|\le b_d+2.
$$


For every count admitted through a linear excess $B\le d/8$,


$$
|p-p_*|\le T_B=O(\sqrt d).
$$


Hence


$$
L-p-\varrho
\ge L/12-O(b_d+\sqrt d),
$$


so (1.3) holds with linear slack throughout the complete localized count range.

The parent first-$d/8$-window exclusion, already audited in Section 6, removes every factorial-forcing and bottom-atom pattern.

### 22.1 $L\equiv1\pmod3$

Take $B=\lfloor L/16\rfloor$. For every eligible count,


$$
\chi_p-1=L-p-\varrho>B
$$


at sufficiently large original indices. Equation (21.1) therefore puts every retained aggregate beyond $\mathfrak m_d+B$.

### 22.2 $L\equiv2\pmod3$

Take $B=\lfloor d/8\rfloor$. Now


$$
\chi_p-1=p+\varrho>B
$$


throughout the localized count range, again with linear slack.

This proves (1.6).

The interval contains infinitely many original indices by the same irrational-rotation argument already used in Turn 15. No new independent choices of $d,L,\varrho$ are introduced. Both parity classes of the dyadic exponent can also be obtained by applying the rotation modulo $2$, but the combined piecewise theorem does not require a separate distribution assumption.

---

# Part VII. Precision ledger, remaining bottleneck, and proof status

## 23. What was divided, and what precision was required

All new divisions above are on explicitly normalized auxiliary matrices over $\mathbb Z_{(2)}$. They do not redefine the original integer-column contents.

| Operation | Required information before division |
|---|---|
| $\theta_r^{(m)}=\Delta^ru_m/(2^rr!)$ | Full divisor $2^rr!$, including its odd part |
| Top source jet modulo $4$ | Full formula (11.1), including $o_d$, $\mathcal R_j$, and physical base $b+h$ |
| Bottom jet modulo $4$ | Complete numerator modulo four times $2^jj!$, with actual $Q_I$ |
| First two row divisions by $2$ | Complete rows (13.1) modulo $4$ |
| Second two row divisions by $2$ | Evaluated lift (13.2), including atom coordinates |
| Evaluation after total division by $16$ | Would require the normalized source and pole jets modulo $8$ |
| Corank-effective division by $2^{\chi_p}$ | Certified unit block of size $n-\chi_p$, not $n-2$ |
| Further two factors in (20.2) | Actual first-lift return zero, proved in (13.2) |

The top and bottom formulas use no physical moment beyond $3d+1$. In particular, the largest bottom normalized order remains $d+1$, and the largest contact order remains $r=d$.

---

## 24. Exact remaining mathematical bottleneck

The requested digit is now evaluated. The outstanding noncancellation problem has moved deeper.

Globally, outside a classified rank window, the next possible layer after (1.1) requires normalized source and physical-pole entries modulo $8$, together with every minimum product count and any other pattern actually admitted at that precision.

On the retained infinite interval, (1.6) shows that the obstruction is substantially larger: one must control a whole effective determinant of the actual corank, together with all weighted source/forcing competitors that become affordable at the chosen higher precision.

A concrete follow-on lemma is:

> **Complete effective noncancellation lemma.**  
> On an explicitly stated infinite original subfamily, produce a nonzero residue of the complete paired coefficient system within $O(d\log d)$ excess, using the actual corank block, all admissible source-jet and two-index partition patterns, every relative odd factor, and the full constant coefficient (3.3).

The proof must evaluate a complete aggregate. Neither count locality, a finite inventory, a unit contact minor, nor a lower divisor supplies its nonzero value.

The required joint binary upper remains


$$
\min(v_2(I_{0,k}),v_2(I_{1,k}))
\le
\frac{15}{4}k^2+d+5+O(k\log k).
\tag{24.1}
$$


Nothing here proves it.

The other-prime descents, exclusion of large primes, final all-prime $G_k$, and same-index whole-error analysis remain separate obligations. Even retirement of this producer would not decide the rationality of $e+\pi$.

---

## 25. Optional bounded arithmetic checks

No bounded arithmetic calculation is indispensable to the proofs above.

If the coordinator wants a genuinely new finite diagnostic of the rank formulas, the following auxiliary inputs are small and fully specified:



$$
(L,\varrho,d,p)=(64,16,144,36),
$$




$$
(L,\varrho,d,p)=(128,32,288,72).
$$



These are **auxiliary instances of the algebraic rank lemma**, not original indices $k=9^{18+32u}$, and are not offered as evidence for an infinite-family conclusion.

Construct only the normalized parity matrix from:

- $\theta_r\bmod2=\operatorname{Tr}(\omega^{r+2})$;
- the top atom ratios and $\mathbf K_d(j,r)$;
- the bottom rows $\mathbf K_p(z,r)$;
- columns $r=0,\ldots,d$.

The expected verifiable outputs are:

| Auxiliary input | Matrix size | Predicted corank | Predicted rank |
|---|---:|---:|---:|
| $(64,16,144,36)$ | $146$ | $13$ | $133$ |
| $(128,32,288,72)$ | $290$ | $105$ | $185$ |

An optional modulo-$4$ check on either input can additionally verify that the two rows obtained from (13.1), divided by $2$, equal the explicit bottom combinations (13.4), with zero atom coordinate modulo $2$.

These checks require no factorial forcing matrix, no $K_d^{-1}$, no prime scan, and no original-sized solve. They would establish only their stated finite scope.

---

## 26. PASS / NEW / CONDITIONAL / OPEN ledger

| Statement | Status |
|---|---|
| Previously passed rank-one perturbation and mixed-$\eta$ window | **Reused; not repeated** |
| Both paired coefficient identities and complete constant border | **Retained at passed scope** |
| Parent terminal second difference and all nominal ties | **PASS** |
| Parent all-$p$, all-$v$ comparison, including empty Cauchy and $p=0$ | **PASS** |
| Parent negative-$M_p$ quadratic gap and $O(d\log d)$ locality | **PASS at stated asymptotic scope** |
| Parent first-$d/8$-window exclusion | **PASS at stated sufficiently-large-original-index scope** |
| Two-index weighted partition bijection and first-two inventories | **PASS** |
| Classical partition counting bound | **Reuse/application** |
| A4 Section 15 every-$I,J$ two-factor payment | **Different audit: PASS** |
| A4 reduction (17.4), including disappearance of all nonminimal pairs modulo $2^{\mathcal L_p+3}$ | **Different audit: PASS** |
| Actual source and physical-pole jets modulo $4$ | **NEW PROVED** |
| Both first lifts return to the actual bottom span | **NEW PROVED** |
| Universal four-factor pure-Cauchy aggregate payment | **NEW PROVED** |
| Whole $2^{\mathfrak m_d+4}\mid D_k$ | **NEW PROVED** |
| Exact parity corank (1.4) under (1.3) | **NEW PROVED** |
| Actual-rank unit block and corank-effective quotient | **NEW PROVED** |
| Linear-depth consequence (1.6) on the same original interval | **NEW PROVED, stated scope only** |
| Exact parity-rank classification outside the displayed rank window | **OPEN; not needed for (1.1)** |
| Nonzero later aggregate and controlled upper excess | **OPEN** |
| Joint coefficient upper, other primes, all-prime gcd upper | **OPEN** |
| Rationality or irrationality of $e+\pi$ | **OPEN** |

---

## Final conclusion

The stronger A4 reduction survives the assigned different audit. Its universal finite Newton argument really does remove every nonminimal $N_d$-pair at the modulo-$8$ precision in question. The near-boundary inverse returns are not omitted; their complete aggregates are paid beyond that layer.

The new modulo-$4$ calculation goes further. It retains the actual top base, every source factor, the physical pole sum, the physical $\theta$-base correction, and the atom coordinates before division. Both first lifted relations return to the actual bottom row span. This proves


$$
\boxed{
2^{\mathfrak m_d+4}\mid
\det[w_*,v^{(0)},\ldots,v^{(d)}]
}
$$


on every original index, so the assigned next aggregate digit is zero.

On the retained infinite original rotation interval, the full $\theta$ matrix has an explicitly determined, generally linear corank—not corank two. The resulting source-specific rank calculation yields the further linear-depth lower bounds (1.6).

The unresolved issue is now a complete higher-depth **noncancellation upper theorem**, not another nominal inventory. Both exact coefficient borders, all paid transfer factors, the actual contents and least clearer, the all-prime gcd, the primitive denominator, and the positive whole evaluated error remain unchanged.

No unconditional proof of rationality or irrationality of $e+\pi$ has been obtained.
