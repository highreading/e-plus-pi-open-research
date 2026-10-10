> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 225 — A second Cartier condition for the fixed $j=2$ cell

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Retain the Item 219/221/224 cell



$$
4m+1=5p-2s,\qquad 1\le s\le\frac{p-3}{6},\qquad
 s\equiv\frac{p-1}{2}\pmod2,\qquad p\ge11,              \tag{1.1}
$$



and



$$
r=\frac{p-6s-3}{2},\qquad
 f_0(z)=z^r g(z),\qquad
 g(z)=(1-z)^r(1+z)(1+z^2)^{2s}.                       \tag{1.2}
$$



This item continues Item 224 through the next Frobenius phase.  It does
not merely enlarge Item 224's finite scan.

> **PROVED — exact regularized recurrence.**  Delete from each formal
> primitive precisely the monomials whose exponents are divisible by
> $p$, and call the resulting period $\widehat T_k$.  If
> 

$$
> K_k=z^{k+1}(1-z^4)f_0,\qquad
> (A_0,\ldots,A_4)=
> (k+r+1,1-r,4s-r-1,1-r,-k-2r-4s-6),
>
$$


> then
> 

$$
> \boxed{\ \sum_{j=0}^4A_j(k)\widehat T_{k+j}
> =-\sum_{a\ge1}[z^{ap}]K_k\,W_{\mathcal L}(ap).\ }    \tag{1.3}
>
$$


> The sum is finite.  The first terminal $k=2s-3$ has right-hand side
> $7(-1)^r$, recovering Item 224.  The second terminal
> $k=p+2s-3$ has the new right-hand side
> 

$$
>                         29(-1)^r.                    \tag{1.4}
>
$$



> **PROVED — the first-resonance freedom disappears before the second
> terminal.**  The free mode introduced at $\widehat T_{2s+1}$ has
> generating polynomial
> 

$$
>                         X(z)=g(z).                   \tag{1.5}
>
$$


> Moreover
> 

$$
> \deg g=\frac{p+2s-1}{2}<p-4.                        \tag{1.6}
>
$$


> Therefore its four entries in the second terminal are identically
> zero.  Equation (1.4) is a genuinely new scalar condition, not an
> equation that merely determines the free first-resonance moment.

> **PROVED — second necessary collision condition.**  Let
> $\tau,\beta,\Omega$ be Item 224's exact recurrence quantities.  The
> second propagation canonically produces two scalars
> $\rho_0,\rho_1$, defined in Section 6, and
> 

$$
> \Psi_{p,s}
> =\tau\bigl(\rho_0-29(-1)^r\bigr)+7(-1)^r\rho_1.      \tag{1.7}
>
$$


> Every actual common-log collision with $s\ge2$ must satisfy
> 

$$
> \boxed{\quad\beta\tau\ne0,\qquad
>        \Omega_{p,s}=0,\qquad\Psi_{p,s}=0\pmod p.\quad} \tag{1.8}
>
$$



> **EXACT FINITE ONLY.**  The seven Item 224 rows with
> $\Omega=0$ through $p\le401$ have respectively
> 

$$
>                  \Psi=15,130,79,71,185,292,230,      \tag{1.9}
>
$$


> each reduced modulo its row prime.  Thus the new condition eliminates
> all seven formal-compatible rows, and there is no simultaneous
> $\Omega=\Psi=0$ row through $p\le401$.

> **OPEN.**  No all-prime exclusion or density theorem for simultaneous
> zeros of $(\Omega,\Psi)$ is proved.  The exceptional $s=1$ family
> remains open.  Hence Item 225 books no capacity reduction and proves
> nothing about $e+\pi$.

## 2. The endpoint phase and coefficient reciprocity

For an endpoint primitive $F$, use real coordinates



$$
E=F(1),\qquad C=\frac{F(i)+F(-i)}2,\qquad
 S=\frac{F(i)-F(-i)}{2i}.                             \tag{2.1}
$$



