> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Turn 23 — Uniform evaluation of the terminal coordinates and the actual leading moment kernel

## Abstract

The rationality or irrationality of $e+\pi$ remains unresolved.

At the finite-core level, the remaining critical terminal coordinates can now be evaluated uniformly. Using the complete stationary law from Turn 22, with its complete corrected columns and both mixed LOW returns, the result is


$$
\boxed{\eta_i=0\quad(0\le i\le I),\qquad h_i=0\quad(0\le i<I).}
$$



The main new ingredient is a finite, source-specific compression of the **actual monic quotient $P_d$** and the **actual LOW remainder $C_d$** modulo $27$. It is proved by monic division with both degree boundaries checked. After all fourteen sources are retained, the five LOW observations in the stationary law fall in an absent macro residue class. In particular,


$$
\boxed{C_{1,i},C_{3,i},C_{5,i},C_{7,i},C_{9,i}\equiv0\pmod{27}}
$$


for every original $0\le i\le I$. These divisibilities are proved, not assumed. The complete stationary numerator is then constructed modulo $3^{30}$, and only afterward divided by $3^{29}$.

Consequently, the actual leading matrix is


$$
\overline B_6=N^TC^{\rm mom}N.
$$


Put


$$
\Lambda=\frac P9,\qquad u=\chi-\Lambda.
$$


Then


$$
t=\Lambda-2u,\qquad I=3u-2,\qquad
\kappa_2=\frac{\Lambda-1}{2}.
$$


The exact leading ranks and kernels are


$$
\boxed{\operatorname{rank}_{\mathbb F_3}C^{\rm mom}
=\operatorname{rank}_{\mathbb F_3}\overline B_6=2u,}
$$




$$
\boxed{
\ker\overline B_6
=
\left\{
\operatorname{coeff}\bigl((1-y)^{2u}q(y)\bigr):
\deg q\le u-3
\right\}.
}
$$


Thus the nullity is $u-2$, and an explicit original-coordinate basis is supplied below.

The actual leading force is compatible with this kernel. An evaluated particular solution is


$$
\boxed{
z_{\rm p}(y)
=
\bar\gamma\,\frac{1-(1-y)^{2u}}{1+y}
\quad\text{in }\mathbb F_3[y],
}
$$


where the displayed polynomial division is exact and
$\deg z_{\rm p}=2u-1<I$.

These are leading finite-core results. They do **not** evaluate the full $B_6\bmod9$, the complete source at precision $34$, the next first-four digit or its different force contraction, physical-$7$ transport, actual primitive normalization, or the nonzero whole error.

---

## 1. Original domain, finite objects, and scope of reuse

### 1.1 Unchanged original indices

Every uniform assertion below concerns sufficiently large members of exactly the original family


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1=2m+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


subject to


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



Retain


$$
P=3^{h-32},\qquad P_0=243P,\qquad N_0=243r,
$$




$$
D=P_0+N_0,\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1.
$$


Also retain


$$
Q=27P,\qquad Q-N_0=2R,\qquad \chi=P-R,
$$


so that


$$
N_0=25P+2\chi,\qquad D=268P+2\chi.
$$



The subwindow is unchanged:


$$
\boxed{\frac3{25}<\frac{\chi}{P}<\frac{31}{250}.}
\tag{1.1}
$$


No independent choices of $P,\chi$, or $I$ are made.

Write


$$
S=h-32,\qquad P=3^S,\qquad H=3^{S+31},\qquad S\ge31,
$$




$$
\Pi=P/3,\qquad t=\Pi-2\chi,
$$




$$
k=3\chi-\Pi-1,\qquad I=k-1=3\chi-\Pi-2.
$$


The original arithmetic gives


$$
v_3(D)=v_3(\chi)=v_3(t)=5,\qquad
\chi/243\equiv1\pmod9,
$$




$$
t+I=\chi-2,\qquad I\equiv25\pmod{27}.
\tag{1.2}
$$



For the new calculation, define


$$
\boxed{\Lambda=P/9,\qquad u=\chi-\Lambda.}
\tag{1.3}
$$


These are derived from the original tuple. Equation (1.1) gives


$$
\boxed{\frac2{25}<\frac u\Lambda<\frac{29}{250}.}
\tag{1.4}
$$


In particular,


$$
\boxed{
t=\Lambda-2u,\qquad I=3u-2,\qquad
\kappa_2=\frac{\Lambda-1}{2},\qquad 4u<\frac{\Lambda}{2}.
}
\tag{1.5}
$$


Since $\Lambda$ is odd and $4u$ is an integer,


$$
\boxed{\kappa_2\ge4u.}
\tag{1.6}
$$


Also $v_3(u)=5$, so all degree ranges used below are nonempty on the retained sufficiently large domain.

### 1.2 Literal finite spaces and boundaries

Set $x=y-1$. The spaces remain


$$
U_r=x^r,\qquad 0\le r<D,
$$




$$
z_i^{\rm mid}=x^Dy^i,\qquad 0\le i<\nu,
\qquad
\nu=D/2-1=134P+\chi-1,
$$




$$
Y_s=y^s,\qquad d\le s\le m,
\qquad
d=D+\nu=402P+3\chi-1.
$$


Thus


$$
m+\nu=r_H,\qquad r_H=\frac{H-1}{2}.
\tag{1.7}
$$



The physical HIGH terminal is still $Y_m$. It is not replaced by $y^{\nu-1}$.

The original prefix and tail boundaries remain


$$
R_*=\frac{9Q+1}{2},\qquad a_0=R_*-1,
$$




$$
\tau=\frac{N_0-3}{2},\qquad \ell=3R+1,
$$




$$
K=\{0,\ldots,3R\},\qquad
J=\{\ell,\ldots,\tau-1\},\qquad R_*+\tau=\nu.
$$



### 1.3 Complete functional and corrected columns

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
\qquad K_{\rm phys}=2n-2=2H-2D+2.
$$



Retain


$$
Q_c=(y+1)x^A(\beta+3y),
\qquad \beta=D-H-71,
$$




