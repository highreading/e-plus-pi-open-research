> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 — actual all-pole assembly and a vanishing theorem for the next radical

The proposed pole assembly needs one correction: its factorial functional is **not** the derangement functional $\mu$ defined in the original construction. After correcting that term, I obtain an explicit evaluation of the next radical form on $\mathcal J^\dagger$.

In particular, on a smaller, still infinite subclass, that entire next radical form is zero modulo $3$. This is an exact rank theorem—rank zero—not an inverse criterion or an extrapolation from $n=65$. It supplies stronger actual distinguished-cofactor divisibility, but also shows that this subclass requires another saturation level.

The analytic source gap can now be closed for the actual map. A3’s same-$N$ selectors pass within their stated dependency scope; their conclusions concern selected subsequences, not all prescribed centers.

## 1. Corrected exact pole assembly

Distinguish the two integral functionals


$$
\mu(y^s)=D_{2s},
\qquad
\mathfrak f(y^s)=(2s)!.
$$


Only $\mathfrak f$ occurs in the rational exponential endpoint term.

For an integral $3$-adic polynomial $F$, write


$$
C_F(y)=\frac{F(y)-F(-1)}{y+1}.
$$


Polynomial division gives


$$
4\int_0^1\frac{F(x^2)}{1+x^2}\,dx
=\pi F(-1)+4\sum_{v\ge0}\frac{[y^v]C_F}{2v+1}.
$$


Thus the complete rational functional is


$$
-\mathfrak f(F)+4\sum_{v\ge0}\frac{[y^v]C_F}{2v+1}.
\tag{1}
$$



Take


$$
F_{ij}=Q^{\rm loc}f_if_j,\qquad
U=4\ell/3^h.
$$


If $T$ denotes $\ell$ times the rational matrix formed using $Q^{\rm loc}$, then exactly


$$
\boxed{
\frac{T_{ij}}U
=-\frac{3^h}{4}\mathfrak f(F_{ij})
+\sum_{r=0}^{h}
\ \sum_{\substack{a\ge1\ {\rm odd}\\3\nmid a\\a3^r\le4n-3}}
3^{h-r}a^{-1}
[y^{(a3^r-1)/2}]C_{F_{ij}}.
}
\tag{2}
$$


Here $a^{-1}$ is its exact rational inverse, a $3$-adic unit—not merely a chosen residue representative.

Indeed,


$$
\deg F_{ij}\le n+2(k-1)=2n-1,
$$


so $\deg C_{F_{ij}}\le2n-2$. The greatest possible odd denominator is consequently $4n-3$, exactly as proposed.

Equation (2) lies in $\mathbb Z_3$. Its factorial contribution has valuation at least $h$, because $\mathfrak f(F_{ij})\in\mathbb Z_3$. After the LOW division by $3$, it vanishes modulo $9$ whenever $h\ge3$, in particular throughout the specified $h\ge5$ domain.

**Normalization qualification.** If $T$ instead uses the actual primitive integer polynomial


$$
Q_n=\lambda Q^{\rm loc},\qquad \lambda=L_n/3\in\mathbb Z_3^\times,
$$


then the right side of (2) must also be multiplied by $\lambda$. This does not change ranks or valuations, but it changes literal residue entries and must not be silently discarded.

## 2. The first actual LOW matrix modulo $9$

Use the parameters from $\mathcal J^\dagger$, and abbreviate


$$
A=n-2,\quad H=3^{h-1},\quad D=H-A=t\delta,
$$




$$
d=\frac{3D}{2}-1,\qquad
m=\frac{A+1}{2},\qquad
\nu=\frac D2-1.
\tag{3}
$$


Thus $d=D+\nu$, and on $\mathcal J^\dagger$


$$
0<D<H/6.
\tag{4}
$$



For the calculation choose the monomial LOW basis $1,y,\ldots,y^{d-1}$, and HIGH basis $y^d,\ldots,y^m$. This is equivalent to the endpoint-adapted basis by an integral unimodular change.

Put


$$
r_1=\frac{H-1}{2},\qquad
r_{\rm top}=\frac{3H-1}{2},\qquad
r_a=\frac{aH/3-1}{2}.
$$


Using the supplied, proved congruence


$$
Q^{\rm loc}\equiv(y+1)(y-1)^A(3y+1)\pmod9,
$$


equation (2) gives


