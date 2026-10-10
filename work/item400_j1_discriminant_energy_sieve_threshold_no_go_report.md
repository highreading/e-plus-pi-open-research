> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 400 — discriminant coprimality, energy blindness, and the sharp ambient-sieve threshold for fixed $j=1$

Date: 2026-09-01

## 1. Outcome and capacity decision first

Retain the actual fixed-$j=1$ joint Hasse--transverse collision set



$$
\mathcal Z_M=\{p\in\mathcal P_M:p\mid R_{H\mathscr T}(M)\},
 \qquad
 W(M)=\sum_{p\in\mathcal Z_M}\log p,                 \tag{1.1}
$$



and Item 395's logarithmic-window cluster radical



$$
\mathcal C_{M,D}
 =\prod_{\substack{p\in\mathcal Z_M\\
          \exists q\in\mathcal Z_M,\ 0<|p-q|\le 2D}}p. \tag{1.2}
$$



The admission test at $D\sim\log M$ is applied before introducing any
new invariant.  A useful upper bound must prove



$$
\log\mathcal C_{M,\lfloor\log M\rfloor}
 <(1/12-\varepsilon)M                                  \tag{1.3}
$$



for some fixed $\varepsilon>0$, or otherwise give a strict retained
constant below (1/36) per (6M).

No such actual-family bound follows from the proposed discriminant,
derivative/Vandermonde, multiplicative-energy, or support-only sieve
inputs.  Instead this item proves a sharp information-class no-go.

1. **PROVED — the discriminant and first-derivative carriers are exactly
   coprime to the target support.**  If
   $F_M(X)=\prod_{p\in\mathcal Z_M}(X-p)$ and
   $R_M=\prod_{p\in\mathcal Z_M}p$, then
   