$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad W=[U\ Y],
\qquad E_c=G_c(W,W),
$$


and every complete corrected column


$$
\boxed{
F[p]=x^Dp-WE_c^{-1}G_c(W,x^Dp).
}
\tag{1.8}
$$



The finite decomposition remains


$$
E_c=
\begin{pmatrix}
3\mathcal L&3\mathcal X\\
3\mathcal X^T&E_Y
\end{pmatrix},
$$




$$
M_L=\mathcal L^{-1},\qquad
\mathcal S_H=E_Y-3\mathcal X^TM_L\mathcal X,
\qquad M_H=\mathcal S_H^{-1}.
\tag{1.9}
$$


The normalized inverses are integral. The physical LOW inverse still costs $3^{-1}$.

### 1.4 All fourteen sources

The complete polynomial is


$$
\begin{aligned}
\Omega_P(y)={}&
(1-y)^{2P}(y^{122P}+3y^{41P})\\
&+9(1+y^P+y^{2P})
(2y^{14P}+2y^{41P}+2y^{95P}-y^{131P}),
\end{aligned}
$$


and


$$
p_i=\Omega_P(1-y)^ty^i,\qquad 0\le i\le I.
\tag{1.10}
$$



Equivalently, the fourteen triples $(\Delta,b,c)$ are


$$
\begin{array}{c|c|c}
\Delta&b&c\\ \hline
2P&122&1\\
2P&41&3\\
0&14,15,16&18\\
0&41,42,43&18\\
0&95,96,97&18\\
0&131,132,133&-9.
\end{array}
\tag{1.11}
$$


Both $c\beta$ and $3c$ channels remain in the complete construction.

The degree bound is


$$
\deg p_i\le133P+\chi-2=\nu-P-1.
\tag{1.12}
$$



### 1.5 Reused results and their status

The following finite-core results are reused at their stated scopes:

- the complete stationary coefficient law from Turn 22;
- the actual finite terminal equation and its completed LOW/HIGH elimination;
- uniform bare cancellation modulo $3^{30}$;
- the actual two-digit source inverse certificate and the paid terminal-side mixed LOW return;
- the complete leading first-four return $R_4=0$;
- the complete leading assembly and leading force from Turns 20–22.

Turn 22’s actual discrepancy and failure of the alternating candidate are reuse. They are not reproved here, and that candidate is not retained.

The supplied parent-favorable and pending DIFFERENT review labels are not upgraded. The new finite polynomial and leading-matrix arguments are proved below; this report does not purport to be a separate audit of every reused dependency.

No theorem is imported from the two literature abstracts mentioned in the assignment. Classical finite binomial identities and finite-dimensional linear algebra suffice for the new proofs.

---

## 2. The complete stationary law being evaluated

Define


$$
g_T=G_c(W,x^Dy^{\nu-1})
=3\binom{\alpha_T}{\upsilon_T},
$$




$$
G_c(W,x^Dp_i)=\binom{3\alpha_i}{9f_i},
$$




$$
v_T=M_H\upsilon_T,\qquad
d_T=\mathcal X^TM_L\alpha_T,\qquad
d_i=\mathcal X^TM_L\alpha_i.
$$



The exact Schur expansion is


$$
\begin{aligned}
g_T^TE_c^{-1}G_c(W,x^Dp_i)
={}&27v_T^Tf_i+3\alpha_T^TM_L\alpha_i\\
&-9v_T^Td_i-27d_T^TM_Hf_i
+9d_T^TM_Hd_i.
\end{aligned}
\tag{2.1}
$$


Thus both mixed LOW source returns are present.

Let


$$
F_T=F[y^{\nu-1}],\qquad
N_i=-G_c(F_T,F[p_i]).
$$


The complete interface is


$$
\boxed{
a\eta_i=N_i/3^{29}\pmod3,
\qquad
a=\overline B_{\ell,\tau-1}\ne0.
}
\tag{2.2}
$$



For the actual finite monic division, write


$$
y^d=C_d+(1-y)^DP_d,
\qquad \deg C_d<D,\qquad \deg P_d=\nu.
\tag{2.3}
$$


Here $D$ is even, so $(1-y)^D=x^D$.

For $v\in\{1,3,5,7,9\}$, put


$$
q_v=\frac{81vP-1}{2},
\qquad
C_{v,i}=[y^{q_v}]C_dp_i.
\tag{2.4}
$$


Also put


$$
\zeta_i=[y^{q_9}](1-y)^DP_dp_i\pmod3.
\tag{2.5}
$$



The complete Turn 22 law is


$$
\boxed{
\begin{aligned}
N_i\equiv{}&
3^{29}\bigl(\zeta_i-C_{1,i}-2C_{5,i}-C_{7,i}\bigr)\\
&-4\cdot3^{28}C_{3,i}
-4\cdot3^{27}C_{9,i}
\pmod{3^{30}}.
\end{aligned}
}
\tag{2.6}
$$



This law includes the following reused payments:

- the complete bare pairing is in $3^{30}$;
- the direct and double LOW terms in (2.1) are in $3^{51}$ and $3^{52}$;
- the terminal-side mixed LOW term satisfies
  

$$
27d_T^TM_Hf_i\in3^{30};
$$


- the HIGH return is evaluated through the required digit by
  

$$
v_T^Tf_i\equiv3^{26}\zeta_i\pmod{3^{27}};
$$


- the source-side mixed LOW term is the five-pole law used in (2.6).

In particular, the reused HIGH certificate retained


$$
\kappa(q)\equiv
7\,\mathbf1_{q=r_H}
+6\,\mathbf1_{q=r_H+H/3}\pmod9.
\tag{2.7}
$$


The second term is the retained contribution of the extra $3H$ channel. Its boundary check belongs to the actual finite source inverse certificate, not to an infinite continuation.

The new proof below evaluates (2.6). It does not infer an inverse-operator grading from a source support statement.

---

## 3. A finite compression of the actual $P_d$ and $C_d$ modulo $27$

### 3.1 The elementary carry principle

