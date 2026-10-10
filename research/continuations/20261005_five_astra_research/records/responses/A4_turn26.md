> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 audit: fixed-depth support closure and the second MAIN29 mixed relation

## Verdict

1. **A1turn25, Operations 1–5: pass for the core blocks defined in the supplied block document.** The inverse coefficients, complete polynomial copies, finite HIGH truncations, and actual LOW projection fit together. I find no offending coefficient or boundary term. Below I give the detailed closure argument, including the degree checks needed to justify the LOW projection.

   **Transfer to the actual polynomial is a conditional pass:** it uses the stated approximation
   

$$
Q^{\rm loc}=Q_c+3^\tau T,\qquad \deg T\le n,\qquad
   \tau=v_3(j)+2,
$$


   and the established integral unit-block structure. The precision-protection argument itself passes. The supplied documents state, but do not derive from an explicit formula for the actual polynomial, the approximation at arbitrary $\tau$.

2. **A2turn20, four-digit factorization and its consequences: conditional pass within the stated bounded-kernel interface.** The four-level factorial stripping, affine harmonic correction, common high factor, polynomial—not merely pointwise—leading identity, finite-range extension, Lucas contraction, and endpoint-fibre cancellation are sound.

   The exact interface requiring retention is important: the supplied documents do not give the underlying contact operators and forcing polynomials from which the asserted effective Newton degrees are derived. Thus I can verify the consequences of the stated integral Newton expansions, but cannot independently reconstruct those expansions from the actual contact inverse. The values $g_0=26,g_1=3$ are also supplied finite arithmetic receipts, not computations independently reproduced here.

3. **The formula for $\beta(d)$ passes on $0\le d\le24,\ T=0$, subject to that same kernel interface.** No conclusion here concerns the shifted second mixed digit for $d=25,\ldots,28$.

These findings establish no irrationality or rationality conclusion for $e+\pi$.

---

# I. A1turn25: fixed-depth support closure

## 1. Domain, columns, metric, and normalization

Fix an integer $r\ge6$. Retain exactly


$$
j>0,\quad v_3(j)\ge r-2,\quad n=4^j+1,\quad H=3^{h-1},
$$




$$
0<D=H-(n-2)<\frac{H}{512(r+1)^2\,3^{r-1}},
\qquad h\ge r+2.
$$


Write


$$
A=H-D,\quad
d=\frac{3D}{2}-1,\quad
\nu=\frac D2-1,\quad
m=\frac{A+1}{2},
$$




$$
r_1=\frac{H-1}{2},\qquad r_*=\frac{3H-1}{2}.
$$



Here $D$ is even and divisible by $3$: both $H$ and $4^j-1$ are divisible by $3$, and both are odd. Since $D>0$, this gives $D\ge6$.

The columns are the actual monomials $1,y,\ldots,y^m$, with


$$
U=(1,\ldots,y^{D-1}),\qquad
z_i=y^i(y-1)^D\quad(0\le i<\nu),
$$


and HIGH equal to the finite interval $[d,m]$.

I use the complete functional in the question, including its factorial force, endpoint-subtracted quotient, and original finite pole cutoffs. Only the primitive unit $\lambda=L_n/3$ is stripped.

The exact core contribution is


$$
G_{ab}^{c}
=[y^{r_*}]P\,y^{a+b}
+3\sum_{t=0}^{h-1}3^tB_t(P\,y^{a+b})
-\frac{3^h}{4}\mathfrak f((y+1)P\,y^{a+b}),
$$


where


$$
P=(y-1)^A(\beta+3y),\qquad \beta=-71-A.
$$


Thus the block factors $3L,3X,E$, and


$$
F=\frac{E-E_0}{3}-X_U^TL_U^{-1}X_U
$$


have the normalization asserted in the source. In particular, the HIGH elimination contributes


$$
-3\widetilde V(E_0+3F)^{-1}\widetilde V^T
$$


to the normalized radical form. There is no additional division by $3$ hidden in this expression.

## 2. Coefficient precision and width budget

Set


$$
u=h-1,\qquad G=H/3^{r-1}.
$$


