> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 Turn 26 — Independent audit of the actual theta lifts and complete terminal aggregation

## Executive summary

The original dyadic indices are retained throughout:


$$
\boxed{k=9^{18+32u},\qquad u\ge0,\qquad d=k-1.}
$$


In particular, $v_2(d)=4$. The last physical row is $2d+1$, and the largest moment remains $3d+1$, with terminal factorial and odd denominator


$$
(6k-4)!,\qquad 6k-5.
$$



The principal audit conclusions are:

1. **The parent modulo-$4$ theta, top-source, atom, and bottom-source laws pass.**  
   This includes arbitrary admitted top bases, every actual pole set, the shifted product-rule base $d+\ell$, all rising-factor ratios, and both physical finite boundaries.

2. **The two first divided relations really are complete-row relations.**  
   Their contact coordinates lie in the existing bottom span, and their atom coordinates remain even. Thus the asserted factor $16$ is valid.

3. **The indispensable complete finite source-jet aggregation from FULL24 passes under the independent derivation below.**  
   It is an exact aggregation over all product-contact choices, both source sets, and all finite Newton patterns. No selected minimal source minor replaces the complete determinant.

4. **FULL A2turn15’s global factorial-competitor exclusion passes.**  
   The proof works for every $1\le v\le p\le d$, including the all-factorial case $p=v$. The $p=0$ and small-$p$ margins are retained. In fact, its inequalities have more than the four digits of slack needed by the parent candidate.

5. **The whole four-zero conclusion passes:**
   

$$
\boxed{2^{m_\star+4}\mid D_k,\qquad
   D_k=\det[w_*,v^{(0)},\ldots,v^{(d)}],\quad
   m_\star=\min_{1\le p\le d}\mathcal L_p(d).}
$$



6. **The complete modulo-$8$ source laws also pass.**  
   Every elementary-symmetric and Stirling carry in the supplied formula is accounted for. The unchanged top and atom laws are correct. The closed modulo-$4$ receipt is not used as modulo-$8$ evidence.

There is a further proved result.

> **New second-lift theorem.** On every original index,
> 

$$
> \boxed{2^{m_\star+6}\mid D_k.}
> \tag{E.1}
>
$$


> Consequently,
> 

$$
> \boxed{v_2(I_{1,k})\ge \alpha_d+v_2(d!)+m_\star+6.}
> \tag{E.2}
>
$$



The proof evaluates the second effective rows, rather than merely naming their residuals. At an arbitrary top Newton base $a$, one second-lift row has a possible boundary-overflow term $aK_d(2)$. Thus an unqualified repetition of the first bottom-span argument would be invalid. The concrete repair is an **exact finite Newton expansion at base $0$** of the original source rows. This changes no original column or index and removes that term. Both effective rows then lie in the admitted bottom span, supplying two further binary factors.

These are lower-divisibility results, not noncancellation upper bounds. The complete constant border $-f+4\rho$, the all-prime gcd, the actual least simultaneous clearer, and the positive primitive whole error remain unchanged.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$



---

# 1. Retained original objects and exact interfaces

## 1.1 Domain, sequences, and finite boundaries

Write


$$
b_d=1+\lfloor\log_2d\rfloor
$$


for the bit length. This is distinct from the nominal minimum $m_\star$.

For $t=18+32u$, $v_2(t)=1$, and


$$
v_2(9^t-1)=v_2(9-1)+v_2(t)=4.
$$


The stronger retained congruences are


$$
d\equiv208\pmod{256},\qquad d\equiv2\pmod3.
$$



The original sequences are


$$
a_0=1,\qquad a_n=1-na_{n-1},
$$




$$
u_n=a_{2n},\quad f_n=(2n)!,\quad w_n=(-1)^n,\quad c_n=u_n-w_n,
$$


and


$$
\rho_0=0,\qquad \rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad r_n=-f_n+4\rho_n.
$$


Their complete returns are


$$
\sigma_n=u_{n+1}+u_n,
$$




$$
\boxed{\tau_n=-(2n+2)!-(2n)!+\frac4{2n+1}.}
\tag{1.1}
$$



Set


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),\qquad T_n=\Lambda_k\tau_n.
$$


No factorial term or rational term in (1.1) is removed.

The finite ranges remain:

- top source rows $0\le a<d$;
- residual rows $0\le i\le d+1$, representing physical row $d+i$;
- theta orders $0\le r\le d$;
- last physical row $2d+1$;
- largest moment $3d+1$.

The original parameter is already much larger than all elementary size thresholds below: $d>2^{57}$.

## 1.2 Complete forcing and corrected columns

To distinguish it from the integer filters introduced later, write $\mathbf K_d$ for the forcing matrix called $K_d$ in the sources.

Retain


$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1),\qquad
\mathcal A_dy=\Delta^d(P_dy),
$$


with its actual determinant payment


$$
\Omega_k=\prod_{a=0}^{d-1}P_d(a).
$$



The complete top forcing is


$$
F_k=-\Lambda_kD_f\mathbf K_dD_f,\qquad
D_f=\operatorname{diag}((2a)!)_{a<d}.
$$


The established oddness of the leading principal determinants of $\mathbf K_d$ is reused at its stated original-index scope.

Put


$$
h_d=(2d-2)!,\qquad
\beta=v_2(h_d),\qquad
\alpha=v_2((2d)!)=\beta+5,
$$




$$
N_d=(h_dD_f^{-1})\operatorname{adj}(\mathbf K_d)(h_dD_f^{-1}),
$$




$$
\delta_k=\Lambda_k\det(\mathbf K_d)h_d^2,\qquad
F_k^{-1}=-N_d/\delta_k.
$$


The bottom forcing is exactly


$$
R(i,j)=
\frac{\Lambda_k}{2(d+i+j)+1}
-\frac{\Lambda_k}{4}\bigl(4(d+i+j)^2+6(d+i+j)+3\bigr)(2(d+i+j))!,
\tag{1.2}
$$


for $0\le i\le d+1,\ 0\le j<d$.

Thus


$$
R=R^{\rm C}-2^{\alpha-2}V,
$$


where


$$
R^{\rm C}(i,j)=\frac{\Lambda_k}{2(d+i+j)+1},
$$




$$
V(i,j)=
\frac{\Lambda_k(4(d+i+j)^2+6(d+i+j)+3)(2(d+i+j))!}{2^\alpha}.
\tag{1.3}
$$


Both matrices are integral on these actual ranges. The identity


$$
(4t^2+6t+3)(2t)!=(2t+2)!+(2t)!
$$


shows explicitly that $V$ retains both factorial returns.

Define the complete finite map


$$
\mathscr T(y)=RN_d(\mathcal A_dy)_{\rm top}+\frac{\delta_k}{4}y_{\rm bot}.
\tag{1.4}
$$


Every return divisor remains the full integer


$$
D_r=2^rr!.
$$



Let


$$
A=v_2(d!)=\alpha-d,\qquad L=\alpha-12,
$$




$$
\gamma=\frac{\delta_k}{2^{2\beta}}
=\Lambda_k\det(\mathbf K_d)\operatorname{odd}(h_d)^2.
$$


Thus $\gamma$ is an actual odd integer, not the integer $1$.

The complete theta columns and atom are


$$
v^{(r)}=\frac{\mathscr T(\Delta^ru)}{2^\alpha D_r},
\qquad 0\le r\le d,
\qquad
w_*=\frac{\mathscr T(w)}{2^d}.
$$


They satisfy the exact decomposition


$$
\boxed{
[w_*,v^{(0)},\ldots,v^{(d)}]
=
RN_d[\mathsf a_w,\mathsf v^{(0)},\ldots,\mathsf v^{(d)}]
+2^L\gamma[2^Aw,\theta_0,\ldots,\theta_d]_{\rm bot},
}
\tag{1.5}
$$