We shall use the finite polynomial fact


$$
A\equiv B\pmod3
\quad\Longrightarrow\quad
A^9\equiv B^9\pmod{27}.
\tag{3.1}
$$


Indeed, write $A=B+3E$ and expand. The linear term has factor $27$, the quadratic term has factor $9\binom92$, divisible by $27$, and every remaining term has at least $3^3$.

Because $3P$ is a power of $3$,


$$
(1-y)^{3P}\equiv1-y^{3P}\pmod3.
$$


Raising to the power $90=9\cdot10$ gives


$$
\boxed{
(1-y)^{270P}\equiv(1-y^{3P})^{90}\pmod{27}.
}
\tag{3.2}
$$



Similarly, since $\Lambda=P/9$ is a power of $3$,


$$
\boxed{
(1-y)^{2P}\equiv(1-y^\Lambda)^{18}\pmod{27}.
}
\tag{3.3}
$$



Both are congruences of finite integer polynomials.

### 3.2 A fixed finite division

Define the fixed integer polynomials $\mathscr P,\mathscr C$ by


$$
\boxed{
Z^{134}=(1-Z)^{90}\mathscr P(Z)+\mathscr C(Z),
\qquad \deg\mathscr C<90.
}
\tag{3.4}
$$


Their explicit finite forms are


$$
\mathscr P(Z)
=
\sum_{j=0}^{44}\binom{89+j}{j}Z^{44-j},
\tag{3.5}
$$




$$
\mathscr C(Z)
=
\sum_{r=0}^{89}\binom{134}{r}(Z-1)^r.
\tag{3.6}
$$


Thus $\deg\mathscr P=44$ and $\deg\mathscr C\le89$.

For completeness, every coefficient of $\mathscr C$ also has a single-product formula:


$$
\boxed{
[Z^a]\mathscr C(Z)
=
(-1)^{89-a}
\binom{134}{a}
\binom{133-a}{89-a},
\qquad 0\le a\le89.
}
\tag{3.7}
$$


To obtain it, expand (3.6), use
$\binom{134}{r}\binom ra=\binom{134}{a}\binom{134-a}{r-a}$,
and apply the finite alternating-binomial identity


$$
\sum_{s=0}^M(-1)^s\binom Ns
=(-1)^M\binom{N-1}{M}.
$$



### Theorem 3.1 — Actual finite quotient and LOW-remainder compression

On the original domain,


$$
\boxed{
P_d(y)\equiv
y^{3\chi-1}(1-y)^{2P-2\chi}\,
\mathscr P(y^{3P})
\pmod{27},
}
\tag{3.8}
$$


and


$$
\boxed{
C_d(y)\equiv
y^{3\chi-1}\mathscr C(y^{3P})
\pmod{27}.
}
\tag{3.9}
$$



#### Proof

Put


$$
E=2P-2\chi>0.
$$


Then


$$
D+E=270P.
$$


Define


$$
\widetilde P
=
y^{3\chi-1}(1-y)^E\mathscr P(y^{3P}),
\qquad
\widetilde C
=
y^{3\chi-1}\mathscr C(y^{3P}).
$$



By (3.2) and (3.4),


$$
\begin{aligned}
(1-y)^D\widetilde P+\widetilde C
&\equiv
y^{3\chi-1}
\left(
(1-y^{3P})^{90}\mathscr P(y^{3P})
+\mathscr C(y^{3P})
\right)\\
&=
y^{3\chi-1}(y^{3P})^{134}\\
&=y^{402P+3\chi-1}=y^d
\pmod{27}.
\end{aligned}
\tag{3.10}
$$



Both original finite degree boundaries must be checked.

For the quotient,


$$
\deg\widetilde P
=
3\chi-1+(2P-2\chi)+132P
=
134P+\chi-1=\nu.
\tag{3.11}
$$


For the LOW remainder,


$$
\deg\widetilde C
\le3\chi-1+267P,
$$


and


$$
D-(3\chi-1+267P)=P-\chi+1>0.
\tag{3.12}
$$


Also $3\chi-1\ge0$, so no Laurent powers have been introduced.

Therefore (3.10) is a quotient-remainder decomposition with exactly the admitted quotient degree and a remainder strictly below $D$. Monic division by $(1-y)^D$ is unique over $\mathbb Z/27\mathbb Z$. Comparing it with the reduction of the actual division (2.3) proves (3.8)–(3.9). ∎

### 3.3 Explicit LOW coefficient law

Theorem 3.1 gives the following complete coefficient law for the actual $C_d\bmod27$:


$$
\boxed{
[y^r]C_d\equiv
\begin{cases}
(-1)^{89-a}\binom{134}{a}\binom{133-a}{89-a},
&
r=3\chi-1+3Pa,\quad 0\le a\le89,\\[1mm]
0,&\text{otherwise},
\end{cases}
\pmod{27}.
}
\tag{3.13}
$$



This is a finite, evaluated coefficient prescription with fixed binomial tops. More importantly for the stationary source, the actual remainder has now been proved to have the precise macro form (3.9). No inverse grading is asserted.

---

## 4. Uniform evaluation of all five LOW observations

### 4.1 The complete macro source

Use $Z=y^\Lambda$. Equation (3.3) turns the whole fourteen-term source into


$$
\Omega_P(y)\equiv\widehat\Omega(y^\Lambda)\pmod{27},
$$


where


$$
\boxed{
\begin{aligned}
\widehat\Omega(Z)={}&
(1-Z)^{18}(Z^{1098}+3Z^{369})\\
&+9(1+Z^9+Z^{18})
(2Z^{126}+2Z^{369}+2Z^{855}-Z^{1179}).
\end{aligned}
}
\tag{4.1}
$$


No source term has been discarded.

Since $3P=27\Lambda$, define


$$
\Psi(Z)=\mathscr C(Z^{27})\widehat\Omega(Z).
\tag{4.2}
$$


The actual source product satisfies


