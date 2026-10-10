> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1, Turn 3 — A finite-band proof that the sixth residual digit vanishes

## Executive conclusion

On the **entire original domain**


$$
\boxed{
n=4^j+1,\qquad 81\mid j,\qquad
0<D=H-(n-2)<H/972,\qquad H=3^{h-1},
}
$$


the residual digit in the assignment vanishes:


$$
\boxed{\mathcal D_6=0.}
$$



Consequently,


$$
\boxed{
\operatorname{rank}_{\mathbb F_3}\mathcal D_6=0,\qquad
\operatorname{rad}\mathcal D_6=\mathbb F_3^\nu,\qquad
\operatorname{im}\mathcal D_6=\{0\},
}
$$


and the transported endpoint


$$
\overline e=\bigl((-1)^i\bigr)_{0\le i<\nu}
$$


is nonzero and is not in its image.

The proof does **not** evaluate only the fifth HIGH-return summand. It proves a finite-band support statement for every required return word, including the LOW correction


$$
3X^TL^{-1}X.
$$


In fact, the support argument yields the stronger core-return congruence


$$
\boxed{
V\widehat E^{-1}V^T\equiv0\pmod{729}.
}
\tag{E1}
$$



Thus the first possible full residual digit, at depth $3^7$, has **no HIGH-return contribution**. It is


$$
\boxed{
\frac{\mathscr R_{\rm act}}{3^7}
\equiv
\mathcal C_7+\mathcal F_R
\pmod3,
}
\tag{E2}
$$


where the core part is the explicit Hankel matrix


$$
\boxed{
(\mathcal C_7)_{ij}
=[y^{\varrho-i-j}](y-1)^D,
\qquad
\varrho=\frac{H/729-1}{2},
}
\tag{E3}
$$


and the actual polynomial-force part is


$$
\boxed{
(\mathcal F_R)_{ij}
=[y^{r_1-i-j}]
\frac{R(y)(y-1)^{2D}-R(-1)(-2)^{2D}}{y+1}.
}
\tag{E4}
$$


Here, exactly as in the source,


$$
R=\frac{3P_n-Q_c}{729};
$$


it is the polynomial fixed by the original derangement orthogonality equations, not a freely chosen perturbation.

The immediate bottleneck has therefore moved:

> Determine the radical and endpoint coupling of the **actual sum**
> $\mathcal C_7+\mathcal F_R$, including its genuine $R$-strip.

No actual primitive-denominator depth or nonzero whole-error decay follows without that additional work. The irrationality of $e+\pi$ remains unresolved.

No tools or external endpoints were used.

---

## 1. Scope, normalization, and a useful extra divisibility

Retain


$$
A=n-2=H-D,\qquad
m=\frac{A+1}{2},\qquad k=m+1,
$$




$$
d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1,
$$


and


$$
r_1=\frac{H-1}{2},\qquad
r_*=\frac{3H-1}{2}.
$$



All matrix boundaries remain the original ones:

- LOW unit columns:
  

$$
U_a=(y-1)^a,\qquad 0\le a<D;
$$


- residual columns:
  

$$
z_i=y^i(y-1)^D,\qquad 0\le i<\nu;
$$


- HIGH columns:
  

$$
Y_b=y^b,\qquad d\le b\le m.
$$



The local polynomial and complete functional are


$$
Q_n^{\rm loc}=Q_c+3^6R,\qquad
Q_c=(y+1)(y-1)^A(\beta+3y),\qquad
\beta=-71-A,
$$


and


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+
3^h\sum_{\substack{v\ge0\\2v+1\le4n-3}}
\frac{[y^v](F-F(-1))/(y+1)}{2v+1}.
\tag{1.1}
$$


In particular, the factorial force, endpoint subtraction, and finite cutoff are retained.

As in the supplied actual-force reduction, this report works in the **full scaled-matrix normalization**, with the primitive unit $\lambda$ temporarily removed.

### 1.1 The grid used in the proof

Put


$$
\boxed{\omega=\frac H{243}=3^{h-6}.}
\tag{1.2}
$$



The strict real-window inequality gives $\omega>4D$. There is also an arithmetic margin which is important for the last return word.

By LTE,


$$
v_3(A)=v_3(4^j-1)=1+v_3(j)\ge5.
$$


The source already establishes $h\ge9$. Hence


$$
27\mid \omega,\qquad 27\mid D.
$$


Therefore


