> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Actual contact numbers: known Bessel identification and uniform binary periods

Coordinator proof candidate, 9 October 2026. DIFFERENT review pending.
This is a coefficient theorem, not a complete terminal valuation upper or a
decision about the rationality of e+pi. No original index, return, column,
border, integer divisor or physical boundary is changed.

## 1. Overlap and primary-source gate

The exact original contact recurrence is already DIFFERENT-passed:



$$
\theta_0=1,\quad\theta_1=0,\quad
\theta_{n+1}=(2n+1)\theta_n+\theta_{n-1}.
$$



The underlying sequence and its Bessel identification are classical, not
claimed as new. The primary contributed entries [A000806](https://oeis.org/A000806)
and [A278990](https://oeis.org/A278990), read in full, identify respectively
the signed Bessel values and the unsigned recurrence. Thus
$\theta_n=(-1)^ny_n(-1)$. The quoted database formulas and combinatorial
interpretations are not imported as a terminal determinant theorem.

Scoped current/Desktop searches for those identifiers, loopless diagrams,
theta period12, and binary Bessel periods find no earlier actual general
higher-precision period result. FULL A2turn16 section10 ALREADY proves the
modulo4 six-step anti-period by a two-step matrix; that result is REUSED,
not claimed as new here. Earlier current period3 statements concern
modulo2. The FULL archive source exponential_beta_bessel_period_congruence
uses instead X_n=(4n-2)X_(n-1)+X_(n-2), with different initial states;
its anti-period hierarchy also assumes odd primes. Those results are REUSE
only at their stated distinct scopes. No exhaustive novelty claim is made.
Primary searches for these exact sequence identifiers and prime-power
periods find the known recurrence/identification, not the needed actual
full source-jet Schur quotient. Elementary matrix products, polynomial
Taylor expansion and finite-ring lifting below are standard methods.

## 2. Uniform transition matrix calculation

Write



$$
M(n)=\begin{pmatrix}2n+1&1\\1&0\end{pmatrix},\qquad
P_T(n)=M(n+T-1)\cdots M(n).
$$



For n>=1 the original state (theta_n,theta_(n-1)) is carried to
(theta_(n+T),theta_(n+T-1)) by P_T(n). To include theta_0 in a periodicity
conclusion, apply this statement at n=1; no negative moment or extra
physical return is introduced.

Modulo8, the individual transition matrices depend only on n modulo4.
The four complete six-step products are



$$
\begin{array}{c|c}
n\bmod4&P_6(n)\bmod8\\\hline
0,2&\begin{pmatrix}3&4\\4&3\end{pmatrix}\\
1,3&\begin{pmatrix}7&4\\4&7\end{pmatrix}.
\end{array}
\tag{2.1}
$$



For a direct finite product derivation, put a=2n+1. Pair consecutive
matrices as



$$
M(n+1)M(n)=
\begin{pmatrix}(a+1)^2&a+2\\a&1\end{pmatrix}.
$$



Then P_6 is the product of this expression at a+8, a+4 and a.
Reduction at a=1,3,5,7 modulo8 gives (2.1). These four residues exhaust
all integer starting phases; they are not an empirical extrapolation.

The reduction to -I modulo4 agrees with the already established FULL
A2turn16 anti-period. Their squares are I modulo8,
and n and n+6 have the same parity. Therefore, uniformly in n,



$$
P_6(n)\equiv-I\pmod4,\qquad P_{12}(n)\equiv I\pmod8.
\tag{2.2}
$$



Consequently theta_(n+6)=-theta_n modulo4 and theta_(n+12)=theta_n
modulo8 for every n>=0. The second coordinate of the transition starting
at n+1 gives the additional precise law



$$
\theta_{n+6}\equiv
\{-1+4(n\bmod2)\}\theta_n+4\theta_{n+1}\pmod8.
\tag{2.3}
$$



The complete theta tables over a period of length12 are therefore



$$
\theta_n\bmod4=(1,0,1,1,0,1,3,0,3,3,0,3),
$$




$$
\theta_n\bmod8=(1,0,1,5,4,1,7,4,3,7,0,7).
\tag{2.4}
$$



Their first six entries follow from the already proved recurrence;
(2.2)-(2.3) prove the remaining entries and uniform repetition.

## 3. General precision: a derivative cancellation and doubling

For an odd integer a, consider the integral matrix polynomial



$$
\mathcal P_T(a)=
\prod_{j=T-1}^{0}\begin{pmatrix}a+2j&1\\1&0\end{pmatrix},
\qquad P_T(n)=\mathcal P_T(2n+1).
$$



Suppose 6 divides T. Modulo2 every factor is



$$
A=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad A^3=I.
$$



With E=diag(1,0), the full polynomial derivative at odd a is



$$
\mathcal P_T'(a)\equiv
\sum_{j=0}^{T-1}A^{T-1-j}EA^j\pmod2.
$$



Each summand has period3 in j. Each of the three classes occurs T/3
times, an even number. Hence every derivative entry is even at every
odd a. This is a uniform full-product cancellation, not a generic
matrix hypothesis.

Now let h>=3 and T=3*2^(h-1), and assume P_T(n)=I modulo2^h for
every n. The argument shift from n to n+T changes a by 2T, of
valuation h. The exact integral polynomial Taylor formula gives



$$
\mathcal P_T(a+2T)-\mathcal P_T(a)
\in2^{h+1}M_2(\mathbb Z).
\tag{3.1}
$$



Indeed, the linear term has its additional derivative factor2, and
each term of degree at least2 contains (2T)^2, of valuation2h>=h+1.
All Taylor coefficients are integer coefficients obtained by binomial
expansion; no division by a Taylor factorial is asserted.

Thus P_T(n+T)=P_T(n) modulo2^(h+1), and



$$
P_{2T}(n)=P_T(n+T)P_T(n)
\equiv P_T(n)^2\equiv I\pmod{2^{h+1}}.
$$



The final equality uses P_T=I+2^hB and 2h>=h+1. The base h=3,
T=12 is (2.2). Induction proves the uniform coefficient theorem



$$
\boxed{\theta_{n+3\cdot2^{h-1}}\equiv\theta_n\pmod{2^h}
\quad(h\ge3,\ n\ge0).}
\tag{3.2}
$$



For h=1, period3 is the passed parity recurrence. For h=2,
period12 follows from (2.2). Minimality of these periods is not needed
or asserted.

## 4. Exact scope and remaining application

The entries B_j(r)=binom(r+j,r)*theta_(r+j) and the passed integer
filters K_b(z,r) can use the tables (2.4) at their actual finite indices.
No row or column factorial is removed. At h>3 the physical-source,
Stirling, elementary-symmetric, rising-ratio and finite-boundary terms
still have to be retained at the requested precision. The periodicity
of theta alone does not evaluate them.

In particular, this theorem does NOT imply that the actual corank-sized
Schur matrix is a unit, that it has rank two, that a selected cofactor
equals a complete determinant, or that the full tied aggregate is nonzero.
The constructive full rank/corank from NEW FULL A2turn16 is separately
being audited by A4turn27. Its full higher effective quotient and the
joint paired upper are OPEN.

The original complete constant border, other-prime contents, actual least
simultaneous clearer, ALL-prime G and same-index primitive whole error
remain unchanged. DIFFERENT audit of the new actual period/lift claims
is PENDING. No unconditional e+pi proof follows.
