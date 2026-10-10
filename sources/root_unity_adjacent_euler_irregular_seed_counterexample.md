> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A genuine interior adjacent Euler-irregular seed

## Exact counterexample to branch incompatibility and index amplification

Checked: 2026-08-27 UTC

## 1. Scope and theorem

Let the secant Euler numbers be defined by



$$
\operatorname {sech}z
       =\sum_{j\geq0}E_j\frac {z^j}{j!}.                    \tag{1}
$$



In the notation of the quadratic Euler-gcd Kummer decomposition, put



$$
\begin{aligned}
 H_N&=\gcd(|E_{2N}|,|E_{2N+2}|),\\
 S_N&=\prod_{q\ {\rm odd\ prime}}
 q^{\min(v_q(H_N),a_q(N))},\\
 J_N&=H_N/S_N,                                               \tag{2}
 \end{aligned}
$$



where



$$
a_q(N)=\max\{a\geq1:\ \varphi(q^a)\leq2N+2\},              \tag{3}
$$



with value zero if the set is empty.

The following is an exact finite theorem.

**Theorem 1.1.**  The integer



$$
p=151483                            \tag{4}
$$



is prime, and



$$
\boxed{\gcd(E_{3286},E_{3288})=151483.}                    \tag{5}
$$



Moreover,



$$
v_p(E_{3286})=v_p(E_{3288})=1,                             \tag{6}
$$



and the complete set of ordinary $E$-irregular indices for $p$ is



$$
\boxed{\{r:\ 2\leq r\leq p-3,\ r\ {\rm even},\
                    p\mid E_r\}=\{3286,3288\}.}             \tag{7}
$$



Thus $i_E(p)=2$, the smallest total irregularity index compatible with
an adjacent pair.

At $N=1643$,



$$
p-1=151482>3288=2N+2,                                     \tag{8}
$$



so $a_p(N)=0$.  Equations (5)--(8) give



$$
\boxed{H_{1643}=J_{1643}=151483,
                    \qquad S_{1643}=1.}                     \tag{9}
$$



For the closer-root primitive-content gcd



$$
G_N=\gcd((2N+2)(2N+1)|E_{2N}|,|E_{2N+2}|),                \tag{10}
$$



the exact value is also



$$
G_{1643}=151483.                    \tag{11}
$$



This supplements and validates the earlier $S_N,J_N$ decomposition; it
does not alter that theorem.  It proves that $J_N$ is genuinely
nontrivial.  It also rules out two proposed shortcuts:

1. neighboring Kummer branches are not universally incompatible; and
2. an adjacent pair need not force a large $E$-irregularity index.

The theorem gives no asymptotic upper bound for $J_N$.  One isolated
squarefree seed neither proves nor disproves $\log J_N=O(N)$ or
$\log J_N=o(N\log N)$.  Nothing here classifies $e+\pi$.

## 2. Three exact verification routes

The deterministic replay uses three different exact representations.

First, FLINT computes the two integer Euler numbers and their integer gcd.
The numbers have respectively 9487 and 9494 decimal digits; the JSON stores
their signs, lengths, and SHA-256 digests rather than printing them.  Trial
division through $\lfloor\sqrt p\rfloor=389$ proves that (4) is prime.

Second, the defining recurrence



$$
E_0=1,\qquad
 E_{2n}=-\sum_{j=0}^{n-1}\binom {2n}{2j}E_{2j}             \tag{12}
$$



is evaluated independently modulo $p^2$.  In least nonnegative
residues it gives



$$
\begin{aligned}
 E_{3286}&\equiv 6825521014\pmod {p^2},\\
 E_{3288}&\equiv 7214529358\pmod {p^2}.                    \tag{13}
 \end{aligned}
$$



Both residues are zero modulo $p$, and neither is zero modulo $p^2$,
which proves (6).  The exact-integer and modular-recurrence residues are
checked against one another.

Third, the complete first-period claim (7) is checked in one polynomial
identity over $\mathbb F_p$.  Define



$$
C_p(X)=\sum_{0\leq 2j\leq p-3}\frac {X^{2j}}{(2j)!}
       \in\mathbb F_p[X]                                   \tag{14}
$$



and let



$$
S_p(X)=C_p(X)^{-1}\pmod {X^{p-1}}.                         \tag{15}
$$



All factorials below $p$ are units.  Therefore the formal identity



$$
\cosh X\,\operatorname {sech}X=1  \tag{16}
$$



implies, coefficient by coefficient,



$$
[X^r]S_p(X)=\frac {E_r}{r!}\pmod p,
             \qquad 0\leq r\leq p-2.                       \tag{17}
$$



The replay verifies $C_pS_p\equiv1\pmod {X^{p-1}}$, verifies that all
odd coefficients vanish, and scans every even coefficient in the range.
Exactly the coefficients at 3286 and 3288 vanish.  Thus (7) is not inferred
from a partial factorization table.

