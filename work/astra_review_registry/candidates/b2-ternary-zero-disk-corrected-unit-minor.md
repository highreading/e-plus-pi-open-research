> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Corrected coefficientwise unit-minor certificate on the auxiliary index disk 3Z_3

Status: UNVERIFIED CANDIDATE
Author: worker_4
Content SHA256: 627b84db31ceb70a32d19d4ed78056281b5ae9e2bcc79510cfc396a8bc76364c

STATUS AND SCOPE

Author: worker_4. Corrected candidate awaiting independent review. This claim concerns an auxiliary integer matrix and its index interpolation. It does not concern the actual reduced denominator of an approximation to e+π.

DEFINITIONS AND STATEMENT

For n≥0 define
H_n(x)=n![z^n]e^{xz}(1−z+z²/2)^n,
J_n=(d/dx)(x^nH_n(x))|_{x=1},
K_n=(d²/dx²)(x^nH_n(x))|_{x=1},
M_n=(d³/dx³)(x^nH_n(x))|_{x=1}.

Let B_n have ordered rows (H_n(1),J_n), (J_{n+1},K_{n+1}), and (K_{n+2},M_{n+2}). Let I_01,I_02,I_12 denote determinants in increasing row order. Define Ω_n=gcd(I_01,I_02,I_12), with nonnegative gcd convention. There is no division by a factorial, row content, or displayed polynomial prefactor.

The entries are integers. Indeed, the contribution indexed by b,c to H_n is (−1)^b binom(n;b,c,n−b−c)(n)_{b+2c}x^{n−b−2c}/2^c when admissible. A product of b+2c consecutive integers contains at least c even factors, so each such coefficient is integral.

The exact index interpolation defined below satisfies, coefficientwise in Z_3⟨Y⟩,
B(3Y) ≡ [[1,0],[1,2],[2,0]] (mod 3),
(I_01(3Y),I_02(3Y),I_12(3Y)) ≡ (2,0,2) (mod 3).
Consequently its first minor is a unit everywhere on 3Z_3, the three minors have no common zero there, and v_3(Ω_n)=0 for every nonnegative integer n divisible by 3. In particular this holds throughout the original n≥2 range on that progression.

PROOF: INTERPOLATION AND COEFFICIENTWISE TAIL

Write (X)_L=X(X−1)…(X−L+1), with (X)_0=1. For r≥0 set
D_r(X)=Σ_{b,c≥0} (−1)^b (X)_{b+2c+r}(X)_{b+c}/(2^c b!c!).
Here D_r denotes the derivative interpolation, not the scalar D appearing later in the prefactor discussion.

At every nonnegative integer n the sum terminates. Expanding the polynomial power by the multinomial theorem and differentiating e^{xz} r times proves D_r(n)=H_n^{(r)}(1), including r>n.

Fix an integer a and put X=a+3Y. For R=b+2c, s=b+c, k=floor(R/3), and q=floor(s/3), at least floor(L/3) factors of (a+3Y)_L belong to 3Z_3[Y]. Also v_3(b!c!)≤v_3(s!)=q+v_3(q!). Therefore each summand has Gauss valuation at least
floor((R+r)/3)+q−v_3(b!c!) ≥ k−v_3(q!) ≥ k−v_3(k!).
The last inequality uses q≤k. Since v_3(k!)≤k/2, these valuations tend to infinity. There are only finitely many pairs for each R. Thus the sums converge in the restricted power-series ring Z_3⟨Y⟩, whose coefficients tend to zero 3-adically.

For R≥3, k≥1 and the integral valuation lower bound is at least 1. Hence every term with R≥3 vanishes coefficientwise modulo 3. This is an infinite-tail proof; a finite computation alone would not establish it.

Define
H(X)=D_0(X),
J(X)=XD_0(X)+D_1(X),
K(X)=X(X−1)D_0(X)+2XD_1(X)+D_2(X),
M(X)=X(X−1)(X−2)D_0(X)+3X(X−1)D_1(X)+3XD_2(X)+D_3(X).
These interpolate the four specified derivative combinations. Define B(X) using rows (H(X),J(X)), (J(X+1),K(X+1)), and (K(X+2),M(X+2)). All operations preserve coefficientwise congruences, since the series are integral on the relevant disks.

PROOF: ALL SHIFTED ROWS AND SIGNED MINORS

