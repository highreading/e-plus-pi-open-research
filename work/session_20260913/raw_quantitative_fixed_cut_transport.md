> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Quantitative fixed-cut transport through a removable parameter singularity

Date: 2026-09-13. Original continuation by audit_sources, following
the proposed complex-disk argument from root. Independent review
in `raw_quantitative_fixed_cut_independent_review.md` passes the
full proof and its propagation to the actual columns and kernels.

This note upgrades the fixed-cut convergence in
`raw_global_corrected_transport.md` to O(log(N)/N), locally
uniformly and holomorphically for x=chi N^2, Re chi>0. It proves
the required full complex disk extension instead of assuming
that a right-half-plane estimate continues there. The rate also
applies to the actual normalized column and high-kernel limits.

The scalar products and the distinct column powers remain exact.
No stability theorem for a determinant with a growing number of
nodes follows from this rate alone.

## 1. An exact corrected step with no square-root ambiguity at zero

For j>=3 put alpha=(j-2)/j and use the parameter

    c(w)=(1-w^2)^2/(4w^2),  x=j^2 c(w),  q=w^2.

For positive small w these are the original branches and
lambda=1/w^2. Fix, for example, R=1/8. On |w|<=R define

    h_alpha(w)=sqrt((1-w^2)^2+4 alpha^2 w^2), h_alpha(0)=1,
    rho_alpha(w)=2alpha/(h_alpha(w)+1-w^2),
    eta(w)=w/(1-w^2),
    b_alpha(w)=sqrt((1+w^2)/h_alpha(w)).                 (1)

All functions in (1) are analytic on a neighborhood of this
closed disk; rho_alpha has no zeros there. The square root of
rho_alpha is chosen to have value sqrt(alpha) at zero. These
properties and their bounds are uniform in 1/3<=alpha<=1:
the squared expression defining h differs from one by at most
2R^2+R^4<1, and its chosen branch stays near one.

Let iota_j embed the last two coordinates of the actual finite
row matrix K_j. Define

    C_j(w)=iota_j^T (I-K_j/(j^2 c(w)))^(-1) iota_j,

    Q_j(w)=[j^2(1-w^2)^2/4] Gamma_j^(-1) C_j(w)^(-1).  (2)

The established spectral enclosure implies ||K_j/j^2||<=1 for
all j>=3. Moreover

    |c(w)| >= (1-R^2)^2/(4R^2)>15

on the punctured disk. The resolvent in (2) and its boundary
compression are therefore invertible by uniform Neumann bounds.
They extend analytically to w=0, with C_j(0)=I. Every entry of
Q_j is analytic in w^2. Gamma_j is lower triangular, so

    Q_j(0)=j^2 Gamma_j^(-1)/4,
    (Q_j(w))_12=O_j(w^2).                              (3)

For positive w, (2) equals the original T_j(x)/lambda(x/j^2).
It follows directly from T_j=Gamma_j^(-1)(R_j^physical)^(-1)
and R_j^physical=x^(-1) C_j.

The explicit cocycle in the accepted global theorem now gives
the following expression for its corrected step:

    S_j(w)=b_alpha(w) exp(-eta(w) sigma_1)
       [[Q_11 sqrt(rho_alpha), Q_12/(w sqrt(rho_alpha))],
        [w Q_21 sqrt(rho_alpha), Q_22/sqrt(rho_alpha)]]
                  exp(alpha eta(w) sigma_1).           (4)

Indeed w(j,x)=w and w(j-2,x)=w rho_alpha(w), while the
scalar ratio is b_alpha. Equation (4) cancels the individual
square roots of w. Its only apparent pole is Q_12/w, which
is removable by (3). Consequently S_j is holomorphic on the
whole disk, including zero, and

    S_j(0)=L_j=diag(ell_j^+,ell_j^-),

    ell_j^+=[j^2/(4 a_(j-1)a_j)] sqrt((j-2)/j),
    ell_j^-=[j^2/(4 a_j a_(j+1))] sqrt(j/(j-2)).         (5)

These are exactly the previously proved fixed-step limits.
Equation (4), rather than a choice of a multivalued individual
F on a loop about zero, defines the full-disk continuation.
It agrees with the original corrected step on its original
small-w right-half-plane domain.

## 2. A uniform O(j^-2) bound on the full disk

We verify that the accepted localized perturbation proof applies
on this disk with constants independent of j. This is necessary
before applying Cauchy's estimate.

Both the embedded K_j/j^2 and the limiting two-channel half-line
operator have norm at most one. Hence on the disk, without any
assumption on Re c,

    ||(cI-K_j/j^2)^(-1)|| <= 2/|c|,
    ||(cI-L_0)^(-1)|| <= 2/|c|.                        (6)

