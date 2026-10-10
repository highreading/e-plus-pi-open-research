> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete primitive-error product for a fixed response-changing seed block

2026-10-02. Original analytic continuation by agent3. The selector's exact seed, actual primitive denominator and content budget are author dependencies, used with attribution rather than independently reviewed. This note concerns simultaneous complete errors in a fixed block; it does not exclude one isolated favorable output or provide a global obstruction to response-changing constructions.

## 1. Fresh gate and precise overlap

The response-changing target gate is saved in `RESPONSE_CHANGING_COMPLETE_ERROR_PROGRESS.md`. The more specific archive queries searched `(primitive|full|complete).{0,30}error.{0,30}product`, `product.{0,40}(primitive|complete).{0,30}(error|residual)`, and qE-squared expressions. Read the returned `sources/item278_beta_casoratian_portfolio_report.md`: it concerns products of a different scalar Casoratian family and pooled p-adic return depths. Read `work/session_20261001_astra/JOINT_COMPANION_OVERLAP_BUDGET_DRAFT.md`: it constrains separate e/pi companions and cancellation deficits, not this scalar seed block. Neither supplies the result below. Search absence is not a novelty claim.

Read the new exact interface `agent2_selector/RESPONSE_CHANGING_SEED_PRIMITIVE_PROJECTION.md`, especially Sections2,4,5,7. Its product-content lemma in Section5 is credited and NOT rederived as new here. Fresh primary searches were `site:arxiv.org simultaneous rational approximations determinant product errors Hermite Pade gcd` and `site:arxiv.org least common multiple shifted integers products gcd arithmetic progression`. Opened https://arxiv.org/pdf/math/0510278, https://arxiv.org/pdf/1409.4053 and Hong–Qian, *The least common multiple of consecutive arithmetic progression terms*, https://arxiv.org/pdf/0903.0530 . Classical common-denominator/determinant and product/lcm arguments are related background. No published theorem about e+pi or the present actual seed error is imported.

## 2. Exact complete-error interface and attributed content

Put S=e+pi and d=6−S>0; the elementary bounds5<S<6 suffice. Let c=p/q be an actual reduced old center with q positive and ODD, and define

    E=S−c, H=p−6q=−q(d+E).

For fixed positive integer K use the selector's fixed seed G6 at a_i=2i,1<=i<=K. Its ACTUAL reduced denominator and COMPLETE primitive residual are

    g_i=gcd(q+2i,H),
    q_i=(q+2i)/g_i,
    R_i=q_i(S−c_i)=(qE−2i d)/g_i.              (1)

These equations include the old exponential and logarithmic endpoints, the seed's entire S−6 error, the changed response, and final rational gcd. The actual seed response is nonzero because q+2i>0. The full kernel and rational coefficient are exactly those in the selector source; no fixed-response arithmetic survival is transferred to these changed responses.

For H nonzero, the selector's Section5 gives

    product_(i=1..K) g_i<=C_K |H|,
    C_K=product_(1<=i<j<=K)2|i−j|.              (2)

For K=2 its sharper exact assertion is

    gcd(g_1,g_2)=1, g_1g_2 divides |H|.         (3)

Neither(2) nor(3) bounds the smaller individual gcd. They are the author-proved CONTENT input, not a newly claimed arithmetic theorem in this note.

## 3. Complete primitive product theorem

Combining the signed COMPLETE formulas(1) with the content budget gives

    product_i |R_i|
      >= |product_i(qE−2i d)|/(C_K |H|).       (4)

For the fixed pair a=2,4 one has the stronger exact inequality

    |R_1 R_2|
      >= |(qE−2d)(qE−4d)|/|H|.                (5)

These bounds are valid when one numerator is zero; their right side is then zero as well. At most one numerator can vanish, by the selector's nonzero block theorem, but no nonzero lower bound is inferred for the other numerator merely from(4).

Let Delta_K=max_i |R_i|. If H is nonzero, (4) also gives the explicit estimate

    |E|<=2K d/q+(C_K |H|)^(1/K) Delta_K/q.      (6)

