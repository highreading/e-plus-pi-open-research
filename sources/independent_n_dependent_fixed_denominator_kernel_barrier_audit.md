> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the $n$-dependent fixed-denominator kernel barrier

Date: 2026-08-26

## Verdict

**ACCEPT.**  The conversion of Salikhov's theorem, the primitive
exponential estimates, the prime-power content calculation, both matching
signs, the fixed-denominator projective height bound, the variable midpoint
identities, and the necessary escape-scale dichotomy all rederive
correctly.  The theorem applies pointwise along any infinite set of even
indices and therefore does not rely on density or consecutiveness of those
indices.

One harmless edge defect was found and corrected before the final source
hash was frozen.  The lower bound containing $(2n-1)!$ was initially stated
for “even $n$,” although the surrounding recurrence also defines $n=0$.
The final source now states explicitly that this bound is for positive even
$n$, equivalently $n\ge2$.  No asymptotic conclusion changed.

The accepted source is
`sources/n_dependent_fixed_denominator_kernel_barrier.md`, with SHA-256

`b7f45b54900b49395c08fb9fe031356572bde3e968ef9ffcebcf165509d5f220`.

## 1. Uniform two-sign lower bound for integer $\pi$-forms

Salikhov's Theorem 1 states that, for positive integers $p,q$ with
$q\ge q_0$,

$$
\left|\pi-\frac pq\right|\ge q^{-\nu_0},
\qquad \nu_0=7.6063\ldots<8.
$$

I checked this quantification against the English primary-source paper; it
is not merely a statement about a selected sequence of approximants.

For $A\in\mathbb Z$, $B\ge1$, and $\delta=\pm1$, put
$p=-\delta A$.  If $p>0$ and $B\ge q_0$, then

$$
|A+\delta B\pi|
=B\left|\pi-\frac pB\right|
\ge B^{1-\nu_0}\ge B^{-7}.
$$

If $p\le0$, the same expression is at least $B\pi$, so this case is easier.
For each of the finitely many $1\le B<q_0$, the minimum over all integer
$A$ is the positive distance from $B\pi$ to the nearest integer.  Taking
the minimum of these finitely many scaled distances and the large-$B$
constant produces a single $c_\pi>0$ such that

$$
|A+\delta B\pi|\ge c_\pi B^{-7}
$$

for both signs, every integer numerator (including zero), and every
$B\ge1$.  Thus the source correctly handles the numerator sign, small
denominators, and non-coprime rational presentations.  Even if one used a
formulation of the irrationality measure restricted to coprime $p,q$,
reducing $p/q$ only decreases the denominator and gives the same weaker
exponent-$8$ conclusion.

## 2. Primitive exponential beta form

Let

$$
E_n=\frac1{n!}\int_0^1x^n(1-x)^ne^x\,dx.
$$

Repeated integration by parts terminates because
$x^n(1-x)^n$ has degree $2n$.  Evaluation of its endpoint derivatives gives,
for even $n$,

$$
E_n=q_ne-p_n,
$$

with

$$
p_n=\sum_{j=0}^n\frac{(n+j)!}{j!(n-j)!},
\qquad
q_n=(-1)^n\sum_{j=0}^n(-1)^j
          \frac{(n+j)!}{j!(n-j)!}.
$$

These are integer sums.  Equivalently, $p_n$ and $(-1)^nq_n$ are the
Bessel polynomial evaluated at $2$ and $-2$, respectively.  The elementary
Bessel recurrence gives, for either sequence,

$$
X_n=2(2n-1)X_{n-1}+X_{n-2}.
$$

Thus the adjacent determinant satisfies

$$
p_nq_{n-1}-p_{n-1}q_n
=-(p_{n-1}q_{n-2}-p_{n-2}q_{n-1}),
$$

and has absolute value $2$ from the initial values.  The recurrence's
coefficient is even and all four initial entries are odd, so all $p_n,q_n$
are odd.  Any common divisor therefore divides $2$ and is odd; hence
$\gcd(p_n,q_n)=1$.

For positive even $n$, reverse the alternating sum for $q_n$.  Its first
pair is

$$
\frac{(2n)!}{n!}
-\frac{(2n-1)!}{(n-1)!}
=\frac{n(2n-1)!}{n!},
$$

