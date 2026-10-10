> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A square-root bound on the number of positive row eigenvalues

Date: 2026-09-13. Original root derivation; independent review requested.
This concerns K_N, not the accessory cubic or the column spectrum.

Let a_0=0 and a_j=j^2/sqrt(4j^2-1) for j>=1. The real symmetric
N-by-N row matrix has diagonal b_k=a_k^2+a_(k+1)^2-k(k+1),
distance-one entries -a_(k+1), and distance-two entries
c_k=a_(k+1)a_(k+2), for 0<=k<N. Let n_+(K_N) count strictly
positive eigenvalues with multiplicity.

For N>=2, put J=floor(log_2(N-1)). Then

    n_+(K_N) <= 1 + 2(J+1) + 2 sum_(j=0)^J 2^(j/2).       (1)

In particular n_+(K_N)=O(sqrt N). The inequality may exceed N
at small N and can of course be replaced by its minimum with N.
For N=1 the elementary bound is n_+<=1.

## Quadratic-form estimate

The elementary inequalities, valid for j>=1, are

    j^2/4 <= a_j^2 <= j^2/4+1/12,
    a_j <= j/2+1/(8j).

The first follows by writing the excess as j^2/[4(4j^2-1)].
For the second, square the positive quantities or use
(1-u)^(-1/2)<=1+u for 0<=u<=1/4. Set c_-2=c_-1=0.
The arithmetic-geometric mean bound on each c shows, also at
k=0,1 by allowing a nonnegative upper bound for the absent c,

    b_k+c_k+c_(k-2) <= 4/3.

Indeed the respective upper bounds are
-k^2/2-k/2+5/12 and k^2/2+k/2+11/12.
Extend a vector u on 0,...,N-1 by zero to all nonnegative indices.
Completing the distance-two squares, and bounding each nearest
neighbor cross term by a_(k+1)(|u_k|^2+|u_(k+1)|^2), gives

    <u,K_N u> <= -sum_(k>=0)c_k |u_(k+2)-u_k|^2
                       +sum_(k=0)^(N-1)(k+3)|u_k|^2.       (2)

For the diagonal bound used here, a_k+a_(k+1)<=k+3/4 holds
for k>=1 from the displayed estimate and for k=0 directly.
Adding 4/3 is less than adding 3. Dropping negative square terms
can only increase the right-hand side.

## Dyadic Neumann comparison

Separate the single index 0 and the consecutive blocks

    B_j={2^j,...,min(2^(j+1)-1,N-1)},  0<=j<=J.

In (2), drop all distance-two squares that do not have both
endpoints in the same block. On a block with left endpoint a=2^j,
the potential k+3 is at most 2a+2<=4a, and every retained edge
has c_k>=(k+1)(k+2)/4>=a^2/4. Each block splits into at most
two parity paths, of lengths m_0,m_1 with m_0+m_1<=a.
Thus its form is bounded above by the direct sum, for nonempty
paths, of

    4a I_m - (a^2/4) L_m,

where L_m is the free-end path Laplacian. Its eigenvalues are
4 sin^2(pi r/(2m)), r=0,...,m-1; the formula includes m=1.
Since sin(pi r/(2m))>=r/m, the r-th comparison eigenvalue is
at most 4a-a^2 r^2/m^2. It can be strictly positive only if
r<2m/sqrt a. Consequently each nonempty path contributes at
most 1+2m/sqrt a positive eigenvalues. The whole block contributes
at most 2+2sqrt a.

Quadratic-form order implies monotonicity of the ordered
eigenvalues, by the finite-dimensional min-max principle.
Summing these bounds and the single index 0 proves (1).
The geometric sum is at most sqrt(2N)/(sqrt2-1), so it has
order sqrt N; the additive logarithm is harmless.

## Relation to the interpolation obstruction

The independently reviewed upper enclosure is
lambda_max(K_N)<=N+3/4. The column nodes satisfy
xi_l>=l(l+1)+3/4. Therefore every factor xi_l I-K_N is
positive definite whenever l(l+1)>N. There are at most
O(sqrt N) nodes failing this sufficient condition.

The new result additionally bounds the dimension of the positive
spectral subspace of K_N itself by O(sqrt N). On its orthogonal
complement every positive-node factor is positive definite.
These are exact spectral separations. Neither a lower bound on
distances from the remaining nodes to eigenvalues nor a lower
bound on a projected multipoint minor follows from them. In
particular restriction of a positive definite polynomial in K_N
to an off-diagonal block need not preserve rank or a singular
value bound. That is the remaining step for the Z_L formulation.
