> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 228 — a second Frobenius condition for the off-diagonal $j=1$ cell

Date: 2026-08-31

## 1. Scope and verdict

Retain the complete Item 223 parameterization



$$
p=2r+6s+3,\qquad r=2h,\qquad h,s\geq1,              \tag{1.1}
$$



and put



$$
\epsilon=(-1)^{(p-1)/2}=(-1)^{s+1},\qquad
 W=(1-z)^r(1+z^2)^{2s-1}.                            \tag{1.2}
$$



Item 223 proves that every original common-log collision must satisfy



$$
\Delta_+=2\Delta_-\ne0\pmod p.      \tag{1.3}
$$



It also excludes the whole diagonal $r=2s$.  Item 228 continues the
same boundary moments through the next Frobenius pole.

**PROVED — an exact regularized recurrence.**  Delete from each primitive
moment exactly the monomials whose primitive denominator is divisible by
$p$.  The Item 223 Pearson recurrence then acquires a finite, explicit
forcing equal to the negative of the deleted derivative contributions.

**PROVED — the next source is $+2\epsilon$.**  The next pole occurs at
the exact multiplier $3p$.  In the unreduced moment its unique pole term
is $\ell_{3p-1}/(3p)$, so



$$
p u_{T+p+3}\equiv{\ell_{3p-1}\over3}
 ={2\epsilon\over3}\pmod p.                         \tag{1.4}
$$



Equation (1.4) is a statement **before** regularization.  The pole monomial
is absent from the regularized moment; its deleted derivative contribution,
or equivalently multiplication of (1.4) by the exact multiplier $3p$,
produces the terminal source $+2\epsilon$.

**PROVED — the first-resonance freedom dies before the next pole.**  The
free mode introduced after the $2p$ terminal has generating polynomial
exactly $W$.  Since



$$
\deg W=r+4s-2<p-3,                 \tag{1.5}
$$



its three entries in the $3p$ terminal covector vanish identically.

**PROVED — a second necessary invariant.**  Exact forced propagation
defines two canonical scalars $\rho_0,\rho_1$.  Every original collision
must satisfy (1.3) and



$$
\boxed{\Psi_{p,r,s}:=
 \Delta_+(\rho_0-2\epsilon)-4\epsilon\rho_1=0\pmod p.}          \tag{1.6}
$$



This is a necessary condition only.  No sufficiency or equivalence is
claimed.

**EXACT FINITE ONLY.**  The 22 corrected Item 223 transfer survivors with
$p\leq2000$ all have $\Psi\ne0$.  Thus no simultaneous
$\Theta=\Psi=0$ row remains through that bound, where
$\Theta=\Delta_+-2\Delta_-$.  This is not extrapolated.

**OPEN.**  No all-prime exclusion or weighted bound for simultaneous zeros
of $(\Theta,\Psi)$ is proved.  The actual new Route-1 linear rate and
divisibility exponent remain zero.

## 2. Boundary moments and monomial weights

Item 223 uses the boundary functional



$$
\mathcal L_\epsilon(f)=
 (2\epsilon-i)\int_0^{-i}f(z)\,dz
 +(2\epsilon+i)\int_0^if(z)\,dz.                    \tag{2.1}
$$



For a monomial,



$$
\mathcal L_\epsilon(z^q)={\ell_q\over q+1},\qquad
 \ell_q=(2\epsilon-i)(-i)^{q+1}+(2\epsilon+i)i^{q+1}.           \tag{2.2}
$$



Since $i^p=\epsilon i$, the weights at successive Frobenius multiples
are



$$
\begin{array}{c|rrrr}
a\bmod4&1&2&3&0\\ \hline
\ell_{ap-1}&-2\epsilon&-4\epsilon&2\epsilon&4\epsilon.
\end{array}                                                     \tag{2.3}
$$



Put $n_*=p+r$ and



$$
u_t=\mathcal L_\epsilon(z^{n_*+t}W).       \tag{2.4}
$$



The collision pair is equivalent at its initial section to



