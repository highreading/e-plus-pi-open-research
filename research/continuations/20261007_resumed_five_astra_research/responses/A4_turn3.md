> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent proof audit: finite multipliers and the repaired integral Cartier evaluator

## 1. Executive findings

The two new candidates address different local problems. Neither evaluates the final all-prime primitive denominator or proves the required comparison with the nonzero whole error.

My findings are:

1. **A1’s finite-multiplier mechanism is valid for the core contraction.** Using only the already accepted width-$20$ core support and the expressly retained producer coefficient, endpoint, and degree-reset information, one obtains
   

$$
T^{T}E_c^{-1}T\in3^5M,
   \qquad
   T_{wi}=\mathcal M(\mathscr R\,wF_i).
$$


   Below I prove this with the original finite polynomial space, an integral unimodular basis, the decomposition error, the LOW inverse loss, and the core-residual term all included.

2. **The passage to the actual contraction has a separate hypothesis.** A1 uses
   

$$
E_{\rm act}-E_c\in3^7M.
   \tag{1.1}
$$


   Its inverse-replacement calculation is correct if (1.1) is established. However, (1.1) is not a consequence merely of the retained producer coefficient, endpoint, and reset theorems, and its defining original-object identity is not displayed in the supplied accepted A4 report. It must be attached explicitly to the retained producer receipts, rather than imported under the label “already proved replacement.”

   Thus:
   - the **core multiplier conclusion is proved** from the permitted support and producer premises;
   - the **actual conclusion**
     

$$
\mathcal Q\in3^6M,\qquad K_{18}=0
$$


     is a proved implication of the additional actual-block perturbation premise;
   - identifying the retained exact producer identity that establishes that premise closes the remaining audit gap. No large computation is needed.

3. **A1’s core boundary scalar calculation is valid.** With the finite top block $E_0$ as the reference lift,
   

$$
V_c=\frac{\widehat E_c-E_0}{3},
$$


   the accepted projection theorem gives
   

$$
\widehat E_{c,dd}\in27\mathbb Z_3,
   \qquad
   V_{c,dd}/3=0\pmod3.
$$



4. **A5’s Euler acceptance identity is correct at its stated nonnegative-exponent scope**, including the exact finite offset tail.

5. **A5’s original denominator transition is false.** The parent’s replacement with the factor $(1-t)^s$ is correct. With this repair, the integral Cartier transition, termination, single-state support bound, exponent-class merging, and union-of-support bound admit algebraic proofs.

6. **The repaired evaluator has no additional whole-sum dyadic clearing loss.** This concerns evaluation of already assembled integral raw expressions. It does not certify the source assembly, actual content $a$, primitive observations, practical production cost, or an infinite-family relative congruence.

7. **The prime-$29$ interpretation correction is adopted without reopening the calculation.** The saved first-column profiles have nonzero counts $414,414,3$, the second-column profiles have counts $0,0,0$, and the five scalar outputs remain zero. The accepted omission accounting remains at its original fixed-layer scope.

The irrationality or rationality of $e+\pi$ is not determined.

---

# Part I. Audit of A1’s finite multiplier

## 2. Original domain and exact finite objects

Retain, without enlargement,


$$
j>0,\qquad j\equiv84645\pmod{531441},
$$




$$
m=2^{2j-1},\qquad n=4^j+1,\qquad A=2m-1,
$$




$$
H=3^{h-1},\qquad D=H-A,
$$


and


$$
\frac1{2C_{16}}<\frac DH<\frac1{C_{16}},
\qquad C_{16}=147968\,3^{15}.
$$



All assertions below concern sufficiently large retained tuples. In particular,


$$
D\ge486,\qquad h\ge22.
$$



The finite polynomials are


$$
U_u=x^u\quad(0\le u<D),\qquad
z_i=x^Dy^i\quad(0\le i<\nu),
$$




$$
Y_b=y^b\quad(d\le b\le m),
$$


where


$$
x=y-1,\qquad \nu=D/2-1,\qquad d=D+\nu.
$$



