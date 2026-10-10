> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Quadratic arctangent pullbacks: analytic radius versus jet arithmetic

## Scope

This note tests whether a quadratic rational change of variable can improve
the integral-jet representation



$$
4\arctan\frac{z}{2-z},\qquad F(1)=\pi,
$$



by moving its nearest singularities farther from the origin.  A simple
one-parameter family does move them as far as $\sqrt5$, but its derivative
jets acquire exact prime-power denominators.  Exact endpoint-matched
Hermite--Padé calculations through degree $8$ grow rather than shrink.
A broader finite search finds no reduced quadratic pullback with integral
jets through order $25$ and radius strictly larger than $\sqrt2$ in the
displayed box.

None of these results decides the arithmetic nature of $e+\pi$, and the
finite search is not a classification theorem.

## 1. A family with radius as large as $\sqrt5$

For an integer $p\ge2$, put



$$
u_p(z)=\frac{(p-1)z}{p-z^2},
 \qquad
 F_p(z)=4\arctan u_p(z).
 \tag{1}
$$



The real denominator is positive on $[0,1]$, and



$$
u_p(0)=0,\qquad u_p(1)=1,\qquad F_p(1)=\pi.
\tag{2}
$$



The possible poles of $u_p$ are removable for the derivative of the
analytic continuation of $F_p$.  Direct differentiation gives



$$
\boxed{
 F_p'(z)=
 \frac{4(p-1)(p+z^2)}
 {z^4+(p^2-4p+1)z^2+p^2}.}
\tag{3}
$$



The actual logarithmic singularities occur at the preimages of $i$ and
$-i$.  For example, $u_p(z)=i$ is equivalent to



$$
z^2-i(p-1)z-p=0,
\tag{4}
$$



whose discriminant is



$$
\Delta_p=4p-(p-1)^2=8-(p-3)^2.
\tag{5}
$$



For $p=2,3,4,5$, this discriminant is positive, and both roots in (4)
have modulus $\sqrt p$; the conjugate equation has the same radii.
Consequently



$$
\rho(F_p)=\sqrt p,\qquad 2\le p\le5.
\tag{6}
$$



For $p\ge6$, write $A_p=p^2-4p+1$.  The squared radii are the positive
numbers whose negatives are the roots of



$$
x^2+A_px+p^2.
$$



The smaller squared radius is



$$
\rho(F_p)^2=
\frac{A_p-\sqrt{A_p^2-4p^2}}2.
\tag{7}
$$



It equals $4$ at $p=6$ and is strictly less than $4$ for $p>6$.
One quick verification is to evaluate
$y^2-A_py+p^2$ at $y=4$:



$$
16-4A_p+p^2=12+16p-3p^2,
$$



which is zero at $p=6$ and negative for $p>6$, placing the smaller
positive root below $4$.  Thus $p=5$ uniquely maximizes the radius
among the integer parameters $p\ge2$:



$$
\boxed{\max_{p\in\mathbb Z,\ p\ge2}\rho(F_p)=\sqrt5.}
\tag{8}
$$



In particular,



$$
F_5(z)=4\arctan\frac{4z}{5-z^2},
\qquad
F_5'(z)=\frac{16(5+z^2)}{z^4+6z^2+25}.
\tag{9}
$$



## 2. Exact denominator cost

Let



$$
F_p'(z)=\sum_{m\ge0}q_{p,m}z^{2m}.
$$



Define the integer sequence



$$
c_{p,0}=1,\qquad
c_{p,1}=-p^2+5p-1,
\tag{10}
$$





$$
c_{p,m}=-(p^2-4p+1)c_{p,m-1}-p^2c_{p,m-2}
\quad(m\ge2).
\tag{11}
$$



Comparing coefficients in (3) proves the exact identity



$$
\boxed{
q_{p,m}=\frac{4(p-1)c_{p,m}}{p^{2m+1}}.}
\tag{12}
$$



Hence



$$
F_p^{(2m+1)}(0)
=\frac{4(p-1)(2m)!\,c_{p,m}}{p^{2m+1}},
\qquad
F_p^{(2m+2)}(0)=0.
\tag{13}
$$



If $p$ is an odd prime, then



$$
c_{p,m}\equiv(-1)^m\pmod p
\tag{14}
$$



by (10)--(11).  Thus no cancellation by $c_{p,m}$ is possible, and
the exact denominator of the nonzero jet in (13) is



$$
\boxed{
p^{\,2m+1-v_p((2m)!)}}.
\tag{15}
$$



Legendre's formula makes the linear denominator growth explicit:



