> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# The first three ordinary Bessel layers and their Wilson carry

Checked: 2026-08-27 UTC.

## 1. Verdict

Let



$$
q_0=q_1=1,\qquad q_n=(4n-2)q_{n-1}+q_{n-2},
\tag{1}
$$



and use the exact large-prime harmonic expansion from the frozen dependency
listed in Section 11.  This note reduces its first three coefficient
polynomials to three explicit finite-field harmonic families.  The two high
factorial blocks are Wilson reflections of the two low blocks.  The result
is an all-prime identity, not a finite extrapolation.

The reduction also gives the actual carried second digit at the unique
ordinary lift.  No bounded valuation theorem follows.  At the base endpoint
$Z=0$, every positive layer vanishes identically, at every order; the
carried digit is just the next digit of $q_r$.  At the other three
endpoints, nonvanishing of a raw second or third layer does not prevent its
cancellation with the carry from lower layers.  Thus a proof based on
``some bounded raw layer is nonzero'' needs, at minimum, a separate theorem
excluding the base endpoint and a noncancellation theorem for the carried
combination derived below.

No implication for $e+\pi$ is claimed.

## 2. The exact five-block decomposition

Fix a prime $p\geq5$,



$$
0\leq r\leq{p-1\over2},\qquad K=2p-r-1.
\tag{2}
$$



For the notation $U_{r,k},\Phi_{r,k},E_{r,k,\ell}$ and
$\mathcal C_{p,r,j}(Z)$, recall the exact formula



$$
\mathcal C_{p,r,j}(Z)=(-1)^r
 \sum_{\substack{0\leq k\leq K\\\nu_{r,k}\leq j}}
 (-1)^kU_{r,k}\Phi_{r,k}(Z)
 Z^{j-\nu_{r,k}}E_{r,k,j-\nu_{r,k}}.
\tag{3}
$$



Split its $k$-range as



$$
\begin{array}{c|c|c}
\text{block}&\text{range}&\nu_{r,k}\\ \hline
A&0\leq k\leq r&0\\
B&r<k<p-r&1\\
C&p-r\leq k<p&2\\
D&p\leq k\leq p+r&1\\
E&p+r<k\leq K&2.
\end{array}
\tag{4}
$$



For a block letter $X$, put



$$
X_\ell^\sharp=
 \sum_{k\text{ in block }X}(-1)^{r+k}U_{r,k}E_{r,k,\ell}.
\tag{5}
$$



Empty blocks contribute zero.  Reading the factors



$$
1,\quad Z,\quad Z(Z+1),\quad Z(Z+1),\quad Z(Z-1)(Z+1)
\tag{6}
$$



from $\Phi_{r,k}$ gives the following **exact identities in
$\mathbf Q[Z]$**:



$$
\boxed{
 \mathcal C_{p,r,1}(Z)
 =Z(A_1^\sharp+B_0^\sharp)+Z(Z+1)D_0^\sharp,}
\tag{7}
$$





$$
\boxed{
 \begin{aligned}
 \mathcal C_{p,r,2}(Z)
 ={}&Z^2(A_2^\sharp+B_1^\sharp)
 +Z(Z+1)C_0^\sharp\\
 &+Z^2(Z+1)D_1^\sharp
 +Z(Z^2-1)E_0^\sharp,
 \end{aligned}}
\tag{8}
$$



and



$$
\boxed{
 \begin{aligned}
 \mathcal C_{p,r,3}(Z)
 ={}&Z^3(A_3^\sharp+B_2^\sharp)
 +Z^2(Z+1)C_1^\sharp\\
 &+Z^3(Z+1)D_2^\sharp
 +Z^2(Z^2-1)E_1^\sharp.
 \end{aligned}}
\tag{9}
$$



No congruence or root hypothesis has been used in (7)--(9).

## 3. Three reduced harmonic families

For $m\in\{0,\ldots,p-1\}$, $d\in\{1,2,3\}$, write