$$
\boxed{
C_dp_i
\equiv
y^{3\chi-1+i}(1-y)^t\Psi(y^\Lambda)
\pmod{27}.
}
\tag{4.3}
$$



### 4.2 An absent macro residue class

Every exponent in the first line of (4.1) is congruent modulo $27$ to


$$
18+r,\qquad 0\le r\le18.
$$


These residues belong to


$$
\{0,1,\ldots,9\}\cup\{18,19,\ldots,26\}.
$$


Every exponent in the second line is a multiple of $9$, so it has residue $0,9$, or $18$.

Consequently,


$$
\boxed{
[Z^a]\widehat\Omega(Z)=0
\quad\text{whenever }a\bmod27\in\{10,\ldots,17\}.
}
\tag{4.4}
$$


Multiplication by $\mathscr C(Z^{27})$ preserves residue classes. Hence


$$
\boxed{
[Z^a]\Psi(Z)=0
\quad\text{whenever }a\bmod27\in\{10,\ldots,17\}.
}
\tag{4.5}
$$



This is an exact support exclusion. It is independent of the numerical values of the fixed coefficients of $\mathscr C$.

### 4.3 The actual observation indices and the original $i$-range

For $v\in\{1,3,5,7,9\}$,


$$
q_v=\frac{729v\Lambda-1}{2}
=
\frac{729v-1}{2}\Lambda+\frac{\Lambda-1}{2}.
$$


Also


$$
3\chi-1+i=3\Lambda+3u-1+i.
$$


Define


$$
r_i=\frac{\Lambda+1}{2}-3u-i,
\qquad
K_v=\frac{729v-7}{2}.
\tag{4.6}
$$


Then


$$
q_v-(3\chi-1+i)=K_v\Lambda+r_i.
\tag{4.7}
$$



The five fixed macro indices are


$$
\boxed{
(K_1,K_3,K_5,K_7,K_9)
=(361,1090,1819,2548,3277).
}
\tag{4.8}
$$


Every one is congruent to $10\pmod{27}$.

It remains essential to exclude contributions from an adjacent macro band. This is where the actual window and $0\le i\le I$ are used.

First,


$$
r_i-\Lambda<0.
\tag{4.9}
$$


Second, since $i\le I=3u-2$,


$$
\begin{aligned}
r_i+\Lambda-t
&=r_i+2u\\
&=\frac{\Lambda+1}{2}-u-i\\
&\ge\frac{\Lambda+5}{2}-4u>0.
\end{aligned}
\tag{4.10}
$$


Finally,


$$
t-r_i
\ge t-r_0
=\frac{\Lambda-1}{2}+u>0.
\tag{4.11}
$$



Thus among all integers $r_i+a\Lambda$, at most $r_i$ itself lies in the literal interval $0\le r\le t$. If $r_i<0$, none lies in that interval.

Writing


$$
c_r=[y^r](1-y)^t,\qquad c_r=0\quad(r<0\text{ or }r>t),
$$


equation (4.3) therefore yields the evaluated single-band law


$$
C_{v,i}\equiv [Z^{K_v}]\Psi(Z)\,c_{r_i}\pmod{27}.
\tag{4.12}
$$


This is not an unevaluated convolution: the only possible macro coefficient is identified, and it is zero by (4.5).

### Theorem 4.1 — Uniform five-pole annihilation

For every original $0\le i\le I$,


$$
\boxed{
C_{1,i}\equiv C_{3,i}\equiv C_{5,i}
\equiv C_{7,i}\equiv C_{9,i}\equiv0\pmod{27}.
}
\tag{4.13}
$$



#### Proof

Equation (4.12) reduces each observation to $[Z^{K_v}]\Psi$. Each $K_v\equiv10\pmod{27}$, so all five coefficients vanish by (4.5). ∎

This proves stronger depths than the five separate precisions required in Turn 22. Those depths have not been presumed at any stage.

---

## 5. Uniform evaluation of $\zeta_i$, the whole numerator, $\eta$, and $h$

The exact finite division gives


$$
(1-y)^DP_dp_i=y^dp_i-C_dp_i.
$$


Since


$$
q_9=\frac{729P-1}{2}<d
$$


and $p_i$ is a polynomial with nonnegative exponents,


$$
[y^{q_9}]y^dp_i=0.
$$


Therefore


$$
\zeta_i=-C_{9,i}\pmod3.
$$


Theorem 4.1 proves


$$
\boxed{\zeta_i=0\qquad(0\le i\le I).}
\tag{5.1}
$$



We now return to the **whole** stationary law (2.6). The contributions satisfy:

- $3^{29}\zeta_i\equiv0\pmod{3^{30}}$;
- the three unit-denominator LOW terms have depth at least $29+3=32$;
- the $C_{3,i}$ term has depth at least $28+3=31$;
- the $C_{9,i}$ term has depth at least $27+3=30$.

Hence


$$
\boxed{N_i\equiv0\pmod{3^{30}}\qquad(0\le i\le I).}
\tag{5.2}
$$



Only now divide the complete numerator by $3^{29}$ in (2.2). Since $a$ is a unit:

### Theorem 5.1 — Complete uniform terminal evaluation

On the unchanged original domain,


$$
\boxed{\eta_i=0\qquad(0\le i\le I),}
\tag{5.3}
$$


and therefore


$$
\boxed{h_i=\eta_i+\eta_{i+1}=0\qquad(0\le i<I).}
\tag{5.4}
$$



Equivalently, the evaluated generating polynomials are


$$
\boxed{
\sum_{i=0}^{I}\eta_i Z^i=0,\qquad
\sum_{i=0}^{I-1}h_i Z^i=0
\quad\text{in }\mathbb F_3[Z].
}
\tag{5.5}
$$


The nonzero critical support is empty.

The reused HIGH-return and source-side LOW laws also now give the uniform consequences


$$
v_T^Tf_i\in3^{27},
\qquad
9v_T^Td_i\in3^{30}.
\tag{5.6}
$$


Together with the already paid terminal-side mixed LOW term, this evaluates the complete stationary return on every original index.

