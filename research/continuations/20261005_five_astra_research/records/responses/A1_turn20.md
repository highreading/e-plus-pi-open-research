> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Verdict

On the domain


$$
\boxed{n=4^j+1,\quad 81\mid j,\quad
0<D=H-(n-2)<H/972,}
$$


the proposed LOW-first contractions do vanish, using the original columns


$$
z_i=y^i(y-1)^D,\qquad 0\le i<\nu.
$$


In particular,


$$
\boxed{T_5=0.}
$$



One index bound in the proposal needs correction: to prove the entire first three-by-three HIGH corner by division, the extended quotient indices run through $\nu+2$. The largest shift including the core is then $2D+3$, not $2D+1$. The smaller domain supplies the stronger required inequality


$$
4D+7<H/81.
$$


Thus this correction does not obstruct the conclusion.

The result concerns the actual weighted rational form. It does not use a positive replacement metric or geometric replacement columns. It does not decide irrationality of $e+\pi$.

## 1. Domain and precision

Retain


$$
A=H-D,\quad d=\frac{3D}{2}-1,\quad
\nu=\frac D2-1,\quad m=\frac{A+1}{2},
$$


and


$$
r_1=\frac{H-1}{2},\quad r_2=\frac{H/3-1}{2},\quad
r_*=\frac{3H-1}{2}.
$$


Here $D$ is a positive multiple of $6$: both $H$ and $A=4^j-1$ are divisible by $3$, and both are odd. Thus


$$
D\ge6,\qquad \nu\ge2.
$$


In particular, the radical endpoint vector below is nonempty.

Since $H>972D$,


$$
H/81>12D>4D+7.
\tag{1}
$$


All the extended indices $d,d+1,d+2$ belong to HIGH; indeed $m-d=(H-4D+3)/2$ is much larger than $3$.

Strip only


$$
\lambda=L_n/3\in\mathbb Z_3^\times.
$$


Use the complete functional $\mathcal M$ in the supplied source, including its factorial contribution, endpoint subtraction, and every pole satisfying $c3^r\le4n-3$. Write


$$
Q_n^{\rm loc}=(y+1)(y-1)^A(\beta+3y)+3^tR_0,
\qquad
\beta=-71-3M_0,\quad t=v_3(j)+2\ge6.
\tag{2}
$$


The full-matrix error from the last term is in $3^6\mathbb Z_3$; after one division by $3$, it is in $243\mathbb Z_3$. Consequently it cannot affect any calculation below. Endpoint subtraction is included in this statement, because monic division by $y+1$ preserves coefficient divisibility after subtracting the exact remainder.

For the lower-support calculations we may therefore use


$$
\beta\equiv1\pmod9,\qquad \beta\equiv10\pmod{27}.
\tag{3}
$$



### Extended direct annihilation

For


$$
0\le i\le\nu+2,\qquad 0\le a\le d+2,
$$


the product with the core has shifts at most $2D+3$. Equation (1), together with the supplied direct-beta valuation, gives


$$
L_{\rm ext}\bigl(y^i(y-1)^D,y^a\bigr)=0\pmod{243}.
\tag{4}
$$


The factorial and actual-polynomial errors remain beyond this precision.

The top pole is absent in these pairs: their largest endpoint-divided degree is bounded by


$$
A+1+2(d+2)=H+2D+3<r_*.
$$


Monic division by $(y-1)^D$ now proves that the lower Schur pairings among $d,d+1,d+2$ vanish modulo $243$. In particular,


$$
F_{dd}\in243\mathbb Z_3,\qquad
F_{\{d,d+1\},\{d,d+1\}}=0\pmod3,
\tag{5}
$$


and


$$
V_{d+s}=0\pmod{243}\quad(0\le s\le2).
$$


Since the $e_m$ and $K$ contributions vanish in these columns,


$$
\boxed{Je_{d+s}\in27\mathbb Z_3^\nu\quad(0\le s\le2).}
\tag{6}
$$



## 2. LOW-first correction and inverse expansion

Put


