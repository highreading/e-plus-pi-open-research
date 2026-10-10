> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Report: actual projection remainder

The exact Christoffel–Darboux subtraction gives

W/p_(n+1)=(v_n/h_n)(1-alpha_n p_n/p_(n+1))/(1-t),
V/p_(n+1)=-(p_n(1)/h_n)(1-b_n p_n/p_(n+1))/(1-t).

The Legendre-square identity proves v_n p_n(1)/h_n=theta_n with 1<=theta_n<=2. Thus the ratio of the scalar magnitudes is exactly epsilon_n=|v_n|/p_n(1), rather than a large coefficient majorant.

On |t|<=1/20, valid explicit bounds are

M_W^sharp=(740/513)theta_n/p_n(1),
M_V^sharp=(1340/513)p_n(1)/|h_n|,
M_W^sharp/M_V^sharp=(37/67)epsilon_n.

A direct argument also proves |W(t)/V(t)|<=epsilon_n on this disk. Its denominator is controlled by an actual lower bound, not by division of upper bounds. The reference functions are nonzero there; no determinant nonvanishing follows.

Writing s=(sqrt(2)-1)^2 and tau=-log s, the paper proof establishes, for n>=1,

2 exp(-s)s^n<=epsilon_n<=8s^n/(1-s)^2.

The Gaussian determinant bounds therefore improve to

|D_W+T|<=B_V^sharp(37/67)epsilon_n(1+Xi),

where Xi=B_T^sharp/B_W^sharp has an exact positive formula. For b=floor(n/2), R=lambda n,

log Xi=-(3/2)n log n+O_lambda(n).

An explicit inequality for R=n and n>=40 is given in the proof. T is retained in full. Smallness of its bound relative to B_W^sharp does not establish smallness relative to the actual D_W.

The old obstruction B_W>4B_V is removed for these new bounds. Their full numerator-to-endpoint-bound ratio has logarithm -tau n+O(1). The actual primitive bound still contains

delta_n^sharp=log q+log(B_V^sharp/|D_V|)>=0.

The remaining sufficient target is delta_n^sharp-tau n tending to minus infinity, with D_V!=0 and D_W+T!=0 on the same unbounded index set. Neither this loss estimate nor the required growing-degree nonvanishing is proved. In particular, the scalar improvement does not justify extrapolating the fixed-b factor (sqrt(2)-1)^b.

The leading cofactor exponent -n^2 log n/2 is unchanged. Consequently the corrected ceiling limsup log g/(n^2 log n)<=3/4 still holds for the previously audited clearer; its strict 3/4 content target remains impossible. The new question concerns the additive O(n) gap log(M B_V^sharp)-log g, not a larger leading content coefficient.

Exact dependencies and all proofs are in ACTUAL_PROJECTION_REMAINDER.md. They use the September 13 Legendre/CD/second-kind identities, the exact reference identities in the September 27 fixed-degree note, the corrected functional domains, and Agent 3's Gaussian bound. No fixed-b determinant asymptotic is used. The endpoint-clearer interpretation uses the completed GROWING_CONTENT_CRITERION_REVIEW.md.

No new computations, degree or prime scans, networking, or edits outside Agent 2's directory were performed. Prior corrections and certificates are preserved. The two newly saved documents must be read back before this continuation is declared complete.
