> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A prime-number-theorem extension of the fully matched critical-Fourier barrier

Date: 2026-08-27.

## 1. Theorem

Let $n>0$ be even and $k>n$.  In the accepted critical-Fourier family,
write



$$
J_{n,k}=R_{n,k}+Q_{n,k}\pi,\qquad Q_{n,k}>0.
 \tag{1}
$$



When $R_{n,k}\ne0$, reduce



$$
\frac{R_{n,k}}{Q_{n,k}}=\frac{A_{n,k}}{B_{n,k}},
 \qquad
 \gcd(A_{n,k},B_{n,k})=1,\qquad B_{n,k}>0,
 \tag{2}
$$



and put



$$
\mathcal L_{n,k}=A_{n,k}+B_{n,k}\pi>0.
 \tag{3}
$$



Minimally match this primitive $\pi$-form with the primitive beta form



$$
E_n=q_ne-p_n>0,\qquad \gcd(p_n,q_n)=1,
 \tag{4}
$$



and divide by the complete integer coefficient content.  Denote the
resulting positive fully primitive value by
$\Lambda_{n,k}^{\mathrm{prim}}$.

Then, for every fixed real number



$$
0<c<\frac1{2+3\log2},
 \tag{5}
$$



one has



$$
\boxed{
 \Lambda_{n,k}^{\mathrm{prim}}\longrightarrow+\infty
 \quad\text{uniformly for}\quad
 n<k\le c\,n\log n.}
 \tag{6}
$$



The explicit rational choice



$$
\boxed{n<k\le\frac6{25}n\log n}
 \tag{7}
$$



is valid.  Together with the separate very-high matching theorem
$k\ge(3/2)n\log n$, this leaves only



$$
\frac6{25}n\log n<k<\frac32n\log n
 \tag{8}
$$



unresolved for the fully primitive matched Fourier family.

This improves the earlier explicit low constant $1/35$.  It uses the prime
number theorem only to estimate a least common multiple; it does not use an
irrationality measure for $\pi$.  It is a no-go theorem for this
construction and proves no arithmetic classification of $e+\pi$.

## 2. Exact matching inequality

Put



$$
d=\gcd(q_n,B_{n,k}),\qquad
 q_n=dq_0,\qquad B_{n,k}=dB_0.
 \tag{9}
$$



The same-sign minimally matched raw value is



$$
W_{n,k}=B_0E_n+q_0\mathcal L_{n,k}>0.
 \tag{10}
$$



If $g$ is its complete integer coefficient content, the accepted exact
matching lemma gives $g\mid d$.  Therefore



$$
\begin{aligned}
 \Lambda_{n,k}^{\mathrm{prim}}
 &=\frac{W_{n,k}}g\\
 &\ge\frac{q_0\mathcal L_{n,k}}g
 =\frac{q_n\mathcal L_{n,k}}{dg}.
 \end{aligned}
 \tag{11}
$$



Both $d$ and $g$ divide, and hence are at most, $B_{n,k}$.  Thus



$$
\boxed{
 \Lambda_{n,k}^{\mathrm{prim}}
 \ge\frac{q_n\mathcal L_{n,k}}{B_{n,k}^2}.}
 \tag{12}
$$



This estimate remains valid without any control of the odd prime factors of
$d$ or $g$.

## 3. Fourier height with the sharp exponential scale of the lcm

Put



$$
K=k-1,\qquad L_K=\operatorname{lcm}(1,\ldots,K),\qquad
 \gamma=\frac{1+\sqrt2}{2}.
 \tag{13}
$$



The exact Fourier reduction gives



$$
B_{n,k}\le L_KC_0.
 \tag{14}
$$



The accepted central-coefficient estimate is



$$
C_0\le4^K\gamma^n.
 \tag{15}
$$



The prime number theorem in its equivalent Chebyshev form says



$$
\log L_K=\psi(K)=K+o(K).
 \tag{16}
$$



Equations (14)--(16) give the uniform height estimate



$$
\boxed{
 \log B_{n,k}
 \le(1+\log4+o(1))K+n\log\gamma.}
 \tag{17}
$$



Here the $o(1)$ depends only on $K$ and tends to zero as $K\to\infty$;
it is therefore uniform over all pairs with $K\ge n\to\infty$.

