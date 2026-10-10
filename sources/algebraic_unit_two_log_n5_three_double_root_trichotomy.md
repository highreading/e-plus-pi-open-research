> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A prescribed-double-root trichotomy for every $n=5$ common-zero branch

Checked: 2026-08-27 UTC

## Verdict

After reduction to a base degree $d<p$, all three common-zero branches in
the general-prime ideal criterion are prescribed-double-root problems.
The simultaneous $P_d(\eta),P_d(\bar\eta)$ branch and the
$P_d(1),P_d(\eta)$ branch are two specializations of one finite-field
differential identity for a complementary weighted-factorial polynomial.
The $P_d(\eta),C_d(\eta)$ branch is the already identified double root at
$\lambda=0$ of a monic parameter polynomial.

This unifies the form of the obstruction, but it does not supply a shared
discriminant whose prime support is fixed.  In particular, an ordinary
discriminant records multiple roots at every point, while each branch below
requires a multiple root at one prescribed algebraic unit or parameter.

## 1. Base-degree and complementary notation

Let $p\ne5$ be an odd rational prime.  For an arbitrary original degree
$n$, first put



$$
d=n\bmod p,\qquad 0\le d<p.
\tag{1}
$$



The exact block congruences for $P_n,C_n,a_n$ reduce every common-zero
branch at degree $n$ to the corresponding branch at degree $d$.  Thus
$d!$ is a unit in all statements below.

Put



$$
\zeta=\zeta _5,\quad x=\eta=(1+\zeta)^{-1},\quad
 y=\bar\eta=1-x,\quad
 u=x^{-1}=1+\zeta,\quad v=y^{-1}=1+\zeta^{-1}.
\tag{2}
$$



Let



$$
m=p-1-d,\qquad
 W_m(Z)=\sum_{j=0}^{d}(m+j)!Z^j\in\mathbb F_p[Z].
\tag{3}
$$



For every algebraic unit $r$, the reversal of the falling factorials gives



$$
\boxed{
 P_d(r^{-1})=\frac{r^{-d}}{m!}W_m(r)\pmod p.}
\tag{4}
$$



In particular, the choices $r=1,u,v$ represent $P_d(1),P_d(x),P_d(y)$,
respectively, up to the displayed unit factors.

The polynomial $W_m$ satisfies



$$
Z^2W_m'(Z)+\{(m+1)Z-1\}W_m(Z)=-m!\pmod p.
\tag{5}
$$



## 2. One two-point differential identity

Let $c,r$ be algebraic units in the relevant localization, and suppose
$c^{-1}-1$ is also a unit.  Define



$$
H_{m,c}(Z)=W_m(cZ)-c^{-1}W_m(Z).
\tag{6}
$$



Apply (5) at $cZ$, multiply by the chain-rule factor, and subtract
$c^{-1}$ times (5) at $Z$.  The two constant terms cancel and give the
polynomial identity



$$
\boxed{
 Z^2H_{m,c}'(Z)
 =c^{-1}\{1-(m+1)cZ\}H_{m,c}(Z)
  +c^{-1}(c^{-1}-1)W_m(Z).}
\tag{7}
$$



At the prescribed point $r$,



$$
H_{m,c}(r)=W_m(cr)-c^{-1}W_m(r),
\tag{8}
$$



whereas (7) gives the reverse recovery formula



$$
(c^{-1}-1)W_m(r)
 =cr^2H_{m,c}'(r)-\{1-(m+1)cr\}H_{m,c}(r).
\tag{9}
$$



Equations (8)--(9), and the unit hypotheses, prove the localized ideal
identity



