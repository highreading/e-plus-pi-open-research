> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: single-channel denominator extremizers

Date: 2026-09-13. Reviewer: audit_results.

**Verdict: PASS, all six sections.** Reviewed `raw_single_channel_denominator_extremizers.md` against the exact multiplier caps, high-factor split, and rational good-space construction. No correction is needed. The growing single-channel bound is proved; a mixed retained-rank improvement is correctly left conditional.

## 1. Stronger interpolation Gram comparison

All principal Gram blocks are positive definite. The aa block of H^(-1) is the inverse of H_a-H_ab H_b^(-1)H_ab^T, which is positive definite and no larger than H_a. Inversion therefore gives (H^(-1))_aa>=H_a^(-1). Combining this with the reviewed full-angle bound and congruencing by J_a proves

    G_a<=G<=delta^(-2)G_a,
    delta^2 G_a^(-1)<=G^(-1)<=G_a^(-1).

The lower comparison is indeed stronger than the earlier factor-1/2 bound. For the same data h, f_h^a-f_h belongs to the full zero-data space. The full extremizer is orthogonal to that space, so the exact Pythagorean difference in (2) follows. The square of the norm, not its norm, is E_a-E. All original jet maps and node amplitudes remain in J_a.

## 2. Actual scalar measure and Hermite representers

The diagonal spectral measure dSigma_aa is nonnegative, and multiplying it by F R^2 L_a^2 gives the stated positive measure mu_a. It need not have a positive weight at every eigenvalue, but its moment Gram through the required degree is H_a>0. That is exactly the condition needed for the finite list of scalar orthonormal polynomials and its reproducing kernel.

For every permitted u, the reproducing property gives

    integral u(t) k_(j,r)(t) dmu_a(t)
      =d_j^(-1)[s^r](Q_a(x_j+r_j s)u(x_j+r_j s)).

Thus the stated functions are the exact jet representers, with the radius and factorial encoded correctly. Their Gram is J_a H_a^(-1)J_a^T=G_a, and their linear combination with G_a^(-1)h is the unique minimum-norm interpolant. This does not turn the off-diagonal matrix spectral measure into a scalar measure.

## 3. Number and normalization of retained band directions

The full multiplier dimensions are d_sigma=n-m_sigma, where m_sigma counts true nodes of parity sigma through n. The retained polynomial caps are q_sigma=floor((n-sigma)/2). Thus the codimension of the condition deg(L_a u)<=q_a is at most

    t_a=max(0,ell_a+d_a-1-q_a).

At the present cutoff ell_a=O(sqrt(n)), and the other three terms differ by a bounded integer. This proves t_a=O(sqrt(n)). Composing these top coefficient equations with the linear map h -> u_h^a can only decrease their rank; consequently the asserted data dimension D-t_a is a valid lower bound. It grows because D has order sqrt(n)log(n) with fixed positive constants.

For such data, the same-channel test p_h=(-1)^(h_a)L_a u_h^a belongs to the exact retained component space. Both it and f_h^a have only one component, so their pairing uses dSigma_aa alone. Since 0<R<=1, the pairing is at least E_a, and since R>=2/n the test norm is at most (n/2)sqrt(E_a). The projection variational formula therefore gives ||Pi_L f_h^a||>=(2/n)||f_h^a||. The bound is a norm ratio; its square is 4/n^2. No full-space angle or approximation estimate is needed for this positive test.

## 4. Comparison subspace and exact subtraction

The full zero-data space has dimension p-D, while the reviewed good space has dimension p-D-k_0. Its orthogonal complement inside the zero-data space therefore has dimension exactly k_0=ell_0+ell_1-2. The linear map projecting f_h^a-f_h onto that complement has rank at most k_0. This proves the subspace H_0 of dimension at least D-k_0 and, on it, the exact inclusion f_h^a-f_h in the good space.

Intersecting with the band data space loses at most another t_a dimensions. Retained good subtraction annihilates the difference, so the projected full and single lifts agree after that subtraction. Because the retained good projector has range inside the retained prefix, Pythagoras within that prefix gives exactly (10).

The first term in (10) is controlled on the band. The second need not be small. The displayed first-channel mismatch in (11) is correct: scalar extremal orthogonality uses mu_a=F R^2 L_a^2 dSigma_aa, whereas the positive test pairs against first-channel good vectors with F R L_a^2 dSigma_aa. The other-channel pairings retain dSigma_ab. Neither scalar positivity nor the full-angle bound removes these pairings.

## 5. Conditional approximation and rank count

The scalar best-approximation problem in (12) uses exactly the first-component F norm and the denominator E_a. On H_0, decompose f_h as f_h^a minus a good vector. Approximate the first by its scalar prefix approximant and the second by its retained projection. The two norm ratios are bounded by

    ||f_h^a||/||f_h||<=delta^(-1),
    ||f_h^a-f_h||/||f_h||<=sqrt(delta^(-2)-1).

This proves the stated epsilon_* bound. If its additional threshold holds, the already reviewed good-tail Schur comparison supplies at least D-k_0 controlled denominator directions. Adding the p-D-k_0 existing good directions yields rank at least p-2k_0, exactly as in (14). The estimate is conditional and is not implied by the positive band bound.

The warning about the present constants is necessary and correct: eta=O(n^3 exp(-2sqrt(6n))) and delta^(-1)=O(n^2 exp(2sqrt(6n))) do not show eta/delta tends to zero. Increasing the rational multiplicity to the specified constant 6 changes its approximation error to exp(-6sqrt(6n)); the good defect then has exponential factor exp(-4sqrt(6n)), and multiplication by delta^(-1) still decays exponentially. The dimension order remains O(sqrt(n)log(n)). This requires using the newly specified Q and its changed data space, as the note explicitly states.

## 6. A bounded continuation that directly addresses the mismatch

The first-channel mismatch can be removed by an exact positive compression rather than by a near-unit approximation. On the actual scalar polynomial space V_a=P_(<d_a) in L^2(mu_a), define

    C_a=Proj_(V_a) M_(1/R)|_(V_a).

Then I<=C_a<=(n/2)I. For u_h^a set w_h=C_a^(-1)u_h^a and test p_h=(-1)^(h_a)L_a w_h. The compression identity gives, for every first-channel zero-data multiplier v,

    <p_h,r_a v>_F=<C_a w_h,v>_(mu_a)=<u_h^a,v>_(mu_a)=0.

It also gives <p_h,f_(h')^a>_F=h^T G_a^(-1)h' and ||p_h||_F<=(n/2)sqrt(E_a(h)). Imposing deg(L_a w_h)<=q_a again removes at most t_a data dimensions. Thus the first-channel good constraints can be satisfied exactly on D-O(sqrt(n)) retained test directions. A separate note records the proof and its precise remaining cross-channel obstruction.

This is the proposed next constructive step: use this positive compression as the test normalization, then study only the actual off-diagonal good pairing, rather than trying to make a scalar approximation error nearly zero. It is not a claim that those off-diagonal pairings vanish or have small rank.
