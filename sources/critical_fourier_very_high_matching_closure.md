> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fully primitive matching in the very high critical-Fourier region

Date: 2026-08-27.

## 1. Theorem

Let $n>0$ be even and $k>n$, and consider



$$
J_{n,k}=\int_0^1\frac{x^n(1-x)^n}{(1+x^2)^k}\,dx
 =R_{n,k}+Q_{n,k}\pi,\qquad Q_{n,k}>0.
 \tag{1}
$$



When $R_{n,k}\ne0$, write



$$
\frac{R_{n,k}}{Q_{n,k}}=\frac{A_{n,k}}{B_{n,k}},
 \qquad
 \gcd(A_{n,k},B_{n,k})=1,\qquad B_{n,k}>0,
 \tag{2}
$$



and orient the primitive $\pi$-form as



$$
\mathcal L_{n,k}=A_{n,k}+B_{n,k}\pi
 =\frac{B_{n,k}}{Q_{n,k}}J_{n,k}>0.
 \tag{3}
$$



Let



$$
E_n=q_ne-p_n>0,\qquad \gcd(p_n,q_n)=1
 \tag{4}
$$



be the primitive exponential beta form, and minimally match the $e$- and
$\pi$-coefficients of (3) and (4).  After division by the complete integer
content, denote the positive fully primitive matched value by
$\Lambda_{n,k}^{\mathrm{prim}}$.

Then, for every fixed real



$$
c>\frac1{\log2},
 \tag{5}
$$



one has



$$
\boxed{
 \Lambda_{n,k}^{\mathrm{prim}}\longrightarrow+\infty
 \quad\text{uniformly for}\quad
 k\ge c\,n\log n.}
 \tag{6}
$$



In particular, the completely explicit rational choice



$$
\boxed{k\ge\frac32n\log n}
 \tag{7}
$$



is valid.  The branch $R_{n,k}=0$ also diverges after matching and is
included separately below.

Combined with the accepted irrationality-measure theorem in the low region,
this proves divergence of the fully primitive matched critical-Fourier forms
throughout



$$
n<k\le\frac1{35}n\log n
 \qquad\text{and}\qquad
 k\ge\frac32n\log n.
 \tag{8}
$$



It leaves the intermediate strip



$$
\frac1{35}n\log n<k<\frac32n\log n
 \tag{9}
$$



unresolved.  The theorem is a no-go result for this construction and proves
no arithmetic classification of $e+\pi$.

## 2. An elementary upper bound for the beta coefficient

Repeated integration by parts gives



$$
p_n=\sum_{j=0}^n a_{n,j},\qquad
 q_n=(-1)^n\sum_{j=0}^n(-1)^ja_{n,j},
 \qquad
 a_{n,j}=\frac{(n+j)!}{j!(n-j)!}.
 \tag{10}
$$



For $0\le j<n$,



$$
\frac{a_{n,j+1}}{a_{n,j}}
 =\frac{(n+j+1)(n-j)}{j+1}
 \ge2.
 \tag{11}
$$



Indeed, $n-j\ge1$, while



$$
\frac{n+j+1}{j+1}=1+\frac n{j+1}\ge2.
$$



The terms in (10) therefore grow by a factor of at least two.  The triangle
inequality and a geometric sum give



$$
0<q_n\le p_n<2a_{n,n}
 =2\frac{(2n)!}{n!}
 =2\prod_{m=n+1}^{2n}m
 \le2(2n)^n.
 \tag{12}
$$



Consequently,



$$
\boxed{\log q_n\le n\log n+n\log2+\log2.}
 \tag{13}
$$



The coefficient of $n\log n$ in (13) is one.  Retaining that coefficient
is what gives the threshold $1/\log2$ in (5).

## 3. Matching without any odd-content estimate

Put



$$
d=\gcd(q_n,B_{n,k}),\qquad q_n=dq_0,\qquad B_{n,k}=dB_0.
 \tag{14}
$$



Minimal same-sign matching gives the positive raw value



$$
W_{n,k}=B_0E_n+q_0\mathcal L_{n,k}.
 \tag{15}
$$



Let $g$ be its complete integer coefficient content.  The accepted exact
matching lemma proves



$$
g\mid d.
 \tag{16}
$$



After primitive reduction, positivity of both terms in (15) gives



