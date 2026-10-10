> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 384 — arbitrary selector universality for the filtered Hasse package and a full-capacity no-go

Date: 2026-09-01

## 1. Outcome and capacity first

Retain the actual fixed-$j=1$ candidate set at fixed $M$,



$$
\mathcal P_M=
 \left\{p\text{ prime}:{4M+3\over3}\leq p\leq{3M-1\over2}\right\},
 \qquad P_M=\prod_{p\in\mathcal P_M}p.                 \tag{1.1}
$$



Every $p\in\mathcal P_M$ gives the unique actual row



$$
h_p=3M-2p,
 \qquad s_p={3p-4M-1\over2},
 \qquad p=4h_p+6s_p+3.                                \tag{1.2}
$$



Items 360 and 363 identify the live target as the joint Hasse--transverse
gate, while Items 374--383 put the transverse coordinate into a rank-two
filtered Frobenius extension with a flat rational connection.  This item
asks whether the *abstract local package itself* can force a strict
cross-prime saving.

The answer is no, in the following exact sense.

> **PROVED — arbitrary-selector universality.**  For every subset
> $\mathcal S\subseteq\mathcal P_M$, there is one integral CRT selector
> $Z_{M,\mathcal S}$, $0\leq Z_{M,\mathcal S}<P_M$, satisfying
> 

$$
> Z_{M,\mathcal S}\equiv
> \begin{cases}0\pmod p,&p\in\mathcal S,\\1\pmod p,&p\notin\mathcal S.
> \end{cases}                                           \tag{1.3}
>
$$


> Put
> 

$$
> \widetilde Z_{M,\mathcal S}=Z_{M,\mathcal S}+P_M,
> \qquad P_M\leq\widetilde Z_{M,\mathcal S}<2P_M.       \tag{1.4}
>
$$


> This nonzero selector has exactly the same candidate-prime residues as
> (Z_{M,\mathcal S}).
> On the two-coordinate filtered-Frobenius family of Section 3, use the
> selector point
> 

$$
> (q_1,q_2)=
> (\widetilde Z_{M,\mathcal S}\bmod p,
>  \widetilde Z_{M,\mathcal S}\bmod p).
> \tag{1.5}
>
$$


> The two graded Hasse invariants vanish jointly exactly for
> $p\in\mathcal S$.  Every member of the family has fixed rank, fixed
> Hodge polygon, flat horizontal connection, two fixed logarithmic pole
> components, and the lift- and coordinate-invariant bounded-splitting
> obstruction of Item 383.  Both selector values $0$ and $1$ avoid
> the poles.

The construction is not special to two coordinates.  For every fixed
$k\geq1$, the direct sum of $k$ copies over
$\mathbb Z_p[[q_1,\ldots,q_k]]$, with every $q_i$ specialized to the
same CRT selector, has a codimension-$k$ joint Hasse divisor and realizes
the same arbitrary subset.  Therefore adding any fixed finite number of
formally independent, locally unconstrained Hasse coordinates does not by
itself create a density theorem.

Prime by prime,



$$
\boxed{
 \gcd(P_M,\widetilde Z_{M,\mathcal S},
            \widetilde Z_{M,\mathcal S})
 =\prod_{p\in\mathcal S}p.}                             \tag{1.6}
$$



Thus every possible joint-zero pattern, including the full pattern, is
compatible with this entire rowwise invariant package.  By the prime
number theorem,



$$
\log P_M={M\over6}+o(M).                               \tag{1.7}
$$



Taking $\mathcal S=\mathcal P_M$ attains the full raw fixed-$j=1$
mass.  Consequently no theorem whose hypotheses use only



$$
\boxed{
 \begin{gathered}
 \text{bounded rank, fixed filtration/Hodge polygon, algebraic
 codimension two,}\\
 \text{flatness, a bounded number of logarithmic poles, and the local}\\
 \text{bounded-splitting or global-disc non-dagger obstruction}
 \end{gathered}}                                        \tag{1.8}
$$



can imply any universal retained bound $cM+o(M)$ with $c<1/6$.
The same is true after requiring a nonzero raw-scale selector:
$P_M\leq\widetilde Z<2P_M$, so
$\log\widetilde Z=\log P_M+O(1)$.

This is a global capacity no-go, not a local representation theorem.  It
closes the proposed use of the Items 374--383 rowwise filtered package as
a black-box density or conductor argument.  It does **not** prove that the
actual moment selector is arbitrary, and it does not estimate the actual
$W_{H,\mathscr T}(M)$.

Therefore



$$
\boxed{\text{new booking}=0},\qquad
 \boxed{\text{new capacity reduction}=0},\qquad
 \boxed{\text{retained fixed-}j=1\text{ ceiling}=1/36}. \tag{1.9}
$$



## 2. Exact CRT theorem on the actual candidate set

