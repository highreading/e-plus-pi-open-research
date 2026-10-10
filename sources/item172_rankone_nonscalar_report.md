> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 172 — scalar-free cubic digits on the positive-mass $\kappa=1$ cell

Date: 2026-08-29

## 1. Scope and verdict

This item attacks the remaining non-scalar system on the forced rank-one
$e=1$ cell from Item 168.  The floor coordinates are denoted $(j,s)$;
the subscript $\nu\in\{0,1\}$ labels the two mixed-cubic differentials and
must not be confused with the floor coordinate $s$.

The conclusions are deliberately scoped.

**PROVED — exact scalar-free lifted digits.**  The complete Hasse coordinates
modulo $p^3$, followed by an elementary convolution-and-carry recurrence,
give $A_0,A_1,B_0$ without dividing by either Cartier scalar.  On this cell



$$
\boxed{p^3\mid c_m\iff A_0=A_1=B_0=0.}       \tag{1.1}
$$



Section 3 gives the digit formulas explicitly.

**PROVED — five-divisor formula for the first two gates.**  On the
integrality-safe range $p\ge2j+3$, which contains every sufficiently large
prime in a fixed band, the first Bockstein reduces both $A_0$ and $B_0$ to
two fixed-$j$ Frobenius-semilinear forms in



$$
\bar T(0),\bar T(1),\bar T(-1),\bar T(i),\bar T(-i),  \tag{1.2}
$$



where the exact lift $\widetilde T$ and its reduction $\bar T$ are defined
in Section 4.  This is scalar-free and uses the Cartier coefficients only
by multiplication.  The next digit $A_1$ still needs
the genuine modulo-$p^3$ Hasse lift; no five-value formula for it is proved.

**PROVED — the scalar reductions do not determine $A_0$.**  The two exact rows



$$
(m,p,j,s)=(99,107,1,15),\qquad(206,107,3,15)              \tag{1.3}
$$



have the same nonzero reduced Cartier-scalar pair



$$
(\bar\gamma _0,\bar\gamma _1)=(2,75)
              \quad\text{in }\mathbb F_{107},               \tag{1.4}
$$



but their first lifted digits are respectively $0$ and $65$ modulo $107$.
Thus $A_0$ is not a function of $(p,s)$ or of the two reduced Cartier
scalars.  This
is a rigorous finite counterexample to scalar determination, not a density
inference.

**PROVED — fixed-polynomial/fixed-affine loci are thin.**  Fix a band $j$.
If a proposed zero family is contained in finitely many congruences



$$
F_{j,k}(s)\equiv0\pmod p            \tag{1.5}
$$



for fixed nonzero polynomials $F_{j,k}\in\mathbb Z[Y]$, then its log-prime
weight is $O_j(\log m)$.  If (1.5) holds band by band for every fixed $j$,
the whole resulting family has weight $o(m)$; an elementary Chebyshev tail
bound makes this conclusion uniform.  In particular every fixed affine ray
$p=As+B$ satisfies



$$
p\mid 2Am+A-B,                    \tag{1.6}
$$



and is thin.  Precise hypotheses and constants appear in Section 6.

**EXPERIMENTAL finite census.**  Among the 2,649 frozen $\kappa=1$ rows
through $m\le250$, 119 have $A_0=0$.  Only 15 of those come from simultaneous
reduced-scalar zero; 104 are genuinely non-scalar.  Ten rows pass the cubic gate,
eight of them non-scalar.  Every one of these numbers is finite-only.  In
particular, the eight non-scalar survivors are not a positive-density
family.

**OPEN.**  The actual Hasse/Bockstein zero set is not proved to satisfy
(1.5).  Arbitrary non-scalar cancellations depending jointly on $(j,s,p)$
remain capable, in principle, of positive weighted mass.  No new uniform
content exponent and no conclusion about $e+\pi$ is claimed.

## 2. The complete $\kappa=1$ cell

Put



$$
u=x(1-x),\qquad Q=(1+x)(1+x^2),\qquad
 \omega_\nu={u^{6m}\over Q^{4m+1+\nu}}\,dx.               \tag{2.1}
$$



For an odd prime in the standing Route-1 range



$$
p<2m,\qquad p\le4m+1<p^2,                 \tag{2.2}
$$



