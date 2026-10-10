> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Shared Hurwitz prefixes: radius forces odd denominator cost and lacunarity

Status: original author deduction, 2026-10-02, not independently reviewed. This is a denominator/radius obstruction for a single shared germ. It proves no irrationality assertion about e+pi.

Let H(z)=sum_{j>=0} h_j z^j/j! be analytic on |z|<R, with h_j odd integers for every j>=1. The pullback H=e^z+F∘phi has this property whenever phi(0)=0 and all derivative jets of phi at zero are integers: the F-jets are even, and integral Bell-polynomial composition preserves evenness. A polynomial phi is not required.

For N>=0 set c_N=sum_{j=0}^N h_j/j!=p_N/q_N in lowest terms, and let o_N be the odd part of q_N. Since N!c_N is integral, v_2(q_N)<=v_2(N!). At every even N the last term h_N is odd and every earlier positive-order factorial weight N!/j! contains the even factor N, so

    v_2(q_N)=v_2(N!)       (N even).               (1)

Here h_0 is assumed integral as it is for the intended H; its weight N! is even for N>=2.

## 1. An exact difference retains its full dyadic denominator

Take even N>=2 and any 0<=M<N. Then

    N!(c_N-c_M)=sum_{j=M+1}^N h_j N!/j!

is an odd integer. Consequently c_N-c_M is nonzero, its reduced denominator has dyadic part exactly 2^v_2(N!), and its odd part divides lcm(o_N,o_M). Therefore

    |c_N-c_M| >= 1/[2^v_2(N!) lcm(o_N,o_M)].       (2)

This does not invoke the value H(1) or assume its irrationality. It is stronger than asserting that each individual truncation is nonzero.

Fix 1<r<R, and let C_r=max_{|z|=r}|H(z)|. Cauchy's coefficient bound gives

    |c_N-c_M| <= C_r sum_{j=M+1}^N r^(-j)
               <= C_r r^(-M)/(r-1).

Combining with (2) yields the finite, all-index inequality

    lcm(o_N,o_M) >= (r-1)r^M/[C_r 2^v_2(N!)].    (3)

Using v_2(N!)=N-s_2(N), the logarithmic form is

    log lcm(o_N,o_M)
      >= M log r-N log2+s_2(N)log2
                         +log(r-1)-log C_r.       (4)

All constants are explicit once an analytic sup bound C_r is supplied. A radius certificate alone implies finiteness of C_r; no numerical bound for it is asserted.

## 2. Consecutive even prefixes require positive odd-prime mass

For M=N-2 and N even, (4) gives

    log lcm(o_N,o_(N-2))
      >= N log(r/2)+s_2(N)log2-O_r(1).             (5)

Thus if R>2, the odd parts of adjacent even endpoint denominators cannot both have subexponential size. More quantitatively,

    max(log o_N,log o_(N-2))
      >= (N/2)log(r/2)+(s_2(N)/2)log2-O_r(1).

Taking r up to R gives

    limsup_(N even) log o_N/N >= (1/2)log(R/2).    (6)

The lcm statement is sharper than the maximum statement: (5) charges new odd denominator mass even when the two denominators overlap. It concerns actual endpoint denominators, after their separate gcd reductions. It gives a limsup/neighbor obstruction, not a pointwise lower bound on every o_N.

At the root's limiting R=53/20, the forced neighboring odd lcm has exponential rate at least log(53/40); the individual even-denominator limsup rate is at least half this. These inequalities do not by themselves exclude shrinking primitive forms, since that denominator lower rate is still below the analytic error upper rate.

## 3. Low odd-denominator indices must be multiplicatively separated

Suppose an increasing sequence of even indices N_1<N_2<... satisfies

    log o_(N_j) <= eta N_j+o(N_j)

for a fixed eta>=0. For successive M=N_j and N=N_(j+1), the upper bound lcm(o_N,o_M)<=o_N o_M and (4) imply

    (log r-eta)M <= (log2+eta)N+o(M+N).

If a subsequence of N/M is unbounded, it already obeys every finite lower separation requirement. On any subsequence where N/M is bounded, division by M makes the remainder vanish. Hence, whenever log R>eta,

    liminf_j N_(j+1)/N_j
        >= (log R-eta)/(log2+eta).                 (7)

The lower bound exceeds1 when 2eta<log(R/2). In particular, for purely dyadic or subexponential-odd-part even truncations,

    liminf_j N_(j+1)/N_j >= log R/log2.             (8)

For R=53/20 this is the exact constant log(53/20)/log2. It is greater1. This excludes bounded gaps and positive-density even-prefix sequences with subexponential odd parts, while leaving sufficiently lacunary subsequences unresolved.

## 4. The elementary integer-series form of the radius2 obstruction

Suppose o_(2k)=1 for every sufficiently large k. Put

    b_k=h_(2k-1)/(2k-1)!+h_(2k)/(2k)!.

The numerator (2k)h_(2k-1)+h_(2k) is odd, so b_k is nonzero with dyadic denominator exactly 2^v_2((2k)!). Since b_k=c_(2k)-c_(2k-2), its odd denominator is1 under the supposition. Therefore 4^k b_k is a nonzero integer. On the other hand Cauchy's estimate gives

    |4^k b_k| <= C_r(1+r)(4/r^2)^k.

When R>2 choose 2<r<R; this tends to zero, contradicting nonzero integrality. Thus a single integral-Hurwitz pullback with radius>2 cannot make all eventual even Taylor endpoint denominators purely dyadic.

This uses only Cauchy's estimate and the integer coefficient lower bound. The Pólya–Carlson theorem is not required, and no D-finiteness is assumed. In particular it applies to the nonpolynomial holomorphic Hurwitz germ constructed by root's new existence theorem. For independently selected polynomials the displayed common-block Cauchy argument is unavailable. The later author extension VARYING_PULLBACK_UNIFORM_RADIUS_SPACING.md gives another proof: difference parity holds without shared jets, and a common endpoint plus a uniform analytic bound controls the difference by both tails. In the pullback class its omitted values make that bound automatic under one common radius. Thus the spacing conclusions extend to that precisely specified varying family as well.

## 5. Archive/current-paper gate and novelty boundary

Before this target, archive query `rg -n 'dyadic.*radius|radius.*dyadic|odd.*denominator.*radius|denominator.*radius.*2|Pólya.Carlson|Polya.Carlson|integer.*power series.*radius|shared.prefix' sources work/session_20260913 work/session_20261001_astra --glob '*.md' --glob '!note_*.md' --glob '!independent*' --glob '!audit*'` found only an unrelated pullback dyadic-jet comparison. The earlier L8 parity search found no shared-prefix result. These searches give a scope boundary, not a universal priority assertion.

Current primary queries: `"integer coefficients" "radius" "Pólya Carlson" power series 2026`; `"Hurwitz" "Taylor" "denominators" "radius"`; `"Pólya–Carlson" "integer coefficients" arxiv`. Opened Bell–Chen–Nguyen–Zannier, [D-finiteness, rationality, and height III](https://arxiv.org/pdf/2306.02590), and Yu, [A multivariate version of Pólya–Carlson theorem](https://arxiv.org/html/2312.00428v1). Their integrality/analytic-continuation framework is relevant background, but their D-finite or unit-boundary results are not used. The new calculation here is the exact odd numerator of an even-endpoint block, its evaluated-denominator lcm lower bound, and the quantitative lacunarity consequence. The elementary scaled-integral-series obstruction itself is a standard analytic principle, specialized here to the complete e+G parity structure.
