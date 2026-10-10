> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Ordinary large-prime Bessel lifts: an exact harmonic expansion and barrier

Checked: 2026-08-27 UTC.

## 1. Verdict

Let



$$
q_0=q_1=1,\qquad
 q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\geq2).
\tag{1}
$$



For every prime $p\geq5$, each reflection orbit in the complete
large-prime window $n<2p$ can be represented by four evaluations around
one base index $0\leq r\leq(p-1)/2$, with two repetitions in the central
orbit.  This note gives an exact finite expansion of all four evaluations
in powers of $p$.  Every coefficient is an explicit sum
of elementary symmetric harmonic sums with denominator prime to $p$.
Consequently the quotient of the unique ordinary square-threshold
representative by $p$ is completely explicit at every $p$-adic order.

The expansion does not yield a sublinear exponent bound.  Section 8 gives a
rigorous countermodel: ordinary slope, reflection, the full all-even
anti-period hierarchy, integral finite expansions, four-point exclusivity,
and an $\exp(O(p\log p))$ height bound are jointly compatible with a
standard representative of valuation $\asymp p$.  The countermodel does
not satisfy the Bessel recurrence or the exact coefficient formulas proved
here.  Its precise conclusion is that a successful bound must use a new
nonvanishing property of those specific coefficients, not merely their
integrality, degree, hierarchy, reflection, or natural global height scale.

No implication for $e+\pi$ is claimed.

## 2. Four evaluations for the window $n<2p$

Define the polynomial hypergeometric terms



$$
T_k(x)={1\over k!}\prod_{a=x-k+1}^{x+k}a
       ={1\over k!}\prod_{j=-k+1}^{k}(x+j),
 \qquad T_0(x)=1,
\tag{2}
$$



and



$$
f(x)=\sum_{k\geq0}(-1)^kT_k(x).
\tag{3}
$$



At every integer $x$, the sum terminates.  For $x\geq0$,



$$
f(x)=(-1)^xq_x,
\tag{4}
$$



and the polynomial terms give the exact reflection



$$
f(-x-1)=f(x).
\tag{5}
$$



Put



$$
s=p-1-r,
 \qquad
 \mathcal Z=\{0,-1,1,-2\},
 \qquad
 F_{p,r}(Z)=(-1)^rf(r+pZ).
\tag{6}
$$



Equations (4)--(5) give the precise index/sign map



$$
\boxed{
 \begin{array}{c|rrrr}
 Z&0&-1&1&-2\\ \hline
 F_{p,r}(Z)&q_r&q_s&-q_{r+p}&-q_{s+p}.
 \end{array}}
\tag{7}
$$



The four indices on the right are exactly the representatives of the
reflection pair below $2p$; when $r=s=(p-1)/2$, the two central indices
each occur twice.

Suppose $p\mid q_r$, and define



$$
c={q_r\over p}\pmod p,
 \qquad
 \delta={-q_{r+p}-q_r\over p}\pmod p.
\tag{8}
$$



The frozen four-point theorem is equivalent to



$$
\boxed{{F_{p,r}(Z)\over p}\equiv c+Z\delta\pmod p
 \qquad(Z\in\mathcal Z).}
\tag{9}
$$



Thus $\delta\ne0$ is the ordinary case, and at most one of the four
values reaches $p^2$.

## 3. Separating every multiple of $p$

Set



$$
K=2p-r-1.
\tag{10}
$$



This is the last nonzero term for the longest evaluation, $Z=-2$; all
other evaluations in $\mathcal Z$ terminate earlier by an explicit zero
factor.

For $0\leq k\leq K$, let



$$
I_{r,k}=\{r-k+1,r-k+2,\ldots,r+k\},
\tag{11}
$$



with $I_{r,0}=\varnothing$.  Define



