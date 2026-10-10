> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review of the additional growing-block structure

Reviewer: Agent 4. This completes the previously unfinished additional-recurrence audit. The completed family and arithmetic reviews are preserved.

Overall verdict: PASS WITH DOCUMENTATION REPAIR. The exact algebraic claims pass. Section 7's strict residual-content target above 1/2 must be marked rejected rather than retained as a live objective. This review supplies that correction without editing the source.

Separate verdicts:

- Differential, Taylor, and derivative recurrences: PASS.
- All-size integer unitriangular column transformation: PASS.
- Maximal-minor ideal preservation and factorial-content accounting: PASS.
- Four-group Vandermonde expansion, signs, and missing-power factors: PASS.
- Required transformation of appended endpoint rows: PASS.
- Integral normalized state recurrence: PASS in its stated k>=2 domain.
- Integrality of the specifically cleared endpoint pair and exact gcd-scale correspondence: PASS.
- New content-growth estimate or growing-degree nonvanishing: NOT ESTABLISHED.

The independent checker completed with exit code 0 and sandboxed=true. Its 83 checks passed, including 24 abstract alternant checks and six complete four-group expansion controls. The unrestricted statements below rest on proofs, with these exact computations as supporting evidence.

## 1. Definitions and factorial accounting

Let 1<=b<=n, m=b-1, and

    R_lj=E_(n+l,l+j-1), 1<=l<=m, 0<=j<=m+1,
    Pcal_k(x)=x^k H_k(x),
    E_(k,r)=Pcal_k^(r)(1),
    theta_(k,r)=E_(k,r)/r!.

The previously reviewed integrality H_k in Z[x] implies theta_(k,r) is integral: it is the coefficient of y^r in Pcal_k(1+y). Set theta to zero outside 0<=r<=2k.

With A_b=product_(a=0)^(m-1) a! and

    Z_lj=binom(l+j-1,j) theta_(n+l,l+j-1),

one has R_lj=(l-1)!j! Z_lj. Extracting the row and retained-column factorials therefore gives, for omitted columns i<j,

    det R_(omit i,j)/A_b^2
      = m!(m+1)!/(i!j!) det Z_(omit i,j).

The multiplier is integral because i<=m and j<=m+1. This proves the identity for every minor, including zero minors. At b=1 the sole empty minor and the multiplier are both 1.

On full row rank, Gamma is the positive gcd of all maximal minors of R and equals Crows*mu in the completed arithmetic review. Consequently A_b^2 divides Gamma. Write gamma_min=Gamma/A_b^2; this is the source's residual-minor gamma, not the older cleared-endpoint gcd. Row divisors already belong to Gamma and cannot be multiplied into it again without a separate sequential divisibility argument.

## 2. Differential and Taylor recurrences

