> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A complete-source nine-period annihilation and the first terminal return

## Abstract

The requested complete-source directional estimate


$$
Cw=z,\qquad w\in 3^{-1}\mathbb Z_3^{\,b/2},
$$


is **not proved in this report**. Nor is the complete relative determinant pair evaluated. In particular, no conclusion about the rationality or irrationality of $e+\pi$ follows.

There is, however, a new quantitative statement on the unchanged original matrices. It uses the actual producer coefficients, the complete moment functional, the exact corrected columns, and the supplied precision-$20$ support theorem:

> On a fixed infinite original subfamily, let $G$ have columns
> 

$$
> (y-1)^b y^a,\qquad 0\le a\le b/2,
>
$$


> in the original coordinates $R_*+K$. Then
> 

$$
> \boxed{
> \mathcal M(\mathscr R F_{G,a}\Delta)\in27\mathbb Z_3
> \quad\text{for every integral }\deg\Delta\le m,
> }
>
$$


> and consequently
> 

$$
> \boxed{
> G^T(S_{\rm act}-S_c)_{R_*+K,R_*+K}G
> \in3^{30}M.
> }
>
$$



Here $F_{G,a}$ is a linear combination of the **exact complete-core corrected columns**, not of freely chosen model columns. The assertion holds independently of the pending precision-$29$ identification H2; H2 is needed only to identify these vectors as the full second radical of the actual reduction.

The mechanism is explicit. The next complete mixed observation is a nine-period coefficient functional determined by ten actual top producer coefficients. The displayed $G$-columns annihilate that functional because


$$
(y-1)^b\equiv0\pmod{y^9-1}
\quad\text{over }\mathbb F_3.
$$


No vanishing of the terminal coefficient vector $t$ is used.

The first returning producer term can also be simplified on the actual finite $J$-block. Its physical terminal satisfies


$$
\boxed{
\bar B^{-1}\delta_J=-e_0,\qquad
\delta_J^T\bar B^{-1}\delta_J=0.
}
$$


Thus the quadratic term in the first return is one digit deeper than the general formula permits. After the new direct-source cancellation, the remaining matrix return is an explicit rank-at-most-two expression involving the actual terminal coefficient and one actual complete-core boundary column. That boundary column has not yet been evaluated.

Finally, the complete finite moment recurrence has an actual resonant step requiring a division by $3^h$, with no common coefficient factor that cancels it. This is an obstruction to an unpaid, uniformly stable recurrence-propagation argument—not a counterexample to the desired bound on $C^{-1}z$.

The new result is therefore a genuine source-level divisibility theorem, but only at a fixed additional digit. It does not yet reach a scale that changes the all-prime primitive-denominator versus whole-error comparison.

---

## 1. Original domain, finite objects, and proof dependencies

### 1.1 The unchanged original indices

Retain


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=n-2=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


and


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



Write $x=y-1$. The finite coordinates are still


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_a=y^a\quad(d\le a\le m),
\qquad
\nu=\frac D2-1,\qquad d=D+\nu.
$$


The physical HIGH terminal remains $Y_m$.

For definiteness, choose the fixed interior subwindow


$$
\boxed{\frac{103}{1000}<\rho:=\frac{N_0}{P_0}<\frac{104}{1000}.}
\tag{1.1}
$$


It lies strictly inside the turn12 window


$$
\frac1{10}<\rho<\frac{19}{180}.
$$



All the original relations are retained:


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1.
$$


The previously established original-index density result is reused only at its stated scope: fixed interior subwindows such as (1.1) contain infinitely many original indices. No auxiliary pair $(P,r)$ is substituted for an original $(j,h)$.

Set


$$
Q=\frac{P_0}{9},\qquad b=Q-N_0,\qquad
\ell=\frac{3b}{2}+1,
$$




$$
R_*=\frac{P_0+1}{2},\qquad
\tau=\frac{N_0-3}{2},\qquad
n_J=\tau-\ell=\frac{Q-4b-5}{2}.
$$


Then


$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\}.
$$


On the fixed subwindow, $b$ is a positive even multiple of $243$, and $n_J\to\infty$.

### 1.2 The complete functional and actual producer

The complete finite functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!.
\tag{1.2}
$$


It is used only on polynomials of degree at most $2n-1$. Its largest allowed pole denominator is


$$
4n-3=4H-4D+5.
$$



The complete core is


$$
G_c(f,g)=\mathcal M(Q_cfg),
\qquad
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A.
$$


The actual source is


$$
Q_{\rm act}=3P_n=Q_c+3^7\mathscr R.
\tag{1.3}
$$



The exact producer coefficients are


$$
3^7\mathscr R=\sum_{a=0}^{A+1}e_ax^a,
\qquad
e_a=-\frac{F}{a!}(t_a+\xi v_a),
\qquad F=(A+1)!,
\tag{1.4}
$$


with the complete force


$$
t=3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
\qquad b_{\rm force}=-n-66.
\tag{1.5}
$$


The recovered source gives $h_{\rm vec},v,t\in\mathbb Z_3^{\,n}$, and the retained signed scalar $\xi$ is a ternary unit after its already paid common division.

The exact endpoint charge is


$$
\boxed{\mathscr R(-1)=-\frac{\xi F^2}{3^7}.}
\tag{1.6}
$$



