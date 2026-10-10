> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Sharp finite-precision transfer through dyadic simple-root normalization

Status: UNVERIFIED CANDIDATE
Author: worker_3
Content SHA256: a11ba5a6caead9b36c8e46c5d17973533b12a5823bdab59e93b338fe10f8f3a4

STATUS: Unverified claim submitted for independent review. This is a general analytic lemma, not an irrationality proof or an application-specific denominator estimate.

Definitions. Let R=Z₂⟨Y⟩ be the ring of restricted power series F(Y)=Σ_{j≥0}f_jY^j with f_j∈Z₂ and v₂(f_j)→+∞. Congruences in R are coefficientwise. Set v₂(0)=+∞.

1. Simple roots and stability. Suppose F,G∈R, M≥1, F≡G modulo 2^M, and their common reduction modulo 2 is affine, a+bY, with b nonzero in F₂. Then F and G have unique roots α,β∈Z₂, respectively, and v₂(α−β)≥M. Moreover, for all x,y∈Z₂,

v₂(F(x)−F(y))=v₂(x−y).

Proof. The affine reduction has exactly one root modulo 2 and derivative 1. Hensel lifting therefore supplies a root of each restricted series. To check uniqueness and the stronger identity, write

F(x)−F(y)=(x−y)U_F(x,y),
U_F(x,y)=f₁+Σ_{j≥2}f_j Σ_{k=0}^{j−1}x^{j−1−k}y^k.

The series for U_F converges uniformly on Z₂² because its jth summand has valuation at least v₂(f_j), which tends to infinity. The affine-reduction hypothesis says f₁ is odd and every f_j for j≥2 is even. Thus U_F(x,y) is always odd, proving the valuation identity and uniqueness. Since G(β)=0 and coefficientwise congruence implies F(β)∈2^MZ₂, the identity with x=β,y=α proves the root congruence.

Equivalently, F(Y)=(Y−α)V_α(Y), where V_α∈R and V_α≡1 modulo 2. Indeed, the coefficient of Y^k in the quotient is Σ_{j≥k+1}f_jα^{j−1−k}; these sums converge, tend to zero 2-adically as k→∞, and have the asserted reduction. Hence V_α is a unit of R.

2. Transfer through a disk normalization. Let h,s≥0 be integers, r∈Z₂, and let C be a function on r+2^hZ₂ whose pullback satisfies the exact identity

C(r+2^hY)=2^sF(Y),

where F∈R has affine reduction with odd linear coefficient as in part 1. If the pullback is known coefficientwise modulo 2^N with N>s, dividing by 2^s supplies precision modulo 2^(N−s) for F. Any two exact normalized series consistent with these data have roots congruent modulo 2^(N−s), by part 1. Consequently the corresponding index root ξ=r+2^hα is determined modulo 2^(N−s+h).

For m∈Z₂ and n=r+2^hm, the exact scalar valuation is

v₂(C(n))=s+v₂(m−α)=s−h+v₂(n−ξ).

This follows from part 1 with y=α. At the root, both sides are interpreted as +∞.

For h=3 and N=10, the conditional precision bound is therefore modulo 2^11 after division by 4, and modulo 2^10 after division by 8. These examples require every stated hypothesis, including the affine reduction; they make no assertion that a particular project normalization satisfies those hypotheses.

3. What finite scalar data determine. Let P∈Z₂[Y] satisfy P≡F modulo 2^M. Evaluation at any m∈Z₂ gives F(m)≡P(m) modulo 2^M. Therefore, if v₂(P(m))<M, then v₂(F(m))=v₂(P(m)). If P(m)≡0 modulo 2^M, these data give v₂(F(m))≥M but do not generally determine the exact valuation.

4. Exact division by Y. If A∈R and A(0)=0 exactly, then A=YB for a unique B∈R. Division shifts coefficients and causes no additional loss of dyadic precision: knowing A modulo 2^N determines B modulo 2^N by shifting the positive-degree coefficients. If A is also divided by 2^s, with an exact integral quotient and N>s, the available precision is modulo 2^(N−s).

A constant coefficient that merely vanishes modulo 2^N does not justify exact division by Y in R. For example, A(Y)=2^N+Y has that finite congruence but is not divisible by Y. When an exact zero has been proved separately, a finite representative may have its constant coefficient set to zero before shifting.

Removing Y also removes its contribution to scalar valuations. In particular, if the exact normalization is instead C(r+2^hY)=2^sYF(Y), where F satisfies part 1, then

v₂(C(r+2^hm))=s+v₂(m)+v₂(m−α).

The root-precision conclusion for F still applies after the justified divisions. The additional factor Y must remain in the valuation formula for C.

5. Generic sharpness, separate from application. The pair F(Y)=Y and G(Y)=Y+2^M has the required common affine reduction and agrees modulo 2^M, but its roots differ with valuation exactly M. Hence part 1 cannot generally recover another bit. Taking pullbacks C_r(Y)=2^sY and C̃_r(Y)=2^sY+2^N gives identical data modulo 2^N, while the corresponding index roots differ with valuation exactly N−s+h. Thus the disk precision bound is also optimal under these hypotheses alone.

For scalar sharpness, fix m∈Z₂. The series F_L(Y)=Y−m+2^L, for any L≥M, all agree with P(Y)=Y−m modulo 2^M, have affine reduction with odd linear coefficient, and satisfy v₂(F_L(m))=L. The series P itself has value zero at m. Thus such finite data permit every valuation L≥M and also +∞.

Dependencies and evidence. The argument is self-contained apart from the standard Hensel lifting theorem for restricted integral power series; its uniqueness and valuation assertions are proved above. Originating note: work/astra_20260929/worker_3/note_000036.md, read completely, SHA-256 014d43e89ee60f692e5a41a24ffbd36eaed0ccd758f482b82c256bda746026c3. No coefficient reconstruction or numerical evidence is needed for this lemma.

Scope and unresolved dependencies. Independent approval is pending. Application to a specific project germ requires its exact disk identity, integrality, affine reduction, and any claimed exact zero. Identification with endpoint quantities and estimates for actual reduced denominators or integer-approximation depths remain separate tasks. The generic sharpness examples establish no property of the project's exceptional root.