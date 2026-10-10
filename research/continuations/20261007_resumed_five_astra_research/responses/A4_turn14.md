> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Research report: complete screening of catalogue shard 4 and a local arithmetic obstruction

## Executive summary

The global objective remains unresolved: **the supplied work does not establish either rationality or irrationality of $e+\pi$**.

This report has two components.

1. **Literature screening.** I read all supplied abstracts in shard 4: **74 families, containing 146 linked papers**, including the explicitly marked secondary writeup in Family107. The coverage ledger below accounts for every supplied family. None of these abstracts supplies a direct theorem implication proving anything new about the rationality of $e+\pi$. A small number warrant targeted examination for transferable techniques.

2. **A proved local result.** For the finite ternary Schur block described in the research scope, I derive an exact valuation trichotomy. It isolates the only scalar valuation at which arbitrarily deep cancellation can occur. I also give an explicit positive-definite $2\times2$ family showing that divisibility by $27$, fixed determinant valuation, and full leading rank do **not** prevent that cancellation. This is a rigorous obstruction to an insufficient argument, not a counterexample to the original construction.

The most useful further readings in this shard are:

- Family122, for its claimed latest-anchor induction and spectrally compact masks;
- Family097, for prescribed-order vector balancing;
- Families229 and 189, for finite exact-certificate methodology;
- Family143, as a lower-priority source of asymptotic-separation techniques.

These are ranked as **inspection targets**, not adopted results. Their applicability depends on hypotheses not established by their abstracts.

No tools or external sources were used. No previously completed finite audit is reopened.

---

## 1. Proof standard and the original research objects

### 1.1 What an irrationality proof must actually deliver

Write


$$
\alpha=e+\pi.
$$


The relevant sufficient criterion is the existence of integers $p_n,q_n$, with $q_n>0$, on **one infinite set of original admissible indices**, such that


$$
0<|q_n\alpha-p_n|\longrightarrow 0.
$$



Indeed, if $\alpha=A/B$, with $A,B\in\mathbb Z$ and $B>0$, then every nonzero such error satisfies


$$
|q_n\alpha-p_n|
=\frac{|Aq_n-Bp_n|}{B}\ge \frac1B,
$$


a contradiction.

The normalization is inseparable from this criterion. If the construction produces a completed integer pair $(P_n,Q_n)$, after all prescribed divisions and clearings, then


$$
G_n=\gcd(|P_n|,|Q_n|),\qquad
q_n=\frac{|Q_n|}{G_n}.
$$


The corresponding sign must also be applied to $p_n$. The primitive error has absolute value


$$
\frac{|Q_n\alpha-P_n|}{G_n}.
$$



Thus:

- a large content in one column is not automatically a large final gcd;
- a determinant denominator is not automatically the primitive denominator;
- divisibility at one prime is not an ALL-prime gcd calculation;
- a small partial error is not a small whole error;
- two infinite index sets need not have an infinite intersection.

For nonzero $P_n,Q_n$, the actual denominator satisfies


$$
\log q_n
=
\sum_{\ell\ \mathrm{prime}}
\max\!\left\{0,v_\ell(Q_n)-v_\ell(P_n)\right\}\log\ell.
$$


This is the quantity that any proposed arithmetic improvement must ultimately control.

For rational columns, the least simultaneous clearer is the least common multiple of their **actual reduced entry denominators at the relevant normalization stage**. Replacing it by a convenient upper bound can be legitimate for an estimate, but cannot justify a claimed exact primitive denominator or a claimed paid gain.

### 1.2 Original scope retained

The compact source does not include every original matrix entry or the numerical specification of the recovered ternary progression. I therefore do not reconstruct missing definitions or silently substitute easier objects.

| Stream | Original domain and indispensable retained data | Outstanding issue relevant to this screen |
|---|---|---|
| **A1, ternary** | The recovered modular progression and fixed interior degree window; the complete moment functional, including both $-3^h(2t)!/4$ and the pole term; complete producer corrections; actual finite moment range and endpoint-diagonal factors. The finite Schur block is $T=\begin{pmatrix}a&z^T\\z&C\end{pmatrix}$, with $T$ divisible by $27$ and $v_3(\lambda)=-1$. | Directional or scalar control of the actual finite Schur return. Leading rank and common determinant depth do not supply it. |
| **A2, prime 29** | $b=3^{249005515+574312172u}$, $n=2001b$, $u\equiv2\pmod{29^9}$; complete normalized force, finite exterior factorial filtration, physical endpoint, fixed source digits and unit $\rho$. The missing upper Hahn boundary cannot be dropped. | The complete exponential residue and the auxiliary scalar clearer's cost in a factorial-content transfer. A logarithmic content bound for one column does not bound the full norm valuation $\nu$. The claimed charge determinant $-2^{n+1}(n!)^2/b!$ remains under review. |
| **A3, endpoint** | $n=15^r$ or $105^r$, $r\ge2$; fixed-seed forced Legendre companion; complete exponential and factorial-logarithmic source; actual integer frame and projected residual $\Xi_j$, including the extra omitted-column correction at $j=0$. | The denominator retains $\frac{|R_j|}{\gcd(R_j,C_j)}\frac{n!}{\gcd(n!,\zeta_j)}$ and the additional $F$-payment. Actual projected adjoint cancellation or a subfactorial correlated-contact estimate is open. The universal six-component rational tensor gauge is already ruled out. |
| **A5, binary** | $b=9^{18+32u}$, $n=4002b$, $u\ge0$; contact $0,\ldots,b-1$, physical reconstruction $0,\ldots,b$, $z_b=0$; $\displaystyle x=\frac12RA^{-1}f,\quad y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},\quad x=2^a x_0$. | $a\ge1$ is accepted. Stronger claims and the full return theorem remain under review. The actual norm is $Q=x_0^Tx_0$, not a minor. The parity scalar is $\displaystyle S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f$, with $S/2^{a+1}$ integral. Positive paid excess $\chi-a$ on an infinite original family is not proved. |

