> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 162 — extended lifted-digit census and a proved square-divisor congruence slab

Date: 2026-08-28

## 1. Scope and verdict

This item extends the exact item-161 Hasse-band formula to every item-149
rank-one row and every item-151 vanishing rank-two row with
$1\le m\le100$. It also evaluates the item-161 Bockstein polynomial $T$
at $0,1,-1,i,-i$ on the full $e=1,\delta=0$ rank-one subcensus.

The conclusions are sharply separated.

**PROVED — exact recurrence and replay.** An $O(K_s)$ differential
recurrence computes every local Hasse coefficient with a complete
$p$-adic precision ledger. On 1,048 unique forced rows, the resulting
digit



$$
\eta_{m,p}\equiv {q_pA_m\over p^{1+\delta_{m,p}}}\pmod p
$$



has zero disagreements with the frozen actual $U_m$-coordinate.

**PROVED — a uniform congruence slab.** Let $p\equiv19\pmod {20}$ be
prime. If



$$
p\mid10m+1,\qquad p\le4m+1<p^2,                         \tag{1.1}
$$



then $q_p=p,\ e_p=1,\ \delta_{m,p}=0$, both first Cartier scalars vanish,
and



$$
\boxed{\eta_{m,p}=0,\qquad p^2\mid c_m.}                 \tag{1.2}
$$



Equivalently, writing $p=20k+19$, the whole family is



$$
m=18k+17+\ell p,\qquad \ell\ge0,\qquad4m+1<p^2.         \tag{1.3}
$$



The subfamily $\ell=0$ is the exact affine prime ray



$$
\boxed{9p=10m+1,\qquad p\equiv19\pmod {20}.}             \tag{1.4}
$$



Dirichlet's theorem makes (1.4) infinite. This is nevertheless a thin
gain: for each fixed $m$, every prime supplied by (1.1) divides
$10m+1$, so their product is at most $10m+1$. The extra logarithmic
mass is $O(\log m)=o(m)$, not a positive exponential rate.

**PROVED NO-GO — first two forced layers.** Even the optimistic hypothesis
that every item-149/item-151 forced prime has $\eta=0$ can certify at most



$$
0.5698162598434433286409096558\ldots
$$



per $6m$ from the radical and first lifted layers together. This is below
the required $1.1561471519642446123307302239\ldots$ by at least
$0.5863308921208012836898205681\ldots$. It is a capacity ceiling for the
present two-layer proof mechanism, not an upper bound on actual $c_m$.

**EXPERIMENTAL — finite census and searches.** Of the 1,048 rows, 260 have
$\eta=0$. The searches find many finite coincidences, but no other
symbolically proved family. None of these finite counts is promoted to an
asymptotic density claim.

**OPEN.** A positive-mass theorem for deeper lifted digits, or enough
sequential matching mass after division by the full actual $c_m$, remains
unknown. Item 162 does not decide the status of $e+\pi$.

## 2. Exact linear-time Hasse recurrence

At either local root $\alpha=-1,i$, write



$$
F(t)={A_\alpha(t)^{6m}\over B_\alpha(t)^{K_s}}
     =\sum_{n\ge0}C_n t^n .                                \tag{2.1}
$$



The two local polynomials $A_\alpha,B_\alpha$ are quadratic Gaussian
integer polynomials and have unit constant terms at every odd prime. Direct
differentiation gives



$$
(A_\alpha B_\alpha)F'
=\bigl(6mA_\alpha'B_\alpha-K_sA_\alpha B_\alpha'\bigr)F.    \tag{2.2}
$$



Comparing the coefficient of $t^n$ determines $C_{n+1}$ from the
preceding coefficients after division by
$(n+1)A_\alpha(0)B_\alpha(0)$. The constant factor is a unit. The only
precision loss is therefore $v_p(n+1)$. To return
$C_0,\ldots,C_{K_s-1}\bmod p^P$, start at precision



$$
P+v_p((K_s-1)!)                                             \tag{2.3}
$$



and debit $v_p(n+1)$ at step $n$. The final precision is exactly $P$.
Every division by a power of $p$ is checked for exactness before the
remaining unit is inverted. This proves the recurrence used by the
certificate; it is not a floating-point acceleration.

Sixteen slow-versus-fast coefficient-list comparisons pass before the fast
routine is installed. The completed $m\le100$ run then reproduces all
frozen digits exactly.

## 3. Complete $m\le100$ census

The union contains 928 item-149 rank-one rows and 120 item-151
rank-two-zero rows, with no overlap. Its main totals are



$$
\begin{array}{c|r}
\text{quantity}&\text{count}\\ \hline
\text{unique forced rows}&1048\\
\eta=0&260\\
\eta\ne0&788\\
\text{frozen-}U_m\text{ mismatches}&0\\
\text{rows changed by deleting all lower Hasse bands}&734.
\end{array}                                                  \tag{3.1}
$$



The zero rows split as follows; omitted entries are zero.



