> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Sharper coefficientwise truncation and optimal termwise block cutoffs for auxiliary interpolation

Status: Independently reviewed research result (AI review; not formal verification)
Author: worker_1
Reviewer: worker_4
Content SHA256: 2757da21024783fba7cd9c881de89c14db59b114a26787209ef0e639b8130799
Review: work/astra_review_registry/reviews/odd-prime-interpolation-tail-cutoff-v1-worker_4.md

STATUS: Unverified candidate submitted for independent review. This concerns auxiliary interpolation only.

Definitions and hypotheses. Let p be an odd prime, d≥1 an integer, a∈{0,...,p−1}, and r≥0 an integer. Write (X)_[m]=∏_{j=0}^{m−1}(X−j), with (X)_[0]=1. Consider

D_r(X)=Σ_{b,c≥0} (−1)^b (X)_[b+2c+r](X)_[b+c]/(2^c b!c!).

After substituting X=a+pT, let v_G be the minimum p-adic valuation of the coefficients of a polynomial. Coefficientwise divisibility of a restricted power series means that every coefficient has the stated divisibility.

Claim 1: Explicit sufficient cutoff. Set

K_p(d)=max(1,ceil((p−1)(d−1)/(p−2))).

The displayed series converges in the Gauss norm to an element of Z_p⟨T⟩. Deleting all summands with b+2c≥pK_p(d) changes it by an element of p^d Z_p⟨T⟩. The bound is uniform in a and r. In particular, for p=3, retain b+2c<3 when d=1, and b+2c<6d−6 when d≥2. Thus cutoff 6 suffices modulo 9.

Proof. Put m=b+2c, s=b+c, k=floor(m/p), and h=floor(s/p). For any length t, each factor a+pT−j has Gauss valuation 1 if j≡a mod p and 0 otherwise. Multiplicativity of the Gauss valuation therefore gives

v_G((a+pT)_[t])=#{0≤j<t:j≡a mod p}≥floor(t/p).

Because p is odd, 2^c is a unit. Since binom(s,b) is an integer, v_p(b!)+v_p(c!)≤v_p(s!). Legendre's formula gives v_p(s!)=h+v_p(h!). Consequently each summand has valuation at least

k+h−v_p(s!)=k−v_p(h!)≥k−v_p(k!)=:L_p(k).

For k≥1, the base-p digit-sum identity gives

L_p(k)=((p−2)k+s_p(k))/(p−1)≥((p−2)k+1)/(p−1).

If k≥K_p(d), this lower bound is strictly greater than d−1. Since L_p(k) is an integer, it is at least d. The bound tends to infinity with k, and only finitely many pairs (b,c) have bounded m. Thus the series converges in the Gauss norm and its omitted tail belongs to p^d Z_p⟨T⟩. This proves Claim 1 without a monotonicity assumption on L_p.

Claim 2: Exact optimal block cutoff for individual-summand certificates. Define

K*_p(d)=1+max{k≥0:L_p(k)<d}.

The maximum exists, since L_p(0)=0<d and Claim 1 bounds all bad indices by K_p(d)−1. Among integer block cutoffs pK, K*_p(d) is the smallest K such that every summand with b+2c≥pK is coefficientwise divisible by p^d, uniformly over all the stated disks and r≥0. It can be computed by checking only 0≤k<K_p(d).

Proof of optimality. Sufficiency follows from the termwise bound. For necessity take a=p−1, r=0, c=0 and b=pk. Exactly k factors in (a+pT)_[pk] have Gauss valuation 1. The corresponding summand has exact valuation

2k−v_p((pk)!)=k−v_p(k!)=L_p(k).

If K<K*_p(d), choose k=K*_p(d)−1. This summand lies in the omitted range and fails the required divisibility. This proves optimality for individual-summand certificates. It does not establish a minimal cutoff for the summed tail, whose terms can cancel.

Evidence and source dependencies. The interpolation definition and previously audited coefficientwise estimate occur in work/session_20260927/literature_update_and_b2_analytic_certificate.md and work/astra_20260929/worker_1/note_000012.md. Preliminary cutoff refinements were recorded in work/astra_20260929/worker_1/note_000022.md and work/astra_20260929/worker_1/note_000024.md. The derivation above supplies the necessary valuation and convergence arguments explicitly. The returned worker_1 step-24 calculation reported passing finite checks for primes 3,5,7,11 and d=1,...,128, plus 117 coefficientwise ternary checks with minimum valuation 2. These finite results corroborate the argument and are not its proof.

Scope and unresolved dependencies. Independent review is required before publication as verified research. The claims do not prove that auxiliary maximal minors have no common zeros on other residue disks, estimate primitive endpoint cancellation or actual reduced denominators, establish asymptotic prefactors, or resolve the rationality of e+pi.