For $0<k<H$,


$$
v_3\binom Hk=u-v_3(k).
$$


One way to see the equality is


$$
\binom Hk=\frac Hk\binom{H-1}{k-1},
$$


where the last binomial is a $3$-adic unit because every base-$3$ digit of $H-1$ is $2$.

For


$$
a_k=[z^k](1-z)^{-H}=\binom{H+k-1}{k},
$$


the identity


$$
a_k=\frac Hk\binom{H+k-1}{k-1}
$$


gives


$$
v_3(a_k)\ge u-v_3(k).
$$


Consequently, below degree $H$, both required coefficient arrays modulo $3^q$ are supported on multiples of


$$
G_q=H/3^{q-1},\qquad 1\le q\le r.
$$


All $G_q/G$ are odd integers.

A pole of weight $3^t$, $t<r$, has index


$$
\frac{cH/3^t-1}{2}
=\frac{c3^{r-1-t}G-1}{2}.
$$


After subtraction of integer-grid exponents, it remains on an odd half-grid. The unit $c^{-1}\in\mathbb Z_3^\times$ changes its coefficient, not its support or precision. This applies separately to every pole satisfying the original cutoff; no pole pairing is needed.

The proposed width budget is sufficient. Starting with


$$
w_0=\nu+1=D/2,
$$


at most $r-2$ applications of $F$ give


$$
w\le(r-1)(\nu+1)\le(r-1)D.
$$


With


$$
W=4(r+1)(D+2)
$$


and $D\ge6$, the assigned constant implies


$$
G>512(r+1)^2D,\qquad W+2D+2<G/8.
$$


In particular, all the combined local shifts used below are much smaller than the separation $G/2$ between the integer and odd half-grids.

## 3. Operation 1: complete $V$-support — pass

For $0\le i<\nu$, $a\in[d,m]$,


$$
i+a\le\nu-1+m=r_1-1.
$$


In the top contribution to $V$, the $\beta B_H$ term cannot reach $r_*$. The term $3yB_H$ reaches it only when


$$
i+a=r_1-1.
$$


Since this is the maximum possible sum, it is precisely the last-radical/last-HIGH corner, with coefficient $1$ after division by $3$.

Every lower contribution has the form


$$
3^tc^{-1}[y^{(cH/3^t-1)/2}]
 B_H(\beta+3y)y^{i+a}.
$$


A surviving coefficient therefore places $a$ at an odd half-grid point with local shift $-i-\epsilon$, $\epsilon\in\{0,1\}$. Thus $V$ is half-grid-supported with width at most $\nu+1$, together with the specified upper corner.

The claimed lower-edge zero also follows entrywise. For


$$
d\le a\le d+W,
$$


the nongrid shift satisfies


$$
i+a+\epsilon\le W+2D-2.
$$


It cannot move an integer-grid coefficient of $B_H$ to an odd half-grid pole. The top corner is absent. Therefore


$$
V_{ia}\equiv0\pmod{3^r}
\quad(0\le i<\nu,\ d\le a\le d+W).
$$



## 4. Operation 2: inverse coefficients and finite polynomial copies — pass

The exact inverse is


$$
R_{ab}
=[z^{D+r_1-a-b}](1-z)^D(1-z)^{-H}.
$$


Every nonnegative coefficient degree selected in HIGH is below $H$, because


$$
D+r_1-a-b\le D+r_1-2d<H.
$$


Thus no coefficient beyond the proven inverse-series range is used.

For a basis input $e_b$, the inverse term $a_{kG}z^{kG}$ contributes, before HIGH intersection,


$$
a_{kG}\,y^{r_1-b-kG}(y-1)^D.
$$


This formula has the correct sign: reversal of the coefficients of $(1-z)^D$ gives $(y-1)^D$, since $D$ is even.

If


$$
b=\frac{(2l+1)G-1}{2}+s,\qquad |s|\le w,
$$


then the copy starts at


$$
r_1-b-kG
=\left(\frac{3^{r-1}-2l-1}{2}-k\right)G-s.
$$


