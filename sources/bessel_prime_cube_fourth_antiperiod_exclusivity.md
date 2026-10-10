> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Fourth anti-periods and cube-threshold exclusivity for Bessel denominators

Checked: 2026-08-27 UTC.

## 1. Results and scope

Let



$$
q_0=q_1=1,\qquad
 q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\geq2).
\tag{1}
$$



The first result goes one full $p$-adic order beyond the known second
anti-period congruence.

**Theorem 1 (fourth anti-period).**  For every prime $p\geq5$ and every
$n\geq0$,



$$
\boxed{
 q_{n+4p}+4q_{n+3p}+6q_{n+2p}+4q_{n+p}+q_n
 \equiv12p^2q_n\pmod {p^3}.}
\tag{2}
$$



The congruence is also true for $p=3$, by the direct initial check recorded
in Section 5.3, but the cube-count theorems below are stated for $p\geq5$
so that the four residues $0,1,-1,-2$ are distinct and the binomial
polynomials of degree at most three have their usual independent bases.

Now let $p\geq5$, let $p\mid q_r$, and define



$$
a_t=(-1)^tq_{r+tp}\qquad(t\geq0).
\tag{3}
$$



The three divided differences



$$
\begin{aligned}
 d_r&={a_1-a_0\over p}
     ={-q_{r+p}-q_r\over p},\\
 e_r&={a_2-2a_1+a_0\over p^2}
     ={q_{r+2p}+2q_{r+p}+q_r\over p^2},\\
 h_r&={a_3-3a_2+3a_1-a_0\over p^2}\\
    &={-q_{r+3p}-3q_{r+2p}-3q_{r+p}-q_r\over p^2}
 \end{aligned}
\tag{4}
$$



are integers.  No slope is divided out in these definitions.  The first
integrality follows from anti-periodicity, the second from the exact second
anti-period on a root, and the third from a universal third-difference
divisibility proved below.

**Theorem 2 (exact cubic Newton law).**  For every integer $t\geq0$,



$$
\boxed{
 a_t\equiv q_r+tpd_r
       +p^2\binom t2e_r+p^2\binom t3h_r
       \pmod {p^3}.}
\tag{5}
$$



Equivalently, after the legitimate division by $p$,



$$
{a_t\over p}\equiv
 \Gamma_r(t):={q_r\over p}+td_r
   +p\binom t2e_r+p\binom t3h_r
 \pmod {p^2}.
\tag{6}
$$



Thus $p^3\mid q_{r+tp}$ if and only if
$\Gamma_r(t)\equiv0\pmod {p^2}$.  Formula (6) is the promised exact
criterion for the single exceptional representative left by the first-lift
four-point theorem; it is a criterion, not a proof that the residue is
nonzero.

Put



$$
c_r={q_r\over p}\pmod p,
 \qquad
 \delta_r=d_r\pmod p.
\tag{7}
$$



The ordinary and singular cube counts are as follows.

**Theorem 3 (ordinary and singular fibres).**

1. If $\delta_r\ne0$, exactly one $t_0\pmod p$ makes
   $p^2\mid q_{r+t_0p}$.  Among the $p$ standard representatives
   $r+tp$, $0\leq t<p$, at most that one can already be divisible by
   $p^3$.  More precisely, if

   

$$
\Gamma_r(t_0)=pL\pmod {p^2},
$$



   then the unique cube lift has second digit

   

$$
u\equiv-L\delta_r^{-1}\pmod p,
   \tag{8}
$$



   meaning $p^3\mid q_{r+(t_0+pu)p}$.  The standard representative itself
   reaches the cube threshold exactly when $u=0$.

2. If $\delta_r=0$ but $c_r\ne0$, none of the $p$ standard
   representatives is even divisible by $p^2$.

3. If $\delta_r=c_r=0$, all $p$ standard representatives are divisible
   by $p^2$.  In this case define the cubic over $\mathbf F_p$

   

$$
\boxed{
    P_r(T)=C_r+D_rT+E_r\binom T2+H_r\binom T3,}
   \tag{9}
