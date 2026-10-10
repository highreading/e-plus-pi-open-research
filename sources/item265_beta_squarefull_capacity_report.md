> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 265: beta squarefull capacity leaves a high-singleton barrier

Date: 2026-08-31 (Beijing time)

## 1. Verdict

The sequential beta denominator is the fixed-seed continuant



$$
q_0=q_1=1,\qquad q_N=(4N-2)q_{N-1}+q_{N-2}.             \tag{1.1}
$$



For clarity, this report uses



$$
\operatorname{sqfull}(n)
 :=\prod_{v_p(n)\ge2}p^{v_p(n)},\qquad
E(n):={n\over\operatorname{rad}(n)}.                    \tag{1.2}
$$



Thus `sqfull` is the full powerful-supported part, not merely the
squarefull radical.  Prime by prime,



$$
\boxed{E(n)\mid\operatorname{sqfull}(n)\mid E(n)^2.}    \tag{1.3}
$$



Consequently



$$
\log\operatorname{sqfull}(q_N)=o(N\log N)
\quad\Longleftrightarrow\quad
\log E(q_N)=o(N\log N).                                 \tag{1.4}
$$



This is exactly the excess-valuation theorem which the sequential
matching branch needs in order to make all beta depth beyond two
squarefree copies negligible.

No such theorem follows from the presently archived data.  The strongest
uniform all-index estimate recovered here is the height bound



$$
\boxed{
\log\operatorname{sqfull}(q_N)
\le \log q_N
=N\log N+(\log4-1)N+O(\log N).}                         \tag{1.5}
$$



At the balanced beta saddle,



$$
{N\log N\over6m}\longrightarrow
\theta=1.1685311871794864979\ldots,                     \tag{1.6}
$$



so (1.5) remains a positive full-scale ceiling.  It neither proves a
little-oh squarefull bound nor reduces the matching capacity.

There is a genuine partial theorem.  Averaged over $N\le n<2N$, the
squarefree smooth support and every excess-valuation level whose
prime-power period is at most $N$ contribute $o(N\log N)$ per term
for the matching cutoff $X\asymp N\log N$.  All possible failure is
therefore localized to prime powers $p^a>N$.  Those levels occur at most
once per residue class in the block.  Exact gap/gcd identities control
their reuse, but not the deepest value at a prime.  That surviving
singleton maximum is the full unresolved squarefull-value problem.

The discriminant, resultant, primitive-divisor, and average-gcd routes do
not close it:

1. the reverse-Bessel discriminant makes every large root simple, while
   $p^2\mid q_N$ is the independent divided value $q_N/p\pmod p$;
2. the first block resultant which sees every singleton is
   $\prod_{N\le n<2N}q_n$, already of size
   $\exp((3/2+o(1))N^2\log N)$;
3. pairwise gcds see reuse and are identically blind to a prime power
   supported at one block index;
4. a primitive-divisor or largest-prime-factor theorem supplies new
   support, not an upper bound for the remaining powerful part.

These are rigorously scoped method barriers, not a proof that (1.4) is
false and not a conclusion about $e+\pi$.  The admission decision is:



$$
\boxed{\text{zero new Route-1 rate and zero new capacity reduction.}} \tag{1.7}
$$



## 2. Exact matching normalization and reservoir overlap

For the primitive mixed-cubic row, retain the archived notation



$$
c_m=\gcd(U_m,V_m),\qquad b_m={|V_m|\over c_m},
$$





$$
\Delta_{m,N}=\gcd(b_m,q_N),\qquad
g_{m,N}=\gcd(P^*_{m,N},\Delta_{m,N}).                    \tag{2.1}
$$



If



$$
\beta_p=v_p(b_m),\quad t_p=v_p(q_N),\quad
d_p=v_p(\Delta_{m,N}),\quad \gamma_p=v_p(g_{m,N}),
$$



then exactly



$$
d_p=\min(\beta_p,t_p),                                  \tag{2.2}
$$





