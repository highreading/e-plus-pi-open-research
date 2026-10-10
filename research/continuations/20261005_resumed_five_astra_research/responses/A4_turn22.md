> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 22 — Independent audit of the fixed-denominator lifts, endpoint Schur reduction, and recurrence-kernel receipt

## Executive assessment

The supplied work does **not** establish rationality or irrationality of $e+\pi$. It does establish useful exact reductions, whose scopes must remain separate.

My principal conclusions are:

1. **A5turn19’s three rational lifts are correct**, including their coefficient targets, finite upper boundary, and ordinary power-series expansion convention. Their stated denominator degrees are correct.

2. **The displayed prime-power Cartier transition is correct.** In particular, the negative-binomial exponent is
   

$$
\ell=\left\lceil\frac{a+1}{2}\right\rceil,
$$


   the denominator-padding factor is $Q^{a+1-\ell}$, and layer $a$ needs precision only modulo $2^{M-a}$.

3. **The common upper index $N_0=n+2$ permits a genuine simplification:** the two weight-marker variables can be replaced by one. This reduces the upper lift from eight variables to seven, and the lower and boundary lifts from seven to six, without changing any summation endpoint or coefficient value. This is an exact reduction, not a feasibility theorem.

4. **The dense twenty-bit numerical inequalities are correct.** One terminology correction is needed: layer $a=19$ is the *largest-degree, lowest-precision* layer, not the highest-precision layer. Dense storage estimates are implementation costs, not lower bounds for every possible algorithm.

5. **The $76\times76$ endpoint formulas are consistent with the accepted finite factorization.** The interval $b-152\le j\le b-1$, maximum lower binomial index $227$, and stated summand counts are correct. The transpose claim is correct only with the corresponding adjoint factor grouping explicitly preserved.

6. **The new recurrence source passes a mathematical audit at its stated auxiliary scope.** Its impulse-polynomial shifts and degree bound are correct. The source cutoff is complete modulo $29^K$, and its finite recurrence ends at state $b-1$, not $b$. The receipt reports 260 source checks **and** 260 particular-output checks, plus 52 impulse-product checks and 522 propagation checks. These are not original Gram computations.

No tools were executed, no files or external endpoints were accessed, and no hashes or computational results were independently reproduced. The literature and previously accepted results are reused only at their stated mathematical scope.

---

## 1. Original domains and proof dependencies

For the binary work, retain


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


The requested original specialization is


$$
b=150094635296999121,\qquad
n=600678730458590482242,
$$


with


$$
M=20,\qquad q=2^{20},\qquad m=76,\qquad N_0=n+2.
$$



Contact coordinates remain $0,\ldots,b-1$, while reconstruction includes $b$. In particular, the final contact block in


$$
b=128D+81
$$


is shortened, and $j=b$ is a separate reconstructed endpoint.

For the $29$-adic family, retain the distinct original domain


$$
b=3^{249005515+574312172u},\qquad n=2001b,\qquad u\ge0.
$$


The auxiliary pairs $(29,57)$ and $(203,203)$ in the new receipt are not replacements for that family.

The accepted operator/particular-input commutator certificate is not reopened. Its scope remains the specified operator and the particular input $(1+x)^{-n}$, not arbitrary weighted inputs or complete Gram outputs.

---

# Part I. Fixed-denominator rational lifts

## 2. Upper transform: coefficient target and finite boundary

Write


$$
W_j=\binom{N_0}{j},\qquad
K_{a,c}(j)=W_{j+a}W_{j+c}\binom{2n+j}{b}.
$$


The finite transform is


$$
(\mathcal T_UK_{a,c})(i)
=\sum_{k=0}^{b-1-i}\binom{-n}{k}K_{a,c}(i+k),
\qquad 0\le i<b.
$$



For


$$
Q_U=
(1-A(1+U))(1-B(1+V))(1-C(1+Z))
(1+(1+Z)Y-T)(1-UVY),
$$


the claimed extraction is correct:


$$
\begin{aligned}
(\mathcal T_UK_{a,c})(i)
={}&[U^{b-1+a}V^{b-1+c}Z^bY^{b-1-i}\\
&\hspace{19mm}A^{N_0}B^{N_0}C^{2n+i}T^{n-1}]\,Q_U^{-1}.
\end{aligned}
$$



Indeed, extracting $A,B,C,T$ leaves


