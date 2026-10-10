> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Parameter Hensel lifting with a finite archimedean radius budget

Author result, 2026-10-02; continuing original research. This target concerns the same degree-160 endpoint-fixed family as M16, but asks a new question about prime-power depth and parameter limits.

## Archive and primary-paper gate

A fresh archive search for parameter Hensel lifting, pullback common p-adic zeros, derangement simple zeros and radius/prime-power constructions found the earlier dyadic Gram germs and the session's M15–M16 interfaces. They do not complete this two-variable construction. The classical derangement interpolation is credited to O'Desky–Richman, *Derangements and the p-adic incomplete gamma function*, arXiv:2012.04615v4, Sections 2 and 4.2 (opened full HTML). A separate fresh primary search opened Birmajer–Gil–Weiner, *On Hensel's roots and a factorization formula in Z[[x]]*, arXiv:1308.2987, Section 3, Theorem 3.1. The joint factorial-subtracted numerator and its parameter/radius budget below are derived here; they are not assertions from those papers.

Sources: https://arxiv.org/html/2012.04615v4 ; https://arxiv.org/pdf/1308.2987 .

## Family and complete arithmetic functions

Set p=163, r=159 and

    P_K(z)=P81(z)+K z^159(1-z)/159!,  K in Z_p.

The coefficients are p-integral for every p-adic integer K. Let G_K=F(P_K), let a_j(K) be the ordinary coefficients of G_K', and let g_j(K)=(j-1)!a_(j-1)(K). The denominator of G_K' has constant term 2, a p-adic unit, so each a_j is a polynomial in K with p-integral coefficients. Define the full arithmetic extensions

    D*(x)=sum_(j>=0) (-1)^j (x)_j,
    C*(x,K)=sum_(j>=1) (-1)^j (x)_j T_j(K),
    T_j(K)=sum_(l=1)^j a_(l-1)(K)/l.

At nonnegative integers N these agree respectively with (-1)^N D_N and (-1)^N(B_N-N!). The factorial subtraction is part of the definition, not an optional normalization. Actual q_N remains |D_N|/gcd(D_N,B_N).

The coefficient bound v_p(T_j)>=-floor(log_p j), together with v_p((x)_j)>=v_p(j!), gives a uniform tail valuation at least

    tau(j)=v_p(j!)-floor(log_p j) -> infinity.

Consequently, for fixed x in Z_p, C*(x,K) is a restricted analytic function of K with integral coefficients. Parameter derivatives obey the same tail bound. This justifies parameter Hensel lifting; continuity alone would not justify it.

## The denominator root and the parameter root

Fresh exact falling-factorial evaluation gives

    D*(159)=0 mod163,  D*'(159)=62 mod163.

The derivative sum modulo p needs terms through j=2p-1: terms j>=2p have at least two vanishing factors in the residue class, and their derivative is zero modulo p. Terms j>=p cannot simply be omitted from the derivative calculation. The unit derivative and integer-coefficient finite approximants yield a unique root x_p in 159+163 Z_p. Higher-depth approximation tails justify the usual Hensel shift formula.

On that denominator-root cell, the complete M15 carry law makes C*(x,K) modulo p independent of the extra index digit. Since all g_j for j<159 are unchanged and g_159 changes by 2K,

    C*(x,K) = (-1)^159 [(B_159(0)-159!)+2K] mod163.

The parameter derivative is therefore -2 modulo163. This is a polynomial identity, not merely an equality of polynomial values: after the uniform cutoff j<2p, its degree in K is at most floor((2p-1)/159)=2<p. Thus the finite-field evaluations uniquely determine that polynomial. The first root is K=-31 modulo163, and restricted analytic Hensel lifting gives a unique K_p in -31+163 Z_p with

    D*(x_p)=C*(x_p,K_p)=0.

This is an exact joint p-adic common zero. It is a statement about a p-adic parameter. Neither rationality of K_p nor a real/complex bound on K_p follows.

## Ten rational specializations retaining radius above two

Let x_k be the Hensel index residue modulo163^k, and let K_k be the centered integer parameter residue modulo163^k. The independent analytic bound from M16 is

    |K|*3*2^159*401^81 < 159!.

The stronger uniform bound with |K|<=floor(163^k/2) holds for k=1,...,10. Hence every one of these ten rational polynomials P_(K_k) omits the two punctures on the closed disk of radius two, and has even integral G-jets and analytic radius greater than two.

For every sufficiently large nonnegative N congruent to x_k modulo163^k,

    163^k divides D_N and B_N,

because N! vanishes at the required precision and C* has period163^k on the denominator-root cell. Thus 163^k divides the actual complete gcd. The script records a concrete large N in every row.

| k | Centered integer K_k |
|---:|---:|
| 1 | -31 |
| 2 | 5837 |
| 3 | -525543 |
| 4 | -273362604 |
| 5 | 17374431421 |
| 6 | 7151318688087 |
| 7 | 1395048667460753 |
| 8 | -13890577538616582 |
| 9 | -37387246651397700657 |
| 10 | 612410837619432241127 |

The largest-depth receipt checks N=6645847199578466624566 modulo163^10. In addition to the ordinary-coefficient Mahler evaluation, it independently constructs integral derivative jets through order1793 by the original differential recurrence and evaluates the complete binomial endpoint convolution. Both give zero at the required precision. No enormous D_N or B_N is materialized or estimated by floating point.

## Consequence and exact limit of the result

Substantial finite good-prime depth is compatible with a certified radius above two. The parameter construction also produces a joint p-adic common zero, clarifying the mechanism behind those finite cells. However, the ten specializations are ten different rational polynomials. Passing to K_p supplies no fixed rational polynomial with unbounded common-content depth; passing to a p-adic limit supplies no archimedean radius bound. Even for the finite specializations, one selected prime power is far from the global factorial-sized content needed to make q_N times the complete error small. No main rationality theorem is claimed.