$$
\gamma_p=
\begin{cases}
\min(\beta_p,v_p(P^*_{m,N})),&\beta_p=t_p>0,\\
0,&\text{otherwise}.
\end{cases}                                             \tag{2.3}
$$



In particular,



$$
\boxed{\Delta_{m,N}g_{m,N}\mid q_N^2.}                 \tag{2.4}
$$



Now let



$$
K_m^{(0)}={K_m\over\gcd(K_m,G_m)},\qquad
D_m={K_m^{(0)}\over\gcd(K_m^{(0)},c_m)}.                \tag{2.5}
$$



The deterministic clearing identities are



$$
K_m^{(0)}\mid V_m,\qquad D_m\mid b_m.                  \tag{2.6}
$$



If $k_p=v_p(K_m^{(0)})$ and
$\kappa_p=v_p(c_m)$, the total reservoir-traceable exponent already in
$c_m$, then recoverable through $\Delta$, and then duplicable through
$g$, is at most



$$
\min(k_p,\kappa_p)+2\max(k_p-\kappa_p,0)\le2k_p.        \tag{2.7}
$$



Thus squarefull beta digits on the same primes cannot be added again on
top of the optimistic two-copy reservoir.  The exact overlap-normalized
form is useful.  Define



$$
J_{m,N}:={\Delta_{m,N}g_{m,N}\over
 \gcd(\Delta_{m,N}g_{m,N},D_m^2)},\qquad
\overline q_{m,N}:={q_N\over\gcd(q_N,D_m)}.              \tag{2.8}
$$



Then



$$
\boxed{J_{m,N}\mid\overline q_{m,N}^{\,2}.}             \tag{2.9}
$$



Indeed, if $a_p=v_p(\Delta g)$ and $r_p=v_p(D_m)$,
then (2.4) gives $a_p\le2t_p$, and



$$
v_p(J)=(a_p-2r_p)_+
\le2(t_p-r_p)_+
=v_p(\overline q^{\,2}).                                \tag{2.10}
$$



This is the correct normalization for any proposed squarefull gain.  It
removes the two copies already allowed to the clearing divisor before
measuring genuinely unbooked beta capacity.  Since division cannot enlarge
the powerful-supported part,



$$
\operatorname{sqfull}(\overline q_{m,N})\mid
\operatorname{sqfull}(q_N).                             \tag{2.11}
$$



Therefore (1.4), if proved, would make the contribution in (2.9) beyond
$\operatorname{rad}(\overline q)^2$ negligible.  It would not by itself
control the two-copy squarefree core or prove its correlation with
$b_m$.

## 3. The uniform height ceiling

Positivity gives, for $N\ge2$,



$$
(4N-2)q_{N-1}<q_N<4Nq_{N-1}.                            \tag{3.1}
$$



Iterating yields



$$
\prod_{j=2}^{N}(4j-2)<q_N<4^{N-1}N!.                   \tag{3.2}
$$



The lower product is exactly



$$
\prod_{j=2}^{N}(4j-2)={(2N)!\over2\,N!}.               \tag{3.3}
$$



Stirling's formula applied to both sides of (3.2) proves the sharpened
height asymptotic



$$
\boxed{\log q_N=N\log N+(\log4-1)N+O(\log N).}          \tag{3.4}
$$



Combining (1.2) and (3.4) proves (1.5).  The same argument gives only



$$
\log E(q_N)\le\log q_N,
\qquad
2\log\!\prod_{p^2\mid q_N}p\le\log q_N.                \tag{3.5}
$$



At (1.6), the $O(N)$ secondary term is $o(m)$, so the right side of
(1.5), divided by $6m$, tends to $\theta$, not zero.  This is the
strongest uniform squarefull estimate supplied by height alone.  It fails
the positive-linear-capacity admission test.  In the two-copy majorant the
uncontrolled depth factor is $E(q_N)^2$, for which the same input gives
only



$$
\limsup {2\log E(q_N)\over6m}\le2\theta
=2.3370623743589729958\ldots.                            \tag{3.6}
$$



