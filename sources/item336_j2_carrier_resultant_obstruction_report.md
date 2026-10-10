> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 336 - resultant collapse and the fixed-$M$ carrier obstruction

Checked: 2026-09-01 (Beijing time)

## 1. Capacity audit first

Item 334 reduced the actual ordinary-$j=2$ collision on each row to the
primitive target-retaining carrier



$$
\mathfrak G_{r,s}
 =\gcd\left(
  |\operatorname {num}(D)|,
  |\operatorname {num}(T_0)|,
  |\operatorname {num}(T_1)|
 \right),                                           \tag{1.1}
$$



with the exact equivalence



$$
p\text{ is an original collision on }(r,s)
 \quad\Longleftrightarrow\quad p\mid\mathfrak G_{r,s}. \tag{1.2}
$$



The fixed-family relation is



$$
2M=5r+14s+7.               \tag{1.3}
$$



The first important fact is that its actual prime rows fill the entire
short prime interval



$$
\boxed{
 \frac{4M+3}{5}\le p\le\frac{6M-1}{7}.}            \tag{1.4}
$$



Therefore the prime number theorem gives the raw Chebyshev mass



$$
\sum_{\substack{p\text{ an actual prime row on }M}}\log p
 =\left(\frac67-\frac45\right)M+o(M)
 =\frac{2M}{35}+o(M).                              \tag{1.5}
$$



After normalization by $6M$, this is exactly



$$
\frac1{105}.               \tag{1.6}
$$



Thus Item 334's direct $O(M^2\log M)$ product-height bound is not the
relevant ceiling; the interval itself already gives the stronger
$O(M)$ bound (1.5).  To reduce capacity, one must prove that the tied
prime fails to divide $\mathfrak G_{r,s}$ on enough rows.  Merely making
each carrier small, recurrent, squarefree, or coprime to other row
carriers is insufficient.

The present item proves two global obstructions:

1. the complete affine resultant/subresultant calculation collapses to
   the old determinant $D$; and
2. on the exact tied row grid, a squarefree, pairwise-coprime,
   constant-order recurrent comparison carrier of pointwise logarithmic
   height $O(\log M)$ still retains the full mass (1.5).

Consequently no smaller rigorous ceiling is obtained:



$$
\boxed{\text{new booking}=0},\qquad
 \boxed{\text{new capacity reduction}=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling}=1/105\text{ per }6M}.
                                                               \tag{1.7}
$$



## 2. The affine target pair

Retain Item 334's notation



$$
U=9cb-11v,\qquad D=\det(f,U),\qquad
 \Phi=c_p+\epsilon h_mP_{r+2}(m),                  \tag{2.1}
$$



and put



$$
K=\frac{9\kappa_rB_s}{2}. \tag{2.2}
$$



The scalar $K$ is a $p$-unit on every actual row.  Before evaluating
the actual Cartier coordinate $\Phi$, introduce an indeterminate $X$
and write the two coupled target polynomials as



$$
\boxed{
 T_\nu(X)=Kf_\nu X
 +(-1)^m\left(f_\nu B_s\tau_{r,s}-U_\nu\right),
 \qquad \nu=0,1.}                                  \tag{2.3}
$$



The actual residuals are $T_\nu=T_\nu(\Phi)$.  Formula (2.3) retains
all moving connection data; only the final Cartier value has temporarily
been left formal.

## 3. Exact resultant and subresultant collapse

For two affine polynomials $a_0X+b_0$ and $a_1X+b_1$, their
coefficient determinant is the resultant



$$
a_0b_1-a_1b_0.             \tag{3.1}
$$



Using (2.3), the $B_s\tau_{r,s}$ terms cancel and give



$$
\begin{aligned}
 \operatorname {Res}_X(T_0,T_1)
 &=K(-1)^m\left[-f_0U_1+f_1U_0\right]\\
 &=\boxed{(-1)^{m+1}KD}.                            \tag{3.2}
\end{aligned}
$$



> **PROVED - target-affine resultant collapse.**  On every actual row,
> 

$$
> \boxed{
> p\mid\operatorname {Res}_X(T_0,T_1)
> \quad\Longleftrightarrow\quad p\mid D.}          \tag{3.3}
>
$$


> The resultant contains exactly the old determinant gate, multiplied by
> a certified unit.  It supplies no second divisor and no reduction of the
> primitive carrier.

