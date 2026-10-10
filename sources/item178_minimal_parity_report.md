> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 178 — actual minimal-parity fixed bands

Date: 2026-08-29

## 1. Scope and verdict

On the Item 172 $\kappa=1$ cell, fix a band $j\ge1$ and take the smallest
admissible value with the required parity,



$$
\epsilon_j=j\pmod2,\qquad s=\epsilon_j,\qquad
 m={(j+1)p-\epsilon_j-1\over2}.                       \tag{1.1}
$$



This item studies the **actual constrained primitive values** on (1.1),
not the ambient five-value functional of Item 175.

The main result is an all-band theorem.

**PROVED — actual constrained nonidentity on every minimal-parity fixed
band.**  For every



$$
j\ge1,\qquad \rho\in\{1,3\},                         \tag{1.2}
$$



the characteristic-zero constant $C_{j,\rho}$ whose reduction is the
minimal-parity $B_0$ digit is nonzero.  Consequently, for each one of
these fixed $j$, $B_0\ne0\pmod p$ for every sufficiently large
admissible prime $p\equiv\rho\pmod4$.

This is not a scan of finitely many primes: it proves a statement about
the entire tail of every minimal-parity fixed-band prime family.

**PROVED — explicit all-$j$ obstruction sequence.**  For every $j\ge1$
and each $\rho$, an integer $\Omega^\#_{j,\rho}$ is given below by a
four-by-four determinant, or equivalently by one of four three-term
central-coefficient formulas.  It satisfies



$$
B_0=0\text{ over }\mathbb Q
             \quad\Longrightarrow\quad
             \Omega^\#_{j,\rho}=0.                    \tag{1.3}
$$



Thus $\Omega^\#_{j,\rho}\ne0$ is a rigorous sufficient certificate of
actual constrained nonidentity.

**PROVED — uniform sign.**  The obstruction has the exact sign



$$
\operatorname {sgn}\Omega^\#_{j,\rho}=(-1)^j   \tag{1.4}
$$



for both $\rho$ and every $j\ge1$.  Section 6 gives a self-contained
coefficient proof.  The former $j\le1000$ computation is retained only
as an independent exact replay of this theorem.

**PROVED — zero-rate scope.**  Even after taking the union over all $j$,
the minimal-parity family has only $O(\log m)$ log-prime weight at fixed
$m$; Section 7 proves this directly.  Thus it gives no positive-rate
density, irrationality, or conclusion about $e+\pi$.

## 2. Exact convention and admissibility

The calculation uses Item 172's repaired convention throughout:



$$
\widetilde\gamma_\nu=[x^{p-1}]P_\nu\in\mathbb Z
$$



is formed exactly, exact resonant cancellation is performed, and only
then are coefficients reduced modulo $p$.  Bars denote reductions;
they never replace the exact coefficients in the definition of the
primitive.

The parity-minimal slices use the two Item 177 primitives:



$$
\begin{array}{c|c|c|c}
s&(\bar\gamma_0,\bar\gamma_1)&B(x)&\widehat T\\ \hline
0&(10,6)&2+2x+3x^2&u^{p-2}B(x)\\[2mm]
1&(1260,776)&
 {484\over5}+290x+578x^2+952x^3+1132x^4+1106x^5
 +970x^6+388x^7+388x^8&u^{p-5}B(x).
\end{array}                                             \tag{2.1}
$$



The representative $\widehat T$ can differ from the literal reduction
of the exact primitive by $c x^p$.  Item 177 proved that this kernel term
changes the Cartier result only by a scalar multiple of the base vector,
and therefore drops out of the determinant wedge.  Hence (2.1) gives the
exact $B_0$ digit.

For a fixed $j$, the simple sufficient cell threshold is



$$
p\ge\max(7,\,2j+3).                  \tag{2.2}
$$



Indeed (2.2) gives $s\le(p-3)/3$, nonnegative exponents, and
$p\le4m+1<p^2$.  It is the **admissibility threshold**, not a claimed
uniform nonvanishing threshold: after (2.2), the finitely many primes
dividing the numerator or denominator of the nonzero rational constant
$C_{j,\rho}$ must also be omitted.  Thus the conclusion is exactly
"all sufficiently large admissible primes" for each fixed band.

## 3. Why the actual digit is constant on a fixed band

In (2.1), the polynomial $B$ and the shift in the exponent depend only
on $s$, hence only on the parity of $j$; the full factor
$u^{p-k}$ still depends on $p$.  At $-1,i,-i$, Fermat and Gaussian
Frobenius nevertheless reduce the relevant primitive values to four fixed
lists indexed by



$$
\epsilon_j\in\{0,1\},\qquad
            \rho=p\pmod4\in\{1,3\}.                  \tag{3.1}
