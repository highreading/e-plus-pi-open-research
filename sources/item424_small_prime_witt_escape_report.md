> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 424 — first-Witt small-prime escape: the missing rational endpoint digit and its exact capacity

Date: 2026-09-01  
Status: **ROOT-AUDITED CANONICAL EXACT FIRST-WITT BRIDGE, NO BOOKING**

## 1. Verdict and capacity first

Retain the actual mixed-cubic differentials



$$
\omega_s={u^{6m}\over Q^{4m+1+s}}\,dx,
 \qquad u=x(1-x),\quad Q=(1+x)(1+x^2),\quad s=0,1,
 \tag{1.1}
$$



their endpoint coordinates



$$
H_s=R_s+{L_s\over4}\log2+{E_s\over8}\pi,
 \tag{1.2}
$$



and the two determinant coordinates



$$
A_m=L_1R_0-L_0R_1,
 \qquad
 B_m={L_1E_0-L_0E_1\over8}.
 \tag{1.3}
$$



Item 421 proves that the normalized log pair
$\lambda_s/F_m$ misses genuine post-booking small-prime depth.  This
item identifies exactly what it misses on the entire positive-rate
ordinary rank-zero branch: the **rational component of the first integral
Witt error vector**.

Let $p$ be an odd prime in Item 200's rank-zero set
$\mathcal P_m$, and assume



$$
p^2>4m+1.                    \tag{1.4}
$$



The omitted rows $p^2\leq4m+1$ have
$p\leq\sqrt{4m+1}$ and hence zero linear logarithmic mass.  Define



$$
b_{m,p}=v_p(K_m),
 \qquad
 K_m={\operatorname {lcm}(1,\ldots,4m+1)\over
           \prod_{2m<q<3m}q}.
 \tag{1.5}
$$



Under (1.4), $b_{m,p}\in\{0,1\}$.  This item proves that there are
canonical vectors



$$
\mathcal W_s=(\rho_s,\ell_s,e_s)
 =\left(R_s,{L_s\over p},{E_s\over p}\right)\pmod p
 \in\mathbb F_p^3                                         \tag{1.6}
$$



and two exact first-error determinants



$$
\kappa_{m,p}=\ell_1\rho_0-\ell_0\rho_1
              ={A_m\over p}\pmod p,                       \tag{1.7}
$$





$$
\xi_{m,p}=\ell_1e_0-\ell_0e_1
           ={8B_m\over p^2}\pmod p.                       \tag{1.8}
$$



They satisfy the exact content bridge



$$
\boxed{
 v_p(c_m)\ge b_{m,p}+1
 \iff \kappa_{m,p}=0.}                                    \tag{1.9}
$$



Moreover,



$$
\boxed{
 \kappa_{m,p}=0,\quad\xi_{m,p}\ne0
 \Longrightarrow v_p(c_m)=b_{m,p}+1.}                     \tag{1.10}
$$



On the actual booked overlap



$$
p\in\mathcal P_m\cap\mathcal H_m,qquad p^2>4m+1,
 \tag{1.11}
$$



one has $b_{m,p}=1$.  Therefore Item 393's post-booking depth is
classified by



$$
\boxed{
 w_{m,p}=v_p(c_m)-1\ge1
 \iff\kappa_{m,p}=0.}                                     \tag{1.12}
$$



This answers the local question raised by Item 421.  The characteristic-
$p$ Cartier zero gives $L_s\equiv0\pmod p$, but dividing the two
log residues by $F_m$ retains only $\ell_s$.  The escape condition is
the proportionality of the two **pairs** $(\rho_s,\ell_s)$; it cannot be
read from the two log scalars alone.

The bridge has positive raw support capacity but no proved positive mass.
Canonical Item 200 gives



$$
\mathfrak C_F=-4\log2+{\pi\over\sqrt3}+3\log3.
 \tag{1.13}
$$



Consequently one complete first-Witt radical layer on all rank-zero rows
has ceiling



$$
{\mathfrak C_F\over6}
 =0.3895079179997942811851475804\ldots,                    \tag{1.14}
$$



while the booked overlap (1.11) has the much smaller ceiling



$$
{\mathfrak C_F-2\over6}
 =0.0561745846664609478518142471\ldots .                  \tag{1.15}
$$



Even perfect saturation of (1.14), after granting Item 418's entire
strictly-large ceiling, leaves



