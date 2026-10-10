> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual logarithmic companion: prime support and endpoint content

New author research, 2026-10-01. Offline. The completed odd-gate and lifting papers are retained unchanged; none of their calculations is repeated. The main FINITE_MEASURE_COMPANION_TRANSFER_DRAFT.md has been read. Its external quantitative approximation input for pi remains pending source confirmation and is not used in the arithmetic proved here.

## 1. Definitions and outcome

Let n=4k, k>=1, m>=0, and define

    A(t)=1-2t+2t^2,
    C(t)=1-4t+2t^2,
    Bpoly(t)=A(t)^n C(t)^(2m),
    N=2n+4m, J=N-n=n+4m,
    K(t)=t^n Bpoly^(n)(t)/n!,
    U=K(1)!=0,
    T=calL((K-U)/(t-1)), beta=T/U,
    Bbeta=den(beta)>0.

Here calL(f)=integral from -1 to 1 of f((1+iu)/2) du. The integer polynomial K and the retained dyadic facts

    2^(n/2) divides U, v_2(T)>=1

are accepted from the existing coefficient/moment argument. No dyadic proof is repeated. The odd-prime arguments below apply at every nonzero U, without the special binary allocation. That allocation is used later to specify a nonzero-node parameter family.

For a positive integer a, let O_a be the lcm of the odd positive integers at most a. The first new deterministic bound is

    O_J T belongs to 2Z,
    Bbeta divides O_J |U|/2.                         (1)

Thus every odd prime-power denominator of T is bounded by J, rather than N. This statement concerns T before division by U. A prime canceled from the moment denominator can still enter Bbeta through U.

A second result gives an explicit congruence for every highest possible odd-prime denominator layer, and an exact two-stage content factorization of Bbeta. A third proves a surviving logarithmic pole for every admissible gap-one prime p=J-1. Unlike the corresponding gate for the complete center, that survival has no additional factorial-recurrence congruence.

## 2. Integration by parts shortens the denominator range

Put

    a_plus=(-1+i)/2, a_minus=(-1-i)/2,
    Bpoly(1+x)=sum_{h=0}^N c_h x^h.

All c_h are integers, and explicitly

    sum c_h x^h=(1+2x+2x^2)^n(1-2x^2)^(2m),
    c_n=U.                                          (2)

The endpoints t_plus=(1+i)/2 and t_minus=(1-i)/2 are roots of A(t). Hence Bpoly has a zero of order at least n at both integration endpoints. All boundary terms in n integrations by parts therefore vanish.

Since

    t^n/(1-t)=1/(1-t)-sum_{h=0}^{n-1}t^h,
    D^n(t^n/(1-t))=n!/(1-t)^(n+1),

and n is even, one obtains the exact identity

    calL(K/(1-t))=calL(Bpoly/(1-t)^(n+1)).           (3)

On the other hand, the definition of T gives

    calL(K/(1-t))=pi U-T.

Set x=t-1. Because n is even,

    Bpoly(t)/(1-t)^(n+1)
      =U/(1-t)-sum_{d=-n, d!=0}^J c_(n+d) x^(d-1).

Every nonlogarithmic summand has an elementary rational primitive. Since du=(2/i)dt, define, for every nonzero integer d,

    tau_d=(2/i)(a_plus^d-a_minus^d).

Integrating the preceding decomposition and comparing with (3) proves

    T=sum_{d=-n, d!=0}^J c_(n+d) tau_d/d.            (4)

No choice of logarithm branch is needed: the single logarithmic term was retained as U/(1-t), whose calL integral is pi U. Equation (4) is a rational identity, not a congruence or a truncated moment expression.

For d>0, tau_d belongs to Z[1/2]. For d<0 this follows even more strongly from

    a_plus^(-1)=-1-i, a_minus^(-1)=-1+i,

which makes tau_d integral. Conjugation shows all tau_d are rational. Consequently every odd denominator in (4) divides the odd part of some |d|<=J, because J>=n. This proves O_J T is integral at every odd prime. The retained bound v_2(T)>=1 then proves O_J T belongs to 2Z, establishing (1).

