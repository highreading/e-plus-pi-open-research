> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Two-depth shared-five endpoint lattice with full error and primitive q

2026-10-02. Original author mathematics by agent3. This is a distinct extension of the one-depth correction mesh, using two permitted rational powers with the same inherited old norm support. All ordinary and exponential period elimination is attributed to the selector's exact differential construction. The full endpoint combination, actual denominator, coefficient costs and remaining nearest-node issue are retained.

## 1. Fresh gate and overlap

Before deriving this target, archive queries searched `(Y_r|Y_(b,r)|Gaussian.{0,30}endpoint).{0,80}(gcd|Bezout|Bézout|two|adjacent)`, `correction.{0,40}(two.depth|Bezout|Bézout|endpoint lattice)`, and `two.{0,15}correction.{0,15}(mesh|lattice)`. The precise internal overlap is the selector's `PURE_DYADIC_POLE_EXACT_QUANTUM.md`, which was read in full: it combines powers of the DIFFERENT quadratic2w²−6w+5 to obtain an exact purely dyadic quantum. It does not have the present inherited5-depth or polynomially bounded gcd of the present endpoint integers. That source explicitly identifies ordinary rational rounding as a remaining issue, which is retained here. The one-depth mesh note is additional exact overlap. These bounded searches do not establish global novelty.

Fresh primary queries were `site:arxiv.org Gaussian powers Lucas sequence polynomial coefficients gcd consecutive terms Bezout` and `site:arxiv.org rational approximation endpoint lattice integer linear combination Hermite Pade`. Opened https://arxiv.org/pdf/math/0510278, https://arxiv.org/pdf/1505.07147, https://arxiv.org/pdf/1409.4053 and https://arxiv.org/pdf/2201.06829 . The Hermite–Padé common-denominator and adjacent-index literature supplies related lattice/determinant background; its general results are not imported as a theorem about this actual corrected center. The logarithmic-phase estimate needed for coefficient size is the already derived `SHARED_FIVE_COMPLETE_COEFFICIENT_MESH.md`, using the read primary complex-logarithm inequality of Sha Section2.4.

## 2. A polynomial bound for the endpoint gcd

Let r and r+2 both be odd and not divisible by5, and put

    d=r+1, D=r+3=d+2,
    Y_r=Im[(4+4r−i(r+2))(2+i)^d].                (1)

Write u+iv=(2+i)^d. Then EXACTLY

    Y_r=(4r+4)v−(r+2)u,
    Y_(r+2)=(16r+52)v+(13r+36)u.                 (2)

The rational integers u,v are coprime. Indeed any common rational prime would divide u²+v²=5^d, so it would be5. But in Z[i], the relatively prime Gaussian primes2+i and2−i lie above5;5 cannot divide (2+i)^d. Thus5 cannot divide both u,v.

The determinant of the two coefficient rows in(2) is

    4(17r²+70r+62).                             (3)

Since each Y is odd and5-unit by the selector's exact endpoint arithmetic, the positive integer

    g=gcd(25Y_r,Y_(r+2))=gcd(Y_r,Y_(r+2))

is odd,5-unit and obeys

    g | 17r²+70r+62, 1<=g<=17r²+70r+62.          (4)

For the divisibility, a common divisor of the two linear forms divides the determinant times u and v; their coprimality removes u,v. Its oddness removes the factor4. Thus the exponential Gaussian phase numerators can have only polynomial common content at these two depths.

## 3. Exact full center at the inherited actual denominator

Use the selector's primitive Q=2w²−10w+13 and actual old reduced center

    c=A/(2^tau B), B=5^b B0, gcd(A,2^tau B)=1.

Assume D<b. Two rationally scaled period-exact corrections give the COMPLETE combined shift

    J/(2^tau5^D),
    J=25k1Y_r+k2Y_(r+2), k1,k2 integers.         (5)

By Bézout, J ranges over gZ. Complete dyadic cancellation is precisely

    J B0 5^(b−D)=A mod2^tau.                    (6)

Since g is odd, this fixes one odd class ell=J/g modulo2^tau. Let ell0 be its centered representative, |ell0|<=2^(tau−1). Then

    J=g(ell0+2^tau m), m integer,
    c_m=c−J/(2^tau5^D),
    E_m=e+pi−c_m
       =E_old+g ell0/(2^tau5^D)+m g/5^D.        (7)

Both full endpoint terms are present in(5); no term is estimated separately and dropped. The period-exact rational kernels retain the actual old response U.

The actual primitive denominator is EXACTLY

    q_m=B,                                     (8)

for every m. To see the content directly, write the reduced numerator after(6) as

    [A−J B0 5^(b−D)]/2^tau.

It is a5-unit because D<b and A is a5-unit. It is a unit at every prime of B0 because the correction term contains B0 and A is coprime to it. Thus the old odd denominator survives unchanged after full reduction, while the entire old dyadic factor disappears. No coefficient clearer is identified with q_m.

The complete center now has SIGNED mesh

    Omega=g/5^D,
    log Omega=−D log5+O(log D),                  (9)

which improves the one-depth phase quantum by an exponential factor5^(D/2), at the SAME inherited actual odd denominator. This is a complete endpoint lattice result, not merely a formal difference of modulus bounds.

