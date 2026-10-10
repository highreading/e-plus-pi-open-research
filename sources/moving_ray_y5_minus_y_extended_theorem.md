> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Slope-10 prime rays through intercept 57

Date: 2026-08-28

## 1. Theorem

Let $m\geq1$, let $L_0,L_1$ be the adjacent mixed-cubic logarithmic
residues, and suppose



$$
p=10m+b
$$



is prime. For every odd $b\leq57$ with $\gcd(b,10)=1$,



$$
\boxed{(L_0,L_1)\not\equiv(0,0)\pmod p.}           \tag{1.1}
$$



The earlier moving-ray package proved the cases



$$
b=1,3,7,9,11,13,17,19,21,23.
$$



The new theorem-grade cases are



$$
\boxed{b=27,29,31,33,37,39,41,43,47,49,51,53,57.} \tag{1.2}
$$



Since every listed $b$ is coprime to 10, each line contains infinitely
many prime instances by Dirichlet's theorem.

## 2. Closed determinant formula in the intercept

Retain



$$
F(y)=y^5-y,\qquad W(y)=(1-y)(1+y^2),
$$



and, on $p=10m+b$, put $n=4m+b$. For



$$
\rho_j=\operatorname {Res}_{y=1}y^jF(y)^{-n}\,dy,
$$



the exact derivative recurrence is



$$
(k+5-3b)\rho_{k+4}+(4m+b-1-k)\rho_k=0\pmod p.     \tag{2.1}
$$



The two residue functionals are



$$
\Phi_0=\operatorname {Res}_{y=1}W^{b-1}F^{-n}\,dy,
 \qquad
 \Phi_1=\operatorname {Res}_{y=1}W^{b-2}F^{-n}\,dy,
 \qquad L_s=4\Phi_s.                               \tag{2.2}
$$



The preceding package reduces all residues needed in (2.2) to two states.
The anchored class is



$$
c_E\equiv b-1\pmod4,\qquad c_E\in\{0,2\}.
$$



The other class is $c_O=1$ for even $m$, and $c_O=3$ for odd $m$.

There is a closed finite formula for the ray determinant. Write



$$
w_{q,j}=[y^j]W(y)^q
 =(-1)^j\sum_{v=0}^{\lfloor j/2\rfloor}
 \binom qv\binom q{j-2v},                         \tag{2.3}
$$



where an out-of-range binomial coefficient is zero. For
$c\in\{0,1,2,3\}$, define



$$
R_{c,r}(b)=
 \frac{\left(\dfrac{5c+5-3b}{20}\right)_r}
      {\left(\dfrac{c+5-3b}{4}\right)_r},          \tag{2.4}
$$





$$
S_c(q;b)=
 \sum_{\substack{r\geq0\\c+4r\leq3q}}
 w_{q,c+4r}R_{c,r}(b).                            \tag{2.5}
$$



Then the exact value of the two-state determinant at the formal ray point
$m=-b/10$ is



$$
\boxed{
 D_{b,\epsilon}=
 S_{c_E}(b-1;b)S_{c_O}(b-2;b)
 -S_{c_O}(b-1;b)S_{c_E}(b-2;b),}                  \tag{2.6}
$$



with $c_O=1$ for $\epsilon=0$ and $c_O=3$ for $\epsilon=1$.

To prove (2.4), iterate (2.1) in one class and then substitute
$m=-b/10$:



$$
\frac{\rho_{c+4r}}{\rho_c}
 =\prod_{j=0}^{r-1}
 \frac{-\left(3b/5-1-c-4j\right)}
      {c+4j+5-3b}
 =R_{c,r}(b).                                     \tag{2.7}
$$



The denominator in (2.4) does not vanish for $c=c_E,c_O$: its only
singular class is $3b-5\pmod4$, the even class opposite $c_E$.
Equations (2.3)--(2.7) are therefore an exact terminating
hypergeometric/Pochhammer classification:

* $D_{b,\epsilon}=0$ is a genuine determinant-zero intercept;
* $D_{b,\epsilon}\ne0$ leaves only the prime divisors of one fixed
  integer ray constant as possible exceptions.

No uniform proof that (2.6) is nonzero for every admissible odd $b$ is
known.

## 3. Sparse Cartier formula for the actual two states

The determinant only identifies candidate primes. The actual ratio of the
two states is also explicit. Put



$$
N=p-n=6m,\qquad
 H(x)=4+10x+10x^2+5x^3+x^4,
$$



so that $F(1+x)=xH(x)$. Since $H(x)^p\equiv4\pmod{x^p}$,



$$
4\rho_j=[x^{n-1}](1+x)^jH(x)^N
         =[x^{p-1}](1+x)^jF(1+x)^N.               \tag{3.1}
$$



Expanding the sparse polynomial in the coordinate $y=1+x$ gives



$$
y^jF(y)^N
 =\sum_{a=0}^N(-1)^{N-a}\binom Na\,y^{j+N+4a}.    \tag{3.2}
$$



For every exponent occurring here, Lucas's theorem gives



$$
[x^{p-1}](1+x)^d=\binom d{p-1}\equiv
 \begin{cases}
 1,&d\equiv p-1\pmod p,\\
 0,&d\not\equiv p-1\pmod p.
 \end{cases}                                      \tag{3.3}
$$



Consequently



