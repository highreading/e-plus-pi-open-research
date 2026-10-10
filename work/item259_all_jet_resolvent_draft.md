> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 259 draft — exact resolvent involution and the full reciprocal-jet no-go

Drafted: 2026-08-31 (Beijing time)

Status: INDEPENDENT AUDIT PASS WITH RING/SCOPE CLARIFICATIONS; not yet integrated.

## 1. Scope

Keep the actual ordinary-$j=2$ phase



$$
p=6m+2d+1,\qquad L=m+1,\qquad
 a=2m+d,\qquad b=3m+d+1=a+L .
$$



For a $p$-unit $c$, introduce the exact resolvent



$$
\mathscr M_q(c;z)
 =\sum_{k=0}^m\binom mk\frac{c^k}{a+q+k-z}.
 \tag{1.1}
$$



Its coefficient of $z^j$ at $z=0$ is the $j$-th denominator jet



$$
J_{q,j}(c)=
 \sum_{k=0}^m\binom mk\frac{c^k}{(a+q+k)^{j+1}}.
 \tag{1.2}
$$



Thus $J_{q,0}=M_q$, $J_{q,1}=N_q$, and $J_{q,2}$ is the second
jet considered at the mod-$p^3$ level.

## 2. Exact functional identities

Termwise partial fractions give the endpoint-retaining resolvent
recurrence



$$
(a+q-z)\mathscr M_q(c;z)
 +c(b+q-z)\mathscr M_{q+1}(c;z)
 =(1+c)^L.
 \tag{2.1}
$$



Iterating it for $0\le q<L$ gives



$$
\mathscr M_L(c;z)
 =A_c(z)\mathscr M_0(c;z)+E_c(z),
 \tag{2.2}
$$



where



$$
A_c(z)=
 \left(-\frac1c\right)^L\frac{(a-z)_L}{(b-z)_L}.
 \tag{2.3}
$$



Reversing $k=m-j$ in (1.1) and using
$b+m-j=p-(a+j)$ gives the exact, untruncated reflection



$$
\boxed{\mathscr M_L(c;z)
 =-c^m\mathscr M_0(c^{-1};p-z).}
 \tag{2.4}
$$



The phase complement also gives



$$
(a-p+z)_L=(-1)^L(b-z)_L,\qquad
 (b-p+z)_L=(-1)^L(a-z)_L,
$$



and hence



$$
\boxed{A_c(z)A_{c^{-1}}(p-z)=1.}
 \tag{2.5}
$$



Put



$$
X(z)=\mathscr M_0(c;z),\qquad
 Y(z)=\mathscr M_0(c^{-1};p-z).
$$



Combining (2.2) and (2.4) for $c$, and then for $c^{-1}$ at
$p-z$, gives



$$
\begin{pmatrix}
 A_c(z)&c^m\\
 c^{-m}&A_{c^{-1}}(p-z)
 \end{pmatrix}
 \binom{X(z)}{Y(z)}
 +
 \binom{E_c(z)}{E_{c^{-1}}(p-z)}
 =0.
 \tag{2.6}
$$



By (2.5), the second row is the first row multiplied by the unit
$c^{-m}A_c(z)^{-1}$.  Since the actual moments satisfy both rows,
the affine terms obey the exact identity



$$
\boxed{
 E_{c^{-1}}(p-z)
 =c^{-m}A_c(z)^{-1}E_c(z).}
 \tag{2.7}
$$



Consequently (2.6) has exact rank one over the rational-function field,
not merely after reduction modulo $p$.

## 3. All finite Hasse levels

To make the topology and the coefficient involution precise, first let
$C$ be an indeterminate.  Let $S\subset\mathbf Z_{(p)}[z]$ be the
multiplicative set of polynomials whose value at $z=0$ is a $p$-unit,
and put



$$
\mathcal R=\mathbf Z_{(p)}[C,C^{-1},z,S^{-1}],
 \qquad \mathfrak m=(p,z).
 \tag{3.0}
