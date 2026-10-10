> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A1 — evaluation of the two remaining lower sixth contributions

On the **same** domain


$$
j>0,\qquad243\mid j,\qquad n=4^j+1,\qquad
H=3^{h-1},\qquad A=n-2=H-D,\qquad0<D<H/8748,
$$


I obtain


$$
\boxed{A_9\equiv0\pmod{27},\qquad A_{27}\equiv0\pmod9.}
$$


Thus the two contributions assigned to A1 satisfy


$$
\boxed{A_9/9=0,\qquad A_{27}/3=0\pmod3.}
$$



The calculations below use the newly supplied **actual block definitions**, including their LOW-unit correction. They do not replace the weighted form by a positive metric or replace its columns by geometric columns.

The conclusion about the entire sixth form remains conditional on A4’s separate certification of $A_{81}$. No primitive-denominator or irrationality conclusion follows merely from these zero contractions.

## 1. Normalization and division audit

Retain


$$
d=\frac{3D}{2}-1,\qquad \nu=\frac D2-1,\qquad
m=\frac{A+1}{2},\qquad
r_1=\frac{H-1}{2},\qquad r_2=\frac{H/3-1}{2}.
$$


HIGH is exactly $d\le a\le m$, and the radical columns are


$$
z_i=y^i(y-1)^D,\qquad0\le i<\nu.
$$


Throughout, supports are intersected with this finite HIGH interval.

Write $B_A=(y-1)^A$, $B_H=(y-1)^H$, and


$$
P=B_A(\beta+3y),\qquad \beta=-71-A,\qquad
c_0=\frac{\beta-1}{3}.
$$


Only the actual primitive unit $\lambda=L_n/3$ is stripped.

The supplied definitions give the block matrix


$$
G=
\begin{pmatrix}
3L&3X\\
3X^T&E
\end{pmatrix}.
$$


Eliminating the unit LOW block $3L_U$ therefore changes the HIGH block to


$$
E-3X_U^TL_U^{-1}X_U=E_0+3F.
$$


Thus the factor in


$$
F=(E-E_0)/3-X_U^TL_U^{-1}X_U
$$


is correct: there is no missing or extra factor $3$.

Likewise the radical–HIGH block before LOW correction is $3Z^TX=3V$. After the first LOW normalization its HIGH Schur contribution is consequently


$$
-3V(E_0+3F)^{-1}V^T,
$$


as in the established sixth-carry identity.

For $u<D$, $a\le m$, the top core coefficient vanishes, since


$$
A+1+u+a\le A+D+m=H+m<r_*.
$$


This verifies the top-pole exclusion used in the formulas for $X_U$ and $L_U$.

The original factorial contribution remains divisible by $3^h$ in $G$, and the depth-seven polynomial error, including its endpoint-subtracted quotient, remains divisible by $3^7$. After the single division by $3$, these are beyond all precisions used below. This is the reason they may be omitted in the displayed congruences—not a change to the complete functional.

In particular, the supplied formulas for $F\bmod27$ and $V\bmod81$ have the correct scalar normalization.

## 2. Precision-weighted support covers from every admissible pole

The following support argument does not cancel pole partners. It keeps every admissible odd unit $c$, with its actual inverse and original cutoff.

For $q=2,3,4$,


$$
B_H\pmod{3^q}
$$


is supported on multiples of $H/3^{q-1}$. At lower depth $t<q$, the factor $3^t$ means that only $B_H\bmod3^{q-t}$ is needed.

Consider a selected coefficient with an additional shift $l+\epsilon$, where $\epsilon\in\{0,1\}$ is supplied by the linear core. Its possible HIGH position is


$$
a=\frac{cH/3^t-1}{2}
-k\frac{H}{3^{q-t-1}}-l-\epsilon.
\tag{1}
$$


Measured in units $H/(2\cdot3^{q-1})$, the coefficient of $H$ here is


$$
c3^{q-1-t}-2k3^t,
$$


which is odd. Hence all surviving bands lie on an **odd half-grid**.

