> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact all-degree local content at $5$ and $19$

Checked: 2026-08-26 UTC

## Statement

Retain the notation of the $n=5,c=f=0$ two-log edge and put



$$
t=\zeta _5+\zeta _5^{-1},\qquad
 \delta _5=2-t,\qquad \delta _{19}=4-t.
$$



The following is an all-degree theorem about two specified local parts of
the primitive content ideal $\mathfrak c_d$:



$$
\boxed{
 v_{\delta _5\mathcal O_K}(\mathfrak c_d)
   =[d\equiv2\pmod5],
}\tag{1}
$$



and



$$
\boxed{
 v_{\delta _{19}\mathcal O_K}(\mathfrak c_d)
   =[d\equiv15\pmod {19}]+[d\equiv205\pmod {361}].
}\tag{2}
$$



Here the notation means the exponent of the displayed principal
$\mathcal O_K$-ideal.  In particular, (2) explains the first lift
$\mathfrak c_{205}=\delta_{19}^2\mathcal O_K$ proved in the separate
countercertificate.  Equations (1)--(2) do **not** assert that these are the
only prime-ideal factors of $\mathfrak c_d$.

## 1. Two elementary recurrences

Let



$$
P_d(X)=d!A_d(X),\qquad C_d(X)=d!B_d(X),\qquad
 a_d=P_d(1),qquad c_d=[X^d]C_d(X).
$$



The coefficient formula gives



$$
P_0=1,\qquad P_d(X)=X^d-dP_{d-1}(X),\qquad
 a_d=1-da_{d-1}.\tag{3}
$$



Also



$$
c_d=\sum_{j=1}^d(-1)^{j+1}\frac{d!}{j(d-j)!}.
$$



Its exponential generating function is



$$
\sum_{d\geq0}c_d\frac{z^d}{d!}=e^z\log(1+z).
$$



Differentiation, or direct coefficient comparison, therefore gives



$$
c_0=0,\qquad c_d=c_{d-1}+a_{d-1},\qquad
 C_d(X)=-dC_{d-1}(X)+c_dX^d.\tag{4}
$$



Thus $P_d(\eta),P_d(\bar\eta),C_d(\eta),C_d(\bar\eta)$
can be advanced with a fixed finite state in every finite quotient.  Put



$$
D_d=P_d(\eta)C_d(\bar\eta)-P_d(\bar\eta)C_d(\eta).\tag{5}
$$



After removing the common $\ell_d$ from the safe blocks (53), the three
relevant blocks are



$$
2a_dP_d(\eta)P_d(\bar\eta),\quad
 -2(-1)^d d!P_d(\eta)P_d(\bar\eta),\quad
 5a_dD_d.\tag{6}
$$



## 2. The prime $19$

The root $t=4\pmod {19}$ of $t^2+t-1$ lifts to
$t=42\pmod {19^2}$.  Hence



$$
s=\eta\bar\eta=(t+2)^{-1}=320\pmod {361}.
$$



Work in the exact finite ring



$$
R_{19}=(\mathbb Z/361\mathbb Z)[X]/(X^2-X+s),\qquad
 \eta=X,\quad\bar\eta=1-X.\tag{7}
$$



Both $X$ and $1-X$ have order $1710$ in this ring.  The coefficient
$d$ in (3)--(4) has period $361$, so a common state period is



$$
T=\operatorname {lcm}(361,1710)=32490.\tag{8}
$$



An exhaustive exact advance of (3)--(5) for one period proves:

* $P_d(\eta)$ and $P_d(\bar\eta)$ are divisible by $19$ exactly
  when $d\equiv15\pmod {19}$, and neither is then zero modulo $361$;
* in that residue class, $D_d\equiv0\pmod {361}$ exactly when
  $d\equiv205\pmod {361}$;
* $a_d\equiv4\pmod {19}$ throughout the exceptional class;
* at the conjugate prime $t=14\pmod {19}$, no $P_d(\eta)$ vanishes
  in its complete period.

This finite check really is all-degree.  At the end of (8), the powers,
the two $P$-values, and $a_d$ return to their initial states.  The two
$C$-values and $c_d$ return shifted by $95P$ and $95$, respectively.
The recurrences (3)--(4) preserve a shift $C\mapsto C+\lambda P$, while
the determinant (5) is invariant under it.  The next period is therefore
identical for every quantity used above.

At this prime $\eta-\bar\eta$ and
$z=i(\zeta _5-\zeta _5^{-1})$ are units.  The first block in (6) has
exact $\delta_{19}$-valuation two in the exceptional mod-19 class, and
the third has valuation one or at least two according to the mod-361
subclass.  This proves (2).  Outside that class the first block is a local
unit unless a rational scalar is common to all blocks; the least rational
clearing removes the latter.  The conjugate-prime computation rules out a
hidden rational $19$-factor in the exceptional class.

## 3. The prime $5$

Put $\varpi=\zeta _5-1$.  It is enough to work in



$$
R_5=\mathbb F_5[\varpi]/(\varpi^4),\qquad
 \eta=(2+\varpi)^{-1},\quad\bar\eta=1-\eta.\tag{9}
$$



Both local units in (9) have order $20$.  Advancing (3)--(5) through
that complete period proves



$$
v_\varpi(P_d(\eta))=v_\varpi(P_d(\bar\eta))=1
 \quad\Longleftrightarrow\quad d\equiv2\pmod5,\tag{10}
$$



and in this class $v_\varpi(D_d)=1$ and $a_d\equiv1\pmod5$.
At the period endpoint the $P$-state returns and the $C$-state is
shifted by $P$, so the same shift-invariance argument makes (10)
all-degree.

Now $v_\varpi(\delta_5)=2$,
$v_\varpi(z)=1$, and $v_\varpi(5)=4$.  The first block of (6) has
valuation two in (10), whereas conversion of the last block to its
$z\mathbb Z[t]$-coordinate gives valuation



$$
v_\varpi(5D_d/z)=4+1-1=4.
$$



Thus precisely one factor $\delta_5$ is common, proving (1).  In the
other residue classes a unit block remains after any common rational
power of $5$ is removed.

## 4. Scope and consequence

The exact implementation is
`scripts/algebraic_unit_two_log_n5_local_5_19_theorem.py`, with result
`results/algebraic_unit_two_log_n5_local_5_19_theorem.json`.

The theorem shows that the discovered $19$-adic lift is capped at
exponent two and that the $5$-part is capped at exponent one.  Therefore
these two primes alone contribute only a bounded amount to
$N(\mathfrak c_d)$, and cannot satisfy the exponential-growth condition
needed to cancel the relative norm.

It does not follow that the full content is bounded or subexponential.
Prime divisors of the recurrence values in (3)--(5) may vary with $d$.
An exact scan through $d=500$ finds no additional prime.  A separate
finite-field diagnostic of the simultaneous-$P$-zero mechanism through
rational primes $3000$ likewise finds no additional candidate; neither
finite computation excludes a later prime or another common-zero
mechanism.  A global theorem must control all such primes simultaneously.

Nothing here proves either algebraicity or transcendence of $e+\pi$.
