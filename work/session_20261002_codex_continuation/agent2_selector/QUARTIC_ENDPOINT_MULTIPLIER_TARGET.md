> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Target-preserving quartic endpoint multiplier

2026-10-02. Original author research after the parent's arithmetic steering. The completed nonzero-block theorems are preserved. This target asks whether a polynomial in the half-step shift can suppress both complex endpoint modes while retaining a nonzero coefficient of e+pi, and whether the full arithmetic cost permits a better rate. No irrationality claim is made.

## Search and overlap recorded before calculation

Archive searches covered `endpoint.*annihilat`, `annihilat.*endpoint`, endpoint elimination/projection, target-preserving combinations, and the explicit factors `1+4w`, `1+4x`, `z^2-2z+2`, quartic selector, and endpoint multiplier over the work archive. The direct-selector height-obstruction draft and complete odd-prime arithmetic note were read. The former applies to arbitrary integer selectors; the latter already gives the complete high-prime numerator gate, so merely deleting the top n moment poles by Lucas' theorem would duplicate a weaker component of that work. The scalar contiguous note warns that a homogeneous annihilator may erase the coefficient of e+pi. Other hits for z^2-2z+2 concern the arctangent differential equation and a different Hermite–Padé family. This bounded search found no present quartic multiplier family.

Online primary-paper searches: Hermite–Padé exponential/logarithmic endpoint error elimination; integer Chebyshev polynomials on complex segments; rational approximation of pi by polynomial endpoint multipliers. Opened full primary sources:

- Doliwa and Siemaszko, *Hermite–Padé approximation and integrability*, https://arxiv.org/pdf/2201.06829, Sections 1.4 and 3. General rational recurrence and projective transformations are classical overlap; they do not prove an arithmetic gain for this family.
- Shvets, *Order-3 pi-formulas, Apéry-like kernels, and Clausen functoriality for Conservative Matrix Fields*, https://arxiv.org/html/2604.09723v1, Lemma 3.1 and Remark 3.2. The coefficient-sum test for an S-1 right factor is classical overlap and motivates retaining the exact target response here.
- Pritsker, *Small polynomials with integer coefficients*, https://arxiv.org/pdf/math/0101166, Sections 1–2. Polynomial factor powers and weighted sup-norm optimization are classical. Its real-set weighted-capacity conclusions are not being applied to this complex contour without their hypotheses.
- Van Assche, *Padé and Hermite–Padé approximation and orthogonality*, https://arxiv.org/pdf/math/0609094, Sections 1.3–1.5. Classical integral error formulas overlap; no positive-measure representation for the actual complete contour is inferred.

A Hata primary PDF request at https://matwbn.icm.edu.pl/ksiazki/aa/aa63/aa6344.pdf returned an internal error, so that full text is not counted as read. The opened papers above suffice for the initial distinct target.

The new calculations concern the actual selector, forcing normalization, full exponential tail, actual logarithmic companion denominator, and simultaneous contour bound. A favorable raw contour bound alone will not be described as a denominator improvement.

## 1. Exact target-preserving family

Let n=4k, r=n/2, and h,b≥0 integers. Put

    A(t)=1−2t+2t², C(t)=1−4t+2t²,
    D(t)=C(t)²+2C(t)+2=1+4(1−t)^4,
    B_(h,b)(t)=A(t)^n C(t)^h D(t)^b,
    N=2n+2h+4b, J=N−n,
    K=t^n B^(n)/n!, U=K(1), T=calL((K−U)/(t−1)).

All are the actual direct-selector objects. On U≠0 define

    α=U^(-1) Σ_(j=n)^N binom(j,n)b_j E_j,
    β=T/U, c=α+β.

The complete identities give coefficient one for e+pi in c. At t=1+x,

    U=(-1)^h u_(n,b)(h),
    u_(n,b)(h)=[x^n](1+2x+2x²)^n(1−2x²)^h(1+4x^4)^b.

For fixed b, u is a polynomial of degree r in h with positive leading coefficient 2^r/r!. In the diagonal b=h, define instead

    v_n(h)=[x^n](1+2x+2x²)^n
                    [(1−2x²)(1+4x^4)]^h.

This too has degree exactly r with the same leading coefficient: the lowest nonconstant degree in the bracket is two. Thus every r+1 distinct h arguments contain a nonzero response even on this diagonal. There is no all-integer response claim.

Equivalently, for fixed b the transformation on the signed forcing mode and numerator is ψ(S)^b, ψ(z)=z²−2z+2=1+(z−1)². It multiplies the contour by D(1−w)=1+4w^4. Because ψ(1)=1, it does not annihilate the leading polynomial forcing mode. Its coefficients have absolute sum 5^b and have signed sum one. The actual unsigned centers use their response weights, rather than a bare unweighted average. No division by an individual old U value is needed to construct the new B.

## 2. Full exponential tail and actual companion denominator

The polynomial B(−t) has nonnegative coefficients. Coefficientwise,

    A(−t) ≤ exp(2t), C(−t) ≤ exp(4t),
    D(−t)=5+16t+24t²+16t³+4t^4 ≤5exp(16t/5).

For the last inequality the coefficients at degrees 0 and 1 agree, and direct rational comparison proves the inequalities at degrees 2, 3, 4; all higher right-hand coefficients are positive. Therefore, with

    Λ=2n+4h+16b/5,

the complete exponential-tail argument proves

    0<|e−α|<3·5^b Λ^n exp(Λ/(n+1))
                    /[(n+1)(n!)²|U|].                    (1)

The strict lower inequality uses rationality of α and irrationality of e. No omitted Taylor tail or old even-exponent dyadic endpoint allocation is assumed.

