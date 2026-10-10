> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Simultaneous Bessel-root residuals: CRT and recurrence-sublattice accounting

Checked: 2026-08-27 UTC.

## 1. Verdict

Fix an integer $n\geq0$.  Let $\mathcal S$ be a finite set of
distinct primes for which $n$ lies on an ordinary Bessel root branch,
and write



$$
a_p=v_p(n-\rho_p)=v_p(q_n),\qquad
 Q=\prod_{p\in\mathcal S}p^{a_p}.
\tag{1}
$$



This note tests whether simultaneous residual conditions, Chinese
remaindering, or a recurrence-special coefficient sublattice can
improve the single-prime lattice barrier.

The answer is exact.

1. For every $B\in\mathbb Z[x]$,

   

$$
\boxed{
   v_p(B(\rho_p))\geq a_p\quad(p\in\mathcal S)
   \quad\Longleftrightarrow\quad Q\mid B(n).}
   \tag{2}
$$



   Thus simultaneous ordinary-root conditions at the same integer
   center are one ordinary CRT congruence.
2. Let $\Gamma$ be any finitely generated additive subgroup of
   integral polynomials, and suppose its evaluation ideal is

   

$$
E_n(\Gamma)=\{B(n):B\in\Gamma\}=g\mathbb Z,
   \qquad g\geq1.
   \tag{3}
$$



   For

   

$$
\Gamma(Q)=\{B\in\Gamma:Q\mid B(n)\},
   \tag{4}
$$



   one has

   

$$
\boxed{
   [\Gamma:\Gamma(Q)]
   =\frac{Q}{\gcd(Q,g)},\qquad
   E_n(\Gamma(Q))=\operatorname{lcm}(Q,g)\mathbb Z.}
   \tag{5}
$$



   Hence the CRT determinant gain never exceeds
   $Q=\prod p^{a_p}$.  Any reduction caused by $g$ is exactly
   pre-existing divisibility of every evaluated form in $\Gamma$.
3. Every $B\in\Gamma(Q)$ with $B(n)\ne0$ still satisfies

   

$$
|B(n)|\geq\operatorname{lcm}(Q,g)\geq Q
   \tag{6}
$$



   and therefore

   

$$
\boxed{
   \log Q\leq
   \log H_1(B)+\deg(B)\log(n+1).}
   \tag{7}
$$



   The full polynomial lattice has $g=1$, determinant gain $Q$,
   and the primitive polynomial $x+(Q-n)$ matches the
   evaluation-weighted threshold within one unit when $Q\geq n$.
4. Recurrence shifts do not create a hidden sublattice.  If

   

$$
f_p(x+j)=U_j(x)f_p(x)+V_j(x)f_p(x+1),
   \tag{8}
$$



   then

   

$$
U_jV_{j+1}-U_{j+1}V_j=(-1)^j.
   \tag{9}
$$



   Consequently two adjacent shifts with arbitrary integral-polynomial
   multipliers generate every residual polynomial $B\in\mathbb Z[x]$.
   A restricted construction may define a proper $\Gamma$, but its
   complete modular accounting is then (5).
5. If $B=cB_0$ with $B_0$ primitive, the residual modulus remaining
   after primitive normalization is

   

$$
\frac{Q}{\gcd(Q,c)}.
   \tag{10}
$$



   The removed factor $\gcd(Q,c)$ is no larger than the
   archimedean content $|c|$.  Thus content cannot turn the summed
   CRT order into a net primitive-height gain.

This rules out a multi-prime amplification based only on simultaneous
vanishing of one residual polynomial and the Bessel shift recurrence.
It does not rule out genuinely different local equations, different
integer centers coupled by an additional identity, or a nonlinear
construction with an independently proved exceptional height bound.

No denominator-height estimate, irrationality result, or
transcendence result is proved.

## 2. Simultaneous ordinary roots collapse by CRT

For every $p\in\mathcal S$, the integral polynomial identity



$$
B(X)-B(Y)=(X-Y)C_B(X,Y),\qquad C_B\in\mathbb Z[X,Y],
\tag{11}
$$



and $v_p(n-\rho_p)=a_p$ imply



$$
B(\rho_p)\equiv B(n)\pmod {p^{a_p}\mathbb Z_p}.
\tag{12}
$$



Thus the $p$-th condition in (2) is equivalent to
$p^{a_p}\mid B(n)$.  The moduli are pairwise coprime, so the Chinese
remainder theorem proves (2).

