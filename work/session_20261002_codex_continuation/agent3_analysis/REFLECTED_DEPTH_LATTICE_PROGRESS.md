> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Discrete depth sensitivity: fresh gate and exact coupling

2026-10-02. Original analysis target, after the saved quadratic critical-window theorem. No audit.

## Gate

Archive queries: `discrete.{0,30}(depth|saddle|parameter|lattice)`, `neighbor.{0,30}(depth|parameter)`, `consecutive.{0,30}(depth|h)`, `rounding.{0,30}(saddle|depth|parameter)`, and `critical.{0,30}(lattice|rounding)`. Read `sources/quartic_neighbor_saddle_phase_barrier.md` opening phase-mesh result and `sources/item376_j1_terminal_normalized_carrier_recurrence_barrier_report.md` Section 5. The first supplies an old polynomial quartic phase mesh with unresolved exponentially close integer phase alignment; the second explains limits of moving-modulus holonomic recurrence. Neither is the reflected two-pole center's positive critical depth increment. The saved quadratic note is exact internal overlap. Search absence is not a novelty claim.

Fresh primary searches:

- `site:arxiv.org discrete saddle point asymptotics consecutive coefficients ratio uniform`
- `site:arxiv.org Laguerre polynomials degree difference asymptotic ratio large alpha`
- `site:arxiv.org rational approximation integer parameter saddle point rounding`

Opened Deano, Huertas, Marcellan, https://arxiv.org/pdf/1301.4266 (introduction and ratio setting), and Huybrechs, Opsomer, https://arxiv.org/pdf/1612.07578 (large-degree expansion framework). Ratio and higher-order expansions are method overlap; fixed-parameter Perron ratios are not imported into the simultaneous n,N limit or onto the positive evaluation point. Prior primary Laguerre/HP readings remain attributed in the quadratic note.

## Exact coupling before asymptotics

For any function f on integer X with the required zero extension, define

    Z_N(f)=sum_l binom(N,l) f(N-2l).

Pascal's identity gives EXACTLY

    Z_(N+1)(f)=sum_l binom(N,l)[f(X+1)+f(X-1)], X=N-2l.

For f_D(X)=binom(X+n,n) on X>=0, its central increment multiplier is

    [f_D(X+1)+f_D(X-1)]/f_D(X)
      =2+n(n-1)/[(X+1)(X+n)].

For f_C(X)=binom(X-1,n) on X>=n+1, it is

    2+n(n-1)/[(X-n)(X-1)].

The edge terms are retained by zero extension and are exponentially negligible at quadratic depth. Thus a discrete result need not be obtained by differentiating an uncontrolled o(1) asymptotic.

The intended critical-depth result is a complete negative spacing

    c_(n,h+1)-c_(n,h) ~ -2sqrt(2)e n^(-3/2)

when the actual alpha tends to e. The exact binomial coupling is now being combined with finite differences of Laguerre reciprocal-root sums and the actual determinant. A mesh theorem would guarantee polynomial rounding accuracy and isolate at most one much more accurate integer depth per n; it would not exclude an exceptionally close alignment with e+pi.
