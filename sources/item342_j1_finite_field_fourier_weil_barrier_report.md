> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 342 — exact finite-field Kummer lift and the Fourier/Weil barrier for fixed $j=1$

Date: 2026-09-01

## 1. Outcome and capacity first

Item 339 reduced the selected fixed-$j=1$ factor on the actual row to



$$
a_{r,n}=[u^n]G(u)^{-r}\in\mathbb Z,\qquad
 G(u)=1-4u+6u^2-4u^3,                                    \tag{1.1}
$$



where



$$
n=2h,\qquad r=2s+1,\qquad p=2n+3r,\qquad 2M=3n+4r.       \tag{1.2}
$$



The original collision implies $a_{r,n}=0\pmod p$; the converse is not
claimed.  Item 339 showed that termwise carries cannot settle the remaining
positive-rate cancellation.  This item gives an exact all-row finite-field
model and determines why ordinary complete-sum estimates still do not settle
it.

Put



$$
H_{p,r}(u)=G(u)^{p-r}.                                    \tag{1.3}
$$



Freshman's dream and $n<p$ give



$$
\boxed{
 a_{r,n}\equiv [u^n]H_{p,r}(u)\pmod p.}                  \tag{1.4}
$$



Moreover,



$$
p-r=2(r+n),\qquad
 D:=\deg H_{p,r}=3(p-r)=2p+2n.                            \tag{1.5}
$$



There are two exact Fourier realizations.

1. Over $\mathbb F_p$, the plain multiplicative moment aliases exactly
   three coefficients:

   

$$
-\sum_{x\in\mathbb F_p^\times}x^{-n}H_{p,r}(x)
   =c_n+c_{n+p-1}+c_{n+2(p-1)},                            \tag{1.6}
$$



   where $c_j=[u^j]H_{p,r}$.

2. Over $\mathbb F_{p^2}$, one moment isolates the target:

   

$$
\boxed{
   c_n=-\sum_{x\in\mathbb F_{p^2}^\times}
                  x^{-n}G(x)^{p-r}.}                     \tag{1.7}
$$



The first model has the attractive complex square-root scale
$O(\sqrt p)$, but it does not isolate the collision-forced coefficient.
The second isolates it, but its square-root scale is
$\sqrt{p^2}=p$, already too large to rule out divisibility by $p$.

The three aliases can be separated over $\mathbb F_p$.  With
$\vartheta=u\,d/du$, define



$$
S_j=\sum_{x\in\mathbb F_p^\times}
            x^{-n}(\vartheta^jH_{p,r})(x),\qquad 0\leq j\leq2. \tag{1.8}
$$



Then exact Vandermonde inversion gives



$$
\boxed{
 c_n=-{1\over2}\left(
 S_2+(3-2n)S_1+(n-1)(n-2)S_0\right).}                    \tag{1.9}
$$



After Teichmüller lifting, (1.9) produces an algebraic integer
$\mathcal T_{p,r,n}\in\mathbb Z[\zeta_{p-1}]$ such that, at a chosen
prime $\mathfrak p\mid p$,



$$
\mathcal T_{p,r,n}\equiv a_{r,n}\pmod{\mathfrak p},\qquad
 |\sigma(\mathcal T_{p,r,n})|\leq21\sqrt p               \tag{1.10}
$$



for every complex embedding $\sigma$.  This is a genuine fixed-support
Kummer-sum lift of the actual target.

However, $p$ splits completely in $\mathbb Q(\zeta_{p-1})$, and (1.10)
concerns only one chosen prime above $p$.  The norm bound is merely



$$
|N(\mathcal T_{p,r,n})|
 \leq(21\sqrt p)^{\varphi(p-1)},                           \tag{1.11}
$$



which is entirely compatible with $p\mid N(\mathcal T_{p,r,n})$.
Complex Weil bounds, even after exact de-aliasing, therefore do not prove
that the target is a $p$-adic unit.

This closes a broad but precise method class:



$$
\boxed{
 \begin{gathered}
 \text{plain coefficient Fourier extraction plus a black-box Weil bound,}\\
 \text{with or without finite Euler-moment de-aliasing, cannot by itself}\\
 \text{reduce the fixed-}j=1\text{ ceiling.}
 \end{gathered}}                                         \tag{1.12}
