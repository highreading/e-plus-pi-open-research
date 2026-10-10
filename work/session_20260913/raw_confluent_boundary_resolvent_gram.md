> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A quantitative confluent boundary-resolvent Gram at the artificial dyadic nodes

Date: 2026-09-13. Original root derivation.
Independent audit: raw_confluent_boundary_gram_independent_review.md
passes the full proof without correction.

This is an actual row-matrix result at the repeated rational-denominator
nodes. It supplies a lower singular-value bound for the full two-component
boundary resolvent family, including repetitions. It does not identify
that family with the remaining exceptional Schur block. That additional
identification must be proved before transferring this bound to the
endpoint problem.

## 1. Exact matrices, nodes and normalizations

Let N=2n, J_N=K_N/N^2, and let V_0 inject into the final two
coordinates, in the usual order. Use the dyadic denominator nodes

    x_j=2n+3/4+3n 2^j,
    0<=j<J,   J=1+floor(log_2(n/2)),
    a_j=x_j/N^2,
    nu=ceil(4sqrt(6n)/log 3),   D=nu J.                 (1)

All assertions are for sufficiently large n. Directly from (1),

    0<a_j<1,
    |a_j-a_k|>=1/N for j!=k,
    a_j-lambda_max(J_N)>=1/N,
    ||J_N||<=2,
    D<=N/4.                                         (2)

For the gap to the row spectrum, its upper bound is
(N+3/4)/N^2 and x_0=5n+3/4=(5/2)N+3/4. Thus the gap is
at least (3/2)/N. Consecutive node gaps are at least (3/2)/N.
The rougher constants in (2) simplify the proof.

Form the N-by-2D block matrix

    W=[(a_j I-J_N)^(-r-1)V_0]_(j=0,...,J-1; r=0,...,nu-1).
                                                               (3)

There are absolute constants C,c>0 such that

    exp(-C D log N)<=sigma_min(W)<=||W||
                            <=exp(C D log N).         (4)

In particular W has full column rank. The constants are independent
of n, the number of nodes, and their multiplicity under (1).

## 2. Boundary block Krylov coordinates have an exponential inverse bound

Group the final coordinates into pairs and let V_r inject into the
r-th pair from the boundary, r=0,...,D-1. The actual band-two matrix
J_N is block tridiagonal in this ordering. Its diagonal blocks and
off-diagonal blocks have uniformly bounded norm. Every off-diagonal
block joining these last D pairs is invertible with uniformly bounded
inverse, because their indices are at least N-2D>=N/2.

For an explicit check, the connecting block, up to transpose and the
fixed order, has two diagonal entries a_(k+1)a_(k+2)/N^2 and
a_(k+2)a_(k+3)/N^2, and one off-diagonal entry -a_(k+2)/N^2.
The reviewed a_l>=l/2 and a_l<=l/2+1/(8l) give diagonal
entries bounded below by an absolute positive constant and all entries
bounded above. Their triangular inverses are therefore bounded by an
absolute constant. The distinct use of a_l here as a recurrence
coefficient, versus node a_j in (1), is only notational; no node enters
this block estimate.

The exact block recurrence can be solved for V_(r+1):

    V_(r+1)=[J_N V_r-V_r A_r-V_(r-1)B_r] C_(r+1)^(-1),
                                                               (5)

where the displayed coefficient blocks and inverses are uniformly
bounded and the r=-1 term is absent. The precise block orientation is
fixed by J_N V_r; equation (5) is just its coefficient identity. No
infinite-operator approximation is used.

By induction there are 2-by-2 coefficients T_(s,r) such that

    V_r=sum_(s=0)^r J_N^s V_0 T_(s,r),
    sum_s ||T_(s,r)||<=C_0^(r+1),                     (6)

with one absolute C_0>1. The estimate follows from the two-term
coefficient-norm recursion implied by (5), increasing C_0 if needed.

Let Y=[V_0,J_N V_0,...,J_N^(D-1)V_0]. The matrix identity (6)
says Y T=[V_0,...,V_(D-1)], with

    ||T||<=D C_0^(D+1).

The right side is an isometry onto the last 2D coordinates. Both Y
and that isometry are supported on those coordinates. Thus the square
tail compression of Y is invertible and T is its inverse. Therefore

    sigma_min(Y)>=[D C_0^(D+1)]^(-1),
    ||Y||<=sqrt(D) 2^(D-1).                           (7)

