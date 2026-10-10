> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Second closed uniform-prime seed certificate

Date: 2026-09-13. Original finite computation by audit_results.
All internal exact checks PASS. The complete successful-prime certificates
for 71 and 83 have independent PASS in
uniform_71_83_independent_review.md. Unsuccessful-prime witness rows
retain their internal certificates here.
Both all-index transfer theorems have independent PASS:
raw_positive_residue_transfer_independent_review.md and
raw_negative_residue_transfer_independent_review.md.
The earlier eight-prime certificate is preserved unchanged.

The second predeclared list is exactly
47,53,59,61,67,71,73,79,83,89,97. For each prime the calculation stops
at the first rigorously checked bad residue. A uniformly good prime
requires all p residues. No original large-degree approximant is built
and no prime outside the closed list is tested.

## 1. Results and their exact scope

The internally certified uniformly good primes are **71 and 83**.
The other primes have the following first bad witnesses:

| p | First bad residue n mod p | Branch, k | Reason | D | E |
|---:|---:|:---|:---|---:|---:|
| 47 | 40 | negative, 6 | endpoint zero | 16 | 0 |
| 53 | 15 | positive, 15 | determinant zero | 0 | not needed |
| 59 | 8 | positive, 8 | endpoint zero | 57 | 0 |
| 61 | 17 | positive, 17 | determinant zero | 0 | not needed |
| 67 | 25 | positive, 25 | determinant zero | 0 | not needed |
| 71 | none | all 71 residues | all good | units | units |
| 73 | 9 | positive, 9 | determinant zero | 0 | not needed |
| 79 | 14 | positive, 14 | determinant zero | 0 | not needed |
| 83 | none | all 83 residues | all good | units | units |
| 89 | 3 | positive, 3 | determinant zero | 0 | not needed |
| 97 | 18 | positive, 18 | determinant zero | 0 | not needed |

A determinant-zero witness establishes a limitation of the determinant
unit test. It is not an assertion that the actual endpoint numerator
vanishes. An endpoint-zero witness with D nonzero does prove actual
Pe_n(1)=0 modulo p on that residue class. Neither type alone determines
the actual higher-depth gcd or reduced denominator.
No classification is asserted for residues after the stopping point.

## 2. One matrix supplies all needed cofactors

For k>=1, use background b=k in the positive branch and b=-k-1
in the negative branch. Put


$$
W_{ij}=({\cal A}_{k+i}^{[b]})^{(j)}(1),\qquad
                    0\le i,j\le k,
$$




$$
\Delta_k=\prod_{j=1}^k j!,\qquad D=\det W/\Delta_k.
 \tag{1}
$$


All degrees k,...,2k are below p. Thus Delta_k is a p-unit.
The small cofactor partition gamma_i=((k+1)^(k-i),k^i) has
degree set {k,...,2k} with k+i removed; its derivative columns are
0,...,k-1. Its Vandermonde is
Delta_k/[i!(k-i)!]. If D is nonzero, solve


$$
W^T x=e_k,\qquad x_i=(W^{-1})_{ki}.
 \tag{2}
$$


The normalized gamma_i cofactor is therefore exactly


$$
\boxed{C_i=(-1)^{i+k}D\,i!(k-i)!\,x_i\pmod p.}       \tag{3}
$$


This follows from cofactor_(i,k)(W)=det(W)(W^-1)_(k,i);
the sign and the omitted Vandermonde factors are both retained.
The implementation checks (2) by exact matrix multiplication.
It uses one elimination, not k separate cofactor determinants.
If D=0 it takes no inverse and already has a sufficient bad witness.

An independently formed rectangular Jacobi--Trudi matrix and direct
hook product check D in every case, including singular ones.
The matrices, modular pivots, both determinant values, hook product,
Vandermonde, inverse row and all reconstructed C_i are saved.

## 3. Endpoint normalization and internal checks

In the positive branch the actual scaled primitive coefficients are


$$
B_l=D\,b_{k,l}/V_k(1)=(-1)^{k-l}\binom kl C_l.
 \tag{4}
$$


Here C_l is the gamma_l cofactor, equal to the former cofactor indexed
by k-l. The two index conventions are not interchanged silently.
The exact upper-tail transformation reconstructs R=D V_k/V_k(1).
The code separately checks coefficientwise


$$
(t-1)^kR=(1+\partial_t^2)^k[t^kB(t)],\qquad R(1)=D.
 \tag{5}
$$


It then computes E from the exact original exponential border.
Thus when D is a unit, E/D is the actual Pe_k(1)/V_k(1) ratio.

In the negative branch, equations (3)-(4) of
raw_negative_residue_schur_and_endpoint_seeds.md give J_h, A_h and E.
The code checks J_0=D, independently recomputes every J_h with
nonnegative binomial arguments at the residue representative p-k-1,
and recomputes A_h by finite differences of the endpoint polynomial.
These are finite functional calculations, not a canonical solution
at that residue representative.

The k=0 positive class uses the empty seed; the k=0 negative class
uses the already reviewed n+1 unit theorem. Every other class obeys
the strict Appell-degree bounds of its transfer theorem.

## 4. Reproducibility

Run:

    /opt/homebrew/bin/python3.12 check_second_predeclared_uniform_seed_list.py

Only exact Python integers and arithmetic modulo the prescribed primes
are used. The full output is
raw_second_predeclared_uniform_seed_certificate.json, with SHA-256

    864873094eb83e9a2bc316ae301109119b4280109d5c6aff8830307dc6ea1bb6

For primes 71 and 83 it retains every residue and its matrix/functional
certificate. For each other prime it retains the first bad certificate
and the stopping index, rather than asserting anything about untested
residues. The separate successful-prime review is recorded in the header.

## 5. Application of the independently checked successful primes

The two reviewed transfer theorems and independently checked
good-prime certificates give


$$
v_p(q_n)=v_p(Z_n)\ge v_p(n!)
$$


for every n satisfying the elementary arctangent threshold.
For p>=7, n>=2p is sufficient: with m=floor(n/p)>=2,
2n<2p(m+1)<p^m, the last inequality following by induction
from 6p<p². Thus the new pair has common threshold n>=166.

Together with the first closed list and the reviewed uniform primes
3 and 7, the candidate all-index mandatory divisor is


$$
2^{a_n}\prod_{p\in\{3,7,23,43,71,83\}}p^{v_p(n!)}
 \mid q_n\qquad(n\ge166),
$$


where a_n=n+2 floor((n+2)/4) is the exact reviewed dyadic depth.
This statement yields, for even n,


$$
\liminf\frac{\log q_n}{n}\ge
 L=\frac32\log2+
 \sum_{p\in\{3,7,23,43,71,83\}}\frac{\log p}{p-1}
 \simeq2.2602038483.
$$


The approximation-shrinking threshold is
5 log(phi), approximately 2.4060591253. The displayed finite set
therefore still falls short by approximately 0.145855277.
The decimal values are descriptive; no modular classification depends
on a floating-point calculation.

The remaining bad witnesses are compatible by the Chinese remainder
theorem. These particular seed tests alone consequently supply no
additional mandatory weight at every index. No global exclusion of
shrinking subsequences and no e+pi irrationality conclusion is claimed.
