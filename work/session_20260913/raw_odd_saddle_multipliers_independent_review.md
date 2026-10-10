> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the actual odd saddle multipliers

Date: 2026-09-13. Reviewer: audit_sources. **FULL PASS.**

Audited in full: raw_odd_saddle_multiplier_limits.md,
check_raw_odd_saddle_multipliers.py, and its saved output
raw_odd_saddle_multiplier_certificate.json. The final postprocessor,
including its added checks against the old solved-vector error intervals,
was rerun unchanged and returned PASS.

No new inverse witness, quadrature, canonical degree, or unverified
floating solution was used in this audit.

## 1. Actual reference and full odd operator

The reference uses a=m+1, the positive metric exponent 2m+2, and
the full two-component degree-m space. Its exact beta is 2m+2.
The polynomial F has degree n-1, while its degree-n reversal
Psi=(-1)^m z Phi_m(-z^2) is monic. The original coefficient maps
P_1(i)/2^m and P_2(-i)/2^m have positive factors; the latter is in
component two. Both unit Riesz polynomials are correctly normalized by
sqrt(c_m).

These normalization facts were independently derived in
raw_odd_hardy_reference_and_reversal_framework.md, which now has
the independent PASS raw_odd_hardy_framework_independent_review.md.
That framework does not use either this amplitude theorem or the new
contour assembly, so the dependency is not circular.

The full odd solution uses



$$
x=Qv-QU(I+VQU)^{-1}VQv,
$$



with the previously certified rank-two perturbation. The order of
Q=(A_0E)^(-1), the Woodbury sign, and the three old witness columns
are correct. The finite strong inverse convergence combined with norm
convergence of the boundary maps proves x_m->x in Hilbert norm.
The scalar g=v*x=1/s_infty is negative, and the proof never invokes
even-family positivity or a missing-channel constraint.

## 2. Actual beta=2m+2 kernel tail

For j<=m, the exact coefficient



$$
\alpha_j=\frac{j(2\beta-j)}{4(\beta-j)^2-1}
$$



is increasing and strictly below 3/4. Its fixed final windows tend to
3/4. The real-variable identity and derivative in the source are exact:



$$
\alpha(j)=\frac{\beta^2-1/4}{4(\beta-j)^2-1}-\frac14,
\qquad
 \alpha'(j)=
 \frac{8(\beta^2-1/4)(\beta-j)}
 {[4(\beta-j)^2-1]^2}.
$$



The derivative is maximized at j=m. With u=m+2 and beta<2u,
the upper bound 32/(9u)<4/(m+1) follows.

At -id, the monic recurrence has positive coefficients:
D_j=dD_(j-1)+alpha_(j-1)D_(j-2).
The possible ratios stay in [d,d+3/(4d)]. The limiting two-step
map has the stated strict contraction on this interval. Comparing a
fixed final window and then increasing its length is valid without
assuming any limit for its lower initial state.

The orthonormal two-step lower bound is also exact. The denominator
sqrt(alpha_j alpha_(j-1)) is both at most
alpha_(j-1)+2/(m+1) and strictly below 3/4. Under the stated threshold
m+1>=4/d^2, the numerator exceeds it by at least d^2/2. This proves
the claimed growth factor 1+2d^2/3. The remaining single step is at
most sqrt(3)/(2d) in the reverse direction.

These estimates control every reversed coefficient, not just a fixed
window. The resulting geometric majorant justifies norm convergence
after normalization, including the stated phases:



$$
\ell_{\pm,d}(r)=\sqrt{1-q(d)^2}(\pm i q(d))^r.
$$



The endpoint case d=1 and the interior plus case are consistent with
the independently known endpoint vector and complex conjugation.

## 3. Exact finite evaluation and phase

The interior ratio pairs matching plus-i phase vectors, leaving no
alternation. In the exterior ratio the actual solution has phase i^m
and the reference has phase (-i)^m, leaving exactly (-1)^m.
The reference is in component two and is multiplied by z. Thus



$$
B_o=\frac{\ell_+^*(x_1+\rho x_2)}{g d_s},\qquad
 A_o=\frac{\ell_-^*(x_1-\phi x_2)}{g(-\phi)d_s}
$$



has the correct scalar, channel, and sign normalization. The positive
base pairing is the geometric sum



$$
d_s=\frac{2}{\sqrt{15}(1-1/\sqrt5)}.
$$



The extra -phi must remain separate from negative g. Neither is a
phase convention which can be discarded.

## 4. Interval certificate and infinite errors

The original three witness vectors have full infinite-dimensional errors
strictly below 4e-13, 3e-12, and 2e-11. The final postprocessor checks
these bounds by parsing the saved certified error intervals and adding
a 10^(-90) serialization allowance.

It likewise checks each rational coarse D_2 and c box against the saved
100-digit intervals, including their imaginary parts. The large margins
are conservative relative to serialization precision. The determinant
has real part greater than 0.62 before its reciprocal is used.

The v test has norm one. Each saddle functional has norm
sqrt(1+z^2)<2 at z=rho,-phi, so widening each test by twice its old
solution error includes the entire infinite tail. The exact witness has
finite support; no separate omission of the true geometric test tail
occurs. Products involving the interval Woodbury coefficients are then
evaluated with outward complex intervals. Correlation loss can enlarge
the enclosure but cannot invalidate it.

The rerun confirms the source's strict rational bounds



$$
0.282<B_o<0.283,\qquad -1.193<A_o<-1.192.
$$



The narrower displayed intervals also check. The actual quantities
are real because they are limits of real finite ratios; the small
imaginary enclosures are not rounded to zero as a proof of reality.

## 5. Local analytic conclusion

The independent odd Hardy theorem bounds both analytic families uniformly
on every compact subdisk. The fixed-d norm limits establish pointwise
convergence on real intervals with interior accumulation points.
Normal-family compactness and the identity theorem therefore identify
one limit for the whole sequence. Cauchy's formula gives every fixed
derivative. This does not require uniformity as d approaches zero.

The strict amplitude bounds imply nonzero limiting neighborhoods and
eventual uniform lower bounds there. They supply no effective first
index or convergence rate, and none is claimed.

All sections pass. No substantive correction was required; the added
automatic comparison to the old solved-vector errors is a robustness
improvement that was incorporated before the final rerun.
