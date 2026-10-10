> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 201 — sharp comparable-gap transfer and the exact packing boundary

Date: 2026-08-30 (Beijing time)

## 1. Verdict

This item continues Route 1 from Item 199 and uses only its report, its
checker, and the actual mixed-cubic row file referenced there.  It does not
produce a positive-rate matching family.  It gives a precisely scoped no-go
and identifies the remaining information gap.

For



$$
C_0(N)=0,\qquad C_1(N)=1,
$$





$$
C_{j+1}(N)=(4N+4j+2)C_j(N)+C_{j-1}(N),
$$



the crude height estimate of Item 199 can be replaced by the uniform sharp
equivalent



$$
\boxed{
 C_h(N)=4^{h-1}\frac{\Gamma(N+h+\tfrac12)}
                         {\Gamma(N+\tfrac32)}
        \left(1+O_A(N^{-1})\right),\qquad 1\le h\le AN.}       \tag{1.1}
$$



Writing $t=h/N$ and



$$
\Psi(t)=(1+t)\log(1+t)-t,
$$



this is equivalently



$$
\boxed{
 \log C_h(N)=(h-1)\log(4N)+N\Psi(t)+O_A(N^{-1}).}             \tag{1.2}
$$



At the frozen beta saddle



$$
\theta_N:=\frac{N\log N}{6m}\longrightarrow
 \theta=1.168531187179486497926964890273\ldots,
$$



one therefore has, for $h/N\to\alpha$,



$$
\boxed{\frac{\log C_h(N)}{6m}\longrightarrow\theta\alpha.}  \tag{1.3}
$$



Thus the leading exponent in Item 199 was already the true transfer
capacity, not an artifact of its height bound.  If



$$
G=0.019632983669431793880306401240\ldots,
$$



then a single common sequential block cannot fill the residual gap when



$$
\boxed{
 \limsup\frac hN<\alpha_0:=\frac G\theta
 =0.0168014203513219247791020171289\ldots.}                   \tag{1.4}
$$



Above $\alpha_0$, (1.3) is capacity only; it supplies no divisor of the
actual $T_N=\Delta_Ng_N$.

There is also an exact cost comparison.  For $h\ge2$,



$$
\boxed{
 C_h(N)\frac{q_{N+1}}{q_N}
 <\frac{q_{N+h}}{q_N}
 <C_h(N)\left(\frac{q_{N+1}}{q_N}+1\right).}                 \tag{1.5}
$$



Since every reusable common block $S$ divides $C_h(N)$, moving the
second beta index costs strictly more beta-denominator height than the
entire common-modulus credit:



$$
\log\frac{q_{N+h}}{q_N}-\log S
 >\log\frac{q_{N+1}}{q_N}>\log(4N+2).                       \tag{1.6}
$$



Equivalently, the net normalized transfer-recycling gain obeys



$$
\boxed{
 \frac{\log S-\log(q_{N+h}/q_N)}{6m}
 <-\frac{\log(4N+2)}{6m}<0.}                               \tag{1.7}
$$



The loss is a factor greater than $4N+2$: polynomial, hence zero-rate,
but strictly adverse at every finite $N$.  Both cost and capacity have
leading saddle rate $\theta\alpha$.  Consequently a
**pure two-index transfer-recycling ledger**, in which the common modulus is
the only new benefit and the beta-index displacement is a cost, can at best
tie at linear scale and loses exactly at every finite $N$.  The same is
true for an ordered one-parent forest of reused blocks.  This no-go does not
apply to fresh single-index factors, to an additional analytic benefit not
present in this ledger, or to a multi-parent portfolio.

Three-index coprimality does not close the latter case.  It makes pair
supports disjoint, but disjoint pair-specific primes may still occupy all
edges incident to one index.  The exact aggregate statements are:

* if every triple in a portfolio has gcd one, its reuse credit $R$ and
  unique CRT modulus $L$ satisfy $R\le L$;
* the pair-specific credit divides the lcm, rather than merely the product,
  of all odd transfer continuants on its reuse edges;
* for three transfer edges, the three pairwise gcds of those continuants are
  all exactly the same common gcd.  Removing it gives the sharp lcm formula;
* the proved gcd-one theorem is only local, for
  $N,N+2,N+4$.  It does not imply global triple-gcd-one, and an actual
  frozen row already supplies a nonconsecutive counterexample.

