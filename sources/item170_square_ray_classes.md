> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 170 — complete valuation classification on the prime-square locus

Date: 2026-08-29

## 1. Scope and verdict

Put



$$
u=x(1-x),\qquad Q=(1+x)(1+x^2),\qquad
\omega_s=\frac{u^{6m}}{Q^{4m+1+s}}\,dx\quad(s=0,1),
$$



and write



$$
H_s=R_s+\frac{L_s}{4}\log 2+\frac{E_s}{8}\pi .
$$



As in items 163--167, define



$$
\mathscr A=L_1(pR_0)-L_0(pR_1)=pA_m,\qquad
\mathscr B=L_1E_0-L_0E_1=8B_m.                    \tag{1.1}
$$



This note classifies the complete prime-square locus



$$
\boxed{10m+1=p^2}.                                    \tag{1.2}
$$



For a prime $p$, integrality in (1.2) is equivalent to
$p\equiv1,9,11,19\pmod {20}$; in particular it excludes $p=2,5$ and
the other odd residue classes.  The exact all-prime result is



$$
\boxed{
\begin{array}{c|c|c|c|c|c}
p\bmod20&\text{item-168 cell}&
\dim_{\mathbb F_p}\langle\mathcal C\omega_0,\mathcal C\omega_1\rangle&
v_p(\mathscr A)\text{ proved}&v_p(\mathscr B)&v_p(c_m)\\ \hline
1&\kappa=0&2&\ge1&0&1\\
9&\kappa=1&1&\ge2&1&2\\
11&\kappa=0&1&\ge2&1&2\\
19&\kappa=1&0&\ge3&2&3
\end{array}}.                                           \tag{1.3}
$$



Here “rank” means the actual dimension of the span of the two first
Cartier images.  It is not the item-168 degree-cell label.  In particular,
both $p\equiv1,11\pmod {20}$ lie in the maximum-rank-two cell
$\kappa=0$, but its exact coefficient determinant is nonzero in the first
class and zero, of actual rank one, in the second.

**PROVED — unique cubic class.**  Item 167 gives exact valuation three in
the $19\pmod {20}$ class.  The nonzero digits below prove exact valuations
one or two in the other classes.  Therefore



$$
p\equiv19\pmod {20}
\quad\Longleftrightarrow\quad
v_p\!\left(c_{(p^2-1)/10}\right)=3,
\qquad p\text{ prime and }10\mid p^2-1.                \tag{1.4}
$$



There are no small-prime exceptions.  The first admissible primes in the
four columns are $41,29,11,19$, and the formulas include $p=11,19$.

**PROVED — zero rate.**  At fixed $m$, equation (1.2) supplies at most
one prime, and



$$
\log p=\frac12\log(10m+1)=O(\log m)=o(m).               \tag{1.5}
$$



Even three copies contribute only $O(\log m)$.  This classification does
not improve the Route-1 exponential content constant.

**EXPERIMENTAL FINITE.**  The deterministic certificate checks every
symbolic formula for admissible primes through $p\le2000$ and independently
computes the Hasse-coordinate determinants through $p\le200$.  These rows
audit the theorem; they are not its proof.

**OPEN.**  No positive-mass deeper layer or conclusion about $e+\pi$
follows.  In contrast, the exact table proves that no fourth content layer
occurs anywhere on this prime-square locus.

## 2. Parameters, normalization, and the item-168 cells

On (1.2),



$$
N=6m=\frac{3(p^2-1)}5,\qquad
K_0=4m+1=\frac{2p^2+3}{5},\qquad
K_1=K_0+1.                                             \tag{2.1}
$$



Thus



$$
p\le K_0<p^2,                                          \tag{2.2}
$$



so the frozen top denominator power is $q_p=p$, or $e_p=1$.  Also
$p<2m$ for every admissible prime.

Write



$$
N=ap+r,\qquad K_0=bp+t,\qquad c=b+1.                  \tag{2.3}
$$



If $p=5q+1$, then



$$
(a,b,r,t,c)=(3q,2q,3q,2q+1,2q+1),\qquad
\kappa=2a-3b=0.                                        \tag{2.4}
$$



