> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 235 — The first Witt lift of the fixed $j=2$ Cartier terminals

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Work in the fixed $j=2$, $s\ge2$ cell



$$
4m+1=5p-2s,
 \qquad 2\le s\le\frac{p-3}{6},
 \qquad r=\frac{p-6s-3}{2}.                           \tag{1.1}
$$



The integrality condition in (1.1) makes $r$ odd, and the first row is
$(p,s)=(17,2)$.  Thus all four integers $1,2,3,4$, every denominator
displayed below other than an explicitly retained multiple of $p$, and
$4(s-1)$ are $p$-units.

This item asks what survives when the Items 224--227 terminal calculation
is lifted from $\mathbb F_p$ to



$$
R_p=\mathbb Z/p^2\mathbb Z.   \tag{1.2}
$$



The answer has two distinct parts.

> **PROVED — exact canonical $p^2$ terminal lift.**  The regularized
> finite-part moments have a literal lift to $R_p$.  At the $q$-th
> terminal, $q=1,2,3,4$, the exact equation is
> 

$$
>        \boxed{a_qY_q-qp\,x_q=(-1)^rW(qp)\pmod {p^2}.}              \tag{1.3}
>
$$


> Here $x_q$ is the retained finite part at the resonant coordinate.
> The coefficient $-qp$ and the rational pole
> $(-1)^rz^{qp}/(qp)$ are kept over the rationals until their $q$'s
> cancel.  No division by $p$, and no accidental loss of the
> multiplicity $q$, occurs.

> **PROVED — periodicity acquires a nontrivial carry.**  The mod-$p$
> identity $\widehat T_{k+4p}=\widehat T_k$ becomes
> 

$$
> \boxed{\widehat T^{(2)}_{k+4p}-\widehat T^{(2)}_k
>       =-4p\sum_{p\nmid d_\ell}
>          g_\ell W(d_\ell)d_\ell^{-2}\pmod {p^2},}                \tag{1.4}
>
$$


> where $d_\ell=r+\ell+k+1$.  This carry is generally nonzero.

> **PROVED SCOPED NO-GO — order-four closure is a tautological carry.**
> Use the four phase-dependent lifted transfers and the corrected carry
> (1.4).  The four closure residuals are exact $R_p$-linear
> combinations of the four terminal residuals.  Consequently endpoint
> propagation through four phases supplies no new invariant beyond the
> lifted terminal rows.  Imposing zero carry would be incorrect.

> **PROVED — canonical Witt-row criterion.**  Inside this canonical
> terminal lift, once a scalar $\lambda_0$ solves all first-digit rows,
> a lift $\lambda_0+p\lambda_1$ exists exactly when a rank-one system of
> second-digit equations, or equivalently all of its $2\times2$ Witt
> minors, vanishes.  This is an exact algebraic statement about the
> lifted terminal model.

> **PROVED SCOPE BARRIER — the frozen common-log bridge does not lift
> naively.**  Item 219 identifies the integer quotient $C_\nu/p$ with
> the beta period only modulo $p$.  At
> $(p,s,\nu)=(17,2,0)$, direct integer coefficient extraction gives
> 

$$
>       C_0/p\equiv224\pmod {17^2},
>       \qquad -35(-1)^{r+1}\widehat T^{(2)}_0
>                     \equiv173\pmod {17^2}.           \tag{1.5}
>
$$


> Their difference is $51=3p$.  Hence the canonical Witt minors are
> **not yet proved necessary** for an additional digit of the original
> common-log quotient.

> **GLOBAL INTERFACE.**  An ordinary $j=2$ common-log collision means
> $p^2\mid C_0,C_1$ and forces only the already frozen mod-$p$
> terminal conditions.  It does **not** force the canonical $R_p$ rows
> of this item.  Even under the stronger multiplicity hypothesis
> $p^3\mid C_0,C_1$, implication of the canonical Witt rows remains
> OPEN because of (1.5).  No fixed-cell capacity is booked.

