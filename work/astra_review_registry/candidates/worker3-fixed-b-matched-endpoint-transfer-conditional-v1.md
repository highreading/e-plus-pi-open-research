> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact matched endpoint reconstruction and fixed-b transfer conditional on the factorial determinant lemma

Status: UNVERIFIED CANDIDATE
Author: worker_3
Content SHA256: 48ed273001a125bce2ec58f5ce053cf10340c71cd64373fde3fc356852bc6601

Status: UNVERIFIED CONDITIONAL CANDIDATE. Author: worker_3.

For every fixed integer b≥1, the argument below proves eventual projective uniqueness, nonzero matched endpoint Y, and

(−1)^n R(1)/(Yε_n)→(√2−1)^b,

conditional on the factorial determinant lemma stated below. All project-specific application hypotheses are derived here. The ordinary Padé prefactor is a separately published dependency. This candidate does not independently approve the determinant lemma, estimate actual reduced denominators, or prove irrationality.

Fix n≥b. Let F(z)=4 arctan(z/(2−z)), and seek rational polynomials A,B,C with degree caps (n,b,n), R=A+Be^z+CF=O(z^(2n+b+1)), and B(1)=C(1)=Y. Write B(z)=Σ_(j=0)^b B_jz^j and C*(t)=t^nC(1/t). All asymptotic assertions below hold with b fixed.

Define the moment functional

ℒ(P)=∫_(−1)^1 P((1+iu)/2)du.

Direct integration gives F(z)=zℒ(1/(1−zt)) near zero, and F(1)=π. Let P_k be the Legendre polynomial, normalized by P_k(1)=1, and put c_k=binom(2k,k) and

p_k(t)=i^kP_k(−i(2t−1))/c_k.

These are monic rational polynomials. Rodrigues' formula and integration by parts give orthogonality and the nonzero bilinear norms

h_k=ℒ(p_k²)=2(−1)^k/[(2k+1)c_k²].

Their recurrence and symmetry are

p_(k+1)=(t−1/2)p_k+β_kp_(k−1),  β_k=k²/[4(4k²−1)],
p_k(1−t)=(−1)^kp_k(t).

In particular p_k(1)>0 by induction in the recurrence. Their roots are (1+iu)/2 with real −1<u<1. Thus p_k(0)≠0, all reciprocal roots have modulus at most 2, and |p_k(0)|=|p_k(1)|≤2^(−k/2).

For analytic germs define the absolutely convergent factorial functionals

ℓ_j(t^r)=1/(n+r+1−j)!,  0≤j≤b,
ℓ_B=Σ_j B_jℓ_j.

Set

K_n(t,s)=Σ_(k=0)^n p_k(t)p_k(s)/h_k,
V(t)=K_n(t,1),
χ_k=ℒ(p_k/(1−t)),
H_n(t)=Σ_(k=0)^n χ_kp_k(t)/h_k,
W(t)=1/(1−t)−H_n(t).

Here H_n is a projection polynomial, not an arithmetic auxiliary sequence.

The exact finite reduction follows from the coefficients above degree n. For r=0,…,n+b−1 they are

ℒ(t^rC*)=−ℓ_B(t^r).

The first n+1 equations uniquely give

C*=−Σ_(k=0)^n ℓ_B(p_k)p_k/h_k.

Orthogonality and triangularity of the monic basis make the remaining equations precisely

ℓ_B(p_(n+l))=0,  1≤l≤b−1.

The endpoint condition is ℓ_B(V)+Σ_jB_j=0. Finally A=−T_n(Be^z+CF), where T_n denotes Taylor truncation through degree n. Consequently these b homogeneous rational equations in the b+1 coefficients of B are equivalent to the original problem. No rank assumption has been used.

The entire evaluated remainder also has an exact expression. At z=1, the exponential Taylor tail beyond degree n is ℓ_B(1/(1−t)). The other tail is ℒ(C*/(1−t)), since |(1+iu)/2|≤1/√2 on the moment segment. Substituting the finite projection gives

