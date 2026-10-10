> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independence and conditioning of the actual low-plus-sparse-bulk union

Date: 2026-09-13. Original continuation by audit_sources.
Independent review passed: `raw_low_bulk_union_independent_review.md`.
The bulk localization step was also checked directly by
audit_computations during derivation.

This note combines the reviewed growing-low-node and actual sparse
bulk theorems. It proves independence of their union, rather than
inferring it from the two separate rank statements. The new input
is a geometric bound for the bulk columns below a cut. A Schur
complement then compares that bound with the actual inverse of the
selected low-node block.

Every row is in n+1,...,2n-1. The actual spectral amplitudes and
all column normalizations are kept explicitly. No asymptotic for
fixed nodes is extended to bulk parameters.

## 1. Actual columns, nodes, and scales

Take

    m=floor((log n)^(1/3))

low nodes ell=0,...,m-1. Independently fix the constants
0<alpha<beta<=1 and 0<kappa<1/C_s from
`raw_actual_sparse_bulk_matrix_theorem.md`. Put

    b=floor(kappa log n), theta=C_s kappa<1,

and retain exactly that theorem's b well-spaced actual bulk
indices l_1,...,l_b in [ceil(alpha n),floor(beta n)]. They
are disjoint from the low indices for sufficiently large n.

For every selected node define the actual physical column

    H_(k,ell)=g_ell p_k^(ell mod 2)(xi_ell)=<E_k,psi_ell>,
    n+1<=k<=2n-1.                                    (1)

Let L_k=integral_0^1 E_k(x)dx>0. Normalize the low columns by
the exact nonzero scalars

    d_ell^low=psi_ell(1)L_(2n), ell<m,                 (2)

and normalize the bulk columns by the exact accepted scalars

    d_i^bulk=g_(l_i) s_(2n)(xi_(l_i)) xi_(l_i)^(p_sigma_i),
    p_0=3/2, p_1=1, sigma_i=l_i mod 2.                (3)

Here s_(2n)=Lambda_(2n,2)/sqrt(2n) is the exact scalar product
from the sparse-bulk theorem. No g_ell has been replaced by its
asymptotic. The low scales in (2) may be treated as signed;
only their nonvanishing is needed. Their signs are harmless
orthogonal column signs for any singular-value statement.

Write the normalized union as

    U=[V,B]=H_union diag(d^low,d^bulk)^(-1).            (4)

Then

    V_(k,ell)=[L_k/L_(2n)] M_(k,ell),
    M_(k,ell)=<E_k,psi_ell>/[L_k psi_ell(1)].           (5)

The matrix B is exactly the normalized bulk feature matrix in
the accepted theorem. Its bounds are, with fixed positive
constants depending only on alpha,beta,kappa,

    sigma_min(B)>=c_B n^(-theta/2), ||B||<=C_B sqrt(b). (6)

The result proved below is that U has full column rank m+b
eventually and

    sigma_min(U)>=exp(-C sqrt(n)),
    cond(U)<=exp(C sqrt(n)).                           (7)

A more informative bound retaining the separate factors appears
in Section 5. Returning to H_union incurs its exact diagonal
scales; those losses are not included in the constant C of (7).

## 2. Geometric localization of the normalized bulk columns

Set

    rho=sqrt(q(alpha^2/4))<1, gamma=-log(rho)>0.

For any high row k choose the largest even N<=k. Thus row k
is one of the two rows of P_N, and n<=N<=2n-2. At every
selected bulk node x=xi_(l_i),

    x/N^2 in [alpha^2/4,(beta+1)^2].

The reviewed even-cut column theorem is uniformly bounded on
this fixed positive compact interval. Therefore the norm of
P_N(x) after division by s_N(x) and its respective column
powers x^(3/2),x is bounded by a fixed constant, uniformly in
n,N,i. Both the lower and upper cuts are even, so the same
column powers cancel exactly. The scalar ratio is

    s_N(x)/s_(2n)(x)
       =sqrt(2n/N) product_(j=N+2,step 2)^(2n) lambda(x/j^2)^(-1)
       <=sqrt(2) q(alpha^2/4)^((2n-N)/2).

It follows that the actual normalized entries satisfy

    |B_(k,i)|<=C rho^(2n-k), n+1<=k<=2n-1.             (8)

