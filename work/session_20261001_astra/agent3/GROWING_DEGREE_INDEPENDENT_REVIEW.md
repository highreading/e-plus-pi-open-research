> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the growing-degree construction

Reviewer: Agent 3. Scope: Agent 2's PROOF_DRAFT.md, REPORT.md, check_growing_regime.py, and growing_regime_certificates.json under work/session_20261001_astra/agent2/.

Overall verdict: PASS for the actual growing-degree identities, uniform absolute bounds, finite certificates, and conditional criterion, WITH AN EXPLICIT DOMAIN CORRECTION to the general determinant lemma. The phrase “for every positive integer d” is not justified by the original definition of the factorial functionals. This correction does not affect either intended application. No growing-degree nonvanishing theorem, favorable primitive-form rate, or exclusion follows from the upper bounds.

The completed b=1 prime search was not reopened. Agent 2's checker was inspected but not executed. A separate independent checker was executed successfully on exactly the existing n=4,6,8,10 certificates. Agent 2's four input files had identical hashes before and after that run. All independent outputs are in Agent 3's directory.

## 1. Separate verdicts

| Component | Verdict | Qualification |
|---|---|---|
| Exact growing-b reduction and complete-tail identities | PASS | Valid for 1<=b<=n; no rank or nonvanishing assumption is hidden in the identities. |
| Contour identities and uniform absolute bounds | PASS in the actual applications; general statement requires repair | Correct powers, signs, dimension factors, and Gamma quotient. Specify the factorial-index domain or explicitly extend the functionals. |
| Existing finite evidence | INDEPENDENT EXACT PASS | Exactly n=4,6,8,10; no additional degree samples and no asymptotic inference. |
| Conditional primitive-form criterion | PASS as a sufficient criterion | Its determinant lower-bound, actual-denominator, and remainder-nonvanishing hypotheses remain unproved. |

## 2. Required correction: factorial domain

The original definition is ell_j(t^k)=1/(n+k+1-j)! for 0<=j<=b, with k>=0 and b<=n. Its minimum factorial argument is n+1-b>=1.

A d-column difference determinant uses D_j=ell_(j+1)-ell_j for j=0,...,d-1, hence requires ell_0 through ell_d. A d-column ordinary determinant uses ell_0 through ell_(d-1). Consequently, under the literal original definition, the difference determinant is defined only for d<=b, and the ordinary determinant only for d<=b+1.

The actual endpoint determinants have d=b and largest functional index b. The companion determinant T has d=b+1 but uses ordinary ell_j, again with largest index b. Thus both applications are fully within the original positive-factorial domain, including b=n. In the assigned regime b=floor(n/2), there is additional margin.

Recommended minimal repair: replace “for every positive integer d” by “for 1<=d<=b for the difference determinant, and 1<=d<=b+1 for the ordinary determinant, with the original functionals.” All displayed bounds then hold unchanged.

A broader positive-factorial version is also valid after explicitly defining ell_j for 0<=j<=n: difference determinants allow d<=n, ordinary determinants allow d<=n+1. If zero factorial arguments are permitted and ell_(n+1) is explicitly defined, these limits become d<=n+1 and d<=n+2 respectively.

Alternatively, the all-positive-d statement can be retained by making a genuinely new definition:

    ell_j(P) = sum_(k>=0) [t^k]P / Gamma(n+k+2-j), for all integers j>=0,

where reciprocal Gamma is its entire continuation and is zero at nonpositive integer arguments. Equivalently, 1/m! is declared zero for negative integer m. For example, ell_(n+2)(1)=0 in this extension, whereas the original formula would require the undefined factorial (-1)!. The contour integral produces precisely this extended functional: a negative required Taylor index of exp(z) contributes zero.

The extension preserves the contour proof and bound for every finite d, but it must be stated explicitly; it is not an implicit property of the original factorial definition. Agent 2's source files have not been changed. This review records the correction rather than silently interpreting the theorem as already repaired.

## 3. Exact system and entire tails

For caps (n,b,n), the original high Taylor equations correspond to moment tests t^q for q=0,...,n+b-1. The first n+1 tests determine C* uniquely through the nonzero bilinear norms h_k. The remaining b-1 tests are exactly ell_B(p_(n+l))=0, l=1,...,b-1. Endpoint matching supplies the row e+v. Taylor truncation determines A uniquely. This proves equivalence to the b-by-(b+1) reduced matrix without a normality assumption.

The logarithmic tail after degree n is L(C*/(1-t)). On the integration segment, |t|<=1/sqrt(2)<1, so its geometric series converges absolutely. Substituting the finite kernel projection gives -ell_B(H). The exponential tail is ell_B(1/(1-t)); its factorial series converges absolutely. Hence R(1)=ell_B(W) is an equality of the full evaluated tails. It does not replace either tail by its first term.

With the cofactor orientation B dot x=det[M;x], multilinearity gives

    Y=det[U;e+v;e]=-det[U;e;v]=-D_V,
    R(1)=det[U;e;w]+det[U;v;w]=D_W+T.

