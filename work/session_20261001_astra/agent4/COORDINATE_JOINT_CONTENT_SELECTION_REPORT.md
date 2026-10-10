> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Joint coordinate content: completion report

This stage develops original joint arithmetic for the three positive rows at n=13^(s+1)+3, s>=5. The earlier effective-content factorization, rank-one exclusion, exact 13-primary theorem, and log B_j<=2n log n+O(n) bound are preserved. No scan or old computation was performed.

Write W for the first two columns of the actual adjugate adj(Nmat), z for the third row of Nmat, and Delta=det Nmat. The new exact identities are

det(W_0,W_1)=Delta z_2,
det(W_0,W_2)=-Delta z_1,
det(W_1,W_2)=Delta z_0,
sum_i z_i W_i=0.

With g_z=content(z) and c_W=content(W), they give

g_z | c_W | |Delta|,
Delta_2(W)=|Delta|g_z,
c_W^2 | |Delta|g_z.

For the actual smaller pairs T_i=W_i/ell_i, where ell_i=nu_i kappa_i and content(T_i)=tau_i, their minors are exactly the corresponding Delta z_k/(ell_i ell_j), with the complementary sign. Thus tau_i tau_j divides that smaller minor.

A stronger residual-content restriction follows from the shared third row:

gcd(tau_i,tau_j) | g_z for i!=j.

At any prime, at most one row can have residual tau-depth exceeding the depth of g_z. Outside g_z, residual cancellation can occur in at most one row. This concerns tau_i only; the already isolated factors ell_i are not discarded.

The final integral companion map gives outputs (A_i,C_i)=tau_i(Theta_i,Phi_i), with e_i=gcd(Theta_i,Phi_i) dividing D_V. Hence

B_i=|A_i|/(tau_i e_i),
(tau_i e_i)(tau_j e_j) | D_V det(T_i,T_j).

The note derives explicit primewise lower bounds for each B_i and a compulsory divisor for EVERY row in the actual eligible set. These are precise conditional arithmetic obstructions, not a newly evaluated asymptotic rate. It records the precision needed after each row's content is removed.

Eligibility remains decisive. Its rational inequality permits any singleton among three nonzero rows, even with prescribed nonzero residues modulo 13. This does not assert that an actual singleton has been exhibited on the Toeplitz family. An explicit auxiliary shared-matrix example proves that the joint cofactor identities plus the eligibility rule alone can select the only row with a large denominator while two other rows have bounded denominators. The example is clearly separated from actual HP data.

To improve the eligible minimum one must prove that the actual eligible set intersects the small-denominator/content-favorable set. To force a lower denominator bound for that minimum, one needs the bound in every eligible row. All-three existence statements do not supply either implication automatically.

No improved uniform rate is established. The completed stage is the exact joint obstruction and the proof of the selection limitation. The substantive remaining inputs are actual cofactor congruences and their relation to eligibility. No coordinate-to-Gram transfer is made.

Deliverables: COORDINATE_JOINT_CONTENT_SELECTION.md and this report. Delivery completion requires readback of both new files.