Set


$$
W=[U\ Y],\qquad
F=Z-WE_c^{-1}C_c,
$$


and


$$
Q_c=(y+1)x^A(\beta+3y),\qquad \beta=-71-A.
$$


The bilinear core form is


$$
G_c(f,g)=\mathcal M(Q_cfg),
$$


with the **complete** functional


$$
\mathcal M(G)=
-\frac{3^h}{4}\mathfrak f(G)
+
3^h\sum_{v=0}^{2n-2}
\frac{[y^v](G-G(-1))/(y+1)}{2v+1}.
$$



The cutoff remains


$$
2v+1\le4n-3=4H-4D+5.
$$


The physical terminal is $Y_m$.

I reuse the accepted conclusions


$$
E_c^{-1}\in3^{-1}M,\qquad
S_c=G_c(F,F)\in3^{21}M,
\tag{2.1}
$$


and


$$
F_i\equiv x^D\psi_i(y)\pmod{3^{20}},
\qquad
\deg\psi_i\le m-D,
\qquad
\operatorname{supp}\psi_i\subseteq I_\Omega(10D),
\tag{2.2}
$$


where


$$
\Omega=H/3^{19}.
$$


Here $I_\Omega(s)$ denotes the integer exponents at distance at most $s$ from $\Omega\mathbb Z$.

This avoids relying on a separately cited precision-$6$ theorem or an unspecified “two-neighbor” calculation.

## 3. The producer representative and its hypotheses

Write


$$
\mathscr R=R_{\rm prod}/3.
$$



The retained coefficient theorem, with its actual division by $3^7$, gives, for $a\le A-19$,


$$
v_3\!\left(\frac{(A+1)!}{a!}\right)
\ge5+v_3(18!)=13.
$$


Indeed,


$$
v_3(18!)=6+2=8.
$$


Thus the retained coefficient formula implies


$$
[x^a]\mathscr R\equiv0\pmod{3^6}
\qquad(a\le A-19).
\tag{3.1}
$$



Use also the retained endpoint congruence


$$
\mathscr R(-1)\equiv0\pmod{3^6}
$$


and the safe degree bound


$$
\deg\mathscr R\le A+2.
$$


After factoring $x^{A-18}$, evaluation at $y=-1$, hence $x=-2$, is evaluation at a $3$-adic unit. Polynomial division by the monic factor $x+2=y+1$ therefore gives


$$
\boxed{
\mathscr R\equiv(y+1)x^{A-18}B(x)\pmod{3^6},
\qquad \deg B\le19.
}
\tag{3.2}
$$



This step is an application of the retained exact producer coefficient and endpoint theorem. It is not justified by factorial valuations alone in the absence of that coefficient formula.

## 4. The finite degree gap

From


$$
m-D=\frac{H-3D+1}{2}
$$


and the fact that $H/\Omega=3^{19}$ is odd, the upper degree endpoint lies near a half-grid point.

Because $10D\ll\Omega/2$, the support condition (2.2) implies


$$
\deg\psi_i\le\frac{H-\Omega}{2}+10D.
$$


Consequently,


$$
\deg(x^D\psi_i)\le m-g,
\qquad
g=\frac{\Omega-23D+1}{2}.
\tag{4.1}
$$



The accepted window gives


$$
\frac{\Omega}{D}>\frac{147968}{81}>1800.
$$


In particular,


$$
g>6,\qquad
21D+7<\frac{\Omega-1}{2}.
\tag{4.2}
$$



These are actual degree bounds for representatives in the original degree-$\le m$ polynomial space. They do not extend HIGH beyond $m$.

## 5. Integral multiplier and integral finite basis

Put


$$
b_0=\beta+3.
$$


Since $b_0\equiv1\pmod3$, define the integral $3$-adic polynomial


$$
T_6(x)=\sum_{a=0}^{5}\frac{(-3x)^a}{b_0^{a+1}}.
$$


Then


