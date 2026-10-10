> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Uniform block nonvanishing of the actual weighted finite difference

Date: 2026-10-02. Status: new author proof, not an independent audit. The elementary block theorem below is proved in full. Its application to the actual selector depends on the saved uniform relative-saddle theorem in `work/session_20261001_astra/agent2/LARGE_SELECTOR_RELATIVE_SADDLE.md`; that analytic theorem remains in its existing author-input status. No numerical checks or reruns of the old 15 cases were used. This is a continuation, not a closeout.

## 1. Search and scope record

Archive searches were run before pursuing this target. The initial patterns were `weighted finite`, `W(n,m)`, `Q_(n,m)`, `Meixner`, `Krawtchouk`, `real.root`, and `Jensen polynomial`; follow-up patterns included `sign.change`, `sign variation`, `discrete Rolle`, `finite difference`, `degree n polynomial`, `opposite signs`, and `four consecutive`. The weighted certificate appears in `LARGE_SELECTOR_WEIGHTED_DIFFERENCE_DRAFT.md`; its own final section explicitly leaves unbounded nonvanishing open. The archive also contains numerous finite-difference and sign results for other families, plus `agent1/LOGARITHMIC_RESIDUAL_RECURRENCE.md`, whose four-consecutive nonvanishing is modular and pertains to a different residual. No searched hit supplies the block interpolation argument below for this actual weighted certificate. This is an overlap assessment of the searched material, not a universal novelty claim.

Online paper searches were `Meixner polynomials zeros generating function finite difference real zeros`, `finite differences polynomial weighted z^j binomial real rooted Euler transform Jensen polynomial`, and then `finite differences polynomial sign changes discrete Rolle theorem paper`. Relevant opened primary sources were:

- A. Jooste, K. Jordaan, and F. Tookos, *Zeros of Meixner and Krawtchouk polynomials*, https://arxiv.org/abs/0901.0817. This concerns hypergeometric zero location; it did not identify the present U polynomial or prove a sign for the present contour moment. The initial orthogonal-polynomial identification was not used.
- D. Gorbachev, V. Ivanov, and S. Tikhonov, *Chebyshev systems and Sturm oscillation theory for discrete polynomials*, Forum of Mathematics, Sigma 14 (2026), e84, DOI https://doi.org/10.1017/fms.2026.10168; opened publisher article https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/chebyshev-systems-and-sturm-oscillation-theory-for-discrete-polynomials/A3EE92545351CD5E4B4FC44221C0C33B. Its abstract and discrete sign-change discussion, in particular Lemmas 3.2–3.4, supply the relevant classical oscillation context.
- *Elements of Pólya-Schur theory in the finite difference setting*, opened author-hosted primary PDF https://staff.math.su.se/shapiro/Articles/FiniteDifference.pdf. Its finite-difference root preservation addresses stronger real-rootedness assumptions, which are unnecessary here.

The overlap is the standard relation between polynomial degree, zero count, and finite differences. The present contribution is an explicit application to E_m=U_m(T_m−πU_m), with a complete treatment of forcing zeros and an O(n) nearby block, followed by the actual certificate's rational lattice. No published general method is claimed new.

## 2. Actual definitions and retained exact identity

For n=4k≥4 put r=n/2 and d=n+1. Retain exactly

    B_m(t)=(1−2t+2t²)^n(1−4t+2t²)^(2m),
    K_m(t)=t^n B_m^(n)(t)/n!,
    U_m=K_m(1),
    T_m=calL((K_m−U_m)/(t−1)),
    calL(f)=∫_{−1}^1 f((1+iu)/2)du.

The polynomial selection formula proves that U_m is a real polynomial of exact degree r in m, with leading coefficient 4^r/r!. For every integer m, U_m is an integer divisible by 2^r. No real-rootedness assertion is needed.

Define, including U_m=0,

    E_m=U_m(T_m−πU_m),
    W(n,m)=Δ^d(U_m T_m)=Δ^d E_m.                    (1)

The last equality holds because U_m² has degree n<d. Put a=(1+i)/2, V(w)=w²−w+1/2, A(w)=(2w²−1)², and

    J_m=∫_(1/2)^a V(w)^n A(w)^m/w^(n+1) dw.

The existing exact contour identity, valid without division by U, gives for even n

    T_m−πU_m=−2^(n+2) Im J_m,
    E_m=−2^(n+2) U_m Im J_m.                       (2)