$$
\frac{(1+U)^{N_0}(1+V)^{N_0}(1+Z)^{2n+i}}
{(1-UVY)(1+(1+Z)Y)^n}.
$$


For $B_i=b-1-i$,


$$
[Y^{B_i}]
\frac1{(1-UVY)(1+(1+Z)Y)^n}
=
\sum_{k=0}^{B_i}(UV)^{B_i-k}\binom{-n}{k}(1+Z)^k.
$$


The remaining extractions give exactly


$$
W_{i+k+a}W_{i+k+c}\binom{2n+i+k}{b}.
$$



Thus:

- $k\le b-1-i$ is encoded exactly;
- no infinite upper endpoint is substituted;
- no Laurent-series ambiguity is introduced;
- no binomial coefficient is divided out.

For integral shifts, use the usual zero convention for binomial lower indices outside their range and for negative ordinary coefficient targets. That convention covers shifted channels with vanishing targets.

### Expansion convention

Every denominator factor has constant term $1$. Consequently $Q_U^{-1}$ is a well-defined element of the ordinary multivariate formal power-series ring. Marker extraction is legitimate coefficient extraction in that ring; it is not evaluation at a nonzero point.

### Degrees

In the stated variable order,


$$
\deg_{\rm coord}Q_U=(2,2,2,2,1,1,1,1).
$$


The factor total degrees are $2,2,2,2,3$, so


$$
\deg Q_U=11.
$$



**Verdict:** correct.

---

## 3. Lower and boundary lifts

### 3.1 Lower transform

The finite transform is


$$
(\mathcal T_LK_{a,c})(j)
=\sum_{i=0}^j(-1)^{j-i}\binom jiK_{a,c}(i).
$$


With


$$
Q_L=
(1-A(1+U))(1-B(1+V))(1-C(1+Z))
(1-T(1+Z-UV)),
$$


marker extraction gives


$$
(1+U)^{N_0}(1+V)^{N_0}(1+Z)^{2n}
(1+Z-UV)^j.
$$


Expanding its last factor as


$$
\sum_{r=0}^j\binom jr(-UV)^r(1+Z)^{j-r}
$$


and setting $i=j-r$ verifies the target


$$
[U^{j+a}V^{j+c}Z^b A^{N_0}B^{N_0}C^{2n}T^j]Q_L^{-1}.
$$



The multidegree and total degree are respectively


$$
(2,2,2,1,1,1,1),\qquad 9.
$$



### 3.2 Boundary pairing

For $0\le h,k<b$,


$$
p_h(j)=(-1)^{h-j}\binom hj
$$


has support $0\le j\le h$. Hence


$$
\mathcal B^{a,c}_{h,k}
=(-1)^{h+k}\sum_j\binom hj\binom kjW_{j+a}W_{j+c}.
$$



With


$$
Q_B=
(1-A(1+U))(1-B(1+V))(1-C(1+Z))
(1-T(UV+Z)),
$$


marker extraction leaves


$$
(1+U)^{N_0}(1+V)^{N_0}(1+Z)^k(UV+Z)^h.
$$


The term indexed by $j$ in the last factor is


$$
\binom hj(UV)^{h-j}Z^j.
$$


The $Z^k$ extraction contributes $\binom{k}{j}$, and the weight targets contribute $W_{j+a}W_{j+c}$. This verifies the displayed formula and sign.

Its multidegree is again $(2,2,2,1,1,1,1)$, with total degree $9$.

These formulas retain the actual high boundary degrees


$$
b-76\le h,k\le b-1.
$$



**Verdict:** both lifts are correct.

---

## 4. Exact common-upper-index reduction

The independent markers $A,B$ are unnecessary because their target exponents are equal. The elementary identity


$$
[D^{N_0}]\frac1{1-D(1+U)(1+V)}
=(1+U)^{N_0}(1+V)^{N_0}
$$


replaces both weight-marker factors.

Define


$$
\begin{aligned}
\widetilde Q_U={}&
(1-D(1+U)(1+V))(1-C(1+Z))\\
&\quad\cdot(1+(1+Z)Y-T)(1-UVY),\\
\widetilde Q_L={}&
(1-D(1+U)(1+V))(1-C(1+Z))
(1-T(1+Z-UV)),\\
\widetilde Q_B={}&
(1-D(1+U)(1+V))(1-C(1+Z))
(1-T(UV+Z)).
\end{aligned}
$$



