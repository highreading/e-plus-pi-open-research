> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A residue-degree criterion for every possible content prime

Checked: 2026-08-27 UTC

## Verdict

There is an exact necessary criterion for an arbitrary rational prime to
divide the primitive content on the $n=5,c=f=0$ edge.  It reduces every
degree $d$ to the single residue $r=d\bmod p$, with $0\leq r<p$.
It does not, however, force $p$ to belong to a fixed finite set and does
not give a subexponential bound for the product of the varying primes.

Put



$$
E=\mathbb Q(\zeta _5),\qquad
 F=\mathbb Q(\zeta _5+\zeta _5^{-1}),\qquad
 \eta=(1+\zeta _5)^{-1},\quad\bar\eta=1-\eta.
$$



For the integral polynomials $P_r=r!A_r$ and $C_r=r!B_r$, define



$$
\begin{aligned}
 a_r&=P_r(1),\\
 N_r&=P_r(\eta)P_r(\bar\eta)\in\mathcal O_F,\\
 D_r&=P_r(\eta)C_r(\bar\eta)
       -P_r(\bar\eta)C_r(\eta),\\
 T_r&=\frac{D_r}{\zeta _5-\zeta _5^{-1}}\in\mathcal O_F,\\
 \mathfrak J_r&=(N_r,a_rT_r)\subseteq\mathcal O_F.
\end{aligned}\tag{1}
$$



The quotient defining $T_r$ is integral: the anti-invariant lattice in
$\mathbb Z[\zeta _5]$ is exactly



$$
(\zeta _5-\zeta _5^{-1})
 \mathbb Z[\zeta _5+\zeta _5^{-1}].\tag{2}
$$



**General-prime criterion.**  Let $p$ be an odd rational prime other
than $5$, let $d\geq1$, and let $r$ be the least nonnegative residue
of $d$ modulo $p$.  If a prime ideal above $p$ divides the primitive
content $\mathfrak c_d$, then



$$
p\mid N_{F/\mathbb Q}(\mathfrak J_r).\tag{3}
$$



Conversely, because $r<p$, condition (3) is equivalent to the occurrence
of a prime above $p$ in the degree-$r$ content $\mathfrak c_r$.
Thus every rational prime which can occur at any later degree is already
visible at its first residue degree below $p$.  Higher degrees can change
the exponent, as $p=19,d=205$ demonstrates, but cannot introduce a new
rational prime without (3).

## 1. Block congruences

The exact recurrences are



$$
\begin{aligned}
 P_0(X)&=1,& P_d(X)&=X^d-dP_{d-1}(X),\\
 a_0&=1,&a_d&=1-da_{d-1},\\
 c_0&=0,&c_d&=c_{d-1}+a_{d-1},\\
 C_0(X)&=0,&C_d(X)&=-dC_{d-1}(X)+c_dX^d,
\end{aligned}\tag{4}
$$



where $c_d=[X^d]C_d$.  In characteristic $p$, put



$$
L_p=\sum_{j=0}^{p-1}a_j\pmod p.
$$



Induction over one block gives, for $d=mp+r$,



$$
\boxed{\begin{aligned}
 P_d(X)&=X^{mp}P_r(X),\\
 a_d&=a_r,\\
 c_d&=c_r+mL_p,\\
 C_d(X)&=X^{mp}\{C_r(X)+mL_pP_r(X)\}
\end{aligned}}\qquad(\bmod p).\tag{5}

The extra multiple of \(P_r\) cancels from the alternating determinant.
Since \(s=\eta\bar\eta\) is a unit, (5) yields

