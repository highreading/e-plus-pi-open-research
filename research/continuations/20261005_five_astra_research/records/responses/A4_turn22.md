> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 — partial sixth-contraction evaluation and independent four-fifths audit

## Verdict

I obtain a **partial evaluation of $A_{81}$** on the assigned domain


$$
n=4^j+1,\qquad j>0,\qquad243\mid j,\qquad
0<D=H-(n-2)<H/8748.
\tag{1}
$$


In particular, the supplied actual support of $J\bmod3$ proves


$$
\boxed{JRJ^T=0\pmod3.}
\tag{2}
$$


The actual edge supports also eliminate the three endpoint terms in $A_{81}$. The remaining task can be reduced to one particularly small support certificate for $FRK^T$.

**I do not certify that support certificate from a complete defining formula for $F$.** The documents provide the complete functional and several evaluations of its blocks, but do not supply the entrywise definitions and normalizations of $E,X_U,L_U$ needed to derive the whole actual matrix


$$
F=\frac{E-E_0}{3}-X_U^TL_U^{-1}X_U
$$


without an additional identification step. Consequently I do not claim an evaluated $A_{81}$, $T_6$, or a sixth gcd improvement.

The independent analytic audit **passes for the new estimates in A3turn20**. Its whole below-$4/5$ theorem follows with the stated contour and complete-residual estimates retained as dependencies. In particular, the defining formula for the complete exponential-force coefficients $eE_i$ is unavailable here, so the complete-residual bounds cannot be independently reproved from these documents.

No conclusion about irrationality of $e+\pi$ follows.

---

# 1. Arithmetic conventions and reused identity

Retain


$$
A=H-D=n-2,\quad d=\frac{3D}{2}-1,\quad
\nu=\frac D2-1,\quad m=\frac{A+1}{2},
$$


and


$$
r_1=\frac{H-1}{2},\qquad r_2=\frac{H/3-1}{2}.
$$


The actual monomial index ranges are

* LOW: $0\le a<d$;
* HIGH: $d\le a\le m$;
* unit LOW space: $U=\langle1,\ldots,y^{D-1}\rangle$;
* radical columns:
  

$$
z_i=y^i(y-1)^D,\qquad0\le i<\nu.
$$



All congruences below use the primitive-unit-stripped normalization $\lambda=L_n/3$. The full depth-seven core and complete factorial, endpoint-subtracted, all-pole functional remain the ones in A4turn21.

I reuse, without rederiving, its completed identity


$$
T_6=-\left(A_9/9+A_{27}/3+A_{81}\right)\pmod3,
\tag{3}
$$


and do not evaluate either contribution assigned to A1.

Write $R=E_0^{-1}$. Modulo $3$, its actual finite HIGH matrix is


$$
R_{ab}=[z^{D+r_1-a-b}](1-z)^D,\qquad d\le a,b\le m.
\tag{4}
$$


Here $d+m=D+r_1$, and all selected nonnegative degrees are below $H$, so the inverse coefficient gap justifies (4).

---

# 2. Proved: the full $JRJ^T$ contraction vanishes

The supplied actual support calculation, including the lower unit-pole pairs, gives


$$
\operatorname{supp}(J\bmod3)
\subseteq
\{m-1,m\}
\cup
\left\{
r_1-\frac{kH}{9}-i-a:
1\le k\le4,\ a\in\{0,1\},\ 0\le i<\nu
\right\},
\tag{5}
$$


with every displayed index intersected with HIGH.

This is sufficient to evaluate $JRJ^T$, not just $KRJ^T$.

## 2.1 Two nonedge bands

Take two possible nonedge indices


$$
b=r_1-kH/9-i-a,\qquad
c=r_1-lH/9-t-a'.
$$


The coefficient degree in (4) is


$$
D+r_1-b-c
=
D+\left(\frac{k+l}{9}-\frac12\right)H
+\frac12+i+t+a+a'.
\tag{6}
$$



Since $2\le k+l\le8$, the coefficient of $H$ stays at distance at least $1/18$ from zero.

* If $k+l\le4$, (6) is negative. Indeed its upper bound is less than $2D+1-H/18<0$.
* If $k+l\ge5$, (6) is greater than $D$.

In either case, the degree-$D$ polynomial in (4) has zero selected coefficient. The much stronger margin $H>8748D$ covers all the finite shifts.

## 2.2 Edge–nonedge and edge–edge pairs

Exactly,


$$
Re_m=e_d,\qquad Re_{m-1}=e_{d+1}+Ae_d.
$$


The established extended corner calculation gives


$$
Je_d=Je_{d+1}=0\pmod3.
$$


