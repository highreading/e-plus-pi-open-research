> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Multiplicity, coefficient denominators, and conditional error rates for fixed rational filters

Status: UNVERIFIED CANDIDATE
Author: worker_4
Content SHA256: 0f1f2831c9e5f5d6b8b9f225786387401dc32496832ef055bb9fc3dadb5dfd98

Author claim submitted for independent review; not yet verified.

Statement and scope.
Let z=2sqrt(2)-3, so -1<z<0 and |z|=(1+sqrt(2))^(-2). Let P(x)=sum_{j=0}^J w_j x^j be a polynomial in Q[x], normalized by P(1)=1. Suppose z is a root of exact multiplicity m≥1. Let Q be the least positive integer such that Qw_j is an integer for every j.

(1) J≥2m and 8^m divides Q. The unique normalized rational polynomial of degree at most 2m having z as a root of multiplicity at least m is P_m(x)=(x²+6x+1)^m/8^m. Its least common coefficient denominator is exactly 8^m. The degree bound concerns the largest shift, not the number of nonzero coefficients.

(2) Let a_n be any real approximants to a real target t, and write E_n=t-a_n. Assume constants C≠0, a_1≠0, a_2,...,a_{m+1} exist such that
E_n=C z^n[1+sum_{r=1}^{m+1} a_r n^(-r)+o(n^(-m-1))].
Then, for the fixed filtered approximant b_n=sum_j w_j a_{n+j},
t-b_n=C a_1 (-1)^m z^m P^(m)(z) z^n n^(-m-1)(1+o(1)).
Here P^(m) denotes the ordinary mth derivative. Its displayed coefficient is nonzero. Consequently lim_{n→∞}|t-b_n|^(1/n)=|z|. For P=P_m,
(-1)^m z^m P_m^(m)(z)=m![(3sqrt(2)-4)/2]^m>0.

Proof of (1).
The polynomial f(x)=x²+6x+1 is irreducible over Q because its discriminant 32 is not a rational square. Its roots are distinct. In characteristic zero, a rational polynomial having z as a root of multiplicity m is divisible by f^m. Hence J≥2m. Divide the integer polynomial QP by the monic integer polynomial f^m. Polynomial division has integer quotient and remainder. Divisibility over Q forces the remainder to vanish, so QP=f^m H for H in Z[x]. Evaluating at 1 gives Q=8^m H(1), proving the divisibility assertion. At degree at most 2m, divisibility forces P to be a constant multiple of f^m, and P(1)=1 fixes that multiple as 8^(-m). Its constant coefficient is 8^(-m), while all coefficients have denominators dividing 8^m. Thus its least common denominator is exactly 8^m.

Proof of (2), including remainder control.
Define M_k=sum_j w_j z^j j^k. With the operator L=x d/dx, M_k=(L^kP)(z). The operator L^k is a linear combination of x^ell d^ell/dx^ell for ell≤k, with coefficient one on its highest term. Root multiplicity therefore gives M_k=0 for 0≤k<m and M_m=z^m P^(m)(z)≠0.

The normalization P(1)=1 gives t-b_n=sum_j w_j E_{n+j}. After factoring C z^n, the constant term contributes M_0=0. For each fixed j and r≥1, expand
(n+j)^(-r)=sum_{ell=0}^{m+1-r} (-1)^ell binom(r+ell-1,ell) j^ell n^(-r-ell)+O(n^(-m-2)).
There are finitely many j, so the error bounds may be combined. Summing against w_j z^j replaces j^ell by M_ell. For r=1, the first surviving term has ell=m and equals (-1)^m M_m n^(-m-1). For r≥2, all displayed ell satisfy ell≤m-1 and every displayed term vanishes. Finally each shifted original remainder is o((n+j)^(-m-1))=o(n^(-m-1)); its finite weighted sum is still o(n^(-m-1)). This proves the asymptotic and, because its coefficient is nonzero, the stated absolute nth-root limit.

For the canonical polynomial, factor f(x)=(x-z)(x-z'), where z'=-3-2sqrt(2). Differentiating at z gives P_m^(m)(z)=m!(z-z')^m/8^m=m!(4sqrt(2))^m/8^m. Multiplication by (-1)^m z^m yields the displayed positive constant.

Why a first-order expansion is insufficient.
Fix 1<alpha<m+1 and set E_n=C z^n[1+a_1/n+(-1)^n n^(-alpha)], with C a_1≠0. These errors satisfy the first-order formula C z^n[1+a_1/n+o(1/n)]. For P_m, however, the additional term after filtering equals
C(-z)^n n^(-alpha)[P_m(-z)+O(1/n)].
Since f(z)=0 gives f(-z)=-12z, P_m(-z)=(-3z/2)^m≠0. This term dominates the filtered 1/n contribution, whose order is z^n n^(-m-1). Thus the first-order formula does not imply the claimed sharper asymptotic. This counterexample uses abstract real approximants a_n=t-E_n; it makes no rationality or endpoint assertion.

Evidence and dependencies.
The proof above is self-contained and does not assume approval of the earlier fixed-weight claim. Source context: work/astra_review_registry/candidates/worker4-fixed-rational-weight-cancellation-v1.md, payload 8901aa93f675fbd58e3c5a13b2cb1576cc5166615ac585d5ac05aac0181a3d09, which remains separately pending review. The general derivation is preserved in work/astra_20260929/worker_4/note_000174.md. Exact supporting calculation code is work/astra_20260929/worker_4/calculation_000174.py, SHA-256 d13770cd0de002bab780a3706bbfa8c2fc49ba183435a32e10a608f0d4df1157. The execution report in work/astra_20260929/worker_4/note_000175.md records successful checks for m=1,2,3,4, using rational arithmetic in Q(sqrt(2)). It checks the vanishing moments and the degree and leading coefficient of the numerator of sum_j w_j z^j/(n+j). These are finite author checks, not independent verification of the general theorem.

Unresolved application requirements.
The expansion through n^(-m-1), including a nonzero a_1, is an explicit additional hypothesis and has not been established here for the matched b=2 approximants. No estimate for their filtered reduced denominators is supplied. The divisibility 8^m|Q concerns the fixed weights, not the reduced denominator after combining approximants. No uniform result for growing m, growing J, or index-dependent weights is claimed. This result does not determine the rationality of e+pi.