No stronger positive-rate packing bound follows from the present data.
The missing arithmetic input is an asymptotic bound for
$\gcd(q_N,q_{N+h})=\gcd(q_N,C_h(N))$, or equivalently a useful lower bound
on shared gcds among comparable-gap transfer capacities that would shrink
their lcm.  That problem remains open.

## 2. Exact sharp asymptotic

Put



$$
a_j=4N+4j+2\qquad(1\le j<h),
 \qquad P_h(N)=\prod_{j=1}^{h-1}a_j.
$$



The continuant expansion is a path-matching identity:



$$
\frac{C_h(N)}{P_h(N)}
 =\sum_{M}\prod_{\{j,j+1\}\in M}\frac1{a_ja_{j+1}},         \tag{2.1}
$$



where $M$ ranges over matchings in the path with vertices
$1,\ldots,h-1$.  The empty matching contributes $1$.  The total
one-edge weight telescopes:



$$
S_{N,h}:=\sum_{j=1}^{h-2}\frac1{a_ja_{j+1}}
 =\frac1{16}\left(
   \frac1{N+\tfrac32}-\frac1{N+h-\tfrac12}\right).          \tag{2.2}
$$



Because every matching is a subset of the edge set, for (S_{N,h}<1),



$$
1+S_{N,h}
 \le\frac{C_h(N)}{P_h(N)}
 \le1+S_{N,h}+\frac{S_{N,h}^2}{1-S_{N,h}}.                 \tag{2.3}
$$



This is an exact rational inequality.  Uniformly for $h\le AN$, it gives



$$
\frac{C_h(N)}{P_h(N)}=1+O_A(N^{-1}).                      \tag{2.4}
$$



It also gives the first relative correction.  With (t=h/N) bounded,



$$
\frac{C_h(N)}{P_h(N)}
 =1+\frac{t}{16(1+t)N}+O_A(N^{-2}).                        \tag{2.5}
$$



The spine product is exact:



$$
P_h(N)=4^{h-1}
 \frac{\Gamma(N+h+\tfrac12)}{\Gamma(N+\tfrac32)}.          \tag{2.6}
$$



Uniform Stirling expansion in $0\le h/N\le A$ gives



$$
\log P_h(N)
 =(h-1)\log(4N)+(N+h)\log(1+t)-h+O_A(N^{-1}),              \tag{2.7}
$$



and (1.1)--(1.2) follow.  In particular, (1.1) is a relative
equivalent, not a logarithmic upper bound.

For later reference, the normalized expansion is



$$
\frac{\log C_h(N)}{6m}
 =\theta_N\left[
 t+\frac{t\log4+\Psi(t)}{\log N}
 -\frac{\log(4N)}{N\log N}
 +O_A\!\left(\frac1{N^2\log N}\right)
 \right].                                                  \tag{2.8}
$$



If one formally freezes $\theta_N=\theta$ and solves the sharp model for
the finite-(N) capacity crossing, then



$$
t_{\rm crit}(N)=\alpha_0-
 \frac{\alpha_0\log4+\Psi(\alpha_0)}{\log N}
 +O((\log N)^{-2}),                                        \tag{2.9}
$$



where



$$
\alpha_0\log4+\Psi(\alpha_0)
 =0.02343207425662527824161143175394746984\ldots.
$$



Equation (2.9) is a frozen-model refinement, not a new asymptotic claim
about the actual saddle error.  The theorem-level dichotomy is (1.4): a
fixed limit below (alpha_0) is impossible for one common block; a limit
at or above it is unresolved by capacity.

## 3. Transfer capacity versus beta-index displacement

Item 199 proves



$$
q_{N+h}=C_h(N)q_{N+1}+C_{h-1}(N+1)q_N.                   \tag{3.1}
$$



The second continuant is positive and, for $h\ge2$, strictly smaller
than (C_h(N)).  One way to see this is to expand both as continuants:
$C_{h-1}(N+1)$ uses the tail $a_2,\ldots,a_{h-1}$, whereas
$C_h(N)$ contains $a_1$ times that positive tail plus another
nonnegative term.  Dividing (3.1) by (q_N) proves (1.5).

The adjacent recurrence gives



$$
4N+2<\frac{q_{N+1}}{q_N}\le4N+3,                         \tag{3.2}
$$



with strictness on the right for $N\ge2$.

Consequently



