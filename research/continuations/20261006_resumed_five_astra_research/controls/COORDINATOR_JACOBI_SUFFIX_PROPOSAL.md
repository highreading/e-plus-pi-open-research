> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# New suffix synchronization and a constructive upper-content proposal

Status: coordinator-derived mathematical proposal, awaiting independent review. This reuses the established Lucas/Kummer digit evaluator and does not claim new general binomial theory. A scoped local search found the eleven previously recorded equal content pairs and special zero-content examples, but no universal suffix synchronization theorem. Targeted public searches for adjacent Jacobi p-adic content and the specific residue returned no directly relevant primary result. That is a search gate, not an exhaustive novelty claim.

## Exact synchronization

Let m=851+6561M, M>=0. The degree, integral upper binomial index, and half-integral upper index are respectively

- J_m: m, 3m-1, m-1/2;
- J_(m-1): m-1, 3m-2, m-3/2.

Run the previously proved eight-state min-plus recurrence, with state order000,001,010,011,100,101,110,111, initialization000 cost0, and each outgoing binomial borrow adding one to the cost. After the first eight digits, BOTH exact vectors equal

    (0, infinity, infinity, infinity, infinity, 1, 1, 3).

The common remaining degree and integral upper index are M and3M. The low residues of the two half-integral indices are4131 and4130; in both cases the remaining 3-adic quotient is M-1/2. Thus all future transition matrices and terminal rules are identical. This proves r=u for EVERY m congruent851 modulo6561, not only sampled powers. In the actual family, t=v3(8m-247)>=8 implies that residue. Subject to the retained unit-normalizer hypothesis, the collision r=4+u is therefore impossible and the accepted noncollision identity gives cont3(E)=2r.

## Constructive upper bound to audit

The resonance suffix m=247/8 modulo3^t, t>=8, has a zero-cost000 path. Its digits above position4 alternate0/1, and its remaining half-index is M-1/2. At the first unknown middle digit the half-carry state is q=0. The integral-upper digit is the preceding degree digit, which is0 or1.

For a degree digit d, the half-index digits are (1,2,0) for q=0 and (2,0,1) for q=1; the next q values are (0,0,1) and (0,1,1). Choose the coefficient split k+r=d as follows:

- q=0,d=0 or1: k=0;
- q=0,d=2: k=2;
- q=1: k=0 if d=0, and k=1 otherwise.

The half-binomial borrow stays zero. The integral binomial contributes one borrow only when q=0,d=2; the next digit always clears that borrow. Two such charge events are separated by at least two positions. A following block of25 leading ones has zero additional cost, and a final zero tail terminates with000.

If L=h-1 is the number of ternary digits and the fixed suffix and prefix are disjoint, the unknown middle has length Mlen=L-t-25. Thus r<=ceil(Mlen/2), giving

    cont3(E)=2r<=Mlen+1=h-t-25,
    s_c=h-2-2r>=t+23.

For t>=9 this would exclude s_c<32 on the actual deep-resonance original family. Check overlapping prefix/suffix cases and every normalization/terminal hypothesis. The finite certificate corroborates all middle words of length0..7, but the proof is the explicit policy and common-tail argument, not extrapolation from those checks. This excludes one uniform inverse-comparison method; it is no irrationality result. The direct whole-pair/directional cofactor route still requires actual scalar guards, all-prime final gcd, and complete same-index error.

## Primary real-logarithm dependency now checked at text scope

The coordinator read the primary English PDF text of Matveev2000, Corollary2.3, printed page1219, via https://www.mathnet.ru/eng/im314 and its full-English PDF link. It gives a lower bound for a nonzero logarithmic linear form with factor D^2 times the logarithmic-height product and logarithms of eD and eB. For the two positive rationals4 and3, take D=1, heights A1=ln4 and A2=ln3, integer coefficients q and -p, and B=max(q,|p|). A nearest integer p to q log_3(4) satisfies |p|<=2q; unique prime factorization makes the form nonzero. A deliberately loose constant K=10^12 therefore gives ||q log_3(4)||>=c q^-K for an effective c>0. This supplies the fixed real-logarithm input used in the quantitative window intersection. No visual PDF inspection or successful direct download is claimed; primary web text succeeded while direct downloadreturned403. Review the application and the inherited exact-window argument, without reopening already accepted moving-base estimates.