$$



The missing input is $p$-adic: chosen-prime nonconcentration, a unit-root
theorem, or descent to a rational or bounded-degree trace together with an
exact nonzero theorem.

No such theorem is proved here.  Hence



$$
\boxed{
 \text{new linear log rate}=0,\qquad
 \text{new fixed-}j=1\text{ capacity reduction}=0,\qquad
 \text{retained ceiling}={1\over36}.}                     \tag{1.13}
$$



## 2. The positive-power Frobenius chart

In $\mathbb F_p[[u]]$,



$$
G(u)^p=G(u^p).                                           \tag{2.1}
$$



Therefore



$$
G(u)^{-r}=G(u)^{p-r}G(u^p)^{-1}.                         \tag{2.2}
$$



Because $n<p$, only the constant coefficient of $G(u^p)^{-1}$
contributes to degree $n$.  This proves (1.4).  Equations (1.2) give



$$
p-r=2r+2n,\qquad
 3(p-r)=6r+6n=2p+2n,                                     \tag{2.3}
$$



which proves (1.5).

The same integer has the exact terminating hypergeometric representation



$$
\begin{aligned}
 a_{r,n}
 &={4r+n-1\choose n}\\
 &\quad\times
 {}_4F_3\!\left(
 \begin{matrix}
 -n/4,&(1-n)/4,&(2-n)/4,&(3-n)/4\\
 r+1/4,&r+1/2,&r+3/4
 \end{matrix};1\right).                                  \tag{2.4}
\end{aligned}
$$



Indeed, the ratio of its $k$-th term to its zeroth term is



$$
{ (r)_k\over k!}
 {n!\over(n-4k)!}
 { (4r-1)!\over(4r+4k-1)!}.                              \tag{2.5}
$$



The multiplication formula for rising factorials cancels $(r)_k$,
giving (2.4).  This is an all-row identity, not a finite fit.  It identifies
a natural hypergeometric route, but an Archimedean estimate for (2.4) still
does not control reduction at the tied prime.

## 3. Exactly three aliases over the base field

Write



$$
H_{p,r}(u)=\sum_{j=0}^{D}c_ju^j.                          \tag{3.1}
$$



For every integer $m$,



$$
\sum_{x\in\mathbb F_p^\times}x^m
 =\begin{cases}
 -1,&p-1\mid m,\\
 0,&p-1\nmid m.
 \end{cases}                                              \tag{3.2}
$$



Thus a multiplicative moment at frequency $n$ sees all indices congruent
to $n\pmod{p-1}$.  From (1.5),



$$
D-\bigl(n+2(p-1)\bigr)=n+2>0,                            \tag{3.3}
$$



whereas



$$
D-\bigl(n+3(p-1)\bigr)=3-3r-n<0.                        \tag{3.4}
$$



Hence the three indices in (1.6) are present and there is no fourth.

The two upper coefficients are not conditions forced by the original
collision.  A nonzero theorem or Weil bound for their sum with $c_n$
cannot be credited toward $W_b(M)$ without another theorem separating
the actual target.

## 4. Exact isolation over $\mathbb F_{p^2}$

Let $q=p^2$.  Since every actual $p\geq13$,



$$
D=2p+2n<3p<p^2-1=q-1.                                  \tag{4.1}
$$



The analogue of (3.2) on $\mathbb F_q^\times$ has only one index
congruent to $n\pmod{q-1}$ in the degree range, which proves (1.7).

If $\omega_q$ is the Teichmüller character of
$\mathbb F_q^\times$, the lift



$$
\sum_{x\in\mathbb F_q^\times}
 \omega_q(x)^{-n}\omega_q(G(x))^{p-r}                    \tag{4.2}
$$



is a pure complete Kummer sum with a fixed number of singular points.
Its standard square-root scale is $O(\sqrt q)=O(p)$.  Even if (4.2)
descended to an ordinary integer, an $O(p)$ bound would not exclude a
nonzero multiple of $p$.  Thus extension-field isolation plus a black-box
Weil bound has zero ledger capacity.

## 5. Euler-moment de-aliasing over $\mathbb F_p$

Applying $\vartheta^j$ multiplies $c_m$ by $m^j$.  Therefore



