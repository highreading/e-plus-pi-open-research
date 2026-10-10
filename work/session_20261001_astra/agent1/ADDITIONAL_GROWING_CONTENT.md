> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Additional structure of the actual growing high block

Status: proved algebraic reductions with successful symbolic supporting checks; independent review pending. No additional divisor with a positive n^2 log n rate is established here. The deliverable is an exact integral recurrence and a structured formula for every residual maximal minor. The completed growing arithmetic reduction, normalized seeds, and correction are preserved.

The main-agent GROWING_FACTORIAL_CONTENT_DRAFT.md and GROWING_CONTENT_CRITERION_DRAFT.md were read. Their combined sufficient analytic criterion remains under separate review. This note does not duplicate or certify that review.

## 1. Count the factorial content once

Let 1<=b<=n, m=b-1, and

    R_lj=E_(n+l,l+j-1), 1<=l<=m, 0<=j<=m+1,
    E_(k,r)=(d/dx)^r[x^k H_k(x)] at x=1,
    A_b=product_(a=0)^(m-1) a!.

Empty products and empty determinants equal one. Write Gamma for the positive gcd of all maximal minors when R has full row rank. In the completed arithmetic reduction,

    Gamma=Crows*mu.

This is an equality: dividing each row by its exact content divides every maximal minor by their product Crows, and mu is the content of the resulting minors. It already includes every factorial divisor of those minors.

Since H_k is an integer polynomial, r! divides E_(k,r). Define

    theta_(k,r)=E_(k,r)/r! = [y^r](1+y)^k H_k(1+y),
    Z_lj=binom(l+j-1,j) theta_(n+l,l+j-1).

Then Z is integral and

    R_lj=(l-1)! j! Z_lj.

If columns i<j are deleted, the remaining m-column minor satisfies the exact identity

    det R_(omit i,j) / A_b^2
      = [m!(m+1)!/(i!j!)] det Z_(omit i,j).                 (1)

The bracketed weight is an integer: i<=m and j<=m+1. Thus A_b^2 divides every maximal minor, including zero minors. On full row rank, put

    gamma=Gamma/A_b^2.

Equation (1) describes the residual coordinates with explicit integer weights; it does not introduce another factor to multiply into Gamma. In particular A_b^2*Crows*mu would double-count A_b^2.

The earlier divisors n+l for rows l>=2 also belong to Gamma. Combining independently established divisors without an exact sequential normalization justifies their least common multiple, not their product. Their total logarithmic weight is only O(n log n) when b=floor(n/2).

## 2. An integral recurrence after derivative factorials are removed

Set Pcal_k(x)=x^k H_k(x). This notation is separate from the Legendre endpoint P_k used later. Coefficient extraction from

    H_k(x)=k![z^k] exp(xz)(1-z+z^2/2)^k