Thus all signs used below refer to the actual weighted error, including zero-forcing nodes and exact zero imaginary parts.

For identification with the exact polynomial-integral certificate, retain

    P_(n,m)(z)=Σ_(j=0)^d (−1)^(d−j) binom(d,j) U_(m+j) z^j,
    P_(n,m)(z)=(z−1)^(r+1) Q_(n,m)(z), Q_(n,m)∈Z[z], deg Q≤r,
    S_(n,m)(w)=w V(w)^n(w²−1)^(r+1) A(w)^m Q_(n,m)(A(w)),
    W(n,m)=i 2^(2n+3) ∫_(bar a)^a S_(n,m)(w)dw
          =−2^(2n+4) Im F_(n,m)(a),

where F_(n,m) is the polynomial primitive of S_(n,m) with constant term zero. Its degree is at most 5n+4m+4. These are the same exact Gaussian-rational evaluations and odd denominator lengths used in the saved weighted draft.

## 3. Four-phase lemma

Suppose z_0,z_1,z_2,z_3 are nonzero complex numbers. Suppose their phase lifts θ_j satisfy

    2π/5 ≤ θ_j−θ_(j+1) ≤ 3π/5,  j=0,1,2.         (3)

Then their imaginary parts include a strictly positive and a strictly negative value.

Proof. If all sin θ_j≥0, each θ_j lies in the union of closed intervals [2hπ,(2h+1)π]. Consecutive decreasing phases cannot move from one such interval to a lower such interval, because the intervening gap has length π, whereas each decrease is at most 3π/5<π. Hence all four phases lie in a single interval of length π. But θ_0−θ_3≥6π/5>π, a contradiction. Applying the same argument to the intervals where sin θ≤0 rules out all sin θ_j≤0. Consequently there is a strict sign of each kind. Exact zero imaginary parts cause no exception. ∎

## 4. General interpolation lemma

Let u(x) be a nonzero real polynomial of degree r. Let e_j=u(M+j)y_j at the integer nodes 0≤j≤N−1, where every four consecutive y-values inside this node range include strict opposite signs. Let d≥1 and put b=d+r. If

    N=4b,

then the d-th finite differences of e cannot all vanish at the N−d available starts.

Proof. If they all vanished, a real polynomial p of degree at most d−1 would agree with e at all N nodes. For completeness, choose the polynomial interpolating the first d nodes. Both its values and e obey the monic order-d recurrence Δ^d f=0. Induction determines all subsequent values, so they agree throughout the full range.

Partition the N nodes into b groups of four nodes, with associated disjoint real intervals

    I_h=[M+4h,M+4h+3],  0≤h≤b−1.

At most r of these intervals contain a real root of u. On every other interval u is nonzero and has constant sign; the four y-values include strict opposite signs, so the sampled products e, and hence p, include strict opposite signs. By the intermediate value theorem p has a root in the interior of that interval. There are at least b−r=d such intervals, producing at least d distinct real roots of p. Moreover p is not identically zero since at least one such group has strictly nonzero samples. This contradicts deg p≤d−1. ∎

This argument neither divides by u at a zero nor infers a uniform sign for u across the whole block.

## 5. Uniform theorem for W

Fix ρ>0. Let n→∞ through n=4k, and let the integer M satisfy

    M=ρ n log n+O(n), M≥0.                         (4)

The saved relative-saddle input proves J_m≠0 and

    J_(m+1)/J_m=−2i[1+O_ρ(1/log n)]               (5)

uniformly on the entire range

    M≤m≤M+6n+3.

To verify the domain rather than assume it, this range still has m=ρ n log n+O(n); any fixed O(n) adjustment is eventually contained in the saved domain |m−ρ n log n|≤C n log n/log log n for a suitable fixed C>0. Consistent adjacent phase lifts in (5) have decrease π/2+O_ρ(1/log n), hence satisfy (3) for all sufficiently large n throughout the full range.

Apply the interpolation lemma with u=U, y_m=−2^(n+2) Im J_m, d=n+1 and r=n/2. Here

    b=d+r=3n/2+1,
    N=4b=6n+4,
    N−d=5n+3.

Therefore

    ∃ h∈{0,…,5n+2}: W(n,M+h)≠0.                  (6)

This holds for every sufficiently large n=4k and every starting M in (4). It gives an actual unbounded nonvanishing selection from a nearby O(n) block. It does not assert W(n,M)≠0 at the original single start, and it does not exclude isolated exceptional nodes of the original direct quotient.

