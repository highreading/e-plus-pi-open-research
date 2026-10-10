> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational scaling removes the entire dyadic layer with inherited five-content

2026-10-02. Original author theorem under root's fresh rational-coefficient steering. No integral-H restriction is imposed by the human request. The rational coefficient denominator, complete signed error, pole periods and final reduced center are all retained.

## Fresh prior-art gate

Archive queries covered negative dyadic scaling, rational coefficient denominators at correction poles, endpoint norm depth dividing the old denominator, and actual content cancellation. Read `SIMULTANEOUS_EXACT_RATIONAL_CORRECTION_GATE.md`, including its explicit exclusion of nonintegral principal-part coefficients from the integral/monic valuation gate. Read `EVEN_LEADING_QUADRATIC_CORRECTION_COST.md`, Sections6–7: its nonnegative scaling exponent imposes d~tau/2, which is the exact internal premise changed here. Opened root's `main/EXPONENTIAL_GAUGED_PULLBACK_PRIMITIVE_INTERFACE.md`: it already emphasizes that rational kernel coefficients may coexist with a much smaller final primitive center. That general normalization principle is overlap, not novelty.

Fresh primary searches concerned rational linear forms, denominator reduction, common-denominator Padé coefficients and prime cancellation. Opened Fischler–Rivoal, *Rational approximation to values of G-functions, and their expansions in integer bases*, full primary https://arxiv.org/pdf/1512.06534, Theorem2 and surrounding normalization discussion. The established restricted-denominator approximation theory is not imported as a bound for e+pi. The present result is the exact derivative-sum correction, inherited-five factor and evaluated primitive gcd below; no new generic denominator method is claimed. Archive search absence is not a global novelty assertion.

## 1. General rational scaling and preserved target

Let an OLD actual reduced matched center be

    c=A/(2^tau B), B=5^b B0,
    tau>=1, A odd, gcd(A,2^tau B)=1, gcd(B0,10)=1,

and let its integer response be U!=0. Fix the primitive polynomial

    Q(w)=2w²−10w+13.

Choose any odd r>=1 with5 not dividing r, set d=r+1 and define

    Y=Im[(4+4r−i(2+r))(2+i)^(r+1)].

The previously proved Gaussian numerator identity gives Y odd and5-adically a unit, and the FULL endpoint effect of Q^(−r) is

    delta=Y/[2^(2r−1)5^d].                                  (1)

Permit the dyadic rational scaling

    j=2r−1−tau=2d−3−tau,
    H=U k2^j Q^(−r), K=H″+H′,

where j may now be NEGATIVE. By exact differentiation, every ordinary residue and every e^w-twisted residue of K at its finite poles vanishes. The e and pi responses, original exponential rational numerator, and the coefficient U remain exactly unchanged. No extra constants from the poles appear.

Both endpoint terms in(1) give the exact shift and COMPLETE signed error

    eta=2^j delta=Y/(2^tau5^d),
    c_k=c−k eta,
    E_k=S−c_k=E_old+k eta.                                  (2)

The formula(2), not a convenient written coefficient clearer, determines the new actual center.

## 2. Actual q in all depth cases

Put m=max(b,d). Before reducing, the complete center is

    c_k=[A5^(m−b)−kYB0 5^(m−d)]/[2^tau B0 5^m].             (3)

Choose k in the concrete dyadic cancellation class

    kYB0 5^(m−d)=A5^(m−b) mod2^tau.                        (4)

All multipliers here are dyadic units, so (4) is a unique odd residue class modulo2^tau. A centered representative satisfies |k|<=2^(tau−1), although a5-unit requirement may need a larger representative when d>=b. No unknown value of S enters(4).

Every old prime power of B0 remains in the final q: modulo any such prime, the first numerator term is a unit and the second is divisible by B0. The prime5 interface is exact:

    d<b: q_k=B0 5^b=B, with NO requirement that5 be coprime to k; (5)
    d=b: q_k=B0 5^max(0,b−v5(A−kYB0));                       (6)
For d>b put e=v5(k). The two unequal cases are

    e<d−b: q_k=B0 5^(d−e),
    e>d−b: q_k=B0 5^b.                                      (7)

At equality e=d−b, retain the exact tied numerator valuation

    q_k=B0 5^max(0,d−v5(A5^(d−b)−kYB0)).                    (8)

Equivalently, in every case the full safe expression is

    q_k=B0 5^max(0,m−v5(A5^(m−b)−kYB0)).                   (9)

Infinite valuation at a zero numerator is allowed. No division by a possibly zero center or error is used. For d>b and5-unit k, (7) specializes to the earlier new-norm cost B0 5^d. The strict inherited case d<b in(5) is the desired improvement: its first numerator term A is a5-unit and the second is divisible by5, so no tied cancellation or accidental new5-cost exists.

Thus for d<b,

    q_k/q=2^(−tau) EXACTLY.                                (10)

The dyadic denominator of the written correction coefficient does not restore a dyadic factor in the FINAL primitive center. It is canceled by the actual evaluated numerator congruence(4). This is a full-q statement, not permission to omit that coefficient denominator from the rational kernel.

## 3. Complete real shift for a bounded known-data coefficient

