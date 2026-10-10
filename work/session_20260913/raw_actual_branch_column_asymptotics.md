> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual branch columns, their linear conditioning, and a mixed-node kernel limit

Date: 2026-09-13. Original continuation by audit_sources.
Independent review: `raw_actual_branch_columns_independent_review.md`
passes this theorem. The subsequent reviewed quantitative argument
in `raw_quantitative_fixed_cut_transport.md` supplies the
O(log(N)/N) rates incorporated below.

This note extracts the actual initial constants from the accepted
global corrected transport, with J=1 in odd degree and J=2 in
even degree. The two columns have different powers of x. The
result gives an explicit limiting column matrix and shows that
the condition number of P_N(cN^2) is asymptotic to N times an
explicit positive function, rather than merely polynomially
bounded. It also gives a concrete mixed-node kernel limit.

No relative claim is made for individual entries at possible
complex zeros, and no stability of a growing determinant is
inferred from locally uniform convergence of its kernel.

## 1. The two actual starting matrices

Keep the symmetric row seeds R_0=(1,0), R_1=(sqrt(3)/2,1).
The first two recurrence equations give exactly

    R_2(x)=(sqrt(5)(6x+1)/8, sqrt(15)/4),
    R_3(x)=(sqrt(7)(15x+8)/24, sqrt(21)(5x+8)/36).        (1)

Thus P_1 has rows R_1,R_2 and P_2 has rows R_2,R_3. These
are the prescribed branch matrices, with no change to the
second seed or the actual column order.

For fixed positive integer J, the explicit cocycle inverse has
the expansion, uniformly as x tends to infinity in the right
half-plane with its argument in a fixed compact range,

    F(J,x)^(-1)=
      [[sqrt(2/J)sqrt(x)(1+O_J(1/x)), O_J(x^(-1/2))],
       [-sqrt(J/2)+O_J(1/x), sqrt(J/2)+O_J(1/x)]].        (2)

The first-row off-diagonal cannot be discarded in every
unscaled entry, since R_(J+1) can have a larger polynomial
degree. Applying (2) to the exact matrices (1), with their
full entries, gives the normalized limits

    F(1,x)^(-1)P_1(x)diag(x^(-1),x^(-1/2))
       -> [[0,sqrt(2)],[3sqrt(5)/(4sqrt(2)),0]],

    F(2,x)^(-1)P_2(x)diag(x^(-3/2),x^(-1))
       -> diag(3sqrt(5)/4,5sqrt(21)/36).                 (3)

For example the odd first column is led by the second row,
of size x, while the odd second column is led by the first
row, of size sqrt(x). In even degree the corresponding leading
powers are x^(3/2) and x. The suppressed entries in (3) tend
to zero, rather than being asserted identically zero.

The accepted diagonal product evaluation in
`raw_global_corrected_transport.md` gives

    D_1=diag(4sqrt(3)/(3pi),32sqrt(5)/(15pi)),
    D_2=diag(4sqrt(10)/15,12sqrt(14)/35).                (4)

Multiplying (3) by these actual constants yields

    C_even=diag(sqrt(2),sqrt(6)/3),
    C_odd=[[0,4sqrt(6)/(3pi)],[4sqrt(2)/pi,0]]
          =(4/pi)sigma_1 C_even.                       (5)

The gamma-product normalization is therefore essential to
the odd constant; it cannot be replaced by the identity.

## 2. The explicit column matrix limit

For c in H={Re c>0}, define with the previously fixed branches

    w(c)=1/(sqrt(c+1)+sqrt(c)), eta(c)=1/(2sqrt(c)),
    D(c)=diag(sqrt(w(c)),1/sqrt(w(c))),
    B(c)=(c+1)^(-1/4)D(c)exp(eta(c)sigma_1).             (6)

Here the letter B(c) denotes this 2-by-2 limiting matrix, not
the scalar HP polynomial B_N(z). At x=cN^2 the exact cocycle is
F(N,x)=N^(-1/2)B(c).

Let J=2 for even N and J=1 for odd N, and retain the exact
nonzero scalar product

    Lambda_(N,J)(x)=product_(j=J+2,J+4,...,N)lambda(x/j^2).

Put

    (p_0,p_1)=(3/2,1) for even N,
    (p_0,p_1)=(1,1/2) for odd N,
    D_p(x)=diag(x^(p_0),x^(p_1)).

All powers are defined by the principal logarithm on H. The
global corrected-transport theorem, (3), and (4) prove

    P_N(cN^2)=Lambda_(N,J)(cN^2) N^(-1/2)
                  [B(c)C_parity+O_K(log(N)/N)]D_p(cN^2), (7)

locally uniformly on every compact K contained in H, through
each parity of N. The statement is a limit of the column-scaled
matrix. It does not replace the different column powers by a
single common power.