$$
\begin{array}{c|c|rrrrr|r}
\text{source}&\delta&e=1&e=2&e=3&e=4&e=5&\text{total}\\ \hline
\text{rank one}&0&35&77&31&20&19&182\\
\text{rank one}&1&15&6&0&0&0&21\\
\text{rank two zero}&0&8&22&11&13&0&54\\
\text{rank two zero}&1&0&3&0&0&0&3\\ \hline
\text{total}&&58&108&42&33&19&260.
\end{array}                                                  \tag{3.2}
$$



Thus lower Hasse bands change 734 of 1,048 digits. The extended scan
reinforces item 161's exact obstruction to a top-layer-only rule.

## 4. Proof of the congruence-slab theorem

Let $p=20k+19$ be prime and assume (1.1). The unique least positive
solution of $10m+1\equiv0\pmod p$ is



$$
m_0={9p-1\over10}=18k+17.
$$



Hence $m=m_0+\ell p$ for some integer $\ell\ge0$. Put
$N=6m,\ K_0=4m+1,\ K_1=K_0+1$. Exact Euclidean division gives



$$
\begin{aligned}
N&=(5+6\ell)p+r,&r&=8k+7,\\
K_0&=(3+4\ell)p+t,&t&=12k+12,\\
K_1&=(3+4\ell)p+(t+1).
\end{aligned}                                               \tag{4.1}
$$



In particular $p-t=r$ and $p-t-1=r-1$. The two item-149 Cartier
polynomials therefore simplify identically to



$$
\begin{aligned}
P_0&=u^rQ^{p-t}=x^r(1-x^4)^r,\\
P_1&=u^rQ^{p-t-1}=x^r(1-x)(1-x^4)^{r-1}.
\end{aligned}                                               \tag{4.2}
$$



Their Cartier scalars are



$$
\gamma_s=[x^{p-1}]P_s.                                      \tag{4.3}
$$



After the initial factor $x^r$, $P_0$ has only offsets congruent to
$0\pmod4$, whereas $P_1$ has only offsets congruent to $0$ or
$1\pmod4$. But the target offset is



$$
p-1-r=12k+11\equiv3\pmod4.                                 \tag{4.4}
$$



Consequently



$$
\boxed{\gamma_0=\gamma_1=0.}                               \tag{4.5}
$$



The relevant degrees are



$$
\deg P_0=5r=2p-3,\qquad \deg P_1=5r-3=2p-6.                \tag{4.6}
$$



Thus both are at most $2p-2$, so $p$ is an item-149 rank-one prime.
The first degree is greater than $p-2$, so the row is not in the old
rank-zero set and $\delta=0$. Also $p<2m$, and (1.1) says precisely
that the top denominator prime-power is $q_p=p$.

The item-149 relative Cartier congruence and (4.5) now give, separately for
$s=0,1$,



$$
(pR_s,L_s,E_s)\equiv(0,0,0)\pmod p.                         \tag{4.7}
$$



It follows that $R_s$ is $p$-integral and $L_s,E_s$ are divisible by
$p$. Hence



$$
A_m=L_1R_0-L_0R_1\equiv0\pmod p,\qquad
pA_m\equiv0\pmod {p^2}.                                    \tag{4.8}
$$



Since $q_p=p$ and $\delta=0$, the exact item-160 one-coordinate bridge
turns (4.8) into (1.2).

The Bockstein formula is consistent term for term. Here



$$
\Theta=\gamma_1P_0-\gamma_0P_1=0,\qquad T'=\Theta,\qquad T=0, \tag{4.9}
$$



so $T(0),T(1),T(-1),T(i),T(-i)$ all vanish and its determinant quotient
is zero. No scalar is inverted.

For each fixed $m$, let $\mathcal S_m$ be the primes supplied by
(1.1). The primes are distinct and each divides $10m+1$, whence



$$
\prod_{p\in\mathcal S_m}p\mid10m+1,\qquad
\sum_{p\in\mathcal S_m}\log p\le\log(10m+1).                \tag{4.10}
$$



This proves both infinitude along the affine subray and the zero
exponential-rate limitation.

## 5. First-two-layer capacity ceiling

Put



$$
R_{H,m}=\sum_{p\in\mathcal H_m}\log p,\qquad
R_{Z,m}=\sum_{p\in\mathcal Z_m}\log p,\qquad
E_{\eta,m}=\sum_{\substack{p\in\mathcal H_m\cup\mathcal Z_m\\
\eta_{m,p}=0}}\log p.                                      \tag{5.1}
$$



The first forced digit contributes $R_{H,m}+R_{Z,m}$, and the first
lifted digit contributes at most one more copy of the same radical.
Therefore



$$
E_{\eta,m}\le R_{H,m}+R_{Z,m},\qquad
R_{H,m}+R_{Z,m}+E_{\eta,m}
\le2(R_{H,m}+R_{Z,m}).                                     \tag{5.2}
$$



The proved rank-one rate and the item-151 rank-two radical ceiling are



$$
{R_{H,m}\over6m}\longrightarrow
r_1=0.1365141682948128184504238226\ldots,\qquad
\limsup {R_{Z,m}\over m}\le
C_2=0.8903637697614530752201860316\ldots .                 \tag{5.3}
$$



