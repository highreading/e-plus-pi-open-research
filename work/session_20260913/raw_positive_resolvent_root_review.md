> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root review of the positive-resolvent obstruction

Date: 2026-09-13. Independent review of
`raw_positive_volterra_resolvent_obstruction.md`.

**Outcome: PASS.** The actual arbitrary-forcing resolvent loses
variation diminution for all sufficiently large parameters, including
the actual grid k(k+1). This does not refute the high-family zero count.

I checked the ordered-factor argument for K and the causal Green jump
k_xxx(y+,y)=1/y². Under epsilon=(a²/lambda)^(1/4), a=1/2, and the
stated positive scaling a²/epsilon³, the four coefficients of the
rescaled equation and its third initial derivative are exactly those
displayed. On a fixed compact triangle the companion matrices and
initial vectors converge uniformly. Variation of constants and the
finite-interval Gronwall bound therefore justify the uniform kernel
limit, with no WKB or moving-interval assumption.

The limiting kernel solves g''''−g=0 with initial third derivative
one, giving g=(sinh−sin)/2. Its displayed minor at t=2pi,h=pi/2 is
exactly [cosh(h)²−2cosh(t)sinh(h)]/4 and is strictly negative.
Uniform convergence preserves that strict sign for every sufficiently
large lambda. The chosen source and target points stay in (0,1).

I separately checked the sign-change deduction. The limiting ratio
tends to infinity at the second source and then increases between
the two designated later targets. A constant strictly between their
ratios gives the three required strict signs. Two disjoint, normalized
smooth bumps approximate the point sources away from every target
and preserve those signs. Their input has one sign change. The full
resolvent's identity term vanishes at all three targets, so its
variation-diminishing claim fails as well.

The source width and location may depend on lambda. Neither the
bumps nor this arbitrary-forcing argument belong to the two specific
origin branches or to the constrained high polynomial span. Those
limitations are correctly explicit in the note.
