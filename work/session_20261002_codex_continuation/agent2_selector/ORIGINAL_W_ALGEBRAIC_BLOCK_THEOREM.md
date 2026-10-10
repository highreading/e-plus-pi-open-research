> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Algebraic removal of the original weighted-certificate nonvanishing condition

2026-10-02. Original author theorem for the ORIGINAL even-step weighted certificate W(n,m), beyond the distinct half-step family. The completed half-step rank-residue proof transfers to the original fixed polynomial with explicit degree and shift changes. This removes its unbounded nonvanishing premise without a moving-saddle input.

## 1. Search and overlap before this transfer

Archive search for all-start, rank-one residues, degree 4n+8, the proposed block endpoint 4n+10, and the proposed length 21n+4M over sources and the preceding session found no original-W algebraic block theorem. The saved original fixed-kernel identity and weighted rational-lattice draft were read; the latter explicitly left unbounded nonvanishing open. The current session's earlier saddle interpolation theorem is retained as prior work.

Online primary-paper search: `Prellberg Three Irrationality Results Dilogarithm four term recurrence nonvanishing 2609.06895`. Opened the primary full HTML https://arxiv.org/html/2609.06895v1, specifically §2.5. Its recurrence-based nonvanishing for a different actual moment family is the relevant overlap; it does not evaluate the present W output determinant or its poles. The present result applies a finite-degree rational-output argument to the exact existing kernel. It is not a new generic holonomic principle or an external irrationality claim.

## 2. Exact original output and changed denominator degree

Let n=4k≥4, r=n/2, d=n+1. The proved original fixed kernel is

    P_old(w)=w(w²−1)^d V(w)^r R_n(w),
    deg P_old=5n+3=10r+3,
    ord_a P_old=ord_(bar a)P_old=r,

where a=(1+i)/2 and R_n(a),R_n(bar a) are nonzero. It obeys

    P_old(w)=[2(1−w²)]^d P_half(w),
    W(n,m)=i2^(n+1)∫_(bar a)^a z(w)^(2m)P_old(w)dw,
    z(w)=1−2w².                                 (1)

Use the regular integer-h state X_h from the half-step proof, now at h=2m. For the rational output row R_old(h), the three consecutive ORIGINAL m outputs pulled back to X_h are

    O_old(h)=[ R_old(h);
               R_old(h+2)S_2(h);
               R_old(h+4)S_4(h) ].               (2)

The maximum even-monomial shift in (2) is 5r+5, while the maximum odd-primitive denominator is h+5r+6. Exactly the rank-one-residue proof in `HALF_STEP_ALGEBRAIC_BLOCK_THEOREM.md` therefore shows that det O_old has only simple possible poles, all cleared by

    D_old(h)=∏_(k=1)^(5r+6)(h+k)
                  ∏_(k=0)^(5r+4)(2h+2k+3).       (3)

Its degree is 10r+11=5n+11. The integer-pole residue direction remains (z_+^k,−z_−^k), independent of the output shift i=0,2,4. At a half-integer pole, all singular forward products have the same right residue direction. Thus no larger pole powers arise in the determinant. No U division is made.

## 3. Exact nonzero coefficient at infinity

The original kernel's even w² coefficient is

    c_old=2^d c_n>0,

with c_n the explicit positive coefficient in the half-step proof. Its upper endpoint coefficient is

    γ_old=(2−i)^d γ_n≠0,

because the multiplying factor in (1) is nonzero at a. All fixed-n endpoint expansions used in that proof therefore remain valid. The only change in the three-output determinant is the Vandermonde on 1,z_+²,z_−² instead of 1,z_+,z_−:

    (z_+²−1)(z_−²−1)(z_−²−z_+²)=20i.

Dividing by the same fundamental-state determinant gives

    det O_old(h)=−10(c_old/4)|γ_old|²
                    h^(−n−3)(1+O_n(1/h)).       (4)

Consequently p_old(h)=D_old(h)det O_old(h) is a NONZERO rational-coefficient polynomial of exact degree

    5n+11−(n+3)=4n+8.                            (5)

The original reduced numerators of degree 4n+6 at n=4,8 are consistent with the two extra negative factors in this safe overclearing. No uniform cancellation of those factors is required here.

## 4. All-start actual W theorem

For every nonnegative integer M, the 4n+9 distinct arguments h=2(M+j), 0≤j≤4n+8, cannot all be roots of p_old. At one such start the matrix (2) is invertible. The actual state X_h is nonzero, because its two endpoint coordinates cannot both vanish. At least one of the three actual outputs there is nonzero. Therefore

    for EVERY n=4k≥4 and M≥0,
    ∃ell∈[M,M+4n+10]∩Z: W(n,ell)≠0.             (6)

The selected certificate uses direct centers only through ell+d≤M+5n+11. Actual forcing zeros and actual zero errors are handled without division. The least nonzero rational W is a finite rule. The original nonvanishing condition is removed at this controlled O(n) block level, with no relative-saddle assumption, no generic odd-denominator separation, and no exclusion based only on phase sparsity.

## 5. Complete original-center budget after the new block

For M=ρ n log n+O(n), define the fully enlarged quantities

    L*=21n+4M+44,
    N*=22n+4M+44,
    A*=max_(0≤j≤5n+11)|U_(M+j)|,
    Λ*=42n+8M+88.

The maximum certificate primitive degree 5n+4ell+4 is L*. The maximum actual center degree 2n+4s is N*, and its full exponential parameter 2n+8s is Λ*. The exact original lattice and weighted identity prove

    |W(n,ell)|≥2^(r+1)/O_(L*),
    ∃s in the selected support with U_s≠0:
    |β_s−π|≥B*=1/[2^r O_(L*) (A*)²].            (7)

For the ACTUAL companion α_s and fully reduced q_s of c_s=α_s+β_s,

    0<|e−α_s|<E*=3(Λ*)^n exp(Λ*/(n+1)) /
                                    [(n+1)(n!)²2^r],
    den(β_s)≤O_(N*)A*/2,
    q_s≥2(C_ε/E*)^(1/(2+ε))/(O_(N*)A*).          (8)

The last inequality follows from den(α_s)≤q_s den(β_s) and the saved elementary e irrationality-measure input. When E*≤B*/2,

    |c_s−(e+π)|≥B*/2,
    q_s|c_s−(e+π)|≥(C_ε/E*)^(1/(2+ε)) /
                      [2^r O_(N*)O_(L*)(A*)³].   (9)

The same actual forcing Cauchy height gives log A*≤r log log n+O_ρ(n). With the classically sourced PNT evaluation of the odd lcm, (7)–(9) yield

    liminf log B*/(n log n)≥−4ρ,
    liminf log q_s/(n log n)≥1/2−4ρ,
    liminf log(q_s|c_s−(e+π)|)/(n log n)≥1/2−8ρ.  (10)

The full exponential error is dominated when 4ρ<1, and these actual selected primitive forms diverge for 0<ρ<1/16. The explicit rational π-enclosure witness selection from the earlier block proof applies with the new B*: it gives logarithmic error ≥3B*/4 and complete error ≥B*/2 once E*≤B*/4. The fully reduced denominator and complete same-index companion are retained.

The arithmetic/lattice and complete-exponential formulas retain their previously stated author-input scopes. The analytic nonvanishing no longer uses the relative saddle theorem. The stronger constant-shift conclusion remains open, and this selected divergence theorem does not prove irrationality of e+π.