Because the primes in $P_M$ are pairwise coprime, the Chinese remainder
theorem gives a unique residue class satisfying (1.3), and the least
nonnegative representative satisfies



$$
0\leq Z_{M,\mathcal S}<P_M.                             \tag{2.1}
$$



Adding (P_M) gives the nonzero representative (widetilde Z) in
(1.4) without changing any residue modulo a candidate prime.

For each $p\mid P_M$, equation (1.3) gives



$$
p\mid \widetilde Z_{M,\mathcal S}
 \quad\Longleftrightarrow\quad p\in\mathcal S.          \tag{2.2}
$$



Since $P_M$ is squarefree, (1.6) follows.  More generally, using two
independent selectors $Z_1,Z_2$ realizes any prescribed intersection
of two zero patterns.  The diagonal choice in (1.5) already realizes an
arbitrary *joint* pattern while keeping the joint Hasse divisor
codimension two on the ambient base.

This exact theorem includes the two extremal cases



$$
\mathcal S=\varnothing:\ \widetilde Z=P_M+1,
 \ \gcd(P_M,\widetilde Z)=1,
 \qquad
 \mathcal S=\mathcal P_M:\ \widetilde Z=P_M,
 \ \gcd(P_M,\widetilde Z)=P_M.                          \tag{2.3}
$$



It also exposes why the raw height bound is neutral.  An arbitrary
pattern has a nonzero carrier of logarithmic height at most
$\log P_M+\log2$, exactly the scale of the support that one is trying to
reduce.  This strengthens
Item 363's CRT warning by retaining the complete filtered-Hasse geometry
developed after that item.

## 3. One fixed geometric information package realizes every pattern

Fix an odd prime $p$ and work on the two-dimensional formal base



$$
R_p=\mathbb Z_p[[q_1,q_2]].                             \tag{3.1}
$$



For one coordinate $q$, take the Item 374 filtered module



$$
A_q=\begin{pmatrix}p&0\\pq&1\end{pmatrix},
 \qquad \operatorname {Fil}^1=R_pe_1.                  \tag{3.2}
$$



Its graded Hasse invariant is $q$.  Take two copies and form



$$
\mathcal E=\mathcal E(q_1)\oplus\mathcal E(q_2).       \tag{3.3}
$$



Then $\mathcal E$ has rank four, determinant $p^2$, filtration rank
two, a fixed Hodge polygon, and joint Hasse divisor



$$
q_1=q_2=0,                                              \tag{3.4}
$$



which has codimension two.

Use Item 383's explicit lift with the prime-independent unit
$\lambda=2$:



$$
\Phi_2(q)={1-(1-2q)^p\exp(-2pq)\over2}.               \tag{3.5}
$$



It is an integral overconvergent Frobenius lift and the exact horizontal
one-form is



$$
\omega_2={dq\over1-2q}.                                \tag{3.6}
$$



The direct-sum connection has pole divisor



$$
(1-2q_1)(1-2q_2)=0,                                    \tag{3.7}
$$



with exactly two fixed components.  It is flat.  At every selector point
used in (1.5), $q_i\in\{0,1\}$, so $1-2q_i\in\{1,-1\}$ is a unit.
The selector never meets the poles.

The nonzero differentials $d\bar q_1,d\bar q_2$ also retain Item 383's
no bounded simultaneous splitting theorem on each summand.  Hence adding
that obstruction, or the corresponding failure of a dagger connection on
the full closed disc, does not restrict (1.3).

Nothing in this construction varies the rank, Hodge polygon, number of
pole components, or formal local equations with $\mathcal S$.  Only the
arithmetic selector map changes.  Therefore a cross-prime theorem must
control that map; it cannot be inferred from the ambient local package.

More generally, $\bigoplus_{i=1}^k\mathcal E(q_i)$ has rank $2k$,
filtration rank $k$, determinant $p^k$, $k$ fixed pole components,
and codimension-$k$ joint Hasse divisor.  The diagonal selector
$q_1=\cdots=q_k=\widetilde Z_{M,\mathcal S}\bmod p$ again vanishes jointly exactly
on $\mathcal S$.  This is an all-$k$ construction for each fixed finite
$k$, not an induction from finite data.

## 4. Exact information-class no-go

Let $\mathfrak I$ denote the data consisting of:

1. a fixed rank bound;
2. a fixed filtration and Hodge polygon;
3. a codimension-two joint Hasse divisor;
4. a flat connection with a fixed finite logarithmic pole divisor;
5. regularity of the selected points;
6. the bounded-splitting and full-disc dagger obstructions; and
7. a nonzero CRT carrier below $2P_M$.

The construction above proves



$$
\boxed{
 \sup_{\text{families satisfying }\mathfrak I}
 \sum_{\substack{p\in\mathcal P_M\\
                  \operatorname {Ha}_1(p)=
                  \operatorname {Ha}_2(p)=0}}
 \log p
 =\log P_M={M\over6}+o(M).}                             \tag{4.1}
