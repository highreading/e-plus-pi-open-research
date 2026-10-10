> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 216 — the unique contiguous residual and an all-phase Gosper obstruction

Date: 2026-08-31

## 1. Scope and verdict

Item 214 reduced the stable common-content problem to two rational sums
$\Phi_{g_1}(b,r),\Phi_{g_0}(b,r)$, where



$$
b\le k+2,\qquad r\equiv k=3s+2\pmod 4,\qquad
 b=qp-5s-4,\quad q\in\{1,2\}.                 \tag{1.1}
$$



This item asks whether a contiguous relation, a gamma/Pochhammer product, or
a first-order telescoper can expose the common gcd for all moving $b$.

**PROVED — unique first contiguous reduction.**  Among combinations of the
two common summands whose coefficients may depend on $(b,r)$ but not on the
summation index, there is a unique pair up to scale that cancels the linear
index dependence:



$$
R_{b,r}:=(r-b-2)\Phi_{g_1}+(b+1)\Phi_{g_0}.       \tag{1.2}
$$



Its common summand $F_h$ has a reduced quotient $F_{h+1}/F_h=A_r/B_r$
with two explicit monic quartics.

**PROVED — phase-uniform Gosper obstruction.**  For every actual stable
phase with $p>5$, $b\ge5$, and outside the support gaps, $F_h$ has no
hypergeometric antidifference in Gosper normal form.  The polynomial degree
that an antidifference would require is



$$
d={3b-8\over5}.            \tag{1.3}
$$



The only residue class in which the specialized normal form could have a
root collision is $b\equiv1\pmod5$, but (1.1) then forces $p=5$.  Thus
the collision class is absent at every phase in scope.

**PROVED — the mandatory exception survives.**  At
$(s,p,q,b,r,k)=(299,2399,1,900,3,899)$, (1.3) equals $2692/5$, so the
no-telescoping theorem applies.  Nevertheless the reduced numerator of
$R_{900,3}$ remains divisible by the entire Item 214 gcd, including
$2399$.  The theorem is a method obstruction, not an arithmetic
nonvanishing theorem.

**FINITE.**  The checker reconstructs every common residual and every
consecutive quotient through $b=120$, checks the phase exclusion on a
declared finite grid, and records all exact $b<5$ gcds.  These checks only
verify the displayed all-parameter identities; they are not extrapolated
factor scans.

**OPEN.**  No forced-product factorization of $G_{b,r}$, no higher-order
creative telescoper in $b$, and no phase-feasible prime-localization bound
is obtained.  Consequently the new usable Route-1 rate credit is zero; the
actual stable/far common-prime log mass remains unbounded by this item.

## 2. Item 214 common term

Put



$$
\alpha={3b+2+5r\over20},\qquad
 \delta={r-b-2\over4},\qquad z=\delta+h,            \tag{2.1}
$$



and



$$
T_h={b\choose r+4h}{(\alpha)_h\over(\delta)_h}.
                                                               \tag{2.2}
$$



On the common support $0\le h\le\lfloor(b-r)/4\rfloor$, Item 214 gives



$$
\Phi_{g_1}^{\rm common}
   =-\sum_h T_h{b+1\over4z+1},\qquad
 \Phi_{g_0}=\sum_h T_h{\delta\over z}.              \tag{2.3}
$$



If $e=(b+1-r)/4$ is a nonnegative integer, $\Phi_{g_1}$ additionally
has the single endpoint



$$
E={ (\alpha)_e\over(\delta)_e}.        \tag{2.4}
$$



There is no denominator singularity on the common support: $z=0$ or
$4z+1=0$ would place $h$ strictly beyond that support.

## 3. The unique contiguous combination

Let $\lambda,\mu$ be independent of $h$.  After putting the two weights
in (2.3) over the common denominator $z(4z+1)$, their combined numerator is



$$
\bigl[-\lambda(b+1)+4\mu\delta\bigr]z+\mu\delta.   \tag{3.1}
$$



Because $b+1\ne0$ and $4\delta=r-b-2\ne0$ when $r\le b$, the
coefficient of $z$ vanishes precisely when



$$
\lambda:\mu=(r-b-2):(b+1).        \tag{3.2}
$$



This proves uniqueness up to an overall scalar.  With the primitive choice
in (3.2),



$$
F_h=T_h{(b+1)\delta\over z(4z+1)},                 \tag{3.3}
$$



and the full exact identity is



$$
R_{b,r}=\sum_{h=0}^{\lfloor(b-r)/4\rfloor}F_h
       +\begin{cases}
         (r-b-2)E,&b+1-r\equiv0\pmod4,\\
         0,&\text{otherwise}.
        \end{cases}                                  \tag{3.4}
$$



Thus the endpoint is already explicit.  The remaining question is whether
the common sum in (3.4) is itself a hypergeometric boundary.

## 4. Exact reduced quotient

Combining the Item 214 ratio for $T_h$ with (3.3), and cancelling the two
linear factors furnished by $z+1$ and $4z+5$, gives



$$
{F_{h+1}\over F_h}={A_r(h)\over B_r(h)},           \tag{4.1}
$$



where



$$
A_r(h)=-{1\over1280}
  \prod_{u=r-1}^{r+1}(b-4h-u)(3b+20h+2+5r),         \tag{4.2}
$$



and, writing $f=\lfloor r/2\rfloor$,
$c=\lceil r/2\rceil$,



$$
B_r(h)={1\over32}(h+1)(2h+1+2f)
              (4h+1+2c)(4h+3+2c).                  \tag{4.3}
$$



