> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Top-prime-power bands in the critical Fourier content

Date: 2026-08-27.

## 1. Exact theorem

Let $n>0$ be even, $K=k-1\ge n$, and set



$$
\ell=K-n.
 \tag{1}
$$



Retain the accepted Fourier polynomial and content



$$
G_{n,k}(y)=P_n(y)(1+y)^{2\ell},\qquad
 C_m=[y^{K+m}]G_{n,k}(y),
 \tag{2}
$$





$$
L_K=\operatorname{lcm}(1,\ldots,K),\qquad
 T_{n,k}=\sum_{m=1}^{K}\frac{L_K}{m}N_m,\qquad
 h_{n,k}=\gcd(4T_{n,k},L_KC_0).
 \tag{3}
$$



Fix an odd prime $p$, put



$$
\lambda=\lfloor\log_pK\rfloor,\qquad Q=p^\lambda,
 \tag{4}
$$



so that



$$
Q\le K<pQ,\qquad v_p(L_K)=\lambda.
 \tag{5}
$$



### Theorem 1.1

Suppose that for some odd integer $a\ge3$,



$$
\boxed{
 \frac{2K}{a+1}<Q\le\frac{2\ell}{a}.}
 \tag{6}
$$



Then



$$
\boxed{
 p\mid C_{mQ}\quad\text{for every integer }m
 \text{ with }|mQ|\le K,}
 \tag{7}
$$



and consequently



$$
\boxed{p\mid C_0,\qquad p\mid T_{n,k},\qquad p\mid h_{n,k}.}
 \tag{8}
$$



For $p>\sqrt K$, one has $Q=p$, and Theorem 1.1 is exactly the
previous generalized odd-prime band theorem.  The new content is that
(7)--(8) remain true for $p\le\sqrt K$ after the Fourier shifts are
changed from multiples of $p$ to multiples of the largest power
$Q=p^\lambda$ not exceeding $K$.

## 2. Proof

Write



$$
2\ell=aQ+s,\qquad0\le s<Q.
 \tag{9}
$$



The upper inequality in (6) gives $aQ\le2\ell$, while the strict lower
inequality gives



$$
2\ell<2K<(a+1)Q.
$$



Thus (9) holds.  Since $a,Q$ are odd and $2\ell$ is even, $s$ is
odd.

The Frobenius identity in characteristic $p$ gives



$$
(1+y)^Q\equiv1+y^Q\pmod p.
 \tag{10}
$$



Consequently, in $(\mathbb Z[i]/p\mathbb Z[i])[y]$,



$$
G_{n,k}(y)
 \equiv R(y)(1+y^Q)^a\pmod p,\qquad
 R(y)=P_n(y)(1+y)^s.
 \tag{11}
$$



Put $d=\deg R\le2n+s$.  The residue of $K=\ell+n$ modulo $Q$ is



$$
r=\frac{Q+s+2n}{2},
 \qquad
 K=\frac{a-1}{2}Q+r.
 \tag{12}
$$



The strict inequality in (6) is equivalent to



$$
(a+1)Q>2K=aQ+s+2n,
$$



so



$$
s+2n<Q.
 \tag{13}
$$



Equations (12)--(13) give



$$
d<r<Q.
 \tag{14}
$$



The right side of (11) is supported only in



$$
[jQ,jQ+d],\qquad0\le j\le a.
 \tag{15}
$$



Every exponent congruent to $K$ modulo $Q$ lies in the complementary
gap described by (14).  The coefficient at each exponent $K+mQ$
therefore vanishes modulo $p$, proving (7).

It remains to pass to $T_{n,k}$.  If $Q\nmid m$, then
$v_p(m)\le\lambda-1$, and hence



$$
p\mid\frac{L_K}{m}.
 \tag{16}
$$



If $Q\mid m\le K$, write $m=tQ$.  Equation (5) gives $1\le t<p$,
so $v_p(m)=\lambda$; equation (7) gives $p\mid C_m$, hence
$p\mid N_m$.  Thus every summand defining $T_{n,k}$ is divisible by
$p$.  Equation (7) also gives $p\mid C_0$, and (8) follows.
$\square$

## 3. Forced product and asymptotic mass

Let $\mathcal P^{\mathrm{top}}_{n,K}$ be the set of odd primes whose top
power $Q=p^{\lfloor\log_pK\rfloor}$ satisfies (6) for at least one odd
$a\ge3$, and put



$$
H^{\mathrm{top}}_{n,K}
 =\prod_{p\in\mathcal P^{\mathrm{top}}_{n,K}}p.
 \tag{17}
$$



Theorem 1.1 gives



$$
\boxed{H^{\mathrm{top}}_{n,K}\mid h_{n,k}.}
 \tag{18}
$$



The primes $p>\sqrt K$ in (17) are precisely those in the previously
proved disjoint bands



$$
\frac{K}{j+1}<p\le\frac{2(K-n)}{2j+1},
 \qquad j\ge1,\qquad p>\sqrt K.
 \tag{19}
$$



Every newly added prime satisfies $p\le\sqrt K$.  Therefore



$$
0\le
 \log H^{\mathrm{top}}_{n,K}-\log H_{n,K}
 \le\vartheta(\sqrt K)=O(\sqrt K),
 \tag{20}
$$



where $H_{n,K}$ is the product from (19) and the last estimate is the
elementary Chebyshev bound.

It follows that, whenever $n=o(K)$,



$$
\boxed{
 \log H^{\mathrm{top}}_{n,K}
 =(2\log2-1+o(1))K.}
 \tag{21}
$$



Thus the top-prime-power extension adds exact small-prime divisibility but
does not improve the leading $2\log2-1$ content constant.  This is only
a limitation of the one-copy theorem above; it does not rule out stronger
higher-$p$-adic divisibility theorems.

## 4. Exact finite-grid certificate

The companion script constructs the Fourier polynomial over
$\mathbb Z[i]$, computes $C_0,T_{n,k},h_{n,k}$ exactly, and checks
(7)--(8) on



$$
2\le n\le12\quad(n\ \mathrm{even}),\qquad n\le K\le180.
 \tag{22}
$$



There are 849 parameter pairs with a nonempty top-power band.  They give
5,010 forced-prime instances and 23,992 separately checked Gaussian
coefficient congruences.  Of the prime instances, 614 have
$p^2\le K$, so they are genuinely new beyond the $Q=p$ theorem.
The script also checks the full forced product divides $h_{n,k}$ for
each parameter pair.

Run

    python -m py_compile scripts/critical_fourier_top_prime_power_bands_certificate.py
    python scripts/critical_fourier_top_prime_power_bands_certificate.py

For a byte-identical rerun, use

    python scripts/critical_fourier_top_prime_power_bands_certificate.py \
      --output /tmp/critical_fourier_top_prime_power_bands_certificate.json
    cmp results/critical_fourier_top_prime_power_bands_certificate.json \
      /tmp/critical_fourier_top_prime_power_bands_certificate.json

This finite computation checks the normalization and the passage from
coefficient gaps to content.  The all-parameter proof is Section 2.

## 5. Limitations

The theorem forces one copy of $p$, not one copy of $Q$.  To force
$p^2\mid T_{n,k}$, the terms with $v_p(m)=\lambda$ would require a
second Fourier digit, while those with $v_p(m)=\lambda-1$ would require
a compatible lower-power gap.  Neither assertion follows from (10).

Equation (21) shows that merely adding one copy of the small primes found
by the top-power gap cannot close the remaining matching strip.  Nothing
in this note bounds the final odd matching content or proves an arithmetic
classification of $e+\pi$.
