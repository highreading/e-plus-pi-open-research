> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Root independent review of the growing consecutive low-node theorem

Date: 2026-09-13. Reviewed the sharpened version of
`raw_growing_low_node_minor_theorem.md`, with relative error
n^(-1/2) exp(C m^2 log(m+1)). Verdict: all claims pass.

The endpoint recurrence gives the stated product bound for the
maximum of all preceding coefficients. Splitting the product at
ceil(sqrt(xi+3)) yields exp(4 ceil(sqrt(xi+3))); the spectral
enclosure makes exp(4m+8) a valid bound for every coefficient
and every selected node. The power-series derivative bound is
used only on the first half interval. Exact reflection parity
then supplies the other half and the uniform Taylor remainder.
No endpoint-value lower bound is being silently assumed after
normalizing the differential equation.

The uniform positive moments are justified through the full
growing order r<=k^(1/8). In the endpoint substitution the two
remaining factors lie in [0,1], and their difference from one
is bounded by (r+2)v/(4 sqrt k). The gamma tail is uniformly
exponentially small. The global coefficient estimate from the
reviewed fixed-node note bounds E_k by C exp(2 sqrt((k+1)x)),
so the other half interval also remains negligible after division
by the r-dependent numerator scale. Integer rounding contributes
only O(r/n). All these constants are independent of the growing
node count in the stated range.

The interior grid gives distinct rows in n+1,...,2n-1 once
n>=m+1. That condition holds uniformly in the theorem's stated
range for sufficiently large n. The actual node gaps exceed
one, and the derivative bound for t^(-1/2) gives the explicit
Vandermonde lower bound with gamma=1/(4 sqrt2). The factorial
product in that bound cancels in the leading determinant exactly
as stated, and the two reversed orientations make its sign positive.

The integrated Taylor order q=m(m-1)/2 is sufficient before
determinant expansion, with an explicit growing-dimensional
continuity bound. In the distinguished Cauchy-Binet term the
scaled moment entries and their errors are uniformly bounded,
so the displayed determinant perturbation estimate applies.
For every other term, r_s>=s-1 and r_s<=q imply
product r_s! <= (product_(r=0)^(m-1)r!) q^(sum r_s-q).
This keeps the excess degree and yields the sharpened error
in (18). The number of degree subsets, the coefficient determinant,
and the two Vandermonde factors are all explicitly included.

The logarithms of every remaining error factor in (17)-(19)
are O(m^2 log(m+1)), including (q+1)! in the Taylor remainder.
Thus m^2 log(m+1)=o(log n) gives vanishing relative error;
m=floor((log n)^(1/3)) is an admissible example. The moment
range condition q+1<=n^(1/8) also holds in that example.

Finally the rank-r Taylor truncations give all singular-value
upper bounds. Dividing the nonzero determinant lower bound by
the other upper bounds yields the corresponding lower bounds
with the stated exp(O(m^2 log(m+1))) dependence. These claims
are in the actual row-mass and endpoint normalization. No
unweighted full-matrix condition bound or independence of the
union with the sparse bulk family is inferred.
