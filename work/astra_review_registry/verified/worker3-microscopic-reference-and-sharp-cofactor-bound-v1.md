> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Quantitative microscopic reference estimates and a sharper fixed-degree endpoint cofactor bound

Status: Independently reviewed research result (AI review; not formal verification)
Author: worker_3
Reviewer: worker_2
Content SHA256: 48241943005ab30cb868e89f6e9927046c2fa5a6f81ea94e10f38e5155682718
Review: work/astra_review_registry/reviews/worker3-microscopic-reference-and-sharp-cofactor-bound-v1-worker_2.md

Status: UNVERIFIED CANDIDATE, awaiting independent review. Author: worker_3.

Scope. This claim audits the analytic reference and additional-cofactor estimates used in the fixed-degree endpoint construction. It proves quantitative reference estimates directly from the original recurrence, verifies the normalized endpoint factors, and proves a factorial determinant upper bound. The endpoint denominator lower bound explicitly uses the separately published factorial-determinant theorem. The ordinary-error ratio explicitly uses the separately published ordinary Padé prefactor. No reduced-denominator estimate, growing-degree uniformity, or irrationality conclusion is claimed.

1. Original normalization and zero control.

Define p_0(t)=1, p_1(t)=t−1/2, and
p_(m+1)(t)=(t−1/2)p_m(t)+β_m p_(m−1)(t),
β_m=m²/[4(4m²−1)], m≥1.
These are precisely the monic polynomials in the original endpoint system:
p_m(t)=i^m P_m(−i(2t−1))/c_m, c_m=binom(2m,m),
where P_m is the Legendre polynomial with P_m(1)=1. Substitution into the Legendre recurrence verifies the recurrence and initial values.

Let S_m be the real symmetric tridiagonal matrix with zero diagonal and successive off-diagonal entries sqrt(β_1),…,sqrt(β_(m−1)). Set J_m=(1/2)I+iS_m. Characteristic-determinant expansion gives p_m(t)=det(tI−J_m). Consequently every zero has real part 1/2. In particular all reciprocal roots have modulus at most 2.

Put q_m(t)=p_m(t)/p_(m+1)(t). This q_m is an analytic polynomial quotient, not a reduced arithmetic denominator. It is the last diagonal entry of (tI−J_(m+1))^(−1). Normality of J_(m+1) therefore gives
sup_(|t|≤r)|q_m(t)|≤1/(1/2−r), r<1/2.
Neither its numerator nor its denominator vanishes on these disks. On |t|≤1/10, the bound is 5/2. The recurrence gives
q_m=1/(t−1/2+β_m q_(m−1)).
Since β_m≤1/12,
|1/q_m(t)|≤3/5+(1/12)(5/2)=97/120, m≥1.
The bound for q_0 is 3/5. Thus |q_m(t)|≥120/97 uniformly, including m=0. Analytic quotients and logarithmic derivatives introduce no uncontrolled small denominator.

2. Quantitative consecutive-quotient convergence.

Use the supremum norm on |t|≤1/10. Subtracting two consecutive recurrences gives, for m≥2,
d_m≤(25/48)d_(m−1)+(125/8)|β_m−β_(m−1)|,
d_m=||q_m−q_(m−1)||.
Indeed the product of the two outer quotients is bounded by 25/4, and the remaining quotient by 5/2. The β_m decrease to 1/16, so their successive differences are summable. Summing the displayed contraction proves Σ d_m<∞. Hence q_m converges uniformly to an analytic, nonvanishing q satisfying
q(t)(t−1/2+q(t)/16)=1.

Let ρ=1+sqrt(2), a=ρ/4, and
f(t)=[1−2t+sqrt((1−2t)²+1)]/ρ,
with the square root positive at zero. The negative values q_m(0), together with the uniform lower bound, select
q(t)=−1/[a f(t)].
Here f(0)=1 and f′(0)=−sqrt(2).

Writing e_m=||q_m−q|| and subtracting the fixed-point equation gives
e_m≤(25/48)e_(m−1)+(125/8)|β_m−1/16|,
β_m−1/16=1/[16(4m²−1)].
Iteration yields e_m=O(m^−2): split the geometric convolution at m/2; the early part is exponentially small and the late part is bounded by a constant times m^−2. Cauchy's formula gives the same rate for every fixed derivative on a smaller fixed disk.