The limiting boundary entry is m=4w^2, and its geometric
boundary vector has coordinates m q^k, q=w^2. Every fixed
polynomially weighted norm of this vector is O(1/|c|), since
|q|<=R^2<1 and

    |c| |m|=|1-w^2|^2.

The same coefficient perturbation bounds as in
`raw_first_matrix_transport_correction.md` thus give, in its
exact sandwiched second resolvent identity,

    R_j^bd(c)=mI+B(c)/j+O(1/(|c|^2 j^2)).              (7)

More explicitly, the linear coefficient remainder is bounded
by C/(|c|^2 j^2), using the weighted boundary vectors. The
quadratic term has the additional resolvent factor from (6)
and is bounded by C/(|c|^3 j^2), which is smaller. No claim
of small operator norm for the entire coefficient perturbation
is used. The explicit first correction B satisfies B/m=O(1/|c|)
on this disk. The geometric vector formula and that expression
for B are analytic identities here, by their resolvent derivation
or continuation from small positive w.

Dividing (7) by m and inverting gives the earlier factorization

    Q_j=(G_j^(-1)/4)(R_j^bd/m)^(-1), G_j=Gamma_j/j^2,
    Q_j=I+A(c)/j+E_j,
    ||E_j||<=C/j^2, |(E_j)_12|<=C/(|c| j^2).           (8)

The last estimate holds because G_j^(-1)/4 is exactly lower
triangular: its unsuppressed second-order error contributes no
upper-right entry. All estimates in (7)-(8) hold uniformly for
large j on the disk. The finitely many smaller j>=3 have the
analytic expressions (2)-(4) with the same fixed disk and can
be incorporated by increasing constants where appropriate.

The reference cocycle has the same error estimate as in (8).
Here this can be checked using the explicit expressions

    s(c)=(1-w^2)/(1+w^2),
    A_12(c)=2w^2/(1-w^2),
    A_21(c)=2/(1-w^2),
    c d/dc=-[w(1-w^2)/(2(1+w^2))] d/dw.               (9)

The diagonal entries of A are -1/(c+1) plus or minus s.
Thus A and cA' are uniformly bounded, while their upper-right
entries are O(1/|c|). Along j-2<=t<=j, |x/t^2|>=|c|, and
the same large-|c| branch of these formulas applies. The local
ODE estimate, with the separate upper-right weighted estimate,
therefore gives

    F(j,x)F(j-2,x)^(-1)=I+A(c)/j+E_j^ref,
    ||E_j^ref||<=C/j^2,
    |(E_j^ref)_12|<=C/(|c| j^2).                       (10)

Subtract (10) from (8). In formula (4), diagonal conjugation
multiplies this difference's upper-right entry by 1/w and its
lower-left entry by w. Since |c|^(-1)=O(|w|^2), all resulting
entries remain O(j^-2), uniformly down to w=0. The factors
b_alpha, sqrt(rho_alpha), and the exponentials in (4) are
uniformly bounded, as are their inverses. This proves

    sup_(|w|<=R) ||S_j(w)-I|| <= C/j^2, j>=3.           (11)

The finite initial j cause no exception: (4) is uniformly
bounded on the fixed disk for each such j, so the finite maximum
of j^2 times that bound can be absorbed into C. There are no
row-spectrum poles on the disk, by (2) and (6).

## 3. Cauchy's estimate and the global product rate

Apply Cauchy's estimate to S_j-I on the disk in (11). On
|w|<=R/2 it gives

    ||S_j(w)-L_j|| <= C |w|/j^2.                       (12)

Now fix a compact K in H={Re chi>0}, let x=chi N^2, and set
w_j=sqrt(q(x/j^2)) on the original branches. The earlier
right-half-plane estimates imply

    |w_j| <= j/(2N sqrt(|chi|)) <= C_K j/N.             (13)

If |w_j|<=R/2 use (12). Otherwise the accepted uniform
right-half-plane estimate S_j-I=O_K(j^-2), together with
L_j-I=O(j^-2), is at most C_K |w_j|/j^2 because now
|w_j|>=R/2. These estimates apply to all sufficiently large j.
For any remaining finite j, (13) places w_j inside the disk for
all sufficiently large N; (12) then applies. Consequently

    ||S_j(chi N^2)-L_j|| <= C_K/(Nj)                  (14)

for every J+2<=j<=N of the prescribed parity, once N is large,
for each fixed initial J>=1.

All ordered subproducts of these S_j and of the L_j are
uniformly bounded: the large-j steps differ from I by summable
O_K(j^-2), and the finite initial steps are bounded by (4).
Telescoping the difference between the two ordered products
and using (14) gives

    ||product_(j=J+2,step 2)^N S_j
          -product_(j=J+2,step 2)^N L_j||
       <= C_(K,J) sum_(j=J+2,step 2)^N 1/(Nj)
       <= C_(K,J) log(N)/N.                            (15)

