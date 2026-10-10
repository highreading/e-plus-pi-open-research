> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A4, Turn 4 — Certified branch elimination, a reconstructed-column relation, and the exact common-content obstruction

## Executive conclusion

The irrationality or rationality of $e+\pi$ remains unresolved.

The new binary calculation supports a substantial simplification, but **only at the stated precision and original index**:



$$
b=9^{18}=150094635296999121,\qquad
n=4002b=600678730458590482242,\qquad
Q=2^{20}.
$$



Inspection of the integral construction, its complete Laurent masks, and the supplied coefficient arrays establishes


$$
P_{f,1}=P_{e,1}=0
\quad\text{in }(\mathbb Z/Q\mathbb Z)[z].
$$


This is not an inference from 152 contact jets. The construction gives a bounded-degree polynomial identity; the supplied arrays certify every coefficient of its two vanishing branches.

There are two useful consequences.

1. **Both reconstructed columns have the same single denominator and polynomial numerators of degree $125$** after removing their common artificial Laurent shift:
   

$$
\widehat F(z)=\frac{V_f(z)}{(1-z)^{2n+125}},
   \qquad
   \widehat E(z)=\frac{V_e(z)}{(1-z)^{2n+125}}
   \pmod{2^{20}}.
$$


   Thus squared-weight extraction needs only one denominator-pair kernel, not four branch-pair kernels. The original finite row cutoff is unchanged.

2. **A further exact observable relation is visible in the complete reconstructed arrays:**
   

$$
V_f(z)\equiv z^3(1+z)^{122},\qquad
   V_e(z)\equiv(1+z)^{125}\pmod2.
$$


   Hence
   

$$
\boxed{(1+z)^3\widehat F(z)\equiv z^3\widehat E(z)\pmod2.}
$$


   This relation has a sharp lifting obstruction. Define
   

$$
Z(z)=\frac{(1+z)^3V_f(z)-z^3V_e(z)}2
   \pmod{2^{19}}.
$$


   Then $Z$ has degree $128$, with
   

$$
Z(0)=182059,\qquad [z^{128}]Z=270601,
$$


   both odd. The displayed relation therefore does **not** lift unchanged to modulus $4$.

For the endpoint-content program, A3 Turn 2’s two-kernel comparison is valid at its stated scope $p>n+2$, with the normalization-unit hypotheses retained. Its polynomial costs do not obscure the common structural content. Writing


$$
N_n=n^2+5n+3,
$$


one obtains the exact large-prime common-content identity


$$
\boxed{
\gcd(\gamma_0,\gamma_3)_{>n+2}
=
\gcd\!\left(D_{\rm mom}H,\,
D_{\rm mom}B_3^\partial,\,
N_n\right)_{>n+2}.
}
$$


At these common-content primes, both polynomial costs $Q_0,Q_3$ are units. This is compatible with—and sharper than using only—the product divisibility in A3.

None of these results computes the original weighted Gram pair, controls the actual all-prime final gcd uniformly, or establishes a same-index whole error tending to zero.

---

## 1. Scope, evidence, and retained boundaries

There are two distinct constructions here. They must not be conflated.

### 1.1 Endpoint families

The endpoint-content results retain


$$
n=15^r,\quad r\ge2,
\qquad\text{or}\qquad
n=105^r,\quad r\ge2.
$$


These indices are odd. The contact matrix is the original $3\times3$ matrix, both reconstructed columns retain all four coordinates, and the complete force ends at exactly $2n+2$.

The accepted $n=225$ calculation remains a calculation at that one index. Its row contents remain


$$
(508500,\ 28350,\ 15525,\ 772).
$$


The new specialized-resultant post-processing uses that archived producer and does not regenerate its force.

The coordinator’s scheduled original $n=3375=15^3$ producer has no completed result in the supplied material. I make no prediction about its entries or gcds.

### 1.2 Original binary index

The binary calculation concerns the single original $u=0$ index displayed above, with:


$$
m=76,\quad I=48,\quad R=100,\quad L_0=176,\quad K_0=124.
$$


Its accepted finite operator and Schur correction are not replacements for an infinite matrix. Their role is precisely to implement the original finite boundary.

The source and arrays now supplied establish finite statements modulo $2^{20}$. They do not establish exact vanishing in $\mathbb Z_2$, at higher precision, or at another index.

### 1.3 What was and was not inspected

This report inspects the supplied source algebra and complete numerator arrays. It does not represent a fresh execution of the coordinator programs.

The following are distinct:

- the bounded integral construction;
- the supplied exact coefficient arrays;
- the 656 Laurent/contact comparisons;
- the 656 reconstruction comparisons;
- an original weighted Gram calculation, which has **not** been performed.

