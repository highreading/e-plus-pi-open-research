> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent complete uniform-prime certificates for 101 and 109

Date: 2026-09-13. Reviewer: audit_computations.

**FULL PASS.** All 101 residues modulo 101 and all 109 residues modulo
109 independently have unit full-determinant and exponential-endpoint
seeds. Every required cofactor, positive b coefficient, and negative
endpoint jet agrees with the source certificate. The reviewed all-index
residue transfer theorems therefore apply to every degree, subject only
to their explicit factorial threshold.

The reviewed source is the 101/109 portion of
`raw_third_predeclared_uniform_seed_certificate.json`. Independent code:
`check_uniform_101_109_independent.py`. Full exact output:
`uniform_101_109_independent_certificate.json`. The output binds the source
bytes by SHA-256. No source-checker module is imported; no other prime or
large-degree canonical approximant is computed. All operations use
integers or finite-field arithmetic, without approximate determinants,
large-integer factorization, or numerical tolerances.

## 1. Transposed Jacobi–Trudi inverse-column formula

Fix a nonempty seed k with 2k<p and background b. Put



$$
h_d=[z^d]e^z(1+z^2)^b,\qquad
 J_{ij}=h_{k+i-j}\quad(0\le i,j\le k).
$$



J is the transpose of the ordinary Jacobi–Trudi matrix for
$\lambda=(k^{k+1})$. Every index is in [0,2k], so all complete-function
factorials have p-unit denominators. They are evaluated using



$$
h_d=\sum_{u\le d/2}\binom bu\frac1{(d-2u)!}\pmod p.
$$



The calculation may replace b by its least nonnegative residue modulo p:
u<p, so $\binom bu$ is a polynomial with a unit denominator in b.
This applies equally to the negative background b=-k-1.

Let $x=J^{-1}e_0$ and $d=\det J$. Then



$$
\boxed{D=H_{(k^{k+1})}d,\qquad
 C_i=H_{\gamma_i}(-1)^{k-i}d\,x_{k-i},\quad
 \gamma_i=((k+1)^{k-i},k^i).}                 \tag{1}
$$



To check the second identity, delete row 0 and column k-i from J.
After transposition, its row r corresponds to the old column r for
r<k-i and to r+1 for r\ge k-i. Its entry in column s is respectively
$h_{k+1-r+s}$ or $h_{k-r+s}$. It is therefore exactly the ordinary
Jacobi–Trudi matrix for gamma_i, with no reversal sign. Cramer's formula
for $(J^{-1})_{k-i,0}$ contributes the displayed sign $(-1)^{k-i}$.
Multiplication by the direct hook product gives (1).

The implementation computes d and x by modular Gauss–Jordan elimination,
and checks both the final identity matrix and the equation Jx=e_0 against
the original matrix. Pivot products and row-swap signs give d. Every hook
length is explicitly checked to lie in [1,p-1]. Thus no nonunit hook or
factorial is inverted. All seed determinants are found nonzero.

For every nonempty seed, the two extreme cofactor determinants i=0,k
are additionally computed directly from their deleted JT matrices and
checked against (1). These checks are not used to generate the cofactor
vector; they independently verify its endpoint indexing and sign.

This method differs from the source's inverse-last-row Appell Wronskian
calculation. The source's separate check of its full determinant by JT
does not enter the present implementation.

## 2. Independent actual endpoint normalization

For a positive seed, the cofactors in (1) have the gamma_i convention,
so the exact scale-free coefficient vector is



$$
B_l=(-1)^{k-l}\binom kl C_l=D\,b_{k,l}/V_k(1).
$$



The endpoint is checked by the original polynomial reconstruction:



$$
U_l=(k+l)!B_l,\quad S=(1+t^2)^kU,\quad
 Q_{3k-d}=\binom d k S_d\quad(k\le d\le3k).
$$



Hence $Q=D\widehat Q_k/V_k(1)$. The endpoint of the product with the
exponential series, truncated at total degree 2k, is exactly E. Only
factorials up to 2k<p are inverted. The binomials $\binom d k$ are
evaluated as integers even when d\ge p; no forbidden factorial division
occurs. This differs from the source's high-tail recovery of V followed
by its exponential endpoint border.

