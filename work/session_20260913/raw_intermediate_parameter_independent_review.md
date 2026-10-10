> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of conditioning down to parameters of order the cut

Date: 2026-09-13. Reviewer: audit_results.

Reviewed raw_intermediate_positive_parameter_conditioning.md in full,
and checked the exact early-cut estimate and seed conventions in
raw_global_adjacent_branch_conditioning.md and
raw_two_step_channel_transport.md.

**Verdict: the substantive theorem passes.** The proof is uniform for
all real x>=2N and does not extrapolate fixed-positive-ratio constants.
One normalization clarification was sent to the author: when the
singular-value statement is transferred to rational row normalization,
its determinant must also be changed, as recorded in Section 6 below.
This does not affect either condition-number theorem.

## 1. Exact parity energies and coefficient bounds

The identities a_l^2=l^2/4+delta_l, with delta_0=0 and
0<=delta_l<=1/12, are exact. The product estimate for c_l follows
from l/2<=a_l<=l/2+1/(12l), with the negative-index edge weights
set to zero as stated. The polynomial parts in

    d_l+c_(l-2)+c_l

sum to 3/4, including l=0 and l=1. The errors have the claimed
nonnegative signs, and their total is safely below the stated
bound two.

Thus the exact parity compression K_0=-D_graph+diag(V_l) holds.
At its top coordinate the outgoing edge to the first omitted
same-parity vertex remains as a Dirichlet contribution to the
diagonal. At the original bottom coordinate the outward edge has
weight zero. These conventions reproduce the diagonal of the
principal compression; deleting the top ghost edge would not.

Since K=K_0-J and -jI<=J<=jI, the operator xI-K lies between
D_graph+(x-j-2)I and D_graph+(x+j+2)I. Inverting these positive
operators gives precisely (6), with the correct direction of both
inequalities. For x>=2N, j<=N, N>=4, every comparison mass is
at least x/4. This also checks the asserted invertibility directly.

## 2. Both constant-chain boundary formulas

The characteristic relation is

    y/w=q+q^(-1)-2,

where q=exp(-2 asinh(sqrt(y)/j)) and w=j^2/4. Solving the
two-point recurrence with its retained left Dirichlet edge gives
the two ratios in (8). The remote conditions v_L=0 and
v_L=v_(L-1) respectively produce the exponents 2L,2L+2 and
2L-1,2L+1; their offset is correct.

For L=1 the formulas reduce to 1/(y+2w) and 1/(y+w).
The displayed error bounds (9) follow immediately for 0<q<1.
In particular there is no missing factor (1-q)^(-1), even when
y/j^2 tends to zero. This absence is important for the new range.

## 3. Layer support and exact cut-edge bracketing

For the reversed parity chain starting at b=j-1 or j-2, the
L-vertex layer uses the top ghost edge c_b, its internal edges,
and the far crossing edge c_(b-2L). Thus the author's list of
L+1 potentially used edge weights has exactly the right endpoints.
The lower product bound (j-2L-1)^2 and upper bound j(j+1),
together with the product error, imply (11) for both parities.

The support and smallness conditions can be made simultaneous:

    delta <=160 log(N)/j+160 log(N)/sqrt(x)+24/j.

For j>=A log N, one sufficiently large absolute A, followed by
one sufficiently large absolute N, makes delta<=1/8 and puts the
entire layer strictly inside both parity chains. No upper bound
on x is needed.

For any positive chain operator, the boundary inverse entry is
the reciprocal minimum energy under v_0=1. Deleting the exterior
and its crossing edge gives the Neumann lower energy, hence the
upper inverse bound. Restricting all exterior values to zero
retains that crossing edge as a Dirichlet edge, increases the
minimum, and gives the lower inverse bound. The unexamined part
of the actual chain requires only positive edge and mass energies.

