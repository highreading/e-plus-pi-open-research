> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A3 Turn 19 — Independent audit of the finite annihilator and closure of the core $\eta _0$ interface

## Executive verdict

**The uniform finite annihilator argument in A1 Turn 18 passes the audit below.** Its conclusion is about the actual finite **core** Schur matrix


$$
\mathcal S_H=E_Y-3\mathcal X^TM_L\mathcal X,
$$


not about an infinite convolution model or the unreturned block $E_Y$. Both finite HIGH masks, the complete fourteen-term source, both $\beta$ and $3y$ channels, the upper $3H$ moment indicator, and the relevant LOW returns are retained.

In particular, the finite witness constructed in A1 Turn 18 does satisfy


$$
\boxed{
\mathcal S_H(e_d+3z_0+9\widehat z_1+27z_2)-\upsilon_T
\in3^{27}\mathbb Z_3^{[d,m]},
\qquad
z_2^Tf_H\in3^{24}\mathbb Z_3,
}
$$


and hence


$$
\boxed{w_2^Tf_H\equiv0\pmod{3^{24}}.}
$$



The inherited endpoint interface also closes at its proper scope. I verify the prefix-returned residual identity, the complete $W$-projection formula, and the bare endpoint cancellation in A1 Turn 13. I then give an additional, source-specific LOW-return payment which proves directly that


$$
\boxed{
g_T^TE_c^{-1}b_0\in3^{30}\mathbb Z_3.
}
$$


Consequently,


$$
\boxed{\eta_0=0\quad\text{in the original core terminal residue space }\mathbb F_3.}
$$



This is unconditional **within the original core construction and its already established finite unit and source hypotheses**, which are valid on the retained sufficiently large original indices. It is no longer dependent on an unpaid endpoint-divisibility premise. It is not an assertion that an entire $3$-adic terminal coordinate vanishes to every order.

Two distinctions remain essential:

* The previously proved nonzero $r_2$ edge makes the two chosen lifts alone sharp at residual depth $3$. It does not contradict the full residual-sequence annihilator audited here. That earlier edge theorem is not relabelled here as independently audited.
* Nothing here transports the core conclusion to
  

$$
Q_{\rm act}=Q_c+3^7\mathscr R,
$$


  evaluates the alternate endpoint or the first-$4$ return, closes the separate higher ternary audit, supplies source precision $34$, or proves an all-prime primitive-denominator saving.

No tools or numerical execution were used. No original-length vector, grid, table, or solve is proposed.

---

## 1. Original domain, finite objects, and reuse

Throughout, $v_3(0)=+\infty$. “Integral” means $3$-adically integral unless ordinary integer integrality is explicitly stated.

### 1.1 The original indices are unchanged

All uniform statements concern sufficiently large tuples in the original family


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


with


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



Retain


$$
P=3^{h-32},\quad P_0=243P,\quad N_0=243r,\quad D=P_0+N_0,
$$




$$
r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1,
$$


and


$$
Q=27P,\qquad Q-N_0=2R,\qquad \chi=P-R.
$$


Thus


$$
N_0=25P+2\chi,\qquad D=268P+2\chi.
$$



The restriction remains


$$
\boxed{\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.}
$$


No independent choices of $P$ and $\chi$ are made.

Write


$$
S=h-32,\qquad P=3^S,\qquad H=3^{S+31},\qquad S\ge31,
$$




$$
\Pi=P/3,\qquad t=\Pi-2\chi,\qquad k=3\chi-\Pi-1.
$$


The retained arithmetic gives


$$
v_3(\chi)=5,\qquad \chi/243\equiv1\pmod9,
$$




$$
v_3(D)=5,\qquad D<269P.
$$



The finite boundaries are


$$
\nu=D/2-1=134P+\chi-1,
$$




$$
d=D+\nu=402P+3\chi-1,
$$




$$
m=\frac{H-D+1}{2},\qquad r_H=\frac{H-1}{2}=m+\nu.
$$



In particular,


$$
D\equiv0,\quad \nu\equiv d\equiv26,\quad r_H\equiv13\pmod{27}.
$$



### 1.2 Literal finite spaces and complete columns

The spaces remain


$$
U_u=x^u,\quad 0\le u<D,\qquad x=y-1,
$$




$$
z_i^{\rm mid}=x^Dy^i,\quad 0\le i<\nu,
$$




$$
Y_s=y^s,\quad d\le s\le m.
$$



The physical HIGH terminal is $Y_m$. The last middle polynomial is $y^{\nu-1}$. They are not interchangeable.

The complete functional is


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{v=0}^{K_{\rm phys}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
$$


where


$$
\mathfrak f(y^a)=(2a)!,
\qquad
K_{\rm phys}=2n-2=2H-2D+2.
$$



The core producer and form are


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=D-H-71,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg).
$$


Set


$$
W=[U\ Y],\qquad E_c=G_c(W,W).
$$


The complete corrected column is


$$
\boxed{
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).
}
$$



The actual finite block decomposition is


$$
E_c=
\begin{pmatrix}
3\mathcal L&3\mathcal X\\
3\mathcal X^T&E_Y
\end{pmatrix},
$$




$$
M_L=\mathcal L^{-1},\qquad
\mathcal S_H=E_Y-3\mathcal X^TM_L\mathcal X,\qquad
M_H=\mathcal S_H^{-1}.
$$


The established finite unit results give integral $M_L$ and $M_H$. The physical LOW inverse remains


$$
(3\mathcal L)^{-1}=\frac13M_L.
$$



### 1.3 The whole fourteen-term source

Retain


$$
p_0=\Omega_P(y)(1-y)^t,
$$


where


$$
\begin{aligned}
\Omega_P(y)={}&
(1-y)^{2P}(y^{122P}+3y^{41P})\\
&+9(1+y^P+y^{2P})
(2y^{14P}+2y^{41P}+2y^{95P}-y^{131P}).
\end{aligned}
$$


Thus


$$
p_0=\sum_{(\Delta,b,c)\in\mathcal T}
c(1-y)^{t+\Delta}y^{bP}.
$$



The sources are


$$
\upsilon_T=\frac{G_c(Y,x^Dy^{\nu-1})}{3},
\qquad
f_H=\frac{G_c(Y,x^Dp_0)}9.
$$


Their established integral normalizations are retained.

### 1.4 Closed results used at their stated scope

I reuse, without repeating their expensive calculations:

1. the finite unit results for $M_L,M_H$;
2. the literal finite leading inverse
   

$$
(\overline M_He_t)_s
   =[Z^{m+d-s-t}](1-Z)^D;
$$


3. the complete first and second chosen lifts and their contractions in $3^{29}$;
4. the paid LOW source results and actual matrix/source gradings from the already passed finite-source work;
5. the exact next-force formula, including its $3^{23}R_d$ term;
6. the established finite prefix inverse image used in A1 Turn 13.

The complete A1 Turn 17 second-lift audit is now reuse. The previous A3 $r_2$-edge theorem retains its separate review status.

---

## 2. The actual finite preconditioner and grading — PASS

### 2.1 The integral preconditioner is not a higher-precision inverse formula

For $v\in\mathscr V:=\mathbb Z_3^{[d,m]}$, write


$$
V_v(y)=\sum_{s=d}^m v_sy^s.
$$


Define


$$
\boxed{
V_{\mathcal K_Hv}(y)
=
\operatorname{pr}_{[d,m]}
\left(x^Dy^{r_H}V_v(y^{-1})\right).
}
$$


Its matrix coefficient is


$$
[y^{s-r_H+t}](y-1)^D
=
[Z^{m+d-s-t}](1-Z)^D.
$$


Therefore


$$
\mathcal K_H\equiv M_H\pmod3.
$$



Both input and output intervals are literal finite intervals. No higher-precision inverse identity is asserted.

### 2.2 Why $\mathcal K_H\bmod9$ is reflection-graded by $13$

For $27\nmid i$,


