> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Research Report: Catalogue Screening and a Sharper Local Obstruction in the $e+\pi$ Programme

## 1. Executive summary and proof status

The global objective remains unresolved: **the supplied work does not establish either rationality or irrationality of $e+\pi$**.

This report has two components.

1. **Complete abstract screening of the supplied shard.**  
   I screened all **158 paper abstracts in 75 families** supplied in `shard_1.md`. The coverage ledger below includes every supplied family ID and its paper count. This is complete coverage of this shard, not an independent reading of the other four shards or of all 722 manuscripts.

2. **A new, rigorously proved local result for the ternary Schur-complement obstruction.**  
   Using only the stated finite block structure, I prove:
   - an exact valuation trichotomy identifying the sole scalar cancellation regime;
   - a scalar congruence sufficient to prevent that cancellation, strictly weaker than the presently proposed directional inverse bound;
   - an explicit family of positive-definite integer matrices showing that divisibility by $27$, fixed determinant valuations, and stable leading rank do **not** prevent arbitrarily deep relative-determinant cancellation.

The last result is an obstruction to a class of proposed arguments, **not a counterexample to the original approximation construction**. The new scalar congruence remains unproved for the actual, endpoint-corrected original matrices.

### Best literature prospects in this shard

The most useful additional primary-source readings are:

1. **Family021:** the claimed uniform Jacobsthal bound, potentially useful for deterministic avoidance of a *proved, finite collection of affine bad congruences*.
2. **Family119:** exact local optimization, calibrated energy inequalities, and finite arithmetic certificates, potentially useful for certifying a genuinely finite reduction of a signed whole-error estimate.
3. **Family266, exact-arithmetic companion only:** certificate design for exhaustive algebraic exclusions, potentially useful after a finite, boundary-complete reduction has independently been proved.

These are prospective techniques, not direct theorem implications for $e+\pi$. Family104 offers a more remote finite-state idea for paid digit inequalities, but no finite-state representation of the original power sequence has been established.

The ongoing readings of **Family005, Family017, and Family022 remain ongoing**. No primary proof section from those papers is included in this turn, and no completion of their verification is claimed here.

---

## 2. Evidence, scope, and the actual irrationality criterion

### 2.1 What has and has not been supplied

The mathematical evidence available here consists of:

- the compact research-scope file;
- the complete abstracts in shard 1;
- the coordinator’s account of acquisition and ongoing priority-paper review.

The repository provenance does not establish mathematical correctness. In particular:

- an abstract is not a proof;
- a catalogue heading can state a broader family conclusion than a particular constituent paper;
- a Lean link does not specify which theorem, hypotheses, computations, or dependencies have been formalized;
- the existence of a verifier does not establish that its complete execution or arithmetic assumptions have been checked.

No tools were available, and no computation was executed.

The compact scope also does **not** contain the complete original coefficient arrays and reconstruction definitions. Consequently, this report cannot calculate an actual primitive denominator from those arrays. It does not replace them with simplified columns or silently reconstruct missing definitions.

### 2.2 The final arithmetic object

Write $\alpha=e+\pi$. After the original construction’s complete forcing, finite reconstruction, endpoint corrections, contents, and normalization payments have been applied, suppose its actual final integer pair is


$$
(\widehat P_n,\widehat Q_n),\qquad \widehat Q_n\ne0.
$$


Define


$$
G_n=\gcd(|\widehat P_n|,|\widehat Q_n|),
$$


where this gcd includes **all primes**, and put


$$
q_n=\frac{|\widehat Q_n|}{G_n},
\qquad
p_n=\frac{\operatorname{sgn}(\widehat Q_n)\widehat P_n}{G_n}.
$$


Then the whole primitive error is exactly


$$
q_n\alpha-p_n
=
\frac{\operatorname{sgn}(\widehat Q_n)}
     {G_n}
\bigl(\widehat Q_n\alpha-\widehat P_n\bigr).
$$



The required conclusion is


$$
0<|q_n\alpha-p_n|\longrightarrow0
$$


on **one and the same infinite set of original admissible indices**.

Indeed, if $\alpha=A/B\in\mathbb Q$, with $B>0$, then every nonzero such error satisfies


$$
|q_n\alpha-p_n|
=\frac{|Aq_n-Bp_n|}{B}\ge\frac1B.
$$


This is the final contradiction sought by the approximation route.

Neither a small unnormalized error, nor a large column content, nor a gain at one prime establishes this criterion by itself.

### 2.3 Research objects that remain unchanged

The following restrictions are retained throughout this report.

