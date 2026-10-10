> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# L23: a proved infinite regular dyadic subfamily of the weighted coefficient-one determinant

Author result, 2026-10-02. This continues the same L23 normalized-moment target. Root owns the exact weighted determinant construction; selector owns odd-prime arithmetic; analysis owns complete approximation error. This is original local arithmetic, not an independent audit of their results.

The earlier conditional formula is in `WEIGHTED_DETERMINANT_DYADIC_GATEWAY.md` §4. Both of its formerly unproved premises are proved here for

    n=4^j+1, k=(n+1)/2, j≥1.                  (1)

The proof is all-degree. Its finite field computation concerns a fixed four-term recurrence, not an atlas of degrees or primes. Neither a general all-n integrality theorem nor an odd-content conclusion is claimed.

## 1. Exact interface and the final reduced denominator

Let A(P)=∫_0^∞e^(−t)P(1−t)dt and let d_r=!r. Thus A(x^(2s))=d_(2s). Put

    C_s=d_(2s)−(−1)^s.

For n=2k−1, let q_n(y) be the primitive integer polynomial, of degree n, whose rational ray satisfies

    Σ_(t=0)^n q_t C_(s+t)=0, 0≤s<n.

The signed moment form is nonsingular for n≥2 by the established Gamma-minus-evaluation argument; all equations below use its actual orthogonal ray. Set w=q_n(−1), v_i=(−1)^i, 0≤i<k, and

    L_s=4Σ_(r=0)^(s−1)(−1)^r/(2s−1−2r), L_0=0,
    V_s=Σ_t q_t L_(s+t),
    R_ij=−Σ_t q_t(2(i+j+t))!+V_(i+j).

All entries of R have odd denominators. The FULL evaluated determinant is

    det(R+S w vv^T)=alpha+beta S,
    alpha=det R, beta=w v^T adj(R)v, S=e+pi.   (2)

Its rational center is −alpha/beta. Clearing the odd denominators and taking the complete gcd gives exactly

    v2(q_center)=max(0,v2(beta)−v2(alpha)).     (3)

This final gcd, rather than any row clearer, is the denominator object throughout.

Write m=k−1=(n−1)/2 and sigma=m+v2(m!). The theorem proved below yields, on(1),

    q_n(2z−1)/2^n∈Z_2[z], leading q_n odd,
    q_n(0) odd,
    v2(V_s)≥n+sigma+1 for EVERY integer s≥0.  (4)

Consequently the exact complete pair has

    gamma=k(k−1)+2Σ_(i=0)^(k−1)v2(i!),
    v2(alpha)=gamma,
    v2(beta)=gamma+v2(w)−2sigma,
    v2(q_center)=v2(w)−2sigma.                (5)

The last expression is positive. In fact v2(w)≥n+sigma, so v2(q_center)≥n−sigma. For m=2^(2j−1), sigma=2m−1=n−2 and this only gives the uniform lower bound2. A stronger rate depends on a genuinely remaining endpoint valuation, isolated in§7. Formula(5) is proved without that stronger valuation and must not be called a factorial survival theorem.

## 2. Exact affine contraction for the normalized Gamma moments

Set z=(x²+1)/2 and

    b_r=A(z^r).

The previously proved normalized moment recurrence is

    b_0=b_1=1,
    b_(r+1)=(r+1)(2r+1)b_r−r(r+1)b_(r−1)−r. (6)

Every b_r is an odd integer. The signed normalized moments are mu_0=0 and mu_r=b_r for r≥1.

Pair consecutive terms as V(t)=(b_(2t+1),b_(2t))^T and write u=2t. Two applications of(6) give EXACTLY

    V(t)=M(u)V(t−1)+c(u),                    (7)

where

    M11=−2u−2u²+4u³+4u⁴,
    M12= u+2u²−u³−2u⁴,
    M21=−u+2u², M22=u−u²,
    c1=1+u−u²−2u³, c2=1−u.

Every entry of M(u) is divisible by u. At t=0, M(0)=0 and c(0)=(1,1)^T, so the recurrence includes its actual initial pair.

The convergent representation on t∈Z_2 is

    V(t)=Σ_(a≥0) M(2t)M(2t−2)...M(2t−2a+2)c(2t−2a),
                                                     (8)

