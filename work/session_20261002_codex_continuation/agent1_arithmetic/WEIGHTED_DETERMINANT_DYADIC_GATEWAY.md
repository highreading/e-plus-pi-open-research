> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Weighted coefficient-one determinant: exact dyadic gateway and open normalization

Incremental author result L23, 2026-10-02. Target gate is in TARGET_LEDGER.md. Root owns the M22 coefficient construction, selector owns odd-prime carry/content, analysis owns full nonzero/error. This note authors dyadic normalization only, not an independent audit of those results. Status: the shifted moment identity and conditional COMPLETE primitive denominator formula are proved; two all-degree hypotheses for the specific orthogonal polynomial remain open.

## 1. Exact target and final pair

Let d_r=!r be ordinary derangement integers, C_s=d_(2s)−(−1)^s. For k≥2 put n=2k−1. Root's family uses a primitive integer polynomial q_n(y)=Σ_(j=0)^n q_j y^j, orthogonal to C at all s=0,…,n−1:

    Σ_j q_j C_(j+s)=0.

For s≤2k−2 this matches the complete e and pi responses. Set w=q_n(−1), v_i=(−1)^i, 0≤i<k, and

    L_s=4Σ_(r=0)^(s−1)(−1)^r/(2s−1−2r), L_0=0,
    V_s=Σ_j q_j L_(s+j),
    R_ij=−Σ_(t=0)^n q_t(2(i+j+t))!+V_(i+j).

All V_s and R_ij have ODD denominators. The full moment matrix is R+S w vv^T, S=e+pi, and

    det(R+S w vv^T)=alpha+beta S,
    alpha=detR, beta=w v^T adj(R)v.                (1)

After clearing the complete odd coefficient denominators and taking the FULL common gcd, the center −alpha/beta has exact dyadic denominator

    v_2(q_center)=max(0,v_2(beta)−v_2(alpha)).       (2)

This is the final pair, not a row-clear count. The notation q_center is distinct from the polynomial q_n.

## 2. First residue and a stronger shifted Gamma identity

The elementary derangement recurrence d_r=r d_(r−1)+(−1)^r gives odd d_(2s) and even d_(2s−1). In fact d_(2s)=1 mod4 because 2s times the even odd-index term is divisible by4. Therefore C_s is even and

    C_s/2=s mod2.

Thus the C-Hankel matrix divided entrywise by2 has rank at most2 mod2. This is a raw coefficient-lattice fact, not a primitive-pair valuation statement.

Use the exact Gamma functional from L22,

    A(P)=∫_0^∞ e^(−t)P(1−t)dt,

and define

    B_r=A((x²+1)^r), b_r=B_r/2^r.

**Proved shifted moment identity:** B_r=2^r b_r with b_r an ODD integer for EVERY r≥0. Its exact recurrence is

    b_0=b_1=1,
    b_(r+1)=(r+1)(2r+1)b_r−r(r+1)b_(r−1)−r.      (3)

Proof. Put sigma(t)=(t−1)²+1 and J_r=∫e^(−t)(t−1)sigma(t)^r dt. Integration by parts gives

    B_(r+1)=2^(r+1)+2(r+1)J_r,
    J_r=(2r+1)B_r−2rB_(r−1)−2^r.

Eliminate J_r and divide by2^(r+1) to obtain(3). The recurrence proves integrality inductively. If the previous two terms are odd, its reduction mod2 is (r+1)−r=1, since r(r+1) is even. Thus v2B_r=r at all depths/degrees. ∎

This is the exact normalization suggested by y→y+1, stronger than a finite residue rank observation.

## 3. A precise equivalent gate for normalized q_n

For z=(y+1)/2 the signed coefficient functional L_C(P)=A(P(x²))−P(−1) has integer normalized moments

    mu_0=0, mu_r=b_r for r≥1.                    (4)

Let K_n=(mu_(i+j))_(0≤i,j<n), and let c_j, 0≤j≤n, be the signed maximal minors of the n×(n+1) moment matrix (mu_(i+j))_(0≤i<n,0≤j≤n), with c_n=detK_n. These signs are chosen so Σ_j c_j mu_(j+s)=0.

The matrix K_n is nonsingular for n≥2: it is congruent to the real Gamma Gram form minus evaluation at y=−1 on the even span; L22's evaluation-norm argument gives a negative nonzero determinant. Thus its monic orthogonal polynomial has coefficients c_j/c_n.

The following statements are equivalent for the primitive integer q_n:

    (a) q_n(2z−1)/2^n∈Z_2[z] and its leading coefficient is odd;
    (b) v2(c_j)≥v2(c_n) for every j;
    (c) the monic normalized polynomial is integral over Z_2 coefficientwise.

Proof. In the shifted/scaled basis the monic polynomial is Σ(c_j/c_n)z^j, so(b) and(c) coincide. If it is2-integral, substitution y=2z−1 reversed as 2^nP((y+1)/2) gives a monic2-integral polynomial in y; its rational coefficients have odd reduced denominators. Clearing only these odd denominators and removing integer content leaves an odd leading coefficient and(a). Conversely(a) divided by its odd leading coefficient gives(c). ∎