A finite rule independent of π is to take the least h in (6), because W is exactly rational. The original polynomial-integral formula remains the exact evaluation mechanism for each tested certificate; the proof did not replace W by a generic moment.

## 6. Enlarged rational-lattice lower bound

Retain the proved author arithmetic of the weighted-certificate draft: if ℓ≥0 and L(ℓ)=5n+4ℓ+4, then

    O_(L(ℓ)) W(n,ℓ) ∈ 2^(r+1) Z,                (7)

where O_s is the least common multiple of the odd positive integers at most s.

For the enlarged block define

    L*=25n+4M+12,
    N*=26n+4M+12,
    H=max_(0≤j≤6n+3)|U_(M+j)|.                   (8)

These precise constants include all support nodes: the largest certificate start is M+5n+2, whose primitive polynomial-integral degree bound is L*; the largest direct node is M+6n+3, whose T moment degree bound 2n+4m is N*. Also H>0 because U has degree r<N.

Let ℓ=M+h be the least nonzero certificate. Since O_(L(ℓ)) divides O_(L*), equations (6)–(7) imply

    |W(n,ℓ)|≥2^(r+1)/O_(L*).                     (9)

Using its exact weighted expression and the sum 2^d of absolute binomial weights gives

    |W(n,ℓ)|≤2^d H² max_(0≤j≤d,U_(ℓ+j)≠0)|β_(ℓ+j)−π|,

where β_j=T_j/U_j. Thus some actual nonzero-forcing direct node s∈[ℓ,ℓ+d]⊆[M,M+6n+3] has

    |β_s−π|≥B*,
    B*=1/(2^r O_(L*) H²).                         (10)

No zero-forcing node is discarded before the identity is used. Equation (10) follows from the actual W lattice, not an arbitrary odd-denominator rational separation claim.

The existing Cauchy bound gives uniformly log H≤(n/2)log log n+O_ρ(n). Using the elementary O_s≤4^s yields

    log B*≥−4ρ log 4·n log n−n log log n−O_ρ(n).  (11)

The enlarged O(n) constants in L* affect only the displayed O_ρ(n) remainder.

## 7. Complete error and actual center denominator

Let α_s be the actual exponential companion and c_s=α_s+β_s, with actual fully reduced denominator q_s. The saved author complete-exponential estimate supplies a uniform positive upper bound E* on |α_s−e| throughout these nonzero-forcing nodes, satisfying

    Λ*=2n+8(M+6n+3)=50n+8M+24,
    E*=3 (Λ*)^n exp(Λ*/(n+1)) /
       [(n+1)(n!)² 2^r],

    log E*≤−n log n+n log log n+O_ρ(n).             (12)

Indeed the saved estimate is 3Λ_s^n exp(Λ_s/(n+1))/[(n+1)(n!)²|U_s|], with Λ_s=2n+8s; Λ_s≤Λ* and |U_s|≥2^r at every nonzero-forcing node. The displayed E* therefore bounds the entire saved exponential remainder on the full enlarged support, without retaining only a leading endpoint term.

For 4ρ log 4<1, E*/B*→0. At the node from (10), eventually

    |c_s−(e+π)|≥B*/2.                             (13)

Thus the complete exponential contribution is present and controlled.

Retain the actual companion denominator assertion

    den(β_s) divides O_(2n+4s)|U_s|/2,
    den(β_s)≤O_(N*) H/2.                          (14)

If a_s=den(α_s), full rational reduction of c_s=α_s+β_s implies a_s≤q_s den(β_s). The saved elementary irrationality-measure input for e says that for every ε>0 there is C_ε>0 with

    |e−A/a|≥C_ε a^(−2−ε)

for reduced rationals A/a. Combining this with (12) and (14) gives the finite uniform lower bound

    q_s≥2(C_ε/E*)^(1/(2+ε))/(O_(N*) H).            (15)

In particular

    liminf log q_s/(n log n)≥1/2−4ρ log 4.         (16)

Combining (13) and (15) without dropping either denominator cost gives

    q_s |c_s−(e+π)|
      ≥(C_ε/E*)^(1/(2+ε)) /
        [2^r O_(N*) O_(L*) H³],                   (17)

and hence, after ε decreases to zero,

    liminf log(q_s |c_s−(e+π)|)/(n log n)
      ≥1/2−8ρ log 4.                              (18)

