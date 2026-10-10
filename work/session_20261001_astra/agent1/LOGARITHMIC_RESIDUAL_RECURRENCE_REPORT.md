> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Logarithmic residual recurrence: report

Original author research, English and offline, 2026-10-01. Earlier collected-coefficient results and successful checks are preserved; no scan, check replay, or independent review was performed.

For both signs, R_n=35A_n-6epsilon 2^(n+1)Pell_n satisfies the proved integer recurrence

    n(n+4)R_(n+4)
    -2(4n^2+15n+6)R_(n+3)
    +4(2n^2+7n+10)R_(n+2)
    +8(n+2)(4n+5)R_(n+1)
    +16(n+1)(n+2)R_n=0.

The proof derives its generating function and records the explicit initial values R_1 through R_4. The equation at n=0 cannot determine R_4. At odd p, forward division fails at n=0,-4 modulo p; backward division fails at n=-1,-2. Every step needed to reach an actual target n<p from those initial values is a unit division. Auxiliary singularities and excluded normalization primes are also listed.

A new all-size content theorem is

    gcd(R_l,R_(l+1),R_(l+2),R_(l+3))
      divides 16^(l-1)l!(l+1)!, l>=1.

Thus four consecutive residual values cannot all vanish modulo an odd prime p>l+1. This is a statement about consecutive integer indices, not consecutive admissible multiples of four.

For even n>=2 both residual signs are strictly positive and bounded by

    R_n^(epsilon)<=C(n)(2+2sqrt(2))^n,
    C(n)=35(n/2+1)+3sqrt(2).

Consequently, on a fixed admissible n=4k, every collection of distinct prime candidates on the actual M=3,t=2 strip whose character-selected residual vanishes satisfies

    sum log p<=2n log(2+2sqrt(2))+2log C(n).

The stronger version weights each logarithm by the valuation of its selected integer residual. This is an O(n) bound uniform over the prime candidates. It asserts no prime supply or density and does not identify higher residual valuations with those of pT.

The actual strip is retained exactly:

    m=2p-1, p>n, p>=11, U!=0,
    floor(2m/p)=3, r=p-2,
    floor((n+2r)/p)=2,
    floor(J/p)=8, J<p^2.

At each such prime epsilon=(2/p). The existing first-layer normalization is pT=(16chi_p/105)R_n^(epsilon) modulo p.

A new endpoint distinction makes a zero residual more informative. At a residual zero, p divides U if and only if p divides Pell_n. Hence:

* Nonzero residual: v_p(T)=-1 and v_p(den(T/U))=1+v_p(U).
* Zero residual with Pell_n a unit: U is a unit, T is integral, and p disappears from den(T/U).
* Simultaneous residual and Pell zeros: endpoint and complete numerator lifting are required.

The proof supplies the endpoint expansion

    U=A_n+4p[x^n]P(x)^n C(x)^(-2)log C(x) modulo p^2

and the exact p-integral decomposition of pT into its eight possible positive p-multiples plus all regular Laurent terms, including negative indices. Absence from the companion denominator requires pT=0 modulo p^(1+v_p(U)). Lifting the residual recurrence alone cannot replace this complete numerator lift.

An optional explicit binary-congruence family is given with n=4(2^a-1) and m~rho n log n. The assertions apply whenever its odd prime candidate is actually prime; infinitely many prime members are not claimed.

These are author proofs forming a completed recurrence/content stage. No general unit theorem, higher-depth cancellation bound, leading companion-rate improvement, or irrationality conclusion is claimed. The four already resolved regions and gap-one pole remain unchanged.

Full proof: work/session_20261001_astra/agent1/LOGARITHMIC_RESIDUAL_RECURRENCE.md.

The new proof and report require controller-confirmed read-back before final handoff.