> **EXACT FINITE ONLY.**  The proof replay checks 74 admissible rows
> through $p\le101$.  The census through $p\le401$ contains 1,115
> rows.  The seven Item 224 rows with $\Omega=0$ all have a nonzero
> canonical second $\Omega$-digit, but they already have
> $\Psi\ne0\pmod p$, and (1.5) prevents interpreting this as an actual
> second common-log exclusion.

> **OPEN.**  A corrected endpoint functional incorporating the true
> second Frobenius digit has not been derived.  There is no all-prime
> $j=2$ exclusion, zero-rate theorem, capacity reduction, new
> divisibility exponent, or conclusion about $e+\pi$.

## 2. Exact finite parts over $R_p$

Retain the Item 224 polynomial and the Item 226 endpoint weight



$$
\begin{aligned}
 g(z)&=(1-z)^r(1+z)(1+z^2)^{2s}=\sum_\ell g_\ell z^\ell,\\
 f_0(z)&=z^rg(z),\\
 W(n)&=W_\chi(n),\qquad \chi=(-1)^{(p-1)/2},
 \end{aligned}                                                     \tag{2.1}
$$



where



$$
\begin{array}{c|rrrr}
n\bmod4&0&1&2&3\\ \hline
W(n)&-11&9-2\chi&29&9+2\chi.
\end{array}                                                        \tag{2.2}
$$



In particular,



$$
W(p),W(2p),W(3p),W(4p)=(7,29,11,-11).     \tag{2.3}
$$



Define the canonical finite part in $R_p$ by



$$
\widehat T^{(2)}_k
   =\sum_{\substack{\ell\\p\nmid r+\ell+k+1}}
      g_\ell\frac{W(r+\ell+k+1)}{r+\ell+k+1}.        \tag{2.4}
$$



Every denominator retained in (2.4) is a unit of $R_p$; every
$p$-divisible denominator is deleted before reduction.

Set



$$
K_k=z^{k+1}(1-z^4)f_0                                      \tag{2.5}
$$



and



$$
\begin{aligned}
A_0(k)&=k+r+1,& A_1(k)&=1-r,\\
A_2(k)&=4s-r-1,& A_3(k)&=1-r,\\
A_4(k)&=-(k+2r+4s+6).
\end{aligned}                                                     \tag{2.6}
$$



The rational differential identity from Item 224 is



$$
K'_k=\sum_{j=0}^4A_j(k)z^{k+j}f_0.             \tag{2.7}
$$



Integrate (2.7) over the localization $\mathbb Z_{(p)}$, deleting
exactly the primitive monomials whose denominators are divisible by
$p$, and only then reduce modulo $p^2$.  For $k\ge-r$, this gives



$$
\boxed{
 \sum_{j=0}^4A_j(k)\widehat T^{(2)}_{k+j}
   =-\sum_{a\ge1}[z^{ap}]K_k\,W(ap)\pmod {p^2}.}      \tag{2.8}
$$



The sum is finite.  This proof is not a Hensel guess: (2.8) is the
reduction of an identity with all rational poles explicitly removed.

## 3. The four exact terminals

Put



$$
k_q=(q-1)p+2s-3,
 \qquad
 Y_q=(\widehat T^{(2)}_{k_q},\ldots,
             \widehat T^{(2)}_{k_q+3})^{\mathsf T},
 \qquad x_q=\widehat T^{(2)}_{k_q+4}.                 \tag{3.1}
$$



At this index,



$$
A_4(k_q)=-qp.                \tag{3.2}
$$



The resonant primitive term before reduction is



$$
\frac{(-1)^rz^{qp}}{qp}.      \tag{3.3}
$$



Multiplying (3.2) by (3.3) gives $-(-1)^rz^{qp}$
over the rationals.  Equivalently,



$$
[z^{qp}]K_{k_q}=-(-1)^r,
 \qquad
 -[z^{qp}]K_{k_q}W(qp)=(-1)^rW(qp).                  \tag{3.4}
$$



If $a_q=(A_0(k_q),\ldots,A_3(k_q))$, equations
(2.8)--(3.4) prove (1.3).  Notice that its second-digit term is
$-qp\,x_q$; reducing (3.2) prematurely would erase it.

