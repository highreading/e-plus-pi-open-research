> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A pure-dyadic permitted pole and its complete real-error quantum

2026-10-02. Original structural author work after the shared-five correction. The target is an even-leading denominator with no odd endpoint norm, with full coefficient and error costs. It does not choose a rational center by approximating the unknown target.

## Prior-art gate and exact overlap

Archive queries covered the explicit polynomials `2w²−6w+5`, equivalent power notation, pure dyadic norm/quantum corrections, and Gaussian unit pole denominators. The archive's `sources/root_unity_gaussian_global_saturation_no_gain.md`, Sections1–3, was opened: it concerns saturation of another Wronskian lattice after Gaussian phase alignment. It supplies relevant background on dyadic Gaussian content but not this permitted differential correction. The returned `work/session_20260927/hp_b1_odd_dyadic_actual_numerator.md`, Sections1–3, was also opened: its b=1 denotes a different Hermite–Padé parameter, not the present pole translation. Current exactness, monic-gate and shared-five work are internal overlap. A bounded archive query finding no explicit formula is not a global novelty claim.

Fresh primary searches covered Gaussian rational approximation, restricted denominators, integer Chebyshev complex rational-point values and leading-coefficient/resultant bounds. Opened Pritsker, *Small polynomials with integer coefficients*, full paper https://arxiv.org/pdf/math/0101166, Theorem2.6 and proof: the basic complex rational-point integrality bound is classical. Opened Fischler–Rivoal, *Rational approximation to values of G-functions, and their expansions in integer bases*, full paper https://arxiv.org/pdf/1512.06534, Theorem2 and Corollary1. Restricted-denominator approximation is established theory, but those hypotheses do not establish an approximation bound for e+pi here and are not imported. The new work below is an exact controlled-pole realization and cost calculation. Rational rounding itself is not claimed novel.

## 1. Primitive quadratic with norm a power of two

Take

    Q(w)=2w²−6w+5=2[(w−3/2)²+1/4].

The coefficient content is1, its two poles are3/2±i/2, and neither meets the vertical path from(1−i)/2 to(1+i)/2. At a=(1+i)/2,

    Q(a)=2(1−i), Q′(a)=2(i−2).

For H_r=Q^(−r), the period-exact differential H_r″+H_r′ has no ordinary or exponential finite-pole residues. Its FULL endpoint effect is

    delta_r=4Im[H_r′(a)+H_r(a)]
           =2^(1−2r) Im[((1+2r)−i(1+r))(1+i)^(r+1)].       (1)

Thus every delta_r is a dyadic rational. Both H and H′ endpoint terms are present; an apparent additional norm factor is entirely dyadic and may not be treated as free real decay.

The exact four residue classes, for nonnegative integer ell with r>=1, are

    delta_(4ell)   = (−1)^ell (4ell)2^(1−6ell),
    delta_(4ell+1) = (−1)^ell (8ell+3)/2^(6ell),
    delta_(4ell+2) = (−1)^ell (3ell+2)/2^(6ell),
    delta_(4ell+3) = (−1)^ell (ell+1)/2^(6ell+1).            (2)

These follow from(1+i)^4=−4, not a finite experimental grid. For the middle classes the numerator's possible extra two-content is explicit. The second class has odd numerator and exact denominator2^(6ell).

## 2. A unit numerator with bounded integral coefficients

Assume5 does not divide ell+1. Let C1=8ell+3,C2=ell+1. Then

    gcd(C1,C2)=gcd(5,ell+1)=1.

Choose y in{−2,−1,1,2} with C2*y=1 modulo5, put x=(1−C2*y)/5, and set

    a_ell=−x, b_ell=8x+y.

The elementary identity5=8C2−C1 gives

    a_ell C1+b_ell C2=1,
    |a_ell|<=(2ell+3)/5, |b_ell|<=8(2ell+3)/5+2.             (3)

Consequently the integral-coefficient rational function

    H_ell=(−1)^ell[a_ell Q^(−(4ell+1))
                              +2b_ell Q^(−(4ell+3))]

has the exact FULL endpoint value

    4Im[H_ell′(a)+H_ell(a)]=2^(−6ell).                     (4)

