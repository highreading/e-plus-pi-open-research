> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Quartic family: actual dyadic denominator and signed primitive growth

2026-10-02. New author theorem for the target-preserving family introduced in `QUARTIC_ENDPOINT_MULTIPLIER_TARGET.md`. This is an exclusion of specified approximation forms, not a solution of the rationality problem for e+pi. The exact contour and final denominator are retained.

## Search and overlap before this extension

Archive search before the saddle extension covered quartic, `1+4w^4`, the proposed saddle value `(20−4i sqrt(2))/27`, and endpoint multipliers in the preceding sessions. The hits concern different quartic saddle equations; no present diagonal multiplier saddle or dyadic unit allocation was located. The exact old dyadic numerator argument was read in `LARGE_SELECTOR_DYADIC_DENOMINATOR_DRAFT.md`; its unique lowest term is reused only after checking that the new J is divisible by four and that every new coefficient retains its bound. The new normalization congruence is derived below.

Primary online search and opened full text: Temme, *Uniform Asymptotic Methods for Integrals*, https://arxiv.org/pdf/1308.1547, Sections 2.3 and 4. Complex Gaussian and analytic-parameter saddle expansion are classical overlap. The actual globally admissible contour and two eligible nodes here are new obligations. A separate binomial prime-power search opened Granville's primary paper at https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/granville.pdf (its extracted text was corrupted) and its readable primary HTML, https://www.cecm.sfu.ca/organics/papers/granville/paper/binomial/html/binomial.html, Introduction and Elementary Number Theory. The factorial valuation and Lucas congruence are classical; no novelty is claimed for them.

## 1. Exact primitive dyadic arithmetic

Let n=4k and h≥0 be EVEN. Use the diagonal selector

    B(t)=(1−2t+2t²)^n(1−4t+2t²)^h[1+4(1−t)^4]^h,
    N=2n+6h, J=n+6h,
    K=t^n B^(n)/n!, U=K(1), T=calL((K−U)/(t−1)),
    c=α+β, β=T/U,
    α=Vexp/(n!J!U),
    Vexp=Σ_(j=n)^N b_j(J)_(N−j)D_j,
    D_j=j!Σ_(a=0)^j1/a!.

Assume U≠0. The old complete-center identity applies by linearity to this integer selector. The new factor's coefficients satisfy v_2([t^j]D)≥ceil(j/2), and so v_2(b_j)≥ceil(j/2). Its leading coefficient is 4, hence

    b_N=2^(n+3h)=2^(N/2).

Now J is divisible by four. For 1≤ell≤J the first-four-factors argument gives

    v_2((J)_ell)≥floor(ell/2)+1.

Thus every j<N term of Vexp has valuation at least N/2+1; the final term has exactly N/2 because D_N is odd. Therefore

    v_2(Vexp)=N/2.

The full logarithmic T has v_2(T)≥1 as proved for the new selector in the preceding note. Also v_2(n!)+v_2(J!)≥3N/4. Consequently the exponential component has strictly lower 2-adic valuation than the logarithmic component. There can be no final cancellation at that valuation. For the denominator q=den(c) AFTER complete rational reduction,

    v_2(q)=v_2(n!)+v_2(J!)+v_2(U)−N/2.               (1)

All quantities on the right are actual endpoint/factorial values. This is not a row-clearer estimate.

At t=1+x, U=(-1)^h v_n(h), where

    v_n(h)=[x^n](1+2x+2x²)^n(1−2x²)^h(1+4x^4)^h.

Pairing the linear terms in the first factor shows

    [x^(2j)](1+2x+2x²)^n /2^j =binom(n,j) mod 2.

Terms with at least two linear selections have an additional power of two; the only surviving terms choose quadratic coefficients. The coefficient convolution therefore gives

    U/2^r =[Y^r](1+Y)^(n+h)(1+Y²)^h
           =binom(n+3h,r) mod 2,       r=n/2.          (2)

This also proves the divisibility before taking the quotient. In particular for n=2^s, s≥4, let k=n/4 and h=2m. Lucas' theorem reduces (2) to

    U/2^r =binom(2k+3m,k) mod 2.

