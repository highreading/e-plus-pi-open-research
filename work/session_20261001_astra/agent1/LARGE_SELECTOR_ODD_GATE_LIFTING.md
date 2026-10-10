> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Large-selector odd gate: algebraic reduction and first-depth lifting

New author research, 2026-10-01. Offline. The completed LARGE_SELECTOR_ODD_ARITHMETIC.md is retained unchanged. Its complete numerator identity is the starting point, not an object of independent review. One new, algebraically selected cancellation example was checked exactly; no prime scan or previous checker was replayed.

## 1. Definitions and retained complete normalization

Let n=4k, k>=1. Let P be a power of two with k<P<=2k, and take m>=0 satisfying m=-k modulo P. The main large-selector author theorem supplies U!=0 on this allocation. Put

    N=2n+4m, J=n+4m,
    B(t)=(1-2t+2t^2)^n(1-4t+2t^2)^(2m)=sum_j b_j t^j,
    K(t)=sum_{j=n}^N binom(j,n)b_j t^j,
    U=K(1), L=calL((K-U)/(t-1)).

Let D_0=1 and D_j=jD_(j-1)+1. The complete rational center and its positive reduced denominator are

    c=W/(n!J!U), q=den(c),
    W=Vexp+n!J!L,
    Vexp=sum_{j=n}^N b_j (J)_(N-j) D_j.

Fix an odd prime

    max(n,N/2)<p<=J,
    s=J-p, R=N-p=n+s<p.

Since J is divisible by four and p is odd, s is necessarily positive and odd. In particular s=0 never occurs in this allocated family. Write

    chi=(-1)^((p-1)/2), Ctop=2^(N/2).

The retained complete gate is

    W = s! sum_{r=n}^{n+s} b_(p+r)
                    (D_r-2 chi r!)/(r-n)! modulo p.       (1)

The term -2 chi r! is the logarithmic moment contribution. Indeed the only moment with a possible p-pole is mu_(p-1), and p mu_(p-1)=2 chi modulo p. Thus W is p-integral, even though L need not be.

With u=v_p(U), exact final reduction gives

    v_p(q)=max(0,1+u-v_p(W)),                            (2)

using v_p(0)=infinity and interpreting W=0 as q=1. The actual endpoint valuation u is never replaced by zero without a separate test.

## 2. Algebraic reduction for every odd terminal gap

This reduction removes m from the residual coefficient condition once n and s are fixed. Define

    Qrev(t)=1-t+t^2/2,
    Crev(t)=1-2t+t^2/2,
    a_h(n,s)=[t^h] Qrev(t)^n Crev(t)^((s-n)/2),
    chi_s=(-1)^((s+1)/2).

The fractional power is the formal expansion with constant term one. Only h<=s is used. These coefficients are rational and p-integral because their binomial denominators involve only 2 and factorials with indices at most s<p.

Reciprocity gives exactly

    b_(p+n+s-h)=Ctop [t^h]Qrev(t)^n Crev(t)^(2m).

But 2m=(p+s-n)/2. For h<=s<p, the coefficient of degree h is a polynomial in the exponent with p-integral coefficients. Therefore

    [t^h]Qrev^n Crev^(2m)=a_h(n,s) modulo p.

Also p=-s modulo four, so chi=chi_s. Consequently the complete gate reduces to

    W=Ctop G_(n,s) modulo p,                            (3)

where the p-independent rational number is explicitly

    G_(n,s)=s! sum_{h=0}^s a_h(n,s)
        (D_(n+s-h)-2 chi_s (n+s-h)!)/(s-h)!.             (4)

Every denominator used in this congruence is a p-unit. Formula (4) concerns the complete rational numerator; dropping its logarithmic term changes the condition.

Thus G_(n,s)!=0 modulo p proves v_p(q)=1+v_p(U). This is an all-index reduction, not a residue table. It is especially short when the prime lies a fixed distance below J.

## 3. The gap-one family and its exact additional congruence

Now impose

    p=J-1=n+4m-1.

Then s=1, N=p+n+1, chi=-1, and p>n+1 whenever m>=1. The two reverse coefficients are

    a_0(n,1)=1, a_1(n,1)=-1.

Using D_(n+1)=(n+1)D_n+1 in (4) yields the integer

    F_n=nD_n+2n n!+1,
    W=Ctop F_n modulo p.                              (5)

Equivalently, the only high coefficients needed at first order are

    b_N=Ctop, b_(N-1)=-(p+1)Ctop.

The logarithmic term supplies the summand 2n n! in F_n. In particular the exponential-only congruence nD_n+1 is not the complete gate.

The survival statement is exact:

* If p does not divide F_n, then v_p(q)=1+v_p(U).
* If p divides F_n and U is a p-unit, then v_p(q)=0.
* If p divides both F_n and U, the first residue alone is insufficient; the first lift below determines the next obstruction.

Since n! is a p-unit, the additional congruence can also be written

    D_n/n! != -2-1/(n n!) modulo p.

All divisions here are legal because p>n. There is no claim that this congruence holds universally.

## 4. Explicit infinite parameter family and its prime qualification