Thus the current theorem removes no positive amount from the raw deep-beta
capacity; overlap with the clearing reservoir must still be handled by
(2.8)--(2.10).

## 4. What recurrence periodicity does prove

For an odd prime $p$, let



$$
R_{p^a}=|\{0\le r<p^a:p^a\mid q_r\}|.
$$



The exact anti-period and zero-gap theorem give



$$
q_{n+p}\equiv-q_n\pmod p,\qquad R_p\le2p^{2/3}.         \tag{4.1}
$$



Prime-power periodicity then gives the unconditional but branching-blind
bound



$$
R_{p^a}\le p^{a-1}R_p\le2p^{a-1/3}.                    \tag{4.2}
$$



For $X\ge3$, the squarefree smooth support satisfies



$$
\sum_{n=N}^{2N-1}\log\operatorname{rad}_{\le X}(q_n)
\le3NX^{2/3}\log X+2X^{5/3}\log X.                    \tag{4.3}
$$



Define the fitted-period excess



$$
\mathcal E_X^{\mathrm{low}}(n)
=\sum_{p\le X}\ \sum_{\substack{a\ge2\\p^a\le N}}
\mathbf1_{p^a\mid q_n}\log p.                         \tag{4.4}
$$



Using (4.2) on an interval of length $N$ gives



$$
{1\over N}\sum_{n=N}^{2N-1}\mathcal E_X^{\mathrm{low}}(n)
\le6N^{1/3}\log N.                                     \tag{4.5}
$$



For fixed $C>0$ and $X=CN\log N$, equations (4.3)--(4.5) imply



$$
{1\over N}\sum_{n=N}^{2N-1}
\left(
\log\operatorname{rad}_{\le X}(q_n)
+\mathcal E_X^{\mathrm{low}}(n)
\right)=o(N\log N).                                    \tag{4.6}
$$



This is a theorem, not a finite trend.  It removes all low valuation
levels on average.  The exact complement is



$$
\mathcal E_X^{\mathrm{high}}(n)
=\sum_{p\le X}\ \sum_{\substack{a\ge2\\p^a>N}}
\mathbf1_{p^a\mid q_n}\log p.                         \tag{4.7}
$$



Here each residue class modulo $p^a$ meets the block at most once, so
root density no longer gives an averaging factor.  The only uniform bound
presently available is



$$
\mathcal E_X^{\mathrm{high}}(n)\le\log q_n=O(N\log N), \tag{4.8}
$$



which is exactly the forbidden main scale.

## 5. The high-singleton decomposition

Let



$$
b_p(N)=\min\{a\ge2:p^a>N\},\qquad
h_{p,n}=(v_p(q_n)-b_p(N)+1)_+                           \tag{5.1}
$$



for $N\le n<2N$.  Put



$$
H(N,X)=\sum_{p\le X}\sum_{n=N}^{2N-1}h_{p,n}\log p,
$$





$$
S(N,X)=\sum_{p\le X}\max_{N\le n<2N}h_{p,n}\log p.   \tag{5.2}
$$



For a pair $n<m$, define the thresholded overlap



$$
G_{N,X}(n,m)=\prod_{p\le X}p^{\min(h_{p,n},h_{p,m})}.   \tag{5.3}
$$



Sorting the $h_{p,n}$'s for each prime gives the exact envelope



$$
\boxed{
S(N,X)\le H(N,X)\le
S(N,X)+\sum_{N\le n<m<2N}\log G_{N,X}(n,m).}           \tag{5.4}
$$



The recurrence continuants



$$
P_0(x)=0,\quad P_1(x)=1,\quad
P_{d+2}(x)=(4x+4d+6)P_{d+1}(x)+P_d(x)                  \tag{5.5}
$$



satisfy



$$
q_{n+d}=P_d(n)q_{n+1}+P_{d-1}(n+1)q_n,
$$





$$
\boxed{\gcd(q_n,q_{n+d})=\gcd(q_n,P_d(n)).}             \tag{5.6}
$$