Between two successive terminals, write $k=k_q+t$,
$1\le t\le p-1$.  Then



$$
A_4(k)=-(qp+t),               \tag{3.5}
$$



which is a unit of $R_p$.  Thus every intervening recurrence step is
uniquely reversible or propagatable.

## 4. The lifted common line and its Witt rows

Choose the displayed rational representative of Item 224's mod-$p$
common line as the **canonical** lift



$$
v^{(2)}=\left(
 0,\ 4s-2,\ 2s-5,\
 -\frac{52s^2-36s-27}{4(s-1)}
 \right)\in R_p^4.                                    \tag{4.1}
$$



The denominator is a $p$-unit by (1.1).  This is a definition of the
canonical representative, not a claim that Item 224's $z^3$ reduction
already supplies its true second digit: that reduction used
$r\equiv-3s-\tfrac32\pmod p$.  Any $p$-carry in the actual initial
line belongs to the OPEN bridge in Section 7.

Propagate (4.1) to the first terminal using (2.8), and backward to the
lower terminal.  Denote the resulting first-terminal covector value by
$\tau^{(2)}$ and the lower value by $\beta^{(2)}$.  Within this
canonical model, the bottom equation is



$$
\beta^{(2)}\lambda=11.        \tag{4.2}
$$



Starting with $Y_1=\lambda v^{(2)}$, use (1.3) at each terminal, set
the resonant coordinate to the actual finite part $x_q$, and propagate
by the unit pivots (3.5).  This constructs five affine rows



$$
c_i\lambda=d_i\pmod {p^2}:    \tag{4.3}
$$



the bottom row and four terminal rows.  The first terminal is explicitly



$$
\tau^{(2)}\lambda=7(-1)^r+p x_1.       \tag{4.4}
$$



Accordingly, the lifted bottom--top minor is



$$
\Omega^{(2)}=
 \beta^{(2)}\{7(-1)^r+p x_1\}-11\tau^{(2)}\pmod {p^2}.             \tag{4.5}
$$



It reduces to Item 224's $\Omega$.  If $\Omega=0\pmod p$, then
$\Omega^{(2)}/p\pmod p$ is the canonical second $\Omega$-digit.

More generally, suppose $\lambda_0\in\{0,\ldots,p-1\}$ solves every
row (4.3) modulo $p$.  Define



$$
\delta_i=\frac{d_i-c_i\lambda_0}{p}\pmod p.          \tag{4.6}
$$



The quotient is integral because of the first-digit equations.  Direct
substitution of $\lambda=\lambda_0+p\lambda_1$ proves



$$
\boxed{\quad \bar c_i\lambda_1=\delta_i\pmod p
                  \quad\hbox{for every }i.\quad}      \tag{4.7}
$$



Since the first-terminal right side is the unit $7(-1)^r$, a compatible
first-digit system has coefficient rank one.  Hence (4.7) is solvable if
and only if



$$
\bar c_i\delta_j-\bar c_j\delta_i=0
              \quad\hbox{for all }i<j.                \tag{4.8}
$$



Equations (4.6)--(4.8) are the precise Witt/Hensel conditions **inside
the canonical terminal model**.  Section 7 explains why they cannot yet
be promoted to conditions on the original integer common-log quotient.

## 5. The nonperiodic $4p$ carry

For every retained denominator $d$, four-periodicity of $W$ and a
one-step inverse expansion give



$$
W(d+4p)=W(d),
 \qquad
 \frac1{d+4p}-\frac1d=-\frac{4p}{d^2}\pmod {p^2}.     \tag{5.1}
$$



The deleted-denominator set is unchanged under $d\mapsto d+4p$.
Summing (5.1) coefficientwise proves (1.4).

The carry is not a cosmetic term.  At $(p,s)=(17,2)$, $k_1=1$, and



$$
\widehat T^{(2)}_{k_1+4p}
               -\widehat T^{(2)}_{k_1}
              \equiv204=12p\not\equiv0\pmod {p^2}.   \tag{5.2}
$$



Thus a literal lift of Item 226's equation
$Y_5=Y_1$ would be false.

