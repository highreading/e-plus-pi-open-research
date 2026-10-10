> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the precision-$32$ calculation and the actual first endpoint-annihilator lift

## Abstract and decision

The principal matrix conclusion of A1 Turn 6 survives audit:



$$
\frac{\widehat{\mathscr G}^{\,T}T_{c,\mathrm{red}}\widehat{\mathscr G}}{3^5}
\equiv-\mathsf D\pmod3,
\qquad
\mathsf D_{uv}
=[y^{(P/3-1)/2-u-v}](1-y)^{2\chi}.
\tag{A}
$$



The newly active denominator layer in the $p=17$ compression is legitimate. The new pole layers are complete, and their weighted cancellations have the stated signs. The finite prefix argument is also valid, but its proof needs one detail made explicit: the residual arrays must be chosen constant on their supported anti-diagonals, not merely supported on the displayed grids. This property follows from the corrected-pairing compression. I supply the resulting finite convolution proof below.

The finite $J$-bordering argument is correct. It retains the last middle column and proves that its unknown coupling is invisible to the quadratic matrix return at $3^5$. It does **not** evaluate the corresponding endpoint return.

The lowest actual endpoint is not open. Reusing the accepted original H2 endpoint gives


$$
\overline f_{\mathrm{act,new}}(g_{L_*+u})
=(-1)^{R_*+L_*+u}.
\tag{B}
$$


Thus the previous lowest-endpoint OPEN label is withdrawn.

Combining (A), the accepted common-frame actual/core matrix transfer, and (B), I obtain the following evaluated **actual** result. After exact endpoint adaptation and elimination of a complement lying in the exact endpoint kernel, the first divided matrix on the endpoint-annihilating radical is


$$
\boxed{
\frac{S_{\mathrm{ann}}}{3^5}
\equiv
-\left(
[y^{\kappa_1-u-v}](1-y)^{2\chi}(1+y)^2
\right)_{0\le u,v\le\delta-2}
\pmod3,
\qquad
\kappa_1=\frac{P/3-1}{2}.
}
\tag{C}
$$



This is the parent’s proposed operator, now justified as an actual returned operator rather than an auxiliary binomial model.

The physical $3^5$ digit is protected from both exact endpoint adaptation and the new $3^{-4}$ complement elimination. The separately adapted $3^6$ digit is not protected in general: its change contains an explicit symmetric term involving


$$
\frac{f_{\mathrm{act,new}}(g_{L_*+u}+g_{L_*+u+1})}{3}\pmod3.
$$


I derive that term, including the simultaneous complement return, in Section 9.

No primitive-denominator saving, whole-error estimate, or conclusion about the rationality of $e+\pi$ follows.

---

## 1. Original objects, finite boundaries, and reused scope

### 1.1 The original index family

All uniform statements concern sufficiently large indices in exactly the original family:


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
\qquad C_{16}=147968\,3^{15},
$$


and


$$
\frac{103}{1000}<\rho=\frac{N_0}{P_0}<\frac{104}{1000}.
$$



Retain


$$
P_0=243P=3^{h-27},\qquad N_0=243r,\qquad D=P_0+N_0,
$$




$$
P=3^{h-32},\qquad r\equiv2\pmod9,\qquad r\ \text{odd},
$$




$$
4^j=243(3^{26}-1)P-243r+1.
$$



Write


$$
x=y-1,\qquad Q=27P,\qquad b=Q-N_0,\qquad R=\frac b2,
\qquad \chi=P-R.
$$


Then


$$
D=10Q-b,\qquad N_0=25P+2\chi,
$$


and the original window gives


$$
.064<\frac bQ<.073,\qquad
.0145<\frac{\chi}{P}<.136.
\tag{1.1}
$$



No independent values of $P,\chi,r$, or $R$ are substituted for original indices. The previously established original-index density result is used only at its stated scope.

### 1.2 Complete functional and corrected columns

The finite coordinates are


$$
U_s=x^s\quad(0\le s<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
\nu=\frac D2-1,\qquad
Y_t=y^t\quad(d\le t\le m),\qquad d=D+\nu,
$$


with


$$
W=[U\ Y].
$$



The physical HIGH terminal remains $Y_m$. It is not the last middle direction $z_{\nu-1}$.

The complete functional is


$$
\mathcal M(P)=
-\frac{3^h}{4}\mathfrak f(P)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](P-P(-1))/(y+1)}{2v+1},
\qquad
\mathfrak f(y^t)=(2t)!.
$$


The core is


$$
G_c(f,g)=\mathcal M(Q_cfg),
\qquad
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A.
$$



The corrected columns are


$$
E_c=G_c(W,W),\qquad
F_i=z_i-WE_c^{-1}G_c(W,z_i).
$$


The prescribed one-lift inputs are


$$
\Psi_a=x^{D+b}y^{k_0+a}(y^{3Q}+3),
\qquad
k_0=\frac{3Q+1}{2},\qquad 0\le a\le R,
$$


and $\mathcal F_a$ denotes correction against this same finite $W$.

The retained boundaries are


$$
R_*=\frac{9Q+1}{2},\qquad a_0=R_*-1,
$$




$$
\tau=\frac{N_0-3}{2},\qquad \ell=3R+1,
$$




$$
K=\{0,\ldots,\ell-1\},\qquad
J=\{\ell,\ldots,\tau-1\},
$$




$$
n_J=\frac{Q-4b-5}{2},\qquad R_*+\tau=\nu.
\tag{1.2}
$$



The physical pole cutoff is


$$
K_{\mathrm{phys}}=2n-2=2H-2D+2,
$$


whose largest denominator is


$$
2K_{\mathrm{phys}}+1=4H-4D+5<3^{h+1}.
\tag{1.3}
$$


Consequently the physically truncated pole functional preserves coefficientwise $3$-adic divisibility.

### 1.3 Closed inputs reused

The following are background results, not new claims of this report:

* the admitted $p=17$ mixed filter and its original degree range;
* residual valuation $17$, the one-digit mixed inverse loss, and the resulting stationary error $3^{33}$;
* the complete-core/pole transfer at its stated precision;
* the exact Jacobi scalar $K_N$, with $K_N\equiv1\pmod3$;
* the finite first-prefix lift and the exact return identities;
* H2, the unit $J$-block, and the original rank-$b$ quotient;
* the closed terminal theorem
  

$$
[y^m]\mathcal F_a\equiv-3^{27}\delta_{a,R}\pmod{3^{28}},
  \qquad \gamma_c=0;
$$


* the complete radical and saturated complement of A1 Turn 5;
* the accepted Turn 7 actual/common-frame matrix transfer.

For the new actual conclusion, the minimum consequence of the last item that is needed is


$$
T_{\mathrm{act,red}}\equiv T_{c,\mathrm{red}}\pmod{3^6}
\tag{1.4}
$$


in the retained common amplitude frame. The accepted precision-$7$ comparison is stronger. It is reused only as a **matrix** theorem; no endpoint or diagonal congruence is appended to it.

The original H2 actual endpoint theorem is also reused, explicitly in Section 8.

---

## 2. Original-arithmetic support: PASS

Put


$$
L_*=\frac{P-1}{2},\qquad
\kappa=\frac{3P-3}{2},
$$




$$
\delta=\min\left\{\chi-1,\frac{P+3}{2}-3\chi\right\},
$$


and


$$
g_{L_*+u}(y)=(1-y)^{2\chi}y^{L_*+u},
\qquad 0\le u<\delta.
$$



The Turn 5 theorem supplies the **entire** radical of the leading core matrix and a saturated integer lift $\mathscr G$ of this basis.

From


$$
\chi=\frac{243r-25P}{2}
$$


one obtains, for sufficiently large original indices,


$$
243\mid\chi,
\qquad
\frac{\chi}{243}\equiv1\pmod9.
\tag{2.1}
$$



For $s=L_*+u,\ t=L_*+v$, define


$$
n_{uv}=\kappa-s-t=L_*-u-v.
$$


