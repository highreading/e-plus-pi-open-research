> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent root review of the joint dual Hankel and even Toeplitz theorem

Date: 2026-09-13. Verdict: PASS.

I independently checked raw_joint_dual_hankel_and_even_root_product.md,
including the all-index arguments, not merely the frozen examples.

The coefficient equation W_k=S_k/(k-n)! is used only for k>=n.
It gives exactly q(D)H=(x-1)^n V. The reversal of binomial indices in
the moment functional is correct, as are the derivative factorials
in equation (7). Reconstructing S,W,T from a kernel vector is injective
and returns the original X_n annihilator, so the uniqueness proof does
not assume nonzero principal Hankel minors. The quadratic functional
identity uses the coefficient U(0), not the different coefficient u_n.

The residue derivation of the Pearson identity retains sigma', yielding
tau=z^3+2z^2+z-2n and the stated four-term finite moment recurrence.

For even n=2m, reversing the Hankel rows really gives
A_ij=a_(n+i-j), and the stated symbol has that Fourier orientation.
Its Hermitian real part is bounded below by e^-1 cos(1) times the
positive Gram matrix of |1+z^2|^(2m). The imaginary part satisfies
the claimed sector bound. Strict accretivity proves invertibility;
the real diagonal inverse entry is strictly positive. Hence both
V(1) and u_n are nonzero without an assumed U(0) condition.

I checked the binomial Toeplitz determinant proof including potential
out-of-range entries: the row factorials used are all nonnegative,
and falling factorials give the required zeros. Translation of the
evaluation points leaves the Vandermonde determinant unchanged for
polynomials of degree at most L-1. At the translated points the
matrix is triangular with exactly the stated diagonal. The even
block has size m+1 and its corner cofactor has size m, giving
((2m)!)^2/(m!(3m)!) with no missing odd-block factor.

For A=H+iK, the Hermitian real part of its inverse is
H^(-1/2)(I+C^2)^(-1)H^(-1/2). The resulting inverse bounds have the
correct directions. Inverting the positive scalar entry in (13)
gives the constants in the root-product bound. Independently expanding
Stirling's formula gives n log n+((3/2)log 3-1)n+O(log n), so the
limiting constant is indeed 3 sqrt(3)/e.

The root-product result does not locate every root. Its factorial
lower bound on the primitive endpoint height is valid because the
leading coefficient of V is a nonzero integer. Taking d=n in the
earlier Legendre-test absolute-mass proof replaces n! by (2n)! with
the same displayed constants. The separately audited all-index
Qhat(0) lemma now permits this last improvement for every n.

The degree-two sign obstruction is exact: the arc polynomial has
opposite strict signs at its outer endpoint and center, hence also
at nearby interior points of positive weight. The negative Hankel
quadratic value does not contradict accretivity after a row reversal,
which is not a congruence.

I replayed the frozen n=1,2 checker with the session's existing math
libraries; every identity passed. No new canonical degree was solved.
No changes to the mathematical statements were needed.

The remaining limit is substantive: these are polynomial geometry and
normalization results. They do not bound the signed sum of the two
error integrals or the fixed-combination gcd. Those factors are
correctly preserved in the note.