3. Microscopic estimate and coefficient majorant.

Put U_n=p_(n+1) and F_n=U_n/U_n(0). On a fixed smaller disk define analytic logarithms
L_j(t)=log(q_j(0)/q_j(t)), L_j(0)=0.
Their second derivatives are uniformly bounded by the preceding upper and lower bounds and Cauchy's formula. Also
L_j′(0)=−sqrt(2)+O(j^−2), j≥1.
Therefore
Σ_(j=0)^n L_j′(0)=−sqrt(2)(n+1)+O(1).

The product telescopes exactly:
F_n(t)=∏_(j=0)^n q_j(0)/q_j(t).
For every fixed R and |z|≤R, Taylor expansion with the uniform second-derivative bound gives
log F_n(z/n)=−sqrt(2)z+O_R(n^−1).
Consequently
F_n(z/n)=exp(−sqrt(2)z)(1+O_R(n^−1))
uniformly on every fixed complex disk, and hence on every fixed compact set. Summability of the derivative errors is the justification for the quantitative product estimate.

If F_n(t)=Σ_k u_(n,k)t^k, the reciprocal-root bound gives
|u_(n,k)|≤binom(n+1,k)2^k,
|u_(n,k)|/n^k≤4^k/k!, n≥1.
This coefficient majorant is independent of the microscopic convergence argument.

For fixed k≥0 define
G_(n,k)(t)=[p_(n+1+k)(t)/p_(n+1+k)(0)]/F_n(t).
Its exact expression is
G_(n,k)(t)=∏_(j=n+1)^(n+k) q_j(0)/q_j(t).
The product is empty when k=0. Uniform quotient bounds and the O(n^−2) convergence prove
G_(n,k)=f^k+O_k(n^−2)
on a fixed smaller disk, with the same rate for each fixed Taylor coefficient. No assertion is made when k grows with n.

4. Endpoint factors and their amplitudes.

Use the original functional and norms
ℒ(P)=∫_(−1)^1 P((1+iu)/2)du,
h_n=ℒ(p_n²)=2(−1)^n/[(2n+1)c_n²],
χ_n=ℒ(p_n/(1−t)).
Let
V(t)=Σ_(k=0)^n p_k(t)p_k(1)/h_k,
W(t)=1/(1−t)−Σ_(k=0)^n χ_k p_k(t)/h_k.
These definitions match the original endpoint construction.

The recurrence and h_n/h_(n−1)=−β_n give Christoffel–Darboux by telescoping. With b_n=p_(n+1)(1)/p_n(1) and α_n=χ_(n+1)/χ_n, its consequences are
V(t)=p_n(1)[U_n(t)−b_np_n(t)]/[h_n(t−1)],
W(t)=[χ_nU_n(t)−χ_(n+1)p_n(t)]/[h_n(1−t)].
For the second identity, integrating the kernel gives
p_(n+1)(1)χ_n−p_n(1)χ_(n+1)=h_n.
Thus subtracting the displayed expression for W from 1/(1−t) produces a polynomial of degree at most n. The displayed W has zero moment against each polynomial of degree at most n: write that polynomial as Q(1)+(t−1)S(t) and apply orthogonality. This identifies its complement with the defining projection polynomial.

Symmetry gives p_m(0)=(−1)^m p_m(1), while the recurrence at t=1 gives p_m(1)>0. Consequently
V(0)=−2p_n(1)U_n(0)/h_n>0,
b_n=−1/q_n(0).
Define ε_n=(−1)^nχ_n/p_n(1). Orthogonality gives
ε_n=2/[c_n²p_n(1)²] ∫_(−1)^1 P_n(u)²/(1+u²)du>0.
The published ordinary Padé prefactor implies
ε_n∼(4π/ρ)ρ^(−2n), hence ε_(n+1)/ε_n→s=ρ^−2.
It follows exactly that
α_n/b_n=−ε_(n+1)/ε_n,
W(0)/V(0)=(−1)^(n+1)ε_n(1+α_n/b_n)/2.
Thus W(0)≠0 eventually, since 1+α_n/b_n→1−s>0.

