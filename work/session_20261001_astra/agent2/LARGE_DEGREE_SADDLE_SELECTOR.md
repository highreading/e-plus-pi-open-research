> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large-degree rational saddle selector

Status: new author analytic reduction, not a completed asymptotic theorem. No numerical scans, repeated checks, or independent review were performed. The logarithmic-degree RATIONAL_SADDLE_SELECTOR theorem is preserved. Its reported Gamma correction is recorded separately in RATIONAL_SADDLE_SELECTOR_GAMMA_CORRECTION.md and has been read back. No result from its m<=log n saddle analysis is extrapolated here.

## 1. Unrestricted direct forcing coordinates

For n>=1 and every integer i>=0 define

 fP_i=[z^(n+i)]Q0(z)^n D_z^n(1/(1-z)),
 fQ_i=[z^(n+i)]Q0(z)^n D_z^n((exp(z)+F(z))/(1-z)),
 Q0(z)=1-z+z^2/2, F(z)=4 arctan(z/(2-z)).

These rational coordinates exist without a Hermite–Pade degree window. Let

 L_m(t)=(2t^2-4t+1)^(2m)=sum_i lambda_i t^i,
 D=sum_i lambda_i fP_i,
 Flog=sum_i lambda_i eF_i,
 Eexp=sum_i lambda_i eE_i.

Here fQ=(e+pi)fP+eF+eE is the complete forcing decomposition. The selector has degree 4m, integer coefficients, and coefficient l1 height 7^(2m). The rational quotient c=sum lambda_i fQ_i/D is defined only if D!=0. In that case c-(e+pi)=(Flog+Eexp)/D. No endpoint reconstruction constant is present in this direct quotient.

Put V(t)=t^2-t+1/2. Coefficient comparison valid for all i>=0 gives

 D=D_t^n[V(t)^n L_m(t)] at t=1.

Consequently, with P(x)=1+2x+2x^2,

 D=n! 2^(-n) C_n(m),
 C_n(m)=[x^n]P(x)^n(1-2x^2)^(2m).

This is an unrestricted finite coefficient formula; there is no requirement 4m<n.

## 2. Denominator gate and an exact finite exceptional set

For k=floor(n/2),

 C_n(m)=sum_(j=0)^k (-2)^j binom(2m,j)[x^(n-2j)]P(x)^n.

For fixed n this is a polynomial in m of degree exactly k. Its leading coefficient is (-4)^k/k! for even n, and 2n(-4)^k/k! for odd n. For n=1 it is the nonzero constant 2. Thus at each fixed n there are at most k exceptional values of m making D zero.

This does NOT prove D!=0 at m=floor(rho n log n). The exceptional polynomial changes with n. Every quotient statement below retains the condition C_n(m)!=0; no nonvanishing assertion on that sequence is made. In particular a proposed conjugate-saddle asymptotic cannot be divided until its signed sum is quantitatively separated from zero.

## 3. Complete logarithmic and exponential integrals

The arbitrary-polynomial logarithmic identity, obtained by coefficient comparison and n integrations by parts with vanishing endpoint terms, is valid at every finite selector degree:

 Flog=(-1)^(n+1)n! integral_-1^1
       V(t)^n L_m(t)/(1-t)^(n+1) dy,
 t=(1+iy)/2.

The zeros of V^n at both endpoints have order n, independently of the degree of L_m. Hence the integration-by-parts boundary cancellation remains valid in the enlarged domain.

Set R=sqrt(2). The equivalent exact real-arc formula is

 Flog=(-1)^(n+1)(-4)^m 2n! integral_-pi/4^pi/4
       (R cos theta-1)^n sin(theta)^(2m) cos(2m theta) dtheta.

The oscillatory factor cannot be replaced by one when m is comparable to n log n. Both conjugate contributions remain in this expression.

The complete exponential contribution is

 Eexp=-integral_0^1 s^n exp(1-s)
       sum_i lambda_i [z^(n+i)]Q0(z)^n exp(sz) ds.

An alternative exact contour form uses Lambda=L_m:

 Eexp=-(1/(2pi i)) integral_0^1 s^n exp(1-s)
       contour exp(sz)Q0(z)^n L_m(1/z) z^(-n-1) dz ds.

The contour is any positively oriented circle around zero. This formula keeps the entire exponential function and the complete s integration. Since

 L_m(1/z)=(z^2-4z+2)^(2m) z^(-4m),