The $\beta+3y$ channel has not been omitted: its complete contribution is part of the stationary law being evaluated. The new macro calculation is applied to the actual $C_d$ that occurs after that completed source reduction.

---

## 6. The explicit finite moment operator

The complete leading first-four return is already zero. The newly proved $\eta=0$ removes the terminal rank-two correction at its actual leading scope:


$$
C_6=C^{\rm mom},
\qquad
(C^{\rm mom})_{ij}=c_{\kappa_2-i-j},
\qquad 0\le i,j\le I.
\tag{6.1}
$$



Identify a vector $(v_0,\ldots,v_I)$ with its polynomial


$$
v(y)=\sum_{j=0}^{I}v_jy^j.
$$


Then


$$
(C^{\rm mom}v)_i
=
[y^{\kappa_2-i}](1-y)^t v(y).
\tag{6.2}
$$


All row indices remain $0\le i\le I$.

### 6.1 The finite annihilator

Since $t+2u=\Lambda$, over $\mathbb F_3$,


$$
(1-y)^t(1-y)^{2u}
=(1-y)^\Lambda=1-y^\Lambda.
\tag{6.3}
$$



Let


$$
v(y)=(1-y)^{2u}q(y),
\qquad \deg q\le u-2.
$$


Then $\deg v\le3u-2=I$, so $v$ is an original coordinate vector.

The observed coefficient indices in (6.2) satisfy


$$
\kappa_2-I\le\kappa_2-i\le\kappa_2,
$$


and, by (1.6),


$$
\kappa_2-I
=\kappa_2-3u+2\ge u+2.
\tag{6.4}
$$


But $\deg q\le u-2$, while every exponent in $y^\Lambda q$ is at least $\Lambda>\kappa_2$. Thus


$$
[y^{\kappa_2-i}](1-y^\Lambda)q=0
$$


for every original row.

Therefore


$$
\left\{(1-y)^{2u}q:\deg q\le u-2\right\}
\subseteq\ker C^{\rm mom}.
\tag{6.5}
$$


This already gives a kernel of dimension $u-1$.

### 6.2 A literal unit principal block

We now prove that there is no larger kernel.

Put $r_0=2u$. Consider the actual principal block on indices


$$
0,1,\ldots,r_0-1.
$$


For those indices,


$$
\kappa_2-i-j\ge\kappa_2-4u+2\ge2.
\tag{6.6}
$$


Also every observed index is less than $\Lambda$.

From


$$
(1-y)^t=\frac{1-y^\Lambda}{(1-y)^{r_0}}
\quad\text{over }\mathbb F_3,
$$


we obtain, throughout this block,


$$
c_{\kappa_2-i-j}
=
\binom{r_0+\kappa_2-i-j-1}{r_0-1}\pmod3.
\tag{6.7}
$$



Use the finite algebra


$$
\mathcal A=\mathbb F_3[z]/(z^{r_0}).
$$


Let


$$
a_i(z)=(1+z)^{-i}\quad\text{in }\mathcal A,
\qquad 0\le i<r_0,
$$


and


$$
U(z)=(1+z)^{r_0+\kappa_2-1}.
$$


Equation (6.7) becomes


$$
c_{\kappa_2-i-j}
=
[z^{r_0-1}]\,U(z)a_i(z)a_j(z).
\tag{6.8}
$$



The $a_i$ form a basis of $\mathcal A$. Indeed, with
$X=(1+z)^{-1}$, the binomial change from $1,X,\ldots,X^{r_0-1}$
to $1,X-1,\ldots,(X-1)^{r_0-1}$ is unit triangular, while


$$
(X-1)^i=(-z)^i(1+z)^{-i}
$$


has leading term $(-1)^iz^i$.

The pairing


$$
(f,g)\longmapsto[z^{r_0-1}]Ufg
$$


is nondegenerate because $U(0)=1$. In the basis $1,z,\ldots,z^{r_0-1}$, its Gram matrix is anti-triangular with unit anti-diagonal. Hence the actual principal block is nonsingular.

In fact its determinant is


$$
(-1)^{r_0(r_0-1)/2}=(-1)^u
\quad\text{in }\mathbb F_3.
\tag{6.9}
$$



### Theorem 6.1 — Actual moment rank and kernel

The original finite matrix $C^{\rm mom}$, of size $I+1=3u-1$, has


$$
\boxed{\operatorname{rank}C^{\rm mom}=2u,}
\tag{6.10}
$$


and


$$
\boxed{
\ker C^{\rm mom}
=
\left\{
\operatorname{coeff}\bigl((1-y)^{2u}q(y)\bigr):
\deg q\le u-2
\right\}.
}
\tag{6.11}
$$



#### Proof

The unit principal block gives rank at least $2u$. The $u-1$-dimensional kernel in (6.5) gives rank at most
$(3u-1)-(u-1)=2u$. Equality follows, and the displayed kernel has the full nullity. ∎

This proof uses the original finite row interval and a literal principal block. It does not replace the finite moment matrix by an infinite Hankel matrix.

---

## 7. The true leading $B_6$, its original-coordinate kernel, and force compatibility

### 7.1 The complete leading matrix

Let $N$ have columns $e_j+e_{j+1}$, $0\le j<I$. Under polynomial coordinates,


$$
Nz\quad\longleftrightarrow\quad(1+y)z(y).
\tag{7.1}
$$



The full leading assembly is


$$
\overline B_6
=
N^TC^{\rm mom}N-(e'h^T+he'^T),
\qquad e'=e_{I-1}.
$$


Since $h=0$,


$$
\boxed{\overline B_6=N^TC^{\rm mom}N.}
\tag{7.2}
$$


Thus, including the literal final row and column,


$$
\boxed{
(\overline B_6)_{ij}
=
c_{\kappa_2-i-j}
+2c_{\kappa_2-i-j-1}
+c_{\kappa_2-i-j-2},
\qquad 0\le i,j<I.
}
\tag{7.3}
$$



### 7.2 Exact kernel and rank

The polynomial $1+y$ is relatively prime to $1-y$ over $\mathbb F_3$. Hence multiplication by $1+y$ is invertible in