The identities remain true for a vanishing cofactor vector. D_V!=0 implies rank M=b and Y!=0. Rank b alone does not imply Y!=0. Neither assertion establishes R(1)!=0.

Replacing columns by the original adjacent differences, while retaining the first column, has determinant one. In D_V and D_W, the e row becomes (1,0,...,0). That row occupies position b, so expansion gives the explicit common sign (-1)^(b+1). The remaining b-by-b rows are the high polynomials followed by V or W. The independent checker verified this sign at all four frozen indices.

## 4. Contour powers, determinant orientation, and full companion

For a permitted functional index, the coefficient of z^-1 in

    exp(z) z^(j-n-2) P(1/z)

requires the exponential-series index n+k+1-j for a monomial t^k. This verifies the power j-n-2 and the factorial argument exactly. For R beyond the reciprocal analytic radius, the Taylor series of P(1/z) converges absolutely on the contour. No asymptotic interchange is required.

The difference functional contributes (z-1)z^j against the common weight exp(z)z^(-n-2) dz/(2*pi*i). The integration identity uses det[P_i(1/z_k)] and det[z_k^j] with increasing j. The latter determinant is Delta(z)=product_(k<l)(z_l-z_k), without an extra sign. Expansion and permutation of variables give the factor 1/d!.

For the ordinary ell determinant, only the factors z_k-1 are omitted. Its dimension is b+1 for T, and its rows are the b-1 high polynomials, V, and W. Thus the bound includes the full companion determinant.

Under z=R exp(i theta), |dz|=R dtheta. The common factor z^(-n-2) therefore contributes R^(-n-1) per variable. Combining exp(R cos theta), |z-1|<=R+1, and the reference-polynomial bound gives exactly the stated E_n(R). The ordinary version removes precisely R+1 per row, not an additional power of R.

For completeness, Delta(1/z)=(-1)^S Delta(z)/product_k z_k^(d-1), where S=d(d-1)/2. This sign is immaterial in the absolute estimate but must not be interpreted as positivity of the contour integrand. The modulus product is exactly the squared unit-circle Vandermonde used in the draft.

## 5. Divided differences and dimension factors

Write P_i=U0 G_i. Factoring U0(1/z_k) from the determinant's columns is exact. Newton divided-difference column elimination gives

    det[G_i(t_k)] = Delta(t) det[G_i[t_1,...,t_(j+1)]].

For nodes |t_k|=1/R<rho, Cauchy's divided-difference formula on |zeta|=rho bounds its order-j entry by

    M_i rho/(rho-1/R)^(j+1).

After extracting M_i from row i and the displayed column factors, every remaining entry has modulus at most one. Hadamard gives d^(d/2). Summing j+1 from 1 through d gives d+S, so

    C_G=d^(d/2) (product_i M_i) rho^d/(rho-1/R)^(d+S)

is correct. Zero row bounds are handled separately as zero rows; coincident nodes follow by continuity. No separation assumption on the nodes is needed.

For theta in [-pi,pi]^d,

    |exp(i theta_l)-exp(i theta_k)| <= |theta_l-theta_k|,
    (theta_l-theta_k)^2 <= 2 sum_j theta_j^2.

Multiplying the S inequalities gives the stated (2||theta||^2)^S majorant. Also cos theta<=1-2theta^2/pi^2. With a=2R/pi^2, enlarging the domain to all real d-space therefore produces

    (2pi)^(-d) integral exp(-a||theta||^2)(2||theta||^2)^S dtheta.

The sphere area is 2*pi^(d/2)/Gamma(d/2), and the radial integral is

    integral_0^infinity exp(-a r^2) r^(2S+d-1) dr
      = Gamma(S+d/2)/(2 a^(S+d/2)).

Their product is exactly

    J_d(R)=2^S a^(-S-d/2) pi^(d/2)
           Gamma(S+d/2)/((2pi)^d Gamma(d/2)).

There is no missing factor two or factorial. The separate 1/d! comes from the determinant integration identity. Thus the displayed bound C_G E_n(R)^d J_d(R)/d! passes after the domain repair.

The visible factor R^(-S) is not a net decay theorem. Gamma(S+d/2), d^(d/2), the disk-gap factor, the products M_i, and all other factors remain dimension dependent. For d=b, S=n^2/8+O(n); for d=b+1, S=b(b+1)/2=n^2/8+O(n). No fixed-size constant may absorb these terms.

Repeated monomial shifts vanish in a multilinear expansion because they give equal rows. Distinct shifts have total at least S. This is a cancellation identity, not a guarantee that the first potentially surviving term is nonzero or dominates uniformly as b grows.

## 6. Reference polynomial, ratios, and analytic factors

The roots of p_(n+1) are (1+i u_k)/2 with real |u_k|<1. Their moduli are at least 1/2, giving reciprocal modulus at most 2 and

    |U0(1/z)| <= |U0(0)|(1+2/R)^(n+1).

For the disk |t|<=rho=1/20, begin with p_1/p_0=t-1/2. If a ratio has real part at most -9/20, it is nonzero and its reciprocal has negative real part. The recurrence with positive beta_k therefore preserves the half-plane. Inductively all ratios are analytic on a neighborhood of the closed disk and have modulus at least 9/20. Since p_0=1,

    |p_(n+1)(t)| >= (9/20)^(n+1).

