> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4 turn 9 — endpoint audit passes; the next radical has dimension one

## Executive conclusions

1. **The coordinator’s exact polynomial-endpoint proposal passes.** Its $b,\xi_{\rm const},c,\xi_{\rm last}$ are the actual residual quantities in A1 turn 5’s partition. Consequently
   

$$
\boxed{v_3\!\left(Q_{4^j+1}(-1)\right)=2v_3((4^j)!),\qquad j\ge1.}
$$


   The polynomial endpoint-depth obligation is **RESOLVED**. This is not a rational-center denominator law.

2. **A3 turn 8’s analytic continuation and generic-domain rate argument pass, conditional on its inherited integral representation, weight formulas, exponential bound, and arithmetic denominator theorem.** The supplied documents do not contain independent derivations of all those inherited inputs. Its explicit exceptions must remain.

3. For the displayed $8\times8$ next radical matrix,
   

$$
\boxed{\operatorname{rank}_{\mathbb F_3}\bar W=7,\qquad
   \ker\bar W=\mathbb F_3(1,2,1,2,1,2,0,0)^T.}
$$


   The distinguished endpoint functional is nonzero on this remaining radical.

4. The polynomial-digit derivation and the **assembly formulas** for the supplied $S\bmod9$ are correct. The numerical identification with the actual $P_{65}$ uses the supplied modular elimination receipt; I have not independently repeated that $63\times63$ elimination.

5. A stronger bounded follow-on is available: the same receipt and the first radical coordinates imply
   

$$
\boxed{3P_{65}(y)\equiv(y+1)(y-1)^{63}(3y+1)\pmod{27},}
$$


   not merely modulo $9$. This determines all polynomial digits needed for the next scalar lift.

6. I do **not** prove recursive saturation on an infinite regular class. The finite radical structure does not supply that missing infinite assertion. Below I derive the precise next scalar and a single bounded computation that decides its first possible nonzero digit.

---

## 1. Exact endpoint audit against the actual partition

Write


$$
n=3M+2,\quad N=3M+1,\quad L=3M,\qquad M\ge1,
$$


and


$$
\phi_d=\frac{(y+1)(y-1)^d}{d!}.
$$


Let $E$ be the Gram block on $\phi_0,\ldots,\phi_{L-1}$, and let


$$
\chi_i=\phi_i-\sum_{e<L}(E^{-1}G_{\cdot i})_e\phi_e,
\qquad i=L,N.
$$



### 1.1 Partition compatibility

In A1 turn 5, $E$ is eliminated while the constant coordinate and the last nonconstant coordinate remain. The residual pairings are therefore exactly


$$
b=\rho(1,\chi_L)=\mu(\chi_L),\qquad
\xi_{\rm const}=\rho(1,\chi_N)=\mu(\chi_N),
$$




$$
c=\rho(\chi_L,\chi_L)=\mu(\chi_L^2),\qquad
\xi_{\rm last}=\rho(\chi_L,\chi_N)=\mu(\chi_L\chi_N).
$$


Every $\chi_i$ vanishes at $-1$, so the negative evaluation mass contributes nothing to these four expressions. Eliminating the constant as well would change the last response; the proposal does not make that change.

Thus the proposed proof addresses the correct numerator


$$
c\xi_{\rm const}-b\xi_{\rm last}.
$$



### 1.2 Exact factorial divisibility

Put $z=y-1$. The finite identity


$$
1=\frac{y+1}{2}\sum_{d=0}^{L-1}\left(-\frac z2\right)^d
+\left(-\frac z2\right)^L
$$


has its first summand in the eliminated space. Orthogonality gives


$$
\mu(\chi_i)=(-2)^{-L}\mu(z^L\chi_i).
$$


For every $e\ge0$,


$$
\frac{\mu(z^L\phi_e)}{L!}
=\binom{L+e}{e}\,t_{L+e}\in\mathbb Z_3.
$$


Because $E^{-1}$ is integral at $3$, every projection coefficient is integral. Hence


$$
b,\xi_{\rm const}\in L!\mathbb Z_3.
$$



This reuses the archive’s orthogonality-doubling strategy. The finite geometric identity and Pascal identities are classical; the present application evaluates the actual odd-prime Schur numerator.

### 1.3 The normalized unit

The residue projection of $\phi_L$ is supported on $e=3q$, with coefficient vector $B_M^{-1}k$, where


$$
(B_M)_{ab}=\binom{a+b}{a},\qquad k_q=\binom{M+q}{q}.
$$


