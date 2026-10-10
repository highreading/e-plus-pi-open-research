> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

## A4 audit result: partial independent PASS, with a precisely delimited remaining dependency

I do **not** claim a complete independent PASS for the original weighted theorem in this turn. The supplied closure data now address the previously requested finite-state objects; I am not treating those records as missing, nor treating an incomplete audit as a disproof of the author theorem.

The distinction is:

* The rational-Cartier transition, its initial rational-function construction, the phase bookkeeping, the linear-transfer interpretation, the boundary-support calculation, and the **complete scalar reconstruction from the reported terminal values** admit the paper checks below.
* The reported coefficientwise closure checks are reproducible finite evidence supplied by the coordinator. I have not independently recomputed every coefficient of those large arrays.
* The remaining paper dependency is upstream of those closures: identification of the actual coupled endpoint quotient with formula (8), including its binary responses, and identification of the displayed rational branch numerators with the actual moment branches. Their proofs are referenced in documents not included here in full. The closure records do not themselves establish these identifications.

The new follow-on result is stronger than merely saying that odd content is unknown: **the compact determinant estimate, combined with exactly the proved dyadic endpoint cancellation and no additional odd-content cancellation, gives an explicit majorant that grows at least like $\exp((\log 2)n^2/2+O(n\log n))$.** This is a failure of that particular available upper bound to certify shrinking—not a proof that the actual errors fail to shrink.

### 1. Rational norm machine: initial representation and exact transition

Work in


$$
\mathcal R=(\mathbb Z/8\mathbb Z)[x]/(x^4+x+1).
$$


Use the source’s $\zeta$, $\eta=\zeta^5$, and four-mode moment representation.

For Newton coefficients $c_t$, put


$$
a_s=\sum_{t=s}^4(-1)^{t-s}\binom ts c_t.
$$


The identity


$$
\binom rt=\sum_{s=0}^t(-1)^{t-s}\binom ts\binom{r+s}{s}
$$


gives


$$
\sum_{t=0}^4c_t\binom rt
 =\sum_{s=0}^4a_s\binom{r+s}{s}.
$$


Consequently a single mode has generating function


$$
\sum_{r\ge0}\zeta^r
 \left(\sum_{t=0}^4c_t\binom rt\right)Z^r
 =\sum_{s=0}^4\frac{a_s}{(1-\zeta Z)^{s+1}}.
$$


This verifies the `rise` conversion and the numerator powers $4-s$ used by `initial()`.

The period-three Fourier inversion is legitimate because $3^{-1}=3\pmod8$. For $p=(1,0,1)$, $r=(1,0,0)$,


$$
p_d=\sum_{a=0}^2\widehat p_a\eta^{ad},
\qquad
r_d=\sum_{a=0}^2\widehat r_a\eta^{ad}.
$$


Also


$$
[X^dY^e]F(uX+vY)
 =\binom{d+e}{d}\rho_{d+e}u^dv^e.
$$


Multiplication by $(1-X)^{-1}(1-Y)^{-1}$ converts extraction at $(m-1,m-1)$ into summation over $0\le d,e<m$. Thus, assuming the four-mode moment identity and the stated $x_0$, the rational function in equation (10) represents $x_0^TTBx_0$.

For $a\ne b$, interchanging $X,Y$ leaves diagonal extraction invariant. Hence the two ordered terms can be combined using


$$
\widehat p_a\widehat r_b+\widehat p_b\widehat r_a,
\quad
2(\widehat p_a\widehat p_b+\widehat r_a\widehat r_b),
$$


exactly as in the six-term construction. This combination is an identity for diagonal extraction; it need not be an equality between the original unsymmetrized rational functions.

Writing


$$
J=1-\zeta(\eta^aX+\eta^bY),\qquad
Q=(1-X)(1-Y)J^5,
$$


the construction is


$$
N=\sum_{s=0}^4 A_sJ^{4-s},\qquad P=NQ^3,
$$


so that $P/Q^4=N/Q$. Its degree in either variable is at most $4+18=22$.

Now let $\sigma$ be unramified Frobenius. Since


$$
Q^2=\sigma(Q)(X^2,Y^2)+2H
$$


for some polynomial $H$, expansion of the fourth power gives


$$
Q^8=\sigma(Q)(X^2,Y^2)^4\pmod8.
$$