In particular, if an odd prime power p^e lies in (J,N], the extra possible factor at that level in O_N is absent from the denominator of T. If p>J, then T is p-integral. No conclusion that p is absent from Bbeta follows without considering v_p(U).

## 3. Exact separation of moment denominator and endpoint content

Define the integer

    Z_T=O_J T/2,
    g_T=gcd(O_J,|Z_T|),
    D_T=O_J/g_T,
    M_T=Z_T/g_T.

Then

    T=2M_T/D_T, gcd(D_T,|M_T|)=1,
    D_T=den(T),

where D_T is odd. These formulas also cover T=0 with g_T=O_J, D_T=1 and M_T=0.

Since U/2 is an integer, final rational reduction gives the exact factorization

    Bbeta=D_T (|U|/2)/gcd(|U|/2,|M_T|).             (5)

Indeed beta=M_T/[D_T(U/2)], and M_T is coprime to D_T. This separates two different cancellations:

1. g_T removes moment denominators before division by U.
2. gcd(|U|/2,|M_T|) removes endpoint content afterwards.

In particular, if T has an actual p-pole of order f>0, then M_T is a p-unit and

    v_p(Bbeta)=f+v_p(U).                            (6)

No part of that pole can cancel against U; dividing by U adds its valuation. Conversely, if T is p-integral, then

    v_p(Bbeta)=max(0,v_p(U)-v_p(T)).                 (7)

The dyadic identity is the same expression with p=2, and the retained bound gives v_2(Bbeta)<=v_2(U)-1. The present work does not assert a sharper universal dyadic equality.

Equivalently, direct reduction from the integer pair gives

    Bbeta=(O_J |U|/2)/gcd(O_J |U|/2,|Z_T|).

The two-stage version (5) is useful because it identifies exactly what canceled in T rather than conflating it with final endpoint cancellation.

## 4. Explicit highest-layer congruence at every odd prime

Fix an odd prime p<=J and put

    e=floor(log_p J), chi_p=(-1)^((p-1)/2).

All calculations in this section take place in Z_(p), or its residue field. The quadratic algebra Z_(p)[i] can be split or nonsplit; both a_plus and a_minus are units because their norm is 1/2.

Frobenius gives, for every integer a,

    tau_(a p^e)=chi_p^e tau_a modulo p.             (8)

For negative a the same identity holds because the endpoint elements are units. Define the finite signed index set

    I_p={a in Z: a!=0, -n<=a p^e<=J}.

Every a in I_p has |a|<p, so a is invertible modulo p. Multiplying (4) by p^e, terms whose denominator has smaller p-adic order vanish modulo p. The surviving terms give

    p^e T=S_p modulo p,
    S_p=chi_p^e sum_{a in I_p} c_(n+a p^e) tau_a/a. (9)

Equation (9) is a finite explicit condition for the actual family. The coefficients c_h come from the integer product (2); no determinant or coefficient-content unit is assumed. It retains both negative and positive exponents when p^e<=n.

For a coefficient-level finite-characteristic computation, if n=sum n_r p^r and 2m=sum m_r p^r are their base-p expansions, Frobenius gives

    sum c_h x^h
      =product_r (1+2x^(p^r)+2x^(2p^r))^(n_r)
                 (1-2x^(2p^r))^(m_r) modulo p.     (10)

This is an all-index expression. It does not assume that coefficient windows avoid carries: ordinary coefficient extraction from the entire finite product retains them.

The conclusions of (9) are precise:

* If S_p!=0, then v_p(T)=-e and v_p(Bbeta)=e+v_p(U).
* If S_p=0, then v_p(T)>=1-e; at least one factor p is removed from O_J in the denominator of T.

Define a deterministic integer from these tests,

    O_ref=product_{odd p<=J} p^(e_p-delta_p),
    e_p=floor(log_p J),
    delta_p=1 if S_p=0, and 0 otherwise.

Then

    O_ref T belongs to 2Z,
    Bbeta divides O_ref |U|/2.                      (11)

This is a proved support refinement, not a statement that its tests vanish for a positive density of primes. No prime scan was performed.