and every remaining reversed pair is nonnegative because the summands
increase with $j$.  Consequently

$$
q_n\ge\frac{n(2n-1)!}{n!}
=n\prod_{k=n+1}^{2n-1}k\ge n^n.
$$

Finally,

$$
0<E_n\le
\frac e{n!}\int_0^1x^n(1-x)^n\,dx
=\frac{e\,n!}{(2n+1)!}.
$$

Dividing by the lower bound for $q_n$ gives exactly

$$
\frac{E_n}{q_n}
\le\frac e{n^n(n+1)^{n+1}}
\le e\,n^{-2n-1}.
$$

These estimates are all valid independently of how sparse the selected
even indices are.

## 3. Minimal matching, prime powers, and the exponent $B^9$

Let $L=A+\varepsilon B\pi$ be primitive, with $B>0$, and orient it by its
nonzero value.  Irrationality of $\pi$ ensures $L\ne0$.  If
$\widetilde L=\widetilde A+\delta B\pi=|L|$, then
$\gcd(\widetilde A,B)=1$ and $\delta=\pm1$.

Put

$$
d=\gcd(q_n,B),\qquad q_n=dq_0,\qquad B=dB_0.
$$

Since $\gcd(q_0,B_0)=1$, the unique minimal positive multipliers that make
the target coefficients equal are $B_0$ and $q_0$.  The common coefficient
is

$$
C=dq_0B_0=\frac{q_nB}{d},
$$

and, in the two sign cases, the constant coefficient is

$$
M=-B_0p_n\mathbin{\pm}q_0\widetilde A.
$$

For every prime $\ell\mid q_0$, reduction modulo $\ell$ gives
$M\equiv-B_0p_n\not\equiv0$, using
$\gcd(B_0,q_0)=\gcd(p_n,q_n)=1$.  For every
$\ell\mid B_0$, it gives
$M\equiv\pm q_0\widetilde A\not\equiv0$.  Therefore, if
$g=\gcd(M,C)$ is the final content, no prime from $q_0B_0$ occurs in $g$;
for every remaining prime its exponent in $C$ is at most its exponent in
$d$.  This proves the full prime-power statement

$$
g\mid d.
$$

This also covers $M=0$.  In that case the preceding congruences force
$q_0=B_0=1$, whence $C=d$ and $g=d$ exactly.

If $\delta=1$, the raw value is the positive sum

$$
W^+=B_0E_n+q_0\widetilde L.
$$

Since $g\le d\le B$,

$$
\frac{W^+}{g}
\ge\frac{q_n|L|}{B^2}
\ge c_\pi\frac{q_n}{B^9}.
$$

The nine powers have a precise origin: seven from the irrationality
measure and at most two from $dg\le B^2$ in minimal matching and primitive
reduction.

If $\delta=-1$, then

$$
W^-=B_0E_n-q_0\widetilde L
=\frac{q_nB}{d}
 \left(\frac{E_n}{q_n}-\frac{|L|}{B}\right).
$$

The ratio of its first positive term to the second satisfies

$$
0\le
\frac{E_n/q_n}{|L|/B}
\le c_\pi^{-1}eB^8n^{-2n-1}.
$$

If $\log B=o(n\log n)$, this tends to zero and is eventually at most
$1/2$.  The same content calculation then yields

$$
\left|\frac{W^-}{g}\right|
\ge\frac{c_\pi}{2}\frac{q_n}{B^9}.
$$

Because $q_n\ge n^n$, this lower bound tends to infinity whenever
$\log B=o(n\log n)$.  Both signs and the exact cancellation threshold are
therefore accounted for.

## 4. Fixed-$Q$ projective coordinate height

Let $D_n(x)=\widehat P(x)x^n(1-x)^n$.  Submultiplicativity of the
coefficient $\ell^1$ norm gives

$$
\|D_n\|_1\le\|\widehat P\|_1\,2^n
\le\mathcal H2^n,
$$

and $\deg D_n=2n+d$.  For $\deg Q\ge1$, polynomial pseudo-division by the
fixed $Q$ gives a common denominator bounded by a power of the fixed
leading coefficient of $Q$.  Each of $O_Q(n+d)$ steps multiplies the
integer numerator norm by at most a fixed constant.  Hence the quotient
and remainder in

