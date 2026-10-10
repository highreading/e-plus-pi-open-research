> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 414 — Forced interval divisor and large-prime normalization of the compatible scalar carrier

Date: 2026-09-01  
Status: **WORK ONLY, UNAUDITED, NO CENTRAL EDIT, NO BOOKING**

## 1. Capacity-first verdict

Canonical Item 410 defines the phase-independent rational scalars



$$
\begin{aligned}
 E_m&=\sum_{j=0}^{3m}(-1)^j\binom{6m}{2j}
 \binom{m-\tfrac12-j}{4m},\\
 O_m&=\sum_{j=0}^{3m-1}(-1)^j\binom{6m}{2j+1}
 \binom{m-\tfrac32-j}{4m},
\end{aligned}                                             \tag{1.1}
$$



and



$$
W_m=\gcd\bigl(|\nu(E_m)|,|\nu(O_m)|\bigr),              \tag{1.2}
$$



whenever the two numerators are not both zero.  It proposed
$\log\operatorname{rad}W_m=o(m)$ as one possible arithmetic target.
That target is not viable: $W_m$ contains a compulsory prime interval of
positive linear Chebyshev mass.

Define



$$
\boxed{Q_m=\prod_{\substack{\ell\ \text{prime}\\4m<\ell<6m}}\ell.}
                                                               \tag{1.3}
$$



The main theorem of this item is



$$
\boxed{Q_m\mid \nu(E_m),\nu(O_m),\qquad
        Q_m\mid W_m,J_{m,0},J_{m,2}}                         \tag{1.4}
$$



for every $m\ge1$, with integer-gcd divisibility read in the usual way
and radical statements restricted to nonzero carriers.  Consequently,
along every sequence on which $W_m$, or either phase carrier, is nonzero,



$$
\min\!\left\{\log\operatorname{rad}W_m,\,
               \log\operatorname{rad}J_{m,\delta}\right\}
 \ge \vartheta(6m)-\vartheta(4m)=2m+o(m)                     \tag{1.5}
$$



by the classical prime number theorem.  A hypothetical value
$E_m=O_m=0$ does not rescue the proposed carrier bound: it makes the
integer carrier degenerate and the support inequality vacuous.

The correct zero-density target strips the irrelevant small primes:



$$
\boxed{
 \log\operatorname{rad}_{>6m}(W_m)=o(m),
 \qquad
 \operatorname{rad}_{>y}(N):=
 \prod_{\substack{\ell>y\\ \ell\mid N}}\ell.}                \tag{1.6}
$$



For the sharper phase carrier $J_{m,\delta}$, the analogous target is
the sum of the two phasewise large-prime radicals, or the all-support
statement $\operatorname{rad}_{>6m}J_{m,\delta}=1$.  Its **full**
radical has the same compulsory $Q_m$ obstruction.  Item 414 proves no
large-prime theorem and therefore changes neither the booking nor the
capacity ledger.

### Provenance: this is a transport theorem, not a new Cartier source

Canonical Item 200 already proves that the earlier raw residue pair has the
complete forced Cartier divisor



$$
F_m=G_m,\qquad
 \log F_m=\mathfrak C m+o(m),\qquad
 \mathfrak C=-4\log2+\frac{\pi}{\sqrt3}+3\log3
 =2.3370475079\ldots .                                      \tag{1.7}
$$



Its $j=0$ interval strip is



$$
D_m=\prod_{\substack{4m+1<p\le6m\\p\ {\rm prime}}}p.
$$



Because $6m$ is composite,



$$
Q_m=D_m\,B_m,\qquad
 B_m=\begin{cases}4m+1,&4m+1\ {\rm prime},\\1,&\text{otherwise}.
 \end{cases}                                                \tag{1.8}
$$



Thus $Q_m$ has the same $2m+o(m)$ rate as Item 200's already known
$j=0$ strip; the optional boundary prime contributes only $O(\log m)$.
The new result here is specifically that this strip, including the boundary
case, divides the later Item-410 scalar carriers $W_m,J_{m,0},J_{m,2}$.
It corrects the normalization of their raw-radical target.  It is not a
new divisor booking, and it does not duplicate the already booked
$F_m=G_m$ content.