For A5, the proposed sufficient endpoint bound is


$$
a\le v_2\binom gd,\qquad
d=\frac{b-1}{4},\quad g=\frac{n/2+1}{2},
$$


and the associated difference is


$$
2s_2(4002b)-s_2(4003b-1)-s_2(4001b+3).
$$


Neither unbounded raw $\chi$ nor primitive minor saturation establishes the required scalar-norm conclusion.

The known binary denominator contribution


$$
v_3(q)=n-\frac{b+15}{2}
$$


also remains present. A proposed binary improvement cannot erase this cost.

### 1.3 Priority readings remain ongoing

Families005, 017 and 022 are not part of this shard. Their full papers or section packets were not supplied in this turn. I therefore make no claim to have inspected additional proof sections of them.

- **Family017:** a claimed irrationality exponent $2$ for $\pi$ alone does not imply irrationality of $e+\pi$. The mixed exponential–logarithmic source hypotheses remain necessary.
- **Family005:** the claimed Catalan construction cannot replace the current factorial functional without an exact compatible identity and complete normalization accounting.
- **Family022:** an almost-everywhere theorem does not select the fixed number $e+\pi$, even if its shift quantifier is uniform. A deterministic transfer to the original integer scalar sequences is still needed.

Their ongoing examination is not recorded as completed verification.

---

## 2. Complete coverage ledger

All results described in this ledger are **catalogue claims**. The ledger records relevance, not proof acceptance. A Lean link is not treated as evidence that the full mathematical claim has been formalized.

### 2.1 Number theory and algebraic geometry

| Family | Papers | Relevance decision |
|---|---:|---|
| 004 | 2 | Rational-zero undecidability and a Selmer-corank converse do not decide this explicit transcendental sum; no supplied encoding or mixed-period construction. |
| 009 | 3 | Milnor $K$-theory reconstruction and derivations may be algebraically interesting, but no bridge to the finite scalar denominator problem is identified. |
| 014 | 8 | Function-field Langlands, Arthur filtrations and eigensheaves have no identified transfer to the approximation objects. Several claims have explicit characteristic or decomposition hypotheses. |
| 019 | 2 | Étale covers and section conjectures concern rational points on hyperbolic curves, not the present mixed exponential–logarithmic approximation. |
| 024 | 1 | Uniform approximation by finite arithmetic data is a possible methodological analogy; totient asymptotics do not control the original gcds. |
| 029 | 2 | Primitive-root infinitude might inspire index selection, but the original indices are constrained. The simultaneous result has four additional analytic/sieve inputs. |
| 034 | 14 | Uniform geometric indices and moduli denominators are not integer-column contents or scalar clearers. No compatible log-pair realization is supplied; conditional papers remain conditional. |
| 039 | 4 | Multiplicity and interpolation geometry is potentially suggestive, but “very general” and geometric-generic points do not include the prescribed contact centers. |
| 044 | 1 | Scheme-theoretic fixed loci retain nilpotents, but there is no quiver/Coulomb-branch model of the original integer frame. |
| 050 | 1 | Positivity counterexamples supply no identified arithmetic or whole-error tool. |
| 055 | 2 | Exact central charges are not the present normalization problem; no relevant derived-category realization is known. |
| 060 | 1 | Global spherical shells: no identified transfer. |
| 066 | 2 | Bounded complements and Cartier sections require Fano-type geometry absent from the original objects. |

### 2.2 Analysis and convex geometry

