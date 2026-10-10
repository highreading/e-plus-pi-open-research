> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform weak coupling of the two boundary parity channels

Date: 2026-09-13. Root continuation of the reviewed matrix
Christoffel-Darboux estimates. Independent review pending.

The full two-channel boundary resolvent is nearly diagonal at a
parameter of order N^2. This is a quantitative statement about
the boundary matrix, not a claim that the entire branch evaluation
matrix is nearly diagonal.

Use K_N, J_N, Gamma_N and M_N from the matrix CD note, N>=8.
Let Pi=diag(1,-1,1,-1,...) on the N interior coordinates.
The exact decomposition is

    K_N=K0_N-J_N,
    Pi K0_N Pi=K0_N, Pi J_N Pi=-J_N,

where K0_N is the principal compression of J^2-Lambda. In
particular Pi K_N Pi=K0_N+J_N. Both matrices have the same
spectrum, and ||J_N||<=N by the already reviewed row bound.

Fix 0<c<=C and c N^2<=x<=C N^2, with N>=max(8,4/c).
Put R=(xI-K_N)^(-1) and Rtilde=Pi R Pi. The spectral bounds give

    ||R||=||Rtilde||<=2/(c N^2),
    R-Rtilde=-2 R J_N Rtilde.

Consequently the parity off-block parts obey

    ||(R-Pi R Pi)/2||<=4/(c^2 N^3),                (1)
    ||(R^2-Pi R^2 Pi)/2||<=16/(c^3 N^5).          (2)

For (2), use R^2-Rtilde^2=(R-Rtilde)R+Rtilde(R-Rtilde)
and the preceding bounds. No commutation between R and Rtilde
is needed. These estimates also bound the single off-diagonal
entry of their compressions to the last two coordinates, since
these coordinates have opposite parity.

Write Gamma_N=[[d1,0],[ell,d2]]. The elementary bounds used
in the CD proof imply

    0<d1,d2<=N^2/2, |ell|<=N.

Since M_N=Gamma_N^T (iota^T R iota) Gamma_N, its off-diagonal
entry is d1*d2*R_(N-2,N-1)+ell*d2*R_(N-1,N-1). Thus

    |(M_N)12| <= (1/c^2+1/c)N.                   (3)

The same computation with R^2, using ||R^2||<=4/(c^2N^4),
gives

    |(-M_N')12| <=(4/c^3+2/c^2)/N.              (4)

The independently reviewed diagonal lower bounds are

    M_N >= N^2/[64(C+1)] I,
    -M_N' >=1/[64(C+1)^2] I.

Combining them with (3)-(4) proves the explicit relative bounds

    |M12|/sqrt(M11 M22)
      <=64(C+1)(c^(-2)+c^(-1))/N,                (5)

    |(-M')12|/sqrt((-M')11 (-M')22)
      <=64(C+1)^2(4c^(-3)+2c^(-2))/N.           (6)

Hence the boundary quadratic forms, after scaling each coordinate
by its actual diagonal entry, approach the identity in operator
norm at rate O(1/N), uniformly on the whole interval x~N^2.
The statement remains valid if the two final coordinate parities
are reversed; Pi only labels the two invariant blocks.

This identifies a small coupling parameter in the positive matrix
object. It does not give a small coupling for P_N itself: the CD
form is conjugated by P_N, and that matrix may be poorly
conditioned. Nor does an O(1/N) bound at each cut by itself bound
a product through N cuts. A useful next step would keep the exact
two-step relation M_N P_N=Gamma_N^T P_(N-2) and analyze its
accumulated off-diagonal transport, with a justified normalization.
No scalar cofactor lower bound or irrationality consequence is
asserted here.
