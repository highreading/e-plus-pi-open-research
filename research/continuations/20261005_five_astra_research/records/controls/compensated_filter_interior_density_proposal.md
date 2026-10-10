> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Coordinator proposal: an actual lower rate near the negative support endpoint

Status: a proposed mechanism, requiring independent derivation. Reuse A3 turn5's
proved exact moment representation and complete exponential bound. Do not infer
a lower bound from the support or from its upper bound. Standard Laplace/Watson
methods are existing tools (https://dlmf.nist.gov/2.3), not novel results.

Let Z_k^ar=sum_(h=0)^4 k^h integral T^k dmu_h(T), supported on [-r,2rho].
For the binomial transform, its exact kernel is g(T)=T^n(5+T)^m and
Euler derivatives D^h g, D=T d/dT. At the interior maximizing negative
saddle T_c=-5/(1+c), Dg/g vanishes to first order. Thus positivity or
nonvanishing of mu_4 alone does NOT certify a surviving transformed amplitude.
Move the derivatives by parts on a smooth interior localization. The relevant
effective density is

 F(T)=sum_(h=0)^4 (D*)^h f_h(T), D* f=-(Tf)',

where f_h are the ACTUAL pushforward densities. Prove their local regularity;
control cutoff/boundary terms separately. Do not silently treat singular
endpoint densities as globally integrable after repeated derivatives.

The corner giving T=-r has theta_1=theta_2=0 and Heine variable v=0, with
three quadratic deviations. Write a=v_circle+1 and beta=sqrt(2-a^2). The
conditional real circle weights are

 w0=e^a cos(beta)>0,
 w1=e^a(a cos(beta)-beta sin(beta)),
 w2=Re((a+i beta)^2 exp(a+i beta)).

All are analytic in the quadratic corner coordinates. The highest-degree
contraction has symmetric weight

 (1/2)(v1-v2) w0(v1)w0(v2) [q(v2)-q(v1)],
 q(v)=a-beta tan(beta).

This vanishes to fourth order in the two angular corner coordinates, not
merely to second order. Hence the candidate f4 near -r is O((T+r)^(5/2)).
Derive this and all other local powers from the actual product integrals.

For the degree-three coefficient, use the exact A3 formulas. If
 F0=B0 A1-B1 A0,
 G0=B0 A0-B1 A0+B1 A1-B2 A0,
then C_k/(k!)^2=k^2 F0+k(F0+G0)+G0.
The coefficient of k^3 in t^2 C_k/(k!)^2 is 3F0+G0.
The degree-three coefficient in S_k/(k!)^2 is B0^2.
At the corner v1=v2=-M,u=-2rho,z1=z2=-sqrt(2), the weight of mu3 relative
to positive circle/Heine product measure is therefore proposed to be

 u(-M)(1+sqrt(2))-2M^2=2M-2M^2=-2sqrt(2)M !=0.

Thus f3 should have a nonzero (T+r)^(1/2) leading term. Its third adjoint
Euler derivative has order (T+r)^(-5/2), dominating f4's fourth derivative
of order (T+r)^(-3/2), and also the lower-degree terms. If every exact
coefficient and corner-density statement passes, F(T) is nonzero on some
open interval (-r,-r+epsilon). The endpoint expansion could give a paper
existence theorem for such epsilon without a numerical scan.

Choose c just above c0=5/r-1, so T_c lies in that interval and the negative
interior saddle strictly dominates the positive branch. A localized Laplace
calculation would then give a genuine nonzero complete transformed asymptotic
with finite exponential rate, including the already factorial-small exp part.
Make parity signs explicit. For integer m/n approaching this c, the entire
real numerator cannot be assigned a lower bound until this amplitude is proved.

If successful, on the already proved admissible odd primorial indices N_x,
choose n=floor(N_x/(1+c)),m=N_x-n. A3's exact denominator lower bound
log q>=2N_x log log N_x(1+o(1)) would dominate any finite exponential decay.
This yields a rigorous EXCLUSION OF THIS FILTERED PRIMORIAL SUBFAMILY, not
a statement about all filtered indices, and not a decision on e+pi.
Only claim that exclusion after proving the COMPLETE signed lower rate.