its z phase, for fixed s, is

 s z+n log Q0(z)+2m log(z^2-4z+2)-(n+4m)log z.

The corresponding stationary equation is

 s+n Q0'(z)/Q0(z)+2m(2z-4)/(z^2-4z+2)-(n+4m)/z=0.

No first-tail-term replacement is used, and the integration endpoints s=0,1 must be retained in any subsequent asymptotic treatment.

## 4. A common meromorphic differential, but different cycles

Define

 G(w)=V(w)^n(2w^2-1)^(2m)/w^(n+1).

Then the two exact integrals are

 D=(-1)^n n!/(2pi i) contour G(w) dw,

 Flog=(-1)^(n+1)2n!/i integral_C G(w) dw.

The closed contour surrounds zero positively. The open path C runs from (1-i)/2 to (1+i)/2, stays to the right of zero, and may be the straight segment. Deformations must preserve its homotopy class relative to zero.

The factor (-1)^n in the denominator is essential. It follows by setting t=1-w in the coefficient formula at t=1. An earlier progress message omitted it; the corrected identity above is the one used here. The open contour follows from w=1-t and the reversal of the two endpoints.

The integrand is a rational function with its only finite pole at zero. The apparent logarithmic singularities introduced for phase analysis are zeros of the original integrand, not additional poles. The endpoints of C are roots of V. Exact endpoints contribute zero, but neighborhoods of them can contribute strongly when the saddle points approach them.

When D!=0, the logarithmic quotient is exactly

 Flog/D=-4pi (integral_C G)/(contour G).

This is only a conditional identity, not an estimate. Closed and open paths can have different saddle decompositions despite sharing the same phase.

## 5. Stationary equations in the large-degree regime

Put kappa=m/n. Away from zeros and zero, write

 Psi_kappa(w)=log V(w)-log w+2kappa log(2w^2-1),
 G(w)=exp(n Psi_kappa(w))/w.

The derivative is single-valued, regardless of local logarithm branches. Its stationary equation reduces to

 (4+16kappa)w^4-16kappa w^3+(8kappa-4)w^2+1=0.       (S)

This same quartic governs BOTH the denominator and the complete logarithmic residual. The contour coefficients, accessibility of saddles, and relative phases remain different.

As kappa tends to infinity, equation (S) has two small roots

 w=+/-i/sqrt(8kappa)+O(kappa^(-1)),

and one root near each of alpha=(1+i)/2 and its conjugate. Their expansions are

 w=alpha+1/(8kappa)+O(kappa^(-2)),
 w=conjugate(alpha)+1/(8kappa)+O(kappa^(-2)).

These expansions follow from the polynomial equation, by the scaling w=kappa^(-1/2)y at the small roots and a simple-root expansion at the other two. They are algebraic root locations, not claims that a particular contour integral is asymptotic to those roots.

At the small roots,

 Re Psi_kappa(w)=0.5 log(2kappa)-0.5+O(kappa^(-1/2)).

Indeed V(w)=1/2+O(kappa^(-1/2)), |w|=(8kappa)^(-1/2)(1+O(kappa^(-1/2))), and 2kappa log|1-2w^2|=1/2+O(kappa^(-1/2)).

At either endpoint-adjacent root,

 Re Psi_kappa(w)=kappa log 2-log kappa+O(1).

Here |V(w)| is of order kappa^(-1), |w| stays bounded away from zero, and |2w^2-1|=sqrt(2)(1+O(kappa^(-1))).

Thus for m=floor(rho n log n), fixed rho>0, the candidate saddle amplitudes, including the n! factor common to the two contractions, have logarithms

 small roots: n log n+0.5 n log log n+O_rho(n),
 endpoint-adjacent roots: (1+rho log 2)n log n
                         -n log log n+O_rho(n).

These are local phase budgets only. They show why the logarithmic-degree Gaussian theorem cannot be extrapolated. In particular the endpoint-adjacent phase is not negligible on the n log n scale. Whether it contributes on C, on the closed cycle, or cancels against another saddle must be established by a uniform contour argument.

## 6. Rigorous global budgets, without assuming saddle dominance

The finite denominator coefficient formula implies

 |C_n(m)|<=5^n 3^(2m),
 |D|<=n! 2^(-n)5^n 3^(2m).

Hence at m=floor(rho n log n),

 log |D|<= [1+2rho log 3]n log n+O_rho(n),