$$
M_{r,k}=\{m\in\mathbf Z:mp\in I_{r,k}\},
 \qquad
 \epsilon_k=\left\lfloor{k\over p}\right\rfloor,
 \qquad
 \nu_{r,k}=|M_{r,k}|-\epsilon_k.
\tag{12}
$$



Because $k<2p$ and the endpoints of (11) lie strictly between
$-2p$ and $2p$,



$$
M_{r,k}\subseteq\{-1,0,1\},
 \qquad \epsilon_k\in\{0,1\},
 \qquad \nu_{r,k}\geq0.
\tag{13}
$$



Remove those multiples and put



$$
\mathcal A_{r,k}=I_{r,k}\setminus p\mathbf Z,
\tag{14}
$$





$$
U_{r,k}=
 {\displaystyle\prod_{a\in\mathcal A_{r,k}}a
  \over\displaystyle k!/p^{\epsilon_k}},
 \qquad
 \Phi_{r,k}(Z)=\prod_{m\in M_{r,k}}(Z+m).
\tag{15}
$$



Both numerator and denominator of $U_{r,k}$ are prime to $p$, so



$$
U_{r,k}\in\mathbf Z_{(p)}^\times.
\tag{16}
$$



Finally, for $\ell\geq0$, define the elementary symmetric harmonic sums



$$
E_{r,k,\ell}
 =e_\ell\bigl((a^{-1})_{a\in\mathcal A_{r,k}}\bigr),
 \qquad E_{r,k,0}=1,
\tag{17}
$$



and set them equal to zero above $|\mathcal A_{r,k}|$.  Every denominator
in (17) is prime to $p$.

## 4. Exact all-power expansion

Separating the factors $a=mp$ from (2) gives the termwise identity



$$
\boxed{
 T_k(r+pZ)=p^{\nu_{r,k}}U_{r,k}\Phi_{r,k}(Z)
 \sum_{\ell=0}^{|\mathcal A_{r,k}|}
    p^\ell Z^\ell E_{r,k,\ell}.}
\tag{18}
$$



This is an equality in $\mathbf Q[Z]$, not merely a congruence.  Indeed,
each removed numerator factor $mp+pZ$ contributes $p(m+Z)$, while
the unique possible factor $p$ in $k!$ accounts for
$p^{\epsilon_k}$.  The remaining factors expand as



$$
\prod_{a\in\mathcal A_{r,k}}\left(1+{pZ\over a}\right).
$$



For $j\geq0$, define the explicit coefficient polynomial



$$
\boxed{
 \mathcal C_{p,r,j}(Z)=(-1)^r
 \sum_{\substack{0\leq k\leq K\\ \nu_{r,k}\leq j}}
 (-1)^kU_{r,k}\Phi_{r,k}(Z)
 Z^{j-\nu_{r,k}}E_{r,k,j-\nu_{r,k}}.}
\tag{19}
$$



Then, for every one of the four window parameters,



$$
\boxed{
 F_{p,r}(Z)=\sum_{j\geq0}p^j\mathcal C_{p,r,j}(Z)
 \qquad(Z\in\mathcal Z),}
\tag{20}
$$



where the right side is finite.  All coefficients of every
$\mathcal C_{p,r,j}$ lie in $\mathbf Z_{(p)}$.  Moreover,



$$
\boxed{\deg \mathcal C_{p,r,j}\leq j+1.}
\tag{21}
$$



To see (21), a summand in (19) has degree



$$
|M_{r,k}|+j-\nu_{r,k}=j+\epsilon_k\leq j+1.
$$



Only $k\leq r$ has $\nu_{r,k}=0$.  Hence the constant layer is



$$
\boxed{\mathcal C_{p,r,0}(Z)=q_r.}
\tag{22}
$$



This proves the requested terminating factorial/harmonic expansion at every
$p$-adic order.

## 5. The ordinary slope and the exceptional quotient

Assume $p\mid q_r$.  Divide (20) by $p$ and use (22):



