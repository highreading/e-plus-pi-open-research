> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## Verdict

On the unchanged ternary domain


$$
n=4^j+1,\qquad j>0,\qquad243\mid j,\qquad
0<D=H-(n-2)<H/8748,
$$


the new block definitions close the identification gap. I obtain the **actual identity**


$$
\boxed{Fp_i=-e_{r_2-i}+e_{r_2-i-1}\pmod3,\qquad0\le i<\nu,}
$$


and consequently


$$
\boxed{A_{81}=0\pmod3.}
$$


This is an evaluation of the assigned contribution, not of $T_6$: the two contributions assigned to A1 remain separate.

For the binary audit, the new large-kernel convolution, its negative Laurent boundary, and its paired modulo-$4$ units pass. In particular, the complete paired contribution to $(H-N)/16$ is zero on the original $r=18\bmod32$ domain. The full endpoint also passes. I do **not** certify the remaining even and odd coordinate calculations as independently checked: several new moment reductions in A5turn17 still require a bounded coefficient verification beyond the supplied fixed-$P,Q,K$ certificate. Thus this response does not independently establish the full binary congruence $H-N\equiv0\pmod{32}$.

No irrationality conclusion follows.

# 1. Actual ternary blocks and their scalar factors

Write


$$
A=H-D=n-2,\quad d=\frac{3D}{2}-1,\quad
\nu=\frac D2-1,\quad m=\frac{A+1}{2},
$$




$$
r_*=\frac{3H-1}{2},\quad r_1=\frac{H-1}{2},
\quad r_2=\frac{H/3-1}{2}.
$$


The columns remain the monomials $1,y,\ldots,y^m$, with LOW $0\le a<d$, HIGH $d\le a\le m$, and


$$
U=\langle1,\ldots,y^{D-1}\rangle,\qquad
z_i=y^i(y-1)^D,\quad0\le i<\nu.
$$



Let


$$
B_A=(y-1)^A,\qquad P=B_A(\beta+3y),\qquad
\beta=-71-A.
$$


The primitive unit $\lambda=L_n/3$ is stripped only for this local calculation.

The complete functional gives, for the core,


$$
G_{ab}
=[y^{r_*}]Py^{a+b}
+3\sum_{t=0}^{h-1}3^tB_t(Py^{a+b})
-\frac{3^h}{4}\mathfrak f((y+1)Py^{a+b}),
$$


with the actual-polynomial error added. Here each $B_t$ retains its exact inverse unit and original cutoff.

The definitions


$$
G=
\begin{pmatrix}
3L&3X\\
3X^T&E
\end{pmatrix}
$$


therefore give, after eliminating $U$, the HIGH block


$$
\widehat E=E-3X_U^TL_U^{-1}X_U=E_0+3F,
$$


where


$$
\boxed{F=\frac{E-E_0}{3}-X_U^TL_U^{-1}X_U.}
$$


The factor $3$ in the correction to $E$, and its absence in the displayed correction to $F$, are correct. Likewise the remaining LOW Schur complement, after dividing its original scale by $3$, has HIGH correction


$$
-3\,\widetilde V\widehat E^{-1}\widetilde V^T.
$$


Thus the supplied definitions agree with the previous sixth-carry normalization.

### Forces, endpoint subtraction, and divisions

The core is divisible by $y+1$, so its endpoint-subtracted quotient is exactly $Py^{a+b}$. For the actual error,


$$
\frac{3^7R(y)-3^7R(-1)}{y+1}\in3^7\mathbb Z_3[y].
$$


Every pole weight in $G$ is $3$-integral. After division by $3$, this error is still in $3^6\mathbb Z_3$.

The factorial term is in $3^h\mathbb Z_3$ before division and $3^{h-1}\mathbb Z_3$ afterwards. On the stated domain $h-1\ge6$. It cannot affect the modulo-$27$, modulo-$9$, or modulo-$3$ formulas used below.

