> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Research report: catalogue screening and the paid-denominator obstruction for $e+\pi$

## 1. Executive assessment

The global objective remains unresolved: **the supplied work does not prove either rationality or irrationality of $e+\pi$**.

This report screens every complete abstract supplied in shard 5. It does not claim to have read the other four shards or the primary manuscripts. The acquisition gate reports a complete collection-wide inventory, but an inventory is not a proof review. In particular:

- Family005 remains a priority manuscript under ongoing review, not an accepted proof of Catalan irrationality.
- Family017 and Family022 are ongoing readings outside this shard. No primary proof sections from either are supplied here.
- None of the abstracts in this shard gives a direct theorem implication establishing irrationality of $e+\pi$.

The strongest literature leads are:

1. **Family005:** potentially reusable signed-determinant arithmetic and energy estimates, subject to compatibility with the complete factorial forcing.
2. **Family020:** potentially useful determinant estimates with adaptive auxiliary primes, but only if an actual arithmetic-geometric encoding of the original scalar cofactors can be established.
3. **Family325:** potentially useful numerical-range bounds for the finite inverse matrices, but only for an analytical estimate and only after verifying numerical-range separation and normalization costs.

Family134 offers a weaker, combinatorial inspiration for finite-state descriptions of carry constraints. It does not establish finite-state control of the binary digits of $9^{18+32u}$.

The new mathematical contribution below is deliberately narrower: an exact derivation of the binary stream’s candidate **paid excess**, together with a pointwise conditional transfer to the normalized return. This identifies a concrete follow-on lemma without presenting a finite digit experiment as an infinitude proof.

---

## 2. Proof standard and the original research objects

Put


$$
\alpha=e+\pi.
$$


The approximation route must produce integers $p_n,q_n$, with $q_n>0$, on one infinite set of original indices, such that


$$
0<|q_n\alpha-p_n|\longrightarrow0.
$$


Indeed, if $\alpha=A/B$, with $A,B\in\mathbb Z$ and $B>0$, every nonzero such error has absolute value at least $1/B$.

This elementary criterion does not permit substituting:

- a small real residual before clearing denominators;
- a pole-only residual for the whole forced error;
- divisibility at one prime for the final all-prime gcd;
- a convenient denominator for the actual primitive denominator;
- separate infinite subsequences for different parts of the argument.

### 2.1 Binary stream retained in this report

The original domain is


$$
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
$$


The contact range is $0,\ldots,b-1$; physical reconstruction is on $0,\ldots,b$, with


$$
z_b=0.
$$


The complete columns are


$$
x=\frac12RA^{-1}f,\qquad
y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},
\qquad x=2^a x_0.
$$


Thus the exponential source, factorial source, correction $e_0$, factor $4b!$, and actual content $2^a$ all remain present.

The norm and the stated linear parity quantity are


$$
Q=x_0^{T}x_0,
$$




$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f,
\qquad
\frac{S}{2^{a+1}}\in\mathbb Z.
$$



The supplied scope marks the following as accepted: $a\ge1$, the full inverse modulo $8$, an exact two-binomial criterion for $a=1$, complete source integrality, and finite boundary completion. It marks the following as unreviewed or open:

- the asserted improvement $a\ge2$ on $u\equiv1\pmod4$;
- the complete short adjoint;
- the full-return estimate
  

$$
v_2(S)\ge1+\chi,\qquad
  \chi=v_2\binom{n+b-1}{b-1};
$$


- positive, growing **paid** excess after the actual content is removed.

The actual least simultaneous clearer, column contents, and primitive minor saturation must not be replaced by generic lattice surrogates. The known original primitive-denominator valuation remains


$$
v_3(q)=n-\frac{b+15}{2}.
$$


No new formula for the complete primitive denominator is asserted here: the supplied compact scope does not contain its full defining scalar formula.

### 2.2 Other streams are not interchangeable with this one

The catalogue screen must also respect the following transfer barriers.