$$
(\beta+3y)T_6(x)\equiv1\pmod{3^6}.
\tag{5.1}
$$



Define


$$
H_i=x^{D-18}B(x)T_6(x)\psi_i(y).
$$


It is a polynomial because $D>18$, and


$$
\deg H_i
\le m-g-18+19+5
=m-g+6\le m.
$$


Equations (2.2), (3.2), and (5.1) give the coefficientwise congruence


$$
\boxed{Q_cH_i-\mathscr RF_i\in3^6\mathbb Z_3[y].}
\tag{5.2}
$$



Here “integral” means over $\mathbb Z_3$, not necessarily over $\mathbb Z$; inversion of $b_0$ is a unit operation.

### Why $[W,F]$ is an integral basis

The polynomials


$$
U_0,\ldots,U_{D-1},z_0,\ldots,z_{\nu-1},Y_d,\ldots,Y_m
$$


are monic with distinct consecutive degrees $0,\ldots,m$. Their coefficient matrix is triangular with diagonal $1$. Thus $[W,Z]$, up to ordering, is a unimodular basis of $\mathbb Z_3[y]_{\le m}$.

Moreover, $C_c\in3M$ and $E_c^{-1}\in3^{-1}M$, so $E_c^{-1}C_c$ is integral. Replacing $Z$ by


$$
F=Z-WE_c^{-1}C_c
$$


is an integral block-unipotent basis change.

Therefore every $H_i$ has an integral decomposition


$$
H=WC+FD.
\tag{5.3}
$$


No denominator is hidden in $C$ or $D$.

## 6. Decomposition error, LOW loss, and the residual term

The complete functional is integral on integral polynomials: every retained denominator has $3$-adic valuation at most $h$, and the factorial coefficient $3^h/4$ is integral.

Let


$$
T_{wi}=\mathcal M(\mathscr R\,wF_i).
$$


Complete core orthogonality and (5.2) imply


$$
T=E_cC+\Delta,\qquad \Delta\in3^6M.
$$


Hence


$$
T^TE_c^{-1}T
=
C^TE_cC+C^T\Delta+\Delta^TC+\Delta^TE_c^{-1}\Delta.
$$


The last term has valuation at least


$$
6+6-1=11.
$$


This explicitly pays the possible LOW inverse loss. Therefore


$$
T^TE_c^{-1}T\equiv C^TE_cC\pmod{3^6}.
\tag{6.1}
$$



On the other hand,


$$
G_c(H,H)=C^TE_cC+D^TS_cD.
$$


Since $D$ is integral and $S_c\in3^{21}M$, the residual term vanishes modulo $3^6$. Thus


$$
\boxed{
T^TE_c^{-1}T\equiv G_c(H,H)\pmod{3^6}.
}
\tag{6.2}
$$



This establishes the finite-basis step in A1 without any residual inverse.

## 7. Exclusion of every relevant pole

Modulo $3^6$,


$$
Q_cH_iH_j
\equiv
(y+1)x^{H+D-36}B(x)^2T_6(x)\psi_i(y)\psi_j(y).
$$


After exact endpoint subtraction, the quotient is


$$
x^H C(x)\psi_i(y)\psi_j(y),
\qquad
C=x^{D-36}B^2T_6,
$$


with


$$
\deg C\le D+7.
$$



Modulo $3^5$, the polynomial $x^H$ is supported on multiples of $H/3^4$, hence on the $\Omega$-grid. The other factors have support within


$$
I_\Omega(21D+7).
\tag{7.1}
$$



Every denominator contributing modulo $3^5$ can be written


$$
2v+1=\alpha3^{h-k},
\qquad 0\le k\le4,
$$


with $\alpha$ positive, odd, and prime to $3$, subject to the unchanged finite cutoff. Therefore


$$
v=\frac{\alpha3^{20-k}\Omega-1}{2}.
$$


This is an odd half-grid index relative to $\Omega$. Its distance from $\Omega\mathbb Z$ is at least


$$
\frac{\Omega-1}{2}>21D+7.
$$


