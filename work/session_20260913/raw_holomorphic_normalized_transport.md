> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Holomorphic normalized transport and uniform parameter derivatives

Date: 2026-09-13. Original continuation by audit_sources.
Independent review requested.

This extends the actual local resolvent and two-step transport
estimates to compact subsets of the right half-plane. After
removing the known scalar product, the transport matrix and its
inverse have uniformly bounded first and second derivatives in
the normalized parameter chi, where x=chi n^2. The proof uses
complex resolvents and the exact geometric vector; no complex
bound is inferred merely from an estimate on the positive axis.

The underlying finite matrices, branch normalization, and exact
identity M_j P_j=Gamma_j^T P_(j-2) are those of
`raw_local_boundary_resolvent_limit.md`. All branch matrices below
are in the symmetric row normalization. They are not themselves
asserted to be symmetric.

## 1. Domain and scalar branches

Let H={c in C: Re c>0}. On H use the principal square roots of
c and c+1, and define

    q(c)=(sqrt(c+1)-sqrt(c))^2,
    m(c)=4q(c),
    lambda(c)=1/q(c)=(sqrt(c+1)+sqrt(c))^2.

These functions are holomorphic and nonzero on H. In particular
the product of the sum and difference of the two square roots
is one. Moreover

    |q(c)|<1, c in H.                                      (1)

To prove (1), note that q+q^(-1)=4c+2. If |q|=1, the left
side is real and belongs to [-2,2], forcing Re c<=0. The
connected domain H contains the positive axis, where |q|<1,
so continuity and the absence of a unit-circle crossing prove
the assertion throughout H.

The sum sqrt(c+1)+sqrt(c) has argument strictly between
-pi/4 and pi/4. Define the holomorphic logarithm

    ell(c)=2 Log(sqrt(c+1)+sqrt(c))=2 asinh(sqrt(c)),         (2)

where Log is principal and the asinh expression uses the same
branches. Then exp(ell)=lambda and ell is real on the positive
axis. This fixes the scalar product logarithm without winding
or sign ambiguity.

## 2. The geometric vector on a complex compact set

Let L be the self-adjoint half-line Jacobi matrix with diagonal
-1/2 and off-diagonal 1/4. Its spectrum lies in [-1,0]. The
same exact recurrence and first-row calculation as on the real
axis prove

    (cI-L)^(-1)e_0 = w(c),
    w_j(c)=m(c)q(c)^j, c in H.                            (3)

Indeed (1) makes this vector square summable, and c lies in
the resolvent set, giving uniqueness. This assertion does not
identify a complex bilinear square with a Hilbert norm.

Fix a compact E contained in H. Put

    a=min_(c in E) Re c>0,
    q_* = max_(c in E)|q(c)|<1,
    m_* = max_(c in E)|m(c)|,
    F_E=m_* sqrt((1+q_*^2)/(1-q_*^2)^3).

Then

    ||((j+1)w_j(c))_(j>=0)|| <= F_E, c in E.              (4)

This follows by summing the absolute squares of the geometric
series; it is valid for complex q.

Reverse either parity block of K_(0,N)/N^2 from its boundary and
extend by a zero tail, obtaining the self-adjoint A_N from the
reviewed real argument. Its coefficient estimates are algebraic
and unchanged:

    |(A_N-L)_(j,j)| <= 4(j+1)/N,
    |(A_N-L)_(j,j+1)| <= 2(j+1)/N.                       (5)

Consequently ||(A_N-L)w(c)||<=8F_E/N, including the finite
boundary and the entire zero tail. Since sup spec A_N<=9/(8N^2),
all sufficiently large N satisfy

    ||(cI-A_N)^(-1)|| <= 2/a, c in E.

This is the complex self-adjoint resolvent distance estimate:
Re c is separated from every real eigenvalue on its right.
The resolvent identity gives the uniform vector bound

    ||(cI-A_N)^(-1)e_0-(cI-L)^(-1)e_0||
         <=16F_E/(aN).                                (6)

