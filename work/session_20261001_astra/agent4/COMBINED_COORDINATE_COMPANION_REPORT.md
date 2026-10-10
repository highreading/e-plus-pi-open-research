> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Agent4 completion report: scoped denominator arithmetic

The mathematical notes are LARGE_SELECTOR_DYADIC_REVIEW.md and COMBINED_COORDINATE_COMPANION.md in this directory. This report records their conclusions; delivery readback is a separate controller verification step.

1. Dyadic review: Sections 1–6 pass with an explicit domain. For n=4k>=4, m>=0 and U!=0, the COMPLETE reduced denominator is

v_2(den(alpha+beta))=v_2(n!)+v_2((n+4m)!)+v_2(U)-(2n+4m)/2.

Choosing a power of two k<P<=2k and m=-k (mod P) proves U!=0 and v_2(U)=n/2. The displayed valuation then equals 3n/2+2m-s_2(n)-s_2(n+4m). The proof uses the unique least-valuation term of the full exponential numerator and a strict valuation gap to beta. Endpoint nonvanishing is proved on this allocation; complete-error asymptotics are not reviewed.

2. Combined coordinate arithmetic: for a positive eligible coordinate, with Ffac=(n!)^2 and the integral contractions X,E,L defined in the note,

B=den(r+beta)=Ffac |X|/gcd(Ffac |X|,|L|), since r=0,
Qexp=Ffac |X|/gcd(Ffac |X|,|E|),
q=Ffac |X|/gcd(Ffac |X|,|E+L|).

These are different reduced denominators. Coordinate zero has the additional correction Delta and must use L+Delta. Reconstruction-row content cancels from Hsel/A=||C||_1/|X|; polynomial content is a separate quantity and also cancels from the reduced companion formula.

3. For b=3, m=1, n>=2^22, n=3 (mod 13), every eligible positive row satisfies, with f=v_13(n!), x=v_13(X), h=floor(log_13(2n+2)),

v_13(q)=v_13(Qexp)=2f+x,
0<=v_13(B)<=x+h.

On n_s=13^(s+1)+3, s>=5, this sharpens to

v_13(q)=v_13(Qexp)=(n_s-4)/6,
0<=v_13(B)<=s+1.

Thus the factorial 13-part in q and the exponential companion does not transfer to B. Its contribution to the combined budget 2log B on this subprogression is only O(log n_s).

4. The unresolved quantity is gcd((n!)^2 |X|,|L|), equivalently the reduced moment gcd in the note. Locally one needs v_13(L) relative to 2v_13(n!)+v_13(X). Other primes and ||C||_1/|X| remain uncontrolled. No global budget exponent follows. Divergence of q on the progression is established, but the upper growth window needed for shrinking independent forms is not.

Evidence classification: these are paper deductions using already reviewed source identities and the previously executed single p=13 gate. No completed audit, residue check, broad historical review, or moving-saddle analysis was rerun. No conclusion about rationality or irrationality of e+pi is obtained.
