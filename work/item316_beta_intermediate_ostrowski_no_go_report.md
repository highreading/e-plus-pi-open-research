> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Item 316 — the exact intermediate-window Ostrowski target and a fixed-precision 2-adic no-go

Checked: 2026-08-31 (Beijing time)

## 1. Strict verdict

Let



$$
q_0=q_1=1,
\qquad
q_n=(4n-2)q_{n-1}+q_{n-2}\quad(n\ge2),
\tag{1.1}
$$



and put



$$
A=4n-2,qquad a=q_{n-1},\quad b=q_n,\quad c=q_{n-2},
\qquad b=Aa+c.
\tag{1.2}
$$



For the actual centered square, write



$$
\kappa=\operatorname{nint}(a^2/b),
\qquad
r_{\rm act}=a^2-\kappa b,
\qquad
R_{\rm act}=|r_{\rm act}|.
\tag{1.3}
$$



Item 313 proves



$$
R_{\rm act}\ge \frac{a}{2c}.
\tag{1.4}
$$



Thus the remaining half-bound problem is exactly



$$
\frac{a}{2c}\le R_{\rm act}<\frac a2.
\tag{1.5}
$$



Item 316 gives a necessary-and-sufficient all-digit description of (1.5).
If $R=\sum\delta_{i+1}Q_i$ is the canonical Ostrowski expansion, define
the two signed dual sums



$$
E(\delta)=\sum_{i=0}^{m-1}\delta_{i+1}(-1)^i\Delta_i,
\qquad
U(\delta)=\sum_{i=0}^{m-1}\delta_{i+1}(-1)^{n+i}\widehat\Delta_i.
\tag{1.6}
$$



Then, for $n\ge5$, an actual half-bound failure is equivalent to



$$
\boxed{
\frac{a}{2c}\le R<\frac a2,qquad
0<|E(\delta)|<c,qquad
U(\delta)=(-1)^n\operatorname{sgn}(E(\delta))\,a.
}
\tag{1.7}
$$



All digit admissibility conditions are made explicit below.  In particular,
the actual nearest quotient is not a free multiplier:



$$
\boxed{\kappa=|E(\delta)|.}
\tag{1.8}
$$



There is no hidden endpoint carry.  The exact dual-error bound



$$
-S<E(\delta)<a-S,
\tag{1.9}
$$



together with $S>c$, rules out the apparent $E=\pm\kappa\pm a$
branches.  Thus the only target is the exact signed equality in (1.7), not
an additional $\pm(b-a)$ target.

This classification does not prove that (1.7) has no solution.  It does,
however, prove a global scoped no-go:

> **FIXED-PRECISION 2-ADIC NO-GO.**  For every fixed $s\ge1$ and all
> sufficiently large $n$, the exact continued-fraction word, canonical
> digits, intermediate-window inequalities, sign, and small dual error are
> compatible with the target congruence
> $U\equiv(-1)^n\operatorname{sgn}(E)a\pmod{2^s}$, while the exact target
> equality fails.

Therefore no argument retaining only a fixed $2^s$-truncation of the
Ostrowski target can close the intermediate window.  This does not rule out
a precision growing with $n$, the full 2-adic equality, an odd-modulus
square invariant, or a global modular-square theorem.

The centered half-bound, every proper-target consequence, and every beta
capacity reduction remain open.  Booking is zero.

## 2. Prefix and dual-tail coordinates

For $n\ge5$, set



$$
m=n-2,qquad
w_1=7,qquad w_i=4i+2\quad(2\le i\le m),
\tag{2.1}
$$



and put $B=w_m=A-4$.  Define convergent coordinates by



$$
Q_{-1}=0,\quad Q_0=1,
\qquad
P_{-1}=1,\quad P_0=0,
\tag{2.2}
$$





$$
Q_i=w_iQ_{i-1}+Q_{i-2},
\qquad
P_i=w_iP_{i-1}+P_{i-2}.
\tag{2.3}
$$



Then



$$
Q_m=a,qquad Q_{m-1}=c,qquad Q_{m-2}=d:=q_{n-3},
\qquad P_m=S,
\tag{2.4}
$$



and



$$
\frac Sa=[0;w_1,w_2,\ldots,w_m].
\tag{2.5}
$$



For $0\le i<m$, define



$$
\Delta_i=K(w_{i+2},\ldots,w_m),
\qquad
\widehat\Delta_i=K(w_{i+2},\ldots,w_m,A),
\tag{2.6}
$$



where an empty word has continuant $1$.  It is convenient to set



$$
\Delta_{-1}=a,qquad \Delta_0=S.
\tag{2.7}
$$



Euler's identities are



$$
Q_iS-P_i a=(-1)^i\Delta_i,
\tag{2.8}
$$



and the appended-tail bridge, including $i=0$, is



