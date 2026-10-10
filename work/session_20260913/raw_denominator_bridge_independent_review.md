> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the denominator-to-resolvent exceptional bridge

Date: 2026-09-13. Reviewer: audit_results.

Reviewed raw_denominator_exceptional_resolvent_bridge.md in full,
including its distance/kernel addenda and conditional physical map.
**Verdict: PASS.** No correction is needed. The D denominator
directions are identified exactly; their retained projected Gram
lower bound remains unproved, as the note states.

## 1. Boundary factors and upper Taylor convolution

In the last two recurrence rows, the missing columns are exactly

    [ a_(N-1)a_N,    0             ]
    [ -a_N,         a_N a_(N+1)    ] P_N.

Thus the omitted boundary term is V_0 Gamma_N P_N, without
a transpose, and (1) is correct. The actual seed recurrence
contributes no left source.

The product rule for normalized Taylor coefficients gives
U_(j,r)=sum_(s<=r) W^Gamma_(j,s) A_(j,r-s). Therefore the
right multiplier is the upper block-Toeplitz matrix with the
displayed block order. Reversal of both derivative indices
turns it into the already reviewed lower Toeplitz operator;
it does not transpose the two-by-two coefficient blocks.

The normalized resolvent conversion in (4) is also exact:
the factor eta_j^r contributes N^(-2r), the resolvent power
contributes N^(2r+2), and Gamma_N/N^2 removes the final N^2.
The full resolvent and Toeplitz lower bounds consequently give
the claimed lower bound for U. Selecting one component in each
block is an isometry on its coefficient space and preserves
that lower singular-value bound in the full row space.

## 2. Strict coprimality and the actual polynomial coordinates

The strict eigenvalue intervals in Section 2 follow from min-max
on the indicated finite-dimensional subspaces: multiplication by
u^2/4 has a strictly positive minimum on the unit sphere of
each such subspace, and its complement from 1/4 does as well.
These intervals exclude every integer-plus-3/4 artificial node.
The newer uniform quantitative gap is reviewed separately in
raw_uniform_node_gap_independent_review.md; strict coprimality
alone suffices for the algebra here.

I checked (11) directly rather than assuming an unrestricted
finite Krylov identity. The seeds satisfy

    Phi_N(z)^T v_0=(1,0)^T,
    Phi_N(z)^T v_1=(0,1)^T,

using the actual offset v_1=e_1-(sqrt(3)/2)e_0. For a power
K^m with m<=n-1, the preceding power K^(m-1)v_sigma has
support at most index 2n-3=N-3. The final two coordinates
in the boundary correction therefore vanish at every induction
step. Hence Phi_N(z)^T K^m v_sigma=z^m e_sigma exactly
through all the degrees actually used. Since deg(Q_sigma u_sigma)
is at most n-1, equation (11) has no omitted finite-boundary term.

Differentiating that identity gives (12), including the factor
d_j^(-1) and the physical radius r_j. Both low and high true
node factors remain in the scalar multiplication map. Its
coprimality with the artificial denominator makes all these
jets vanish exactly when u_a is divisible by Q. The degree
caps then give codimension D and full row rank of J_a, with
the other channel unrestricted.

## 3. Exact complement in the energy metric

With Y=F^(-1/2)Z, the matrix H=Y^T Y is positive definite
because the actual coefficient map Z is injective. The frame
formula for Pi_W is the orthogonal projector onto ran Y.
For C_a=F^(1/2)U_a, the identity C_a^T Y=U_a^T Z=J_a
has no remaining F factor. It proves both versions of G_a
and its positive definiteness.

The restricted energy image is exactly W intersect ker C_a^T.
The range of Pi_W C_a is its orthogonal complement inside W,
with Gram G_a. Thus O_D=Pi_W C_a G_a^(-1/2) is an exact
orthonormal frame for all D missing denominator directions.
The alternate formula using Y,H and J_a follows directly.

This does not provide a lower bound for G_a from the full-space
Gram of U_a. The intervening projection and F factors are
mathematically distinct, and the note retains them.

## 4. Retained Schur block, distance and kernel

The retained frame U_L is an isometry because its Gram reduces
to F[L,L]. The projected good frame has Gram R_g^2 and is
injective because its defect is below one. The dimensions are
consistent: the retained coordinate space has n+1 entries,
the good space has g=p-D-k0, and its complement has D+k0+2.

Substituting O_D into U_e^T U_L^T O_D gives exactly (20):
U_L^T Y=F[L,L]^(-1/2) Z_L. Squaring that identity gives
the full Gram in (21), with every projector and normalization
in the correct order. Its middle factor is the retained
projector after the projected good directions are removed.

The estimate for the removed good component follows from
O_g^T O_D=0 and ||(I-Pi_L)O_g||<=eta. Its squared norm is
at most eta^2/(1-eta^2), with the stated positive-semidefinite
sign of the correction. This is not a relative error bound
against an unknown smallest eigenvalue.

The distance formula (21a) follows because U_L is isometric
and U_L U_g spans Pi_L G. The vector in the kernel formula
(21b) has exactly the stated subtracting coefficient R_g^(-1)
U_g^T U_L^T O_Dv. It kills the retained projection when
T_Dv=0. Conversely, decomposition into the orthogonal good
and denominator components and invertibility of R_g recover
that coefficient uniquely. No low-factor component enters
this correspondence.

## 5. Conditional second Schur step and physical coordinates

If the specified Gram has lower bound gamma_n^2 I, the polar
frame V_D and its complement V_ell give the exact block matrix
(22). The off-diagonal block has norm at most one, because
the original residual is a product of contractions. The
triangular eliminator and its inverse each have norm at most
1+gamma_n^(-1). Its rank contribution is D, yielding

    rank Z_L=p-k0+rank T_low.

For the transpose kernel, no hidden elimination factor is
required: T_D^T u=0 says u=V_ell v, and the remaining
condition is T_low^T v=0. Consequently composing the previous
physical map J_e with V_ell gives exactly J_low and the
compressed physical Gram in (24). The low-cardinal, spectral
amplitude and energy factors have all been retained.

The new true/artificial separation and the local factor-jet
bounds may quantify parts of J_a. They do not by themselves
bound the two projected angles in (21), prove T_D full rank,
or remove these D directions unconditionally. The source
correctly states this remaining limitation.