The original complete return is not changed:


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{1.7}
$$


In particular, the logarithmic force, exponential boundary charge, finite return, exterior constant, and physical-terminal contribution remain in the actual source.

### 1.3 Established results used, and the pending result not used

The new proof uses the following results at their supplied sufficiently-large original scope:

1. The exact complete-core corrected columns
   

$$
F=Z-WE_c^{-1}C_c,\qquad G_c(W,F)=0.
$$


2. The original bounds
   

$$
E_c^{-1},E_{\rm act}^{-1}\in3^{-1}M.
$$


3. The corrected-column representatives
   

$$
F_i^*=x^D\psi_i,\qquad F_i^*\equiv F_i\pmod{3^{20}},
$$


   with their strict degree gap below $m$ and their stated support envelope.
4. The complete jets
   

$$
F_i\equiv x^D
   \left(y^i-3\delta_iq_d-9y^{H/3+i}
   +9\delta_iq_{d+1}\right)\pmod{27},
   \qquad
   \delta_i=\mathbf1_{\{i=\nu-1\}}.
   \tag{1.8}
$$


5. The exact perturbation formula
   

$$
S_{\rm act}-S_c=3^7\Phi_{\mathscr R}-3^{13}\mathcal Q,
   \qquad
   \mathcal Q\in3^{21}M.
   \tag{1.9}
$$


6. The accepted first returning producer digit
   

$$
U_{\rm act}-U_c
   \equiv9\kappa(\delta t^T+t\delta^T)\pmod{27},
   \qquad
   U=-S/3^{26},
   \tag{1.10}
$$


   where
   

$$
t_i=\frac{[y^m]F_i}{3^{20}}.
$$


7. The accepted first-radical finite block and its $K\sqcup J$ boundary.

The precision-$29$ original identification H2 remains under A4 review. The new direct-source theorem below does **not** assume H2. The vectors involved exist in the original finite space whether or not H2 is eventually validated.

---

## 2. Two actual producer coefficient cutoffs

The coefficient estimates needed below are small consequences of the recovered exact producer, not new dense producer computations.

### 2.1 The endpoint charge is paid

Since $v_3(A)=5$, $A+1$ is a ternary unit, and $\xi$ is a unit,


$$
v_3\bigl(\mathscr R(-1)\bigr)=2v_3(F)-7.
$$


Legendre’s formula gives


$$
2v_3(F)=(n-1)-s_3(n-1),
$$


so


$$
v_3\bigl(\mathscr R(-1)\bigr)
=n-8-s_3(n-1).
\tag{2.1}
$$


This is much larger than $24$ on the retained sufficiently large family.

Put


$$
c=\mathscr R(-1),\qquad
D_{\rm prod}(y)=\frac{\mathscr R(y)-c}{y+1}.
$$


The division is monic. Thus $D_{\rm prod}\in\mathbb Z_3[y]$, with degree at most $A$.

The accepted producer reset gives


$$
D_{\rm prod}\equiv\kappa x^A\pmod3.
$$


Consequently the following is an **exact definition** of an integral polynomial:


$$
\boxed{
B_1=\frac{D_{\rm prod}-\kappa x^A}{3}\in\mathbb Z_3[y].
}
\tag{2.2}
$$


The additional division by $3$ is paid by the displayed congruence.

### 2.2 A nine-width source at the next mixed digit

For $a\le A-10$, the factorial quotient $F/a!$ contains $A,A-1,\ldots,A-9$. Because $9<3^5$,


$$
v_3(F/a!)\ge5+v_3(9!)=5+4=9.
$$


After the actual division by $3^7$,


$$
[x^a]\mathscr R\in9\mathbb Z_3\qquad(a\le A-10).
$$


Hence


$$
\mathscr R\bmod9
$$


is divisible by $x^{A-9}$.

Since $c\equiv0\pmod9$, and $x+2=y+1$ is coprime to $x$ over $\mathbb Z/9\mathbb Z$, monic division preserves this factor:


$$
D_{\rm prod}\equiv x^{A-9}p(x)\pmod9,\qquad \deg p\le9.
$$


Subtracting $\kappa x^A$ and paying (2.2) gives


$$
\boxed{
\bar B_1=\sum_{k=0}^{9}\eta_kx^{A-k}
\quad\text{in }\mathbb F_3[x].
}
\tag{2.3}
$$



These are actual producer coefficients. Explicitly, synthetic division gives


$$
\boxed{
\eta_k=
\overline{
\frac{
\displaystyle
\sum_{a=A-k+1}^{A+1}(-2)^{a-A+k-1}e_a
-3^7\kappa\,\mathbf1_{\{k=0\}}
}{3^8}
},
\qquad 0\le k\le9.
}
\tag{2.4}
$$


The entire numerator is divisible by $3^8$; the terms in it are not individually divided without that payment.

Formula (2.4) retains every term of (1.4)–(1.5), including $\xi v_a$. No value of $\eta_k$ is guessed.

### 2.3 A precision-$24$ coefficient cutoff

For $a\le A-55$,


$$
v_3(F/a!)\ge5+v_3(54!)=5+(18+6+2)=31.
$$


Therefore


$$
[x^a]\mathscr R\in3^{24}\mathbb Z_3.
$$


Using (2.1) and monic division once more,


