> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact generating-function convention for the joint-force note

The first paragraph of COORDINATOR_JOINT_BINARY_LOG_FORCE_GUARD.md contains a notation error: the source L_m is m![z^m](F(z)/(1-z)), not m![z^m](e^z F(z)). This correction is required by the complete contact excerpt, equations7/8, and the exact recurrence L_m=m L_(m-1)+g_m. The earlier source packet and its SHA remain preserved; this addendum records the correction explicitly.

All subsequent coefficient identities and the proof in that note use the CORRECT convention:

    L_m = sum_(r=1)^m (m!/r!)g_r.

That is the coefficient formula for F/(1-z). It is not the e^z convolution, whose binomial weights would differ. The former formula implies the displayed paid bound

    v2(L_m)>=floor(m/2)+2-s2(m)-floor(log2m),

and hence the joint whole-source estimate n+floor(i/2)-3ell. The actual complete source, its factorial payment and the final4b! division therefore retain the intended proof, once the first paragraph is corrected. Do not adopt the false e^z coefficient identification or regard the addendum as a changed source.

Independent auditors should explicitly check this convention against the supplied COMPLETE_CONTACT_FORCE_SOURCE_EXCERPT.md. No computation or whole-error claim is introduced by this correction.