$$
B=U^TLZ,\qquad C=L_U^{-1}B,\qquad
\widetilde V=V-C^TX_U.
$$


Equation (4) gives $B,C\in243\mathbb Z_3$. The exact radical block after LOW-first elimination, in the first-LOW normalization, is


$$
\mathcal R
=Z^TLZ-B^TL_U^{-1}B
-3\widetilde V\widehat E^{-1}\widetilde V^T,
\qquad
\widehat E=E-3X_U^TL_U^{-1}X_U.
\tag{7}
$$


Thus modulo $243$,


$$
\mathcal R\equiv-3V\widehat E^{-1}V^T.
\tag{8}
$$


This proves the required negligibility of the $Z^TLU$ corrections before dropping them.

With $R=E_0^{-1}$ and $\widehat E=E_0+3F$,


$$
\widehat E^{-1}
\equiv R-3RFR+9RFRFR-27RFRFRFR\pmod{81}.
$$


Multiplication by the **exact**


$$
V=-2ee_m^T+3K+9J
$$


gives the proposed $9A_9+27A_{27}$ expansion. Before using (5), there is also the term


$$
-12F_{dd}ee^T,
$$


which vanishes modulo $81$. The signs and coefficients in both displayed $A_9,A_{27}$ are correct. No additional coupling array is needed.

It remains to evaluate $A_9$ modulo $9$ and $A_{27}$ modulo $3$.

## 3. The inverse coefficient gaps

The exact orientation is


$$
R_{ab}=[z^{d+m-a-b}](1-z)^{-A}.
\tag{9}
$$


For degrees below $H$,


$$
(1-z)^{-A}
\equiv(1-z)^D
\left(1+3z^{H/3}-3z^{2H/3}\right)\pmod9.
\tag{10}
$$


Indeed $(1-z)^H\equiv1-z^H-3z^{H/3}+3z^{2H/3}\pmod9$, and inversion below degree $H$ gives (10).

The degrees selected by $KRK^T$ are


$$
D+\frac{H+3}{6}+i+j,\qquad 0\le i,j<\nu.
$$


They lie strictly between $D$ and $H/3$. Therefore


$$
\boxed{KRK^T=0\pmod9.}
\tag{11}
$$



Modulo $3$, (9) has no nonzero coefficient degrees strictly between $D$ and $H$. This gap will also dispose of the nonedge bands below.

## 4. Actual support of $Fe_d$ modulo $9$

Here is the required lower-functional support calculation, rather than an assumption about the next digit.

For a product $y^i(y-1)^D y^b$, put $s=i+b$. In the range


$$
0\le i\le\nu,\qquad d\le b\le m,
$$


we have $s\le r_1$. Modulo $9$:

* The first lower pole uses
  

$$
(y-1)^H\equiv y^H-1+3y^{H/3}-3y^{2H/3}.
$$


  Including $\beta+3y$, its only possible shifts in this range are
  

$$
s=r_1,\quad r_1-1,\quad r_2.
$$


* The next lower layer has weight $3$, so uses $y^H-1$ modulo $3$. The only possible shift is $r_2$. The two contributions with units $1,7$ have opposite polynomial signs and equal inverse units modulo $3$, and cancel at their required precision.
* Every deeper layer is zero modulo $9$.

Both members of the unit pair are within the original cutoff, since $7H/3<4n-3$ on this domain. Thus no cutoff term has been silently discarded.

Divide $y^d$ by $(y-1)^D$. By (4), its remainder of degree below $D$ agrees modulo $243$ with the actual $L_U$-projection. Hence its lower Schur column modulo $9$ is an integral combination of the pairings just listed, for $0\le i\le\nu$.

The bands $b=r_1-i$ and $b=r_1-i-1$, when intersected with HIGH, lie in $\{m-1,m\}$. The remaining band is $b=r_2-i$.

The top perturbation at column $d$ is supported in $\{m-1,m\}$ by degree. Consequently


