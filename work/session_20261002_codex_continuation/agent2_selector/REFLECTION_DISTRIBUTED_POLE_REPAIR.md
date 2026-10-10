> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Reflection-compatible distribution of rational pole depth

2026-10-02. Original author continuation, after the complete analytic result for the unilateral quartic rational kernel. This is a distinct family and an exact interface, not a claimed successful approximation or denominator rate.

## Search and overlap before choosing the target

Archive queries covered reflection, symmetric rational poles, two-pole rational kernels, rational multipliers, and Hermite–Pade exponentials in the prior session and `sources`. Read `sources/fixed_rational_kernel_barrier.md`, Sections 1–2: its fixed positive rational kernel on a real beta interval is existing obstruction evidence; it does not cover a growing two-pole kernel on the present complex path. Read `sources/quartic_neighbor_saddle_phase_barrier.md`, Section 8.2: its positive rational combination is a polynomial selector in an existing contour variable, rather than the pole-depth redistribution below. The previous rational-period classification and matched projection are also explicit overlap.

Online primary searches concerned Hermite–Pade exponentials, rational interpolation with two poles, and reflection of pole residues. Opened full primary texts:

- Kuijlaars, Stahl, Van Assche, Wielonsky, *Type II Hermite–Pade approximation to the exponential function*, https://arxiv.org/pdf/math/0510278, Sections 1–2 and the integral/saddle discussion at Section 3.1. Exponential normality and simultaneous shared denominators are classical background, not a theorem about the current pi output.
- Crouzeix and Ruamps, *On rational approximations to the exponential*, https://www.numdam.org/item/M2AN_1977__11_3_241_0.pdf, complete paper. Classical Pade approximation and pole control overlap; its stability theorem does not estimate this projected rational center.
- Bostan, Chyzak, Lairez, Salvy, https://arxiv.org/pdf/1805.03445, Sections 3.5–3.6. Reduction modulo derivatives and fixed-pole quotient spaces are classical overlap.

The new research question is whether exact reflection-compatible pole distribution keeps both target outputs in a useful regime after projection, and what its complete final denominator costs. The exact coefficient interface below is authored here. No uniqueness or novelty for the residue method is claimed.

## 1. Exact family and target projection

Let n=4k>=4, h>=1, N=n+h, V=w²−w+1/2, and a=(1+i)/2. Put

    F0=(2V)^N/[w^(N+1)(1−w)^h],  F1=wF0.               (1)

Equivalently (1) multiplies the old `(2V)^n/w^(n+1)` kernel by the reflection-compatible endpoint factor `(2V/[w(1−w)])^h`. Poles are only at0 and1; their respective orders are N+1 and h. The degree at infinity is n−1 for F0, and at most n for their projected combination. Both kernels vanish to order N at a and bar(a).

For i=0,1 define

    Ri=Res0 Fi−Res1 Fi,
    Ai=Res1(e^(w−1)Fi), Bi=Res0(e^w Fi),
    T=(h−1)!, Mi=T Ai, mi=Mi−T Ri.

All Ri,Mi,mi are integers. Use the ACTUAL projected kernel

    F=m1F0−m0F1,
    U=R(F)=A(F)=M1R0−M0R1.                              (2)

If U!=0, take its rational Hermite primitive

    F=P′+r0/w+r1/(w−1), Pi=4 Im P(a).

The actual center and COMPLETE signed error are

    c=−[B(F)+Pi]/U,
    e+pi−c=[(1/(2pi i))∮Γ e^wF dw−2i∫_(bar a)^a F dw]/U. (3)

Gamma encloses both poles positively, and the vertical integral is upward. No exponential pole or rational primitive endpoint is omitted. The existing two-pole log increments prove that no additional period enters (3).

## 2. Exact algebraic generating interface for every n

Set z=w(1−w) and

    K_N=(1−2z)^N/z^(N+1),  F0=(1−w)^(n+1)K_N.

For formal t define the branches

    d(t)=sqrt((1−2t)/(1+2t)),
    w_t=(1−d(t))/2, Delta(t)=sqrt(1−4t²),
    d(0)=Delta(0)=1.

The identity

    Σ_(N>=0) K_N t^N=1/[z−t(1−2z)]

has simple poles at w_t and1−w_t, with derivatives ±Delta. Taking the formal residue around0 or1 before extracting coefficients gives the following EXACT expressions (the n parameter is fixed while extracting t^N):

    R0=[t^N]{(1−w_t)^(n+1)+w_t^(n+1)}/Delta,
    R1=[t^N]{w_t(1−w_t)^(n+1)+(1−w_t)w_t^(n+1)}/Delta,
    B0=[t^N] e^(w_t)(1−w_t)^(n+1)/Delta,
    B1=[t^N] w_t e^(w_t)(1−w_t)^(n+1)/Delta,
    A0=−[t^N] e^(−w_t)w_t^(n+1)/Delta,
    A1=−[t^N](1−w_t)e^(−w_t)w_t^(n+1)/Delta.             (4)

