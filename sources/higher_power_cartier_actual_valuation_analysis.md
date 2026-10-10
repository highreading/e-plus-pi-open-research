> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Higher-power Cartier audit for the actual mixed-cubic coordinates

Date: 2026-08-28

## 1. Scope and verdict

This note continues items 149 and 151 using the actual frozen mixed-cubic
coordinates.  It does not modify the Desktop archive.

The outcome has three sharply separated parts.

**PROVED (using the archived item-149/item-151 theorems).**  For every prime
already forced by either the rank-one set $\mathcal H_m$ or the rank-two
zero set $\mathcal Z_m$, a surviving square $p^2\mid c_m$ is equivalent
to one additional digit in the rational coordinate $U_m$.  More exactly,
if $q_p=p^{e_p}$ is the top denominator layer and



$$
\delta_{m,p}=\mathbf 1_{p\in\mathcal P_m},
$$



then



$$
\boxed{p^2\mid c_m
 \quad\Longleftrightarrow\quad
 v_p(q_pA_m)\ge 2+\delta_{m,p}.}                 \tag{1.1}
$$



Thus the non-rank-zero case needs $q_pA_m\equiv0\pmod {p^2}$, while the
rank-zero case, after the already removed factor in $G_m$, needs
$q_pA_m\equiv0\pmod {p^3}$.  This is a one-coordinate reduction, not a
proof that the extra digit occurs.

**EXPERIMENTAL (exact finite diagnostic; not asymptotic).**  On the 928
item-149 forced pairs with
$1\le m\le100$, the valuation distribution of the actual content is



$$
\begin{array}{c|rrrrrrr}
v_p(c_m)&1&2&3&4&5&6&9\\ \hline
\#&725&116&48&21&12&5&1.
\end{array}                                                     \tag{1.2}
$$



Hence 725 of 928 forced pairs are sharp at one digit.  In particular, a
uniform $p^2$-lift theorem on $\mathcal H_m$ is false for the actual
coordinates.  This failure occurs in both normalization branches:



$$
(m,p)=(3,3): (v_p(U_m),v_p(V_m),v_p(c_m))=(1,3,1)
$$



is non-rank-zero, whereas



$$
(m,p)=(9,13): (v_p(U_m),v_p(V_m),v_p(c_m))=(1,2,1)
$$



is rank-zero.  The 120 vanishing rank-two pairs with $m\le100$ likewise
split into 63 sharp pairs and 57 pairs with a square.

**EXPERIMENTAL (exact finite negative tests).**  Two natural candidates were
tested and failed on the frozen grid: equality of the two raw coordinate
valuations, and affine dependence of the normalized next digit on the next
quotient digit of $m$.  **OPEN:** no credible all-parameter higher-lift
pattern is known.  The missing theorem is a genuine mod-$p^2$ (or
Witt/Dwork) lift of the endpoint determinant, not another application of
characteristic-$p$ Cartier proportionality.

## 2. Exact coordinates and what data are available

Use the frozen notation



$$
D_m^\sharp=2^{9m+5}K_m,
 \qquad U_m={D_m^\sharp A_m\over G_m},
 \qquad V_m={D_m^\sharp B_m\over G_m},
 \qquad c_m=\gcd(U_m,V_m).
$$



The integral raw coordinates satisfy



$$
\widehat A_m=2^{9m+4}M_{4m+1}A_m,
 \qquad \widehat B_m=2^{9m+5}B_m,
$$



and the exact local ledger is



$$
\begin{aligned}
v_p(U_m)&=\mathbf1_{p=2}+v_p(\widehat A_m)-v_p(T_m)-v_p(G_m),\\
v_p(V_m)&=v_p(K_m)+v_p(\widehat B_m)-v_p(G_m),\\
v_p(c_m)&=\min\{v_p(U_m),v_p(V_m)\}.                 \tag{2.1}
\end{aligned}
$$



After orientation and primitive reduction,



$$
a_m={\sigma U_m\over c_m},
 \qquad \varepsilon b_m={\sigma V_m\over c_m},
$$



so every primitive-coordinate valuation is also exact:



$$
\boxed{v_p(a_m)=v_p(U_m)-v_p(c_m),\qquad
 v_p(b_m)=v_p(V_m)-v_p(c_m).}                       \tag{2.2}
$$



The frozen $m\le100$ scan serializes the complete integers
$U_m,V_m,c_m,a_m,b_m$.  The isolated $m=150,200$ factor probes serialize
the complete factorization of $c_m$ over the checked range and the local
$(v_p(U_m),v_p(V_m))$ maps, but not the full huge integers $U_m,V_m$.