write $6m=ap+r$ and $4m+1=bp+t$.  On $\kappa=2a-3b=1$ there
are unique integers $j\ge1$ and $s$ such that



$$
(a,b)=(3j+2,2j+1),\qquad
 r=p-3s-3,\qquad t=p-2s-1,                                \tag{2.3}
$$





$$
2m+1=(j+1)p-s,\qquad
 0\le s\le{p-3\over3},\qquad s\equiv j\pmod2.             \tag{2.4}
$$



Conversely (2.4), together with (2.2), reconstructs the cell.  The
prime-number-theorem interval is



$$
{2\over j+1}<{p\over m}<{6\over3j+2}.     \tag{2.5}
$$



Its exact width is



$$
w_j={6\over3j+2}-{2\over j+1}
     ={2\over(3j+2)(j+1)}.                                 \tag{2.6}
$$



Thus



$$
\sum_{j>J}w_j
 <\sum_{j>J}{2\over3j(j+1)}
 ={2\over3(J+1)}.                                         \tag{2.7}
$$



The total cell constant is



$$
C_1=\sum_{j\ge1}w_j
 =-1-{\pi\over\sqrt3}+3\log3
 =0.4820375017701113\ldots .                              \tag{2.8}
$$



Set



$$
F_j={u^{3j+2}\over Q^{2j+2}},\qquad
 P_0=u^{p-3s-3}Q^{2s+1},\qquad
 P_1=u^{p-3s-3}Q^{2s}.                                    \tag{2.9}
$$



Then exactly



$$
\omega_\nu=F_j^pP_\nu\,dx,         \tag{2.10}
$$



and



$$
\deg P_0=2p-3,\qquad
                         \deg P_1=2p-6.                    \tag{2.11}
$$



There is one Cartier resonance in each row.  Distinguish the exact integer
coefficients from their Cartier reductions:



$$
\widetilde\gamma_\nu=[x^{p-1}]P_\nu\in\mathbb Z,
 \qquad
 \bar\gamma_\nu=\widetilde\gamma_\nu\bmod p.              \tag{2.12}
$$



Writing $r=p-3s-3$ and $h=2s+1$, the finite four-section formulas are



$$
\begin{aligned}
 \widetilde\gamma_0&=[x^{3s+2}](1-x)^{r-h}(1-x^4)^h,\\
 \widetilde\gamma_1&=[x^{3s+2}](1-x)^{r-h+1}(1-x^4)^{h-1}.
\end{aligned}                                             \tag{2.13}
$$



Generalized binomial coefficients make (2.13) valid even when $r-h<0$;
the target degree is below $p$, so all recurrence denominators are units.
The exact coefficients, and hence their reductions, depend on $(p,s)$ and
do not depend on $j$.  The deterministic tables store the reduced pair
$(\bar\gamma_0,\bar\gamma_1)$.

## 3. Scalar-free Hasse digits and carries

Let



$$
X_\nu=pR_\nu,qquad
 \mathscr A=L_1X_0-L_0X_1,qquad
 \mathscr B=L_1E_0-L_0E_1.                               \tag{3.1}
$$



The Hasse coefficients at $\alpha\in\{-1,i,-i\}$ are



$$
C_{\nu,\alpha}(q)
 =[z^q]{u(\alpha+z)^{6m}\over
 Q_\alpha(\alpha+z)^{4m+1+\nu}},                         \tag{3.2}
$$



where $Q(x)=(x-\alpha)Q_\alpha(x)$.  They give $L_\nu,E_\nu$
from the simple-pole residues.  Direct integration gives the finite endpoint
formula



$$
X_\nu=
 \sum_{\alpha}\sum_{n=1}^{4m+\nu}
 {p\over n}C_{\nu,\alpha}(4m+\nu-n)
 \{(-\alpha)^{-n}-(1-\alpha)^{-n}\}.                     \tag{3.3}
$$



Equation (3.3) is evaluated $p$-adically.  Because $e=1$, every $n$ has
$v_p(n)\le1$ and the terms split into exactly two bands: $p\mid n$ and
$p\nmid n$.  The local differential recurrence used by the certificate
computes (3.2) modulo $p^3$ with an exact factorial-valuation reserve.
Thus (3.2)--(3.3) are a finite, deterministic evaluation of all coordinates
needed below.

Write their canonical digits as



