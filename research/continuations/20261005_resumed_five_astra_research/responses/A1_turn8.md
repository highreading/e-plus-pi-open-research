> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 8 — Complete finite propagation, a terminal-boundary reduction of the nonlinear force, and the actual determinant pair

## Executive conclusion

The formula-level qualification in A4 Turn 12 can be discharged from the supplied finite block formulas. The key is to cancel the top pole **before** dividing by $3$. This produces an exact formula for the complete return operator, including the LOW subtraction and factorial contribution. It proves the refined supported-return lemma on the original finite HIGH interval.

That repair also permits a further analysis of the nonlinear term. The resulting advance is not a determination of the primitive denominator, but it is more than another unsupported precision claim:

1. **The refined complete propagation lemma is proved.** On
   

$$
D<H/2916,\qquad \Omega'=H/729,
$$


   the actual finite core operator satisfies
   

$$
R_H\mathsf F_H:\mathcal C_{\Omega'}(W)
   \longrightarrow\mathcal C_{\Omega'}(W+1)\pmod{3^6}
$$


   under the stated separation condition. The proof evaluates the complete numerator modulo $3^7$.

2. **The precision-parametrized core support mechanism is repaired.** It no longer depends on an assertion that an earlier proof “extends.” Its application to the actual producer still uses factorial saturation, not the unsupported arbitrary-depth approximation to $Q_c$.

3. **The nonlinear cancellation improves from**
   

$$
\mathcal Q\in3M
   \quad\text{to}\quad
   \boxed{\mathcal Q\in27M}
$$


   on the original $D<H/972$ domain. Three actual structural facts are responsible:
   - the LOW mixed force is supported in at most nine initial coordinates modulo $27$;
   - those coordinates are totally isotropic for the actual LOW inverse modulo $27$;
   - after LOW elimination, the leading HIGH mixed force is a single terminal corner, whose next boundary return also vanishes.

4. **There is an exact bulk–boundary representation**
   

$$
\boxed{
   \frac{\mathcal Q}{27}
   =
   \mathcal B^T\widehat E_{\rm act}^{-1}\mathcal B
   +27a_1^TL_{\rm act}^{-1}a_1
   +\mathcal F^T\mathcal J\mathcal F,
   }
$$


   where $\mathcal J$ is an explicit integral unit matrix of order
   

$$
s=2\kappa_3+2\le20.
$$


   This is an actual uniform finite-rank boundary correction, not a new name for the whole nonlinear operator. The remaining bulk term is displayed rather than suppressed.

5. On the same fixed original-index window proposed in Turn 7, and for sufficiently large indices, the repaired support theorem gives
   

$$
\boxed{S_{\rm act}=-3^{16}\Psi,\qquad \Psi\in M_\nu(\mathbb Z_3).}
$$


   This is a divisibility statement, **not** a claim that depth $16$ is the first nonzero depth.

6. The determinant and distinguished cofactor admit an exact bordered reduction with at most twenty additional boundary coordinates. Nevertheless, their nonvanishing and relative valuation remain unresolved. The common determinant powers still cancel:
   

$$
\boxed{
   v_3(q)=
   \max\!\left\{
   0,\,
   h-16+v_3(Q_n^{\rm loc}(-1))
   +v_3(\delta_1)-v_3(\delta_0)
   \right\}
   }
$$


   when the indicated determinant pair is nonzero. There is no gain proportional to $16\nu$, or to $14\nu$, in this ratio.

No tools were used. The irrationality or rationality of $e+\pi$ remains unresolved.

---

## 1. Original domain, finite spaces, and complete functional

Throughout, retain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$




$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad0<D<H/972,
$$


and


$$
t=v_3(A)=1+v_3(j)\ge5.
$$



The finite dimensions and endpoints are


$$
m=\frac{A+1}{2},\qquad
d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1.
$$


Put $x=y-1$, and use


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m).
$$



Thus


$$
\deg z_i\le d-1,\qquad i+j\le D-4.
$$


There is no enlargement of HIGH beyond $m$, and no restoration of a deleted residual coordinate.

The producer is


$$
Q_n^{\rm loc}=Q_c+3^6R,
\qquad
Q_c=(y+1)x^A(\beta+3y),
\qquad
\beta=-71-A,
$$


with


$$
R\in\mathbb Z_3[y],\qquad \deg R\le A+1.
$$



The complete functional remains


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\!\!\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^r)=(2r)!.
\tag{1.1}
$$



Write


$$
G_c(f,g)=\mathcal M(Q_cfg),\qquad
K(f,g)=\mathcal M(Rfg).
$$



The accepted factorial-saturation theorem is used at its stated scope. In particular, at precision $3^p$,


$$
R\equiv(y+1)x^{A-\kappa_p}B_p(x)\pmod{3^p},
\qquad \deg B_p\le\kappa_p,
\tag{1.2}
$$


provided the exact factorial-tail and endpoint conditions hold.

For $p=3$,


$$
\kappa_3=
\begin{cases}
9,&t=5,6,\\
6,&t=7,\\
3,&t=8,\\
0,&t\ge9.
\end{cases}
\tag{1.3}
$$


These are the actual terminal lengths supplied by saturation.

The signed producer scalar


$$
\eta_n=((n-1)!)^2-u^T\mathsf T_n^{-1}u
$$


is retained. It is nonzero, but it is not replaced by a $3$-adic unit.

---

# Part I. Discharging the complete supported-return obligation

## 2. Separate the top pole before dividing