For beta synchronization,



$$
\Delta_m=\gcd(b_m,q_N),\qquad
 g_m=\gcd(b_0p_N-\varepsilon q_0a_m,\Delta_m),
$$



and therefore



$$
v_p(\Delta_m)=\min\{v_p(b_m),v_p(q_N)\}.              \tag{2.3}
$$



The earlier equal-positive-valuation theorem gives



$$
v_p(g_m)=0\quad(v_p(b_m)\ne v_p(q_N)),                 \tag{2.4}
$$



and, when both valuations equal $r>0$,



$$
v_p(g_m)=\min\{r,v_p(b_0p_N-\varepsilon q_0a_m)\}.     \tag{2.5}
$$



Only two selected $(\Delta_m,g_m)$ records per $m$ are serialized in
the frozen $m\le100$ JSON: the minimum-positive-match record and the
maximum-total-content record.  All other finite $N$ are exactly
recomputable from the serialized $a_m,b_m$ and the beta recurrence, but
their individual ledgers are not stored in that JSON.  The new probe
recomputes all 200 serialized selected records exactly.

## 3. Proof of the one-coordinate higher-lift bridge

Let $p\in\mathcal H_m\cup\mathcal Z_m$.  Both definitions impose
$p<2m$, hence $p\nmid T_m$.  Put $q=q_p=p^{e_p}$ and
$\delta=\delta_{m,p}$.  Since $q$ is the largest $p$-power at most
$4m+1$,



$$
v_p(D_m^\sharp)=e_p,
\qquad D_m^\sharp/q\in\mathbb Z_{(p)}^\times.
$$



The Cartier product is squarefree, so $v_p(G_m)=\delta$.  Consequently



$$
\boxed{
v_p(U_m)=v_p(qA_m)-\delta,
\qquad
v_p(V_m)=e_p+v_p(B_m)-\delta.}                   \tag{3.1}
$$



The item-149 and item-151 divisibility arguments prove, in both the
rank-zero and non-rank-zero branches,



$$
v_p(U_m)\ge1,
\qquad v_p(V_m)\ge e_p+1.                         \tag{3.2}
$$



Because $e_p\ge1$, the second inequality already gives $p^2\mid V_m$.
Thus $p^2\mid\gcd(U_m,V_m)$ if and only if $p^2\mid U_m$.  Substitution
of (3.1) proves (1.1).

More generally, for every $1\le r\le e_p+1$,



$$
\boxed{p^r\mid c_m
\quad\Longleftrightarrow\quad
v_p(q_pA_m)\ge r+\delta_{m,p}.}                   \tag{3.3}
$$



For $r>e_p+1$, one must additionally control the $B_m$-coordinate.
This is the exact point at which the one-coordinate bridge stops.

Equation (3.3) also explains why iterating Cartier to the
prime-power denominator layer does not create prime-power divisibility:
$\mathcal C^{e_p}$ still produces only a congruence modulo $p$.  It
detects the layer $q_p$, not a congruence modulo $q_p$ or $p^2$.

## 4. Exact finite census

The rank-one $m\le100$ census has 291 rank-zero pairs and 637
non-rank-zero pairs.  Their distributions are



$$
\begin{array}{c|rrr}
v_p(c_m)&1&2&3\\ \hline
\text{rank-zero}&270&19&2
\end{array}
$$



and



$$
\begin{array}{c|rrrrrrr}
v_p(c_m)&1&2&3&4&5&6&9\\ \hline
\text{non-rank-zero}&455&97&46&21&12&5&1.
\end{array}
$$



Only seven lifted rank-one pairs in this grid have $p\ge29$:



$$
(m,p)=(21,31),(41,61),(53,31),(53,59),(71,79),(84,29),(99,107).
                                                               \tag{4.1}
$$



This is useful negative information: neither rank-zero membership nor a
large-prime cutoff supplies a universal square.  It is not an asymptotic
sparsity theorem.

For the rank-two determinant-zero set, the $m\le100$ distribution is



$$
\begin{array}{c|rrrrrrr}
v_p(c_m)&1&2&3&4&5&6&7\\ \hline
\#&63&34&8&8&5&1&1.
\end{array}                                                     \tag{4.2}
$$



For example, the proved ray instance $(m,p)=(4,7)$ has
$(v_p(U_m),v_p(V_m))=(1,2)$, so even an exact rank-two determinant zero
does not force a square.

## 5. Pattern searches and their exact failures

### 5.1 Raw equal-valuation candidate

A tempting candidate was