$$
-S_j=\sum_{\ell=0}^{2}
 \bigl(n+\ell(p-1)\bigr)^j c_{n+\ell(p-1)}.              \tag{5.1}
$$



Modulo $p$, the three nodes are



$$
n,\qquad n-1,\qquad n-2.                                \tag{5.2}
$$



The Lagrange polynomial which is one at $n$ and zero at the other nodes is



$$
L_0(X)={(X-n+1)(X-n+2)\over2}.                          \tag{5.3}
$$



Substituting (5.1) proves (1.9).

Set $E=p-r$.  The exact derivatives are



$$
\vartheta H=E(\vartheta G)G^{E-1},                       \tag{5.4}
$$



and



$$
\vartheta^2H
 =E(\vartheta^2G)G^{E-1}
  +E(E-1)(\vartheta G)^2G^{E-2}.                          \tag{5.5}
$$



Thus (1.9) is a fixed linear combination of four Kummer sums attached to



$$
\begin{array}{ll}
 R_0=x^{-n}G^E,
 &R_1=x^{-n}(\vartheta G)G^{E-1},\\
 R_{2a}=x^{-n}(\vartheta^2G)G^{E-1},
 &R_{2b}=x^{-n}(\vartheta G)^2G^{E-2}.                   \tag{5.6}
\end{array}
$$



The numbers of distinct zeros and poles, including infinity, are bounded by



$$
5,\qquad7,\qquad6,\qquad7,                               \tag{5.7}
$$



respectively.  Indeed,



$$
\vartheta G=uG'(u),\qquad
 \vartheta^2G=-4u(1-3u)^2,                               \tag{5.8}
$$



and $G$ has three distinct roots for every actual prime.  None of the
four functions is a $(p-1)$-st power: at a root of $G$, its nonzero
exponent is one of $E,E-1,E-2$, all strictly between $0$ and $p-1$.

Choose $\mathfrak p\mid p$ in $\mathbb Q(\zeta_{p-1})$.  Let
$[a]$ denote the Teichmüller lift of $a\in\mathbb F_p$, and put



$$
\mathcal K(R)=\sum_{x\in\mathbb F_p^\times}\omega(R(x)), \tag{5.9}
$$



with value zero at a zero of $R$.  One may take



$$
\begin{aligned}
 \mathcal T_{p,r,n}=-[1/2]\bigl(&[E]\mathcal K(R_{2a})
 +[E(E-1)]\mathcal K(R_{2b})\\
 &+[(3-2n)E]\mathcal K(R_1)
 +[(n-1)(n-2)]\mathcal K(R_0)\bigr).                    \tag{5.10}
\end{aligned}
$$



Reduction modulo $\mathfrak p$ gives (1.9).  The standard
multiplicative-character estimate and (5.7) give at most



$$
(5-1)+(7-1)+(6-1)+(7-1)=21                              \tag{5.11}
$$



square-root units.  Every Galois conjugate replaces the full Teichmüller
character by another full-order character, so the estimate holds for every
embedding.  This proves (1.10).

## 6. Why the Weil bound is not a $p$-adic unit theorem

The conductor in Section 5 is bounded, but the coefficient field is not:



$$
K_p=\mathbb Q(\zeta_{p-1}),\qquad
 [K_p:\mathbb Q]=\varphi(p-1).                            \tag{6.1}
$$



Because $p\equiv1\pmod{p-1}$, $p$ splits completely in $K_p$.
The actual coefficient chooses one prime above $p$.  If
$a_{r,n}=0\pmod p$, then



$$
\mathcal T_{p,r,n}\in\mathfrak p,                        \tag{6.2}
$$



so $p$ divides its rational norm.  But (1.10) yields only (1.11), an
upper bound much larger than $p$.  There is no contradiction.

This identifies the additional theorem a finite-field route must supply:

- a chosen-prime $p$-adic unit or nonconcentration statement;
- descent of $\mathcal T_{p,r,n}$ to a rational or uniformly
  bounded-degree field, followed by exact trace nonvanishing; or
- an actual-family relation controlling the two upper aliases before a
  base-field trace estimate is invoked.

Even rational descent would not suffice by itself.  For $p>21^2$, the
bound would reduce $p\mid\mathcal T$ to the exact equation
$\mathcal T=0$, but a separate nonzero or weighted trace-zero theorem
would remain necessary.