$$



The five-divisor weights depend on $j$, but not on $p$.  Therefore



$$
B_0=C_{j,\rho}\pmod p              \tag{3.2}
$$



for a fixed rational $C_{j,\rho}$.  The circular coordinate carries
the global sign



$$
\chi_4(p)=(-1)^{(p-1)/2}.           \tag{3.3}
$$



This is the Item 177 correction to Item 172 equation (4.11).  It changes
signed values in the $\rho=3$ class but never changes a zero condition;
the obstruction below is correspondingly insensitive to this overall
nonzero sign.

If the constrained evaluations are assembled as a partial fraction
$h=N(x)/Q(x)$, the four numerator polynomials are



$$
\begin{array}{c|c|c}
\epsilon_j&\rho&N(x)\\ \hline
1&1&(274-32x-38x^2)/5\\
1&3&(306+32x-6x^2)/5\\
0&1&-(9+4x+x^2)/2\\
0&3&(-5+4x+3x^2)/2.
\end{array}                                             \tag{3.4}
$$



These are actual values of the parity-specific primitive, not free
coordinates.

## 4. Cayley normal form

Make the Cayley substitution



$$
y={x+1\over1-x},\qquad t=y-1,\qquad
 D(y)=y(1+y^2),\qquad
 \Delta(t):=D(1+t)=2+4t+3t^2+t^3.                    \tag{4.1}
$$



Put



$$
A=3j+2,\qquad K=2j+2.              \tag{4.2}
$$



Up to the nonzero scalar $(-1)^j2^{-j-1}$, the base differential and
the constrained second differential are



$$
\alpha_j={(1-y)^A\over D(y)^K}\,dy,\qquad
 \beta_{j,\rho}=\alpha_j\,{M_{\epsilon_j,\rho}(y)\over4D(y)}. \tag{4.3}
$$



The coefficients of $M(1+t)$, low degree first, are



$$
\begin{array}{c|c|c}
\epsilon_j&\rho&M(1+t)\\ \hline
1&1&(2192+3160t+1440t^2+204t^3)/5\\
1&3&(2448+3800t+1952t^2+332t^3)/5\\
0&1&-36-62t-36t^2-7t^3\\
0&3&-20-22t-4t^2+t^3.
\end{array}                                             \tag{4.4}
$$



For odd $j$, multiply $M$ by $5$; for even $j$, leave it
unchanged.  Denote the resulting integral vector by $m^\#_{j,\rho}$.

## 5. The exactness obstruction

Item 175 proves that the circular/logarithmic residue vector of
$\alpha_j$ is nonzero for every $j\ge1$: otherwise its nonzero
$w^B_{j,1}$ wedge would vanish.  Hence, if the actual $B_0$ wedge of
$\alpha_j$ and $\beta_{j,\rho}$ vanishes, there is a rational
$\lambda$ for which



$$
{ (1-y)^A\bigl(M(y)-4\lambda D(y)\bigr)
   \over D(y)^{K+1}}\,dy                              \tag{5.1}
$$



has zero residues.  A rational differential on $\mathbb P^1$ with all
residues zero is exact.  A primitive of (5.1), normalized to vanish at
infinity, has the form $R/D^K$ with $\deg R\le A+1$.

Let



$$
P(t)=\Delta(t)^K=D(1+t)^K,\qquad
 p_r=[t^{A+r}]P(t)\quad(r=2,3,4).                     \tag{5.2}
$$



The coefficients of the primitive equation below order $A$ force



$$
R=C\,P_{\le A+1}+q\,t^{A+1}.                        \tag{5.3}
$$



Here $P_{\le A+1}$ is the truncation of $P$, $C$ is the homogeneous
solution parameter, and $q$ is the one new coefficient at degree
$A+1$.  Equating the four remaining coefficients,
$t^A,\ldots,t^{A+3}$, gives
a linear dependence among the four columns



$$
q_j=\begin{pmatrix}
 2(A+1)\\4(A+1-K)\\3(A+1-2K)\\A+1-3K
 \end{pmatrix},\quad
 d=\begin{pmatrix}2\\4\\3\\1\end{pmatrix},       \tag{5.4}
$$





$$
c_j=\begin{pmatrix}
 0\\
 -2(A+2)p_2\\
 -4(A+2-K)p_2-2(A+3)p_3\\
 -3(A+2-2K)p_2-4(A+3-K)p_3-2(A+4)p_4
 \end{pmatrix},                                       \tag{5.5}
$$



and $m^\#_{j,\rho}$ from (4.4).  Define



