> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Scalar center gcd report

New author research, offline, 2026-10-01. No prime sweep, old checker replay, or independent review.

For the actual numerator N=(n!)^2 Qcal+2^n Acal and denominator Z=(n!)^2 P, separate dyadic accounting proves

 2^n divides gcd(Z,|N|), n>=4,
 q_n <= (n!)^2 P_n/2^n.

The proof establishes Acal integrality and retains both numerator terms. The sharper dyadic law is conditional on strict valuation separation; otherwise the exact quantity needing lifting is Acal+((n!)^2/2^n)Qcal.

The retained scalar Acal transfer gives ternary residues (1,0,0). The endpoint generating function gives nonzero ternary digit factors (1,2,2), so P_n is always a 3-unit. Consequently

 v_3(q_n)=2v_3(n!), n>=3 and 3 divides n.

Combining this NEW law with the main draft's retained 5-adic law yields

 3^(2v_3(n!))5^(2v_5(n!)) divides q_n,
 n>=6 and 3 divides n.

Its exponential rate log 3+(log 5)/2 strictly exceeds 2log(1+sqrt(2)). With the COMPLETE signed scalar error retained, the actual primitive forms satisfy

 q_n |e+pi-c_n| -> infinity

along multiples of three. Their eventual sign is (-1)^n when written as q_n(e+pi)-a_n. This stops that specific subsequence as a shrinking-primitive-form route. The eventual error threshold remains ineffective, as in the author input.

In the other ternary classes the unit argument stops. The precise normalized quantity needing depth control is

 Acal_n+2^(-n)(n!)^2 Qcal_n.

A zero Acal residue is not promoted to a valuation theorem. No all-index exclusion or sufficiently small exponential upper bound for q_n is established.

The main scalar identities, error estimates, and 5-adic theorem remain author dependencies. TOEPLITZ_LOCAL_ARITHMETIC is preserved with its exact domains; its interior-window theorem is not used at p=3. No older excluded family is identified with this construction.

Full proof: work/session_20261001_astra/agent1/SCALAR_CENTER_GCD_RESEARCH.md.
