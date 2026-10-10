> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 13 — Precision-parametrized actual Schur forgetting, its finite support ceiling, and the first unresolved coefficient layer

## Executive conclusion

The general factorial-saturation theorem already settles the “next-digit saturation” obligation left in Turn 12. Comparing the actual precision-$12$ jet with the chosen precision-$11$ lift, using their **same monic factor**, gives


$$
\boxed{S_{\rm act}\in3^{19}M_\nu(\mathbb Z_3).}
$$


No new upstream producer digit is computed or presumed in this deduction.

More substantially, the finite polynomial inverse transfer can be organized with a **weighted truncation**, rather than a rectangular product of two truncations. Combined with the complete finite core transfer, it gives the following precision-parametrized result.

Let $P$ be the core-support precision, $p$ the actual saturation precision, and $L$ the polynomial inverse-transfer precision. Under the explicit simultaneous conditions in §4,


$$
\boxed{
S_{\rm act}-S_c
\in3^{\,\min(L+1,\;P+7,\;p+7)}
M_\nu(\mathbb Z_3).
}
\tag{E.1}
$$


In particular,


$$
\boxed{
S_{\rm act}\in
3^{\,\min(P+1,\;L+1,\;p+7)}
M_\nu(\mathbb Z_3).
}
\tag{E.2}
$$



This is an **actual-core forgetting theorem**, not merely a theorem about the linear force. Its proof retains the complete nonlinear Schur remainder.

On the original sufficiently large Turn 7–12 window, one may take


$$
P=25,\qquad L=31,\qquad p=25,\qquad \kappa_{25}=54.
$$


All finite-degree, tail-length, and upper-gap conditions hold. Consequently,


$$
\boxed{
S_c\in3^{26}M_\nu(\mathbb Z_3),\qquad
S_{\rm act}\equiv S_c\pmod{3^{32}}.
}
\tag{E.3}
$$


Thus


$$
\boxed{
S_{\rm act}\in3^{26}M_\nu(\mathbb Z_3),\qquad
\Psi,\mathsf H\in3^{10}M_\nu(\mathbb Z_3).
}
\tag{E.4}
$$


Every original moment, including those determined by the complete last-column forcing, satisfies


$$
\boxed{\mu_k\equiv0\pmod{3^{10}}\qquad(0\le k\le D-4).}
\tag{E.5}
$$



There is, however, a definite ceiling to this support certificate on that fixed real window. The grid spacing decreases geometrically with $P$, while the original finite support widths do not. The full window supports $P=25$; a specified portion supports $P=26$; **none supports $P=27$ under this separation mechanism**. Failure of the certificate is not proof of a nonzero coefficient.

The first form not settled by the uniform vanishing theorem is


$$
-S_{\rm act}/3^{26}\pmod3.
$$


By (E.3), it is a **core** coefficient calculation, not an unevaluated actual-producer digit. An exact complete coefficient formula for it appears in §8. That formula retains all lower-pole carries, the finite cutoff, and the factorial term before any justified omission.

Finally, neither (E.3) nor the common depth $26$ establishes a usable relative determinant/cofactor valuation. The exact remaining local object is


$$
\det\Theta,\qquad
e_{\rm act}^{T}\operatorname{adj}(\Theta)e_{\rm act}
-3^{26}d_{\rm act}\det\Theta,
\qquad
\Theta=-S_{\rm act}/3^{26}.
$$


Common dimension-scaled powers cancel from their ratio. The all-prime gcd and the whole evaluated error remain separate obligations.

**No tools were used. No producer coefficients or numerical receipts were regenerated.**



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$



---

## 1. Domain, finite boundaries, and proof dependencies

Retain the original domain


$$
n=4^j+1,\qquad j>0,\qquad81\mid j,
$$


and


$$
A=n-2=H-D,\qquad H=3^{h-1},\qquad0<D<H/972.
$$


Set


$$
t=v_3(A)=1+v_3(j)\ge5,\qquad x=y-1,
$$




$$
m=\frac{A+1}{2},\qquad
d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1.
$$



The original finite columns are


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),\qquad W=[U\ Y].
$$


In particular,


$$
\deg z_i\le d-1,\qquad i+j\le D-4.
$$


No HIGH column beyond $m$ and no additional residual coordinate is introduced.

The complete functional remains


$$
\boxed{
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\!
\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^r)=(2r)!.
}
\tag{1.1}
$$



The actual producer is


$$
Q_{\rm act}=Q_c+3^6R,
\qquad
Q_c=(y+1)x^A c(y),
\qquad
c(y)=\beta+3y,\quad \beta=-71-A.
\tag{1.2}
$$


Here


$$
R\in\mathbb Z_3[y],\qquad \deg R\le A+1,\qquad \beta\in\mathbb Z_3^\times.
$$



The results reused at their stated scope are:

- the factorial-saturation theorem and exact signed producer denominator from Turn 5;
- the precision-$p$ saturation formulation in Turn 7;
- the complete finite return formula and finite HIGH inverse from Turn 8;
- the accepted eliminated-block inverse loss
  

$$
E^{-1}\in3^{-1}M(\mathbb Z_3);
$$


- the actual corrected-column residue $\widehat Z\equiv Z\pmod3$;
- the Hankel normalization and complete endpoint transport audited in A4 Turn 20.

The strengthened core-support statement needed below is proved from the supplied finite return formulas in §3. It is not treated as established merely because Turn 12 stated it.