Both quartics are monic.  Their cubic coefficients are



$$
[h^3]A_r=-{3b\over5}+r+{1\over10},\qquad
 [h^3]B_r(h-1)=r-{3\over2}.                         \tag{4.4}
$$



The standard-library checker proves (4.1) as an identity in the polynomial
ring $\mathbb Q[b,h]$, before making any numerical substitutions.

## 5. Gosper normality and the degree obstruction

The four roots of $A_r$ are



$$
{b-r+1\over4},\quad {b-r\over4},\quad {b-r-1\over4},
 \quad -{3b+2+5r\over20}.                            \tag{5.1}
$$



Every root of $B_r(h+j)$, $j\ge0$, is a constant nonpositive rational
number.  Hence over $\mathbb Q(b)$, no root in (5.1) is identically a root
of $B_r(h+j)$.  Therefore (4.1) is in Gosper normal form with the auxiliary
factor $C=1$.

The same normality holds after every actual phase specialization in scope.
Indeed, for $b\ge5$ the first three roots in (5.1) are positive, whereas
the roots of every $B_r(h+j)$ are negative.  A collision involving the
fourth root would require



$$
-{3b+2+5r\over20}=\rho-j                            \tag{5.2}
$$



for a quarter-integral root $\rho$ of $B_r$.  Multiplication by 20 and
reduction modulo 5 gives



$$
3b+2\equiv0\pmod5,
 \qquad\text{hence}\qquad b\equiv1\pmod5.           \tag{5.3}
$$



For a hypergeometric antidifference to exist, Gosper's normal-form theorem
requires a polynomial $x(h)$ satisfying



$$
A_r(h)x(h+1)-B_r(h-1)x(h)=1.        \tag{5.4}
$$



If $d=\deg x\ge0$, comparison of the coefficient of $h^{d+3}$ in
(5.4), using monicity and (4.4), forces



$$
d=[h^3]B_r(h-1)-[h^3]A_r(h)={3b-8\over5}.          \tag{5.5}
$$



Now use the phase equation in (1.1).  Modulo 5 it says



$$
b\equiv qp-4\pmod5.         \tag{5.6}
$$



If the exceptional class $b\equiv1\pmod5$ held, then $qp\equiv0\pmod5$.
Because $q\in\{1,2\}$, this would force $p=5$.  Thus every actual phase
with $p>5$ avoids (5.3).  At such a phase the right side of (5.5) is not
an integer, contradicting $d\in\mathbb Z_{\ge0}$.  This proves the stated
no-antidifference theorem.

The theorem's prime domain is explicitly $p>5$.  The fixed primes
$p\le5$, already constrained by $p>3s+2$, have zero asymptotic log-prime
coefficient and do not affect the rate ledger.

For $b<5$, direct exact gcds contain no phase-feasible odd prime greater
than 5.  The formal zero-gcd support gaps are $(b,r)=(0,2),(0,3),(1,3)$;
the Item 214 phase congruence leaves only $(0,3)$ compatible with an odd
prime greater than 5.  That is the already separated support-gap ray.

## 6. Mandatory $b=900$ exception

At $(b,r)=(900,3)$, the degree demanded by (5.5) is $2692/5$, so the
obstruction applies.  Exact rational reconstruction nevertheless gives a
576-digit reduced numerator and a 335-digit denominator for $R_{900,3}$,
with



$$
\operatorname{num}(R_{900,3})\equiv0\pmod {2399},\qquad
 \operatorname{den}(R_{900,3})\equiv954\pmod {2399}. \tag{6.1}
$$



More strongly, the complete Item 214 gcd



$$
2^{449}\cdot911\cdot971\cdot991\cdot1031\cdot1051\cdot1091
 \cdot1151\cdot1171\cdot1231\cdot1291\cdot2399                \tag{6.2}
$$



divides the reduced numerator, and is coprime to the denominator.  The
quotient has 407 digits.  Its decimal SHA-256 is

```text
11b7931b943a572f2780d719d6ac1c5ae5a7eb534e0b7a343f7dc132197cd35b
```

This is the exact obstruction to interpreting (1.2) as a product extraction:
the unique simplest residual still carries every common factor.  No claim is
made that those factors are irreducible pieces of a universal gamma product.

## 7. Route-1 rate consequence

One additional common-content valuation copy would need log-prime
coefficient greater than



$$
6G=0.1177979020165907632818384072\ldots\quad\text{per }m, \tag{7.1}
$$



while the full $\kappa=1$ cell coefficient is
$0.4820375017701112$ per $m$.  Item 216 proves no upper or lower
asymptotic bound on the actual common-prime mass.  Its new usable rate credit
is therefore exactly zero.  It only closes the direct first-order
term-by-term hypergeometric telescoping avenue.

The following remain **OPEN** and are not ruled out by this result:

1. a higher-order creative telescoper connecting several $b$-values;
2. a fourth-root filter followed by a non-termwise gamma multiplication
   identity;
3. a forced-product/residual-determinant factorization of $G_{b,r}$;
4. a resultant or modular-singularity argument that localizes
   phase-feasible prime divisors;
5. any $O(m)$, $o(m)$, or positive-density bound for far moving phases.

## 8. Replay

From the archive root, with the Item 212 and Item 214 checkers beside the
Item 216 checker in `scripts/`, run

```text
python scripts/item216_gosper_phase_obstruction_certificate.py \
  --output results/item216_gosper_phase_obstruction_certificate.json
```

Only Python 3.11+ and its standard library are required.  The portable
manifest records the exact dependency hashes and the independent replay
output.
