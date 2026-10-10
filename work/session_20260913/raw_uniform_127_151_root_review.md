> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent root certificate review: all residues at 127 and151

2026-09-13. Verdict: FULL PASS. Both original general residue-transfer
theorems already passed separate independent proof audits. This review
checks the finite inputs for the two explicitly assigned primes.

The independent program check_uniform_127_151_root.py imports no author
or agent checker. It reconstructs the complete-function coefficients
from the differential generating-function recurrence

    d h_d=h_(d-1)+(2b-d+2)h_(d-2)+h_(d-3), h_0=1.

Every coefficient index is below p, so its division by d is a unit.
It constructs the actual Toeplitz Jacobi-Trudi seed matrix, computes
its determinant and first inverse column by modular elimination, and
checks the full original matrix residual. The exact hook ratio then
recovers every cofactor. All factorial arguments are below p. A full
inverse-column residual certifies all cofactors simultaneously, not a
selected minor sample.

For positive residues, it constructs the factorial U, multiplies by
(1+t^2)^k, reconstructs Q with its actual binomial derivative factors,
and evaluates Q times the truncated exponential. Thus the endpoint
check does not reuse the source's V/border calculation.

For negative residues, it reconstructs the original positive-index
high-tail map at r=p-k-1, obtains every needed derivative at1, forms the
Taylor representative, and evaluates the original finite endpoint
border. It does not reuse the source's negative-binomial functional.
The zero-th derivative is separately required to equal the determinant
seed. Every other jet is compared as well.

The fixed boundaries k=0, positive k=(p-1)/2, and negative
k=(p-3)/2 are included. Coverage is EXACTLY all127 and all151 residues.
Every determinant and endpoint seed is nonzero, and every cofactor,
jet and ratio agrees with the source certificate. The source bytes are
pinned by SHA-256 in uniform_127_151_root_certificate.json; the source
is raw_third_predeclared_uniform_seed_certificate.json.

Therefore the reviewed residue-transfer theorems prove, for ALL degrees,

    v_127(q_n)=v_127(Z_n)>=v_127(n!) for n>=254,
    v_151(q_n)=v_151(Z_n)>=v_151(n!) for n>=302.

The threshold follows uniformly for p>=7,n>=2p: if m=floor(n/p)>=2,
then 2n<2(m+1)p<=p^m. The base comparison6p<p² holds at p>=7 and
persists with m, while v_p(n!)>=m. Thus the arctangent gap is strict.

These exact finite certificates are proof inputs to the already audited
all-index theorems. They are not estimates or extrapolations from
numerical approximants. Combined rate consequences require the other
independently checked primes and the separate exact logarithm audit.