For the centered representative in(4), the FULL endpoint estimate is

    |k eta|<=d 5^(−(d−1)/2).                               (11)

Indeed |Q(a)|=4sqrt5 and |Q′(a)/Q(a)|=sqrt17/(2sqrt5)<1. Retaining H and H′ yields

    |delta|<=4(4sqrt5)^(−r)(1+r|Q′(a)/Q(a)|).

Multiplying by |k|2^j<=2^(tau−1+j), and using tau+j=2r−1, cancels all powers of4 exactly and leaves at most(1+r)5^(−r/2), which is(11). The calculation is valid for negative j as well as positive j.

Consequently

    |E_k|<=|E_old|+d5^(−(d−1)/2),
    q_kE_k=q_k[E_old+k eta].                                (12)

There is no claim that (12) makes a primitive residual small. It provides the complete signed interface and an exponentially small shift whenever d tends to infinity. A known old error substantially larger than the allowance in(11) retains its sign and relative scale; comparable-error alignment remains open.

## 4. Actual scalar coefficient denominator and full rational height

Let u2=v2(U). In the negative-j regime put a=tau−2d+3>0 and

    D=max(0,a−u2).

Since k in(4) is odd, the scalar U k/2^a has ACTUAL reduced dyadic denominator2^D. If D>0, its integer numerator is U_odd k, U_odd=U/2^u2, with

    |U_odd k|<=|U_odd|2^(tau−1).

Its real absolute value instead obeys

    |U k2^j|<=|U|2^(2d−4).                                (13)

These are different costs: small real magnitude does not remove a large rational coefficient denominator. The exact correction is

    K=U k2^j r[(r+1)(4w−10)²−(4w−6)Q(w)]/Q(w)^(r+2).        (14)

Its numerator degree is3, denominator degree2d+2, and the rational coefficient numerator height after clearing only its scalar denominator is O(|U_odd|2^tau d²). A safe written denominator height bound is

    height(2^D Q^(r+2))<=2^D25^(d+1).                       (15)

The bracket in(14) has dyadic content exactly2 when r is odd: its constant coefficient100r+178 is2 modulo4, while all coefficients are even. Thus the correction's coefficient dyadic denominator actually divides2^max(0,D−1); this extra factor is not needed for the final-q theorem. Both finite poles have order at most r+2=d+1. The degree and rational coefficient denominator are retained throughout.

## 5. Explicit reflected critical subsequence

Use the independently authored actual-five theorem `agent1_arithmetic/REFLECTED_ACTUAL_FIVE_DENOMINATOR.md` and complete analytic subsequence `agent3_analysis/POWER_TWO_INVERSE_CRITICAL_SUBSEQUENCE.md`. At N=2^s, n nearest a20-multiple to the EXACT inverse-critical Psi root, h=N−n, they give

    tau=N, b=v5(q)=v5(N!)+v5(U)>=v5(N!),
    |c−(e+pi)|=O(N^(−1/4)), n~sqrt(2N).                     (16)

Choose d to be the greatest EVEN integer at most v5(N!)−1 with5 not dividing d−1. Such d exists for all sufficiently large N, differs from v5(N!) by O(1), and satisfies

    d=N/4−O(log N)<b,
    r=d−1 odd and5-unit,
    j=2d−3−N=−N/2−O(log N).                                (17)

This choice uses the actual theorem to justify b>=v5(N!), rather than assuming a factorial factor survives. Since d<b, there is no tied5-depth. Take the centered k in(4), so |k|<=2^(N−1). Then(5),(10),(11),(16) prove

    q_k=q/2^N EXACTLY, q_k=B0 5^b,
    |k eta|<=exp[−((log5)/8)N+O(log N)],
    c_k→e+pi, |c_k−(e+pi)|=O(N^(−1/4)).                    (18)

The denominator reduction improves the earlier integral-coefficient exponent log2−log5/4 to the FULL log2. The tradeoff is a smaller real-decay exponent log5/8 instead of log5/4, still enough to preserve the complete convergence theorem.

On this subsequence u2=1, so the scalar denominator in Section4 is exactly

    2^(N−2d+2)=2^(N/2+O(log N)),

and the correction's coefficient denominator divides2^(N−2d+1). The written polynomial denominator degree is2d+2=N/2+O(log N), and the safe coefficient-height bound in(15) has logarithm

    D log2+(d+1)log25
       =[log2/2+log25/4]N+O(log N).                         (19)

All original odd content remains, including the compulsory actual factor

    q_k>=5^b>=exp[((log5)/4)N−O(log N)].                     (20)

The available complete polynomial error in(18), or even the correction bound with exponent log5/8, does not certify a primitive small form against(20). Equations(12),(18) retain the exact signed possibility of cancellation; no lower bound for the old residual is claimed.

## Outcome

Allowing explicit dyadic rational coefficients does remove the apparent integral-scaling cost barrier. The resulting convergent e+pi family has actual denominator exactly the old odd part, a whole2^N saving, despite a written rational coefficient denominator of size2^(N/2+O(log N)). This is a proven arithmetic and representation improvement. The complete small-error/nonvanishing problem remains open, and no irrationality conclusion follows.
