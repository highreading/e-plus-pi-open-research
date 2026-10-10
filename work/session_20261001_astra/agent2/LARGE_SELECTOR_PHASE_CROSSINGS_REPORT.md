> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large-selector phase crossings report

New author analysis. The relative saddle proof is preserved and its separately assigned examination is not duplicated. The main phase-sparsity draft was read as an author deduction. No computations or additive-enclosure replay were performed.

A consistent entire continuation in m is specified along the original segment by

    Log A(w)=log 2-i pi/2+2 Log C0(x),
    w=alpha-i x/2, C0(x)=1-x+(1+i)x^2/4,

with Log C0 continued from zero. It agrees with every original integer power.

The new derivative justification is a complex-parameter lemma: on disks |zeta-m|<=m/256 the relative saddle formula has a holomorphic O(1/n) error, uniformly when n/m is sufficiently small. The proof controls complex-parameter tails on the original path and a uniform central contour deformation. Cauchy bounds then give

    |d^j/dm^j Log(1+e_n(m))|
      <=2C0 j!/[n(m/512)^j].

Thus the phase remainder is differentiated only after derivative control is proved.

For the exact phase lift Theta_n(m)=-m pi/2+psi_n(m), uniformly in the fixed-rho block,

    psi_n'(m)=-3n^2/(8m^2)
                  +O(n^3/m^3+n/m^2+1/(nm)),
    psi_n''(m)=3n^2/(4m^3)
                  +O(n^3/m^4+n/m^3+1/(nm^2)).

Eventually the reduced phase is strictly decreasing and strictly convex. Explicit bounds are

    n^2/(4m^2)<=-psi_n'<=n^2/(2m^2),
    n^2/(2m^3)<=psi_n''<=n^2/m^3.

For each integer parity epsilon, define exact slow crossings by

    r_(epsilon,k)=psi_n^(-1)(epsilon pi/2+k pi).

They are zeros of the parity interpolant's imaginary part; they need not be real crossings of the original J_m at noninteger m. The two parity families interlace. Same-parity spacing is asymptotic to (8pi/3)rho^2(log n)^2. Their inverse parametrization and curvature bounds are recorded explicitly.

With a block padded by n, let vmin=n^2/(4B_+^2), vmax=n^2/(2B_-^2). At any integer m in the original block, if d is its distance to the crossings of its own parity and delta=dist(arg J_m,pi Z), then

    vmin d<=delta<=vmax d.

For an eligible integer, put K=2^(n+2)|J_m|/|U|, retain the complete exponential bound B_E, and let q be the ACTUAL reduced denominator. A primitive error at most H necessarily implies

    d<=pi(H/q+B_E)/(2K vmin).

Conversely d<=(H/q-B_E)/(K vmax) suffices when H/q>B_E. The latter extra hypothesis is not presumed: qB_E need not be small.

Using the separate compulsory dyadic denominator q2, bounded primitive errors must lie within crossing windows of width

    exp(-kappa_rho n log n+o(n log n)),
    kappa_rho=min(3rho log 2,1+rho log 2).

The two exponents respectively retain the primitive denominator cost and possible cancellation against the complete exponential residual. The note also gives the exact finite-parameter necessary bound before this leading-scale simplification.

The outstanding assertion is integer avoidance: sufficiently strong separation of these exact crossing locations from eligible integers of the matching parity. Neither monotonicity, curvature, crossing counts, nor a finite-order phase expansion proves it. In particular a sparse sequence of exponentially close integer crossings is not excluded.

The new result is analytic crossing geometry with derivative-controlled errors and the precise required arithmetic distance scale. It is not an all-node exclusion or an irrationality theorem. Analytic constants and sufficiently large thresholds are uniform, but no numerical threshold values are supplied.

Full proofs: LARGE_SELECTOR_PHASE_CROSSINGS.md. Both new outputs require read-back before completion is reported.