Then


$$
\min_{u,v}(n_{uv}-2\chi)
=\frac{P+3}{2}-2\delta-2\chi.
$$



On the branch $\delta=\chi-1$, this is


$$
\frac{P+7}{2}-4\chi>0,
\qquad
\frac{P+7}{2}-4\chi\equiv125\pmod{243}.
$$


On the other branch, it is


$$
4\chi-\frac{P+3}{2}>0,
\qquad
4\chi-\frac{P+3}{2}\equiv120\pmod{243}.
$$


The strict positivity follows directly from the inequality selecting the branch. Therefore


$$
\boxed{2\chi+120\le n_{uv}\le L_*<P.}
\tag{2.2}
$$



This is a valid original-arithmetic gap, not merely an asymptotic separation. It pays all the small coefficient shifts below. In particular, the inverse $A_-$ correction can produce a total shift of three after both grid offsets are included; the gap $120$ still more than suffices.

---

## 3. Extension of the same $p=17$ compression: PASS

Let


$$
N=3^{16},\qquad L=3^{h-17},\qquad H=NL.
$$


For $\deg p_i\le\nu-2$, retain the admitted trials


$$
\widetilde F[p_i]=x^Dp_iR_N(y^L).
$$



### 3.1 Errors which do not change

The existing payments remain


$$
\begin{array}{c|c}
\text{error}&\text{valuation lower bound}\\ \hline
\text{stationary projection error}&33\\
\text{exponential terms of order at least two}&34\\
\text{bare macro-denominator replacement}&35\\
\text{logarithmic reciprocal replacement}&34\\
\text{complete-core transfer}&h.
\end{array}
\tag{3.1}
$$



For clarity, if


$$
B=x^D(\beta+3y)p_1p_2,
$$


then


$$
\deg B\le2D-5,\qquad v_3(2s+1)\le h-26
\quad(0\le s\le\deg B).
\tag{3.2}
$$



In the formal logarithmic expansion, write


$$
k=v-qL-s,\qquad c=2s+1,\qquad d_v=2v+1.
$$


A scalar logarithmic term has valuation


$$
2h-1-v_3(k)-v_3(d_v).
$$



If $v_3(k)<v_3(c)$, the relation


$$
d_v=2k+c+2qL
$$


gives $v_3(d_v)=v_3(k)$, and the valuation is at least $53$.

If $v_3(k)>v_3(c)$, then $v_3(d_v)=v_3(c)$. Since the logarithmic sum excludes multiples of $L$, $v_3(k)\le h-18$, giving the lower bound $43$.

Thus only $v_3(k)=v_3(c)$ can matter.

### 3.2 The new active layer is included

To retain terms modulo $3^{32}$, one must include


$$
v_3(d_v)\ge h-6.
\tag{3.3}
$$


These denominators remain multiples of $L$. The replacement


$$
\frac1k\longmapsto-\frac2c
$$


has error


$$
\frac1k+\frac2c=\frac{d_v-2qL}{kc}.
$$


After multiplication by $3^hH/d_v$, its valuation is at least


$$
3h-18-v_3(d_v)-2v_3(c)\ge34.
$$


The added $h-6$ layer therefore does not invalidate the reciprocal replacement.

The newly inactive terms have $v_3(d_v)\le h-7$, so


$$
2h-1-(h-26)-(h-7)=32.
\tag{3.4}
$$


Their addition to the complete macro sum is paid at the new modulus.

### 3.3 Physical macro completion remains exact

Let


$$
A_{\mathrm{mac}}(Y)=(Y-1)^NR_N(Y)^2.
$$


Then


$$
\deg A_{\mathrm{mac}}=2N-1,\qquad A_{\mathrm{mac}}(1)=0.
$$



The trial degree and bare macro support satisfy


$$
m-\deg\widetilde F[p_i]\ge\frac{L-4D+7}{2}>0,
$$




$$
(2N-1)L+\deg B
\le2H-L+2D-5<K_{\mathrm{phys}}.
$$



If $d_v=(2q_0+1)L$, the condition $k>0$ is exactly $q\le q_0$, because $s<(L-1)/2$. The physical position $q_0=2N-1$ is present, but its partial sum is the complete zero $A_{\mathrm{mac}}(1)$. The last potentially nonzero completed term has denominator


$$
(4N-3)L<4H-4D+5.
$$


The next macro position is outside the cutoff.

No terminal macro term has been silently omitted.

### 3.4 Audited compression theorem

Consequently, on the same admitted degree range,


$$
\boxed{
G_c(F[p_1],F[p_2])
\equiv
K_N\mathcal J_h\!\left(x^D(\beta+3y)p_1p_2\right)
\pmod{3^{32}},
}
\tag{3.5}
$$


where


$$
\mathcal J_h(B)=3^h\sum_{s=0}^{\deg B}\frac{[y^s]B}{2s+1}.
$$



All one-lift amplitudes used in the double radical contraction satisfy the degree restriction, since


$$
b+k_0+R+3Q=R_*+3R<\nu-2
$$


for sufficiently large original indices.

The last middle column $F_{\nu-1}$ does not satisfy that restriction and will not be compressed.

---

## 4. Complete pole audit and the modulo-$9$ band: PASS

Let


$$
X(y)=(y-1)^{10Q}.
$$


Before radical multiplication, the relevant polynomial is


$$
X(y)(\beta+3y)y^{3Q+1+w}(y^{3Q}+3)^2,
\qquad 0\le w\le2b.
\tag{4.1}
$$


The original window supplies


$$
2b+4<\frac Q6.
\tag{4.2}
$$



For $Q=3^q$, $k=uQ+r$, $0<r<Q$, reuse the established exact valuation


$$
v_3\binom{10Q}{k}
=q-v_3(r)+v_3\binom9u.
\tag{4.3}
$$



### 4.1 Complete layer list

At precision $3^{32}$, the smallest relevant denominator grid is $Q/9$. The layer audit is:

| Denominator grid | Pole weight | Outcome |
|---|---:|---|
| unit multiple of $Q/9$ | $3^{31}$ | Four unit-coefficient contributions; their weighted sum is zero |
| unit multiple of $Q/3$ | $3^{30}$ | Coefficient valuation at least $2$; no contribution |
| unit multiple of $Q$ | $3^{29}$ | Two valuation-$2$ high coefficients; weighted sum zero |
| unit multiple of $3Q$ | $3^{28}$ | Valid bands have coefficient valuation at least $4$ |
| $9Q$ | $3^{27}$ | Only the explicitly $9$-weighted low term can enter; too deep |
| $27Q$ | $3^{26}$ | Old coefficient, neighboring $P$-bands, high $3y$, and weighted middle term |

This includes both terms of $\beta+3y$ and all three terms of $(y^{3Q}+3)^2$.

### 4.2 The two weighted cancellations

At the unit-$Q$ layer, valuation $2$ can occur only in the high term at


$$
19Q,\quad37Q,\qquad w=\kappa.
$$


The signed normalized coefficient units are $2$ and $1$; both denominator units are $1\pmod3$. Hence their sum is zero.

One can verify the relative sign without a new large table: after stripping the common power of $3$, the relevant binomials are $\binom{90}{4}$ and $\binom{90}{5}$, whose normalized units agree modulo $3$, while the coefficient parities are opposite. The first normalized unit is $2$.

At the new unit-$Q/9$ layer, $X\bmod3$ is


$$
X(y)\equiv1-y^Q-y^{9Q}+y^{10Q}.
$$


A unit coefficient can occur only at $w=\kappa$. The four denominators are


$$
(163+18u)\frac Q9,\qquad u=0,1,9,10.
$$


They are all physical and all have unit part $1\bmod3$. Their complete weighted residue is


$$
1-1-1+1=0.
\tag{4.4}
$$



Thus the newly active layer genuinely cancels. It is not absent by an extrapolated support claim.

### 4.3 The $27Q$ pole and signed units