Every such extraction vanishes. The factorial term also vanishes modulo $3^5$.

Thus


$$
G_c(H,H)\in3^5M,
$$


and (6.2) proves the new core statement


$$
\boxed{T^TE_c^{-1}T\in3^5M.}
\tag{7.2}
$$



## 8. Actual inverse replacement: valid algebra, separate premise

Suppose the original actual blocks satisfy


$$
E_{\rm act}-E_c\in3^7M.
\tag{8.1}
$$


Since $E_c^{-1}\in3^{-1}M$,


$$
E_c^{-1}(E_{\rm act}-E_c)\in3^6M.
$$


A convergent integral Neumann inverse then gives


$$
E_{\rm act}^{-1}\in3^{-1}M,
\qquad
E_{\rm act}^{-1}-E_c^{-1}\in3^5M.
\tag{8.2}
$$


The retained source normalization $T\in3M$ yields


$$
T^T(E_{\rm act}^{-1}-E_c^{-1})T\in3^7M.
$$


Hence (7.2) passes to the actual inverse.

The normalization is also correct. With


$$
T=3\binom{3a}{\beta_s},
\qquad
\widetilde\beta_s=\beta_s-3X_{\rm act}^TL_{\rm act}^{-1}a,
$$


block elimination gives


$$
3T^TE_{\rm act}^{-1}T
=
81a^TL_{\rm act}^{-1}a+
27\widetilde\beta_s^T\widehat E_{\rm act}^{-1}\widetilde\beta_s
=\mathcal Q.
$$


Therefore, under (8.1),


$$
\boxed{\mathcal Q\in3^6M,\qquad K_{18}=0.}
\tag{8.3}
$$



### Exact audit gap

The supplied A1 text asserts (8.1), but the permitted coefficient/endpoint/reset premises do not themselves establish it. A sufficient original-object identity is


$$
E_{\rm act}-E_c
=
3^6\bigl(\mathcal M(R_{\rm prod}ww')\bigr)_{w,w'\in W},
\qquad R_{\rm prod}=3\mathscr R.
\tag{8.4}
$$


If (8.4) is part of the retained producer receipts, then integrality of $\mathcal M$ immediately proves (8.1), and the actual next-digit conclusion is accepted.

If it is not, the conclusion remains conditional. The repair required is a citation or derivation of (8.4) from the actual producer definition—not a new full-size computation. In fact, a bound $E_{\rm act}-E_c\in3^5M$ would already suffice for the divisibility conclusion.

## 9. Boundary scalar and the next residual layer

Let


$$
g_d=Y_d-UL^{-1}X_d.
$$


The accepted finite projection theorem gives


$$
g_d\equiv x^Dq_d\pmod{27},
\qquad \deg q_d=\nu.
$$


Thus


$$
\widehat E_{c,dd}
\equiv
\mathcal M\!\left((y+1)x^{H+D}(\beta+3y)q_d^2\right)
\pmod{27}.
$$



The endpoint-subtracted polynomial has degree


$$
H+D+1+2\nu=H+2D-1<r_*.
$$


The top extraction is absent. Modulo $27$, $x^H$ is supported on the $H/9$-grid; the other factor has degree at most $2D-1$. All remaining relevant poles lie on the corresponding odd half-grid and are separated by the original window. Therefore


$$
\widehat E_{c,dd}\equiv0\pmod{27}.
$$



For the finite top block,


$$
(E_0)_{dd}=0,
$$


since its Toeplitz coefficient index is $d-m<0$. Consequently


$$
\boxed{V_{c,dd}/3=0\pmod3.}
$$



A1’s separate sensitivity formulas cite A1 turn3, which is not supplied as an independently retained theorem here. Their degree and support cancellations are compatible with the accepted geometry, but their exact sensitivity identities should not be promoted solely from those citations. They are unnecessary for the multiplier proof above.

If (8.4) is confirmed, the already accepted exact Schur identity gives the additional consequence


$$
S_{\rm act}=S_c+3^6\Phi_R-3^{13}\mathcal Q\in3^{19}M.
$$


The next complete normalization is then


$$
\Upsilon_{19}=-S_{\rm act}/3^{19},
$$


with


$$
\Upsilon_{19}\equiv\mathcal Q/3^6\pmod9.
$$


The zero $K_{18}$ has full radical $\mathbb F_3^\nu$ and zero-dimensional nondegenerate complement. It does not evaluate the next form or the distinguished endpoint/diagonal pair.

---

# Part II. Audit of A5’s repaired evaluator

## 10. Original family and source scope

This part uses the different original family


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


Contact coordinates remain $0\le j<b$; physical reconstruction remains $0\le j\le b$.

The exact corrected columns are


$$
x=\frac12\mathcal RA^{-1}\mathfrak f,
\qquad
y=\frac{\mathcal RA^{-1}(h^e+h^F)+e_0}{4b!}.
$$


The complete logarithmic forcing, factorial subtraction, both differential boundary charges, finite Schur returns, and the separate physical terminal are not replaced by the evaluator.

The raw quantities are


$$
\mathcal U=
\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)^2
+b^2W_b^2(z^f_{b-1})^2,
$$