$$
0.5908590983307739249345460183\ldots
 -0.3895079179997942811851475804\ldots
 =0.2013511803309796437493984379\ldots .                  \tag{1.16}
$$



Thus one first-Witt layer cannot complete Route 1.  Deeper Witt layers or
other small-prime strata remain indispensable.  No weighted lower bound for
the zero set of $\kappa$ is proved here, and no existing ceiling is
lowered:



$$
\boxed{
 \Delta C_{\leq}=\Delta r_{\rm booked}
 =\Delta C_{\rm global}=\Delta(T-r_1)=0.}                  \tag{1.17}
$$



## 2. Construction of the integral error vector

Write, for each $s$,



$$
6m=a_sp+r_s,
 \qquad
 4m+1+s=b_sp+t_s,
 \qquad0\leq r_s,t_s<p.                                  \tag{2.1}
$$



The usual Cartier factorization is



$$
\omega_s=F_s^pP_s\,dx.                                  \tag{2.2}
$$



Since $p\in\mathcal P_m$,



$$
\deg P_s\leq p-2.                \tag{2.3}
$$



There is therefore a unique primitive with zero constant term



$$
T_s(0)=0,
 \qquad T_s'=P_s,
 \qquad T_s\in\mathbb Z_{(p)}[x].                         \tag{2.4}
$$



The integrality in (2.4) is exact: the possible denominators are
$1,\ldots,p-1$, all $p$-units.  Put



$$
\eta_s=F_s^{p-1}F_s'T_s\,dx.             \tag{2.5}
$$



Differentiation gives the exact Bockstein identity



$$
\boxed{
 \omega_s=d(F_s^pT_s)-p\eta_s.}                           \tag{2.6}
$$



Every rank-zero prime satisfies $p\leq6m$, so the numerator exponent in
$F_s$ is positive.  Hence $F_s(0)=F_s(1)=0$, and the endpoint boundary
of $F_s^pT_s$ vanishes.  Taking the three mixed-cubic coordinates in
(2.6) yields



$$
R_s=-pR(\eta_s),
 \qquad L_s=-pL(\eta_s),
 \qquad E_s=-pE(\eta_s).                                  \tag{2.7}
$$



The rank-zero Cartier theorem already guarantees the required
$p$-integrality.  Equations (1.6) and (2.7) therefore give the intrinsic
formula



$$
\boxed{
 \mathcal W_s
 =\bigl(-pR(\eta_s),-L(\eta_s),-E(\eta_s)\bigr)\pmod p.}  \tag{2.8}
$$



This is a genuine integral lift.  It is not another characteristic-
$p$ degree test: it records the divided first error of the exact
characteristic-zero differential.  Formula (2.8) is the rank-zero
specialization of the archived endpoint Bockstein, but (2.6)--(2.8) give a
self-contained construction for the present branch.

## 3. Proof of the determinant bridge

Write



$$
R_s\equiv\rho_s,
 \qquad L_s=p\ell_s,
 \qquad E_s=pe_s\pmod {p^2}                               \tag{3.1}
$$



with the divided entries interpreted modulo $p$.  Substitution into
(1.3) gives



$$
{A_m\over p}
 \equiv\ell_1\rho_0-\ell_0\rho_1=\kappa_{m,p}\pmod p,    \tag{3.2}
$$





$$
{8B_m\over p^2}
 \equiv\ell_1e_0-\ell_0e_1=\xi_{m,p}\pmod p.             \tag{3.3}
$$



In particular,



$$
v_p(A_m)\ge1,
 \qquad v_p(B_m)\ge2,                                    \tag{3.4}
$$



and



$$
v_p(A_m)\ge2\iff\kappa_{m,p}=0,                         \tag{3.5}
$$





$$
v_p(B_m)=2\iff\xi_{m,p}\ne0.                            \tag{3.6}
$$



Now use the exact normalization



$$
U_m={D_m^\sharp A_m\over G_m},
 \qquad
 V_m={D_m^\sharp B_m\over G_m},
 \qquad
 D_m^\sharp=2^{9m+5}K_m.                                 \tag{3.7}
$$



Because $p\in\mathcal P_m$, the squarefree product $G_m$ contains
exactly one copy of $p$.  Under (1.4),
$v_p(D_m^\sharp)=v_p(K_m)=b_{m,p}$.  Thus



$$
v_p(U_m)=b_{m,p}+v_p(A_m)-1,
 \qquad
 v_p(V_m)=b_{m,p}+v_p(B_m)-1.                              \tag{3.8}