$$
\begin{aligned}
 L_\nu&=\ell_{\nu,0}+p\ell_{\nu,1}+p^2\ell_{\nu,2}\pmod {p^3},\\
 X_\nu&=x_{\nu,0}+px_{\nu,1}+p^2x_{\nu,2}\pmod {p^3},\\
 E_\nu&=e_{\nu,0}+pe_{\nu,1}+p^2e_{\nu,2}\pmod {p^3},
\end{aligned}                                             \tag{3.4}
$$



with every digit in $\{0,\ldots,p-1\}$.  Define



$$
S_n^A=\sum_{q=0}^n
  (\ell_{1,q}x_{0,n-q}-\ell_{0,q}x_{1,n-q}),              \tag{3.5}
$$



and start with $c_{-1}^A=0$.  Recursively put



$$
d_n^A\equiv S_n^A+c_{n-1}^A\pmod p,quad0\le d_n^A<p,
\qquad
 c_n^A={S_n^A+c_{n-1}^A-d_n^A\over p}.                   \tag{3.6}
$$



Then $d_n^A$ is exactly the $n$-th base-$p$ digit of $\mathscr A$.
Rank one gives $d_0^A=0$, and therefore



$$
\boxed{
 A_0=d_1^A\equiv S_1^A+{S_0^A\over p}\pmod p.}           \tag{3.7}
$$



If $A_0=0$, the next quotient is integral and



$$
\boxed{
 A_1=d_2^A\equiv
 S_2^A+{S_1^A+S_0^A/p\over p}\pmod p.}                   \tag{3.8}
$$



For the $B$-minor replace $x_{\nu,q}$ in (3.5)--(3.6) by
$e_{\nu,q}$.  Calling the result $S_n^B,c_n^B,d_n^B$, one has



$$
\boxed{
 B_0=d_1^B\equiv S_1^B+{S_0^B\over p}\pmod p.}           \tag{3.9}
$$



Every division by $p$ in (3.6)--(3.9) occurs only after the displayed
divisibility has been verified.  No Cartier-scalar inverse appears.

On $\kappa=1$ one has $\delta=0$ and $D=1$.  The exact primitive
normalization gives



$$
v_p(U_m)=1+v_p(\mathscr A/p),\qquad
 v_p(V_m)=2+v_p(\mathscr B/p).                             \tag{3.10}
$$



Taking the minimum in (3.10) proves (1.1): $p^3\mid c_m$ precisely when
$\mathscr A/p$ has two zero digits and $\mathscr B/p$ has one.

## 4. What the first Bockstein really reduces

Put



$$
\widetilde\Theta
 =\widetilde\gamma_1P_0-\widetilde\gamma_0P_1.            \tag{4.1}
$$



Its $x^{p-1}$ coefficient vanishes exactly over the integers.  Therefore the
zero-constant primitive



$$
\widetilde T(x)=\sum_{\substack{0\le q\le2p-3\\q\ne p-1}}
       {[x^q]\widetilde\Theta\over q+1}x^{q+1}            \tag{4.2}
$$



is $p$-integral and satisfies
$\widetilde T'=\widetilde\Theta$.  Write
$\bar T=\widetilde T\bmod p$ and define



$$
\eta=F_j^{p-1}F_j'\widetilde T\,dx.     \tag{4.3}
$$



The exact identity



$$
\widetilde\gamma_1\omega_0-\widetilde\gamma_0\omega_1
 =d(F_j^p\widetilde T)-p\eta                              \tag{4.4}
$$



is the first determinant Bockstein.  Since $F_j(0)=F_j(1)=0$, its boundary
term is zero.

For $p\ge2j+3$, the pole order $2j+2$ of $F_j$ is at most $p-1$, so the
relative endpoint operation in (4.4) is integral.  The finitely many smaller
primes are covered directly by Section 3.  Let



$$
\mathcal S=\{0,1,-1,i,-i\},                               \tag{4.5}
$$



and write



$$
{dF_j\over F_j}
 =\sum_{a\in\mathcal S}n_a{dx\over x-a},                  \tag{4.6}
$$



where



$$
n_0=n_1=3j+2,qquad n_{-1}=n_i=n_{-i}=-(2j+2).            \tag{4.7}
$$



Let $\tau_p$ be inverse Frobenius on the residue splitting field
$\mathbb F_p(i)$; it is the identity on $\mathbb F_p$ and is either the
identity or conjugation on $i$.  Modulo exact differentials and a scalar
differential,



