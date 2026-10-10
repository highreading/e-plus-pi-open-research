> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large-degree saddle selector report

New author analytic reduction, not a proved large-degree asymptotic. Earlier logarithmic-degree results are preserved. Their Gamma lower-bound correction was saved separately and read back; no proof or computation was replayed.

Direct forcing coordinates are valid for every i>=0, without an HP window. For the selector of degree 4m,

 D=n!2^(-n)[x^n](1+2x+2x^2)^n(1-2x^2)^(2m).

For fixed n the coefficient is a nonzero polynomial of degree floor(n/2) in m. This proves only a finite exceptional set at that n, not nonvanishing along m=floor(rho n log n).

Both denominator and complete logarithmic residual reduce to the same meromorphic differential

 G(w)dw=V(w)^n(2w^2-1)^(2m)w^(-n-1)dw.

The denominator is (-1)^n n!/(2pi i) times its closed integral around zero. The logarithmic residual is (-1)^(n+1)2n!/i times its open integral from (1-i)/2 to (1+i)/2 to the right of zero. The denominator factor (-1)^n corrects an omission in an earlier progress message.

Writing kappa=m/n, BOTH phases have stationary equation

 (4+16kappa)w^4-16kappa w^3+(8kappa-4)w^2+1=0.

There are two small roots near +/-i/sqrt(8kappa) and two roots at (1+/-i)/2+1/(8kappa)+O(kappa^(-2)). Including n!, their candidate amplitudes at m=floor(rho n log n) have leading n log n coefficients 1 and 1+rho log 2 respectively. These are local phase calculations, not dominance statements. The different integration cycles and conjugate cancellation must be resolved.

Rigorous global bounds are retained:

 |D|<=n!2^(-n)5^n3^(2m),
 |Flog|<=pi n!2^m(sqrt(2)-1)^n,
 |Eexp|<=9(1+sqrt(2))^n[2(1+sqrt(2))]^(2m)/(n+1).

The research note also gives the exact complete exponential integral and its stationary equation. The exponential residual cannot be assumed negligible at this new degree scale.

On D!=0, an honest common clearer with H=2n+4m is J=2^H H!, giving

 q<=2^(H-n)H!n!5^n3^(2m),
 log q<=4rho n(log n)^2+O_rho(n log n log log n).

This is an upper bound for the actual reduced denominator, not an identification with it. Its coarseness prevents a shrinking-form certificate from an error bound only of order exp(-c n log n). It does not prove divergence.

The precise open task is a uniform decomposition of the two specified cycles through the four quartic saddles, with signed multipliers and bounded remainders, first establishing denominator nonvanishing. Endpoint-adjacent contributions and the complete exponential integral must then be compared on that same normalization. Improved arithmetic cancellation may also be necessary.

No explicit rho is certified, and no all-rho obstruction is proved. The output is the permitted effective saddle reduction with explicit unresolved dominance, not an extrapolation of the logarithmic-degree theorem. No scans, repeated checks, or independent review were performed.

Files: LARGE_DEGREE_SADDLE_SELECTOR.md and this report. Both require read-back before completion is reported.