The two finite parity blocks can differ in dimension by one;
the common estimates (5) already include that distinction.

## 3. Restoring the actual matrix and inverting its boundary form

Let R_N(c)=(cI-K_N/N^2)^(-1). The actual perturbation from
K_(0,N)/N^2 has norm at most 1/N. Both complex resolvents have
norm at most 2/a for all sufficiently large N, using the
reviewed upper spectral bounds. Thus their difference has norm
at most 4/(a^2 N). Combining with (6) on the two parity blocks
gives

    ||iota_N^T R_N(c) iota_N-m(c)I_2|| <= D_E/N,
    D_E=4/a^2+16F_E/a.                                 (7)

All transposes here involve the real coordinate embeddings and
real coupling matrix. They are exactly the analytic matrices
appearing in the actual recurrence.

Write G_N=Gamma_N/N^2. The existing elementary coefficient
bounds give ||G_N-I/4||<=1/N and ||G_N||<=1/2. Therefore

    A_N^bd(c):=M_N(cN^2)/N^2
       =G_N^T(iota_N^T R_N(c)iota_N)G_N
       =(m(c)/16)I_2+Z_N(c),
    ||Z_N(c)|| <= E_E/N,                               (8)

where E_E=D_E/4+3/(4a) is sufficient. Here |m(c)|<=1/a
follows from (3) and the half-line resolvent bound. The notation
A_N^bd is distinct from the reversed parity matrix A_N above.

Let mu_E=min_(c in E)|m(c)|>0. For N>=32 E_E/mu_E,
(8) proves that A_N^bd is invertible and

    ||(A_N^bd)^(-1)|| <=32/mu_E.                        (9)

This is a complex matrix inversion estimate; a real positive
quadratic-form lower bound has not been substituted for it.
Alternatively, when Re(cN^2)>sup spec K_N, the Hermitian real
part of the actual resolvent is positive, so the full boundary
form is strictly accretive and invertible as well.

The exact two-step transfer is

    T_N(cN^2)=(A_N^bd(c))^(-1)G_N^T.

Subtract lambda(c)I and use lambda(c)m(c)/16=1/4 in (8).
On E this gives

    T_N(cN^2)=lambda(c)(I+F_N(c)),
    ||F_N(c)|| <= C_E/N,                              (10)

with, for example,

    C_E = 32(1+lambda_* E_E)/(mu_E lambda_min),
    lambda_*=max_E|lambda|,
    lambda_min=min_E|lambda|>0.

Every function in (10) is holomorphic wherever the indicated
finite resolvents and matrices are invertible. On an open
neighborhood of a fixed compact E, these conditions hold for
all sufficiently large N. Thus (10) is a genuinely locally
uniform holomorphic estimate.

## 4. Products on a dyadic cut interval

Let K be any compact subset of H. Choose delta>0 such that

    K^+={chi: dist(chi,K)<=2delta}

is still contained in H, and form the compact set

    E={r chi: chi in K^+, 1/4<=r<=1}.

It is contained in H. Take integers n<=m<=2n of the same
parity. For j=n+2,n+4,...,m and x=chi n^2, the local parameter
c_j=x/j^2 belongs to E for every chi in K^+. Applying (10)
at all these cuts is therefore uniform. Define

    Lambda_(m,n)(chi)=product_j lambda(chi n^2/j^2),
    V_(m,n)(chi)=ordered product_(j increasing to the left)
                    [T_j(chi n^2)/lambda(chi n^2/j^2)].

The empty products at m=n equal 1 and I. The exact recurrence
gives

    P_m(chi n^2)
       =Lambda_(m,n)(chi)V_(m,n)(chi)P_n(chi n^2).         (11)