## 4. Combining height and the primitive-component lower bound

The primitive beta coefficient satisfies the accepted elementary lower bound



$$
q_n\ge n^n.
 \tag{18}
$$



For an exact proof pointer, equation (9) of
sources/n_dependent_fixed_denominator_kernel_barrier.md reverses the
alternating endpoint sum in (4) and gives, for every positive even $n$,



$$
q_n\ge\frac{n(2n-1)!}{n!}
 =n\prod_{j=n+1}^{2n-1}j
 \ge n^n.
 \tag{18a}
$$



The all-degree $2$-adic Fourier theorem gives, for $R_{n,k}\ne0$,



$$
\begin{aligned}
 \log\mathcal L_{n,k}
 &\ge
 (k-n/2-1)\log2-3\log K\\
 &\quad +(n+1)\left(\frac12\log\frac nk-\log4\right)
 -n\sqrt{\frac nk}-\frac n4
 -n\log\gamma-\log\pi.
 \end{aligned}
 \tag{19}
$$



For all sufficiently large $n$, this inequality is valid uniformly for
every $k>n$: the underlying divisor exponent



$$
k-\frac n2-3\lfloor\log_2K\rfloor-1
$$



is then positive, already at $k=n+1$, and increases thereafter.

Combining (12), (17), (18), and (19) gives



$$
\begin{aligned}
 \log\Lambda_{n,k}^{\mathrm{prim}}
 &\ge n\log n
 +(k-n/2-1)\log2\\
 &\quad-2(1+\log4+o(1))K
 +\frac{n+1}{2}\log\frac nk
 +O(n+\log K).
 \end{aligned}
 \tag{20}
$$



The $O(n+\log K)$ is uniform; it absorbs the fixed
$\log4,\log\gamma,\log\pi$ terms and
$-n\sqrt{n/k}\ge-n$.

Since $\log4=2\log2$, the coefficient lost per unit of $k$ in (20) is



$$
2(1+\log4)-\log2=2+3\log2.
 \tag{21}
$$



Uniformly for $n<k\le c\,n\log n$, equation (20) therefore gives



$$
\frac1n\log\Lambda_{n,k}^{\mathrm{prim}}
 \ge
 \left(1-c(2+3\log2)+o(1)\right)\log n
 -\frac12\log\log n+O_c(1).
 \tag{22}
$$



To justify using the upper endpoint uniformly, note that every
$k$-dependent term omitted from the leading coefficient is bounded below
throughout the interval by its value at $c\,n\log n$, except
$-n\sqrt{n/k}$, which is bounded below by $-n$.  Also,
the $o(1)$ in (17) is uniform because $K\ge n\to\infty$.

If $c(2+3\log2)<1$, the right side of (22) tends to $+\infty$.  This
proves (6).

For $c=6/25$, the already certified elementary inequality
$\log2<7/10$ gives



$$
\frac6{25}(2+3\log2)
 <\frac6{25}\frac{41}{10}
 =\frac{123}{125}<1.
 \tag{23}
$$



The fixed margin $2/125$ absorbs the $o(1)$ in (22), proving (7).

## 5. The zero rational-coordinate branch

If $R_{n,k}=0$, lowest terms give



$$
(A_{n,k},B_{n,k})=(0,1),\qquad\mathcal L_{n,k}=\pi.
$$



Minimal matching is already primitive:



$$
E_n+q_n\pi=q_n(e+\pi)-p_n.
 \tag{24}
$$



By (18), its value is at least $\pi n^n$, so it diverges.  Thus the theorem
does not require a proof that $R_{n,k}$ is always nonzero.

## 6. Limitation

The improvement comes from combining three independent exact scales:

* $q_n\ge n^n$;
* the primitive-component factor $2^k$ in (19);
* $\log L_K\sim K$ and $C_0\le4^K\gamma^n$.

The resulting denominator cost is $2+3\log2$ per unit of $k$, which
explains the threshold in (5).  Entering the remaining strip (8) requires a
better upper bound on the actual primitive coefficient $B_{n,k}$, a
nontrivial bound on $dg$, or a stronger primitive-component estimate.
Nothing in this note proves that $e+\pi$ is algebraic, transcendental,
rational, or irrational.