This lower bound concerns the reference polynomial on a small disk; it is not a determinant lower bound.

The adjacent upper bound is also correct:

    |p_(k+1)/p_k| <= 11/20 + (1/12)/(9/20)
                     =397/540 <3/4, k>=1.

The initial ratio is at most 11/20. Multiplying the appropriate l-1 ratios gives |p_(n+l)/p_(n+1)|<=(3/4)^(l-1), including the empty product for l=1.

Division by the nonvanishing U0 makes all polynomial quotients analytic on the disk. The coefficient majorant for P/U0 and the stated bound for W/U0 follow directly from the lower bound for U0 and |1/(1-t)|<=1/(1-rho). W is analytic there because H is a polynomial and its only displayed pole is at t=1. Thus the required analytic G_i exist, with explicit bounds rather than fixed-b limiting assumptions.

The H coefficients are finite, explicitly defined real quantities, not asserted rational numbers. One can also write H=pi V-Q with a rational polynomial Q, as independently checked in the certificates. This makes clear how rigorous coefficient enclosures could be obtained when numerically evaluating the bound. The displayed coefficient majorants are valid symbolic inequalities without treating numerical estimates of H as exact.

## 7. Independent finite evidence

The inspected author checker writes its output into Agent 2's directory, so it was not rerun. Instead, check_growing_degree_independent.py constructs the monic polynomials from the explicit ordinary Legendre binomial formula, integrates monomials directly, obtains F coefficients from (z^2-2z+2)F'=4, and checks the original Taylor matrix separately from the reduced matrix.

The independent execution completed with exit code zero. It verified every Taylor coefficient through the required vanishing order, direct bilinear orthogonality, the projection, cofactor scaling, endpoint matching, column-difference signs, both complete-tail rational companions, primitive polynomial content, and the separate endpoint gcd.

| n | b | Original matrix rank | Reduced rank | q digits | Endpoint gcd | floor(log10 L) |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 2 | 7 | 2 | 10 | 3 | 5 |
| 6 | 3 | 10 | 3 | 23 | 20 | 17 |
| 8 | 4 | 13 | 4 | 43 | 140 | 35 |
| 10 | 5 | 16 | 5 | 68 | 28224 | 58 |

All four forms are strictly positive. The author's exact intervals were reproduced from 220-term Machin arctangent bounds and the exponential sum through 300. Independent refinement to 230 arctangent terms and exponential terms through 320 gave intervals contained in the stored intervals, still strictly positive. The reported decimals agree within relative 10^-32 with these rigorous enclosures. Decimal values remain summaries, not the source of nonvanishing.

The exact decomposition used in the independent check is

    H=pi V-Q,
    w=e*erow-pi*v+arow,
    arow_j=-sum_(k=0)^(n-j)1/k!+ell_j(Q).

If A0=det[U;erow;arow] and A1=det[U;v;arow], then D_W=A0+pi*Y, T=A1+e*Y, and A0+A1=X in cofactor normalization. This checks both companion signs and shows explicitly why the certificates concern entire tails.

These are four exact finite results only. They establish no eventual rank, sign, lower bound, or obstruction for b=floor(n/2).

## 8. Conditional primitive-form criterion

For Y!=0, reducing X/Y to p/q with q>0 gives exactly

    L=p+q(e+pi)=q R(1)/Y,
    |L|=q |D_W+T|/|D_V|.

Clearing all coefficients and removing their common content does not remove the need for the final endpoint gcd. The draft's definition of q includes that gcd correctly and is invariant under common scaling of the triple.

Let B_W and B_T denote the corrected-domain contour bounds. On an unbounded index set, the three conditions

    D_V!=0,
    D_W+T!=0,
    q(B_W+B_T)/|D_V| ->0

are sufficient for nonzero shrinking primitive integer forms. The exponential inequality with exp(-eta n) is a stronger sufficient condition. The triangle inequality proves the asserted upper bound, but supplies no nonvanishing. Nonzero shrinking integer forms would imply irrationality of e+pi: for a rational value with denominator v, every nonzero such form has modulus at least 1/v.

No result audited here proves these hypotheses on an unbounded index set. In particular, upper bounds on D_V cannot supply its required lower bound, and the extra factorial row in T cannot be declared negligible relative to D_V without such control. The fixed-b error limit cannot be substituted with b=floor(n/2). The draft and report correctly retain these limitations.

## 9. Deliverables and preservation

Independent files under work/session_20261001_astra/agent3/:

- GROWING_DEGREE_INDEPENDENT_REVIEW.md — this review and explicit correction.
- check_growing_degree_independent.py — independent exact checker, restricted to the four existing degrees.
- growing_degree_independent_certificate.json — successful results, exact endpoint data, interval enclosures, and source/checker hashes.

The checker was executed successfully once; no additional degree samples were introduced. Agent 2's proof, report, checker, and certificate were preserved. Their before/after hashes agree and are recorded in the independent certificate. No networking, installations, external paths, historical-link restoration, or prime-search extension was performed.
