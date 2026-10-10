> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Strict block Loewner positivity and an exact many-node determinant

Date: 2026-09-13. Original root continuation of the reviewed
two-channel matrix Christoffel-Darboux identity. Independent
verification requested.

This result compares several spectral parameters while retaining
both channels at every parameter. It does not assert positivity
of the scalar mixed evaluation minors in the actual high kernel.

## 1. Definitions and the Gram identity

Let N>=2, K=K_[0,N-1], B=iota_N Gamma_N, and

    M(x)=B^T(xI-K)^(-1)B.

Here K is exactly the real symmetric row compression and Gamma_N
is the invertible triangular boundary matrix from
`raw_branch_matrix_christoffel_darboux.md`. Choose r distinct real
numbers x_1,...,x_r outside the finite spectrum of K. Define the
2r-by-2r block matrix L by

    L_ij=(M(x_i)-M(x_j))/(x_j-x_i), i!=j;
    L_ii=-M'(x_i).

With R_i=(x_i I-K)^(-1), the resolvent identity gives

    L_ij=B^T R_i R_j B,
    L=W^T W,  W=[R_1 B | ... | R_r B].                 (1)

This formula applies whether the real parameters are in the same
component of the resolvent set or different components. No scalar
entrywise positivity is assumed.

## 2. Strict positivity up to the full dimension

For 2r<=N, L is positive definite.

First, the block Krylov matrix

    V_r=[B | KB | ... | K^(r-1)B]

has column rank 2r. A multiplication by the pentadiagonal K can
propagate support at most two coordinates to the left. In the
last 2r coordinates, reverse the order of its r two-column blocks.
The resulting block triangular matrix has invertible diagonal
blocks: each is a product of distance-two boundary coupling
matrices, ending in Gamma_N. Every such matrix is triangular
with nonzero diagonal. This proves the rank assertion, for odd
and even N alike. Rows outside those last 2r coordinates do not
affect it.

If W(v_1,...,v_r)^T=0, multiply by the invertible polynomial
P(K)=prod_i(x_i I-K). The result is

    sum_i L_i(K)B v_i=0,
    L_i(t)=prod_(j!=i)(x_j-t).

These r scalar polynomials form a basis of the polynomials of
degree at most r-1: at t=x_i only the i-th is nonzero. Independence
of V_r therefore makes every v_i zero. Thus W has rank 2r, and
(1) proves strict positive definiteness.

In particular every selection of one nonzero channel vector at
each chosen parameter gives a positive definite scalar Gram
matrix by block congruence. This is positivity of a Gram matrix
of resolvent columns, not of the original evaluation matrix.

## 3. Exact full determinant when N=2r

Write Delta(x)=prod_(i<j)(x_j-x_i). When N=2r, V_r and W are
square and

    |det W|=|det V_r| Delta(x)^2
              / prod_i |det(x_i I-K)|.               (2)

Proof. Let T be the scalar coefficient matrix of L_i(t), with
rows ordered by powers 0,...,r-1. Then

    P(K) W=V_r (T tensor I_2).

The coefficient determinant has |det T|=|Delta(x)|. For example,
evaluating the coefficient matrix at the x_i gives a diagonal
matrix with entries prod_(j!=i)(x_j-x_i); taking determinants
and dividing by the ordinary Vandermonde determinant proves this
identity including its absolute value. Consequently
det(T tensor I_2)=(det T)^2=Delta(x)^2. Also
det P(K)=prod_i det(x_i I-K). Taking absolute determinants proves
(2). Squaring yields the exact positive identity

    det L=(det V_r)^2 Delta(x)^4
                / prod_i det(x_i I-K)^2.             (3)

All quantities in the denominator are nonzero by the spectral
assumption.

For this actual matrix, the Krylov determinant is explicit:

    det V_r=prod_(m=1)^r det(Gamma_(2m))^m >0,
    det Gamma_j=a_(j-1) a_j^2 a_(j+1).               (4)

Indeed group the rows in pairs (0,1),(2,3),...,(N-2,N-1).
After reversing its two-column blocks, V_r is block triangular.
The diagonal block in row pair j, counted from zero, is
Gamma_(2j+2) Gamma_(2j+4) ... Gamma_N. A fixed Gamma_(2m)
appears in exactly m such blocks. Reversing blocks of size two
has positive determinant sign. Taking the product of the block
determinants proves (4). Combining (3)-(4) gives a full finite
determinant with no unknown cofactors.

## 4. Relation to branch evaluations and the unresolved restriction

The reviewed CD identity expresses the same blocks as

    L_ij=P_N(x_i)^(-T)
          [sum_(k<N) R_k(x_i)^T R_k(x_j)] P_N(x_j)^(-1).

Thus the strict positivity and determinant formula apply to a
precisely normalized two-channel evaluation Gram kernel. The
actual high-row matrix differs in two material ways: it retains
only the parity-selected channel at each prolate node, and it
retains the high interval of rows rather than all rows below N.
Deleting those rows is not a positive congruence of the full Gram
matrix. The present theorem therefore does not prove its rank,
its smallest singular value, or its maximal-cofactor bounds.

Nevertheless (3) supplies an exact many-parameter positive
determinant and a concrete basis for studying these restrictions.
The immediate next question is whether a controlled Schur
complement or complementary-minor identity relates the actual
high-row, alternating-channel selection to this full block object.
Any such step must retain the relevant principal subspace and
its conditioning; positivity of the full object alone is
insufficient. No irrationality or primitive-height assertion is
made here.