## 6. Why corrected order-four closure adds no invariant

Let $M_q^{(2)}$ be the homogeneous difference transfer from phase $q$
to phase $q+1$, with the resonant-coordinate difference reset to zero.
The exact coefficients in (3.5) make the four matrices phase-dependent
over $R_p$, although



$$
M_q^{(2)}\equiv M\pmod p      \tag{6.1}
$$



for Item 226's one-phase matrix $M$.  Put



$$
P^{(2)}=M_4^{(2)}M_3^{(2)}M_2^{(2)}M_1^{(2)}          \tag{6.2}
$$



and form the terminal observability matrix



$$
\mathcal K^{(2)}=
 \begin{pmatrix}
 a_1\\
 a_2M_1^{(2)}\\
 a_3M_2^{(2)}M_1^{(2)}\\
 a_4M_3^{(2)}M_2^{(2)}M_1^{(2)}
 \end{pmatrix}.                                      \tag{6.3}
$$



Modulo $p$, this is the $M$-Krylov matrix



$$
(a,aM,aM^2,aM^3)^{\mathsf T}. \tag{6.4}
$$



Item 227 proved that $N=M+ua$ has invertible observability matrix
$(a,aN,aN^2,aN^3)^{\mathsf T}$.  Replacing $M$ by the rank-one
feedback $N=M+ua$ changes successive Krylov rows by a lower unitriangular
row operation.  Therefore (6.4) is invertible.  It follows that
$\det\mathcal K^{(2)}$ is a $p$-unit, so (6.3) is invertible over
$R_p$.

Let $E\in R_p^4$ be the four terminal residuals and let $R\in R_p^4$
be the corrected closure residual: final minus initial state, minus the
actual carry (1.4).  If $D_1$ is the candidate-minus-actual initial
difference, then coefficientwise propagation gives



$$
E=\mathcal K^{(2)}D_1,
 \qquad
 R=(P^{(2)}-I)D_1.                                   \tag{6.5}
$$



Consequently



$$
\boxed{
 R=(P^{(2)}-I)(\mathcal K^{(2)})^{-1}E.}              \tag{6.6}
$$



This identity uses no determinant division by a possibly singular
closure matrix: the only inverse is the proved $p$-unit observability
matrix.  It proves that all four corrected closure rows lie in the exact
row span of the terminal equations.  Order-four endpoint control creates
only its tautological carry, not a new arithmetic invariant.

## 7. The missing bridge to the actual second common-log digit

Item 197 defines the exact integers



$$
C_\nu=[z^{4m+\nu}]
 \frac{(1-z)^{6m}(1+z)^{1+3\nu}}
      {(1+z^2)^{4m+1+\nu}}.                           \tag{7.1}
$$



Rank zero gives $p\mid C_\nu$.  The ordinary common-log condition is
$p^2\mid C_0,C_1$; an additional digit would require



$$
p^3\mid C_0,C_1.              \tag{7.2}
$$



The frozen bridge used by Items 219--227 is only



$$
\frac{C_\nu}{p}\equiv
 -35(-1)^{r+1}S_\nu\pmod p.                           \tag{7.3}
$$



There is a transparent reason that replacing $S_\nu$ by the finite
part (2.4) modulo $p^2$ is insufficient.  Put



$$
U=1-z,\quad V=1+z^2,\quad U_0=1-z^p,\quad V_0=1+z^{2p},          \tag{7.4}
$$





$$
X=\frac{U^p-U_0}{pU_0},
 \qquad
 Y=\frac{V^p-V_0}{pV_0},
 \qquad G=\frac{U^7}{V^5}.                            \tag{7.5}
$$



These are $p$-integral formal series.  Since



$$
G^p=G(z^p)(1+pX)^7(1+pY)^{-5},                       \tag{7.6}
$$



the binomial expansion through degree two gives the exact congruence



$$
\boxed{
 \frac{G^p-G(z^p)}p
 \equiv G(z^p)\left{
 7X-5Y+p(21X^2+15Y^2-35XY)
 \right}\pmod {p^2}.}                               \tag{7.7}
$$