R(1)=ℓ_B(W).

Both complete tails have been included; this is not an estimate using a single Taylor coefficient.

For the cofactor identities, let U_l=p_(n+l), let U denote the b−1 rows (ℓ_j(U_l))_(j=0)^b, and put e=(1,…,1), v=(ℓ_j(V)), w=(ℓ_j(W)). The reduced matrix is M=[U;e+v]. Choose its signed maximal-cofactor vector B so that B·z=det[M;z]. Then exactly

Y=−D_V,  R(1)=D_W+N,
D_V=det[U;e;v],  D_W=det[U;e;w],  N=det[U;v;w].

If D_V≠0, then det[M;e]≠0. Therefore M has rank b, its kernel is one-dimensional, and its nonzero cofactor vector reconstructs the unique projective solution with Y≠0. The same endpoint determinant suffices for both conclusions.

Next identify the ordinary error and the reference normalization. Define the rational ordinary endpoint approximant

f_n=ℒ((p_n(1)−p_n(t))/(1−t))/p_n(1).

Then π−f_n=χ_n/p_n(1). Orthogonality applied to the polynomial (p_n(1)−p_n(t))/(1−t) gives

χ_n/p_n(1)
=2(−1)^n/[c_n²p_n(1)²] · ∫_(−1)^1 P_n(u)²/(1+u²)du.

Thus ε_n=(−1)^nχ_n/p_n(1)>0. The published claim worker3-ordinary-pade-prefactor-v1 gives, with ρ=1+√2,

ε_n∼(4π/ρ)ρ^(−2n).

In particular ε_(n+1)/ε_n→ρ^(−2). The present candidate uses that published result without changing it.

Put U_0=p_(n+1), b_n=p_(n+1)(1)/p_n(1), and α_n=χ_(n+1)/χ_n. Christoffel–Darboux, obtained by telescoping the recurrence with the displayed norms, gives

V(t)=p_n(1)[U_0(t)−b_np_n(t)]/[h_n(t−1)].

Integrating its kernel form gives

p_(n+1)(1)χ_n−p_n(1)χ_(n+1)=h_n.

It follows that

W(t)=[χ_nU_0(t)−χ_(n+1)p_n(t)]/[h_n(1−t)].

For completeness, the numerator divided by h_n equals 1 at t=1. Subtracting this expression from 1/(1−t) therefore gives a polynomial of degree at most n. The displayed expression has zero moment against every polynomial Q of degree at most n: write Q(t)=Q(1)+(t−1)S(t) and use orthogonality to eliminate S. Hence that polynomial is exactly H_n, proving the formula for W.

Symmetry now yields the exact normalizations

V(0)=−2p_n(1)U_0(0)/h_n>0,
W(0)/V(0)=(−1)^(n+1)ε_n(1+α_n/b_n)/2,
α_n/b_n=−ε_(n+1)/ε_n.

Let J_n=U_0/U_0(0). Whenever W(0)≠0, write V=V(0)J_nG_(V,n) and W=W(0)J_nG_(W,n), where

G_(V,n)=[1−b_np_n/U_0]/[2(1−t)],
G_(W,n)=[1−α_np_n/U_0]/[(1+α_n/b_n)(1−t)].

The following is the precise external factorial determinant hypothesis, abbreviated FD. Fix d≥1 and S=d(d−1)/2. Let J_n=Q_n/Q_n(0), where deg Q_n≤n+1, Q_n(0)≠0, the reciprocal roots are uniformly bounded, and J_n(z/n)→exp(−cz) locally uniformly. Suppose P_(i,n)=a_(i,n)J_nG_(i,n), where every a_(i,n) is nonzero and all G_(i,n) are uniformly analytic and bounded on a common fixed disk. Put Δ_j=ℓ_(j+1)−ℓ_j and

E_n=det([t^r]G_(i,n))_(1≤i≤d,0≤r≤d−1),
Ξ_(n,d)=(n!)^d n^S det(Δ_j(t^rJ_n))_(0≤r,j≤d−1).