Indeed every correction term is divisible by $8$. Therefore


$$
\Lambda_{1,1}\!\left(\frac P{Q^4}\right)
 =
 \frac{\Lambda_{1,1}(PQ^4)}{\sigma(Q)^4}.
$$


This proves the stated transition.

Since $\deg_X Q,\deg_YQ\le6$, a numerator box of side $24$ maps into itself:


$$
\deg_X\Lambda_{1,1}(PQ^4)
 \le\left\lfloor\frac{24+24-1}{2}\right\rfloor=23,
$$


and likewise for $Y$.

Finally, Newton sums for $x^4+x+1$ give


$$
\operatorname{Tr}(1)=4,\quad
\operatorname{Tr}(x)=\operatorname{Tr}(x^2)=0,\quad
\operatorname{Tr}(x^3)=-3.
$$


Thus the output functional $4a_0-3a_3$ is correct.

**Phase check.** The source phase at $h=6$ is $2$. One transition sends it to $3$, the phase at $h=3$. Therefore the reported equality of the six resulting polynomials is equality of the **whole state**, not merely equality of numerators with different denominators. Once that coefficient equality and reachability are checked, determinism proves period four for every later state.

**Status:** paper PASS for this representation construction and transition, conditional on the upstream moment and $x_0$ identities. The large coefficient equalities remain coordinator-checked evidence rather than a computation independently performed in this answer.

### 2. Linear transfer: interpretation and boundary terms

Let $M=m-1$. The binary inverse kernel is supported on


$$
d\mathbin{\mathrm{OR}}e=M.
$$


Writing


$$
d=32D+\ell,\qquad e=32E+u
$$


splits this into


$$
\ell\mathbin{\mathrm{OR}}u=31,\qquad
D\mathbin{\mathrm{OR}}E=2^{h-5}-1.
$$



Reading the remaining binary digits from the most significant end permits precisely


$$
(x,y)=(0,1),(1,0),(1,1).
$$


The accumulated residues therefore evolve as


$$
(a,b)\longmapsto(2a+x,2b+y)\pmod{15}.
$$


After fixing the top two left digits to quarter $q$, the initial right-quarter weight is


$$
V_q(q,b)=\kappa_b\quad(q\mathbin{\mathrm{OR}}b=3).
$$


There remain $h-7$ bulk digits. This proves the interpretation of the four initial vectors and the bulk-step count.

For any valid periodic left row $L_{q,s}(d)$, its terminal functional is exactly


$$
\sum_{\substack{0\le\ell,u<32\\ \ell\mathrm{OR}u=31}}
\sum_{s,t=0}^1
L_{q,s}(32a+\ell)\,
c_{st}\!\left(2M-32a-\ell-32b-u\right)
\rho_{m+32b+u}(b_{2+t}),
$$


with the source’s residue reductions. This is the mathematical meaning of `terminal()`. The right-quarter factor $\kappa_b$ is already in the initial vector; it must not be inserted again.

The common transition is independent of $h$. Hence a verified equality


$$
(V_0,V_1,V_2,V_3)_{11}
 =(V_0,V_1,V_2,V_3)_3
$$


proves period eight from step three onward. The two terminal phases also repeat under $h\mapsto h+8$.

#### Both-last-coordinate correction

For $0<e<m=2^h$,


$$
v_2\binom{m-1+e}{e}=h-v_2(e).
$$


For example, this follows from


$$
\binom{m-1+e}{e}
 =\frac me\binom{m-1+e}{e-1},
$$


whose last binomial factor is odd by Lucas’s theorem.

The boundary row has an extra factor $2$. Modulo $8$, it therefore vanishes except at $e=0,m/2$. At $e=m/2$ its binomial coefficient is $2\pmod4$. This proves precisely the two boundary-row formulas in the theorem.

At $d=0$, the OR condition forces $e=M$. At $d=m/2$, it permits only $e=m/2-1,M$. Thus the point responses really are one- and two-term sums, respectively. In particular, the second kernel residue is $m/2-1$, not $m/4-1$.

For the supplied point values, the boundary contraction is


$$
(2,2)\cdot(7,7)+(0,0)\cdot(0,2)=28\equiv4\pmod8.
$$


