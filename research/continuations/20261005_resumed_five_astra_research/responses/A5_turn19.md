> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, Turn 19 — Fixed-denominator lifts for the actual weighted kernels, and a bounded original-index endpoint certificate

## Executive conclusion

The large parameter-dependent powers in Turn 18 can be removed from the denominators **without changing the original finite summation endpoints**. In particular, the weighted upper transform admits an ordinary rational coefficient representation in eight variables whose denominator has multidegree


$$
(2,2,2,2,1,1,1,1)
$$


and total degree $11$, independently of $b,n$. The weighted lower transform and the boundary Gram kernel admit seven-variable representations of total denominator degree $9$.

These are exact integral reductions, not substitutes for the actual weights. They permit the established prime-power Cartier method to be applied directly. I give explicit integral transitions and numerical bounds at $M=20$.

The resulting conclusion is qualified:

* **Proved:** fixed-denominator rational representations and a concrete prime-power linear coefficient-extraction scheme for the three first-layer kernels.
* **Not proved:** a practically small representation for all the actual divided-power, finite-Schur, force and contraction descendants.
* **Quantitative limitation:** even the eight-variable first-layer scheme has a dense numerator box containing more than $5\cdot10^{11}$ monomials in its highest precision layer. The supplied data do not establish sparse reachable support sufficient to avoid that cost.
* **Concrete narrower output:** the actual $76\times76$ finite endpoint Schur matrix can be generated and inverted using only precision-sized tables and binomial lower indices at most $227$. This is a useful original-index certificate, distinct from the already-passed interior audit.

No tools were executed. No new numerical Gram residues or independently verified hashes are claimed.

An unconditional proof or disproof of the irrationality of $e+\pi$ remains unresolved.

---

## 1. Original parameters, actual coefficients, and receipt scope

The family remains


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


Here the requested specialization is


$$
u=0,\qquad
b=150094635296999121,\qquad
n=600678730458590482242,
$$


with


$$
M=20,\qquad q=2^{20}=1048576,\qquad m=76.
$$



Contact coordinates remain $0,\ldots,b-1$; reconstructed coordinates remain $0,\ldots,b$. In block notation,


$$
b=128D+81:
$$


there are $D$ full contact blocks, the final contact block has residues $0,\ldots,80$, and $j=b$ is a separate reconstructed endpoint.

Write


$$
N_0=n+2,\qquad W_j=\binom{N_0}{j}.
$$



### 1.1 The actual symbol, not a test operator

The coordinator’s source specifies the symbol in the divided-power algebra. Put


$$
V=(0,-1,2,-3,3),
$$


and define


$$
d^{(0)}_s=\mathbf1_{s=0},\qquad
d^{(a+1)}_s=\sum_{j=0}^4\binom sj d^{(a)}_{s-j}V_j,
$$


with invalid indices zero. Then the actual coefficients used at this precision are


$$
\lambda_s=
\sum_{a=0}^{19}2^a\binom{n/2}{a}d^{(a)}_s
\pmod q.
$$


Thus the force-layer coefficients may be retained as


$$
\lambda_s^{(a)}=2^a\binom{n/2}{a}d_s^{(a)}.
$$



The actual inverse coefficients are


$$
c_0=1,\qquad
c_k=-\sum_{s=1}^k\binom ks\lambda_s c_{k-s}\pmod q.
$$


The accepted filtration gives


$$
v_2(\lambda_s),v_2(c_s)\ge\left\lceil s/4\right\rceil
\quad(s>0).
$$



The receipt reports:

* 153 inverse-product residual checks;
* 152 filtration checks;
* 2926 original-index endpoint-commutator comparisons;
* zero nonzero returning endpoint coefficients for the particular input
  

$$
F(x)=(1+x)^{-n}.
$$



The last statement is stronger than merely saying that the two sides agree, but its scope remains that particular input and those 2926 positions. It does **not** show that the finite endpoint correction vanishes on weighted input polynomials, and it is not a norm law.

### 1.2 Binary input schedule

The actual low twenty bits are