It is therefore a complete integer-grid polynomial copy with shift of magnitude at most $w$, unless the finite HIGH interval cuts it.

There are only two possible boundaries:

* **Upper boundary.** The upper edge lies within $O(D)$ of the half-grid centre $H/2$. An integer-grid copy of width $w+D$ cannot straddle that boundary under the stated gap. It is either wholly inside or wholly outside.
* **Lower boundary.** Only the copy centred at the integer-grid point $0$ can be cut. Its largest exponent is at most $w+D$. Any surviving part lies in
  

$$
[d,w+D]\subseteq[d,d+w],
$$


  because $d\ge D$.

Thus finite truncation introduces only a lower-edge vector, with no width increase. The coefficients $a_{kG}$ retain their original valuations; no division is introduced.

## 5. Operation 3: actual $F$ on an internal copy — pass

Let


$$
p=y^{kG+s}(y-1)^D
$$


be wholly supported in HIGH. Then


$$
B_Ap=B_Hy^{kG+s}.
$$



### Actual LOW force

The absence of a top coefficient in $X_Up$ is justified before using any grid argument. For $u<D$,


$$
\deg(Pp\,y^u)\le A+1+m+D-1=H+m<r_*.
$$


The lower extractions involve


$$
B_H(\beta+3y)y^{kG+s+u}.
$$


Their local shifts have magnitude at most $w+D+1$, so none reaches a retained half-grid pole. Hence


$$
X_Up\equiv0\pmod{3^r}.
$$


Since $L_U^{-1}$ is integral, the actual LOW correction in $Fp$ vanishes at the same precision.

### Remaining terms

The three remaining terms are


$$
c_0E_0p,\qquad
\bigl([y^{r_*}]yB_Ap\,y^a\bigr)_a,\qquad
\left(\sum_t3^tB_t(B_Ap(\beta+3y)y^a)\right)_a,
$$


where


$$
c_0=(\beta-1)/3\in\mathbb Z_3.
$$


Each coefficient extraction subtracts an integer-grid exponent from a half-grid index. The linear factor increases the local shift by at most one. Thus


$$
F(\text{internal copies of width }w)
\subseteq
\text{half-grid plus upper edge of width }w+1.
$$


This conclusion uses the actual projected $F$, not its unprojected part.

## 6. Operation 4: actual lower-edge projection — pass

For $0\le s\le w$, divide monically:


$$
y^{d+s}=r_s+B_Dq_s,\qquad \deg r_s<D,
$$




$$
q_s=\sum_{a=0}^{\nu+s}\binom{D+a-1}{a}y^{\nu+s-a}.
$$


This quotient is integral and has degree $\nu+s$.

For $u<D$, the difference between the LOW forces of $y^{d+s}$ and $r_s$ is extracted from


$$
B_H(\beta+3y)q_sy^u.
$$


Its shifts lie between $0$ and $\nu+s+D$, within the proved gap. Its degree is at most


$$
H+\nu+s+D<r_*,
$$


again by the width bound. Therefore


$$
X_Ue_{d+s}\equiv L_Ur_s\pmod{3^r},
\qquad
L_U^{-1}X_Ue_{d+s}\equiv r_s\pmod{3^r}.
$$



Substitution into the actual definition of $F$ gives precisely the displayed generalization of $Fe_d$. There is no unaccounted top contribution from subtracting $r_s$, since its top LOW/HIGH coefficient vanishes by the same degree bound.

For the top terms,


$$
r_*-A-d=m.
$$


It follows that $E_0e_{d+s}$ is supported in the last $s+1$ coordinates, and the extra factor $y$ permits only one further coordinate. The lower terms have half-grid shifts in


$$
[-(\nu+s+1),0].
$$


Hence the width increase is at most $\nu+1$, as claimed.

## 7. Operation 5: exact upper-to-lower transport — pass

For $b=m-s$,


$$
D+r_1-a-b=d+s-a.
$$


A negative coefficient degree gives zero, so


$$
R_{a,m-s}=0\qquad(a>d+s).
$$


Therefore


$$
R(\text{upper edge of width }w)
\subseteq\text{lower edge of width }w
$$


