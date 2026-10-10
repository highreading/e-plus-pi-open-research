> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Weighted Cayley residues: exact three-term no-go at the first propagation row

## 1. Statement and scope

Let



$$
P(z)=1+z+z^2+z^3,
 \qquad
 \alpha=\frac{2q-3}{3},
$$



and



$$
J_s=\frac{P(z)^{\alpha-s}}{z^q(1-z)^q}\,dz,
 \qquad
 B_s=2\operatorname {Res}_0J_s+\operatorname {Res}_1J_s.
$$



Here $q$ is a positive odd integer with $3\nmid q$.  On a valid
fresh-prime ray,



$$
p=6m+q>6m,\qquad m\geq1,
$$



and all formulas are reduced modulo $p$.

There is an exact rational three-term telescoper among $B_0,B_1,B_2$,
but the same propagation argument would next require one among
$B_1,B_2,B_3$.  This note proves that no such *uniform rational
telescoper* exists in the formal nonresonant connection.  After reduction
on valid rays, its natural Hermite matrix is invertible except at the
single valid rank drop $p=10m+3$, whose sole content is the already-known
identity $B_2=0$ and has no $B_3$ term.  Thus the rational rank-two
intuition does not propagate the initial common zero.

This is a uniform no-go theorem for this recurrence mechanism, not a proof
of fresh-prime coprimality.  It does not exclude prime-specific
characteristic-$p$ certificates with higher $P$-pole order at a
resonant integral exponent.

## 2. Complete Hermite ansatz at $s=1$

Seek a rational telescoping identity



$$
a_0+\frac{a_1}{P}+\frac{a_2}{P^2}
 =H'+H\left(
 -\frac qz+\frac q{1-z}+(\alpha-1)\frac{P'}P
 \right).                                                \tag{2.1}
$$



Multiplication by $J_1$ and taking residues would give



$$
a_0B_1+a_1B_2+a_2B_3=0.                                \tag{2.2}
$$



Over the formal characteristic-zero field $\mathbb Q(q)$, the following
ansatz is complete, not merely a bounded search:



$$
H=\frac{z(1-z)U(z)}{P(z)},\qquad \deg U\leq7.            \tag{2.3}
$$



Indeed, a pole of $H$ away from $0,1$, and the roots of $P$,
would create an uncancelled pole in (2.1).  At $0$ and $1$, the
right side of (2.1) is regular, so $H$ must vanish.  At a root of the
squarefree polynomial $P$, the right side has pole order at most two.
Because



$$
\alpha-1=\frac{2q-6}{3}
$$



is not an integer when $3\nmid q$, no higher-pole resonance is possible;
hence $H$ has at most a simple $P$-denominator.

Finally, if $r=\deg U$, then $H\sim z^{r-1}$ at infinity, while the
logarithmic derivative in (2.1) is



$$
-\frac6z+O(z^{-2}).
$$



The leading term of $H'+H(\log J_1)'$ is therefore proportional to
$(r-7)z^{r-2}$.  Since the left side of (2.1) is bounded at infinity,
one must have $r\leq7$; the case $r=7$ is the sole leading-term
resonance.  This proves (2.3).

## 3. Exact determinant

Write



$$
U=u_0+u_1z+\cdots+u_7z^7.
$$



After substituting (2.3) into (2.1), clear denominators and equate the
eleven coefficients of $z$.  In descending coefficient order and with
column order



$$
(u_0,u_1,\ldots,u_7,a_0,a_1,a_2),
$$



the resulting system is an $11\times11$ homogeneous matrix.  Its exact
determinant is



$$
\boxed{
 2^9 3^7 7\,(q-3)(2q-9)^2(5q-9)(5q-6).}         \tag{3.1}
$$



Consequently, outside the factors displayed in (3.1), (2.1) has only the
zero solution.  In particular, the uniform rational telescoper that would
turn $B_1=B_2=0$ into $B_3=0$ does not exist.

## 4. Every determinant factor on a valid ray

The factors $2$ and $3$ are units.  The factor $q-3$ cannot vanish:
$0<q<p$ and $3\nmid q$.

### The factor $2q-9$

Since $-p<2q-9<2p$ for $p>7$, divisibility by $p$ would force
$2q-9=p$.  Together with $p=6m+q$, this gives
$p=12m+9$, a composite multiple of three.  The only endpoint missed by
that inequality is



$$
(p,m,q)=(7,1,1).
$$



A direct row reduction over $\mathbb F_7$ gives matrix rank nine and
nullity two, but both nullvectors have



$$
(a_0,a_1,a_2)=(0,0,0).
$$



Thus even this rank drop gives no recurrence among the $B_s$ within the
reduced simple-pole Hermite system.

### The factor $5q-9$

If $5q-9=kp$, then $k\in\{1,2,3,4\}$ and



$$
(5-k)q=6km+9.                                      \tag{4.1}
$$



For $k=1$ or $3$, parity makes (4.1) impossible.  For $k=4$,
it gives $3\mid q$.  The sole valid case is $k=2$:



$$
q=4m+3,\qquad p=10m+3.                             \tag{4.2}
$$



Modulo this prime, $q=9/5$.  Substitution into the exact system leaves
a one-dimensional nullspace with



$$
(a_0,a_1,a_2)=(0,1,0)
$$



and



$$
H=\frac5{16}z(1-z)(5z^4-4).                        \tag{4.3}
$$



Direct differentiation gives



$$
H'+H\left(
 -\frac qz+\frac q{1-z}+(\alpha-1)\frac{P'}P
 \right)=\frac1P
 \qquad(q=9/5).                                    \tag{4.4}
$$



Hence $J_2=d(HJ_1)$ and $B_2=0$.  This is precisely the known
exceptional-ray vanishing of $\Lambda_2$; because the coefficient of
$B_3$ is zero, (4.4) supplies no forward propagation.

### The factor $5q-6$

Writing $5q-6=kp$, with $k\in\{1,2,3,4\}$, gives



$$
(5-k)q=6km+6.
$$



For $k=1$, the resulting $p$ is a composite multiple of three.  The
case $k=2$ makes $q$ even, $k=3$ makes $3\mid q$, and $k=4$
again makes $q$ even.  Thus this factor never vanishes on a valid prime
ray.

The remaining constant factor $7$ has already been handled by the direct
$p=7$ calculation.

## 5. Conclusion

The initial rational telescoper for $B_0,B_1,B_2$ is an isolated
$s=0$ phenomenon.  At the very next row:

* the complete formal simple-pole Hermite system is invertible after
  reduction on every valid nonexceptional ray;
* $p=7$ has no nullvector with nonzero recurrence coordinates; and
* $p=10m+3$ has only the degenerate relation $B_2=0$.

Therefore the sought uniform rational three-term connection cannot
propagate $B_0=B_1=B_2=0$ to a terminal nonzero anchor.  Any successful
proof must use information beyond this rational three-term de Rham
recurrence, such as the prime-specific Cartier line.  The calculation does
not rule out higher-pole characteristic-$p$ resonant identities; those
would already use precisely such extra prime-specific information.

The deterministic certificate is
`scripts/weighted_cayley_three_term_no_go.py`; its byte-stable output is
`results/weighted_cayley_three_term_no_go.json`.
