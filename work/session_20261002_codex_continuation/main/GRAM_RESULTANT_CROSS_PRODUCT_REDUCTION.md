> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A normalized cross-product reduction of the canonical Gram resultant

Root original deduction, 2026-10-02. This records progress on M1 without asserting the missing subfactorial gcd estimate.

## 1. Novelty boundary and sources

The inherited `CANONICAL_EXCEPTIONAL_DEFICIT_CONTENT.md` factors the binary resultant into reconstruction content, quadratic content and a positive primitive resultant. `CANONICAL_FACTORIAL_DEFICIT_LOCAL_GEOMETRY.md` reduces the factorial deficit to a primitive linear congruence. Both global valuation sums remain unproved. Searches of those papers and the contiguous/companion papers did not locate the explicit normalized cross-product identity below.

Primary-paper searches covered Gram/Hermite-Pade gcds, recurrence resultants, and factorial reduction. Opened Elimelech et al., *Algorithm-assisted discovery of an intrinsic order among mathematical constants*, PNAS 121 (2024), e2321440121, primary full text https://arxiv.org/html/2308.11829v2. Section 2.1 describes factorial reduction as a search heuristic and conjectural signature, not a theorem applicable to this selector. Opened the existing e+pi audit at https://arxiv.org/html/2606.17303v1; it is already in the archive. No black-box subfactorial content bound was found for these Gram quotients. The linear algebra below is classical; only its application/normalization is new to this ledger.

## 2. Normalized data

Use Agent 1's exact normalized definitions N=M/2^n, H=Krec^T Omega Krec, D0=diag(1,n+1,d), d=(n+1)(n+2). They retain the full endpoint. Write Delta_N=det N and

    Jpair=[[4(n+2),0],
           [2(n+2),n+2],
           [2(n+1),2n+3]],
    Ypair=adj(N) D0 Jpair=[y0 y1].

For any column w in Q^3, the unprimitive binary quadratic and row are

    B(X,Y)=(X y0+Y y1)^T H (X y0+Y y1),
    ell=(w^T y0,w^T y1).

Let K_i be the actual integral direct Rodrigues kernel for the selector t^i, so K_i(1)=J_i. Put the full logarithmic moment column

    B_i=calL((K_i-J_i)/(t-1)), i=0,1,2,
    theta_hat=L H adj(N) D0 B.

Here L clears every B_i, and the normalized selector is zhat=D0 adj(N)^T H Y. Thus beta=Y^T H adj(N)D0 B/D, exactly. The actual complete rational numerator, after multiplication by F L D, has this form with

    w=2^n L[H adj(N) A+Delta_N k0^T]+F theta_hat,

where F=(n!)^2. The factors 2^n,F,L and both complete companions are retained; no substitute pure logarithmic numerator is used.

## 3. Cross-product identity

Set m=y0 cross y1 and z=m cross w. By the vector triple-product identity,

    z=-(w^T y1)y0+(w^T y0)y1.

Since a binary quadratic evaluated on the kernel of a linear row is its resultant with that row, the exact unprimitive resultant is

    Res(B,ell)=z^T H z.                              (1)

The adjugate identity for a three-dimensional cross product gives

    m=Delta_N N^T[(D0 j0) cross (D0 j1)].

A direct multiplication of the displayed two endpoint columns yields

    (D0 j0) cross (D0 j1)=gamma_n v_n,
    gamma_n=4(n+1)(n+2)^2,
    v_n=(d/2,-(2n+3),1)^T.

Therefore

    Res(B,ell)
      =gamma_n^2 Delta_N^2
       [(N^T v_n cross w)^T H (N^T v_n cross w)].     (2)

These are polynomial identities and extend to singular N; nonsingularity is only needed when identifying the actual normal center. For rational normalized coefficients they hold in Z[1/2] after retaining the selected integer moment clearer.

## 4. What the identity removes and what it does not

The determinant-squared factor in (2) is forced before any evaluation at (P_n,P_(n+1)). It isolates the same response-lattice normal direction N^T v_n that occurs in the archived Smith-factor formula. The primitive resultant is obtained only AFTER division by the actual quadratic and row contents. Thus (2) supplies a computable raw factor, and gives a shorter exact contraction than expanding a binary quadratic plus two row coefficients separately.

It does not prove that Delta_N^2 survives in the primitive resultant, that the quotient has subfactorial height, or that the final cancellation depth is small. Those claims would require a uniform comparison with k_C,k_R,abar_B and the complete row content. Positivity of H over R also does not prevent arbitrary divisibility at an odd prime. The unresolved factorial congruence from the previous paper is preserved.

M1 has produced the explicit factorization (2), but its desired global subfactorial estimate remains open. This is a working mathematical record, not permission to close the research stage.