For K=2, replace C_K by1 in this estimate. To prove(6), put t=qE. If |t|<=2K d its first term suffices. Otherwise every |t−2i d| is at least |t|−2K d; combine this with(4) and product_i|R_i|<=Delta_K^K. This argument retains all signs and does not divide by E.

Suppose c tends to S and q tends to infinity. Then |H| is asymptotic to d q. Therefore the simultaneous small-form condition

    R_i→0 for EVERY i=1..K

necessarily implies

    E=o(q^(−1+1/K)).                           (7)

For the fixed two-output nonzero selector this requirement is

    E=o(q^(−1/2)).                             (8)

This is a necessary condition for BOTH complete primitive forms to be small. It leaves one exceptionally favorable seed output entirely possible and supplies no main irrationality theorem. It does not substitute a polynomial error upper bound for a lower bound on the actual inverse-critical residual.

Conversely, on any subsequence where q|E| tends to infinity,

    max_i |R_i|
       >=(1+o(1)) |E|q^(1−1/K)/(C_K d)^(1/K).  (9)

For the pair, the sharper constant from(3) is

    max(|R_1|,|R_2|)
       >=(1+o(1)) |E|sqrt(q/d).                (10)

If an ACTUAL old signed-error rate |E|=q^(−gamma+o(1)) is known with gamma<1−1/K, then at least one fixed-block primitive error grows at rate at least q^(1−1/K−gamma+o(1)). An upper bound alone does not give such a signed-error rate or this conclusion.

## 4. An unconditional scoped application to farther reflected lattice nodes

The previously proved `REFLECTED_DEPTH_COMPLETE_LATTICE_SPACING.md` gives, for each sufficiently large n divisible by20, a consecutive depth pair bracketing S in the critical quadratic window. Choose its FARTHER node, whose COMPLETE signed error has

    |E_far|=Theta(n^(−3/2)),
    N=n+h is asymptotic to n²/2.                (11)

No such lower bound is asserted for the nearer node. The arithmetic agent's author theorem `agent1_arithmetic/REFLECTED_ACTUAL_FIVE_DENOMINATOR.md` gives actual b5>=v5(N!) at these n,h. The two-depth known-data fixed-response correction from `TWO_DEPTH_SHARED_FIVE_ENDPOINT_LATTICE.md` uses D=N/4−O(log N)<b5, removes the entire actual dyadic layer, and changes the complete center by at most

    exp[−(log5/4)N+O(log N)].                   (12)

Consequently this corrected old center has ODD actual q=B,

    log q>=(log5/4)N−O(log N),
    |E|=Theta(n^(−3/2)),                       (13)

with the same nonzero sign as the farther node. This uses actual five-depth and the complete exponentially smaller endpoint perturbation, rather than an unreduced factorial denominator.

Now apply the response-changing seeds a=2,4. They erase all inherited old prime supports, exactly as the selector source proves, and each center still converges to S. Nevertheless(10),(13) show

    max(|q_2(S−c_2)|,|q_4(S−c_4)|)
       >=exp[(log5/8)N−O(log N)] n^(−3/2)→infinity. (14)

In fact both complete primitive numerators qE−2d,qE−4d have the sign of E eventually. Thus both outputs are nonzero in this particular FARTHER-node application. Formula(14) constrains their simultaneous smallness; it does not bound the smaller of the two actual primitive residuals and does not exclude a single favorable selected seed. It neither applies a lower bound to the nearer inverse-critical node nor re-establishes old prime survival in the new denominator.

## 5. Varying cancellation indices remain a separate mechanism

The exact real cancellation index of the seed is

    a_star=qE/d.

Fixed a=2i cannot track a_star when q|E| tends to infinity. A varying index near this value may have a completely different small numerator in(1). Its actual content g_a=gcd(q+a,H), response, rational coefficient and divisor/index restrictions must then all be retained. Those exact algebraic restrictions are owned by the selector's Section7. Selecting a divisor or an index by approximating S can simply encode ordinary rational approximation; no favorable distribution is assumed here.

The new result is the complete primitive PRODUCT and its necessary old-error threshold. Its purpose is to distinguish a fixed nonzero selector from a simultaneous small-form selector while preserving the genuine response-changing arithmetic freedom. No fixed-response cost is promoted to a global obstruction.
