> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 — sixth-depth direct annihilation, an exact carry formula, and the critical-scale audit

## Verdict

On


$$
\boxed{
n=4^j+1,\qquad j>0,\qquad243\mid j,\qquad
0<D=H-(n-2)<H/8748,
}
\tag{1}
$$


I prove the requested **direct extended lower annihilation modulo $729$**, including a rectangle slightly larger than the one used at fifth depth. I also derive the complete sixth-carry expansion modulo $243$, with the LOW-unit correction retained inside $F$.

**I do not evaluate the sixth saturation.** The resulting formula isolates actual higher-digit contractions not evaluated by the supplied fifth proof. In particular, previous vanishing does not determine their next quotients.

The independent audit of A3turn19 finds that its third-derivative cumulant estimate and quartic stationary remainder are valid. Its scalar and whole-error conclusion passes **within its expressly stated prior contour and complete-residual interfaces**. I explain that dependency below rather than claiming a fresh proof of the exponential-force bounds.

No conclusion about irrationality of $e+\pi$ follows.

---

## 1. Parameters and complete functional

Use the actual monomial columns, with


$$
A=H-D=n-2,\qquad
d=\frac{3D}{2}-1,\qquad
\nu=\frac D2-1,\qquad
m=\frac{A+1}{2}.
$$


LOW is $0,\ldots,d-1$, HIGH is $d,\ldots,m$, and


$$
U=\langle1,y,\ldots,y^{D-1}\rangle,\qquad
z_i=y^i(y-1)^D,\quad0\le i<\nu.
$$


Write


$$
r_*=\frac{3H-1}{2},\qquad r_1=\frac{H-1}{2},
\qquad r_2=\frac{H/3-1}{2}.
$$



Strip only the primitive unit $\lambda=L_n/3$. At the precision supplied in the assignment,


$$
Q^{\rm loc}=(y+1)(y-1)^A(\beta+3y)+3^7R_0,
\qquad
\beta=-71-3M_0.
\tag{2}
$$


No digit of $\beta$ is discarded in the argument below.

The exact functional remains


$$
\mathcal M(F)=
-\frac{3^h}{4}\mathfrak f(F)
+\sum_{r=0}^{h}
\sum_{\substack{c\ge1\ {\rm odd}\\3\nmid c\\c3^r\le4n-3}}
3^{h-r}c^{-1}
[y^{(c3^r-1)/2}]
\frac{F(y)-F(-1)}{y+1},
\tag{3}
$$


where $\mathfrak f(y^s)=(2s)!$. In particular, the endpoint subtraction, factorial force, exact unit inverses, and cutoff are unchanged.

---

## 2. Proved: extended direct annihilation modulo $729$

Define


$$
w_i=y^i(y-1)^D,\qquad0\le i\le\nu+3.
$$


Then, for the lower functional obtained from (3) by the first LOW division,


$$
\boxed{
L_{\rm ext}(w_i,y^a)\equiv0\pmod{729},
\qquad
0\le i\le\nu+3,\quad0\le a\le d+3.
}
\tag{4}
$$



This is a rectangular statement, not merely a triangular collection of division tests.

### 2.1 Uniform shift margin

The largest shift before the linear core is


$$
i+a\le(\nu+3)+(d+3)=2D+4,
$$


and after it is at most $2D+5$. The required margin is


$$
4D+11<H/243.
\tag{5}
$$


Indeed, (1) gives $H/243>36D$, and $D\ge6$ makes (5) immediate.

### 2.2 Every surviving lower pole

At lower pole depth $t=0,\ldots,5$, after the first division by $3$, the weight is $3^t$, and its coefficient index is


$$
p_{c,t}=\frac{cH/3^t-1}{2}.
$$



Modulo $3^{6-t}$, the binomial polynomial $(y-1)^H$ has support only at multiples of


$$
G_t=\frac{H}{3^{5-t}}.
\tag{6}
$$


This follows directly from


$$
v_3\binom Hr=v_3(H)-v_3(r),\qquad0<r<H.
$$


The endpoint coefficients also lie on that grid.

Put $G=H/243$. Both $G_t$ and $H/3^t$ are odd integer multiples of $G$. Consequently every pole index $p_{c,t}$ is a half-grid point relative to the coarser covering grid $G\mathbb Z$: its distance from that grid is at least


$$
(G-1)/2.
$$


No nonnegative shift of size at most $2D+5$ reaches it, by (5).

This proves vanishing **term by term for every admissible unit $c$** at every contributing depth. Thus no pole-pair cancellation, and no assumption that the cutoff contains a missing partner, is needed for (4). Lower depths have weight divisible by $729$.

### 2.3 Top pole, factorial force, and endpoint-subtracted error

