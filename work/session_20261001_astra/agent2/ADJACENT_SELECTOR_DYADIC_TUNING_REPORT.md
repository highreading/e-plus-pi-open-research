> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Adjacent-selector dyadic tuning report

Status: new author deductions, not independently reviewed. Main proof: ADJACENT_SELECTOR_DYADIC_TUNING.md. PHASE_CROSSING_ARITHMETIC_BYPASS.md is preserved. No continuation proof, generic cancellation construction, numerical scan, or independent review was repeated.

For an eligible adjacent pair, write

    r=n/2, J=n+4m, N=2n+4m,
    t0=N/2-v2(n!)-v2(J!),
    d=v2(J+4)-1>=1, t1=t0-d,
    B=r-t0.

Retain BOTH complete rational numerators X_j,Y_j, with Z_j=X_j+Y_j, and write

    U_j=2^r u_j,
    Z_0=2^t0 gamma v0, Z_1=2^t1 gamma v1,

where u_j are odd integers, v0,v1 are coprime odd integers, and gamma is a rational dyadic unit.

EXACT DENOMINATOR DEPTH. For primitive a,b and nonzero forcing, let

    L=u0 a+u1 b, M=2^d v0 a+v1 b.

Then the actual reduced denominator satisfies

    v2(q)=[B+d+v2(L)-v2(M)]_+.

Increased forcing valuation worsens the denominator; it does not create savings. For 1<=k<=B, saving at least k powers relative to B is equivalent to primitive membership in

    Lambda_k={2^d v0 a+v1 b=0 mod 2^(d+k)}.

Its index is 2^(d+k). Every primitive member has a odd, b=2^d c with c odd, nonzero forcing of valuation r, and primitive polynomial content one. With r_k=-v0/v1 modulo 2^k, a basis is

    (1,2^d r_k), (0,2^(d+k)).

Writing c=r_k a+2^k l, primitivity is exactly a odd and gcd(a,l)=1. The remaining exponent is [B-v2(v0 a+v1 c)]_+. Depth beyond B yields no further dyadic denominator saving.

EXCEPTIONAL DIRECTIONS. The primitive forcing-annihilator direction is (u1/g_u,-u0/g_u); it has both entries odd and belongs to no saving lattice. The complete rational-numerator annihilator is (v1,-2^d v0); it belongs to every lattice, has nonzero forcing, and gives center zero with q=1 and error |e+pi|. Separate X and Y annihilators need not give complete cancellation. The full-error annihilator exists over integers exactly when e+pi is rational and is explicitly described in the proof.

HEIGHT THEOREM. Primitive membership of height at most H is exactly the finite condition

    1<=a<=H odd, |c|<=H/2^d,
    c=r_k a mod 2^k, gcd(a,c)=1.

A primitive saving vector exists with h<=2^(d+k-1); a nonzero-center one exists with h<=2^(d+k). Every nonannihilating saving vector obeys

    h>=max(2^d,2^(d+k)/(2^d|v0|+|v1|)).

Once 2^(d+k)>(2^d|v0|+|v1|)h_ann, the shortest primitive vector is exactly the complete numerator-annihilator direction, of height h_ann=max(|v1|,2^d|v0|). Thus an index-based lower bound for shortest primitive height is invalid. The proof also gives congruence lattices with very short nonprimitive vectors but primitive height of order 2^k; primitive division can lose depth.

GEOMETRIC DYADIC COST. To obtain v2(q)<=E_n=O(n), take k=B-E_n. A nonzero-center vector exists with

    log h<=2m log 2+O(n),
    log H_sel<=2m log 14+O(n).

This tunes only the dyadic part. It supplies neither a small error nor a geometric whole denominator. No matching necessary asymptotic height is established for these particular residues.

EXACT FINAL REDUCTION. Retain D=n!(J+4)!O_(N+4), A_j=DZ_j, and

    g=gcd(aA_0+bA_1,D(aU_0+bU_1)).

Then q=D|aU_0+bU_1|/g and q|c-S|=D|aR_0+bR_1|/g. Membership in Lambda_k guarantees the actual divisor

    g_k=2^(N/2+d+2+k).

The odd part of g remains unresolved.

FULL-ERROR COMPATIBILITY. If R_1!=0, set

    y=(-R_0/(2^d R_1)-r_k)/2^k.

The complete residual for a primitive lattice vector is

    aR_0+bR_1=2^(d+k)R_1(l-a y).

The exact missing problem is an odd a, gcd(a,l)=1, with weighted height at most H and

    0<D 2^(d+k)|R_1||l-a y|/g<epsilon.

The strict lower bound is the separate nonvanishing requirement. Using the guaranteed dyadic gcd cancels the modulus from the sufficient error multiplier:

    (D/g_k)2^(d+k)=C_2=D/2^(N/2+2).

An odd-denominator convergent l/a with nonzero error and

    a>C_2|R_1|/epsilon,
    a<=H/(2 max(1,|R_0/R_1|)),
    a>=2^(d+k+1)/H

would meet the desired complete-error and height budgets. The preceding unrestricted construction does not guarantee such a convergent. For rational y=P/Q with even Q, every odd a has |l-a y|>=1/Q; nearby irrational values can postpone adequate restricted approximation beyond any prescribed finite height. Infinitely many odd convergent denominators for an irrational y do not bound the first usable one. Here y is a nonconstant rational fractional-linear transform of e+pi.

The stopping result is an exact depth/height theorem plus an explicit simultaneous restricted approximation obstruction. The available coefficient budget has ample algebraic room, but the required approximation inside that room, odd-prime reduction, and nonvanishing remain unproved. No irrationality or rationality conclusion follows.
