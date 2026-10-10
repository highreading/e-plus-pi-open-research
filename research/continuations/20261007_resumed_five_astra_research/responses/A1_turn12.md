> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The next producer digit and a complete second-radical observation

## Abstract

The proposed next producer formula is correct, with the actual terminal coefficient retained:


$$
\boxed{
\frac{S_{\rm act}-S_c}{3^{28}}
\equiv-\kappa(\delta t^T+t\delta^T)\pmod3,
\qquad
t_i=\frac{[y^m]F_i}{3^{20}}.
}
$$


Here $F_i$ denotes the complete, exactly corrected core column, not a freely chosen approximation. No vanishing of $t$ is assumed or proved.

A further calculation is possible on an explicit surviving radical. Choose any fixed open original subwindow contained in


$$
\boxed{\frac1{10}<\frac{N_0}{P_0}<\frac{19}{180}.}
$$


This is a next-layer calculation, not another attempt at the already disproved once-divided unit criterion.

Put


$$
Q=\frac{P_0}{9},\qquad b=Q-N_0,\qquad
\ell=\frac{3b}{2}+1,\qquad
E=\frac{Q-3}{2}.
$$


The first $\ell$ coordinates of the original radical tail form its first-digit radical. After eliminating the original unit prefix and the nondegenerate part of the first radical digit, the complete actual matrix on these coordinates satisfies


$$
\boxed{
\frac{\mathcal S^{(2)}_{uv}}9
\equiv-[y^{E-u-v}](y-1)^{N_0}
=[y^{E-u-v}](1-y)^{-b}\pmod3.
}
$$


All finite boundaries are retained. In particular:

* the next producer correction restricts to zero here, without requiring $t=0$;
* the prefix cross correction is evaluated and is zero here;
* elimination of the first-radical nondegenerate block costs a $3^{-1}$ inverse, but its matrix correction begins at $3^3$, beyond this digit;
* the complete bordered diagonal after that elimination has the exact valuation
  

$$
\boxed{v_3(\lambda^{(2)})=-1.}
$$



The evaluated next-layer operator has rank exactly $b$. Its full radical has dimension $b/2+1$, and the actual endpoint is nonzero on that radical. Its endpoint-annihilating restriction therefore has rank $b$ and nullity $b/2$.

Thus this complete next layer gives a genuine intermediate scalar noncancellation theorem and an explicit new operator. It does **not** give final relative-cofactor noncancellation or an arithmetic-scale primitive saving. The remaining radical is still growing, and the common determinant depth cancels from the relative cofactor.

No unconditional proof of rationality or irrationality of $e+\pi$ is obtained.

---

## 1. Original objects, accepted scope, and notation

The original index domain is unchanged:


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1,\qquad A=4^j-1=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


and


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



Write $x=y-1$. The finite polynomial coordinates remain


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_a=y^a\quad(d\le a\le m),
\qquad
\nu=\frac D2-1,\qquad d=D+\nu.
$$


The physical HIGH terminal is still $Y_m$.

The complete core form is


$$
G_c(f,g)=\mathcal M(Q_cfg),
\qquad
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A,
$$


where


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!.
$$


Its denominator cutoff is exactly


$$
2v+1\le4H-4D+5.
$$



The following established results are reused at their supplied sufficiently-large original scope:

1. $F=Z-WE_c^{-1}C_c$, where $W=[U\ Y]$, and
   

$$
G_c(W,F)=0.
$$


2. $[W,F]$ is an integral unimodular basis of the original degree-$\le m$ space.
3. $E_c^{-1},E_{\rm act}^{-1}\in3^{-1}M$.
4. $S_c=G_c(F,F)\in3^{26}M$.
5. The corrected-column support theorem holds through precision $20$, with its stated degree gap.
6. The exact perturbation identity is
   

$$
S_{\rm act}=S_c+3^6\Phi_R-3^{13}\mathcal Q,
   \qquad
   \Phi_R=3\Phi_{\mathscr R},\qquad
   \mathcal Q\in3^{21}M.
$$


7. The independently checked mixed observation and transport are
   

$$
\mathcal M(\mathscr R F_i\Delta)\in3\mathbb Z_3
   \quad(\deg\Delta\le m),
   \qquad
   S_{\rm act}\equiv S_c\pmod{3^{28}}.
$$


8. The complete first two corrected-column jets are
   

$$
F_i\equiv x^D
   \left(y^i-3\delta_iq_d-9y^{H/3+i}
   +9\delta_iq_{d+1}\right)\pmod{27},
$$


   where
   

$$
\delta_i=\mathbf1_{\{i=\nu-1\}},\qquad
   y^a=r_a+x^Dq_a,\quad \deg r_a<D.
$$



No old producer computation or closed once-divided rank calculation is repeated.

In the adjacent domain write


$$
P_0=243P,\qquad N_0=243r,\qquad D=P_0+N_0,
$$


