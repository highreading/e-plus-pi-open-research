> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 220 — twisted de Rham reduction of the paired fixed cells

## 1. Outcome and status

This item attacks the two fixed-cell common-log conditions isolated in Item
217 by an exact Hermite/Euler reduction.  The reduction succeeds completely
at removing the finite logarithm from the interior differential.  It does
**not** prove the needed all-prime nonvanishing.

The strongest exact conclusions are these.

1. Write
   

$$
p=2r+6s+3,\qquad r\geq1.
$$


   The actual $j=1$ rows are exactly the even-$r$ rows and the actual
   $j=2$ rows are exactly the odd-$r$ rows.
2. For both moments $\nu=0,1$, the Laurent form carrying the moving weight
   is exact.  A nonresonant Euler resolvent gives an explicit primitive.
   After integration by parts, no finite-logarithm or Fermat-quotient
   coordinate remains in the interior.
3. The remaining boundary data have the common endpoint basis
   $(E_\nu,C_\nu,S_\nu)$, obtained by evaluating the Euler resolvent at
   $1,i,-i$.  The actual common-log pairs are
   

$$
\begin{array}{c|cc}
   j=1&C_0-2\epsilon S_0&2C_1+\epsilon S_1\\[1mm]
   j=2&20C_0-2\epsilon S_0-9E_0&
        2\epsilon C_1+20S_1-9E_1,
   \end{array}                                      \tag{1.1}
$$


   where $\epsilon=(-1)^{(p-1)/2}$.  Simultaneous vanishing of the
   appropriate pair is necessary and sufficient for the fixed-cell
   collision.
4. The endpoint functionals in (1.1) are genuine incomplete
   Euler/hypergeometric boundary values.  A certified one-good-prime rank
   calculation rules out every universal polynomial-coefficient linear
   relation among all six endpoint coordinates of total degree at most
   eight.  A second full-rank calculation rules out every affine Bezout
   identity
   

$$
A(r,s)H_0+B(r,s)H_1+C(r,s)=0                 \tag{1.2}
$$


   with $\deg A,\deg B,\deg C\leq8$ in total degree, separately on all
   four actual parity components.

The all-prime exclusion of either pair in (1.1) is therefore **OPEN**.
The new unconditional linear logarithmic rate and the new divisibility
exponent are both zero.  The exact reduction replaces a finite-logarithm
problem by an incomplete-endpoint problem; it does not close Route 1.

## 2. Phase parameterization and actual-cell parity

Use the notation of Item 217:


$$
P_\nu(z)=(1-z)^r(1+z)^{1+3\nu}(1+z^2)^{2s-\nu},
 \qquad \nu\in\{0,1\}.                              \tag{2.1}
$$


The prescribed row relation is


$$
4m+1=(2j+1)p-2s.                                  \tag{2.2}
$$


Substituting $p=2r+6s+3$ in (2.2) and reducing modulo four gives


$$
\begin{array}{c|c}
 j=1&4m+1\equiv2r+1\pmod4,\\
 j=2&4m+1\equiv2r+3\pmod4.
 \end{array}
$$


Thus $j=1$ requires $r$ even and $j=2$ requires $r$ odd.  Put


$$
\epsilon=(-1)^{(p-1)/2}=(-1)^{r+s+1},\qquad
 \delta=(-1)^s.                                    \tag{2.3}
$$


On the actual $j=1$ component $\delta=-\epsilon$; on the actual
$j=2$ component $\delta=\epsilon$.

The two moving weights differ by the promised rational twist


$$
\frac{P_1}{P_0}=\frac{(1+z)^3}{1+z^2}. \tag{2.4}
$$



## 3. Exact Euler primitive

Set


$$
d_\nu=\deg P_\nu=r+1+\nu+4s,
 \qquad N_\nu=2p-2s+\nu-1.                         \tag{3.1}
$$


If $P_\nu(z)=\sum_{k=0}^{d_\nu}p_{\nu,k}z^k$, define


$$
V_\nu(z)=\sum_{k=0}^{d_\nu}
              \frac{p_{\nu,k}}{N_\nu-k}z^k.       \tag{3.2}
$$


The denominators are units modulo every actual row prime.  Indeed,