The high extraction is


$$
k=\frac{9Q-3}{2}-w.
$$


Its valuation-$4$ coefficient is at $w=\kappa$. The additional valuation-$5$ coefficients are


$$
w=\kappa-P,\qquad \kappa+P,\qquad \kappa+2P,
$$


when those indices belong to $0\le w\le2b$.

Their signed normalized units are


$$
1,\qquad2,\qquad1.
\tag{4.5}
$$


They reduce respectively to the signed units of


$$
\binom{270}{121},\qquad
\binom{270}{119},\qquad
\binom{270}{118}.
$$



The high $3y$ term contributes at order $3^{31}$, supported at


$$
w=\kappa-1.
$$


The $6$-weighted middle term contributes at order $3^{31}$, supported at $w=\kappa$. Its signed normalized binomial coefficient is $1$, so the additional factor $6/3$ gives weighted unit $2$. The explicitly $9$-weighted low term cannot contribute at this precision.

The old normalized coefficient at $40Q/9$ is reused with unit $1$. Its closed $\binom{90}{40}$ calculation is not repeated.

### 4.4 Radical multiplication eliminates every new order-$31$ pole term

For $s=L_*+u,\ t=L_*+v$,


$$
(1-y)^b g_s(y)g_t(y)
=y^{s+t}(1-y)^{2P+2\chi}.
$$


Put


$$
F(y)=(1-y)^{2P+2\chi}.
$$


Modulo $3$,


$$
F(y)\equiv(1+y^P+y^{2P})(1-y)^{2\chi}.
\tag{4.6}
$$



The order-$31$ pole terms observe coefficients at


$$
n_{uv},\quad n_{uv}-P,\quad n_{uv}+P,\quad
n_{uv}+2P,\quad n_{uv}-1.
$$


By (2.2), these lie outside the three support bands in (4.6), or outside the polynomial altogether. Every such contracted contribution is therefore zero modulo $3$.

The order-$30$ term is different. Its contracted coefficient is divisible by $3$, but its quotient by $3$ must be evaluated.

### 4.5 Frobenius modulo $9$, including its sign

For a positive power $P$ of $3$,


$$
(1-y)^P
\equiv
1-3y^{P/3}+3y^{2P/3}-y^P\pmod9.
$$


This follows inductively by cubing: all terms involving a pre-existing factor $3$ disappear modulo $9$, except those already present in the cube of $1-y^{P/3}$.

Hence


$$
(1-y)^{2P}
\equiv
(1-y^P)^2+
6(1-y^P)(-y^{P/3}+y^{2P/3})
\pmod9.
\tag{4.7}
$$



Since


$$
2\chi<n_{uv}<P/2,
$$


only the band $-6y^{P/3}$ can enter the coefficient under consideration. Therefore


$$
\frac{[y^{n_{uv}}]F(y)}3
\equiv
-2[y^{n_{uv}-P/3}](1-y)^{2\chi}
\pmod3.
$$


Because $-2\equiv1\pmod3$,


$$
\boxed{
\frac{[y^{n_{uv}}]F(y)}3
\equiv
[y^{\kappa_1-u-v}](1-y)^{2\chi},
\qquad
\kappa_1=\frac{P/3-1}{2}.
}
\tag{4.8}
$$



The division is paid by (4.6). No value of the old binomial unit or of $K_N$ modulo $9$ is needed, because their multiplying coefficient is already divisible by $3$.

Thus


$$
\boxed{
\frac{\mathscr G^T G_c(\mathcal F,\mathcal F)\mathscr G}{3^{31}}
\equiv\mathsf D\pmod3.
}
\tag{4.9}
$$



---

## 5. Finite prefix inverse and every contracted correction: PASS, with an explicit proof completion

Let


$$
U(y)=(1-y)^{N_0},
$$


and, for $0\le p,q\le a_0$, define


$$
(A_0)_{pq}=U_{a_0-p-q},
$$




$$
(A_-)_{pq}=U_{a_0-1-p-q},\qquad
(A_+)_{pq}=U_{a_0+3Q-p-q}.
$$



### 5.1 The prefix matrix modulo $9$

The actual finite calculation gives


$$
\boxed{
\mathsf A
\equiv K_N(-2\beta A_0+3A_- -3\beta A_+)\pmod9.
}
\tag{5.1}
$$



Here is a sign check. Since $N_0$ is odd,


$$
x^{N_0}=-U,
$$


and


$$
x^{9Q}\equiv y^{9Q}-3y^{6Q}+3y^{3Q}-1\pmod9.
$$


After the sign in the normalized prefix matrix is included:

* the $27Q$ pole gives
  

$$
\beta A_0+3A_- -3\beta A_+;
$$


* the $9Q$ pole gives
  

$$
-3\beta A_0.
$$



The total is (5.1). Thus the displayed formula in A1 Turn 6 is correct. Its explanatory reference to an “additional $3\beta A_0$ term” must be read with this **negative** sign in $\mathsf A$.

### 5.2 The inverse is genuinely finite

The exact inverse of $A_0$ is


$$
(A_0^{-1})_{pq}
=[y^{p+q-a_0}]U^{-1}.
\tag{5.2}
$$


In the matrix product, nonzero summands force precisely the finite convolution interval. Thus no coefficient outside $0,\ldots,a_0$ is introduced.

Also,


$$
\boxed{
(A_0^{-1}A_-A_0^{-1})_{pq}
=[y^{p+q-a_0-1}]U^{-1}.
}
\tag{5.3}
$$


For example, writing $A_-=A_0S$, where $S$ is the finite one-step shift, proves (5.3). The apparently missing first row is already zero because its coefficient indices are negative. This establishes the shifted inverse formula without an infinite-matrix boundary assumption.

### 5.3 Residual grids and the necessary anti-diagonal property

The exact prefix relation is


$$
\mathsf A Z=d,\qquad
d_{pa}=\frac{G_c(F_p,\mathcal F_a)}{3^{28}}.
\tag{5.4}
$$



The pole audit modulo $3^{30}$ gives


$$
d_{pa}\equiv0\pmod9
$$


unless


$$
p+a+1\in3P\mathbb Z
\quad\text{or}\quad
p+a+2\in3P\mathbb Z.
\tag{5.5}
$$


Modulo $3$, the grid is $9P$ instead of $3P$.

Indeed, outside (5.5), the high $27Q$ extraction is a nonmultiple of $Q/9$ in $4Q<k<9Q$, so (4.3) gives coefficient valuation at least $4$. The explicitly weighted low term has at least three coefficient digits in addition to its factor $3$. Other pole contributions outside the same grids are deep enough.

A support statement alone would not justify absorbing both radical factors into a generating function. The needed additional fact is:

> Modulo $9$, $d_{pa}$ depends on $p+a$, not separately on $p$ and $a$.

This follows directly from (3.5), because the compressed prefix-to-one-lift polynomial depends on those two indices only through $p+a$. Its error, after division by $3^{28}$, is still zero modulo $9$.

Choose the canonical lift $d_0$ of $d\bmod3$, constant on these anti-diagonals, and write


$$
d=d_0+3d_1.
$$


Then $d_0$ has the $9P$-grid form and $\overline d_1$ has the $3P$-grid form, with coefficients independent of the amplitude.

The finite ranges are exactly


$$
p=k(3P)-a-\sigma,\quad 1\le k\le40,\quad \sigma\in\{1,2\},
$$


and


$$
p=k(9P)-a-\sigma,\quad 1\le k\le13,\quad \sigma\in\{1,2\}.
\tag{5.6}
$$


They are uniform for every $0\le a\le R$. For instance, the first positive grid point is positive even at $a=R$, the displayed last point is at most $a_0$, and the next point is larger than $a_0$ even at $a=R$.

This proves that radical multiplication does not create amplitude-dependent truncations.

### 5.4 Base inverse terms

After the two radical factors are absorbed, the relevant generating function is