$$
H_m^{(d)}=\sum_{u=1}^m u^{-d}\quad\hbox{in }\mathbf F_p,
 \qquad H_m=H_m^{(1)}.
\tag{10}
$$



For a power-sum vector $P=(P_1,P_2,P_3)$, define



$$
\begin{aligned}
 \operatorname{el}_0(P)&=1,\\
 \operatorname{el}_1(P)&=P_1,\\
 \operatorname{el}_2(P)&={P_1^2-P_2\over2},\\
 \operatorname{el}_3(P)&={P_1^3-3P_1P_2+2P_3\over6}.
 \end{aligned}
\tag{11}
$$



All denominators in (11) are units because $p\geq5$.  Define weights



$$
a_h=(-1)^{r+h}{(r+h)!\over h!(r-h)!}
 \qquad(0\leq h\leq r),
\tag{12}
$$





$$
b_h=-{h!(2r+1+h)!\over(r+1+h)!}
 \qquad(0\leq h\leq p-2r-2),
\tag{13}
$$



and



$$
g_h=(-1)^{r+1}{h!(r-h-1)!\over(2r-h)!}
 \qquad(0\leq h\leq r-1).
\tag{14}
$$



An upper endpoint below zero means that the sum is empty.  Set



$$
P^A_{h,d}=H_{r+h}^{(d)}-H_{r-h}^{(d)},
\tag{15}
$$





$$
P^B_{h,d}=(-1)^dH_h^{(d)}+H_{2r+1+h}^{(d)},
\tag{16}
$$



and



$$
P^G_{h,d}=H_h^{(d)}-H_{2r-h}^{(d)}.
\tag{17}
$$



The three reduced families are



$$
A_\ell=\sum_{h=0}^r a_h\operatorname{el}_\ell(P^A_h)
 \quad(0\leq\ell\leq3),
\tag{18}
$$





$$
B_\ell=\sum_{h=0}^{p-2r-2}b_h\operatorname{el}_\ell(P^B_h)
 \quad(0\leq\ell\leq2),
\tag{19}
$$



and



$$
G_\ell=\sum_{h=0}^{r-1}g_h\operatorname{el}_\ell(P^G_h)
 \quad(0\leq\ell\leq1).
\tag{20}
$$



They are elements of $\mathbf F_p$.  Notice that



$$
A_0=q_r\pmod p.
\tag{21}
$$



Indeed, (18) at $\ell=0$ is the terminating formula for $q_r$.

## 4. Wilson reflection of the high blocks

The elementary identities used below are



$$
(p-1-m)!m!\equiv(-1)^{m+1}\pmod p
\tag{22}
$$



and, for $1\leq d<p-1$,



$$
H_{p-1}^{(d)}=0,
 \qquad
 H_{p-1-m}^{(d)}=(-1)^{d+1}H_m^{(d)}
 \quad\text{in }\mathbf F_p.
\tag{23}
$$



Parameterize block $D$ by $k=p+h$, $0\leq h\leq r$.  Removing
the numerator multiples $0,p$ and the denominator multiple $p$
gives



$$
(-1)^{r+k}U_{r,k}\equiv a_h\pmod p.
\tag{24}
$$



For completeness, the other signed unit reductions, with the parameters
from (26) and $k_C=p-r+h$, are



$$
\begin{aligned}
 (-1)^{r+k_B}U_{r,k_B}&=b_h
     &&\text{in }\mathbf Z_{(p)},\\
 (-1)^{r+k_E}U_{r,k_E}&\equiv b_h\pmod p,\\
 (-1)^{r+k_C}U_{r,k_C}&\equiv g_h\pmod p.
 \end{aligned}
\tag{24a}
$$



The reciprocal power sums of the $D$-block remaining factors reduce,
using (23), to $P^A_{h,d}$, for every $d\in\{1,2,3\}$.  Consequently



$$
\boxed{D_\ell^\sharp\equiv A_\ell\pmod p
 \qquad(0\leq\ell\leq2).}
\tag{25}
$$



