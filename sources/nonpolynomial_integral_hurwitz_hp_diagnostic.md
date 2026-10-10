> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact diagonal HP diagnostic for the non-polynomial pullback

## Scope

This note records a finite exact type-I Hermite--Padé computation for the
entire endpoint-fixing pullback $\phi$ proved in
sources/nonpolynomial_integral_hurwitz_pullback.md, with



$$
G(z)=4\arctan\frac{\phi(z)}{2-\phi(z)}.
$$



The calculation covers the diagonal degrees $1\leq n\leq15$. It is a
diagnostic only: it proves no all-degree rank, nonvanishing, content, height,
or asymptotic statement, and it proves nothing about the algebraic nature of
$e+\pi$.

## Independent exact jet generation

The script first constructs $\phi^{(j)}(0)$ through $j=46$ directly from
the all-order integer formula. For an exponential summand



$$
\frac{k}{m!}z^m(z-1)e^{az},
$$



the contribution is $-k$ at order $m$, and at order $j=m+r$, $r\geq1$,
it is



$$
k\binom{j}{m}\left(r a^{r-1}-a^r\right).
$$



It then constructs the $G$-jets by two separate exact rational routes:

1. generate the ordinary Taylor series of $F(w)=4\arctan(w/(2-w))$ from
   $(2-2w+w^2)F'(w)=4$, then compose that series with $\phi$;
2. independently solve the coefficient recurrence in

   

$$
\bigl(\phi^2-2\phi+2\bigr)G'=4\phi'.
$$



The two complete integer vectors agree byte-for-byte. Their SHA-256 hashes
are



$$
\begin{aligned}
\operatorname{SHA256}(\phi^{(0)},\ldots,\phi^{(46)})
  &={\tt c370b3107e2e11f0124a9b778567a662ffbeb72543be2c3aacba0a3e64f0dc1d},\\
\operatorname{SHA256}(G^{(0)},\ldots,G^{(46)})
  &={\tt db192d18af2ea0ba5f18439f5bbe325a0cc190ad1c31ee614fd87d353ded69b4}.
\end{aligned}
$$



## Exact diagonal records

For each $n$, the endpoint-matched high-order matrix has shape
$(2n+1)\times(2n+2)$. Every matrix below has full row rank and nullity
one. The primitive type-I triple has a nonzero first free coefficient at
order $3n+1$. In the table, “height” is the number of decimal digits in
the largest absolute primitive-triple coordinate, “content” is the number
of digits in the common maximal-cofactor factor, and “decade” is the single
base-10 decade certified by an exact rational enclosure of the endpoint
linear form in $e+\pi$.

| $n$ | rank | nullity | height | content | sign of first free coefficient | endpoint gcd | decade |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1  | 3  | 1 | 1   | 1   | $-$ | 0  | zero |
| 2  | 5  | 1 | 4   | 1   | $-$ | 1  | 0 |
| 3  | 7  | 1 | 12  | 3   | $+$ | 1  | 7 |
| 4  | 9  | 1 | 25  | 4   | $-$ | 2  | 17 |
| 5  | 11 | 1 | 42  | 9   | $+$ | 1  | 29 |
| 6  | 13 | 1 | 63  | 14  | $+$ | 1  | 50 |
| 7  | 15 | 1 | 88  | 22  | $-$ | 1  | 72 |
| 8  | 17 | 1 | 119 | 31  | $-$ | 6  | 99 |
| 9  | 19 | 1 | 157 | 42  | $-$ | 1  | 134 |
| 10 | 21 | 1 | 199 | 55  | $+$ | 3  | 173 |
| 11 | 23 | 1 | 247 | 71  | $-$ | 1  | 217 |
| 12 | 25 | 1 | 301 | 89  | $+$ | 1  | 268 |
| 13 | 27 | 1 | 365 | 105 | $+$ | 21 | 328 |
| 14 | 29 | 1 | 431 | 128 | $-$ | 6  | 391 |
| 15 | 31 | 1 | 509 | 150 | $+$ | 1  | 464 |

The $n=1$ endpoint pair is exactly $(0,0)$. For every
$2\leq n\leq15$, the raw endpoint pair is nonzero and the interval
certificate excludes zero. The positive, rapidly growing endpoint decades
show that this particular diagonal sequence does not presently produce
small linear forms. This is an observation about these fifteen exact
records, not an extrapolation.

## Reproducible artifacts

The exact program is

scripts/nonpolynomial_integral_hurwitz_hp_probe.py

with SHA-256

27574fa09fc8a63231347776fa06f6a17b6fa8aafebec48224d5619ad29066b9.

Its frozen output is

results/nonpolynomial_integral_hurwitz_hp_n15.json

with SHA-256

ab01f6a7a731066f860c6f2f91423f30940b5cf9ecccb785c703fdfa867206fc.

It can be reproduced with

    python scripts/nonpolynomial_integral_hurwitz_hp_probe.py \
      --max-n 15 \
      --output /tmp/nonpolynomial_integral_hurwitz_hp_n15.json

A fresh rerun was byte-identical to the frozen JSON. The JSON stores the
complete exact endpoint pairs and first-free rational coefficients, together
with hashes of the complete primitive kernels and triples and hashes of both
endpoints of every rigorous $e+\pi$ interval evaluation.