$$
v_3\binom Di
\ge v_3(D)-v_3(i)\ge3.
$$


Thus $x^D\bmod9$ is supported at exponents divisible by $27$.

A nonzero entry of $\mathcal K_H\bmod9$ consequently requires


$$
s+t\equiv r_H\equiv13\pmod{27}.
$$


Coordinate projection preserves this support statement.

### 2.3 Validation of the actual Schur grading

It is useful to make explicit why the grading applies to the returned matrix.

Temporarily use monomial LOW coordinates $y^u$, $0\le u<D$. The change from $x^u$ is integral and unimodular. If its matrix is $T$, then


$$
\mathcal L_y=T^T\mathcal L T,\qquad
\mathcal X_y=T^T\mathcal X,
$$


and


$$
\mathcal X_y^T\mathcal L_y^{-1}\alpha_y
=
\mathcal X^TM_L\alpha.
$$


This is only a coordinate device for the proof; it does not redefine any original integer column or content.

Since $v_3(A)=5$, coefficients of $x^A$ at indices not divisible by $27$ have valuation at least $3$. The moment poles visible modulo $9$ have pole index congruent to $13\pmod{27}$.

For the normalized LOW and LOW/HIGH blocks, the $3H$ pole is absent:

* LOW/LOW rational degree is at most $H+D-1$;
* LOW/HIGH rational degree is at most $H+m$;
* both are strictly below $(3H-1)/2$.

Their division by $3$ is therefore compatible with integral pole weights. It follows that, modulo $9$,


$$
\mathcal L_y=L_0+3L_1,\qquad
\mathcal X_y=X_0+3X_1,
$$


where the subscript $0$ part has reflection grade $13$, and the subscript $1$ part has reflection grade $12$.

For $E_Y$, the $3H$ pole can occur and is retained. Its weight is integral. The same coefficient argument gives


$$
E_Y=E_0+3E_1\pmod9
$$


with grades $13$ and $12$, respectively.

Modulo $3$, the finite inverse of $L_0$ also has reflection grade $13$. Hence


$$
3\mathcal X^TM_L\mathcal X\pmod9
$$


has reflection grade $13$. Thus


$$
\boxed{
\mathcal S_H\equiv S_0+3S_1\pmod9,
}
$$


where $S_0$ has reflection grade $13$ and includes the leading LOW matrix return, while $S_1$ has reflection grade $12$.

This validates the asserted grading in the actual finite objects. Replacing $\mathcal S_H$ by $E_Y$ would be unnecessary and incorrect.

### 2.4 Validation of the actual source grading

For one source term, the beta top in $G_c(Y,x^Dp_0)$ is


$$
N=H+t+\Delta=H+N_{\rm lo},
\qquad v_3(N)=5.
$$


The actual degree remains below $(3H-1)/2$, because $b+\Delta/P\le133$ and


$$
H+m+t+\Delta+bP+\epsilon
=
\frac{3H}{2}
-\left(134-b-\frac{\Delta}{P}-\frac13\right)P
-3\chi+\frac12+\epsilon.
$$



After division by $9$, the only potentially negative pole-weight valuation is $-1$, at denominator $H$. Its coefficient index $r$, for either actual channel, satisfies


$$
N_{\rm lo}<r<H.
$$


Indeed, the smallest such index occurs at the largest actual channel argument and obeys


$$
r-N_{\rm lo}
\ge
\left(134-b-\frac{\Delta}{P}-\frac13\right)P+3\chi-2>0.
$$


Since


$$
(1+z)^{H+N_{\rm lo}}
\equiv(1+z^H)(1+z)^{N_{\rm lo}}\pmod3,
$$


the coefficient at such an $r$ is divisible by $3$. This pays the possible $3^{-1}$.

Off the required residue class modulo $27$, the coefficient valuation is at least $3$; even the worst pole weight then leaves valuation at least $2$. Consequently,


$$
\boxed{
f_H\equiv f_{13}+3f_{12}\pmod9,
}
$$


where the subscripts specify HIGH support residues modulo $27$.

This argument retains all fourteen source terms and does not depend on a cancellation guessed from leading residues.

### 2.5 The preconditioned action

Put


$$
\mathcal A=\mathcal K_H\mathcal S_H.
$$


Composition of the two reflection gradings gives


$$
\mathcal A\equiv A_0+3A_1\pmod9,
$$


with


$$
A_0:\mathscr V_b\longrightarrow\mathscr V_b,
\qquad
A_1:\mathscr V_b\longrightarrow\mathscr V_{b+1}.
$$


Also


$$
\mathcal A\equiv I\pmod3.
$$



These are actual finite-matrix statements.

---

## 3. Safe-grid seeds and both masks — PASS

Set


$$
B_\circ=\frac{H}{3^{24}}=2187P,
\qquad
C_\circ=\frac{3^{24}-1}{2}.
$$


Then


$$
C_\circ B_\circ=\frac{H-B_\circ}{2}.
$$



The original bounds imply


$$
B_\circ>4D+60,\qquad B_\circ/2>540P,\qquad \nu>28.
$$



Define


$$
\mathsf T_{a,v}
=
3^{(a-1)_+}
\operatorname{pr}_{[d,m]}
\left(x^Dy^{vB_\circ+\nu-1+a}\right),
\quad 0\le a\le27,
$$




$$
\mathsf Q_{a,v}
=
3^a
\operatorname{pr}_{[d,m]}
\left(x^Dy^{vB_\circ}P_{d+a}\right),
\quad 0\le a\le26,
$$




$$
\mathsf O_{a,v}
=
3^a
\operatorname{pr}_{[d,m]}
\left(x^Dy^{vB_\circ+a}\right),
\quad 0\le a\le26,
$$


for $0\le v\le C_\circ$, where


$$
P_{d+a}=\sum_{i=0}^{\nu+a}b_i y^{\nu+a-i},
\qquad
b_i=\binom{D+i-1}{i}.
$$


Let $\mathscr B$ be their $\mathbb Z_3$-span.

There are $28+27+27=82$ weighted families. That count is not the proof of annihilation or closure.

### 3.1 Exact interior support inequalities

For $1\le v\le C_\circ$, the seeds are wholly inside the HIGH interval.

For terminal seeds, the upper margin is


$$
m-(C_\circ B_\circ+d-1+a)
=
\frac{B_\circ-4D+5-2a}{2}.
$$


For quotient seeds, it is


$$
m-(C_\circ B_\circ+d+a)
=
\frac{B_\circ-4D+3-2a}{2}.
$$


For ordinary seeds, it is


$$
m-(C_\circ B_\circ+D+a)
=
\frac{B_\circ-3D+1-2a}{2}.
$$


All are nonnegative in the stated offset ranges.

The lower inequalities follow from $B_\circ>d$, and, for terminal seeds, from $B_\circ>D+1$.

### 3.2 Exact lower-edge values

At $v=0$,


$$
\mathsf Q_{a,0}=3^a y^{d+a},
\qquad
\mathsf O_{a,0}=0.
$$


For $a\ge1$,


$$
\boxed{
\mathsf T_{a,0}
=
3^{a-1}\sum_{b=0}^{a-1}
(-1)^{a-1-b}\binom D{a-1-b}y^{d+b}.
}
$$


For $a=0$, the projection is zero.

These are literal lower-mask formulas.

### 3.3 The inner mask identity

For each seed


$$
y^{\nu-1+a},\qquad P_{d+a},\qquad y^a,
$$


one has


$$
\boxed{
\operatorname{pr}_{[d,m]}
\left[
x^D\operatorname{pr}_{[\nu,m-D]}
(y^{vB_\circ}\,\text{seed})
\right]
=
\operatorname{pr}_{[d,m]}
(x^Dy^{vB_\circ}\,\text{seed}).
}
$$



Here is the complete boundary justification.

* A seed exponent below $\nu$ cannot reach $d=D+\nu$ after multiplication by $x^D$.
* For $0\le v\le C_\circ$, every seed exponent is at most
  