The discussion of literature is limited to the supplied mathematical Markdown material. No external archive or endpoint was accessed. Prime-power digit methods and rational-diagonal methods are background tools; they do not supply a feasible-state theorem for this actual parameter-dependent kernel.

---

## 2. The precision-$12$ correction to Turn 12

On the retained window,


$$
j\equiv81\pmod{243},
$$


so $t=5$.

The accepted exact tail formula, valid here because the relevant lengths are below $3^5=243$, is


$$
\kappa_p=\min\{k\ge0:5+v_3(k!)\ge6+p\}.
$$


Now


$$
v_3(26!)=10,\qquad v_3(27!)=13.
$$


Therefore


$$
\boxed{\kappa_{11}=\kappa_{12}=27.}
\tag{2.1}
$$



Let


$$
M_{27}(y)=(y+1)x^{A-27}.
$$


Choose integral lifts of the actual saturated quotients $B_{11},B_{12}$, with


$$
R\equiv M_{27}B_{11}\pmod{3^{11}},
\qquad
R\equiv M_{27}B_{12}\pmod{3^{12}}.
$$


Reducing the second congruence modulo $3^{11}$ gives


$$
M_{27}(B_{12}-B_{11})\equiv0\pmod{3^{11}}.
$$



Multiplication by a monic polynomial is injective on polynomial coefficient modules over $\mathbb Z/3^{11}\mathbb Z$: a nonzero polynomial has a nonzero leading coefficient after multiplication by a monic polynomial. Hence


$$
B_{12}-B_{11}\in3^{11}\mathbb Z_3[x].
$$


Define


$$
C=\frac{B_{12}-B_{11}}{3^{11}},\qquad \deg C\le27.
$$


For the exact Turn 12 remainder


$$
\Delta_{11}=\frac{R-M_{27}B_{11}}{3^{11}},
$$


we obtain


$$
\boxed{\overline{\Delta}_{11}=M_{27}\overline C.}
\tag{2.2}
$$



Consequently its evaluated moment polynomial is


$$
x^{2D}\frac{\overline{\Delta}_{11}}{y+1}
=x^{H+D-27}\overline C
=(y^H-1)x^{D-27}\overline C.
$$


Its support is contained in


$$
[0,D]\cup[H,H+D].
$$


It misses the entire original window


$$
r_1-(D-4),\ldots,r_1,\qquad r_1=(H-1)/2.
$$


The depth-$18$ normalized form in Turn 12 is therefore zero modulo $3$, giving


$$
\boxed{S_{\rm act}\in3^{19}M_\nu(\mathbb Z_3).}
\tag{2.3}
$$



This uses the **existence and compatibility of the actual saturated jets**. It does not compute their coefficients.

---

## 3. Finite core support with an upper-degree budget

The following version makes the numerical budget used later explicit.

### Lemma 3.1 — Core representatives and finite upper gap

Let $P\ge7$, and put


$$
\Omega=\frac H{3^{P-1}}.
$$


Assume


$$
h-1\ge P,\qquad
\Omega>4D+2P+3.
\tag{3.1}
$$


Define


$$
g_P=\frac{\Omega-4D-2P-3}{2}.
\tag{3.2}
$$


Then there are polynomial representatives


$$
\phi_i=x^D\psi_i
$$


such that


$$
\widehat z_i^{\,c}\equiv\phi_i\pmod{3^P},
\qquad
\phi_i\equiv z_i\pmod3,
$$




$$
\operatorname{supp}\psi_i\subseteq I_\Omega(\nu+P),
\qquad
\deg\phi_i\le m-g_P.
\tag{3.3}
$$


Moreover,


$$
\boxed{S_c\in3^{P+1}M_\nu(\mathbb Z_3).}
\tag{3.4}
$$



#### Proof

The complete normalized lower-pole form from Turn 8 gives the exact decomposition


$$
G_c=\beta H_0+3H_1+3\Lambda.
$$


Every pole surviving in $\Lambda\bmod3^P$ has extraction position on the $\Omega$ half-grid. Also


$$
v_3\binom Hk=h-1-v_3(k)\qquad(0<k<H)
$$


implies that $x^H\bmod3^P$ is supported on multiples of $\Omega$. The factorial coefficient in $\Lambda$ contains $3^{h-1}$, so it vanishes at this stated modulus.

For the LOW coupling with $z_i$, the nongrid degree in


$$
x^H x^u y^i(\beta+3y)
$$


is at most $D+\nu-1$. Condition (3.1) separates it from all surviving half-grid extractions.

The complete finite return formula is


$$
\begin{aligned}
(\mathsf F_Hp)_b={}&
c_0[y^{r_*}]x^Hq\,y^b
+[y^{r_*}]x^Hyq\,y^b\\
&+
\sum_{\substack{0\le a\le h-1\\c\ {\rm odd},\ 3\nmid c\\c3^a\le4n-3}}
3^{h-1-a}c^{-1}
[y^{(c3^a-1)/2}]x^H(\beta+3y)q\,y^b\\
&-\frac{3^{h-1}}4
\mathfrak f((y+1)x^H(\beta+3y)q\,y^b)
-(X^T\varepsilon)_b .
\end{aligned}
\tag{3.5}
$$


Thus the LOW subtraction and every finite lower pole are included before reduction.

The finite HIGH inverse maps the appropriate half-grid support to grid support without increasing its width. Each complete return increases the width by at most one. The retained expansion modulo $3^P$ therefore has width at most $\nu+P$. Throughout,


