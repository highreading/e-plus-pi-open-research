> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete forcing envelope with rate log 2

Status: preserved main-agent author derivation. Not independently reviewed. The kernel estimate below is a new paper argument; propagation to the actual rational center depends on the separate quantitative inverse estimates in agent3/CONTACT_INVERSE_RESEARCH.md, especially its completion Section 9. Accepted contact normality does not by itself verify those inverse estimates. No denominator-growth theorem or conclusion about e+pi is established.

This records the pre-maintenance derivation before further expansion. Agent 2 subsequently reported a separate bound with the same exponential rate in SIGNED_ADJOINT_REMAINDER.md. That report is another author result, not independent verification of this draft.

## 1. Domain and actual forcing

Write Q0(z)=1-z+z^2/2, S=e+pi, R=sqrt(2), M=1+sqrt(2), and d=b-1. The elementary kernel argument applies for n>=2 and 1<=b<=n. The center application uses n>=16, 3<=b<=n, and n>=512 b^4 log n.

The reviewed contact reduction uses the b by b Toeplitz matrix

    T_ij=[z^(n+i-j)] exp(z)Q0(z)^n, 0<=i,j<b.

Its actual forcing columns satisfy fQ=S fP+eF+eE, where eF and eE are the coefficients at n+i of the complete residual functions

    H_F(z)=-n! integral_-1^1 [t Q0(z)/(1-tz)]^n
                         /[(1-t)(1-tz)] du,
    t=(1+iu)/2,

    H_E(z)=-Q0(z)^n integral_0^1 x^n exp(1-x)exp(xz) dx.

Both entire forcing contributions and the constant term in reconstruction must remain. Let D_R=diag((-R)^i), 0<=i<b.

## 2. A kernel bound retaining both conjugate endpoints

Set t_plus=(1+i)/2 and t_minus=(1-i)/2. Then

    Q0(z)=(1-t_plus z)(1-t_minus z).

For u in [-1,1], put alpha=(1+u)/2. Since t=alpha t_plus+(1-alpha)t_minus,

    (1-tz)/Q0(z)
      =alpha/(1-t_minus z)+(1-alpha)/(1-t_plus z).

For any complex w with |w|<=theta<1,

    Re(1/(1-w))>=1/(1+theta).

Indeed, after multiplication by |1-w|^2, the required difference is

    theta+(1-theta)Re(w)-|w|^2>=0,

using Re(w)>=-theta and |w|^2<=theta^2. Thus on |z|<=R theta the preceding convex combination has real part at least 1/(1+theta). Inverting its modulus and using |t|<=1/R gives

    |t Q0(z)/(1-tz)| <= (1+theta)/R.                (1)

Also |1-t|>=1/2 and |1-tz|>=1-theta. Integrating over an interval of length two therefore yields

    |H_F(z)| <= 4n!/(1-theta) * [(1+theta)/R]^n.

This bound involves the complete integral, not its first omitted coefficient. The circle remains strictly inside all possible poles.

## 3. Complete coefficient-vector bound

Cauchy's coefficient estimate on |z|=R theta, with the original coefficient index n+i and the diagonal scaling R^i retained, gives

    ||D_R eF||_2
      <=4 sqrt(b)n!/(1-theta) * theta^(-d)
                         *[(1+theta)/(2theta)]^n.     (2)

Choose theta=1-1/n. Then theta^(-d)<=theta^(-(n-1))<e<3, and

    [(1+theta)/(2theta)]^n
       =[1+1/(2(n-1))]^n<=e<3.

Consequently

    ||D_R eF||_2 <=36n sqrt(b)n!.                     (3)

The former estimate was 16 sqrt(b) R^d n!(3/2)^n. Equation (3) removes its exponential factor. No assertion that this contour is optimal is made.

The separate exponential residual retains the previously derived bound

    ||D_R eE||_2 <=27 sqrt(b)M^n/(n+1).

Thus a complete forcing envelope is

    E0_new=36n sqrt(b)n!+27 sqrt(b)M^n/(n+1).          (4)

## 4. Conditional propagation through the actual inverse

Retain the inverse paper's explicit quantities

    Cint=(16 b^2 n)^d binom(2d,d)/(d!)^2,
    K0=2048 b sqrt(n) Cint,
    Hplus=(n+1)^d, Hminus=(n+b)^d,
    Fminus=n!2^n/(2n+1),
    L=Fminus/[9b R^d Hplus M^n].

The required separate inverse inputs are

    ||D_R T^(-1)f||_2<=K0 M^(-n)||D_R f||_2,
    ||D_R T D_R^(-1)||_2<=9M^n,

and the finite reconstruction bounds recorded in that paper. They imply, for the actual B-coefficient lift u=Psi(1,0), v=Psi(0,1),

    ||u||_2>=L,
    ||v-Su||_2<=E_new,
    E_new=1+2Hminus K0 E0_new/M^n.                    (5)