This is the item-168 $\kappa=0$ cell, with both cell parameters equal to
$q$.  If $p=5q-1$, then



$$
(a,b,r,t,c)=(3q-1,2q-1,2q-1,3q,2q),\qquad
\kappa=1.                                               \tag{2.5}
$$



Hence the classes $1,11\pmod {20}$ lie in $\kappa=0$, while
$9,19\pmod {20}$ lie in $\kappa=1$.

Put



$$
\mathfrak D=uQ=x(1-x^4).                                \tag{2.6}
$$



In every class,



$$
P_0=\mathfrak D^r,\qquad
P_1=u\mathfrak D^{r-1}
=x^r(1-x)(1-x^4)^{r-1},\qquad
\omega_s=F^pP_s\,dx,\quad F=\frac{u^a}{Q^c}.            \tag{2.7}
$$



For $p=5q-1$, the degrees of $P_0,P_1$ are $2p-3,2p-6$;
for $p=5q+1$, they are $3p-3,3p-6$.  All exceed $p-2$, so
the square-ray prime is never in the already removed rank-zero product
$\mathcal P_m$.  Since $p<2m$, it is not in the removed middle product.
The frozen normalization therefore gives



$$
\boxed{
v_p(U_m)=v_p(\mathscr A),\qquad
v_p(V_m)=1+v_p(\mathscr B),\qquad
v_p(c_m)=\min\{v_p(\mathscr A),1+v_p(\mathscr B)\}.}    \tag{2.8}
$$



This ledger applies whether or not the first Cartier determinant vanishes.

## 3. First Cartier ranks

For a polynomial $P$, record the two possible resonances as



$$
\Gamma(P)=([x^{p-1}]P,[x^{2p-1}]P).                    \tag{3.1}
$$



Every displayed binomial coefficient below has upper argument less than
$p$, so it is a unit modulo $p$.

If $p=20k+1$, then $r=12k$ and



$$
\begin{aligned}
\Gamma(P_0)&=(g_0,0),
&g_0&=(-1)^{2k}{12k\choose2k},\\
\Gamma(P_1)&=(g_1,d_1),
&d_1&=(-1)^{7k+1}{12k-1\choose7k}\ne0.
\end{aligned}                                           \tag{3.2}
$$



Thus the coefficient determinant $g_0d_1$ is nonzero and the actual rank
is two.

If $p=20k+11$, then $r=12k+6$ and



$$
\Gamma(P_0)=(g,0),\qquad
\Gamma(P_1)=\left(\frac{5g}{6},0\right),\qquad
g=(-1)^{2k+1}{12k+6\choose2k+1}\ne0.                  \tag{3.3}
$$



This remains a $\kappa=0$ row, but its actual rank is one.

If $p=20k+9$, then $r=8k+3$ and



$$
\Gamma(P_0)=(0,0),\qquad
\Gamma(P_1)=(\varepsilon,0),\qquad
\varepsilon=(-1)^{3k+2}{8k+2\choose3k+1}\ne0.         \tag{3.4}
$$



The actual rank is one.  Finally, for $p=20k+19$,



$$
\Gamma(P_0)=\Gamma(P_1)=(0,0),                         \tag{3.5}
$$



so the actual rank is zero.  This proves the rank column in (1.3) and
reconciles it explicitly with item 168.

## 4. Relative endpoint lemma

The extra valuations of $\mathscr A$ use a relative endpoint identity.
Let



$$
\vartheta=\frac{dx}{1+x^2}.                              \tag{4.1}
$$



Suppose a proper rational differential $W$ over $\mathbb F_p$ has poles
only at the roots of $Q$, of order $K<p$, satisfies
$W=O(x^{-2})dx$, and has the form



$$
W=\frac{P(x)}{Q(x)^p}\,dx,\qquad \deg P\le3p-2.         \tag{4.2}
$$



If $\mathcal C(W)=0$, the coefficients of $P$ at $p-1,2p-1$ vanish.
The zero-constant primitive



