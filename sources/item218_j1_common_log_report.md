> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 218 — exact tail reduction for the normalized common-log cell $j=1$

Date: 2026-08-31

## 1. Scope and verdict

Items 197, 203, and 217 reduce the fixed cell $j=1$ to the two
simultaneous divided-coordinate conditions



$$
2Y'_\nu-Y_\nu=0\pmod p,
                 \qquad \nu=0,1.                 \tag{1.1}
$$



This item attacks (1.1), including every admissibility condition from the
PNT row.

**PROVED — exact all-row reduction.**  Every admissible row has unique
integers $h,s\geq1$ with



$$
p=4h+6s+3,\qquad r=2h,\qquad m=3h+4s+2.          \tag{1.2}
$$



Both coordinates in (1.1) are reduced to explicit rational tails of
$\log(1+z^2)$, all of whose denominators are $p$-units.  Eliminating
the two factorial prefactors gives an exact necessary rational eliminant
$E_h(s)$, but a moving binomial/hypergeometric residue remains.

**PROVED — an all-index twisted-de-Rham identity.**  The two weights satisfy
a unique bounded-degree identity



$$
P_1=\alpha P_0+\beta P'_0.       \tag{1.3}
$$



After integration by parts, this removes the logarithmic derivative term
at every index above $\deg P_0+2$, including both target indices.  The
result is a four-term local transfer from the $\nu=1$ tail to the
$\nu=0$ tail.

**PROVED — complete residual-strip exclusion.**  For every $s\geq1$, no
admissible prime on any line $0\leq h\leq8$ satisfies both coordinates.
The proof factors each fixed-$h$ rational eliminant, its denominator, and
the phase resultant, then checks the finite list of compatible prime
divisors exactly.

**FINITE.**  An exact scan of all 22,934 admissible rows with $p\leq2000$
finds 20 zeros of the first coordinate and 26 zeros of the second, but no
simultaneous zero.  This is evidence only and is not extrapolated.

**OPEN.**  Neither (1.3) nor the fixed-$h$ result controls unbounded
$h$.  No all-prime exclusion or positive Route-1 log-mass saving for the
full $j=1$ cell is proved.  The actual new usable rate coefficient is
therefore zero.

## 2. Exact cell and admissibility

For $j=1$, Item 217's retained-state vector is



$$
J_1=(-12,-12,6,12).                               \tag{2.1}
$$



This is the four-component vector
$(a u_0,a u_1,-c v_0,-c v_1)$, with $(a,c)=(4,3)$; it is not the
three-component Item 197 vector.  In Item 197's coordinates one instead
has