| Family | Papers | Relevance decision |
|---|---:|---|
| 072 | 2 | Inverse derivative integral means could matter only after an explicit univalent-function representation; none is supplied. |
| 077 | 2 | Fourier extension estimates concern curved surfaces and $L^p$ norms, not current scalar gcd or fixed-index nonvanishing. |
| 082 | 3 | Two-endpoint truncation and absolute dyadic estimates are structurally interesting. They do not supply a fixed-point arithmetic estimate or replace finite physical boundaries. |
| 087 | 3 | Polar-volume and symplectic methods may inform lattice geometry; volume products do not control a prescribed primitive scalar denominator. |
| 092 | 2 | A freely chosen covering lattice is not the fixed arithmetic lattice of the construction. |
| 097 | 1 | **Shortlist:** prescribed-order signing and zero-sum reordering may help a new compatible finite construction, provided exact forcing constraints survive. |

### 2.3 Theoretical computer science

| Family | Papers | Relevance decision |
|---|---:|---|
| 102 | 5 | Approximation hardness has no identified mathematical transfer to the irrationality bottleneck. |
| 107 | 3 | Exact matrix multiplication could support future finite verification only. Arithmetic-operation exponents do not bound coefficient growth, certify divisions, or prove infinite behavior. Includes one secondary writeup. |
| 112 | 1 | Circuit lower bounds: no identified transfer. |
| 117 | 2 | Cut hardness and semidefinite gaps do not control the original norm or gcd. |
| 122 | 3 | **Shortlist:** latest-anchor induction and spectrally compact masks may suggest controlled contact constructions. Arithmetic height and complete forcing compatibility are unproved transfer hypotheses. |
| 128 | 1 | String superposition algorithms do not supply the needed exact identities. |
| 133 | 4 | Finite witness and parity-lift methods are at most proof-engineering analogies; graph-refinement complexity gives no arithmetic implication. |
| 138 | 2 | Could assist a bounded search for finite integer witnesses, but randomized search neither proves infinite existence nor certifies absence without an independent argument. |

### 2.4 Dynamics and combinatorics

| Family | Papers | Relevance decision |
|---|---:|---|
| 143 | 2 | **Reserve shortlist:** separation of asymptotic expansions on nested complex domains may inform a genuinely new whole-error argument. Uniformity in the growing original dimension is missing. |
| 148 | 1 | Self-similar entropy dimension, even allowing exact overlaps, does not imply deterministic digit estimates for the prescribed powers. |
| 153 | 1 | The pointwise arithmetic criterion is more relevant than an almost-everywhere statement, but it is an infinite algebraic-unit approximation condition, not rational approximation of $e+\pi$. |
| 158 | 1 | Plane coloring: no identified transfer. |
| 164 | 1 | Arbitrarily large finite monochromatic configurations do not provide a compatible infinite original subsequence or preserve the required progressions. |
| 169 | 1 | Combinatorial positivity might be useful only after an exact representation of a residual or cofactor as the stated coefficient; none is supplied. |
| 174 | 2 | Deterministic cut balancing may inspire constrained selection, but no graph-cut representation preserving forcing and contents is available. |
| 179 | 1 | Autocorrelation arithmetic is suggestive, but the original finite matrices are not supplied as circulant Hadamard objects. Cyclic completion would alter physical endpoints. |
| 184 | 2 | Coloring and independence estimates: no identified transfer. |
| 189 | 1 | **Verification-method shortlist:** a proved finite reduction with exact deduction traces is relevant to certificate design, not directly to denominator growth. |

### 2.5 Algebra and probability

| Family | Papers | Relevance decision |
|---|---:|---|
| 194 | 1 | Flat-local multiplicity is not a scalar valuation bound. Flatness and a compatible local-ring model would first have to be proved. |
| 199 | 2 | Homological counterexamples: no identified transfer. |
| 204 | 1 | Tensor-invariant saturation is different from saturation of the actual integer frame or its scalar norm. |
| 209 | 2 | Integral $K$-theory counterexamples warn against discarding integral information, but supply no actual gcd estimate. |
| 214 | 1 | Percolation operator thresholds: no identified transfer. |
| 219 | 2 | Random regular-graph universality cannot be applied to prescribed deterministic matrices. |
| 224 | 3 | Model-specific pivotal normalization is conceptually cautionary, but the results are probabilistic and depend on Cardy inputs where stated. |
| 229 | 3 | **Verification-method shortlist:** exact polynomial-inequality certificates may be reusable after a sound finite reduction. The deterministic-tree capacity theorem does not remove the model mismatch. |
| 234 | 1 | Haar-random eigenvectors and limiting pressure do not control a fixed scalar norm or final gcd. |
| 239 | 2 | Sharp random singularity estimates do not prove nonvanishing of a prescribed matrix. Deterministic structural sublemmas would need separate inspection. |

### 2.6 Logic, groups, physics and operator algebras