| Stream | Original domain and indispensable retained data |
|---|---|
| **A1, ternary** | The recovered modular progression and fixed interior degree window remain unchanged. Their numerical specification is not included in this packet. The complete moment functional retains both the factorial contribution $-3^h(2t)!/4$ and the pole contribution. The physical endpoint, producer corrections, endpoint-diagonal factors, and finite moment range remain present. |
| **A2, prime $29$** | $b=3^{249005515+574312172u}$, $n=2001b$, $u\equiv2\pmod{29^9}$. Retain the complete normalized force, finite exterior factorial filtration, physical endpoint, source digits, and unit $\rho$. A logarithmic bound for one column’s content does not bound the full norm valuation $\nu$. |
| **A3, endpoint** | $n=15^r$ or $105^r$, $r\ge2$. Retain the complete exponential plus factorial-logarithmic source, the actual integer frame, the projected residual $\Xi_j$, and the additional omitted-column correction at $j=0$. The denominator contains the retained factors $\lvert R_j\rvert/\gcd(R_j,C_j)$ and $n!/\gcd(n!,\zeta_j)$, together with the extra $F$-payment. |
| **A5, binary** | $b=9^{18+32u}$, $n=4002b$, $u\ge0$. Contact indices are $0,\ldots,b-1$; physical reconstruction is $0,\ldots,b$, with $z_b=0$. Retain $\displaystyle x=\tfrac12RA^{-1}f,\quad y=\frac{RA^{-1}(h^e+h^F)+e_0}{4b!},\quad x=2^a x_0$, the norm $Q=x_0^Tx_0$, and the complete return scalar $S$. |

For A5, specifically,


$$
S=\sum_{j<b}(n+1-j)\binom{n+2}{j}z_j^f,
\qquad
\frac{S}{2^{a+1}}\in\mathbb Z.
$$


The proposed full-return estimate and infinite paid excess remain under review or open. The digit expression


$$
2s_2(4002b)-s_2(4003b-1)-s_2(4001b+3)
$$


cannot be replaced by an estimate for generic binary strings.

The accepted primitive-denominator valuation


$$
v_3(q_n)=n-\frac{b+15}{2}
$$


also remains in force. In particular,


$$
q_n\ge 3^{\,n-(b+15)/2}.
$$


A prospective binary gain cannot erase this existing odd-prime cost.

---

## 3. Ranked literature assessment

No theorem in this shard, at the scope visible in its abstract, directly implies irrationality of $e+\pi$.

### 3.1 First priority: Family021 — deterministic coprime selection

**Paper:** *A quadratic bound for Jacobsthal’s function.*

#### Exact abstract claim

For the least $h(k)$ such that every interval of $h(k)$ consecutive integers contains an integer coprime to any prescribed integer with at most $k$ distinct prime factors, the abstract claims


$$
h(k)\ll \frac{k^2}{(\log\log(3k))^2}.
$$


The important potential advantage is uniformity in both the prime set and interval position.

The abstract does not disclose enough of the proof mechanism to assess its validity.

#### Possible use

A deterministic coprime-selection lemma could help choose admissible parameters avoiding unwanted local degeneracy of a scalar cofactor or an auxiliary clearer.

It does **not** automatically provide a useful final gcd. Avoiding a prime in one scalar can help one stage and hurt another; the final effect must be evaluated in the actual primitive numerator and denominator.

#### Exact transfer hypothesis

The forbidden conditions must first be shown to reduce to one forbidden residue per relevant prime, along the actual original progression.

Here is the precise conditional transfer.

**Conditional affine-avoidance lemma.**  
Let


$$
F_j(t)=a_jt+b_j\in\mathbb Z[t].
$$


Suppose that, for every prime in a finite set $\mathcal P$, all nonconstant conditions


$$
F_j(t)\not\equiv0\pmod p
$$


exclude either no residue or one common residue $r_p\pmod p$. Suppose also that no condition is identically zero modulo $p$. Then, assuming the claimed Jacobsthal estimate, every sufficiently long interval of $t$-values contains a simultaneous admissible value, with interval length bounded by the claimed $h(|\mathcal P|)$.

**Derivation.** By the Chinese remainder theorem choose $c$ with


$$
c\equiv r_p\pmod p
\quad(p\in\mathcal P).
$$


For


$$
P=\prod_{p\in\mathcal P}p,
$$


the conditions become


$$
\gcd(t-c,P)=1.
$$


Translation preserves interval length, so the claimed bound applies. ∎

For an original progression $u=u_0+Mt$, an affine expression becomes


$$
Au+B=(AM)t+(Au_0+B).
$$


If $p\mid AM$, it is either always nonzero modulo $p$, or always zero. In the latter case no parameter selection is possible.

#### Decisive obstructions

This transfer fails without further work if:

- a prime excludes several residues;
- the relevant scalar is nonlinear with uncontrolled roots;
- the bad prime set changes with the selected parameter in a circular way;
- the required index is not in the original admissible progression;
- selection must also remain within a fixed degree window whose available width is too small;
- the proof needs prime-power valuation control rather than avoidance modulo $p$;
- unexamined primes still affect the final gcd.

Thus this is **a potentially reusable deterministic selection technique**, not an all-prime cofactor theorem.

#### Primary proof material needed

Before adoption, inspect the portions containing:

1. the exact definition of $h(k)$, including small $k$;
2. the uniform interval estimate and its constants;
3. the reduction from prime sets to the final bound;
4. every sieve, covering, or exceptional-set input used in that reduction.