For $u<D$ and $a\le m$, the core degree in a LOW–HIGH entry satisfies


$$
\deg(Py^{u+a})
\le A+1+(D-1)+m=H+m<r_*,
$$


because $D>2$. Hence the top pole is absent from $X_U$; it is also absent from $L_U$.

Finally $4n-3<9H$, so the top layer has only the unit $c=1$. At the first lower layer, the only possible units are $1,5,7$, while the polynomial degree is at most $2n-2<5H/2-1/2$. Thus only $c=1$ actually contributes there. These observations justify, in particular,


$$
\begin{aligned}
F_{ab}\equiv{}&
\frac{\beta-1}{3}(E_0)_{ab}
+[y^{r_*}]yB_Ay^{a+b}\\
&+\sum_{t=0}^{2}3^tB_t(Py^{a+b})
-(X_U^TL_U^{-1}X_U)_{ab}\pmod{27}.
\end{aligned}
$$


No endpoint or force term has been deleted before establishing its depth.

# 2. The actual two-position identity

Set


$$
p_i(y)=y^{H/3+i}(y-1)^D,\qquad0\le i<\nu.
$$


Every coefficient of this polynomial belongs to HIGH: its minimum exponent is $H/3+i>d$, while


$$
H/3+i+D\le H/3+\frac{3D}{2}-2<m.
$$


Both inequalities follow from $H>8748D$.

Modulo $3$,


$$
B_Ap_i=y^{H/3+i}(y^H-1).
$$


Also


$$
\frac{\beta-1}{3}=-24-\frac A3\equiv0\pmod3,
\qquad \beta\equiv1\pmod3.
$$



## 2.1 The actual LOW correction vanishes

For $0\le u<D$,


$$
(X_Up_i)_u
=[y^{r_1}]\,\beta y^{H/3+i+u}(y^H-1)\pmod3.
$$


The low branch cannot contribute because


$$
H/3+i+u
\le H/3+\frac{3D}{2}-3<r_1.
$$


The high branch has degree greater than $r_1$. Therefore


$$
X_Up_i=0\pmod3.
$$


Since $L_U$ is a unit block,


$$
X_U^TL_U^{-1}X_Up_i=0\pmod3.
$$


This eliminates the **actual** LOW projection, not a substitute projection.

## 2.2 The top linear term

For a HIGH row $a$, its value on $p_i$ is


$$
[y^{r_*}]y^{H/3+i+a+1}(y^H-1).
$$


The positive branch contributes precisely when


$$
a=r_*-H-H/3-i-1=r_2-i-1,
$$


with coefficient $+1$.

The negative branch would require


$$
a=r_*-H/3-i-1,
$$


which is greater than $m$. It is therefore excluded by the actual finite HIGH range.

## 2.3 The first lower pole

Modulo $3$, all $t\ge1$ layers vanish. The remaining lower term is


$$
[y^{r_1}]\,\beta y^{H/3+i+a}(y^H-1).
$$


Its negative branch contributes precisely at


$$
a=r_1-H/3-i=r_2-i,
$$


with coefficient $-\beta=-1\pmod3$; its positive branch would require a negative HIGH index.

Both surviving positions are in HIGH. Indeed their smallest possible value is


$$
r_2-\nu>d,
$$


and their largest is $r_2<m$.

Combining all terms proves


$$
\boxed{Fp_i=-e_{r_2-i}+e_{r_2-i-1}\pmod3.}
$$



# 3. Evaluation and scope of $A_{81}$

Reuse the already completed evaluations


$$
JRJ^T=0
$$


and the three edge contractions in A4turn22. Thus


$$
A_{81}=-KRFRJ^T-JRFRK^T+KRFRFRK^T\pmod3.
$$



The actual finite inverse satisfies


$$
RK^Te_i=p_i,\qquad
Re_{r_2-i}=p_i,\qquad Re_{r_2-i-1}=p_{i+1}\pmod3.
$$


