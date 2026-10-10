> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the actual even saddle multiplier

Date: 2026-09-13. Reviewer: audit_sources.
Status: PASS after an identical interval postprocessor rerun.
No mathematical correction required.

Reviewed raw_even_saddle_multiplier_limit.md and
check_raw_even_saddle_multiplier.py in full, including the fixed-$d$ kernel argument and the explicit final nonzero neighborhood. The review uses the independently passed even inverse-corner theorem and the previously certified full-space errors of the unchanged odd witness vectors.

## 1. Original monic and Cayley normalization

The reciprocal identity is


$$
\widetilde R_{2m}(1/z)=u(z)/(u_0\Psi_{2m}(z)),
$$


with the monic $\Psi_{2m}=(-1)^m\Phi_m(-z^2)$, not the reversed polynomial $F_m(z)$. This is exactly the original full-degree reversal for real coefficients.

The common Cayley denominator exponent $m$ gives the second-channel constraint at $-i$, as in the independently reviewed even inverse-corner theorem. At $y=i$, only the constant original coefficient survives and its factor is $2^m$. At $y=-i$, only the leading even coefficient survives, with the same positive factor $2^m$:


$$
P_1(i)/2^m=u_0,\qquad P_1(-i)/2^m=u_{2m}.
$$


There is no hidden sign in these two scalar evaluations.

The leading-coefficient functional has Riesz polynomial $c_m\Psi_{2m}$, so its unit vector is $\sqrt{c_m}\Psi_{2m}$. The endpoint solution has coordinates $\sqrt{c_m}x_m^o$, while $u_0=c_mg_m$. These exact identities cancel all scalar and kernel norms in (7).

At an exterior negative real point, $t=z^2$, the evaluation remains $P_1+zP_2$. In particular at the saddle it is $P_1-\phi P_2$. Replacing this by a one-channel evaluation would change the actual multiplier.

## 2. The alternating phase

The original $+i$ endpoint vector is $i^{-m}v_m$; the original $-i$ leading-coefficient vector is $(-i)^{-m}k_m$. The exterior imaginary-node Riesz vector has the same phase as the latter.

Consequently the numerator of (7), after taking the evaluation row's conjugate phase, acquires $(-1)^m$, while the denominator pairing of the two negative-imaginary-node vectors acquires no sign. This proves the exact finite formula (10). It establishes an alternating actual amplitude, not a single unsigned normalization silently inserted into the contour formula.

## 3. The fixed-$d$ kernel proof

I checked the argument for every fixed $d>0$, separately from the special $d=1/\sqrt5$ lemma.

The monic imaginary-axis recurrence has positive coefficients, so its ratios lie in
$[d,d+3/(4d)]$. Its final coefficient window tends to $3/4$; the displayed two-step contraction is uniform on this interval. It therefore gives the limiting monic ratio without assuming any convergence of the unknown earlier state.

The derivative bound for $\alpha(j)$ is correct. The denominator satisfies $4(m+1)^2-1\ge3(m+1)^2$, giving the displayed bound $4/(m+1)$. For the two-step orthonormal ratio, use both


$$
\sqrt{\alpha_j\alpha_{j-1}}\le\alpha_{j-1}+2/(m+1),
\qquad \sqrt{\alpha_j\alpha_{j-1}}<3/4.
$$


When $m+1\ge4/d^2$, the excess of the numerator over this denominator is at least $d^2/2$. Division by the latter bound proves exactly $1+2d^2/3$, not merely a weaker nongeometric bound.

The remaining single step is controlled by $\sqrt3/(2d)$. This supplies a summable reversed tail for each fixed $d>0$, so dominated normalization is justified. Dividing the limiting monic ratio by $\sqrt3/2$ gives the displayed geometric ratio


$$
\rho(d)=\frac{\sqrt{d^2+3}-d}{\sqrt3}.
$$


The normalized Riesz column and its evaluation row have opposite phases, correctly retained in (12)-(15).

## 4. Actual amplitude and unchanged interval witnesses

The constrained inverse vector is exactly


$$
x=\sqrt2(f_1-\alpha f_0),\qquad
\alpha=(w^*f_1)/(w^*f_0).
$$


The denominator has positive real part by the already proved coercivity. This formula enforces $w^*x=0$ and uses the same two previously certified solutions; it is not a newly fitted finite approximation.

The limiting denominator $\ell_d^*k_1$ is a positive geometric sum. At the saddle it equals


$$
d_s=\frac{2}{\sqrt{15}(1-1/\sqrt5)}.
$$


Thus (15)-(16) contain exactly the original amplitude scalar.

I reran the identical postprocessor with

    /opt/homebrew/bin/python3.12 work/session_20260913/check_raw_even_saddle_multiplier.py

It completed PASS. The unchanged dyadic vectors are paired with the exact geometric rows; the full-space errors $4\cdot10^{-13}$ and $3\cdot10^{-12}$ exceed the independently certified errors. The saddle functional has norm $\sqrt{1+\phi^2}<2$, so doubling these error bounds is valid. No tail of the true solved vectors is omitted, and no new inverse solve or quadrature is trusted.

The rerun gives


$$
0.0493603201444840<A_s<0.0493603201863010,
$$


hence the stated rational enclosure $0.049<A_s<0.050$. The positive sign follows from the certified interval. Reality follows from the exact real finite ratios and their convergence, not from the small imaginary interval alone.

## 5. Entire-sequence local convergence and a fixed nonzero disk

The uniform Hardy bound makes the phase-adjusted reversal factors a locally bounded analytic family. The fixed-$d$ proof gives the same pointwise limit at every point of $(-1,0)$. Therefore any two analytic subsequential limits agree by the identity theorem, and compact convergence holds for the full sequence. The usual compact-circle Cauchy formula then gives convergence of all fixed-order derivatives.

The explicit disk assertion also checks. On $|w|\le4/5$, the Hardy estimate is below 9 using $e<11/4$ and $\cos1>27/50$. Since $\rho<5/8$, the radius-$1/6$ disk centered at $-\rho$ lies inside that disk. Taylor/Cauchy bounds imply variation at radius $1/10000$ at most $54/9994<0.006$. The certified center value exceeds $0.049$, so the limiting real part exceeds $0.043$ there. Compact convergence gives eventual actual phase-adjusted real part above $0.04$.

This supplies a fixed explicit neighborhood, but no convergence rate or effective first index. It does not prove the global contour phase gap, a complete arctangent saddle estimate by itself, or any primitive-denominator bound.

