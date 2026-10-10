> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Endpoint-matched Hermite--Padé analysis for the Möbius arctangent pullback

Date: 2026-08-26

## Status

This note studies the endpoint-matched type-I Hermite--Padé family for



$$
F(z)=4\arctan\frac{z}{2-z},\qquad F(1)=\pi,
$$



with



$$
R_n(z)=A_n(z)+B_n(z)e^z+C_n(z)F(z),\qquad
 \deg A_n,\deg B_n,\deg C_n\le n,
$$



subject to



$$
R_n(z)=O(z^{3n+1}),\qquad C_n(1)=B_n(1).       \tag{1}
$$



The results below are rigorous but deliberately limited:

* an exact period-eight jet formula and differential recurrence;
* a stronger forced divisor of every maximal cofactor;
* a sharpened primitive-height upper bound, conditional only on full row
  rank of the defining matrix;
* exact modular certificates of rank, endpoint nonvanishing, and exact zero
  order for every $1\le n\le100$, with the endpoint exception at $n=1$;
* exact tail and integral remainder formulas.

None of these results proves that the endpoint forms tend to zero.  In the
finite exact data they instead grow rapidly.  Nothing here proves
irrationality, algebraicity, or transcendence of $e+\pi$.

## 1. Exact jets, including the period-eight form

Put



$$
\tau_k=F^{(k)}(0).
$$



Direct differentiation gives



$$
F'(z)=\frac4{z^2-2z+2}.                         \tag{2}
$$



If $k\ge1$, partial fractions at $1\pm i$, or the coefficient
recurrence from (2), gives



$$
\boxed{\tau_k=4(k-1)!\,2^{-k/2}\sin\frac{k\pi}{4}.} \tag{3}
$$



Thus, for $q\ge0$, the fully rational period-eight version is



$$
\begin{array}{c|c}
k&\tau_k\\ \hline
8q+1&\displaystyle \frac{2(8q)!}{16^q}\\[4pt]
8q+2&\displaystyle \frac{2(8q+1)!}{16^q}\\[4pt]
8q+3&\displaystyle \frac{(8q+2)!}{16^q}\\[4pt]
8q+4&0\\[2pt]
8q+5&\displaystyle-\frac{(8q+4)!}{2\,16^q}\\[4pt]
8q+6&\displaystyle-\frac{(8q+5)!}{2\,16^q}\\[4pt]
8q+7&\displaystyle-\frac{(8q+6)!}{4\,16^q}\\[4pt]
8q+8&0.
\end{array}                                                    \tag{4}
$$



In particular the signs are



$$
(+,+,+,0,-,-,-,0)\quad\hbox{for }k\pmod 8.       \tag{5}
$$



The equivalent period-four formula is



$$
\begin{aligned}
 \tau_{4q+1}&=(-1)^q\frac{2(4q)!}{4^q},&
 \tau_{4q+2}&=(-1)^q\frac{2(4q+1)!}{4^q},\\
 \tau_{4q+3}&=(-1)^q\frac{(4q+2)!}{4^q},&
 \tau_{4q+4}&=0.                                  \tag{6}
\end{aligned}
$$



Legendre's formula immediately shows that all these numbers are integers.
The identity $(z^2-2z+2)F'(z)=4$ also gives the independent recurrence



$$
2\tau_{m+1}-2m\tau_m+m(m-1)\tau_{m-1}=0
 \qquad(m\ge1).                                  \tag{7}
$$



The modular certificate script checks (7) at every jet that it uses; it
does not extrapolate the sequence from signs alone.

## 2. The exact integer matrix

Write



$$
B(z)=\sum_{j=0}^n b_jz^j,\qquad
 C(z)=\sum_{j=0}^n c_jz^j.
$$



Order the unknown vector as



$$
(b_0,\ldots,b_n,c_0,\ldots,c_n).
$$



For each $k=n+1,\ldots,3n$, the high-jet row is



$$
\bigl((k)_0,\ldots,(k)_n,
       (k)_0\tau_k,(k)_1\tau_{k-1},\ldots,(k)_n\tau_{k-n}\bigr), \tag{8}
$$



where $(k)_j=k!/(k-j)!$.  The last row is



$$
(-1,\ldots,-1,1,\ldots,1),                     \tag{9}
$$



