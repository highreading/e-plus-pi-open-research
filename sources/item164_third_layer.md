> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 164 — an infinite third-content-layer tail on the congruence slab

Date: 2026-08-29

## 1. Scope and verdict

Let



$$
u=x(1-x),\qquad Q=(1+x)(1+x^2),\qquad
 \omega_s={u^{6m}\over Q^{4m+1+s}}\,dx\quad(s=0,1).
$$



Write the endpoint coordinates as



$$
H_s=R_s+{L_s\over4}\log2+{E_s\over8}\pi,
$$



and retain the item-163 minors



$$
\mathscr A=L_1(pR_0)-L_0(pR_1)=pA_m,
 \qquad
 \mathscr B=L_1E_0-L_0E_1=8B_m.                 \tag{1.1}
$$



This note studies the item-162 slab



$$
p=20k+19\text{ prime},\qquad
 m=18k+17+\ell p,\qquad p\le4m+1<p^2.           \tag{1.2}
$$



Its conclusions are as follows.

**PROVED — exact second-Cartier formula.**  The next normalized
$A$-digit has an explicit characteristic-$p$ formula.  Two
polynomials $H_0,H_1\in\mathbb F_p[x]$, each of degree at most five
and each divisible by $x$, produce two rational differentials



$$
\Phi_s={u^{4+6\ell}H_s\over Q^{5+4\ell}}\,dx.    \tag{1.3}
$$



If



$$
{\mathscr A\over p}=a_0+a_1p+O(p^2),
$$



then $a_0=0$ on the slab and



$$
\boxed{
 a_1=L(\Phi_1)R(\Phi_0)-L(\Phi_0)R(\Phi_1)\pmod p.} \tag{1.4}
$$



This is an exact classification of the third layer at every slab point:
because the period minor supplies its required digit automatically,



$$
p^3\mid c_m\quad\Longleftrightarrow\quad a_1=0.
                                                               \tag{1.5}
$$



**PROVED — an infinite third-layer tail.**  Under (1.2), if



$$
6\ell+4\ge p,                 \tag{1.6}
$$



then both $\Phi_s$ are exact modulo $p$.  Consequently



$$
\boxed{p^3\mid c_m.}           \tag{1.7}
$$



The complete $e=1$ range in (1.2) is



$$
0\le\ell\le5k+3.                    \tag{1.8}
$$



The tail (1.6) is nonempty for every such prime.  In particular,
$\ell=5k+3$ gives the explicit infinite quadratic subray



$$
\boxed{20m=5p^2-17p-2,\qquad p\equiv19\pmod {20}.} \tag{1.9}
$$



Dirichlet's theorem therefore refutes a uniform large-prime assertion
that $p^3\nmid c_m$ on all positive-mass $e=1$ forced bands.

**PROVED — zero-rate limitation.**  Every prime in this theorem still
divides $10m+1$.  At fixed $m$, the product of all selected primes
is at most $10m+1$.  Thus the newly certified third layer has only
$O(\log m)=o(m)$ logarithmic mass.  It does not improve the proved
positive exponential content rate.

**EXPERIMENTAL — exact finite extension only.**  For all slab rows with
$p\le500$, the finite certificate checks 862 rows attached to 13
primes.  The proved tail contains 281 rows and has zero failures.  There
are 301 total third-layer survivors, of which 20 lie before the proved
tail.  Those 20 are diagnostics only.  Six rows with $m\le100$ agree
with the independent item-163 full Hasse-coordinate computation.

**OPEN.**  The pre-tail zeros do not yet have a complete symbolic
classification.  In particular, the 13 finite points on
$10m+1=p^2$ are not promoted to a theorem here.  No positive-mass
third-layer divisor theorem at fixed $m$, no fourth-layer theorem, and
no proof about $e+\pi$ follows from this item.

## 2. Exact slab parameters and the strict $e=1$ band

Put



$$
r=8k+7={2p-3\over5},\qquad t=12k+12.
$$



The item-162 division identities are



$$
\begin{aligned}
 6m&=(5+6\ell)p+r,\\
 4m+1&=(3+4\ell)p+t,\\
 4m+2&=(3+4\ell)p+t+1.                    \tag{2.1}
\end{aligned}
$$



Here $0<t<t+1<p$.  Therefore $p\le4m+1<p^2$ is exactly the
top-prime-power condition $q_p=p$, or $e_p=1$.  In (2.1) it is
equivalent to



$$
0\le\ell\le5k+3.               \tag{2.2}
$$



Indeed, the quotient $3+4\ell$ advances in steps of four and has the
same residue modulo four as $p$; the largest quotient strictly below
$p$ is $p-4$, attained at $\ell=5k+3$.

The equality $4m+1=p^2$ cannot occur inside this slab: (2.1) has the
nonzero remainder $t$ modulo $p$, while $p^2$ has remainder zero.
Equivalently, combining $4m+1=p^2$ with $p\mid10m+1$ would give
$0\equiv-3/2\pmod p$, impossible for $p\equiv19\pmod {20}$.
The strict inequality is nevertheless essential in the general ledger:
at equality the top layer is $q_p=p^2$, so $e_p=2$, and the
item-163 $e=1$ third-layer gate used below is no longer the applicable
normalization.