Set


$$
r_*=\frac{3H-1}{2},\qquad r_1=\frac{H-1}{2}.
$$



At the original cutoff, the only denominator of valuation $h$ is $3H=3^h$. Define the top coefficient forms


$$
H_0(f,g)=[y^{r_*}]x^Afg,
\qquad
H_1(f,g)=[y^{r_*}]x^Ayfg.
$$



Define the complete normalized lower-pole form


$$
\begin{aligned}
\Lambda(f,g)
={}&
\sum_{\substack{0\le a\le h-1\\
c\ge1\ {\rm odd},\ 3\nmid c\\
c3^a\le4n-3}}
3^{h-1-a}c^{-1}
[y^{(c3^a-1)/2}]x^A(\beta+3y)fg\\
&-\frac{3^{h-1}}4
\mathfrak f\!\left((y+1)x^A(\beta+3y)fg\right).
\end{aligned}
\tag{2.1}
$$



This includes every lower pole at its original cutoff and the full factorial part. Exactly,


$$
\boxed{G_c=\beta H_0+3H_1+3\Lambda.}
\tag{2.2}
$$



For a LOW column and any polynomial of degree at most $m$, both top forms vanish:


$$
\deg(x^AU_uf)\le H-1+m<r_*,
$$




$$
\deg(x^AyU_uf)\le H+m<r_*.
\tag{2.3}
$$


Consequently,


$$
L=\Lambda(U,U),\qquad X=\Lambda(U,Y),
$$


and


$$
G_c(U,U)=3L,\qquad G_c(U,Y)=3X.
$$



On HIGH put


$$
E_0=H_0(Y,Y),\qquad
\widehat E=G_c(Y,Y)-3X^TL^{-1}X.
$$


Since


$$
c_0=\frac{\beta-1}{3}\in\mathbb Z_3,
$$


the complete return operator is exactly


$$
\boxed{
\mathsf F_H
=
\frac{\widehat E-E_0}{3}
=
c_0E_0+H_1(Y,Y)+\Lambda(Y,Y)-X^TL^{-1}X.
}
\tag{2.4}
$$



Equation (2.4) is the required top-pole cancellation. In particular, it avoids treating $E_0p/3$ as though it were separately integral.

---

## 3. The complete LOW subtraction for a finite supported lift

Let $p$ be a HIGH polynomial supported in $d,\ldots,m$. Divide monically:


$$
p=Ur+x^Dq,\qquad \deg(Ur)<D.
\tag{3.1}
$$


Put


$$
\varepsilon=L^{-1}\Lambda(U,x^Dq).
\tag{3.2}
$$


Then, exactly,


$$
L^{-1}Xp=r+\varepsilon.
\tag{3.3}
$$



The top forms kill $Ur$, again by (2.3). Substitution into (2.4) therefore gives, for each original HIGH row $b$,


$$
\boxed{
\begin{aligned}
(\mathsf F_Hp)_b={}&
c_0[y^{r_*}]x^Hq\,y^b
+[y^{r_*}]x^Hyq\,y^b\\
&+
\sum_{\substack{0\le a\le h-1\\
c\ge1\ {\rm odd},\ 3\nmid c\\
c3^a\le4n-3}}
3^{h-1-a}c^{-1}
[y^{(c3^a-1)/2}]
x^H(\beta+3y)q\,y^b\\
&-\frac{3^{h-1}}4
\mathfrak f\!\left((y+1)x^H(\beta+3y)q\,y^b\right)
-(X^T\varepsilon)_b .
\end{aligned}
}
\tag{3.4}
$$



This is the complete formula requested by the audit:

- the finite HIGH interval is unchanged;
- the full LOW subtraction is the final term;
- the top numerator has already been canceled integrally;
- every lower pole is present;
- the factorial contribution remains explicit.

The analogous exact LOW-force formula is


$$
\Lambda(U_u,x^Dq)
$$


with lower-pole polynomial


$$
x^Hx^u(\beta+3y)q
\tag{3.5}
$$


and the corresponding factorial term.

---

## 4. Formula-level support lemma

For an odd power-of-three spacing $\Omega$, write


$$
I_\Omega(W)=\{a\Omega+s:a\in\mathbb Z,\ |s|\le W\},
$$




$$
J_\Omega(W)=
\left\{\frac{(2a+1)\Omega-1}{2}+s:
a\in\mathbb Z,\ |s|\le W\right\}.
$$



Suppose:

1. $\operatorname{supp}q\subseteq I_\Omega(W)$;
2. modulo $3^q$, the polynomial $x^H$ is supported on multiples of $\Omega$;
3. every lower pole surviving in (2.1) modulo $3^q$ belongs to $J_\Omega(0)$;
4. $h-1\ge q$;
5.
   

$$
W+D<\frac{\Omega-1}{2}.
   \tag{4.1}
$$



Here the precision $q$ and the polynomial $q(y)$ are distinct objects; below, the polynomial will usually be clear from context.

The polynomial in (3.5) is supported in $I_\Omega(W+D)$. Hence every surviving LOW extraction is zero modulo $3^q$. The factorial contribution is also zero modulo $3^q$. Thus


$$
\Lambda(U,x^Dq)\equiv0\pmod{3^q},
\qquad
\varepsilon\equiv0\pmod{3^q}.
\tag{4.2}
$$



Now apply (3.4). A surviving coefficient of $x^Hq$, or of $x^Hyq$, can meet a top or lower pole only when $b$ belongs respectively to $J_\Omega(W)$ or $J_\Omega(W+1)$. Therefore