$$



   where

   

$$
C_r={q_r\over p^2},\qquad
    D_r={d_r\over p},\qquad
    E_r=e_r,\qquad H_r=h_r
    \pmod p.
   \tag{10}
$$



   Every division in (10) is integral under the hypotheses.  Then

   

$$
\boxed{p^3\mid q_{r+tp}\quad\Longleftrightarrow\quad P_r(t)=0}
    \qquad(0\leq t<p).
   \tag{11}
$$



   Either $P_r$ is nonzero and at most three of these $p$ representatives
   reach the cube threshold, or $P_r$ is identically zero and all $p$
   do.  The full-fibre alternative is exact:

   

$$
\boxed{
    P_r\equiv0
    \quad\Longleftrightarrow\quad
    C_r\equiv D_r\equiv E_r\equiv H_r\equiv0\pmod p.}
   \tag{12}
$$



The last theorem treats one residue fibre.  Reflection gives a sharper
coupled statement.

**Theorem 4 (reflection-paired cube exclusivity).**  Suppose
$r<s=p-1-r$, $p^2\mid q_r$, and $\delta_r=0$.  The first-lift theorem
then makes both residue fibres singular and all-square.  Their polynomials
satisfy



$$
\boxed{P_s(T)=P_r(-1-T)\quad\text{in }\mathbf F_p[T].}
\tag{13}
$$



Consequently:

* if $P_r\ne0$, at most six of the $2p$ standard representatives
  $r+tp,s+tp$, $0\leq t<p$, reach the cube threshold;
* if $P_r=0$, all $2p$ do;
* among the four representatives in the original large-prime window

  

$$
r,\quad s,\quad r+p,\quad s+p<2p,
  \tag{14}
$$



  either at most three reach the cube threshold, or all four do and this
  already forces $P_r=0$, hence all $2p$ standard representatives do.

At the central fixed point $r=s=(p-1)/2$, one has



$$
P_r(T)=P_r(-1-T).
\tag{15}
$$



After translating by $-1/2$, this is an even polynomial of degree at most
three, hence it actually has degree at most two.  It therefore has at most
two roots in $\mathbf F_p$, unless it vanishes identically, in which case
all $p$ standard representatives reach the cube threshold.

These are genuine all-prime multiplicity statements.  They do **not** bound
the valuation of the one ordinary standard representative that reaches
$p^3$, nor do they exclude the identically-zero singular polynomial.

## 2. Inputs and frozen dependencies

For every odd prime $p$ and every $n\geq0$, the already proved
anti-period and second anti-period congruences are



$$
q_{n+p}\equiv-q_n\pmod p,
\tag{16}
$$





$$
S_2(n):=q_{n+2p}+2q_{n+p}+q_n
 \equiv2p q_n\pmod {p^2}.
\tag{17}
$$



Their complete factorial/recurrence proof is in

    sources/bessel_denominator_zero_gap_smooth_radical_barrier.md

with frozen SHA-256

    dac7cd496b4342a8afc6d379274986d2030bc327c9017b3f6fa877108e62e1fc.

The exact modulus-$p^2$ reflection coupling and the first-lift four-point
theorem are in

    sources/bessel_large_prime_four_point_exclusivity.md

with frozen SHA-256

    1e8fed0a5ab04c97c4e0749d40304d6398f9fd32d55c7b49085fb4b4ecca4e41.

We shall also use the Mahler coefficients of
$f(n)=(-1)^nq_n$.  Their exact formula and divisibility proof are in

    sources/bessel_padic_index_interpolation_analytic_height_barrier.md

with frozen SHA-256

    a50f45248133e437ee318b8cc28e6bbcc51de3568f3e621043221c90ddb4f348.

The specific coefficient facts needed below are reproduced in Section 4,
so the source makes clear exactly where every factor of $p$ enters.

## 3. A recurrence for anti-period binomial sums

For $k\geq0$, put