whenever D is nonzero. This is only an upper bound and cannot justify dividing by a saddle estimate.

From the complete real-arc formula, h(theta)=R cos theta-1 lies between zero and chi=R-1, and sin^2(theta)<=1/2. Therefore

 |Flog|<=pi n! 2^m chi^n,
 log |Flog|<= [1+rho log 2]n log n+O_rho(n).

This matches the endpoint-adjacent candidate leading scale at n log n precision but proves neither a lower bound nor a sign.

Using the complete exponential integral on |z|=R and the exact absolute selector sum

 sum_i |lambda_i| R^(-i)=(2(1+R))^(2m),

one obtains

 |Eexp|<=9(1+R)^n(2(1+R))^(2m)/(n+1).

In particular

 log |Eexp|<=2rho log(2(1+R))n log n+O_rho(n).

Unlike the logarithmic-degree regime, this majorant need not be negligible compared with a candidate denominator amplitude. It must remain in every complete-error budget. Further analysis could improve it, but no such improvement is asserted here.

## 7. Honest rational denominator upper bound

Let H=2n+4m and J=2^H H!. Then J clears every relevant fQ_i and fP_i, i<=4m. To see this, expand Q0^n and the differentiated cumulative Taylor series. Its factors are powers of two of exponent at most n, integer derivative factorial ratios, and either exponential denominators dividing H! or logarithmic coefficients whose denominators divide h*2^h. Since only h<=H occurs, the combined power of two is at most H: in a term with Q0 coefficient index s, its binary denominator exponent is at most s, and the cumulative index is 2n+i-s. Thus s+h<=H. This proves the asserted common clearer without identifying it as minimal.

When D!=0, both JD and J sum lambda_i fQ_i are integers. The actual reduced denominator q consequently satisfies

 q<=|JD|<=2^(H-n)H!n!5^n3^(2m).

For m=floor(rho n log n), this yields

 log q<=4rho n(log n)^2+O_rho(n log n log log n).

This upper bound is valid but too coarse for a certificate using only an exp(-c n log n) complete-error envelope. It is a limitation of this particular clearer bound, not a lower bound for q and not divergence of the primitive forms. No quotient estimate is used when D=0.

The main DIRECT_SELECTOR_HEIGHT_OBSTRUCTION_DRAFT.md was read. Its logarithmic-degree divergence conclusion is conditional on the preserved author saddle theorem. The present family has degree and logarithmic coefficient height of order n log n and lies outside that conclusion's low-degree regime. Leaving that regime is not an approximation gain. Neither the old obstruction nor the crude upper clearer above settles this family.

## 8. Precise remaining dominance problem

The reduction is effective in the following concrete sense: the denominator is a finite integer polynomial C_n(m), both logarithmic cycles integrate the same explicit rational G, all four stationary points are roots of the displayed quartic, and the competing local and global n log n budgets are specified. No unknown norm is offered as a substitute for these objects.

A completed asymptotic at fixed rho requires all of the following:

1. A deformation of the closed cycle around zero and the open cycle C into explicitly oriented paths through accessible roots of (S), with bounds on the remaining paths uniform for kappa=rho log n+O(1/n).
2. Explicit multipliers and phases for each conjugate pair. The denominator needs a lower bound for the resulting real signed sum; equal saddle magnitudes alone do not prevent cancellation.
3. Treatment of the endpoint-adjacent saddles at distance O(1/kappa) from the zeros of V. Merely declaring the endpoints zero omits their neighborhoods.
4. A complete exponential-contour estimate on the same denominator scale, retaining its s integration.
5. A reduced-denominator upper bound stronger than the displayed common clearer if the complete error is only exponentially small at n log n scale.

The exact obstruction to a quotient conclusion at present is denominator nonvanishing and quantitative signed dominance on the specified sequence, not the existence of unrestricted coordinates. The fixed-n polynomial exceptional-set result does not remove it. No explicit rho is currently certified to produce a useful complete primitive-error rate, and no rigorous all-rho exclusion of this selected family is proved.

This is a new saddle reduction with precise unresolved dominance, as permitted by the assignment. It preserves the old theorem and correction, does not repeat its proof or checks, and does not claim that saving these records closes the analytic gaps. Read-back of this file and LARGE_DEGREE_SADDLE_SELECTOR_REPORT.md remains required.