Since $t_s\equiv2\pmod3$, Lucas reduction yields


$$
\frac b{L!}\equiv
2(-2)^{-L}
\left(\binom{2M}{M}-k^TB_M^{-1}k\right)\pmod3.
$$


The bracket equals $1$ over $\mathbb Q$: it is the final Schur complement in the Pascal Gram matrix $B_{M+1}$, whose determinant and leading principal determinant are both $1$. Also $(-2)^{-L}\equiv1\pmod3$. Thus


$$
\boxed{b/L!\equiv2\pmod3.}
$$



A1’s first lift gives $v_3(c)=1$ and $\xi_{\rm last}\equiv2\pmod3$. Therefore


$$
\frac{c\xi_{\rm const}}{L!}\equiv0,\qquad
\frac{b\xi_{\rm last}}{L!}\equiv1\pmod3,
$$


and


$$
\boxed{
\frac{c\xi_{\rm const}-b\xi_{\rm last}}{L!}\equiv2\pmod3.
}
$$


This is strict separation of the two summands, not subtraction of valuation lower bounds.

Since $N=L+1$ is a $3$-unit,


$$
v_3(L!)=v_3(N!).
$$


Combining with A1’s actual primitive-content formula proves


$$
\boxed{v_3(Q_{4^j+1}(-1))=2v_3((4^j)!),\quad j\ge1.}
$$



The endpoint is nonzero, both by this finite valuation and by the orthogonal-modification identity.

### A modest extension

The same leading-content argument in A1 turn 5 actually works for every $n=3M+2$, $M\ge1$: $N=3M+1$ is a unit, all $\eta$-coordinates have valuation at least $-1$, and the coefficient of $y^{n-1}$ has valuation exactly $-1$. Thus the primitive leading multiplier has depth one throughout this larger domain. Consequently


$$
\boxed{
v_3(Q_n(-1))=2v_3((n-1)!),\qquad n\ge5,\ n\equiv2\pmod3.
}
$$


This extension concerns the polynomial only; it does not extend any regular-family center theorem.

---

## 2. Audit of A3 turn 8

### 2.1 Critical values and analytic pushforward

At $T\ne0$, the three critical-point equations force


$$
\sin\theta_1=\sin\theta_2=0,\qquad y=0.
$$


The resulting nonzero critical values are exactly


$$
-r,\qquad p,\qquad -2\rho^3.
$$


The extension to $y\in\mathbb R$, with half the measure, legitimately removes the boundary because the map and weights are even there.

Properness over compact subintervals away from $0$ follows from


$$
|T|\le M^2|u(y)|\longrightarrow0.
$$


The analytic-flow argument is valid: over a sufficiently small interval around a regular value, the analytic flow of


$$
X=\frac{\nabla T}{|\nabla T|^2}
$$


identifies compact fibers analytically. Integration over a fixed compact fiber preserves local real analyticity. This proves analyticity of the **total** densities, not merely a corner contribution.

The singular expansion


$$
\mathcal F(-r+s)
=-\frac34 bMr^3K\,s^{-5/2}+O(s^{-3/2})
$$


also has the correct leading differentiation constant: the third derivative of $s^{1/2}$ is $3s^{-5/2}/8$, and $A=-2bM$.

### 2.2 Positive endpoint and Watson constants

The two attaining corners are correctly counted. From the stated map,


$$
p-T=b\rho^2\alpha^2+b\beta^2+b\rho^2y^2+O(|(\alpha,\beta,y)|^4).
$$


For this quadratic form, integration over $y\ge0$ gives the density coefficient


$$
\frac{\pi}{b^{3/2}\rho^2}s^{1/2}.
$$


Multiplication by the stated corner measure density $\rho/\pi^2$, and then by two corners, gives


$$
K_+=\frac2{\pi b^{3/2}\rho}.
$$


The five displayed $A_h$ values follow correctly from the displayed values $F=-4,G=1,B=-1,D_0=4$.

The resulting orders and constants are correct:


$$
n^{3/2}C_-(c_n)r^n(5-r)^m
$$


at the negative endpoint, and


$$
n^{5/2}C_+(c_n)p^n(5+p)^m
$$


at the positive endpoint, with


$$
C_-=AK\Gamma(3/2)r^{3/2}a_-^{3/2}<0,
$$




$$
C_+=8\rho K_+\Gamma(3/2)p^{3/2}a_+^{5/2}>0.
$$


In particular, the negative endpoint’s $a_-^{3/2}$, rather than $a_-^3$, correctly includes the Watson integration.

