> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Complete normalized b=2 prime seeds

Status: exact computations PASS; paper deductions below are not independently reviewed. The main-agent ternary theorem is undergoing a separate review; this document does not assign it a review outcome.

The closed prime list for this assignment is exactly 5,7,11,13. All 36 residue entries were computed by two exact constructions, using the 13 distinct scalar seeds 0 through 12. These are scalar seed calculations, not a canonical HP degree sweep. No additional prime or lifted-index calculation was performed.

## Exact normalization and endpoint domain

Use the original b=2 endpoint notation, with t=n+1, f=2^n/(n!)^2, h=H_n(1), u=H'_n(1), v=H''_n(1), J=nh+u. Define

    a=-nh+nu+v/2,
    k=(1-n)h+(n-1)u+v,
    ell=(-n^2+3n+2)h+(n^2-2n-1)u+nv,
    sigma=t k^2-a ell,
    omega=kJ-ell h,
    C=(t k-a)J-t(ell-k)h.

Here K_j remains the b=2 second derivative of x^j H_j(x). The lower-case k is a separately defined scalar.

The accepted polynomial state transition gives

    H_(n+1)=a,
    H'_(n+1)=t(h-u+v/2),
    H''_(n+1)=t(nh+u-(n+2)v/2).

Substitution into the derivative definitions proves J_(n+1)=t k and K_(n+1)=t ell. Consequently the original minors satisfy the exact identities

    S=t sigma, W=t omega,
    C=(J_(n+1)-H_(n+1))J_n-(K_(n+1)-J_(n+1))H_n.

These are polynomial identities, not inferred divisibilities at a residue. The polynomial H_n has integer coefficients: a term involving c quadratic factors in [z^s](1-z+z^2/2)^n has denominator dividing 2^c and s>=2c, while the consecutive product (n)_s contains at least c even factors. Its second derivative at 1 is even. Thus a,k,ell,sigma,omega,C are integers.

Write Acal_n and Bcal_n for the original Rodrigues contractions, so T_P=f Acal_n and T_U=2f Bcal_n/t. Define

    Vtilde=sigma Acal_n-C Bcal_n-a omega,
    Qtilde=2w_P sigma-t w_U C,
    Dtilde=t P_(n+1)C-2P_n sigma.

The original complete endpoint expression is

    Xcal=2(w_P+T_P)S-t^2(w_U+T_U)C-2f a W,
    Dcal=t^2 P_(n+1)C-2P_n S.

Substituting the exact factors and contractions gives

    Xcal=t(Qtilde+2f Vtilde),
    Dcal=t Dtilde,
    V=t Vtilde,

where V=S Acal_n-t C Bcal_n-a W is Agent 1's ORIGINAL scalar. It is not Vtilde. Since t is a nonzero ordinary integer, cancellation over Q proves

    X/Y=(Qtilde+2^(n+1)Vtilde/(n!)^2)/Dtilde.

This cancellation precedes local reduction and does not invert t modulo p. Dtilde is integral and Vtilde belongs to Z[1/2]. Every actual endpoint or q statement assumes n>=2 and Dtilde!=0, equivalently Dcal!=0 and Y!=0. Eventual nonvanishing is inherited from the reviewed fixed-b theorem. Seeds 0 and 1 are finite scalar definitions, not assertions about actual approximants at those degrees.

The checker verifies eight formal identities, including both complete endpoint factors and V=t Vtilde. Its second exact construction also checks the source's rational-minor endpoint formula (5), including the second-kind Wronskian, at every seed in the source domain 2 through 12. It compares actual quotients whenever Dtilde is nonzero.

## Transfer proof, including the prime-block boundary

Let a_s(n)=[z^s](1-z+z^2/2)^n and D_j=j! E_j. For d=0,1,2,

    H_n^(d)(1)=sum_(s=0)^(n-d) (n)_(s+d) a_s(n),

with empty sums zero. If n=mp+r, 0<=r<p, all terms with s+d>r vanish modulo an odd p. In the remaining terms s<p, Frobenius transfers a_s(n) to a_s(r), and the falling factorial transfers as well. Thus h,u,v transfer at every residue.

