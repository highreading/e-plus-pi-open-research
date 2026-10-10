> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A double-zero index-Hensel counterexample for the Bessel denominator

Checked: 2026-08-27 UTC.

## 1. Exact verdict

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2}.
\tag{1}
$$



The proposed uniform estimate



$$
v_p(q_n)\leq 1+\lceil\log_p n\rceil
\tag{2}
$$



is false.  An exact counterexample is



$$
\boxed{
 p=7,\qquad
 n_*=464838342618219576262104570205987685961890202821,
 \qquad v_7(q_{n_*})=59.}
\tag{3}
$$



Indeed,



$$
7^{56}<n_*<7^{57},
 \qquad
 {q_{n_*}\over 7^{59}}\equiv2\pmod7.
\tag{4}
$$



Thus the right side of $(2)$ is $58$, whereas the left side is $59$.
The class lies on the ordinary $7$-adic index-root branch through $2$:



$$
q_2=7,
 \qquad
 \delta_7(2)={-q_9-q_2\over7}\equiv5\pmod7.
\tag{5}
$$



In the convention that the digit $d_a$ lifts a root modulo $7^a$ to
one modulo $7^{a+1}$, the two digits



$$
d_{57}=d_{58}=0
\tag{6}
$$



are consecutive.  The next digit is $d_{59}=6$.  This rigorously
falsifies the hoped-for assertion that an ordinary branch cannot contain
two consecutive zero Hensel digits.

The counterexample does **not** disprove the weaker block target



$$
V_N(C)=o(N\log N).
\tag{7}
$$



It only rules out one particularly sharp $O(\log N)$ route to $(7)$.

## 2. The exact Mahler evaluation

Put



$$
f(n)=(-1)^nq_n,
 \qquad
 A_j=\Delta^j f(0).
\tag{8}
$$



The already proved index interpolation gives



$$
f(x)=\sum_{j\geq0}A_j\binom{x}{j}
 \quad (x\in\mathbf Z_7),
\tag{9}
$$



where $A_{-1}=0,A_0=1,A_1=-2$ and



$$
A_{j+2}=-4(j+2)A_{j+1}-(8j+6)A_j-4jA_{j-1}.
\tag{10}
$$



Independently, the closed formula is



$$
A_j=(-1)^j j!
 \sum_{m=0}^{\lfloor j/2\rfloor}
 {(-1)^m\over m!}\binom{2j-2m}{j}.
\tag{11}
$$



In particular,



$$
{j!\over\lfloor j/2\rfloor!}\mid A_j.
\tag{12}
$$



For $j\geq869$, even the first Legendre layer gives



$$
\begin{aligned}
 v_7(A_j)
 &\geq v_7(j!)-v_7(\lfloor j/2\rfloor!)\\
 &\geq \left\lfloor{j\over7}\right\rfloor
       -\left\lfloor{\lfloor j/2\rfloor\over7}\right\rfloor
 \geq60.
 \end{aligned}
\tag{13}
$$



The final inequality also follows uniformly from



$$
\left\lfloor{j\over7}\right\rfloor
 -\left\lfloor{\lfloor j/2\rfloor\over7}\right\rfloor
 \geq {j\over14}-1>60.
\tag{14}
$$



Therefore $(9)$, modulo $7^{60}$, is the finite and exact sum



$$
f(n_*)\equiv
 \sum_{j=0}^{868}A_j\binom{n_*}{j}\pmod {7^{60}}.
\tag{15}
$$



Exact integer arithmetic gives



$$
f(n_*)\equiv5\cdot7^{59}\pmod {7^{60}}.
\tag{16}
$$



Since $n_*$ is odd, $f(n_*)=-q_{n_*}$, and $(4)$ follows.  Moreover,



$$
f(n_*+6\cdot7^{59})\equiv0\pmod {7^{60}},
\tag{17}
$$



which checks the orientation and value of the next lift digit.

## 3. Base-$7$ representative and the two zero digits

The least-significant-first base-$7$ digits of $n_*$ are



$$
\begin{split}
(&2,4,6,5,4,0,2,4,5,2,3,6,2,4,4,2,6,4,4,4,3,2,5,6,1,1,1,1,\\
 &5,5,5,6,6,3,6,3,3,5,6,2,2,6,2,5,6,3,6,3,3,6,2,5,3,4,2,1,2).
\end{split}
\tag{18}
$$



There are $57$ displayed digits.  Equations $(15)$--$(16)$ say that
this same integer is a root representative modulo $7^{57}$, $7^{58}$,
and $7^{59}$.  Hence appending the digits at positions $57$ and $58$
appends two zeros.  Appending $6$ at position $59$ produces the root
representative in $(17)$.

## 4. What a sufficient replacement would have to control

Let $r_a\in[0,p^a)$ be a compatible root path (an ordinary path, or one
selected through a surviving singular branch), and write its base-$p$
digits as $d_0,d_1,\ldots$.  If an integer root $n$ on that path has



$$
p^a\mid q_n,
 \qquad
 b=\lceil\log_p(n+1)\rceil<a,
\tag{19}
$$



then necessarily



$$
d_b=d_{b+1}=\cdots=d_{a-1}=0.
\tag{20}
$$



Thus the excess valuation beyond the index scale is exactly a terminal
zero-run problem.  Uniformly for $N\leq n<2N$ and
$p\leq C N\log N$, one has



$$
v_p(q_n)\log p
 \leq \log(2N)+\log p+L_{p,n}\log p,
\tag{21}
$$



where $L_{p,n}$ is the relevant terminal zero-run length.  Consequently,
a uniform estimate



$$
L_{p,n}=o(N)
\tag{22}
$$



over **all surviving root paths** and indices in that range would already
imply $(7)$.  In particular, this formulation does not silently discard
a singular branch.  A much stronger fixed-exponent $p$-adic irrationality
estimate for an ordinary root,



$$
p^{v_p(q_n)}\leq C_p n^{\mu_p}
\tag{23}
$$



would give $v_p(q_n)\log p=O_p(\log n)$ for each fixed $p$, but fixed-
$p$ constants do not by themselves give the uniform-in-$p$ statement
$(7)$.  Neither $(22)$ nor a suitably uniform version of $(23)$ is
proved here.

## 5. Certificate and scope

The companion script

    scripts/bessel_padic_index_double_zero_counterexample_certificate.py

performs the following exact checks.

1. It constructs all $A_j$, $0\leq j\leq868$, both from $(10)$ and
   from $(11)$, and checks equality coefficient by coefficient.
2. It independently checks the finite-difference definition of $A_j$
   through $j=80$ against the integer recurrence $(1)$.
3. It evaluates $(15)$ once with exact binomial coefficients and once
   with a $7$-unit/valuation recurrence for the binomial coefficients.
4. It proves $(16)$, the nonzero quotient
   $q_{n_*}/7^{59}\equiv2\pmod7$, the power interval in $(4)$, $(5)$,
   and the next lift $(17)$.

All calculations are exact integer or modular-integer calculations.  The
finite computation proves the displayed counterexample because $(13)$ gives
a rigorous cutoff; it is not an extrapolation to other branches or levels.

Nothing in this note proves irrationality or transcendence of $e+\pi$.