$$
\boxed{\omega-4D\ge27.}
\tag{1.3}
$$



This small extra margin is obtained from the original index condition. It is not an additional real-window restriction.

Also,


$$
\boxed{\beta\equiv-71\pmod{243}.}
\tag{1.4}
$$



---

## 2. Complete support and bounded phase constants for $V$

The beta moments are


$$
B_p(s)=
\frac{(-1)^p2^pp!}
{\prod_{a=0}^{p}(2s+2a+1)}.
\tag{2.1}
$$


At the needed precision,


$$
V_{ib}\equiv
H\bigl[\beta B_H(i+b)+3B_H(i+b+1)\bigr]\pmod{243}.
\tag{2.2}
$$


The factorial term after division by $3$ is divisible by $H$, hence is zero at this precision.

For the original ranges,


$$
d\le i+b\le r_1-1.
$$



### 2.1 A phase-reduction identity

It is convenient to write


$$
\mathcal B_M(x)=
\frac{(-1)^M2^MM!}{\prod_{a=0}^{M}(x+2a)}
=B_M\!\left(\frac{x-1}{2}\right)
$$


for odd $x$.

When $3\mid x$ and $M$ is odd,


$$
\mathcal B_{3M}(x)
=\frac13\mathcal B_M(x/3)\,\Theta_M(x),
\tag{2.3}
$$


where


$$
\Theta_M(x)=
\frac{
2^{2M}\displaystyle\prod_{\substack{1\le a\le3M\\3\nmid a}}a
}{
\displaystyle\prod_{\substack{0\le a\le3M\\3\nmid a}}(x+2a)
}.
\tag{2.4}
$$


This is a $3$-adic unit. If $3^u\mid x$, then


$$
\boxed{\Theta_M(x)\equiv1\pmod{3^u}.}
\tag{2.5}
$$



Indeed, the factors excluded from the denominator are precisely those with $3\mid a$; on all remaining factors, $x+2a\equiv2a\pmod{3^u}$.

This identity reduces all surviving $V$-phases to beta products of lengths at most $82$.

### 2.2 Exact beta bands modulo $243$

For $s\le r_1-1$,


$$
v_3(B_H(s))=-v_3(2s+1).
$$


Thus the beta summand can survive modulo $243$ only if


$$
2s+1=cH/81
$$


with $c$ odd and $1\le c\le79$.

Repeated use of (2.3)–(2.5) gives


$$
\boxed{
H B_H\!\left(\frac{cH/81-1}{2}\right)
\equiv
81B_{81}\!\left(\frac{c-1}{2}\right)
\pmod{243}.
}
\tag{2.6}
$$



For clarity about precision, write $v=v_3(c)$. The displayed scaled quantity has valuation $4-v$. At each reduction step, the unit factor is $1$ modulo at least $3^{1+v}$, exactly enough to preserve the residue modulo $3^5$.

Define


$$
a_c=-71\cdot81B_{81}\!\left(\frac{c-1}{2}\right)
\pmod{243},
\qquad c=1,3,\ldots,79.
\tag{2.7}
$$


Then


$$
\boxed{v_3(a_c)=4-v_3(c).}
\tag{2.8}
$$


Its exact normalized phase is the bounded rational unit


$$
\boxed{
\frac{a_c}{3^{4-v_3(c)}}
=
-71\cdot3^{v_3(c)}
B_{81}\!\left(\frac{c-1}{2}\right)
\pmod{3^{1+v_3(c)}}.
}
\tag{2.9}
$$



Thus these are forty explicitly specified, nonzero bands, not merely possible support locations.

### 2.3 Exact extra-$3$ bands and the top endpoint

Away from $s=r_1-1$, the second summand survives only if


$$
2s+3=cH/27,\qquad c=1,3,\ldots,25.
$$


Similarly,


$$
\boxed{
3H B_H\!\left(\frac{cH/27-1}{2}\right)
\equiv
81B_{27}\!\left(\frac{c-1}{2}\right)
\pmod{243}.
}
\tag{2.10}
$$



Define


$$
b_c=81B_{27}\!\left(\frac{c-1}{2}\right)\pmod{243}.
\tag{2.11}
$$


Then


$$
\boxed{
v_3(b_c)=4-v_3(c),\qquad
\frac{b_c}{3^{4-v_3(c)}}
=
3^{v_3(c)}B_{27}\!\left(\frac{c-1}{2}\right)
\pmod{3^{1+v_3(c)}}.
}
\tag{2.12}
$$