exactly. This does not rely on an unrestricted-series replacement.

## 8. Closing the Schur walks

The direct LOW terms have the required precision as well. Their lower extractions involve


$$
B_H(\beta+3y)B_Dy^{i+l},
\qquad
B_H(\beta+3y)y^{i+u},
$$


with local shifts bounded by $2D$. Their top coefficients vanish by degree. Thus


$$
Z^TLZ\equiv Z^TLU\equiv0\pmod{3^r}.
$$



Inside the radical Schur form, the outer factor $3$ means that only


$$
\sum_{a=0}^{r-2}(-3)^a(RF)^aR
$$


is needed from the HIGH inverse. Each retained walk sends $V^T$ to complete internal integer-grid copies plus lower-edge vectors. The left $V$ kills:

* internal copies by the integer/half-grid separation, including separation from the upper corner;
* lower-edge vectors by the entrywise vanishing established in Operation 1.

Therefore the **core** conclusion is proved:


$$
\mathcal R_c\in3^r\operatorname{Mat}_{\nu}(\mathbb Z_3).
$$



## 9. Precision protection of the actual form

The turn24 perturbation proof passes with its stated integral-lift hypothesis. If


$$
Q^{\rm loc}-Q_c=3^\tau T,\qquad \deg T\le n,
$$


and the core orthogonal lift is $W_c=Z+3N$, then


$$
\Delta(W_c,W_c)
\equiv3^\tau\mathcal M(TZZ^T)\pmod{3^{\tau+1}}.
$$


Modulo $3$, only the top pole survives. But


$$
\deg(Tz_iz_l)\le H+2D-2,
$$


so the endpoint-subtracted quotient has degree at most $H+2D-3<r_*$. The linear perturbation therefore gains one factor of $3$.

The eliminated inverse has valuation at least $-1$, so the quadratic Schur correction has valuation at least $2\tau-1$ before radical division, and $2\tau-2\ge\tau$ afterwards. Hence


$$
\mathcal R_{\rm rad}(Q^{\rm loc})-\mathcal R_c
\in3^\tau\operatorname{Mat}_{\nu}(\mathbb Z_3).
$$



The factorial force is likewise harmless here: after the first division it has valuation at least $h-1\ge r+1$. Perturbations of the integral unit inverses do not lower this to the target precision.

Thus, **given the stated actual-polynomial approximation and unit-block interface**, the actual fixed-depth divisibility follows. Nothing here extends $r$ to a growing parameter or determines an exact denominator.

---

# II. A2turn20: common high factor and whole second mixed digit

## 10. Domain and the exact remaining interface

Retain


$$
p=29,\quad b=3^a,\quad n=2001b,\quad
a\ge1,\quad a\equiv432827\pmod{682892},\quad m_w=1.
$$


Coordinates are $0\le j\le b$; contact inverses use $0\le i,j<b$.

The metric is **falling**:


$$
\omega_j=j!\binom{n+2}{j}=(n+2)_{\underline j},
\qquad \Omega=\operatorname{diag}(\omega_j^2).
$$


Use


$$
P=Z_w/p^2,\qquad Q=(V_w/b!)/p^3,\qquad D=P^TP,\quad M=P^TQ.
$$



The proof requires the following bounded-kernel data:

* integral Newton coefficients at the asserted effective degrees;
* positive reconstructed support at most $58$ at the relevant grades;
* the displayed complete factorial boundary;
* the complete logarithmic-force bound;
* the endpoint-absorbed reconstruction identity.

The supplied sources state these data, but do not include the contact-operator definitions needed to derive the degree bounds independently. My conditional pass is explicitly limited by this interface.

## 11. Force accounting and termwise normalization

The carry proof extends to $0\le q\le145$: at digit $1$, absence of the weight borrow forces $j_1\le7$, and the second addition still carries; digit $3$ supplies a distinct compulsory factor. Likewise the negative range $-118\le q\le0$ retains the digit-$3$ factor.

The unit-boundary monomials require the stronger bounds


