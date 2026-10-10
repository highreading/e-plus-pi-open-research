> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 Turn 27 — Independent audit of the full theta defect and a computed first effective quotient

## Executive summary

The original index family is retained:


$$
\boxed{k=9^{18+32u},\qquad u\ge 0,\qquad d=k-1,\qquad n=d+2.}
$$



This report has two parts.

### Audit conclusion

The substantial rank, corank, unit-block, source-excess, and linear-divisibility assertions in A2 Turn 16 **pass**, with the following necessary clarification:

> The constructive unit complement in the case $L\equiv1\pmod3$ uses the low-coordinate functionals **after applying the inverse triangular trace operator**. Raw low coefficients are not being asserted to give the stated triangular block without that coordinate change.

The clarification is a paid finite unit transformation, not an additional hypothesis.

In particular, under


$$
d=2L+\rho,\qquad L\text{ a power of }2,\qquad
\rho\ge4\text{ even},\qquad p\ge5,\qquad p+\rho\le L-2,
\tag{E.1}
$$


the actual normalized minimal-source matrix has corank


$$
\boxed{
\chi_p=
\begin{cases}
L-p-\rho+1,&L\equiv1\pmod3,\\
p+\rho+1,&L\equiv2\pmod3.
\end{cases}}
\tag{E.2}
$$


The last unpaired source row, the actual atom pivot, and all contact columns $0\le r\le d$ are essential in this calculation.

The whole linear lower divisor of A2 Turn 16 also passes. Its proof includes every source-jet pattern, both Cauchy–Binet index sets, all factorial competitors, the bottom atom, all-bottom terms, and every localized product count.

### New result

The report then computes the **entire first effective map**, not merely its values on the two previously known null directions, on the subfamily


$$
L\equiv2\pmod3.
$$



For every actual pole set $I$, with the minimal source-jet pattern at base $0$, let $S_p$ be the Schur block obtained from the constructive unit block of rank $n-\chi_p$. Then


$$
S_p\in2M_{\chi_p}(\mathbb Z_{(2)}).
$$



We derive an explicit polynomial model for $S_p/2\bmod2$, including the first Frobenius carry at degree $2L$. It yields


$$
\boxed{
\operatorname{rank}_{\mathbb F_2}(S_p/2)
=\rho+1+\operatorname{rank}_{\mathbb F_2}C_{L,\rho,p},
}
\tag{E.3}
$$


where $C_{L,\rho,p}$ is a fully specified matrix having only


$$
\left(\left\lfloor\frac p2\right\rfloor+(p\bmod2)\right)
\times \left\lfloor\frac p2\right\rfloor
$$


entries. More importantly, the calculation gives quantified rank information without assuming that this remaining matrix is nonsingular:


$$
\boxed{
\rho+1\le \operatorname{rank}(S_p/2)
\le \rho+1+\left\lfloor\frac p2\right\rfloor,
}
\tag{E.4}
$$


and hence


$$
\boxed{
\left\lceil\frac p2\right\rceil
\le \operatorname{corank}(S_p/2)\le p.
}
\tag{E.5}
$$



Thus at least $\rho+1$ of the first divided directions have now been proved to be units, while at least $\lceil p/2\rceil$ directions continue to the next level. This is a genuine effective-rank theorem for the full radical.

Using the already paid second lifts of the two distinguished source relations gives, for these actual minimal-source matrices,


$$
\boxed{
v_2(\det Z_{I,0})\ge
\chi_p+\left\lceil\frac p2\right\rceil+2.
}
\tag{E.6}
$$



The theorem is also propagated through **all** finite source-jet patterns and **all** $I,J$, giving the complete pure-Cauchy, product-atom lower payment


$$
\boxed{
\mathcal L_p+w(I,J)+
\chi_p+\left\lceil\frac p2\right\rceil-3.
}
\tag{E.7}
$$



These are effective-rank and lower-divisibility results. They do **not** prove a terminal-excess upper bound, do not evaluate the complete constant border, and do not establish the joint binary target.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$



---

# 1. Original objects, boundaries, and paid arithmetic

Throughout, $L$ denotes the dyadic number in $d=2L+\rho$. To avoid a collision with it, write


$$
\ell_d=\alpha-12
$$


for the bottom-correction exponent called $L_d$ in A2 Turn 16.

The original congruences are


$$
v_2(d)=4,\qquad d\equiv208\pmod{256},\qquad d\equiv2\pmod3.
$$


Indeed, for $t=18+32u$,


$$
v_2(9^t-1)=v_2(9-1)+v_2(t)=4.
$$



The sequences remain


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
\tag{1.1}
$$


Neither factorial term is omitted.

Set


$$
\Lambda_k=\operatorname{lcm}(1,3,\ldots,6k-5),\qquad T_m=\Lambda_k\tau_m.
$$



The finite boundaries are unchanged:

- original top source rows: $0\le a<d$;
- residual rows: $0\le i\le d+1$, representing physical row $d+i$;
- theta/contact columns: $0\le r\le d$;
- last physical row: $2d+1$;
- largest moment: $3d+1=3k-2$.

The terminal factorial and odd denominator are therefore


$$
\boxed{(6k-4)!,\qquad 6k-5.}
$$



## 1.1 Complete forcing and correction map

Retain


$$
P_d(x)=\prod_{h=0}^{d-1}(2x+2h+1),\qquad
\mathcal A_d y=\Delta^d(P_dy),
$$


and its actual determinant payment


$$
\Omega_k=\prod_{a=0}^{d-1}P_d(a).
$$



Write the forcing matrix as


$$
F_k=-\Lambda_kD_f\mathbf K_dD_f,\qquad
D_f=\operatorname{diag}((2a)!)_{a<d}.
$$


Here $\mathbf K_d$ is the actual forcing matrix, not a theta filter. The previously established oddness of its leading principal determinants is reused only at its established original-index scope.

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



The complete bottom forcing is


$$
\boxed{
R(i,j)=
\frac{\Lambda_k}{2(d+i+j)+1}
-\frac{\Lambda_k}{4}
\bigl(4(d+i+j)^2+6(d+i+j)+3\bigr)(2(d+i+j))!,
}
\tag{1.2}
$$


for $0\le i\le d+1$, $0\le j<d$. The identity


$$
(4t^2+6t+3)(2t)!=(2t+2)!+(2t)!
$$


makes explicit the retention of both factorial returns.

The finite correction map remains


$$
\mathscr T(y)=RN_d(\mathcal A_dy)_{\rm top}
+\frac{\delta_k}{4}y_{\rm bot}.
\tag{1.3}
$$



Every return divisor is the full integer


$$
D_r=2^rr!,
$$


including its odd part.

Let


$$
A=v_2(d!)=\alpha-d,\qquad
\gamma=\Lambda_k\det(\mathbf K_d)\operatorname{odd}(h_d)^2.
$$


Then


$$
v^{(r)}=\frac{\mathscr T(\Delta^ru)}{2^\alpha D_r},
\qquad
w_*=\frac{\mathscr T(w)}{2^d}
$$


satisfy the complete decomposition


$$
\boxed{
[w_*,v^{(0)},\ldots,v^{(d)}]
=
RN_d[\mathsf a_w,\mathsf v^{(0)},\ldots,\mathsf v^{(d)}]
+2^{\ell_d}\gamma[2^Aw,\theta_0,\ldots,\theta_d]_{\rm bot}.
}
\tag{1.4}
$$


The odd number $\gamma$ remains actual.

## 1.2 Both literal paired borders

The passed determinant-one paired transformation is retained:


$$
\widehat{\mathcal Q}_k(s)=
\left[
\varkappa_dv^{(d)}-w_*,
\ (v^{(r)}-a_rv^{(d)})_{r<d},
\ \mathfrak b_0+s\mathfrak c_kv^{(d)}
\right],
$$


where


$$
a_r=(-1)^{d-r}\frac{d!}{r!},\qquad
\varkappa_d=2^{\alpha-d}d!,\qquad
\mathfrak c_k=\Lambda_k2^\alpha d!,
$$


and


$$
\boxed{
\mathfrak b_0=\Lambda_k\mathscr T(r)
=\Lambda_k2^{-d}\mathscr T(\Delta^dr).
}
\tag{1.5}
$$


The right side contains both $-\Delta^df$ and $4\Delta^d\rho$.

Writing


$$
\det\mathcal Q_k(s)=I_{0,k}+I_{1,k}s,
$$


the exact identities are


$$
\boxed{
I_{1,k}=-\mathfrak c_kD_k,\qquad
D_k=\det[w_*,v^{(0)},\ldots,v^{(d)}],
}
\tag{1.6}
$$


and


$$
\boxed{
\begin{aligned}
I_{0,k}
={}&\varkappa_d
\det[v^{(0)},\ldots,v^{(d)},\mathfrak b_0]\\
&-\sum_{r=0}^d\frac{d!}{r!}
\det[w_*,v^{(0)},\ldots,\widehat{v^{(r)}},
\ldots,v^{(d)},\mathfrak b_0].
\end{aligned}}
\tag{1.7}
$$


No theta-only determinant is substituted for (1.7).

---

# 2. The actual normalized source matrices

The paid integer theta recurrence is


$$
\theta_0=1,\qquad \theta_1=0,\qquad
\theta_{r+1}=(2r+1)\theta_r+\theta_{r-1}.
\tag{2.1}
$$


At every nonnegative physical base,


$$
\theta_r^{(m)}
=\frac{\Delta^ru_m}{2^rr!}
=\sum_{\ell=0}^{m}
\binom m\ell 2^\ell(r+1)_\ell\theta_{r+\ell}.
\tag{2.2}
$$



Define


$$
B_j(r)=\binom{r+j}{r}\theta_{r+j},\qquad
K_b(z,r)=\sum_{t=0}^b\binom btB_{z+t}(r).
\tag{2.3}
$$


Thus


$$
K_{b+1}(z)=K_b(z)+K_b(z+1)
$$


as an exact integer identity.

Let


$$
R_j=(d+1)_j,\qquad o_d=d!/2^{v_2(d!)}.
$$


The full top normalization is


$$
T_j^{(a)}(r)
=
\frac{\Delta^j\mathsf v_a^{(r)}}{2^jR_j}
=
o_d\sum_{h=0}^d
\binom dhQ_h(a)
\binom{d-h+r+j}{r}
\theta_{d-h+r+j}^{(a+h)},
\tag{2.4}
$$


where


$$
Q_h(a)=\prod_{t=h}^{d-1}(2a+2t+1).
$$


Its admitted range is


$$
a+j\le d-1,\qquad 0\le r\le d.
$$



The actual atom is


$$
A_j^{(a)}
=
\frac{\Delta^j\mathsf a_w(a)}{2^j}
=
(-1)^{a+j}\sum_{h=0}^d
\binom{d+j}{h}\frac{d!}{(d-h)!}Q_h(a).
\tag{2.5}
$$



For an actual pole set $I$, $|I|=p$, put


$$
Q_I(i)=\prod_{t\in I}(2(d+i+t)+1),\qquad
J_\ell=\frac{\Delta^\ell Q_I(0)}{2^\ell\ell!}.
$$


The normalized bottom rows are


$$
V_z^I(r)=
\sum_{\ell=0}^p
J_\ell\binom{r+p+z-\ell}{r}
\theta_{r+p+z-\ell}^{(d+\ell)},
\quad 0\le z\le d+1-p.
\tag{2.6}
$$


This is the exact division of the original bottom jet by


$$
2^{p+z}(p+z)!.
$$


The physical base is $d+\ell$. Its largest raw moment is $3d+1$.

For a source pattern $U=\{j_0<\cdots<j_{p-1}\}$, with maximum $m$, the normalized complete matrix has top rows


$$
\left[
\frac{R_m}{R_j}\frac{A_j^{(a)}}{o_d},
\quad
\left(\frac{T_j^{(a)}(r)}{o_d}\right)_{r=0}^d
\right],
\qquad j\in U,
\tag{2.7}
$$


and bottom rows


$$
[0,V_z^I],\qquad 0\le z\le d+1-p.
\tag{2.8}
$$


The division by $o_d$ is an auxiliary odd-unit normalization in $\mathbb Z_{(2)}$; the determinant prefactor retains $o_d^p$.

For the minimal source pattern $U_0=\{0,\ldots,p-1\}$, denote this matrix at base $0$ by $Z_{I,0}$. Its parity is also the parity used for A2 Turn 16’s $Z_p$, whose admitted source base is $d-p$.

---

# Part I. Different full audit of the A2 Turn 16 rank and linear-divisor claims

# 3. The actual atom pivot and the finite contact span

Write


$$
D=d-p.
$$



Modulo $2$, the top contact row of order $j$ is $K_d(j)$, independently of the admitted top base and pole set. The bottom rows are


$$
K_p(0),\ldots,K_p(D+1).
$$



The last top atom entry, at $j=p-1$, is an actual odd unit. It is not replaced by the integer $1$ in the original matrix.

The atom support is different for the two parities of $p$.

- If $p$ is odd, $d+p-1$ is even. All atom entries except the last are even.
- If $p$ is even, the last two atom entries are odd, and all earlier ones are even.

Consequently, after using the last row as the atom pivot, the parity contact rows from the top are



$$
\begin{cases}
K_d(0),\ldots,K_d(p-2),&p\text{ odd},\\
K_d(0),\ldots,K_d(p-3),\ K_d(p-2)+K_d(p-1),&p\text{ even}.
\end{cases}
\tag{3.1}
$$



This verifies the actual pivot and retains the last unpaired source row.

Now use the exact filter relation


$$
K_d(j)=(1+E)^D K_p(j).
\tag{3.2}
$$


The leading coefficient of $E^j(1+E)^D$ is $1$. Therefore a triangular reduction against the existing bottom orders gives the contact row spaces


$$
\boxed{
\begin{cases}
\operatorname{span}\{K_p(0),\ldots,K_p(d-2)\},&p\text{ odd},\\
\operatorname{span}\{K_p(0),\ldots,K_p(d-3),
K_p(d-2)+K_p(d-1)\},&p\text{ even}.
\end{cases}}
\tag{3.3}
$$


In the even case, $D$ is even, so the last two unreduced coefficients are both $1$.

There are $d-1$ formal rows in either display. The two relations lost in reaching this formal row space are precisely the two source relations of orders $0$ and $1$. No bottom order above $D+1$ has been used.

**Audit verdict: PASS.**

---

# 4. The trace polynomial and its finite unit transformation

Work first over


$$
\mathbb F_4=\mathbb F_2(\omega),\qquad \omega^2+\omega+1=0.
$$


The parity recurrence gives


$$
\theta_r=\operatorname{Tr}(\omega^{r+2}).
$$



Put


$$
a=1+\omega Y,\qquad b=1+\omega^2Y,\qquad
S=ab=1+Y+Y^2.
$$


A direct generating-function calculation gives


$$
\sum_{r\ge0}K_p(j,r)Y^r
=
\operatorname{Tr}\left(
\omega^{j+2+2p}\frac{b^p}{a^{p+j+1}}
\right).
\tag{4.1}
$$