Consequently



$$
\limsup {R_{H,m}+R_{Z,m}+E_{\eta,m}\over6m}
\le2\left(r_1+{C_2\over6}\right)
=0.5698162598434433286409096558\ldots .                    \tag{5.4}
$$



The internal-content threshold is



$$
T_{\rm req}=1.1561471519642446123307302239\ldots,
$$



so this ceiling misses it by at least



$$
T_{\rm req}-2\left(r_1+{C_2\over6}\right)
=0.5863308921208012836898205681\ldots .                    \tag{5.5}
$$



This is stronger negative information than the thinness of the new slab:
even a hypothetical positive-mass theorem making every first lifted digit
zero would still be insufficient by itself. Deeper lifted digits or
sequential matching mass after division by the full actual $c_m$ are
unavoidable. Equations (5.4)--(5.5) do not bound unforced factors or deeper
powers in actual $c_m$.

## 6. Bockstein divisor-evaluation audit

The divisor probe covers all 453 $e=1,\delta=0$ item-149 rows through
$m=100$. Its exact counts are



$$
\begin{array}{c|r}
\text{quantity}&\text{count}\\ \hline
\text{integrality-safe rows}&453\\
\eta=0&35\\
T(0)=T(1)=T(-1)=T(i)=T(-i)=0&6\\
\text{all-}T\text{-zero rows with }\eta\ne0&0\\
\text{proved slab rows}&6\\
\text{proved slab failures}&0\\
\text{all-}T\text{-zero rows outside the slab}&0\\
\eta=0\text{ rows not explained by }T\equiv0&29.
\end{array}                                                  \tag{6.1}
$$



The six slab rows are



$$
(m,p)=(17,19),(36,19),(53,59),(55,19),(71,79),(74,19).      \tag{6.2}
$$



For fixed $p=19$, the four rows are exactly the allowed
$m=17+\ell p,\ 0\le\ell\le3$ members before $q_p$ jumps from $19$
to $19^2$. The other 29 zeros arise from nontrivial determinant
cancellation; vanishing of all five evaluations is sufficient here, not a
necessary characterization of $\eta=0$.

The probe deliberately applies the rank-one formula only to
$e=1,\delta=0$. Rank-zero $\delta=1$ rows require the separate
item-161 two-primitive formula and are not silently folded into (6.1).

## 7. Finite pattern searches

All statements in this section are **EXPERIMENTAL exact finite searches**.

The old fixed-$(p,e,\delta,m\bmod q)$ affine test has 56 groups with at
least three usable points: 55 fail and one passes. The unique passing group
is



$$
p=19,\quad e=1,\quad\delta=0,\quad m\equiv17\pmod {19},
$$



on $m=17,36,55,74$. The theorem above now explains this finite group.

A bounded rational-slope search (denominator at most 12) produces 104
all-zero lines through at least four census points; these are dominated by
small-prime coincidences and mixed source branches. Requiring at least two
zero points with $p\ge29$ leaves six unrefined lines:



$$
p=m+8,\quad2p=3m-1,\quad5p=3m+182,\quad6p=m+90,
\quad8p=7m+101,\quad9p=10m+1.                              \tag{7.1}
$$



Every one has a nonzero counterexample somewhere in the stored census.
For $6p=m+90$, the stored counterexample is small
$(m,p)=(12,17)$; the two displayed large-prime zeros alone do not refute
a further refined claim. In particular, the unrefined last line has the
exact nonzero controls



$$
(m,p,\eta)=(26,29,9),(80,89,30),(98,109,66).                \tag{7.2}
$$



These are $p\equiv9\pmod {20}$. The congruence refinement
$p\equiv19\pmod {20}$ in (1.4) is therefore essential, not cosmetic.

No other affine or residue-class family is claimed.

## 8. Exact certificate scope

The archived standard-library files are:

* lifted_endpoint_hasse_extended_certificate.py and
  lifted_endpoint_hasse_extended_census_m100.json;
* witt_divisor_evaluation_probe.py and
  witt_divisor_evaluation_probe_m100.json;
* affine_prime_ray_p2_certificate.py and
  affine_prime_ray_p2_certificate_p5000.json.

The congruence-slab certificate checks all 48,511 complete $e=1$-band
members attached to the 84 primes $p\equiv19\pmod {20}$, $p\le5000$.
It also evaluates the full item-161 Hasse digit on all 33 slab rows with
$p,m\le500$, with zero failures. The $\ell=0$ affine subray contributes
13 of those rows. Ten neighboring $p\equiv9\pmod {20}$ controls are all
nonzero.

Three canonical output replays are byte-identical. The two independent
cross-audits pass the complete census, the congruence-slab proof, the
item-149/item-160 bridge, and the Hasse/Bockstein compatibility.

These finite computations audit the formulas and the frozen data. The
uniform theorem is the symbolic support proof in Section 4; it does not
depend on extrapolating any finite sample.
