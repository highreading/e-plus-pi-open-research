> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 241 — Character-harmonic collapse of the corrected $j=2$ kernel

Checked: 2026-08-31 (Beijing time)

## 1. Scope and verdict

Work in the normalized fixed $j=2$ cell of Item 239.  Thus $p\ge17$
is prime, $1\le n<p$, and



$$
h=\frac{p-1}{2},\qquad
 \chi=(-1)^h.                                         \tag{1.1}
$$



Item 239 wrote the actual second-digit correction as



$$
K_p(n)=K_p^{(1)}(n)+K_p^{(2)}(n),                    \tag{1.2}
$$



where $K_p^{(2)}$ was displayed using coefficient tables of
$A_p^2,B_p^2,A_pB_p$.  This item removes those convolution tables.

> **PROVED — all-index convolution collapse.**  Every one of the nine
> quadratic sections in Item 239 is an explicit prefix-harmonic
> expression.  The full kernel $K_p(n)$ is given by the two parity
> formulas (5.1)--(5.2).  The proof holds for every prime $p\ge17$
> and every $1\le n<p$, not merely for scanned rows.

> **PROVED — finite coefficient state.**  On each parity, the simplified
> kernel is the output of a seven-coordinate rational first-order state;
> the exact transitions are (6.2) and (6.4).  Every transition
> denominator in its stated range is a $p$-unit.

> **PROVED — isolated character-prefix forcing.**  Put
> 

$$
> \mathcal O_u=\sum_{j=0}^{u-1}\frac{(-1)^j}{2j+1},
> \qquad R_u=(-1)^u\mathcal O_u.
>
$$


> Then
> 

$$
> R_{u+1}=-R_u-\frac1{2u+1}.                          \tag{1.3}
>
$$


> At every odd denominator $n=2u+1$, the full kernel contains
> $90R_u/n$.  The coefficient $90/n$ is a unit for every admissible
> prime.  This is an explicit inhomogeneous bulk state, not an unnamed
> convolution coordinate.

> **SCOPED CONSEQUENCE.**  The corrected kernel therefore has a finite
> coefficient-state description.  This is not yet a boundary-only
> terminal recurrence for
> $K_\nu=\sum_\ell c_{\nu,\ell}K_p(n_\ell)$.  After summation against
> the restricted $P_\nu$ coefficients, the source in (1.3) produces a
> bulk moment.  A separate telescoping or cancellation theorem could
> still remove it; none is proved here.

> **GLOBAL INTERFACE.**  The kernel $K_\nu$ enters only the stronger
> Item 239 condition $p^3\mid C_\nu$.  An ordinary common-log collision
> requires only $p^2\mid C_0,C_1$, so the present simplification does
> not strengthen that gate and books no fixed-cell capacity.

> **EXACT FINITE ONLY.**  The checker exhausts all 14,174 pairs
> $(p,n)$ with $17\le p\le401$ prime and $1\le n<p$, as well as
> 7,014 transitions on each parity.  Those computations replay the
> all-index identities but are not their proof.

> **OPEN / BOOKING.**  No all-prime common-log exclusion, zero-rate
> theorem, new divisibility exponent, or capacity reduction follows.

## 2. Prefixes and the quadratic kernels

All formulas in Sections 2--6 are in $\mathbb F_p$.  Set



$$
H_N=\sum_{j=1}^N\frac1j,\qquad H_0=0,               \tag{2.1}
$$



and introduce the two prefixes



$$
\alpha_N=\sum_{j=1}^N\frac{(-1)^j}{j},\qquad
 \mathcal O_N=\sum_{j=0}^{N-1}\frac{(-1)^j}{2j+1}.  \tag{2.2}
$$



Separating the even and odd summands gives the exact identity



$$
\boxed{\alpha_N=H_{\lfloor N/2\rfloor}-H_N.}        \tag{2.3}
$$



Thus $\alpha_N$ is only shorthand for ordinary harmonic prefixes.
The genuinely new named prefix is $\mathcal O_N$, the partial harmonic
sum for the nontrivial character modulo four.

Recall from Item 239 that



$$
A_p(z)=-\sum_{k=1}^{p-1}\frac{z^k}{k},\qquad
 B_p(z)=\sum_{k=1}^{p-1}\frac{(-1)^{k-1}z^{2k}}k.    \tag{2.4}