$$
\boxed{
 {F_{p,r}(Z)\over p}
 ={q_r\over p}+\mathcal C_{p,r,1}(Z)
 +p\mathcal C_{p,r,2}(Z)+p^2\mathcal C_{p,r,3}(Z)+\cdots}
\tag{23}
$$



for $Z\in\mathcal Z$.  This is a finite exact rational equality whose
value is an integer and whose displayed coefficient denominators are all
prime to $p$.

By (21), $\mathcal C_{p,r,1}$ has degree at most two.  Equations (9) and
(23) show that, modulo $p$, it agrees with $Z\delta$ at the four
distinct points $0,-1,1,-2$.  Therefore



$$
\boxed{
 \mathcal C_{p,r,1}(Z)\equiv Z\delta\pmod p
 \quad\text{as a polynomial in }\mathbf F_p[Z].}
\tag{24}
$$



In particular, the ordinary slope is the explicit finite symmetric-sum
coefficient of $Z$ in (19) at $j=1$.

Let $Z_0\in\mathcal Z$ be the unique ordinary parameter, if any, for
which $p^2\mid F_{p,r}(Z_0)$.  Every higher exponent is now exactly the
valuation of the finite expression



$$
\boxed{
 v_p(F_{p,r}(Z_0))
 =1+v_p\left(
 {q_r\over p}+\sum_{j\geq1}p^{j-1}
 \mathcal C_{p,r,j}(Z_0)
 \right).}
\tag{25}
$$



The reduction of the entire expression in parentheses modulo $p$ vanishes
by the choice of $Z_0$, but no all-prime nonvanishing theorem is known for
the subsequent explicit layers.
Equation (25) is a reduction, not a bound.

## 6. Geometry of the factors

For reference, the exponent $\nu_{r,k}$ in (18) has only four elementary
ranges:



$$
\begin{array}{c|c|c}
\text{range of }k&M_{r,k}&\nu_{r,k}\\ \hline
0\leq k\leq r&\varnothing&0\\
r<k<p-r&\{0\}&1\\
p-r\leq k<p&\{0,1\}&2\\
p\leq k\leq p+r&\{0,1\}&1\\
p+r<k\leq K&\{-1,0,1\}&2.
\end{array}
\tag{26}
$$



Empty ranges are simply omitted.  The factors $Z$, $Z+1$, and
$Z-1$ in this table explain the terminations at $r$, $s$, and
$r+p$; the final evaluation $Z=-2$ terminates at the next, omitted
factor $Z+2$.  Thus no infinite tail has been hidden in (20).

## 7. The unconditional height bound remains linear

The elementary recurrence estimate



$$
0<q_n<4^{n-1}n!\qquad(n\geq2)
\tag{27}
$$



gives, for $p>n/2$,



$$
\boxed{
 v_p(q_n)
 \leq{(n-1)\log4+\log(n!)\over\log p}
 =n+O\left({n\over\log n}\right).}
\tag{28}
$$



The finite expansion (23) does not improve this estimate by denominator
clearing: its coefficients are $p$-integral, but their numerators retain
the same natural factorial-scale height.  A proof of $o(n)$ must show
special noncancellation in (25), not merely bound the sizes of its summands.

## 8. A sharp ordinary-path countermodel

The following theorem scopes exactly what the structural inputs do not
prove.

**Theorem (countermodel).**  Let $p\geq5$, $A\geq2$, and choose



$$
Z_*\in\{0,-1,1,-2\}.
$$



Define the integral linear polynomial



$$
\boxed{G_{p,A,Z_*}(T)=p(T-Z_*-p^{A-1}).}
\tag{29}
$$



Then:

1. $p\mid G(t)$ for every integer $t$, and the normalized slope is the
   unit

   

$$
{\Delta G(t)\over p}=1.
$$



2. Among the four parameters $\mathcal Z$,

   