These are formal identities, not incomplete asymptotic residues. For N<n, the same identity simply describes the rational function `(1−w)^(n+1)K_N`; the intended parameters have N=n+h>n.

The complete exponential contour output for F0 is the coefficient of

    [e^(w_t)(1−w_t)^(n+1)−e^(1−w_t)w_t^(n+1)]/Delta. (5)

Its numerator cancels at t=1/2. At t=−1/2, w_t tends to infinity and exponential effects remain. The simultaneous n-growth matters: putting t=−x/2 gives s=sqrt((1+x)/(1−x)), and the ordinary residue numerator involves `(s+1)^(n+1)−(s−1)^(n+1)`, whereas A0 has the factor `exp((s−1)/2)(s−1)^(n+1)`. A fixed-n asymptotic conclusion cannot be transferred to n growing with N without retaining this bias.

For the ordinary residues, define S0(z)=2,S1(z)=1 and Sj=S_(j−1)−z S_(j−2). Then w^j+(1−w)^j=Sj(z), so

    R0=[t^N] S_(n+1)(t/(1+2t))/Delta,
    R1=[t^N] [t/(1+2t)] S_n(t/(1+2t))/Delta.          (6)

Thus the ordinary response is an explicit finite algebraic coefficient, with no undefined saddle normalization.

## 3. Actual complete numerator and denominator

All principal-part and polynomial coefficients of Fi, hence of F, are integers. Let O_N be the odd part of lcm(1,...,N), and E=N! B(F). The pole0 exponential order is N+1, so E is an integer: it is N!, not the old n!, that is required here.

The rational primitive Pi is2-integral. For a negative power at either pole, a^(-1)=1−i and (a−1)^(-1)=−1−i are Gaussian integers; the imaginary part of their t-th power has2-valuation at least floor(t/2)>=v2(t). The factor4 in Pi therefore leaves each divided negative-power term of valuation at least2.

For a polynomial coefficient p_l, expansion at infinity gives

    v2(p_l)>=ceil((n+2h+1+l)/2).

Indeed every numerator coefficient of degree j in `(1−2w+2w²)^N` is divisible by2^ceil(j/2), and the inverse denominator at infinity has integer coefficients. Multiplication by the integer projected linear multiplier preserves the weaker bound with n+2h+l replacing n+2h+1+l. At the primitive endpoint, Im(a^(l+1)) has valuation at least−ceil((l+1)/2), and division by l+1 loses at most floor(log2(n+1)). Since n>=4,h>=1, the remaining valuation, including factor4, is nonnegative. (For the unprojected kernels it is at least2.) Consequently O_N Pi is an integer.

Every odd primitive divisor is at most max(N,h−1,n+1)=N. Therefore the EXACT final reduced denominator is

    q=N! O_N |U| / gcd(N! O_N U, O_N E+N! O_N Pi).   (7)

Formula (7) retains projection content and the complete exponential/rational numerator. The low infinity degree removes the earlier h-sized polynomial dyadic allowance, but the pole0 factorial has increased from n! to N!. This is a real cost of the repair and is not a favorable rate statement.

## 4. Strictly positive actual determinant for all positive even n

The determinant nonzero premise in (3) can be removed uniformly, without a saddle argument. This subsection only requires n>=2 even and h>=1, with N=n+h.

At0 use the exact identity

    (1−2w+2w²)^N/(1−w)^h
      =Σ_(ell=0)^N binom(N,ell) w^(2ell)(1−w)^(N+n−2ell).

For j=N,N−1 all contributing exponents N+n−2ell are nonnegative and at least j−2ell. Therefore

    d_j=(−1)^j D_j,
    D_j=Σ_(ell=0)^floor(j/2) binom(N,ell)
                                     binom(N+n−2ell,j−2ell)>0. (8)

At1 use

    H1=(1+2u+2u²)^N/(1+u)^(N+1)
      =Σ_(ell=0)^N binom(N,ell) u^(2ell)(1+u)^(N−1−2ell).

For 0<=j<=L=h−1<N−1, the same reasoning gives

    c_j=Σ_(ell=0)^floor(j/2) binom(N,ell)
                                     binom(N−1−2ell,j−2ell)>0. (9)

The two particular residue sums are

    D_N=Σ_(ell=0)^floor(N/2) binom(N,ell)binom(N+n−2ell,n),
    c_L=Σ_(ell=0)^floor(L/2) binom(N,ell)binom(N−1−2ell,n).

On the common range, the first upper binomial argument exceeds the second by n+1 and both lower arguments are n>=1. Thus every common term is strictly larger, with any additional D_N terms positive. Consequently D_N>c_L.

