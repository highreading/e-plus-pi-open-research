> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: Ordinary Padé error prefactor and conditional fixed-b shrinking criterion

Reviewer: worker_2
Verdict: approved
Candidate SHA256: e2b926b3f2d184f5cd501ef88d3031968ab3a8fb0bbce0fd456292ef52991aa3

Approved for the exact scoped statement. The prior read-only hash computation verified that the candidate payload has the registered SHA-256 e2b926b3f2d184f5cd501ef88d3031968ab3a8fb0bbce0fd456292ef52991aa3. The whole Markdown file has hash 4c32cac01e95eef84f72a863aaf6bef7dcd8245e762852d52a2a2c50b3b520bf because it includes registry headers; this is not a content-identity discrepancy.

I independently derived the ordinary Padé normalization from the original moment and Rodrigues formulas, checked the sign, justified the generating-function coefficient limit with tail domination, and checked the Legendre probability-measure limit. These calculations establish, with rho=1+sqrt(2), epsilon_n=(4*pi/rho)*rho^(-2*n)*(1+o(1)). The exact candidate agrees with my independent derivation in work/astra_20260929/worker_2/note_000009.md. The constant is nonzero, so the asserted eventual nonvanishing follows; this does not certify every initial index.

For each fixed integer b>=1, the candidate correctly identifies work/session_20260927/fixed_exponential_degree_error_theorem.md as a separate dependency. Applying its stated transfer ratio gives R(1)/Y=(-1)^n*(4*pi/rho^(b+1))*rho^(-2*n)*(1+o(1)). I checked the transfer theorem's statement, normalization and applicability, but did not independently re-audit its determinant proof. Approval of this matched-family consequence is explicitly conditional on that theorem and its hypotheses, including the endpoint nonvanishing needed to form the ratio. No uniform assertion for growing b is approved.

With q_n the positive actual reduced denominator of A(1)/Y, the nonzero fixed leading constant makes |q_n R(1)/Y| tending to zero equivalent to q_n/rho^(2*n) tending to zero along any unbounded admissible subsequence. This checks an equivalence, not the existence of such a subsequence. No bound on the actual denominators, successful shrinking subsequence, or conclusion about the irrationality of e+pi is established by this review.