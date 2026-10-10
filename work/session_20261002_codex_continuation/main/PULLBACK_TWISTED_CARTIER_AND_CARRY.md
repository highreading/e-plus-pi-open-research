> Archived research record. Read the [current proof status](../../../docs/PROJECT_STATE.md) and [errata](../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Twisted Cartier rigidity and a universal gauged carry

Root original application,2026-10-02. Author theorem; main problem remains open.

## Archive/literature gate

The archive already has Cartier/Frobenius modules for other elliptic families, including item263_punctured_frobenius_report.md and item269_fixed_frobenius_divisor_report.md, and actual logarithmic prime support in the20261001 session. These were searched/read before this target. Their generic Cartier method is credited overlap. M11 computes the pth pullback jet as a family parameter; it has not supplied the universal quadratic-character law or the all-power normalized-jet valuation below.

Fresh primary searches/readings included Beukers and Vlasenko, Dwork crystals I, Section3, https://arxiv.org/html/1903.11155v3 . That paper supplies coefficient-selection/Frobenius background, not the final endpoint gcd theorem needed here. A TIFR logarithmic-Cartier source was located by search but its PDF failed to open; no argument below relies on uninspected text. The proof is given directly by rational logarithmic derivatives.

## Good-prime coefficient law

Let P in Q[z] with P(0)=0, and put

    G=4 arctan(P/(2-P)), G'=4P'/((P-1)^2+1)=sum_(k>=0)a_k z^k.

Let p be any odd prime outside the denominator support of the monomial coefficients of P. Then all a_k are p-integral, since the denominator of G' has constant2. Define chi_p=(-1|p). At EVERY k>=0,

    a_(p(k+1)-1) = chi_p a_k mod p.                 (1)

There is no requirement p>deg P. In particular, if g_j=G^(j)(0), then

    g_p = -chi_p g_1 mod p, g_1=2P'(0).            (2)

Thus the pth jet residue for a good prime depends only on the quadratic character and the first jet, rather than the high-degree polynomial.

### Direct proof, including reduction degeneracies

Over the algebraic closure of F_p factor P-(1+i) and P-(1-i). Roots cannot be0 because P(0)=0 and p is odd. Retain multiplicities, allowing degree drop or inseparability after reduction. Assign the logarithmic weights L_lambda=-2i m_lambda on the first set and+2i m_lambda on the second. The derivative identity gives

    a_k=-sum_lambda L_lambda lambda^(-k-1).

A multiplicity divisible by p simply gives zero weight; no square-free assumption is used. Frobenius permutes the roots of the first/second set if chi_p=1 and interchanges the sets if chi_p=-1. At the image root lambda^p its weight is chi_p L_lambda. Reindexing this finite power sum proves(1). Wilson's theorem applied to g_p=(p-1)!a_(p-1) gives(2).

Equivalently the differential G'dz is a Cartier eigenvector with eigenvalue chi_p. The root calculation proves the eigenrelation for this actual rational pullback, without confusing absolute Frobenius pullback with Cartier or importing an unrelated elliptic-module theorem.

## All-depth normalized derivative units

Iterating(1) gives, for every s>=1 and m>=1,

    a_(p^s m-1) = chi_p^s a_(m-1) mod p.          (3)

If a_(m-1) is a p-unit then the ACTUAL derivative has exactly

    v_p(g_(p^s m))=v_p((p^s m-1)!).               (4)

In particular if p does not divide g_1, then

    v_p(g_(p^s))=v_p((p^s-1)!)  for every s>=1.    (5)

This is an all-depth valuation equality for the derivative itself. It is not a modulo p^2 coefficient congruence or an all-depth final-center gcd theorem. For the degree61/81 constructions P'(0)=1, every good odd p has g_1=2 and satisfies(5).

## Simplified actual endpoint carry

Use M11's integer endpoint arrays D_N=N!E_N, B_N=N!(1+V_N), with the actual q_N=|D_N|/gcd(D_N,B_N). For N=pa+r,0<=r<p, combine(2) with the already derived Lucas carry calculation:

    D_N=(-1)^a D_r mod p,
    B_N=(-1)^a [B_r-r!+a chi_p g_1 D_r] mod p.    (6)

On D_r=0 the carry is still killed exactly. For P'(0)=1, the universal seed r=1 has B_1-1=2, so every good odd prime with N=1 mod p retains its FULL valuation v_p(D_N) in q_N. Formula(6) fixes the off-zero carry as well and removes an independent pth-jet parameter from the finite local arithmetic interface.

Changing a pullback while preserving p-integral monomial coefficients and P'(0) cannot change its pth jet residue. Tuning that jet independently must leave this good-prime class, for example by introducing p into coefficient denominator support. Such a change has an arithmetic cost and cannot be treated as a free response parameter.

## New receipt and remaining problem

PULLBACK_CARTIER_CARRY_CERTIFICATE.json contains four independent polynomial cases: linear, cubic, new degree61, and new degree81. It checks(1) at k0..7 at every good odd prime below200, the universal pth jet, the independently computed binomial endpoint arrays through5p, and normalized p-squared jets at the first two good primes of each case. Counts are45,45,29,24 good primes. The p-squared checks are modulo p normalized coefficient units, not assertions of an unproved modulo p^2 formula.

The complete final q remains governed by the common-zero residues B_r-r! at the derangement roots D_r, deeper cancellation when those residues vanish, and primes larger than N. A fixed collection of r1 congruences does not supply positive exponential prime mass: imposing N=1 mod many distinct primes forces their product to divide N-1. Therefore the universal local rigidity is useful arithmetic structure but does not prove a favorable gcd rate, a global gauged-family exclusion, or the irrationality of e+pi.
