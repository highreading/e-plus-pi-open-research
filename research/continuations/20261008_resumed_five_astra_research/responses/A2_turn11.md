> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A paid Newton frame and an evaluated dyadic paired cofactor for the original coefficient pencil

## 1. Result and proof status

The rationality or irrationality of $e+\pi$ remains unresolved. I also do **not** prove the requested uniform upper bound


$$
v_2(G_k)\le \frac{19}{4}k^2+o(k^2)
$$


on the original index set.

There is, however, a new evaluated source lemma after the turn10 rational annihilator. It has three parts.

1. **A full weighted Newton column payment.**  
   All $d=k-1$ corrected contact-return columns admit the additional, simultaneous integer divisions
   

$$
D_r=2^r r!,\qquad 0\le r<d.
$$


   The entire factor
   

$$
\mathfrak D_d=\prod_{r=0}^{d-1}2^r r!
$$


   is retained, including its odd part.

2. **An evaluated paired cofactor, not an assumed residual unit.**  
   In that paid pencil, the retained contact column and the first divided contact-return difference have actual two-column maximal-minor content with binary valuation exactly $5$. More precisely, if their entries in the residual physical rows are $x_i,y_i$, $0\le i<d+2$, then
   

$$
\boxed{
   x_i\equiv1\pmod2,\qquad
   32\mid x_i y_j-x_jy_i,\qquad
   \frac{x_i y_j-x_jy_i}{32}\equiv j-i\pmod2.
   }
   \tag{1.1}
$$


   In particular, the first two residual rows give
   

$$
\boxed{
   x_0y_1-x_1y_0=32\mu_k,\qquad \mu_k\ \text{odd}.
   }
   \tag{1.2}
$$


   Every physical row can therefore be interpolated from these two rows over $\mathbb Z_{(2)}$, after a proved integer division by $32$. The remaining denominator is the explicitly retained odd integer $\mu_k$.

3. **A further paid reduction of the complete affine pair.**  
   After that evaluated two-column elimination, every entry of the remaining $d\times d$ pencil is even. Paying those $d$ row divisions gives an explicitly defined integer pencil
   

$$
\mathcal P_k(s),\qquad
   \det\mathcal P_k(s)=P_{0,k}+P_{1,k}s.
$$


   With
   

$$
g_k^{\mathrm{new}}=\gcd(|P_{0,k}|,|P_{1,k}|),
   \qquad
   \nu_k=v_2(g_k^{\mathrm{new}}),
$$


   the resulting exact binary identity is
   

$$
\boxed{
   v_2(G_k)=\chi_k+\nu_k,
   }
   \tag{1.3}
$$


   where, on the unchanged original domain,
   

$$
\boxed{
   \chi_k
   =
   d^2+4d+29+(d+4)s_2(d)
   -3\sum_{n=0}^{d-1}s_2(n)
   =
   k^2+O(k\log k).
   }
   \tag{1.4}
$$



This is more than another definition of a Schur determinant. The new calculation evaluates a complete corrected two-column cofactor lattice at $2$, proves its saturation after the exact payment $32$, evaluates its row-interpolation residues, and removes the full Newton factor $\mathfrak D_d$. No uncomputed cofactor or interpolation denominator is declared a binary unit.

The remaining single binary valuation is precisely $\nu_k$. A sufficient next statement is


$$
\boxed{
\nu_k\le \frac{15}{4}k^2+O(k\log k)
\qquad
\bigl(k=9^{18+32u}\bigr).
}
\tag{1.5}
$$


It would imply the final-$G$ target $19/4$. Statement (1.5) remains open.

---

## 2. Original objects and normalization

### 2.1 Unchanged index set and complete sequences

Throughout,


$$
\boxed{
\mathcal K=\{9^{18+32u}:u\ge0\},\qquad d=k-1.
}
\tag{2.1}
$$


In particular, every original $d$ satisfies


$$
d\ge32,\qquad v_2(d)=4,\qquad d\equiv2\pmod3.
\tag{2.2}
$$


The assertion $v_2(d)=4$ is reused from turn10. No auxiliary compact index replaces $\mathcal K$.

Retain


$$
a_0=1,\qquad a_n=1-na_{n-1},
$$




$$
u_n=a_{2n},\qquad f_n=(2n)!,\qquad w_n=(-1)^n,
\qquad c_n=u_n-w_n,
$$


and


$$
\rho_0=0,\qquad
\rho_{n+1}+\rho_n=\frac1{2n+1},
\qquad r_n=-f_n+4\rho_n.
\tag{2.3}
$$



The returns remain


$$
\sigma_n=c_{n+1}+c_n=u_{n+1}+u_n
\tag{2.4}
$$


and


$$
\boxed{
\tau_n=r_{n+1}+r_n
=-(2n+2)!-(2n)!+\frac4{2n+1}.
}
\tag{2.5}
$$



Put


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),
\qquad T_n=\Lambda_k\tau_n.
$$


Thus the complete integer forcing is


$$
\boxed{
T_n
=
-\Lambda_k\bigl((2n+2)!+(2n)!\bigr)
+\frac{4\Lambda_k}{2n+1}.
}
\tag{2.6}
$$



The original determinant is


$$
\boxed{
H_k(s)=
\det\left[
(c_{m+j})\
\middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right]
=H_{0,k}+H_{1,k}s,
}
\tag{2.7}
$$


where $0\le m<2k$ and $0\le j<k$.

Its physical terminal remains


$$
\boxed{
\text{moment }3k-2,\qquad
\text{factorial }(6k-4)!,\qquad
\text{last odd denominator }6k-5.
}
\tag{2.8}
$$



### 2.2 Actual clearers, contents, final gcd, and whole error

The individual least original right-column entry clearers remain


$$
\Lambda_{k,j}
=
\operatorname{lcm}(1,3,\ldots,4k+2j-3),
\qquad 0\le j<k.
\tag{2.9}
$$


The common least entry clearer is $\Lambda_k$.

