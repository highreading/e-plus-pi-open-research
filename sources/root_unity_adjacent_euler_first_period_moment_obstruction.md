> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Adjacent first-period Euler primes have full finite-field moment complexity

## 1. Result and scope

Write the secant Euler numbers as



$$
\operatorname {sech}t
       =\sum_{n\geq0}E_n\frac {t^n}{n!},
       \qquad E_0=1,\quad E_2=-1.
$$



For $N\geq1$, the still-uncontrolled squarefree first-period product is



$$
{\cal P}_N=
 \prod_{\substack{p>2N+2\\ p\ {\rm prime}\\
                   p\mid E_{2N},\ p\mid E_{2N+2}}}p.          \tag{1}
$$



This note gives an exact all-prime finite-field model for every factor in
(1).  If $p$ is odd and $r=(p-1)/2$, then the Euler sequence modulo
$p$ is a moment sequence on all $r$ quadratic residues, with every
weight nonzero.  Its minimal constant-coefficient linear recurrence has
order exactly $r$.  The unique polynomial which interpolates the
weights has degree exactly $r-1$, and its square is $4$ in the split
algebra



$$
\mathbb F_p[X]/(X^r-1).                  \tag{2}
$$



Thus the canonical recurrence, low-degree interpolation/resultant, and
moment-rank routes do not compress an adjacent first-period pair to
bounded effective dimension.  This is an obstruction theorem for those
specific routes.  It is not an upper bound for ${\cal P}_N$, not a
claim about arbitrary nonlinear or arithmetic couplings, and not a
classification of $e+\pi$.

## 2. The primary power-sum congruence and the paired moment

Cosgrave and Dilcher record the congruence



$$
E_m\equiv\sum_{j=0}^{p-1}(-1)^j(2j+1)^m\pmod p,
 \qquad m\geq1,                                               \tag{3}
$$



as the prime specialization of their equation (2.3).  Their convention
for Euler numbers is exactly the secant convention above.

Fix $n\geq1$, put



$$
r=\frac {p-1}{2},\qquad
 a_j=2j+1,\qquad x_j=a_j^2,\qquad
 w_j=2(-1)^j
 \quad(0\leq j<r),                                           \tag{4}
$$



and interpret these quantities in $\mathbb F_p$.  Pair in (3) the
terms indexed by $j$ and $p-1-j$.  Their signs agree because $p-1$
is even, while their bases are negatives of one another modulo $p$.
The unpaired middle term $j=r$ has base $p$, hence is zero for the
positive exponent $2n$.  Therefore



$$
\boxed{\quad
 E_{2n}\equiv M_p(n):=
       \sum_{j=0}^{r-1}w_jx_j^n
       =2\sum_{j=0}^{r-1}(-1)^j(2j+1)^{2n}\pmod p .
 \quad}                                                       \tag{5}
$$



This proves both the sign and the factor $2$ in the normalization.
The definition of $M_p(n)$ also makes sense at $n=0$, but (5) is
asserted only for $n\geq1$, as in the primary congruence.

The support in (5) is exactly the set of nonzero quadratic residues.
Indeed, the $a_j$ are the odd integers from $1$ through $p-2$.
If $a_i^2\equiv a_j^2\pmod p$, then $p$ divides either
$a_i-a_j$ or $a_i+a_j$.  The first alternative gives $i=j$.
The second is impossible: $a_i+a_j$ is even, whereas its only possible
multiple of $p$ in the relevant range would be the odd integer $p$.
Thus the $r$ squares are distinct.  There are exactly $r$ nonzero
quadratic residues, so they exhaust that group.  Also



$$
w_j\neq0\pmod p                     \tag{6}
$$



for every $j$, because $p$ is odd.

## 3. Exact linear complexity

Since the $x_j$ are precisely the roots of $Z^r-1$ in
$\mathbb F_p$,



$$
\prod_{j=0}^{r-1}(Z-x_j)=Z^r-1.             \tag{7}
$$



Consequently $M_p(n+r)=M_p(n)$.  This period relation has minimal
constant-coefficient order exactly $r$.

To prove minimality, suppose a polynomial $Q(Z)\in\mathbb F_p[Z]$
annihilates the moment sequence on a full tail:



$$
\sum_\ell q_\ell M_p(n+\ell)=0
              \quad\hbox{for every }n\geq n_0.               \tag{8}
$$



For $n=n_0,\ldots,n_0+r-1$, substitution of (5) into (8) gives



$$
\sum_{j=0}^{r-1}
       \bigl(w_jx_j^{n_0}Q(x_j)\bigr)x_j^{n-n_0}=0.           \tag{9}
$$



The square Vandermonde matrix on the distinct $x_j$ is invertible.
Every factor $w_jx_j^{n_0}$ is nonzero, so (9) forces
$Q(x_j)=0$ for all $j$.  Hence either $Q=0$, or