FD asserts

(n!)^d n^S det(Δ_j(P_(i,n)))/∏_i a_(i,n)
=Ξ_(n,d)E_n+O(1/n),
Ξ_(n,d)→exp(−dc)∏_(j=0)^(d−1)j!≠0.

The remainder is uniform under the stated analytic bounds. For two families sharing J_n and d, with the denominator coefficient determinant bounded away from zero, division gives their amplitude ratio multiplied by E_(W,n)/E_(V,n)+O(1/n). No rate for convergence of E_n is assumed. This is exactly the scoped content needed from fixed-size-factorial-determinant-finite-jet-factorization-v1; its independent verification remains separate.

We now verify the actual reference hypotheses without importing a historical microscopic-limit assertion. Put r_k=p_(k+1)/p_k. On |t|≤1/20, induction in r_k=t−1/2+β_k/r_(k−1) gives

Re r_k≤−9/20,  |r_k|≤397/540.

The maps w↦t−1/2+(1/16)/w preserve the closed half-plane Re w≤−9/20 and are contractions there. Their fixed point is

λ(t)=[t−1/2−sqrt((t−1/2)²+1/4)]/2,
λ(0)=−a,  a=ρ/4,

with the square-root branch positive at zero. Comparing the recurrences gives

sup|r_k−λ|≤(100/243)sup|r_(k−1)−λ|+(20/9)|β_k−1/16|.

Since β_k→1/16, r_k→λ uniformly. Cauchy's formula gives convergence of fixed derivatives on a smaller disk.

To obtain the microscopic limit, define a_k=r_k′(0)/r_k(0). The uniform bounds and absence of zeros give a uniform second-order Taylor bound for the analytic logarithms of r_k(t)/r_k(0), normalized to vanish at zero. Since a_k→λ′(0)/λ(0)=−√2 and p_(n+1)=∏_(k=0)^n r_k, uniformly for z in any fixed compact set,

log J_n(z/n)=(z/n)Σ_(k=0)^n a_k+O(1/n)→−√2z.

Thus J_n(z/n)→exp(−√2z). The root bound required by FD is the exact bound 2 already obtained from the Legendre zeros.

For each high row use amplitude U_l(0) and factor

G_(l,n)=[U_l(t)/U_l(0)]/J_n(t).

The finite product of ratios r_k(t)/r_k(0) gives G_(l,n)→h(t)^(l−1) uniformly, where h=λ/λ(0). These factors are uniformly analytic and bounded for fixed b. Symmetry gives b_n=−r_n(0)→a. If κ=ρ^(−1)=√2−1 and s=κ², the ordinary error ratio gives α_n→−as and

1+α_n/b_n→1−s>0.

Therefore W(0)≠0 eventually, and the two displayed normalized factors for V and W are uniformly analytic and bounded on a common smaller disk.

The fixed-point equation implies

1−t=a(h+1)(h−s)/h,  a(1−s)=1/2,
h(0)=1,  h′(0)=−√2.

Consequently their limiting factors simplify exactly to

G_V=(1−s)/(h−s),  G_W=2/(h+1).

Apply FD with d=b to the rows U_1,…,U_(b−1),V and to the rows U_1,…,U_(b−1),W. For b=1 the high-row list is empty. Replacing each column after the first by its difference with the preceding original column leaves e=(1,0,…,0). Expansion in that row gives

D_V=(−1)^(b+1)det(Δ_j(P_i^V)),
D_W=(−1)^(b+1)det(Δ_j(P_i^W)).

The limiting coefficient determinants have rows 1,h,…,h^(b−2),G_V or G_W. Put S=b(b−1)/2. Changing the local variable from t to x=h−1 multiplies each determinant by (h′(0))^S. The polynomial rows become (1+x)^j and have triangular coefficient matrix with diagonal 1. Hence the limiting determinants are explicitly

