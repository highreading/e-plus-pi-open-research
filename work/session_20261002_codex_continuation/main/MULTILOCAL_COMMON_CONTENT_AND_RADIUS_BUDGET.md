> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Two-prime common content and its archimedean budget

Author result, 2026-10-02. This is a new simultaneous-local construction, not an irrationality proof.

## Fresh target gate

The archive was searched for CRT pullbacks, simultaneous prime cells, multiprime integral-Hurwitz tuning and Chinese remainder/radius constructions. Existing simultaneous content bounds and logarithmic quotient-sector reports concern other normalized Gram responses. M17 supplies a one-prime parameter construction. No completed two-prime radius-compatible actual gauged content example was found. A fresh primary-paper search opened Checcoli–Fehm, *Constructing totally p-adic numbers of small height*, arXiv:2101.08631, Section 2.1, particularly the bounded residue representatives in Proposition 2.2 and the deformation mechanism. Frisch's simultaneous interpolation paper was identified in its author's university repository, but the preprint fetch failed; only its abstract was inspected. The theorem below uses ordinary integer CRT directly; neither paper is represented as solving this endpoint problem.

Sources: https://arxiv.org/pdf/2101.08631 ; https://tugraz.elsevierpure.com/en/publications/simultaneous-interpolation-and-p-adic-approximation-by-integer-va/ .

## Local constructions and isolation

Use

    P(z)=P81(z)+K157 z^157(1-z)/157!+K159 z^159(1-z)/159!.

Both p=163 and p=347 are good primes for its coefficients. Fresh normalized derangement evaluations give simple root cells

    p=163: r=159, D*'(r)=62 modp;
    p=347: r=157, D*'(r)=15 modp.

For either cell, the single matching parameter has derivative -2 in C*(x,K) modulo p; the restricted parameter power series and factorial-subtracted complete numerator are those derived in M17. Each cell therefore has a unique index lift and a unique local parameter lift.

At depth k set a=163^k, b=347^k and M=ab. Choose centered integer coefficients by CRT:

    K157=0 moda, K157=local157parameter modb;
    K159=local159parameter moda, K159=0 modb.

The coefficient divisible by the other prime power is invisible in C* at that precision, by its integral restricted parameter coefficients. Thus the two local constructions are compatible in the same rational polynomial. Choose N simultaneously in the two lifted denominator-root classes, and sufficiently large that N! vanishes at both depths. Then

    M divides gcd(D_N,B_N).

This is actual complete endpoint content, not content of an intermediate polynomial or of the raw factorial clearer. The exact primitive denominator remains |D_N|/gcd(D_N,B_N).

## Explicit radius budget

Each centered coefficient has magnitude at most floor(M/2). On |z|<=2, the two perturbations together are at most

    3 floor(M/2) [2^157/157!+2^159/159!].

The baseline factor bound is greater than401^-81. After clearing denominators, the sufficient strict budget is

    3 floor(M/2) [159*158*2^157+2^159] 401^81 < 159!.

It holds for k=1,2,3,4 and fails as a uniform centered-representative guarantee at k=5. This failure is only of this sufficient uniform bound; it is not a proof that every depth-five representative is analytically impossible.

## Four simultaneous exact specializations

| Depth at both primes | K157 | K159 | Actual joint index N |
|---:|---:|---:|---:|
| 1 | 5868 | -5899 | 35204 |
| 2 | 1446044394 | -329077797 | 2023900906 |
| 3 | -32156376795098 | -78587368279162 | 5114260361064 |
| 4 | 1941709431936832513 | 4513461826283302902 | 1068315834361344888 |

Every row defines a degree-160 rational polynomial with endpoints0/1, first derivative1, integral P-jets and even G-jets. Its composition has radius greater than two, and its actual gcd at the displayed N is divisible by (163*347)^k. The new receipt evaluates the full factorial-subtracted numerator and denominator independently in both prime-power rings for the two-coefficient polynomial; it does not infer cancellation from CRT coefficient congruences alone.

## Meaning and remaining target

Separate good-prime common-content cells can coexist in one polynomial without losing the proven analytic radius. The cost is explicit: the product modulus enters the centered coefficient height and consumes the factorial-weighted perturbation budget. These are four finite-depth specializations, not a uniform infinite-prime supply or a fixed rational polynomial with arbitrary-depth content. Moreover, the selected divisor is much smaller than the factorial scale of D_N at the enormous joint indices. A useful global denominator theorem still requires simultaneous prime supply, depth, index size and complete error estimates at compatible scales.