No section numbers can responsibly be supplied from this abstract alone.

---

### 3.2 Second priority: Family119 — calibrated inequalities with exact local certificates

**Papers:**

- *Sharp binary-information contraction on the discrete cube*;
- *Hellinger contraction with arbitrary Boolean output bias*.

#### Exact claimed methods

The first abstract identifies:

- an explicit three-point optimizer for a local joining problem;
- two entropy capacities;
- a common-output thinning inequality;
- dimension induction;
- integration along a noise semigroup.

The second identifies:

- asymmetric dimension induction;
- a calibrated noise-semigroup energy estimate;
- finite exact arithmetic certificates.

These are more informative methodological claims than a bare announcement of a theorem.

#### Possible use

The likely reusable component is the conversion of a global inequality into a finite, exactly checkable local inequality with a rigorous induction or propagation theorem.

Potential targets include:

- a signed whole-error bound after an exact integral or recurrence reduction;
- an adjoint estimate that retains both source components;
- a finite boundary inequality propagating through an original recurrence.

The existing whole-error theorems should not be reopened merely because the terminology is similar. A new reading should identify a **specific missing inequality**.

#### Decisive transfer hypothesis

One must first construct an exact representation of the original expression in the paper’s certified class.

A Boolean noise-semigroup argument cannot be applied directly to the complete factorial moment functional. In particular:

- signed weights are not probability weights;
- a factorial tail is not a compact positive kernel;
- a local positivity certificate does not establish nonvanishing of a whole signed expression;
- dimension induction must preserve the actual finite upper boundary and physical terminal.

The plausible transfer is **certificate architecture**, not the stated information-theoretic theorem.

#### Primary proof material needed

Inspect:

1. the exact local optimizer and its boundary cases;
2. the hypotheses for dimension induction;
3. the calibration identities making the energy estimate exact;
4. the finite arithmetic certificate specification;
5. the theorem converting those finite certificates into a statement for every dimension and parameter.

A finite certificate is useful only after the reduction theorem has excluded every omitted case.

---

### 3.3 Third priority: Family266 — exact algebraic certificates, not the binary64 exclusion

**Papers:**

- *The maximum number of mutually unbiased bases in dimension six*;
- *Exact Fourier certificates for complex Hadamard matrices of order six*.

#### Important separation of claims

The main paper’s abstract describes a computer-assisted exclusion of four bases under stated binary64 and compiler conditions.

The companion’s abstract instead claims integer/rational certificates for:

- a Fourier-vanishing statement outside Tao’s cubic equivalence class;
- exclusion of seven mutually unbiased bases, giving an upper bound of five through a completion theorem.

These are different conclusions. The exact companion does not, by its abstract alone, establish the main paper’s bound of three.

#### Possible use

The exact companion may offer a reusable method for:

- exhaustive algebraic case decomposition;
- rational certificate checking;
- excluding determinant degeneracies after a finite parameter reduction;
- separating exceptional algebraic components from a generic argument.

It is not currently a determinant theorem for the approximation matrices.

#### Decisive transfer hypothesis

There must be a proved finite reduction of the original problem:

- all original index classes covered;
- all exceptional components retained;
- every division justified;
- no lost terminal equation;
- no replacement of scalar norm isotropy by minor saturation.

In particular, A5’s accepted primitive $2\times2$-minor information does not itself exclude isotropy of $x_0^Tx_0$. A finite certificate would need to address that actual scalar condition.

#### Primary proof material needed

Inspect:

1. the algebraic parameterization;
2. the exhaustive treatment of equivalence classes and exceptional loci;
3. all saturation or denominator exclusions;
4. the exact certificate identities;
5. the proof that the verifier checks the entire intended domain.

The binary64 pipeline is not an authorized substitute for a bounded exact-arithmetic certificate in this programme.

---

### 3.4 Lower-priority heuristic: Family104 — finite-state paid-growth problems

Family104 claims exact algorithms and certifiable strategies for finite mean-payoff and related games.

A conceivable application is to a **proved finite-state model** of carries and payments in a digit inequality. For instance, a transition system might record a cumulative paid excess rather than raw divisibility.

The decisive missing hypothesis is substantial:

> The system must represent precisely the original sequence $b=9^{18+32u}$, its finite returns, and all normalization costs—not all binary strings or an enlarged family of admissible paths.

Digit operations for fixed multipliers can often be represented by finite carry states. That does not show that the base-two expansions of the required powers form the appropriate finite-state path family. Moreover, a nonnegative mean payoff alone does not prove an unbounded positive total excess: zero-weight cycles can persist forever.

Accordingly, this is **heuristic inspiration only**. The relevant primary material would be the exact game encoding, treatment of zero value, strategy certificates, and bit-complexity accounting—not the algorithmic headline alone.

---

## 4. The three priority families already under review

These families are not part of the supplied shard’s ledger.