$$



Write



$$
a(t)=[z^t]A_p^2,\quad b(t)=[z^t]B_p^2,
 \quad c(t)=[z^t]A_pB_p.                              \tag{2.5}
$$



The depth-two correction is



$$
\begin{aligned}
K_p^{(2)}(n)={}&9a(p+n)-18a(n)\\
&-3b(3p+n)+6b(2p+n)+6b(p+n)-36b(n)\\
&-9c(2p+n)-16c(p+n)+54c(n).                           \tag{2.6}
\end{aligned}
$$



## 3. The two square collapses

Let $L(x)=\sum_{k=1}^{p-1}x^k/k$ and
$d(t)=[x^t]L(x)^2$.  The partial fraction



$$
\frac1{k(t-k)}=\frac1t\left(\frac1k+\frac1{t-k}\right)             \tag{3.1}
$$



and $H_{p-1}=0$ give, for $1\le n<p$,



$$
d(n)=\frac{2H_{n-1}}n,\qquad
 d(p+n)=-\frac{2H_n}{n}.                             \tag{3.2}
$$



The endpoint cases are included: both sides of the first identity vanish
at $n=1$, and both sides of the second vanish at $n=p-1$.
Since $A_p^2=L(z)^2$, substitution into (2.6) yields



$$
\boxed{
 9a(p+n)-18a(n)
 =-\frac{54H_{n-1}}n-\frac{18}{n^2}.}                \tag{3.3}
$$



Also



$$
b(2t)=(-1)^t d(t),\qquad b(2t+1)=0.                 \tag{3.4}
$$



For even $n=2u$, put $\varepsilon=(-1)^u$ and note that
$C(n)=2\varepsilon$.  For odd $n$, put
$h_n=(p+n)/2$, so $J_\chi(n)=2(-1)^{h_n}$.  Equation (3.2) then
gives



$$
\boxed{
\begin{aligned}
&-3b(3p+n)+6b(2p+n)+6b(p+n)-36b(n)\\
&\quad=
\begin{cases}
C(n)\left(-30H_{u-1}/u+6/u^2\right),&n=2u,\\
J_\chi(n)\left(3H_{h_n-1}/h_n-3/h_n^2\right),&n\text{ odd}.
\end{cases}                                           \tag{3.5}
\end{aligned}}
$$



## 4. The mixed collapse

Because $A_p=-L(z)$ and $B_p=-L(-z^2)$,



$$
c(t)=\sum_{\substack{1\le j\le p-1\\1\le t-2j\le p-1}}
 \frac{(-1)^j}{j(t-2j)}.                              \tag{4.1}
$$



For $t\equiv n\not\equiv0\pmod p$, use



$$
\frac1{j(t-2j)}
 =\frac1t\left(\frac1j+\frac2{t-2j}\right).         \tag{4.2}
$$



The required ranges of $j$ are



$$
\begin{array}{c|ccc}
&t=n&t=p+n&t=2p+n\\ \hline
n=2u&1\ldots u-1&u+1\ldots h+u&h+u+1\ldots p-1\\
n=2u+1&1\ldots u&u+1\ldots h+u&h+u+2\ldots p-1.
\end{array}                                           \tag{4.3}
$$



Empty endpoint ranges contribute zero.  Reindexing the second summand
in (4.2) by $t-2j$, and using $(-1)^h=\chi$, gives the following six
identities.

For $n=2u$, $1\le u\le h$, and
$\varepsilon=(-1)^u$,



$$
\boxed{
\begin{aligned}
c(n)&=\frac{(1+\varepsilon)\alpha_{u-1}}n,\\
c(p+n)&=\frac{\alpha_{h+u}-\alpha_u
                 +2\chi\varepsilon\mathcal O_h}{n},\\
c(2p+n)&=\frac{\alpha_{p-1}-\alpha_{h+u}
                 -\varepsilon(\alpha_h-\alpha_u)}n.
\end{aligned}}                                        \tag{4.4}
$$



For $n=2u+1$, $0\le u\le h-1$,