Let


$$
H=4L,\qquad q=2L-p.
$$


The hypotheses (E.1) imply


$$
d+2p=2L+\rho+2p
\le4L-\rho-4<H.
\tag{4.2}
$$


In particular all exponents below are nonnegative.

Multiplication of the contact generating polynomials by $S^{-p}$, truncated modulo $Y^{d+1}$, is a finite unit column operation. Its matrix is triangular with diagonal $1$. Its inverse is multiplication by $S^p$, with the same truncation. Thus neither operation removes a content factor or adds a contact column.

Since $a^H\equiv1\pmod{Y^H}$, the transformed row is


$$
P_s(Y)=
\operatorname{Tr}\bigl(\omega^{H+1}(Y+\omega^2)^s\bigr),
\qquad
s=H-2p-j-1=2q-j-1,
\tag{4.3}
$$


modulo $Y^{d+1}$.

The truncation includes the coefficient of $Y^d$, corresponding to the actual contact terminal $r=d$. The higher-degree polynomial in (4.3) is only a representation of these $d+1$ coefficients.

**Audit verdict: PASS.** In particular, $S^p$ is used as a unit of the finite coefficient ring, not as an unpaid polynomial divisor.

---

# 5. Audit when $L\equiv2\pmod3$

Here $H\equiv2\pmod3$, so


$$
P_s=F_s(S),\qquad
F_s=x^s+(x+1)^s,\qquad x=Y+\omega^2,
$$


with $x(x+1)=S$.

The recurrence


$$
F_0=0,\quad F_1=1,\quad F_{s+2}=F_{s+1}+SF_s
$$


gives


$$
F_s(S)=\sum_j\binom{s-j-1}{j}S^j.
\tag{5.1}
$$



All rows in (3.3) have $s\le2q-1$, hence degree in $S$ below $q$.

The $q$ rows


$$
F_q,\ldots,F_{2q-1}
$$


form a basis of the degree-$<q$ polynomial space. Indeed, after taking successive forward differences in the row index, the coefficient in difference row $i$, column $j$, is


$$
\binom{q-j-1}{j-i}.
$$


It vanishes for $j<i$, and equals $1$ for $j=i$.

These rows are contained in the ordinary part of both row lists in (3.3). In the even case this uses $q\le d-2$, which follows immediately from $p+\rho\ge2$.

Finally, substitution


$$
S=1+Y+Y^2
$$


is injective after truncation at $Y^{d+1}$ on degree-$<q$ polynomials. If a nonzero polynomial has multiplicity $t$ at $S=1$, its substituted polynomial has $Y$-adic order $t$, and $t<q\le d$.

Thus


$$
\operatorname{rank}(\text{contact part})=q,
$$


and


$$
\boxed{\operatorname{rank}\overline Z_p=q+1,\qquad
\chi_p=p+\rho+1.}
\tag{5.2}
$$



The forward-difference basis, followed by the unit substitutions $S\mapsto1+T$, $T=Y+Y^2$, gives an actual unit complement. Together with the actual odd atom pivot, it constructs a unit block of size $q+1$.

**Audit verdict: PASS, for both parities of $p$.**

## 5.1 An alternative exact kernel description

This description will also be used in the new first-lift calculation.

Set


$$
A_0=2(L-p)-\rho+1.
\tag{5.3}
$$


This is odd. The formal polynomial source spaces corresponding to (3.3) are


$$
\begin{cases}
\operatorname{span}\{X^{A_0},\ldots,X^{2q-1}\},&p\text{ odd},\\
\operatorname{span}\{X^{A_0+1},\ldots,X^{2q-1},
X^{A_0}+X^{A_0-1}\},&p\text{ even}.
\end{cases}
\tag{5.4}
$$



The trace map is


$$
f(X)\longmapsto f(x)+f(x+1).
$$


Its kernel consists exactly of the translation-invariant polynomials


$$
f(X)=G(X^2+X).
$$



Therefore the contact kernel is represented by



$$
\boxed{
\begin{cases}
G(S)\in S^{A_0}\mathbb F_2[S],\quad \deg G<q,
&p\text{ odd},\\[1mm]
G(S)=S^{A_0-1}\{c(1+S)+S^2J(S)\},\quad \deg G<q,
&p\text{ even}.
\end{cases}}
\tag{5.5}
$$



In either case its dimension is


$$
q-A_0=p+\rho-1=\chi_p-2.
$$


The other two null directions are the two formal source relations from Section 3.

This independently checks the kernel dimension, including the even-$p$ final combined row.

---

# 6. Audit when $L\equiv1\pmod3$

Here


$$
P_s=\mathcal U(Y^s),\qquad
\mathcal Uf(Y)=
\omega^2f(Y+\omega^2)+\omega f(Y+\omega).
\tag{6.1}
$$


The leading coefficient is preserved, so $\mathcal U$ is triangular and invertible on every finite degree range.

Put


$$
h=2L,\qquad \tau=2(L-p),\qquad A_0=\tau-\rho+1.
$$


The high rows satisfy


$$
P_{h+t}=Y^hP_t+F_t(S),\qquad 0\le t<\tau.
\tag{6.2}
$$



The low rows are



$$
\begin{cases}
P_{A_0},\ldots,P_{h-1},&p\text{ odd},\\
P_{A_0+1},\ldots,P_{h-1},P_{A_0}+P_{A_0-1},&p\text{ even}.
\end{cases}
\tag{6.3}
$$


They have rank $h-A_0$.

For a high-row combination represented by $f(Y)$, $\deg f<\tau$, its low part is


$$
\mathcal U\bigl(f(Y+1)+f(Y)\bigr).
$$


Let


$$
\Delta_1f=f(Y+1)+f(Y).
$$



Vanishing modulo the low space requires divisibility of $\Delta_1f$ by $Y^{A_0}$ in the odd case, and by $Y^{A_0-1}$, together with the final coefficient condition, in the even case.

But $\Delta_1f$ is translation-invariant. If it is divisible by $Y^a$, it is also divisible by $(Y+1)^a$. Moreover,


$$
\deg\Delta_1f\le\tau-2.
$$


Since


$$
\tau\ge2\rho+4,
$$


even the weaker divisibility by $Y^{A_0-1}(Y+1)^{A_0-1}$ has degree greater than $\tau-2$. Hence


$$
\Delta_1f=0.
$$



Thus


$$
f(Y)=g(T),\qquad T=Y^2+Y.
$$


For these polynomials,


$$
\mathcal Uf=g(T+1).
$$


The high coefficients through the physical terminal $Y^{h+\rho}=Y^d$ vanish exactly when


$$
(X+1)^{\rho+1}\mid g(X).
$$


Because $\deg g\le L-p-1$, the high-row kernel dimension is


$$
L-p-\rho-1.
$$


Consequently


$$
\operatorname{rank}(\text{contact part})
=(d-1)-(L-p-\rho-1)=L+p+2\rho,
$$


and


$$
\boxed{\chi_p=L-p-\rho+1.}
\tag{6.4}
$$



## 6.1 Constructive unit complement

Write $m=L-p$. In the high-row polynomial space, take


$$
YT^j,\quad 0\le j<m,
$$


and


$$
T^j,\quad 0\le j\le\rho,
$$


as a complement to the kernel


$$
(T+1)^{\rho+1}T^j,\quad
0\le j\le m-\rho-2.
$$



For $YT^j$,


$$
\Delta_1(YT^j)=T^j.
$$


After applying $\mathcal U^{-1}$ to the low coordinates, the first $m$ coefficient functionals give a unit-triangular block, because $T^j$ has lowest degree $j$.

