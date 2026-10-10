> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the local resolvent limit and dyadic transport

Date: 2026-09-13. Root verification of
`raw_two_step_channel_transport.md` and
`raw_local_boundary_resolvent_limit.md`.

**Verdict: both the finite estimates and the uniform O(1/N)
local limit pass.**

For the diagonal balance, the two parity blocks of K0 are aligned
one original index apart. The stated bounds on the differences
of diagonal and off-diagonal entries follow from
a_j^2=j^2/4+delta_j and a_j=j/2+O(1/j). For odd size the added
decoupled first entry leaves the actual boundary resolvent value
unchanged; its one omitted coupling is bounded. Row sums give
the claimed O(N) matrix difference. The resolvent identity then
gives O(N^-3) balance of the two diagonal boundary entries after
the two K0-to-K perturbation errors are included.

Expanding Gamma^T R Gamma retains its diagonal difference,
cross term, and the square of the lower off-diagonal entry. The
four separate bounds in the note sum to its displayed constant.
Combining that balance with the independently reviewed off-diagonal
bound justifies a scalar normalization of T_N, not only a diagonal
normalization. The ordered product estimate uses the full sum of
1/N and the inverse inequality for errors <=1/2. Its correction
is allowed to remain O(1) on a dyadic interval, as required.

For the local limit, the half-line matrix with diagonal -1/2 and
off-diagonal 1/4 has its spectrum in [-1,0]. The explicit vector
w_j=4q^(j+1) satisfies both the interior and boundary resolvent
equations and is square summable. Its squared norm is -m'(c).

Reversing each actual parity block gives coefficients at depth j
within O((j+1)/N) of the half-line constants. The zero extension
is harmless: at its omitted coupling and throughout its tail the
depth is already of order N. The estimates are not uniform
operator-norm convergence, and the proof does not use them as such.
Instead, the three diagonals acting on the geometric resolvent
vector are bounded by its explicitly summable weighted norm.
This proves the vector O(1/N) estimate via the resolvent identity.

The squared-resolvent estimate compares squared vector norms.
It does not differentiate an uncontrolled error. Restoring the
opposite-parity J/N^2 coupling costs O(1/N) in both resolvents
and squared resolvents. The compression of the square is correctly
kept distinct from the square of the compression.

The expansion Gamma_N/N^2=I/4+O(1/N) then yields exactly the
m(c)/16 and -m'(c)/16 constants. The derivative in the second
formula is with respect to the original parameter x; the powers
of N are consistent. Uniform positive lower bounds justify the
inverse used to obtain T_N=lambda(c)I+O(1/N), with
lambda=4/m=(sqrt(c)+sqrt(c+1))^2.

On a fixed dyadic interval, these errors form an ordered product
with uniformly bounded norm and inverse. The scalar logarithm is
a step-two Riemann sum. The step-size factor cancels the factor
two in log lambda and gives the stated asinh integral with O(1)
error. The antiderivative and the coherent-vector interpretation
both check.

No global high-row mixed-cofactor estimate is supplied by these
same-parameter results. Their finite-size correction and parameter
dependence remain present.
