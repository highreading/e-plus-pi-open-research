> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Generalized odd prime bands in the critical Fourier content

Date: 2026-08-27.

## 1. Exact band theorem

Let $n>0$ be even, $k>n$, and put



$$
K=k-1,\qquad \ell=K-n.
 \tag{1}
$$



In the accepted Fourier normalization, let



$$
G_{n,k}(y)=P_n(y)(1+y)^{2\ell},
 \qquad
 P_n(y)=i^{-n}(y-1)^n((1+i)y+1-i)^n,
 \tag{2}
$$



and



$$
C_m=[y^{K+m}]G_{n,k}(y),\qquad-K\le m\le K.
 \tag{3}
$$



For $m>0$, write $C_m=A_m+iB_m$ and put



$$
N_m=A_m\sin\frac{m\pi}{2}
 -B_m\left(1-\cos\frac{m\pi}{2}\right).
 \tag{4}
$$



Finally, define



$$
L_K=\operatorname{lcm}(1,\ldots,K),\qquad
 T_{n,k}=\sum_{m=1}^K\frac{L_K}{m}N_m,
 \qquad
 h_{n,k}=\gcd(4T_{n,k},L_KC_0).
 \tag{5}
$$



### Theorem 1.1

Let $p$ be an odd prime satisfying



$$
p>\sqrt K.
 \tag{6}
$$



Suppose that, for some odd integer $a\ge3$,



$$
\boxed{
 \frac{2K}{a+1}<p\le\frac{2\ell}{a}.}
 \tag{7}
$$



Then



$$
\boxed{
 p\mid C_{mp}\quad\text{for every integer }m
 \text{ with }|mp|\le K.}
 \tag{8}
$$



In particular,



$$
\boxed{p\mid C_0,\qquad p\mid T_{n,k},\qquad p\mid h_{n,k}.}
 \tag{9}
$$



For $a=3$, equation (7) is the previously proved band



$$
\frac K2<p\le\frac{2(K-n)}3.
$$



The restriction $a\ge3$ is essential for the content conclusion.  The
formal $a=1$ interval has $p>K$, so $p$ does not occur in $L_K$ and
the argument forcing $p\mid T_{n,k}$ is unavailable.

## 2. Proof of the exact band theorem

Write



$$
2\ell=ap+s,\qquad0\le s<p.
 \tag{10}
$$



The inequalities (7) imply both statements in (10): the upper inequality
gives $ap\le2\ell$, while



$$
p>\frac{2K}{a+1}>\frac{2\ell}{a+1}
$$



gives $2\ell<(a+1)p$.  Since $a$ and $p$ are odd while $2\ell$ is
even, $s$ is odd.

In the characteristic-$p$ ring
$(\mathbb Z[i]/p\mathbb Z[i])[y]$, Freshman's dream gives



$$
G_{n,k}(y)
 \equiv
 R(y)(1+y^p)^a\pmod p,
 \qquad
 R(y)=P_n(y)(1+y)^s.
 \tag{11}
$$



Put



$$
d=\deg R\le2n+s.
 \tag{12}
$$



The residue of $K=\ell+n$ modulo $p$ is



$$
r=\frac{p+s+2n}{2}.
 \tag{13}
$$



Indeed,



$$
K=\frac{ap+s}{2}+n
 =\frac{a-1}{2}p+r.
$$



The strict lower inequality in (7) is equivalent to



$$
(a+1)p>2K=2\ell+2n=ap+s+2n,
$$



and hence



$$
s+2n<p.
 \tag{14}
$$



Equations (12)--(14) give



$$
0\le d<r<p.
 \tag{15}
$$



The right side of (11) has support only in the intervals



$$
[jp,jp+d],\qquad0\le j\le a.
 \tag{16}
$$



Every exponent congruent to $K$ modulo $p$ has the form $jp+r$.
By (15), it lies strictly after the interval $[jp,jp+d]$ and strictly
before the next interval.  Thus every such coefficient in $G_{n,k}$
vanishes modulo $p$.  Since the exponent defining $C_{mp}$ is
$K+mp$, equation (8) follows.

It remains to pass from coefficient vanishing to $T_{n,k}$.  Equations
(6)--(7), with $a\ge3$, imply



$$
p<K<p^2.
 \tag{17}
$$



