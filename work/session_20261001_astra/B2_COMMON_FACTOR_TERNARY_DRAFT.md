> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Common-factor normalization and a ternary denominator theorem for b=2

Author: main agent. Status: paper proof draft, pending exact execution and independent review. No computational success is asserted by this document.

## Statement and domain

Consider the actual endpoint-matched degree-(n,2,n) construction for exp(z) and F(z)=4 arctan(z/(2-z)), with F(1)=pi. Let q_n be the positive denominator of the actual rational endpoint A(1)/B(1), reduced to lowest terms.

For n>=3 on the nonzero-endpoint domain, the proposed theorem is

    v_3(q_n)=2v_3(n!)+v_3(Dtilde_n)>=2v_3(n!).

More precisely, equality with 2v_3(n!) holds for n=0 or 2 modulo 3. For n=1 modulo 3, the bound is at least 2v_3(n!)+1. Eventual endpoint nonvanishing follows from the independently reviewed fixed-b theorem, used only at b=2.

This gives a uniform factorial contribution at one prime. Its exponential denominator contribution is log 3, below tau=2 log(1+sqrt(2)). It neither proves shrinking nor excludes the whole b=2 family, and does not settle rationality of e+pi.

## Sources and notation

The exact endpoint quotient and second-kind normalization come from:

- work/session_20260913/hp_b2_contiguous_endpoint_arithmetic.md, Sections 1–3;
- work/session_20260913/hp_b2_contiguous_endpoint_independent_review.md.

The state transition comes from:

- work/session_20260927/hp_b2_cubic_maximal_minor_gate.md, Section 2;
- work/session_20260927/hp_b2_cubic_maximal_minor_independent_review.md.

Only its polynomial identities are used here. Its large-prime local ideal theorem is not applied to small primes.

The partial-exponential Rodrigues contractions and their all-residue transfer come from:

- work/session_20260927/hp_b1_ternary_actual_denominator.md, Sections 1–2;
- work/session_20260927/hp_b1_prime_seed_transfer_and_closed_atlas.md, Section 2;
- work/session_20260927/hp_b1_uniform_5_13_independent_review.md.

Their polynomial functionals use the same n for both adjacent Legendre polynomials and therefore occur in the b=2 endpoint formula as well. This use does not transfer a b=1 denominator conclusion to b=2.

Throughout, K_j denotes the b=2 second derivative of x^j H_j(x) at x=1. It is not the b=1 quotient J_j/j. The new symbol k below is that quotient at the particular adjacent index, derived explicitly rather than identified by notation alone.

Put

    H_n(x)=n! [z^n] exp(xz)(1-z+z^2/2)^n,
    h=H_n(1), u=H'_n(1), v=H''_n(1),
    t=n+1, J=J_n=nh+u.

Let L_j(y) be the integer Legendre polynomial in the endpoint source, P_j=L_j(1), and

    w_P=calL((L_n(y)-P_n)/(y-1)),
    w_U=calL((L_(n+1)(y)-P_(n+1))/(y-1)),
    calL(g)=integral_(-1)^1 g((1+ix)/2) dx.

The letter t above is an integer index expression, not the variable of these polynomials.

## 1. An exact common factor

The accepted transition gives

    a=H_(n+1)(1)=-nh+nu+v/2,
    H'_(n+1)(1)=t(h-u+v/2),
    H''_(n+1)(1)=t(nh+u-(n+2)v/2).

Define

    k=(1-n)h+(n-1)u+v,
    ell=(-n^2+3n+2)h+(n^2-2n-1)u+nv.

Substitution into the derivative definitions proves

    J_(n+1)=t k,
    K_(n+1)=t ell.

Set

    sigma=t k^2-a ell,
    omega=kJ-ell h,
    C=(t k-a)J-t(ell-k)h.

The original b=2 source uses

    S=J_(n+1)^2-H_(n+1)K_(n+1),
    W=J_(n+1)J_n-K_(n+1)H_n.