The actual ordinary responses, with c_(−1)=0, satisfy

    R0=(−1)^h(D_N−c_L),
    R1=−(−1)^h(D_(N−1)+c_L+c_(L−1)).               (10)

The actual exponential residues are (−1)^h times sums of positive c_j/(L−j)! and positive (c_j+c_(j−1))/(L−j)!, respectively. Hence A0 and A1 both have sign (−1)^h, whereas R0 and R1 have opposite signs. Both summands in A1R0−A0R1 are strictly positive. Therefore

    U=T(A1R0−A0R1)>0 for every positive even n and h>=1. (11)

This is the ACTUAL projected determinant, not a generic sequence normality theorem. It establishes the denominator in (3) everywhere in the stated domain. It supplies no approximation error estimate by itself.

## 5. Complete factorial dyadic obstruction for EVERY h

Return to the project domain n=4k>=4,h>=1,N=n+h. No binary eligibility is needed for the following exact identity:

    E=N!B(F) is odd,
    v2(q)=v2(N!)+v2(U)>=v2(N!)+1.                 (12)

Proof. The infinity coefficient estimate above shows Res0 Fi+Res1 Fi is divisible by2^(n/2+h), hence Ri=2Res0 Fi−(Res0 Fi+Res1 Fi) is even for both rows. At1, c0=1 and c1=N−1. Modulo2, only falling-factorial terms j=0,1 can survive. If h is odd, L=h−1 is even, so M0 and M1 are odd. If h is even, L is odd and N is even, so

    M0=c0+L c1=0 mod2,
    M1=c0+L(c1+c0)=1 mod2.

The sign (−1)^h does not change parity. Thus m1 is always odd and m0=h mod2, since subtraction of T Ri preserves parity.

At0 the regular factor has d0=1,d1=h−2N. If N is even, the falling-factorial sums give N!B0 odd and N!B1 even. If N is odd, then h is odd, d1 is odd, and the first two terms of N!B0 are1+N d1=0 mod2; every j>=2 falling factorial is even. Meanwhile N!B1 has odd leading term N d0 and all higher terms even. Thus in the second case N!B0 is even and N!B1 odd. In both cases m1(N!B0)−m0(N!B1) is odd, proving E odd.

Section3 proves Pi is2-integral. Hence B(F)+Pi has EXACT valuation −v2(N!), with no possible cancellation at its lowest dyadic valuation. The actual U is an even nonzero integer by Section4. Dividing the complete numerator by U proves (12). In particular

    q>=2^(N−s2(N)+1)                              (13)

for EVERY h>=1, where s2 is binary digit sum. At h proportional to nlogn this is an h-sized exponential cost, and at h of order n² it is quadratic exponential. No analytic error is replaced by this arithmetic lower bound.

## 6. A uniform exact valuation of U on eligible nodes

Suppose n and h are divisible by4, h>=4, and binom(N+h−1,N) is odd. One explicit unbounded subcase is N=n+h a power of2>N and h=N−n. At0 write

    H0=(1−2w+2w²)^N/(1−w)^h=Σ d_j w^j.

Modulo2, d_N=binom(N+h−1,N) is odd by assumption; the power-of-two subcase satisfies this by Lucas since h−1<N. Also d_(N−1) is even since N+h−2 is even. The sum of residues of either Fi is its1/w coefficient at infinity, divisible by2^(n/2+h). Hence

    v2(R0)=1, v2(R1)>=2.                            (14)

At1 write u=w−1 and

    H1=(1+2u+2u²)^N/(1+u)^(N+1)=Σ c_j u^j.

The sign (−1)^h is positive here. Since c0=1,c1=N−1=3 mod4, and c0,c1,c2,c3 are odd, the falling-factorial expressions with L=h−1=3 mod4 give

    M0=Σ_(j=0)^L c_j (L)_j=2 mod4,
    M1=Σ_(j=0)^L(c_j+c_(j−1))(L)_j=1 mod2.

Terms j=2,3 cancel modulo4 and j>=4 have falling factorial divisible by4. As v2(T)>=1, (8) gives v2(m0)=1 and m1 odd. Thus

    v2(U)=1, U!=0.                                 (15)

Moreover N!B0=Σ d_j(N)_j=1 mod4 and N!B1 is divisible by4, because N is a multiple of4. Hence E is odd. The complete primitive term Pi has nonnegative2-valuation (in fact at least2 in this regime), so (7) proves

    v2(q)=v2(N!)+1.                                (16)

This proves the complete reduced-center dyadic valuation on an unbounded explicitly defined parameter set, and it records the compulsory h-sized dyadic denominator cost. The all-parameter nonzero theorem is (11); neither theorem asserts that the centers approximate e+pi. Complete analytic error is assigned to the analysis agent as independent original work.