$$
(\nu+P)+D<\frac{\Omega-1}{2},
$$


so the complete LOW error $\varepsilon$ vanishes at the working modulus.

Both original HIGH boundaries remain in force. In particular, the inverse formula


$$
(R_H)_{ab}=[z^{d+m-a-b}](1-z)^{-A},
\qquad d\le a,b\le m,
$$


introduces no degree beyond $m$; the lower-edge monic remainder has the already accounted finite degree.

Since $H/\Omega$ is odd, the adjacent grid centers around $H/2$ are


$$
\frac{H-\Omega}{2},\qquad \frac{H+\Omega}{2}.
$$


The upper one is excluded by (3.1). The resulting upper-degree estimate implies the conservative gap (3.2).

Finally,


$$
(S_c)_{ij}=G_c(z_i,\widehat z_j^{\,c}).
$$


The functional $G_c(z_i,\cdot)/3$ is integral on the entire original degree-$\le m$ space. Replacing the corrected column by $\phi_j$ is therefore legitimate after this division. The remaining nongrid width is at most


$$
D+i+1+(\nu+P)\le2D-2+P,
$$


which misses the surviving half-grid. The top coefficient is absent by the upper-degree gap. This proves (3.4). ∎

---

## 4. A weighted finite polynomial inverse

### 4.1 Exact saturation input

Let $\ell_{6+p}$ be the least terminal length for which


$$
v_3\!\left(\frac{(A+1)!}{(A+1-\ell_{6+p})!}\right)\ge6+p,
$$


with the factorial defined, and put


$$
\kappa_p=\ell_{6+p}-2.
$$


Retain the endpoint condition


$$
2v_3((A+1)!)\ge6+p.
$$


The accepted saturation theorem gives


$$
R\equiv R_p:=(y+1)x^{A-\kappa_p}B_p(x)\pmod{3^p},
\qquad
\deg B_p\le\kappa_p.
\tag{4.1}
$$



Write


$$
a(y)=x^{-\kappa_p}B_p(x),\qquad
Q_p=(y+1)x^A(c+3^6a).
$$



### 4.2 The weighted truncation

Let $L\ge7$, and set


$$
q_L=\left\lfloor\frac{L-1}{6}\right\rfloor.
$$


The formal inverse multiplier


$$
\frac{c}{c+3^6a}
$$


has the expansion


$$
1+
\sum_{a_0\ge1}\sum_{b\ge0}
(-1)^{a_0+b}
\binom{a_0+b-1}{b}
\beta^{-a_0-b}
3^{6a_0+b}a(y)^{a_0}y^b.
$$


Retain exactly the terms with $6a_0+b<L$, and define


$$
\boxed{
f_i=\phi_i\!\left[
1+
\sum_{a_0=1}^{q_L}
\sum_{b=0}^{L-6a_0-1}
(-1)^{a_0+b}
\binom{a_0+b-1}{b}
\beta^{-a_0-b}
3^{6a_0+b}
x^{-a_0\kappa_p}B_p^{a_0}y^b
\right].
}
\tag{4.2}
$$



Two budgets are now transparent.

- **Lower-factor budget**
  

$$
\boxed{q_L\kappa_p\le D}
  \tag{4.3}
$$


  makes every retained term a polynomial.

- **Upper-degree budget**
  

$$
\deg f_i\le\deg\phi_i+L-7.
$$


  Thus
  

$$
\boxed{g_P\ge L-6}
  \tag{4.4}
$$


  gives
  

$$
\deg f_i\le m-1.
$$



This improves the rectangular truncation used in Turn 12. The required upper-degree allowance is $L-7$, not a product of two truncation lengths.

The finite product identity is


$$
\boxed{Q_pf_i\equiv Q_c\phi_i\pmod{3^L}.}
\tag{4.5}
$$


It follows either by multiplying the displayed finite sum or by truncating the formal identity in the $3$-adically completed Laurent ring and then observing that both sides are actual polynomials.

Also,


$$
\boxed{f_i-\phi_i\in3^6\mathbb Z_3[y].}
\tag{4.6}
$$



### 4.3 Simultaneous hypotheses

The theorem below uses precisely:



$$
\boxed{
\begin{gathered}
P,L\ge7,\qquad p\ge1,\qquad h-1\ge P,\\
\Omega=H/3^{P-1}>4D+2P+3,\\
\text{the exact terminal length }\ell_{6+p}\text{ exists},\\
2v_3((A+1)!)\ge6+p,\\
\kappa_p=\ell_{6+p}-2,\qquad
\left\lfloor\frac{L-1}{6}\right\rfloor\kappa_p\le D,\\
\frac{\Omega-4D-2P-3}{2}\ge L-6.
\end{gathered}
}
\tag{4.7}
$$



The last line is equivalently


$$
\Omega\ge4D+2P+2L-9.
$$


It is the finite upper-gap budget, not merely a grid-separation condition.

---

## 5. Actual Schur forgetting, with the complete nonlinear remainder

### Theorem 5.1 — Precision-parametrized actual-core forgetting

Under (4.7), define


$$
J=\min(L+1,P+7,p+7),\qquad
V=\min(P+1,L+1,p+7).
$$


Then


$$
\boxed{S_{\rm act}-S_c\in3^JM_\nu(\mathbb Z_3)}
\tag{5.1}
$$


and


