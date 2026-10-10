> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 341 - diagonal affine coordinates and the missing moving-state theorem

Checked: 2026-09-01 (Beijing time)

## 1. Scope, capacity, and strict verdict

Retain the actual ordinary-$j=2$ family



$$
p=2r+6s+3=6m+2d+1,
 \qquad m=s-1,
 \qquad d=r+4,
\tag{1.1}
$$



and Item 338's tied-prime-safe saturated carrier.  Saturation changes
foreign factor support but preserves the exact collision equivalence at
the tied prime.  Thus the raw fixed-$M$ mass and ceiling entering this
item are still



$$
\frac{2}{35}M+o(M),
 \qquad
 \frac1{105}\text{ per }6M.
\tag{1.2}
$$



This item imposes the old determinant gate and the legitimate moving
period target simultaneously.  Its main theorem is an exact normal form.

> **PROVED - diagonal affine-coordinate theorem.**  On the
> $\ell_r\ne0\pmod p$ chart, the determinant residual and the actual
> Cartier target residual are independent affine coordinates in the two
> actual state variables
> 

$$
> c=4^s,\qquad H_m=\sum_{j=0}^m\frac1{8^j}\binom{2j}{j}.
>
$$


> Explicitly,
> 

$$
> \boxed{D=9\ell_r(c-c_r^*)},\qquad
> \boxed{T_\ell=-\epsilon_pK_{r,s}\ell_r(H_m-\Theta_{r,s})},
> \tag{1.3}
>
$$


> where $K_{r,s}=9\kappa_rB_s/2$ and every displayed multiplier is a
> $p$-unit.

> **PROVED - localized elimination no-go.**  The Jacobian of (1.3) is a
> unit.  Hence the localized collision ideal is exactly the ideal of the
> moving point $(c_r^*,\Theta_{r,s})$.  Eliminating the two state
> variables produces no nonzero coefficient-only condition.  All
> resultants, subresultants, and Groebner eliminations using only the
> affine connection equations are therefore exhausted.

> **PROVED - degenerate-chart localization.**  For $p>11$, any
> collision with $\ell_r=0$ forces all three connection-plane minors
> $\ell_r,\mu_r,C_r$ to vanish.  Such a tied prime divides an explicit
> $r$-only primitive triple-minor carrier.

> **PROVED - fixed algebraic state curves are impossible.**  The actual
> state sequence $(4^{m+1},H_m)$ is Zariski dense in $\mathbb A^2$,
> even after restriction to the actual prime rows on the fixed ray
> $r=1$.  Thus no fixed characteristic-zero algebraic curve supplies
> the missing relation between the two state coordinates.

The theorem identifies the first genuinely missing input, but does not
prove weighted zero density.  Therefore



$$
\boxed{\text{new booking}=0},\qquad
 \boxed{\text{new capacity reduction}=0},\qquad
 \boxed{\text{ceiling remains }1/105\text{ per }6M}.
\tag{1.4}
$$



No finite census is promoted.

## 2. The retained connection data

Use Item 334's connection vectors $f,b,v$ and minors



$$
\ell=\det(f,b),\qquad
 \mu=\det(f,v),\qquad
 C=\det(b,v).
\tag{2.1}
$$



The old determinant is



$$
D=9c\ell-11\mu,
 \qquad c=4^s.
\tag{2.2}
$$



The true diagonal Cartier target is



$$
\Phi_{r,s}=c_p+\epsilon_ph_mP_{r+2}(m),
 \qquad
 h_m=\frac1{8^m}\binom{2m}{m}.
\tag{2.3}
$$



Put



$$
K_{r,s}=\frac{9\kappa_rB_s}{2}.
\tag{2.4}
$$



Item 334's exterior target is



$$
T_\ell
 =K_{r,s}\ell\Phi_{r,s}
  +(-1)^m(\ell B_s\tau_{r,s}-11C).
\tag{2.5}
$$



All denominators in (2.1)-(2.5) and the factors $2,3$ are
$p$-units on every actual row.

## 3. Exact centering at the moving point

On the $\ell$-chart define



$$
\boxed{c_r^*=\frac{11\mu_r}{9\ell_r}},
\tag{3.1}
$$



and



$$
\boxed{
 \Phi_{r,s}^*
 =(-1)^{m+1}\frac{2}{9\kappa_r}
   \left(\tau_{r,s}-\frac{11C_r}{\ell_rB_s}\right).}
\tag{3.2}
$$



Direct subtraction in (2.2) and (2.5) gives the characteristic-zero
identities



$$
\boxed{D=9\ell_r(c-c_r^*)},
 \qquad
 \boxed{T_\ell=K_{r,s}\ell_r(\Phi_{r,s}-\Phi_{r,s}^*)}.
\tag{3.3}
$$



No recurrence, interpolation, or finite observation enters (3.3).

Item 331's exact diagonal Cartier bridge is



$$
H_m=\epsilon_p(1-c_p)\pmod p.
\tag{3.4}
$$