$$



If $\kappa\ne0$, equations (3.4)--(3.5) make the two lower bounds in
(3.8) respectively exact at $b$ and at least $b+1$, so
$v_p(c_m)=b$.  If $\kappa=0$, both are at least $b+1$.
This proves (1.9).  If also $\xi\ne0$, the second coordinate is exactly
$b+1$, proving (1.10).

For $p\in\mathcal P_m\cap\mathcal H_m$ with top layer $q=p$, one has
$p<2m$.  Hence $p\leq4m+1$ and $p$ is not in the removed middle
product, so $b=1$.  Item 149 books exactly that first post-$G_m$ copy.
Equation (1.12) follows.

## 4. The decisive actual row $(m,p)=(13,11)$

Here



$$
N=78,
 \qquad(K_0,K_1)=(53,54),
 \qquad(a,h)=(7,5),                                      \tag{4.1}
$$



and



$$
P_0=uQ^2,
 \qquad P_1=uQ,                                          \tag{4.2}
$$



of degrees $8,5\leq9=p-2$.  Exact rational Hermite reduction and the
independent Bockstein reconstruction (2.8) both give



$$
\mathcal W_0=(7,6,6),
 \qquad
 \mathcal W_1=(2,8,3)
 \quad\text{in }\mathbb F_{11}^3.                         \tag{4.3}
$$



Therefore



$$
\kappa_{13,11}=8\cdot7-6\cdot2=44\equiv0\pmod {11},     \tag{4.4}
$$



whereas



$$
\xi_{13,11}=8\cdot6-6\cdot3=30\equiv8\pmod {11}.       \tag{4.5}
$$



Since $11\in\mathcal P_{13}\cap\mathcal H_{13}$, one has $b=1$.
Equations (1.9)--(1.10) now prove, without reading it off from a gcd scan,



$$
\boxed{v_{11}(c_{13})=2.}                 \tag{4.6}
$$



This is precisely Item 421's missing post-booking digit.  The two log
errors $6,8$ are both nonzero, so dividing $\lambda_s$ by the forced
$F_m$-copy leaves units.  Nevertheless the rational-log pairs



$$
(7,6),\qquad(2,8)                                       \tag{4.7}
$$



are proportional modulo $11$, which makes $\kappa=0$.  The full
three-vectors are not proportional because $\xi\ne0$.  This explains
both the extra content copy and why the depth stops at exactly two.

Two comparison rows separate the roles cleanly.

* At $(m,p)=(2,11)$,
  

$$
\mathcal W_0=(0,1,6),\quad\mathcal W_1=(7,3,6),
  \quad\kappa=4\ne0.
$$


  Here $b=0$, so $v_{11}(c_2)=0$, although $11\mid F_2$.

* At $(m,p)=(9,47)$,
  

$$
\mathcal W_0=(39,37,24),\quad\mathcal W_1=(26,9,5),
  \quad(\kappa,\xi)=(0,31).
$$


  Again $b=0$, but now (1.9)--(1.10) give
  $v_{47}(c_9)=1$.  This is Item 421's upper-small-prime escape.

Thus one and the same Witt coordinate explains all three normalization
phenomena.

## 5. Exact row parametrization and the support capacity

Canonical Item 200 parametrizes every ordinary rank-zero row uniquely by



$$
4m+1=(2j+1)p-2s,
 \qquad1\leq s\leq{p-3\over6},                             \tag{5.1}
$$



with



$$
6m=(3j+1)p+{p-6s-3\over2}.                               \tag{5.2}
$$



In this notation



$$
F={u^{3j+1}\over Q^{2j+1}},
 \qquad
 P_0=u^{(p-6s-3)/2}Q^{2s},
 \qquad
 P_1=u^{(p-6s-3)/2}Q^{2s-1}.                              \tag{5.3}
$$



The degrees are exactly $p-3$ and $p-6$, so the construction in
Section 2 applies uniformly.  Formula (5.3) makes the remaining arithmetic
target explicit: prove weighted zero density, or a useful weighted upper
bound, for the actual moving determinant $\kappa_{m,p}$.

Define the squarefree first-error supports



$$
\mathcal R_W(m)=
 \prod_{\substack{p\in\mathcal P_m,\ p^2>4m+1\\
                   \kappa_{m,p}=0}}p,                       \tag{5.4}
$$



and