and


$$
\mathcal V=
\sum_{j=0}^{b-1}W_j^2(\Delta_jz^f)(\Delta_jz^k)
+b^2W_b^2z^f_{b-1}z^k_{b-1}
+bW_b^2z^f_{b-1}.
\tag{10.1}
$$



The source-to-profile formulas are reused only at their previously established filtration scope. The seven new kernel tests do not prove those formulas or their source coefficients.

## 11. Euler acceptance and the exact finite tail

For one assembled kernel, order the factors so that


$$
\varepsilon_1\le\varepsilon_2,\qquad
\delta=\varepsilon_2-\varepsilon_1.
$$


Put


$$
N=n+2,\qquad A=2n+a_1,\qquad B=2n+a_2,
\qquad a_i=\eta_i-\varepsilon_i.
$$



Under $A-\delta\ge0$ and $B\ge0$,


$$
\sum_{k\ge0}
\binom{A+k}{k}\binom{B+k+\delta}{k+\delta}t^k
=
\frac{\sum_{\ell\ge0}\binom{A-\delta}{\ell}
\binom{B+\delta}{\ell+\delta}t^\ell}
{(1-t)^{A+B+1}}.
\tag{11.1}
$$


For example, dividing by $\binom{B+\delta}{\delta}$ identifies the left side with


$$
{}_2F_1(A+1,B+\delta+1;\delta+1;t).
$$


Euler’s transformation gives numerator parameters $\delta-A,-B$, and restoring the scalar gives exactly the integral numerator in (11.1). This proves the identity over $\mathbb Q[[t]]$, hence coefficientwise over the integers.

The constant-term representations in A5 follow directly from binomial expansion. Their product gives the stated coefficient acceptance formula.

The finite cutoff requires care. With $r=b-j$, the physical range is $r\ge1$, and $k=r+\varepsilon_1$.

- If $\varepsilon_1<0$, the omitted smaller physical $r$-values have negative lower binomial index and vanish.
- If $\varepsilon_1\ge0$, the extension introduces precisely $k=0,\ldots,\varepsilon_1$.

Thus the correction is exactly


$$
\mathcal T_{\rm off}
=
\sum_{k=0}^{\varepsilon_1}
\binom N{b+\varepsilon_1-k}^{2}
\binom{b+\varepsilon_1-k}{d}
\binom{A+k}{k}
\binom{B+k+\delta}{k+\delta},
$$


when $\varepsilon_1\ge0$, and zero otherwise.

This proves the finite acceptance identity, not merely an infinite convolution identity. In the original assembled range, A5’s condition


$$
n>4(I+2m+T+4)+2
$$


ensures the required nonnegative exponents. Also $\varepsilon_1\ge-I-1\ge-b$, so the target $b+\varepsilon_1$ is nonnegative.

## 12. Correct denominator transition