Since k is a power of two, this is the k-th binary digit of 3m. Both m≡k and m≡k+1 modulo 2k are eligible because 3k≡k and 3(k+1)≡k+3 modulo 2k, with k+3<2k for k≥4. At BOTH corresponding nodes U is nonzero and v_2(U)=r.

For every initial M there is a first m0≥M congruent to k modulo 2k; it satisfies M≤m0<M+2k. Thus the two nodes m0,m0+1 are selected within O(n), explicitly, with no response-zero division. On each, Legendre's factorial formula turns (1) into

    v_2(q)=3n/2+3h−s_2(n)−s_2(n+6h).              (3)

For h=κ n log n+O(n), κ>0 fixed, this proves

    log q ≥3κ log2 · n log n+O_κ(n).                (4)

## 2. Explicit global contour for the actual upper moment

Put a=(1+i)/2, V=w²−w+1/2, and

    G(w)=(1−2w²)(1+4w^4)=1−2w²+4w^4−8w^6,
    J_(n,h)=∫_(1/2)^a (V(w)/w)^n G(w)^h dw/w.

There is a unique upper-right stationary point

    σ=x0+iy0,
    x0²=(sqrt3+1)/12, y0²=(sqrt3−1)/12,
    σ²=(1+i sqrt2)/6,
    g0=G(σ)=(20−4i sqrt2)/27,
    γ=|g0|=4sqrt3/9<1.                             (5)

G'(σ)=0 and G''(σ)≠0. We do not infer dominance merely by listing critical points. Deform the original upper half-segment to the path from 1/2 along the real axis to x0, up the vertical segment x0+i[0,1/2], then horizontally to a. Its rectangle lies in Re(w)≥x0>19/40, so the only pole at zero is outside; the integrand is single-valued and holomorphic there.

The following exact global gap proves that this contour passes through a contributing and dominant saddle. Write v=y² and v0=y0². Direct polynomial identity gives

    16/27−|G(x0+iy)|²=−64(v−v0)² Q(v),

    Q(v)=v^4+(2sqrt3/3+4/3)v³
         +(7sqrt3/12+3/2)v²+(sqrt3/6+67/108)v
         −331sqrt3/1296−1193/5184.

All nonconstant coefficients of Q are positive. For 0≤v≤1/4,

    Q(v)≤Q(1/4)=901/20736−865sqrt3/5184<0.

The strict final sign is an exact rational comparison with sqrt3. Thus the saddle is the unique maximum of |G| on the entire vertical segment and has a quadratic gap there. The symbolic identity was saved in `quartic_saddle_geometry.json`; its displayed numerical roots are diagnostic only and are not used in this proof.

The bottom connector obeys G(w)≤G(19/40)<2/3, because G is real positive and decreasing there. On the top connector G(a)=0, |G'|≤17 throughout |w|≤1/sqrt2, and its length is <1/40, hence |G|<17/40. Both bounds are strictly less than γ. These connectors are therefore exponentially smaller in h than the saddle contribution, including the factor (V/w)^n when n/h tends to zero.

## 3. Uniform perturbed saddle and relative error

Let ε=n/h and locally define

    Φ_ε(w)=log G(w)+ε log(V(w)/w).

The logs are taken on fixed disks around σ avoiding their zeros; their powers represent the original integer integrand. The implicit-function theorem gives a unique analytic stationary point σ_ε=σ+O(ε), and

    b_ε=Φ_ε''(σ_ε), Re(b_ε)>c>0

for all sufficiently small nonnegative ε. The positive real part follows at ε=0 from the strict vertical quadratic maximum just proved and continues by continuity. All local derivatives and amplitudes are uniformly bounded and the saddle amplitude 1/σ_ε stays nonzero.

Use the vertical contour through Re(σ_ε), with the same bottom/top connectors. Outside a fixed saddle disk the strict |G| gap persists uniformly. The other amplitude factor has upper bound C^n on the compact contour; since n/h→0 this cannot overcome a fixed exponential gap in h. Zeros at a make that bound smaller, and no logarithmic analyticity at a is required. In the disk, uniform strict concavity of Re Φ along the vertical direction gives the Gaussian quadratic bound about σ_ε. These facts control every competing contour piece.

