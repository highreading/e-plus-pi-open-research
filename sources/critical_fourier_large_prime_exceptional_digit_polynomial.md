> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The exceptional large-prime Fourier digit as a fixed polynomial

Date: 2026-08-27.

## 1. Outcome

Let $n>0$ be even, $K=k-1\ge n$, and let $p$ be an odd prime in
the one-block band



$$
K<p\le2(K-n).
 \tag{1}
$$



Put



$$
\ell=K-n,\qquad s=2\ell-p.
 \tag{2}
$$



The exact first-digit theorem gives



$$
D_{n,K,p}\equiv\frac{C_0}{p}\pmod p,
 \tag{3}
$$



and calls $D_{n,K,p}=0$ the exceptional branch.  This note proves that
the exception is governed by one fixed integer polynomial.

For $0\le h\le n/2$, define



$$
A_{n,h}
 =\binom n{2h}\frac{(2n-2h)!\,n!}{(n-h)!}\in\mathbb Z_{>0},
 \tag{4}
$$



and put



$$
\boxed{
 \Phi_n(X)=
 \sum_{h=0}^{n/2}
 A_{n,h}\,2^h
 \prod_{t=1}^{h}(X+2t-1)
 \in\mathbb Z[X].}
 \tag{5}
$$



The empty product at $h=0$ is one.

### Theorem 1.1

Every prime satisfying (1) obeys $p>2n$, and



$$
\boxed{
 D_{n,K,p}
 \equiv
 -\frac{s!}{n!\,\ell!\,K!}\Phi_n(s)
 \pmod p.}
 \tag{6}
$$



All factorials in the denominator of (6) are $p$-adic units.  Since
$s\equiv2\ell\pmod p$,



$$
\boxed{
 D_{n,K,p}=0
 \quad\Longleftrightarrow\quad
 p\mid\Phi_n(2\ell).}
 \tag{7}
$$



The degree of $\Phi_n$ remains exactly $n/2$ modulo every such $p$.
Consequently, for fixed $n,p$, at most $n/2$ values of $K$ in (1)
can lie in the exceptional branch.

If $\mathcal E_{n,K}$ is the squarefree product of the primes in (1)
that both lie in the exceptional branch and divide the final matching
content, then



$$
\boxed{
 \mathcal E_{n,K}
 \mid\gcd\!\left(q_n,\Phi_n(2(K-n))\right).}
 \tag{8}
$$



This is an exact resultant-style localization of the exceptional
large-prime support.  It does not control the generic first-digit branch.

## 2. Proof

Write $n=2r$.  From $K<p\le2(K-n)$ one obtains



$$
p>2n,\qquad
 0\le s<p,\qquad
 2\ell=p+s,\qquad
 s+2n<p.
 \tag{9}
$$



The accepted super-Catalan expression for the central coefficient is



$$
C_0=
 \sum_{j=0}^{r}
 \binom n{2j}
 \frac{(n+2j)!(2K-n-2j)!}
 {(r+j)!(K-r-j)!K!}.
 \tag{10}
$$



Set $h=r-j$.  Then (10) becomes



$$
C_0=
 \sum_{h=0}^{r}
 \binom n{2h}
 \frac{(2n-2h)!(p+s+2h)!}
 {(n-h)!(\ell+h)!K!}.
 \tag{11}
$$



Equation (9) shows



$$
p\le p+s+2h<2p
 \qquad(0\le h\le r).
$$



Wilson's theorem therefore gives



$$
\frac{(p+b)!}{p}
 =(p-1)!\prod_{j=1}^{b}(p+j)
 \equiv-b!\pmod p
 \qquad(0\le b<p).
 \tag{12}
$$



Divide (11) by $p$, use (12), and factor out the $h=0$ factorials.
This gives



$$
\frac{C_0}{p}
 \equiv
 -\frac{(2n)!\,s!}{n!\,\ell!\,K!}
 \sum_{h=0}^{r}
 c_{n,h}
 \frac{(s+2h)!}{s!}
 \frac{\ell!}{(\ell+h)!}
 \pmod p,
 \tag{13}
$$



where



$$
c_{n,h}
 =\binom n{2h}
 \frac{(2n-2h)!\,n!}
 {(2n)!(n-h)!}.
 \tag{14}