The original identity


$$
(1-t)^2=(1-t^2)-2t
$$


is false. Consequently A5’s original $K_0$, original transition, and claims proved through that transition are not valid as written.

The repaired identity starts from


$$
(1-t)^2=(1-t^2)-2t(1-t).
$$


For $M=2h+\epsilon$,


$$
(1-t)^{-2h}
=
(1-t^2)^{-h}
\left(1-\frac{2t(1-t)}{1-t^2}\right)^{-h}.
$$


Expanding the negative-binomial series and discarding $s\ge L$ gives


$$
(1-t)^{-M}\equiv
\frac{(1+t)^\epsilon K_0^{\rm rep}(t)}
{(1-t^2)^{h+\epsilon+L-1}}
\pmod{2^L},
$$


where


$$
K_0^{\rm rep}(t)=
\sum_{s=0}^{L-1}
2^s\binom{h+s-1}{s}
t^s(1-t)^s(1-t^2)^{L-1-s}.
\tag{12.1}
$$


The $h=0$ convention is correct.

Each summand before the optional odd factor has degree


$$
s+s+2(L-1-s)=2L-2.
$$


Thus the repaired denominator multiplier still has degree at most


$$
J=2L-1.
$$



This proves the repair algebraically. The parent’s $M=2,L=2$ counterexample correctly distinguishes the original coefficient $1$ from the required coefficient $3$ at $t^2\bmod4$.

## 13. Closure and termination

The numerator transition follows from


$$
(1+v)^{2h}=((1+v^2)+2v)^h.
$$


Truncating terms with at least $L$ factors of $2$ proves A5’s numerator identity without division by $2$.

After inserting all five repaired multiplier polynomials, the remaining large factors depend only on $t^2,X^2,Y^2$. For any such factor $G$,


$$
\mathcal C_{\mathbf e}\bigl(P\,G(t^2,X^2,Y^2)\bigr)
=
\mathcal C_{\mathbf e}(P)\,G(t,X,Y).
$$


This identity is valid for Laurent exponents in $X,Y$, and proves shift closure.

The numerator exponents satisfy


$$
N_i'=\max\{\lfloor N_i/2\rfloor-(L-1),0\}.
$$


They therefore eventually become zero. The target is repeatedly halved and also becomes zero. The denominator exponent need not become zero.

All numerator polynomials retain nonnegative $t$-exponents. Therefore, once the four $N_i$ and the target vanish,


$$
[t^0X^0Y^0]\frac{P}{(1-t)^M}
=[t^0X^0Y^0]P.
$$


This proves terminal acceptance. A zero polynomial can of course terminate earlier.

## 14. Support and merging bounds

Each numerator multiplier has degree at most $J$ in its monomial direction; the repaired denominator multiplier has degree at most $J$ in $t$.

### Single state

Multiplication enlarges either Laurent-coordinate width by at most $2J$. Cartier extraction halves exponents, so


$$
w_X'\le\lfloor w_X/2\rfloor+J,
\qquad
w_Y'\le\lfloor w_Y/2\rfloor+J.
$$


Starting at width zero gives


$$
w_X,w_Y\le2J.
$$


Similarly,


$$
\deg_tP'\le\left\lfloor\frac{\deg_tP+3J}{2}\right\rfloor,
$$


hence $\deg_tP\le3J$.

The accepted single-state bound is therefore


$$
\boxed{(3J+1)(2J+1)^2=(6L-2)(4L-1)^2.}
$$



### Exponent classes

The update maps are


$$
N\mapsto\max\{\lfloor N/2\rfloor-(L-1),0\},
$$




$$
M\mapsto\lceil M/2\rceil+L-1,
\qquad
B_{\rm tar}\mapsto\lfloor B_{\rm tar}/2\rfloor.
$$


Each maps an integer interval of width $w$ into one of width at most $\lceil w/2\rceil$.

Using the original assembled spreads, after


$$
t_0=\left\lceil\log_2\max(2r_f,r_f+\Delta_\varepsilon)\right\rceil
$$