$$
\boxed{
\operatorname{supp}(\mathsf F_Hp\bmod3^q)
\subseteq J_\Omega(W+1).
}
\tag{4.3}
$$



This proof treats the **whole numerator**. Equivalently,


$$
(\widehat E-E_0)p=3\mathsf F_Hp
$$


has the asserted supported representative modulo $3^{q+1}$, and that representative is exactly divisible by $3$.

### Why the pole hypotheses hold

For


$$
\Omega=\frac H{3^{r-1}},\qquad q\le r,
$$


a lower-pole weight $3^{h-1-a}$ can survive modulo $3^q$ only if


$$
a\ge h-q.
$$


Thus $3^a$ is an odd multiple of $\Omega$, so its coefficient position is on the required half-grid.

Also,


$$
v_3\binom Hk=h-1-v_3(k)\qquad(0<k<H),
$$


so $x^H\bmod3^q$ has the required grid support.

No pole pairing and no extension of a finite pole range is involved.

---

## 5. The finite HIGH inverse, with both boundaries retained

The inverse is


$$
(R_H)_{ab}
=[z^{d+m-a-b}](1-z)^{-A},
\qquad d\le a,b\le m.
\tag{5.1}
$$


At the required precision,


$$
(1-z)^{-A}\equiv(1-z)^DS(z^\Omega).
$$



For a half-grid-supported input $w$, the untruncated polynomial copies are


$$
x^D\sum_b w_b\sum_{u\ge0}s_u y^{r_1-b-u\Omega}.
\tag{5.2}
$$


Their quotient exponents belong to $I_\Omega(W)$.

The two finite boundaries are handled as follows.

- Negative quotient exponents cannot reach HIGH after multiplication by $x^D$, because $d>D$.
- At the upper boundary,
  

$$
r_1-b\le r_1-d=m-D,
$$


  so no degree beyond $m$ is introduced.
- Removing the part below $d$, and then restoring the remainder modulo $x^D$, changes the quotient only by a polynomial of degree at most
  

$$
d-1-D=\nu-1.
$$



Consequently, for $W\ge\nu-1$,


$$
\boxed{
R_H:J_\Omega(W)\longrightarrow\mathcal C_\Omega(W)
}
\tag{5.3}
$$


at the stated precision, on the actual interval $d,\ldots,m$.

Combining (4.3) and (5.3) gives


$$
\boxed{
R_H\mathsf F_H:
\mathcal C_\Omega(W)\longrightarrow
\mathcal C_\Omega(W+1).
}
\tag{5.4}
$$



This is the full finite supported-return statement, not an infinite convolution identity.

---

## 6. The specific refined modulus in A4 Turn 12

Now impose


$$
D<H/2916,\qquad \Omega'=\frac H{729}.
$$


The original arithmetic conditions give


$$
\Omega'-4D\ge3^t\ge243.
\tag{6.1}
$$



Use (3.4) modulo $3^6$. Its multiplication by $3$ gives the full numerator modulo $3^7$. The hypotheses in §4 hold because:

- $x^H\bmod3^6$ is supported on multiples of $3\Omega'$;
- every surviving normalized lower pole is on the $\Omega'$ half-grid;
- the factorial coefficient contains $3^{h-1}$;
- the complete LOW error $\varepsilon$ vanishes modulo $3^6$;
- the top cancellation is already exact in (2.4).

