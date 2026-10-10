> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Reflected projection: a prime-independent determinant and actual odd-denominator survival

Author result L20, 2026-10-02. This is an original arithmetic continuation of L19, not an independent audit. The target gate, queries, primary URLs and overlap boundary are recorded in TARGET_LEDGER.md, L20. The symbolic result holds for every odd prime; the small exact receipt supports definitions and one complete gcd computation, and is not a prime atlas.

The main conclusion is that the complete reflected exponential numerator on p|n has residue Z_(N mod p), where Z_r is one prime-independent integer determinant. Its first two residue classes are universally units: Z_0=1 and Z_1=−1. A residue unit forces the complete actual denominator to retain v_p(N!)+v_p(U), after Pi and the final gcd are included. The familiar five-prime formula is special: Z_2=13 supplies a zero at p=13.

## 1. Exact family and complete evaluated denominator

Use the selector's exact reflected family, with positive n divisible by 4, h≥1, N=n+h, L=h−1, epsilon=(−1)^h, T=L!:

    V(w)=w²−w+1/2,
    F0(w)=(2V(w))^N/[w^(N+1)(1−w)^h],  F1(w)=wF0(w).

The integral coefficient series at the two poles are

    d(w)=(1−2w+2w²)^N/(1−w)^h=Σ d_j w^j,
    c(u)=(1+2u+2u²)^N/(1+u)^(N+1)=Σ c_j u^j,
    c_(−1)=d_(−1)=0.

Write (a)_j=a(a−1)…(a−j+1), with (a)_0=1. The projection and exponential endpoint are exactly

    R0=d_N−epsilon c_L,
    R1=d_(N−1)−epsilon(c_L+c_(L−1)),
    M0=epsilon Σ_(j=0)^L c_j(L)_j,
    M1=epsilon Σ_(j=0)^L(c_j+c_(j−1))(L)_j,
    m_i=M_i−TR_i,
    U=M1 R0−M0 R1,
    X_N=Σ_(j=0)^N d_j(N)_j,
    Y_N=Σ_(j=1)^N d_(j−1)(N)_j,
    E=m1 X_N−m0 Y_N.

Selector's REFLECTION_EXACT_COEFFICIENT_HANDOFF.md and REFLECTION_DISTRIBUTED_POLE_REPAIR.md retain both poles and the polynomial part. In their notation Pi=4 Im P(a), a=(1+i)/2, for the complete primitive polynomial/principal part P, and the actual center is

    c_n,h=−(E/N!+Pi)/U.

For O_N=oddLCM(1,…,N), the FULL reduced denominator is

    q=N! O_N U / gcd(N! O_N U, O_N E+N! O_N Pi).

Here U is a positive integer for positive even n and h≥1, by selector's authored nonvanishing result. All coefficients in the partial/polynomial primitive source are integral, O_N Pi is integral, and every primitive exponent denominator is at most N. These exact interfaces are used as attributed definitions/results, rather than independently audited here. In particular neither v_p(E) nor a raw factorial clearer alone is the actual denominator.

## 2. Universal integer determinant

For each integer r≥1 define ordinary integral series

    d^[r](w)=(1−2w+2w²)^r/(1−w)^r,
    c^[r](u)=(1+2u+2u²)^r/(1+u)^(r+1).

Only degrees at most r are used. Let d^[r]_j,c^[r]_j be their coefficients and c^[r]_(−1)=0. Define the integers

    A_r=Σ_(j=0)^(r−1) c^[r]_j(r−1)_j,
    B_r=Σ_(j=0)^(r−1)(c^[r]_j+c^[r]_(j−1))(r−1)_j,
    X_r=Σ_(j=0)^r d^[r]_j(r)_j,
    Y_r=Σ_(j=1)^r d^[r]_(j−1)(r)_j,
    Z_r=B_r X_r−A_r Y_r.

Set Z_0=1 separately. This gives a prime-independent integer 2×2 determinant, with no search over prime residues:

| r | A_r | B_r | X_r | Y_r | Z_r |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 1 | −1 |
| 2 | 2 | 3 | 3 | −2 | 13 |
| 3 | 13 | 19 | 4 | 21 | −197 |
| 4 | 82 | 145 | 81 | −92 | 19289 |