### 2.3 Switch, exceptions, and rounding

The derivative


$$
\Delta'(c)=\log\frac{5-x_c}{5+p}<0
$$


proves uniqueness of the switch. The comparisons at $c=1,2$ are correct, including


$$
B_+(1)=r,\qquad B_+(2)=2M^3.
$$


Thus $1<c_{\rm s}<2$.

The exception set


$$
\mathcal E=\left\{c\in(c_0,c_{\rm s}):
\mathcal F\!\left(-\frac5{1+c}\right)=0\right\}
$$


is finite: the endpoint expansion excludes accumulation at $c_0$, and analyticity on a neighborhood of the remaining compact saddle interval excludes all other accumulation.

This is an **explicit definition**, not an evaluated list or an effective cardinality bound.

At bounded rounding,


$$
m-c_{\rm s}n=O(1),
$$


the ratio of the negative-saddle magnitude to the positive-endpoint magnitude is $O(n^{-3})$. Positive dominance therefore follows even if the negative amplitude vanishes at the switch.

One precision qualification is useful: under the more general condition


$$
n\Delta(c_n)\le(3-\epsilon)\log n,
$$


positive dominance follows with an additional relative error $O(n^{-\epsilon})$. The sharper relative $O(n^{-1})$ in the pure positive-endpoint formula need not hold when $0<\epsilon<1$. Bounded rounding does retain the stated $O(n^{-1})$.

### 2.4 Whole correction and actual gcd

The supplied exponential estimate gives


$$
\log|\mathcal Z^{\rm exp}_{n,m}|\le-n\log n+O(n)
$$


when $m/n$ is bounded. It is negligible against each stated nonzero exponential main term. This conclusion uses the bound for the **entire** correction; no individual deficit is discarded.

With


$$
U=L_N\mathcal H,\quad V=L_N\mathcal J,\quad
g=\gcd(|U|,|V|),
$$




$$
P=-\operatorname{sgn}(V)U/g,\qquad q=|V|/g,
$$


the identity


$$
q(e+\pi)-P=q\,\frac{\mathcal Z}{\mathcal J}
$$


is exact. Consequently the rate theorem and enlarged primorial exclusion follow from their stated inherited denominator inputs.

**Audit verdict:** pass with those inherited dependencies, the error-term qualification above, and all explicit exceptions retained:
- $c=c_0$;
- the finite unevaluated set $\mathcal E$;
- unrestricted approaches to $c_{\rm s}$.

No conclusion is justified in the possible cancellation window merely from equality of exponential rates.

---

## 3. Polynomial-digit and assembly audit at $n=65$

Use the local normalization


$$
Q^{\rm loc}=3P_{65}.
$$


It differs from the actual primitive polynomial by a $3$-adic unit, which changes neither valuations nor the reduced rational center.

### 3.1 The modulo-$9$ digit

The exact coefficient formula is


$$
3P_{65}
=3h_{65}-3\cdot64!\eta_{\rm const}
-\sum_{d=0}^{63}\frac{64!}{d!}(3\eta_{d+1})h_{d+1}.
$$


For $d\le62$, the factorial ratio contains $63$, of depth two, so these terms vanish modulo $9$. The constant term also vanishes.

The endpoint theorem makes the $b$-corrections negligible at this precision. The supplied receipt gives


$$
\xi_{\rm last}\equiv2\pmod9,\qquad c/3\equiv4\pmod9.
$$


Therefore


$$
3\eta_{\rm last}\equiv2\cdot4^{-1}=5\pmod9.
$$


Hence


$$
3P_{65}\equiv
(y+1)(y-1)^{63}\bigl(3(y-1)-64\cdot5\bigr)
\equiv(y+1)(y-1)^{63}(3y+1)\pmod9.
$$



### 3.2 Assembly

Here $h=5$, so the relevant pole denominators are


$$
243,\quad81,\quad27,\ 135,\ 189.
$$


After dividing the first low Schur matrix by its global unit, the formula is


$$
S_{ij}\equiv
[y^{40}]C_{ij}
+3\sum_{a=1,5,7}a^{-1}[y^{(27a-1)/2}]C_{ij}
-3(XE^{-1}X^T)_{ij}\pmod9.
$$


The highest pole is absent from LOW–LOW exactly by degree. In LOW–HIGH its only possible contribution is the corner $(25,32)$, with coefficient


$$
\operatorname{lc}(Q^{\rm loc})/3=1.
$$


Thus the code’s corner addition, lower poles, cross-correction sign, and required inverse precision are correct.