$$
\mathbb F_3[y]/(1-y)^{2u}.
$$


Theorem 6.1 shows that the moment pairing is nondegenerate on this quotient. Since $I\ge2u$, the image of the original degree-$<I$ space under multiplication by $1+y$ covers that quotient.

It follows that


$$
z\in\ker\overline B_6
\quad\Longleftrightarrow\quad
(1-y)^{2u}\mid z(y).
$$


Respecting $\deg z\le I-1=3u-3$, we obtain:

### Theorem 7.1 — Actual leading $B_6$ rank and kernel



$$
\boxed{
\operatorname{rank}_{\mathbb F_3}\overline B_6=2u
=2\chi-\frac{2P}{9},
}
\tag{7.4}
$$




$$
\boxed{
\dim\ker\overline B_6=u-2
=\chi-\frac P9-2,
}
\tag{7.5}
$$


and


$$
\boxed{
\ker\overline B_6
=
(1-y)^{2u}\mathbb F_3[y]_{\le u-3}.
}
\tag{7.6}
$$



An explicit original-coordinate basis is


$$
\boxed{
k^{(r)}(y)=y^r(1-y)^{2u},
\qquad 0\le r\le u-3.
}
\tag{7.7}
$$


Its coordinates are


$$
\boxed{
k^{(r)}_j=
\begin{cases}
(-1)^{j-r}\binom{2u}{j-r}\pmod3,
&0\le j-r\le2u,\\
0,&\text{otherwise}.
\end{cases}
}
\tag{7.8}
$$


Every last supported index satisfies


$$
2u+r\le3u-3=I-1.
$$


No vector extends beyond the original matrix.

The principal block on indices $0,\ldots,2u-1$ is again a unit block. The proof of Section 6 applies with weight


$$
(1+z)^{2u+\kappa_2-3}(z+2)^2,
$$


whose constant term is $1$ in $\mathbb F_3$. Its determinant is again $(-1)^u$.

Thus the monomials $e_0,\ldots,e_{2u-1}$, together with (7.7), give an explicit finite pivot frame. The corresponding integral coefficient change is unimodular: each kernel polynomial has highest coefficient $1$ at the distinct index $2u+r$.

### 7.3 The actual leading force

Retain


$$
\bar\gamma=(\sigma2^t)^{-1}\in\mathbb F_3,
\qquad
\sigma=(-1)^{R_*+L_*},
\qquad L_*=\frac{P-1}{2}.
$$


The complete leading force is


$$
\boxed{
\overline w_6=\bar\gamma N^TC^{\rm mom}e_0,
}
\tag{7.9}
$$


or


$$
(\overline w_6)_i
=
\bar\gamma(c_{\kappa_2-i}+c_{\kappa_2-i-1}).
$$



Define


$$
\boxed{
z_{\rm p}(y)
=
\bar\gamma\,\frac{1-(1-y)^{2u}}{1+y}.
}
\tag{7.10}
$$


This is an exact polynomial over $\mathbb F_3$. At $y=-1$,


$$
(1-y)^{2u}=2^{2u}=1,
$$


so the numerator is divisible by $1+y$. Its degree is $2u-1<I$.

Moreover,


$$
(1+y)z_{\rm p}
=
\bar\gamma e_0-\bar\gamma(1-y)^{2u}
$$


in polynomial coordinates, and the second term is in $\ker C^{\rm mom}$. Therefore


$$
\boxed{\overline B_6z_{\rm p}=\overline w_6.}
\tag{7.11}
$$



This is an evaluated original-coordinate solution, not merely an orthogonality test or a generic existence assertion.

All leading solutions are


$$
\boxed{
z(y)=z_{\rm p}(y)+(1-y)^{2u}q(y),
\qquad \deg q\le u-3.
}
\tag{7.12}
$$



In particular,


$$
\boxed{(k^{(r)})^T\overline w_6=0
\qquad(0\le r\le u-3).}
\tag{7.13}
$$


The actual leading force is compatible with the whole actual kernel.

### 7.4 The evaluated leading force contraction

The particular solution also gives


$$
z_{\rm p}^T\overline w_6
=
\bar\gamma^2\,c_{\kappa_2}.
$$


Now $243\mid t$, so $(1-y)^t$ over $\mathbb F_3$ is supported at multiples of $243$, whereas


$$
\kappa_2\equiv121\pmod{243}.
$$


Hence


$$
\boxed{z_{\rm p}^T\overline w_6=0.}
\tag{7.14}
$$



This is a leading force contraction in the current block. It is **not** the separate contraction defining $\lambda_4$, and it gives no next-digit value for that quantity.

---

## 8. What is paid, and the exact next local bottleneck

The leading problem has changed substantially. There is no remaining unknown $h$, and no rank-two update remains at this precision. The actual leading radical has dimension $u-2$; it is not represented by the rejected alternating vector.

The leading kernel and force compatibility are now proved. The complete allowed solve still requires higher precision.

For


$$
B_6x=w_6,\qquad x\in3^{-1}\mathbb Z_3^I,
$$


write


$$
3x=\widehat z_0+3z_1.
$$


The retained next equation is


$$
\overline B_6z_0=0,
$$


followed by


$$
\boxed{
\overline B_6z_1+
\overline{B_6\widehat z_0/3}
=\overline w_6.
}
\tag{8.1}
$$


The second term depends on the actual whole $B_6\bmod9$. The leading theorem does not evaluate it.

### 8.1 A concrete finite polynomial frame for the next calculation

Let $\widehat K$ be the integer matrix whose columns are the literal binomial lifts


$$
y^r(1-y)^{2u},\qquad 0\le r\le u-3,
$$


and let $E$ select the original indices $0,\ldots,2u-1$. The matrix


$$
\mathsf U=[E\ \widehat K]
$$


is unimodular.

For the full integral normalized matrix and source, the leading theorem implies a block form