$$
\boxed{S_{\rm act}\in3^VM_\nu(\mathbb Z_3).}
\tag{5.2}
$$



The conclusion concerns the complete actual Schur complement, eliminating exactly $W=[U\ Y]$.

### Proof

#### Step 1: the product error gains one digit when paired with a corrected residual column

By (4.5),


$$
E_i:=\frac{Q_pf_i-Q_c\phi_i}{3^L}
$$


is integral. Since $\deg f_i,\deg\phi_i\le m-1$,


$$
\deg E_i\le A+m+1.
$$


Therefore


$$
\deg(E_iz_j)\le A+m+d=r_*,
\qquad r_*=\frac{3H-1}{2}.
$$


After endpoint subtraction and division by $y+1$, the degree is below $r_*$. Hence the unique valuation-zero pole is absent and


$$
\mathcal M(E_iz_j)\in3\mathbb Z_3.
$$


Since $\widehat z_j^{\,p}\equiv z_j\pmod3$,


$$
\mathcal M(E_i\widehat z_j^{\,p})\in3\mathbb Z_3.
$$


Thus


$$
G_p(f_i,\widehat z_j^{\,p})
\equiv G_c(\phi_i,\widehat z_j^{\,p})
\pmod{3^{L+1}}.
\tag{5.3}
$$



This extra digit uses the original finite degree boundary. It is not an unrestricted continuity assertion for $\mathcal M/3$.

#### Step 2: compare with the exact core-corrected columns

In the integral basis $[W,\widehat Z^{\,c}]$, write


$$
\Phi=W B+\widehat Z^{\,c}C,
$$


where $\Phi$ has columns $\phi_i$. Lemma 3.1 gives


$$
B\in3^PM,\qquad C\equiv I\pmod{3^P}.
\tag{5.4}
$$



Let


$$
T_p=K_p(W,\widehat Z^{\,c}),\qquad
K_p(f,g)=\mathcal M(R_pfg).
$$


The original degree argument gives


$$
T_p\in3M.
$$


Exact elimination yields


$$
\widehat Z^{\,p}
=
\widehat Z^{\,c}-3^6WE_p^{-1}T_p.
$$


Consequently,


$$
G_c(W,\widehat Z^{\,p})
=-3^6E_cE_p^{-1}T_p\in3^7M.
\tag{5.5}
$$


Here


$$
E_cE_p^{-1}
=I-3^6K_p(W,W)E_p^{-1}
$$


is integral; the eliminated inverse loss is only one.

If $A_f$ denotes the residual-coordinate matrix of the $f_i$, then


$$
A_f\equiv C\pmod{3^6},\qquad A_f\in\operatorname{GL}_\nu(\mathbb Z_3).
$$


Using (5.3)–(5.5),


$$
A_f^TS_p-C^TS_c
\in3^{\min(L+1,P+7)}M.
\tag{5.6}
$$


Thus, for


$$
U=C^{-T}A_f^T,
$$


we have


$$
U\equiv I\pmod{3^6},
\qquad
US_p-S_c\in3^{\min(L+1,P+7)}M.
\tag{5.7}
$$



#### Step 3: restore the whole actual producer remainder

Define the exact integral remainder


$$
\Delta_p=\frac{R-R_p}{3^p},\qquad \deg\Delta_p\le A+1,
$$


and put $s=p+6$. Then


$$
Q_{\rm act}=Q_p+3^s\Delta_p.
$$



Let


$$
\Phi_{\Delta_p}
=\mathcal M(\Delta_p\widehat Z^{\,p}\widehat Z^{\,p}),
\qquad
T_{\Delta_p}
=\mathcal M(\Delta_pW\widehat Z^{\,p}).
$$


The exact Schur identity is


$$
\boxed{
S_{\rm act}
=
S_p+3^s\Phi_{\Delta_p}
-3^{2s}T_{\Delta_p}^TE_{\rm act}^{-1}T_{\Delta_p}.
}
\tag{5.8}
$$


No higher perturbation terms are omitted: they are contained in $E_{\rm act}^{-1}$.

The same original degree argument gives


$$
T_{\Delta_p}\in3M,\qquad \Phi_{\Delta_p}\in3M.
$$


Therefore


$$
3^{2s}T_{\Delta_p}^TE_{\rm act}^{-1}T_{\Delta_p}
\in3^{2s+1}M,
$$


and


$$
\boxed{S_{\rm act}-S_p\in3^{p+7}M.}
\tag{5.9}
$$


This estimate accounts for the complete nonlinear remainder.

Combining (5.7) and (5.9),


$$
US_{\rm act}-S_c\in3^JM.
\tag{5.10}
$$


Since $S_c\in3^{P+1}M$, this first implies $S_{\rm act}\in3^VM$.

Finally,


$$
S_{\rm act}-S_c
=(US_{\rm act}-S_c)-(U-I)S_{\rm act}.
$$


The second term belongs to $3^{V+6}M$, and


$$
V+6\ge J.
$$


This proves (5.1). ∎

### What is, and is not, optimal here

The theorem supplies an explicit envelope for this construction:

- the inverse truncation needs at most $q_L\kappa_p$ powers of $x$;
- its maximal degree increase is exactly bounded by $L-7$;
- the supplied core approximation contributes the $P+7$ forgetting ceiling;
- restoring an otherwise unevaluated precision-$p$ remainder contributes the $p+7$ ceiling.