Then the three exact targets become


$$
\begin{aligned}
\mathcal T_UK_{a,c}(i)
={}&[U^{b-1+a}V^{b-1+c}Z^bY^{b-1-i}
D^{N_0}C^{2n+i}T^{n-1}]\widetilde Q_U^{-1},\\
\mathcal T_LK_{a,c}(j)
={}&[U^{j+a}V^{j+c}Z^bD^{N_0}C^{2n}T^j]
\widetilde Q_L^{-1},\\
\mathcal B^{a,c}_{h,k}
={}&(-1)^{h+k}
[U^{h+a}V^{h+c}Z^kD^{N_0}C^kT^h]
\widetilde Q_B^{-1}.
\end{aligned}
$$



The improved degree data are


$$
\begin{array}{c|c|c|c}
&\text{variables}&\text{coordinate degrees}&\text{total degree}\\ \hline
\widetilde Q_U&7&(2,2,2,2,1,1,1)&10\\
\widetilde Q_L,\widetilde Q_B&6&(2,2,2,1,1,1)&8.
\end{array}
$$



This is a rigorous reduction of one variable and one unit of total degree.

It does **not** justify identifying $U$ and $V$. Those variables still select two separate lower binomial indices. Substitution $U=V$ would generally conflate the required coefficient with other coefficients having the same combined degree. Symmetry alone also does not supply a smaller exact coefficient-extraction scheme for all shifted channels.

---

# Part II. Prime-power Cartier transition and complexity

## 5. Transition audit

Let $Q(0)=1$, with coordinate degree bounds $d_i$, and set


$$
E=\frac{Q(\boldsymbol x)^2-Q(\boldsymbol x^2)}2\in\mathbb Z[\boldsymbol x].
$$


Integrality follows from the characteristic-two Frobenius congruence.

Represent the series modulo $2^M$ by


$$
F=\sum_{a=0}^{M-1}2^a\frac{P_a}{Q^{a+1}},
\qquad
\deg_{x_i}P_a\le(a+1)d_i.
$$


The numerator $P_a$ is stored modulo $2^{M-a}$.

Put


$$
\ell=\left\lceil\frac{a+1}{2}\right\rceil.
$$


Then


$$
Q^{-a-1}=Q^{2\ell-a-1}(Q^2)^{-\ell},
$$


where $2\ell-a-1\in\{0,1\}$. Therefore


$$
(Q^2)^{-\ell}
\equiv
\sum_{j=0}^{M-a-1}
(-2)^j\binom{\ell+j-1}{j}
\frac{E^j}{Q(\boldsymbol x^2)^{\ell+j}}
\pmod{2^{M-a}}.
$$



Applying Cartier and padding to denominator $Q^{a+j+1}$ gives the stated contribution to layer $a+j$:


$$
\boxed{
(-1)^j\binom{\ell+j-1}{j}
\Lambda_{\boldsymbol\epsilon}
\!\left(P_aQ^{2\ell-a-1}E^j\right)
Q^{a+1-\ell}.
}
$$



Every exponent and precision in this formula is correct.

### Degree preservation

Before Cartier, the degree in coordinate $i$ is at most


$$
(a+1)d_i+(2\ell-a-1)d_i+2jd_i
=2(\ell+j)d_i.
$$


After Cartier it is at most $(\ell+j)d_i$; padding adds
$(a+1-\ell)d_i$. Thus the output lies in the required box


$$
\deg_{x_i}\le(a+j+1)d_i.
$$



Processing all binary digits of the **full nonnegative coefficient target** leaves the desired coefficient as the constant term


$$
\sum_{a=0}^{M-1}2^aP_a(0)\pmod{2^M}.
$$



The same proof applies to the reduced denominators $\widetilde Q$.

---

## 6. Numerical dense-box audit

For the original upper lift, the last layer has exactly


$$
41^4\,21^4=549\,556\,825\,041
$$


slots. Consequently


$$
20\cdot41^4\,21^4
=10\,991\,136\,500\,820<1.1\cdot10^{13}.
$$


Its one-bit packed storage alone exceeds $62.5$ decimal GB.

The transition intermediate bound $40d_i$ is valid, giving the box


$$
81^4\,41^4>10^{14}
$$


slots. Four bytes per slot would exceed $400$ decimal TB.