| Family | Ongoing purpose | Status supportable in this turn |
|---|---|---|
| **005** | Mixed signed determinants, Taylor cancellation, odd-prime denominator layers, Frobenius nonvanishing, real energy estimates | Ongoing full-source or section-packet review reported by the coordinator. No primary proof section is supplied here. No claim is adopted. |
| **017** | Center-uniform multivariable interpolation, integer determinant nonvanishing, denominator and error estimates | Ongoing review. The claimed irrationality exponent $2$ for $\pi$ is not a theorem about $e+\pi$. |
| **022** | Inhomogeneous metric approximation, gcd and overlap estimates | Ongoing review. No supplied primary sections establish a deterministic estimate for the original scalar sequences. |

### Family005: exact functional compatibility is indispensable

A usable identity must act on the complete functional, including


$$
-\frac{3^h(2t)!}{4},
$$


not merely on its pole part. Replacing it by a compact Jacobi or Chebyshev kernel requires a proved identity, a paid transformation, or an explicitly new construction with its own error and denominator analysis.

### Family017: an irrationality exponent for $\pi$ does not transfer

Even a valid theorem that $\mu(\pi)=2$ would not establish irrationality of $e+\pi$. It places a restriction on rational approximation to $\pi$, not on an additive relation between $\pi$ and $e$.

A transfer needs a mixed exponential/logarithmic construction with verified interpolation hypotheses, nonvanishing, denominator bounds, and evaluated whole error.

### Family022: “every shift” does not remove “almost every $x$”

A theorem holding for almost every $x$, even simultaneously for every shift, does not identify the fixed point $x=e+\pi$. Nor does it automatically select the sparse original indices.

The potentially reusable part is a deterministic overlap or gcd estimate extracted from the proof and then verified for the actual integer sequences. That extraction remains open.

---

## 5. New proved result: the exact ternary cancellation regime

This section is independent of the catalogue claims.

### 5.1 Finite hypotheses

Let


$$
T=\begin{pmatrix}a&z^T\\ z&C\end{pmatrix}
$$


be a finite symmetric matrix over $\mathbb Q_3$, with


$$
a\in27\mathbb Z_3,\qquad
z\in27\mathbb Z_3^m,\qquad
C\in27M_m(\mathbb Z_3),
$$


and suppose $C$ is invertible. Let


$$
v_3(\lambda)=-1,\qquad d=1-\lambda a.
$$


Since $v_3(\lambda a)\ge2$,


$$
d\in1+9\mathbb Z_3,
$$


so $d$ is a unit.

The accepted finite relative-determinant expression is


$$
d\det\!\left(C+\frac{\lambda}{d}zz^T\right).
$$


Define its ratio to $\det C$ by


$$
\mathcal R
=
\frac{d\det(C+\lambda zz^T/d)}{\det C}.
$$


The finite matrix determinant lemma gives


$$
\mathcal R=d+\lambda z^TC^{-1}z.
\tag{5.1}
$$



Nothing here replaces a finite matrix by an infinite one.

### 5.2 Integral scaling and an exact scalar certificate

Write


$$
a=27\alpha,\qquad z=27w,\qquad C=27B,\qquad \lambda=\frac{\eta}{3},
$$


where


$$
\alpha\in\mathbb Z_3,\quad
w\in\mathbb Z_3^m,\quad
B\in M_m(\mathbb Z_3),\quad
\eta\in\mathbb Z_3^\times.
$$


Set


$$
\delta=\det B\ne0,\qquad
H=w^T\operatorname{adj}(B)w,\qquad D=v_3(\delta).
$$


Because $B,w$ are integral,


$$
D\ge0,\qquad H\in\mathbb Z_3.
$$


Also


$$
z^TC^{-1}z
=27w^TB^{-1}w
=27\frac{H}{\delta}.
$$


Thus


$$
\boxed{\mathcal R=1-9\eta\alpha+9\eta\frac{H}{\delta}.}
\tag{5.2}
$$



This is an exact identity for the complete finite blocks.

### 5.3 The valuation trichotomy

**Theorem 5.1.**  
Under the hypotheses above, put


$$
r=v_3(H)-D,
$$


with $r=+\infty$ if $H=0$.

1. If $r\ge-1$, then
   

$$
\mathcal R\in1+3\mathbb Z_3.
$$


2. If $r\le-3$, then
   

$$
v_3(\mathcal R)=r+2<0.
$$


3. If $r=-2$, define the unit
   

$$
U=9H/\delta\in\mathbb Z_3^\times.
$$


   Then
   

$$
\mathcal R=d+\eta U.
$$


   This is the only regime in which cancellation between two units can produce arbitrarily large positive valuation.

Furthermore,


$$
\boxed{
\mathcal R\in1+3\mathbb Z_3
\iff
v_3(H)\ge D-1.
}
\tag{5.3}
$$



**Proof.**

The term $1-9\eta\alpha=d$ is a unit congruent to $1\pmod9$. The remaining term in (5.2) has valuation $r+2$.

- If $r\ge-1$, that valuation is at least $1$, proving the first assertion.
- If $r\le-3$, it is negative and strictly smaller than $v_3(d)=0$. The ultrametric valuation rule therefore gives
  