Thus (5.6) controls the overlap term in (5.4).  It cannot see $S(N,X)$:
a prime power occurring at exactly one block index contributes its full
depth to $S$ and zero to every pairwise gcd.  Even a perfect
average-gcd theorem would therefore leave the singleton maximum untouched.
This is an exact blind spot, not a heuristic objection.

The same issue appears in nearby sequential matching.  The archived
two-index theorem gives, for the transfer continuant $C_h(N)$,



$$
\gcd(\Delta_Ng_N,\Delta_{N+h}g_{N+h})\mid C_h(N),       \tag{5.7}
$$



and the common gcd of the three nearest parity-compatible factors at
$N,N+2,N+4$ is one.  Sublinear gaps therefore have zero reused rate,
but a single index and disjoint prime supports remain open.

## 6. Why the standard arithmetic closures stop

### 6.1 Discriminant and Hensel coordinate

The monic reverse-Bessel polynomial



$$
A_N(X)=\sum_{k=0}^N{(2N-k)!\over k!(N-k)!}X^k           \tag{6.1}
$$



satisfies



$$
q_N=A_N(-1),\qquad
2A_N'(X)=A_N(X)-XA_{N-1}(X).                            \tag{6.2}
$$



Its discriminant is



$$
\operatorname{Disc}(A_N)
=(-1)^{N(N-1)/2}(2N-1)!!
\prod_{k=1}^{N-1}\left({(2k)!\over k!}\right)^2.       \tag{6.3}
$$



Hence every prime $p>2N+1$ is absent from the discriminant.  More
directly, if $p\mid q_N$, then



$$
2A_N'(-1)=q_N+q_{N-1}\not\equiv0\pmod p                \tag{6.4}
$$



because adjacent denominators are coprime.  Nevertheless, writing



$$
\lambda_{p,N}=q_N/p\pmod p,
$$



the unique Hensel lift of $-1\pmod p$ has digit



$$
t_{p,N}\equiv-2\lambda_{p,N}q_{N-1}^{-1}\pmod p,       \tag{6.5}
$$



and



$$
p^2\mid q_N\iff t_{p,N}=0.                              \tag{6.6}
$$



Thus separability and the discriminant identify a unique lift but do not
control the divided value deciding whether the distinguished integer
$-1$ is that lift.

### 6.2 Block resultants and subresultants

Let



$$
Q_N=\prod_{n=N}^{2N-1}q_n.
$$



The product bounds (3.2) imply



$$
\boxed{\log Q_N={3\over2}N^2\log N+O(N^2).}             \tag{6.7}
$$



The unpolluted resultant



$$
\operatorname{Res}_Y\!\left(Y,
 \prod_{n=N}^{2N-1}(Y-q_n)\right)=\pm Q_N              \tag{6.8}
$$



is the first standard block invariant which necessarily records every
singleton valuation.  It already pays the full product height (6.7).
Interpolation on the integer grid adds an extra $N^2\log N$, and
discriminants see collisions rather than isolated depth.  When a prime
$p>N$ divides exactly one block value, the resultant records
$v_p(q_n)$, while the first nonzero degree-one subresultant is a
$p$-unit.  Descending the subresultant chain therefore deletes precisely
the singleton datum sought.

### 6.3 Primitive divisors and large prime factors

A theorem asserting that $q_N$ has a primitive divisor, many distinct
divisors across an initial segment, or one large prime factor is a lower
bound on support.  Equation (1.4) is an upper bound on the total
multiplicity of all repeated primes.  The former statement is compatible
with the remaining cofactor carrying essentially all of $\log q_N$ on
squarefull support.  Therefore primitive-divisor and largest-prime-factor
results do not imply (1.4) without an additional upper bound for that
cofactor.  This is a logical non-implication, not a claim that such results
are false for the Bessel sequence.

## 7. The exact missing theorem and booking decision

For fixed $C>0$, a sufficient block theorem is



$$
\sum_{n=N}^{2N-1}\mathcal E_{CN\log N}^{\mathrm{high}}(n)
=o(N^2\log N).                                          \tag{7.1}
$$