For $T^j$, the low part vanishes and the high image is $(T+1)^j$. Its first $\rho+1$ coefficients give another unit block.

The low rows in (6.3), these high complement rows, and the atom pivot therefore construct a unit block of size $n-\chi_p$.

**Audit verdict: PASS with the explicit coordinate clarification stated above.** The clarification supplies the exact unit transformation required to interpret the claimed low triangular block.

---

# 7. Audit of the Schur quotient and the source-excess tradeoff

The preceding constructions give actual finite binary row and column bases. Lift their elementary operations integrally. After these operations,


$$
Z_p\sim
\begin{pmatrix}A&B\\ C&D_0\end{pmatrix},
\qquad \det A\text{ odd},
$$


where $A$ has size $n-\chi_p$. The Schur block is


$$
S_p=D_0-CA^{-1}B\in2M_{\chi_p}(\mathbb Z_{(2)}),
$$


and


$$
\boxed{
\det Z_p=\pm\det A\cdot2^{\chi_p}\det(S_p/2).
}
\tag{7.1}
$$



The hypotheses imply


$$
3\le\chi_p\le L-1.
$$


Thus a unit $(n-2)$-minor does not exist in this window.

The two paid first source relations are independent null directions. Their first divided residues lie in the leading row space, so the first effective map vanishes on them. Hence


$$
v_2(\det Z_p)\ge\chi_p+2.
$$



**Audit verdict: PASS.** This is a lower bound, not an exact valuation.

## 7.1 General source patterns

Compare an arbitrary source pattern $U$ with $U_0$. Let


$$
t=|U\setminus U_0|.
$$


After matching common source orders, the contact part changes in at most $t$ rows. The atom column can change once more because its normalization uses the actual maximum order.

Thus


$$
\operatorname{corank}\overline Z_U
\ge \max(0,\chi_p-t-1).
$$


The source excess


$$
\sigma(U)=\sum_{a=0}^{p-1}(j_a-a)
$$


satisfies $\sigma(U)\ge t$. Therefore


$$
\sigma(U)+\operatorname{corank}\overline Z_U\ge\chi_p-1.
\tag{7.2}
$$



The bottom parity is independent of the actual pole set $I$, and the finite Newton coefficients for the actual source set $J$ are integers. Hence the bound applies to every $I,J,U$, not only to minimal sets.

**Audit verdict: PASS.**

---

# 8. Audit of the whole linear divisor

The paid nominal cost is


$$
\mathcal L_p
=(n-p)\ell_d+S_p+S_n+2E_p+B_p,
\tag{8.1}
$$


where


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


Let


$$
m_\star=\min_{1\le p\le d}\mathcal L_p.
$$



The exact convexity formulas already audited in FULL26 are reused:


$$
\mathcal L_{p+1}-\mathcal L_p
=
8p-2d+5-s_2(p)+2s_2(d-p-1)-s_2(d+p-1),
\tag{8.2}
$$


and the successive increments increase by at least $4$. Consequently all counts through excess $B$ satisfy


$$
|p-p_\star|\le T_B:=\frac{1+\sqrt{1+2B}}2,
\qquad
|p_\star-d/4|\le b_d+2.
\tag{8.3}
$$



Both possible adjacent minimizers are retained.

## 8.1 All factorial competitors, including $p=v$

For $v\ge1$ factorial columns and $a=p-v$ Cauchy columns, the paid global comparison is


$$
\mathcal F(p,v)\ge
\mathcal L_a+
v(4a+3v-3b_d-2).
\tag{8.4}
$$


It includes $a=0$, hence all-factorial terms.

This comparison gives a direct finite-window exclusion.

If $p\ge b_d+2$, its extra factor is positive:


$$
4a+3v-3b_d-2=4p-v-3b_d-2\ge3p-3b_d-2>0.
$$


If such a term were admitted through $m_\star+B$, then $\mathcal L_a\le m_\star+B$. The all-bottom cost $\mathcal L_0$ is already too large, so $a\ge1$ and (8.3) applies to $a$. Therefore


$$
4a+3v-3b_d-2
\ge d-7b_d-7-4T_B.
$$


For $B\le d/8$, this is greater than $B$ at all sufficiently large original indices, excluding $v\ge1$.

If $p\le b_d+1$, the separately paid small-$p$ estimate gives


$$
\mathcal F(p,v)-m_\star
\ge2d-3b_d^2-17b_d-21>d/8.
$$


Thus no small-$p$ exception remains.

This verifies the required whole-window exclusion without relying on a positive local margin at an unlocalized product count.

## 8.2 Bottom atom and $p=0$

For a bottom atom, the additional source payment is


$$
b_p^{\rm at}=v_2((d+1)_{p-1})
\ge p-1-b_d.
$$


Throughout the localized strip for $B\le d/8$,


$$
b_p^{\rm at}
\ge d/4-2b_d-3-T_B>B
$$


at sufficiently large original indices.

The physical atom factor $2^A$ still pays the missing bottom factorial valuation, because


$$
v_2(j!)\le v_2((d+1)!)=A,\qquad j\le d+1.
$$


Odd factorial denominators are local units, not newly claimed integer contents.

At $p=0$,


$$
\mathcal L_0-\mathcal L_1=\ell_d,
$$


which is much greater than $d/8$ on the original family.

Hence the entire first-$d/8$ window consists only of pure-Cauchy, product-atom aggregates.

## 8.3 Validation on the same infinite original interval

On


$$
\frac98\,2^{a_k}<k<\frac76\,2^{a_k},
\qquad L=2^{a_k-1},
$$


write $d=2L+\rho$. Then


$$
L/4-1<\rho<L/3-1,
$$


and $\rho$ is divisible by $16$.

Let


$$
E=b_d+2+T_B.
$$


For $B\le d/8$, every relevant count satisfies


$$
|p-d/4|\le E.
$$


Thus


$$
L-p-\rho>L/12-E.
$$


This proves the rank-window hypotheses with linear slack.

For $L\equiv1\pmod3$, take $B=\lfloor L/16\rfloor$. Then


$$
\chi_p-1=L-p-\rho>B
$$


once $L/48>E$.

For $L\equiv2\pmod3$, take $B=\lfloor d/8\rfloor$. Then


$$
\chi_p-1=p+\rho>B
$$


with an even larger linear margin.

All these elementary inequalities hold, for example, once $L\ge2^{20}$; the original indices are far beyond this threshold.

By (7.2), every actual $I,J,U$ aggregate is beyond $m_\star+B$. The factorial, bottom-atom, and all-bottom exclusions cover all other classes. Therefore


$$
\boxed{
v_2(D_k)\ge
\begin{cases}
m_\star+\lfloor L/16\rfloor+1,&L\equiv1\pmod3,\\
m_\star+\lfloor d/8\rfloor+1,&L\equiv2\pmod3.
\end{cases}}
\tag{8.5}
$$



The interval contains infinitely many original indices. Indeed,


$$
\log_2k=(18+32u)\log_2 9,
$$


and $32\log_2 9$ is irrational. Rotation modulo $2$ supplies infinitely many hits in either parity class of $a_k$, without changing the original index domain.

**Audit verdict: PASS.**

In particular, on this interval an exact valuation $m_\star+6$ is impossible for sufficiently large original $d$. FULL26’s possible-next-digit identity remains a valid reduction, but its right side must vanish there.

---

# Part II. A computed first effective quotient for the full radical

# 9. Scope and construction of the actual unit block

For the remainder of the new calculation assume


$$
L\equiv2\pmod3
$$


and the rank-window hypotheses (E.1).