Only R<3 is needed modulo 3. Its denominators are 3-adic units, and every retained falling factorial on a+3Y reduces to its value at a. Thus for a=0,1,2 and r=0,1,2,3, D_r(a+3Y) reduces coefficientwise to H_a^{(r)}(1). Terms excluded from the integer evaluation vanish there, so this assertion follows from the truncation, not from assuming residue constancy.

Direct expansion gives H_0=1, H_1=x−1, H_2=x²−4x+4. The corresponding derivative tuples through order three, evaluated at 1, are
(1,0,0,0), (0,1,0,0), (1,−2,2,0).

They give the residue representatives for the ordered matrix rows:
(H_0(1),J_0)=(1,0),
(J_1,K_1)=(1,2),
(K_2,M_2)=(2·1+4·(−2)+2, 6·(−2)+6·2)=(−4,0).
Therefore B(3Y) has the asserted reduction. At X=0 its exact matrix is [[1,0],[1,2],[−4,0]], with ordered determinants (2,0,8). Coefficientwise throughout the disk their reductions are (2,0,2).

In particular I_01(3Y)=2+3G(Y) for G∈Z_3⟨Y⟩. Every Y∈Z_3 therefore gives valuation zero. This proves all stated conclusions about the auxiliary minors and Ω_n.

EXCEPTIONAL PREFACTORS AND THEIR SCOPE

The original algebraic reduction displays I_01=(X+1)D and I_02=(X+2)(2X+3)E, where, writing h=D_0(X), u=D_1(X), v=D_2(X),
D=2(X+1)h²−2hu−(X−1)u²−uv,
E=−2X(X+2)h²+4Xhu+(X+2)hv+(X²−2X−1)u²+Xuv.
These identities are contextual source identities; the unit-minor proof above does not rely on them or on division by their prefactors. Their analytic extensions follow from continuity and the density of nonnegative integer indices on each disk.

The displayed exceptional parameters are −1, −2, and −3/2. The first two lie outside 3Z_3. The third lies inside it, and the proved unit first minor excludes a common zero there despite the vanishing factor 2X+3 in the second minor. In fact 2X+3 is divisible by 3 throughout this disk, consistently with the second minor's zero reduction. No classification on other disks is claimed, and no exceptional prefactor is cancelled to infer a valuation theorem.

The archived endpoint-gcd transfer requires p>2n+4. At p=3 it does not apply for n≥2. Accordingly v_3(Ω_n)=0 here gives no assertion about actual primitive endpoint cancellation, the final reduced numerator or denominator, or irrationality of e+π.

CORRECTION HISTORY, EVIDENCE, AND SELF-AUDIT

The error originated in worker_4/note_000002.md, which wrote H_2=x²−4x+6. Both original definitions instead give four contributions, from (b,c)=(0,0),(1,0),(2,0),(0,1), equal to x², −4x, 2, 2. Equivalently (1−z+z²/2)² has z² coefficient 2. Thus its constant contribution after multiplying by 2! is 4. The earlier third row (0,0) modulo 3 and third minor 0 modulo 3 are withdrawn. The corrected third row is (2,0), and the third minor is 2. The first-minor conclusion survives for the explicit reasons proved above.

Source dependencies and evidence paths:
• work/session_20260927/literature_update_and_b2_analytic_certificate.md, §§3–4, SHA-256 0e3c1da5a871f1684955c66305a60ff95c4d273bf3e6c3d2442232f838ff2a15: interpolation and analytic-tail framework, read completely.
• work/session_20260927/hp_b2_cubic_maximal_minor_gate.md, §§1,3,5–6, SHA-256 7736790e3894ce58b43cc2810fca914c1e6a0f1e51029921ef4469817fe062b1: exact matrix normalization, contextual prefactors, and stated endpoint-transfer cutoff, read completely.
• work/astra_20260929/worker_4/note_000002.md: preserved erroneous derivation.
• work/astra_20260929/worker_4/note_000003.md through note_000005.md: discrepancy disclosure, source reconciliation, and reported successful fresh finite computation.

The proof above supplies the infinite-tail justification separately from that computation. Archived PASS labels and the author's checks are not independent approval. Worker_1's independent review is pending. There is no unresolved mathematical dependency for the stated auxiliary unit-minor conclusion beyond checking this argument; the actual endpoint denominator problem remains unresolved.