| Family | Papers | Relevance decision |
|---|---:|---|
| 244 | 1 | Choice and symmetric models: no identified transfer. |
| 249 | 1 | Cohomological/geometric dimension counterexample: no identified transfer. |
| 254 | 3 | Artin asphericity, CAT(0) obstruction and parabolic intersections: no identified transfer. All three links, including the CAT(0) path, are counted. |
| 259 | 1 | Measured group-action cost is unrelated to paid arithmetic normalization. |
| 264 | 3 | Generic inextendibility does not establish a property of fixed arithmetic objects. No transfer from the evolution estimates is identified. |
| 269 | 2 | A Fock-space coercive inequality could only transfer through an exact operator model; no such model of the signed factorial functional is supplied. |
| 274 | 2 | Quantum parity lower bounds do not imply the required binary digit or scalar parity estimates. |
| 279 | 1 | Exact quantum factoring is, at most, a computational claim. It neither supplies an available tool here nor replaces an infinite ALL-prime proof. |
| 284 | 1 | Query-complexity separation: no identified transfer. |
| 289 | 3 | Operator-algebra stability and its one-sided failures do not provide arithmetic lattice stability. |
| 294 | 1 | Quasitrace and tensor-finiteness counterexamples: no identified transfer. |
| 299 | 1 | Central-sequence character criteria: no identified transfer. |

### 2.7 Topology, functional analysis, differential geometry and PDE

| Family | Papers | Relevance decision |
|---|---:|---|
| 304 | 1 | Hilbert–Smith: no identified transfer. |
| 309 | 1 | A prime-three spectral-sequence theorem is not a ternary scalar-cofactor estimate. |
| 314 | 1 | Chromatic fixed-point loss is not valuation loss in the finite Schur problem, despite similar terminology. |
| 319 | 1 | Height-two spectra are unrelated to the Hahn-polynomial boundary issue. |
| 324 | 2 | Metric/linear distinction is a caution against changing structures, not an arithmetic tool here. |
| 329 | 1 | Entropy-duality counterexamples caution against a free primal–dual estimate; no positive bound for the original frame follows. |
| 334 | 1 | Infinite-order contact without local realization is conceptually relevant to distinguishing formal from actual identities, but gives no present construction. |
| 339 | 1 | Entropy rigidity: no identified transfer. |
| 344 | 1 | Metric Blaschke theorem: no identified transfer. |
| 349 | 1 | Minimal-volume estimates: no identified transfer. |
| 354 | 1 | Geometric formulas involving $\pi$ do not furnish rational approximations to $e+\pi$. |
| 359 | 2 | Negative curvature and bounded holomorphic functions have no identified compatible analytic representation. |
| 364 | 2 | Complete centering and factorial marginals are methodologically cautionary, but these are kinetic probability results, not the current factorial functional. |
| 369 | 1 | Neumann eigenfunction noncriticality requires an exact PDE realization absent here. |
| 374 | 1 | Optimal-transport stability could support perturbation estimates only after a measure model with controlled constants; it gives no arithmetic denominator bound. |

**Ledger total: 74 families, 146 papers.**

This completes the supplied shard, not the other four disjoint shards. The coordinator’s complete-collection inventory is broader than the material independently screened here.

---

## 3. Ranked candidates and decisive transfer tests

No candidate below is a direct theorem implication for $e+\pi$.

Because only abstracts are available here, “proof sections needed” means the indicated mathematical content, not invented section numbers.

### Rank 1 — Family122: latest-anchor induction and spectrally compact masks

**Classification:** promising heuristic inspiration; possibly a reusable construction technique after primary-proof inspection.

#### Exact advertised method

The second paper explicitly advertises a **latest-anchor induction with spectrally compact masks** for worst-case trace reconstruction. Its abstract gives quasipolynomial sample bounds for every fixed retention probability. The first paper adds a uniform decoder and bit-complexity bounds for known rational retention probabilities.

The abstracts do **not** state that the masks have small integer height, small simultaneous denominator, or compatibility with factorial moments.

#### Outstanding obligation it might address

The most plausible target is A3’s open **subfactorial correlated-contact estimate**, or a new finite construction in which exponential and logarithmic contact can be enforced without factorial-sized arithmetic losses.

For A2, a mask identity would have to retain the complete exponential residue and the scalar clearer. For A1, it would have to act on the factorial-plus-pole functional, not merely its pole part.

#### Decisive transfer hypothesis

One needs an exact identity expressing the original completed source or projected residual in terms of the proposed masks, together with:

1. the full finite support and both boundary contributions;
2. coefficient-height and least-clearer estimates;
3. all divisions required to enforce contact;
4. a bound for the whole evaluated error;
5. a proof that the transformation stays within the same original indices.

Spectral concentration alone is insufficient.

A simple necessary bound illustrates the normalization issue. If a finite signed or complex measure $\mu$, supported in $[-R,R]$ with $R>0$, represents moments $m_j$, then


$$
|m_{2M}|
=
\left|\int x^{2M}\,d\mu(x)\right|
\le R^{2M}\|\mu\|_{\mathrm{TV}}.
$$


Hence


$$
\|\mu\|_{\mathrm{TV}}\ge \frac{|m_{2M}|}{R^{2M}}.
$$