$$
\boxed{
b\Delta_i+(-1)^{n+i}Q_i=a\widehat\Delta_i.
}
\tag{2.9}
$$



All words in (2.6) are positive.  There is no negative-index continuant:
$\Delta_{-1}$ in (2.7) is a declared boundary coordinate, not a lookup.

The two length-$(m-1)$ words defining $S$ and $c$ are coefficientwise
strictly ordered, so



$$
S>c.
\tag{2.10}
$$



Splitting the word for $a$ after its first entry also gives



$$
a=7S+K(w_3,\ldots,w_m)>c+S.
\tag{2.11}
$$



## 3. Canonical Ostrowski digits and the exact half-language

Every integer $0\le R<a=Q_m$ has a unique expansion



$$
\boxed{R=\sum_{i=0}^{m-1}\delta_{i+1}Q_i}
\tag{3.1}
$$



with



$$
0\le\delta_1\le6,
\qquad
0\le\delta_i\le w_i\quad(2\le i\le m),
\tag{3.2}
$$



and the Markov condition



$$
\delta_i=w_i\quad\Longrightarrow\quad\delta_{i-1}=0
\qquad(2\le i\le m).
\tag{3.3}
$$



This is the ordinary greedy Ostrowski theorem.  It follows directly by
dividing first by $Q_{m-1}$ and recursing.  If the leading digit reaches
$w_m$, the remainder is below $Q_{m-2}$, which forces the next digit
to be zero; the same argument repeats at every level.

Because $a$ is odd, $R<a/2$ is equivalent to



$$
R\le H_m:=\frac{Q_m-1}{2}.
\tag{3.4}
$$



The digits of $H_m$ are exact.  From



$$
H_m=\frac{w_m}{2}Q_{m-1}+H_{m-2},
\tag{3.5}
$$



and $H_1=3$, they are



$$
\eta_i^{(m)}=
\begin{cases}
3,&i=1\text{ and }m\text{ is odd},\\
w_i/2,&i\ge2\text{ and }i\equiv m\pmod2,\\
0,&\text{otherwise}.
\end{cases}
\tag{3.6}
$$



Consequently the exact half-language condition is



$$
(\delta_m,\ldots,\delta_1)
\le_{\rm lex}
(\eta_m^{(m)},\ldots,\eta_1^{(m)}).
\tag{3.7}
$$



The comparison is non-strict because $(a-1)/2<a/2$.  Equations
(3.2), (3.3), and (3.7) are every digit/admissibility hypothesis used in
this item.

## 4. The exact dual-error lemma

Given the digits in (3.1), set



$$
P(\delta)=\sum_{i=0}^{m-1}\delta_{i+1}P_i,
\tag{4.1}
$$



and define $E(\delta)$ as in (1.6).  Summing (2.8) gives



$$
\boxed{E(\delta)=RS-P(\delta)a.}
\tag{4.2}
$$



The dual tails obey



$$
\Delta_{i-1}=w_{i+1}\Delta_i+\Delta_{i+1}.
\tag{4.3}
$$



The positive part of the alternating sum is bounded by



$$
(w_1-1)\Delta_0
+\sum_{\substack{2\le i<m\\i\equiv0\pmod2}}
w_{i+1}\Delta_i
\le a-\Delta_0=a-S,
\tag{4.4}
$$



because (4.3) telescopes.  The negative part similarly gives



$$
-\sum_{\substack{1\le i<m\\i\equiv1\pmod2}}
w_{i+1}\Delta_i
\ge-\Delta_0=-S.
\tag{4.5}
$$



Thus $-S\le E\le a-S$.  Equality at either endpoint would give



$$
E\equiv-S\pmod a,
$$



and (4.2), together with $\gcd(S,a)=1$, would force
$R\equiv-1\pmod a$.  Since $0\le R<a/2$, this is impossible.
Therefore



$$
\boxed{-S<E(\delta)<a-S.}
\tag{4.6}
$$



The same telescoping argument for the appended word gives



$$
-S_n<R S_n-P(\delta)b<b-S_n,
\tag{4.7}
$$



where $S_n=K(w_2,\ldots,w_m,A)$.  In particular, the appended signed
sum $U$ satisfies



$$
|U|<b.
\tag{4.8}
$$



Finally, multiplying (2.9) by
$\delta_{i+1}(-1)^{n+i}$ and summing gives the exact master identity



$$
\boxed{aU(\delta)=(-1)^n bE(\delta)+R.}
\tag{4.9}
$$



No bounded observation enters (4.6) or (4.9).

## 5. Necessary and sufficient actual-square target

Assume first that the actual square violates the half-bound.  Write



$$
r_{\rm act}=\epsilon R,\qquad \epsilon\in\{\pm1\},
\qquad R<a/2.
\tag{5.1}
$$