$$
\boxed{
\mathscr R\equiv
(y+1)x^{A-54}q_{24}(x)\pmod{3^{24}},
\qquad \deg q_{24}\le54.
}
\tag{2.5}
$$


This is the same coefficient-width mechanism already used at precision $22$, now with its full available valuation recorded.

---

## 3. The complete finite moment recurrence

Let


$$
\mu_t=\mathcal M(y^t),\qquad 0\le t\le2n-1.
$$


The complete recurrence is


$$
\mu_0=-\frac{3^h}{4},
$$




$$
\boxed{
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\quad 0\le t\le2n-2.
}
\tag{3.1}
$$



For clarity, set


$$
\nu_t=\mu_t+\frac{3^h}{4}(2t)!.
$$


Then


$$
\nu_0=0,\qquad
\nu_{t+1}+\nu_t=\frac{3^h}{2t+1},
$$


and finite iteration yields


$$
\mu_t=
-\frac{3^h}{4}(2t)!
+
3^h\sum_{v=0}^{t-1}\frac{(-1)^{t-1-v}}{2v+1}.
\tag{3.2}
$$


This is an exact finite identity, with the original initial charge and factorial component present.

On the original degree range,


$$
2v+1\le4n-3<3^{h+1},
$$


so $v_3(2v+1)\le h$. Thus the factor $3^h$ pays every ternary pole denominator. In particular,


$$
\mathcal M:\mathbb Z_3[y]_{\le2n-1}\longrightarrow\mathbb Z_3.
\tag{3.3}
$$



At any precision below $h$, the factorial term may be omitted **only after** its factor $3^h$ has been recorded. It has not been removed from the functional.

---

## 4. A new complete mixed observation modulo $27$

### Theorem 4.1

Let $i\le\nu-2$, so that $\delta_i=0$, and let $\Delta\in\mathbb Z_3[y]$ have degree at most $m$. Put


$$
r_H=\frac{H-1}{2}.
$$


Then


$$
\boxed{
\mathcal M(\mathscr R F_i\Delta)
\equiv
9[y^{r_H-i}]\,B_1x^D\Delta
\pmod{27}.
}
\tag{4.1}
$$



This includes $\Delta=Y_m$.

### Proof

Because $\delta_i=0$, (1.8) gives


$$
F_i\equiv x^D(y^i-9y^{H/3+i})\pmod{27}.
$$


Equations (2.1)–(2.2), together with complete integrality, allow the endpoint-zero model


$$
\frac{\mathscr R F_i\Delta}{y+1}
\equiv
\kappa x^Hy^i\Delta
+3B_1x^Dy^i\Delta
-9\kappa x^Hy^{H/3+i}\Delta
\pmod{27}.
\tag{4.2}
$$


All displayed model polynomials remain inside the original functional cutoff.

Since $i\le\nu-2$,


$$
i+m\le r_H-2<r_H.
\tag{4.3}
$$



We now evaluate every pole layer that can survive modulo $27$.

#### Unit-weight pole

The only pole of weight a ternary unit has denominator $3H=3^h$, at


$$
r_{3H}=\frac{3H-1}{2}.
$$


The first two terms of (4.2) have degree below $r_{3H}$, because $\deg B_1\le A$ and (4.3) holds.

For the third term, use


$$
x^H\equiv y^H-1\pmod3.
$$


Only its upper term can reach $r_{3H}$. Its contribution is


$$
-9\kappa[y^{d_i}]\Delta,
\qquad
d_i=\frac{H/3-1}{2}-i.
\tag{4.4}
$$



#### Weight-$3$ pole

The only pole of exact weight valuation one has denominator $H$, at $r_H$.

For a power $H$ of $3$,


$$
x^H\equiv y^H-1+3y^{H/3}-3y^{2H/3}\pmod9.
\tag{4.5}
$$


Indeed, writing $x^{H/3}=y^{H/3}-1+3R$ and cubing proves (4.5).

By (4.3), only $3y^{H/3}$ contributes from the first term of (4.2). Its weighted contribution is


$$
+9\kappa[y^{d_i}]\Delta,
$$


which cancels (4.4).

The $3B_1$-term contributes precisely


$$
9[y^{r_H-i}]B_1x^D\Delta.
\tag{4.6}
$$



#### Weight-$9$ poles

The denominators of exact valuation $h-2$ within the original cutoff are


$$
\frac H3,\quad \frac{5H}{3},\quad \frac{7H}{3},\quad \frac{11H}{3}.
$$


Only the leading term $\kappa x^Hy^i\Delta$ matters.

The first and third of these poles give respectively


$$
-9\kappa[y^{d_i}]\Delta,
\qquad
+9\kappa\,7^{-1}[y^{d_i}]\Delta.
$$


Since $7^{-1}\equiv1\pmod3$, they cancel. The other two extractions are outside the support allowed by (4.3).

All remaining pole weights are divisible by $27$. The complete factorial contribution is divisible by $3^h$, hence by $27$.

The sole surviving contribution is (4.6). ∎

This calculation is specific to the complete original source. In particular, the cancellation uses both the order-two corrected-column jet and all four weight-$9$ poles.

---

## 5. Evaluation as a nine-period functional

For $i=R_*+u$, $u\in K$,


$$
r_H-i=m+\nu-i=m+\tau-u.
$$


Thus