The degree of the endpoint-divided core in the largest test is at most


$$
A+1+2(d+3)=H+2D+5<r_*.
$$


Thus the top pole is absent for the core in every test in (4).

The factorial contribution after division has valuation at least $h-1$, which exceeds the required depth on (1).

For the error in (2), monic division gives


$$
\frac{3^7R(y)-3^7R(-1)}{y+1}\in3^7\mathbb Z_3[y].
$$


Every coefficient weight in (3) is integral over $\mathbb Z_3$. The first LOW division therefore leaves this entire error in $3^6\mathbb Z_3$. This also covers its possible top-pole contribution.

These observations prove (4) for the complete functional.

### 2.4 Consequences for extended projections

Monic division


$$
y^{d+s}=r_s(y)+(y-1)^Dq_s(y),
\quad
\deg r_s<D,\quad\deg q_s=\nu+s,
\qquad0\le s\le3,
$$


uses only indices covered by (4). Hence the exact LOW projection agrees modulo $729$ with the polynomial remainder projection.

In particular,


$$
\boxed{
F_{\{d,d+1,d+2,d+3\},\{d,d+1,d+2,d+3\}}
\equiv0\pmod{729},
}
\tag{7}
$$


and


$$
V_{d+s}\equiv0\pmod{729}\quad(0\le s\le3).
\tag{8}
$$


Here (7) uses the fact that the top representative and its actual top perturbation vanish by degree in this small corner.

Since both $-2ee_m^T$ and $K$ vanish in these columns,


$$
\boxed{Je_{d+s}\in81\mathbb Z_3^\nu,\qquad0\le s\le3.}
\tag{9}
$$



These are new sixth-precision statements; they do not evaluate the nonedge higher digits of $F$ and $J$.

---

## 3. LOW-force corrections are negligible before they are removed

Use


$$
B=U^TLZ,\qquad C=L_U^{-1}B,\qquad
\widetilde V=V-C^TX_U.
$$


The exact residual is


$$
\mathcal R=
Z^TLZ-B^TL_U^{-1}B
-3\widetilde V\widehat E^{-1}\widetilde V^T,
\qquad
\widehat E=E-3X_U^TL_U^{-1}X_U.
\tag{10}
$$


By (4),


$$
B,C,Z^TLZ\in729\mathbb Z_3.
$$


The first quadratic correction has valuation at least $12$, while replacing $\widetilde V$ by $V$ in the final term produces valuation at least $7$. Therefore


$$
\boxed{\mathcal R\equiv-3V\widehat E^{-1}V^T\pmod{729}.}
\tag{11}
$$


The LOW-unit correction *inside* $\widehat E$, however, is not negligible and remains present.

---

## 4. Proved bounded follow-on: the complete sixth-carry formula

Set


$$
R=E_0^{-1},\qquad \widehat E=E_0+3F,\qquad
V=-2ee_m^T+3K+9J,
\tag{12}
$$


all exactly. In particular $J$ contains every higher digit.

Write


$$
\operatorname{Sym}(e,v)=ev^T+ve^T.
$$


The inverse expansion is


$$
\widehat E^{-1}\equiv
\sum_{\ell=0}^{4}(-3)^\ell R(FR)^\ell\pmod{243}.
\tag{13}
$$



Direct multiplication, using $Re_m=e_d$, $R_{mm}=0$, and $Ke_d=0$, gives


$$
\boxed{
V\widehat E^{-1}V^T
\equiv-12F_{dd}ee^T+9A_9+27A_{27}+81A_{81}
\pmod{243},
}
\tag{14}
$$


where the completed fifth expressions are


$$
\begin{aligned}
A_9={}&KRK^T-2\operatorname{Sym}(e,Je_d)
 +2\operatorname{Sym}(e,KRFe_d)
 +4(FRF)_{dd}ee^T,\\
A_{27}={}&KRJ^T+JRK^T
 +2\operatorname{Sym}(e,JRFe_d)-KRFRK^T\\
&-2\operatorname{Sym}(e,KRFRFe_d)
 -4(FRFRF)_{dd}ee^T,
\end{aligned}
\tag{15}
$$


and the additional term is


$$
\boxed{
\begin{aligned}
A_{81}={}&JRJ^T
-KRFRJ^T-JRFRK^T
+KRFRFRK^T\\
&-2\operatorname{Sym}(e,JRFRFe_d)\\
&+2\operatorname{Sym}(e,KRFRFRFe_d)\\
&+4(FRFRFRF)_{dd}ee^T.
\end{aligned}}
\tag{16}
$$



For example, the last term comes from the fourth inverse term:


$$
81(-2ee_m^T)RFRFRFRFR(-2e_me^T)
=324(FRFRFRF)_{dd}ee^T.
$$