For the left correction, XOR with $1$ changes a binary integer $a$ by $1-2a$. The two displayed phase tables start with $(1,1)$ and $(0,0)$. Their corrections give respectively


$$
(-1,-1)\cdot(7,7)\equiv2\pmod4,
\qquad
(1,1)\cdot(7,7)\equiv2\pmod4.
$$


Both left boundary constants are therefore correct.

**Status:** paper PASS for the transfer interpretation, boundary support, point-support formula, and arithmetic of the displayed boundary constants. This does not by itself verify every entry of the periodic left and right row tables.

### 3. Modulo-eight branch: what is checked and what is not

For an integral ordinary series,


$$
F(u-2)=F-2F'+2F''\pmod8
$$


is valid coefficientwise: the Taylor term of order $r\ge3$ has coefficients divisible by $2^r$.

Starting from the asserted functional equation, one obtains


$$
F=Q-2RF'+2RF''.
$$


Modulo four, $F=Q-2RQ'$, because every second derivative of an integral series is even. Differentiating that congruence and substituting back gives


$$
F=Q-2RQ'+4R(RQ')'+2RQ''\pmod8.
$$


Thus the last term has correctly been retained.

The period proof also works. Write $u^{15}-1=DQ_0+2R_0$. In


$$
u^{480}-1=\sum_{a=1}^{32}\binom{32}{a}(u^{15}-1)^a,
$$


the terms $a=1,\ldots,4$ have $8$-divisible coefficients; those for $a=5,6$ have at least $16$; and for $a\ge7$, every term lacking five factors $D$ contains at least three factors $2R_0$. Hence


$$
D^5\mid u^{480}-1\quad\text{in }(\mathbb Z/8\mathbb Z)[u].
$$



**Precise remaining branch dependency:** the packet does not display the actual $M(u),c(u)$ used to derive the supplied O/E numerators. A numerator receipt and a stated denominator do not establish their equality to the actual moment branches. This is an identification dependency, not a missing closure-state record.

### 4. Full scalar reconstruction—no omitted correction

Denote the two terminal contractions by $L_{\rm base},R_{\rm base}$, and put $W=2w^T\omega$, where here $w$ means the additive binary-response lift used in the source, not the polynomial endpoint.

The complete formula is


$$
U\equiv q_0-2S_1-2E
 +2(L_{\rm base}+L_{\partial})
 -R_{\rm base}-R_{\partial}+W\pmod8.
$$


The supplied constants give:

* phase $m\bmod15=8$:
  

$$
E=0,\quad L_{\partial}=2,\quad R_{\partial}=4,
$$


  so
  

$$
U\equiv q_0-2S_1+2L_{\rm base}-R_{\rm base}+W;
$$


* phase $m\bmod15=2$:
  

$$
E=2,\quad L_{\partial}=2,\quad R_{\partial}=4,
$$


  so
  

$$
U\equiv q_0-2S_1+2L_{\rm base}-R_{\rm base}-4+W.
$$



Substitution in all six reported rows gives, before reduction modulo eight,


$$
12,\quad4,\quad4,\quad4,\quad12,\quad4.
$$


Every row therefore gives $U=4\pmod8$. This checks the **whole scalar reconstruction**, including the last constant and both boundary contractions.

**Precise remaining coupled dependency:** formula (8), the universal $x_0$, and the last response (9) are asserted with proofs referred to `WEIGHTED_ENDPOINT_CARRY_TRANSFER.md` and `WEIGHTED_ENDPOINT_PERIODIC_NORM_REDUCTION.md`. Their full derivations are not present here. In particular, a finite $h=7$ row-normalization check cannot substitute for the all-degree commutator/half-symmetric quadratic identity. I therefore do not promote this scalar arithmetic check into an independent proof of the original theorem.

### 5. Actual final gcd and denominator transfer

On the regular domain


$$
n=4^j+1,\quad j\ge1,\qquad
m=2^{2j-1},\quad k=m+1,\quad \sigma=n-2,
$$


the supplied endpoint interface says


$$
v_2(\alpha)=\gamma,\qquad
v_2(\beta)=\gamma+v_2(q_n(-1))-2\sigma.
$$


If the audited upstream identifications establish $U=4\pmod8$, then


$$
v_2(P_n(0))=2\sigma+2,\qquad
v_2(q_n(-1))=3n-2,
$$