Combining (2.3) and (3.4),



$$
\Phi_{r,s}
 \equiv1-\epsilon_p(H_m-h_mP_{r+2}(m))\pmod p.
\tag{3.5}
$$



Define



$$
\boxed{
 \Theta_{r,s}
 =h_mP_{r+2}(m)+\epsilon_p(1-\Phi_{r,s}^*).}
\tag{3.6}
$$



Then



$$
\Phi_{r,s}-\Phi_{r,s}^*
 \equiv-\epsilon_p(H_m-\Theta_{r,s})\pmod p.
\tag{3.7}
$$



Substitution in (3.3) proves the promised coupled normal form



$$
\boxed{
 (D,T_\ell)
 =\left(9\ell_r(c-c_r^*),
       -\epsilon_pK_{r,s}\ell_r(H_m-\Theta_{r,s})\right)
       \pmod p.}
\tag{3.8}
$$



Item 319's branch formulae also give



$$
\ell_r=2\sigma_{e,n}\mathfrak a_r,qquad
 \mu_r=-\sigma_{e,n}\mathfrak b_r,
\tag{3.9}
$$



so



$$
\boxed{c_r^*=-\frac{11\mathfrak b_r}{18\mathfrak a_r}.}
\tag{3.10}
$$



Thus the first coordinate of the moving point is exactly the selected
Item-314 gate root, not a new norm factor.

## 4. The affine ideal is already complete

Work over the actual residue field on the chart where
$\ell_rK_{r,s}\ne0$.  Treat $c,H$ as state variables and all
connection quantities as coefficients.  From (3.8),



$$
\frac{\partial(D,T_\ell)}{\partial(c,H)}
 =\begin{pmatrix}
   9\ell_r&0\\
   0&-\epsilon_pK_{r,s}\ell_r
  \end{pmatrix}.
\tag{4.1}
$$



Its determinant is



$$
\boxed{-9\epsilon_pK_{r,s}\ell_r^2
 =-\epsilon_p\frac{81\kappa_rB_s}{2}\ell_r^2,}
\tag{4.2}
$$



a unit.  Consequently



$$
\boxed{(D,T_\ell)=(c-c_r^*,H-\Theta_{r,s})}
\tag{4.3}
$$



in the localized polynomial ring.

Evaluation at $(c_r^*,\Theta_{r,s})$ identifies the quotient with the
coefficient field.  Hence



$$
(D,T_\ell)\cap R=(0)
\tag{4.4}
$$



for the coefficient ring $R$.  In particular:

- eliminating $H$ returns only the old determinant coordinate;
- eliminating $c$ returns only the moving period coordinate;
- eliminating both produces no coefficient-only divisor; and
- the nonzero Jacobian rules out a hidden multiplicity or tangency
  condition.

> **PROVED - scoped algebraic no-go.**  No resultant, subresultant,
> determinant, norm, or Groebner-basis calculation formed solely from
> the two affine connection equations can reduce the collision support.
> A new condition must come from arithmetic of the actual state
> $(4^s,H_m)$, not from another elimination of the connection plane.

This is stronger than saying that one chosen resultant collapses: (4.3)
identifies the entire localized ideal.

## 5. The complete degenerate-chart localization

The $\ell$-chart does not silently discard zero-minor rows.  Suppose
$p>11$, $D=0$, and $\ell=0\pmod p$.  Equation (2.2) gives



$$
\mu=0\pmod p.
\tag{5.1}
$$



If $C\ne0\pmod p$, then $b,v$ are independent and $f=0$.  The
original affine vector becomes $9cb-11v$, which cannot vanish because
independent vectors cannot be proportional.  Hence every degenerate
collision also forces



$$
C=0\pmod p.
\tag{5.2}
$$



Define the primitive $r$-only Pluecker content



$$
\boxed{
 \mathfrak P_r
 =\gcd\bigl(|\operatorname {num}\ell_r|,
            |\operatorname {num}\mu_r|,
            |\operatorname {num}C_r|\bigr).}
\tag{5.3}
$$



The reduced denominators are actual-row $p$-units.  Therefore



$$
\boxed{
 p>11,\ p\text{ a degenerate collision}
 \quad\Longrightarrow\quad p\mid\mathfrak P_r.}
\tag{5.4}
$$



At $p=11$, (1.1) has only the row $(r,s)=(1,1)$, so this exceptional
characteristic has zero asymptotic mass.

Formula (5.4) is a genuine divisor localization, but its fixed-$M$
weighted support is **OPEN**.  Individual height again sums to a bound
larger than the raw $O(M)$ ceiling.  Thus (5.4) identifies, rather than
solves, the degenerate branch's first arithmetic task.

## 6. The actual state lies on no fixed algebraic curve

The affine ideal theorem says that a further algebraic elimination would
need a relation between $c=4^{m+1}$ and $H_m$.  There is no fixed
characteristic-zero relation of this kind.

Put



$$
\delta_m=\sqrt2-H_m.
\tag{6.1}
$$