Therefore $v_p(L_K)=1$.  If $p\nmid m$, then
$p\mid L_K/m$.  If $m=tp\le K$, then $t<p$, so
$v_p(m)=1$, and (8) gives $p\mid C_m$ and hence $p\mid N_m$.
Every summand in (5) is consequently divisible by $p$, proving
$p\mid T_{n,k}$.  Equation (8) also gives $p\mid C_0$, so
$p\mid h_{n,k}$.  This proves (9).  $\square$

## 3. The disjoint union of bands

Write $a=2j+1$.  The content-producing bands are



$$
\boxed{
 \frac{K}{j+1}<p\le
 \frac{2(K-n)}{2j+1},
 \qquad j\ge1,\qquad p>\sqrt K.}
 \tag{18}
$$



They are pairwise disjoint.  Indeed, the upper endpoint of the
$(j+1)$-st band is strictly less than



$$
\frac{2K}{2j+3}<\frac{K}{j+1},
$$



the lower endpoint of the $j$-th band.

Let $\mathcal P_{n,K}$ be the union of the prime sets in (18), and put



$$
H_{n,K}=\prod_{p\in\mathcal P_{n,K}}p.
 \tag{19}
$$



Theorem 1.1 gives the exact squarefree divisibility



$$
\boxed{H_{n,K}\mid h_{n,k}.}
 \tag{20}
$$



## 4. Asymptotic mass

Suppose



$$
n=o(K).
 \tag{21}
$$



Let



$$
\vartheta(x)=\sum_{p\le x}\log p.
$$



For every fixed $J$, the cutoff $p>\sqrt K$ is eventually automatic
in the first $J$ bands.  The prime number theorem therefore gives their
exact total logarithmic mass as



$$
\begin{aligned}
 \sum_{j=1}^{J}\ \sum_{\substack{p\ \mathrm{prime}\\
                 K/(j+1)<p\le2(K-n)/(2j+1)}}\log p
 &=
 \sum_{j=1}^{J}
 \left[
 \vartheta\left(\frac{2(K-n)}{2j+1}\right)
 -\vartheta\left(\frac{K}{j+1}\right)
 \right]\\
 &=
 K\sum_{j=1}^{J}
 \left(\frac{2}{2j+1}-\frac1{j+1}\right)
 +o_J(K).
 \end{aligned}
 \tag{22}
$$



This is a lower bound for $\log H_{n,K}$.  The bands with $j>J$ are
all supported on primes below $K/(J+1)$, so their total logarithmic mass
is at most



$$
\vartheta\left(\frac{K}{J+1}\right)=O\left(\frac KJ\right).
 \tag{23}
$$



Moreover,



$$
\sum_{j=1}^{\infty}
 \left(\frac{2}{2j+1}-\frac1{j+1}\right)
 =2\log2-1.
 \tag{24}
$$



For completeness, the sum beginning at $j=0$ is $2\log2$, by the
alternating harmonic series, and its $j=0$ term is one.

Letting first $K\to\infty$ and then $J\to\infty$ in (22)--(24)
proves



$$
\boxed{
 \log H_{n,K}
 =(2\log2-1+o(1))K
 \qquad(n=o(K)).}
 \tag{25}
$$



Only the lower bound in (25) is needed below.

## 5. Improved primitive coefficient height

The exact primitive coefficient satisfies



$$
B_{n,k}=\frac{L_KC_0}{h_{n,k}}.
 \tag{26}
$$



The accepted estimates



$$
\log L_K=K+o(K),\qquad
 C_0\le4^K\gamma^n,\qquad
 \gamma=\frac{1+\sqrt2}{2},
 \tag{27}
$$



together with (20) and (25), give



$$
\begin{aligned}
 \log B_{n,k}
 &\le
 \left(1+\log4-(2\log2-1)+o(1)\right)K
 +O(n)\\
 &=\boxed{(2+o(1))K+O(n)}
 \qquad(n=o(K)).
 \end{aligned}
 \tag{28}
$$



The cancellation in the first line is exact because $\log4=2\log2$.

## 6. Fully primitive matching consequence

Let $\Lambda_{n,k}^{\mathrm{prim}}$ be the positive fully primitive form
obtained by minimally matching



$$
E_n=q_ne-p_n>0
$$



with the oriented primitive form
$\mathcal L_{n,k}=A_{n,k}+B_{n,k}\pi>0$.
The exact matching lemma gives



$$
\Lambda_{n,k}^{\mathrm{prim}}
 \ge\frac{q_n\mathcal L_{n,k}}{B_{n,k}^2}.
 \tag{29}
$$



The accepted endpoint estimate gives