This audits the assembly rule. The displayed matrix is a finite computational output, not a proof of an infinite lifting pattern.

### 3.3 New: the same polynomial formula holds modulo $27$

For $d\le59$, $64!/d!$ contains both $60$ and $63$, hence has depth at least three.

For $d=60,61,62$, its depth is two, so only $3\eta_{d+1}\bmod3$ matters. The first radical coordinates give


$$
3\eta_E\equiv-2z\pmod3,
$$


supported on $d=3D$. At $d=60$, the relevant coefficient is


$$
z_{20}=\binom{21}{20}=21\equiv0\pmod3;
$$


at $d=61,62$ it is zero by support. These three terms therefore vanish modulo $27$ as well.

From the supplied integer residues,


$$
c\equiv39\pmod{81},\qquad \xi_{\rm last}\equiv11\pmod{27}.
$$


Thus


$$
3\eta_{\rm last}\equiv11\cdot13^{-1}
\equiv11\cdot25\equiv5\pmod{27}.
$$


It follows that


$$
\boxed{
3P_{65}\equiv(y+1)(y-1)^{63}(3y+1)\pmod{27}.
}
$$


The algebraic reduction is proved; its numerical input is the supplied finite elimination receipt.

---

## 4. Exact rank and endpoint projection of the displayed next matrix

Let $\bar W$ be the supplied $8\times8$ matrix and set


$$
k=(1,2,1,2,1,2,0,0)^T.
$$


Direct row multiplication gives $\bar Wk=0$.

The principal submatrix on coordinates $1,\ldots,7$ is nonsingular. Its first five coordinates form an anti-triangular $5\times5$ matrix with all antidiagonal entries $1$, hence determinant $1$. Its final two coordinates form


$$
\begin{pmatrix}0&1\\1&2\end{pmatrix},
$$


of determinant $2$. Thus that principal minor has determinant $2$.

Consequently


$$
\boxed{\operatorname{rank}\bar W=7,\qquad\ker\bar W=\mathbb F_3k.}
$$


The supplied distinguished vector is $e_0$, and


$$
e_0^Tk=1.
$$


The endpoint survives on the remaining radical.

This is an exact statement about the displayed matrix, not a one-dimensional description of the preceding $26\times26$ residue, whose radical has dimension eight.

---

## 5. A concrete next scalar, and what it already determines

Let $W$ now denote the **actual** saturated $8\times8$ block obtained from $S$. Put


$$
C=(e_1,\ldots,e_7),\qquad J=C^TWC.
$$


Since $J\bmod3$ is nonsingular, define


$$
\tau=\frac{k^TWk-k^TWC\,J^{-1}C^TWk}{3}\in\mathbb Z_3.
$$


The numerator is divisible by $3$. Moreover, $C^TWk\equiv0\pmod3$, so


$$
\boxed{\tau\equiv\frac{k^TWk}{3}\pmod3.}
$$



The distinguished residual endpoint on this last scalar is a unit, because its reduction is $e_0^Tk=1$.

Therefore, if $S$ is nonsingular,


$$
\boxed{v_3((S^{-1})_{00})=-2-v_3(\tau)\le-2.}
$$


Here the depth is not inferred from determinant valuation alone: the unit endpoint projection supplies the noncancelling scalar pole.

There is also a useful cofactor conclusion independent of the depth of $\tau$. Two successive block eliminations give


$$
\boxed{v_3(\operatorname{adj}(S)_{00})=7.}
$$


Indeed, $\det S$ has the factor $3^8$ from the eight-dimensional first radical and a further $3\tau$; the endpoint inverse contributes a unit times $1/(9\tau)$. Their product has depth $7$. The same cofactor identity extends algebraically to $\tau=0$, where the remaining endpoint coefficient is still a unit.

Thus, **conditional on the supplied finite matrices being the actual lifts**, at $n=65$,


$$
v_3(B)=5+60+25+7=97,
$$


and


$$
v_3(A)=35+v_3(\tau),
$$


with $v_3(0)=+\infty$. The actual denominator satisfies


$$
\boxed{v_3(q)=\max\{0,62-v_3(\tau)\}.}
$$


In particular, a unit $\tau$ would give


$$
v_3((S^{-1})_{00})=-2,\qquad v_3(A)=35,\qquad v_3(q)=62.
$$



These are finite-index consequences. I do not extend the rank-seven pattern or the scalar saturation to an infinite regular class.

---

## 6. Exact next modulus and bounded computation