where an empty product is the identity. The a-th summand is divisible as a polynomial by

    2^a(t)_a.

Its values therefore have depth at least a+v2(a!), uniformly on Z_2. This proves uniform convergence and uniqueness among bounded solutions of(7). At each nonnegative integer t the formula terminates because M(0)=0 and reproduces(6).

There is also a useful stronger coefficient statement. Regarding(8) as a series in u, its a-th summand contains

    u(u−2)...(u−2a+2).

The coefficient of u^ell in this product has depth at least max(0,a−ell); subsequent integral polynomial factors cannot reduce this bound for a fixed ell. Thus every coefficient converges, is2-integral, and defines

    V(t)=(O(2t),E(2t))^T,
    O,E∈Z_2[[u]].                            (9)

These power series converge on u∈2Z_2. Consequently b_r has integral ordinary Taylor coefficients on each parity disk:

    b_r=E(r) for even r,
    b_r=O(r−1) for odd r.

For every d,r≥0 this proves the ALL-DEPTH difference law

    v2(Delta_2^d b_r)≥d+v2(d!),              (10)

where Delta_2 f(r)=f(r+2)−f(r). To see this, translate the relevant integral series to r, which is an even translation within its disk. For f(r+h)=Σ a_ell h^ell, a_ell∈Z_2, the identity

    Delta_2^d f(r)/(2^d d!)
      =Σ_(ell≥d) a_ell 2^(ell−d) S(ell,d)

uses integer Stirling numbers. It also shows that the residue of the normalized difference is precisely the degree-d Taylor coefficient modulo2.

## 3. The exact residue series

Reducing(7) coefficientwise modulo2 is legitimate in(9). Translation u→u−2 reduces to u, and solving the resulting2×2 system gives

    Ebar(u)=(1+u²+u³)/(1+u+u⁴),
    Obar(u)=(1+u+u³)/(1+u+u⁴).               (11)

Let e_d,o_d be these coefficients over F_2. Equation(10) refines to

    Delta_2^d b_r/(2^d d!) = e_d mod2 if r is even,
                               o_d mod2 if r is odd. (12)

All higher Taylor terms carry an additional2. Translating by an even integer preserves the Taylor coefficient residue, so(12) holds for every starting r, not merely r=0,1.

Their sum a_d has generating function

    Abar(u)=Ebar(u)+Obar(u)=u(1+u)/(1+u+u⁴). (13)

This is a fixed exact F_2 recurrence: a_0=0,a_1=1,a_2=a_3=0, and a_r=a_(r−1)+a_(r−4) for r≥4. Its first fifteen coefficients are

    0,1,0,0,0,1,1,1,1,0,1,0,1,1,0.

The next four coefficients repeat the initial state, so induction by the recurrence proves period15 at ALL indices. Since2^h modulo15 cycles through1,2,4,8,

    a_(2^h−1)=1 exactly when h is odd.        (14)

This finite recurrence certificate supports an all-degree identity; it is not experimental extrapolation of orthogonal polynomials.

## 4. A monic basis and exact normalized Gram units

Use the MONIC integral polynomial basis

    h_0(z)=1,
    h_(2d+1)(z)=z(z²−1)^d,
    h_(2d+2)(z)=z²(z²−1)^d, d≥0.            (15)

Its change of basis from ordinary monomials is integral unit triangular. Set D_0=1 and D_(2d+1)=D_(2d+2)=2^d d!. These D are moment-row scales, not primitive denominators.

Let L be the signed functional L(z^r)=mu_r. Products of nonconstant basis polynomials are z^(a+b)(z²−1)^(d+e), so(10) proves that

    G_ij=L(h_i h_j)/(D_iD_j)∈Z_2.           (16)

The constant row also obeys this bound; L(h_0²)=0. The EXACT residue for i,j≥1 is

    G_ij=binom(d+e,d) e_(d+e) if i+j even,
                         o_(d+e) if i+j odd,

where d=floor((i−1)/2), e=floor((j−1)/2). Its constant row is o_d at odd i and e_d at even i.