where


$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\text{ odd}.
$$


The original relation


$$
4^j=243(3^{26}-1)P-243r+1
$$


is retained. Auxiliary parameters used below are not substitutions for this original relation.

---

## 2. Audit of the proposed complete mixed observation modulo $9$

### Theorem 2.1

For every integral $\Delta$ of degree at most $m$,


$$
\boxed{
\mathcal M(\mathscr R F_i\Delta)
\equiv-3\kappa\delta_i[y^m]\Delta\pmod9.
}
\tag{2.1}
$$



### Proof

The accepted producer reset, endpoint identity, and mod-$3$ jet give


$$
\mathscr R\equiv
(y+1)(\kappa x^A+3B_1)\pmod9,
\qquad \deg B_1\le A.
$$


The division by $y+1$ is monic. It introduces no nonunit denominator.

Combining this with the complete first core jet gives the endpoint-zero model


$$
\mathscr R F_i\Delta\equiv
(y+1)\left(
\kappa x^Hy^i\Delta
+3B_1x^Dy^i\Delta
-3\kappa\delta_i x^Hq_d\Delta
\right)\pmod9.
\tag{2.2}
$$


Complete functional integrality validates this substitution, including endpoint subtraction.

#### The unit-weight pole

The sole unit-weight pole has denominator $3H$ and index


$$
r_*=\frac{3H-1}{2}.
$$


The first two terms in the quotient in (2.2) have degree at most


$$
H+i+m\le r_*-1.
$$


They therefore contribute nothing at this pole.

Since $q_d$ is monic of degree $\nu$,


$$
H+\nu+m=r_*.
$$


Consequently the third term contributes exactly


$$
-3\kappa\delta_i[y^m]\Delta.
$$



#### The weight-$3$ pole

A weight of valuation exactly one requires an odd denominator of valuation $h-1$. Below the original cutoff, the only such denominator is $H$: the next eligible odd multiple is $5H$, which is outside the cutoff. The denominator $3H$ belongs to the unit-weight layer already treated.

At the $H$-pole only the leading product modulo $3$ matters. Its quotient is


$$
\kappa x^Hy^i\Delta
\equiv\kappa(y^H-1)y^i\Delta\pmod3.
$$


The extraction index is


$$
r_1=\frac{H-1}{2}.
$$


The upper part starts at degree $H$, while


$$
i+\deg\Delta\le i+m\le r_1-1.
$$


Thus this extraction is zero.

All remaining pole weights are divisible by $9$. The factorial term is also divisible by $9$ on the retained sufficiently large family. This proves (2.1). ∎

This calculation includes the physical terminal $\Delta=Y_m$. The one-degree distinction at that terminal is precisely what produces the right side of (2.1).

---

## 3. The proposed model estimate and its payments

Let


$$
F_i^*=x^D\psi_i,\qquad F_i^*\equiv F_i\pmod{3^{20}}
$$


be the established representative with its strict degree gap below $m$.

### 3.1 Producer coefficient payment at precision $22$

For $a\le A-55$, the exact factorial quotient contains $A,A-1,\ldots,A-54$. Since $v_3(A)=5$ and $54<3^5$,


$$
v_3\!\left(\frac{(A+1)!}{a!}\right)
\ge5+v_3(54!)
=5+(18+6+2)=31.
$$


After the actual division by $3^7$, these coefficients vanish even modulo $3^{24}$, hence certainly modulo $3^{22}$.

The exact endpoint identity then gives


$$
\mathscr R\equiv
(y+1)x^{A-54}q_{22}(x)\pmod{3^{22}},
\qquad \deg q_{22}\le54.
\tag{3.1}
$$


Again, division by $y+1$ is monic.

### 3.2 Complete model separation

The endpoint-subtracted quotient of the model product is


$$
x^H\left(x^{D-54}q_{22}(x)\psi_i\psi_j\right).
$$


Its non-$x^H$ factor has the retained support


$$
\Omega_{20}\mathbb Z+[-21D,21D].
$$


At precision $22$, take


$$
\Lambda=\frac H{3^{21}}=\frac{\Omega_{20}}9.
$$


The coefficients of $x^H$ relevant modulo $3^{22}$ lie on the $\Lambda$-grid. Every contributing pole lies on its odd half-grid. The original window gives


$$
\frac{\Lambda}{D}>\frac{147968}{729}>42.
$$


Thus


$$
21D<\frac{\Lambda-1}{2}
$$


for sufficiently large original tuples, and every contributing extraction vanishes.

All products remain inside the original degree cutoff. The model has its endpoint factor exactly, and the factorial term retains its factor $3^h$. Therefore


$$
\boxed{
\mathcal M(\mathscr R F_i^*F_j^*)\in3^{22}\mathbb Z_3.
}
\tag{3.2}
$$



---

