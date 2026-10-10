> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual cost of an even-leading quadratic rational correction

2026-10-02. Original author research under the parent's even-leading-denominator steering. This is a distinct permitted-pole family, independent of the already excluded nlogn families. It acts on an arbitrary actual matched center and retains the complete final denominator.

## Prior-art gate

Archive queries covered even-leading/nonmonic denominators, Gaussian endpoint valuations, endpoint norm costs and dyadic corrections. Read `sources/root_unity_gaussian_global_saturation_no_gain.md`, Sections1–3: its phase-aligned Gaussian global image and endpoint content are related arithmetic background, but concern a different Wronskian lattice. Earlier correction exactness and the odd-leading/monic gate are explicit overlap. A bounded additional query for the particular quadratic coefficients and powers-of-five denominator formulas located no exact present correction construction in the prior selector archive. Search absence is not a novelty assertion.

Fresh primary searches concerned integer Chebyshev rational functions, Gaussian rational-point denominators, leading coefficients and prime valuations. Opened full primary Pritsker, *Small polynomials with integer coefficients*, https://arxiv.org/pdf/math/0101166, Theorem2.6 and its proof, and the author-hosted full paper https://math.okstate.edu/people/igor/intcheb.pdf, Sections1–2. The rational-point integrality/norm constraint is classical overlap. Opened the primary Granville text https://www.cecm.sfu.ca/organics/papers/granville/paper/binomial/html/node4.html for prime-power arithmetic background. None supplies the actual corrected-center denominator identity below.

## 1. Primitive quadratic and complete period elimination

Let b=2^s with s>=1, and define the PRIMITIVE integer polynomial

    Q_b(w)=2w²−2(1+2b)w+1+2b+2b².                 (1)

Its leading coefficient is2, its height is1+2b+2b², and its poles are c_b=(1/2)+b±i/2, strictly off the vertical path. Its numerator content is1. The unnormalized expression `4[(w−(1/2+b))²+1/4]` has content2; keeping that factor would create an artificial dyadic gain and is therefore avoided.

For r>=1 take H=Q_b^(-r) and add H″+H′ to a matched kernel. Both ordinary and e^w-twisted pole residues vanish EXACTLY, by `SIMULTANEOUS_EXACT_RATIONAL_CORRECTION_GATE.md`. Thus no additional constants appear. With a=(1+i)/2,

    Q_b(a)=2b(b−i), Q_b′(a)=2(i−2b).

Put M=b²+1 and

    Y_(b,r)=Im[(b²+2br−i(b+r))(b+i)^(r+1)]∈Z.

Direct endpoint evaluation gives the COMPLETE correction

    delta_(b,r)=4Im[H′(a)+H(a)]
       =2^[3−(s+1)(r+1)] Y_(b,r)/M^(r+1).         (2)

This retains the derivative and H endpoint contributions together. The rational denominator degree is2r and numerator degree0; the differential correction denominator divides Q_b^(r+2), still a controlled degree linear in r.

## 2. Exact Gaussian numerator arithmetic

If r is ODD then Y_(b,r) is odd. Indeed b=0 modulo2, and modulo2 the defining Gaussian expression is `−ri^(r+2)`, whose imaginary coordinate is odd precisely for odd r.

If an odd prime p divides M and p does not divide r, then p does NOT divide Y_(b,r). This includes higher prime powers in M, since the first-level unit already suffices. To prove it, work modulo p using the root i=−b of i²+1, which exists since b²+1=0. In the difference of the two conjugate expressions defining2iY, the `(b+i)^(r+1)` term vanishes. The other coefficient satisfies

    b²+2br+i(b+r)=br, b−i=2b,

so2iY is congruent to `−br(2b)^(r+1)`, a unit. Consequently

    gcd(r,M)=1 ⇒ gcd(Y_(b,r),M)=1.                 (3)

Under r odd and (3), define t0=(s+1)(r+1)−3, which is positive. The ACTUAL reduced denominator of delta is

    den(delta)=2^t0 M^(r+1).                      (4)

Thus a permitted nonreal pole can reach a large negative Gaussian valuation with small fixed leading coefficient, but its odd norm factor survives completely in the actual endpoint rational value. No generic denominator-free pole gain is obtained.

## 3. Actual corrected-center q, including coefficient content

Let c=A/(2^tau B) be an ACTUAL reduced center, A odd, B odd positive, gcd(A,2^tau B)=1, tau>=1. A matched kernel with response U realizes any correction below by the period-exact addition `U*k*2^j*(Q_b^(-r))″+U*k*2^j*(Q_b^(-r))′`; this notation means U*k*2^j times the derivative sum. It keeps the target responses exactly and subtracts k*2^j*delta from c. The dependence on U is explicit and cancels from the corrected center, not hidden in a generic clearing factor.

Choose odd r with gcd(r,M)=1 and t0>=tau, and put j=t0−tau. Then

    eta=2^j delta=Y/(2^tau M^(r+1)).

For integer k the FULL corrected center and ACTUAL q are

    c_k=[A M^(r+1)−k Y B]/[2^tau B M^(r+1)],
    q_k=2^tau B M^(r+1)/
           gcd(2^tau B M^(r+1),A M^(r+1)−kYB).     (5)