In particular, representing the pure factorial moment $m_{2M}=(2M)!$ on a fixed compact interval entails factorial growth in this norm.

This is **not** a lower bound for the complete A1 moment without evaluating its pole contribution. It demonstrates why a compact representation is not automatically a cheap representation.

#### Primary proof material needed

- the definitions, supports and coefficients of the masks;
- the latest-anchor induction, including every exceptional case;
- the separation estimate used to distinguish strings;
- dependence on length and retention probability;
- any coefficient-growth or rational-denominator estimates;
- the decoder’s conversion from analytic separation to a finite guarantee.

The trace-reconstruction lower-bound paper is relevant to understanding limitations, but is not itself an approximation construction.

---

### Rank 2 — Family097: prescribed-order vector balancing

**Classification:** potentially reusable deterministic technique, conditional on primary verification and exact constraint compatibility.

#### Exact advertised theorem

Every prescribed-order finite sequence in the Euclidean unit ball of $\mathbb R^d$ allegedly admits signs for which all signed prefixes have norm at most $C\sqrt d$, independently of sequence length. The paper also claims a corresponding reordering bound for zero-sum families.

The prescribed-order quantifier makes this more relevant than a generic-sequence result.

#### Possible use

A compatible signed block decomposition might reduce an archimedean whole-error estimate while preserving all contact equations. It could also control intermediate partial sums in a new finite construction.

It does not directly control contents, a least clearer, or scalar norm isotropy.

#### The exact obstruction to applying it freely

Suppose blocks are indexed by $1,\ldots,N$, and a matrix $B$ records their complete forcing contributions. If the original unsigned construction has force $B\mathbf1$, a signing $\varepsilon\in\{-1,1\}^N$ preserves that force only if


$$
B\varepsilon=B\mathbf1,
\qquad\text{equivalently}\qquad
B(\varepsilon-\mathbf1)=0.
$$


An unconstrained vector-balancing theorem does not impose this equation.

For example, if $B$ has full column rank, then


$$
B(\varepsilon-\mathbf1)=0
\quad\Longrightarrow\quad
\varepsilon=\mathbf1.
$$


There is then no signing freedom at all.

Even when a kernel exists, the admissible signs must preserve the exponential force, factorial-logarithmic force, omitted-column corrections and physical terminal simultaneously.

#### Primary proof material needed

- the prescribed-order signing lemma and its exact norm normalization;
- the derivation of the zero-sum reordering statement;
- dependence on dimension and any auxiliary scaling;
- whether a constrained-signing variant is proved;
- any constructive selection procedure, if finite witnesses are to be produced.

The concrete follow-on question is therefore not “can the blocks be balanced?” but:

> Does the kernel of the actual complete forcing map contain enough admissible signed moves to obtain balancing without changing the arithmetic lattice?

That remains unproved.

---

### Rank 3 — Families229 and 189: exact finite-certificate methodology

**Classification:** likely reusable proof-verification technique; no direct approximation theorem.

#### Exact advertised methods

- Family229 explicitly says that its four-state threshold proof uses exact-arithmetic verification of polynomial inequalities.
- Family189 claims a mathematical reduction to $3{,}099$ finite parameter-pattern instances, excluded by two exact implementations of proved inference rules, with deduction traces.

The useful feature is the architecture


$$
\text{infinite theorem}
\;\longrightarrow\;
\text{proved finite reduction}
\;\longrightarrow\;
\text{independently checkable exact certificate}.
$$



#### Possible use

This could support a future verification of:

- a finite family of invariant-cone inequalities;
- a finite carry-state transition system;
- boundary identities in an adjoint recurrence;
- a finite exceptional range after an independently proved asymptotic argument.

#### Decisive transfer hypothesis

The original research must first admit a **sound finite reduction**.

For example, checking a residue pattern modulo $2^K$ does not control arbitrary higher binary digits in


$$
2s_2(4002b)-s_2(4003b-1)-s_2(4001b+3),
\qquad b=9^{18+32u}.
$$


A finite-state method would need a proof that its states capture every relevant carry and that the prescribed exponent sequence follows the certified transitions.

Similarly, a finite ternary precision calculation cannot establish an unbounded-index scalar valuation bound without a recurrence or invariant that propagates the result.

#### Primary proof material needed

- the exact theorem reducing the infinite problem to finitely many cases;
- definitions of the finite states or parameter patterns;
- soundness of each inference rule;
- the exact certificate format and its mathematical interpretation;
- treatment of equality and boundary cases;
- the distinction between a witness-producing program and an independent checker.

No downloaded program should be treated as a proof merely because two implementations agree.

---

### Rank 4 — Family143: separation of asymptotic expansions

**Classification:** lower-priority analytic inspiration.

#### Exact advertised method

The first paper expressly attributes its uniform limit-cycle bound to **separation of asymptotic expansions on nested complex domains and a finite-dimensional counting argument**.

#### Possible use

A suitable separation lemma might help prove nonvanishing of a new mixed whole error, especially when several asymptotic contributions nearly cancel.