which is exactly $C(1)-B(1)=0$.  Denote the resulting
$(2n+1)$-by-$(2n+2)$ integer matrix by $M_n$.

Once $(B,C)$ has been found, the low coefficients are



$$
[z^k]A=-\frac1{k!}\sum_{j=0}^k
 (k)_j\bigl(b_j+c_j\tau_{k-j}\bigr),\qquad 0\le k\le n. \tag{10}
$$



Consequently multiplication by $n!$ clears every coefficient of $A$.
At the endpoint, (1) becomes



$$
R_n(1)=A_n(1)+B_n(1)(e+\pi).                    \tag{11}
$$



## 3. A forced divisor of all maximal cofactors

For a nonnegative integer $r$, let



$$
\operatorname{odd}(r!)=\frac{r!}{2^{v_2(r!)}}.
$$



For $t\ge0$, define



$$
q_t=\left\lfloor\frac{t+1}{4}\right\rfloor,
 \qquad
 \delta_t=2q_t+1-s_2(q_t),
 \qquad
 D_t=2^{\delta_t}\operatorname{odd}(t!),          \tag{12}
$$



where $s_2$ is binary digit sum.  Finally put



$$
\begin{aligned}
 \Lambda_n&=\left(\prod_{j=0}^{n-1}j!\right)^2,\\
 \Gamma_n&=\prod_{t=0}^{n-2}D_t,\\
 d_s&=\left\lfloor\frac{s-1}{4}\right\rfloor,
 \qquad \varepsilon_s=2d_s-s_2(d_s),\\
 \Omega_n^*&=\prod_{s=1}^{n-1}
  2^{\varepsilon_s}\operatorname{odd}((s-1)!),\\
 K_n&=\Lambda_n\Gamma_n\Omega_n^*,               \tag{13}
\end{aligned}
$$



with empty products interpreted as one.

### Theorem 1

Every signed maximal cofactor of $M_n$ is divisible by $K_n$.  Moreover



$$
\log K_n=2n^2\log n+O(n^2).                     \tag{14}
$$



### Proof

Delete any one column of $M_n$, and expand the resulting square
determinant along the endpoint row (9).  Each term is a $2n$-by-$2n$
high-jet determinant obtained after two columns of the original matrix have
been removed.

First, every high entry in either the $B_j$ or $C_j$ column contains
the explicit factor



$$
(k)_j=j!\binom{k}{j}.                            \tag{15}
$$



The multiset of these column factors before the two removals is
$\{j!,j!:0\le j\le n\}$.  The product left after any two removals is
divisible by the product obtained by removing the two largest factors,
namely $\Lambda_n$.

Second, index a $C_j$ column by $t=n-j$.  Its high entries have
$m=k-j\ge t+1$.  For a nonzero jet $m=4q+r$,
$r\in\{1,2,3\}$, (6) gives



$$
v_2(\tau_m)=2q+1-s_2(q),\qquad
 \operatorname{odd}((m-1)!)\mid\tau_m.           \tag{16}
$$



The dyadic quantity in (16) is strictly increasing with $q$.  If
$t+1$ is divisible by four, the first candidate jet is zero and the next
one has $q=q_t$.  Thus every high entry in this $C$-column is divisible
by $D_t$.  At least $n-1$ of the original $n+1$ $C$-columns remain
after two removals.  The $D_t$ form a divisibility chain, so the retained
product is divisible by $\Gamma_n$.

It remains to prove the extra row factor $\Omega_n^*$.  Index the high rows
by



$$
s=k-n\in\{1,\ldots,2n\}.
$$



For a retained $C$-column indexed by $t=n-j$, one has $m=s+t$.
After literally extracting $j!D_t$, its residual entry is



$$
\binom{n+s}{n-t}\frac{\tau_{s+t}}{D_t}.          \tag{17}
$$



For every odd prime $p$, a nonzero entry satisfies



$$
\begin{aligned}
 v_p\!\left(\frac{\tau_{s+t}}{D_t}\right)
 &=v_p((s+t-1)!)-v_p(t!)\\
 &\ge v_p((s-1)!),                                \tag{18}
\end{aligned}
$$



because



$$
\frac{(s+t-1)!}{t!(s-1)!}=\binom{s+t-1}{s-1}
$$



