> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Closed eight-prime residue-seed certificate

Date: 2026-09-13. Original finite arithmetic by audit_results.
Finite arithmetic: internal cross-checks PASS. The complete successful-prime
data for 23 and 43 have independent PASS in
raw_uniform_23_43_independent_review.md; the other classification rows
retain only their internal checks here. Both transfers have independent PASS, in
raw_positive_residue_transfer_independent_review.md and
raw_negative_residue_transfer_independent_review.md. No new all-index
statement is justified by finite arithmetic alone.

The predeclared primes are exactly
17,19,23,29,31,37,41,43. Every residue was evaluated for each prime.
All matrices are fixed Schur seed matrices with Appell degrees below p.
No original large-degree approximant, large integer factorization, or
unbounded prime search is used.

## 1. Complete classification

A determinant-zero class has D=0. An endpoint-zero class has D nonzero
and E=0, so it proves actual Pe_n(1)=0 modulo p on that class.
These two statuses are not interchangeable.

| p | Determinant-zero residues n mod p | Endpoint-zero residues n mod p | All residues good |
|---:|:---|:---|:---:|
| 17 | 6 | 15 | no |
| 19 | none | 5 | no |
| 23 | none | none | yes |
| 29 | 8 | none | no |
| 31 | none | 16 | no |
| 37 | 2 | none | no |
| 41 | 7 | 9 | no |
| 43 | none | none | yes |

Every residue absent from the two exception columns is good.
The exact exceptional (D,E) pairs are


$$
\begin{array}{c|c|c}
p& n\bmod p &(D,E)\bmod p\\ \hline
17&6&(0,6)\\
17&15&(5,0)\\
19&5&(15,0)\\
29&8&(0,10)\\
31&16&(5,0)\\
37&2&(0,19)\\
41&7&(0,10)\\
41&9&(23,0).
\end{array}
$$


The complete good-residue data, not only these witnesses, are retained
in the certificate.

## 2. Normalizations and two independent determinant formulas

For a positive residue 0<=k< p/2, use background k and partitions
lambda_D=(k^(k+1)) and lambda_j=((k+1)^j,k^(k-j)).
Let D=M_D(1) and C_j=M_j(1). The scaled primitive coefficients are


$$
B_l=D b_{k,l}/V_k(1)
       =(-1)^{k-l}\binom kl C_{k-l}.
$$


They require no division by D, even when D=0 modulo p.
The polynomial R=D V_k/V_k(1) is reconstructed by both:

1. The exact factorial upper-tail transformation followed by inversion
   of multiplication by (t-1)^k.
2. Polynomial division in the exact identity
   (t-1)^k R=(1+partial_t²)^k[t^k B(t)].

The two answers agree coefficientwise, and R(1)=D is checked.
The positive endpoint seed is E=sum R_r D_(k,r), with the original
integer exponential border. For unit D it satisfies
E/D=Pe_k(1)/V_k(1), so the reviewed positive transfer applies.
The empty k=0 convention gives D=E=1.

For a negative residue n congruent to -k-1, use background -k-1,
the full partition (k^(k+1)), and
gamma_i=((k+1)^(k-i),k^i). The derivative and endpoint seeds are exactly
equations (3)-(4) of raw_negative_residue_schur_and_endpoint_seeds.md.
The code checks J_0=D, recomputes J using only nonnegative binomial
arguments at the residue representative p-k-1, and checks the border
coefficients by finite differences of its degree-k polynomial.
The negative k=0 class is supplied by the reviewed n+1 unit theorem.

Every augmented Schur value is checked by both the normalized
Appell Wronskian and hook-product times Jacobi--Trudi. The two matrices,
their modular determinants, elimination pivots, Vandermonde and hook
product are all saved. The Vandermonde and hook product are explicitly
checked nonzero modulo p; all Appell degrees are checked below p.
No inverse of a zero determinant is taken.

## 3. Reproducible certificate and scope

Run:

    /opt/homebrew/bin/python3.12 check_predeclared_residue_seed_atlas.py

It uses only standard Python exact integers and finite-field arithmetic.
The output is raw_predeclared_residue_seed_atlas.json, containing all
240 residue classes and 2300 determinant certificates.
Its SHA-256 is

    48e6f9f9e07c72709e775601c6fd555dd6ba00221f1013f2161114e335695b16

The prime list is hard-coded and closed. Positive classes are
0,...,(p-1)/2; negative classes use k=0,...,(p-3)/2.
These cover every residue exactly once and respect both transfer
theorems' Appell-degree conditions.

The independently verified successful-prime data and reviewed transfers give


$$
v_{23}(q_n)\ge v_{23}(n!),\qquad
 v_{43}(q_n)\ge v_{43}(n!)
$$


for every sufficiently large n. In fact n>=86 is a common threshold:
for p>=7 and m=floor(n/p)>=2,
2n<2p(m+1)<p^m. The second inequality starts with 6p<p² and
then follows by induction. Thus floor(log_p(2n))<m<=v_p(n!).

Together with the independently established uniform three- and
seven-adic bounds and the dyadic rate, these two primes contribute
the exponential lower rate


$$
L=\frac32\log2+\frac12\log3+\frac16\log7
                   +\frac1{22}\log23+\frac1{42}\log43
   \simeq2.1454201214.
$$


This is still below 5 log(phi), approximately 2.4060591253.
The displayed decimals describe the size only; the finite modular
certificate does not depend on them.
The remaining six primes cannot automatically add a uniform weight
through this seed test: choosing one bad residue for each gives
compatible simultaneous congruences by the Chinese remainder theorem.
Such a congruence class is a limitation of these sufficient tests,
not evidence of an actually small denominator.

No exclusion of every shrinking raw subsequence, and no proof about
irrationality of e+pi, follows from this finite set alone.