\[
             N_d=s^{mp}N_r,\qquad D_d=s^{mp}D_r
             \pmod p.\tag{6}

This is the exact reason the prime test depends only on \(r\), rather than
an extrapolation from a numerical period.

## 2. Proof of the criterion

After the automatic common \(\ell_d\) is removed from the safe clearing,
the coefficient blocks are, up to signs and units,

\[
 2a_dN_d,\qquad 2d!N_d,\qquad 5a_dD_d.\tag{7}

Multiplication by \(-i\) puts them in
\(K=\mathbb Q(\zeta _5,i)^+\).  If

\[
 z=i(\zeta _5-\zeta _5^{-1}),
$$



then the last block is the $z\mathcal O_F$-coordinate
$5a_dT_d$.  Both $z$ and $5$ are local units at every prime in the
statement.

First take the base degree $d=r<p$.  Here $r!$ is a $p$-adic unit.
If $a_r\not\equiv0\pmod p$, a prime over $p$ divides both coordinates
in (7) exactly when it divides both $N_r$ and $T_r$.  If
$a_r\equiv0\pmod p$, the first and third blocks vanish and the second
shows that divisibility is exactly the condition that it divide $N_r$.
These two cases are combined by



$$
\mathfrak J_r=(N_r,a_rT_r).\tag{8}
$$



This proves the converse assertion at the base degree.

For a general $d=mp+r$, equations (5)--(6) show that the algebraic-unit
parts of the same blocks reduce to those at $r$.  If $a_r$ is a unit
modulo $p$, failure of (8) leaves either the first or third block a local
unit, so no rational clearing can create a common prime factor.  If
$a_r\equiv0$, but $N_r$ is a local unit, the only common factors in
the first two blocks are rational powers of $p$ coming from $a_d$ and
$d!$.  The least rational clearing removes their minimum; whichever
minimum is attained leaves a local-unit multiple of $N_d$.  Again no
prime above $p$ remains.  Therefore occurrence at $d$ implies (8),
and taking ideal norms proves (3).

There is an equivalent common-zero description.  Let $\mathfrak P$ be
a prime of $E$ over the relevant prime of $F$.  Away from $5$, (8)
can hold only through one of



$$
\begin{array}{ll}
 P_r(\eta)=P_r(\bar\eta)=0, &\text{or}\\
 P_r(\eta)=C_r(\eta)=0, &\text{or the conjugate pair,}\\
 a_r=0\ \text{and}\ P_r(\eta)P_r(\bar\eta)=0,
\end{array}\qquad(\bmod\mathfrak P).\tag{9}

Indeed, if exactly one of the two \(P\)-values vanishes, the determinant
\(D_r\) vanishes precisely when the corresponding \(C\)-value does.

## 3. Why this does not yet give a global norm bound

For each fixed \(r\), (3) is finite and effective: every candidate prime
divides the explicit positive integer
\(N_{F/\mathbb Q}(\mathfrak J_r)\).  But the residue \(r=d\bmod p\)
changes with \(p\).  Consequently there is no single fixed resultant or
integer whose prime divisors contain all possibilities.

The elementary height estimate for (1) is only

\[
 \log N_{F/\mathbb Q}(\mathfrak J_r)=O(r\log r),\tag{10}
$$



because the coefficients of $P_r,C_r$ have factorial size.  Even the
product of possible primes $p\leq d$ is bounded naively by a quantity of
exponential size, while primes $p>d$ are controlled only by the
degree-$d$ integer in (10).  These estimates do not prove



$$
\limsup_{d\to\infty}\frac1d\log N(\mathfrak c_d)<\log\varphi,
$$



let alone a zero limsup.  A subexponential theorem would require new
information on the varying ideal sequence $\mathfrak J_r$, such as a
uniform fixed-divisor theorem or a sufficiently sparse large-prime
theorem.  Neither follows from (5) or from a finite scan.

The companion exact diagnostic script checks (8) for every odd prime
$p\leq1000$, $p\ne5$, and every $0\leq r<p$; the only hit is
$(p,r)=(19,15)$.  This is evidence for the criterion's usefulness, not
an all-prime theorem.

Nothing here proves either algebraicity or transcendence of $e+\pi$.