$$
C_\circ B_\circ+\nu+26\le m-D,
$$


  by
  

$$
B_\circ-4D-49>0.
$$


* For $v\ge C_\circ+1$, even the start of a quotient or ordinary block exceeds $m$.
* For $v<0$, the entire block lies below the range capable of reaching HIGH.

Thus no translated block contributes an exponent in the dangerous interval $(m-D,m]$.

This is the finite fact that licenses the later convolution identity. It is not an infinite-convolution assumption.

---

## 4. Whole fourteen-source annihilation — PASS

The beta ratio and its exact valuation are reused:


$$
\mathcal B(N,q)
=
\frac{4^NN!(N+q)!(2q)!}{q!(2N+2q+1)!},
$$




$$
v_3\mathcal B(N,q)
=
-\sum_{e\ge1}
\mathbf1_{\{N\bmod3^e\ge j_e(q)\}},
\qquad
j_e(q)=\left(\frac{3^e-1}{2}-q\right)\bmod3^e.
$$



After division by $9$, the common functional scale is


$$
3^{h-2}=3^{S+30}.
$$


A source term and channel carry the full multiplier


$$
c\,\beta^{1-\epsilon}3^\epsilon,
\qquad \epsilon=0,1.
$$



### 4.1 All fourteen residual bounds

Put $\delta=\Delta/P\in\{0,2\}$. For terminal, quotient, and lower-edge estimates, the relevant residual sum is bounded by


$$
N_{\rm lo}+q_{\rm lo}
\le
\left(402+\frac13+\delta+b\right)P+\chi+27.
$$



The complete table is:

| $\delta$ | $b$ | $c$ | $v_3(c)$ | coefficient of $P$ in the bound |
|---:|---:|---:|---:|---:|
| 2 | 122 | 1 | 0 | $526+\frac13$ |
| 2 | 41 | 3 | 1 | $445+\frac13$ |
| 0 | 14 | 18 | 2 | $416+\frac13$ |
| 0 | 15 | 18 | 2 | $417+\frac13$ |
| 0 | 16 | 18 | 2 | $418+\frac13$ |
| 0 | 41 | 18 | 2 | $443+\frac13$ |
| 0 | 42 | 18 | 2 | $444+\frac13$ |
| 0 | 43 | 18 | 2 | $445+\frac13$ |
| 0 | 95 | 18 | 2 | $497+\frac13$ |
| 0 | 96 | 18 | 2 | $498+\frac13$ |
| 0 | 97 | 18 | 2 | $499+\frac13$ |
| 0 | 131 | $-9$ | 2 | $533+\frac13$ |
| 0 | 132 | $-9$ | 2 | $534+\frac13$ |
| 0 | 133 | $-9$ | 2 | $535+\frac13$ |

Since


$$
\frac{\chi}{P}<\frac{31}{250},\qquad P\ge3^{31},
$$


every displayed bound is strictly below $540P$. Ordinary seeds have a smaller bound.

This validates the uniform bound separately for all fourteen sources and both channels.

### 4.2 Exclusion of all high indicators

For interior terminal and quotient seeds,


$$
N=H+268P+\Pi+\Delta,
\qquad v_3(N)=S-1.
$$


Write $N=H+N_{\rm lo}$, $q=vB_\circ+q_{\rm lo}$.

For $S+7\le e\le S+31$, the modulus $3^e$ is an odd multiple of $B_\circ$. The threshold $j_e(q)$ has the form


$$
rB_\circ+\frac{B_\circ-1}{2}-q_{\rm lo}
$$


for some nonnegative integer $r$. Hence


$$
j_e(q)\ge\frac{B_\circ-1}{2}-q_{\rm lo}>N_{\rm lo}.
$$


The indicator is absent.

At modulus $3H$,


$$
q\le\frac{H-B_\circ}{2}+q_{\rm lo},
$$


so


$$
\frac{3H-1}{2}-q
\ge
H+\frac{B_\circ-1}{2}-q_{\rm lo}
>
H+N_{\rm lo}.
$$


All higher indicators are absent as well.

This argument is uniform in every grid coefficient. It is not a check at selected grid positions.

### 4.3 Terminal and ordinary seeds

For terminal seeds,


$$
q=vB_\circ+(134+b)P+\chi-2+a+\epsilon.
$$


The first $S-1$ indicators count


$$
v_3(2a+2\epsilon-3)\le3.
$$


For ordinary seeds,


$$
q=vB_\circ+a+bP+\epsilon,
$$


and the corresponding count is


$$
v_3(2a+2\epsilon+1)\le3.
$$



The precise elementary bound is that the relevant nonzero odd integers have absolute value at most $55<81$. This makes the valuation bound explicit; merely saying “less than $243$” would not by itself imply valuation at most $3$.

There are only seven additional possible indicators, at levels $S,\ldots,S+6$. Thus the total count is at most $10$, and the contraction depth is at least


$$
S+30-10=S+20\ge51.
$$


All generator weights and source coefficients can only improve this.

### 4.4 Every coefficient of every finite quotient

For


$$
P_{d+a}=\sum_{i=0}^{\nu+a}b_i y^{\nu+a-i},
$$


the arguments are


$$
q=vB_\circ+\nu+a-i+bP+\epsilon.
$$


Put


$$
u=a+\epsilon,\qquad \omega=2u-1,\qquad \lambda=v_3(\omega)\le3.
$$



If $v_3(i)\ne\lambda$, including $i=0$, then


$$
v_3(2q+1)\le\lambda.
$$


This is already more than sufficient.

If $v_3(i)=\lambda$, then $i>0$, and the exact identity


$$
b_i=\frac Di\binom{D+i-1}{i-1}
$$


gives


$$
v_3(b_i)\ge5-\lambda.
$$


Allowing all first $S-1$ indicators and all seven remaining possible ones, the weighted contraction has valuation at least


$$
S+30+a+\epsilon+5-\lambda-(S+6)
=
29+u-\lambda.
$$


For every nonnegative integer $u$,


$$
v_3(2u-1)\le u.
$$


Therefore every coefficient contributes in $3^{29}$.

The finite range $0\le i\le\nu+a$, including both endpoints, has been retained. No infinite quotient tail is used.

### 4.5 Weighted lower edges

For $3^a y^{d+a}$,


$$
N=H+t+\Delta,\qquad v_3(N)=5,
$$




$$
q=(402+b)P+3\chi-1+a+\epsilon.
$$


The first five indicators contribute


$$
\lambda=v_3(2a+2\epsilon-1)\le3.
$$


There are at most $S+1$ more possible indicators, at levels $6,\ldots,S+6$. Thus the weighted valuation is at least


$$
S+30+a+\epsilon-(S+1+\lambda)
=
29+a+\epsilon-\lambda\ge29.
$$



In the lower-mask formula for $\mathsf T_{a,0}$, the factor $3^{a-1}$ pays the required factor $3^b$ for every $b\le a-1$. Hence the entire masked polynomial, not just its top monomial, has the required bound.

### 4.6 Physical cutoff and factorial contribution

For every interior contraction,


$$
N+q
\le
H+\frac{H-B_\circ}{2}+540P
<
\frac{3H}{2}
<
K_{\rm phys}.
$$


There is a large strict margin, so the possible half-integer endpoint causes no issue.

The factorial contribution after division by $9$ lies in


$$
3^{h-2}\mathbb Z_3=3^{S+30}\mathbb Z_3,
$$


because all polynomial coefficients are integral.

Therefore


$$
\boxed{\mathscr B^Tf_H\subseteq3^{29}\mathbb Z_3.}
$$



This is whole-source annihilation to a stated modulus, not exact vanishing in $\mathbb Z_3$.

### 4.7 A useful source-specific extension

The quotient proof did not require $v\ge1$. At $v=0$, it also proves


$$
\boxed{
\frac{G_c(3^a x^DP_{d+a},x^Dp_0)}9
\in3^{29}\mathbb Z_3,
\qquad 0\le a\le26.
}
$$