$$
(u_0,u_1,u_2)=\lambda(1,1,-1).        \tag{2.5}
$$



No denominator in (2.5) is divisible by $p$, so regularization below
does not change this line.

## 3. Exact regularization and the forcing sign

Let



$$
\sigma=(1-z)(1+z^2)                       \tag{3.1}
$$



and, for every integer $t$, set



$$
K_t=z^{p+r+t+1}\sigma W.                   \tag{3.2}
$$



Define $\widehat{\mathcal L}_\epsilon$ on monomials by



$$
\widehat{\mathcal L}_\epsilon(z^q)=
 \begin{cases}
 \ell_q/(q+1),&p\nmid q+1,\\
 0,&p\mid q+1,
 \end{cases}                                                    \tag{3.3}
$$



and put 

$$
\widehat u_t=\widehat{\mathcal L}_\epsilon
(z^{p+r+t}W)
$$

.  This deletes exactly the pole monomials and makes every
$\widehat u_t$ $p$-integral.

The exact Item 223 Pearson identity is



$$
B_tu_t-C_tu_{t+1}+D_tu_{t+2}-A_tu_{t+3}=0,          \tag{3.4}
$$



where



$$
\begin{aligned}
A_t&=p+2r+4s+t+2,&B_t&=p+r+t+1,\\
C_t&=p+2r+t+2,&D_t&=p+r+4s+t+1.                      \tag{3.5}
\end{aligned}
$$