**Theorem 1.** For every odd prime p, p|n and h≥p+1, put r=N mod p, 0≤r<p. Then

    epsilon E ≡ Z_r (mod p).

The stronger condition p(p−1)|n proposed at the start of this target is therefore sufficient but unnecessary for this arithmetic residue theorem.

Proof. Since L≥p, T=L!≡0 mod p and m_i≡M_i. Every (N)_j and (L)_j with j≥p contains a multiple of p. Thus every projected exponential contraction uses only coefficients of degree below p. Frobenius gives Q(w)^p=Q(w^p) mod p for the two integral quadratics, and (1±w)^p=1±w^p. Consequently these low coefficients depend only on N and h mod p. As p|n, these two residues are equal to r.

If 1≤r<p, the low coefficients are those of d^[r],c^[r]. Moreover (L)_j≡(r−1)_j vanishes for j≥r, and (N)_j≡(r)_j vanishes for j≥r+1. Hence M0/epsilon≡A_r, M1/epsilon≡B_r, X_N≡X_r, Y_N≡Y_r. This gives the determinant.

If r=0, the low d series is 1 and the low c series is (1+u)^−1. Then X_N=1 mod p and Y_N=0 mod p because (N)_j vanishes for all j≥1. Also c_j+c_(j−1)=0 mod p for j≥1, so M1/epsilon=1 mod p. The value of M0 is immaterial. This proves epsilon E=1 mod p, including the otherwise exceptional r=0 class. ∎

**Corollary 1.** Under these hypotheses, N≡0 or 1 mod p implies p∤E. For r=1 the surviving four quantities are exactly A=B=Y=1 and X=0, so epsilon E=−1 mod p at every odd prime.

## 3. Why the five-prime expression is special

At p=5, the list Z_0,…,Z_4 reduces to 1,4,3,3,4. On that finite field it is exactly 1−2r² and has no zero. This recovers L19 without carrying a prime-dependent list into the all-prime theorem.

At p=13,r=2, however, Z_2=13 vanishes whereas 1−2r²=−7=6 mod13. Both p=5 and p=13 have (−1/p)=1, so that character does not enforce the five-prime nonvanishing phenomenon. This disproves the specific universal polynomial extension and automatic all-residue unit survival; it does not purport to rule out every possible character-dependent formula.

The receipt evaluates the complete integer E for n=156,h=28,N=184, retaining the m_i=M_i−TR_i correction. It gives v_13(E)=1 and the same residue zero. A zero of E does not establish any particular surviving valuation or cancellation in actual q; Pi and U must still be compared at the required depths. No conclusion for that example's q_13 is inferred here.

## 4. Strict comparison with the full primitive and final gcd

For every odd p the Gaussian numbers a,a−1 and their inverses used in the principal parts are p-integral: their denominators/norm denominators use only 2. The ordinary coefficients of the polynomial/partial fraction source are integers, and integration introduces only 1/t with t≤N. Taking 4 Im preserves this p-integrality bound. Thus, for the COMPLETE Pi,

    v_p(Pi)≥−floor(log_p N).

This includes both pole principal parts and the polynomial at infinity. For N≥2p,

    v_p(N!)>floor(log_p N).

Indeed 2p≤N<p² gives v_p(N!)≥2>1. If t=floor(log_p N)≥2, then v_p(N!)≥floor(N/p)≥p^(t−1)>t for odd p. This is a strict comparison, not an asymptotic assumption.

**Theorem 2 (actual denominator).** Under Theorem1's hypotheses and N≥2p, if p∤Z_(N mod p), then

    v_p(q)=v_p(N!)+v_p(U).

Proof. E is a unit, so v_p(E/N!)=−v_p(N!), strictly smaller than v_p(Pi). The full sum therefore has that exact valuation. Division by the positive integer U gives v_p(c_n,h)=−v_p(N!)−v_p(U)<0. This is exactly the negative valuation of the reduced rational center, hence the asserted denominator valuation. Equivalently it is the valuation remaining in the full O_N-cleared numerator after the displayed final gcd, not a coefficient-content assertion. ∎

If p|Z_r, the theorem is silent. It does not promote a first-digit numerator zero to factorial cancellation, and does not exclude survival of most or all deeper factorial content.

## 5. Simultaneous survival on convergent critical subsequences

