> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit: actual b=1 ternary endpoint denominator

Date: 2026-09-27. Reviewer: audit_sources.
Source: hp_b1_ternary_actual_denominator.md.
Status: FULL PASS. No mathematical correction required.

The accepted theorem is



$$
v_3(q_n)=2v_3(n!)\qquad(n\ge5,\ n\equiv2\pmod3),
$$



where q_n is the reduced denominator of the actual matched endpoint.
The proof controls the rational numerator before reduction; it does
not identify a coefficient clearer with q_n.

## 1. Independent normalization derivation

I checked the endpoint formula against the September 13 adjacent-scalar
source and its review. In both T_n and T_{n+1}, the partial-exponential
index is n+j. This fixed-n convention is essential.

Let c_r=[t^r](t^2-t+1/2)^k. The Rodrigues normalization gives



$$
[t^j]L_k=\frac{2^k c_{k+j}(k+j)!}{k!j!}.
$$



For k=n, multiplying by E_{n+j}=D_{n+j}/(n+j)! and setting j=n-s
leaves 2^n/(n!)^2 times (n)_s a_s(n)D_{2n-s}.
For k=n+1 the remaining ratio is n+1+j. At s=0 it combines with
n!/(n+1)! to give exactly 2; at s>=1 it gives
(n)_{s-1}(2n+2-s). Thus both prefactors in (6) are exact, including
the single n+1 in the second denominator.

Replacing D by 1 gives the two factorial contractions H_n and
K_{n+1}. All A,B,C quantities used modulo 3 lie in Z[1/2].
Substitution in the actual numerator yields exactly
Qpart+2^{n+1} C_n/(n!)^2, with the minus sign in
C_n=K_{n+1}A_n-H_n B_n retained.

## 2. All-index congruences

The recurrence D_d=d D_{d-1}+1 resets to 1 whenever 3 divides d.
Its full residue pattern is therefore (1,2,2).

For n=2 modulo 3, the three surviving weights in the first contraction
are (1,2,1). I independently checked a_2(n)=n^2/2 and the falling
factorials. The remaining weights contain a factor 3. Their D indices
give A_n=0 modulo 3, while H_n=1.

For the second contraction, Frobenius makes a_s(n+1)=0 modulo 3
at s=1,2. The s=3 summand contains the separate multiplier
2n+2-s, divisible by 3. Every s>=4 summand contains a factor 3 in
(n)_{s-1}. Thus B_n=2D_{2n+1}=1 and K_{n+1}=2 modulo 3.
Consequently C_n=2, a unit. This is a uniform proof, with no inferred
pattern from the frozen controls.

## 3. Strict valuation separation and actual reduction

The second-kind formula is an integer convolution with denominators
at most k, so v_3(Q_k)>=-floor(log_3 k). It follows that the Q part
of the actual numerator has valuation at least -floor(log_3(n+1)).
I checked the stated elementary proof of
2v_3(n!)>floor(log_3(n+1)) throughout the required class, including
n=5. The scaled Q part is therefore divisible by 3 and cannot cancel
the unit C_n. The full numerator has exact valuation -2v_3(n!).

For completeness, the integer Legendre endpoint generating function is



$$
F(t)=\sum_{j\ge0}P_jt^j=(1-4t-4t^2)^{-1/2}.
$$



Modulo 3 it satisfies F(t)=(1-t-t^2)F(t^3). This follows by squaring,
using Frobenius, and choosing constant term 1. Each base-3 digit
contributes 1 or -1, so every P_j is a unit. As n+1=0 modulo 3,
Delta_n=-4P_n is a unit. In particular the endpoint does exist on
this residue class; no appeal to eventual normality is needed here.
Dividing the numerator by this unit proves the exact reduced-q result.

The source's equation (17) in the older clearing convention is also
correct: multiplying by (2n+1)! simply adds that factorial valuation.
The exponent is nonnegative because (2n+1)!/(n!)^2 is an integer.

## 4. General odd-prime statement

Section 5 passes separately. For n=-1 modulo p, all s>=p terms in the
first contraction vanish. The low coefficients of
(1-x+x^2/2)^n reduce to those of its reciprocal, and
(n)_s=(-1)^s s! for s<p. In the second contraction, s=1,...,p-1
vanish by Frobenius, s=p is killed by its explicit multiplier,
and s>p by the falling factorial. The D sequence is periodic modulo p
with period p because its recurrence resets at each multiple of p.
These facts give exactly c_p in (18), including p-2-s and p-1.

The asserted conclusion still requires c_p!=0, P_n!=0 and the strict
factorial/logarithmic inequality. None of those conditions has been
silently promoted to an all-prime theorem.

## 5. Reproducibility and scope

I inspected and reran the unchanged
check_hp_b1_ternary_actual_denominator.py using Python 3.12.
The exact Fraction arithmetic passes and agrees with the frozen
September 13 data at n=2,8. It independently builds Rodrigues
coefficients and checks the full rational numerator and reduced endpoint.
The n=2 value q_2=28 is properly excluded by the theorem.
No additional canonical index or prime was computed.

The contribution 2v_3(n!) log3=n log3+O(log n) is correct.
It does not by itself beat the established exponential error rate,
does not cover the other two ternary residues, and proves neither
irrationality nor failure of the whole b=1 family.