Every function in the scaled expression is holomorphic on a
fixed neighborhood of K for large N. Local uniform convergence
therefore gives, for r=0,1,2,

    partial_c^r{N^(1/2)Lambda_(N,J)(cN^2)^(-1)
                    P_N(cN^2)D_p(cN^2)^(-1)}
       -> partial_c^r{B(c)C_parity}.                    (8)

The original fixed-cut product argument supplied a qualitative
limit. The subsequent full-complex-disk argument in
`raw_quantitative_fixed_cut_transport.md` sharpens the error
in (7), and in each derivative limit (8), to O_K(log(N)/N).
These are derivatives of the fully normalized matrix; they do
not omit derivatives of an unremoved exponential scalar.

## 3. Exact asymptotic condition numbers

For real c>0 put A_parity(c)=B(c)C_parity and let u_parity(c)
be its first column. This matrix is invertible. Equation (7)
has the form of a common scalar times

    [A_parity(c)+o(1)]diag(sqrt(x),1), x=cN^2,

after factoring out x^(p_1). For any uniformly convergent
invertible 2-by-2 matrix A_N->A and rho tending to infinity,

    sigma_max(A_N diag(rho,1))/rho -> ||A e_0||,
    sigma_min(A_N diag(rho,1)) -> |det A|/||A e_0||.      (9)

The first assertion is direct convergence after division by
rho; the second follows from the exact product of the singular
values. It remains valid despite an error in the first column
being multiplied by rho. Thus (7) gives, uniformly on positive
compact c intervals,

    cond(P_N(cN^2))/N
       =kappa_parity(c)+O_K(log(N)/N),                 (10)

where the explicit positive limits are

    kappa_even(c)=sqrt(3c)
       [w(c)cosh(eta(c))^2+w(c)^(-1)sinh(eta(c))^2],

    kappa_odd(c)=sqrt(3c)
       [w(c)sinh(eta(c))^2+w(c)^(-1)cosh(eta(c))^2].      (11)

Indeed the ratio ||u||^2/|det A| is sqrt(3) times the
bracket in (11); the odd factor 4/pi cancels. In particular
the condition number is asymptotically linear, not bounded.

For completeness the two singular values themselves retain the
exact scalar product and column powers:

    sigma_max(P_N(cN^2))
      ~Lambda_(N,J)(cN^2)N^(-1/2)x^(p_0)||u_parity(c)||,

    sigma_min(P_N(cN^2))
      ~Lambda_(N,J)(cN^2)N^(-1/2)x^(p_1)
                       |det A_parity(c)|/||u_parity(c)||.       (12)

Both asymptotics in (12) have relative error O_K(log(N)/N),
by the quantitative continuation. These norm and determinant
assertions on the positive axis do not assert relative
approximations to entries at complex zeros.

## 4. A mixed-node boundary kernel

Let

    Kcal_N(x,y)=sum_(k=0)^(N-1) R_k(x)^T R_k(y).

For parameters above the row spectrum, the exact matrix Green
identity and M_N P_N=Gamma_N^T P_(N-2) give

    Kcal_N(x,y)=P_N(x)^T
                    [M_N(x)-M_N(y)]/(y-x) P_N(y).       (13)

The diagonal uses -M_N'(x). This is an analytic divided
difference, not a limiting prescription that discards the
diagonal. The local holomorphic resolvent theorem implies,
uniformly for c,d in compact subsets of H,

    [M_N(cN^2)-M_N(dN^2)]/[N^2(d-c)]
       =k(c,d)I+O_K(1/N),                              (14)

where

    k(c,d)=[m(c)-m(d)]/[16(d-c)]
           =q(c)q(d)/[1-q(c)q(d)].                     (15)

Formula (15) also holds at c=d by continuation. To justify
uniformity near the diagonal in (14), use the derivative bound
on the holomorphic O(1/N) remainder on the convex hull of a
slightly enlarged compact set. No division by a small d-c is
performed without this bound.

Set s_N(x)=Lambda_(N,J)(x)N^(-1/2). Combining (7) and (14)
now gives the explicit matrix kernel limit

    D_p(x)^(-1) Kcal_N(x,y)D_p(y)^(-1)
                      /[s_N(x)s_N(y)]
       -> k(c,d) A_parity(c)^T A_parity(d),
    x=cN^2, y=dN^2.                                   (16)

The absolute matrix error in (16) is O_K(log(N)/N), locally
uniformly and under any fixed number of parameter derivatives,
including the first two. It keeps the
actual columns and transpose convention. On nonreal parameters
no conjugation is inserted into this holomorphic kernel.

## 5. The prescribed high interval has the same leading kernel