The final gcd is always the all-prime gcd


$$
\boxed{
G_k=\gcd(|H_{0,k}|,|H_{1,k}|).
}
\tag{2.10}
$$


For the rational coefficient pair $H_k/\Lambda_k^k$, define


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
\tag{2.11}
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
\tag{2.12}
$$


Write


$$
\mathscr R_k=\delta_{2k-1}(Z_k),
\qquad
\mathscr L_k=\delta_{2k-1}(Y_k).
$$


The established interface is


$$
\boxed{
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k
\mid \Lambda_k\mathscr L_k\mathscr R_k.
}
\tag{2.13}
$$



The accepted sign and nonvanishing results imply, at every original index,


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
\tag{2.14}
$$


Neither $q_k$ nor the whole error $\ell_k$ is replaced by a quantity obtained from a lower divisor of $G_k$.

---

## 3. The paid turn10 reduction being continued

The turn10 annihilator and factorial pivot are reused at their displayed scope. Their different full audit is still pending; this report does not claim that the pending audit has occurred. The new argument below does not assume that their residual pencil is a unit.

### 3.1 Rational annihilator and complete forcing pivot

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


Because $d$ is even,


$$
\mathcal A_d y=\Delta^d(P_dy).
\tag{3.2}
$$



The square row operation $\mathcal S_d$ applies $\mathcal A_d$ to rows $0,\ldots,d-1$ and leaves rows $d,\ldots,2d+1$ unchanged. Its determinant is


$$
\Omega_k=\prod_{n=0}^{d-1}P_d(n),
\tag{3.3}
$$


an explicitly retained odd integer.

The rational channel in every one of the $d$ common return columns is annihilated exactly. With


$$
b(t)=4t^2+6t+3,
$$


the complete resulting forcing entries are


$$
F_k(n,j)
=
-\Lambda_k
\sum_{i=0}^d
(-1)^i\binom di
P_d(n+i)b(n+i+j)(2(n+i+j))!,
\quad n,j<d.
\tag{3.4}
$$


Here $b(t)(2t)!=(2t+2)!+(2t)!$; both factorial terms remain.

Put


$$
D_f=\operatorname{diag}((2n)!)_{0\le n<d},
$$


and


$$
K_d(n,j)=
\sum_{i=0}^d
(-1)^i\binom diP_d(n+i)b(n+i+j)
\frac{(2(n+i+j))!}{(2n)!(2j)!}.
\tag{3.5}
$$


Then


$$
F_k=-\Lambda_kD_fK_dD_f.
\tag{3.6}
$$



The established congruence is


$$
K_d(n,j)\equiv\binom{n+j}{j}\pmod2.
\tag{3.7}
$$


In particular, $\eta_d=\det K_d$ is odd. We will also use its immediate finite-block consequence:

> Every leading principal block of $K_d$ has odd determinant.

This uses the same classical Pascal Gram factorization already established in turn10; no new Pascal determinant theorem is being claimed.

The exact forcing determinant and its binary valuation are


$$
f_k=\det F_k
=(-\Lambda_k)^d\eta_d
\left(\prod_{n=0}^{d-1}(2n)!\right)^2,
$$




$$
v_2(f_k)=V_d
=2\sum_{n=0}^{d-1}v_2((2n)!).
\tag{3.8}
$$



### 3.2 Complete residual pencil and all its old payments

After the determinant-one adjacent-column operations and the already paid column permutation,


$$
H_k(s)=\det[\mathcal T\mid\mathcal M(s)],
$$


where


$$
\mathcal T=(T_{m+j})_{\substack{0\le m<2d+2\\0\le j<d}},
$$




$$
\mathcal M(s)
=
[c_m\mid(\sigma_{m+j})_{j<d}\mid
\Lambda_k(r_m+sw_m)]_{m<2d+2}.
\tag{3.9}
$$


Thus all $d$ common return columns and the complete affine border remain.

Partition


$$
\mathcal S_d[\mathcal T\mid\mathcal M(s)]
=
\begin{pmatrix}
F_k&A_0+sA_1\\
B&C_0+sC_1
\end{pmatrix}.
\tag{3.10}
$$


The bottom rows are exactly the original rows $m=d,\ldots,2d+1$.

Set


$$
h_d=(2d-2)!,
\qquad
\beta_d=v_2(h_d),
\qquad
\widehat D_f=h_dD_f^{-1},
$$




$$
N_d=\widehat D_f\,\operatorname{adj}(K_d)\,\widehat D_f,
\qquad
\delta_k=\Lambda_k\eta_dh_d^2.
\tag{3.11}
$$


Then


$$
F_k^{-1}=-\frac{N_d}{\delta_k},
\qquad
v_2(\delta_k)=2\beta_d.
\tag{3.12}
$$



The complete integer Schur numerators are


$$
E_i=\delta_kC_i+BN_dA_i,\qquad i=0,1.
\tag{3.13}
$$



Put


$$
\alpha_d=v_2((2d)!).
$$


The already proved simultaneous column divisions are:

* $2^{d+2}$ from the first contact column;
* $2^{\alpha_d+3}$ from each of the $d$ contact-return columns;
* $4$ from the complete affine border.

The resulting integer pencil is $\widehat E_k(s)$, with


$$
\det\widehat E_k(s)=J_{0,k}+J_{1,k}s.
$$


The total old binary column payment is


$$
\lambda_d=d\alpha_d+4d+4.
\tag{3.14}
$$


Thus


$$
\boxed{
\delta_k^{d+2}\Omega_kH_{i,k}
=f_k\,2^{\lambda_d}J_{i,k},
\qquad i=0,1.
}
\tag{3.15}
$$



Writing $g_k^\sharp=\gcd(|J_{0,k}|,|J_{1,k}|)$, the exact all-prime identity is


$$
|\delta_k|^{d+2}\Omega_kG_k
=
|f_k|\,2^{\lambda_d}g_k^\sharp.
\tag{3.16}
$$


At $2$,


