> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# All-degree polynomial invariant exclusion for the Bessel recurrence

Checked: 2026-08-27 UTC.

## 1. Theorem and scope

Put



$$
T(x)=
 \begin{pmatrix}
 -(4x+2)&1\\
 1&0
 \end{pmatrix}.
\tag{1}
$$



The Bessel interpolation state
$Y_x=(f_p(x),f_p(x-1))^{\mathsf T}$ satisfies
$Y_{x+1}=T(x)Y_x$.

The following all-degree theorem strengthens the earlier quadratic
invariant exclusion.

> **Theorem.**  Let
> $\mathscr P(x;y,z)\in\mathbb Q[x,y,z]$ and
> $\lambda\in\mathbb Q^\times$.  Suppose
>
> 

$$
> \mathscr P(x+1;-(4x+2)y+z,y)
> =\lambda\mathscr P(x;y,z)
> \tag{2}
>
$$


>
> as a polynomial identity.  If $\lambda=1$, then
> $\mathscr P$ is constant.  If $\lambda\ne1$, then
> $\mathscr P=0$.

In particular, the recurrence has no nonconstant polynomial first
integral in the index and one state vector, in any state degree.  It
also has no nonzero polynomial anti-invariant.

The proof uses only the classical exponential Padé pair and the
transcendence of $e$.  It does not use the open $p$-adic Euler
factorial constant.

This theorem is deliberately scoped.  It does not exclude rational
invariants with poles, Darboux polynomials with a nonconstant
multiplier, invariants involving two independent state vectors,
nonlocal transforms, or nonlinear auxiliaries that are not exact
recurrence invariants.

No Bessel denominator-height bound is proved.

## 2. Two primitive real solutions

Let



$$
\begin{aligned}
 &q_0=q_1=1,\qquad
 q_n=(4n-2)q_{n-1}+q_{n-2},\\
 &p_0=1,\quad p_1=3,\qquad
 p_n=(4n-2)p_{n-1}+p_{n-2}.
\end{aligned}
\tag{3}
$$



The beta-integral identity is



$$
\frac1{n!}\int_0^1t^n(1-t)^ne^t\,dt
 =(-1)^n(q_ne-p_n)>0.
\tag{4}
$$



It follows immediately that



$$
\frac{p_n}{q_n}\longrightarrow e.
\tag{5}
$$



Indeed, $q_n\geq1$, while the absolute value of (4) is at most
$e\,n!/(2n+1)!$.

Both $p_n$ and $q_n$ are odd.  Hence



$$
s_n=\frac{p_n-q_n}{2}\in\mathbb Z
\tag{6}
$$



is a second integral solution of (3), with $s_0=0,s_1=1$, and



$$
\frac{s_n}{q_n}\longrightarrow
 c:=\frac{e-1}{2}.
\tag{7}
$$



The number $c$ is transcendental.

The discrete Wronskian



$$
W_n=q_ns_{n-1}-s_nq_{n-1}
\tag{8}
$$



satisfies $W_{n+1}=-W_n$ and $W_1=-1$.  Therefore



$$
W_n=(-1)^n.
\tag{9}
$$



For even $n\geq2$, the alternating endpoint formula for $q_n$
also gives



$$
q_n\geq n^n.
\tag{10}
$$



Only the resulting superpolynomial growth along the even integers will
be needed.

## 3. The unimodular fundamental matrix

The signed sequences



$$
\phi_n=(-1)^nq_n,\qquad \psi_n=(-1)^ns_n
\tag{11}
$$



both satisfy



$$
h_{n+1}=-(4n+2)h_n+h_{n-1}.
\tag{12}
$$



Define



$$
F_n=
 \begin{pmatrix}
 \phi_n&\psi_n\\
 \phi_{n-1}&\psi_{n-1}
 \end{pmatrix}.
\tag{13}
$$



Equations (9) and (11) give



$$
\det F_n=(-1)^{n+1},\qquad
 F_1=
 \begin{pmatrix}
 -1&-1\\
 1&0
 \end{pmatrix}.
\tag{14}
$$



Let



$$
M_n=F_nF_1^{-1}.
\tag{15}
$$



Then $M_n$ is the transfer matrix from index $1$ to index $n$.
A direct inversion using (14) gives the crucial exact vector identity



$$
\boxed{
 M_n^{-1}\binom01
 =\binom{q_n-s_n}{s_n}.}
\tag{16}
$$



Thus the projective direction of the backward image of one fixed state
vector converges to



$$
(1-c,c).
\tag{17}
$$



Its two coordinates retain the full factor $q_n$.

## 4. Exclusion in one homogeneous state degree