No odd denominator or period is introduced. Equation(4) is a unit-valued endpoint identity, rather than an upper bound that could hide numerator cancellation.

For any actual dyadic precision tau>=1, choose ell>=ceil(tau/6), increasing it by at most1 if5 divides ell+1. Put j=6ell−tau. Then

    0<=j<=11,
    4Im[(2^jH_ell)′(a)+2^jH_ell(a)]=2^(−tau).              (5)

Its written denominator degree is8ell+6=(4/3)tau+O(1), with fixed primitive quadratic coefficient height6 and integral numerator coefficients O(tau). Thus nonmonic complex poles improve the polynomial-only degree needed to access a dyadic endpoint valuation. The real value in(5), however, is an exact dyadic quantum, not an extra exponential factor beyond that valuation.

## 3. Exact removal of the old dyadic factor

Let the OLD actual center be

    c=A/(2^tau B), A odd, B positive odd,
    gcd(A,2^tau B)=1,

with actual matched response U. Choose the centered integer representative z of the known-data congruence

    z B=A mod2^tau, |z|<=2^(tau−1).                        (6)

The representative is odd; either centered choice is permitted at a tie. Add the exact rational differential K=H″+H′ with

    H=U z2^j H_ell.

The e and pi responses are unchanged exactly, and no new pole periods appear. The complete center and its ACTUAL primitive denominator are

    c_z=c−z/2^tau=(A−zB)/(2^tau B),
    q_z=B, q_z/q=2^(−tau).                                (7)

The numerator is divisible by2^tau by(6). Every prime power of B survives because A is a unit at that prime and2 is invertible there. This includes the zero numerator case: zero forces B=1 under the original coprimality, and then q_z=1. No cancellation claim is based only on a convenient clearer.

The full signed error is EXACTLY

    E_z=S−c_z=E_old+z/2^tau,
    |E_z|<=|E_old|+1/2.                                   (8)

Hence the actual arithmetic saving2^tau costs a modular rounding displacement, bounded by1/2, whose smallness is NOT forced by increasing the pole depth. If E_old→0, convergence of c_z to S is equivalent to the specific condition

    z/2^tau→0.                                           (9)

The construction proves no such alignment for the reflected centers. If complete old and new errors are each at most exp(−sigma tau), then their exact difference in(8) requires

    |z|<=2 exp[(log2−sigma)tau].                           (10)

For sigma>log2 this is eventually impossible because z is a nonzero odd integer. This last statement has two explicit complete-error premises; it is not a lower bound for the original approximation error.

More simply, if |E_old|<=2^(−tau−1), the complete error obeys

    |E_z|>=2^(−tau−1), q_z|E_z|>=B2^(−tau−1).             (11)

This is the unavoidable dyadic quantum after removing the whole dyadic layer with a purely dyadic endpoint shift. The lower bound may itself tend to zero, and no irrationality consequence is asserted.

## 4. Full rational coefficient and pole costs

Write R=4ell+3. Then H_ell=(−1)^ell P/Q^R with P=a_ell Q²+2b_ell, degree(P)<=4 and coefficient height O(ell). Its correction has the exact rational numerator

    (P″+P′)Q²−(2R P′+R P)Q Q′
           −R P Q Q″+R(R+1)P(Q′)²,

over Q^(R+2), times the scalar(−1)^ell U z2^j. The numerator degree is at most7, its denominator degree8ell+10=(4/3)tau+O(1), and both finite-pole orders are at most R+2.

Because |z|<=2^(tau−1), j<=11, the scalar is at most1024|U|2^tau. The numerator coefficient height is O(|U|2^tau tau³), while the denominator coefficient height is at most13^(R+2), using the coefficient1-norm13 of Q. These costs are kept even though U cancels in the exact evaluated center formula(7).

## 5. Structural outcome

This pure-dyadic pole supplies an exact zero-odd-cost endpoint identity with controlled degree and integral coefficients, and removes an old dyadic denominator exactly. Its full correction does not inherit the exponentially small real shift available in the shared-five construction: the congruence coefficient consumes the same dyadic decay. Maintaining convergence becomes the specific modular alignment(9), which remains open. This is a structural description of the surviving denominator/error tradeoff, not an approximation method beyond rational rounding, and not a completed route to e+pi irrationality.