$$
r_H-i-m\ge n_J+1.
\tag{5.1}
$$


For sufficiently large original indices, the right side is at least $9$.

Define the actual polynomial


$$
\boxed{
\mathcal B_9(y)
=
\sum_{k=1}^{9}(-1)^{k+1}\eta_k(1-y)^{9-k}
\in\mathbb F_3[y],
\qquad \deg\mathcal B_9\le8.
}
\tag{5.2}
$$



The $k=0$ term of (2.3) contributes nothing in (4.1), because its low-degree part is constant and the extraction index exceeds $\deg\Delta$. For $k\ge1$, at indices below $H$,


$$
x^{H-k}
=\frac{y^H-1}{(y-1)^k}
\equiv
(-1)^{k+1}(1-y)^{-k}
$$


for the relevant low coefficient extraction.

In characteristic $3$,


$$
(1-y)^{-k}=\frac{(1-y)^{9-k}}{1-y^9}
\qquad(1\le k\le9).
$$


Consequently Theorem 4.1 becomes


$$
\frac{\mathcal M(\mathscr R F_i\Delta)}9
\equiv
[y^{r_H-i}]
\frac{\mathcal B_9(y)\bar\Delta(y)}{1-y^9}
\pmod3.
\tag{5.3}
$$



Because of (5.1),


$$
r_H-i>\deg(\mathcal B_9\bar\Delta).
$$


Therefore the coefficient in (5.3) is exactly the coefficient in the indicated residue class of the finite remainder:


$$
\boxed{
\frac{\mathcal M(\mathscr R F_i\Delta)}9
\equiv
[y^{\,r_H-i\bmod9}]
\bigl(\mathcal B_9(y)\bar\Delta(y)\bmod(y^9-1)\bigr).
}
\tag{5.4}
$$



Thus, for fixed $\Delta$, the normalized mixed observation is a nine-period function of the original index $i$. This is an evaluated finite functional, not an unevaluated new contraction.

### Theorem 5.1 — Actual nine-period annihilation

Let


$$
g(y)=\sum_{u=0}^{\ell-1}g_uy^u\in\mathbb Z_3[y],
$$


and suppose


$$
\bar g\equiv0\pmod{y^9-1}.
$$


Define the exact corrected combination


$$
F_g=\sum_{u=0}^{\ell-1}g_uF_{R_*+u}.
$$


Then


$$
\boxed{
\mathcal M(\mathscr R F_g\Delta)\in27\mathbb Z_3
\quad\text{for every }\deg\Delta\le m.
}
\tag{5.5}
$$



#### Proof

By (5.4), the normalized sum is a cyclic coefficient of


$$
\bar g(y)\mathcal B_9(y)\bar\Delta(y)
\quad\bmod(y^9-1).
$$


That remainder is zero. ∎

Now take


$$
g_a=(y-1)^by^a,\qquad 0\le a\le b/2.
\tag{5.6}
$$


Since $b\ge9$,


$$
y^9-1=(y-1)^9
$$


divides $\bar g_a$. Also


$$
\deg g_a\le b+b/2=\ell-1.
$$


Thus all these vectors belong to the exact original finite $K$-space, and Theorem 5.1 applies to them.

Notice what has **not** been asserted:

* $F_g$ has not been replaced by $F_g^*$;
* $[y^m]F_g/3^{20}$ has not been set to zero;
* $F_g(-1)$ has not been replaced by a Jacobi endpoint;
* the original physical terminal has not been removed.

---

## 6. A new precision-$30$ direct producer bound

### 6.1 The model estimate reaches precision $23$

Use the established representatives $F_i^*=x^D\psi_i$. By (2.5),


$$
\mathscr R F_i^*F_j^*
\equiv
(y+1)x^H
\left(x^{D-54}q_{24}(x)\psi_i\psi_j\right)
\pmod{3^{23}}.
\tag{6.1}
$$


The polynomial in parentheses has the same retained support envelope as in the accepted precision-$22$ model calculation:


$$
\Omega_{20}\mathbb Z+[-21D,21D].
$$



At precision $23$, put


$$
\Lambda_{23}=\frac H{3^{22}}=81P_0.
$$


Since $\Omega_{20}=27\Lambda_{23}$, the binomial grid and the support envelope combine into


$$
\Lambda_{23}\mathbb Z+[-21D,21D].
$$


On (1.1),


$$
\frac{\Lambda_{23}}D=\frac{81}{1+\rho}>73.
$$


Hence


$$
21D<\frac{\Lambda_{23}-1}{2}.
\tag{6.2}
$$



Every pole that can contribute modulo $3^{23}$ has its extraction index on the odd half-grid relative to $\Lambda_{23}$. Inequality (6.2) excludes all such extractions. The factorial term retains its factor $3^h$.

Therefore


$$
\boxed{
\mathcal M(\mathscr R F_i^*F_j^*)\in3^{23}\mathbb Z_3.
}
\tag{6.3}
$$



No support theorem beyond precision $20$ has been used.

### 6.2 Transfer to the exact columns

For $g$ as in Theorem 5.1, write


$$
F_g^*=F_g+3^{20}\Delta_g,\qquad \deg\Delta_g\le m.
$$


The division by $3^{20}$ is paid by the supplied congruence.

For two such vectors $g,h$,


