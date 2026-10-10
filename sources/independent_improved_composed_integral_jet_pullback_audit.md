> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Independent audit of the improved composed integral-jet pullback

Date: 2026-08-26

Audited snapshots:

```text
f16d9872d452af37e67f361c0435ac6197066680ed699281b2c8b96de95964eb  sources/improved_composed_integral_jet_pullback.md
c0ac1d342c94f24796f2bc02ef996e12aa25816ebecbe157ffa7694e73cb8824  scripts/improved_composed_pullback_certificate.py
6118a7152c964d957bccb4342f59a24c5767eccebc70f7fb8980dc30787aee5d  results/improved_composed_pullback_certificate.json
62d4ed61ff7876319a39a5f9da691673fdbb717054c68fe063aca70c47e8e5a4  scripts/composed_integral_pullback_hp_probe.py
ec590212db0b7a3b40c896db7f9b822594c023c43e9c839d9e4f8644a5aa1bae  results/composed_integral_pullback_hp_n15.json
```

## Verdict and status of the claims

**Accept without a source correction.**  The composition has integral
derivative jets in every order, and its nearest genuine singularity is
strictly farther from the origin than $\sqrt2$.  The latter assertion is
proved by the five exact positive Schur--Cohn gaps, not by the decimal root
calculation.

All 15 finite endpoint-matched HP records also pass an independent exact
recomputation.  The displayed nearest-root modulus



$$
1.4597454685987641723304\ldots
$$



is numerically stable in a second high-precision algorithm, but remains
explicitly diagnostic.  The finite HP calculations establish no all-degree
rank, height, or asymptotic theorem.  Nothing in the construction determines
the arithmetic nature of (e+\pi).

## 1. Endpoint values and all-order Hurwitz integrality

Set



$$
F(w)=4\arctan\frac{w}{2-w},\qquad
 \phi(z)=z-\frac{z^3}{6}+\frac{5z^4}{24}-\frac{z^5}{24},
 \qquad G=F\circ\phi.
$$



Directly,



$$
\phi(0)=0,\qquad
 \phi(1)=1+\frac{-4+5-1}{24}=1.
$$



The nonzero derivative jets of $\phi$ are



$$
\phi'(0)=1,\qquad
 \phi^{(3)}(0)=-1,\qquad
 \phi^{(4)}(0)=5,\qquad
 \phi^{(5)}(0)=-5,                              \tag{A1}
$$



with $\phi''(0)=0$ and all derivatives past order five equal to zero.
Thus every Hurwitz coefficient of $\phi$ is integral.

For completeness, the base-function jet formula can be recovered without
assuming it.  Since



$$
F'(w)=\frac4{w^2-2w+2}
 =\frac4{(w-(1+i))(w-(1-i))},
$$



partial fractions at (w=0), using
$1\pm i=\sqrt2e^{\pm i\pi/4}$, give



$$
F^{(k)}(0)=4(k-1)!2^{-k/2}\sin\frac{k\pi}{4}. \tag{A2}
$$



Its integrality is transparent by residue class.  For (q\geq0), the three
possibly nonzero cases are



$$
\begin{aligned}
 F^{(4q+1)}(0)&=(-1)^q2^{1-2q}(4q)!,\\
 F^{(4q+2)}(0)&=(-1)^q2^{1-2q}(4q+1)!,\\
 F^{(4q+3)}(0)&=(-1)^q2^{-2q}(4q+2)!,
\end{aligned}                                   \tag{A3}
$$



and (F^{(4q+4)}(0)=0).  For (q\geq1), even just the factors of two in
the even entries of each factorial show that the displayed powers of two
divide; the (q=0) cases are immediate.  Hence every jet in (A2) is an
integer.

Faà di Bruno's formula is