With $\chi=(-1)^{(p-1)/2}$, the Item 219 functional and its reciprocal
covector are



$$
{\mathcal L}=(9,-20,-2\chi),\qquad
 {\mathcal L}^{\vee}=(9,-2,-20\chi).                  \tag{2.2}
$$



Their monomial weights obey



$$
W_{\mathcal L}(n)=
 \begin{cases}
 -11,&n\equiv0\pmod4,\\
 9-2\chi,&n\equiv1\pmod4,\\
 29,&n\equiv2\pmod4,\\
 9+2\chi,&n\equiv3\pmod4,
 \end{cases}                                          \tag{2.3}
$$



and direct evaluation in both phases gives



$$
W_{{\mathcal L}^{\vee}}(n)=W_{\mathcal L}(p-n),\qquad
 W_{\mathcal L}(p)=7,\qquad W_{\mathcal L}(2p)=29.    \tag{2.4}
$$



Put $d=\deg g=r+4s+1$.  Reversing the factors in (1.2) gives the exact
integer identity



$$
z^d g(1/z)=(-1)^r g(z),\qquad
 g_\ell=(-1)^r g_{d-\ell}.                            \tag{2.5}
$$



If $k^\vee=2s-r-k$, then the paired primitive denominators satisfy



$$
(r+\ell+k+1)+(r+d-\ell+k^\vee+1)=p.                 \tag{2.6}
$$



Using (2.4)--(2.6), and deleting the paired $p$- and $0$-resonant
terms when present, proves



$$
\boxed{\quad
 \widehat T_{{\mathcal L},k}
 =(-1)^{r+1}
 \widehat T_{{\mathcal L}^{\vee},\,2s-r-k}.
 \quad}                                               \tag{2.7}
$$



The sign in (2.7) includes the minus sign from
$(p-n)^{-1}=-n^{-1}\pmod p$.  In particular, the first upper
resonance $k=2s+1$ pairs with the omitted lower logarithmic term
$k^\vee=-r-1$.  Reciprocity alone exchanges phase coordinates; the
additional scalar obstruction comes from advancing to the second
Cartier terminal.

## 3. Exact finite-part recurrence

Write



$$
f_0(z)=\sum_n c_nz^n.        \tag{3.1}
$$



Define the regularized primitive and period by



$$
\widehat F_k(x)=
 \sum_{\substack{n\\p\nmid n+k+1}}
 \frac{c_nx^{n+k+1}}{n+k+1},\qquad
 \widehat T_k={\mathcal L}(\widehat F_k).              \tag{3.2}
$$



All displayed inverses in (3.2) are therefore $p$-units.  Item 224's
exact differential identity is



$$
K'_k=\sum_{j=0}^4A_j(k)z^{k+j}f_0.  \tag{3.3}
$$



Integrate (3.3) over the integers before reduction.  For every exponent
$ap$, the omitted primitive terms on the left sum to exactly
$[z^{ap}]K_kz^{ap}$.  Consequently



$$
\sum_{j=0}^4A_j(k)\widehat F_{k+j}
 =K_k-K_k(0)-\sum_{a\ge1}[z^{ap}]K_kz^{ap}.           \tag{3.4}
$$



For the ranges used below, $K_k(0)=0$, and $K_k$ vanishes at
$1,i,-i$ because of $1-z^4$.  Applying $\mathcal L$ proves
(1.3).  This derivation audits every Cartier regularization at once; it
never reduces a zero denominator.

Let



$$
h(z)=(1-z^4)f_0(z).
$$



Since



$$
\deg f_0=p-2s-2,\qquad
 \deg h=p-2s+2,\qquad
 [z^{p-2s+2}]h=(-1)^{r+1},                            \tag{3.5}
$$



the first terminal $k=2s-3$ has
$[z^p]K_k=(-1)^{r+1}$.  Equations (1.3) and (2.4) give
$7(-1)^r$.