Coefficient extraction from the defining polynomial gives

    H'_(k+1)=(k+1)(H_k-H'_k+H''_k/2),
    H_(k+1)=x H''_k/2+(k+1-x)(H'_k-H_k).

For the second identity, differentiate exp(xz)(1-z+z^2/2)^(k+1) in z and compare its coefficient of z^k. Thus the recurrence concerns the actual H sequence.

Substitute H_k=x^(-k)Pcal_k and multiply the second identity by 2x^(k+1). Collection of derivatives gives exactly

    2Pcal_(k+1)
      =x^2 Pcal''_k+2x(1-x)Pcal'_k
       +(2x^2-2x-k(k+1))Pcal_k.

This derivation is initially valid away from x=0. Both sides are polynomials, so the resulting identity holds everywhere.

At x=1+y, the three coefficient polynomials on the right are

    1+2y+y^2,
    -2y-2y^2,
    2y+2y^2-k(k+1).

Extracting y^r and dividing by 2 gives

    theta_(k+1,r)
      =binom(r+2,2)theta_(k,r+2)
       +r(r+1)theta_(k,r+1)
       +[r(r-3)-k(k+1)]theta_(k,r)/2
       -(r-2)theta_(k,r-1)+theta_(k,r-2).

Every coefficient is integral. In particular the middle coefficient equals

    binom(r,2)-r-binom(k+1,2).

The initial data are theta_(0,0)=1, with all other entries zero. The zero-extension convention handles r=0 and r=1 and all degrees beyond the support. No local division or prime hypothesis occurs.

## 3. Third-order equation and derivative-column recurrence

Differentiate the second H identity and subtract the first to obtain

    xH'''_k+(k+2-2x)H''_k+2(x-1)H'_k-2kH_k=0.

After substituting x^(-k)Pcal_k and multiplying by x^(k+1), this becomes

    x^2 Pcal'''_k+[(2-2k)x-2x^2]Pcal''_k
      +[k(k-1)+(4k-2)x+2x^2]Pcal'_k
      -(2k^2+4kx)Pcal_k=0.

General Leibniz differentiation r times at x=1 yields coefficients

    1,
    -2(k-r),
    (k-r)(k-r+3),
    -2(k-r)(k-r+2),
    -2r(2k-r+1)

on E_(k,r+3), E_(k,r+2), E_(k,r+1), E_(k,r), and E_(k,r-1), respectively. Solving for the highest derivative proves equation (5) with precisely the source's signs. At r=0 the last coefficient is zero; no negative-order derivative is required.

Set k=n+l and r=l+j. The highest derivative corresponds to column j+4. Moreover

    k-r=n-j,
    (l+j)(2n+l-j+1)=l(l+2n+1)+j(2n+1-j).

Writing lambda_l=l(l+2n+1) and Lambda_spec=diag(lambda_l), the recurrence is therefore

    R_(j+4)=2(n-j)R_(j+3)
      -(n-j)(n-j+3)R_(j+2)
      +2(n-j)(n-j+2)R_(j+1)
      +[2Lambda_spec+2j(2n+1-j)I]R_j.

It holds for all retained columns and their natural derivative extension. Lambda_spec is a spectral diagonal matrix; it is unrelated to the scalar endpoint clearer used below.

## 4. All-size integral column transformation and ideals

Put W_(4q+s)=(2Lambda_spec)^q R_s, 0<=s<4, using only starting columns needed by the actual block.

Inductively assume R_j=W_j plus a Z[n]-linear combination of W_i with i<j. Multiplication by 2Lambda_spec sends every W_i to W_(i+4). Hence the term 2Lambda_spec R_j has leading term W_(j+4), with all its other indices below j+4. Every other term of the recurrence involves columns with indices at most j+3. The coefficient of W_(j+4) is exactly 1.

Thus for every finite number of retained columns

    R=W T,

where T is upper unitriangular over Z[n]. This is an existence statement obtained by the recurrence even if the evaluated W columns are dependent. No independence assumption is needed. The strictly upper triangular part is nilpotent, so its finite geometric-series inverse proves T^(-1) also lies over Z[n]. In particular det T=1.

Cauchy–Binet expresses every maximal minor of R as a Z[n]-linear combination of those of W. Applying it to W=R T^(-1) gives the reverse containment. After specializing the integer n, their maximal-minor ideals over Z are equal. This includes deficient-rank cases, where both ideals are zero.

All maximal minors of W are therefore divisible by A_b^2. Divide the Cauchy–Binet identities in both directions by this common integer divisor to obtain equality of the residual ideals. This does not require, and does not assert, that the corresponding individual minors are equal. Nor does it assert that T remains integral or unimodular after separately dividing column j by j!.

For endpoint rows v,w, right multiplication of the entire square augmented matrix by T^(-1) gives the precise identity

    det[R;v;w]=det[W;v T^(-1);w T^(-1)].

Using W while leaving the appended rows unchanged is generally incorrect. An independent arbitrary-matrix control in the checker gives an error polynomial 2n(n+2) when those rows are left unchanged, while the correctly transformed determinants agree identically. This is an abstract linear-algebra control, not an HP degree evaluation.

The source explicitly states the appended-row requirement. Its endpoint gcd calculation in Section 6 uses the original convention and does not silently substitute untransformed endpoint rows into W determinants.

## 5. Four-group expansion and permutation signs

For retained columns J, let N_s count available columns congruent to s modulo four, and let A_s be the omitted exponents in that group. Write t_s=|A_s| and d_s=N_s-t_s. Exactly two columns are omitted, so sum t_s=2 and sum d_s=m.

First factor 2^floor(j/4) from retained column j, giving the common factor 2^Q_J. Permute the retained columns into groups s=0,1,2,3, retaining increasing exponents within each group. Let epsilon_col be the sign of that permutation relative to the original retained-column order.

Expand the grouped determinant over ordered row partitions I_0,...,I_3 with |I_s|=d_s, each subset written increasingly. Let epsilon_row be the sign of their concatenation relative to the natural row order. The Laplace expansion contributes epsilon_row times the product of the four group determinants. Since the inverse column permutation has the same sign, the sign in the original determinant is exactly

    epsilon(I,J)=epsilon_col*epsilon_row.

In group s, factor R_(l,s) from the corresponding row l. The remaining determinant is the alternant with rows lambda_l and retained powers. Its ordinary Vandermonde is

    Delta(I)=product_(u<v in I)(lambda_v-lambda_u)
            =product_(u<v in I)(v-u)(2n+1+u+v).

This verifies the node factor and its orientation.

For d nodes z_1,...,z_d, use e_0=1 and e_a=0 outside 0<=a<=d. The required alternant factors are:

- No missing powers from 0,...,d-1: 1.
- One missing power a from 0,...,d: e_(d-a).
- Two missing powers a<c from 0,...,d+1:

      e_(d-a)e_(d+1-c)-e_(d-a+1)e_(d-c).

Here is an all-size sign verification. Let P(z)=product_i(z-z_i) and p_j=[z^j]P, with zero coefficients outside its degree range. For one missing power, the kernel coefficient vector of the full evaluation matrix is (p_j), giving

    det V_(omit a)=(-1)^(d-a) Delta p_a=Delta e_(d-a).

For two missing powers, the coefficient vectors of P and zP form the kernel matrix with row j equal to (p_j,p_(j-1)). The complementary-minor relation, normalized using omitted columns d,d+1, is

    det V_(omit a,c)
      =(-1)^(a+c+1) Delta (p_a p_(c-1)-p_(a-1)p_c).

The normalizing kernel minor at d,d+1 is 1, and the corresponding evaluation minor is the ordinary Vandermonde. Substituting p_j=(-1)^(d-j)e_(d-j) cancels the sign (-1)^(a+c+1) and yields exactly the displayed difference of two products.

This proof may first be made over the field of rational functions in distinct nodes, where the evaluation rank is d. Both resulting sides are polynomials, so the identities hold for all node specializations, including coincident nodes. For d=0 the empty determinant is 1; the possible hole sets are empty, {0}, or {0,1}, and the same correction factors equal 1.

Combining these facts proves the source's formula

    det W_J=2^Q_J sum_(I_0,...,I_3) epsilon(I,J)
      product_s [(product_(l in I_s)R_(l,s)) Delta(I_s) Phi_s(I_s)]

for every maximal minor. If a starting-column group is absent, its empty contribution is 1 and no nonexistent starting column is evaluated.

The independent checks include 24 symbolic alternant identities and six complete expansions of one prescribed arbitrary seven-row matrix. The controls include two holes in one group, holes in different groups, an empty group, and both permutation signs. They use neither actual H values nor a specialized HP index.

Divisibility by A_b^2 is proved for the whole minor. It is not proved for individual partition summands. Vandermonde factors from different summands cannot be multiplied to infer a common divisor, and powers of two or node differences may overlap previously extracted content. No new content-growth rate follows from this expansion.

## 6. Integral three-coordinate state

For k>=2, define h_k=H_k(1), u_k=H'_k(1)/k, and v_k=H''_k(1)/(k(k-1)). These are normalized derivatives, distinct from the raw derivative symbols used in earlier notes.

For 0<=d<=k, coefficients of H_k^(d)/(k)_d are (k-d)_s a_s(k), in their valid range. The consecutive-even-factor argument from the completed arithmetic review proves their integrality. In particular u_k,v_k are integers.

Substituting the raw derivatives k u_k and k(k-1)v_k into the accepted raw transition gives

    T_k=[-k, k^2, k(k-1)/2;
          1, -k, k(k-1)/2;
          1, 1, 1-k(k+1)/2].

All entries are integral. Adding k times row two to row one makes its first two entries zero and its third entry k(k-1)(k+1)/2. The remaining two-by-two determinant is k+1. Therefore

    det T_k=k(k-1)(k+1)^2/2.

The domain k>=2 avoids the undefined normalization of v_1. This determinant is not a common divisor of the output state or of high-block minors. No small-prime transfer theorem is inferred from it.

## 7. Integral endpoint pair and exact reconciliation of gcds

Retain the previously reviewed monic cofactor normalization. Define

    F=(2n+1)!,
    f=2^n/(n!)^2,
    rho_plus=product_(l=1)^(b-1)(2n+2l)!,
    M=2^(2n+3)F^2 rho_plus,
    Gamma=Crows*mu.

On Y!=0, Gamma and the three-contraction content d are positive. The starred contractions are integers, and

    Dstar=(n+1)P_(n+1)cstar-2P_n sigmastar,
    Nstar=Qstar+2fVstar
      =2(w_P+T_P)sigmastar
       -(n+1)(w_U+T_U)cstar-2f kappastar.

The source calls Nstar U*. This review uses Nstar to match the earlier gcd comparison. It retains both second-kind values and both complete partial-exponential contractions.

Set

    N0=fF^2 Nstar,
    Z0=fF^2 Dstar.

Integrality must be established before assigning their integer gcd. Put

    beta=fF=2^n(2n+1)binom(2n,n),
    alpha=fF^2/[2^n(n+1)!]
          =binom(2n+1,n)^2(n+1)!.

Both are integers. The known denominators imply

    Wp=2^n(n+1)! w_P and Wu=2^n(n+1)! w_U are integers,
    TPint=F T_P and TUint=F T_U are integers.

Consequently the full first coordinate is exactly

    N0=2(alpha Wp+beta TPint)sigmastar
       -(n+1)(alpha Wu+beta TUint)cstar
       -2beta^2 kappastar.

This is an integer term by term. Also Z0=beta F Dstar is integral. This proof uses the complete numerator rather than only one factorial component.

The original endpoints have scale

    (X,Y)=(-1)^n Gamma d f/[rho_plus 2^(2n+3)] (Nstar,Dstar).

Therefore

    (MX,MY)=(-1)^n Gamma d (N0,Z0),
    g=Gamma*d*g0,
    g0=gcd(|N0|,|Z0|).

Now distinguish the old scalar endpoint clearer from Lambda_spec:

    Lambda_clear=2^(n+1)(n+2)!F(n!)^2,
    gamma_end=gcd(|Lambda_clear Nstar|,|Lambda_clear Dstar|).

The ratio of the two pair clearers is

    a_n=fF^2/Lambda_clear
       =F/[2(n+2)!(n!)^4].

This is a positive rational number, not generally an integer. Nevertheless the two pairs are integral and proportional. Divide the old pair by gamma_end to obtain a primitive integer pair (u,v). The new pair is a_n gamma_end(u,v). A Bezout combination of u,v is 1, so integrality of both new coordinates implies a_n gamma_end is an integer. Their gcd is then exactly that integer. Thus

    g0=F*gamma_end/[2(n+2)!(n!)^4],
    g=Gamma*d*F*gamma_end/[2(n+2)!(n!)^4].

This is precisely the rational-scale identity accepted in GROWING_ARITHMETIC_CONTENT_REVIEW.md. The denominator is retained; the new formula is not merely an agreement of leading logarithmic rates.

The source's residual-minor gamma is gamma_min=Gamma/A_b^2, so

    g/A_b^2=gamma_min*d*g0.

Neither gamma_min nor Gamma is the old gamma_end. All three meanings have been kept separate here.

Finally

    q=|Z0|/g0=Lambda_clear|Dstar|/gamma_end

is the same actual reduced denominator. If Nstar=0 while Y!=0, then g0=|Z0| and q=1; the scale argument remains valid.

## 8. Domain qualifications and rejected target

At b=1, m=0, the unique empty maximal minor is 1, Gamma=A_1=Crows=mu=rho_plus=1, and the column transformation on the available starting columns is the identity. The four-group formula has one empty row partition and evaluates to 1. The endpoint formulas still require Y!=0 and d>0.

If the high block has deficient rank, R and W have zero maximal-minor ideals. The chosen augmented cofactor representative vanishes. This does not exclude other solutions of the underlying underdetermined system. No positive Gamma or residual gcd should be defined by division through zero content. Full high-row rank alone does not prove nonzero endpoint. Endpoint nonvanishing and full evaluated-remainder nonvanishing remain separate questions.

Section 7 of the source retains the former strict residual target above 1/2. That target has already been rejected in the current research record and is not endorsed by this review. Its presentation requires the documentation repair stated in the verdict. The exact recurrences, ideal equalities, and gcd formulas remain useful independently of that rejected target.

No growing-degree nonvanishing, new positive quadratic-logarithmic divisor rate, replacement shrinking criterion, or assertion about rationality of e+pi follows here.

## 9. Inspected code, real execution, and artifacts

The exact assigned inputs were inspected:

- work/session_20261001_astra/agent1/ADDITIONAL_GROWING_CONTENT.md
- work/session_20261001_astra/agent1/check_additional_growing_content.py
- work/session_20261001_astra/agent1/additional_growing_content_certificate.json

The author program records twelve symbolic checks. Its Taylor test compares two displayed expressions, and its abstract column test covers twelve columns; these do not replace the all-size proofs. The author program does not itself compute the four-group expansion. It was not executed or modified during this independent audit.

The separately saved and inspected check_additional_growing_independent.py derives the Taylor coefficients from the translated differential operator and the derivative recurrence from general Leibniz differentiation. It verifies twelve free columns using spectral_a=2lambda, an integral inverse, both Cauchy–Binet directions on an arbitrary matrix, the required endpoint-row transformation, missing-power alternants, complete grouped expansions, and termwise endpoint clearing.

Its actual application execution returned exit code 0 in 1.16 seconds with sandboxed=true and status PASS_INDEPENDENT_STRUCTURAL_CHECKS. All 83 recorded checks passed. The output reports:

- Twelve abstract free columns.
- Twenty-four abstract alternant checks.
- Six complete four-group expansion controls.
- Appended-row transformation and exact integer-pair scale verified.
- Protected inputs and completed review artifacts unchanged during execution.
- No actual HP indices evaluated and no primes scanned.

Independent evidence under work/session_20261001_astra/agent4/:

- check_additional_growing_independent.py
- additional_growing_independent_checks.json
- additional_growing_independent_stdout.txt
- ADDITIONAL_GROWING_REVIEW.md

The certificate stores the transformation and its inverse, exact expansion controls, clearer correspondence, and hashes of protected inputs and prior artifacts. The stdout file records the real execution summary. These finite computations are supporting evidence for the paper proofs and are not a degree or prime scan.

Only Agent 4 artifacts were written. Reviewed sources and the completed family and arithmetic reviews were preserved. No networking, installations, external paths, or security changes were used.