For higher depth put

    R_p=p^e T
       =sum_{d=-n, d!=0}^J c_(n+d) p^e tau_d/d.

Each summand is p-integral. If R_p!=0 and w_p=v_p(R_p), exact reduction is

    v_p(Bbeta)=max(0,e+v_p(U)-w_p).                 (12)

The remaining deciding congruence for absence of p from Bbeta is

    R_p=0 modulo p^(e+v_p(U)).                      (13)

A zero first layer only decides (13) when the required depth is one. All terms suppressed in (9) must be restored for a deeper lift. If T=0, Bbeta=1 and no valuation of a nonzero numerator is asserted.

## 5. The one-pole interval and a simpler coefficient condition

Now specialize to the previously studied interval

    max(n,N/2)<p<=J.

Then p>n, N<2p, and J<2p, so e=1 and I_p={1}. Since tau_1=2, equation (9) reduces to

    pT=2 chi_p c_(n+p) modulo p.                    (14)

This also identifies the earlier moment-pole expression exactly modulo p. If Bpoly(t)=sum b_j t^j, the retained expression was

    pT=2 chi_p Uhigh modulo p,
    Uhigh=sum_{j=p}^N binom(j,n)b_j.

Taylor translation and Lucas reduction give

    c_(n+p)=sum_{r=n}^{N-p} binom(p+r,p+n)b_(p+r)
           =sum_{r=n}^{N-p} binom(r,n)b_(p+r)
           =Uhigh modulo p.                        (15)

Terms with r<n in Uhigh vanish modulo p. Thus integration by parts turns the sum of high K coefficients into one translated Bpoly coefficient. Both formulas include the same logarithmic pole; neither involves the exponential numerator.

Set s=J-p and Ctop=2^(N/2). Since J is divisible by four, s is positive and odd. Reversing the translated product (2) gives the exact identity

    c_(n+p)=Ctop [x^s](1+x+x^2/2)^n(1-x^2/2)^(2m).

Here 2m=(p+s-n)/2. Because s<p, replacing this exponent by (s-n)/2 is valid for coefficients through degree s modulo p. Define the p-independent rational polynomial expression

    L_(n,s)=[x^s](1+x+x^2/2)^n
                         (1-x^2/2)^((s-n)/2).

Only a finite formal expansion is needed, and every binomial denominator involved has index at most s<p. Consequently

    pT=2 chi_p Ctop L_(n,s) modulo p.               (16)

This is the actual logarithmic companion test. It is distinct from the previously retained complete-center test involving D_j.

For fixed odd s, L_(n,s) is a polynomial in n over Q of degree at most s. It is divisible by n: at n=0 the formal series whose coefficient is extracted is even, so its odd coefficient vanishes. This divisibility is not itself a unit statement at primes p>n.

The simplest two examples, obtained by formal coefficient expansion, are

    L_(n,1)=n,
    L_(n,3)=n(2n^2+3n-11)/12.                       (17)

For the second expression, the coefficient of x^3 in (1+x+x^2/2)^n is (n^3-n)/6, and the remaining contribution is n(n-3)/4. These are algebraic identities, not a numerical residue scan. Their denominators are units on the stated interval for the corresponding gap.

If L_(n,s)!=0 modulo p, then

    v_p(T)=-1,
    v_p(Bbeta)=1+v_p(U).                            (18)

If L_(n,s)=0, then T is p-integral. When U is a p-unit this proves p does not divide Bbeta. When U is not a unit, the further cancellation needed is T=0 modulo p^(v_p(U)); equivalently pT=0 modulo p^(1+v_p(U)).

## 6. A compulsory logarithmic pole on an explicit parameter family

Take the gap-one slice

    p=J-1=n+4m-1,

and suppose its candidate p is prime. Then chi_p=-1 and the exact translated coefficient is

    c_(n+p)=c_(N-1)=n Ctop.