At the exceptional endpoint $s=r_1-1$, the shifted beta argument is $r_1$. Here


$$
v_3(B_H(r_1))=-h,
$$


so its extra-$3$ contribution is a unit. Its exact phase is


$$
\boxed{
\tau
=
243B_{81}(40)\pmod{243},
\qquad
\tau\equiv-2\pmod3.
}
\tag{2.13}
$$


This follows by reducing $H$ to $81$ in (2.3); every removed unit factor is $1$ modulo $243$.

### 2.4 The complete $V$-formula

Combining the preceding facts,


$$
\boxed{
\begin{aligned}
V_{ib}\equiv{}&
\sum_{\substack{1\le c\le79\\c\ {\rm odd}}}
a_c\,
\mathbf1_{\displaystyle b=(cH/81-1)/2-i}\\
&+
\sum_{\substack{1\le c\le25\\c\ {\rm odd}}}
b_c\,
\mathbf1_{\displaystyle b=(cH/27-3)/2-i}\\
&+\tau\,\mathbf1_{i=\nu-1,\ b=m}
\pmod{243}.
\end{aligned}
}
\tag{2.14}
$$



All fifty-three nonendpoint bands lie inside the original HIGH interval. For example, at the lower end of the first beta band,


$$
\frac{H/81-1}{2}-(\nu-1)>d
$$


follows already from $H>324D$; the present domain is stronger. The upper endpoints are similarly strictly below $m$.

The beta and extra-$3$ bands cannot collide: such a collision would equate two multiples of $H/81$ whose difference is $2$, impossible since $3\mid H/81$.

Therefore (2.14) is the **complete support with its actual phases**, including the exact top endpoint. In particular,


$$
V\equiv-2e_{\nu-1}e_m^T\pmod3.
\tag{2.15}
$$



---

## 3. Two support classes

For $W\ge0$, define subsets of the integer degree line


$$
I(W)=\{t\omega+u:t\in\mathbb Z,\ |u|\le W\},
$$




$$
J(W)=
\left\{\frac{(2t+1)\omega-1}{2}+u:
t\in\mathbb Z,\ |u|\le W\right\}.
\tag{3.1}
$$



They are, respectively, integer-grid and half-grid bands.

The distance between their unthickened grids is


$$
\frac{\omega-1}{2}.
$$


Consequently,


$$
\boxed{
I(W_1)\cap J(W_2)=\varnothing
\quad\text{if}\quad
W_1+W_2<\frac{\omega-1}{2}.
}
\tag{3.2}
$$



Formula (2.14) implies, row by row,


$$
\boxed{\operatorname{supp}(V_{i,\bullet}\bmod243)\subseteq J(\nu).}
\tag{3.3}
$$



The beta valuation gives the slightly stronger fact needed later:


$$
\boxed{\operatorname{supp}(V_{i,\bullet}\bmod729)\subseteq J(\nu).}
\tag{3.4}
$$


At modulus $729$, the beta grid is $H/243=\omega$, the extra-$3$ grid is $H/81=3\omega$, and the same top endpoint remains exceptional.

### 3.1 The divisible lift of a HIGH vector

For a HIGH polynomial


$$
p(y)=\sum_{b=d}^{m}p_by^b,
$$


let


$$
\pi(p)=p-\operatorname{rem}_{(y-1)^D}p.
\tag{3.5}
$$


Thus


$$
\pi(p)=(y-1)^Dq(y),\qquad \deg q\le m-D.
$$



Say that $p$ belongs to $\mathcal C(W)$, modulo the stated modulus, if it has a representative for which


$$
\operatorname{supp}q\subseteq I(W).
\tag{3.6}
$$


In particular,


$$
\boxed{
p\in\mathcal C(W)\Longrightarrow
\operatorname{supp}p\subseteq I(W+D).
}
\tag{3.7}
$$



This lift is only an analysis device. It does not enlarge HIGH or alter its finite boundaries.

---

## 4. The inverse $R_H$ propagates half-grid bands to divisible integer-grid bands

The exact inverse orientation remains


$$
(R_H)_{ab}
=[z^{d+m-a-b}](1-z)^{-A},
\qquad d\le a,b\le m,
\tag{4.1}
$$


and


$$
d+m=r_1+D.
$$



The elementary prime-power congruences needed here are


$$
(1-z)^H\equiv(1-z^{3\omega})^{81}\pmod{243},
\tag{4.2}
$$