Consequently S=t sigma and W=t omega, while its scalar C is exactly the C above.

All these quantities are integers. For completeness, the coefficient of x^(n-s) in H_n is (n)_s a_s(n), where a_s(n)=[z^s](1-z+z^2/2)^n. A term with c quadratic factors has denominator 2^c and s>=2c; the consecutive product (n)_s contains at least c even factors. Thus H_n has integer polynomial coefficients. In particular v/2 is integral. Integrality of a,k,ell,sigma,omega,C also follows from their displayed formulas.

Let Acal_n and Bcal_n denote the reviewed Rodrigues contractions, and put f=2^n/(n!)^2. The exact partial-exponential identities are

    T_P=f Acal_n,
    T_U=(2f/t) Bcal_n.

The full original numerator and denominator are

    Xcal=2(w_P+T_P)S-t^2(w_U+T_U)C-2f a W,
    Dcal=t^2 P_(n+1)C-2P_n S.

Define

    Vtilde=sigma Acal_n-C Bcal_n-a omega,
    Qtilde=2w_P sigma-t w_U C,
    Dtilde=t P_(n+1)C-2P_n sigma.

Direct substitution gives the exact rational identities

    Xcal=t(Qtilde+2f Vtilde),
    Dcal=t Dtilde.

Since t=n+1 is a nonzero ordinary integer, it can be cancelled over Q before any local reduction:

    X/Y=(Qtilde+2^(n+1)Vtilde/(n!)^2)/Dtilde.

This does not divide by a possibly nonunit t modulo a prime. The nonzero-endpoint domain Dcal!=0 is exactly Dtilde!=0. The second-kind part is retained in full. Dtilde is integral, and Vtilde belongs to Z[1/2].

## 2. Transfer of the normalized numerator at every odd prime

For j=0,1,2 the polynomial definition gives

    H_n^(j)(1)=sum_(s=0)^n (n)_s a_s(n) (n-s)_j,

where falling factorials of length zero equal 1. Terms with j>n-s vanish by the falling factorial; no negative factorial convention is required.

Fix an odd prime p and write n=mp+r, 0<=r<p. Terms with s>r vanish modulo p because (n)_s contains a factor p and a_s(n) has only powers of two in its denominator. For s<=r, Frobenius gives

    (1-z+z^2/2)^n
      ==(1-z+z^2/2)^r (1-z^p+z^(2p)/2)^m modulo p,

so its coefficient of z^s is the seed-r coefficient. The two falling factorial factors also reduce to their seed-r values. Hence

    (h_n,u_n,v_n)==(h_r,u_r,v_r) modulo p.

Together with the previously proved transfer of Acal_n and Bcal_n, all polynomial expressions defining Vtilde transfer:

    Vtilde_n==Vtilde_r modulo p.

The expression uses division by 2 only, so this proof includes r=p-1. It needs no division by n+1. This is a new transfer statement for the normalized numerator, not the original V=t Vtilde.

## 3. Three exact seeds

The following are hand-derived exact scalar values, awaiting a saved exact checker:

| r | h | u | v | Acal | Bcal | a | k | ell | sigma | C | omega | Vtilde |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 | 1 | 3 | 0 | 1 | 2 | 1 | -1 | -2 | 4 |
| 1 | 0 | 1 | 0 | 3 | 10 | 1 | 0 | -2 | 2 | -1 | 0 | 16 |
| 2 | 1 | -2 | 2 | 21 | 133 | -5 | -1 | 10 | 53 | -33 | -10 | 5452 |

Each last-column entry is 1 modulo 3. The transfer theorem therefore proves

    Vtilde_n==1 modulo 3 for every integer n>=0.

The indices 0 and 1 here define finite scalar contractions, not actual degree-(n,2,n) approximants. Their use in the transfer does not assert existence of those small approximants.