$$
\mathcal C\left(\bar T{dF_j\over F_j}\right)
 \equiv\sum_{a\in\mathcal S}\tau_p(n_a\bar T(a)){dx\over x-a}.
                                                                  \tag{4.8}
$$



The omitted scalar multiple produces a multiple of $F_jdx$ after
Cartier and hence drops out of every wedge below.

Let



$$
v_j=(R_j,L_j,E_j)=\operatorname {coord}(F_jdx),
\quad
 z_{j,a}=(R_{j,a},L_{j,a},E_{j,a})
 =\operatorname {coord}\left({F_j\over x-a}dx\right).     \tag{4.9}
$$



All these are fixed rational numbers once $j$ is fixed; away from a finite
set of primes their denominators are units.  Put
$c_a=\tau_p(n_a\bar T(a))$ and
$\chi_4(p)=(-1)^{(p-1)/2}$.  Under the archive convention
$E=-4\operatorname {Im}\operatorname {Res}_i$, applying the relative
Cartier coordinates to (4.4) gives the two exact scalar-free digit formulas



$$
\boxed{
 A_0=\sum_{a\in\mathcal S}c_a
       (R_jL_{j,a}-L_jR_{j,a})\pmod p,}                    \tag{4.10}
$$





$$
\boxed{
 B_0=\chi_4(p)\sum_{a\in\mathcal S}c_a
       (E_jL_{j,a}-L_jE_{j,a})\pmod p.}                    \tag{4.11}
$$



Equations (4.10)--(4.11) are the precise five-divisor collapse.  The
quadratic sign in (4.11) is a unit, so it changes signed values when
$p\equiv3\pmod4$ but changes no zero condition.  The formulas do
not say that every $\bar T(a)$ vanishes, nor that the two linear forms are
independent.  If both reduced scalars vanish, then
$\widetilde\Theta$ and $\widetilde T$ are divisible by $p$, so
$\bar T=0$ and both gates vanish; this is far from necessary.

The evaluations themselves are



$$
\widetilde T(a)=\widetilde\gamma_1
 \sum_{\substack q\ne p-1}{[x^q]P_0\over q+1}a^{q+1}
 -\widetilde\gamma_0
 \sum_{\substack q\ne p-1}{[x^q]P_1\over q+1}a^{q+1}.     \tag{4.12}
$$



Their support and degree grow with $(p,s)$.  No fixed-degree polynomial in
$s$ is obtained from (4.12), and no corresponding collapse for the
second-lift digit $A_1$ is known.

## 5. Exact failure of scalar determination

The certificate evaluates the complete Hasse coordinates and the carries
for six controls.  The decisive pair is



$$
\begin{array}{c|c|c|c|c|c|c|c}
m&p&j&s&(\bar\gamma_0,\bar\gamma_1)&A_0&A_1&B_0\\ \hline
99&107&1&15&(2,75)&0&75&50\\
206&107&3&15&(2,75)&65&2&73.
\end{array}                                                \tag{5.1}
$$



Both rows satisfy (2.2)--(2.4).  Their exact coefficient pair is



$$
(\widetilde\gamma_0,\widetilde\gamma_1)
 =(103402679403168,34844059107936),
$$



whose common reduction is (1.4).  Thus their common
$P_0,P_1,\widetilde T$ come from the same $(p,s)$; only $F_j$ and hence the
weights in (4.10)--(4.11) change.  This proves that neither the exact nor
the reduced scalars, nor the floor-residue pair $(p,s)$, determines $A_0$.

For comparison, the reduced-scalar-zero controls



$$
\begin{array}{c|c|c|c|c|c|c}
m&p&j&s&A_0&A_1&B_0\\ \hline
17&19&1&3&0&16&0\\
36&19&3&3&0&0&0
\end{array}                                                \tag{5.2}
$$



show that even $\bar\gamma_0=\bar\gamma_1=0$ forces only the first lifted
determinants.  The cubic gate still depends on $j$ through $A_1$.

## 6. A quantitative thinness theorem for fixed polynomial loci

Let $\mathcal Z_{m,j}$ be any selected set of $\kappa=1$ primes in the
$j$-th band.  Make the following explicit hypothesis.