The binomial series gives



$$
\sum_{j=0}^{\infty}\frac1{8^j}\binom{2j}{j}=\sqrt2.
\tag{6.2}
$$



Stirling's formula and the ratio of successive terms give



$$
\frac1{8^j}\binom{2j}{j}
 \sim\frac{2^{-j}}{\sqrt{\pi j}},
 \qquad
 \boxed{\delta_m\sim\frac{2^{-m}}{\sqrt{\pi m}}.}
\tag{6.3}
$$



> **PROVED - Zariski density.**  For every unbounded set
> $\mathcal S\subseteq\mathbb N$, the points
> 

$$
> \bigl(4^{m+1},H_m\bigr),\qquad m\in\mathcal S,
> \tag{6.4}
>
$$


> are not contained in the zero set of any nonzero polynomial in
> $\mathbb C[X,Y]$.

To prove this, suppose $P(4^{m+1},H_m)=0$ on an unbounded
$\mathcal S$.  After the exact finite expansion around $Y=\sqrt2$,



$$
P(X,\sqrt2-\delta)=\sum_{i,k}a_{i,k}X^i\delta^k.
\tag{6.5}
$$



For every nonzero term, (6.3) gives



$$
(4^{m+1})^i\delta_m^k
 \sim4^i\pi^{-k/2}
      2^{(2i-k)m}m^{-k/2}.
\tag{6.6}
$$



Choose a nonzero pair $(i,k)$ maximizing $2i-k$, and among ties
minimizing $k$.  It is the unique dominant term in (6.5): equality of
both ordering parameters forces equality of $i,k$.  The sum therefore
cannot vanish along an unbounded sequence, a contradiction.

This statement applies to actual prime rows.  On the fixed ray $r=1$,



$$
p=6m+11.
\tag{6.7}
$$



Every prime $p\equiv5\pmod6$, $p\ge11$, gives such an actual row,
and Dirichlet's theorem supplies infinitely many.  Taking their
corresponding unbounded set of $m$'s in (6.4) proves Zariski density
even on this actual-prime subsequence.

The theorem closes fixed algebraic-curve compression.  It does not rule
out a moving relation whose coefficients depend on $m,r,p$, a
finite-field Frobenius relation, or a distribution theorem modulo the
changing prime.

## 7. Exact remaining weighted problem

For $p>11$, split actual rows on a fixed-$M$ slice into the disjoint
charts $\ell_r\ne0$ and $\ell_r=0$.  Equations (3.8) and (5.4) give



$$
\begin{aligned}
 W_M^{\rm nd}
 &=\sum_{\substack{(r,s)\in\mathcal R_M\\
 4^s\equiv c_r^*\ (p)\\
 H_m\equiv\Theta_{r,s}\ (p)}}\log p,\\
 W_M^{\rm deg}
 &\leq\sum_{\substack{(r,s)\in\mathcal R_M\\
 p\mid\mathfrak P_r}}\log p.
\end{aligned}
\tag{7.1}
$$



The original collision mass is at most



$$
W_M^{\rm nd}+W_M^{\rm deg}+O(1).
\tag{7.2}
$$



The sufficient Closer target is



$$
\boxed{W_M^{\rm nd}+W_M^{\rm deg}=o(M).}
\tag{7.3}
$$



No current theorem proves either summand sublinear.  The exact first
missing inputs are now separated:

1. an average-gcd or weighted-support theorem for the $r$-only triple
   content $\mathfrak P_r$; and
2. on the nondegenerate chart, a genuinely moving mod-$p$ theorem for
   the simultaneous hit of $(4^s,H_m)$ against
   $(c_r^*,\Theta_{r,s})$.

The second input could take the form of a target-specific Frobenius
module, monodromy/equidistribution, a large sieve for the joint state, or
a sequence-specific average gcd.  It cannot be replaced by another
connection-plane elimination or a fixed characteristic-zero state curve.

## 8. Deterministic replay and strict labels

The certificate verifies:

- three generic exact rational instances of the centered identities and
  nonzero Jacobian;
- seven actual tied rows, including three old determinant hits;
- the diagonal Cartier-to-$H_m$ substitution and centered target;
- rank-one Pluecker identities and the impossible $C\ne0$ chart;
- the exact $h_m,H_m,4^{m+1}$ state through $m=120$; and
- the unique asymptotic ordering key on 169 declared exponent pairs.

The bounded rows, counts, samples, and digests are **EXACT FINITE ONLY**.
The centered identities (3.3), diagonal normal form (3.8), ideal theorem
(4.3)-(4.4), degenerate localization (5.4), and Zariski-density proof
(6.1)-(6.7) are **PROVED**.

The following remain **OPEN**:

- both weighted bounds in (7.3);
- any strict reduction of the $1/105$ ceiling;
- any positive Route 1 booking from ordinary $j=2$; and
- every moving finite-field/Frobenius relation not covered by the fixed
  algebraic-curve no-go.