each of the five varying entries has at most two values. The sixth entry, $N_2$, is common initially and remains common. Thus there are at most $32$ exponent/target classes.

### Union of supports

This requires more than linearity. Across the entire initial collection, the $X$-exponents range over $[0,2r_f]$, and the $Y$-exponents over $[0,\Delta_\varepsilon]$. At every step, all multipliers move either Laurent coordinate only within $[-J,J]$. Hence the **global union width** obeys the same recurrence


$$
w'\le\lfloor w/2\rfloor+J.
$$


After $t_0$ steps,


$$
w_X,w_Y\le2J+1.
$$


The global $t$-degree remains at most $3J$. Therefore the union, and consequently each merged class, has at most


$$
\boxed{(3J+1)(2J+2)^2=(6L-2)(4L)^2}
$$


possible positions.

This supplies the missing explicit justification for A5’s moving-center assertion. It remains invariant under subsequent transitions.

At $L=32$, the stated values $r_f=379$, $\Delta_\varepsilon=567$ give $t_0=10$.

## 15. What survives the repair

The repaired evaluator uses integral additions, multiplications, and coefficient selection modulo $2^L$. Therefore


$$
e_{\rm sum}=0
$$


is correct for evaluating the assembled raw pair.

This does not erase:


$$
L_Q=K+2a+2,\qquad L_E=K+a+3,
$$


or the paid relative identity


$$
E-rQ=2^{-2a-3}(2^a\mathcal V-2r\mathcal U).
$$


Short-binomial computations must still pay their factorial divisions using sufficient parameter precision.

Both physical terminal terms in $\mathcal V$ remain:


$$
b^2W_b^2z^f_{b-1}z^k_{b-1}
\quad\text{and}\quad
bW_b^2z^f_{b-1}.
$$


The offset tail removes the artificial contact contribution; it does not replace the physical terminal by the auxiliary value $z_b^k=-1$.

The polynomial support and line-convolution description support polynomial per-shift arithmetic bounds. They do not certify a practical full source assembly, its memory use, or the cost of obtaining source coefficients from the original parameter word.

---

# Part III. Certificates, remaining obligations, and global arithmetic

## 16. Finite evidence

The seven parent tests are accepted as reported auxiliary finite comparisons of the repaired kernel evaluator. Their direct residues are


$$
16,\ 0,\ 0,\ 0,\ 0,\ 0,\ 10
$$


at the stated moduli, with zero differences.

All reported tail residues happen to be zero. Thus these computations are not independent evidence of a nonzero modular tail cancellation; the tail theorem is justified by the exact convolution argument above.

No rerun of these tests, the closed prime-$29$ assembly, or the old producer calculations is requested.

The prime-$29$ correction is final for this audit: nonzero first-column profiles coexist with the five zero aggregate coefficients. Nothing here revives the withdrawn six-zero-profile interpretation.

## 17. Concrete follow-on obligations

### Prime $3$

First attach the exact actual-block perturbation identity (8.4), or an equivalent proved bound at precision $3^5$ or better, to the retained producer normalization.

Once that is done, the next substantive lemma is:

> **Complete next-residual lemma.** Evaluate
> 

$$
> K_{19}=(\mathcal Q/3^6)\bmod3
>
$$


> using the actual inverse and complete corrected columns; determine its full radical and the transported endpoint/diagonal observation. Any subsequent Schur reduction must include the complete bordered diagonal term.

The finite multiplier closes the previous digit under the stated perturbation premise; it does not supply this next observation.

### Prime $2$

A concrete remaining lemma is:

> **Actual assembled observable lemma.** Starting from the complete source-dependent two-channel states, including all offset tails and both physical terminal terms, prove a specified acceptance congruence for
> 

$$
> 2^a\mathcal V-2r(u)\mathcal U
>
$$


> at modulus $2^{K+2a+3}$, or prove a specified nonzero primitive digit, on an explicit infinite subdomain of $b=9^{18+32u}$.

