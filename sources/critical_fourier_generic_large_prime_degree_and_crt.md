> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A degree obstruction and a CRT bound for generic large-prime matching

Date: 2026-08-27.

## 1. Scope

For an odd prime in the one-block band



$$
K<p\le2(K-n),
 \tag{1}
$$



the accepted first-digit theorem defines explicit residues
$D_{n,K,p},U_{n,K,p}\in\mathbb F_p$.  On the branch $D,U\ne0$ and
$v_p(q_n)=1$, survival in the final matching content is equivalent to



$$
F_{n,p}(K):=
 4(q_n/p)U_{n,K,p}-p_nD_{n,K,p}
 \equiv0\pmod p.
 \tag{2}
$$



This note records two rigorous facts about (2).

First, the raw dependence on $K$ need not have low polynomial degree:
one certified example has the maximum interpolation degree permitted by
the number of admissible parameters.

Second, simultaneous generic survivors satisfy a square-modulus CRT
divisibility.  A direct archimedean estimate of that divisibility is too
large to give a subfactorial bound throughout the unresolved strip.

## 2. Exact interpolation-degree counterexample

Take



$$
n=64,\qquad p=937.
 \tag{3}
$$



The beta coefficient has



$$
v_{937}(q_{64})=1.
 \tag{4}
$$



The admissible one-block parameters are



$$
s=2(K-n)-p\in\{1,3,\ldots,807\},
 \tag{5}
$$



or equivalently



$$
K=533,534,\ldots,936.
$$



Put $s=2x+1$, so $0\le x\le403$, and let



$$
f_x=F_{64,937}(K)\in\mathbb F_{937},
 \qquad K=533+x.
 \tag{6}
$$



### Proposition 2.1

For the 404 exact residues in (6),



$$
\boxed{\Delta^{403}f_0=513\ne0\pmod{937}.}
 \tag{7}
$$



Consequently the unique polynomial
$P(X)\in\mathbb F_{937}[X]$ of degree at most $403$ satisfying



$$
P(x)=f_x\qquad(0\le x\le403)
$$



has degree exactly $403$.  In particular, the raw generic congruence on
this admissible set cannot be represented by any polynomial in $K$ of
degree at most $402$.

The only zero with $D,U\ne0$ is



$$
x=264,\qquad s=529,\qquad K=797,
 \tag{8}
$$



where



$$
D=257,\qquad U=463,\qquad
 q_{64}/937=601,\qquad p_{64}=397\pmod{937}.
 \tag{9}
$$



This is the previously certified surviving prime $937>K$.

### Interpretation

Proposition 2.1 refutes a low-degree *raw polynomial interpolation*
strategy; for example, it rules out any universal claim that the degree
in (2) is at most $6n$.  It does not rule out a low-order relation after
extracting factorial, character, or hypergeometric factors, and it does
not rule out a bounded-degree rational or algebraic relation.

## 3. Proof and exact recurrence used by the certificate

The certificate starts from



$$
R_s(y)=P_{64}(y)(1+y)^s\pmod{937}
$$



at $s=1$.  It advances through all values in (5) by the exact recurrence



$$
R_{s+2}(y)=R_s(y)(1+y)^2.
 \tag{10}
$$



For each $s$, it computes



$$
U=\sum_{t=0}^{128+s}
 \frac{\nu_{u+t}([y^t]R_s)}{u+t},
 \qquad
 u=\frac{937-s-128}{2},
 \tag{11}
$$



and computes $D$ independently from the fixed exceptional-digit
polynomial formula



$$
D\equiv
 -\frac{s!}{64!\,((937+s)/2)!\,K!}\Phi_{64}(s)
 \pmod{937}.
 \tag{12}
$$



All denominators in (11)--(12) are nonzero modulo $937$.  Substitution
in (2) gives the sequence $f_x$.  Repeated exact finite differencing
gives (7).  Since the leading Newton interpolation coefficient is
$\Delta^{403}f_0/403!$, and $403!$ is a unit modulo $937$, (7)
proves Proposition 2.1.

For an additional integrity check, the comma-separated decimal residue
sequence has SHA-256 digest

    de44c4cdb29ed59fdaf1823d9ba69aa637f9fa56325fb49b8ca474f200853d9f

The digest is not a proof substitute; the certificate emits all data
needed to reproduce the finite difference.

## 4. A simultaneous-survivor CRT lemma

Return to general even $n$ and $K$.  Define the fixed integer



$$
Z_{n,K}=4q_nT_{n,k}-p_nL_KC_0.
 \tag{13}
$$