$$
\mathsf U^TB_6\mathsf U
=
\begin{pmatrix}
A&3C\\
3C^T&3D
\end{pmatrix},
\qquad
\mathsf U^Tw_6=
\binom{f}{3g},
\tag{8.2}
$$


where $A$ is a unit matrix over $\mathbb Z_3$.

After eliminating this actual unit complement, the next kernel equation is governed by


$$
3\bigl(D-3C^TA^{-1}C\bigr)
$$


and the complete force


$$
3\bigl(g-C^TA^{-1}f\bigr).
\tag{8.3}
$$



Their first digits require, in particular,


$$
\boxed{
\frac{\widehat K^TB_6\widehat K}{3}\pmod3
}
\tag{8.4}
$$


and


$$
\boxed{
\frac{
\widehat K^Tw_6
-
\widehat K^TB_6E\,
(E^TB_6E)^{-1}E^Tw_6
}{3}\pmod3.
}
\tag{8.5}
$$


The numerators in these definitions are whole original-coordinate expressions. Their integrality follows from the proved leading kernel and force compatibility; their values remain unpaid.

A concrete follow-on obligation is therefore:

> **Annihilator-filtered next-digit lemma.**  
> In the original finite frame $y^r(1-y)^{2u}$, evaluate the actual whole operator and force in (8.4)–(8.5), with the complete source precision $34$, the next first-four return and its force contribution, and physical-$7$ transport retained. Determine the resulting kernel and force compatibility, or give a source-specific obstruction to an allowed lift.

This is a more precise repair than a one-row correction to the alternating candidate. It does not request an original-sized inverse array. The finite polynomial annihilator provides a symbolic frame in which the next source-specific operator calculation can be attempted.

No source grading in Sections 3–5 is being promoted to an inverse-operator grading for this unpaid step.

---

## 9. Precision and division ledger

| Object | Required precision or division | Status |
|---|---|---|
| Complete corrected columns | Physical LOW inverse $3^{-1}M_L$ | Retained |
| Actual HIGH source inverse | Literal HIGH interval, extra $3H$ channel, modulo $9$ | Reused at Turn 22 scope |
| Bare terminal pairing | Modulo $3^{30}$ | Reused uniform zero |
| Direct/double LOW terms | Complete Schur expansion | Reused depths $51,52$ |
| Terminal-side mixed LOW | $27d_T^TM_Hf_i$ | Reused depth $30$ |
| Actual $P_d,C_d$ | Modulo $27$, finite monic division | Newly proved compression |
| Carry for $270P$ | Whole finite polynomial modulo $27$ | Newly proved |
| Carry for $2P$ | Whole finite polynomial modulo $27$ | Newly proved |
| All fourteen sources | Entire $\widehat\Omega$ retained | Newly evaluated macro exclusion |
| Five LOW observations | Required moduli $3,9,3,3,27$ | All newly proved zero modulo $27$ |
| HIGH coefficient $\zeta_i$ | Modulo $3$ | Newly proved zero uniformly |
| Complete stationary numerator | Modulo $3^{30}$ | Newly proved zero uniformly |
| Final $\eta_i$ | Divide the whole numerator by $3^{29}$ | Paid after complete zero |
| Leading $C^{\rm mom}$ | Original finite matrix over $\mathbb F_3$ | Rank and kernel proved |
| Leading $\overline B_6$ | All original rows and endpoints | Rank $2u$, nullity $u-2$ proved |
| Leading force | Actual $\overline w_6$ | Compatible; explicit solution proved |
| Full allowed $3^{-1}$ solve | Whole next equation, actual $B_6\bmod9$ | Open |
| Actual source $34$ | Complete physical source | Open |
| Next first-four digit and $\lambda_4$ | Different operator/force payments | Open |

No $3$-adic division has been justified by discarding part of its numerator.

---

## 10. Complete physical producer, forcing, and later returns remain unchanged

The actual producer is still


$$
\boxed{Q_{\rm act}=Q_c+3^7\mathscr R.}
\tag{10.1}
$$


The new leading theorem is not promoted to physical $7$.

Retain


$$
F_{\rm fac}=(n-1)!,
$$




$$
T_n(a,b)=\binom{a+b}{a}\gamma_{a+b},
\qquad0\le a,b<n,
$$




$$
\gamma_0=1,\qquad \gamma_1=0,\qquad
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


Under the original existence and denominator hypotheses,


$$
[x^a](3^7\mathscr R)
=
-\frac{F_{\rm fac}}{a!}
\bigl((t_{\rm force})_a+\xi v_a\bigr),
\qquad0\le a\le n-1,
$$




$$
\mathscr R(-1)=-\frac{\xi F_{\rm fac}^2}{3^7}.
\tag{10.2}
$$



The complete forcing identity remains


$$
\boxed{
J^T\boldsymbol\varepsilon+\omega
=
-\boldsymbol\varepsilon
-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
}
\tag{10.3}
$$


Neither forcing term is removed.

The complete recurrence remains


$$
\mu_{r+1}+\mu_r
=
\frac{3^h}{2r+1}
-\frac{3^h}{4}\bigl((2r+2)!+(2r)!\bigr),
\qquad0\le r\le2n-2.
\tag{10.4}
$$


The shifted label


$$
r_*=\frac{3^h-5}{2}
$$


is unchanged; the displayed denominator pole occurs at $r=r_*+2$.

The force payments are still


$$
\lambda_{\rm new}
=
\lambda^{\rm pref}
-\frac13f_J^TB^{-1}f_J
-\frac19f_b^TA_b^{-1}f_b
\in3^{-2}\mathbb Z_3,
$$




$$
\boxed{
\lambda_4
=
\lambda_{\rm new}
-\frac1{3^4}f_C^TA_4^{-1}f_C
\in3^{-4}\mathbb Z_3.
}
\tag{10.5}
$$


Neither the reused $R_4=0$ nor the new leading force contraction (7.14) evaluates $\lambda_4$.

Still separate and open are:

- actual/core transport at physical $7$;
- physical-$5$ complementary and kernel-pivot returns;
- next digits of earlier returns, including the first-four return;
- higher endpoint adaptation;
- the complete stationary source at precision $34$.

