> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Relative leading equivalence of all actual coordinates at proportional size

Agent 3, 2026-10-02. Original author refinement, not independently reviewed. Fix 0<c<1/1000 and b/n->c as in PROPORTIONAL_ACTUAL_CENTER_SIGNED_RATE.md. Let c_b be the actual rational center from its highest B coefficient. Then

    sup_(0<=j<=b) |(c_j-(e+pi))/(c_b-(e+pi))-1|->0.     (1)

Consequently EVERY positive diagonal actual metric, even depending arbitrarily on n, satisfies

    (c_W-(e+pi))/(c_b-(e+pi))->1.                       (2)

The previous proportional theorem gave a shared sign and n-exponent; (1)-(2) give relative leading equivalence, including the prefactor, without requiring a closed formula for that common prefactor. Positive metric tuning has no relative order-one effect in this proportional allocation. No primitive-denominator conclusion follows.

## 1. Target checks

Pre-target archive queries included proportional prefactor, uniform coordinate, gamma sampling, reconstruction limit and mean z. They located earlier fixed-b coordinate equivalence, current uniform growing-b results and other unrelated endpoint statements, but no completed proportional relative-coordinate target in the bounded check. The earlier results are inputs at their stated scopes, not being re-audited.

Primary queries were characteristic polynomial beta ensemble linear statistics one cut asymptotics analytic perturbation, and Toeplitz minors Schur asymptotics elementary symmetric function Hermite Pade. Opened https://arxiv.org/abs/1107.1167, https://arxiv.org/abs/1706.02574 and the full https://arxiv.org/html/1502.06695. The returned Lambert/Ledoux/Webb linear-statistic paper, https://arxiv.org/abs/1706.10251, is background rather than an imported CLT. The proof below uses only elementary sampling, gamma concentration and the empirical law already proved for the actual model. No claim of global novelty is made.

## 2. A deterministic asymptotic for the full gamma insertion

For a circle configuration z_1,...,z_d, set zbar=d^(-1)sum z_l. For 0<=k<=d consider

    U_k(z)=E_(U~Gamma(n+k,1)) E_(I uniform k-subset)
                           product_(l in I)(1-sigma z_l/U).

This is EXACTLY the normalized degree-k term in the full gamma reconstruction. Every actual normalized S_j=s_jR_j/B_j is either U_d (j=0), U_0=1 (j=b), or a positive reference-weight combination of U_(d-j+1) and U_(d-j). No top-column truncation is made.

Uniformly across all configurations |z_l|<=1 and all k<=d<=n/1000,

    U_k(z)=exp[-sigma k/(n+k) zbar]+O(n^(-1/2)).        (3)

To prove this, restrict U to U>=(19/20)n. The uniform gamma-tail argument controls its omitted contribution exponentially. On the main region the logarithm of the selected product is

    -sigma U^(-1)sum_(l in I)z_l+O(k/U^2),

with an absolute uniform constant. The finite-population mean is E sum_I z=k zbar; its complex squared deviation is at most 4k. Since the exponent stays in a fixed bounded disk, the complex exponential is Lipschitz there. Averaging therefore replaces the selected sum by its mean with error O(sqrt(k)/n)+O(k/n^2).

For U~Gamma(n+k,1), E|U-(n+k)|<=sqrt(n+k). On the main region, k|U^(-1)-(n+k)^(-1)|<=C k|U-(n+k)|/n^2. Averaging makes another O(n^(-1/2)) error, and gamma tails are exponentially small. This proves (3). It remains valid at k=0 and k=d; no independence of selected particles is assumed.

Define k_j=max(d-j,0) for j>=1 and k_0=d, and kappa_j=k_j/n. The two middle reference terms differ by one in k. The function k/(n+k) changes by O(1/n), so (3) gives the pointwise full-coordinate estimate

    S_j(z)=exp[-sigma kappa_j/(1+kappa_j) zbar]
                      +O(n^(-1/2)),                    (4)