$$
(1-z)^H\equiv(1-z^\omega)^{243}\pmod{729}.
\tag{4.3}
$$


They follow from the freshman’s-dream congruence modulo $3$, followed by repeated cubing; each cubing gains one power of $3$.

Since these series have constant term $1$, inversion preserves the congruences. Hence, at either modulus,


$$
\boxed{
(1-z)^{-A}
=(1-z)^D(1-z)^{-H}
\equiv(1-z)^D S(z^\omega),
}
\tag{4.4}
$$


for an explicitly specified scalar series $S$. At modulus $243$, it can be taken to be


$$
S(z^\omega)=(1-z^{3\omega})^{-81}.
$$



### Lemma 4.1 — finite-boundary inverse propagation

If a HIGH vector $w$ is supported in $J(W)$, with $W\ge\nu$, then


$$
\boxed{R_Hw\in\mathcal C(W)}
\tag{4.5}
$$


modulo $243$, and also modulo $729$ when the input support is known at that precision.

#### Proof

Using (4.4), the HIGH coefficients of $R_Hw$ are those of


$$
(y-1)^D
\sum_b w_b\sum_{u\ge0}s_u
y^{r_1-b-u\omega}.
\tag{4.6}
$$


If $b\in J(W)$, then


$$
r_1-b-u\omega\in I(W).
$$



Only finitely many terms can reach degrees $d,\ldots,m$. Terms of negative exponent may be discarded: after multiplication by $(y-1)^D$, they cannot reach degree $d>D$. At the upper boundary,


$$
r_1-b\le r_1-d=m-D,
$$


so no polynomial degree beyond $m$ is introduced.

Let the resulting full polynomial be $P=(y-1)^DQ$, and let $p=P_{\ge d}$. Then


$$
\pi(p)
=
P-\left(P_{<d}-\operatorname{rem}_{(y-1)^D}P_{<d}\right).
$$


The quotient in the second term has degree at most


$$
d-1-D=\nu-1.
$$


Those degrees lie in $I(W)$ because $W\ge\nu$. This proves (4.5), including the finite lower boundary. ∎

The lower-boundary correction is essential. Simply treating $R_H$ as an infinite convolution would not prove this lemma.

---

## 5. Propagation through the complete $F$, including the LOW correction

Use the exact core blocks


$$
\widehat E=E-3X^TL^{-1}X,\qquad
F=\frac{\widehat E-E_0}{3}.
\tag{5.1}
$$


The source establishes that $F$ is integral. Its reduction modulo $81$ is the $F_*$ used in the five-term formula.

### Lemma 5.1 — complete $F$-propagation

Suppose $p\in\mathcal C(W)$ and


$$
W+D<\frac{\omega-1}{2}.
\tag{5.2}
$$


Then


$$
\boxed{
\operatorname{supp}(Fp\bmod243)\subseteq J(W+1).
}
\tag{5.3}
$$



#### Proof

Choose a representative with


$$
\pi(p)=(y-1)^DQ,\qquad \operatorname{supp}Q\subseteq I(W).
$$



First consider the LOW pairing


$$
\frac{G_c(U_a,\pi(p))}{3}.
$$


Its arctangent polynomial is


$$
(y-1)^H(y-1)^a(\beta+3y)Q.
\tag{5.4}
$$


Modulo $729$,


$$
(y-1)^H\equiv(y^\omega-1)^{243}.
\tag{5.5}
$$


Thus (5.4) is supported in $I(W+D)$.

After the division by $3$, a pole layer of valuation $r$ has weight $3^{h-1-r}$. Every layer that can contribute modulo $243$ has


$$
r\ge h-5.
$$


Each of its pole indices lies on the half-grid $J(0)$. The possible top weight $1/3$ is why (5.5) was used modulo $729$, rather than merely modulo $243$.

By (5.2), no such coefficient is present. All lower layers vanish at the stated precision, and the factorial part is also zero after division by $3$. Therefore


$$
\boxed{
G_c(U,\pi(p))/3\equiv0\pmod{243}.
}
\tag{5.6}
$$



Write the remainder of $p$ in the $U$-basis as $Ur$. Equation (5.6) gives


$$
Xp\equiv Lr\pmod{243}.
$$


Consequently,


$$
\boxed{
\widehat Ep
\equiv G_c(Y,\pi(p))\pmod{729}.
}
\tag{5.7}
$$