This verifies both its coefficient and its number of $F$-factors.

Equation (7) eliminates the first term in (14). Reusing the completed fifth divisibilities


$$
A_9\in9\mathbb Z_3^{\nu\times\nu},
\qquad
A_{27}\in3\mathbb Z_3^{\nu\times\nu},
$$


the sixth form is therefore


$$
\boxed{
T_6=\frac{\mathcal R}{243}
\equiv-
\left(\frac{A_9}{9}+\frac{A_{27}}3+A_{81}\right)\pmod3.
}
\tag{17}
$$



### Exact obstruction

The fifth proof does not evaluate


$$
A_9\bmod27,\qquad A_{27}\bmod9,\qquad A_{81}\bmod3.
\tag{18}
$$


In particular,


$$
A_9\equiv0\pmod9
\quad\not\Rightarrow\quad
A_9/9\equiv0\pmod3.
$$



The extended corner estimates (7)–(9) remove several edge terms, but do not determine every contraction in (18). New nonedge digits of the actual $F$ and $J$, including their LOW projections, are still required. I do not replace that calculation by a recurrence assertion.

The half-grid argument in Section 2 proves a direct-functional support lemma. It is **not** an all-depth theorem for closed HIGH contractions: inverse convolutions, finite HIGH truncations, and LOW projections require a separate precision-weighted support induction.

---

## 5. Independent audit of A3turn19

I reuse the already audited sharp virial moments and first two derivative estimates, rather than repeat their derivation.

### 5.1 Third derivative and complex cumulant: pass

At either positive anchor, put


$$
H_q=\sum_i(e^{-i\theta_i}+q)^{-1},\qquad
J_q=-\sum_i(e^{-i\theta_i}+q)^{-2}.
$$


Both statistics have real and imaginary parts with Lipschitz constant $O(\sqrt d)$. The principal measure has Hessian bounded below by $cnI$. Its concentration consequence gives


$$
\mathbb E|H_q-\mathbb EH_q|^r
=O((d/n)^{r/2}),\qquad r=2,3,
$$


and the analogous second-moment estimate for $J_q$.

This transfers correctly to the actual complex averages. Indeed, let


$$
Y=H_q-\mathbb EH_q,\qquad
\langle G\rangle_j=\frac{\mathbb E(W_jG)}{N_j},
$$


with $\|W_j\|_\infty=O(1)$ and $|N_j|\ge1/2$. Then


$$
\operatorname{Cum}_{3,j}(H_q)
=\langle Y^3\rangle_j
-3\langle Y^2\rangle_j\langle Y\rangle_j
+2\langle Y\rangle_j^3
=O((d/n)^{3/2}).
$$


Thus positivity of a complex covariance is neither needed nor asserted.

For the leading trace,


$$
\left|\left\langle2\sum_i h(\theta_i)^3-\frac{2d}{(1+q)^3}
\right\rangle_j\right|
\le C\mathbb E\sum_i|\theta_i|
\le C\sqrt{d\,\mathbb EQ}
=O(d^{3/2}/\sqrt n).
$$


This proves the claimed third-derivative error.

At $d\asymp n^{3/4}$, its largest contribution to the stationary value is


$$
\frac{d^3}{n^3}\frac{d^{3/2}}{\sqrt n}
=O(n^{-1/8})=o(1).
$$



### 5.2 Quartic coefficient and stationary remainder: pass

Summing the five displayed terms in A3’s table gives, in each column,


$$
C_4=\frac{-41+29\sqrt2}{192}.
$$


The coefficient errors are multiplied respectively by


$$
d/n,\qquad d^2/n^2,\qquad d^3/n^3,
$$


and tend to zero on the critical domain.

The fixed-neighborhood bounds $U^{(k)}=O(d)$ are compatible with the supplied actual zero-free interface: on a fixed disk around either anchor, one can choose a holomorphic logarithm; the partition comparisons bound its real-part variation by $O(d)$, and the usual interior holomorphic estimates give the derivative bounds on a smaller disk.

Consequently the unretained Taylor terms contribute


$$
O\!\left(n(d/n)^5\right)=O(d^5/n^4)=O(n^{-1/4}).
$$


There is also no missing order-one term from using


$$
r=1+x_1(d/n)+x_2(d/n)^2.
$$


Its stationary-equation residual is $O(n(d/n)^3)$, apart from the already controlled derivative errors. Correcting this displacement changes the stationary value by


$$
O(n(d/n)^6)=O(n^{-1/2}),
$$


again negligible.

### 5.3 Original scalar contours: compatible with the critical scale

The actual plus contour is closed; the minus contour is open and requires both connectors. For $d=O(n^{3/4})=o(n)$,