Parameterize blocks $B,E$ by



$$
k_B=r+1+h,
 \qquad
 k_E=p+r+1+h,
 \qquad 0\leq h\leq p-2r-2.
\tag{26}
$$



Their signed unit weights have the reductions in (24a), and both reciprocal
power-sum vectors reduce to $P^B_h$, for
$d\in\{1,2,3\}$.  Hence



$$
\boxed{E_\ell^\sharp\equiv B_\ell\pmod p
 \qquad(0\leq\ell\leq1).}
\tag{27}
$$



Finally, put $k=p-r+h$, $0\leq h\leq r-1$, in block $C$.
Wilson complementation gives the weight $g_h$, while (23) gives
$P^G_h$, again for $d\in\{1,2,3\}$.  Thus



$$
\boxed{C_\ell^\sharp\equiv G_\ell\pmod p
 \qquad(0\leq\ell\leq1).}
\tag{28}
$$



Equations (24)--(28) hold for every prime $p\geq5$ and every $r$ in
(2), with all displayed block congruences taken in $\mathbf F_p$.  They
are the special Bessel/Wilson cancellation absent from a generic
finite-difference model.

## 5. Closed formulas for the first three layers

For every prime $p\geq5$ and every $r$ in (2), reducing (7)--(9) with
(25)--(28) proves the following identities in $\mathbf F_p[Z]$, without
assuming that $p\mid q_r$:



$$
\boxed{
 \mathcal C_{p,r,1}(Z)\equiv
 Z(A_1+B_0)+Z(Z+1)A_0\pmod p,}
\tag{29}
$$





$$
\boxed{
 \begin{aligned}
 \mathcal C_{p,r,2}(Z)\equiv{}&
 Z^2(A_2+B_1)+Z(Z+1)G_0\\
 &+Z^2(Z+1)A_1+Z(Z^2-1)B_0
 \pmod p,
 \end{aligned}}
\tag{30}
$$



and



$$
\boxed{
 \begin{aligned}
 \mathcal C_{p,r,3}(Z)\equiv{}&
 Z^3(A_3+B_2)+Z^2(Z+1)G_1\\
 &+Z^3(Z+1)A_2+Z^2(Z^2-1)B_1
 \pmod p.
 \end{aligned}}
\tag{31}
$$



Suppose now that $p\mid q_r$.  Then $A_0=0$, and comparison with
the ordinary first-lift law gives the closed slope formula



$$
\boxed{\delta=A_1+B_0\quad\text{in }\mathbf F_p.}
\tag{32}
$$



In particular, ordinary means precisely that the finite factorial-harmonic
sum on the right of (32) is nonzero.

## 6. The endpoint table

Put



$$
X=A_2+B_1,
 \qquad Y=A_3+B_2.
\tag{33}
$$



For a root $p\mid q_r$, equations (30)--(31) give



$$
\boxed{
\begin{array}{c|c|c}
Z&\mathcal C_{p,r,2}(Z)&\mathcal C_{p,r,3}(Z)\\ \hline
0&0&0\\
-1&X&-Y\\
1&X+2G_0+2A_1&Y+2G_1+2A_2\\
-2&4X+2G_0-4A_1-6B_0&-8Y-4G_1+8A_2+12B_1.
\end{array}}
\tag{34}
$$



This is the requested closed finite-field description at every possible
ordinary window lift $Z_0\in\{0,-1,1,-2\}$.

## 7. The Wilson carry modulo $p^2$

Raw layers are not the digits after carrying.  The first carry can also be
made explicit.  Let



$$
W_p={(p-1)!+1\over p}\pmod p
\tag{35}
$$



be the Wilson quotient.  In block $D$, the exact signed unit belonging
to $k=p+h$ is



$$
d_h^\sharp=-(p-r+h-1)!
 \prod_{j=h+1}^{h+r}(p+j).
\tag{36}
$$



Expanding the complement factorial and the short product modulo $p^2$
gives



