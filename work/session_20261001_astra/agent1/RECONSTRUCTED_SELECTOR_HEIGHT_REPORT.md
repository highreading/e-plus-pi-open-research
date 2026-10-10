> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Reconstructed selector height report

New author deductions, English and offline, 2026-10-01. No scans, prior checker replay, or independent review. The main direct-selector obstruction is an author input, not audited here.

The exact reconstruction K=D_B(D+1)^(-n) is integral and saturated. With

 M=2^n n! D0 T, D0_ii=(n+i)!/n!, Delta=det M,
 J=2^n fP/n!, V=D0 J,
 C=K adj(M)D0, x=CJ,

one has u=(n!)^2 x/Delta. All formulas require det T!=0; coordinate formulas additionally require x_j!=0.

For coordinate j, put g_j=gcd(C_j). The actual primitive selector and its heights are

 lambda_j=C_j/g_j,
 H_j=||C_j||_1/g_j, A_j=|x_j|/g_j.

The correction is zero for j>0. For coordinate zero it is Delta/((n!)^2 x_0), with its EXACT reduced denominator retained.

For the specified factorial Gram weights W=tau^2 Omega, put

 z=C^T Omega x, D=x^T Omega x, gamma=gcd(z).

Then

 lambda_G=z/gamma,
 H_G=||z||_1/gamma, A_G=D/gamma,
 r_G=Delta x_0/((n!)^2 D).

The common factorials and tau^2 cancel from the primitive selector. The correction denominator does not automatically cancel.

New all-size content restrictions are

 g_j divides dmax Delta,
 gamma divides dmax Delta rho det(K^T Omega K),

where dmax=(n+b-1)!/n! and rho=gcd(x)=gcd(adj(M)V). Their proofs use integer matrix identities and saturation, not generic coprimality. For b=O(log n), log dmax and log det(K^T Omega K) are o(n log n). Explicit cofactor height ceilings retain the actual coefficient gcds; they are not promoted to attained primitive heights.

The retained local domain is unchanged: p odd, p>2b+3, p>=3b, n=ap+r, b<=r<=floor((p-b)/2). New reconstructed transfers give

 C(n)=2^(a(b-1))C(r),
 x(n)=2^(ab)h_a x(r) mod p.

For fixed subtraction depth m, corresponding Gram transfers are also proved. Conditional nonzero-residue tests determine primitive selector content and can force v_p(den(r))=2v_p(n!). Vanishing residues require the complete vector/contraction lifts; no unit is assumed.

The necessary budget is now expressed exactly as

 coordinate: log||C_j||_1+log|x_j|-2log g_j+2log den(r_j),
 Gram: log||z||_1+log D-2log gamma+2log den(r_G).

Whether it reaches n log n is unresolved. For j>0 the gap is the actual row gcd; for Gram selection the response and adjoint contents also remain. For coordinate zero and Gram selection, actual correction-denominator cancellation must be controlled. Common multiplication of a selector is stopped as a purported height improvement.

This delivers the canonical selector/correction interface, leaving eligible-coordinate reduced denominators to Child 4. The scalar small-denominator route remains stopped, and its completed dyadic/ternary results are preserved.

Full derivation: work/session_20261001_astra/agent1/RECONSTRUCTED_SELECTOR_HEIGHT.md.
