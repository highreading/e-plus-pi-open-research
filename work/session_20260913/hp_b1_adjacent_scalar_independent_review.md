> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent review: the b=1 adjacent scalar valuation gate

Date: 2026-09-13. Reviewer: audit_results.
Source: hp_b1_adjacent_scalar_valuation_gate.md.
Verdict: FULL PASS. No mathematical correction requested.

This is a proof audit and an identical rerun of the already frozen
n=2,8 controls. It introduces no degree or prime scan and proves
no unclaimed denominator-growth theorem.

## 1. Integer Legendre and second-kind normalization

The integer normalization is L_k=2^k i^k Leg_k(-i(2t-1)).
Its generating function at t=1 is (1-4z-4z^2)^(-1/2).
Changing variables in the polynomial divided difference gives
Q_k=2^(k+2)i^(k-1) W_(k-1)(-i).
The ordinary second-kind generating function, or its recurrence
with W_0=1, gives
W_(k-1)=sum_(j=1)^k Leg_(j-1)Leg_(k-j)/j.
Converting both factors therefore gives exactly the factor 8
in Q_k=8 sum P_(j-1)P_(k-j)/j. This also proves the stated
lcm denominator bound without an untracked dyadic factor.

## 2. Actual endpoint numerator and kernel cancellation

I independently derived the same endpoint identity from the
rational second-kind Wronskian. In integer normalization put
P=L_n, U=L_(n+1), A=P(1), B=U(1), and
G=AQ_(n+1)-BQ_n=(-1)^n 2^(2n+3)/(n+1).
Then the elementary endpoints are


$$
t_j=(A T_j(U)-B T_j(P))/G,\qquad
 x_j=(Q_nT_j(U)-Q_{n+1}T_j(P))/G.
$$


The second identity follows by writing the exact projection
remainder as D/(1-t)-pi K_n, where
D=(Q_(n+1)P-Q_nU)/G and D(1)=1, then reconstructing the
Taylor polynomial. Thus it retains the actual A endpoint.
Using T_0(Q)-T_1(Q)=ell_1(Q) in
X=(1+t_1)x_0-(1+t_0)x_1 and Y=t_1-t_0 gives exactly


$$
X/Y=
 [R_{n+1}(Q_n+T_n)-R_n(Q_{n+1}+T_{n+1})]/
 [P_{n+1}R_n-P_nR_{n+1}].
$$


This verifies the sign and the fixed-n convention for T_(n+1).
It also independently verifies the source's monic derivation,
including the -1 in its polynomial second-kind CD identity.

## 3. Factorials, integer scalar, and the reduced gcd

Rodrigues gives
sum [t^j]L_k x^(k+j)/(k+j)! =
2^k x^k H_k(x)/(k!)^2.
Its first derivative gives the second contraction in source (9).
The factor J_(n+1)/(n+1)=K_(n+1) is integral because
H'_k(1)/k=(k-1)![t^(k-1)]e^t(1-t+t^2/2)^k is integral.
Consequently the Delta in source (10) is an integer, and the
integer CD normalization above gives exactly


$$
\delta=(-1)^n\Delta_n/[2^{n+3}(n!)^2].
$$



M=(2n+1)! clears both T sums and both rational Q values.
Hence the stated N_n is integral, and X/Y=N_n/(M Delta_n).
The denominator and prime-valuation formulas in (14) are therefore
exact for every prime, including endpoint cancellation and full
coefficient content. They remain correct if N_n=0 under the
stated infinite-valuation convention.

## 4. All prime blocks, with the numerator obstruction retained

The previously independently proved J_k/k congruence gives K_k=2
mod p for odd p dividing k. Therefore Delta_n=-4P_n mod p when
p divides n+1. The formal-series Frobenius identity
F(t)=(1-4t-4t^2)^((p-1)/2)F(t^p)
has a polynomial factor of degree p-1. Coefficient comparison
proves the Lucas identity at arbitrary a, with no restriction to
one prime block. Its last coefficient is chi_p, so
P_(ap-1)=chi_p P_(a-1) mod p.

At p=3 the three digit coefficients are 1,-1,-1, all units.
Thus Delta_n is a 3-unit for every n=2 mod 3, and the exact
valuation of delta is -2 v_3(n!). The source correctly retains
v_3(N_n) in the actual denominator formula; it does not confuse
this factorial pole with a factorial lower bound for reduced q.
The already passed n=p-1 exclusion is consistent: it forces an
extra numerator factor p when v_p(M)=1.

## 5. Frozen rerun and remaining scope

The identical invocation
/opt/homebrew/bin/python3.12 check_hp_b1_adjacent_scalar_gate.py
passes. Its only degrees are the previously frozen 2 and 8.
The direct full-kernel quotient, scalar quotient, second-kind
moment calculation, Rodrigues contractions, and reduced gcd
all agree. The JSON field v3_delta denotes the rational
lower-case endpoint difference, not the integer Delta_n.

The new all-index arithmetic achievement is the exact adjacent
scalar quotient and the denominator-side prime-block unit theorem.
The remaining estimate is a bound, or a proved opposing
cancellation, for the single integer N_n in (13). The source
correctly leaves b=1 primitive growth/shrinking unresolved.