$$
\log\frac{q_{N+h}}{q_N}
 =\log C_h(N)+\log(4N)+O(N^{-1}),                          \tag{3.3}
$$



and



$$
\frac1{6m}\log\frac{q_{N+h}}{q_N}\longrightarrow
 \theta\alpha.                                           \tag{3.4}
$$



Let $S=(T_N,T_{N+h})$, or let $S$ be what remains after any already
booked reservoir is removed.  Item 199 gives $S\mid C_h(N)$, so (1.6)
and (1.7) are exact.  Thus the normalized net is strictly negative with a
polynomial deficit and tends to zero from below under the saddle
hypotheses.  This shows why going to a comparable gap does not create a
free linear exponent in this ledger: the newly available transfer capacity
is precisely one beta-height displacement exponent.

The scope matters.  Equations (1.5)--(1.6) compare one common reuse credit
with the height cost of moving its endpoint.  They do not say that every
analytic effect of increasing (N) is adverse, and they do not upper-bound
a fresh factor supported at only one index.

## 4. The three-transfer gcd theorem

Let



$$
v_n=(p_n,q_n),\qquad
 D_{ij}=\det(v_i,v_j).
$$



Every (p_n,q_n) is odd.  The adjacent Wronskian from Item 199 implies
((p_n,q_n)=1).  For (i<j),



$$
D_{ij}=\pm2C_{j-i}(i).                                   \tag{4.1}
$$



For (i<j<k), the two-dimensional Pluecker identity is



$$
D_{ij}v_k-D_{ik}v_j+D_{jk}v_i=0.                         \tag{4.2}
$$



If an odd prime power divides two of the three determinants, (4.2) and
((p_i,q_i)=1) force it to divide the third.  Therefore, on writing



$$
A=\operatorname{odd}(C_{j-i}(i)),\quad
 B=\operatorname{odd}(C_{k-i}(i)),\quad
 D=\operatorname{odd}(C_{k-j}(j)),
$$



one has the all-index identity



$$
\boxed{
 (A,B)=(A,D)=(B,D)=(A,B,D)=:H.}                           \tag{4.3}
$$



It follows primewise that



$$
\boxed{\operatorname{lcm}(A,B,D)=\frac{ABD}{H^2}.}       \tag{4.4}
$$



Thus a comparable triple could improve the naive product capacity only
through the term $2\log H$.  No asymptotic lower bound for $H$ is
available from Item 199 or the frozen input.  In particular, finite samples
with small (H) cannot prove that this term has zero rate.

At the nearest parity-compatible triple the situation is completely
explicit:



$$
\operatorname{odd}(C_2(N))=2N+3,
$$





$$
\operatorname{odd}(C_2(N+2))=2N+7,
$$





$$
\operatorname{odd}(C_4(N))
 =(2N+5)(8N^2+40N+43).                                   \tag{4.5}
$$



These three integers are pairwise coprime.  The first two differ by (4).
Modulo either (2N+3) or (2N+7), the quadratic factor in the third is
(1), and its linear factor differs by (2).  Thus (4.3) has (H=1)
here.  There is no hidden gcd loss among the three transfer capacities.

For the actual sequential factors, put



$$
G_{ij}=(T_i,T_j),\qquad H_T=(T_i,T_j,T_k),
$$



and define the exact reuse multiplicity



$$
R_{ijk}=\frac{T_iT_jT_k}{\operatorname{lcm}(T_i,T_j,T_k)}.
$$



A primewise ordering of the three valuations gives



$$
\boxed{R_{ijk}=\frac{G_{ij}G_{ik}G_{jk}}{H_T}.}           \tag{4.6}
$$



For (N,N+2,N+4), Item 199 has (H_T=1).  Hence the three pair gcds are
pairwise coprime, and (4.5) yields



$$
R_{N,N+2,N+4}\mid
 (2N+3)(2N+7)(2N+5)(8N^2+40N+43).                         \tag{4.7}
$$



This is polynomial and therefore zero-rate.  It is also the sharp
information obtainable from those three edge capacities: the capacities
themselves are pairwise coprime, so taking their gcds cannot reduce (4.7).

## 5. Aggregate CRT accounting

For selected indices $n_1<\cdots<n_k$, write



$$
P=\prod_{i=1}^kT_{n_i},\qquad
 L=\operatorname{lcm}_{i}T_{n_i},\qquad
 R=\frac PL.                                               \tag{5.1}
$$