For 0<ρ<1/(16 log 4), these actual primitive forms diverge along the selected family. The actual q_s, rather than a raw coefficient clearer, occurs in every such statement. The exponential estimate, e irrationality-measure estimate, and arithmetic assertions (7), (14) remain explicitly named author dependencies; this note is not their independent audit.

The implication in the original weighted draft therefore no longer needs a separate unbounded nonvanishing hypothesis if its saved relative-saddle input is accepted. The selection now uses the starts M,…,M+5n+2, with direct nodes through M+6n+3. The leading rate and ρ range survive because the extra cost is O(n).

## 8. Explicit rational rule for a direct witness

The existential node in (10) can be turned into a finite rational selection without testing closeness to an unknown real number. Compute the actual rational B* in (10), and choose a rational p with a proved enclosure |p−π|≤B*/8. Such p is supplied, for example, by truncating the convergent integral series

    π/4=arctan 1=Σ_(k≥0) ∫_0^1 (1−t²)^k dt / 2^(k+1).

This identity follows from 1/(1+t²)=(1/2)Σ_(k≥0)((1−t²)/2)^k. Each integral is rational by polynomial expansion, and the omitted tail after k=K is at most 2^(−K−1), so the corresponding π tail is at most 2^(1−K). Choose the first K for which 2^(1−K)≤B*/8. No Machin formula or external numerical π oracle is needed.

Among the nonzero U nodes in the support of the least nonzero certificate, choose s with largest rational quantity |β_s−p|, breaking ties toward the smaller s. If t is the existential witness from (10), then

    |β_s−π|≥|β_s−p|−B*/8
             ≥|β_t−p|−B*/8≥3B*/4.

Once E*≤B*/4, this explicitly selected node satisfies (13) with the same B*/2. Thus (15)–(18) hold for this finite rational rule. It was defined mathematically, not executed as a numerical search.

## 9. Classical prime-number-theorem refinement of the same rates

This further goal was to sharpen only the elementary lcm estimate in the preceding proof. Before doing so, archive searches for `O_L`, `O_N`, `odd lcm`, `log lcm`, `Chebyshev psi`, `PNT`, and `prime number theorem` found the old large-selector drafts using O_X≤4^X, and many other archived uses of the prime number theorem. This refinement has classical overlap and is not a new prime-distribution result. The online paper query was `Rosser Schoenfeld Approximate formulas some functions prime numbers 1962 psi x 1.03883 pdf`.

Opened primary source: J. B. Rosser and L. Schoenfeld, *Approximate formulas for some functions of prime numbers*, Illinois Journal of Mathematics 6 (1962), 64–94, DOI https://doi.org/10.1215/ijm/1255631807. The publisher landing page was opened; its download URL did not expose the paper text through the browser. A full original-paper PDF was opened at https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf. Page 64 defines ψ(x) as the logarithm of the least common multiple through x; equation (2.29) on page 68 gives θ(x)=x+o(x), and Theorem 13, equation (3.36), on page 71 gives ψ(x)−θ(x)<1.42620 sqrt(x). These supply ψ(x)=x+o(x).

Since removing the prime 2 from the lcm removes exactly its largest power through X,

    log O_X=ψ(X)−floor(log_2 X)log 2=X+o(X).        (19)

Here L*,N*=4ρ n log n+O_ρ(n). Consequently

    log O_(L*)=4ρ n log n+o_ρ(n log n),
    log O_(N*)=4ρ n log n+o_ρ(n log n).             (20)

Applying (20) to the same finite bounds (10), (15), and (17) gives

    liminf log B*/(n log n)≥−4ρ,
    liminf log q_s/(n log n)≥1/2−4ρ,
    liminf log(q_s |c_s−(e+π)|)/(n log n)≥1/2−8ρ. (21)

The complete-error domination now needs 4ρ<1. The primitive divergence therefore holds for the larger strict range

    0<ρ<1/16.                                    (22)

The same exact rational selection rule and the same actual reduced denominator q_s are used. The finite bounds (9)–(17) are unchanged; only their asymptotic evaluation is sharpened by a published classical theorem. The endpoint ρ=1/16 is not settled by this leading-rate argument.

## 10. Limits

This is a nonvanishing and primitive-divergence theorem for a selected nearby certificate and at least one associated direct node. It does not show a fixed sign or nonzero W at every start, does not control all direct selectors, and does not prove irrationality of e+π. The analytic source theorem is the only nontrivial asymptotic input to (6); the phase-sparsity theorem is unused. Exact tests of small n cannot substitute for this proof and were not rerun.