$$
S_k(n)=\sum_{j=0}^k\binom kj q_{n+jp}.
\tag{18}
$$



Apply (1) to each shifted index $n+jp$.  The identity
$j\binom kj=k\binom{k-1}{j-1}$ gives, for $n\geq2$,



$$
\boxed{
 S_k(n)=(4n-2)S_k(n-1)+S_k(n-2)
        +4kpS_{k-1}(n+p-1).}
\tag{19}
$$



The third binomial sum is



$$
S_3(n)=S_2(n+p)+S_2(n).
\tag{20}
$$



Equations (16)--(17) imply



$$
S_3(n)\equiv2p(q_{n+p}+q_n)\equiv0\pmod {p^2}.
\tag{21}
$$



This proves, in particular, the integrality of $h_r$ in (4).

Take $k=4$ in (19).  By (21), its inhomogeneous term
$16pS_3(n+p-1)$ vanishes modulo $p^3$.  Therefore $S_4(n)$ satisfies
the same homogeneous recurrence as $q_n$, modulo $p^3$.  To prove
Theorem 1 it remains only to establish



$$
S_4(0)\equiv S_4(1)\equiv12p^2\pmod {p^3}.
\tag{22}
$$



The initial values contain the genuinely new arithmetic and are proved next.

## 4. Mahler coefficients at the two initial values

Let $\Delta f(x)=f(x+1)-f(x)$, and put



$$
A_j=\Delta^jf(0).
\tag{23}
$$



The exact coefficient formula is



$$
A_j=(-1)^j j!\sum_{m=0}^{\lfloor j/2\rfloor}
       {(-1)^m\over m!}\binom{2j-2m}{j}.
\tag{24}
$$



Writing $h=\lfloor j/2\rfloor$ immediately gives



$$
{j!\over h!}\mid A_j.
\tag{25}
$$



When $p\mid h$, all terms except $m=h$ disappear modulo $p$ after
normalization.  For the two cases needed here this gives



$$
{A_{4p}\over(4p)!/(2p)!}\equiv1\pmod p,
\tag{26}
$$





$$
{A_{4p+1}\over(4p+1)!/(2p)!}\equiv-2\pmod p.
\tag{27}
$$



Indeed, the surviving binomial coefficient in (27) is
$\binom{4p+2}{4p+1}=4p+2$, and the sign is negative.

There are exactly two multiples of $p$, namely $3p,4p$, in
$(2p,4p]$.  Wilson's theorem on the two intervening reduced blocks gives



$$
{1\over p^2}{(4p)!\over(2p)!}
 \equiv (3\cdot4)((p-1)!)^2\equiv12\pmod p.
\tag{28}
$$



The extra factor $4p+1$ is one modulo $p$.  Thus



$$
A_{4p}\equiv12p^2,\qquad
 A_{4p+1}\equiv-24p^2\pmod {p^3}.
\tag{29}
$$



## 5. Proof of the fourth anti-period

### 5.1 Operator expansion

Let $E=1+\Delta$ be the unit-shift operator and set



$$
R(z)=(1+z)^p-1=z^p+B(z),
 \qquad
 B(z)=\sum_{j=1}^{p-1}\binom pjz^j.
\tag{30}
$$



Every coefficient of $B$ is divisible by $p$, and



$$
R(z)^4=z^{4p}+4z^{3p}B+6z^{2p}B^2+4z^pB^3+B^4.
\tag{31}
$$



Since $R(\Delta)=E^p-1$,



$$
(E^p-1)^4f(0)
 =\sum_j[z^j]R(z)^4 A_j.
\tag{32}
$$



For $3p<j<4p$, (25) gives $p^2\mid A_j$.  For
$2p<j<4p$, it gives $p\mid A_j$.  These valuation statements follow
directly from Legendre's formula; here $4p+1<p^2$ for $p\geq5$.
Consequently, modulo $p^3$:

* the $B^3,B^4$ terms vanish from their coefficients alone;
* the $z^{3p}B$ terms vanish because their coefficients contain $p$
  and their $A_j$ contain $p^2$;
