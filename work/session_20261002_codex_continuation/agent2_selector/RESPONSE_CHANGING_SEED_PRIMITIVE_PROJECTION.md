> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Response-changing simple-pole projection and the actual primitive content

2026-10-02. Original author work under root's distinct response-changing-rational-projection steering. It does not duplicate root's polynomial amplitude multiplying e^(-z). The matched kernel response changes here; the complete target is still e+pi. Elementary homographic transformations of rational numbers are not claimed novel.

## Fresh archive and primary gate

Archive queries covered response-changing affine/Mobius corrections, low-degree matched seeds, `2/w+1/(w−1)`, and denominator changes under a response U+t. Opened `sources/common_kernel_growing_correction_full_window_cancellation.md`, Section5: its extra response channels solve another moment lattice and are relevant background, not this scalar primitive projection. Read the current exact rational period gate and fixed-response correction notes as internal overlap. A bounded search finding no explicit present seed identity is not a global novelty assertion.

Fresh primary queries covered mixed exponential/logarithmic Hermite–Padé approximation, rational normalization, and homographic denominator/content changes. Opened full primary Van Assche, *Padé and Hermite–Padé approximation and orthogonality*, https://arxiv.org/pdf/math/0609094, Section3.2 and its common-denominator irrationality criterion. Opened González Ricardo–López Lagomasino–Medina Peralta, *Logarithmic asymptotic of multi-level Hermite–Padé polynomials*, https://arxiv.org/pdf/2002.06194, Sections1–2 on rational perturbations of a Nikishin system. Common-denominator approximation and rational perturbation are established background. Their asymptotics do not apply automatically to the present mixed e/pi period kernel and are not imported. The exact target, gcd and error identities below are the specific author contribution.

## 1. Minimal matched seed with an integer center

Use the actual rational-kernel functionals

    R(F)=Res0 F−Res1 F,
    A(F)=Res1(e^(w−1)F), B(F)=Res0(e^wF),
    Pi(F)=4Im P_F(a), a=(1+i)/2,

where F=P_F′+r0/w+r1/(w−1) is its rational primitive decomposition. An actual matched kernel has R(F)=A(F)=U!=0 and center c=−[B(F)+Pi(F)]/U.

The fixed rational seed

    G6(w)=2/w+1/(w−1)−4                                  (1)

has EXACT functionals

    R(G6)=1, A(G6)=1, B(G6)=2,
    P_G6(w)=−4w, Pi(G6)=−8, c(G6)=6.                     (2)

It introduces no new poles or periods. The pi logarithmic periods are those already used at0,1; its two primitive endpoints give the complete Pi in(2). Among kernels with only simple poles at0,1 and no polynomial term, the matched residues are proportional to(2,1), giving center−2. The constant term−4 in(1) changes that seed center to6 while preserving R,A. This low-degree construction is independent of any unknown value of S=e+pi.

## 2. Exact projection for any actual p/q

Let c=p/q be the OLD actual reduced center, q>0, gcd(p,q)=1, and take the original response U to be an integer as in the reflected construction. For a rational number t, adding tG6 changes both matched responses to U+t and gives

    c_t=(Uc+6t)/(U+t),
    (S−c_t)=[U(S−c)+t(S−6)]/(U+t).                       (3)

This is a response-changing operation, distinct from H″+H′ corrections that keep U fixed. No division by the old error or by a new numerator is used.

For an integer a with q+a>0 choose the explicit coefficient t=aU/q. Then

    F_a=F+(aU/q)G6,
    R(F_a)=A(F_a)=U(q+a)/q!=0,
    c_a=(p+6a)/(q+a).                                    (4)

Its ACTUAL final denominator is exactly

    g_a=gcd(q+a,p−6q),
    q_a=(q+a)/g_a, p_a=(p+6a)/g_a.                        (5)

The equality uses gcd(q+a,p+6a)=gcd(q+a,p−6q). Infinite or undefined valuations are unnecessary even when p+6a=0: the ordinary gcd formula(5) remains valid.

The COMPLETE signed errors, including the primitive normalization, are

    E_a=S−c_a=[qE_old+a(S−6)]/(q+a),
    q_aE_a=[qE_old+a(S−6)]/g_a,
    c_a−c=a(6−c)/(q+a).                                  (6)

Thus every old exponential and logarithmic endpoint error is retained through E_old, and the added seed's entire target error is S−6. There is no transferred contour or saddle estimate that could omit the seed contribution.