The relative edge bounds compare the full positive energy forms,
including their unchanged mass terms, within factors 1+/-delta.
This proves (12) without an uncontrolled norm perturbation of the
far part of the chain.

## 4. Uniform small- and large-ratio errors

Writing a=j/sqrt(x), the inequality

    (1+a) asinh(1/(2a)) >= (1+a)/(2a+1) >=1/2

proves L asinh(sqrt(y)/j)>=10 log N at every comparison mass.
The factor 2 in log q and 2L-1>=L then give the claimed N^(-20)
tail. This proof covers both a tending to zero and a tending to
infinity; there is no compact-ratio hypothesis.

Differentiation gives exactly

    d(log r_infinity)/dy=-1/sqrt(y(y+j^2)).

Over the two comparison intervals, the absolute logarithmic
change is at most

    2(j+2)/(j sqrt(x)) <= 2.5/sqrt(x)    for j>=8,

which is within (15). Combining these bounds with the scalar
Dirichlet/Neumann estimates bounds both diagonal comparison
matrices between scalar multiples of the identity. The Loewner
sandwich therefore bounds the full actual symmetric 2-by-2
resolvent block, including its off-diagonal entry, relative to
m(x/j^2)/j^2. It gives (16) with one absolute constant.

The loose explicit error 8delta+10/sqrt(x)+4N^(-20) is safe
for delta<=1/8 and sufficiently large N. Collecting it yields
exactly log(N)/j+log(N)/sqrt(x), with an absolute coefficient.

## 5. Actual transfer, initial cut, and accumulation

The transfer identity has the correct order:

    T_j=Gamma_j^(-1) R_boundary^(-1).

Indeed M=Gamma^T R_boundary Gamma, so M^(-1)Gamma^T equals
that product. The coefficient estimates give
Gamma=(j^2/4)(I+H), ||H||<=4/j. Inverting both factors in
their actual order gives the positive scalar 4/m and the bound
(18); no commutation or first-order expansion is required.

At j>=J_N of the specified parity, choosing A sufficiently
large makes all relative errors at most one half. Summation
along the step-two sequence gives O(log^2 N+N log N/sqrt(x))
for both logarithmic condition and the two ordered-product norm
bounds. The scalar factors are positive and harmless for
conditioning, but are not discarded from the actual determinant.

For the growing early cut, the previously proved exact estimate
(20) only needs x>=2(j+3/4). This holds uniformly for
j<=J_N=O(log N), x>=2N, once N is large. Also j^2<=x there,
so 2048/j is a valid bound. Starting at a fixed sufficiently
large cut makes these errors small and costs only O(log J_N).
Thus the proof does not invoke an earlier theorem with constants
depending on a shrinking lower ratio.

At the fixed seed, the degree bound and the exact Casoratian
give bounded even conditioning and O(x) odd conditioning. The
last term (N mod 2) log(1+x) is therefore necessary in this
argument and is retained correctly. On 2N<=x<=C' N^2 it is
absorbed by the claimed O_(C')(sqrt(N) log N) bound.

The exact determinant and the condition bound imply (3) for
both actual singular values by their product and ratio. Nothing
here implies a many-node or confluent interpolation inverse.

## 6. Rational-normalization clarification

With the already stated normalization bridge

    P_N=diag(sqrt(2N+1),sqrt(2N+3))
        P_N^rat diag(1,1/sqrt(3)),

the condition numbers differ by at most a fixed factor, so
(1)--(2) transfer as claimed. The determinant for (3), however,
must be

    D_N^rat=sqrt(3) D_N/sqrt((2N+1)(2N+3)).

Using D_N^rat and H_N+log 3 gives the corresponding rational
singular-value bounds. Keeping D_N would miss a factor of
order N in the determinant; this cannot be absorbed into an
absolute multiplicative constant. The correction was communicated
directly to the author. It affects only the final normalization
sentence, not the proof or the new parameter range.
The author has applied the correction explicitly in Section 1.
