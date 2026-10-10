> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the branch pencils and adjacent Casoratian

Date: 2026-09-13. Root verification of
`raw_branch_boundary_pencils_and_casoratian.md`.

**Verdict: the exact determinant identities, stated obstruction, and
combined-polynomial real-root assertions pass.**

Diagonal similarity by sqrt(2j+1) gives the rational upper
distance-two entry (j+1)^2(j+2)^2/((2j+1)(2j+3)) and the stated
nearest-neighbor entries. The odd branch has one extra fixed
sqrt(3) normalization, giving the rational seed matrix of determinant
one. This is consistent in both the scalar and adjacent identities.

For the scalar pencil, the recurrence pivots eliminate coordinates
2 through k-1 in order. Moving the first two columns after them has
sign (-1)^(2(k-2))=1. The one remaining recurrence row is precisely
minus the omitted distance-two coefficient times the future
coordinate. Its determinant with (-1/2,1) is the negative even
solution, and with (1,0) is the positive odd solution. The pivot
product telescopes to the displayed double-factorial constant.
The k=2 empty-pivot case has the same signs.

The positive-mass obstruction uses the correct invariant: a size-k
Hermitian pencil with a positive semidefinite coefficient of rank
k-1 has, after congruence, a one-dimensional zero-mass block. If
that block's constant coefficient is nonzero the degree is k-1.
Otherwise regularity forces a nonzero off-block vector, whose
squared norm gives a nonzero leading coefficient at degree k-2.
The actual determinant degrees are strictly smaller in exactly the
stated ranges. Constant strict equivalence preserves degree and
mass rank, so the exclusion follows. It does not cover a smaller
deflated pencil or indefinite mass. The signed-residue argument
is also valid: the selected left and right vectors have disjoint
supports in those ranges, so residues sum to zero; regularity
prevents the rational function from vanishing identically.

For the adjacent determinant, the final two recurrence equations
have coefficients -U_(N-2)u_N and
N^2/(2N-1)u_N-U_(N-1)u_(N+1). Their triangular combination has
positive determinant U_(N-2)U_(N-1). The earlier elimination has
even sign, and the two seed columns have determinant one, giving
exactly C_(N+1) times the Casoratian. The explicit N=1 calculation
also checks the constant and sign. Conversion to the symmetric p
normalization contributes sqrt((2N+1)(2N+3))/sqrt(3), consistent
with the product of the a coefficients in (15).

The characteristic polynomial is that of the actual principal
finite compression of a real symmetric K, so its zeros are real
and principal-compression eigenvalues weakly interlace. No claim
of simple eigenvalues is required. The positive first-coordinate
Rayleigh quotient ensures at least one positive zero. These facts
apply to the determinant of two adjacent rows; they do not transfer
to either scalar branch individually.

The reviewed bound K_[0,N-1]<= (N+3/4)I supplies a useful direct
corollary: for xi>N+3/4 the Casoratian is nonzero and has sign
(-1)^N. This holds in the growing regime xi comparable to N^2
for all sufficiently large N. It is a same-parameter, two-channel
statement and does not determine mixed minors at different nodes.