$$
2m+1-v_p((2m)!)
=2m+1-\frac{2m-s_p(2m)}{p-1}.
\tag{16}
$$



For the radius-maximizing choice $p=5$, the exponent is
$3m/2+O(\log m)$.  The analytic gain from $\sqrt2$ to $\sqrt5$
therefore comes with a large, provably unavoidable $5$-adic cost.

The two even composite cases in (6) can also be read exactly from (13).
For $p=2$, both $p^2-4p+1=-3$ and $c_{2,1}=5$ are odd, and (11)
keeps every $c_{2,m}$ odd.  Since
$v_2((2m)!)=2m-s_2(m)$, the exact jet denominator is



$$
2^{\max(0,s_2(m)-1)}.
\tag{17}
$$



For $p=4$, $p^2-4p+1=1$, $c_{4,1}=3$, and again every $c_{4,m}$
is odd.  The exact jet denominator is now



$$
2^{\,2m+s_2(m)}.
\tag{18}
$$



These formulas quantify the analytic/arithmetic tradeoff; by themselves
they are not a no-go theorem for every possible normalization of a
Hermite--Padé construction.

## 3. Exact finite endpoint-matched calculation

For $p=2,3,4,5$ and $1\le n\le8$, the companion script constructs,
over $\mathbb Q$, the system



$$
A_n(z)+B_n(z)e^z+C_n(z)F_p(z)=O(z^{3n+1}),
\qquad
C_n(1)=B_n(1),
\tag{19}
$$



with all three degrees at most $n$.  It then clears all polynomial
denominators, makes the full triple primitive, and separately removes the
complete gcd of the endpoint pair



$$
A_n(1)+B_n(1)(e+\pi).
\tag{20}
$$



In all $32$ cases, the high-jet-plus-endpoint matrix has full row rank,
the projective kernel is one-dimensional, and the first unconstrained
coefficient at order $3n+1$ is nonzero.  Directed rational intervals for
$e+\pi$ certify that every reduced endpoint form is nonzero.  The
certified values of
$\lfloor\log_{10}|A_n(1)+B_n(1)(e+\pi)|\rfloor$, in increasing order
$n=1,\ldots,8$, are



$$
\begin{array}{c|rrrrrrrr}
p&1&2&3&4&5&6&7&8\\ \hline
2&0&3&9&18&31&48&68&90\\
3&1&4&12&25&39&57&81&105\\
4&0&1&8&17&32&47&68&91\\
5&0&6&14&24&40&62&89&118
\end{array}
\tag{21}
$$



Thus the larger-radius choices do not yield small primitive endpoint forms
in this finite range.  No asymptotic conclusion is inferred from (21).

The exact script is
scripts/quadratic_arctan_pullback_probe.py, and its output is
results/quadratic_arctan_pullback_p2_p5_n8.json.

## 4. Broader finite integral-jet search

A second script searches reduced rational functions



$$
u(z)=\frac{z(A+Bz)}{C+Dz+Ez^2},
\qquad A+B=C+D+E,
\tag{22}
$$



with primitive integer parameters,



$$
|A|,|B|,|D|,|E|\le16,\qquad
C\in\{1,2,4,8,16\},
\tag{23}
$$



and with no denominator zero on $[0,1]$.  It excludes a common
numerator/denominator factor exactly, expands
$4u'/(1+u^2)$ over $\mathbb Q$, and requires all derivative jets
through order $25$ to be integers.

After these reductions, $53{,}036$ candidates with a safe real path were
tested; $16{,}158$ passed the finite jet-integrality test.  None had
computed singular radius strictly larger than $\sqrt2$.  The radius
comparison in this exploratory search uses floating algebraic root
evaluation with a $10^{-12}$ separation threshold, so this is recorded
only as a reproducible finite diagnostic, not as an exact exhaustive
certificate.

The search script is
scripts/quadratic_integral_jet_pullback_search.py, and its output is
results/quadratic_integral_jet_pullback_search_R16.json.

## 5. Conclusion

The family (1) proves that a rational pullback can substantially enlarge the
analytic disk while retaining $F_p(1)=\pi$.  Equations (15), (17), and
(18) show why this alone is insufficient: the Taylor-jet arithmetic worsens
at the same time.  The present finite endpoint calculations are strongly
unfavorable, and the finite integral-jet search finds no genuinely improved
quadratic competitor in its box.  A useful future direction would be either

1. an all-degree height/content theorem proving that the denominators in
   (15) cannot be recovered by determinant content, or
2. a higher-degree pullback whose enlarged singular radius coexists with
   an all-order integral Hurwitz expansion.

Neither statement is proved here.