There is no comparison between the two different fixed initial
parity cuts here: using even N for every row avoids that issue.
The physical amplitude cancels only against the exact same
amplitude in (3).

For any cut K between n and 2n-1, summing the squared geometric
tail gives the operator-norm estimate

    ||B_[n+1,...,K]||
       <=C sqrt(b) rho^(2n-K).                        (9)

This is a whole prefix bound, including its interaction with
arbitrary bulk-column coefficients. It is stronger than an
entrywise comparison without normalization.

## 3. The chosen low rows leave a long top interval

Use precisely the interior grid from the growing-low theorem:

    t_j=1+j/(m+1), k_j=floor(nt_j), j=1,...,m,
    R={k_1,...,k_m},
    K=k_m=2n-ceil(n/(m+1)), d=2n-K=ceil(n/(m+1)),
    T={K+1,...,2n-1}.                                 (10)

The sets R and T are disjoint, lie in the actual high interval,
and |T|=d-1>b for sufficiently large n.

The growing-low theorem gives for A=(M_(k_j,ell))

    sigma_min(A)
       >=exp(-C m^2 log(m+1)) n^(-(m-1)/2).            (11)

Its relative determinant error tends to zero in the stated m
regime, so this is an actual lower bound. The positive row-mass
estimate, uniform for n<=k<=2n, is

    L_k=[exp(2sqrt(k))/(2pi k^(3/4))](1+O(n^(-1/2))).

Consequently, with a=2(sqrt(2)-1),

    c exp(-a sqrt(n)) <= L_k/L_(2n) <= C.              (12)

Let A_0=V_R. Equations (5), (11), and (12) show

    sigma_min(A_0)>=a_n,
    a_n=c exp[-a sqrt(n)-C m^2 log(m+1)] n^(-(m-1)/2). (13)

This loss is retained; the low block is not assumed uniformly
well conditioned. The all-order endpoint bound in the growing-low
proof also gives |M_(k,ell)|<=2E_m with E_m=exp(4m+8), for
every high row and ell<m. Thus there is a bound M_n>=1 with

    ||V||<=M_n,  M_n=C E_m sqrt(nm).                  (14)

In particular the top low block C=V_T satisfies ||C||<=M_n.

For E=B_R, (9) gives

    ||E||<=t_n, t_n=C sqrt(b) exp(-gamma d).            (15)

By (9), the same t_n bounds the entire prefix through K, not only
the selected rows R. The full bulk Gram therefore loses at most
t_n^2 in norm when the prefix
through K is removed. Since t_n is exponentially smaller than
the polynomial lower bound in (6), the top bulk block B_T has

    sigma_min(B_T)>=b_n,
    b_n=(c_B/2)n^(-theta/2)                            (16)

for all sufficiently large n.

## 4. The mixed Schur complement is stable

Restrict the actual normalized union to rows R followed by T:

    U_[R,T]=[[A_0,E],[C,B_T]].

The Schur correction obeys

    ||C A_0^(-1) E||/b_n
       <=eta_n:=M_n t_n/(a_n b_n).                    (17)

All terms on the right have been bounded in the same matrix
normalization. Their logarithms give

    log eta_n <=-gamma n/(m+1)+a sqrt(n)
           +[(m-1)/2]log n+C m^2 log(m+1)+4m+O(log n).

For m=floor((log n)^(1/3)), every positive term is
o(n/(m+1)). Hence, eventually,

    eta_n<=exp[-gamma n/(2(m+1))] ->0.                 (18)

The remaining top block

    S=B_T-C A_0^(-1)E

therefore has sigma_min(S)>=b_n/2. If U_[R,T](u,v)^T=0,
its first block equation gives u=-A_0^(-1)Ev, and its second
then gives Sv=0. Thus v=0 and u=0. This proves full rank of
the mixed restriction and hence of U and H_union.

The proof does not compare fixed-node and bulk formulas at
the same moving spectral parameter. It compares a controlled
inverse of one actual finite block with a controlled geometric
tail of the other family on disjoint row regions.

## 5. Quantitative conditioning in the exact column normalization