> **Bandwise fixed-polynomial hypothesis.**  For every fixed $j$ there are
> finitely many nonzero polynomials
> $F_{j,1},\ldots,F_{j,k_j}\in\mathbb Z[Y]$, independent of $m,p$, such
> that, for all sufficiently large $m$, every $p\in\mathcal Z_{m,j}$
> divides at least one $F_{j,k}(s)$.

This hypothesis is a definition of the certificate class being ruled out.
It is **not** proved for the actual zero set of (3.7)--(3.9).

From (2.4),



$$
s\equiv-(2m+1)\pmod p.             \tag{6.1}
$$



Fix $J$.  For a polynomial $F$ of degree $d$ and coefficient height
$H=\max|[Y^q]F|\ge1$,



$$
|F(-2m-1)|\le(d+1)H(2m+1)^d.                             \tag{6.2}
$$



Put



$$
D_J=\sum_{j\le J}\sum_{k\le k_j}\deg F_{j,k},qquad
 H_J^*=\prod_{j\le J}\prod_{k\le k_j}
       (\deg F_{j,k}+1)H(F_{j,k}).                         \tag{6.3}
$$



Apart from finitely many $m$ for which a fixed evaluation is literally
zero, (6.1) implies



$$
\prod_{\substack{j\le J\\p\in\mathcal Z_{m,j}}}p
 \ \Bigm|\
 \operatorname {rad}
 \prod_{j\le J}\prod_{k\le k_j}F_{j,k}(-2m-1).           \tag{6.4}
$$



Therefore



$$
\sum_{\substack{j\le J\\p\in\mathcal Z_{m,j}}}\log p
 \le D_J\log(2m+1)+\log H_J^*
 =O_J(\log m).                                            \tag{6.5}
$$



No uniform bound on $D_J,H_J^*$ as $J\to\infty$ is assumed.  The tail is
handled independently.  If $j>J$, (2.5) gives



$$
p<{6m\over3J+5}.                   \tag{6.6}
$$



Hence Chebyshev's estimate $\vartheta(x)=O(x)$ gives, uniformly for an
arbitrary subset of the tail,



$$
\sum_{\substack{j>J\\p\in\mathcal Z_{m,j}}}\log p
 \le\vartheta\left({6m\over3J+5}\right)
 =O\left({m\over J}\right).                               \tag{6.7}
$$



First let $m\to\infty$ in (6.5)--(6.7), then let $J\to\infty$.  This
proves



$$
\sum_{j,p\in\mathcal Z_{m,j}}\log p=o(m). \tag{6.8}
$$



Thus no additional PNT-uniformity assumption is required for the zero-rate
conclusion.  If one wants the sharper PNT coefficient, the required
uniform summable-tail statement is exactly



$$
\limsup_{m\to\infty}{1\over m}
 \sum_{\substack{j>J\\p\text{ in the }j\text{-th cell}}}\log p
 \le\sum_{j>J}w_j<{2\over3(J+1)}.                         \tag{6.9}
$$



The proof of (6.8) deliberately uses only the weaker unconditional
(6.7).

For an affine ray



$$
p=As+B\qquad(A>0),                 \tag{6.10}
$$



take $F(Y)=AY+B$.  Equations (6.1) and (6.10) give



$$
p\mid2Am+A-B,                      \tag{6.11}
$$



which proves (1.6).  More generally, a fixed affine floor relation
$p=As+Bj+C$ gives, on fixed $j$,



$$
p\mid-A(2m+1)+Bj+C.                \tag{6.12}
$$



Congruence refinements do not change the bound.  For example, the known
support-zero ray



$$
p=5s+4,\qquad p\equiv19\pmod {20}  \tag{6.13}
$$



is contained in the divisors of $10m+1$.

The theorem covers every argument that reduces the gate, band by band, to
finitely many fixed polynomial congruences.  It does not cover a polynomial
whose degree/support grows with $p$, an unbounded collection of relations
inside a fixed band, or arbitrary cancellation in (4.10)--(4.12).

## 7. Finite diagnostics, not asymptotics

The frozen $m\le250$ census specializes as follows.