| Stream | Original feature that a proposed transfer must retain |
|---|---|
| A1, ternary | The full moment functional, including $-3^h(2t)!/4$ and the pole term; recovered modular progression; fixed interior window; endpoint-diagonal factors and finite moment range. The directional estimate $C^{-1}z\in3^{-1}\mathbb Z_3$ remains open. |
| A2, prime $29$ | $b=3^{249005515+574312172u}$, $n=2001b$, $u\equiv2\pmod{29^9}$; complete force, physical endpoint, fixed digits, unit $\rho$, and upper finite boundary. A column-content bound does not bound the full norm valuation. |
| A3, endpoint | $n=15^r$ or $105^r$, $r\ge2$; complete forced companion, projected residual, and extra $j=0$ correction. The denominator retains $\lvert R_j\rvert/\gcd(R_j,C_j)$, $n!/\gcd(n!,\zeta_j)$, and the extra $F$ payment. |

Nothing in the abstract screen supplies an identity allowing these streams to share arithmetic gains.

---

## 3. Complete coverage ledger for shard 5

Counts below count linked papers, including separate versions when separately listed. Relevance decisions concern the present $e+\pi$ programme, not the intrinsic importance or correctness of the claimed results.

| Family | Papers | Relevance decision |
|---|---:|---|
| 005 | 1 | **Priority, ongoing review.** Signed irrationality construction may contain reusable identities; no accepted transfer. |
| 010 | 3 | Two-adic Galois/Hecke results; no attached representation encoding our scalars or periods. |
| 015 | 3 | Torus-packet equidistribution; no complete-packet realization of the original sparse indices. |
| 020 | 1 | **Secondary candidate.** Adaptive-prime determinant estimates might inform all-prime arithmetic. |
| 025 | 1 | Short unit-fraction expansions do not control the actual least clearer or whole error. |
| 030 | 1 | Elliptic-curve modularity; no mixed-period identification supplied. |
| 035 | 2 | Positive-characteristic abundance; no relevant threefold pair or arithmetic lattice construction. |
| 040 | 1 | Zero-cycle/Albanese theorem; no identified surface whose cycles encode the approximation. |
| 046 | 2 | Universal-cover counterexamples; no operative transfer. |
| 051 | 1 | Hyperbolic Kähler canonical ampleness; no compatible geometric object. |
| 056 | 5 | Minimal-model termination; finite termination is not scalar-content control. |
| 062 | 1 | Contact-Fano/quaternionic classification; no relevant period realization. |
| 067 | 1 | Nef-tangent classification; no identified application. |
| 073 | 1 | Distance-set positivity; measure-theoretic conclusion does not select our fixed arithmetic objects. |
| 078 | 1 | Fourier multiplier bounds; no kernel identity linking them to the complete error. |
| 083 | 1 | Short-scale directional Hilbert transform; no compatible operator representation. |
| 088 | 2 | Projection-body inequalities/counterexample; real volume does not determine integral content. |
| 093 | 1 | Log-Sobolev estimate; no log-concave measure representing the signed forced functional. |
| 098 | 1 | Banach embedding obstruction; no arithmetic consequence identified. |
| 103 | 1 | Derandomization claim; no specified randomized log-space subproblem in the proof obligation. |
| 108 | 1 | Determinantal-complexity lower bound; not nonvanishing or valuation of our evaluated determinants. |
| 113 | 2 | Matching counts and entropy; approximate positive counts do not certify signed scalar gcds. |
| 118 | 1 | Bin-packing integrality gaps; cautionary analogy only. |
| 124 | 1 | Boundary-aware dynamic programming; weak inspiration, no bounded-state arithmetic reduction. |
| 129 | 2 | Automaton lower bounds; warns against unjustified bounded-state compression. |
| 134 | 3 | **Heuristic lead.** Finite monoid descriptions might organize carry predicates if regularity is independently proved. |
| 139 | 1 | Sampling oracle complexity; unrestricted between-query computation and approximate output are incompatible with exact gcd certification. |
| 144 | 1 | Constructed smooth spectrum; no representation of the original sequence. |
| 149 | 2 | Mass-action permanence; no positive dynamical system representing the signed forcing. |
| 154 | 4 | Almost-everywhere mixing averages; cannot select a prescribed orbit or sparse arithmetic indices. |
| 159 | 1 | Progressions from divergent reciprocal sums; original exponential index sets have convergent reciprocal sums. |
| 165 | 2 | Graph crossing formulas; no graph model of the scalar obstruction. |
| 170 | 2 | Ramsey logarithmic exponents; no deterministic content bound supplied. |
| 175 | 3 | Expectation thresholds/discrete convexity; probabilistic covers are not same-index certificates. |
| 180 | 1 | Hamiltonian-cycle existence; no compatible graph encoding. |
| 185 | 1 | Infinite matroid counterexamples; not applicable to the finite integral frames. |
| 190 | 1 | Ordered matrix removal obstruction; combinatorial pattern density is not exact valuation. |
| 195 | 1 | Local-domain counterexample; no relevant local ring realization. |
| 200 | 2 | Hilbert/Betti comparison over characteristic zero; does not preserve evaluated integral lattices or paid divisions. |
| 205 | 2 | Representation support in tensor squares; no integral scalar-cofactor control. |
| 210 | 2 | Complex equivariant maps; rational/integral normalization costs absent. |
| 215 | 5 | Continuum/mass-gap statements, including an explicit $e,\pi$ prefactor; no integer approximation construction. |
| 220 | 3 | Random-environment laws; probabilistic hypotheses do not hold for the fixed sequences. |
| 225 | 1 | Gaussian field variance involving $\arcsin$; a normalization identity is not irrationality. |
| 230 | 2 | Almost-sure SLE gauges; no deterministic arithmetic transfer. |
| 235 | 4 | Computability/certificate inspiration only; computability of a real does not decide rationality. |
| 240 | 2 | Categoricity thresholds; no mathematical bridge to the finite approximation problem. |
| 245 | 1 | Type-system normalization; unrelated to factorial or rational normalization here. |
| 250 | 3 | Group embeddings; no useful encoding with quantitative arithmetic bounds. |
| 255 | 1 | Quasi-isometric recognition; no relevant group model. |
| 260 | 13 | Geometric inequalities carefully retaining original data; methodological analogy, not an arithmetic tool. |
| 265 | 2 | Full-gap area laws and approximate tensor networks; approximate compression does not preserve exact integral contents. |
| 270 | 2 | Spectral bound states; no finite-matrix/source identification. |
| 275 | 2 | Continuum hardness; no reduction to the particular exact calculations required here. |
| 280 | 1 | Unitary VOA/net equivalence; no mixed-period or lattice realization. |
| 285 | 3 | Irrational projection trace; no identity relating that trace to $e+\pi$. |
| 290 | 2 | Modular spectral recovery; “modular” here is not congruence arithmetic. |
| 295 | 1 | Bounded Hochschild primitives; no integral primitive-denominator implication. |
| 300 | 2 | Strong-operator paving; compression/approximation need not preserve finite endpoints or scalar cofactors. |
| 305 | 3 | Topological disk/tensor obstructions; not the rational tensor-gauge problem already settled in A3. |
| 310 | 1 | Rational homology for each prime; no all-prime gcd theorem for our integers. |
| 315 | 1 | $L^2$-Betti vanishing; no relevant analytical identity. |
| 320 | 1 | Aspherical-manifold counterexamples; no operative transfer. |
| 325 | 2 | **Analytical candidate.** Numerical-range functional calculus could bound a finite inverse if separation and costs are proved. |
| 330 | 1 | Failure of uniform bounded approximation; caution against assuming uniformity, not a new estimate. |
| 335 | 2 | Scalar curvature/simplicial volume; no compatible geometric construction. |
| 340 | 1 | Exact Lagrangian counterexample; “exact” has no denominator consequence. |
| 345 | 1 | Closed-geodesic infinitude; unrelated to infinitude of good arithmetic indices. |
| 350 | 3 | Nodal estimates/counterexamples; no PDE realization of the actual error. |
| 355 | 1 | Fixed-center flow uniqueness; methodological analogy only. |
| 360 | 2 | Transport regularity under weak MTW; no positive transport representation of the signed functional. |
| 365 | 3 | Boundary inverse problems; no identity with the finite forced inverse matrices. |
| 370 | 1 | Nonexistence for nonlinear elliptic systems; no compatible positive entire solution. |
| 375 | 1 | Stable/monotone PDE classification; no identified transfer. |

