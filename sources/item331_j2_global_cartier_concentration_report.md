> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 331 - global Cartier-coefficient concentration and the fixed-target dichotomy

Checked: 2026-09-01 (Beijing time)

## 1. Scope and strict verdict

Retain the actual ordinary-$j=2$ rows



$$
p=2r+6s+3,\qquad r\geq1\text{ odd},\qquad3\nmid r,
 \qquad s\geq1,                                      \tag{1.1}
$$



and Item 328's tied variables



$$
m=s-1,\qquad d=r+4,\qquad n=3m+d=\frac{p-1}{2},
 \qquad q=2m+d,\qquad p=6m+2d+1.                    \tag{1.2}
$$



For



$$
\mathcal F_{m,d}(x)=(1-x)^n(1+x)^{n+q}
 =\sum_kc_kx^k,                                    \tag{1.3}
$$



Item 328 proved that, after the old determinant gate and on the
$\ell_r\ne0\pmod p$ chart, the original collision is exactly



$$
c_p=1-\epsilon\Theta_{r,s}\pmod p,
 \qquad \epsilon=\left(\frac2p\right).              \tag{1.4}
$$



The present item studies the globally visible coefficient $c_p$, rather
than another bounded-depth recurrence around its Frobenius break.

Put



$$
\boxed{A_m=\sum_{j=0}^m8^{m-j}\binom{2j}{j}},
 \qquad
 H_m=\frac{A_m}{8^m}.                               \tag{1.5}
$$



> **PROVED - one fixed rational constant-term kernel.**  If
> 

$$
>  \mathscr A(x)=(1-x)^3(1+x)^5,\qquad
>  \mathscr B(x)=(1-x)(1+x)^2,
>
$$


> then, over $\mathbf Z$,
> 

$$
> \boxed{
> c_{6m+2d+1}
> =\operatorname {CT}_x x^{-1}
>   \left(\frac{\mathscr A(x)}{x^6}\right)^m
>   \left(\frac{\mathscr B(x)}{x^2}\right)^d.}     \tag{1.6}
>
$$


> Thus the whole tied coefficient array is a fixed rational
> constant-term array, not a polynomial family that changes with $p$.

> **PROVED - global Frobenius concentration.**  On every actual row,
> 

$$
> \boxed{8^m c_p\equiv8^m-\epsilon A_m\pmod p.}     \tag{1.7}
>
$$


> Consequently, on a fixed-$m$ ray the coefficient has only the two
> rational values
> 

$$
>                  C_m^{\epsilon}=1-\epsilon H_m,   \tag{1.8}
>
$$


> selected solely by the residue class of $p$ modulo $8$.

> **PROVED - positive-mass fixed-value fibres.**  For each fixed
> $m\geq0$ and $\epsilon\in\{1,-1\}$, one reduced class
> $a_{m,\epsilon}\pmod8$ consists, apart from finitely many small
> primes, entirely of actual rows with
> $c_p=C_m^\epsilon\pmod p$.  Explicitly,
> 

$$
> \begin{array}{c|cc}
> &\epsilon=1&\epsilon=-1\\ \hline
> m\text{ even}&7&3\\
> m\text{ odd}&1&5
> \end{array}\pmod8.                                \tag{1.9}
>
$$


> The prime number theorem in arithmetic progressions therefore gives
> 

$$
> \boxed{
> \sum_{\substack{p\le X\\p\equiv a_{m,\epsilon}\ (8)}}\log p
> \sim\frac X4.}                                    \tag{1.10}
>
$$


> In particular, the actual $m=0$ ray satisfies
> 

$$
> \boxed{c_p=0\pmod p\quad(p\equiv7\pmod8)},\qquad
> \boxed{c_p=2\pmod p\quad(p\equiv3\pmod8)},       \tag{1.11}
>
$$


> for every sufficiently large prime in the indicated class.

> **PROVED - all fixed rational targets are localized exactly.**  Let
> $a=u/v\in\mathbf Q$, with $\gcd(u,v)=1$.  On a fixed
> $(m,\epsilon)$ ray and for $p\nmid2v$,
> 