The mod-$29$ controls mentioned in the assignment are also finite controls. Their numerical receipt is not reproduced among the complete sources here, so I do not add numerical claims about them.

---

## 2. The integral Laurent construction

Work in


$$
\mathcal R=\mathbb Z/2^{20}\mathbb Z,
\qquad
t(z)=(1-z)^{-n},
\qquad
B=b-1.
$$



Let $C_s$, $0\le s\le m$, denote the archived inverse-operator coefficients called `CC` in the source. The finite contact operator is


$$
[\Psi_+Y]_k
=
\sum_{s=0}^{m}
(-1)^s C_s
\binom{B-k}{s}Y_{k+s},
\qquad k\ge0.
$$



For the construction, it is useful to extend this operator to Laurent series. On a monomial,


$$
\Psi_L(z^r)
=
\sum_{s=0}^{m}
(-1)^s C_s
\binom{B-r+s}{s}z^{r-s}.
$$


If $Y$ is analytic, then


$$
\boxed{\Psi_+Y=\Pi_+\Psi_LY,}
\tag{2.1}
$$


where $\Pi_+$ retains nonnegative powers.

The prefix subtraction in `numerator_psi` implements exactly (2.1). In particular, it is applied to the **whole analytic source**, not separately to incomplete pieces.

### 2.1 The product formula used by the code

For an integer $a\ge0$,


$$
\begin{aligned}
\Psi_L\!\left(z^r(1-z)^{-a}\right)
={}&
\sum_{s=0}^{m}(-1)^sC_s
\sum_{e=0}^{s}(-1)^e
\binom{B-r+s-e}{s-e}
\binom{a+e-1}{e}\\
&\hspace{28mm}\cdot
z^{r-s+e}(1-z)^{-a-e}.
\end{aligned}
\tag{2.2}
$$


For $a=0$, only $e=0$ contributes.

This follows by applying the polynomial in the Euler operator to the product and using divided derivatives. It is also exactly the pattern in the code:

- `RISING_CHOOSE[r][s-e]`;
- `DERIV[extra][e]`;
- the shift $r-s+e+L_0$;
- the complementary factor $(1-z)^{K_0-\text{extra}-e}$.

No even integer is inverted in $\mathcal R$. The binomial coefficients are computed as integers before reduction. This is essential: interpreting the factorial quotients as modular divisions would invalidate the construction.

### 2.2 The load decomposition

For a finite load $\ell=(\ell_0,\ldots,\ell_{q-1})$, put


$$
T_r(z)=\sum_{e=0}^{r}(-1)^e\binom ne z^e,
$$




$$
A_\ell(z)=
\sum_{r=0}^{q-1}(-1)^r\ell_rz^{-r-1}T_r(z),
\qquad
\ell^-(z)=
\sum_{r=0}^{q-1}(-1)^r\ell_rz^{-r-1}.
$$


The analytic load is


$$
\boxed{Y_\ell=tA_\ell-\ell^-.}
\tag{2.3}
$$


Indeed, $tT_r-1$ starts in degree $r+1$.

Equation (2.3) explains the two outputs of `load_polynomials`. The negative Laurent part is not an optional correction: it is what makes the load analytic.

### 2.3 Why the masks cover the entire construction

The source ranges imply:

- direct first-force source: $0\le r\le47$, extra denominator exponent $48$;
- first-column Schur load: $-76\le r\le-1$;
- complete exponential load: $-100\le r\le-1$;
- inverse-operator order: $0\le s\le76$.

Consequently every high-denominator contribution fits in


$$
0\le \deg P_{\bullet,2}\le299.
$$


For example, the maximal degree from the first source is


$$
47+176+(124-48)=299.
$$


For a load source it is


$$
-1+176+124=299.
$$



The low-denominator branch, including the complete prefix subtraction and direct exponential exterior term, has degree at most $175$.

Thus the constructed identities have the form


$$
G_\bullet(z)
=
z^{-176}
\left(
\frac{P_{\bullet,2}(z)}{(1-z)^{2n+124}}
+
\frac{P_{\bullet,1}(z)}{(1-z)^n}
\right),
\tag{2.4}
$$


with precisely the finite masks used in the certificate.

There is no unrepresented polynomial tail beyond these masks. Once the numerator coefficients have been constructed, (2.4) is a formal Laurent-series identity at every coefficient, not merely at the checked jets.

---

## 3. What explains the vanishing $n$-branches?

A universal exact vanishing theorem is not supplied by the current sources. What can be proved is a precise principal-part characterization, followed by a complete precision-scoped certificate.

### 3.1 Principal-part characterization

Write each analytic contact source as


$$
Y_\bullet=Z_\bullet+C_\bullet,
$$


where:

- $Z_\bullet$ contains its $t=(1-z)^{-n}$ factor;
- $C_\bullet$ is a strictly negative Laurent polynomial.

For the first column, $C_f=\eta_f^-$. For the exponential contact source,


$$
C_e=-(h_{\rm out}-\eta_e)^-.
$$



Since $\Psi_L C_\bullet$ is still strictly negative,


$$
\begin{aligned}
\Psi_+Y_\bullet
&=\Psi_LZ_\bullet+\Psi_LC_\bullet
-\Pi_-\Psi_L(Z_\bullet+C_\bullet)\\
&=\Psi_LZ_\bullet-\Pi_-\Psi_LZ_\bullet.
\end{aligned}
$$


Therefore the low-denominator numerators are exactly


$$
\boxed{
P_{f,1}=-z^{176}\Pi_-\Psi_LZ_f,
}
\tag{3.1}
$$


and


$$
\boxed{
P_{e,1}
=
z^{176}\left(A_v-\Pi_-\Psi_LZ_e\right),
}
\tag{3.2}
$$


where $v$ is the retained factorial exterior load.

Hence the observed cancellation means:


$$
\Pi_-\Psi_LZ_f=0,
\qquad
\Pi_-\Psi_LZ_e=A_v
\pmod{2^{20}}.
\tag{3.3}
$$



This is a useful symbolic explanation: the vanished branches are precisely the residual principal-part mismatches after the finite Schur correction and the complete exponential exterior restoration.

It would be unjustified to promote (3.3) to all precisions merely because a Schur complement is present. At present, its complete verification is at $20$ bits.

### 3.2 The complete finite certificate

The supplied arrays give


$$
P_{f,1}[j]=P_{e,1}[j]=0
\qquad(0\le j<176).
$$


Together with the degree bounds just proved, this establishes


$$
\boxed{P_{f,1}=P_{e,1}=0\quad\text{in }\mathcal R[z].}
\tag{3.4}
$$



The surviving arrays have:


$$
\begin{array}{c|c|c|c}
 & \deg & \operatorname{ord}_z & \text{nonzero coefficients}\\ \hline
P_{f,2}&299&176&124\\
P_{e,2}&299&155&145.
\end{array}
$$



These are assertions about all their coefficients.

The independent comparisons provide additional corroboration:

- every Laurent coefficient from $-176$ through $-1$;
- contact coefficients $0,\ldots,151$;
- the analogous reconstructed coefficients;
- the exterior constant check.

They are valuable independent tests, but they are not being used as a uniqueness argument from 152 jets.

---

## 4. The exterior tail explains the reconstructed support

The reconstructed generating functions use


$$
\mathcal D=\theta-b-z,
\qquad \theta=z\frac{d}{dz}.
$$



The factorial exterior coefficients satisfy


$$
v_0=1,\qquad v_{r+1}=(b+r+1)v_r.
$$


Let


$$
E^-(z)=\sum_{r=0}^{23}(-1)^rv_rz^{-r-1}.
$$


Then, coefficient by coefficient,


$$
\boxed{\mathcal D E^-=-1\pmod{2^{20}},}
\tag{4.1}
$$


because all negative coefficients cancel by the recurrence and the terminal residual is $v_{24}=0$.

This proves the exterior contribution in the reconstructed constant term:


$$
[\mathcal DG_e]_0=-b[G_e]_0-1.
$$


It is the transformed form of the retained exterior $+1$, not permission to remove that correction.

### 4.1 The order $155$ is consistent with the exact exterior support

There is also a short valuation explanation for the surviving pole order.

Since


$$
b=9^{18}\equiv17\pmod{64},
$$


the valuations of the even factors among $b+1,\ldots,b+20$ sum to


$$
1+2+1+3+1+2+1+5+1+2=19.
$$


Thus


$$
v_2(v_{20})=19,\qquad v_2(v_{21})=20.
$$


Modulo $2^{20}$, the exterior principal part has pole order exactly $21$, with leading coefficient $2^{19}$.

Therefore


$$
176-21=155
$$


is the expected first possible exponent of $P_{e,2}$, and the supplied coefficient there is indeed $524288$.

This sharpens the safe length-$24$ exterior truncation without changing it.

### 4.2 Reconstructed numerators of degree $125$

Let


$$
A=2n+124.
$$


For a Laurent numerator $P$, reconstruction gives


$$
\mathcal D\!\left(z^{-176}P(1-z)^{-A}\right)
=
z^{-176}(1-z)^{-A-1}\mathcal H(P),
$$


where