The additive one comes from B=Q+(z-1)B' and is essential.

Fix the factorial weights used in MULTIROW_REMAINDER_RESEARCH.md:

    1<=m<=floor((b-1)/2),
    w_j=(n+m+1-b)!/(n+m+1-j)!,
    W=diag(w_j^2).

They satisfy 0<w_j<=1 and wmin>=(2n)^(-b). Define the actual rational B-only center

    t_n=(u^T W v)/(u^T W u).

Weighted Cauchy-Schwarz and (5) give

    |S-t_n|<=E_new/(wmin L)<=(2n)^b E_new/L.           (6)

This center need not equal the full-coefficient Gram center.

Expanding the last expression in (6) gives three positive terms. Their exponential factors and prefactors are respectively

    ((M/2)^n/n!) * C1,
    2^(-n) * C2,
    ((M/2)^n/n!) * C3,

where

    C1=9(2n)^b b R^d Hplus(2n+1),
    C2=648n(2n)^b b sqrt(b) R^d Hplus Hminus K0(2n+1),
    C3=486(2n)^b b sqrt(b) R^d Hplus Hminus K0(2n+1)/(n+1).

Each is at most n^(10b) in the stated slow-growth domain. An explicit conservative ledger uses K0<=n^(2b), (2n)^b<=n^(3b/2), Hplus,Hminus<=n^(3d/2), R^d<=n^(d/2), b sqrt(b)<=n, and 2n+1<=n^2. The numerical constants are at most n on this domain. Including the extra n in C2 gives exponent at most 7b+3/2<=10b; C1 and C3 have fewer factors. These comparisons depend on the inverse paper's proved-within-author-scope bound for K0.

Therefore the preserved envelope is

    |S-t_n|<=delta_n,
    delta_n=n^(10b)[2^(-n)+2(M/2)^n/n!].             (7)

Since b log n=o(n) uniformly when n>=512b^4 log n, and the factorial term is eventually smaller than 2^(-n),

    delta_n<=exp(-(log 2)n+o(n)).                     (8)

This is an upper-envelope rate, not a nonzero signed asymptotic or an error lower bound.

## 5. Complete primitive forms and the actual denominator

Write t_n=p_n/q_n in lowest terms, q_n>0. Choose integers x_n,y_n with

    q_n x_n+p_n y_n=1, |y_n|<=q_n/2.

The primitive endpoint vectors (-p_n,q_n) and (x_n,y_n) have determinant -1. Their complete forms satisfy

    |-p_n+q_n S|<=q_n delta_n,
    |x_n+y_n S|<=1/q_n+q_n delta_n/2.                (9)

Each vector's minimal integer polynomial lift multiplies its coefficients, remainder, and endpoint gcd by the same factor. That factor cancels and supplies no additional primitive gain.

Consequently q_n->infinity and q_n delta_n->0 suffice for irrationality. A sufficient same-index rate condition using (8) is

    q_n->infinity,
    limsup log(q_n)/n<log 2.                         (10)

Neither condition has been established for the actual center.

Alternatively, q_n delta_n->0 together with nonstabilization of the rational centers suffices. If S=u/v were rational, any different center would satisfy q_n|S-t_n|>=1/v. Thus the bound would force t_n=S eventually, contrary to nonstabilization.

Whenever two centers differ, rational separation gives

    1/(q_n q_l)<=|t_n-t_l|<=delta_n+delta_l.          (11)

For adjacent changing centers, (8) therefore implies log q_n+log q_(n+1)>=(log 2)n-o(n). A uniform upper exponent below (log 2)/2 would force eventual stabilization. This is a constraint on the proposed strategy, not an actual denominator theorem.

## 6. Exact arithmetic interface and scope

Use precisely the B-only factorial norm in Agent 4's RATIONAL_CENTER_ARITHMETIC.md. Its notation gives

    q=g1 A_*/kappa,
    kappa=gcd(g1 A_*, |g2(t A_*+c_perp H_*)|).

The t inside this last expression is that paper's saturated-basis integer, not the rational center t_n. The two conditions for the direct pair (9) are exactly

    g1 A_* delta_n=o(kappa),
    kappa=o(g1 A_*).

The necessary large-gcd conditions derived for the older separated-tail quadratic certificate are not automatically necessary for this direct directional estimate. The complete cancellation is retained in (6) before primitive evaluation.

The exact signed adjoint identity remains available. If u=K T^(-1)fP and v=e0+K T^(-1)fQ, with K the full B reconstruction operator, put a=u^T W u and z=T^(-T)K^T W u. Then

    t_n-S=[u^T W e0+z^T(fQ-SfP)]/a.

Equation (7) bounds this indirectly; it supplies neither a nonzero signed leading term nor nonstabilization.

The limited review needed for the newly used inverse inequalities and this propagation has not yet completed. Contact normality alone has scoped independent PASS. The unconditional rationality or irrationality of e+pi remains unresolved.