For each original seven-variable lift,


$$
41^3\,21^4=13\,403\,825\,001,
$$


and


$$
20\cdot41^3\,21^4
=268\,076\,500\,020<2.7\cdot10^{11}.
$$



All displayed inequalities are correct.

### Terminology correction

The last layer $a=19$ is the **largest-degree layer**, but it needs only one bit per coefficient. The highest-precision layer is $a=0$, stored modulo $2^{20}$.

### Effect of the common-marker reduction

For the reduced upper lift,


$$
\widetilde R_U
=\sum_{t=1}^{20}(2t+1)^4(t+1)^3,
$$


and the last layer has


$$
41^4\,21^3=26\,169\,372\,621
$$


slots.

For the reduced lower and boundary lifts,


$$
\widetilde R_6
=\sum_{t=1}^{20}(2t+1)^3(t+1)^3,
$$


with last layer


$$
41^3\,21^3=638\,277\,381
$$


slots.

These are substantial reductions, but they still do not prove practical feasibility of the complete calculation.

The upper bounds


$$
R_M=\sum_{t=1}^M\prod_i(td_i+1),\qquad
B_M=\sum_{t=1}^M(M+1-t)\prod_i(td_i+1)
$$


correctly bound coefficient slots and representation bits. The resulting $2^{B_M}$ is an upper bound on possible representations, not a count of distinct rational-series states or reachable states.

The claim of at most 71 target bits is valid for the displayed original first-layer targets and the bounded shifts contemplated here; it should not be read as a statement for arbitrarily large unrestricted shifts $a,c$.

**No impossibility conclusion follows from these dense boxes.** Sparse support, factorized arithmetic, streaming, target-specific quotients, or other exact representations may cost much less.

---

## 7. Primary-method overlap and its limits

The Cartier extraction mechanism belongs to the established prime-power rational-series/diagonal toolkit associated with the cited Rowland–Yassawi work and related literature. It should not be presented as a new automaticity theorem.

The source-specific contributions are:

- explicit rational lifts for these actual weighted finite kernels;
- coefficient targets that retain their original endpoints;
- explicit layer-degree bookkeeping;
- the common-marker simplification above.

The distinction from a generic automaticity application is important. The original powers $n,b$ have been moved into coefficient targets of fixed rational functions, but the complete problem still includes divided-power descendants, finite contact inversion, endpoint Schur corrections, full forcing, and weighted contractions.

Neither the cited primary methods nor newer state-complexity results, without a verified specialization and cost analysis, prove that this complete collection has a small reachable representation.

No external literature or archive search was performed here; there is no exhaustive novelty claim.

---

# Part III. Actual endpoint Schur computation

## 8. Entries, interval, and maximal lower index

Use the accepted finite factorization


$$
A\equiv LU(H+F\overline K E)U\pmod q,
$$


where $E$ selects $b-76,\ldots,b-1$.

The supplied endpoint matrix is


$$
S_{\rm end}=I_{76}+G\overline K,\qquad G=EH^{-1}F.
$$



For $0\le r,t<76$,


$$
\overline K_{r,t}
=
\lambda_{76+r-t}\binom{b+r}{76+r-t},
$$


with support


$$
1\le76+r-t\le76.
$$


Equivalently, its potentially nonzero entries satisfy $r\le t$.

The inverse band formula gives


$$
G_{t,r}
=
\sum_{s=0}^{76}
c_s\binom{b-76+t}{s}F_{b-76+t-s,r}.
$$


The minimum index used here is $b-152$, and the maximum is $b-1$. Thus the exact required interval is


$$
\boxed{b-152\le j\le b-1.}
$$



On that interval,


$$
F_{j,r}
=
-\sum_{v=0}^r
\binom{-n}{b+v-j}\binom n{r-v}.
$$


Its largest lower index is


$$
b+75-(b-152)=227.
$$


All other lower indices are at most $76$ or $75$.

**Verdict:** the interval and maximum $227$ are correct. This remains a finite original-index boundary computation.

---

## 9. Primal/adjoint orientation

Let


$$
M_0=H+F\overline K E.
$$


For a primal solve $M_0x=y$, introduce $z=Ex$. Then


$$
x=H^{-1}y-H^{-1}F\overline K z
$$


and


$$
(I+G\overline K)z=EH^{-1}y.
$$


This proves the stated primal orientation.