This applies term by term, including boundary poles. A cutoff may remove bands but cannot introduce a band outside this cover.

All separation estimates below have margin at least $H/54-O(D)$. The stipulated inequality $H>8748D$ is much stronger than required.

### 2.1 The actual $Fe_d$ formula

Put $w=Fe_d$. Monic division gives


$$
y^d=r_d+B_Dq_d,\qquad
q_d=\sum_{s=0}^{\nu}\binom{D+s-1}{s}y^{\nu-s}.
$$


The established extended annihilation identifies the actual LOW projection with $r_d$ modulo $729$. Thus the supplied formula indeed gives


$$
w=(c_0-A)e_m+e_{m-1}
+\left(
\sum_{t=0}^2 3^t
 B_t\!\left(B_H(\beta+3y)q_dy^a\right)
\right)_{a\in{\rm HIGH}}
\pmod{27}.
\tag{2}
$$


The two explicit top entries follow from


$$
E_0e_d=e_m,\qquad
\bigl([y^{r_*}]yB_Ay^{a+d}\bigr)_a=e_{m-1}-Ae_m.
$$



Applying (1) with $q=3$, $0\le l\le\nu$, proves


$$
\operatorname{supp}(w\bmod27)
\subseteq\{m-1,m\}\cup\mathcal W,
\tag{3}
$$


where


$$
\mathcal W=
\left\{
\frac{bH/9-1}{2}-l-\epsilon:
b\in\{1,3,5,7\},\
0\le l\le\nu,\ \epsilon\in\{0,1\}
\right\}.
\tag{4}
$$


The $b=9$ bands meet HIGH only at the two separated edge positions.

At the lower precision, applying the same argument with $q=2$ gives


$$
w=u+3v\pmod9,
\tag{5}
$$


where $u$ is supported on $m-1,m$, and $v\bmod3$ may be chosen supported on


$$
\left\{r_2-l-\epsilon:0\le l\le\nu,\ \epsilon\in\{0,1\}\right\}.
\tag{6}
$$


Allowing $\epsilon=1$ is harmless; it avoids relying on any unnecessary coefficient cancellation.

### 2.2 The actual $J\bmod9$ bands

The audited formula is


$$
V_{ia}=(ee_m^T)_{ia}
+\sum_{t=0}^3 3^t
 B_t\!\left(B_H(\beta+3y)y^{i+a}\right)
\pmod{81}.
\tag{7}
$$


Here $e$ is the last standard radical vector, not the transported endpoint.

Apply (1) with $q=4$. Subtracting the explicitly prescribed corner and $3K$, and then dividing by $9$, does not introduce any new support: the $K$-band itself is on this half-grid. Therefore


$$
\operatorname{supp}(J\bmod9)
\subseteq\{m-1,m\}\cup\mathcal J,
\tag{8}
$$


where


$$
\mathcal J=
\left\{
\frac{bH/27-1}{2}-i-\epsilon:
b=1,3,\ldots,25,\
0\le i<\nu,\ \epsilon\in\{0,1\}
\right\}.
\tag{9}
$$


The possible $b=27$ bands are absorbed into the edge cover.

This establishes the required new nonedge cover from the full $V\bmod81$ formula.

## 3. Evaluation of $KRFe_d$ and $(FRF)_{dd}$ modulo $27$

Reuse the established exact inverse bands:


$$
R_{ab}=[z^{D+r_1-a-b}](1-z)^{-A},
$$


whose coefficients modulo $27$, below degree $H$, are supported on


$$
[kH/9,kH/9+D],\qquad0\le k\le8.
\tag{10}
$$



### 3.1 $KRFe_d=0\pmod{27}$

For a nonedge position


$$
a=\frac{bH/9-1}{2}-l-\epsilon,\qquad b\ \text{odd},
$$


the degree selected by row $i$ of $KR$ is


$$
D+\left(\frac13-\frac b{18}\right)H
+\frac12+i+l+\epsilon.
\tag{11}
$$


