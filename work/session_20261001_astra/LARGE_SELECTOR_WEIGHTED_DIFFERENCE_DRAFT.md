> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A weighted finite difference eliminating the logarithmic constant

Status: main-agent author research, not independently reviewed. The saved exact checker completed 15 cases (n=4,8,12 and m=0,...,4): polynomial identities and rational-lattice assertions passed, and all 15 certificates were nonzero. The evidence file large_selector_weighted_difference_checks.json was read back. These finite results do not prove unbounded nonvanishing. The principal nonvanishing condition remains open. The consequence below concerns selected members of parameter blocks, not every large selector and not the irrationality of e+pi.

## 1. Definitions that also cover zero forcing

Let n=4k>=4, r=n/2, and m>=0 be integers. Put

B_m(t)=(1-2t+2t^2)^n(1-4t+2t^2)^(2m),
K_m(t)=t^n B_m^(n)(t)/n!,
U_m=K_m(1),
T_m=calL((K_m-U_m)/(t-1)),
calL(f)=integral_{-1}^1 f((1+iu)/2)du.

Both U_m and T_m are defined when U_m=0. The first is an integer and the second is rational. When U_m!=0, beta_m=T_m/U_m is the logarithmic rational companion.

The saved polynomial selection proof gives that U_m, as a polynomial in m, has degree r and leading coefficient 4^r/r!. In particular U_m^2 has degree n. Also 2^r divides every U_m.

Set d=n+1 and define the entirely rational certificate

W(n,m)=sum_{j=0}^d (-1)^(d-j) binom(d,j) U_(m+j) T_(m+j).

Since Delta^d(U_m^2)=0, this has the exact alternative expression

W(n,m)=sum_{j=0}^d (-1)^(d-j) binom(d,j)
        U_(m+j)(T_(m+j)-pi U_(m+j)).                 (1)

For U_(m+j)!=0, its summand is U_(m+j)^2(beta_(m+j)-pi). For U_(m+j)=0, its summand is zero. This avoids the zero-forcing-node problem that arises with an unweighted difference of T_m.

## 2. A polynomial integral for the certificate

Write a=(1+i)/2, abar=(1-i)/2, V(w)=w^2-w+1/2, and z(w)=(2w^2-1)^2. The path C goes from abar to a along the straight segment. It does not pass through zero.

Direct integration by parts proves

T_m-pi U_m = i 2^(n+1) integral_C
                 V(w)^n(2w^2-1)^(2m)/w^(n+1) dw.  (2)

Indeed calL(1/(t-1))=-pi, so the left side is calL(K_m/(t-1)). In the latter integral integrate B_m^(n) by parts n times. Boundary terms vanish because B_m has zeros of order at least n at a and abar. The identity

D_t^n(t^n/(t-1))=(-1)^n n!/(t-1)^(n+1)

then applies. Substitute w=1-t and retain the reversed endpoints. For even n the resulting multiplier is i 2^(n+1), as in (2).

Define the integer polynomial

P_(n,m)(z)=sum_{j=0}^d (-1)^(d-j) binom(d,j) U_(m+j) z^j.

For 0<=ell<=r, its ell-th derivative at z=1 is the d-th difference of U_(m+j)(j)_ell. This is a polynomial in j of degree at most r+ell<=n<d, so the derivative is zero. Therefore

P_(n,m)(z)=(z-1)^(r+1) Q_(n,m)(z),
Q_(n,m) belongs to Z[z], deg Q_(n,m)<=r.            (3)

Integer coefficients follow by division by the monic integer polynomial (z-1)^(r+1). This argument does not require individual U values to be nonzero.

Because z(w)-1=4w^2(w^2-1), substitution of (2)-(3) into (1) cancels the entire pole at zero. Define the rational-coefficient polynomial

S_(n,m)(w)=w V(w)^n(w^2-1)^(r+1)(2w^2-1)^(2m)
           Q_(n,m)((2w^2-1)^2).

Then

W(n,m)=i 2^(2n+3) integral_abar^a S_(n,m)(w)dw.     (4)

The integrand is now a polynomial of degree at most 5n+4m+3. If A_(n,m) is its polynomial primitive with constant term zero, its coefficients are real rational numbers, and

W(n,m)=-2^(2n+4) Im A_(n,m)(a).                    (5)

Equation (5) is a finite Gaussian-rational evaluation. It neither involves an approximation to pi nor suppresses a conjugate contribution.

## 3. An exact rational lattice

Put L=5n+4m+4 and let O_L be the least common multiple of the odd positive integers at most L.