## 4. The next actual producer digit

Write


$$
F_i^*=F_i+3^{20}\Delta_i,
\qquad
t_i=\frac{[y^m]F_i}{3^{20}}\in\mathbb Z_3.
$$


The degree gap of $F_i^*$ gives


$$
[y^m]\Delta_i=-t_i.
$$



Expanding the product and applying Theorem 2.1,


$$
\begin{aligned}
\mathcal M(\mathscr R F_i^*F_j^*)
={}&\Phi_{\mathscr R,ij}\\
&+3^{20}\mathcal M\bigl(\mathscr R(F_i\Delta_j+\Delta_iF_j)\bigr)
+3^{40}\mathcal M(\mathscr R\Delta_i\Delta_j).
\end{aligned}
$$


The quadratic term is paid by complete integrality. The linear term is


$$
3^{21}\kappa(\delta_it_j+t_i\delta_j)\pmod{3^{22}}.
$$


Using (3.2) proves


$$
\boxed{
\frac{\Phi_{\mathscr R}}{3^{21}}
\equiv-\kappa(\delta t^T+t\delta^T)\pmod3.
}
\tag{4.1}
$$


Since $\Phi_R=3\Phi_{\mathscr R}$ and


$$
3^{13}\mathcal Q\in3^{34}M,
$$


we obtain the complete proposed correction:


$$
\boxed{
\frac{S_{\rm act}-S_c}{3^{28}}
\equiv-\kappa(\delta t^T+t\delta^T)\pmod3.
}
\tag{4.2}
$$



This is a proved rank-$\le2$ formula in the unchanged middle coordinates. It is not a formula for the full next Schur correction.

---

## 5. Choice of the surviving original radical

Choose a fixed open original subwindow contained in


$$
\frac1{10}<\frac{N_0}{P_0}<\frac{19}{180}.
\tag{5.1}
$$


The established original-index density result applies to such fixed intervals. No assertion is made about arbitrary auxiliary pairs $(P,r)$ satisfying only this ratio.

Set


$$
Q=\frac{P_0}{9},\qquad b=Q-N_0.
$$


Here $b$ is a positive even multiple of $243$. Moreover,


$$
0<b<\frac Q6
\tag{5.2}
$$


with a fixed positive margin on every fixed interior subwindow of (5.1).

Recall


$$
R_*=\frac{P_0+1}{2},\qquad
\tau=\frac{N_0-3}{2},\qquad
C=\frac{P_0/3-3}{2}.
$$


The first radical digit is


$$
V_{uv}=[y^{C-u-v}]x^{N_0},
\qquad 0\le u,v<\tau.
$$


The previously proved finite-boundary rank calculation identifies its full radical as the first


$$
\boxed{
\ell=\frac{P_0/3-3N_0}{2}+1=\frac{3b}{2}+1
}
\tag{5.3}
$$


tail coordinates.

Let


$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\}.
$$


The block $V_{JJ}$ is invertible over $\mathbb F_3$, and every row and column of $V$ indexed by $K$ is zero.

The physical terminal corresponds to $u=\tau-1$, which lies in $J$, not in $K$. Thus


$$
\delta|_K=0.
\tag{5.4}
$$


Equation (4.2) consequently vanishes on $K\times K$, regardless of $t$.

---

## 6. A complete low-degree moment formula modulo $3^{29}$

The next core calculation benefits from an exact evaluation of the complete pole sum.

Define


$$
L_s=\mathcal M((y+1)x^Hy^s).
$$


For $0\le s\le2D$, the factorial contribution vanishes modulo $3^{29}$, and all coefficients of the quotient lie inside the original cutoff. The elementary partial-fraction identity gives


$$
\boxed{
L_s\equiv
-\frac{3^h\,2^H H!}
{\prod_{k=0}^{H}(2s+1+2k)}
\pmod{3^{29}}.
}
\tag{6.1}
$$


This evaluates the complete pole sum; it is not a selected-pole approximation.

Because $2s+1<H$ and $2s+2H+1<3H$, counting multiples of powers of $3$ in the denominator gives


$$
v_3(L_s)=h-v_3(2s+1)
\tag{6.2}
$$


for the rational expression in (6.1).

Put


$$
U_s=\frac{(2s+1)L_s}{3^h}
$$


for that expression. Then


$$
U_s=U_0\prod_{j=1}^{s}
\left(1+\frac{2H}{2j+1}\right)^{-1},
$$


and


$$
U_0=-\frac{4^H}{(2H+1)\binom{2H}{H}}.
$$


For $H\ge27$,


$$
4^H\equiv1\pmod{27},\qquad
\binom{2H}{H}\equiv20\pmod{27},
$$


so


$$
U_0\equiv4\pmod{27}.
\tag{6.3}
$$



For completeness, the central-binomial congruence follows by separating the multiples of $3$:


$$
\frac{\binom{2H}{H}}{\binom{2H/3}{H/3}}
=
\prod_{\substack{1\le k\le H\\3\nmid k}}\left(1+\frac Hk\right).
$$


For $H\ge27$ the product is $1\pmod{27}$. At $H=9$, it is again $1\pmod{27}$, since the sum of the six unit reciprocals is zero modulo $3$. The base value is $\binom63=20$.

For $s\le2D$, every correction factor in $U_s/U_0$ is $1\pmod{27}$. Hence $U_s\equiv4\pmod{27}$.

Let


$$
\mu=\frac{P_0}{3},\qquad c_a=\frac{a\mu-1}{2}.
$$


On (5.1), the only relevant odd multiples are $a=1,3,5,7,9,11,13$. Thus for every integral $P$ of degree at most $2D$,


$$
\boxed{
\begin{aligned}
\mathcal M((y+1)x^HP)\equiv{}&
4\,3^{26}P_{c_9}
+4\,3^{27}P_{c_3}\\
&+3^{28}\sum_{a\in\{1,5,7,11,13\}}
a^{-1}P_{c_a}
\pmod{3^{29}},
\end{aligned}
}
\tag{6.4}
$$


where the inverses in the last line are taken modulo $3$.

This formula includes every lower pole and the factorial payment.

---

## 7. Paying all corrected-column terms on $K\times K$

For $i=R_*+u$ with $u\in K$, the terminal indicator is zero. The first jets are therefore


$$
\phi_{i,0}=y^i,\qquad
\phi_{i,1}=0,\qquad
\phi_{i,2}=-y^{H/3+i}\pmod3.
$$



It would be invalid simply to extend the earlier stationary estimate by one digit. In particular, replacing the exact quadratic error by a precision-$20$ representative can leave an unpaid mixed term. We instead evaluate the relevant digit orders directly.

### 7.1 Total order two

The order-two contribution on $K\times K$ is


$$
-18\,\mathcal M\bigl((y+1)x^Hy^{H/3}
x^D(\beta+3y)y^{i+j}\bigr).
\tag{7.1}
$$



The exact product calculation used in §6 also applies to a monomial shifted by $H/3$: the complete quotient still ends below the original cutoff, and its largest odd denominator is below $3H$. At the precision needed here,


$$
\frac{\mathcal M((y+1)x^Hy^{H/3}P)}{3^{26}}
\equiv[y^{c_9}]P\pmod3
\qquad(\deg P\le2D).
\tag{7.2}
$$


Indeed, the valuation of


$$
2H/3+2s+1
$$


is the valuation of $2s+1$, since the latter has much smaller possible valuation; the normalized unit is $1\pmod3$.

For the present $P$, the extraction in (7.2) lies strictly between $N_0$ and $P_0$, where $x^D\bmod3$ has no support. Thus (7.1) vanishes modulo $3^{29}$.

### 7.2 Total order three

Since $\phi_{i,1}=0$, only the terms


$$
\phi_{i,3}y^j+y^i\phi_{j,3}
$$


remain.

The strict degree gap of the precision-$20$ representative makes the unit-weight pole absent in these pairings. The digit representatives may be chosen coefficientwise with the same top-degree bound; the already fixed lower jets also lie below that bound.

All remaining poles have a factor $3$. Consequently a valid common grid for the remaining moment modulo $3^{26}$ is


$$
\frac H{3^{24}}=9P_0.
$$


The retained support width is at most


$$
\frac72D+1<\frac{9P_0-1}{2}.
$$


Every remaining extraction is therefore zero.

### 7.3 Total order at least four

At total order $s=4$, the usual complete common grid is again $9P_0$, while


$$
4D+1<\frac{9P_0-1}{2},
$$


because $N_0/P_0<1/9$. Subsequent grids grow faster than the widths until the retained $\Omega_{20}$-grid takes over. Terms with sufficiently large explicit digit order vanish by their powers of $3$.

This argument uses only the supplied support theorem through precision $20$.

We have proved


$$
\boxed{
(S_c)_{ij}\equiv G_c(z_i,z_j)\pmod{3^{29}}
\quad(i,j\in R_*+K).
}
\tag{7.3}
$$



---

## 8. Evaluation of the next core contribution

Write


$$
i=R_*+u,\qquad j=R_*+v,\qquad 0\le u,v<\ell.
$$


Apply (6.4) to


$$
P=x^D(\beta+3y)y^{i+j}.
$$



The $c_3$-extraction and those with $a\le5$ are below the minimum degree. The $a=7,11,13$ extractions lie, respectively, in coefficient gaps or above degree $D$. These exclusions have fixed positive margins on (5.1).

Only $c_9$ remains. Put


$$
k_{uv}=\frac{P_0-3}{2}-u-v.
$$


Throughout $K\times K$,


$$
\frac{P_0}{3}+N_0<k_{uv}<\frac{2P_0}{3},
$$