$$
v_2(G_k)=\kappa_k+v_2(g_k^\sharp),
\tag{3.17}
$$


where, on the original domain,


$$
\boxed{
\kappa_k
=
4d+24+(d+4)s_2(d)
-2\sum_{n=0}^{d-1}s_2(n).
}
\tag{3.18}
$$



The new work starts with this particular, fully paid pencil.

---

## 4. A full weighted Newton payment in the corrected contact-return columns

Define


$$
D_r=2^rr!,\qquad 0\le r<d,
\qquad
\mathfrak D_d=\prod_{r=0}^{d-1}D_r.
\tag{4.1}
$$



In the $d$ contact-return columns of $\widehat E_k(s)$, make the determinant-one Newton transformation


$$
(\sigma_0,\ldots,\sigma_{d-1})
\longmapsto
(\sigma_0,\Delta\sigma_0,\ldots,\Delta^{d-1}\sigma_0),
\tag{4.2}
$$


where each column is understood with its original row shifts. Then divide column $r$ by the full integer $D_r$.

### Proposition 4.1

All these divisions are integral in the complete corrected pencil.

#### Proof

Reuse the sequence divisibility


$$
2^{t+1}t!\mid\Delta^t\sigma_n
\qquad(n,t\ge0).
\tag{4.3}
$$


Also,


$$
\Delta^hP_d(n)
=
2^h\frac{d!}{(d-h)!}
Q_h(n),
\qquad
Q_h(n)=\prod_{a=h}^{d-1}(2n+2a+1).
\tag{4.4}
$$



Apply the finite-difference product rule to


$$
\mathcal A_d(\Delta^r\sigma)_n
=\Delta^d(P_d\Delta^r\sigma)_n.
$$


Every summand has the form


$$
\binom dh
2^h\frac{d!}{(d-h)!}Q_h(n)
\Delta^{d-h+r}\sigma_{n+h}.
$$


By (4.3), it is divisible by


$$
2^{d+r+1}d!r!,
$$


because


$$
\frac{(d-h+r)!}{(d-h)!}
=r!\binom{d-h+r}{r}.
$$


Therefore


$$
\boxed{
2^{d+1}d!D_r
\mid
\mathcal A_d(\Delta^r\sigma)_n.
}
\tag{4.5}
$$



The bottom contact-return entry satisfies


$$
2D_r\mid\Delta^r\sigma_m.
\tag{4.6}
$$



In the Schur numerator, $B$ is divisible by $4$. Moreover, the old payment inequality gives


$$
2\beta_d\ge\alpha_d+2.
\tag{4.7}
$$


Consequently, after division by $2^{\alpha_d+3}D_r$,

* the term $BN_d\mathcal A_d(\Delta^r\sigma)$ is integral by (4.5);
* the term $\delta_k\Delta^r\sigma$ is integral by (4.6)–(4.7).

The odd part of $d!$ is not discarded:


$$
\frac{2^{d+1}d!}{2^{\alpha_d+1}}
=\operatorname{odd}(d!)\in\mathbb Z.
$$


This proves the proposition. ∎

Let the resulting integer pencil be $\mathcal Q_k(s)$, with


$$
\det\mathcal Q_k(s)=I_{0,k}+I_{1,k}s.
$$


Exactly,


$$
\boxed{
J_{i,k}=\mathfrak D_d I_{i,k},
\qquad i=0,1.
}
\tag{4.8}
$$


This is an all-prime identity. In particular,


$$
v_2(\mathfrak D_d)
=
\sum_{r=0}^{d-1}(r+v_2(r!))
=
d(d-1)-\sum_{r=0}^{d-1}s_2(r).
\tag{4.9}
$$



The division by $\mathfrak D_d$ alone would not evaluate a residual cofactor. The next sections provide that missing evaluation.

---

## 5. Two normalized source columns

Let $x$ be the first contact column of $\mathcal Q_k(s)$. Let $y$ be its contact-return column $r=1$, namely the column obtained from $\Delta\sigma$ after all old payments and the additional division $D_1=2$.

Both are independent of $s$.

Write


$$
R=\frac B4\in\mathbb Z^{(d+2)\times d},
\tag{5.1}
$$


and define top source vectors


$$
a_n=\frac{(\mathcal A_dc)_n}{2^d},
\qquad
b_n=\frac{(\mathcal A_d\Delta\sigma)_n}{2^{\alpha_d+2}},
\qquad 0\le n<d.
\tag{5.2}
$$


Here $a_n$ is local notation for a normalized column entry, not a redefinition of the original recurrence sequence.

The exact corrected columns are


$$
\boxed{
x
=
RN_da+\frac{\delta_k}{2^{d+2}}c_{\mathrm{bot}},
}
\tag{5.3}
$$




$$
\boxed{
y
=
RN_db+\frac{\delta_k}{2^{\alpha_d+4}}
(\Delta\sigma)_{\mathrm{bot}}.
}
\tag{5.4}
$$



The two bottom correction terms in (5.3)–(5.4) remain in every exact matrix. They will only be reduced modulo a justified power of $2$.

### 5.1 The atom gives an alternating unit modulo $4$

The turn10 atom formula is


$$
(\mathcal A_dw)_n=(-1)^n2^dU_d(n),
$$




$$
U_d(n)=
\sum_{h=0}^d
\binom dh\frac{d!}{(d-h)!}
\prod_{r=h}^{d-1}(2n+2r+1).
\tag{5.5}
$$



Because $16\mid d$, every $h\ge1$ term is divisible by $4$. The $h=0$ term is a product of $d$ consecutive odd numbers and is $1\pmod4$. Hence


$$
U_d(n)\equiv1\pmod4.
\tag{5.6}
$$



Also, $2^dd!\mid(\mathcal A_du)_n$, and $4\mid d!$. Since $c=u-w$,


$$
\boxed{
a_n\equiv-(-1)^n\pmod4.
}
\tag{5.7}
$$


This is where retaining the literal atom is essential.

### 5.2 A normalized contact parity sequence

Define the integers