and therefore


$$
v_2(\beta)=\gamma+n+2.
$$



For any positive odd simultaneous clearer $D$,


$$
g=\gcd(D\alpha,D\beta)
$$


has **exactly**


$$
v_2(g)=\gamma.
$$


Thus the actual primitive denominator, not a coefficient clearer, satisfies


$$
q=\frac{|D\beta|}{g},\qquad v_2(q)=n+2.
$$



For sign precision, let $\varepsilon=\operatorname{sgn}(\beta)$. Then


$$
p=-\varepsilon D\alpha/g,\qquad q=|D\beta|/g,
$$


and the whole evaluated error is


$$
q(e+\pi)-p
 =\varepsilon\frac Dg\bigl(\alpha+\beta(e+\pi)\bigr).
$$


Finite valuations imply $\alpha,\beta,q_n(-1)\ne0$. They do **not** imply that this last evaluated error is nonzero.

---

## 6. New weighted bottleneck lemma: an explicit compact determinant and a dyadic-only obstruction

This section uses the original weighted construction and its endpoint theorem as supplied; it does not assert that the independent audit above is complete.

### 6.1 Exact compact representation of the complete evaluated error

Set $Q=q_n$, $w=Q(-1)$. For $0\le s<n$, orthogonality gives


$$
A\!\left(x^{2s}Q(x^2)\right)=(-1)^sw.
$$


Changing variables in $A$,


$$
eA\!\left(x^{2s}Q(x^2)\right)
 =\sum_aQ_a(2s+2a)!
   +\int_0^1e^x x^{2s}Q(x^2)\,dx.
$$


Also, for every integer $r\ge0$,


$$
L_r=4\int_0^1\frac{x^{2r}-(-1)^r}{1+x^2}\,dx.
$$


Consequently


$$
R_{i\ell}+(e+\pi)w(-1)^{i+\ell}
 =\int_0^1
 \left(e^x+\frac4{1+x^2}\right)
 Q(x^2)x^{2i+2\ell}\,dx.                         \tag{16}
$$


Here $0\le i,\ell<k$, and $i+\ell\le2k-2=n-1$, so every use of orthogonality is within its domain.

Let $E$ be this matrix. Then, exactly,


$$
\alpha+\beta(e+\pi)=\det E.
$$


This retains all rational-arctangent contributions.

By determinant integration,


$$
\det E=\frac1{k!}\int_{[0,1]^k}
 \prod_{r=1}^k
 \left[\left(e^{x_r}+\frac4{1+x_r^2}\right)Q(x_r^2)\right]
 \prod_{r<t}(x_t^2-x_r^2)^2\,d\mathbf x.           \tag{17}
$$


No positivity is claimed: $Q(x_r^2)$ may change sign.

Put $M_Q=\sup_{0\le y\le1}|Q(y)|$. Since the positive weight in brackets is at most $e+4$,


$$
|\det E|\le (e+4)^k M_Q^k H_k,                    \tag{18}
$$


where the Cauchy determinant is explicitly


$$
H_k=\det_{0\le i,\ell<k}\frac1{2i+2\ell+1}
 =\frac{\displaystyle\prod_{0\le i<\ell<k}
                 [2(\ell-i)]^2}
        {\displaystyle\prod_{i,\ell=0}^{k-1}(2i+2\ell+1)}.
                                                               \tag{19}
$$



Using the accepted compact bound $M_Q\le |w|e^{C\sqrt n}$, with fixed $C\ge0$, gives the concrete primitive-error estimate


$$
|q(e+\pi)-p|
 \le \frac Dg\,(e+4)^k |w|^k e^{Ck\sqrt n}H_k.    \tag{20}
$$



### 6.2 The available dyadic cancellation cannot make this majorant shrink

Write


$$
g=2^\gamma g_{\rm odd}.
$$


If no lower bound for the additional odd content is used, the resulting certified majorant is


$$
B_n=D\,2^{-\gamma}(e+4)^k|w|^k e^{Ck\sqrt n}H_k. \tag{21}
$$


This is an explicit expression, not an unnamed determinant factor.

The dyadic theorem implies


$$
|w|\ge2^{3n-2}=2^{6k-5}.
$$


Moreover,


