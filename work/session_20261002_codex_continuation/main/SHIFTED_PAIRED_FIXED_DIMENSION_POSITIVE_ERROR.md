> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A positive shifted paired family: fixed-dimension complete error

Root original target M23, 2026-10-02. Author theorem with new finite exact receipts; research remains ACTIVE.

## Gate and scope

Fresh full-archive searches checked shifted even-derangement moment determinants, large-parameter Hermite limits, and weighted matching Hankel families. The scalar positive common-kernel construction is prior, as are M22's unshifted paired matrix and agent3's signed normalization. This target adds a positive-power shift and proves the COMPLETE error at fixed matrix dimension as the shift grows.

Fresh primary searches identified López–Temme's large-parameter Hermite approximations, the primary CWI record https://ir.cwi.nl/pub/4562/ was read, and NIST's current classical Laguerre-to-Hermite limit https://dlmf.nist.gov/18.7.E26 was read. The university PDF fetch failed and the CWI full-text link failed; no inaccessible full-text theorem is assumed. The proof below uses explicit Gamma moments. Classical orthogonal-polynomial limits and exterior Christoffel kernels are acknowledged methods. The new normalized exponential/logarithmic paired application is author work.

## Shifted exact response matching

Fix k>=2 and n=2k-1. For an EVEN integer M define

    rho_M(F)=mu(y^M F)-F(-1),
    mu(F)=integral_0^infinity exp(-t)F((1-t)^2)dt.

At all sufficiently large M there is a unique monic rational q_(n,M) with rho_M(y^j q)=0 for j<n. Choose its primitive integer normalization. Form

    H_ij=integral_0^1 x^(2(M+i+j))q_(n,M)(x^2)
                        [exp(x)+4/(1+x^2)]dx.

The exact endpoint computation from M22 gives

    H=R+S q(-1)vv^T, S=e+pi, v_i=(-1)^i,         (1)

where R is rational and includes the full exponential constant and rational arctangent endpoint parts. Thus det H=beta_0+beta_1 S. The final rational center and primitive denominator still require the full coefficient clearer and gcd from M22. Neither positivity nor a raw row clearer replaces that arithmetic.

## Why all roots move beyond the integration interval

Split the defining positive measure at t=1 and put u=t-1 on its tail. EXACTLY, for every polynomial F,

    mu(y^M F)=exp(-1) integral_0^infinity u^(2M)exp(-u)F(u^2)du
                   +integral_0^1 exp(-t)(1-t)^(2M)F((1-t)^2)dt.  (2)

The second measure has mass at most1. The first has mass exp(-1)(2M)!, and after division by that mass u has the Gamma distribution of shape alpha=2M+1 and scale1.

Set z=(y-alpha^2)/(2 alpha^(3/2)). For X=(u-alpha)/sqrt(alpha), z=X+X^2/(2sqrt(alpha)). The moment generating function of X is exp(-s sqrt(alpha))(1-s/sqrt(alpha))^(-alpha); expansion at the origin gives convergence of every fixed moment to the standard normal moments. Thus the Gamma-square z moments have the same limit. The compact remainder in(2) and the signed evaluation at y=-1 contribute at most a fixed power of alpha divided by(2M)! to every fixed z moment, hence vanish.

The fixed-degree moment matrices therefore converge to the positive definite normal Gram matrices. The finite linear system defining the scaled monic q converges to the one defining the probabilists' Hermite polynomial He_n. Consequently all n roots are real and simple for sufficiently large M, and have

    lambda_j=alpha^2+2 alpha^(3/2)(h_j+o(1)),      (3)

where h_j are the distinct real roots of He_n. In particular every lambda_j is greater than1. Real simplicity follows from coefficient convergence around the simple real Hermite roots; disjoint small disks and conjugation keep each root real. This proves existence and root location for fixed n, not a uniform estimate when n grows with M.

For y in[0,1], the product over these roots gives

    q(y)/q(-1)=product_j (lambda_j-y)/(lambda_j+1)
              =1+O_n(M^-2)>0.                    (4)

Hence q(-1)!=0 and the normalized moment matrix J=H/q(-1) is positive definite. For odd n its primitive polynomial is negative throughout[0,1] at sufficiently large M; dividing by q(-1) keeps the normalized measure positive.

## Exact signed complete error

Positive definiteness and(1) imply beta_1!=0: the coefficient of S equals q(-1)^k v^T adj(J)v, which is nonzero. The COMPLETE center c=-beta_0/beta_1 satisfies

    S-c=det J/[v^T adj(J)v]
        =1/[v^T J^(-1)v]>0.                      (5)

No exponential endpoint is discarded here. The reciprocal on the right is the minimum squared norm of a degree<k polynomial constrained to take value1 at the exterior point y=-1, for the actual positive normalized measure

    y^M [q(y)/q(-1)]
       [exp(sqrt(y))+4/(1+y)]/(2sqrt(y)) dy.

Thus(5) proves nonvanishing and that these rational centers lie below S. To prove irrationality one would still need the ACTUAL primitive q times this positive error to tend to0. This theorem does not supply that denominator estimate.

## Sharp fixed-k asymptotic constant

Put f(1)=(e+2)/2. In the basis(1-y)^j, j=0,...,k-1, the same positive Gram has entries

    E_ij=integral_0^1 y^M(1-y)^(i+j)[q(y)/q(-1)]f(y)dy
         =f(1)(i+j)! M^(-i-j-1)(1+o(1)),         (6)

with f(y)=[exp(sqrt(y))+4/(1+y)]/(2sqrt(y)). Endpoint scaling u=M(1-y) proves(6); the integrable singularity at0 is suppressed by y^M, and(4) is uniform. After diagonal scaling, the limiting matrix A_ij=(i+j)! is invertible. Its lower-right inverse entry is1/((k-1)!)^2, as follows from the monic Laguerre norms or direct factorial Hankel elimination.

The exterior evaluation vector in this basis is(1,2,...,2^(k-1)). The last term in the inverse quadratic form has the strictly largest power of M, giving

    v^T J^(-1)v ~ 2^(2k-2) M^(2k-1)
                           /[f(1)((k-1)!)^2].

Therefore the COMPLETE positive error is

    S-c_(k,M) ~ (e+2)((k-1)!)^2
                         /[2^(2k-1) M^(2k-1)].   (7)

Every fixed k gives a rational convergent sequence with exact nonzero error. Formula(7) is not uniform in k. It says nothing about a proportional or diagonal growing-dimension sequence; agent3's separate quantitative coercivity target addresses that question.

## New exact finite receipt and arithmetic limit

SHIFTED_PAIRED_DERANGEMENT_CERTIFICATE.json constructs NINE new full paired polynomials/matrices: k=2,3,4 and M=8,32,128. Exact Sturm counts prove every polynomial root is real and greater than1 in these nine cases. Every equal e/pi response, the full determinant's affine dependence, and its final primitive gcd are checked independently. No real diagnostic is used to certify those algebraic facts.

The1000-digit complete error times M^(2k-1), at M=128, is approximately .56855617,.53397328,1.09466916 for k=2,3,4. The respective limits in(7) are about .58978523,.58978523,1.32701676. These values test the fixed-k constant and are labeled diagnostics. Actual q at the same M has10725,26617,50049 bits. That large finite cost is not turned into an asymptotic denominator theorem; neither the full gcd rate nor a main irrationality proof is established. Original arithmetic work continues.