However, accepted whole-error results in the existing streams should not be reproved merely because the terminology resembles them.

#### Decisive transfer hypothesis

The original exponential and logarithmic expressions would have to lie in the paper’s actual analytic class, on its actual domains, with constants controlled as the original contact order and matrix dimension grow.

A statement uniform for each fixed polynomial degree is not automatically uniform when that degree grows with $n$. Nor does counting zeros of a function automatically bound its value at a prescribed endpoint.

#### Primary proof material needed

- the expansion-separation theorem;
- its function class and remainder hypotheses;
- dependence on dimension, degree and domain shrinkage;
- the zero-counting step;
- all reductions from return maps to the analytic class.

---

## 4. Important exclusions after the broader screen

Several tempting transfers fail at identifiable hypotheses.

### 4.1 Primitive roots do not select the required indices

Family029 concerns primes at which a fixed admissible integer is a primitive root.

- The A5 value $b=9^{18+32u}$ is a square, so it is not an admissible base for the stated theorem.
- Treating the varying A2 value $b$ as a base would require uniformity in the base that the abstract does not claim.
- Applying the theorem to a fixed base such as $3$ still gives no identity connecting those primes to the required original scalar sequences.

The original indices cannot be replaced by convenient primes.

### 4.2 Generic interpolation points are not the prescribed centers

Family039’s “very general” and geometric-generic hypotheses do not establish multiplicity bounds at the particular centers of the original contact problem. An explicit exclusion of the exceptional locus, or a center-uniform theorem, is necessary.

### 4.3 Random nonsingularity does not prove deterministic nonsingularity

Family239 assumes independent random signs. The original finite matrices are highly structured and deterministic. A probability estimate cannot be evaluated at one prescribed matrix.

A deterministic structural lemma extracted from such a proof could be useful, but its hypotheses would still need verification in the actual columns.

### 4.4 Representation-theoretic saturation is not arithmetic saturation

Family204’s saturation concerns tensor invariants for dominant weights satisfying a root-lattice condition. It does not identify:

- the content of an actual integer column;
- the least simultaneous clearer;
- the saturation of the relevant scalar norm;
- the final gcd.

Likewise, Family194’s flat-local multiplicity theorem cannot be invoked without a proved flat-local model that encodes the required scalar.

### 4.5 Cyclic completion changes finite boundaries

A circulant or autocorrelation argument from Family179 cannot be imposed by wrapping the original finite matrix around. Such a modification generally changes the upper boundary, forcing returns and physical terminal. An exact boundary-correction identity is indispensable.

---

## 5. New proved result: the critical ternary scalar and an explicit obstruction

This section is independent of all unverified catalogue claims.

### 5.1 Exact finite-block hypotheses

Let


$$
T=
\begin{pmatrix}
a&z^T\\
z&C
\end{pmatrix}
$$


be a finite symmetric matrix over $\mathbb Q_3$, with


$$
a\in27\mathbb Z_3,\qquad
z\in27\mathbb Z_3^m,\qquad
C\in27M_m(\mathbb Z_3).
$$


Assume $C$ is invertible over $\mathbb Q_3$, and let


$$
\lambda=\frac{\ell}{3},
\qquad \ell\in\mathbb Z_3^\times.
$$


Set


$$
d=1-\lambda a.
$$


Since $v_3(\lambda a)\ge2$, $d$ is a unit.

Consider the exact relative determinant from the source:


$$
\mathcal D
=
d\det\!\left(C+\frac{\lambda}{d}zz^T\right).
$$



Write


$$
a=27\alpha,\qquad z=27v,\qquad C=27H,
$$


and define


$$
\sigma=v^TH^{-1}v.
$$



These hypotheses match the stated local divisibility structure. Application at actual original indices additionally requires the full finite $C$ to be invertible there. That is not supplied by an abstract or by a leading-rank assertion alone.

### 5.2 Exact identity

The rank-one determinant identity gives


$$
\begin{aligned}
\mathcal D
&=d\det(C)\left(1+\frac{\lambda}{d}z^TC^{-1}z\right)\\
&=\det(C)\left(d+\lambda z^TC^{-1}z\right).
\end{aligned}
$$


Now


$$
z^TC^{-1}z=27\,v^TH^{-1}v=27\sigma,
$$


so


$$
\boxed{\;
\frac{\mathcal D}{\det C}
=
1-9\ell\alpha+9\ell\sigma.
\;}
\tag{5.1}
$$


In particular, the actual endpoint-diagonal contribution $-9\ell\alpha$ remains in the formula.

### 5.3 Valuation trichotomy

Let


$$
R=\frac{\mathcal D}{\det C}.
$$



**Proposition.**

1. If $v_3(\sigma)\ge-1$, including $\sigma=0$, then
   

$$
R\in1+3\mathbb Z_3,
   \qquad v_3(R)=0.
$$



