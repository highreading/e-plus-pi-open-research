> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Exact common-zero reductions on the $n=5$ two-log edge

Checked: 2026-08-27 UTC

## Verdict

Every base-representative obstruction in the ideal



$$
\mathfrak J_d=(N_d,a_dT_d),\qquad
 N_d=P_d(\eta)P_d(\bar\eta),
$$



has an exact formulation in terms of a truncated exponential when the
residue characteristic $p$ satisfies $p>d$.  For an arbitrary degree
$n$, the previously proved block reduction replaces $n$ by its least
residue $d=n\bmod p$, so that $0\le d<p$, before the reductions in this
note are applied.  In particular, the simultaneous zero of the two
$P$-values is equivalent, away from $5d!$, to two consecutive zeros of
one scalar recurrence in the real quadratic field.  That recurrence also
splits into five first-order residue-class recurrences.

These reductions do **not** prove that $19$ is the only possible rational
content prime.  The remaining assertion is a uniform finite-characteristic
zero-avoidance problem; the finite scans in the companion certificate are
diagnostic only.

## 1. Notation

Put



$$
\zeta=\zeta _5,\quad x=\eta=(1+\zeta)^{-1},\quad
 y=\bar\eta=1-x=\zeta x,
$$



and



$$
u=x^{-1}=1+\zeta,\qquad
 v=y^{-1}=1+\zeta^{-1},\qquad
 A=u+v=uv=2+(\zeta+\zeta^{-1}).
$$



Thus $A^2-3A+1=0$.  Let



$$
E_d(Z)=\sum_{j=0}^d\frac{Z^j}{j!},\qquad
 P_d(X)=(-1)^d d!E_d(-X).
\tag{1}
$$



The exact recurrences used below are



$$
P_d(X)=X^d-dP_{d-1}(X),\qquad P_d'(X)=dP_{d-1}(X),
\tag{2}
$$



and hence



$$
P_d'(X)+P_d(X)=X^d.
\tag{3}
$$



To make the quantifiers explicit, let $p\ne5$ be an odd residue
characteristic.  If the original degree is $n=mp+d$, $0\le d<p$, the
exact block congruences



$$
\begin{aligned}
 P_n(X)&\equiv X^{mp}P_d(X),& a_n&\equiv a_d,\\
 C_n(X)&\equiv X^{mp}\{C_d(X)+mL_pP_d(X)\}
 \end{aligned}
\tag{3a}
$$



hold modulo $p$, where $L_p$ is independent of $d$.  Hence, for



$$
D_n=P_n(x)C_n(y)-P_n(y)C_n(x),
$$



one has



$$
P_n(x)P_n(y)\equiv(xy)^{mp}P_d(x)P_d(y),\qquad
 D_n\equiv(xy)^{mp}D_d.
\tag{3b}
$$



Because $x,y$ are units, every common-zero alternative at degree $n$
is therefore exactly the corresponding alternative at its base
representative $d<p$.  Sections 2--5 always concern that representative.

## 2. Simultaneous $P$-zeros

Define



$$
K_d(X)=P_d(\zeta X)-\zeta^{d+1}P_d(X).
\tag{4}
$$



Equation (3) gives the polynomial identity



$$
K_d'(X)+\zeta K_d(X)=\zeta^{d+1}(1-\zeta)P_d(X),
\tag{5}
$$



while (2), evaluated at $x$, gives



$$
K_d'(x)=d\zeta K_{d-1}(x).
\tag{6}
$$



Consequently, at a prime whose residue characteristic $p$ satisfies
$p>d$ and $p\ne5$,



$$
P_d(x)=P_d(y)=0
 \quad\Longleftrightarrow\quad
 K_d(x)=K_{d-1}(x)=0.
\tag{7}
$$



Indeed, the forward implication follows from (4) and then (5).  Conversely,
(6) turns the right side into $K_d(x)=K_d'(x)=0$; (5) gives
$P_d(x)=0$, and (4) then gives $P_d(y)=0$.  Every factor divided out in
this argument is a unit under the stated hypotheses.

Normalize



$$
h_d=\frac{K_d(x)}{(1-\zeta)y^d}.
\tag{8}
$$



Since



$$
\sum_{d\ge0}P_d(X)\frac{z^d}{d!}=\frac{e^{Xz}}{1+z},
$$



substitution in (4), followed by replacing $z$ with $z/y$, proves



$$
\boxed{\displaystyle
 \sum_{d\ge0}h_d\frac{z^d}{d!}
       =\frac{e^z}{1+Az+Az^2}.}
\tag{9}
$$



In particular, $h_d\in\mathcal O_F=\mathbb Z[A]$, and



$$
\begin{aligned}
 h_0&=1,\qquad h_1=1-A,\\
 h_d+Adh_{d-1}+Ad(d-1)h_{d-2}&=1\qquad(d\ge2).
 \end{aligned}
\tag{10}
$$



Let



$$
Q(z)=1+Az+Az^2=(1+uz)(1+vz).
\tag{11}
$$



When $d!$ is invertible, multiplication of the truncated series in (9)
by $Q$ shows



$$
h_d=h_{d-1}=0
 \quad\Longleftrightarrow\quad
                         Q(z)\mid E_d(z).
\tag{12}
$$



