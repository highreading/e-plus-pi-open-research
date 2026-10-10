> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: full channel angle at the square-root cutoff

Date: 2026-09-13. Reviewer: audit_results.

**Verdict: PASS.** The statements in `raw_sqrt_cutoff_full_channel_angle.md` follow from the previously reviewed positive-weight reflection lemma and ratio approximation, with the stated sufficiently-large-index scope. No mathematical correction is needed. In particular, a polynomial of degree proportional to n is used only in the proof of the full angle; it is not part of the dimension count supplied by the separate rational surrogate.

Reviewed directly: `raw_sqrt_cutoff_full_channel_angle.md`, `raw_positive_weight_channel_angle_closure.md`, the dimension and support calculation in `raw_rational_surrogate_rank_improvement.md`, and the positive partial-fraction/Chebyshev construction in `raw_high_ratio_quasilocal_approximation.md`.

## 1. Actual root bounds and support

Set N=2n, b=ceil(192 sqrt(n)), m=ceil(n/8), and H0=(2n+1)I-K_N. The actual true-node lower bound gives, for every high node with index l>b,

    xi_l-(2n+1)
      >=(b+1)(b+2)+3/4-(2n+1)
       =b^2-2n+3b+7/4 >=b^2/2.

The last inequality holds already from b^2>=36864n; it does not use the old condition b^2/n tending to infinity. Relative to M_n=2n+3/4 the gap is larger. The upper actual node bound xi_n<=n(n+1)+1 gives

    xi_n-M_n<=n^2-n+1/4<=n^2.

Thus the retained high roots still lie in the gap range [2n,n^2] used by the rational construction. The optional transfer of the final high root to the other factor does not create a lower high index or a larger node. The reviewed interlacing comparison 2/n<=R(K)<=1 remains applicable.

The polynomial F has degree h<=n/2+1 and positive coefficients in H0. The full surrogate support ends at

    s<=n+2ell_max+2m+2,
    ell_max<=ceil((b+1)/2)+1.

Consequently s+h<=7n/4+O(sqrt(n))<2n. This is the exact boundary condition needed by the supported reflection proof. For an even power H0^(2r), the reflected intermediate polynomial has support at most s+2r; for an odd power the same condition leaves the required one further energy factor. No coupling beyond the finite K_N boundary is silently removed.

The old metric estimate is unchanged: lambda_min(H0)>=1/4, lambda_max(H0)<=7n^2, and cond(H0)<=28n^2. Together with the reviewed coefficient reflection bound ||C_N||<=12n exp(2sqrt(6n)), it gives

    A_n=12sqrt(28)n^2 exp(2sqrt(6n)).

The surrogate's separately orthonormalized full pair therefore has least singular value at least 1/A_n.

## 2. Approximation constants and normalization

The actual row spectral interval has length at most 6n^2. The rescaled high pole obeys

    z_beta-1=2(beta-M_n)/length>=b^2/(6n^2).

The lower bound on the right tends to zero and is at most one eventually. Applying monotonicity of arcosh first, then arcosh(1+u)>=sqrt(u) for 0<=u<=1, is valid even when a particular pole has a larger rescaled gap. The normalized positive partial-fraction weights sum to less than one, so there is no factor equal to the number of poles. The degree-m approximation satisfies

    epsilon_n<=2exp(-(m+1)b/(sqrt(6)n))
             <=2exp(-4sqrt(6n)),

because (m+1)b>=(n/8)192sqrt(n). Since F, R and p_m commute, their operator error is the same in F energy. Since R>=2/n, p_m is eventually positive on the row spectrum.

Let B=diag(B_a,B_b) be the actual individual Gram square roots, E=F^(1/2)X B^(-1), and use the same B for the surrogate. The first block estimate follows from

    R^2 F >=(4/n^2)F,

which gives ||F^(1/2)W_a B_a^(-1)||<=n/2. Hence ||E-E_tilde||<=t_n=(n/2)epsilon_n without any assumption about the full angle. The two surrogate blocks have least singular value at least 1-t_n. Applying the supported angle estimate after separately orthonormalizing those blocks, then undoing that normalization, gives

    sigma_min(E_tilde)>=(1-t_n)/A_n.

Singular-value perturbation now gives

    delta_n=sigma_min(E)>=(1-t_n)/A_n-t_n>=1/(2A_n)

eventually. Indeed A_n t_n=O(n^3 exp(-2sqrt(6n))) tends to zero. This establishes the full actual pair estimate at the new cutoff. It does not establish it at the smaller earlier cutoff ceil(2sqrt(n)).

## 3. The rational exceptional count at the same cutoff

The new high gaps remain inside the original rational bin range [2n,n^2], so its nodes, multiplicity nu and degree D=O(sqrt(n)log(n)) remain valid. Some initial bins can contain no high pole; that causes no change to the approximation proof. There are eventually more than D available first-channel multiplier degrees.

Restricting that multiplier to Q multiples removes D coefficient directions. Replacing RQ by its polynomial numerator introduces no further degree cost: the degree D numerator restores precisely the degree lost by division by Q. Thus this different surrogate has support n+O(b), and its support plus h is still strictly below 2n. The same positive-weight proof supplies the reviewed retained defect O(n^3 exp(-2sqrt(6n))).

With q_sigma=floor((n-sigma)/2), q_0+q_1=n-1, the good dimension is exactly

    (q_a-ell_a-D+1)+(q_b-ell_b+1)
       =n+1-ell_0-ell_1-D.

Writing p=n-1 gives the defect

    k=D+ell_0+ell_1-2=O(sqrt(n)log(n)).

The linear degree m from the full-angle proof does not occur in this count. Both estimates use the same new factorization and F metric, so they may be combined. The original full coefficient map Z is unchanged.

## 4. Full and single-channel Gram comparison

The exact coefficient Gram is

    H=Z^T F^(-1)Z=X^T F X=B E^T E B.

Each block of E is isometric, so ||E||<=sqrt(2), independently of the angle. Thus

    delta_n^2 B^2<=H<=2B^2,
    (1/2)B^(-2)<=H^(-1)<=delta_n^(-2)B^(-2).

The first inequality also proves the individual channel estimates in the source note. Removing R from the first channel costs at most n/2. All resulting full-channel cancellation factors are exp(O(sqrt(n))).

Keep the distinction between the full constraint matrix mathcal J=[J_a,0] and its nonzero channel block J_a. The exact resolvent bridge supplies a full-row-rank mathcal J and retains all node amplitudes and low/high factors. Therefore

    G=mathcal J H^(-1)mathcal J^T,
    G_single=J_a B_a^(-2)J_a^T>0.

Congruencing the preceding inequalities, then inverting, gives exactly

    (1/2)G_single<=G<=delta_n^(-2)G_single,
    delta_n^2 G_single^(-1)<=G^(-1)<=2G_single^(-1).

The inversion direction and normalization are correct. These estimates control full minimum-energy lifts by their actual single-channel counterparts, with only a subexponential cancellation loss.

## 5. Scope

This is an all-sufficiently-large-n theorem; no additional degree construction or numerical scan is used. It closes the full-channel cancellation factor at a cutoff compatible with O(sqrt(n)log(n)) exceptional dimension. It does not prove a bound for the single-channel evaluation Gram, the retained denominator Schur map, or the physical metric containing spectral amplitudes and S^(-1). In particular it supplies no irrationality conclusion by itself.