gives

    H'_(k+1)=(k+1)(H_k-H'_k+H''_k/2),
    H_(k+1)=x H''_k/2+(k+1-x)(H'_k-H_k).

For the second identity, apply [z^k] to the derivative in z of exp(xz)(1-z+z^2/2)^(k+1). These identities therefore concern the actual polynomials, not a freely chosen solution of a recurrence.

Substituting H_k=x^(-k)Pcal_k yields

    2Pcal_(k+1)
      =x^2 Pcal''_k+2x(1-x)Pcal'_k
        +(2x^2-2x-k(k+1))Pcal_k.                           (2)

Expanding at x=1 gives the integral recurrence

    theta_(k+1,r)
      =binom(r+2,2) theta_(k,r+2)
       +r(r+1) theta_(k,r+1)
       +[r(r-3)-k(k+1)]/2 * theta_(k,r)
       -(r-2) theta_(k,r-1)+theta_(k,r-2).                (3)

Here r>=0, theta_(k,r)=0 outside 0<=r<=2k, and theta_(0,0)=1. Every coefficient in (3) is an integer: r(r-3) and k(k+1) are even. This is an all-size recurrence for the factorial-normalized entries in (1), with no local division and no prime restriction.

Thus the residual problem can already be computed from an integral coefficient recurrence, instead of repeatedly differentiating large polynomials and removing factorials afterward. This alone does not supply a positive lower rate for gamma.

## 3. Four starting columns generate the entire actual block

Differentiating the second H identity and subtracting the first gives

    x H'''_k+(k+2-2x)H''_k+2(x-1)H'_k-2kH_k=0.

Its Pcal version is

    x^2 Pcal'''_k+[(2-2k)x-2x^2]Pcal''_k
      +[k(k-1)+(4k-2)x+2x^2]Pcal'_k
      -(2k^2+4kx)Pcal_k=0.                                (4)

Differentiate (4) r times and evaluate at one. Leibniz's rule gives

    E_(k,r+3)
      =2(k-r)E_(k,r+2)
       -(k-r)(k-r+3)E_(k,r+1)
       +2(k-r)(k-r+2)E_(k,r)
       +2r(2k-r+1)E_(k,r-1).                              (5)

For r=0 the last term is zero. No value of E at a negative derivative order is needed.

Now put k=n+l and r=l+j, and define

    lambda_l=l(l+2n+1),
    Lambda=diag(lambda_1,...,lambda_m).

Writing R_j for column j, equation (5) becomes

    R_(j+4)=2(n-j)R_(j+3)
      -(n-j)(n-j+3)R_(j+2)
      +2(n-j)(n-j+2)R_(j+1)
      +2[Lambda+j(2n+1-j)I]R_j.                           (6)

This holds whenever the indicated columns are retained, and also for their naturally extended derivative sequence. The scalar identity behind the diagonal term is

    (l+j)(2n+l-j+1)=lambda_l+j(2n+1-j).

Let w_s=R_s for s=0,1,2,3. For a block with fewer than four columns use only the starting columns that occur. Define

    W_(4q+s)=(2Lambda)^q w_s, 0<=s<4.                    (7)

There exists an upper unitriangular matrix T over Z[n], of the actual number of columns, such that

    R=W T.                                               (8)

Proof: induction on the column index. It is immediate for indices below four. In (6), the term 2Lambda R_j has leading term W_(j+4). Multiplication of any earlier W_i by 2Lambda gives W_(i+4), still earlier than W_(j+4). Every other term in (6) uses columns of index at most j+3. Thus R_(j+4)=W_(j+4) plus an integer-polynomial combination of earlier W columns. This proves (8), with diagonal entries one. Its inverse is also integral.

Consequently R and W have exactly the same maximal-minor ideal over Z, by Cauchy--Binet in both directions. In particular their maximal-minor contents are equal. Since all minors of R are divisible by A_b^2, so are all minors of W, and dividing all these coordinates by A_b^2 preserves the equality of their generated ideals.

This is an integral transformation of the full R block. It is not asserted to remain unimodular after separately dividing every column by its factorial in Z. Those are two different, explicitly justified reductions.

For endpoint determinants, changing the high block from R to W requires applying the same column transformation to every appended endpoint row. Content calculations alone need no such endpoint-row modification. The original endpoint formulas in Section 6 below stay in their original convention.

## 4. Explicit maximal minors: four groups and only two missing powers

Equation (7) has a useful refinement because a maximal minor deletes exactly two columns.

Fix retained columns J, the complement of i<j in {0,...,m+1}. For s=0,1,2,3, let N_s be the number of available columns congruent to s modulo four. Their exponents in (7) are exactly 0,...,N_s-1. Let A_s be the set of exponents deleted in this group, t_s=|A_s|, and d_s=N_s-t_s. Then

    sum_s t_s=2, sum_s d_s=m.

Thus each exponent group has at most two missing powers. Let Q_J=sum_(j in J) floor(j/4).

Partition the row set {1,...,m} into four ordered subsets I_s of sizes d_s, with each subset listed increasingly. Define

    Delta(I)=product_(u<v in I)(lambda_v-lambda_u)
            =product_(u<v in I)(v-u)(2n+1+u+v).

For a row subset I, write e_a(I) for the elementary symmetric polynomial of degree a in its lambda values, with e_0=1 and e_a=0 for a<0 or a>|I|. Define the following correction factor for group s:

    Phi_s(I)=1                                      if t_s=0;
    Phi_s(I)=e_(d_s-a)(I)                            if A_s={a};
    Phi_s(I)=e_(d_s-a)(I)e_(d_s+1-c)(I)
             -e_(d_s-a+1)(I)e_(d_s-c)(I)             if A_s={a,c}, a<c.

Then the exact minor identity is

    det W_J = 2^Q_J sum_(I_0,...,I_3) epsilon(I,J)
        product_(s=0)^3 [
          (product_(l in I_s) R_(l,s))
          Delta(I_s) Phi_s(I_s)].                         (9)

Only starting columns that actually occur contribute. Empty groups contribute one. The sign epsilon is the product of two permutation signs: grouping the retained columns by s, preserving exponent order within each group; and concatenating the increasing row subsets I_0,I_1,I_2,I_3 relative to their natural row order. This completely specifies the signs.

Proof: extract 2^floor(j/4) from each retained column and expand the grouped determinant by its four column groups. In each summand, R_(l,s) factors from row l of group s, leaving the alternant det[lambda_l^q]. With no missing exponent this is the ordinary Vandermonde. With one missing exponent its quotient by the Vandermonde is e_(d-a). With two missing exponents a<c, its quotient is the two-by-two elementary-symmetric determinant displayed above.

The latter alternant formula can be verified without a limiting argument: the coefficient vectors of P(z)=product_(l in I)(z-lambda_l) and zP(z) span the kernel of the matrix with powers 0,...,d+1. Their two-coordinate determinants give its complementary maximal minors. Substituting [z^a]P=(-1)^(d-a)e_(d-a) gives exactly the displayed difference of two products. The one-hole formula follows in the same way from P alone. These are polynomial identities, so the formulas include empty cases with the stated conventions.

Equation (9) reduces all the growing derivative columns to four actual starting columns, explicit quadratic-node Vandermonde factors, and elementary symmetric corrections. Because only two columns are deleted, each summand has at most two nontrivial elementary-symmetric factors, or a difference of two such products within one group. General high-degree Schur polynomials are unnecessary here.

This is the promised smaller residual problem. The integers

    (det W_J)/A_b^2

are exact alternative generators for the residual ideal in (1). Formula (9), together with (3) and the actual starting columns, describes these generators structurally rather than merely renaming their gcd.

A_b^2 divides the complete sum in (9). It has not been proved to divide each partition summand separately. Nor may the displayed Vandermonde factors be multiplied across different summands to infer a common divisor. Their products and the column powers of two can overlap the factorial content already extracted. No new logarithmic rate is inferred from their sizes.

## 5. A complementary integral state recurrence

The specific H sequence also admits a three-coordinate integral state. For k>=2 put

    h_k=H_k(1),
    u_k=H'_k(1)/k,
    v_k=H''_k(1)/(k(k-1)).

These u_k,v_k are normalized derivatives, unlike the raw derivatives in some earlier notes. They are integers: the coefficient of H_k^(d)/(k)_d is (k-d)_s [z^s](1-z+z^2/2)^k, and the same consecutive-even-factor argument proving H_k integral applies.

The H recurrence and its derivatives yield

    [h_(k+1),u_(k+1),v_(k+1)]^T
      = T_k [h_k,u_k,v_k]^T,

    T_k = [ -k, k^2, k(k-1)/2;
             1, -k, k(k-1)/2;
             1,  1, 1-k(k+1)/2 ].

Every entry is integral, and

    det T_k=k(k-1)(k+1)^2/2.

This supplies another exact representation of the actual state underlying the starting columns. The determinant of a transition matrix is not, by itself, a common divisor of its output coordinates or of the high-block minors. No prime-transfer theorem is extracted from this identity.

## 6. Exact connection to the monic cleared endpoint gcd

Keep precisely the monic cofactor scale of the main-agent draft. Write

    F=(2n+1)!,
    rho_plus=product_(l=1)^(b-1)(2n+2l)!,
    M=2^(2n+3)F^2 rho_plus,
    f=2^n/(n!)^2,
    g=gcd(|MX|,|MY|), on Y!=0.

This g is the cleared endpoint gcd in that particular monic scale. It is not the endpoint gcd after primitive polynomial normalization or the gcd in an arbitrary alternative clearer.

In the completed arithmetic reduction, the primitive high-minor coordinates give integer contractions sigma,c,kappa. Put

    d=gcd(|sigma|,|c|,|kappa|),
    sigma*=sigma/d, c*=c/d, kappa*=kappa/d.

On Y!=0, Gamma and d are positive. With tau=n+1 and the original Legendre and second-kind conventions, define

    D*=tau P_(n+1)c*-2P_n sigma*,
    Q*=2w_P sigma*-tau w_U c*,
    V*=sigma* Acal_n-c* Bcal_n-kappa*,
    U*=Q*+2f V*.

Both partial-exponential contractions Acal_n,Bcal_n and both second-kind values remain present. Equivalently, with T_P=f Acal_n and T_U=2f Bcal_n/tau,

    U*=2(w_P+T_P)sigma*-tau(w_U+T_U)c*-2f kappa*.

The exact original endpoints from that reduction are

    X=(-1)^n Gamma d f U*/[rho_plus 2^(2n+3)],
    Y=(-1)^n Gamma d f D*/[rho_plus 2^(2n+3)].

Therefore define

    N0=f F^2 U*, Z0=f F^2 D*.

Both are integers. Here is a direct integrality check specific to this translation. The T denominators divide F, and fF=2^n(2n+1)binom(2n,n) is an integer. The second-kind denominators divide 2^n(n+1)!, and

    fF^2/[2^n(n+1)!]
      =binom(2n+1,n)^2 (n+1)!

is an integer. Finally 2f^2F^2=2(fF)^2 is an integer. These three observations clear every term of the complete expanded U*. The integrality of Z0 follows from D* integral and fF^2 integral.

Thus, exactly,

    MX=(-1)^n Gamma d N0,
    MY=(-1)^n Gamma d Z0,
    g=Gamma d g0,  g0=gcd(|N0|,|Z0|),
    g/A_b^2=gamma d g0.                                  (10)

This is the required relationship to the monic cleared endpoint gcd. It counts the high-minor factorial content once and retains the further contraction content and final rational endpoint cancellation separately through specified exact normalizations.

In particular,

    q=|Z0|/g0

is the actual reduced denominator. If N0=0, then g0=|Z0| and q=1. If Y=0, none of these quotient assertions applies. The structural reductions do not prove growing-degree endpoint nonvanishing or nonvanishing of the full remainder.

Equation (10) is a local algebraic translation from the completed arithmetic reduction, not a review of the proposed Gaussian estimate or combined sufficient criterion.

## 7. Rates and what remains unproved

For b=floor(n/2),

    log(A_b^2)=n^2 log n/4+O(n^2).

The former strict residual-content target above 1/2 is withdrawn. The completed [content correction](../agent2/GROWING_CONTENT_CORRECTION_SUMMARY.md) gives g<=M|D_V|<=M B_V and hence limsup log g/(n^2 log n)<=3/4 on every unbounded nonzero-endpoint set with b=floor(n/2). Subtracting the proved factorial rate gives

    limsup log(g/A_b^2)/(n^2 log n)<=1/2.

Thus the former strict liminf target above 1/2 is impossible in this normalization, not a live conditional objective. The exact identity (10), g/A_b^2=gamma*d*g0, remains valid and counts all contents once. [Agent 4's additional review](../agent4/ADDITIONAL_GROWING_REVIEW.md) passes the structural arguments and exact gcd translation, with this documentation repair required. No structural proof or prior certificate is changed by withdrawing the target. The ceiling does not exclude shrinking actual forms or differently rebuilt estimates; the separate high-row-slack conclusion is reviewed in REVISED_REMAINDER_INDEPENDENT_REVIEW.md.

The known row factors n+l have only O(n log n) total logarithmic weight and cannot supply a missing positive n^2 log n coefficient. They also overlap Gamma's factorial content. Neither the four-column recurrence nor the transition determinant warrants adding an unproved independent factor to A_b^2.

The useful new result is the exact integral reduction (3), (6), (8), and especially (9): the residual minors are controlled by four actual starting-column weights and explicit Vandermonde sums with at most two missing powers. The next arithmetic problem is to prove divisibility or cancellation bounds for these particular weighted sums, and then translate them through (10). Such a proof must account for cancellations between row partitions and for the actual H sequence; sizes of individual products are insufficient.

## 8. Supporting evidence and execution history

check_additional_growing_content.py and additional_growing_content_certificate.json provide the saved supporting evidence. The final execution returned exit code 0 with sandboxed=true and PASS_SYMBOLIC_STRUCTURAL_IDENTITIES. All twelve checks passed: the two differential translations, derivative recurrence, spectral factor, column-index substitution, integral Taylor recurrence, integral state transition and determinant, the abstract column transformation, and the two monic endpoint scale identities.

The column calculation used twelve abstract columns with symbolic n and spectral variable. It did not evaluate an actual HP degree. The all-size column theorem is proved by induction above; the bounded symbolic check is supporting evidence only. The four-group minor identity follows from Laplace expansion and the annihilating-polynomial argument above; it is not claimed to follow merely from the finite check.

The first execution stopped with two symbolic equality checks unresolved and wrote no success certificate. Rechecking with the intended domain, integer k and positive x, made both differential identities simplify to zero. Their equality there proves the polynomial identities globally. The repaired checker then passed all twelve checks. No mathematical formula was changed during that repair.

No degree sweep, new prime list, growing-prime transfer, networking, installation, or access outside the workspace was used. New writes were confined to the assigned agent1 directory. No independent review outcome or irrationality conclusion is claimed.