Combining this with the weighted lower-edge result and


$$
y^{d+a}=C_{d+a}+x^DP_{d+a}
$$


gives


$$
\boxed{
\frac{G_c(3^a C_{d+a},x^Dp_0)}9
\in3^{29}\mathbb Z_3.
}
$$


This extension will pay a complete LOW-source return in the endpoint interface.

---

## 5. Exceptional module: whole pairing and actual closure — PASS

Define


$$
\mathscr E
=
\mathscr V_{25}+\mathscr V_{26}+\mathscr V_0
+3\mathscr V_1+9\mathscr V.
$$


By the actual source grading,


$$
\boxed{\mathscr E^Tf_H\subseteq9\mathbb Z_3.}
$$



The preconditioned grading gives


$$
25\longmapsto26,\qquad26\longmapsto0,\qquad0\longmapsto1
$$


for the part carrying a factor $3$. A vector already carrying $3$ at grade $1$ can reach grade $2$ only with a second factor $3$. Therefore


$$
\boxed{\mathcal A\mathscr E\subseteq\mathscr E.}
$$



Set


$$
\mathscr N=\mathscr B+3^{25}\mathscr E+3^{27}\mathscr V.
$$


Then


$$
\boxed{\mathscr N^Tf_H\subseteq3^{27}\mathbb Z_3.}
$$



The $9\mathscr V$ term in $\mathscr E$ is important: it makes this a statement about full two-digit jets, including their carries.

---

## 6. Complete bulk transition and every LOW return — PASS

### 6.1 Exact adaptation through LOW

For any HIGH polynomial $V$, divide exactly:


$$
V=x^DP+C,\qquad \deg C<D.
$$


Let $c$ be the original LOW coordinate vector of $C$, and define


$$
\alpha[P]=\frac{G_c(U,x^DP)}3.
$$


Then


$$
\mathcal Xv=\alpha[P]+\mathcal Lc,
$$


and


$$
E_Yv=G_c(Y,x^DP)+3\mathcal X^Tc.
$$


Consequently,


$$
\boxed{
\mathcal S_Hv
=
G_c(Y,x^DP)-3\mathcal X^TM_L\alpha[P].
}
$$


The LOW polynomial part cancels exactly. This is the true Schur adaptation.

### 6.2 Bulk LOW force at depth $25$

For every unweighted adapted bulk seed, in monomial LOW coordinates,


$$
q=vB_\circ+j+u+\epsilon,
\qquad
0\le u<D,\quad 0\le j\le\nu+27.
$$


The safe-grid bounds give


$$
q<r_H,
$$


and


$$
0<2(j+u+\epsilon)+1<3D+60<B_\circ.
$$


Thus


$$
v_3(2q+1)\le S+6.
$$



For beta top $H$ below $r_H$,


$$
v_3(H\mathcal B(H,q))=S+31-v_3(2q+1)\ge25.
$$


The $3y$ channel is deeper, and the factorial contribution after division by $3$ is also deeper. Therefore


$$
\boxed{\alpha[P]\in3^{25}\mathbb Z_3^D.}
$$



After the explicit Schur factor $3$, the LOW return starts at depth $26$.

### 6.3 Its leading grade

Only weight-one generators can contribute below $3^{27}$. Their grades are:

| adapted seed | exponent grade | normalized LOW force grade | grade after $\mathcal K_H\mathcal X^TM_L$ |
|---|---:|---:|---:|
| $y^{vB_\circ+\nu-1}$ | 25 | 15 | 25 |
| $y^{vB_\circ+\nu}$, $y^{vB_\circ}P_d$ | 26 | 14 | 26 |
| $y^{vB_\circ}$ | 0 | 13 | 0 |

The visible beta argument has grade $13$. The leading LOW inverse and cross each have reflection grade $13$, and $\mathcal K_H$ supplies the final reflection.

Hence


$$
\boxed{
3\mathcal K_H\mathcal X^TM_L\alpha[P]
\in
3^{26}(\mathscr V_{25}+\mathscr V_{26}+\mathscr V_0)
+3^{27}\mathscr V
\subseteq3^{25}\mathscr E.
}
$$



No depth-$25$ adapted-force assertion is imposed on an arbitrary exceptional vector. Subsequent exceptional feedback is handled by the actual $\mathcal A\bmod9$ closure.

---

## 7. Actual moment kernel, coarse action, fine action, and terminal — PASS

### 7.1 The physical kernel and the extra indicator

Write $L=S+31$, so $H=3^L$, and put


$$
\kappa(q)=-3H\mathcal B(H,q).
$$


For any actual adapted HIGH polynomial, the largest possible argument is


$$
q\le m+(m-D)+1=H-2D+2<H.
$$


Thus


$$
G_c(Y_s,x^DP)
=
\sum_jp_j\bigl(\beta\kappa(s+j)+3\kappa(s+j+1)\bigr)
$$


up to a factorial term in $3^h$.

The exact valuation is


$$
\boxed{
v_3\kappa(q)=
\begin{cases}
L+1-v_3(2q+1),&q<r_H,\\
0,&q=r_H,\\
L-v_3(2q+1),&q>r_H.
\end{cases}
}
$$


The last line includes the additional indicator at modulus $3H$. It has not been dropped.

### 7.2 Coarse and fine parts

The coarse part consists of arguments satisfying


$$
B_\circ\mid2q+1.
$$


At every other argument,


$$
\kappa_{\rm fine}(q)\in
\begin{cases}
3^{26}\mathbb Z_3,&q<r_H,\\
3^{25}\mathbb Z_3,&q>r_H.
\end{cases}
$$


Moreover,


$$
\kappa_{\rm fine}(q)/3^{25}\not\equiv0\pmod9
\quad\Longrightarrow\quad
243P\mid2q+1.
$$


Every visible divided fine argument therefore has grade $13\pmod{27}$.

The complete unit $\kappa(r_H)$ belongs to the coarse part.

### 7.3 Exact finite coarse action

Define the finite Laurent polynomial


$$
\mathcal C(y)=
\sum_{\substack{0\le q\le H-2D+2\\B_\circ\mid2q+1}}
\kappa(q)y^{r_H-q}.
$$


Its exponents are multiples of $B_\circ$.

The finite row reflection gives exactly


$$
\boxed{
\operatorname{pr}_{[d,m]}
\left[
x^D\operatorname{pr}_{[\nu,m-D]}
\bigl((\beta+3y)\mathcal C(y)P(y)\bigr)
\right].
}
$$


Indeed, the exponent $r_H-s$ runs through $[\nu,m-D]$ as the actual row $s$ runs through $[d,m]$.

The safe-grid mask identity now applies. The only nontrivial quotient transition is the exact finite identity


$$
\boxed{yP_{d+a}=P_{d+a+1}-b_{\nu+a+1}.}
$$



Therefore:

* $\beta$ preserves each weighted family;
* $3y$ raises an offset and pays its new weight;
* the quotient constant correction belongs to the ordinary family;
* terms beyond the largest displayed offsets carry $3^{27}$;
* translated blocks outside the finite interval have zero projection.

Thus the coarse action belongs to


$$
\mathscr B+3^{27}\mathscr V.
$$



All digits of $\beta$ and all integral coarse kernel coefficients remain in this argument.

### 7.4 Fine action, including both clipped edges

For $27\nmid i$,


$$
v_3(b_i)\ge5-v_3(i)\ge3.
$$


Hence


$$
P_{d+a}\bmod9
$$


has exponent grade $\nu+a$.

After extracting $3^{25}$, the only potentially visible weighted seeds are:

| seed | weight modulo $9$ | beta-output grade |
|---|---:|---:|
| $\mathsf T_{0,v}$ | 1 | 25 |
| $\mathsf T_{1,v}$ | 1 | 26 |
| $\mathsf T_{2,v}$ | 3 | 0 |
| $\mathsf Q_{0,v}$ | 1 | 26 |
| $\mathsf Q_{1,v}$ | 3 | 0 |
| $\mathsf O_{0,v}$ | 1 | 0 |
| $\mathsf O_{1,v}$ | 3 | 1 |