$$
\theta_t=\frac{\Delta^tu_0}{2^tt!},
\qquad
\eta_t^{(m)}=\frac{\Delta^t\sigma_m}{2^{t+1}t!},
\qquad
\eta_t=\eta_t^{(0)}.
\tag{5.8}
$$


From $\sigma=2u+\Delta u$,


$$
\eta_t=\theta_t+(t+1)\theta_{t+1}.
\tag{5.9}
$$



The finite formula already available for $\theta_t$ gives, modulo $2$,


$$
\theta_t
\equiv
\sum_{h=0}^t\binom{t+h}{2h}.
\tag{5.10}
$$


For the integer sum on the right, the formal generating function is


$$
\begin{aligned}
\sum_{t\ge0}\sum_{h=0}^t
\binom{t+h}{2h}z^t
&=
\sum_{h\ge0}\frac{z^h}{(1-z)^{2h+1}}\\
&=\frac{1-z}{1-3z+z^2}.
\end{aligned}
$$


Over $\mathbb F_2$, this becomes


$$
\frac{1+z}{1+z+z^2}.
$$


Thus


$$
\boxed{
\theta_{t+2}\equiv\theta_{t+1}+\theta_t\pmod2,
\qquad
(\theta_0,\theta_1,\theta_2)\equiv(1,0,1).
}
\tag{5.11}
$$


The parity sequence has period $3$.

A finite Newton shift also gives


$$
\eta_t^{(m)}
=
\sum_{h=0}^m
\binom mh\,2^h(t+1)_h\,\eta_{t+h},
$$


so


$$
\boxed{
\eta_t^{(m)}\equiv\eta_t\pmod2.
}
\tag{5.12}
$$



### 5.3 The divided $\Delta\sigma$ column is odd

Put


$$
\widetilde b_n
=
\frac{(\mathcal A_d\Delta\sigma)_n}{2^{d+2}d!}.
\tag{5.13}
$$


The product-rule calculation from Section 4 gives


$$
\widetilde b_n
=
\sum_{h=0}^d
\binom dh Q_h(n)(d-h+1)
\eta_{d-h+1}^{(n+h)}.
\tag{5.14}
$$



Set $t=d-h$. Since $d$ is even, $\binom dt$ is even when $t$ is odd. Using (5.12),


$$
\widetilde b_n
\equiv
\sum_{t=0}^d\binom dt\eta_{t+1}
\pmod2.
\tag{5.15}
$$



Write $d=2D$. Lucas reduction and (5.9) give


$$
\sum_{t=0}^d\binom dt\eta_{t+1}
\equiv
\sum_{h=0}^{D}\binom Dh\theta_{2h+1}.
$$


The period-$3$ table in (5.11) shows


$$
\theta_{2h+1}\equiv\theta_{h+1}\pmod2.
$$


On this sequence, the shift operator $E$ satisfies $E^2=E+1$. Therefore


$$
\begin{aligned}
\sum_{h=0}^{D}\binom Dh\theta_{h+1}
&=((1+E)^D\theta)_1\\
&=(E^{2D}\theta)_1\\
&=\theta_{d+1}.
\end{aligned}
$$


Now $3\mid d+1=k$, so $\theta_{d+1}\equiv1\pmod2$. Consequently


$$
\widetilde b_n\equiv1\pmod2.
$$


Since


$$
b_n=\operatorname{odd}(d!)\,\widetilde b_n,
$$


we obtain


$$
\boxed{b_n\equiv1\pmod2.}
\tag{5.16}
$$



This evaluates the source sum in (5.14); it is not left as a named parity assumption.

### 5.4 The same column is constant modulo $4$ in its top row index

Using $d$ even,


$$
\Delta_n(\mathcal A_d\Delta\sigma)_n
=
\Delta^{d+1}(P_d\Delta\sigma)_n.
$$


The product rule and (4.3)–(4.4) show that this is divisible by


$$
2^{d+3}d!
$$


times an integer sum in which every term contains


$$
(d-h+1)(d-h+2).
$$


That product is even. Hence


$$
2^{d+4}d!
\mid
\Delta_n(\mathcal A_d\Delta\sigma)_n.
$$


After the actual normalization in (5.2),


$$
\boxed{
b_{n+1}-b_n\equiv0\pmod4.
}
\tag{5.17}
$$



Combining (5.7), (5.16), and (5.17), every two-row minor of the $d\times2$ source matrix


$$
A^{(2)}=[a\mid b]
\tag{5.18}
$$


is even. For the last two top rows,


$$
I_*=\{d-2,d-1\},
$$


the normalized atom changes sign modulo $4$, while $b$ remains the same odd residue. Therefore


$$
\boxed{
v_2\!\left(\det A^{(2)}[I_*,:]\right)=1.
}
\tag{5.19}
$$



---

## 6. Evaluation of the complete corrected paired cofactor

Three source evaluations now combine: a complete bottom forcing minor, the paid factorial adjugate minor, and the contact-atom minor from Section 5.

### 6.1 Complete bottom forcing minors

The residual bottom row $i$ corresponds to the original row


$$
m=d+i,\qquad 0\le i<d+2.
$$


Thus


$$
R(i,j)
=
\frac{\Lambda_k}{2(d+i+j)+1}
-\frac{\Lambda_k}{4}
b(d+i+j)(2(d+i+j))!.
\tag{6.1}
$$



The factorial correction in every entry has binary valuation at least


$$
\alpha_d-2.
$$


This is much larger than $3$ on the original domain. Therefore, modulo $8$, the complete matrix $R$ has the same entries as its displayed rational term. This reduction does not delete the factorial term from any exact matrix.

For two rows $i<i'$ and columns $j<j'$, the rational Cauchy determinant is exactly


$$
\frac{
4\Lambda_k^2(i'-i)(j'-j)
}{
\prod_{\substack{a\in\{i,i'\}\\b\in\{j,j'\}}}
(2(d+a+b)+1)
}.
\tag{6.2}
$$