For a negative seed, r=p-k-1 is a positive representative. The code uses



$$
b_i=(-1)^{r-i}\binom ri C_i,\qquad
 w_i=\sum_{2u\le k-i}\binom ru(r+i+1)^{\overline{2u}}b_{i+2u},
$$





$$
J_h=h!\sum_{i=h}^k\binom{r+i}{r+h}w_i.
$$



The identity J_0=D is checked. The degree-k Taylor polynomial with these
derivatives at 1 is then paired with the original positive-index border



$$
D_{r,j}=\sum_{s=0}^{r+j}\binom{r+s}{s}(r+j)_{\underline s}.
$$



Modulo p this border, as a function of j, has degree at most k. Terms
k<s<p vanish through the first binomial, and terms s\ge p vanish through
the falling factorial. Consequently it depends only on derivatives of V
at 1 of orders 0,...,k, making the Taylor substitution exact. This route
checks E without using the source's generalized-negative-binomial
coefficients A_{k,h}. Every J_h is nevertheless compared afterward with
the original certificate.

The empty positive seed and the negative k=0 class use their already
reviewed unit theorems. They do not rely on a singular empty-matrix
inverse convention.

## 3. Complete residue coverage and exact results

| Prime | Positive seeds | Negative seeds | Residue rows checked | Unit pairs |
|---:|---|---|---:|---:|
| 101 | k=0,...,50 | k=49,...,0 | 101 | 101 |
| 109 | k=0,...,54 | k=53,...,0 | 109 | 109 |

The positive range covers residues 0,...,(p-1)/2; the negative range
covers all remaining residues via r=p-k-1. The largest positive degree
obeys 2k=p-1<p, and the largest negative seed obeys 2k+1=p-2<p.
Thus no boundary seed falls outside a theorem's strict hypotheses.

Every D and E is nonzero. All 210 rows match the source. The complete
output retains each residue's D,E,C, the inverse-column data and pivot
certificate, original-endpoint reconstruction data, and negative J where
applicable. Assertions also verify complete, duplicate-free residue
coverage. The implementation finished its exact checks in approximately
7.5 seconds; timing plays no role in the validity of the certificate.

## 4. Actual uniform denominator theorem

Use the accepted all-index transfer theorems and their full reviews:

- `raw_positive_residue_transfer_independent_review.md`;
- `raw_negative_residue_transfer_independent_review.md`.

All residue classes now have a p-unit Pe_n(1) for p=101 and p=109.
Retain the actual primitive scale



$$
q_n=\frac{|Z_n|}{\gcd(|Z_n|,|Pe_n(1)+4Pa_n(1)|)}.
$$



The proved global content divisibility supplies



$$
v_p(Z_n)\ge v_p(n!),\quad
 v_p(Pa_n(1))\ge v_p(n!)-\lfloor\log_p(2n)\rfloor.
$$



For p\ge7 and n\ge2p, put m=\lfloor n/p\rfloor\ge2. The elementary
inequality



$$
2n\le2p(m+1)-2<p^m
$$



holds at m=2 by 6p-2<p^2 and then by induction. Since
$v_p(n!)\ge m$, the arctangent endpoint is divisible by p. The sum
Pe_n(1)+4Pa_n(1) is therefore a p-unit. The endpoint gcd removes no
p-factor from Z_n, proving



$$
\boxed{v_{101}(q_n)=v_{101}(Z_n)\ge v_{101}(n!)\quad(n\ge202),}
$$




$$
\boxed{v_{109}(q_n)=v_{109}(Z_n)\ge v_{109}(n!)\quad(n\ge218).}
$$



In particular these are uniform bounds on the full eventual even
sequence. They are established all-index statements obtained from
complete finite seed data and proved transfer identities, not numerical
extrapolations. No verdict on the separately assigned primes 71,83,127,
151 is included in this review. A global rate crossing that uses those
primes must wait for their independent certificates.
