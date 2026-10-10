> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Limited independent review of slow-growth contact normality

Verdict: PASS for the theorem in agent3/CONTACT_NORMALITY_RESEARCH.md: in its stated ascending monomial column order, det J_(n,b)>0 whenever n>=16, 2<=b<=n, and n>=512 b^4 log n. The explicit allocation b=floor((n/(512 log n))^(1/4)), n>=2^18, is nonempty and unbounded. No mathematical correction to this theorem or its prefactors is required.

This review covers the new exact logarithmic-block reduction, Toeplitz determinant, complete circle integral, uniform bounds, and allocation. It does not reopen any endpoint, Bernstein, fixed-degree, or two-scalar audit. The source's optional differential-annihilator reformulation is unnecessary to this verdict and is not separately certified here. The proof below is a paper verification; no numerical scan or previous checker was executed.

## Exact reduction and signs

The square matrix has Taylor rows 0,...,2n+b-1 and columns z^j for j<n, z^j exp(z) for j<b, and z^j F(z) for j<n, in that order. Set Q=1-z+z^2/2, alpha=1+i, beta=1-i, and delta=2i. Direct differentiation gives F'=2/Q=-2i[(z-alpha)^(-1)-(z-beta)^(-1)].

For C of degree less than n, U_n(C)=Q^n D^n(CF) is rational and has degree less than n. To verify the latter assertion and its determinant, use C_j=(z-alpha)^j(z-beta)^(n-1-j), 0<=j<n. These form a basis over Q(i): division by (z-beta)^(n-1) turns a linear relation into a polynomial relation in the nonconstant Mobius coordinate w=(z-alpha)/(z-beta).

With u=z-beta and w=1-delta/u, the covariance identity is

D_z^n[u^(n-1)f(w)]=delta^n u^(-n-1) f^(n)(w).

One can verify it first by expanding f near w=1. Terms with power r<n vanish after differentiation; for r>=n, D^n u^(n-1-r)=(-1)^n r!/(r-n)! u^(-r-1). Together with the factor (-delta)^r this agrees termwise with the right side. The resulting identities continue to the local germ needed for CF. Changing the logarithm branch adds a multiple of C and hence does not affect D^n(CF).

For 0<=j<n,

D_w^n(w^j log w)=(-1)^(n-j-1)j!(n-j-1)!w^(j-n).

Since Q=(z-alpha)(z-beta)/2, it follows that

U_n(C_j)=2 i^(n-1)(-1)^(n-j-1)j!(n-j-1)! C_j.

Multiplying these eigenvalues yields det U_n=2^n P_n^2, where P_n=product_(j=0)^(n-1) j!. Indeed i^(n(n-1))=(-1)^(n(n-1)/2), which cancels the product of the displayed real signs. The determinant is positive for both parities of n. This also proves invertibility and the claimed image space.

Eliminating the initial polynomial identity block leaves Taylor rows n,...,2n+b-1. Replacing these by the first n+b coefficients of the nth derivatives multiplies row k by (n+k)!/k!, for 0<=k<n+b. Therefore recovering the original determinant supplies the factor product k!/(n+k)!.

On the exponential columns, (D+1)^n is triangular with diagonal one. On the logarithmic columns, the column transformation is U_n with determinant 2^n P_n^2. Multiplication of all differentiated functions by Q^n is a lower triangular transformation of Taylor rows with diagonal one. The resulting columns are z^j exp(z)Q(z)^n, j<b, followed by z^j, j<n.

Swapping these blocks contributes (-1)^(nb). Elimination of the polynomial block leaves Delta_(n,b)=det[g_(n+i-j)]_(i,j=0,...,b-1), where exp(z)Q(z)^n=sum g_m z^m. Finally,

product_(k=0)^(n+b-1) k!/(n+k)!=P_n/product_(m=n+b)^(2n+b-1) m!.

Consequently the exact formula is

det J_(n,b)=(-1)^(nb) K_(n,b) Delta_(n,b),
K_(n,b)=2^n P_n^3/product_(m=n+b)^(2n+b-1) m!>0.

The prefactor in the source is correct. Every entry of the remaining determinant uses a positive index between n-b+1 and n+b-1. The coefficient recurrence also follows directly from QG'= (Q+nQ')G:

(m+1)g_(m+1)=(m+1-n)g_m+(2n-m-1)g_(m-1)/2+g_(m-2)/2,

with g_0=1 and negative subscripts zero. No factorial with a negative argument is required by its direct coefficient formula.

## Complete circle integral

Put a=sqrt(2) and z=a exp(i theta). Exactly,

Q(z)/z=a cos(theta)-1.

Thus w_n(theta)=exp(a exp(i theta))(a cos(theta)-1)^n equals G_n(z)/z^n. Its kth Fourier coefficient, using integration against exp(-ik theta), is a^k g_(n+k). In the Toeplitz determinant these factors cancel between row and column scalings.

Expansion of the two Vandermonde determinants gives

Delta_(n,b)=1/[b!(2pi)^b] integral product_l w_n(theta_l) |V(exp(i theta_1),...,exp(i theta_b))|^2 dtheta.