The exact normalized factors are
V=V(0)F_n G_(V,n),
G_(V,n)=[1−b_nq_n(t)]/[2(1−t)],
W=W(0)F_n G_(W,n),
G_(W,n)=[1−α_nq_n(t)]/[(1+α_n/b_n)(1−t)].
All are analytic and uniformly bounded on one fixed smaller disk for sufficiently large n. This follows from the quotient bounds, b_n→a, α_n→−as, and the denominator bounded away from zero.

The fixed-point equation gives
1−t=a(f+1)(f−s)/f, a(1−s)=1/2.
Therefore
G_(V,n)→G_V=(1−s)/(f−s),
G_(W,n)→G_W=2/(f+1)
uniformly on that disk. The first convergence has rate O(n^−2). For the second, only convergence is asserted: the quoted ordinary prefactor supplies no O(n^−2) error-ratio estimate by itself.

5. Hypotheses for the denominator determinant.

Fix b≥1 and n≥b. For 0≤j≤b define precisely
ℓ_j(t^r)=1/(n+r+1−j)!, r≥0.
For analytic germs, extend by their absolutely convergent coefficient sums. Let the b−1 high rows be P_l=p_(n+l), 1≤l≤b−1. The list is empty for b=1. Define row vectors e=(1,…,1), v=(ℓ_j(V)) and w=(ℓ_j(W)), and
D_V=det[(ℓ_j(P_l)); e; v],
N=det[(ℓ_j(P_l)); v; w].
These are the original denominator and additional-remainder determinants, with the same row order and factorial indices.

For the difference functionals Δ_j=ℓ_(j+1)−ℓ_j, column subtraction and expansion along e give
D_V=(−1)^(b+1)det(Δ_j(P_i)),
where the remaining rows, in order, are P_1,…,P_(b−1),V and j=0,…,b−1.

The published factorial-determinant theorem applies with determinant size b, reference polynomial U_n, normalized reference F_n, and microscopic parameter sqrt(2). Its hypotheses have now been checked individually: degree n+1; reference value nonzero; reciprocal-root bound 2; compact-uniform microscopic convergence; nonzero row amplitudes P_l(0),V(0); and uniformly bounded analytic factors on a common fixed disk. The analogous W family has an eventually nonzero amplitude as well.

The high-row factors converge to 1,f,…,f^(b−2). Write S=b(b−1)/2. The limiting Taylor coefficient determinant for these rows and G_V, using columns of degrees 0,…,b−1, is
E_V=(−sqrt(2))^S (−1)^(b−1)/(1−s)^(b−1)≠0.
For the W family it is
E_W=(−sqrt(2))^S (−1)^(b−1)/2^(b−1)≠0.
To check these formulas, change variables to x=f−1. This multiplies the determinant by f′(0)^S. The polynomial rows (1+x)^j have triangular coefficient matrix with diagonal 1; the last required coefficients of (1−s)/(1−s+x) and 2/(2+x) are the displayed ones. For b=1 both determinants equal 1.

The published theorem therefore gives, for sufficiently large n,
|D_V|≥c_b [∏_(l=1)^(b−1)|P_l(0)|] |V(0)| (n!)^(−b)n^(−S),
with c_b>0. This is the only asymptotic determinant theorem needed for the following relative cofactor estimate. No convergence rate for E_W is required.

6. A general full-factorial-determinant bound.

Fix d≥1. Suppose F_n is a polynomial with |[t^k]F_n|≤(Cn)^k/k! for a constant C, and P_i=a_iF_nG_i, where the G_i are uniformly bounded and analytic on a common fixed disk. Define T_j(t^m)=1/(n+m+1−j)!, j=0,…,d−1. Then, for sufficiently large n,
|det(T_j(P_i))|≤C_d [∏_i|a_i|](n!)^(−d)n^(−d(d+1)/2).
Constants can depend on d, the coefficient majorant, and the common analytic bounds.

Proof. Write G_i=Σ_r g_(i,r)t^r, with |g_(i,r)|≤M R^−r by Cauchy's bound on a fixed circle. For nonnegative integers x_i, the exact factorial identity is
det(1/(n+x_i+1−j)!)_(i=1,…,d;j=0,…,d−1)
=∏_(i<h)(x_h−x_i)/∏_i(n+x_i+1)!.
Indeed, after extracting the row denominators, column j is the monic falling-factorial polynomial of degree j evaluated at n+x_i+1.