$$
N_\nu-d_\nu=3r+6s+4=p+r+1>p,
 \qquad N_\nu\leq2p-2.                             \tag{3.3}
$$


Consequently


$$
p<N_\nu-k<2p\qquad(0\leq k\leq d_\nu),     \tag{3.4}
$$


so no $N_\nu-k$ is zero modulo $p$.  More strongly,


$$
N_\nu-p=d_\nu+r+1>d_\nu,                         \tag{3.5}
$$


which is the coefficient-window nonresonance used below.

Coefficientwise, (3.2) gives


$$
(N_\nu-z\partial_z)V_\nu=P_\nu.             \tag{3.6}
$$


Equivalently, the Laurent form is exact:


$$
P_\nu(z)z^{-N_\nu-1}\,dz
       =-d\!\left(z^{-N_\nu}V_\nu(z)\right).       \tag{3.7}
$$


This is the smallest de Rham statement in the present branch: the class of
the moving base form itself is zero.  The obstruction survives only through
the endpoint terms created after the finite-log kernel is differentiated.

## 4. Differentiating the two finite-log kernels

Retain Item 217's finite polynomials


$$
A_p(z)=-\sum_{k=1}^{p-1}\frac{z^k}{k},\qquad
 B_p(z)= \sum_{k=1}^{p-1}\frac{(-1)^{k-1}z^{2k}}k. \tag{4.1}
$$


Combine the low and high coefficient extractions into


$$
L_1=(2-z^p)B_p,\qquad
 L_2=9z^pA_p+(1-10z^p)B_p.                         \tag{4.2}
$$


Then


$$
H_{1,\nu}=[z^{N_\nu}]L_1P_\nu=2Y'_\nu-Y_\nu,
 \quad
 H_{2,\nu}=[z^{N_\nu}]L_2P_\nu
       =9X_\nu-10Y_\nu+Y'_\nu.                   \tag{4.3}
$$


By (3.7) and residue integration by parts,