The repaired transition gives a finite integral evaluation mechanism. It does not determine that observable or the actual content $a$.

### Bounded arithmetic needed now

**No new bounded calculation is essential to the algebraic audit.** The outstanding prime-$3$ issue is an original-object identity, not a numerical test. The corrected Cartier identities and support bounds have been proved symbolically.

If a coordinator elects to inspect the perturbation identity at one tuple, the inputs must be the exact original $j,h$, the actual finite producer polynomial, and the original $W$-indexed blocks; the expected output is entrywise verification of (8.4). Such a calculation establishes only that tuple and is not a substitute for the defining identity.

## 18. Actual primitive arithmetic and same-index error

For the determinant construction, retain the actual contents, multiplier, and least simultaneous clearer:


$$
A_\ell=\ell_{\rm clr}^{m+1}\beta_0,\qquad
B_\ell=\ell_{\rm clr}^{m+1}\beta_1,
$$




$$
g_\ell=\gcd(|A_\ell|,|B_\ell|)
$$


over all primes. When $B_\ell\ne0$,


$$
q=\frac{|B_\ell|}{g_\ell},
\qquad
p=-\frac{\operatorname{sgn}(B_\ell)A_\ell}{g_\ell},
$$


and


$$
q(e+\pi)-p
=
\frac{\operatorname{sgn}(B_\ell)\ell_{\rm clr}^{m+1}}{g_\ell}
\det H_{\rm complete}.
$$



For the weighted construction, preserve the actual least simultaneous clearer


$$
d_B=\operatorname{lcm}_{0\le j\le b}
\{\operatorname{den}(u_j),\operatorname{den}(v_j)\},
$$


with no reconstructed row-content division. Writing $N=x^Tx$, $H=x^Ty$,


$$
A_B=d_B^2\,4\Lambda^2R^2N,\qquad
H_B=d_B^2\,8\Lambda Rb!H,
$$




$$
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
$$


Again, $g_B$ is the all-prime final gcd.

The whole error is


$$
q_n(e+\pi)-p_n=-q_n\epsilon_n.
$$


The retained nonzero signed-error result must be used only at its stated original-index scope. What is still missing is an all-prime estimate for the **actual primitive denominator** strong enough to prove


$$
0<|q_n\epsilon_n|\longrightarrow0
$$


on the **same infinite original indices**.

Local cancellation at $2$, $3$, or $29$ does not establish this comparison.

## 19. Final proof-status ledger

| Statement | Audit status |
|---|---|
| Integral finite basis $[W,F]$ | Proved from accepted blocks |
| Degree-$\le m$ multiplier | Proved using accepted width-$20$ support |
| Decomposition error, LOW loss, residual term | Fully accounted for |
| $T^TE_c^{-1}T\in3^5M$ | New proved conclusion |
| Core boundary scalar $V_{c,dd}/3=0\bmod3$ | Proved |
| Actual inverse replacement | Correct under explicit actual-block perturbation premise |
| $\mathcal Q\in3^6M,\ K_{18}=0$ | Proved implication; perturbation premise must be attached to retained original-object receipts |
| Euler coefficient identity and finite tail | Proved at stated exponent scope |
| Original A5 denominator identity | False |
| Parent’s repaired denominator transition | Proved |
| Repaired closure, termination, support, merging, union bound | Proved |
| Additional whole-sum dyadic loss $0$ | Proved for integral assembled raw expressions |
| Actual source assembly and primitive content | Not certified by the new finite tests |
| Infinite-family primitive relative observation | Open |
| All-prime primitive denominator versus whole same-index error | Open |

The new rigorous advances are the explicit finite-core multiplier proof and the repaired, fully bounded integral Cartier evaluation theorem. The exact local gaps are the original-object actual-block perturbation receipt at prime $3$, followed by the next residual observation, and the source-dependent primitive acceptance value at prime $2$.



$$
\boxed{\text{No unconditional proof of rationality or irrationality of }e+\pi
\text{ has been obtained.}}
$$


