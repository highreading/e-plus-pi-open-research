> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the sharp fixed-node branch asymptotic

Date: 2026-09-13. Reviewer: audit_sources.

Reviewed `raw_fixed_node_branch_asymptotics.md` in full, against
`raw_spectral_branch_generating_function.md`,
`raw_boundary_free_moment_intertwiner.md`,
`raw_spectral_amplitude_factorial_theorem.md`, and the accepted
shifted-coefficient positivity theorem.

**Verdict: the mathematical claims pass independent review.**
The direct coefficient argument establishes the leading constant
and error term at each fixed matching node. No coefficient-transfer
theorem from the generating-function singularity is needed or used.
The separate compact-complex upper bound is also valid. No new
degree, node, or numerical asymptotic scan was performed.

One display-only typo in equation (12) was reported to the author
and has been corrected. It did not affect any estimate. The added
Section 8, including its fixed two-column minor, is also reviewed
below and passes.

## 1. Exact coefficients and the growing summation range

The displayed formula for A_(k,d) agrees with the raw monic
Legendre normalization after multiplication by c_k and division
of the monomial coefficient by d!. In particular the Borel
coefficient has denominator (d!)^2. Taking the quotient at d+2
gives exactly

    (k-d)(k+d+1) = k(k+1)-d(d+1).

The even initial value is a central binomial coefficient divided
by 2^k. The odd initial value divided by k has the same leading
sqrt(2/(pi k)) normalization. The difference between k and its
nearest even neighbor only changes the relative O(1/k) term.

For d<=L sqrt(k), dividing each two-step factor by k^2 gives
1+1/k-d(d+1)/k^2. Every factor differs from one by O_L(1/k),
uniformly over that whole growing range, and there are at most
O_L(sqrt(k)) factors. The logarithmic estimate is consequently
O_L(k^(-1/2)), rather than an unproved fixed-d approximation.

For the full range, every nonnegative factor is at most
kappa_k^2=k(k+1). The initial even and odd bounds give
A_(k,d)<=C k^(-1/2) kappa_k^d with an absolute C, also for the
odd initial d=1. This supplies the required tail majorant.

To make the tail estimate explicit, for d>L sqrt(k), x<=b, and
L>4e sqrt(b+1), the quantity

    (e^2 kappa_k b/d^2)^d

is bounded by theta^d for a fixed theta<1, once k is large.
The ratio between successive terms in the unfiltered majorant
is kappa_k b/(d+1)^2<1/2. Its tail is therefore O(exp(-c sqrt(k)))
even before division by the leading exponentially growing term.
The same reasoning controls the comparison series k^d. The
finite endpoint d<=k in the actual polynomial creates no omitted
main contribution, since L sqrt(k)<k eventually. Thus the
uniform approximation to the coefficients may legitimately be
summed with its relative O_(a,b)(k^(-1/2)) error on every fixed
0<a<=x<=b.

## 2. Bessel normalization and the exact constant

The parity filter is precisely half of I_0 plus or minus J_0;
the latter is bounded on the real axis. For t=kx with x>=a>0,
the J_0 contribution is exponentially smaller than the I_0
contribution. The usual real integral for I_0 and its local
Gaussian expansion give a relative O(t^(-1/2))=O(k^(-1/2))
error uniformly on the interval.

Multiplying the constants directly gives

    sqrt(2/(pi k)) * (1/2) / sqrt(4 pi sqrt(kx))
      = 1/(2 pi sqrt(2) k^(3/4) x^(1/4)).

This verifies equation (11), including the factor from the
parity restriction. The global coefficient majorant and
I_0(u)<=exp(u) separately prove equation (12) on all of [0,1].
Equation (11) is not asserted uniformly as x approaches zero;
the global bound, not a false extension of (11), controls that
endpoint in the subsequent integral.

## 3. Signed endpoint projection

On [0,a] for fixed a<1, the global bound is exponentially
smaller than exp(2 sqrt(k)) k^(-5/4). On [a,1], the uniform
relative error from (11) is bounded after integration against
|f|. The main integral becomes, after x=u^2,

    integral 2 u^(1/2) f(u^2) exp(2 sqrt(k) u) du.

Integration by parts supplies its leading value
exp(2 sqrt(k)) f(1)/sqrt(k), with an additive error bounded by
C ||f||_(C^1) exp(2 sqrt(k))/k. The derivative is uniformly
bounded on [sqrt(a),1]. This proves (13) with its stated
additive error for signed or complex C^1 functions, including
the case f(1)=0. No lower bound for a signed integral is
inferred before proving the nonzero endpoint value.

The exact spectral moment identity multiplies (13) by
sqrt(2k+1)/g_l. Its result is

    [psi_l(1)/(2 pi g_l)] k^(-3/4) exp(2 sqrt(k))
       * (1+O_l(k^(-1/2))),

once the endpoint is known nonzero. The factor sqrt(2) from
sqrt(2k+1) cancels the sqrt(2) in (13); no odd-branch factor
sqrt(3) belongs in this p_k normalization.

## 4. Endpoint nonvanishing and the scope of the node constants

