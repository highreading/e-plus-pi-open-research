> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Corrected fourth-integral-jet omission ceiling: radius below 2.70

Root original deduction,2026-10-02. Author proof with exact rational Schur-tree certificate. The earlier2.66 claim in this working note was invalid and is withdrawn. The third-jet2.809621359339520 theorem is unaffected. The main irrationality problem remains open and research is active.

## Correction and exact theorem

Under the endpoint-fixing, real-coefficient and omitted-value assumptions of the preceding notes, integrality of the first four derivatives forces R<27/10=2.70. Every larger disk is excluded by restriction to that rational disk.

The correction is algebraic. For r=xi''/xi' and the Schwarzian S,

    r'=S+(1/2)r^2,
    xi'''/xi'=S+(3/2)r^2,
    xi''''/xi'=S'+4rS+3r^3.

The previous manual formula used3rS instead of4rS. Hence the correct fourth normalized derivative is

    zeta=a xi''''(0)=-3/4-ell+3ell^3.

The earlier2.66 certificate only certified inequalities using the incorrect input and cannot establish an omission ceiling. It has been replaced by a corrected exact tree, and the reproduction script now uses the Riccati recurrence directly.

## Proof by exhaustive necessary interpolation

Let f be the real-path lift, with f(0)=0,f(1)=t. Put h(z)=f(Rz)=z g(z),s=1/R. At each stage, the Schur function has real constant b and prescribed value T at s. Schwarz-Pick gives the necessary parameter interval

    (T-s)/(1-sT) <= b <= (T+s)/(1+sT).

The kth constant depends affinely on the new integer derivative j_k:

    b=b0+F j_k,
    F=R^k/[a k! product_(earlier b)(1-b^2)] >0.

The full lower-derivative contribution b0 is obtained by exact formal composition of xi with the previous jets and k-1 Schur divisions. All possible integers in this interval are enumerated; every branch is either excluded by a strict necessary inequality or continued with endpoint(T-b)/(s(1-bT)). This leaves successive frontier sizes1,1,2,0 at R=2.70. Thus all first-four-derivative choices are exhausted.

The exact rational enclosures for a,t,ell come from SECOND_JET_RADIUS_CERTIFICATE.json. The inverse-coordinate coefficients are generated from the exact rational Schwarzian by the Riccati recurrence, then xi'=exp(integral r)/a. Every operation is rounded outward on a rational grid10^-40. No numerical root or floating-point decision is used. FOURTH_JET_RADIUS_CERTIFICATE.json retains every node, candidate interval and endpoint inequality, including branches pruned by an empty integer interval.

## Prior work and scope

Archive searches for four-jet Schur/interpolation omission ceilings found earlier constructions and moment jets, but no completed theorem of this scope. Fresh primary reads were Abate's iterated hyperbolic-difference-quotient paper and Waldschmidt's Hurwitz-function survey. This is an application of their standard framework, not a new general Schur theorem.

The archive's strongest located lower construction has radius>1.7679119, from nonpolynomial_integral_hurwitz_pullback.md. It is compatible with this upper bound. Integrality of further derivatives can impose additional constraints; the fifth-jet exact tree in the current session gives2.68. None of these analytic bounds alone controls a primitive denominator or settles e+pi.