For the adjoint,


$$
M_0^T=H^T+E^T\overline K^TF^T.
$$


Use the adjoint boundary variable


$$
\eta=\overline K^TF^Tx.
$$


Then its endpoint matrix is


$$
I+\overline K^TF^TH^{-T}E^T
=I+\overline K^TG^T
=S_{\rm end}^T.
$$



There is an important qualification: using instead the adjoint variable $F^Tx$ produces


$$
I+G^T\overline K^T=(I+\overline K G)^T,
$$


which is generally **not** $S_{\rm end}^T$.

Thus the transpose comparison must document the low-rank factor grouping. Reversing the two $76\times76$ factors without changing boundary variables is an error.

---

## 10. Cost and invertibility

The stated direct counts are correct:


$$
152\cdot76=11552
$$


stored $F$-entries,


$$
152\sum_{r=0}^{75}(r+1)=444752
$$


summands for $F$,


$$
76^2\cdot77=444752
$$


for $G$, and


$$
76^3=438976
$$


for the final product. The total is


$$
1\,328\,480<1.4\text{ million}
$$


contraction summands, before inversion.

Exact small-lower-index binomial recurrences are division-safe when computed over the integers before reduction. Modular implementations must instead separate valuations and invert only units.

Since every potentially nonzero $\lambda_s$ here has $s>0$,


$$
\overline K\equiv0\pmod2,\qquad
S_{\rm end}\equiv I\pmod2.
$$


Invertibility modulo $2^{20}$, and unit-pivot elimination in the natural order, follow.

No completed endpoint matrix or inverse is supplied in this packet. Its computation is a proposed exact bounded certificate, not an already verified output and not a Gram certificate.

---

# Part IV. New recurrence-kernel source

## 11. Impulse polynomials: degree and shifts

The recurrence coefficients, written in the final index $j=i+1$, are


$$
\begin{aligned}
A(j)&=2n+2j-1,\\
B(j)&=\frac{(n+j-1)(n+3j-4)}2,\\
C(j)&=\frac{(n+j-1)(n+j-2)(2-j)}2.
\end{aligned}
$$


The source implements these correctly.

For


$$
q_d(j)=e_1^TT_{j-1}\cdots T_{j-d}e_1,\qquad q_0(j)=1,
$$


the exact recurrence is


$$
\boxed{
q_d(j)=
A(j)q_{d-1}(j-1)
-B(j)q_{d-2}(j-2)
-C(j)q_{d-3}(j-3),
}
$$


with negative-index $q$'s zero.

The shifts $-1,-2,-3$ are essential and are implemented correctly.

Because $A,B,C$ have total degrees at most $1,2,3$ in $(n,j)$, induction gives


$$
\boxed{\deg_{n,j}q_d\le d.}
$$


The natural coefficient ring is $\mathbb Z[1/2]$, hence also $\mathbb Z_{29}$. No integrality over $\mathbb Z$ is needed.

The code’s assertion checks degree in $j$ after specialization and reduction modulo $29^2$. That finite assertion alone would not prove the symbolic total-degree theorem; the induction above does.

---

## 12. Complete source cutoff

The source is


$$
\mathcal H_i
=
\sum_s a_s(n+1)(n+i)_{\underline s}
\binom{2n+i-s+1}{b},
$$


where $a_s(n+1)$ is the coefficient of


$$
\left(1-z+\frac{z^2}{2}\right)^{n+1}.
$$



The implemented formula for these coefficients is correct: choose $t$ quadratic terms and $s-2t$ linear terms.

The identity


$$
(n+i)_{\underline s}=s!\binom{n+i}{s}
$$


and Vandermonde give


$$
\binom{n+i}{s}
=\sum_{k=0}^s\binom n{s-k}\binom ik.
$$


This is exactly the independent source comparison in the code.

For $s\ge29K$,


$$
v_{29}(s!)\ge\left\lfloor\frac{s}{29}\right\rfloor\ge K.
$$


All coefficients $a_s(n+1)$ are $29$-integral. Therefore discarding $s\ge29K$ is valid modulo $29^K$, and the polynomial itself ends at $2n+2$. The complete safe cutoff is


$$
\boxed{s\le\min(2n+2,29K-1).}
$$


A tighter valuation-based cutoff is possible but is unnecessary for correctness.

---

## 13. Finite-memory identity and generating-function shifts