$$
\boxed{
 (W_m(r),W_m(cr))
 =(H_{m,c}(r),H_{m,c}'(r)).}
\tag{10}
$$



Thus two weighted values vanish simultaneously if and only if the prescribed
point $r$ is a multiple root of $H_{m,c}$.  This is an exact identity,
not a finite-scan inference.

## 3. The two $Z$-double-root branches

For the simultaneous $P$-value branch, take



$$
r=u,\qquad c=\zeta^{-1}.
\tag{11}
$$



Then $cr=v$, and $c^{-1}-1=\zeta-1$, which is a unit away from $5$.
Equations (4) and (10) give



$$
\boxed{
 (P_d(x),P_d(y))
 =(H_{m,\zeta^{-1}}(u),H_{m,\zeta^{-1}}'(u))}
\tag{12}
$$



up to multiplication of the displayed generators by local units.  The
coefficient of $Z^j$ in this $H$-polynomial is



$$
(m+j)!(\zeta^{-j}-\zeta),
$$



so all coefficients with $j\equiv4\pmod5$ vanish.

For the $a_d=P_d(1)$ and $P_d(x)$ branch, take



$$
r=1,\qquad c=u.
\tag{13}
$$



Here $cr=u$ and



$$
c^{-1}-1=x-1=-y
$$



is a global unit.  If



$$
G_m(Z)=W_m(uZ)-u^{-1}W_m(Z),
\tag{14}
$$



then (4) and (10) give



$$
\boxed{
 (P_d(1),P_d(x))=(G_m(1),G_m'(1))}
\tag{15}
$$



again up to local units.  Unlike (12), this branch has no fixed
residue-class lacuna, because $u$ is not a root of unity in characteristic
zero.  The conjugate $P_d(1),P_d(y)$ branch is obtained by replacing
$u,x$ with $v,y$.

## 4. The parameter-double-root branch

Define



$$
\mathcal F_d(\lambda,u)
 =d![z^d]\frac{e^z(1+z)^\lambda}{1+uz}.
\tag{16}
$$



It is a monic degree-$d$ polynomial in $\lambda$.  Direct substitution
in the exponential generating functions gives



$$
\mathcal F_d(0,u)=u^dP_d(x),\qquad
 \partial_\lambda\mathcal F_d(0,u)=u^dC_d(x).
\tag{17}
$$



Consequently



$$
\boxed{
 (P_d(x),C_d(x))
 =(\mathcal F_d(0,u),\partial_\lambda\mathcal F_d(0,u))}
\tag{18}
$$



up to the common unit $u^d$, and this branch is exactly the assertion that
$\lambda=0$ is a multiple root of $\mathcal F_d(\lambda,u)$.  The
conjugate branch uses $\mathcal F_d(\lambda,v)$.

## 5. Clean form of the trichotomy

Let



$$
N_d=P_d(x)P_d(y),\qquad
 D_d=P_d(x)C_d(y)-P_d(y)C_d(x),\qquad
 T_d=\frac{D_d}{\zeta-\zeta^{-1}},
$$



and



$$
\mathfrak J_d=(N_d,a_dT_d).
\tag{19}
$$



If a prime above $p$ divides $\mathfrak J_d$, extend it to the
cyclotomic field and, after applying conjugation if necessary, assume
$P_d(x)=0$.  Exactly one or more of the following prescribed-double-root
conditions then holds:



$$
\begin{array}{lll}
P_d(y)=0
 &\Longleftrightarrow&
 u\text{ is a multiple root of }H_{m,\zeta^{-1}},\\[2pt]
a_d=P_d(1)=0
 &\Longleftrightarrow&
 1\text{ is a multiple root of }G_m,\\[2pt]
C_d(x)=0
 &\Longleftrightarrow&
 0\text{ is a multiple root of }\mathcal F_d(\lambda,u).
\end{array}
\tag{20}
$$



The alternatives are exhaustive because, once $P_d(x)=0$, the condition
$N_d=a_dT_d=0$ says either $P_d(y)=0$, or $a_d=0$, or
$D_d=0$; in the last case $D_d=-P_d(y)C_d(x)$, so either the first
branch already holds or $C_d(x)=0$.

## 6. Why the shared form does not yet close the prime classification

The first two polynomials satisfy the shared differential identity (7), but
their scaling constants have different arithmetic: $\zeta^{-1}$ has
order five, whereas $u$ is a non-torsion unit.  The third double root lies
in the parameter $\lambda$, not the evaluation variable $Z$, and
$\mathcal F_d$ does not satisfy (7).

Taking a full discriminant in any branch loses the prescribed-point
condition.  It introduces primes arising from unrelated multiple roots, just
as the quadratic resultant in the weighted-pair problem can vanish when only
one of its two values vanishes.  Therefore (20) is a uniform compression of
the obstruction, not a proof that its support is confined to $19$.

## 7. The shared first-jet/subresultant invariant

There is one exact invariant common to all three rows of (20).  Let $f$ be
any of their three polynomials and let $s$ be its prescribed point.  Taylor
division by the monic square gives, over any coefficient ring,



$$
f(X)\equiv f(s)+f'(s)(X-s)\pmod{(X-s)^2}.
\tag{21}
$$



Thus



$$
\mathcal I_s(f)=(f(s),f'(s))
\tag{22}
$$



is precisely the coefficient ideal of the first remainder, or prescribed
first jet.  It vanishes after reduction exactly when $s$ is a multiple
root.  The ordinary resultant with the square remembers only the value:



$$
\operatorname {Res}_X((X-s)^2,f)=f(s)^2.
\tag{23}
$$



Nevertheless, adjoining the derivative recovers the exact prime support.
Indeed, if



$$
\mathcal K_s(f)=(f'(s),\operatorname {Res}_X((X-s)^2,f)),
$$



then



$$
\boxed{
 \mathcal I_s(f)^2\subseteq\mathcal K_s(f)\subseteq\mathcal I_s(f),
 \qquad
 \sqrt{\mathcal K_s(f)}=\sqrt{\mathcal I_s(f)}.}
\tag{24}
$$



This applies with



$$
(f,s)=
 (H_{m,\zeta^{-1}},u),\qquad
 (G_m,1),\qquad
 (\mathcal F_d(\lambda,u),0),
$$



and likewise to the conjugate branches.  It is the precise shared
subresultant compression sought here.  A full discriminant
$\operatorname {Res}(f,f')$ is only a necessary condition: it also
vanishes when $f$ has an unrelated multiple root away from $s$.

There are small exact false positives in all three branches.  For the first
two, take $p=31,d=18,m=12,\zeta=16$, so $u=17$.  Exact Euclidean
calculation in $\mathbb F_{31}[Z]$ gives



$$
\begin{aligned}
 \gcd(H_{12,\zeta^{-1}},H_{12,\zeta^{-1}}')&=Z-8,
 &\bigl(H_{12,\zeta^{-1}}(17),
        H_{12,\zeta^{-1}}'(17)\bigr)&=(26,19),\\
 \gcd(G_{12},G_{12}')&=Z-8,
 &\bigl(G_{12}(1),G_{12}'(1)\bigr)&=(1,1).
\end{aligned}
\tag{25}
$$



Thus both full discriminants vanish, but neither prescribed first jet does.
For the parameter branch, take $p=11,d=4,\zeta=4,u=5$.  Then



$$
\mathcal F_4(\lambda,5)
 =\lambda^4-3\lambda^2-\lambda+5,\qquad
 \gcd(\mathcal F_4,\partial_\lambda\mathcal F_4)=\lambda-4,
\tag{26}
$$



while



$$
\bigl(\mathcal F_4(0,5),\partial_\lambda\mathcal F_4(0,5)\bigr)
 =(5,10)\ne(0,0).
\tag{27}
$$



These are rigorous counterexamples to replacing the prescribed first-jet
ideal by a full discriminant in any row of (20).

The companion script checks (4)--(18) in exact arithmetic over stated finite
ranges and reproduces (25)--(27).  Those finite checks are diagnostic only.
Nothing here proves either algebraicity or transcendence of $e+\pi$.