The recurrence uses r<=D-2, so its farthest connecting block still
lies among the pairs in (2).

## 3. A quantitative partial-fraction polynomial basis

Put

    q(t)=product_j(a_j-t)^nu,
    p_(j,r)(t)=q(t)/(a_j-t)^(r+1).                    (8)

These D polynomials have degree below D and form a basis of that
polynomial space: dividing a relation by q and taking its principal
parts at each distinct a_j proves independence. Let C_q be their
coefficient matrix in 1,t,...,t^(D-1), with ordering as in (3).

The following rough bound retains the growing multiplicity:

    ||C_q^(-1)||<=D(8N)^D.                           (9)

To prove it, take p with coefficient Euclidean norm one. For fixed j
let q_j(t)=q(t)/(a_j-t)^nu. On the disk |t-a_j|=1/(4N), all
other factors have modulus at least 3/(4N), by (2). Also |t|<=2,
so |p(t)|<=sqrt(D) 2^(D-1). It follows that

    |p(t)/q_j(t)|<=sqrt(D)2^(D-1)(4N/3)^(D-nu).

The principal-part coefficient for (a_j-t)^(-r-1) is, up to a
sign, the Taylor coefficient of order nu-r-1 in p/q_j at a_j.
Cauchy's bound on the displayed disk multiplies by at most
(4N)^(nu-1). Thus every such coefficient has magnitude at most
sqrt(D)(8N)^D. Taking the Euclidean norm of the D coefficients
proves (9). It also proves invertibility constructively, with no
assumption about a generic confluent Vandermonde.

Since spec J_N is contained in [-2,2] and all a_j lie in (0,1),

    ||q(J_N)||<=3^D.                                 (10)

Moreover q(J_N) is positive definite by (2). Its inverse exists.

## 4. Exact factorization and the lower bound

Functional calculus gives the exact identity

    W=q(J_N)^(-1) Y (C_q tensor I_2),                (11)

up to the fixed common ordering of the blocks. All multipliers have
been retained. Equations (7), (9), and (10) imply

    sigma_min(W)>=3^(-D) [D C_0^(D+1)]^(-1)
                             [D(8N)^D]^(-1).

This is the lower inequality in (4). The upper inequality follows
directly from (2): every block in (3) has norm at most N^(r+1),
so ||W||<=sqrt(D)N^nu. These estimates prove (4).

In particular the Gram W^T W is positive definite with its smallest
eigenvalue at least exp(-C D log N). Constants may be enlarged when
squaring. With D=O(sqrt(N)log(N)), the exponent is o(N).

## 5. Local Taylor scaling and actual boundary factors

Let h_j=sqrt(x_j)log(N)/2 and t_j=h_j/N^2. For sufficiently
large N, (1) gives

    N^(-2)<=t_j<=1.

Multiplying the r-th block at node j by t_j^r and a sign (-1)^r
therefore changes the least singular value by at worst
N^(-2(nu-1)); its upper bound is not increased. The analogue of (4)
still holds in these locally scaled jet coordinates. In unscaled x,
these blocks are exactly

    N^2 h_j^r [ (1/r!) d^r/dx^r (xI-K_N)^(-1) ]_(x=x_j) V_0.
                                                               (12)

Thus this is a confluent resolvent-jet statement at the same radii
used in the independently developed holomorphic branch estimates.
The factor N^2 in (12) is essential.

If the actual Weyl boundary generator V_0 Gamma_N/N^2 is used,
its 2-by-2 factor and inverse are uniformly bounded for large N.
Right multiplication of every jet block by it preserves the scale
of (4). If Gamma_N is used without division by N^2, that explicit
common N^2 factor must instead be retained.

## 6. Precise remaining bridge

This proves a quantitative lower bound for an actual positive Gram
of both boundary components at every artificial node and all their
repeated derivatives. The construction does not use the error between
an asymptotic kernel and the actual Gram; hence no tiny determinant
is inferred from insufficient entrywise accuracy.

The remaining exceptional matrix was obtained by removing particular
good directions from Z_L, with physical metric involving S. Identifying
its D rational-denominator directions with a controlled compression of
(3), and preserving the original two channel restrictions and low
factors, is additional work. A general compression of a well-conditioned
rectangular matrix need not preserve its least singular value. The
O(sqrt(n)) low-factor directions also remain. Therefore (4) is not yet
a lower bound for the exceptional T_n or its endpoint kernel.