Also(a) implies q_n(0) is odd: writing q_n(y)=Σ t_j(y+1)^j gives v2t_j≥n−j and t_n odd, hence q_n(0)=Σt_j is odd. The implication is exact; the all-degree cofactor inequalities in(b) remain unproved. A rank≤2 observation modulo2 does not prove them, and the existing finite q data cannot be extrapolated.

## 4. Conditional complete-pair theorem

The following theorem uses a separate arctangent divisibility gate. It does NOT incorrectly transfer a bound between two different polynomial bases.

Assume q_n is an integer polynomial with q_n(0) odd, w=q_n(−1)≠0, the response matching above holds, and

    v2(V_(i+j))≥i+j+v2(i!)+v2(j!)+1
                    for EVERY 0≤i,j<k.           (5)

Then define gamma_k=k(k−1)+2Σ_(i=0)^(k−1)v2(i!). The FULL pair in(1) satisfies

    v2(alpha)=gamma_k,
    v2(beta)=gamma_k+v2(w)−2[k−1+v2((k−1)!)],
    v2(q_center)=max(0,v2(w)−2[k−1+v2((k−1)!)])  (6)

after the complete common gcd.

Proof. Put D_i=2^i i!. The factorial part of −R, divided entrywise by D_iD_j, is an integer matrix. Indeed for t≥0,

    (2(i+j+t))!/(2^(i+j)i!j!)
      =2^t [(i+j+t)!/(i!j!)] (2(i+j+t)−1)!!.

For t≥1 this is even. The t=0 term reduces modulo2 to binom(i+j,i). Gate(5) makes the COMPLETE rational arctangent correction even in this same normalization. Hence R=D M D over Z_2 with

    M_ij=−q_n(0)binom(i+j,i) mod2.               (7)

The matrix Z_ij=binom(i+j,i) is the product P P^T for the unit lower triangular Pascal matrix P_it=binom(i,t). Every northwest principal determinant is1. Thus M is2-integrally invertible and all its northwest principal minors are odd. The determinant gives the first equality in(6).

Write z_i=v_i/D_i. In v^T R^−1v=z^T M^−1z, the valuation of z_i is −[i+v2(i!)], strictly decreasing with i. The diagonal entry (M^−1)_(k−1,k−1) is an odd ratio of consecutive northwest minors. Therefore its final-coordinate square is the unique term of lowest valuation; all cross/other terms have strictly higher valuation. Thus

    v2(v^T R^−1v)=−2[k−1+v2((k−1)!)].

The identity beta=w alpha v^T R^−1v gives the second equality. Equation(2) proves the last equality after the FINAL common content, independently of any row denominator or raw cofactor content. ∎

This formula explains the finite dyadic primitive pair exactly when(5) is verified. It still requires an all-degree proof of the actual family hypotheses, rather than a finite-pair pattern.

## 5. Why normalized q alone does not yet prove gate(5)

If(a) holds, t_j in q_n(y)=Σt_j(y+1)^j obey v2t_j≥n−j. Let

    I_r=∫_0^1(1+x²)^r dx.

Integration by parts gives (2r+1)I_r=2r I_(r−1)+2^r. Thus I_r/2^r is2-integral for all r. The rational arctangent contribution to q_n(y)(y+1)^s is therefore at least n+s+1 deep: its terms are4t_j I_(j+s−1), except the constant residual at j=s=0, which supplies pi rather than a rational contribution.

HOWEVER this bound is in the (y+1)^i basis. The factorial/Pascal normalization in(7) is in the y^i basis. Expanding y^s in powers of y+1 yields only the unconditional bound v2V_s≥n+1 from this argument. For large k it does not reach (5) at the largest indices. An early message to root proposed the stronger bridge prematurely; this basis mismatch was corrected before saving a theorem. An additional cancellation identity for the specific orthogonal q_n is needed.

The two precise remaining arithmetic obligations are now:

1. prove the all-degree cofactor inequalities in§3, or provide a counterexample;
2. prove gate(5) for the actual orthogonal q_n, with the rational arctangent response retained.

Neither obligation is an audit of another agent. They are new author arithmetic, and no broader scan is proposed as a substitute.

## 6. Integral operator representation of the normalized moments

There is a concrete integral structure behind b_r, beyond integrality of the moments. Let L_m(t) be the standard Laguerre basis, orthonormal for e^(−t)dt on[0,infinity). Multiplication by x=1−t has symmetric tridiagonal matrix J with

    J_(m,m)=−2m, J_(m,m+1)=J_(m+1,m)=m+1.

Consequently multiplication by z=(x²+1)/2 has the INTEGRAL symmetric pentadiagonal matrix T=(J²+I)/2:

    T_(m,m)=3m²+m+1,
    T_(m,m+1)=−(m+1)(2m+1),
    T_(m,m+2)=(m+1)(m+2)/2,

with its symmetric counterparts. Every displayed entry is an integer, despite the division by2 in the polynomial defining z. Since L_0=1,

    b_r=(T^r)_(0,0).                            (8)

For any fixed r only finitely many indices are needed. This follows from the standard three-term Laguerre recurrence and exact multiplication, with no limiting2-adic measure presumed.