$$
b\equiv116433=\mathtt{0x1C6D1}\pmod q,
$$




$$
n\equiv397122=\mathtt{0x60F42}\pmod q,\qquad
N_0\equiv\mathtt{0x60F44}\pmod q.
$$


The full $b$ has 58 binary digits and $n$ has 70.

The coefficient algorithms below must consume the **full integer targets**, not just these low residues. For every displayed target vector $\boldsymbol T$, the exact digit schedule is


$$
\boldsymbol T^{(0)}=\boldsymbol T,\qquad
\boldsymbol\epsilon_r=\boldsymbol T^{(r)}-2\left\lfloor\boldsymbol T^{(r)}/2\right\rfloor,\qquad
\boldsymbol T^{(r+1)}=\left\lfloor\boldsymbol T^{(r)}/2\right\rfloor.
$$


This specifies the original binary input unambiguously using the exact decimal integers above. I do not claim to have executed its state traversal.

---

## 2. A fixed-denominator lift retaining $b-1-i$

Use $U,V,Z,Y$ as coefficient variables, and $A,B,C,T$ as power-marker variables. They are unrelated to the contact matrix $A$.

For fixed shifts $a,c$, consider the genuine weighted channel


$$
K_{a,c}(j)=W_{j+a}W_{j+c}\binom{2n+j}{b}.
$$



### Theorem 1 — Ordinary rational lift of the finite upper transform

For $0\le i<b$,


$$
\boxed{
\begin{aligned}
(\mathcal T_UK_{a,c})(i)
={}&[U^{b-1+a}V^{b-1+c}Z^bY^{b-1-i}\\
&\qquad A^{N_0}B^{N_0}C^{2n+i}T^{n-1}]
\frac1{Q_U},
\end{aligned}}
$$


where


$$
\boxed{
Q_U=
(1-A(1+U))
(1-B(1+V))
(1-C(1+Z))
(1+(1+Z)Y-T)
(1-UVY).
}
$$



All expansions are ordinary formal power-series expansions at the origin.

#### Proof

Extracting the four power-marker coefficients gives


$$
\frac{(1+U)^{N_0}(1+V)^{N_0}(1+Z)^{2n+i}}
{(1-UVY)(1+(1+Z)Y)^n},
$$


because


$$
[T^{n-1}]\frac1{1+(1+Z)Y-T}
=(1+(1+Z)Y)^{-n}.
$$



Set $B_i=b-1-i$. The remaining $Y$-coefficient is


$$
[Y^{B_i}]
\frac1{(1-UVY)(1+(1+Z)Y)^n}
=
\sum_{k=0}^{B_i}
(UV)^{B_i-k}\binom{-n}{k}(1+Z)^k.
$$


Consequently the $U,V$ targets select


$$
\binom{N_0}{b-1+a-(B_i-k)}
\binom{N_0}{b-1+c-(B_i-k)}
=
W_{i+k+a}W_{i+k+c}.
$$


The $Z^b$ coefficient supplies $\binom{2n+i+k}{b}$. This is exactly the finite sum defining $\mathcal T_UK_{a,c}$. ∎

### Why this lift matters

The factor $1-UVY$ is an **integral finite-binomial-sum encoding**. It retains $k\le b-1-i$ through the target $Y^{b-1-i}$, without introducing a negative power of $U$ or $V$.

There is no substitution at $Y=1$, no infinite-endpoint replacement, and no division by a binomial coefficient.

### Denominator degrees

In variable order


$$
(U,V,Z,Y,A,B,C,T),
$$


the multidegree is


$$
\boxed{(2,2,2,2,1,1,1,1)}.
$$


The total degree is $11$. Moreover $Q_U(0)=1$, as required for the rational-series Cartier construction.

---

## 3. Fixed-denominator lifts for the other two first-layer kernels

### 3.1 Weighted lower transform

The exact identity in Turn 18 becomes


$$
\boxed{
\begin{aligned}
(\mathcal T_LK_{a,c})(j)
={}&[U^{j+a}V^{j+c}Z^b
 A^{N_0}B^{N_0}C^{2n}T^j]\frac1{Q_L},
\end{aligned}}
$$