For the actual interval n+1,...,2n-1, define

    Kcal_hi,n(x,y)=Kcal_(2n)(x,y)-Kcal_(n+1)(x,y).

Take x=cn^2 and y=dn^2, with c,d in compact subsets of H.
The cut 2n is even, so its normalization in (16) always uses
C_even, D_p(x)=diag(x^(3/2),x), and parameters c/4,d/4.
The lower cut is exponentially smaller in this normalization.

Here is an explicit justification, including the parity of the
lower cut. The logarithm of lambda is ell(z)=2asinh(sqrt(z)).
For either fixed starting cut J=1 or 2 and a cut L of order n,
the right-endpoint sum with mesh 2/n gives

    log Lambda_(L,J)(cn^2)
       =n integral_0^(L/n) asinh(sqrt(c)/t) dt
                       +O_K(log n).                   (17)

Near t=0 the integrand is log(2sqrt(c)/t)+O_K(t^2).
Stirling's formula controls the Riemann sum of -log t with
O(log n) error, while the remaining function has a bounded
derivative at zero. This proves (17) uniformly and with the
chosen holomorphic logarithm, for either parity lattice.

Subtracting the cuts 2n and n+1 yields

    log Lambda_(2n,2)(cn^2)
       -log Lambda_(n+1,J)(cn^2)
       =n G(c)+O_K(log n),
    G(c)=integral_1^2 asinh(sqrt(c)/t) dt.               (18)

The real part of G is positive throughout H: the real part
of asinh(sqrt(z)) is (1/2)log|lambda(z)|>0 because |q(z)|<1.
It therefore has a positive minimum on each compact K.
The finite column powers and N^(-1/2) factors in (7) are
only polynomial. Equations (7), (14), and (18) show that the
normalized lower-cut contribution is O_K(exp(-delta_K n))
for some positive delta_K. This comparison is between matrices
in their stated locations, not between possibly vanishing
individual entries.

Consequently the explicit prescribed high-kernel limit is

    D_even(x)^(-1) Kcal_hi,n(x,y) D_even(y)^(-1)
                       /[s_(2n)(x)s_(2n)(y)]
       -> k(c/4,d/4) A_even(c/4)^T A_even(d/4),
    x=cn^2, y=dn^2.                                   (19)

The convergence is locally uniform and holomorphic with first
and second derivatives. The lower-cut error is exponentially
small; the subsequent quantitative fixed-cut theorem makes the
total absolute matrix error in (19) O_K(log(n)/n), including
every fixed number of parameter derivatives.

## 6. Explicit scalar features and the remaining determinant problem

For real c>0 write q=q(c), eta=eta(c). The two columns of
A_even(c) are

    a_0(c)=sqrt(2)(c+1)^(-1/4)
                   (q^(1/4)cosh eta, q^(-1/4)sinh eta)^T,

    a_1(c)=(sqrt(6)/3)(c+1)^(-1/4)
                   (q^(1/4)sinh eta, q^(-1/4)cosh eta)^T.       (20)

Thus after the explicit amplitude and column-power factors,
an actual parity-selected mixed-node entry has limiting kernel

    k(c,d) a_sigma(c)^T a_tau(d).                     (21)

The original high Gram uses c=xi_l/(2n)^2 in this formula
and retains its actual factors g_l g_j as well. Those factors
are not replaced by asymptotic amplitudes.

The scalar factor has the positive feature expansion

    k(c,d)=sum_(r>=1)q(c)^r q(d)^r.

For any fixed finite set of distinct positive parameters and
arbitrary selected parities, the matrix of (21) is strictly
positive definite. Indeed q(c) is strictly decreasing on the
positive axis, the scalar Cauchy kernel is positive definite
on distinct q values, and even just the first components in
(20), which are all nonzero there, give a positive definite
congruence of that scalar kernel. The second components add
a positive semidefinite matrix.

This fixed-size fact is not uniform stability of a growing
determinant. Its smallest eigenvalue can become very small as
the number of nodes increases or their separation decreases.
The O_K(log(n)/n) absolute matrix error in (19) is not
automatically smaller than that eigenvalue. A comparison
requires an explicit eigenvalue bound and the number of
selected nodes. Moreover nodes with
xi_l/n^2 tending to zero lie outside the current compact-domain
asymptotics. Neither these low nodes nor the prescribed
amplitude-weighted cardinal normalization may be dropped.

The new concrete target is therefore a stability estimate for
the explicit Cauchy-type, two-component kernel (21), at the
actual moving nodes, together with control of the excluded
small-parameter regime. No mixed determinant lower bound or
irrationality conclusion is claimed here.

Only the explicitly requested starting cuts 1 and 2 were
evaluated from the recurrence; no new degree or root scan was
performed.