Let S be ANY fixed finite set of odd primes. Define fixed integers

    A=lcm(4,{p(p−1):p∈S}),
    J=lcm({ord_p(2):p∈S}).

Take s→∞ through multiples of J and N=2^s. Then N≡1 mod p for every p∈S. Let t_s be the large continuous critical root of

    Psi(t,N)=t^(3/2)/sqrt(N)−2sqrt(N)/sqrt(t)
             +log(sqrt(N)/(4t^(3/2)))=0,

and put n=A·nearest(t_s/A), h=N−n. Eventually n>0, n,h are divisible by4, h≥max(S)+1 and N≥2max(S). At every p∈S, p|n and N modp=1, so Theorem2 gives simultaneously

    v_p(q)=v_p(N!)+v_p(U)≥v_p(N!).

The complete analytic convergence is attributed to analysis's FIXED_CONGRUENCE_INVERSE_CRITICAL_COROLLARY.md (and POWER_TWO_INVERSE_CRITICAL_SUBSEQUENCE.md for the original modulus20): rounding in any fixed A gives

    c_n,h−(e+pi)=O_A(N^(−1/4)),

with both poles, determinant, and both vertical endpoints retained. Arithmetic here does not rederive that error. For large N, 0<n<N; the binary digit of N in 2N−n−1 is1, so binom(2N−n−1,N) is odd. Selector's eligible power-two dyadic result therefore gives v_2(U)=1 and v_2(q)=v_2(N!)+1=N for these n,h. Legendre's factorial valuation identity gives the unconditional odd-prime lower rate

    log q ≥ N Σ_(p∈S) log(p)/(p−1) − O_S(log N).

The complete dyadic contribution N log2 can also be added to this bound. No estimate for v_p(U) is needed.

This is an all-index theorem along the specified infinite subsequence, obtained by a universal residue class, rather than a finite atlas extrapolation. S and A remain fixed in the statement; no distribution theorem for other residues, uniform growing-prime theorem, or favorable primitive approximation rate is inferred.

## 6. Fixed norm support cannot remove these chosen layers

Let delta_N be ANY rational correction that is p-integral for each p∈S. It may vary in height and degree with N. Since Theorem2 gives v_p(c_n,h)<0, the ultrametric inequality is strict between the center and correction, and

    v_p(c_n,h+delta_N)=v_p(c_n,h),
    v_p(q_corrected)=v_p(N!)+v_p(U)  (p∈S).

In particular a finite chain of rational corrections whose odd denominator support lies in a fixed finite set T is integral at every odd p outside T. Choosing any fixed S disjoint from T preserves all the factorial layers above even if the dyadic denominator is cancelled exactly. This applies to norm5 corrections by choosing S outside {5}, and to zero-odd-norm corrections if their complete shifts are integral at those primes. The exact correction's written coefficient denominator alone is not used to decide this support; the complete evaluated rational shift must be p-integral.

The rate sum can be made arbitrarily large by choosing a larger fixed S outside any fixed T, since the sum over primes of log(p)/(p−1) diverges. This means: for each prescribed finite rate, there is a fixed modulus and an infinite convergent subsequence with at least that surviving rate. It does NOT assert that one unspecified original sequence has that rate, or that a varying modulus is analytically uniform. It supplies an obstruction to a fixed finite collection of odd norm repairs removing all factorial layers. Growing support and corrections with negative p-valuations at chosen primes remain separate arithmetic cases.

## 7. Exact evidence and scope

REFLECTED_UNIVERSAL_PRIME_RESIDUE_RECEIPT.json stores the first five prime-independent integer determinants, one p13 residue counterexample, and one FULL center at n=60,N=256,h=196. The latter has

    v_3(N!)=126, v_3(U)=3, v_3(Pi)=−4, actual v_3(q)=129,
    v_5(N!)=63,  v_5(U)=0, v_5(Pi)=−2, actual v_5(q)=63,
    actual v_2(q)=256.

Its complete numerator/denominator/gcd are computed exactly, with hashes and bit lengths retained. The script's small optional integer-state return was added to the existing L19 exact function without rerunning or overwriting the L19 receipt. No prime atlas was run and no experiment is used as an infinite theorem. No shrinking primitive form or irrationality conclusion about e+pi follows from this result alone.