$$
U^{-1}(1-y)^{4\chi}
=(1-y)^{2P+2\chi-Q}.
\tag{5.7}
$$



For grids of spacings $L,L'$, a coefficient index has the form


$$
kL+lL'-123P+n_{uv}-(\sigma+\tau-2).
\tag{5.8}
$$



For a $d_0$-$d_1$ cross term, its residue modulo $3P$ is


$$
n_{uv}-(\sigma+\tau-2).
$$


It lies strictly between $2\chi$ and $P$. Modulo $3$, (5.7) has support only in


$$
[0,2\chi],\quad[P,P+2\chi],\quad[2P,2P+2\chi]
\pmod{3P}.
$$


Thus every cross coefficient is zero.

For the $d_0$-$d_0$ term modulo $9$, the residue modulo $9P$ is


$$
3P+n_{uv}-(\sigma+\tau-2).
\tag{5.9}
$$


In


$$
(1-y)^{2P+2\chi-Q}
=\frac{(1-y)^{2P+2\chi}}{(1-y)^Q},
$$


the numerator has degree $2P+2\chi<3P$, while the denominator and its reciprocal modulo $9$ are series in $y^{9P}$. The residue (5.9) is above the numerator degree. The entire base contraction is therefore zero modulo $9$.

The $d_1$-$d_1$ term already carries a factor $9$.

### 5.5 The $A_-$ and $A_+$ corrections

The $A_-$ term shifts (5.8) down by one. Its residue modulo $3P$ remains strictly between $2\chi$ and $P$, even when the total shift is three. Hence it vanishes.

For $A_+$, put


$$
z_0=A_0^{-1}d_0\mathscr G.
$$


The relevant one-sided convolution is


$$
U^{-1}(1-y)^{2\chi}
=(1-y)^{2P-Q}
\equiv\frac{1+y^P+y^{2P}}{1-y^Q}\pmod3.
$$


Consequently column $u$ of $z_0$ is supported only on rows


$$
p\equiv u\quad\text{or}\quad u+1\pmod P.
\tag{5.10}
$$



Meanwhile


$$
U(y)\equiv(1-y^P)^{25}(1-y)^{2\chi}\pmod3.
$$


A potentially observed $A_+$ coefficient has residue


$$
n_{uv}-i-j,\qquad i,j\in\{0,1\},
$$


again strictly between $2\chi$ and $P$. Every such entry is zero.

Expanding (5.1) as a unit inverse modulo $9$ now accounts for the base term, both cross terms, and both inverse corrections. Therefore


$$
\boxed{
\mathscr G^TZ^T\mathsf A Z\mathscr G\in9M.
}
\tag{5.11}
$$



The proof does not require the individual grid weights to be evaluated: every allowed weight multiplies a coefficient just proved to be zero. This is a termwise finite annihilation argument, not an unevaluated sum presented as a result.

---

## 6. The finite $J$-return, including the last middle column: PASS

Define


$$
\mathscr L=\frac{L_c^TG\mathscr G}{3}.
\tag{6.1}
$$


Its integrality is paid by the accepted $\gamma_c=0$.

### 6.1 Interior couplings

For


$$
\ell\le v\le\tau-2,
$$


the column $F_{R_*+v}$ is admitted by the compression theorem. Put


$$
\kappa_0=\frac{9P-3}{2}.
$$


The compressed cross polynomial is


$$
x^{10Q}(\beta+3y)y^{6Q+1+v+a}(y^{3Q}+3),
$$


with


$$
v+a\le\frac{Q-7}{2}.
\tag{6.2}
$$



At $27Q$, the high extraction lies strictly between $4Q$ and $9Q/2$. Valuation $3$ occurs only when its remainder is $Q/3$, namely at


$$
v+a=\kappa_0.
$$


The signed normalized unit is $1$, from the signed coefficient associated with $\binom{30}{13}/3^3$. Every other term is deeper. Hence


$$
\frac{G_c(F_{R_*+v},\mathcal F_a)}{3^{29}}
\equiv\delta_{v+a,\kappa_0}\pmod3.
\tag{6.3}
$$



The divided prefix cross block gives the same finite selector:


$$
\left(
\overline{\mathsf B_v/3}^{\,T}\overline{\mathsf A}^{-1}
\right)_p
=-\delta_{p,k_0+v}.
\tag{6.4}
$$


The selected row is inside the actual prefix.

At $p=k_0+v$, the high $27Q$ extraction in the residual is at least $7Q+2$; after the $3y$ shift it is still at least $7Q+1$. The relevant coefficients have at least three digits, and the other layers are likewise too deep. Therefore


$$
d_{k_0+v,a}\equiv0\pmod3.
$$


The upper bound (6.2) is what excludes the troublesome last-middle boundary extraction.

Combining these facts,


$$
\boxed{
\overline{\mathscr L}_{v,u}
=-[y^{\kappa_0-v-L_*-u}](1-y)^{2\chi}.
}
\tag{6.5}
$$


Writing $i=v-\ell$, the support lies in


$$
P+\chi-2-u\le i\le P+3\chi-2-u.
\tag{6.6}
$$


In particular its first $J$-coordinate is zero, and all displayed support lies strictly inside $J$.

No value for the last coupling is inferred from (6.5).

### 6.2 Leading interior $J$-block

For rows and columns other than the last, compression modulo the needed precision gives


$$
\overline B_{c,ij}
=[y^{N_0+n_J-1-i-j}]U
=-[y^{i+j-n_J+1}]U.
\tag{6.7}
$$



One may check the finite extraction directly. At the $27Q$ pole, only the $3y^{3Q}$ band in the expansion of $x^{9Q}$ can enter. Its index becomes


$$
\frac{3Q-3}{2}-(\ell+i)-(\ell+j)
=N_0+n_J-1-i-j.
$$


The prefix correction is zero in this leading $J$-digit because both prefix cross blocks are divisible by $3$.

Let $N_J=n_J$. Retaining the actual last row and column, write


$$
\overline B_c=
\begin{pmatrix}
0&0&a\\
0&B_I&w\\
a&w^T&c
\end{pmatrix}.
\tag{6.8}
$$


The established unit property of $B_c$ implies $a\ne0$. The finite interior inverse is


$$
(B_I^{-1})_{ij}
=-[y^{N_J-1-i-j}]U^{-1},
\qquad1\le i,j\le N_J-2.
\tag{6.9}
$$


Its dimension is exactly $N_J-2$.

### 6.3 Exact bordering, not an endpoint evaluation

For two vectors


$$
l=(0,l_I,l_\partial),\qquad
l'=(0,l'_I,l'_\partial),
$$


solving the first row of (6.8) forces the last coordinate of $\overline B_c^{-1}l'$ to be zero. Therefore


$$
\boxed{
l^T\overline B_c^{-1}l'=l_I^TB_I^{-1}l'_I.
}
\tag{6.10}
$$


This bilinear identity proves the matrix assertion directly.

For the supports (6.6), every coefficient index in (6.9) lies strictly between $b$ and $Q$. For example the extreme bounds are


$$
\frac{15P-4\chi+1}{2}
\le N_J-1-i-j
\le
\frac{15P+4\chi+4\delta-3}{2}.
$$


These are $>b$ and $<Q$ throughout the original window.

But


$$
U^{-1}
\equiv\frac{(1-y)^b}{1-y^Q}\pmod3
$$


has no coefficient in that interval. Hence


$$
\boxed{\mathscr L^TB_c^{-1}\mathscr L\equiv0\pmod3.}
\tag{6.11}
$$


Its physical matrix return is


$$
27\mathscr G^TG^TL_cB_c^{-1}L_c^TG\mathscr G
=3^5\mathscr L^TB_c^{-1}\mathscr L\in3^6M.
\tag{6.12}
$$



For an endpoint vector $f=(f_0,f_I,f_\partial)$, the corresponding identity is instead


$$
\boxed{
l^T\overline B_c^{-1}f
=
l_I^TB_I^{-1}\left(f_I-\frac wa f_0\right)
+\frac{l_\partial f_0}{a}.
}
\tag{6.13}
$$