For n=2m+1≥3, the first n basis vectors consist of h_0 and m complete pairs. Replace h_0 by h_0+h_2=1+z². Modulo2 it has norm1 and is orthogonal to EVERY other basis vector: its two pairings are identical by(12). This replacement is unit triangular as a change of finite basis.

Within each remaining pair replace its even member by the sum of its odd and even members. With P_d=h_(2d+1), Q_d=h_(2d+1)+h_(2d+2), the remaining residue matrix becomes

    [ H_E  H_A ]
    [ H_A   0  ],

with H_A(d,e)=binom(d+e,d)a_(d+e), 0≤d,e<m. Hence

    det(G_(0≤i,j<n)) = det(H_A)^2 mod2.      (17)

Now let m=2^h. Lucas's binomial criterion gives H_A(d,e)=0 if d+e≥m: such a sum of two h-bit numbers necessarily has a binary carry. On the anti-diagonal d+e=m−1, the two indices are binary complements and the binomial coefficient is1. The matrix is therefore anti triangular, with every anti-diagonal entry a_(m−1). Thus

    det H_A=a_(m−1)^m in F_2.                (18)

By(14), this determinant is1 when h is odd. Equations(17)–(18) prove G is2-integrally invertible for n=4^j+1, for EVERY j≥1.

## 5. Integral orthogonal coefficients, with their stronger filtration

More generally suppose the normalized n×n Gram G in(16) is a dyadic unit. Let P_n(z) be the monic normalized orthogonal polynomial. Write

    P_n=h_n−Σ_(i<n) gamma_i h_i.

The mixed normalized row w_i=L(h_nh_i)/(D_nD_i) is integral by the SAME difference theorem. Solving the original Gram system gives EXACTLY

    gamma_i=(D_n/D_i)(G^−1 w)_i.             (19)

For i<n the integers d_i=floor((i−1)/2) are at most d_n, so D_n/D_i is2-integral. It follows that P_n∈Z_2[z]. The stronger coefficient statement is

    v2(gamma_i)≥v2(D_n)−v2(D_i).             (20)

For odd n=2m+1, v2(D_n)=sigma=m+v2(m!). The constant term is −gamma_0 and has depth at least sigma.

Returning to the ACTUAL primitive integer ray in y, the polynomial2^nP_n((y+1)/2) is monic and2-integral. Its rational coefficients have odd reduced denominators. Clearing only odd denominators and removing integer content produces the primitive q_n with an odd leading coefficient lambda. Therefore

    q_n(2z−1)=lambda 2^n P_n(z), lambda odd.  (21)

If P_n=Σ p_j z^j, the coefficients of(y+1)^j in q_n have depth at least n−j. Its value at y=0 is thus odd, because the final j=n coefficient is odd and all the other terms are even. This proves the first two premises in(4) on the infinite regular family.

## 6. The rational arctangent functional respects the SAME filtration

For I_r=∫_0^1(1+x²)^r dx, put u_r=I_r/2^r. Integration by parts gives

    u_0=1, (2r+1)u_r=r u_(r−1)+1.           (22)

All u_r are2-integral. Pairing its even/odd indices gives a scalar affine contraction. With u=2t and F(2t)=u_(2t+1),

    F(u)=A(u)F(u−2)+B(u),
    A(u)=u(u+1)/[(2u+1)(2u+3)],
    B(u)=(3u+2)/[(2u+1)(2u+3)].             (23)

Both A,B have integral ordinary series; A is divisible by u. The expansion by products of A(u−2ell) converges coefficientwise: its length-a product contains u(u−2)...(u−2a+2), whose degree-ell coefficient has depth at least max(0,a−ell). The remaining rational factors have integral series, since their constant denominators are odd. Thus F∈Z_2[[u]], and the even branch

    u_(2t)=[2t F(2t−2)+1]/(4t+1)

also has integral ordinary Taylor coefficients. These exact branch statements imply, for all r,d≥0,

    v2(Delta_2^d u_r)≥d+v2(d!).             (24)

Define the rational arctangent response on normalized polynomials by

    R_at(1)=0, R_at(z^r)=2u_(r−1), r≥1.      (25)

The FULL real period identity is

    4∫_0^1 P((x²+1)/2)/(1+x²)dx
      =pi P(0)+R_at(P).