As in item 162, set



$$
a=5+6\ell,\qquad c=4+4\ell,\qquad
 \mathfrak D=uQ=x(1-x^4).                                  \tag{2.3}
$$



Then the common rational factor and the two Cartier polynomials are



$$
F={u^a\over Q^c},\qquad
 P_0=\mathfrak D^r,\qquad P_1={\mathfrak D^r\over Q},
 \qquad \omega_s=F^pP_s\,dx.                              \tag{2.4}
$$



The support of neither $P_s$ contains $x^{p-1}$.  More explicitly,
$P_0$ has offsets $0\pmod4$ after $x^r$, while $P_1$ has
offsets $0,1\pmod4$, and the target offset is $3\pmod4$.
This is a literal support statement over $\mathbb Z$, not just a
congruence.

## 3. First primitive and the normalized-minor ledger

Let $T_s\in\mathbb Z_{(p)}[x]$ be the zero-constant primitive



$$
T_s'=P_s.                    \tag{3.1}
$$



It is $p$-integral because the only potentially forbidden division is
at the coefficient of $x^{p-1}$, and that coefficient is exactly zero.
Differentiating $F^pT_s$ gives the exact identity



$$
\omega_s=d(F^pT_s)-p\Psi_s,\qquad
 \Psi_s=F^{p-1}F'T_s\,dx.                                \tag{3.2}
$$



Since $a\ge5$, the boundary term $[F^pT_s]_0^1$ is zero.  Hence,
coordinate by coordinate,



$$
(R_s,L_s,E_s)=-p\bigl(R(\Psi_s),L(\Psi_s),E(\Psi_s)\bigr). \tag{3.3}
$$



The rational coordinate on the right can have a denominator $p$; this
is why (3.3) does not by itself force a third content layer.  The
top-layer endpoint lemma gives



$$
\bigl(pR(\Psi_s),L(\Psi_s),E(\Psi_s)\bigr)
 \equiv \operatorname {Frob}\mathcal Z(\mathcal C\Psi_s)\pmod p.
                                                               \tag{3.4}
$$



All terms are integral here.  The pole order of $\Psi_s$ at a root of
$Q$ is $cp+1<p^2$, because (2.2) gives $c\le p-3$.  Thus no
unrecorded $p^2$-denominator band occurs.

On the slab, $L_s,E_s\in p\mathbb Z_{(p)}$ and
$R_s\in\mathbb Z_{(p)}$.  Therefore



$$
\mathscr B=L_1E_0-L_0E_1\in p^2\mathbb Z_{(p)}.          \tag{3.5}
$$



For $e=1,\delta=0$, item 163 gives the exact valuation ledger



$$
v_p(U_m)=1+v_p(\mathscr A/p),\qquad
 v_p(V_m)=2+v_p(\mathscr B/p).                            \tag{3.6}
$$



Thus (3.5) already proves $v_p(V_m)\ge3$.  The only remaining
third-layer condition is $v_p(\mathscr A)\ge3$.

## 4. The explicit second-Cartier polynomial

In $\mathbb F_p(x)$, define



$$
N_s=T_s\{a u'Q-cQ'u\}.                                  \tag{4.1}
$$



Since $F'/F=a u'/u-cQ'/Q$,



