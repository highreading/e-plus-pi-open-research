> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A uniform nonvanishing block for the actual half-step certificate

2026-10-02. Original author proof continuing the distinct all-integer-selector target in `ODD_SELECTOR_HALF_STEP_DRAFT.md`. The exact state formulas and finite all-axis determinants are in `HALF_STEP_THREE_STATE_OUTPUT.md`. The present theorem applies along n→∞ and does not assume the unresolved uniform determinant conjecture.

## 1. Search, overlap and analytic input

The initial archive/primary search ledger for the altered family is in `ODD_SELECTOR_HALF_STEP_DRAFT.md`. Before pursuing the present analytic transfer, an additional archive search for `half.step`, `odd.selector`, `saddle.*half`, `six.phase`, `six consecutive`, and `degree 2n` over the preceding session and sources found no half-step phase/block theorem. The saved exact relative-saddle proof was read in full: `work/session_20261001_astra/agent2/LARGE_SELECTOR_RELATIVE_SADDLE.md`.

The additional online paper search was `Temme uniform asymptotic methods integrals saddle point endpoint coalescing 2013 arxiv`. Opened primary source: Nico M. Temme, *Uniform Asymptotic Methods for Integrals*, https://arxiv.org/pdf/1308.1547, specifically §2.3 and the introduction to §4. Its treatment of contour deformation and additional parameters is classical overlap. It does not supply the present contour identity, the actual forcing sign, or the arithmetic certificate.

The analytic argument below transfers the saved explicit saddle proof to integer h. The scaled phase, local deformation and Gaussian remainder are literally the same functions as that proof, rather than an inference from a ratio on even h. The new contribution is the actual half-step phase/sign identification and the complete certificate consequence. The saved analytic bounds remain author inputs rather than independently audited claims.

## 2. Exact half-step saddle formula and the effective phase

Let a=(1+i)/2, V(w)=w²−w+1/2, q(w)=2w²−1, and define the actual upper-endpoint moment

    J_h=∫_(1/2)^a V(w)^n q(w)^h/w^(n+1) dw.

Both exponents n,h are integers. Set λ=2n/h for h>0, ν=1/n, w=a−ix/2=a(1−ax), and

    C_0(x)=1−x+(1+i)x²/4.

Exactly,

    V(w)=(x/2)(1−x/2), q(w)=(i−1)C_0(x),
    J_h=[i/(2a)](2a)^(−n)(i−1)^h λ^(n+1)
                 ∫_0^(1/λ) exp(n φ(t;λ,ν))dt,

    φ=log t+(2/λ)log C_0(λt)+log(1−λt/2)
                  −(1+ν)log(1−aλt).

This is the saved exact scaled phase. Let t_s(λ,ν) be its exact root φ'=0 near 1/2, let F(λ,ν)=φ(t_s;λ,ν), and b(λ,ν)=−φ''(t_s;λ,ν). Retain the analytic branches from λ=0, with b^(1/2)→2. The saved local contour and tail proof gives

    J_h=[i/(2a)](2a)^(−n)(i−1)^h λ^(n+1)
         exp(nF) sqrt(2π/n) b^(−1/2)(1+O(1/n)),   (1)

uniformly for n sufficiently large and 0<λ≤λ_0.

The applicability to odd h requires no fractional-power branch. To verify the global tail bound directly, the saved chord estimate for |q(w)^2/q(a)^2| gives

    |q(w)/q(a)|≤exp(−7x/16).

Then hλ=2n gives the same envelope sqrt(2)t^n exp(−7nt/8) as before. All original powers are integer powers; the central logarithms lie in the same analytic rectangle. The exact saddle, strict real-phase curvature, connector gaps, and odd-cubic Gaussian cancellation are unchanged. Formula (1), including its relative O(1/n) remainder, therefore holds at odd and even h and proves J_h≠0.

The ACTUAL forcing is U_h=(−1)^h u_n(h). Define the effective upper moment Z_h=(−1)^h J_h. Its leading integer phase is (1−i)^h. Since

    λ'=2n/(h+1)=λ/(1+λ/(2n)),

the same analytic derivative bounds for F,b give

    Z_(h+1)/Z_h=(1−i)
       exp[−(1+ν)λ/2+O(λ²+1/n)].                  (2)

The O term can be complex. Its imaginary part is O(λ²+1/n); the exact growing phase n Im F was retained before taking this adjacent difference.

Fix ρ>0 and an integer start H=2ρ n log n+O(n). The entire support H,…,H+9n+5 has the same regime. For all sufficiently large n, adjacent decreasing phase lifts from (2) satisfy

    9π/40 ≤ arg Z_j−arg Z_(j+1) ≤11π/40           (3)

on that full support. This verifies the phase domain on all nodes used below.

## 3. Six-phase interpolation and actual nonvanishing

Any six consecutive nonzero complex values whose decreasing phase lifts satisfy (3) have imaginary parts of both strict signs. Indeed all nonnegative imaginary parts would place the lifted phases in the union of positive closed semicircles. Steps smaller than π cannot cross the intervening negative gap. They would therefore remain in one interval of length π, whereas the five steps have total decrease at least 45π/40>π. The argument for all nonpositive imaginary parts is identical. Zero imaginary parts do not obstruct either contradiction.

Retain r=n/2, d=n+1, and the actual entirely rational certificate

    W̆(n,h)=Δ_h^d(U_h T_h)
           =Δ_h^d[U_h(T_h−πU_h)].