## 2. PROVED — the forced divisor of $E_m$ and $O_m$

Fix a prime $\ell$ with $4m<\ell<6m$, and put



$$
a=6m-\ell.
$$



Then $a$ is odd and



$$
1\le a<2m<\ell,qquad 6m=\ell+a.                            \tag{2.1}
$$



All denominators in (1.1) are powers of two after reduction, and
$\ell>4m\ge4$.  Hence $2$, $4$, and $(4m)!$ are $\ell$-adic
units.  For $x\in\mathbb Z_{(\ell)}$, therefore,



$$
\binom{x}{4m}\equiv0\pmod\ell
 \quad\Longleftrightarrow\quad
 x\bmod\ell\in\{0,1,\ldots,4m-1\}.                          \tag{2.2}
$$



Lucas' theorem applied to $6m=\ell+a$ gives, for
$0\le r\le6m$,



$$
\binom{6m}{r}\not\equiv0\pmod\ell
 \quad\Longrightarrow\quad
 r\le a\quad\hbox{or}\quad r=\ell+s\ (0\le s\le a).       \tag{2.3}
$$



Consider first an even index $r=2j$ from $E_m$, and write



$$
x=m-\frac{r+1}{2}.
$$



If $r\le a$, then $r\le a-1$, and the integer representative



$$
u=\frac{2m-r-1+\ell}{2}
   =4m-\frac{a+r+1}{2}                                     \tag{2.4}
$$



lies in $[0,4m-1]$.  If $r=\ell+s$, parity forces
$1\le s\le a$ odd, and



$$
u=\frac{2m-s-1}{2}\in[0,m-1]                              \tag{2.5}
$$



represents the same residue $x\bmod\ell$.  Thus every term of $E_m$
either has $\ell\mid\binom{6m}{r}$, or has its generalized binomial
factor divisible by $\ell$.  Hence $\ell\mid\nu(E_m)$.

For an odd index $r=2j+1$ from $O_m$, put



$$
x=m-1-\frac r2.
$$



If $r\le a$, the representative



$$
u=\frac{2m-2-r+\ell}{2}
   =4m-\frac{a+r+2}{2}\in[0,4m-1].                          \tag{2.6}
$$



If $r=\ell+s$, then $s$ is even with $0\le s\le a-1$, and



$$
u=m-1-\frac s2\in[0,m-1].                                 \tag{2.7}
$$



Again (2.2) kills the generalized binomial whenever the ordinary binomial
survives Lucas.  Therefore $\ell\mid\nu(O_m)$.  Multiplying over the
distinct primes in (1.3) proves (1.4).  The endpoints cause no exception:
$4m$ and $6m$ are composite for $m\ge1$, while every prime in the
open interval is at least $5$; in particular neither $2$ nor $3$
enters the argument.

## 3. PROVED — the forced factor in both phases of $J_{m,\delta}$

Canonical Item 410 also defines



$$
\begin{aligned}
 U_{m,\delta}
 &=\sum_{\substack{0\le h\le10m+1\\h\equiv\delta\ (4)}}
 (-1)^h\binom{10m+1}{h}
 \binom{(10m-1-h)/4}{4m},\\
 V_{m,\delta}
 &=\sum_{\substack{0\le h\le10m+1\\h\equiv\delta-1\ (4)}}
 (-1)^h\binom{10m+1}{h}
 \binom{(10m-2-h)/4}{4m},                                  \tag{3.1}
\end{aligned}
$$



for $\delta\in\{0,2\}$, and lets $J_{m,\delta}$ be the gcd of the
four reduced numerators in (1.1) and (3.1).

For a prime $\ell$ in (1.3), define its matching phase



$$
\delta_\ell\equiv\ell-6m-1\pmod4,
 \qquad\delta_\ell\in\{0,2\}.                              \tag{3.2}
$$



The stronger all-phase theorem is



$$
\boxed{Q_m\mid J_{m,0},\qquad Q_m\mid J_{m,2}.}             \tag{3.3}
$$



First set $n_\ell=\ell-6m-1<0$.  For a summand of
$U_{m,\delta_\ell}$, the integer



