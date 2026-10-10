> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The depth-$21$ residual vanishes: a finite-precision reduction to an explicit depth-$26$ Hankel operator

## Abstract

The failure of the old sufficient width inequality at $r=21$ does **not** signal a nonzero residual. In fact, the retained finite-core results imply substantially more:


$$
\boxed{S_c\in 3^{26}M(\mathbb Z_3).}
$$



The new argument does not replace the old safety factor $1/8$ by an assumed smaller constant. Instead, it uses complete core orthogonality to evaluate the residual to higher precision from the already established precision-$20$ corrected columns. The finite LOW projection, finite HIGH inverse, physical terminal $Y_m$, and all LOWER pole terms remain present.

Put


$$
\Omega=\frac{H}{3^{25}},\qquad c=\frac{\Omega-1}{2}.
$$


For sufficiently large original retained tuples, the first potentially nonzero core operator has the following explicit description:


$$
\boxed{
-\frac{S_c}{3^{26}}\pmod3
=
K_{26},\qquad
(K_{26})_{ij}
=
-[y^{\,c-i-j}](y-1)^D
\quad(0\le i,j<\nu).
}
\tag{A}
$$


Thus $K_{21},\ldots,K_{25}$ all vanish.

Formula (A) is a finite Hankel operator on the **unchanged original residual coordinates**, not an unnamed coefficient sum or an infinite-matrix replacement. It is nonzero exactly when


$$
c\le 2D-4.
$$


On an explicit infinite subfamily of the original progression satisfying


$$
3<\frac{\Omega}{D}<\frac72,
$$


its rank and radical are determined exactly:


$$
\boxed{
\operatorname{rank}K_{26}=2D-3-c,\qquad
\operatorname{rad}K_{26}
=
\operatorname{span}_{\mathbb F_3}\{e_0,\ldots,e_{t-1}\},
\quad
t=c-\frac{3D}{2}+2.
}
\tag{B}
$$


The transported actual endpoint is nonzero on that radical.

The passage to the actual residual uses, at their stated scope, the paid multiplier-chain conclusion and the stronger retained-reset linear bound. It gives the conditional actual conclusion


$$
S_{\rm act}\in3^{26}M,\qquad
-\frac{S_{\rm act}}{3^{26}}\equiv K_{26}\pmod3.
$$


No producer calculation or multiplier chain is repeated here.

These results do not resolve the rationality of $e+\pi$. The remaining local problem is now an explicitly identified radical Schur operator with its actual endpoint. The global obstruction remains the transport through actual contents and clearing factors to the final all-prime gcd, followed by comparison of the actual primitive denominator with the nonzero whole error at the same infinite original indices.

---

## 1. Exact domain, finite objects, and hypotheses

Retain


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


and the original window


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
\tag{1.1}
$$



All assertions below concern sufficiently large retained tuples. We may therefore require $h\ge27$, in addition to


$$
v_3(D)=5,\qquad 2\mid D,\qquad D\ge486.
$$



Write $x=y-1$, and retain the original finite coordinates


$$
U_u=x^u\quad(0\le u<D),
$$




$$
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),
$$


where


$$
\nu=\frac D2-1,\qquad d=D+\nu=\frac{3D}{2}-1.
$$


The physical HIGH terminal is $Y_m$.

Let


$$
W=[U\ Y],\qquad
F=Z-WE_c^{-1}C_c.
$$


The core form is


$$
G_c(f,g)=\mathcal M(Q_cfg),
\qquad
Q_c=(y+1)x^A(\beta+3y),
\qquad \beta=-71-A,
$$


with the complete functional


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^s)=(2s)!.
\tag{1.2}
$$



The finite denominator cutoff remains


$$
2v+1\le4n-3=4H-4D+5.
\tag{1.3}
$$



### Retained core mathematics used

The proof uses the following results from the accepted finite-core audit.

1. The basis $[W,F]$ is integral unimodular, and
   

$$
G_c(W,F)=0.
$$



2. The only possible nonunit eliminated inverse loss is
   

$$
E_c^{-1}\in3^{-1}M(\mathbb Z_3).
$$



3. The precision-$20$ theorem gives
   

$$
S_c=G_c(F,F)\in3^{21}M.
$$



4. The finite-walk support conclusion in A4 turn2, §5.6, applies for $1\le p\le20$:
   

$$
F_i\equiv x^D\psi_{i,p}\pmod{3^p},
$$


   

