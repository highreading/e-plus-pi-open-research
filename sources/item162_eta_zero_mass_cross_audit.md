> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent cross-audit: eta-zero weighted mass and capacity ceilings

Date: 2026-08-28

## Verdict

**PASS, with no substantive mathematical correction.** The definitions,
normalizations, sufficient conditions, two-layer and four-layer capacity
ceilings, and thin-support no-go statements in
sources/eta_zero_weighted_mass_adversary.md agree with frozen items 149, 151,
160, and 161. The companion checker reproduces its advertised finite census
and constants when pointed at the archived item-161 certificate.

The result is a limitation theorem for what the forced radical and finitely
many lifted digits can certify. It is not an upper bound for the actual
content $c_m$, whose other primes and deeper powers remain uncontrolled.

## 1. Lifted digit and square divisibility

For $p\in\mathcal H_m\cup\mathcal Z_m$, frozen item 160 proves, for
$1\le r\le e_p+1$,



$$
p^r\mid c_m
 \quad\Longleftrightarrow\quad
 v_p(q_pA_m)\ge r+\delta_{m,p},
 \qquad \delta_{m,p}={\bf1}_{p\in\mathcal P_m}.
$$



Since $e_p\ge1$, the case $r=2$ is within this range. Item 161 defines



$$
\eta_{m,p}\equiv {q_pA_m\over p^{1+\delta_{m,p}}}\pmod p.
$$



Therefore, exactly,



$$
\eta_{m,p}=0
 \iff v_p(q_pA_m)\ge2+\delta_{m,p}
 \iff p^2\mid c_m.
$$



This remains correct in the rank-zero branch: the extra power in the
denominator of $\eta$ accounts for the squarefree factor already removed
in $G_m$.

As an independent finite normalization check, I compared all 118 rows of the
pinned item-161 certificate with the archived exact integers $c_m$ for
$m\le30$. There were zero failures of the displayed equivalence and zero
rows with the certificate agreement flag false.

## 2. Disjointness and the eta ledger

For $q_p\ge5$, item 151 identifies the rank-one region with the top-floor
parameter at least one and the genuinely new rank-two region with that
parameter equal to zero. The definition of $\mathcal Z_m$ also excludes
the only $q=3$ exception. Hence



$$
\mathcal H_m\cap\mathcal Z_m=\varnothing.
$$



An independent reconstruction through $m=100$ gave 928 rank-one pairs,
120 rank-two-zero pairs, and zero intersections.  The four other archived
rank-two-zero rows occur only at the separate $m=150,200$ checkpoints.

It follows prime by prime that



$$
\log c_m\ge R_{H,m}+R_{Z,m}+E_{\eta,m}.
$$



If the rank-two contribution is retained only where its lifted digit
vanishes, the still valid weaker bound is



$$
\log c_m\ge R_{H,m}
 +\sum_{p\in\mathcal H_m^0}\log p
 +2\sum_{p\in\mathcal Z_m^0}\log p.
$$



The coefficient two on $\mathcal Z_m^0$ is correct: one copy is the
previously unbooked item-151 radical, and the second is the item-160/161
lift. Nonzero rows in $\mathcal Z_m$ are simply discarded in this weaker
bound.

## 3. Sequential sufficiency

Frozen item 161 gives the exact primewise sequential identity



$$
v_p(c_m\Delta_{m,N}g_{m,N})
 =\kappa_p+d_p+\gamma_p,
$$



with $d_p=\min(v_p(b_m),v_p(q_N))$, and with $\gamma_p$ nonzero only in
the equal-positive-valuation case after division by the full actual $c_m$.
Consequently overlap of a prime among
$c_m,\Delta_{m,N},g_{m,N}$ is legitimate, while computing either later
factor from the raw $V_m$ would be invalid.

At the optimal beta scale the frozen condition is



$$
\liminf {\log(c_m\Delta_{m,N_m}g_{m,N_m})\over6m}>T.
$$



Combining it with the two preceding lower bounds and
$R_{H,m}/(6m)\to r_1$ proves formulas (3.3) and (3.4) of the audited note.
Their strict right-hand side $D=T-r_1$ is correct. In particular, neither
formula double-counts a matching factor; all matching terms are evaluated
only after full primitive normalization.

