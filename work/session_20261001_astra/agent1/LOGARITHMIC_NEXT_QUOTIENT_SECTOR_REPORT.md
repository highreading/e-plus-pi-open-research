> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Child 1 handoff: M=4 logarithmic quotient sector

2026-10-02. Finish-only completion of the accepted task. No further assignment is requested.

## Completed author result

The companion paper LOGARITHMIC_NEXT_QUOTIENT_SECTOR.md derives the M=4 residue from the actual polynomial coefficients. Its exact domain is n=4k, p prime, p>n, p>=11, odd 1<=t<=p, m=(5p-t)/2, and U!=0. The three floor sectors are

    d=2 for t<=n/2;
    d=1 for n/2<t<=(p+n)/2;
    d=0 for t>(p+n)/2.

All three are realized in the actual n=4 family with nonzero endpoint. The correct weights are

    Phi(4)=(16/3,-536/315,4/5).

Writing A,B,D as the actual complementary-power coefficient sums, the residue in d=2 is

    pT=(4chi_p/315)(420A-134(2/p)B+63D) modulo p.

D is positive for the allowed odd t in d=2 and zero in d=1. In d=0 the residue is the already established unit multiple (16chi_p/3)U. Primes 2,3,5,7 are outside the domain. Prime 67 is allowed: it kills the middle weight, and in d=1 gives the same unit-multiple-of-U gate; it does not erase the D term in d=2.

A written parity-moment argument proves

    0<B<=2sqrt(2)A, 0<=D<=2A,
    (420-268sqrt(2))A
       <=420A-134epsilon B+63D
       <=(546+268sqrt(2))A

for both epsilon=+1,-1 and every n=4k, odd t>=1. Thus both rational residuals are strictly positive.

The explicit dyadic clearer

    H=2^(n/2+2t-2)

produces two nonzero positive p-independent integers Z_(n,t)^epsilon. Their product Delta satisfies

    log Delta <=2(n/2+2t-2)log 2+2n log(2+2sqrt(2))
                 +2log binom(t+n/2-1,n/2)
                 +2log(546+268sqrt(2))
              =O(n+t).

For each fixed n,t, with m=(5p-t)/2 varying with p, every d=1 or d=2 first-residue zero satisfies p|Z_(n,t)^((2/p)). Therefore

    sum_p v_p(Z_(n,t)^((2/p))) log p <=log Delta.

In particular the one-factor cancellation mass is O(n) on each fixed-t fiber, uniformly O_C(n) on an individual fiber with t<=C n. This extends the prime-independent residual method beyond the completed M=3,t=2 strip.

## Specific obstruction and remaining scope

This is not a uniform all-t result. The natural rational residuals already have, for n=4 and odd t>=7, exact reduced denominator

    2^(2t-10-s_2(t-1)).

Their positive reduced numerators consequently have logarithmic height Omega(t). The calculation uses the saved exact n=4 formula for B and Legendre's central-binomial valuation. It applies within the actual d=1 domain whenever p>2t, p>=11; U is nonzero for every integral m at n=4. It obstructs obtaining an all-t O(n) bound merely by clearing and reducing these residuals. It does not prove that every alternative prime-parameter elimination is impossible.

Even d=2 has n/4 possible odd t values; multiplying all its separate residual pairs supplies only an O(n^2) height estimate. No bounded collection of O(n)-height residuals covering all M=4 sectors, no all-t O(n) mass estimate, and no growing-M extension is proved.

Retain the endpoint distinction. With u=v_p(U),

    v_p(den(T/U))=max(0,1+u-v_p(pT)).

A zero first residue removes p from den(T/U) immediately only when U is a p-unit. Otherwise the full Laurent expression must vanish modulo p^(1+u), including regular and negative-index terms. Higher valuations of Z are not proved to equal those of pT. The complete-center denominator is a separate object.

## Evidence and verification status

The paper contains author proofs, without independent review. The existing certificate logarithmic_next_sector_checks.json was genuinely read back during closeout and has status PASS_NEW_M4_WEIGHT_AND_SYMBOLIC_OBSTRUCTION_IDENTITIES. It checks the three weights, normalized residue coefficients, exact n=4 formulas, and a positive constant. It does not certify the all-index proof. No successful old check, M=3 recurrence, support scan, or accepted review was repeated. No new prime search or density assumption was used.

The retained LOGARITHMIC_RESIDUAL_RECURRENCE.md and its report remain unchanged, including the fourth-order recurrence, exceptional indices, and fixed-n M=3 mass theorem. The collected-coefficient paper was read as the existing source of the actual block formulas; no new independent-review verdict is attached to it.

## Provenance and collaboration disposition

Two recent durable author notes were read and reconciled:

* [session identifier removed] (14:45:10+0800): its announced M=4 weights, sectors, intended fixed-t bounds, and intended obstruction are now coherently recorded in the companion paper. Its announcement was not previously a proof or file receipt.
* [session identifier removed] (15:19:57+0800): its finish-only save promise is discharged by this paper/report and their subsequent confirmed readbacks. It supplied no extra mathematical deduction.

The companion paper records the exact source-note paths and distinguishes preservation from verification. The broad historical provenance audit, integration of other children's reports, and shared closeout files remain the main agent's responsibility. Child 1 did not repeat that accepted audit or claim to inspect every historical message.

## File index and termination status

All paths below are under work/session_20261001_astra/agent1/:

* LOGARITHMIC_NEXT_QUOTIENT_SECTOR.md — current-stage paper: exact sectors, positivity proof, integer residual height/mass theorem, obstruction, endpoint ledger, provenance.
* LOGARITHMIC_NEXT_QUOTIENT_SECTOR_REPORT.md — this handoff.
* logarithmic_next_sector_checks.json — preserved finite symbolic evidence; genuine readback completed before this handoff was written.
* LOGARITHMIC_COLLECTED_COEFFICIENT_RELATIONS.md and LOGARITHMIC_COLLECTED_COEFFICIENT_RELATIONS_REPORT.md — retained coefficient/weight source and earlier handoff.
* LOGARITHMIC_RESIDUAL_RECURRENCE.md and LOGARITHMIC_RESIDUAL_RECURRENCE_REPORT.md — preserved completed M=3 package.

At the time this report's content was submitted, the two new document readbacks were still pending; final completion must follow real readback receipts, not this text's assertion. The final Child 1 reply will supply that status. No bulk deletion, relocation, shared-file edit, delegation, or new research direction is part of this closeout.

The accepted stage ends with the fixed-t theorem and the explicit natural-residual obstruction. Unresolved global arithmetic remains unresolved. In particular, the actual e+pi problem remains OPEN.