$$
\boxed{
 4\rho_j=
 \sum_{\substack{0\leq a\leq6m\\
                  4a\equiv n-j-1\pmod p}}
 (-1)^{6m-a}\binom{6m}{a}\pmod p.}                \tag{3.4}
$$



For the two surviving classes there is exactly one term:



$$
a_E=\frac{n-c_E-1}{4},\qquad
 a_O=\frac{n-c_O-1+p}{4},                         \tag{3.5}
$$





$$
\boxed{
 4E=(-1)^{6m-a_E}\binom{6m}{a_E},\qquad
 4O=(-1)^{6m-a_O}\binom{6m}{a_O}\pmod p.}          \tag{3.6}
$$



Thus the final candidate test is a completely explicit pair of binomial
congruences, not an extrapolation from small $m$.

## 4. Exact factorization and candidate replays

For every $b$ in (1.2) and both parities, the companion certificate:

1. reconstructs the exact rational determinant polynomial;
2. retains and factors its rational scale;
3. evaluates its primitive numerator at $m=-b/10$;
4. completely factors the resulting integer;
5. verifies the factor product exactly and verifies every returned prime
   factor by the seven-base deterministic Miller--Rabin test for unsigned
   64-bit integers;
6. imposes the ray congruence and the parity of $m=(p-b)/10$.

Every final factor in this package is below $2^{64}$. The largest is
$28224641983280857$, below $2^{55}$.

Only five compatible large candidates remain:

| $b$ | $p$ | $m$ | $(L_0,L_1)\bmod p$ |
|---:|---:|---:|---:|
| 29 | 106512286889 | 10651228686 | (18108325412, 82027007427) |
| 33 | 1283 | 125 | (766, 309) |
| 37 | 3727 | 369 | (2428, 3387) |
| 39 | 4077079 | 407704 | (1591880, 2704488) |
| 41 | 1361 | 132 | (1197, 313) |

All are excluded. There are no compatible large candidates for the other
eight intercepts in (1.2).

There are also 50 prime cases with $p\leq3b-5$, where the singular
representative can wrap modulo $p$. The certificate evaluates all 50
directly from the original scalar Taylor recurrence; none has a common
zero. Every pair is retained in the JSON.

These exact factorizations, the five nonzero candidate pairs, and the 50
wrapped replays prove (1.1) for all the new intercepts.

## 5. The $O(\sqrt p)$ large-candidate replay

The candidate $p=106512286889$ is far beyond a linear Taylor scan. The
certificate evaluates (3.6) by a product tree.

For each required factorial $r!\pmod p$, choose a power of two $B$
with $B^2\geq r$, and form



$$
P_B(X)=\prod_{i=1}^B(X+i).
$$



A subproduct tree constructs $P_B$. A second subproduct/remainder tree
evaluates it simultaneously at



$$
0,B,2B,\ldots,(B-1)B.
$$



Prefix products of these block values, followed by fewer than $B$ scalar
multiplications, give every required factorial. This costs
$O(M(B)\log B)$ field operations with $B=O(\sqrt p)$.

For the large candidate, the independently retained audit data are



$$
B=262144,
$$





$$
(6m,a_E,6m-a_E,a_O,6m-a_O)
 =(63907372116,10651228693,53256143423,
   37279300415,26628071701),
$$





$$
(r!\bmod p)
 =(3719167100,96377933757,4525679140,
   17719372598,38523073633),
$$





$$
(4E,4O)=(6883996212,38167897735).
$$



Substitution into the exact two-state matrix gives the first row of the
candidate table.

The replay environment is recorded in the JSON:

* Python 3.13.14;
* SymPy 1.14.0;
* python-flint 0.9.0;
* FLINT runtime 3.6.0.

SymPy is used only to find the integer factorizations; every factor product
and every factor's deterministic primality test are independently checked.
python-flint performs the finite-field polynomial product and remainder
trees.

## 6. Determinant-zero audit beyond the proved rays

The companion standard-library scan evaluates (2.6) modulo
$\ell=1000000007$ for both parities and every admissible odd



$$
3\leq b\leq2001,\qquad 5\nmid b.
$$



There are 800 intercepts and 1600 parity rows. Every modular determinant is
nonzero. Since every denominator in (2.4) has absolute value below
$3b<\ell$, this rigorously proves that none of those 1600 rational
determinants is zero. The ordered residue stream has SHA-256



$$
\texttt{cd262f0f3ef203607b39b3af8d97ab9a504c0fcb2c45b429c7d04fe9388920a0}.
$$



This is a finite exact determinant classification, not a uniform theorem in
$b$. It also does not prove all rays through $b=2001$: after determinant
nonvanishing, one must still factor each fixed ray constant and replay its
compatible prime divisors. That second stage is completed here only through
$b=57$.

## 7. Artifacts

The freeze-ready files are:

* moving_ray_y5_minus_y_extended_theorem.md;
* moving_ray_y5_minus_y_extended_certificate.py;
* moving_ray_y5_minus_y_extended_certificate.json;
* moving_ray_determinant_nonzero_scan.py;
* moving_ray_determinant_nonzero_scan_b2001.json.

The extended generator expects the earlier
mixed_cubic_moving_ray_y5_minus_y_certificate.py in the same directory. The large
candidate replay additionally requires the dependency versions listed in
Section 5. Both JSON outputs are deterministic; an independent rerun should
be byte-identical.