For $n\ge5$, one has $0<\kappa<c$, directly from the recurrences.
Indeed, $c\ge q_3=71$, $d<c$, and $c>A$; the last inequality follows
from the base row $q_3=71>18$ and induction.  Therefore
$a=(A-4)c+d>A+1$, while $b=Aa+c<(A+1)a<a^2$, so $a^2/b>1$.
Moreover,



$$
bc-a^2=a(4c-d)+c^2>3ac+c^2>\frac b2.
$$



The last inequality is equivalent to
$a(6c-A)+c(2c-1)>0$.  Hence



$$
1<\frac{a^2}{b}<c-\frac12,
\qquad 1\le\kappa\le c-1.
$$



The exact inverse congruence from Items 302 and 305 is



$$
\kappa\equiv\sigma RS\pmod a,
\qquad
\sigma=(-1)^n\epsilon.
\tag{5.2}
$$



Because $E\equiv RS\pmod a$, there is an integer $z$ such that



$$
E=\sigma\kappa+za.
\tag{5.3}
$$



The carry is exactly zero.  If $z\ge1$, then the smallest possible
right side is $a-\kappa>a-c>a-S$, contradicting (4.6).  If $z\le-1$,
then the largest possible right side is $-a+\kappa<-a+c<-S$, using
(2.11).  Hence



$$
\boxed{z=0,\qquad E=\sigma\kappa.}
\tag{5.4}
$$



This proves (1.8) and fixes every sign.  Substituting (5.4) and
$a^2=b\kappa+\epsilon R$ into (4.9) gives



$$
\boxed{U=\epsilon a
=(-1)^n\operatorname{sgn}(E)\,a.}
\tag{5.5}
$$



Item 313 supplies the lower inequality in (1.7).

Conversely, suppose a canonical digit word satisfies



$$
\frac{a}{2c}\le R<a/2,qquad 0<|E|<c,
\qquad U=(-1)^n\operatorname{sgn}(E)a.
\tag{5.6}
$$



Put



$$
\kappa=|E|,qquad
\sigma=\operatorname{sgn}(E),qquad
\epsilon=(-1)^n\sigma.
\tag{5.7}
$$



Multiplying (4.9) by $\epsilon$ gives



$$
a^2=b\kappa+\epsilon R.
\tag{5.8}
$$



Since $R<a/2<b/2$, $\kappa$ is the unique nearest integer to
$a^2/b$, and $\epsilon R$ is its actual centered remainder.
This proves both directions of (1.7).

The classification is genuinely all-digit.  Item 313 applies after the
smaller window collapses the word to one supported convergent multiplier.
Nothing in Item 313 gives a valuation for the general alternating sum
$U(\delta)$.

## 6. Exact fixed-precision witnesses

Fix $s\ge1$, and let



$$
M=2^{s-1}.
\tag{6.1}
$$



Take



$$
n\ge N_s:=\max\{6,M+2\}.
\tag{6.2}
$$



Then $B/2=2n-3\ge2M$.  Since $A/2=2n-1$ is odd, the congruence



$$
\frac A2\,\kappa_*
\equiv\frac{a-1}{2}\pmod M
\tag{6.3}
$$



has one residue class modulo $M$.  The interval



$$
\frac B2<\kappa_*\le B
\tag{6.4}
$$



contains at least two representatives of that class.  Choose one which is
not $(a-1)/A$ when the latter is an integer, and set



$$
g=B-\kappa_*.
\tag{6.5}
$$



Thus $0\le g<B/2$.  Use the canonical digit word



$$
\delta_{m-1}=1,qquad \delta_m=g,qquad
\delta_i=0\quad(i\ne m-1,m).
\tag{6.6}
$$



It gives the exact coordinates



$$
\boxed{
R_*=gc+d,qquad
E_*=(-1)^n(B-g)=(-1)^n\kappa_*,
\qquad
U_*=A(B-g)+1=A\kappa_*+1.
}
\tag{6.7}
$$



The word is admissible.  Its window is exact:



$$
\frac{a}{2c}<d\le R_*<\frac a2,
\tag{6.8}
$$



for $n\ge6$.  The first inequality follows from
$d=q_{n-3}>B/2+1/2>a/(2c)$; the second uses
$g\le B/2-1$, $d<c$, and $a=Bc+d$.  Also



$$
0<\kappa_*\le B<c.
\tag{6.9}
$$



The dual sign is exactly the positive-square sign:



$$
(-1)^n\operatorname{sgn}(E_*)=1.
\tag{6.10}
$$



Direct recurrence arithmetic gives



$$
\boxed{b\kappa_*+R_*=aU_*.}
\tag{6.11}
$$



Equation (6.3) is precisely



$$
U_*\equiv a\pmod{2^s},
\tag{6.12}
$$