$$
\begin{aligned}
\mathcal M(\mathscr R F_g^*F_h^*)
={}&\mathcal M(\mathscr R F_gF_h)\\
&+3^{20}\mathcal M\bigl(\mathscr R(F_g\Delta_h+F_h\Delta_g)\bigr)\\
&+3^{40}\mathcal M(\mathscr R\Delta_g\Delta_h).
\end{aligned}
$$


Theorem 5.1 pays both linear terms by $3^{23}$. Complete integrality pays the quadratic term. Equation (6.3) therefore proves


$$
\boxed{
\mathcal M(\mathscr R F_gF_h)\in3^{23}\mathbb Z_3.
}
\tag{6.4}
$$



Let $G$ be the integral matrix whose columns are (5.6). Applying the exact perturbation formula (1.9),


$$
3^7G^T\Phi_{\mathscr R}G\in3^{30}M,
$$


while


$$
3^{13}G^T\mathcal QG\in3^{34}M.
$$


We obtain the announced theorem:


$$
\boxed{
G^T(S_{\rm act}-S_c)_{R_*+K,R_*+K}G
\in3^{30}M.
}
\tag{6.5}
$$



Equivalently, in the normalized matrices,


$$
\boxed{
G^T(U_{\rm act}-U_c)_{R_*+K,R_*+K}G\in81M.
}
\tag{6.6}
$$



This proves that the direct producer term at the first normalized order-$27$ observation on these vectors vanishes. It is an actual original-source result, not a statement about arbitrary completions of a leading matrix digit.

---

## 7. The actual first returning producer term

The direct term is not the whole next reduction.

After the original unit-prefix elimination, write


$$
\mathcal R_{\alpha,JJ}=3B_\alpha,\qquad
\mathcal R_{\alpha,KJ}=9L_\alpha,
\qquad \alpha\in\{c,{\rm act}\}.
$$


Both $B_\alpha$ are integral units. The complete reduction is


$$
\mathcal S^{(2)}_\alpha
=
\mathcal R_{\alpha,KK}
-27L_\alpha B_\alpha^{-1}L_\alpha^T,
\tag{7.1}
$$




$$
f^{(2)}_\alpha
=
f_{\alpha,K}-3L_\alpha B_\alpha^{-1}f_{\alpha,J},
\tag{7.2}
$$




$$
\lambda^{(2)}_\alpha
=
\lambda_\alpha-\frac13f_{\alpha,J}^TB_\alpha^{-1}f_{\alpha,J}.
\tag{7.3}
$$



### 7.1 An evaluated physical-terminal inverse direction

Reindex $J$ by $0,\ldots,n_J-1$. The accepted first-radical digit gives


$$
\bar B=-V_{JJ},
$$


where


$$
(V_{JJ})_{\alpha\beta}
=
[y^{\alpha+\beta-(n_J-1)}](1-y)^{N_0}.
\tag{7.4}
$$


Its first column is exactly $e_{n_J-1}$, because negative coefficient indices vanish and the constant coefficient is one. Thus


$$
V_{JJ}e_0=e_{n_J-1}.
$$



The actual terminal vector is


$$
\delta_J=e_{n_J-1}.
$$


Consequently


$$
\boxed{
\bar B^{-1}\delta_J=-e_0.
}
\tag{7.5}
$$


For $n_J>1$,


$$
\boxed{
\delta_J^T\bar B^{-1}\delta_J=0.
}
\tag{7.6}
$$



These identities use the actual finite boundary and the actual terminal. They are not deductions from a radical dimension.

The leading endpoint is alternating. Put


$$
\varepsilon_0=(-1)^{R_*+\ell}.
$$


Then


$$
\bar f_{J,0}=\varepsilon_0,
$$


and (7.5) gives the additional evaluated contraction


$$
\boxed{
\delta_J^T\bar B^{-1}\bar f_J=-\varepsilon_0,
}
\tag{7.7}
$$


which is a unit.

### 7.2 Transfer of the new direct bound through the unit prefix

The accepted producer digit has $\delta$ zero on the prefix and on $K$. Hence the prefix-to-$K$ producer difference starts at $27$, while the old prefix-to-$K$ block starts at $3$. Since the prefix inverse is integral, the difference of their quadratic prefix corrections is in $81M$.

Together with (6.6), this proves


$$
\boxed{
G^T(\mathcal R_{{\rm act},KK}-\mathcal R_{c,KK})G\in81M.
}
\tag{7.8}
$$


Thus the new direct cancellation survives the original unit-prefix elimination.

### 7.3 The remaining matrix return

Modulo $3$,


$$
\bar L_{\rm act}
=
\bar L_c+\bar\kappa\,\bar t_K\delta_J^T.
\tag{7.9}
$$


Define the actual vectors


$$
\widehat t=G^T\bar t_K,\qquad
\widehat l=G^T\bar L_ce_0.
\tag{7.10}
$$



Substituting (7.9) in (7.1), using (7.5)–(7.8), gives


$$
\boxed{
\frac{
G^T(\mathcal S^{(2)}_{\rm act}-\mathcal S^{(2)}_c)G
}{27}
\equiv
\bar\kappa
\bigl(\widehat t\,\widehat l^{\,T}
+\widehat l\,\widehat t^{\,T}\bigr)
\pmod3.
}
\tag{7.11}
$$