For n large enough that C_E/n<=1/2, every factor is I plus
an error of norm at most C_E/j. The ordered product need not
commute, but submultiplicativity and the step-two sum imply

    ||V_(m,n)|| <= exp(C_E sum_j 1/j)<=2^(C_E/2),
    ||V_(m,n)^(-1)|| <= exp(2C_E sum_j 1/j)<=2^C_E.        (12)

These bounds hold uniformly on K^+. The factors and their
inverses are holomorphic on a neighborhood of K^+ for all
sufficiently large n. No estimate that grows like an uncontrolled
number of cuts is hidden in (12).

## 5. Uniform first and second derivatives

Set B=2^(C_E/2) and B_inv=2^C_E. The matrix-valued Cauchy
integral formula on circles of radius delta now proves, for
chi in K and r=1,2 (indeed any fixed r>=0),

    ||partial_chi^r V_(m,n)(chi)|| <= r! B/delta^r,
    ||partial_chi^r V_(m,n)^(-1)(chi)||
                                      <=r! B_inv/delta^r.       (13)

The same estimates hold on the delta-neighborhood of K, because
the bounding circles remain inside K^+. These are derivatives
in chi=x/n^2. Derivatives with respect to x gain the factors
n^(-2r); no x derivative has been mistaken for a chi derivative.

For chi in K and |chi'-chi|<=delta, integration along the
straight segment and (13) give the useful relative bound

    ||V_(m,n)(chi')V_(m,n)(chi)^(-1)-I||
           <=(B B_inv/delta)|chi'-chi|.                     (14)

A Taylor approximation has a quadratic remainder bounded by
B |chi'-chi|^2/delta^2, and analogously for the inverse.
Thus nearby actual nodes whose normalized separation is O(1/n)
give an O(1/n) change in this scalar-removed transport. The
constants are independent of n, m, and those nodes inside the
specified compact domain.

## 6. Removing the explicit continuum scalar instead

The branch choice (2) defines

    log Lambda_(m,n)(chi)=sum_j ell(chi n^2/j^2)

as an exact holomorphic logarithm of the finite product. Write
t=m/n in [1,2] and put

    I_t(chi)=integral_1^t asinh(sqrt(chi)/s) ds.

The integrand and its s derivative are uniformly bounded on
K^+ times [1,2]. The right-endpoint Riemann sum with mesh 2/n
therefore gives

    log Lambda_(m,n)(chi)=n I_t(chi)+e_(m,n)(chi),
    |e_(m,n)(chi)|<=C_K, chi in K^+.                       (15)

The error is holomorphic; Cauchy's formula also bounds its
first and second chi derivatives uniformly on K. Consequently

    exp(-n I_t(chi)) P_m(chi n^2)P_n(chi n^2)^(-1)
         =exp(e_(m,n)(chi)) V_(m,n)(chi)                   (16)

and its inverse satisfy the same type of uniform norm and
first/second derivative bounds, with larger constants. The
finite branch matrices are invertible here by their exact
Casoratian and the spectral separation Re(chi n^2)>sup spec K_j.
This gives either an exact-product normalization or the explicit
continuum normalization without introducing a logarithmic branch
ambiguity.

## 7. What this controls and what it leaves open

The theorem controls the analytic variation of the normalized
transport between two nearby cuts, uniformly over a dyadic cut
interval and over complex parameters in a compact subset of
Re chi>0. It applies to the full two-component matrix and its
inverse, rather than to only one selected branch.

It does not assert convergence of V_(m,n) on a full dyadic
interval, or that V_(m,n)-I tends to zero there. More importantly,
(11) still contains the initial matrix P_n(chi n^2). Its own
parameter dependence is not removed by (13)-(14). A growing
matrix formed from many different nodes, followed by deletion
of prescribed low rows, can have cancellations that are not
bounded by these transport estimates. No lower bound for the
actual remainder cofactors or primitive denominator follows
without that remaining comparison.

No numerical or prime scan was used. All complex estimates were
derived from the finite resolvent identities and the explicit
localized half-line vector.