is an integer.  The binomial factor in (17) can only increase the
valuation.  Here equality in the first line of (18) uses both that
$\tau_{s+t}\ne0$ and that the odd part of $D_t$ is exactly
$\operatorname{odd}(t!)$; a zero jet is trivially divisible by all the
displayed factors.  Hence the residual entry in row $s$ is divisible by
$\operatorname{odd}((s-1)!)$.

There is also a forced dyadic part.  Write $t+1=4q+r$, with
$0\le r\le3$.  For a nonzero jet $m=s+t$,



$$
\left\lfloor\frac{m-1}{4}\right\rfloor-q
 =\left\lfloor\frac{s+r-2}{4}\right\rfloor
 \ge d_s.                                         \tag{18a}
$$



Indeed, the only residue that could lower the right side by one is exactly
the residue for which $m\equiv0\pmod4$, and that jet is zero.  Binary
digit sum is subadditive, so, for $d\ge d_s$,



$$
\begin{aligned}
 \bigl(2(q+d)+1-s_2(q+d)\bigr)
  -\bigl(2q+1-s_2(q)\bigr)
 &\ge 2d-s_2(d)\\
 &\ge 2d_s-s_2(d_s)=\varepsilon_s.               \tag{18b}
\end{aligned}
$$



The function $2d-s_2(d)$ is strictly increasing, since its increment is
one plus the number of trailing binary ones.  Thus the residual entry in
row $s$ is divisible by the full row factor



$$
2^{\varepsilon_s}\operatorname{odd}((s-1)!).    \tag{18c}
$$



Expand each high determinant by its retained $C$-columns.  Every term
assigns those columns to at least $n-1$ distinct high rows.  The odd
full row factors in (18c) form a divisibility chain, so their product is
divisible by the product of the $n-1$ smallest row factors, which is
$\Omega_n^*$.  The
three factors in (13) were extracted successively from the explicit
factorization (15)--(18), so there is no double counting even when they
share primes.  Thus every endpoint-row term, and hence every maximal
cofactor, is divisible by $K_n$.

Finally,



$$
\sum_{j<n}\log(j!)=\frac12n^2\log n+O(n^2),
$$



and removing or restoring the dyadic part of a factorial changes the sum
by only $O(n^2)$; the additional exponents $\varepsilon_s$ also sum to
$O(n^2)$.  Therefore $\Lambda_n$, $\Gamma_n$, and
$\Omega_n^*$ contribute respectively
$1,\tfrac12,\tfrac12$ times $n^2\log n$, proving (14). $\square$

### Consequence for primitive height

Assume $M_n$ has full row rank.  Expanding a maximal cofactor along its
endpoint row leaves high determinants with between $n-1$ and $n+1$
$C$-columns.  The column estimates



$$
\|B_j\|_2\le\sqrt{2n}(3n)^j,\qquad
 \|C_j\|_2\le4\sqrt{2n}(3n)!                    \tag{19}
$$



and Hadamard's inequality give



$$
\log|\text{raw maximal cofactor}|
 \le\frac72n^2\log n+O(n^2).                    \tag{20}
$$



The signed-cofactor kernel vector has a common divisor at least $K_n$.
After making that vector primitive,



$$
\boxed{\log H(B_n,C_n)\le
 \frac32n^2\log n+O(n^2).}                       \tag{21}
$$



Reconstructing $A_n$ by (10) and multiplying by $n!$ does not change
the leading term in (21).  This is sharper than applying one uniform entry
bound to the raw integer matrix.  It is still much too large to be defeated
by the fixed geometric analytic radius $\sqrt2$, and it says nothing
about the additional gcd of the endpoint pair.

## 4. Exact finite rank and endpoint theorem through degree 100

The reproducible certificate uses the prime



$$
p=65521.
$$



The script verifies its primality by deterministic trial division.  For
each $n$, it deletes the $B_0$ column of $M_n$.  If the resulting
square determinant is nonzero modulo $p$, then $M_n$ has full row rank
over $\mathbb Q$, and the kernel can be normalized by $B_0=1$ modulo
$p$.

### Theorem 2 (finite exact computation)

For every integer $1\le n\le100$:

1. the determinant of $M_n$ with its $B_0$ column deleted is nonzero
   modulo $65521$; hence $M_n$ has full row rank over $\mathbb Q$;
2. the first unconstrained jet, at index $3n+1$, is nonzero modulo
   $65521$, hence the endpoint-matched remainder has exact zero order
   $3n+1$;
