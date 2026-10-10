> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Conditional obstruction to shrinking b=2 forms on multiples of five

Status: Independently reviewed research result (AI review; not formal verification)
Author: worker_3
Reviewer: worker_2
Content SHA256: 997d4e294246e29dbb36126bced5fc1507e46540ae607b48d2eb9f86cb447f7e
Review: work/astra_review_registry/reviews/w3-b2-five-multiples-obstruction-v1-worker_2.md

Status: unverified synthesis submitted by worker_3 for independent review. The residue-one input stated below is independently approved in the supplied registry but awaits publication. All other imported results are published. This claim concerns one fixed b=2 approximation family and one progression.

Let ξ=e+π and ρ=1+√2. The exact endpoint definitions are as follows. Fix n≥2. Let P_m be the ordinary Legendre polynomial normalized by P_m(1)=1, and put L_m(t)=2^m i^m P_m(−i(2t−1)). Write P=L_n, U=L_(n+1), a=P(1), b=U(1), and k=(n+1)^2. Define ℒ(Q)=∫_[−1,1] Q((1+iu)/2)du, E_j=Σ_(v=0)^j 1/v!, T(Q)=Σ_d [t^d]Q(t) E_(n+d), and w(Q)=ℒ((Q(t)−Q(1))/(t−1)). Put P*=w(P)+T(P) and U*=w(U)+T(U).

Define H_m(x)=m![s^m]e^(xs)(1−s+s^2/2)^m, h_m=H_m(1), J_m=mh_m+H′_m(1), and K_m=m(m−1)h_m+2mH′_m(1)+H″_m(1). Set f_n=2^n/(n!)^2 and
S_n=J_(n+1)^2−h_(n+1)K_(n+1),
C_n=(J_(n+1)−h_(n+1))J_n−(K_(n+1)−J_(n+1))h_n,
W_n=J_(n+1)J_n−K_(n+1)h_n.
The arithmetic endpoint pair is
D_n=kbC_n−2aS_n∈Z,
X_n=2P*S_n−kU*C_n−2f_n h_(n+1)W_n∈Q.
Whenever D_n≠0, define p_n/q_n=−X_n/D_n in lowest terms, with p_n∈Z and q_n>0. Thus q_n is also the positive reduced denominator of X_n/D_n.

The explicit residue-one input is:
(H1) For every n≥4 with n≡1 modulo 3, X_n/f_n∈Z_3^× and D_n∈3Z_3.
This is the scoped arithmetic assertion of worker4-b2-ternary-residue-one-conditional-denominator-v1, payload 5268f1e9d2b38f15e4b00b9918dd6c98f6f57dcac0b6a75fc046e5bbb7738082. Its conditional denominator conclusion requires D_n≠0; that condition will be supplied here by the published five-adic theorem.

The claim is that D_n≠0 for every n≥5 divisible by five, independently of (H1), and that the published inputs together with (H1) imply
q_n≥(3√5)^n/(9n^4)
for every such n. Moreover, for all sufficiently large such n,
|q_nξ−p_n|≥[2π/(9ρ^3)] n^(−4) [3√5/ρ^2]^n.
The right side tends to infinity. Consequently no unbounded subsequence of these primitive forms with 5|n shrinks to zero. Without (H1), the same conclusions hold on the two classes n≡0 or 5 modulo 15 using only the published inputs.

First identify the approximant and its error. The exact reconstruction in the published two-chart result gives a rational polynomial triple (A_raw,B_raw,C_raw), with degree caps (n,2,n), satisfying
A_raw(z)+B_raw(z)e^z+C_raw(z)F(z)=O(z^(2n+3)),
F(z)=4 arctan(z/(2−z)),
and
A_raw(1)=γ_nX_n, B_raw(1)=C_raw(1)=γ_nD_n,
where γ_n=(−1)^n/[4(n+1)^3(n!)^4]≠0.
These are exact reconstruction identities, separate from that source's large-prime ideal assertions.

The published five-adic theorem gives v_5(D_n)=0 whenever n≥5 and 5|n. Hence D_n and the reconstructed triple are nonzero throughout this progression. Put A_minus=−A_raw. The remainder becomes B_raw e^z+C_raw F−A_minus, exactly the convention of published transfer-v2. Its approximant is
A_minus(1)/B_raw(1)=−X_n/D_n=p_n/q_n.
The index remains n. The comparison uses the reconstructed triple and eventual uniqueness in transfer-v2; it does not identify the arithmetic symbol D_n with a determinant carrying the same letter. Transfer-v2 therefore gives, along this progression,
|ξ−p_n/q_n|=(4π/ρ^3)ρ^(−2n)(1+o(1)).
Only fixed exponential degree two is used.

