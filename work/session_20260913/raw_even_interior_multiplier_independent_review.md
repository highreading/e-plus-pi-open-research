> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the actual interior saddle multiplier

Date: 2026-09-13. Reviewer: audit_sources.
Status: PASS, including an identical interval postprocessor rerun.

Reviewed raw_even_interior_multiplier_limit.md and check_raw_even_interior_multiplier.py in full. No correction required.

The interior reference is $F_m$, whose constant-coefficient Riesz polynomial is $c_mF_m$. The actual solution and unit reference therefore map to $\sqrt{c_m}x_m^o$ and $v_m^o/\sqrt{c_m}$, respectively, while $u_0=c_mg_m$. Their Cayley scalars cancel exactly in (4). The second channel remains multiplied by the actual evaluation coordinate $+\rho$.

The endpoint vector, solution, and positive-imaginary evaluation kernel all have the same original phase. Reversal and multiplication by $i^m$ therefore cancel identically in numerator and denominator; no $(-1)^m$ remains. This distinction from the exterior monic normalization is correct.

The fixed-$d$ norm convergence follows by conjugating the independently checked negative-imaginary kernel argument. It includes the full summable tail and gives the displayed positive-imaginary geometric profile. The limiting base pairing is positive and equals $2/[\sqrt{15}(1-1/\sqrt5)]$ at the saddle.

The constrained solution $x=\sqrt2(f_1-\alpha f_0)$, its normalization $g_m\to g_+>0$, and $\alpha=(w^*f_1)/(w^*f_0)$ use exactly the previously certified operator columns. The interior test has norm $\sqrt{1+\rho^2}<2$, so the stated doubled solution errors are valid full-space bounds.

I reran

    /opt/homebrew/bin/python3.12 work/session_20260913/check_raw_even_interior_multiplier.py

with the unchanged dyadic witnesses. Outward interval arithmetic again gives


$$
0.6040688968602422<B_s<0.6040688969081851,
$$


hence the asserted rational bounds $0.604<B_s<0.605$. No new solve, quadrature, or canonical degree is involved.

The normal-family argument uses pointwise limits on every point of $(0,1)$, so the identity theorem indeed yields full-sequence local uniform convergence and convergence of each fixed derivative. The explicit disk bound also checks: the radius-$1/6$ disk about $\rho$ lies inside $|z|<4/5$; the Hardy bound there is below 9; and the variation at radius $1/10000$ is at most $54/9994<0.006$. Thus the limiting real part exceeds $0.598$, and the eventual actual real part exceeds $0.59$, on the smaller disk.

This proves the nonzero actual interior multiplier, with its original normalization and absence of a parity sign. It does not evaluate the residue contour or prove an arithmetic denominator bound by itself.