For lower-masked terminal seeds, this table is still valid:

* $\mathsf T_{1,0}=y^d$ has adapted quotient $P_d$;
* $\mathsf T_{2,0}=3(y^{d+1}-Dy^d)$ has adapted quotient
  

$$
3(P_{d+1}-DP_d),
$$


  and the $D$-term is too deep to affect this two-digit jet.

The $3y$ channel raises the listed grade by one and costs $3$. Every resulting term is allowed by $\mathscr E$. Coordinate clipping cannot change a residue class.

Consequently,


$$
\boxed{\text{fine action}\in3^{25}\mathscr E.}
$$



This contains the complete upper clipping on the $729P$ grid and both lower and upper clipping on the $243P$ grid. The inequalities


$$
D<729P<4D,\qquad243P<D
$$


explain why those geometric interactions are real; they are not ignored.

Combining the coarse, fine, factorial, and LOW terms proves


$$
\mathcal A\mathscr B\subseteq\mathscr N,
\qquad
\boxed{\mathcal A\mathscr N\subseteq\mathscr N.}
$$



### 7.5 The normalized terminal source

The actual terminal beta arguments satisfy


$$
q=s+\nu-1<r_H.
$$


The actual $3y$ arguments satisfy


$$
q=s+\nu\le r_H,
$$


with equality only at the physical terminal $s=m$.

The coarse contribution can be written explicitly:


$$
\begin{aligned}
\mathcal K_H\upsilon_{T,\rm coarse}
={}&
\sum_{v=1}^{C_\circ}
\frac{\beta\kappa(r_H-vB_\circ)}3\,\mathsf T_{0,v}\\
&+\sum_{v=1}^{C_\circ}
\kappa(r_H-vB_\circ)\,\mathsf T_{1,v}
+\kappa(r_H)e_d.
\end{aligned}
$$


Every coefficient is integral. The potentially nonintegral isolated quantity


$$
\kappa(r_H)/3
$$


does not occur in the beta channel and is not divided there.

The fine beta part starts at depth $25$ and has grade $25$ after $\mathcal K_H$. The fine $3y$ part starts at depth $26$ and has grade $26$. The factorial part after terminal normalization lies in $3^{h-1}$.

Therefore


$$
\boxed{\mathcal K_H\upsilon_T\in\mathscr N.}
$$



This completes the audited finite transition theorem.

---

## 8. Full residual sequence and the precision-$27$ witness — PASS

Retain the already established exact decomposition


$$
M_H\upsilon_T=e_d+3z_0+9\widehat z_1+27w_2.
$$


Set


$$
V^{(0)}=e_d+3z_0+9\widehat z_1,
\qquad
e^{(0)}=\upsilon_T-\mathcal S_HV^{(0)}=27r_2.
$$



The exact force is


$$
\begin{aligned}
r_2={}&
\frac{\delta_{\rm raw}-G_c(Y,x^DP_*)-3G_c(Y,x^DP^{[1]})}{9}\\
&+\frac19\mathcal X^TM_L\alpha_d
+\frac13\mathcal X^TM_L\alpha_*
+\mathcal X^TM_L\alpha_{[1]}.
\end{aligned}
$$


At the required precision,


$$
r_2\equiv
\frac{\delta_{\rm raw}-G_c(Y,x^DP_*)-3G_c(Y,x^DP^{[1]})}{9}
+3^{23}R_d
\pmod{3^{24}}.
$$


The numerator is retained modulo $3^{26}$ before division by $9$.

The $3^{23}R_d$ term becomes $3^{26}R_d$ in $e^{(0)}$. It is included in the actual LOW-return analysis above. In particular, it is not deleted because a later contraction vanishes.

### 8.1 Initial membership

The weights show


$$
V^{(0)}\in\mathscr B.
$$


For example,


$$
3z_0=3\mathsf T_{0,3^{23}}-\mathsf Q_{1,0},
$$


and the $9\widehat z_1$ terms use grid indices


$$
3^{22},\quad2\cdot3^{22},\quad4\cdot3^{22},\quad3^{23},
$$


together with $\mathsf Q_{2,0}$ and $\mathsf Q_{0,0}$. All these grid indices lie in $[0,C_\circ]$.

### 8.2 Exact finite lifting identities

For $0\le j<24$, define algebraically


$$
V^{(j+1)}=V^{(j)}+\mathcal K_He^{(j)},
\qquad
e^{(j)}=\upsilon_T-\mathcal S_HV^{(j)}.
$$


Then


$$
e^{(j+1)}=(I-\mathcal S_H\mathcal K_H)e^{(j)}.
$$


Since $\mathcal S_H\mathcal K_H\equiv I\pmod3$,


$$
e^{(j)}\in3^{j+3}\mathscr V.
$$



Inductively,


$$
\mathcal K_He^{(j)}
=
\mathcal K_H\upsilon_T-\mathcal A V^{(j)}
\in\mathscr N,
$$


and hence


$$
V^{(j)}\in\mathscr N,
\qquad
(\mathcal K_He^{(j)})^Tf_H\in3^{27}\mathbb Z_3.
$$



Define


$$
d_j=\frac{\mathcal K_He^{(j)}}{3^{j+3}}.
$$


This division is paid by the residual depth. Dividing the **whole** contraction gives


$$
\boxed{d_j^Tf_H\in3^{24-j}\mathbb Z_3.}
$$



### 8.3 The witness and every division

Set


$$
\boxed{
z_2=\frac{V^{(24)}-V^{(0)}}{27}
=\sum_{j=0}^{23}3^j d_j.
}
$$


Every summand defining $V^{(24)}-V^{(0)}$ is divisible by $27$, so $z_2$ is integral.

Since $e^{(24)}\in3^{27}\mathscr V$,


$$
\boxed{
\mathcal S_H(V^{(0)}+27z_2)-\upsilon_T\in3^{27}\mathscr V.
}
$$


Also,


$$
3^j d_j^Tf_H\in3^{24}\mathbb Z_3
$$


for every $0\le j<24$, so


$$
\boxed{z_2^Tf_H\in3^{24}\mathbb Z_3.}
$$



The witness is a finite algebraic identity. It is not a proposal to execute original-sized vector updates. Its scalar is evaluated by the proved annihilator, not left as an unevaluated matrix pairing.

### 8.4 Actual scalar

Because $M_H$ is integral,


$$
M_He^{(24)}=27(w_2-z_2)
$$


implies


$$
w_2-z_2\in3^{24}\mathscr V.
$$


Since $f_H$ is integral,


$$
\boxed{w_2^Tf_H\equiv0\pmod{3^{24}}.}
$$



Moreover,


$$
w:=M_H\upsilon_T
$$


satisfies


$$
w-V^{(24)}\in3^{27}\mathscr V,
$$


so


$$
\boxed{w\in\mathscr N,\qquad w^Tf_H\in3^{27}\mathbb Z_3.}
$$



The previous nonzero $r_2$ edge is compatible with all of this: it says the starting residual has exact depth $3$, not that its subsequent full corrections cannot have annihilating contractions.

---

## 9. Audit of the A1 Turn 13 endpoint interface

### 9.1 Prefix normalization and finite boundaries — PASS

Retain


$$
R_*=\frac{9Q+1}{2},\quad a_0=R_*-1,\quad
\tau=\frac{N_0-3}{2},\quad \ell=3R+1,
$$




$$
K=\{0,\ldots,3R\},\qquad J=\{\ell,\ldots,\tau-1\},
\qquad R_*+\tau=\nu.
$$


Write $T=\tau-1$, and


$$
F_T=F[y^{\nu-1}].
$$



The normalized prefix matrix and source are


$$
\mathsf A=-\frac{G_c(F_{\rm pref},F_{\rm pref})}{3^{26}},
\qquad
q[p]=-\frac{G_c(F_{\rm pref},F[p])}{3^{27}}.
$$