$$
\begin{aligned}
 (p-1-m)!&\equiv {(-1)^m\over m!}
 \{-1+p(W_p-H_m)\}\pmod {p^2},\\
 \prod_{j=h+1}^{h+r}(p+j)&\equiv{(r+h)!\over h!}
 \{1+p(H_{r+h}-H_h)\}\pmod {p^2},
 \end{aligned}
\tag{36a}
$$



where $m=r-h$.  Substitution into (36) gives



$$
\boxed{
 d_h^\sharp\equiv a_h\left[1+p\left(
 H_{r+h}-H_h+H_{r-h}-W_p
 \right)\right]\pmod {p^2}.}
\tag{37}
$$



In (37), $a_h$ denotes the lift to $\mathbf Z_{(p)}/p^2$ given by
the same factorial quotient (12); each harmonic number and $W_p$ inside
the parentheses is reduced modulo $p$.  The congruence holds for every
prime $p\geq5$, every $r$ in (2), and every $0\leq h\leq r$.

If $p\mid q_r$, then $\sum_h a_h=q_r$ makes the Wilson quotient
disappear:



$$
\boxed{
 {D_0^\sharp-q_r\over p}\equiv R_r\pmod p,\qquad
 R_r=\sum_{h=0}^r a_h
 (H_{r+h}-H_h+H_{r-h}).}
\tag{38}
$$



This cancellation is exact and does not assume that $W_p\ne0$.

Let



$$
\widehat P=A_1^\sharp+B_0^\sharp\in\mathbf Z_{(p)}
\tag{39}
$$



denote the unreduced low-block sum.  Suppose the root is ordinary and
$Z_0\in\{0,-1,1,-2\}$ is its unique square-threshold parameter, so



$$
{q_r\over p}+Z_0\delta\equiv0\pmod p.
\tag{40}
$$



Then the numerator in the following fraction is divisible by $p$ in
$\mathbf Z_{(p)}$, and (37)--(38) give



$$
\boxed{
 \kappa_2(Z_0)=
 {q_r/p+Z_0\widehat P+Z_0(Z_0+1)q_r\over p}
 +Z_0(Z_0+1)R_r\pmod p.}
\tag{41}
$$



The actual carried second digit is therefore



$$
\boxed{
 {F_{p,r}(Z_0)\over p^2}
 \equiv\kappa_2(Z_0)+\mathcal C_{p,r,2}(Z_0)
 \pmod p.}
\tag{42}
$$



Consequently the valuation is exactly two if and only if the right side
of (42) is nonzero.  Formula (42), unlike raw-layer nonvanishing, includes
the lower-layer carry.

## 8. The precise bounded-layer obstruction

For every $j\geq1$, every summand in (3) contains a factor $Z$: for
$k\leq r$ it comes from $Z^j$, while for $k>r$ it comes from
$\Phi_{r,k}(Z)$.  Hence



$$
\boxed{\mathcal C_{p,r,j}(0)=0\qquad(j\geq1)}
\tag{43}
$$



as an exact rational identity, not just modulo $p$.  If the unique
ordinary lift is $Z_0=0$, equation (42) becomes



$$
{F_{p,r}(0)\over p^2}={q_r\over p^2}.
\tag{44}
$$



Thus the complete positive-layer sequence is blind to the base-endpoint
valuation.  A bounded raw-layer theorem cannot cover this case; it must
first exclude $p^2\mid q_r$ for $p>2r$, or separately bound that
valuation.

For $Z_0\ne0$, (42) shows the other obstruction: a nonzero value in
the endpoint table (34) can cancel with $\kappa_2(Z_0)$.  The third raw
layer has the same issue after the next carry.  Therefore neither
$\mathcal C_2(Z_0)\ne0$ nor
$(\mathcal C_2(Z_0),\mathcal C_3(Z_0))\ne(0,0)$ is, by itself, a
valuation bound.

The low family already contains classical factorial-residue arithmetic.
For example, at $r=0$,