$$
\boxed{
 H_{j,\nu}=\operatorname {Res}_{z=0}
       L'_j(z)z^{-N_\nu}V_\nu(z)\,dz.}            \tag{4.4}
$$



In characteristic $p$,


$$
A'_p=-\frac{1-z^{p-1}}{1-z},\qquad
 B'_p=2z\frac{1-z^{2p-2}}{1+z^2},                 \tag{4.5}
$$


and $(z^p)'=0$.  Hence


$$
\begin{aligned}
L'_1={}&2(2-z^p)z\frac{1-z^{2p-2}}{1+z^2},\\
L'_2={}&-9z^p\frac{1-z^{p-1}}{1-z}
 +2(1-10z^p)z\frac{1-z^{2p-2}}{1+z^2}.            \tag{4.6}
\end{aligned}
$$


Both displayed quotients are polynomials.  Formula (4.6) is the decisive
Hermite step: the truncated logarithm has vanished exactly.  There is no
residual finite-logarithm or Fermat-quotient coordinate to estimate.

## 5. The common endpoint basis and the two exact pairs

Write


$$
\begin{aligned}
 E_\nu&=V_\nu(1)
       =\sum_k\frac{p_{\nu,k}}{N_\nu-k},\\
 C_\nu&=\sum_h(-1)^h
       \frac{p_{\nu,2h}}{N_\nu-2h},\\
 S_\nu&=\sum_h(-1)^h
       \frac{p_{\nu,2h+1}}{N_\nu-2h-1}.
                                                               \tag{5.1}
\end{aligned}
$$


Thus $V_\nu(i)=C_\nu+iS_\nu$, while $V_\nu(-i)=C_\nu-iS_\nu$.
The nonresonance window (3.5) lets each geometric quotient in (4.6) see
the entire matching parity part of $V_\nu$.  Direct coefficient extraction
from (4.4) gives


$$
\begin{aligned}
H_{1,0}&=2\delta(\epsilon C_0-2S_0),&
H_{1,1}&=2\delta(2C_1+\epsilon S_1),\\
H_{2,0}&=-9E_0+2\delta(10\epsilon C_0-S_0),&
H_{2,1}&=-9E_1+2\delta(C_1+10\epsilon S_1).
                                                               \tag{5.2}
\end{aligned}
$$


Using the actual parity identities following (2.3), and discarding only
nonzero phase scalars, (5.2) becomes exactly (1.1).

The three endpoint evaluations are independent as universal polynomial
functionals.  On $V=1,z,z^2$, the $(E,C,S)$-evaluation matrix is


$$
\begin{pmatrix}1&1&0\\1&0&1\\1&-1&0\end{pmatrix},
 \qquad \det=2.                                    \tag{5.3}
$$


Thus for odd primes a common universal endpoint reduction cannot use fewer
than three coordinates.  This minimality statement is for arbitrary
polynomial inputs; it does not by itself prove minimality on the restricted
actual family $V_\nu(r,s)$.

There is a tempting formal coupling of the two cells.  For $\nu=0$, their
covectors in the $(E,C,S)$ basis are


$$
(0,1,-2\epsilon),\quad(-9,20,-2\epsilon),          \tag{5.4}
$$


whose $(E,C)$-minor is $9$.  For $\nu=1$, they are


$$
(0,2,\epsilon),\quad(-9,2\epsilon,20),             \tag{5.5}
$$


whose corresponding minor is $18$.  These prove formal independence for
$p>3$, but they do **not** give a same-row determinant obstruction: the
first row is actual only for even $r$, and the second only for odd $r$.
The cells occupy disjoint phase components.  This is the exact scoped reason
the attractive $9$ and $18$ Bezout minors cannot close the argument.

## 6. Certified bounded-ansatz no-go

The certificate evaluates the rational endpoint sums over the auxiliary
prime


$$
\ell=1,000,000,007.         \tag{6.1}
$$


Every division used by the rank matrices is explicitly audited.

For the six-coordinate linear-contiguity ansatz, the sample grid is
$1\leq r,s\leq18$.  It contains $324$ rows and
$6\binom{8+2}{2}=270$ columns.  Across the two values of $\nu$, the
checker inspects all $32,400$ denominators; they are integers in
$[13,258]$, and none is zero modulo $\ell$.  The matrix rank is exactly
$270$ modulo $\ell$.

For (1.2), there are $3\binom{8+2}{2}=135$ columns.  The actual $r$
parity and the $s$ parity are separated so that $\epsilon$ is constant
on each block.  On $1\leq r,s\leq33$, the audited results are


$$
\begin{array}{c|r|r|r|c}
\text{block}&\text{rows}&\text{columns}&\text{rank mod }\ell&
 \text{audited denominators}\\ \hline
j=1,\ s\equiv0&256&135&135&44,800\text{ in }[22,454]\\
j=1,\ s\equiv1&272&135&135&47,600\text{ in }[16,464]\\
j=2,\ s\equiv0&272&135&135&47,600\text{ in }[19,458]\\
j=2,\ s\equiv1&289&135&135&50,575\text{ in }[13,468].
\end{array}                                        \tag{6.2}
$$


Again, every audited denominator is nonzero modulo $\ell$.

Here is why one good auxiliary prime proves an exact characteristic-zero
no-go.  A rational identity in either stated ansatz supplies a rational null
vector for its rational sample matrix.  Clear its coefficient denominators
and divide by the gcd to obtain a nonzero primitive integer vector.  Because
every matrix-entry denominator is a unit modulo $\ell$, the rational
matrix has a well-defined reduction modulo $\ell$.  A primitive integer
vector cannot have all coordinates divisible by $\ell$, so its reduction
would be a nonzero modular null vector.  Full column rank in (6.1)--(6.2)
contradicts this.  Hence the rational nullity is exactly zero.

This theorem has a deliberately narrow scope.  It excludes:

* a polynomial-coefficient linear covector among
  $(E_0,C_0,S_0,E_1,C_1,S_1)$ of total degree at most eight; and
* an affine identity (1.2) of total degree at most eight on any actual
  parity component.

It does not exclude a higher-degree relation, a nonlinear resultant, a
relation that exists only after imposing primality of $p$, or another
genuinely arithmetic boundary theorem.

## 7. Exact interpretation and literature boundary

The residue calculation itself is elementary and self-contained.  Besser's
finite-polylogarithm framework places (4.1) among standard finite logarithm
objects, but no external functional equation is needed here: differentiation
already removes the logarithm exactly.  See [Besser, *Finite and p-adic
polylogarithms*](https://arxiv.org/abs/math/0006051).

The surviving $(E,C,S)$ values are incomplete endpoints rather than closed
periods.  This is consistent with the inhomogeneous holonomic behavior of
incomplete beta and incomplete A-hypergeometric functions described by
[Nishiyama--Takayama, *Incomplete A-Hypergeometric Systems*](https://arxiv.org/abs/0907.0745).
That general theory motivates the endpoint language but supplies no
nonvanishing theorem for (1.1).  Likewise, known work on Fermat quotients and
Mirimanoff-polynomial zeros illustrates that even ordinary finite-log zero
questions require arithmetic input; see [Grohmann, *On the Zeros of Fermat
Quotients and Mirimanoff Polynomials*](https://arxiv.org/abs/math/0604427).
No claim in this item depends on either analogy.

The precise remaining problem is therefore:


$$
\begin{array}{ll}
r\text{ even}:&
(C_0-2\epsilon S_0,\;2C_1+\epsilon S_1)\ne(0,0),\\[1mm]
r\text{ odd}:&
(20C_0-2\epsilon S_0-9E_0,\;
 2\epsilon C_1+20S_1-9E_1)\ne(0,0),                \tag{7.1}
\end{array}
$$


for every admissible row prime.  This all-prime assertion is **OPEN**.

## 8. Finite replay, kept separate from the exact no-go

The deterministic actual-row replay covers every prime $p\leq251$, every
admissible $s$, and both moments.  It compares (5.2) against the direct
Item 217 coefficient moments and quotient digits.  The counts are


$$
\begin{array}{c|r|r|r|r}
\text{cell}&\text{rows}&H_0=0&H_1=0&(H_0,H_1)=(0,0)\\ \hline
j=1&479&1&2&0\\
j=2&482&3&3&0.
\end{array}                                        \tag{8.1}
$$


Across both $\nu$'s, individual endpoint-coordinate zero counts are
$E:28$, $C:25$, and $S:69$.  These individual zeros reinforce that
no single-coordinate nonvanishing shortcut is available.

Equation (8.1) is classified **EXACT_FINITE_ONLY**.  It is bounded evidence,
not an all-prime theorem and not part of the modular full-rank proof in
Section 6.

## 9. Rate ledger

The fixed-cell masses from Item 217 are


$$
\frac16\quad(j=1),\qquad \frac2{35}\quad(j=2)
                                                              \tag{9.1}
$$


per $m$.  These two masses are exact.  If, and only if, both all-prime
exclusions in (7.1) were proved, subtracting them from the displayed
Item 217 numerical ceiling would give


$$
0.3370475079987658-\frac16-\frac2{35}
 \approx0.11323798418924199047                     \tag{9.2}
$$


per $m$, hence


$$
\approx0.01887299736487366508                     \tag{9.3}
$$


per $6m$.  This lies below the required gap
$0.01963298366943179388$ by


$$
\approx0.00075998630455812880.                    \tag{9.4}
$$


Thus paired fixed-cell exclusion remains a sufficient Route-1 target at the
displayed precision.  The proof uses the exact masses $1/6$ and $2/35$;
the decimal input and outputs in (9.2)--(9.4) are conditional numerical
bookkeeping inherited from Item 217, not a new exact transcendental identity.
Because (7.1) is open, Item 220 books no new rate and no new exponent.

## 10. Reproducibility and labels

The companion checker produces deterministic, byte-identical canonical and
replay JSON.  It verifies the Euler identity, all endpoint formulas, the
three-coordinate minimality determinant, all sampled denominator audits,
the two modular rank no-gos, the direct finite actual-row comparison, and the
rate arithmetic.

Classification:

* **PROVED:** phase parity; nonresonant exact primitive; endpoint formulas;
  universal three-endpoint minimality; degree-at-most-eight linear and affine
  no-go within the stated ansatz.
* **EXACT_FINITE_ONLY:** no paired collision on actual rows through
  $p\leq251$.
* **OPEN:** all-prime fixed-cell nonvanishing; any higher-order or arithmetic
  endpoint boundary; every positive unconditional rate or radical saving.
