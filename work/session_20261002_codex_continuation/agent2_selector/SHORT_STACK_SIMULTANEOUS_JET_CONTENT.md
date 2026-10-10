> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete short-stack simultaneous jet and two-sided content interface

Author work in progress, 2026-10-02. The exact reductions and divisor sandwich below are proved. A uniform size estimate for their two rectangular contents remains open. Generic Pade/Smith theory is classical; the actual moment projections and final normalization are retained explicitly.

## 1. Complete formal functions

Let d_r=D_(2r), f_r=(2r)!, a_r=1/(2r+1). Define FORMAL series D(z),F(z),A(z) with these respective coefficients, and put

    V(z)=1/(1+z), C(z)=D(z)-V(z),
    R(z)=-F(z)+4z A(z)/(1+z).

These series need not converge analytically; all statements are coefficient identities. They retain both the factorial and the full arctangent term. With

    L0=4z^3 d^2/dz^2+10z^2 d/dz+(2z-1),

the exact recurrences give

    L0 F=-1,
    L0 D=-1+z(1+z)/(1-z)^2,
    2z A'+A=1/(1-z),
    L0 C=-1+z(1+z)/(1-z)^2+(7z^2+1)/(1+z)^3.

Initial values are D0=F0=A0=1, C0=0, R0=-1. Reduction modulo p is valid for every needed finite jet when p>6k-5; no nonexistent arctangent coefficient with denominator divisible by p is introduced.

## 2. Moving the response to one column and one row

Retain the actual M24 matrices and integer pair

    M=[C;L_k R],
    u=(0,...,0,1,-1,...,(-1)^(k-1))^t,
    v=(1,-1,...,(-1)^(2k-1))^t,
    det(M+t uv^t)=I0+t J1,
    I0=L_k^k beta0, J1=L_k^(k-1) beta1,
    I1=L_k J1.

All matrices and vectors displayed here are integral; u and v are primitive. The physical parameter is t=L_k S, not t=S. This distinction retains the compulsory row-clearer factor in the ACTUAL coefficient pair.

The integer column basis

    1, (y+1), y(y+1), ..., y^(2k-2)(y+1)

has determinant 1 and sends evaluation v to the first coordinate. Its last 2k-1 columns form the ACTUAL tall matrix

    N=[G;L_k K],
    G_r=d_r+d_(r+1),
    K_r=-f_r-f_(r+1)+4/(2r+1),

with k rows in each block, columns j=0,...,2k-2. The identity K_r=R_r+R_(r+1) retains the complete rational term.

The lower-row basis R0, R1+R0,...,R_(k-1)+R_(k-2) has determinant 1 and moves u to one row. Omitting that response row gives the ACTUAL wide matrix

    W=[C;L_k K],

with k C rows, k-1 K rows and columns j=0,...,2k-1. Write h_N and h_W for the positive gcds of ALL maximal minors of these two rectangular matrices. Whenever beta1!=0 they have full rational rank, so their contents are positive.

Both h_N and h_W divide I0 and J1, because each is a cofactor divisor of the corresponding one-column or one-row extension. They therefore divide BOTH physical coefficients I0,I1. No extra right-family column has been added; these are integer changes of basis of the fixed M24 construction.

## 3. The full all-prime gcd sandwich

The actual common divisor satisfies

    lcm(h_N,h_W) divides G_actual=gcd(I0,L_k J1),
    G_actual divides L_k h_N h_W.

Consequently the actual reduced denominator has the honest two-sided interface

    abs(J1)/(h_N h_W) <= q_actual
      <= L_k abs(J1)/lcm(h_N,h_W),
    q_actual=L_k abs(J1)/gcd(I0,L_k J1).

These bounds do not assume the two rectangular contents are coprime. In particular one cannot multiply two lower bounds on common content without accounting for overlap. A useful sharp size estimate for h_N,h_W is still required before the lower bound is an asymptotic obstruction.

### Local proof with all carries

After integer unimodular row/column changes taking primitive u,v to the first coordinates, write the base pencil as

    [[a+t,b],[c,H]].