These equations apply whether or not any prime or dyadic cancellation occurs. The exact signed target error is `S−c_k=(S−c)+k eta`, so no real smallness follows from a congruence alone.

Assume additionally gcd(B,M)=1. Removing the ENTIRE old dyadic factor requires the concrete congruence

    k Y B=A M^(r+1) mod2^tau.                     (6)

All factors multiplied by k in (6) are units, so this fixes one odd residue class of k modulo2^tau. It does not involve the unknown S. Once (6) holds, every old B prime remains: the numerator is A M^(r+1) modulo that prime, a unit. At each M prime the numerator is −kYB modulo its complete M-power, with YB a unit. Therefore the ACTUAL final denominator is exactly

    q_k=B M^(r+1)/gcd(k,M^(r+1)).                 (7)

In particular if k is coprime to M, then q_k/(2^tau B)=M^(r+1)/2^tau>1. The inequality is strict since M=b²+1>2b=2^(s+1), while tau<=t0<(s+1)(r+1). Thus the full odd cost restores MORE than the removed dyadic factor in this unit-coefficient subfamily. This is an exact full-q comparison, not comparison of clearing multipliers.

More generally a bounded coefficient |k|<=K gives, under (6),

    q_k/(2^tau B)>=M^(r+1)/(2^tau K).             (8)

To avoid increasing the actual denominator, a necessary condition is

    K>=M^(r+1)/2^tau.

For fixed s and r chosen with t0=tau+O_s(1), this coefficient-content threshold has

    log K >= tau[log(b²+1)/(s+1)−log2]+O_s(1),    (9)

with a STRICT positive bracket. For b=2 it is log(sqrt5/2)>0. This is a quantitative degree/height tradeoff for this actual correction family; shared norm factors are priced in k, rather than assumed away.

If M divides B, (5) remains the complete formula but (7) does not apply; the actual old/new numerator content at those primes must be calculated. If gcd(r,M)>1, (2),(5) remain valid but the unit proof (3) does not apply. These are explicit surviving cases, not silently discarded prime exceptions.

## 4. Size and the remaining analytic obligation

The endpoint correction obeys the complete upper bound

    |delta|<=4 |Q_b(a)|^(−r)
                      [1+r |Q_b′(a)/Q_b(a)|],
    |Q_b(a)|=2b sqrt(b²+1),
    |Q_b′(a)/Q_b(a)|=sqrt(4b²+1)/[b sqrt(b²+1)].   (10)

For fixed s, r grows linearly with the dyadic precision tau. Bounded small k can yield an exponentially small real translation, but (7)–(9) prove that it increases the actual denominator if the odd norm cost is not paid by coefficient content. Coefficients with enough odd norm content can change this conclusion; (5) and the signed error retain their exact effect. No bound on the COMPLETE target error, and no solution or all-even-leading-denominator exclusion, is inferred from (10).

## 5. Fixed quadratic degree: an explicit positive endpoint formula

Taking r=1 removes any possible Gaussian phase cancellation. Then

    Y=b³+3b²+b+1>0,
    delta=Y/[2^(2s−1)(b²+1)²].                    (11)

For any requested dyadic precision tau>=1 choose

    s=ceil((tau+1)/2), j=2s−1−tau∈{0,1}.

The denominator degree is only2, and eta=2^j delta=Y/[2^tau M²]. Its primitive quadratic coefficient height is explicit:

    height(Q_b)=1+2b+2b²,
    log2(height(Q_b))=tau+O(1),
    log2(M²)=2tau+O(1).                            (12)

Thus fixed degree can supply the requested valuation only through exponentially growing pole/coefficient height, and the odd endpoint denominator is quadratic in that height. Under gcd(B,M)=1 and complete dyadic cancellation (6), the ACTUAL q comparison is

    q_k/(2^tau B)=M²/[2^tau gcd(k,M²)].            (13)

With |k| bounded or exp[o(tau)], (13) grows like exp[(log2+o(1))tau]; there is no primitive denominator reduction. Avoiding that increase requires |k|>=M²/2^tau=exp[(log2+o(1))tau] in norm content. Complete cancellation of the odd norm requires M²|k and hence log2|k|>=2tau+O(1), with the dyadic congruence still imposed.

There is also a COMPLETE small-error consequence with a precise premise, rather than a bare denominator comparison. Suppose the old actual signed error E=S−c obeys |E|<=eta/2. For every nonzero integer k satisfying full dyadic cancellation, including coefficients with norm content,

    |S−c_k|>=|k| eta/2,
    q_k |S−c_k|>=B |k|Y/[2^(tau+1)gcd(k,M²)]
                    >=B Y/2^(tau+1)>=B b.         (14)

Here Y>=b³ and 2^(tau+1)<=b². This last inequality is uniform for both possible parity choices of tau. It shows that this positive fixed-degree correction destroys a pre-existing error smaller than its own quantum, even when all its available odd norm content is used. It does not address old errors comparable to k eta, where real cancellation may occur. That residual approximation question remains explicit.

