> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 263 — exact Frobenius/Cartier action on the punctured elliptic normal form

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Let



$$
E:\quad Z^2=g(X)=X^3-\frac12,
 \qquad
 D=\{(\alpha,\beta):\alpha^3=1,\ \beta^2=1/2\}.
 \tag{1.1}
$$



For an odd prime $p\ge5$, put



$$
n={p-1\over2},\qquad \epsilon=\left({2\over p}\right),
 \tag{1.2}
$$



and introduce



$$
\omega_a={X^a\over X^3-1}{dX\over Z}\quad(0\le a\le2),
 \qquad
 \eta={dX\over Z},\qquad \xi={X\,dX\over Z}.
 \tag{1.3}
$$



The three residue vectors of the $\omega_a$'s span the odd part of the
residue quotient, while $\eta,\xi$ span the compact de Rham part.  Thus
these five classes form a basis of the hyperelliptic-odd part of
$H^1_{\rm dR}(E\setminus D)$.

The absolute Frobenius pullback on ordinary differentials is zero in
characteristic $p$.  The nontrivial mod-$p$ Frobenius operator relevant
to these moments is therefore the Cartier operator $\mathcal C$.  The
following theorem computes both the geometric Frobenius permutation on
$D$ and this Cartier action; it does not silently identify Cartier with
an unchosen characteristic-zero Frobenius lift.

Write $h_j=(1/2)_j/(j!2^j)$ and $H_j=\sum_{i=0}^j h_i$.

> **PROVED — complete odd punctured Cartier module.**  If
> $p=6q+1$, then
> 

$$
> \boxed{
> \begin{aligned}
> \mathcal C\omega_0&=\epsilon\omega_0+(H_q-h_q)\eta,&
> \mathcal C\omega_1&=\epsilon\omega_1,\\
> \mathcal C\omega_2&=\epsilon\omega_2,&
> \mathcal C\eta&=h_q\eta,&
> \mathcal C\xi&=0.
> \end{aligned}}
> \tag{1.4}
>
$$


> If $p=6q+5$, then
> 

$$
> \boxed{
> \begin{aligned}
> \mathcal C\omega_0&=\epsilon\omega_1,&
> \mathcal C\omega_1&=\epsilon\omega_0+H_q\eta,\\
> \mathcal C\omega_2&=\epsilon\omega_2,&
> \mathcal C\eta&=0,&
> \mathcal C\xi&=-h_q\eta.
> \end{aligned}}
> \tag{1.5}
>
$$



The Item-261 logarithmic class for $p\equiv1\pmod6$ is
$-3\omega_0$.  The Item-260 logarithmic class for
$p\equiv5\pmod6$ is $\omega_1$.  In particular,



$$
\mathcal C^2\omega_1=\omega_1\qquad(p\equiv5\pmod6).           \tag{1.6}
$$



This is a genuine fixed order-two relation on the *cohomology class*, but
it is not a scalar relation on the finite punctured period: the finite
endpoint functional does not descend to de Rham cohomology.

> **PROVED — the two moving coordinates occur as Cartier matrix
> coefficients.**  On the $p\equiv1$ phase, the noncompact extension
> coefficient in (1.4) is
> 

$$
> \lambda_1=H_{q-1}=H_q-h_q.                                   \tag{1.7}
>
$$


> On the $p\equiv5$ phase, the corresponding coefficient in (1.5) is
> 

$$
> \lambda_5=H_q.                                                \tag{1.8}
>
$$


> The remaining nonzero compact coefficient is $h_q$, which is a
> $p$-unit on every actual row.  Hence the exact punctured Frobenius
> matrix contains, rather than constrains, the same unresolved pair
> $(H_q,h_q)$.

> **PROVED — exact endpoint dictionary.**  For the two finite normal forms
> of Items 260–261, let $U_p$ denote the surviving compact/second-kind
> coordinate and $V_p$ the logarithmic coordinate.  Then
> 

$$
> \begin{array}{c|c|c|c}
> p\pmod6&U_p&V_p&\lambda\\ \hline
> 1&-h_q/5-\epsilon&-H_q+2\epsilon/3
>   &-V_p+5U_p+17\epsilon/3\\[2mm]
> 5&h_q-\epsilon&-H_q+4\epsilon/3
>   &-V_p+4\epsilon/3.
> \end{array}                                                   \tag{1.9}
>
$$