$$
T(x)=\sum_e\frac{[x^e]P}{e+1}x^{e+1}                  \tag{4.3}
$$



is therefore well-defined in $\mathbb F_p[x]$ and
$W=d(T/Q^p)$.  The unique proper primitive normalized at infinity is
$A/Q^{K-1}$ with $\deg A<3(K-1)$.  The difference of the two primitives
has zero derivative, so perfection of $\mathbb F_p$ gives



$$
T=AQ^{p-K+1}+J(x)^p,\qquad \deg J\le2.                 \tag{4.4}
$$



For $T=\sum t_ex^e$, put



$$
S_j=\sum_{e\equiv j\ (4)}t_e.                          \tag{4.5}
$$



Quadratic interpolation at $-1,i,-i$ gives



$$
\begin{array}{c|c|c}
p\bmod4&J(0)&T(1)-J(1)\\ \hline
1&S_0-S_3&4S_3\\
3&S_0-S_1&4S_1.
\end{array}                                             \tag{4.6}
$$



Because $T(0)=0$, equation (4.4) says $A(0)=-J(0)$, while evaluation at
$1$ gives $4^{p-K+1}A(1)=T(1)-J(1)$.  Therefore



$$
\begin{array}{ll}
p\equiv1\pmod4:&S_0=S_3=0\Longrightarrow[A/Q^{K-1}]_0^1=0,\\
p\equiv3\pmod4:&S_0=S_1=0\Longrightarrow[A/Q^{K-1}]_0^1=0.
\end{array}                                             \tag{4.7}
$$



The four balanced differentials below have these primitive-section
supports:



$$
\begin{array}{c|c|c|c}
p\bmod20&\text{balanced }W&
\text{non-}\vartheta\text{ sections}&\text{required sections}\\ \hline
1&dF+g(xF)-gd\vartheta&\{1,2\}&\{0,3\}\\
9&dF+gX-gd\vartheta&\{1,2\}&\{0,3\}\\
11&g\Phi-(a_0-b)F+gb\vartheta&\{2,3\}&\{0,1\}\\
19&\delta G+\gamma X+\gamma\delta\vartheta&\{2,3\}&\{0,1\}.
\end{array}                                             \tag{4.8}
$$



To handle the remaining sections, use



$$
(1+x)^p(1+x^2)^{p-1}
=(1+x^p)\sum_{j=0}^{p-1}(-1)^jx^{2j}.                 \tag{4.9}
$$



For $p\equiv1\pmod4$, both required sums contributed by $\vartheta$ are,
up to a common scalar,



$$
\sum_{r=0}^{(p-3)/2}\frac1{4r+3}=0.                    \tag{4.10}
$$



The involution $r\mapsto(p-3)/2-r$ pairs every denominator with its
negative and has no fixed point.  For $p\equiv3\pmod4$, the corresponding
identity is



$$
\sum_{r=0}^{(p-1)/2}\frac1{4r+1}=0,                    \tag{4.11}
$$



under $r\mapsto(p-1)/2-r$.  Thus every row in (4.8) satisfies



$$
\boxed{R(W)=0}.                                         \tag{4.12}
$$



This argument retains the relative endpoint; absolute exactness alone
would not suffice.

## 5. Exact leading digits in the four classes

### 5.1 The class $p\equiv1\pmod {20}$

Let $p=20k+1$, $a=12k$, and $c=8k+1$.  Since $a+c=p$,



$$
F=\frac{\mathfrak D^a}{Q^p},\qquad
xF=\frac{x\mathfrak D^a}{Q^p}.
$$



Put



$$
g=(-1)^{2k}{a\choose2k},\qquad
d=(-1)^{7k}{a\choose7k}.                              \tag{5.1}
$$



Then



$$
\mathcal C(F\,dx)=g\frac{dx}{Q},\qquad
\mathcal C(xF\,dx)=d\frac{x\,dx}{Q}.                   \tag{5.2}
$$



Cartier fixes $\vartheta$ in this class, so the first balanced row in
(4.8) has zero Cartier image.  Equation (4.12) gives
$dR(F)+gR(xF)=0$.  Since the logarithmic coordinates in (5.2) are
$g,-d$, this is exactly the required $R,L$ determinant identity.  The
top relative-Cartier formula and (3.2) give