Fix any real rho>0. For every k>=1 put n=4k, let P_k be the least power of two strictly greater than k, and define

    ell_k=ceil((rho n log n+k)/P_k),
    m_k=P_k ell_k-k,
    p_k=n+4m_k-1=4P_k ell_k-1.

Then

    m_k=-k modulo P_k,
    rho n log n<=m_k<rho n log n+P_k,
    m_k=rho n log n+O(n),
    p_k=-1 modulo 4P_k.

These are infinitely many explicit parameter triples with unbounded n. Whenever p_k is prime, it satisfies the required interval:

    p_k>n, p_k>N/2, p_k=J-1<=J.

Indeed p_k-N/2=2m_k-1>0. Equations (5) and the lifting theorem below apply at every such prime candidate.

This is an infinite family of parameter congruences and a theorem conditional on primality of its candidate. It does NOT prove that infinitely many p_k are prime, that every moving interval contains such a prime, or that infinitely many candidates satisfy p_k not dividing F_n. No prime-distribution theorem is being invoked.

The same construction with a fixed positive odd gap s and p_k=J-s eventually lies in the interval and is governed by (4), with p_k=-s modulo 4P_k. The detailed lift here is for s=1.

## 5. First-depth expansion of the actual endpoint

Continue with p=J-1. The retained endpoint representation is

    U=[x^n](1+2x+2x^2)^n(1-2x^2)^(2m).

Define p-independent rational coefficients

    e0=(1-n)/2,
    Aend_n=[x^n](1+2x+2x^2)^n(1-2x^2)^e0,
    Bend_n=(1/2)[x^n](1+2x+2x^2)^n
                        (1-2x^2)^e0 log(1-2x^2).

Here log(1-2x^2)=-sum_{h>=1}2^h x^(2h)/h. All coefficients needed have indices h<=n/2<p, so their denominators are p-units.

Since 2m=e0+p/2, Taylor expansion in the exponent, truncated at degree n in x, proves

    U=Aend_n+p Bend_n modulo p^2.                     (6)

A direct justification without infinite p-adic analytic assumptions is to write each required coefficient using binom(e,h), h<=n/2. It is a polynomial in e with denominator h!, a p-unit. Its Taylor remainder after replacing e by e0+p/2 is divisible by p^2. Differentiation in e produces exactly the logarithm above.

Thus:

* If Aend_n!=0 modulo p, then u=0.
* If Aend_n=0 modulo p and

      Omega_(n,p)=Aend_n/p+Bend_n !=0 modulo p,

  then u=1.
* If both quantities vanish, u>=2 and the endpoint itself needs a further lift.

The quotient Aend_n/p is formed over Q only after its numerator is known to be divisible by p in Z_(p). It is not modular inversion of p. The author allocation still guarantees U!=0 over Q, so its actual valuation is finite.

## 6. First-depth expansion of the complete numerator

All definitions in this section are exact rational or integer quantities before reduction. Put

    Uhigh=sum_{j=p}^N binom(j,n)b_j,
    H1=(Uhigh-n Ctop)/p,
    wp=((p-1)!+1)/p,
    Mp=p mu_(p-1), epsp=(Mp+2)/p,
    Lreg=L-mu_(p-1)Uhigh.

Here wp is integral by Wilson's theorem. Lucas reduction and the two top coefficients give Uhigh=n Ctop modulo p, so H1 is integral. Since chi=-1, Mp=-2 modulo p and epsp is p-integral. Finally Lreg is p-integral because the unique moment pole has been removed.

Define

    En=n! (D_(p-1)+sum_{v=1}^n D_(v-1)/v!),
    Slow=sum_{j=n}^{p+n-1} b_j D_j/(j-n)!.

Every factorial denominator in these expressions is below p. Define the complete first-order coefficient

    Xi = Ctop (n En-D_n)
       + n! [2H1+n Ctop(2-2wp-epsp)]
       - Slow-n! Lreg.                               (7)

Then the all-index first lift is

    W=Ctop F_n+p Xi modulo p^2.                      (8)

In particular Xi retains the moment-pole correction epsp, the regular logarithmic part Lreg, the Wilson quotient, and all exponential terms previously suppressed by one factorial p.

### Proof of (8)

The recurrence restart gives D_p=1+pD_(p-1). Induction in 0<=r<=n gives

    D_(p+n)=D_n+p En modulo p^2.

Indeed the first-order coefficients satisfy E_0=D_(p-1) and E_r=D_(r-1)+r E_(r-1), whose explicit solution is the displayed En.

The two top terms of Vexp combine EXACTLY as

    Ctop[D_(p+n+1)-(p+1)^2 D_(p+n)]
      =Ctop[(n-p-p^2)D_(p+n)+1].

Their expansion is Ctop(nD_n+1)+p Ctop(nEn-D_n) modulo p^2. Every remaining term has j<=p+n-1 and equals J! b_j D_j/(j-n)!. Since J=p+1,

    J!/p=(p+1)(p-1)!=-1+p(wp-1) modulo p^2.

Their combined contribution is therefore -p Slow modulo p^2.