$$
q_n\ge n\frac{(2n-1)!}{n!}
 =n\prod_{r=n+1}^{2n-1}r\ge n^n
 \tag{30}
$$



For an exact proof, reverse the alternating endpoint sum for $q_n$: its
first pair is the first quantity in (30), and every remaining pair is
nonnegative.  This is also equation (9) of
`sources/n_dependent_fixed_denominator_kernel_barrier.md`.

The accepted primitive Fourier lower bound is



$$
\begin{aligned}
 \log\mathcal L_{n,k}
 &\ge
 (k-n/2-1)\log2-3\log K\\
 &\quad +(n+1)\left(\frac12\log\frac nk-\log4\right)
 -n\sqrt{\frac nk}-O(n)
 \end{aligned}
 \tag{31}
$$



Equations (28)--(31) give, when $k\asymp n\log n$,



$$
\frac1n\log\Lambda_{n,k}^{\mathrm{prim}}
 \ge
 \left(1-c(4-\log2)+o(1)\right)\log n
 -\frac12\log\log n+O_c(1)
 \tag{32}
$$



uniformly for $k\le c\,n\log n$.

To cover the entire interval $n<k\le c\,n\log n$ uniformly, choose a
fixed small $\delta>0$.  For $k\le\delta n\log n$, the cruder height
$\log B\le(1+\log4+o(1))K+O(n)$ already gives divergence if $\delta$
is sufficiently small.  For $k>\delta n\log n$, one has
$n/K=O(1/\log n)$ uniformly, so (25)--(32) apply.  Hence, for every



$$
c<\frac1{4-\log2},
 \tag{33}
$$





$$
\boxed{
 \Lambda_{n,k}^{\mathrm{prim}}\longrightarrow+\infty
 \quad\text{uniformly for}\quad
 n<k\le c\,n\log n.}
 \tag{34}
$$



The explicit choice



$$
\boxed{n<k\le\frac3{10}n\log n}
 \tag{35}
$$



is valid.  Indeed, the elementary inequality $\log2>2/3$ gives



$$
\frac3{10}(4-\log2)<1.
 \tag{36}
$$



One proof of $\log2>2/3$ is $e^{2/3}<2$: the elementary estimate
$e<11/4$ gives $e^2<121/16<8$.

Together with the separate very-high theorem
$k\ge(3/2)n\log n$, this leaves only



$$
\frac3{10}n\log n<k<\frac32n\log n
 \tag{37}
$$



unresolved for this fully primitive matched Fourier construction.

## 7. Exact finite-grid certificate

The companion script constructs $G_{n,k}$ over the Gaussian integers,
computes $C_0,T_{n,k},h_{n,k}$ exactly, and checks every predicted
coefficient congruence and divisibility on the grid



$$
2\le n\le16\quad(n\ \text{even}),\qquad n\le K\le240.
$$



There are 1,522 parameter pairs with a nonempty band on this grid.  They
give 9,931 forced-prime instances, with odd exponents $a$ from (3)
through (27), and 50,159 separately checked Gaussian coefficient
congruences.  The script also verifies $H_{n,K}\mid h_{n,k}$ in every
one of the 1,522 cases.  All these checks use exact integer arithmetic.
The separate large-$K$ mass calculation is explicitly diagnostic and
uses floating point; it is not part of the proof of (25).

Run

    python -m py_compile scripts/critical_fourier_generalized_odd_prime_bands_certificate.py
    python scripts/critical_fourier_generalized_odd_prime_bands_certificate.py

For a byte-identical rerun, use

    python scripts/critical_fourier_generalized_odd_prime_bands_certificate.py \
      --output /tmp/critical_fourier_generalized_odd_prime_bands_certificate.json
    cmp results/critical_fourier_generalized_odd_prime_bands_certificate.json \
      /tmp/critical_fourier_generalized_odd_prime_bands_certificate.json

This finite computation checks the normalization, endpoints, and passage
from coefficients to content.  The all-parameter result is the proof in
Sections 1--4.

## 8. Limitations

The theorem forces only one copy of each prime in (18); it makes no claim
about higher valuations of $h_{n,k}$.  It also does not bound the odd
final matching content prime by prime.  Its matching consequence works
because the forced content lowers the primitive coefficient
$B_{n,k}=L_KC_0/h_{n,k}$, while the general inequality (28) permits the
worst remaining matching content.

Nothing here proves that $e+\pi$ is algebraic, transcendental, rational,
or irrational.