Every denominator is odd. Hence


$$
\boxed{
4\mid\det R[\{i,i'\},\{j,j'\}],
}
\tag{6.3}
$$


and


$$
\boxed{
\frac{\det R[\{i,i'\},\{j,j'\}]}4
\equiv(i'-i)(j'-j)\pmod2.
}
\tag{6.4}
$$



In particular, for $I_*=\{d-2,d-1\}$,


$$
\frac{\det R[\{i,i'\},I_*]}4
\equiv i'-i\pmod2.
\tag{6.5}
$$



### 6.2 The relevant paid adjugate minor

Let


$$
e_n=v_2\!\left(\frac{h_d}{(2n)!}\right),
\qquad 0\le n<d.
$$


The final factorial diagonal entries have


$$
\boxed{
e_{d-1}=0,\qquad e_{d-2}=1,\qquad e_n\ge3\quad(n\le d-3).
}
\tag{6.6}
$$


Indeed, the first two gaps use $d-1$ odd and $v_2(d-2)=1$, consequences of $16\mid d$.

For any two-element row and column sets $I,J$,


$$
v_2(\det N_d[I,J])
\ge
\sum_{i\in I}e_i+\sum_{j\in J}e_j.
\tag{6.7}
$$


The minimum possible sum on each side is $1$, attained only by $I_*$.

For the principal pair, the adjugate minor identity gives


$$
\det\operatorname{adj}(K_d)[I_*,I_*]
=
\eta_d\det K_d[0,\ldots,d-3;\,0,\ldots,d-3].
\tag{6.8}
$$


Both factors on the right are odd by Section 3. Thus


$$
\boxed{
v_2(\det N_d[I_*,I_*])=2.
}
\tag{6.9}
$$


For every $(I,J)\ne(I_*,I_*)$,


$$
\boxed{
v_2(\det N_d[I,J])\ge4.
}
\tag{6.10}
$$



Also,


$$
N_d\equiv e_{d-1}e_{d-1}^{\,T}\pmod2,
\tag{6.11}
$$


where the $e_{d-1}$ on the right denotes the standard basis vector.

These facts use the factorial diagonal payments explicitly. Invertibility of $K_d$ alone would not imply them.

### 6.3 The retained bottom corrections cannot change the depth-five result

On the original domain,


$$
\alpha_d=\beta_d+5.
\tag{6.12}
$$


The correction in $x$ in (5.3) has valuation at least


$$
2\beta_d-d-1,
$$


because $c_m$ is even. The correction in $y$ in (5.4) has valuation at least


$$
2\beta_d-\alpha_d-2
=\alpha_d-12,
$$


because $4\mid\Delta\sigma_m$.

Since $d\ge32$ and $\alpha_d\ge d$, both corrections are divisible entrywise by $2^6$. Thus


$$
[x\mid y]\equiv RN_dA^{(2)}\pmod{2^6}.
\tag{6.13}
$$



### 6.4 Evaluated compound-product calculation

For a fixed pair of bottom rows $M=\{i,i'\}$, Cauchy–Binet gives the exact finite identity


$$
\det(RN_dA^{(2)})[M,:]
=
\sum_{\substack{|I|=2\\|J|=2}}
\det R[M,I]\,
\det N_d[I,J]\,
\det A^{(2)}[J,:].
\tag{6.14}
$$



Here the sum is fully evaluated at the needed binary depth:

* every $R$-minor is divisible by $2^2$;
* every $A^{(2)}$-minor is divisible by $2$;
* the term $I=J=I_*$ has the paid valuations $2,2,1$;
* every other term has valuation at least $2+4+1=7$.

By (5.19), (6.5), and (6.9), the distinguished term, divided by $2^5$, has residue $i'-i\pmod2$. The retained corrections in (6.13) contribute only multiples of $2^6$.

Therefore


$$
\boxed{
32\mid x_i y_{i'}-x_{i'}y_i,\qquad
\frac{x_i y_{i'}-x_{i'}y_i}{32}
\equiv i'-i\pmod2.
}
\tag{6.15}
$$



Finally, (6.1), (6.11), and the oddness of $a_{d-1}$ give


$$
x_i\equiv1\pmod2.
\tag{6.16}
$$



This proves (1.1).

### Theorem 6.1 — evaluated depth-five paired cofactor

Let


$$
\mathscr C_k^{(2)}
=
\gcd_{0\le i<i'<d+2}
|x_i y_{i'}-x_{i'}y_i|
$$


be the **actual all-prime two-column content**. Then, at every original index,


$$
\boxed{
v_2(\mathscr C_k^{(2)})=5.
}
\tag{6.17}
$$


Its odd part is not evaluated or assigned the value $1$.

For the first two residual rows,


$$
\Pi_k=
\begin{pmatrix}
x_0&y_0\\
x_1&y_1
\end{pmatrix},
\qquad
\boxed{\det\Pi_k=32\mu_k,\quad \mu_k\ \text{odd}.}
\tag{6.18}
$$



For any other residual row $i$, the interpolation coefficients satisfy


$$
(x_i,y_i)\Pi_k^{-1}\in\mathbb Z_{(2)}^2
$$


and


$$
\boxed{
(x_i,y_i)\Pi_k^{-1}
\equiv(1-i,i)\pmod2.
}
\tag{6.19}
$$



#### Payment in the interpolation

Each Cramer numerator is one of the two-column minors proved divisible by $32$. After that integer division, the only remaining denominator is $\mu_k$, which is proved odd. Formula (6.19) follows directly from (6.15).

This is a saturated row-basis statement at the full depth $5$, not merely a low-depth rank calculation on unnormalized entries. ∎

---

## 7. Transfer of the complete coefficient pair through the evaluated cofactor

### 7.1 A parity fact for the whole weighted pencil

Every column of $\mathcal Q_k(s)$, coefficientwise in $s$, is constant across its residual rows modulo $2$.

For the weighted contact-return column $r$, its exact form is


$$
\frac{\delta_k\Delta^r\sigma_{\mathrm{bot}}}
     {2^{\alpha_d+3}D_r}
+
RN_d
\frac{\mathcal A_d\Delta^r\sigma}
     {2^{\alpha_d+1}D_r}.
\tag{7.1}
$$


The first term is even, uniformly in $r$, by the payment in Section 4 and the stronger original-domain bound used in Section 6. The second is row-constant modulo $2$, because $R$ is entrywise odd and $N_d$ has the rank-one residue (6.11).

The same is true for the first contact column by (5.3). For the complete affine border, its old division was only by $4$, so its exact form is


$$
\frac{\delta_k(C_{0,\mathrm{border}}+sC_{1,\mathrm{border}})}4
+
RN_d(A_{0,\mathrm{border}}+sA_{1,\mathrm{border}}).
\tag{7.2}
$$


The first term is even; the second is again row-constant modulo $2$.

Thus this assertion uses the **whole constant border and the whole linear border**. It does not discard $\Lambda_kr$ or the literal $\Lambda_kw$.

### 7.2 Exact integer elimination

In $\mathcal Q_k(s)$, interchange the contact-return columns $r=0$ and $r=1$, so that $x,y$ are the first two columns. This is one column transposition. Partition the resulting matrix as


$$
\begin{pmatrix}
\Pi_k&U_k(s)\\
V_k&C_k(s)
\end{pmatrix}.
\tag{7.3}
$$


The top rows are the original residual rows $m=d,d+1$; the bottom rows are $m=d+2,\ldots,2d+1$. In particular, the original last row remains.

Define


$$
M_k^{(2)}
=
\frac{V_k\operatorname{adj}(\Pi_k)}{32}.
\tag{7.4}
$$


The division is integral by Theorem 6.1. Exactly,


$$
V_k\Pi_k^{-1}=\frac{M_k^{(2)}}{\mu_k}.
\tag{7.5}
$$



Set


$$
\mathcal V_k(s)=\mu_kC_k(s)-M_k^{(2)}U_k(s).
\tag{7.6}
$$


This is an integer pencil.

By (6.19), each row of $M_k^{(2)}/\mu_k$ has coefficient sum $1\pmod2$. Section 7.1 says that the two pivot rows and the corresponding bottom row have the same column values modulo $2$. Therefore


$$
\mathcal V_k(s)\equiv0\pmod2
$$


coefficientwise. We may consequently make the proved integer division


$$
\boxed{
\mathcal P_k(s)=\frac{\mathcal V_k(s)}2
\in\mathbb Z[s]^{d\times d}.
}
\tag{7.7}
$$


Only its last column depends on $s$, so


$$
\det\mathcal P_k(s)=P_{0,k}+P_{1,k}s.
\tag{7.8}
$$



### 7.3 Every scalar in the transfer

The block determinant in (7.3) equals $-\det\mathcal Q_k(s)$, owing to the one column transposition. Using $\det\Pi_k=32\mu_k$,


$$
-\det\mathcal Q_k(s)
=
32\mu_k^{1-d}\det\mathcal V_k(s)
=
2^{d+5}\mu_k^{1-d}\det\mathcal P_k(s).
$$


Together with (4.8), this gives


$$
\boxed{
\mu_k^{d-1}J_{i,k}
=
-2^{d+5}\mathfrak D_dP_{i,k},
\qquad i=0,1.
}
\tag{7.9}
$$



Taking actual all-prime gcds,


$$
\boxed{
|\mu_k|^{d-1}g_k^\sharp
=
2^{d+5}\mathfrak D_d\,g_k^{\mathrm{new}}.
}
\tag{7.10}
$$


Combining this with the complete turn10 transfer,


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_k|^{d-1}G_k
=
|f_k|\,2^{\lambda_d+d+5}\mathfrak D_d
\,g_k^{\mathrm{new}}.
}
\tag{7.11}
$$



This identity retains:

* the full $\Omega_k$;
* the full $\delta_k=\Lambda_k\eta_dh_d^2$;
* the full $f_k=(-\Lambda_k)^d\eta_d(\prod(2n)!)^2$;
* every old binary column payment;
* every new full factorial column payment $D_r=2^rr!$;
* the paired-cofactor payment $32$;
* the $d$ new row divisions by $2$;
* the actual odd interpolation factor $\mu_k$;
* the final actual all-prime gcd $g_k^{\mathrm{new}}$.

In particular, $\mu_k$ is not silently replaced by $1$, and $\mathfrak D_d$ is not replaced by its binary part in the all-prime formula.

### 7.4 The new exact remaining binary valuation

Since $\mu_k$ is odd,


$$
v_2(g_k^\sharp)
=
v_2(\mathfrak D_d)+d+5+\nu_k,
\tag{7.12}
$$


where


$$
\boxed{
\nu_k
=
\min\bigl(v_2(P_{0,k}),v_2(P_{1,k})\bigr).
}
\tag{7.13}
$$



Substituting (3.18) and (4.9) yields


$$
\boxed{
v_2(G_k)
=
d^2+4d+29+(d+4)s_2(d)
-3\sum_{n=0}^{d-1}s_2(n)
+\nu_k.
}
\tag{7.14}
$$


This is (1.3)–(1.4).

The coefficient pair $P_{0,k},P_{1,k}$ is a common rational scalar multiple of the original pair, with that scalar fully paid in (7.11). Hence its full primitive normalization is the original one:


$$
\boxed{
\frac{|P_{1,k}|}{g_k^{\mathrm{new}}}
=
\frac{|H_{1,k}|}{G_k}=q_k,
}
\tag{7.15}
$$




$$
\boxed{
\frac{|P_{0,k}+P_{1,k}(e+\pi)|}{g_k^{\mathrm{new}}}
=
\frac{|H_k(e+\pi)|}{G_k}=\ell_k>0.
}
\tag{7.16}
$$


These are normalization identities, not numerical evaluations of the primitive denominator.

---

## 8. Why this is a quantified advance, and what it does not prove

The turn10 identity


$$
v_2(G_k)=\kappa_k+\min(v_2(J_{0,k}),v_2(J_{1,k}))
$$


left the whole corrected paired depth unpaid.

The present argument proves, in the actual source columns,


$$
\boxed{
\min(v_2(J_{0,k}),v_2(J_{1,k}))
=
\left[d(d-1)-\sum_{r<d}s_2(r)\right]
+d+5+\nu_k.
}
\tag{8.1}
$$



More importantly, it identifies why the next elimination has no hidden binary denominator:

* the full weighted Newton divisions are proved integral;
* the actual two-column content has binary valuation exactly $5$;
* an explicit original-row paired cofactor attains that valuation;
* its Cramer numerators are divisible by the full $32$;
* its remaining denominator $\mu_k$ is proved odd;
* the interpolation residues are evaluated, not assumed;
* those residues justify the additional division of the complete residual pencil by $2$.

Thus this is not just a full determinant renamed and rescaled by an uncontrolled rational number. A specific nonunit cofactor has been evaluated and paid, and the unknown pencil has lost two common columns and two rows.

Nevertheless, (8.1) is **not an upper bound for $\nu_k$**. The new integer pencil can still have substantial common binary coefficient content. Nothing in the proof establishes that either $P_{0,k}$ or $P_{1,k}$ is a unit, or that their gcd is controlled by the displayed cofactor.

### Exact next binary obligation

The single remaining binary depth after this evaluated lemma is


$$
\nu_k=v_2\gcd(|P_{0,k}|,|P_{1,k}|),
$$


for the complete, explicit pencil in (7.3)–(7.8).

A concrete sufficient follow-on lemma is:

> **Residual original-domain upper-bound lemma — open.**  
> On an eventual tail of $k=9^{18+32u}$,
> 

$$
> \nu_k\le\frac{15}{4}k^2+O(k\log k).
>
$$



Because $\chi_k=k^2+O(k\log k)$, this would imply


$$
v_2(G_k)\le\frac{19}{4}k^2+O(k\log k).
$$



An exact, non-asymptotic version of the same target is to bound


$$
\nu_k\le \frac{19}{4}k^2-\chi_k+o(k^2).
$$


No such upper bound is claimed here.

---

## 9. Reused analytic gain and the sharp conditional odd payment

The first Laguerre/Jensen audit and its gain $4/85$ are established reuse. No trace enumeration, normalization audit, logarithm bracket, or later pairwise-convexity argument is repeated here.

The accepted same-$H$ consequence is


$$
\boxed{
\log|H_k(e+\pi)|
\ge
4k^2\log k+
\left(15\log2-\frac92\log3+\frac4{85}\right)k^2
+o(k^2).
}
\tag{9.1}
$$



For $k=3^s\in\mathcal K$, the accepted ternary contents are


$$
v_3(\mathscr L_k)=v_3(\mathscr R_k)=E_k,
\qquad
E_k=\frac{(k-2)(k-1-2s)}2.
\tag{9.2}
$$


They imply only


$$
\boxed{
E_k\le v_3(G_k)\le2E_k+s+1.
}
\tag{9.3}
$$


No equality for $v_3(G_k)$ is inferred.

Define


$$
W_k^{\mathrm{odd}}
=
3^{2k}\Lambda_k^k
\left(\prod_{j=0}^{k-1}\operatorname{odd}(j!)\right)^4,
$$




$$
B_p(k)=
k\bigl(2\mathbf1_{p=3}+v_p(\Lambda_k)\bigr)
+4\sum_{j=0}^{k-1}v_p(j!).
\tag{9.4}
$$


The already audited excess $B_3(k)-E_k$ permits the sharp certificate


$$
W_{k,\mathrm{sharp}}^{\mathrm{odd}}
=
W_k^{\mathrm{odd}}/3^{B_3(k)-E_k}.
\tag{9.5}
$$



The remaining odd hypotheses are distinct:

1. For every prime $5\le p\le6k-5$,
   

$$
v_p(\mathscr L_k),\,v_p(\mathscr R_k)\le B_p(k).
   \tag{9.6}
$$


2. For every prime $p>6k-5$,
   

$$
v_p(\mathscr L_k)=v_p(\mathscr R_k)=0.
   \tag{9.7}
$$



Both remain open. The local odd factors $\eta_d,\mu_k$, and the other exact factors in (7.11) do not prove these global odd-prime statements.

Conditionally on (9.6)–(9.7),


$$
\operatorname{odd}(G_k)
\mid
\Lambda_k\bigl(W_{k,\mathrm{sharp}}^{\mathrm{odd}}\bigr)^2.
\tag{9.8}
$$


If one also proves


$$
v_2(G_k)\le Ak^2+o(k^2),
$$


the reused sharp odd payment gives


$$
\log\ell_k
\ge
\left(
(19-A)\log2-\frac72\log3-\frac{506}{85}
\right)k^2+o(k^2).
\tag{9.9}
$$



The sufficient final-$G$ threshold is therefore


$$
\boxed{
A<
A_*+\frac{\log3}{\log2},
}
\tag{9.10}
$$


approximately $4.86435$, as already certified in the overlap gate.

For $A=19/4$, the exact positive margin is


$$
\frac{57}{4}\log2-\frac72\log3-\frac{506}{85}>0.
\tag{9.11}
$$


Its positivity follows from the already certified logarithm bounds; no new numerical bracket is needed.

Thus the open residual lemma in Section 8, together with the still-open other odd-prime descents, would force


$$
\ell_k\longrightarrow+\infty
\qquad(k\in\mathcal K).
$$


That would retire this compact producer as a source of primitive whole-error decay. It would **not** prove $e+\pi$ rational.

---

## 10. Boundary and normalization audit

The new proof preserves the original finite objects.

* The turn10 annihilator still acts only on the first $d$ rows.
* Its common forcing block still has all $d$ return columns.
* The new Newton transformation uses only the original contact-return shifts $0,\ldots,d-1$.
* The divided $r=1$ column is exactly $(\sigma_1-\sigma_0)/2$ after the preceding payments; no external contact column is introduced.
* The paired pivot uses original rows $m=d,d+1$.
* The remaining physical rows are $m=d+2,\ldots,2d+1$, including the original last row.
* The largest return index is still $3d=3k-3$.
* Its successor moment is still $3d+1=3k-2$.
* The largest factorial remains $(6k-4)!$.
* The rational forcing is canceled only in the already specified top rows. Its full bottom contribution remains in $R$.
* Both factorial terms remain in $F_k$, $B$, $R$, and all exact Schur corrections.
* The literal atom is retained in $c=u-w$, and its alternating residue is indispensable in (5.7) and (5.19).
* The entire border $\Lambda_k(r+sw)$ passes through the same transformations and the same row divisions.
* The actual all-prime contents and gcds remain in the exact transfer identities. No displayed lower divisor is substituted for $G_k$.

No result is transferred to the separate binary producer. Its domain, terminal condition $z_b=0$, complete corrected columns


$$
x=\frac12RA^{-1}f,
\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
$$


and complete return


$$
\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f
$$


remain separate, with their actual contents, primitive denominator, norm, and final all-prime gcd unchanged.

---

## 11. Finite arithmetic and computation scope

No tool execution has occurred. No new original-determinant scan, adjacent scan, factorial determinant scan, capped Smith computation, or Wishart enumeration is proposed.

The proof of Theorem 6.1 is symbolic and uniform on $\mathcal K$. No auxiliary matrix computation is indispensable.

The only small finite arithmetic underlying the new parity evaluation is already displayed in the proof:

* **Inputs:** the recurrence over $\mathbb F_2$
  

$$
\theta_0=1,\quad\theta_1=0,\quad
  \theta_{n+2}=\theta_{n+1}+\theta_n,
$$


  and
  

$$
\eta_n=\theta_n+(n+1)\theta_{n+1}.
$$


* **Expected verifiable output through index $5$:**
  

$$
(\theta_0,\ldots,\theta_5)=(1,0,1,1,0,1),
$$


  

$$
(\eta_0,\ldots,\eta_5)=(1,0,0,1,1,1).
$$


* **Uniform justification:** the recurrence, not the finite table alone, proves the period-$3$ assertion and the shift-operator identity used in Section 5.
* **Scope:** verification of the local parity calculation only. It supplies no upper bound for $\nu_k$.

The already completed $k=32,33$ data are not rerun and are not extrapolated to the original domain. They do not prove the $19/4$ final-$G$ target or the new $15/4$ residual target.

---

## 12. Proof-status ledger

| Statement | Status and scope |
|---|---|
| First Laguerre/Jensen gain $4/85$ | **Established reuse**; closed audit not repeated |
| Later pairwise-convexity improvement | **Not used** |
| Exact ternary contents and $B_3-E_k$ payment | **Established reuse** |
| Equality for $v_3(G_k)$ | **Not asserted**; only (9.3) retained |
| Turn10 rational annihilator, factorial pivot, and old simultaneous payments | **Reused proved construction**; different full audit remains pending |
| Full additional Newton divisions $D_r=2^rr!$ | **New proved integer divisions** |
| Normalized atom residue $a_n\equiv-(-1)^n\pmod4$ | **New evaluated refinement** on the original domain |
| Divided $\Delta\sigma$ source is odd and row-constant modulo $4$ | **New proved source evaluation** |
| Actual two-column content has $v_2=5$ | **New evaluated theorem**, every original index |
| Paid interpolation denominator $\mu_k$ is odd | **Proved**, not assumed |
| Interpolation residues depend on row parity as in (6.19) | **New proved congruence** |
| Complete residual pencil is even after the paid paired elimination | **Proved**, including the full affine border |
| Exact all-prime identity (7.11) | **Proved** |
| Explicit identity $v_2(G_k)=\chi_k+\nu_k$, $\chi_k=k^2+O(k\log k)$ | **Proved** |
| Residual bound $\nu_k\le(15/4)k^2+O(k\log k)$ | **Open** |
| Final bound $v_2(G_k)\le(19/4)k^2+o(k^2)$ | **Open** |
| Odd descent at $5\le p\le6k-5$ | **Open** |
| Large-prime exclusion at $p>6k-5$ | **Separate open obligation** |
| Primitive whole-error divergence | **Conditional** on the binary and remaining odd bounds |
| Actual primitive denominator | **Preserved exactly**, not numerically evaluated |
| Rationality or irrationality of $e+\pi$ | **Unresolved** |

## Final conclusion

The new result is an evaluated binary paired-cofactor lemma for the **actual corrected source pencil after the turn10 annihilator**. After the full additional Newton payments, the retained atom column and the divided $\Delta\sigma$ column have exact dyadic two-column content $2^5$, with an explicit attaining cofactor and fully paid, odd-denominator interpolation.

This yields the exact all-prime transfer


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_k|^{d-1}G_k
=
|f_k|\,2^{\lambda_d+d+5}\mathfrak D_d
\,g_k^{\mathrm{new}},
}
$$


and the explicitly evaluated binary payment


$$
\boxed{
v_2(G_k)
=
d^2+4d+29+(d+4)s_2(d)
-3\sum_{n<d}s_2(n)
+\nu_k.
}
$$



The single remaining binary bottleneck after this lemma is


$$
\boxed{
\nu_k=
v_2\gcd(|P_{0,k}|,|P_{1,k}|),
}
$$


for the complete integer pencil defined in Section 7. The concrete next target is


$$
\nu_k\le\frac{15}{4}k^2+O(k\log k)
$$


at the same infinite original indices. This bound has not been proved.

The remaining odd-prime descents are independent obligations. No additional bounded matrix computation is needed to verify the new lemma, and no finite scan can replace its outstanding uniform upper-bound obligation. The original all-prime gcd, actual primitive denominator, and nonzero whole evaluated error remain unchanged throughout.
