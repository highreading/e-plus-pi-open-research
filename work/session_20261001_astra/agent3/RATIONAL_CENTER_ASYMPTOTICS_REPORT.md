> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational-center asymptotics: Agent 3 report

Status: new author deductions using the accepted provisional inverse in its stated scope. No prior proof was re-audited and no checks or HP scans were rerun.

The elementary conclusions are |t-(e+pi)|<=exp(-n/8) and det Gram/a^2<=exp(-n/4). They follow directly from the previous lift estimate and are not the new result.

The exact rational center now has a structured formula. Let u,v be the two actual forcing columns, x=T^(-1)u, y=T^(-1)v, U=Z(I+D)^(-n), H=R^T W R, K=U^T H U, and kappa_vec=U^T H e0. Then

    t=(x^T Ky+x^T kappa_vec)/(x^T Kx).

Equivalently, with X=adj(T)u, Y=adj(T)v, Delta=det T,

    t=[X^T KY+Delta X^T kappa_vec]/[X^T KX].

This defines t using rational forcing, coefficient recurrences, and full reconstruction only. It does not use a numerical value of e+pi.

A rational adjoint vector

    lambda=T^(-T)Kx/(x^T Kx)

satisfies lambda^T u=1. Its rational polynomial L(z)=sum lambda_i z^i controls the signed error. There is an exact decomposition

    t-(e+pi)=kappa+epsilon_E+epsilon_F,

and both error components are differences of explicitly defined rational companions from e and pi. No endpoint term is discarded.

The logarithmic component has the new exact arc representation

    epsilon_F=(-1)^(n+1)2n! integral_(-pi/4)^(pi/4)
       (sqrt(2)cos theta-1)^n
       L(1-exp(i theta)/sqrt(2)) dtheta.

Both conjugate endpoints and their orientation are retained. A uniform saddle estimate gives, with

    zstar=1-1/sqrt(2), c=(2+sqrt(2))/2,
    A_n=2n!(sqrt(2)-1)^n sqrt(pi/(cn)),
    Nlambda=sum_i |lambda_i|2^(-i/2),

    |(-1)^(n+1)(t-e-pi)/A_n-L(zstar)|
       <=Nlambda[(12+(b-1)^2)/n+exp(-n)].

The exponential contribution also has a rational integration-by-parts expansion with an explicit uniform remainder. Its first b coefficients come directly from the solved Toeplitz columns. The complete endpoint-plus-exponential correction is factorially smaller than the displayed logarithmic envelope in the stipulated slow range.

The leading coefficient L(zstar) is algebraic construction data, defined without e+pi. However, its uniform separation from zero remains unproved. A rigorous signed two-sided bound follows when

    |L(zstar)|/Nlambda > (12+(b-1)^2)/n+exp(-n).

No such inequality is claimed on an unbounded family. For b>=3, exact vanishing is equivalent to divisibility of L by 2z^2-4z+1. For b=2 that vanishing is impossible, but a sufficient uniform quantitative lower bound is still missing.

The explicit b dependence permits analytic parameter choice if a lower bound for this coefficient ratio is established. The additive remainder tends uniformly to zero on its Nlambda scale for n>=512b^4 log n; finite nonzero coefficients or fixed-b asymptotics cannot supply the missing uniform lower bound.

Child 4 retains reduced-denominator arithmetic. Child 2 retains the complete functional bound. Full-coefficient and B-only centers are distinguished explicitly; constant-factor norm comparison does not identify them.

Saved deliverables: RATIONAL_CENTER_ASYMPTOTICS.md, RATIONAL_CENTER_ASYMPTOTICS_REPORT.md, and RATIONAL_CENTER_COORDINATION.md. These require actual read-back before completion is reported. No first uniformly nonzero signed error term or shrinking primitive pair is claimed.