The passed higher ternary-block theorem does not supply these actual inverse and source evaluations.

---

## 11. Actual contents, least simultaneous clearer, all-prime gcd, and whole error

No actual integer column content is altered or evaluated by the new leading result. The contents remain those of the complete original columns.

The least simultaneous clearer remains the actual $\ell_{\rm clr}$, not a convenient multiple and not merely a power of $3$. Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final gcd over **all primes**


$$
\boxed{G=\gcd(|A_\ell|,|B_\ell|).}
\tag{11.1}
$$


For $B_\ell\ne0$, the actual primitive pair is


$$
\boxed{
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{G},
\qquad
q=\frac{|B_\ell|}{G}.
}
\tag{11.2}
$$



The whole evaluated error is still


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
G\det H_{\rm complete}.
}
\tag{11.3}
$$


When the complete determinant is nonzero,


$$
|q(e+\pi)-p|
=
\frac{\ell_{\rm clr}^{m+1}}G
|\det H_{\rm complete}|>0.
\tag{11.4}
$$



An irrationality proof would require, at the **same infinite original indices**,


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
\tag{11.5}
$$


These conditions would make the nonzero whole errors tend to zero. If $e+\pi=a/b$ were rational, every nonzero integer linear error would have absolute value at least $1/b$.

The leading rank, kernel, and force solution proved here establish none of these global nonvanishing, normalization, or decay conditions.

---

## 12. A bounded auxiliary exact-arithmetic receipt

No tools or numerical execution were used. No computation is indispensable to the proofs above.

A coordinator-authored auxiliary receipt can be confined to the genuinely new fixed macro division and source exclusion.

### Bounded inputs

1. The exact division of
   

$$
Z^{134}
   \quad\text{by}\quad
   (1-Z)^{90}.
$$


2. The fixed polynomial
   

$$
\begin{aligned}
   \widehat\Omega(Z)={}&
   (1-Z)^{18}(Z^{1098}+3Z^{369})\\
   &+9(1+Z^9+Z^{18})
   (2Z^{126}+2Z^{369}+2Z^{855}-Z^{1179}).
   \end{aligned}
$$


3. Arithmetic in $(\mathbb Z/27\mathbb Z)[Z]$.

### Expected verifiable outputs

1. Quotient degree $44$, remainder degree at most $89$, and
   

$$
Z^{134}=(1-Z)^{90}\mathscr P+\mathscr C
$$


   with (3.5)–(3.7).
2. For
   

$$
\Psi(Z)=\mathscr C(Z^{27})\widehat\Omega(Z),
$$


   whose degree is at most $3600$, the five coefficients
   

$$
[Z^{361}]\Psi,\quad
   [Z^{1090}]\Psi,\quad
   [Z^{1819}]\Psi,\quad
   [Z^{2548}]\Psi,\quad
   [Z^{3277}]\Psi
$$


   are all zero modulo $27$.
3. More strongly, every coefficient of $\Psi$ at a degree congruent to
   $10,\ldots,17\pmod{27}$ is zero.

This calculation has fixed degree bounds and fixed binomial tops at most $134$. It is not an original-index scan, an original-length source table, or an inverse-array computation. Its finite scope verifies only this receipt. The uniform embedding into the original $P_d,C_d,p_i$, and the finite-boundary arguments, are the symbolic proofs in Sections 3–5.

---

## 13. Consolidated result and proof status

| Item | Status |
|---|---|
| Turn 22 single-index discrepancy and alternating-candidate failure | Reused; not reproved |
| Actual finite $P_d,C_d\bmod27$ | Newly proved compression with both degree boundaries |
| All fourteen macro sources | Retained and evaluated |
| Five LOW observations at every original $i$ | Newly proved zero modulo $27$ |
| $\zeta_i$ at every original $i$ | Newly proved zero |
| Complete stationary numerator modulo $3^{30}$ | Newly proved zero uniformly |
| All $\eta_i$ and $h_i$ | Newly evaluated as zero |
| Actual leading moment rank/kernel | Newly proved |
| Actual leading $B_6$ rank/kernel | Newly proved: rank $2u$, nullity $u-2$ |
| Actual leading force compatibility | Newly proved |
| Original-coordinate leading particular solution | Newly evaluated |
| Full $B_6\bmod9$, allowed lift, source $34$ | Open |
| Next first-four digit and complete $\lambda_4$ force | Open |
| Complete physical-$7$ transport | Open |
| Actual contents, least clearer, all-prime $G$, primitive denominator | Unevaluated |
| Same-index nonzero whole error and decay | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

## Conclusion

The remaining critical terminal coordinates are now uniformly evaluated:


$$
\boxed{\eta=0,\qquad h=0.}
$$



The decisive new source calculation is the finite congruence


$$
\boxed{
C_d(y)\equiv y^{3\chi-1}\mathscr C(y^{3P})\pmod{27},
}
$$


proved for the actual finite LOW remainder. Combined with the complete fourteen-term source and the original $\chi/P$ window, it forces every relevant LOW observation into an absent macro residue class. The complete numerator is zero modulo $3^{30}$ before the final division.

The repaired actual leading equation is no longer a rank-two perturbation with an unknown terminal vector. Its exact kernel is


$$
\boxed{
\ker\overline B_6=(1-y)^{2u}\mathbb F_3[y]_{\le u-3},
\qquad u=\chi-P/9,
}
$$


and the actual leading force has the explicit solution


$$
\boxed{
z_{\rm p}
=
\bar\gamma\,\frac{1-(1-y)^{2u}}{1+y}.
}
$$



The next local bottleneck is the **whole next-digit operator and force on this explicit annihilator frame**, together with the separately unpaid actual source-$34$, first-four force, and physical-$7$ transport calculations. The global bottleneck remains the actual all-prime primitive normalization and a nonzero whole error tending to zero at the same infinite original indices.



$$
\boxed{\text{No unconditional rationality or irrationality decision for }e+\pi\text{ follows.}}
$$