$$
\deg Q\geq r.                       \tag{10}
$$



Equivalently, the reduced rational generating function



$$
\sum_{n\geq0}M_p(n)T^n
      =\sum_{j=0}^{r-1}\frac {w_j}{1-x_jT}                   \tag{11}
$$



has denominator exactly $1-T^r$: none of its $r$ distinct poles can
cancel because every residue weight is nonzero.

The qualification in (10) is essential.  It is a theorem about
constant-coefficient linear recurrences, even if they are required only
on a tail.  It does not exclude a nonlinear recurrence, coefficients
depending on $n$ or $p$, a modular-form identity, a class-number
coupling, or another arithmetic construction not represented by (8).

## 4. The exact sign interpolant

Let $W_p(X)$ be the unique polynomial of degree less than $r$ such
that



$$
W_p(x_j)=w_j.                       \tag{12}
$$



Because every value in (12) is $2$ or $-2$,



$$
W_p(X)^2\equiv4\pmod {X^r-1}.              \tag{13}
$$



Write $W_p(X)=\sum_{a=0}^{r-1}c_aX^a$, and extend $M_p$
periodically to integer arguments.  Fourier inversion on the cyclic
group of quadratic residues gives



$$
c_a=r^{-1}M_p(-a),\qquad0\leq a<r.          \tag{14}
$$



For $1\leq k\leq r$, take $a=r-k$.  Equations (5) and (14), including
the valid positive exponent $k=r$, yield



$$
c_{r-k}=r^{-1}E_{2k}=-2E_{2k}\pmod p,      \tag{15}
$$



because $r=(p-1)/2\equiv-1/2\pmod p$.  Hence the interpolant has the
explicit Euler-coefficient form



$$
\boxed{\quad
 W_p(X)=-2\sum_{k=1}^{r}E_{2k}X^{r-k}\quad\hbox{in }
 \mathbb F_p[X].
 \quad}                                                       \tag{16}
$$



In particular, $E_2=-1$ makes the coefficient of $X^{r-1}$ equal to
$2$.  Therefore



$$
\deg W_p=r-1.                       \tag{17}
$$



There is also a proof needing no Fourier coefficient beyond (13).
For $p\geq5$, the values $w_0=2$ and $w_1=-2$ show that $W_p$
is not constant.  If $2\deg W_p<r$, divisibility in (13) would force
the polynomial identity $W_p^2=4$, hence $W_p=2$ or $W_p=-2$.
Thus



$$
\deg W_p\geq\left\lceil\frac r2\right\rceil,
                                                                    \tag{18}
$$



with (17) giving the sharp exact value.  Formula (17) rules out a
bounded-degree polynomial encoding of these deterministic signs; it does
not rule out every conceivable eliminant.

The congruence (13) by itself is highly nonrigid.  Since $X^r-1$ splits
into $r$ distinct linear factors, the Chinese remainder theorem shows
that (2) has exactly $2^r$ square roots of $4$, one for each assignment
of signs to the $r$ roots.  Equation (12) selects one of them.

If $C_p(X)$ is the degree-less-than-$r$ representative of
$W_p(X^{-1})$ in (2), then (15) says



$$
C_p(X)=-2E_{2r}-2\sum_{k=1}^{r-1}E_{2k}X^k,\qquad
 C_p(X)^2\equiv4\pmod {X^r-1}.                               \tag{19}
$$



Thus, away from the period endpoint, simultaneous divisibility of two
adjacent Euler numbers says exactly that two adjacent Fourier
coefficients of this particular square root vanish.

## 5. The full moment determinant does not drop rank

For any integer $s$, form the $r$-by-$r$ Hankel matrix



$$
{\cal H}_{p,s}=
             \bigl(M_p(s+a+b)\bigr)_{0\leq a,b<r}.            \tag{20}
$$



With $V=(x_j^a)_{0\leq a,j<r}$, one has the exact factorization



$$
{\cal H}_{p,s}
   =V\operatorname {diag}(w_jx_j^s)_{j=0}^{r-1}V^{\mathsf T},
\qquad
 \det{\cal H}_{p,s}
   =\left(\prod_jw_jx_j^s\right)
      \prod_{i<j}(x_j-x_i)^2\neq0.                            \tag{21}
$$



Even if $M_p(N)=M_p(N+1)=0$, taking $s=N$ merely makes the
upper-left entry and its two adjacent off-diagonal entries zero.  The
full moment matrix remains nonsingular.  Therefore the obvious
Vandermonde or large-sieve-style rank determinant produces no rank
defect divisible by $p$.  Detecting the complete support uses dimension
$r$, which depends on $p$ and can be arbitrarily larger than $N$.
This is a precise failure of this canonical determinant, not an
impossibility theorem for all large-sieve or product arguments.

## 6. Consequences for primes beyond the cutoff

By (5),