$$
\frac{D_n}{Q}=U_n+\frac{R_n}{Q},
\qquad\deg R_n<\deg Q,
$$

have a common denominator and numerator norms bounded by

$$
\exp(C_Q(n+d+\log\mathcal H)).
$$

If $\deg Q=0$, this argument reduces simply to $U_n=D_n/Q$ and $R_n=0$;
the same bound is immediate.  In fact, in the theorem's application a
constant $Q$ makes every moment rational, so the hypothesis of a nonzero
rational $\pi$-coordinate is impossible and the main assertion is
vacuous.  The height lemma itself remains valid.

Integrating $U_n$ introduces denominators only from
$1,2,\ldots,2n+d+1$.  A common denominator is their least common multiple,
not their product, and the elementary estimate

$$
\operatorname{lcm}(1,\ldots,m)\le16^m
$$

keeps this cost exponential.  The remainder uses only the fixed values

$$
\omega_j=\int_0^1\frac{x^j}{Q(x)}\,dx,
\qquad0\le j<\deg Q.
$$

In the finite-dimensional rational span of $1,\pi,\omega_0,\ldots$, the
irrationality of $\pi$ makes $1,\pi$ independent, so they can be included
in a fixed basis.  The rational coordinate matrix of the finitely many
$\omega_j$ has fixed height.  Consequently, if all other coordinates
cancel and

$$
\widehat J_n=\rho+\gamma\pi,
$$

then the reduced heights of $\rho$ and $\gamma$ have the claimed
exponential bound.  No unproved linear independence involving the
$\omega_j$ is assumed; only a basis of their actual rational span is used.

If $\rho=a/b$ and $\gamma=u/v$ are reduced, multiplication by $bv$ gives
the integer pair $(av,bu)$.  Thus the primitive $\pi$-coefficient is at
most $b|u|$, so the two coordinate-height bounds imply

$$
B\le\exp(C_Q(n+d+\log\mathcal H))
$$

after enlarging $C_Q$.  This explicitly includes the otherwise easy-to-miss
numerator of $\gamma$ and denominator of $\rho$; bounding individual raw
rational coefficients without their common primitive normalization would
not suffice.

Finally, replacing $P$ by $\lambda\widehat P$ multiplies both rational
coordinates by the same nonzero rational $\lambda$.  Clearing denominators
and taking primitive content returns the same integer direction, up to
overall sign.  Hence an arbitrarily large numerator or denominator in
$\lambda$ cannot affect $B$.  Under the source's condition

$$
n+d_n+\log\mathcal H_n=o(n\log n),
$$

the projective height bound supplies precisely the hypothesis of the
matching lemma and proves the main theorem.

## 5. Midpoint order, beta factor, and arithmetic lower bound

Symmetrization is exact because the beta weight is invariant under
$x\mapsto1-x$.  The displayed numerator of the symmetrized kernel is a
polynomial of degree at most $d_n+\deg Q$.  If it vanished identically,
the moment would be zero; since a rational relation
$r_n+\varepsilon_nc_n\pi=0$ with $c_n>0$ is impossible, this zero case is
excluded.  The symmetrized kernel is even at the midpoint, so its finite
zero order is $2m_n$ and

$$
2m_n\le d_n+\deg Q.
$$

Writing it as $t^{2m_n}G_n(t)$ gives a continuous residual factor with
$G_n(0)\ne0$.  For

$$
M_{n,m}=\int_{-1/2}^{1/2}(1-4t^2)^nt^{2m}\,dt,
$$

the substitution $u=4t^2$ gives

$$
M_{n,m}=\frac1{2\cdot4^m}B\left(m+\frac12,n+1\right).
$$

The half-integer gamma identities then give exactly

$$
4^{-n}M_{n,m}
=\frac{2(2m)!\,n!\,(n+m+1)!}
       {4^m m!(2n+2m+2)!}.
$$

Moreover, $4^{-n}M_{n,m}$ is
$\int_0^1[x(1-x)]^n|x-1/2|^{2m}\,dx$.  Bounding on all of $[0,1]$ and
below on $[1/8,1/4]$ proves

