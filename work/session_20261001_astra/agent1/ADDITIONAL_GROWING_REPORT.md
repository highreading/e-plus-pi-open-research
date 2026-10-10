> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Agent 1: additional growing-content report

Status: algebraic deliverable completed on paper; twelve symbolic checks passed. Independent review pending. Existing growing arithmetic, normalized seeds, and correction were preserved.

A_b^2 is already a divisor of Gamma=Crows*mu. It must not be added to that content again. After deleting columns i<j, with m=b-1, the exact factorial-normalized minor is

    det R_(omit i,j)/A_b^2
      = [m!(m+1)!/(i!j!)] det Z_(omit i,j),

where Z_lj=binom(l+j-1,j) E_(n+l,l+j-1)/(l+j-1)! is integral.

The new structural result is an all-size integral reduction of the ACTUAL high block. Its columns satisfy

    R_(j+4)=2(n-j)R_(j+3)
      -(n-j)(n-j+3)R_(j+2)
      +2(n-j)(n-j+2)R_(j+1)
      +2[Lambda+j(2n+1-j)I]R_j,

with Lambda_ll=l(l+2n+1). Consequently an integer unitriangular column transformation replaces column 4q+s by

    (2Lambda)^q R_s, 0<=s<4.

It preserves the complete maximal-minor ideal, including after all coordinates are divided by A_b^2.

Every maximal minor of this transformed block has an explicit four-group Vandermonde expansion. Since only two columns are deleted, each group has at most two missing powers. The correction factors are elementary symmetric polynomials, or a two-by-two determinant of them. Thus the residual content is reduced to four actual starting-column weights and explicit partition sums with pair factors

    lambda_v-lambda_u=(v-u)(2n+1+u+v).

The proof also supplies an integral recurrence for theta_(k,r)=E_(k,r)/r!, allowing the factorial-normalized entries to be generated directly. No further divisor with a positive n^2 log n rate is proved. Divisibility of a complete partition sum must not be inferred from the sizes of its individual terms.

The exact endpoint-scale translation is retained. For F=(2n+1)!, f=2^n/(n!)^2, and the complete starred endpoint expressions from the earlier reduction, let

    N0=fF^2[Q*+2fV*], Z0=fF^2 D*,
    g0=gcd(|N0|,|Z0|).

These are integer endpoint coordinates. If d is the previously defined three-contraction content and gamma=Gamma/A_b^2, then in the main-agent monic clearer scale,

    g=Gamma*d*g0,
    g/A_b^2=gamma*d*g0,
    q=|Z0|/g0.

Both second-kind terms and both partial-exponential contractions remain in Q*+2fV*. The formulas assume Y!=0; no growing-degree nonvanishing is established.

The former strict residual target above one half is withdrawn. The completed [content correction](../agent2/GROWING_CONTENT_CORRECTION_SUMMARY.md) proves limsup log(g/A_b^2)/(n^2 log n)<=1/2 on unbounded nonzero-endpoint sets with b=floor(n/2), so a strict liminf above that ceiling is impossible. The identity g/A_b^2=gamma*d*g0 and all structural results remain valid. [Agent 4's additional review](../agent4/ADDITIONAL_GROWING_REVIEW.md) passes those arguments with this documentation repair. This conclusion concerns the stated normalization and bounds, not actual-family divergence or failure of all alternative estimates. The known n+l row factors have only O(n log n) weight and overlap the existing content.

Evidence: the final symbolic execution passed all twelve checks with exit code 0 and sandboxed=true. An initial simplification failure in two differential identities was resolved by specifying their intended domain; no mathematical formula changed. Twelve abstract columns were checked, with no actual degree or prime evaluation. The all-size and minor-expansion statements have separate written proofs.

Files:

- ADDITIONAL_GROWING_CONTENT.md: full reconciliation, integral recurrences, structured minor formula, endpoint-gcd translation, and scope.
- check_additional_growing_content.py: reproducible symbolic checks.
- additional_growing_content_certificate.json: successful certificate.
- ADDITIONAL_GROWING_REPORT.md: this report.

Next attainable lemma: prove a common divisor or controlled cancellation statement for the actual four-group weighted Vandermonde sums after factorial normalization. No independent review, combined analytic-criterion approval, or irrationality result is claimed.