$$
\gcd(R_M,\operatorname{Disc}F_M)
      =\gcd\left(R_M,\prod_{p\in\mathcal Z_M}F'_M(p)\right)
      =\gcd(R_M,F'_M(0))=1.                            \tag{1.4}
$$


   This is an exact theorem for the actual collision polynomial, including
   every nonempty or singleton case.

2. **PROVED — the short-gap Vandermonde has sublinear height but carries no
   endpoint prime.**  At $D\asymp\log M$, the product of all short root
   differences has logarithm (o(M)) by Item 391's Selberg bound, but it is
   coprime to $R_M$.  It records the labels of the graph edges and forgets
   their prime endpoints.

3. **PROVED — ordinary multiplicative energy is completely gap-blind.**  A
   set of (n) distinct primes has ordered multiplicative energy
   

$$
E_\times(\mathcal Z_M)=2n^2-n,                  \tag{1.5}
$$


   independently of every spacing or clustering property.  Graph-degree
   energy likewise needs a new bound on positive-degree vertices; its
   universal inequalities allow the entire raw scale.

4. **PROVED — Item 395's threshold is sharp for ambient-prime/sieve
   information.**  Take the full candidate set
   $\mathcal Z_M^{\rm all}=\mathcal P_M$.  If
   $D\sim c\log M$, $c>1/2$, then its cluster radical satisfies
   

$$
\liminf_{M\to\infty}{1\over M}
       \log\mathcal C^{\rm all}_{M,D}
      \ge {2c-1\over12c}.                              \tag{1.6}
$$


   At $c=1$, the lower bound is exactly $1/12$.  More generally the
   right side of (1.6) is exactly the strict-saving coefficient that Item
   395 requires one to beat.

Consequently no theorem which uses only the tied prime support, the generic
root-polynomial identities, universal discriminant or energy inequalities,
and a sieve/large-sieve estimate valid for every subset of the candidate
primes can prove (1.3).  The full candidate set is a countermodel, and Item
384 shows that even a fixed-rank filtered-Hasse selector package can realize
that full pattern.

This does **not** close a gate-specific large sieve, monodromy theorem,
cross-(M) recurrence, or special factorization of the original
Hasse--transverse moments.  It proves no new upper bound on the actual
$\mathcal C_{M,D}$.  Hence



$$
\boxed{\text{new booking}=0,\qquad
        \text{new whole-cell capacity reduction}=0,\qquad
        \text{retained fixed-}j=1\text{ ceiling}=1/36.} \tag{1.7}
$$



## 2. Actual tied setup and the exact admission coefficient

The candidate interval is



$$
L_M={4M+3\over3},\qquad U_M={3M-1\over2},\qquad
 H_M=U_M-L_M={M-9\over6}.                              \tag{2.1}
$$



Let



$$
F_M(X)=\prod_{p\in\mathcal Z_M}(X-p),\qquad
 R_M=\prod_{p\in\mathcal Z_M}p,
 \qquad n_M=|\mathcal Z_M|,                            \tag{2.2}
$$



with $F_M=R_M=1$ when the set is empty.  Join two roots when



$$
0<|p-q|\le2D,                                         \tag{2.3}
$$



and write $\Gamma_{M,D}$ for the resulting graph.  Its positive-degree
vertex radical is exactly (1.2).

Item 395 gives



$$
W(M)\le\log\mathcal C_{M,D}
 +\left(1+{M-9\over12D}\right)\log U_M.               \tag{2.4}
$$



For $D\sim c\log M$, a strict improvement over the raw
$W(M)\le M/6+o(M)$ therefore requires



$$
\limsup {1\over M}\log\mathcal C_{M,D}
 <a(c),\qquad
 a(c):={2c-1\over12c},\qquad c>{1\over2}.              \tag{2.5}
$$



At $c=1$, $a(1)=1/12$.  Every proposed invariant below is judged
against (2.5), not merely against an unspecified (O(M)) estimate.

## 3. The discriminant and Vandermonde are candidate-prime units

Order the roots $p_1<\cdots<p_n$ and put



$$
V_M=\prod_{1\le i<j\le n}(p_j-p_i).                  \tag{3.1}
$$



Every nonzero root difference obeys



$$
0<p_j-p_i\le H_M={M-9\over6}<L_M\le r               \tag{3.2}
$$



for every candidate prime $r\in\mathcal Z_M$.  Since $r$ is prime,
it divides no factor in (3.1).  Thus



$$
\boxed{\gcd(R_M,V_M)=1.}                              \tag{3.3}
$$



For a monic squarefree root polynomial,



$$
\operatorname{Disc}F_M=V_M^2,                        \tag{3.4}
$$



and



$$
\prod_{p\in\mathcal Z_M}F'_M(p)
 =(-1)^{n_M(n_M-1)/2}V_M^2.                            \tag{3.5}
$$



Equations (3.3)--(3.5) give the first two equalities in (1.4).

There is a separate exact obstruction at the origin.  For $n_M\ge1$,



$$
F'_M(0)=(-1)^{n_M-1}
       \sum_{p\in\mathcal Z_M}{R_M\over p}.           \tag{3.6}
$$



Fix a root prime (r).  Modulo (r), every term in (3.6) vanishes except
the term $p=r$, and



$$
F'_M(0)\equiv(-1)^{n_M-1}{R_M\over r}\not\equiv0
 \pmod r.                                              \tag{3.7}
$$



Hence $\gcd(R_M,F'_M(0))=1$.  The empty-set convention also gives one,
and the singleton case has $F'_M(0)=1$.

The conclusion is stronger than a poor height estimate: these natural
derivative/discriminant integers have **zero** valuation at every target
prime.  They cannot be external carriers for $\mathcal C_{M,D}$.

## 4. A sublinear short-gap integer which loses every endpoint

Let $E_{M,D}$ be the edge set of $\Gamma_{M,D}$, and define the
short-gap Vandermonde factor



$$
V_{M,D}^{\rm short}
 =\prod_{\substack{\{p,q\}\in E_{M,D}\\p<q}}(q-p),   \tag{4.1}
$$



with empty product one.  This is the part of (3.1) supported on gaps at
most (2D).  Equation (3.2) still gives



$$
\boxed{\gcd(R_M,V_{M,D}^{\rm short})=1.}              \tag{4.2}
$$



On the other hand it is genuinely small.  Every edge has gap (2d) for
some $1\le d\le D$, so



$$
\log V_{M,D}^{\rm short}\le |E_{M,D}|\log(2D).       \tag{4.3}
$$



Because the actual edge set is a subset of the ambient prime-pair set,
Item 391's uniform Selberg bound and exact singular-factor average imply,
for $D\le\log U_M+O(1)$,



$$
|E_{M,D}|
 \le\sum_{d\le D}\pi_2(U_M;d)
 \le {\pi C_{\rm S}\over2}
      {U_MD\over(\log U_M)^2}.                         \tag{4.4}
$$



Here $C_{\rm S}$ is the one absolute Selberg constant in Item 391.
Taking $D\sim\log M$ in (4.3)--(4.4) gives



$$
\boxed{\log V_{M,D}^{\rm short}
 =O\!\left({M\log\log M\over\log M}\right)=o(M).}   \tag{4.5}
$$



Thus the short edges do admit a sublinear-height integer encoding, but it
encodes only their small difference labels.  By (4.2), it contains none of
the endpoint primes whose radical is (1.2).  This is the precise failure of
the tempting argument "the short-gap product is small, therefore the
cluster radical is small."

Item 398 gives the complementary endpoint product



$$
\mathcal E_{M,D}
 =\prod_{\{p,q\}\in E_{M,D}}pq
 =\prod_{p\in\mathcal Z_M}p^{\deg_D(p)},
 \qquad
 \operatorname{rad}\mathcal E_{M,D}=\mathcal C_{M,D}.  \tag{4.6}
$$



Unlike (4.1), (4.6) retains the endpoints, but it repeats them according to
degree and has no subthreshold height theorem.  The two natural products
therefore form an exact dichotomy: the gap-label carrier is sublinear and
coprime to the target, while the endpoint carrier has the right radical and
retains the unknown linear mass.

## 5. Multiplicative energy is exactly blind to logarithmic clustering

For a finite set (S), use the standard ordered multiplicative energy



$$
E_\times(S)=
 \#\{(a,b,c,d)\in S^4:ab=cd\}.                         \tag{5.1}
$$



If (S) consists of (n) distinct primes, unique factorization gives



$$
\{a,b\}=\{c,d\}                                      \tag{5.2}
$$



as multisets.  There are $n$ diagonal ordered pairs $a=b$, each with
one representation, and $n(n-1)$ ordered pairs with $a\ne b$, each
with two representations.  Therefore



$$
\boxed{E_\times(S)=n+2n(n-1)=2n^2-n.}                \tag{5.3}
$$



In particular two prime sets with the same cardinality have identical
multiplicative energy even if one is entirely isolated at scale (D) and
the other is entirely clustered.  No multiplicative-energy inequality
which uses only (5.3) can bound (1.2).

The local graph energies do see additive spacing, but their universal
content is still insufficient.  Put



$$
e_D=|E_{M,D}|,\qquad
 N_D=\#\{p:\deg_D(p)>0\},\qquad
 Q_D=\sum_p\deg_D(p)^2.                                \tag{5.4}
$$



The handshake identity and Cauchy give



$$
N_D\le2e_D,
 \qquad
 4e_D^2\le N_DQ_D.                                    \tag{5.5}
$$



Item 398's modular theorem supplies



$$
\deg_D(p)\le D+\lfloor D/3\rfloor,                   \tag{5.6}
$$



and hence



$$
Q_D\le2e_D\bigl(D+\lfloor D/3\rfloor\bigr).         \tag{5.7}
$$



Equations (5.5)--(5.7) give lower bounds on $N_D$ from a large edge
energy, but no upper bound sharper than $N_D\le2e_D$.  Combining that
last inequality with the ambient pair sieve gives only



$$
\log\mathcal C_{M,D}\le2e_D\log U_M=O(M)             \tag{5.8}
$$



at $D\asymp\log M$, with no coefficient satisfying (2.5).  Weighting an
endpoint by its graph degree, as in (4.6), increases valuations and does
not reduce its radical.

## 6. The full ambient prime set saturates the admission threshold

The preceding failures are not merely losses in the displayed
inequalities.  The coefficient (a(c)) itself is sharp for every theorem
that only knows "a subset of the tied candidate primes."

Take



$$
\mathcal Z_M^{\rm all}=\mathcal P_M,
 \qquad
 R_M^{\rm all}=\prod_{p\in\mathcal P_M}p.              \tag{6.1}
$$



The prime number theorem in the fixed linear interval gives



$$
\sum_{p\in\mathcal P_M}\log p
 =\vartheta(U_M)-\vartheta(L_M^-)
 =H_M+o(M)={M\over6}+o(M).                             \tag{6.2}
$$



Let $\mathcal I^{\rm all}_{M,D}$ be the primes in $\mathcal P_M$ with
no second candidate prime within numerical distance $2D$.  Distinct
members of this isolated set are more than $2D$ apart, so elementary
packing in an interval of length $H_M$ gives



$$
|\mathcal I^{\rm all}_{M,D}|
 \le1+\left\lfloor{H_M\over2D}\right\rfloor.         \tag{6.3}
$$



Therefore, if $D\sim c\log M$,



$$
\sum_{p\in\mathcal I^{\rm all}_{M,D}}\log p
 \le\left(1+{H_M\over2D}\right)\log U_M
 ={M\over12c}+o(M).                                   \tag{6.4}
$$



Subtract (6.4) from (6.2).  The complement is precisely the positive-degree
vertex radical for the full candidate set, so



$$
\boxed{
 \log\mathcal C^{\rm all}_{M,D}
 \ge\left({1\over6}-{1\over12c}\right)M+o(M)
 ={2c-1\over12c}M+o(M).}                              \tag{6.5}
$$



This proves (1.6).  For $c=1$,



$$
\liminf {1\over M}
 \log\mathcal C^{\rm all}_{M,\lfloor\log M\rfloor}
 \ge{1\over12}.                                      \tag{6.6}
$$



The lower coefficient in (6.5) is exactly (a(c)), the strict upper
coefficient demanded by (2.5).  Thus no uniform support-only estimate can
insert the needed $\varepsilon$.

This witness also respects the local selector information already audited.
Item 384 constructs, for every subset of $\mathcal P_M$, a nonzero
raw-scale CRT selector inside a fixed-rank filtered-Hasse package.  Taking
the full subset realizes (6.1).  Fixed rank, fixed Hodge data, algebraic
codimension, and generic local Frobenius regularity therefore do not remove
the threshold-saturating witness.

## 7. Sharp information-class no-go

Define the **discriminant--energy--Vandermonde--sieve information class** to
consist of arguments whose inputs are restricted to:

1. $\mathcal Z_M\subseteq\mathcal P_M$ and the tied interval (2.1);
2. the root products $F_M,R_M$, generic polynomial identities, their
   discriminant, derivatives, and Vandermonde products;
3. ordinary multiplicative energy or the universal graph identities
   (5.5)--(5.7);
4. prime, pair-sieve, large-sieve, or packing estimates valid uniformly for
   every subset of $\mathcal P_M$; and
5. the fixed-rank local selector geometry shown universal in Item 384.

Within this class:

- the derivative/discriminant candidate part is one by (1.4);
- the sublinear short-gap integer is coprime to the endpoint radical by
  (4.2)--(4.5);
- multiplicative energy is a function of cardinality alone by (5.3);
- graph energy needs an external positive-degree vertex theorem; and
- the full candidate set violates every strict bound below (a(c)M) by
  (6.5).

Hence the following statement is false in this information class:



$$
\text{``there exist }c>1/2,\ \varepsilon>0\text{ such that }
 \log\mathcal C_{M,D}\le(a(c)-\varepsilon)M+o(M)
 \text{ for }D\sim c\log M.''                         \tag{7.1}
$$



This is a sharp no-go because $a(c)$ is not an arbitrary failed constant:
it is simultaneously the Item 395 admission coefficient and the ambient
lower coefficient (6.5).

The scope must not be enlarged.  A numerical discriminant identity special
to the actual hypergeometric orbit, extra residue exclusions supplied by the
actual gate, or cancellation across (M) is outside the class.  Such an
input would fail for the full-set witness and could still prove a strict
actual-family bound.

## 8. Minimal live inputs after this closure

A future fixed-$j=1$ theorem must introduce arithmetic which distinguishes
the actual selector from $\mathcal P_M$.  In capacity terms it must do one
of the following.

1. **Gate-specific larger sieve.**  Prove that the simultaneous divisibility
   conditions in Item 363 omit quantitatively many residue classes for a
   positive-mass family of auxiliary moduli.  The ordinary fact that roots
   are primes only omits the zero class and is already saturated by (6.1).
2. **Special derivative or discriminant law.**  Produce an external integer
   from the original Hasse--transverse moments, not merely from the unknown
   root polynomial, whose candidate part contains $\mathcal C_{M,D}$ and
   whose logarithmic height is $<(a(c)-\varepsilon)M$.
3. **Cross-$M$ correlation.**  Relate the actual selector maps at different
   (M)'s in a way incompatible with arbitrary CRT patterns.  Every theorem
   confined to one fixed $M$ must overcome Item 384's selector universality.
4. **Actual positive-degree bound.**  Prove directly that the actual joint
   gate has fewer than $(a(c)-\varepsilon)M/\log M$ clustered vertices in
   weighted form.  An ambient pair upper bound of the natural
   $M/\log M$ scale is insufficient.

Each candidate should be checked against (2.5) before a long proof.  Merely
producing another $O(M)$ estimate, a sublinear integer coprime to $R_M$,
or an energy identity that holds for (6.1) does not pass admission.

## 9. Deterministic replay and finite-data policy

The standard-library certificate pins Items 384, 391, 395, and 398 and
verifies, on declared abstract root sets inside actual candidate intervals:

1. the Vandermonde, discriminant, and product-of-root-derivatives identities;
2. exact coprimality of $R_M$ with the Vandermonde, discriminant,
   root-derivative product, $F'_M(0)$, and short-gap Vandermonde;
3. the formula $E_\times(S)=2|S|^2-|S|$ both directly and by product
   multiplicities;
4. graph degrees, edge count, degree energy, cluster radical, short-gap
   product, and endpoint edge product; and
5. exact rational values of (a(c)) and the isolated packing inequality.

The declared sets are algebraic controls only.  Full candidate sets among
the controls verify finite identities but do not support the asymptotic
theorem (6.5), which is proved from the prime number theorem and packing.
No actual collision search, zero census, optimization, or finite-to-infinite
inference is performed.

From the archive root run

```text
python work/item400_j1_discriminant_energy_sieve_threshold_no_go_certificate.py \
  --output work/item400_j1_discriminant_energy_sieve_threshold_no_go_certificate_replay.json
```

The replay must be byte-identical to the shipped certificate.

## 10. Strict decision and ledger

### PROVED

- exact candidate-prime coprimality of the discriminant, Vandermonde,
  product of root derivatives, and derivative at zero;
- sublinear height but zero target-prime content of the short-gap
  Vandermonde at logarithmic scale;
- exact multiplicative-energy blindness for every prime root set;
- the universal graph-energy limitations;
- the full ambient prime-set lower bound (6.5), exactly saturating Item
  395's admission coefficient;
- the scoped discriminant/energy/Vandermonde/support-only-sieve no-go;
- zero booking and retention of the (1/36) ceiling.

### CONDITIONAL OR OUTSIDE THE CLOSED CLASS

- a gate-specific larger-sieve or monodromy theorem;
- a special actual-moment carrier below the threshold (2.5);
- any cross-$M$ restriction on the actual selector;
- any strict bound on the actual $\mathcal C_{M,D}$.

### DECLARED EXACT CONTROLS ONLY

- four abstract prime-root sets inside the tied intervals;
- no actual gate scan and no density inference from finite data.

### OPEN

- logarithmic-window weighted zero density for the actual fixed-$j=1$
  gate;
- $W(M)=o(M)$ or any strict fixed-$j=1$ retained constant;
- any new Route-1 booking and every conclusion about $e+\pi$.



$$
\boxed{
 \text{new proved linear log rate}=0,\quad
 \text{new booked mass}=0,\quad
 \text{new whole-cell capacity reduction}=0.}         \tag{10.1}
$$