$$
b=4m+\frac{n_\ell-h}{4}
   =\frac{10m+\ell-1-h}{4}                                 \tag{3.4}
$$



satisfies $0\le b<4m$, because $0\le h\le10m+1$ and
$h\equiv n_\ell\pmod4$.  Modulo $\ell$, its residue is exactly
$(10m-1-h)/4$, so (2.2) kills every summand.  The same argument for
$V$, with



$$
b=4m+\frac{n_\ell-1-h}{4}
   =\frac{10m+\ell-2-h}{4},                                 \tag{3.5}
$$



again gives $0\le b<4m$ and kills every summand in the matching phase.

It remains to treat the opposite phase
$\bar\delta_\ell=\delta_\ell+2\pmod4$.  Put



$$
n'_\ell=n_\ell+2\ell=3\ell-6m-1,
 \qquad k=4m+1,\quad N=10m+1,\quad h_\ell=\ell-k.            \tag{3.6}
$$



The coefficient formula for



$$
S_m(z)=\frac{(1-z)^N}{(1-z^4)^k}
$$



shows, because $n'_\ell\equiv\bar\delta_\ell\pmod4$ and



$$
4m+\frac{n'_\ell-h}{4}
 \equiv\frac{10m-1-h}{4}\pmod\ell,
$$



with the analogous congruence for $n'_\ell-1$ and $10m-2-h$, that

the terms beyond the ordinary coefficient range cause no extension error.
Indeed, if $h>n'_\ell$, then



$$
0<
 4m+\frac{n'_\ell-h}{4}<4m,
 \qquad
 4m+\frac{n'_\ell-h}{4}
 \ge\frac{3\ell-2}{4},
$$



because $h\le N=10m+1$; the generalized binomial is therefore zero
modulo $\ell$.  The $V$-sum has the same property, with lower bound
$(3\ell-3)/4$.  Consequently the full scalar sums, not merely their
truncations, satisfy



$$
U_{m,\bar\delta_\ell}\equiv[z^{n'_\ell}]S_m,\qquad
 V_{m,\bar\delta_\ell}\equiv[z^{n'_\ell-1}]S_m\pmod\ell.    \tag{3.7}
$$



Here $0<n'_\ell<4\ell$.  In $\mathbb F_\ell[[z]]$,



$$
\frac1{(1-z^4)^k}
 =\frac{(1-z^4)^{\ell-k}}{1-z^{4\ell}},
$$



so both coefficients in (3.7) equal those of



$$
P(z)=(1-z)^N(1-z^4)^{h_\ell}.                              \tag{3.8}
$$



Let $a=6m-\ell$ as in Section 2 and
$A(z)=1+z+z^2+z^3$.  Since $1-z^4=(1-z)A(z)$,
$6m=\ell+a$, and $(1-z)^\ell=1-z^\ell$ in
$\mathbb F_\ell[z]$,



$$
\begin{aligned}
 P(z)
 &=(1-z)^{\ell+6m}A(z)^{h_\ell}\\
 &=(1-z^\ell)^2R(z),\\
 R(z)&=(1-z)^aA(z)^{h_\ell},\qquad
 \deg R=a+3h_\ell=\ell-a-3.                                 \tag{3.9}
\end{aligned}
$$



But



$$
n'_\ell-1=2\ell-a-2,\qquad n'_\ell=2\ell-a-1.              \tag{3.10}
$$



The middle support band of $(1-z^\ell)^2R$ ends at
$\ell+\deg R=2\ell-a-3$, while its last band begins at $2\ell$.
Thus the two degrees in (3.10) lie in an exact two-coefficient gap, and
both coefficients in (3.7) vanish.  The prime $\ell$ therefore divides
all four scalar numerators in either phase.  Multiplication over the
distinct interval primes proves (3.3).

This proof does not use, and does not prove, Item 410's finite observation
that the complete integers $J_{m,0}$ and $J_{m,2}$ agree through
$m=128$.  It proves only their common compulsory divisor $Q_m$.

## 4. Correct large-prime carrier and height screen

Let $\mathcal P_H(m)$ be the actual compatible $H$-collision primes
from Item 410.  Every such prime is strictly larger than $6m$.  Hence the
Item-410 carrier implication sharpens tautologically but importantly to



$$
\boxed{
 \sum_{p\in\mathcal P_H(m)}\log p
 \le\log\operatorname{rad}_{>6m}(W_m).}                    \tag{4.1}
$$



Equivalently one may split the left side by $p-6m-1\pmod4$ and use the
two large-prime parts of $J_{m,0}$ and $J_{m,2}$.  All factors in
$Q_m$ are therefore irrelevant to the actual collision support and must
be removed before interpreting the carrier arithmetically.

When $W_m>0$, (1.4) and the Item-410 height estimate give



$$
\operatorname{rad}_{>6m}(W_m)
 \le \frac{W_m}{Q_m}
 \le \frac{2^{14m}(6m)^{4m}}{(4m)!\,Q_m}.                  \tag{4.2}
$$



Using the classical prime number theorem in (1.5), the normalized constant
is at most



$$
\frac{14\log2+4\log(3e/2)}6-\frac13
 =2.2209868267\ldots .                                     \tag{4.3}
$$



This is a valid improvement over the raw Item-410 height constant
$2.5543201600\ldots$, but it is still much worse than the inherited
combined ceiling



$$
\frac{\log136}{6}=0.8187758142\ldots .                    \tag{4.4}
$$



It therefore produces no capacity reduction.  The smallest useful open
lemma exposed by the normalization is not a full-radical statement but



$$
\boxed{\log\operatorname{rad}_{>6m}(W_m)=o(m)}             \tag{4.5}
$$



together with uniform nonresonance, or the sharper phasewise analogue for
$J_{m,\delta}$.  Perfect phasewise exclusion would close the compatible
$H$-stratum, but the primitive branch can still occupy the full combined
Item-390 ceiling, so even that success has no presently proved standalone
numerical ceiling reduction.

## 5. Strict labels

### PROVED

* The all-$m$ forced divisor $Q_m\mid\nu(E_m),\nu(O_m)$, hence
  $Q_m\mid W_m$ whenever $W_m>0$.
* The all-phase refinement $Q_m\mid J_{m,0},J_{m,2}$.
* The exact provenance $Q_m=D_mB_m$ relative to Item 200's already
  forced $F_m=G_m$, with only an optional boundary-prime difference.
* The corrected actual-support carrier (4.1).
* The stripped height estimate (4.2) and its PNT corollary (4.3).
* Zero booking and zero proved capacity reduction.

### EXACT FINITE ONLY

* Certificate normalization rows for the displayed rational sums.
* All Item-410 phase equality and support observations through $m=128$.

### OPEN

* Uniform exclusion of $E_m=O_m=0$.
* The corrected large-prime zero-density bound (4.5).
* Uniform support of both phase carriers in primes at most $6m$.
* The four-adjacent lemma, primitive/marked branch control, Route 1, and
  irrationality of $e+\pi$.

### NOT CLAIMED

* That either full radical has zero rate; $W_m$ and both
  $J_{m,\delta}$ have a compulsory positive-rate factor whenever defined.
* Any uniform multiplicity beyond the radical-one divisor $Q_m$.
* Any exhaustive no-go for other normalizations or carriers.

### BOOKING



$$
\boxed{\Delta r_{\rm booked}=0,
        \qquad\Delta C_{\rm total}^{\rm proved}=0.}         \tag{5.1}
$$



No canonical, master, status, checkpoint, or research-log file is edited by
this work package.

## 6. Replay

From the archive root run:

```text
python work/item414_mixed_scalar_forced_interval_normalization_certificate.py \
  --output work/item414_mixed_scalar_forced_interval_normalization_certificate.replay.json
```

The standard-library checker verifies the canonical Item-410 dependency
pins, the Lucas/root proof schema on transparent finite normalization rows,
the exact rational divisibilities on selected values of $m$, both the
matching-phase root argument and opposite-phase two-point gap, and
byte-stable replay.  Its finite rows are not
the proof of the all-$m$ theorem; the proof is the uniform argument in
Sections 2 and 3.  The checker does not claim to prove the prime number
theorem.
