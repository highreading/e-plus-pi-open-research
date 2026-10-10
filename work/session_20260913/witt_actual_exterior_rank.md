> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual first-Witt exterior state: a six-exception rank theorem

2026-09-13. New exact auxiliary theorem. This addresses the actual endpoint state, with its characteristic-p Frobenius ambiguity retained explicitly. It does not use a phase-period continuation, fixed-prime experiment, or presumed nonzero seed.

## 1. The theorem and precise range

Let p be prime and let j>=0, s>=1, r>=12 satisfy

    p=2r+6s+3, 3j+1<p, 2j+2<p.

For j>=1 the second inequality follows from the first; it is automatic for j=0 in this range. Put u=x(1-x), Q=(1+x)(1+x^2). For k=0,1,2 let T_k be the unique zero-constant primitive of degree less than p of

    P_k=u^(r-6k)Q^(2s+4k).

All three P_k have degree p-3, so the primitives exist and have degree at most p-2. They are exactly the Item426 nu=0 primitives in three consecutive actual rows.

Define the integer sextic

    S_6(r)=176275r^6-6297825r^5+89867547r^4-649457253r^3
                         +2470644018r^2-4573809342r+3062922660.

If S_6(r)!=0 modulo p, the four vectors indexed by zeta^4=1,

    (T_0(zeta)), (T_1(zeta)), (T_2(zeta)), (zeta^p),

are linearly independent. Here T_1 and T_2 label shifted nu=0 rows, not the nu=1 differential.

Consequently the three Item426 endpoint-coordinate vectors

    E_j(H_0(r)), E_j(H_0(r-6)), E_j(H_0(r-12))

form a basis of F_p^3. In particular the actual states

    (L_j(H_0(r)),L_j(H_0(r-6)),L_j(H_0(r-12))),
    (R_j(H_0(r)),R_j(H_0(r-6)),R_j(H_0(r-12)))

are independent. Their exterior product is nonzero. At each fixed p there are at most six r in this range where the exterior state can vanish, since S_6 has degree six and integer content one.

## 2. From a rank failure to a bounded polynomial identity

Suppose the four evaluation vectors are dependent. There exist c_0,c_1,c_2,delta in F_p, not all zero, for which

    W(x)=c_0T_0(x)+c_1T_1(x)+c_2T_2(x)-delta x^p

vanishes at every fourth root of unity. At least one c_k is nonzero, because the vector (zeta^p) is nonzero. Also W(0)=0 and deg W<=p. Its derivative is

    W'=u^(r-12)Q^(2s)
                       [c_0u^12+c_1u^6Q^4+c_2Q^8].       (1)

At 0 and1 the derivative has order at least r-12. Since r-11<p, the vanishing of W itself forces order at least r-11 there. At each root of Q the derivative has order at least2s; since2s+1<p, the corresponding order of W is at least2s+1. This local statement remains valid in characteristic p: all relevant Taylor coefficients are multiplied on differentiation by integers strictly between0 andp. A possible local p-th-power term has still higher order and cannot invalidate the divisibility.

The two factors are coprime. Hence

    u^(r-11)Q^(2s+1) divides W.

Their product has degree

    2(r-11)+3(2s+1)=p-22.

Since deg W<=p, there is a polynomial A with deg A<=22 such that

    W=u^(r-11)Q^(2s+1) A.

Differentiating and comparing with(1), then cancelling u^(r-12)Q^(2s), gives

    c_0u^12+c_1u^6Q^4+c_2Q^8
       =uQ A'+[(r-11)Qu'+(2s+1)uQ']A.

The actual row relation gives2s+1=-2r/3 modulo p. Thus a rank failure supplies a nonzero solution of the exact coefficient system

    3uQ A'+[3(r-11)Qu'-2r uQ']A
                      -3(c_0u^12+c_1u^6Q^4+c_2Q^8)=0.  (2)

The Frobenius term delta x^p was essential in this argument. It was neither set to zero nor confused with a literal homogeneous recurrence for the chosen zero-constant primitives.

## 3. The exact determinant

Write A=sum_(h=0)^22 A_h x^h. In (2), coefficients through x^25 give a26 by26 linear system in

    A_0,...,A_22,c_0,c_1,c_2.

The apparent x^26 coefficient vanishes identically: for A=x^h the highest coefficient is3(22-h), so the top case h=22 cancels. Every matrix entry lies in Z[r].

Its determinant, with rows ordered x^0,...,x^25 and columns as displayed, is exactly

    -2^38*3^13*5^2 * r^2*(r-11)*(r-10)*(r-9)*(r-8)*(r-7)*(r-6)
       *(r-3)^2*(r-1)*(2r-21)*(2r-15)*(2r-9)^2*(2r-3)^2 * S_6(r).  (3)

The companion program check_witt_actual_exterior_rank.py constructs every matrix column directly from(2), computes its determinant over Z[r], and checks the expanded difference from(3) is the zero polynomial. The complete matrix and its canonical serialized hash are saved in witt_actual_exterior_rank_certificate.json. This is an exact symbolic determinant; it is not a value interpolation or a fitted operator.