This covers **74 supplied families and 139 linked papers**. No primary manuscript proof has been validated merely by this ledger.

Several family descriptions are broader than individual abstracts. For example, Family134 contains separate claimed bounds of thirteen, four, and three; Family215 distinguishes spin correlations from the full transfer gap; and Family260 contains materially different area, charge, decay, and rigidity hypotheses. Such distinctions prevent collapsing a family into an unrestricted theorem.

---

## 4. Detailed assessment of the best candidates

### 4.1 Rank 1: Family005 — signed determinants and paid arithmetic

**Evidence supplied.** The abstract claims irrationality of Catalan’s constant but gives no method. The separate acquisition gate describes a mixed signed determinant, Taylor contact cancelling $\zeta(2)$, two odd-prime denominator layers, prime-index Frobenius nonvanishing, and a real energy estimate. These method descriptions are themselves claims awaiting proof inspection.

**Outstanding obligation it might address.** A genuinely new identity could potentially connect:

- determinant nonvanishing;
- whole signed error estimates;
- exact prime-by-prime clearing costs.

That combination is more relevant than the mere fact that the target constant is another classical constant.

**Decisive transfer hypothesis.** There must be an explicit identity transporting the proposed kernel or determinant to the **complete original forced functional**, with every normalization accounted for. In A1 this includes the factorial term; in A5 it includes $h^e+h^F$, the $e_0$ correction, $4b!$, and the terminal reconstruction.