E_V=(−√2)^S(−1)^(b−1)/(1−s)^(b−1),
E_W=(−√2)^S(−1)^(b−1)/2^(b−1).

Both are nonzero, including when b=1. Their ratio is κ^(b−1). FD therefore proves eventual D_V≠0 and

D_W/D_V=(W(0)/V(0))[E_(W,n)/E_(V,n)+O(1/n)]
=(W(0)/V(0))[κ^(b−1)+o(1)].

The O(1/n) comparison concerns the finite-n coefficient-determinant ratio. It is not asserted as a rate for convergence to κ^(b−1).

It remains necessary to control N, the additional determinant in the full remainder. If J_n=Σ_k u_(n,k)t^k, its root bound gives |u_(n,k)|/n^k≤4^k/k!. Uniform Cauchy bounds for G, together with

n!/(n+k+r+1)!≤n^(−k−r−1),

and the falling-factorial expression for ℓ_j give, for every fixed 0≤j≤b,

|ℓ_j(aJ_nG)|≤C_b|a|n^j/n!.

The sums converge uniformly for sufficiently large n because the Taylor coefficient bound contributes a geometric factor in r and the displayed bound contributes a factorial weight in k.

Expanding N by permutations and summing the column powers j=0,…,b gives

|N|≤C_b(∏_(l=1)^(b−1)|U_l(0)|)|V(0)W(0)|
       · n^[b(b+1)/2]/(n!)^(b+1).

The nonzero FD asymptotic gives the corresponding lower bound

|D_V|≥c_b(∏_(l=1)^(b−1)|U_l(0)|)|V(0)|
        · n^(−S)/(n!)^b

for sufficiently large n. Therefore

N/D_V=(W(0)/V(0))O(n^(b²)|V(0)|/n!).

Finally, the exact formula for V(0), the norm h_n, the bound c_n≤4^n, and |p_k(0)|=|p_k(1)|≤2^(−k/2) imply

|V(0)|≤(2n+1)8^n/√2.

Thus n^(b²)|V(0)|/n!→0, proving that N/D_V is negligible relative to W(0)/V(0).

Combining all exact identities and estimates gives

R(1)/Y=−(D_W+N)/D_V
=−(W(0)/V(0))[κ^(b−1)+o(1)].

Since (1+α_n/b_n)/2→(1−s)/2=κ, this proves the asserted conditional transfer

(−1)^nR(1)/(Yε_n)→κ^b.

The limiting constant is positive. Hence the normalized remainder is eventually nonzero and has sign (−1)^n. The endpoint determinant also establishes eventual one-dimensionality of the projective solution space and Y≠0. Using the separately published ordinary prefactor yields

R(1)/Y=(−1)^n[4π/ρ^(b+1)]ρ^(−2n)(1+o(1)).

Dependencies and evidence: the external FD candidate is work/astra_review_registry/candidates/fixed-size-factorial-determinant-finite-jet-factorization-v1.md, payload SHA-256 6eecc758557e4295ac85093753ee77245492520ce6c0cc0539bc68886a0732f3. The published ordinary prefactor is work/astra_review_registry/verified/worker3-ordinary-pade-prefactor-v1.md, payload SHA-256 e2b926b3f2d184f5cd501ef88d3031968ab3a8fb0bbce0fd456292ef52991aa3. Original formulas were read in work/session_20260913/unequal_degree_hp_attempt.md and work/session_20260927/fixed_exponential_degree_error_theorem.md. The preserved endpoint assembly is work/astra_20260929/worker_3/note_000056.md. Archived PASS labels are not used as independent verification.

Self-audit and limits: this is an author-derived conditional candidate awaiting independent review. FD remains an explicit hypothesis until its separate audit is accepted. The exact projection and complete-tail identities do not require FD. All constants and eventual assertions may depend on fixed b. No statement is made about growing b, attainment of every degree cap, or exact vanishing order at zero. For the actual reduced denominator q of A(1)/Y, the result provides an error asymptotic but no estimate for q. It therefore supplies no complete irrationality proof.