$$
v_p(V_m)-v_p(U_m)=v_p(M_{4m+1}),                         \tag{5.1}
$$



equivalent for odd $p\le4m+1$ to
$v_p(\widehat A_m)=v_p(\widehat B_m)$.  The exact probe tests 4,553
prime-index pairs across the available $m\le100,150,200$ rows and finds
343 failures.  The first is $(m,p)=(4,3)$, where



$$
e_p=2,\qquad (v_p(U_m),v_p(V_m))=(3,4),
$$



so the difference is one, not two.  Candidate (5.1) is refuted, not left as
a conjecture.

### 5.2 A next-digit affine candidate

For a forced rank-one pair define the normalized first unproved digit



$$
\eta_{m,p}\equiv {q_pA_m\over p^{1+\delta_{m,p}}}\pmod p.       \tag{5.2}
$$



By (3.1), it is computed exactly from $U_m/p$ after multiplying by the
known $p$-adic unit $(G_m/p^\delta)/(D_m^\sharp/q_p)$.  Equation (1.1)
is precisely



$$
p^2\mid c_m\quad\Longleftrightarrow\quad\eta_{m,p}=0.           \tag{5.3}
$$



Rows were grouped by the residual labels
$(p,e_p,m\bmod q_p,\delta_{m,p})$, and $\eta_{m,p}$ was tested for
affine dependence on $\lfloor m/q_p\rfloor$ modulo $p$.  Among 51 groups
having at least three points, only one is affine; it is the degenerate
identically-zero group $p=19,m\equiv17\pmod{19}$ on the four available
points.  The other 50 groups fail.  Thus the simplest Hensel-style affine
law is also refuted on the finite exact grid.

The finite data do show many genuine higher powers, especially at small
primes, but they do not isolate a stable all-parameter family that would
add positive logarithmic mass.  Declaring the observed zeros of
$\eta_{m,p}$ to be periodic or Henselian would go beyond the evidence.

## 6. Remaining barrier

The exact next target is now narrow.  One needs a formula for (5.2), or a
mod-$p^2$ relative endpoint theorem, strong enough to prove
$\eta_{m,p}=0$ on a family with positive prime-number-theorem mass.  A
Witt-vector Cartier operator, a Dwork congruence, or an explicit lifted
Hermite endpoint determinant could in principle supply such a formula.

What is not sufficient is:

1. another characteristic-$p$ Cartier iteration;
2. rank-two proportionality modulo $p$ alone;
3. a radical support theorem; or
4. the finite presence of high powers at small primes without a uniform
   valuation-mass estimate.

The current exact data therefore establish a useful reduction and close
two tempting shortcuts, but do not improve the proved asymptotic content
rate from item 149.

## 7. Deterministic replay and provenance

The standard-library script

`scripts/higher_power_cartier_probe.py`

reads and hashes these frozen inputs:

* `mixed_cubic_positive_match_exact_scan_m100_N6m.json` —
  `7284ea76cef084e7cb0faeba172454ebe2825a9dd60682c7d1b91c3f78852e96`;
* `mixed_cubic_content_factor_m150.json` —
  `1c037ffddb890658a74f38e4a855d7a7ea5aac66b9402dba0e29866e402a4749`;
* `mixed_cubic_content_factor_m200.json` —
  `6938230842b2e6b019607da2429a0219bffa28b656d0b4f07c0a9b7954d9247c`;
* `mixed_cubic_rank_two_cartier_certificate.json` —
  `1fbc73c50ca83cdbbabef090460a944218dc1074a573b32555e4a009f2cb1b02`.

It verifies every stored integer digest and gcd, independently recomputes
the Hermite coordinates for $1\le m\le12$, closes every displayed content
factorization over primes at most $6m$, reconstructs the 928 rank-one
rows, reads the 124 archived rank-two rows, and recomputes all 200 serialized
selected $(\Delta_m,g_m)$ records.  The output is

`results/higher_power_cartier_probe_m100_150_200.json`.

All computations are exact integer or rational arithmetic.  The census and
counterexamples are exact finite certified statements about the frozen rows;
the uniform bridge (3.3) is hand algebra from the archived theorems; no finite
scan is used to infer an asymptotic statement.

## 8. Archive-worthiness

This package is archive-worthy as a negative higher-power audit and as an
exact one-coordinate reduction.  It should not be described as a new
prime-power divisor theorem or as an improvement in asymptotic content
mass.  If archived, its checkpoint wording should say that the naive
uniform $p^2$ lift is refuted and that the remaining object is the lifted
digit $\eta_{m,p}$ in (5.2).