The quadratic producer term is absent because of the **evaluated** equality (7.6). More precisely, its exact scalar coefficient


$$
\delta_J^TB_\alpha^{-1}\delta_J
$$


is divisible by $3$, so that contribution begins at $81$, not $27$.

Equation (7.11) is the complete first matrix return on $G$ at this digit. The direct contribution that was open in turn13 has now been proved zero there.

It does not prove that the returning linear term vanishes: neither $\widehat t$ nor $\widehat l$ has been set to zero.

### 7.4 The endpoint and complete diagonal also return

They cannot be discarded merely because the matrix quadratic term vanishes.

From the complete original perturbation $G_{\rm act}-G_c=3^7\mathcal M(\mathscr R\,\cdot\,\cdot)$ and the paid original inverse bounds,


$$
E_{\rm act}^{-1}-E_c^{-1}\in3^5M.
$$


Hence the original endpoint and diagonal changes satisfy


$$
e_{\rm act}-e_c\in3^5\mathbb Z_3^\nu,\qquad
d_{\rm act}-d_c\in3^5\mathbb Z_3.
$$


After the unit prefix,


$$
f_{{\rm act},K}-f_{c,K}\in27\mathbb Z_3^K,\qquad
f_{{\rm act},J}-f_{c,J}\in9\mathbb Z_3^J,
$$


and


$$
\lambda_{\rm act}-\lambda_c\in27\mathbb Z_3.
$$



Using (7.2) and (7.7),


$$
\boxed{
f^{(2)}_{\rm act}-f^{(2)}_c
\equiv
3\bar\kappa\,\varepsilon_0\,\bar t_K
\pmod9.
}
\tag{7.12}
$$



For the diagonal, put


$$
u_0=\bar B^{-1}\bar f_J.
$$


Expanding the unit inverse to its first returning order gives an integral difference and


$$
\boxed{
\lambda^{(2)}_{\rm act}-\lambda^{(2)}_c
\equiv
-2\bar\kappa\,\varepsilon_0\,
(\bar t_J^Tu_0)
\pmod3.
}
\tag{7.13}
$$



Thus a producer matrix cancellation does not remove the producer’s endpoint or complete-diagonal effects. The physical terminal remains active through the unit contraction (7.7).

---

## 8. A concrete next source lemma

The new calculation reduces the first matrix return to one actual complete-core boundary column.

### Proposed boundary-column lemma

On the same infinite original subfamily, prove


$$
\boxed{
G^T\bar L_ce_0=0.
}
\tag{8.1}
$$



A specific sufficient original-coordinate identity is


$$
\boxed{
(\bar L_ce_0)_u
=
[y^{E-\ell-u}](1-y)^{-b},
\qquad
0\le u<\ell,
\qquad E=\frac{Q-3}{2}.
}
\tag{8.2}
$$


This is a statement about the **first column of the original $J$-block coupling**, not an arbitrary extension of the $K\times K$ leading form.

If (8.2) is proved, its contraction is immediately evaluated. For a column $g_a=(y-1)^by^a$,


$$
[y^{E-\ell}](1-y)^{-b}g_a
=[y^{E-\ell}]y^a.
$$


But


$$
E-\ell=n_J+\frac b2>\frac b2\ge a.
$$


Thus the coefficient is zero, proving (8.1).

The important remaining point is the original-object identification (8.2). H2 as stated only identifies the $K\times K$ operator; it does not by itself authorize an additional boundary column. Establishing (8.2) requires the complete finite moment calculation and the actual prefix correction on that strip. It belongs alongside, not outside, the ongoing A4 precision-$29$ audit.

If (8.1) is established, (7.11) improves to


$$
G^T(\mathcal S^{(2)}_{\rm act}-\mathcal S^{(2)}_c)G\in81M.
$$


Even then, the endpoint and diagonal returns (7.12)–(7.13) remain, and the complete-core next digit still has to be evaluated.

---

## 9. An actual recurrence obstruction to an unpaid inverse argument

The turn13 division-free recurrence is useful, but “division-free identity” does not mean “unit-cost forward solve.”

Put


$$
q_t=(2t+2)(2t+1),
$$




$$
L_t=(2t+3)\mu_{t+2}+2\mu_{t+1}-(2t+1)\mu_t,
$$




$$
C_t=(2t+3)q_tq_{t+1}+2q_t-(2t+1).
$$


Then


$$
C_tL_{t+1}-q_tC_{t+1}L_t=0.
\tag{9.1}
$$


The coefficient of $\mu_{t+3}$ is


$$
(2t+5)C_t.
$$



There is a resonant step in the actual original range:


$$
t_*=\frac{3^h-5}{2}=\frac{3H-5}{2},
\qquad
T=t_*+3=\frac{3H+1}{2}.
\tag{9.2}
$$


The original window ensures $T\le2n-1$, so this is not an exterior moment.

Write $s=2t+3$. Direct algebra gives


$$
C_t=(s-2)(s^4-s^2+2s-3).
\tag{9.3}
$$


At $t=t_*$, $s=3^h-2\equiv1\pmod3$, and therefore


$$
C_{t_*}\equiv1\pmod3.
$$


Hence


$$
\boxed{
v_3\bigl((2t_*+5)C_{t_*}\bigr)=h.
}
\tag{9.4}
$$