At the second terminal $k=p+2s-3$, the lowest exponent of $K_k$ is
strictly greater than $p$, while its top exponent is $2p$.
Thus the only Cartier term is



$$
[z^{2p}]K_k=(-1)^{r+1},
$$



and (1.3) gives $29(-1)^r$, proving (1.4).

## 4. Every intervening pivot is a unit

At the first terminal, the last recurrence coefficient is $-p$.
For



$$
k=2s-2,\ldots,p+2s-4,
$$



write $k=2s-3+t$, where $1\le t\le p-1$.  Then



$$
-(k+2r+4s+6)=-(p+t)\equiv-t\not\equiv0\pmod p.       \tag{4.1}
$$



At $k=p+2s-3$, this coefficient is $-2p$, producing the second
terminal.  Therefore the recurrence propagates uniquely between the
two terminals, apart from the single free value
$\widehat T_{2s+1}$ introduced at the first one.

## 5. The free mode is exactly $g$

Let $X_n$ be the homogeneous response to



$$
X_0=1,\qquad X_{-1}=X_{-2}=X_{-3}=0,                 \tag{5.1}
$$



where $X_n$ is attached to moment index $2s+1+n$.  Substituting
$k=2s-2+n$ into the recurrence and using
$p=2r+6s+3$ gives



$$
\begin{aligned}
(n+1)X_{n+1}={}&(1-r)X_n+(4s-r-1)X_{n-1}
 +(1-r)X_{n-2}\\
& +(n+r+2s-1)X_{n-3}.                                \tag{5.2}
\end{aligned}
$$



For $X(z)=\sum_{n\ge0}X_nz^n$, equation (5.2) is



$$
(1-z^4)X'=
 \bigl((1-r)+(4s-r-1)z+(1-r)z^2+(r+2s+2)z^3\bigr)X. \tag{5.3}
$$



On the other hand, logarithmic differentiation of $g$ gives the same
right-hand side except that its $z^3$-coefficient is
$-(r+4s+1)$.  The difference is exactly



$$
(r+2s+2)-\bigl(-(r+4s+1)\bigr)=2r+6s+3=p.           \tag{5.4}
$$



Thus $g$ satisfies (5.3) in $\mathbb F_p[z]$, and $g(0)=1$.
The pivots $n+1$ are units for $0\le n\le p-2$, so uniqueness
proves (1.5) through every index needed at the second terminal.

For $s\ge2$, admissibility forces $p\ge17$, and



$$
\deg g=r+4s+1=\frac{p+2s-1}{2},\qquad
 p-4-\deg g=\frac{p-2s-7}{2}>0.                      \tag{5.5}
$$



Indeed $6s\le p-3$ makes the final numerator at least
$2(p-9)/3>0$.  The four free-mode indices in the second terminal are
$p-4,p-3,p-2,p-1$, all beyond $\deg g$.  Their coefficients vanish
identically.  This proves the second theorem in Section 1.

## 6. Definition and necessity of $\Psi$

Let $U_k$, $\tau$, $\beta$, and



$$
\Omega=7(-1)^r\beta-11\tau                         \tag{6.1}
$$



be Item 224's canonical first-phase quantities.  Before the first
resonance, a common collision has $\widehat T_k=\lambda U_k$.

To define the second-phase quantities without division by $\tau$, set



$$
(C_k,V_k)=(0,U_k)\quad(k\le2s),\qquad
 (C_{2s+1},V_{2s+1})=(0,0),                          \tag{6.2}
$$



and propagate (1.3) from $k=2s-2$ through
$k=p+2s-4$, putting the inhomogeneous right-hand side into $C$ and
using the homogeneous recurrence for $V$.  Every pivot is a unit by
Section 4.

At $k_2=p+2s-3$, define



$$
\rho_0=\sum_{j=0}^3A_j(k_2)C_{k_2+j},\qquad
 \rho_1=\sum_{j=0}^3A_j(k_2)V_{k_2+j}.                \tag{6.3}
$$