$$
v_3(\mathcal R)=r+2.
$$


- If $r=-2$, both summands are units, and their sum may have any nonnegative valuation, including $+\infty$.

For the equivalence, subtract $1$:


$$
\mathcal R-1
=9\eta\left(\frac{H}{\delta}-\alpha\right).
$$


If $v_3(H/\delta)\ge-1$, the right side lies in $3\mathbb Z_3$. Conversely, if $v_3(H/\delta)<-1$, integrality of $\alpha$ prevents cancellation with $H/\delta$; hence


$$
v_3(\mathcal R-1)=2+v_3(H/\delta)\le0.
$$


This proves (5.3). ∎

### 5.4 Consequence for the open directional bound

The proposed directional condition


$$
C^{-1}z=B^{-1}w\in3^{-1}\mathbb Z_3^m
$$


implies


$$
w^TB^{-1}w\in3^{-1}\mathbb Z_3.
$$


Therefore it implies the scalar certificate


$$
v_3(H)\ge D-1,
$$


and hence


$$
v_3(\mathcal R)=0.
$$



But the scalar certificate is **strictly weaker**.

**Example.** Take


$$
B=9I_3,\qquad w=(1,1,1)^T,\qquad \alpha=\eta=1.
$$


Then


$$
B^{-1}w=\frac19(1,1,1)^T
\notin3^{-1}\mathbb Z_3^3.
$$


Nevertheless,


$$
\delta=9^3=729,\qquad
H=3\cdot9^2=243,
$$


so


$$
D=6,\qquad v_3(H)=5=D-1.
$$


Consequently,


$$
\mathcal R=1-9+9\left(\frac13\right)=-5,
$$


a $3$-adic unit.

Thus a scalar proof can succeed even where the directional estimate fails. This gives a concrete, less restrictive follow-on target.

### 5.5 Explicit obstruction: fixed determinant depths do not control the relative scalar

**Theorem 5.2.**  
For every integer $M\ge1$, there is a positive-definite symmetric integer matrix $T_M$, divisible by $27$, and a fixed $\lambda=1/3$, such that


$$
v_3(\det C_M)=5,\qquad v_3(\det T_M)=6,
$$


the reduction of $T_M/27$ modulo $3$ is independent of $M$ and nonsingular, but


$$
v_3(\mathcal R_M)=M.
$$



**Construction and proof.** Set


$$
t_M=8\cdot3^M-1,
$$


and define


$$
a_M=27\cdot3^M,\qquad
z_M=27t_M,\qquad
C_M=243t_M.
$$


Here $C_M$ is a $1\times1$ block, and $t_M\equiv2\pmod3$.

Every entry is divisible by $27$, and


$$
v_3(C_M)=5.
$$


Moreover,


$$
\begin{aligned}
\det T_M
&=(27\cdot3^M)(243t_M)-(27t_M)^2\\
&=729t_M(9\cdot3^M-t_M)\\
&=729t_M(3^M+1).
\end{aligned}
$$


Both $t_M$ and $3^M+1$ are $3$-adic units, so


$$
v_3(\det T_M)=6.
$$


The diagonal entries are positive and this determinant is positive; hence $T_M$ is positive definite over $\mathbb R$.

Modulo $3$,


$$
\frac{T_M}{27}
=
\begin{pmatrix}
3^M&t_M\\
t_M&9t_M
\end{pmatrix}
\equiv
\begin{pmatrix}0&2\\2&0\end{pmatrix},
$$


which is nonsingular and independent of $M$.

Finally,


$$
d_M=1-\frac{a_M}{3}=1-9\cdot3^M,
$$


and


$$
z_M^TC_M^{-1}z_M
=\frac{(27t_M)^2}{243t_M}
=3t_M.
$$


Therefore


$$
\mathcal R_M
=d_M+\frac13(3t_M)
=1-9\cdot3^M+t_M
=-3^M.
$$


Thus $v_3(\mathcal R_M)=M$, as claimed. ∎

This example also has


$$
C_M^{-1}z_M=\frac19,
$$


so the proposed directional bound fails in exactly the relevant direction.

### 5.6 What this proves—and what it does not

Theorems 5.1 and 5.2 rigorously establish that:

- leading rank does not control the relative scalar;
- common determinant depth does not control it;
- even real positive definiteness does not repair that inference;
- the dangerous cancellation is concentrated in the exact scalar shell
  

$$
v_3(H)=D-2;
$$


- a weaker scalar congruence can replace the full directional bound for the purpose of proving $\mathcal R$ is a unit.

They do **not** establish that the original A1 matrices enter, avoid, or behave uniformly inside that shell.

The actual follow-on obligation is:

> **Endpoint-complete scalar lemma.**  
> On an infinite subset of the original A1 progression, within the original fixed interior degree window, prove for the actual finite corrected blocks that
> 

$$
> w_n^T\operatorname{adj}(B_n)w_n
> \equiv0\pmod{3^{\max(D_n-1,0)}},
> \qquad
> D_n=v_3(\det B_n).
> \tag{5.4}
>
$$