$$
\boxed{
\begin{aligned}
c(n)&=\frac{\alpha_u+2\varepsilon\mathcal O_u}{n},\\
c(p+n)&=\frac{\alpha_{h+u}-\alpha_u
                 -\chi\varepsilon\alpha_h}{n},\\
c(2p+n)&=\frac{\alpha_{p-1}-\alpha_{h+u+1}
                 -2\varepsilon(\mathcal O_h-\mathcal O_{u+1})}{n}.
\end{aligned}}                                        \tag{4.5}
$$



Equations (4.4)--(4.5), inserted into



$$
-9c(2p+n)-16c(p+n)+54c(n),                           \tag{4.6}
$$



remove the last quadratic convolution table.

## 5. The full simplified corrected kernel

Add (3.3), (3.5), and (4.6) to the depth-one formula from Item 239.
For even $n=2u$, $1\le u\le h$, one obtains



$$
\boxed{
\begin{aligned}
K_p(2u)={1\over n}\{&-63H_{2u-1}-100\varepsilon H_{u-1}
-9\alpha_{p-1}-7\alpha_{h+u}\\
&+9\varepsilon\alpha_h-32\chi\varepsilon\mathcal O_h
+(70+45\varepsilon)\alpha_{u-1}\}
+\frac{80\varepsilon-36}{n^2}.
\end{aligned}}                                        \tag{5.1}
$$



For odd $n=2u+1$, $0\le u\le h-1$,



$$
\boxed{
\begin{aligned}
K_p(2u+1)={1\over n}\{&-63H_{2u}
-10\chi\varepsilon H_{h+u}
-9\alpha_{p-1}-7\alpha_{h+u}+70\alpha_u\\
&+16\chi\varepsilon\alpha_h
+18\varepsilon\mathcal O_h+90\varepsilon\mathcal O_u\}
+\frac{8\chi\varepsilon-36}{n^2}.
\end{aligned}}                                        \tag{5.2}
$$



The coefficient of the variable character prefix in (5.2) is
$90\varepsilon/n$.  Since $p\ge17$, neither $90$ nor $n$ is
zero modulo $p$.  The coefficient is therefore a unit.  This is a
coefficientwise statement; it does not assert linear independence after
summation against $P_\nu$.

## 6. Exact seven-coordinate coefficient states

The formulas above admit especially small first-order states.  For the
even subsequence define



$$
V_u^{\rm e}=
\left(1,\varepsilon,H_{2u-1},\varepsilon H_{u-1},
\alpha_{h+u},\alpha_{u-1},\varepsilon\alpha_{u-1}\right)^T,
\quad 1\le u\le h.                                    \tag{6.1}
$$



For $u<h$, its transition is



$$
\boxed{
\begin{aligned}
\varepsilon'&=-\varepsilon,\\
H_{2u+1}&=H_{2u-1}+\frac1{2u}+\frac1{2u+1},\\
(\varepsilon H_{u-1})'&=-\varepsilon H_{u-1}-\frac\varepsilon u,\\
\alpha_{h+u+1}&=\alpha_{h+u}
                 -\frac{\chi\varepsilon}{h+u+1},\\
\alpha_u&=\alpha_{u-1}+\frac\varepsilon u,\\
(\varepsilon\alpha_{u-1})'&=-\varepsilon\alpha_{u-1}-\frac1u.
\end{aligned}}                                        \tag{6.2}
$$



Equation (5.1) is a linear output map from $V_u^{\rm e}$, followed by
the displayed rational double-pole term.

For the odd subsequence define



$$
V_u^{\rm o}=
\left(1,\varepsilon,H_{2u},\varepsilon H_{h+u},
\alpha_{h+u},\alpha_u,R_u\right)^T,
\quad R_u=\varepsilon\mathcal O_u,\quad 0\le u\le h-1. \tag{6.3}
$$



For $u<h-1$,



$$
\boxed{
\begin{aligned}
\varepsilon'&=-\varepsilon,\\
H_{2u+2}&=H_{2u}+\frac1{2u+1}+\frac1{2u+2},\\
(\varepsilon H_{h+u})'&=-\varepsilon H_{h+u}
                         -\frac\varepsilon{h+u+1},\\
\alpha_{h+u+1}&=\alpha_{h+u}
                 -\frac{\chi\varepsilon}{h+u+1},\\
\alpha_{u+1}&=\alpha_u-\frac\varepsilon{u+1},\\
R_{u+1}&=-R_u-\frac1{2u+1}.
\end{aligned}}                                        \tag{6.4}
$$