so



$$
a^2\equiv b\kappa_*+R_*\pmod{2^s}.
\tag{6.13}
$$



But the choice in (6.4) makes $U_*\ne a$, and therefore



$$
a^2\ne b\kappa_*+R_*.
\tag{6.14}
$$



These are exact witnesses, not a scan.  They satisfy every declared
continued-fraction, digit, sign, dual-error, window, and fixed-
$2^s$ square congruence, but they are deliberately not the actual nearest
square.

This proves the scoped information-class no-go:



$$
\boxed{
\text{exact CF/Ostrowski/window data plus a fixed }2^s
\text{ target congruence do not imply target exclusion.}
}
\tag{6.15}
$$



The modulus is fixed before $n$ grows.  The theorem says nothing against
using the exact equality, a modulus whose precision grows with $n$, odd
prime factors of $b$, or a global modular-square distribution theorem.

## 7. Relation to Item 313 and remaining arithmetic

Item 313's transfer congruence remains exact and useful in its proved
scope.  In the smaller Item-305 window, Legendre's theorem forces one
supported multiplier and the square identity becomes one appended-tail
divisibility.  Item 313 then obtains incompatible 2-adic valuations.

In (1.5), the exact state is instead the full signed sum (1.6).  Even the
two-top-digit witnesses (6.6) give the inhomogeneous coordinate



$$
U_*=A\kappa_*+1,
\tag{7.1}
$$



not a single block divisor.  Applying the Item-313 valuation to individual
tails does not control cancellation in $U$.  Section 6 proves that no
fixed-precision truncation repairs this gap.

The smallest remaining exact lemma is therefore



$$
\boxed{
U(\delta)\ne(-1)^n\operatorname{sgn}(E(\delta))a
}
\tag{7.2}
$$



for every canonical half-language word with
$a/(2c)\le R<a/2$ and $0<|E|<c$.  This is an exact all-digit target,
not a finite search instruction.

An odd-modulus or full modular-square invariant may still exclude (7.2).
No such invariant is proved here.

## 8. Small indices, endpoints, and denominator audit

The theorem above uses $n\ge5$, where $m\ge3$,
$0<\kappa<c$, and Item 313 applies.  The exact smaller rows are



$$
\begin{array}{c|ccc}
n&a&c&R_{\rm act}\\ \hline
2&1&1&1\\
3&7&1&22\\
4&71&7&36
\end{array}
\tag{8.1}
$$



and none violates the half-bound.

All moduli $a,b$ are odd, so nearest integers and centered residues are
unique; there is no half-integer tie.  All modular divisions in Sections 5
and 6 are by odd numbers.  For $s=1$, (6.3) is read modulo $1$, and the
construction remains valid.  Empty dual tails use $K(\varnothing)=1$.
There are no analytic functions or poles.

## 9. Proper targets, product baseline, and capacity

The theorem concerns only the full modulus $b=q_n$.  A lower bound for
its centered remainder would not automatically descend to a proper
de-overlapped divisor $Q\mid b$.  No proper target is constructed or
bounded here.

Item 282's common coefficient/product baseline is independent of this
additive nearest-square problem and is unchanged.

### PROVED

* Canonical Ostrowski existence, uniqueness, and the exact half-language.
* The strict dual-error lemma (4.6).
* Elimination of every endpoint carry in (5.3).
* The necessary-and-sufficient actual target (1.7), including the exact
  nearest quotient $\kappa=|E|$.
* The fixed-precision witness theorem (6.1)-(6.14).

### PROVED SCOPED INFORMATION-CLASS NO-GO

* Exact CF/Ostrowski/window/sign data plus any fixed $2^s$ truncation of
  the square target do not force exclusion.
* This does not cover growing precision, full equality, odd moduli, or
  global modular-square invariants.

### EXACT FINITE ONLY

* The deterministic replay's declared digit and witness control rows.
  They replay the symbolic identities and are not promoted into the
  all-$n$ theorems.

### OPEN

* The all-digit exclusion (7.2) and the centered half-bound.
* A growing/full 2-adic or odd-modulus modular-square invariant.
* Any proper-target consequence or beta capacity reduction.
* Route 1 and every conclusion about $e+\pi$.

### BOOKING



$$
\boxed{
\text{new beta capacity reduction}=0,
\qquad
\text{new Route-1 rate}=0.
}
\tag{9.1}
$$



No canonical, master, status, or research-log file is edited by this work
package.

## 10. Deterministic replay

From the archive root:

~~~text
python work/item316_beta_intermediate_ostrowski_no_go_certificate.py ^
  --output work/item316_beta_intermediate_ostrowski_no_go_certificate.replay.json
~~~

The checker uses only the Python standard library and exact integer
arithmetic.  It performs no half-bound scan and promotes no bounded row.