$$
v_p(G(Z_*))=A,
    \qquad
    v_p(G(Z))=1\quad(Z\ne Z_*).
   \tag{30}
$$



3. For every $k\geq1$, with $C_k=(2k)!/k!$,

   

$$
\boxed{
    \Delta^{2k}G(t)\equiv C_kp^kG(t)\pmod {p^{k+1}}.}
   \tag{31}
$$



   Indeed, the left side is zero and the right side contains $p^{k+1}$.
   The adjacent odd finite differences have the divisibilities required
   by the all-even hierarchy as well: $\Delta G=p$, while every higher
   divided difference is zero.
   Thus the complete local consequence of the all-even Bessel hierarchy is
   satisfied at every order.

4. The companion

   

$$
\widetilde G(T)=G(-1-T)
$$



   has the exact reflection relation used by the paired-fibre arguments.

5. The coefficient height satisfies

   

$$
p^A-2p\leq H(G)\leq p^A+2p\leq2p^A.
   \tag{32}
$$



   Choosing $A=\lfloor cp\rfloor$ for any fixed $c>0$ and all
   sufficiently large $p$ gives

   

$$
\log H(G)=(c+o(1))p\log p,
    \qquad v_p(G(Z_*))\asymp p.
   \tag{33}
$$



The model has the exact permitted finite integral layer form



$$
G(T)=G(0)+pT,
$$



with a constant zeroth layer, a linear first layer, and all higher layers
zero.  For $Z\ne Z_*$, the nonzero difference $Z-Z_*$ has absolute
value at most three and hence is a unit modulo $p$; this proves (30).
Its product over the four low parameters therefore has valuation $A+3$, so a
finite-shift norm or product estimate at the same factorial height scale
also permits a linear exceptional exponent.

The theorem does **not** say that the actual Bessel coefficients in (19)
can realize arbitrary digits.  It proves the narrower and rigorous barrier:

> Ordinary unit slope, reflection, all even finite-difference congruences,
> $p$-integral finite expansions of the permitted degree, four-point
> exclusivity, and $\exp(O(p\log p))$ global height do not imply a
> sublinear exceptional valuation.

Any successful argument must use an additional recurrence-specific
nonvanishing property of the exact symmetric sums $U_{r,k}E_{r,k,\ell}$.

## 9. Frozen dependencies

The four-point quotient law (9) is proved in the frozen source

    sources/bessel_large_prime_four_point_exclusivity.md

with SHA-256

    1e8fed0a5ab04c97c4e0749d40304d6398f9fd32d55c7b49085fb4b4ecca4e41.

The all-even hierarchy used to scope the countermodel is proved in

    sources/bessel_all_even_antiperiod_higher_threshold_exclusivity.md

with SHA-256

    c0c834ca8851ddc8dba9edbc9ec74461c0d3aa1b553f79c2320b3d083a0c37de.

The terminating formula (2)--(4) and the bound (27) also appear in

    sources/bessel_large_prime_unit_cancellation_frontier.md

with frozen SHA-256

    baa384012e6f56f3437de42eb7614e0475763a883529fbfda97120497c97b11d.

## 10. Replay

The companion script reconstructs every set and rational coefficient in
(11)--(19), checks the termwise identity (18), reconstructs all four exact
integer values from (20) for every base orbit at $p=5,7,11,13$, and
verifies (22)--(24) on the ordinary roots at $p=7,11,13$, including the
square lift $13^2\mid q_8$.  It separately verifies every assertion of
the countermodel.  These finite checks are diagnostic only; the expansion
and countermodel are symbolic theorems.

Run

    python -m py_compile scripts/bessel_large_prime_ordinary_harmonic_expansion_barrier_certificate.py
    python scripts/bessel_large_prime_ordinary_harmonic_expansion_barrier_certificate.py

The computation is exact and CPU-bound.  Its memory footprint is tiny
relative to the available 50 GiB RAM; a hardware accelerator would not help
the short rational recurrences.