Indeed, the left side of (3.4) is
$\mathcal L_\epsilon(K_t')$, and the endpoint values of $K_t$ vanish
at $0,i,-i$.  For
$K_t=\sum_q k_qz^q$, the full derivative integral is



$$
\sum_qk_q\ell_{q-1}=0.                 \tag{3.6}
$$



Regularization keeps the terms with $p\nmid q$ and deletes those with
$q=ap$.  Therefore (3.4) becomes the exact congruence



$$
\boxed{\begin{aligned}
B_t\widehat u_t-C_t\widehat u_{t+1}
 +D_t\widehat u_{t+2}-A_t\widehat u_{t+3}
 =-\sum_{a\geq1}[z^{ap}]K_t\,\ell_{ap-1}\pmod p.
\end{aligned}}                                                   \tag{3.7}
$$



The minus sign in (3.7) is forced by moving the deleted terms in (3.6)
to the retained side.  It is not a convention inferred from finite data.

There is a second exact sign check on the entire $2p$ band.  Write
$W=\sum_kw_kz^k$ and



$$
R_t=-2\epsilon\,w_{p-r-t-1},                         \tag{3.8}
$$



with coefficients outside the support taken as zero.  Before
regularization the unique $2p$-pole part is $R_t/p$, so
$u_t=\widehat u_t+R_t/p$.  Substitution in (3.4) gives



$$
f_t={B_tR_t-C_tR_{t+1}+D_tR_{t+2}-A_tR_{t+3}\over p}.          \tag{3.9}
$$



The coefficient Pearson recurrence for $W$ proves that the numerator
in (3.9) is divisible by $p$, and simplifies it to



$$
f_t=2(R_t-R_{t+1}+R_{t+2}-R_{t+3}).                \tag{3.10}
$$



Equation (3.4) then gives the regularized forcing $-f_t$, exactly
agreeing with (3.7).  At the first terminal, (3.10) equals
$+4\epsilon$, so the retained recurrence has source
$-4\epsilon$, as required by Item 223.

## 4. The $2p$ and $3p$ terminal sources

Set



$$
T=2s+1.                \tag{4.1}
$$



The degree of $\sigma W$ is $r+4s+1$, and its leading coefficient is
$-1$, because $r$ is even.  For $t<T$, the support of $K_t$
contains no exponent divisible by $p$.  At $t=T$, its top exponent is
$2p$.  Thus (3.7) has the first terminal source



$$
-(-1)\ell_{2p-1}=-4\epsilon.            \tag{4.2}
$$



The exact multiplier is



$$
A_T=2p.                \tag{4.3}
$$



After one complete prime-length transfer, at



$$
T_2=T+p,                \tag{4.4}
$$



the top exponent of $K_{T_2}$ is $3p$, again with coefficient
$-1$.  Equations (2.3) and (3.7) give



$$
-(-1)\ell_{3p-1}=+2\epsilon,            \tag{4.5}
$$



while the exact multiplier is



$$
A_{T_2}=3p.              \tag{4.6}
$$



To audit the multiplicity without regularization, consider the actual
rational moment $u_{T_2+3}$.  Its leading $W$-monomial has exponent
$3p-1$, coefficient 1, and primitive denominator $3p$.  Every other
denominator is a $p$-unit.  Hence



$$
p u_{T_2+3}\equiv{\ell_{3p-1}\over3}
 ={2\epsilon\over3}\pmod p.                         \tag{4.7}
$$



Multiplying (4.7) by the factor 3 in $A_{T_2}=3p$ recovers exactly
$+2\epsilon$.  The companion checker verifies the unreduced rational
identity



$$
B_{T_2}u_{T_2}-C_{T_2}u_{T_2+1}+D_{T_2}u_{T_2+2}
 =3p\,u_{T_2+3}                                      \tag{4.8}
$$



on every actual row in its declared source grid.  Thus the coefficient
3, the sign, and the distinction between pre- and post-regularization
statements are all checked directly.

## 5. The first-pole free mode

At $t=T$, the reduced leading coefficient vanishes and
$\widehat u_{T+3}$ is free after the terminal compatibility is imposed.
Let $x_n$ be the coefficient of this freedom in
$\widehat u_{T+3+n}$, with



$$
x_{-2}=x_{-1}=0,\qquad x_0=1.          \tag{5.1}
$$



For $n\geq0$, the homogeneous recurrence obtained from (3.4) is



$$
(n+1)x_{n+1}=(n-r)x_n+(4s-n-1)x_{n-1}
                  +(n-r-4s)x_{n-2}.                 \tag{5.2}
$$



On the other hand, direct logarithmic differentiation gives



$$
\sigma W'=\bigl(-r+(4s-2)z-(r+4s-2)z^2\bigr)W.     \tag{5.3}
$$



Coefficient extraction from (5.3) is precisely (5.2), with the initial
values (5.1).  Therefore



$$
\sum_{n\geq0}x_nz^n=W(z).              \tag{5.4}
$$



The second terminal covector uses the free-mode indices
$p-3,p-2,p-1$.  But



$$
(p-3)-\deg W
 =2r+6s-(r+4s-2)=r+2s+2>0.                         \tag{5.5}
$$



All three entries therefore vanish as ordinary integer coefficients, not
merely after numerical reduction modulo $p$.

## 6. Construction of the second invariant

Propagate triples recording the constant forced part, the initial
$\lambda$-coefficient, and the first-pole free coefficient.  Start with



$$
\widehat u_0=(0,1,0),\quad
 \widehat u_1=(0,1,0),\quad
 \widehat u_2=(0,-1,0).                              \tag{6.1}
$$



For $0\leq t<T$, the reduced pivot is a unit.  At $t=T$, the terminal
covector is



$$
(0,\Delta_+,0),         \tag{6.2}
$$



and (4.2) imposes



$$
\lambda\Delta_+=-4\epsilon.            \tag{6.3}
$$



Set the new free state $\widehat u_{T+3}=(0,0,1)$ and propagate (3.7)
for $T<t<T+p$.  Every pivot is a unit because



$$
A_t\equiv t-T\pmod p.          \tag{6.4}
$$



At $t=T_2$, the terminal triple has the canonical form



$$
(\rho_0,\rho_1,0),          \tag{6.5}
$$



where the last zero is the theorem of Section 5.  The source (4.5) requires



$$
\rho_0+\lambda\rho_1=2\epsilon.         \tag{6.6}
$$



If a collision exists, Item 223 already gives $\Delta_+\ne0$.  Eliminating
$\lambda$ between (6.3) and (6.6), without dividing in the definition,
gives exactly (1.6).

Combining the two levels, every collision satisfies



$$
\boxed{\Delta_+=2\Delta_-\ne0,
        \qquad\Psi_{p,r,s}=0\pmod p.}                \tag{6.7}
$$



There is no hidden degenerate case: if $\Delta_+=0$ or
$\Delta_-=0$, Item 223 already excludes a collision; all propagation
pivots in (6.4) are units; and $\rho_0,\rho_1$ are defined without an
inverse of either transfer scalar.  Conditions (6.7) remain necessary,
not sufficient.

## 7. Exact replay and finite evidence

The source replay covers all 479 actual rows with $p\leq251$.  On every
row it checks:

* the unreduced residue (4.7);
* the exact multiplier $3p$ and recurrence (4.8);
* the top coefficient $-1$, weight $\ell_{3p-1}=2\epsilon$, and forcing
  sign in (4.5);
* 79,759 individual $2p$-band forcing steps, comparing (3.7) with the
  unreduced subtraction (3.8)--(3.10).

The source-row stream has SHA-256
`dd18e6aecdea1271657e9ae3eaaf954a59386f426fd313b2a986ac22df051961`.
These computations replay identities already proved symbolically; their
declared finite bound is not used to extrapolate the theorem.

Separately, the exact finite census contains all 22,934 actual rows with
$p\leq2000$.  Item 223 leaves 22 rows satisfying (1.3); Item 228 finds



$$
\begin{array}{c|r}
\text{Item 223 transfer survivors}&22\\
\Psi\ne0\text{ on those survivors}&22\\
\Theta=\Psi=0&0.
\end{array}                                                     \tag{7.1}
$$



The survivor stream augmented by $(\rho_0,\rho_1,\Psi)$ has SHA-256
`d021d0bcf4ff7a9541c7666006d037aa9642116b2f59a6a9b1b764d561f9536e`.
The first three values of $(p,r,s;\Psi)$ are



$$
(223,38,24;115),
 \quad(239,40,26;51),
 \quad(311,16,46;270).                               \tag{7.2}
$$



Statements (7.1)--(7.2) are labeled **EXACT FINITE ONLY**.  In particular,
they prove neither that all future survivors are absent nor that their
prime-log weight has density zero.

## 8. Route-1 rate ledger

Conditional exclusion of the complete $j=1$ cell would remove



$$
{1\over6}\text{ per }m
                 ={1\over36}\text{ per }6m.                    \tag{8.1}
$$



Item 228 supplies a new all-row necessary invariant but no all-prime or
weighted classification of its simultaneous zeros with $\Theta$.
Therefore the currently bookable quantities are



$$
\boxed{\text{new unconditional linear log rate}=0,
        \qquad\text{new divisibility exponent}=0.}             \tag{8.2}
$$



The next rigorous target is a structural gcd, resultant, or further
Frobenius condition controlling simultaneous $\Theta=\Psi=0$, rather
than a larger finite scan.

## 9. Reproducibility and labels

From the archive root, run

```text
python scripts/item228_j1_second_frobenius_certificate.py --output results/item228_j1_second_frobenius_certificate.json
python scripts/item228_j1_second_frobenius_certificate.py --output results/item228_j1_second_frobenius_certificate.replay.json
```

The checker uses only Python 3.11+ standard-library exact integer,
`Fraction`, polynomial, and finite-field arithmetic.  It depends only on
the frozen Item 218 and Item 223 checkers named in the portable manifest.

**PROVED:** the regularized recurrence (3.7), its forcing sign, the direct
$3p$ pole residue and source (4.5)--(4.8), the free-mode identity (5.4)
and support vanishing (5.5), and the necessary implication (6.7).

**EXACT FINITE:** the source replay through $p\leq251$, and elimination
by $\Psi$ of every corrected Item 223 survivor through $p\leq2000$.

**OPEN:** all-prime exclusion or a weighted bound for simultaneous
$\Theta=\Psi=0$; sufficiency of the transfer conditions; any positive
Route-1 rate or radical saving from the $j=1$ cell; and the separate
$j=2$ classification.