$$



The upper bound is tautological and the lower bound is the full selector
$\mathcal S=\mathcal P_M$.  Thus (4.1) is an exact sharp capacity
theorem for the information class, not merely a counterexample at one
prime.

This closes all arguments of the form



$$
\text{``the local filtered object has small fixed complexity, therefore
 its selected zero primes have strict sub-full mass.''}  \tag{4.2}
$$



The implication in (4.2) is false without a compatibility theorem for the
actual selector.  Algebraic codimension two does not repair it: the
comparison family has the same codimension and still realizes every
pattern.

Nor does any other fixed finite codimension repair it: the preceding
rank-$2k$ comparison has codimension $k$ and still attains full raw
mass.  A useful extra coordinate must therefore come with an actual
cross-prime compatibility law, not merely local algebraic independence.

## 5. Relation to the actual joint gate

For the actual family, Items 360 and 363 prove only the one-way inclusion



$$
\text{full ordinary collision}
 \Longrightarrow a_{2s+1,2h}=0,
 \quad\mathscr T_{h,s}=Q_0(h,s)=0\pmod p.               \tag{5.1}
$$



The actual weighted envelope is



$$
W_{H,\mathscr T}(M)=
 \sum_{\substack{p\in\mathcal P_M\\
                  a_{2s_p+1,2h_p}=0\\
                  Q_0(h_p,s_p)=0\ ({\rm mod}\ p)}}
 \log p.                                                \tag{5.2}
$$



Item 384 does not replace either actual coordinate by the comparison
selector.  It proves that the following inputs are still missing:

1. a prime-independent arithmetic or geometric origin for the actual
   moving moment map;
2. a horizontal statistic that retains both actual coordinates and has a
   genuine compatibility law across primes;
3. a sequence-specific average-gcd or factor-localization theorem; or
4. a direct weighted nonconcentration theorem for (5.2).

A future compatible system would be new information precisely because it
would restrict the selector maps excluded from $\mathfrak I$.  Item 384
does not rule out such a system, Chebotarev after constructing it, or an
actual aggregate resultant smaller than the raw scale.

## 6. Deterministic certificate

The standard-library certificate verifies:

1. the pinned dependencies from Items 360, 363, 374, and 383;
2. the exact candidate-row bijection (1.2);
3. every CRT pattern, for both the least and nonzero shifted selectors, at
   the predeclared values
   $M=9,34,76,120,180$, comprising $2,2,16,16,32$ subsets;
4. the shifted-selector radical identity (1.6), including empty and full
   selectors;
5. regularity of the points $q_i=0,1$ away from the fixed pole
   $q_i=1/2$; and
6. declared exact power-series controls of (3.5)--(3.6) at $p=13,17$.

The subset controls verify the implementation of the all-subset CRT
theorem; the proof itself is (2.1)--(2.2).  The finite formal-series
truncations replay the already exact logarithmic identity and are not
prime-distribution evidence.  No collision scan or asymptotic inference
from finite data is made.

## 7. Strict labels

### PROVED

- the all-$M$, all-subset nonzero CRT selector theorem (1.3)--(1.6);
- the fixed-rank, fixed-Hodge, codimension-two direct-sum filtered-Hasse
  realization;
- its all-fixed-$k$ codimension-$k$ generalization;
- the rational flat connection with two fixed logarithmic pole components
  and selector regularity;
- preservation of the Item 383 bounded-splitting obstruction;
- the sharp full-capacity theorem (4.1);
- the scoped black-box local-geometry/rowwise-conductor no-go;
- zero booking and retention of the $1/36$ ceiling.

### DECLARED EXACT CONTROLS ONLY

- five fixed $M$ values and all their subsets;
- two formal-series connection controls;
- no actual collision census, density extrapolation, or finite-to-infinite
  inference.

### OPEN

- any arithmetic restriction on the *actual* selector map;
- an actual prime-independent compatible system or monodromy theorem;
- an actual aggregate gcd, resultant, or factor-localization bound;
- $W_{H,\mathscr T}(M)=o(M)$, or any strict retained constant;
- any fixed-$j=1$ booking, Route 1, and every conclusion about
  $e+\pi$.

## 8. Ledger consequence



$$
\begin{array}{c|c}
\text{quantity}&\text{Item 384 value}\\ \hline
\text{information-class maximal joint-zero mass}&M/6+o(M)\\
\text{new actual-family weighted theorem}&0\\
\text{new proved linear log rate}&0\\
\text{new fixed-}j=1\text{ capacity reduction}&0\\
\text{retained fixed-}j=1\text{ ceiling per }6M&1/36
\end{array}                                               \tag{8.1}
$$



Item 384 is a Closer result: it removes a material but insufficient
information class from the live program.  It is not an Auditor decision
and does not alter any booked mass.