The last identity includes $i+1=\nu$; that extended polynomial still lies entirely in HIGH.

The established $J$-support is disjoint from every $p_i$, $0\le i\le\nu$: the nonedge bands lie at least $H/18$ away from their support, and the last two HIGH coordinates are also disjoint. Hence


$$
Jp_i=0,\qquad0\le i\le\nu.
$$


Consequently,


$$
JRFRK^Te_i=J(-p_i+p_{i+1})=0.
$$


Its transpose vanishes as well.

For the remaining term, two support positions of $Fp_i,Fp_t$, written


$$
b=r_2-i-\delta,\qquad c=r_2-t-\delta',
\quad\delta,\delta'\in\{0,1\},
$$


select in $R$ the coefficient degree


$$
D+r_1-b-c
=D+\frac{H+3}{6}+i+t+\delta+\delta'>D.
$$


The relevant inverse polynomial modulo $3$ is $(1-z)^D$, so that coefficient is zero. Thus


$$
(Fp_i)^TR(Fp_t)=0.
$$



It follows that


$$
\boxed{A_{81}=0\pmod3,\qquad
\operatorname{rank}_{\mathbb F_3}A_{81}=0,\qquad
\operatorname{im}A_{81}=\{0\}.}
$$



The transported radical endpoint remains


$$
\overline e_{\rm rad}=((-1)^i)_{0\le i<\nu}\ne0,
$$


and is outside this image. This statement concerns $A_{81}$, **not** the full sixth form


$$
T_6=-\left(A_9/9+A_{27}/3+A_{81}\right)\pmod3.
$$


A1’s two contributions must still be evaluated before asserting a rank or image for $T_6$.

### Other formulas in the new note

The supplied $Fe_d$ and $V$ formulas have the correct scalars:

* In column $d$, $E_0e_d=e_m$, while the linear top term is $e_{m-1}-Ae_m$. The remainder projection from monic division therefore gives exactly the stated edge coefficient
  

$$
\left((\beta-1)/3-A\right)e_m+e_{m-1}.
$$


* In $V$, the unique top contribution after division by $3$ is $+ee_m^T$, since $i+a\le r_1-1$, with equality only at the last radical/HIGH corner.
* The polynomial error remains in $3^6\mathbb Z_3$ after this division, so both the modulo-$81$ formula for $V$ and the subsequent modulo-$9$ formula for $J$ have sufficient precision.

I do not evaluate the higher contractions of these two formulas assigned elsewhere.

# 4. Independent binary audit: the large convolution passes

Here the domain and notation are separate:


$$
b=9^r,\quad n=4002b,\quad r=18+32u,\quad u\ge0,
$$




$$
b=128D+81,\quad n=128C+66,\quad
C=4002D+2532,\quad e=2C+1.
$$


Thus $D$ is odd, $C\equiv2\pmod4$, and $e$ is odd.

Retain the actual columns


$$
X=Z_w/(2R),\qquad Y=V_w/(4b!),
$$


and the exact falling metric


$$
\Omega=\operatorname{diag}\bigl((n+2)_{\underline j}^{\,2}\bigr)_{0\le j\le b}.
$$


No replacement of this metric by unweighted original coordinates is made.

Use the supplied certified fixed-polynomial identities for $K$, including $K(16)=48$. The following audit concerns the genuinely unbounded convolution.

## 4.1 Kernel reduction

Repeated squaring modulo $64$ gives


$$
(1-z)^{128}\equiv(1-z^4)^{32}\pmod{64}.
$$


Both series have constant term $1$; inversion and raising to the positive integer $e$ preserve this congruence. Thus


$$
(1-z)^{-128e}\equiv(1-z^4)^{-32e}\pmod{64}.
$$



For


$$
c_v=\binom{32e+v-1}{v},
$$


the identity


$$
c_v=\frac{32e}{v}\binom{32e+v-1}{v-1}
$$


