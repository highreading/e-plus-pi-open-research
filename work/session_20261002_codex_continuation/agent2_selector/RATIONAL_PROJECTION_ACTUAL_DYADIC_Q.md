> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational quartic projection: uniform response and actual dyadic denominator

2026-10-02. New author proof for the exact F,wF projection in `RATIONAL_MULTIPLIER_PERIOD_GATE.md`. The analytic signed error is assigned by the parent to the analysis agent as original work; this note owns the actual final denominator. No audit or irrationality claim is made.

Subsequent complete analytic scope: `../agent3_analysis/RATIONAL_QUARTIC_COMPLETE_LIMIT_TO_PI.md` proves that this actual center tends to pi when n=4k tends to infinity and h/n tends to infinity. Its complete e+pi error tends to e. The exact nonzero/dyadic component theorem below remains valid, but the intended h proportional to nlogn regime does not approximate e+pi. No favorable combined-rate claim is made.

## Search and overlap before this arithmetic target

Archive search covered matching/dyadic, the proposed v_2(q)=v_2(n!)+1 law, and pole-one odd residue numerators in the preceding sessions. The existing large-selector dyadic theorem and adjacent-selector tuning report were located and read previously; neither is this two-pole rational kernel or its matching determinant. Online search on factorial/binomial prime-power principal-part valuations opened the primary Granville full HTML, https://www.cecm.sfu.ca/organics/papers/granville/paper/binomial/html/node3.html and node4.html. Lucas/Legendre congruences are classical overlap. The new assertion is the complete projected-center valuation and exact determinant nonvanishing, with every rational numerator component retained.

The one new exact example n=4,h=1 in `rational_period_projection_n4_h1.json` addressed whether this new projection is nonzero and changes the center; it was not a rerun of archived W cases. The uniform proof below is independent of that finite example. No extra finite grid is run.

## 1. Exact construction and notation

Let n=4k≥4,h≥1, r=n/2,

    V=w²−w+1/2, G=(1−2w²)(1+4w^4),
    F0=(2V)^n G^h/[w^(n+1)(1−w)^(4h)], F1=wF0,
    L=4h−1, T=L!.

Both have integral principal parts and integral polynomial part. Define

    Ri=Res_0(Fi)−Res_1(Fi),
    Ai=Res_1(exp(w−1)Fi),
    Bi=Res_0(exp(w)Fi),
    Mi=T Ai, mi=Mi−T Ri,
    F=m1F0−m0F1,
    U=R(F)=A(F)=M1R0−M0R1.

The matching identity is exact; M_i,m_i,U are integers. Let F=P'+r0/w+r1/(w−1) be its Hermite reduction with rational P. Put

    Π(F)=4 Im P((1+i)/2),
    c(F)=[−B(F)−Π(F)]/U.

This is the complete actual center when U≠0, as derived in the period-gate note. Its denominator q is reduced AFTER summing the exponential and logarithmic rational numerators.

## 2. Exact low residue parities

At zero write

    H0(w)=(2V(w))^n G(w)^h/(1−w)^(4h)=Σ d_j w^j.

Then Res_0 F0=d_n and Res_0 F1=d_(n−1). Modulo two,

    H0(w)=(1−w^4)^(−h),
    d_n=binom(h+k−1,k) mod2,
    d_(n−1)=0 mod2.                               (1)

Equivalently d_n=binom(n+4h−1,n) mod2 by Lucas. Assume from now on the explicit eligibility condition

    binom(n+4h−1,n) is odd.                       (2)

Thus d_n is a 2-adic unit and d_(n−1) is even.

The sum of the finite residues is the coefficient of 1/w at infinity. Since every coefficient of (2V)^n G^h in degree j has v_2≥ceil(j/2), expansion of the integer inverse (1−1/w)^(−4h) at infinity gives

    Res_0 Fi+Res_1 Fi ∈2^(r+2h) Z, i=0,1.          (3)

For F0 the minimum contributing numerator degree is n+4h; for F1 it is n+4h−1, whose ceiling half is still r+2h. Consequently

    R0=2d_n−(Res_0 F0+Res_1 F0), v_2(R0)=1,
    R1=2d_(n−1)−(Res_0 F1+Res_1 F1), v_2(R1)≥2.  (4)

This includes R1=0, with infinite valuation. No division by R1 is used.

## 3. Exact exponential pole-one numerators

At w=1+u define

    H(u)=(1+2u+2u²)^n G(1+u)^h/(1+u)^(n+1)
        =Σ c_j u^j.

Since 4h is even, Fi has regular pole-one factors H(u) and (1+u)H(u), respectively. Therefore

    M0=Σ_(j=0)^L c_j(L)_j,
    M1=Σ_(j=0)^L (c_j+c_(j−1))(L)_j,
    c_(−1)=0.                                    (5)

The constant c0=(−5)^h is odd. Direct logarithmic differentiation gives

    c1/c0=n−1+36h/5,
    c1=3c0 mod4.

Modulo two H(u)=(1+u)^(−n−1), so c0,c1,c2,c3 are all odd because n is divisible by four. Now L=4h−1 is 3 modulo four. In M0, the first two terms are

    c0+L c1=2 mod4.