Thus every pairing involving one of the two edge columns vanishes after the complete row sum is taken. Pairings between the two edge columns vanish as well, since the corresponding corner of $R$ is zero.

This proves (2) for the actual finite HIGH matrix. No infinite convolution or replacement columns have been used.

---

# 3. Endpoint terms in $A_{81}$

The established supports are


$$
Fe_d\in\langle e_{m-1},e_m\rangle,\qquad
Fe_{d+1}\in\langle e_{m-2},e_{m-1},e_m\rangle
\pmod3.
\tag{7}
$$



The same actual monic-division argument extends one more step:


$$
\boxed{
Fe_{d+2}\in
\langle e_{m-3},e_{m-2},e_{m-1},e_m\rangle\pmod3.
}
\tag{8}
$$



For clarity, the relevant ingredients for this limited extension are already present in A4turn21:

1. Divide $y^{d+2}$ by $(y-1)^D$. Its quotient degree is $\nu+2$.
2. Extended direct annihilation identifies its exact LOW-unit projection with this remainder at more than the required precision.
3. Modulo $3$, the first lower pole applied to the quotient terms can survive only when $i+b=r_1$. Since $i\le\nu+2$ and $r_1=m+\nu$, these HIGH indices satisfy $b\ge m-2$.
4. The linear top perturbation adds at most the index $m-3$.
5. Deeper lower layers and the depth-seven core error do not contribute at this precision.

This proves (8) without determining the corresponding coefficients.

The inverse image under $R$ of the last $s+1$ HIGH coordinates is supported in the first $s+1$ HIGH coordinates. This follows immediately from (4), including finite truncation.

Put $w=RFe_d$. By (7),


$$
\operatorname{supp}w\subseteq\{d,d+1\}.
$$


Consequently


$$
\operatorname{supp}(RFw)\subseteq\{d,d+1,d+2\}.
$$


Since $J$ kills these three coordinates,


$$
\boxed{JRFRFe_d=0\pmod3.}
\tag{9}
$$



Using (7)–(8), one further application of $RF$ lands in
$\{d,d+1,d+2,d+3\}$, all killed by $K$. Hence


$$
\boxed{KRFRFRFe_d=0\pmod3.}
\tag{10}
$$



Finally $Fw=FRFe_d$ is supported in the last three HIGH coordinates, where $R$ has a zero corner. Therefore


$$
\boxed{
(FRFRFRF)_{dd}
=(FRFe_d)^TR(FRFe_d)=0\pmod3.
}
\tag{11}
$$



Thus the entire assigned endpoint portion is evaluated, with the actual endpoint not substituted for the last radical basis vector $e$.

Combining (2) and (9)–(11),


$$
\boxed{
A_{81}
=-KRFRJ^T-JRFRK^T+KRFRFRK^T
\pmod3.
}
\tag{12}
$$



---

# 4. A bounded support certificate that would finish $A_{81}$

This section is a **conditional reduction**, not an asserted evaluation of the missing actual block.

The established polynomial interpretation is


$$
RK^Te_i\longleftrightarrow
p_i(y)=y^{H/3+i}(y-1)^D,\qquad0\le i<\nu.
\tag{13}
$$



A sufficient remaining certificate is


$$
\boxed{
\operatorname{supp}(Fp_i\bmod3)
\subseteq\{r_2-i,\ r_2-i-1\},
\qquad0\le i<\nu,
}
\tag{14}
$$


where $p_i$ means its actual finite HIGH coefficient vector.

## 4.1 Why this certificate is sufficient

From (4), for $\delta=0,1$,


$$
Re_{r_2-i-\delta}
\longleftrightarrow
y^{H/3+i+\delta}(y-1)^D.
\tag{15}
$$


The entire polynomial lies in HIGH, even for $i+\delta=\nu$.

The support proof for $Jp_i=0$ extends to $i=\nu$. Indeed a nonedge $J$-index is near


$$
\left(\frac12-\frac{k}{9}\right)H,
$$


whereas the support of $p_i$ is near $H/3$. Their separation has magnitude at least $H/18$, larger than all the degree-$D$ shifts. The last two HIGH coordinates are also disjoint from the support of these polynomials. Therefore


$$
Jp_i=0,\qquad0\le i\le\nu.
\tag{16}
$$



Under (14), equations (15)–(16) give


$$
JRFRK^T=0,
$$


and symmetry gives $KRFRJ^T=0$.

For the remaining contraction, the two support indices
$b=r_2-i-\delta$, $c=r_2-t-\delta'$ select in $R$ the degree


$$
D+r_1-b-c
=
D+\frac{H+3}{6}+i+t+\delta+\delta'>D.
$$


Thus


$$
(Fp_i)^TR(Fp_t)=0,
$$