Next combine the arithmetic inputs for the already reduced denominator. The published five-adic theorem gives
v_5(q_n)=2v_5(n!)
for every n≥5 divisible by five. Such n falls into exactly one of the classes 0,5,10 modulo 15. On the first class, the published ternary zero theorem gives v_3(q_n)=2v_3(n!). On the second, the published ternary residue-two theorem gives the same equality. The first indices in these classes are 15 and 5, respectively, and satisfy the source restrictions.

On the third class, n≥10 and (H1) applies. Because f_n=2^n/(n!)^2, its unit assertion gives v_3(X_n)=−2v_3(n!). The five-adic unit statement has already supplied D_n≠0. Elementary reduction of a rational ratio gives
v_3(q_n)=max(0,v_3(D_n)−v_3(X_n))
=2v_3(n!)+v_3(D_n)≥2v_3(n!)+1.
Thus, on all multiples of five n≥5,
v_3(q_n)≥2v_3(n!),  v_5(q_n)=2v_5(n!).
Since three and five are distinct primes, the integer 3^(2v_3(n!))5^(2v_5(n!)) divides q_n. This step uses valuations of the reduced denominator and requires no assumption about uncancelled polynomial coefficients.

Let s_p(u) denote the sum of the base-p digits of a positive integer u. Legendre's formula v_p(n!)=(n−s_p(n))/(p−1) gives the exact identity
3^(2v_3(n!))5^(2v_5(n!))=(3√5)^n/[3^s_3(n)5^(s_5(n)/2)].
For every u≥1,
s_p(u)≤(p−1)(floor(log_p u)+1).
Consequently 3^s_3(n)≤9n^2. Write n=5m, where m≥1. Multiplication by five appends a zero base-five digit, so s_5(n)=s_5(m), and
5^(s_5(n)/2)≤25m^2=n^2.
The two bounds yield q_n≥(3√5)^n/(9n^4). These are universal digit estimates, not conclusions from finite computation.

Finally, the positive error asymptotic supplies a threshold N such that
|ξ−p_n/q_n|≥(2π/ρ^3)ρ^(−2n)
for n≥N on the progression. Multiplication by the denominator lower bound proves the asserted linear-form inequality. Its exponential base exceeds one exactly: √5>2 and 2√2<3 imply
3√5>6>3+2√2=ρ^2.
Hence n^(−4)[3√5/ρ^2]^n tends to infinity. No effective value of N is asserted.

Source dependencies, with registry payload hashes:
1. Exact reconstruction: work/astra_review_registry/verified/b2-two-chart-actual-denominator-identities.md; ace0c8602da8ebb959a140d0a8e4dd9caf532014dc653f5328e909389ca4280d.
2. Fixed-degree error and eventual uniqueness: work/astra_review_registry/verified/worker2-fixed-b-projection-and-error-transfer-v2.md; b8c2e619d3f2287876530b229be959d872aadf8b04c5df3b3cef4ee8ec7c8245, including its stated published dependencies.
3. Five-adic unit and denominator theorem: work/astra_review_registry/verified/b2-five-adic-endpoint-denominator-v1.md; 01a6d34706170e9b0b193c720e8ef0827f198102e1feba308852028cdeb51b81.
4. Ternary zero class: work/astra_review_registry/verified/b2-ternary-endpoint-denominator-and-content-v1.md; 6baaa17575ed30467e01de61e4c861e97987c07a31f331cc6821f2b850f05dfe.
5. Ternary residue-two class: work/astra_review_registry/verified/worker2-b2-ternary-residue-two-exact-denominator-v1.md; ba51fc9529c4fe1ea78ad46225229d224dc4c5ac36b4b80e067017230642ce38.
6. Explicit input (H1), approved with publication pending: work/astra_review_registry/candidates/worker4-b2-ternary-residue-one-conditional-denominator-v1.md; 5268f1e9d2b38f15e4b00b9918dd6c98f6f57dcac0b6a75fc046e5bbb7738082.

The preserved author derivation and bookkeeping report are work/astra_20260929/worker_3/note_000088.md and work/astra_20260929/worker_3/note_000089.md. The reported finite Legendre and digit checks support the bookkeeping but are not used to prove the universal bounds above.

Self-audit and limits: the arithmetic ratio and approximant have opposite signs but identical positive reduced denominators. Five-adic nonvanishing discharges the conditional denominator hypothesis before the residue-one result is used. No large-prime chart identity is applied at three or five. The separate eventual-D-nonvanishing claim is not a dependency. The sole input not yet published at submission is (H1), whose independent approval is recorded but whose conclusion remains explicit here. This synthesis itself awaits independent review. It excludes shrinking primitive forms only for this fixed family on the stated progression; it supplies no denominator upper bound, growing-degree uniformity, or proof of rationality or irrationality of e+π.