The exact contractions are

    Acal_n=sum_(s=0)^n (n)_s a_s(n)D_(2n-s),
    Bcal_n=2D_(2n+1)
      +sum_(s=1)^(n+1) (n)_(s-1)(2n+2-s)a_s(n+1)D_(2n+1-s).

The recurrence D_0=1, D_j=jD_(j-1)+1 proves D_j=D_(j mod p) modulo p. Only s<=r survives in Acal. For Bcal, when r<=p-2 only s<=r+1<p survives. These terms transfer directly. When r=p-1, terms s>=p+1 vanish through their falling factorial; terms 1<=s<p vanish by Frobenius for a_s(n+1); the s=p term vanishes through 2n+2-s. Only 2D_(2n+1) remains, identically to the seed computation. No division by n+1 is used.

Every displayed normalized scalar is a polynomial over Z[1/2] in n,h,u,v,Acal,Bcal. Hence

    Vtilde_n=Vtilde_(n mod p) modulo p

for every odd p and n>=0. This proof, not a finite sample of lifts, justifies all-index use of the seed table.

## Complete exact seed table

Entries are ordered by r=0,...,p-1.

| p | Vtilde residues modulo p | Zero residues | Uniform unit seeds |
|---|---|---|---|
| 5 | 4,1,2,2,0 | {4} | No |
| 7 | 4,2,6,4,4,6,3 | none | Yes |
| 11 | 4,5,7,8,3,4,2,7,2,5,5 | none | Yes |
| 13 | 4,3,5,9,7,10,9,8,11,2,12,6,2 | none | Yes |

Construction 1 uses exact Rodrigues tail sums for h,u,v,Acal,Bcal and the polynomial normalized expressions. Construction 2 generates integer Legendre polynomials by their three-term recurrence and applies rational factorial and exponential-partial-sum functionals directly. It obtains sigma=S/(r+1), omega=W/(r+1), and Vtilde=V/(r+1) over Q before reducing modulo p. Thus even the boundary seed is computed without modular division by zero. Every state coordinate, not only Vtilde, agrees between the constructions.

The certificate stores all exact seed states, original and normalized endpoint scalars, and all 36 modular state rows. Both methods share the mathematical definitions but use different computational constructions; their agreement is not independent researcher review.

## Second-kind separation and actual denominator consequence

The integer polynomial (L_k(y)-P_k)/(y-1) has degree at most k-1. Its moment functional has

    calL(y^j)=((1+i)^(j+1)-(1-i)^(j+1))/(i 2^j(j+1)).

The numerator after division by i is an integer. For odd p the moment valuation is at least -v_p(j+1). Therefore, with L=floor(log_p(n+1)),

    v_p(w_P), v_p(w_U)>=-L,
    v_p(Qtilde)>=-L.

For n>=p, F=v_p(n!) satisfies 2F>L. Indeed if L=1 then F>=1; if L>=2 then n>=p^L-1, and 2F>=2(p^(L-1)-1)>L. Thus the scaled second-kind term

    Rsecond=(n!)^2 Qtilde/2^(n+1)

has valuation at least 2F-L>=1. Put

    R=Vtilde+Rsecond.

If the seed is a unit, v_p(R)=0 and the complete normalized numerator has valuation -2F. Exact rational reduction gives

    v_p(q_n)=2v_p(n!)+v_p(Dtilde_n)>=2v_p(n!).

This holds for each p=7,11,13, for every n>=p on the nonzero-endpoint domain, with no residue exception. For p=5 it holds on residues 0,1,2,3 when n>=5. Legendre-unit assumptions are unnecessary in this unit-numerator argument: any positive depth of the nonzero Dtilde increases q's exponent.

For n>=13 on the same domain, the three uniform contributions may be multiplied:

    7^(2v_7(n!)) 11^(2v_11(n!)) 13^(2v_13(n!)) divides q_n.

No claim concerning all primes or a global resolution follows. The finite seeds require the transfer and separation proofs above to yield these infinite-index statements.

## The sole normalized zero: p=5, r=4

The complete residue state is

    (h,u,v,J,Acal,Bcal,a,k,ell,sigma,C,omega)
       =(0,3,3,3,3,0,1,2,3,2,2,1) modulo 5.