where


$$
\mathsf a_w=\frac{\mathcal A_dw}{2^d},\qquad
\mathsf v^{(r)}=\frac{\mathcal A_d\Delta^ru}{2^\alpha D_r}.
$$



All these complete columns retain the physical terminal $3d+1$.

## 1.3 Both literal paired borders

The passed determinant-one paired transformation is reused, not recalculated.

With


$$
a_r=(-1)^{d-r}\frac{d!}{r!},\qquad
\varkappa_d=2^{\alpha-d}d!,\qquad
\mathfrak c_k=\Lambda_k2^\alpha d!,
$$


the exact paired pencil is


$$
\widehat{\mathcal Q}_k(s)=
\left[
\varkappa_dv^{(d)}-w_*,
\ (v^{(r)}-a_rv^{(d)})_{r<d},
\ \mathfrak b_0+s\mathfrak c_kv^{(d)}
\right],
\tag{1.6}
$$


where


$$
\boxed{
\mathfrak b_0=\Lambda_k\mathscr T(r)
=\Lambda_k2^{-d}\mathscr T(\Delta^dr).
}
\tag{1.7}
$$


The right side still contains both $-\Delta^df$ and $4\Delta^d\rho$.

Writing $\det\mathcal Q_k(s)=I_{0,k}+I_{1,k}s$, the two coefficient identities remain


$$
\boxed{I_{1,k}=-\mathfrak c_kD_k,\qquad
D_k=\det[w_*,v^{(0)},\ldots,v^{(d)}],}
\tag{1.8}
$$


and


$$
\boxed{
\begin{aligned}
I_{0,k}
={}&\varkappa_d\det[v^{(0)},\ldots,v^{(d)},\mathfrak b_0]\\
&-\sum_{r=0}^d\frac{d!}{r!}
\det[w_*,v^{(0)},\ldots,\widehat{v^{(r)}},
\ldots,v^{(d)},\mathfrak b_0].
\end{aligned}}
\tag{1.9}
$$



No theta-only calculation below evaluates (1.9).

---

# 2. Exact theta normalization and the paid divisions

## 2.1 Integral contact numbers

Let $\mathcal L(t^j)=j!$. Then