where


$$
\boxed{
Q_L=
(1-A(1+U))
(1-B(1+V))
(1-C(1+Z))
(1-T(1+Z-UV)).
}
$$



Indeed, power-marker extraction leaves


$$
(1+U)^{N_0}(1+V)^{N_0}(1+Z)^{2n}(1+Z-UV)^j.
$$


Taking the indicated coefficients is precisely Turn 18’s constant-term expression after clearing $(UV)^{-j}$.

In variable order $(U,V,Z,A,B,C,T)$, the denominator multidegree is


$$
\boxed{(2,2,2,1,1,1,1)},
$$


and its total degree is $9$.

### 3.2 Boundary Gram kernel

For


$$
p_h(j)=(-1)^{h-j}\binom hj,
$$


define the shifted-weight pairing


$$
\mathcal B^{a,c}_{h,k}
=\sum_j W_{j+a}W_{j+c}p_h(j)p_k(j).
$$


Then


$$
\boxed{
\begin{aligned}
\mathcal B^{a,c}_{h,k}
={}&(-1)^{h+k}
[U^{h+a}V^{h+c}Z^k\\
&\qquad A^{N_0}B^{N_0}C^kT^h]\frac1{Q_B},
\end{aligned}}
$$


with


$$
\boxed{
Q_B=
(1-A(1+U))
(1-B(1+V))
(1-C(1+Z))
(1-T(UV+Z)).
}
$$



To verify this, extract the power markers and expand


$$
(1+Z)^k(UV+Z)^h.
$$


The coefficient of $Z^k$, followed by the $U,V$ extractions, gives


$$
\sum_j\binom hj\binom kjW_{j+a}W_{j+c},
$$


with the stated sign.

Again, the multidegree is $(2,2,2,1,1,1,1)$ and the total degree is $9$.

These formulas retain the actual high degrees


$$
b-76\le h,k\le b-1.
$$


They do not replace them by small proxy degrees.

---

## 4. Explicit prime-power Cartier transitions

The relevant background is the established rational-diagonal/Cartier method, including the cited Rowland–Yassawi work. A general automaticity theorem alone is not a feasibility estimate. Here the transition formula and degree box can be written down directly.

Let $Q\in\mathbb Z[\boldsymbol x]$, $Q(0)=1$, and let its coordinatewise degree vector be $\boldsymbol d$. Set


$$
E(\boldsymbol x)=\frac{Q(\boldsymbol x)^2-Q(\boldsymbol x^2)}2.
$$


This is integral.

For a binary digit vector $\boldsymbol\epsilon$, let


$$
\Lambda_{\boldsymbol\epsilon}
\left(\sum_{\boldsymbol r}a_{\boldsymbol r}\boldsymbol x^{\boldsymbol r}\right)
=
\sum_{\boldsymbol r}a_{2\boldsymbol r+\boldsymbol\epsilon}
\boldsymbol x^{\boldsymbol r}.
$$



Represent a rational series modulo $2^M$ as


$$
\boxed{
F=\sum_{a=0}^{M-1}2^a\frac{P_a}{Q^{a+1}},
\qquad
\deg_{x_i}P_a\le(a+1)d_i.
}
$$


The initial series $1/Q$ has $P_0=1$ and all other $P_a=0$.

### Integral transition

For each layer $a$, put


$$
\ell=\left\lceil\frac{a+1}{2}\right\rceil.
$$


For $0\le j<M-a$, add to the new numerator in layer $a+j$


$$
\boxed{
(-1)^j
\binom{\ell+j-1}{j}
\Lambda_{\boldsymbol\epsilon}
\!\left(
P_aQ^{2\ell-a-1}E^j
\right)
Q^{a+1-\ell}.
}
\tag{4.1}
$$



The binomial coefficient in this formula is essential: it comes from a negative power of exponent $\ell$, not always exponent one.

#### Derivation

Write


$$
Q^{-a-1}=Q^{2\ell-a-1}(Q^2)^{-\ell}.
$$


