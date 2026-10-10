> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual mixed-cubic positive matches: exact finite certificate

Date: 2026-08-28

## 1. Scope and theorem boundary

This package evaluates the actual item-133 mixed-cubic coordinates, not an
arithmetic countermodel.  It proves the following finite statement by exact
rational arithmetic:

> For every $1\le m\le100$ and every parity-compatible beta index
> $1\le N\le6m$, the canonical positive matched form defined below has an
> exact lower bound greater than $1$.

There are 15,150 candidates in this scope.  The assertion does not cover
$m>100$, $N>6m$, a different mixed-cubic ray, or any asymptotic limit.  In
particular, it does **not** prove that $e+\pi$ is rational, irrational, or
transcendental.

## 2. Exact construction

Put $n=6m$, $k=4m+1$, and use the item-133 logarithm-cancelled form



$$
U_m+V_m\pi.
$$



The self-contained generator recomputes the two period coordinates by exact
Hermite reduction, applies the frozen sharp clearing and Cartier product, and
sets



$$
c_m=\gcd(U_m,V_m).
$$



Exact rational Machin bounds for



$$
\pi=16\arctan(1/5)-4\arctan(1/239)
$$



orient the primitive form as



$$
L_m=a_m+\varepsilon_m b_m\pi>0,
 \qquad \gcd(a_m,b_m)=1,quad b_m>0.
$$



No floating-point sign decision enters the certificate.

For the beta form, start with



$$
(p_0,q_0)=(1,1),\qquad (p_1,q_1)=(3,1),
$$



and apply, componentwise,



$$
x_N=(4N-2)x_{N-1}+x_{N-2}.
$$



Then



$$
E_N=(-1)^N(q_Ne-p_N)>0,
 \qquad E_N\ge\frac{N!}{(2N+1)!}.
$$



Choose the parity $(-1)^N=\varepsilon_m$, and define



$$
\Delta=\gcd(b_m,q_N),\qquad b_m=\Delta b_0,
 \qquad q_N=\Delta q_0,
$$





$$
P^*=b_0p_N-\varepsilon_m q_0a_m,
 \qquad g=\gcd(P^*,\Delta).
$$



The primitive positive match is exactly



$$
\Omega_{m,N}
 =\frac{b_0E_N+q_0L_m}{g}>0.
$$



If $L_m^-$ is the exact lower endpoint obtained from the Machin interval,
then



$$
\boxed{
 \Omega_{m,N}\ge
 \frac{b_0N!/(2N+1)!+q_0L_m^-}{g}.}
$$



The right side is a canonical rational number.  The generator enumerates
every admissible $N$ in the finite scope, hashes the complete fraction
transcript for each $m$, records the smallest certified lower bound, and
stores its raw numerator and denominator.

## 3. Exact result and independent replay

The final generator and result hashes are

```text
fc1888eb7a123c7efd177d25e85686765e720fb1538f2eb95e4cf098640eafa5  scripts/mixed_cubic_positive_match_exact_scan.py
7284ea76cef084e7cb0faeba172454ebe2825a9dd60682c7d1b91c3f78852e96  results/mixed_cubic_positive_match_exact_scan_m100_N6m.json
```

An independent end-to-end regeneration produced the result byte for byte.
The separate verifier checks the pinned sources, exact scope, row coverage,
parity, candidate counts, canonical fractions, digit counts, fraction hashes,
and the raw inequalities numerator $>$ denominator $>0$.  Its aggregate
minimum-witness stream is

```text
601bca1946a45d36026a8c168613d578427f6b6bd4f99709286723f64c674b8c
```

The stored row minimum is a replay-based certificate: exhaustiveness over all
candidates follows from the independently replayed deterministic generator.
Without that replay, a standalone certificate would need all 15,150 raw
candidate fractions rather than one minimum per row.

## 4. Finite support diagnostics

The same exact coordinates give additional finite observations.

- For every $1\le m\le100$, trial division removes all of $c_m$ using
  primes at most $6m$.
- Independent exact probes at $m=150$ and $m=200$ also leave cofactor
  one after primes at most $6m$ are removed.
- The corresponding content rates are
  $0.172286833139\ldots$ and $0.164995723146\ldots$.
- Among $m\ge80$ in the $N\le6m$ scan, the largest observed total-content
  rate is $0.257894809399\ldots$, at $(m,N)=(100,141)$.

These statements are exact for their listed indices only.  They neither prove
the support conjecture



$$
p\mid c_m\Longrightarrow p\le6m
$$



nor give the exponential lower bound



$$
\liminf\frac1{6m}\log(c_m\Delta_mg_m)
 >h-d/2=1.156147151964\ldots
$$



required by item 137.  Indeed, the finite positive matches being greater than
one show that the canonical integer-contradiction mechanism has not crossed
its target anywhere in the certified window.

## 5. Reproduction

The package consists of the self-contained generator, its independent
structural verifier, the exact JSON result, and two finite support probes.  The
authoritative hashes are collected in
`results/mixed_cubic_actual_positive_match_finite_hashes.sha256`.
