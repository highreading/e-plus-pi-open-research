> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Certified nonzero odd limiting boundary determinants

Date: 2026-09-13. Original bounded continuation by audit_results.
Independent review: PASS by audit_sources after an identical interval rerun; see raw_odd_limiting_certificate_independent_review.md.

The single fixed-operator certificate below proves

    0.62 < det D2_+ < 0.63,
    -1.36 < det D3_+ < -1.35,                              (1)

for the actual limiting matrices of the independently reviewed
raw_odd_boundary_operator_limit.md. Thus both limiting determinants are nonzero.
Their ratio lies in (-0.47,-0.45).

Combined with the proved operator limit and exact finite scalar identity, this establishes

    s_m -> s_infty=det D2_+/det D3_+ !=0,
    -0.47 < s_infty < -0.45.                              (2)

Consequently the absolute odd root-product limit is 3sqrt(3)/e, matching the already proved even limit. This is a theorem about the actual dual polynomial endpoint/root product. It does not establish a shrinking primitive integer form or resolve the e+pi problem.

## 1. Fixed operators and the certificate data

All spaces and matrices here are the fixed limiting objects, not new canonical degrees. On ell^2(Z), let

    J e_r=(sqrt(3)/2)(e_(r-1)+e_(r+1)),
    P_+=projection onto r>=0,
    Y=P_+ J P_+.

Use two components and set

    t(y)=(1+iy)/(1-iy),
    F(y)=exp [0 t(y); 1 0],
    E=P_+F(J)P_+,
    A0=1/2 [0 I+iY; I-iY 0],
    Q=(A0 E)^(-1),
    gamma=sqrt(3)/4,
    U=gamma e_0,
    W=iota_(-1)*F(J)P_+,
    V=[0 i;-i 0] W,
    v_r=sqrt(2/3)(i/sqrt(3))^r [1;0].

Here e_0 inserts a two-component vector at position zero. The proved bounds used by the certificate are deliberately loose:

    ||A0||<=1,  ||A0^(-1)||<=2,
    ||E||<=e<3,  ||E^(-1)||<=e/cos(1)<6,
    ||Q||<12,  ||V||<3,  ||v||=1.                        (3)

The inverse estimate only needs e<3 and cos(1)>1/2. It does not depend on the separate sharper accretivity improvement.

As in the operator-limit theorem,

    D2=I+VQU,
    D3=[D2 VQv; v*QU v*Qv].                              (4)

The fixed dimensions and cutoffs are:

    input support L=64 positions (128 scalar components);
    checked output prefix 0,...,127;
    periodic quadrature M=512;
    24 terms each for c(t) and s(t);
    outward interval precision 100 decimal digits.

The three approximate vectors are stored as exact dyadic rational coordinates in
raw_odd_limit_certificate_vectors.json. They approximate QUe_1, QUe_2, Qv. Their method of discovery is not trusted by the proof: the verifier establishes their errors from the full half-line residual alone.

The executable verifier is check_raw_odd_limit_interval_certificate.py.
Its complete interval output is raw_odd_limit_interval_certificate.json.
Use Python 3.12 explicitly. The original run used
[private local path removed];
the independent rerun used /opt/homebrew/bin/python3.12.
The script loads the local math_packages/mpmath interval implementation
(version 1.4.1). The machine's unqualified python3 may be too old for that package.

## 2. A rigorous analytic bound for all Fourier tails

Fourier transformation identifies J with multiplication by

    y(zeta)=(sqrt(3)/2)(zeta+zeta^(-1)).

Take R=4/3. On the closed annulus R^(-1)<=|zeta|<=R,

    |Im y|<=7sqrt(3)/24=:b<17/33.

Therefore 1-iy never vanishes there and

    |t(y)|<=(1+b)/(1-b)<25/8.

The two entire power series

    c(t)=sum_(j>=0)t^j/(2j)!,
    s(t)=sum_(j>=0)t^j/(2j+1)!

give F=[[c,ts],[s,c]]. Put q=9/5>sqrt(25/8). Its maximum row and column absolute sums are bounded by

    cosh(q)+q sinh(q) <= q e^q <16.

For the last strict bound, q<2 and e<11/4 suffice. Hence throughout the annulus

    ||F(y(zeta))||<16.                                    (5)

Write its Laurent coefficients as F_k. Cauchy's inequality gives

    ||F_k||<=16 R^(-|k|).                                 (6)

The symbol is unchanged by zeta->zeta^(-1), so F_(-k)=F_k exactly. The half-line matrix has block (r,s) equal to F_(r-s), and W has blocks F_(r+1).

For 0<=k<=128, the exact M-point trapezoidal coefficient differs from F_k by at most

    eta=32 R^(-(M-128))/(1-R^(-M))                        (7)

in matrix norm. This follows by summing the aliased coefficients F_(k+lM), l!=0, using (6). With M=512, eta is below 3.379 times 10^(-47).