$$
\deg\psi_{i,p}\le m-D,\qquad
   \operatorname{supp}\psi_{i,p}
   \subseteq I_{\Omega_{20}}(pD/2),
   \qquad
   \Omega_{20}=\frac{H}{3^{19}}.
   \tag{1.4}
$$


   This is stronger than retaining only the terminal statement at $p=20$, and its stated $p$-scope is important below.

5. In the normalized block notation
   

$$
E_c=
   \begin{pmatrix}
   3L&3X\\
   3X^T&E_Y
   \end{pmatrix},
   \qquad
   C_c=\binom{3B}{3V^T},
$$


   one has
   

$$
B\in3^{20}M.
   \tag{1.5}
$$



No new general width-$21$ theorem is assumed.

---

## 2. Why the old width failure is not the relevant residual obstruction

At $r=21$, the old sufficient condition asks for


$$
8\bigl(W_{21}+2D+2\bigr)<\Omega_{21}.
$$


Its failure only says that this particular uniform allowance no longer certifies every operation by itself.

There is a sharper route for the **actual residual**. Complete orthogonality makes the residual insensitive, to twice the approximation precision, to a small error in the corrected columns.

### Lemma 2.1 — Stationary finite-Gram approximation

Suppose


$$
F^*=F+3^p\Delta
$$


with integral polynomial columns of degree at most $m$. If $S_c\in3^sM$, then


$$
G_c(F^*,F^*)-S_c
\in3^{\min(p+s,\,2p)}M.
\tag{2.1}
$$



#### Proof

Decompose $\Delta$ in the original integral basis:


$$
\Delta=WC+FD,
\qquad C,D\ \text{integral}.
$$


Complete orthogonality gives


$$
G_c(F,\Delta)=S_cD.
$$


Consequently,


$$
G_c(F^*,F^*)
=
S_c
+3^p(S_cD+D^TS_c)
+3^{2p}G_c(\Delta,\Delta).
$$


The functional is integral on integral polynomial inputs at the retained cutoff. The last term is therefore integral after division by $3^{2p}$, proving (2.1). ∎

With $p=20$ and $s=21$,


$$
\boxed{S_c\equiv G_c(F^*,F^*)\pmod{3^{40}}.}
\tag{2.2}
$$



This uses no new inverse and therefore introduces no new LOW loss.

### The requested depth-$21$ margin

Take the established representative


$$
F_i^*=x^D\psi_i,
\qquad
\operatorname{supp}\psi_i\subseteq I_{\Omega_{20}}(10D).
$$


The complete endpoint-subtracted core product is


$$
x^H\,x^D(\beta+3y)\psi_i\psi_j.
\tag{2.3}
$$


Its local width is at most


$$
21D+1.
$$



To evaluate modulo $3^{22}$, use the grid


$$
\Omega_{22}=\frac{H}{3^{21}}.
$$


Every relevant extraction is on its odd half-grid, whereas the polynomial support is within $21D+1$ of its integer grid. The exact sufficient margin is


$$
21D+1<\frac{\Omega_{22}-1}{2}.
\tag{2.4}
$$


The original window gives


$$
\frac{\Omega_{22}}D>\frac{147968}{729}>202,
$$


so (2.4) holds with a large positive margin.

Thus


$$
G_c(F^*,F^*)\in3^{22}M,
$$


and (2.2) proves


$$
\boxed{K_{21}=0.}
$$



This is not an unexplained replacement of $1/8$ by $1/2$. The quantity being bounded is the fully assembled residual polynomial (2.3), whose width is explicitly known. The five finite operations are reused at their established precision; their approximation error is then paid by the exact stationary identity.

---

## 3. The five finite operations and the first two corrected-column digits

For the stronger result, the terminal contribution and its actual LOW feedback must be identified rather than hidden inside a support bound.

The five operations enter as follows.

| Finite operation | Information retained or evaluated here |
|---|---|
| Complete initial HIGH force | Its first normalized digit is exactly the physical $Y_m$ charge |
| Finite inverse copies | $R e_{Y_m}=e_{Y_d}$, with the original finite HIGH boundaries |
| Complete return on internal copies | Retained in the nested support theorem (1.4), including LOWER poles |
| Actual LOW projection of a lower-edge column | $Y_d$ projects to its actual remainder modulo $x^D$ |
| Physical upper-terminal return | The $Y_m$-to-$Y_d$ return is used, not an infinite Toeplitz replacement |

We now check the first two digits explicitly.

### 3.1 The complete normalized HIGH force modulo $3$

For $0\le i<\nu$, $d\le b\le m$,


$$
i+b\le\nu-1+m=r_1-1,
\qquad r_1=\frac{H-1}{2}.
$$