The coefficients of S have denominators dividing a power of two. Evaluating its primitive at a introduces only additional powers of two and integer denominators at most L. Consequently the odd part of the reduced denominator of W divides O_L.

There is also a dyadic lower valuation. If b_j is the coefficient of t^j in B_m, then v_2(b_j)>=ceil(j/2). For

mu_l=calL(t^l)=((1+i)^(l+1)-(1-i)^(l+1))/(i 2^l(l+1)),

one has v_2(mu_l)>=1-floor((l+1)/2), with zero moments interpreted as having infinite valuation. The coefficient of t^j in K_m is binom(j,n)b_j. Expanding

(K_m-U_m)/(t-1)=sum_{j>=n} [t^j]K_m (1+t+...+t^(j-1))

therefore proves v_2(T_m)>=1, term by term. Since v_2(U_m)>=r, each summand defining W has valuation at least r+1. Combining the odd and dyadic assertions gives

O_L W(n,m) belongs to 2^(r+1) Z.                  (6)

Thus

W(n,m)!=0 implies |W(n,m)|>=2^(r+1)/O_L.           (7)

This is an implication, not a proof of W(n,m)!=0.

## 4. A block lower bound, conditional only on this certificate

Let Amax=max_{0<=j<=d}|U_(m+j)|. Since there are d+1>r nodes, Amax>0. Equations (1) and (7), and the absolute coefficient sum 2^d, imply that if W(n,m)!=0, some j in [0,d] satisfies U_(m+j)!=0 and

|beta_(m+j)-pi| >= 1/(2^r O_L Amax^2).             (8)

No assumption that every forcing value is nonzero is needed. The witness need not be a maximizer of |U|, and (8) does not establish the separate large-U selection property.

Now fix rho>0 and let m=rho n log n+O(n). The Cauchy estimate in LARGE_SELECTOR_SELECTION_DRAFT.md applies uniformly across this block and gives

log Amax <= (n/2)log log n+O_rho(n).

Using O_L<=4^L in (8), the witness has

log|beta_(m+j)-pi| >= -4rho log(4) n log n
                                  -n log log n-O_rho(n). (9)

The saved author exponential estimate, together with the integer divisibility |U|>=2^r on every nonzero node, gives uniformly

log|e-alpha_(m+j)| <= -n log n+n log log n+O_rho(n).

For 4rho log 4<1 this is negligible compared with (9). Hence the same witness has a nonzero complete error with the same lower rate.

## 5. Actual denominator consequence without the pending dyadic equality

For every nonzero U, the moment calculation above also gives

O_N T belongs to 2 Z, N=2n+4m,
den(beta) divides O_N |U|/2.                       (10)

The odd denominator assertion follows directly from the moment indices, and the dyadic assertion is v_2(T)>=1. Thus (10) is valid without the special parity allocation. This extension of the stated allocation-specific bound is an author deduction here; no independent examination is claimed.

Let c=alpha+beta and q=den(c) after full rational reduction. Then den(alpha)<=q den(beta). Combining (10), the saved factorial exponential bound, and the saved elementary inequality

|e-a/b|>=C_epsilon b^(-2-epsilon)

for rational a/b in reduced form, yields uniformly for nonzero nodes with m=rho n log n+O(n)

liminf log q/(n log n)>=1/2-4rho log 4.             (11)

To see this explicitly, the exponential bound has logarithm at most

-n log n+n log log n+O_rho(n)-log|U|,

whereas log den(beta)<=N log 4+log|U|. After combining inequalities, divide by n log n, use log|U|=o(n log n), and let epsilon decrease to zero. No exact dyadic-denominator theorem is needed for (11).

If W(n,m)!=0 on an unbounded sequence n=4k with m=rho n log n+O(n), then for one nonzero node in each such block, (9)-(11) give

liminf log(q |c-(e+pi)|)/(n log n)
    >=1/2-8rho log 4.                              (12)

In particular the selected primitive errors diverge when

0<rho<1/(16 log 4).

This is conditional on the unbounded nonvanishing of W. Even if that condition is established, the conclusion concerns a selection from each block. It does not exclude all choices of m in the block or all large-selector constructions.

## 6. Exact unresolved question

Prove W(n,floor(rho n log n))!=0 on an explicit unbounded family in the stated rho range, or find a comparably short nearby block with this property. Equations (3)-(5) give an exact polynomial evaluation to study. A finite list of nonzero values cannot establish the required unbounded assertion.

The new certificate removes pi exactly and preserves zero-forcing nodes correctly. It does not by itself prove its own nonvanishing, any all-family obstruction, or irrationality of e+pi.