Let $\mathcal G^{\mathrm{gen}}_{n,K}$ be the squarefree product of the
primes $p$ in (1) that lie on the generic branch $D\ne0$ and divide
the final matching content.

### Proposition 4.1



$$
\boxed{
 \mathcal G^{\mathrm{gen}}_{n,K}\mid q_n,\qquad
 \left(\mathcal G^{\mathrm{gen}}_{n,K}\right)^2
 \mid Z_{n,K}.}
 \tag{14}
$$



### Proof

The first-digit theorem gives $v_p(q_n)=v_p(B)=1$ for every factor in
$\mathcal G^{\mathrm{gen}}_{n,K}$.  In particular, every such prime
divides $q_n$ and occurs only once in the final content.  Since $p>K$,
one has $v_p(L_K)=0$, while $D\ne0$ gives $v_p(C_0)=1$.
The exact local survival congruence is therefore



$$
4q_nT_{n,k}\equiv p_nL_KC_0\pmod{p^2}.
 \tag{15}
$$



The squares of the distinct primes are pairwise coprime, so the Chinese
remainder theorem proves (14).  $\square$

## 5. What the direct size argument yields

Let $\|G_{n,k}\|_1$ denote the sum of the complex absolute values of the
coefficients of the Fourier polynomial.  Its factorization gives



$$
\|G_{n,k}\|_1
 \le
 2^n(2\sqrt2)^n2^{2(K-n)}
 =2^{2K+n/2}.
 \tag{16}
$$



Since $|N_m|\le3|C_m|$,



$$
|T_{n,k}|
 \le3L_K\|G_{n,k}\|_1.
 \tag{17}
$$



For even $n$, the positive beta remainder gives
$0<p_n<e q_n<3q_n$.  Equations (13), (16), and (17) imply



$$
\boxed{
 |Z_{n,K}|
 \le15q_nL_K2^{2K+n/2}.}
 \tag{18}
$$



If $Z_{n,K}\ne0$, equations (14) and (18) give



$$
\mathcal G^{\mathrm{gen}}_{n,K}
 \le
 \min\left\{
 q_n,\,
 \sqrt{15q_nL_K2^{2K+n/2}}
 \right\}.
 \tag{19}
$$



Using $\log q_n\le n\log(2n)+O(1)$ and
$\log L_K=K+o(K)$, the square-root term at
$K\sim c\,n\log n$ has leading logarithm



$$
\frac12\left(1+c(1+2\log2)\right)n\log n.
 \tag{20}
$$



For



$$
c\ge\frac1{1+2\log2},
$$



this is no smaller at leading order than the elementary bound
$\mathcal G^{\mathrm{gen}}\le q_n$.  Thus the direct CRT-plus-size
argument does not give a uniform subfactorial bound in the upper part of
the unresolved strip.

If $Z_{n,K}=0$, (14) has no archimedean consequence; that exact-ratio
branch must be handled separately.  Nothing here proves that a sharper
use of the arithmetic structure of $Z_{n,K}$ is impossible.

## 6. Exact certificate

The companion script constructs the 404 residues in (6) using only exact
arithmetic modulo $937$.  The update (10) avoids a separate expansion
for each parameter.  It emits the complete residue list, verifies its
digest, performs all 403 rounds of finite differencing, and checks
(7)--(9).

The script also reconstructs the full Gaussian Fourier polynomials for the
three known generic large-prime survivors.  In each case it computes
$Z_{n,K}$ exactly, verifies $v_p(Z)=2$, and verifies the explicit
bound (18).

Run

    python -m py_compile scripts/critical_fourier_generic_large_prime_degree_and_crt_certificate.py
    python scripts/critical_fourier_generic_large_prime_degree_and_crt_certificate.py

For a byte-identical rerun, use

    python scripts/critical_fourier_generic_large_prime_degree_and_crt_certificate.py \
      --output /tmp/critical_fourier_generic_large_prime_degree_and_crt_certificate.json
    cmp results/critical_fourier_generic_large_prime_degree_and_crt_certificate.json \
      /tmp/critical_fourier_generic_large_prime_degree_and_crt_certificate.json

The interpolation statement is a rigorous finite counterexample, while
the CRT and size estimates in Sections 4--5 hold for all parameters.

## 7. Limitations

The finite counterexample concerns raw polynomial degree, not all possible
algebraic normalizations.  The CRT lemma controls only generic primes in
the one-block band and gives no information about the small-prime or
$D=0$ branches beyond the separate theorems.

No uniform upper bound for the full matching content, and no arithmetic
classification of $e+\pi$, follows from this note.