$$
\mathcal L(F')=\mathcal L(F)-F(0).
$$


With $X=t(t-2)$,


$$
u_m=\mathcal L((t-1)^{2m}),\qquad
\Delta^ru_0=\mathcal L(X^r).
$$



Put $I_r=\mathcal L(X^r)$ and $J_r=\mathcal L((t-1)X^r)$. For $r\ge1$,


$$
I_{r+1}=2(r+1)J_r,
$$




$$
J_r=(2r+1)I_r+2rI_{r-1}.
$$


Consequently


$$
\theta_r=\frac{I_r}{2^rr!}
$$


satisfies


$$
\boxed{
\theta_0=1,\quad \theta_1=0,\quad
\theta_{r+1}=(2r+1)\theta_r+\theta_{r-1}.
}
\tag{2.1}
$$


In particular, all $\theta_r$ are integers.

For every nonnegative physical base $m$,


$$
\boxed{
\theta_r^{(m)}
=\frac{\Delta^ru_m}{2^rr!}
=\sum_{\ell=0}^{m}
\binom m\ell 2^\ell(r+1)_\ell\theta_{r+\ell}.
}
\tag{2.2}
$$


This is a finite integer identity. It also gives


$$
\Delta^j\theta_r^{(m)}
=2^j(r+1)_j\theta_{r+j}^{(m)}.
\tag{2.3}
$$



Thus


$$
\theta_r^{(m)}
\equiv\theta_r+2m(r+1)\theta_{r+1}\pmod4.
\tag{2.4}
$$



## 2.2 Full top divisor

Let


$$
R_j=(d+1)_j,\qquad o_d=\frac{d!}{2^{v_2(d!)}},
$$


and


$$
Q_h(a)=\prod_{t=h}^{d-1}(2a+2t+1).
$$


The finite difference identity


$$
\Delta^hP_d(a)=2^h\frac{d!}{(d-h)!}Q_h(a)
$$


and the shifted product rule give


$$
\boxed{
T_j^{(a)}(r):=
\frac{\Delta^j\mathsf v_a^{(r)}}{2^jR_j}
=
o_d\sum_{h=0}^d
\binom dh Q_h(a)
\binom{d-h+r+j}{r}
\theta_{d-h+r+j}^{(a+h)}.
}
\tag{2.5}
$$


This proves integer divisibility by the full return factor $2^rr!$ and the full rising factor $2^jR_j$, including their odd parts.

The admitted range is


$$
a+j\le d-1,\qquad 0\le r\le d.
\tag{2.6}
$$


The raw largest $u$-index in (2.5) is


$$
a+d+j+r\le3d-1.
$$


Thus this top normalization stays within the original finite data.

## 2.3 Actual atom jets

The actual $w$-atom obeys


$$
\boxed{
A_j^{(a)}:=
\frac{\Delta^j\mathsf a_w(a)}{2^j}
=
(-1)^{a+j}
\sum_{h=0}^d
\binom{d+j}{h}\frac{d!}{(d-h)!}Q_h(a).
}
\tag{2.7}
$$


Every displayed term is integral.

When a source-jet determinant has maximum order $m$, its normalized atom entry in row $j$ is


$$
\frac{R_m}{R_j}A_j^{(a)},
\tag{2.8}
$$


not merely $A_j^{(a)}$. The ratio is the literal integer rising product.

## 2.4 Full bottom divisor and physical base

For an actual pole set $I\subseteq\{0,\ldots,d-1\}$, $|I|=p$, define


$$
Q_I(i)=\prod_{t\in I}(2(d+i+t)+1),
$$




$$
J_\ell=\frac{\Delta^\ell Q_I(0)}{2^\ell\ell!}.
$$


Writing $Q_I$ as a polynomial in $2i$, the Stirling expansion proves $J_\ell\in\mathbb Z$.

For $j\ge p$, the exact shifted product rule is


$$
\boxed{
\frac{\Delta_i^j(Q_I(i)\theta_r^{(d+i)})|_{i=0}}
{2^jj!}
=
\sum_{\ell=0}^p
J_\ell\binom{r+j-\ell}{r}
\theta_{r+j-\ell}^{(d+\ell)}.
}
\tag{2.9}
$$


The physical base is $d+\ell$, not $d$, $0$, or an independently chosen parameter.

Every division in (2.9) is an integer division. The bottom range is


$$
p\le j\le d+1,
$$


and the largest raw moment is


$$
d+j+r\le3d+1.
\tag{2.10}
$$



**Verdict:** the complete return, top, and theta-bottom divisions pass. Odd-unit normalization of an entire auxiliary top row is performed in $\mathbb Z_{(2)}$; it is not an additional integer-content division in the original pencil.

---

# 3. Audit of the complete modulo-$4$ laws

Define the integer contact rows and filters


$$
B_j(r)=\binom{r+j}{r}\theta_{r+j},
$$




$$
K_b(z,r)=\sum_{t=0}^b\binom bt B_{z+t}(r).
\tag{3.1}
$$


These are integer filters, distinct from $\mathbf K_d$. Exactly,


$$
K_{b+1}(z)=K_b(z)+K_b(z+1).
\tag{3.2}
$$



## 3.1 Top source: PASS

For $1\le h\le d$,


$$
h\binom dh=d\binom{d-1}{h-1}
$$


gives


$$
v_2\binom dh\ge4-v_2(h).
$$


Hence a term visible modulo $4$ has $8\mid h$, apart from the separately included $h=0$.

Because $16\mid d$,


$$
Q_h(a)\equiv(-1)^{ha+\binom h2}\equiv1\pmod4
$$


for these $h$. Also $a+h\equiv a\pmod2$, and $d-h$ is even.

Substitute (2.4) into (2.5), and use


$$
(r+j+t+1)\binom{r+j+t}{r}
=(j+t+1)\binom{r+j+t+1}{r}.
$$


With $t=d-h$, the $2at$ term vanishes modulo $4$. Therefore


$$
\boxed{
T_j^{(a)}(r)
\equiv o_d\{K_d(j,r)+2a(j+1)K_d(j+1,r)\}\pmod4.
}
\tag{3.3}
$$


This holds for every admitted physical top base $a$, not just $a=0$ or $a=d-p$.

## 3.2 Atom: PASS

In (2.7), every $h\ge1$ term contains the integer $d$, hence is divisible by $16$. The $h=0$ product is $1\bmod4$. Thus


$$
\boxed{A_j^{(a)}\equiv(-1)^{a+j}\pmod4.}
\tag{3.4}
$$


The rising ratio in (2.8) is still required.

## 3.3 Bottom coefficients: PASS

Put


$$
S_I=\sum_{t\in I}(d+t)\pmod2.
$$


Let $e_q$ be the elementary symmetric polynomial of degree $q$ in the odd constants $1+2(d+t)$.

Since


$$
J_\ell=\sum_{q=\ell}^p2^{q-\ell}e_{p-q}S(q,\ell),
$$


only $q=\ell,\ell+1$ survive modulo $4$. Consequently


$$
J_\ell
\equiv e_{p-\ell}
+2\binom{\ell+1}{2}e_{p-\ell-1}\pmod4,
$$


and


$$
\boxed{
J_\ell\equiv
\binom p\ell
+2S_I\binom{p-1}{\ell}
+2\binom{\ell+1}{2}\binom p{\ell+1}
\pmod4.
}
\tag{3.5}
$$



Now write $j=p+z$, and denote the normalized bottom row in (2.9) by $V_z^I$. The physical-base correction in (2.4), applied at $d+\ell$, is


$$
2(d+\ell)(j-\ell+1)B_{j-\ell+1}.
$$


Since $2d\equiv0\pmod4$, this reduces to the term with $2\ell$, but the shift $\ell$ cannot be omitted.

Using


$$
\ell\binom p\ell=p\binom{p-1}{\ell-1},
$$


and


$$
\binom{\ell+1}{2}\binom p{\ell+1}
=\binom p2\binom{p-2}{\ell-1},
$$


one obtains


$$
\boxed{
V_z^I\equiv
K_p(z)+2(S_I+pj)K_{p-1}(z+1)
+2\binom p2K_{p-2}(z+1)\pmod4.
}
\tag{3.6}
$$



For


$$
T_p=\{d-p,\ldots,d-1\},
$$




$$
S_{T_p}\equiv\binom{p+1}{2}\pmod2.
$$


Writing


$$
\beta_I=S_I+p+\binom p2\pmod2,
$$


the equivalent form is


$$
\boxed{
V_z^I\equiv
K_p(z)+2(pz+\beta_I)K_{p-1}(z+1)
+2\binom p2K_{p-2}(z+2)\pmod4.
}
\tag{3.7}
$$


For $I=T_p$, $\beta_I=0$.

This proves the parent bottom laws for every actual $I$.

---

# 4. Both first divided relations and the factor $16$

Let


$$
D=d-p\ge2.
$$


The actual bottom rows are $V_0^I,\ldots,V_{D+1}^I$.

Normalize each auxiliary top row by the actual odd unit $o_d$, retaining $o_d^p$ in the determinant prefactor. For $j=0,1$, subtract


$$
\sum_{t=0}^D\binom DtV_{j+t}^I
$$


from the normalized top row.

The exact integer filter identity


$$
K_d(j)=(1+E)^DK_p(j)
\tag{4.1}
$$


shows that both resulting rows are even. From (3.3) and (3.7), their contact coordinates after division by $2$ are


$$
\boxed{
L_j=
a(j+1)K_d(j+1)
-(pj+\beta_I)K_{d-1}(j+1)
-\left(pD+\binom p2\right)K_{d-2}(j+2)
\pmod2.
}
\tag{4.2}
$$



The $z$-weighted convolution is paid by


$$
\sum_t t\binom DtE^t=DE(1+E)^{D-1}.
$$



Every surviving term in (4.2) lies in the existing bottom span:

- at $j=0$, $K_d(1)$ uses bottom orders $1,\ldots,D+1$;
- at $j=1$, the coefficient $2a$ is zero modulo $2$, so no order $D+2$ is used;
- $K_{d-1}(j+1)$ uses orders through $D+1$;
- $K_{d-2}(j+2)$ also uses orders through $D+1$.

The atom must be checked separately. For a source-jet pattern containing $0,1$, with maximum $m\ge4$, its first two normalized atom entries are


$$
\frac{R_m}{R_j}\frac{A_j^{(a)}}{o_d},\qquad j=0,1.
$$


Here $R_0,R_1$ are odd, while


$$
v_2(R_4)=v_2((d+1)(d+2)(d+3)(d+4))=3.
$$


Thus both atom entries remain even after the first division by $2$. Bottom atom entries are zero in an atom-product aggregate.

Subtract the certified bottom combinations representing (4.2). Both divided rows become even again. Each original row is therefore divisible by $4$, so the complete normalized determinant has a factor $16$.

This proof neither requires nor proves corank exactly two.

**Verdict: PASS.**

---

# 5. Independent proof of the complete finite source-jet aggregation

This is the indispensable part of FULL24 whose separate A2turn16 review is pending. The following supplies an independent proof at the scope used here.

## 5.1 Exact fixed-$I,J$ aggregation

Let $n=d+2$. Consider a pure-Cauchy term with $p$ product columns, with the atom among them. Fix forcing and source sets


$$
I,J\subseteq\{0,\ldots,d-1\},\qquad |I|=|J|=p.
$$



The exact mixed Cauchy identity has scalar


$$
C_p(I)=
\frac{\Lambda_k^p2^{p(p-1)}\Phi_pV(I)}
{\prod_{i=0}^{n-1}Q_I(i)},
\qquad
\Phi_p=\prod_{j=0}^{p-1}j!.
\tag{5.1}
$$


All denominators are actual odd physical denominators.

After clearing $Q_I$, the Cauchy columns become polynomial columns of degrees $0,\ldots,p-1$. The finite Newton transformation on rows $0,\ldots,n-1$ sends their binomial basis to the first $p$ coordinate columns. The remaining bottom rows are exactly


$$
\Delta^j(Q_IW)(0),\qquad p\le j\le n-1.
$$



Summing over **all** choices of the $p-1$ contact columns accompanying the atom is precisely the Laplace expansion of the stacked matrix


$$
\left[
\begin{array}{c}
[\mathsf a_w,\mathsf v^{(0)},\ldots,\mathsf v^{(d)}][J,:]\\[2mm]
[0,\Delta^j(Q_I\theta_0),\ldots,\Delta^j(Q_I\theta_d)]_{j=p}^{n-1}
\end{array}
\right].
\tag{5.2}
$$


Thus (5.2), multiplied by


$$
(2^L\gamma)^{n-p}C_p(I)\det N_d[I,J],
$$


is the complete fixed-$I,J$ atom-product contribution. It is not one selected product-column summand.

## 5.2 Exact finite Newton expansion of arbitrary source rows

For every original source row $x\in J$,


$$
\mathsf S_x=\sum_{j=0}^{x}\binom xj\Delta^j\mathsf S_0,
\qquad
\mathsf S=[\mathsf a_w,\mathsf v^{(0)},\ldots,\mathsf v^{(d)}].
$$


Therefore the top exterior product in (5.2) is the finite sum over


$$
U=\{j_0<\cdots<j_{p-1}\}\subseteq\{0,\ldots,d-1\}
$$


with integer coefficient


$$
\det\!\left[\binom{x}{j}\right]_{x\in J,\ j\in U}.
\tag{5.3}
$$



No infinite interpolation or source row beyond $d-1$ is introduced.

Let $m=j_{p-1}$. Multiply the atom column by $R_m$, and divide top row $j_a$ by $2^{j_a}R_{j_a}$. The exact extracted factor is


$$
\boxed{
\mathfrak F(U)
=2^{\sum_a j_a}\prod_{a=0}^{p-2}R_{j_a}.
}
\tag{5.4}
$$


The remaining atom entry is the literal ratio (2.8). All contact entries are the integral $T_{j_a}^{(0)}(r)$.

Define


$$
\mathfrak F_p=2^{\binom p2}\prod_{a=0}^{p-2}R_a,\qquad
B_p(d)=v_2(\mathfrak F_p).
$$


Since $j_a\ge a$,


$$
\frac{\mathfrak F(U)}{\mathfrak F_p}
=
2^{\sum_a(j_a-a)}
\prod_{a=0}^{p-2}\frac{R_{j_a}}{R_a}
\in\mathbb Z.
\tag{5.5}
$$


In particular,


$$
v_2\!\left(\frac{\mathfrak F(U)}{\mathfrak F_p}\right)
\ge \epsilon(U):=\sum_a(j_a-a).
\tag{5.6}
$$



The complete fixed-$I,J$ expression is consequently


$$
\boxed{
\begin{aligned}
&(2^L\gamma)^{n-p}C_p(I)\det N_d[I,J]
\prod_{j=p}^{n-1}(2^jj!)\\
&\qquad\times
\sum_U
\det\!\left[\binom{x}{j}\right]_{x\in J,j\in U}
\,\mathfrak F(U)\,o_d^p\,
\det\widetilde Z_{I,U}^{(0)}.
\end{aligned}}
\tag{5.7}
$$


Here the top rows of $\widetilde Z_{I,U}^{(0)}$ are


$$
\left[
\frac{R_m}{R_j}\frac{A_j^{(0)}}{o_d},
\quad
\left(\frac{T_j^{(0)}(r)}{o_d}\right)_{r=0}^d
\right],
$$


and its bottom rows are


$$
[0,V_z^I],\qquad 0\le z\le D+1.
$$



Equation (5.7) retains every actual odd factor, both source sets, and every finite Newton coefficient.

## 5.3 Exhaustion of the low-excess patterns

The shifts $j_a-a$ are nonnegative and nondecreasing. For $\epsilon\le3$, their nonzero tails are exactly


$$
\varnothing;\quad
(1);\quad
(2),(1,1);\quad
(3),(1,2),(1,1,1).
\tag{5.8}
$$


For $p\ge5$, every one contains jet orders $0,1$, and its maximum is at least $p-1\ge4$. Section 4 therefore supplies a factor $16$ for every such normalized determinant, for every $I,J$.

All other patterns already pay at least four factors through (5.6). Thus


$$
\boxed{
\text{pure-Cauchy atom-product \(p\)-sector}
\in2^{\mathcal L_p(d)+4}\mathbb Z_2,
\qquad p\ge5,\ d-p\ge2.
}
\tag{5.9}
$$



This independently pays the aggregation needed by the parent four-zero candidate. It does not purport to settle every other statement assigned to the pending A2turn16 audit.

---

# 6. Global factorial, bottom-atom, and product-count audit

## 6.1 Nominal payments and the actual $N_d$-sets

Define


$$
\lambda_j=j+v_2(j!),\qquad S_q=\sum_{j=0}^{q-1}\lambda_j,
$$




$$
e_j=v_2\!\left(\frac{h_d}{(2j)!}\right),\qquad
E_p=\sum_{j=d-p}^{d-1}e_j.
$$


Then


$$
\boxed{
\mathcal L_p
=(n-p)L+S_p+S_n+2E_p+B_p(d).
}
\tag{6.1}
$$


Set $\mathcal L_0=nL+S_n$.

Since


$$
e_j-e_{j+1}=1+v_2(j+1)>0,
$$


the unique set minimizing a $p$-element diagonal weight is $T_p$. Jacobi’s identity gives


$$
\det N_d[T_p,T_p]
=
\left(\prod_{j\in T_p}\frac{h_d}{(2j)!}\right)^2
(\det\mathbf K_d)^{p-1}
\det\mathbf K_d[0{:}d-p-1,0{:}d-p-1].
\tag{6.2}
$$


The last two factors are odd. Thus its valuation is exactly $2E_p$.

For other $I,J$, the actual adjugate minor is retained; only its integrality is used. It is not presumed odd.

The weight-one locality stated in A2turn15 also passes. If $b=d-p>0$, the only possible weight-one change is


$$
T'_p=\{b-1,b+1,\ldots,d-1\},
$$


and it occurs only when $p$ is odd, because


$$
e_{b-1}-e_b=1+v_2(b).
$$


Moreover,


$$
V(T'_p)/\Phi_p=p.
$$


Our uniform fixed-$I,J$ proof is stronger than needed for those near-minimal pairs; it does not require their inverse returns.

## 6.2 Every factorial pattern, including $p=v$

Suppose there are $p$ product columns, $v\ge1$ factorial-forcing columns, and


$$
a=p-v
$$


Cauchy columns.

For an actual forcing column $j$, put


$$
g_j=v_2((2(d+j))!)-\alpha.
$$


Its factorial-column payment combines with its $N_d$-diagonal factor as


$$
e_j+g_j
=2d+s_2(j)-s_2(d+j)-5
\ge 2d-b_d-6.
\tag{6.3}
$$


Write $C_{\rm fac}=2d-b_d-6$.

Expand the $v$ factorial columns on their actual residual rows. The remaining $a+n-p=n-v$ rows need not be consecutive. Finite Newton expansion on those rows still forces polynomial orders $0,\ldots,a-1$, and every surviving bottom order is at least $a$. Therefore the complete multiple-return payment is


$$
S_a+S_{n-v}.
$$



This argument also includes a bottom atom. Its explicit factor $2^A$ pays the missing binary factorial valuation through the entire physical range because


$$
v_2(j!)\le v_2((d+1)!)=A,\qquad j\le d+1.
\tag{6.4}
$$


Odd factorial denominators remain units in $\mathbb Z_{(2)}$; no new integer-pencil division by them is asserted.

The full lower payment is


$$
\boxed{
\mathcal F(p,v)
=(n-p)L+v(\alpha-2+C_{\rm fac})
+E_p+E_a+B_p+S_a+S_{n-v}.
}
\tag{6.5}
$$


This includes $a=0$, hence the all-factorial case $p=v$.

Because $\alpha-2-L=10$,


$$
\mathcal F(p,v)-\mathcal L_a
=
v(10+C_{\rm fac})+(E_p-E_a)+(B_p-B_a)-(S_n-S_{n-v}).
\tag{6.6}
$$


The elementary bounds


$$
E_p-E_a\ge v(2a+v-1-b_d),
$$




$$
B_p-B_a\ge v(2a+v-b_d-2),
$$




$$
S_n-S_{n-v}\le v(2d+3-v)
$$


give exactly


$$
\boxed{
\mathcal F(p,v)\ge
\mathcal L_a+v(4a+3v-3b_d-2).
}
\tag{6.7}
$$



For $p\ge b_d+2$, the last expression is


$$
v(4p-v-3b_d-2).
$$


As a concave quadratic in $v$, its minimum on $1\le v\le p$ occurs at an endpoint. The two endpoint bounds are


$$
4p-3b_d-3\ge b_d+5,
$$


and


$$
p(3p-3b_d-2)\ge4p.
$$


Thus these patterns lie above $m_\star+b_d+5$.

For $p\le b_d+1$, the exact marginal formula gives


$$
D_{b_d+2}\le11b_d+7,
$$


where $D_t=T_t-T_{t-1}$ and $T_t=S_t+2E_t+B_t$. Consequently, for $a\le b_d+1$, including $a=0$,


$$
\mathcal L_a-m_\star\ge2d-12b_d-19.
$$


Allowing the full possible negative part of (6.7) gives


$$
\boxed{
\mathcal F(p,v)-m_\star
\ge2d-3b_d^2-17b_d-21.
}
\tag{6.8}
$$


This is greater than $7$ on the original domain. For completeness, $d\ge2^{b_d-1}$, and the inequality follows already for $b_d\ge9$ by induction from


$$
2^9-3\cdot9^2-17\cdot9-21=95.
$$



Thus every factorial pattern is beyond $m_\star+7$, which is stronger than the parent’s required $m_\star+4$.

**Verdict: PASS, including all $p,v$, all forcing factors, and both large- and small-$p$ regimes.**

For a fixed $p\le d/3$, (6.5) also gives the useful local bound


$$
\mathcal F(p,v)-\mathcal L_p
\ge v(\alpha-4p-2b_d-11),
\tag{6.9}
$$


which is greater than $7v$ on the original domain. This validates, with slack, the weaker local margin quoted in FULL24.

## 6.3 Bottom atom and $p=0$

When the atom is a bottom correction, all $p$ top sources are contact sources. Their source payment exceeds $B_p$ by


$$
b_p^\uparrow=v_2(R_{p-1}).
$$


The physical bottom-atom payment is exactly (6.4).

Since $v_2(d)=4$,


$$
v_2(R_4)=3,\qquad v_2(R_6)=4,\qquad v_2(R_8)=7.
\tag{6.10}
$$


Therefore:

- $p\ge7$ gives at least four extra factors;
- $p\ge9$ gives at least seven extra factors.

For $p=0$, the all-bottom payment is $\mathcal L_0$, and


$$
\mathcal L_0-\mathcal L_1=L>0.
$$


The same large small-$p$ gap used above separates $p=0,1,\ldots,8$ from the relevant minimum.

Thus no atom-bottom term was discarded by treating it as a contact column without payment.

## 6.4 Localization and all ties

Direct subtraction of (6.1) gives


$$
\boxed{
\mathcal L_{p+1}-\mathcal L_p
=
8p-2d+5-s_2(p)+2s_2(d-p-1)-s_2(d+p-1).
}
\tag{6.11}
$$


The marginal increments satisfy


$$
D_{p+1}-D_p
=
1+v_2(p)+2(1+v_2(d-p))+1+v_2(d+p-1)\ge4.
\tag{6.12}
$$


Hence the nominal minimum is unique or is an adjacent tie.

The digit terms in (6.11) show that every count within any of the first seven digits of the minimum lies in


$$
\left|p-\frac d4\right|\le b_d+3.
\tag{6.13}
$$


On the original domain this lies inside


$$
9\le p\le d/3,\qquad d-p\ge4.
\tag{6.14}
$$



All such counts are retained individually. No relative odd prefactor is replaced by $1$ in an integer identity, and no assumption about which tie occurs is required.

## 6.5 Whole four-zero candidate: PASS

For counts with $\mathcal L_p\le m_\star+3$, (6.14) applies:

- the pure-Cauchy atom-product part has four extra factors by (5.9);
- the bottom atom has at least four extra factors by (6.10);
- factorial patterns are globally deeper by (6.7)–(6.8).

Every remaining atom-product count already has nominal payment at least $m_\star+4$.

Therefore


$$
\boxed{2^{m_\star+4}\mid D_k.}
\tag{6.15}
$$



This conclusion is independent of the pending A2turn16 response because the particular aggregation and locality inputs used here have now been independently proved.

---

# 7. Audit of the complete modulo-$8$ source laws

## 7.1 Physical theta expansion: PASS

In (2.2), the $\ell=2$ term contains


$$
4(r+1)(r+2),
$$


which is divisible by $8$. Every $\ell\ge3$ term has an explicit factor $8$. Hence


$$
\boxed{
\theta_r^{(m)}
\equiv\theta_r+2m(r+1)\theta_{r+1}\pmod8.
}
\tag{7.1}
$$


The stated stronger physical-base law is correct.

## 7.2 Unchanged top and atom laws: PASS

A summand of (2.5) visible modulo $8$ has $4\mid h$. Then $d-h$ is a multiple of $4$, and every group of four consecutive odd factors has product $1\bmod8$. Thus


$$
Q_h(a)\equiv1\pmod8.
$$


Also


$$
a+h\equiv a\pmod4,\qquad d-h\equiv0\pmod4.
$$


The same shifted-binomial calculation now gives


$$
\boxed{
T_j^{(a)}(r)
\equiv o_d\{K_d(j,r)+2a(j+1)K_d(j+1,r)\}\pmod8.
}
\tag{7.2}
$$



In the atom formula, all $h\ge1$ terms contain $d\in16\mathbb Z$, while $Q_0(a)\equiv1\bmod8$. Therefore


$$
\boxed{A_j^{(a)}\equiv(-1)^{a+j}\pmod8.}
\tag{7.3}
$$



These statements retain $o_d$ and the literal atom ratios. They do not assert that either is $1\bmod8$.

## 7.3 Every elementary-symmetric and Stirling carry

For $p\ge5$, set


$$
x_t=d+t,\qquad
X_1=\sum_{t\in I}x_t,\qquad
X_2=\sum_{\substack{s<t\\s,t\in I}}x_sx_t,
$$


and $C_q=\binom pq$.

The elementary-symmetric expansion in $1+2x_t$ is


$$
e_{p-\ell}\equiv
\binom p\ell
+2X_1\binom{p-1}{\ell}
+4X_2\binom{p-2}{\ell}
\pmod8.
\tag{7.4}
$$


Thus $X_1\bmod4$ and $X_2\bmod2$ are exactly the required pole data.

In


$$
J_\ell=\sum_{q=\ell}^p2^{q-\ell}e_{p-q}S(q,\ell),
$$


the degrees $q=\ell,\ell+1,\ell+2$ survive. The relevant Stirling identities are


$$
S(\ell+1,\ell)=\binom{\ell+1}{2},
$$




$$
S(\ell+2,\ell)=\binom{\ell+2}{3}+3\binom{\ell+2}{4}.
$$


The latter counts one block of size three or two blocks of size two.

Using the integer binomial identities before reduction gives


$$
\boxed{
\begin{aligned}
J_\ell\equiv{}&
\binom p\ell
+2X_1\binom{p-1}{\ell}
+4X_2\binom{p-2}{\ell}\\
&+2C_2\binom{p-2}{\ell-1}\\
&+4\left\{X_1\binom{p-1}{2}+C_3\right\}
 \binom{p-3}{\ell-1}\\
&+4C_4\binom{p-4}{\ell-2}
\pmod8.
\end{aligned}}
\tag{7.5}
$$


The last coefficient is $4$, because $12\equiv4\bmod8$. Out-of-range binomial coefficients are zero.

No carry is missing.

## 7.4 Complete bottom law: PASS

From (2.9) and (7.1), with $j=p+z$,


$$
V_z^I\equiv
\sum_{\ell=0}^pJ_\ell
\{B_{j-\ell}+2\ell(j-\ell+1)B_{j-\ell+1}\}
\pmod8.
\tag{7.6}
$$


Again $d+\ell$ was used before the $2d$ term was removed modulo $8$.

The ordinary part of (7.5) converts directly to filters. The physical-base part needs $J_\ell\bmod4$. Its three contributions are


$$
2pjK_{p-1}(z+1)-2p(p-1)K_{p-2}(z+1),
$$




$$
4X_1(p-1)jK_{p-2}(z+2),
$$




$$
4C_2j\{K_{p-2}(z+2)+(p-2)K_{p-3}(z+2)\}.
$$


The omitted term in the second line has the even factor $(p-1)(p-2)$. In the third line the discarded part has $k(k+1)$, also even.

Combining all terms yields exactly


$$
\boxed{
\begin{aligned}
V_z^I\equiv{}&
K_p(z)+2(X_1+pj)K_{p-1}(z+1)-2C_2K_{p-2}(z+1)\\
&+4\{X_2+j[X_1(p-1)+C_2]\}K_{p-2}(z+2)\\
&+4\left\{X_1\binom{p-1}{2}+C_3+jC_2(p-2)\right\}
 K_{p-3}(z+2)\\
&+4C_4K_{p-4}(z+2)
\pmod8.
\end{aligned}}
\tag{7.7}
$$



For the actual minimal set,


$$
\boxed{
X_1=2dp-\binom{p+1}{2},\qquad
X_2\equiv\binom{\lceil p/2\rceil}{2}\pmod2.
}
\tag{7.8}
$$


The second formula counts pairs of odd elements in the literal interval
$\{2d-p,\ldots,2d-1\}$.

The modulo-$8$ source candidate therefore survives the algebraic audit.

---

# 8. New evaluated second effective lift

## 8.1 Full integer lifts are fixed before division

The first binary combinations must not be reduced prematurely.

Set, as full integers,


$$
b=X_1+p+C_2,\qquad c=pD+C_2,
$$




$$
\mu=X_1(p-1)+C_2,\qquad
\nu=C_2(p-2),
$$




$$
\varphi=X_1\binom{p-1}{2}+C_3,\qquad
\chi=C_4.
\tag{8.1}
$$


In particular, $b$ is not replaced by its parity before the next division.

Using Pascal’s identity, (7.7) can be rewritten


$$
V_z^I\equiv K_p(z)+2U_z+4W_z\pmod8,
\tag{8.2}
$$


where


$$
U_z=(pz+b)K_{p-1}(z+1)+C_2K_{p-2}(z+2),
\tag{8.3}
$$


and


$$
\boxed{
\begin{aligned}
W_z={}&[X_2+(p+z)\mu]K_{p-2}(z+2)\\
&+[\varphi+(p+z)\nu]K_{p-3}(z+2)
+\chi K_{p-4}(z+2).
\end{aligned}}
\tag{8.4}
$$



Let $H=1+E$, where $E$ shifts the bottom-row index. Put


$$
P_0=H^D,\qquad P_1=EH^D,
$$


and choose the following full integer lifts of the first binary bottom combinations:


$$
\boxed{
C_0=aEH^D-bEH^{D-1}-cE^2H^{D-2},
}
\tag{8.5}
$$




$$
\boxed{
C_1=-(p+b)E^2H^{D-1}-cE^3H^{D-2}.
}
\tag{8.6}
$$


Their degrees are at most $D+1$, so they use only the actual bottom rows.

The $2aK_d(2)$ term in the first divided relation for row $1$ has zero binary coefficient. We choose its lift to be zero in (8.6), rather than introducing the nonexistent bottom order $D+2$. Its resulting carry will be retained explicitly below.

Let $\mathsf Z_j$ denote normalized top row $j$, including its actual atom coordinate. The complete rows


$$
\boxed{
\mathcal E_j=
\frac{\mathsf Z_j-P_jV-2C_jV}{4},
\qquad j=0,1,
}
\tag{8.7}
$$


are already known to be $2$-integral by the first-lift proof.

Changing $C_j$ to a binary-coefficient lift would change $\mathcal E_j$ by the explicit bottom combination


$$
\frac{C_j-C_j^{\rm bin}}2V.
$$


Thus such carries are not absent; the full choice (8.5)–(8.6) records them.

## 8.2 Evaluation of the second contact residues

For every nonnegative $q,s$,


$$
\boxed{
\sum_t\binom qtU_{s+t}
=
(ps+b)K_{p+q-1}(s+1)
+(pq+C_2)K_{p+q-2}(s+2).
}
\tag{8.8}
$$


The analogous convolution of (8.4) is obtained by the same first-moment identity. In particular,


$$
\begin{aligned}
P_jW={}&[X_2+(p+j)\mu]K_{d-2}(j+2)
+D\mu K_{d-3}(j+3)\\
&+[\varphi+(p+j)\nu]K_{d-3}(j+2)
+D\nu K_{d-4}(j+3)
+\chi K_{d-4}(j+2).
\end{aligned}
\tag{8.9}
$$



The source law (7.2), with the full combinations retained, gives


$$
\mathcal E_0\equiv-P_0W-C_0U\pmod2,
$$




$$
\mathcal E_1\equiv aK_d(2)-P_1W-C_1U\pmod2.
\tag{8.10}
$$



Expanding (8.8)–(8.10) evaluates these rows completely. Their contact coordinates are:



$$
\boxed{
\begin{aligned}
\mathcal E_0\equiv{}&
a(p+b)K_{d-1}(2)+acK_{d-2}(3)\\
&+[X_2+p\mu+b(p+1)]K_{d-2}(2)\\
&+[D\mu+bp]K_{d-3}(3)
+[\varphi+p\nu]K_{d-3}(2)\\
&+D\nu K_{d-4}(3)+\chi K_{d-4}(2)+cK_{d-4}(4)
\pmod2,
\end{aligned}}
\tag{8.11}
$$


and


$$
\boxed{
\begin{aligned}
\mathcal E_1\equiv{}&
aK_d(2)\\
&+[X_2+(p+1)\mu+b(p+1)]K_{d-2}(3)\\
&+[D\mu+p(1+b)]K_{d-3}(4)\\
&+[\varphi+(p+1)\nu]K_{d-3}(3)\\
&+D\nu K_{d-4}(4)+\chi K_{d-4}(3)+cK_{d-4}(5)
\pmod2.
\end{aligned}}
\tag{8.12}
$$



These are evaluated identities, not unevaluated effective-return symbols.

## 8.3 Exact finite-span test and the boundary obstruction

Assume $D\ge4$. Every term


$$
K_{d-s}(t)=E^tH^{D-s}K_p(0)
$$


in (8.11) uses bottom orders at most $D+1$. The same is true of every term in (8.12) except $aK_d(2)$.

Indeed,


$$
K_d(2)=H^DK_p(2)
$$


has highest bottom order $D+2$, which would correspond to normalized bottom jet $d+2$, outside the physical boundary $d+1$.

Therefore the exact second-lift statement at an arbitrary top base is


$$
\boxed{
\mathcal E_0\in\operatorname{span}_{\mathbb F_2}(V_0,\ldots,V_{D+1}),
}
\tag{8.13}
$$




$$
\boxed{
\mathcal E_1\equiv aK_p(D+2)
\pmod{\operatorname{span}_{\mathbb F_2}(V_0,\ldots,V_{D+1})}.
}
\tag{8.14}
$$



Equation (8.14) is the precise obstruction to an unqualified “both second lifts are again bottom relations” claim at an odd base.

The concrete repair is already paid by (5.3): expand every original source set $J$ in the finite Newton basis at $a=0$. This does not replace the original source values; it is their exact finite expansion. At that base, the offending term vanishes.

The atom coordinates also pass. For the first two rows, the numerator in (8.7) has unchanged atom coordinate


$$
\frac{R_m}{R_j}\frac{A_j^{(0)}}{o_d}.
$$


If $m\ge4$, its valuation is at least $3$, so after division by $4$ it is still even. Hence the bottom-span conclusions are conclusions about the complete rows.

Subtract the bottom combinations specified by (8.11)–(8.12), now at $a=0$. Both rows in (8.7) become even. Thus each of the original two rows is divisible by $8$, and


$$
\boxed{64\mid\det\widetilde Z_{I,U}^{(0)}}
\tag{8.15}
$$


whenever $U$ contains $0,1$, $m\ge4$, and $D\ge4$.

No unit minor and no exact corank assertion is involved.

---

# 9. Complete six-zero consequence

## 9.1 All source-jet patterns still within budget

For $\epsilon(U)\le5$, the additional nonzero tails beyond (5.8) are



$$
\begin{array}{c|l}
\epsilon&\text{nonzero shift tails}\\ \hline
4&(4),(1,3),(2,2),(1,1,2),(1,1,1,1),\\
5&(5),(1,4),(2,3),(1,1,3),(1,2,2),
(1,1,1,2),(1,1,1,1,1).
\end{array}
\tag{9.1}
$$



These are all partitions of the excess, written as nondecreasing tails. For $p\ge7$, every one contains jet orders $0,1$, and its maximum is at least $p-1\ge6$.

Thus (8.15) applies to every pattern with $\epsilon\le5$. Every other pattern already pays at least six factors through (5.6). Any additional rising-factor valuation or Newton-coefficient valuation only increases the payment.

For every $I,J$, therefore,


$$
\boxed{
\text{pure-Cauchy atom-product \(p\)-sector}
\in2^{\mathcal L_p+6}\mathbb Z_2,
\qquad p\ge7,\ d-p\ge4.
}
\tag{9.2}
$$



This includes all actual $N_d$-minors and all atom positions. Only the first two atom coordinates were used in the row-division argument; every other atom coordinate remains in the determinant.

## 9.2 Complete sectors and the whole determinant

For


$$
9\le p\le d/3,
$$


the bottom atom pays at least seven extra factors by (6.10), and factorial terms pay more than seven by (6.9). Hence


$$
\boxed{\mathcal D_p\in2^{\mathcal L_p+6}\mathbb Z_2}
\tag{9.3}
$$


for the complete $p$-sector in this range.

Every product count with


$$
\mathcal L_p\le m_\star+5
$$


lies in this range by (6.13)–(6.14). Every other atom-product count already has nominal payment at least $m_\star+6$. The global factorial and all-bottom arguments cover the remaining classes.

We have proved:

### Theorem 9.1 — complete second-lift lower divisor

On every original index $k=9^{18+32u}$,


$$
\boxed{
2^{m_\star+6}\mid
\det[w_*,v^{(0)},\ldots,v^{(d)}].
}
\tag{9.4}
$$



Using the passed linear-coefficient identity,


$$
\boxed{
v_2(I_{1,k})\ge\alpha+A+m_\star+6.
}
\tag{9.5}
$$



The four-zero parent candidate is therefore not only passed; it is strengthened by two further complete zero digits.

---

# 10. A paid reduction of the next possible digit

The new lower bound permits a sharper statement of the remaining local obligation.

For a minimizing count $p$, let $\widetilde Z_{p,0}$ have top rows $j=0,\ldots,p-1$


$$
\left[
\frac{R_{p-1}}{R_j}\frac{A_j^{(0)}}{o_d},
\quad
\left(\frac{T_j^{(0)}(r)}{o_d}\right)_{r=0}^d
\right],
$$


and bottom rows


$$
[0,V_z^{T_p}],\qquad 0\le z\le d+1-p.
$$



The exact finite Newton coefficient of the minimal jet set on the consecutive source set $T_p$ is


$$
\det\left[\binom{x}{j}\right]_{\substack{x\in T_p\\0\le j<p}}
=\frac{V(T_p)}{\Phi_p}=1.
$$



At precision $\mathcal L_p+7$:

- every nonminimal $N_d$-pair pays one extra factor on top of the six proved factors;
- every positive-excess source pattern through excess six contains $0,1$ in the original minimizing strip and pays six additional factors;
- higher source excess is already at least seven;
- bottom atoms and factorial terms are deeper.

Thus the remaining scalar is the actual odd unit


$$
\boxed{
\begin{aligned}
u_p={}&
\gamma^{\,n-p}\Lambda_k^p
\frac{\det N_d[T_p,T_p]}{2^{2E_p}}
\operatorname{odd}(\Phi_p)^2
\frac{\mathfrak F_p}{2^{B_p}}\,o_d^p\\
&\times
\frac{\displaystyle\prod_{j=p}^{n-1}\operatorname{odd}(j!)}
{\displaystyle\prod_{i=0}^{n-1}Q_{T_p}(i)}.
\end{aligned}}
\tag{10.1}
$$



Let


$$
\mathcal P_\star=\{p:\mathcal L_p=m_\star\}.
$$


It has one element or two adjacent elements, and both are retained. The paid reduction is


$$
\boxed{
\frac{D_k}{2^{m_\star+6}}
\equiv
\sum_{p\in\mathcal P_\star}
u_p\,\frac{\det\widetilde Z_{p,0}}{64}
\pmod2.
}
\tag{10.2}
$$



Equation (10.2) is **not** an evaluation as nonzero. It identifies the next exact obstruction after the proved six zeros.

The quotient $\det\widetilde Z_{p,0}/64$ is the determinant after the two certified row divisions by $8$. Its parity requires the appropriate normalized source information modulo $16$, before those divisions. The remaining matrix may have additional corank; a single unit cofactor cannot replace its determinant.

A concrete follow-on lemma is therefore:

> **Third-lift/noncancellation lemma.** Produce complete modulo-$16$ source laws and evaluate the full determinant in (10.2), with the specified integer row lifts, at the same original indices. A nonzero value of the complete sum would prove
> 

$$
> v_2(D_k)=m_\star+6.
>
$$


> A further zero would be another lower-divisibility theorem, not an upper bound.

This is the exact local bottleneck. The source formulas needed for it have not been proved here.

---

# 11. Audit and scope ledger

| Assertion | Verdict and exact scope |
|---|---|
| $v_2(d)=4$, physical terminal $3d+1$ | **PASS**, original indices retained |
| Integral $\theta_r^{(m)}$, full return divisor | **PASS** |
| Full top divisor $2^j(d+1)_j$ | **PASS**, $a+j\le d-1,\ r\le d$ |
| Actual atom formula and rising ratios | **PASS** |
| Modulo-$4$ top law for arbitrary admitted $a$ | **PASS** |
| Modulo-$4$ bottom law for every actual $I$ | **PASS**, with base $d+\ell$ retained |
| Both first divided complete rows lie in bottom span | **PASS**, $p\ge5,\ d-p\ge2$ in the application |
| Factor $16$ for every low-excess normalized aggregate | **PASS** |
| FULL24 exact finite source-jet aggregation | **PASS independently here at the indispensable scope** |
| Unique minimal $N_d$-sets and weight-one locality | **PASS** |
| A2turn15 global factorial comparison | **PASS**, all $1\le v\le p\le d$, including $p=v$ |
| $p=0$ and small-$p$ separation | **PASS** |
| Actual bottom-atom rising payment in the minimizing strip | **PASS** |
| Whole four-zero consequence | **PASS** |
| Modulo-$8$ physical theta law | **PASS** |
| Claimed unchanged modulo-$8$ top and atom laws | **PASS** |
| Complete $J_\ell\bmod8$, including all carries | **PASS** |
| Complete $V_z^I\bmod8$, including $X_1\bmod4$, $X_2\bmod2$ | **PASS** |
| Automatic repetition of the second bottom-span argument at arbitrary odd base | **Not valid without repair**: the term $aK_d(2)$ reaches bottom order $D+2$ |
| Exact finite base-$0$ Newton repair | **NEW PROVED REPAIR** |
| Evaluated second effective rows (8.11)–(8.12) | **NEW PROVED IDENTITIES** |
| Whole six-zero theorem (9.4) | **NEW PROVED RESULT** |
| Exact corank two, a nonzero next digit, or a useful terminal upper | **OPEN; not inferred** |
| Complete constant coefficient (1.9) | **Unevaluated; retained literally** |
| Other-prime arithmetic and final all-prime gcd | **OPEN** |
| Rationality or irrationality of $e+\pi$ | **OPEN** |

The pending A2turn16 audit may address further locality or rank assertions. No conclusion here assumes its eventual outcome. The specific aggregation and valuation facts used in this report have their independent derivations above.

No ternary index family has been merged with this dyadic family. The separate FULL25 moment-lift and $\Delta A/\Delta C$ obligations are not repeated or declared resolved.

---

# 12. Actual contents, least clearer, all-prime gcd, and whole error

The original determinant remains


$$
H_k(s)=H_{0,k}+H_{1,k}s
=
\det\left[
(c_{m+j})\ \middle|\ 
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right],
$$


with $0\le m<2k,\ 0\le j<k$.

The individual least right-column entry clearers are


$$
\Lambda_{k,j}=\operatorname{lcm}(1,3,\ldots,4k+2j-3).
$$


Retain the all-prime quantities


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
$$




$$
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


The actual least simultaneous coefficient clearer and subsequent content are exactly


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
}
\tag{12.1}
$$



The actual maximal-minor contents of the original rectangles remain


$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
\mathscr L_k=\delta_{2k-1}(Y_k),
$$


where


$$
Z_k=[(c_{m+j})_{m<2k,j<k}\mid(T_{m+j})_{m<2k,j<k-1}],
$$




$$
Y_k=[(\sigma_{m+j})_{m<2k-1,j<k}\mid(T_{m+j})_{m<2k-1,j<k}].
$$


Their established relation is


$$
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k\mid\Lambda_k\mathscr L_k\mathscr R_k.
\tag{12.2}
$$



The paid five-column pivots and their odd quotients are reused, not recomputed. With


$$
\lambda_d^{\rm tr}=d\alpha+4d+4,\qquad
\mathfrak D_d=\prod_{r<d}2^rr!,
$$


the exact all-prime transfer remains


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_{5,k}|^{d-4}G_k
=
|f_k|\,2^{\lambda_d^{\rm tr}+d+69}
\mathfrak D_d\,g_k^{[5]}.
}
\tag{12.3}
$$