with enough margin to include $k_{uv}-1$. Thus


$$
[y^{k_{uv}}]x^D,\ [y^{k_{uv}-1}]x^D\in9\mathbb Z_3.
$$


Since $\beta\equiv1\pmod9$, division of the assembled expression gives


$$
\frac{(S_c)_{ij}}{3^{28}}
\equiv\frac{[y^{k_{uv}}]x^D}{9}\pmod3.
\tag{8.1}
$$



Modulo $27$, the coefficients of $x^{P_0}$ that can meet this interval lie on the $P_0/9$-grid. The only possible band is the one beginning at $4P_0/9$. Its normalized coefficient is


$$
\frac{[y^{4P_0/9}]x^{P_0}}9\equiv1\pmod3.
$$


Therefore


$$
\boxed{
\frac{(S_c)_{R_*+u,R_*+v}}{3^{28}}
\equiv[y^{E-u-v}]x^{N_0}\pmod3,
\qquad
E=\frac{P_0/9-3}{2}.
}
\tag{8.2}
$$



This is the complete next core contribution on the chosen surviving radical.

---

## 9. The prefix cross correction is evaluated, not discarded

Partition


$$
U=-S_{\rm act}/3^{26}
=
\begin{pmatrix}
\mathsf A&\mathsf B\\
\mathsf B^T&\mathsf C
\end{pmatrix}
$$


at the original unit prefix $R_*$.

Let


$$
a=\frac{P_0-1}{2},\qquad J_0=\frac{P_0}{3}-1.
$$


The leading prefix and its finite inverse are


$$
(\mathsf A_0)_{ij}=[y^{a-i-j}](1-y)^{N_0},
$$




$$
(\mathsf A_0^{-1})_{ij}
=[y^{i+j-a}](1-y)^{-N_0},
\qquad 0\le i,j\le a.
\tag{9.1}
$$



For a column $u\in K$, the complete precision-$28$ core formula gives


$$
\boxed{
(\mathsf B_1)_{i,u}
=\overline{(\mathsf B/3)_{i,u}}
=[y^{J_0-i-u}]x^{N_0}.
}
\tag{9.2}
$$


Only the $2P_0/3$-band contributes to this divided coefficient. The producer cannot affect $\mathsf B_1$, since its correction to $U$ starts at $9$.

Convolving the three finite coefficient expressions in (9.1)–(9.2) gives


$$
\boxed{
(\mathsf B_1^T\mathsf A_0^{-1}\mathsf B_1)_{uv}
=[y^{C-u-v}](1-y)^{N_0}
=-V_{uv}.
}
\tag{9.3}
$$


The finite bounds do not truncate this convolution: any nonnegative contributing inverse exponent forces the two other coefficient indices within their displayed ranges.

Since $K\subseteq\ker V$, (9.3) is zero on $K\times K$.

Hence for


$$
\mathcal R=\mathsf C-\mathsf B^T\mathsf A^{-1}\mathsf B,
$$


equations (4.2), (5.4), (8.2), and (9.3) prove


$$
\boxed{
\frac{\mathcal R_{KK}}9
\equiv-[y^{E-u-v}]x^{N_0}\pmod3.
}
\tag{9.4}
$$



---

## 10. First-radical elimination, endpoint lift, and complete diagonal

Retain the exact endpoint and full diagonal after prefix elimination:


$$
f=e_R-\mathsf B^T\mathsf A^{-1}e_C,
$$




$$
\boxed{
\lambda=3^{26}d_{\rm act}-e_C^T\mathsf A^{-1}e_C.
}
\tag{10.1}
$$


The original diagonal term has not been removed.

Since


$$
\mathcal R/3\equiv -V\pmod3,
$$


we have


$$
\mathcal R_{JJ}=3B_J,\qquad B_J\in\operatorname{GL}_{|J|}(\mathbb Z_3),
$$


and


$$
\mathcal R_{KJ}\in9M.
$$


Thus


$$
\mathcal R_{JJ}^{-1}=3^{-1}B_J^{-1}
$$


is a new, explicitly paid inverse.

Define the exact second reduction


$$
\mathcal S^{(2)}
=\mathcal R_{KK}
-\mathcal R_{KJ}\mathcal R_{JJ}^{-1}\mathcal R_{JK},
$$




$$
f^{(2)}
=f_K-\mathcal R_{KJ}\mathcal R_{JJ}^{-1}f_J,
$$




$$
\boxed{
\lambda^{(2)}
=\lambda-f_J^T\mathcal R_{JJ}^{-1}f_J.
}
\tag{10.2}
$$



The matrix correction has valuation at least


$$
2+2-1=3.
$$


It does not change (9.4). The endpoint correction is divisible by $3$, so


$$
\overline{f^{(2)}_u}=(-1)^{R_*+u}.
\tag{10.3}
$$