Since $Q^2=Q(\boldsymbol x^2)+2E$,


$$
(Q^2)^{-\ell}
\equiv
\sum_{j=0}^{M-a-1}
(-2)^j\binom{\ell+j-1}{j}
\frac{E^j}{Q(\boldsymbol x^2)^{\ell+j}}
\pmod{2^{M-a}}.
$$


Apply


$$
\Lambda_{\boldsymbol\epsilon}
\bigl(G(\boldsymbol x)H(\boldsymbol x^2)\bigr)
=
\Lambda_{\boldsymbol\epsilon}(G)H(\boldsymbol x),
$$


and multiply the resulting numerator by $Q^{a+1-\ell}$ to use denominator $Q^{a+j+1}$. This gives (4.1).

All operations are integral. No factorial or nonunit division occurs.

### Degree preservation

Before Cartier extraction, the coordinate degree is at most


$$
2(\ell+j)d_i.
$$


After extraction it is at most $(\ell+j)d_i$; denominator padding adds $(a+1-\ell)d_i$. Thus the result lies in the layer-$(a+j)$ box


$$
\deg_{x_i}\le(a+j+1)d_i.
$$



After processing all target digits, the desired coefficient is


$$
\sum_{a=0}^{M-1}2^aP_a(0)\pmod{2^M}.
$$



This proves a concrete linear coefficient-extraction scheme for the three displayed fixed rational functions. It does not assert small reachable support.

---

## 5. Numerical bounds at twenty bits

For a denominator of multidegree $\boldsymbol d$, the above representation has at most


$$
R_M(\boldsymbol d)
=
\sum_{t=1}^{M}\prod_i(td_i+1)
$$


numerator coefficient slots.

Accounting for the different layer moduli, a finite-state upper bound is


$$
2^{B_M(\boldsymbol d)},\qquad
B_M(\boldsymbol d)
=
\sum_{t=1}^{M}(M+1-t)\prod_i(td_i+1).
$$


This is an upper bound for the representation, not a measured reachable-state count.

### 5.1 Eight-variable upper transform

Here


$$
\boxed{
R_U=\sum_{t=1}^{20}(2t+1)^4(t+1)^4.
}
$$


Its highest layer alone has


$$
41^4\,21^4>5\cdot10^{11}
$$


coefficient slots, and


$$
R_U\le20\cdot41^4\,21^4<1.1\cdot10^{13}.
$$



Even storing only one bit per coefficient in that highest layer requires more than $62.5$ GB. Storing the full layered representation densely is substantially more expensive.

A straightforward intermediate polynomial in a transition can have coordinate degree bounded by $40d_i$. The corresponding dense box has


$$
81^4\,41^4>10^{14}
$$


slots. Allocating that box in four-byte residues would exceed $400$ TB.

These are concrete dense-implementation costs, not claims that all those coefficients are nonzero.

### 5.2 Seven-variable lower and boundary kernels

For each of $Q_L,Q_B$,


$$
\boxed{
R_7=\sum_{t=1}^{20}(2t+1)^3(t+1)^4.
}
$$


The last layer has


$$
41^3\,21^4>1.3\cdot10^{10}
$$


slots, while


$$
R_7<2.7\cdot10^{11}.
$$



### 5.3 Actual input length does not cure the numerator size

All first-layer targets at this original index have at most 71 binary digits. Thus a single specified extraction follows at most 71 transitions, plus its initial state. It does not require enumerating every possible automaton state.

Nevertheless, a short digit path does not make a dense numerator small. The unresolved issue is the size of the numerator supports or an equivalent compressed linear scheme **along these particular paths**.

### Precise obstruction

The present obstacle is therefore not an impossibility theorem for modular extraction. It is this:

> The proved, parameter-independent Cartier representation is too large in its guaranteed dense form, and no supplied argument bounds the actual sparse supports, their transition costs, or their observable quotient dimensions at twenty bits.

It would be incorrect to turn this upper-bound cost into a lower bound for every algorithm. Conversely, merely citing automaticity or the newer prime-power state-complexity framework does not establish that these actual paths are small.