$$
\begin{aligned}
 \Lambda_{n,k}^{\mathrm{prim}}
 &=\frac{W_{n,k}}g\\
 &\ge\frac{q_0\mathcal L_{n,k}}g
 =\frac{q_n\mathcal L_{n,k}}{dg}.
 \end{aligned}
 \tag{17}
$$



No information about the odd prime factors of $d$ or $g$ is needed:
since $d\le q_n$ and $g\le d\le q_n$,



$$
\boxed{
 \Lambda_{n,k}^{\mathrm{prim}}
 \ge\frac{\mathcal L_{n,k}}{q_n}.}
 \tag{18}
$$



This deliberately permits the worst possible matching loss $dg=q_n^2$.

## 4. The high-$k$ lower bound

Put $K=k-1$, $r=n/2$, and



$$
\gamma=\frac{1+\sqrt2}{2}.
 \tag{19}
$$



The accepted all-degree $2$-adic Fourier theorem proves, whenever
$R_{n,k}\ne0$,



$$
\begin{aligned}
 \log\mathcal L_{n,k}
 &\ge
 (k-r-1)\log2-3\log K\\
 &\quad +(n+1)\left(\frac12\log\frac nk-\log4\right)
 -n\sqrt{\frac nk}-\frac n4
 -n\log\gamma-\log\pi.
 \end{aligned}
 \tag{20}
$$



Call the right side $\Phi_n(k)$.  The same theorem proves



$$
\Phi_n'(k)
 \ge
 \log2-\frac3{k-1}-\frac{n+1}{2k}.
 \tag{21}
$$



For every fixed $c>0$, the right side of (21) is positive uniformly for
$k\ge c\,n\log n$ once $n$ is sufficiently large.  Thus the lower bound
is minimized at the left endpoint of any such region.

Combining (13), (18), and (20), and substituting
$k=c\,n\log n$, gives



$$
\begin{aligned}
 \frac1n\log\Lambda_{n,k}^{\mathrm{prim}}
 &\ge
 (c\log2-1)\log n
 -\frac12\log\log n+O_c(1).
 \end{aligned}
 \tag{22}
$$



The $O_c(1)$ term contains only fixed multiples of
$\log2,\log c,\log\gamma$, and constants; the terms
$3\log K/n$ and $\sqrt{n/k}$ tend to zero.  If $c\log2>1$, the right
side of (22) tends to $+\infty$.  Monotonicity (21) then proves the
uniform assertion (6), including sequences for which $k$ grows
arbitrarily faster than $n\log n$.

For the explicit choice $c=3/2$, it remains only to certify



$$
\frac32\log2>1.
 \tag{23}
$$



Equivalently, $2^{3/2}>e$.  The elementary bounds



$$
e<\frac{11}{4},\qquad
 2\sqrt2>\frac{11}{4}
 \tag{24}
$$



prove this.  For example,



$$
e=\sum_{j=0}^{\infty}\frac1{j!}
 <1+1+\frac12+\frac14=\frac{11}{4},
 \tag{25}
$$



because $j!\ge2\cdot3^{j-2}$ for $j\ge2$, with strict inequality for
some $j$; and $2\sqrt2>11/4$ follows after squaring from
$8>121/16$.  This proves (7).

## 5. The zero rational-coordinate branch

If $R_{n,k}=0$, lowest terms give



$$
(A_{n,k},B_{n,k})=(0,1),\qquad \mathcal L_{n,k}=\pi.
$$



Here $d=g=1$, and minimal matching is already primitive:



$$
E_n+q_n\pi=q_n(e+\pi)-p_n.
 \tag{26}
$$



The accepted lower bound $q_n\ge n^n$ gives



$$
E_n+q_n\pi\ge\pi n^n\longrightarrow+\infty.
 \tag{27}
$$



Thus no assertion that $R_{n,k}$ is always nonzero is required.

## 6. Exact scope

The proof uses the worst-case inequalities $d,g\le q_n$, so it is
unaffected by the known examples in which the odd final content contains
several primes, repeated prime powers, or primes larger than $K$.  Its
constant $1/\log2$ is the natural threshold of this particular
worst-content comparison: the Fourier lower bound supplies
$k\log2$, while the elementary beta upper bound costs $n\log n$.

Improving the theorem into the strip (9) still requires genuinely new
control of $dg$, or a stronger lower bound for the primitive
$\pi$-component.  Nothing here proves that $e+\pi$ is algebraic,
transcendental, rational, or irrational.