Here (L) is the unique combined prime-power modulus and (R) is exactly
the multiplicative credit from reusing digits already present at an earlier
index.  Indeed, primewise, its exponent is



$$
\sum_i v_p(T_{n_i})-\max_i v_p(T_{n_i}).                 \tag{5.2}
$$



There are three distinct packing regimes.

### 5.1 Global triple-gcd-one

Assume every three selected (T)'s have gcd one.  Each prime then occurs at
at most two indices.  The pair gcds (G_{ij}) have pairwise disjoint prime
supports and



$$
\boxed{R=\prod_{i<j}G_{ij}.}                             \tag{5.3}
$$



If



$$
A_{ij}=\operatorname{odd}(C_{n_j-n_i}(n_i)),
$$



then Item 199 and pairwise support disjointness give the stronger packing
bound



$$
\boxed{R\mid\operatorname{lcm}_{i<j}A_{ij}.}             \tag{5.4}
$$



The generic product of all edge capacities is unnecessary.  Also, for a
prime appearing with exponents $a\ge b>0$ at its two vertices, its
exponents in (L,R) are (a,b).  Hence



$$
\boxed{R^2\mid P,\qquad R\le L.}                         \tag{5.5}
$$



Thus globally triple-free pair reuse never exceeds the unique CRT modulus
that remains to be paid.  Since $g_N\mid\Delta_N$, one also has the exact
local capacity



$$
T_N=\Delta_Ng_N\mid b^2,\qquad T_N\mid q_N^2,             \tag{5.6}
$$



and therefore $R\le b^k$ and $R\le\prod_iq_{n_i}$.  These latter bounds
are not strong enough to close Route 1, but they prevent unlimited edge
packing at one vertex.

### 5.2 One-parent ordered reuse

Suppose every reused prime block is assigned to one edge $i\to j$, and
each later vertex $j$ has at most one earlier parent.  Distinct edge
blocks are coprime, so their product is the aggregate credit.  By (1.6),



$$
S_{ij}<\frac{q_{n_j}}{q_{n_i}}
 \le\frac{q_{n_j}}{q_{n_1}}.
$$



Multiplying once for each child gives



$$
\boxed{
 R_{\rm edge}<\prod_{j=2}^k\frac{q_{n_j}}{q_{n_1}}.}       \tag{5.7}
$$



More precisely, if $i(j)$ is the unique parent of child $j$, then



$$
\frac{R_{\rm edge}}
 {\prod_j(q_{n_j}/q_{n_{i(j)}})}
 <\prod_j\frac1{4n_{i(j)}+2}.                              \tag{5.8}
$$



Thus its normalized net is at most zero, with one explicit polynomial loss
per reuse edge.  For a fixed number of edges the loss has zero normalized
rate, so this is an exact finite deficit rather than an extra negative
linear exponent.

At saddle-scaled locations $n_j/N\to1+t_j$, this says



$$
\operatorname{rate}(R_{\rm edge})
 \le\theta\sum_{(i,j)}(t_j-t_i)
 \le\theta\sum_{j=2}^kt_j,                                \tag{5.9}
$$



which is no larger than the total beta-index displacement of the selected
children.  This proves the forest version of the pure-recycling no-go.

### 5.3 What the local theorem does not give

Item 199 proves gcd one only for every three consecutive vertices of the
parity lattice.  In a block of $k$ such vertices, a fixed prime support
can therefore avoid three consecutive positions while still occupying



$$
s_k=\left\lceil\frac{2k}{3}\right\rceil                 \tag{5.10}
$$



positions.  From (5.2) one gets only



$$
R^{s_k}\le P^{s_k-1}.                                    \tag{5.11}
$$



As $k\to\infty$, (5.11) leaves the reusable fraction arbitrarily close to
the full gross modulus.  Local triple coprimality therefore supplies no
uniform aggregate saving.

More importantly, even global triple-gcd-one permits a later index to use
different primes on edges to two or more earlier indices.  The edge supports
remain disjoint, but the right side of (5.7) would then count that endpoint
more than once.  Formula (5.4) is the exact available correction.  Without
an asymptotic upper bound for its lcm, or for the denominator gcds feeding
the actual $T$'s, a multi-parent positive-rate portfolio is neither proved
nor ruled out.

This is the exact information boundary: three-index coprimality closes
common-to-three recycling and one-parent recycling, but it does not close
pair-specific multi-parent packing.