2. If $v_3(\sigma)\le-3$, then
   

$$
v_3(R)=2+v_3(\sigma).
$$



3. If $v_3(\sigma)=-2$, put $u=9\sigma\in\mathbb Z_3^\times$. Then
   

$$
R=1+\ell u-9\ell\alpha,
$$


   and for every integer $k\ge1$,
   

$$
v_3(R)\ge k
   \quad\Longleftrightarrow\quad
   u\equiv9\alpha-\ell^{-1}\pmod{3^k}.
   \tag{5.2}
$$



**Proof.**

If $v_3(\sigma)\ge-1$, then $9\ell\sigma\in3\mathbb Z_3$, while $9\ell\alpha\in9\mathbb Z_3$. Equation (5.1) gives the first assertion.

If $v_3(\sigma)\le-3$, then $9\ell\sigma$ has negative valuation. The other term $1-9\ell\alpha$ is a unit. The two valuations differ, so their sum has the smaller valuation:


$$
v_3(R)=v_3(9\ell\sigma)=2+v_3(\sigma).
$$



In the remaining case $u=9\sigma$ is a unit, and


$$
R=\ell\bigl(u-(9\alpha-\ell^{-1})\bigr).
$$


Since $\ell$ is a unit, (5.2) follows. ∎

**Consequently, arbitrarily deep positive cancellation can occur only at**


$$
\boxed{v_3(\sigma)=-2.}
$$



This evaluates the noncritical valuation regimes completely.

### 5.4 The directional hypothesis is sufficient

The archived desired bound is


$$
C^{-1}z\in3^{-1}\mathbb Z_3^m.
$$


Since $C^{-1}z=H^{-1}v$ and $v\in\mathbb Z_3^m$, it implies


$$
\sigma=v^TH^{-1}v\in3^{-1}\mathbb Z_3.
$$


Therefore the first case applies:


$$
v_3(\mathcal D)=v_3(\det C).
$$



This is a rigorous conditional consequence. It does not prove the directional hypothesis for the original matrices.

### 5.5 A scalar test retaining every division

Let


$$
D_H=\det H,\qquad N_H=v^T\operatorname{adj}(H)v.
$$


Then


$$
\sigma=\frac{N_H}{D_H}.
$$


The exact numerator identity is


$$
R
=
\frac{(1-9\ell\alpha)D_H+9\ell N_H}{D_H}.
\tag{5.3}
$$


No determinant denominator has disappeared.

Suppose the critical case holds. If $s=v_3(D_H)$, then


$$
v_3(N_H)=s-2.
$$


Thus $s\ge2$, and we may write


$$
D_H=3^sD_0,\qquad N_H=3^{s-2}N_0,
$$


where $D_0,N_0$ are units. Equation (5.2) becomes the division-free unit congruence


$$
\boxed{\;
\ell N_0+(1-9\ell\alpha)D_0
\equiv0\pmod{3^k}.
\;}
\tag{5.4}
$$



As a small corollary, if $v_3(\det H)\le1$, then the critical case is impossible and $R$ is a unit. The compact source does not establish this determinant hypothesis on the original growing family.

### 5.6 Explicit counterexample to rank-and-depth control

For every integer $k\ge1$, define


$$
c_k=\frac{1+7\cdot3^{2k}}8.
$$


This is a positive integer because $3^{2k}\equiv1\pmod8$, and it is a $3$-adic unit.

Take


$$
a=27,\qquad z=27,\qquad C=243c_k,\qquad \lambda=\frac13.
$$


Then


$$
T_k=
\begin{pmatrix}
27&27\\
27&243c_k
\end{pmatrix}.
$$



Every entry is divisible by $27$, and


$$
\frac{T_k}{27}\equiv
\begin{pmatrix}1&1\\1&0\end{pmatrix}\pmod3,
$$


which has full rank.

Moreover,


$$
\det T_k
=729(9c_k-1),
$$


so


$$
v_3(\det T_k)=6
$$


for every $k$. Also $v_3(C)=5$ for every $k$.

These matrices are positive definite over $\mathbb R$: their first principal minor is positive, and $9c_k-1>0$.

Nevertheless,


$$
d=-8
$$


and


$$
\begin{aligned}
\mathcal D_k
&=dC+\lambda z^2\\
&=-8(243c_k)+243\\
&=243(1-8c_k)\\
&=-7\cdot3^{5+2k}.
\end{aligned}
$$


Hence


$$
v_3(\mathcal D_k)=5+2k,
\qquad
v_3\!\left(\frac{\mathcal D_k}{\det C}\right)=2k.
$$



The relative cancellation is unbounded, despite:

- divisibility of $T_k$ by $27$;
- full leading rank;
- fixed valuation of $\det T_k$;
- fixed valuation of $\det C$;
- real positive definiteness.

The directional quantity is exactly


$$
C^{-1}z=\frac1{9c_k},
$$


of valuation $-2$, placing the example in the critical case.