$$
\boxed{
\operatorname{supp}(Fe_d\bmod9)
\subseteq
\{m-1,m\}\cup\{r_2-i:0\le i\le\nu\}.
}
\tag{12}
$$


The nonedge band is divisible by $3$, consistently with the established two-edge residue.

Choose $u$ supported on $m-1,m$ with $Fe_d=u+3v$. Then (12) gives the asserted support of $v\bmod3$. Exactly,


$$
KRu=0,
$$


since $Re_m=e_d$, $Re_{m-1}=e_{d+1}+Ae_d$, and $K$ kills $d,d+1$.

For $b=r_2-l$, $0\le l\le\nu$, the coefficient degree selected by $KR e_b$ is


$$
D+\frac{H+3}{6}+i+l,
$$


strictly between $D$ and $H$. Therefore


$$
\boxed{KRFe_d=0\pmod9.}
\tag{13}
$$



Also $v_d=v_{d+1}=0\pmod3$. Since $Ru$ is supported at $d,d+1$ and the last two-by-two corner of $R$ is exactly zero,


$$
(Fe_d)^TR(Fe_d)
=u^TRu+6u^TRv+9v^TRv=0\pmod9.
$$


Thus


$$
\boxed{(FRF)_{dd}=0\pmod9.}
\tag{14}
$$



Equations (6), (11), (13), and (14) evaluate every term of $A_9$:


$$
\boxed{A_9=0\pmod9.}
\tag{15}
$$



## 5. Actual support of $J\bmod3$

Modulo $27$, the first lower layer has the full $H/9$ grid, the next layer has the $H/3$ grid, and the third has only $y^H-1$. The core has degree one.

For $0\le i<\nu$, $b\le m$, one has $i+b\le r_1-1$. Listing the possible selected shifts gives:

* First lower layer:
  

$$
b=r_1-kH/9-i-a,\quad 0\le k\le4,\quad a=0,1.
$$


* Second lower layer: its half-grid shifts in this range correspond to $k=0,3$ in the same list.
* Third lower layer: the admissible unit residues give $k=1,2,4$. Including these bands is sufficient whether or not their paired coefficients cancel.

The $k=0$ bands meet HIGH only at an edge. The top pole in $V$ itself is supported only at its last corner. Subtracting $-2ee_m^T+3K$ does not create any new support, and the actual-polynomial error is zero modulo $27$ after the LOW division. Hence


$$
\boxed{
\operatorname{supp}(J\bmod3)
\subseteq
\{m-1,m\}\cup
\{r_1-kH/9-i-a:
1\le k\le4,\ a=0,1,\ 0\le i<\nu\}.
}
\tag{16}
$$



For a nonedge band, $KRJ^T$ selects degrees


$$
D-r_2+kH/9+i+l+a.
$$


For $k=1$ they are negative. For $k=2,3,4$ they lie strictly between $D$ and $H$. These assertions follow directly from $D<H/972$ and $i+l\le D-4$. The edge bands are killed exactly by $KR$. Therefore


$$
\boxed{KRJ^T=JRK^T=0\pmod3.}
\tag{17}
$$



## 6. The remaining $F$-contractions

Modulo $3$, the $i$-th column of $RK^T$ is precisely the coefficient vector of


$$
p_i(y)=y^{H/3+i}(y-1)^D.
\tag{18}
$$


This follows from (9), $d+m-D=r_1$, and the inverse gap; the whole polynomial in (18) lies within HIGH.

For the top contribution to $p_i^TFp_j$, the selected polynomial modulo $3$ is


$$
y^{2H/3+i+j+1}(y^H-1)(y-1)^D.
$$


At degree $r_*$, neither the unshifted nor the $H$-shifted degree-$D$ band reaches the coefficient. The lower first pole is below the minimum shift $2H/3+i+j$.

Finally the $X_U$-coupling of $p_i$ modulo $3$ selects a coefficient of


$$
y^{H/3+i+a}(y^H-1),\qquad 0\le a<D,
$$


at $r_1$, which is zero. Thus the LOW unit correction inside $F$ also vanishes, proving