Because both polynomials have degree one, their complete subresultant
chain contains only their leading coefficients $Kf_0,Kf_1$ and the
resultant (3.2).  On a chart with one nonzero $f_\nu$, the leading
coefficient is merely the chart pivot.  On $f=0$, the degree drops and
the individual constant coordinates $-(-1)^mU_\nu$ are exactly the
degenerate tests already retained by Item 334.

Thus the whole natural resultant/subresultant class is settled:



$$
\boxed{
 \text{eliminating the Cartier target }X
 \text{ returns }D\text{ and necessarily loses the actual target.}} \tag{3.4}
$$



This is not a claim that target-specific arithmetic is impossible.  It
proves that such arithmetic cannot come from the affine resultant or its
subresultants; it must evaluate $X=\Phi_{r,s}$ and control the numerical
gcd in (1.1).

## 4. Exact fixed-$M$ prime parametrization

Starting from an odd prime $p$ in (1.4), define



$$
m=\frac{5p-4M-3}{2},\qquad
 d=6M-7p+4,qquad
 r=d-4=6M-7p,qquad s=m+1.                         \tag{4.1}
$$



The endpoints in (1.4) are exactly the conditions $m\ge0$ and
$d\ge5$.  Because $p$ is odd, $m$ is integral and $r$ is odd.
If $3\mid r$, then $3\mid p$; this is impossible for the primes in
the interval once $M$ is nontrivial.  Direct substitution gives



$$
p=2r+6s+3,qquad 2M=5r+14s+7.                    \tag{4.2}
$$



Conversely, every actual row satisfying (1.3) gives (4.1) and lies in
(1.4).  This proves a bijection between actual fixed-$M$ prime rows and
the primes in that interval.

Applying $\vartheta(x)=x+o(x)$ at the two endpoints proves (1.5).  No
prime scan or unproved distribution statement is used.

Along the full odd row grid, increasing $p$ by two changes the tied
indices by



$$
(m,d,r,s)\longmapsto
                         (m+5,d-14,r-14,s+5).       \tag{4.3}
$$



This exact linear grid will be used for the information-class obstruction.

## 5. A full-mass comparison carrier on the exact tied grid

For each actual fixed-$M$ row define the comparison triple



$$
\widetilde D_{M,p}=p,qquad
 \widetilde T_{0,M,p}=p,qquad
 \widetilde T_{1,M,p}=p,                            \tag{5.1}
$$



and hence



$$
\boxed{\widetilde{\mathfrak G}_{M,p}=p.}           \tag{5.2}
$$



This is deliberately **not** asserted to equal the actual carrier.  It is
a comparison family on precisely the actual tied row grid, used to test
what qualitative carrier information can logically imply.

It has all of the properties that a height/recurrence/reuse argument might
hope to exploit:

1. it is squarefree on every prime row;
2. distinct prime-row carriers are pairwise coprime;
3. its pointwise logarithmic height is only $O(\log M)$; and
4. on the full grid (4.3),
   

$$
\widetilde{\mathfrak G}_{j+1}
   -\widetilde{\mathfrak G}_j=2,qquad
   \widetilde{\mathfrak G}_{j+2}
   -2\widetilde{\mathfrak G}_{j+1}
   +\widetilde{\mathfrak G}_j=0.                  \tag{5.3}
$$



Nevertheless every actual prime row divides its own carrier, so



$$
\sum_{p\mid\widetilde{\mathfrak G}_{M,p}}\log p
 =\frac{2M}{35}+o(M).                              \tag{5.4}
$$



> **PROVED - carrier information-class no-go.**  On the actual tied row
> grid, even the conjunction of squarefreeness, pairwise coprimality,
> $O(\log M)$ pointwise height, and a constant-coefficient order-two
> recurrence does not imply $o(M)$ tied-prime mass, or any reduction of
> the $1/105$ ceiling.

The theorem is deliberately scoped to qualitative carrier metadata.  It
does not compare the actual values of $\mathfrak G_{r,s}$ with $p$,
and it does not rule out an actual-sequence factor localization or an
average-gcd theorem.

## 6. Why pairwise gcds and product identities do not improve the union bound

Distinct rows on a fixed-$M$ slice have distinct tied primes by (4.2).
The collision condition is rowwise:



$$
p_i\mid\mathfrak G_i.      \tag{6.1}
$$