Every degree-j coefficient of B has 2-adic valuation at least ceil(j/2). This is preserved by D because its coefficients have valuations 0,4,3,4,2 in degrees 0,1,2,3,4; each meets the required bound. Hence 2^r divides U and the full rational T has v_2(T)≥1. The actual logarithmic companion satisfies

    den(β) divides O_N |U|/2.                            (2)

This is an upper bound for the denominator after rational reduction, not an equality or a lower bound for the final center. If q=den(c), and C_ε a^(−2−ε) is the saved lower bound for approximating e by a rational with denominator a, then den(α)≤q O_N|U|/2 and (1) imply the actual final-center bound

    q ≥ 2/(O_N|U|) ·
       [C_ε(n+1)(n!)²|U| /
             (3·5^b Λ^n exp(Λ/(n+1)))]^(1/(2+ε)).        (3)

Complete cancellation between the two rational numerator components is retained in q. No coefficient clearer is substituted for it.

## 3. Uniform contour gain on the diagonal b=h

Let a=(1+i)/2, V(w)=w²−w+1/2, z(w)=1−2w², and integrate on the complete vertical segment from bar(a) to a. The exact logarithmic identity is

    T−πU=i2^(n+1)(−1)^h
         ∫ V(w)^n z(w)^h (1+4w^4)^b /w^(n+1) dw.       (4)

On the diagonal b=h, let G(w)=z(w)(1+4w^4). Both endpoints are zeros of G. If w=1/2+iy, s=4y²∈[0,1], exact calculation gives

    |z|²=(s²+6s+1)/4,
    |1+4w^4|²=(1−s)²(s²+6s+25)/16.

The degree-six polynomial

    5/8−|G|² = (15−106s+225s²−44s³−39s^4−10s^5−s^6)/64

is strictly positive on [0,1]. An exact Bernstein proof is saved in `quartic_contour_certificate.json`: the intervals [0,1/4], [1/4,1/2], [1/2,1] have strictly positive degree-six Bernstein coefficients. Positivity of those coefficients proves positivity on each entire interval, without a sampled-grid inference. This experiment addressed the new whole-contour hypothesis and supplies a finite rational certificate.

Thus, with η=sqrt(5/8)<1, |G|<η everywhere. Moreover |V/w|≤1/2, |w|≥1/2, and the segment has length one. Formula (4) consequently proves the full uniform estimate

    |β−π| ≤4η^h/|U|,       U≠0, b=h.                    (5)

Both conjugate endpoints and every part of the contour are retained. This is a new geometrically decaying actual companion error in the h~κ n log n range; it is an upper bound and does not prove a nonzero signed logarithmic error.

## 4. Normalization size and honest leading budget

On b=h, for every R>0 Cauchy's estimate gives

    |U| ≤ R^(−n) exp(2nR+2hR²+4hR^4).

Here (1+2R+2R²)^n≤exp(2nR), (1+2R²)^h≤exp(2hR²), and (1+4R^4)^h≤exp(4hR^4). Taking R²=n/(2h) proves

    log|U|≤r log(2h/n)+n+2n sqrt(n/(2h))+n²/h.

For h=κ n log n+O(n), κ>0 fixed, this is r log log n+O_κ(n), hence o(n log n). The integer response can be selected nonzero within r+1 nodes without changing that leading regime.

The complete exponential bound then has

    log RHS(1)=(-1+κ log5)n log n+O_κ(n log log n),

while N=6κ n log n+O(n), and (5) has leading rate κ logη. Under the classical PNT odd-lcm estimate, (3) proves, with ε decreased to zero,

    liminf log q/(n log n) ≥ max(0, 1/2−κ(6+(log5)/2)). (6)

The factor 5^h is essential in this calculation. The error bound (5) is substantially better than the growing complex endpoint factor for the old large selector, but the logarithmic denominator upper bound and exponential coefficient cost worsen. The present formulas therefore do not bridge the denominator gap, do not give a shrinking primitive form, and do not resolve rationality of e+pi. A gain would require actual denominator cancellation or a better complete exponential bound for this exact family, not merely the contour contraction.

## 5. Integral endpoint-shift multiplier has a forced value at the exponential origin

This same target has a simple arithmetic obstruction beyond the chosen power. A bounded archive search for forced endpoint multiplier powers of five and ψ(−1) located no prior instance. The rational-point lower-bound perspective in the opened Pritsker primary paper is classical overlap; only the following exact specialization is claimed here.

Let P(z)∈Z[z], P(1)=1, and suppose P vanishes to order at least b at BOTH za=1−i and zb=1+i. Then the monic irreducible polynomial ψ(z)=z²−2z+2 has ψ(z)^b dividing P(z) in Z[z]. Write P=ψ^b H. Since ψ(1)=1, H(1)=1. Evaluating at −1 proves

    P(−1)=5^b H(−1).

Thus either |P(−1)|≥5^b or P(−1)=0. For the corresponding actual selector multiplier P(−C(t)), its value at the exponential origin t=0 is P(−1). Therefore an integer shift multiplier retaining unit target response and imposing these endpoint multiplicities cannot avoid a factor 5^b in its constant coefficient unless it also vanishes at the exponential origin. This statement is about the actual coefficient, not a lower bound for the complete exponential error: cancellation in that entire tail remains possible.

If P(−1)=0, the additional factor z+1 changes the family and raises the exponential-origin contact order. It also has P(1) divisible by two when the multiplier is integral and consists only of ψ^b(z+1)^a. Such a modification must retain its normalization and complete arithmetic; it is not covered by the unit-response power analyzed here. No general no-go for other rationally normalized multipliers is asserted.