> Thus adjoining every endpoint restores exactly $(H_q,h_q)$; it does
> not create a third, independent condition.

> **PROVED, SHARPLY SCOPED FROBENIUS OBSTRUCTION.**  The characteristic
> polynomials of (1.4) and (1.5) are respectively
> 

$$
> T(T-\epsilon)^3(T-h_q),
> \qquad
> T^2(T-\epsilon)(T^2-1).                                      \tag{1.10}
>
$$


> Hence scalar trace/determinant data see no $H_q$ at all.  The extension
> entry that does see it is exactly the original moving prefix.  Moreover,
> the endpoint functional is nonzero on exact differentials for every
> actual prime in both phases.  Consequently the residue action, compact
> Frobenius data, and exact endpoint augmentation yield no new fixed
> scalar/unit relation beyond the cutoff identity.

This no-go is intentionally scoped.  It does not assert that every
possible crystalline, $p$-adic, or automorphic method must fail.  It
rules out the natural shortcut that treats the finite punctured sum as a
Frobenius-equivariant functional of the de Rham class.

> **NO ALL-PRIME EXCLUSION / ZERO BOOKING.**  Actual zeros remain in both
> phases:
> 

$$
> (p,r,s,m,\delta)=(43,11,3,2,5),\qquad(47,7,5,4,3).             \tag{1.11}
>
$$


> Therefore Item 263 books
> 

$$
> \boxed{\text{new unconditional Route-1 rate}=0,
> \qquad\text{new ordinary-\(j=2\) capacity reduction}=0.}      \tag{1.12}
>
$$



Every bounded scan in the checker is **EXACT FINITE ONLY**.

## 2. Residues and geometric Frobenius

At $P_{\alpha,\beta}=(\alpha,\beta)\in D$,



$$
\boxed{\operatorname {Res}_{P_{\alpha,\beta}}\omega_a
 ={\alpha^{a-2}\over3\beta}.}                                 \tag{2.1}
$$



The six points occur in three pairs exchanged by $Z\mapsto-Z$.  An odd
residue vector has the form



$$
e_k(\alpha,\beta)={\alpha^k\over\beta},\qquad k=0,1,2,         \tag{2.2}
$$



and automatically has total residue zero.  These three characters form a
basis of the odd residue quotient.  Since



$$
\alpha^p=\alpha^{p\bmod3},\qquad
 \beta^p=\beta(1/2)^n=\epsilon\beta,                            \tag{2.3}
$$



geometric Frobenius sends



$$
(\alpha,\beta)\longmapsto(\alpha^p,\epsilon\beta).             \tag{2.4}
$$



Cartier takes a logarithmic residue to its $p$-th root.  Therefore



$$
\boxed{\mathcal C(e_k)=\epsilon e_{k p^{-1}\bmod3}.}           \tag{2.5}
$$



For $p\equiv1\pmod6$, all three characters are $\epsilon$-eigenvectors.
For $p\equiv5\pmod6$, $e_0$ is an $\epsilon$-eigenvector and
$e_1,e_2$ are exchanged with multiplier $\epsilon$.  This proves the
residue part of (1.4)–(1.5).

## 3. Exact Cartier calculation

For a rational function $f(X)$, the hyperelliptic Cartier formula is



$$
\mathcal C\left(f(X){dX\over Z}\right)
 ={1\over Z}\,\mathcal C_{\mathbf P^1}\left(f(X)g(X)^n,dX\right).
 \tag{3.1}
$$



Put $v=X^3$.  Polynomial division gives the coefficientwise identity



$$
{g(X)^n\over X^3-1}
 ={(1/2)^n\over X^3-1}+Q_n(X^3),
 \quad
 Q_n(v)={(v-1/2)^n-(1/2)^n\over v-1}.                           \tag{3.2}
$$



Euler's criterion gives $(1/2)^n=\epsilon$.  The proper rational part
of (3.2), together with (2.5), produces the logarithmic term in
(1.4)–(1.5).  For the polynomial part, use



$$
\mathcal C_{\mathbf P^1}\left(\sum_e a_eX^e,dX\right)
 =\sum_{j\ge0}a_{pj+p-1}X^j,dX.                               \tag{3.3}