* the real stationary radii have displacement $O(d/n)$;
* scalar remote-arc losses have the form $e^{-cn+O(d)}$;
* the minus connectors have $h=O(d/n)$, versus a fixed positive saddle value;
* differentiated particle outer sectors retain exponential suppression, even after polynomial derivative factors;
* the local Gaussian curvature is $n\alpha_\pm+O(d)$.

Thus none of these contour margins degenerates at the critical scale. The original scalar normalization ratio is still $4\pi$, and the Gaussian ratio is $M^{-1}(1+o(1))$.

### 5.4 Complete residual: the stated interface is sufficient, but remains an input

The exact coordinate identity must remain


$$
c_j-(e+\pi)
=\frac{E_j}{P_j}
+(-1)^{n+1}\frac{F_j}{P_j}
+(-1)^n\delta_{j0}\frac{D}{P_j}.
\tag{19}
$$


The quoted bounds


$$
|E_j/P_j|\le\frac{e^{Cb}}{n!\sqrt n},
\qquad
|D/P_0|\le\frac{C\sqrt n\,e^{Cb}}{n!B_0}
$$


are sufficient: relative to $M^{-2n-b}$, their logarithms are


$$
-n\log n+O(n+b)\longrightarrow-\infty.
$$



The supplied documents do not independently expand all $eE_i$ needed to reprove these bounds from their defining exponential force. Accordingly, my audit conclusion is:



$$
\boxed{
c_W-(e+\pi)
=(-1)^{n+1}4\pi M^{-2n-b}(1+o(1))
}
\tag{20}
$$


passes on


$$
\kappa_0n^{3/4}\le b\le\kappa_1n^{3/4}
$$


**with A3’s stated complete-residual interface retained as an input**, uniformly for positive diagonal metrics in the actual coordinates. Eventual nonvanishing follows within precisely that scope. No $o(n^{4/5})$ extension is used.

---

## 6. Primitive normalization and arithmetic scope

### Weighted construction

Restore $\lambda=L_n/3$. It multiplies the residual form and hence multiplies (17) by that unit.

Because $T_6$ has not been evaluated, there is no new sixth Smith or gcd bound here. The established fifth bound remains


$$
v_3(g)\ge d+5\nu=4D-6
$$


under the supplied normalization identity.

Retain


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|),\qquad
q=\frac{|B_{\rm det}|}{g},\qquad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g.
$$


For $B_{\rm det}\ne0$, the whole real error is exactly


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_{\rm det})\ell^k}{g}
\det H_{\rm complete},
\qquad k=(n+1)/2.
}
\tag{21}
$$


The primitive multiplier is $\ell^k/g$. Neither its decay nor whole-error nonvanishing is proved by the direct annihilation lemma.

### Analytic actual-coordinate centers

For the actual cleared columns $N_B=d_B[u,v]$ and integral positive diagonal metric $\Omega$, retain


$$
A_B=N_{B,1}^T\Omega N_{B,1},\quad
H_B=N_{B,1}^T\Omega N_{B,2},\quad
g_B=\gcd(A_B,|H_B|),
$$




$$
q_B=A_B/g_B,\qquad p_B=H_B/g_B.
$$


The primitive multiplier is $d_B^2/g_B$, and within the audited analytic interfaces,


$$
\boxed{
q_B(e+\pi)-p_B
=(-1)^n4\pi q_BM^{-2n-b}(1+o(1))\ne0.
}
\tag{22}
$$


No weighted-family gcd estimate transfers to this different center.

---

## Closing ledger

### (1) New result and proof status

**Proved:**

* Complete direct $L_{\rm ext}$ annihilation modulo $729$ on (1), through $0\le i\le\nu+3$, $0\le a\le d+3$.
* Negligibility of the actual $Z^TLU$ corrections at sixth precision.
* Extended small-corner and coupling divisibilities (7)–(9).
* The complete sixth-carry identity (17), including every inverse term through $\ell=4$.

**Audited:** A3turn19’s third cumulant, quartic coefficient, stationary remainder, and compatibility with the original scalar contours. Its whole critical-scale theorem passes within its explicitly retained complete-residual interface.

**Not proved:** an evaluated $T_6$, a sixth rank, or an all-depth HIGH-contraction support theorem.

### (2) Exact remaining bottleneck

For the assigned sixth saturation, evaluate the actual quantities in (18), deriving the necessary nonedge $F/J$ digits from the complete pole functional and LOW projections.

For irrationality, the separate unresolved requirement is same-index control of the **actual reduced denominator after the final gcd**, together with nonzero whole primitive errors tending to zero. Neither result above supplies it.

### (3) Computation request

None. The next required step is a symbolic higher-digit support-and-coefficient calculation for (18); a finite rank scan would not settle its infinite-domain assertion.