These are the strongest bounds obtained from the stated representative accuracy, degree argument, and mixed-force divisibility. This is **not** a claim that every possible refinement of the actual kernel must stop there. A stronger theorem would need additional cancellations or more detailed support information.

---

## 6. Consequences on the original depth-$16$ window

Retain


$$
j\equiv81\pmod{243},
\qquad
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad
C_{16}=147968\,3^{15}.
\tag{6.1}
$$


Thus $t=5$ and $D\ge486$.

### 6.1 Uniform depth $26$ and forgetting through precision $32$

Choose


$$
P=25,\qquad L=31,\qquad p=25.
$$


The exact tail requirement is


$$
5+v_3(k!)\ge31.
$$


Since


$$
v_3(53!)=23,\qquad v_3(54!)=26,
$$


we have


$$
\kappa_{25}=54.
$$


Also


$$
q_{31}=5,\qquad q_{31}\kappa_{25}=270<D.
$$



The required upper-gap inequality is


$$
\Omega_{25}\ge4D+103.
$$


But


$$
\frac{\Omega_{25}}D
=\frac{H}{3^{24}D}
>\frac{147968}{19683}>7.5.
$$


Together with $D\ge486$, this proves the gap inequality with considerable room.

For sufficiently large original indices, the factorial and $h$-conditions hold. Theorem 5.1 therefore gives


$$
\boxed{
S_c\in3^{26}M,\qquad
S_{\rm act}-S_c\in3^{32}M.
}
\tag{6.2}
$$



In particular, the first six normalized digits of


$$
S_{\rm act}/3^{26}
$$


agree with those of


$$
S_c/3^{26}.
$$


That agreement is symbolic and uniform on the stated window. No $B_{25}$ coefficients have been evaluated.

### 6.2 Moments and complete forcing

With the audited actual normalization


$$
S_{\rm act}=-3^{16}\Psi,\qquad
\mathsf H=\mathsf V^T\Psi\mathsf V,
$$


equation (6.2) gives


$$
\Psi,\mathsf H\in3^{10}M.
$$


Hence every original moment satisfies


$$
\mu_k\in3^{10}\mathbb Z_3,\qquad0\le k\le2\nu-2=D-4.
$$



The displacement identity and unit terminal generator likewise give


$$
t_{\rm act}-\theta r_{\rm act}\in3^{26}\mathbb Z_3^\nu.
$$


Thus the original forcing vector $b$, normalized at depth $16$, belongs to $3^{10}\mathbb Z_3^\nu$.

Put


$$
\mu_k^{\langle26\rangle}=\mu_k/3^{10},
\qquad
b^{\langle26\rangle}=b/3^{10}.
$$


The complete recurrence is still


$$
\boxed{
\mu_{i+\nu}^{\langle26\rangle}
+\sum_{k=0}^{\nu-1}f_k\mu_{i+k}^{\langle26\rangle}
=b_i^{\langle26\rangle},
\qquad0\le i\le\nu-2.
}
\tag{6.3}
$$


No extra moment $\mu_{2\nu-1}$ is added.

The complete endpoint return also remains:


$$
\boxed{
J^T\varepsilon+\omega
=
-\varepsilon
-s\bigl(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\bigr).
}
\tag{6.4}
$$


In particular, the terminal component of $\omega$ is not suppressed.

---

## 7. Where the support certificate stops

There are four distinct ways the construction can cease to apply:

1. the exact terminal factorial length ceases to exist at the requested precision;
2. endpoint divisibility fails at that precision;
3. the inverse multiplier exhausts the lower factor:
   

$$
q_L\kappa_p>D;
$$


4. core separation or the finite upper-degree budget fails:
   

$$
\Omega>4D+2P+3,\qquad
   g_P\ge L-6.
$$



These are failures of a certificate, not statements that the actual matrix becomes nonzero.

### 7.1 A useful balanced specialization

Taking


$$
L=P+6,\qquad p=P
$$


gives


$$
S_{\rm act}-S_c\in3^{P+7}M,\qquad
S_{\rm act}\in3^{P+1}M,
$$


provided


$$
\boxed{
\Omega\ge4D+4P+3,\qquad
\left\lfloor\frac{P+5}{6}\right\rfloor\kappa_P\le D,
}
\tag{7.1}
$$


together with the factorial and $h$-conditions.

Even the weaker choice designed only for vanishing, $L=P$, requires


$$
\Omega\ge4D+4P-9.
$$


Thus every such certified core precision has


$$
3^{P-1}<\frac{H}{4D}.
\tag{7.2}
$$


On a fixed real window $D/H\ge a>0$, the admissible $P$ is bounded independently of the original index.

Increasing $n$ within that fixed window does not make this support certificate arbitrarily deep.

### 7.2 Exact placement on the retained window

For $P=26$,


$$
\frac{\Omega_{26}}D
\in
\left(
\frac{147968}{59049},
\frac{295936}{59049}
\right),
$$


approximately $(2.506,5.012)$.

Therefore part, but not all, of the window can satisfy the necessary gap.

For example:

- if
  

$$
\Omega_{26}\ge4D+95,
$$


  the vanishing choice $L=26,p=20$ gives $S_{\rm act}\in3^{27}M$;

- if
  

$$
\Omega_{26}\ge4D+107,
$$


  then $L=32,p=26,\kappa_{26}=57$ gives
  

$$
S_{\rm act}-S_c\in3^{33}M,\qquad S_{\rm act}\in3^{27}M.
$$



For $P=27$, however,