The coefficient J1 is det H, up to a common sign. Work over Z_p and take a Smith form H=diag(p^lambda_i), absorbing units into b,c; lambda_i>=0. This does not alter any relevant local content. Put s=sum lambda_i, and

    U=max(0,max_i(lambda_i-v_p(b_i))),
    V=max(0,max_i(lambda_i-v_p(c_i))),
    alpha=v_p(h_N)=s-U,
    gamma=v_p(h_W)=s-V.

Zero b_i,c_i have infinite valuation and contribute no positive deficit. Exactly

    I0=a det H-sum_i b_i c_i product_(j!=i)p^lambda_j,
    g0=v_p gcd(I0,J1)=min(v_p(I0),s).

The cofactor divisibility already gives max(alpha,gamma)<=g0. If U+V<=s, then alpha+gamma>=s>=g0. If U+V>s, the maximum deficits must occur at the SAME unique index i: different indices would give U+V<=lambda_i+lambda_j<=s. Its term in I0 has valuation

    s+lambda_i-U-V,

strictly smaller than s and all other terms, because U+V>s>=lambda_i+lambda_j. There is no cancellation and

    g0=s+lambda_i-U-V<=alpha+gamma.

Thus max(alpha,gamma)<=g0<=alpha+gamma at every prime. Finally, with ell=v_p(L_k),

    v_p(G_actual)=min(v_p(I0),s+ell),
    g0<=v_p(G_actual)<=g0+ell.

This proves the stated global sandwich. It also records an exact carried answer when U+V>s; the potentially cancelling case U+V<=s retains the COMPLETE sum for I0 rather than its lowest individual term.

## 4. Simultaneous field zeros and the two jet branches

For p not dividing L_k, both physical coefficients vanish modulo p if and only if N OR W loses maximal rank modulo p. This statement includes all coranks.

For a direct proof put M0=[C;R]. At corank 1 its adjugate is a nonzero scalar times x y^t, with right and left nullvectors. The response coefficient is a scalar times (v^t x)(y^t u). A right-null endpoint zero gives rank loss of N; a left-null response zero gives rank loss of W. At corank>=2 there is a right nullvector with v^t x=0 and a left nullvector with y^t u=0, so both rectangular tests lose rank. Conversely a nullvector satisfying either extra condition forces both coefficients to vanish. At primes dividing L_k, the correct base pair is I0,J1 and the physical extra factor ell is retained by Section 3; one must not transfer the unscaled field statement blindly.

The right branch is an ACTUAL polynomial Q(y)=(y+1)P(y), deg P<=2k-2, satisfying all k G and all k K moments. It is a type-II common-denominator jet with 2k conditions on 2k-1 coefficients.

The left branch has lower response polynomial B(y)=(y+1)P(y), deg P<=k-2, and top polynomial A(y), deg A<=k-1. It gives

    sum_i A_i C_(i+j)+sum_i P_i K_(i+j)=0,
    0<=j<2k.

Reversing both polynomials to degree k-1 gives Q_C(z),Q_K(z), with z dividing Q_K, and a numerator of degree<=k-2 such that

    Q_C(z)C(z)+Q_K(z)K(z)-P0(z)=O(z^(3k-1)).

This is a type-I finite jet with the lower endpoint constraint retained. The two branches cannot be replaced by one without losing possible complete common content.

## 5. Current scope

The simple Gamma rational-ODE normality proof does not automatically apply to these joint jets. The factorial, derangement forcing and arctangent first-order equation must all be retained. The current exact sandwich reduces the actual final-gcd question to two specified rectangular contents and a controlled overlap, but supplies no all-k upper bound on those contents at the scale needed for an irrationality conclusion.

One pre-existing k=5 complete pair was used to test the precise large-prime-content hypothesis: after removing every prime <=6k-5 from its FULL gcd, the cofactor is 1. This is a hypothesis check of one existing normalization, not a prime atlas or a proof of a uniform support bound. No prime-support claim is made. The next author step is a lower-block-dependent jet/Smith estimate for h_N or h_W, with the full primitive normalization above.