For the logarithmic part use the exact identity

    n!J!L=n!(J!/p)Mp Uhigh+p n!(J!/p)Lreg.

Substitute

    Mp=-2+p epsp,
    Uhigh=n Ctop+pH1,
    J!/p=-1+p(wp-1) modulo p^2.

The result is

    2n n! Ctop
      +p n![2H1+n Ctop(2-2wp-epsp)-Lreg]
      modulo p^2.

Adding the complete exponential expression proves (8). No term with a possible contribution at order p has been discarded.

For a shorter explicit computation of H1 modulo p, let H_n=sum_{v=1}^n 1/v. Expansion of the two upper binomial coefficients and of those crossing p gives

    H1=Ctop(n H_n-n-1)
        +sum_{r=0}^{n-1}
          (-1)^(n-1-r) r!(n-1-r)! b_(p+r)/n!
        modulo p.                                    (9)

Indeed binom(p+r,n)/p has the displayed coefficient for r<n; binom(p+n,n)=1+pH_n and binom(p+n+1,n)=(n+1)(1+p(H_(n+1)-1)) modulo p^2. Formula (9) has only n additional coefficients and p-unit denominators. It is an optional algebraic simplification, not a further numerical check.

## 7. Exact lifting and surviving-prime cases

Suppose p divides F_n and set

    Theta_(n,m,p)=Ctop(F_n/p)+Xi modulo p.             (10)

Equation (8) proves W/p=Theta modulo p. This is a complete first-depth obstruction:

* If Theta!=0, then v_p(W)=1 and v_p(q)=u.
* If Theta=0, then v_p(W)>=2 and

      v_p(q)<=max(0,u-1).

  In particular p cancels entirely when u<=1.

Combining this with (6) gives an explicit first-depth surviving family of conditions:

    p divides F_n,
    Aend_n=0 modulo p,
    Omega_(n,p)!=0 modulo p,
    Theta_(n,m,p)!=0 modulo p

implies

    v_p(U)=1, v_p(W)=1, v_p(q)=1.                    (11)

Thus a zero first gate does not automatically cancel p when the endpoint also vanishes. Conversely, if Aend_n is a unit and p divides F_n, p cancels regardless of Theta. These are local theorems for every admissible parameter, not assertions that the listed congruence classes are populated infinitely often.

If both endpoint and numerator first lifts vanish, the next exact problem is to compare their higher orders in

    U=[x^n](1+2x+2x^2)^n(1-2x^2)^(2m),
    W=Vexp+n!(J!/p)(pL).

All regular moments and suppressed exponential terms must again be retained. Formula (2), rather than separate numerator valuations, governs final survival. This note supplies no universal bound on those higher orders.

## 8. One algebraically selected cancellation witness

The gate was reduced before selecting this example. At n=4,

    D_4=65,
    F_4=4*65+8*24+1=453=3*151.

The factor p=151 satisfies p>n+1. Set m=(151+1-4)/4=37. With k=1 and P=2, the required dyadic congruence is satisfied. Also N=156, J=152, and 151 lies strictly above N/2=78.

The endpoint has the exact formula

    U_(4,m)=8m^2-132m+136,
    U_(4,(p-3)/4)=p^2/2-36p+479/2.

Hence U=6204=13 modulo 151, so u=0. Equation (5) already proves v_151(q)=0: the compulsory factorial prime cancels. This disproves universal first-order survival on the gap-one slice. It does not disprove eventual survival on an asymptotic sequence.

The single new exact execution additionally verified

    Aend_4=479/2, Bend_4=-36,
    Theta=28 modulo 151,
    v_151(W)=1,
    v_151(q)=0.

It independently formed B, the complete rational moment sum, Vexp, U, and the reduced rational denominator. It checked (8) modulo p^2 and (6) modulo p^2. The controller returned exit code zero and status PASS_SINGLE_NEW_GATE_AND_FIRST_LIFT_WITNESS.

Artifacts:

    work/session_20261001_astra/agent1/check_large_selector_odd_gate_lifting.py
    work/session_20261001_astra/agent1/large_selector_odd_gate_lifting_check.json

This is finite exact evidence for one new witness and the implemented identities. The all-index conclusions rest on the proofs above. The script was not rerun.

For a literal membership example in the parameter family of Section 4, choose rho=37/(4 log 4). Its k=1 member is precisely m=37 and p=151. No conclusion about later prime candidates follows from that finite member.

## 9. Outcome and remaining scope

The new results are the p-independent short-window gate (4), its gap-one integer reduction F_n, the explicit parameter congruences with m~rho n log n, the endpoint lift (6), and the complete numerator lift (8). Equations (10)-(11) specify the first higher-depth obstruction while retaining the actual U valuation and the logarithmic pole.

Universal survival fails, as the new exact example shows. A universal or eventual nonvanishing theorem for F_n modulo the moving prime candidates is not proved. Nor is there a theorem producing infinitely many primes in this parameter family. No asymptotic product of surviving primes, complete-error estimate, or irrationality conclusion is claimed. The existing dyadic theorem and earlier odd-arithmetic proof are preserved without audit or modification.
