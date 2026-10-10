> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact complete-error interface for unshifted M22

Author: Agent 3, 2026-10-02. This completes the conditional analytic interface requested before moving to a separately gated growing-shift target. The unconditional signed normalization is in PAIRED_DERANGEMENT_SIGNED_NORMALIZATION.md. Root's arithmetic matching and final content remain separate.

Use n=2k-1, k>=2, with the positive-leading normalization of q_n. Set lambda=q_n(-1)>0 and

    d sigma(y)=[exp(sqrt(y))+4/(1+y)]dy/[2sqrt(y)],   0<y<1,
    J_{ij}=integral_0^1 y^{i+j}q_n(y)/lambda d sigma(y),
    v=(1,-1,...,(-1)^{k-1})^T.

The ACTUAL mixed exponential/arctangent matrix is H=lambda J=R+S lambda vv^T, S=e+pi. Its rational affine determinant is a_k+b_k S, and the actual rational center is -a_k/b_k when b_k!=0. The rank-one identity gives

    b_k=lambda^k v^T adj(J) v,
    S-c_k=det(J)/[v^T adj(J)v].                    (1)

This remains valid even if J is singular, provided the displayed cofactor is nonzero. If J is invertible, it becomes 1/[v^T J^{-1}v]. Both rational endpoint contributions are included throughout.

If q_n is strictly positive on [0,1], then J is positive definite, both determinants/cofactors are nonzero, and

    0<S-c_k=min_{deg p<k, p(-1)=1} integral_0^1 p(y)^2 q_n(y)/lambda d sigma(y).  (2)

This is the standard Christoffel variational identity, applied to the actual compact measure only under the stated positivity hypothesis. Testing the scaled Chebyshev polynomial gives

    0<S-c_k <= (S-1) sup_{[0,1]}[q_n/lambda]/T_{k-1}(3)^2.

Thus subexponential growth of that scalar supremum, together with compact positivity, would give exponential complete convergence with rate at least 4 log(1+sqrt(2)) per k. Neither hypothesis is established uniformly here. The positive pushforward mu, the unique negative exterior scalar root, and q_n(-1)>0 do not establish them.

Small new exact scalar diagnostics in PAIRED_SIGNED_SCALAR_DIAGNOSTICS.json confirm no roots in (0,1) for n=3,5,7,9,15. The attempted larger Sturm computation was stopped because it was expensive and would not prove the all-degree interface. No infinite sign, center convergence, determinant asymptotic, or primitive-form smallness is inferred from those finite results.

Additional bounded archive searches for signed Christoffel/Freud overlap found the different complex-segment fixed-weight construction in session_20261001_astra/agent1/FIXED_WEIGHT_CHRISTOFFEL_RESEARCH.md. Its alternating signed norms and complete companion estimates are not this compact M22 matrix. Fresh primary searches included `orthogonal polynomials weight "exp(-|x|)" asymptotics` and `orthogonal polynomials "exponential weight" "log n" "origin"`. The primary Chen--Lawrence paper *Small eigenvalues of large Hankel matrices*, https://arxiv.org/pdf/math/0009238, was opened in full; its main theorem is for exp(-y^beta), beta>1/2, with the beta=1/2 point treated as critical. It does not supply the uniform signed compact Gram estimate needed in (1), and is not being imported as a proof.

The fixed unshifted complete sign/convergence remains OPEN. The next original target changes the scalar moment shift and will prove its own actual positivity rather than filling this gap by assumption. No claim about rationality of S is made.
