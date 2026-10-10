> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A recurrence-to-density transfer lemma for future actual cells

Status: rigorous general auxiliary deduction, with an application already
checked for the actual ordinary-j=2 determinant. This note is a reusable
mathematical statement, not a claim that every archived cell meets its
hypotheses or that the main irrationality problem is solved.

## Statement

Fix an order r>=2 and rational polynomials P_0,...,P_r of degree at
most D, with deg P_r=D. Suppose the rational companion transfer



$$
T(h)=\begin{pmatrix}
0&1&0&\cdots&0\\
0&0&1&\cdots&0\\
\vdots&&&\ddots&\vdots\\
0&0&0&\cdots&1\\
-P_0/P_r&-P_1/P_r&\cdots&&-P_{r-1}/P_r
\end{pmatrix}
$$



has a finite limit C as h tends to positive infinity. Assume all
eigenvalues of C are nonzero, and no ratio of distinct eigenvalues is
a root of unity. Repeated eigenvalues are permitted.

For each sufficiently large prime p, let an actual sequence u_(p,n)
be defined and p-integral for 0<=n<N_p, where N_p is comparable to p
and N_p<p. It obeys the recurrence at h=h_0+kn whenever all necessary
indices are actual, with fixed rational h_0 and fixed nonzero integer k.
Finite many choices of h_0 are permitted. Require p to avoid their
denominators and k. Most importantly, assume that the number of starts
of zero full states



$$
(u_{p,n},\ldots,u_{p,n+r-1})=0\pmod p
$$



is o(p), uniformly for the allowed family. Then



$$
\#\{n<N_p:u_{p,n}=0\pmod p\}=o(p).
\tag{1}
$$



The initial state may depend on p. No cross-prime independence is
assumed. If zero-state starts are uniformly bounded, the proof also
gives a bound using the finite progression-free function r_r(K), with
K a constant multiple of log p; for r=3 this yields the logarithmic
rate in the session's Roth application.

## Observation determinants for every fixed spacing

Let e_1=(1,0,...,0). The row e_1 is cyclic for the companion matrix C:
the rows e_1,e_1C,...,e_1C^{r-1} form the identity matrix. For every
positive integer d, the matrix C is a polynomial in C^d. To see this,
on each generalized eigenspace the map z->z^d has nonzero derivative
at its nonzero eigenvalue. Distinct eigenvalues have distinct d-th
powers by the non-root-of-unity hypothesis. Hermite interpolation
therefore constructs a polynomial f_d with f_d(C^d)=C, matching the
required derivatives through each Jordan block size. Equivalently,
take the local inverse of z^d at each eigenvalue and interpolate its
finite Taylor jets at the distinct d-th powers.

It follows that Q[C^d]=Q[C] after extending scalars if necessary; the
argument only needs equality of the complex spans. Thus e_1 is also
cyclic for C^d, and



$$
\det(e_1C^{jd})_{j=0}^{r-1}\ne0.
\tag{2}
$$



The rational observation determinant formed from the actual transfer
products at spacings0,d,...,(r-1)d tends to(2) as h->infinity. It is
therefore a nonzero rational function for every d. This establishes a
symbolic nonidentity; it makes no finite-field approximation assertion.

For each fixed d, clear its denominator and exclude finitely many primes
where the resulting numerator becomes the zero polynomial. At any other
prime, the observation determinant and transfer denominators vanish at
only O_d(1) actual starts, since h=h_0+kn is injective modulo p on the
actual interval. Except for these starts and O_r(d) boundary starts, an
r-term progression of zero observations forces a zero full state.

Therefore, for each fixed d, the number of all-zero r-term progressions
of spacing d is O_d(1)+o(p). For any fixed K, removing the starting
indices of all such progressions with 1<=d<=K costs o(p). Every block
of length K in the remaining zero set is r-term-progression-free.
Consequently



$$
\limsup_{p\to\infty}\frac{\#\{n:u_{p,n}=0\}}{N_p}
\le\frac{r_r(K)}K.
$$



Szemeredi's theorem gives r_r(K)=o(K). Letting K->infinity proves(1).
For r=3 only Roth's older three-term progression theorem is needed.
The limit order is important: K is first fixed, so only finitely many
step sizes and exceptional-prime sets enter.

## A simpler quantitative reduction using only a leading coefficient

Clear a common constant denominator so all P_j are integer polynomials.
Put M(h)=P_r(h)T(h), and let L be its degree-D coefficient matrix.
Then L=lc(P_r)C. Translation of h does not change L. Thus the leading
matrix coefficient of a length-jd product is L^{jd}.

The unreduced integer observation numerator J_d has degree at most



$$
Dd\sum_{j=1}^{r-1}j=Dd\frac{r(r-1)}2.
$$



Its coefficient at exactly that degree is



$$
\ell_d=\det(e_1L^{jd})_{j=0}^{r-1}\ne0
\tag{3}
$$



by(2). This particular integer coefficient is sufficient to prevent
J_d from vanishing identically modulo p. No bound on all its lower
coefficients is needed.

Let B be the larger of2 and the maximum absolute row-sum norm of L.
The determinant expansion bounds



$$
|\ell_d|\le (r-1)! B^{d r(r-1)/2}.
\tag{4}
$$



Taking K_p=c_r log p/log B with a sufficiently small positive constant
c_r makes the right side of(4) less than p for all d<=K_p and large p.
Because ell_d is a nonzero integer, J_d is then nonzero modulo p
uniformly for those d. The observation and denominator degree bounds
are O_r,D(d), so if full zero states have a uniform constant bound,
deleting all short progression starts costs O(K_p^2). Therefore



$$
Z(p)\le\frac{N_p}{K_p}r_r(K_p)+O(K_p^2+K_p).
\tag{5}
$$



For the present order-three case, |ell_d|<=2B^{3d} and
K_p=floor(log p/(6 log B)) works once p>4. This improves the earlier
log p/log log p choice by using only the leading coefficient; the
final exp(-c(log log p)^(1/9)) shape from Bloom–Sisask is unchanged.

## An essential failure mode

The zero-state hypothesis cannot be dropped. The central binomial
coefficients v_n=binom(2n,n) obey a first-order rational recurrence with
nonzero limiting multiplier4. Nevertheless, for odd p, every n with
(p+1)/2<=n<p has v_n=0 modulo p, because (2n)! contains one factor p
and n! contains none. A recurrence numerator becomes zero and sends
the reduced state to zero on a long interval.

This example explains why the session's actual p-unit and reverse-
propagation arguments are indispensable. Algebraicity, a rational
recurrence, and a well-behaved limiting characteristic polynomial alone
do not imply the desired density statement. Future applications must
prove nonzero-state control in their precise actual range.

## Source and application limits

The progression theorem is an imported established result. Primary
reference: E. Szemeredi, [On sets of integers containing no k elements
in arithmetic progression](https://doi.org/10.4064/aa-27-1-199-245),
Acta Arithmetica27(1975),199–245. The specialized r=3 source and the
quantitative Bloom–Sisask statement are given in
`fixed_prime_roth_density.md`.

This note has not checked every cell against the hypotheses. In
particular, a merely finite recurrence fit, a generating-function norm,
or an unproved bridge from a collision to a coefficient zero is
insufficient. Higher p-adic multiplicity weights require a separate
argument; zero-density of the support alone does not bound their sum.
