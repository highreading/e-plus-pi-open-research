> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Prime-power automata: source update and the actual residue pair

2026-09-13. This note continues Item200, Section6, rather than claiming
its rational diagonal as a new result. The current arithmetic target is
the normalized pair C_0/F_m,C_1/F_m in the reviewed integral depth reduction.

## Primary sources and exact scope

Rowland and Yassawi, [Algebraic power series and their automatic complexity
modulo prime powers](https://ericrowland.github.io/papers/Algebraic_power_series_and_their_automatic_complexity_modulo_prime_powers.pdf),
author version dated June25,2026, was inspected through the state
construction and digit normalization in Sections2–3. Its Theorem3 bounds
the number of states for a rational diagonal modulo p^alpha. The main
innovation stores polynomial digits whose degrees grow with the digit
level, replacing the earlier double exponential dependence on alpha.
Theorem1's asymptotic is stated with each parameter tending to infinity
while the others remain fixed; it must not be treated as a uniform
multi-parameter estimate. State counting alone gives no frequency bound
for common zero outputs. The actual transition graph and its output map
still matter. In particular, for primes comparable to m, the inputs have
few base-p digits, so a fixed-prime long-word density cannot simply be
used in the moving-prime sum. This is an applicable computational and
structural framework, with the valuation-tail estimate still missing.

Rosen, [The sequence of prime coefficients of an algebraic power series](https://julianrosen.net/pdf/Rosen_The_sequence_of_prime_coefficients_of_an_algebraic.pdf),
RIMS Kokyuroku2160(2020),249–253, gives relations modulo p obtained
from Cartier's coordinate invariance. Its prime-index coefficient
framework is relevant to the existing characteristic-p period bridges.
It supplies no uniform prime-power depth bound for the present gcd.

## A concrete two-digit implementation target

The formulas below are derived directly over the polynomial ring. They
specialize the general digit idea to Item200's actual coefficient pair,
including the slope-four index carry. They are not a new general
automaticity theorem.

Use variables t,z and put

    D(t,z)=(1+z^2)^4-t(1-z)^6,
    P_nu(z)=(1+z)^(1+3nu)(1+z^2)^(3-nu), nu=0,1.

Then, exactly,

    C_nu(m)=[t^m z^(4m+nu)] P_nu/D.

This is the coefficient version of the archived constant-term formula.
The denominator has constant term1 and bidegree(1,8); each numerator
has bidegree at most(1,8). No implicit algebraic equation or branch
selection is needed for the computation.

For a prime p define the integral polynomial

    E_p=(D(t,z)^p-D(t^p,z^p))/p.

Let Lambda_(r,s) select monomials with exponents congruent to(r,s)
modulo p and divide the remaining exponents by p. A state modulo p^2
is represented by

    A/D+p B/D^2,

where A and B have coefficients in {0,...,p-1}, with bidegrees at most
(1,8) and(2,16), respectively. The representation as a rational series
is unique: reduction modulo p first determines A, then determines B.
Distinct series can of course have the same selected coefficient sequence.

For a digit r of m and a current index offset c, set

    s=(4r+c) mod p, c'=floor((4r+c)/p).

For p>=5 and c initially0 or1, all subsequent c lie in{0,1,2,3}.
The next selected sequence is obtained from Lambda_(r,s) of the series.

Compute the polynomial U=Lambda_(r,s)(A D^(p-1)) modulo p^2.
Write U=A'+p U_1 coefficientwise, with A' the canonical mod-p lift.
The exact transition is

    B'=U_1 D
       +Lambda_(r,s)(B D^(2p-2)-A D^(p-1) E_p) mod p.

Proof: expand the formal inverse using D(t^p,z^p)=D^p-p E_p:

    1/D = D^(p-1)/D(t^p,z^p)
          -p D^(p-1) E_p/D(t^p,z^p)^2 mod p^2.

For pB/D^2 only the reduction modulo p is needed, giving numerator
B D^(2p-2) and denominator D(t^p,z^p)^2. Applying Lambda pulls these
denominators back to D and D^2. Carrying U_1 from the first rational
digit multiplies it by D, giving the displayed formula. This explicitly
retains both the Frobenius defect and ordinary coefficient carries.

Degree bounds are preserved: before selection, the terms contributing
to A' have bidegree at most p(1,8); those contributing to B' have
bidegree at most2p(1,8). Selection divides these bounds by p. The carry
term U_1 D also has bidegree at most(2,16). Initialization uses
A=P_nu mod p and B=((P_nu-A)/p)D mod p.

After all digits of m have been read, the output is the coefficient of
z^c at t=0 in A/D+pB/D^2. Thus the output uses only
D(0,z)=(1+z^2)^4 and c<=3. The safe state count for one sequence is
4p^(18+51)=4p^69. It is a size upper bound, not a common-zero density.

## What a successful next step must add

On an ordinary rank-zero row the forced factor F_m contains one copy
of p. Therefore the common zero output modulo p^2 is exactly the first
extra common-log condition, with the other factors of F_m p-units.
At higher depth one needs the corresponding complete digit sequence;
modulo p^2 alone cannot bound an unbounded valuation. The root's
two-digit specialization was checked against original integer
coefficient extraction on54 cases at p=5,7,11, including indices on both
sides of p^2, slope carries, and both residue coordinates. An extra
leading zero preserves every checked output. The independent extraction
and complete transitions are in `check_actual_log_two_digits.py`, with
results in `actual_log_two_digit_checks.json`. These are finite
normalization checks of the displayed identities. No statement about zero-output frequencies or
full valuation moments follows from the construction so far.