## 7. Capacity audit and scoped no-go

Unlike a fixed-target or bounded-gap construction, these identities hold on
every actual row.  They reach the full raw fixed-$j=1$ mass



$$
{M\over6}+o(M),                                          \tag{7.1}
$$



which is large enough to matter.  The failure is not thin support; it is
the absence of a $p$-adic conclusion.

The following method classes are now closed for this target.

1. **Plain base-field Fourier plus Weil.** It controls the three-alias sum,
   not the collision-forced coefficient.
2. **Extension-field isolation plus Weil.** It isolates the coefficient,
   but its square-root scale is already $p$.
3. **Finite Euler de-aliasing plus conjugate-size bounds alone.** It gives
   the exact lift (1.10), but the growing cyclotomic norm leaves
   $\mathfrak p$-divisibility possible.

This scoped no-go does not cover $p$-adic monodromy, unit roots,
chosen-prime equidistribution, descent, or average gcd.  Those are the live
global directions.

No actual zero row is excluded, so



$$
\text{proved excluded weighted mass}=0,\qquad
 \text{fixed-}j=1\text{ ceiling}={1\over36}.              \tag{7.2}
$$



## 8. Exact controls

The deterministic certificate uses only the five rows preselected in
Item 339 and performs no prime scan.

| $(h,s,p)$ | $(n,r)$ | three aliased coefficients | $(S_0,S_1,S_2)$ | recovered $c_n$ | $\mathbb F_{p^2}$ moment |
|---|---:|---|---|---:|---|
| $(1,1,13)$ | $(2,3)$ | $0,9,12$ | $5,4,4$ | $0$ | $0$ |
| $(2,1,17)$ | $(4,3)$ | $8,14,15$ | $14,15,9$ | $8$ | $-8$ |
| $(8,2,47)$ | $(16,5)$ | $0,22,33$ | $39,7,3$ | $0$ | $0$ |
| $(4,4,43)$ | $(8,9)$ | $2,2,1$ | $38,7,39$ | $2$ | $-2$ |
| $(2,6,47)$ | $(4,13)$ | $36,35,42$ | $28,43,22$ | $36$ | $-36$ |

The extension moments lie in the base-field component of the chosen
quadratic model and equal $-c_n$.  The two zero rows are selected-carrier
zeros only; no full ordinary collision is inferred.

## 9. Strict labels

### PROVED

- the positive-power Frobenius chart (1.4)--(1.5);
- the exact terminating ${}_4F_3$ representation (2.4);
- the exact three-alias theorem (1.6);
- exact coefficient isolation over $\mathbb F_{p^2}$, equation (1.7);
- exact three-Euler-moment de-aliasing, equation (1.9);
- the fixed-support Kummer lift and $21\sqrt p$ conjugate bound;
- the cyclotomic norm obstruction;
- the scoped Fourier/Weil no-go in Section 7.

### EXACT FINITE ONLY

- the five preselected $\mathbb F_p$ and $\mathbb F_{p^2}$ controls;
- no control is promoted to a density statement or a full collision.

### OPEN

- chosen-prime $p$-adic nonconcentration or a unit-root theorem;
- rational or bounded-degree descent and exact trace nonvanishing;
- an actual-family relation controlling the two upper aliases;
- average gcd or factor localization for Item 339's rational carrier;
- $W_b(M)=o(M)$ or any strict fixed-$j=1$ ceiling reduction;
- fixed-$j=1$ closure, Route 1, and every conclusion about $e+\pi$.

## 10. Ledger consequence



$$
\begin{array}{c|c}
\text{quantity}&\text{Item 342 value}\\ \hline
\text{actual rows reached by the exact transform}&\text{all}\\
\text{new independent condition}&0\\
\text{new proved excluded log mass}&0\\
\text{new fixed-}j=1\text{ capacity reduction}&0\\
\text{retained fixed-}j=1\text{ ceiling per }6M&1/36
\end{array}                                                \tag{10.1}
$$



Item 342 converts the target into a precise finite-field object and
identifies the missing theorem as $p$-adic rather than Archimedean.  It is
a global method-class closure, not a ledger gain.