In degree at most $d$, the simultaneous coefficient lattice therefore
has the explicit basis



$$
Q,\quad x-n,\quad (x-n)x,\quad\ldots,\quad
 (x-n)x^{d-1},
\tag{13}
$$



determinant $Q$, and dual



$$
\mathbb Z^{d+1}
 +\frac1Q\mathbb Z(1,n,\ldots,n^d).
\tag{14}
$$



Equivalently, intersection of the individual prime-power lattices
multiplies their indices exactly:



$$
[\mathbb Z^{d+1}:\Lambda_d(n;Q)]
 =Q=\prod_{p\in\mathcal S}p^{a_p}.
\tag{15}
$$



There is no additional determinant factor beyond the sum of the local
logarithmic depths.

With the evaluation-adapted norm



$$
\|\boldsymbol b\|_{1,n+1}
 =\sum_{j=0}^{d}|b_j|(n+1)^j,
\tag{16}
$$



every nonzero-evaluation point in this lattice has norm at least $Q$.
When $Q\geq n$, the primitive polynomial



$$
B_*(x)=x+(Q-n)
\tag{17}
$$



has $B_*(n)=Q$ and weighted norm $Q+1$.  Thus even the simultaneous
primal-dual threshold lies in the exact interval $[Q,Q+1]$.

Using separate residuals cannot improve the summed accounting either.
If $B_p(n)\ne0$ and
$v_p(B_p(\rho_p))\geq a_p$, then the single-prime evaluation bound
gives



$$
\sum_{p\in\mathcal S}
 \left(\log H_1(B_p)+\deg(B_p)\log(n+1)\right)
 \geq\sum_{p\in\mathcal S}a_p\log p
 =\log Q.
\tag{18}
$$



## 3. An arbitrary recurrence-special additive sublattice

Let $\Gamma$ be a nonzero finitely generated free abelian group of
integral polynomials.  Evaluation is a homomorphism



$$
E_n:\Gamma\longrightarrow\mathbb Z.
\tag{19}
$$



If $E_n(\Gamma)=0$, every member has $B(n)=0$, so the group is
unusable for the residual argument.  Otherwise its image is the
principal ideal $g\mathbb Z$ in (3).

Reducing (19) modulo $Q$, the image is the cyclic subgroup of
$\mathbb Z/Q\mathbb Z$ generated by $g$.  Its order is



$$
\frac{Q}{\gcd(Q,g)}.
\tag{20}
$$



The kernel is precisely $\Gamma(Q)$.  The first isomorphism theorem
proves the index formula in (5).

The evaluations that are both in $g\mathbb Z$ and divisible by $Q$
form



$$
g\mathbb Z\cap Q\mathbb Z
 =\operatorname{lcm}(g,Q)\mathbb Z,
\tag{21}
$$



which proves the second formula in (5) and (6).  Prime by prime,



$$
[\Gamma:\Gamma(Q)]
 =\prod_{p\in\mathcal S}
 p^{\max\{0,a_p-v_p(g)\}}.
\tag{22}
$$



The local determinant gain lost to $v_p(g)$ has not vanished: it is
already present in every value $B(n)$, $B\in\Gamma$.  In
particular,



$$
\begin{aligned}
 \log[\Gamma:\Gamma(Q)]+\log g
 &=\log Q+\log\frac{g}{\gcd(Q,g)}\\
 &\geq\log Q.
\end{aligned}
\tag{23}
$$



This is the exact determinant accounting identity.

Finally,



$$
|B(n)|\leq H_1(B)(n+1)^{\deg B}
\tag{24}
$$



turns (6) into (7).  A smaller congruence index inside $\Gamma$
cannot imply a smaller evaluated-height cost.

## 4. Application to the Bessel shift module

The Bessel interpolation satisfies



$$
f_p(x+2)+(4x+6)f_p(x+1)-f_p(x)=0.
\tag{25}
$$



Define $U_j,V_j\in\mathbb Z[x]$ for $j\geq0$ by



$$
\begin{aligned}
 &(U_0,V_0)=(1,0),\qquad (U_1,V_1)=(0,1),\\
 &(U_{j+2},V_{j+2})
 =(U_j,V_j)-(4x+4j+6)(U_{j+1},V_{j+1}).
\end{aligned}
\tag{26}
$$



Then induction in (25) proves (8).  Put



$$
D_j=U_jV_{j+1}-U_{j+1}V_j.
\tag{27}
$$



The recurrence (26) gives $D_{j+1}=-D_j$, while $D_0=1$.
This proves (9) for every $j\geq0$.