$$



Every displayed resolvent denominator and every factor of $A_C(z)$ is
a unit in this ring, by the phase range audit below.  The substitution



$$
\iota(C,z)=(C^{-1},p-z)
$$



preserves $S$, is an automorphism of $\mathcal R$, and preserves every
$\mathfrak m^N$.  After proving the universal identities one may
specialize $C$ to any $p$-unit $c$; equivalently, $\iota$ then
identifies the paired $c$- and $c^{-1}$-systems.  Therefore
(2.4)--(2.7) descend to every filtered quotient
$\mathcal R_N=\mathcal R/\mathfrak m^N$.

Concretely, if $F(z)=\sum_{j<N}f_jz^j$, then $F=0$ in
$\mathcal R_N$ exactly when $f_j=0\pmod {p^{N-j}}$ for every
$0\leq j<N$.  This total-degree rule is the source of the tiered
precision in (3.1); it is not a coefficientwise mod-$p^N$ truncation.

In ordinary denominator jets, (2.4) reads, for $0\le j<N$,



$$
\boxed{
 J_{L,j}(c)\equiv
 (-1)^{j+1}c^m
 \sum_{h=0}^{N-j-1}
 \binom{j+h}{h}p^hJ_{0,j+h}(c^{-1})
 \pmod {p^{\,N-j}}.}
 \tag{3.1}
$$



The coefficient of $z^j$ in (2.1) gives the complete triangular
contiguous tower:



$$
\begin{aligned}
 &(a+q)J_{q,0}+c(b+q)J_{q+1,0}=(1+c)^L,\\
 &(a+q)J_{q,j}+c(b+q)J_{q+1,j}
   =J_{q,j-1}+cJ_{q+1,j-1}\qquad(j\ge1).
 \end{aligned}
 \tag{3.2}
$$



Equations (2.5)--(2.7) show that, after adjoining all jets required at
precision $N$, the two reciprocal functional rows still generate the
same rank-one submodule.  Equivalently, one may choose the entire
$X$-jet freely and solve uniquely for the $Y$-jet because $c^m$
is a unit.  The coordinate change $F(z)\mapsto F(p-z)$ on truncated
ordinary jets is triangular with diagonal entries $(-1)^j$, hence is
invertible in every $\mathcal R_N$.  It converts $Y(z)$ back to the
ordinary reciprocal jets without losing a digit.  The second reciprocal
row supplies no compatibility condition.

Here “choose freely” is a statement about the solution module of the
recurrence/reflection relations.  It does not claim that the explicitly
defined binomial resolvent assumes arbitrary arithmetic values as the
parameters vary.

## 4. Draft verdict and strict scope

The independent audit proves the following sharply scoped no-go:

> The endpoint-retaining contiguous recurrence, denominator-complement
> reflection, and every finite tower of denominator jets obtained from
> them cannot by themselves impose a polynomial or linear compatibility
> condition on $M_0(-2)$, on $H_m$, or on the affine Item-251 target.

This closes the reciprocal-jet strategy at all finite Hasse levels.  It
does **not** prove that $H_m$ can vanish on infinitely many actual rows,
does not control the punctured finite-field period arithmetically, and
does not rule out an independent period, a nonlinear relation, or another
Route-1 mechanism.  It therefore books



$$
\text{new unconditional linear-log rate}=0,\qquad
 \text{capacity reduction}=0.
$$



## 5. Unit and boundary audit

For $0\leq q,k\leq m$,



$$
0<a+q+k\leq4m+d<p,\qquad
 0<b+q\leq4m+d+1<p.
$$



At $q=L$, $0<a+L+k\leq4m+d+1<p$, and the reflected constants
$p-(a+k)$ also lie strictly between $0$ and $p$.  Hence every
denominator used in the resolvent, multiplier, recurrence, reflection,
and all of their $z$-expansions is a $p$-unit.  Also $c$ and
$c^m$ are units.  The endpoint $(1+c)^L$ in (2.1) is retained
exactly.
