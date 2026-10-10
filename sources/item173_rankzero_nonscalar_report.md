> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 173 — the rank-zero missing digit and an extended exact tail

Date: 2026-08-29

## 1. Scope and verdict

Put



$$
u=x(1-x),\qquad Q=(1+x)(1+x^2),\qquad
 \omega_s={u^{6m}\over Q^{4m+1+s}}\,dx\quad(s=0,1),
$$



and retain the endpoint coordinates



$$
H_s=R_s+{L_s\over4}\log2+{E_s\over8}\pi,
 \qquad X_s=pR_s,
$$



and minors



$$
\mathscr A=L_1X_0-L_0X_1,\qquad
 \mathscr B=L_1E_0-L_0E_1.                         \tag{1.1}
$$



This note treats the regular second-Cartier part $2j+2<p$ of the
top-layer rank-zero cell $\kappa=2$ from Item 168.  This contains every
fixed-$j$, prime-number-theorem-scale band.  The outer pole boundary
$j=(p-1)/2$ is arithmetically zero-rate but crosses the next denominator
band and is not classified here.  The conclusions are deliberately scoped.

**PROVED — exact scalar-free carry formula.**  The first Cartier images
vanish separately.  After one exact primitive, define integral coordinates



$$
\ell_s={L_s\over p},\qquad \rho_s={X_s\over p},
 \qquad \varepsilon_s={E_s\over p}.                    \tag{1.2}
$$



Then, without dividing by a Cartier scalar,



$$
\boxed{{\mathscr A\over p^2}=\ell_1\rho_0-\ell_0\rho_1},
 \qquad
 \boxed{{\mathscr B\over p^2}=\ell_1\varepsilon_0-
                                  \ell_0\varepsilon_1}. \tag{1.3}
$$



Writing canonical base-$p$ digits gives the exact formula for the
previously missing digit $A_1$, including its determinant carry; see
Section 3.

**PROVED — one-row extension of the automatic second layer.**  Item 168
used



$$
3j\ge p,\qquad2j+2\le p.             \tag{1.4}
$$



The exact endpoint identity



$$
\boxed{H_s(1)=N_s(1)=-4aT_s(1)}         \tag{1.5}
$$



adds the boundary $3j+1=p$.  Thus the sharper uniform hypothesis is



$$
\boxed{3j+1\ge p,\qquad2j+2\le p}.      \tag{1.6}
$$



Every row in (1.6) has



$$
A_0=B_0=0,qquad p^2\mid c_m.    \tag{1.7}
$$



At the new boundary, (1.5) makes $H_s$ divisible by $u$, and the
remaining polynomial after extracting $(u/Q)^p$ has degree at most
$p-2$.  This is an exact characteristic-$p$ statement.

**PROVED — zero-rate support.**  Condition (1.6) gives



$$
p^2\le6m.                     \tag{1.8}
$$



Consequently all primes reached by this automatic mechanism have total
logarithmic weight $O(\sqrt m)=o(m)$.  The boundary extension cannot
produce positive prime-number-theorem mass.

**PROVED — the tail hypotheses determine neither value of the missing
digit.**  Exact rows give the counterpair



$$
\begin{array}{c|c|c|c|c}
(m,p,j,s)&A_0&A_1&B_0&\text{conclusion}\\ \hline
(54,17,6,2)&0&4&0&17^2\parallel c_{54},\\
(180,29,12,2)&0&0&0&29^3\mid c_{180}.
\end{array}                                             \tag{1.9}
$$



Both rows satisfy (1.6).  Thus those hypotheses force neither automatic
cubic divisibility nor automatic cubic nondivisibility.  The two rows are
not claimed to have identical reduced coordinate data.

**EXPERIMENTAL FINITE.**  The deterministic scan through $p\le43$
contains 249 regular rank-zero cells and 84 rows in (1.6), including
eight new boundary rows.  Every tail row has $A_0=B_0=0$; five have
$A_1=0$, while 79 have $A_1\ne0$.  These counts audit the formulas
and have no asserted density meaning.

**OPEN.**  No positive-mass family is known for
$A_0=A_1=B_0=0$ in the PNT-scale part of the rank-zero cell.  No
equidistribution or independence of the digits is assumed.  This item
does not improve the Route-1 exponential constant and gives no conclusion
about $e+\pi$.

