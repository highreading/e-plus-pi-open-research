> Archived research record. Read the [current proof status](../../../../../docs/PROJECT_STATE.md) and [errata](../../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Coordinator proposal: resolve the actual compensated signed filter by real moments

Status: a proposed proof mechanism for independent derivation and audit. The
identities below must be checked against the original raw b=2 normalization.
No primitive shrinking or irrationality conclusion is asserted.

The archive's ADAPTIVE_ARC_INVERSE_DRAFT already uses the exact circle symbol
(1+sqrt(2) cos(theta))^n exp(-sqrt(2) exp(i theta)). Reuse that known identity.
RATIONAL_INDEX_FILTERS treats a different B-only b=3 center with fixed-order
filters. A bounded archive/literature overlap gate did not locate the following
complete raw b=2 proportional-order filter calculation. This is not a universal
novelty claim. Standard Legendre Laplace/Heine integral representations are
existing tools, not new results: https://dlmf.nist.gov/18.10.E5 and
https://dlmf.nist.gov/14.25.E2. The latter is for Olver's Q; translate its
normalization and branch before using standard Q_n.

## 1. Known circle representation, used at all finite jet orders

Let phi(z)=1-z+z^2/2, M=1+sqrt(2), rho=sqrt(2)-1=1/M,
H_k(x)=k![z^k] exp(xz) phi(z)^k. On z=-sqrt(2) exp(i theta),

 H_k^(d)(1)/k! = (1/(2 pi)) integral_0^(2 pi)
                     z^d exp(z) [phi(z)/z]^k dtheta,
 phi(z)/z=-1-sqrt(2) cos(theta) in [-M,rho].

The d=0 real weight exp(-sqrt(2)cos(theta)) cos(sqrt(2)sin(theta))
is positive. Higher fixed-d weights are bounded and need not be positive.
Adjacent index shifts and J_k,K_k are fixed-degree polynomial amplitudes
in k multiplying real moments on this same support.

## 2. Retain the correct second-kind sign and both exponential pieces

Use EXACTLY the old contiguous raw S_k,C_k,W_k, Dcal_k and V_k:
 t=k+1, f_k=2^k/(k!)^2,
 Dcal_k=t^2 L_(k+1)(1) C_k-2 L_k(1) S_k,
 Q_k=2 w_k S_k-t^2 w_(k+1) C_k,
 V_k=Acal_k S_k-t Bcal_k C_k-H_(k+1)(1) W_k.
Thus compensated Z_k=(Q_k+2 f_k V_k+(e+pi)Dcal_k)/(k!)^2.

Set epsilon_k=pi L_k(1)-w_k and E_k=e L_k(1)-T_k(L_k).
The full decomposition is

 Z_k = [t^2 C_k epsilon_(k+1)-2 S_k epsilon_k]/(k!)^2
       +[t^2 C_k E_(k+1)-2 S_k E_k
                              -2 f_k H_(k+1)(1) W_k]/(k!)^2.

In particular it is pi L_k(1) MINUS w_k. At k=0,epsilon_0=pi;
at k=1,epsilon_1=2pi-8<0. A sign reversal destroys this calculation.
The following candidate exact Heine expression passes those two checks:

 epsilon_k=4(-2)^k integral_0^infinity
                         (1+sqrt(2)cosh(t))^(-k-1) dt.

Independently prove its branch/normalization. Its real moment base is in
[-2rho,0], with a finite measure (dt/(1+sqrt(2)cosh(t))).

For Fcal_k(x)=x^k H_k(x), the exact Laplace transform should give
 integral_0^infinity exp(-x) Fcal_k(x) dx=(k!)^2 2^(-k)L_k(1),
 T_k(L_k)=f_k Acal_k, T_k(L_(k+1))=2f_k Bcal_k/t,
 E_k=e f_k integral_0^1 exp(-x) Fcal_k(x) dx.

This yields a UNIFORM factorial-small bound on the SECOND line, including
the final H_(k+1)W_k term. Derive all polynomial powers and constants needed;
do not omit that endpoint term or call it an arctangent remainder.

## 3. Candidate full proportional-order bound

The first line is a finite sum of real moments T^k with bounded signed
weights and polynomial-in-k amplitudes of fixed degree. Product supports
should put T in [-2M,2rho]: two jet bases in [-M,rho], times a second-kind
base in [-2rho,0]. Let r=2M, d=2M^3=14+10sqrt(2).

For weights binom(m,j) 5^(m-j), perform the binomial transform on the EXACT
moment expression. Polynomial amplitudes are handled by a fixed number of
Euler derivatives, with 5+T>0 throughout the support. A proposed uniform
bound is

 |sum_j binom(m,j)5^(m-j) Z_(n+j)|
 <= C (n+m)^D max_{T in [-r,2rho]} |T|^n(5+T)^m
       + a uniformly factorial-small complete exponential part.

On m/n -> c>0, the inherited one-sign J_k and ratio J_(k+1)/J_k ->d
give a denominator lower bound at (5+d)^m d^n up to subexponential factors.
Hence, if all exact decompositions above pass, the complete center error
has proposed exponent

 limsup (1/n) log|S-center|
 <= log(max_{T in [-r,2rho]} |T|(5+T)^c)-log d-c log(5+d).

The negative branch is max_{0<=x<=r} x(5-x)^c; its maximizer is
min(r,5/(1+c)). The positive endpoint 2rho(5+2rho)^c MUST also be retained.
Do not replace the whole support by its original dominant negative endpoint.
Compare this rate with the unfiltered error at the SAME N=n+m.

This is an analytic task distinct from final-gcd control. Even a genuine
improvement here does not prove primitive shrinking: q has only a large
factorial upper bound and the new p|N theorem supplies lower bounds.
The coordinator's separate primorial corollary strengthens that lower bound
on some indices, but cannot be used as an upper bound or as an exclusion
without a complete real lower bound for the transformed numerator.
