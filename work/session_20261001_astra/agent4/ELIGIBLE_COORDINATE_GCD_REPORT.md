> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Eligible coordinate gcd report

A new actual-family factorial denominator theorem is proved in ELIGIBLE_COORDINATE_GCD.md.

Fix b=3, m=1. For every n>=2^22 with n=3 mod 13, the retained rational eligibility set is nonempty. Every eligible coordinate satisfies

    v_13(gcd(|N_(j,1)|,|N_(j,2)|))=0,
    v_13(q_j)>=2v_13(n!).

On the explicit unbounded subset

    n_s=13^(s+1)+3, s>=5,

all three positive coordinates are defined and

    v_13(q_j)=2v_13(n_s!)=(n_s-4)/6.

Thus the conclusion applies to any rational selection among the eligible coordinates, including the minimum-denominator selection. Analytic eligibility and its selection cost are retained. This is a fixed-b unbounded family, not a growing-b theorem.

The proof uses one new exact residue gate, b=r=3,p=13, which executed successfully with exit code 0 and PASS_SINGLE_NEW_RESIDUE_GATE. The reconstructed residual-positive and exponential contractions were respectively (1,10,1) and (8,3,3) modulo 13; the normalized Toeplitz determinant was 7. All relevant data are recorded in the research note. The existing local transfer is used only in its actual prime/residue domain. The high-block scalar is kept; its value is proved to be one modulo 13 on the displayed subsequence using Frobenius. No prime table or previous checker was rerun.

The canonical primitive selector is also explicit. With M the fixed row-normalized Toeplitz matrix, a_j the reconstruction row, and s_i=(n+i)!/n!, put

    B_j=a_j adj(M)diag(s_i),
    eta_j=gcd(entries B_j), l_j=B_j/eta_j.

Then l_j is the primitive integer selector, its height is ||B_j||_1/eta_j, and its integer forcing normalization is Usel_j=X_j/eta_j. The common factor 2^n n! has been removed exactly. Eligible j>=1 have zero rational correction.

The complete denominator factorization is

    N_(j,1)=(n!)^2 X_j, N_(j,2)=Y_j,
    K_j=gcd(|X_j|,|Y_j|),
    F_j=gcd((n!)^2,|Y_j|/K_j),
    q_j=((n!)^2/F_j)|X_j|/K_j.

Both residual contents remain explicit. Neither is replaced by a lift denominator. On the new progression both K_j and F_j are 13-adic units. The retained saturated formula also gives v_13(h_j)=v_13(d), so the original rational scale between the adjugate and saturated coordinate gcds is preserved.

The reviewed obstruction gives an additional necessary height condition for any eligible coordinate sequence with log q_j=O(n):

    liminf log Hsel_j/(n log n)>=1/2.

Thus a successful direct-envelope certificate must use factorial-scale canonical primitive selector height. This does not establish signed coordinate-error asymptotics or transfer the scalar divergence theorem to reconstructed centers.

The proved lower denominator exponent is (log 13)/6, strictly below log 2. Divergence of q_j is established on this subfamily, but the upper bound needed for q_j delta_coord->0 remains open. The note identifies the precise further local lemma: control the reconstructed COMPLETE second forcing contraction at the factorial threshold, simultaneously with eligibility, retaining logarithmic corrections at their actual depth.

The separate DIRECT_SELECTOR_OBSTRUCTION_REVIEW.md gives PASS with an explicit degree-hypothesis qualification for the rational-correction asymptotic statements. Its saddle consequence remains conditional on Agent 2's author asymptotic. Completed earlier reviews and checks remain untouched. No rationality or irrationality conclusion for e+pi is claimed.