There is no common factor $3$ in all coefficients of (9.1) at this step. Indeed,


$$
v_3(q_{t_*})=1,\qquad v_3(C_{t_*+1})=1,
$$


so the coefficient of $\mu_{t_*+2}$,


$$
2C_{t_*}-(2t_*+3)q_{t_*}C_{t_*+1},
$$


is a unit.

The source moments themselves show the associated cancellation. Before the first unit-weight pole appears,


$$
\mu_t\in3\mathbb Z_3\qquad(0\le t<T).
$$


At $t=T$, the new denominator is


$$
2T-1=3H=3^h,
$$


with coefficient one. Thus


$$
\boxed{\mu_T\equiv1\pmod3.}
\tag{9.5}
$$


The numerator in the forward solve at $t_*$ consequently has valuation exactly $h$.

This proves a precise obstruction:

> Solving the complete homogeneous recurrence for its highest moment at this actual original step requires a division by $3^h$. That divisor cannot be canceled as a common factor of the recurrence coefficients.

It does **not** prove that the actual solution of $Cw=z$ has valuation below $-1$. It proves that the desired directional bound cannot be justified by an unpaid, uniformly one-digit-stable propagation of this recurrence. A successful recurrence method must establish the necessary resonance cancellations in the actual boundary-value problem.

---

## 10. Relation to the requested directional inverse and determinant pair

Under H2, turn13’s endpoint-adapted elimination gives


$$
T=
\begin{pmatrix}
a&z^T\\ z&C
\end{pmatrix}\in27M,
\qquad f_T=e_0,
\qquad v_3(\lambda)=-1,
$$


with exact complete diagonal $\lambda$. Its pair is


$$
D_0=\det T,\qquad
D_1=\det C-\lambda\det T.
$$


If $C$ is nonsingular and the actual solution satisfies


$$
C^{-1}z\in3^{-1}\mathbb Z_3^{b/2},
$$


then the already proved directional lemma gives


$$
v_3D_1=v_3\det C,\qquad
v_3D_0-v_3D_1\ge2
$$


when $D_0\ne0$.

Nothing proved above establishes that hypothesis:

* the new direct producer bound does not prove $C$ nonsingular;
* the finite $J$-direction (7.5) is not the much larger solve $Cw=z$;
* the common radical dimension is not a relative cofactor saving;
* the unevaluated vector $\widehat l$ and the complete endpoint returns remain relevant;
* H2 itself is still under the stated original-object audit.

Likewise, the exact complete determinant transfer remains


$$
\Delta=\det(\zeta_{i+j})_{0\le i,j\le m},
\qquad
\zeta_t=\sum_{s=0}^{n}q_s\mu_{s+t},
$$




$$
K=
\det(\zeta_{i+j+2}+2\zeta_{i+j+1}+\zeta_{i+j})_{0\le i,j<m},
$$


with the **actual** $q_s=[y^s]Q_{\rm act}$, and


$$
v_3\mathcal D_0-v_3\mathcal D_1
=
v_3\Delta-v_3K-26.
$$


The largest moment used is exactly $2n-1$. This transfer is reused, but neither determinant valuation has been evaluated here.

The leading-completion examples from turn13 are not used as original-matrix examples.

---

## 11. Divisor and boundary ledger

The new calculation makes no unrecorded column-content division.

| Operation | Payment or justification |
|---|---|
| Actual producer normalization | The original division by $3^7$ in (1.4) |
| Signed scalar $\xi$ | Its previously paid common division is retained |
| Division by $y+1$ | Monic; no nonunit divisor |
| Definition of $B_1$ | One additional division by $3$, paid by the actual mod-$3$ producer reset |
| Top coefficients $\eta_k$ | The complete numerator in (2.4) is divided by $3^8$ |
| Pole denominators | Paid by $3^h$ on the exact original cutoff |
| Factorial part in the new congruences | Vanishes only because its retained factor $3^h$ exceeds the stated precision |
| $F_i^*-F_i$ | Division by $3^{20}$, paid by the supplied exact congruence |
| Original LOW/HIGH inverse | Cost $3^{-1}$, reused at its stated scope |
| Original unit prefix | Unit inverse |
| First-radical $J$-block | Exact inverse $3^{-1}B^{-1}$ |
| Rank-$b$ elimination under H2 | Cost $3^{-2}$; application still depends on H2 |
| Forward recurrence at $t_*$ | Actual coefficient divisor $3^h$, proved in §9 |
| Inverse of $C$ | **Not paid or assumed** |

The original finite coordinates, physical terminal, exact endpoint lifts, complete diagonal, and all source returns remain present.

---

## 12. Arithmetic scale and the global objective

The new bound (6.5) is a fixed-depth improvement. It is not a factor $3^b$ in the primitive denominator, and it does not turn a common determinant factor into a relative one.

The existing support envelope also stops here as a general certification mechanism. At precision $24$,


$$
\frac{\Lambda_{24}}D=\frac{27}{1+\rho}<27,
$$


whereas the same half-grid argument requires a ratio greater than $42$. Thus the proof of (6.3) cannot simply be iterated to unbounded precision.

The large valuation of the producer endpoint charge (2.1) is real, but it is not a license to divide that charge out of primitive affine residual columns or the unit physical endpoint. The previously closed Jacobi-content obstruction continues to apply.