On an actual row r>=12, p=2r+6s+3 with s>=1, we have p>=37 and

    0<r-a<p for a=0,1,3,6,7,8,9,10,11,
    0<2r-a<p for a=3,9,15,21.

Thus the scalar and every displayed linear factor in(3) are units. If S_6(r)!=0, (2) has only the zero solution, contradicting the nonzero c vector. This proves the evaluation-rank theorem. The gcd of all seven coefficients of S_6 is1; its reduction is never the zero polynomial for any prime, even if the leading coefficient reduces to zero. It therefore has at most six roots modulo p.

## 4. The exact endpoint quotient and its j=0 extension

The canonical source is sources/item194_rankzero_pnt_report.md, Sections4.1-4.2, equations(4.4)-(4.9). It proves the following for the ordinary j>=1 rows. The same proof applies at j=0, as detailed here.

Let V be the four-dimensional space of polynomials H of degree at most4 with H(0)=0. Set

    D_j=(3j+1)-(5j+2)(x+x^2+x^3)+x^4,
    G_j=uQ+xD_j=(3j+2)x-(5j+2)(x^2+x^3+x^4).

The four-section construction is characterized by

    H(zeta^p)=D_j(zeta)T(zeta), zeta^4=1.             (4)

Evaluation on these four distinct points is an isomorphism after adjoining i; over F_p, its target is the four-dimensional algebra F_p[x]/(x^4-1), so the same rank statement descends. The factors D_j(1)=-4(3j+1) and D_j(-1)=D_j(i)=D_j(-i)=4(2j+1) are units in the stated range. Thus(4) is an invertible map on evaluation vectors. The Frobenius vector T(zeta)=zeta^p maps exactly to G_j, because uQ=x-x^5 vanishes on these endpoints and D_j(zeta)=D_j(zeta^p).

The endpoint map E_j=(R_j,L_j,E_j) is the mixed-cubic coordinate map of

    u^(3j)H/Q^(2j+2) dx.

It has kernel exactly F_p G_j. One inclusion follows from

    u^(3j)G_j/Q^(2j+2) dx
                    =d[x u^(3j+1)/Q^(2j+1)],

whose primitive vanishes at0 and1. For the converse, zero logarithmic and circular coordinates mean all finite residues vanish. All finite pole orders are at most2j+2<p, so a rational primitive exists by ordinary partial fractions, without any resonant p-th-order pole. The differential is proper at infinity; choose a primitive finite there. Zero rational endpoint means its values at0 and1 are equal. Subtracting that common value gives zeros of order at least3j+1 at both endpoints, poles of order at most2j+1 at Q's roots, and a finite value at infinity. Therefore the primitive has the form

    u^(3j+1)(alpha+beta x)/Q^(2j+1).

Since H(0)=0 and3j+1 is a unit, its derivative forces alpha=0. Thus H is a scalar multiple of G_j. All statements hold for j=0: the endpoint zero order is1, finite pole orders are2<p, and3j+1=1. This explicitly extends the rank-three quotient to that cell.

Consequently evaluation independence of T_0,T_1,T_2,Frobenius implies independence of H_0,H_1,H_2,G_j. Their three quotient classes form a basis of V/F_p G_j. Since E_j induces an isomorphism of that quotient with F_p^3, its three coordinate vectors form a basis. Two coordinate rows, in particular the R and L rows, must therefore be independent. This is exactly the nonzero exterior state needed in the recurrence argument.

## 5. Relation to the recurrence and scope

There is also a fixed-start corollary without any character calculation. At s=1 or2, the actual r reduces modulo p to -9/2 or -15/2 respectively, and direct exact evaluation gives

    S_6(-9/2)=3^6*7*17*134854903/64,
    S_6(-15/2)=3^8*5^2*41*8712533/64.

Thus either permitted-parity start is a nonzero exterior state outside its displayed finite prime set (and the finite r<12 range), uniformly in every admissible j. This corollary is weaker than the direct six-exception theorem for the density argument, but it independently answers the fixed-seed question without enumerating algebraic character choices.

The projected order-three recurrence and contiguity from witt_exterior_recurrence_attempt.md must be understood after applying E_j. Raw zero-constant primitives can differ by a multiple of x^p when a telescoping primitive has degree p. The quotient theorem above shows that this ambiguity is killed exactly by E_j, so it is compatible with the projected system. The present rank proof already works modulo that ambiguity from the beginning.

The theorem supplies an actual O(1) bound on zero full exterior states. In combination with the independently checked projected recurrence, cyclic limiting observation, and non-root-of-unity eigenvalue ratios, it supplies the previously missing state hypothesis of the progression-density method. Poles of a chosen rational observation or transfer still require their explicit bounded-degree exception count; they do not justify silently using a singular companion. No appeal to continuation of a characteristic-zero period is needed for the actual state bound.

No unbounded valuation-depth estimate follows from this rank theorem. A density theorem for the first-Witt support must continue to be distinguished from any summation over all Witt depths or any final irrationality claim.
