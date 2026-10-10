> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 164 — exact finite third-layer census through $m=250$

Date: 2026-08-29

## Scope and status

This is an exact, deterministic finite census of the $e=1$ forced rows
through $m=250$.  It reuses two proved ingredients:

1. the item-162 local Hasse recurrence for $(pR_s,L_s,E_s)$; and
2. the item-163 scalar-free two-minor gate for the third content layer.

It makes **no density, positive-mass, or asymptotic claim**.  All congruence
patterns below are finite observations unless explicitly identified as an
externally supplied proved condition.

For $D=1+\delta$, write



$$
\frac{\mathscr A}{p^D}=a_0+a_1p+\cdots,
 \qquad
 \frac{\mathscr B}{p^D}=b_0+b_1p+\cdots.
$$



The exact gates used here are



$$
p^2\mid c_m\iff a_0=0,
 \qquad
 p^3\mid c_m\iff a_0=a_1=b_0=0.
$$



The computation first obtains $a_0$ on every forced row and performs the
more expensive precision lift only on the $a_0=0$ rows.

## Exact census

| source and $\delta$ | forced rows | $p^2$ candidates | $p^3$ survivors |
|---|---:|---:|---:|
| rank one, $\delta=0$ | 2,649 | 119 | 10 |
| rank one, $\delta=1$ | 1,752 | 62 | 4 |
| rank-two zero, $\delta=0$ | 134 | 15 | 0 |
| **total** | **4,535** | **196** | **14** |

There are 9 new $p^3$ survivors in $101\le m\le250$.  The survivor
multiplicities by prime are



$$
p=17:1,\quad p=19:3,\quad p=23:4,\quad p=29:3,\quad p=31:3.
$$



Thus every observed $p^3$ survivor is rank one and has $p\le31$.  The
census covers the complete $e=1$ range for every prime $p\le31$: for an
odd prime, the upper edge is $m\le(p^2-5)/4$, which is at most 239 for
$p\le31$.  This completeness does not extend to $p\ge37$.

The finite large-prime counts are:

| cutoff | forced rows | $p^2$ candidates | $p^3$ survivors |
|---|---:|---:|---:|
| $p\ge37$ | 4,190 | 51 | 0 |
| $p\ge101$ | 2,731 | 19 | 0 |
| $p\ge251$ | 659 | 6 | 0 |

The largest prime reaching $p^2$ in this census is 331, while the largest
prime reaching $p^3$ is 31.  These are finite facts, not evidence sufficient
for a uniform large-prime theorem.  In particular, the observed absence of
survivors with $p\ge37$ does not conflict with the supplied slab tail: the
next eligible slab prime after 19 is $p=59$, and its first row satisfying
$6\ell+4\ge p$ has $\ell=10$ and $m=53+10\cdot59=643>250$.

## Classification against the supplied slab tail

The structural branch supplied the proved sufficient condition



$$
p=20k+19\text{ prime},\qquad
 m=18k+17+\ell p,\qquad
 4m+1<p^2,\qquad
 6\ell+4\ge p,
$$



which implies $p^3\mid c_m$.  This census does not re-audit that proof; it
uses the displayed condition only as a classifier.

Exactly one row through $m=250$ satisfies the condition:



$$
(m,p,k,\ell)=(74,19,0,3).
$$



It is a $p^3$ survivor.  Therefore the finite classification has **one tail
hit and zero tail misses**.

The 13 survivors outside the supplied tail are:

| prime | outside-tail $m$-values |
|---:|---|
| 17 | 67 |
| 19 | 36, 89 |
| 23 | 100, 101, 102, 103 |
| 29 | 172, 180, 199 |
| 31 | 166, 177, 208 |

## Finite patterns outside the tail

Two repeated patterns occur in the outside-tail set.

1. At $p=23$, the four consecutive values $m=100,101,102,103$ survive.
   This is a finite block, not a proved interval family.
2. At $p=31$, $m=177,208$ both satisfy
   $m\equiv22\pmod{31}$, have $\delta=1$, and survive.  The same forced
   residue class also contains the six non-survivors
   $m=22,53,84,115,146,239$.  Hence the data explicitly rule out the whole
   residue class as a sufficient condition.

If the supplied tail is temporarily put back into the pattern search, the
$p=19$, $m\equiv17\pmod{19}$, $\delta=0$ class has survivors
$m=36,74$, but also non-survivors $m=17,55$.  Again, the full residue
class is not sufficient; $m=74$ is the one member certified by the supplied
tail condition.

No repeated affine class was found among the other outside-tail survivors.
This last statement is only about the finite search domain.

## Reproducibility checks

- All 784 item-163 rows through $m=100$ were reproduced, including
  $(a_0,a_1,b_0)$: 0 mismatches.
- Forced determinant divisibility failures: 0.
- Low/high precision lift mismatches: 0.
- The canonical row fingerprints are stored in the JSON certificate.
- A second complete root replay was required to be byte-identical to the
  canonical JSON.

Pinned inputs and SHA-256 values:

```text
lifted_endpoint_hasse_certificate.py
0408acbd448b81a00092ece49c4aa6513fc815c1ecd0bf72df882ea060001c65

lifted_endpoint_hasse_extended_certificate.py
583734adcf32ee945725c1da6ae4277b0a51a7aecace0672a5d8116b53952902

item163_deeper_digits_certificate.py
549c9f4df81d4dd46617cedc0cfa6aa2d39656754c4e9a096f3168702b42229c

item163_deeper_digits_certificate.json
c3234900f80abb0ff2ee4c96e82d8c19fd5734b58135d16c5090e397dcebc9d1

mixed_cubic_rank_two_cartier_probe_m500.json
a1dbe6bc335720e3ce6130376b2319effee8cb72c89a349e63744b772dc4337e
```

## Open point

The census supplies neither a positive-weighted-mass theorem for the third
layer nor a uniform obstruction to large-prime survivors.  Outside the
proved slab tail, all 13 rows remain isolated finite data requiring a
structural explanation.
