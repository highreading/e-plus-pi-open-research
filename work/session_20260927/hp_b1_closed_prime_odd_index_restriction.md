> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact odd-index restriction from the closed six-prime list

Date: 2026-09-27. Author: audit_computations.
Status: complete finite CRT/rate argument, NOT independently reviewed
before the user's stop instruction. Its seed/lift inputs have separately
passed `hp_b1_uniform_5_13_independent_review.md`; that review explicitly
does not certify this odd-index synthesis or CRT count.

Only the predeclared primes 5,7,11,13,17,19 are used here. The
underlying actual-q transfer and seed table are in
`hp_b1_prime_seed_transfer_and_closed_atlas.md`; the root at residue1
is resolved for every p>=5 by `hp_b1_residue_one_actual_numerator.md`.
No extra prime or canonical degree is tested.

## 1. Precisely which prime bounds have been proved

For every sufficiently large n, primes5 and13 give
v_p(q_n)>=2v_p(n!). The other four primes give the same bound
outside their following **unresolved** residue sets:



$$
B_7=\{2,3\},\quad B_{11}=\{2\},\quad
 B_{17}=\{3,11\},\quad B_{19}=\{14\}.                    \tag{1}
$$


These sets remove the residue1 root from the full seed-zero table,
because its all-depth numerator cancellation is now controlled.
An unresolved residue is not asserted to have a small denominator;
the present certificate simply supplies no factorial lower bound there.

Write w_p=2log(p)/(p-1), and set



$$
b=w_5+w_{13}=\tfrac12\log5+\tfrac16\log13,
 \qquad t=2\log(1+\sqrt2).
$$


For any fixed residue combination, the proved mandatory divisor gives



$$
\liminf\frac{\log q_n}{n}\ge b+
 \sum_{p\in\{7,11,17,19\}:\ n\bmod p\notin B_p}w_p.
 \tag{2}
$$


The finite set of residue combinations means that every strict
comparison with t yields a uniform positive margin on that collection
of combinations, not merely a separate pointwise margin.

## 2. Exact threshold logic

The following three inequalities characterize exactly which combinations
this particular mandatory-divisor rate excludes:



$$
b+w_7>t,\qquad b+w_{17}+w_{19}>t,
 \qquad b+w_{11}<t.                                    \tag{3}
$$


The weights decrease with p>1, since log(p)/(p-1) has negative
derivative. Thus w_11>w_17>w_19: among the last three primes the
two smallest suffice, while even the largest single weight does not.
It follows that the proved divisor exceeds the error threshold exactly
when either 7 is good, or at least two of 11,17,19 are good.

All comparisons in (3) are certified by integer arithmetic, not rounded
logarithms. Respectively exponentiate by 6,72,30 and compare



$$
5^3 13\,7^2>(1+\sqrt2)^{12},
$$




$$
5^{36}13^{12}17^9 19^8>(1+\sqrt2)^{144},
$$




$$
5^{15}13^5 11^6<(1+\sqrt2)^{60}.
$$


The checker obtains the exact integer pair A,B for
(1+sqrt2)^k=A+B sqrt2. For an integer L>A, the comparison is
equivalent to (L-A)^2 versus 2B^2; if L<=A its sign is immediate.
The certificate preserves these integer margins.

## 3. The exact unexcluded CRT set

The remaining odd indices therefore lie in



$$
\boxed{n\bmod7\in\{2,3\},\quad
 \text{at least two of }
 \left\{n\bmod11=2,\ n\bmod17\in\{3,11\},\ n\bmod19=14\right\}.}
 \tag{4}
$$


This is an exact description by independent congruences; no large
enumeration is necessary. Modulo11*17*19 there are



$$
1\cdot2\cdot18+1\cdot15\cdot1+10\cdot2\cdot1
       +1\cdot2\cdot1=36+15+20+2=73
$$


classes with at least two bad primes. The two bad classes modulo7
give 146 classes modulo



$$
M=7\cdot11\cdot17\cdot19=24871.                        \tag{5}
$$


Parity is independent of this odd modulus. Thus (4) has density
146/24871 among odd integers. Combined with the proved all-even
exclusion, it has density 146/49742 among all integers.

For every index outside this set and all sufficiently large n, the
actual primitive form has a uniform positive exponential lower rate,
by the already proved b=1 evaluated-error exponent. Hence any
shrinking subsequence in this family must eventually be confined to
the set (4).

The density is that of an **unexcluded index set**, not a density of
successful approximants. Inside (4), (2) supplies a lower bound below
the critical rate; it supplies no upper bound for actual q_n and no
shrinking forms. Additional prime factors or deeper cancellation
analysis can still exclude some or all of these indices.

## 4. Verification and scope

Files:
`check_hp_b1_closed_prime_rate_and_crt.py` and
`hp_b1_closed_prime_rate_and_crt_certificate.json`.
They check the three exact algebraic inequalities and all four CRT
component counts. Seed values are independently checked in the
separate complete scalar-seed certificate, with no unbounded scan.

The current arithmetic inputs do not prove or disprove irrationality
of e+pi. They rule out much of this particular degree-one route and
leave the explicit odd CRT set (4) unresolved.