$$
\boxed{\Omega^\#_{j,\rho}
       =\det[q_j\;c_j\;d\;m^\#_{j,\rho}].}           \tag{5.6}
$$



Exactness of (5.1) implies (5.6) is zero, proving (1.3).  This report uses
only that direction.  It does **not** claim that a zero determinant alone
is sufficient for an actual cancellation without also checking the full
primitive system.  The certificate verifies
$\operatorname {rank}[q_j,c_j,d]=3$ for $j\le1000$, but no uniform
rank/converse theorem is needed for the stated result.

## 6. Simplified central-coefficient formulas

Expanding (5.6) gives a particularly small obstruction.  For odd $j$,



$$
\begin{aligned}
 \Omega^\#_{j,1}
  &=64(j+1)\{-11(5j+4)p_2+(51j+101)p_3+18(j+2)p_4\},\\
 \Omega^\#_{j,3}
  &=64(j+1)\{-11(5j+4)p_2+(53-29j)p_3+114(j+2)p_4\}.
                                                               \tag{6.1}
\end{aligned}
$$



For even $j$,



$$
\begin{aligned}
 \Omega^\#_{j,1}
  &=16(j+1)\{(5j+4)p_2+(9j-1)p_3-18(j+2)p_4\},\\
 \Omega^\#_{j,3}
  &=16(j+1)\{(5j+4)p_2-(11j+13)p_3+6(j+2)p_4\}.
                                                               \tag{6.2}
\end{aligned}
$$



Here $p_2,p_3,p_4$ are three adjacent coefficients immediately to the
right of the center of



$$
\Delta(t)^{2j+2}=(2+4t+3t^2+t^3)^{2j+2};       \tag{6.3}
$$



indeed its degree is $6j+6$, and their indices are
$3j+4,3j+5,3j+6$.

These four signs can be proved uniformly.  Put



$$
n=j+1,\qquad k=3n+3,\qquad
 a_r=[t^r]\Delta(t)^{2n-1}.                            \tag{6.4}
$$



For any polynomial $S$, coefficient extraction gives the Euler identity



$$
\begin{aligned}
 &[t^k]\Delta^{2n-1}
 \{\Delta R+(tS'-kS)\Delta+2ntS\Delta'\}\\
 &\hspace{35mm}=[t^k]\Delta^{2n}R,                    \tag{6.5}
\end{aligned}
$$



because the added term is
$(t\,d/dt-k)(S\Delta^{2n})$, whose $t^k$ coefficient is zero.
For the four braces in (6.1)-(6.2), take respectively



$$
\begin{array}{c|c|c}
\epsilon_j&\rho&S(t)\\ \hline
1&1&6+25t+11t^2\\
1&3&38+41t+11t^2\\
0&1&-6-5t-t^2\\
0&3&2-t-t^2.
\end{array}                                             \tag{6.6}
$$



Direct polynomial collection in (6.5) gives, in the same order,



$$
\begin{array}{c|c|c}
\epsilon_j&\rho&\text{brace in (6.1) or (6.2)}\\ \hline
1&1&-n(6a_{k-4}+22a_{k-5})\\
1&3&-n(38a_{k-4}+22a_{k-5})\\
0&1& n(6a_{k-4}+2a_{k-5})\\
0&3& 2n(a_{k-5}-a_{k-4}).
\end{array}                                             \tag{6.7}
$$



The first three signs are immediate because every coefficient of
$\Delta^{2n-1}$ is positive.  For the fourth, let



$$
L=2n-1,\qquad m=k-5=3n-2={3L-1\over2}.               \tag{6.8}
$$



The factorization



$$
\Delta(t)=(1+t)\bigl((1+t)^2+1\bigr)                 \tag{6.9}
$$



gives the self-contained binomial decomposition



$$
\Delta(t)^L
   =\sum_{r=0}^{L}\binom Lr(1+t)^{L+2r}.              \tag{6.10}
$$



For $r<L$, put $N=L+2r$.  Then $N\le3L-2<2m+1$, so



$$
\binom Nm\ge\binom N{m+1},           \tag{6.11}
$$



with a strict supported inequality, for example at $r=L-1$.  At
$r=L$, $N=3L=2m+1$, and the two central binomial coefficients are
equal.  Summing (6.11) in (6.10) proves



$$
[t^m]\Delta^L>[t^{m+1}]\Delta^L.                     \tag{6.12}
$$



Thus the last line of (6.7) is also positive.  Equations (6.1), (6.2),
and (6.7) prove



$$
\boxed{\operatorname {sgn}
             \Omega^\#_{j,\rho}=(-1)^j}
             \qquad(j\ge1,\ \rho=1,3).                \tag{6.13}
$$



Together with (1.3), this proves actual constrained nonidentity for every
fixed minimal-parity band.

## 7. Zero-rate consequence and exact replay

### 7.1 The all-band union still has zero rate

At fixed $m$, the two parity cases of (1.1) are exactly



$$
\begin{array}{c|c}
j\ \text{even}&(j+1)p=2m+1,\\
j\ \text{odd}&(j+1)p=2m+2.
\end{array}                                             \tag{7.1}
$$



Therefore every prime occurring anywhere in the minimal-parity union
divides one of the two fixed integers $2m+1$ and $2m+2$.  Moreover,
for a fixed prime and a fixed row of (7.1), $j+1$ is determined, so
there is no hidden band multiplicity.  Its total log-prime weight is at
most



$$
\sum_{p\mid 2m+1}\log p+\sum_{p\mid 2m+2}\log p
 \le\log\bigl((2m+1)(2m+2)\bigr)=O(\log m).            \tag{7.2}
$$



Hence even the all-$j$ theorem has zero asymptotic rate in the
fixed-$m$ problem.

### 7.2 Deterministic replay and sample values

Starting at $j=1$ with $P=\Delta^4$, the recurrence



$$
P_{j+1}=\Delta^2P_j             \tag{7.3}
$$



computes every needed coefficient using integers only.  The deterministic
certificate checks both the determinant (5.6) and the simplified formulas
(6.1)-(6.2) for all $1\le j\le1000$.  It finds no zero and no sign-law
failure in 2000 exact cases.

This $j\le1000$ run is a replay of the all-$j$ proof, not the basis for
claiming (6.13).  The first values are



$$
\begin{array}{c|r|r}
j&\Omega^\#_{j,1}&\Omega^\#_{j,3}\\ \hline
1&-1\,680\,384&-3\,253\,248\\
2&18\,002\,880&1\,172\,160\\
3&-41\,637\,707\,776&-80\,704\,110\,592\\
4&345\,286\,310\,400&22\,363\,660\,800\\
5&-686\,130\,530\,291\,712&-1\,330\,251\,756\,539\,904.
\end{array}                                             \tag{7.4}
$$



For example,



$$
\begin{aligned}
 |\Omega^\#_{1,1}|&=2^{10}\cdot3\cdot547,\\
 |\Omega^\#_{1,3}|&=2^{10}\cdot3^2\cdot353,\\
 \Omega^\#_{2,1}&=2^6\cdot3^2\cdot5\cdot7\cdot19\cdot47,\\
 \Omega^\#_{2,3}&=2^6\cdot3^2\cdot5\cdot11\cdot37.
                                                               \tag{7.5}
\end{aligned}
$$



Restoring the normalizations for the two Item 177 cases gives



$$
\begin{aligned}
 j=1:&\quad B_0=-\chi_4(p){5\over12288}\Omega^\#_{1,\rho},\\
 j=2:&\quad B_0=-\chi_4(p){49\over122880}\Omega^\#_{2,\rho}.
                                                               \tag{7.6}
\end{aligned}
$$



Thus (7.6) reproduces exactly



$$
(2735/4,-5295/4),\qquad(-918897/128,59829/128),       \tag{7.7}
$$



including the $\chi_4$ sign.  This is an independent normalization
cross-check against Item 177.

The SHA-256 digest of the ordered stream



$$
(j,\rho,\Omega^\#_{j,\rho}),
          \quad1\le j\le1000,\ \rho=1,3,              \tag{7.8}
$$



is

```text
4d5a254ff0a2890aa006885e6f34b887d732c73bd9ee8aa54d072dee471d0af4
```

## 8. Reproduction and status

Run

```powershell
python work/item178_minimal_parity_certificate.py `
  --max-j 1000 `
  --output work/item178_minimal_parity_certificate_replay.json
```

The canonical and replay JSON files are byte-identical.  The script is
location-portable: from the staging work directory its default output is
next to the script; after archival under scripts, its default output is
../results/item178_minimal_parity_certificate.json.  It has no hard-coded
archive path.

Status summary:

1. **THEOREM:** $C_{j,\rho}\ne0$ for both residue classes and every
   $j\ge1$.
2. **THEOREM:** each such band has $B_0\ne0$ for all sufficiently large
   admissible primes.
3. **THEOREM:** $\operatorname {sgn}\Omega^\#_{j,\rho}=(-1)^j$ for all
   $j\ge1$ and both residue classes.
4. **THEOREM:** the union over all minimal-parity bands has at most
   $O(\log m)$ log-prime weight at fixed $m$, hence zero rate.
5. **REPLAY ONLY:** exact integer verification of the all-$j$ identities
   and signs through $j=1000$.
6. **OPEN:** determine explicit exceptional prime sets beyond the first
   two bands and find a positive-rate family away from minimal parity.
