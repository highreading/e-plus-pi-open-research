> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the two-branch evaluation-minor obstruction

Date: 2026-09-13. Root verification of
`raw_two_branch_evaluation_minor_obstruction.md`.

**Verdict: the all-index fixed-row obstruction passes.** It does not
give an obstruction in the coupled finite window, and the source states
that restriction correctly.

I independently checked the normalization in (1): the odd generator is
u=x-1/2, whereas the normalized spectral generator is sqrt(3)u. Thus
r^1=sqrt(3)p^1/sqrt(2k+1) gives precisely the displayed identity.
The action of T on u^d in (2) follows by differentiating u^d; the
degree-preserving coefficient is d(d+1)+3/4, and its once-used sum
in T^M is the stated S_(M,sigma). No lowering term can contribute to
the first subleading coefficient, since it loses four degrees relative
to a raising term.

The monic imaginary-Legendre coefficient is k(k-1)/(2(2k-1)); the
Borel transform multiplies its ratio to the leading coefficient by
k(k-1). Shifting x=u+1/2 gives the four coefficients in (4), including
the factor (k-2)/2 multiplying rho_k in the fourth coefficient.
Subtracting the appropriate Krylov sum gives all four entries in (7).
Their factored differences in (10), (12), (14), and (15) agree by
rational algebra. The constant boundary branch at m=1 is handled as
an absent coefficient, not a negative power.

For equal-degree polynomials f=A(x^d+a x^(d-1)+...),
g=B(x^d+b x^(d-1)+...), the leading term of f g'-f'g is
AB(a-b)x^(2d-2). For degrees d,d+1 its leading coefficient is
AB>0. These facts produce exactly the three-row sign table (-,+),
(+,-),(+,+). Positivity of the actual branches on x>=1 justifies
passing from the Wronskian sign to the sign of an evaluation minor
for every pair of nodes beyond a fixed-row threshold.

The invariant argument allows arbitrary interleaving of the four
chosen columns: the orientation of each selected same-branch column
pair is fixed independently of the selected row pair. Row signs and
row permutations affect the two compared minors equally. Column
signs and permutations multiply all three sign ratios by a common
factor. The unequal ratios (-,-,+) therefore cannot become equal.
If all nonzero order-two minors had one sign, all three ratios would
be positive, a contradiction. Positive spectral amplitudes, and the
reflection sign change, do not invalidate this argument.

Each fixed row block occurs on sufficiently far actual spectral
columns because both parity subsequences of xi_l are unbounded. The
proof supplies no uniform threshold when m grows. In particular,
the coefficients of order m^3 divided by nodes of order n^2 need not
be small for m of order n. The note correctly leaves the retained
finite matrix's conditioning and kernel angle unresolved. No new
numerical computation was needed for this review.