Thus the boundary coupling is generally visible to the endpoint channel.

On the present radical its full endpoint return carries the additional physical factor $9$, because $L_c^TG\mathscr G=3\mathscr L$. This makes it invisible to the lowest endpoint digit; it does not evaluate its higher contribution.

---

## 7. Assembly, arithmetic entry evaluation, and ranks: PASS

### 7.1 All matrix returns

The exact retained identity is


$$
T_{c,\mathrm{red}}
=
-\frac{G_c(\mathcal F,\mathcal F)}{3^{26}}
-81Z^T\mathsf A Z
-27G^TL_cB_c^{-1}L_c^TG
-81M_{b,c}^TA_{b,c}^{-1}M_{b,c}.
\tag{7.1}
$$



The accepted Turn 5 proof gives


$$
M_{b,c}\in3M.
$$


Its proof uses the original finite prefix selector and $\gamma_c=0$, so the corresponding return is in $3^6M$.

Let


$$
\mathcal C=\{0,\ldots,R\}\setminus
\{L_*,\ldots,L_*+\delta-1\},
$$




$$
K_c=T_{c,\mathrm{red}}/81,
$$




$$
A_c=E_{\mathcal C}^TK_cE_{\mathcal C},
\qquad
C_c=E_{\mathcal C}^TK_c\mathscr G.
$$


The full radical theorem and its saturated complement prove


$$
A_c^{-1}\in M(\mathbb Z_3),\qquad C_c\in3M.
$$


Thus


$$
\widehat{\mathscr G}
=\mathscr G-E_{\mathcal C}A_c^{-1}C_c
$$


is an exact lift, and its physical return is


$$
81C_c^TA_c^{-1}C_c\in3^6M.
\tag{7.2}
$$



Equations (4.9), (5.11), (6.12), and (7.2) prove


$$
\boxed{
\frac{\widehat{\mathscr G}^{\,T}
T_{c,\mathrm{red}}\widehat{\mathscr G}}{3^5}
\equiv-\mathsf D\pmod3.
}
\tag{7.3}
$$



Every division in (7.3) is paid.

### 7.2 Every entry is explicitly evaluated

For $k=\kappa_1-u-v$, the entry is zero outside $0\le k\le2\chi$. Otherwise, if


$$
2\chi=\sum_i c_i3^i,\qquad k=\sum_i k_i3^i,
$$


then


$$
\mathsf D_{uv}
=(-1)^k\prod_i\binom{c_i}{k_i}\quad\text{in }\mathbb F_3.
\tag{7.4}
$$


This follows by expanding


$$
(1-y)^{2\chi}
=\prod_i(1-y^{3^i})^{c_i}
$$


in characteristic $3$.

In particular,


$$
\mathsf D_{uv}=0
\quad\text{unless}\quad u+v\equiv121\pmod{243}.
$$


For sufficiently large original indices, (2.1) gives the sharper condition


$$
u+v\equiv607,\ 850,\ 1093\pmod{2187}.
\tag{7.5}
$$


The latter assertion uses $\kappa_1\equiv1093\pmod{2187}$, valid once the original power $P/3$ is divisible by $2187$.

### 7.3 Ranges I and II

Put


$$
B_1=2\chi+2\delta-1-\kappa_1,\qquad
\varepsilon=2\chi+\delta-P/3.
$$



Reversing both coordinate orders and using the symmetry of the coefficients of $(1-y)^{2\chi}$ changes the entries to


$$
[y^{B_1-1-u-v}](1-y)^{2\chi}.
$$



* If $B_1\le0$, every entry is zero.
* If $0<B_1\le\delta$, the first $B_1$ reversed coordinates form an anti-triangular block with anti-diagonal $1$, and all other rows and columns are zero.

Therefore


$$
\operatorname{rank}\mathsf D=B_1,\qquad
\ker\mathsf D
=\operatorname{span}\{e_0,\ldots,e_{\delta-B_1-1}\}
$$


in Range II. The last $B_1$ original monomials are an explicit unit complement.

These arguments are finite and characteristic-independent at the anti-triangular step.

### 7.4 Range III: primitive syzygy completeness

Let


$$
\Pi=P/3,\qquad
a=\frac{\Pi+1}{2},\qquad b'=B_1,\qquad c=2\chi,
$$


and assume $\varepsilon>0$.

The original inequalities imply


$$
a,b'>\delta-1,\qquad a,b',c\le\Pi,\qquad
a+b'=c+2\delta.
\tag{7.6}
$$


For the nontrivial bound $b'\le\Pi$, the definition of $\delta$ gives


$$
c+2\delta\le\frac{P+1}{2}
=\frac{3\Pi+1}{2},
$$


hence $b'=c+2\delta-a\le\Pi$.

The selected graded multiplication map has source degree $\delta-1$, multiplier $(Y-X)^c$, and target degree


$$
D_1=c+\delta-1=\Pi+\varepsilon-1.
$$


Its surviving target interval is exactly


$$
[\kappa_1-\delta+1,\kappa_1].
$$


Thus it is the required finite matrix, after row reversal.