$$
\boxed{
\mathcal H(P)
=
(1-z)\bigl(zP'-(b+176+z)P\bigr)+AzP.
}
\tag{4.2}
$$


This is the source’s `reconstruct` formula.

For the first column, analyticity already gives the factor $z^{176}$. For the exponential column, (4.1) proves that reconstruction kills every negative Laurent coefficient. Hence it also has that factor.

The supplied reconstructed arrays therefore give polynomials


$$
V_f=z^{-176}\mathcal H(P_{f,2}),
\qquad
V_e=z^{-176}\mathcal H(P_{e,2}),
$$


both of degree $125$, and


$$
\boxed{
\widehat F=\frac{V_f}{(1-z)^{2n+125}},
\qquad
\widehat E=\frac{V_e}{(1-z)^{2n+125}}
\pmod{2^{20}}.
}
\tag{4.3}
$$



The original degree $301$ masks remain correct; the new statement removes their certified common factor $z^{176}$.

---

## 5. A new exact observable relation from the complete arrays

The parity masks of the two degree-$125$ reconstructed numerators are especially simple.

For $V_f$, the odd coefficients occur exactly at


$$
j\equiv3,5\pmod8,\qquad 0\le j\le125.
$$


For $V_e$, they occur exactly at


$$
j\equiv0,1\pmod4,\qquad 0\le j\le125.
$$



These masks are read from the complete reconstructed arrays, not inferred from the response jets. In $\mathbb F_2[z]$,


$$
\begin{aligned}
V_f
&=(z^3+z^5)(1+z^8+\cdots+z^{120})
=z^3(1+z)^{122},\\
V_e
&=(1+z)(1+z^4+\cdots+z^{124})
=(1+z)^{125}.
\end{aligned}
$$


Consequently,


$$
\boxed{(1+z)^3V_f=z^3V_e\pmod2.}
\tag{5.1}
$$



Because both columns have the same denominator, this proves the all-coefficient formal-series relation


$$
\boxed{(1+z)^3\widehat F=z^3\widehat E\pmod2.}
\tag{5.2}
$$



### 5.1 A sharp lifted defect

Define


$$
Z(z)=
\frac{(1+z)^3V_f(z)-z^3V_e(z)}2
\in(\mathbb Z/2^{19}\mathbb Z)[z].
\tag{5.3}
$$


Division by $2$ here is legitimate after the proved coefficientwise evenness. It loses exactly one bit.

The supplied endpoint coefficients give


$$
V_f(0)=364118,\quad
[z^{125}]V_f=798223,\quad
[z^{125}]V_e=257021.
$$


Therefore


$$
Z(0)=182059,
\qquad
[z^{128}]Z
=\frac{798223-257021}{2}=270601.
\tag{5.4}
$$


Both are odd.

Thus:

- $Z$ has degree exactly $128$ modulo $2^{19}$;
- the uncorrected relation (5.2) fails modulo $4$;
- there is a fully specified bounded-degree lifting defect.

Put


$$
W(z)=\frac{Z(z)}{(1-z)^{2n+125}}\pmod{2^{19}}.
$$


Then


$$
\boxed{
(1+z)^3\widehat F-z^3\widehat E=2W
\pmod{2^{20}}.
}
\tag{5.5}
$$


For every $k\ge0$, the rational-series coefficients obey


$$
\boxed{
\widehat E_k
=
\widehat F_{k+3}
+3\widehat F_{k+2}
+3\widehat F_{k+1}
+\widehat F_k
-2W_{k+3}
\pmod{2^{20}}.
}
\tag{5.6}
$$



This is a new exact observable relation. It reduces the exponential column to four shifts of the first column plus an explicit one-bit-deeper defect. It does **not** say that the defect is norm-negligible.

---

## 6. Consequences for the actual squared-weight extraction

Let $\mathcal I_{\rm orig}$ denote the original reconstructed-row set, in the coefficient orientation used by (4.3), and let $\omega_k$ be the corresponding original unsquared weights. Both must be imported unchanged from the original norm definition.

The supplied sources here do not spell out that complete metric and its row endpoints. I therefore do not silently identify it with a full Hahn measure or replace its endpoint by $151$, $125$, or an infinite sum.

Set


$$
a=2n+125,
\qquad
u_r(k)=
\begin{cases}
\displaystyle\binom{a+k-r-1}{k-r},&k\ge r,\\
0,&k<r.
\end{cases}
$$


The one surviving kernel is


$$
\boxed{
K_{r,s}^{\rm orig}
=
\sum_{k\in\mathcal I_{\rm orig}}
\omega_k^2\,u_r(k)u_s(k),
\qquad 0\le r,s\le125.
}
\tag{6.1}
$$


Then


$$
\langle\widehat F,\widehat F\rangle
=V_f^{\,T}K^{\rm orig}V_f,
\qquad
\langle\widehat F,\widehat E\rangle
=V_f^{\,T}K^{\rm orig}V_e
\pmod{2^{20}}.
\tag{6.2}
$$



The practical improvement is exact:

- two branch denominators per column have become one;
- four possible denominator-pair channels have become one;
- the reconstructed numerator masks have shrunk from $302$ slots to $126$.

No row or weight has been discarded.

### 6.1 A finite-cutoff observable identity

Define, using the same original row set,


$$
C_r=
\sum_{k\in\mathcal I_{\rm orig}}
\omega_k^2\widehat F_k\widehat F_{k+r},
\qquad
D_3=
\sum_{k\in\mathcal I_{\rm orig}}
\omega_k^2\widehat F_kW_{k+3}.
$$


Equation (5.6) gives


$$
\boxed{
\langle\widehat F,\widehat E\rangle
=
C_3+3C_2+3C_1+C_0-2D_3
\pmod{2^{20}}.
}
\tag{6.3}
$$



At the upper end of the original row range, the shifted coefficients in this formula are coefficients of the explicit rational extension (4.3). They must be retained as terminal terms; they cannot be replaced by zero padding.

Equation (6.3) is useful for designing an observable extraction, but neither side has been evaluated for the original weighted target.

### 6.2 The remaining computational lemma

A concrete next lemma is:

> **Original finite squared-weight extraction lemma.**  
> For the original metric and original row endpoints, evaluate the two contractions in (6.2), or an equivalent set of observables in (6.3), by a division-free prime-power procedure whose reachable-and-observable size is explicitly bounded for this input.

The rational/diagonal and creative-telescoping literature supplies background methods. It does not, by itself, prove that the required observable module is small or that a recurrence can be propagated through its nonunit leading coefficients.

The branch reduction makes this target more economical. It does not close it.

---

## 7. Audit of A3 Turn 2’s two-kernel comparison

I retain A3’s notation:


$$
H=b+(n-3)c-2(n-1)d,\qquad K=2d-c,
$$




$$
B_0^\partial=3K-(n+3)c,\qquad
B_3^\partial=(n+2)K-c,
$$




$$
Q_0=n^2+6n+4,\qquad Q_3=n^2+4n+1.
$$



### 7.1 The complete resultant

The cancellation of $B_n$ from the common resultant is algebraically valid:


$$
\mathcal F=\frac{D^2L^2}{n+1}\Theta,
$$


with


$$
\begin{aligned}
\Theta={}&
H\left((-1)^nn!\mathscr S_n-\tau_nF_n
+2(n+1)d\tau_{n+1}\right)\\
&+(n+1)K
\left(\tau_{n+1}\bigl(2(n-1)d+3c\bigr)-\tau_nK\right).
\end{aligned}
\tag{7.1}
$$


The complete displacement $\mathscr S_n$, terminal coefficient $F_n$, and exterior correction all survive. There is no legitimate further universal division by $H$.

### 7.2 Normalization units

For $p>n+2$:

- the moment clearers and the relevant factorials are units;
- the reference-plane normalization is integral and unimodular at the required places;
- the fixed reference Wronskian supplies the primitive reference pair;
- the primitive-row normalization must still use the actual evaluated exponential coordinate.

Under those hypotheses, A3’s no-loss assertion


$$
v_p(\gamma_j)
=
\min\{v_p(r_jv),v_p(r_jw)\}
$$


is justified by the actual exterior-corrected exponential column. It is not a free-triple assertion.

The two-kernel comparison then gives


$$
(\mathcal C_j^\sharp)_{>n+2}
\mid \mathfrak D_j
\mid (Q_j)_{>n+2}(\mathcal C_j^\sharp)_{>n+2},
$$


and the actual denominator comparison


$$
(d_j)_{>n+2}
\mid \widehat K_j
\mid (Q_j)_{>n+2}(d_j)_{>n+2}.
\tag{7.2}
$$



### 7.3 Multiplicity costs must not be conflated

The denominator comparison in (7.2) has a **single** $Q_j$ cost. That follows from the correlated structural and force-content valuations in A3’s proof.

It would not be valid to obtain the same single cost merely by multiplying the two separate content comparisons. For an unrestricted product of structural and force-content distortions, the separate estimates can allow a $Q_j^2$ cost.

A3’s $O(\log n)$ conclusion survives either way, but an exact multiplicative statement must distinguish these operations.

For the denominator imbalance itself, the proved statement is


$$
\left|
v_p(|AB|)-v_p(\widehat Z)
\right|
\le v_p(Q_0Q_3),
\qquad p>n+2.
\tag{7.3}
$$


It does not control the omitted smaller primes.

---

## 8. Exact common $\gamma$-content: the polynomial costs disappear there

Set


$$
N_n=n^2+5n+3.
$$


The defect identity is


$$
\boxed{
(n+2)B_0^\partial-3B_3^\partial=-N_nc.
}
\tag{8.1}
$$



At a prime $p>n+2$ dividing both defect gcds, the primitive moment-state argument makes $c$ a unit. Hence (8.1) forces $p\mid N_n$.

Now


$$
Q_0-N_n=n+1,\qquad N_n-Q_3=n+2.
$$


Thus


$$
\gcd(N_n,Q_0)=1,
\qquad
\gcd(N_n,Q_3)\mid3.
$$


On both retained original families, $3\mid n$, so $Q_3\equiv1\pmod3$. Therefore


$$
\boxed{\gcd(N_n,Q_0Q_3)=1.}
\tag{8.2}
$$



At every common large-prime structural-content prime, A3’s polynomial costs are consequently units. Its structural inequalities become equalities there.

Writing $D_{\rm mom}=2^n(n+2)!$, this proves


$$
\boxed{
\gcd(\gamma_0,\gamma_3)_{>n+2}
=
\gcd(D_{\rm mom}H,\,
D_{\rm mom}B_0^\partial,\,
D_{\rm mom}B_3^\partial)_{>n+2}.
}
\tag{8.3}
$$


Using (8.1) and the unit $c$,


$$
\boxed{
\gcd(\gamma_0,\gamma_3)_{>n+2}
=
\gcd(D_{\rm mom}H,\,
D_{\rm mom}B_3^\partial,\,
N_n)_{>n+2}.
}
\tag{8.4}
$$



This is the exact common-content comparison, rather than only


$$
\gamma_0\gamma_3\mid N_n\,\operatorname{num}(H)
$$


at large primes. In particular,


$$
\gcd(\gamma_0,\gamma_3)_{>n+2}\mid (N_n)_{>n+2}.
$$



It remains a common-content statement. It neither bounds each individual $\gamma_j$ by a polynomial nor estimates the complete-force gcd.

### 8.1 The prime $p=n+2$ is genuinely exceptional

The restriction $p>n+2$ is not cosmetic.

Clear the two reference columns by $2(n+2)$:


$$
v'=(2(n+2),\,n+2,\,n+1)^T,
$$




$$
w'=(0,\,n+2,\,2n+3)^T.
$$


If $p=n+2$ is prime, these reduce to the same nonzero line:


$$
v'\equiv w'\equiv(0,0,-1)^T\pmod p.
$$


Their annihilator is then two-dimensional, not the single normal line used in the large-prime argument.

Accordingly, neither (7.2) nor (8.4) may be extended to this prime without a separate calculation.

At $n=225$, the exceptional prime is $227$, and the accepted finite calculation covers it through the cutoff $>226$. At the scheduled $n=3375$,


$$
n+2=3377=11\cdot307
$$


is composite; there is no prime equal to $n+2$, though all smaller unselected primes still require their actual treatment.

---

## 9. Fixed exponential boundary and the limited counterexample

A3’s modified-seed example is correctly limited.

The replacement


$$
B_m^\dagger=B_m+6\rho_m
$$


preserves the displayed forced diagonal recurrence and terminal relation but changes the exponential initial boundary. Its evaluated modified force, including the exterior correction, produces the stated large-prime content $7$ at $n=2$.

Therefore it refutes only the proposition that the forced diagonal recurrence and terminal return **alone** imply large-prime support $1$.

It does not refute the original-family fixed-seed assertion. Conversely, it identifies the precise missing hypothesis in any attempted recurrence-only proof: the original exponential seed must enter the arithmetic argument.

The follow-on fixed-seed target remains concrete:


$$
U_0U_3\mathfrak D_0\mathfrak D_3,
$$


or the actual imbalance $\widehat Z$, must receive an infinite arithmetic estimate using that fixed seed. Real asymptotics of the displacement or moments do not bound these evaluated numerator gcds.

---

## 10. The new $n=225$ post-processing

The supplied source verifies the specialized identities on the archived original $n=225$ data:

- the determinant/moment identity;
- the actual force syzygies;
- the integer Bézout identities;
- the common-resultant law away from the exceptional moment;
- the specialized defect divisibilities.

The receipt reports


$$
\gcd(X_{0,>226},\mathcal F_{>226})
=
\gcd(X_{3,>226},\mathcal F_{>226})=1.
$$


It also reports one-digit exceptional-support factors. Since those factors are supported on primes $>226$, they must be $1$.

Thus this index has no hidden large-prime exceptional-$H$ contribution to those $X_j$, and the common-resultant gcd is genuinely trivial there.

The 521-digit moment numerator part and 1420-digit resultant part do not alter that finite conclusion. Nor do they establish an infinite support theorem.

No accepted producer, force calculation, post-processing, or enclosure calculation should be repeated.

---

## 11. The adjacent-polynomial correction

The factor-$2$ correction is valid. It can also be derived symbolically, rather than relying only on the 115 checked coefficients.

With the normalization in the supplied Bernstein source,


$$
c_i=
(-1)^m\frac{(1/2)_m}{m!}
\frac{(-m)_i(3m-\tfrac12)_i}{(1/2)_i\,i!},
$$


whereas the adjacent degree-$(m-1)$ polynomial has


$$
d_i=
(-1)^{m-1}\frac{(1/2)_{m-1}}{(m-1)!}
\frac{(1-m)_i(3m-\tfrac32)_i}{(1/2)_i\,i!}.
$$


For $0\le i<m$,


$$
\frac{d_i}{c_i}
=
-\frac{2m}{2m-1}
\frac{m-i}{m}
\frac{6m-3}{6m+2i-3}
=
\boxed{-\frac{6(m-i)}{6m+2i-3}.}
\tag{11.1}
$$


At $i=m$, both the stated formula and $d_m=0$ agree.

In particular,


$$
\frac{d_0}{c_0}=-\frac{2m}{2m-1},
$$


so the $m=2$ value is $-4/3$, not $-2/3$.

Any collision formula using the old $3\rho$ normalization is therefore unaccepted pending repair. The earlier abstract Bézout identity is logically separate and remains valid at its own hypotheses.

---

## 12. Matveev and the normalization intersection

The primary-literature conclusion stated in the assignment is sufficient for the intended normalization obstruction.

Let $p$ be a nearest integer to $q\log_3 4$. Then


$$
\Lambda=q\log4-p\log3\ne0,
$$


because $4^q\ne3^p$.

Matveev’s primary Corollary 2.3, with two fixed positive rational algebraic numbers and degree $D=1$, yields effective constants $c>0,K>0$ such that


$$
|\Lambda|\ge c q^{-K}.
$$


Equivalently,


$$
\boxed{\|q\log_3 4\|\ge c' q^{-K}.}
\tag{12.1}
$$


One may use the fixed numbers $4,3$, or equivalently $4/3,3$ after replacing the second integer coefficient.

Thus any proposed normalization intersection that requires


$$
\|q\log_3 4\|\le C e^{-\eta q}
$$


for unbounded $q$ is impossible. This does not exclude normalizations whose required accuracy is only polynomial, and it is not an irrationality theorem for $e+\pi$.

The evidence distinction is preserved:

- the coordinator reports reading the primary web text;
- the public direct PDF download returned $403$;
- no visual PDF-page inspection is claimed here.

---

## 13. Actual primitive denominator and whole error

The new binary contents and large-prime comparisons do not replace the final all-prime normalization.

For a reduced weight $\lambda=a/k$, retain


$$
J_{\rm wt}=B\widetilde v_0-A\widetilde v_3,
\qquad
T_{\rm wt}=aJ_{\rm wt}+kA\widetilde v_3,
$$




$$
F_{\rm gcd}
=\gcd(|A|,|a|)\gcd(|B|,|a-k|),
$$




$$
G=\gcd(k,|J_{\rm wt}|),
\qquad
H_{\rm gcd}
=
\gcd\!\left(h,\frac{|T_{\rm wt}|}{F_{\rm gcd}G}\right).
$$


The actual primitive pair is


$$
\boxed{
q_\lambda=
\frac{kh|AB|}{F_{\rm gcd}GH_{\rm gcd}},
\qquad
p_\lambda=
\operatorname{sgn}(AB)
\frac{T_{\rm wt}}{F_{\rm gcd}GH_{\rm gcd}}.
}
\tag{13.1}
$$


Every prime remains in these gcds.

The same-index whole error is


$$
\boxed{
q_\lambda(e+\pi)-p_\lambda
=
q_\lambda e_3\alpha_{n,2}
(\lambda-\Lambda_{n,2}).
}
\tag{13.2}
$$


The required irrationality criterion is still an infinite sequence with


$$
\boxed{
0<
q_\lambda|e_3\alpha_{n,2}|
\,|\lambda-\Lambda_{n,2}|
\longrightarrow0.
}
\tag{13.3}
$$



Neither a low-precision column relation nor cancellation of one reference component establishes (13.3).

In particular, the accepted absolute logarithmic omission bound in the binary calculation is not a norm-relative omission theorem. Subsequent normalization may lose precision; it cannot be ignored merely because the raw omitted contribution vanishes modulo $2^{20}$.

---

## 14. New bounded work and exact expected outputs

No completed coordinator calculation needs to be requested or regenerated.

### 14.1 Small new post-processing: the lifted observable defect

A genuinely new, bounded calculation can use only the supplied reconstructed numerator arrays:

1. remove their certified factor $z^{176}$;
2. form
   

$$
\Delta_{\rm obs}=(1+z)^3V_f-z^3V_e;
$$


3. verify coefficientwise evenness;
4. output
   

$$
Z=\Delta_{\rm obs}/2\pmod{2^{19}}.
$$



Its expected verifiable output is:

- a $129$-coefficient array;
- degree exactly $128$;
- constant coefficient $182059$;
- leading coefficient $270601$;
- zero residual in
  

$$
(1+z)^3V_f-z^3V_e-2Z\pmod{2^{20}}.
$$



This is post-processing, not regeneration of the numerator construction. The two odd endpoint coefficients already prove that the uncorrected parity relation cannot lift to modulus $4$.

### 14.2 The outstanding original weighted calculation

The genuinely missing original calculation is the weighted Gram pair.

Its inputs should be:

- the two degree-$125$ numerator arrays;
- the common exponent $2n+125$;
- the original finite row cutoff and original squared weights;
- the retained normalization units and terminal terms.

Its expected verifiable output is:

- exact residues of the two required contractions modulo $2^{20}$;
- exact valuations when a residue is nonzero;
- only lower valuation bounds when a residue is zero;
- a boundary certificate showing that the original cutoff, not an infinite or standard Hahn cutoff, was used.

The feasibility of a suitably small extraction module remains an outstanding lemma, not a completed computation.

### 14.3 The already scheduled $n=3375$ index

The coordinator’s one original integer-recurrence producer should stand as scheduled, with all eight entries. No result is yet known.

For interpreting its eventual output, the relevant polynomials are


$$
N_n=11407503,\qquad
Q_0=11410879,\qquad
Q_3=11404126.
$$


The exact common-content identity (8.4) provides a check on its large-prime structural overlap. It does not predict that the complete-force contents will be $1$.

---

## 15. Proof-status ledger

| Statement | Status |
|---|---|
| Integral Laurent product formula and complete masks | Proved |
| Meaning of the vanished branches as principal-part mismatches | Proved |
| $P_{f,1}=P_{e,1}=0$ at original $u=0$, modulo $2^{20}$ | Complete finite coefficient certificate |
| Vanishing at all precisions or all original indices | Not proved |
| Reconstruction kills the complete exponential principal part and retains the exterior constant | Proved at the stated precision |
| Common reconstructed denominator with degree-$125$ numerators | Proved from construction and arrays |
| Parity relation $(1+z)^3\widehat F=z^3\widehat E$ | Complete finite-mask proof |
| Failure of that relation to lift unchanged modulo $4$ | Proved by the odd lifted defect coefficients |
| Original weighted Gram pair | Not computed |
| A3 two-kernel denominator comparison for $p>n+2$ | Valid with stated unit and fixed-force hypotheses |
| Exact common large-prime $\gamma$-gcd, equation (8.4) | Proved |
| Extension to a prime $p=n+2$ | Requires separate treatment |
| Infinite fixed-seed content bound | Open |
| Corrected adjacent coefficient ratio | Proved symbolically; finite receipt corroborates |
| Exponentially narrow logarithmic normalization intersection | Excluded by Matveev under the stated reduction |
| Successful actual primitive whole-error sequence | Open |

---

## Conclusion

The new result is a certified simplification of the original binary target, not merely a numerical pattern:



$$
\boxed{
\widehat F=\frac{V_f}{(1-z)^{2n+125}},
\qquad
\widehat E=\frac{V_e}{(1-z)^{2n+125}},
\qquad
\deg V_f=\deg V_e=125
\pmod{2^{20}}.
}
$$



The complete masks also yield the exact parity observable


$$
\boxed{(1+z)^3\widehat F\equiv z^3\widehat E\pmod2,}
$$


with an explicit degree-$128$, one-bit-deeper lifting defect. This gives a concrete reduced target for the still-unevaluated squared-weight extraction, while preserving every original row and terminal contribution.

On the endpoint side, the two-kernel comparison is compatible with the exact common structural-content formula


$$
\boxed{
\gcd(\gamma_0,\gamma_3)_{>n+2}
=
\gcd(D_{\rm mom}H,D_{\rm mom}B_3^\partial,n^2+5n+3)_{>n+2}.
}
$$


The polynomial costs $Q_0,Q_3$ do not occur at those common-content primes.

The remaining bottlenecks are exact and separate:

1. evaluate or control the **original finite weighted observables**, including norm-relative omission and normalization losses;
2. prove an **infinite fixed-seed arithmetic estimate** for the actual endpoint contents or denominator imbalance;
3. combine any such result with the **all-prime primitive denominator** and the **same-index whole error**.

None of those three obligations is closed by the present finite certificates.



$$
\boxed{\text{The irrationality or rationality of }e+\pi\text{ remains unresolved.}}
$$