Equations (10.2), not an arbitrary endpoint replacement, define the retained actual lift.

### Theorem 10.1 — A new actual scalar noncancellation

Let


$$
n_J=|J|=\tau-\ell=\frac{Q-4b-5}{2}.
$$


Then


$$
\boxed{
3\lambda^{(2)}
\equiv(-1)^{n_J-1}n_J\not\equiv0\pmod3,
}
\tag{10.4}
$$


and consequently


$$
\boxed{v_3(\lambda^{(2)})=-1.}
\tag{10.5}
$$



### Proof

After reindexing $J$ by $0,\ldots,n_J-1$,


$$
(V_{JJ})_{\alpha\beta}
=[y^{\alpha+\beta-(n_J-1)}](1-y)^{N_0}.
$$


Its inverse is


$$
(V_{JJ}^{-1})_{\alpha\beta}
=[y^{n_J-1-\alpha-\beta}](1-y)^{-N_0}.
$$


Using the alternating endpoint and $\mathcal R_{JJ}/3\equiv-V_{JJ}$,


$$
3\lambda^{(2)}
\equiv
[y^{n_J-1}](1+y)^{-2}(1-y)^{-N_0}\pmod3.
\tag{10.6}
$$



Since $N_0=Q-b$ and $Q$ is a power of $3$,


$$
(1-y)^{-N_0}
=\frac{(1-y)^b}{1-y^Q}.
$$


The extraction index in (10.6) is below $Q$, so it reduces to


$$
[y^{n_J-1}](1+y)^{-2}(1-y)^b.
$$


By (5.2), $n_J-1>b$ for sufficiently large tuples.

For a polynomial $P$ and $t\ge\deg P$,