For example, if the two last coefficients on the left vanish, the degree
$d-2$ truncation of the series in (9) is an exact quotient of $E_d$ by
$Q$.  The converse follows by uniqueness of formal power-series division.
The roots of $Q$ are $-x$ and $-y$, so (12) also follows immediately
from (1).

There is an exact five-step refinement.  Put



$$
\kappa=5A-2,
 \quad
 R(z)=1-Az+(2A-1)z^2+(1-2A)z^3.
\tag{13}
$$



Using $A^2=3A-1$, direct multiplication gives



$$
Q(z)R(z)=1-\kappa z^5,
             \qquad N_{F/\mathbb Q}(\kappa)=-1.
\tag{14}
$$



Equivalently, $u^5=v^5=2-5A=-\kappa$.  Equations (9) and (14) give,
for every $d\ge5$,



$$
\boxed{\begin{aligned}
 h_d-\kappa(d)_5h_{d-5}
  ={}&1-Ad+(2A-1)d(d-1)\\
    &+(1-2A)d(d-1)(d-2),
\end{aligned}}
\tag{15}
$$



where $(d)_5=d(d-1)\cdots(d-4)$.  Thus each residue class modulo five
obeys a first-order inhomogeneous recurrence.  Merely propagating (15) from
a consecutive zero pair does not close the argument: the two adjacent
residue classes retain independent endpoint data.

## 3. The $a_d$-and-$P_d(x)$ alternative

The same construction works without a fifth root of unity.  Define



$$
L_d(X)=P_d(uX)-u^{d+1}P_d(X),\qquad
 g_d=\frac{L_d(x)}{1-u}.
\tag{16}
$$



Since $ux=1$, exactly the same differentiation proves, at a residue
characteristic greater than $d$,



$$
a_d=P_d(1)=P_d(x)=0
 \quad\Longleftrightarrow\quad
                         g_d=g_{d-1}=0.
\tag{17}
$$



The generating function is



$$
\sum_{d\ge0}g_d\frac{z^d}{d!}
       =\frac{e^z}{(1+z)(1+uz)}.
\tag{18}
$$



Therefore (17) is also equivalent to



$$
(1+z)(1+uz)\mid E_d(z)
\tag{19}
$$



in the relevant residue field.  Unlike (11), the two reciprocal poles in
(18) do not have root-of-unity ratio.

## 4. The $P_d(x)$-and-$C_d(x)$ alternative

Let $C_d=d!B_d$, so that



$$
\sum_{d\ge0}C_d(X)\frac{z^d}{d!}
       =\frac{e^{Xz}\log(1+Xz)}{1+z}.
\tag{20}
$$



For an indeterminate $\lambda$, define



$$
\mathcal F_d(\lambda,u)
   =d![z^d]\frac{e^z(1+z)^\lambda}{1+uz}.
\tag{21}
$$



This is a monic degree-$d$ polynomial in $\lambda$ over
$\mathcal O_E$.  Substituting $z\mapsto uz$ in the generating
functions for $P_d(x)$ and $C_d(x)$ gives the exact identities



$$
\mathcal F_d(0,u)=u^dP_d(x),\qquad
 \frac{\partial\mathcal F_d}{\partial\lambda}(0,u)=u^dC_d(x).
\tag{22}
$$



Thus



$$
P_d(x)=C_d(x)=0
 \quad\Longleftrightarrow\quad
 \lambda=0\text{ is a multiple root of }
                 \mathcal F_d(\lambda,u)
\tag{23}
$$



after reduction.  A generic discriminant estimate is too coarse here:
full discriminants of $\mathcal F_d$ already acquire large varying prime
factors in small degrees, even though the special constant-and-linear
coefficient ideal has no factor in the certified finite range.

## 5. Exhaustion of the common-zero alternatives

Let



$$
N_d=P_d(x)P_d(y),\qquad
 T_d=\frac{D_d}{\zeta-\zeta^{-1}}\in\mathcal O_F,
 \qquad \mathfrak J_d=(N_d,a_dT_d).
\tag{24}
$$



Suppose a prime of $F$, of odd residue characteristic $p\ne5$ with
$p>d$, divides $\mathfrak J_d$, and extend it to a prime of $E$.
Since



$$
D_d=P_d(x)C_d(y)-P_d(y)C_d(x),
$$



one may interchange $x,y$ and assume $P_d(x)=0$.  Then either



$$
\begin{array}{ll}
 P_d(y)=0, &\text{the case in Section 2},\\
 a_d=0, &\text{the case in Section 3},\\
 C_d(x)=0, &\text{the case in Section 4}.
 \end{array}
\tag{25}
$$



This is exactly the base-representative common-zero trichotomy, now
expressed as two fixed-divisor problems for $E_d$ and one
prescribed-multiple-root problem for $\mathcal F_d$.  For an arbitrary
original degree $n$, equations (3a)--(3b) first reduce it to
$d=n\bmod p<p$; no claim in Sections 2--4 is being made with a
noninvertible $d!$.

The companion script checks all algebraic identities above in exact
arithmetic and records finite diagnostics.  Those scans do not establish
an all-degree Bezout identity such as $361\in\mathfrak J_d$, and nothing
in this note proves algebraicity or transcendence of $e+\pi$.