* the $z^{2p}B^2$ terms vanish because their coefficients contain $p^2$
  and their $A_j$ contain $p$.

Only the endpoint remains.  Equations (29) and (32) give



$$
(E^p-1)^4f(0)\equiv A_{4p}\equiv12p^2\pmod {p^3}.
\tag{33}
$$



Because $p$ is odd, the left side of (33) is exactly $S_4(0)$.

### 5.2 The shifted initial value

At $x=1$,



$$
\Delta^jf(1)=A_j+A_{j+1}.
\tag{34}
$$



The same valuation argument remains valid with $A_j+A_{j+1}$; at the
upper endpoints the divisibilities in (25) are unchanged.  Hence



$$
(E^p-1)^4f(1)
 \equiv A_{4p}+A_{4p+1}
 \equiv-12p^2\pmod {p^3}.
\tag{35}
$$



The parity normalization now contributes a minus sign:



$$
(E^p-1)^4f(1)=-S_4(1).
$$



Thus (35) proves the second congruence in (22).  The homogeneous recurrence
from Section 3 now proves (2) for every $n\geq0$.

### 5.3 The prime $p=3$

Modulo $27$, direct recurrence gives



$$
(q_0,q_1,q_3,q_4,q_6,q_7,q_9,q_{10},q_{12},q_{13})
 \equiv(1,1,17,2,7,19,8,17,19,25).
$$



These values give $S_4(0)\equiv S_4(1)\equiv0\pmod {27}$, which equals
$12\cdot3^2q_0\equiv12\cdot3^2q_1$.  Equations (19)--(21) then prove
(2) also for $p=3$.

## 6. Proof of the cubic Newton law

For the sequence (3), its fourth forward difference is



$$
\Delta_t^4a_t
 =(-1)^t S_4(r+tp).
\tag{36}
$$



Anti-periodicity makes $p\mid q_{r+tp}$ for every $t$.  Theorem 1
therefore gives



$$
\Delta_t^4a_t\equiv0\pmod {p^3}.
\tag{37}
$$



All higher forward differences are also zero modulo $p^3$.  Newton's
exact finite-difference formula, reduced modulo $p^3$, is consequently



$$
a_t\equiv a_0+t\Delta a_0+\binom t2\Delta^2a_0
                   +\binom t3\Delta^3a_0\pmod {p^3}.
$$



Substitution of (4) proves (5).  Since every term in (5) and every $a_t$
is divisible by $p$, division of the integer congruence by $p$ proves
(6) modulo $p^2$.  This audits the change of modulus explicitly.

If $t=t_0+pu$, then the two binomial polynomials at $t$ and $t_0$
are congruent modulo $p$, so (6) gives



$$
\Gamma_r(t_0+pu)\equiv\Gamma_r(t_0)+pu d_r\pmod {p^2}.
\tag{38}
$$



Reduction modulo $p$ gives the affine first-lift equation
$c_r+t\delta_r=0$.  If $\delta_r\ne0$, it has one solution and (38)
proves (8).  If $c_r=\delta_r=0$, division of (6) by one further factor
of $p$ gives (9)--(11).  The four binomial-basis polynomials in (9) are
linearly independent over $\mathbf F_p$ for $p\geq5$, proving (12) and
Theorem 3.

## 7. Reflection coupling at the cube threshold

Assume the hypotheses of Theorem 4.  For $0\leq t<p$, reflection modulo
$p^3$ sends



$$
r+tp\longmapsto
 p^3-1-r-tp
 =s+(p-1-t)p+(p-1)p^2.
\tag{39}
$$



The translate parameter on the $s$-fibre is therefore



$$
T=p^2-1-t\equiv-1-t\pmod p.
$$



Moreover, $T$ and $t$ have the same parity.  Exact reflection modulo
$p^3$, followed by the legitimate division by $p^2$, yields



$$
P_r(t)=P_s(-1-t).
\tag{40}
$$