Its macroscopic center is an odd multiple of $H/18$, whereas the inverse bands in (10) are centered at even multiples of $H/18$. The finite shifts cannot bridge their separation.

The two edge positions are killed exactly:


$$
KRe_m=KRe_{m-1}=0.
$$


Hence


$$
\boxed{KRFe_d=0\pmod{27}.}
\tag{12}
$$



### 3.2 $(FRF)_{dd}=0\pmod{27}$

For two nonedge positions in (4), the selected inverse degree is


$$
D+\left(\frac12-\frac{b+b'}{18}\right)H
+\frac12+l+l'+\epsilon+\epsilon'.
\tag{13}
$$


Because $b+b'$ is even, its macroscopic center is again an odd multiple of $H/18$, disjoint from (10).

For edge–nonedge contributions, use the exact identities


$$
Re_m=e_d,\qquad Re_{m-1}=e_{d+1}+Ae_d.
$$


The established small-corner estimate gives


$$
w_d=w_{d+1}=0\pmod{729}.
$$


Edge–edge pairings vanish in the exact far corner of $R$. Consequently


$$
\boxed{(FRF)_{dd}=w^TRw=0\pmod{27}.}
\tag{14}
$$



Together with the reused $KRK^T=0\pmod{27}$ and $Je_d\in81\mathbb Z_3^\nu$, this evaluates every term:


$$
\boxed{A_9=0\pmod{27}.}
\tag{15}
$$



## 4. Evaluation of every $A_{27}$ term modulo $9$

### 4.1 $KRJ^T=JRK^T=0$

For a nonedge $J$-position in (9), $KR$ selects a degree centered at


$$
\left(\frac13-\frac b{54}\right)H.
$$


Its numerator in units $H/54$ is odd. Modulo $9$, the inverse bands are centered at multiples of $H/3=18H/54$, whose numerators are even. The separation is at least $H/54-O(D)$.

Edges are killed exactly as before. Thus


$$
\boxed{KRJ^T=JRK^T=0\pmod9.}
\tag{16}
$$



### 4.2 $JRFe_d=0$

Use (5). The edge contribution vanishes because


$$
Je_d=Je_{d+1}=0\pmod9.
$$


For the contribution $3JRv$, only $J,R,v\bmod3$ is needed. A nonedge $J\bmod3$ position is centered at an odd multiple of $H/18$; a position of $v$ is centered at $H/6=3H/18$. Their sum has even numerator, whereas $r_1$ has center $9H/18$. The selected degree is therefore separated from the only modulo-$3$ inverse band $[0,D]$.

Hence


$$
\boxed{JRFe_d=0\pmod9.}
\tag{17}
$$



### 4.3 The actual $Fp_i\bmod9$ support

This calculation is needed at higher precision than A4’s modulo-$3$ certificate.

Modulo $9$, the exact finite inverse gives


$$
RK^Te_i=p_i,\qquad
p_i=y^{H/3+i}(y-1)^D,\qquad0\le i<\nu.
\tag{18}
$$


Indeed the next inverse band would be supported in $i,\ldots,D+i$, entirely below HIGH; all further bands also lie outside HIGH.

For the actual $F$-formula:

* $X_Up_i=0\pmod9$. Its lower first-pole coefficient lies between the $H/3$-grid positions, while the depth-one endpoint positions also miss the range $0\le u<D$.
* The $c_0E_0p_i$ contribution is supported at $r_2-i$. Here $c_0\equiv3\pmod9$; the possible upper grid position lies above HIGH.
* The linear top term is supported at $r_2-i-1$, with a possible additional entry at $m$.
* The first lower pole is supported at $r_2-i,r_2-i-1$.
* At depth one, the endpoint branches either miss HIGH or give positions above $m$; the linear-core factor would supply a further factor $3$ and vanishes modulo $9$.

Therefore the full actual matrix satisfies


$$
\boxed{
\operatorname{supp}(Fp_i\bmod9)
\subseteq\{r_2-i,\ r_2-i-1,\ m\}.
}
\tag{19}
$$


In particular, this calculation retains and eliminates the LOW-unit correction rather than omitting it.

The supports of $p_t$, centered at $H/3$, are disjoint from (19). Consequently


$$
\boxed{KRFRK^T=0\pmod9.}
\tag{20}
$$



### 4.4 $KRFRFe_d=0$

By (18), its $i$-th entry is


$$
(Fp_i)^TRw.
$$


The nonedge positions of $Fp_i$ are centered at $H/6$. The nonedge positions of $w\bmod9$ have the same center and are divisible by $3$. Their inverse pairings select degrees centered at $H/6$, away from the modulo-$9$ inverse bands.

Pairings with the edges reduce to the small coordinates $d,d+1$, where $w$ and $Fp_i$ vanish at the required precision. Thus


$$
\boxed{KRFRFe_d=0\pmod9.}
\tag{21}
$$



### 4.5 $(FRFRF)_{dd}=0$

Again write $w=u+3v\pmod9$. Then


$$
(Rw)^TF(Rw)
=(Ru)^TF(Ru)+6(Ru)^TF(Rv)\pmod9.
$$


The first term vanishes by the established small $F$-corner, since $Ru$ is supported at $d,d+1$.

For the cross term only modulo $3$ is needed. The actual columns $Fe_d,Fe_{d+1}\bmod3$ are supported in the last three HIGH positions. Applying $R$ sends these to the first three HIGH positions, disjoint from the support of $v$. Thus the cross term vanishes as well:


$$
\boxed{(FRFRF)_{dd}=0\pmod9.}
\tag{22}
$$



Equations (16), (17), (20), (21), and (22) evaluate all the terms in the assigned expression:


$$
\boxed{A_{27}=0\pmod9.}
\tag{23}
$$



## 5. Sixth form, endpoint, and primitive arithmetic

The established complete identity now reduces to


$$
T_6=-\left(A_9/9+A_{27}/3+A_{81}\right)
\equiv-A_{81}\pmod3.
$$


Accordingly:

* **Proved here:** both lower divided contributions are zero.
* **Conditional on A4’s separate certification $A_{81}=0$:**
  

$$
T_6=0,\qquad \operatorname{rank}T_6=0,\qquad
  \operatorname{im}T_6=\{0\}.
$$


  The transported endpoint remains
  

$$
\bigl((-1)^i\bigr)_{0\le i<\nu}\ne0,
$$


  and would therefore lie outside that image.

Restoring $\lambda$ preserves all the zero congruences. I make no independent sixth-rank claim before the third contribution is certified.

Retain the final integer pair and its **final gcd**


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|).
$$


For $B_{\rm det}\ne0$, the actual reduced center is


$$
q=\frac{|B_{\rm det}|}{g},\qquad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g,
$$


and its whole real error is exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_{\rm det})\ell^{(n+1)/2}}{g}
\det H_{\rm complete}.
}
$$


The primitive multiplier remains $\ell^{(n+1)/2}/g$. No unrelated Smith lower bounds have been subtracted to estimate $q$. Neither response nonvanishing nor whole-error nonvanishing is established by the contractions above.

## Closing ledger

1. **New result and proof status.** Proved on the stipulated SAME243 domain: the new actual $Fe_d\bmod27$ and $J\bmod9$ support covers, $KRFe_d=(FRF)_{dd}=0\pmod{27}$, and every remaining $A_{27}$ contraction modulo $9$. Hence $A_9/9=A_{27}/3=0\pmod3$. The block and division factors in the new note pass the audit.

2. **Exact remaining bottleneck.** The sixth form is now $-A_{81}\pmod3$; its final rank and endpoint-image conclusion await A4’s separate certification. Beyond sixth saturation, an irrationality proof still needs same-index control of the actual denominator after the final gcd and nonzero whole primitive errors tending to zero. Irrationality of $e+\pi$ remains undecided.

3. **Computation request.** None. The new conclusions are uniform finite-band arguments on the full index domain, not extrapolations from finite numerical evidence.