## 6. Shared old norm: exact tied and untied formulas at5

The coprime B,M premise is a material restriction: existing odd denominator content can absorb some pole cost. The following resolves that interface exactly, without inferring an actual prime depth from a raw factorial clearer.

Fix b=2, so Q=2w²−10w+13 and M=5. Choose an ODD r>=ceil((tau+1)/2) with5 not dividing r, taking the least such value, and put

    d=r+1, t0=2r−1, j=t0−tau.

Then0<=j<=7, d=tau/2+O(1), and the same endpoint numerator Y is odd and a5-adic unit. The scaled correction is

    eta=Y/(2^tau5^d).

Write the ACTUAL old center c=A/(2^tau B) with B=5^b5 B0, gcd(B0,5)=1. Let L=lcm(B,5^d). For integer k the COMPLETE denominator is

    q_k=2^tau L/gcd(2^tau L,
                       A L/B−kY L/5^d).           (15)

Full dyadic cancellation is the concrete unit congruence

    kY L/5^d=A L/B mod2^tau.                     (16)

It fixes an odd class k modulo2^tau. One can choose a representative with5 not dividing k and |k|<=(5/2)2^tau, by testing five consecutive representatives of this SAME class. This is deterministic cancellation of known rational data; it does not tune a center to the unknown S.

With that unit choice, every prime of B0 survives unchanged in the full numerator. If b5!=d, the two5-adic numerator orders are unequal and the smaller term is a unit. Thus the ACTUAL reduced denominator is

    q_k=B0·5^max(b5,d),
    q_k/q_old=5^max(d−b5,0)/2^tau.                (17)

If b5=d, the tied case is retained exactly:

    q_k=B0·5^max(0,b5−v5(A−kYB0)).               (18)

Zero numerator is assigned infinite valuation, so (18) includes a zero corrected center without division by it. Tied extra content can only improve the old5-depth; it is not assumed generic or absent.

For d=tau/2+O(1), (17) gives a strict actual denominator gain whenever

    b5 > [1/2−log2/log5]tau+O(1),
    1/2−log2/log5=0.0693234419... .                (19)

This is a GENUINE surviving arithmetic mechanism: the old actual norm depth can pay enough of the new pole cost to remove the dyadic layer. The value b5 must come from the COMPLETE original evaluated numerator/shared-response gcd. In particular v5(N!)≈N/4 in a convenient clearer is not substituted for it. The arithmetic agent has been assigned that separate actual-depth target.

## 7. Full error and coefficient costs in the shared5 mechanism

For the explicit unit representative above, the exact shift is k eta. The COMPLETE endpoint bound (10), with |Q(a)|=4sqrt5 and |Q′(a)/Q(a)|=sqrt17/(2sqrt5)<1, proves

    |k eta|<=5(r+1)5^(−r/2)
             <=5(r+1)5^(−(tau+1)/4).             (20)

Indeed tau+j=2r−1, so the full2^tau coefficient allowance and the scaling2^j cancel exactly against4^r in the norm bound. The shift is exponentially small in the old dyadic precision, including the derivative endpoint term. There is no hidden term from either conjugate endpoint or a new pole period.

The full target error satisfies EXACTLY

    E_k=S−c_k=E_old+k eta,
    |E_k|<=|E_old|+5(r+1)5^(−r/2).                (21)

Multiplying (21) by the ACTUAL q in (17) or (18) gives the complete primitive upper bound. Neither denominator reduction nor the exponentially small shift makes that upper bound small automatically: old non-dyadic content and the actual old error still enter. If |E_old| exceeds twice the right-hand shift allowance, its eventual sign and relative size are preserved. If it is comparable to or smaller than the shift, the exact signed expression in (21) must be used; exceptional cancellation is not excluded by spacing or by a norm upper bound.

In kernel normalization the correction is H=U k2^j Q^(-r). Its scalar coefficient obeys

    |U k2^j|<=320 |U|2^tau.

The correction H″+H′ has the explicit rational form

    U k2^j · r[(r+1)(4w−10)²−(4w−6)Q(w)]/Q(w)^(r+2). (22)

Its numerator degree is3 and its denominator degree2r+4. The numerator coefficient height is O(|U|2^tau r²), and the denominator coefficient height is at most25^(r+2), since the coefficient1-norm of Q is25. All these costs are explicit; the center's U cancels only through the exact evaluated formula (15), not by treating a large written coefficient as harmless.

Applied to the analysis agent's critical quadratic centers, tau is their ACTUAL denominator valuation v2(N!)+v2(U), and (20) is exponentially small on the N-scale. It preserves their known convergence c→S, but their proved O(n^(−1/2)) or depth-mesh O(n^(−3/2)) error does not become exponentially small. No primitive small-form conclusion follows without that stronger complete error or a proven cancellation.

This target has therefore produced a permitted pole, exact valuation access, uniform odd-prime survival, and a full-q/content/height/error interface. The remaining assigned question is actual old5-depth; a separate controlled cancellation of the real residual remains open. Arbitrary rational tuning of the center is not counted as progress.