Every odd factor in this identity remains actual.

The open joint binary target is still


$$
\min(v_2(I_{0,k}),v_2(I_{1,k}))
\le \frac{15}{4}k^2+d+5+O(k\log k).
\tag{12.4}
$$


A lower bound for $I_{1,k}$ does not prove (12.4), nor does it determine a common divisor of both coefficients.

The actual primitive denominator and numerator remain


$$
q_k=\frac{|H_{1,k}|}{G_k}>0,\qquad
p_k=-\frac{(-1)^kH_{0,k}}{G_k}.
$$


The retained same-index whole evaluated error is


$$
\boxed{
0<q_k(e+\pi)-p_k
=\frac{|H_k(e+\pi)|}{G_k}.
}
\tag{12.5}
$$


Neither a pure-Cauchy reference, a selected error summand, nor a binary divisor is substituted for (12.5).

The odd-prime descents, large-prime exclusions, final all-prime $G_k$, and any primitive-error conclusion remain separate obligations. Even a future retirement of this producer would not decide the rationality of $e+\pi$.

---

# 13. Finite evidence and an optional new bounded diagnostic

## 13.1 Closed receipt

The supplied receipt reports:

- $20{,}653$ top checks;
- $317$ atom checks;
- $108{,}174$ bottom checks;
- $11{,}304$ complete second-even coordinates;
- $90$ auxiliary configurations;

