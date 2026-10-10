> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Extended factorial-Pascal endpoint scan

## Exact finite diagnostics for $13\le q\le100$

Checked: 2026-08-27 UTC

The frozen factorial-Pascal theorem proves



$$
\log H(C_q^{\rm prim})
 \le 3(\log2)q^2+O(q\log q).
$$



Its deterministic certificate covers $1\le q\le12$.  The companion
extended scan begins at $q=13$, so none of those certified rows is
recomputed.  It uses exact FLINT integer nullspaces for the signed
even-Pascal matrix, exact secant Euler numbers, and the integral endpoint
convolutions from that theorem.  Every completed row is checkpointed to
Google Drive.

The exact scan now contains all 88 rows



$$
13\le q\le100.
$$



For representative orders it records:



$$
\begin{array}{c|ccccc}
q&
\log D_q/q^2&
\log H_{\rm raw}/q^2&
\log K_q/(q\log q)&
\log H_{\rm prim}/q^2&
-\log|r_q-4/\pi^2|/q\\ \hline
13&1.291270&3.331920&2.734079&2.792476&8.941546\\
20&1.260499&2.744632&2.255711&2.406757&8.890484\\
40&1.208561&2.081657&1.616372&1.932592&8.840789\\
60&1.198015&1.832255&1.486124&1.730843&8.823736\\
80&1.201437&1.705132&1.317514&1.632965&8.815118\\
100&1.201433&1.621863&1.295797&1.562189&8.809918
\end{array}
$$



Here $D_q$ is the largest Pascal cofactor, $H_{\rm raw}$ is the
factorially cleared endpoint height before its two-coordinate gcd,
$K_q$ is that gcd, $H_{\rm prim}$ is the primitive height, and
$r_q$ is the resulting positive coefficient ratio.  At $q=100$,
$H_{\rm prim}$ has 22,538 bits while $K_q$ has only 861 bits.
No content collapse occurs anywhere on the declared grid.

As a separate exact diagnostic, the contents at



$$
q=30,50,75,100
$$



were completely factored.  In each case every prime factor is at most
$8q+2$, and the largest prime exponent is at most $5$.  The same
smoothness holds for every $q\le25$ in a separate exact check.
This suggests that $K_q$ may be only exponential in $q$, while the
primitive height remains exponential in $q^2$.  It is not an
all-$q$ support or valuation theorem: an unseen larger order could
contain a new large prime or substantially deeper valuation.

The run uses a 12-GiB per-process failure guard, not a memory allocation
or a limit on the 50-GiB Colab runtime.  Its measured peak was about
1.56 GiB, and about 47 GiB remained available.  Exact integer nullspace
and Euler convolution arithmetic is CPU-bound; the T4 GPU was not useful.

Companion files:

* scripts/centered_cosh_factorial_pascal_extended_scan.py
* results/centered_cosh_factorial_pascal_extended_scan.json

The finite scan does not prove a height lower bound, a content upper
bound, or any classification of $e+\pi$.