The signed moments mu_0=0,mu_r=b_r for r≥1 can be represented by the direct sum T⊕0 and vector(e_0,1), paired with the integral signature form diag(I,−1). Thus the normal-basis Hankel matrix is an integer indefinite Gram matrix of explicitly given Krylov vectors. This is a new exact candidate for a2-adic block/Smith analysis.

The existence of an integral symmetric moment operator ALONE does not imply2-integral monic orthogonal coefficients. For example the integral symmetric3×3 matrix [[0,1,1],[1,0,1],[1,1,1]] at state e_0 has moments1,0,2,3 and monic degree2 orthogonal polynomial z²−(3/2)z−2. The special pentadiagonal structure in(8), and the signed mass at0, must supply any missing all-degree cofactor bound. It is not assumed here.

The receipt stores eleven NEW normalized moment states n=2,…,12, not independently reconstructed parent projections. Their determinant valuations are0,1,2,4,11,18,27,36,49,62,77 and their monic coefficients are2-integral at those degrees. These support the block strategy, while both all-degree obligations above remain open. The first-degree signed Hankel determinant vanishes, so an ordinary nonsingular Jacobi recurrence cannot be used starting at degree0 without treating that initial singular block.

## 7. Proved integral orthogonal block basis in the quadratic ring

The moment operator has a stronger canonical lattice structure. Let

    ell_r(x)=r! L_r(1−x),

the monic shifted Laguerre polynomial. Then

    ell_0=1, ell_1=x,
    ell_(r+1)=(x+2r)ell_r−r²ell_(r−1),
    A(ell_r ell_s)=delta_(r,s)(r!)².             (9)

Work in the FREE rank2 ring over Z_2[z]

    R_2=Z_2[z,x]/(x²−2z+1).

**Block integrality theorem:** for every h≥0,

    ell_(2h), ell_(2h+1)∈2^h R_2.              (10)

Proof. The h=0 pair is1,x. Combining two consecutive recurrences gives

    ell_(2h+2)
      =[x²+(8h+2)x+12h²+4h−1]ell_(2h)
       −4h²(x+4h+2)ell_(2h−1).

In R_2 the bracket is2[z+(4h+1)x+6h²+2h−1]. Thus the first term is in2^(h+1)R_2 if ell_(2h) is in2^hR_2. The second term is also in2^(h+1)R_2 by the preceding odd polynomial's2^(h−1) divisibility (and is zero when h=0). The next single recurrence,

    ell_(2h+3)=(x+4h+4)ell_(2h+2)−4(h+1)²ell_(2h+1),

proves the same depth for the next odd polynomial. This closes induction. ∎

Set Phi_(2h)=ell_(2h)/2^h and Phi_(2h+1)=ell_(2h+1)/2^h. Their expansions are integral in the quadratic ring. Write

    Phi_(2h)=E_h(z)+x A_h(z),
    Phi_(2h+1)=B_h(z)+x O_h(z).

E_h and O_h are MONIC degreeh, degA_h≤h−1, degB_h≤h. The coefficient of z^h in B_h is (2h)(2h+1), obtained from the x^(2h) coefficient of the monic odd Laguerre polynomial; it is even. The leading degree-h change of basis from z^h,xz^h to this pair is consequently a triangular2-integral matrix with diagonal1. The full change of basis by degree is unit triangular by2×2 blocks. Its inverse is2-integral as well. Thus the Phi pairs are an explicit Z_2 basis of R_2, not merely a rational orthogonal basis with unspecified denominators.

Their Gamma norms are

    A(Phi_(2h)²)=[(2h)!/2^h]²,
    A(Phi_(2h+1)²)=[(2h+1)!/2^h]²,

with BOTH exact dyadic valuations2v2(h!), by v2((2h)!)=h+v2(h!). Distinct Phi polynomials are Gamma-orthogonal. Hence every consecutive pair supplies one integral orthogonal block with equal valuation, and the block valuations are nondecreasing with h.

The signed evaluation at z=0 is integral in this same quadratic ring (x=i), so the actual normalized signed coefficient form is this diagonal Gamma block form plus the explicit rank-one evaluation correction restricted to Z_2[z]. This provides an exact block lattice for proving the maximal-minor inequalities in§3. A subspace restriction and a rank-one correction can still alter primitive pivots, so no cofactor inequality or arctangent cancellation is asserted solely from(10). The remaining target is now a concrete integral block elimination problem, rather than a generic moment-integrality claim.

## 8. Subsequent regular-subfamily resolution

The continuation `WEIGHTED_REGULAR_DYADIC_SUBFAMILY.md` now proves BOTH premises of§4 for EVERY n=4^j+1, j≥1. It uses a new monic divided-difference basis with exact normalized moment branches and a period15 residue identity, then proves the atan response bound in that SAME basis. The full actual-q formula is consequently unconditional on that infinite subfamily. General-all-n integrality remains unproved; the endpoint depth v2q_n(−1) is isolated rather than replaced with a raw factorial count. The earlier notes in§3–§7 describe the exact state before that new subfamily theorem.
