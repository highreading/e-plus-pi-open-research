> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A local $p$-adic zero-run no-go theorem

Checked: 2026-08-27 UTC.

## 1. Verdict

The currently proved local properties of the normalized Bessel index
interpolation do not, by themselves, imply any upper bound on terminal
zero-run length.  More precisely, the following collection of properties
is compatible with arbitrarily prescribed zero gaps, including gaps large
enough to produce the full $n\log n$ valuation scale:

1. $1$-Lipschitz $p$-adic analyticity;
2. reflection symmetry under $x\mapsto-x-1$;
3. a simple ordinary root;
4. periodicity modulo every $p^a$; and
5. an exact affine lift law modulo $p^{2a}$.

The proof is an explicit comparison family.  It is not a construction of
long runs for the Bessel root.  Its rigorous consequence is a method
barrier: Hensel simplicity, reflection, and the exponent-doubling/affine
lift theorem cannot alone prove the desired sublinear terminal-run bound.
A successful proof must use a genuinely global input specific to the
Bessel recurrence, such as a rational-coefficient height theorem or an
effective $p$-adic irrationality measure for its special root.

## 2. Arbitrary-gap comparison theorem

Let $p$ be an odd prime.  Choose



$$
r\in\{0,\ldots,p-1\},
 \qquad
 2r+1\not\equiv0\pmod p,
\tag{1}
$$



and any strictly increasing sequence of positive integers



$$
N_1<N_2<N_3<\cdots.
\tag{2}
$$



Define



$$
\rho=r+\sum_{j\geq1}p^{N_j}\in\mathbf Z_p
\tag{3}
$$



and



$$
F_\rho(x)=x(x+1)-\rho(\rho+1)
          =(x-\rho)(x+\rho+1).
\tag{4}
$$



Then $F_\rho$ is a polynomial over $\mathbf Z_p$, and



$$
F_\rho(-x-1)=F_\rho(x).
\tag{5}
$$



Its root at $x=\rho$ is ordinary because



$$
F_\rho'(\rho)=2\rho+1\equiv2r+1\not\equiv0\pmod p.
\tag{6}
$$



For every $a\geq1$, $M=p^a$, and $t\in\mathbf Z$, the exact
translation identity is



$$
F_\rho(x+tM)
 =F_\rho(x)+tM(2x+1)+t^2M^2.
\tag{7}
$$



Consequently,



$$
F_\rho(x+M)\equiv F_\rho(x)\pmod M
\tag{8}
$$



and



$$
F_\rho(x+2M)-2F_\rho(x+M)+F_\rho(x)=2M^2.
\tag{9}
$$



In particular, modulo $M^2$, the values on a lift fiber are exactly
affine in $t$.  This is at least as strong as the affine conclusion used
to lift an ordinary Bessel root.

Now put



$$
n_j=r+\sum_{i=1}^{j}p^{N_i}.
\tag{10}
$$



The two factors in $(4)$ give



$$
\begin{aligned}
 \rho-n_j
 &=p^{N_{j+1}}
   \left(1+\sum_{i\geq j+2}p^{N_i-N_{j+1}}\right),\\
 n_j+\rho+1
 &\equiv2r+1\not\equiv0\pmod p.
 \end{aligned}
\tag{11}
$$



Therefore



$$
\boxed{v_p(F_\rho(n_j))=N_{j+1}.}
\tag{12}
$$



The least representative $n_j$ ends with its last nonzero digit in
position $N_j$, while the next nonzero root digit is in position
$N_{j+1}$.  Hence its terminal zero-run length is exactly



$$
\boxed{N_{j+1}-N_j-1.}
\tag{13}
$$



Because the sequence in $(2)$ was arbitrary, no bound on this length
can follow from properties $(5)$--$(9)$.

## 3. A main-scale choice

To match the scale of the live Bessel obstruction, choose recursively



$$
N_{j+1}=N_jp^{N_j}.
\tag{14}
$$



The gaps then tend rapidly to infinity, and



$$
n_j=p^{N_j}(1+o(1)),
\qquad
 \log n_j=N_j\log p+o(1).
\tag{15}
$$



Equations $(12)$, $(14)$, and $(15)$ give



$$
\boxed{
 {v_p(F_\rho(n_j))\log p\over n_j\log n_j}\longrightarrow1.}
\tag{16}
$$



Thus even the full forbidden main scale is compatible with a simple,
symmetric, locally analytic root and exact affine lifting.

This comparison also explains why a generic theorem about ordinary
$p$-adic roots cannot solve the Bessel problem.  The missing theorem
must distinguish the actual interpolation



$$
f_p(x)=\sum_{j\geq0}A_j\binom{x}{j}
\tag{17}
$$



from $F_\rho$ through global arithmetic data.  The comparison coefficient
$-\rho(\rho+1)$ is generally a nonrational $p$-adic integer; no rational
or integral global-height claim is made for it.

## 4. Exact sufficient target for the Bessel root

For a Bessel root path, let $L_{p,n}$ denote the number of consecutive
zero lift digits immediately above the base-$p$ expansion of $n$.
If $N\leq n<2N$ and $p\leq CN\log N$, then the exact digit bookkeeping
gives



$$
v_p(q_n)\log p
 \leq \log(2N)+\log p+L_{p,n}\log p.
\tag{18}
$$



Hence the genuinely sufficient uniform theorem is



$$
\boxed{
 \max_{\substack{N\leq n<2N\\p\leq CN\log N}}
 L_{p,n}\log p=o(N\log N).}
\tag{19}
$$



The simpler condition $L_{p,n}=o(N)$, uniformly over all ordinary and
surviving singular paths in this range, implies $(19)$.  For one fixed
prime $p$, a finite irrationality exponent



$$
p^{v_p(q_n)}\leq C_p n^{\mu_p}
\tag{20}
$$



would be more than sufficient, but constants depending arbitrarily on
$p$ do not yield the uniform statement $(19)$.

Neither $(19)$ nor $(20)$ is proved here.  The theorem of this note is
the exact no-go statement $(1)$--$(16)$, which identifies what a future
proof must add.

## 5. Certificate and scope

The companion script

    scripts/bessel_padic_local_zero_run_no_go_certificate.py

checks $(5)$, $(7)$, $(9)$, and $(12)$--$(13)$ with exact modular
integer arithmetic in four finite examples.  The all-parameter proof is the
displayed factorization and translation calculation; the finite checks are
regression tests only.

Nothing in this note proves a long-run theorem for the Bessel root, nor
irrationality or transcendence of $e+\pi$.