$$
> \boxed{
> c_p=a\pmod p
> \quad\Longleftrightarrow\quad
> p\mid N_{m,\epsilon}(a),}
> \quad
> N_{m,\epsilon}(a)
> =v(8^m-\epsilon A_m)-u8^m.                        \tag{1.12}
>
$$


> If $a=C_m^\epsilon$, the integer in (1.12) is zero and the
> equality has the positive mass (1.10).  For every other fixed target
> it is a nonzero fixed integer, so the equality is supported on only
> finitely many primes.

Equations (1.10)-(1.11) disprove universal nonvanishing of $c_p$ and,
more strongly, every proposed uniform fixed-value zero-density or
equidistribution theorem for $c_p$ alone on all actual rows.  This is a
global coefficient-method no-go, but its scope is exact: it says nothing
against a theorem that retains the moving target $\Theta_{r,s}$, the old
determinant gate, and the actual connection data.

No such target-coupled theorem is obtained here.  Hence the strict ledger
effect is



$$
\boxed{\text{new booking}=0},\qquad
 \boxed{\text{new capacity reduction}=0},\qquad
 \boxed{\text{ordinary-}j=2\text{ ceiling}=1/105\text{ per }6M}.
                                                               \tag{1.13}
$$



## 2. Admission, capacity, and the actual implication

The coefficient in (1.3) is admitted because Item 328 proved the unit
equivalence



$$
H_m=\Theta_{r,s}\pmod p
 \quad\Longleftrightarrow\quad
 c_p=1-\epsilon\Theta_{r,s}\pmod p                 \tag{2.1}
$$



after the already retained determinant gate and on the
$\ell_r\ne0$ chart.  Thus $c_p$ is not an auxiliary moment.  It is
exactly the remaining incomplete period in Cartier coordinates.

The raw isolated ordinary-$j=2$ ceiling is still



$$
\mathcal C_{\max}=\frac1{105}
                 \quad\text{per }6M.               \tag{2.2}
$$



Even perfect avoidance in (2.1) would only close this branch; it would not
fill the Route-1 deficit.  Conversely, the positive mass in (1.10) must
not be booked.  It is mass in the prime variable while $m$ is fixed,
and it does not impose either the determinant gate or the target equality.

There is also a fixed-$M$ thinness check.  From Item 328,



$$
2M=14m+5d+1.               \tag{2.3}
$$



For fixed $m$, equation (2.3) determines at most one $d$, hence at
most one row, in a fixed-$M$ slice.  Any fixed finite set of horizontal
rays therefore has total weight $O(\log M)=o(M)$.  Thus (1.10) is a
decisive obstruction to a *uniform coefficient-only theorem*, not a new
positive-capacity mechanism.

The $\ell_r=0$ and rank-at-most-one charts remain outside (2.1), exactly
as in Items 322 and 328.  Nothing in this item discards them.

## 3. A fixed rational constant-term model

The tied exponents split as



$$
n=3m+d,\qquad n+q=5m+2d.                          \tag{3.1}
$$



Therefore



$$
\mathcal F_{m,d}(x)
 =\bigl((1-x)^3(1+x)^5\bigr)^m
  \bigl((1-x)(1+x)^2\bigr)^d
 =\mathscr A(x)^m\mathscr B(x)^d.                 \tag{3.2}
$$



Since the requested coefficient index is $6m+2d+1$, multiplying the
coefficient extractor by the two matching Laurent monomials gives (1.6).
Equivalently, the entire two-parameter array has the fixed rational
generating kernel



$$
\boxed{
 \sum_{m,d\ge0}c_{6m+2d+1}y^mz^d
 =\operatorname {CT}_x
   \frac{x^7}
   {(x^6-y\mathscr A(x))(x^2-z\mathscr B(x))}.}     \tag{3.3}
$$



This is a genuine global realization: neither its numerator nor its two
denominator polynomials depends on $m,d,p$.  However, a rational
constant-term representation is structural metadata, not a zero-density
theorem.  Sections 4-6 show why its coefficient-only specialization is in
fact maximally concentrated on horizontal rays.

## 4. Exact Frobenius collapse to an integer numerator

Item 328's Cartier identity is



