> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 162 extended Hasse census: independent cross-audit

## Verdict

**PASS, with one search-scope caveat.** The stored `m <= 100` census is
byte-for-byte reproducible, its row counts reconstruct independently from the
two archived row sources, and every stored lifted digit agrees with the frozen
`U_m` digit.  The affine searches are correctly labelled finite/experimental;
they do not prove a prime ray.

## Pinned artifacts and replay

- script SHA-256:
  `583734adcf32ee945725c1da6ae4277b0a51a7aecace0672a5d8116b53952902`
- stored census SHA-256:
  `4277b4835e488f68894a7f42ea867e648d2a3d429c4a81eaa319fa41f439ece2`
- independent replay SHA-256:
  `4277b4835e488f68894a7f42ea867e648d2a3d429c4a81eaa319fa41f439ece2`
- stored and replayed lengths: 475,149 bytes; direct byte comparison: equal.
- the 16 fast/slow local-series spot checks all pass during replay.

The three input hashes embedded in the JSON equal the files currently in the
archive: item-161 Hasse script
`0408acbd448b81a00092ece49c4aa6513fc815c1ecd0bf72df882ea060001c65`,
exact scan
`7284ea76cef084e7cb0faeba172454ebe2825a9dd60682c7d1b91c3f78852e96`,
and rank-two certificate
`1fbc73c50ca83cdbbabef090460a944218dc1074a573b32555e4a009f2cb1b02`.

The fast recurrence implements



$$
(AB)F'=(N A'B-KAB')F,\qquad F=A^N/B^K,
$$



and its precision ledger starts with the conservative reserve
`v_p((K-1)!)`, subtracting exactly `v_p(n+1)` at each staged division.  I found
no discrepancy in the coefficient recurrence or its modular divisions.

## Independently reconstructed counts

Reconstructing the eligible rows directly from the rank-one inequalities and
the archived rank-two-zero list gives 928 rank-one rows plus 120 rank-two-zero
rows, with zero overlap and hence 1,048 unique `(m,p)` pairs.  All 1,048 rows
also satisfy `q=p^e`, `0 <= eta < p`, and `eta=expected_eta`.

- `eta=0`: 260; `eta!=0`: 788.
- source totals: rank one 928, rank two zero 120.
- delta totals: delta 0 is 753, delta 1 is 295.
- exponent totals: `e=1,2,3,4,5` are respectively
  `784,156,54,34,20`.
- zero totals by source: rank one 203, rank two zero 57.
- zero totals by delta: delta 0 is 236, delta 1 is 24.
- zero totals by exponent `e=1,2,3,4,5` are respectively
  `58,108,42,33,19`.
- deleting the lower Hasse bands changes the digit on 734 rows.
- duplicate `(m,p)` pairs: 0; frozen-`U_m` mismatches: 0.

The full zero breakdown `(source,delta,e): count` is

```text
rank_one,0,1: 35       rank_two_zero,0,1: 8
rank_one,0,2: 77       rank_two_zero,0,2: 22
rank_one,0,3: 31       rank_two_zero,0,3: 11
rank_one,0,4: 20       rank_two_zero,0,4: 13
rank_one,0,5: 19       rank_two_zero,1,2: 3
rank_one,1,1: 15
rank_one,1,2: 6
```

## Affine-search audit

The fixed-prime affine-digit test examines 56 groups: 55 fail and one passes.
The sole passing sample is the constant-zero group
`source=rank_one, p=19, e=1, delta=0, m mod 19=17`, with the four sampled
quotients `m//19=0,1,2,3`.  This is only a finite fixed-prime observation.

An independent reimplementation of the bounded line enumeration
(`denominator <= 12`, reduced positive slope below 2) reproduces:

- 104 all-zero finite-sample lines with at least four stored points; none has
  two zero points with `p >= 29`;
- exactly six lines with at least two zero points having `p >= 29`;
- zero such lines without *some* nonzero counterexample in the full census.

| line | large zero points | all counterexamples | counterexamples with `p>=29` |
|---|---:|---:|---:|
| `p=m+8` | 2 | 12 | 12 |
| `2p=3m-1` | 2 | 12 | 10 |
| `5p=3m+182` | 2 | 1 | 1 |
| `6p=m+90` | 2 | 1 | 0 |
| `8p=7m+101` | 2 | 1 | 1 |
| `9p=10m+1` | 2 | 3 | 3 |

**Scope caveat.** For `6p=m+90`, the only stored counterexample is the small
point `(m,p)=(12,17)`; the two `p>=29` points `(84,29)` and `(96,31)` both
vanish.  Moreover these three points cross distinct branches: the
counterexample is rank-one/delta-one, while the two zeros are respectively
rank-one/delta-zero and rank-two-zero/delta-zero.  Thus the JSON's literal
count `such_lines_without_a_nonzero_counterexample=0` is correct, but it should
not be paraphrased as saying every line has a large-prime, same-branch
counterexample.  No refined family follows from these two points.

All affine conclusions above remain **EXPERIMENTAL, EXACT FINITE ONLY**.