The three forms $X^a,Y^{b'},(Y-X)^c$ have the syzygy


$$
S=
\left(
X^{\Pi-a},-Y^{\Pi-b'},(Y-X)^{\Pi-c}
\right)
$$


of total degree $\Pi$, because


$$
X^\Pi-Y^\Pi+(Y-X)^\Pi=0.
$$


Its first two components are coprime, so it is primitive.

For any syzygy $T$ of degree $D_1$, the cross product $S\times T$ is a polynomial multiple of


$$
(X^a,Y^{b'},(Y-X)^c).
$$


The multiplier degree would be


$$
\Pi+D_1-(a+b'+c)=-\varepsilon-1<0.
$$


It is therefore zero. Primitivity then forces


$$
T=fS,\qquad \deg f=\varepsilon-1.
$$



There is no ambiguity from a two-form syzygy, because


$$
a+b'=c+2\delta>D_1.
$$


Taking third components and dehomogenizing proves the complete radical


$$
\boxed{
(1-y)^{\Pi-2\chi}y^v,\qquad0\le v<\varepsilon.
}
\tag{7.7}
$$


Hence


$$
\boxed{
\operatorname{nullity}\mathsf D=\varepsilon,\qquad
\operatorname{rank}\mathsf D=\Pi-2\chi.
}
\tag{7.8}
$$



The first $\varepsilon$ coefficient rows of these integer lifts are triangular with diagonal $1$. They are saturated, and monomials $\varepsilon,\ldots,\delta-1$ give a unit complement.

The remaining range $B_1>\delta,\ \varepsilon\le0$ is not assigned a rank formula by A1 Turn 6. Its stated finite syzygy problem and degree $3\chi-2$ are correct.

### 7.5 Smith scope

If $r_1=\operatorname{rank}\mathsf D$, the complete core has exactly

* $R+1-\delta$ elementary divisors of valuation $4$;
* $r_1$ elementary divisors of valuation $5$;
* all others of valuation at least $6$, or zero.

The accepted common-frame transfer gives the same first two counts for the full returned actual matrix.

These are counts for the **full matrix**. They are not automatically the rank or Smith counts of the new endpoint-annihilator operator (C), and they are not primitive cofactor estimates.

---

## 8. The actual lowest endpoint is closed, and the $3^5$ adapted digit is protected

### 8.1 Reuse of the original actual endpoint

The accepted H2 theorem says


$$
\overline f_{\mathrm{act}}^{(2)}{}_u=(-1)^{R_*+u},
\qquad0\le u\le3R.
$$


The subsequent actual rank-$b$ endpoint is


$$
f_{\mathrm{act,new}}
=G^Tf_{\mathrm{act}}^{(2)}
-3M_{b,\mathrm{act}}^TA_{b,\mathrm{act}}^{-1}f_{\mathrm{act},b}.
\tag{8.1}
$$


The latter correction is divisible by $3$ using only the already established integrality of $M_{b,\mathrm{act}}$ and the unit inverse.

Because $b$ is even,


$$
\boxed{
\overline f_{\mathrm{act,new}}(a)
=(-1)^{R_*}a(-1)
}
\tag{8.2}
$$


for every amplitude of degree at most $R$. Hence


$$
\boxed{
\overline f_{\mathrm{act,new}}(g_{L_*+u})
=\sigma(-1)^u,\qquad
\sigma=(-1)^{R_*+L_*}\in\mathbb F_3^\times.
}
\tag{8.3}
$$



This is the actual returned endpoint, not a replacement by bare evaluation. It closes every lowest radical endpoint value.

### 8.2 Exact adaptation in the original amplitude lattice

For this section set


$$
T=T_{\mathrm{act,red}},\qquad K=T/81,\qquad
f=f_{\mathrm{act,new}}.
$$



Choose the endpoint-unit vector


$$
v=\frac{g_{L_*}}{f(g_{L_*})}.
$$


For $0\le u\le\delta-2$, let


$$
h_u=g_{L_*+u}+g_{L_*+u+1},
$$




$$
h_u^{\,f}=h_u-vf(h_u).
\tag{8.4}
$$


Then


$$
f(v)=1,\qquad f(h_u^{\,f})=0,\qquad
h_u^{\,f}-h_u\in3\,\operatorname{span}_{\mathbb Z_3}\mathscr G.
$$



For each original monomial complement column $e_i$, set


$$
V_i=e_i-vf(e_i).
\tag{8.5}
$$


Thus $f(V_i)=0$ exactly. The basis


$$
[v,\ V,\ H^f]
$$


is invertible over $\mathbb Z_3$: modulo $3$, the radical part is a unit-normalized first generator followed by the adjacent sums, and the complementary columns remain a complement to the full radical.

Because the leading matrix is $-\mathsf H_\kappa$, the matrix


$$
A_f=V^TKV
$$


is a unit matrix. Its cross blocks with $v$ and $H^f$ belong to $3M$.

Eliminate this complement exactly:


$$
\widehat H
=H^f-VA_f^{-1}V^TKH^f,
$$




$$
\widehat v
=v-VA_f^{-1}V^TKv.
\tag{8.6}
$$


These vectors remain in the original finite amplitude space. They satisfy


$$
f(\widehat H)=0,\qquad f(\widehat v)=1.
$$



The physical inverse costs $3^{-4}$. Its cross blocks are in $3^5M$, so its displacement is in $3M$ and its matrix return is in $3^6M$.

This is the already established endpoint-adapted complement lemma applied to the now-validated original hypotheses. It is not a new general elimination theorem.

### 8.3 Evaluation of the actual first annihilator operator

Let $\mathsf N$ be the $\delta\times(\delta-1)$ adjacent-sum matrix with columns


$$
e_u+e_{u+1}.
$$


Both the exact endpoint correction (8.4) and the complement return (8.6) are invisible at physical order $3^5$. Indeed, on the full radical the matrix starts at $3^5$, and the endpoint correction is a multiple of $3$; its linear effect begins at $3^6$.

Using the actual/common-frame transfer and (7.3),


$$
\frac{\widehat H^TT\widehat H}{3^5}
\equiv-\mathsf N^T\mathsf D\mathsf N\pmod3.
$$


Entrywise,


$$
(\mathsf N^T\mathsf D\mathsf N)_{uv}
=\mathsf D_{uv}+2\mathsf D_{u,v+1}+\mathsf D_{u+1,v+1}.
$$


Therefore


$$
\boxed{
\frac{\widehat H^TT\widehat H}{3^5}
\equiv
-\left(
[y^{\kappa_1-u-v}](1-y)^{2\chi}(1+y)^2
\right)_{0\le u,v\le\delta-2}
\pmod3.
}
\tag{8.7}
$$



The sign is negative, and the factor is $(1+y)^2$, not an independently selected model.

Every entry has an immediate digit evaluation. For


$$
k=\kappa_1-u-v,\qquad 2\chi=243c,
$$


the entry is zero unless


$$
k=243m+d,\qquad d\in\{0,1,2\},\qquad0\le m\le c.
$$


In the latter case it equals


$$
-\epsilon_d(-1)^m\prod_i\binom{c_i}{m_i},
\qquad
(\epsilon_0,\epsilon_1,\epsilon_2)=(1,2,1),
\tag{8.8}
$$


where $c_i,m_i$ are ternary digits. In particular, it vanishes unless


$$
u+v\equiv119,\ 120,\ 121\pmod{243}.
$$



The lowest actual forcing in this same frame is also protected:


$$
\frac{\widehat H^TT\widehat v}{3^5}
\equiv
-\sigma^{-1}\mathsf N^T\mathsf D e_0\pmod3.
\tag{8.9}
$$


Its $u$-th coordinate is the negative signed coefficient of


$$
(1-y)^{2\chi}(1+y)
$$


at $\kappa_1-u$, multiplied by $\sigma^{-1}$. This identifies the direction needed for the next payment; it does not classify its behavior on the second radical.

---

## 9. Why the separately adapted $3^6$ digit can depend on the higher endpoint

This question must be kept separate from the accepted raw/common-frame matrix comparison.

### 9.1 An explicit formula including the complement return

Work before the latest complement elimination, in the fixed basis


$$
[E_{\mathcal C},\mathscr G].
$$


Define


$$
A=E_{\mathcal C}^TKE_{\mathcal C},
\qquad
C_1=\frac{E_{\mathcal C}^TK\mathscr G}{3},
$$




$$
M=\frac{\mathscr G^TT\mathscr G}{3^5}.
$$


These are integral, $A$ is a unit matrix, and


$$
\overline M=-\mathsf D=:M_0.
$$



Let


$$
e=f(E_{\mathcal C}),\qquad
u_0=f(g_{L_*}),\qquad
v_0=\frac{e_0}{u_0},
$$


where $v_0$ is the coordinate vector of $v$ in the $\mathscr G$-basis. Define the actual higher endpoint vector


$$
t=\frac{f(\mathscr G\mathsf N)}3
=\left(\frac{f(h_u)}3\right)_u.
\tag{9.1}
$$


It is integral, but its reduction has not been supplied by the lowest H2 endpoint.

The adapted radical columns are


$$
\mathscr G(\mathsf N-3v_0t^T),
$$


and the adapted complement is


$$
V=E_{\mathcal C}-\mathscr Gv_0e^T.
$$



Modulo $3$, the divided cross block is


$$
Q_f
=\left(\overline C_1-\overline e\,\overline v_0^{\,T}M_0\right)\overline{\mathsf N}.
\tag{9.2}
$$


The returned annihilator matrix satisfies the following modulo-$9$ identity after division by $3^5$:


$$
\boxed{
\begin{aligned}
\frac{S_{\mathrm{ann}}}{3^5}
\equiv{}&
\mathsf N^TM\mathsf N\\
&-3\left(
t\,\overline v_0^{\,T}M_0\mathsf N
+\mathsf N^TM_0\overline v_0\,t^T
+Q_f^T\overline A^{-1}Q_f
\right)
\pmod9.
\end{aligned}}
\tag{9.3}
$$



To check the powers:

* endpoint adaptation contributes a linear term $3t$ against the physical radical block $3^5M$, hence order $3^6$;
* its quadratic term starts at $3^7$;
* the adapted complement cross is $3^5Q_f$;
* the physical complement inverse is $3^{-4}\overline A^{-1}$;
* its matrix return therefore starts at $3^6$.

Thus the $3^5$ digit is protected, while all terms displayed on the second line of (9.3) are potentially active at $3^6$.

### 9.2 Exact criterion for higher-endpoint dependence

Set


$$
r_0=\mathsf N^TM_0\overline v_0.
$$


The endpoint-dependent part of the $3^6$ digit is


$$
-\bigl(t r_0^T+r_0t^T\bigr).
\tag{9.4}
$$



Accordingly:

* if $r_0=0$, this particular higher-endpoint dependence vanishes;
* if $r_0\ne0$, changing the higher endpoint generally changes the separately adapted $3^6$ matrix;
* on a second-radical subspace with coefficient matrix $Z_2$, the dependence is exactly
  

$$
-\left(
  (Z_2^Tt)(Z_2^Tr_0)^T+
  (Z_2^Tr_0)(Z_2^Tt)^T
  \right).
  \tag{9.5}
$$


  It disappears there if $Z_2^Tr_0=0$.

This is the precise interface with A1’s separate rank/kernel/direction classification. It would be incorrect either to declare universal $3^6$ protection or to declare universal dependence without checking that direction.

Even when two raw common-frame matrices agree modulo $3^7$, their separately endpoint-adapted matrices need not agree modulo $3^7$: the adaptation matrices can differ by $3$, and they act on a block beginning at $3^5$.

No defect in the accepted raw/common-basis comparison is implied.

---

## 10. Complete border, diagonal, and forcing: nothing already returned is erased

### 10.1 The complete retained diagonal

The original actual prefix quantities remain


$$
f^{\mathrm{pref}}
=e_R-\mathsf B^T\mathsf A^{-1}e_C,
$$




$$
\lambda^{\mathrm{pref}}
=3^{26}d_{\mathrm{act}}-e_C^T\mathsf A^{-1}e_C.
$$



The accepted original premise makes $\lambda^{\mathrm{pref}}$ integral. The full subsequent returns are


$$
f^{(2)}=f_K-3L_{\mathrm{act}}B_{\mathrm{act}}^{-1}f_J,
$$




$$
\lambda^{(2)}
=\lambda^{\mathrm{pref}}
-\frac13f_J^TB_{\mathrm{act}}^{-1}f_J,
$$




$$
f=f_{\mathrm{act,new}}
=f_R-3M_{b,\mathrm{act}}^TA_{b,\mathrm{act}}^{-1}f_b,
$$




$$
\boxed{
\lambda_{\mathrm{new}}
=\lambda^{(2)}
-\frac19f_b^TA_{b,\mathrm{act}}^{-1}f_b.
}
\tag{10.1}
$$



The old actual theorem evaluates


$$
v_3(\lambda^{(2)})=-1.
$$


It does not, merely by itself, evaluate the unadapted $\lambda_{\mathrm{new}}$.

Since $f_b$ is integral and the normalized rank-$b$ inverse is integral, one does at least have the paid bound


$$
\lambda_{\mathrm{new}}\in3^{-2}\mathbb Z_3.
\tag{10.2}
$$



To assert $\lambda_{\mathrm{new}}=\eta/3$ with $\eta$ a unit in this particular retained frame requires the appropriate quadratic residue in (10.1). It is not supplied by the matrix audit.

### 10.2 Zero new diagonal return from the adapted complement

The complement $V$ in (8.5) lies in the exact endpoint kernel. Its elimination therefore makes:

* no new endpoint Schur correction;
* no new complete-diagonal Schur correction.

In particular it preserves the **entire** $\lambda_{\mathrm{new}}$ of (10.1), including its already incurred $1/3$ and $1/9$ terms.

This must not be confused with eliminating the unadapted monomial complement. The latter gives


$$
\lambda_{\mathrm{rad}}
=\lambda_{\mathrm{new}}
-\frac1{81}f_C^TA^{-1}f_C,
$$


and that term cannot be dropped. Nor may the diagonal from that unadapted frame be inserted into the matrix from the endpoint-first frame without the corresponding exact transformation.

### 10.3 The complete remaining border

After the adapted complement elimination, the retained border is


$$
\begin{pmatrix}
\lambda_{\mathrm{new}}&1&0\\
1&a^\circ&(r^\circ)^T\\
0&r^\circ&S_{\mathrm{ann}}
\end{pmatrix},
\tag{10.3}
$$


where


$$
a^\circ,\ r^\circ,\ S_{\mathrm{ann}}\in3^5M.
$$



The exact two-coordinate return is


$$
\boxed{
S^\sharp
=S_{\mathrm{ann}}
+\frac{\lambda_{\mathrm{new}}}{1-\lambda_{\mathrm{new}}a^\circ}
\,r^\circ(r^\circ)^T.
}
\tag{10.4}
$$


By (10.2),


$$
1-\lambda_{\mathrm{new}}a^\circ\in1+3^3\mathbb Z_3
$$


is a unit, and the correction in (10.4) lies in $3^8M$.

Thus, in this exact endpoint-first frame, the complete bordered two-coordinate return cannot alter either physical digit $3^5$ or $3^6$. This conclusion retains the whole diagonal; it does not require its unit residue to have been evaluated.

When a separately paid normalization $\lambda=\eta/3$ is available, (10.4) reduces to the previously retained $B^\sharp$ formula. That stronger normalization is not inferred here from matrix information.

---

## 11. Audit ledger

| A1 Turn 6 assertion or proposed use | Verdict | Reason or qualification |
|---|---|---|
| Original divisibility of $\chi$ and strengthened support gap | **PASS** | Section 2 derives the exact positive residues modulo $243$ |
| Same $p=17$ compression through $3^{32}$ | **PASS** | New $h-6$ active layer included; inactive terms start at $32$ |
| Stationary, logarithmic, and physical-cutoff payments | **PASS** | No trial or completed macro term crosses the original boundary |
| Complete new pole list | **PASS** | Includes $Q/9$, both weighted cancellations, $3y$, middle and low terms |
| Signed units $1,2,1$ at the new $P$-bands | **PASS** | Exact bounded factorial-unit verification |
| Modulo-$9$ Frobenius $P/3$ band | **PASS** | Sign $-6/3=-2\equiv1$ gives $+\mathsf D$ in the pairing |
| Prefix matrix formula modulo $9$ | **PASS** | The $9Q$ contribution is $-3\beta A_0$ in $\mathsf A$ |
| Prefix proof from support alone | **Insufficient as a standalone inference** | Anti-diagonal constancy is also needed; compression supplies it, as proved in Section 5 |
| Full contracted prefix return in $9M$ | **PASS** | Base, both cross terms, $A_-$, and $A_+$ are all evaluated |
| Interior $J$-couplings and finite interior inverse | **PASS** | Admitted degrees and exact finite ranges checked |
| Last-middle bordering identity | **PASS** | Actual boundary entries retained; no extrapolated compression |
| Quadratic $J$-return zero at $3^5$ | **PASS** | Bilinear finite bordering plus the interval $b<k<Q$ |
| Using that zero to evaluate the endpoint return | **FALSE** | Equation (6.13) retains the last coupling |
| Assembly of the matrix digit $-\mathsf D$ | **PASS** | Prefix, $J$, rank-$b$, and physical $3^{-4}$ returns all paid |
| Ranges I–III ranks, primitive syzygy completeness, saturated complements | **PASS** | Exact graded degrees and finite target interval checked |
| Treating the lowest actual endpoint as open | **FALSE** | Already evaluated by original H2, equation (8.3) |
| Actual first annihilator operator with $(1+y)^2$ | **PASS** | Derived from the complete returned actual matrix and exact endpoint lift |
| Universal protection of a separately adapted $3^6$ digit | **FALSE** | Higher endpoint term (9.4) can be active |
| $3^6$ protection on a specified second radical | **CONDITIONAL** | Requires the exact direction test in (9.5), or the corresponding higher endpoint values |
| Unit normalization of the retained unadapted $\lambda_{\mathrm{new}}$ | **CONDITIONAL** | Requires the actual quadratic residue in (10.1) |
| Primitive-$q$ or whole-error gain from these matrix ranks | **Not established** | Final contents, all-prime gcd, nonvanishing and real-size comparison remain separate |

---

## 12. Complete producer and global arithmetic normalization remain unchanged

The actual producer is still


$$
Q_{\mathrm{act}}=3P_n=Q_c+3^7\mathscr R,
$$




$$
3^7\mathscr R=\sum_{a=0}^{A+1}e_ax^a,
\qquad
e_a=-\frac{(A+1)!}{a!}(t_a+\xi v_a),
$$


with the complete forcing


$$
t=
3nh_{\mathrm{vec}}
+(b_{\mathrm{force}}+6)e_{n-1}
+\frac{2b_{\mathrm{force}}}{n-1}e_{n-2},
\qquad
b_{\mathrm{force}}=-n-66.
\tag{12.1}
$$


The signed paid $\xi$, both terminal forcing coordinates, and the entire $t+\xi v$ remain present. Also retained are


$$
\mathscr R(-1)
=-\frac{\xi((A+1)!)^2}{3^7},
$$




$$
J^T\varepsilon+\omega
=-\varepsilon-s_{\mathrm{ret}}
\left(\theta e_{\nu-1}+3^{26}b^{\langle26\rangle}\right).
\tag{12.2}
$$



The complete-source recurrence remains


$$
\mu_{t+1}+\mu_t
=
\frac{3^h}{2t+1}
-\frac{3^h}{4}\bigl((2t+2)!+(2t)!\bigr),
\qquad0\le t\le2n-2,
$$


with its genuine resonance divisor at


$$
t_*=\frac{3^h-5}{2}.
$$


No local matrix calculation removes that divisor.

All local unit inverses and adapted bases are $3$-adic operations inside the original finite spaces. They do not redefine the actual integer column contents or the actual least simultaneous clearer $\ell_{\mathrm{clr}}$.

Retain


$$
A_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\mathrm{clr}}^{m+1}\beta_1,
$$


and the gcd over **all primes**


$$
g_\ell=\gcd(|A_\ell|,|B_\ell|).
$$


For $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell}.
$$


The whole error is exactly


$$
\boxed{
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\mathrm{clr}}^{m+1}}
{g_\ell}\det H_{\mathrm{complete}}.
}
\tag{12.3}
$$



An irrationality proof still requires, at the **same infinite original indices**,


$$
B_\ell\ne0,\qquad \det H_{\mathrm{complete}}\ne0,
$$


and


$$
\boxed{
\log g_\ell-(m+1)\log\ell_{\mathrm{clr}}
-\log|\det H_{\mathrm{complete}}|
\longrightarrow+\infty.
}
\tag{12.4}
$$


Under those hypotheses the nonzero whole error would tend to zero, contradicting rationality. The present report proves none of these final nonvanishing or decay conditions.

In particular, determinant factors associated with growing radicals may occur in both distinguished cofactors and disappear in the final primitive quotient.

---

## 13. Exact next original proof obligation and bounded arithmetic receipt

### 13.1 The next local obligation

The first divided actual annihilator matrix is now evaluated. The next obligation is not the lowest endpoint and not the already paid common-frame transfer.

A precise continuation lemma is:

> **Actual second-radical matrix-and-direction lemma.**  
> On the same original indices, use the complete returned endpoint and forcing to evaluate
> 

$$
> t_u=\frac{f_{\mathrm{act,new}}(h_u)}3\pmod3
>
$$


> in the specified endpoint-first frame, together with the physical $3^6$ matrix terms in (9.3). Restrict the result and the returned forcing to the complete radical of (8.7), using its proved finite complement. Evaluate the complement’s directional return, and establish the required Smith-direction divisibilities at that same original index.

The core terms becoming active at this next matrix digit include


$$
\frac{\mathscr G^TZ^T\mathsf A Z\mathscr G}{9}\pmod3,
\qquad
\frac{\mathscr L^TB_c^{-1}\mathscr L}{3}\pmod3,
$$




$$
\left(\frac{M_{b,c}\mathscr G}{3}\right)^T
A_{b,c}^{-1}
\left(\frac{M_{b,c}\mathscr G}{3}\right)\pmod3,
\qquad
C_1^TA_c^{-1}C_1\pmod3,
\tag{13.1}
$$


as well as the moment pairing through modulus $3^{33}$.

Their vanishing at the preceding digit does not evaluate them now.

If $Z_2$ spans the complete radical of (8.7), a unit complement at physical order $3^5$ has inverse cost $3^{-5}$, radical cross in $3^6M$, and matrix return in $3^7M$. Its **directional** return can already be active at $3^6$, because the complementary forcing begins at $3^5$. That payment must be retained.

The exact endpoint sensitivity on this second radical is already isolated in (9.5). A1’s direction classification can determine when that sensitivity vanishes; otherwise A4’s higher actual endpoint calculation is genuinely needed.

### 13.2 Bounded exact arithmetic

No tool computation was performed. No dense original matrix calculation, old $\binom{90}{40}$ table, terminal constant, or previously closed determinant is requested again.

The optional finite receipt for the new signed units has bounded inputs


$$
270,\ 118,\ 119,\ 121,\ 149,\ 151,\ 152,\ 30,\ 13,\ 17.
$$


For each, calculate the finite Legendre sum and factorial unit modulo $3$. The expected outputs are


$$
\begin{array}{c|r|c}
n&v_3(n!)&n!/3^{v_3(n!)}\pmod3\\ \hline
270&134&1\\
118&57&2\\
119&57&1\\
121&58&1\\
149&71&2\\
151&72&1\\
152&72&2\\
30&14&1\\
13&5&2\\
17&6&1
\end{array}
$$


and hence


$$
\binom{270}{118}\equiv243\pmod{729},
$$




$$
\binom{270}{119}\equiv243\pmod{729},
$$




$$
\binom{270}{121}\equiv486\pmod{729},
\qquad
\binom{30}{13}\equiv54\pmod{81}.
$$



These follow symbolically from


$$
\frac{n!}{3^{v_3(n!)}}
\equiv(-1)^{v_3(n!)}\prod_i n_i!\pmod3.
$$


A coordinator-authored check needs only a bounded factorial-unit pass through $1,\ldots,270$, or the displayed Legendre and ternary-digit computations.

After coefficient signs are inserted, the outputs are precisely the new units $1,2,1$ and the interior $J$-unit $1$. This finite receipt verifies only those universal constants. The original-index matrix theorem rests on the uniform proofs above.

---

## Conclusion

The independent audit closes the precision-$32$ **matrix** calculation at its stated scope. In particular:

1. the same $p=17$ compression includes the new $h-6$ denominator layer without boundary or stationary-error debt;
2. the complete new pole layers and signed cancellations are valid;
3. every contracted second-prefix term is evaluated, including the finite inverse corrections;
4. the actual last middle $J$-column is retained, and its quadratic invisibility at $3^5$ is proved without an endpoint extrapolation;
5. the rank-$b$ and physical $3^{-4}$ returns leave the digit $-\mathsf D$ unchanged;
6. the Ranges I–III rank and saturated-complement statements are valid.

Using the accepted actual/common-matrix transfer and the **already solved** actual H2 endpoint, the new actual conclusion is


$$
\boxed{
\frac{S_{\mathrm{ann}}}{3^5}
\equiv
-\left(
[y^{(P/3-1)/2-u-v}](1-y)^{2\chi}(1+y)^2
\right)_{0\le u,v\le\delta-2}
\pmod3.
}
$$



The exact endpoint-adapted complement makes no **new** diagonal return; it does not erase the prior $1/3$ and $1/9$ corrections. The separately adapted $3^6$ digit can depend on $f(h_u)/3$, with the precise dependence given in (9.4)–(9.5).

The remaining local bottleneck is the evaluated second-radical matrix **and its paid actual direction**, including the higher endpoint where that direction makes it relevant. The remaining global bottleneck is still same-index nonvanishing and decay of the whole error after the actual contents, least simultaneous clearer, all-prime gcd, and primitive denominator.



$$
\boxed{\text{The rationality or irrationality of }e+\pi\text{ remains unresolved.}}
$$