$$
\mathcal R_W^{\rm book}(m)=
 \prod_{\substack{p\in\mathcal P_m\cap\mathcal H_m,\
                   p^2>4m+1\\\kappa_{m,p}=0}}p.            \tag{5.5}
$$



They are subsets of Item 200's support.  Since the omitted
$p^2\leq4m+1$ primes contribute $o(m)$, Item 200's exact PNT
calculation gives



$$
\limsup {\log\mathcal R_W(m)\over6m}
 \leq{\mathfrak C_F\over6}.                               \tag{5.6}
$$



The $j=0$ cell has length two per $m$ and is not in $\mathcal H_m$.
Every fixed $j\geq1$ cell has $p<2m$ and is in the booked overlap.
Consequently



$$
\limsup {\log\mathcal R_W^{\rm book}(m)\over6m}
 \leq{\mathfrak C_F-2\over6}.                             \tag{5.7}
$$



Equations (5.6)--(5.7) are genuine capacity upper bounds for **one
squarefree Witt layer**.  They do not bound



$$
\sum_{\kappa_{m,p}=0}(v_p(c_m)-b_{m,p})\log p,            \tag{5.8}
$$



because a zero of $\kappa$ can carry further digits.  A second-error
coordinate is required on the subbranch where the first layer vanishes;
$\xi$ closes only those rows on which it is nonzero.

No theorem here proves a positive lower bound for (5.4) or (5.5).  The raw
capacities are positive, so positive linear mass is arithmetically
possible, but it remains unproved.  Conversely, even their theoretical
maxima are too small to fill Item 418's outside-large residual, as shown in
(1.16).

## 6. Deterministic finite replay

The replay checks every ordinary rank-zero incidence with
$p^2>4m+1$ for $1\leq m\leq100$.  It verifies (1.9) from the exact
stored integers $U_m,V_m$, the exact clearing, and the exact Cartier
product.  It records:

* 1,953 ordinary rank-zero $q=p$ incidences;
* 24 zeros of $\kappa$ among them;
* 13 of those stopped at the first escape layer by $\xi\ne0$;
* 285 incidences in the booked overlap;
* 15 booked-overlap zeros of $\kappa$, of which 4 have $\xi\ne0$;
* the first booked-overlap zero at $(m,p)=(13,11)$; and
* the content-depth distribution
  $1659,279,14,1$ at depths $0,1,2,3$, respectively.

These are exact normalization checks only.  They are not used to infer
density, frequency, or positive mass.

For the three displayed rows, the replay independently reconstructs all
rational endpoint coordinates by Hermite reduction, constructs
$T_s,\eta_s$, verifies (2.6)--(2.8) exactly over $\mathbb Q$, and
checks the two determinant digits against the normalized integer
coordinates.

## 7. Strict claim ledger

### PROVED

* The integral first-Witt error vector (1.6) and its exact Bockstein model
  (2.8).
* The exact first-escape criterion (1.9) on every ordinary rank-zero row
  satisfying (1.4).
* The stopping criterion (1.10).
* The exact post-booking criterion (1.12) on the positive-rate booked
  overlap.
* The complete explanation and exact depth at $(13,11)$, together with
  the comparison rows $(2,11)$ and $(9,47)$.
* The one-layer support ceilings (5.6)--(5.7).
* Zero change to every booked or central ceiling quantity.

### EXACT FINITE ONLY

* Every count and digest in Section 6.
* The observed frequency of $\kappa$- and $\xi$-zeros through
  $m=100$.

### OPEN

* Positive weighted density or weighted zero density for
  $\kappa_{m,p}$.
* A uniform multiplicity bound after $\kappa=0$.
* The next rational Witt digit on the $\kappa=\xi=0$ branch.
* The non-rank-zero and non-Cartier parts of the small-prime remainder.
* Route 1 and the irrationality of $e+\pi$.

### NOT CLAIMED

* That the finite zero census has an asymptotic density.
* That one first-Witt layer supplies positive mass.
* That (5.6) bounds arbitrary higher powers.
* A reduced small-prime ceiling, a new booked divisor, Route-1 closure, or
  an irrationality proof.

## 8. Replay

Run

```text
python scripts/item424_small_prime_witt_escape_certificate.py \
  --output results/item424_small_prime_witt_escape_certificate_replay.json \
  --replay results/item424_small_prime_witt_escape_certificate.json
```

The checker uses only the Python standard library and contains no random
sampling or host-dependent output.  The canonical package is stored under
`sources/`, `scripts/`, `results/`, and `manifests/`.