$$
H_m=\epsilon(1-c_p)\pmod p. \tag{4.1}
$$



The individual summands have the elementary form



$$
h_j=\frac{(1/2)_j}{j!2^j}
     =\frac1{8^j}\binom{2j}{j}.                    \tag{4.2}
$$



Thus (1.5) is an integer and $H_m=A_m/8^m$.  Multiplication of (4.1)
by the $p$-unit $8^m$, followed by $\epsilon^2=1$, proves (1.7).
No interpolation, finite scan, or characteristic-zero lifting is used.

The full generating series also gives a convenient height bound:



$$
1\le H_m<\sum_{j\ge0}\binom{2j}{j}8^{-j}
 =(1-4/8)^{-1/2}=\sqrt2.                            \tag{4.3}
$$



Hence



$$
0<A_m<\sqrt2\,8^m.         \tag{4.4}
$$



This bound will make the fixed-target divisor estimate completely
explicit.  It is not, by itself, strong enough for a moving-$m$
fixed-$M$ density theorem.

## 5. Actual horizontal rays and positive Chebyshev mass

Fix $m\ge0$, put $s=m+1$, and let $p>6m+9$ be an odd prime.  The
only possible value of $r$ is



$$
r=\frac{p-6m-9}{2}.        \tag{5.1}
$$



It is odd exactly when



$$
p\equiv2m+3\pmod4.         \tag{5.2}
$$



If $3\mid r$, equation (1.1) would give $3\mid p$, impossible for
the primes under consideration.  Therefore (5.2), together with the
finite lower bound, is the complete actual-row condition on a fixed
$m$ ray.

Euler's criterion gives



$$
\left(\frac2p\right)=
 \begin{cases}
  1,&p\equiv1,7\pmod8,\\
 -1,&p\equiv3,5\pmod8.
 \end{cases}                                        \tag{5.3}
$$



Intersecting (5.2) and (5.3) yields exactly the four classes in (1.9).
For every sufficiently large prime in one such class, (1.7) yields the
same rational residue (1.8).  The prime number theorem for the fixed
reduced progression modulo $8$ proves (1.10).

At $m=0$, $A_0=1$ and $H_0=1$.  Formula (1.8) is therefore $0$
when $\epsilon=1$ and $2$ when $\epsilon=-1$, proving (1.11).  In
particular,



$$
\sum_{\substack{p\le X\\p\equiv7\ (8)\\c_p=0\ (p)}}\log p
 \sim\frac X4.                                      \tag{5.4}
$$



Thus even coefficient *vanishing* has positive Chebyshev mass inside the
declared actual family.  A claim that $c_p$ is universally nonzero, or
that every fixed residue fibre has $o(X)$ mass, is not merely unproved;
it is false.

## 6. Complete divisor localization for fixed rational targets

Let $a=u/v$ be reduced and exclude the finitely many primes dividing
$2v$.  Combining (1.7) with $vc_p=u$ gives



$$
\begin{aligned}
 c_p=a\pmod p
 &\Longleftrightarrow
 v(8^m-\epsilon A_m)-u8^m=0\pmod p\\
 &\Longleftrightarrow p\mid N_{m,\epsilon}(a),
\end{aligned}                                       \tag{6.1}
$$



which is (1.12).  If $N_{m,\epsilon}(a)\ne0$, then



$$
\sum_{\substack{p:\ c_p=a\ (p)\\
                  p\text{ on the fixed }(m,\epsilon)\text{ ray}}}
       \log p
 \le\log|N_{m,\epsilon}(a)|.                       \tag{6.2}
$$



By (4.4),



$$
|N_{m,\epsilon}(a)|
 <\bigl(|u|+(1+\sqrt2)|v|\bigr)8^m,                \tag{6.3}
$$



so the right side of (6.2) is at most



$$
m\log8+O_{u,v}(1).                \tag{6.4}
$$



If $N_{m,\epsilon}(a)=0$, then $a=C_m^\epsilon$, and every
sufficiently large prime in the class (1.9) satisfies the equality.  This
proves a sharp dichotomy for *every fixed rational target*: the support is
either a positive-mass full progression or a finite divisor set.