A stronger sufficient termwise theorem is



$$
\log\operatorname{sqfull}(q_N)=o(N\log N).              \tag{7.2}
$$



Equivalently, one may prove a uniform prime-power height bound



$$
\max_{\substack{N\le n<2N\\p\le CN\log N}}
v_p(q_n)\log p=o(N\log N),                              \tag{7.3}
$$



together with control of primes beyond the cutoff if the full, rather
than matching-smooth, squarefull part is claimed.  A polynomial bound
$p^{v_p(q_n)}\le(2N)^A$ on the matching range would be more than enough
for the smooth high-singleton aggregate.

Current inputs prove (4.6) but none of (7.1)--(7.3).  The only uniform
substitute is (1.5), whose saddle rate is $\theta$.  It is not below a
positive-linear threshold and cannot be used to shrink the optimistic
two-copy reservoir ceiling



$$
0.1365141682948128\ldots+1
=1.1365141682948128\ldots                               \tag{7.4}
$$



or to resolve its remaining gap



$$
G=0.01963298366943179388\ldots.                         \tag{7.5}
$$



Moreover, any squarefull mass supported on $D_m$ overlaps the two-copy
term already admitted in (2.7) and must be removed through (2.8), not added
again.  The positive-linear-capacity admission test therefore fails.

## 8. Exact replay and strict labels

The standard-library checker accompanying this report performs no search
for isolated exceptional primes.  It checks:

1. the fixed-seed recurrence, oddness, adjacent coprimality, companion
   Wronskian, and both product bounds through a bounded range;
2. the reverse-Bessel specialization and derivative identity exactly as
   polynomial identities in a bounded range;
3. the transfer identity and gcd identity (5.6) on a bounded rectangle;
4. the primewise reservoir ceiling, sequential valuation law, and
   overlap-normalized divisibility (2.9) on a bounded exponent box;
5. the exact valuation inequalities behind (1.3).

Every bounded count in its JSON output is labelled **EXACT FINITE ONLY**.
The general claims in this report are proved algebraically or inherited
from the sealed dependencies listed below; no finite nonoccurrence is used
as an all-prime theorem.

### PROVED

- The exact normalization (2.1)--(2.10), including the overlap quotient.
- The excess/squarefull equivalence (1.3)--(1.4).
- The height asymptotic (3.4) and the main-scale ceiling (1.5).
- The averaged low-level theorem (4.3)--(4.6).
- The singleton decomposition and pairwise-gcd blind spot (5.1)--(5.6).
- The sharply scoped discriminant, resultant/subresultant, average-gcd,
  and primitive-support barriers in Sections 5--6.

### EXACT FINITE ONLY

- The bounded independent replay described above.  It verifies identities;
  it does not scan for or infer a distribution of square divisors.

### OPEN

- The termwise estimate (7.2).
- The average high-singleton estimate (7.1).
- Any uniform prime-power height estimate strong enough for (7.3).
- The actual moving correlation between $b_m$, $q_N$, and the
  transverse factor $g_{m,N}$.
- Route 1 and every conclusion about $e+\pi$.

### BOOKING

No new Route-1 logarithmic rate and no new capacity reduction are booked.

## 9. Portable artifacts and frozen dependencies

The sealed package consists of

```text
sources/item265_beta_squarefull_capacity_report.md
scripts/item265_beta_squarefull_capacity_certificate.py
results/item265_beta_squarefull_capacity_certificate.json
results/item265_beta_squarefull_capacity_certificate_replay.json
results/item265_beta_squarefull_capacity_ledger.json
manifests/item265_beta_squarefull_capacity_manifest.json
results/item265_beta_squarefull_capacity_hashes.sha256
```

The principal frozen dependencies are the sequential matching audit, the
two-index matching theorem, the zero-gap smooth-radical theorem, the
prime-square branching theorem, the high-tail singleton decomposition, the
block-resultant dichotomy, and the reverse-Bessel discriminant report.