$$
W_jB_0(j),\quad W_jB_{-1}(j),\quad jW_jB_{-2}(j)\in p^3\mathbb Z_p.
$$


The $j$-factor in the last expression is essential and is retained.

The boundary accounting in turn20 is consistent:

* $s=0,1$: combinations of $B_0,B_{-1},jB_{-2}$, retained;
* $2\le s\le30$: coefficient valuation at least $2$, retained;
* $31\le s\le59$: coefficient valuation at least $3$, retained through $Y\bmod p^5$;
* $s\ge60$, including such terms feeding lower $c_s$: coefficient valuation at least $4$, hence killed modulo $p^5$ only **after** the compulsory negative-reconstruction factor;
* positive contact terms of grades $1,2$: retained;
* positive contact grade at least $3$: killed after the two reconstruction factors.

Thus normalization of the retained $Q$-summands by $p^3$ is termwise legitimate. The logarithmic force disappears only through its supplied whole-force bound, not through a formal omission.

The claimed effective degree $58$ is sufficient for everything that follows. Its derivation from the actual contact inverse remains the interface noted above.

## 12. Four factorial-stripping levels — pass

Write


$$
L=p^4,\quad j=LJ+x,\quad v=b_*-x,\quad b_*=687936.
$$


For retained $q$, set


$$
e=\mathbf1_{x>191112},\quad
u=\left\lfloor\frac{382219+v}{L}\right\rfloor,\quad
r_q=\mathbf1_{v-q<0}.
$$


All three lie in $\{0,1\}$, and the relevant residual indices stay within a single four-digit block.

The high factorial ratio after four stripping steps is


$$
\frac{N!}{J!(N-J-e)!}
\frac{(2N+h-J+u)!}{(h-J-r_q)!(2N)!}.
$$


It factors exactly as


$$
F(J)(N-J)^e(2N+h-J+1)^u(h-J)^{r_q},
$$


where


$$
F(J)=\binom NJ\binom{2N+h-J}{h-J}.
$$


No high factorial unit has been discarded.

For the low units,


$$
U_p(pm+s)
\equiv((p-1)!)^m s!(1+pmH_s)\pmod{p^2}.
$$


The full-block correction vanishes because $H_{p-1}=0\pmod p$. In a factorial ratio, the exponent of $(p-1)!$ is the fixed low carry across that stripping level. At the first three levels, the $J$-part of the harmonic quotient is zero modulo $p$; at the fourth it is affine in $J$. Therefore the stripped low unit is


$$
u_0+p(u_1+Ju_2)\pmod{p^2}.
$$



Multiplication by the high factor of degree at most $3$ gives degree at most $4$. This is a genuine polynomial representation, not interpolation at selected $J$.

## 13. Freezing kernel coefficients and extending the finite range

For $1\le i\le58$,


$$
v_p\binom{LJ}{i}\ge4-v_p(i)\ge3.
$$


Vandermonde consequently gives


$$
\binom{x+LJ}{s}\equiv\binom xs\pmod{p^3},
\qquad 0\le s\le58.
$$


With integral Newton coefficients, this permits exactly the coefficient freezing used in turn20. For boundary coefficients linear in $j$, the replacement error contains $LJ$; combined with the negative reconstruction factor it is divisible by $p^5$.

The exact ranges are


$$
0\le J\le h\quad(x\le b_*),\qquad
0\le J\le h-1\quad(x>b_*).
$$


For $x>b_*$, every nonnegative $P$-power has $r_q=1$. Thus its polynomial multiplier contains $h-J$. Extension to $J=h$ adds zero to both the norm and mixed contractions. No assertion that $Q_x$ itself vanishes there is needed.

This verifies the finite-range step at every low index, including newly admitted support.

## 14. Leading polynomial identity and low constants

On the old support $\mathcal X$, the stripping calculation gives polynomial identities


$$
P_x=C_nc(x)\ell_e,\qquad Q_x=\xi(x)\ell_e\pmod p.
$$


Outside $\mathcal X$, the leading $P_x$ is the zero polynomial: its vanishing follows from an extra **low** factor, not from a zero of $F(J)$.