$$
{F'\over F}T_s={N_s\over\mathfrak D}.                   \tag{4.2}
$$



For a polynomial differential use the convention



$$
\mathcal C\left(\sum_ng_nx^n\,dx\right)
 =\sum_{j\ge0}g_{pj+p-1}x^j\,dx.                         \tag{4.3}
$$



The identity



$$
\mathfrak D^{p-1}
 =x^{p-1}(1-x^4)^{p-1}
 =x^{p-1}\sum_{j=0}^{p-1}x^{4j}\pmod p                  \tag{4.4}
$$



gives



$$
\mathcal C\left({N_s\over\mathfrak D}\,dx\right)
 ={H_s\over\mathfrak D}\,dx,                            \tag{4.5}
$$



where the promised explicit polynomial is



$$
\boxed{
 H_s(x)=\sum_{n=0}^{5}
 \left(\sum_{j=0}^{p-1}[x^{pn-4j}]N_s\right)x^n.}         \tag{4.6}
$$



Coefficients outside the range of $N_s$ are interpreted as zero.
Indeed, $\deg T_s\le2p-2$ and the factor in braces in (4.1) has
degree at most four, so $\deg N_s\le2p+2$.  After multiplication by
$\mathfrak D^{p-1}$, (4.3) cannot produce an exponent above five.
Also $T_s(0)=0$, hence $N_s(0)=0$, and (4.6) gives $H_s(0)=0$.

Using $\Psi_s=F^p(F'/F)T_s\,dx$ and the Cartier multiplication rule,



$$
\Phi_s:=\mathcal C\Psi_s
 =F{H_s\over\mathfrak D}\,dx
 ={u^{a-1}H_s\over Q^{c+1}}\,dx,                         \tag{4.7}
$$



which is (1.3).

Frobenius fixes the rational $R,L$ coordinates in (3.4).  Substituting
(3.3)--(3.4) into $\mathscr A$, and remembering that
$\mathscr A/p=a_0+a_1p+O(p^2)$, proves



$$
a_1=L(\Phi_1)R(\Phi_0)-L(\Phi_0)R(\Phi_1)\pmod p.       \tag{4.8}
$$



Together with (3.5)--(3.6), this proves the exact criterion (1.5).

## 5. Proof of the infinite exact tail

Assume now (1.6).  Put



$$
\rho=a-1-p=4+6\ell-p,\qquad K=c+1=5+4\ell.              \tag{5.1}
$$



The complete band bound (2.2) gives



$$
0\le\rho<p,\qquad1\le K\le p-2.                        \tag{5.2}
$$



In characteristic $p$, (4.7) becomes



$$
\Phi_s=\left({u\over Q}\right)^p
 \left(u^\rho H_sQ^{p-K}\right)dx.                      \tag{5.3}
$$



The residual polynomial in parentheses has degree



$$
\begin{aligned}
 2\rho+\deg H_s+3(p-K)
 &=2(4+6\ell-p)+\deg H_s+3(p-5-4\ell)\\
 &=p-7+\deg H_s\\
 &\le p-2.                                               \tag{5.4}
\end{aligned}
$$



The elementary characteristic-$p$ exactness lemma says that
$f^pP(x)dx$ is exact whenever $\deg P\le p-2$: integrate $P$
term by term, with no division by $p$.  Equations (5.3)--(5.4)
therefore make both $\Phi_0,\Phi_1$ exact.  In particular,



$$
L(\Phi_s)=E(\Phi_s)=0.                \tag{5.5}
$$



Equation (4.8) gives $a_1=0$, so $v_p(\mathscr A)\ge3$.  Equation
(3.5) gives $v_p(\mathscr B)\ge2$.  The two exact formulas in (3.6)
now yield



$$
v_p(U_m),v_p(V_m)\ge3,           \tag{5.6}
$$



and hence $p^3\mid c_m$.  This proves (1.7).

The interval is nonempty: its upper endpoint $\ell=5k+3$ satisfies



$$
6\ell+4=30k+22\ge20k+19=p.                              \tag{5.7}
$$



Substitution into $m=18k+17+\ell p$ gives (1.9).  Dirichlet supplies
infinitely many primes $p\equiv19\pmod {20}$, so these are arbitrarily
large counterexamples to any universal large-prime third-layer
nondivisibility assertion.

## 6. The gain remains arithmetically thin

For every row of the original slab,



$$
10m+1=(10\ell+9)p.              \tag{6.1}
$$



At fixed $m$, let $\mathcal T_m$ be the primes selected by the new
tail.  They are distinct divisors of $10m+1$, so



$$
\prod_{p\in\mathcal T_m}p\mid10m+1,
 \qquad
 \sum_{p\in\mathcal T_m}\log p\le\log(10m+1)=o(m).      \tag{6.2}
$$



Equation (6.2) is the exact mass of the newly certified third copy.  The
theorem refutes a universal obstruction, but it does not supply the
positive prime-number-theorem-scale mass required by Route 1.

## 7. Exact certificate and replay

The standard-library certificate

`scripts/item164_third_layer_certificate.py`

constructs $P_s,T_s,N_s,H_s,\Phi_s$ over $\mathbb F_p$, computes the
three endpoint coordinates of each $\Phi_s$, checks (4.8) against the
independent item-163 Hasse tower on every available slab row through
$m=100$, and verifies the tail degree inequality (5.4) row by row.

With `--prime-bound 500 --direct-max-m 100`, it records



$$
\begin{array}{l|r}
\text{quantity}&\text{count}\\ \hline
\text{primes }p\equiv19\pmod {20}&13\\
\text{complete slab rows}&862\\
\text{proved-tail rows}&281\\
\text{proved-tail failures}&0\\
\text{all finite }p^3\text{ survivors}&301\\
\text{pre-tail survivors (diagnostic)}&20\\
\text{points with }10m+1=p^2\text{ (diagnostic)}&13\\
\text{independent full-Hasse cross-checks}&6\\
\text{cross-check failures}&0.
\end{array}                                                   \tag{7.1}
$$



Two canonical runs are byte-identical.  Their hashes are pinned in the
item-164 aggregate manifest under `results/`.

## 8. Remaining boundary

The formula (4.8) classifies every slab row exactly, but its zero set
before (1.6) is not symbolically classified.  The finite scan suggests
additional subfamilies, notably $10m+1=p^2$, but finite agreement over
13 primes is not proof.  More importantly, every theorem in this note is
contained in the thin divisor set of $10m+1$.  A Route-1 closure still
needs a positive-mass deeper-digit identity outside this thin set, or a
theorem-scale sequential-matching gain.