> Alternatively, if the critical shell occurs, evaluate its actual unit cancellation and bound it with all endpoint factors retained.

Equation (5.4) is an open obligation, not a claimed evaluation of the original scalar. Its advantage is that it is strictly weaker than the directional condition and has an exact finite certificate formulation.

---

## 6. Complete coverage ledger

**Codes:**  
**R** — primary proof reading worth prioritizing for a specific possible transfer.  
**I** — indirect inspiration or infrastructure only; no current transfer.  
**N** — no sufficiently specific compatible route identified.

Counts refer to supplied paper abstracts, not independently verified results.

### 6.1 Number theory and algebraic/complex geometry

| Family | Papers | Decision and concise relevance assessment |
|---|---:|---|
| 001 | 1 | **N.** Specialized Hodge-class pairings require an abelian-variety realization; no bridge to the mixed exponential/logarithmic construction is supplied. |
| 006 | 2 | **N.** Twist densities and mean rank do not control fixed approximation scalars or original sparse indices. |
| 011 | 3 | **I.** Dilation graphs and smooth shifted primes may contain sieve ideas; prime-predecessor statistics do not determine our all-prime gcd. |
| 016 | 4 | **N.** Unlikely intersections concern specified algebraic subvarieties and special loci; no applicable realization of the $e,\pi$ relation is given. |
| 021 | 1 | **R.** Uniform deterministic coprime selection could address verified affine bad residues; prime powers and the final gcd remain separate. |
| 026 | 1 | **N.** Positive-density large gaps do not select admissible original indices or control their cofactors. |
| 031 | 1 | **N.** Galois-group reconstruction gives no mixed-period approximation or denominator estimate. |
| 036 | 4 | **N.** Numerical semiampleness and minimal models have no identified arithmetic transfer; numerical equivalence also permits changes absent from our normalization problem. |
| 041 | 2 | **N.** Hyperkähler semiampleness and Lagrangian bases do not supply an integer construction for $e+\pi$. |
| 047 | 1 | **N.** Affine cancellation and fibration counterexamples do not address scalar denominator saturation. |
| 052 | 2 | **N.** Tangent-bundle splitting is geometric decomposition, not a decomposition of the complete forced sources. |
| 057 | 3 | **N.** Special-variety fundamental groups and conditional root-orbifold constructions lack a relevant arithmetic realization. |
| 063 | 1 | **N.** Fano dimension–pseudoindex inequalities have no identified transfer. |
| 068 | 7 | **I.** Exact-rank and boundary-correction themes are conceptually relevant; semipositive anticanonical geometry does not imply finite cofactor or content estimates. |

### 6.2 Analysis, metric geometry, and theoretical computer science

| Family | Papers | Decision and concise relevance assessment |
|---|---:|---|
| 074 | 2 | **N.** Kakeya maximal and dimension estimates do not control these fixed arithmetic determinants. |
| 079 | 1 | **N.** Wave local smoothing provides no compatible whole-error representation. |
| 084 | 2 | **I.** Uniform affine-copy exclusion illustrates careful quantifiers; geometric sequences here are not our arithmetic power indices. |
| 089 | 2 | **N.** Metric embeddings and flow–cut bounds do not preserve exact integer scalar identities. |
| 094 | 1 | **N.** Nonlinear bounded-distortion dimension reduction cannot preserve contents, gcds, and exact errors. |
| 099 | 3 | **I.** Finite coding and explicit boundary handling are methodological only; no edit-distance encoding of the arithmetic obligation exists. |
| 104 | 4 | **I.** Exact finite-game certificates could help a proved carry-state reduction; the original power sequence has not been so encoded. |
| 109 | 1 | **I.** Exact multiplication is computational infrastructure only; the tiny asymptotic saving does not solve the mathematical bottleneck. |
| 114 | 2 | **N.** Approximate randomized counting of bases is not an exact scalar-gcd or nonvanishing certificate. |
| 119 | 2 | **R.** Calibrated local inequalities, induction, and exact certificates may transfer after an exact signed-expression reduction. |
| 125 | 2 | **N.** Metric approximation ratios and recovery payments do not furnish arithmetic normalization identities. |
| 130 | 2 | **I.** Exact Fourier circuits may inspire finite algebraic organization, but unrestricted complex scalar cost is not integer bit cost or denominator control. |
| 135 | 1 | **N.** Circuit lower bounds do not establish nonvanishing or paid heights of the evaluated determinants. |
| 140 | 6 | **N.** Random-projection and information bounds concern distributed observations, not fixed scalar sequences; average-case success is incompatible with the target. |

### 6.3 Dynamics, combinatorics, and algebra