uniformly in ALL j and every circle configuration. In particular, the deterministic approximation is insensitive to which of the two middle reference terms dominates.

## 3. The explicit equilibrium mean and actual complex averages

The mean of z under the principal equilibrium (3) of the center-rate note is real by reflection. It has the explicit value

    m_c=integral z(x) dmu_c(x)
       =(M^2+c+1)/[(M^2+1)(c+1)]
       =1-M^2 c/[(M^2+1)(c+1)].                       (5)

For a direct calculation, write m_c=2 integral(1+x^2)^(-1) dmu_c-1. The identity

    1/[(1+x^2)^2(M^2-x^2)]
       =1/(M^2+1)[1/(1+x^2)^2
                           +1/((1+x^2)(M^2-x^2))]

and

    (1/pi)integral_(-A)^A sqrt(A^2-x^2)/(1+x^2)^2 dx
       =A^2/[2sqrt(1+A^2)]

give (5), using the normalization and the exact A,C formulas. Put

    t_(j,n)=exp[-sigma kappa_j/(1+kappa_j) m_c]>0.

These constants are uniformly bounded away from zero and infinity. Under every positive principal characteristic tilt q in the fixed compact zero-free neighborhoods, the already proved empirical law implies zbar->m_c in expectation. This convergence is uniform in q: a bounded order-d tilt changes the concentration probabilities by at most exp(O(d)), while the compact-energy exclusion gap has scale d^2. Equation (4) therefore gives

    sup_(j,q) E_q|S_j-t_(j,n)|->0.                      (6)

Keep the original actual phase exp(i Phi) in the integral. Its modulus is one. Thus (6) bounds the absolute difference of the ACTUAL averages, normalized by the positive partition Z_d(q). The odd outer sectors are exponentially small by the same adjacent-norm estimates. Since the actual highest-coordinate average satisfies |A_b(q)|/B_b>=Z_d(q)/2, division is safe, and

    A_j(q)/A_b(q)
       =(s_j B_j/B_b)[t_(j,n)+o(1)]                    (7)

uniformly in j and q on the fixed complex neighborhoods. This conclusion concerns the original oscillatory average. The modulus ensemble is used only to bound a difference, with its nonzero actual denominator independently controlled.

## 4. Transfer through the true shifted scalar saddles

The normalized quotient in (7) is holomorphic in q, so the uniform o(1) error also has o(1) derivatives on smaller fixed neighborhoods. Use the highest-coordinate finite-n saddle contour for EVERY coordinate, rather than assigning a new contour to each ratio. On its central plus or minus Gaussian arc, (7) is a slowly varying multiplicative insertion t_(j,n)+o(1). The actual Gaussian analysis gives

    P_j/P_b=(s_j B_j/B_b)t_(j,n)(1+o(1)),
    F_j/F_b=(s_j B_j/B_b)t_(j,n)(1+o(1)),               (8)

uniformly in j. The central absolute Gaussian integral bounds the quotient's o(1) contribution, and the common leading Gaussian is real and nonzero. The remote contours and BOTH true minus endpoint connectors obey the same uniform exponentially small bounds as in the center-rate theorem; bounded t_(j,n) and the pointwise reconstruction bounds retain their relative suppression.

Dividing the two equations in (8) yields

    (F_j/P_j)/(F_b/P_b)->1

uniformly in j. The complete E_j/P_j and coefficient-zero D/P_0 terms are uniformly exp(-n log n+O(n)), whereas F_b/P_b has the established exp[-(2+c)log(M)n+o(n)] scale. They cannot change this relative result. The exact complete coordinate identity therefore proves (1).

Finally, the full actual Gram center is the positive convex average of the c_j with weights W_jj u_j^2/sum_l W_ll u_l^2. Averaging the uniformly relative o(1) errors in (1) proves (2) for arbitrary positive actual weights. This is a stronger limitation on metric tuning in the proved proportional regime than merely sharing an exponential rate.