## 6. Exact finite replay — not asymptotic evidence

The companion checker performs the following deterministic checks.

1. For $1\le N\le160$ and $1\le h\le2N$, it checks 25,760 instances
   each of the spine lower bound, the two-sided rational correction (2.3),
   the transfer determinant, and the displacement sandwich (1.5).
2. For $1\le N\le60$ and $1\le r,s\le24$, it checks 34,560 triples for
   (4.3)--(4.4), with no failure.  It checks (4.5) and its pairwise
   coprimality for another 1,000 values of (N).
3. It reconstructs all 15,150 actual local factors for $1\le m\le100$
   and scans all 1,515,000 parity-compatible pairs.  There are 212,720
   pairs with common (T) above one and 175 with common (g) above one.
4. In the narrow finite bin
   $\alpha_0\le h/N<0.02$, it checks 4,614 pairs.  Exactly 254 have common
   (T>1); none has common (g>1).  The largest common (T) is (77), at
   ((m,N,M)=(20,114,116)).
5. The largest common factor in the full finite scan is an exact
   synchronized pair at
   ((m,N,M)=(40,40,132)): both indices have
   $(\Delta,g,T)=(199,199,39601)$.  Its ratio is $h/N=23/10$.  This is a
   finite witness, not a positive-rate family.
6. The actual row (m=4) gives
   ((T_2,T_4,T_{16})=(7,1001,7)), whose common gcd is (7).  Thus the
   nearest-triple theorem cannot be extended to arbitrary triples.  In row
   (m=99), the prime (7) occurs at 86 parity-compatible indices while
   never occupying three consecutive parity positions.

One sampled comparable transfer triple, ((N,r,s)=(20,10,10)), has common
odd edge gcd (H=355).  This illustrates (4.3), but says nothing about the
asymptotic size of (H).

Every count in this section is classified **FINITE**.  In particular, the
empty final-matching bin near (alpha_0) is not used to infer a zero density
or an asymptotic obstruction.

## 7. Route-1 boundary

### PROVED

* The path-matching formula (2.1), exact correction bounds (2.2)--(2.3),
  uniform relative equivalent (1.1), and sharp logarithmic expansion
  (1.2).
* The exact saddle rate $\theta\alpha$ and the single-common-block no-go
  for every fixed limiting gap ratio below $G/\theta$.
* The displacement sandwich (1.5), exact polynomial loss (1.6)--(1.7), and the pure
  two-index and one-parent-forest transfer-recycling no-go.
* The all-index odd transfer-gcd identity (4.3), lcm identity (4.4), and
  nearest-triple coprime capacities (4.5)--(4.7).
* The exact reuse identities (5.1)--(5.5), including $R\le L$ under
  global triple-gcd-one, and the local support bound (5.10)--(5.11).
* $T_N\mid b^2$ and $T_N\mid q_N^2$.

### FINITE

* All replay ranges, counts, examples, and maxima in Section 6.  They are
  exact within their declared scope and are not asymptotic evidence.

### OPEN

* A positive-rate lower bound for one actual (T_N), one actual (g_N),
  or a comparable-gap common block.
* An asymptotic bound for
  $\gcd(q_N,q_{N+h})=\gcd(q_N,C_h(N))$ when $h\asymp N$.
* A rate bound for the common odd gcd (H) in (4.3), or for the lcm in
  (5.4), over a comparable multi-index portfolio.
* Multi-parent packing with pair-specific prime supports.  Local
  three-index coprimality does not rule it out.
* Fresh factors occurring at only one index, existence of the required
  actual primes and valuations in (b_m), the normalized final congruence,
  and a small moving CRT representative.
* Any conclusion about irrationality, rationality, or transcendence of
  $e+\pi$.

The result is therefore a sharp no-go for pure transfer recycling, not a
route-wide impossibility theorem.

## 8. Portable replay

After integration at the archive root, run

```text
python -m py_compile scripts/item201_comparable_gap_certificate.py
python scripts/item201_comparable_gap_certificate.py \
  --archive . \
  --output results/item201_comparable_gap_certificate_replay.json
```

The canonical and replay JSON files are byte-identical.  The checker records
only archive-relative input names and their SHA-256 hashes.  It embeds no
host path, timestamp, Python version, platform string, or runtime-sensitive
floating value.  Explicit input flags exist only for flat staging before
archive integration; they do not alter serialized paths.
