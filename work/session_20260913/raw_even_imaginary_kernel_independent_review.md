> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: the even imaginary saddle kernel

Date: 2026-09-13. Reviewer: audit_results.
Target: raw_even_imaginary_saddle_kernel_tail.md.
Verdict: PASS. No correction required.

I independently checked the positive imaginary-axis recurrence and all
normalizations. The coefficient square increases with j and remains below
3/4. The lower single-step bound 2/sqrt(15) is uniform.

The split proof of two-step growth also checks. For 2<=j<=9 the
m=20 majorant is 82/455 and its reciprocal contribution is 91/82>11/10.
For j>=10 the adjacent square ratio is at least 41/50; adding the
4/15 term makes the stated bound strictly stronger than 11/10.
Consequently the reversed-ratio bound holds at every index, not merely
in a fixed upper window.

The limiting two-step map has derivative at most (15/19)^2 on the
stated lower-bounded interval. The finite-window comparison is uniform
over starting states in a compact interval, so the order of the two
limits is justified and does not assume convergence at the lower edge.

Finally, the geometric bound permits dominated summation of the squared
ratios, with limiting total 5/2. The Riesz vector really has coordinates
conjugate(q_j(-i/sqrt(5))); after reversing and multiplying by (-i)^m
the resulting profile is sqrt(2/5)(-i sqrt(3/5))^r. The evaluation row
therefore has conjugate phase, as stated. The all-m extension and its
tail sum have the correct floors and the factor 2.

This is a normalized scalar-kernel theorem. The original polynomial
evaluation still needs its common Cayley scalar, the component
combination (1,-phi), the endpoint solution normalization and the
monic comparison phase; these are handled separately in
raw_even_saddle_multiplier_limit.md.