$$
\boxed{
S_{ij}\equiv
[y^{r_1}](y-1)^A(3y+1)f_if_j
+3\sum_{\substack{a\ {\rm odd},\ 3\nmid a\\aH/3\le4n-3}}
a^{-1}[y^{r_a}](y-1)^Af_if_j
-3(\bar X\bar E^{-1}\bar X^T)_{ij}
\pmod9.
}
\tag{5}
$$


Here


$$
\bar E_{ij}=[y^{r_{\rm top}}](y-1)^Ay^{i+j},
\quad d\le i,j\le m,
\tag{6}
$$


and


$$
\bar X_{ij}=[y^{r_1}](y-1)^Ay^{i+j}
+\mathbf1_{i=d-1,\ j=m}.
\tag{7}
$$



The endpoint subtraction is retained in (2); passing to (5) uses the supplied deep endpoint valuation on this family. It is not an additional omitted rational term.

The surviving $h-2$ pole units are precisely


$$
a=1,5,7,\quad\text{and possibly }11.
$$


The highest LOW–HIGH pole gives exactly the corner in (7), since


$$
\operatorname{lc}(Q^{\rm loc})/3=1.
$$


Thus, apart from replacing $\mu$ by $\mathfrak f$, the coordinator’s first-LOW formula passes.

## 3. An explicit radical lift

The recurrence radical has a particularly convenient integral lift:


$$
\boxed{
z_i(y)=y^i(y-1)^D,\qquad 0\le i<\nu.
}
\tag{8}
$$


These are equivalent modulo $3$ to the step-$t$ recurrence polynomials


$$
y^i(y^t-1)^\delta,
$$


because $t$ is a power of $3$.

Their leading terms have degrees $D+i$, so adjoining $1,y,\ldots,y^{D-1}$ gives a unimodular basis of the LOW space. The known first residue rank is $D$, hence these $\nu$ independent radical vectors constitute its entire radical.

Let $Z$ be their coefficient matrix. The next divided radical residue is


$$
\bar W=\frac{Z^TSZ}{3}\pmod3.
\tag{9}
$$


The correction from eliminating the first residue-unit block vanishes in (9): its mixed entries are divisible by $3$, so their quadratic Schur correction is divisible by $9$.

The already present HIGH-block correction in (5), however, must first be contracted. The following calculation does that explicitly.

### 3.1 The HIGH-block correction vanishes after radical contraction

In characteristic $3$,


$$
(y-1)^Az_i=y^i(y-1)^H=y^i(y^H-1).
$$


For $j\le m$ and $i<\nu$,


$$
i+j\le\nu-1+m=\frac{H-3}{2}<r_1.
$$


Therefore the coefficient part of $Z^T\bar X$ vanishes. Only its corner remains:


$$
Z^T\bar X=e_{\nu-1}e_m^T.
\tag{10}
$$



Also


$$
d+m=r_{\rm top}-A.
$$


Consequently $\bar E_{ij}=0$ when $i+j<d+m$, and its anti-diagonal entries are $1$. Its inverse has zero entries when $i+j>d+m$. In particular,


$$
(\bar E^{-1})_{mm}=0,
\tag{11}
$$


since the HIGH block has more than one coordinate.

Combining (10)–(11),


$$
\boxed{
Z^T\bar X\bar E^{-1}\bar X^TZ=0.
}
\tag{12}
$$


This is a proved cancellation of the actual first HIGH Schur correction, not a decision to omit it.

### 3.2 The next pole level cancels after contraction

Modulo $3$,


$$
(y-1)^Az_iz_j
=y^{i+j}(y^H-1)(y-1)^D.
\tag{13}
$$


The two potentially contributing poles are $a=1$ and $a=7$, whose coefficient indices differ by exactly $H$. Both are always admissible on $\mathcal J^\dagger$, and


$$
1^{-1}=7^{-1}=1\pmod3.
$$


Their contributions in (13) have opposite signs and cancel.

The $a=5$ and possible $a=11$ indices lie outside both coefficient ranges in (13), because


$$
\deg\bigl(y^{i+j}(y-1)^D\bigr)\le2D-4<H/3.
$$


Thus


$$
\boxed{
\sum_a a^{-1}
[y^{r_a}](y-1)^Az_iz_j=0\pmod3.
}
\tag{14}
$$



## 4. Evaluated next radical form

The preceding cancellations leave only the first term of (5). For every positive power $H$ of $3$,