The exact prefix correction is


$$
\widehat F[p]=F[p]-3F_{\rm pref}\mathsf A^{-1}q[p].
$$



For the one-lift,


$$
d_i=\frac{G_c(F_{\rm pref},\mathcal F[H_i])}{3^{28}},
\qquad Z_i=\mathsf A^{-1}d_i,
$$


and


$$
K_i=\mathcal F[H_i]+9F[Z_i].
$$


Indeed,


$$
G_c(F_{\rm pref},K_i)
=
3^{28}d_i-9\cdot3^{26}\mathsf A Z_i=0.
$$



The factor $9$ is therefore exact and necessary.

### 9.2 The finite terminal equation and residual polynomial — PASS

The leading finite bordered inverse retains its true last row. Its evaluated interior inverse image is represented by


$$
\mathcal T_i(y)=y^{131P}(1+y^P+y^{2P})z_i(y),
\qquad
z_i=(1-y)^t y^i.
$$


Its support is wholly in the original $J$-interior.

The exact terminal equation gives


$$
a\eta_i
=
-\frac{
G_c(\widehat F_T,K_i-9\widehat F[\mathcal T_i])
}{3^{29}}
\pmod3.
$$


The signs agree with


$$
a\eta_i=\theta_i-w^TX_i.
$$



Both columns in the second argument are exactly prefix-orthogonal. Thus $\widehat F_T$ may be replaced by $F_T$ in this pairing.

Now


$$
-9\widehat F[\mathcal T_i]
=
-9F[\mathcal T_i]
+27F_{\rm pref}\mathsf A^{-1}q[\mathcal T_i].
$$


Since


$$
G_c(F_T,F_{\rm pref})\in3^{27}M,
$$


the additional term contributes in $3^{30}$.

Likewise, replacing $Z_i$ by its established leading lift


$$
\overline Z_i
=
2(y^{14P}+y^{41P}+y^{95P})(1+y^P+y^{2P})z_i
$$


changes $9F[Z_i]$ by $27$ times an integral prefix column. Its terminal pairing is again in $3^{30}$.

The one-lift polynomial is exactly


$$
z_i(1-y)^{2P}(y^{122P}+3y^{41P}).
$$


Substitution therefore gives


$$
\boxed{
a\eta_i
=
-\frac{G_c(F_T,F[\Omega_Pz_i])}{3^{29}}
\pmod3.
}
$$


The numerator is in $3^{29}$, because it differs by a term in $3^{30}$ from the already normalized terminal equation.

No ordinary-column compression theorem has been applied to $F_T$. The lower $3y^{41P}$ source is retained in $\Omega_P$; where prefix orthogonality is used, it is exact orthogonality, not deletion of a coefficient.

### 9.3 Complete projection formula — PASS

Put


$$
g_T=G_c(W,x^Dy^{\nu-1}),
\qquad
b_i=G_c(W,x^D\Omega_Pz_i).
$$


Expanding both complete corrected columns gives the exact identity


$$
\boxed{
G_c(F_T,F[\Omega_Pz_i])
=
G_c(x^Dy^{\nu-1},x^D\Omega_Pz_i)
-g_T^TE_c^{-1}b_i.
}
$$



The entire $W$-return is present, including the physical $Y_m$. The inverse allowance is the actual


$$
E_c^{-1}\in3^{-1}M(\mathbb Z_3),
$$


not an integral-inverse substitution.

### 9.4 Bare endpoint cancellation — PASS

At $i=0$ and $i=k-1$, the two beta tops are


$$
H+D+t=(3^{32}+805)\Pi,
$$




$$
H+D+t+2P=(3^{32}+811)\Pi.
$$


Both have valuation


$$
h-33=S-1.
$$



The actual rational degree is at most


$$
H+535P+4\chi-3<K_{\rm phys},
$$


and its largest denominator is below $3H=3^h$. Thus every active pole weight has valuation at least $1$.

A pole visible modulo $3^{30}$ has odd denominator $\rho$ with


$$
v_3(\rho)\ge h-29.
$$


For a source macro-shift $bP$, the binomial index is


$$
r=
\frac{\rho-(268+2b)P+3}{2}
-\chi-i-\epsilon.
$$



At $i=0$,


$$
v_3(r)=
\begin{cases}
1,&\epsilon=0,\\
0,&\epsilon=1.
\end{cases}
$$


At $i=k-1=3\chi-\Pi-2$,


$$
r\equiv\frac72-4\chi-\epsilon\pmod\Pi,
$$


so $v_3(r)=0$ in both channels.

For an in-range nonzero coefficient,


$$
\binom Nr=\frac Nr\binom{N-1}{r-1}
$$


therefore gives valuation at least $h-34$ in the weakest case. The pole weight adds one digit, giving at least $h-33\ge30$. Out-of-range coefficients are zero. Inactive poles and the factorial part are already in $3^{30}$.

Hence


$$
\boxed{
G_c(x^Dy^{\nu-1},x^D\Omega_Pz_i)\in3^{30}\mathbb Z_3,
\qquad i=0,\ k-1.
}
$$



Combining the three audited identities gives


$$
\boxed{
\eta_i
=
a^{-1}\frac{g_T^TE_c^{-1}b_i}{3^{29}}
\pmod3,
\qquad i=0,\ k-1.
}
$$


The quotient is integral. Its integrality is proved by the prefix-returned identity and bare cancellation, rather than assumed.

---

## 10. New paid interface lemma: the complete $W$-return at $i=0$

The following supplies an explicit source-specific payment of the inherited interface. It does not require another LOW48 calculation.

Define


$$
\alpha_T=\frac{G_c(U,x^Dy^{\nu-1})}{3},
\qquad
f_L=\frac{G_c(U,x^Dp_0)}9.
$$


Thus


$$
g_T=\binom{3\alpha_T}{3\upsilon_T},
\qquad
b_0=\binom{9f_L}{9f_H}.
$$



### Lemma 10.1 — Joint source-return payment

For these actual sources,


$$
f_L\in3^{24}\mathbb Z_3^D,
$$




$$
M_H\mathcal X^TM_L\alpha_T\in3^{25}\mathscr E,
$$


and


$$
\boxed{
\mathscr N^T\mathcal X^TM_Lf_L
\subseteq3^{29}\mathbb Z_3.
}
$$



#### Proof

**LOW source depth.** In monomial LOW coordinates, a source term has


$$
N=H+t+\Delta,\qquad q=u+bP+\epsilon,\quad 0\le u<D.
$$


Here


$$
N-H+q
\le
\left(268+\frac13+b+\frac{\Delta}{P}\right)P
\le\left(401+\frac13\right)P.
$$


All indicators above level $S+6$ are absent. There are at most $S+6$ indicators in total. After the scale $3^{S+30}$,


$$
v_3(f_L)\ge24.
$$


The factorial part is deeper.

**Terminal LOW two-digit jet.** The terminal LOW force satisfies $\alpha_T\in3^{25}$. After extracting $3^{25}$, its beta part can be visible modulo $9$ only when the beta argument has grade $13$. Since $\nu-1\equiv25$,


$$
\alpha_T/3^{25}
\in
\mathscr U_{15}+3\mathscr U_{14}+9\mathbb Z_3^D,
$$


where $\mathscr U_b$ denotes monomial LOW support of grade $b$.

From


$$
\mathcal L_y=L_0+3L_1\pmod9
$$


with reflection grades $13,12$, finite inversion gives


$$
M_{L,y}=M_0+3M_1\pmod9
$$


with reflection grades $13,14$. Therefore


$$
\mathcal K_H\mathcal X_y^TM_{L,y}
$$


has reflection grade $13$ at order zero and reflection grade $14$ at order one. It follows that


$$
\mathcal K_H\mathcal X^TM_L\alpha_T
\in
3^{25}(\mathscr V_{25}+3\mathscr V_{26}+9\mathscr V)
\subseteq3^{25}\mathscr E.
$$