---

## 6. Bounded weight use and degree-76 descendants

There is no need for closure under arbitrarily repeated multiplication by $W_j^2$.

For the actual norm,


$$
Q_{\rm rec}=\mathcal R^T\mathcal R
$$


has


$$
(Q_{\rm rec})_{ii}=W_i^2+(i+1)^2W_{i+1}^2,
$$




$$
(Q_{\rm rec})_{i,i+1}=-(i+1)W_{i+1}^2.
$$


A bilinear contraction therefore has one reconstruction Gram insertion, using two binomial weight factors. The first-layer lifts already encode those two factors.

The divided-power inverse adds only the labels $0\le s\le76$. Its transfers use integral factors such as $\binom{k}{s}$, with coefficient $c_s$, and should be implemented as bounded sums of shifted coefficient targets. Divided derivatives can also be handled by coefficient extraction from $F(\boldsymbol x+\boldsymbol t)$, without dividing by $s!$.

However, neither observation proves that **composing all finite transfers and contracting them** leaves the seven- or eight-variable degree boxes unchanged. That composition must be specified and bounded. The current report proves the three first-layer schemes, not the complete specialized lemma for all descendants.

The accepted characteristic-zero Vandermonde obstruction remains valid only for unrestricted closure. It supplies no additional modular lower bound here.

---

## 7. A narrower original-index certificate: the complete endpoint Schur matrix

There is a useful bounded calculation that goes beyond the supplied commutator audit and does not require the large weighted extraction.

Use the accepted finite factorization


$$
A\equiv LU(H+F\overline K E)U\pmod q,
$$


where $E$ selects contact coordinates $b-76,\ldots,b-1$.

The primal endpoint Schur matrix is


$$
\boxed{S_{\rm end}=I_{76}+EH^{-1}F\overline K.}
$$


Its transpose is the corresponding adjoint Schur matrix.

### 7.1 All necessary entries have bounded lower binomial indices

For $0\le r,t<76$,


$$
\boxed{
\overline K_{r,t}
=
\lambda_{76+r-t}\binom{b+r}{76+r-t},
}
$$


with the entry zero unless $1\le76+r-t\le76$.

The inverse of $H$ has


$$
(H^{-1})_{j,j-s}=c_s\binom js,\qquad0\le s\le76.
$$


Therefore, if


$$
G=EH^{-1}F,
$$


then


$$
\boxed{
G_{t,r}=
\sum_{s=0}^{76}
c_s\binom{b-76+t}{s}
F_{b-76+t-s,r}.
}
$$


The needed $F$-entries are


$$
\boxed{
F_{j,r}
=
-\sum_{v=0}^{r}
\binom{-n}{b+v-j}\binom n{r-v},
\qquad b-152\le j\le b-1.
}
$$



Every large-upper binomial in these formulas has lower index at most


$$
75+152=227.
$$


Thus none requires summation to $b$, a length-$b$ vector, or the unresolved weighted Gram scheme.

### 7.2 Concrete cost

A direct implementation uses:

* $152\cdot76$ values of $F_{j,r}$;
* at most
  

$$
152\sum_{r=0}^{75}(r+1)=444752
$$


  summands to form them;
* at most $76^2\cdot77=444752$ summands for $G$;
* $76^3=438976$ summands for $G\overline K$.

The contraction work before inversion is below $1.4$ million scalar summands. A $76\times76$ unit-pivot inversion adds only a few million modular arithmetic operations.

Large-upper, small-lower binomials can be generated exactly by the integral recurrence


$$
B_{d+1}=B_d\frac{N-d}{d+1}
$$


using exact integers before modular reduction, or by valuation/odd-unit arithmetic. The former entails only integers of roughly $227$ times the upper-parameter bit length, not factorials of size $n$.

Since $\overline K\equiv0\pmod2$,


$$
S_{\rm end}\equiv I_{76}\pmod2.
$$


Hence unit-pivot inversion is justified.

### What this certifies—and what it does not

