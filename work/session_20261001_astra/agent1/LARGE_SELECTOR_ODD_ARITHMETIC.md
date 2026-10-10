> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large direct selectors: complete odd-prime numerator gate

New author deductions. Offline; no prime scan, numerical computation, or independent review. The main large-selector draft supplies the exact rational components and nonzero endpoint as author inputs. Its dyadic law is neither repeated nor audited.

## Domain and rational normalization

Use n=4k, k>=1, m>=0, and the stated allocation m=-k modulo a power of two P with k<P<=2k. Retain the main author's conclusion U!=0. Set N=2n+4m and J=N-n. Write

 B(t)=(1-2t+2t^2)^n(1-4t+2t^2)^(2m)=sum b_j t^j,
 K(t)=sum_{j=n}^N binom(j,n)b_j t^j,
 U=K(1),
 L=calL((K-U)/(t-1)).

The COMPLETE rational center is

 c=W/(n! J! U),
 W=Vexp+n! J! L,
 Vexp=sum_{j=n}^N b_j (J)_(N-j) D_j.

This identity is over Q before any reduction. It is invariant under any common rational scaling of K, B, and their associated terms; no coefficient-content unit is assumed.

Fix an odd prime satisfying

 max(n,N/2)<p<=J.

Put s=J-p and R=N-p=n+s. Then

 0<=s<p-n, n<=R<p, J=p+s<2p, N=p+R<2p.

In particular v_p(n!)=0 and v_p(J!)=1. There are no old Toeplitz-window restrictions here. The interval may contain no prime at an individual index; every assertion is conditional on a prime in this specified interval.

## The unique moment pole

The moments are

 mu_h=((1+i)^(h+1)-(1-i)^(h+1))/(i 2^h(h+1)).

For 0<=h<N, the only possible p-denominator occurs at h=p-1. Put chi=(-1)^((p-1)/2). In the quadratic algebra over F_p, Frobenius gives

 p mu_(p-1)=2 chi mod p.

Indeed (1+i)^p-(1-i)^p=2 chi i and 2^(p-1)=1. This works in both the split and nonsplit quadratic algebra.

Since (t^j-1)/(t-1)=sum_{h=0}^{j-1}t^h,

 L=sum_{j=n}^N binom(j,n)b_j sum_{h=0}^{j-1}mu_h.

Consequently L is in p^(-1)Z_(p), and

 pL=2 chi U_high mod p,
 U_high=sum_{j=p}^N binom(j,n)b_j.

Thus W is p-integral, although L need not be. Discarding L before multiplication by J! would lose an actual term in the residue of W.

## Surviving exponential terms

For h=N-j, the factor (J)_h is divisible by p exactly when h>s. Hence only j>=p+n survive in Vexp modulo p. For j=p+r, n<=r<=R,

 (J)_(N-j)=s!/(r-n)! mod p,
 D_(p+r)=D_r mod p.

The second equality follows from D_l=lD_(l-1)+1, whose restart at p is D_p=1=D_0. All factorials inverted here have arguments below p.

Lucas reduction also gives

 binom(p+r,n)=binom(r,n) mod p,

which is zero for r<n. Therefore

 U_high=sum_{r=n}^R binom(r,n)b_(p+r) mod p.

Wilson's theorem gives J!/p=-s! mod p. Combining BOTH rational numerator components proves the central identity

 W=s! sum_{r=n}^R b_(p+r) [D_r-2 chi r!]/(r-n)! mod p.       (1)

The minus sign is the Wilson factor; the moment contribution has not been absorbed into an unspecified unit.

## Explicit product-polynomial coefficient condition

Define

 H_p(B)=sum_{r=n}^R b_(p+r) [D_r-2 chi r!]/(r-n)! in F_p.

Equation (1) is an all-index formula W=s! H_p(B) modulo p. It requires only the s+1 high coefficients b_(p+n),...,b_N.

Those coefficients have an explicit short reverse-polynomial formula. Put

 T(t)=(1-t+t^2/2)^n(1-2t+t^2/2)^(2m).

Reciprocity gives exactly

 b_(p+r)=2^(N/2) [t^(R-r)]T(t).