The top $\beta x^H$ extraction is absent by degree. The extra $3y$ reaches the top extraction only when


$$
i=\nu-1,\qquad b=m.
$$



At the LOWER pole $r_1$, after division by the mixed-block factor $3$, use


$$
x^H\equiv y^H-1\pmod3.
$$


Since $i+b\le r_1-1$, its extraction vanishes. Every further LOWER pole has an additional factor $3$ after normalization. The factorial term also vanishes.

Therefore


$$
\boxed{
V^T\equiv e_{Y_m}e_{\nu-1}^T\pmod3.
}
\tag{3.1}
$$



### 3.2 Actual LOW feedback

Let $r_d$ be the remainder of $y^d$ on division by $x^D$:


$$
y^d=r_d+x^Dq_d,\qquad \deg r_d<D,
$$


where


$$
q_d(y)=
\sum_{a=0}^{\nu}
\binom{D+a-1}{a}y^{\nu-a},
\qquad \deg q_d=\nu.
\tag{3.2}
$$



The retained finite projection theorem gives


$$
L^{-1}Xe_{Y_d}\equiv r_d\pmod3.
\tag{3.3}
$$


The finite HIGH inverse gives


$$
Re_{Y_m}=e_{Y_d}.
\tag{3.4}
$$



Solving the displayed finite block equations, using $B\in3^{20}M$, now yields


$$
\boxed{
F_i\equiv
x^D\bigl(y^i-3\delta_{i,\nu-1}q_d(y)\bigr)
\pmod9.
}
\tag{3.5}
$$



In particular,


$$
F_i\equiv z_i\pmod3.
\tag{3.6}
$$



Equation (3.5) includes the physical terminal charge and its actual LOW return. Omitting either would change this calculation.

---

## 4. A digitwise representative in the original finite space

Using (1.4), choose


$$
F_i^*=x^D\sum_{a=0}^{19}3^a\phi_{i,a}(y)
\equiv F_i\pmod{3^{20}},
\tag{4.1}
$$


with


$$
\deg\phi_{i,a}\le m-D,
\qquad
\operatorname{supp}\phi_{i,a}
\subseteq I_{\Omega_{20}}\bigl((a+1)D/2\bigr).
\tag{4.2}
$$


The first two digits may be chosen as


$$
\phi_{i,0}=y^i,
\qquad
\phi_{i,1}=-\delta_{i,\nu-1}q_d.
\tag{4.3}
$$



Here is why the simultaneous choice is legitimate. Multiplication by the monic polynomial $x^D$ is injective over $(\mathbb Z/3^p\mathbb Z)[y]$. Thus the quotients supplied by (1.4) agree at their common precision. The support sets are nested as $p$ increases, so coefficientwise digit extraction gives (4.2). Replacing the first digit lift by the exact polynomial in (4.3) does not enlarge its support.

Every polynomial in (4.1) still has degree at most $m$. No HIGH coordinate beyond $Y_m$ is introduced.

---

## 5. All terms of total digit order at least two vanish modulo $3^{27}$

Consider a product of digits with


$$
s=a+b\ge2.
$$


Its contribution carries the explicit factor $3^s$. To prove that it is zero modulo $3^{27}$, it suffices to evaluate its functional modulo


$$
3^q,\qquad q=27-s.
$$



For $s\ge27$, integrality already suffices. Suppose $2\le s\le26$.

After removing $y+1$, its polynomial is


$$
x^H\,x^D(\beta+3y)\phi_{i,a}\phi_{j,b}.
$$


The local width is at most


$$
w_s=\left(2+\frac s2\right)D+1.
\tag{5.1}
$$



At precision $3^q$, the support of $x^H$ lies on the grid


$$
H/3^{q-1}.
$$


Combining this with the $\Omega_{20}$-grid in (4.2), the relevant common grid is


$$
\Lambda_q=\frac{H}{3^{\max(19,q-1)}}.
\tag{5.2}
$$


Every retained pole contributing modulo $3^q$, including the top pole, is on the odd half-grid relative to $\Lambda_q$.

The worst comparison is $s=2$, $q=25$. Put


$$
\Omega_{25}=\frac{H}{3^{24}}.
$$


The original window gives


$$
\frac{\Omega_{25}}D
>
\frac{147968}{19683}
>
\frac{15}{2}.
\tag{5.3}
$$


Hence


$$
3D+1<\frac{\Omega_{25}-1}{2}.
$$



For $3\le s\le7$, the grid separation grows by a factor $3$ at each step, whereas $w_s$ grows only by $D/2$. For $s\ge7$, the common grid is at least $\Omega_{20}$, and


