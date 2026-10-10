> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the separated-channel low evaluation theorem

Date: 2026-09-13. Root verification of
`raw_separated_channel_low_evaluation.md`.

**Verdict: the determinant, explicit inverse, and all-index
exponential inverse bound pass.** The high-row remainder matrix
is a separate unbounded factor.

The even row has a new leading monomial in channel zero, and the
odd row in channel one; its other component has no later monomial
in the interleaved ordering. Thus the coefficient matrix really
is lower triangular. Successive distance-two recurrence pivots
give the stated diagonal entries. Counting each pivot's occurrences
gives the power floor((N-1-k)/2) in its determinant. The symmetric
normalization includes precisely the two indicated products of a_j.

Grouping interleaved monomial rows requires
sum_(j=0)^(q-1)(m-1-j) crossings. This is the stated s_N for
both odd and even N. The grouped channel evaluation matrix is
block diagonal with the two ordinary Vandermonde factors.
Interleaving the actual spectral columns cancels this same sign.
The positivity assertion therefore has the correct column order.
Coincidences across channels are harmless; only within-channel
coincidences would make a Vandermonde zero.

The transpose in the interpolation inverse is correct: a row
combination c of the branch basis has monomial coefficients H^T c.
Its two prescribed component polynomials are uniquely obtained by
the separate cardinal polynomials, so c=H^(-T)b.

The inverse coefficient bound has an independent operator proof,
rather than an inversion of forward entry bounds. A path starting
at coordinate zero in j applications of K reaches at most 2j;
one starting at coordinate one reaches at most 2j+1. In all
the asserted monomial identities these indices stay below N, so
no compression boundary term is lost. The correct odd seed row is
e1^T-(sqrt(3)/2)e0^T, of norm sqrt(7)/2. After the scale xi=N^2z,
the reviewed ||K_N||<=N^2 makes every inverse coefficient row
bounded by this norm. Frobenius summation yields sqrt(7N)/2.

The actual spectral bounds put every scaled parity node in [0,1].
Their gap minus 2|j-i|(i+j+1) is positive even in the closest
case i=0,j=1. The two factorial estimates in the product of gaps
hold for every i. For t>=2, N<=2t+1<=5(t-1), and Stirling's
elementary lower bound gives the displayed exponential denominator
bound. The coefficient l1 norm of each numerator is at most
2^(t-1). The t=1 channel is treated separately as the constant
cardinal polynomial. Frobenius summation of both channel inverse
blocks therefore gives exactly the stated sqrt(N) factor and
base 50e^2.

Combining the two independently bounded inverse factors proves
the explicit inverse bound for Y_p,low. The rational-normalization
conversion and the separate g_l diagonal are correctly retained.
The ordinary generating-function upper bound is uniform on this
growing parameter range and supplies the claimed at-most-exponential
condition number, without a claim about weighted moment condition
numbers.

Finally polynomial reduction separately modulo the two node
polynomials preserves all selected evaluations. Reexpanding the
remainders in the invertible low basis proves
Y_high=A_rem Y_low exactly. The source correctly does not infer
a lower bound on A_rem's nonzero singular values from the bounds
on Y_low. That is the remaining high-row question.