which is exactly $KRFRFRK^T=0$.

Hence:

> **Proved conditional lemma.** The actual support certificate (14), together with the supplied actual $J$-support, implies $A_{81}=0\pmod3$.

## 4.2 What is not yet certified

There is a plausible direct explanation for (14):

* the first lower coefficient extraction from $p_i y^b$ selects $b=r_2-i$;
* the linear top perturbation selects $b=r_2-i-1$;
* the supplied calculation gives $X_Up_i=0\pmod3$, eliminating the displayed LOW-unit correction.

However, this is not yet a derivation of the **whole** actual $F$. In particular, the precise identification of its remaining lower HIGH block with that first-pole extraction must be supplied with its normalization. The complete functional alone does not explicitly define the block symbols $E,X_U,L_U$ used in the Schur formula.

Accordingly, (14) is an exact, bounded missing certificate—not a renamed general contraction. Its verification requires only two allowed positions in each $Fp_i$, with all other positions shown zero uniformly. No coefficients at those two positions need be evaluated to finish (12).

---

# 5. Independent audit of A3turn20

The analytic domain is separately


$$
n\to\infty,\qquad3\le b=o(n^{4/5}),\qquad d=b-1,\qquad0\le j\le b,
\tag{17}
$$


on both parities. It has no identification with the weighted arithmetic family above.

## 5.1 Endpoint-safe $Q_8$ virial: pass

For $v_7(t)=t^7g(t)/M$,


$$
v_7\left(-n\frac{g'}g\right)
=\alpha_0nt^7\sin t\ge cn t^8
$$


on the closed principal interval. The other one-particle terms have bounds


$$
v_7h_q'=O(t^8),\qquad v_7'=O(t^6).
$$



The pair estimate is valid on the full square:


$$
|(v_7(x)-v_7(y))\cot((x-y)/2)|
\le C(|x|^6+|y|^6).
$$


Indeed the divided difference is bounded by $C(|x|^6+|y|^6)$, and
$(x-y)\cot((x-y)/2)$ is bounded for $|x-y|\le3\pi/2$.

The field vanishes at the endpoints, and the collision flux vanishes because of the quadratic Vandermonde zero. Thus


$$
cn\,\mathbb EQ_8\le Cd\,\mathbb EQ_6+C\mathbb EQ_8.
$$


With the established sixth moment, absorption gives


$$
\mathbb EQ_8=O(d^5/n^4).
$$



## 5.2 Signed $C_5$ with the actual complex denominator: pass

Reflection gives $\mathbb EC_5=0$, including on the ordered chamber after reversing the particle order. Poincaré gives


$$
\mathbb EC_5^2\le Cn^{-1}\mathbb EQ_8=O(d^5/n^5).
$$



With the actual weight $\mathcal W_j=S_je^{i\Phi_q}$,


$$
\begin{aligned}
|\mathbb E(\mathcal W_jC_5)|
&\le
\sqrt{\mathbb EC_5^2\,\mathbb E\Phi_q^2}
+\|S_j-1\|_\infty\sqrt{\mathbb EC_5^2}\\
&=O(d^3/n^3)+O((d/n)^{7/2}).
\end{aligned}
$$


Division by $N_j=\mathbb E\mathcal W_j$, with $|N_j|\ge1/2$, yields


$$
\langle C_5\rangle_j=O(d^3/n^3).
$$


No symmetry of $S_j$ is needed.

## 5.3 Improved third derivative and fourth moment: pass

For the real centered component $Y_0$ of
$H-\mathbb EH$, $\|\nabla Y_0\|^2\le Cd$. Therefore


$$
\operatorname{Var}(Y_0^2)
\le \frac Cn\mathbb E\|\nabla(Y_0^2)\|^2
\le C\frac dn\mathbb EY_0^2
=O((d/n)^2).
$$


This proves the claimed fourth moment, and hence


$$
\mathbb E|H-\mathbb EH|^3=O((d/n)^{3/2}).
$$


Bounded $\mathcal W_j/N_j$ transfers the absolute moment estimates to the algebraic cumulant expansion. It does not turn that cumulant into a positive variance.

The signed linear expansion


$$
2h(t)^3=\frac2{(1+q)^3}
+\frac{6i}{(1+q)^4}t+O(t^2)
$$


gives the improved trace remainder $O(d/n+d^2/n)$. Thus the stated third-derivative remainder is valid.

## 5.4 Scalar error exponents: pass within the stationary interface

With $\epsilon=d/n$, the three derivative remainders contribute respectively


$$
O(d^2/n^2+d^5/n^4),
$$




$$
O(d^3/n^3+d^5/n^4),
$$


and


$$
O(d^4/n^4+d^5/n^4+(d/n)^{9/2}).
$$


All are bounded by $O(d/n+d^5/n^4)$ for $2\le d=o(n)$. The next Taylor remainder is $O(n\epsilon^5)=O(d^5/n^4)$.

Thus, using the established lower stationary-coefficient cancellations and reciprocal-anchor comparison, the improved error genuinely closes on (17). At $d\asymp n^{4/5}$, it need not tend to zero.

## 5.5 Whole theorem: dependencies remain explicit

The following are still inputs to the whole theorem:

1. the fixed-neighborhood actual zero-free logarithm and derivative bounds;
2. signed particle outer-sector estimates, including differentiated insertions;
3. the deformed scalar contour estimates, both minus connectors, and the $O(n^{-1/5})$ local relative error;
4. the complete exponential-force and endpoint bounds
   

$$
|E_j/P_j|\le \frac{e^{Cb}}{n!\sqrt n},\qquad
   |D/P_0|\le\frac{C\sqrt n\,e^{Cb}}{n!B_0}.
$$



The last bounds are sufficient: after division by $M^{-2n-b}$, their logarithms are $-n\log n+O(n+b)$. But their defining $eE_i$ formula is absent, so this audit does not independently establish them.

Normality is compatible with (17), since eventually $b\le n/1000$. Uniform coordinate errors transfer exactly to every positive diagonal metric through the convex weights


$$
\frac{w_ju_j^2}{\sum_\ell w_\ell u_\ell^2}.
$$


This does not extend to arbitrary nondiagonal metrics.

Therefore, **with those dependencies**, the whole law and its eventual nonvanishing pass:


$$
c_W-(e+\pi)=(-1)^{n+1}4\pi M^{-2n-b}
\left[1+O\!\left(\frac bn+\frac{b^5}{n^4}+n^{-1/5}\right)\right].
\tag{18}
$$



---

# 6. Primitive arithmetic and nonvanishing scope

For the weighted construction retain the final pair


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|),\quad
q=\frac{|B_{\rm det}|}{g},\quad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g.
$$


Where $B_{\rm det}\ne0$,


$$
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_{\rm det})\ell^{(n+1)/2}}g
\det H_{\rm complete}.
\tag{19}
$$