Consequently Vtilde=2*3-2*0-1*1=0 modulo 5, while

    Dtilde=(n+1)P_(n+1)C-2P_n sigma=P_n modulo 5.

To determine the actual denominator residue, use the Legendre generating function

    G(z)=sum P_n z^n=(1-4z-4z^2)^(-1/2).

In F_5[[z]], set A(z)=1-4z-4z^2. The identities A G^2=1 and G(z)^5=G(z^5) imply

    G(z)=A(z)^2 G(z^5).

The degree-four factor is

    A(z)^2=1+2z+3z^2+2z^3+z^4 modulo 5.

Coefficient comparison proves P_(5m+r)=b_r P_m modulo 5 with (b_0,...,b_4)=(1,2,3,2,1). Every digit factor is nonzero; induction on the base-five digits proves P_n is a unit for every n. Hence

    v_5(Dtilde_n)=0 whenever n=4 modulo 5.

This also proves endpoint nonvanishing on this residue class for n>=2. The result follows from the generating-function proof; the residual checker only verifies its finite digit polynomial and the already computed residue state.

The zero is therefore a cancellation within the complete normalized factorial scalar, not an uncancelled common n+1 factor in the normalized numerator and denominator. There is no further common factor of positive 5-adic valuation in Dtilde that could remove it while keeping the denominator quotient locally integral. This assertion does not deny factorial clearing and subsequent rational cancellation: that cancellation is measured by R below. No additional exact factor is cancelled.

For example, the already computed exact seed r=4 has Vtilde=17169002260 and Dtilde=-350897184, the latter a unit modulo 5. This finite value is not used to infer the depth at other indices.

## Precise remaining depth question

In general, on Dtilde!=0, let d=v_p(Dtilde) and F=v_p(n!). For R!=0 the exact joint formula is

    v_p(q_n)=max(0,2F+d-v_p(R)),
    R=Vtilde+(n!)^2 Qtilde/2^(n+1).

If R=0, the rational endpoint is zero and q_n=1. This formula retains the complete second-kind term, all factorial losses, and final rational reduction.

For n=4 modulo 5 with n>=5 (thus n>=9), the denominator result makes d=0. The open problem is therefore to control

    v_5(Vtilde_n+(n!)^2 Qtilde_n/2^(n+1)).

Both summands together give R=0 modulo 5; the seed calculation gives no upper depth bound. If b=v_5(Vtilde_n) is finite and b<2F-floor(log_5(n+1)), strict separation proves v_5(R)=b and v_5(q_n)=max(0,2F-b). At or beyond that threshold the second-kind term can affect the result and cannot be discarded.

The next attainable arithmetic lemma is an all-index congruence modulo 25 for the COMPLETE Vtilde on n=4 modulo 5, with a proved bound on discarded tails, followed by a depth argument on any remaining zero classes. The first congruence would classify potential further zeros; it would not by itself prove an all-depth upper bound. No lift has been inferred or computed here.

## Evidence, scope, and sources

Both new checkers completed with exit code 0 and sandboxed=true. The main checker reports PASS for eight formal identities, two exact constructions at all required scalar seeds, and the full endpoint comparisons in their degree domain. The residual checker reports PASS without generating additional indices.

Files in this assigned directory:

- check_normalized_prime_seeds.py
- normalized_prime_seed_certificate.json
- check_normalized_five_residual.py
- normalized_five_residual_certificate.json
- NORMALIZED_PRIME_SEEDS.md
- NORMALIZED_REPORT.md

The new shared B2_COMMON_FACTOR_TERNARY_DRAFT.md, its checker, and its successful certificate were read, not modified. The original endpoint source and the b=1 contraction sources were supplied and read earlier. The draft's header still says execution pending; its separate successful controller result and certificate provide the actual execution evidence. Agent 2's review remains separate.

No historical files, shared records, or other agents' files were changed. No networking or external paths were used. The large-prime maximal-minor theorem retains p>2n+4 and is not applied here. Fixed-b error bounds are inherited, not reproved. These results do not solve e+pi, establish primitive shrinking, or settle any all-depth question at the exceptional normalized zero.
