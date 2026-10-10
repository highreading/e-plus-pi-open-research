> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Positive forcing, even-index normality, and the complete tau envelope

Status: preserved main-agent author deductions. Not independently reviewed. This records the previously unsaved arguments without changing LOG_TWO_FORCING_ENVELOPE_DRAFT.md. The complete tau envelope additionally assumes the new logarithmic forcing-vector inequality reported in agent2/LOGARITHMIC_FORCING_VECTOR.md. No reduced-denominator or irrationality conclusion is established.

## 1. Exact positive forcing normalization

Put Q0(z)=1-z+z^2/2, R=sqrt(2), M=1+sqrt(2), and d=b-1. The actual positive forcing column is

    fP_i=[z^(n+i)] Q0(z)^n D^n(1/(1-z)),
    fP_i=n! 2^(-n) sum_l binom(n,l)binom(2n+i-2l,n+i),

where 0<=l<=floor(n/2), and 0<=i<b. All summands are positive.

The central entry satisfies

    fP_0=n! binom(2n,n)p_n(1).                         (1)

Indeed fP_0/n! is the coefficient of z^n in

    2^(-n)((1+z)^2+1)^n=(1+z+z^2/2)^n.

The generating function of these central coefficients is (1-2x-x^2)^(-1/2). This follows by taking the constant term of 1/[1-x(z^(-1)+1+z/2)]. The Legendre generating function gives the same series for binom(2n,n)p_n(1), proving (1).

Write s=(sqrt(2)-1)^2 and a=M/4. The established inequalities

    p_n(1)>=(1-s)a^n,
    binom(2n,n)>=4^n/(2sqrt(n))

and (1-s)/2=1/M imply

    fP_0>=n! M^(n-1)/sqrt(n), n>=1.                  (2)

In each summand of fP_i, its binomial factor divided by the corresponding factor at i=0 is

    product_(j=1)^i (2n-2l+j)/(n+j).

Every factor lies between one and two. Consequently, with D_R=diag((-R)^i),

    fP_0 sqrt(2^b-1)<=||D_R fP||_2
                         <=fP_0 sqrt((8^b-1)/7).     (3)

These identities concern the actual coefficient window and retain the diagonal scaling.

## 2. Contact normality for every even n

Take even n>=2 and 2<=b<=n. The retained exact contact reduction is

    det J_(n,b)=(-1)^(nb) K_(n,b) det T,
    T_ij=[z^(n+i-j)]exp(z)Q0(z)^n,
    K_(n,b)>0.

Set H=(-1)^n D_R T D_R^(-1). Its Toeplitz symbol is

    phi(u)=(1+R cos u)^n exp(-R exp(iu)).

For a coefficient polynomial p associated to a vector x, Fourier expansion gives

    Re(x* H x)=(1/(2pi)) integral_-pi^pi
       (1+R cos u)^n exp(-R cos u)
       cos(R sin u)|p(exp(iu))|^2 du.                 (4)

Changing the Fourier convention replaces u by -u and leaves the real quadratic form unchanged. The elementary alternating cosine bound gives cos(R sin u)>=7/45. For even n, the remaining weight is nonnegative and vanishes at only finitely many points. A nonzero polynomial cannot vanish on an arc, so (4) is strictly positive for x!=0.

Thus H is nonsingular. It is real. Every matrix (1-t)I+tH, 0<=t<=1, is strictly accretive, so its real determinant never vanishes. Continuity from the identity proves det H>0. Since n is even, det J_(n,b)>0.

The established endpoint-kernel division by z-1 now gives a two-dimensional relaxed matched space and an endpoint isomorphism onto Q^2 throughout this even-index range. In particular b=floor(n/2) is included. This argument does not establish useful primitive approximants there.

## 3. Explicit even-index inverse bound

Let

    Cint=(16b^2 n)^d binom(2d,d)/(d!)^2.

Interpolation on the arc |u|<=1/sqrt(n) gives

    integral |p(exp(iu))|^2 du
       >=||x||_2^2/(b sqrt(n) Cint).                 (5)

For completeness, choose b intervals of width 1/(b sqrt(n)), alternating with gaps of the same width inside that arc. Select one point in each interval by the integral mean inequality. Distances between nodes indexed i,j are at least |i-j|/(2b sqrt(n)). Each degree-d Lagrange numerator has coefficient l1 norm at most 2^d. Cauchy-Schwarz applied to the interpolation formula, together with sum_j binom(d,j)^2=binom(2d,d), proves (5).

