> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Recovered pending main-agent deductions

Verbatim attributed author drafts recovered from the original local transcript. These are NOT independently verified theorems. Later corrections and the current research plan take precedence. Read selectively; do not repeat accepted old audits. The actual e+pi question remains OPEN.

## Source 9: 2026-10-01T13:31:20+0800

Original author: primary agent; message ID: [session identifier removed].
Exact source text SHA-256: 1051475e618b13cb1bc5d52c16d7c612858751315e53ead70c9bdaa912e3bf84.

The third assignment was rejected because its identifier ended in `6d4a`; the existing third agent’s identifier ends in `6d4d`. The other two assignments were accepted.

The proposed Laguerre row-sign lemma has a direct proof. The following derivation is not yet saved or independently audited.

Define T_n(t^m)=n!x^m/(n+m)! and J_n(x^m)=x^(m+1)/(n+m+1). Put F_(n,k)=T_n(p_k) and S_(n,k)=(I−J_n)F_(n,k). For n≥24, b=⌊n/2⌋ and 0≤k≤n+b−1, we obtain, throughout 0≤x≤1,

    (−1)^(k+r) F_(n,k)^(r)(x)>0   for 0≤r≤k,
    (−1)^(k+r) S_(n,k)^(r)(x)>0   for 0≤r≤k+1.

To prove this, expand the monic transformed Legendre polynomial as

    p_k(t)=Σ_j c_(k,j)(t−1/2)^(k−2j),
    c_(k,j)=(2k−2j)!/[4^j j!(k−j)!(k−2j)! binom(2k,k)]>0.

The finite coefficient formula for generalized Laguerre polynomials gives

    T_n((t−1/2)^m)=(-1/2)^m m!n!/(n+m)! L_m^(n)(2x).

It remains to control the Laguerre factors and their derivatives. For α≥0, their monic recurrence has diagonal coefficients α+2j+1 and adjacent symmetric matrix entries √((j+1)(α+j+1)). Both the recurrence and the derivative identity

    d^r/dx^r L_m^(n)(2x)=(−2)^r L_(m−r)^(n+r)(2x)

follow by comparing coefficients in the finite Laguerre series.

The recurrence identifies the zeros of L_m^(α) with the eigenvalues of its m×m symmetric tridiagonal matrix. For row j, the diagonal minus the sum of the adjacent absolute entries is at least

    α+2j+1−2√((j+1)(α+j+1))
      =(√(α+j+1)−√(j+1))²−1.

Consequently every zero is at least

    (√(α+m)−√m)²−1.

This bound increases with α and decreases with m. Thus, whenever α≥n and 1≤m≤3n/2, every zero exceeds

    n(4−√15)−1>2   for n≥24.

The last inequality follows exactly from √15<31/8. Since L_m^(α)(0)>0, these polynomials are positive on [0,2]; degree zero is immediate. The same argument applies to every surviving derivative, whose parameter increases and degree decreases.

All degrees k−2j have the parity of k. Hence the positive coefficients c_(k,j) and the derivative identity establish the asserted signs for F. Strictness follows from the leading term m=k.

Finally, T_n(tP)=J_nT_n(P), so S_(n,k)=T_n((1−t)p_k). For each centered monomial,

    (1−t)(t−1/2)^m=(t−1/2)^m/2−(t−1/2)^(m+1).

After transformation and differentiation, both terms have the same required sign. Their largest degree is k+1≤n+b≤3n/2, so the preceding zero bound applies. The leading degree k+1 supplies strictness through derivative order k+1.

This establishes individual row and derivative signs in the stated range. It does not establish the signs of the endpoint determinants: their alternating sums still require control. The endpoint, reduced-denominator and full-remainder gaps remain unresolved, and no proof concerning the irrationality of e+π is claimed.

## Source 46: 2026-10-02T03:51:51+0800

Original author: primary agent; message ID: [session identifier removed].
Exact source text SHA-256: 7f102fce3a05d425673c0e29b8996e984b2d6de7094eae6ed286caa2ff09127c.