$$
w_s\le15D+1\ll\frac{\Omega_{20}-1}{2}.
$$



Thus every relevant coefficient extraction vanishes. The factorial contribution vanishes because $h\ge27$. We have proved


$$
\boxed{
\text{Every term with }a+b\ge2
\text{ contributes }0\pmod{3^{27}}.
}
\tag{5.4}
$$



All LOWER poles are included in this argument. It is not a top-pole-only calculation.

---

## 6. An evaluated complete low-degree moment

The remaining terms have total digit order $0$ or $1$. By (4.3), their low polynomial factors have degree at most $2D$. The following lemma evaluates the complete functional on precisely those factors.

### Lemma 6.1 — Complete moment at depth $26$

Set


$$
\Omega=\frac{H}{3^{25}},\qquad c=\frac{\Omega-1}{2}.
$$


For an integral polynomial $P$ with $\deg P\le2D$,


$$
\boxed{
\mathcal M\bigl((y+1)x^H P(y)\bigr)
\equiv
3^{26}[y^c]P(y)
\pmod{3^{27}}.
}
\tag{6.1}
$$



#### Proof

The original window implies


$$
\frac{\Omega}{D}>
\frac{147968}{59049}>\frac52,
\tag{6.2}
$$


so $\deg P<\Omega$.

The top extraction is absent because


$$
\deg(x^HP)\le H+2D<\frac{3H-1}{2}.
$$


The factorial term is zero modulo $3^{27}$.

Write every LOWER denominator uniquely as


$$
\alpha H/3^t,\qquad
\alpha>0\text{ odd},\quad3\nmid\alpha,
$$


subject to the original cutoff. Its functional weight is


$$
3^{t+1}\alpha^{-1}.
$$



Only $0\le t\le25$ can contribute modulo $3^{27}$.

#### Interior layers $1\le t\le24$

At layer $t$, the required precision of $x^H$ is $3^{26-t}$, whose support lies on


$$
H/3^{25-t}.
$$


Together with the pole grid $H/3^t$, the half-grid separation is at least that of


$$
H/3^{24}=3\Omega.
$$


By (6.2), half this spacing exceeds $2D$. Every extraction therefore vanishes.

#### The layer $t=0$

The only LOWER denominator at this layer is $H$, with weight $3$, at


$$
r_1=\frac{H-1}{2}.
$$


Modulo $3^{26}$, the relevant coefficients of $x^H$ lie on the $\Omega$-grid.

Because $\deg P<\Omega$, the only possible coefficient of $P$ is its coefficient at


$$
c=\frac{\Omega-1}{2}.
$$


The accompanying index of $x^H$ is


$$
k=L\Omega,\qquad L=\frac{3^{25}-1}{2},
$$


and $L\equiv1\pmod3$.

For $0<k<H$,


$$
\binom Hk=\frac Hk\binom{H-1}{k-1}.
$$


Also


$$
\binom{H-1}{k-1}\equiv(-1)^{k-1}\pmod3.
$$


Including the sign in the coefficient of $(y-1)^H$, and using that $H$ is odd, gives


$$
\frac{[y^{L\Omega}]x^H}{3^{25}}
\equiv L^{-1}\equiv1\pmod3.
$$


This layer contributes


$$
3^{26}[y^c]P.
$$



#### The layer $t=25$

Here the weight is $3^{26}\alpha^{-1}$, so only


$$
x^H\equiv y^H-1\pmod3
$$


is needed.

Since $\deg P<\Omega$, the only possible bottom and upper-end extractions occur at


$$
c,\qquad H+c.
$$


Their denominators are respectively


$$
\Omega,\qquad 2H+\Omega.
$$


Both are inside the retained finite cutoff. Their normalized units are


$$
1,\qquad 2\cdot3^{25}+1,
$$


which are equal modulo $3$. The two polynomial coefficients have opposite signs, from $-1$ and $y^H$. Consequently these two contributions cancel modulo $3^{27}$.

No other term remains. This proves (6.1). ∎

The cancellation at $t=25$ is important. Discarding LOWER pole terms would give an incomplete derivation even though the final displayed kernel is simple.

---

## 7. Evaluation of the first surviving core operator

Apply Lemma 6.1 to the total digit-order-zero term:


$$
G_c(z_i,z_j)
=
\mathcal M\!\left(
(y+1)x^H x^D(\beta+3y)y^{i+j}
\right).
$$


Since $\beta\equiv1\pmod3$,