We use the constructive rank-$(q+1)$ block from Section 5:

1. the actual last top atom pivot;
2. contact rows representing $F_q,\ldots,F_{2q-1}$;
3. their forward-difference basis;
4. the first $q$ coefficient functionals after the finite unit coordinate changes.

Choose elementary integral lifts of these finite binary operations. The actual Schur block is therefore the block in (7.1), with


$$
\chi_p=p+\rho+1.
$$



We compute its first divided reduction through the intrinsic map


$$
\beta_Z:\ker(\overline Z^{\,T})\longrightarrow
\mathbb F_2^{\,n}/\operatorname{rowspan}(\overline Z),
$$




$$
\beta_Z(\lambda)=
\left[\frac{\widetilde\lambda^{\,T}Z}{2}\right]\pmod2.
\tag{9.1}
$$


Changing an integer lift $\widetilde\lambda$ by $2h$ changes the result by $h^T\overline Z$, so the quotient class is well-defined.

After complete leading binary elimination, (9.1) is exactly $S_p/2\bmod2$. Thus computing this map computes the full first Schur quotient, independently of arbitrary lift choices.

The leading row space is


$$
\operatorname{span}\{[1,0]\}
\oplus
\{[0,F(S)]:\deg F<q\}.
\tag{9.2}
$$


In particular, the atom coordinate is killed by a proved actual unit pivot. Atom carries are not discarded: they lie in the explicitly eliminated unit coordinate.

---

# 10. Full source information used before division

Write, as full integers,


$$
X_1=\sum_{t\in I}(d+t),\qquad
X_2=\sum_{s<t,\ s,t\in I}(d+s)(d+t),\qquad C_j=\binom pj,
$$




$$
b_I=X_1+p+C_2.
$$


The passed modulo-$8$ source laws are


$$
\frac{T_j^{(a)}}{o_d}
\equiv K_d(j)+2a(j+1)K_d(j+1)\pmod8,
\tag{10.1}
$$




$$
A_j^{(a)}\equiv(-1)^{a+j}\pmod8,
\tag{10.2}
$$


and


$$
V_z^I\equiv K_p(z)+2U_z+4W_z\pmod8,
\tag{10.3}
$$


where


$$
U_z=(pz+b_I)K_{p-1}(z+1)+C_2K_{p-2}(z+2),
\tag{10.4}
$$




$$
\begin{aligned}
W_z={}&[X_2+(p+z)\mu]K_{p-2}(z+2)\\
&+[\varphi+(p+z)\nu]K_{p-3}(z+2)
+C_4K_{p-4}(z+2),
\end{aligned}
\tag{10.5}
$$


with


$$
\mu=X_1(p-1)+C_2,\quad
\nu=C_2(p-2),\quad
\varphi=X_1\binom{p-1}{2}+C_3.
$$



These coefficients are fixed as integers before division. For the first effective map, modulo $4$ is sufficient, but the full integer lift (10.4), rather than a prematurely reduced binary coefficient list, is used.

The completed FULL26 two-row second lifts are reused later, only for their two already paid directions.

---

# 11. A modulo-$4$ lift of the entire theta kernel

The missing ingredient for the full first quotient is the modulo-$4$ lift of all theta rows, not only two source rows.

Work in


$$
\mathcal O=\mathbb Z_{(2)}[\zeta],\qquad \zeta^2+\zeta+1=0,
$$


with conjugation $\zeta\leftrightarrow\zeta^2$.

Put


$$
c=\zeta-1.
$$


Then


$$
\boxed{
\theta_m\equiv
(-1)^{\binom{m+1}{2}}\operatorname{Tr}(c\zeta^m)
\pmod4.
}
\tag{11.1}
$$



To verify this, the trace sequence satisfies


$$
h_{m+1}+h_m+h_{m-1}=0.
$$


The sign ratio in (11.1), together with


$$
2m+1\equiv(-1)^m\pmod4,
$$


gives the original theta recurrence modulo $4$. The initial values are


$$
\operatorname{Tr}(\zeta-1)=-3\equiv1,\qquad
\operatorname{Tr}((\zeta-1)\zeta)=0.
$$



Consequently, with $a=1-\zeta Y$,


$$
\sum_{m\ge0}\theta_mY^m
\equiv
\operatorname{Tr}\left[
c\left(a^{-1}+2a^{-2}-2a^{-3}\right)
\right]\pmod4.
\tag{11.2}
$$


Taking the appropriate Hasse coefficient gives


$$
\boxed{
B_j(Y)\equiv
\operatorname{Tr}\left[
c\zeta^j
\left(
a^{-j-1}
+2(j+1)a^{-j-2}
-2\binom{j+2}{2}a^{-j-3}
\right)
\right]\pmod4.
}
\tag{11.3}
$$



This formula evaluates all first theta carries.

## 11.1 The indispensable Frobenius carry

Let $H=4L$ and $h=2L$. Since $H$ is dyadic,


$$
\boxed{
(1-\zeta Y)^H
\equiv1+2\zeta^hY^h
\pmod{4,\ Y^{d+1}}.
}
\tag{11.4}
$$


The coefficient at $Y^h$ is the unique interior binomial coefficient visible modulo $4$. It cannot be omitted: $h=2L\le d$.

This carry will produce the terminal term


$$
Y^{2L}G(S)
$$


in the full effective map. Omitting it would give the wrong first quotient.

---

# 12. Evaluation of the full first effective map

Let


$$
N=2q-1,\qquad s=N-j.
$$


After multiplication by the actual unit $S^{-p}$, the leading lifted trace polynomial has, up to an odd row unit, the form


$$
H_{s-1}(1+2Y,S),
$$


where $H_m(t,S)$ is the complete symmetric polynomial in two variables whose sum is $t$ and product is $S$.

Its first non-invariant contribution is


$$
Y(s-1)F_s(S).
\tag{12.1}
$$


This follows from


$$
H_{s-1}(1+2Y,S)
\equiv H_{s-1}(1,S)+2Y\partial_tH_{s-1}(1,S)\pmod4
$$


and weighted homogeneity:


$$
\partial_tH_{s-1}(1,S)\equiv(s-1)F_s(S)\pmod2.
$$



Convolving (11.3) with the full integer binomial coefficients $\binom pt$ gives the remaining first-order terms. Before reduction, their coefficients are


$$
j+1,\quad \binom{j+2}{2},\quad
p,\quad (j+2)p,\quad \binom p2.
$$


After the displayed factor $2$ has been removed, one may use


$$
j+1\equiv s,\qquad
\binom{j+2}{2}\equiv\binom s2+p\pmod2.
$$



Writing $x=Y+\omega^2$, so $x(x+1)=S$, the coefficient of $Y$, modulo polynomial terms of degree $<q$ in $S$, is


$$
\begin{aligned}
G_s^{\rm eff}={}&
(s+1)F_s+sF_{s-1}
+\left(\binom s2+p\right)F_{s-2}\\
&+\frac pS F_s
+\frac{p(s+1)}S F_{s-1}
+\frac{C_2}{S^2}F_s+\frac pS F_{s+1}.
\end{aligned}
\tag{12.2}
$$



For a relation


$$
f(X)=G(X^2+X),
$$


summing (12.2) simplifies exactly. The identities


$$
F_s'=sF_{s-1},\qquad
\binom s2F_{s-2}=F_s'+F_s^{[2]}
$$


and $\sum c_sF_s=0$ eliminate the derivative terms. Also,


$$
\sum c_s(s+1)F_s=G'(S),
$$


because it is the trace of $Xf'(X)+f(X)$, and


$$
\sum c_sF_{s-1}=\frac{G(S)}S.
$$