$$
(U_1,V_1,W_1)=(0,2,-4),\qquad
 {C_\nu(m)\over p}\equiv6(2Y'_\nu-Y_\nu)\pmod p.  \tag{2.2}
$$



All primes here satisfy $p\geq13$, so 6 is a unit.  The frozen PNT-row
relations give (1.2).  Conversely, (1.2) with $h,s\geq1$ is the complete
integer parameterization of this cell.  Moreover



$$
p\equiv h\pmod3.               \tag{2.3}
$$



Thus $3\mid h$ would force the prime $p>3$ to be composite.  This
automatically removes $h=0,3,6$ in the residual strip.

## 3. Palindromic transfer to rational tails

Put



$$
B_p(z)=\sum_{k=1}^{p-1}{(-1)^{k-1}z^{2k}\over k},                 \tag{3.1}
$$




$$
P_0=(1-z)^{2h}(1+z)(1+z^2)^{2s},\qquad
 P_1=(1-z)^{2h}(1+z)^4(1+z^2)^{2s-1}.              \tag{3.2}
$$



Modulo $p$, coefficient pairing $k\leftrightarrow p-k$ gives
$B_p(z)=z^{2p}B_p(1/z)$.  Both $P_\nu$ are self-reciprocal.  Hence the
two high sections $Y'_\nu$ reflect to the same low index



$$
T=2h+6s+2.                                        \tag{3.3}
$$



The low sections $Y_\nu$ occur at



$$
L_0=4h+4s+2,\qquad L_1=4h+4s+3.                  \tag{3.4}
$$



All three indices are below $p$:



$$
p-T=2h+1,\qquad p-L_0=2s+1,\qquad p-L_1=2s.       \tag{3.5}
$$



They also exceed the corresponding polynomial degrees.  Therefore the
truncation in (3.1) is invisible and may be replaced coefficientwise by
the formal series $\log(1+z^2)$.  Define over $\mathbb Q$



$$
H_\nu(N)=[z^N]P_\nu(z)\log(1+z^2),\qquad
 Q_\nu=2H_\nu(T)-H_\nu(L_\nu).                    \tag{3.6}
$$



Then the exact divided-coordinate bridge is



$$
{C_\nu(m)\over p}\equiv6Q_\nu\pmod p.         \tag{3.7}
$$



Every denominator used in (3.6) is an integer $1\leq k<p$, hence a
$p$-unit.  The checker additionally reconstructs the original integer
coefficient and verifies (3.7), including division by $p$, for every
admissible row through $p\leq31$.

## 4. Closed rational tails and the necessary eliminant

For an integer kernel $K(z)=\sum K_nz^n$, set



$$
\operatorname{Odd}(K;a,q)
 =\sum_{t\geq0}(-1)^t{(a+1)_t\over(q+a+2)_t}K_{2t+1},            \tag{4.1}
$$




$$
\operatorname{Even}(K;a,q)
 =\sum_{t\geq0}(-1)^t{(a)_t\over(q+a+1)_t}K_{2t}.               \tag{4.2}
$$



The sums terminate at the degree of $K$.  These formulas follow from
the exact tail coefficient



$$
[w^n](1+w)^q\log(1+w)
 =(-1)^{n-q-1}{q!(n-q-1)!\over n!},\qquad n>q.     \tag{4.3}
$$



Let



$$
K_0=(1-z)^{2h}(1+z),\qquad K_1=(1-z)^{2h}(1+z)^4,               \tag{4.4}
$$


and abbreviate



$$
\begin{aligned}
 x&=\operatorname{Odd}(K_0;s,2s),&
 y&=\operatorname{Odd}(K_0;h,2s),\\
 u&=\operatorname{Even}(K_1;s,2s-1),&
 v&=\operatorname{Odd}(K_1;h,2s-1).
\end{aligned}                                                   \tag{4.5}
$$



With



$$
\begin{aligned}
 A&=(-1)^s{(2s)!s!\over(3s+1)!},&
 B&=(-1)^h{(2s)!h!\over(2s+h+1)!},\\
 C&=(-1)^{s-1}{(2s-1)!(s-1)!\over(3s-1)!},&
 D&=(-1)^h{(2s-1)!h!\over(2s+h)!},
\end{aligned}                                                   \tag{4.6}
$$



the two coordinates become exactly



$$
Q_0=2Ax-By,\qquad Q_1=2Cu-Dv.             \tag{4.7}
$$



All factorial indices in (4.6), and all rising-factorial entries in
(4.1)--(4.2), lie strictly between 0 and $p$.  Thus reduction modulo
$p$ is legitimate without exceptional denominator cases.

The prefactor ratios are



$$
{C\over A}=-{3(3s+1)\over2s},\qquad
 {D\over B}={2s+h+1\over2s}.                       \tag{4.8}
$$



Consequently a simultaneous zero in (4.7) necessarily satisfies



$$
\boxed{E_h(s):={2s+h+1\over2s}xv
             +{3(3s+1)\over2s}uy=0\pmod p.}        \tag{4.9}
$$



This elimination is not sufficient.  One original equation still imposes
the moving congruence



$$
{B\over A}=(-1)^{h-s}{h!\binom{3s+1}{s}\over(2s+2)_h}\pmod p. \tag{4.10}
$$



Uniform control of (4.10) is the present arithmetic obstruction.  It is a
factorial/finite-log residue of growing length, not a fixed algebraic
number.  Known finite-log functional equations do not by themselves give
a nonvanishing theorem for this weighted incomplete-beta residue.

## 5. All-index twisted-de-Rham identity

Since $P_1/P_0=(1+z)^3/(1+z^2)$, direct common-denominator reduction gives



$$
P_1=\alpha P_0+\beta P'_0,                         \tag{5.1}
$$


where



$$
\alpha={2h+4s-1\over4s}+{h+2s\over s}z
        +{2h+4s+1\over4s}z^2,\qquad
 \beta={(1-z^2)(1+z)\over4s}.                     \tag{5.2}
$$



Indeed, after division by $P_0$, (5.1) is the elementary rational
identity



$$
{ (1+z)^3\over1+z^2}=\alpha+\beta
 \left(-{2h\over1-z}+{1\over1+z}+{4sz\over1+z^2}\right).       \tag{5.3}
$$



This solution is unique in the domain
$\deg\alpha\leq2,\deg\beta\leq3$: the difference of two solutions would
force $\beta$ to be divisible by the square-free radical
$(1-z)(1+z)(1+z^2)$, of degree four.

Write $F=P_0\log(1+z^2)$.  Integration by parts gives



$$
P_1\log(1+z^2)=(\alpha-\beta')F+(\beta F)'
                 -\beta P_0{2z\over1+z^2}.         \tag{5.4}
$$



The last term is a polynomial of degree $\deg P_0+2$.  Hence, for every
$N>\deg P_0+2$, coefficient extraction yields the all-index identity



$$
\boxed{\begin{aligned}
4sH_1(N)={}&(N+1)H_0(N+1)
 +(N+2h+4s-1)H_0(N)\\
& +(4h+8s+1-N)H_0(N-1)
 +(2h+4s+3-N)H_0(N-2).
\end{aligned}}                                                   \tag{5.5}
$$



Both required $\nu=1$ indices are in this domain because



$$
T-(\deg P_0+2)=2s-1\geq1,\qquad
 L_1-(\deg P_0+2)=2h\geq2.                        \tag{5.6}
$$



Thus (5.5) is a genuine exact reduction, not finite evidence.  Its scoped
limitation is equally exact: $Q_0$ couples $T$ to $L_0$, whose
separation is



$$
|L_0-T|=2|h-s|.            \tag{5.7}
$$



The local four-term identity does not identify these two endpoint germs,
and the transfer distance is unbounded.  Uniqueness in the bounded-degree
domain rules out tuning (5.1) to remove that boundary, but does not rule
out a higher-order or growing-degree construction.  Such a construction
remains open.

## 6. Complete all-$s$ exclusion for $0\leq h\leq8$

For fixed $h$, exact rational simplification writes



$$
E_h(s)=\lambda_h{N_h(s)\over D_h(s)},    \tag{6.1}
$$



with primitive coprime integer polynomials.  The numerator factorization
is complete:

| $h$ | $\lambda_h$ | factorization of $N_h$ | exact coefficient record |
|---:|---:|---|---|
| 1 | $-2$ | $24s^3+96s^2+112s+41$, irreducible mod 5 | SHA-256 `c585842afb44006ed191daf613ac5fe0a0a80a17cbee2126d5ccd0edcc49ee0c` |
| 2 | $-2$ | $(2s^2+11s+13)(64s^2+80s+27)$ | SHA-256 `328b5acfd1b18d3f1c88a00dcc9f61f50890d44eddf88f0eb2482c106c1fc5d0` |
| 4 | $4/3$ | irreducible degree 8, mod-11 witness | SHA-256 `bed149c7b4e75ab73711e6bca04972c7392e56a6e88def2bfce0ac11382d73d6` |
| 5 | $8/3$ | irreducible degree 9, mod-11 witness | SHA-256 `4ee126e188b4d529234cc680b7e7d4055fca811392d08ef06e805ee6aab566b9` |
| 7 | $-32/9$ | irreducible degree 13, mod-67 witness | SHA-256 `073f345dfac3e8eccbc24aa5f4c68cdaa12fe08d7cff2c83f3f4eab466bbb530` |
| 8 | $-16/9$ | irreducible degree 14, mod-113 witness | SHA-256 `5dbab589b1ccbf7ade27cc38942d1d4cafb9a646e580f30d878330fcbf35c4b7` |

For $h=2$, the two discriminants are 17 and $-512$, so the displayed
quadratics are irreducible over $\mathbb Z$.  For every other line, the
checker performs the full Rabin irreducibility test over the stated finite
field.  The canonical JSON stores every numerator coefficient, low to
high, rather than relying on a digest alone.

The primitive denominators factor as follows:



$$
\begin{array}{c|l}
h&D_h(s)\\ \hline
1&s(2s+3)(3s+2)\\
2&s(s+2)(2s+5)(3s+2)\\
4&s(s+3)(s+4)(2s+7)(2s+9)(3s+2)(3s+4)(3s+5)\\
5&s(s+4)(s+5)(2s+7)(2s+9)(2s+11)(3s+2)(3s+4)(3s+5)\\
7&s(s+5)(s+6)(s+7)(2s+9)(2s+11)(2s+13)(2s+15)
   (3s+2)(3s+4)(3s+5)(3s+7)(3s+8)\\
8&s(s+5)(s+6)(s+7)(s+8)(2s+11)(2s+13)(2s+15)(2s+17)
   (3s+2)(3s+4)(3s+5)(3s+7)(3s+8).
\end{array}                                                       \tag{6.2}
$$



Every displayed linear factor is positive and strictly below
$p=6s+4h+3$.  The scalar $\lambda_h$ uses only 2 and 3; admissible
$p$ is odd and $p\ne3$.  This is the complete denominator/unit audit.

Let $d_h=\deg N_h$.  If (4.9) holds, then $p\mid N_h(s)$, and the phase
equation implies



$$
p\mid R_h:=6^{d_h}N_h\left(-{4h+3\over6}\right).                \tag{6.3}
$$



The exact fully factored resultants are



$$
\begin{array}{c|r|l}
h&R_h&\text{prime factorization of }|R_h|\\ \hline
1&624&2^4\,3\,13\\
2&-54976&2^6\,859\\
4&1705140003840&2^{10}\,3\,5\,7\,13\,1219909\\
5&-475657910425600&2^{11}\,5^2\,7^2\,53\,1033\,3463\\
7&127117923618801750835200&2^{16}\,3\,5^2\,7^2\,11\,13\,73\,1103\,1409\,32533\\
8&-118887712469320504213504000&2^{18}\,5^3\,7^2\,11\,13\,47\,1314127\,8383391.
\end{array}                                                       \tag{6.4}
$$



Only prime factors compatible with $p=6s+4h+3$, $s\geq1$, need be
tested.  Exact modular evaluation of the original pair (4.7) gives



$$
\begin{array}{c|r|r|r|r}
h&p&s&Q_0&Q_1\\ \hline
1&13&1&9&4\\
4&1219909&203315&833864&86967\\
5&53&5&36&14\\
7&73&7&32&58\\
7&32533&5417&20350&11902\\
8&47&2&30&41\\
8&8383391&1397226&6424621&1596119.
\end{array}                                                       \tag{6.5}
$$



There is no compatible candidate for $h=2$, and no row in (6.5) is a
simultaneous zero.  Together with the automatic composite lines
$h=0,3,6$, this proves the stated all-prime exclusion through $h=8$.

## 7. Declared finite scan

The standard-library checker enumerates every prime $p\leq2000$ and
every positive $(h,s)$ satisfying (1.2).  It obtains



$$
\begin{array}{c|r}
\text{admissible rows}&22934\\
Q_0=0&20\\
Q_1=0&26\\
Q_0=Q_1=0&0\\
E_h(s)=0&58.
\end{array}                                                       \tag{7.1}
$$



The 46 one-coordinate rows are distinct.  The first three are



$$
(p,h,s;Q_0,Q_1,E)=(29,5,1;15,0,2),
 (53,11,1;11,0,17),
 (109,10,11;0,35,11).                            \tag{7.2}
$$



Thus neither coordinate is individually nonzero on all admissible rows;
only a paired theorem can close the cell.  The complete row stream has
SHA-256
`b641131ccb68bea399df3bc40429916f639da72546ef7c2da61d890158d778b6`.
The scan is labeled **FINITE**, not a density statement or all-prime proof.

## 8. Route-1 rate ledger

The proved $h\leq8$ strip contributes at most $O(\log m)$ prime-log
weight for each $m$, hence zero linear-rate coefficient.  The actual new
usable coefficient from Item 218 is therefore



$$
\boxed{0}.            \tag{8.1}
$$



Conditionally, excluding the entire $j=1$ cell would remove



$$
{1\over6}\ \text{per }m={1\over36}\ \text{per }6m.             \tag{8.2}
$$



That alone would leave `0.0283968068886832...` per $6m$, so it does not
close the global gap while $j=2$ remains open.  The $j=2$ cell is
$2/35$ per $m$.  If both cells were excluded, the remainder would be



$$
C_0-{47\over210}=0.1132379841892420\ldots\ \text{ per }m
 =0.0188729973648737\ldots\ \text{ per }6m,         \tag{8.3}
$$



where $C_0=-4\log2+\pi/\sqrt3+3\log3-2$.  This is below $G$ by
`0.0007599863045581...` per $6m$.  Equation (8.3) is conditional
bookkeeping only; this item proves neither full-cell exclusion.

## 9. Reproducibility and labels

From the archive root, run

```text
python scripts/item218_j1_common_log_certificate.py --output results/item218_j1_common_log_certificate.json
python scripts/item218_j1_common_log_certificate.py --output results/item218_j1_common_log_certificate.replay.json
```

The checker uses only Python 3.11+ standard-library exact integer,
`Fraction`, and finite-field arithmetic.  It has no host paths or external
data dependencies.

**PROVED:** (1.2), (2.1)--(4.10), the all-index identity (5.5), all
denominator/unit audits, every factorization and candidate check in
(6.1)--(6.5), and the all-$s$ exclusion for $0\leq h\leq8$.

**FINITE:** the scan (7.1)--(7.2), with no extrapolation.

**OPEN:** all-prime exclusion for unbounded $h$; uniform control of
(4.10); a higher-order endpoint transfer closing (5.7); any positive
Route-1 rate gain from $j=1$; and the $j=2$ classification.