Since $\mathcal A\equiv I\pmod3$,


$$
\mathcal A^{-1}\equiv2I-\mathcal A\pmod9.
$$


The proved closure of $\mathscr E$ under $\mathcal A$ therefore also gives closure under $\mathcal A^{-1}$. Using


$$
M_H=\mathcal A^{-1}\mathcal K_H,
$$


we obtain


$$
M_H\mathcal X^TM_L\alpha_T\in3^{25}\mathscr E.
$$



**Pairing the complete LOW source return with $\mathscr B$.** For $v\in\mathscr B$, write its exact adaptation as


$$
V_v=x^DP+C.
$$


Then


$$
v^T\mathcal X^TM_Lf_L
=
\alpha[P]^TM_Lf_L+c^Tf_L.
$$


The first term lies in $3^{49}$.

For interior bulk seeds, $C=0$. For lower-mask seeds, $C$ lies in the weighted span of


$$
3^a C_{d+a},\qquad0\le a\le26.
$$


Section 4.7 proves


$$
c^Tf_L\in3^{29}.
$$


Thus


$$
\mathscr B^T\mathcal X^TM_Lf_L\subseteq3^{29}.
$$



Finally, the $3^{25}\mathscr E$ and $3^{27}\mathscr V$ parts of $\mathscr N$ pair with $\mathcal X^TM_Lf_L\in3^{24}\mathscr V$ in depths at least $49$ and $51$. This proves the lemma. ∎

### 10.2 Exact block expansion and the physical $3^{-1}$ loss

Block elimination gives


$$
\boxed{
\begin{aligned}
g_T^TE_c^{-1}b_0
={}&
9\alpha_T^TM_Lf_L\\
&+27(\upsilon_T-\mathcal X^TM_L\alpha_T)^T
M_H(f_H-\mathcal X^TM_Lf_L).
\end{aligned}
}
$$


The factor $9$ in the first term is exactly


$$
3\cdot\frac13\cdot9.
$$


Thus the physical LOW inverse loss has been paid explicitly.

Put


$$
w=M_H\upsilon_T,\qquad
v_T=M_H\mathcal X^TM_L\alpha_T.
$$


The established bounds are


$$
w\in\mathscr N,\qquad w^Tf_H\in3^{27},
$$




$$
v_T\in3^{25}\mathscr E,\qquad v_T^Tf_H\in3^{27},
$$




$$
w^T\mathcal X^TM_Lf_L\in3^{29},
\qquad
v_T^T\mathcal X^TM_Lf_L\in3^{49}.
$$



The complete valuation ledger is therefore

| Term in $g_T^TE_c^{-1}b_0$ | Lower bound |
|---|---:|
| $9\alpha_T^TM_Lf_L$ | $51$ |
| $27w^Tf_H$ | $30$ |
| $-27v_T^Tf_H$ | $30$ |
| $-27w^T\mathcal X^TM_Lf_L$ | $32$ |
| $27v_T^T\mathcal X^TM_Lf_L$ | $52$ |

Hence


$$
\boxed{g_T^TE_c^{-1}b_0\in3^{30}\mathbb Z_3.}
$$


The audited A1 Turn 13 formula now yields


$$
\boxed{\eta_0=0\in\mathbb F_3.}
$$



### 10.3 The inherited scalar interface is now fully justified

The same block calculation gives


$$
g_T^TE_c^{-1}b_0
\equiv27w^Tf_H\pmod{3^{30}}.
$$


Using


$$
w=e_d+3z_0+9\widehat z_1+27w_2,
$$


the weighted edge bound and the two accepted whole contractions imply


$$
g_T^TE_c^{-1}b_0
\equiv3^6w_2^Tf_H\pmod{3^{30}}.
$$


Before evaluating the scalar, the already proved integrality of


$$
g_T^TE_c^{-1}b_0/3^{29}
$$


therefore gives


$$
w_2^Tf_H\in3^{23}\mathbb Z_3.
$$


Dividing the congruence by $3^{29}$ yields exactly


$$
\boxed{
a\eta_0=\frac{w_2^Tf_H}{3^{23}}\pmod3.
}
$$



Thus both the identity and its divisibility premise are paid in the original core objects. The zero modulo $3^{24}$ proved in Section 8 then gives the endpoint value.

This is the requested repair of the earlier conditional presentation of the interface. It is source-specific, retains every block return, and uses no arbitrary-matrix counterexample.

---

## 11. Consolidated audit and precision ledger

### 11.1 Verdicts

| A1 Turn 18 claim or dependency | Verdict |
|---|---|
| Original safe-grid inequalities | **PASS** |
| Interior seed support at both HIGH boundaries | **PASS** |
| Exact $v=0$ lower masks | **PASS** |
| Inner mask identity | **PASS**, with the dangerous interval explicitly excluded |
| Fourteen-source residual bounds | **PASS** |
| Terminal and ordinary beta counts | **PASS**; the explicit bound is $55<81$ |
| Every finite quotient coefficient and weight | **PASS** |
| Weighted lower-edge estimates | **PASS** |
| Both $\beta/3y$ channels | **PASS** |
| Physical cutoff and factorial payment | **PASS** |
| Integral $\mathcal K_H$, inverse only modulo $3$ | **PASS** |
| Actual two-digit Schur grading | **PASS**, including LOW matrix feedback |
| Exceptional pairing and closure | **PASS** |
| Exact LOW adaptation | **PASS** |
| Bulk LOW depth and leading return grades | **PASS** |
| Upper $3H$ moment indicator | **PASS**, retained |
| Finite coarse transition | **PASS**, not an infinite replacement |
| Complete fine transition, including both clipped edges | **PASS** |
| Complete normalized terminal source | **PASS**; excluded resonance is not divided |
| $\mathcal K_H\upsilon_T\in\mathscr N$, $\mathcal A\mathscr N\subseteq\mathscr N$ | **PASS** |
| All full residual corrections | **PASS** |
| Precision-$27$ certificate | **PASS** |
| $w_2^Tf_H\bmod3^{24}$ | **Evaluated as $0$** |
| A1 Turn 13 residual identity (5.3) | **PASS** |
| Complete projection formula (5.7) | **PASS** |
| Bare endpoint cancellation | **PASS** |
| Complete return relation (6.10) | **PASS**, with integrality proved |
| Core $\eta_0$ interface | **Closed by the additional paid return lemma** |
| Transfer to $Q_{\rm act}$ or physical $7$ | **Not proved and not inferred** |
| Alternate endpoint, first-$4$, higher ternary audit | **Separate open obligations** |
| Primitive denominator or global irrationality conclusion | **Not obtained** |

No substantive false theorem was found in the new uniform annihilator argument.

### 11.2 Divisions and required pre-division precision

| Quantity | Division | Required information |
|---|---:|---|
| $\upsilon_T\bmod3^{27}$ | $3$ | terminal pairing modulo $3^{28}$ |
| $f_H\bmod3^{24}$ | $9$ | whole source pairing modulo $3^{26}$ |
| $r_2\bmod3^{24}$ | $9$ | its complete numerator modulo $3^{26}$ |
| Fine kernel two-digit jet | $3^{25}$ | kernel modulo $3^{27}$ |
| Terminal beta fine jet | an additional $3$ | kernel modulo $3^{28}$ |
| $d_j$ | $3^{j+3}$ | actual residual depth $j+3$, whole pairing depth $27$ |
| $z_2$ | $27$ | cumulative difference divisible by $27$ |
| $w_2-z_2\bmod3^{24}$ | $27$ | certificate residual modulo $3^{27}$ |
| Prefix terminal identity | $3^{29}$ | complete pairing modulo $3^{30}$ |
| Leading prefix-image replacement | error factor $9\cdot3$ | terminal-prefix pairing in $3^{27}$ |
| Physical LOW inverse | $3$ | retained explicitly in the block expansion |
| Endpoint scalar | $3^{23}$ | actual $w_2^Tf_H\bmod3^{24}$ |