$$
v_p(\mathscr A)\ge1.                                    \tag{5.3}
$$



Using



$$
(L,E)(dx/Q)=(1,1),\qquad (L,E)(x\,dx/Q)=(-1,1),
$$



the exact leading period digit is



$$
\boxed{\mathscr B\equiv-2g_0d_1gd\not\equiv0\pmod p.}   \tag{5.4}
$$



Equations (2.8), (5.3), and (5.4) prove $v_p(c_m)=1$.

### 5.2 The class $p\equiv9\pmod {20}$

Let



$$
p=20k+9,\quad r=8k+3,\quad a=12k+5,\quad c=8k+4,\quad n=a-1.
$$



Since $\mathcal C(P_0dx)=0$, let $T_0'=P_0$ be the zero-constant
primitive.  Exact integration by parts gives



$$
\omega_0=d(F^pT_0)-p\Psi_0,\qquad
\Psi_0=F^{p-1}F'T_0\,dx.                              \tag{5.5}
$$



Its next Cartier image is



$$
\mathcal C(\Psi_0)=hX,\qquad
X=\frac{u^nx^4}{Q^{c+1}}\,dx,                          \tag{5.6}
$$



where



$$
I=\frac14\frac{(2k)!(8k+3)!}{(10k+4)!},\qquad
h=-4aI\ne0\pmod p.                                     \tag{5.7}
$$



The factorial formula is the beta integral
$T_0(1)=\int_0^1x^r(1-x^4)^r\,dx$.

Put



$$
\gamma=(-1)^{7k+3}{a\choose7k+3},\qquad
\delta=(-1)^{2k}{n\choose2k}.                           \tag{5.8}
$$



Then



$$
\mathcal C(F\,dx)=\gamma\frac{x\,dx}{Q},\qquad
\mathcal C(X)=\delta\frac{dx}{Q}.                       \tag{5.9}
$$



The second balanced row in (4.8) supplies the relative endpoint identity
in the divided form of (5.5), proving



$$
v_p(\mathscr A)\ge2.                                    \tag{5.10}
$$



With $\varepsilon$ from (3.4), the exact first nonzero period digit is



$$
\boxed{\frac{\mathscr B}{p}
\equiv2\varepsilon h\gamma\delta\not\equiv0\pmod p.}    \tag{5.11}
$$



Every factor is a displayed binomial or factorial unit.  Hence
$v_p(\mathscr B)=1$, and (2.8) gives $v_p(c_m)=2$.

### 5.3 The class $p\equiv11\pmod {20}$

Put



$$
p=20k+11,\qquad a=r=12k+6,\qquad c=8k+5,\qquad n=a-1.
$$



The scalar-free Bockstein uses



$$
\Theta=\frac{5g}{6}P_0-gP_1,\qquad T'=\Theta,
$$



and gives



$$
\frac{5g}{6}\omega_0-g\omega_1=d(F^pT)-p\Psi,\qquad
\mathcal C(\Psi)=\Phi=\frac{u^nH}{Q^{c+1}}\,dx.         \tag{5.12}
$$



Four-section support has



$$
H=h_1x+h_4x^4+h_5x^5.                                  \tag{5.13}
$$



Only $h_4$ is needed.  The $3\pmod4$ section of $\Theta$ gives



$$
I=\frac14\frac{(3k+1)!(12k+5)!}{(15k+7)!},\qquad
h_4=-4agI\ne0\pmod p.                                  \tag{5.14}
$$



Write



$$
\mathcal C(\Phi)=\frac{a_0+bx}{Q}\,dx,\qquad
b=h_4(-1)^{7k+3}{n\choose7k+3}\ne0.                    \tag{5.15}
$$



Also $\mathcal C(F\,dx)=g\,dx/Q$.  Since
$\mathcal C(\vartheta)=-\vartheta$, the third balanced row in (4.8)
gives the divided $R,L$ determinant identity in (5.12).  Therefore