The missing tail of the convergent product of L_j is O_J(1/N),
since L_j-I=O(j^-2). In the notation of the accepted global
theorem, its exact positive diagonal limit is D_J. We obtain

    W_(N,J)(chi N^2)=D_J+O_(K,J)(log(N)/N).             (16)

The same bound holds for W_(N,J)^(-1)-D_J^(-1), by inversion
near the nonzero limiting matrix. Every expression is
holomorphic in chi on a fixed neighborhood of K for all large
N. Applying (16) on a slightly larger compact subset of H and
then Cauchy's formula proves, for each fixed integer r>=0,

    partial_chi^r [W_(N,J)(chi N^2)-D_J]
          =O_(K,J,r)(log(N)/N),                        (17)

and the analogous assertion for the inverse. For r>=1 the
derivative of the constant D_J is zero. These are derivatives
after the exact scalar product has been removed.

## 4. Propagation to the actual columns and their conditioning

Use J=2 in even degree and J=1 in odd degree, as in
`raw_actual_branch_column_asymptotics.md`. That note's two
explicit initial matrices, evaluated in (4)'s local parameter,
satisfy their scaled limits with O_K(1/N) error when x=chi N^2.
This follows directly from the finite polynomial entries and
the convergent expansion in x^(-1/2); it is also valid locally
holomorphically with derivatives.

Let A_parity(c)=B(c) C_parity and D_p(x) be exactly the
limiting column matrix and power diagonal defined in that note.
Equations (16)-(17) now sharpen its formulas (7)-(8) to

    N^(1/2) Lambda_(N,J)(cN^2)^(-1)
                  P_N(cN^2) D_p(cN^2)^(-1)
       =A_parity(c)+O_K(log(N)/N),                     (18)

with the same rate for every fixed number of c derivatives.
The scalar Lambda and both unequal column powers are unchanged.
No entrywise relative estimate at a possible complex zero is
implied.

On positive compact intervals A_parity is uniformly invertible
and its first column has norm bounded away from zero. The
two-by-two singular-value argument in the column note therefore
also gives

    cond(P_N(cN^2))/N
       =kappa_parity(c)+O_K(log(N)/N).                 (19)

Each of its two singular-value asymptotics in formula (12) has
relative error O_K(log(N)/N). These real norm consequences do
not require derivatives of singular values at complex points.

## 5. Propagation to the mixed-node and actual high kernels

The analytic boundary divided difference in the column note
already has O_K(1/N) error, including its diagonal and fixed
parameter derivatives. Combining it with (18) sharpens that
note's full-kernel limit (16) to

    D_p(x)^(-1) Kcal_N(x,y) D_p(y)^(-1)
                      /[s_N(x)s_N(y)]
       =k(c,d) A_parity(c)^T A_parity(d)
                       +O_K(log(N)/N),
    x=cN^2, y=dN^2.                                   (20)

The error is an absolute two-by-two matrix norm error, locally
uniform in both complex parameters, with every fixed number
of derivatives. Here s_N, k, and the transpose convention are
unchanged from the original exact formula.

For the actual interval n+1,...,2n-1 at x=cn^2,y=dn^2,
the lower-cut contribution in the upper-cut 2n normalization
was proved exponentially small, uniformly on these compact
sets. Its estimate did not require a rate for the upper-cut
columns. Hence the same argument and (20) give

    D_even(x)^(-1) Kcal_hi,n(x,y) D_even(y)^(-1)
                         /[s_(2n)(x)s_(2n)(y)]
       =k(c/4,d/4) A_even(c/4)^T A_even(d/4)
                         +O_K(log(n)/n).               (21)

This rate likewise survives any fixed number of parameter
derivatives. Actual node amplitude factors remain exact when
passing from this matrix kernel to a selected physical Gram
matrix; they have not been absorbed into a uniform error.

## 6. Scope

The full-disk removable singularity supplies the factor |w_j|
that was missing from the original summable-tail argument. The
result is a quantitative fixed-cut limit and a quantitative
absolute kernel approximation on compact subsets of Re c>0.

For m selected nodes in such a compact set, a uniform entry
error O(log(n)/n) gives only the crude operator error
O(m log(n)/n) before further structural information. This is
not automatically smaller than the limiting matrix's smallest
eigenvalue. In particular it does not settle the full-density
many-node determinant problem, nor does it cover parameters
tending to zero. A sparse-node consequence requires a separate
explicit eigenvalue comparison with this actual error rate.

No numerical degree or root scan was used in this proof.