This is precisely where the LOW correction is retained. It is not assumed to vanish; it subtracts the actual remainder to the required precision.

Now divide (5.7) by $3$. The same pole-support argument, with the polynomial


$$
(y-1)^H(\beta+3y)Qy^b,
$$


shows that


$$
G_c(Y_b,\pi(p))/3
$$


is zero modulo $243$ outside $J(W+1)$.

It remains to treat $E_0p/3$. The remainder of $p$ has degree below $D$, and


$$
A+(D-1)+m=H-1+m<r_*.
$$


Hence the top-pole matrix kills that remainder exactly:


$$
E_0p=E_0\pi(p).
$$


The latter selects coefficients of


$$
(y-1)^HQy^b.
$$


By (5.5), after division by $3$ it is zero modulo $243$ outside $J(W)$.

Subtracting these two supported quantities proves (5.3). ∎

This proof uses every admissible pole at every relevant depth. It requires no pairing or cancellation of a selected subset of pole units.

---

## 6. Every required HIGH-return word vanishes

For a residual column label $j$, define


$$
p_{\ell,j}=(R_HF)^\ell R_HV_j^T.
\tag{6.1}
$$



By (3.3) and Lemma 4.1,


$$
p_{0,j}\in\mathcal C(\nu).
$$


Lemmas 4.1 and 5.1 then give inductively


$$
\boxed{
p_{\ell,j}\in\mathcal C(\nu+\ell)
\qquad(0\le\ell\le5)
\pmod{243}.
}
\tag{6.2}
$$



All intermediate width conditions hold. Indeed, for the largest needed value,


$$
\nu+5+D<\frac{\omega-1}{2}
$$


follows from $D\ge6$ and $\omega-4D\ge27$.

By (3.7),


$$
\operatorname{supp}p_{\ell,j}\subseteq I(\nu+\ell+D).
$$


The support of $V_i$ lies in $J(\nu)$. Their total thickening is


$$
\nu+(\nu+\ell+D)=2D-2+\ell.
$$


For $0\le\ell\le5$,


$$
2D-2+\ell\le2D+3<\frac{\omega-1}{2},
$$


again by (1.3).

Therefore


$$
\boxed{
V(R_HF)^\ell R_HV^T\equiv0\pmod{243},
\qquad 0\le\ell\le5.
}
\tag{6.3}
$$



In particular, **each of the five summands required for $\mathcal D_6$** vanishes at a precision sufficient to retain all its carries:


$$
\begin{aligned}
VR_HV^T&\equiv0,\\
VR_HFR_HV^T&\equiv0,\\
VR_HFR_HFR_HV^T&\equiv0,\\
VR_HFR_HFR_HFR_HV^T&\equiv0,\\
VR_HFR_HFR_HFR_HFR_HV^T&\equiv0
\end{aligned}
\qquad\pmod{243}.
\tag{6.4}
$$



This is stronger than extracting only their last base-$3$ digits. No carry from an earlier summand has been discarded.

### 6.1 A stronger return congruence

At modulus $729$, (3.4) and the modulus-$729$ version of Lemma 4.1 imply directly


$$
VR_HV^T\equiv0\pmod{729}.
\tag{6.5}
$$


For the remaining terms in the six-term inverse expansion,


$$
\widehat E^{-1}
\equiv
\sum_{\ell=0}^{5}(-3R_HF)^\ell R_H
\pmod{729},
\tag{6.6}
$$


equation (6.3) supplies a factor $243$, and the coefficient $3^\ell$ supplies at least one further factor $3$.

Hence


$$
\boxed{V\widehat E^{-1}V^T\equiv0\pmod{729}.}
\tag{6.7}
$$



### 6.2 Compression achieved

This is a bounded-band proof, not a size-$H$ matrix procedure.

The only grids involved at the decisive precision have spacing $\omega=H/243$. Within the original finite interval, their number of bands is bounded independently of $H,D,j$; a conservative bound of $245$ bands suffices. The return depth is at most five, and the widths increase by only one at each $F$-step.

More importantly, **no within-band coefficient propagation is needed to decide $\mathcal D_6$**: the integer-grid and half-grid bands remain disjoint.

The proof is explicit and does not invoke a generic finite-state theorem for a growing matrix.

---

## 7. Consequences for the actual sixth digit and its endpoint

The supplied actual-force Schur reduction gives


$$
\mathscr R_{\rm act}
\equiv-9V\widehat E^{-1}V^T\pmod{3^7}.
$$