This calculation certifies the actual finite boundary solve, including its nontrivial Schur matrix, at the original $u=0$. It does not evaluate the weighted pairings of its symbolic boundary columns, and therefore does not yield $4N$ or $8H$.

---

## 8. Complete force and the logarithmic budget

The actual normalization is unchanged:


$$
\mathsf a=\mathcal RA^{-1}f,\qquad
\mathsf b=\mathcal RA^{-1}r+W_be_b,
$$




$$
r=\frac{h^e+h^F-A(j!)_{0\le j<b}}{b!}.
$$


The desired outputs are


$$
D_{\rm raw}=4N,\qquad E_{\rm raw}=8H.
$$



For the normalized exponential force retain


$$
\boxed{
r_i^e\equiv
\sum_{\substack{a,t\ge0\\a+v_2(t!)<20}}
\sum_{s=0}^{4a}
\lambda_s^{(a)}
\binom{n+i}{s}
t!\binom{b+t}{t}
\binom{2n+i-s}{b+t}
\pmod q,
}
$$


with every original valid-term guard.

At this precision $t\le23$ and $s\le76$. This is a bounded set of force labels, not permission to keep only $s=t=0$.

The first force can be truncated only through its accepted factorial budget:


$$
D_{\rm raw}\equiv\sum_{i=0}^{47}f_iw_i\pmod q,
\qquad w=A^{-T}\mathcal R^T\mathsf a.
$$


The $f_i$ here are the complete actual coefficients.

### Logarithmic protection at the requested index

The accepted threshold is


$$
K_{\rm norm}
=
1+v_2((n/2)!)-v_2(b!)
-\lfloor\log_2(2n+b-1)\rfloor.
$$


Since $n/2=2001b$, Legendre’s formula gives


$$
K_{\rm norm}
=
1+2000b-s_2(2001b)+s_2(b)
-\lfloor\log_2(8005b-1)\rfloor.
$$


Here $2001b<2^{69}$ and $8005b-1<2^{71}$, so


$$
K_{\rm norm}\ge2000b-138>20.
$$


Thus omission of the complete logarithmic force is justified for these **absolute twenty-bit outputs**. This argument does not justify omission at arbitrary norm-relative precision.

The exterior $+1$ remains incorporated through


$$
\mathcal R(j!)=-e_0+b!W_be_b,
$$


and therefore


$$
\boxed{
D_{\rm raw}=w^Tf,\qquad
E_{\rm raw}=w^Tr+W_b\mathsf a_b.
}
$$


The endpoint contribution is not removed by the rational lifts or the Schur certificate.

---

## 9. Norm cancellation and nonvanishing

Let


$$
d=v_2(D_{\rm raw}),\qquad e=v_2(E_{\rm raw}).
$$


Because


$$
\frac HN=\frac{E_{\rm raw}}{2D_{\rm raw}},
$$


relative precision $2^s$ is sufficiently protected by


$$
M_E\ge s+d+1,\qquad
M_D\ge s+2d+1-e,
$$


together with $M_E>e$, $M_D>d$.

The assignment’s baseline $M=20$ does not certify that these conditions hold. In particular, a zero Gram residue modulo $2^{20}$ would give only a lower valuation bound.

For an approximate first column with coordinate error depth $T$, retain the distinct error budgets:

* squared approximate norm:
  

$$
\min(T+a+1,2T);
$$


* one-sided contraction against the exact first force:
  

$$
T+a;
$$


* mixed contraction against the exact second column:
  

$$
T+c.
$$



No new mixed nonvanishing result follows from this turn. Previously accepted nonvanishing is reused only at its stated original-family scope.

---

## 10. Exact next lemma and bounded inspection request

### Follow-on lemma

The outstanding computational lemma can now be stated more sharply:

> For the fixed polynomials $Q_U,Q_L,Q_B$ above, construct a sparse or observable-quotient implementation of the explicit Cartier transition (4.1), along the actual original target digit paths and their degree-76 divided-power descendants. Include all finite-Schur pairings and all complete-force labels. Prove bounds for the number of stored coefficients and modular operations, and preserve the coefficient targets encoding $b-1-i$.