## 3. Old prime support disappears without increasing the rate ceiling

Equation(5) implies

    gcd(q_a,q) divides gcd(a,q).                          (7)

In particular, if the OLD q is odd, take the fixed value a=2. Then

    gcd(q_2,q)=1, q_2<=q+2,
    c_2−c=2(6−c)/(q+2).                                  (8)

Every prime divisor of the old denominator disappears from the NEW actual q. On the rational-scaled reflected subsequence, old q is exactly its odd part B and tends to infinity at least exponentially. Therefore(8) preserves convergence to e+pi, with a complete shift O(1/q), while removing every previously forced old prime, including5 and any finite set supplied by the arithmetic agent's all-prime theorem.

This does not contradict fixed-response prime survival: the scalar aU/q need not be p-integral at an old denominator prime and the response itself changes. Its coefficient denominator is retained in Section6. No claim is made that the global size of q_2 is smaller by an exponential factor. The safe comparison q_2<=q+2 preserves the denominator growth ceiling; a genuine global gain would require quantified new content g_2.

The same statement holds for a=4 when q is odd. More generally any fixed a coprime to q changes denominator support while giving q_a<=q+a and a full O(1/q) perturbation of a bounded center. It uses only known rational data and a fixed integer6, rather than rounding to S.

## 4. A two-output nonzero selector without a phase premise

The elementary known bounds give5<S<6. For any two distinct integers a,b with q+a,q+b>0, E_a and E_b cannot BOTH be zero. From(6) their vanishing would imply

    qE_old+a(S−6)=0,
    qE_old+b(S−6)=0,

and subtraction would give S=6, a contradiction. This proof is valid if E_old=0 and never divides by an error.

Consequently the fixed two-seed block a=2,4 contains a nonzero COMPLETE primitive error for every OLD matched center with odd q. Both new q values are odd, coprime to the entire old q and at most q+4. The actual response is nonzero throughout the enlarged block. This supplies a genuine fixed-length selector, but by(6) a seed contribution of primitive size O(1) remains unless the new gcd grows; nonzero selection alone is not a primitive-small-form theorem.

## 5. A global content budget for a fixed seed block

Put C=p−6q. On a convergent subsequence c→S<6, C!=0 eventually and |C|=q|c−6|~(6−S)q.

For the two odd denominators q+2,q+4,

    gcd(g_2,g_4)=1, g_2g_4 divides |C|.

Hence their actual denominator product obeys

    q_2q_4>=(q+2)(q+4)/|C|.                              (9)

At least one has denominator of order at least sqrt(q). Equation(9) does not bound the smaller denominator, nor identify which node has the favorable gcd or a nonzero error.

More generally let a_i=2i,1<=i<=K, with K fixed and OLD q odd. Then gcd(g_i,g_j) divides2|i−j|. Define the fixed constant

    C_K=product_(1<=i<j<=K) 2|i−j|.

For positive integers, product g_i/lcm(g_i) is at most product of their pairwise gcds: prime by prime, sum of valuations minus their maximum is bounded by the sum of pairwise minima. Since lcm(g_i) divides |C|,

    product_i g_i<=C_K|C|,
    product_i q_i>=product_i(q+2i)/(C_K|C|)
                     =Omega_K(q^(K−1)).                  (10)

Thus a fixed block cannot supply the same large content gain at EVERY node; at least one q_i is Omega_K(q^(1−1/K)). This is a block/global-content limitation, not an exclusion of a single isolated favorable node. At most one complete error can vanish in this block, as proved in Section4.

## 6. Full coefficient, pole and degree cost

The added scalar aU/q has ACTUAL reduced rational denominator

    q/gcd(aU,q)

and integer numerator aU/gcd(aU,q). These costs are explicit. If L is any existing complete coefficient denominator for F, a safe coefficient denominator for F_a is

    lcm(L,q/gcd(aU,q)).                                   (11)

There are no new finite poles, no pole-order increase beyond max(old order,1), and the added polynomial part has degree0. The rational numerator has fixed degree2 over w(w−1):

    G6=(−4w²+7w−2)/[w(w−1)].                             (12)

Its coefficient height is7. The added term's real coefficient size is O(|aU|/q), and after clearing its rational scalar denominator its numerator height is O(|aU|/gcd(aU,q)). The FINAL response normalization in(4) and actual q in(5) are not identified with that coefficient clearer.