**Scope of the counterexample.** This family is not asserted to arise from the original moment construction. It disproves only the proposed inference from the listed coarse matrix properties to a bound on the relative scalar.

---

## 6. Concrete follow-on lemma for the original ternary stream

The trichotomy suggests a weaker target than proving the full directional bound everywhere.

### Proposed critical-unit nonresonance lemma — open

On one infinite set of the **original admissible ternary indices**, with the recovered progression, interior degree window, complete producer corrections and actual finite endpoints unchanged, prove that there is a fixed $K\ge0$ such that whenever


$$
v_3(\sigma_n)=-2,
$$


the actual normalized units satisfy


$$
\ell_nN_{0,n}
+(1-9\ell_n\alpha_n)D_{0,n}
\not\equiv0\pmod{3^{K+1}}.
\tag{6.1}
$$



Then the proposition implies


$$
v_3(\mathcal D_n)-v_3(\det C_n)\le K
$$


throughout that same index set:

- the high-valuation regime gives difference $0$;
- the low-valuation regime gives a negative difference;
- the critical regime is bounded by (6.1).

This is a specific scalar nonresonance obligation. It retains the endpoint term and the normalized determinant units.

It remains **open** because the supplied compact source does not evaluate these units for the original complete matrices. Formula (6.1) is not presented as a completed arithmetic proof. Its value is that it identifies exactly what must be controlled, and the counterexample shows why coarser information cannot replace that control.

Even a proof of (6.1) would resolve only this local ternary obstruction. It would still need to enter the actual ALL-prime primitive-denominator calculation and be combined with the accepted whole-error theorem on the same infinite indices.

---

## 7. Bounded verification requests

### 7.1 Primary-source requests

A bounded next literature packet should consist of the relevant proof material from:

1. Family122’s latest-anchor paper and uniform-decoder paper;
2. Family097’s signing theorem and zero-sum reordering derivation;
3. one exact-certificate reduction from Family229, together with Family189’s inference-rule soundness and certificate interpretation.

Family143 should remain secondary unless a new analytic construction genuinely requires it.

These are requests for mathematical text. No build instructions, scripts or accompanying programs need to be executed to inspect the stated transfer hypotheses.

### 7.2 Optional exact arithmetic certificate for the new obstruction

The symbolic proof in Section 5 already establishes the counterexample for every $k\ge1$. No computation is needed for its validity.

If the coordinator wants a small independent arithmetic certificate, the complete bounded input is


$$
k\in\{1,2,3\},\quad
c_k=\frac{1+7\cdot3^{2k}}8,\quad
T_k=\begin{pmatrix}27&27\\27&243c_k\end{pmatrix},
\quad \lambda=\frac13.
$$



Expected outputs are:

| $k$ | $c_k$ | $\det T_k$ | $\mathcal D_k$ | $v_3(\det T_k)$ | $v_3(\mathcal D_k)$ |
|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 51,759 | $-15,309$ | 6 | 7 |
| 2 | 71 | 465,102 | $-137,781$ | 6 | 9 |
| 3 | 638 | 4,185,189 | $-1,240,029$ | 6 | 11 |

The checker should also verify the exact identities


$$
\det T_k=729(9c_k-1),\qquad
\mathcal D_k=243(1-8c_k).
$$



This is a new diagnostic check, not a repetition of an archived original-index audit. Its finite output establishes only those three instances; the infinite statement rests on the algebraic proof above.

No original-index matrix computation is specified here because the full original ternary input definitions are absent from this packet. Inventing them would invalidate the intended verification.

---

## 8. Conclusion and proof status

### New proved statements

1. The finite ternary relative determinant has the exact scalar formula
   

$$
\frac{\mathcal D}{\det C}=1-9\ell\alpha+9\ell\sigma.
$$


2. Its valuation is completely determined outside the critical case $v_3(\sigma)=-2$.
3. In that critical case, cancellation is exactly the unit congruence (5.4).
4. An explicit positive-definite family shows that leading rank and fixed determinant depths do not bound this cancellation.

### Conditional deductions

- The archived directional bound $C^{-1}z\in3^{-1}\mathbb Z_3^m$ would make the relative scalar a unit.
- The proposed critical-unit nonresonance lemma would bound positive relative valuation loss on its stated original index set.
- The shortlisted literature methods could be useful only after their full proofs and the identified transfer hypotheses are checked.

### Open obligations

The immediate local obligation is to evaluate or constrain the **actual corrected ternary critical units**, not surrogate leading matrices.

The global bottleneck remains the **actual primitive denominator after all contents, paid divisions, the least simultaneous clearer and the ALL-prime final gcd**, compared with the **nonzero whole evaluated error on the same infinite original indices**.

The catalogue screen supplies inspection priorities and rejects several invalid transfers. The local calculation sharpens one arithmetic obstruction. **Neither supplies an unconditional proof of rationality or irrationality of $e+\pi$.**