The first contact term vanishes on $\mathcal X$ coefficientwise at its required grade. For the surviving boundary monomials there, $r_q=0$ and $e+u=1$, so their high multiplier is indeed $\ell_e$.

The supplied finite receipts give


$$
(\kappa_0,\kappa_1)=(11,18),\qquad(g_0,g_1)=(26,3).
$$


The arithmetic comparison is correct:


$$
6^{-1}=5,\qquad 5\cdot11=26,\qquad5\cdot18=3\pmod{29}.
$$


Therefore, for $c=(6C_n)^{-1}$,


$$
\sum_x(P_xQ_x-cP_x^2)\equiv0
$$


as a polynomial in $J$. This coefficientwise conclusion is stronger than a pointwise identity after multiplication by $F(J)^2$, and is exactly what the next step needs.

I have not independently recomputed the 9108-case low sums; they remain finite arithmetic inputs.

## 15. Lucas contraction and the whole mixed relation

The residual polynomial has the form


$$
\sum_x(P_xQ_x-cP_x^2)=pR(J)\pmod{p^2}.
$$


Thus


$$
M-cD\equiv p\sum_{J=0}^hF(J)^2R(J)\pmod{p^2}.
$$



Writing $J=pk+t$, a nonzero $F(J)\bmod p$ requires


$$
0\le t\le3,\qquad 0\le d-t\le22.
$$


For these $t$, the exact remaining range is $0\le k\le H$, and


$$
F(pk+t)\equiv
\binom3t B_{d-t}X_k\pmod p.
$$


Since $R(pk+t)=R(t)$, one obtains


$$
\sum_{J=0}^hF(J)^2R(J)
=
T\sum_{\substack{0\le t\le3\\0\le d-t\le22}}
\binom3t^2B_{d-t}^2R(t)\pmod p.
$$


There is no degree restriction on this last contraction identity.

Consequently, on $0\le d\le24,\ T=0$,


$$
M-(6C_n)^{-1}D\equiv0\pmod{p^2},
$$


and hence


$$
M_1=(6C_n)^{-1}D_1.
$$


This is the whole mixed relation, conditional on the stated complete bounded-kernel data—not merely the old-support part.

## 16. Audit of $\beta(d)$ on the assigned locus

For admissible $t$, put $v=d-t$. The first-order binomial expansion has $k$-coefficient


$$
r_t=H_{3-t}-H_t+H_v-H_{v+6}.
$$


Also


$$
\ell_0(pk+t)=v+7+p(2A+H-k),\qquad
\ell_1(pk+t)=3-t+p(A-k).
$$


The $k$-independent corrections multiply $T$ and vanish on $T=0$. The $k$-dependent terms give


$$
D_1=C_n^2\bigl(f(d)T_1+\beta(d)U\bigr),
$$


with


$$
\begin{aligned}
\beta(d)=2\!\!
\sum_{\substack{0\le t\le3\\0\le d-t\le22}}
\binom3t^2B_{d-t}^2
\Big[&
\bigl(11(d-t+7)^2+18(3-t)^2\bigr)\\
&\times(H_{3-t}-H_t+H_{d-t}-H_{d-t+6})\\
&-11(d-t+7)-18(3-t)
\Big].
\end{aligned}
$$


The signs of both derivative terms are correct. For example, at $d=0$, the sole summand gives $\beta(0)=17$, agreeing with the source.

Thus the associated norm formula passes on its stated locus. It does not evaluate any shifted $d=25,\ldots,28$ second mixed digit.

## 17. Endpoint-fibre cancellation — pass

For $x=b_*$, factorial stripping gives


$$
W_{LJ+b_*}/p^3
\equiv5(N-J)\binom NJ\pmod p.
$$


The displayed factorial ratio reduces to $5$: using the listed residues, its numerator and denominator reduce to $7$ and $16$, respectively, so the signed ratio is $-7/16=5\pmod{29}$.

On this fibre, positive powers have an additional final carry. The surviving $P$-coefficient is $1-h_0(27)=14$. For the unit $Q$-boundary, the three coefficient/unit products sum to