all passing at $d=16,48,80$.

That receipt is closed auxiliary evidence. It has not been rerun, and it supplies no modulo-$8$, original-index, or infinite theorem. The proofs above are algebraic.

No computation is indispensable to the proved results in this report.

## 13.2 Optional genuinely new diagnostic

If a coordinator wants a bounded independent check of the new modulo-$8$ and second-effective-row identities, the following is sufficient and does not involve an original-sized solve.

### Exact inputs

Use only


$$
d=16,\qquad p\in\{7,8,9\},
$$


with pole sets


$$
I=T_p,\qquad
I=T'_p=\{d-p-1,d-p+1,\ldots,d-1\}.
$$


Use top bases $a=0,1$.

Generate the exact original recurrence values $u_m=a_{2m}$ only for


$$
0\le m\le49=3d+1.
$$


Use the literal polynomial $P_{16}$, full divisors $2^rr!$, $2^jR_j$, $2^jj!$, and


$$
o_{16}=16!/2^{15}.
$$



Take all nineteen source-jet patterns of unweighted excess $0,\ldots,5$ listed in (5.8) and (9.1). Their largest top order is at most $13$, so both bases satisfy the finite top boundary.

### Expected verifiable outputs

1. Zero discrepancies in the new modulo-$8$ top law for
   