The unnormalized V has seed values 4,32,16356, respectively. Its vanishing at residue -1 modulo 3 is therefore a consequence of the removed factor n+1, and must not be confused with vanishing of Vtilde.

## 4. Second-kind bound and actual rational reduction

For j>=0, direct integration gives the rational moment

    mu_j=calL(y^j)
        =((1+i)^(j+1)-(1-i)^(j+1))/(i 2^j(j+1)).

Its numerator after division by i is an integer. Thus, for an odd prime p,

    v_p(mu_j)>=-v_p(j+1).

The polynomials (L_n-P_n)/(y-1) and (L_(n+1)-P_(n+1))/(y-1) have integer coefficients and degrees at most n-1 and n. Consequently

    v_p(w_P), v_p(w_U)>=-floor(log_p(n+1)),
    v_p(Qtilde)>=-floor(log_p(n+1)).

The latter follows from integrality of sigma,t,C, not from a claim that the moments themselves are integers.

For every odd p and n>=p,

    2v_p(n!)>floor(log_p(n+1)).

To see this, put L=floor(log_p(n+1)). If L=1, v_p(n!)>=1. If L>=2, then n>=p^L-1 and

    2v_p(n!)>=2(p^(L-1)-1)>L.

At p=3 the numerator Vtilde is a unit for every index. Therefore for n>=3 its factorial term has valuation -2v_3(n!), strictly less than that of Qtilde. There is a unique least-valuation term, so

    v_3(Qtilde+2^(n+1)Vtilde/(n!)^2)=-2v_3(n!).

On Dtilde!=0 the actual reduced denominator is thus

    v_3(q_n)=max(0,v_3(Dtilde)+2v_3(n!))
            =v_3(Dtilde)+2v_3(n!).

This includes the final rational reduction and all numerator cancellation. No coefficient clearer is substituted for q_n.

More generally, the same argument proves a useful conditional criterion for every odd p: if n>=p, Dtilde_n!=0, and Vtilde_(n mod p) is a p-unit, then

    v_p(q_n)=2v_p(n!)+v_p(Dtilde_n)>=2v_p(n!).

Any extension using that criterion must establish its complete seed conditions and handle zero seeds separately.

## 5. The exact ternary residue refinement

The integer Legendre endpoints have generating function

    G(z)=sum_(n>=0)P_n z^n=(1-4z-4z^2)^(-1/2).

For instance this follows from their defining Legendre generating function after the stated change of variable. Work in F_3[[z]] and put A(z)=1-z-z^2. Then A(z)G(z)^2=1 and Frobenius gives G(z)^3=G(z^3). Multiplication yields

    G(z)=A(z)G(z^3).

Comparing coefficients gives

    P_(3m)=P_m,
    P_(3m+1)=2P_m,
    P_(3m+2)=2P_m modulo 3.

Since P_0=1, every P_m is a ternary unit. The seed values of sigma and C, combined with the normalized denominator formula, now give

    Dtilde_(3m)==2P_m,
    Dtilde_(3m+1)==0,
    Dtilde_(3m+2)==P_m modulo 3.

Thus Dtilde is a unit on residues 0 and 2, giving equality v_3(q_n)=2v_3(n!). On residue 1, a nonzero Dtilde has valuation at least one, giving the stated stronger lower bound.

No all-depth formula for Dtilde on residue 1 is proved here.

## 6. Review requirements and limits

The independent reviewer should check the transition-derived factors, exact quotient cancellation, original factorial indices, seed arithmetic, coefficientwise transfer at residue p-1, moment denominator bound, strict valuation separation, endpoint domain, and the Legendre generating-function reduction. Exact computation should verify identities and complete finite seeds, without being presented as an infinite-index proof by itself.

The current proof uses the inherited endpoint formula and analytic nonvanishing theorem in their established scopes. No large-prime gcd theorem is imported at p=3. No growing-b analytic theorem or estimate for irrationality is asserted.