$$
\frac{\Omega_{27}}D
<
\frac{295936}{177147}<1.671<4.
$$


Thus the basic separation $\Omega_{27}>4D+\cdots$ fails everywhere on the retained window.

Accordingly:



$$
\boxed{
\begin{array}{c|c}
\text{Scope}&\text{Certified conclusion by this construction}\\ \hline
\text{whole retained window}&S_{\rm act}\in3^{26}M,\quad S_{\rm act}\equiv S_c\pmod{3^{32}}\\
\text{specified portion satisfying the stronger gap}&S_{\rm act}\in3^{27}M,\quad S_{\rm act}\equiv S_c\pmod{3^{33}}\\
P=27\text{ core support on this window}&\text{not separated}
\end{array}
}
\tag{7.3}
$$



---

## 8. The first potential coefficient window at loss of separation

It is important to distinguish:

- the first **geometric support collision**;
- the first **nonzero complete Schur coefficient**.

They are not the same. Carries and pole-pair cancellations remain possible at a geometric collision.

### 8.1 A complete formula for the first unresolved uniform layer

Take the $P=25$ core representatives


$$
\phi_i=x^D\psi_i.
$$


More generally, for any $P\ge7$ covered by Lemma 3.1, define


$$
T_{ij}(y)=x^{H+D}(\beta+3y)\psi_i(y)\psi_j(y).
$$


Then


$$
Q_c\phi_i\phi_j=(y+1)T_{ij}.
$$



Because $\phi_i-\widehat z_i^{\,c}\in3^P\mathbb Z_3[y]$, orthogonality gives


$$
G_c(\phi_i,\phi_j)-(S_c)_{ij}\in3^{2P}M.
$$


Since $2P\ge P+2$, the first normalized core layer is therefore exactly


$$
\boxed{
\frac{(S_c)_{ij}}{3^{P+1}}
\equiv
\frac1{3^{P+1}}
\left[
-\frac{3^h}{4}\mathfrak f((y+1)T_{ij})
+
\sum_{\ell=0}^{P+1}
\ \sum_{\substack{c\ge1\ {\rm odd},\ 3\nmid c\\
c3^{h-\ell}\le4n-3}}
3^\ell c^{-1}
[y^{(c3^{h-\ell}-1)/2}]T_{ij}
\right]
\pmod3.
}
\tag{8.1}
$$



The whole bracket is evaluated before division. Its terms are not individually presumed divisible by $3^{P+1}$.

For $P=25$, equation (6.2) identifies the actual first unresolved layer:


$$
\boxed{
-\frac{S_{\rm act}}{3^{26}}
\equiv
-\frac{S_c}{3^{26}}
\pmod3,
}
\tag{8.2}
$$


with the right side given by (8.1).

Thus the remaining first-layer calculation does **not** require a new actual numerical producer.

### 8.2 The newly exposed finest-pole window

Put


$$
\omega=\frac H{3^P}.
$$


At the newly exposed pole layer $\ell=P+1$, the extraction positions are


$$
r_c=\frac{c\omega-1}{2}.
$$


Modulo $3$,


$$
\psi_i\equiv y^i,\qquad
T_{ij}\equiv(y^H-1)x^Dy^{i+j}.
$$


Consequently the individual finest-pole contribution is controlled by


$$
[y^{r_c-H-k}]x^D-[y^{r_c-k}]x^D,
\qquad0\le k\le D-4.
\tag{8.3}
$$



The two candidate coefficient windows are therefore


$$
\boxed{
[r_c-H-(D-4),\,r_c-H]\cap[0,D],
}
$$


and


$$
\boxed{
[r_c-(D-4),\,r_c]\cap[0,D].
}
\tag{8.4}
$$



For the first low pole $c=1$, $r=(\omega-1)/2$, the low-copy window first becomes nonempty when


$$
r\le2D-4,
\qquad\text{equivalently}\qquad
\boxed{\omega\le4D-7.}
\tag{8.5}
$$


When $D<r\le2D-4$, it is


$$
[r-(D-4),D].
$$



This is a concrete description of the first possible coefficient window after geometric separation is lost.

### 8.3 Why one must still evaluate the complete expression

Even the finest-pole window does not by itself give a surviving matrix entry.

For example, the pole indexed by $c$ and the pole indexed by


$$
c+2\cdot3^P
$$


have extraction positions differing by $H$, and their unit inverse weights agree modulo $3$. When both are inside the original cutoff, the corresponding low and high copies in (8.3) can cancel.

Moreover, lower pole layers in (8.1) carry higher coefficient digits and finite-return contributions. Those terms cannot be dropped merely because the newly exposed finest-pole contribution has been identified.

Thus the precise follow-on calculation is the **whole bracket in (8.1)**, not one isolated binomial coefficient.

---

## 9. What forgetting can and cannot say about relative valuations

Equation (6.2) is stronger than successive common zero layers: it says that the actual Schur matrix agrees with the core through precision $32$.

It nevertheless does not automatically protect a core inverse.

If $S_c$ is nonsingular, put


$$
s_c=-\min_{i,j}v_3((S_c^{-1})_{ij}).
$$


Since $S_c\in3^{26}M$,


$$
s_c\ge26.
$$


The established relative-matrix criterion gives a conditional consequence:



$$
\boxed{
s_c<32
\ \Longrightarrow\
\frac{\det S_{\rm act}}{\det S_c}\in1+3^{32-s_c}\mathbb Z_3,
}
\tag{9.1}
$$