$$



When $p=6q+1$, $n=3q$ and
$\deg_X(X^aQ_n(X^3))\le9q-1<2p-1$.  The sole possible selected
exponent is $p-1=6q$, and its congruence modulo three forces $a=0$.
Its coefficient is



$$
\begin{aligned}
 [v^{2q}]Q_n(v)
 &=\sum_{k=2q+1}^{3q}\binom{3q}{k}(-1/2)^{3q-k}\\
 &=\sum_{j=0}^{q-1}\binom nj(-1/2)^j
 \equiv\sum_{j=0}^{q-1}h_j=H_{q-1}\pmod p.                    \tag{3.4}
 \end{aligned}
$$



When $p=6q+5$, $n=3q+2$ and the same degree argument leaves only
$p-1=6q+4$; its congruence forces $a=1$.  Now



$$
[v^{2q+1}]Q_n(v)
 =\sum_{j=0}^{q}\binom nj(-1/2)^j
 \equiv H_q\pmod p.                                            \tag{3.5}
$$



In both equations we used $n\equiv-1/2\pmod p$, so



$$
\binom nj(-1/2)^j\equiv{(1/2)_j\over j!2^j}=h_j.              \tag{3.6}
$$



Applying (3.3) directly to $g^n dX$ and $Xg^n dX$ gives



$$
\begin{array}{c|cc}
 p\pmod6&\mathcal C\eta&\mathcal C\xi\\ \hline
 1&\binom{3q}{2q}(-1/2)^q\eta=h_q\eta&0\\[1mm]
 5&0&\binom{3q+2}{2q+1}(-1/2)^{q+1}\eta=-h_q\eta.
 \end{array}                                                    \tag{3.7}
$$



For the last equality,
$h_{q+1}/h_q=(2q+1)/(4q+4)\equiv-1\pmod p$ on the
$p=6q+5$ phase.  This completes the matrix proof.

## 4. Endpoint functional does not descend

For $p=6q+5$, Item 260's exact differential operator is



$$
\mathcal L(R)=gR'+{3\over2}X^2R,
 \qquad \mathcal L(R){dX\over Z}=d(RZ).                         \tag{4.1}
$$



Its finite functional satisfies, for $j\equiv1\pmod3$ in the actual
phase range,



$$
\Lambda_p(\mathcal L(X^{-j}))=\epsilon{j-3\over2}.             \tag{4.2}
$$



Already $j=1$ gives $-\epsilon\ne0$ for every actual prime.
Therefore even the order-two class identity (1.6) cannot be evaluated by
simply applying $\Lambda_p$.

For $p=6q+1$, Item 261's Kummer differential operator gives



$$
\Lambda_p(\mathcal D(R_j))
 =-{3h_{q-j+1}\over2(3j-1)}-\epsilon{3j-1\over6},
 \qquad0\le j<q.                                                \tag{4.3}
$$



On this phase $h_{q+1}=h_q/5$.  If $d_j$ denotes the right-hand side
of (4.3), direct simplification yields



$$
30d_0+12d_1=\epsilon.                                         \tag{4.4}
$$



Hence at least one of two exact differentials has nonzero finite
endpoint for every actual $p\equiv1\pmod6$ row.  This is an all-prime
obstruction to treating the finite sum as a functional on de Rham
cohomology, not a statistical observation.

Combining (4.2)–(4.3) with the direct finite evaluations gives (1.9).
The apparent extra Frobenius extension coefficient is therefore precisely
the old logarithmic period.

## 5. Cutoff and full Item-251 affine gate

The two phases share the exact cutoff form



$$
m=q-\delta,\qquad H_m=H_q-K_\delta h_q.                         \tag{5.1}
$$



All coefficients in the following table depend only on the fixed row
parameter $r$:



$$
\begin{array}{c|c|c|c|c}
p\pmod6&\delta&r&c_{j+1}/c_j&\Pi_r\\ \hline
1&(r+4)/3&3\delta-4&(6j+1)/(3j+2)&
\displaystyle\sum_{k=1}^{r+2}2^{-k}{(1/3-\delta)_k\over(1/2)_k}\\[3mm]
5&(r+2)/3&3\delta-2&(6j+5)/(3j+4)&
\displaystyle\sum_{k=1}^{r+2}2^{-k}{(-1/3-\delta)_k\over(1/2)_k}.
\end{array}                                                     \tag{5.2}
$$