Now let $P_j,P_{j+1}\in\mathbb Z[x]$.  The residual coefficient of



$$
P_j(x)f_p(x+j)+P_{j+1}(x)f_p(x+j+1)
\tag{28}
$$



is



$$
P_jV_j+P_{j+1}V_{j+1}.
\tag{29}
$$



Equation (9) supplies the integral Bézout representation



$$
1=(-1)^j\bigl(U_jV_{j+1}-U_{j+1}V_j\bigr).
\tag{30}
$$



Multiplying (30) by an arbitrary $B(x)\in\mathbb Z[x]$ and using the
two resulting coefficients in (28) realizes that $B$ as a residual.
Thus the unrestricted adjacent-shift module has $\Gamma=\mathbb Z[x]$
and $g=1$.  The recurrence itself contributes no congruence index.

Degree or height restrictions on the multipliers can define a smaller
finite-rank image.  Formula (5) applies to that image.  The degree and
height needed to multiply (30) by $B$ are an archimedean cost, not an
extra CRT determinant.

There is also a transparent one-generator example.  If residuals are
restricted to



$$
B(x)=A(x)V_j(x),
\tag{31}
$$



then their evaluation ideal is $V_j(n)\mathbb Z$.  For $j\geq1$,
equation (26) gives by induction



$$
(-1)^{j-1}V_j(n)>0\qquad(n\geq0).
\tag{32}
$$



If $Q\mid V_j(n)$, the new congruence index can fall to $1$, but
every nonzero evaluated residual already has absolute value at least
$|V_j(n)|\geq Q$.  Automatic recurrence divisibility replaces local
index by pre-existing evaluated size; it does not create a height
saving.

## 5. Primitive normalization for a composite CRT modulus

Let $B=cB_0$, where $B_0\in\mathbb Z[x]$ is primitive and
$c\ne0$.  From $Q\mid cB_0(n)$, elementary cancellation gives



$$
\frac{Q}{\gcd(Q,c)}\mid B_0(n).
\tag{33}
$$



If $B(n)\ne0$, equations (24) and (33) yield



$$
\boxed{
 \log\frac{Q}{\gcd(Q,c)}
 \leq
 \log H_1(B_0)+\deg(B_0)\log(n+1).}
\tag{34}
$$



Since $\gcd(Q,c)\leq|c|$,



$$
\begin{aligned}
 \log Q
 &\leq
 \log|c|+\log H_1(B_0)+\deg(B_0)\log(n+1)\\
 &=\log H_1(B)+\deg(B)\log(n+1).
\end{aligned}
\tag{35}
$$



Thus primitive normalization accounts for all simultaneous
prime-power content exactly.

## 6. Scope and exact survivor

The following routes are now rigorously closed:

- intersecting the ordinary-root congruence lattices for several
  primes at the same $n$;
- applying generic transference or coefficient capacity to that
  intersection;
- restricting to an additive recurrence-generated coefficient lattice
  and counting its congruence determinant without also counting its
  evaluation ideal;
- and inserting CRT order through removable coefficient content.

A surviving construction must use more than simultaneous copies of
$B(\rho_p)\equiv0$: for example, genuinely different local
functional equations, a relation coupling distinct integer centers,
or a nonlinear family with an independently proved primitive
height collapse and nonvanishing.

Nothing here proves the required bound for
$\sum_pv_p(q_n)\log p$, or any irrationality or transcendence result.

## 7. Exact certificate

The companion script

    scripts/bessel_simultaneous_crt_recurrence_sublattice_certificate.py

checks simultaneous CRT lattices, dual pairings and weighted
near-attainers; the general subgroup index and evaluation-ideal
formulas; the all-shift Bessel polynomial recurrence and adjacent
Bézout identity; representative restricted shift sublattices; and
composite-content cancellation over finite exact boxes.  The
all-parameter results are the symbolic proofs above.

Run

    python -m py_compile scripts/bessel_simultaneous_crt_recurrence_sublattice_certificate.py
    python scripts/bessel_simultaneous_crt_recurrence_sublattice_certificate.py

For byte-identical replay, use

    python scripts/bessel_simultaneous_crt_recurrence_sublattice_certificate.py \
      --output /tmp/bessel_simultaneous_crt_recurrence_sublattice_certificate.json
    cmp results/bessel_simultaneous_crt_recurrence_sublattice_certificate.json \
      /tmp/bessel_simultaneous_crt_recurrence_sublattice_certificate.json