and


$$
S_{\rm act}^{-1}-S_c^{-1}\in3^{32-2s_c}M.
\tag{9.2}
$$



But no supplied result proves $s_c<32$ for the moving original family.

Even (9.1) would not settle the endpoint cofactor. The exact endpoint changes remain


$$
e_{\rm act}-e_c\in3^6\mathbb Z_3^\nu,
\qquad
d_{\rm act}-d_c\in3^4\mathbb Z_3.
$$


Under the inverse hypothesis, the whole scalar comparison has the bound


$$
\begin{aligned}
&
\left(d_{\rm act}+e_{\rm act}^TS_{\rm act}^{-1}e_{\rm act}\right)
-\left(d_c+e_c^TS_c^{-1}e_c\right)\\
&\hspace{10mm}\in
3^{\min(4,\ 6-s_c,\ 32-2s_c)}\mathbb Z_3.
\end{aligned}
\tag{9.3}
$$


A relative conclusion additionally requires this exponent to exceed the valuation of the **whole core scalar**. That scalar may exhibit cancellation.

### A quantified obstruction to inference from common depth

Let $N\ge2$, fix $d\in3^{-1}\mathbb Z_3$, and normalize a primitive endpoint to $e_1$.

For


$$
\Theta_r=\operatorname{diag}(3^r,1,\ldots,1),
$$


one has


$$
v_3(\det\Theta_r)=r,
$$


while


$$
e_1^T\operatorname{adj}(\Theta_r)e_1
-3^Nd\det\Theta_r
=1-3^{N+r}d
$$


is a unit. The relative valuation is $-r$, which is unbounded.

The complete cofactor difference can also vanish at an invertible matrix. In dimension two, take


$$
\Theta=
\begin{pmatrix}
0&1\\
1&-3^Nd
\end{pmatrix}.
$$


Then $\det\Theta=-1$, and


$$
e_1^T\Theta^{-1}e_1=3^Nd.
$$


Hence


$$
e_1^T\operatorname{adj}(\Theta)e_1-3^Nd\det\Theta=0.
$$



These are not actual-family counterexamples. They prove that common depth, matrix invertibility, and a primitive endpoint do not logically imply the required relative-pair statement.

---

## 10. Exact depth-$26$ determinant pair and primitive normalization

Define


$$
\Theta=-S_{\rm act}/3^{26},
$$




$$
D_0=\det\Theta,
$$




$$
\boxed{
D_1=
e_{\rm act}^T\operatorname{adj}(\Theta)e_{\rm act}
-3^{26}d_{\rm act}\det\Theta.
}
\tag{10.1}
$$


The subtraction is part of the definition.

Since $\Psi=3^{10}\Theta$, the depth-$16$ pair satisfies


$$
\boxed{
\delta_0=3^{10\nu}D_0,\qquad
\delta_1=3^{10(\nu-1)}D_1.
}
\tag{10.2}
$$


If both members are nonzero,


$$
v_3(\delta_1)-v_3(\delta_0)
=-10+v_3(D_1)-v_3(D_0).
\tag{10.3}
$$



Thus the common dimension-scaled divisibility cancels.

Retain the actual endpoint law


$$
Q_{\rm act}(-1)=-F^2\xi_n,\qquad
F=(n-1)!,\qquad \xi_n\in1+3\mathbb Z_3.
$$


When $D_0\ne0$,


$$
\boxed{
\frac{\beta_1}{\beta_0}
=
\frac{3^{h-26}F^2\xi_n}{4}\frac{D_1}{D_0}.
}
\tag{10.4}
$$


If $D_0D_1\ne0$, the actual primitive denominator has


$$
\boxed{
v_3(q)=
\max\left\{
0,\,
h-26+2v_3(F)+v_3(D_1)-v_3(D_0)
\right\}.
}
\tag{10.5}
$$



There is no gain of $10\nu$, $26\nu$, or any similar dimension-multiplied quantity in this formula.

### Full gcd and whole error

Restore


$$
Q_n=\lambda Q_{\rm act},\qquad
R_{\rm rat}=\frac{4\lambda}{3^h}G_{\rm act},
$$




$$
H_{\rm complete}
=R_{\rm rat}+(e+\pi)Q_n(-1)vv^T,
$$




$$
\beta_0=\det R_{\rm rat},\qquad
\beta_1=Q_n(-1)v^T\operatorname{adj}(R_{\rm rat})v.
$$



With the least actual original clearing integer $\ell_{\rm clr}$, put


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
\boxed{g_\ell=\gcd(|A_\ell|,|B_\ell|).}
\tag{10.6}
$$


Every prime remains in this gcd.

When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and the whole same-index evaluated error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
}
\tag{10.7}
$$



Nothing in the new forgetting theorem proves the least clearer, the full gcd, the nonvanishing of (10.7), or its decay.

---

## 11. Concrete follow-on lemma and bounded exact arithmetic

### 11.1 The next useful lemma

The immediate local target is now more specific than “compute another producer digit”:

> **Core first-layer and relative-pair lemma.**  
> On the retained original window, evaluate the complete core coefficient expression (8.1) at $P=25$, including all carries before division. Determine the radical and endpoint action of
> 

$$
> -S_c/3^{26}\pmod3.
>
$$


> If it is singular, continue with the exact radical/complement Schur operator and transported endpoint. Establish either a usable core inverse-loss bound $s_c<32$, together with the necessary complete scalar comparison, or a direct nonvanishing and relative-valuation law for the actual pair $(D_0,D_1)$.