The j=2 and j=3 falling factorials are both 2 modulo four; their contributions cancel modulo four because c2,c3 are odd. Every j≥4 has a falling factorial divisible by four, and absent j values when h=1 are simply omitted. Thus

    v_2(M0)=1.                                   (6)

For M1, its first regular coefficient c1+c0 is even. Every j≥2 falling factorial is even, while the constant c0 is odd. Hence

    v_2(M1)=0.                                   (7)

Since v_2(T)≥1, (4),(6),(7) give

    v_2(m0)=1, v_2(m1)=0,
    v_2(U)=v_2(M1R0−M0R1)=1.                     (8)

The determinant is therefore NONZERO uniformly at every eligible (n,h), independently of an analytic saddle or a numerical experiment. A zero of R1 or any higher content in it causes no problem.

## 4. Complete exponential numerator at zero

Using H0 above and n divisible by four,

    n!B0=Σ_(j=0)^n d_j(n)_j =1 mod4,
    n!B1=Σ_(j=1)^n d_(j−1)(n)_j =0 mod4.          (9)

Indeed d0=1 and all falling factorials (n)_j with j≥1 are divisible by four. Thus

    E=n!B(F)=m1(n!B0)−m0(n!B1)

is an ODD integer, by (8),(9). Therefore

    v_2(B(F))=−v_2(n!).                          (10)

This is the entire exponential rational component, not its highest pole term alone.

## 5. The full logarithmic rational numerator is 2-integral

Every higher principal-part term a_j(w−c)^(−j), c=0 or 1, integrates to −a_j(w−c)^(−j+1)/(j−1). At a=(1+i)/2 the inverses are

    a^(−1)=1−i, (a−1)^(−1)=−1−i.

For every integer t≥1,

    v_2(Im((±1−i)^t))≥floor(t/2)≥v_2(t),

with zero imaginary parts interpreted as infinite valuation. Multiplication by four therefore gives valuation at least two for EVERY negative-power primitive contribution to Π(F). No cancellation or discarded term is needed for this lower bound.

For the polynomial part p(w)=Σ p_ell w^ell, the infinity expansion just used gives the coefficient bound

    v_2(p_ell)≥r+2h+floor(ell/2).

This coarse bound holds for both Fi and their integral projection combination. Also

    v_2(Im(a^(ell+1)))≥−ceil((ell+1)/2).

The polynomial primitive term therefore has valuation at least

    2+r+2h−1−v_2(ell+1)≥2.

Here ell+1≤n+2h+1, and floor(log2(n+2h+1))≤r+2h−1 for n≥4,h≥1. The latter elementary inequality holds at n=4,h=1 and remains true when either n or h increases. This controls EVERY polynomial primitive term, including zero coefficients. Combining both parts proves

    v_2(Π(F))≥2.                                (11)

The same bound holds for Π(F0) and Π(F1) separately.

## 6. Actual final-q theorem and explicit eligible sequence

Equations (10),(11) imply that B(F)+Π(F) has exactly valuation −v_2(n!). Using the ACTUAL matched response (8), final rational reduction gives the uniform theorem

    v_2(q)=v_2(n!)+1,                            (12)

for EVERY n divisible by four and h≥1 satisfying (2). This proves both U≠0 and the precise dyadic denominator after combining the complete e and pi rational components.

Eligible indices exist with explicit O(n) adjustment. Choose a power of two P with k<P≤2k, and require

    h=1 mod P.

Then h−1 has all its low binary digits zero and Lucas gives binom(h+k−1,k) odd. For any positive prescribed H, the first h≥H in this class satisfies H≤h<H+P. In particular h=κ n log n+O(n) is available for every κ>0. When n is a power of two the eligibility condition is just the binary digit of h−1 with place value k=n/4 being ZERO; the sign of that bit condition must not be reversed.

The polynomial quartic family forced an additional 3h in its dyadic q valuation on its selected even nodes. The present rational projection has removed that compulsory h-scale dyadic cost. This is a material actual-component arithmetic improvement, but it does not estimate odd denominator content or complete signed error and therefore supplies no small-form or irrationality conclusion.

## 7. Exact odd clearer and final gcd

Let

    ell=max(n,4h−1,n+2h+1), O_ell=lcm(odd positive integers≤ell).

Each rational primitive denominator divides an integer at most ell; (11) shows that all dyadic denominators disappear from Π(F). Hence O_ell Π(F) is an integer. With E=n!B(F) as above, the complete actual denominator is

    q=n! O_ell |U| /
       gcd(n! O_ell U, O_ell E+n! O_ell Π(F)).       (13)

No powers of two from Gaussian polynomial evaluation are needed in this final clearer. In the main regime h/n→∞, ell=4h−1. Thus the explicit odd-lcm length is 4h, while the entire remaining primitive denominator question is the ODD content of the determinant U and numerator gcd in (13). The factorial T used to build the projection coefficients is absent as a formal common denominator, but can still influence their size and odd content. Its favorable cancellation is not assumed.