Because the substitution in (2) is linear in $y,z$, each homogeneous
state-degree component of $\mathscr P$ separately satisfies (2).
Suppose a nonzero component has state degree $m\geq1$, and write



$$
\mathscr P_x(y,z)=\mathscr P(x;y,z).
\tag{18}
$$



First, $\mathscr P_1$ cannot be the zero polynomial.  If it were,
(2) at $x=1$, together with the invertibility of $T(1)$, would give
$\mathscr P_2=0$.  Induction would give
$\mathscr P_n=0$ at every positive integer $n$.  Every coefficient,
being a polynomial in $x$, would then vanish identically.

Iterating (2) from $1$ to $n$ gives the polynomial identity



$$
\mathscr P_n(M_nY)=\lambda^{n-1}\mathscr P_1(Y).
\tag{19}
$$



Set $Y=M_n^{-1}(0,1)^{\mathsf T}$.  Equations (16) and homogeneity
give



$$
\begin{aligned}
 \mathscr P_n(0,1)
 &=\lambda^{n-1}
   \mathscr P_1(q_n-s_n,s_n)\\
 &=\lambda^{n-1}q_n^m
   \mathscr P_1(1-s_n/q_n,s_n/q_n).
\end{aligned}
\tag{20}
$$



The univariate polynomial



$$
R(t)=\mathscr P_1(1-t,t)
\tag{21}
$$



is nonzero.  Indeed, a nonzero homogeneous polynomial cannot vanish
identically on the affine line $y+z=1$: its projective ratios vary
over infinitely many values on that line.

By (7) and the transcendence of $c$,



$$
R(c)\ne0.
\tag{22}
$$



Consequently, along the even integers,



$$
|\mathscr P_n(0,1)|
 \geq C|\lambda|^nq_n^m
\tag{23}
$$



for some fixed $C>0$ and all sufficiently large $n$.
Equations (10) and (23) grow faster than every polynomial in $n$.

But $\mathscr P_n(0,1)$ is simply the coefficient of $z^m$ in
$\mathscr P(x;y,z)$, evaluated at $x=n$.  It has at most polynomial
growth.  This contradiction proves that no positive homogeneous
state-degree component can occur.

## 5. Completion of the theorem

Remove the highest state-degree component and repeat Section 4.
Every positive state-degree component vanishes.  Hence



$$
\mathscr P(x;y,z)=A(x)
\tag{24}
$$



for some $A\in\mathbb Q[x]$, and (2) reduces to



$$
A(x+1)=\lambda A(x).
\tag{25}
$$



If $A\ne0$, comparison of leading terms forces $\lambda=1$, and
then the polynomial periodicity $A(x+1)=A(x)$ forces $A$ to be
constant.  This proves the theorem.

The same argument works over any algebraic coefficient field:
the restriction polynomial $R$ then has algebraic coefficients, and
the transcendental number $c$ still cannot be one of its zeros.

## 6. Consequence for the residual search

Any exact polynomial expression



$$
\mathscr P\bigl(x;f_p(x),f_p(x-1)\bigr)
\tag{26}
$$



which is invariant or anti-invariant under one recurrence step is now
classified: it is constant or zero.  Thus no higher-degree analogue of
the failed quadratic Hankel invariant can encode the ordinary-root
depth while retaining polynomial dependence on the index.

This does not classify polynomial expressions whose value is multiplied
by a nonconstant function of $x$, or determinants built from several
independently transformed states.  Those are the precise algebraic
survivors beyond the theorem.

Nothing here proves
$v_p(n-\rho_{p,r})\log p=o(n\log n)$, or irrationality or
transcendence of $e+\pi$.

## 7. Exact certificate

The companion script

    scripts/bessel_all_degree_polynomial_invariant_certificate.py

checks the $p_n,q_n,s_n$ recurrences and Wronskians, the exact
fundamental-matrix inverse vector (16), superpolynomial lower bounds,
and full-rank invariant systems over finite state- and index-degree
boxes.  It also checks that representative nonzero homogeneous
polynomials restrict nontrivially to $y+z=1$.  The all-degree theorem
is the symbolic proof in Sections 2--5.

Run

    python -m py_compile scripts/bessel_all_degree_polynomial_invariant_certificate.py
    python scripts/bessel_all_degree_polynomial_invariant_certificate.py

For byte-identical replay, use

    python scripts/bessel_all_degree_polynomial_invariant_certificate.py \
      --output /tmp/bessel_all_degree_polynomial_invariant_certificate.json
    cmp results/bessel_all_degree_polynomial_invariant_certificate.json \
      /tmp/bessel_all_degree_polynomial_invariant_certificate.json
