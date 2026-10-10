> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of adjacent dual cross products and the deleted-row carrier

Date: 2026-09-13. Reviewer: audit_results.

Target: raw_adjacent_dual_cross_and_fixed_gcd.md by audit_sources.
Status: FULL PASS. No correction required.

I checked all ten sections, giving priority to the all-index deleted-last-row determinant, the sign of the origin vector, and the prime-power approximate-kernel argument. Frozen controls are saved as raw_adjacent_dual_cross_independent_controls.json. They use only the previously available degrees 1 and 2.

## 1. The deleted-last-row determinant is nonzero in every degree

The argument for (10) is valid for every r>=1. After division of rows k=r,...,3r-1 by k!, an exponential minor on row set E factors as

    (prod_(j<r)j!)/(prod_(k in E)k!) times det[binom(k,j)].

The last determinant is an integer. If E consists of consecutive rows, its value is exactly 1: the Vandermonde numerator and the leading-coefficient denominator prod j! agree. Thus the lower bound S(r)-sum_E phi(k), and equality on the proposed top set, have their correct factorial scales.

After reversing the arctangent columns, their entries are L(t^(k-r+j)), j=0,...,r-1, with L(t^a)=tau_(a+1). All row exponents k-r are nonnegative. The already established monic raw Legendre basis and its inverse triangular change of basis are dyadically integral in every needed degree. Expansion of an arbitrary row polynomial against the first r basis elements writes the moment matrix as an integral coefficient matrix times the diagonal norms. The norm valuations are 2phi(j); hence every such determinant has valuation at least 2S(r). For row exponents 0,...,r-1 the coefficient matrix is triangular with unit diagonal, giving equality. No negative moment or extra endpoint functional occurs.

For E0={2r,...,3r-1}, the complementary arctangent rows are exactly r,...,2r-1, so both bounds are attained. Every other size-r exponential row set replaces at least one row at or above 2r by one at or below 2r-1. Since

    phi(2r)-phi(2r-1)=v_2(2r)>0,

its lower valuation exceeds that of E0 strictly, regardless of factorial plateaus elsewhere or any vanishing minor. There is a unique least Laplace valuation, so it cannot cancel. Restoring all row factorials proves precisely

    v_2(Delta_r^0)=3S(r)+sum_(k=r)^(2r-1)phi(k).

This proves Delta_r^0!=0 without a perfectness assumption. The last cofactor has sign (-1)^(3r-r)=+1, so

    Q_r(0)=((3r)!/r!) Delta_r^0/F_r

has the sign and factor asserted in (11). In particular actual Q_r(0) is nonzero in every degree. This claim is stronger than the finite controls and is proved independently of them.

## 2. Adjacent cross product, degree, high order and endpoint signs

Write e_r=(0,R_e,r,R_a,r), so Y_r=Q_r f-e_r, f=(1,e^z,atan z). Expanding the cross product gives

    Y_n cross Y_(n+1)
      =Q_(n+1) f cross e_n
       -Q_n f cross e_(n+1)+e_n cross e_(n+1).

Every component has order at least M=3n+1 and degree at most 4n+2. Therefore division by z^M is integral and leaves degree at most n+1.

Taking its scalar product with f removes the first two terms. The last term gives exactly R_e,n R_a,n+1-R_a,n R_e,n+1. Its order is at least 2M+3; after division the order is M+3=3n+4, the required next-degree high order. This does not impose endpoint matching.

The ordinary cross-product signs give

    U_C(1)-4U_B(1)
       =Z_n(P_(n+1)(1)+4T_(n+1)(1))
        -(P_n(1)+4T_n(1))Z_(n+1).

Thus (7) is correct. Strictly increasing known dyadic valuations of the reduced endpoint denominators make this integer nonzero, so U is nonzero. Both terms are divisible by G_n G_(n+1), proving (8). Substituting Lambda_r=Z_r(e+pi)-N_r gives the sign in (9).

## 3. Primitive approximate kernel and the content term

For p>3n+3, both endpoint triples reduce modulo p^h to scalar multiples of (0,-4,1). Their cross product, and hence U(1), is zero modulo p^h. After dividing the integral content c and assuming h>s=v_p(c), the resulting polynomial triple is primitive and its endpoint values vanish modulo p^(h-s).

Monic division by z-1 over that quotient ring lowers its degree to at most n. The factor is a unit at the origin, so high Taylor order 3n+4 is preserved. The divided triple remains nonzero modulo p: multiplication by the nonzero polynomial z-1 cannot annihilate a nonzero polynomial triple over the residue field.

Its B,C coefficient vector is primitive. Otherwise the low equations would force every A coefficient to vanish modulo p as well. The divided A has degree at most n, and all necessary low Taylor denominators are units. This gives a primitive approximate right kernel of X_(n+1), with all its rows n+1,...,3n+3 retained.

For any square maximal submatrix M, Mv=0 modulo p^(h-s). The adjugate identity gives det(M)v=0; a unit coordinate of v forces p^(h-s)|det(M). It follows that v_p(F_(n+1))>=h-s, proving (2) with full depth. Neither maximal rank modulo p nor a single Smith exponent is assumed. The content term is retained exactly.