The mod-$p$ endpoint period sees only the first digits of $7X-5Y$.
At the next digit, both the second digits of $X,Y$ and the quadratic
term in (7.7) survive.  They are absent from the naive lift (2.4).
Likewise, the mod-$p$ $z^3$ reduction fixes (4.1) only after reducing
$r$; its possible initial-line carry is not supplied by Item 224.

The smallest exact counterexample is (1.5).  In more detail, direct
integer evaluation of (7.1) gives



$$
C_0\equiv3808\pmod {17^3},
 \qquad C_0/17\equiv224\pmod {17^2},                  \tag{7.8}
$$



whereas the canonical beta lift is $173$.  Both reduce to 

$$
3\pmod
{17}
$$

, as required by (7.3), but they are different modulo $17^2$.

Thus (7.7), not the uncorrected finite part, must be translated into a
new endpoint functional before (4.7)--(4.8) can be called necessary
conditions for (7.2).  That translation is OPEN.

## 8. Exact finite census

The exact census through $p\le401$ contains 1,115 admissible $s\ge2$
rows.  The seven rows with Item 224's first-digit $\Omega=0$ are:



$$
\begin{array}{c|r|r|r}
p&s&\Psi\pmod p&\Omega^{(2)}/p\pmod p\\ \hline
23&3&15&21\\
157&4&130&80\\
193&26&79&69\\
241&4&71&87\\
311&47&185&215\\
349&50&292&69\\
397&44&230&282
\end{array}                                                        \tag{8.1}
$$



Every displayed canonical second digit is nonzero.  This is useful as a
diagnostic of the lift, but it proves no new exclusion:

1. every row in (8.1) already fails the first-digit condition
   $\Psi=0$; and
2. Section 7 proves that the canonical second digit is not yet the actual
   second common-log digit.

No asymptotic inference is drawn from this bounded census.

## 9. Reproducibility and booking

The standard-library checker
`item235_j2_witt_terminal_certificate.py` performs the following exact
tasks:

1. constructs $g$ over the integers, not merely modulo $p$;
2. checks (2.8) at every index from the lower regular range through four
   complete phases on every proof-replay row;
3. retains and verifies all four exact $qp$ multiplicities and rational
   pole cancellations;
4. verifies the four coordinates of (1.4);
5. reconstructs all lifted affine terminal and corrected closure rows;
6. reduces them to the frozen Item 226 rows and one-phase matrix;
7. proves the lifted observability determinant is a $p$-unit and checks
   (6.6) coefficientwise for both coefficients and right sides;
8. evaluates (7.1) as an exact integer to replay (7.8); and
9. reproduces the finite census (8.1).

From the archive root, the deterministic commands are

```text
python scripts/item235_j2_witt_terminal_certificate.py \
  --output results/item235_j2_witt_terminal_certificate.json
python scripts/item235_j2_witt_terminal_certificate.py \
  --output results/item235_j2_witt_terminal_certificate_replay.json
```

The outputs contain no host path, timestamp, random seed, or elapsed time.
Canonical and replay JSON are byte-identical.

### Status ledger

**PROVED**

- the exact localized $p^2$ recurrence and every $qp$ terminal;
- the harmonic $4p$ carry;
- the canonical Witt-row criterion;
- the exact redundancy of corrected order-four closure;
- the second Frobenius-defect expansion (7.7); and
- the counterexample (7.8) to the naive common-log lift.

**EXACT FINITE ONLY**

- the 74-row proof replay through $p\le101$;
- the 1,115-row census through $p\le401$; and
- the seven canonical second digits in (8.1).

**OPEN**

- turn (7.7) into a corrected endpoint/terminal functional;
- derive actual second-digit conditions forced by (7.2);
- classify their simultaneous zeros; and
- obtain any all-prime exclusion or asymptotic bound for the $j=2$
  common-log cell.

The booking is therefore



$$
\boxed{
 \text{new unconditional log rate}=0,
 \quad\text{new divisibility exponent}=0,
 \quad\text{capacity reduction}=0.}                  \tag{9.1}
$$



Item 235 proves no statement about the arithmetic nature of $e+\pi$.