$$
v_p(\mathscr A)\ge2.                                    \tag{5.16}
$$



Frobenius fixes $L$ and negates $E$ in this class.  The exact leading
period digit is



$$
\boxed{\frac{\mathscr B}{p}\equiv-2gb\not\equiv0\pmod p.} \tag{5.17}
$$



Thus $v_p(\mathscr B)=1$ and $v_p(c_m)=2$.  Formula (5.14) is valid at
$k=0,p=11$, so there is no exception.

### 5.4 The class $p\equiv19\pmod {20}$

This is item 167.  Put



$$
a=12k+11,\quad n=a-1=12k+10,\quad K=8k+9,\quad \rho=8k+7.
$$



The first Bockstein images are



$$
\Phi_0=hX,\qquad \Phi_1=\lambda G+\mu X,\qquad
G=\frac{u^nx^3}{Q^K}\,dx,\quad X=xG.                  \tag{5.18}
$$



Here



$$
h=-4a\left\{\frac14\frac{(2k+1)!(8k+7)!}{(10k+9)!}\right\}, \tag{5.19}
$$



and, with $(z)_\rho=z(z+1)\cdots(z+\rho-1)$,



$$
S=-\frac14\frac{(\rho-1)!}{((\rho+2)/4)_\rho},\qquad
\lambda=-4aS.                                           \tag{5.20}
$$



Finally,



$$
\gamma=(-1)^{7k+6}{n\choose7k+6},\qquad
\delta=(-1)^{2k+1}{n\choose2k+1}.                       \tag{5.21}
$$



All factors are units.  Item 167 proves the last balanced endpoint row in
(4.8) and obtains



$$
v_p(\mathscr A)\ge3,\qquad
\boxed{\frac{\mathscr B}{p^2}
\equiv-2h\lambda\gamma\delta\not\equiv0\pmod p.}        \tag{5.22}
$$



Thus $v_p(\mathscr B)=2$ and $v_p(c_m)=3$, including $k=0,p=19$.

## 6. Thinness and deterministic replay

Dirichlet's theorem gives infinitely many primes in each class, but



$$
m=\frac{p^2-1}{10}.                                     \tag{6.1}
$$



For fixed $m$ there is at most one positive square-ray prime.  Booking its
exact multiplicity from (1.3) contributes at most
$3\log p=O(\log m)=o(m)$.

The deterministic checker is

    scripts/item170_square_ray_certificate.py

It reconstructs the four resonant-vector patterns, verifies every
factorial/binomial digit in (5.4), (5.11), (5.17), and (5.22), constructs
each balanced numerator, checks both zero resonances and all pole/degree
hypotheses in Section 4, and verifies the paired reciprocal cancellation.
It reuses the pinned item-167 checker for the $19\pmod {20}$ row.  Through
$p\le200$, it independently computes $(pR_s,L_s,E_s)\bmod p^4$ by the
Hasse recurrence and compares the exact valuations and leading digits.

Two canonical runs are byte-identical.  The companion SHA-256 manifest
pins the report, checker, both JSON outputs, and the item-164/item-167
dependencies.

## 7. Status ledger

### PROVED

- The complete all-prime table (1.3), with no small-prime exceptions.
- Exact reconciliation with the item-168 $\kappa=0,1$ terminology.
- The balanced relative endpoint identities forcing the stated
  $\mathscr A$-valuations.
- The nonzero leading $\mathscr B$-digits proving all upper valuations.
- Uniqueness of $p\equiv19\pmod {20}$ as the cubic square-ray class.
- The $O(\log m)=o(m)$ mass of the entire square locus.

### EXPERIMENTAL FINITE

- All admissible primes through $p\le2000$ pass the symbolic certificate.
- All admissible primes through $p\le200$ pass an independent
  Hasse-coordinate calculation modulo $p^4$.

### OPEN

- Any positive-mass deeper layer outside a thin polynomial-divisor locus.
- Any positive-mass fourth or fifth layer outside this thin square locus.
- Any improvement of the proved Route-1 exponential content constant.
- Any conclusion about $e+\pi$.