The original high-order endpoint zeros can be filled by this low-order seed. Therefore a proof relying on their persistence cannot be reused; the COMPLETE error identity(6) replaces that inference exactly.

## 7. Exact divisor/index interface and the small-a window

Write H=p−6q and D=q+a>0. For H!=0, EVERY integer a corresponds uniquely to

    g=gcd(D,|H|), m=D/g>0, t=H/g,
    gcd(m,t)=1,
    a=gm−q, c_a=6+t/m, q_a=m.                            (13)

Conversely, choose a positive divisor g of|H| and an integer m>0 with gcd(m,H/g)=1. Setting a=gm−q gives EXACTLY the actual denominator m and center6+(H/g)/m. The complete primitive error becomes

    m(S−6)−H/g.                                         (14)

Thus arbitrary divisor/index freedom is not an approximation gain by itself: (14) is a fresh rational approximation of S−6, with numerator constrained to be the signed divisor H/g. There is no known uniformly favorable divisor distribution for these actual H values.

Every possible g is coprime to the OLD q because

    gcd(H,q)=gcd(p,q)=1.                                 (15)

The new gcd cannot be paid by any old forced factorial or fixed-prime denominator content. It must come from the numerator H at primes outside the old denominator. Also gcd(a,g)=1 follows from a=gm−q and(15). These are exact content constraints.

Suppose the OLD c tends to S, q tends to infinity and q+a>0. Since S−6!=0, the response-changing centers converge to S IF AND ONLY IF

    a/q→0.                                              (16)

For necessity, c_a−6=H/(q+a) and c−6=H/q both tend to the same nonzero number S−6; their ratio forces(q+a)/q→1. Sufficiency follows from the complete error identity(6). This handles a negative perturbation without assuming the new response is bounded away from0 before checking its actual denominator.

For a specified window0<=W<q, EVERY |a|<=W satisfies the complete bound

    |E_a|<=[q|E_old|+W|S−6|]/(q−W).                      (17)

If W=o(q), the old convergence is uniform throughout the window and q_a<=q+W. A prospective denominator ceiling q_a<=M requires a divisor/index pair in(13) satisfying

    g>=(q−W)/M,
    (q−W)/g<=m<=(q+W)/g,
    m<=M,
    gcd(m,H/g)=1.                                       (18)

These conditions are also sufficient. If g>2W, the integer interval in(18) has length less than1, so at most one candidate m exists for that divisor. Its existence amounts to the exact residue condition dist(q,gZ)<=W, along with coprimality and the ceiling. No generic short-interval divisor assertion is imported.

If preserving an odd NEW denominator is desired, one may restrict a to even integers: D is then odd and both actual g,m are odd. If erasing the OLD prime support is also desired, retain gcd(a,q)=1 explicitly. Arbitrary variable a in the small window need not satisfy that condition.

There is a useful conditional construction with a prescribed ACTUAL divisor g of|H| satisfying g<=2q, as every such divisor eventually does on the convergent subsequence here. Choose D to be the nearest positive multiple of g to q, and put a=D−q. Then |a|<=g/2. Its actual gcd g_actual=gcd(D,|H|) may be larger than g, but it is never smaller. Consequently

    q_a<=q/g+1/2,
    |q_aE_a|<=q|E_old|/g+|S−6|/2.                        (19)

If such divisors obey g→infinity and g=o(q), the global denominator is reduced by an unbounded factor and convergence survives. Their existence is NOT proved. The primitive bound in(19) still has a constant seed term and does not tend to zero automatically. Making g large alone does not settle the required alignment of the complete error.

Finally put T=6−S>0. The EXACT real cancellation index is

    a_star=qE_old/T,
    q_aE_a=T(a_star−a)/g_a.                              (20)

This is an analytic description, not an authorization to use the unknown S as construction data. A nearby integer a only guarantees a constant primitive residual when g_a is bounded. A small primitive form would require simultaneous control of the actual gcd at that nearby index and the signed distance in(20). That joint question is distinct from selecting an arbitrary divisor.

## Outcome and unresolved actual arithmetic

The response-changing seed supplies a target-preserving rational representation with complete error, full q and a uniform two-output nonzero selector. It erases ALL old local-prime denominator support at a bounded analytic perturbation and without increasing the global denominator-rate ceiling. The remaining actual arithmetic is the explicit divisor g_a of C=p−6q at q+a. Its growth is not proved. This is a structural primitive projection with a concrete arithmetic target, not a solution of the e+pi irrationality problem or a claim of a general exponential q saving.
