> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 219 — the fixed common-log cell $j=2$

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Stay on the normalized common-log cell



$$
4m+1=5p-2s,\qquad 1\le s\le\frac{p-3}{6},\qquad p>7,
 \tag{1.1}
$$



where $p$ is prime and $m$ is integral.  This is exactly the fixed
Item 197/217 cell $j=2$.  Put



$$
r=\frac{p-6s-3}{2},\qquad q_\nu=2s-\nu\quad(\nu=0,1).
 \tag{1.2}
$$



> **PROVED — independent fixed normalization.**  Direct expansion of the
> two rational functions in (3.2) gives
> 

$$
> J_2=(-245,70,315,-35).                              \tag{1.3}
>
$$


> Independently, the Item 197 normalization gives
> $(U_2,V_2,W_2)=(-45,-70,7)$, and hence
> 

$$
> \frac{C_\nu(m)}p=-35(9X_\nu-10Y_\nu+Y'_\nu)\pmod p. \tag{1.4}
>
$$


> The four entries in (1.3) are not identified componentwise with the
> three entries in (1.4).

> **PROVED — explicit all-prime criterion without truncated logs.**  Let
> $\chi=(-1)^{(p-1)/2}$, set
> 

$$
> P_\nu(z)=(1-z)^r(1+z)^{1+3\nu}(1+z^2)^{2s-\nu}
>          =\sum_\ell p_{\nu,\ell}z^\ell,             \tag{1.5}
>
$$


> and define
> 

$$
> S_\nu(p,s)=\sum_\ell
>   p_{\nu,\ell}\frac{W_\chi(r+\ell+1)}{r+\ell+1}\pmod p, \tag{1.6}
>
$$


> where
> 

$$
> \begin{array}{c|rrrr}
> n\bmod4&0&1&2&3\\ \hline
> W_\chi(n)&-11&9-2\chi&29&9+2\chi.
> \end{array}                                          \tag{1.7}
>
$$


> Every denominator in (1.6) lies in $[1,p-1]$, and
> 

$$
> \boxed{\frac{C_\nu(m)}p=-35(-1)^{r+1}S_\nu(p,s)\pmod p.} \tag{1.8}
>
$$


> Since $p\ge11$, the normalized common-log condition is exactly
> 

$$
>                 \boxed{S_0(p,s)=S_1(p,s)=0\pmod p.} \tag{1.9}
>
$$



> **PROVED SCOPED NO-GO — the simplest twisted Hermite reduction cannot
> close (1.9).**  A boundary-free scalar reduction below Frobenius degree
> would have
> 

$$
> d(Hf_0)=f_1-Rf_0,\qquad
> H=\frac{c_0+c_1z+c_2z^2+c_3z^3}{1+z}.              \tag{1.10}
>
$$


> Six coefficient equations have augmented determinant
> 

$$
>                       2304s(2s+1)^2,                \tag{1.11}
>
$$


> a unit on every row (1.1).  Thus no such scalar reduction exists.
> This does not exclude a Frobenius-resonant $z^p$ term or a reduction
> with a genuine cohomology-basis remainder.

> **EXACT FINITE ONLY.**  The canonical replay checks all 1,153 admissible
> rows through $p\le401$.  It finds five separate $S_0$-zeros, six
> separate $S_1$-zeros, and no simultaneous zero.  Eighty-five rows
> through $p\le101$ are also reconstructed from the independent
> four-coordinate Frobenius-incidence formula.  These counts imply no
> all-prime or density statement.

> **OPEN.**  No all-prime exclusion and no finite exceptional-prime
> classification is proved for (1.9).  The problem has been reduced to a
> pair of moving finite-log, or Mirimanoff-type, beta periods; it has not
> been reduced to a fixed Fermat quotient such as $q_p(2)$.  No known
> Fermat-quotient theorem therefore finishes this cell.

The capacity consequence is sharp but conditional.  The $j=1$ and
$j=2$ cell lengths are respectively $1/6$ and $2/35$ per $m$.
If separate all-prime theorems excluded both cells, the remaining
common-log ceiling would be



$$
0.1132379841892420\ldots\quad\hbox{per }m,
 \qquad
 0.0188729973648737\ldots\quad\hbox{per }6m,          \tag{1.12}
$$



which is below
$G=0.01963298366943179388\ldots$ by
$0.0007599863045581\ldots$ per $6m$.  Item 219 proves neither
exclusion, so (1.12) is not booked.

## 2. Cell arithmetic and units

Equation (1.1) makes $m$ integral exactly when



$$
s\equiv\frac{p-1}{2}\pmod2.         \tag{2.1}
$$



Thus $s$ is even for $p\equiv1\pmod4$ and odd for
$p\equiv3\pmod4$.  Also $p\ge11$.  If $p=6k+1$, the largest
allowed $s$ is $k-1$, and if $p=6k+5$, it is $k$.  Consequently



$$
r\ge1.                       \tag{2.2}
$$



In particular the integrands used below vanish at zero.  Further,



$$
1\le r+\ell+1\le p-q_\nu-1<p                       \tag{2.3}
$$



for every coefficient occurring in (1.6).  Equations (2.2)--(2.3),
$p\ge11$, and $2s+1<p$ are the complete unit audit used here.

## 3. The two independent fixed normalizations

Put



$$
A(v)=1-3v+2v^2,\qquad D(v)=1-2v+2v^2,\qquad a=7,\quad c=5. \tag{3.1}
$$



In the four-coordinate incidence normalization, define



$$
U=\frac{A^6}{D^5},\qquad V=\frac{A^7}{D^6},
 \quad
 u_0=[v^4]U,\ u_1=[v^3]U,\ v_0=[v^4]V,\ v_1=[v^3]V. \tag{3.2}
$$



Exact series division gives



$$
(u_0,u_1,v_0,v_1)=(-35,10,-63,7),                  \tag{3.3}
$$



and hence



$$
(au_0,au_1,-cv_0,-cv_1)=(-245,70,315,-35)=J_2.    \tag{3.4}
$$



For comparison, the three Item 197 coefficient extractions give



$$
(U_2,V_2,W_2)=(-45,-70,7).       \tag{3.5}
$$



Substitution into its general separated-defect formula yields (1.4).
Equations (3.4) and (3.5) are two coordinate systems for the same scalar
quotients, not componentwise equal vectors.

For completeness, the four-coordinate moving side can be replayed as
follows.  Put



$$
L=p-2s-5,\qquad P(v)=A(v)^rD(v)^{2s-1},\qquad
 \Delta_pR=\frac{R(v)^p-R(v^p)}p\pmod p.             \tag{3.6}
$$



For $1\le t\le5$, set



$$
w_t=\bigl([v^{L+t}]\Delta_pA\,P,
 [v^{p+L+t}]\Delta_pA\,P,
 [v^{L+t}]\Delta_pD\,P,
 [v^{p+L+t}]\Delta_pD\,P\bigr).                    \tag{3.7}
$$



Then $e_{t-4}=w_t\cdot J_2$,



$$
\frac{C_0}p=e_0-2e_{-1}+2e_{-2},\qquad
 \frac{C_1}p=e_1,                                   \tag{3.8}
$$



and the equivalent common-line gate is



$$
w_4\cdot J_2=(w_3-2w_1)\cdot J_2
              =(w_2-2w_1)\cdot J_2=0.              \tag{3.9}
$$



The checker constructs (3.6)--(3.9) directly modulo $p^2$ on its
independent cross-check range.

## 4. From finite logarithms to three beta periods

Let



$$
A_p(z)=-\sum_{k=1}^{p-1}\frac{z^k}{k},\qquad
 B_p(z)=\sum_{k=1}^{p-1}\frac{(-1)^{k-1}z^{2k}}k=A_p(-z^2). \tag{4.1}
$$



The Item 197 moving moments are



$$
\begin{aligned}
 X_\nu&=[z^{p-q_\nu-1}]A_pP_\nu,\\
 Y_\nu&=[z^{p-q_\nu-1}]B_pP_\nu,\\
 Y'_\nu&=[z^{2p-q_\nu-1}]B_pP_\nu.
\end{aligned}                                         \tag{4.2}
$$



Write $d_\nu=\deg P_\nu$.  Directly,



$$
d_0=\frac{p+2s-1}{2},\qquad
 d_1=\frac{p+2s+1}{2},\qquad
 p-q_\nu-1-d_\nu=r+1.                               \tag{4.3}
$$



Moreover



$$
z^{d_\nu}P_\nu(1/z)=(-1)^rP_\nu(z).                \tag{4.4}
$$



Because all target degrees in (4.2) occur before the omitted terms of
the ordinary power series, $A_p$ and $B_p$ can be replaced there by
$\log(1-z)$ and $\log(1+z^2)$, respectively.

Work in $\mathbb F_p[i]$, with $i^2=-1$, and define the formal
polynomial antiderivatives



$$
I_\nu(\alpha)=\int_0^\alpha z^rP_\nu(z)\,dz,
 \qquad \alpha\in\{1,i,-i\}.                        \tag{4.5}
$$



All denominators are units by (2.3).  Applying (4.4) term by term gives



$$
\begin{aligned}
 X_\nu&=(-1)^{r+1}I_\nu(1),\\
 Y_\nu&=(-1)^{r+1}\{I_\nu(i)+I_\nu(-i)\},\\
 Y'_\nu&=(-1)^{r+1}\{i^pI_\nu(i)+(-i)^pI_\nu(-i)\}.
\end{aligned}                                         \tag{4.6}
$$



For the last identity, the high target changes the antiderivative
exponent from $r$ to $p+r$.  Termwise reduction modulo $p$
multiplies the endpoint value by $\alpha^p$.  Since $i^p=\chi i$,
(1.4) and (4.6) show that the relevant period is



$$
9I_\nu(1)+(-10+\chi i)I_\nu(i)
            +(-10-\chi i)I_\nu(-i).                \tag{4.7}
$$



## 5. The four-residue sum

For a monomial $p_{\nu,\ell}z^\ell$ in (1.5), put
$n=r+\ell+1$.  Its contribution to (4.7) is



$$
\frac{p_{\nu,\ell}}n
 \{9+(-10+\chi i)i^n+(-10-\chi i)(-i)^n\}.          \tag{5.1}
$$



The braces in (5.1) are exactly the four values in (1.7).  This proves
(1.6)--(1.9).  If a literal binomial sum is preferred, then



$$
\boxed{
 S_\nu=\sum_{a=0}^{r}\sum_{b=0}^{1+3\nu}
              \sum_{c=0}^{2s-\nu}
 (-1)^a\binom ra\binom{1+3\nu}{b}\binom{2s-\nu}{c}
 \frac{W_\chi(r+a+b+2c+1)}{r+a+b+2c+1}.}            \tag{5.2}
$$



This is an all-prime, denominator-audited criterion depending only on
$(p,s)$.  It is also the precise arithmetic obstruction: the two sums
move with both $p$ and $s$.  They are finite-log/Mirimanoff-type
periods, not values of one fixed Fermat quotient.

## 6. A scoped twisted-Hermite obstruction

Set



$$
f_\nu(z)=z^rP_\nu(z),\qquad
 \frac{f_1}{f_0}=\frac{(1+z)^3}{1+z^2}.              \tag{6.1}
$$



Suppose a scalar reduction



$$
d(Hf_0)=f_1-Rf_0                       \tag{6.2}
$$



has no Frobenius-degree term and its primitive vanishes at
$0,1,i,-i$.  The derivative on the right has the exact zero
multiplicities needed to show that



$$
z^r(1-z)^r(1+z^2)^{2s}\mid Hf_0.                   \tag{6.3}
$$



The right side of (6.2) has degree at most $p-2s-1$, so its
sub-$p$ primitive has degree at most $p-2s$.  The divisor in (6.3)
has degree $p-2s-3$.  Therefore (6.2) necessarily has the form (1.10).

Substitute (1.10) into



$$
H'+\frac{f'_0}{f_0}H=\frac{(1+z)^3}{1+z^2}-R,      \tag{6.4}
$$