Indeed only the first quadratic factor in (2) contributes to the next-to-leading coefficient; its ratio to its leading coefficient is one, repeated n times. The second factor is even. Since p>n, equation (14) proves unconditionally on this prime slice

    pT=-2n Ctop modulo p !=0,
    v_p(T)=-1,
    v_p(Bbeta)=1+v_p(U).                            (19)

There is no remaining first-order congruence for survival of this logarithmic pole. The actual endpoint valuation is still present in (19).

To place the statement on the requested asymptotic allocation, fix rho>0. For each k>=1 let n=4k, let P_k be the least power of two strictly greater than k, and put

    m_k=P_k ceil((rho n log n+k)/P_k)-k,
    p_k=n+4m_k-1.

Then m_k=-k modulo P_k, m_k=rho n log n+O(n), and p_k=-1 modulo 4P_k. The retained binary nonvanishing result supplies U!=0. Whenever p_k is prime, m_k>=1 and

    p_k>N/2, p_k>n, p_k=J-1<=J,

so (19) applies. This is an explicit infinite family of parameter congruences and a compulsory pole theorem for every prime member. Infinitely many prime members are not proved or assumed.

This is an obstruction to a proposed universal cancellation of the large odd moment primes. It does not give an asymptotic lower bound for the product of those primes, because no unbounded supply of prime members is established.

The distinction from the complete center is concrete. The retained lifting paper already established, at (n,m,p)=(4,37,151), that U=6204 is a p-unit and p cancels from the complete center denominator q. Equation (19) now proves

    v_151(Bbeta)=1

at that same retained example. No calculation is repeated. Complete-center cancellation therefore cannot be used as evidence that the corresponding prime disappears from Bbeta.

## 7. Size of the deterministic refinement and transfer implications

For all admitted indices, (1) improves the earlier O_N |U|/2 bound by replacing O_N with O_J. The difference is an exact arithmetic refinement, but it does not by itself change the leading n log n rate under m~rho n log n.

More precisely,

    O_N/O_J divides binom(N,n).                     (20)

To prove this, J>=n and N=J+n<=2J. A prime can gain at most one power between O_J and O_N. If its new power p^a lies in (J,N], it exceeds both J and n, and the a-th term in the factorial valuation of binom(N,n) equals one. Every other floor-difference term is nonnegative. This proves the divisibility for each odd prime.

Hence

    0<=log(O_N/O_J)<=n log(eN/n)
                    =O_rho(n log log n)=o(n log n). (21)

Using only the inherited coarse bound O_J<=4^J and log|U|=o(n log n), equation (1) still gives

    limsup log Bbeta/(n log n)<=4rho log 4.

No improved leading constant is claimed from that replacement alone. A leading improvement from (11) would require a quantitative lower bound on

    sum_{odd p<=J, S_p=0} log p,

or a stronger estimate for the higher moment content g_T and the endpoint cancellation in (5). Such a bound is not proved here. The explicitly surviving gap-one primes show that these cancellations cannot be presumed universally.

The transfer draft needs an upper bound for this actual Bbeta, rather than the full-center denominator q or a coefficient clearer. Equations (5), (9), (11), and (13) supply that arithmetic interface. Any subsequent exclusion using a finite irrationality measure for pi remains conditional on the external theorem whose exact statement and source are still pending. This note asserts no such exclusion.

## 8. Remaining deciding congruences and status

The all-size proved results are the rational integration-by-parts formula (4), the denominator-range reduction (1), the two-stage actual content factorization (5), the highest-layer congruences (9)-(11), and the compulsory gap-one pole (19). These are author proofs, not an independent review.

For an arbitrary odd prime, the precise remaining local question is the valuation of the explicit p-integral rational number R_p=p^e T relative to e+v_p(U), as in (13). In the one-pole interval, its first test is the finite coefficient L_(n,s) modulo p; if it vanishes and U is not a unit, the full regular part of T must be lifted as well. For s=1 the first test is always nonzero, so only the independently determined endpoint valuation is needed to obtain the exact exponent in Bbeta.

No broad scan, old checker replay, numerical experiment, new external citation, or assertion about infinitely many primes in moving intervals was used. Earlier files are preserved. No irrationality or rationality conclusion about e+pi follows from this arithmetic package.