For sufficiently large n take a_n,b_n<=1 and M_n>=1. Also
t_n/a_n<=1 by (17)-(18). For any vector (u,v), let
z=U_[R,T](u,v)^T and write its two row blocks as z_1,z_2.
The two exact equations imply

    ||v|| <= (2/b_n)(1+M_n/a_n)||z||,
    ||u|| <= a_n^(-1)||z||+(t_n/a_n)||v||.

Adding these estimates yields

    ||(u,v)|| <= [9M_n/(a_n b_n)] ||z||.

Therefore

    sigma_min(U)>=a_n b_n/(9M_n),
    ||U||<=M_n+C_B sqrt(b).                            (19)

Equations (13)-(14) and (16) imply (7), since
m log n, m^2 log(m+1), and log n are all o(sqrt(n)) in
the stated regime. The more precise bound (19) is retained
rather than absorbing these factors into an unqualified
polynomial condition number.

For the original physical matrix, put
d_min=min{|d_ell^low|,d_i^bulk} and similarly d_max. Then

    sigma_min(H_union)>=d_min a_n b_n/(9M_n),
    cond(H_union)<=cond(U) d_max/d_min.                (20)

These are exact scaling inequalities. The possibly large
factorial-scale ratio d_max/d_min is not silently omitted.

## 6. An actual square mixed minor and a relative factorization

There is also a square-minor formulation. Choose a b-element
subset J of T maximizing |det B_J|, with a fixed lexicographic
tie rule. Since B_T has least singular value at least b_n,
finite Cauchy-Binet gives

    |det B_J|>=b_n^b / sqrt(binomial(|T|,b))
              >=b_n^b n^(-b/2).                      (21)

This defines an actual finite row selection using only the bulk
matrix, and proves it is nonzero. No new numerical row search is
required for the existence theorem. Since ||B_J||<=C_B sqrt(b),

    sigma_min(B_J)>=
       b_n^b n^(-b/2)/(C_B sqrt(b))^(b-1)
       >=exp(-C(log n)^2)=:b'_n.                      (22)

Use the actual low block C_J=V_J in the square mixed minor.
The analogous correction satisfies

    ||B_J^(-1)C_J A_0^(-1)E||
       <=M_n t_n/(a_n b'_n)
       <=exp[-gamma n/(2(m+1))]=:eta'_n               (23)

eventually, because the additional O((log n)^2) in the
logarithm is still o(n/(m+1)). The exact determinant identity is

    det U_[R,J]
       =det A_0 det B_J
          det(I-B_J^(-1)C_J A_0^(-1)E).                (24)

The last determinant is positive for eta'_n<1: the real path
I-tB_J^(-1)C_J A_0^(-1)E is nonsingular for 0<=t<=1.
Its logarithm has absolute value at most 2b eta'_n when
eta'_n<=1/2. Thus (24) is a relative factorization with a
vanishing, explicitly bounded error, not merely an entrywise
approximation of a possibly small determinant.

For completeness, the known low determinant factor is exactly

    det A_0=[product_(j=1)^m L_(k_j)/L_(2n)]
       L_m n^(-q/2)(1+R_(n,m)),

    |R_(n,m)|<=n^(-1/2) exp(Cm^2 log(m+1)),

with L_m and q from the growing-low theorem. The other factor
det B_J remains the actual selected normalized bulk determinant,
bounded below by (21), rather than being replaced by a
one-point determinant or by an unproved local approximation.
Multiplying (24) by the exact column factors (2)-(3) restores
the corresponding physical mixed minor. In particular the low
row and column factors combine to
product_j L_(k_j) times product_(ell<m) psi_ell(1); the
bulk factors still include their actual g_(l_i).

## 7. Scope and what remains unresolved

The selected m+b columns of the actual high matrix are jointly
independent, and (19) bounds their conditioning after the
specified exact column scalings. This closes the interaction
question for these two particular growing families. Their
individual rank theorems alone would not have proved it;
the geometric localization and Schur estimate (17) are the
additional argument.

The low count remains in the proved endpoint range and the bulk
count retains the sparse theorem's restriction kappa<1/C_s.
The intermediate nodes between these ranges, a full-density
bulk, and the actual full high-row inverse are not covered.
The result does not establish the final amplitude-weighted
cardinal angle, shrinking of the primitive remainder, or
the rationality of e+pi.

No degree, node, prime, or root scan was performed.
