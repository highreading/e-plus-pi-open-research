> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Gauged divisor tuning as exact even-grid quantization

Author result, 2026-10-02. This isolates the complete error and primitive content of a high-jet tuning operation. The tuning principle overlaps the arithmetic agent's earlier ordinary Taylor single-jet construction; the new object here is the full exponential-gauged derangement denominator and its exact remaining grid content.

## Fresh target gate

The archive was searched for gauged divisor tuning, derangement/single-jet tuning, quantized endpoints and nearest even numerators. Prior single-jet Taylor tuning, M11's fixed-polynomial gauged interface and M16–M18's common-cell examples are credited. No completed gauged grid/content identity was found. Fresh primary-paper searches opened Miska's *Arithmetic properties of the sequence of derangements and its generalizations*, arXiv:1508.01987v1, including its discussion of divisors and normalized derangements. These known divisor facts do not provide the favorable divisor size or small residue needed below.

Primary source: https://arxiv.org/html/1508.01987 .

## Exact identity, including the remaining primitive gcd

Fix an endpoint polynomial P0 with integral jets and G0=F(P0), and take even N. Let B=B_N(P0), D=D_N, so B is even and D is odd. For any positive odd divisor H of D, choose the centered integer

    K = -B/2 modH,  |K|<=H/2,
    P_N=P0+K z^N(1-z)/N!.

All earlier G-jets are unchanged, while g_N changes by2K because F'(0)=2. The complete endpoint changes exactly by

    B_N(P_N)=B+2K,  c_N(P_N)=c_N(P0)+2K/D.

Set A=B/2, m=(A+K)/H and Q=D/H. Then

    c_N(P_N)=2m/Q,
    q_N(P_N)=Q/gcd(Q,m).

The centered choice makes 2m/Q the nearest rational to c_N(P0) on the even-numerator grid of denominator Q (grid spacing2/Q). Thus the procedure is a precise rational quantization operation. It forces H into the actual gcd, but may lose unrelated old gcd factors: q_new<=D/H does not imply q_new<=q_old/H.

For S=e+pi and E0=c_N(P0)-S the full primitive residual is exactly

    q_new |c_N(P_N)-S|
      = |Q E0 + 2K/H| / gcd(Q,m).

This displays both the signed cancellation and the remaining primitive content. The bound |2K/H|<=1 gives only a bounded grid residual; it does not imply a residual tending to zero. Nor does the fixed-P three-even-index nonvanishing theorem apply to an independently changed P_N at every N.

## Analytic radius and coefficient support cost

For the concrete P81 baseline, on |z|<=2 the baseline puncture-distance exceeds401^-81. The sufficient exact condition

    3 |K| 2^N 401^81 < N!

preserves omission of both punctures and hence analytic radius above two, as well as all endpoint and integral-jet constraints. This makes many moderate divisor targets cheap analytically. It supplies no infinite sequence of favorable divisors near the factorial scale D/R^N, and no small centered residue K/H.

The ordinary coefficients of the new high jet include N! denominators. Consequently, a prime formerly good for P81 can become a bad coefficient prime for P_N. This is how the operation can cancel a factor prohibited by the old fixed-good-prime carry law; it does not contradict that law.

## New exact examples

| N | H | Centered K | H coprime to old coefficient denominator | H coprime to new coefficient denominator |
|---:|---:|---:|:---:|:---:|
| 160 | 159 | 33 | No | No |
| 180 | 179 | 1 | Yes | No |
| 200 | 199 | 1 | Yes | No |
| 320 | 319 | 87 | No | No |
| 322 | 163 | 31 | Yes | No |

Fresh original jet recurrences and complete endpoint convolutions verify the2K shift, exact gcd/grid formula and strict integer radius bound for every row. Full old/new primitive denominators, remaining grid content and coefficient support are saved in the receipt. In the prime rows N=p+1 with p previously good, the old carry gives B_N=-2 modp, so the one-unit K=1 perturbation cancels that prime in the endpoint; the new polynomial is outside the old good-prime premise.

## Remaining research questions

This reduction turns favorable divisor tuning into explicit questions about the divisors of D_N, the residues of B_N/2 modulo those divisors, and the remaining gcd(Q,m). Large forced H alone is insufficient: the complete residual above must tend to zero and remain nonzero. Replacing these questions by an assumed small residue would restate the desired approximation, rather than prove it. The main rationality problem remains open.