Let


$$
H_K=58K+1.
$$


With zero initial particular state, the exact finite-memory congruence is


$$
\boxed{
\tau_j\equiv
\sum_{\ell=\max(1,j-H_K)}^{j-1}
q_{j-\ell-1}(j)\mathcal H_\ell
\pmod{29^K},
\qquad 2\le j<b.
}
$$


The maximum retained propagator length is $H_K-1=58K$.

The source loops over recurrence rows


$$
1,\ldots,b-2
$$


and produces states only through $b-1$. It does not produce the reconstructed endpoint $b$.

A reusable generating identity that makes all shifts and finite boundaries explicit is the following. Define


$$
\mathcal H_{\rm fin}(z)=\sum_{\ell=1}^{b-2}\mathcal H_\ell z^\ell,
\qquad \theta=z\frac{d}{dz}.
$$


Then


$$
\boxed{
\sum_{j=0}^{b-1}\tau_jz^j
\equiv
P_{<b}\sum_{d=0}^{H_K-1}
q_d(n,\theta)\bigl(z^{d+1}\mathcal H_{\rm fin}(z)\bigr)
\pmod{29^K}.
}
$$


Equivalently,


$$
q_d(n,\theta)\bigl(z^{d+1}\mathcal H_{\rm fin}\bigr)
=
z^{d+1}q_d(n,\theta+d+1)\mathcal H_{\rm fin}.
$$



This identity is useful protection against a possible future mistake: placing $z^{d+1}$ outside the differential operator **without** shifting $\theta$ would evaluate $q_d$ at the source index rather than the final index.

The accepted source pole-order bound $29K$, combined with differential degree at most $58K$, yields the stated bound $87K$ for the indicated untruncated rational kernel. This is not a bound on a complete weighted/contact state dimension. The finite projection $P_{<b}$ remains required.

---

## 14. Receipt counts and exact scope

The listing reports:

- $57+203=260$ source-coefficient comparisons;
- another $57+203=260$ complete particular-output comparisons;
- $26+26=52$ impulse/product comparisons;
- $3\cdot6\cdot29=522$ all-phase propagation comparisons.

Thus “260 complete auxiliary source/particular checks” is best understood as 260 indices checked in each of two categories, not 260 scalar equalities in total.

The 522 propagation checks test


$$
n\in\{29,203,191110\},\quad K=1,\ldots,6,
\quad\text{all 29 phases},
$$


at length $58K+1$. The listing does not separately test the aligned $58K$ bound; that sharper aligned statement is inherited from the accepted proof.

The imported `product` implementation is not reproduced in this packet. The matrix-comparison assessment therefore depends on the previously accepted multiplication orientation and implementation.

The supplied PASS receipt is consistent with the mathematics. It does not establish:

- an original high-index source evaluation;
- contact-inverted norm or mixed values;
- a relative congruence after norm cancellation;
- a Gram alignment law.

The uniform $58K+1$ theorem continues to rest on the accepted all-phase nilpotence argument, not on extrapolation from these 522 finite tests.

---

# Part V. Remaining obligations and exact next computations

## 15. Complete force and true norm cancellation remain necessary

The binary raw outputs remain


$$
D_{\rm raw}=4N,\qquad E_{\rm raw}=8H,
$$


with the complete normalized second force


$$
r=\frac{h^e+h^F-A(j!)_{0\le j<b}}{b!}.
$$


The exponential contribution retains every valid label:


$$
r_i^e\equiv
\sum_{\substack{a,t\ge0\\a+v_2(t!)<20}}
\sum_{s=0}^{4a}
\lambda_s^{(a)}
\binom{n+i}{s}
t!\binom{b+t}{t}
\binom{2n+i-s}{b+t}
\pmod{2^{20}},
$$


with all original valid-term guards. The bounded ranges $t\le23$, $s\le76$ do not justify retaining only one channel.

The logarithmic-force omission remains justified only by its accepted budget for the stated **absolute** twenty-bit outputs. It is not an unlimited relative-precision omission.

The mixed endpoint contribution remains


$$
E_{\rm raw}=w^Tr+W_b\mathsf a_b.
$$


Likewise, the reconstruction Gram retains


$$
(Q_{\rm rec})_{b-1,b-1}=W_{b-1}^2+b^2W_b^2.
$$



If