Thus, whenever $W+D<(\Omega'-1)/2$,


$$
\boxed{
R_H\mathsf F_H:
\mathcal C_{\Omega'}(W)\to
\mathcal C_{\Omega'}(W+1)\pmod{3^6}.
}
\tag{6.2}
$$



The complete $V$-formula, obtained from (2.2), gives


$$
\operatorname{supp}(V_{i,\bullet}\bmod3^7)
\subseteq J_{\Omega'}(\nu).
$$


Its top contribution is exactly the original last-residual/last-HIGH corner; all lower contributions are covered individually by (2.1).

The initial inverse image therefore lies in $\mathcal C_{\Omega'}(\nu)$ modulo $3^7$. For the retained return words, the largest final contraction width is


$$
\nu+(\nu+6+D)=2D+4
<\frac{\Omega'-1}{2}.
$$


Hence


$$
V(R_H\mathsf F_H)^\ell R_HV^T\equiv0\pmod{3^6}
\qquad(1\le\ell\le6),
$$


while the $\ell=0$ contraction vanishes modulo $3^7$.

The finite seven-term inverse expansion gives


$$
\boxed{V\widehat E^{-1}V^T\in3^7M.}
\tag{6.3}
$$



The LOW coupling $B\in3^7M$ follows from the same complete normalized lower-pole formula: its top coefficient is absent by degree, and its remaining polynomial is


$$
x^Hx^uy^i(\beta+3y).
$$



**The qualification in A4 Turn 12 is therefore discharged.** The subsequent depth-eight identification in Turn 6 now follows from its complete residual formula and the supplied beta-moment evaluation. Its singularity still follows from the genuine shortened residue class; no new nonsingularity assertion results.

---

## 7. Repair of the precision-parametrized use in Turn 7

The same calculation proves the conservative fixed-precision version used in Turn 7.

For


$$
C_r=512(r+1)^2\,3^{r-1},
$$


assume


$$
h\ge r+2,\qquad C_rD<H.
$$


The displayed width budget in the older source is more than sufficient for (4.1), the finite inverse boundaries, and every retained contraction.

The direct LOW terms are covered by the same formula, with nongrid degree at most $2D$. Therefore


$$
\boxed{S_c\in3^{r+1}M_\nu(\mathbb Z_3).}
\tag{7.1}
$$



No step of this core proof uses $v_3(j)\ge r-2$. It uses the original $t\ge5$, $\beta\equiv1\pmod3$, the finite endpoints, and the displayed numerical conditions. The old large-$v_3(j)$ hypothesis belonged to the unsupported actual-producer transfer, not to these core calculations.

The corrected columns consequently have the supported representatives needed in Turn 7:


$$
\widehat z_i^{\,c}\equiv x^D\psi_i\pmod{3^p},
\qquad
\deg\psi_i\le m-D,
\qquad
\operatorname{supp}\psi_i\subseteq I_{\Omega_r}(pD/2),
\tag{7.2}
$$


under that report’s explicit fixed-precision hypotheses.

Substituting the actual saturated jet (1.2), with its endpoint condition, then proves


$$
\Phi_R=K(\widehat Z^{\,c},\widehat Z^{\,c})\in3^pM
\tag{7.3}
$$


under the stated final separation inequality.

Thus the support gate is closed. It is still a **fixed-precision theorem with explicit hypotheses**, not an unbounded-depth statement on a fixed window.

---

# Part II. The actual nonlinear term

## 8. Exact Schur identity and actual unit blocks

Let $W=[U\ Y]$, and write


$$
E_c=G_c(W,W),\qquad
\widehat Z^{\,c}=Z-WE_c^{-1}G_c(W,Z).
$$


Define


$$
T=K(W,\widehat Z^{\,c}),\qquad
E_{\rm act}=E_c+3^6K(W,W).
$$



The accepted loss-one estimate and the integral perturbation imply that $E_{\rm act}$ is nonsingular and


$$
E_{\rm act}^{-1}\in3^{-1}M(\mathbb Z_3).
$$



The exact identity is


$$
S_{\rm act}
=
S_c+3^6\Phi_R-3^{12}T^TE_{\rm act}^{-1}T.
\tag{8.1}
$$



By the original degree bound, $T\in3M$. Write


$$
T=3\binom ab.
$$


For the actual eliminated block use


$$
E_{\rm act}=
\begin{pmatrix}
3L_{\rm act}&3X_{\rm act}\\
3X_{\rm act}^T&E_{Y,\rm act}
\end{pmatrix},
$$




$$
\widehat E_{\rm act}
=
E_{Y,\rm act}
-3X_{\rm act}^TL_{\rm act}^{-1}X_{\rm act},
$$


and


$$
\widetilde b=b-X_{\rm act}^TL_{\rm act}^{-1}a.
$$



Then


$$
\boxed{
S_{\rm act}
=
S_c+3^6\Phi_R-3^{13}\mathcal Q,
}
\tag{8.2}
$$


where


$$
\boxed{
\mathcal Q
=
a^TL_{\rm act}^{-1}a
+
3\widetilde b^T\widehat E_{\rm act}^{-1}\widetilde b.
}
\tag{8.3}
$$



Everything below concerns these actual blocks.

---

## 9. LOW localization and isotropy through modulus $27$

On the original $D<H/972$ domain, the now-proved supported-return calculation gives


$$
\widehat z_i^{\,c}\equiv x^D\psi_i\pmod{27},
\qquad
\operatorname{supp}\psi_i\subseteq I_\Omega(\nu+1),
\qquad
\Omega=H/243.
\tag{9.1}
$$



### 9.1 Actual LOW mixed-force support

For every LOW row, the top pole in $K(U_u,\widehat z_i^{\,c})$ is absent by degree:


$$
\deg(RU_u\widehat z_i^{\,c})
\le H+m<r_*.
$$


Thus division by $3$ leaves an integral lower-pole evaluation.

Use the actual jet $R\bmod27$ from (1.2). If $u\ge\kappa_3$, its quotient polynomial is


$$
x^{H+u-\kappa_3}B_3(x)\psi_i.
$$


Its support lies in


$$
I_\Omega(u+\nu+1).
$$


Since


$$
u+\nu+1\le\frac{3D}{2}-1
<\frac{\Omega-1}{2},
$$


all surviving normalized lower-pole extractions vanish. The factorial part also vanishes at this precision. Therefore


$$
\boxed{
a_{ui}\equiv0\pmod{27}
\qquad(u\ge\kappa_3).
}
\tag{9.2}
$$



### 9.2 The actual LOW inverse is isotropic on that support

For $u+v\ge D$, the normalized core LOW polynomial is


$$
x^Hx^{u+v-D}(\beta+3y).
$$


The same lower-pole separation, now with local degree at most $D-1$, proves


$$
L_{uv}\equiv0\pmod{27}\qquad(u+v\ge D).
\tag{9.3}
$$


Its antidiagonal is a unit modulo $3$.

The actual perturbation satisfies


$$
L_{\rm act}-L\in3^5M.
$$


Hence (9.3) also holds for $L_{\rm act}$ modulo $27$. Reversing columns gives a triangular unit matrix over $\mathbb Z/27\mathbb Z$, so


$$
\boxed{
(L_{\rm act}^{-1})_{uv}\equiv0\pmod{27}
\qquad(u+v<D-1).
}
\tag{9.4}
$$



Because $\kappa_3\le9$ and $D\ge486$, the initial $\kappa_3$-coordinate space is totally isotropic at this precision. Combining (9.2) and (9.4),


$$
\boxed{
a^TL_{\rm act}^{-1}a\in27M.
}
\tag{9.5}
$$



This is stronger than the modulo-three isotropy used in Turn 7.

---

## 10. The leading HIGH force is one actual terminal corner

Let


$$
u=e_m
$$


in HIGH coordinates and


$$
v=e_{\nu-1}
$$


in residual coordinates. Let


$$
c=[y^{A+1}]R\in\mathbb Z_3.
\tag{10.1}
$$



The original finite inverse satisfies exactly


$$
R_Hu=e_d,\qquad u^TR_Hu=0.
\tag{10.2}
$$



Modulo $3$, the core coupling $V$ is the single terminal corner. Consequently,


$$
\boxed{
\widehat z_i^{\,c}
\equiv
z_i-3\,\pi(y^d)\,\mathbf1_{i=\nu-1}
\pmod9,
}
\tag{10.3}
$$


where


$$
\pi(y^d)=y^d-\operatorname{rem}_{x^D}y^d=x^Dq_d,
\qquad \deg q_d=\nu.
$$



For every original HIGH monomial $y^b$, its core LOW projection modulo $3$ is its remainder modulo $x^D$. This follows directly from


$$
[y^{r_1}]x^Hx^uq_b=0,
\qquad
\deg(x^uq_b)\le b-1<r_1.
$$


Thus the lower-pole part of the mixed force cancels after LOW elimination.

The correction in (10.3) can reach the top pole only at $b=m$. Its leading coefficient is $c$. Therefore


$$
\boxed{
\widetilde b\equiv-cuv^T\pmod3.
}
\tag{10.4}
$$



This is a genuine actual rank-one terminal statement. It uses the leading coefficient of the actual $R$, not a freely selected perturbation.

Define the integral next mixed force


$$
\boxed{
\mathcal B=\frac{\widetilde b+cuv^T}{3}.
}
\tag{10.5}
$$



---

## 11. Two further terminal cancellations

Put


$$
M=L_{\rm act}^{-1},\qquad
H_{\rm inv}=\widehat E_{\rm act}^{-1},
$$


and


$$
\boxed{
\mathcal C=\frac{H_{\rm inv}-R_H}{3}.
}
\tag{11.1}
$$


This matrix is integral because $\widehat E_{\rm act}\equiv E_0\pmod3$.

### 11.1 The terminal inverse correction

Write


$$
F_{\rm act}=\frac{\widehat E_{\rm act}-E_0}{3}.
$$


Then


$$
\mathcal C=-R_HF_{\rm act}H_{\rm inv}.
$$


Using (10.2),


$$
\mathcal C_{mm}\equiv-(F_{\rm act})_{dd}\pmod3.
\tag{11.2}
$$



At this precision the actual perturbation does not change $F_{\rm act}$. The entry on the right is the normalized core form of $\pi(y^d)$ with itself. Its lower-pole polynomial is


$$
x^{H+D}q_d^2(\beta+3y).
$$


Modulo $3$, its possible low degree is at most


$$
D+2\nu=2D-2<r_1.
$$


The top contribution is absent by degree. Hence


$$
\boxed{\mathcal C_{mm}\in3\mathbb Z_3.}
\tag{11.3}
$$



### 11.2 The first return to the lower HIGH boundary

Set


$$
w=\mathcal B^Te_d.
\tag{11.4}
$$



The actual LOW projection of $y^d$ agrees with its monic remainder modulo $27$, by the complete LOW calculation of §4. Therefore


$$
3\widetilde b_{d,\bullet}
\equiv
K(\pi(y^d),\widehat Z^{\,c})
\pmod{27}.
\tag{11.5}
$$



Use the actual jet and (9.1). The quotient in the right-hand side is congruent modulo $27$ to


$$
x^H x^{D-\kappa_3}B_3(x)q_d\psi_i.
$$


Its nongrid width is at most


$$
D+\nu+(\nu+1)=2D-1.
$$


Since $\Omega>4D$, this support misses **all six** pole positions contributing to $\mathcal M\bmod27$. The endpoint subtraction is justified by $R(-1)\equiv0\pmod{27}$, and the factorial part vanishes at this modulus.

Thus


$$
\widetilde b_{d,\bullet}\in9M.
$$


Because $d\ne m$, equation (10.5) gives


$$
\boxed{w\in3\mathbb Z_3^\nu.}
\tag{11.6}
$$



---

## 12. The improved nonlinear divisibility

Substitute


$$
\widetilde b=-cuv^T+3\mathcal B,
\qquad
H_{\rm inv}=R_H+3\mathcal C
$$


into (8.3). Using (10.2), one obtains


$$
\begin{aligned}
\frac{\mathcal Q}{27}
={}&
\frac{a^TMa}{27}
+\mathcal B^TH_{\rm inv}\mathcal B\\
&+\frac{c^2\mathcal C_{mm}}3vv^T
-\frac c3(vw^T+wv^T)\\
&-c\left(
v\,u^T\mathcal C\mathcal B
+\mathcal B^T\mathcal C u\,v^T
\right).
\end{aligned}
\tag{12.1}
$$



Every term is integral by (9.5), (11.3), and (11.6). Therefore


$$
\boxed{\mathcal Q\in27M_\nu(\mathbb Z_3).}
\tag{12.2}
$$



This proves


$$
\boxed{
S_{\rm act}-S_c\in3^{\min(6+p,16)}M
}
\tag{12.3}
$$


whenever the repaired linear-force theorem supplies $\Phi_R\in3^pM$.

The bound $16$ is only the depth not excluded by the present argument. Further cancellation is possible.

---

# Part III. An exact uniform bulk–boundary representation

## 13. Isolate the finite LOW jet

Put


$$
\kappa=\kappa_3\le9,
$$


and let $P$ embed the first $\kappa$ LOW coordinates. Define


$$
\alpha=P^Ta,\qquad
a_1=\frac{a-P\alpha}{27}.
\tag{13.1}
$$


These are integral by (9.2).

The actual LOW inverse jet


$$
J_{\rm low}=\frac{P^TMP}{27}
\tag{13.2}
$$


is integral by (9.4). Put


$$
\zeta=P^TMa_1.
\tag{13.3}
$$


Then exactly,


$$
\frac{a^TMa}{27}
=
\alpha^TJ_{\rm low}\alpha
+\alpha^T\zeta+\zeta^T\alpha
+27a_1^TMa_1.
\tag{13.4}
$$



For the terminal HIGH terms define


$$
\tau=\frac{c^2\mathcal C_{mm}}3,
\qquad
\gamma=-c\left(\frac w3+\mathcal B^T\mathcal C u\right).
\tag{13.5}
$$


Both are integral.

Let


$$
\mathcal F=
\begin{pmatrix}
\alpha\\
\zeta\\
v^T\\
\gamma^T
\end{pmatrix},
\qquad
\mathcal J=
\begin{pmatrix}
J_{\rm low}&I_\kappa&0&0\\
I_\kappa&0&0&0\\
0&0&\tau&1\\
0&0&1&0
\end{pmatrix}.
\tag{13.6}
$$


The matrix $\mathcal J$ is an integral unit matrix:


$$
\det\mathcal J=(-1)^{\kappa+1}.
$$


Its order is


$$
s=2\kappa+2\le20.
$$



Equations (12.1)–(13.6) prove the exact identity


$$
\boxed{
\frac{\mathcal Q}{27}
=
\mathcal B^TH_{\rm inv}\mathcal B
+27a_1^TMa_1
+\mathcal F^T\mathcal J\mathcal F.
}
\tag{13.7}
$$



### What this representation accomplishes

It separates:

- the next complete HIGH mixed-force bulk,
  

$$
\mathcal B^TH_{\rm inv}\mathcal B;
$$


- an explicitly $27$-divisible LOW tail;
- an actual boundary correction of rank at most $20$, uniformly in the moving original index.

The boundary features are not arbitrary: they consist of the first at most nine LOW force coordinates, their actual inverse coupling, and the original terminal HIGH/residual corner.

### What it does not accomplish

It does **not** prove that the whole matrix $\mathcal Q/27$ has bounded rank. The bulk term can have growing rank. Nor does it prove its determinant or distinguished cofactor nonzero.

That distinction is essential.

---

## 14. The role of the finite Pascal inverse

The producer coefficients entering these formulas remain actual and computable from


$$
e_a=-\frac{(n-1)!}{a!}\bigl(t_a+\xi_nv_a\bigr),
\qquad
\xi_n=\frac{\chi_n}{\eta_n},
$$


with the complete force from Turn 5.

The accepted residue–Pascal unit inverse supplies finite digit lifting for


$$
\mathsf T_n^{-1}\tau,\qquad \mathsf T_n^{-1}u
$$


with the true finite residue-class sizes. Factorial saturation then restricts the required producer data to the actual terminal jet.

For example, obtaining $R\bmod81$ requires only the terminal jet with


$$
\kappa_4\le12
$$


on the original domain. This is enough producer precision for inspecting several of the first normalized quantities in (13.7), together with the corresponding finite core lifts.

However, computing $\xi_n\bmod3^M$ by division still requires certified precision beyond $v_3(\eta_n)$. The Pascal unit theorem does not remove that scalar denominator. No uniform bound on that additional precision is asserted here.

---

# Part IV. The actual determinant pair

## 15. The fixed window from Turn 7 now gives a depth-$16$ factorization

Retain the same fixed window


$$
j\equiv81\pmod{243},
\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
$$


where


$$
C_{16}=512\cdot17^2\,3^{15}.
\tag{15.1}
$$



Its original-index infinitude is already available and is not reproved.

For sufficiently large indices:

- the repaired core theorem gives
  

$$
S_c\in3^{17}M;
$$


- the repaired linear-force theorem at $p=11$ applies;
- here $t=5$, and the exact terminal width is
  

$$
\kappa_{11}=27<D;
$$


- hence
  

$$
\Phi_R\in3^{11}M;
$$


- §12 gives
  

$$
\mathcal Q\in27M.
$$



Define


$$
\boxed{
\Psi=
\frac{\mathcal Q}{27}
-\frac{\Phi_R}{3^{10}}
-\frac{S_c}{3^{16}}.
}
\tag{15.2}
$$


Then


$$
\boxed{S_{\rm act}=-3^{16}\Psi.}
\tag{15.3}
$$



The last two terms in (15.2) are divisible by $3$. Thus (13.7) also identifies the leading bulk–boundary structure of $\Psi$, without claiming it is nonzero.

---

## 16. A bounded-border determinant and cofactor law

Set


$$
\mathcal A=
\mathcal B^TH_{\rm inv}\mathcal B
+27a_1^TMa_1
-\frac{\Phi_R}{3^{10}}
-\frac{S_c}{3^{16}}.
\tag{16.1}
$$


Then the exact, actual decomposition is


$$
\boxed{\Psi=\mathcal A+\mathcal F^T\mathcal J\mathcal F,}
\tag{16.2}
$$


where the boundary order $s\le20$.

Let $e=e_{\rm act}$ be the exact transported residual endpoint, and retain


$$
d_{\rm act}=W(-1)^TE_{\rm act}^{-1}W(-1).
$$


Define


$$
\delta_0=\det\Psi,
$$




$$
\boxed{
\delta_1=e^T\operatorname{adj}(\Psi)e
-3^{16}d_{\rm act}\det\Psi.
}
\tag{16.3}
$$



Introduce the bordered matrix


$$
\mathscr K=
\begin{pmatrix}
\mathcal A&\mathcal F^T\\
\mathcal F&-\mathcal J^{-1}
\end{pmatrix},
\qquad
\widetilde e=\binom e0.
\tag{16.4}
$$


Since $-\mathcal J^{-1}$ is a unit matrix, exact Schur identities give


$$
\det\mathscr K=\det(-\mathcal J^{-1})\,\delta_0,
\tag{16.5}
$$


and


$$
\boxed{
\widetilde e^T\operatorname{adj}(\mathscr K)\widetilde e
-3^{16}d_{\rm act}\det\mathscr K
=
\det(-\mathcal J^{-1})\,\delta_1.
}
\tag{16.6}
$$



These identities hold even when $\Psi$ or $\mathcal A$ is singular. The boundary unit multiplies both members of the determinant pair equally.

This is a relative cofactor law for the actual decomposition, rather than a generic precision-protection inequality.

### Conditional smaller-matrix reduction

If $\mathcal A$ is nonsingular, put


$$
\mathcal H=\mathcal J^{-1}+\mathcal F\mathcal A^{-1}\mathcal F^T.
$$


Then


$$
\det\Psi=\det\mathcal A\,\det\mathcal J\,\det\mathcal H.
\tag{16.7}
$$


When $\mathcal H$ is also nonsingular,


$$
\boxed{
e^T\Psi^{-1}e
=
e^T\mathcal A^{-1}e
-
(\mathcal F\mathcal A^{-1}e)^T
\mathcal H^{-1}
(\mathcal F\mathcal A^{-1}e).
}
\tag{16.8}
$$



The remaining small matrix has order at most twenty. But the inverses and the cancellation in (16.8) are actual obligations. Neither nonsingularity hypothesis is presently established for the moving family.

---

## 17. Relation to the Turn 7 pair

Turn 7 defined


$$
S_{\rm act}=-3^{14}\Upsilon.
$$


The present result gives


$$
\Upsilon=9\Psi.
$$


Therefore its original pair satisfies exactly


$$
\boxed{
\mathcal D_0=3^{2\nu}\delta_0,\qquad
\mathcal D_1=3^{2(\nu-1)}\delta_1.
}
\tag{17.1}
$$



Thus the work has not bypassed the old nonvanishing target:


$$
\mathcal D_0\ne0\iff\delta_0\ne0,
\qquad
\mathcal D_1\ne0\iff\delta_1\ne0.
$$



The relative valuation changes by precisely two:


$$
v_3(\mathcal D_1)-v_3(\mathcal D_0)
=
-2+v_3(\delta_1)-v_3(\delta_0).
\tag{17.2}
$$


There is no dimension-multiplied denominator gain after the common powers cancel.

---

## 18. Primitive denominator and whole same-index error

Restore


$$
Q_n=\lambda Q_n^{\rm loc},
\qquad
R_{\rm rat}=\frac{4\lambda}{3^h}G_{\rm act},
$$


and


$$
H_{\rm complete}
=
R_{\rm rat}+(e+\pi)Q_n(-1)vv^T.
$$



Retain


$$
\beta_0=\det R_{\rm rat},
\qquad
\beta_1=Q_n(-1)v^T\operatorname{adj}(R_{\rm rat})v.
$$



The actual endpoint $Q_n^{\rm loc}(-1)$ is nonzero. It is not replaced by the zero core endpoint.

When $\delta_0\ne0$,


$$
\boxed{
\frac{\beta_1}{\beta_0}
=
-\frac{3^{h-16}Q_n^{\rm loc}(-1)}4
\frac{\delta_1}{\delta_0}.
}
\tag{18.1}
$$



For a clearing integer $\ell$, with $k=m+1$, retain


$$
A_\ell=\ell^k\beta_0,\qquad B_\ell=\ell^k\beta_1,
$$




$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|).}
\tag{18.2}
$$


All primes are included.

When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$



If $\delta_0\delta_1\ne0$, equation (18.1) yields


$$
\boxed{
v_3(q)=
\max\!\left\{
0,\,
h-16+v_3(Q_n^{\rm loc}(-1))
+v_3(\delta_1)-v_3(\delta_0)
\right\}.
}
\tag{18.3}
$$



The whole evaluated error is still


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
}
\tag{18.4}
$$



Neither the bounded border nor the improved local depth determines the all-prime gcd or proves nonvanishing and decay of (18.4).

---

# Part V. Remaining bottleneck and bounded verification

## 19. What has actually become smaller

The nonlinear analysis now has a concrete structure:



$$
\text{next complete HIGH bulk}
\quad+\quad
\text{at most twenty actual boundary features}
\quad+\quad
\text{controlled LOW tail}.
$$



The next useful lemma should therefore concern the **bulk relative pair**, not another isolated common zero digit.

> **Actual bulk–boundary relative-pair lemma.**  
> For the exact $\mathcal A,\mathcal F,\mathcal J,e,d_{\rm act}$ in §§13–16, establish nonvanishing of
> 

$$
> \det(\mathcal A+\mathcal F^T\mathcal J\mathcal F)
>
$$


> and of its complete distinguished cofactor
> 

$$
> e^T\operatorname{adj}(\mathcal A+\mathcal F^T\mathcal J\mathcal F)e
> -3^{16}d_{\rm act}
> \det(\mathcal A+\mathcal F^T\mathcal J\mathcal F),
>
$$


> together with a uniform law or sufficiently strong bound for their relative valuation.

A promising specific route is to analyze the displacement or supported-return structure of


$$
\mathcal B^TH_{\rm inv}\mathcal B,
$$


where $\mathcal B$ is the actual next mixed force after removal of the terminal corner. The finite-border formulas then prescribe exactly which endpoint contractions must be retained.

The present report does not prove that this bulk is invertible, does not control its inverse loss, and does not show that the scalar subtraction in (16.8) is nonzero.

---

## 20. Bounded exact arithmetic for personal inspection

No finite calculation is needed for the complete propagation proof or the exact identities above.

The coordinator’s proposed $18\times18$ modulo-three LOW check remains useful auxiliary corroboration. A modest extension can inspect the stronger modulo-$27$ LOW mechanism.

### Auxiliary inputs

Take


$$
H=19683,\qquad D=18,\qquad
A=H-D=19665,
$$




$$
h=10,\qquad n=A+2=19667,\qquad
\nu=8,\qquad \kappa=9,
$$


and


$$
\beta=-71-A.
$$



These are auxiliary polynomial parameters, **not original indices** and not an invocation of the actual order-six producer theorem.

Construct the $18\times18$ core LOW matrix modulo $27$ using the complete normalized form


$$
L_{uv}=\frac{G_c(x^u,x^v)}3,\qquad0\le u,v<18.
$$


The top pole is absent. The surviving lower layers are:

- $r_1=(H-1)/2$, weight $1$;
- $(cH/3-1)/2$, weight $3c^{-1}$, for $c=1,5,7,11$;
- $(cH/9-1)/2$, weight $9c^{-1}$, for the odd units $c\le35$.

The original auxiliary cutoff is


$$
4n-3=78665.
$$


The factorial contribution vanishes modulo $27$ after division by $3$.

For $0\le b\le9$, $0\le i<8$, form the LOW vectors given by the complete normalized evaluation with quotient polynomial


$$
x^{H-\kappa+b+u}y^i,\qquad0\le u<18.
$$



### Expected verifiable output

1. $L$ is invertible modulo $27$.
2.
   

$$
L_{uv}=0\pmod{27}\qquad(u+v\ge18).
$$


3.
   

$$
(L^{-1})_{uv}=0\pmod{27}\qquad(u+v<17).
$$


4. All eighty force vectors are supported in coordinates $0,\ldots,8$.
5. All $80^2$ inverse pairings vanish modulo $27$.

This calculation corroborates the finite algebra behind (9.5). It cannot establish the actual producer jet, the moving-family bulk determinant, a relative valuation theorem, or a global irrationality conclusion.

---

## 21. Proof-status ledger

| Statement | Status in this report |
|---|---|
| Complete formula for $(\widehat E-E_0)p/3$, including LOW and factorial terms | Derived exactly |
| Refined supported return modulo $3^6$, from the complete numerator modulo $3^7$ | Proved |
| Finite HIGH lower and upper boundaries | Retained and checked |
| Precision-parametrized core support mechanism | Repaired by the explicit formula |
| Arbitrary-depth approximation $Q_n^{\rm loc}\approx Q_c$ | Not assumed |
| Actual terminal jet from factorial saturation | Reused at its exact scope |
| LOW mixed-force support modulo $27$ | Proved |
| Actual LOW inverse isotropy modulo $27$ | Proved |
| Leading LOW-eliminated HIGH force is one terminal corner | Proved |
| $\mathcal Q\in27M$ | Proved |
| Exact bulk–boundary representation with boundary order at most $20$ | Proved |
| Depth-$16$ factorization on the fixed Turn 7 window | Proved for sufficiently large indices |
| First nonzero residual depth | Not determined |
| Nonvanishing of $\delta_0,\delta_1$ | Unresolved |
| Uniform relative valuation of the determinant pair | Unresolved |
| Full final gcd and whole nonzero error tending to zero | Unresolved |

## Closing conclusion

The outstanding propagation qualification has been resolved at formula level. The full LOW subtraction, exact top-pole cancellation, every surviving finite pole, the factorial part, and both HIGH boundaries are now included in one explicit supported-return proof.

The nonlinear term also has a more informative actual structure:


$$
\mathcal Q\in27M,
$$


and its divided operator consists of a displayed complete HIGH bulk plus a uniformly bounded, at-most-twenty-dimensional boundary correction and a controlled LOW tail. This yields an exact bordered determinant/cofactor law.

The decisive unresolved issue remains


$$
\boxed{
\text{nonvanishing and relative valuation of the actual determinant pair,}
}
$$


now expressed through that concrete bulk–boundary decomposition. The full all-prime gcd and the whole same-index evaluated error remain additional global obligations.



$$
\boxed{\text{An unconditional proof or disproof of irrationality of }e+\pi
\text{ remains unresolved.}}
$$