Equation (6.7) therefore proves


$$
\boxed{\mathscr R_{\rm act}\in3^7M_\nu(\mathbb Z_3)}
\tag{7.1}
$$


and


$$
\boxed{\mathcal D_6=0.}
\tag{7.2}
$$



The exact corrected endpoint remains the one obtained by evaluating the full corrected columns. Its residue is


$$
\overline e=\bigl((-1)^i\bigr)_{i<\nu}.
$$


Since $\nu\ge2$, this is nonzero. Thus


$$
\boxed{
\operatorname{rad}\mathcal D_6=\mathbb F_3^\nu,\qquad
\overline e\notin\operatorname{im}\mathcal D_6.
}
\tag{7.3}
$$



There is no invertible or nonisotropic branch at depth $6$ on this domain.

### Infinite original-index scope

The domain is infinite by the retained irrational-rotation argument applied to $j=81t$. Equivalently, one takes a closed ratio interval strictly inside


$$
1<H/A<972/971.
$$


The present proof covers every original index in that domain. It introduces no restricted ternary-digit condition.

---

## 8. The depth-$7$ residual: an explicit core Hankel matrix plus the actual $R$-strip

The exact core Schur formula is


$$
\mathscr R_c
=
G_c(Z,Z)-3B^TL^{-1}B
-9\widetilde V\widehat E^{-1}\widetilde V^T,
$$


where


$$
B\in3^6M,\qquad
\widetilde V=V-B^TL^{-1}X.
$$


Thus


$$
3B^TL^{-1}B\in3^{13}M,
$$


and replacing $\widetilde V$ by $V$ changes the HIGH-return term only by $3^8M$.

Together with (6.7), this proves


$$
\boxed{
\mathscr R_c\equiv G_c(Z,Z)\pmod{3^8}.
}
\tag{8.1}
$$



### 8.1 Evaluation of the core direct digit

Expand the remaining factor $(y-1)^D$:


$$
\begin{aligned}
G_c(z_i,z_j)\equiv
3^h\sum_{t=0}^{D}
(-1)^{D-t}\binom Dt
\bigl[
\beta B_H(i+j+t)
+3B_H(i+j+t+1)
\bigr]
\pmod{3^8}.
\end{aligned}
\tag{8.2}
$$


The factorial part is zero at this precision since $h\ge9$.

All shifts satisfy


$$
2(i+j+t)+1\le4D-7<\omega,
$$


and the shifted extra-$3$ term satisfies the corresponding bound $4D-5<\omega$.

For the beta term to survive after division by $3^7$, one must have


$$
v_3(2(i+j+t)+1)=h-7.
$$


Below $\omega=3^{h-6}$, the only positive odd multiple of $3^{h-7}$ is $3^{h-7}$ itself. Thus the only surviving shift is


$$
i+j+t=\varrho,\qquad
\varrho=\frac{H/729-1}{2}.
\tag{8.3}
$$



Its normalized beta unit is $1$ modulo $3$. One way to verify this is to apply (2.3) down to $B_{729}(0)$; factorial-unit cancellation gives


$$
B_{3^a}(0)\equiv1\pmod3\qquad(a\ge1).
$$


Also $\beta\equiv1\pmod3$.

The extra-$3$ summand has valuation at least $8$ and does not contribute at this digit. Therefore


$$
\boxed{
\frac{G_c(z_i,z_j)}{3^7}
\equiv
(-1)^{D-\varrho+i+j}
\binom D{\varrho-i-j}
=
[y^{\varrho-i-j}](y-1)^D
\pmod3.
}
\tag{8.4}
$$


As usual, an out-of-range binomial coefficient is zero.

This proves (E3).

### 8.2 The actual polynomial correction

The degree-sensitive Schur perturbation argument in the supplied reduction is applicable here. Its ingredients are:

1. the eliminated inverse loses at most one power of $3$;
2. the linear perturbation is the complete functional applied to $R$ times the corrected residual columns;
3. the top pole is absent by the exact degree bound;
4. modulo $9$, the first corrected-column terms have degree at most $d$, so their top-pole cross terms also vanish.

Consequently,


$$
\frac{\mathscr R_{\rm act}-\mathscr R_c}{3^7}
\equiv\mathcal F_R\pmod3,
$$


with


$$
(\mathcal F_R)_{ij}
=
[y^{r_1}]
\frac{Rz_iz_j-R(-1)z_i(-1)z_j(-1)}{y+1}.
\tag{8.5}
$$