This identity does not assume that the weight is positive or real. It is an identity of finite determinant expansions; the integrands are continuous on the compact torus. It integrates the entire function G_n, not a branch of F.

Translate theta_l=u_l+pi periodically. Let h(u)=1+a cos u and M0=1+a. Then the real part of the translated weight is represented exactly by

(-1)^(nb)b! Delta_(n,b)
=(2pi)^(-b) integral |V(exp(iu))|^2 product_l[h(u_l)^n exp(-a cos u_l)] cos(a sum_l sin u_l) du.

Simultaneous reflection of all u_l cancels the imaginary part. The factor (-1)^(nb) comes from the b factors (-h)^n. The signs of h^n for odd n are retained in this expression. Translating the Vandermonde contributes no factor to its squared absolute value.

## Uniform scalar bound and central mass

For every |u|<=pi,

|h(u)|<=M0 exp(-u^2/16).

If h>=0, use a/(1+a)>1/2, 1-cos u>=2u^2/pi^2, and 1-x<=exp(-x), followed by pi<4. If h<0, then |h|/M0<1/4, whereas exp(-u^2/16)>exp(-1)>1/3. Both estimates are valid at the transition h=0.

Set delta0=1/(2b) and let the central box be |u_l|<=delta0. There h is positive and |a sum sin u_l|<=a/2. Hence cos(a sum sin u_l)>=1-a^2/8=3/4.

Define Z_G and Z_tail as the integrals of the nonnegative absolute weight over this box and its complement, including normalization (2pi)^(-b). The complete determinant satisfies

(-1)^(nb)b! Delta_(n,b)>=(3/4)Z_G-Z_tail.

The complement includes all odd-n negative weights and all adverse phases. No positivity is assumed there.

When n>=4b^2, use the b separated intervals

I_j=[-1/sqrt(n)+2(j-1)/(b sqrt(n)), -1/sqrt(n)+(2j-1)/(b sqrt(n))].

Each has length 1/(b sqrt(n)); the gaps have that same length. Their product is inside the central box. On them h/M0>=1-u^2/2>=1-1/(2n), and Bernoulli's inequality gives h^n>=M0^n/2. Also exp(-a cos u)>=exp(-a).

For different intervals the angular separation is at least 1/(b sqrt(n)) and at most 2/sqrt(n)<=pi. The chord estimate 2 sin(|u-v|/2)>=2|u-v|/pi>=|u-v|/2 therefore gives a distance at least 1/(2b sqrt(n)). It follows that

Z_G>=L=M0^(nb)2^(-b)exp(-ab)(2b sqrt(n))^(-b(b-1))(2pi b sqrt(n))^(-b)>0.

This uses only one ordered product of intervals. There is no unaccounted b! in this lower bound.

## Complete tail and constants

Outside the box, sum u_l^2>=1/(4b^2). Applying the scalar Gaussian bound, the chord upper bound 2, and exp(-a cos u)<=exp(a), and using normalized torus volume one, gives

Z_tail<=U=M0^(nb)exp(ab)4^(b(b-1)/2)exp(-n/(64b^2)).

Cancellation of all powers in U/L gives exactly

U/L=exp(-n/(64b^2))(4b sqrt(n))^(b^2)(pi exp(2a))^b.

In particular the exponent b^2 on the middle factor is correct; no dimension factor has been dropped.

The hypothesis n>=512b^4 log n implies n>=4b^2 in the stated domain. Therefore log(4b sqrt(n))<=log(2n)<=2 log n. Also log pi+2sqrt(2)<5, b<=b^2/2, and log n>2. These imply

b^2 log(4b sqrt(n))+b(log pi+2sqrt(2))<4b^2 log n.

Meanwhile n/(64b^2)>=8b^2 log n. Thus U/L<=n^(-4b^2)<1/4. Combining the complete-tail and central estimates proves

(-1)^(nb)Delta_(n,b)>=L/(2b!)>0,

det J_(n,b)>=K_(n,b)L/(2b!)>0.

These constants are uniform for all pairs in the claimed domain. They prove the full determinant sign without a parity restriction.

## Nonempty unbounded range and scope

For n>=2^18 the function n/log n is increasing. At the initial value, log n=18 log 2<18 and 2^18>512*2^4*18. Thus n/(512 log n)>16 throughout this interval. Its fourth-root floor b_*(n) is at least two, satisfies b_*(n)<=n, and obeys n>=512b_*(n)^4 log n. Since n/log n tends to infinity, b_*(n) is unbounded.

The stated endpoint-rank consequence follows on this domain: an endpoint-zero matched triple is divisible componentwise by z-1 and gives a vector in ker J. Nonsingularity makes that vector zero; the dimension count then makes the endpoint map an isomorphism onto Q^2. This consequence supplies the domain needed for the rational lift in the arithmetic research.

The theorem does not cover the proportional allocation b=floor(n/2) for large n. It proves neither inverse conditioning nor reduced-center denominator estimates, and it supplies no shrinking-pair theorem. Those remain separate research obligations. The existing two-scalar audit and its 907 checks were not reopened or repeated.