No actual column content or least simultaneous clearer is replaced by a convenient local bound. Retain exactly


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the gcd over **all primes**


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$, the actual primitive integers are


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole evaluated error is unchanged:


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{12.1}
$$



An irrationality proof requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\boxed{
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|
\longrightarrow+\infty.
}
\tag{12.2}
$$


Neither the nonvanishing nor this limiting comparison is proved here.

---

## 13. Bounded exact-arithmetic audit

No computation was executed. No original dense producer calculation, closed rank calculation, or previous $P=2187,r=227$ certificate needs to be repeated for the proofs above.

A small optional audit can check the new cyclic normalization and signs.

### 13.1 An $81$-coefficient check

For $1\le k\le9$ and $0\le r\le8$, compute over $\mathbb F_3$


$$
T_{k,r}=(-1)^{k+1}\binom{r+k-1}{k-1}.
$$


The expected matrix, with rows $k=1,\ldots,9$, is


$$
\begin{pmatrix}
1&1&1&1&1&1&1&1&1\\
2&1&0&2&1&0&2&1&0\\
1&0&0&1&0&0&1&0&0\\
2&2&2&1&1&1&0&0&0\\
1&2&0&2&1&0&0&0&0\\
2&0&0&1&0&0&0&0&0\\
1&1&1&0&0&0&0&0&0\\
2&1&0&0&0&0&0&0&0\\
1&0&0&0&0&0&0&0&0
\end{pmatrix}.
\tag{13.1}
$$


These are also the coefficients of


$$
(-1)^{k+1}(1-y)^{9-k}
$$


in degrees $0,\ldots,8$.

### 13.2 An optional complete-moment normalization check

For a bounded auxiliary scalar check—not an original index—take


$$
H=729,\quad h=7,\quad D=54,\quad A=675,\quad n=677,\quad m=338.
$$


Use the complete functional (1.2), with its cutoff $2n-2=1352$.

For


$$
1\le k\le9,\quad 0\le a\le8,\quad i\in\{0,9\},
$$


set


$$
\mathscr R_k=(y+1)(x^A+3x^{A-k}),
$$




$$
F_i^{\rm test}=x^D(y^i-9y^{H/3+i}),
\qquad \Delta=y^a.
$$


All these products lie within the stated finite functional boundary.

The expected $162$ outputs are


$$
\mathcal M(\mathscr R_kF_i^{\rm test}y^a)\in9\mathbb Z_3,
$$




$$
\frac{\mathcal M(\mathscr R_kF_i^{\rm test}y^a)}9
\equiv
T_{k,\,(364-i-a)\bmod9}\pmod3.
\tag{13.2}
$$


In particular, the $81$ differences between $i=0$ and $i=9$ are divisible by $27$.

This checks the finite complete-functional normalization behind the new identity. It does not verify the actual producer coefficients, H2, original-index infinitude, or any denominator/error estimate.

---

## 14. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Actual top producer coefficient formulas and all force terms | Retained exactly |
| Complete mixed observation (4.1) | Proved from the complete finite source and accepted jets |
| Nine-period annihilation (5.5) | Proved |
| Precision-$23$ model estimate | Proved with the existing support envelope |
| Actual direct producer bound $G^T(S_{\rm act}-S_c)G\in3^{30}M$ | Proved on the stated infinite original subfamily |
| Actual finite terminal direction $\bar B^{-1}\delta_J=-e_0$ | Evaluated and proved |
| Quadratic first producer return at order $27$ | Proved zero |
| Remaining first matrix return | Reduced exactly to (7.11) |
| Complete endpoint and diagonal returns | Retained and expanded in (7.12)–(7.13) |
| Boundary-column cancellation $G^T\bar L_ce_0=0$ | Open original-source lemma |
| Precision-$29$ identification H2 | Still under A4 review |
| Actual resonant recurrence divisor $3^h$ | Proved |
| Actual bound $C^{-1}z\in3^{-1}\mathbb Z_3^{b/2}$ | Open |
| Evaluated complete relative determinant pair | Open |
| Arithmetic-scale primitive saving | Not obtained |
| Same-index all-prime gcd versus nonzero whole error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

### Final conclusion

The new result is an actual complete-source cancellation:


$$
\boxed{
\mathcal M(\mathscr R F_{G,a}\Delta)\in27\mathbb Z_3,
\qquad
G^T(S_{\rm act}-S_c)G\in3^{30}M.
}
$$


Its proof uses the factorial component with its full payment, all pole layers at the required precision, actual producer coefficients, exact corrected columns, and the unchanged finite boundary.

The first returning producer term is now more sharply localized. Its quadratic part vanishes because the **actual physical terminal** has the evaluated inverse image $-e_0$ in the finite first-radical block. The remaining matrix return depends on one explicit complete-core boundary column, while the endpoint and complete diagonal continue to carry terminal information.

The exact local bottleneck remains a theorem about the **actual complete-source direction $C^{-1}z$**, or an evaluated complete relative determinant pair. A recurrence-based proof must additionally pay and control its actual $3^h$-resonant steps. A fixed additional producer digit does not meet the arithmetic-scale requirement.

The global bottleneck is unchanged: establish the actual all-prime gcd and primitive denominator against the **nonzero whole evaluated error at the same infinite original indices**.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ is obtained.}}
$$