A compact Catalan kernel is not a substitute for a factorial moment functional simply because both admit Chebyshev or determinant descriptions.

**Primary proof material required.** Before application, inspect the complete proofs of:

1. the mixed determinant identity and its sign conventions;
2. Taylor contact and cancellation of the unwanted period;
3. both odd-prime denominator layers;
4. Frobenius nonvanishing, including its exact index restrictions;
5. the energy estimate for the entire error;
6. the final arithmetic assembly after all divisions.

No section numbers are available in the supplied material; inventing them would falsely imply primary-source inspection.

**Classification.** Likely reusable *technique*, conditional on a specific new identity. No direct implication for $e+\pi$, and no completed validation of the Catalan claim in this report.

---

### 4.2 Rank 2: Family020 — adaptive-prime determinant estimates

**Claimed method.** Number-field factorization, determinant estimates with adaptive auxiliary primes, and explicit low-degree geometry establish squarefree or power-free values of certain fixed irreducible polynomials.

**Potential obligation.** The most relevant target is an all-prime scalar-cofactor estimate, rather than another fixed-prime content gain. Adaptive primes might provide a mechanism for treating prime divisors that depend on the index.

**Decisive transfer hypothesis.** One would need an explicit model in which the actual scalar pair defining the primitive denominator is represented by controlled polynomial or algebraic data, with:

- fixed or quantitatively controlled degree;
- explicit coefficient heights;
- the required irreducibility and local conditions;
- uniformity in every parameter that grows with $n$;
- a conclusion valid on the original exponentially sparse index set.

None of these hypotheses has been supplied for $Q=x_0^Tx_0$ and its companion scalar.

Even a proved positive density of good values among all integers would not suffice. A density-one set can omit an entire exponentially sparse sequence. Likewise, “no fixed prime-square divisor” is a local condition on polynomial values, not a theorem about the final gcd of two evaluated scalar expressions.

**Primary proof material required.**

- the adaptive auxiliary-prime selection argument;
- uniform determinant bounds, with all height and degree dependence;
- the large-prime tail estimate;
- the local-to-global density assembly;
- the treatment of primes dividing field/order indices or coefficient discriminants.

**Classification.** A promising arithmetic technique to inspect, not an applicable theorem at present.

---

### 4.3 Rank 3: Family325 — numerical ranges and finite inverse bounds

**Claimed method.** The complete Crouzeix inequality bounds matrix-valued functional calculus by twice the supremum over the numerical range. The second abstract claims extension to functions holomorphic near its closure.