$$
G_c(z_i,z_j)
\equiv
3^{26}[y^{c-i-j}]x^D
\pmod{3^{27}}.
\tag{7.1}
$$



The total digit-order-one terms have an additional factor $3$. Their low factors have degree at most $2D$, so Lemma 6.1 makes them divisible by $3^{27}$.

Combining (5.4), (7.1), and the stationary congruence (2.2) proves:

### Theorem 7.1 — Explicit depth-$26$ core residual

On the unchanged original window, for sufficiently large retained tuples,


$$
\boxed{
S_c\equiv3^{26}H_c\pmod{3^{27}},
\qquad
(H_c)_{ij}=[y^{c-i-j}](y-1)^D.
}
\tag{7.2}
$$


In particular,


$$
\boxed{S_c\in3^{26}M,\qquad K_{21}=\cdots=K_{25}=0.}
$$



The depth-$26$ operator is


$$
\boxed{K_{26}=-H_c.}
$$



### Compact exact description

For every original pair $0\le i,j<\nu$,


$$
(K_{26})_{ij}
=
\begin{cases}
-(-1)^{D-c+i+j}\displaystyle\binom D{c-i-j}\pmod3,
&0\le c-i-j\le D,\\[2mm]
0,&\text{otherwise}.
\end{cases}
\tag{7.3}
$$



This is a finite Hankel band. Reversing one coordinate order makes it a truncated Toeplitz operator. Its coefficients can also be evaluated digitwise by


$$
\binom Da\equiv\prod_{\ell\ge0}\binom{D_\ell}{a_\ell}\pmod3,
\tag{7.4}
$$


where $D_\ell,a_\ell$ are ternary digits. No original full matrix is needed to specify the operator.

### Exact nonvanishing criterion

The maximum value of $i+j$ is $D-4$. Thus $H_c=0$ if $c>2D-4$.

Conversely, if $c\le2D-4$, put


$$
s_0=c-D.
$$


The original lower window bound gives $c>D$ for sufficiently large tuples, and


$$
0\le s_0\le D-4.
$$


Choose $i,j<\nu$ with $i+j=s_0$. Then


$$
(H_c)_{ij}=[y^D]x^D=1.
$$


Therefore


$$
\boxed{K_{26}\ne0\iff c\le2D-4.}
\tag{7.5}
$$



There is no uniform claim that every original tuple has a nonzero depth-$26$ digit.

---

## 8. Rank and radical on an infinite original subfamily

Consider the stricter inequalities


$$
3<\frac{\Omega}{D}<\frac72.
\tag{8.1}
$$


This is a subwindow of the original window, not a new index family.

Put


$$
s_0=c-D,\qquad
t=s_0-(\nu-1)=c-\frac{3D}{2}+2,
$$




$$
r=\nu-t=2D-3-c.
\tag{8.2}
$$


For sufficiently large tuples satisfying (8.1),


$$
t\ge2,\qquad r>0.
$$



Entries with $i+j<s_0$ vanish, while entries on $i+j=s_0$ equal $-1$ in $K_{26}$. Consequently:

* rows and columns $0,\ldots,t-1$ are zero;
* on indices $t,\ldots,\nu-1$, reversal of one ordering gives a triangular matrix with diagonal $-1$.

Hence


$$
\boxed{
\operatorname{rank}K_{26}=r=2D-3-c,
}
$$


and


$$
\boxed{
\operatorname{rad}K_{26}
=
\operatorname{span}_{\mathbb F_3}\{e_0,\ldots,e_{t-1}\}.
}
\tag{8.3}
$$



This proves the full radical, not merely a lower bound on its dimension or the existence of one nonzero minor.

### 8.1 Infinitely many original indices satisfy this subwindow

Let


$$
\alpha=\log_3 4.
$$


It is irrational, since a rational equality $\alpha=a/b$ would imply $4^b=3^a$.

Write the original progression as


$$
j=84645+531441\,k,\qquad k\ge0.
$$


The rotation step $531441\,\alpha$ is irrational. Therefore the fractional parts of $j\alpha$ visit every nonempty open interval infinitely often. This standard density fact follows, for example, by the pigeonhole construction of arbitrarily small nonzero rotation steps, followed by their successive translates around the unit circle.

For $N=\lceil j\alpha\rceil$, set $H=3^N$. Then


$$
\frac DH
=
1-3^{j\alpha-N}+3^{-N}.
\tag{8.4}
$$


The term $3^{-N}$ tends to zero. Thus every open subinterval of the original $D/H$-window is attained infinitely often by original $j$'s.

Condition (8.1) corresponds to