Equation (5.2) is the corresponding linear output map.  If the isolated
character contribution is normalized as



$$
Z_u=\frac{90R_u}{2u+1},                              \tag{6.5}
$$



then (6.4) is equivalent to



$$
\boxed{
 Z_{u+1}=-\frac{2u+1}{2u+3}Z_u
          -\frac{90}{(2u+1)(2u+3)}.}                 \tag{6.6}
$$



The source in (6.6) is nonzero throughout its transition range.

### Range and unit audit

For the even transition, $1\le u<h$.  Hence
$u,2u,2u+1,h+u+1$ all lie strictly between $0$ and $p$.
For the odd transition, $0\le u<h-1$.  Hence
$u+1,2u+1,2u+2,h+u+1,2u+3$ do also.  The summands in
$\mathcal O_h$ have denominators $1,3,\ldots,p-2$.  Finally
$p\ge17$ implies $p\nmid90$.  Every inverse used in
(4.4)--(6.6) is therefore legitimate.

## 7. What the finite state does and does not prove

For the Item 239 polynomial
$P_\nu=\sum_\ell c_{\nu,\ell}z^\ell$, the corrected carry is



$$
K_\nu=\sum_\ell c_{\nu,\ell}K_p(n_\ell).            \tag{7.1}
$$



The variable character contribution singled out by (5.2) is exactly



$$
90\sum_{\substack{\ell\\n_\ell=2u+1}}
 c_{\nu,\ell}\frac{R_u}{2u+1}.                       \tag{7.2}
$$



Equations (6.4)--(6.6) prove that this can be propagated with one extra
coefficient-state coordinate.  They also show why this is presently a
bulk coordinate: its update has a nonzero source at each interior odd
index.  Summation by parts against $c_{\nu,\ell}$ leaves a source sum
unless a new identity for the restricted $P_\nu$ family cancels it.

Therefore Item 241 proves neither that a finite boundary-only terminal
system exists nor that one is impossible.  It replaces the convolution
obstacle by the precise telescoping problem (7.2).  Aggregate
cancellation, a creative telescoper, and an enlarged cohomology
interpretation remain open.

## 8. Replay, status, and booking

The standard-library checker
`item241_j2_character_harmonic_collapse_certificate.py`:

1. verifies (2.3) for every replayed prefix;
2. compares (3.3), (3.5), and (4.4)--(4.5) with the exact Item 239
   convolution coefficients;
3. checks the full parity formulas (5.1)--(5.2);
4. checks every in-range state transition (6.2), (6.4), and (6.6); and
5. audits the fixed Item 239 dependency hash.

From the archive root, run:

    python scripts/item241_j2_character_harmonic_collapse_certificate.py --output results/item241_j2_character_harmonic_collapse_certificate.json
    python scripts/item241_j2_character_harmonic_collapse_certificate.py --output results/item241_j2_character_harmonic_collapse_certificate_replay.json

Canonical and replay outputs are byte-identical and contain no host path,
timestamp, random seed, or elapsed time.

### Status ledger

**PROVED**

- the all-index $A_p^2,B_p^2,A_pB_p$ harmonic collapse;
- the full corrected-kernel formulas (5.1)--(5.2);
- the two exact seven-coordinate coefficient states; and
- the character-prefix forcing law and complete range/unit audit.

**EXACT FINITE ONLY**

- 14,174 coefficient-pair replays through $p\le401$; and
- 7,014 even, 7,014 odd, and 7,014 isolated-forcing transitions.

**OPEN**

- a boundary-only recurrence for the aggregated periods (7.1);
- cancellation or noncancellation of (7.2) on the restricted row family;
- an all-prime classification of simultaneous $j=2$ zeros; and
- any Route-1 rate or capacity improvement.

The booking is



$$
\boxed{
\text{new unconditional log rate}=0,\qquad
\text{new divisibility exponent}=0,\qquad
\text{capacity reduction}=0.}                        \tag{8.1}
$$



Item 241 proves no statement about the arithmetic nature of $e+\pi$.