Expand locally through fourth order on a symmetric vertical interval about σ_ε, then put the displacement equal to iu/sqrt(h). The leading integral is the nonzero complex Gaussian with Re(b_ε)>c. The first cubic contribution is odd and integrates to zero; quartic and squared cubic terms are O(1/h) relative to it. Bounded higher derivatives and a restriction |u|≤h^(1/10) give a uniform smaller remainder, while the quadratic gap makes the complementary tails exponentially small. This supplies the relative, rather than merely absolute, formula

    J_(n,h)= i/σ_ε · sqrt(2π/(h b_ε))
             exp[hΦ_ε(σ_ε)] (1+O(1/h)),               (6)

uniformly for n/h sufficiently small. The square root continues from Re(b_0)>0. In particular J is nonzero and

    log|J_(n,h)|=h logγ+O(n+log h+n²/h).              (7)

Differentiating hΦ_(n/h)(σ_(n/h)) with n fixed gives log G(σ_(n/h)); the stationary-point derivative cancels. The analytic amplitude changes by O(1/h+n/h²) over a shift two. Applying (6) at both parameters thus proves

    J_(n,h+2)/J_(n,h)=g0²(1+O(n/h+1/h)).             (8)

The imaginary part of g0² is −160sqrt2/729, strictly nonzero. Thus for all sufficiently small n/h, the two real linear maps Im(J) and Im(J_(h+2)) have a uniformly nonsingular 2×2 matrix in (Re J,Im J). Consequently a fixed c1>0 satisfies

    max(|Im J_(n,h)|, |Im J_(n,h+2)|)≥c1 |J_(n,h)|.  (9)

This includes a zero at either node. It does not assert either individual imaginary part is nonzero.

## 4. Same-node complete error and actual primitive lower rate

Fix κ in

    0<κ<κ0=1/log(5/γ),        γ=4sqrt3/9.             (10)

Let n run through powers of two with n≥16. Start M=floor(κ n log n/2), take m0 as in Section 1, and consider h0=2m0,h0+2. Both are eligible, h0=κ n log n+O(n), and their actual U have valuation r. For a completely rational selection, refine a certified enclosure [p−δ,p+δ] of π until max |β−p|≥4δ, then select the node s maximizing that rational distance. The process terminates by (9); ties can be broken by the smaller node. The chosen true distance is at least 3/5 of the maximum true distance, since max |β−π|≤max |β−p|+δ and the chosen |β_s−π|≥max |β−p|−δ. Thus (9) retains a fixed positive constant without requiring an exact comparison of two real distances.

The complete contour identity, including both halves, is

    T−πU=−2^(n+2)(−1)^h Im J_(n,h).

Combine (7), (9), and the Cauchy upper bound log|U|=o(n log n) from the preceding note. At the selected node,

    log|β_s−π|≥κ logγ · n log n+o(n log n).           (11)

The full exponential error (1) of the preceding note has upper leading rate −1+κ log5. Condition (10) makes that strictly smaller than κ logγ. Hence at this very same node the exponential part is negligible relative to the logarithmic part and cannot cancel it. The complete center satisfies

    |c_s−(e+π)|≥(1−o(1))|β_s−π|>0.

Using the actual final denominator (4) proves the authored primitive-form exclusion

    liminf log(q_s |c_s−(e+π)|)/(n log n)
       ≥κ[3 log2+logγ]>0.                            (12)

The positivity is exact: 2³γ=32sqrt3/9>1. Thus these specified target-preserving diagonal quartic forms grow in primitive magnitude in the entire stated κ range. Their logarithmic errors do decay, but the exact dyadic denominator cost grows faster. This improves the authored exclusion regime and exhibits a concrete arithmetic cost of suppressing both endpoint modes. It neither rules out different approximation families nor proves irrationality or rationality of e+pi.