Expand each row t^(r_i)F_n using indices k_i and set x_i=r_i+k_i. Use
n!/(n+x_i+1)!≤n^(−x_i−1),
|∏_(i<h)(x_h−x_i)|≤∏_i(1+x_i)^(d−1).
The sums over k_i are bounded by a constant times ∏_i(1+r_i)^(d−1), because Σ_k C^k(1+k)^(d−1)/k! converges. Thus
|det(T_j(t^(r_i)F_n))|
≤C_d(n!)^(−d)n^(−d−Σr_i)∏_i(1+r_i)^(d−1).

Cauchy–Binet applied to the Taylor expansion of the G_i leaves only strictly increasing shifts 0≤r_1<…<r_d; repeated shifts have identical rows and vanish. The accompanying coefficient determinant is bounded by d! M^d R^(−Σr_i). Since Σr_i≥d(d−1)/2, summing these bounds gives an additional factor O(n^(−d(d−1)/2)). More explicitly, put r_i=i−1+h_i and drop the ordering restriction on the nonnegative h_i; the resulting products of polynomially weighted geometric sums are uniformly bounded for nR≥2. This also proves absolute convergence of the expansions. The asserted exponent d(d+1)/2 follows. This proof uses no microscopic limit.

7. Sharper cofactor normalization.

Apply the preceding bound to N with d=b+1, common reference F_n, and amplitudes
P_1(0),…,P_(b−1)(0),V(0),W(0).
The coefficient majorant from section 3 has C=4. The required analytic bounds were proved in section 4. Hence
|N|≤C_b [∏_(l=1)^(b−1)|P_l(0)|] |V(0)W(0)|
×(n!)^(−b−1)n^(−(b+1)(b+2)/2).
Divide by the denominator lower bound in section 5. Since
[(b+1)(b+2)−b(b−1)]/2=2b+1,
we obtain
|N/D_V|≤C_b |W(0)|/[n! n^(2b+1)],
or equivalently
|(N/D_V)/(W(0)/V(0))|≤C_b |V(0)|/[n! n^(2b+1)].
This includes b=1 and retains the exact normalization relative to the principal error amplitude W(0)/V(0).

Finally, the Legendre zeros lie in (−1,1), so the zeros of p_m lie on the segment (1+iu)/2, |u|<1. Therefore |p_m(1)|≤2^(−m/2). Combining the exact V(0) formula with c_n≤4^n gives
|V(0)|≤(2n+1)8^n/sqrt(2).
Thus the relative additional cofactor tends to zero factorially for every fixed b. This improves the earlier sufficient bound with factor n^(b²), while leaving the unresolved arithmetic denominator problem unchanged.

Dependencies and evidence. The original recurrence, moment normalization, and factorial indices are in work/session_20260927/fixed_exponential_degree_error_theorem.md and work/session_20260913/unequal_degree_hp_attempt.md. The audited supplements are work/astra_20260929/main/note_000114.md and work/astra_20260929/main/note_000118.md; both were read completely. The separately published determinant dependency is work/astra_review_registry/verified/fixed-size-factorial-determinant-finite-jet-factorization-v1.md, payload SHA-256 6eecc758557e4295ac85093753ee77245492520ce6c0cc0539bc68886a0732f3. The separately published ordinary prefactor is work/astra_review_registry/verified/worker3-ordinary-pade-prefactor-v1.md, payload SHA-256 e2b926b3f2d184f5cd501ef88d3031968ab3a8fb0bbce0fd456292ef52991aa3. The exact endpoint assembly is also preserved in candidate worker3-fixed-b-matched-endpoint-transfer-conditional-v1, payload SHA-256 48ed273001a125bce2ec58f5ce053cf10340c71cd64373fde3fc356852bc6601; the supplied registry records its approval, with publication pending.

Self-audit. The recurrence estimates, zero bounds, microscopic rate, coefficient domination, and general determinant upper bound are proved here. The endpoint denominator lower bound invokes the named published theorem only after checking its application hypotheses. The W-factor limit invokes the named ordinary-error ratio and claims no unjustified convergence rate. This audit does not independently reapprove either published dependency or the full endpoint projection theorem. All constants and eventual assertions may depend on fixed b or d. No new numerical computation or archived PASS assertion is used. Independent review of this exact new claim remains required.