$$
d=v_2(D_{\rm raw}),\qquad e=v_2(E_{\rm raw}),
$$


the source’s sufficient precision conditions


$$
M_E\ge s+d+1,\qquad M_D\ge s+2d+1-e
$$


are valid, together with $M_E>e$, $M_D>d$. Neither valuation has been supplied by these endpoint or recurrence receipts.

For the $29$-adic route, the unresolved relation remains


$$
\mathcal C-29\rho_n\mathcal N
\in29^2\mathcal N\mathbb Z_{29},
$$


requiring precision reaching the actual first nonzero norm digit. Short recurrence memory does not prove it.

---

## 16. Concrete follow-on lemma

The improved computational target is:

> Construct an exact target-compatible sparse, factorized, or observable-quotient realization of Cartier transitions for $\widetilde Q_U,\widetilde Q_L,\widetilde Q_B$, including all required degree-$76$ descendants, finite-Schur pairings, and complete-force labels. Prove its resource bounds along the actual full target-digit paths and retain the finite endpoint projections.

The exact common-marker identity proves the first reduction needed for this lemma. It does not prove closure of the complete descendants.

A successful certificate should state explicit reconstruction identities and measured or proved support/operator sizes. An automaticity citation or an unexplained small-state assertion is insufficient.

---

## 17. Bounded exact arithmetic calculation now warranted

The coordinator’s ongoing endpoint calculation is the appropriate narrow next output.

### Inputs

- the exact original $b,n$;
- $q=2^{20}$, $m=76$;
- the accepted divided-power $\lambda_s,c_s$ through order $76$;
- the formulas for $F,\overline K,G$ audited above.

### Required output

1. Complete residues of $S_{\rm end}$ and its inverse.
2. Verification
   

$$
S_{\rm end}\equiv I\pmod2.
$$


3. Both residual matrices:
   

$$
S_{\rm end}S_{\rm end}^{-1}-I=0,\qquad
   S_{\rm end}^{-1}S_{\rm end}-I=0\pmod{2^{20}}.
$$


4. An independently formed adjoint matrix with the boundary-variable grouping stated, and
   

$$
S_{\rm adj}-S_{\rm end}^T=0.
$$


5. Explicit confirmation of:
   

$$
b-152\le j\le b-1,\qquad
   \text{maximum lower binomial index }227,
$$


   and no original-length array.

These outputs would certify the finite boundary solve at the original $u=0$. They would not certify $D_{\rm raw}$, $E_{\rm raw}$, or a relative-output law.

---

## 18. Full gcd, primitive denominator, and whole error

Nothing in this audit changes the final arithmetic reduction. With the least actual two-column clearer $d_B$, retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


and


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
}
$$


The primitive multiplier remains $d_B^2/g_B$. Every prime in $g_B$ matters.

Under the accepted complete signed-error theorem,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)<0
$$


eventually, with the stated asymptotic decay. The relevant evaluated form is nevertheless the whole quantity


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
$$



An irrationality proof by this route requires a same-index bound on the **actual primitive denominator** forcing this nonzero quantity to tend to zero. Neither a finite endpoint inverse nor a finite absolute-precision Gram calculation supplies that all-prime bound.

---

## Conclusion

The new rigorous simplification is


$$
\boxed{
\text{one common weight marker replaces two independent equal-exponent markers.}
}
$$


It reduces the exact first-layer lifts to seven and six variables while preserving the original finite endpoints and ordinary expansion convention.

A5turn19’s Cartier transition, degree preservation, dense-cost inequalities, and bounded endpoint-entry reduction survive audit. The adjoint transpose assertion requires explicit factor grouping, and the largest-degree Cartier layer should not be called the highest-precision layer.

The recurrence source also survives audit: its polynomial shifts, degree bound, complete cutoff, and finite endpoint range are correct. The new receipt is auxiliary finite evidence consistent with the accepted uniform propagation theorem—not an original norm/mixed output.

The exact remaining bottlenecks are:

1. a bounded complete weighted-extraction implementation, beyond first-layer lifts;
2. complete original norm/mixed evaluation at true norm-sensitive precision;
3. any required relative law on the original family, with nonvanishing retained;
4. control of the full gcd, actual primitive denominator, and whole evaluated error.



$$
\boxed{\text{The irrationality or rationality of }e+\pi
\text{ remains unconditionally unresolved.}}
$$