$$
\frac{2}{7\cdot3^{25}}
<
\frac DH
<
\frac{1}{3\cdot3^{25}}.
\tag{8.5}
$$


It lies strictly inside (1.1), because


$$
\frac{147968}{59049}<3,
\qquad
2\frac{147968}{59049}>\frac72.
$$


Choosing a closed interval strictly inside (8.5) absorbs the vanishing correction in (8.4). Hence infinitely many **original** indices satisfy (8.1).

This establishes the required infinite scope; it is not an inference from finitely many favorable tuples.

---

## 9. Transport to the actual residual and actual endpoint

The repaired receipt gives the exact original-object identity


$$
Q_{\rm act}=Q_c+3^6R_{\rm prod},
\qquad R_{\rm prod}=3\mathscr R,
$$


hence


$$
E_{\rm act}=E_c+3^7J,
\qquad
J=\bigl(\mathcal M(\mathscr R\,ww')\bigr).
\tag{9.1}
$$



I do not redo the four-multiplier chain. At its stated retained-producer scope, its conclusion is


$$
\mathcal Q\in3^{21}M.
\tag{9.2}
$$


The stronger linear result in A4 turn2, §7, uses the actual reset, exact coefficient formula, and endpoint identity:


$$
\Phi_R\in3^{21}M.
\tag{9.3}
$$


The weaker bound $\Phi_R\in3^{20}M$ would not suffice to identify the actual depth-$26$ digit with the core digit.

Using (9.2)–(9.3) in


$$
S_{\rm act}=S_c+3^6\Phi_R-3^{13}\mathcal Q
$$


gives the following explicitly scoped implication:


$$
\boxed{
S_{\rm act}\in3^{26}M,\qquad
-\frac{S_{\rm act}}{3^{26}}\equiv K_{26}\pmod3.
}
\tag{9.4}
$$



The new core theorem is independent of the producer. Equation (9.4) additionally uses the retained paid-chain and actual-reset results; this report is not a substitute for their independent review.

### 9.1 The actual endpoint

Let


$$
e_{\rm act}
=
Z(-1)^T-C_{\rm act}^TE_{\rm act}^{-1}w,
\qquad w=W(-1)^T.
$$


Complete core orthogonality and (9.1) give


$$
F_{\rm act}=F-3^7WE_{\rm act}^{-1}T.
$$


Since $T\in3M$ and $E_{\rm act}^{-1}\in3^{-1}M$,


$$
e_{\rm act}\equiv F(-1)^T\pmod3.
$$


Using (3.6),


$$
\boxed{
(\bar e_{\rm act})_i=(-1)^i.
}
\tag{9.5}
$$



On the subfamily (8.1), the radical contains $e_0$, and the endpoint has value $1$ there. Thus its restriction to the radical is nonzero.

The actual diagonal remains


$$
d_{\rm act}=w^TE_{\rm act}^{-1}w\in3^{-1}\mathbb Z_3.
\tag{9.6}
$$


It has not been discarded.

---

## 10. The distinguished pair, its updated loss, and the residual inverse still to be paid

At normalization $26$, put


$$
U=-S_{\rm act}/3^{26}.
$$


The distinguished pair is


$$
\mathcal D_0=\det U,
$$




$$
\mathcal D_1
=
e_{\rm act}^T\operatorname{adj}(U)e_{\rm act}
-
3^{26}d_{\rm act}\det U.
\tag{10.1}
$$



If


$$
a=v_3(\det U),\qquad
b=v_3\!\left(e_{\rm act}^T\operatorname{adj}(U)e_{\rm act}\right),
$$


then the sufficient relative target is now


$$
\boxed{a<\infty,\qquad b<a+25.}
\tag{10.2}
$$


Indeed, the diagonal term has valuation at least $a+25$.

This is exactly the old depth-$21$ target transported to the new normalization. Since


$$
\Upsilon_{21}=3^5U,
$$


one has


$$
a_{21}=5\nu+a,\qquad
b_{21}=5(\nu-1)+b,
$$


and


$$
b_{21}<a_{21}+20
\iff
b<a+25.
$$



### 10.1 What the proved rank says—and does not say

On (8.1), the bordered reduction modulo $3$,


$$
\begin{pmatrix}
K_{26}&\bar e_{\rm act}\\
\bar e_{\rm act}^T&0
\end{pmatrix},
$$


has rank


$$
r+2,
\tag{10.3}
$$


because the endpoint is nonzero on the $t$-dimensional radical.

Nevertheless, $t\ge2$, so both the determinant and the first bordered determinant still vanish modulo $3$. Rank alone does not evaluate their next digits.

### 10.2 Concrete next residual lemma

Order coordinates as the proved nondegenerate complement followed by the proved radical, and write


$$
U=
\begin{pmatrix}
A&B\\
B^T&C
\end{pmatrix},
\qquad
e_{\rm act}=\binom{e_C}{e_R}.
$$


The complement $A$ is a $3$-adic unit matrix. Define


$$
R=C-B^TA^{-1}B\in3M,
\qquad
f=e_R-B^TA^{-1}e_C.
\tag{10.4}
$$


The complete bordered diagonal after this elimination is


$$
3^{26}d_{\rm act}-e_C^TA^{-1}e_C.
\tag{10.5}
$$



The next concrete obligation is to evaluate


$$
\boxed{R/3\pmod3,\qquad f\pmod3,}
\tag{10.6}
$$


and, if necessary, its next effective operator.

An accessible sufficient theorem would be:

> If $V=R/3$ is a unit matrix and
> 

$$
> \bar f^T\operatorname{adj}(\bar V)\bar f\ne0,
>
$$


> then
> 

$$
> a=t,\qquad b=t-1,
>
$$


> so (10.2) holds and $\mathcal D_1\ne0$.

To verify this, use


$$
\det U=\det A\,\det R
$$


and


$$
e_{\rm act}^T\operatorname{adj}(U)e_{\rm act}
=
\det A\left(
f^T\operatorname{adj}(R)f
+
(e_C^TA^{-1}e_C)\det R
\right).
$$


If $R=3V$, the first displayed term has order $3^{t-1}$, while the second has order at least $3^t$.

The inverse of $R$, if used, is


$$
R^{-1}=3^{-1}V^{-1}.
$$


That new division must be paid independently. The inverse of $E_{\rm act}$ does not pay for it.

---

## 11. A rigorous link from cofactor structure to gcd information

A rank theorem matters globally only after it is transported to the actual final integers. The following elementary link identifies what must be transported.

### Lemma 11.1 — Determinantal divisor common factor

Let $M$ be an integral $N\times N$ matrix, let $u$ be an integral vector, and let $\delta$ be integral. Let $\Delta_{N-1}(M)$ be the gcd of all $(N-1)$-minors. Then


$$
\Delta_{N-1}(M)
\mid
\gcd\!\left(
\det M,\,
u^T\operatorname{adj}(M)u-\delta\det M
\right).
\tag{11.1}
$$



#### Proof

Every entry of $\operatorname{adj}(M)$ is an $(N-1)$-minor up to sign, hence is divisible by $\Delta_{N-1}(M)$. The same divisor divides $\det M$, either by Laplace expansion or by Smith normal form. Both displayed integers are therefore divisible by it. ∎

Over $\mathbb Z_3$, rank $N-t$ modulo $3$ implies


$$
v_3(\Delta_{N-1}(M))\ge t-1.
\tag{11.2}
$$


If the next radical Schur matrix in §10.2 is a unit after exactly one division by $3$, and the distinguished pairing is nonzero, the determinant/bordered-pair common valuation is exactly $t-1$.

For the unnormalized residual $S_{\rm act}= -3^{26}U$, the corresponding cofactor scale contains


$$
3^{26(\nu-1)}.
$$


The possible $3^{-1}$ in $d_{\rm act}$ is harmless for this particular common-divisor lower bound because its determinant term has the much larger factor $3^{26\nu}$.

### What is still missing for the actual all-prime gcd

These statements are not yet statements about $g_\ell$. One must prove the exact transport through:

* the actual column contents;
* the actual multiplier;
* every paid division;
* the least simultaneous clearer;
* the determinant/cofactor identities producing $\beta_0,\beta_1$.

For example, if an exact original-object identity gives final integers as a common rational scale times a determinant/bordered pair, then prime by prime


$$
v_p(g_\ell)
=
v_p(\text{actual common scale})
+
\min\bigl(v_p(\text{first observation}),v_p(\text{second observation})\bigr).
$$


The common scale cannot be guessed from the auxiliary core calculation.

A genuinely useful all-prime theorem would provide verified bounds for these valuations **after** all actual contents and clearing factors, with a summed logarithmic bound strong enough for the whole-error comparison below.

---

## 12. Complete forcing, final gcd, primitive denominator, and whole error

Nothing in the argument replaces the actual corrected columns or their forcing. In particular, the original closure remains


$$
J^T\varepsilon+\omega
=
-\varepsilon-s_{\rm ret}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
$$


The logarithmic forcing, both exponential boundary charges, finite returns, exterior constants, and physical terminal remain in the original complete construction.

The polynomials $F^*$ used above are approximation devices for proving a core congruence. They are not substitutes for the actual determinant multiplier.

Retain


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over **all primes**. For $B_\ell\ne0$, retain the actual primitive quantities


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The complete same-index error is


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}
{g_\ell}
\det H_{\rm complete}.
}
\tag{12.1}
$$