Equation(25) therefore retains, rather than loses, the endpoint pi response. For every a≥1, (24) applied to u_(a−1) yields

    v2 R_at(z^a(z²−1)^d)≥1+d+v2(d!).        (26)

The same lower bound holds after multiplying h_i by ANY integral polynomial in z, because ordinary monomial multiplication only changes the starting index a. For h_0 this statement reduces to R_at(Z_2[z])⊂2Z_2. In particular it holds for (2z−1)^s, for every integer s≥0.

Use the SAME h_i basis as(19)–(20), without converting a bound to a different basis prematurely. Each lower-degree term gamma_i h_i has rational response depth at least sigma+1 by(20),(26). The leading h_n term has the same depth. Therefore

    v2 R_at(P_n(z)(2z−1)^s)≥sigma+1.

Equation(21) proves exactly v2 V_s≥n+sigma+1 as claimed in(4). This repairs the previously identified basis obstruction through a new common filtration, not by asserting that the old(y+1)-basis bound was a y-basis bound.

For i,j<k=m+1, the required factorial/Pascal gate is

    v2 V_(i+j)≥i+j+v2(i!)+v2(j!)+1.

Its right side is at most2sigma+1; the proved bound is n+sigma+1, which is larger since n−sigma≥2. Thus the actual matrix R obeys the same-y-basis hypothesis of the complete-pair theorem.

## 7. What is established after full content, and the next endpoint target

Normalize the factorial part in the y^i basis by E_i=2^i i!. Because q_n(0) is odd, its reduction is the Pascal Gram matrix binom(i+j,i); all t≥1 polynomial-coefficient terms are even. The complete arctangent correction is even in this SAME normalization by§6. Thus R=E M E, with M integral unit and every northwest principal minor a unit. The final-coordinate term is uniquely lowest in v^T R^−1v, of depth −2sigma. This proves the alpha,beta depths and the ACTUAL final-q equality(5), including the full gcd.

Let eta=(G^−1w)_0 in(19). Then

    P_n(0)=−D_n eta,
    v2(q_n(−1))=n+sigma+v2(eta),
    v2(q_center)=n−sigma+v2(eta).             (27)

The real signed form ensures q_n(−1)≠0, so eta≠0. Indeed if P_n(0)=0, write P_n=zW with degW<n; its orthogonality to W would say A(zW²)=0. Since z=(x²+1)/2 is strictly positive on the real Gamma support, this contradicts W≠0. On n=4^j+1, (27) reduces to

    v2(q_center)=2+v2(eta).                  (28)

The unit Gram proof only shows eta∈Z_2; it does not determine its possibly large depth. Quantifying this one full endpoint scalar is the next original target. It cannot be replaced by v2(n!), v2(detK_n), or a raw row count. Bounded moment states at n5 and n17 give q-center dyadic depths7 and19 via this proved theorem, but they establish no general formula for eta.

## 8. Gate and novelty boundary

The original L23 archive/primary gate is recorded in TARGET_LEDGER.md and the gateway note. Before the new branch-contraction sublemma, the additional archive query was `normalized.*moment.*dyadic.*interpol|Laguerre.*2.adic.*moment|b_r.*2.adic|B_r.*affine.*contract|2t.*moment.*contract|paired.*moment.*interpol` across the designated sources and old sessions; it returned no matches. Fresh primary queries were `"p-adic" "Laguerre" "moments" recurrence`, `"2-adic" "Bessel polynomials" recurrence moments`, and `"derangement" "p-adic" interpolation 2026`.

Opened full primary O'Desky–Richman, https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2022/81.pdf and https://arxiv.org/html/2012.04615v4. Metric interpolation of ordinary/cyclic derangements, Mahler expansions and factorial-tail convergence are established overlap. The b_r here are the quadratic-ring NORMALIZED Gamma moments, not ordinary derangements with a changed sign or cyclic parameter. The exact coupled matrix(7), residue series(11), anti-triangular divided-power Gram certificate(17)–(18), and its simultaneous arctangent filtration(23)–(26) are the author-specific arithmetic. No general interpolation theorem is imported as a primitive orthogonal-coefficient theorem.

No conclusion about irrationality of e+pi, a general-all-n premise, or odd determinant content is asserted.