$$
G^{(n)}(0)=\sum_{k=1}^nF^{(k)}(0)
 B_{n,k}\bigl(\phi'(0),\ldots,\phi^{(n-k+1)}(0)\bigr). \tag{A4}
$$



The exponential partial Bell polynomials have integer coefficients.  One
direct proof, also used in the independent implementation, is their recurrence



$$
B_{n,k}(x_1,x_2,\ldots)
 =\sum_{j=1}^{n-k+1}\binom{n-1}{j-1}x_jB_{n-j,k-1}, \tag{A5}
$$



starting from (B_{0,0}=1).  Equations (A1), (A3), and (A4) therefore show



$$
G^{(n)}(0)\in\mathbb Z\qquad(n\geq1),
$$



while (G(0)=F(0)=0\).  This proves the all-order claim; it is not an
inference from a finite jet scan.

A fresh integer implementation of (A3)--(A5) through order (100), rather
than rational division of (G'\), reproduced the archived jet-list digest

```text
6e629f5bad2d856732294834a3e25da42c5b389c8683f46078066c7001a32f93
```

exactly.

## 2. Obstruction for ordinary integer-coefficient compositions

Let $\psi\in\mathbb Z[z]$ have degree (d\geq1), leading coefficient
$a_d$, and satisfy $\psi(0)=0$, $\psi(1)=1$.  The polynomial



$$
\psi(z)-(1+i)
$$



has leading coefficient (a_d) and constant coefficient (-(1+i)).
Vieta's formula therefore says that, counting multiplicity,



$$
\prod_{j=1}^d|z_j|=\frac{|1+i|}{|a_d|}
 =\frac{\sqrt2}{|a_d|}\leq\sqrt2.               \tag{A6}
$$



Since the geometric mean bounds the minimum,



$$
\min_j|z_j|leq
 \left(\frac{\sqrt2}{|a_d|}\right)^{1/d}
 \leq2^{1/(2d)}.                                \tag{A7}
$$



For (d\geq2), the right side is strictly below $\sqrt2$.  For (d=1),
the endpoint constraints force $\psi(z)=z$, whose preimages of (1\pm i)
have modulus exactly $\sqrt2$.

The preimage supplied by (A7) is a genuine singularity, not merely a root of
an auxiliary equation.  If $\psi(z)-(1+i)$ has multiplicity (m\) at a
root, then $\psi'$ has multiplicity exactly (m-1), and the chain-rule
derivative of (F\circ\psi) has a simple pole there.  Thus ordinary integral
polynomials cannot evade the obstruction through ramification or
cancellation.  The rational ordinary coefficients but integral Hurwitz
coefficients in $\phi$ are exactly what escape (A6).

## 3. Genuine singularities of the composed function

The derivative (F'\) is rational with exactly two finite poles,



$$
w=1+i,\qquad w=1-i.
$$



The apparent pole at (w=2) in the arctangent argument is removable after
analytic continuation; it is not a pole of (F'\).  Therefore all finite
candidate singularities of (G\) solve



$$
\phi(z)=1+i\quad\hbox{or}\quad\phi(z)=1-i.      \tag{A8}
$$



They are all genuine.  Indeed,



$$
G'(z)=
 \frac{4\phi'(z)}
 {(\phi(z)-(1+i))(\phi(z)-(1-i))}.               \tag{A9}
$$



Suppose $\phi(z)-(1+i)=(z-z_0)^mh(z)$, with (h(z_0)\ne0\).  In
characteristic zero its derivative has order exactly (m-1), while the
second denominator factor in (A9) equals (2i\) at (z_0).  Hence (G'\)
has a simple pole.  The same argument works for (1-i).  Each root in (A8)
is consequently a logarithmic singularity of the continued germ, and the
Taylor radius of (G\) is exactly the least modulus among those roots.

## 4. Schur--Cohn convention and the five exact gaps

Let



$$
q(z)=\phi(z)-(1+i),\qquad r=\sqrt2.
$$



Since (q(0)\ne0\), the change (w=r/z\) bijects the five roots of (q) with
the roots of



$$
\begin{aligned}
 P_0(w)&=w^5q(r/w)\\
 &=-(1+i)w^5+\sqrt2w^4-\frac{\sqrt2}{3}w^2
   +\frac56w-\frac{\sqrt2}{6}.                  \tag{A10}
\end{aligned}
$$



Thus all roots of (q) lie outside $|z|=\sqrt2$ exactly when every root
of (P_0) lies in the open unit disk.

The coefficient convention in the source is the following.  For



$$
P(w)=a_0w^n+a_1w^{n-1}+\cdots+a_n,
$$



put



$$
P^*(w)=\overline{a_n}w^n+\overline{a_{n-1}}w^{n-1}
 +\cdots+\overline{a_0}.                         \tag{A11}
$$



When $|a_0|>|a_n|$, Cohn's degree-reduction rule in precisely this
leading-to-constant convention is



$$
\mathcal S(P)(w)=
 \frac{\overline{a_0}P(w)-a_nP^*(w)}w.          \tag{A12}
$$



The constant term in the numerator is
$\overline{a_0}a_n-a_n\overline{a_0}=0$, while its leading coefficient is
$|a_0|^2-|a_n|^2>0$; hence (A12) really has degree (n-1).  Cohn's rule
says that (P) has all (n) roots in the open disk if and only if (A12) has
all (n-1) roots there.  One way to see the zero count is to use
$|P^*(w)|=|P(w)|$ on $|w|=1$: the first term in the numerator dominates
the second, and the forced zero at (w=0\) accounts for the one-degree drop.
The boundary case follows by the usual limiting form and is detected by a
zero gap at some stage.  Thus strict positivity of every successive gap and
a nonzero final constant is the required certificate.

I recomputed the recursion without SymPy and without the audited script.  An
element of $\mathbb Q(\sqrt2,i)$ was represented exactly as a rational
four-tuple



$$
a+b\sqrt2+i(c+d\sqrt2),
$$



and (A11)--(A12) were applied coefficient by coefficient.  The successive
degrees and gaps are



$$
\begin{array}{c|c}
\deg P&|a_0|^2-|a_n|^2\\ \hline
5&\dfrac{35}{18}\\[2mm]
4&\dfrac{919}{324}\\[2mm]
3&\dfrac{90755}{13122}\\[2mm]
2&\dfrac{31025233225}{816293376}\\[2mm]
1&\dfrac{20206728833189212829375}{60719765548297125888}
\end{array}                                      \tag{A13}
$$



The final degree-zero polynomial is exactly the last positive rational in
(A13).  This independently confirms the convention, the recursion, and all
five source values.  Hence every root of (P_0) is in the open unit disk,
every root of $\phi(z)=1+i$ is outside $|z|=\sqrt2$, and conjugation gives
the same for (1-i).  Together with Section 3,



$$
\rho(G)>\sqrt2                                   \tag{A14}
$$



is a rigorous exact theorem.

## 5. Numerical root diagnostic

As a separate check, I solved the original degree-five polynomial with
`mpmath.polyroots` at 100 decimal digits, rather than the SymPy root routine
used by the audited certificate.  The least two moduli were



$$
\begin{aligned}
 1.4597454685987641723304126458569750\ldots,\\
 1.5337715423135480552862624388377889\ldots.
\end{aligned}
$$



The least root was



$$
0.30697678579809387946212248584918\ldots
 +1.42710268939403824043791725188847\ldots,i,
$$



with polynomial residual about (1.43\times10^{-101}\).  The observed gaps
are



$$
\rho_{\rm num}-\sqrt2
 =0.0455319062256691235287\ldots,                \tag{A15}
$$





$$
\rho_{2,\rm num}-\rho_{\rm num}
 =0.0740260737147838829558\ldots.                \tag{A16}
$$



These separations and residuals make the displayed decimal stable.  They are
still only numerical diagnostics; the strict inequality (A14) rests solely on
the exact table (A13).

## 6. Independent audit of all 15 HP records

Write ordinary-coefficient polynomials



$$
B(z)=\sum_{j=0}^nb_jz^j,\qquad
 C(z)=\sum_{j=0}^nc_jz^j.
$$



For (n+1\leq k\leq3n\), the high derivative equations are



$$
\sum_{j=0}^n(k)_j\bigl(b_j+c_jG^{(k-j)}(0)\bigr)=0, \tag{A17}
$$



and the endpoint row is



$$
-\sum_{j=0}^nb_j+\sum_{j=0}^nc_j=0.            \tag{A18}
$$



This is a $(2n+1)$-by-$(2n+2)$ integer matrix.  For a kernel vector, the
low equations reconstruct



$$
a_k=-\frac1{k!}\sum_{j=0}^k(k)_j
 \bigl(b_j+c_jG^{(k-j)}(0)\bigr),
 \qquad0\leq k\leq n,                            \tag{A19}
$$



and the first unconstrained ordinary Taylor coefficient is



$$
[z^{3n+1}](A+Be^z+CG)
 =\sum_{j=0}^n
 \frac{b_j+c_jG^{(3n+1-j)}(0)}{(3n+1-j)!}.       \tag{A20}
$$



The independent audit generated the jets by (A3)--(A5), formed (A17)--(A18),
and used rational Gauss--Jordan elimination rather than the original domain
matrix nullspace.  A hand-written integer Bareiss determinant independently
recovered one maximal cofactor and its common-content quotient.  After full
triple denominator clearing and gcd reduction, every one of the 15 records
matched the archive in all checked fields:

1. shape, full row rank, and nullity one;
2. primitive high-kernel SHA-256 digest;
3. maximal-cofactor common-content digit count;
4. primitive-triple height and SHA-256 digest;
5. raw endpoint pair, its full gcd, and the reduced endpoint pair;
6. exact numerator and denominator of (A20); and
7. directed endpoint sign and both bounding base-ten decades.

For the endpoint certification I used independent rational bounds: the
exponential series through order (300) with a geometric tail majorant,
adjacent alternating sums through (500,501) for $\arctan(1/5)$, adjacent
sums through (120,121) for $\arctan(1/239)$, and Machin's identity for
$\pi$.  The independently certified signs and decades are



$$
\begin{array}{c|rrrrrrrrrrrrrrr}
n&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15\\ \hline
\operatorname{sgn}&+&-&-&-&+&-&+&-&+&-&-&-&+&+&-\\
\lfloor\log_{10}|L_n|\rfloor
&0&2&9&19&34&53&77&106&138&176&219&263&318&374&439
\end{array}                                      \tag{A21}
$$



Thus the source's decade row is exact.  The original radius/jet certificate
and the original HP probe were also rerun with their archived arguments; both
regenerated JSON files were byte-for-byte identical to the saved results.
All statements in this section remain finite certificates, not asymptotic
claims.

## 7. Independent artifacts

```text
8bfa7cea37f8f3541e4e6243dd19658314aaa8cb6e57cffe52e5f623973389af  scripts/improved_composed_pullback_independent_audit.py
b66c92a9c3316a4adb6e2ef1edee4160242c0efbeb125403fbfc738843582455  results/improved_composed_pullback_independent_audit.json
```

The JSON explicitly separates its exact Schur, Bell-jet, and HP fields from
the high-precision root diagnostic.