## 2. Complete rank-zero cell and first primitive

Assume



$$
p\le4m+1<p^2                    \tag{2.1}
$$



and write



$$
6m=ap+r,\qquad4m+1=bp+t,
 \qquad0\le r,t<p,\qquad2a-3b=2.                       \tag{2.2}
$$



The complete $t>0$ parameterization is



$$
\begin{aligned}
 a&=3j+1,& b&=2j,\\
 t&=p-2s,& r&={p-6s-3\over2},                           \tag{2.3}\\
 4m+1&=(2j+1)p-2s,&
 1&\le s\le {p-3\over6}.
\end{aligned}
$$



The last displayed upper bound means its integer floor.  One also requires
the right side of the formula for $4m+1$ to be $1\pmod4$.  These
conditions make $r,t$ integral and give $0\le r,t<p$.  The strict
top-layer inequality adds $1\le j\le(p-1)/2$.  From Section 3 onward
we work in the regular range $2j+2<p$, leaving the single outer value
$j=(p-1)/2$ outside the claim.

Set



$$
F={u^{3j+1}\over Q^{2j+1}},\qquad
 P_0=u^rQ^{2s},\qquad P_1=u^rQ^{2s-1}.                  \tag{2.4}
$$



Then



$$
\omega_s=F^pP_s\,dx.             \tag{2.5}
$$



The two polynomial degrees are



$$
\deg P_0=p-3,\qquad
                        \deg P_1=p-6.                   \tag{2.6}
$$



In particular neither polynomial has an $x^{p-1}$ term, so both first
Cartier images vanish.  Let $T_s$ be the zero-constant, $p$-integral
primitive



$$
T_s'=P_s.                  \tag{2.7}
$$



No denominator in (2.7) is divisible by $p$, by (2.6).  Differentiating
$F^pT_s$ gives the exact identity



$$
\omega_s=d(F^pT_s)-p\Psi_s,
 \qquad \Psi_s=F^{p-1}F'T_s\,dx.                       \tag{2.8}
$$



The boundary term vanishes because $F$ vanishes at both endpoints.
Therefore



$$
R_s=-pR(\Psi_s),\qquad
 L_s=-pL(\Psi_s),\qquad E_s=-pE(\Psi_s).               \tag{2.9}
$$



The top-layer endpoint lemma makes



$$
pR(\Psi_s),\quad L(\Psi_s),\quad E(\Psi_s)             \tag{2.10}
$$



all $p$-integral.  Thus (1.2) is equivalently



$$
\ell_s=-L(\Psi_s),\qquad
 \rho_s=-pR(\Psi_s),\qquad
 \varepsilon_s=-E(\Psi_s).                             \tag{2.11}
$$



Substitution of (2.9)--(2.11) into (1.1) proves (1.3) as an
identity over $\mathbb Z_p$.  This is why the construction remains
nonsingular when both first Cartier scalars are zero.

## 3. The exact determinant carry and the missing digit

Write canonical digits



$$
\ell_s=\ell_{s,0}+p\ell_{s,1}+O(p^2),\qquad
 \rho_s=\rho_{s,0}+p\rho_{s,1}+O(p^2),                 \tag{3.1}
$$



with every displayed digit in $\{0,\ldots,p-1\}$.  Put



$$
\begin{aligned}
 S_0&=\ell_{1,0}\rho_{0,0}-\ell_{0,0}\rho_{1,0},\\
 S_1&=\ell_{1,0}\rho_{0,1}+\ell_{1,1}\rho_{0,0}
      -\ell_{0,0}\rho_{1,1}-\ell_{0,1}\rho_{1,0}.      \tag{3.2}
\end{aligned}
$$



Let $A_0$ be the canonical residue of $S_0$ modulo $p$, and let



$$
c_0={S_0-A_0\over p}.          \tag{3.3}
$$



The quotient in (3.3) is an integer, possibly negative.  Expanding the
first identity in (1.3) now gives the exact scalar-free carry formula



$$
\boxed{A_0\equiv S_0\pmod p,\qquad
        A_1\equiv S_1+c_0\pmod p.}                       \tag{3.4}
$$



The identical construction with $\rho_s$ replaced by
$\varepsilon_s$ gives $B_0$.  Formula (3.4) is the rank-zero
specialization of Item 163's all-depth determinant recurrence, but (1.3)
shows directly where its two forced zero digits come from.