The verifier evaluates the paired cosine trapezoidal sum with outward intervals. Each real quadrature node has |t|=1. After 24 terms the absolute tail of each c,s series is below 2/(48)!, by its decreasing factorial ratios. Each computed c,s enclosure is widened by that amount before constructing F. It then widens every Fourier coefficient by (7). Thus neither floating quadrature error nor the omitted Laurent coefficients are left implicit.

## 3. Full half-line residual bounds

Let f be one of the saved approximate vectors, supported at positions 0,...,L-1. All its coordinates are exact rationals. Interval convolution of its finite support with the certified F_k computes

    g_r=(Ef)_r,       0<=r<=128.

The verifier then evaluates (A0 g)_r for 0<=r<128. For r=0 the negative neighbor is zero, as required by the half-line boundary. It bounds the norm of this residual prefix by the sum of the absolute real and imaginary components, an upper bound for its Hilbert norm.

For the omitted tail define

    C(f)=sum_(s=0)^(L-1) R^(s-L+1)||f_s||_2.

The verifier uses the larger componentwise absolute sum for each block norm. For r>=L, (6) gives

    ||(Ef)_r||_2<=16 C(f) R^(-(r-L+1)).

Consequently

    ||(Ef)_(r>=127)||_2
       <=16 C(f)R^(-(128-L))/sqrt(1-R^(-2)).              (8)

Since A0 has bandwidth one and norm at most one,

    ||(A0 Ef)_(r>=128)||_2
       <=||(Ef)_(r>=127)||_2.

The U right-hand sides have no tail. The v right-hand side has exact tail norm 3^(-128/2).

Adding the prefix and tail bounds gives a bound epsilon for ||u-A0Ef||. Equation (3) then gives the rigorous solution error

    ||Qu-f||<=12 epsilon.                                (9)

The verifier obtains, respectively, bounds smaller than

    3.508 times 10^(-13),
    2.827 times 10^(-12),
    1.682 times 10^(-11).                                (10)

The finite approximate matrix inverse is never used as an error estimate.

## 4. Boundary testing and interval determinants

For a saved finite-support f, Wf is computed exactly within the coefficient intervals using blocks F_(s+1). Multiplication by Jb=[0 i;-i 0] gives Vf. If the solved-vector error is delta, the actual Vf is within 3delta in complex modulus, by (3). Each real and imaginary component is widened by that amount.

The lower row uses the exact geometric v. Its pairing with f is a finite sum, and the actual v*Qu differs from it by at most delta. This includes all effects of the infinite vector v through its unit norm; it does not truncate the true test vector without a bound.

The resulting component intervals are inserted into the exact 2 by 2 and 3 by 3 determinant formulas. The complete verifier finishes with PASS. Its narrower enclosures imply (1); approximately, their centers are

    det D2_+ = 0.62377837058...,
    det D3_+ = -1.35377310993...,
    s_infty = -0.46077024725....

These decimals are descriptive; the asserted bounds are the explicit rational intervals in (1)-(2).

The determinants are real. For example, the diagonal phase gauge e_r->i^r e_r makes E and A0 real matrices: F_k is real for even k and purely imaginary for odd k, and the phases cancel to real entries. In this gauge v and U are real, while the phase of W is canceled by Jb. Thus (4) is real. Alternatively, reality follows from convergence of the exact real finite determinant ratios and their real base determinants. The interval imaginary widths are also explicitly bounded in the output.

## 5. Consequences for the actual odd family

The independently passed operator-limit theorem proves D2_m->D2_+ and D3_m->D3_+. Equation (1) supplies the previously missing nonzero limits. Therefore the exact finite identity proves (2).

Since

    V_(2m+1)(1)/[t^(2m+1)]V_(2m+1)
       = B_m^odd s_m,
    B_m^odd=(4m+2)!m!(3m+2)!/((2m+1)!)^3,

Stirling's formula gives

    (|V_n(1)/[t^n]V_n|)^(1/n)/n ->3sqrt(3)/e             (11)

along odd n. The same limit along even n was already proved by the accretive Toeplitz comparison, so the absolute limit now holds along all degrees. Along sufficiently large odd degrees, V_n(1)/[t^n]V_n is negative because B_m^odd>0 and s_infty<0.

The operator-side inverse obstruction is also removed asymptotically. D2_m has a bounded inverse for all sufficiently large m, hence Woodbury and the uniform exterior bounds give ||A_m^(-1)||=O(1). For the actual high compression B_m,

    B_m^(-1)=Pi A_m^(-1)Pi
       -(Pi A_m^(-1)v)(v*A_m^(-1)Pi)/(v*A_m^(-1)v)

on v-perpendicular. Its denominator is 1/s_m and converges to a nonzero number. Hence ||B_m^(-1)||=O(1) as well.

These O(1) statements do not specify an effective first degree: the present operator-limit proof asserts convergence without a rate. All finite matrices are already known nonzero, so no finite exceptional degree has been silently discarded.

The certificate concerns one fixed limiting operator. It uses no new canonical HP degree and no degree, prime, root, or singular-value scan. The signed dual remainder and the actual endpoint gcd remain separate requirements for any e+pi conclusion.
