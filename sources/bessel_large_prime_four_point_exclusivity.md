> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Four-point exclusivity for large-prime Bessel valuations

Checked: 2026-08-27 UTC.

## 1. The theorem

Let



$$
q_0=q_1=1,\qquad
 q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\geq2).
\tag{1}
$$



Fix a prime $p$ and consider precisely the range relevant to
$p>n/2$:



$$
0\leq n<2p.
\tag{2}
$$



For $p\geq5$, let $r\in\{0,\ldots,(p-1)/2\}$ satisfy
$p\mid q_r$, and put



$$
s=p-1-r,\qquad
 c={q_r\over p}\pmod p,\qquad
 \delta={-q_{r+p}-q_r\over p}\pmod p.
\tag{3}
$$



The quotients in (3) are defined only after the displayed hypothesis
$p\mid q_r$.  The four indices in the reflection orbit and its first
anti-period translate are



$$
r,\quad s,\quad r+p,\quad s+p.
\tag{4}
$$



When $r<s$, these are four distinct integers in $[0,2p)$, and every
index in $[0,2p)$ whose residue is in the reflection pair
$\{r,s\}$ occurs exactly once in (4).  Their divided values obey the
exact first-lift table



$$
\boxed{
 \left(
 {q_r\over p},
 {q_s\over p},
 {q_{r+p}\over p},
 {q_{s+p}\over p}
 \right)
 \equiv
 \left(c,c-\delta,-c-\delta,-c+2\delta\right)
 \pmod p.}
\tag{5}
$$



Consequently:

1. If $\delta\ne0$, at most one of the four integers in (5) is
   divisible by $p$.  Equivalently, at most one of the four original
   values has $p$-adic valuation at least two, and each of the other
   three has valuation exactly one.

2. If $\delta=0$, either all four original values have valuation exactly
   one (when $c\ne0$), or all four have valuation at least two (when
   $c=0$).

At the central fixed point $r=s=(p-1)/2$, one necessarily has
$\delta=0$.  The orbit in (4) then has only the two distinct indices
$r,r+p$, and



$$
{q_r\over p}\equiv c,\qquad
 {q_{r+p}\over p}\equiv-c\pmod p.
\tag{6}
$$



Thus the two central values both have valuation exactly one or both have
valuation at least two.  For $p=2,3$ there is no root in $[0,2p)$, so
the theorem is vacuous there.

This is an all-prime multiplicity theorem for the full large-prime window,
not a finite-grid extrapolation.  It is also deliberately narrower than a
uniform exponent bound: the one exceptional value in an ordinary orbit can
still have arbitrarily large valuation as far as this argument shows, and a
singular orbit with $c=0$ remains a fully branching obstruction.

## 2. The universal congruences

We use the following already proved recurrence congruences.  For every odd
prime $p$ and every $n\geq0$,



$$
q_{n+p}\equiv-q_n\pmod p
\tag{7}
$$



and



$$
q_{n+2p}+2q_{n+p}+q_n\equiv2p q_n\pmod {p^2}.
\tag{8}
$$



The complete factorial proof of (8), including its two initial values, is
in the frozen dependency

    sources/bessel_denominator_zero_gap_smooth_radical_barrier.md

with SHA-256

    dac7cd496b4342a8afc6d379274986d2030bc327c9017b3f6fa877108e62e1fc.

We also use the odd-modulus reflection congruence



$$
q_{M-1-u}\equiv q_u\pmod M\qquad(M\text{ odd}),
\tag{9}
$$



whenever the two displayed indices are nonnegative.  Here is the short
recurrence proof needed in this package.  The odd-modulus anti-period theorem
gives



$$
q_M\equiv q_{M+1}\equiv-1\pmod M.
$$



Running (1) backwards twice gives
$q_{M-1}\equiv q_{M-2}\equiv1\pmod M$.  If
$Y_j=q_{M-1-j}$, rearranging (1) at index $M-j$ gives



$$
Y_{j+1}\equiv(4j+2)Y_j+Y_{j-1}\pmod M.
$$



This is exactly the recurrence for $q_{j+1}$, and
$(Y_0,Y_1)\equiv(1,1)=(q_0,q_1)$.  Induction proves (9), in particular
for $M=p^2$.  A complete proof of the underlying odd-modulus period
theorem, together with the prime-square affine law, is in the frozen
dependency

    sources/bessel_denominator_all_lift_branching_wieferich_barrier.md

with SHA-256

    f02b4b936c2ca810299f037e158e7406214e89ef77e8ca98dcd67b2a9bd00911.

For clarity, the deductions from (7)--(9) needed here are reproved below;
in particular, no simple-root or Hensel assumption is made.

## 3. Affine lifting without simplicity

Suppose $p\mid q_r$ and define, for $t\geq0$,



$$
a_t=(-1)^tq_{r+tp}.
\tag{10}
$$



Equation (7) makes every $a_t$ divisible by $p$.  Apply (8) at
$n=r+tp$.  Its right-hand side is then divisible by $p^2$, while its
left-hand side, after multiplication by the unit $(-1)^t$, is



$$
a_{t+2}-2a_{t+1}+a_t.
$$



Therefore $(a_t)$ is affine modulo $p^2$.  Since



$$
a_1-a_0=-q_{r+p}-q_r=p\delta,
$$



we obtain, for every $t\geq0$,



