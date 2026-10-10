> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Companion overlap, adaptive canonical bounds, and large-selector phase requirements

Status: main-agent author deductions, not independently reviewed. This note preserves four deductions previously stated but not saved. The new relative-saddle theorem and completed dyadic review have been reported by their authors; their full texts still require main inspection at this checkpoint. Conditional applications below retain those dependencies. No new computation or numerical selection is claimed. The rationality or irrationality of e+pi remains unresolved.

## 1. Adaptive canonical exponential budget

Consider the actual factorial B-only canonical center, with even n, 3<=b<=n, d=b-1, and factorial-weight parameter 1<=m_w<=floor((b-1)/2). Put M=1+sqrt(2). Retain the exact companion bridge and canonical energy argument in agent3/CANONICAL_COMPANION_TRANSFER.md, which the main has read in full.

For the enlarged domain, explicitly assume the following estimates in that domain:

    ||T^(-1)||_2 <= 2^(d/2) M^(-n) Kinv,
    Kinv <=512 sqrt(bn) exp(b)(2304n/b)^d,
    ||T||_2 <=9*2^(d/2)M^n,
    ||Krec||_2 <=2(n+b)^d,
    wmin >=(2n)^(-b).

The adaptive inverse input has author status; its extension is not independently accepted merely because the earlier slow-growth inverse was reviewed. The other displayed bounds must also hold on every sequence to which this section is applied.

Substituting the inverse bound into the retained canonical energy calculation gives

    Ccan=18b(n+1)^d(n+b)^d Kinv 2^d/wmin,
    E <=54pi sqrt(bn) Ccan/((n+1)n!),

where E is the positive direct-selector exponential-error bound, so |alpha-e|<=E. The universal forcing-height bound also gives

    E >=27 sqrt(n)/(2^b(n+1)n!).

This last inequality is a lower bound for the chosen majorant E, not for the actual error |alpha-e|.

The explicit factors imply

    log Ccan=O(b log n+b log(n/b)+log n).

Consequently, on every sequence with b=o(n), the logarithm of Ccan is o(n log n). Stirling's formula and the two bounds for E prove

    -log E ~ n log n.

Thus the canonical factorial exponential budget extends conditionally to even b=o(n), without requiring subfactorial primitive-selector height. This extension needs the displayed estimates in the enlarged domain; it must not be presented as part of the already reviewed slow-growth theorem.

Writing the exact canonical center as c=alpha+gamma, gamma=kappa+beta, the published pi input and PI_COMPANION_NECESSARY_BUDGET_DRAFT.md then imply that bounded complete primitive errors require

    liminf log den(gamma)/(n log n)>=5/82.

A proved upper rate strictly below 5/82 instead implies primitive-error divergence. The actual joint gcd determining den(gamma) remains essential.

## 2. Retaining denominator overlap in the complete inequality

Let alpha,gamma be rational. Define

    c=alpha+gamma, q=den(c), B=den(gamma),
    C=gcd(q,B), R=q|c-(e+pi)|.

All denominators are positive and reduced. Suppose |e-alpha|<=E, E>0. Use the retained e inequality with nu=2+epsilon and constant C_epsilon>0, and the published pi inequality with mu=36/5 and constant C_pi>0.

Since alpha=c-gamma,

    den(alpha) divides lcm(q,B)=qB/C.

Therefore

    E>=C_epsilon(qB/C)^(-nu),
    1/q<=C_epsilon^(-1/nu) E^(1/nu) B/C.

The complete decomposition gives

    C_pi B^(-mu)<=|pi-gamma|<=E+R/q.

Combining the two inequalities proves

    C_pi<=E B^mu
          +R C_epsilon^(-1/nu) E^(1/nu) B^(mu+1)/C.   (1)

No contour-sign premise, logarithmic-dominance premise, or dyadic theorem is used in (1).

Suppose X tends to infinity,

    -log E=X+o(X), R is bounded,
    liminf log C/X>=h>=0.

Then necessarily

    liminf log B/X>=min{1/mu,(1/2+h)/(mu+1)}
                   =min{5/36,(5/41)(1/2+h)}.          (2)

Indeed, if (2) fails, choose a subsequence with log B/X bounded above by a constant strictly below both thresholds. Choose epsilon sufficiently small and use arbitrarily small slack in the lower rate for C. Both terms on the right of (1) then tend to zero, contradicting C_pi>0.

If B divides q eventually, C=B. Substituting this exact identity into (1), rather than treating C as an independent fixed rate, gives the stronger necessary condition

    liminf log B/X>=1/(2mu)=5/72.                    (3)

No divisibility B|q is asserted for the constructions under investigation. A large denominator contribution to q with a small contribution to B does not establish it. The relevant arithmetic data are the actual pair (B,gcd(q,B)), with the endpoint correction retained.

## 3. A predetermined adjacent parity-qualified pair

