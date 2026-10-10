> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fixed-kernel zero localization: an explicit next obligation

2026-10-02. Structural subtarget following the uniform actual-W fixed-kernel identity: control R_n at the complex saddle in the actual regime m≈ρn log n, or derive the full output Casoratian from the positive-shift Euler factorization. A moving-saddle lower bound and a relative integral error remain essential; exact endpoint nonvanishing alone does not settle the regime.

Archive search before choosing this subtarget: `polar derivative`, `Gauss.Lucas`, `half.?disk`, `strip.*root`, `root.*strip`, and `Euler.*operator.*root` across the preceding session and sources. The single textual half-disk hit concerns a different exterior reflection estimate, not the present R_n. No usable zero-localization result for this kernel was located. The earlier actual-U root proof is a local input and does not control R_n by itself.

Online primary-paper searches: "rational functions polar derivatives zeros disk Laguerre theorem positive residues", "Euler differential operator theta plus c polynomial zeros strip preservation", and "Borcea Branden linear differential operators circular domains strip stability rational functions".

Opened relevant primary texts:

- Julius Borcea and Petter Brändén, *Multivariate Pólya–Schur classification problems in the Weyl algebra*, https://arxiv.org/pdf/math/0606360. Its symbol criteria concern polynomial stability preservation.
- Petter Brändén and Matthew Chasse, *Classification theorems for operators preserving zeros in a strip*, https://arxiv.org/pdf/1402.2795. Strip-preserving operators require their specific symbol conditions; no application to the present operator is assumed.
- *Hermite–Poulain theorems for linear finite difference operators*, https://arxiv.org/pdf/1901.06398. Its constant-coefficient difference operators and line/strip results do not identify this variable-coefficient rational Euler product.
- Jonathan Leake, *A representation theoretic explanation of the Borcea–Brändén characterization*, https://doi.org/10.1007/s00209-021-02825-4. Its circular-domain and polar-derivative discussion was opened for possible Möbius/apolarity transfer.

Classical overlap: Gauss–Lucas, polar derivative, and polynomial stability-preserver methods are established. What remains project-specific is the exact treatment of the density V(w)^n/w^(n+2) under the positive-shift Euler factors, including its pole and branch changes, followed by a uniform saddle or quotient-output argument. Generic preservation statements do not automatically apply to this rational density.

Candidate meaningful hypothesis: the degree-2n residual R_n may have no zeros in the vertical strip 0≤Re w≤1/2. Such a statement would need a proof with quantitative separation in the relevant endpoint neighborhood before being used in saddle analysis. Exact whole-polynomial half-plane root counts are a suitable initial hypothesis test; approximate root plots cannot establish it. No all-n claim is made here.

Exact test completed on the two already derived fixed-kernel polynomials, without a W point scan: `check_fixed_kernel_strip.py` constructs rational Routh arrays for R_n(w) and R_n(w+1/2). There are no zero pivots or all-zero rows, including a nonzero last entry. The count of roots with Re w>0 and the count with Re w>1/2 are both n: 4 and 4 at n=4; 8 and 8 at n=8. Thus these exact residuals have no roots in the closed strip. The complete rational first columns are saved in `fixed_kernel_exact_strip_counts.json`. This establishes two finite-n instances of the proposed geometry, not a uniform theorem or a quantitative endpoint distance.

The primary Brändén–Chasse text concerns operators preserving zeros *within* a strip, formulated as stability on the union of its exterior half-planes. The candidate here instead excludes zeros from the interior strip and leaves roots on both sides. Its theorem cannot be cited as an immediate proof of this candidate.