The exact full-contour relation gives

    T_h−πU_h=−2^(n+2) Im J_h,
    U_h(T_h−πU_h)=−2^(n+2)u_n(h) Im Z_h.         (4)

Thus the sign polynomial used in interpolation is u_n, of degree r, rather than the alternating actual U_h. This corrects the sign which would otherwise make a half-step phase argument invalid.

Set b=d+r=3n/2+1 and take 6b=9n+6 nodes H,…,H+9n+5. If all d-th differences vanished, these node values would agree with a polynomial p of degree ≤d−1. Partition the nodes into b disjoint six-node intervals. At most r intervals contain a real zero of u_n. Each remaining interval has constant nonzero u sign and, by the six-phase lemma, contains strict opposite sampled signs in (4). It forces a distinct interior root of p. At least b−r=d roots are forced, while p is not identically zero because an interval has nonzero sampled signs. This contradicts deg p≤d−1. The standard finite-difference interpolation induction is the one proved in `WEIGHTED_DIFFERENCE_BLOCK_NONVANISHING.md` and applies with six in place of four.

Consequently, for every sufficiently large n=4k and every such H,

    ∃ell∈[H,H+8n+4]∩Z: W̆(n,ell)≠0.             (5)

The certificate support at each selected start ends at ell+d≤H+9n+5. Forcing zeros, imaginary-part zeros, and vanishing individual weighted errors were handled without division. The least nonzero certificate is an exact finite rational rule.

## 4. Complete lattice and error budget on the enlarged block

Define the exact enlarged quantities

    L*=19n+2H+10,
    N*=20n+2H+10,
    A*=max_(0≤j≤9n+5)|U_(H+j)|,
    Λ*=38n+4H+20.

Here L* is the largest certificate primitive degree 3n+2ell+2, and N* is the largest direct center degree 2n+2s. The exponential parameter at a direct node is 2n+4s, whose maximum is Λ*. Also A*>0 because u_n has degree r less than the node count.

Write O_X for the odd lcm through X. The proved exact half-step lattice gives

    |W̆(n,ell)|≥2^(r+1)/O_(L*).

The actual weighted identity, and the sum 2^d of its absolute binomial weights, therefore supply a direct node s within the selected support, with U_s≠0 and

    |β_s−π|≥B*, B*=1/[2^r O_(L*) (A*)²].         (6)

At every nonzero-forcing support node the full exponential error satisfies

    0<|e−α_s|<E*,
    E*=3(Λ*)^n exp(Λ*/(n+1))/[(n+1)(n!)²2^r].     (7)

This uses the entire exact tail estimate for the actual odd/even center, not a leading asymptotic term. Cauchy coefficient estimation with radius sqrt(n/(2h)) gives

    |u_n(h)|≤(2h/n)^r exp[n+n sqrt(2n/h)]

when h>0; hence log A*≤r log log n+O_ρ(n) on the support. Stirling's formula gives log E*≤−n log n+n log log n+O_ρ(n).

The actual logarithmic component denominator obeys

    den(β_s) divides O_(2n+2s)|U_s|/2,
    den(β_s)≤O_(N*) A*/2.                         (8)

Let q_s be the actual fully reduced denominator of c_s=α_s+β_s. The denominator of α_s is at most q_s den(β_s). Retaining the saved elementary e irrationality-measure input |e−A/a|≥C_ε a^(−2−ε) for every ε>0, equations (7),(8) give

    q_s≥2(C_ε/E*)^(1/(2+ε))/(O_(N*) A*).          (9)

If E*≤B*/2, the same-node complete error obeys |c_s−(e+π)|≥B*/2. Then

    q_s|c_s−(e+π)|≥(C_ε/E*)^(1/(2+ε)) /
                   [2^r O_(N*) O_(L*) (A*)³].    (10)

The classical odd-lcm evaluation log O_X=X+o(X), recorded and sourced in the old block note, gives L*,N*=4ρ n log n+O_ρ(n), so

    liminf log B*/(n log n)≥−4ρ,
    liminf log q_s/(n log n)≥1/2−4ρ,
    liminf log(q_s|c_s−(e+π)|)/(n log n)≥1/2−8ρ.  (11)

The domination E*/B*→0 holds if 4ρ<1; the actual selected primitive forms diverge if 0<ρ<1/16. The half-step alteration improves the finite block and O(n) lattice constants, rather than the leading ρ threshold. With only the elementary O_X≤4^X, replace 4ρ and 8ρ by 4ρ log4 and 8ρ log4, respectively.

An explicit rational direct-node rule follows the already proved π-enclosure construction: choose a rational p with |p−π|≤B*/8 and maximize |β_s−p| over nonzero U nodes of the selected certificate. It has |β_s−π|≥3B*/4. Once E*≤B*/4 its complete error is at least B*/2, so (9)–(11) apply to that exact rational rule. No unknown real comparison is required.

## 5. Scope and remaining stronger target

The actual half-step family now has unbounded controlled block nonvanishing, with actual forcing signs, full exponential errors, and actual reduced-center denominators attached. The support is H,…,H+9n+5 and certificate starts end at H+8n+4. The general three-output determinant remains open despite exact all-axis evidence for n=4,8. A constant-shift all-n result would further shorten the finite budget; it is not assumed here. These selected divergence statements concern the specified centers and imply no irrationality theorem for e+π.