Therefore the non-invariant part is


$$
Y\left(G'(S)+p\frac{G(S)}S\right).
\tag{12.3}
$$



The invariant rational terms have only removable poles at $S=0$. Indeed, every $G$ in (5.5) is divisible by a high power of $S$; the remaining numerators vanish at $S=0$, and their polynomial quotients have degree $<q$. They lie in the proved leading row space.

Finally, (11.4) contributes


$$
Y^h\operatorname{Tr}(\omega f(x))=Y^hG(S),
$$


since $\operatorname{Tr}(\omega)=1$.

We have therefore evaluated the theta part of every null direction.

## 12.1 Why all actual pole corrections vanish in this quotient

The transformed first pole correction is


$$
(pz+b_I)S^{-1}F_{s+1}+C_2S^{-2}F_{s+2},
\qquad s=N-z.
$$


Modulo the polynomial space of degree $<q$, it equals


$$
C_2S^{-2}
+\bigl((p+C_2)z+b_I+C_2\bigr)S^{-1}.
\tag{12.4}
$$



Let $\lambda_z$ be the bottom coefficients of a complete null relation. Its formal contact polynomial is


$$
g(E)=\sum_z\lambda_zE^z+(1+E)^D a(E)
=E^Nf(1/E).
\tag{12.5}
$$


Since $f=G(X^2+X)$ vanishes to order at least $2$ at $X=1$, and $D\ge2$,


$$
\sum_z\lambda_z=g(1)=0,\qquad
\sum_z z\lambda_z=g'(1)=0.
$$


Hence the complete sum of (12.4) is zero.

This proves independence of the first effective map from the actual pole set $I$. It is not an assumption that nonminimal poles have the same higher residues.

The same argument covers the two formal source relations, for which $g(E)=0$.

## 12.2 Top-base and atom carries

The top-base term in (10.1) is a combination of transformed $F_s$ of degree $<q$, so it lies in the leading row space.

The actual atom coordinate is removed by the certified odd pivot in (9.2). Thus any first divided atom carry is accounted for in that unit coordinate.

All integer basis-lift carries from the polynomial $H_{s-1}(1,S)$ are polynomials of degree $<q$ in $S$; after division they again lie in the same leading row space. This explains precisely why no first-lift carry has been silently dropped.

### Theorem 12.1 — full first effective map

On the whole $\chi_p$-dimensional null space:

- the two formal source relations map to zero;
- the remaining $\chi_p-2$ directions are the $G$'s in (5.5), and


$$
\boxed{
\beta_Z(G)=
\left[
Y\left(G'(S)+p\frac{G(S)}S\right)+Y^{2L}G(S)
\right]
}
\tag{12.6}
$$


in


$$
\mathbb F_2[Y]/(Y^{d+1})
\big/
\{F(S):\deg F<q\}.
$$



This is the first divided Schur matrix, expressed in explicit finite coordinates.

---

# 13. Rank and kernel of the computed map

Put


$$
\rho=2r,\qquad p=2P+\varepsilon,\qquad
\varepsilon\in\{0,1\},
$$




$$
Q=L-P,\qquad a=L-p-r.
\tag{13.1}
$$


Then


$$
q=2Q-\varepsilon,\qquad A_0=2a+1.
$$



Use the finite unit local coordinate


$$
T=Y+Y^2,\qquad S=1+T.
$$


Over $\mathbb F_2$, its inverse is


$$
Y=\Phi(T):=\sum_{j\ge0}T^{2^j},
$$


truncated at degree $d$. This is only a finite triangular coordinate change. An integral lift is supplied by the usual integral formal inverse of $Y+Y^2$.

Also


$$
Y^{2L}\equiv T^{2L}\pmod{T^{d+1}}.
$$



The cokernel coordinates are now exactly the coefficients of


$$
T^q,\ldots,T^d.
$$



## 13.1 Even $p$

For $p=2P$, the kernel polynomials in (5.5) can be written uniquely


$$
G(S)=U(S)^2+S V(S)^2,
$$


where


$$
\deg U,\deg V<Q,\qquad
S^a\mid U,V,
$$


and the coefficients of $S^a$ in $U,V$ are equal.

Set


$$
u(T)=U(1+T),\qquad v(T)=V(1+T),
$$




$$
W(T)=\Phi(T)v(T)+T^L(u(T)+v(T)).
$$


Equation (12.6), after removing terms of degree below $q$, becomes


$$
\boxed{\beta_Z(G)=
[W(T)^2+T^{2L+1}v(T)^2].}
\tag{13.2}
$$



Because the second term has odd exponents and the first has even exponents,


$$
\boxed{
\beta_Z(G)=0
\iff
\begin{cases}
T^r\mid v(T),\\
[T^Q,\ldots,T^{L+r}]\,W(T)=0.
\end{cases}}
\tag{13.3}
$$



The first condition leaves


$$
V(S)=S^a(S+1)^r R(S),\qquad \deg R<P.
$$


The conditions on $W$ below degree $L$ depend only on $V$:


$$
[T^Q,\ldots,T^{L-1}]\,\Phi(T)V(1+T)=0.
\tag{13.4}
$$


There are $P$ such conditions.

For any $V$ satisfying (13.4), the $r+1$ terminal conditions can be solved for $U$. The required jet map at $S=1$ is surjective because powers of $S$ are units modulo $(S+1)^{r+1}$. The equality of the $S^a$-coefficients is retained; the remaining solution space for $U$ has dimension $P-2$.

## 13.2 Odd $p$

For $p=2P+1$, write uniquely


$$
G(S)=S U(S)^2+S^2V(S)^2,
$$


where


$$
\deg U,\deg V<Q-1,\qquad S^a\mid U,V.
$$


With the same definitions of $u,v,W$,


$$
\boxed{
\beta_Z(G)=
[(1+T)\{W(T)^2+T^{2L+1}v(T)^2\}].
}
\tag{13.5}
$$



Now $q=2Q-1$. Comparing the retained even and odd coefficients, including the final coefficient of degree $d=2L+2r$, gives


$$
\boxed{
\beta_Z(G)=0
\iff
\begin{cases}
T^r\mid v(T),\\
[T^{Q-1},\ldots,T^{L+r}]\,W(T)=0.
\end{cases}}
\tag{13.6}
$$



Again


$$
V(S)=S^a(S+1)^rR(S),\qquad \deg R<P.
$$


The conditions below $L$ are now


$$
[T^{Q-1},\ldots,T^{L-1}]\,\Phi(T)V(1+T)=0,
\tag{13.7}
$$


a system of $P+1$ equations. For every admissible $V$, the terminal conditions leave a solution space for $U$ of dimension $P-1$.

The last terminal coefficient is necessary for these dimension counts. Truncating at $r=d-1$ would change them.

---

# 14. The smaller explicit matrix and quantified effective rank

Choose the basis


$$
R(S)=(S+1)^j,\qquad 0\le j<P.
$$


Define $C_{L,\rho,p}$ by


$$
\boxed{
C_{ij}
=
\sum_{\substack{e=1,2,4,\ldots\\e<L}}
\binom{a}{Q-\varepsilon+i-r-j-e}
\pmod2,
}
\tag{14.1}
$$


with


$$
0\le i<P+\varepsilon,\qquad 0\le j<P.
$$


Out-of-range binomial coefficients are zero.

This is the coefficient matrix of (13.4) or (13.7). Every sum has at most $\log_2L$ terms; no original-sized solve is proposed.

From the exact kernel counts above, including the two formal source relations,


$$
\boxed{
\operatorname{corank}(S_p/2)=p-\operatorname{rank}C_{L,\rho,p},
}
\tag{14.2}
$$


and hence


$$
\boxed{
\operatorname{rank}(S_p/2)
=\rho+1+\operatorname{rank}C_{L,\rho,p}.
}
\tag{14.3}
$$



This is not merely an unevaluated determinant formula. It proves:

1. a constructive unit block of size $\rho+1$ in the first divided quotient;
2. an exact reduction of its remaining rank question to (14.1);
3. the quantified bounds
   

$$
\rho+1\le\operatorname{rank}(S_p/2)
   \le\rho+1+\lfloor p/2\rfloor;
$$


4. the quantified surviving defect
   

$$
\lceil p/2\rceil
   \le\operatorname{corank}(S_p/2)\le p.
$$



The unit block of size $\rho+1$ is constructive: the $r$ terminal odd-coefficient conditions extract the first $r$ jets of $V(1+T)$, and the remaining $r+1$ terminal conditions extract an independent jet block from $U(1+T)$. The two jet maps are units after multiplication by the appropriate power of $S$, using the coprimality of $S$ and $S+1$.

Thus a linear number of exact first-level pivots has been paid in the actual full quotient.

## 14.1 Valuation consequence and the paid second lifts

Let


$$
\nu_p=\operatorname{corank}(S_p/2).
$$


Elementary unit elimination gives a block with:

- $q+1$ unit directions;
- $\rho+1+\operatorname{rank}C$ directions divisible by $2$, with odd quotient;
- $\nu_p$ directions divisible by at least $4$.

The two already completed base-$0$ second source lifts can be chosen as the first two surviving null directions. Their complete rows are divisible by $8$, after the paid bottom combinations. Eliminating the other unit blocks preserves that divisibility.

Therefore


$$
\boxed{
v_2(\det Z_{I,0})\ge\chi_p+\nu_p+2
\ge\chi_p+\left\lceil\frac p2\right\rceil+2.
}
\tag{14.4}
$$



This conclusion holds for every actual pole set $I$. It is a lower estimate; no nonzero terminal determinant is asserted.

---

# 15. Propagation through every source-jet pattern and both index sets

The complete fixed-$I,J$ pure-Cauchy product-atom aggregate is the paid finite sum


$$
\begin{aligned}
&(2^{\ell_d}\gamma)^{n-p}
C_p(I)\det N_d[I,J]\,
\prod_{j=p}^{n-1}(2^jj!)\\
&\qquad\times
\sum_U
\det\!\left[\binom{x}{j}\right]_{x\in J,j\in U}
\mathfrak F(U)o_d^p\det Z_{I,U}^{(0)},
\end{aligned}
\tag{15.1}
$$


where


$$
C_p(I)=
\frac{\Lambda_k^p2^{p(p-1)}\Phi_pV(I)}
{\prod_{i=0}^{n-1}Q_I(i)},
\qquad
\Phi_p=\prod_{j=0}^{p-1}j!,
$$


and


$$
\mathfrak F(U)=2^{\sum j_a}\prod_{a=0}^{p-2}R_{j_a}.
$$


All denominators in $C_p(I)$ are actual odd physical denominators. All Newton coefficients are finite integers. Every $I,J,U$ remains in (15.1).

The diagonal excess is


$$
w(I,J)=\sum_{i\in I}e_i+\sum_{j\in J}e_j-2E_p\ge0.
$$


No complementary forcing minor for a nonminimal pair is presumed odd.

## 15.1 A two-level rank-loss estimate

For $t=|U\setminus U_0|$, the stronger elementary estimate is


$$
\boxed{\sigma(U)\ge t^2.}
\tag{15.2}
$$


The minimum is obtained by replacing the largest $t$ minimal orders by
$p,p+1,\ldots,p+t-1$.

After matching common source rows, $Z_{I,U}^{(0)}$ differs from $Z_{I,0}$ in at most $t$ rows and one atom column.

If a matrix has $\chi$ directions divisible by $2$ and $\nu$ directions divisible by $4$, every codimension-$h$ minor has valuation at least


$$
\max(\chi-h,0)+\max(\nu-h,0).
$$


This follows directly by factoring the paid row powers after unit elimination. Expanding the $t$ changed rows and one changed column therefore gives


$$
v_2(\det Z_{I,U}^{(0)})
\ge
\max(\chi_p-t-1,0)+
\max(\nu_p-t-1,0).
\tag{15.3}
$$



Combining (15.2)–(15.3),


$$
\begin{aligned}
\sigma(U)+v_2(\det Z_{I,U}^{(0)})
&\ge\chi_p+\nu_p+t^2-2t-2\\
&\ge\chi_p+\nu_p-3.
\end{aligned}
$$


Thus


$$
\boxed{
\text{every fixed-\(I,J\) pure-Cauchy product-atom aggregate has depth}
\ge
\mathcal L_p+w(I,J)+
\chi_p+\left\lceil\frac p2\right\rceil-3.
}
\tag{15.4}
$$



This covers all source-jet patterns, not only a bounded excess inventory.

The result has deliberately not been promoted to a new unrestricted whole-coefficient bound. Beyond the already paid first linear window, bottom atoms and factorial patterns must be reconsidered at the new precision. The complete constant border (1.7) also remains a different problem.

Within the first-$d/8$ window, all competitors have already been handled in Section 8, so every minimizing count and every tie remains covered by the audited whole lower theorem.

---

# 16. New bounded exact-arithmetic diagnostic

No computation was performed, and none is needed for the algebraic proofs above.

A genuinely new bounded check can test the full first Schur calculation, rather than rerunning the closed source-law scans.

## 16.1 Inputs

Use the auxiliary parameters


$$
L=32,\qquad \rho=16,\qquad d=80,
$$


with


$$
p=8,\quad p=9.
$$


These satisfy the algebraic rank-window hypotheses and $16\mid d$, but are **not original indices** $9^{18+32u}-1$.

For each $p$, use both


$$
I=T_p=\{d-p,\ldots,d-1\}
$$


and


$$
I=T'_p=\{d-p-1,d-p+1,\ldots,d-1\}.
$$



Construct the actual normalized matrices $Z_{I,0}$ modulo $4$ from the original recurrence, with:

- $u_m=a_{2m}$ only for $0\le m\le241=3d+1$;
- literal $P_{80}$;
- full divisors $2^rr!$, $2^j(81)_j$, and $2^jj!$;
- actual atom ratios and $o_{80}=80!/2^{78}$;
- all contact columns $0\le r\le80$;
- all bottom orders $p\le j\le81$.

No forcing inverse or original-sized solve is required.

## 16.2 Expected verifiable outputs

For $p=8$,


$$
q=56,\qquad \chi_p=25.
$$


Here $P=4,r=8,a=16,Q=28$, and (14.1) gives


$$
C=
\begin{pmatrix}
1&0&1&1\\
0&1&0&1\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}.
$$



For $p=9$,


$$
q=55,\qquad \chi_p=26.
$$


Here $P=4,r=8,a=15,Q=28$, and


$$
C=
\begin{pmatrix}
1&1&0&1\\
0&1&1&0\\
0&0&1&1\\
0&0&0&1\\
0&0&0&0
\end{pmatrix}.
$$



Thus the predicted complete outputs, for both pole sets, are


$$
\begin{array}{c|c|c|c|c}
p&\text{matrix size}&\operatorname{rank}\overline Z&
\operatorname{rank}(S/2)&\operatorname{corank}(S/2)\\ \hline
8&82&57&21&4\\
9&82&56&21&5
\end{array}
$$



A verifiable certificate should include:

1. the finite binary row and column transformations producing the stated leading unit block;
2. the transformed matrix modulo $4$, before division;
3. the complete $S/2\bmod2$;
4. row-reduction certificates for ranks $21$;
5. verification that both actual pole sets give the same effective map after the stated coordinate identifications.

This would establish only these four finite matrix checks. It would not establish an original-index valuation upper, a Smith spectrum at all depths, or any conclusion about $e+\pi$.

---

# 17. Audit and proof-status ledger

| Claim | Decision and scope |
|---|---|
| Actual atom pivot and both $p$-parity contact lists | **PASS** |
| Last unpaired source row | **PASS; retained explicitly** |
| Finite span reduction (3.3) | **PASS** |
| Trace generating function and $P_s$ | **PASS** |
| Truncation through contact terminal $r=d$ | **PASS** |
| Multiplication/division by $S^p$ as a finite unit | **PASS; no content division** |
| Exact rank for $L\equiv2\pmod3$ | **PASS, both $p$ parities** |
| Exact rank for $L\equiv1\pmod3$ | **PASS, both $p$ parities** |
| Constructive unit complement in the second case | **PASS with explicit $\mathcal U^{-1}$ coordinate clarification** |
| Corank-effective Schur identity | **PASS** |
| A2 bound $v_2(\det Z_p)\ge\chi_p+2$ | **PASS; lower bound only** |
| General $\chi_p-1$ source-excess tradeoff | **PASS for all finite $U,I,J$** |
| Whole linear lower divisor on the original rotation interval | **PASS, including all forcing classes and counts** |
| Exact valuation $m_\star+6$ on that interval | **Excluded for sufficiently large original indices** |
| Full first effective map (12.6) | **NEW PROVED**, $L\equiv2\pmod3$ |
| First effective rank formula (14.3) | **NEW PROVED** |
| At least $\rho+1$ first-level unit pivots | **NEW PROVED** |
| Surviving first-quotient corank between $\lceil p/2\rceil$ and $p$ | **NEW PROVED** |
| Two-level all-pattern bound (15.4) | **NEW PROVED**, complete pure-Cauchy product-atom aggregates |
| Full first quotient for $L\equiv1\pmod3$ | **Not evaluated here** |
| General rank of $C_{L,\rho,p}$ beyond the proved bounds | **OPEN** |
| Higher effective determinants and terminal-excess upper | **OPEN** |
| Complete constant coefficient $I_{0,k}$ | **OPEN; literal border retained** |
| Joint binary target and all-prime gcd control | **OPEN** |
| Rationality or irrationality of $e+\pi$ | **OPEN** |

No eigenvalue/Smith equality theorem or ordinary automatic-sequence Hankel theorem has been imported. The new calculation uses finite trace identities, explicit source laws, triangular basis changes, and Schur elimination with checked hypotheses.

---

# 18. Actual contents, least clearer, final gcd, and whole error

The original determinant remains


$$
H_k(s)=H_{0,k}+H_{1,k}s
=
\det\left[
(c_{m+j})\
\middle|\
\bigl(\Lambda_k(r_{m+j}+s(-1)^{m+j})\bigr)
\right],
$$


with $0\le m<2k$, $0\le j<k$.

The individual least right-column entry clearers remain


$$
\Lambda_{k,j}
=\operatorname{lcm}(1,3,\ldots,4k+2j-3).
$$



Retain the all-prime quantities


$$
G_k=\gcd(|H_{0,k}|,|H_{1,k}|),
\qquad
d_{H,k}=\gcd(\Lambda_k^k,H_{0,k},H_{1,k}).
$$


The actual least simultaneous coefficient clearer and subsequent content are


$$
\boxed{
\frac{\Lambda_k^k}{d_{H,k}},
\qquad
\frac{G_k}{d_{H,k}}.
}
\tag{18.1}
$$



The actual maximal-minor contents remain


$$
\mathscr R_k=\delta_{2k-1}(Z_k),\qquad
\mathscr L_k=\delta_{2k-1}(Y_k),
$$


for the original rectangles


$$
Z_k=[(c_{m+j})_{m<2k,j<k}\mid(T_{m+j})_{m<2k,j<k-1}],
$$




$$
Y_k=[(\sigma_{m+j})_{m<2k-1,j<k}\mid(T_{m+j})_{m<2k-1,j<k}],
$$


with


$$
\operatorname{lcm}(\mathscr L_k,\mathscr R_k)
\mid G_k\mid\Lambda_k\mathscr L_k\mathscr R_k.
\tag{18.2}
$$



The paid five-column all-prime transfer is unchanged:


$$
\boxed{
|\delta_k|^{d+2}\Omega_k|\mu_{5,k}|^{d-4}G_k
=
|f_k|\,2^{\lambda_d^{\rm tr}+d+69}
\left(\prod_{r<d}2^rr!\right)g_k^{[5]},
}
\tag{18.3}
$$


where


$$
\lambda_d^{\rm tr}=d\alpha+4d+4,
\qquad
f_k=(-\Lambda_k)^d\det(\mathbf K_d)
\left(\prod_{m<d}(2m)!\right)^2.
$$


Every odd factor in this identity remains actual.

The open joint binary target is still


$$
\boxed{
\min(v_2(I_{0,k}),v_2(I_{1,k}))
\le\frac{15}{4}k^2+d+5+O(k\log k).
}
\tag{18.4}
$$


Neither the audited linear lower divisor nor the new effective-rank theorem proves it.

The actual primitive numerator and denominator remain


$$
q_k=\frac{|H_{1,k}|}{G_k}>0,\qquad
p_k=-\frac{(-1)^kH_{0,k}}{G_k},
$$


with the retained same-index nonzero whole evaluated error


$$
\boxed{
0<q_k(e+\pi)-p_k
=\frac{|H_k(e+\pi)|}{G_k}.
}
\tag{18.5}
$$


No binary divisor replaces the all-prime $G_k$, and no selected error summand replaces the whole value in (18.5).

---

# Final conclusion: new result and exact remaining bottleneck

The A2 Turn 16 parity-rank and linear-divisor claims survive a different full audit. The proof retains both $L\bmod3$ cases, both parities of $p$, the final combined source row, the actual atom pivot, and the physical contact terminal $r=d$. The source-excess tradeoff and the whole linear lower divisor also survive all-pattern and all-forcing checks.

The new advance is a computation of the full first divided Schur map on the $L\equiv2\pmod3$ subfamily:


$$
\boxed{
G\longmapsto
\left[
Y\left(G'(S)+pG(S)/S\right)+Y^{2L}G(S)
\right].
}
$$


The terminal term $Y^{2L}G(S)$ is the first Frobenius carry and is indispensable.

This computation proves that the first quotient has at least $\rho+1$ unit directions and leaves a defect between $\lceil p/2\rceil$ and $p$. It also gives an exact smaller rank matrix and a uniform two-level lower payment for every finite source-jet pattern and both Cauchy–Binet index sets.

The remaining local bottleneck is now more precise:

1. determine the residual ranks and, more importantly, the higher divided matrices on the explicitly described kernel of (12.6);
2. prove a nonzero complete aggregate within $O(d\log d)$ excess, including all newly affordable source, pole, forcing, and product-count competitors;
3. do so for the literal paired coefficient system, including the complete $-f+4\rho$ border.

Even that would still leave the other-prime arithmetic, final all-prime gcd, and same-index primitive whole-error comparison to be completed.

The optional bounded calculation in Section 16 would test the newly computed full first quotient and its carries on two small auxiliary matrices. Its expected outputs and finite scope are explicit; no original-sized solve or closed scan is requested.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi\text{ is obtained.}}
$$


