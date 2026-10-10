> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete shared-five correction on the critical reflected subsequence

2026-10-02. Original author synthesis of the selector's period-exact correction, the arithmetic agent's actual denominator theorem, and the analysis agent's complete critical-window convergence. This is a continuation of the gated even-leading-quadratic target, not a new generic denominator claim. Its prior-art gate is recorded in `EVEN_LEADING_QUADRATIC_CORRECTION_COST.md`.

## 1. Inputs and their exact scope

Take N=2^s and define the analysis agent's exact inverse curve by Psi(t,N)=t/R_t−2R_t+log(R_t/(4t))=0, R_t=sqrt(N/t). Choose n to be the nearest multiple of20 to its root near sqrt(2N), and set h=N−n. For sufficiently large s, n,h>=6, n is a multiple of4 and h is a multiple of4. The underlying rational kernels and actual matched center are exactly those in `REFLECTION_EXACT_COEFFICIENT_HANDOFF.md`:

    F0=(1−2w+2w²)^N/[w^(N+1)(1−w)^h], F1=wF0,
    F=m1F0−m0F1, U=M1R0−M0R1>0,
    c=−[E/N!+Pi]/U.

The final evaluated numerator/shared-response gcd is retained. Write the ACTUAL reduced center as

    c=A/[2^N 5^b B0],
    A odd, gcd(A,2^N5^bB0)=1, gcd(B0,10)=1.

The selector's all-h dyadic theorem and the power-two eligibility give tau=v2(q)=N. The arithmetic agent's independently authored `agent1_arithmetic/REFLECTED_ACTUAL_FIVE_DENOMINATOR.md` complete-q theorem gives, for n divisible by20 and h>=6,

    b=v5(q)=v5(N!)+v5(U)
       >=(N−s5(N))/4=N/4−O(log N).                 (1)

This uses its proved unit property for the COMPLETE E=N!B(F), and the exact Pi contribution; it is not an inference from a raw factorial clearer. Here s5 is the base-five digit sum.

The analysis agent's complete `agent3_analysis/POWER_TWO_INVERSE_CRITICAL_SUBSEQUENCE.md` theorem gives c→S=e+pi and, on the exact inverse-curve subsequence rounded to a20-multiple,

    |S−c|=O(n^(−1/2)), N~n²/2.                   (2)

Both vertical endpoints and exponential forcing are present in (2). No positive lower bound for |S−c| is an input.

## 2. An entirely explicit coefficient and pole choice

Fix the primitive integer quadratic

    Q(w)=2w²−10w+13.

Its two poles are 5/2±i/2 and lie off the vertical integration segment. Choose the least odd r>=(N+1)/2 with5 not dividing r. If r+1=b, replace r by the next odd integer not divisible by5. This optional replacement removes the tied case and changes r by at most4. Put

    d=r+1=N/2+O(1), j=2r−1−N, 0<=j<=15.

The endpoint numerator

    Y=Im[(4+4r−i(2+r))(2+i)^(r+1)]

is odd and is a5-adic unit. Set eta=Y/(2^N5^d), m=max(b,d). Choose k in the concrete residue class

    k Y B0 5^(m−d)=A5^(m−b) mod2^N,              (3)

with5 not dividing k and |k|<=(5/2)2^N. Five consecutive representatives of the same class always supply such a k. Equation (3) involves only known exact rational coefficients, not S.

The correction kernel is the exact rational differential

    K=H″+H′, H=U k2^j Q^(−r).

Every ordinary and e^w-twisted finite-pole residue of K is zero, so the entire target response is preserved and no new periods occur. Its full evaluated effect is

    c_k=c−k eta, S−c_k=(S−c)+k eta.              (4)

## 3. Actual q, including ties

Before any prime cancellation the full common denominator is2^N B0 5^m, and the exact numerator is

    A5^(m−b)−kY B0 5^(m−d).

Every prime power of B0 survives unchanged, because the first summand is a unit at each such prime and the second is divisible by B0. Equation (3) removes the entire dyadic denominator.

If b!=d, exactly one of the two summands is a5-adic unit. Consequently

    q_k=B0 5^max(b,d),
    q_k/q=5^max(d−b,0)/2^N.                      (5)

If the optional untied replacement is not made and b=d, the exact formula instead is

    q_k=B0 5^max(0,b−v5(A−kYB0)).               (6)

Infinite valuation for a zero numerator makes (6) valid without division by that numerator. Extra tied content can only help the denominator reduction. The explicit untied version (5) is useful when a uniform compulsory factor is desired.

Using (1), both (5) and (6) imply

    q_k/q <= exp[−gamma N+O(log N)],
    gamma=log2−(log5)/4=0.2907877...>0.           (7)

Thus this is a genuine exponential reduction of the ACTUAL final denominator. In the untied implementation its remaining compulsory factor obeys

    q_k>=5^d=exp[((log5)/2)N+O(1)].               (8)

All old primes other than2,5 remain exactly as B0. Neither (7) nor (8) estimates their size or assumes they cancel.

## 4. Complete signed error and written coefficient costs

At a=(1+i)/2, |Q(a)|=4sqrt5 and |Q′(a)/Q(a)|=sqrt17/(2sqrt5)<1. Retaining H and H′ together, the exact conjugate-endpoint evaluation gives

    |k eta| <= 5(r+1)5^(−r/2)
              =exp[−((log5)/4)N+O(log N)].        (9)

This includes the complete coefficient allowance |k|<=(5/2)2^N and the normalization2^j: the powers cancel because N+j=2r−1. No endpoint or derivative term is discarded.

Equations (2),(4),(9) give the COMPLETE conclusion

    |S−c_k| <= |S−c|+5(r+1)5^(−r/2)
               =O(n^(−1/2)), c_k→e+pi.          (10)

The exact primitive residual satisfies only the signed identity and bound

    q_k(S−c_k)=q_k[(S−c)+k eta],
    |q_k(S−c_k)|<=q_k[|S−c|+5(r+1)5^(−r/2)].    (11)

The presently known polynomial error in (2) does not make the right-hand side small on the N-scale. Even the endpoint correction's own proven upper bound has exponent(log5)/4, while the untied denominator has compulsory exponent(log5)/2 in (8). These comparisons concern the available bounds, not a lower bound for the actual signed error: exceptional real alignment remains open.

For the entire rational function, the scalar prefactor obeys

    |U k2^j| <= 81920 |U|2^N.

The exact differential correction is

    K=U k2^j r[(r+1)(4w−10)²−(4w−6)Q(w)]/Q(w)^(r+2).

Its numerator degree is3, its denominator degree2r+4=N+O(1), its numerator coefficient height is O(|U|2^N r²), and its denominator coefficient height is at most25^(r+2). Its two finite-pole orders are r+2. The coefficient U disappears from the evaluated center only through the exact response-preserving formula (4); it is fully present in this written kernel cost.

## 5. Consequence and remaining question

The combined results prove a convergent e+pi family with a new permitted-pole correction and an exponential improvement of its actual primitive denominator. This improves the arithmetic rate constant by at least gamma in (7), rather than merely improving a convenient clearer. It does not produce a small primitive form, a nonvanishing lower bound for the true nearest error, or an irrationality proof. A stronger complete analytic error or a controlled exact combination that cancels the actual residual remains necessary.