$$
\gamma=k(k-1)+2\sum_{i=0}^{k-1}v_2(i!)
 \le 2k(k-1),
$$


since $v_2(i!)\le i$. Therefore


$$
2^{-\gamma}|w|^k\ge 2^{4k^2-3k}.                 \tag{22}
$$



For completeness, formula (19) yields


$$
\log H_k=-2(\log2)k^2+O(k\log k).                \tag{23}
$$


Indeed, after extracting powers of $2$,


$$
\log H_k
 =-k\log2
  +2\sum_{j=1}^{k-1}\log(j!)
  -\sum_{i,j=0}^{k-1}\log(i+j+\tfrac12).
$$


Stirling summation gives


$$
2\sum_{j=1}^{k-1}\log(j!)
 =k^2\log k-\tfrac32k^2+O(k\log k),
$$


while the corresponding double Riemann sum gives


$$
\sum_{i,j=0}^{k-1}\log(i+j+\tfrac12)
 =k^2\log k+
   (2\log2-\tfrac32)k^2+O(k\log k).
$$


Their difference proves (23).

Since $D\ge1$ and the remaining factors in (21) are at least one,


$$
\boxed{\log B_n\ge2(\log2)k^2-O(k\log k).}         \tag{24}
$$


Equivalently,


$$
\log B_n\ge \tfrac12(\log2)n^2-O(n\log n).
$$



Thus **this compact bound plus the exact dyadic cancellation does not certify a shrinking primitive error**. Even its most optimistic use of $|w|$ leaves a positive quadratic exponent. This is only an obstruction to the available majorant; it supplies no lower bound for the actual error.

### 6.3 Why divided-basis arithmetic does not automatically supply the missing odd content

The actual paired divided basis has denominators


$$
D_d=2^dd!,\qquad 0\le d<m,
$$


each appearing twice. Relative to the integral monic $h$-basis, its lattice-index factor is


$$
J_m=\prod_{d=0}^{m-1}D_d^2.
$$


For every prime $p>m-1$, this change of basis is invertible over $\mathbb Z_p$. Hence it preserves all determinantal ideals over $\mathbb Z_p$: every transformed minor is a $\mathbb Z_p$-linear combination of original minors, and the inverse transformation gives the reverse inclusion.

In particular, **the basis conversion itself forces no new $p$-content for any $p>m-1$**. At smaller primes, its determinant factors still cannot simply be declared factors of


$$
\gcd(D\alpha,D\beta):
$$


that requires an endpoint-pair divisibility argument after evaluation and after retaining the rational $L_s$ terms.

This pinpoints what is absent from a saturation argument. Divided-basis integrality is not yet a lower bound for the odd part of the final evaluated endpoint gcd.

## Closing record

1. **New result and proof status.**  
   Paper checks establish the rational-Cartier construction and transition, correct phase closure implication, four-vector transfer interpretation, both boundary-support formulas, and full scalar reconstruction from the supplied terminal outputs. A complete independent PASS remains withheld only for dependencies not independently established here. The new compact determinant identity (16)–(19) is proved, and the explicit dyadic-only majorant obstruction (24) is proved using the supplied original endpoint theorem.

2. **Exact remaining bottleneck.**  
   For the audit: the actual-moment identification of the O/E rational branches and the all-degree coupled identity leading to formula (8), including its binary responses. For shrinking: a genuine lower bound for the **odd part of the final endpoint gcd**, or a substantially sharper estimate exploiting cancellation in (17). The present compact absolute-value bound loses at least the explicit quadratic amount in (24). Nonvanishing of the complete evaluated determinant must also be retained; it does not follow from the dyadic valuation alone.

3. **Bounded computation request.**  
   No new determinant nodes or repetition of the already checked closure orbits is requested. A useful remaining finite check is to regenerate, from the supplied four-mode coefficients and formulas, all terminal and quarter-row arrays in the two phases and compare them entrywise with the linear receipt. Inputs: the displayed moment coefficients, $\zeta$, $m\bmod15\in\{2,8\}$, four quarters, residues $0\le d<480$, and terminal residues $0\le a,b<15$. Expected verifiable output: zero discrepancies, or the first discrepancy with its phase, quarter, member/residue coordinates, and both values. This would audit finite table evaluation; it would not replace the remaining all-degree identification proofs.