An irrationality proof still requires, on the same infinite original indices,


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


Neither the new rank formula nor ternary local divisibility alone establishes this all-prime comparison.

The independent prime-$2$ and prime-$29$ computations concern different original families and different stated scopes. They cannot be combined with the present subfamily to manufacture an unproved simultaneous denominator estimate.

---

## 13. Bounded exact arithmetic and proof-status ledger

### 13.1 No closed computation needs repetition

No producer calculation, four-multiplier chain, prime-$29$ assembly, or repaired dyadic evaluator test is required again.

The new proof is symbolic. Its elementary numerical margins use the bounded inputs


$$
147968,\quad59049,\quad19683,\quad486.
$$


Expected verifiable outputs include


$$
2\cdot147968-5\cdot59049=691>0,
$$




$$
2\cdot147968-15\cdot19683=691>0,
$$




$$
147968<3\cdot59049,
$$




$$
4\cdot147968>7\cdot59049.
$$


These verify the moment spacing and the containment of the infinite subwindow.

### 13.2 Optional compact actual-tuple certificate

For one coordinator-selected certified original tuple, bounded inputs are:

* exact $j,h,D,m,\nu$;
* verification of the original progression and window;
* $\Omega=H/3^{25}$ and $c=(\Omega-1)/2$.

Expected outputs are:

1. the band formula (7.3), represented by its binomial coefficient sequence;
2. whether $c\le2D-4$;
3. if $3<\Omega/D<7/2$, the integers
   

$$
t=c-\frac{3D}{2}+2,\qquad r=2D-3-c;
$$


4. the zero leading rows and columns and the unit anti-triangular trailing block;
5. the endpoint vector $((-1)^i)_{0\le i<\nu}$ modulo $3$.

This is a compact exact certificate of the proved operator. It need not construct the huge original matrix.

A calculation of the **next** radical operator additionally requires certified original actual blocks to sufficient precision. Its expected output must be $R/3\bmod3$, the transported actual $f$, and the complete bordered observation—not merely a rank or one selected minor. Such a calculation establishes only the chosen tuple.

### 13.3 Status

| Statement | Status |
|---|---|
| Stationary finite-Gram approximation | New proof |
| $K_{21}=0$ without changing the safety factor | New proof |
| $S_c\in3^{26}M$ | New proof from retained finite-core results |
| Explicit depth-$26$ Hankel operator | New evaluated formula |
| Exact nonvanishing criterion for $K_{26}$ | New proof |
| Rank and full radical on $3<\Omega/D<7/2$ | New proof |
| Infinitely many original indices in that subwindow | New proof |
| Actual depth-$26$ identification | Conditional on the retained paid-chain and stronger actual-reset linear bound |
| Actual endpoint modulo $3$ | Proved from the exact actual-block identity and retained integrality |
| Next radical Schur digit and distinguished pairing | Open |
| Transport through actual contents and least clearer | Open |
| Final all-prime gcd versus nonzero whole error | Open |
| Rationality or irrationality of $e+\pi$ | Unresolved |

---

## Conclusion

The first potentially nonzero depth-$21$ CORE residual is zero. The old width failure was a limitation of a sufficient operation-wide allowance, not a surviving boundary observation.

The substantive new result is


$$
\boxed{
S_c\in3^{26}M,\qquad
-\frac{S_c}{3^{26}}\equiv
-\bigl([y^{c-i-j}](y-1)^D\bigr)_{0\le i,j<\nu}\pmod3,
\quad
c=\frac{H/3^{25}-1}{2}.
}
$$



This operator is explicitly nonzero on an infinite subfamily of the original progression, and its rank, radical, and endpoint restriction are proved there. The next local bottleneck is the once-normalized Schur operator on that radical, with its independently paid inverse and complete bordered diagonal.

The global bottleneck is unchanged but now more concretely connected to the local calculation: the determinant/cofactor information must survive the actual contents, multiplier, divisions, and least simultaneous clearer to control the **final all-prime gcd and actual primitive denominator**, and must then be compared with the **nonzero whole error at the same infinite original indices**.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ has been obtained.}}
$$