The leading reductions in (3.1) are supplied by the second Cartier
differentials.  Set



$$
N_s=T_s\{a u'Q-cQ'u\},\qquad a=3j+1,\quad c=2j+1,      \tag{3.5}
$$



and define



$$
H_s(x)=\sum_{n=0}^{4}
 \left(\sum_{z=0}^{p-1}[x^{pn-4z}]N_s\right)x^n.        \tag{3.6}
$$



The coefficient range makes $\deg H_s\le4$, and $T_s(0)=0$
gives $H_s(0)=0$.  The standard filter with
$\mathfrak D=uQ=x(1-x^4)$ gives



$$
\Phi_s:=\mathcal C\Psi_s
 ={u^{3j}H_s\over Q^{2j+2}}\,dx.                       \tag{3.7}
$$



Modulo $p$, up to the harmless Frobenius sign on the circular
coordinate,



$$
(\rho_{s,0},\ell_{s,0},\varepsilon_{s,0})
 =(-R(\Phi_s),-L(\Phi_s),-\chi_4(p)E(\Phi_s)).          \tag{3.8}
$$



Thus $A_0$ and $B_0$ are first determinants of the transformed
coordinates, whereas $A_1$ contains the genuinely new digits
$\ell_{s,1},\rho_{s,1}$ and the carry (3.3).

This is also a formal non-determination statement.  If the leading vector
$(\rho_{0,0},\rho_{1,0})$ is nonzero while
$\ell_{0,0}=\ell_{1,0}=0$, varying the new pair
$(\ell_{0,1},\ell_{1,1})$ realizes every value of $A_1$ in
$\mathbb F_p$.  The first and second Cartier reductions alone do not
fix the missing digit.  This coordinate observation does not assert that
all such lifts occur in the mixed-cubic family.

## 4. The endpoint identity and the boundary extension

Summing the coefficients in (3.6) gives a useful exact identity.  For
each exponent $k$ occurring in $N_s$, there is exactly one
$z\in\{0,\ldots,p-1\}$ for which



$$
k+4z\equiv0\pmod p,          \tag{4.1}
$$



because $4$ is invertible modulo the odd prime $p$.  Hence every
coefficient of $N_s$ appears exactly once in $H_s(1)$, and



$$
H_s(1)=N_s(1).               \tag{4.2}
$$



At $x=1$, one has $u(1)=0$, $u'(1)=-1$, and $Q(1)=4$.
Equation (3.5) therefore yields



$$
H_s(1)=N_s(1)=-4aT_s(1),               \tag{4.3}
$$



which proves (1.5).

Assume (1.6) and put $K=2j+2$.  There are two cases.

### 4.1 The ordinary tail: $3j\ge p$

Equation (3.7) becomes



$$
\Phi_s=\left({u\over Q}\right)^p
 u^{3j-p}H_sQ^{p-K}\,dx.                               \tag{4.4}
$$



Its residual polynomial has degree



$$
2(3j-p)+\deg H_s+3(p-K)
 =p-6+\deg H_s\le p-2.                                 \tag{4.5}
$$



### 4.2 The new boundary: $3j+1=p$

Here $a=p=0$ in $\mathbb F_p$.  Equations (3.6) and (4.3) give



$$
H_s(0)=H_s(1)=0.                \tag{4.6}
$$



Thus $u=x(1-x)$ divides $H_s$.  Now



$$
\Phi_s=\left({u\over Q}\right)^p
 {H_s\over u}Q^{p-K}\,dx.                              \tag{4.7}
$$



The equality $j=(p-1)/3$ implies



$$
K={2p+4\over3},\qquad p-K={p-4\over3}\ge1.            \tag{4.8}
$$



Since $\deg(H_s/u)\le2$, the residual degree is at most



$$
2+3(p-K)=p-2.                   \tag{4.9}
$$



In both cases, the elementary characteristic-$p$ lemma makes
$f^pP(x)dx$ exact whenever $\deg P\le p-2$.  Therefore both
$\Phi_s$ are exact.  In particular,



$$
L(\Phi_s)=E(\Phi_s)=0,
 \quad\ell_{s,0}=\varepsilon_{s,0}=0.                  \tag{4.10}
$$