Writing


$$
W_R(y)=
\frac{R(y)(y-1)^{2D}-R(-1)(-2)^{2D}}{y+1},
$$


gives exactly


$$
\boxed{
(\mathcal F_R)_{ij}=[y^{r_1-i-j}]W_R(y).
}
\tag{8.6}
$$



Combining (8.1), (8.4), and (8.6),


$$
\boxed{
\mathscr R_{\rm act}=3^7\mathcal T_7,\qquad
\mathcal T_7\bmod3=\mathcal C_7+\mathcal F_R.
}
\tag{8.7}
$$



Only the actual strip


$$
r_1-(D-4),\ldots,r_1
$$


of $W_R$ is needed for this digit.

If $v_3(j)>4$, the supplied stronger polynomial congruence makes $R\equiv0\pmod3$, so $\mathcal F_R=0$. This is a valid simplification on that subfamily, but it does not evaluate the rank of $\mathcal C_7$.

### 8.3 Where the next HIGH return can first occur

Equation (6.7) places the first still-unevaluated pure $V$-return at


$$
\boxed{
-\frac{V\widehat E^{-1}V^T}{729}\pmod3,
}
\tag{8.8}
$$


which contributes to the full residual at depth $3^8$, not $3^7$.

It can be specified using the seven-term inverse expansion modulo $2187$. At that depth one must also restore the difference between $V$ and $\widetilde V$. If


$$
J=B/729,
$$


then the corresponding core HIGH-return digit includes


$$
-\frac{V\widehat E^{-1}V^T}{729}
+
J^TL^{-1}X\,\widehat E^{-1}V^T
+
V\widehat E^{-1}X^TL^{-1}J
\pmod3.
\tag{8.9}
$$


Thus even the next core-return calculation cannot discard the LOW–residual coupling.

Equation (8.9) identifies that next return obligation; it does not claim to evaluate the entire depth-$8$ actual residual.

---

## 9. Conditional denominator depth and comparison with the actual error

The depth-$6$ sufficient branch in the source is now empty on this domain. Its normalization was nevertheless correct.

At depth $7$, suppose one subsequently proves


$$
\det(\mathcal C_7+\mathcal F_R)\ne0
$$


and


$$
\overline e^{\,T}
(\mathcal C_7+\mathcal F_R)^{-1}
\overline e\ne0
\quad\text{in }\mathbb F_3.
\tag{9.1}
$$


Then


$$
v_3(\det G_{\rm act})=D+7\nu,
\qquad
v_3(v^TG_{\rm act}^{-1}v)=-7.
\tag{9.2}
$$



Using the exact normalization


$$
\frac{\beta_1}{\beta_0}
=
\frac{3^hQ_n^{\rm loc}(-1)}4
\,v^TG_{\rm act}^{-1}v
$$


and the retained actual endpoint law,


$$
v_3(Q_n^{\rm loc}(-1))=2v_3((n-1)!),
$$


one obtains the conditional exact primitive-denominator law


$$
\boxed{
v_3(q)=
\max\{0,\ h+2v_3((n-1)!)-7\}.
}
\tag{9.3}
$$



More generally, an invertible, nonisotropic residual branch first occurring at full depth $t$ gives the same formula with $7$ replaced by $t$.

These are sufficient-branch deductions, not presently established actual denominator values.

### 9.1 What this would require of the real error

For fixed $t$,


$$
h+2v_3((n-1)!)-t
=
h+n-1-s_3(n-1)-t
=
n+O(\log n).
\tag{9.4}
$$


Thus such a branch would already force a $3$-part of the denominator of exponential size.

Since


$$
\frac{\det H_{\rm complete}}{\beta_1}
=(e+\pi)+\frac{\beta_0}{\beta_1},
$$


a necessary consequence of whole primitive errors tending to zero would be


$$
\left|
\frac{\det H_{\rm complete}}{\beta_1}
\right|
=
o\!\left(
3^{-h-2v_3((n-1)!)+t}
\right).
\tag{9.5}
$$


This condition is not sufficient: the denominator can have substantial contributions at other primes.

No audited real estimate in the supplied A1 material establishes (9.5) for the actual complete determinant. A core-only positivity statement or an unreviewed saddle estimate cannot replace it.

### 9.2 Final gcd and whole evaluated error

Retain