Here $c_0=1$, $K_\delta=\sum_{j=0}^{\delta-1}c_j$, and



$$
{h_m\over h_q}=c_\delta.                                      \tag{5.3}
$$



Set



$$
D_r=K_\delta+c_\delta\Pi_r.                                  \tag{5.4}
$$



Then Item 251's integer period, in both phases, is



$$
\boxed{A_s=(-1)^m\{\epsilon[H_q-D_rh_q]-1\}\pmod p.}          \tag{5.5}
$$



Consequently the surviving quantity



$$
Z=B_s\left({9\kappa_r\over2}A_s-\tau_{r,s}\right)             \tag{5.6}
$$



and each affine gate $G_\nu=f_\nu Z+U_\nu$ remain explicit affine
functions of the same two states $(H_q,h_q)$.  Equations
(1.4)–(1.5) do not add an independent equation for them and do not remove
Item 251's separate $f_0=f_1=0$ branch.

## 6. Unit and boundary audit

On actual $p=6q+1$ rows, $q\ge\delta\ge3$, with $\delta$ odd.
On actual $p=6q+5$ rows, $q\ge\delta\ge1$, again with $\delta$
odd.  The following bounds cover every division above:

* $p\ge5$, so $2$ and $3$ are units.
* In $h_q$, $0\le j<q$ gives
  $1\le2j+1<p$ and $1\le4(j+1)<p$ on every actual row.
  Thus $h_q\ne0\pmod p$.
* In (4.3), $0\le j<q$ gives $|3j-1|<p$, so the endpoint
  denominator is a unit.
* For $p\equiv1$, $d=r+2=3\delta-2$ and
  $2d-1=6\delta-5<p$.
* For $p\equiv5$, $d=r+2=3\delta$ and
  $2d-1=6\delta-1<p$.

The last two inequalities prove that every denominator in $(1/2)_k$
in (5.2) is a $p$-unit.  The recurrence denominators
$3j+2$ and $3j+4$ are smaller still.  For $p\equiv5\pmod6$, the
cube map on $\mathbf F_p$ is bijective, so the only rational zero of
$X^3-1$ is the explicitly omitted endpoint $X=1$.

No denominator or omitted puncture is hidden in the matrix calculation.

## 7. Why no scalar/unit shortcut survives

For $p\equiv1\pmod6$, one might try to split the triangular block in
(1.4) by dividing by $h_q-\epsilon$.  This is not an all-prime unit:



$$
p=19,\quad q=3,\quad h_q=18=\epsilon,\quad H_q-h_q=15\pmod{19}.
 \tag{7.1}
$$



Thus the block can become genuinely resonant.  For $p\equiv5\pmod6$,
even the extension coefficient itself can vanish:



$$
p=83,\quad q=13,\quad H_q=0,\quad h_q=22\pmod{83}.             \tag{7.2}
$$



These are exact witnesses, not heuristic samples.  They prohibit the two
first natural universal unit divisions.  More fundamentally, (1.7)–(1.9)
show that retaining the extension entry merely retains the moving prefix.

The exact finite scan through $p\le401$ checked:

* 77 prime phases and every polynomial-division/Cartier coefficient;
* 1,150 $p\equiv1$ endpoint identities and 1,192
  $p\equiv5$ endpoint identities;
* 1,153 actual cutoff rows and all 1,153 corresponding Item-251 period
  formulas;
* the actual cutoff zeros in (1.11), together with two further
  $p\equiv1$ zeros in that finite window.

This scan is **EXACT FINITE ONLY** and supports no density claim.

## 8. Reproduction and booking decision

Run the standard-library checker twice.  It independently constructs the
quotient in (3.2), applies coefficient-level Cartier selection, evaluates
the finite endpoint sums, verifies the cutoff and Item-251 identities,
and reproduces byte-identical certificates.

The theorem delivered by this item is the exact five-dimensional odd
Cartier module and the all-prime endpoint non-descent obstruction.  It is
not an all-prime exclusion and proves no weighted zero rate.  The booking
decision is therefore strictly zero.
