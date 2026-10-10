> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Growing-degree determinant domain correction

The current proof and report incorporate the minimal repair requested in ../agent3/GROWING_DEGREE_INDEPENDENT_REVIEW.md, Section 2.

The original Section 3 phrase "for every positive integer d" overstated the domain. Section 1 defines only ell_j(t^k)=1/(n+k+1-j)! for 0<=j<=b. A contour expression does not by itself extend that definition.

A difference determinant has columns D_j=ell_(j+1)-ell_j for j=0,...,d-1 and therefore requires ell_0 through ell_d. Its corrected scope is 1<=d<=b. An ordinary determinant has columns ell_j for j=0,...,d-1 and requires ell_0 through ell_(d-1). Its corrected scope is 1<=d<=b+1.

The endpoint determinants D_V and D_W reduce by adjacent column differences to d=b difference determinants. The complete companion determinant T is an ordinary determinant with d=b+1. Both use largest functional index b. For every Taylor index k>=0, n+k+1-j>=n+1-b>=1. In particular this holds for n>=2 and b=floor(n/2), and throughout the underlying domain 1<=b<=n.

The contour identities and the bound C_G E_n(R)^d J_d(R)/d! retain all their factors. The ordinary version still replaces E_n(R) by E_n(R)/(R+1). The cancellation orders remain b(b-1)/2 for the endpoint difference determinants and b(b+1)/2 for T. No reciprocal-Gamma extension of the functionals is introduced; the Gamma factors already present in the Gaussian integral bound are unchanged.

PROOF_DRAFT.md now states the permitted indices in the contour formula and the two determinant ranges in the bound. REPORT.md records the same correction. Existing finite certificates and their checker are preserved, with no new degree computation or scan.

This scope repair supplies no determinant lower bound, remainder nonvanishing theorem, or reduced-denominator estimate. Those gaps and the conditional primitive-form criterion remain unchanged. The interrupted b=2 audit is not completed by this correction.