**Potential obligation.** An explicit finite-matrix representation might give an archimedean bound for $A^{-1}f$, an adjoint, or a whole-error operator without diagonalizing a highly nonnormal matrix.

**Decisive transfer hypothesis.** For the actual finite matrix $A$, one must establish an enclosure of its numerical range that excludes zero:


$$
\delta=\operatorname{dist}(0,W(A))>0.
$$


The matrix must retain the original upper boundary and physical endpoint. Any similarity or basis change must be tracked in both norm and rational/integral normalization.

There is also an important reason not to overstate this candidate. For an ordinary inverse, numerical-range separation already gives the elementary bound


$$
\|A^{-1}\|\le\delta^{-1}.
$$


Indeed, for every unit vector $v$,


$$
\|Av\|\ge |\langle Av,v\rangle|\ge\delta.
$$


Thus the sharp Crouzeix theorem is not needed merely to bound $A^{-1}$. Its possible additional value lies in a more complicated polynomial or holomorphic operator expression.

Invertibility alone does not validate separation. For example,


$$
A=\begin{pmatrix}1&M\\0&1\end{pmatrix},\qquad M\ge2,
$$


is invertible, but for $v=(1,-1)/\sqrt2$,


$$
\langle Av,v\rangle=1-\frac M2.
$$


The numerical range contains both $1$ and a nonpositive real number, and hence contains zero.

**Primary proof material required.**

- the finite-dimensional matrix-valued inequality;
- the holomorphic extension if rational functions are used;
- boundary/degenerate numerical-range cases;
- the exact similarity assertion and its condition-number bound.

**Classification.** Potential analytical support. It supplies neither $3$-adic directional integrality nor an all-prime gcd bound. A real operator norm bound cannot be silently read as a $p$-adic inverse estimate.

---

### 4.4 Lower-priority inspiration: Family134

The claimed finite-monoid and prefix-code constructions suggest a way to organize an already finite-state carry problem. They do **not** prove that the full binary expansions of


$$
9^{18+32u}
$$


admit a fixed finite-state description as $u$ varies.

For a fixed precision $2^k$, the residues of these powers are periodic because they lie in the finite group $(\mathbb Z/2^k\mathbb Z)^\times$. But the digit-sum expressions relevant below depend on a number of bits growing with $u$. Fixed-precision periodicity therefore does not control the whole digit sum.

A useful transfer would first require a uniform finite-state encoding that retains all carries and terminal conditions. Only then would regular-language or finite-monoid techniques become applicable. The exact primary constructions and their state-size dependence would need inspection. Present status: heuristic inspiration, not a theorem application.

---

## 5. Priority papers outside this shard

### Family017

The gate describes a claimed irrationality exponent $2$ for $\pi$, using center-uniform multivariable interpolation and an integer determinant.

Even if correct, an irrationality-exponent theorem for $\pi$ alone does not prove irrationality of $e+\pi$. Under a hypothetical relation $e+\pi=r\in\mathbb Q$, the number $r-e$ is not itself a rational approximant to $\pi$; one must build and estimate a compatible mixed exponential/logarithmic integer construction.

The indispensable proof packets are the center-uniform interpolation theorem, determinant nonvanishing, denominator and error estimates, and all quantifiers. **None of those primary sections is supplied here.**

### Family022

The described theorem has an almost-everywhere quantifier in the variable $x$, even if the shift quantifier ranges over every real number. A fixed $x=e+\pi$ can remain in the exceptional set.

The useful possible component is a deterministic gcd/overlap estimate applicable to the original scalar sequences. Such a transfer would require the actual integer inputs, sparse-index restrictions, and complete normalizations. **No primary gcd/overlap proof section is included in this prompt**, so the ongoing reading cannot be reported as completed.

---

## 6. New exact result: the binary paid-excess identity

This section proves an elementary arithmetic statement on the original domain. It does not assume the unreviewed full-return theorem.

Let $s_2(m)$ denote the number of ones in the binary expansion of a nonnegative integer $m$. Define


$$
d=\frac{b-1}{4},\qquad
g=\frac{n/2+1}{2}=\frac{2001b+1}{2},
$$


and