Equations (3.2)--(3.4) give



$$
A_0=B_0=0,
 \qquad
 \boxed{A_1=\ell_{1,1}\rho_{0,0}
              -\ell_{0,1}\rho_{1,0}\pmod p}.           \tag{4.11}
$$



The rational endpoints $\rho_{s,0}=-R(\Phi_s)$ need not vanish, and
the new logarithmic digits $\ell_{s,1}$ are not determined by
exactness of $\Phi_s$.  This is the sharp stopping point of the
automatic argument.

Finally, (1.6) says $a=3j+1\ge p$.  From
$6m=ap+r$ and $r\ge0$,



$$
6m\ge p^2.                 \tag{4.12}
$$



Thus



$$
\sum_{\substack{p\text{ accessible by }(1.6)}}\log p
 \le\vartheta(\sqrt{6m})=O(\sqrt m)=o(m).               \tag{4.13}
$$



This proves the zero-rate assertion without any conjectural distribution
input.

## 5. Exact counterpair and finite replay

On the exact tail, the Item-163 content gate is



$$
p^3\mid c_m
 \iff A_0=A_1=B_0=0.                                   \tag{5.1}
$$



For $(m,p,j,s)=(54,17,6,2)$, the exact coordinate digits are



$$
\begin{aligned}
 (\ell_{0,0},\ell_{0,1})&=(0,3),&
 (\ell_{1,0},\ell_{1,1})&=(0,0),\\
 (\rho_{0,0},\rho_{0,1})&=(9,3),&
 (\rho_{1,0},\rho_{1,1})&=(10,15).
\end{aligned}                                           \tag{5.2}
$$



Equation (4.11) gives $A_1=-3\cdot10=4\pmod {17}$.
Hence $17^2\parallel c_{54}$.

For $(m,p,j,s)=(180,29,12,2)$, the corresponding leading pairs are



$$
(\ell_{0,0},\ell_{0,1})=(0,6),\quad
 (\ell_{1,0},\ell_{1,1})=(0,27),\quad
 (\rho_{0,0},\rho_{1,0})=(4,18).                        \tag{5.3}
$$



Thus



$$
A_1=27\cdot4-6\cdot18=0\pmod {29}.    \tag{5.4}
$$



The same exact computation gives $B_0=0$, and so
$29^3\mid c_{180}$.  Equations (5.2)--(5.4) prove the counterpair
in (1.9).  They do not constitute a density theorem.

The standard-library certificate

`scripts/item173_rankzero_nonscalar_certificate.py`

uses the helper

`scripts/item173_probe.py`

and checks the following through $p\le43$:



$$
\begin{array}{l|r}
\text{regular rank-zero cells}&249\\
\text{primes represented}&10\\
\text{frozen Item-163 coordinate cross-checks}&92\\
\text{rows in the extended exact tail}&84\\
\text{new }3j+1=p\text{ boundary rows}&8\\
\text{tail failures of }A_0=B_0=0&0\\
\text{tail rows with }A_1=0&5\\
\text{tail rows with }A_1\ne0&79\\
\text{carry-formula mismatches}&0.
\end{array}                                             \tag{5.5}
$$



Every row also checks (2.3), (2.6), (4.3), the relevant residual-degree
bound, and $p^2\le6m$.  Two canonical runs are byte-identical.  The
finite counts in (5.5) are diagnostics only; the uniform statements are
the symbolic arguments in Sections 2--4.

## 6. Status ledger

### PROVED

- The exact rank-zero identities (1.3) and determinant carry (3.4).
- The second-Cartier endpoint identity (1.5).
- The extended automatic second layer (1.6)--(1.7).
- The zero-rate support bound $p^2\le6m$.
- The counterpair (1.9), showing that the tail hypotheses force neither
  value of the missing digit.

### EXPERIMENTAL FINITE

- The 249-cell regular second-Cartier scan and 84-row lifted tail replay through
  $p\le43$.
- Five cubic survivors and 79 failures in that finite tail sample.

### OPEN

- A positive-PNT-mass family satisfying $A_0=A_1=B_0=0$ in the
  rank-zero cell.
- A uniform classification of the zeros of (4.11).
- Any resulting improvement in the Route-1 content exponent.
- Any conclusion about the rationality, irrationality, or transcendence
  of $e+\pi$.