gives


$$
v_2(c_v)\ge5-v_2(v)\qquad(v>0).
$$



When $16\mid L$, the certified properties $4\mid K(4s)$ and $16\mid K(16s)$ eliminate respectively


$$
v\ \text{odd},\quad v\equiv2\pmod4,\quad
v\equiv4\pmod8,\quad v\equiv8\pmod{16}.
$$


Only $v=16w$ remains.

Modulo $4$, repeated binary reduction gives


$$
c_{16w}\equiv\binom{2e+w-1}{w}.
$$


The $64$-periodicity on multiples of $16$ makes the surviving sampled factor $K(L)$. Summing by the hockey-stick identity yields


$$
\boxed{
\eta_j-2\theta_j
\equiv K(L)
\binom{2e+\lfloor L/64\rfloor}{\lfloor L/64\rfloor}
\pmod{64}.}
$$



## 4.2 The negative boundary degree is harmless

The Laurent support starts at $-7$, so only $-4$ can be sampled. Its actual coefficient is


$$
-B_3+4B_4-10B_5+20B_6
\equiv-56+224-160+960
\equiv8\pmod{64}.
$$


For $16\mid L$, the corresponding kernel index is


$$
v=(L+4)/4,
$$


which is odd. Its coefficient has depth at least $5$; multiplied by the displayed boundary coefficient it vanishes modulo $64$. This checks the omitted negative range directly.

## 4.3 Paired units and the contracted cancellation

For $j=128t,128t+64$, put $d=D-t$ and


$$
Z_d=\binom{e+d}{d}.
$$


The two values of $\lfloor L/64\rfloor$ are $2d+1,2d$. Binary scaling gives


$$
\binom{2e+2d}{2d}\equiv Z_d\pmod4.
$$


The adjacent ratio is


$$
\frac{2e+2d+1}{2d+1}
=1+\frac{2e}{2d+1}\equiv3\pmod4.
$$


Thus the two convolution units are indeed $3\kappa,\kappa$, where


$$
\kappa=K(16)/16=3\pmod4.
$$



The weight reduction also passes:


$$
W_{128t}\equiv W_{128t+64}\equiv\binom Ct\pmod4.
$$


For example,


$$
(1+z)^{32C}\equiv(1+z^{32})^C\pmod4
$$


because the intermediate correction is a multiple of $2C$, and $C$ is even; multiplication by $(1+z)^{17}$ supplies coefficients $1,17\equiv1$ at the two offsets.

Let


$$
E_t=\binom Ct\binom{e+D-t}{D-t}.
$$


Every $E_t$ is even. Therefore $3\kappa E_t$ and $\kappa E_t$ agree modulo $4$, and both equal $E_t\pmod4$. Reconstruction, including its division by $4$, gives


$$
\frac{X_{128t}-Y_{128t}}8
\equiv
\frac{X_{128t+64}-Y_{128t+64}}8
\equiv E_t/2\pmod2.
$$


Together with the established first-column parity, the two defect terms cancel. Hence


$$
\boxed{\sum_{j\in\mathcal P}X_j(Y_j-X_j)\equiv0\pmod{32}.}
$$



The full endpoint passes separately: $v_2(W_b)\ge6$ implies


$$
v_2(X_b)\ge5,\qquad v_2(Y_b)\ge4,
$$


using $Y_b=W_b(1+b\eta_{b-1})/4$, with its $1$ retained.

# 5. Binary audit limitation and bounded follow-on

The fixed $P,Q,K$ certificate does not itself verify the new coordinate moment reductions used in A5turn17 §§9–10. In particular, the new modulo-$8$ reconstructions (45), (53), (57), the modulo-$4$ $Q$-reconstruction (55), and the modulo-$16$ assertion in the weight-unit $j=4k$ case are additional polynomial identities after finite moment summation.

I have not independently completed those coefficient calculations here. Consequently the proof status is:

* **Proved in this audit:** paired contribution zero; negative Laurent boundary zero; actual endpoint zero.
* **Not independently certified here:** full even off-pair refinement and all shifted odd-pair reductions.
* **Therefore not asserted here:** $H-N\equiv0\pmod{32}$, or its valuation alternative.

A bounded follow-on reduction is now exact:


$$
H-N\equiv
\sum_{\substack{j\text{ even}\\j\notin\mathcal P}}
X_j(Y_j-X_j)
+
\sum_{\substack{j<b\\j\text{ odd}}}
X_jY_j
\pmod{32}.
$$


The odd $X_j^2$ terms vanish by the established $8\mid X_j$. Thus no further paired convolution, Laurent-boundary calculation, or endpoint calculation is needed to finish this audit.

# 6. Primitive normalization and whole real errors

For the ternary determinant family, retain


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|),\qquad
q=|B_{\rm det}|/g,\qquad
p=-\operatorname{sgn}(B_{\rm det})A_{\rm det}/g.
$$


When $B_{\rm det}\ne0$,


$$
q(e+\pi)-p
=\frac{\operatorname{sgn}(B_{\rm det})\ell^{(n+1)/2}}g
\det H_{\rm complete}.
$$


The primitive multiplier remains $\ell^{(n+1)/2}/g$. Evaluation of $A_{81}$ alone establishes neither a new sixth gcd bound nor nonvanishing of this whole error.

For the binary family, retain the least actual column clearer $d_B$, the stated falling metric, and


$$
A_B=N_{B,1}^T\Omega N_{B,1},\quad
H_B=N_{B,1}^T\Omega N_{B,2},\quad
g_B=\gcd(A_B,|H_B|).
$$


Then


$$
q_n=A_B/g_B,\qquad p_n=H_B/g_B,
$$


and the multiplier relative to the uncleared quadratic form is $d_B^2/g_B$.

The exact denominator interface remains


$$
v_2(q_n)=
\max\left\{0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)\right\}.
$$


Within the retained complete signed-error theorem,


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
$$


eventually, with


$$
\log|\epsilon_n|
=-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


This is conditional on that analytic interface and concerns the whole error, not a selected force. No bound here makes the primitive error tend to zero.

## Closing ledger

### (1) New result and proof status

**Proved:** the actual two-position identity for $Fp_i$, with finite HIGH indices, exact LOW correction, and all force/error depths retained; hence $A_{81}=0$, with rank zero and image $\{0\}$, on precisely the assigned ternary domain.

**Independently audited:** the binary high convolution, negative boundary degree, paired modulo-$4$ units, complete paired cancellation, and actual endpoint.

**Incomplete:** independent certification of the remaining binary even and odd moment reductions. No value of $N/16$ is assumed.

### (2) Exact remaining bottleneck

For $T_6$, A1 must evaluate $A_9/9$ and $A_{27}/3$.

For the binary fourth carry, the remaining task is the bounded coefficient verification identified in §5, followed by its stated carry classifications.

For irrationality, neither construction yet controls the actual reduced denominator after its final gcd sufficiently to produce a compatible infinite sequence of nonzero primitive errors tending to zero.

### (3) Computation request

A bounded exact request to the coordinator is useful:

**Inputs:** the supplied $P^\#\bmod32$, $Q^\#\bmod64$, seven boundary values, and the finite moment identity for


$$
T(-2n)\mathcal S_bf,
$$


keeping the large binomials symbolic as


$$
\mathcal M_v(j)=\binom{2n+b-1-j}{b-1-j-v}.
$$



**Expected verifiable output:** Newton-coefficient certificates for A5turn17 (45), (53), (55), (57), and the exceptional $\mathcal M_4$ coefficient in §9.2, with the precise residue assumptions on $j,n,b$ recorded before every division. These are fixed-degree identities, not growing-index tests. They would close the specific audit gap without pretending that finite sampling proves an infinite assertion.