## 4. First-error scalars and the origin vector

Direct coefficient extraction at degree 3n+1 gives

    a_n=(1/n!)sum w_k/(k+1),
    b_n=(1/n!)sum k!w_k tau_(k+1).

The integer lcm through 3n+1 clears these denominators. Therefore I_n,J_n are integral and v_p(A_err)=min(v_p(a_n),v_p(b_n)) for p>3n+3.

If both first errors vanished over Q, multiplication of Y_n by z^2 would have the next allowed degree and high order 3n+4. Uniqueness of the next simultaneous space would make it proportional to Y_(n+1). This contradicts either the nonzero adjacent cross product or the just-proved nonzero Q_(n+1)(0). Hence A_err is a positive nonzero integer.

In the cross expansion above only Q_(n+1) f cross e_n contributes at order M. Since f(0)=(1,1,0),

    f(0) cross (0,a_n,b_n)=(b_n,-b_n,a_n).

This verifies (15), including its sign and the factor Q_(n+1)(0). The content of U divides each of its constant coordinates, giving (16). The possible rational denominators of a_n,b_n are units at the stated primes, not omitted arbitrarily.

## 5. Full-depth divisibility of A_err into Delta^0_(n+1)

If a_n,b_n vanish modulo p^t, then z^2Y_n satisfies every next simultaneous high condition modulo p^t. Its denominator is primitive modulo p because Q_n is primitive there. Under the reversed coefficient correspondence

    w_k = (r!/k!) [z^(3r-k)]Q,  r=n+1,

all factors are units for p>3r. The next simultaneous equations through degree 3r are precisely the left-kernel equations of X_r. This can also be checked directly: the exponential coefficient at 3r-j is (1/r!)sum (k)_j w_k, and the arctangent coefficient is (1/r!)sum k!tau_(k-j)w_k, for j<r.

The denominator z^2Q_n has zero constant coefficient, so this primitive left vector has last coordinate zero. Deleting that coordinate gives a primitive left annihilator of the square matrix whose determinant is Delta_r^0. Its adjugate forces p^t|Delta_r^0. This proves (3) at every depth; it is not merely a support argument.

Combining this with the previously checked inequality and Q_r(0)=((3r)!/r!)Delta_r^0/F_r, the factorial ratio being a p-unit, gives exactly (17) and (4). In particular the extremal content F_r is combined by an identity rather than silently set to one.

## 6. Exceptional support of the cross-product content

Modulo p>3n+3 both simultaneous triples are nonzero, have the proved maximum degrees, and have no common nonzero algebraic root among their coordinates. Their component gcds are therefore powers of z, up to scalars.

If their cross product vanishes, removing those powers gives primitive polynomial vectors proportional over F_p(z). Such primitive polynomial vectors differ by a nonzero constant, as follows from unique factorization or a coordinate Bezout combination. The difference of their maximum degrees is exactly two, so the original relation is Y_(n+1)=gamma z^2Y_n with gamma in F_p^times.

The next Taylor conditions then kill both first old error coefficients, since their shifted degree is 3n+3. All coefficients used are below p. This proves the support implication (18), and hence (20). The note correctly does not upgrade support to c|A_err.

## 7. Normalized determinant and heights

The sign in (21) is positive. Preserve the first r original rows and replace each of the following r rows by its rth forward difference. This is a triangular row transformation with diagonal 1. Its bottom exponential block vanishes; its top exponential determinant is prod_(j<r)j!. Its bottom arctangent block is exactly the stated G matrix. Scaling those r rows by L'_r/(r+i)! gives the stated Z minor, proving (21).

Every scalar factor removed in this identity is supported on primes at most 3r. Thus the localized replacement by B_r is valid with all exponents. The cited entry bounds control every relevant normalized minor, not only the displayed one.

The cofactor-transport formula bounds the primitive w coefficients by normalized minors times factorial ratios and binomial coefficients, of additional logarithmic size O(n log n); division by its positive integral normalizer can only reduce that bound. Therefore the cited n^2 log n+O(n^2) bound for their total absolute size follows. The estimate for A_err then costs only O(n log n) more. The final carrier bound 2n^2 log n+O(n^2) is correctly stated as no improvement over the available single-index endpoint height.

## 8. Frozen normalization controls and scope

The independent controls reconstruct the cross product only from the already saved Y_1,Y_2. They reproduce all three displayed U_1 polynomials, content 6, a_1=-1/4, b_1=-2, and endpoint mismatch -109938. The original matrices at those same two degrees give

    Delta_1^0=-1, F_1=1, Q_1(0)=-6;
    Delta_2^0=196, F_2=4, Q_2(0)=17640.

They confirm the positive last-cofactor convention and the factorial ratio. No additional degree or prime was examined.

The note passes in full. Its all-index constant-coefficient nonvanishing theorem is unconditional; its adjacent endpoint divisibilities retain the cross-product content and all prime powers. Neither isolated fixed-4 cancellation nor the signed analytic shrinking estimate is settled.