$$
[y^t](1+y)^{-2}P(y)
=(-1)^t\bigl((t+1)P(-1)+P'(-1)\bigr).
$$


Take $P=(1-y)^b$. Because $b$ is even and divisible by $3$,


$$
P(-1)\equiv1,\qquad P'(-1)\equiv0\pmod3.
$$


Thus (10.6) is $(-1)^{n_J-1}n_J$. Finally,


$$
n_J=\frac{Q-4b-5}{2}\equiv2\pmod3,
$$


so this value is nonzero. ∎

This theorem concerns an exact intermediate bordered scalar. It does not identify the final endpoint-observed relative cofactor.

---

## 11. Exact rank of the complete second-radical operator

Combining the preceding calculations,


$$
\boxed{
\frac{\mathcal S^{(2)}_{uv}}9
\equiv-[y^{E-u-v}]x^{N_0}
=[y^{E-u-v}](1-y)^{-b}\pmod3,
\quad 0\le u,v<\ell.
}
\tag{11.1}
$$


The second equality holds because $E<Q$ and


$$
x^{N_0}=-\frac{1-y^Q}{(1-y)^b}
$$


in characteristic $3$.

Let $\mathcal H$ denote the matrix in (11.1).

### Theorem 11.1



$$
\boxed{
\operatorname{rank}\mathcal H=b,\qquad
\dim\ker\mathcal H=\frac b2+1.
}
\tag{11.2}
$$


Under the identification of a coordinate vector with


$$
f(y)=\sum_{u=0}^{\ell-1}f_uy^u,
$$


its full radical is


$$
\boxed{
\ker\mathcal H
=(y-1)^b\,\mathbb F_3[y]_{\le b/2}.
}
\tag{11.3}
$$



### Proof

First,


$$
E-2(\ell-1)=\frac{Q-3}{2}-3b>0
$$


on the fixed subwindow. Thus every matrix index is nonnegative.

The coefficient sequence of $(1-y)^{-b}$ satisfies a recurrence of exact order $b$, with characteristic polynomial $(T-1)^b$. Hence $\operatorname{rank}\mathcal H\le b$.

A consecutive $b\times b$ Hankel block of this sequence has determinant a unit. One elementary verification starts with the block whose coefficient indices are


$$
i+j-(b-1).
$$


Coefficients at $-1,\ldots,-(b-1)$ are zero and the coefficient at zero is one, making that block anti-triangular with unit antidiagonal. Shifting the block forward preserves its determinant up to a unit, because the recurrence has unit last coefficient. Therefore any consecutive nonnegative block of size $b$ is invertible. Such a block occurs within $\mathcal H$, proving rank $b$.

If


$$
f=(y-1)^bg,\qquad \deg g\le b/2,
$$


then $b$ is even and


$$
(1-y)^{-b}f=g.
$$


The $u$-th pairing is $[y^{E-u}]g$, which is zero because


$$
E-(\ell-1)>\frac b2.
$$


These vectors give $b/2+1=\ell-b$ independent radical directions and therefore the whole kernel. ∎

### Endpoint restriction

By (10.3), the endpoint on this radical is, up to the fixed sign $(-1)^{R_*}$,


$$
f\longmapsto f(-1).
$$


For $f=(y-1)^bg$,


$$
f(-1)=(-2)^bg(-1)=g(-1)\quad\text{in }\mathbb F_3.
$$


The endpoint is therefore nonzero on the radical.

Its annihilating radical has the explicit basis


$$
\boxed{
(y+1)(y-1)^b y^a,\qquad 0\le a<\frac b2.
}
\tag{11.4}
$$


Consequently the actual endpoint-annihilating second-layer restriction has


$$
\boxed{
\operatorname{rank}=b,\qquad \operatorname{nullity}=\frac b2.
}
\tag{11.5}
$$



An exact integral basis annihilating $f^{(2)}$ uses only unit divisions. Its reduction gives the alternating-endpoint kernel used above. Corrections to that basis are divisible by $3$, so they cannot change a matrix already divisible by $9$ at its displayed normalized digit.

---

## 12. What this proves about cofactors—and what it does not

The next layer now has an explicit operator, exact rank, explicit radical, actual endpoint reduction, and an evaluated complete diagonal valuation. Nevertheless, the final relative cofactor remains undetermined.

One may eliminate the newly proved rank-$b$ block. That block is a unit only after division by $9$, so its inverse costs a further $3^{-2}$. After the two nondegenerate radical eliminations, the common determinant factor has valuation


$$
n_J+2b.
$$


It appears in both distinguished cofactors and cancels from their ratio.

The remaining unbordered space has dimension


$$
\frac b2+1,
$$


and its endpoint-annihilator has dimension $b/2$. These dimensions grow on the fixed original subwindow. The remaining block starts at a further digit, but its determinant and its complete bordered determinant have not been evaluated.

Thus:

* the scalar noncancellation $v_3(\lambda^{(2)})=-1$ is rigorous;
* it does not imply final cofactor noncancellation;
* the exact rank $b$ supplies common determinant depth, not a primitive saving of size $3^b$;
* no growing bound for $v_3D_0-v_3D_1$ follows from this fixed-depth calculation.

At the retained scope of the actual primitive-ratio identity,


$$
v_3(q)=
\max\!\left(
0,\,
h-26+v_3Q_{\rm loc}(-1)+v_3D_1-v_3D_0
\right).
$$


Only a quantitative estimate for the **relative** cofactor can improve this exponent. Common factors introduced by the eliminated blocks cannot do so.

### Concrete follow-on lemma

The next local obligation can now be stated on explicit original vectors, rather than on an unspecified radical:

> Lift the vectors
> 

$$
> (y-1)^b y^a,\qquad 0\le a\le b/2,
>
$$


> to the actual second Schur reduction, retaining the exact endpoint $f^{(2)}$, the diagonal $\lambda^{(2)}$, and the newly paid $3^{-2}$ inverse. Evaluate the next actual digit on their endpoint-annihilating combinations
> 

$$
> (y+1)(y-1)^b y^a,\qquad 0\le a<b/2.
>
$$


> The calculation must include the returning producer terms and the cross corrections created by that elimination.

For arithmetic scale, a fixed additional digit is not enough by itself. A distinct route is required: either a precision-growing, endpoint-controlled elimination theorem on the original objects, or a new all-prime content/gcd mechanism, or a stronger whole-error estimate. The supplied endpoint-contact theorem gives only its already paid polynomial intersection bound; it is not an independent growing gcd source.

---

## 13. Complete forcing, returns, contents, and whole error

Nothing in the local calculation changes the actual determinant columns


$$
F_{\rm act}=Z-WE_{\rm act}^{-1}C_{\rm act}.
$$



The producer identity remains


$$
3P_n-Q_c=3^7\mathscr R
=\sum_{a=0}^{A+1}e_ax^a,
$$




$$
e_a=-\frac{(A+1)!}{a!}(t_a+\xi v_a),
$$


with complete force


$$
t=3nh_{\rm vec}
+(b_{\rm force}+6)e_{n-1}
+\frac{2b_{\rm force}}{n-1}e_{n-2},
\qquad b_{\rm force}=-n-66.
$$


The signed scalar $\xi$ and its previously paid common division are unchanged.

The complete return remains


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


No logarithmic force, exponential boundary charge, finite return, exterior constant, or physical-terminal term has been deleted.

The actual column contents and least simultaneous clearer $\ell_{\rm clr}$ have not been reevaluated. They remain their original exact quantities, not convenient bounds. Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$


and the final gcd over **all primes**


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole evaluated error is still


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}\det H_{\rm complete}.
}
\tag{13.1}
$$



An irrationality proof still requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\rm complete}\ne0,
$$


and


$$
\boxed{
\log g_\ell-(m+1)\log\ell_{\rm clr}
-\log|\det H_{\rm complete}|\longrightarrow+\infty.
}
\tag{13.2}
$$