Fix rho>0, let n=2^s with s>=3, and put k=n/4. Define

    m0=floor(rho n log n),
    m=2k ceil(m0/(2k))+k.

Then 0<=m-m0<3k, so m=rho n log n+O(n). Both m and m+1 have residues in [k,2k-1] modulo 2k. The saved polynomial parity argument gives

    v_2(U_m)=v_2(U_(m+1))=n/2.

Thus both direct centers exist. This conclusion does not require a maximizer search or the complete denominator theorem.

For this section assume the reported relative-saddle results, uniformly in the stated block:

    log|J_m|=m log 2-n log(m/n)+O_rho(n),
    J_(m+1)/J_m=-2i(1+o(1)).                        (4)

The full proof of (4) must be inspected before its application is accepted. In particular, a merely additive endpoint enclosure would not suffice.

Write J_m=a+ib. The ratio in (4) gives

    (Im J_m,Im J_(m+1)/2)=(b,-a)+o(|J_m|).

Hence, eventually,

    max(|Im J_m|,|Im J_(m+1)|)>=|J_m|/(2sqrt(2)).   (5)

At both nodes the retained forcing estimates give

    2^(n/2)<=|U_j|<=exp((n/2)log log n+O_rho(n)).

The exact normalized logarithmic remainder is

    (-1)^(n+1)2^(n+2)Im J_j/U_j.

The entire exponential residual is bounded by exp(-n log n+n log log n+O_rho(n)). Retain the saved Gaussian-rational endpoint sums Z_j with normalized truncation error at most exp(-2n log n).

Choose j_n to be the smaller maximizer of |Im Z_j/U_j| over j=m,m+1. This is a finite rational selection rule; it has not been executed. The uniform truncation bound shows that its actual normalized logarithmic magnitude is at least the maximum actual magnitude over the pair minus twice that truncation bound. Equation (5) and the full exponential bound therefore imply

    rho(log 2)n log n-(3/2)n log log n-O_rho(n)
      <=log|c_(j_n)-(e+pi)|
      <=rho(log 2)n log n-n log log n+O_rho(n).       (6)

Consequently, conditional on (4),

    log|c_(j_n)-(e+pi)|/(n log n)->rho log 2.

This is raw complete-error divergence for a specified selection from each predetermined pair. It does not establish divergence at both endpoints, every eligible node, or the original forcing-only maximizer.

If the separately reported complete dyadic theorem applies, then at these parity-qualified nodes

    v_2(q_j)=3n/2+2j-s_2(n)-s_2(n+4j),

where q_j is the actual reduced center denominator. It follows that

    liminf log(q_(j_n)|c_(j_n)-(e+pi)|)/(n log n)
      >=3rho log 2.

Raw-error divergence already implies primitive-error divergence because q_j>=1; the dyadic theorem strengthens the rate.

## 4. Necessary exponentially precise phase alignment

Continue within the reported saddle domain and assume its magnitude estimate. Put

    X=n log n, a=rho log 2,
    log|J_m|=aX+o(X), log|U_m|=o(X).

Retain the exact complete decomposition

    c_m-(e+pi)=epsilon_m
       +(-1)^(n+1)2^(n+2)Im J_m/U_m,
    |epsilon_m|<=exp(-X+o(X)).

Let q_m be the actual reduced denominator, assume

    liminf log q_m/X>=g>=0,

and suppose the complete primitive errors satisfy

    R_m=q_m|c_m-(e+pi)|<=exp(-sigma X+o(X)),
    sigma>=0.

Bounded R_m is the special case sigma=0. The exact decomposition yields

    |sin(arg J_m)|
      <=|U_m|[R_m/q_m+|epsilon_m|]
                        /(2^(n+2)|J_m|).

Therefore

    |sin(arg J_m)|
      <=exp(-(a+min(1,g+sigma))X+o(X)).             (7)

For delta=dist(arg J_m,pi Z), one has 0<=delta<=pi/2 and delta<=(pi/2)|sin(arg J_m)|. Thus (7) also bounds that phase distance.

When the complete dyadic theorem supplies g=2rho log 2=2a, bounded primitive errors require phase alignment at rate

    a+min(1,2a).

The reported adjacent ratio prevents both members of a neighboring pair from satisfying such alignment. It does not exclude a sequence choosing isolated favorable nodes. A relative saddle remainder of order 1/n is much larger than the exponential phase scale in (7), so that remainder alone cannot settle the isolated-node question.

## 5. Status and next verification

The overlap inequality is an elementary author proof using the already located published pi theorem and retained e bound. The adaptive canonical extension requires the displayed enlarged-domain estimates. The adjacent selection and phase requirements use the reported relative-saddle theorem; its proof remains to be inspected at this checkpoint. The strengthened dyadic rates require the exact domain of the completed review to be read.

No new computation was performed in preparing this note. These deductions do not establish small primitive forms on a useful unbounded sequence and do not resolve the actual e+pi problem.