The accepted finite-Fourier relation has nonzero eigenvalue and
an entire left side, so it gives the stated entire continuation
of the matching eigenfunction. In the prolate differential
equation, an analytic zero y(u)=a(u-1)^r+... with r>=1 contributes
at order r-1 the coefficient -2r(r-1)a-2ra=-2r^2 a.
It cannot be canceled by the remaining coefficient times y,
which starts at order r. Hence y(1) cannot vanish. A zero of
infinite order would contradict analyticity and normalization.

In the phase g_l>0, shifted positivity makes matching branch
values positive at xi_l>1. Their established nonzero limit
constant then implies psi_l(1)>0 for l>=1. This is a conclusion
from the proved asymptotic and positivity, not an assumed sign
of a general eigenfunction on the whole interval. The ground
state does not require an added sign assertion for (1).

The constants depend on the fixed eigenfunction and its nonzero
amplitude. A fixed compact node interval contains only finitely
many nodes by the spectral enclosure, so uniformity over those
nodes is justified. No bound uniform in l growing with k is
provided by this argument.

## 5. Uniform complex-parameter upper bounds

For a fixed compact parameter set, the radius
max|xi-1| is finite. Each matching-parity spectral sequence is
unbounded, so one may choose a single fixed node of each parity
whose shifted value dominates this radius. Nonnegative
coefficients in xi-1 give the absolute-value comparison (15).
Only those two fixed-node asymptotics are then used.

After restoring the positive factors sqrt(2k+1) and sqrt(3),
this proves both (16) and (17), with the finite initial indices
absorbed into C_K. The exceptional zero r_0^(1) satisfies the
bound automatically. The comparison does not require positive
coefficients in xi, a nonzero general-parameter leading
constant, or an asymptotic for the opposite branch at a node.

## 6. Real-axis Abelian endpoints

At a matching node the auxiliary Laplace transform is exactly
h_sigma/g_l times the eigenfunction integral. This gives its
entire continuation and the usual exp(w)/w leading term on the
positive real axis. Its Taylor coefficients are not identified
with the branch sequence.

For the actual generating function near z=1, first the Bessel
factor contributes 1/sqrt(2 pi x eta), and then the x=1 endpoint
integration contributes 1/(2 eta). Including the outer square
root leaves

    A_l exp(2 eta)/(2 eta sqrt(2 pi z)).

Since 2 eta=(1-z)^(-1)-1/2+O(1-z), this is exactly (20).
The contribution near x=0 can be discarded exponentially by
the global Bessel bound; no nonuniform Bessel approximation at
x=0 is used.

For z approaching -1 along the real axis, eta=-R and
exp(-t)I_0(t)<=C/sqrt(1+t). The outer factor divided by sqrt(R)
is 1/sqrt(-z), bounded there. Consequently the integrable
majorant C x^(-1/2)|psi_l(x)| justifies dominated convergence
and gives (21), with its precise factor 1/sqrt(2 pi). The limit
may vanish, as the note explicitly allows.

Both endpoint conclusions are real-axis Abelian statements.
The coefficient theorem was proved separately and does not
depend on analytic singularity transfer or on an uncontrolled
approach elsewhere on the unit circle.

## 7. The added moment correction and fixed two-column minor

The actual E_k has positive integral L_k. For fixed integer r,
the substitution v=2 sqrt(k)(1-sqrt(x)) transforms (1-x)^r
into k^(-r/2) v^r (1-v/(4 sqrt(k)))^r. Its remaining endpoint
factor has an integrable O((v+1)/sqrt(k)) correction under
exp(-v), and the leading integral is Gamma(r+1)=r!. Positivity
allows the uniform relative kernel error to be integrated at
the same relative precision. Dividing by the r=0 mass therefore
gives (22), including r=1,2 at the precision used afterwards.

Taylor's formula for a signed C^2 function leaves a remainder
bounded by its C^2 norm times (1-x)^2. Hence the first-moment
coefficient is exactly -f'(1)/sqrt(k), with an O(||f||_(C^2)/k)
remainder. No universal k^(-1/2) coefficient in the Borel kernel
itself has been presumed.

The original differential expression at x=1 gives
psi_l'(1)+psi_l(1)=xi_l psi_l(1). This proves the correction
1-(xi_l-1)/sqrt(k) in (24), with the exact row mass retained.
Expanding the two-by-two determinant directly gives the sign
and factor

    psi_a(1) psi_b(1) (xi_b-xi_a)
       * (k_n^(-1/2)-j_n^(-1/2)).

The product of the first corrections cancels, and every retained
remainder is O(n^(-1)) when both row indices are proportional to n.
With distinct limiting row proportions, the displayed difference
has a nonzero coefficient at scale n^(-1/2). The eventual
nonvanishing and sign conclusion is valid. It uses actual
matching columns and permits different node parities. For
adjacent rows the main difference can be O(n^(-3/2)), below the
proved error, so the explicitly stated exclusion of that case
is necessary and correct.

## 8. Remaining boundary of the theorem

The sharp fixed-node scale and compact-complex upper bounds are
rigorous. They do not estimate a mixed determinant, its inverse,
or the same quantities at nodes escaping every compact set.
The next required transition estimate must retain the actual
node-dependent amplitudes and distinguish fixed-node constants
from any bounds uniform in a growing node range.