$$
A_\ell=\ell^k\beta_0,\qquad
B_\ell=\ell^k\beta_1,\qquad
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell^k}{g_\ell}
\det H_{\rm complete}.
}
\tag{9.6}
$$



The primitive polynomial multiplier $\lambda$ must be restored in the actual matrices and coefficient pair. Its cancellation in the relative endpoint formula does not remove it from the global arithmetic.

The results above do not determine the final all-prime gcd, prove $B_\ell\ne0$ unconditionally, or establish nonvanishing and decay of (9.6).

---

## 10. Bounded exact arithmetic for inspection

The proof of $\mathcal D_6=0$ does not require a numerical rank calculation.

A useful bounded certificate would check only the new phase constants and sparse polynomial congruences.

### Inputs

1. Modulus $243$.
2. The beta products:
   

$$
B_{81}\!\left(\frac{c-1}{2}\right),
   \quad c=1,3,\ldots,79;
$$


   

$$
B_{27}\!\left(\frac{c-1}{2}\right),
   \quad c=1,3,\ldots,25;
$$


   

$$
B_{81}(40),\qquad B_{729}(0).
$$


3. Auxiliary collapse checks at
   

$$
H=243,\ 729,
$$


   with exactly the same finite sets of $c$'s.
4. The polynomial congruences at $H=729$:
   

$$
(1-z)^{729}\equiv(1-z^9)^{81}\pmod{243},
$$


   

$$
(1-z)^{729}\equiv(1-z^3)^{243}\pmod{729}.
$$



These are bounded auxiliary inputs, not original-index samples.

### Expected verifiable output

- The forty $a_c$'s and thirteen $b_c$'s are nonzero modulo $243$.
- Their valuations are exactly
  

$$
4-v_3(c).
$$


- Their normalized residues equal the rational-unit formulas (2.9) and (2.12).
- The top constant satisfies
  

$$
243B_{81}(40)\equiv-2\pmod3.
$$


- Every auxiliary collapse congruence (2.6), (2.10), and (2.13) holds.
- The two sparse polynomial congruences have zero coefficientwise differences at their stated moduli.
- Finally,
  

$$
B_{729}(0)\equiv1\pmod3.
$$



The largest beta product has $730$ denominator factors. No growing matrix, original-index scan, or finite inference about an infinite rank pattern is involved.

---

## 11. Closing ledger

### New results and proof status

Using the accepted block structure and actual-force congruence at their stated scope, the following are proved here:

1. **Complete $V$-support and phases:** fifty-three nonendpoint bands and one exact top corner, with all phases reduced to fixed beta products.
2. **Finite-boundary inverse propagation:** $R_H$ maps half-grid bands to divisible integer-grid bands without extending HIGH.
3. **Complete $F$-propagation:** the LOW correction $3X^TL^{-1}X$ restores the required divisible lift; it is retained, not discarded.
4. **All required return words vanish:** every summand contributing to $\mathcal D_6$, including its carries, is covered.
5. **The actual sixth digit is zero:**
   

$$
\mathcal D_6=0,
$$


   with full radical and nonzero endpoint outside its image.
6. **Stronger core-return depth:**
   

$$
V\widehat E^{-1}V^T\in729M_\nu(\mathbb Z_3).
$$


7. **The first remaining actual digit is explicit:**
   

$$
\mathcal T_7\bmod3=\mathcal C_7+\mathcal F_R,
$$


   with $\mathcal C_7$ given by (E3) and the actual correction strip by (E4).

These results hold on the entire stated original domain, hence on an infinite original family. No restricted-digit infinitude assertion is used.

### Exact remaining mathematical bottleneck

The immediate outstanding lemma is:

> **Actual depth-seven endpoint lemma.**  
> For
> 

$$
> R=(3P_n-Q_c)/729
>
$$


> fixed by the original derangement equations, evaluate the coefficient strip (E4), and determine the radical, endpoint image, and—on an invertible branch—the endpoint contraction of
> 

$$
> \mathcal C_7+\mathcal F_R.
>
$$



On its singular branches, further saturation must retain the next complete core return, the LOW–residual cross terms, higher actual force, and the transported endpoint.

### Overall research status

The actual-force residual analysis has advanced by one full digit and has identified the next actual force explicitly. It has not closed the denominator/error argument.

An irrationality proof still requires an infinite original-index sequence with the **final primitive pair** satisfying


$$
0<|q(e+\pi)-p|\longrightarrow0.
$$





$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