A concrete success criterion would be an inspected list of transition numerators or compressed linear operators with measured support sizes, accompanied by exact reconstruction identities. An unexplained assertion of a small automaton is not enough.

### Recommended bounded computation now

**Inputs**

* the original $b,n$ above;
* $q=2^{20}$, $m=76$;
* the actual symbol and inverse recurrences in §1.1.

**Calculation**

1. Generate $F_{j,r}$ on $b-152\le j<b$, $0\le r<76$.
2. Generate $\overline K$, $G$, and $S_{\rm end}=I+G\overline K$.
3. Invert $S_{\rm end}$ modulo $q$.
4. Independently generate the adjoint Schur matrix and compare it with $S_{\rm end}^T$.
5. Verify both inverse products.
6. Report the actual matrices, or an inspectable complete residue table, not only a PASS label.

**Expected verifiable output**



$$
S_{\rm end}\equiv I\pmod2,
$$




$$
S_{\rm end}S_{\rm end}^{-1}
=S_{\rm end}^{-1}S_{\rm end}
=I\pmod q,
$$


and zero transpose-comparison residuals.

The receipt should explicitly state:

* largest binomial lower index: $227$;
* largest matrix dimension: $76$;
* no original-length array;
* no claim of a Gram or relative-output certificate.

This is narrower than the full assignment, but it is original-index, bounded, and advances the finite endpoint layer rather than repeating the supplied commutator check.

---

## 11. Full gcd, primitive denominator, and whole evaluated error

Nothing in the coefficient extraction changes the final arithmetic.

With the least actual two-column clearer $d_B$, retain


$$
A_B=N_{B,1}^T\Omega N_{B,1}>0,\qquad
H_B=N_{B,1}^T\Omega N_{B,2},
$$


and the full reduction


$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=\frac{A_B}{g_B},\qquad
p_n=\frac{H_B}{g_B}.
}
$$


The primitive multiplier is


$$
\frac{d_B^2}{g_B}.
$$


Every prime in $g_B$ matters.

The retained binary interface is


$$
v_2(q_n)=
\max\left\{
0,\frac{3n}{2}-v_2(b!)-s_2(n)-1-(\gamma-\alpha)
\right\},
$$


where $\alpha=v_2(N)$, $\gamma=v_2(H)$. No original value of $\gamma-\alpha$ has been established here.

Under the accepted complete signed-error theorem,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi)<0
\quad\text{eventually},
$$


and


$$
\log|\epsilon_n|
=
-\left(2+\frac1{4002}\right)n\log(1+\sqrt2)+o(n).
$$


The relevant whole evaluated form is


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n>0
\quad\text{eventually}.
}
$$



Irrationality by this route requires a same-index estimate forcing this complete nonzero quantity to tend to zero. Even an evaluated original twenty-bit Gram pair would not supply the required all-prime primitive-denominator bound.

---

## Conclusion: new result and proof status

The new rigorous result is a **fixed-denominator, ordinary rational lift of the actual weighted first-layer kernels**, including the finite upper endpoint, together with explicit integral prime-power Cartier transitions and concrete twenty-bit degree bounds.

A second rigorous reduction shows that the **actual finite endpoint Schur matrix** is computable with lower binomial indices at most $227$, using a few million modular arithmetic operations rather than any original-length array.

The remaining bottlenecks are:

1. **Computational:** prove and implement a small sparse or observable representation for the actual weighted Cartier paths and all degree-76 finite-boundary descendants.
2. **Local arithmetic:** evaluate the complete raw pair, detect its first nonzero digits, and pay the true norm cancellation.
3. **Family theorem:** establish any required relative-output relation on the original indices, rather than extrapolate a finite receipt.
4. **Global arithmetic:** control the full gcd and actual primitive denominator against the whole signed approximation error.

The dense state-growth estimates identify why the straightforward fixed-variable method is not yet a feasible full computation. They do not rule out a better specialized modular scheme.



$$
\boxed{\text{The irrationality or rationality of }e+\pi
\text{ remains unconditionally unresolved.}}
$$