$$
(y-1)^H
\equiv y^H-1+3y^{H/3}-3y^{2H/3}\pmod9.
\tag{15}
$$


For example, this follows by induction from cubing the corresponding formula for $H/3$; the terms carrying an existing factor $3$ disappear on cubing modulo $9$.

Set


$$
r_2=\frac{H/3-1}{2}.
$$


Using (4), the coefficient range relevant to $r_1-i-j$ excludes the $-1$, $y^{2H/3}$, and $y^H$ terms in (15), including the low-degree contribution from multiplication by $3y$. Hence


$$
\boxed{
\bar W_{ij}
=[y^{r_2-i-j}](y-1)^D
\quad\text{in }\mathbb F_3,
\qquad 0\le i,j<\nu.
}
\tag{16}
$$



This evaluates $Z^TSZ/3\bmod3$ for the actual all-pole matrix on all of $\mathcal J^\dagger$. It is not obtained by treating an arbitrary binomial representative of $\bar S$ as its actual lift: equations (12) and (14) account for the extra terms in that lift.

The endpoint projection is equally explicit:


$$
z_i(-1)=(-1)^i(-2)^D\equiv(-1)^i\pmod3.
$$


Thus


$$
\boxed{
\bar e_Z=(1,-1,\ldots,(-1)^{\nu-1})^T\ne0.
}
\tag{17}
$$



## 5. An infinite subclass with exact next rank zero

Define


$$
\boxed{
\mathcal J^{\ddagger}
=\{j\in\mathcal J^\dagger:H/A<12/11\}.
}
\tag{18}
$$


This is infinite by the same irrational-rotation argument used to establish infinitude of $\mathcal J^\dagger$: restrict the ratio of the next power of $3$ to $4^j-1$ to any closed interval strictly inside $(1,12/11)$, with $3\mid j$.

On this subclass,


$$
D=H-A<H/12.
$$


Since


$$
i+j+D\le2D-4
$$


and


$$
r_2=(H/3-1)/2>2D-4,
$$


every coefficient in (16) is zero. Therefore


$$
\boxed{
\operatorname{rank}_{\mathbb F_3}\bar W=0
\qquad(j\in\mathcal J^{\ddagger}).
}
\tag{19}
$$


The endpoint projection (17) remains nonzero on this entire radical.

### Actual cofactor consequences

After elimination of the $D$-dimensional first unit block, the remaining $\nu$-dimensional block is divisible by $9$, not merely by $3$. Hence, for the actual LOW matrix,


$$
\boxed{
v_3(\det S)\ge2\nu=D-2,
\qquad
v_3\!\left(\operatorname{adj}(S)_{00}\right)
\ge2\nu-2=D-4.
}
\tag{20}
$$


The latter follows because every $(d-1)$-minor contains at least $\nu-1$ nonunit Smith factors, each now of valuation at least $2$. It applies after the unimodular endpoint-basis change as well.

Using the supplied normalization formulas, this strengthens the actual final-gcd lower bound to


$$
\boxed{
v_3(g)\ge d+2\nu=\frac{5D}{2}-3
\qquad(j\in\mathcal J^{\ddagger}).
}
\tag{21}
$$


These are lower bounds, not exact depths. In particular, one cannot subtract them to determine $v_3(q)$.

## 6. Analytic audit with the now-supplied original map

The actual map is


$$
T=v_1v_2u(y),\qquad
v_i=-1-\sqrt2\cos\theta_i,\qquad
u(y)=-\frac2{1+\sqrt2\cosh y}.
\tag{22}
$$


The five weights follow by expanding


$$
u(k+1)^3(kF+G)-2(k+1)^2((k+1)B+D_0).
$$


This reproduces all five rows of A3’s weight table. Although the quotient notation $q=w_1/w_0$, $h=w_2/w_0$ is convenient locally, the global weighted expressions must be read after multiplying by $w_0(v_1)w_0(v_2)$; they then have no artificial quotient singularities.

### Properness and critical values

On any compact interval of nonzero $T$-values, $|u(y)|$ is bounded below because $|v_i|\le M$; hence $y$ is bounded. Neither circle factor can approach zero. This proves properness over such intervals within either fixed sign component.

At a nonzero critical point, differentiation of (22) requires


$$
\sin\theta_1=\sin\theta_2=0,\qquad y=0.
$$


The possible nonzero critical values are therefore exactly