---

## 12. What remains separate

### 12.1 Alternate endpoint and first-$4$ return

The bare cancellation at $i=k-1$ is proved, but the present endpoint conclusion is for $i=0$. It must not be transferred merely by changing a displayed exponent.

A concrete next source is already specified:


$$
p_{\rm alt}=\Omega_P(y)(1-y)^t y^{k-1}.
$$


Its complete return is


$$
g_T^TE_c^{-1}G_c(W,x^Dp_{\rm alt}).
$$


A source-specific follow-on lemma should establish the corresponding weighted bulk contractions and normalized LOW-source returns for this polynomial. The two endpoint sources must remain distinct throughout that proof.

The physical-$6$ assembly remains


$$
C_6=C^{\rm mom}
-\bigl(e_{k-1}\eta^T+\eta e_{k-1}^T\bigr)-R_4\pmod3.
$$


The first-$4$ mixed-prefix return remains


$$
P_{ui}=\frac{d_u^T\mathsf A^{-1}d_H{}_i}{3}\pmod3,
$$


with


$$
(C_H)_{ui}
=
-c_{P-1-u-i-\Pi}
+c_{P-1-u-i-2\Pi}
-2\mathbf1_{u=R,\ i=k-1}
-P_{ui}.
$$


The actual finite $A_4^{-1}$ in


$$
R_4=C_H^TA_4^{-1}C_H
$$


has not been replaced.

The later directional allowance remains


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^{k-1}.
$$


Its higher digit is still necessary.

The diagonal payments remain


$$
\lambda_{\rm new}
=
\lambda^{\rm pref}
-\frac13f_J^TB^{-1}f_J
-\frac19f_b^TA_b^{-1}f_b
\in3^{-2}\mathbb Z_3,
$$




$$
\lambda_4
=
\lambda_{\rm new}
-\frac1{3^4}f_C^TA_4^{-1}f_C
\in3^{-4}\mathbb Z_3.
$$



The distinct higher ternary block audit remains open. This focused audit neither passes nor discards it.

### 12.2 Actual producer and complete forcing

The actual producer remains


$$
\boxed{Q_{\rm act}=Q_c+3^7\mathscr R.}
$$



Retain


$$
F_{\rm fac}=(n-1)!,
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},\qquad0\le a,b<n,
$$




$$
\gamma_0=1,\quad\gamma_1=0,\quad
\gamma_{r+1}=(4r+2)\gamma_r+4\gamma_{r-1},
$$




$$
h_{\rm vec}
=
T_n^{-1}
\left(\binom{n+a}{a}\gamma_{n+a}\right)_{a=0}^{n-1},
$$




$$
u_a=\frac{F_{\rm fac}(-2)^a}{a!},\qquad v=T_n^{-1}u,
$$




$$
b_{\rm force}=-n-66,
$$




$$
t_{\rm force}
=
3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
$$




$$
\xi=\frac{u^Tt_{\rm force}}{F_{\rm fac}^2-u^Tv}.
$$


The complete correction is


$$
[x^a](3^7\mathscr R)
=
-\frac{F_{\rm fac}}{a!}
\bigl((t_{\rm force})_a+\xi v_a\bigr),
\qquad0\le a\le n-1,
$$


and


$$
\mathscr R(-1)=-\frac{\xi F_{\rm fac}^2}{3^7}.
$$



The full forcing identity remains


$$
\boxed{
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
}
$$


Neither forcing term is removed.

The complete moment recurrence remains


$$
\mu_{r+1}+\mu_r
=
\frac{3^h}{2r+1}
-\frac{3^h}{4}\bigl((2r+2)!+(2r)!\bigr),
\qquad0\le r\le2n-2.
$$


The later construction’s designated index


$$
r_*=\frac{3^h-5}{2}
$$


and its separate division obligations are retained. It is not identified with $r_H$ or with the pole index $(3^h-1)/2$ of the displayed denominator.

Actual/core transport, source precision $34$, and the physical-$5$ complementary and kernel-pivot returns remain necessary for physical $7$.

---

## 13. Actual contents, least clearer, final gcd, and whole error

No actual integer column content is evaluated by the core cancellation. Temporary LOW coordinate changes do not redefine those contents.

The least simultaneous clearer remains the actual $\ell_{\rm clr}$, not a convenient common multiple and not a power of $3$. Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final gcd over **all primes**


$$
\boxed{G=\gcd(|A_\ell|,|B_\ell|).}
$$



For $B_\ell\ne0$, the actual primitive pair is


$$
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{G},
\qquad
q=\frac{|B_\ell|}{G}.
$$


The whole evaluated error remains


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{G}
\det H_{\rm complete}.
}
$$



An irrationality proof still requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\boxed{
\log G-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|
\longrightarrow+\infty.
}
$$


These conditions would make the nonzero whole errors tend to zero. If $e+\pi=a/b$ were rational, every such nonzero integer linear error would have absolute value at least $1/b$.

The local core annihilator proves none of these nonvanishing, all-prime normalization, or real-decay assertions.

---

## 14. Bounded arithmetic and final proof status

No new indispensable arithmetic execution is required by this report. The proofs above are symbolic and uniform.

An optional independent bookkeeping check can have only the following fixed inputs:

* offsets $0\le a\le27$ and channels $\epsilon=0,1$;
* the fourteen triples in Section 4.1;
* residues $D=0,\nu=26,r_H=13\pmod{27}$;
* the displayed seed weights;
* the rational interval $3/25<\chi/P<31/250$, with $P\ge3^{31}$.

Its expected verifiable outputs are:

1. the maximum relevant fixed odd absolute value is $55$, and the maximum valuation is $3$;
2. $v_3(2a+2\epsilon-1)\le a+\epsilon$ throughout the stated ranges;
3. all fourteen residual bounds are below $540P$;
4. exactly the seven fine seed types listed in Section 7.4 survive after extracting $3^{25}$ modulo $9$;
5. the exceptional grades are closed under the paid shift and are disjoint from source grades $12,13$;
6. the three safe-grid upper margins and the finer-grid inequalities are positive.

Such a check verifies only that bounded bookkeeping. It is not the proof of uniform annihilation, the finite transition theorem, or the same-index global error criterion.

No old $729$-position table, LOW48 solve, resonant-unit receipt, original factorial matrix, or original-length inverse computation is requested.

---

## Conclusion

The new uniform finite annihilator in A1 Turn 18 is valid at its stated core scope. Its whole-source and actual-operator properties are


$$
\mathscr B^Tf_H\subseteq3^{29}\mathbb Z_3,
$$




$$
\mathscr E^Tf_H\subseteq9\mathbb Z_3,
\qquad
\mathcal A\mathscr E\subseteq\mathscr E,
$$




$$
\mathcal K_H\upsilon_T\in\mathscr N,
\qquad
\mathcal A\mathscr N\subseteq\mathscr N.
$$


They pay every remaining full residual correction and prove


$$
\boxed{w_2^Tf_H\equiv0\pmod{3^{24}}.}
$$



The additional proved result of this report is the complete interface payment


$$
\boxed{
\mathscr N^T\mathcal X^TM_Lf_L\subseteq3^{29}\mathbb Z_3,
\qquad
g_T^TE_c^{-1}b_0\in3^{30}\mathbb Z_3.
}
$$


Together with the independently inspected prefix-returned identity and bare cancellation, this makes


$$
\boxed{\eta_0=0\in\mathbb F_3}
$$


an unconditional result in the original sufficiently large **core** construction, rather than a conclusion resting on an unpaid interface premise.

The remaining local obligations are the alternate endpoint with its complete source return, the first-$4$ return, the separate higher ternary audit, and the actual physical-$7$/source-$34$ calculation. The global bottleneck remains the actual contents, least simultaneous clearer, all-prime final gcd, actual primitive denominator, and a nonzero whole error tending to zero at the same infinite original indices.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi\text{ is obtained.}}
$$


