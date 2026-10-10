> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent all-residue certificate audit at 71 and 83

Date: 2026-09-13. Reviewer: audit_sources. **FULL PASS.**

This review covers exactly the two assigned primes 71 and 83 in
raw_second_predeclared_uniform_seed_certificate.json and its generator
check_second_predeclared_uniform_seed_list.py. No other prime or original
large-degree approximant was computed. The exact independent verifier is
check_uniform_71_83_independent.py; its full output is
uniform_71_83_independent_certificate.json.

## 1. Complete coverage and result

Every residue was independently recomputed, with no early stopping:

| Prime | Positive seeds | Negative seeds | Total classes | Product of D | Product of E |
|---:|:---|:---|---:|---:|---:|
| 71 | k=0,...,35 | k=34,...,0 | 71 | 58 mod 71 | 33 mod 71 |
| 83 | k=0,...,41 | k=40,...,0 | 83 | 26 mod 83 | 39 mod 83 |

All 154 full determinant values D and endpoint values E are nonzero in
their respective prime fields. Every individual value agrees with the
source certificate, not just the two product checks. Every required
cofactor also agrees. The verifier performed **3,206 separate direct
determinants**.

The last positive seeds satisfy 2k=p-1, so they meet the strict positive
condition p>2k. The first negative seeds satisfy 2k+1=p-2, so they meet
the strict negative condition p>2k+1. Residue zero uses the empty positive
seed. Residue p-1 uses the independently proved n+1 theorem and its
empty negative seed. Thus neither middle boundary nor either empty
boundary is omitted.

## 2. Independent reconstruction of all Schur values

The source obtains all cofactors from one Appell Wronskian inverse row.
The independent verifier does not import or call that routine. It obtains
the complete coefficients a_j from the differential equation



$$
H(t)=e^t(1+t^2)^b,\qquad
 (1+t^2)H'=(1+t^2+2bt)H,
$$




$$
(d+1)a_{d+1}=a_d+(2b-d+1)a_{d-1}+a_{d-2},\qquad
 a_0=1,\quad a_{-1}=a_{-2}=0.
$$



Only d+1<=2k<p is divided by. This works for both backgrounds b=k
and b=-k-1; no infinite negative binomial expansion is numerically cut
off or approximated.

For every partition used, the verifier constructs its own Jacobi--Trudi
matrix and multiplies its determinant by its own hook product:



$$
M_\lambda^{[b]}(1)
 =H_\lambda\det[a_{\lambda_i-i+j}].
$$



The full partition is (k^(k+1)), while each individual cofactor has
partition



$$
\gamma_i=((k+1)^{k-i},k^i),\qquad 0\le i\le k.
$$



The full determinant and all k+1 cofactors are recomputed separately.
Every needed coefficient index and hook length is at most 2k, so all
normalizing denominators are units modulo p. In particular this audit
does not assume that the source's inverse-row factorial/Vandermonde
ratio is correct: the direct normalized minors check that ratio.

The source's displayed inverse-row formula is itself correct:
deleting row i and the last derivative column gives the sign
(-1)^(i+k), and the ratio of the full to omitted degree Vandermondes
is i!(k-i)!.

## 3. Independent positive endpoint calculation

From the independently computed cofactor values C_j, use the coherent
cofactor scale



$$
b_j=(-1)^{k-j}\binom kj C_j,\qquad
 U_j=(k+j)!\,b_j,\qquad S(t)=(1+t^2)^kU(t).
$$



The verifier computes the actual simultaneous polynomial and truncated
exponential numerator by the coefficient identities



$$
Q_j=\binom{3k-j}{k}S_{3k-j},\quad 0\le j\le2k,
$$




$$
[z^h]P_e=\sum_{j=0}^h\frac{Q_j}{(h-j)!},
 \qquad E=P_e(1)=\sum_{h=0}^{2k}[z^h]P_e.
$$



These are the established original coefficient identities, in the same
coherent scale as D. Every exponential factorial is at most (2k)! and
therefore a p-unit. Binomial coefficients with upper index above p are
computed as integers, so there is no illicit factorial inverse.
The original high exponential moment equations were also checked after
integral factorial clearing:



$$
\sum_{j=0}^{2k}Q_j(h)_{\underline j}=0
 \quad(2k+1\le h\le3k).
$$



Thus E is checked without using the source's reconstructed V polynomial
or its endpoint border sum. The result agrees in every positive class.
Unit D makes this cofactor scale a unit multiple of the primitive
normalization required by the transfer theorem.

## 4. Independent negative endpoint calculation

Put r=p-k-1. The verifier forms the selected low factorial coefficients,
then the high-tail coefficients and ordinary endpoint jets:



$$
b_i=(-1)^{r-i}\binom ri C_i,
\quad
 H_i=\sum_{u=0}^{\lfloor(k-i)/2\rfloor}
 \binom ru(r+i+1)^{\overline{2u}}b_{i+2u},
$$




$$
J_h=h!\sum_{i=h}^k\binom{r+i}{r+h}H_i.
$$



These are the finite nonnegative-representative coefficient maps proved
in the negative-residue theorem. The full jet vectors agree with the
source, including the required J_0=D.

For the endpoint functional, this verifier constructs the ordinary
polynomial



$$
f(X)=\sum_{s=0}^k\binom{r+s}{s}(r+X)_{\underline s}
     =\sum_{d=0}^k f_dX^d.
$$



It then converts powers to falling powers using integer Stirling numbers
of the second kind:



$$
X^d=\sum_h {d\brace h}(X)_{\underline h},\qquad
 A_h=\sum_{d=h}^k f_d{d\brace h},\qquad E=\sum_h A_hJ_h.
$$



This uses neither the source's negative-binomial closed expression for
A_h nor its finite-difference cross-check. All A and E values agree.
No cancellation or denominator conclusion is inferred from a floating
calculation; all field calculations and residual comparisons are exact.

## 5. Theorem consequence and scope

The positive and negative transfer theorems have independent PASS in
raw_positive_residue_transfer_independent_review.md and
raw_negative_residue_transfer_independent_review.md. Combining them with
this finite certificate proves, for every n with



$$
v_p(n!)>\lfloor\log_p(2n)\rfloor,\qquad p\in\{71,83\},
$$



that the actual primitive numerator is a p-unit and



$$
v_p(q_n)=v_p(Z_n)\ge v_p(n!).
$$



In particular n>=2p suffices for each of these primes, so both bounds
hold simultaneously at every n>=166. This does not claim that q_n
equals the displayed factorial part or that any other prime is uniformly
good. The all-even asymptotic consequence requires the other assigned
prime certificates and the separately reviewed signed relative error.

The output records SHA-256 hashes of both audited source files. The
checker was run directly with Python 3.12 and returned PASS for all 154
classes. No correction to the source certificate was needed.