A bound on $\gcd(\mathfrak G_i,\mathfrak G_j)$ controls only primes
reused by two carriers.  There is no implication in (6.1) that the unique
tied prime $p_i$ divides any other row carrier.  The comparison family
(5.2) makes this sharp: every pairwise gcd is one, yet every row is
selected.

Similarly, a product identity yields at best



$$
\sum_{p_i\mid\mathfrak G_i}\log p_i
 \le\log\operatorname {rad}\left(\prod_i\mathfrak G_i\right), \tag{6.2}
$$



and (5.2) makes the right side exactly the full raw mass.  Therefore:

- pairwise-coprime carriers are not automatically sparse;
- lack of prime reuse is not a Closer theorem; and
- a product formula matters only if it localizes the *tied* prime away
  from most row factors.

This closes pairwise-gcd and carrier-product arguments that use no
additional cross-row implication.  A genuine transfer forcing the tied
prime into another row carrier would be extra arithmetic, not carrier
metadata; no such positive-capacity transfer is proved here.

## 7. The actual carrier is not uniformly tiny

Item 334's canonical replay found carrier bit length at most three on its
334 declared rows.  It would be unsafe to promote that observation.  Exact
evaluation gives



$$
\begin{array}{c|c|c|c}
p&r&s&\mathfrak G_{r,s}\\ \hline
17&1&2&3\\
29&1&4&7\\
331&17&49&23\\
599&7&97&173
\end{array}                                         \tag{7.1}
$$



All four are actual tied rows, and all values are primitive gcds from
(1.1).  In particular, the bounded observation $\mathfrak G\le7$ and
the factor set $\{3,7\}$ already fail by $p=599$.

Equation (7.1) is **EXACT FINITE REPLAY ONLY**.  It proves neither
unboundedness nor a density statement.  Its role is solely to prevent a
small-census conjecture from entering the ledger.

## 8. Strategic conclusion

The strongest globally valid carrier statement remains



$$
W_{\mathfrak G}(M)
 =\sum_{\substack{p\text{ in }(1.4)\\p\mid\mathfrak G_{r(p),s(p)}}}
   \log p
 \le\frac{2M}{35}+o(M).                            \tag{8.1}
$$



The desired closure is



$$
W_{\mathfrak G}(M)=o(M),   \tag{8.2}
$$



or, more modestly, a strict constant improvement in (8.1).  Both remain
**OPEN**.

Item 336 rules out the following as sufficient inputs by themselves:

- affine resultants or subresultants in the formal target;
- bounded-order recurrence or holonomy metadata for a carrier;
- pointwise polylogarithmic height;
- squarefreeness and pairwise coprimality; and
- product identities with no tied-prime factor localization.

An admissible continuation must use actual arithmetic of
$\Phi_{r,s}$ after evaluation, for example a target-specific divisor
localization, a monodromy statement that excludes the tied Frobenius, or
a genuine average theorem for the numerical gcd (1.1).

## 9. Deterministic replay

The companion certificate verifies:

- four exact affine resultant identities and twelve subresultant
  coefficient identities on generic rational planes;
- the fixed-$M$ prime-row bijection over $50\le M\le500$;
- 5,124 comparison-recurrence checks and 1,387 pairwise prime-gcd checks;
- 1,184 exact finite prime rows on those slices; and
- the four primitive carrier values in (7.1).

Every finite count, numerical Chebyshev ratio, and carrier example is
**EXACT FINITE REPLAY ONLY**.  The asymptotic mass theorem follows from
the prime number theorem and the symbolic row bijection, not from the
finite replay.

## 10. Strict labels

### PROVED

- the exact target-affine resultant formula (3.2);
- the complete degree-one subresultant collapse and its scoped no-go;
- the fixed-$M$ prime interval and raw mass $(2/35)M+o(M)$;
- the full-mass comparison carrier on the exact tied grid; and
- the information-class no-go for recurrence, height, squarefreeness,
  pairwise gcd, and uncoupled product metadata.

### EXACT FINITE REPLAY ONLY

- all bounded counts, digests, ratios, and the carrier values (7.1).

### OPEN / NOT CLAIMED

- $W_{\mathfrak G}(M)=o(M)$;
- any strict improvement of the $1/105$ ceiling;
- unboundedness, boundedness, or a distribution law for the actual
  primitive carrier;
- a target-specific factor localization or average-gcd theorem; and
- any new Route-1 booking or global Route-1 conclusion.