This is (13).  If the common transformed polynomial is nonzero, it has at
most three roots.  Over all $p$ translate parameters each root can occur
once in each of the two fibres, giving at most six cube-threshold
representatives.  If it is zero, (12)--(13) give all $2p$.

For the four low representatives (14), the corresponding arguments of
$P_r$ are



$$
0,\quad1,\quad-1,\quad-2.
\tag{41}
$$



They are distinct for $p\geq5$.  A nonzero cubic cannot vanish at all
four; if all four values reach $p^3$, (41) forces $P_r=0$, proving the
four-to-full-fibre assertion.

When $r=s$, equation (40) becomes (15).  The translation
$U=T+1/2$ changes the involution to $U\mapsto-U$.  An invariant cubic
in characteristic at least five has no odd-degree terms, so it has degree at
most two.  This proves the central count.

## 8. Consequences for windows $n<kp$

Let $1\leq k\leq p$.  The representatives of a noncentral reflection
pair below $kp$ are exactly



$$
r+tp,\quad s+tp\qquad(0\leq t<k).
\tag{42}
$$



For an ordinary fibre, at most one of its $k$ representatives can reach
the square or cube threshold, hence at most two across the pair.

For a singular all-square pair, the cube tests in (42) evaluate the single
polynomial $P_r$ on



$$
\{0,1,\ldots,k-1\}\cup\{-1,-2,\ldots,-k\}.
\tag{43}
$$



If $2k\leq p$, these $2k$ arguments are distinct, so a nonzero cubic
allows at most three cube-threshold representatives across the pair.  For
arbitrary $k\leq p$, each field element occurs at most twice in (43), so
the corresponding bound is six.  If $P_r=0$, all $2k$ representatives
reach the threshold.  The original large-prime window $n<2p$ is the case
$k=2$, giving precisely the dichotomy in Theorem 4.

For a central singular all-square fibre, a nonzero polynomial permits at
most two cube-threshold representatives in every such window; the zero
polynomial permits all $k$.

These counts concern distinct integer representatives, not merely root
classes counted with multiplicity.

## 9. What remains for the denominator-height target

Theorem 1 supplies the exact next finite-difference law, and Theorems 2--4
replace an uncontrolled singular first lift by a cubic obstruction with an
explicit full-fibre condition.  They still do not prove



$$
v_p(q_n)=O(1),\qquad
 v_p(q_n)=o(n),
 \qquad\text{or}\qquad
 v_p(q_n)\log p=o(n\log n)
$$



uniformly for $p>n/2$.  In an ordinary orbit the unique low representative
selected at each level may continue to have zero higher digits.  In a
singular orbit the four congruences in (12) may, in principle, vanish
simultaneously.  Excluding those phenomena requires a new nonvanishing
input; finite-difference degree alone does not provide it.

For $p=2,3$, the original range $0\leq n<2p$ contains no divisor of
$q_n$, as checked in the first-lift package.  Thus the restriction
$p\geq5$ loses no case in the large-prime application.

## 10. Replay

The companion certificate independently reconstructs the recurrence and
Mahler coefficients.  It verifies (2) on a deterministic prime/index grid,
checks the exact initial-value reductions (26)--(29), verifies the cubic
Newton law on every root fibre in its grid, and rechecks the finite
$p<10000$ large-prime window.  The latter still contains only
$13^2\mid q_8$ and no cube; this is explicitly finite evidence, not part
of the proof.

The replay grid contains no singular all-square fibre.  It therefore records
zero qualifying reflection-polynomial instance checks.  The reflection law
(13), the full-fibre alternative (12), and their counts are symbolic
consequences of the proved congruences, not claims inferred from a finite
singular example.

Run

    python -m py_compile scripts/bessel_prime_cube_fourth_antiperiod_exclusivity_certificate.py
    python scripts/bessel_prime_cube_fourth_antiperiod_exclusivity_certificate.py

Peak storage is linear in the largest reconstructed index and remains tiny
relative to the available 50 GiB RAM.