and use $r\equiv-3s-3/2\pmod p$.  Six selected coefficient equations
have the following augmented matrix; the columns are
$(c_0,c_1,c_2,c_3,R\mid\mathrm{rhs})$:



$$
\begin{pmatrix}
-6s-3&0&0&0&0&0\\
6s+3&-6s-1&0&0&2&2\\
14s+3&6s+3&1-6s&0&2&8\\
6s+3&14s+3&6s+3&3-6s&0&10\\
0&4s+4&6s+3&14s+3&-2&-10\\
0&0&0&4s&0&-2
\end{pmatrix}.                                       \tag{6.5}
$$



Its determinant is (1.11).  Because $p\ge11$, $s\ne0$, and
$2s+1<p$, the augmented rank is six while the coefficient matrix has
only five columns.  This proves the scoped no-go.

Adding $cz^p$ to a primitive changes none of its derivatives in
characteristic $p$, but it changes its endpoint values.  Equally, a
small non-scalar cohomology remainder can carry independent periods.
Neither possibility is excluded by (6.5); labeling (6.5) as a complete
Hermite impossibility would be incorrect.

## 7. Capacity bookkeeping

The $j$-cell length per $m$ is



$$
\frac6{3j+1}-\frac4{2j+1}
 =\frac2{(3j+1)(2j+1)}.                              \tag{7.1}