$$
H=v_2\binom gd.
$$



### Proposition 1 — exact valuation difference on every original index

For every $u\ge0$, with $b=9^{18+32u}$ and $n=4002b$, the integers $d,g$ are valid binomial parameters and


$$
\boxed{\;
\chi-H
=
2s_2(4002b)-s_2(4003b-1)-s_2(4001b+3).
\;}
$$



#### Proof

The exponent $18+32u$ is even. Since $9^2\equiv1\pmod{16}$,


$$
b\equiv1\pmod{16}.
$$


Consequently $d$ and $g$ are integers, and


$$
g-d=\frac{4001b+3}{4}>0.
$$



Legendre’s formula at $2$ is


$$
v_2(m!)=m-s_2(m).
$$


Applying it to a binomial coefficient yields


$$
v_2\binom{r+s}{r}=s_2(r)+s_2(s)-s_2(r+s).
$$


Therefore


$$
\chi
=s_2(b-1)+s_2(n)-s_2(n+b-1),
$$


and


$$
H=s_2(d)+s_2(g-d)-s_2(g).
$$



Multiplication or exact division by a power of $2$ does not change binary digit sum. Thus


$$
s_2(d)=s_2(b-1),\qquad
s_2(g-d)=s_2(4001b+3),
$$


and, since $4g=n+2$,


$$
s_2(g)=s_2(n+2).
$$



Finally, $b\equiv1\pmod{16}$ gives $n\equiv2\pmod{16}$. Write $n=16k+2$. Then


$$
s_2(n)=s_2(k)+1=s_2(n+2).
$$


Subtracting the formulas for $\chi$ and $H$, and using $n+b-1=4003b-1$, proves the identity. $\square$

This proof validates the digit expression in the original objects; it does not replace them by a generic sequence.

### Proposition 2 — conditional paid-return transfer

At any original index for which both


$$
a\le H
\quad\text{and}\quad
v_2(S)\ge1+\chi
$$


hold, put


$$
D(u)=2s_2(4002b)-s_2(4003b-1)-s_2(4001b+3).
$$


Then, with $v_2(0)=+\infty$,


$$
v_2\!\left(\frac{S}{2^{a+1}}\right)
\ge \chi-a
\ge D(u).
$$


In particular, if $D(u)\ge L\ge0$, then


$$
2^L\mid \frac{S}{2^{a+1}}.
$$



#### Proof

The first inequality follows by subtracting the actual paid exponent $a+1$ from the assumed full-return valuation:


$$
v_2(S)-(a+1)\ge\chi-a.
$$


The endpoint bound gives


$$
\chi-a\ge\chi-H=D(u),
$$


where the last equality is Proposition 1. $\square$

The conclusion is divisibility of a normalized return. It is **not** yet divisibility of the final gcd, and it is not a denominator estimate.

---

## 7. Precise obstruction and concrete follow-on lemma

There are three distinct unclosed steps.

### 7.1 Actual content versus raw binomial gain

Unbounded $\chi$ does not imply unbounded $\chi-a$. The exact subtraction above explains why a content upper bound is indispensable.

A concrete next lemma is:

> **Paid-excess subsequence lemma — open target.**  
> Prove that there exist strictly increasing original parameters $u_k\ge0$ such that
> 

$$
> a(u_k)\le v_2\binom{g(u_k)}{d(u_k)}
>
$$


> and
> 

$$
> 2s_2(4002b(u_k))
> -s_2(4003b(u_k)-1)
> -s_2(4001b(u_k)+3)\ge k.
>
$$


> Establish the full-return estimate at these same indices.

This is stronger than positivity of the candidate excess. Growth, not merely infinitely many values equal to $1$, is the natural target for an increasing arithmetic saving. It is also still insufficient by itself for irrationality.

### 7.2 Minor saturation versus scalar norm cancellation

Primitive column or minor data do not determine norm valuations. A small explicit illustration is


$$
x=(1,2,2)^T,\qquad y=(0,1,0)^T.
$$


Both are primitive, and the minor from the first two rows is $1$, so the $2\times2$ minors are saturated. Nevertheless,


$$
x^Tx=9.
$$