$$



Since $\ell=(p+s)/2$, cancellation of the even factors gives



$$
\frac{(s+2h)!}{s!}\frac{\ell!}{(\ell+h)!}
 \equiv
 2^h\prod_{t=1}^{h}(s+2t-1)
 \pmod p.
 \tag{15}
$$



Indeed, the denominator on the left is congruent to
$2^{-h}\prod_{t=1}^{h}(s+2t)$, which cancels the even factors in the
first quotient.  Every canceled factor is nonzero by (9).

Substitution of (14)--(15) into (13) cancels the displayed factor
$(2n)!$ and gives (6), because



$$
(2n)!c_{n,h}=A_{n,h}.
$$



Equation (3) proves (7).  The leading coefficient of $\Phi_n$ is



$$
2^rA_{n,r}
 =2^r\frac{(n!)^2}{(n/2)!},
 \tag{16}
$$



which is nonzero modulo $p>2n$.  Thus the reduced polynomial has degree
$r$ and at most $r$ roots.  The map



$$
K\longmapsto s=2K-2n-p
$$



is injective modulo $p$ on the interval $K<p$, proving the root-count
assertion.

Finally, every prime in $\mathcal E_{n,K}$ divides $q_n$, because the
final content divides $q_n$, and divides the polynomial value by (7).
The primes are distinct, so their product divides the gcd in (8).
$\square$

## 3. An explicit size bound

All coefficients and all factors in (5) are positive at $X=2\ell$.
The elementary estimates



$$
A_{n,h}\le2^n(2n)!\,n^{n/2},
 \qquad
 \prod_{t=1}^{h}(2\ell+2t-1)
 \le(2\ell+n)^{n/2}
 \tag{17}
$$



give



$$
\boxed{
 0<\Phi_n(2\ell)
 \le
 \left(\frac n2+1\right)
 2^{3n/2}(2n)!\,n^{n/2}(2\ell+n)^{n/2}.}
 \tag{18}
$$



In particular,



$$
\log\mathcal E_{n,K}
 =O\!\left(n\log(n+K)\right).
 \tag{19}
$$



This bound is rigorous but not strong enough to close the remaining
$K\asymp n\log n$ matching strip: its right side is still of factorial
scale.

## 4. Exact super-Catalan certificate

The companion script computes $C_0$ directly from (10), independently
evaluates $\Phi_n$, and checks (6)--(7) on



$$
2\le n\le24\quad(n\ \mathrm{even}),\qquad n\le K\le300.
 \tag{20}
$$



The grid contains 77,063 primes in the one-block band, spread over 3,261
parameter pairs.  It verifies the digit normalization in every instance
and finds 287 instances of $D=0$.  For each fixed $(n,p)$, it also
checks that the number of exceptional $K$-values does not exceed
$n/2$; the largest count observed on the grid is three.  These counts
are exact finite diagnostics, not density claims.

The script separately checks the three known generic survivors and the
exceptional normalization $(n,K,p)=(4,35,43)$.

Run

    python -m py_compile scripts/critical_fourier_large_prime_exceptional_digit_polynomial_certificate.py
    python scripts/critical_fourier_large_prime_exceptional_digit_polynomial_certificate.py

For a byte-identical rerun, use

    python scripts/critical_fourier_large_prime_exceptional_digit_polynomial_certificate.py \
      --output /tmp/critical_fourier_large_prime_exceptional_digit_polynomial_certificate.json
    cmp results/critical_fourier_large_prime_exceptional_digit_polynomial_certificate.json \
      /tmp/critical_fourier_large_prime_exceptional_digit_polynomial_certificate.json

The all-parameter theorem is the factorial argument in Section 2; the
finite grid checks its normalization and endpoints.

## 5. Limitations

The polynomial theorem controls only the branch $D=0$.  When $D\ne0$,
a prime can survive through the simple-root congruence



$$
4(q_n/p)U_{n,K,p}\equiv p_nD_{n,K,p}\pmod p,
$$



whose quotient $q_n/p\pmod p$ is not determined by the root condition
$q_n\equiv0\pmod p$.  A uniform bound for simultaneous generic
survivors requires additional information.

Nothing here proves a uniform upper bound for the complete matching
content or an arithmetic classification of $e+\pi$.