I will preserve the four accepted assignments. A new exact identity gives the main research a complementary target: **denominator mismatch can obstruct a small center denominator before we estimate cancellation depth.**

Write the reduced companions as

α=a/Q, γ=b/B, c=α+γ=p/q.

Set G=gcd(Q,B), u=Q/G, v=B/G, and N=av+bu. Then gcd(u,v)=1. Reduction of the two companions also gives gcd(N,uv)=1: modulo any prime dividing u, only av remains, and both factors are units; the argument for v is identical.

Consequently, defining δ=gcd(G,|N|), we obtain exactly

q=(G/δ)uv, uv divides q, gcd(δ,uv)=1.

Moreover, gcd(q,B)=B/δ, so this δ is precisely the previously defined overlap deficit B/gcd(q,B). The identities become

**Q=δq/v, B=δq/u, av+bu=δp.**

These formulas include zero numerators using reduced denominator one. They concern the actual rational companions, including the endpoint correction in γ.

Two useful consequences follow.

First, the mismatch between the denominator prime powers satisfies

**log(Q/G)+log(B/G)≤log q.**

Thus a proved positive factorial-scale lower bound for this mismatch would exclude q=exp(O(n)), without estimating the equal-depth cancellation deficit. This gives a distinct arithmetic target alongside Child 3’s existing deficit assignment.

Second, suppose X=n log n and log q=o(X). Since u,v divide q,

0≤log Q−log δ≤log q,

0≤log B−log δ≤log q.

Hence

**log Q=log B=log δ+o(X).**

The small-q target therefore requires the exponential denominator, combined logarithmic denominator, and cancellation deficit to agree at factorial scale. Merely proving that each is large is insufficient: their prime-power mismatch must also be subfactorial.

Using the retained factorial exponential accuracy, the earlier approximation inequality gives liminf log δ/X≥1/2. The identities above show more precisely what this demands: almost all factorial-scale denominator mass must be shared and then canceled in the endpoint-corrected numerator av+bu. Its uncanceled denominator is exactly q.

This is a new, **unsaved author proof**, with no computation or independent examination claimed. The next main arithmetic direction is to express u and v in the canonical integer data and seek a mismatch bound; the children’s current assignments remain unchanged. Neither this condition nor the existing local results resolves e+π.

## Source 47: 2026-10-02T03:53:49+0800

Original author: primary agent; message ID: [session identifier removed].
Exact source text SHA-256: 3c13c6ec285b1b23b4cbcb65b814f9bf59e252ae2381083ac7cbe73f703b7c7d.

The canonical denominator-mismatch target reduces to **two gcds that omit the logarithmic moment numerator**. This is a new author deduction, not yet saved or independently reviewed. The four accepted child assignments remain unchanged.

Use the retained canonical identities

α=𝒜/(F d Dg), κ=ℛ/(F Dg), β=Tz/(L Dg),

where F=(n!)², d=(n+b−1)!/n!, ℛ=Δx₀, and all displayed numerators are integers. Here Dg>0 is the actual Gram contraction and L is the retained moment clearer. The center is c=α+κ+β, with actual reduced denominator q.

Define

A★ = Fd / gcd(Fd, L|𝒜|),

K★ = F / gcd(F, L|ℛ|),

M★ = A★K★ / gcd(A★,K★)².

Then **M★ divides q**. This holds without assumptions about coefficient content, prime units, or logarithmic noncancellation.

To prove it, set H=L Dg and γ=κ+β. At a prime p, write h=vₚ(H), and let a,k,b be the denominator exponents of α,κ,γ respectively. Because den(β) divides H, adding β preserves every denominator depth of κ exceeding h. Thus

(b−h)₊=(k−h)₊.

The retained rational-addition identity shows that p^|a−b| divides q. Since truncation is distance-decreasing,

|(a−h)₊−(k−h)₊|≤|a−b|.