The dichotomy does not extend to (1.4) by replacing
$a$ with $1-\epsilon\Theta_{r,s}$.  That target carries the moving
connection data $P_{r+2}(m),\kappa_r,\tau_{r,s},C_r/\ell_r$, and
$B_s$.  Clearing it produces an $(r,s)$-dependent integer, not the
fixed integer in (6.1).  Dropping this dependence would drop the logical
link to the original collision.

## 7. The scoped global coefficient-method no-go

Define the **coefficient-only fixed-target class** to consist of arguments
whose final exclusion step uses only $c_p$ and a characteristic-zero
rational target on a horizontal ray, without retaining the determinant
gate or any of the connection-plane target data.

Sections 5-6 settle this entire class:

1. at the natural target $C_m^\epsilon$, zero density is false, with
   exact Chebyshev mass $X/4+o(X)$;
2. at every other fixed rational target, the support is already the finite
   divisor set (6.1); and
3. neither alternative addresses the moving target in (1.4).

Consequently, a factorization of the integer coefficient, an algebraic or
rational diagonal realization, a P-recursive description, or a
fixed-value Frobenius equidistribution statement cannot close the actual
branch **unless it is coupled to $\Theta_{r,s}$ and the determinant
gate**.  The conclusion here is not that every global coefficient method
is impossible.  It closes the broad but precisely defined class that
forgets the affine target.

This also explains why (1.6) is not promoted as a new representation item:
its arithmetic consequence is the concentration/no-go theorem, not merely
the existence of another coefficient extractor.

## 8. What remains open

The legitimate weighted target remains



$$
\boxed{
 \sum_{\substack{
 p\text{ in the actual fixed-}M\text{ family}\\
 p\mid D_{r,s},\ \ell_r\ne0\ (p)\\
 c_p=1-\epsilon\Theta_{r,s}\ (p)}}\log p=o(M).}     \tag{8.1}
$$



Equation (8.1) is **OPEN**.  No positive density of its collision primes
is asserted either.  A viable continuation must study a target-coupled
object, for example a cleared gcd/resultant between the fixed rational
Cartier array and the actual connection sequence, or an average theorem
for that coupled pair.  Studying the marginal distribution of $c_p$
alone is now ruled out as a Closer strategy.

The following also remain open:

- a target-retaining divisor whose total logarithmic mass is $o(M)$;
- a fixed-conductor Frobenius object that contains the moving affine
  target rather than only $c_p$;
- an average-gcd theorem along $2M=14m+5d+1$; and
- any reduction of the ceiling (2.2).

## 9. Deterministic certificate

The companion certificate independently checks:

- the exact integer constant-term coefficient identity and reciprocity on
  a declared generic $(m,d)$ box;
- (1.7) on 503 actual rows through $p\le257$;
- the fixed-ray residue classes and concentrations on 1,007 actual rows
  with $m\le12$ and $p\le997$;
- 7,049 exact fixed-target divisor equivalences for seven declared
  rational targets; and
- the $m=0$ values $0$ and $2$ on the two relevant progressions.

All these counts are **EXACT FINITE REPLAY ONLY**.  The all-row identities
are proved symbolically above, and the asymptotic (1.10) is an application
of the prime number theorem in arithmetic progressions, not an
extrapolation from the replay.

## 10. Strict outputs

### PROVED

- the fixed rational constant-term kernel (1.6)-(3.3);
- the global numerator collapse (1.7);
- the actual fixed-ray classification (1.9);
- positive Chebyshev mass of the natural fixed-value fibres (1.10),
  including the zero fibre (1.11);
- the complete fixed-rational-target divisor dichotomy (1.12); and
- the scoped no-go for coefficient-only fixed-target methods.

### EXACT FINITE REPLAY ONLY

- every bounded check and digest listed in Section 9.

### OPEN / NOT CLAIMED

- the actual affine-target density theorem (8.1);
- any theorem on the $\ell_r=0$ or rank-at-most-one charts beyond the
  inherited division-free formulation;
- any new booking or capacity reduction; and
- any Route-1 completion or no-go conclusion from this branch alone.