The free first-resonance value contributes zero by Section 5.
Therefore every actual common collision must satisfy



$$
\rho_0+\lambda\rho_1=29(-1)^r,\qquad
 \lambda\tau=7(-1)^r,\qquad
 \lambda\beta=11.                                    \tag{6.4}
$$



Eliminating $\lambda$ from the first two equations yields (1.7).
Eliminating it with the bottom equation gives the equivalent condition



$$
\Psi^\flat
 =\beta\bigl(\rho_0-29(-1)^r\bigr)+11\rho_1=0.        \tag{6.5}
$$



When $\Omega=0$,



$$
11\Psi=7(-1)^r\Psi^\flat,   \tag{6.6}
$$



and $7,11$ are units because $s\ge2$ forces $p\ge17$.
This proves (1.8) with no exceptional denominator.

## 7. Exact finite census

The deterministic replay enumerates all 1,153 admissible rows through
$p\le401$: 38 have $s=1$, and 1,115 have $s\ge2$.  Among the
latter, 1,108 already have $\Omega\ne0$.  The remaining exact data
are



$$
\begin{array}{c|r|r|r|r|r|r}
p&s&\tau&\rho_0&\rho_1&29(-1)^r&\Psi\\ \hline
23&3&1&0&2&17&15\\
157&4&75&99&52&128&130\\
193&26&49&121&184&164&79\\
241&4&25&188&214&212&71\\
311&47&251&217&42&282&185\\
349&50&82&153&96&320&292\\
397&44&147&314&251&368&230
\end{array}                                           \tag{7.1}
$$



All entries in a row are reduced modulo its first-column prime.  Thus
all seven Item 224 formal-compatible rows fail the new necessary
condition, and the finite joint-zero census is empty.  The complete
row transcript has SHA-256

c7ed88de837b23527dd8b8c926978b5d493606bc8810c4bef8709f739467eb0e.

As an independent formula replay, every admissible $s\ge2$ row
through $p\le101$ is checked coefficient by coefficient for
reciprocity, the full forcing identity (1.3), both terminal constants,
and the free-mode formula.  These finite checks replay the identities;
Sections 2--6 contain the all-row proofs.

## 8. Capacity and limitations

The fixed $j=2$ common-log cell has capacity $2/35$ per $m$.
A finite empty joint-zero census does not exclude the cell
asymptotically.  Item 225 therefore books rate $0$.

The new theorem changes the all-prime target from one congruence to the
simultaneous system



$$
\Omega_{p,s}=\Psi_{p,s}=0.   \tag{8.1}
$$



Classifying or bounding the solutions of (8.1), rather than merely
extending the finite scan, is the next arithmetic problem.

## 9. Reproduction and status ledger

From the portable archive root:

~~~
python scripts/item225_j2_second_cartier_certificate.py \
  --output results/item225_j2_second_cartier_certificate.json
python scripts/item225_j2_second_cartier_certificate.py \
  --output results/item225_j2_second_cartier_certificate_replay.json
~~~

The checker uses only Python's standard library and the frozen Item 219,
Item 221, and Item 224 helpers stored beside it.

**PROVED**

- exact coefficient and regularized-period reciprocity in both
  $p\bmod4$ phases;
- the finite-part forcing formula (1.3);
- $W_{\mathcal L}(p)=7$ and $W_{\mathcal L}(2p)=29$;
- the free-mode identity $X=g$ and the exact support gap (5.5);
- collision implies $\beta\tau\ne0$ and
  $\Omega=\Psi=0$.

**EXACT FINITE**

- all seven Item 224 $\Omega$-zeros have $\Psi\ne0$ through
  $p\le401$;
- there is no joint $\Omega=\Psi=0$ row through that bound.

**OPEN**

- an all-prime exclusion or density bound for simultaneous zeros;
- the $s=1$ family;
- a zero-rate theorem for the fixed $j=2$ cell;
- any capacity reduction or conclusion about $e+\pi$.