Thus an equivalent finite condition is

 H_p(B)=2^(N/2) sum_{h=0}^s [t^h]T(t)
                *[D_(R-h)-2 chi (R-h)!]/(s-h)!.            (2)

Only coefficients through degree s are needed. Formula (2) specifies the remaining scalar completely; it makes no unit assumption about it.

For an explicit Frobenius extraction directly from the requested product, put A(t)=1-2t+2t^2 and C(t)=1-4t+2t^2. The interval implies n<p and 2m<p. In F_p[[t]], define

 E(t)=A(t)^(-(p-n)) C(t)^(-(p-2m)).

Negative powers are formal series with constant term one, so no nonunit division is involved. Frobenius gives

 B(t)=A(t^p)C(t^p) E(t).

Since A(t^p)C(t^p)=1-6t^p+terms of degree at least 2p, and N<2p,

 b_(p+r)=[t^(p+r)]E(t)-6[t^r]E(t), 0<=r<=R.              (3)

Equations (1) and (3) isolate the surviving high block by Frobenius. Formula (2) is usually shorter to evaluate. There is no assertion that either exponent of B itself crosses p: both are below p in this domain. Introducing the complementary exponents in E is what makes the Frobenius extraction valid.

All quantities in (2)-(3) are finite coefficient conditions at any requested precision; equation (3) is specifically a characteristic-p identity. At higher precision it cannot be reused without its Frobenius correction terms.

## Actual reduced-denominator conclusion

Let q=den(c)>0, and u=v_p(U)>=0. Because W is p-integral and v_p(n!J!U)=1+u, exact rational reduction gives, for W!=0,

 v_p(q)=max(0,1+u-v_p(W)).                              (4)

If W=0, c=0 and q=1. In particular the explicit nonzero test

 H_p(B)!=0

proves

 v_p(q)=1+v_p(U).                                      (5)

Thus the compulsory single factorial p survives completely, including any extra endpoint valuation. This is a theorem about the reduced rational center, not a row clearer.

If H_p(B)=0, then v_p(W)>=1. When U is a p-unit, this already proves v_p(q)=0: the factorial p is completely canceled. Consequently on the explicit additional condition U!=0 mod p the gate is a full equivalence,

 p divides q if and only if H_p(B)!=0,

and v_p(q) is respectively one or zero.

For completeness the endpoint condition itself is explicit:

 U=sum_{j=n}^{p-1} binom(j,n)b_j
       +sum_{r=n}^R binom(r,n)b_(p+r) mod p.             (6)

No endpoint-unit premise is silently imposed. If U is divisible by p and H_p(B)=0, (4) remains the exact criterion, but higher depth is required. The first residue alone does not decide whether p survives.

## Precise complete lift when the gate vanishes

Define the p-integral moment numerators

 eta_h=p mu_h, 0<=h<N,
 L_p=sum_{j=n}^N binom(j,n)b_j sum_{h=0}^{j-1}eta_h=pL.

Then exactly over Q,

 W=Vexp+n! (J!/p) L_p.                                (7)

Every term in (7) is p-integral. To determine survival at a prime dividing U, compute this COMPLETE quantity modulo p^(1+u), or to the first nonzero order if an exact valuation is desired. Nonvanishing modulo p^(1+u) is equivalent to v_p(q)>0. Terms other than eta_(p-1), which vanish in the first residue, must be restored in the lift. Likewise the formerly suppressed falling-factorial terms in Vexp return at positive p-adic orders.

An exact finite method uses the integer coefficients of B, the recurrence D_j=jD_(j-1)+1 through N, and the displayed rational moment formula with its p factor extracted first. All remaining moment denominators are p-units. This specifies the lifting problem without claiming it was computed or that its cancellation is favorable.

No uniform nonzero theorem for H_p(B), no prime scan, and no asymptotic product of surviving primes is established. The new result is the complete one-block residue (1), explicit coefficient tests (2)-(3), the reduced-denominator gate (4)-(6), and the exact higher-depth quantity (7). The allocation's dyadic theorem and its status remain unchanged. No complete-error or irrationality conclusion follows from these local identities.