$$
p\mid E_{2N},E_{2N+2}
 \quad\Longleftrightarrow\quad
 M_p(N)=M_p(N+1)=0.                                         \tag{22}
$$



If $p>2N+2$, then $r\geq N+1$.  There is one endpoint possibility:
$p=2N+3$, so $r=N+1$.  The period relation and the direct evaluation
of the middle term give



$$
E_{p-1}\equiv M_p(r)=M_p(0)
              =1-(-1)^r\pmod p.                             \tag{23}
$$



Consequently this unique possible endpoint factor occurs exactly when



$$
p=2N+3\ \hbox{is prime},\qquad
 p\equiv1\pmod4,\qquad p\mid E_{p-3}.                        \tag{24}
$$



Its contribution to (1) is at most $2N+3$, hence has logarithm
$O(\log N)$.

For every strict first-period prime $p>2N+3$, one has $r\geq N+2$.
The two zeros in (22) are the vanishing coefficients



$$
[X^{r-N}]W_p=[X^{r-N-1}]W_p=0,                 \tag{25}
$$



or, equivalently,



$$
[X^N]C_p=[X^{N+1}]C_p=0.                \tag{26}
$$



The exact recurrence order is $r>N+1$, the exact interpolant degree is
$r-1$, and the full moment determinant has dimension $r$ and is
nonzero.  A low-degree resultant in the exponent variable which factors
through this recurrence or interpolant therefore cannot have bounded
effective dimension uniformly in $p$.

There is no uniform multiplicative-character shortcut either in the
all-prime statement.  For example, if $p\equiv3\pmod4$ and $p\geq7$,
then the quadratic-residue group has odd order $r$, so every homomorphism
from it to $\{1,-1\}$ is trivial.  The normalized weights
$w_j/2=(-1)^j$ take both signs and therefore are not such a character.
For $p\equiv1\pmod4$, this note makes no universal classification of
the weight function; (13) is the only all-prime square-root identity
being used.

## 7. The interior seed and the quantitative obstruction

The frozen exact adjacent-irregular seed is



$$
N=1643,\qquad p=151483,\qquad
                 p\mid E_{3286},E_{3288}.                   \tag{27}
$$



Here



$$
r=75741,\qquad
 \deg W_p=75740,\qquad
 \left\lceil r/2\right\rceil=37871,                          \tag{28}
$$



and the zero coefficients in (25) have exponents $74098$ and $74097$.
Moreover $p\equiv3\pmod4$, so the normalized alternating weights are
not a multiplicative character of the quadratic-residue group.  Direct
modular power sums and the independent secant recurrence both give



$$
M_p(1643)=M_p(1644)=0.              \tag{29}
$$



This one actual seed proves that two adjacent zero moments, full support,
and the nonsingular determinant (21) are mutually compatible.  It is not
extrapolated to a density or independence assertion.

The elementary bound remains only



$$
{\cal P}_N\mid\gcd(E_{2N},E_{2N+2}),\qquad
               \log{\cal P}_N\leq2N\log N+O(N).              \tag{30}
$$



Indeed, the exact beta-value formula



$$
|E_{2N}|=\frac {4^{N+1}(2N)!}{\pi^{2N+1}}\,
                     \beta(2N+1)
$$



and Stirling's formula give
$\log|E_{2N}|=2N\log N+O(N)$.

Nothing above improves (30) to $O(N)$ or $o(N\log N)$.  A successful
argument still needs a new global lemma coupling the deterministic
square roots $W_p$ as $p$ varies, or another arithmetic construction
which does not pass through the full order-$r$ moment model.  In
particular, one would need an estimate of the form



$$
\sum_{\substack{p>2N+3\\p\mid E_{2N},E_{2N+2}}}\log p
                         =o(N\log N),                        \tag{31}
$$



and neither (13), (17), nor (21) supplies it.

## 8. Replay and logical boundary

From the research directory run

    python3 scripts/root_unity_adjacent_euler_first_period_moment_certificate.py
    sha256sum -c results/root_unity_adjacent_euler_first_period_moment_hashes.sha256

The replay checks the power-sum normalization, support, exact Fourier
interpolants, cyclic square identity, minimal-polynomial identity, and
Hankel factorization on a declared prime grid.  At the full seed
$p=151483$, it independently checks primality, the paired and unpaired
power sums, and the secant recurrence modulo $p$.  Finite checks are
certificates of the displayed normalizations and seed only; the
all-parameter theorems are the proofs above.

## 9. Primary reference

J. B. Cosgrave and K. Dilcher, *On a congruence of Emma Lehmer related
to Euler numbers*, Acta Arith. **161** (2013), 47--67,
<https://www.impan.pl/shop/publication/transaction/download/product/82378>.
Equation (2.3) is precisely (3); equations (2.1)--(2.2) give the associated
Euler--Kummer congruences.
