> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of global dyadic Hermite interpolation and branch composition

Date: 2026-09-13. Reviewer: audit_results.

Reviewed raw_dyadic_hermite_interpolation_and_branch_composition.md
in full, against the exact denominator in
raw_rational_surrogate_rank_improvement.md and the independently
reviewed local jet theorem.

**Verdict: PASS.** No correction is required. The global Hermite
isomorphism and the quotient-module composition are exact in the
specified norms. The amplitude obstruction is substantive: the
unweighted actual quotient multiplier is exponentially ill-conditioned,
while its explicitly weighted version has subexponential bounds.
Those are different operators/norms, as the note clearly states.

## 1. Actual nodes and jet coordinates

The shift is exactly M_n=N+3/4, and the dyadic centers are
(3/2)N 2^j. Thus the first node is 5N/2+3/4. The stated J,
multiplicity and D agree with the rational-surrogate denominator.
The largest multiplier lies between N/8 and N/4, giving the
claimed scaled-node upper bound and the minimum gap 3/(2N).

The radius r_j=sqrt(x_j)log N/2 is exactly half the holomorphic
radius. Its scaled version eta_j=r_j/N^2 satisfies the loose
N^(-2)<=eta_j<=1 bounds for N>=8. The local coordinate in (4)
therefore coincides with the physical coordinate z=x_j+r_j t.
Both the r! and N^2 conversions are correct.

## 2. Cardinal inverse with growing multiplicity

Each matrix entry of E is
binom(k,r) alpha_j^(k-r) eta_j^r, and is bounded by 2^D.
The D-by-D operator bound D2^D follows.

The cardinal polynomial H_(j,r) has total degree at most D-1.
At its own node, substituting y=alpha_j+eta_j t cancels the
factor eta_j^(-r), while the truncated reciprocal produces
t^r modulo t^nu. There is no missing eta_j^(-s): the reciprocal
coefficients are taken in the original increment w and are
evaluated at w=eta_j t. At the other nodes, the factor q_j
gives the complete required multiplicity. Thus E H_(j,r)
is exactly the indicated coordinate vector.

The coefficient-one-norm of q_j is bounded by (2N)^(D-nu).
The reciprocal disk of radius 1/(2N) stays away from every
other node, and each normalized factor there has modulus at
least one half. Cauchy's bound is consequently
2^(D-nu)(2N)^s, with no derivative factorial.

Combining these estimates gives precisely

    ||H_(j,r)||_1
      <=nu(4N)^(D-1)(N/2)^r
      <=nu(4N)^(2D).

The Frobenius norm over D inverse columns yields (11).
All multiplicity dependence remains explicit. Repeating the
coordinates for two components preserves the operator and
inverse norms exactly under the Kronecker product with I_2.

## 3. Exact quotient-module map and inverse

The identity Q(N^2 y)=(-1)^D N^(2D) Qhat(y) has the correct
sign and common scale. Remainder modulo Qhat preserves exactly
the local jets used in E, including repetitions. Evaluation of
P_N(N^2 y) at those local coordinates is P_N(x_j+r_j t),
whose multiplication map is d_j T_j. Hence

    M_N=E_2^(-1) Dscr Tscr E_2

and the stated inverse follow without approximation. The
polynomial matrix is a unit in this finite quotient because its
determinant is nonzero at every node; the inverse analytic jets
also prove this directly at each repeated local factor.

The local bound l_N is uniform across all nodes because N is
even, x_j>=2N and x_j<N^2. Thus the odd-seed factor is absent
and every local matrix and inverse has the claimed common
subexponential upper bound.

## 4. Both directions of the global norm comparison

The upper bounds in (18) follow from similarity by E_2 and
the block-diagonal amplitude and local multiplication factors.
For the lower bound, the block with amplitude d_max has norm
at least d_max/l_N, using the upper bound for the inverse of
its normalized T_j. Similarity loses at most cond E_2. The
inverse argument at the d_min block is identical, using the
upper bound on T_j rather than its inverse. Thus both lower
bounds, and the absolute logarithmic comparison in (19), are
valid.

The scalar cardinal sums sigma_N and s_N have exactly constant
local jets d_j and d_j^(-1). Their product is one modulo Qhat.
Consequently S_N=E_2^(-1) Dscr E_2, and multiplication by its
inverse cancels the full scalar block in the exact order:

    S_N^(-1) M_N=E_2^(-1) Tscr E_2.

The subexponential bounds for this weighted operator and its
inverse follow. No assertion about positivity of sigma_N(K_N)
on the original row space is needed or implied. The note also
correctly distinguishes s_N from a Taylor expansion of 1/d_N.

## 5. Genuine exponential variation of the amplitudes

The derivative of log d_N is half the positive trace of the
resolvent, so the first and last nodes attain the minimum and
maximum amplitudes. The lower dyadic endpoint bound gives

    x_last-x_0>=3N^2/16-3N/2>=3N^2/32

for N>=16. The lower spectral bound gives

    x_0-lambda_i<=N^2+5N/2+3/8<=(6/5)N^2

in that same range. Their ratio is at least 5/64, which is
stronger than the 1/16 used. Every eigenvalue factor in the
determinant ratio is therefore at least 17/16. Taking the
positive square root proves (21) with exponent N/2.

The error 2 log B_N is O(sqrt(N)log^2 N)=o(N). Subtracting it
from the amplitude logarithm proves an exponential lower bound
for the condition number of the unweighted M_N. This is not
an artifact of dropping a normalization: it follows while all
actual amplitudes are retained.

## 6. Consequence for the remaining bridge

The proven map acts on a complete two-component quotient module
of dimension 2D. The exceptional projected block has different
dimension, subspaces and physical metric, and includes additional
low-factor directions. The note explicitly does not identify
these maps. Its weighted theorem cannot be inserted into that
physical problem without a proof that transports the amplitude
weight and the relevant restrictions. The exponential unweighted
obstruction makes this distinction mathematically necessary.