$$
\begin{array}{l|r}
\text{quantity}&\text{count}\\ \hline
\kappa=1\text{ forced rows}&2649\\
\bar\gamma_0=\bar\gamma_1=0&15\\
A_0=0&119\\
A_0=0\text{ with }(\bar\gamma_0,\bar\gamma_1)\ne(0,0)&104\\
A_0=A_1=B_0=0&10\\
\text{non-scalar cubic gates}&8\\
\text{same }(p,s)\text{ groups containing both }A_0=0,A_0\ne0&55.
\end{array}                                                \tag{7.1}
$$



The ten cubic survivors are



$$
\begin{array}{c|c|c|c|c}
m&p&j&s&(\bar\gamma_0,\bar\gamma_1)\\ \hline
36&19&3&3&(0,0)\\
67&17&7&1&(2,11)\\
74&19&7&3&(0,0)\\
100&23&8&6&(6,11)\\
101&23&8&4&(13,0)\\
102&23&8&2&(10,16)\\
103&23&8&0&(10,6)\\
166&31&10&8&(18,24)\\
172&29&11&3&(2,26)\\
199&29&13&7&(24,15).
\end{array}                                                \tag{7.2}
$$



All primes in (7.2) are at most $31$.  This observation is finite-only and
does not imply eventual nonexistence.

A bounded search over $p=As+B$, $1\le A\le12$, $|B|\le20$, found no
unrefined line containing at least eight stored rows and three primes on
which every $A_0$ vanished.  Adding small residue refinements rediscovers
(6.13), with 15 stored rows and seven primes; it finds no line on which all
stored rows pass the cubic gate.  These searches audit the known ray and
look for simple missed patterns.  They are not a classification theorem.

## 8. Capacity consequence and remaining target

Equation (6.8) shows that any bounded number of valuation copies carried by
a bandwise fixed-polynomial family contributes $o(m)$ to the logarithm of
the content.  After normalization by $6m$, its Route-1 capacity is zero.
Such rays cannot reduce any positive capacity deficit.

For scale only, if every prime in the entire $\kappa=1$ cell carried three
copies, that cell would contribute at most



$$
{3C_1\over6}={C_1\over2}
                         =0.2410187508850556\ldots           \tag{8.1}
$$



per $6m$.  The two copies beyond its already forced radical would contribute
at most $C_1/3=0.1606791672567038\ldots$.  These are ceilings, not proved
gains.  Item 168 already shows that even three complete layers over all
rank-at-most-two cells miss the Route-1 threshold.

The genuine remaining target is therefore not another fixed ray.  It is a
uniform theorem for the moving, non-scalar system



$$
A_0(j,s,p)=A_1(j,s,p)=B_0(j,s,p)=0 \tag{8.2}
$$



on a PNT-positive subset, or a theorem placing the actual solutions of
(8.2) inside the fixed-polynomial class of Section 6.  Neither is proved.

## 9. Deterministic certificate

The standard-library checker

`scripts/item172_rankone_nonscalar_certificate.py`

performs the following exact tasks.

1. It reconstructs every frozen $\kappa=1$ row and verifies (2.3)--(2.4).
2. It evaluates (2.13), including generalized-binomial cases.
3. It replays six rows from the modulo-$p^3$ local Hasse recurrence and
   verifies the raw convolutions, carries, $A_0,A_1,B_0$, and direct
   determinants.
4. It certifies the counterpair (1.3)--(1.4).
5. It checks the width identity (2.6), the tail comparison (2.7), and the
   affine divisor identity (1.6) on every stored line row.
6. It reports the finite counts and bounded affine searches in Section 7.

Two canonical executions are required to be byte-identical before the
package is integrated.  The replay is an audit of the exact formulas and
finite data; the uniform statements are the algebraic proofs above.

## 10. Status ledger

### PROVED

- The complete scalar-free Hasse/carry formulas (3.7)--(3.9).
- The exact cubic gate (1.1).
- The integrality-safe five-divisor $A_0,B_0$ formulas (4.10)--(4.11).
- The same exact/reduced-scalar counterpair (1.3)--(1.4).
- The quantitative fixed-polynomial and affine thinness theorem.

### EXPERIMENTAL FINITE

- The counts $2649,119,104,10,8$ in (7.1).
- The ten stored cubic survivors (7.2).
- The bounded affine/residue search.

### OPEN

- Any positive-mass non-scalar family satisfying (8.2).
- Any proof that the actual zero set belongs to the fixed-polynomial class.
- Any new positive asymptotic content exponent.
- The rationality, irrationality, or transcendence of $e+\pi$.
