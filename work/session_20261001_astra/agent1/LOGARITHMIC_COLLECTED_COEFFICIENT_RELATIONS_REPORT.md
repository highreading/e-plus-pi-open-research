> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Collected logarithmic coefficient relations: report

Original author research, English and offline, 2026-10-01. The completed cancellation-range results are preserved. No prime scan, assumed prime supply, or independent review.

For p>max(n,sqrt(J)), write 2m=Mp+r and retain the actual three-term collected expression from Section 6 of the preceding paper.

The new weight relations are

    V_0=0, V_1=1, V_(j+2)=2V_(j+1)-2V_j,
    Phi_2(M)=-V_(M+1)/(M+1),
    Phi_0(M)=2 sum_{j=1}^M V_j/j,
    (2M+3)Phi_1(M+1)=2(M+1)Phi_1(M)-4V_M.

All required denominator units are specified. In particular, when Phi_2 is present, its residue vanishes exactly when M+1 is divisible by four.

A deterministic collected-coefficient region is proved. For a=1,2,3,4, every prime satisfying

    max(n,sqrt(J),J/(2a+1))<p<=2m/a

has M=a,d=0 and

    pT=chi_p c_a U modulo p,
    (c_1,c_2,c_3,c_4)=(2,4,16/3,16/3).

These are units. Thus moment cancellation in these regions occurs exactly at primes dividing U. Their total removable logarithmic mass is at most log|U|=o(n log n). This is a collected-coefficient obstruction, not a missing-monomial bound.

The actual differential equation of P^n C^r gives an explicit coefficient recurrence. Its steps at multiples of p cannot be inverted. The proof resolves the relevant blocks using t=p-r and

    P^n C^r=C(x^p) P^n/C^t modulo p.

It reduces ell_0,ell_1,ell_2 to finite n-index expressions A_(n,t), (2/p)B_(n,t), and D_(n,t), with every denominator a p-unit.

On the explicit M=3 strip

    p>n, p>=11,
    2<=t<=n/2 even, m=2p-t/2, U!=0,

Phi_2 vanishes, but cancellation is equivalent to the additional congruence

    35A_(n,t)-6(2/p)B_(n,t)=0 modulo p.

For t=2, B_(n,2)=2^(n+1)Pell_n, where Pell_n satisfies the integer recurrence Pell_(n+2)=2Pell_(n+1)+Pell_n. The residual is therefore reduced to two p-independent quantities and one quadratic-character sign. No unevaluated Phi weights or high-degree coefficient extractions remain.

The actual n=4 coefficients give residual 9660-2304(2/p), disproving an automatic rational cancellation identity after Phi_2 is removed. This specialization does not assert an asymptotic prime family. The general congruence remains an unresolved arithmetic condition.

The gap-one surviving pole is preserved exactly. Moment cancellation is kept separate from endpoint content: after a zero residue the deciding condition for absence from Bbeta is

    pT=0 modulo p^(1+v_p(U)),

with all regular and negative Laurent terms restored in the lift.

The already successful new symbolic certificate, logarithmic_collected_relations_checks.json, has not been rerun. It supports the differential polynomials, weight constants, and the n=4 coefficient specialization; the all-index conclusions rely on the written proofs.

No leading-rate improvement below the actual companion threshold 5/82 is established. The paper provides a rigorous cancellation limitation on explicit regions and a shorter residual congruence elsewhere, without claiming that all collected cancellation is subleading.

Deliverables:

    work/session_20261001_astra/agent1/LOGARITHMIC_COLLECTED_COEFFICIENT_RELATIONS.md
    work/session_20261001_astra/agent1/LOGARITHMIC_COLLECTED_COEFFICIENT_RELATIONS_REPORT.md

Controller-confirmed write and read-back remain required before final handoff.