$$
a=0,1,\quad 0\le j\le13,\quad 0\le r\le16
$$


   — $476$ coordinate checks.

2. Zero discrepancies in the atom law on the same $a,j$ — $28$ checks.

3. Zero discrepancies in the complete bottom law for both pole sets, all $r=0,\ldots,16$, and all admitted bottom orders — $1{,}020$ checks.

4. Zero discrepancies in the evaluated second-effective-row identities (8.11)–(8.12), including the atom coordinate, for all $228$ configurations — $8{,}208$ complete-coordinate checks.

5. For the $114$ base-$0$ configurations, after subtracting the explicit second bottom combinations, every one of the two complete numerators is divisible by $8$ — $4{,}104$ coordinate divisibility checks.

Odd denominators can be avoided in the implementation by multiplying the auxiliary row identities by the actual $o_{16}$ before checking remainders.

The base-$1$ checks must retain the term $K_d(2)$ in (8.12); they must not falsely expect it to be an admitted bottom row.

This diagnostic would establish only those stated finite checks. It is not a computation of $D_k$, $\mathbf K_d^{-1}$, an original Smith form, or a terminal valuation upper.

---

# Final conclusion

The supplied parent theta first-lift formulas survive a different complete audit. Their factor-$16$ consequence is valid for the complete finite source-jet aggregation, not just for a minimal source minor. The global factorial exclusion also passes for every product count and every number of factorial columns, with the $p=0$, small-$p$, bottom-atom, and finite-boundary payments retained. Therefore the parent whole four-zero statement is proved.

The complete modulo-$8$ source formulas likewise pass. They permit an evaluated second effective lift. That lift exposes a real boundary term at an arbitrary odd top base, but the exact finite base-$0$ Newton expansion gives a concrete, fully paid repair.

The new result is


$$
\boxed{
2^{m_\star+6}\mid
\det[w_*,v^{(0)},\ldots,v^{(d)}]
}
$$


at every original index.

The exact next local bottleneck is the complete third-lift residue in (10.2), requiring normalized modulo-$16$ source information before division and noncancellation across every minimizing product count. No exact-corank assumption or selected unit minor can replace that calculation.

The whole coefficient upper, the complete constant border, other-prime arithmetic, final all-prime gcd, actual primitive denominator, and positive whole error remain at their stated unresolved scopes.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi\text{ is obtained.}}
$$