$$
-2M,\qquad -2\rho^3,\qquad 2\rho.
$$


On the $--$ component the only one is $-2M$. Thus the actual $--$ densities are analytic throughout $(-2M,0)$, using an even extension in $y$ at its boundary. This closes the previously identified global-map gap.

### Local $B_3$

Expanding (22) gives the supplied quartic $Q_4$. Expanding the actual multiplied weights gives


$$
L_2=\frac{\sqrt2-2}{2}(\theta_1^2+\theta_2^2)
-\frac{\sqrt2}{2M}y^2,
$$


and


$$
A_3=A+6(\theta_1^2+\theta_2^2)-\sqrt2\,y^2+O(R^4).
$$


The spherical averages therefore give exactly


$$
B_3
=A\left(\frac{8\sqrt2-15}{24\sqrt2}+\frac1{3M}\right)
+2\sqrt2-\frac13.
$$


Thus the local coefficient now passes from the original map and weights, rather than only from its previously quoted expansion.

### A3 turn 11 selector

The selector argument passes:

* interior integration by parts acts on the entire kernel and leaves the amplitude independent of rounding;
* at an odd-order amplitude zero, the first relevant even coefficient is affine in $\beta$ with nonzero slope;
* the two same-$N$ rounding parameters differ exactly by $1+c$;
* in a compact transition window, the corrected-profile difference is of order $n^{-1/2}$, while the retained remainder is $O(n^{-1})$.

Each candidate must retain its **own**


$$
g_i=\gcd(|L_N\mathcal H_{n_i,m_i}|,\,
         |L_N\mathcal J_{n_i,m_i}|),
\qquad
q_i=\frac{|L_N\mathcal J_{n_i,m_i}|}{g_i}.
$$


No gcd or valuation may be transferred between candidates. The conclusions outside the directly proved interior and transition regimes still depend on the other endpoint laws cited by A3; those laws are not newly proved here.

## 7. Final normalization and whole error

For the weighted determinant construction retain


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|),\qquad
q=\frac{|B_{\rm det}|}{g},\qquad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g.
$$


Where $B_{\rm det}\ne0$,


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_{\rm det})}{g}
\bigl(A_{\rm det}+B_{\rm det}(e+\pi)\bigr)
=\frac{\operatorname{sgn}(B_{\rm det})\ell^k}{g}
\det H_{\rm complete}.
}
$$


The arithmetic results above apply on $\mathcal J^\dagger$, with the stronger bounds on $\mathcal J^{\ddagger}$. They do not independently prove determinant-response nonvanishing or whole-error nonvanishing. Those remain dependent on the inherited regular-family results described in the sources.

For A3’s selected pairs, eventual whole-numerator nonvanishing follows from its audited selector estimates, and the exact primitive error remains


$$
q_i(e+\pi)-P_i
=q_i\,\frac{\mathcal Z_{n_i,m_i}}{\mathcal J_{n_i,m_i}}.
$$



## Closing ledger

### (1) New result and proof status

**Proved:**

* Corrected exact all-pole assembly (2), with the factorial functional $\mathfrak f$, complete cutoff, and scalar-unit qualification.
* Actual next radical evaluation (16), including explicit cancellation of both the HIGH Schur correction and the next pole level.
* Explicit endpoint projection (17).
* Exact next-radical rank zero on the infinite subclass $\mathcal J^{\ddagger}$.
* Stronger actual cofactor and final-gcd lower bounds (20)–(21).

**Audited from the newly supplied original formulas:** global properness, the nonzero critical-value list, the $--$-component continuation domain, local $B_3$, and A3’s same-$N$ selectors within their stated dependencies.

### (2) Exact remaining bottleneck

On $\mathcal J^{\ddagger}$, the next form is identically zero modulo $3$, so a unit theorem must move to the following saturation. That requires the actual matrix one digit deeper, including the modulo-$27$ polynomial core, the next pole level, and the now potentially surviving unit-block corrections. Endpoint nonzero projection alone does not determine its distinguished cofactor.

Neither these divisibility results nor the analytic selectors control the actual reduced denominators sufficiently to produce nonzero primitive errors tending to zero. Irrationality of $e+\pi$ remains undecided.

### (3) Computation request

None is required for the displayed infinite results. The next useful task is a symbolic all-pole expansion one saturation deeper on $\mathcal J^{\ddagger}$, rather than another finite rank scan.