| Family | Papers | Decision and concise relevance assessment |
|---|---:|---|
| 145 | 1 | **N.** Mixing of a transformation does not establish genericity or equidistribution of our fixed arithmetic sequence. |
| 150 | 2 | **N.** Billiard ergodicity and weak mixing require geometric systems not identified here; irrational angles cannot be used circularly. |
| 155 | 1 | **I.** Finite local rules versus global behavior is a useful warning, not an arithmetic construction. |
| 160 | 1 | **I.** Explicit coloring constructions might inspire avoidance; they do not preserve the original modular and valuation conditions. |
| 166 | 1 | **N.** Distinct-distance lower bounds have no identified scalar-cofactor transfer. |
| 171 | 1 | **N.** Ramsey embeddings of cubes do not yield paid digit inequalities. |
| 176 | 1 | **N.** Random-graph appearance thresholds do not address deterministic original indices. |
| 181 | 1 | **I.** Finite decomposition could help an independently identified dependency graph; none is supplied. |
| 186 | 2 | **N.** Influence and sharp-threshold estimates are probabilistic and symmetry-based, not fixed-sequence arithmetic bounds. |
| 191 | 1 | **I.** Explicit determinant-area separation is a remote nonvanishing analogy; no compatible parameterization is known. |
| 196 | 1 | **N.** Group-algebra zero divisors do not imply cancellation in the actual rational finite matrices. |
| 201 | 1 | **N.** Noncommutative algebraic division rings have no identified transfer. |
| 206 | 2 | **N.** Representation undecidability does not obstruct or certify this particular finite arithmetic problem. |

### 6.4 Probability, logic, and group theory

| Family | Papers | Decision and concise relevance assessment |
|---|---:|---|
| 211 | 7 | **I.** Exact clock and normalization tracking are good proof practice; random-map scaling limits do not transfer to primitive denominators. |
| 216 | 6 | **N.** Critical scaling and Gaussian-field limits concern different models and retain substantial companion assumptions. |
| 221 | 1 | **N.** Hierarchical variational formulas require probabilistic factorization and positivity absent from the signed functional. |
| 226 | 1 | **N.** Loop-ensemble convergence does not control fixed arithmetic errors. |
| 231 | 1 | **N.** Strongly Rayleigh and positive-contraction determinantal processes cannot be assumed for these signed finite matrices. |
| 236 | 1 | **N.** Factor-of-IID thresholds on trees are not deterministic cofactor estimates. |
| 241 | 1 | **N.** Turing-degree rigidity has no specific mathematical transfer. |
| 246 | 1 | **N.** Boundary-modulus uniformization is not an archimedean determinant estimate in the original objects. |
| 251 | 2 | **I.** Stability-to-exactness is a broad analogy; operator-norm closeness does not preserve integer contents or gcds. |
| 256 | 2 | **N.** Solutions in overgroups do not solve the fixed rational linear-algebra normalization problem. |

### 6.5 Mathematical physics and operator algebras

| Family | Papers | Decision and concise relevance assessment |
|---|---:|---|
| 261 | 2 | **N.** Almost-sure spectral results for random potentials do not select the required deterministic matrices. |
| 266 | 2 | **R.** Exact companion certificates may be reusable; distinguish them from the separate binary64-assisted upper bound of three. |
| 271 | 4 | **N.** Exact thermodynamic coefficients and ordered limits supply no mixed-period integer construction. |
| 276 | 1 | **I.** Reduction to a one-variable optimization is methodological only; channel positivity and tensor hypotheses are unverified here. |
| 281 | 2 | **N.** Limiting expected energy and nonquantitative depth existence cannot certify the original infinite index family. |
| 286 | 2 | **N.** Arithmeticity of operator-algebra correspondences concerns different arithmetic objects. |
| 291 | 4 | **N.** Comparison and absorption theorems do not imply scalar saturation or integer denominator bounds. |
| 296 | 1 | **N.** Operator generation is unrelated to a boundary-complete finite forced recurrence. |
| 301 | 1 | **N.** Trace-cone classification does not provide the needed signed scalar evaluation. |

### 6.6 Topology, functional analysis, differential geometry, and PDE

| Family | Papers | Decision and concise relevance assessment |
|---|---:|---|
| 306 | 1 | **N.** Cosmetic-surgery exclusion has no identified arithmetic transfer. |
| 311 | 1 | **N.** Classification at every prime is still about Lubin–Tate invariant ideals; it is not an all-prime gcd theorem for our integers. |
| 316 | 1 | **N.** Mod-two stable homotopy information is neither the relevant binary scalar nor an all-prime result. |
| 321 | 1 | **N.** Finite CW-model obstructions do not address this approximation construction. |
| 326 | 1 | **N.** Banach-space cotype hypotheses do not furnish arithmetic heights or nonvanishing. |
| 331 | 7 | **I.** Explicit tree energies and recursive potentials may inspire inequalities, but no compatible norm or exact source representation is supplied. |
| 336 | 3 | **N.** Spectral curvature and width estimates concern geometric fibers, not finite cofactor directions. |
| 341 | 1 | **N.** Cohomology-preserving deformation has no identified mixed-period arithmetic implication. |
| 346 | 2 | **N.** Almost-everywhere regularity does not certify a distinguished arithmetic point or index sequence. |
| 351 | 3 | **I.** Multivariable asymptotic path selection is potentially interesting, but selected real paths need not lie in the original modular progression or degree window. |
| 356 | 2 | **I.** Upgrading weak bounds to every geodesic is a quantifier analogy only; RCD hypotheses have no arithmetic realization here. |
| 361 | 2 | **N.** Geometry depending on the growth degree cannot substitute for one compatible original approximation family. |
| 366 | 1 | **N.** Planar minimizer regularity gives no determinant, denominator, or whole-error estimate. |
| 371 | 1 | **N.** Stable PDE blowup, including positive-probability conclusions, has no identified transfer. |
| 376 | 9 | **I.** Full-domain realization and all-time verification illustrate completeness requirements; universal computation does not decide this fixed irrationality problem. |

