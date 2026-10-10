> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the separated-channel low evaluation inverse

Date: 2026-09-13. Reviewer: audit_results.

Reviewed raw_separated_channel_low_evaluation.md in full, with
particular attention to Sections 4--5. All stated algebraic
identities and the explicit inverse bound pass. No correction
was required. No additional degree construction or numerical
test was used.

## 1. Exact coefficient-transform orientation and boundary support

The interleaved monomials form the claimed degree-capped vector
space. The branch recurrence creates each new leading term only
from xi times the row two positions earlier, giving the listed
positive diagonal factors. The row grouping requires
q(m-1)-q(q-1)/2 transpositions; ordering the actual parity nodes
in increasing spectral index reverses the same permutation.
The resulting low evaluation determinant is positive.

The equations c=H^(-T)b and Y=H E have the correct orientations.
For the symmetric recurrence, multiplication by xi is represented
by the infinite matrix K. In the row e_0^T K^j, every path stays
below index 2j; in (e_1^T-s e_0^T)K^j every path stays below
2j+1. These are strictly below N for each requested monomial.
Thus replacing K by its N-dimensional principal block introduces
no boundary term. This proves the inverse coefficient rows in (9)
before estimating their norms.

Dividing by N^(2j) correctly changes from monomials in xi to
monomials in z=xi/N^2. For N>=2 the reviewed spectral bounds
give norm(K_N)<=N^2. The seed row e_1^T-s e_0^T has norm
sqrt(1+s^2)=sqrt7/2. Consequently each inverse row has the
asserted bound, and its Frobenius norm is at most sqrt(7N)/2.
This is a bound for an explicitly represented inverse, rather
than an inversion of an upper bound on H.

## 2. Actual-node interpolation constants

The spectral enclosures place every initial scaled node in [0,1].
For j>i in a fixed parity channel, the exact lower gap is
4(j-i)(i+j+sigma+1/2)-1/4. After subtracting the proposed
2(j-i)(i+j+1), the result is
2(j-i)(i+j+2sigma)-1/4>0 because i+j>=1.

Multiplying these gaps yields (13). Its second inequality follows
from i!(t-1-i)! >= (t-1)!/2^(t-1) and
product_(j!=i)(i+j+1) >= t!/(i+1) >= (t-1)!.
For each actual channel N<=2t+1; if t>=2 then this is at most
5(t-1). The factorial lower bound and the numerator coefficient
l1 norm at most 2^(t-1) therefore give the explicit cardinal
coefficient bound (50e^2)^(t-1). The t=1 channel has the constant
cardinal polynomial and needs no factorial estimate.

The interleaved inverse evaluation transpose has these cardinal
coefficient columns. Its Frobenius norm is at most sqrt(N) times
the larger column bound. Combining with the coefficient inverse
gives exactly

    ||Y_(p,low)^(-1)|| <= (sqrt7/2) N
                          (50e^2)^(ceil(N/2)-1), N>=2.

The rational-to-symmetric branch conversion is also correctly
oriented: Y_p=D_row Y_r D_channel. Hence
Y_r^(-1)=D_channel Y_p^(-1) D_row, with norm(D_channel)=1
and norm(D_row)=sqrt(2N-1). The additional spectral amplitudes
are retained in the separate maximum reciprocal factor.

## 3. Scope

The initial low rows span the entire degree-capped vector-polynomial
space. This is exactly what makes independent Lagrange interpolation
valid. It does not hold automatically for the specified high rows.
The exact remainder reduction Y_high=A_rem Y_low retains that
missing matrix explicitly and does not infer a lower singular-value
bound for A_rem. The reviewed theorem therefore supplies a useful
controlled basis change, without resolving the high-kernel estimate,
endpoint cancellation or the irrationality problem.