$$
\frac18\left(\frac7{64}\right)^n16^{-m}
\le4^{-n}M_{n,m}\le4^{-n-m}.
$$

Thus $m=O(n)$ supplies only an exponential penalty.

The coefficient norm estimate for $G_n$ also checks.  Substitution
$x\mapsto1-x$ costs at most $2^{d_n}$ in coefficient norm, translating by
$1/2$ costs another fixed exponential in the degree, and division by the
known factor $t^{2m_n}$ merely shifts the nonzero coefficients.  The fixed
denominator is bounded away from zero on the compact interval.  Therefore

$$
\log(1+\|G_n\|_\infty)
\le C_Q(d_n+\log\mathcal H_n).
$$

For the arithmetic lower bound, a nonzero reduced rational
$\gamma=u/v$ of height at most $X$ satisfies $|\gamma|\ge X^{-1}$.  If
$A+\varepsilon B\pi$ is the primitive coordinate direction, then

$$
\frac{|\widehat J_n|}{|\gamma|}
=\frac{|A+\varepsilon B\pi|}{B}
\ge c_\pi B^{-8}.
$$

Combining $|\gamma|\ge X^{-1}$ and $B\le X$ gives a lower bound of the
form $X^{-9}$, which is exactly the claimed

$$
|\widehat J_n|
\ge\exp(-C'_Q(n+d_n+\log\mathcal H_n)).
$$

This argument requires the $\pi$-coordinate to be nonzero; the assumption
$c_n>0$ and the nonzero projective scale guarantee that condition.

## 6. Necessary escape dichotomy

Suppose the final primitive forms are bounded by a fixed constant along an
infinite subsequence.  In the same-sign case the lower bound
$c_\pi q_n/B_n^9$ and $q_n\ge n^n$ immediately imply

$$
\log B_n\ge\frac19n\log n-O(1).
$$

In the opposite-sign case, either the $\pi$-form term is at least twice the
exponential term, in which case the same estimate applies, or

$$
\frac{E_n/q_n}{|L_n|/B_n}>\frac12.
$$

The universal upper bound for this ratio then forces

$$
B_n^8\gg n^{2n+1},
\qquad
\log B_n\ge\frac14n\log n-O(\log n).
$$

These two alternatives are exhaustive at every selected index, regardless
of how the signs or alternatives vary along the subsequence.  Hence every
bounded escape subsequence must satisfy at least

$$
B_n\ge n^{\,n/9-o(n)}.
$$

The projective height upper bound then makes

$$
n+d_n+\log\mathcal H_n=\Omega_Q(n\log n)
$$

necessary.  This is a necessary scale, not a sufficiency assertion.  In
particular, an $O(n)$ midpoint order, $O(n)$ numerator degree, and
exponential projective numerator height remain strictly within the
barrier.

## 7. Independent checks and file validation

In addition to the symbolic derivations above, I performed the following
finite stress checks.  They are corroboration only and were not used as
proof.

* The exact $p_n,q_n$ formulas, common recurrence, alternating determinant,
  parity, and gcd were checked for every $0\le n\le60$; the $q_n$ lower
  bound was checked for every even $2\le n\le60$.
* The content assertion $g\mid d$ was independently tested in
  $1{,}276{,}802$ primitive finite-box cases, including $1{,}598$ cases
  with $M=0$, and in 8,540 additional cases using the actual exponential
  sequence.
* The beta identity and both elementary bounds were checked as exact
  rational identities for every pair $0\le n,m\le30$.
* Salikhov's positivity and large-denominator quantifiers were checked
  against the English primary-source PDF linked in the source note.

The final Markdown source is 16,742 bytes, strict UTF-8 and LF-only, with no
forbidden C0 control bytes or replacement characters.  It has 65 ordered
display pairs, 139 ordered inline pairs, and the complete sequential tag
list 1 through 38.  A Pandoc render check exits successfully.

The accepted conclusion is construction-specific: fixed denominator and
subfactorial projective numerator complexity force divergence under the
specified minimal coefficient matching.  It makes no unconditional claim
about the arithmetic nature of $e+\pi$ and leaves the larger-complexity,
varying-denominator, and different-matching regimes open.