3. for every $2\le n\le100$, both $A_n(1)$ and
   $B_n(1)=C_n(1)$ are nonzero modulo $65521$, hence are nonzero over
   $\mathbb Q$.

At $n=1$, the unique projective triple is



$$
A=2(1-z),\qquad B=-2(1-z),\qquad C=1-z,          \tag{22}
$$



so all three endpoint values are zero.  Its first free coefficient is
nonzero, so this is an endpoint degeneracy, not a rank degeneracy.

The modular calculation was independently cross-checked against exact
rational triples through $n=12$, including $A(1)$, $B(1)$, and the
first free jet.  The elimination determinant residues were also
cross-checked by direct exact determinant evaluation of the reduced
matrices through $n=5$.  This theorem is finite: it does not assert any
property for $n>100$.

The finite reduced endpoint forms are not small.  Their certified base-ten
decades for $n=2,3,\ldots,15$ are



$$
0,4,10,18,31,47,65,87,112,141,174,210,249,293. \tag{23}
$$



These data are diagnostic, not an asymptotic lower bound.

## 5. Exact endpoint tail and integral remainder

Let



$$
L=3n+1,\qquad \lambda=\frac{1+i}{2}.
$$



The logarithmic identity



$$
F(z)=-2i\bigl(\log(1-\overline\lambda z)
                 -\log(1-\lambda z)\bigr)        \tag{24}
$$



gives



$$
[z^m]F(z)=\frac{4\,\operatorname{Im}(\lambda^m)}m. \tag{25}
$$



For $M\ge1$, define



$$
\begin{aligned}
 E_M&=\sum_{m=M}^{\infty}\frac1{m!}
     =\frac1{(M-1)!}\int_0^1 e^{1-u}u^{M-1}\,du,\\
 T_M(\lambda)&=\sum_{m=M}^{\infty}\frac{\lambda^m}{m}
     =\lambda^M\int_0^1\frac{u^{M-1}}{1-\lambda u}\,du. \tag{26}
\end{aligned}
$$



Because all coefficients of $R_n$ below $L$ vanish and $L>n$, its
endpoint value has the exact tail representation



$$
\boxed{R_n(1)=
 \sum_{j=0}^n b_jE_{L-j}
 +4\sum_{j=0}^n c_j\operatorname{Im}T_{L-j}(\lambda).} \tag{27}
$$



In particular,



$$
|R_n(1)|\le
 e\sum_{j=0}^n\frac{|b_j|}{(L-j)!}
 +\frac4{1-2^{-1/2}}
  \sum_{j=0}^n\frac{|c_j|2^{-(L-j)/2}}{L-j}.      \tag{28}
$$



There is also the exact Taylor integral



$$
R_n(1)=\frac1{(3n)!}\int_0^1(1-t)^{3n}R_n^{(3n+1)}(t)\,dt. \tag{29}
$$



Here



$$
D^L(B_ne^z)=e^z(D+1)^LB_n,
$$



while $D^L(C_nF)$ is rational because $L>n$ and every surviving term
differentiates $F$ at least once.  Its denominator divides
$((z-1)^2+1)^L$.  Thus (29) is an elementary exponential-plus-rational
integral, but it is not a positive kernel in the computed family.  For
example, at $n=6$ and $n=8$ the sign of the first free Taylor
coefficient is opposite to the rigorously certified sign of $R_n(1)$.
Consequently first-term domination is false even at small degrees.

## 6. Reproducibility and frozen hashes

Exact rational/cofactor probe:

```text
scripts/mobius_arctan_hp_probe.py
results/mobius_arctan_hp_n15.json
```

Finite modular rank certificate:

```text
scripts/mobius_arctan_hp_modular_rank_certificate.py
results/mobius_arctan_hp_modular_rank_n100.json
```

At the time this note was frozen, the SHA-256 hashes of the latter two
files were

```text
e66d534729c80ceb49dbae5a70dcd15853bd6e70be030dc44cc0ca6804c3c78c  scripts/mobius_arctan_hp_modular_rank_certificate.py
07209359807ae3a578b940cb7644ca751f2af8dd6f236f8314abb8b67616bc60  results/mobius_arctan_hp_modular_rank_n100.json
```

The finite computation proves no all-degree statement and no result about
the arithmetic nature of $e+\pi$.