## 4. A bounded known-data shift and its coefficient cost

The m=0 representative in(7) is computed entirely from the old rational center and the known integers Y. It obeys

    |c_0−c|<=g/(2·5^D).                         (10)

Thus it removes2^tau while preserving any established convergence of the old center, with a substantially smaller shift than the one-depth norm estimate. It has not used the unknown target error to tune ell0.

Let a=25Y_r and b1=Y_(r+2). For any J in gZ choose k1 centered in its necessary residue class modulo |b1|/g, then k2=(J−a k1)/b1. This gives actual integer coefficients satisfying(5) with

    |k1|<=|b1|/(2g),
    |k2|<=|J|/|b1|+|a|/(2g).                  (11)

The one-depth primary-logarithm phase bound gives |Y_(r+2)|=5^(D/2) exp[O(log²D)], and the modulus upper bound gives |25Y_r|<=5^(D/2)exp[O(log D)]. For J=g ell0, (11) yields

    max(|k1|,|k2|)
       <=exp[max((D/2)log5,
                  tau log2−(D/2)log5)+O(log²D)]. (12)

This is an upper bound, not a claimed lower bound for these particular Bézout representatives. It explicitly prices the phase cancellation needed to make the endpoint shift(10).

The full common-denominator rational function realizing(5) is

    H=U 2^(2d−3−tau)
             [k1 Q(w)²+16k2]/Q(w)^(r+2).        (13)

Adding H″+H′ preserves the ordinary and exponential period responses exactly by the selector's construction. Its numerator degree is at most4 before differentiation, denominator degree2r+4, and after differentiation the denominator divides Q^(r+4) with degree2r+8. Both conjugate endpoint effects in H′+H give(5).

The polynomial coefficient content of P_k=k1Q²+16k2 must be retained in its rational scalar. With c2=min_j v2([w^j]P_k), its EXACT written coefficient dyadic denominator exponent is

    max(0,tau−2d+3−v2(U)−c2).                 (14)

For the cancelling odd J, k1+k2 is odd and P_k is nonzero. Its c2 is between0 and6: the nonconstant coefficients of Q² have common two-content4, and the constant coefficient169 is odd; if k1 has two-valuation4, the remaining tie cannot exceed the nonconstant minimum6. The polynomial numerator height is bounded by O(|k1|+|k2|), since Q is fixed. Multiplication by the scalar in(13), and the explicit rational denominator(14), prices its full rational coefficient height. No reduction of written coefficient height is substituted for the actual q saving(8).

## 5. Real tuning and the remaining primitive-width problem

Using the actual complete E_old, choose m nearest to −E_old/Omega−ell0/2^tau. Then

    |E_m|<=g/(2·5^D).                           (15)

This latter selection uses the target residual; it is ordinary rounding in the exactly realized lattice, not an approximation theorem supplied by congruence(6). The two consecutive m values bracketing zero have errors whose absolute values sum to Omega, so their farther node has

    |E_far|>=Omega/2,
    q_far|E_far|>=B0·5^(b−D)g/2.               (16)

There is again **no lower bound for the nearer node**. Exceptional closer alignment or equality is not excluded.

If E_old is nonzero and log|E_old|=o(D), a rounding value of J has |J|=2^tau5^D|E_old|(1+o(1)). Equation(11) and its elementary converse |J|<=(|a|+|b1|)max|ki| show that efficient coefficients satisfy

    log max(|k1|,|k2|)
          =tau log2+(D/2)log5+o(D).             (17)

Thus the stronger two-depth mesh can be reached without a larger leading exponential coefficient cost than the one-depth real-rounding construction. The full scalar and its coefficient denominator remain(13)–(14).

On the reflected N=2^s inverse-critical subsequence, one may take the greatest admissible even D<=v5(N!)−1 with r=D−3 and r+2 both5-units. The gaps between admissible D are bounded by6, so

    D=N/4−O(log N)<b,
    q_m=q_old/2^N,
    |c_0−c|<=exp[−(log5/4)N+O(log N)].           (18)

The known-data m=0 representative therefore preserves the full O(N^(−1/4)) convergence, and optional real rounding improves the complete error upper bound to exp[−(log5/4)N+O(log N)] at that actual odd q. In this regime(12) gives bounded-shift coefficients of logarithmic size at most

    [log2−(log5/8)]N+O(log²N),                 (19)

whereas the natural scalar in(13) has logarithmic modulus above |U| at most

    [(log2/2)−(log5/8)]N+O(log²N).              (20)

Its dyadic coefficient denominator is still approximately2^(N/2), explicitly counted in(14); the small scalar modulus is not a denial of that rational height.

For the rounded center the mesh multiplied by actual q is B0·5^(b−D)g. This need not tend to zero, even if no additional norm-depth cost is introduced. If actual b−D is bounded and B0=1, the guaranteed rounding upper bound has only a bounded primitive size; if B0 is large, the available upper bound retains it. The main remaining problem is closer real alignment at this inherited congruence grid, together with actual denominator support. No primitive residual tending to zero, nonvanishing theorem, or rationality statement follows from(15) or(18).