Therefore the mismatch between the denominators remaining above H also divides q. Those remaining denominators are exactly A★ and K★: direct valuation calculation gives

(a−h)₊=(vₚ(Fd)−vₚ(L)−vₚ(𝒜))₊,

(k−h)₊=(vₚ(F)−vₚ(L)−vₚ(ℛ))₊.

These are precisely their gcd formulas. Zero numerators are covered by gcd(N,0)=N.

The cancellation of Dg from these formulas is algebraic; it assumes nothing about its content. The divisor also eliminates Tz entirely. Consequently, the main’s distinct arithmetic target is now

**log M★ = Σₚ |vₚ(A★)−vₚ(K★)| log p.**

A positive lower rate for this sum at scale n log n would exclude q=exp(O(n)). Conversely, a geometric-denominator construction necessarily has log M★=o(n log n), alongside the previously proved requirement that its total cancellation deficit have lower rate at least 1/2.

No positive global mismatch rate has yet been established. The retained 11-adic Gram example has equal depths here, so it contributes no mismatch; its cancellation remains part of Child 3’s separate deficit problem. This reduction supplies a simpler target for the main’s arithmetic work, without deciding whether e+π is irrational.

## Source 48: 2026-10-02T03:55:33+0800

Original author: primary agent; message ID: [session identifier removed].
Exact source text SHA-256: 86c6d74f86b2c6317207cde9fd451368842ad64d7556e60203d7e453e2563de5.

Child 4’s completion report is received; its new global factorization awaits inspection. The other three assignments remain active.

The main arithmetic reduction strengthens further: **the complete center’s denominator above the logarithmic clearer depends on one endpoint-corrected numerator.**

Retain the canonical identities

α=𝒜/(FdDg), κ=ℛ/(FDg), β=Tz/(LDg),

where F=(n!)², d=(n+b−1)!/n!, and c=α+κ+β. All displayed numerators are integers. Define

H=LDg, Z=Fd, S=𝒜+dℛ,
g₀=gcd(Z,|LS|), qhigh=Z/g₀, s₀=LS/g₀.

Then

Hc=LS/Z+Tz=(s₀+qhigh·Tz)/qhigh.

Because gcd(s₀,qhigh)=1, this fraction is reduced. Consequently, for the actual q=den(c),

**qhigh=q/gcd(q,H),**

and, more explicitly,

**q=H·qhigh/gcd(H,|s₀+qhigh·Tz|).**

These identities include zero numerators. They retain the endpoint correction in S.

Thus qhigh divides q, while its formula contains neither Dg nor Tz. The previously derived mismatch divisor M★ also divides qhigh: apply the rational-addition mismatch lemma to L𝒜/(Fd) and Lℛ/F.

There is an exact primewise consequence. Put z=vₚ(Fd), ℓ=vₚ(L), and s=vₚ(S). Whenever s<z−ℓ,

vₚ(qhigh)=z−ℓ−s>0,

so the remaining numerator is a p-unit and

**vₚ(q)=vₚ(Dg)+z−s.**

At these primes, the logarithmic numerator cannot change the denominator depth. Only primes with qhigh having zero depth retain a possible cancellation involving Tz.

For b=3,m=1, this gives a particularly strong necessary condition for geometric q. Since

Fd/gcd(Fd,|S|) divides L·qhigh,

we have

log gcd(Fd,|S|) ≥ log(Fd)−log L−log q.

Here log L=O(n) and d=(n+1)(n+2). Therefore:

- If log q=o(n log n), then **log gcd(Fd,|S|)/(n log n)→2**.
- If log q=O(n), then **log gcd(Fd,|S|)≥2log(n!)−O(n)**.

A small center denominator therefore requires almost all the double-factorial denominator mass to cancel already in **S=𝒜+dΔx₀**, before the logarithmic numerator matters. This supplies a simpler main research target than the full summed-numerator gcd.

This is an unsaved author deduction; no calculation or independent examination is claimed. No bound establishing or excluding the required global content has been proved. The irrationality of e+π remains unresolved.
