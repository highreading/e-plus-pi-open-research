> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Canonical overlap deficit report

Original author research for the SAME b=3,m=1 factorial B-only Gram center. The interrupted derivation is now submitted for saving. No seed, modulo-121 transfer, old read-back, or completed calculation is repeated. This is not an independent review.

The total deficit remains

    delta=B/gcd(q,B),
    q=den(alpha+gamma), B=den(gamma), gamma=kappa+beta.

Using the retained integers and a uniform valid moment clearer L=2^(2n+1)lcm(1,...,2n+2), the exact complete numerator is

    Psi=L(Acal+d0 Delta x_0)+F d0 Tlog,
    F=(n!)^2, d0=(n+1)(n+2).

The original final-gcd formula is

    delta=gcd(F d0 L Dg,|Psi|)
       /gcd(F d0 L Dg,|L Acal|,|d0(L Delta x_0+F Tlog)|).

The endpoint and logarithmic terms are both retained.

The main structural advance reduces the actual forcing to the primitive pair w=(P_n,P_(n+1))/gcd(P_n,P_(n+1)). Its reconstructed Gram contraction becomes a positive definite integral binary form Bform. After removing common row content and the FINAL evaluated numerator gcd, the note constructs exact integers D2,U,V with

    gcd(D2,U,V)=1,
    Wcancel=U+V,
    delta=gcd(D2,|Wcancel|).

Every prime lost from the overlap has U,V both units. Its depth is exactly min(v_p(D2),v_p(Wcancel)).

Write Bform=a_B Bprim with primitive positive form Bprim, and write the normalized sum row as c_H(H0,H1), where gcd(H0,H1)=1. The explicit resultant

    Rres=Bprim(-H1,H0)>0

is nonzero by Gram positivity. With t0=gcd(P_n,P_(n+1)), the proved factorization is

    delta_F=gcd(F,D2,|Wcancel|),
    delta_exc=delta/delta_F,
    delta_exc divides d0 L t0 a_B c_H Rres.

The two factors need not be coprime. More sharply, delta_exc divides the gcd of that exceptional product with Wcancel. Since log(d0 L t0)=O(n),

    log delta<=log gcd(F,D2,|Wcancel|)
                         +log(a_B c_H Rres)+O(n).

This controls excess cancellation beyond factorial multiplicities by explicit contents and a positive resultant. It does not prove either remaining term is subfactorial. The resultant varies with the actual recurrence data; positivity does not control its size.

A complementary perturbation lemma compares delta with the deficit delta0 for alpha+kappa:

    |v_p(delta)-v_p(delta0)|<=v_p(den(beta)).

Outside primes dividing Dg, the total discrepancy is at most log L=O(n). Thus those primes reduce to the endpoint-corrected numerator Acal+d0 Delta x_0. At Gram primes the complete Wcancel remains necessary.

The precise sufficient global conditions are subfactorial bounds for

    gcd(F,D2,|Wcancel|)

and

    gcd(d0 L t0 a_B c_H Rres,|Wcancel|).

Neither bound is established. The retained single lost 11 factor supplies no global estimate.

The main's newly reported joint budget follows directly from the exact identity

    lcm(q,B)=lcm(Q,B)=q delta, Q=den(alpha).

Factorial exponential accuracy and the retained e approximation inequality imply

    liminf (log q+log delta)/(n log n)>=1/2.

This requires no complete-error premise or pi input. If log delta=o(n log n) were proved, it would force liminf log q/(n log n)>=1/2 and exclude geometric q. The deficit hypothesis is still unproved.

For the complete overlap transfer, the sufficient rate condition remains

    mu limsup(log B/(n log n))
       +limsup(log delta/(n log n))<1/2.

Hence the strict threshold 5/72 is available with subfactorial deficit and the corresponding strict B-rate bound, using admissible pi exponents approaching the confirmed published bound 36/5. Neither global condition is claimed.

The strongest completed mathematics is the exact normalized-numerator reduction, perturbation bound, positive-resultant factorization, and their explicit unresolved arithmetic conditions. Both new files require application-confirmed saving and read-back before operational completion is reported.