No gain from a different original family has been imported.

---

## 14. A bounded new exact-arithmetic audit

No computation has been executed here. The following bounded audit checks only the new identities; it does not establish original-index infinitude.

Take the auxiliary inputs


$$
P=2187,\qquad r=227.
$$


They satisfy $r\equiv2\pmod9$, $r$ odd, and


$$
\frac1{10}<\frac rP<\frac{19}{180}.
$$


They are **not** asserted to arise from an original pair $(j,h)$.

The derived integers are


$$
P_0=531441,\qquad N_0=55161,\qquad D=586602,
$$




$$
Q=59049,\qquad b=3888,\qquad
\ell=5833,\qquad \tau=27579,
$$




$$
n_J=21746,\qquad E=29523.
$$



### Inputs and requested checks

1. Compute, modulo $27$, the coefficients
   

$$
a_s=[y^{265719-s}](y-1)^{586602},
   \qquad 0\le s\le11664.
$$


   Verify divisibility by $9$, then compare
   

$$
a_s/9
   \quad\text{with}\quad
   [y^{29523-s}](y-1)^{55161}\pmod3.
$$



2. Verify the truncated generating-function identity
   

$$
-(y-1)^{55161}\equiv(1-y)^{-3888}
   \pmod{(3,y^{29524})}.
$$



3. Check the recurrence/radical certificate for the $5833$-dimensional Hankel operator:
   

$$
(y-1)^{3888}y^a,\qquad 0\le a\le1944.
$$


   The recurrence has order $3888$ and unit last coefficient. No dense $5833\times5833$ matrix is necessary.

4. Compute
   

$$
[y^{21745}](1+y)^{-2}(1-y)^{3888}\pmod3.
$$



5. For the small universal unit calculation, verify
   

$$
4^{27}\equiv1\pmod{27},\qquad
   \binom{54}{27}\equiv20\pmod{27}.
$$



### Expected verifiable output

* zero discrepancies in the divided-coefficient comparison;
* full next-layer rank $3888$;
* full radical dimension $1945$;
* endpoint-annihilating radical dimension $1944$;
* the coefficient in item 4 equals $1$, agreeing with
  

$$
(-1)^{21745}\,21746\equiv1\pmod3;
$$


* both small congruences in item 5 hold.

These are finite checks with explicit bounds and expected certificates. Their scope is only this auxiliary instance and the small unit calculation.

---

## 15. Proof-status ledger

| Statement | Status |
|---|---|
| Mixed observation modulo $9$ for every degree-$\le m$ $\Delta$ | Proved from complete original poles and finite degrees |
| Precision-$22$ model producer estimate | Proved with coefficient, endpoint, support, and factorial payments |
| Rank-$\le2$ next actual producer digit | Proved; actual $t$ retained |
| $t=0\pmod3$ | Not asserted |
| Complete next core contribution on the chosen $K$ | Proved |
| Prefix cross correction on $K$ | Evaluated and proved zero |
| First-radical inverse payment | Explicitly paid as $3^{-1}$ |
| Exact actual endpoint after that elimination | Retained by (10.2); required reduction proved |
| Complete diagonal valuation $v_3(\lambda^{(2)})=-1$ | New actual scalar theorem |
| Complete second-radical operator | Evaluated as a rational-coefficient Hankel operator |
| Its rank, full radical, and endpoint-annihilating nullity | Proved exactly |
| Final relative-cofactor noncancellation | Open |
| Growing primitive saving and all-prime gcd/error comparison | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

## Conclusion

The parent’s producer proposal survives the audit:


$$
\boxed{
\frac{S_{\rm act}-S_c}{3^{28}}
\equiv-\kappa(\delta t^T+t\delta^T)\pmod3.
}
$$


Its rank bound is genuine, but the actual terminal coefficient $t$ cannot be silently removed.

On the explicitly chosen surviving original radical, the complete next Schur digit is nevertheless independent of that unknown coefficient. After evaluating the core, prefix cross correction, and first-radical elimination, it is


$$
\boxed{
\frac{\mathcal S^{(2)}_{uv}}9
\equiv[y^{E-u-v}](1-y)^{-b}\pmod3.
}
$$


Its exact rank is $b$, its radical is


$$
(y-1)^b\mathbb F_3[y]_{\le b/2},
$$


and its endpoint-annihilating nullity is $b/2$. The complete diagonal also yields the new original scalar theorem


$$
\boxed{v_3(\lambda^{(2)})=-1.}
$$



These are substantive next-layer results, but not a final denominator theorem. The remaining mathematical bottleneck is the producer-aware higher observation on the explicit radical (11.3), followed by a growing **relative**, rather than common, cofactor estimate. The global bottleneck remains the same-index comparison of the **actual all-prime final gcd and primitive denominator** with the **nonzero whole evaluated error**, after the actual contents and least simultaneous clearer.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