$$



Thus



$$
c_1=\frac16,\qquad c_2=\frac2{35},\qquad
 c_1+c_2=\frac{47}{210}.                             \tag{7.2}
$$



The full $j\ge1$ common-log ceiling is



$$
c_{\ge1}=-4\log2+\frac\pi{\sqrt3}+3\log3-2
 =0.3370475079987658\ldots\quad\text{per }m.         \tag{7.3}
$$



Subtracting (7.2) gives (1.12).  Excluding $j=2$ alone leaves
$0.0466507751426514\ldots$ per $6m$, still above $G$.  Therefore
the useful comparison with $G$ requires independent all-prime
exclusions of both $j=1$ and $j=2$.  Those exclusions remain open at
this checkpoint.

## 8. Deterministic replay and status ledger

The standard-library checker

`scripts/item219_common_log_j2_certificate.py`

performs these exact tasks:

1. reconstructs (3.3)--(3.5) by integer series division and binomial sums;
2. verifies (4.2), (4.6), and (1.6)--(1.8) on every scanned row;
3. reconstructs (3.6)--(3.9) independently on the cross-check range;
4. expands the determinant in (6.5) as an integer polynomial in $s$;
5. records every separate finite zero and a SHA-256 digest of all rows.

The canonical and replay JSON are byte-identical.  The checker contains
no host path, timestamp, elapsed time, random seed, or non-standard
dependency.

### PROVED

- The fixed vector (1.3), the independent three-coordinate normalization,
  and the scalar formula (1.4).
- The all-prime period and residue-class criteria (1.6)--(1.9).
- The scoped sub-Frobenius scalar-Hermite obstruction (1.11).
- The conditional arithmetic comparison (1.12), with no rate booked.

### EXACT FINITE ONLY

- The 1,153-row classification through $p\le401$, its separate zeros,
  and the absence of a common zero in that finite range.
- The 85-row independent incidence cross-check through $p\le101$.

### OPEN

- All-prime nonvanishing of $(S_0,S_1)$.
- A proof that the exceptional-prime set is finite, or a classification of
  that set.
- Frobenius-resonant or non-scalar cohomological reductions strong enough
  to decide (1.9).
- The separate $j=1$ theorem required before the ceiling in (1.12) can
  be used.
- Any new Route-1 content rate or conclusion about $e+\pi$.
