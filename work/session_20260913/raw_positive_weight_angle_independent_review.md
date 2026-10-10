> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the positive-weight channel-angle closure

Date: 2026-09-13. Reviewer: audit_computations.

Reviewed `raw_positive_weight_channel_angle_closure.md` in full.
The proof passes. I independently derived its positive-power lemma,
finite support conditions, cutoff-dependent factorization, surrogate
angle bound, separately normalized perturbation, and retained rank
consequence. No correction is requested.

My companion derivation `raw_reoptimized_energy_angle_independent_proof.md`
gives somewhat sharper optional constants. They are not necessary for
the source theorem. The source's deliberate loose constants are valid.

## 1. The commutation claim uses the correct finite support condition

The actual reflection matrix C is upper triangular and therefore
preserves every coordinate prefix. Its exact commutator with K has
right support in the last two coordinates. For H=MI−K, expansion

    [H^r,C]=sum_(j=0)^(r−1) H^(r−1−j)[H,C]H^j

shows that every summand annihilates a vector supported through s
when s+2r<N. Indeed H^j w is supported through
s+2j<=s+2r−2<=N−3, strictly before those two boundary coordinates.
This independently verifies source equation (1), including the
strict inequality and its endpoint indices.

The infinite polynomial argument in the source gives the same result:
all polynomial degrees remain below N in both compositions, because
reflection never increases degree. No choice of a self-adjoint
realization of the infinite row operator is involved.

## 2. The positive-power estimate is valid for the whole supported sum

For j=2r, equation (1) applies through r, giving

    (Cw)*H^(2r)Cw=||C H^r w||²
                   <=||C||² w*H^(2r)w.

For j=2r+1 it gives exactly

    (Cw)*H^(2r+1)Cw=(C H^r w)*H(C H^r w)
      <=lambda_max(H)||C||²||H^r w||²
      <=cond(H)||C||² w*H^(2r+1)w.

Thus only floor(h/2) commuting powers are needed, even though F has
degree h. The sufficient assumption s+h<N covers every term, and
all coefficients of the stated polynomial F are nonnegative. Summing
the quadratic inequalities is legitimate and proves source (2).

This does not assume C commutes with F, F^(1/2), or the full finite K.
It also does not estimate the unsupported full weighted reflection
operator. The distinction is the central valid improvement.

For the surrogate spaces, the energy-space involution is
F^(1/2) C F^(−1/2) restricted to their combined image. Its norm is
bounded by (2). This orientation is correct. The full actual-space
reflection in the preceding residue note was instead
F^(−1/2) C F^(1/2); the source explicitly distinguishes the two.

The reviewed principal-angle identity gives
delta_*=sqrt(2/(1+M_C²)). Since M_C>=1,
delta_*>=1/M_C. No ordinary orthogonality of the raw component
spaces has been assumed.

## 3. Constants, actual roots, and degree counting

For N=2n and M=2n+1, the reviewed row-spectrum enclosure gives

    H>=I/4,
    H<=(4n²+2n+5/8)I<=7n²I.

Therefore cond(H)<=28n². Multiplying its square root by the
reviewed bound ||C_(2n)||<=12n exp(2sqrt(6n)) gives precisely
the source's A_n=12sqrt(28)n² exp(2sqrt(6n)).

For b=ceil(n^(3/4)) and every retained high root with l>b,

    xi_l−M>=l(l+1)−2n−1/4>=b²/2

for all sufficiently large n. This includes the −1/4 caused by
using M=2n+1 instead of the spectral upper endpoint 2n+3/4.
Thus every factor beta_i−M is positive, and the expansion of
F_b(K)=product[(beta_i−M)I+H] has positive coefficients.

Moving one last root into a low factor preserves the original
Q_sigma and makes the high degrees equal. The original domain
dimensions and actual offset seed e_1−(sqrt3/2)e_0 are unchanged.
The source's support estimate n+2ell_max+2m+2 and h<=n/2+1
give s+h<=3n/2+O(n^(3/4))<2n eventually. Hence all surrogate
polynomial coefficient identities are within the finite degree range.