## 4. Capacity constants and strict inequalities

Using the exact frozen formulas



$$
r_1={-4\log2+6\log3-3\over6},\qquad
 C_2=6-{\pi\over\sqrt3}-3\log3,
$$



and the archived directed interval for $T$, I independently recomputed



$$
r_1+{C_2\over6}
 =0.28490812992172166432045482788211918\ldots .
$$



Thus the full radical plus one extra eta digit has ceiling



$$
2\left(r_1+{C_2\over6}\right)
 =0.56981625984344332864090965576423837\ldots<T,
$$



with gap



$$
T-2\left(r_1+{C_2\over6}\right)
 =0.58633089212080128368982056809289502\ldots .
$$



Likewise four complete surviving digits at every possible rank-at-most-two
forced prime have ceiling



$$
4\left(r_1+{C_2\over6}\right)
 =1.13963251968688665728181931152847674\ldots<T,
$$



and the strict gap exceeds



$$
0.0165146322773579550489109123286.
$$



These margins are many orders of magnitude larger than the archived
interval widths, so the strict signs are rigorous. Five complete digits are
the first count not excluded by this support ceiling. Again, these are
ceilings on the stated certification mechanism, not on actual $c_m$.

## 5. Finite census and thin patterns

The pinned certificate independently yields 45 eta-zero rows: 33 rank-one
and 12 rank-two-zero. Their distinct primes are exactly
$\{3,5,7,11,19,31\}$. The maximum within-index weight occurs at $m=17$,
where the zero primes are $3,5,7,19$ and the rate is
$0.07449411107180356\ldots$ per $6m$. These are finite diagnostics.

The thin-pattern conclusions are elementary and correct:

* a fixed finite prime set has $O(1)$ eta weight;
* support in $p\le m^\alpha$, $\alpha<1$, has
  $O(m^\alpha)=o(m)$ weight by Chebyshev's bound;
* support in $p\le\varepsilon_m m$, $\varepsilon_m\to0$, has $o(m)$
  weight;
* finitely many exact affine rays contribute $O(\log m)$ per index;
* if every selected prime divides one of finitely many fixed nonzero
  polynomials $F_j(m)$, their squarefree product divides
  $\prod_j|F_j(m)|$ away from finitely many zero values, so its logarithm
  is $O(\log m)$.

The conclusions concern a bounded number of certified valuation layers.
They do not exclude large, separately proved valuations at fixed primes.

## 6. Reported affine ray

The separately reported family



$$
p=20k+19,\qquad m=18k+17
$$



is the exact ray $9p=10m+1$. Its symbolic support calculation is valid:
with $r=8k+7$, the item-149 Cartier polynomials are



$$
P_0=x^r(1-x^4)^r,\qquad
 P_1=x^r(1-x)(1-x^4)^{r-1},
$$



while the selected offset is $p-1-r\equiv3\pmod4$. Both Cartier scalars
therefore vanish; $q_p=p$, $\delta_{m,p}=0$, and item 160 gives
$p^2\mid c_m$. Nevertheless this ray supplies only one prime at a fixed
$m$, of weight



$$
\log p=\log((10m+1)/9)=O(\log m).
$$



The stronger congruence slab also remains thin: all its selected primes for
a fixed $m$ divide $10m+1$, so their total logarithmic weight is at most
$\log(10m+1)$.

## 7. Checker audit

Running

    python scripts/eta_zero_mass_adversary_check.py

returned PASS, 118 rows, 45 zeros, the correct $33+12$ source split,
the six-prime support, and the constants displayed above. The pinned
certificate SHA-256 is

    54025499d507749259d7d52a231f5594a77885bf0bf1ee0df747d94d86afde3c

Optional hardening, not a correctness repair: a future version of the
checker could explicitly assert every row's agreement flag, replay
$\eta=0\iff p^2\mid c_m$ from the archived actual $c_m$, and serialize
the four-layer ceiling. Those checks were performed independently in this
audit and all passed.