**Ledger total: 75 families, 158 paper abstracts.**

---

## 7. Bounded verification requests

### 7.1 Primary-source reading requests

The next literature work should be narrow rather than a new broad acquisition exercise:

1. **Family021:** the main uniform interval theorem and its full proof dependency chain.
2. **Family119:** the local certified inequality and the theorem propagating it to all dimensions and parameters.
3. **Family266:** the exact-arithmetic companion’s reduction and certificate-validity proofs.

For each packet, the coordinator should identify the supplied theorem and proof ranges and list any dependent proof not included. A partial packet must remain a partial verification.

The ongoing Family005/017/022 readings should not be duplicated or relabelled as complete.

### 7.2 A bounded exact-arithmetic test for the new A1 scalar condition

No computation is needed to establish Theorems 5.1 and 5.2. The following is a proposed **new finite diagnostic**, not a repetition of the completed precision-$29$ or other historical audits.

#### Inputs

A coordinator-authored packet containing:

- one explicit original A1 admissible index and its original interior degree;
- the already reconstructed, endpoint-complete rational blocks $C,z$;
- $B=C/27$ and $w=z/27$;
- an existing accepted certificate for
  

$$
D=v_3(\det B);
$$


- a declared finite dimension and rational bit-size bound.

For a modest first task, one may impose the explicit caps


$$
m\le64,\qquad D\le32,
$$


and at most $4096$ bits for each reduced numerator and denominator. If no already available original packet meets these caps, the output should be **“no eligible packet under this bounded request”**, not an unbounded reconstruction.

The provenance of the blocks must confirm that the full factorial term, producer corrections, endpoint-diagonal factors, and finite moment range are retained.

#### Calculation

For $D\le1$, condition (5.4) is automatic.

For $D\ge2$, compute


$$
H\bmod 3^{D-1}.
$$


A convenient division-free certificate uses the bordered matrix


$$
J=
\begin{pmatrix}
B&w\\
w^T&0
\end{pmatrix}.
$$


Since $B$ is invertible,


$$
\det J
=\det B\,(-w^TB^{-1}w)
=-H.
$$


Thus it suffices to compute


$$
-\det J\pmod{3^{D-1}}.
$$


Reduced rational denominators are $3$-adic units and can be inverted modulo this modulus. No division by a nonunit is permitted in modular elimination; use a division-free determinant method or an exact integer method with its divisions certified.

#### Expected verifiable output

The output should contain:

1. the original index and degree;
2. the exact input packet identifier;
3. the modulus $3^{D-1}$;
4. the residue of $H$;
5. either:
   - **pass:** residue zero, proving $\mathcal R\in1+3\mathbb Z_3$ for this one matrix; or
   - **failure of this sufficient condition:** residue nonzero.

The second outcome does not by itself prove harmful cancellation. The critical-shell residue must then be evaluated using Theorem 5.1.

A pass establishes only that stated finite instance. It does not prove an infinite-index lemma, determine the final all-prime gcd, or establish irrationality.

---

## 8. Conclusion: new result and exact remaining bottlenecks

### New proved statement

The finite ternary Schur problem now has an exact scalar description:


$$
\mathcal R
=1-9\eta\alpha+9\eta\frac{H}{\delta}.
$$


Arbitrarily deep positive cancellation can occur only in the critical shell


$$
v_3(H)=v_3(\delta)-2.
$$


The sufficient congruence


$$
v_3(H)\ge v_3(\delta)-1
$$


is strictly weaker than the proposed directional inverse bound. An explicit positive-definite integer counterfamily proves that common determinant depths and stable leading rank cannot replace this scalar control.

These statements are rigorously proved here.

### Remaining local A1 bottleneck

Prove a boundary-complete scalar congruence or critical-shell cancellation bound for the **actual original matrices**, on an infinite subset of the original modular progression and within the original fixed degree window. No pole-only substitution is admissible.

### Remaining global bottleneck

Even a successful local A1 lemma must be carried through:

- every normalization payment;
- actual column contents;
- the least simultaneous clearer;
- the complete final scalar construction;
- the final gcd over all primes;
- the actual primitive denominator;
- the nonzero whole evaluated error;

all at the **same infinite original indices**.

The catalogue screen identifies a few techniques worth examining, but it supplies no missing theorem at those exact hypotheses. The unconditional rationality or irrationality of $e+\pi$ therefore remains open in this work.
