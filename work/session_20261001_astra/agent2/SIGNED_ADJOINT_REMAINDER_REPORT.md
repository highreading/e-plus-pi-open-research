> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Signed adjoint remainder report

New author research. Completed directional and multirow records are preserved; no controls, scans, or old checks were repeated. Quantitative inverse estimates remain separate author inputs from Child 3.

The exact norm is fixed by

    m=floor((b-1)/2), r0=n+m+1-b,
    w_j=r0!/(n+m+1-j)!, W=diag(w_j^2).

For b=2 this means m=0 and unsubtracted factorial weights. For b>=3 it is the maximal allowed completed multirow norm.

With H=(I+D)^(-n), D_B multiplication by xi-1, and K=D_B H, the ACTUAL B lift is

    u=K T^(-1)f_P,
    v=e_0+K T^(-1)f_Q.

Set a=u^T W u, t=u^T W v/a, z=T^(-T)K^T W u. Then z^T f_P=a and, with lambda=z/a and c0=u^T W e_0/a,

    t-(e+pi)=c0+lambda^T(f_Q-(e+pi)f_P).

The note retains the two complete forcing integrals and their negative outer signs before any absolute values. In its notation,

    t-(e+pi)=c0-C_lambda(E_n)-C_lambda(A_n).

The new analytic lemma is

    |tau q0(xi)/(1-tau xi)|<=sqrt(2)

for tau=(1+iy)/2, -1<=y<=1, and |xi|<=sqrt(2), with endpoint cancellation understood. Its proof uses that 1/tau lies on the right semicircle |omega-1|=1 and that q0(xi)/xi=Re(xi)-1 on the radius-sqrt(2) circle.

Applying Cauchy's formula on rho=sqrt(2)(1-1/n) to the COMPLETE arctangent integral gives the direct adjoint estimate

    |C_lambda(A_n)|<=64 n n! J_lambda,
    J_lambda^2=sum_(i=0)^(b-1)2^(-i)lambda_i^2.

The exponential integral gives

    |C_lambda(E_n)|<=9(1+sqrt(2))^n J_lambda/(n+1).

These estimates retain the actual adjoint polynomial before taking its angular norm. The new arctangent bound removes the former (3/2)^n forcing factor. It is not merely the old forcing estimate with an inverse norm inserted.

Only afterward, using Child 3's author inverse constants, the note proves

    J_lambda<=2Hminus K0/[(1+sqrt(2))^n sqrt(a)],

and the explicit directional bound

    |t-(e+pi)| <=
      [w_0+128n Hminus K0 n!/(1+sqrt(2))^n
                  +18Hminus K0/(n+1)]/sqrt(a).

Every reconstruction and factorial-weight factor is retained. Replacing sqrt(a) by its valid author-input lower bound gives a fully explicit n,b expression in the main note.

On n>=16, 2<=b<=n, n>=512b^4 log n, a displayed exponent ledger yields

    |t-(e+pi)|<=2 n^(8b) 2^(-n)
              =exp(-n log 2+o(n))

as a uniform upper-bound envelope. This improves the previous exp(-n log(4/3)+o(n)) envelope. It is conditional on the separate quantitative inverse input, not an independently accepted inverse theorem or an asymptotic equality for the error.

The complete directional form consequently satisfies

    |P+Q(e+pi)|<=|P+tQ|+2n^(8b)2^(-n)|Q|.

For the actual reduced center t=p/q, the center-pair bounds retain q times this error and 1/q plus half that quantity. No estimate for q is asserted, and each radial lift factor cancels against its own endpoint gcd.

The signed-leading-term branch stops at an exact unresolved coefficient: the arctangent contour includes Lambda((-1+i)/2), its conjugate value, and their signed oscillatory combination. No lower bound preventing their cancellation is known. The exact sum c0-C_lambda(E_n)-C_lambda(A_n) therefore has no proved sign or nonzero leading term. The new quantitative upper bound remains valid without such a claim.

Full proof, constants, and stopping boundary: SIGNED_ADJOINT_REMAINDER.md. Both files must be read back before completion is reported. No center recurrences or reduced-denominator arithmetic were duplicated.