The primitive multiplier remains $\ell^{(n+1)/2}/g$. No sixth gcd bound or whole-error nonvanishing follows from this partial evaluation. Restoring $\lambda$ does not affect any zero congruence proved above. The transported endpoint residue remains $((-1)^i)_{i<\nu}\ne0$, but its relation to the image of the still unevaluated $T_6$ is unknown.

For the separate analytic construction, retain the least actual clearer $d_B$, integral positive diagonal metric $\Omega$, and


$$
N_B=d_B[u,v],\quad
A_B=N_{B,1}^T\Omega N_{B,1},\quad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_B=A_B/g_B,\qquad p_B=H_B/g_B.
$$


The primitive multiplier is $d_B^2/g_B$. Within the audited analytic dependencies,


$$
q_B(e+\pi)-p_B
=(-1)^n4\pi q_BM^{-2n-b}
\left[1+O\!\left(\frac bn+\frac{b^5}{n^4}+n^{-1/5}\right)\right]\ne0.
\tag{20}
$$


There is still no bound ensuring these primitive errors tend to zero.

---

## Closing ledger

### (1) New result and proof status

**Proved from the supplied actual supports and extended projection identities:**

* $JRJ^T=0\pmod3$, with finite HIGH ranges retained.
* The three endpoint contractions in $A_{81}$ vanish.
* $A_{81}$ reduces to (12).
* The explicit two-position support certificate (14) would eliminate all three remaining contractions.

**Audit:** A3turn20’s eighth moment, signed fifth trace, Poincaré fourth-moment argument, improved derivatives, and subcritical scalar error exponents pass. Its whole theorem remains dependent on the expressly retained contour and complete-residual interfaces.

### (2) Exact remaining bottleneck

For A4’s sixth contribution, certify (14) from the complete actual block definitions, including the lower HIGH normalization and LOW-unit projection. The actual full $F\bmod3,J\bmod3$ matrices have not been derived here.

Even after $A_{81}$ is evaluated, no sixth gcd conclusion is available until A1’s two normalized contributions are evaluated.

For irrationality, the unresolved arithmetic requirement remains same-index control of the **actual denominator after the final gcd**, together with nonzero whole primitive errors tending to zero.

### (3) Computation request

None. A finite rank computation would not settle the missing uniform support assertion. The bounded symbolic item needed next is the entrywise definition of $E$ and $X_U$, with their normalization relative to the complete functional, sufficient to verify or refute (14).