On the central arc, (1+R cos u)^n>=M^n/2, exp(-R cos u)>1/9, and cos(R sin u)>=7/45. Thus Re phi>=M^n/128. All contributions outside the arc remain nonnegative for even n. Equations (4)-(5) imply

    ||D_R T^(-1)D_R^(-1)||_2
       <=256pi b sqrt(n) Cint M^(-n).               (6)

The forward norm is at most exp(R)M^n<9M^n. No fourth-power restriction on b is used in this even-index argument. Its dimension costs can nevertheless be large.

## 4. Complete forcing combination

The actual forcing decomposition is fQ=S fP+eF+eE, S=e+pi. Assume the newly reported complete logarithmic-vector bound

    ||D_R eF||_2<=2sqrt(pi b/n)n! M^(-n), n>=16,     (A)

from agent2/LOGARITHMIC_FORCING_VECTOR.md. This note does not independently certify (A). Retain the complete exponential bound

    ||D_R eE||_2<=27sqrt(b)M^n/(n+1).

Let Kinv be an explicit constant with inverse norm at most Kinv M^(-n). One may use the inverse paper's K0 on its stated slow-growth domain, or the new even-index constant in (6) on its author-proved domain. Put

    Hplus=(n+1)^d, Hminus=(n+b)^d.

The finite operators (D+1)^n and (D+1)^(-n) on degree-d polynomials have norms at most Hplus and Hminus. This follows from their finite derivative expansions and ||D^l||_2=d!/(d-l)!.

Write u=Psi(1,0), v=Psi(0,1) for the actual B-coefficient lift. Multiplication by z-1 costs at most two; its inverse on its image costs at most b. Using (2)-(3), the forward Toeplitz bound gives

    ||u||_2>=Lstar,
    Lstar=n!sqrt(2^b-1)/(9M b R^d Hplus sqrt(n)).       (7)

The complete residual, including the constant endpoint term, satisfies

    ||v-Su||_2<=Estar,
    Estar=1+54Hminus Kinv sqrt(b)/(n+1)
             +4Hminus Kinv sqrt(pi b/n)n!M^(-2n).    (8)

The additive one must remain.

Fix the factorially weighted B-only norm

    1<=m<=floor((b-1)/2),
    w_j=(n+m+1-b)!/(n+m+1-j)!, W=diag(w_j^2).

For b>=3, these weights satisfy wmin>=(2n)^(-b). The same rational center throughout is

    t=(u^T W v)/(u^T W u).

Weighted Cauchy-Schwarz proves

    |S-t|<=deltastar=(2n)^b Estar/Lstar.             (9)

Equivalently, with

    Pstar=9M b R^d Hplus sqrt(n)(2n)^b/sqrt(2^b-1),

one has the explicit envelope

    deltastar=Pstar[(1+54Hminus Kinv sqrt(b)/(n+1))/n!
                   +4Hminus Kinv sqrt(pi b/n)M^(-2n)]. (10)

On the previously reviewed slow-growth normality domain, the author inverse bound has log Kinv=O(b log n+log n). Therefore (10), conditional on its named inputs, gives

    |S-t_n|<=exp(-tau n+o(n)), tau=2log M.

Using (6), the same conclusion follows within author scope for even n and b log n=o(n). The next note improves the dimension dependence of the even inverse.

## 5. Primitive arithmetic remains unresolved

For the actual reduced center t_n=p_n/q_n, choose q_n x_n+p_n y_n=1 with |y_n|<=q_n/2. The independent primitive forms have bounds

    |-p_n+q_n S|<=q_n deltastar,
    |x_n+y_n S|<=1/q_n+q_n deltastar/2.

Thus q_n->infinity and q_n deltastar->0 suffice for irrationality. Alternatively, nonstabilization and q_n deltastar->0 suffice. Neither is established for these centers. The full-coefficient Gram center generally differs from this B-only center.

Every minimal polynomial lifting multiplier cancels against its own endpoint gcd. The exact denominator q cannot be replaced by a clearer, a lattice index, or a bound for inverse entries.

All extensions in this note remain author deductions. In particular the even-index result and the combined tau propagation have not completed independent examination. No conclusion about the rationality of e+pi is claimed.