$$
-2-24-2=1\pmod{29}.
$$


The higher factorial and contact grades vanish at this fibre’s required precision.

Therefore


$$
\left[\frac Mp\right]_{j=LJ+b_*}
=2C_n(N-J)^2F(J)^2\pmod p.
$$


Summing the **actual** fibre $0\le J\le h$ gives a multiple of $T$, hence zero on $T=0$. Its last term is exactly the endpoint contribution


$$
2C_n(N-h)^2\binom Nh^2
=C_n\eta(d)\binom AH^2.
$$


Thus the source’s interior cancellation formula follows with the correct sign. The endpoint $1+b\theta^Q_{b-1}$ has not been deleted or canceled against an artificial coordinate.

---

# III. Primitive arithmetic and nonvanishing retained

For the weighted determinant family, retain


$$
g=\gcd(|A_{\rm det}|,|B_{\rm det}|).
$$


When $B_{\rm det}\ne0$,


$$
q=\frac{|B_{\rm det}|}{g},\qquad
p=-\frac{\operatorname{sgn}(B_{\rm det})A_{\rm det}}g,
$$


and


$$
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_{\rm det})\ell^{(n+1)/2}}g
\det H_{\rm complete}.
$$


The primitive multiplier is $\ell^{(n+1)/2}/g$. The support audit proves neither $B_{\rm det}\ne0$ nor nonvanishing of the whole determinant error. The transported radical endpoint retains its nonzero residue


$$
((-1)^i)_{0\le i<\nu},
$$


but the first possibly nonzero divided radical and its endpoint image remain unevaluated.

For MAIN29, with the actual falling metric, retain


$$
N_B=d_B[u,v],\quad
A_B=N_{B,1}^T\Omega N_{B,1}>0,\quad
H_B=N_{B,1}^T\Omega N_{B,2},
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$


The primitive multiplier is $1/g_B$ on the integer pair, or $d_B^2/g_B$ on the rational Gram pair. In particular,


$$
v_{29}(q_n)=
\max\{0,\ 2F_n-F_b-1+\delta-\mu\}
$$


is not determined by the audited common-zero results.

The whole error remains


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$


Under the retained complete signed-error theorem, $\epsilon_n>0$ eventually and


$$
\log|\epsilon_n|
=-\left(2+\frac1{2001}\right)n\log(1+\sqrt2)+o(n).
$$


That conditional nonvanishing and sign concern the complete error, including exponential residual, logarithmic force, factorial boundary, and endpoint. They are not consequences of the local congruences.

---

## Closing ledger

### (1) New result and proof status

* **Proved audit result:** A1’s five core support operations close with the stated width budget, actual LOW projection, inverse coefficient valuations, and finite HIGH truncations.
* **Conditional actual result:** the arbitrary fixed-$r$ radical divisibility follows from the stated actual-polynomial approximation and integral unit-block interface; the precision-protection proof passes.
* **Conditional MAIN29 result:** given the stated complete integral bounded kernels and finite low constants, the common-high-factor proof establishes the whole second mixed relation on $0\le d\le24,\ T=0$. The norm $\beta(d)$ formula and actual endpoint-fibre cancellation pass.
* No offending coefficient or boundary was found in either new closure argument. No growing-$r$, exact-denominator, or shifted $25,\ldots,28$ second-digit assertion is made.

### (2) Exact remaining bottleneck

For fully self-contained certification from the actual constructions, the missing inputs are:

* the derivation of the arbitrary-depth approximation $Q^{\rm loc}-Q_c\in3^{v_3(j)+2}\mathbb Z_3[y]$;
* the explicit integral Newton expansions or graded contact-operator proof yielding the asserted effective MAIN29 degrees and supports.

Beyond these interfaces, irrationality still requires control of the **actual final gcd and reduced denominator**, together with nonzero whole primitive errors tending to zero. Fixed-depth saturation and second-depth alignment do not provide that control.

### (3) Computation request

**None.** A new finite rank scan or low-digit enumeration would not resolve the remaining construction-level interfaces or the global denominator problem.
