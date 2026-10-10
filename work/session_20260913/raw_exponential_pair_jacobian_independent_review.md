> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: exponential-pair Jacobian and the pole pairing

Date: 2026-09-13. Reviewer: audit_results.

**Verdict: PASS, all six sections.** No mathematical correction is needed. The note gives an exact remaining Jacobian determinant and a valid obstruction to two attempted shortcuts. It does not prove that the exponential pair is étale at actual four-equation roots.

Reviewed source: `raw_exponential_pair_jacobian_and_pole_pairing.md`. Dependencies checked directly: the exact operator and cofactor normalization in `raw_extremal_four_accessory_equations.md`, and the pole Wronskian and rational factorization in `literature_accessory_heine_stieltjes_and_pole_identity.md`. The latter literature claims are not re-reviewed here.

## 1. Exact square determinant and cokernel

The parameter derivatives of P=L^[1] are exactly z(partial+1)-d and partial+1. With the source's descending monomial column order and descending coefficient row order, the upper d-by-d block T has diagonal -1,-2,...,-d. Its determinant is (-1)^d d!, and its inverse exists over Z[1/d!] and every permitted residue ring.

Differentiating the upper equations for the monic B gives the upper elimination coefficients -T^(-1)U_top and -T^(-1)V_top. The resulting lower 2-by-2 Schur complement is the matrix of parameter derivatives of ([z]PB,[1]PB), in that order. Each row of the displayed E Jacobian is multiplied by d!, so the determinant of the Schur complement is J_d/(d!)^2. Therefore

    det W_d=(-1)^d J_d/d!,
    J_d=(-1)^d d! det W_d.

The sign and the single surviving factorial are correct. This identity holds for all parameters, not just on E_1=E_0=0. The injectivity of P on degree <=d-1 follows from the nonzero highest coefficient m-d; hence its cokernel in degree <=d+1 has dimension two. The source's two normalized elimination functionals are exactly a basis of that cokernel. The determinant in (4) has the correct row order and factor (d!)^2.

I independently expanded P(z^m) in the five powers z^(m+2),...,z^(m-2), symbolically for arbitrary m,d,beta,gamma. Every coefficient in recurrence (5) agrees. Its forward pivots d-m, 0<=m<d, are units in the stated rings. Injectivity alone supplies neither the nonzero determinant nor a unit determinant of the two parameter directions.

## 2. Adjoint normalization and finite jets

Write the rational monic factorization as L/(zD)=A_1 A_2, with

    A_1=partial-s/z+2D'/D+J'/J.

The function g=D^2J/z^s has logarithmic derivative -s/z+2D'/D+J'/J, so A_1^dagger g=0. Taking the adjoint of L=(zD)A_1 A_2 reverses the order. Consequently f=g/(zD)=DJ/z^(s+1) satisfies L^dagger f=0. Both the power of z and the D factor in (7) are correct; J is nonzero for the actual pair.

For the actual normalized triple put M=s+2=3d+4. The finite exponential and arctangent jets through M-1 are defined whenever p>3d+3, including p=M. Their derivative errors relative to E_T and 1/D begin in degree M-1. Therefore, writing U_T=BE_T and R_T=A+U_T+CF_T=O(z^M), one obtains

    E_T DJ = D(CU_T'-C'U_T) mod z^(M-1)
            = D(AC'-A'C)-C^2 mod z^(M-1).

The term D(CR_T'-C'R_T) starts in degree M-1 or later; multiplication by polynomials does not lower its order. This argument divides by no coefficient of degree M and uses no characteristic-p infinite exponential. If p=M causes the derivative of a leading remainder term to vanish, its order only improves.

The Wronskian AC'-A'C has degree <=2d-2. If both degrees are d, the leading terms cancel; otherwise their degree sum is <=2d-1 before differentiation. Thus K=D(AC'-A'C)-C^2 has degree <=2d. For f of degree <=d+1, every coefficient of K that could contribute to [z^s]Kf has index at least s-(d+1)=2d+1 and is zero. The congruence retains precisely all required coefficients through s. It follows that Lambda is identically zero on the entire cokernel test space, as claimed.

The pole identity itself has the correct sign and normalization: reducing the cleared determinant modulo D gives N=CD'J modulo D, and N=kappa z^s gives CJ=(kappa/2)z^(s-1) in R[z]/(D). Taking its rank-two determinant norm yields 4 Res(D,C)Res(D,J)=kappa^2, without dividing by polynomial content. These units do not repair the zero functional just proved.

## 3. Single exact counterexample certificate

An independent control was written as `exponential_pair_jacobian_independent_checks.py`, with output `exponential_pair_jacobian_independent_checks.json`. It uses the universal operator coefficient identity and only the predeclared symbolic degree d=2 and prime p=751. It does not construct further actual degrees or scan primes.

The control independently solves the two upper equations for monic B, constructs E_1,E_0, and verifies the symbolic determinant identity. It checks the displayed beta eliminant, its exact discriminant 2^19*3^6*751*318737, primality of 751, and gcd(f,f')=beta-30 modulo 751. It then verifies every stated field quantity:

    (beta,gamma)=(30,15),
    Jac E=[[55,72],[214,444]],
    B=z^2+20z-151,
    C*=-328z^2-14z+68,
    (Res(D,C*),Res(D,J*))=(53,124),
    residue remainder=257+193z.

The Jacobian determinant is 12*751, and the tangent vector (72,-55), dot B=72z+358 satisfies the actual inhomogeneous tangent equation modulo 751. Also 4*53*124=3 modulo 751 and 3 is a nonsquare there.

This is therefore a valid counterexample to the weaker assertion consisting only of the exponential equations plus the two pole units. It is explicitly not a root of the two residue equations, and does not satisfy the stronger actual norm identity with a unit kappa. It supplies no counterexample to the actual étaleness question.

## 4. Conditional improvement of norm content

Suppose the actual residue point exists and the specific E_1,E_0 Jacobian is a unit there. The finite free exponential algebra has a local factor with residue algebra F_p and invertible Jacobian. Its completed factor is finite étale over Z_p with residue field F_p, hence is Z_p itself. Thus it has no hidden multiplicity or ramified branch at that point.

On this factor the residue equations become scalars rho_0,rho_1 with min(v_p rho_0,v_p rho_1)=f, by the already proved full quotient Z_p/(p^f). It contributes rho_0+t rho_1 to the norm polynomial. Every other local factor has no simultaneous residue zero modulo its maximal ideal. Over the algebraic closure of the residue field, its determinant norm reduces to a product of nonzero linear polynomials, counted with local lengths; this product is nonzero even when the factor is nonreduced. Hence its Gauss content is a unit. Additivity of polynomial Gauss valuation gives exact norm-content valuation f.

The argument correctly requires the particular two-row unit hypothesis. The previously proved rank-two four-row Jacobian does not imply it, and finite freeness alone does not imply it either. Exact norm-content equality would still not bound f or the Archimedean height of the carrier.

## 5. Scope

The all-index identities, finite-characteristic boundary argument and conditional norm statement pass. The extra exact computation checks one stated counterexample and is not evidence for or against an all-index actual unit theorem. The remaining mathematical task is to use both actual residue equations to prove the specific cokernel determinant is a unit, or to find an actual counterexample. No conclusion concerning rationality or irrationality of e+pi follows here.
