> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Rational first-integral exclusion for one Bessel recurrence state

Checked: 2026-08-27 UTC.

## 1. Theorem

Let



$$
\sigma(x)=x+1,\qquad
 \sigma(y)=-(4x+2)y+z,\qquad
 \sigma(z)=y
\tag{1}
$$



act on $\mathbb Q[x,y,z]$.  This is the one-step substitution for the
two-dimensional Bessel interpolation state.

The constant-multiplier theorem in
`sources/bessel_all_degree_polynomial_recurrence_invariant_exclusion.md`
extends to every polynomial Darboux multiplier.

> **Theorem 1.**  Suppose
> $P\in\mathbb Q[x,y,z]\setminus\{0\}$ and
> $\mu\in\mathbb Q[x]\setminus\{0\}$ satisfy
> 

$$
>                         \sigma(P)=\mu P.          \tag{2}
>
$$


> Then $\mu=1$ and $P\in\mathbb Q^\times$.

Consequently the rational fixed field is trivial:



$$
\boxed{\mathbb Q(x,y,z)^\sigma=\mathbb Q.}         \tag{3}
$$



More generally, if $R\in\mathbb Q(x,y,z)$ and
$\sigma(R)=\lambda R$ for a constant
$\lambda\in\mathbb Q^\times$, then either $R=0$, or
$\lambda=1$ and $R\in\mathbb Q^\times$.

Thus no rational expression in the index and one recurrence state can be a
nonconstant first integral or constant-multiplier semi-invariant.  The result
does not exclude constructions involving two independently transported
states, nonlocal sums/products, or rational Darboux factors with genuinely
rational nonpolynomial multipliers when they are not assembled into a first
integral.

No Bessel digit-depth estimate and no conclusion about $e+\pi$ is proved.

## 2. The substitution is a polynomial automorphism

Put $(X,Y,Z)=\bigl(\sigma(x),\sigma(y),\sigma(z)\bigr)$.  Then



$$
x=X-1,\qquad y=Z,\qquad z=Y+(4X-2)Z.              \tag{4}
$$



Hence $\sigma$ is an automorphism of the unique-factorization domain
$\mathbb Q[x,y,z]$.  It preserves total degree in the two state variables
$y,z$, although it can increase degree in $x$.

## 3. Polynomial Darboux factors

Decompose $P$ into components homogeneous in $(y,z)$.  Because both
$\sigma$ and multiplication by $\mu(x)$ preserve this grading, every
component separately satisfies (2).  Suppose that a nonzero component has
positive state degree $m$, and denote it again by $P$.

Use the primitive real Bessel solutions



$$
\begin{aligned}
 q_0=q_1&=1,&q_n&=(4n-2)q_{n-1}+q_{n-2},\\
 p_0&=1,&p_1&=3,&p_n&=(4n-2)p_{n-1}+p_{n-2},\\
 s_n&=(p_n-q_n)/2.
 \end{aligned}                                      \tag{5}
$$



For the unimodular transfer matrix $M_n$ from index $1$ to index $n$,
the previously proved exact identity is



$$
M_n^{-1}\binom01=\binom{q_n-s_n}{s_n},
 \qquad \frac{s_n}{q_n}\longrightarrow
 c:=\frac{e-1}{2}.                                  \tag{6}
$$



The number $c$ is transcendental, and $q_n\ge n^n$ on the even
positive integers.

First observe that $\mu(k)\ne0$ for every positive integer $k$.  If
$\mu(k)=0$, specializing (2) at $x=k$ and using invertibility of the
state substitution gives $P(k+1;y,z)=0$.  Equation (2) then propagates
this identity to every subsequent integer.  Each coefficient of $P$, as
a polynomial in $x$, would have infinitely many zeros, forcing $P=0$.

Iteration of (2) from $1$ to $n$, followed by (6), gives



$$
\begin{aligned}
 P(n;0,1)
 &=\left(\prod_{k=1}^{n-1}\mu(k)\right)
   P\bigl(1;q_n-s_n,s_n\bigr)\\
 &=\left(\prod_{k=1}^{n-1}\mu(k)\right)
   q_n^mR(s_n/q_n),                                  \tag{7}
 \end{aligned}
$$



where



$$
R(t)=P(1;1-t,t).            \tag{8}
$$



The polynomial $R$ is nonzero: a nonzero homogeneous polynomial cannot
vanish on the whole affine line $y+z=1$.  Since $R$ has rational
coefficients and $c$ is transcendental,



$$
R(c)\ne0.               \tag{9}
$$



Let $d=\deg\mu$.  If $d=0$, the product in (7) is a fixed nonzero
constant to the power $n-1$.  If $d>0$, then for some constants
$C_0,C_1>0$ and all sufficiently large $n$,



$$
\left|\prod_{k=1}^{n-1}\mu(k)\right|
       \ge C_0 C_1^n(n!)^d.                          \tag{10}
$$



Equations (6)--(10), restricted to even $n$, make the absolute value of
the right side of (7) grow faster than every polynomial in $n$.  The left
side is the coefficient of $z^m$ in $P$, evaluated at $x=n$, and has
only polynomial growth.  This contradiction removes every positive
state-degree component.

It remains that $P=A(x)$.  Equation (2) becomes



$$
A(x+1)=\mu(x)A(x).        \tag{11}
$$



Degree comparison forces $\deg\mu=0$; leading coefficients then force
$\mu=1$.  A polynomial of period one is constant.  This proves Theorem 1.

## 4. Passage from polynomial factors to rational invariants

Let $R=P/Q$ be in lowest terms, with nonzero coprime
$P,Q\in\mathbb Q[x,y,z]$, and suppose first that $\sigma(R)=R$.  Then



$$
\sigma(P)Q=P\sigma(Q).   \tag{12}
$$



The UFD property and $(P,Q)=1$ imply $P\mid\sigma(P)$, so



$$
\sigma(P)=AP            \tag{13}
$$



for some polynomial $A$.  Comparing total state degrees in (13) shows
that $A\in\mathbb Q[x]$.  Substitution in (12) then gives
$\sigma(Q)=AQ$.  Theorem 1 forces $A=1$ and both $P,Q$ to be
constant, proving (3).

If $\sigma(R)=\lambda R$, the same coprime-factor argument gives



$$
\sigma(P)=AP,\qquad
                   \sigma(Q)=\frac A\lambda Q,      \tag{14}
$$



where both displayed multipliers are polynomials in $x$.  Theorem 1
forces both to equal one.  Hence $\lambda=1$ and $R$ is constant.

## 5. Exact certificate and scope

The companion script

    scripts/bessel_rational_first_integral_darboux_certificate.py

checks the polynomial automorphism and its inverse, the primitive transfer
identities, the growth inputs, representative polynomial-multiplier
Darboux systems over exact finite degree boxes, and sample coprime rational
factor identities.  The all-degree result is the symbolic UFD and growth
proof above; finite ranks are not used as a substitute.

Run

    python -m py_compile scripts/bessel_rational_first_integral_darboux_certificate.py
    python scripts/bessel_rational_first_integral_darboux_certificate.py

For byte-identical replay, use the script's `--output` option and compare it
with

    results/bessel_rational_first_integral_darboux_certificate.json