Thus a primitive frame can have a norm divisible by $3^2$. This is not an example from the original stream; it exhibits the logical gap in trying to infer scalar norm control solely from frame saturation.

The actual A5 scalar norm and companion scalar must be treated directly.

### 7.3 The final all-prime denominator and whole error

Even a proved binary paid gain leaves the actual least simultaneous clearer and final all-prime gcd to be evaluated. The retained valuation


$$
v_3(q)=n-\frac{b+15}{2}
$$


implies


$$
q\ge3^{\,n-(b+15)/2}.
$$


Consequently, on any successful original subsequence,


$$
3^{\,n-(b+15)/2}
\left|\alpha-\frac pq\right|
\le
|q\alpha-p|
\longrightarrow0.
$$


This is a necessary scale requirement, not a sufficient one: $q$ can have substantial contributions from other primes.

The final proof must use the actual primitive $p,q$ and the **nonzero whole evaluated error** on precisely the same indices. No supplied abstract closes this step.

---

## 8. Bounded coordinator verification

No computation has been performed here, and no completed historical matrix or content audit should be repeated.

A new, inexpensive **auxiliary digit check** can screen the open paid-excess target without constructing any enormous matrix.

### Fixed inputs

Use exactly


$$
u=0,1,\ldots,31,\qquad b_u=9^{18+32u}.
$$


For each $u$, form


$$
n_u=4002b_u,\quad
d_u=(b_u-1)/4,\quad
g_u=(2001b_u+1)/2.
$$



These are modest exact integers for this purpose. Since $18+32u\le1010$ and $9<16$,


$$
b_u<2^{4040};
$$


all integers needed for the digit expressions have fewer than $4053$ bits.

### Expected verifiable output

Return a table containing


$$
\begin{array}{c}
u,\ s_2(b_u-1),\ s_2(n_u),\
s_2(n_u+b_u-1),\\
s_2(d_u),\ s_2(g_u-d_u),\ s_2(g_u),\
\chi_u,\ H_u,\ D(u).
\end{array}
$$


Compute $\chi_u,H_u$ by the digit-sum valuation formulas, not by expanding the enormous binomial coefficients. Verify row by row


$$
\chi_u-H_u=D(u),
\qquad
b_u\equiv1\pmod{16}.
$$


Report the minimum and maximum of $D(u)$, and the original parameters in this finite range for which $D(u)>0$.

There is no prespecified expected sign pattern. The certificate is the exact table and the verified identities, not a desired experimental outcome.

**Finite scope:** this check says nothing about $a(u)$, the unreviewed full-return theorem, infinitely many positive or growing excesses, the final gcd, or irrationality. Its sole purpose is to prioritize a precise infinite digit/carry lemma. If an identical table already exists, reuse it rather than rerunning it.

---

## 9. Conclusion and proof status

### Newly proved here

On every original binary index $u\ge0$, the candidate endpoint valuation satisfies the exact identity


$$
\chi-v_2\binom gd
=
2s_2(4002b)-s_2(4003b-1)-s_2(4001b+3).
$$


Under the separately stated endpoint-content and full-return hypotheses, this expression lower-bounds the valuation of the **already paid** normalized return $S/2^{a+1}$.

### Literature result

The entire supplied shard has been screened: 74 families, 139 linked papers. Family005, Family020, and Family325 merit the most focused mathematical inspection. Their roles are, respectively, a potentially compatible signed construction, a possible adaptive-prime arithmetic technique, and possible finite-matrix analytical support. None currently supplies a direct implication for $e+\pi$.

### Exact remaining bottleneck

The programme still needs a theorem controlling the **actual primitive denominator after every normalization and the final all-prime gcd**, together with a nonzero whole-error estimate tending to zero on the same infinite original index set.

Within A5, the next concrete task is to prove actual content control and growing paid excess on an infinite original subsequence, then connect that saving to the actual scalar gcd rather than merely to primitive minors or a normalized return.

Accordingly, **irrationality and rationality of $e+\pi$ both remain unproved by the supplied work**. The report advances an exact local arithmetic reduction and a bounded verification target, not a completed solution to the global problem.