This uses the new actual-core forgetting interval. It does not assume the first layer is nonzero.

### 11.2 Small exact arithmetic audit of the precision budgets

No computation is needed for the symbolic proof. A bounded audit of its numerical thresholds uses only:

- $t=5$;
- $7\le P\le27$;
- factorial valuations $v_3(k!)$ for $0\le k\le243$;
- the rational constants $147968/3^{P-16}$;
- the lower bound $D\ge486$.

Expected exact output includes


$$
\kappa_{11}=\kappa_{12}=27,\qquad
\kappa_{19}=45,\qquad
\kappa_{25}=54,\qquad
\kappa_{26}=57,
$$




$$
q_{31}\kappa_{25}=270,\qquad
q_{32}\kappa_{26}=285,
$$


and exact rational verification of:

- the uniform $P=25,L=31$ gap;
- the conditional $P=26$ gaps;
- impossibility of $P=27$ core separation throughout the retained window.

This is a finite arithmetic audit of constants, not an original-family determinant computation.

### 11.3 Original-data first-layer calculation

**Inputs**

A certified original tuple


$$
(j,n,H,D,h)
$$


satisfying (6.1), and a target normalized precision


$$
1\le K\le6.
$$



**Calculation**

1. Construct the complete finite core blocks on the original indices.
2. Use normalized LOW/HIGH unit inverses, preserving $d,\ldots,m$.
3. Compute
   

$$
-S_c/3^{26}\pmod{3^K}.
$$


   At $K=1$, formula (8.1) with $\phi_i$ known modulo $3^{25}$ provides a direct complete coefficient evaluation.
4. Compute the exact core endpoint transport to the required modulus.
5. Evaluate the determinant and complete endpoint cofactor residues of the normalized finite matrix.

By (6.2), these matrix residues are the actual normalized Schur residues for $K\le6$. Also $e_{\rm act}\equiv e_c\pmod{3^6}$. The term $3^{26}d_{\rm act}$ is zero at these bounded moduli by valuation, though it remains in the exact pair.

**Expected verifiable output**

- the original-index certificate;
- all working moduli and normalization divisions;
- the full first normalized matrix, or an exact structured representation with a verified reconstruction identity;
- its rank, radical, and actual endpoint residue at $K=1$;
- determinant/cofactor residues at the chosen $K$;
- either nonzero residues certifying the corresponding valuations, or only stated lower bounds when the residues vanish.

No nonzero output is predicted.

The calculation is finite but can be very large. No feasible running-time or state-size claim is made.

For higher actual precision beyond the forgetting interval, the complete producer must again be supplied. Its exact signed system, full force, scalar denominator $\eta_n$, and certified precision losses remain obligations; a short terminal jet does not by itself make its evaluation inexpensive.

---

## 12. Proof-status ledger and conclusion

| Statement | Status |
|---|---|
| Precision-$11$/$12$ lift comparison with the same monic factor | Proved from accepted general saturation |
| Actual next zero layer $S_{\rm act}\in3^{19}M$ | Proved without computing a producer digit |
| Finite core representatives with explicit upper gap | Derived from the supplied complete finite return formulas |
| Weighted inverse transfer with degree growth $L-7$ | Proved |
| Complete nonlinear restoration identity | Retained exactly |
| Actual forgetting $S_{\rm act}-S_c\in3^{\min(L+1,P+7,p+7)}M$ | Proved under (4.7) |
| Uniform $S_{\rm act}\in3^{26}M$, $S_{\rm act}\equiv S_c\pmod{3^{32}}$ | Proved on the sufficiently large retained window |
| All original moments and complete forcing divisible by $3^{10}$ | Proved through the audited actual normalization |
| Fixed-window support ceiling | Quantified |
| First unresolved layer as a complete core coefficient calculation | Derived |
| Numerical value or rank of that first unresolved layer | Not computed |
| Residual determinant and complete cofactor nonvanishing | Unresolved |
| Usable relative determinant/cofactor valuation | Unresolved |
| Least clearer, final all-prime gcd, primitive denominator, whole nonzero error decay | Unresolved |

### New result

The principal advance is the actual-core forgetting theorem


$$
\boxed{
S_{\rm act}-S_c
\in3^{\min(L+1,P+7,p+7)}M,
}
$$


with explicit factorial-tail, lower-factor, finite-degree, and upper-gap conditions.

On the original fixed window this yields


$$
\boxed{
S_{\rm act}\in3^{26}M,\qquad
S_{\rm act}\equiv S_c\pmod{3^{32}}.
}
$$


Thus the next unresolved local calculation is a complete **core** calculation over a six-digit normalized interval, not a demand for an unevaluated new upstream producer.

### Exact remaining bottleneck

The method has reached a genuine support boundary. Beyond it, geometric separation no longer eliminates the candidate coefficient windows, and the whole finite expression—including pole-pair cancellations and carries—must be evaluated.

Even after that evaluation, the decisive local obligation remains


$$
\boxed{
D_0\ne0,\qquad D_1\ne0,\qquad
\text{a usable law for }v_3(D_1)-v_3(D_0).
}
$$


The global obligation remains same-index control of the least clearer, full gcd, actual primitive denominator, and the whole nonzero evaluated error.



$$
\boxed{\text{No unconditional proof or disproof of irrationality of }e+\pi
\text{ has been obtained.}}
$$