The same single k=5 receipt computes the NEW two rectangular contents by exact integer Smith forms, rather than using a row clearer as content. It obtains h_N=41878198878732288000 and h_W=654346857480192000, checks their divisibility into BOTH full base coefficients, the base and physical gcd sandwiches, and exact agreement with the already-saved 308-bit actual q. All assertions pass in `short_stack_joint_content_receipt.py`; results are saved in `SHORT_STACK_JOINT_CONTENT_RECEIPT.json`. These two large contents are actual lower-block-dependent divisors; their one-instance sizes or ratio are not asserted as all-k formulas.

## 6. Exact elimination of the arctangent particular solution

The exponential generating functions give an additional exact structural reduction. Put

    d_E(z)=sum_r d_r z^(2r)/(2r)!=(cosh z-z sinh z)/(1-z^2),
    f_E(z)=1/(1-z^2), v_E(z)=cos z,
    C_E=d_E-cos z, R_E=-f_E+Z(z).

The COMPLETE rational companion has the unique even formal particular solution

    Z''+Z=4 sinh z/z, Z(0)=Z'(0)=0.

Multiplication by y+1 becomes the operator d^2/dz^2+1. Therefore the two actual transformed moment functions are

    G_E=d_E+d_E''
      =2[(1+z^2+2z^4)cosh z-z(2+z^2+z^4)sinh z]/(1-z^2)^3,
    K_E=R_E+R_E''
      =4 sinh z/z-(z^4+4z^2+3)/(1-z^2)^3.

The arctangent particular solution has been eliminated EXACTLY, not estimated or dropped. G_E and K_E are elementary rational combinations of e^z,e^(-z),1. The left-branch C_E retains the cos z endpoint response as required. This is a basis reduction of the original m=1 family and does not define a new higher-pole family.

It suggests a concrete Hermite--Pade or jet-lattice approach to h_N,h_W. However it is not itself a normality theorem over finite fields: differentiating the rational coefficients raises their endpoint pole orders, and clearing those poles raises coefficient degrees. The generic Gamma scalar proof's degree count cannot be transferred without a new bound. Any future resultant or Vandermonde extraction must count this denominator/degree cost and must return to the physical I0,L_k J1 gcd.

## 7. Exact primitive cofactor extraction and the remaining overlap

The two rectangular contents can be removed exactly from the physical coefficient pair, without estimating them or invoking a new matching family. In the original column basis 1,(y+1),...,y^(2k-2)(y+1), let m0 be the first column of the full integer stack. If w is the PRIMITIVE left nullvector of N, its signed maximal-minor vector is h_N w, with one common orientation sign. Therefore

    I0=epsilon h_N (w^t m0),
    J1=epsilon h_N (w^t u),
    q_actual=L_k abs(w^t u)/gcd(w^t m0,L_k w^t u).       (11)

All entries in the scalar gcd are integers. The actual beta1 nonzero premise ensures w^t u!=0, so this formula never divides by a zero response. This is a fixed codimension-one cofactor extraction, not a larger-column Siegel lattice or a new response-tuning operation.

There is a useful symmetric form which accounts for the overlap of BOTH contents. Put

    D=lcm(h_N,h_W), g=gcd(h_N,h_W),
    s=I0/D, t=J1/D.

The exact common divisor sandwich from Section3 implies

    gcd(s,t) | g,
    gcd(s,L_k t) | L_k g,
    q_actual=L_k abs(t)/gcd(s,L_k t).                   (12)

Thus the mandatory lcm has already canceled in BOTH entries. Any further primitive reduction is supported in the actual overlap g together with the physical clearer L_k; at primes outside that support the remaining scalar pair is primitive. This assertion retains every carried cancellation through the displayed exact gcd, rather than claiming coprimality of s,t.

For a cofactor interpretation write h_N=g a,h_W=g b with gcd(a,b)=1. The two primitive response contractions satisfy

    J1=h_N b_N=h_W b_W,
    b_N=b t, b_W=a t.

Consequently t is the response AFTER the entire guaranteed lcm extraction. The new compact-diagonal basis has nontrivial theta indices, so one must transfer its contents by the exact formulas in `SHORT_STACK_COMPACT_DIAGONAL_INDEX.md` before using (11)--(12). Its basis-induced common factors cannot be counted as favorable actual overlap.