$$
\boxed{(-1)^tq_{r+tp}\equiv q_r+tp\delta\pmod {p^2}.}
\tag{11}
$$



This proof remains valid when $\delta=0$; it does not divide by the slope
and does not assume that the root is simple.

## 4. Reflection couples the two slopes

Put $s=p-1-r$, and write $\delta_s$ for the slope defined as in (3)
with $s$ in place of $r$.  Apply (9) with $M=p^2$ and
$u=r+tp$, where $0\leq t<p$.  The reflected index is



$$
p^2-1-(r+tp)=s+(p-1-t)p.
\tag{12}
$$



Because $p-1$ is even, $t$ and $p-1-t$ have the same parity.  Using
(11) on both sides of (9) therefore gives



$$
q_r+tp\delta
 \equiv
 q_s+(p-1-t)p\delta_s
 \pmod {p^2}.
\tag{13}
$$



Comparing (13) at two consecutive values of $t$, and then at $t=0$,
yields



$$
\boxed{
 \delta_s\equiv-\delta\pmod p,
 \qquad
 q_s\equiv q_r-p\delta\pmod {p^2}.}
\tag{14}
$$



Again, this is a congruence calculation on possibly singular roots, not a
Hensel argument.

If $r=s$, the first congruence in (14) gives
$2\delta\equiv0\pmod p$.  Since $p$ is odd, $\delta=0$, proving the
central singularity asserted in Section 1.

## 5. Proof of the quotient table and exclusivity

All four values in (4) are divisible by $p$: this holds for $r,s$ by
(7), (9), and the hypothesis, and then for their translates by (7).
Dividing (14) by $p$ gives



$$
{q_s\over p}\equiv c-\delta\pmod p.
\tag{15}
$$



Putting $t=1$ in (11) gives



$$
{q_{r+p}\over p}\equiv-c-\delta\pmod p.
\tag{16}
$$



Apply the same formula at $s$, use $\delta_s=-\delta$, and substitute
(15):



$$
{q_{s+p}\over p}
 \equiv-{q_s\over p}-\delta_s
 \equiv-c+2\delta\pmod p.
\tag{17}
$$



Equations (15)--(17) prove (5).

When $\delta\ne0$, the vanishing of the four entries of (5) would require,
respectively,



$$
{c\over\delta}\equiv0,\quad1,\quad-1,\quad2\pmod p.
\tag{18}
$$



These four residues are distinct for $p\geq5$, so at most one condition
can hold.  When $\delta=0$, (5) becomes
$(c,c,-c,-c)$, which proves the all-or-none assertion.  The central
formula (6) is the same calculation after identifying the repeated indices.

Finally,



$$
(q_0,q_1,q_2,q_3)=(1,1,7,71)
$$



are all odd, and



$$
(q_0,\ldots,q_5)=(1,1,7,71,1001,18089)
$$



contain no multiple of $3$.  This disposes of $p=2,3$.

## 6. Why this is exactly the $p>n/2$ reduction

The strict inequality $p>n/2$ is equivalent to $0\leq n<2p$.  Reduce
such an $n$ modulo $p$, obtaining $a\in\{0,\ldots,p-1\}$.  By
(7), $p\mid q_n$ implies $p\mid q_a$.  Pair $a$ with
$p-1-a$ using (9), and let



$$
r=\min(a,p-1-a),\qquad s=p-1-r.
$$



The only nonnegative integers below $2p$ in those two residue classes are
exactly the four in (4), with the two central repetitions removed.  Thus
every large-prime divisor in the requested window is covered by one and only
one orbit of the theorem.

## 7. Sharp example and remaining obstruction

The square example



$$
q_8=312129649=13^2\cdot1846921
\tag{19}
$$



lies in the noncentral orbit $(r,s)=(4,8)$.  Here



$$
c={q_4\over13}\equiv12,
 \qquad \delta_{13}(4)\equiv12\pmod {13},
$$



so only the second entry $c-\delta$ in (5) vanishes.  This shows that
“valuation exactly one” cannot replace the theorem's “at most one
exception.”

The theorem materially localizes, but does not solve, the desired uniform
bound.  It leaves precisely two mechanisms:

* one exceptional integer in an ordinary four-point orbit, whose exponent
  is not bounded by (5); or
* a singular orbit with $c=0$, in which all four representatives already
  survive modulo $p^2$ (two representatives in the central case).

Ruling out long cancellation in those mechanisms requires information past
the first affine lift.  Neither the terminating factorial formula nor the
continuant coprimality of adjacent denominators supplies that information by
itself.

## 8. Replay

The companion script independently reconstructs the recurrence modulo prime
powers, verifies (7)--(9), (5), and the exclusivity dichotomy, and performs a
finite diagnostic scan over every prime $p<10000$ and every
$0\leq n<2p$.  That scan finds the sole valuation-two instance
$(p,n)=(13,8)$ and no valuation-three instance.  Those two scan statements
are finite evidence only; the theorem is the symbolic argument above.

Run

    python -m py_compile scripts/bessel_large_prime_four_point_exclusivity_certificate.py
    python scripts/bessel_large_prime_four_point_exclusivity_certificate.py

Peak storage is
$O(\max(B_{\rm scan},B_{\rm identity}^2))$ modular residues for the two
independently chosen replay bounds.  At the defaults this is only about
40,000 Python integers and remains far below the available 50 GiB RAM.
