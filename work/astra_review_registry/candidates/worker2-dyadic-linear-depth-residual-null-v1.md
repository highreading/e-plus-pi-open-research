> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Linear-depth dyadic approximation along odd-modulus progressions is residual, Haar-null, and of Hausdorff dimension zero

Status: UNVERIFIED CANDIDATE
Author: worker_2
Content SHA256: a8be775b6a40b05145fc2a8e8938d43d4fb744325d57e97575d6d5fec033dd4b

Status: unverified author submission; independent review required.

Statement. Let c>0 be a real constant, let m be a positive odd integer, and let a be any integer. Give Z_2 its usual dyadic metric d_2(x,y)=2^{-v_2(x-y)}, with v_2(0)=+infinity, and normalized Haar measure mu(Z_2)=1. Define
E(c;m,a)={x in Z_2 : v_2(x-n)>=ceil(c n) for infinitely many positive integers n satisfying n congruent to a modulo m}.
Then E(c;m,a) is a dense G_delta subset of Z_2, has Haar measure zero, and has Hausdorff dimension zero in d_2. In particular its intersection with every nonempty dyadic open ball is nonempty, has measure zero, and has Hausdorff dimension zero.

Proof. Write h_n=ceil(c n) and B_n=n+2^{h_n}Z_2 for each admissible positive integer n. This ball is clopen, has Haar measure 2^{-h_n}, and has dyadic diameter 2^{-h_n}. For each positive integer N put U_N=union B_n, where the union is over admissible n>=N. Then E(c;m,a)=intersection_{N>=1} U_N, so it is G_delta.

Each U_N is dense. Indeed, let b+2^k Z_2 be any basic nonempty open ball, with k>=0 and b an integer representative. Since m is odd, the Chinese remainder theorem gives arbitrarily large positive integers n satisfying n congruent to a modulo m and n congruent to b modulo 2^k. Choose one with n>=N and h_n>=k, possible because c>0. Then B_n is contained in b+2^k Z_2. Thus every basic ball meets U_N. The complete metric space Z_2 is a Baire space, so the intersection of the open dense sets U_N is dense. This proves the first assertion.

For every N, countable subadditivity gives
mu(E(c;m,a)) <= sum_{n>=N, n congruent to a mod m} 2^{-h_n} <= sum_{n>=N} 2^{-c n}.
The final geometric tail tends to zero. Hence mu(E(c;m,a))=0.

Fix any real s>0. The same balls with n>=N cover E(c;m,a); their diameters are at most 2^{-cN}, which tends to zero. Their total s-power diameter is bounded by
sum_{n>=N} (2^{-h_n})^s <= sum_{n>=N} 2^{-s c n},
which also tends to zero. For any prescribed positive covering scale and positive total-cost tolerance, sufficiently large N satisfies both. Consequently the s-dimensional Hausdorff measure of E(c;m,a) is zero. This holds for every s>0, proving Hausdorff dimension zero. Density ensures nonemptiness, including in every nonempty open ball; monotonicity of measure and dimension proves the final assertions.

Scope and interpretation. Indices n are ordinary positive integers, and c n uses their ordinary real size. The odd-modulus congruence is a restriction on those integer indices; it is not an extra dyadic restriction on x. Infinite approximation means infinitely many distinct indices, equivalently arbitrarily large indices. The integer-valued valuation makes the displayed condition equivalent to v_2(x-n)>=c n. Category and measure differ here: this set is residual while Haar-null. No inference from Haar-nullity excludes a particular specified dyadic number, and density shows that a finite dyadic residue condition alone cannot exclude this approximation property.

Dependencies and evidence. The proof uses only dyadic balls and their Haar measures, the Chinese remainder theorem, the Baire category theorem for complete metric spaces, and the definition of Hausdorff measure. Preliminary author derivations are recorded in work/astra_20260929/worker_2/note_000042.md and work/astra_20260929/worker_2/note_000043.md; the complete argument above is self-contained and does not require those notes as proof dependencies. No numerical computation is used.

Unresolved project applicability. This theorem concerns arbitrary elements of Z_2. It neither places the project's particular exceptional roots inside E(c;m,a) nor outside it. Their defining analytic identities may impose further restrictions not considered here. No actual reduced-denominator estimate and no rationality or irrationality conclusion for e+pi follows. Independent review of this exact claim remains pending.