$$
A_0+B_0=-\sum_{h=0}^{p-1}h!\pmod p.
\tag{45}
$$



Thus even its simplest uniform nonvanishing specialization is a genuine
factorial congruence, not a formal consequence of Wilson's theorem.

## 9. Two exact square witnesses

For $(p,r,Z_0)=(13,4,-1)$, the reduced blocks are



$$
A=(0,10,0,0),\quad B=(2,3,10),\quad G=(3,2)
 \quad\text{in }\mathbf F_{13}.
\tag{46}
$$



Here $\kappa_2=8$, $\mathcal C_2(-1)=3$, and



$$
{q_8\over13^2}\equiv8+3=11\pmod {13}.
\tag{47}
$$



A new finite diagnostic square occurs at



$$
p=52453,\quad r=14378,\quad Z_0=1,\quad n=66831.
\tag{48}
$$



The exact recurrence gives



$$
v_p(q_n)=2,\qquad {q_n\over p^2}\equiv41153\pmod p.
\tag{49}
$$



The block calculation gives



$$
\begin{aligned}
 A&=(0,34845,16631,11785),\\
 B&=(31094,10624,6887),\\
 G&=(24501,31115),\\
 R_r&=16091
\end{aligned}
\quad\text{in }\mathbf F_p,
\tag{50}
$$



and



$$
\kappa_2(1)=22712,\qquad
 \mathcal C_2(1)=41041.
\tag{51}
$$



Because $F_{p,r}(1)=-q_n$, equations (42), (49), and (51) agree:



$$
22712+41041\equiv11300\equiv-41153\pmod {52453}.
\tag{52}
$$



## 10. Finite scan scope

An exact eight-thread CPU scan modulo $p^3$, starting strictly above the
frozen $p<10000$ grid, checked



$$
10000\leq p<500000.
\tag{53}
$$



It found the square (48), no other square, and no cube.  More precisely:



$$
\begin{array}{c|r|r|r|r}
\text{prime range}&\#p&\text{ordinary orbits}&\text{singular orbits}
 &\text{square values}\\ \hline
[10000,50000)&3904&1937&0&0\\
[50000,200000)&12851&6430&0&1\\
[200000,500000)&23554&11984&0&0.
\end{array}
\tag{54}
$$



There was no cube in any row.  Equation (54) is an exhaustive recurrence
computation for the displayed finite prime range only.  It is not used in
the proof of (7)--(45), and it does not justify a universal bound
$v_p(q_n)\leq2$.

The scan was CPU-bound exact modular arithmetic.  It used eight CPU threads
and small per-worker $2p$-arrays; a floating-point GPU would not improve
the certified arithmetic.  System RAM remained far below the available
50 GiB.

## 11. Frozen dependencies and replay

The exact all-power expansion (3) is proved in

    sources/bessel_large_prime_ordinary_harmonic_expansion_barrier.md

with SHA-256

    28a91596edafac946448ea68f4c95dfdcd94e63bcf7586394c464a69d6a76e3d.

The four-point sign map and ordinary quotient law are proved in

    sources/bessel_large_prime_four_point_exclusivity.md

with SHA-256

    1e8fed0a5ab04c97c4e0749d40304d6398f9fd32d55c7b49085fb4b4ecca4e41.

The companion replay reconstructs the five blocks independently, verifies
(7)--(31) on a deterministic prime grid, checks the Wilson lift (37)--(38),
and reconstructs both carried square digits (47), (52).  The separate C++
scanner reproduces the explicitly finite diagnostic (54).

Run

    python -m py_compile scripts/bessel_ordinary_first_three_layer_wilson_carry_certificate.py
    python scripts/bessel_ordinary_first_three_layer_wilson_carry_certificate.py
    g++ -O3 -march=native -fopenmp scripts/bessel_ordinary_large_prime_scan.cpp -o /tmp/bessel_ordinary_large_prime_scan
    OMP_NUM_THREADS=8 /tmp/bessel_ordinary_large_prime_scan