$$
\boxed{KRFRK^T=0\pmod3.}
\tag{19}
$$



The same division argument as in Section 4, now modulo $3$ for $y^{d+1}$, gives


$$
\operatorname{supp}(Fe_{d+1}\bmod3)
\subseteq\{m-2,m-1,m\}.
\tag{20}
$$


Indeed the lower first-pole condition is $i+b=r_1$ with $i\le\nu+1$; the top perturbation supplies at most one further edge. The matrix $KR$ kills all three edges exactly.

Using the two-edge support of $Fe_d\bmod3$, (6), (20), and (5), respectively, yields


$$
\boxed{
JRFe_d=0,\qquad
KRFRFe_d=0,\qquad
(FRFRF)_{dd}=0
\pmod3.
}
\tag{21}
$$


For the last identity, write it as


$$
(RFe_d)^TF(RFe_d);
$$


the vector is supported at $d,d+1$, where the relevant corner of $F$ is zero.

Equations (17), (19), and (21) evaluate every term of $A_{27}$:


$$
\boxed{A_{27}=0\pmod3.}
$$


Together with (15),


$$
\boxed{T_5=-(A_9/3+A_{27})=0.}
$$



## 7. Transported endpoint and arithmetic scope

The exact LOW-first corrected columns are


$$
\widehat Z
=Z-UC-
\bigl(Y-UL_U^{-1}X_U\bigr)\widehat E^{-1}(3\widetilde V^T).
\tag{22}
$$


Their endpoint is obtained by evaluating this entire expression at $-1$, not by deleting its correction terms. Since $C\in243\mathbb Z_3$ and the HIGH correction is divisible by $3$,


$$
\widehat Z(-1)\equiv
\bigl((-1)^i(-2)^D\bigr)_{i<\nu}
=\bigl((-1)^i\bigr)_{i<\nu}\pmod3.
$$


This is nonzero, and therefore


$$
\boxed{\overline e_{\rm rad}\notin\operatorname{im}T_5.}
$$



Restoring $\lambda$ multiplies the residual form by that actual primitive unit. The Smith consequences are


$$
v_3(\det S)\ge5\nu,\qquad
v_3(\operatorname{adj}(S)_{ab})\ge5(\nu-1).
$$


Under the supplied complete-pair normalization identity,


$$
\boxed{v_3(g)\ge d+5\nu=4D-6.}
$$


These remain lower bounds, not exact denominator valuations.

Retain the final pair


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|),\quad
q=\frac{|B_{\rm det}|}{g},\quad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g.
$$


Where $B_{\rm det}\ne0$, the whole real error is exactly


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_{\rm det})\ell^k}{g}
\det H_{\rm complete},
\qquad k=(n+1)/2.
}
$$


The multiplier is the full clearer divided by the **final gcd**. Polynomial endpoint nonvanishing does not by itself prove complete-response or whole-error nonvanishing.

The domain is infinite by irrational rotation on $81\mid j$, taking a closed ratio interval strictly inside $1<H/A<972/971$.

The separate critical-three-quarters saddle proposal is not used here. Its sharp moment and actual derivative estimates, and consequently its proposed critical-scale relative law, remain unaudited in this response.

## Closing ledger

1. **New result and proof status.** Proved: every proposed fifth contraction vanishes at its required precision for the actual $Z$ columns on $81\mid j,\ 0<D<H/972$. Thus $T_5=0$, with nonzero transported endpoint residue outside its image. The extended-test shift bound needed a harmless strengthening. The final-gcd bound improves to $4D-6$ under the supplied normalization identity.

2. **Exact remaining bottleneck.** Fifth rank zero requires a further saturation; it does not determine the relative transported-cofactor depth or the actual reduced denominator. An irrationality argument still requires same-index control of the final denominator and nonzero **whole primitive errors tending to zero**. No proof or disproof of irrationality of $e+\pi$ follows.

3. **Computation request.** None. The fifth-contraction evaluation uses uniform coefficient support and exact Schur identities, not finite rank evidence.