The opposite component spaces cannot intersect there. Multiplication
by a nonzero p_m does not destroy injectivity, since its nonzero
polynomial product has an interleaved leading index below N.
There is no appeal to an unproved generic rank statement.

An optional tighter count is s<=n+b+2+2m and h<=(n−b)/2,
so b+4m+4<n suffices. The source needs only eventual admissibility,
for which its simpler bound is fully adequate.

## 4. Approximation exponent and block normalization

The actual spectral interval has length <=6n² and the enlarged pole
gap is at least b²/2. Thus z_beta−1>=b²/(6n²). Monotonicity of
arcosh, followed by arcosh(1+u)>=sqrt(u) for 0<=u<=1, supplies
the source's error

    epsilon_n<=2exp[−(m+1)b/(sqrt6 n)].

With b>=n^(3/4) and m>=24n^(3/4), its exponent is at least
4sqrt(6n), exactly as in (9). Positive partial-fraction weights
sum to less than one, so no omitted multiplicity factor enters.

The old bound R>=2I/n remains valid for this larger gap, since its
first gap eventually exceeds2n and its final denominator is at most
n². Hence p_m is positive on the row spectrum eventually.

With the *actual* first-channel Gram G_a, the difference obeys

    ||F^(1/2)(R−p_m)W_a G_a^(−1/2)||<=n epsilon_n/2.

This uses the commuting F energy and R>=2I/n; it does not need
an angle bound. The second block is unchanged. Thus the exact
t_n in (10) is correct, and the surrogate's individual smallest
singular values are at least1−t_n. Its separate orthonormalization
and the supported angle bound then give
sigma_min(E_tilde)>=(1−t_n)/A_n.

Weyl gives delta_n>=(1−t_n)/A_n−t_n. Because
A_n t_n=O(n³exp(−2sqrt(6n))) tends to zero, eventually
t_n<=1/(4A_n). For A_n>=1 this implies delta_n>=1/(2A_n).
Thus both the constant and the exponent in source (12) are valid.
The proof does not substitute a surrogate Gram for the actual Gram.

## 5. The retained normalization and its precise consequence

The surrogate lies in a coordinate prefix enlarged by at most
r=min(n−1,2(m+ell_max)+4). Its energy-image projection defect
therefore has rank at most r. Replacing it by E costs t_n, and
orthonormalizing the combined actual image costs exactly 1/delta_n.
This gives the source's decreasing-singular-value bound

    sigma_(r+1)((I−Pi_L^F)O)<=t_n/delta_n<=2A_n t_n.

The source's O(n³exp(−2sqrt(6n))) follows immediately.
Since the energy retained space has dimension n+1 and O has n−1
orthonormal columns, at least n−1−r retained singular values are
at least sqrt(1−eta_n²), once eta_n<1. This proves the stated
rank lower bound.

I checked the actual pairing: an orthonormal retained energy basis
is F^(1/2)P_L^T F[L,L]^(−1/2), and the combined normalized basis
is F^(1/2)[R W_a,W_b] B^(−1)(E*E)^(−1/2). Their pairing is

    F[L,L]^(−1/2) Z_L B^(−1)(E*E)^(−1/2).

This is exactly the source's matrix, with all finite positive
Gram factors retained. Its rank is the original rank of Z_L.
The already proved high factorization has invertible Z_H and S,
so the same rank bound holds for the prescribed high moment block
on rows n+1,...,2n−1 and spectral nodes xi_0,...,xi_n.

## 6. Accepted scope

This is an actual minimum-angle bound after cutoff reoptimization,
not another equivalent unresolved norm target. It yields a proved
n−O(n^(3/4)) retained rank and an explicit energy-normalized
projection estimate outside O(n^(3/4)) directions.

The source correctly leaves those exceptional directions, the
amplitude-weighted cardinal factors, complete high rank, the physical
endpoint angle, and primitive shrinking unresolved. The new metric
depends on b; neither the old sqrt(n)-cutoff angle nor the full Theta
operator is implicitly bounded. All substantive claims pass.