As independent public corroboration, the Euler-number factor table at
<https://www.bernoulli.org/download/en_factors.txt> lists



$$
\begin{array}{c|l}
 3286&19,151483,\ldots\\
 3288&5,13,43,1097,1663,151483,\ldots
 \end{array}                                                 \tag{18}
$$



The replay itself is network-independent and does not use this table.

## 3. Why this is exactly a $J_N$ seed

At $N=1643$, the Kummer cutoff in (3) is $2N+2=3288$.  Since
$\varphi(p)=p-1=151482$, not even the first $p$-period fits under that
cutoff.  Thus the $p$-layer in (5) cannot be placed in $S_N$; it lies in
$J_N$.  Because the exact gcd (5) has no other factor, (9) follows.

This contrasts with the previously observed factors 149 and 241.  Their
adjacent zeros occur at the Kummer boundary and every recurrence in the
$N$-grid is absorbed by $S_N$.  The pair (7) is instead strictly
interior:



$$
2\leq3286<3288\leq p-3.                   \tag{19}
$$



The replay computes every $H_N,S_N,J_N$ exactly for
$1\leq N\leq1643$.  Within this declared finite range the only row with
$J_N>1$ is (9).  This is a finite certificate, not an assertion about all
larger $N$.

## 4. Consequences for proposed $J_N$ arguments

### 4.1 Qualitative branch incompatibility is false

The two values in (7) occupy different neighboring residue branches of
the $p$-adic Dirichlet $L$-function attached to the mod-$4$
character.  Their simultaneous vanishing proves that there is no
unconditional rule saying two neighboring branches cannot both be
irregular.

### 4.2 Adjacency need not amplify total irregularity

The complete scan (7) gives $i_E(p)=2$, not merely $i_E(p)\geq2$.
Hence an implication of the form



$$
\text{adjacent pair}\quad\Longrightarrow\quad
 i_E(p)\text{ is large}                                    \tag{20}
$$



is false without additional hypotheses.  General upper bounds for the
total index of $\chi$-irregularity therefore do not control this seed by
such an amplification mechanism.

### 4.3 One-branch lifting still does not bound the product

Kummer congruences propagate each irregular branch through its own
prime-power periods.  They do not bound the number or size of distinct
interior adjacent seeds, nor do they couple the valuations of the two
branches.  This example has valuation one in each branch, so it does not
settle the harder question of simultaneous higher-power layers.

Consequently the exact obstruction from the earlier note remains:



$$
\log G_N=\log J_N+O(N),                                   \tag{21}
$$



and a useful primitive-height theorem still requires a genuinely
quantitative all-$N$ estimate for $J_N$.

## 5. Literature audit and limits of the claim

A focused primary-literature search found the following relevant tools.

1. R. Ernvall and T. Metsänkylä, *Cyclotomic invariants and
   $E$-irregular primes*, Math. Comp. 32 (1978), 617--629,
   <https://doi.org/10.1090/S0025-5718-1978-0482273-9>, develops the
   $E$-irregularity and cyclotomic-invariant framework and reports the
   early finite census.

2. R. Ernvall, *An upper bound for the index of
   $\chi$-irregularity*, Mathematika 32 (1985), 39--44,
   <https://doi.org/10.1112/S0025579300010834>, bounds a total
   irregularity index.  Such a total-index result does not forbid the
   index-two configuration (7).

3. J. B. Cosgrave and K. Dilcher, *On a congruence of Emma Lehmer related
   to Euler numbers*, Acta Arith. 161 (2013), 47--67,
   <https://www.impan.pl/shop/publication/transaction/download/product/82378>,
   gives the prime-power Euler Kummer congruence used in the decomposition
   of $H_N$.

4. R. J. McIntosh, *Congruences involving Euler numbers and power sums*,
   Fibonacci Quart. 58 (2020), 328--333,
   <https://www.fq.math.ca/Papers/58-4/mcintosh04112020.pdf>, gives a
   first-period power-sum test for individual $E$-irregular pairs.

These sources provide periodicity, individual tests, or total-index
information.  No theorem located in this search supplies the required
uniform product bound for simultaneous adjacent first-period layers.  That
last sentence is a literature-audit report, not a proof that no such result
exists anywhere.

## 6. Replay and logical scope

From the research directory run

    python3 scripts/root_unity_adjacent_euler_irregular_seed_certificate.py
    sha256sum -c results/root_unity_adjacent_euler_irregular_seed_hashes.sha256

The JSON is deterministic.  Timing and peak RSS are printed but omitted
from the JSON.  The exact $N\leq1643$ scan and the complete
$p=151483$ first-period inversion are finite computations only.  The
package proves a concrete obstruction, not an asymptotic estimate and not
a classification of $e+\pi$.