To determine $\tau\bmod3$, one needs $W\bmod9$, hence $S\bmod27$.

Write


$$
C^{[r]}_{ij}=[y^r]\,
\frac{Q^{\rm loc}f_if_j-Q^{\rm loc}(-1)f_i(-1)f_j(-1)}{y+1}.
$$


At this index the endpoint term vanishes to more than the required precision. Define


$$
\mathcal A=\{1,5,7,11,13,17,19,23,25\}.
$$


These are exactly the positive odd $3$-units $a$ with $9a\le257$.

The required normalized LOW–LOW formula is


$$
S_{ij}\equiv C^{[40]}_{ij}
+3\sum_{a=1,5,7}a^{-1}C^{[(27a-1)/2]}_{ij}
+9\sum_{a\in\mathcal A}a^{-1}C^{[(9a-1)/2]}_{ij}
-3(XE^{-1}X^T)_{ij}\pmod{27}.
$$


It needs:
- $Q^{\rm loc}\bmod27$ at the $81$-pole;
- $Q^{\rm loc}\bmod9$ at the $27$-poles;
- $Q^{\rm loc}\bmod3$ at the $9$-poles;
- $X\bmod9$ and $E\bmod9$.

For $X\bmod9$, retain the unique highest-pole corner, the $81$-pole, and the $27$-poles. For $E\bmod9$, retain the $243$- and $81$-poles. No further polynomial digit is needed. The factorial portion vanishes at this precision because its clearer already has depth five.

All polynomial inputs are supplied by


$$
Q^{\rm loc}\equiv(y+1)(y-1)^{63}(3y+1)\pmod{27}.
$$



---

## 7. Actual normalization and whole evaluated error

For the weighted construction retain


$$
g=\gcd(|A|,|B|),\qquad
q=\frac{|B|}{g},\qquad
p=-\frac{\operatorname{sgn}(B)A}{g}.
$$


The whole evaluated error is exactly


$$
\boxed{
q(e+\pi)-p
=\frac{\operatorname{sgn}(B)}g\bigl(A+B(e+\pi)\bigr)
=\frac{\operatorname{sgn}(B)\ell^k}{g}\det H_{\rm complete}.
}
$$


No period or rational arctangent term has been omitted.

On the supplied regular domain $n=4^j+1,\ j\ge1$, the inherited dyadic result gives $B\ne0$ and distinct centers; hence the whole errors are nonzero except possibly at one index. Nothing proved here establishes their decay.

---

## Closing ledger

### (1) New result and proof status

- **Proved:** the coordinator’s exact endpoint argument passes in the actual Schur partition. Polynomial endpoint depth is resolved, and the same proof extends to all $n\ge5$, $n\equiv2\pmod3$.
- **Audited with inherited dependencies:** A3’s generic signed-rate theorem, bounded switch rounding, and enlarged primorial exclusion. Its exceptions remain; the wider switch-dominance condition needs the relative-error qualification stated above.
- **Proved for the displayed finite matrix:** the next radical has dimension one and nonzero endpoint projection.
- **Derived from the supplied finite elimination receipt:** the stronger polynomial congruence modulo $27$.
- **Conditional on the finite lift receipt:** the cofactor depth $7$, $v_3(B)=97$, and the exact scalar law $v_3(q)=\max(0,62-v_3(\tau))$ at $n=65$.

### (2) Exact remaining bottleneck

The bounded bottleneck is $\tau\bmod3$. The infinite bottleneck is different: prove a recursive rank-and-endpoint-projection law for the **actual lifted Schur matrices** on a specified infinite regular class. Lucas support of the first residue, or valuations of its classical integer representative, do not prove such a law.

No proof or disproof of irrationality of $e+\pi$ is obtained.

### (3) Single computation request

**Input:** only $n=65$, with the polynomial modulo $27$ and pole formulas in Section 6.

**Requested verifiable output:**
1. $S\bmod27$, reducing to the supplied $S\bmod9$;
2. its first saturated block $W\bmod9$, reducing to the displayed rank-seven matrix;
3. $\tau\bmod3$, computed both by the scalar Schur formula and by $k^TWk/3\bmod3$;
4. the residual endpoint scalar modulo $3$, which must equal $1$ in the stated normalization.

If $\tau\not\equiv0$, this certifies the finite conclusions $v_3(A)=35$, $v_3(B)=97$, and $v_3(q)=62$. If $\tau\equiv0$, report only $v_3(\tau)\ge1$; do not infer its exact depth or an infinite saturation theorem.
